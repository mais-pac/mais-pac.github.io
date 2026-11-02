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
