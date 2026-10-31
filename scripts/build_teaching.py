"""Build the Teaching page and its styled PDFs.

Run from the repository root with:
    .venv/bin/python scripts/build_teaching.py

The lecture PDFs are original MAIS PAC theory notes followed by official IOAA
exam identifiers only. Copyrighted IOAA question statements are not copied.
"""
from pathlib import Path
from html import escape
import re

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak,
)

from lecture_content import LECTURES
from question_sets import SETS

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "teaching"
PDF = OUT / "pdf"
PDF.mkdir(exist_ok=True)
SITE_URL = "https://mais-pac.github.io/"
SYLLABUS_SOURCE = "https://www.ioaa2026.vn/en/ioaa-syllabus"
PAGE_W, PAGE_H = 595.28, 841.89
LEFT, RIGHT = 60, 535
CONTENT_W = RIGHT - LEFT

# Syllabus content and colors used by the curriculum PDF.
groups = []
for line in (OUT / "syllabus-topics.txt").read_text().splitlines():
    if line.startswith("# "):
        groups.append((line[2:], []))
    elif line.strip():
        name, detail = line.split(" | ", 1)
        groups[-1][1].append((name, detail))

notes = [
    "Extensive contents in basic astronomical concepts are required in theoretical and practical problems.",
    "Basic concepts in physics and mathematics at high school level are required in solving the problems. Standard solutions should not involve use of complex numbers and/or solving differential equations.",
    "Astronomical software packages may be used in practical and observational problems. The contestants will be informed the list of software packages to be used at least 3 months in advance. The chosen software packages should be preferably freeware or low-cost ones enabling all countries to obtain them easily for practice purpose. The chosen software should preferably be available on multiple OSs (Windows / Unix / GNU-Linux / Mac).",
    "Concepts and phenomena not included in the Syllabus may be used in questions but sufficient information must be given in the questions so that contestants without previous knowledge of these topics would not be at a disadvantage.",
    "Sophisticated practical equipment likely to be unfamiliar to the candidates should not dominate a problem. If such devices are used in the questions, sufficient information must be provided. In such cases, students should be given opportunity to familiarise themselves with the equipment before the exam.",
    "The original text of the problems must use SI units, wherever applicable. Participants will be expected to give appropriate units in their answers and should be familiar with the idea of correct rounding off and expressing the final result(s) and error(s) with the correct number of significant digits.",
    "A standard table of constants (supplied as a supplement to this Syllabus) shall be used when setting questions and provided to the students. Additional constants may be added to specific questions as required.",
]
faqs = [
    ("What is the Cosmic Calculation Series?", "A collection of astronomy learning materials organized around the IOAA syllabus, intended to support physical understanding and curiosity about the universe."),
    ("What is available for Basic Astrophysics?", "Each of the five Basic Astrophysics topics has a theory-first lecture PDF followed by an index of official past-paper problem identifiers. The question statements themselves are not reproduced. Original club practice exercises are available for the two Coordinates and Times topics."),
    ("Are solutions available?", "The Solutions PDFs are styled placeholders while worked solutions are being prepared."),
    ("What background does the syllabus require?", "The IOAA syllabus requires high-school physics and mathematics. Standard solutions should not require complex numbers or solving differential equations. The listed mathematical methods include basic calculus."),
    ("What does (Q) mean?", "Qualitative understanding only. Quantitative reasoning or proficiency in topics marked (Q) is not mandatory."),
    ("Is this an official IOAA publication?", "No. This is a MAIS PAC study resource. The syllabus PDF is a reformatted study edition of the syllabus; the topic codes and practical-topic labels are club organizational aids."),
    ("Where are the existing club handouts?", "The introductory physics and astronomy sheets, their solutions, and downloadable PDF versions are linked in the Teaching page's Existing club handouts section."),
]

# Embedded Unicode fonts preserve Greek letters, units and mathematical symbols.
FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
for font_name, file_name in [
    ("Club", "DejaVuSans.ttf"),
    ("ClubBold", "DejaVuSans-Bold.ttf"),
    ("ClubMono", "DejaVuSansMono.ttf"),
]:
    pdfmetrics.registerFont(TTFont(font_name, str(FONT_DIR / file_name)))
