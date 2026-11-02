/* Original MAIS PAC IPhO experiments. SVG only; no network requests. */
(() => {
'use strict';
const $ = id => document.getElementById(id), PI = Math.PI, D2R = PI / 180, R2D = 180 / PI;
const value = id => Number($(id).value);
const fmt = (x, n = 2) => Number.isFinite(x) ? x.toFixed(n) : '—';
const sci = (x, n = 2) => Number.isFinite(x) ? x.toExponential(n) : '—';
const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
const out = (key, k, v) => { const e = $(`out-${key}-${k}`); if (e) e.textContent = v; };
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const text = (x, y, s, extra = '') => `<text x="${x}" y="${y}" fill="#526079" font-size="12" ${extra}>${esc(s)}</text>`;
const line = (x1, y1, x2, y2, col = '#cbd5e1', extra = '') => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${col}" ${extra}/>`;
const path = (pts, col = '#2457c5', extra = '') => `<polyline points="${pts.filter(p => p.every(Number.isFinite)).map(p => p.map(v => v.toFixed(2)).join(',')).join(' ')}" fill="none" stroke="${col}" stroke-width="2.6" ${extra}/>`;
const dot = (x, y, r = 5, col = '#7c3aed') => `<circle cx="${x}" cy="${y}" r="${r}" fill="${col}"/>`;
function draw(key, body) { const e = $('plot-' + key); if (e) e.innerHTML = '<title>' + esc(key) + ' interactive plot</title>' + body; }
function summary(key, s) { const e = $('summary-' + key); if (e) e.textContent = s; }
function axes(xlab, ylab) {
  return line(60, 275, 645, 275) + line(60, 275, 60, 25) + text(350, 315, xlab, 'text-anchor="middle"') + text(18, 20, ylab);
}
function bind(key, update) {
  const section = $('lab-' + key); if (!section) return;
  const controls = [...section.querySelectorAll('input,select')];
  const defaults = controls.map(el => ({ el, value: el.value, checked: el.checked }));
  controls.forEach(el => el.addEventListener('input', () => { const r = $('range-' + el.id); if (r) r.textContent = el.value; update(); }));
  const reset = section.querySelector('[data-reset]');
  if (reset) reset.addEventListener('click', () => {
    defaults.forEach(d => { d.el.value = d.value; if (d.el.type === 'checkbox') d.el.checked = d.checked; const r = $('range-' + d.el.id); if (r) r.textContent = d.el.value; });
    update();
  });
  update();
}
function seeded(seed) { let s = seed >>> 0; return () => { s = (1664525 * s + 1013904223) >>> 0; return s / 4294967296; }; }

const init = {}, EXPORTS = {};

/* === TOPIC FRAGMENTS === */

/* ---- 01.01 ---- */
/* 01.01 — dimensional analysis searchlight */
const DIMS = {
  pend: { M: 0, L: 1, T: 0 },
  kepler: { M: -1, L: 3, T: 0 },
  escape: { M: 0, L: 1, T: -2 },
  wrong: { M: 1, L: 2, T: -1 }
};
function sup(n) {
  const map = { '-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹' };
  return String(n).split('').map(c => map[c] || c).join('');
}
function dimString(d) {
  const parts = [];
  for (const k of ['M', 'L', 'T']) if (d[k]) parts.push(k + (d[k] === 1 ? '' : sup(d[k])));
  return parts.length ? parts.join(' ') : 'dimensionless';
}
function initUnits() {
  bind('units', () => {
    const key = $('units-formula').value, want = DIMS[key];
    const guess = { M: value('units-m'), L: value('units-l'), T: value('units-t') };
    const same = ['M', 'L', 'T'].every(k => guess[k] === want[k]);
    out('units', 'want', dimString(want));
    out('units', 'got', dimString(guess));
    out('units', 'verdict', same ? '✓ dimensions agree' : '✗ cannot equal the target');
    out('units', 'pi', same ? 'yes — a pure-number ratio' : 'not yet');
    let b = `<rect x="60" y="36" width="560" height="62" rx="8" fill="#eff6ff" stroke="#2457c5"/>`;
    b += text(80, 62, 'Target: ' + $('units-formula').selectedOptions[0].textContent, 'text-anchor="start"');
    b += `<text x="80" y="86" fill="#1e3a8a" font-size="15" font-weight="700">${esc(dimString(want))}</text>`;
    b += `<rect x="60" y="110" width="560" height="62" rx="8" fill="${same ? '#f0fdf7' : '#fef2f2'}" stroke="${same ? '#059669' : '#b91c1c'}"/>`;
    b += text(80, 136, 'Your candidate', 'text-anchor="start"');
    b += `<text x="80" y="160" fill="${same ? '#047857' : '#b91c1c'}" font-size="15" font-weight="700">${esc(dimString(guess))}</text>`;
    ['M', 'L', 'T'].forEach((k, i) => {
      const x = 90 + i * 180, base = 268, h = clamp(guess[k], -2, 4) * 15;
      b += line(x, base, x + 130, base, '#94a3b8');
      b += `<rect x="${x + 10}" y="${h >= 0 ? base - h : base}" width="110" height="${Math.abs(h) || 1}" fill="${guess[k] === want[k] ? '#a7f3d0' : '#fecaca'}"/>`;
      b += text(x + 65, base + 18, k + ' exponent', 'text-anchor="middle"');
      b += line(x + 10, base - want[k] * 15, x + 120, base - want[k] * 15, '#2457c5', 'stroke-dasharray="5 4"');
    });
    b += text(340, 312, 'Dashed line = the exponent the target demands', 'text-anchor="middle"');
    draw('units', b);
    summary('units', same
      ? 'Dimensions agree. Any dimensionless constant (2π, ½, a pure number) is still unknown — dimensions never fix it.'
      : 'Dimensions disagree, so no choice of constant can rescue the relation. Change one exponent and check again.');
  });
}
init.units = initUnits;
EXPORTS.dimString = dimString;
EXPORTS.DIMS = DIMS;

/* ---- 02.01 ---- */
/* 02.01 — projectile range and time of flight */
function projectileModel(v0, angle, g) {
  const a = angle * D2R, vx = v0 * Math.cos(a), vy = v0 * Math.sin(a);
  const t = 2 * vy / g;
  return { vx, vy, t, range: vx * t, apex: vy * vy / (2 * g), tApex: vy / g };
}
function initProjectile() {
  bind('projectile', () => {
    const v0 = value('proj-v'), ang = value('proj-a'), g = value('proj-g');
    const m = projectileModel(v0, ang, g);
    out('projectile', 'range', fmt(m.range, 2) + ' m');
    out('projectile', 'apex', fmt(m.apex, 2) + ' m');
    out('projectile', 'time', fmt(m.t, 2) + ' s');
    out('projectile', 'vx', fmt(m.vx, 2) + ' m/s');
    const xmax = Math.max(10, projectileModel(v0, 45, g).range * 1.1);
    const ymax = Math.max(5, m.apex * 1.25);
    const X = x => 70 + x / xmax * 560, Y = y => 268 - y / ymax * 210;
    let b = line(70, 268, 640, 268, '#64748b') + line(70, 268, 70, 40, '#64748b');
    b += text(350, 300, 'horizontal distance (m)', 'text-anchor="middle"');
    b += text(20, 40, 'height (m)');
    const pts = [];
    for (let i = 0; i <= 160; i++) {
      const t = m.t * i / 160;
      pts.push([X(m.vx * t), Y(m.vy * t - 0.5 * g * t * t)]);
    }
    b += path(pts, '#2457c5');
    b += dot(X(m.range), 268, 5) + dot(X(m.vx * m.tApex), Y(m.apex), 4, '#059669');
    b += line(X(m.range), 268, X(m.range), 60, '#94a3b8', 'stroke-dasharray="5 4"');
    b += text(X(m.range), 52, fmt(m.range, 1) + ' m', 'text-anchor="middle"');
    draw('projectile', b);
    const pair = 90 - ang;
    summary('projectile', 'Time of flight 2v₀sinθ/g grows with angle, but horizontal speed v₀cosθ falls: the product peaks at 45°. '
      + `At ${fmt(ang, 0)}° the range is ${fmt(m.range, 1)} m; at the complementary ${fmt(pair, 0)}° it is the same (${fmt(projectileModel(v0, pair, g).range, 1)} m).`);
  });
}
init.projectile = initProjectile;
EXPORTS.projectileModel = projectileModel;

/* ---- 02.02 ---- */
/* 02.02 — ladder equilibrium */
function ladderModel(L, m, angle, muWall, muFloor = 0.45, g = 9.81) {
  const a = angle * D2R, W = m * g;
  // Torque about the foot: the wall reaction Ww acts horizontally at height L sin a (lever arm L sin a),
  // the wall friction mu*Ww acts vertically at horizontal distance L cos a, and the weight
  // acts at horizontal distance (L/2) cos a.  Hence Ww L sin a + muW Ww L cos a = W (L/2) cos a.
  const denom = Math.sin(a) + muWall * Math.cos(a);
  const Ww = denom > 1e-9 ? W * 0.5 * Math.cos(a) / denom : Infinity;
  const fNeeded = Ww, fMax = muFloor * W;
  // Critical angle: Ww = muFloor W  =>  0.5 cos a / (sin a + muW cos a) = muFloor
  // 0.5 cos a = muF sin a + muF muW cos a  =>  tan a = (0.5 - muF muW) / muF
  const k = 0.5 - muFloor * muWall;
  const critical = k > 1e-9 ? Math.atan(k / muFloor) * R2D : 90;
  return { W, Ww, fNeeded, fMax, stable: fNeeded <= fMax, critical, nf: W };
}
function initLadder() {
  bind('ladder', () => {
    const m = ladderModel(value('ladder-l'), value('ladder-m'), value('ladder-a'),
      value('ladder-mu'));
    out('ladder', 'nf', fmt(m.nf, 1) + ' N');
    out('ladder', 'ffloor', fmt(m.fNeeded, 1) + ' N');
    out('ladder', 'fmax', fmt(m.fMax, 1) + ' N');
    out('ladder', 'status', m.stable ? 'holds' : 'slips');
    out('ladder', 'angle', fmt(m.critical, 1) + '°');
    let b = line(80, 260, 640, 260, '#64748b') + line(80, 260, 80, 40, '#64748b');
    const L = value('ladder-l'), ang = value('ladder-a') * D2R;
    const px = x => 80 + x / (L * 1.15) * 520, py = y => 260 - y / (L * 1.15) * 210;
    b += text(350, 300, 'horizontal distance (m)', 'text-anchor="middle"');
    b += text(20, 40, 'height (m)');
    b += `<line x1="${px(0)}" y1="${py(0)}" x2="${px(L * Math.cos(ang))}" y2="${py(L * Math.sin(ang))}" stroke="#2457c5" stroke-width="5"/>`;
    b += dot(px(0), py(0), 6, '#1e3a8a');
    b += dot(px(L * Math.cos(ang)), py(L * Math.sin(ang)), 6, '#1e3a8a');
    b += `<line x1="${px(0)}" y1="${py(0)}" x2="${px(0.35)}" y2="${py(0.35 * Math.tan(ang))}" stroke="#b45309" stroke-width="3" stroke-dasharray="5 4"/>`;
    b += text(px(0.38), py(0.38 * Math.tan(ang)), 'friction', 'text-anchor="start"');
    draw('ladder', b);
    summary('ladder', m.stable
      ? `Friction needed ${fmt(m.fNeeded, 0)} N is below the ${fmt(m.fMax, 0)} N available, so the ladder holds. The critical angle is ${fmt(m.critical, 1)}°: below it the required friction exceeds the limit.`
      : `Friction needed ${fmt(m.fNeeded, 0)} N exceeds the ${fmt(m.fMax, 0)} N available, so the ladder slips. The critical angle is ${fmt(m.critical, 1)}°.`);
  });
}
init.ladder = initLadder;
EXPORTS.ladderModel = ladderModel;

/* ---- 02.03 ---- */
/* 02.03 — one-dimensional collisions with restitution e */
function collisionModel(m1, v1, m2, v2, e) {
  const p = m1 * v1 + m2 * v2, M = m1 + m2;
  const vcm = p / M;
  // Relative velocity reverses and shrinks by e.
  const uRel = v1 - v2;
  // The relative velocity reverses and shrinks by e: v1f - v2f = -e (v1 - v2).
  const v1f = vcm - (m2 / M) * e * uRel;
  const v2f = vcm + (m1 / M) * e * uRel;
  const keIn = 0.5 * m1 * v1 * v1 + 0.5 * m2 * v2 * v2;
  const keOut = 0.5 * m1 * v1f * v1f + 0.5 * m2 * v2f * v2f;
  return { v1f, v2f, keIn, keOut, lost: keIn - keOut, p, vcm, pf: m1 * v1f + m2 * v2f };
}
function initCollision() {
  bind('collision', () => {
    const eKey = $('col-type').value;
    const e = eKey === 'elastic' ? 1 : eKey === 'inelastic' ? 0 : 0.5;
    const m = collisionModel(value('col-m1'), value('col-v1'), value('col-m2'), value('col-v2'), e);
    out('collision', 'v1f', fmt(m.v1f, 2) + ' m/s');
    out('collision', 'v2f', fmt(m.v2f, 2) + ' m/s');
    out('collision', 'pf', fmt(m.pf, 2) + ' kg m/s');
    out('collision', 'ke', fmt(m.lost, 2) + ' J of ' + fmt(m.keIn, 2) + ' J');
    out('collision', 'com', fmt(m.vcm, 2) + ' m/s');
    const X = t => 340 + t * 62;
    let b = line(60, 190, 640, 190, '#64748b');
    b += text(340, 300, 'position (arbitrary units)', 'text-anchor="middle"');
    b += text(340, 34, 'before and after: the centre of mass moves at a constant speed', 'text-anchor="middle"');
    b += dot(X(-1.6), 170, 4 + 5 * value('col-m1'), '#2457c5');
    b += dot(X(0.6), 210, 4 + 5 * value('col-m2'), '#7c3aed');
    b += dot(X(-1.6 + 2.2 * 0), 120, 6, '#94a3b8');
    b += `<line x1="${X(-2.4)}" y1="120" x2="${X(2.4)}" y2="120" stroke="#cbd5e1" stroke-dasharray="5 4"/>`;
    b += text(X(-2.4) + 4, 108, 'centre of mass track', 'text-anchor="start"');
    const arrowAt = (t, y, v, col) => {
      const len = clamp(Math.abs(v) * 16, 0, 90) * Math.sign(v || 1);
      return `<line x1="${X(t)}" y1="${y}" x2="${X(t) + len}" y2="${y}" stroke="${col}" stroke-width="3"/>`;
    };
    b += arrowAt(-1.6, 152, value('col-v1'), '#2457c5');
    b += arrowAt(0.6, 232, value('col-v2'), '#7c3aed');
    b += text(X(-1.6), 140, 'v₁', 'text-anchor="middle"');
    b += text(X(0.6), 250, 'v₂', 'text-anchor="middle"');
    draw('collision', b);
    summary('collision', e === 1
      ? `Perfectly elastic: momentum ${fmt(m.pf, 2)} kg m/s is conserved and the kinetic energy loss is ${fmt(m.lost, 3)} J — zero, as it must be.`
      : `Momentum is still conserved (${fmt(m.pf, 2)} kg m/s) but ${fmt(m.lost, 2)} J of kinetic energy has gone into deformation and heat. In the centre-of-mass frame the total momentum is always zero, however the collision ends.`);
  });
}
init.collision = initCollision;
EXPORTS.collisionModel = collisionModel;

/* ---- 02.04 ---- */
/* 02.04 — orbit geometry and vis-viva speed */
function orbitModel(a, e, nu, mu = 398600.4418, R = 6371) {
  const p = a * (1 - e * e);
  const r = p / (1 + e * Math.cos(nu * D2R));
  const v = Math.sqrt(mu * (2 / r - 1 / a));
  const rp = a * (1 - e), ra = a * (1 + e);
  const vp = Math.sqrt(mu * (2 / rp - 1 / a)), va = Math.sqrt(mu * (2 / ra - 1 / a));
  const T = 2 * Math.PI * Math.sqrt(a ** 3 / mu);
  return { r, v, rp, ra, vp, va, T, p };
}
function initOrbit() {
  bind('orbit', () => {
    const a = value('orbit-r') * 6371, e = value('orbit-e'), nu = value('orbit-nu');
    const m = orbitModel(a, e, nu);
    out('orbit', 'r', fmt(m.r / 6371, 2) + ' R⊕');
    out('orbit', 'v', fmt(m.v, 3) + ' km/s');
    out('orbit', 'peri', fmt(m.vp, 3) + ' km/s');
    out('orbit', 'apo', fmt(m.va, 3) + ' km/s');
    out('orbit', 'T', fmt(m.T / 60, 1) + ' min');
    const b = a * Math.sqrt(1 - e * e);
    const X = x => 340 + x / (a * 1.3) * 260, Y = y => 165 + y / (a * 1.3) * 260;
    let g = `<ellipse cx="340" cy="165" rx="${a / (a * 1.3) * 260}" ry="${b / (a * 1.3) * 260}" fill="none" stroke="#2457c5" stroke-width="2.4"/>`;
    g += `<circle cx="${X(-a * e)}" cy="165" r="10" fill="#b45309"/>`;
    g += `<circle cx="${X(a * (1 - e * e) / (1 + e * Math.cos(nu * D2R)) * Math.cos(nu * D2R) - a * e)}" cy="${Y(a * (1 - e * e) / (1 + e * Math.cos(nu * D2R)) * Math.sin(nu * D2R))}" r="6" fill="#059669"/>`;
    g += text(340, 320, 'central body at the occupied focus; the empty focus is a geometric point', 'text-anchor="middle"');
    g += text(340, 26, 'a = ' + fmt(value('orbit-r'), 1) + ' R⊕, e = ' + fmt(e, 2) + ', ν = ' + fmt(nu, 0) + '°', 'text-anchor="middle"');
    draw('orbit', g);
    summary('orbit', 'The vis-viva equation gives the speed at every point; the body is fastest at periapsis and slowest at apoapsis. '
      + `Here the speed ranges from ${fmt(m.vp, 2)} to ${fmt(m.va, 2)} km/s. Kepler's second law is the statement that the radius vector sweeps equal areas in equal times, so a shorter radius means a larger speed.`);
  });
}
init.orbit = initOrbit;
EXPORTS.orbitModel = orbitModel;

/* ---- 02.05 ---- */
/* 02.05 — Torricelli jet from a tank */
function torricelliModel(h, H, d, g = 9.81, rho = 1000) {
  const A = Math.PI * (d / 2000) ** 2;       // m²
  const v = Math.sqrt(2 * g * h);
  const Q = A * v;                            // m³/s
  const t = (v * v) / (2 * g);                // fall time from the hole at height H
  const range = v * Math.sqrt(2 * Math.max(H, 0) / g);
  const empty = Q > 0 ? (1.0 * A) / Q : Infinity; // placeholder tank volume = A_tank*h with A_tank = 1 m² reference
  return { v, Q, range, t, empty };
}
function initTorricelli() {
  bind('torricelli', () => {
    const m = torricelliModel(value('tor-h'), value('tor-H'), value('tor-d'));
    out('torricelli', 'v', fmt(m.v, 2) + ' m/s');
    out('torricelli', 'range', fmt(m.range, 2) + ' m');
    out('torricelli', 'flow', sci(m.Q, 2) + ' m³/s');
    out('torricelli', 'time', Number.isFinite(m.empty) ? fmt(m.empty / 60, 1) + ' min*' : '—');
    let b = line(60, 270, 640, 270, '#64748b');
    const h = value('tor-h'), H = value('tor-H'), d = value('tor-d');
    const scale = 200 / Math.max(2, h + H);
    const tankTop = 270 - (h + H) * scale, holeY = 270 - H * scale;
    b += `<rect x="120" y="${tankTop}" width="120" height="${(h + H) * scale}" fill="#dbeafe" stroke="#2457c5" stroke-width="2"/>`;
    b += `<rect x="120" y="${holeY}" width="120" height="${h * scale}" fill="#93c5fd"/>`;
    b += `<circle cx="242" cy="${holeY}" r="${Math.max(2, d / 2)}" fill="#1e3a8a"/>`;
    // jet parabola
    const pts = [];
    for (let i = 0; i <= 60; i++) {
      const t = (m.t * i / 60);
      pts.push([242 + m.v * t * 18, holeY + 0.5 * 9.81 * t * t * 18]);
    }
    b += path(pts, '#059669');
    b += text(340, 40, 'jet from a hole of diameter ' + d + ' mm', 'text-anchor="middle"');
    b += text(340, 300, 'tank drawn to scale; time marked * assumes a 1 m² tank section', 'text-anchor="middle"');
    draw('torricelli', b);
    summary('torricelli', 'Torricelli’s law gives v = √(2gh): the speed depends only on the depth, not on the hole size. '
      + 'A bigger hole gives more volume per second but the same speed, and the jet falls as a projectile, so the horizontal range is v√(2H/g).');
  });
}
init.torricelli = initTorricelli;
EXPORTS.torricelliModel = torricelliModel;

/* ---- 02.06 ---- */
/* 02.06 — loaded potential divider */
function dividerModel(V, R1, R2, RL) {
  const ideal = V * R2 / (R1 + R2);
  const parallel = RL === 0 ? 0 : (R2 * RL) / (R2 + RL);
  const real = V * parallel / (R1 + parallel);
  const current = V / (R1 + parallel);
  const power = V * current;
  const delivered = (real * real) / (RL || Infinity);
  return { ideal, real, err: ideal === 0 ? 0 : (real - ideal) / ideal, power, delivered, current };
}
function initDivider() {
  bind('divider', () => {
    const m = dividerModel(value('div-v'), value('div-r1'), value('div-r2'), value('div-rl'));
    out('divider', 'ideal', fmt(m.ideal, 3) + ' V');
    out('divider', 'real', fmt(m.real, 3) + ' V');
    out('divider', 'err', fmt(100 * m.err, 1) + ' %');
    out('divider', 'power', fmt(m.power * 1000, 1) + ' mW');
    out('divider', 'eff', fmt(100 * m.delivered / m.power, 1) + ' %');
    let b = axes('load resistance R_L (kΩ, log scale)', 'output voltage (V)');
    const pts = [];
    for (let i = 0; i <= 60; i++) {
      const RL = 1000 * Math.pow(10, i / 60 * 3);
      const mm = dividerModel(value('div-v'), value('div-r1'), value('div-r2'), RL);
      pts.push([60 + i / 60 * 585, 275 - mm.real / value('div-v') * 250]);
    }
    b += path(pts);
    const yIdeal = 275 - m.ideal / value('div-v') * 250;
    b += line(60, yIdeal, 645, yIdeal, '#059669', 'stroke-dasharray="6 4"');
    draw('divider', b);
    summary('divider', `With a heavy load the output sags below the ideal ${fmt(m.ideal, 2)} V: the divider's own Thevenin `
      + `resistance R₁∥R₂ sets how much current it can supply. The error is ${fmt(100 * m.err, 1)}% at R_L = ${fmt(value('div-rl') / 1000, 0)} kΩ.`);
  });
}
init.divider = initDivider;
EXPORTS.dividerModel = dividerModel;

/* ---- 02.07 ---- */
/* 02.07 — charged particle in a uniform magnetic field */
function cyclotronModel(m, q, B, v) {
  const r = (m * v) / (q * B);
  const T = (2 * Math.PI * m) / (q * B);
  const f = 1 / T;
  return { r, T, f, k: 0.5 * m * v * v, omega: q * B / m };
}
function initCyclotron() {
  bind('cyclotron', () => {
    const u = 1.66053907e-27, e = 1.602176634e-19;
    const m = value('cyc-m') * u, q = value('cyc-q') * e, B = value('cyc-B'), v = value('cyc-v') * 1e6;
    const mm = cyclotronModel(m, q, B, v);
    out('cyclotron', 'r', fmt(mm.r * 1000, 3) + ' mm');
    out('cyclotron', 'f', fmt(mm.f / 1e6, 2) + ' MHz');
    out('cyclotron', 'T', fmt(mm.T * 1e9, 1) + ' ns');
    out('cyclotron', 'k', fmt(mm.k / e / 1e6, 3) + ' MeV');
    out('cyclotron', 'check', 'r/(mv/qB) = ' + fmt(mm.r / (m * v / (q * B)), 3));
    const Rpx = 120, scale = Rpx / Math.max(mm.r, 1e-9);
    let b = line(60, 275, 640, 275, '#64748b') + line(60, 275, 60, 25, '#64748b');
    b += text(350, 315, 'displacement (scaled to fit)', 'text-anchor="middle"');
    b += `<circle cx="330" cy="150" r="${Math.min(115, mm.r * scale)}" fill="none" stroke="#2457c5" stroke-width="2.6"/>`;
    b += `<circle cx="330" cy="150" r="4" fill="#7c3aed"/>`;
    b += text(330, 30, 'orbit radius ' + fmt(mm.r * 1000, 2) + ' mm', 'text-anchor="middle"');
    draw('cyclotron', b);
    summary('cyclotron', 'The radius grows with momentum and shrinks with field: r = mv/(qB). The period is independent of speed — '
      + `the cyclotron principle. Here f = ${fmt(mm.f / 1e6, 2)} MHz and T = ${fmt(mm.T * 1e9, 0)} ns.`);
  });
}
init.cyclotron = initCyclotron;
EXPORTS.cyclotronModel = cyclotronModel;

/* ---- 02.08 ---- */
/* 02.08 — series RLC resonance */
function rlcModel(R, L, C, Vrms) {
  const f0 = 1 / (2 * Math.PI * Math.sqrt(L * C));
  const w0 = 2 * Math.PI * f0;
  const Q = (1 / R) * Math.sqrt(L / C);
  const bw = f0 / Q;
  const Imax = Vrms / R;             // at resonance the reactances cancel
  const Vc = Imax / (w0 * C);        // voltage across C at resonance
  const Vl = Imax * w0 * L;          // equal to Vc in the ideal case
  const zeta = R / 2 * Math.sqrt(C / L);
  return { f0, w0, Q, bw, Imax, Vc, Vl, zeta };
}
function initRlc() {
  bind('rlc', () => {
    const R = value('rlc-r'), L = value('rlc-l') * 1e-3, C = value('rlc-c') * 1e-6;
    const Vrms = 10;
    const m = rlcModel(R, L, C, Vrms);
    out('rlc', 'f0', fmt(m.f0, 1) + ' Hz');
    out('rlc', 'q', fmt(m.Q, 2));
    out('rlc', 'bw', fmt(m.bw, 1) + ' Hz');
    out('rlc', 'imax', fmt(m.Imax, 3) + ' A');
    out('rlc', 'vc', fmt(m.Vc, 1) + ' V');
    const W = 620, H = 250, left = 70, top = 30, bottom = 210;
    const x0 = Math.log10(0.1), x1 = Math.log10(10);
    const peak = m.Imax;
    const X = (w) => left + (Math.log10(w) - x0) / (x1 - x0) * W;
    const Y = (i) => bottom - (i / peak) * (bottom - top);
    let b = line(left, bottom, left + W, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    for (const dec of [0.1, 1, 10]) {
      b += line(X(dec), top, X(dec), bottom, '#e2e8f0');
      b += text(X(dec), bottom + 18, dec + ' f₀', 'text-anchor="middle"');
    }
    b += text(left + W / 2, bottom + 40, 'frequency (as a multiple of resonance)', 'text-anchor="middle"');
    b += text(left - 12, top + 6, 'I', 'text-anchor="end"');
    let pts = '';
    for (let i = 0; i <= 200; i++) {
      const w = Math.pow(10, x0 + (x1 - x0) * i / 200);
      const re = R, im = m.w0 * L * (w - 1 / w);
      const z = Math.sqrt(re * re + im * im);
      pts += `${X(w).toFixed(1)},${Y(Vrms / z).toFixed(1)} `;
    }
    b += `<polyline points="${pts}" fill="none" stroke="#2457c5" stroke-width="2.6"/>`;
    b += line(X(1), top, X(1), bottom, '#b45309', 1.4, '5 4');
    b += text(X(1) + 6, top + 14, 'resonance', 'text-anchor="start"', '#b45309');
    draw('rlc', b);
    summary('rlc', `At resonance f₀ = ${fmt(m.f0, 1)} Hz the reactances cancel and the current is limited only by R: `
      + `I = ${fmt(m.Imax, 2)} A. The voltage across the capacitor is then Q times the supply, ${fmt(m.Vc, 0)} V, `
      + `which is why high-Q circuits need components rated for high voltage.`);
  });
}
init.rlc = initRlc;
EXPORTS.rlcModel = rlcModel;

/* ---- 02.09 ---- */
/* 02.09 — the simple pendulum, small-angle formula versus the exact period */
function pendulumModel(L, theta0deg, g) {
  const t0 = theta0deg * Math.PI / 180;
  const small = 2 * Math.PI * Math.sqrt(L / g);
  const k = Math.sin(t0 / 2);
  // complete elliptic integral of the first kind via the arithmetic-geometric mean
  let a = 1, b = Math.sqrt(1 - k * k);
  for (let i = 0; i < 40; i++) { const an = (a + b) / 2, bn = Math.sqrt(a * b); a = an; b = bn; }
  const K = Math.PI / (2 * a);
  const exact = 4 * Math.sqrt(L / g) * K;
  const vmax = Math.sqrt(2 * g * L * (1 - Math.cos(t0)));
  return { small, exact, err: (exact - small) / small, f: 1 / exact, vmax, theta0: t0 };
}
function initPendulum() {
  bind('pendulum-swing', () => {
    const L = value('swing-l'), a = value('swing-a'), g = value('swing-g');
    const m = pendulumModel(L, a, g);
    out('pendulum-swing', 'T', fmt(m.small, 3) + ' s');
    out('pendulum-swing', 'Tex', fmt(m.exact, 3) + ' s');
    out('pendulum-swing', 'err', fmt(m.err * 100, 2) + ' %');
    out('pendulum-swing', 'f', fmt(m.f, 3) + ' Hz');
    out('pendulum-swing', 'vmax', fmt(m.vmax, 2) + ' m/s');
    const cx = 340, cy = 60, R = 190;
    let b = line(200, cy, 480, cy, '#64748b', 'stroke-width="4"');
    b += text(200, cy - 10, 'pivot', 'text-anchor="start"');
    // extreme positions and the true swing arc
    for (const s of [-1, 1]) {
      const th = s * m.theta0;
      b += line(cx, cy, cx + R * Math.sin(th), cy + R * Math.cos(th), '#cbd5e1', 'stroke-dasharray="5 4"');
    }
    const th = m.theta0;
    b += line(cx, cy, cx + R * Math.sin(th), cy + R * Math.cos(th), '#1e3a8a', 'stroke-width="2.4"');
    b += `<path d="M${cx + 90 * Math.sin(-th).toFixed(1)},${(cy + 90 * Math.cos(th)).toFixed(1)} A90,90 0 0,1 ${(cx + 90 * Math.sin(th)).toFixed(1)},${(cy + 90 * Math.cos(th)).toFixed(1)}" fill="none" stroke="#94a3b8"/>`;
    b += line(cx, cy, cx, cy + R + 30, '#e2e8f0', 'stroke-dasharray="4 4"');
    b += dot(cx + R * Math.sin(th), cy + R * Math.cos(th), 9, '#b45309');
    b += text(cx + 12, cy + 60, 'θ = ' + fmt(a, 0) + '°', 'text-anchor="start"');
    b += text(cx, cy + R + 55, 'T = ' + fmt(m.exact, 3) + ' s   (small-angle ' + fmt(m.small, 3) + ' s)', 'text-anchor="middle" style="font-size:13px"');
    draw('pendulum-swing', b);
    summary('pendulum-swing', `Small angles: T = 2π√(L/g) = ${fmt(m.small, 3)} s. At ${fmt(a, 0)}° the exact period is `
      + `${fmt(m.exact, 3)} s, ${fmt(m.err * 100, 1)}% longer, because the restoring force mg sinθ is weaker than mgθ. `
      + `The bob passes the lowest point at ${fmt(m.vmax, 2)} m/s.`);
  });
}
init['pendulum-swing'] = initPendulum;
EXPORTS.pendulumModel = pendulumModel;

/* ---- 02.10 ---- */
/* 02.10 — Doppler shift for sound, and the light comparison */
function dopplerModel(f, vs, vo, v) {
  v = v || 343;
  const approach = f * v / (v - vs) * (v + vo) / v;      // source approaching, observer approaching
  const recede = f * v / (v + vs) * (v - vo) / v;        // both moving away
  const c = 299792458;
  const light = f * Math.sqrt((1 + vs / c) / (1 - vs / c));
  return { approach, recede, df: approach - f, light, ratio: approach / recede, shock: vs / v };
}
function initDoppler() {
  bind('doppler', () => {
    const f = value('dop-f'), vs = value('dop-vs'), vo = value('dop-vo');
    const m = dopplerModel(f, vs, vo, 343);
    out('doppler', 'fa', fmt(m.approach, 1) + ' Hz');
    out('doppler', 'fr', fmt(m.recede, 1) + ' Hz');
    out('doppler', 'df', fmt(m.df, 1) + ' Hz');
    out('doppler', 'light', sci((m.light - f) / f, 2));
    out('doppler', 'ratio', fmt(m.ratio, 3));
    const cx = 340, cy = 175, R = 130;
    let b = line(60, cy, 620, cy, '#e2e8f0', 'stroke-dasharray="4 4"');
    b += line(cx, 30, cx, 300, '#e2e8f0', 'stroke-dasharray="4 4"');
    // wavefront spacing: lambda ahead = (v - vs)/f, behind = (v + vs)/f, drawn to scale
    const lam0 = 343 / f;                       // metres
    const pxPerM = 60 / lam0;
    const ahead = Math.max(4, (343 - vs) / f * pxPerM);
    const behind = (343 + vs) / f * pxPerM;
    for (let i = 1; i <= 6; i++) {
      if (cx + i * ahead < 630) b += `<circle cx="${(cx + i * ahead).toFixed(0)}" cy="${cy}" r="10" fill="none" stroke="#2457c5"/>`;
      if (cx - i * behind > 50) b += `<circle cx="${(cx - i * behind).toFixed(0)}" cy="${cy}" r="10" fill="none" stroke="#7ea6f0"/>`;
    }
    b += dot(cx, cy, 8, '#b45309');
    b += text(cx + 12, cy - 12, 'source', 'text-anchor="start"');
    b += text(60, 40, 'front: crests ' + fmt(ahead / pxPerM, 3) + ' m apart (squashed)', 'text-anchor="start"');
    b += text(60, 60, 'behind: crests ' + fmt(behind / pxPerM, 3) + ' m apart (stretched)', 'text-anchor="start"');
    b += text(60, 316, 'observer hears ' + fmt(m.approach, 0) + ' Hz ahead and ' + fmt(m.recede, 0) + ' Hz behind', 'text-anchor="start"');
    draw('doppler', b);
    summary('doppler', `Approaching: ${fmt(m.approach, 1)} Hz, receding: ${fmt(m.recede, 1)} Hz, a shift of ${fmt(m.df, 1)} Hz `
      + `at ${fmt(f, 0)} Hz. If this were light, the same speed would shift the frequency by the fraction `
      + `${sci((m.light - f) / f, 2)} only — sound needs the air as a medium, light does not, and at these speeds the `
      + `relativistic effect is minute.`);
  });
}
init.doppler = initDoppler;
EXPORTS.dopplerModel = dopplerModel;

/* ---- 02.11 ---- */
/* 02.11 — the thin lens, with a ray diagram drawn to scale */
function lensModel(f, u, h) {
  // all lengths in cm; real-is-positive convention for a converging lens
  const inv = 1 / f - 1 / u;
  const v = Math.abs(inv) < 1e-9 ? Infinity : 1 / inv;
  const m = Number.isFinite(v) ? -v / u : -Infinity;
  const real = Number.isFinite(v) && v > 0;
  return { v, m, real, hi: m * h, power: 100 / f, vertex: 0 };
}
function initThinLens() {
  bind('thin-lens', () => {
    const f = value('lens-f'), u = value('lens-u'), h = value('lens-h');
    const m = lensModel(f, u, h);
    out('thin-lens', 'v', Number.isFinite(m.v) ? fmt(m.v, 1) + ' cm' : 'at infinity');
    out('thin-lens', 'm', fmt(m.m, 2));
    out('thin-lens', 'type', m.real ? (Math.abs(m.m) > 1 ? 'real, magnified, inverted' : 'real, diminished, inverted')
      : 'virtual, upright');
    out('thin-lens', 'hi', fmt(Math.abs(m.hi), 2) + ' cm');
    out('thin-lens', 'power', fmt(m.power, 2) + ' D');
    // geometry: put the lens at x = 430, 1 cm = 3.2 px
    const sx = 3.2, lx = 430, axis = 150;
    let b = line(40, axis, 660, axis, '#cbd5e1', 'stroke-dasharray="6 4"');
    b += `<path d="M${lx},${axis - 95} Q${lx + 34},${axis} ${lx},${axis + 95} Q${lx - 34},${axis} ${lx},${axis - 95} Z" fill="#e0f2fe" stroke="#2457c5" stroke-width="2"/>`;
    b += dot(lx + f * sx, axis, 4, '#b91c1c') + text(lx + f * sx + 4, axis + 16, 'F', 'text-anchor="start"');
    b += dot(lx - f * sx, axis, 4, '#b91c1c') + text(lx - f * sx - 4, axis + 16, 'F′', 'text-anchor="end"');
    // object
    const ox = lx - u * sx;
    b += `<line x1="${ox.toFixed(1)}" y1="${axis}" x2="${ox.toFixed(1)}" y2="${(axis - h * sx).toFixed(1)}" stroke="#b45309" stroke-width="3"/>`;
    b += text(ox, axis + 16, 'object', 'text-anchor="middle"');
    if (Number.isFinite(m.v)) {
      const ix = lx + m.v * sx;
      const ih = -m.hi;
      b += `<line x1="${ix.toFixed(1)}" y1="${axis}" x2="${ix.toFixed(1)}" y2="${(axis - ih * sx).toFixed(1)}" stroke="${m.real ? '#059669' : '#7c3aed'}" stroke-width="3" stroke-dasharray="${m.real ? '' : '6 4'}"/>`;
      b += text(ix, axis + (m.real ? 34 : 16), m.real ? 'real image' : 'virtual image', 'text-anchor="middle"');
      // principal rays: parallel then through F, and through the centre
      b += line(ox, axis - h * sx, lx, axis - h * sx, '#f59e0b', 'stroke-dasharray="4 3"');
      b += line(lx, axis - h * sx, Math.max(30, Math.min(650, ix)), axis - ih * sx, '#f59e0b', 'stroke-dasharray="4 3"');
      b += line(ox, axis - h * sx, Math.max(30, Math.min(650, ix)), axis - ih * sx, '#f59e0b', 'stroke-dasharray="2 3"');
    } else {
      b += text(560, 90, 'is = ∞: parallel rays leave the lens', 'text-anchor="middle"');
    }
    draw('thin-lens', b);
    summary('thin-lens', m.real
      ? `The image is real and inverted, ${fmt(Math.abs(m.v), 1)} cm beyond the lens, with magnification ${fmt(m.m, 2)}. `
        + `It could be caught on a screen there.`
      : `The image is virtual and upright, ${fmt(Math.abs(m.v), 1)} cm on the same side as the object, with magnification `
        + `${fmt(m.m, 2)} — this is the magnifying-glass case, and you must look through the lens to see it.`);
  });
}
init['thin-lens'] = initThinLens;
EXPORTS.lensModel = lensModel;

/* ---- 02.12 ---- */
/* 02.12 — relativistic travel */
function relativityModel(beta, lightYears, mass) {
  const c = 299792458, yr = 3.15576e7;
  const g = 1 / Math.sqrt(1 - beta * beta);
  const labTime = lightYears / beta;              // years, since distance is in light years
  const properTime = labTime / g;                 // traveller's clock
  const length = lightYears / g;                  // contracted distance in the traveller's frame
  const energy = (g - 1) * mass * c * c;          // joules
  const momentum = g * mass * beta * c;
  return { g, labTime, properTime, length, energy, momentum, beta };
}
function initRelativity() {
  bind('relativity', () => {
    const b = value('rel-b'), d = value('rel-d'), m0 = value('rel-m');
    const m = relativityModel(Math.min(b, 0.9999), d, m0);
    out('relativity', 'gamma', fmt(m.g, 4));
    out('relativity', 'clock', fmt(m.properTime, 3) + ' yr');
    out('relativity', 'length', fmt(m.length, 3) + ' ly');
    out('relativity', 'energy', sci(m.energy, 3) + ' J');
    out('relativity', 'mass', sci(m.g * m0, 3) + ' kg equivalent');
    const left = 70, right = 640, top = 40, bottom = 250;
    let s = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    s += text(left + 6, top + 6, 'lab time (years)', 'text-anchor="start"');
    s += text(right - 6, bottom + 24, 'distance (light years)', 'text-anchor="end"');
    // mark the traveller's clock at evenly spaced lab times
    const xmax = Math.max(1, d);
    const X = (x) => left + (x / xmax) * (right - left);
    const Y = (t) => bottom - Math.min(1, t / Math.max(1, d / Math.max(0.05, b))) * (bottom - top);
    s += path([[X(0), Y(0)], [X(xmax), Y(xmax / Math.max(0.05, b))]], '#2457c5');
    for (let i = 0; i <= 5; i++) {
      const x = xmax * i / 5, tLab = x / Math.max(0.05, b), tProp = tLab / m.g;
      if (tLab / Math.max(1, d / Math.max(0.05, b)) <= 1) {
        s += dot(X(x), Y(tLab), 4, '#b45309');
        if (i > 0) s += text(X(x) + 6, Y(tLab) - 6, fmt(tProp, 1) + ' yr aboard');
      }
    }
    s += text(left + 10, top + 24, 'one dot = a year on the traveller’s clock', 'text-anchor="start"');
    draw('relativity', s);
    summary('relativity', `At ${fmt(b, 3)}c the Lorentz factor is ${fmt(m.g, 3)}: ten light years take `
      + `${fmt(m.labTime, 1)} years measured from Earth but only ${fmt(m.properTime, 1)} years on the traveller's clock. `
      + `The journey is ${fmt(m.length, 1)} light years long in the traveller's frame, and the kinetic energy is `
      + `${sci(m.energy, 2)} J — it is the energy cost, not the speed limit in principle, that makes relativistic travel hard.`);
  });
}
init.relativity = initRelativity;
EXPORTS.relativityModel = relativityModel;

/* ---- 02.13 ---- */
/* 02.13 — the photoelectric effect */
function photoelectricModel(phi, lambdaNm, intensity) {
  const h = 6.62607015e-34, c = 2.99792458e8, e = 1.602176634e-19;
  const f = c / (lambdaNm * 1e-9);
  const E = h * f / e;                       // photon energy in eV
  const K = Math.max(0, E - phi);            // maximum kinetic energy in eV
  const f0 = phi * e / h;                    // threshold frequency
  const lam0 = c / f0 * 1e9;                 // threshold wavelength in nm
  const n = E > phi ? intensity * (E - phi) / E : 0;   // relative electron rate
  return { f, E, K, V: K, f0, lam0, n, emits: E > phi };
}
function initPhotoelectric() {
  bind('photoelectric', () => {
    const phi = value('pe-w'), lam = value('pe-l'), inten = value('pe-i');
    const m = photoelectricModel(phi, lam, inten);
    out('photoelectric', 'E', fmt(m.E, 2) + ' eV');
    out('photoelectric', 'K', fmt(m.K, 2) + ' eV');
    out('photoelectric', 'V', fmt(m.V, 2) + ' V');
    out('photoelectric', 'f0', fmt(m.lam0, 0) + ' nm');
    out('photoelectric', 'n', fmt(m.n, 0) + ' a.u.');
    const left = 90, right = 620, top = 60, bottom = 230;
    const maxE = Math.max(5.5, m.E + 0.5);
    const Y = (e) => bottom - e / maxE * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(40, (top + bottom) / 2, 'energy (eV)', 'transform="rotate(-90 40 ' + (top + bottom) / 2 + ')"');
    // axes ticks
    for (let e = 0; e <= maxE; e += 1) {
      b += line(left - 4, Y(e), left, Y(e), '#64748b') + text(left - 8, Y(e) + 4, fmt(e, 0), 'text-anchor="end"');
    }
    // bars: photon energy, work function, kinetic energy
    const x0 = 150, w = 90, gap = 40;
    const bars = [['photon hf', m.E, '#2457c5'], ['work function φ', phi, '#b45309'], ['kinetic K', m.K, '#059669']];
    bars.forEach(([label, val, col], i) => {
      const x = x0 + i * (w + gap);
      b += `<rect x="${x}" y="${Y(val)}" width="${w}" height="${Math.max(1, bottom - Y(val))}" fill="${col}" rx="3"/>`;
      b += text(x + w / 2, bottom + 18, label, 'text-anchor="middle"');
      b += text(x + w / 2, Y(val) - 6, fmt(val, 2) + ' eV', 'text-anchor="middle"');
    });
    b += line(left, Y(0), right, Y(0), '#64748b', 'stroke-width="1.5"');
    b += text(340, 290, m.emits ? 'hf > φ: electrons are emitted, with K = hf − φ'
      : 'hf < φ: no electrons, however bright the light', 'text-anchor="middle" style="font-size:13px"');
    draw('photoelectric', b);
    summary('photoelectric', m.emits
      ? `${fmt(lam, 0)} nm light gives photons of ${fmt(m.E, 2)} eV; after paying the work function of ${fmt(phi, 1)} eV, `
        + `electrons leave with up to ${fmt(m.K, 2)} eV, stopped by ${fmt(m.V, 2)} V. The threshold is ${fmt(m.lam0, 0)} nm.`
      : `Photons of ${fmt(m.E, 2)} eV are below the ${fmt(phi, 1)} eV work function, so nothing is emitted — and raising `
        + `the intensity only supplies more photons that are each still too weak. The threshold is ${fmt(m.lam0, 0)} nm.`);
  });
}
init.photoelectric = initPhotoelectric;
EXPORTS.photoelectricModel = photoelectricModel;

/* ---- 02.14 ---- */
/* 02.14 — radioactive decay of a finite sample */
function decayModel(halfLife, N0, t) {
  const lambda = Math.LN2 / halfLife;
  const left = N0 * Math.pow(0.5, t / halfLife);
  const A = lambda * left;                  // decays per second for the nuclei remaining
  return { lambda, left, frac: left / N0, A, tau: 1 / lambda, halfLife };
}
function initDecay() {
  bind('decay', () => {
    const half = value('dec-h'), N0 = value('dec-n'), t = value('dec-t');
    const m = decayModel(half, N0, t);
    out('decay', 'left', fmt(Math.round(m.left), 0));
    out('decay', 'frac', fmt(m.frac * 100, 1) + ' %');
    out('decay', 'A', fmt(m.A, 1) + ' Bq');
    out('decay', 'lambda', fmt(m.lambda, 4) + ' /s');
    out('decay', 'tau', fmt(m.tau, 3) + ' s');
    const left = 70, right = 640, top = 40, bottom = 250;
    const T = Math.max(3 * half, t * 1.2);
    const X = (x) => left + x / T * (right - left);
    const Y = (f) => bottom - f * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'nuclei remaining', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'time (s)', 'text-anchor="end"');
    // exact exponential
    const pts = [];
    for (let i = 0; i <= 200; i++) {
      const x = T * i / 200;
      pts.push([X(x), Y(Math.pow(0.5, x / half))]);
    }
    b += path(pts, '#2457c5');
    // half-life markers
    for (let k = 1; k <= 3; k++) {
      const x = k * half;
      if (x <= T) {
        b += line(X(x), top, X(x), bottom, '#e2e8f0', 'stroke-dasharray="4 4"');
        b += text(X(x) + 4, Y(Math.pow(0.5, k)) - 4, '½^' + k, 'text-anchor="start"');
      }
    }
    // simulated finite sample: random but seeded, so it is reproducible
    const rnd = seeded(12345);
    let alive = N0;
    const sim = [[X(0), Y(1)]];
    const steps = 160;
    const p = 1 - Math.pow(0.5, T / half / steps);
    for (let i = 1; i <= steps; i++) {
      for (let n = 0; n < alive; n++) if (rnd() < p) alive--;
      sim.push([X(i * T / steps), Y(alive / N0)]);
    }
    b += path(sim, '#059669', 'stroke-dasharray="3 3" stroke-width="1.6"');
    b += dot(X(t), Y(m.frac), 6, '#b45309');
    b += text(left + 14, top + 26, 'smooth curve: N = N₀·2^(−t/T½)', 'text-anchor="start"');
    b += text(left + 14, top + 44, 'jagged line: one random sample of ' + fmt(N0, 0) + ' nuclei', 'text-anchor="start"');
    draw('decay', b);
    summary('decay', `After ${fmt(t, 1)} s (${fmt(t / half, 2)} half-lives) about ${fmt(m.frac * 100, 1)}% of the nuclei `
      + `remain, and the activity is ${fmt(m.A, 1)} decays per second. With only ${fmt(N0, 0)} nuclei the actual decay `
      + `is visibly random; with 10²³ nuclei the statistical jitter is far too small to see.`);
  });
}
init.decay = initDecay;
EXPORTS.decayModel = decayModel;

/* ---- 02.15 ---- */
/* 02.15 — the ideal gas */
function gasModel(n, V, T) {
  const R = 8.314, kB = 1.380649e-23, NA = 6.02214076e23, mu = 0.02897;   // air
  const p = n * R * T / V;
  const N = n * NA;
  const vrms = Math.sqrt(3 * R * T / mu);
  const vmp = Math.sqrt(2 * R * T / mu);
  const vmean = Math.sqrt(8 * R * T / (Math.PI * mu));
  const ek = 1.5 * kB * T;
  return { p, N, vrms, vmp, vmean, ek, density: n * mu / V };
}
function initGas() {
  bind('gas', () => {
    const n = value('gas-n'), V = value('gas-v'), T = value('gas-t');
    const m = gasModel(n, V, T);
    out('gas', 'p', (m.p / 1000).toFixed(2) + ' kPa');
    out('gas', 'vrms', fmt(m.vrms, 1) + ' m/s');
    out('gas', 'ek', sci(m.ek, 2) + ' J');
    out('gas', 'n', sci(m.N / V, 2) + ' m⁻³');
    out('gas', 'vmp', fmt(m.vmp, 1) + ' m/s');
    // speed distribution, scaled to its own peak
    const left = 70, right = 640, top = 40, bottom = 250;
    const vmax = 3 * m.vrms;
    const X = (v) => left + v / vmax * (right - left);
    const Y = (f) => bottom - f * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'relative number', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'molecular speed (m/s)', 'text-anchor="end"');
    const pts = [];
    for (let i = 0; i <= 200; i++) {
      const v = vmax * i / 200;
      const f = (v * v / (m.vmp * m.vmp)) * Math.exp(1 - v * v / (m.vmp * m.vmp));
      pts.push([X(v), Y(f)]);
    }
    b += path(pts, '#2457c5');
    for (const [val, col, lab] of [[m.vmp, '#059669', 'most probable'], [m.vmean, '#7c3aed', 'mean'], [m.vrms, '#b45309', 'rms']]) {
      b += line(X(val), Y(0), X(val), Y(1), col, 'stroke-dasharray="4 3"');
      b += text(X(val) + 4, top + 20 + 16 * ['most probable', 'mean', 'rms'].indexOf(lab), lab + ' ' + fmt(val, 0), 'text-anchor="start"');
    }
    draw('gas', b);
    summary('gas', `${n.toFixed(1)} mol at ${T.toFixed(0)} K in ${(V * 1000).toFixed(1)} L gives `
      + `${(m.p / 1000).toFixed(1)} kPa. The molecules rms speed is ${fmt(m.vrms, 0)} m/s, the most probable speed `
      + `${fmt(m.vmp, 0)} m/s, and each molecule carries on average ${sci(m.ek, 2)} J — only a function of temperature.`);
  });
}
init.gas = initGas;
EXPORTS.gasModel = gasModel;

/* ---- 02.16 ---- */
/* 02.16 — Newton's law of cooling */
function coolingModel(T0, Tamb, k, t) {
  const excess0 = T0 - Tamb;
  const excess = excess0 * Math.exp(-k * t);
  return {
    T: Tamb + excess,
    excess,
    rate0: k * excess0,                    // initial cooling rate, K/s
    half: Math.LN2 / k,                    // time to halve the excess temperature
    tau: 1 / k,
    t20: Math.log(5) / k                   // time to fall to 20% of the surplus
  };
}
function initCooling() {
  bind('cooling', () => {
    const T0 = value('cool-t0'), Ta = value('cool-amb'), k = value('cool-k');
    const m = coolingModel(T0, Ta, k, 60);
    out('cooling', 'rate', fmt(m.rate0, 2) + ' K/s');
    out('cooling', 'half', fmt(m.half, 1) + ' s');
    out('cooling', 'tau', fmt(m.tau, 1) + ' s');
    out('cooling', 't20', fmt(m.t20, 1) + ' s');
    out('cooling', 'final', fmt(m.T, 1) + ' °C');
    const left = 80, right = 640, top = 44, bottom = 250;
    const Tmax = Math.max(T0, Ta) + 2, Tmin = Math.min(T0, Ta) - 2;
    const X = (t) => left + t / 240 * (right - left);
    const Y = (T) => bottom - (T - Tmin) / (Tmax - Tmin) * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'temperature (°C)', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'time (s)', 'text-anchor="end"');
    // gridlines and labels
    for (let T = Math.ceil(Tmin / 10) * 10; T <= Tmax; T += 10) {
      b += line(left, Y(T), right, Y(T), '#eef2f7');
      b += text(left - 8, Y(T) + 4, fmt(T, 0), 'text-anchor="end"');
    }
    for (let t = 0; t <= 240; t += 60) {
      b += text(X(t), bottom + 18, fmt(t, 0), 'text-anchor="middle"');
    }
    // ambient line
    b += line(left, Y(Ta), right, Y(Ta), '#059669', 'stroke-dasharray="6 4"');
    b += text(right - 8, Y(Ta) - 8, 'room ' + fmt(Ta, 0) + ' °C', 'text-anchor="end"');
    // the curve
    const pts = [];
    for (let i = 0; i <= 200; i++) {
      const t = 240 * i / 200;
      pts.push([X(t), Y(coolingModel(T0, Ta, k, t).T)]);
    }
    b += path(pts, '#b45309');
    // tangent at t = 0 to show the initial rate
    const slope = (Y(Ta) - Y(T0)) / 240 * m.tau;   // px per second
    if (Math.abs(slope) < 40) {
      b += line(X(0), Y(T0), X(60), Y(T0) + slope * 60, '#94a3b8', 'stroke-dasharray="4 3"');
    }
    b += dot(X(0), Y(T0), 5, '#b45309');
    draw('cooling', b);
    summary('cooling', `Starting at ${fmt(T0, 0)} °C in a room at ${fmt(Ta, 0)} °C, the object cools fastest at first `
      + `(${fmt(m.rate0, 2)} K/s) and then ever more slowly: the surplus over room temperature halves every `
      + `${fmt(m.half, 1)} s. After 60 s it is at ${fmt(m.T, 1)} °C.`);
  });
}
init.cooling = initCooling;
EXPORTS.coolingModel = coolingModel;

