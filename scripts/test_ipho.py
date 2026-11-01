"""Structural tests for IPhO guides and their syllabus reading copy."""
from pathlib import Path
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup
import pymupdf
R = Path(__file__).resolve().parents[1]
for key in ('ipho-theory', 'ipho-experimental', 'ipho-mathematics'):
    counts = []
    for suffix in ('', '-solutions'):
        path = R / 'handouts' / f'{key}{suffix}.html'
        soup = BeautifulSoup(path.read_text(), 'html.parser')
        counts.append(len(soup.select('.solution' if suffix else '.problem')))
        for a in soup.find_all('a', href=True):
            url = urlparse(a['href'])
            if url.scheme or not url.path: continue
            target = (path.parent / unquote(url.path)).resolve()
            assert target.exists(), (path, a['href'])
            if url.fragment and target.name == 'index.html':
                assert BeautifulSoup(target.read_text(), 'html.parser').find(id=url.fragment), (path, a['href'])
    assert counts[0] > 0 and counts[0] == counts[1], (key, counts)
    print(key, counts[0], 'matched problems and solutions')
pdf = pymupdf.open(R / 'teaching/pdf/ipho-syllabus.pdf')
assert len(pdf) == 6 and 'reading copy' in pdf[0].get_text().lower()
print('IPhO syllabus reading copy: 6 pages')
