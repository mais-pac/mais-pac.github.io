/* 02.14 — radioactive decay of a finite sample */
function decayModel(halfLife, N0, t) {
  const lambda = Math.LN2 / halfLife;
  const left = N0 * Math.pow(0.5, t / halfLife);
  const A = lambda * left;                  // decays per second for the nuclei remaining
  return { lambda, left, frac: left / N0, A, tau: 1 / lambda, halfLife };
}
function initDecay() {
  bind('decay', () => {
    const half = value('dec-h'), N0 = value('dec-n'), t = value('dec-t');
    const m = decayModel(half, N0, t);
    out('decay', 'left', fmt(Math.round(m.left), 0));
    out('decay', 'frac', fmt(m.frac * 100, 1) + ' %');
    out('decay', 'A', fmt(m.A, 1) + ' Bq');
    out('decay', 'lambda', fmt(m.lambda, 4) + ' /s');
    out('decay', 'tau', fmt(m.tau, 3) + ' s');
    const left = 70, right = 640, top = 40, bottom = 250;
    const T = Math.max(3 * half, t * 1.2);
    const X = (x) => left + x / T * (right - left);
    const Y = (f) => bottom - f * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'nuclei remaining', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'time (s)', 'text-anchor="end"');
    // exact exponential
    const pts = [];
    for (let i = 0; i <= 200; i++) {
      const x = T * i / 200;
      pts.push([X(x), Y(Math.pow(0.5, x / half))]);
    }
    b += path(pts, '#2457c5');
    // half-life markers
    for (let k = 1; k <= 3; k++) {
      const x = k * half;
      if (x <= T) {
        b += line(X(x), top, X(x), bottom, '#e2e8f0', 'stroke-dasharray="4 4"');
        b += text(X(x) + 4, Y(Math.pow(0.5, k)) - 4, '½^' + k, 'text-anchor="start"');
      }
    }
    // simulated finite sample: random but seeded, so it is reproducible
    const rnd = seeded(12345);
    let alive = N0;
    const sim = [[X(0), Y(1)]];
    const steps = 160;
    const p = 1 - Math.pow(0.5, T / half / steps);
    for (let i = 1; i <= steps; i++) {
      for (let n = 0; n < alive; n++) if (rnd() < p) alive--;
      sim.push([X(i * T / steps), Y(alive / N0)]);
    }
    b += path(sim, '#059669', 'stroke-dasharray="3 3" stroke-width="1.6"');
    b += dot(X(t), Y(m.frac), 6, '#b45309');
    b += text(left + 14, top + 26, 'smooth curve: N = N₀·2^(−t/T½)', 'text-anchor="start"');
    b += text(left + 14, top + 44, 'jagged line: one random sample of ' + fmt(N0, 0) + ' nuclei', 'text-anchor="start"');
    draw('decay', b);
    summary('decay', `After ${fmt(t, 1)} s (${fmt(t / half, 2)} half-lives) about ${fmt(m.frac * 100, 1)}% of the nuclei `
      + `remain, and the activity is ${fmt(m.A, 1)} decays per second. With only ${fmt(N0, 0)} nuclei the actual decay `
      + `is visibly random; with 10²³ nuclei the statistical jitter is far too small to see.`);
  });
}
init.decay = initDecay;
EXPORTS.decayModel = decayModel;