/* ---- 03.01 ---- */
/* 03.01 — reading a vernier calliper */
function vernierModel(mainMm, division, zeroErrorMm) {
  const least = 0.1;                       // 1 mm main scale, 10 vernier divisions
  const raw = mainMm + division * least;
  const corrected = raw - zeroErrorMm;
  const unc = Math.abs(zeroErrorMm) > 0 ? Math.max(least, Math.abs(zeroErrorMm) / 10) : least / 2;
  const digits = corrected === 0 ? 1 : Math.floor(Math.log10(Math.abs(corrected))) + 2;
  return { least, raw, corrected, unc, digits, zeroErrorMm };
}
function initVernierReading() {
  bind('vernier-reading', () => {
    const main = value('read-main'), div = value('read-vern'), zero = value('read-zero');
    const m = vernierModel(main, div, zero);
    out('vernier-reading', 'raw', fmt(m.raw, 2) + ' mm');
    out('vernier-reading', 'corrected', fmt(m.corrected, 2) + ' mm');
    out('vernier-reading', 'digits', String(m.digits));
    out('vernier-reading', 'unc', '±' + fmt(m.unc, 2) + ' mm');
    out('vernier-reading', 'verdict', m.corrected < 0 ? 'impossible: the calliper would read a negative length'
      : (Math.abs(zero) > 0.2 ? 'large zero error — recalibrate' : 'consistent'));
    // draw the two scales
    const left = 90, top = 70, px = 42;
    let b = '';
    for (let i = 0; i <= 10; i++) {
      const x = left + i * px;
      b += line(x, top, x, top + 26, '#1e3a8a', 'stroke-width="1.6"');
      b += text(x, top + 42, String(i), 'text-anchor="middle"');
    }
    b += line(left, top + 13, left + 10 * px, top + 13, '#1e3a8a');
    b += text(left, top - 10, 'main scale (mm)', 'text-anchor="start"');
    // vernier: 10 divisions spanning 9 mm, its zero placed at the measured length
    for (let j = 0; j <= 10; j++) {
      const x = left + (m.raw + j * 0.9) * px;
      const hit = j === Math.round(div);
      b += line(x, top + 58, x, hit ? top + 86 : top + 78, hit ? '#b45309' : '#2457c5', 'stroke-width="' + (hit ? 2.4 : 1.6) + '"');
      b += text(x, top + 100, String(j), 'text-anchor="middle" style="font-size:11px"');
    }
    b += text(left, top + 124, 'vernier scale: 10 divisions over 9 mm, its zero at the reading', 'text-anchor="start"');
    b += text(left, top + 148, 'coincidence at division ' + fmt(div, 0) + ' → raw reading ' + fmt(m.raw, 2) + ' mm', 'text-anchor="start" style="font-size:13px"');
    b += text(left, top + 178, 'zero error ' + fmt(zero, 1) + ' mm → true length ' + fmt(m.corrected, 2) + ' mm',
      'text-anchor="start" style="font-size:13px"');
    draw('vernier-reading', b);
    summary('vernier-reading', `The main scale reads ${fmt(main, 1)} mm and vernier division ${fmt(div, 0)} lines up, `
      + `giving a raw reading of ${fmt(m.raw, 2)} mm. Correcting for a zero error of ${fmt(zero, 1)} mm gives `
      + `${fmt(m.corrected, 2)} mm — and the reading is only trustworthy to about ${fmt(m.unc, 2)} mm.`);
  });
}
init['vernier-reading'] = initVernierReading;
EXPORTS.vernierModel = vernierModel;

