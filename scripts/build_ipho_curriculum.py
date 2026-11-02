"""Build the IPhO HTML-first curriculum (same structure as the IOAA handouts).

Run from the repository root after `npm install` and with the Python
dependencies in requirements.txt:

    .venv/bin/python scripts/build_ipho_curriculum.py            # all topics
    .venv/bin/python scripts/build_ipho_curriculum.py 01.01      # one topic

Each topic is one Markdown source in scripts/ipho/<code>.md containing a
lecture, `{{FIG:...}}` and `{{LAB:...}}` components, then `<!-- PROBLEMS -->`
and `<!-- SOLUTIONS -->` blocks. The output is a pair of self-contained HTML
files in handouts/ (`NN.NN.html` and `NN.NN-solutions.html`) using the same
sheet theme, KaTeX pipeline, figure kit and experiment machinery as the IOAA
curriculum, so the two programmes look and behave identically.
"""
from pathlib import Path
import base64
import json
import re
import subprocess
import sys

import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'scripts' / 'ipho'))

from build_cosmology import katex_css, format_problem_parts  # noqa: E402
from ipho_topics import TOPICS, PROBLEMS_PER_TOPIC  # noqa: E402
from ipho.parts import FIGURES, LABS  # noqa: E402
from ipho_reading import references  # noqa: E402

SRC = ROOT / 'scripts' / 'ipho'
N = PROBLEMS_PER_TOPIC
LAB_HEADER = '/* === TOPIC FRAGMENTS === */'


def compile_labs():
    """Rebuild scripts/ipho/labs.js from the per-topic fragments.

    The generated file is the one the handouts embed, so a topic's experiment
    code travels with the topic rather than inside one shared script.
    """
    script = (SRC / 'labs.js').read_text()
    head, _, tail = script.partition(LAB_HEADER)
    tail = tail[tail.index('for (const [key, start]'):]
    fragments = ''
    for path in sorted((SRC / 'labs').glob('*.js')):
        fragments += f'\n/* ---- {path.stem} ---- */\n' + path.read_text().strip() + '\n'
    if 'const init = {}, EXPORTS' not in head:
        raise ValueError('labs.js header is missing the init/EXPORTS registry')
    (SRC / 'labs.js').write_text(head + LAB_HEADER + '\n' + fragments + '\n' + tail)


def render(source):
    """Markdown -> HTML with pre-rendered KaTeX and expanded components."""
    maths = []

    def stash(match, display):
        index = len(maths)
        maths.append({'tex': match.group(1).strip(), 'display': display})
        if display:
            return f'\n\nMATHBLOCK{index:04d}END\n\n'
        return f'MATHINLINE{index:04d}END'

    source = re.sub(r'\$\$(.*?)\$\$', lambda m: stash(m, True), source, flags=re.S)
    source = re.sub(r'(?<!\$)\$([^\n$]+?)\$(?!\$)', lambda m: stash(m, False), source)
    html = markdown.markdown(source, extensions=['extra', 'toc', 'sane_lists', 'md_in_html'])
    if maths:
        result = subprocess.run(
            ['node', str(ROOT / 'scripts' / 'render_cosmology_math.mjs')],
            input=json.dumps(maths), text=True, capture_output=True, check=True,
        )
        for i, (m, rendered) in enumerate(zip(maths, json.loads(result.stdout))):
            if m['display']:
                number = sum(item['display'] for item in maths[:i + 1])
                token = f'MATHBLOCK{i:04d}END'
                box = (f'<div class="eq"><div class="eq__expr">{rendered}</div>'
                       f'<span class="eq__num">({number})</span></div>')
                html = html.replace(f'<p>{token}</p>', box).replace(token, box)
            else:
                html = html.replace(f'MATHINLINE{i:04d}END', rendered)
    html = expand(html, 'FIG', FIGURES)
    html = expand(html, 'LAB', LABS)
    if 'MATHBLOCK' in html or 'MATHINLINE' in html or '{{' in html:
        raise ValueError('Unrendered mathematics or component placeholder')
    return html


def expand(html, kind, registry):
    def replace(match):
        name = match.group(1)
        if name not in registry:
            raise KeyError(f'Unknown {kind} component: {name}')
        component = registry[name]
        return component() if callable(component) else component
    html = re.sub(rf'<p>\{{\{{{kind}:([\w-]+)\}}\}}</p>', replace, html)
    return re.sub(rf'\{{\{{{kind}:([\w-]+)\}}\}}', replace, html)


