"""Export the six existing club handouts and their solutions as styled PDFs.

Requires: reportlab, xhtml2pdf, PyMuPDF. Run after installing requirements:
    .venv/bin/python scripts/build_handout_pdfs.py
"""
from __future__ import annotations

from io import BytesIO
from pathlib import Path

import pymupdf as fitz
from lxml import etree, html as lxml_html
from xhtml2pdf import pisa

ROOT = Path(__file__).resolve().parents[1]
HANDOUTS = ROOT / "handouts"
OUTPUT = HANDOUTS / "pdf"
OUTPUT.mkdir(exist_ok=True)
SITE_URL = "https://mais-pac.github.io/"

ACCENTS = {
    "A1": ("#2457c5", "#1e3a8a"),
    "A2": ("#7540b8", "#4c1d95"),
    "A3": ("#0c8275", "#115e59"),
    "P1": ("#c23c68", "#9d174d"),
    "P2": ("#c16a20", "#92400e"),
    "P3": ("#2457c5", "#1e3a8a"),
}

BASE_CSS = r"""
@page { size: A4; margin: 52pt 48pt 48pt; }
@font-face { font-family: ClubSans; src: url("pdf/fonts/DejaVuSans.ttf"); }
@font-face { font-family: ClubSans; src: url("pdf/fonts/DejaVuSans-Bold.ttf"); font-weight: bold; }
body { margin: 0; padding: 0; color: #202938; font-family: ClubSans; font-size: 9.5pt; line-height: 1.45; }
.skip-link, .handout-bar, .sheet-nav, .site-footer { display: none; }
.running-head { display: none; }
.sheet-page { max-width: none; margin: 0; padding: 0; color: #202938; font-family: ClubSans; font-size: 10pt; line-height: 1.48; }
.sheet-title-block { margin: 0 0 14pt; padding: 13pt 15pt; text-align: left; background-color: #f3f6ff; border: 1pt solid #c7d2fe; border-left: 5pt solid ACCENT; }
.sheet-title-block h1 { margin: 0 0 5pt; color: DARKACCENT; font-family: ClubSans; font-size: 19pt; line-height: 1.22; }
.sheet-subtitle { margin: 0; color: #526079; font-size: 9.5pt; }
.sheet-intro { margin: 0 0 15pt; padding: 10pt 13pt; background-color: #f8f5ff; border: 1pt solid #ddd6fe; border-left: 4pt solid #7540b8; }
.sheet-intro p { margin: 0; }
.sheet-page h2 { margin: 19pt 0 8pt; padding: 6pt 9pt; color: DARKACCENT; font-family: ClubSans; font-size: 12pt; background-color: #f3f6ff; border: 1pt solid #d8e2fa; border-left: 4pt solid ACCENT; }
.sheet-page p { margin: 0 0 8pt; }
.problem, .solution, .remark, .thm { margin: 10pt 0; padding: 9pt 11pt; border: 1pt solid #dce4f2; }
.problem { background-color: #f4f8ff; border-color: #bfdbfe; border-left: 4pt solid #2563eb; }
.solution { background-color: #f0fdf7; border-color: #a7f3d0; border-left: 4pt solid #059669; }
.remark { background-color: #faf7ff; border-color: #ddd6fe; border-left: 4pt solid #7c3aed; }
.thm { background-color: #f5f5ff; border-color: #c7d2fe; border-left: 4pt solid #4338ca; }
.eq { margin: 8pt 0; padding: 7pt 8pt; text-align: center; background-color: #eff6ff; border: 1pt solid #bfdbfe; border-left: 4pt solid #2563eb; }
.eq__expr { text-align: center; font-family: ClubSans; font-size: 10pt; }
.eq__num { color: #526079; }
.frac { text-align: center; }
.subparts { list-style-type: none; list-style-image: none; margin-left: 17pt; padding-left: 0; }
.thm-head { color: #4338ca; font-weight: bold; }
.prob-head { color: #1d4ed8; font-weight: bold; }
.sol-head { color: #047857; font-weight: bold; }
.remark-head { color: #6d28d9; font-weight: bold; }
.subparts { margin: 5pt 0 8pt 17pt; padding-left: 0; }
.subparts li { margin: 3pt 0; }
.part-label { font-weight: bold; }
strong, b { font-weight: bold; }
i, em { font-style: italic; }
a { color: DARKACCENT; text-decoration: none; }
"""


def link_callback(uri: str, rel: str | None) -> str | None:
    if uri.startswith("file:///usr/share/fonts/truetype/dejavu/"):
        local = Path(uri.removeprefix("file://"))
        return str(local) if local.is_file() else None
    return None