/* ---- 03.02 ---- */
/* 03.02 — propagation through a power law */
function uncertaintyModel(a, da, n) {
  const f = Math.pow(a, n);
  const df = Math.abs(n) * Math.pow(a, n - 1) * da;       // exact for a power law
  const rel = Math.abs(df / f);
  const digits = rel > 0 ? Math.max(1, Math.floor(-Math.log10(rel)) + 1) : 4;
  return { f, df, rel, digits: Math.min(digits, 6) };
}
function initUncertainty() {
  bind('uncertainty', () => {
    const a = value('unc-a'), da = value('unc-da'), n = value('unc-n');
    const m = uncertaintyModel(a, da, n);
    // round the uncertainty to one significant figure, and the value to match
    const e = Math.floor(Math.log10(m.df));
    const step = Math.pow(10, e);
    const dfq = Math.round(m.df / step) * step;
    const fq = Math.round(m.f / step) * step;
    out('uncertainty', 'f', sci(m.f, 4));
    out('uncertainty', 'df', sci(m.df, 2));
    out('uncertainty', 'rel', (m.rel * 100).toFixed(2) + ' %');
    const dp = Math.max(0, -e);
    out('uncertainty', 'quoted', fq.toFixed(dp) + ' ± ' + dfq.toFixed(dp));
    out('uncertainty', 'digits', String(m.digits));
    // a picture: the curve f = a^n with the uncertainty band on a
    const left = 80, right = 630, top = 50, bottom = 250;
    const amax = Math.max(a * 1.6, a + 3 * da, 1);
    const fmax = Math.pow(amax, n) * 1.05;
    const X = (v) => left + v / amax * (right - left);
    const Y = (v) => bottom - v / fmax * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'f = aⁿ', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'a', 'text-anchor="end"');
    const pts = [];
    for (let i = 0; i <= 160; i++) {
      const x = amax * i / 160;
      pts.push([X(x), Y(Math.pow(x, n))]);
    }
    b += path(pts, '#2457c5');
    // the uncertainty box in a
    b += line(X(a - da), Y(0), X(a - da), Y(Math.pow(a - da, n)), '#b45309', 'stroke-dasharray="4 3"');
    b += line(X(a + da), Y(0), X(a + da), Y(Math.pow(a + da, n)), '#b45309', 'stroke-dasharray="4 3"');
    b += line(X(a - da), Y(Math.pow(a - da, n)), X(a + da), Y(Math.pow(a + da, n)), '#b45309', 'stroke-width="2.4"');
    b += dot(X(a), Y(m.f), 5, '#b45309');
    b += text(X(a) + 8, Y(m.f) - 8, 'f = ' + fmt(m.f, 2) + ' ± ' + fmt(m.df, 2), 'text-anchor="start"');
    b += text(left + 10, bottom - 12, 'a = ' + fmt(a, 2) + ' ± ' + fmt(da, 2), 'text-anchor="start"');
    draw('uncertainty', b);
    summary('uncertainty', `For f = a^${fmt(n, 0)} with a = ${fmt(a, 2)} ± ${fmt(da, 2)}, the relative uncertainty in a `
      + `is ${(100 * da / a).toFixed(1)}%, so the relative uncertainty in f is ${fmt(n, 0)} × that, `
      + `${(m.rel * 100).toFixed(1)}%. Only ${fmt(m.digits, 0)} significant figures of f are justified.`);
  });
}
init.uncertainty = initUncertainty;
EXPORTS.uncertaintyModel = uncertaintyModel;

