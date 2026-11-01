"""Build self-contained Cosmology HTML in the existing MAIS PAC handout theme.
Run after npm install. Python dependency: Markdown. Mathematics is pre-rendered
with KaTeX; fonts, CSS, SVG and experiment code are embedded for offline use.
"""
from pathlib import Path
import base64, json, re, subprocess
import markdown
from bs4 import BeautifulSoup
from cosmology_model import synthetic_data
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'scripts' / 'cosmology'
sys.path.insert(0, str(SRC))
from figures import FIGURES
from labs import LABS


def read(name):
    return (SRC / name).read_text()


def format_problem_parts(source):
    """Match the existing handouts' labelled subpart lists."""
    def group(m):
        items=[]
        for line in m.group(0).strip().splitlines():
            part, rest = re.match(r'^\(([a-z])\)\s+(.*)$', line).groups()
            items.append(f'<li><span class="part-label">({part})</span> {rest}</li>')
        return '<ul class="subparts" markdown="1">\n'+'\n'.join(items)+'\n</ul>'
    return re.sub(r'(?:^\([a-z]\) .*\n?)+', group, source, flags=re.M)


def render_markdown(source):
    maths = []
    def display(m):
        i = len(maths); maths.append({'tex': m.group(1).strip(), 'display': True})
        return f'\n\nMATHBLOCK{i:04d}END\n\n'
    def inline(m):
        i = len(maths); maths.append({'tex': m.group(1).strip(), 'display': False})
        return f'MATHINLINE{i:04d}END'
    source = re.sub(r'\$\$(.*?)\$\$', display, source, flags=re.S)
    source = re.sub(r'(?<!\$)\$([^\n$]+?)\$(?!\$)', inline, source)
    html = markdown.markdown(source, extensions=['extra', 'toc', 'sane_lists', 'md_in_html'])
    if maths:
        result = subprocess.run(['node', str(ROOT/'scripts'/'render_cosmology_math.mjs')],
                                input=json.dumps(maths), text=True, capture_output=True, check=True)
        rendered = json.loads(result.stdout)
        for i, (m, out) in enumerate(zip(maths, rendered)):
            if m['display']:
                token = f'MATHBLOCK{i:04d}END'
                number = sum(item['display'] for item in maths[:i+1])
                box = f'<div class="eq"><div class="eq__expr">{out}</div><span class="eq__num">({number})</span></div>'
                html = html.replace(f'<p>{token}</p>', box).replace(token, box)
            else:
                html = html.replace(f'MATHINLINE{i:04d}END', out)
    html = re.sub(r'<p>\{\{FIG:(\w+)\}\}</p>', lambda m: FIGURES[m.group(1)](), html)
    html = re.sub(r'\{\{FIG:(\w+)\}\}', lambda m: FIGURES[m.group(1)](), html)
    html = re.sub(r'<p>\{\{LAB:(\w+)\}\}</p>', lambda m: LABS[m.group(1)](), html)
    html = re.sub(r'\{\{LAB:(\w+)\}\}', lambda m: LABS[m.group(1)](), html)
    if 'MATHBLOCK' in html or 'MATHINLINE' in html or '{{' in html:
        raise ValueError('Unrendered mathematics or component placeholder')
    return html


def katex_css():
    css = (ROOT/'node_modules'/'katex'/'dist'/'katex.min.css').read_text()
    # Retain only WOFF2 sources, each embedded. Modern browsers and print export
    # support these; this avoids external requests in the sandboxed file viewer.
    def embed(m):
        name = m.group(1)
        data = (ROOT/'node_modules'/'katex'/'dist'/'fonts'/(name+'.woff2')).read_bytes()
        return 'src:url(data:font/woff2;base64,'+base64.b64encode(data).decode()+') format("woff2")'
    css = re.sub(r'src:url\(fonts/([^)]+?)\.woff2\) format\("woff2"\),url\(fonts/[^)]+?\.woff\) format\("woff"\),url\(fonts/[^)]+?\.ttf\) format\("truetype"\)', embed, css)
    if 'url(fonts/' in css:
        raise ValueError('A KaTeX font was not embedded')
    return css


def page(title, running, heading, subtitle, intro, body, solutions=False):
    soup = BeautifulSoup(body, 'html.parser')
    for table in soup.find_all('table'):
        wrapper = soup.new_tag('div', attrs={'class': 'table-scroll'})
        table.wrap(wrapper)
    links = []
    for i, h in enumerate(soup.find_all('h2'), 1):
        h['id'] = f'cosmo-section-{i}'
        links.append((h['id'], re.sub(r'^\d+\.\s*', '', h.get_text(' ', strip=True))))
    if solutions:
        toc = '<nav class="cosmo-toc" aria-label="Solution index"><strong>Solution index</strong><div class="solution-index">' + ''.join(f'<a href="#s{i}" aria-label="Solution {i}">{i}</a>' for i in range(1,31)) + '</div></nav>'
    else:
        toc = '<details class="cosmo-toc" open><summary>Contents &amp; learning path</summary><ol>' + ''.join(f'<li><a href="#{id}">{text}</a></li>' for id,text in links) + '</ol></details>'
    content = str(soup).replace('<div id="cosmo-toc"></div>', toc)
    css = (ROOT/'style.css').read_text() + '\n' + read('cosmology.css') + '\n' + katex_css()
    icon = base64.b64encode((ROOT/'assets'/'club-logo.png').read_bytes()).decode()
    top = ('<a href="06.01.html">Lecture + Problems</a><strong>Solutions</strong><a class="pdf-download" href="pdf/06.01-solutions.pdf" download>Solutions PDF</a>' if solutions else
           '<strong>Handout 06.01</strong><a href="06.01-solutions.html">Solutions</a><a class="pdf-download" href="pdf/06.01.pdf" download>Download PDF</a>')
    script = ''
    if not solutions:
        js = read('labs.js').replace('__HUBBLE_DATA__', json.dumps(synthetic_data(), separators=(',',':')))
        script = '<script>'+js+'</script>'
    nav = ('<nav class="sheet-nav" aria-label="Handout navigation"><a href="../teaching/">← All teaching resources</a><a href="06.01.html">Lecture + Problems</a><a href="pdf/06.01-solutions.pdf" download>Solutions PDF</a></nav>' if solutions else
           '<nav class="sheet-nav" aria-label="Handout navigation"><a href="../teaching/">← All teaching resources</a><a href="#lab-expansion">Interactive experiments</a><a href="06.01-solutions.html">Worked solutions →</a></nav>')
    klass = 'sheet-page cosmology-solutions' if solutions else 'sheet-page cosmology-lecture'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Comprehensive MAIS PAC Cosmology handout: Olympiad-level lecture notes, 30 problems, worked solutions, vector diagrams and five interactive experiments.">