pdfmetrics.registerFontFamily(
    "Club", normal="Club", bold="ClubBold", italic="Club", boldItalic="ClubBold"
)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="Text", fontName="Club", fontSize=9.35, leading=14.2,
    textColor=colors.HexColor("#263244"), spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="TitleClub", fontName="ClubBold", fontSize=25, leading=31,
    textColor=colors.HexColor("#172554"), spaceAfter=8,
))
styles.add(ParagraphStyle(
    name="BoxHead", fontName="ClubBold", fontSize=10, leading=13,
    textColor=colors.white,
))
styles.add(ParagraphStyle(
    name="TopicHead", fontName="ClubBold", fontSize=10, leading=14,
    textColor=colors.HexColor("#172554"), spaceAfter=5,
))
styles.add(ParagraphStyle(
    name="SmallClub", fontName="Club", fontSize=7.8, leading=11,
    textColor=colors.HexColor("#536078"), spaceAfter=7,
))
styles.add(ParagraphStyle(
    name="FormulaClub", fontName="ClubMono", fontSize=9.2, leading=14,
    alignment=1, textColor=colors.HexColor("#172554"),
))
styles.add(ParagraphStyle(
    name="QuestionTitle", fontName="ClubBold", fontSize=11, leading=15,
    textColor=colors.HexColor("#244bc1"), spaceBefore=12, spaceAfter=5,
    keepWithNext=True,
))
styles.add(ParagraphStyle(
    name="ContentsEntry", fontName="ClubBold", fontSize=9.5, leading=15,
    textColor=colors.HexColor("#244bc1"),
))
styles.add(ParagraphStyle(
    name="CalloutBody", fontName="Club", fontSize=8.9, leading=13.2,
    textColor=colors.HexColor("#273449"),
))

PALETTE = ["#244bc1", "#6d28a4", "#08756e", "#b54221"]
INK = colors.HexColor("#172554")
PALE = colors.HexColor("#f3f6ff")
LINE = colors.HexColor("#d8e0ef")


def color(value):
    return colors.HexColor(value)


def p(text, style="Text"):
    return Paragraph(escape(str(text)), styles[style])


def heading(text, accent):
    table = Table([[p(text, "BoxHead")]], colWidths=[CONTENT_W])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color(accent)),
        ("BOX", (0, 0), (-1, -1), 0.5, color(accent)),
        ("LEFTPADDING", (0, 0), (-1, -1), 11),
        ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    table.keepWithNext = True
    return table


def callout(label, text, accent):
    table = Table(
        [[p(label.upper(), "BoxHead")], [p(text, "CalloutBody")]],
        colWidths=[CONTENT_W],
    )
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), color(accent)),
        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#f5f7ff")),
        ("BOX", (0, 0), (-1, -1), 0.7, color(accent)),
        ("LINEBEFORE", (0, 0), (0, -1), 3, color(accent)),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 1), (-1, 1), 8),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 8),
    ]))
    return table


def formula_box(text, accent):
    table = Table([[Paragraph(escape(text), styles["FormulaClub"])]], colWidths=[CONTENT_W])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#f2f6ff")),
        ("BOX", (0, 0), (-1, -1), 0.8, color(accent)),
        ("LINEBEFORE", (0, 0), (0, -1), 3, color(accent)),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return table


