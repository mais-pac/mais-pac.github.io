# Basic Astrophysics — HTML-first handouts

Topics `01.01`–`01.05` now use the same sheet design as Cosmology (`06.01`): running head, boxed title/introduction, numbered equations, theorem/problem/solution boxes, vector figures, an interactive experiment, and separate worked-solution pages.

| Code | Topic | Lecture | Solutions |
|---|---|---|---|
| 01.01 | Celestial Mechanics | `handouts/01.01.html` | `handouts/01.01-solutions.html` |
| 01.02 | Electromagnetic Theory & Quantum Physics | `handouts/01.02.html` | `handouts/01.02-solutions.html` |
| 01.03 | Thermodynamics | `handouts/01.03.html` | `handouts/01.03-solutions.html` |
| 01.04 | Spectroscopy and Atomic Physics | `handouts/01.04.html` | `handouts/01.04-solutions.html` |
| 01.05 | Nuclear Physics | `handouts/01.05.html` | `handouts/01.05-solutions.html` |

Each topic has 8 lecture sections, 15 original graded problems, 15 worked solutions, 2 vector figures and 1 interactive experiment. PDFs are exported to `handouts/pdf/01.0x.pdf` and `handouts/pdf/01.0x-solutions.pdf`. The earlier theory/index PDFs in `teaching/pdf/01.0x-problems.pdf` are retained as archives.

## Build

```bash
npm run build:basic       # render Markdown + KaTeX + SVG + labs into self-contained HTML
npm run pdf:basic         # Playwright print export to handouts/pdf/
npm run integrate:basic   # connect the five HTML cards in Teaching
npm run test:basic        # offline checks; set BASE_URL for live checks
```

Sources live in `scripts/basic/01.0x/{lecture,problems,solutions}.md`, with shared `figures.py`, `labs.py` and `labs.js`. The builder reuses the Cosmology stylesheet and KaTeX font embedding so the visual design matches exactly.

## Syllabus PDF

`npm run build:syllabus` rebuilds `teaching/pdf/ioaa-syllabus.pdf` in the black-and-white official-style format: title/General Notes page, then two-column Contents/Remarks tables. It keeps the newer 17 November 2021 syllabus content while following the layout of the USAAAO-hosted reference PDF.

## Provenance

The exercises and solutions are original MAIS PAC teaching material inspired by the syllabus skills. They are not official IOAA questions or marking schemes. Each lecture’s “Further practice” section lists official past-paper identifiers from the earlier club compilation without reproducing copyrighted question statements.
