# IPhO curriculum (complete)

The IPhO section of the Teaching page now carries a complete, topic-by-topic
curriculum: 24 syllabus topics in 8 groups, redesigned in the same house style
as the IOAA curriculum. Every topic has

* a lecture written from scratch, with vector figures and a worked reasoning path;
* five inline SVGs (the shared figure kit in `scripts/ipho/figures.py`);
* exactly one interactive experiment (pure HTML controls + inline SVG, no network);
* ten original graded problems (`[1]`/`[2]`/`[3]`) and ten worked solutions, each
  ending in a `**Check:**` consistency line.

The material is original MAIS PAC practice, not official IPhO questions. The
syllabus is the coverage checklist; use the official past papers for timed
integrated practice.

| group | topics |
| --- | --- |
| Foundations | 01.01 |
| Mechanics and fields | 02.01–02.16 |
| Experimental skills | 03.01–03.03 |
| Mathematics | 04.01–04.04 |

The three older introductory guides (`handouts/ipho-theory.html`,
`ipho-experimental.html`, `ipho-mathematics.html`) remain available online and as
PDFs.

## Build and check

```sh
npm ci                                     # KaTeX for the maths renderer
.venv/bin/pip install -r requirements.txt  # reportlab, xhtml2pdf, PyMuPDF, Markdown, bs4

python scripts/build_ipho_curriculum.py [04.01 ...]   # HTML pairs into handouts/
python scripts/integrate_ipho.py                      # cards + PDF links on Teaching
python scripts/build_ipho_pdfs.py [04.01 ...]         # handouts/pdf/ipho-*.pdf
python scripts/audit_handouts.py                      # structural audit (now covers IPhO)
python scripts/build_ipho.py; python scripts/build_ipho_syllabus.py; python scripts/test_ipho.py
```

## Source layout

| path | contents |
| --- | --- |
| `scripts/ipho_topics.py` | the 24 topics, codes, titles and groups |
| `scripts/ipho/NN.NN.md` | lecture, `{{FIG:key}}`/`{{LAB:key}}` slots, problems, solutions |
| `scripts/ipho/_parts/NN.NN.py` | `FIGURES` and `LABS` for one topic |
| `scripts/ipho/labs/NN.NN.js` | the lab model + draw code; exports a testable model function |
| `scripts/ipho/figures.py`, `labs.py`, `labs.js` | shared figure kit, control helpers, browser runtime |
| `scripts/build_ipho_curriculum.py` | markdown → HTML, and `compile_labs()` for `labs.js` |

`compile_labs()` concatenates the per-topic JS fragments into
`scripts/ipho/labs.js`; run it (or just run the builder) after editing any
fragment. Each fragment ends with `init.<key> = fn;` and `EXPORTS.<model> = …`,
and every generated model function is a pure function so it can be tested in
Node without a browser.

## PDF export notes

`build_ipho_pdfs.py` reuses the print CSS and masthead from
`build_handout_pdfs.py`. Two things need care because the curriculum sheets are
self-contained:

* the sheet's inline stylesheet includes KaTeX; every formula is therefore
  flattened back to a linear text form from its KaTeX annotation before export;
* xhtml2pdf cannot draw inline SVG, so each figure is rasterised with PyMuPDF
  and embedded as a PNG. Interactive labs are replaced by a one-line note.

The attached 2014/2015 syllabus is preserved as
`teaching/pdf/ipho-syllabus-supplied.pdf`; `ipho-syllabus.pdf` is a reading copy
with a provenance cover. Consult the
[IPhO syllabus webpage](https://www.ipho-new.org/statutes-syllabus/) for current
requirements.

## Limits

The handout audit checks structure — unresolved templates, KaTeX errors,
duplicate IDs, broken SVG references, internal anchors and problem/solution
counts — not scientific correctness. Content was reviewed figure by figure and
lab by lab during authoring, but independent review is still welcome; please
open an issue with the topic code.