/* ---- 03.03 ---- */
/* 03.03 — least-squares fitting of a straight line */
function fitModel(m, c, noise, n, seed) {
  const rnd = seeded(seed || 20240501);
  const xs = [], ys = [];
  for (let i = 0; i < n; i++) {
    const x = 0.05 + 0.9 * i / Math.max(1, n - 1);
    // a bell-ish deviation from the sum of three uniforms, scaled by the noise
    const dev = (rnd() + rnd() + rnd() - 1.5) * noise * 1.6;
    xs.push(x);
    ys.push(m * x + c + dev);
  }
  const nn = xs.length;
  const mx = xs.reduce((a, b) => a + b, 0) / nn;
  const my = ys.reduce((a, b) => a + b, 0) / nn;
  let sxy = 0, sxx = 0, syy = 0;
  for (let i = 0; i < nn; i++) {
    sxy += (xs[i] - mx) * (ys[i] - my);
    sxx += (xs[i] - mx) * (xs[i] - mx);
    syy += (ys[i] - my) * (ys[i] - my);
  }
  const slope = sxy / sxx;
  const intercept = my - slope * mx;
  let ssr = 0;
  for (let i = 0; i < nn; i++) ssr += Math.pow(ys[i] - (slope * xs[i] + intercept), 2);
  const r2 = syy > 0 ? 1 - ssr / syy : 1;
  const dm = nn > 2 ? Math.sqrt(ssr / (nn - 2) / sxx) : 0;
  return { xs, ys, slope, intercept, r2, dm, n: nn };
}
function initFit() {
  bind('fit', () => {
    const m = value('fit-slope'), c = value('fit-int'), noise = value('fit-noise'), n = value('fit-n');
    const f = fitModel(m, c, noise, n);
    out('fit', 'm', fmt(f.slope, 3));
    out('fit', 'c', fmt(f.intercept, 3));
    out('fit', 'r2', fmt(f.r2, 4));
    out('fit', 'dm', fmt(f.dm, 3));
    const ok = Math.abs(f.slope - m) < 3 * f.dm + 1e-9;
    out('fit', 'verdict', ok ? 'consistent within 3σ' : 'outside 3σ — unlucky or biased');
    const left = 80, right = 630, top = 44, bottom = 250;
    const X = (x) => left + x * (right - left);
    const ymin = Math.min(...f.ys, 0) - 0.2, ymax = Math.max(...f.ys, m + c) + 0.2;
    const Y = (y) => bottom - (y - ymin) / (ymax - ymin) * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'y', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'x', 'text-anchor="end"');
    // the true line, faint
    b += line(X(0), Y(c), X(1), Y(m + c), '#cbd5e1', 'stroke-dasharray="6 4"');
    // the fitted line
    b += line(X(0), Y(f.intercept), X(1), Y(f.slope + f.intercept), '#b91c1c', 'stroke-width="2.4"');
    for (let i = 0; i < f.n; i++) {
      b += dot(X(f.xs[i]), Y(f.ys[i]), 5, '#2457c5');
      b += line(X(f.xs[i]), Y(f.ys[i]), X(f.xs[i]), Y(f.slope * f.xs[i] + f.intercept), '#f59e0b', 'stroke-dasharray="3 3"');
    }
    b += text(left + 10, bottom - 10, 'dashed grey: true line   red: least-squares fit', 'text-anchor="start"');
    draw('fit', b);
    summary('fit', `Fitted gradient ${fmt(f.slope, 3)} ± ${fmt(f.dm, 3)} against a true ${fmt(m, 3)}, intercept `
      + `${fmt(f.intercept, 2)} against ${fmt(c, 2)}. R² = ${fmt(f.r2, 3)}: with ${fmt(n, 0)} points and this scatter, `
      + `the gradient is determined to about ${fmt(100 * f.dm / Math.max(0.01, Math.abs(f.slope)), 1)}%.`);
  });
}
init.fit = initFit;
EXPORTS.fitModel = fitModel;