def page(topic, body, solutions=False):
    code = topic['code']
    key = topic['key']
    name = topic['title']
    group = topic['group']
    soup = BeautifulSoup(body, 'html.parser')
    links = []
    problem_anchor = None
    for table in soup.find_all('table'):
        table.wrap(soup.new_tag('div', attrs={'class': 'table-scroll'}))
    for i, heading in enumerate(soup.find_all('h2'), 1):
        heading['id'] = f'ipho-section-{i}'
        title = re.sub(r'^\d+\.\s*', '', heading.get_text(' ', strip=True))
        links.append((heading['id'], title))
        if 'Problems' in title:
            problem_anchor = heading['id']
    if solutions:
        toc = ('<nav class="cosmo-toc" aria-label="Solution index"><strong>Solution index</strong>'
               '<div class="solution-index">'
               + ''.join(f'<a href="#s{i}" aria-label="Solution {i}">{i}</a>' for i in range(1, N + 1))
               + '</div></nav>')
    else:
        toc = ('<details class="cosmo-toc" open><summary>Contents &amp; learning path</summary><ol>'
               + ''.join(f'<li><a href="#{ident}">{text}</a></li>' for ident, text in links)
               + '</ol></details>')
    lab = soup.select_one('.cosmo-lab')
    lab_anchor = lab['id'] if lab else f'lab-{key}'
    content = str(soup).replace('<div id="curriculum-toc"></div>', toc)
    icon = base64.b64encode((ROOT / 'assets' / 'club-logo.png').read_bytes()).decode()
    css = ((ROOT / 'style.css').read_text() + '\n'
           + (ROOT / 'scripts' / 'cosmology' / 'cosmology.css').read_text() + '\n'
           + katex_css() + '\n'
           + '.curriculum-solutions .solution{break-inside:auto}\n'
           + '.lab-unit{color:#6e767d;font-weight:400}\n'
           + '.ipho-refs{display:grid;gap:9px;margin:14px 0 4px}\n'
           + '.ipho-ref{border-left:3px solid #bfdbfe;padding:2px 0 2px 12px;font:13px/1.6 var(--sans)}\n'
           + '.ipho-ref a{font-weight:650}\n'
           + '.ipho-ref span{display:block;color:#526079}\n')
    if solutions:
        top = (f'<a href="{code}.html">Lecture + Problems</a><strong>Solutions</strong>'
               f'<a class="pdf-download" href="pdf/ipho-{code}-solutions.pdf" download>Solutions PDF</a>')
    else:
        top = (f'<strong>IPhO {code}</strong><a href="{code}-solutions.html">Solutions</a>'
               f'<a class="pdf-download" href="pdf/ipho-{code}.pdf" download>Download PDF</a>')
    if solutions:
        quick = (f'<a href="{code}.html">Lecture + Problems</a>'
                 f'<a href="pdf/ipho-{code}.pdf">Lecture PDF</a>'
                 f'<a href="../teaching/#ipho-curriculum-{group}">{topic["group_name"]} curriculum</a>')
    else:
        quick = (f'<a href="#ipho-section-1">Start the lecture</a>'
                 + (f'<a href="#{problem_anchor}">Problem set</a>' if problem_anchor else '')
                 + f'<a href="#{lab_anchor}">Interactive experiment</a>'
                 f'<a href="{code}-solutions.html">Worked solutions →</a>')
    if solutions:
        nav = (f'<nav class="sheet-nav" aria-label="Handout navigation">'
               f'<a href="../teaching/">← All teaching resources</a>'
               f'<a href="{code}.html">Lecture + Problems</a>'
               f'<a href="pdf/ipho-{code}-solutions.pdf" download>Solutions PDF</a></nav>')
    else:
        nav = (f'<nav class="sheet-nav" aria-label="Handout navigation">'
               f'<a href="../teaching/">← All teaching resources</a>'
               f'<a href="#{lab_anchor}">Interactive experiment</a>'
               f'<a href="{code}-solutions.html">Worked solutions →</a></nav>')
    heading = name + (': Worked Solutions' if solutions else '')
    subtitle = 'MAIS Physics &amp; Astronomy Club (PAC) · ' + (
        'Reasoning, derivations and checks' if solutions else 'IPhO lecture + problem handout')
    if solutions:
        meta = f'{N} worked solutions · independent explanations · consistency checks'
    else:
        meta = f'{len(links) - 2} lecture sections · {N} problems · 1 interactive experiment · 5 vector figures'
    if solutions:
        intro = ('<p>Make a genuine attempt before reading. Each solution explains how to choose the method, carries '
                 'units through the calculation, and checks the result. The exercises are original MAIS PAC teaching '
                 'problems, not official IPhO questions or marking schemes. Parameters are supplied locally; an exam’s '
                 'constants take precedence.</p>')
    else:
        intro = ('<p>Start with a physical picture, then introduce only the mathematics needed to make it predictive. '
                 'The lecture connects everyday reasoning to olympiad measurements. Five vector diagrams and an '
                 'interactive experiment support the argument; ten graded problems and independent worked solutions '
                 'turn the ideas into practice. The coverage checklist is the IPhO syllabus, not this handout.</p>')
    script = '' if solutions else '<script>' + (SRC / 'labs.js').read_text() + '</script>'
    header = '<script data-pac-sticky>' + (ROOT / 'scripts' / 'header.js').read_text() + '</script>'
    label = 'Solutions' if solutions else 'handout'
    classes = 'cosmology-solutions curriculum-solutions' if solutions else 'cosmology-lecture curriculum-lecture'
    running = 'Worked Solutions' if solutions else 'Lecture + Problems'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="MAIS PAC IPhO {name}: Olympiad lecture, {N} original problems and worked solutions, vector figures and interactive experiment."><meta name="theme-color" content="#ffffff"><title>IPhO {code}: {heading} · MAIS PAC</title><link rel="icon" type="image/png" href="data:image/png;base64,{icon}"><style>{css}</style>{header}</head><body><a class="skip-link" href="#sheet">Skip to {label}</a><div class="handout-bar"><div class="handout-bar__inner"><a href="../teaching/">← MAIS Physics &amp; Astronomy Club</a><div class="handout-bar__links">{top}<button class="print-btn" type="button" onclick="window.print()">Print / PDF</button></div></div></div><main class="sheet-page {classes}" id="sheet" data-topic="ipho-{code}"><div class="running-head"><a class="brand-link" href="../" aria-label="MAIS PAC home">MAIS PAC</a><span>IPhO {code}: {name} · {running}</span></div><header class="sheet-title-block"><h1>{heading}</h1><p class="sheet-subtitle">{subtitle}</p><p class="cosmo-meta">{meta}</p></header><div class="sheet-intro">{intro}</div><div class="cosmo-quicklinks">{quick}</div>{content}{nav}</main>{script}</body></html>'''


def provenance(topic):
    return f'''
