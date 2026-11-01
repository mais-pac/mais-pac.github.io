# Extended curriculum handouts (07–10)

HTML-first lecture notes in the same sheet theme as Cosmology 06.01.

## Topics

- 07.01 Multi-wavelength Astronomy
- 07.02 Instrumentation
- 08.01 Numerical Methods
- 08.02 Basic Calculus
- 08.03 Vectors
- 08.04 Geometric Instruments
- 08.05 Statistics & Error Analysis
- 09.01 Naked-Eye Observations
- 09.02 Sky Maps and Catalogues
- 09.03 Observational Coordinates and Estimates
- 09.04 Astronomical Instruments
- 10.01 Error Sources
- 10.02 Graphs and Best Fit
- 10.03 Geometrical Instruments in Practice
- 10.04 Experimental Techniques

Each topic has 6 lecture sections, 2 vector figures, 1 interactive experiment, 10 original problems and 10 worked solutions. Lecture and solutions pages have A4 PDFs.

## Build

```bash
python scripts/build_curriculum.py          # all topics
python scripts/build_curriculum.py 08.01    # subset
python scripts/integrate_curriculum.py      # Teaching cards + WEB_HANDOUTS
node scripts/export_curriculum.mjs          # 30 PDFs
node scripts/test_curriculum.mjs            # offline
BASE_URL=http://127.0.0.1:3000/handouts/ node scripts/test_curriculum.mjs
```

npm scripts: `build:curriculum`, `integrate:curriculum`, `pdf:curriculum`, `test:curriculum`.

## Sources

- `scripts/curriculum_topics.py`: topic registry.
- `scripts/extended/{code}.md`: lecture, problems and solutions separated by `<!-- PROBLEMS -->` and `<!-- SOLUTIONS -->`.
- `scripts/extended/figures.py`: 30 inline SVG figures.
- `scripts/extended/labs.py` and `labs.js`: 15 interactive experiments; `window.CurriculumLabs` exposes pure models for tests.
- `scripts/build_curriculum.py`: renders KaTeX, figures, labs and the Cosmology sheet theme.

Problems are original MAIS PAC teaching exercises inspired by the IOAA syllabus; they are not official IOAA questions or marking schemes. Synthetic lab data are labelled as teaching data.
