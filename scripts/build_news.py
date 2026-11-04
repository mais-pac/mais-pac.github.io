"""Build news/index.html from live astronomy/spaceflight feeds.

Run manually:
    python scripts/build_news.py

Run automatically:
    .github/workflows/daily-news.yml triggers this on a daily cron, then
    commits the result if anything changed. See that file for the schedule.

Data sources (both free, no account needed):
  - NASA APOD API           https://api.nasa.gov/planetary/apod
      -> powers the "Today's Cosmic Wonder" explainer: one real discovery or
         sky event, turned into one simple paragraph with a hook opener and
         closer (see scripts/news_data.py for the phrase pools).
  - Spaceflight News API v4 https://api.spaceflightnewsapi.net/v4/articles/
      -> powers the three auto-updated headline lists (astronomy, missions
         & rockets, Musk & SpaceX), sorted newest first and bucketed by
         keyword.

If either call fails (offline, API outage, rate limit, or a sandboxed run
with no network access) the script falls back to a hand-checked, real,
sourced dataset in scripts/news_data.py so the page is always complete and
never breaks or goes blank — only the "last refreshed" stamp changes.

Set the NASA_API_KEY environment variable to use your own NASA API key
instead of the shared DEMO_KEY (higher rate limit). Not required.
"""
from __future__ import annotations

import html
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

_KEYWORD_PATTERN_CACHE: dict[str, re.Pattern] = {}


def has_keyword(text: str, keyword: str) -> bool:
    """Whole-word(s) match, case-insensitive, so short keywords like "iss"
    or "star" cannot match inside unrelated words ("Missing", "started")."""
    pattern = _KEYWORD_PATTERN_CACHE.get(keyword)
    if pattern is None:
        pattern = re.compile(r"\b" + re.escape(keyword) + r"\b", re.IGNORECASE)
        _KEYWORD_PATTERN_CACHE[keyword] = pattern
    return bool(pattern.search(text))


def has_any_keyword(text: str, keywords) -> bool:
    return any(has_keyword(text, k) for k in keywords)


def esc(text: str) -> str:
    """Escape text for use inside HTML element content (keeps apostrophes
    and quotes readable in the generated source)."""
    return html.escape(text, quote=False)


def esc_attr(text: str) -> str:
    """Escape text for use inside an HTML attribute value."""
    return html.escape(text, quote=True)


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "scripts" / "news" / "template.html"
OUT = ROOT / "news" / "index.html"

sys.path.insert(0, str(ROOT / "scripts"))
import news_data as nd  # noqa: E402

REQUEST_TIMEOUT = 12
USER_AGENT = "mais-pac-news-builder/1.0 (+https://mais-pac.github.io/)"
ULAANBAATAR_OFFSET = timezone(timedelta(hours=8))


# ---------------------------------------------------------------------------
# Network helpers
# ---------------------------------------------------------------------------
def _get_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_apod():
    api_key = os.environ.get("NASA_API_KEY", "DEMO_KEY")
    url = "https://api.nasa.gov/planetary/apod?" + urllib.parse.urlencode({"api_key": api_key, "thumbs": "true"})
    try:
        data = _get_json(url)
        if not isinstance(data, dict) or "title" not in data or "explanation" not in data:
            raise ValueError("unexpected APOD response shape")
        return data
    except Exception as exc:  # noqa: BLE001 - any failure just falls back
        print(f"[build_news] NASA APOD fetch failed, using fallback hero: {exc}", file=sys.stderr)
        return None


def fetch_spaceflight_news(limit: int = 30):
    url = "https://api.spaceflightnewsapi.net/v4/articles/?" + urllib.parse.urlencode(
        {"limit": limit, "ordering": "-published_at"}
    )
    try:
        data = _get_json(url)
        results = data.get("results") if isinstance(data, dict) else None
        if not results:
            raise ValueError("no results in Spaceflight News API response")
        return results
    except Exception as exc:  # noqa: BLE001
        print(f"[build_news] Spaceflight News API fetch failed, using fallback headlines: {exc}", file=sys.stderr)
        return None


def wikipedia_lookup(query: str):
    """Best-effort: find a real Wikipedia page related to `query`. Returns
    (title, url) or None. Never raises."""
    try:
        url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode(
            {"action": "opensearch", "search": query, "limit": 1, "namespace": 0, "format": "json"}
        )
        data = _get_json(url)
        titles, _descs, urls = data[1], data[2], data[3]
        if titles and urls:
            return titles[0], urls[0]
    except Exception:  # noqa: BLE001
        pass
    return None


