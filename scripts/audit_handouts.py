"""Structural re-audit for the handout set (Errata cycle 2+).

Checks generated HTML for unresolved templates, KaTeX errors, duplicate IDs,
broken SVG marker references, internal links/anchors, problem/solution pairing,
Club navigation, and removal of the Explore Mechanics feature card.
"""
from __future__ import annotations
import re
from pathlib import Path
from urllib.parse import unquote, urlparse
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
HANDOUTS = ROOT / 'handouts'
issues: list[str] = []

def issue(where: str, msg: str) -> None:
    issues.append(f'{where}: {msg}')

# --- Generated handout HTML -------------------------------------------------
codes = [f'01.0{i}' for i in range(1, 6)] + ['06.01'] + [
    '07.01', '07.02', '08.01', '08.02', '08.03', '08.04', '08.05',
    '09.01', '09.02', '09.03', '09.04', '10.01', '10.02', '10.03', '10.04']
legacy = ['A1', 'A2', 'A3', 'P1', 'P2', 'P3']
all_codes = codes + legacy

for code in all_codes:
    for suffix in ('', '-solutions'):
        p = HANDOUTS / f'{code}{suffix}.html'
        if not p.exists():
            issue(p.name, 'missing file')
            continue
        soup = BeautifulSoup(p.read_text(), 'html.parser')
        ids = [el['id'] for el in soup.select('[id]')]
        for i in sorted({i for i in ids if ids.count(i) > 1}):
            issue(p.name, f'duplicate id {i}')
        idset = set(ids)
        for svg in soup.find_all('svg'):
            local = {el['id'] for el in svg.select('[id]')}
            for el in svg.find_all():
                for attr, val in el.attrs.items():
                    if isinstance(val, str):
                        for ref in re.findall(r'url\(#([^)]+)\)', val):
                            if ref not in local and ref not in idset:
                                issue(p.name, f'unresolved SVG reference #{ref} in {attr}')
        if soup.select('.katex-error'):
            issue(p.name, f'{len(soup.select(".katex-error"))} KaTeX errors')
        text = soup.get_text(' ', strip=True)
        for token in re.findall(r'\{\{[^}]+\}\}', text):
            issue(p.name, f'unresolved template {token}')
        # Internal links and anchors.
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith(('mailto:', 'http:', 'https:', '#')):
                if href.startswith('#') and href[1:] and href[1:] not in idset:
                    issue(p.name, f'broken local anchor {href}')
                continue
            parsed = urlparse(href)
            path = unquote(parsed.path)
            if not path:
                continue
            target = (p.parent / path).resolve()
            if not target.exists():
                issue(p.name, f'broken link {href}')
            elif parsed.fragment and target.suffix == '.html':
                tsoup = BeautifulSoup(target.read_text(), 'html.parser')
                if not tsoup.find(id=parsed.fragment):
                    issue(p.name, f'broken cross-file anchor {href}')
        if code in codes:
            expected = 30 if code == '06.01' else (15 if code.startswith('01.') else 10)
            if suffix == '':
                n = len(soup.select('.problem'))
                if n != expected:
                    issue(p.name, f'expected {expected} problems, found {n}')
            else:
                n = len(soup.select('.solution'))
                if n != expected:
                    issue(p.name, f'expected {expected} solutions, found {n}')

# --- Site navigation and requested removals --------------------------------
main_pages = ['index.html', 'about/index.html', 'club/index.html', 'teaching/index.html',
              'explore/index.html', 'resources/index.html', '404.html',
              'scripts/teaching-template.html', 'mechanics/index.html', 'scripts/mechanics/page-template.html']
for rel in main_pages:
    p = ROOT / rel
    soup = BeautifulSoup(p.read_text(), 'html.parser')
    nav = soup.select_one('.site-nav')
    if not nav or not nav.find('a', string='Club'):
        issue(rel, 'missing Club navigation link')
    if soup.select('[data-mechanics-feature]'):
        issue(rel, 'Mechanics feature card still present')
explore = BeautifulSoup((ROOT / 'explore/index.html').read_text(), 'html.parser')
if 'Mechanics Playground' in explore.get_text():
    issue('explore/index.html', 'Mechanics Playground card text still present')
if not (ROOT / 'club/index.html').exists():
    issue('club/index.html', 'missing Club page')

# --- Report -----------------------------------------------------------------
if issues:
    print('AUDIT FAIL')
    for i in issues:
        print(' -', i)
    raise SystemExit(1)
print(f'AUDIT PASS: {len(all_codes) * 2} handout HTML files, {len(main_pages)} navigation pages; '
      'no unresolved templates, KaTeX errors, duplicate IDs, broken SVG refs, broken internal links, '
      'or problem/solution count mismatches. Club nav present; Explore feature card absent.')
