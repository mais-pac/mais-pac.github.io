"""Official-style black-and-white IOAA syllabus study edition.
Layout reference: https://usaaao.org/wp-content/uploads/2016/06/ioaa_syllabus.pdf
Content retained from the newer 17 November 2021 syllabus, not the older reference.
"""
from pathlib import Path
from html import escape
import ast, subprocess
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
ROOT=Path(__file__).resolve().parents[1]
# Read literal data only: importing build_teaching would rebuild unrelated PDFs.
tree=ast.parse((ROOT/'scripts/build_teaching.py').read_text())
notes=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='notes' for t in n.targets))
groups=[]
for line in (ROOT/'teaching/syllabus-topics.txt').read_text().splitlines():
    if line.startswith('# '): groups.append((line[2:],[]))
    elif line.strip():
        name,detail=line.split(' | ',1); groups[-1][1].append((name,detail))
fontdir=Path('/usr/share/fonts/truetype/dejavu')
for name,file in [('Syllabus','DejaVuSans.ttf'),('SyllabusBold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(fontdir/file)))
pdfmetrics.registerFontFamily('Syllabus',normal='Syllabus',bold='SyllabusBold')
body=ParagraphStyle('body',fontName='Syllabus',fontSize=10.5,leading=14.1,spaceAfter=9,alignment=TA_LEFT)
bold=ParagraphStyle('bold',parent=body,fontName='SyllabusBold',spaceAfter=10,keepWithNext=True)
small=ParagraphStyle('small',parent=body,fontSize=8,leading=10.5,textColor=colors.HexColor('#555555'))
cell=ParagraphStyle('cell',parent=body,fontSize=10,leading=13.5,spaceAfter=0)
cellbold=ParagraphStyle('cellbold',parent=cell,fontName='SyllabusBold')
num=ParagraphStyle('num',parent=body,alignment=2)
title=ParagraphStyle('title',parent=bold,fontSize=22,leading=28,spaceAfter=22)
P=lambda text,style=body:Paragraph(escape(text),style)

def numbered(items):
    return Table([[P(str(i)+'.',num),P(t)] for i,t in enumerate(items,1)],colWidths=[30,438],style=TableStyle([
        ('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(0,-1),6),('RIGHTPADDING',(1,0),(1,-1),0),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),9)]))

def topic_table(rows):
    data=[[P('Contents',cellbold),P('Remarks',cellbold)]]+[[P(n,cellbold),P(d,cell)] for n,d in rows]
    t=Table(data,colWidths=[229,239],repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('GRID',(0,0),(-1,-1),0.85,colors.black),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),7),('BACKGROUND',(0,0),(-1,-1),colors.white)]))
    return t

story=[P('Syllabus of',ParagraphStyle('syllabusof',parent=bold,fontSize=17,leading=22,spaceAfter=20)),P('International Olympiad on Astronomy and Astrophysics (IOAA)',title),Spacer(1,7),P('General Notes',bold),numbered(notes),Spacer(1,10),P('MAIS PAC study edition. Content: IOAA syllabus updated 17 November 2021. Layout follows the USAAAO-hosted IOAA syllabus. This is a club study resource, not a newly issued official syllabus.',small),PageBreak(),P('A. Theoretical Part',bold),P('Symbol (Q) is attached to some topics in the list. It means “qualitative understanding only”. Quantitative reasoning / proficiency in these topics is not mandatory.'),P('The following theoretical contents are proposed for the contestants.')]
for i,(name,rows) in enumerate(groups[:8],1):
    story.extend([P(f'{i}. {name}',bold),topic_table(rows),Spacer(1,15)])
story.extend([P('B. Practical Part',bold),P('This part consists of 2 sections: observations and data analysis sections. The theoretical part of the Syllabus provides the basis for all problems in the practical part.'),P('The observations section focuses on contestants’ experience in:',bold),numbered([d for _,d in groups[8][1]]),P('Observational objects may be from real sources in the sky or imitated sources in the laboratory. Computer simulations may be used in the problems but sufficient instructions must be provided to the contestants.'),P('The data analysis section focuses on the calculation and analysis of the astronomical data provided in the problems. Additional requirements are as follows:'),numbered([d for _,d in groups[9][1]]),Spacer(1,12),Paragraph('Sources: <link href="https://www.ioaa2026.vn/en/ioaa-syllabus" color="#333333">IOAA syllabus (updated 17 November 2021)</link>; <link href="https://usaaao.org/wp-content/uploads/2016/06/ioaa_syllabus.pdf" color="#333333">USAAAO-hosted layout reference</link>. Minor punctuation and typography have been normalized. Club topic codes are omitted from this document.',small)])

def footer(canvas,doc):
    canvas.saveState();canvas.setFont('Syllabus',7.5);canvas.setFillColor(colors.HexColor('#666666'))
    canvas.drawString(72,30,'MAIS PAC · IOAA syllabus study edition · 2021 content')
    canvas.drawRightString(540,30,str(doc.page));canvas.restoreState()
out=ROOT/'teaching/pdf/ioaa-syllabus.pdf'
doc=SimpleDocTemplate(str(out),pagesize=(612,792),leftMargin=72,rightMargin=72,topMargin=64,bottomMargin=52,title='IOAA Syllabus — MAIS PAC Study Edition',author='MAIS Physics & Astronomy Club',subject='IOAA syllabus updated 17 November 2021; official-style study edition')
doc.build(story,onFirstPage=footer,onLaterPages=footer)
print('Built official-style syllabus:',out)
