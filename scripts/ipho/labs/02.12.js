/* 02.12 — relativistic travel */
function relativityModel(beta, lightYears, mass) {
  const c = 299792458, yr = 3.15576e7;
  const g = 1 / Math.sqrt(1 - beta * beta);
  const labTime = lightYears / beta;              // years, since distance is in light years
  const properTime = labTime / g;                 // traveller's clock
  const length = lightYears / g;                  // contracted distance in the traveller's frame
  const energy = (g - 1) * mass * c * c;          // joules
  const momentum = g * mass * beta * c;
  return { g, labTime, properTime, length, energy, momentum, beta };
}
function initRelativity() {
  bind('relativity', () => {
    const b = value('rel-b'), d = value('rel-d'), m0 = value('rel-m');
    const m = relativityModel(Math.min(b, 0.9999), d, m0);
    out('relativity', 'gamma', fmt(m.g, 4));
    out('relativity', 'clock', fmt(m.properTime, 3) + ' yr');
    out('relativity', 'length', fmt(m.length, 3) + ' ly');
    out('relativity', 'energy', sci(m.energy, 3) + ' J');
    out('relativity', 'mass', sci(m.g * m0, 3) + ' kg equivalent');
    const left = 70, right = 640, top = 40, bottom = 250;
    let s = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    s += text(left + 6, top + 6, 'lab time (years)', 'text-anchor="start"');
    s += text(right - 6, bottom + 24, 'distance (light years)', 'text-anchor="end"');
    // mark the traveller's clock at evenly spaced lab times
    const xmax = Math.max(1, d);
    const X = (x) => left + (x / xmax) * (right - left);
    const Y = (t) => bottom - Math.min(1, t / Math.max(1, d / Math.max(0.05, b))) * (bottom - top);
    s += path([[X(0), Y(0)], [X(xmax), Y(xmax / Math.max(0.05, b))]], '#2457c5');
    for (let i = 0; i <= 5; i++) {
      const x = xmax * i / 5, tLab = x / Math.max(0.05, b), tProp = tLab / m.g;
      if (tLab / Math.max(1, d / Math.max(0.05, b)) <= 1) {
        s += dot(X(x), Y(tLab), 4, '#b45309');
        if (i > 0) s += text(X(x) + 6, Y(tLab) - 6, fmt(tProp, 1) + ' yr aboard');
      }
    }
    s += text(left + 10, top + 24, 'one dot = a year on the traveller’s clock', 'text-anchor="start"');
    draw('relativity', s);
    summary('relativity', `At ${fmt(b, 3)}c the Lorentz factor is ${fmt(m.g, 3)}: ten light years take `
      + `${fmt(m.labTime, 1)} years measured from Earth but only ${fmt(m.properTime, 1)} years on the traveller's clock. `
      + `The journey is ${fmt(m.length, 1)} light years long in the traveller's frame, and the kinetic energy is `
      + `${sci(m.energy, 2)} J — it is the energy cost, not the speed limit in principle, that makes relativistic travel hard.`);
  });
}
init.relativity = initRelativity;
EXPORTS.relativityModel = relativityModel;