def page_furniture(canvas, doc):
    """Repeat a clickable MAIS PAC masthead and folio on every PDF page."""
    accent = getattr(doc, "accent_color", PALETTE[0])
    header_label = getattr(doc, "header_label", "TEACHING RESOURCES")
    canvas.saveState()
    x, y, w, h = LEFT, PAGE_H - 34, 67, 18
    canvas.setFillColor(INK)
    canvas.roundRect(x, y, w, h, 4, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("ClubBold", 8)
    canvas.drawCentredString(x + w / 2, y + 5.5, "MAIS PAC")
    canvas.linkURL(SITE_URL, (x, y, x + w, y + h), relative=0, thickness=0)
    canvas.setFillColor(colors.HexColor("#526079"))
    canvas.setFont("Club", 7.5)
    canvas.drawRightString(RIGHT, PAGE_H - 27, header_label[:62])
    canvas.setStrokeColor(color(accent))
    canvas.setLineWidth(1.5)
    canvas.line(LEFT, PAGE_H - 43, RIGHT, PAGE_H - 43)
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(LEFT, 43, RIGHT, 43)
    canvas.setFont("Club", 7.5)
    canvas.setFillColor(colors.HexColor("#64748b"))
    canvas.drawString(LEFT, 29, "MAIS PAC  ·  mais-pac.github.io")
    canvas.drawRightString(RIGHT, 29, str(doc.page))
    canvas.restoreState()


def write_pdf(path, title, story, accent=PALETTE[0], header_label="TEACHING RESOURCES"):
    doc = SimpleDocTemplate(
        str(path), pagesize=(PAGE_W, PAGE_H),
        rightMargin=PAGE_W - RIGHT, leftMargin=LEFT, topMargin=60, bottomMargin=60,
        title=title, author="MAIS Physics & Astronomy Club",
    )
    doc.accent_color = accent
    doc.header_label = header_label
    doc.build(story, onFirstPage=page_furniture, onLaterPages=page_furniture)


def problem_reference_card(index, year, round_name, label, accent):
    ident = f"IOAA {year}  ·  {round_name} {label}"
    content = Table([[p(f"{index:02d}", "BoxHead"), p(ident, "ContentsEntry")]], colWidths=[32, CONTENT_W - 32])
    content.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), color(accent)),
        ("BACKGROUND", (1, 0), (1, 0), colors.HexColor("#f6f8ff")),
        ("BOX", (0, 0), (-1, -1), 0.55, LINE),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ALIGN", (0, 0), (0, 0), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return content


def write_lecture(code, lecture):
    refs = lecture["problem_ids"]
    if not 15 <= len(refs) <= 30:
        raise ValueError(f"{code} needs 15–30 problem identifiers; found {len(refs)}")

    accent = lecture["accent"]
    title = lecture["title"]
    story = [
        p(f"{code}  ·  THEORY + PAST-PAPER INDEX", "SmallClub"),
        p(title, "TitleClub"),
        p(lecture["subtitle"], "TopicHead"),
        callout("Start here", lecture["intro"], accent),
        Spacer(1, 12),
        heading("LEARNING GOALS", accent),
    ]
    outcomes = [[p("✓", "TopicHead"), p(item, "Text")] for item in lecture["outcomes"]]
    outcome_table = Table(outcomes, colWidths=[24, CONTENT_W - 24])
    outcome_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#eef3ff")),
        ("BOX", (0, 0), (-1, -1), 0.55, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (0, 0), (0, -1), "CENTER"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
    ]))
    story.extend([outcome_table, Spacer(1, 15)])

    for section in lecture["sections"]:
        story.append(heading(section["title"], accent))
        for kind, *values in section["blocks"]:
            if kind == "text":
                story.append(p(values[0]))
                story.append(Spacer(1, 2))
            elif kind == "formula":
                story.extend([formula_box(values[0], accent), Spacer(1, 8)])
            elif kind == "callout":
                story.extend([callout(values[0], values[1], accent), Spacer(1, 9)])
            else:
                raise ValueError(f"Unknown lecture block type: {kind}")
        story.append(Spacer(1, 7))

    story.extend([
        PageBreak(),
        heading("PAST IOAA PROBLEM REFERENCES", accent),
        p("The following questions are from official past IOAA problem sets."),
        p("Use each year, round and question label to locate the original problem in its official paper.", "SmallClub"),
        Spacer(1, 5),
    ])
    for index, (year, round_name, label) in enumerate(refs, 1):
        story.extend([problem_reference_card(index, year, round_name, label, accent), Spacer(1, 5)])

    filename = PDF / f"{code}-problems.pdf"
    write_pdf(
        filename,
        f"{code} {title} — Theory and Past IOAA Problem Index",
        story, accent=accent, header_label=f"{code}  ·  THEORY + PROBLEM INDEX",
    )


