/* ============================================================
   app.js — UI wiring for the MAIS PAC "Cosmic Quest" site.
   ============================================================ */

import { loadPreference, isEnabled, setEnabled, play } from './sfx.js';

const root = document.documentElement;
root.classList.add('js');

const $ = (selector, scope = document) => scope.querySelector(selector);
const $$ = (selector, scope = document) => Array.from(scope.querySelectorAll(selector));
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ------------------------------------------------------------
   Boot screen
   ------------------------------------------------------------ */
(function boot() {
  const el = $('#boot');
  const bar = $('#boot-bar');
  if (!el || !bar) return;

  let progress = 6;
  let done = false;

  const tick = window.setInterval(() => {
    progress = Math.min(progress + 6 + Math.random() * 12, 92);
    bar.style.width = `${progress}%`;
  }, 95);

  function finish() {
    if (done) return;
    done = true;
    window.clearInterval(tick);
    bar.style.width = '100%';
    window.setTimeout(() => {
      el.classList.add('is-done');
      window.setTimeout(() => el.remove(), 600);
    }, reduceMotion ? 40 : 260);
  }

  window.addEventListener('load', finish, { once: true });
  window.setTimeout(finish, 2600);
  ['keydown', 'pointerdown', 'touchstart'].forEach((type) => {
    window.addEventListener(type, finish, { once: true, passive: true });
  });
})();

/* ------------------------------------------------------------
   Sound
   ------------------------------------------------------------ */
(function sound() {
  const button = $('#sound-toggle');
  const label = $('#sound-label');
  if (!button) return;

  let on = loadPreference();

  function render() {
    button.setAttribute('aria-pressed', String(on));
    button.classList.toggle('is-on', on);
    button.setAttribute('aria-label', on ? 'Turn sound effects off' : 'Turn sound effects on');
    if (label) label.textContent = on ? 'SFX ON' : 'SFX OFF';
  }

  button.addEventListener('click', () => {
    on = setEnabled(!isEnabled());
    render();
    if (on) play('toggle');
  });

  render();
})();

/* ------------------------------------------------------------
   HUD: scroll progress, active link, mobile menu
   ------------------------------------------------------------ */