# ---------------------------------------------------------------------------
# "Today's Cosmic Wonder" builder
# ---------------------------------------------------------------------------
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def simplify_explanation(explanation: str, max_sentences: int = 2) -> str:
    """Trim a (sometimes technical) APOD paragraph down to its first couple
    of sentences, which is normally where the plain "what is this" fact
    lives, and strip inline citation clutter."""
    text = re.sub(r"\s+", " ", explanation).strip()
    sentences = [s.strip() for s in SENTENCE_SPLIT.split(text) if s.strip()]
    core = " ".join(sentences[:max_sentences]) if sentences else text
    # Keep it readable: cap length even if sentences are long.
    if len(core) > 420:
        core = core[:420].rsplit(" ", 1)[0] + "…"
    return core


def pick_by_date(pool: list[str], d: datetime) -> str:
    index = d.timetuple().tm_yday % len(pool)
    return pool[index]


def build_hero(apod: dict | None, build_date: datetime) -> dict:
    if apod is None:
        hero = dict(nd.FALLBACK_HERO)
        hero["further_reading"] = dict(hero["further_reading"])
        hero["reference"] = dict(hero["reference"])
        return hero

    title = html.unescape(apod.get("title", "Today's sky")).strip()
    explanation = html.unescape(apod.get("explanation", "")).strip()
    date_str = apod.get("date", build_date.strftime("%Y-%m-%d"))
    try:
        apod_date = datetime.strptime(date_str, "%Y-%m-%d")
        date_display = f"{apod_date.day} {apod_date.strftime('%B')} {apod_date.year}"
        permalink_date = apod_date.strftime("%Y-%m-%d")
    except ValueError:
        apod_date = build_date
        date_display = f"{build_date.day} {build_date.strftime('%B')} {build_date.year}"
        permalink_date = build_date.strftime("%Y-%m-%d")

    opener = pick_by_date(nd.HOOK_OPENERS, apod_date)
    closer = pick_by_date(nd.HOOK_CLOSERS, apod_date)
    core = simplify_explanation(explanation)
    paragraph = f"{opener} {core} {closer}"

    further_reading = {
        "url": f"https://apod.nasa.gov/apod/ap{permalink_date[2:4]}{permalink_date[5:7]}{permalink_date[8:10]}.html",
        "label": f"NASA Astronomy Picture of the Day, {date_display}",
    }

    reference = None
    hit = wikipedia_lookup(title)
    if hit:
        reference = {"url": hit[1], "label": f"Wikipedia: {hit[0]}"}
    else:
        lowered = (title + " " + explanation).lower()
        reference = _match_reference(lowered)

    image_url = apod.get("url") if apod.get("media_type") == "image" else None

    return {
        "date": date_display,
        "title": title,
        "paragraph": paragraph,
        "image_url": image_url,
        "image_alt": title,
        "further_reading": further_reading,
        "reference": reference,
    }


def render_hero_figure(hero: dict) -> str:
    if not hero.get("image_url"):
        return ""
    alt = esc_attr(hero.get("image_alt", hero["title"]))
    return (
        '<figure class="cw-figure">'
        f'<img src="{esc_attr(hero["image_url"])}" alt="{alt}" loading="lazy" width="640" height="420">'
        "</figure>"
    )


def render_hero(hero: dict) -> dict:
    return {
        "HERO_DATE": esc(hero["date"]),
        "HERO_TITLE": esc(hero["title"]),
        "HERO_PARAGRAPH": esc(hero["paragraph"]),
        "HERO_FURTHER_URL": esc_attr(hero["further_reading"]["url"]),
        "HERO_FURTHER_LABEL": esc(hero["further_reading"]["label"]),
        "HERO_REFERENCE_URL": esc_attr(hero["reference"]["url"]),
        "HERO_REFERENCE_LABEL": esc(hero["reference"]["label"]),
        "HERO_FIGURE": render_hero_figure(hero),
        "HERO_CARD_MODIFIER": "" if hero.get("image_url") else "no-image",
    }


# ---------------------------------------------------------------------------
# Headline list builder
# ---------------------------------------------------------------------------
def _match_reference_in(text: str):
    for keywords, url, label in nd.REFERENCE_MAP:
        if has_any_keyword(text, keywords):
            return {"url": url, "label": label}
    return None


def _match_reference(lowered_text: str):
    """Kept for the fallback dataset, where title+summary together are the
    only signal available."""
    return _match_reference_in(lowered_text) or dict(zip(("url", "label"), nd.DEFAULT_REFERENCE))


def pick_reference(title: str, summary: str) -> dict:
    """Prefer a match found in the title (the main topic) over one only
    found in the summary (which may just mention something in passing)."""
    match = _match_reference_in(title.lower())
    if match is None:
        match = _match_reference_in(f"{title} {summary}".lower())
    if match is None:
        url, label = nd.DEFAULT_REFERENCE
        match = {"url": url, "label": label}
    return match