/* ---- 04.01 ---- */
/* 04.01 — the quadratic explorer */
function quadModel(a, b, c) {
  if (Math.abs(a) < 1e-6) {
    const root = Math.abs(b) > 1e-6 ? -c / b : NaN;
    return { disc: NaN, nature: 'not a quadratic: a = 0 gives a straight line', x1: root, x2: NaN,
      vx: NaN, vy: NaN, factor: 'no completed-square form' };
  }
  const disc = b * b - 4 * a * c;
  const vx = -b / (2 * a);
  const vy = c - b * b / (4 * a);
  let nature, x1, x2;
  if (Math.abs(disc) < 1e-9) { nature = 'one double root'; x1 = -b / (2 * a); x2 = x1; }
  else if (disc > 0) { nature = 'two distinct real roots'; x1 = (-b + Math.sqrt(disc)) / (2 * a); x2 = (-b - Math.sqrt(disc)) / (2 * a); }
  else { nature = 'no real roots (complex pair)'; x1 = NaN; x2 = NaN; }
  const inner = Math.abs(vx) < 0.005 ? 'x' : (vx > 0 ? `x − ${fmt(vx, 2)}` : `x + ${fmt(-vx, 2)}`);
  const factor = `${fmt(a, 2)}(${inner})² ${vy < 0 ? '−' : '+'} ${fmt(Math.abs(vy), 2)}`;
  return { disc, nature, x1, x2, vx, vy, factor };
}
function initQuad() {
  bind('quad', () => {
    const a = value('quad-a'), b = value('quad-b'), c = value('quad-c');
    const q = quadModel(a, b, c);
    out('quad', 'disc', isFinite(q.disc) ? fmt(q.disc, 2) : 'not defined');
    out('quad', 'nature', q.nature);
    out('quad', 'x1', isFinite(q.x1) ? fmt(q.x1, 3) : 'none');
    out('quad', 'x2', isFinite(q.x2) ? fmt(q.x2, 3) : 'none');
    out('quad', 'vertex', isFinite(q.vx) ? `(${fmt(q.vx, 2)}, ${fmt(q.vy, 2)})` : '—');
    out('quad', 'factor', q.factor);
    const left = 90, right = 630, top = 40, bottom = 250;
    if (!isFinite(q.vx)) {
      let s0 = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
      s0 += line(left, bottom / 2, right, top, '#2457c5', 'stroke-width="2.6"');
      s0 += text(left + 10, top + 14, 'a = 0: a straight line, not a parabola', 'text-anchor="start"');
      draw('quad', s0);
      summary('quad', 'With a = 0 the equation is no longer quadratic: the graph is a straight line and there is at most '
        + 'one root. This is exactly the case the quadratic formula cannot handle.');
      return;
    }
    const X = (x) => left + (x - q.vx + 3) / 6 * (right - left);
    const yA = q.vy - 3, yB = q.vy + 3;
    const Y = (y) => bottom - (y - yA) / (yB - yA) * (bottom - top);
    let s = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    if (yA <= 0 && yB >= 0) s += line(left, Y(0), right, Y(0), '#cbd5e1', 'stroke-dasharray="4 4"');
    let d = '';
    for (let i = 0; i <= 140; i++) {
      const x = q.vx - 3 + 6 * i / 140;
      const y = a * x * x + b * x + c;
      d += `${i ? 'L' : 'M'}${X(x).toFixed(1)},${Y(y).toFixed(1)}`;
    }
    s += `<path d="${d}" fill="none" stroke="#2457c5" stroke-width="2.6"/>`;
    s += line(X(q.vx), top, X(q.vx), bottom, '#94a3b8', 'stroke-dasharray="5 4"');
    if (isFinite(q.x1)) s += dot(X(q.x1), Y(0), 5, '#b91c1c');
    if (isFinite(q.x2)) s += dot(X(q.x2), Y(0), 5, '#b91c1c');
    s += dot(X(q.vx), Y(q.vy), 5.5, '#059669');
    s += text(left + 8, top + 12, 'vertex', 'text-anchor="start"');
    draw('quad', s);
    summary('quad', `a = ${fmt(a, 1)}: the parabola opens ${a > 0 ? 'upwards and has a minimum' : 'downwards and has a maximum'}. `
      + `Discriminant ${fmt(q.disc, 2)} → ${q.nature}. The vertex sits on the axis of symmetry x = ${fmt(q.vx, 2)} `
      + `because it is where the two roots would average out.`);
  });
}
init.quad = initQuad;
EXPORTS.quadModel = quadModel;

