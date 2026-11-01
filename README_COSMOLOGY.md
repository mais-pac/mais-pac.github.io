# Cosmology handout — MAIS PAC

This is a merged, static-site build of the MAIS Physics & Astronomy Club website with a new **06.01 Elementary Cosmology** handout. It is a live-preview/review package, not a claim that the public GitHub Pages site has been changed.

## Deliverables

- `handouts/06.01.html` — self-contained Lecture + Problems page in the existing boxed handout theme.
- `handouts/06.01-solutions.html` — 30 worked solutions, including strategy and consistency checks for the original IOAA-inspired challenges.
- `handouts/pdf/06.01.pdf` — print edition of the lecture, problems and experiment snapshots.
- `handouts/pdf/06.01-solutions.pdf` — print edition of the solutions.
- `handouts/data/hubble-practice.csv` — explicitly synthetic Hubble-law teaching data.
- `teaching/index.html` — curriculum card and announcement linked to the new handout.

The new pages embed the existing `style.css`, KaTeX fonts, SVG figures and experiment JavaScript. They therefore work offline and in a network-sandboxed file viewer. The original site stylesheet is unchanged.

## Content

- 15 lecture sections, from the cosmological principle and Hubble flow through FLRW geometry, Friedmann dynamics, distances, the CMB, BBN, structure, inflation and horizons.
- 30 problems: 12 foundations, 8 website-sourced adaptations, and 10 original IOAA-inspired challenges.
- 5 interactive SVG experiments: expansion, expansion history, CMB cooling, cosmic distances, and Hubble-law fitting.
- 6 static vector figures.
- Source links and attribution are included in the handout. Adapted problems are not official IOAA questions; solutions are independent MAIS PAC explanations.

The Hubble catalogue is synthetic. Its generating value is 72 km/s/Mpc with fixed teaching perturbations. It must not be cited as an observational measurement. The rounded benchmark cosmology is H0 = 70, Omega_m = 0.3, Omega_Lambda = 0.7; radiation is omitted only where explicitly stated.

## Build and preview

Requirements: Node.js 20+ and Python 3.10+.

```sh
npm ci
python -m pip install -r requirements.txt
npx playwright install chromium
# On a minimal Linux host, browser system libraries may also be needed:
# npx playwright install-deps chromium

npm run build:cosmology
npm run integrate:cosmology
npm run pdf:cosmology
npm run preview
```

Open `http://localhost:3000/teaching/` locally, or use the platform's live preview. In the Arena sandbox the server binds to `0.0.0.0:3000`.

To rebuild the entire existing Teaching page and its older PDFs as well, run `python scripts/build_teaching.py` before the Cosmology build. The Cosmology routing is already implemented in that source generator, so a future rebuild will not replace the new links with placeholders.

## Tests

```sh
npm run test:cosmology
# Or against a running server:
BASE_URL=http://127.0.0.1:3000/handouts/ npm run test:cosmology
```

The checks cover problem/solution counts, numerical benchmarks, all five labs, presets and resets, CSV export, internal links, offline operation, mobile overflow, source attribution, and PDF presence. PDF pagination and text bounds were also checked with PyMuPDF. `npm audit` reports no known vulnerabilities for the pinned build dependencies.

## Publishing after review

This package is ready for a static host. To update the public site, commit the changed/generated files to the website repository and deploy through its existing GitHub Pages workflow. No repository credentials were used and no public push was performed in this session. Review the source attributions and the club's preferred wording before public publication.
