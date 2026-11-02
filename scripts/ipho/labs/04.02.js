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