/* ---- 04.02 ---- */
/* 04.02 — vector addition, resolving, dot and cross products */
function vecModel(ax, ay, bx, by) {
  const magA = Math.sqrt(ax * ax + ay * ay);
  const magB = Math.sqrt(bx * bx + by * by);
  const sx = ax + bx, sy = ay + by;
  const sum = Math.sqrt(sx * sx + sy * sy);
  const dot = ax * bx + ay * by;
  const cross = Math.abs(ax * by - ay * bx);
  const angle = (magA > 1e-9 && magB > 1e-9)
    ? Math.acos(Math.max(-1, Math.min(1, dot / (magA * magB)))) * 180 / Math.PI
    : NaN;
  return { magA, magB, sx, sy, sum, dot, cross, angle,
    dirA: Math.atan2(ay, ax) * 180 / Math.PI,
    dirSum: Math.atan2(sy, sx) * 180 / Math.PI };
}
function initVector() {
  bind('vector', () => {
    const ax = value('vec-ax'), ay = value('vec-ay'), bx = value('vec-bx'), by = value('vec-by');
    const v = vecModel(ax, ay, bx, by);
    out('vector', 'magA', fmt(v.magA, 2));
    out('vector', 'dirA', `${fmt(v.dirA, 1)}° from east`);
    out('vector', 'magB', fmt(v.magB, 2));
    out('vector', 'sum', `${fmt(v.sum, 2)} at ${fmt(v.dirSum, 1)}°`);
    out('vector', 'angle', isFinite(v.angle) ? `${fmt(v.angle, 1)}°` : 'undefined (a zero vector)');
    out('vector', 'dot', fmt(v.dot, 2));
    out('vector', 'cross', fmt(v.cross, 2));
    const left = 60, right = 620, top = 30, bottom = 280, cx = 340, cy = 155, sc = 22;
    let s = line(left, cy, right, cy, '#cbd5e1') + line(cx, top, cx, bottom, '#cbd5e1');
    for (let k = -8; k <= 8; k += 2) {
      if (!k) continue;
      s += line(cx + k * sc, cy - 3, cx + k * sc, cy + 3, '#94a3b8');
      s += line(cx - 3, cy - k * sc, cx + 3, cy - k * sc, '#94a3b8');
    }
    const P = (x, y) => [cx + x * sc, cy - y * sc];
    const [a1x, a1y] = P(ax, ay), [b1x, b1y] = P(bx, by), [s1x, s1y] = P(v.sx, v.sy);
    // a faint parallelogram
    s += line(a1x, a1y, s1x, s1y, '#c7d2fe', 'stroke-dasharray="5 4"');
    s += line(b1x, b1y, s1x, s1y, '#bbf7d0', 'stroke-dasharray="5 4"');
    s += line(cx, cy, s1x, s1y, '#b91c1c', 'stroke-width="3"');
    s += line(cx, cy, a1x, a1y, '#2457c5', 'stroke-width="2.8"');
    s += line(cx, cy, b1x, b1y, '#059669', 'stroke-width="2.8"');
    s += dot(cx, cy, 4, '#1e3a8a');
    s += dot(a1x, a1y, 5, '#2457c5') + dot(b1x, b1y, 5, '#059669') + dot(s1x, s1y, 5, '#b91c1c');
    s += text(a1x + 8, a1y - 8, 'A', 'text-anchor="start"');
    s += text(b1x + 8, b1y - 8, 'B', 'text-anchor="start"');
    s += text(s1x + 8, s1y - 8, 'A + B', 'text-anchor="start"');
    s += text(left + 6, cy - 8, 'east', 'text-anchor="start"');
    s += text(cx + 8, top + 10, 'north', 'text-anchor="start"');
    draw('vector', s);
    const rel = v.dot > 0 ? 'less than 90° apart, so the resultant is long'
      : v.dot < 0 ? 'more than 90° apart, so the resultant is short'
        : 'exactly perpendicular, so Pythagoras applies directly';
    summary('vector', `The two vectors are ${fmt(v.angle, 1)}° apart — ${rel}. The resultant has length ${fmt(v.sum, 2)} at `
      + `${fmt(v.dirSum, 1)}° from east, while the sum of the lengths is ${fmt(v.magA + v.magB, 2)}: the gap is the angle `
      + `between them. The dot product ${fmt(v.dot, 2)} measures how much of B lies along A.`);
  });
}
init.vector = initVector;
EXPORTS.vecModel = vecModel;

