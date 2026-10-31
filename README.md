# mais-pac.github.io

The Physics & Astronomy Club (PAC) at Mongol Aspiration International School in Ulaanbaatar, Mongolia. Its aim is to give students a starting point in astronomy and physics, and a place where questions can be asked until they become understanding.

Live site: <https://mais-pac.github.io/>

## Structure

A static academic website with physics and astronomy club handouts, the Cosmic Calculation Series, and teaching resources.

```
index.html                  Club homepage
about/index.html            Club background
teaching/index.html         Curriculum, lecture PDFs, problem sets, and handouts
handouts/                   Six handouts and six worked-solution pages
handouts/pdf/               Downloadable PDFs of the handouts and solutions
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
