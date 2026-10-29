# mais-pac.github.io

The Physics & Astronomy Club (PAC) at Mongol Aspiration International School.
Its aim is to give students a starting point in astronomy, and a place where
questions can be asked until they become understanding.

Live site: <https://mais-pac.github.io/>

## What's here

A single, static, video-game-styled homepage — no build step, no trackers, no
cookies, and no third-party requests at runtime. GitHub Pages serves the
repository root directly.

```
index.html          the homepage
404.html            "lost in space" fallback page
og-card.html        source for the social preview image (not part of the site)
css/
  global.css        fonts, design tokens, background, utilities
  components.css    buttons, HUD, dialogs, toasts, boot screen
  sections.css      hero, levels, club, sky lab, arcade, resources, footer
js/
  app.js            UI wiring: quests, sky lab, reveals, sound toggle
  hero-3d.js        interactive three.js black hole scene
  arcade.js         "Star Catcher" mini-game
  sfx.js            tiny WebAudio chiptune synth (no audio files)
assets/
  fonts/            self-hosted woff2 fonts
  img/              pixel-art mascot, icons and props (generated from the artwork)
  vendor/           three.js (vendored locally)
  club-logo.png     club crest
```

## Features

- **Pixel mascot hero** with an interactive 3D black hole, accretion disk and
  star field you can drag to rotate.
- **Eight "levels"** — physics, astronomy, astrophysics, cosmology, maths,
  machine learning, AI and computer science — each opening a quest file with
  starter questions and a side quest.
- **Sky lab** — a stylised star chart with eight real star files.
- **Star Catcher arcade** — a small, complete canvas game with arrow keys,
  touch support, pause, lives and a saved high score.
- **Optional chiptune sound effects**, off by default, synthesised in the
  browser with WebAudio.
- Keyboard accessible throughout, respects `prefers-reduced-motion`, and works
  without JavaScript (all written content stays readable).

## Local preview

```bash
python3 -m http.server 8080
# then open http://localhost:8080/
```

ES modules need to be served over HTTP; opening `index.html` from the file
system will not load the JavaScript.

## Credits

Mascot artwork, club crest and club story: MAIS Physics & Astronomy Club.
Site built with plain HTML, CSS and JavaScript.