/* ---- 04.03 ---- */
/* 04.03 — displacement, its derivative and its integral */
function calcModel(A, w, t0) {
  const y = A * Math.cos(w * t0);
  const dy = -A * w * Math.sin(w * t0);
  const area = (A / w) * Math.sin(w * t0);
  const peak = A * w;
  const firstMax = w > 1e-9 ? 2 * Math.PI / w : NaN;
  const secondDeriv = -w * w * y;
  return { y, dy, area, peak, firstMax, secondDeriv };
}
function initCalc() {
  bind('calc', () => {
    const A = value('calc-a'), w = value('calc-w'), t0 = value('calc-t0');
    const r = calcModel(A, w, t0);
    out('calc', 'y', fmt(r.y, 3));
    out('calc', 'dy', fmt(r.dy, 3));
    out('calc', 'area', fmt(r.area, 3));
    out('calc', 'peak', fmt(r.peak, 3));
    out('calc', 'when', fmt(r.firstMax, 2) + ' s');
    const left = 70, right = 630, top = 26, bottom = 268, mid = 150;
    const X = (t) => left + t / 12 * (right - left);
    const Y = (v) => mid - v / 1.6 * (bottom - top) * 0.55;
    let s = line(left, mid, right, mid, '#cbd5e1') + line(left, top, left, bottom, '#cbd5e1');
    for (let k = 0; k <= 12; k += 2) s += text(X(k), bottom - 4, String(k), 'text-anchor="middle"');
    s += text(right - 6, mid - 8, 't / s', 'text-anchor="end"');
    let d1 = '', d2 = '', d3 = '';
    for (let i = 0; i <= 240; i++) {
      const t = 12 * i / 240;
      d1 += `${i ? 'L' : 'M'}${X(t).toFixed(1)},${Y(A * Math.cos(w * t)).toFixed(1)}`;
      d2 += `${i ? 'L' : 'M'}${X(t).toFixed(1)},${Y(-A * w * Math.sin(w * t)).toFixed(1)}`;
      d3 += `${i ? 'L' : 'M'}${X(t).toFixed(1)},${Y((A / w) * Math.sin(w * t)).toFixed(1)}`;
    }
    s += `<path d="${d1}" fill="none" stroke="#2457c5" stroke-width="2.6"/>`;
    s += `<path d="${d2}" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="6 4"/>`;
    s += `<path d="${d3}" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="2 4"/>`;
    // the shaded area up to the marker, on a compressed scale
    s += line(X(t0), top, X(t0), bottom, '#94a3b8', 'stroke-dasharray="4 4"');
    s += dot(X(t0), Y(r.y), 5.5, '#b91c1c');
    const slope = -A * w * Math.sin(w * t0);
    const dt = 0.6;
    s += line(X(Math.max(0, t0 - dt)), Y(A * Math.cos(w * t0) - slope * dt), X(Math.min(12, t0 + dt)),
      Y(A * Math.cos(w * t0) + slope * dt), '#b91c1c', 'stroke-width="2"');
    s += text(left + 6, top + 10, 'y (blue), dy/dt (green dashed), area (amber dotted)', 'text-anchor="start"');
    draw('calc', s);
    const where = Math.abs(r.dy) < 0.02 * r.peak ? 'at a turning point, where the gradient is zero'
      : r.y * r.dy > 0 ? 'moving away from the equilibrium, so the displacement is growing'
        : 'moving towards the equilibrium, so the displacement is shrinking';
    summary('calc', `At t = ${fmt(t0, 1)} s the displacement is ${fmt(r.y, 3)} and its gradient is ${fmt(r.dy, 3)} — the `
      + `marker is ${where}. The velocity amplitude is ωA = ${fmt(r.peak, 2)}, while the displacement amplitude is only `
      + `${fmt(A, 2)}: a fast oscillation needs a large velocity even for a small swing.`);
  });
}
init.calc = initCalc;
EXPORTS.calcModel = calcModel;

