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
