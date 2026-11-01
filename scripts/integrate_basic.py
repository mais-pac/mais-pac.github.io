"""Connect the five HTML-first Basic Astrophysics handouts to Teaching (idempotent)."""
from pathlib import Path
from html import escape
import re,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from lecture_content import LECTURES
p=ROOT/'teaching/index.html';text=p.read_text()
for code,lec in LECTURES.items():
 name=lec['title']
 card=(f'<li class="curriculum-card"><span class="topic-code">{code}</span><div><h4>{escape(name)}</h4><div class="pdf-actions">'
       f'<a href="../handouts/{code}.html" aria-label="{escape(name)}: interactive lecture, 15 original problems and vector experiment">Lecture + Problems</a>'
       f'<a href="../handouts/{code}-solutions.html" aria-label="{escape(name)}: 15 fully worked solutions">Solutions</a></div></div></li>')
 text,n=re.subn(rf'<li class="curriculum-card"><span class="topic-code">{re.escape(code)}</span>.*?</li>',lambda _:card,text,count=1,flags=re.S)
 if n!=1:raise RuntimeError(f'Missing curriculum card {code}')
p.write_text(text);print('Connected 01.01–01.05 HTML lectures and solutions')
