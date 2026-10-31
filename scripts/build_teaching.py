"""Rebuild Teaching and its PDFs: pip install reportlab; python scripts/build_teaching.py."""
from pathlib import Path
from question_sets import SETS
from html import escape
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'teaching'
PDF = OUT / 'pdf'
PDF.mkdir(exist_ok=True)
SOURCE = 'https://www.ioaa2026.vn/en/ioaa-syllabus'
groups = []
for line in (OUT / 'syllabus-topics.txt').read_text().splitlines():
    if line.startswith('# '):
        groups.append((line[2:], []))
    elif line.strip():
        name, detail = line.split(' | ', 1)
        groups[-1][1].append((name, detail))
notes = [
'Extensive contents in basic astronomical concepts are required in theoretical and practical problems.',
'Basic concepts in physics and mathematics at high school level are required in solving the problems. Standard solutions should not involve use of complex numbers and/or solving differential equations.',
'Astronomical software packages may be used in practical and observational problems. The contestants will be informed the list of software packages to be used at least 3 months in advance. The chosen software packages should be preferably freeware or low-cost ones enabling all countries to obtain them easily for practice purpose. The chosen software should preferably be available on multiple OSs (Windows / Unix / GNU-Linux / Mac).',
'Concepts and phenomena not included in the Syllabus may be used in questions but sufficient information must be given in the questions so that contestants without previous knowledge of these topics would not be at a disadvantage.',
'Sophisticated practical equipment likely to be unfamiliar to the candidates should not dominate a problem. If such devices are used in the questions, sufficient information must be provided. In such cases, students should be given opportunity to familiarise themselves with the equipment before the exam.',
'The original text of the problems must use SI units, wherever applicable. Participants will be expected to give appropriate units in their answers and should be familiar with the idea of correct rounding off and expressing the final result(s) and error(s) with the correct number of significant digits.',
'A standard table of constants (supplied as a supplement to this Syllabus) shall be used when setting questions and provided to the students. Additional constants may be added to specific questions as required.'
]
faqs = [
('What is the Cosmic Calculation Series?', 'A planned collection of astronomy learning materials organized around the IOAA syllabus. It is intended to support both physical understanding and curiosity about the universe.'),
('Are the problems and solutions available?', 'Original problem sets are available for the five Basic Astrophysics topics and the two Coordinates and Times topics. All other problem PDFs and every Solutions PDF are placeholders marked “To be Added!”'),
('What background does the syllabus require?', 'The IOAA syllabus requires high-school physics and mathematics. Standard solutions should not require complex numbers or solving differential equations. The listed mathematical methods include basic calculus.'),
('What does (Q) mean?', 'Qualitative understanding only. Quantitative reasoning or proficiency in topics marked (Q) is not mandatory.'),
('Is this an official IOAA publication?', 'No. This is a MAIS PAC study resource. The syllabus PDF is a reformatted reproduction of the syllabus published on the IOAA 2026 website, which credits IOAA and an update of 17 November 2021. The topic codes and practical-topic labels are club organizational aids.'),
('Where are the existing club handouts?', 'The existing introductory physics and astronomy handouts remain available in the Teaching page’s “Existing club handouts” section. They are separate from the Cosmic Calculation Series.')
]
# Embedded Unicode fonts preserve mathematical marks and typographic punctuation.
fontdir = Path('/usr/share/fonts/truetype/dejavu')
for name, file in [('Club', 'DejaVuSans.ttf'), ('ClubBold', 'DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(fontdir / file)))
pdfmetrics.registerFontFamily('Club', normal='Club', bold='ClubBold', italic='Club', boldItalic='ClubBold')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Text', fontName='Club', fontSize=9.5, leading=15, spaceAfter=10))
styles.add(ParagraphStyle(name='TitleClub', fontName='ClubBold', fontSize=27, leading=34, textColor=colors.HexColor('#172554'), spaceAfter=15))
styles.add(ParagraphStyle(name='BoxHead', fontName='ClubBold', fontSize=12, leading=17, textColor=colors.white))
styles.add(ParagraphStyle(name='TopicHead', fontName='ClubBold', fontSize=10, leading=15, textColor=colors.HexColor('#172554'), spaceAfter=5))
styles.add(ParagraphStyle(name='SmallClub', fontName='Club', fontSize=8, leading=12, textColor=colors.HexColor('#536078'), spaceAfter=12))
palette = ['#244bc1', '#6d28a4', '#08756e', '#b54221']
def p(text, style='Text'):
    return Paragraph(escape(text), styles[style])
def heading(text, color):
    t = Table([[p(text, 'BoxHead')]], colWidths=[475])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),colors.HexColor(color)),('BOX',(0,0),(-1,-1),0,colors.white),('LEFTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)]))
    t.keepWithNext = True
    return t

def footer(c, doc):
    c.setStrokeColor(colors.HexColor('#d7deee')); c.line(60,44,535,44)
    c.setFont('Club', 8); c.setFillColor(colors.HexColor('#536078'))
    c.drawString(60,30,'MAIS PAC · Cosmic Calculation Series')
    c.drawRightString(535,30,str(doc.page))
def write_pdf(path, title, story):
    doc = SimpleDocTemplate(str(path), pagesize=(595.28,841.89), rightMargin=60,leftMargin=60,topMargin=48,bottomMargin=62,title=title,author='MAIS Physics & Astronomy Club')
    doc.build(story,onFirstPage=footer,onLaterPages=footer)


# The contents entries link to the corresponding questions within each PDF.
styles.add(ParagraphStyle(name='QuestionTitle', fontName='ClubBold', fontSize=12, leading=17, textColor=colors.HexColor('#244bc1'), spaceBefore=13, spaceAfter=6, keepWithNext=True))
styles.add(ParagraphStyle(name='ContentsEntry', fontName='ClubBold', fontSize=10, leading=16, textColor=colors.HexColor('#244bc1')))

def write_questions(code, name, color):
    questions = SETS[code]
    story = [p('COSMIC CALCULATION SERIES  /  PROBLEMS', 'SmallClub'),
             p(name, 'TitleClub'), p(f'{code}  ·  Original practice problems', 'TopicHead'),
             p('Show your reasoning, use SI units where appropriate, and state any assumptions. Constants are supplied in the questions that need them.'),
             heading('CONTENTS', color), Spacer(1, 10)]
    for i, (title, _) in enumerate(questions, 1):
        story.append(Paragraph(f'<link href="#q{i}" color="{color}">{i:02d}  {escape(title)}</link>', styles['ContentsEntry']))
        story.append(Spacer(1, 8))
    story += [Spacer(1, 20), p('A MAIS Physics & Astronomy Club study resource. These are original exercises, not official IOAA problems.', 'SmallClub'), PageBreak(),
              heading('PROBLEMS', color), Spacer(1, 8)]
    for i, (title, question) in enumerate(questions, 1):
        story.append(Paragraph(f'<a name="q{i}"/><font color="{color}">{i:02d}  {escape(title)}</font>', styles['QuestionTitle']))
        story.append(p(question))
        story.append(Spacer(1, 8))
    write_pdf(PDF/f'{code}-problems.pdf', f'{name} — Problems', story)

story = [p('IOAA Syllabus', 'TitleClub'), p('A study edition · MAIS Physics & Astronomy Club', 'TopicHead'), p('Reformatted from the IOAA 2026 website. Source credits IOAA; updated 17 November 2021. Topic wording is preserved with minor punctuation and typography normalization. Club topic codes and practical-topic labels are organizational aids, not official designations.', 'SmallClub'), Paragraph(f'<link href="{SOURCE}" color="#244bc1">Official source: IOAA 2026 syllabus</link>',styles['Text']), heading('General Notes',palette[0]), Spacer(1,10)]
for i,n in enumerate(notes,1): story.append(p(f'{i}. {n}'))
story += [heading('Theoretical Part',palette[1]),Spacer(1,10),p('Symbol (Q) is attached to some topics in the list. It means “qualitative understanding only”. Quantitative reasoning / proficiency in these topics is not mandatory. The following theoretical contents are proposed for the contestants.')]
blocks=[]
for gi,(group, topics) in enumerate(groups):
    if gi==8:
        story += [PageBreak(),p('Practical Part','TitleClub'),p('This part consists of 2 sections: observations and data analysis sections. The theoretical part of the Syllabus provides the basis for all problems in the practical part.'),p('The observations section focuses on contestant’s experience in:')]
    if gi==9:
        story += [p('Observational objects may be from real sources in the sky or imitated sources in the laboratory.'),p('Computer simulations may be used in the problems but sufficient instructions must be provided to the contestants.'),p('The data analysis section focuses on the calculation and analysis of the astronomical data provided in the problems. Additional requirements are as follows:')]
    story += [heading(group,palette[gi%4]),Spacer(1,12)]
    cards=[]
    for ti,(name, detail) in enumerate(topics,1):
        code=f'{gi+1:02d}.{ti:02d}'
        story.append(KeepTogether([p(code+'  '+name,'TopicHead'),p(detail),Spacer(1,5)]))
        for kind in ['problems','solutions']:
            filename=f'{code}-{kind}.pdf'
            if kind == 'problems' and code in SETS:
                write_questions(code, name, palette[gi % 4])
            else:
                write_pdf(PDF/filename,f'{name} — {kind.title()}',[p('Cosmic Calculation Series','SmallClub'),p(name,'TitleClub'),heading(kind.title(),palette[gi%4]),Spacer(1,20),p('To be Added!','TitleClub'),p('This is a placeholder only. No '+kind+' have been published for this topic.'),p('Syllabus topic: '+detail),p('Return to Teaching: https://mais-pac.github.io/teaching/','SmallClub')])
        problem_status = '' if code in SETS else ', to be added'
        cards.append(f'''<li class="curriculum-card"><span class="topic-code">{code}</span><div><h4>{escape(name)}</h4><div class="pdf-actions"><a href="pdf/{code}-problems.pdf" aria-label="{escape(name)}: Problems PDF{problem_status}">Problems</a><a href="pdf/{code}-solutions.pdf" aria-label="{escape(name)}: Solutions PDF, to be added">Solutions</a></div></div></li>''')
    blocks.append(cards)
# Group the curriculum under the nine syllabus headings; combine practical sections.
curriculum_sections = []
for gi in range(9):
    title = groups[gi][0] if gi < 8 else 'Practical Part'
    cards = blocks[gi] if gi < 8 else blocks[8] + blocks[9]
    curriculum_sections.append(f'<section class="curriculum-group" aria-labelledby="curriculum-{gi}"><h3 id="curriculum-{gi}">{escape(title)}</h3><ul class="curriculum-grid">'+''.join(cards)+'</ul></section>')
write_pdf(PDF/'ioaa-syllabus.pdf','IOAA Syllabus · MAIS PAC study edition',story)
faqstory=[p('Frequently Asked Questions','TitleClub'),p('Cosmic Calculation Series · Teaching logistics','SmallClub')]
for q,a in faqs: faqstory += [p(q,'TopicHead'),p(a),Spacer(1,8)]
write_pdf(PDF/'frequently-asked-questions.pdf','Teaching · Frequently Asked Questions',faqstory)
base=(ROOT/'scripts/teaching-template.html').read_text()
legacy=base[base.index('        <div class="handout-group">'):base.rindex('      </section>')]
content='''<main id="main-content" class="teaching-main">
<h2 class="page-title">Teaching</h2>
<section class="teaching-section" aria-labelledby="series-title"><h2 id="series-title">Cosmic Calculation Series</h2>
<p>I wrote this series to be the resource I wish I had when I first began studying astronomy, and I hope it helps other students develop both their understanding of physics and their curiosity about the universe.</p>
<h3>Logistics</h3><ul class="logistics-links"><li><a href="pdf/ioaa-syllabus.pdf">Syllabus <span>(PDF)</span></a> and <a href="pdf/frequently-asked-questions.pdf">Frequently Asked Questions <span>(PDF)</span></a></li><li><a href="https://www.ioaa2026.vn/en/ioaa-syllabus">Official IOAA syllabus ↗</a></li></ul>
<p class="publication-note"><strong>Now available:</strong> Problems for Basic Astrophysics and Coordinates and Times. All other Problems and all Solutions links currently open placeholder PDFs.</p>
<h3>Core Curriculum</h3><p class="curriculum-note">Organized by IOAA syllabus topics, including observations and data analysis. Club topic codes are for navigation; (Q) in the syllabus means qualitative understanding only.</p>
'''+''.join(curriculum_sections)+'''</section><section class="teaching-section" aria-labelledby="legacy-title"><h2 id="legacy-title">Existing club handouts</h2><p>Our introductory physics and astronomy sheets remain available below. These are separate from the Cosmic Calculation Series.</p>'''+legacy+'''</section></main>'''
page=re.sub(r'<main id="main-content">.*?</main>',lambda m:content,base,flags=re.S)
page=page.replace('Handouts ·','Teaching ·').replace('https://mais-pac.github.io/handouts/','https://mais-pac.github.io/teaching/').replace('>Handouts</a>','>Teaching</a>').replace('aria-current="page" href="../handouts/"','aria-current="page" href="../teaching/"')
page=page.replace('A place to explore physics, begin learning astronomy, and ask questions until they become understanding.','Teaching resources, the Cosmic Calculation Series, and the IOAA syllabus.')
(OUT/'index.html').write_text(page)
print(f'Built Teaching: {sum(len(t) for _,t in groups)} topics, {len(SETS)} problem sets, syllabus, FAQ, and remaining placeholders.')