def write_questions(code, name, accent):
    questions = SETS[code]
    story = [
        p("COSMIC CALCULATION SERIES  /  ORIGINAL PRACTICE", "SmallClub"),
        p(name, "TitleClub"),
        p(f"{code}  ·  Original club practice problems", "TopicHead"),
        p("Show your reasoning, use SI units where appropriate, and state any assumptions. Constants are supplied in the questions that need them."),
        heading("CONTENTS", accent),
    ]
    for i, (title, _) in enumerate(questions, 1):
        story.append(Paragraph(f'<link href="#q{i}" color="{accent}">{i:02d}  {escape(title)}</link>', styles["ContentsEntry"]))
        story.append(Spacer(1, 7))
    story.extend([
        Spacer(1, 15),
        p("These are original MAIS PAC practice exercises, not official IOAA problems.", "SmallClub"),
        PageBreak(), heading("PROBLEMS", accent),
    ])
    for i, (title, question) in enumerate(questions, 1):
        story.append(Paragraph(f'<a name="q{i}"/><font color="{accent}">{i:02d}  {escape(title)}</font>', styles["QuestionTitle"]))
        story.append(p(question))
        story.append(Spacer(1, 7))
    write_pdf(
        PDF / f"{code}-problems.pdf", f"{name} — Original Problems", story,
        accent=accent, header_label=f"{code}  ·  ORIGINAL PRACTICE",
    )


# Build the IOAA syllabus PDF with the same clickable masthead and boxed style.
story = [
    p("IOAA Syllabus", "TitleClub"),
    p("A study edition  ·  MAIS Physics & Astronomy Club", "TopicHead"),
    p("Reformatted from the IOAA 2026 website. Source credits IOAA; updated 17 November 2021. Topic wording is preserved with minor punctuation and typography normalization. Club topic codes and practical-topic labels are organizational aids, not official designations.", "SmallClub"),
    Paragraph(f'<link href="{SYLLABUS_SOURCE}" color="#244bc1">Official source: IOAA 2026 syllabus</link>', styles["Text"]),
    heading("GENERAL NOTES", PALETTE[0]),
]
for i, note in enumerate(notes, 1):
    story.append(p(f"{i}. {note}"))
story.extend([
    heading("THEORETICAL PART", PALETTE[1]),
    p("Symbol (Q) is attached to some topics in the list. It means qualitative understanding only. Quantitative reasoning or proficiency in these topics is not mandatory. The following theoretical contents are proposed for contestants."),
])
blocks = []
for gi, (group, topics) in enumerate(groups):
    if gi == 8:
        story.extend([
            PageBreak(), p("PRACTICAL PART", "TitleClub"),
            p("This part consists of observations and data-analysis sections. The theoretical part of the Syllabus provides the basis for all practical problems."),
            p("The observations section focuses on contestants' experience in:"),
        ])
    if gi == 9:
        story.extend([
            p("Observational objects may be real sources in the sky or imitated sources in the laboratory."),
            p("Computer simulations may be used, with sufficient instructions provided to contestants."),
            p("The data-analysis section focuses on calculation and analysis of astronomical data provided in the problems."),
        ])
    accent = PALETTE[gi % len(PALETTE)]
    story.append(heading(group.upper(), accent))
    cards = []
    for ti, (name, detail) in enumerate(topics, 1):
        code = f"{gi + 1:02d}.{ti:02d}"
        story.append(KeepTogether([p(f"{code}  {name}", "TopicHead"), p(detail), Spacer(1, 4)]))
        for kind in ("problems", "solutions"):
            filename = f"{code}-{kind}.pdf"
            if kind == "problems" and code in LECTURES:
                write_lecture(code, LECTURES[code])
            elif kind == "problems" and code in SETS:
                write_questions(code, name, accent)
            else:
                placeholder = [
                    p("COSMIC CALCULATION SERIES", "SmallClub"),
                    p(name, "TitleClub"),
                    heading(kind.upper(), accent),
                    callout("In preparation", f"This is a clearly marked placeholder. No {kind} have been published for this topic yet.", accent),
                    Spacer(1, 10), p("Syllabus topic: " + detail),
                    p("Return to Teaching: https://mais-pac.github.io/teaching/", "SmallClub"),
                ]
                write_pdf(
                    PDF / filename, f"{name} — {kind.title()}", placeholder,
                    accent=accent, header_label=f"{code}  ·  {kind.upper()}",
                )
        is_published = code in LECTURES or code in SETS
        problem_label = "Lecture + Problems" if code in LECTURES else "Problems"
        problem_detail = "Theory and past-paper problem index" if code in LECTURES else "Problems PDF"
        problem_status = "" if is_published else ", to be added"
        cards.append(
            f'<li class="curriculum-card"><span class="topic-code">{code}</span><div><h4>{escape(name)}</h4>'
            f'<div class="pdf-actions"><a href="pdf/{code}-problems.pdf" aria-label="{escape(name)}: {problem_detail}{problem_status}">{problem_label}</a>'
            f'<a href="pdf/{code}-solutions.pdf" aria-label="{escape(name)}: Solutions PDF, to be added">Solutions</a></div></div></li>'
        )
    blocks.append(cards)

