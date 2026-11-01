"""Connect the 15 extended HTML-first handouts to Teaching (idempotent).
Also registers them in build_teaching.py so future rebuilds keep HTML links.
"""
from pathlib import Path
from html import escape
import re,sys
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from curriculum_topics import TOPICS
# 1) Register in build_teaching.py WEB_HANDOUTS without disturbing existing entries.
bt=ROOT/'scripts/build_teaching.py';text=bt.read_text()
entries=[]
for t in TOPICS:
    code=t['code']
    if f'"{code}":' in text.split('WEB_HANDOUTS = {',1)[1].split('\n}',1)[0]:
        continue
    entries.append(f'    "{code}": {{"lecture": "../handouts/{code}.html", "solutions": "../handouts/{code}-solutions.html", "detail": "Interactive lecture, 10 original problems and vector experiment"}},')
if entries:
    text=text.replace('WEB_HANDOUTS = {\n','WEB_HANDOUTS = {\n'+'\n'.join(entries)+'\n',1)
# Update FAQ wording so it no longer calls 07–10 placeholders.
text=text.replace('Other curriculum solution PDFs remain placeholders; the introductory club handouts already have their own solutions.',
                  'Instrumentation, Mathematical Methods and the Practical Part (07–10) also have HTML lectures and worked solutions; remaining placeholder PDFs are clearly marked.')
text=text.replace('Basic Astrophysics (01.01–01.05) has 75 fully worked solutions, and Cosmology (06.01) has 30.',
                  'Basic Astrophysics (01.01–01.05) has 75 fully worked solutions, Cosmology (06.01) has 30, and the extended curriculum (07–10) has 150.')
bt.write_text(text)
# 2) Patch the current Teaching page cards directly (avoids regenerating unrelated PDFs).
p=ROOT/'teaching/index.html';html=p.read_text()
for t in TOPICS:
    code,name=t['code'],t['title']
    card=(f'<li class="curriculum-card"><span class="topic-code">{code}</span><div><h4>{escape(name)}</h4><div class="pdf-actions">'
          f'<a href="../handouts/{code}.html" aria-label="{escape(name)}: interactive lecture, 10 original problems and vector experiment">Lecture + Problems</a>'
          f'<a href="../handouts/{code}-solutions.html" aria-label="{escape(name)}: 10 fully worked solutions">Solutions</a></div></div></li>')
    html,n=re.subn(rf'<li class="curriculum-card"><span class="topic-code">{re.escape(code)}</span>.*?</li>',lambda _:card,html,count=1,flags=re.S)
    if n!=1:raise RuntimeError(f'Missing curriculum card {code}')
html=html.replace('Other curriculum solution PDFs remain placeholders; the introductory club handouts already have their own solutions.',
                  'Instrumentation, Mathematical Methods and the Practical Part (07–10) also have HTML lectures and worked solutions; remaining placeholder PDFs are clearly marked.')
html=html.replace('Basic Astrophysics (01.01–01.05) has 75 fully worked solutions, and Cosmology (06.01) has 30.',
                  'Basic Astrophysics (01.01–01.05) has 75 fully worked solutions, Cosmology (06.01) has 30, and the extended curriculum (07–10) has 150.')
if 'The extended curriculum (07.01–10.04) now adds' not in html:
    html=html.replace('Basic Astrophysics (01.01–01.05) now uses the same HTML-first design, with 75 original problems, fully worked solutions, vector figures and five interactive experiments.',
                      'Basic Astrophysics (01.01–01.05) now uses the same HTML-first design, with 75 original problems, fully worked solutions, vector figures and five interactive experiments. The extended curriculum (07.01–10.04) now adds 15 HTML-first lectures, 150 original problems and worked solutions, 30 vector figures and 15 interactive experiments.')
p.write_text(html)
print('Connected 07.01–10.04 HTML lectures and solutions; registered in build_teaching.py')
