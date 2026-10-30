# mais-pac.github.io

The Physics & Astronomy Club (PAC) at Mongol Aspiration International School in Ulaanbaatar, Mongolia. Its aim is to give students a starting point in astronomy and physics, and a place where questions can be asked until they become understanding.

Live site: <https://mais-pac.github.io/>

## Structure

A simple, static academic website with self-contained physics and astronomy club handouts — no build step, no JavaScript dependencies, no trackers, and no cookies.

```
index.html                  Club homepage & handout index
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
