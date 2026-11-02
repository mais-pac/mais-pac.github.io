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