## Further practice and provenance

The {N} exercises above and their solutions are **original MAIS PAC problems**, inspired by the skills in this IPhO syllabus topic. They are not copied from official papers and are not official marking schemes.

<div class="remark" markdown="1"><span class="remark-head">Sources and scope.</span> Topic coverage follows the IPhO syllabus (accepted 2014, amended 2015) as published by the [IPhO organisation](https://www.ipho-new.org/statutes-syllabus/). Official problems are available through the [IPhO past-paper archive](https://www.ipho-new.org/documentations/). The derivations, diagrams, experiments and numerical teaching examples in this handout were prepared independently for MAIS PAC. Calculator-level methods are emphasized; optional calculus connections are explicitly identified. 
Synthetic data, when used, are labelled as teaching data.</div>

## Where to learn more

{references(topic['group_name'])}
'''


def counts(html, solutions):
    soup = BeautifulSoup(html, 'html.parser')
    return (len(soup.select('.solution' if solutions else '.problem')),
            len(soup.select('.cosmo-figure')), len(soup.select('.cosmo-lab')))


def build(only=None):
    compile_labs()
    for topic in TOPICS:
        code = topic['code']
        if only and code not in only:
            continue
        source_path = SRC / f'{code}.md'
        if not source_path.exists():
            print(f'{code}  (no source yet — skipped)')
            continue
        raw = source_path.read_text()
        lecture, rest = raw.split('<!-- PROBLEMS -->', 1)
        problems, solutions = rest.split('<!-- SOLUTIONS -->', 1)
        problems = format_problem_parts(problems.strip())
        section_count = len(re.findall(r'^## ', lecture, flags=re.M))
        lecture = (lecture.strip()
                   + f'\n\n## {section_count + 1}. Problems: reason, calculate, check\n\n'
                     'Ten original problems in three tiers: **[1]** foundation, **[2]** multi-step olympiad '
                     'reasoning, **[3]** challenge. Use the constants supplied in the lecture unless a question '
                     'overrides them. State assumptions, keep units, and estimate the answer before computing it. '
                     'Every problem has a worked solution with a consistency check.\n\n'
                   + problems + provenance(topic))
        for suffix, body, is_solution in [('', '<div id="curriculum-toc"></div>\n\n' + lecture, False),
                                          ('-solutions', '<div id="curriculum-toc"></div>\n\n' + solutions.strip(), True)]:
            html = page(topic, render(body), is_solution)
            (ROOT / 'handouts' / f'{code}{suffix}.html').write_text(html)
            found, figures, labs = counts(html, is_solution)
            if found != N:
                raise ValueError(f'{code}{suffix}: expected {N} {"solutions" if is_solution else "problems"}, got {found}')
            if not is_solution and (figures < 5 or labs < 1):
                raise ValueError(f'{code}: expected at least 5 figures and 1 lab, got {figures} and {labs}')
            words = len(BeautifulSoup(html, 'html.parser').get_text(' ', strip=True).split())
            print(f'{code}{suffix}  words {words}  figures {figures}  labs {labs}')
        print(f'   built IPhO {code}: {topic["title"]}')


if __name__ == '__main__':
    build(set(sys.argv[1:]) or None)