/* ---- 04.04 ---- */
/* 04.04 — how good is the small-angle approximation? */
function apxModel(x) {
  const sinx = Math.sin(x), tanx = Math.tan(x), cosx = Math.cos(x);
  const err = x - sinx;
  const rel = Math.abs(x) > 1e-12 ? err / sinx : 0;
  const cosapprox = 1 - x * x / 2;
  const cube = x * x * x / 6;
  const coserr = cosapprox - cosx;
  let verdict;
  if (Math.abs(rel) < 0.001) verdict = 'excellent: better than 0.1%';
  else if (Math.abs(rel) < 0.01) verdict = 'good: under 1% error';
  else if (Math.abs(rel) < 0.05) verdict = 'usable if 5% is good enough';
  else verdict = 'too coarse: quote the neglected term instead';
  return { x, sinx, tanx, cosx, err, rel, cosapprox, cube, coserr, verdict };
}
function initApx() {
  bind('apx', () => {
    const x = value('apx-x');
    const r = apxModel(x);
    out('apx', 'sinx', fmt(r.sinx, 4));
    out('apx', 'approx', fmt(x, 4));
    out('apx', 'err', fmt(r.err, 5));
    out('apx', 'rel', fmt(100 * r.rel, 2) + ' %');
    out('apx', 'cosx', fmt(r.cosx, 4));
    out('apx', 'cosapprox', fmt(r.cosapprox, 4));
    out('apx', 'cube', fmt(r.cube, 5));
    out('apx', 'verdict', r.verdict);
    const left = 80, right = 620, top = 30, bottom = 250;
    const X = (a) => left + a / 1.5 * (right - left);
    const Y = (v) => bottom - v / 1.5 * (bottom - top);
    let s = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    s += line(left, Y(0.5), right, Y(0.5), '#eef2fa');
    for (let a = 0.25; a <= 1.25; a += 0.25) s += text(X(a), bottom + 18, a.toFixed(2), 'text-anchor="middle"');
    let d1 = '', d2 = '', d3 = '';
    for (let i = 0; i <= 150; i++) {
      const a = 1.5 * i / 150;
      d1 += `${i ? 'L' : 'M'}${X(a).toFixed(1)},${Y(Math.sin(a)).toFixed(1)}`;
      d3 += `${i ? 'L' : 'M'}${X(a).toFixed(1)},${Y(1 - a * a / 2).toFixed(1)}`;
    }
    s += `<path d="${d1}" fill="none" stroke="#2457c5" stroke-width="2.6"/>`;
    s += `<path d="${d3}" fill="none" stroke="#7c3aed" stroke-width="2.2" stroke-dasharray="6 4"/>`;
    s += line(X(0), Y(0), X(1.5), Y(1.5), '#059669', 'stroke-width="2" stroke-dasharray="7 5"');
    s += line(X(x), top, X(x), bottom, '#94a3b8', 'stroke-dasharray="4 4"');
    s += dot(X(x), Y(r.sinx), 5.5, '#b91c1c');
    s += dot(X(x), Y(x), 4.5, '#059669');
    s += line(X(x), Y(r.sinx), X(x), Y(x), '#f59e0b', 'stroke-width="3"');
    s += text(left + 4, top + 10, 'sin x (blue), x (green), 1 − x²/2 (purple)', 'text-anchor="start"');
    s += text(left + 4, bottom + 40, 'the amber bar is the error you are discarding', 'text-anchor="start"');
    draw('apx', s);
    summary('apx', `At x = ${fmt(x, 2)} rad the approximation sin x ≈ x is wrong by ${fmt(100 * r.rel, 2)}%, while the `
      + `discarded term x³/6 equals ${fmt(r.cube, 4)} — the same size, as the Taylor series promises. `
      + `The verdict is: ${r.verdict}.`);
  });
}
init.apx = initApx;
EXPORTS.apxModel = apxModel;

for (const [key, start] of Object.entries(init)) if ($('plot-' + key)) start();
window.IphoLabs = EXPORTS;
document.documentElement.dataset.iphoReady = 'true';
})();
