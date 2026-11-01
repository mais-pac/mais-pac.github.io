"""Build the self-contained Mechanics Playground page."""
from pathlib import Path
import base64
ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'scripts'/'mechanics'
OUT=ROOT/'mechanics'
OUT.mkdir(exist_ok=True)
css=(ROOT/'style.css').read_text()+'\n'+(SRC/'mechanics.css').read_text()
js=(SRC/'mechanics.js').read_text()
icon='data:image/png;base64,'+base64.b64encode((ROOT/'assets'/'club-logo.png').read_bytes()).decode()
html=(SRC/'page-template.html').read_text().replace('{{CSS}}',css).replace('{{JS}}',js).replace('{{ICON}}',icon).replace('{{HEADER_JS}}',(ROOT/'scripts'/'header.js').read_text())
(OUT/'index.html').write_text(html)
print(f'Built mechanics/index.html ({len(html):,} characters)')
