"""Export the IPhO curriculum handouts (lecture + solutions) as styled PDFs.

Reuses the print styling, fraction flattening and masthead from
`build_handout_pdfs.py`, but the curriculum sheets inline their own stylesheet
and carry their figures as inline SVG, so they are cleaned up first:

* `<script>`, controls and the interactive canvas are removed (they print blank);
* each interactive lab is replaced by a short static note;
* the sheet's own `<style>` blocks are kept, the print CSS is appended.

Run after building the HTML:

    .venv/bin/python scripts/build_ipho_curriculum.py
    .venv/bin/python scripts/build_ipho_pdfs.py [code ...]
"""
from __future__ import annotations

import base64
import sys
from io import BytesIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pymupdf as fitz  # noqa: E402
from lxml import etree  # noqa: E402
from lxml import html as lxml_html  # noqa: E402
from xhtml2pdf import pisa  # noqa: E402

from build_handout_pdfs import (  # noqa: E402
    BASE_CSS,
    IPHO_ACCENTS,
    OUTPUT,
    ROOT,
    _flatten_fractions,
    add_masthead,
)
from ipho_topics import TOPICS  # noqa: E402


def clean(root) -> None:
    """Drop everything that only exists for the browser."""
    for node in root.xpath("//script | //button | //input | //select | //output"):
        node.getparent().remove(node)
    for lab in root.xpath("//section[contains(@class,'cosmo-lab')]"):
        title = lab.xpath(".//h3")
        heading = title[0].text_content().strip() if title else "Interactive experiment"
        note = lxml_html.fragment_fromstring(
            '<p class="ipho-pdf-note"><em>Interactive experiment: '
            + heading
            + ' — open the online handout to use it.</em></p>'
        )
        note.tail = lab.tail
        lab.getparent().replace(lab, note)
    # the quick-link row and the navigation bar are screen furniture
    for node in root.xpath("//div[contains(@class,'cosmo-quicklinks')] | //nav[contains(@class,'sheet-nav')]"):
        node.getparent().remove(node)
    # KaTeX duplicates every formula as MathML for screen readers; keeping both
    # makes xhtml2pdf print the raw TeX as well as the typeset form.
    for node in root.xpath("//*[contains(@class,'katex-mathml')]"):
        node.getparent().remove(node)


SUPS = str.maketrans("0123456789+-n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻ⁿ")
SUBS = str.maketrans("0123456789+-", "₀₁₂₃₄₅₆₇₈₉₊₋")


SYMBOLS = {
    "cdot": "·", "times": "×", "approx": "≈", "to": "→", "rightarrow": "→", "neq": "≠",
    "leq": "≤", "geq": "≥", "pm": "±", "mp": "∓", "Delta": "Δ", "delta": "δ",
    "theta": "θ", "omega": "ω", "mu": "μ", "pi": "π", "rho": "ρ", "sigma": "σ",
    "tau": "τ", "phi": "φ", "Omega": "Ω", "lambda": "λ", "alpha": "α", "beta": "β",
    "gamma": "γ", "epsilon": "ε", "varepsilon": "ε", "infty": "∞", "int": "∫",
    "sum": "Σ", "propto": "∝", "ll": "≪", "gg": "≫", "circ": "°", "prime": "′",
    "qquad": "   ", "quad": "  ", ",": " ", ";": " ", "!": "", " ": " ",
    "left": "", "right": "", "big": "", "Big": "", "text": "", "mathrm": "",
    "mathbf": "", "mathit": "", "operatorname": "", "hat": "", "bar": "", "vec": "",
    "overline": "", "dot": "", "tilde": "",
}
FUNCS = {"sin", "cos", "tan", "ln", "log", "exp", "lim", "max", "min"}


def _read_atom(text, i):
    """Return (rendered, index after) for one TeX atom starting at i."""
    if i >= len(text):
        return "", i
    ch = text[i]
    if ch == "{":
        depth, j = 0, i
        while j < len(text):
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
                if depth == 0:
                    return tex_to_text(text[i + 1:j]), j + 1
            j += 1
        return tex_to_text(text[i + 1:]), len(text)
    if ch == "\\":
        j = i + 1
        while j < len(text) and text[j].isalpha():
            j += 1
        if j == i + 1:
            j = i + 2
        return tex_to_text(text[i:j]), j
    return ch, i + 1


