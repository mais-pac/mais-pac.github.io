/* 03.03 — least-squares fitting of a straight line */
function fitModel(m, c, noise, n, seed) {
  const rnd = seeded(seed || 20240501);
  const xs = [], ys = [];
  for (let i = 0; i < n; i++) {
    const x = 0.05 + 0.9 * i / Math.max(1, n - 1);
    // a bell-ish deviation from the sum of three uniforms, scaled by the noise
    const dev = (rnd() + rnd() + rnd() - 1.5) * noise * 1.6;
    xs.push(x);
    ys.push(m * x + c + dev);
  }
  const nn = xs.length;
  const mx = xs.reduce((a, b) => a + b, 0) / nn;
  const my = ys.reduce((a, b) => a + b, 0) / nn;
  let sxy = 0, sxx = 0, syy = 0;
  for (let i = 0; i < nn; i++) {
    sxy += (xs[i] - mx) * (ys[i] - my);
    sxx += (xs[i] - mx) * (xs[i] - mx);
    syy += (ys[i] - my) * (ys[i] - my);
  }
  const slope = sxy / sxx;
  const intercept = my - slope * mx;
  let ssr = 0;
  for (let i = 0; i < nn; i++) ssr += Math.pow(ys[i] - (slope * xs[i] + intercept), 2);
  const r2 = syy > 0 ? 1 - ssr / syy : 1;
  const dm = nn > 2 ? Math.sqrt(ssr / (nn - 2) / sxx) : 0;
  return { xs, ys, slope, intercept, r2, dm, n: nn };
}
function initFit() {
  bind('fit', () => {
    const m = value('fit-slope'), c = value('fit-int'), noise = value('fit-noise'), n = value('fit-n');
    const f = fitModel(m, c, noise, n);
    out('fit', 'm', fmt(f.slope, 3));
    out('fit', 'c', fmt(f.intercept, 3));
    out('fit', 'r2', fmt(f.r2, 4));
    out('fit', 'dm', fmt(f.dm, 3));
    const ok = Math.abs(f.slope - m) < 3 * f.dm + 1e-9;
    out('fit', 'verdict', ok ? 'consistent within 3σ' : 'outside 3σ — unlucky or biased');
    const left = 80, right = 630, top = 44, bottom = 250;
    const X = (x) => left + x * (right - left);
    const ymin = Math.min(...f.ys, 0) - 0.2, ymax = Math.max(...f.ys, m + c) + 0.2;
    const Y = (y) => bottom - (y - ymin) / (ymax - ymin) * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'y', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'x', 'text-anchor="end"');
    // the true line, faint
    b += line(X(0), Y(c), X(1), Y(m + c), '#cbd5e1', 'stroke-dasharray="6 4"');
    // the fitted line
    b += line(X(0), Y(f.intercept), X(1), Y(f.slope + f.intercept), '#b91c1c', 'stroke-width="2.4"');
    for (let i = 0; i < f.n; i++) {
      b += dot(X(f.xs[i]), Y(f.ys[i]), 5, '#2457c5');
      b += line(X(f.xs[i]), Y(f.ys[i]), X(f.xs[i]), Y(f.slope * f.xs[i] + f.intercept), '#f59e0b', 'stroke-dasharray="3 3"');
    }
    b += text(left + 10, bottom - 10, 'dashed grey: true line   red: least-squares fit', 'text-anchor="start"');
    draw('fit', b);
    summary('fit', `Fitted gradient ${fmt(f.slope, 3)} ± ${fmt(f.dm, 3)} against a true ${fmt(m, 3)}, intercept `
      + `${fmt(f.intercept, 2)} against ${fmt(c, 2)}. R² = ${fmt(f.r2, 3)}: with ${fmt(n, 0)} points and this scatter, `
      + `the gradient is determined to about ${fmt(100 * f.dm / Math.max(0.01, Math.abs(f.slope)), 1)}%.`);
  });
}
init.fit = initFit;
EXPORTS.fitModel = fitModel;
