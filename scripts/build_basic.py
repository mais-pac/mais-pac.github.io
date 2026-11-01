"""Build five HTML-first Basic Astrophysics handouts in the exact Cosmology sheet theme."""
from pathlib import Path
import base64, json, re, subprocess, sys
import markdown
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]; SRC=ROOT/'scripts/basic'
sys.path.insert(0,str(ROOT/'scripts'));sys.path.insert(0,str(SRC))
from build_cosmology import katex_css, format_problem_parts
from lecture_content import LECTURES
from basic.figures import FIGURES
from basic.labs import LABS
TOPICS={f'01.{i:02d}':key for i,key in enumerate(['orbit','blackbody','gas','spectrum','decay'],1)}

def render(source):
    maths=[]
    def stash(m,display):
        i=len(maths);maths.append({'tex':m.group(1).strip(),'display':display})
        return f'\n\nMATHBLOCK{i:04d}END\n\n' if display else f'MATHINLINE{i:04d}END'
    source=re.sub(r'\$\$(.*?)\$\$',lambda m:stash(m,True),source,flags=re.S)
    source=re.sub(r'(?<!\$)\$([^\n$]+?)\$(?!\$)',lambda m:stash(m,False),source)
    html=markdown.markdown(source,extensions=['extra','toc','sane_lists','md_in_html'])
    if maths:
        result=subprocess.run(['node',str(ROOT/'scripts/render_cosmology_math.mjs')],input=json.dumps(maths),text=True,capture_output=True,check=True)
        for i,(m,out) in enumerate(zip(maths,json.loads(result.stdout))):
            if m['display']:
                number=sum(x['display'] for x in maths[:i+1]);token=f'MATHBLOCK{i:04d}END'
                box=f'<div class="eq"><div class="eq__expr">{out}</div><span class="eq__num">({number})</span></div>'
                html=html.replace(f'<p>{token}</p>',box).replace(token,box)
            else:html=html.replace(f'MATHINLINE{i:04d}END',out)
    html=re.sub(r'<p>\{\{FIG:(\w+)\}\}</p>',lambda m:FIGURES[m.group(1)](),html)
    html=re.sub(r'\{\{FIG:(\w+)\}\}',lambda m:FIGURES[m.group(1)](),html)
    html=re.sub(r'<p>\{\{LAB:(\w+)\}\}</p>',lambda m:LABS[m.group(1)](),html)
    html=re.sub(r'\{\{LAB:(\w+)\}\}',lambda m:LABS[m.group(1)](),html)
    if 'MATHBLOCK' in html or 'MATHINLINE' in html or '{{' in html:raise ValueError('Unrendered component')
    return html

