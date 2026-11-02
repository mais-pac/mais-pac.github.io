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
