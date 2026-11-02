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