def page(code,key,body,solutions=False):
    soup=BeautifulSoup(body,'html.parser');links=[];problem_anchor=None
    for table in soup.find_all('table'):table.wrap(soup.new_tag('div',attrs={'class':'table-scroll'}))
    for i,h in enumerate(soup.find_all('h2'),1):
        h['id']=f'basic-section-{i}';title=re.sub(r'^\d+\.\s*','',h.get_text(' ',strip=True));links.append((h['id'],title))
        if 'Lecture + Problems' in title:problem_anchor=h['id']
    if solutions:
        toc='<nav class="cosmo-toc" aria-label="Solution index"><strong>Solution index</strong><div class="solution-index">'+''.join(f'<a href="#s{i}" aria-label="Solution {i}">{i}</a>' for i in range(1,16))+'</div></nav>'
    else:toc='<details class="cosmo-toc" open><summary>Contents &amp; learning path</summary><ol>'+''.join(f'<li><a href="#{id}">{text}</a></li>' for id,text in links)+'</ol></details>'
    content=str(soup).replace('<div id="basic-toc"></div>',toc)
    name=LECTURES[code]['title'];icon=base64.b64encode((ROOT/'assets/club-logo.png').read_bytes()).decode()
    css=(ROOT/'style.css').read_text()+'\n'+(ROOT/'scripts/cosmology/cosmology.css').read_text()+'\n'+katex_css()+'\n.basic-solutions .solution{break-inside:auto}\n'
    top=(f'<a href="{code}.html">Lecture + Problems</a><strong>Solutions</strong><a class="pdf-download" href="pdf/{code}-solutions.pdf" download>Solutions PDF</a>' if solutions else f'<strong>Handout {code}</strong><a href="{code}-solutions.html">Solutions</a><a class="pdf-download" href="pdf/{code}.pdf" download>Download PDF</a>')
    quick=(f'<a href="{code}.html">Lecture + Problems</a><a href="pdf/{code}.pdf">Lecture PDF</a><a href="../teaching/#curriculum-0">Basic Astrophysics curriculum</a>' if solutions else f'<a href="#basic-section-1">Start the lecture</a><a href="#{problem_anchor}">Problem set</a><a href="#lab-{key}">Interactive experiment</a><a href="{code}-solutions.html">Solutions</a>')
    nav=(f'<nav class="sheet-nav" aria-label="Handout navigation"><a href="../teaching/">← All teaching resources</a><a href="{code}.html">Lecture + Problems</a><a href="pdf/{code}-solutions.pdf" download>Solutions PDF</a></nav>' if solutions else f'<nav class="sheet-nav" aria-label="Handout navigation"><a href="../teaching/">← All teaching resources</a><a href="#lab-{key}">Interactive experiment</a><a href="{code}-solutions.html">Worked solutions →</a></nav>')
    heading=name+(': Worked Solutions' if solutions else '')
    subtitle='MAIS Physics &amp; Astronomy Club (PAC) · '+('Reasoning, derivations and checks' if solutions else 'Olympiad lecture + problem handout')
    meta='15 worked solutions · independent explanations · consistency checks' if solutions else f'{len(links)-2} lecture sections · 15 problems · 1 interactive experiment · 2 vector figures'
    intro=('<p>Make a genuine attempt before reading. Each solution explains how to choose the method, carries units through the calculation, and checks the result. The exercises are original MAIS PAC teaching problems, not official IOAA questions or marking schemes. Parameters are supplied locally; an exam’s constants take precedence.</p>' if solutions else '<p>Start with a physical picture, then introduce only the mathematics needed to make it predictive. The lecture connects everyday reasoning to astronomical measurements. Two vector diagrams and an interactive experiment support the argument; 15 graded problems and independent worked solutions turn the ideas into practice.</p>')
    script='' if solutions else '<script>'+(SRC/'labs.js').read_text()+'</script>'
    header='<script data-pac-sticky>'+ (ROOT/'scripts/header.js').read_text()+'</script>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="MAIS PAC {name}: Olympiad lecture, 15 original problems and worked solutions, vector figures and interactive experiment."><meta name="theme-color" content="#ffffff"><title>{code}: {heading} · MAIS PAC</title><link rel="icon" type="image/png" href="data:image/png;base64,{icon}"><style>{css}</style>{header}</head><body><a class="skip-link" href="#sheet">Skip to {'solutions' if solutions else 'handout'}</a><div class="handout-bar"><div class="handout-bar__inner"><a href="../teaching/">← MAIS Physics &amp; Astronomy Club</a><div class="handout-bar__links">{top}<button class="print-btn" type="button" onclick="window.print()">Print / PDF</button></div></div></div><main class="sheet-page {'cosmology-solutions basic-solutions' if solutions else 'cosmology-lecture basic-lecture'}" id="sheet" data-topic="{code}"><div class="running-head"><a class="brand-link" href="../" aria-label="MAIS PAC home">MAIS PAC</a><span>{code}: {name} · {'Worked Solutions' if solutions else 'Lecture + Problems'}</span></div><header class="sheet-title-block"><h1>{heading}</h1><p class="sheet-subtitle">{subtitle}</p><p class="cosmo-meta">{meta}</p></header><div class="sheet-intro">{intro}</div><div class="cosmo-quicklinks">{quick}</div>{content}{nav}</main>{script}</body></html>'''

def practice(code):
    rows=LECTURES[code]['problem_ids']
    items=''.join(f'<li>IOAA {y} · {r} · {q}</li>' for y,r,q in rows)
    return '\n\n## Further practice and provenance\n\nThe 15 exercises above and their solutions are **original MAIS PAC problems**, inspired by the skills in this syllabus topic. They are not copied from the papers below. The earlier club lecture compiled these official past-paper identifiers for further practice; only identifiers are reproduced, not copyrighted question statements or official solutions. Round and question labels retain the earlier compilation’s notation and should be checked against the official paper.\n\n<ul class="past-paper-index">'+items+'</ul>\n\n<div class="remark" markdown="1"><span class="remark-head">Sources and scope.</span> Topic coverage follows the [IOAA syllabus](https://www.ioaa2026.vn/en/ioaa-syllabus). Official problems and constants are available through the [IOAA past-paper archive](https://ioaa-stud.org/). The derivations, diagrams, experiments and numerical teaching examples in this handout were prepared independently for MAIS PAC. Calculator-level methods are emphasized; optional calculus connections are explicitly identified.</div>\n'

def build():
    for code,key in TOPICS.items():
        folder=SRC/code
        lecture=(folder/'lecture.md').read_text()
        problems=format_problem_parts((folder/'problems.md').read_text())
        # Put the problem-set heading immediately before the first problem block.
        n=len(re.findall(r'^## ',lecture,flags=re.M))
        lecture+=f'\n\n## {n+1}. Lecture + Problems: predict, calculate, check\n\nFifteen original problems: **[1]** foundation, **[2]** multi-step Olympiad reasoning, **[3]** challenge. Use the constants supplied in the lecture unless a question overrides them. Explain assumptions and keep units. Every problem has a worked solution.\n\n'+problems+practice(code)
        solutions=(folder/'solutions.md').read_text()
        for suffix,source,is_sol in [('', '<div id="basic-toc"></div>\n\n'+lecture,False),('-solutions','<div id="basic-toc"></div>\n\n'+solutions,True)]:
            html=page(code,key,render(source),is_sol);(ROOT/'handouts'/f'{code}{suffix}.html').write_text(html)
            soup=BeautifulSoup(html,'html.parser');assert len(soup.select('.solution' if is_sol else '.problem'))==15
            print(code+suffix, 'words',len(soup.get_text(' ',strip=True).split()),'SVGs',len(soup.select('svg')))
if __name__=='__main__':build()