(function hud() {
  const bar = $('#scroll-progress');
  const navLinks = $$('.hud__nav a');
  const burger = $('#nav-toggle');
  const mobileNav = $('#mobile-nav');

  let queued = false;
  function onScroll() {
    if (queued) return;
    queued = true;
    window.requestAnimationFrame(() => {
      queued = false;
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const ratio = max > 0 ? Math.min(1, window.scrollY / max) : 0;
      if (bar) bar.style.width = `${(ratio * 100).toFixed(2)}%`;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const sections = $$('main section[id]');
  if ('IntersectionObserver' in window && sections.length) {
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const id = entry.target.id;
        navLinks.forEach((link) => {
          const matches = link.getAttribute('href') === `#${id}`;
          link.classList.toggle('is-active', matches);
          if (matches) link.setAttribute('aria-current', 'true');
          else link.removeAttribute('aria-current');
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    sections.forEach((section) => spy.observe(section));
  }

  function closeMenu() {
    if (!mobileNav || !burger) return;
    mobileNav.hidden = true;
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-label', 'Open menu');
  }

  function openMenu() {
    if (!mobileNav || !burger) return;
    mobileNav.hidden = false;
    burger.setAttribute('aria-expanded', 'true');
    burger.setAttribute('aria-label', 'Close menu');
  }

  if (burger && mobileNav) {
    burger.addEventListener('click', () => {
      play('click');
      if (mobileNav.hidden) openMenu();
      else closeMenu();
    });
    mobileNav.addEventListener('click', (event) => {
      if (event.target.closest('a')) closeMenu();
    });
    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') closeMenu();
    });
    window.addEventListener('resize', () => {
      if (window.innerWidth > 1040) closeMenu();
    });
  }
})();

/* ------------------------------------------------------------
   Scroll reveal
   ------------------------------------------------------------ */
(function reveal() {
  const items = $$('.reveal');
  if (!items.length) return;

  if (!('IntersectionObserver' in window) || reduceMotion) {
    items.forEach((item) => item.classList.add('is-in'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-in');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });

  items.forEach((item, index) => {
    const siblings = item.parentElement ? Array.from(item.parentElement.children).indexOf(item) : 0;
    item.style.setProperty('--delay', `${Math.min(index, 8) * 45 + (siblings % 4) * 70}ms`);
    observer.observe(item);
  });

  // never leave content invisible if something goes wrong
  window.setTimeout(() => {
    items.forEach((item) => item.classList.add('is-in'));
  }, 4000);
})();

/* ------------------------------------------------------------
   Background star field (fixed canvas)
   ------------------------------------------------------------ */
(function starfield() {
  const canvas = $('#starfield');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  let width = 0;
  let height = 0;
  let stars = [];
  let scrollY = window.scrollY || 0;
  let raf = 0;
  let last = 0;
  let running = false;
  let shooting = null;

  function build() {
    const count = Math.max(70, Math.min(280, Math.round((width * height) / 8200)));
    stars = Array.from({ length: count }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      r: Math.random() < 0.86 ? 1 : 2,
      alpha: 0.18 + Math.random() * 0.7,
      phase: Math.random() * Math.PI * 2,
      speed: 0.25 + Math.random() * 1.3,
      depth: 0.2 + Math.random() * 0.8,
      tint: Math.random() < 0.12 ? '255,214,150' : Math.random() < 0.35 ? '150,205,255' : '255,255,255'
    }));
  }

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 1.6);
    width = canvas.clientWidth || window.innerWidth;
    height = canvas.clientHeight || window.innerHeight;
    canvas.width = Math.round(width * dpr);
    canvas.height = Math.round(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    build();
    if (reduceMotion) draw(0);
  }

  function draw(time) {
    ctx.clearRect(0, 0, width, height);
    const drift = scrollY * 0.12;

    for (const star of stars) {
      const y = ((star.y - drift * star.depth) % (height + 20) + height + 20) % (height + 20) - 10;
      const twinkle = reduceMotion ? 1 : 0.65 + Math.sin(time * 0.001 * star.speed + star.phase) * 0.35;
      ctx.fillStyle = `rgba(${star.tint},${(star.alpha * twinkle).toFixed(3)})`;
      ctx.fillRect(Math.round(star.x), Math.round(y), star.r, star.r);

      if (star.r > 1) {
        ctx.fillStyle = `rgba(${star.tint},${(star.alpha * twinkle * 0.14).toFixed(3)})`;
        ctx.fillRect(Math.round(star.x) - 3, Math.round(y) + 0, 7, 1);
        ctx.fillRect(Math.round(star.x), Math.round(y) - 3, 1, 7);
      }
    }

    if (shooting) {
      shooting.life -= 0.016;
      shooting.x += shooting.vx;
      shooting.y += shooting.vy;
      const grad = ctx.createLinearGradient(shooting.x, shooting.y, shooting.x - shooting.vx * 12, shooting.y - shooting.vy * 12);
      grad.addColorStop(0, `rgba(200,235,255,${Math.max(0, shooting.life)})`);
      grad.addColorStop(1, 'rgba(200,235,255,0)');
      ctx.strokeStyle = grad;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(shooting.x, shooting.y);
      ctx.lineTo(shooting.x - shooting.vx * 12, shooting.y - shooting.vy * 12);
      ctx.stroke();
      if (shooting.life <= 0 || shooting.x > width + 200 || shooting.y > height + 200) shooting = null;
    } else if (!reduceMotion && Math.random() < 0.0022) {
      shooting = {
        x: Math.random() * width * 0.7,
        y: Math.random() * height * 0.4,
        vx: 7 + Math.random() * 4,
        vy: 3.5 + Math.random() * 2,
        life: 1
      };
    }
  }

  function loop(time) {
    if (!running) return;
    const fine = time - last > 26; // ~38fps is plenty for a background
    if (fine) {
      last = time;
      draw(time);
    }
    raf = window.requestAnimationFrame(loop);
  }

  function start() {
    if (running || reduceMotion) return;
    running = true;
    last = 0;
    raf = window.requestAnimationFrame(loop);
  }

  function stop() {
    running = false;
    window.cancelAnimationFrame(raf);
  }

  window.addEventListener('scroll', () => { scrollY = window.scrollY || 0; }, { passive: true });
  window.addEventListener('resize', resize);
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stop();
    else start();
  });

  resize();
  draw(0);
  start();
})();

/* ------------------------------------------------------------
   Mascot
   ------------------------------------------------------------ */
(function mascot() {
  const el = $('#mascot');
  if (!el) return;
  let jumps = 0;

  function burst() {
    const layer = document.createElement('div');
    layer.className = 'mascot__burst';
    for (let i = 0; i < 10; i++) {
      const spark = document.createElement('span');
      const angle = (Math.PI * 2 * i) / 10 + Math.random() * 0.4;
      const distance = 60 + Math.random() * 70;
      spark.style.setProperty('--dx', `${Math.cos(angle) * distance}px`);
      spark.style.setProperty('--dy', `${Math.sin(angle) * distance}px`);
      spark.style.background = i % 3 === 0 ? '#35c6ff' : i % 3 === 1 ? '#ffc21a' : '#ffffff';
      spark.style.animationDelay = `${Math.random() * 60}ms`;
      layer.append(spark);
    }
    el.append(layer);
    window.setTimeout(() => layer.remove(), 900);
  }

  function jump() {
    el.classList.remove('is-jump');
    void el.offsetWidth;
    el.classList.add('is-jump');
    burst();
    play('jump');
    jumps += 1;
    if (jumps === 5) achievement('mascot');
  }

  el.addEventListener('click', jump);
  el.addEventListener('keydown', (event) => {
    if (event.key === 'Enter' || event.key === ' ') {
      event.preventDefault();
      jump();
    }
  });
})();

/* ------------------------------------------------------------
   Achievements / toasts
   ------------------------------------------------------------ */
const unlocked = new Set();

const ACHIEVEMENTS = {
  first: { kicker: 'Achievement unlocked', text: 'First quest opened' },
  allquests: { kicker: 'Achievement unlocked', text: 'All eight worlds unlocked' },
  stargazer: { kicker: 'Achievement unlocked', text: 'Star gazer — 8 stars logged' },
  mascot: { kicker: 'Achievement unlocked', text: 'PIX says hello' },
  highscore: { kicker: 'New record', text: 'Personal best in Star Catcher' }
};

function achievement(id) {
  if (!ACHIEVEMENTS[id] || unlocked.has(id)) return;
  unlocked.add(id);
  const holder = $('#toasts');
  if (!holder) return;

  const toast = document.createElement('div');
  toast.className = 'toast';
  toast.innerHTML = '<img class="toast__icon" src="assets/img/star.png" alt="" width="24" height="24"><div><p class="toast__kicker"></p><p class="toast__text"></p></div>';
  toast.querySelector('.toast__kicker').textContent = ACHIEVEMENTS[id].kicker;
  toast.querySelector('.toast__text').textContent = ACHIEVEMENTS[id].text;
  holder.append(toast);
  play('big');

  window.setTimeout(() => {
    toast.classList.add('is-out');
    window.setTimeout(() => toast.remove(), 400);
  }, 4600);
}

/* ------------------------------------------------------------
   Quest dialog
   ------------------------------------------------------------ */
const QUESTS = {
  physics: {
    name: 'Physics',
    level: 'LV.01',
    icon: 'assets/img/topics/physics.png',
    blurb: 'Physics asks how the world works and then tries to write the answer as something you can test. We start with motion, forces, energy and light, and connect the maths to things you can actually see.',
    questions: [
      'Why does a spinning top stay upright?',
      'What is light, really — a wave, a particle, or both?',
      'How do we measure something we cannot see?'
    ],
    quest: 'Drop two objects from the same height and time them. Do they land together? Work out why your answer is what it is.'
  },
  astronomy: {
    name: 'Astronomy',
    level: 'LV.02',
    icon: 'assets/img/topics/astronomy.png',
    blurb: 'Astronomy is the oldest science that anyone can start tonight. We learn how to find planets, read the Moon, and understand what stars are telling us with their light.',
    questions: [
      'How would you find Saturn tonight without an app?',
      'Why do stars twinkle but planets usually do not?',
      'What can you actually see from Ulaanbaatar’s sky?'
    ],
    quest: 'Sketch the Moon’s phase at the same time for seven nights. What pattern appears, and why?'
  },
  astrophysics: {
    name: 'Astrophysics',
    level: 'LV.03',
    icon: 'assets/img/topics/astrophysics.png',
    blurb: 'Astrophysics points the laws of physics at the most extreme places we know: black holes, neutron stars, and gas falling so fast it glows. It is where gravity and light get interesting.',
    questions: [
      'What happens to time near a black hole?',
      'How do we know what a star is made of without visiting it?',
      'Why can a neutron star spin hundreds of times a second?'
    ],
    quest: 'Build a scale model where the Sun is a 1 cm marble. Where would Earth be? Where would the nearest star be?'
  },
  cosmology: {
    name: 'Cosmology',
    level: 'LV.04',
    icon: 'assets/img/topics/cosmology.png',
    blurb: 'Cosmology treats the entire universe as a single object with a history. We look at expansion, the cosmic microwave background, and the strange ingredients — dark matter and dark energy — that most of it seems to be made of.',
    questions: [
      'What does “the universe is expanding” actually mean?',
      'Can we ask what came before the Big Bang?',
      'What is dark matter, and why do we think it is there?'
    ],
    quest: 'Make a timeline of the universe where 1 cm equals 100 million years. How long is human history on that scale?'
  },
  math: {
    name: 'Mathematics',
    level: 'LV.05',
    icon: 'assets/img/topics/math.png',
    blurb: 'Maths is the language physics borrows. Vectors, calculus and geometry are not obstacles before the interesting part — they are the tools that make the interesting part possible.',
    questions: [
      'Why does calculus describe change so well?',
      'What is a vector, and why does physics love them?',
      'How can one equation predict where a planet will be?'
    ],
    quest: 'Measure the height of a building using only its shadow, a ruler and the Sun. Compare with a friend’s method.'
  },
  ml: {
    name: 'Machine Learning',
    level: 'LV.06',
    icon: 'assets/img/topics/ml.png',
    blurb: 'Machine learning is pattern-finding at scale. Modern sky surveys produce more images than any team could check by hand, so we teach computers to help — and then we check their work.',
    questions: [
      'How does a computer learn from examples?',
      'Could a model learn to recognise a galaxy?',
      'What is overfitting, and why is it dangerous?'
    ],
    quest: 'Sort ten objects into two groups using a rule you write down before you look. Then test the rule on a friend’s objects.'
  },
  ai: {
    name: 'Artificial Intelligence',
    level: 'LV.07',
    icon: 'assets/img/topics/ai.png',
    blurb: 'AI is both an engineering project and a set of questions: what do we want these systems to do, how do we check them, and who is accountable when they are wrong? Science needs clear answers.',
    questions: [
      'Where is the line between machine learning and AI?',
      'What can AI do well, and what does it miss?',
      'How should we use AI honestly in schoolwork and research?'
    ],
    quest: 'Ask an AI tool a physics question, then verify the answer with a textbook or a teacher. Note what it got wrong.'
  },
  cs: {
    name: 'Computer Science',
    level: 'LV.08',
    icon: 'assets/img/topics/cs.png',
    blurb: 'Computer science turns ideas into simulations. Want to see two galaxies collide, or watch a wave function evolve? Write it, run it, and compare it with the universe.',
    questions: [
      'What makes one algorithm faster than another?',
      'How do simulations show us things we cannot photograph?',
      'What is a data structure, really?'
    ],
    quest: 'Write a short program that prints the first 20 Fibonacci numbers. Then change it so it prints every third one.'
  }
};

const questOrder = Object.keys(QUESTS);
const openedQuests = new Set();

(function quests() {
  const dialog = $('#quest-dialog');
  if (!dialog) return;

  const els = {
    icon: $('#dialog-icon'),
    level: $('#dialog-level'),
    title: $('#dialog-title'),
    blurb: $('#dialog-blurb'),
    questions: $('#dialog-questions'),
    quest: $('#dialog-quest'),
    close: $('#dialog-close'),
    ok: $('#dialog-ok')
  };

  let currentId = null;

  function fill(id) {
    const quest = QUESTS[id];
    if (!quest) return;
    currentId = id;
    els.icon.src = quest.icon;
    els.level.textContent = quest.level;
    els.title.textContent = quest.name;
    els.blurb.textContent = quest.blurb;
    els.questions.replaceChildren(...quest.questions.map((text) => {
      const li = document.createElement('li');
      li.textContent = text;
      return li;
    }));
    els.quest.textContent = quest.quest;
  }

  function open(id) {
    fill(id);
    if (!dialog.open) {
      dialog.showModal();
      document.body.classList.add('is-locked');
    }
    play('open');
    openedQuests.add(id);
    if (openedQuests.size === 1) achievement('first');
    if (openedQuests.size === questOrder.length) achievement('allquests');
  }

  $$('.level').forEach((button) => {
    button.addEventListener('click', () => open(button.dataset.quest));
  });

  els.close.addEventListener('click', () => {
    play('close');
    dialog.close();
  });

  els.ok.addEventListener('click', () => {
    play('open');
    const index = questOrder.indexOf(currentId);
    const next = questOrder[(index + 1) % questOrder.length];
    fill(next);
    openedQuests.add(next);
    if (openedQuests.size === questOrder.length) achievement('allquests');
  });

  dialog.addEventListener('close', () => {
    document.body.classList.remove('is-locked');
    play('close');
  });

  dialog.addEventListener('click', (event) => {
    // clicking the backdrop (the dialog element itself) closes it
    if (event.target === dialog) dialog.close();
  });
})();

/* ------------------------------------------------------------
   Sky lab
   ------------------------------------------------------------ */
const STARS = {
  sirius: {
    name: 'Sirius',
    type: 'Main sequence + white dwarf',
    distance: '≈ 8.6 light-years',
    text: 'The brightest star in the night sky. It is a binary: a hot white star orbited by a faint white dwarf — the collapsed core of a star that has already died.'
  },
  betelgeuse: {
    name: 'Betelgeuse',
    type: 'Red supergiant',
    distance: '≈ 640 light-years',
    text: 'The shoulder of Orion. So large that it would swallow the orbit of Mars, and it dims and brightens unpredictably. One day it will collapse — possibly within the next hundred thousand years.'
  },
  rigel: {
    name: 'Rigel',
    type: 'Blue supergiant',
    distance: '≈ 860 light-years',
    text: 'The bright blue foot of Orion. It is roughly 20 times the mass of the Sun and burns thousands of times brighter — energy that comes at the cost of a short life.'
  },
  vega: {
    name: 'Vega',
    type: 'Main sequence (A0)',
    distance: '≈ 25 light-years',
    text: 'Once the zero point of the brightness scale. Vega spins so quickly that its equator bulges — a star visibly flattened by its own rotation.'
  },
  polaris: {
    name: 'Polaris',
    type: 'Cepheid variable',
    distance: '≈ 430 light-years',
    text: 'The North Star: almost directly above Earth’s north pole, so the whole sky wheels around it. It is a pulsating Cepheid — a cosmic distance marker.'
  },
  aldebaran: {
    name: 'Aldebaran',
    type: 'Red giant',
    distance: '≈ 65 light-years',
    text: 'The eye of Taurus, the bull. Its name means “the follower”, because it appears to follow the Pleiades across the sky. It is a swollen red giant, already past its prime.'
  },
  antares: {
    name: 'Antares',
    type: 'Red supergiant',
    distance: '≈ 550 light-years',
    text: 'The heart of Scorpius. Its name means “rival of Mars” — a comment on its orange-red colour. Like Betelgeuse, it is a supergiant close to the end of its life.'
  },
  alphacen: {
    name: 'Alpha Centauri',
    type: 'Triple star system',
    distance: '≈ 4.3 light-years',
    text: 'The closest star system to our own. Two Sun-like stars orbit each other, and a third — Proxima Centauri — is the nearest single star, with at least one known planet.'
  }
};

(function skylab() {
  const chart = $('#chart');
  const canvas = $('#chart-canvas');
  if (!chart || !canvas) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;

  const buttons = $$('.star-dot', chart);
  const readout = {
    name: $('#readout-name'),
    meta: $('#readout-meta'),
    text: $('#readout-text'),
    type: $('#readout-type'),
    dist: $('#readout-dist'),
    count: $('#readout-count')
  };

  const defaults = {
    name: 'Nothing selected',
    meta: 'Pick a star on the chart, or press Tab to move between them.',
    text: 'Every point of light in the night sky is a real object — some are close neighbours, some are dying giants hundreds of light-years away.',
    type: '—',
    dist: '—'
  };

  const logged = new Set();
  let pinned = null;

  function render(data) {
    readout.name.textContent = data.name;
    readout.meta.textContent = data.meta;
    readout.text.textContent = data.text;
    readout.type.textContent = data.type;
    readout.dist.textContent = data.dist;
  }

  function show(id, pin) {
    const data = STARS[id];
    if (!data) return;
    render({
      name: data.name,
      meta: pin ? 'File pinned · tap another star to compare' : 'Previewing star file',
      text: data.text,
      type: data.type,
      dist: data.distance
    });
    buttons.forEach((button) => button.classList.toggle('is-active', button.dataset.star === id));
  }

  function reset() {
    if (pinned) {
      show(pinned, true);
      return;
    }
    render(defaults);
    buttons.forEach((button) => button.classList.remove('is-active'));
  }

  buttons.forEach((button) => {
    const id = button.dataset.star;
    button.addEventListener('click', () => {
      pinned = id;
      logged.add(id);
      button.classList.add('is-logged');
      readout.count.textContent = String(logged.size);
      show(id, true);
      play('click');
      if (logged.size === Object.keys(STARS).length) achievement('stargazer');
    });
    button.addEventListener('mouseenter', () => { if (!pinned) show(id, false); });
    button.addEventListener('focus', () => show(id, false));
    button.addEventListener('mouseleave', () => { if (!pinned) reset(); });
    button.addEventListener('blur', () => { if (!pinned) reset(); });
  });

  /* twinkling chart background */
  let width = 0;
  let height = 0;
  let dots = [];
  let raf = 0;
  let running = false;
  let time = 0;

  function build() {
    const count = Math.max(40, Math.round((width * height) / 3600));
    dots = Array.from({ length: count }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      r: Math.random() < 0.88 ? 1 : 2,
      a: 0.15 + Math.random() * 0.7,
      phase: Math.random() * Math.PI * 2,
      speed: 0.4 + Math.random() * 1.4
    }));
  }

  function resize() {
    const dpr = Math.min(window.devicePixelRatio || 1, 1.6);
    width = canvas.clientWidth;
    height = canvas.clientHeight;
    canvas.width = Math.max(1, Math.round(width * dpr));
    canvas.height = Math.max(1, Math.round(height * dpr));
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    build();
    draw(0);
  }

  function draw(t) {
    ctx.clearRect(0, 0, width, height);

    // milky way wash
    const band = ctx.createLinearGradient(0, height * 0.1, width, height * 0.9);
    band.addColorStop(0, 'rgba(122,60,255,0)');
    band.addColorStop(0.45, 'rgba(122,60,255,.10)');
    band.addColorStop(0.6, 'rgba(53,198,255,.10)');
    band.addColorStop(1, 'rgba(53,198,255,0)');
    ctx.fillStyle = band;
    ctx.fillRect(0, 0, width, height);

    for (const dot of dots) {
      const tw = reduceMotion ? 1 : 0.55 + Math.sin(t * 0.001 * dot.speed + dot.phase) * 0.45;
      ctx.fillStyle = `rgba(255,255,255,${(dot.a * tw).toFixed(3)})`;
      ctx.fillRect(Math.round(dot.x), Math.round(dot.y), dot.r, dot.r);
    }
  }

  function loop(t) {
    if (!running) return;
    time = t;
    draw(t);
    raf = window.requestAnimationFrame(loop);
  }

  function start() {
    if (running || reduceMotion) return;
    running = true;
    raf = window.requestAnimationFrame(loop);
  }
  function stop() {
    running = false;
    window.cancelAnimationFrame(raf);
  }

  const io = new IntersectionObserver((entries) => {
    if (entries[0]?.isIntersecting) start();
    else stop();
  }, { threshold: 0.05 });
  io.observe(chart);

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stop();
  });

  window.addEventListener('resize', resize);
  resize();
  void time;
})();

