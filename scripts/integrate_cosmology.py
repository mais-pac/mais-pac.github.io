"""Idempotently connect Cosmology to Teaching while preserving source formatting.
The same routing is implemented in build_teaching.py for future rebuilds.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'teaching'/'index.html'
text=path.read_text()
card=('<li class="curriculum-card"><span class="topic-code">06.01</span><div><h4>Elementary Cosmology</h4>'
      '<div class="pdf-actions">'
      '<a href="../handouts/06.01.html" aria-label="Elementary Cosmology: interactive lecture, 30 problems and vector experiments">Lecture + Problems</a>'
      '<a href="../handouts/06.01-solutions.html" aria-label="Elementary Cosmology: 30 fully worked solutions">Solutions</a>'
      '</div></div></li>')
text,n=re.subn(r'<li class="curriculum-card"><span class="topic-code">06\.01</span>.*?</li>',lambda _:card,text,count=1,flags=re.S)
if n!=1:
    raise RuntimeError('Cosmology curriculum entry 06.01 not found')
note=('<p class="publication-note"><strong>New: <a href="../handouts/06.01.html">Cosmology — Lecture + Problems</a>.</strong> '
      'Comprehensive notes, five interactive experiments, vector diagrams and 30 problems with '
      '<a href="../handouts/06.01-solutions.html">fully worked solutions</a>, including website-sourced adaptations and original IOAA-inspired challenges. '
      'Theory-first lecture PDFs with official past-paper identifiers remain available for Basic Astrophysics (01.01–01.05); '
      'the Coordinates and Times problem PDFs remain original club practice sets.</p>')
text,n=re.subn(r'<p class="publication-note">.*?</p>',lambda _:note,text,count=1,flags=re.S)
if n!=1:
    raise RuntimeError('Teaching publication note not found')
path.write_text(text)
print('Connected 06.01 Lecture + Problems and Solutions in teaching/index.html')
