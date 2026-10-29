/* ============================================================
   arcade.js — "Star Catcher", a tiny canvas mini-game.
   Everything is drawn procedurally in a limited palette so it
   keeps the same look as the pixel-art mascot.
   ============================================================ */

let W = 900;
let H = 420;
const DURATION = 30;
const BEST_KEY = 'mais-pac-best';

const C = {
  night: '#05061a',
  night2: '#0b1030',
  grid: 'rgba(126,154,235,.10)',
  cyan: '#35c6ff',
  cyanSoft: '#8fe3ff',
  yellow: '#ffc21a',
  orange: '#ff6a1f',
  purple: '#a06bff',
  green: '#6ee06b',
  pink: '#ff4d97',
  white: '#ffffff',
  red: '#ff4d5e'
};

const rand = (min, max) => min + Math.random() * (max - min);
const clamp = (v, min, max) => Math.min(max, Math.max(min, v));

function readBest() {
  try {
    return Number(localStorage.getItem(BEST_KEY)) || 0;
  } catch {
    return 0;
  }
}

function writeBest(value) {
  try { localStorage.setItem(BEST_KEY, String(value)); } catch { /* ignore */ }
}

export function initArcade(refs) {
  const {
    canvas, overlay, kicker, title, note, startBtn, pauseBtn,
    scoreEl, bestEl, timeEl, livesEl, statusEl,
    playSfx = () => {}, onAchievement = () => {}
  } = refs;

  const ctx = canvas.getContext('2d');
  if (!ctx) return null;

  canvas.tabIndex = 0;
  canvas.setAttribute('role', 'application');
  canvas.setAttribute('aria-label', 'Star catcher. Use the left and right arrow keys to move the collector.');

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const state = {
    mode: 'idle',        // idle | playing | paused | over
    score: 0,
    best: readBest(),
    lives: 3,
    time: DURATION,
    elapsed: 0,
    player: { x: W / 2, targetX: W / 2, w: 92, h: 30 },
    items: [],
    particles: [],
    popups: [],
    stars: [],
    spawnTimer: 0,
    shake: 0,
    hitFlash: 0,
    invuln: 0,
    lastTime: 0,
    raf: 0,
    keys: new Set(),
    pointerActive: false,
    status: ''
  };

  const FONT = '"Space Grotesk", system-ui, sans-serif';

  /* background star field for the play area */
  function buildStars() {
    state.stars.length = 0;
    const count = Math.round((W * H) / 2900);
    for (let i = 0; i < count; i++) {
      state.stars.push({
        x: Math.random() * W,
        y: Math.random() * H,
        r: Math.random() < 0.82 ? 1 : 2,
        a: rand(0.15, 0.85),
        phase: Math.random() * Math.PI * 2,
        speed: rand(0.4, 2.2)
      });
    }
  }

  /* keep the play area usable on phones: portrait space, portrait field */
  function measure() {
    const cssWidth = canvas.clientWidth || 900;
    const portrait = cssWidth < 620;
    const nextW = portrait ? 520 : 900;
    const nextH = portrait ? 620 : 420;
    if (nextW === W && nextH === H && canvas.width === W) return false;
    W = nextW;
    H = nextH;
    canvas.width = W;
    canvas.height = H;
    canvas.style.aspectRatio = `${W} / ${H}`;
    state.player.x = Math.min(state.player.x, W - state.player.w / 2 - 8);
    state.player.targetX = Math.min(state.player.targetX, W - state.player.w / 2 - 8);
    state.items.length = 0;
    state.player.x = W / 2;
    state.player.targetX = W / 2;
    buildStars();
    return true;
  }

  measure();

  bestEl.textContent = String(state.best);

  /* ---------------- HUD ---------------- */
  let hudScore = null;
  let hudTime = null;
  let hudLives = null;

  function syncHud() {
    if (hudScore !== state.score) { scoreEl.textContent = String(state.score); hudScore = state.score; }
    const t = Math.max(0, Math.ceil(state.time));
    if (hudTime !== t) { timeEl.textContent = String(t); hudTime = t; }
    const lives = state.lives > 0 ? '♥'.repeat(state.lives) : '—';
    if (hudLives !== lives) { livesEl.textContent = lives; hudLives = lives; }
    bestEl.textContent = String(state.best);
  }

  function announce(message) {
    state.status = message;
    if (statusEl) statusEl.textContent = message;
  }

  /* ---------------- overlay ---------------- */
  function setOverlay(kind) {
    if (kind === 'hidden') {
      overlay.classList.add('is-hidden');
      pauseBtn.hidden = false;
      return;
    }
    overlay.classList.remove('is-hidden');
    overlay.classList.remove('is-hidden');
    startBtn.innerHTML = '<span aria-hidden="true">▶</span> Insert coin';
    startBtn.hidden = false;

    if (kind === 'idle') {
      kicker.textContent = 'Bonus level';
      title.textContent = 'Catch the starlight';
      note.textContent = 'Collect stars and planets. Avoid the void. 30 seconds on the clock.';
      pauseBtn.hidden = true;
    } else if (kind === 'paused') {
      kicker.textContent = 'Paused';
      title.textContent = 'Take a breath';
      note.textContent = 'The sky will wait. Press resume to jump back in.';
      startBtn.innerHTML = '<span aria-hidden="true">▶</span> Resume';
      pauseBtn.hidden = true;
    } else if (kind === 'over') {
      kicker.textContent = state.score >= state.best && state.score > 0 ? 'New high score' : 'Game over';
      title.textContent = state.score >= state.best && state.score > 0 ? 'Record broken!' : 'Run complete';
      note.textContent = `You caught ${state.score} points of starlight. Best: ${state.best}.`;
      startBtn.innerHTML = '<span aria-hidden="true">▶</span> Play again';
      pauseBtn.hidden = true;
    }
  }

  /* ---------------- game flow ---------------- */
  function reset() {
    state.score = 0;
    state.lives = 3;
    state.time = DURATION;
    state.elapsed = 0;
    state.items.length = 0;
    state.popups.length = 0;
    state.particles.length = 0;
    state.spawnTimer = 0.2;
    state.player.x = W / 2;
    state.player.targetX = W / 2;
    state.hitFlash = 0;
    state.invuln = 0;
    syncHud();
  }

  function start() {
    stopIdle();
    reset();
    state.mode = 'playing';
    setOverlay('hidden');
    canvas.focus({ preventScroll: true });
    playSfx('start');
    announce('Game started. You have 30 seconds.');
    state.lastTime = 0;
    cancelAnimationFrame(state.raf);
    state.raf = requestAnimationFrame(loop);
  }

  function pause() {
    if (state.mode !== 'playing') return;
    state.mode = 'paused';
    setOverlay('paused');
    cancelAnimationFrame(state.raf);
    announce('Game paused.');
  }

  function resume() {
    if (state.mode !== 'paused') return;
    state.mode = 'playing';
    setOverlay('hidden');
    state.lastTime = 0;
    canvas.focus({ preventScroll: true });
    announce('Game resumed.');
    state.raf = requestAnimationFrame(loop);
  }

  function gameOver() {
    state.mode = 'over';
    cancelAnimationFrame(state.raf);
    const isBest = state.score > state.best;
    if (isBest) {
      state.best = state.score;
      writeBest(state.best);
    }
    syncHud();
    setOverlay('over');
    playSfx(isBest ? 'big' : 'over');
    announce(`Game over. Score ${state.score}. Best ${state.best}.`);
    if (isBest && state.score > 0) onAchievement('highscore');
  }

  /* ---------------- spawning ---------------- */
  function spawn() {
    const progress = 1 - state.time / DURATION;
    const roll = Math.random();
    let type = 'star';
    if (roll > 0.86 - progress * 0.1) type = 'void';
    else if (roll > 0.7) type = 'planet';
    else if (roll > 0.62) type = 'comet';

    const margin = 44;
    const item = {
      type,
      x: rand(margin, W - margin),
      y: -40,
      vy: rand(105, 155) + progress * 90 + (type === 'comet' ? 60 : 0),
      vx: type === 'comet' ? rand(-40, 40) : 0,
      size: type === 'void' ? 30 : type === 'planet' ? 26 : 20,
      rot: rand(0, Math.PI * 2),
      spin: rand(-2, 2),
      wobble: Math.random() * Math.PI * 2
    };
    state.items.push(item);
  }

  /* ---------------- update ---------------- */
  function update(dt) {
    state.time -= dt;
    state.elapsed += dt;
    void 0;
    if (state.time <= 0) {
      state.time = 0;
      syncHud();
      gameOver();
      return;
    }

    const p = state.player;
    const speed = 620;
    if (state.keys.has('left')) p.targetX -= speed * dt;
    if (state.keys.has('right')) p.targetX += speed * dt;
    p.targetX = clamp(p.targetX, p.w / 2 + 8, W - p.w / 2 - 8);
    p.x += (p.targetX - p.x) * Math.min(1, dt * 14);

    state.spawnTimer -= dt;
    if (state.spawnTimer <= 0) {
      spawn();
      const progress = 1 - state.time / DURATION;
      state.spawnTimer = rand(0.42, 0.72) - progress * 0.18;
    }

    state.invuln = Math.max(0, state.invuln - dt);
    state.hitFlash = Math.max(0, state.hitFlash - dt * 2.4);
    state.shake = Math.max(0, state.shake - dt * 26);

    const catchY = H - 64;
    const catchHalf = p.w / 2 - 8;

    for (let i = state.items.length - 1; i >= 0; i--) {
      const item = state.items[i];
      item.y += item.vy * dt;
      item.x += item.vx * dt + Math.sin(state.elapsed * 2 + item.wobble) * 8 * dt;
      item.rot += item.spin * dt;

      const withinX = Math.abs(item.x - p.x) < catchHalf + item.size * 0.5;
      const withinY = item.y > catchY - 26 && item.y < H - 22;

      if (withinX && withinY) {
        state.items.splice(i, 1);
        if (item.type === 'void') {
          if (state.invuln <= 0) {
            state.lives -= 1;
            state.invuln = 1.1;
            state.hitFlash = 1;
            state.shake = reduceMotion ? 0 : 10;
            playSfx('hit');
            announce(`Ouch. ${state.lives} ${state.lives === 1 ? 'life' : 'lives'} left.`);
            state.popups.push({ x: item.x, y: H - 90, text: 'OUCH', color: C.red, life: 1 });
            if (state.lives <= 0) {
              syncHud();
              gameOver();
              return;
            }
          }
        } else {
          const base = item.type === 'planet' ? 25 : item.type === 'comet' ? 40 : 10;
          state.score += base;
          playSfx(item.type === 'star' ? 'coin' : 'star');
          state.popups.push({ x: item.x, y: H - 96, text: `+${base}`, color: item.type === 'planet' ? C.cyanSoft : C.yellow, life: 1 });
          for (let k = 0; k < 8; k++) {
            state.particles.push({
              x: item.x,
              y: H - 78,
              vx: rand(-90, 90),
              vy: rand(-150, -30),
              life: rand(0.35, 0.7),
              color: k % 3 === 0 ? C.white : k % 3 === 1 ? C.yellow : C.cyan
            });
          }
          syncHud();
        }
        continue;
      }

      if (item.y > H + 50) {
        state.items.splice(i, 1);
      }
    }

    for (let i = state.particles.length - 1; i >= 0; i--) {
      const part = state.particles[i];
      part.life -= dt;
      part.vy += 240 * dt;
      part.x += part.vx * dt;
      part.y += part.vy * dt;
      if (part.life <= 0) state.particles.splice(i, 1);
    }
    for (let i = state.popups.length - 1; i >= 0; i--) {
      const popup = state.popups[i];
      popup.life -= dt * 1.3;
      popup.y -= 26 * dt;
      if (popup.life <= 0) state.popups.splice(i, 1);
    }

    syncHud();
  }

  /* ---------------- drawing ---------------- */
  function drawBackground() {
    const g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, C.night2);
    g.addColorStop(0.55, C.night);
    g.addColorStop(1, '#070b24');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    // distant nebula
    const neb = ctx.createRadialGradient(W * 0.78, H * 0.18, 0, W * 0.78, H * 0.18, W * 0.55);
    neb.addColorStop(0, 'rgba(122,60,255,.20)');
    neb.addColorStop(0.5, 'rgba(53,198,255,.07)');
    neb.addColorStop(1, 'rgba(0,0,0,0)');
    ctx.fillStyle = neb;
    ctx.fillRect(0, 0, W, H);

    ctx.strokeStyle = C.grid;
    ctx.lineWidth = 1;
    ctx.beginPath();
    for (let x = 0; x <= W; x += 48) {
      ctx.moveTo(x + 0.5, 0);
      ctx.lineTo(x + 0.5, H);
    }
    for (let y = 0; y <= H; y += 48) {
      ctx.moveTo(0, y + 0.5);
      ctx.lineTo(W, y + 0.5);
    }
    ctx.stroke();

    for (const star of state.stars) {
      const tw = 0.6 + Math.sin(state.elapsed * star.speed + star.phase) * 0.4;
      ctx.globalAlpha = star.a * tw;
      ctx.fillStyle = star.r > 1 ? C.cyanSoft : C.white;
      ctx.fillRect(Math.round(star.x), Math.round((star.y + state.elapsed * star.speed * 6) % H), star.r, star.r);
    }
    ctx.globalAlpha = 1;
  }

  function drawStar(x, y, size, tint) {
    const s = size / 2;
    ctx.save();
    ctx.translate(Math.round(x), Math.round(y));
    ctx.fillStyle = tint;
    ctx.shadowColor = tint;
    ctx.shadowBlur = 16;
    // pixel diamond
    const step = Math.max(2, Math.round(size / 10));
    for (let i = 0; i < 5; i++) {
      const w = (5 - Math.abs(i - 2)) * step;
      ctx.fillRect(-w / 2, (i - 2) * step, w, step);
    }
    ctx.shadowBlur = 0;
    ctx.fillStyle = C.white;
    ctx.fillRect(-step / 2, -step / 2, step, step);
    ctx.restore();
    void s;
  }

  function drawPlanet(x, y, size) {
    const r = size / 2;
    ctx.save();
    ctx.translate(Math.round(x), Math.round(y));
    ctx.shadowColor = C.cyan;
    ctx.shadowBlur = 18;
    ctx.fillStyle = '#2f6bff';
    ctx.beginPath();
    ctx.arc(0, 0, r, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.fillStyle = '#79c8ff';
    ctx.beginPath();
    ctx.arc(-r * 0.25, -r * 0.28, r * 0.55, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = C.cyanSoft;
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.ellipse(0, 0, r * 1.5, r * 0.5, -0.35, 0, Math.PI * 2);
    ctx.stroke();
    ctx.restore();
  }

  function drawComet(x, y, size, rot) {
    ctx.save();
    ctx.translate(Math.round(x), Math.round(y));
    ctx.rotate(rot * 0.15);
    const grad = ctx.createLinearGradient(0, 0, 0, -size * 2.6);
    grad.addColorStop(0, 'rgba(255,194,26,.85)');
    grad.addColorStop(1, 'rgba(255,106,31,0)');
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.moveTo(-size * 0.35, 0);
    ctx.lineTo(size * 0.35, 0);
    ctx.lineTo(size * 0.9, -size * 2.6);
    ctx.lineTo(-size * 0.9, -size * 2.6);
    ctx.closePath();
    ctx.fill();
    ctx.fillStyle = C.yellow;
    ctx.shadowColor = C.yellow;
    ctx.shadowBlur = 20;
    ctx.fillRect(-size * 0.3, -size * 0.3, size * 0.6, size * 0.6);
    ctx.restore();
  }

  function drawVoid(x, y, size, rot) {
    ctx.save();
    ctx.translate(Math.round(x), Math.round(y));
    ctx.rotate(rot * 0.4);
    ctx.shadowColor = C.purple;
    ctx.shadowBlur = 26;
    ctx.fillStyle = '#ff4d97';
    ctx.beginPath();
    ctx.arc(0, 0, size * 0.62, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.fillStyle = '#2a0a2e';
    ctx.beginPath();
    ctx.arc(0, 0, size * 0.46, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#05030c';
    ctx.beginPath();
    ctx.arc(0, 0, size * 0.32, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = 'rgba(255,77,151,.65)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.ellipse(0, 0, size * 0.9, size * 0.32, 0.5, 0, Math.PI * 2);
    ctx.stroke();
    ctx.restore();
  }

  function drawCatcher() {
    const p = state.player;
    const x = Math.round(p.x);
    const y = H - 58;
    const w = p.w;
    const blink = state.invuln > 0 && Math.floor(state.invuln * 12) % 2 === 0;

    ctx.save();
    ctx.globalAlpha = blink ? 0.45 : 1;

    // beam
    const beam = ctx.createLinearGradient(0, y - 70, 0, y);
    beam.addColorStop(0, 'rgba(53,198,255,0)');
    beam.addColorStop(1, 'rgba(53,198,255,.22)');
    ctx.fillStyle = beam;
    ctx.beginPath();
    ctx.moveTo(x - w * 0.28, y);
    ctx.lineTo(x + w * 0.28, y);
    ctx.lineTo(x + w * 0.5, y - 74);
    ctx.lineTo(x - w * 0.5, y - 74);
    ctx.closePath();
    ctx.fill();

    // dish (pixel steps)
    ctx.shadowColor = C.cyan;
    ctx.shadowBlur = 22;
    ctx.fillStyle = C.cyan;
    ctx.fillRect(x - w * 0.5, y - 12, w, 8);
    ctx.fillRect(x - w * 0.42, y - 18, w * 0.84, 8);
    ctx.fillRect(x - w * 0.3, y - 24, w * 0.6, 8);
    ctx.shadowBlur = 0;

    ctx.fillStyle = C.cyanSoft;
    ctx.fillRect(x - w * 0.5, y - 12, w, 3);
    ctx.fillStyle = C.yellow;
    ctx.fillRect(x - w * 0.3, y - 24, w * 0.6, 3);

    // base
    ctx.fillStyle = '#1a2358';
    ctx.fillRect(x - w * 0.34, y + 2, w * 0.68, 10);
    ctx.fillStyle = '#2f3f96';
    ctx.fillRect(x - w * 0.34, y + 2, w * 0.68, 3);
    ctx.fillStyle = C.purple;
    ctx.fillRect(x - 5, y + 12, 10, 4);
    ctx.restore();
  }

  function draw() {
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, W, H);

    if (state.shake > 0) {
      const s = state.shake;
      ctx.translate(rand(-s, s), rand(-s, s));
    }

    drawBackground();

    for (const item of state.items) {
      if (item.type === 'star') drawStar(item.x, item.y, item.size, C.yellow);
      else if (item.type === 'planet') drawPlanet(item.x, item.y, item.size);
      else if (item.type === 'comet') drawComet(item.x, item.y, item.size, item.rot);
      else drawVoid(item.x, item.y, item.size, item.rot);
    }

    for (const part of state.particles) {
      ctx.globalAlpha = Math.max(0, part.life * 1.6);
      ctx.fillStyle = part.color;
      ctx.fillRect(Math.round(part.x), Math.round(part.y), 4, 4);
    }
    ctx.globalAlpha = 1;

    ctx.strokeStyle = 'rgba(143,227,255,.35)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, H - 18.5);
    ctx.lineTo(W, H - 18.5);
    ctx.stroke();

    drawCatcher();

    ctx.font = `700 20px ${FONT}`;
    ctx.textAlign = 'center';
    for (const popup of state.popups) {
      ctx.globalAlpha = Math.max(0, popup.life);
      ctx.fillStyle = popup.color;
      ctx.fillText(popup.text, popup.x, popup.y);
    }
    ctx.globalAlpha = 1;

    if (state.hitFlash > 0) {
      ctx.fillStyle = `rgba(255,77,94,${state.hitFlash * 0.28})`;
      ctx.fillRect(0, 0, W, H);
    }

    if (state.mode === 'playing' && state.time <= 5) {
      ctx.fillStyle = `rgba(255,77,94,${0.25 + Math.sin(state.elapsed * 10) * 0.12})`;
      ctx.fillRect(0, 0, W, 6);
    }
  }

  /* ---------------- loop ---------------- */
  function loop(now) {
    if (state.mode !== 'playing') return;
    const seconds = now / 1000;
    const raw = state.lastTime ? seconds - state.lastTime : 0.016;
    // never let a slow frame hide an item: run the sim in small fixed steps
    let remaining = Math.min(0.4, raw);
    state.lastTime = seconds;
    while (remaining > 0 && state.mode === 'playing') {
      const step = Math.min(0.05, remaining);
      update(step);
      remaining -= step;
    }
    draw();
    if (state.mode === 'playing') state.raf = requestAnimationFrame(loop);
  }

  /* ---------------- input ---------------- */
  function pointerX(event) {
    const rect = canvas.getBoundingClientRect();
    return ((event.clientX - rect.left) / rect.width) * W;
  }

  canvas.addEventListener('pointerdown', (event) => {
    if (state.mode !== 'playing') return;
    state.pointerActive = true;
    state.player.targetX = clamp(pointerX(event), 0, W);
    canvas.setPointerCapture?.(event.pointerId);
  });
  canvas.addEventListener('pointermove', (event) => {
    if (state.mode !== 'playing') return;
    if (event.pointerType === 'mouse' || state.pointerActive) {
      state.player.targetX = clamp(pointerX(event), 0, W);
    }
  });
  const releasePointer = () => { state.pointerActive = false; };
  canvas.addEventListener('pointerup', releasePointer);
  canvas.addEventListener('pointercancel', releasePointer);

  const keyMap = {
    ArrowLeft: 'left', KeyA: 'left',
    ArrowRight: 'right', KeyD: 'right'
  };

  window.addEventListener('keydown', (event) => {
    if (state.mode === 'paused' && (event.code === 'Space' || event.code === 'Enter')) {
      event.preventDefault();
      resume();
      return;
    }
    if (state.mode !== 'playing') return;
    const dir = keyMap[event.code];
    if (dir) {
      event.preventDefault();
      state.keys.add(dir);
    }
    if (event.code === 'KeyP' || event.code === 'Escape') {
      event.preventDefault();
      pause();
    }
  });

  window.addEventListener('keyup', (event) => {
    const dir = keyMap[event.code];
    if (dir) state.keys.delete(dir);
  });

  window.addEventListener('blur', () => {
    state.keys.clear();
    pause();
  });

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pause();
  });

  let resizeTimer = 0;
  window.addEventListener('resize', () => {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(() => {
      measure();
      if (state.mode === 'idle') draw();
      else draw();
    }, 180);
  });

  startBtn.addEventListener('click', () => {
    playSfx('click');
    if (state.mode === 'paused') resume();
    else start();
  });

  pauseBtn.addEventListener('click', () => {
    playSfx('click');
    if (state.mode === 'playing') pause();
  });

  /* ---------------- idle demo ---------------- */
  let idleRaf = 0;
  let idleLast = 0;
  const idleItems = [];

  function idleLoop(now) {
    if (state.mode !== 'idle') return;
    const seconds = now / 1000;
    const dt = idleLast ? Math.min(0.05, seconds - idleLast) : 0.016;
    idleLast = seconds;

    state.elapsed += dt;
    if (Math.random() < dt * 1.15 && idleItems.length < 9) {
      idleItems.push({
        type: Math.random() < 0.16 ? 'planet' : Math.random() < 0.3 ? 'comet' : 'star',
        x: rand(50, W - 50),
        y: -40,
        vy: rand(50, 95),
        vx: rand(-12, 12),
        size: 18,
        rot: rand(0, 6.28),
        spin: rand(-1, 1),
        wobble: rand(0, 6.28)
      });
    }
    for (let i = idleItems.length - 1; i >= 0; i--) {
      const item = idleItems[i];
      item.y += item.vy * dt;
      item.x += item.vx * dt;
      item.rot += item.spin * dt;
      if (item.y > H + 40) idleItems.splice(i, 1);
    }

    drawBackground();
    for (const item of idleItems) {
      if (item.type === 'planet') drawPlanet(item.x, item.y, item.size);
      else if (item.type === 'comet') drawComet(item.x, item.y, item.size, item.rot);
      else drawStar(item.x, item.y, item.size, C.yellow);
    }
    ctx.strokeStyle = 'rgba(143,227,255,.2)';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, H - 18.5);
    ctx.lineTo(W, H - 18.5);
    ctx.stroke();
    drawCatcher();
    idleRaf = requestAnimationFrame(idleLoop);
  }

  function startIdle() {
    if (state.mode !== 'idle' || reduceMotion) { draw(); return; }
    cancelAnimationFrame(idleRaf);
    idleLast = 0;
    idleRaf = requestAnimationFrame(idleLoop);
  }

  function stopIdle() {
    cancelAnimationFrame(idleRaf);
  }

  const idleIO = new IntersectionObserver((entries) => {
    if (entries[0]?.isIntersecting) startIdle();
    else stopIdle();
  }, { threshold: 0.08 });
  idleIO.observe(canvas);

  document.addEventListener('visibilitychange', () => {
    if (document.hidden) stopIdle();
    else startIdle();
  });

  state.player.x = W / 2;
  setOverlay('idle');
  startIdle();

  return {
    start,
    pause,
    resume,
    drawIdle() { state.mode = 'idle'; draw(); },
    get mode() { return state.mode; }
  };
}
