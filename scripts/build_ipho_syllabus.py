"""Create a clearly labelled reading copy of the supplied syllabus PDF."""
from io import BytesIO
from pathlib import Path
import pymupdf as fitz
from reportlab.pdfgen import canvas
R = Path(__file__).resolve().parents[1]
buf = BytesIO()
c = canvas.Canvas(buf, pagesize=(595,842))
c.setTitle('IPhO syllabus — MAIS PAC reading copy')
c.setFont('Helvetica-Bold', 19); c.drawString(54,780,'IPhO syllabus: reading copy')
c.setFont('Helvetica', 11)
y=740
for line in [
    'MAIS Physics & Astronomy Club | checked 1 November 2026',
    '',
    'The following five pages reproduce the supplied syllabus PDF:',
    'accepted in 2014 and amended in 2015. This is not an official',
    'newly issued syllabus or a claim of a new syllabus revision.',
    '',
    'The IPhO organisation publishes the syllabus online:',
    'https://www.ipho-new.org/statutes-syllabus/',
    'Consult that page and your contest organisers for current guidance.',
    '',
    'A wording difference: the online measurement-apparatus list explicitly',
    'includes transistors; the supplied PDF does not. The online version',
    'is the authority for that wording. Other changes may also exist.',
    '',
    'Source of supplied PDF:',
    'https://physicscup.ee/wp-content/uploads/2019/10/Syllabus-new.pdf',
    '',
    'This reading copy adds this cover only; the original pages follow.',
]:
    c.drawString(54,y,line); y-=19
c.linkURL('https://www.ipho-new.org/statutes-syllabus/',(54,601,330,616),relative=0)
c.showPage();c.save()
out=fitz.open(stream=buf.getvalue(),filetype='pdf')
original=fitz.open(R/'teaching/pdf/ipho-syllabus-supplied.pdf')
out.insert_pdf(original)
out.save(R/'teaching/pdf/ipho-syllabus.pdf',deflate=True)
