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