<meta name="theme-color" content="#ffffff"><title>{title}</title>
<link rel="icon" type="image/png" href="data:image/png;base64,{icon}"><style>{css}</style><script data-pac-sticky>{(ROOT/'scripts/header.js').read_text()}</script></head>
<body><a class="skip-link" href="#sheet">Skip to {'solutions' if solutions else 'handout'}</a>
<div class="handout-bar"><div class="handout-bar__inner"><a href="../teaching/">← MAIS Physics &amp; Astronomy Club</a><div class="handout-bar__links">{top}<button class="print-btn" type="button" onclick="window.print()">Print / PDF</button></div></div></div>
<main class="{klass}" id="sheet"><div class="running-head"><a class="brand-link" href="../" aria-label="MAIS PAC home">MAIS PAC</a><span>{running}</span></div>
<header class="sheet-title-block"><h1>{heading}</h1><p class="sheet-subtitle">{subtitle}</p><p class="cosmo-meta">{'30 worked solutions · independent explanations · source attribution' if solutions else '15 lecture sections · 30 problems · 5 interactive experiments · 6 vector figures'}</p></header>
<div class="sheet-intro">{intro}</div>
<div class="cosmo-quicklinks">{'<a href="06.01.html">Lecture + Problems</a><a href="pdf/06.01.pdf">Lecture PDF</a><a href="../teaching/#curriculum-5">Cosmology curriculum</a>' if solutions else '<a href="#cosmo-section-1">Start the lecture</a><a href="#cosmo-section-16">Problem set</a><a href="#lab-expansion">Experiments</a><a href="06.01-solutions.html">Solutions</a><a href="#cosmo-section-15">Sources</a>'}</div>
{content}{nav}</main>{script}</body></html>'''


def build():
    lecture_md = read('lecture-core.md')+'\n\n'+read('lecture-frontiers.md')+'\n\n'+format_problem_parts(read('problems.md'))
    # Place the contents immediately after the title/introduction, before Section 1.
    lecture_md = lecture_md.replace('\n\n<div id="cosmo-toc"></div>\n\n','\n\n')
    lecture_md = '<div id="cosmo-toc"></div>\n\n'+lecture_md
    solutions_md = '<div id="cosmo-toc"></div>\n\n'+read('solutions-foundations.md')+'\n\n'+read('solutions-challenges.md')
    lecture = page('06.01: Cosmology — Lecture + Problems · MAIS PAC',
                   '06.01: Cosmology · Lecture + Problems',
                   'Cosmology: From the Hubble Law to the Early Universe',
                   'MAIS Physics &amp; Astronomy Club (PAC) · Olympiad lecture + problem handout',
                   '<p>Begin with a question a ruler could answer: <em>what changes when the universe expands?</em> From that picture we build redshift, gravity, cosmic distances and the thermal history of the universe. Sophisticated ideas are introduced through physical reasoning before the formalism. The 30 problems include website-sourced adaptations and new IOAA-inspired challenges; every one has a worked solution.</p>',
                   render_markdown(lecture_md))
    solutions = page('06.01: Cosmology — Worked Solutions · MAIS PAC',
                     '06.01: Cosmology · Worked Solutions',
                     'Cosmology: Worked Solutions',
                     'MAIS Physics &amp; Astronomy Club (PAC) · Reasoning, derivations and checks',
                     '<p>Read a solution after making a genuine attempt. The difficult original challenges include an <strong>Idea</strong> paragraph explaining how to choose the method, an explicit <strong>IOAA connection</strong>, and final consistency checks. These are independent MAIS PAC solutions, not official marking schemes. Rounded benchmark parameters are teaching choices, not claims about the latest observational consensus.</p>',
                     render_markdown(solutions_md), solutions=True)
    (ROOT/'handouts'/'06.01.html').write_text(lecture)
    (ROOT/'handouts'/'06.01-solutions.html').write_text(solutions)
    # Machine-readable checks and the same transparent data used by the lab.
    subprocess.run([sys.executable,str(ROOT/'scripts'/'cosmology_model.py')],check=True,capture_output=True)
    for name,html in [('06.01.html',lecture),('06.01-solutions.html',solutions)]:
        soup=BeautifulSoup(html,'html.parser')
        words=len(soup.get_text(' ',strip=True).split())
        print(f'{name}: {len(html):,} characters, ~{words:,} words, {len(soup.select("svg"))} SVGs')
    print('Built self-contained Cosmology HTML, embedded fonts and synthetic practice data.')

if __name__=='__main__':
    build()