def _inner_html(element) -> str:
    parts = [element.text or ""]
    for child in element:
        parts.append(etree.tostring(child, encoding="unicode", method="html", with_tail=False))
        parts.append(child.tail or "")
    return "".join(parts)


def _flatten_fractions(root) -> None:
    # xhtml2pdf does not support CSS grid, so serialize stacked HTML fractions
    # as clear inline numerator/denominator forms instead of losing the slash.
    fraction_nodes = root.xpath(
        ".//span[contains(concat(' ', normalize-space(@class), ' '), ' frac ')]"
    )
    for node in reversed(fraction_nodes):
        parts = node.findall("./span")
        if len(parts) != 2 or node.getparent() is None:
            continue
        replacement = lxml_html.fragment_fromstring(
            "<span>(" + _inner_html(parts[0]) + ")/ (" + _inner_html(parts[1]) + ")</span>"
        )
        replacement.tail = node.tail
        node.getparent().replace(node, replacement)


def pdf_html(source: Path, accent: str, dark: str) -> str:
    text = source.read_text(encoding="utf-8")
    css = BASE_CSS.replace("DARKACCENT", dark).replace("ACCENT", accent)
    root = lxml_html.fromstring(text)
    stylesheets = root.xpath("//link[@rel='stylesheet' and starts-with(@href, '../style.css')]")
    if not stylesheets:
        raise RuntimeError(f"Could not find site stylesheet link in {source}")
    style = lxml_html.Element("style")
    style.text = css
    stylesheets[0].getparent().replace(stylesheets[0], style)
    body = root.find("body")
    if body is not None:
        body.set("class", "pdf-export")
    _flatten_fractions(root)
    return lxml_html.tostring(root, encoding="unicode", doctype="<!doctype html>")


def add_masthead(pdf_bytes: bytes, code: str, accent: str, title: str) -> bytes:
    document = fitz.open(stream=pdf_bytes, filetype="pdf")
    rgb = tuple(int(accent[i:i + 2], 16) / 255 for i in (1, 3, 5))
    for page_number, page in enumerate(document, 1):
        width, height = page.rect.width, page.rect.height
        badge = fitz.Rect(47, 15, 116, 34)
        page.draw_rect(badge, color=rgb, fill=rgb, width=0)
        page.insert_text((53, 28), "MAIS PAC", fontname="helv", fontsize=8, color=(1, 1, 1))
        page.insert_link({"kind": fitz.LINK_URI, "from": badge, "uri": SITE_URL})
        page.insert_textbox(
            fitz.Rect(127, 16, width - 48, 34),
            f"{code}  ·  {title.upper()}",
            fontname="helv", fontsize=7.2, color=(0.32, 0.38, 0.48), align=2,
        )
        page.draw_line((47, 42), (width - 48, 42), color=rgb, width=1.1)
        page.draw_line((47, height - 39), (width - 48, height - 39), color=(0.84, 0.88, 0.93), width=0.6)
        page.insert_text((47, height - 24), "MAIS PAC  ·  mais-pac.github.io", fontname="helv", fontsize=7, color=(0.38, 0.43, 0.51))
        page.insert_text((width - 56, height - 24), str(page_number), fontname="helv", fontsize=7, color=(0.38, 0.43, 0.51))
    document.set_metadata({
        "title": title,
        "author": "MAIS Physics & Astronomy Club",
        "subject": "MAIS PAC physics and astronomy handout",
        "keywords": "MAIS PAC, physics, astronomy, handout",
    })
    return document.tobytes(garbage=4, deflate=True)


def main() -> None:
    built = 0
    for source in sorted(HANDOUTS.glob("*.html")):
        if source.name == "index.html":
            continue
        stem = source.stem
        code = stem.removesuffix("-solutions")
        if code not in ACCENTS:
            continue
        accent, dark = ACCENTS[code]
        kind = "Solutions" if stem.endswith("-solutions") else "Handout"
        output = OUTPUT / f"{stem}.pdf"
        rendered = BytesIO()
        result = pisa.CreatePDF(
            pdf_html(source, accent, dark),
            dest=rendered,
            path=str(source),
            encoding="utf-8",
            link_callback=link_callback,
        )
        if result.err:
            raise RuntimeError(f"Could not render {source.name}: {result.err}")
        pdf_bytes = add_masthead(rendered.getvalue(), code, accent, kind)
        output.write_bytes(pdf_bytes)
        built += 1
        print(f"Built {output.relative_to(ROOT)} ({len(pdf_bytes):,} bytes)")
    print(f"Built {built} handout PDFs in {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
