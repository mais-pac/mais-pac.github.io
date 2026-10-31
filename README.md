# mais-pac.github.io

The Physics & Astronomy Club (PAC) at Mongol Aspiration International School in Ulaanbaatar, Mongolia. Its aim is to give students a starting point in astronomy and physics, and a place where questions can be asked until they become understanding.

Live site: <https://mais-pac.github.io/>

## Structure

A simple, static academic website with self-contained physics and astronomy club handouts — no build step, no JavaScript dependencies, no trackers, and no cookies.

```
index.html                  Club homepage
about/index.html            Club background
handouts/index.html         Physics & astronomy handout index
explore/index.html          Topics and learning approach
resources/index.html        Recommended references & tools
404.html                    Minimal fallback page
style.css                   Academic layout, handout typography & print styles
assets/club-logo.png        Club crest
handouts/
  P1.html, P1-solutions.html    Physical Reasoning & Estimation
  P2.html, P2-solutions.html    Motion, Forces & Conservation
  P3.html, P3-solutions.html    Gravity, Orbits & Waves
  A1.html, A1-solutions.html    The Night Sky & Celestial Motion
  A2.html, A2-solutions.html    Light, Telescopes & Stars
  A3.html, A3-solutions.html    Relativity & Black Holes
```

## Local preview

```bash
python3 -m http.server 8080 --bind 0.0.0.0
```

## Teaching curriculum and PDFs

`teaching/` contains the Cosmic Calculation Series curriculum, with 37 topic
blocks based on the IOAA syllabus, a reformatted syllabus PDF, and an FAQ PDF.
Original problem sets are available for the five Basic Astrophysics topics and
the two Coordinates and Times topics (01.01–02.02). Each has a linked, colored
contents page and four multi-part questions. Other Problems PDFs and all
Solutions PDFs are clearly labeled placeholders. Existing club sheets remain
in `handouts/` and are linked from Teaching.

The syllabus source is https://www.ioaa2026.vn/en/ioaa-syllabus (which credits
IOAA, updated 17 November 2021). Club codes and practical-topic labels are
organizational aids, not official IOAA designations.

To rebuild the Teaching page and PDFs, install `reportlab` in a Python virtual
environment and run `python scripts/build_teaching.py`. The generator uses
DejaVu Sans fonts from `/usr/share/fonts/truetype/dejavu/`. The authored
questions are maintained in `scripts/question_sets.py`.
