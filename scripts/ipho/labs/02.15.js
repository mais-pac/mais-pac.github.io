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
