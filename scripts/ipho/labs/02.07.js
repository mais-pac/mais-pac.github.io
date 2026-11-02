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