/* ------------------------------------------------------------
   Arcade (loaded on demand)
   ------------------------------------------------------------ */
(function arcade() {
  const canvas = $('#game');
  if (!canvas) return;

  const refs = {
    canvas,
    overlay: $('#game-overlay'),
    kicker: $('#game-kicker'),
    title: $('#game-title'),
    note: $('#game-note'),
    startBtn: $('#game-start'),
    pauseBtn: $('#game-pause'),
    scoreEl: $('#score'),
    bestEl: $('#best'),
    timeEl: $('#time'),
    livesEl: $('#lives'),
    statusEl: $('#game-status'),
    playSfx: play,
    onAchievement: achievement
  };

  let loaded = false;
  function load() {
    if (loaded) return;
    loaded = true;
    import('./arcade.js')
      .then((mod) => mod.initArcade(refs))
      .catch(() => {
        const note = $('#game-note');
        if (note) note.textContent = 'The arcade needs JavaScript to run. Everything else on this page still works.';
      });
  }

  if (!('IntersectionObserver' in window)) {
    load();
    return;
  }
  const io = new IntersectionObserver((entries) => {
    if (entries[0]?.isIntersecting) {
      io.disconnect();
      load();
    }
  }, { rootMargin: '400px 0px' });
  io.observe(canvas);
})();

/* ------------------------------------------------------------
   Hero 3D (loaded after first paint)
   ------------------------------------------------------------ */
(function hero3d() {
  const canvas = $('#hero-canvas');
  if (!canvas) return;

  const start = () => {
    import('./hero-3d.js')
      .then((mod) => {
        if (!mod.supportsWebGL()) return;
        mod.init(canvas);
      })
      .catch(() => {
        // No 3D? The CSS sky and mascot still carry the hero.
      });
  };

  if ('requestIdleCallback' in window) {
    window.requestIdleCallback(start, { timeout: 1800 });
  } else {
    window.setTimeout(start, 500);
  }
})();

/* ------------------------------------------------------------
   Small stuff
   ------------------------------------------------------------ */
const year = $('#year');
if (year) year.textContent = String(new Date().getFullYear());