def tex_to_text(tex: str) -> str:
    """Turn a KaTeX annotation back into a compact linear formula."""
    import re
    out = []
    i = 0
    while i < len(tex):
        ch = tex[i]
        if ch == "^":
            atom, j = _read_atom(tex, i + 1)
            clean = atom.strip()
            if clean in ("2", "3"):
                out.append({"2": "²", "3": "³"}[clean])
            else:
                out.append("^(" + clean + ")" if len(clean) > 1 else "^" + clean)
            i = j
            continue
        if ch == "_":
            atom, j = _read_atom(tex, i + 1)
            clean = atom.strip()
            out.append("_" + clean if len(clean) == 1 else "_(" + clean + ")")
            i = j
            continue
        if ch == "\\":
            j = i + 1
            while j < len(tex) and tex[j].isalpha():
                j += 1
            name = tex[i + 1:j] if j > i + 1 else tex[i + 1:i + 2]
            if name in ("frac", "dfrac", "tfrac"):
                a, j2 = _read_atom(tex, j)
                b, j3 = _read_atom(tex, j2)
                out.append("(" + a + ")/(" + b + ")")
                i = j3
                continue
            if name == "sqrt":
                a, j2 = _read_atom(tex, j)
                out.append("√(" + a + ")")
                i = j2
                continue
            if name in FUNCS:
                a, j2 = _read_atom(tex, j)
                out.append(name + " " + a)
                i = j2
                continue
            out.append(SYMBOLS.get(name, ""))
            i = j
            continue
        out.append(ch)
        i += 1
    flat = "".join(out).replace("\\\\", " ").replace("\\,", " ").replace("\\;", " ").replace("\\ ", " ")
    flat = flat.replace("\\", "")
    flat = re.sub(r"\s+", " ", flat).strip()
    flat = re.sub(r"\s+([,.;:)])", r"\1", flat)
    return flat


def flatten_mathml(root) -> None:
    """Replace every KaTeX rendering by a readable linear form of its TeX."""
    for node in reversed(root.xpath(
            "//*[contains(@class,'katex')][not(ancestor::*[contains(@class,'katex')])]")):
        ann = node.xpath(".//annotation")
        if not ann:
            continue
        text = tex_to_text(ann[0].text_content())
        span = lxml_html.fragment_fromstring('<span>' + text + '</span>')
        span.tail = node.tail
        node.getparent().replace(node, span)


def rasterise(root, dpi: int = 150) -> None:
    """xhtml2pdf cannot draw inline SVG, so embed each figure as a PNG."""
    for index, svg in enumerate(root.xpath("//svg")):
        box = svg.get("viewBox", "0 0 680 300").split()
        width, height = float(box[2]), float(box[3])
        markup = lxml_html.tostring(svg, encoding="unicode")
        try:
            doc = fitz.open(stream=markup.encode("utf-8"), filetype="svg")
            pix = doc[0].get_pixmap(dpi=dpi)
            png = pix.tobytes("png")
        except Exception as exc:  # pragma: no cover - defensive
            print(f"  ! could not rasterise svg {index}: {exc}")
            continue
        img = lxml_html.fragment_fromstring(
            f'<img src="data:image/png;base64,{base64.b64encode(png).decode()}" '
            f'width="{min(500.0, width * 0.74):.0f}" height="{min(500.0, width * 0.74) * height / width:.0f}" alt="figure"/>'
        )
        img.tail = svg.tail
        svg.getparent().replace(svg, img)


def pdf_html(source: Path, accent: str, dark: str) -> str:
    root = lxml_html.fromstring(source.read_text(encoding="utf-8"))
    flatten_mathml(root)
    clean(root)
    rasterise(root)
    css = BASE_CSS.replace("DARKACCENT", dark).replace("ACCENT", accent)
    head = root.find("head")
    style = lxml_html.Element("style")
    style.text = css
    head.append(style)
    body = root.find("body")
    if body is not None:
        body.set("class", "pdf-export")
    _flatten_fractions(root)
    return lxml_html.tostring(root, encoding="unicode", doctype="<!doctype html>")


def main(codes=None) -> None:
    built = 0
    for topic in TOPICS:
        code = topic["code"]
        if codes and code not in codes:
            continue
        group = int(code.split(".")[0])
        accent, dark = IPHO_ACCENTS[(group - 1) % len(IPHO_ACCENTS)]
        for suffix, kind in (("", "Handout"), ("-solutions", "Solutions")):
            source = ROOT / "handouts" / f"{code}{suffix}.html"
            if not source.exists():
                print(f"{source.name}  (missing — skipped)")
                continue
            rendered = BytesIO()
            result = pisa.CreatePDF(pdf_html(source, accent, dark), dest=rendered,
                                    path=str(source), encoding="utf-8")
            if result.err:
                raise RuntimeError(f"Could not render {source.name}: {result.err}")
            pdf_bytes = add_masthead(rendered.getvalue(), f"IPhO {code}", accent, kind)
            output = OUTPUT / f"ipho-{code}{suffix}.pdf"
            output.write_bytes(pdf_bytes)
            built += 1
            print(f"Built {output.relative_to(ROOT)} ({len(pdf_bytes):,} bytes)")
    print(f"Built {built} IPhO PDFs in {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main(set(sys.argv[1:]) or None)
