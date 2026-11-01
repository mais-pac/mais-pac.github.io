"""Keep Club and Mechanics Lab in navigation; use a quiet handout heading in Teaching.
No featured playground cards on Home, Teaching or Explore. Idempotent and formatting-preserving.
"""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
PAGES={'index.html':'','about/index.html':'../','club/index.html':'../','teaching/index.html':'../','explore/index.html':'../','resources/index.html':'../','scripts/teaching-template.html':'../','scripts/mechanics/page-template.html':'../'}

def add_nav(html,prefix):
    m=re.search(r'(<nav class="site-nav"[^>]*>)(.*?)(</nav>)',html,re.S)
    if not m: return html
    inner=m.group(2)
    if '>Club</a>' not in inner:
        t=re.search(r'<a[^>]*>About</a>',inner)
        if t: inner=inner[:t.end()]+f'\n        <a href="{prefix}club/">Club</a>'+inner[t.end():]
    if 'Mechanics Lab' not in inner:
        t=re.search(r'<a[^>]*>Teaching</a>',inner)
        if t: inner=inner[:t.end()]+f'\n        <a href="{prefix}mechanics/">Mechanics Lab</a>'+inner[t.end():]
    return html[:m.start(2)]+inner+html[m.end(2):]


for rel,prefix in PAGES.items():
    p=ROOT/rel; html=p.read_text(); html=add_nav(html,prefix)
    # The Mechanics Playground feature card was removed by request from Home,
    # Teaching and Explore. Keep the Mechanics Lab page and navigation item only.
    html=re.sub(r'\n?<section data-mechanics-feature\b.*?</section>\n?', '\n', html, flags=re.S)
    if rel in ('teaching/index.html','scripts/teaching-template.html'):
        heading=f'<h3 class="physics-mechanics-heading">Physics / <a href="{prefix}mechanics/">Mechanics Lab</a></h3>'
        html=re.sub(r'<h3(?: class="physics-mechanics-heading")?>Physics(?: / <a[^>]*>Mechanics Lab</a>)?</h3>',lambda _:heading,html,count=1)
    p.write_text(html); print('integrated',rel)
