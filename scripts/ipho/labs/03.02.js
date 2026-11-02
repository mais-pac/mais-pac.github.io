/* 03.02 — propagation through a power law */
function uncertaintyModel(a, da, n) {
  const f = Math.pow(a, n);
  const df = Math.abs(n) * Math.pow(a, n - 1) * da;       // exact for a power law
  const rel = Math.abs(df / f);
  const digits = rel > 0 ? Math.max(1, Math.floor(-Math.log10(rel)) + 1) : 4;
  return { f, df, rel, digits: Math.min(digits, 6) };
}
function initUncertainty() {
  bind('uncertainty', () => {
    const a = value('unc-a'), da = value('unc-da'), n = value('unc-n');
    const m = uncertaintyModel(a, da, n);
    // round the uncertainty to one significant figure, and the value to match
    const e = Math.floor(Math.log10(m.df));
    const step = Math.pow(10, e);
    const dfq = Math.round(m.df / step) * step;
    const fq = Math.round(m.f / step) * step;
    out('uncertainty', 'f', sci(m.f, 4));
    out('uncertainty', 'df', sci(m.df, 2));
    out('uncertainty', 'rel', (m.rel * 100).toFixed(2) + ' %');
    const dp = Math.max(0, -e);
    out('uncertainty', 'quoted', fq.toFixed(dp) + ' ± ' + dfq.toFixed(dp));
    out('uncertainty', 'digits', String(m.digits));
    // a picture: the curve f = a^n with the uncertainty band on a
    const left = 80, right = 630, top = 50, bottom = 250;
    const amax = Math.max(a * 1.6, a + 3 * da, 1);
    const fmax = Math.pow(amax, n) * 1.05;
    const X = (v) => left + v / amax * (right - left);
    const Y = (v) => bottom - v / fmax * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'f = aⁿ', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'a', 'text-anchor="end"');
    const pts = [];
    for (let i = 0; i <= 160; i++) {
      const x = amax * i / 160;
      pts.push([X(x), Y(Math.pow(x, n))]);
    }
    b += path(pts, '#2457c5');
    // the uncertainty box in a
    b += line(X(a - da), Y(0), X(a - da), Y(Math.pow(a - da, n)), '#b45309', 'stroke-dasharray="4 3"');
    b += line(X(a + da), Y(0), X(a + da), Y(Math.pow(a + da, n)), '#b45309', 'stroke-dasharray="4 3"');
    b += line(X(a - da), Y(Math.pow(a - da, n)), X(a + da), Y(Math.pow(a + da, n)), '#b45309', 'stroke-width="2.4"');
    b += dot(X(a), Y(m.f), 5, '#b45309');
    b += text(X(a) + 8, Y(m.f) - 8, 'f = ' + fmt(m.f, 2) + ' ± ' + fmt(m.df, 2), 'text-anchor="start"');
    b += text(left + 10, bottom - 12, 'a = ' + fmt(a, 2) + ' ± ' + fmt(da, 2), 'text-anchor="start"');
    draw('uncertainty', b);
    summary('uncertainty', `For f = a^${fmt(n, 0)} with a = ${fmt(a, 2)} ± ${fmt(da, 2)}, the relative uncertainty in a `
      + `is ${(100 * da / a).toFixed(1)}%, so the relative uncertainty in f is ${fmt(n, 0)} × that, `
      + `${(m.rel * 100).toFixed(1)}%. Only ${fmt(m.digits, 0)} significant figures of f are justified.`);
  });
}
init.uncertainty = initUncertainty;
EXPORTS.uncertaintyModel = uncertaintyModel;