def classify_bucket(title: str, summary: str) -> str:
    combined = f"{title} {summary}"
    if has_any_keyword(combined, nd.MUSK_KEYWORDS):
        return "musk"
    if has_any_keyword(combined, nd.MISSION_KEYWORDS):
        return "mission"
    return "astro"


def format_published(published_at: str, fallback: datetime) -> str:
    try:
        d = datetime.strptime(published_at[:10], "%Y-%m-%d")
    except (ValueError, TypeError):
        d = fallback
    return f"{d.day} {d.strftime('%B')} {d.year}"


def build_buckets_from_api(articles: list[dict], build_date: datetime, per_bucket: int = 5):
    buckets: dict[str, list[dict]] = {"astro": [], "mission": [], "musk": []}
    for art in articles:
        title = html.unescape((art.get("title") or "").strip())
        summary = html.unescape((art.get("summary") or "").strip())
        url = art.get("url")
        site = art.get("news_site") or "source"
        if not title or not url:
            continue
        bucket = classify_bucket(title, summary)
        if len(buckets[bucket]) >= per_bucket:
            continue
        if len(summary) > 320:
            summary = summary[:320].rsplit(" ", 1)[0] + "…"
        reference = pick_reference(title, summary)
        item = {
            "date": format_published(art.get("published_at", ""), build_date),
            "title": title,
            "summary": summary,
            "sources": [{"label": site, "url": url}],
            "reference": reference,
        }
        buckets[bucket].append(item)
    return buckets


def build_buckets_from_fallback():
    buckets: dict[str, list[dict]] = {"astro": [], "mission": [], "musk": []}
    for art in nd.FALLBACK_ARTICLES:
        reference = pick_reference(art["title"], art["summary"])
        item = dict(art)
        item["reference"] = reference
        buckets[art["bucket"]].append(item)
    return buckets


def render_item(item: dict) -> str:
    source_links = " · ".join(
        f'<a href="{esc_attr(s["url"])}" target="_blank" rel="noopener">{esc(s["label"])} ↗</a>'
        for s in item["sources"]
    )
    existing_urls = {s["url"] for s in item["sources"]}
    ref = item.get("reference")
    ref_html = ""
    if ref and ref["url"] not in existing_urls:
        ref_html = (
            ' &nbsp;·&nbsp; <a class="news-ref" href="'
            f'{esc_attr(ref["url"])}" target="_blank" rel="noopener">Reference: {esc(ref["label"])} ↗</a>'
        )
    return (
        "          <li>\n"
        f'            <span class="news-date">{esc(item["date"])}</span>\n'
        f"            <h4>{esc(item['title'])}</h4>\n"
        f"            <p>{esc(item['summary'])}</p>\n"
        f'            <p class="news-src">Read more: {source_links}{ref_html}</p>\n'
        "          </li>"
    )


def render_bucket(items: list[dict]) -> str:
    if not items:
        return "          <li><p>No fresh items in this category today — check back tomorrow.</p></li>"
    return "\n".join(render_item(item) for item in items)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    build_date = datetime.now(timezone.utc)
    ulan_time = build_date.astimezone(ULAANBAATAR_OFFSET)
    last_updated = (
        f"{ulan_time.day} {ulan_time.strftime('%B')} {ulan_time.year} · "
        f"{ulan_time.strftime('%H:%M')} Ulaanbaatar time"
    )

    apod = fetch_apod()
    hero = build_hero(apod, build_date)

    articles = fetch_spaceflight_news()
    if articles:
        buckets = build_buckets_from_api(articles, build_date)
        # Guard against a thin/odd API response: if every bucket is empty,
        # the keyword classifier probably has nothing to work with — fall
        # back rather than publish three empty sections.
        if not any(buckets.values()):
            buckets = build_buckets_from_fallback()
    else:
        buckets = build_buckets_from_fallback()

    template = TEMPLATE.read_text(encoding="utf-8")
    replacements = {
        "{{LAST_UPDATED}}": esc(last_updated),
        "{{ASTRO_ITEMS}}": render_bucket(buckets["astro"]),
        "{{MISSION_ITEMS}}": render_bucket(buckets["mission"]),
        "{{MUSK_ITEMS}}": render_bucket(buckets["musk"]),
    }
    for key, value in render_hero(hero).items():
        replacements[f"{{{{{key}}}}}"] = value

    out_html = template
    for placeholder, value in replacements.items():
        out_html = out_html.replace(placeholder, value)

    OUT.write_text(out_html, encoding="utf-8")
    print(f"Built {OUT.relative_to(ROOT)} ({len(out_html):,} characters) — last refreshed {last_updated}")


if __name__ == "__main__":
    main()
