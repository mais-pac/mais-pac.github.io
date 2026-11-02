/* 03.01 — reading a vernier calliper */
function vernierModel(mainMm, division, zeroErrorMm) {
  const least = 0.1;                       // 1 mm main scale, 10 vernier divisions
  const raw = mainMm + division * least;
  const corrected = raw - zeroErrorMm;
  const unc = Math.abs(zeroErrorMm) > 0 ? Math.max(least, Math.abs(zeroErrorMm) / 10) : least / 2;
  const digits = corrected === 0 ? 1 : Math.floor(Math.log10(Math.abs(corrected))) + 2;
  return { least, raw, corrected, unc, digits, zeroErrorMm };
}
function initVernierReading() {
  bind('vernier-reading', () => {
    const main = value('read-main'), div = value('read-vern'), zero = value('read-zero');
    const m = vernierModel(main, div, zero);
    out('vernier-reading', 'raw', fmt(m.raw, 2) + ' mm');
    out('vernier-reading', 'corrected', fmt(m.corrected, 2) + ' mm');
    out('vernier-reading', 'digits', String(m.digits));
    out('vernier-reading', 'unc', '±' + fmt(m.unc, 2) + ' mm');
    out('vernier-reading', 'verdict', m.corrected < 0 ? 'impossible: the calliper would read a negative length'
      : (Math.abs(zero) > 0.2 ? 'large zero error — recalibrate' : 'consistent'));
    // draw the two scales
    const left = 90, top = 70, px = 42;
    let b = '';
    for (let i = 0; i <= 10; i++) {
      const x = left + i * px;
      b += line(x, top, x, top + 26, '#1e3a8a', 'stroke-width="1.6"');
      b += text(x, top + 42, String(i), 'text-anchor="middle"');
    }
    b += line(left, top + 13, left + 10 * px, top + 13, '#1e3a8a');
    b += text(left, top - 10, 'main scale (mm)', 'text-anchor="start"');
    // vernier: 10 divisions spanning 9 mm, its zero placed at the measured length
    for (let j = 0; j <= 10; j++) {
      const x = left + (m.raw + j * 0.9) * px;
      const hit = j === Math.round(div);
      b += line(x, top + 58, x, hit ? top + 86 : top + 78, hit ? '#b45309' : '#2457c5', 'stroke-width="' + (hit ? 2.4 : 1.6) + '"');
      b += text(x, top + 100, String(j), 'text-anchor="middle" style="font-size:11px"');
    }
    b += text(left, top + 124, 'vernier scale: 10 divisions over 9 mm, its zero at the reading', 'text-anchor="start"');
    b += text(left, top + 148, 'coincidence at division ' + fmt(div, 0) + ' → raw reading ' + fmt(m.raw, 2) + ' mm', 'text-anchor="start" style="font-size:13px"');
    b += text(left, top + 178, 'zero error ' + fmt(zero, 1) + ' mm → true length ' + fmt(m.corrected, 2) + ' mm',
      'text-anchor="start" style="font-size:13px"');
    draw('vernier-reading', b);
    summary('vernier-reading', `The main scale reads ${fmt(main, 1)} mm and vernier division ${fmt(div, 0)} lines up, `
      + `giving a raw reading of ${fmt(m.raw, 2)} mm. Correcting for a zero error of ${fmt(zero, 1)} mm gives `
      + `${fmt(m.corrected, 2)} mm — and the reading is only trustworthy to about ${fmt(m.unc, 2)} mm.`);
  });
}
init['vernier-reading'] = initVernierReading;
EXPORTS.vernierModel = vernierModel;
