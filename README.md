# mais-pac.github.io

The Physics & Astronomy Club (PAC) at Mongol Aspiration International School in Ulaanbaatar, Mongolia. Its aim is to give students a starting point in astronomy and physics, and a place where questions can be asked until they become understanding.

Live site: <https://mais-pac.github.io/>

## Structure

A static academic website with physics and astronomy club handouts, the Cosmic Calculation Series, and teaching resources.

```
index.html                  Club homepage
about/index.html            Club background
teaching/index.html         Curriculum, lecture PDFs, problem sets, and handouts
handouts/                   Six legacy handouts, Cosmology 06.01, and Basic Astrophysics 01.01–01.05
handouts/pdf/               Downloadable PDFs of the handouts and solutions
mechanics/index.html        Self-contained Mechanics Playground (13 interactive simulations)
scripts/build_mechanics.py  Build the Mechanics Playground page
scripts/build_basic.py      Build the five HTML-first Basic Astrophysics handouts
scripts/build_syllabus.py   Build the official-style IOAA syllabus PDF
scripts/build_teaching.py   Build Teaching page and curriculum PDFs
scripts/build_handout_pdfs.py  Export the existing HTML handouts as PDFs
scripts/lecture_content.py  Original theory notes and past-paper identifiers
scripts/question_sets.py   Original practice exercises for Coordinates and Times
style.css                   Site layout and colorful print/handout styles
assets/club-logo.png        Club crest
```

## Local preview

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

## Basic Astrophysics

`01.01`–`01.05` use the same HTML-first design as Cosmology: lecture notes, 15 original problems and worked solutions per topic, vector figures, one interactive experiment per topic, and downloadable PDFs. See `README_BASIC.md`.

## Mechanics Playground

`mechanics/` is a visual-first mechanics lab: pendulum, projectiles, ramp friction, force and motion, springs/resonance, collisions, energy coaster, orbits, torque, Atwood machine, rolling race, Newton’s cradle, and standing waves. Each experiment has sliders, live readouts, a challenge, and an optional “Show the physics” panel. The page is fully self-contained (inline CSS/JS/SVG) and works offline.

```bash
npm run build:mechanics       # rebuild mechanics/index.html from scripts/mechanics/
npm run integrate:mechanics   # add nav links and featured cards (idempotent)
npm run test:mechanics        # Playwright checks; set BASE_URL for live or file:// offline
```

See `README_MECHANICS.md` for the experiment list, models, and teaching notes.

## Teaching curriculum and PDFs

`teaching/` contains 37 topic blocks based on the IOAA syllabus, a reformatted syllabus PDF, and an FAQ PDF. Each Basic Astrophysics topic (01.01–01.05) now has a theory-first lecture PDF. Its final pages provide 16–26 official past-paper identifiers (year, round, question label); the copyrighted question statements are not reproduced. Each lecture PDF includes the requested notice: “The following questions are from official past IOAA problem sets.”

The Coordinates and Times PDFs (02.01–02.02) remain original MAIS PAC practice sets. Other Problems PDFs and the Solutions PDFs are clearly marked placeholders. The curriculum and handout PDFs carry a repeated, clickable MAIS PAC website badge at the top left and use the shared color-box style.

The existing six physics/astronomy handouts and their six solution pages remain available as HTML. Downloadable, styled PDF exports are in `handouts/pdf/` and linked from Teaching and from each handout page. DejaVu font files needed for those exports are included in `handouts/pdf/fonts/` with their license.

The syllabus study edition is based on the IOAA syllabus updated 17 November 2021. Club topic codes and practical-topic labels are organizational aids, not official IOAA designations.

## Rebuilding PDFs

Create a virtual environment, install the build dependencies, and run both generators:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/build_teaching.py
.venv/bin/python scripts/build_handout_pdfs.py
```

`build_teaching.py` requires DejaVu Sans at `/usr/share/fonts/truetype/dejavu/`. It builds the curriculum page, all curriculum PDFs, the five theory-first Basic Astrophysics PDFs, the two original Coordinates and Times practice PDFs, placeholders, syllabus and FAQ. `build_handout_pdfs.py` exports the twelve existing HTML pages and stamps every page with a clickable website badge.


## Extended curriculum (07–10)

Fifteen HTML-first handouts in the Cosmology sheet theme cover Instrumentation and Space Technologies, Mathematical Methods and Tools, and the Practical Part. Each topic has 10 original problems, 10 worked solutions, 2 vector figures, 1 interactive experiment and A4 PDFs. See `README_CURRICULUM.md` and the `*:curriculum` npm scripts.

## Handout quality assurance

The handout set was audited in two cycles. Findings and fixes are recorded in
[`ERRATA.md`](ERRATA.md) and published as [`handouts/errata.html`](handouts/errata.html).
Run `npm run audit:handouts` for the structural re-audit (templates, KaTeX, SVG
references, internal links, problem/solution counts, Club navigation and the
removed Explore feature card). Legacy P1–P3/A1–A3 PDFs are rebuilt with
`npm run pdf:legacy`.
