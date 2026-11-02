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