# Group the curriculum under the nine syllabus headings; combine practical sections.
curriculum_sections = []
for gi in range(9):
    title = groups[gi][0] if gi < 8 else "Practical Part"
    cards = blocks[gi] if gi < 8 else blocks[8] + blocks[9]
    curriculum_sections.append(
        f'<section class="curriculum-group" aria-labelledby="curriculum-{gi}">'
        f'<h3 id="curriculum-{gi}">{escape(title)}</h3><ul class="curriculum-grid">'
        + "".join(cards) + "</ul></section>"
    )

write_pdf(
    PDF / "ioaa-syllabus.pdf", "IOAA Syllabus — MAIS PAC Study Edition", story,
    accent=PALETTE[0], header_label="IOAA SYLLABUS  ·  STUDY EDITION",
)
faqstory = [
    p("Frequently Asked Questions", "TitleClub"),
    p("Cosmic Calculation Series  ·  Teaching logistics", "SmallClub"),
]
for question, answer in faqs:
    faqstory.extend([callout(question, answer, PALETTE[0]), Spacer(1, 8)])
write_pdf(
    PDF / "frequently-asked-questions.pdf", "Teaching — Frequently Asked Questions", faqstory,
    accent=PALETTE[0], header_label="TEACHING  ·  FAQ",
)

# The handout rows are shared with the teaching page's existing template.
base = (ROOT / "scripts/teaching-template.html").read_text()
legacy = base[base.index('        <div class="handout-group">'):base.rindex("      </section>")]
content = '''<main id="main-content" class="teaching-main">
<h2 class="page-title">Teaching</h2>
<section class="teaching-section" aria-labelledby="series-title"><h2 id="series-title">Cosmic Calculation Series</h2>
<p>I wrote this series to be the resource I wish I had when I first began studying astronomy, and I hope it helps other students develop both their understanding of physics and their curiosity about the universe.</p>
<h3>Logistics</h3><ul class="logistics-links"><li><a href="pdf/ioaa-syllabus.pdf">Syllabus <span>(PDF)</span></a> and <a href="pdf/frequently-asked-questions.pdf">Frequently Asked Questions <span>(PDF)</span></a></li><li><a href="https://www.ioaa2026.vn/en/ioaa-syllabus">Official IOAA syllabus ↗</a></li></ul>
<p class="publication-note"><strong>New:</strong> Theory-first lecture PDFs with official past-paper problem identifiers are available for Basic Astrophysics (01.01–01.05). Their final section lists problem IDs only; question statements are not reproduced. The Coordinates and Times problem PDFs remain original club practice sets.</p>
<h3>Core Curriculum</h3><p class="curriculum-note">Organized by IOAA syllabus topics, including observations and data analysis. Club topic codes are for navigation; (Q) in the syllabus means qualitative understanding only.</p>
'''+''.join(curriculum_sections)+'''</section><section class="teaching-section" aria-labelledby="legacy-title"><h2 id="legacy-title">Existing club handouts</h2><p>Our introductory physics and astronomy sheets remain available below, with matching downloadable PDFs for handouts and solutions.</p>'''+legacy+'''</section></main>'''
page = re.sub(r'<main id="main-content">.*?</main>', lambda _match: content, base, flags=re.S)
page = page.replace("Handouts ·", "Teaching ·")
page = page.replace("https://mais-pac.github.io/handouts/", "https://mais-pac.github.io/teaching/")
page = page.replace(">Handouts</a>", ">Teaching</a>")
page = page.replace('aria-current="page" href="../handouts/"', 'aria-current="page" href="../teaching/"')
page = page.replace(
    "A place to explore physics, begin learning astronomy, and ask questions until they become understanding.",
    "Teaching resources, the Cosmic Calculation Series, and the IOAA syllabus.",
)
(OUT / "index.html").write_text(page)

print(
    f"Built Teaching: {sum(len(topics) for _, topics in groups)} topics, "
    f"{len(LECTURES)} theory-first Basic Astrophysics PDFs, "
    f"{sum(code not in LECTURES for code in SETS)} original problem sets, syllabus, FAQ and placeholders."
)
