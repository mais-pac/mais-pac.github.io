/* 02.16 — Newton's law of cooling */
function coolingModel(T0, Tamb, k, t) {
  const excess0 = T0 - Tamb;
  const excess = excess0 * Math.exp(-k * t);
  return {
    T: Tamb + excess,
    excess,
    rate0: k * excess0,                    // initial cooling rate, K/s
    half: Math.LN2 / k,                    // time to halve the excess temperature
    tau: 1 / k,
    t20: Math.log(5) / k                   // time to fall to 20% of the surplus
  };
}
function initCooling() {
  bind('cooling', () => {
    const T0 = value('cool-t0'), Ta = value('cool-amb'), k = value('cool-k');
    const m = coolingModel(T0, Ta, k, 60);
    out('cooling', 'rate', fmt(m.rate0, 2) + ' K/s');
    out('cooling', 'half', fmt(m.half, 1) + ' s');
    out('cooling', 'tau', fmt(m.tau, 1) + ' s');
    out('cooling', 't20', fmt(m.t20, 1) + ' s');
    out('cooling', 'final', fmt(m.T, 1) + ' °C');
    const left = 80, right = 640, top = 44, bottom = 250;
    const Tmax = Math.max(T0, Ta) + 2, Tmin = Math.min(T0, Ta) - 2;
    const X = (t) => left + t / 240 * (right - left);
    const Y = (T) => bottom - (T - Tmin) / (Tmax - Tmin) * (bottom - top);
    let b = line(left, bottom, right, bottom, '#64748b') + line(left, top, left, bottom, '#64748b');
    b += text(left + 6, top + 6, 'temperature (°C)', 'text-anchor="start"');
    b += text(right - 6, bottom + 20, 'time (s)', 'text-anchor="end"');
    // gridlines and labels
    for (let T = Math.ceil(Tmin / 10) * 10; T <= Tmax; T += 10) {
      b += line(left, Y(T), right, Y(T), '#eef2f7');
      b += text(left - 8, Y(T) + 4, fmt(T, 0), 'text-anchor="end"');
    }
    for (let t = 0; t <= 240; t += 60) {
      b += text(X(t), bottom + 18, fmt(t, 0), 'text-anchor="middle"');
    }
    // ambient line
    b += line(left, Y(Ta), right, Y(Ta), '#059669', 'stroke-dasharray="6 4"');
    b += text(right - 8, Y(Ta) - 8, 'room ' + fmt(Ta, 0) + ' °C', 'text-anchor="end"');
    // the curve
    const pts = [];
    for (let i = 0; i <= 200; i++) {
      const t = 240 * i / 200;
      pts.push([X(t), Y(coolingModel(T0, Ta, k, t).T)]);
    }
    b += path(pts, '#b45309');
    // tangent at t = 0 to show the initial rate
    const slope = (Y(Ta) - Y(T0)) / 240 * m.tau;   // px per second
    if (Math.abs(slope) < 40) {
      b += line(X(0), Y(T0), X(60), Y(T0) + slope * 60, '#94a3b8', 'stroke-dasharray="4 3"');
    }
    b += dot(X(0), Y(T0), 5, '#b45309');
    draw('cooling', b);
    summary('cooling', `Starting at ${fmt(T0, 0)} °C in a room at ${fmt(Ta, 0)} °C, the object cools fastest at first `
      + `(${fmt(m.rate0, 2)} K/s) and then ever more slowly: the surplus over room temperature halves every `
      + `${fmt(m.half, 1)} s. After 60 s it is at ${fmt(m.T, 1)} °C.`);
  });
}
init.cooling = initCooling;
EXPORTS.coolingModel = coolingModel;
