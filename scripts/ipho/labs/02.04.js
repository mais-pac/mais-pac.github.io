/* 02.04 — orbit geometry and vis-viva speed */
function orbitModel(a, e, nu, mu = 398600.4418, R = 6371) {
  const p = a * (1 - e * e);
  const r = p / (1 + e * Math.cos(nu * D2R));
  const v = Math.sqrt(mu * (2 / r - 1 / a));
  const rp = a * (1 - e), ra = a * (1 + e);
  const vp = Math.sqrt(mu * (2 / rp - 1 / a)), va = Math.sqrt(mu * (2 / ra - 1 / a));
  const T = 2 * Math.PI * Math.sqrt(a ** 3 / mu);
  return { r, v, rp, ra, vp, va, T, p };
}
function initOrbit() {
  bind('orbit', () => {
    const a = value('orbit-r') * 6371, e = value('orbit-e'), nu = value('orbit-nu');
    const m = orbitModel(a, e, nu);
    out('orbit', 'r', fmt(m.r / 6371, 2) + ' R⊕');
    out('orbit', 'v', fmt(m.v, 3) + ' km/s');
    out('orbit', 'peri', fmt(m.vp, 3) + ' km/s');
    out('orbit', 'apo', fmt(m.va, 3) + ' km/s');
    out('orbit', 'T', fmt(m.T / 60, 1) + ' min');
    const b = a * Math.sqrt(1 - e * e);
    const X = x => 340 + x / (a * 1.3) * 260, Y = y => 165 + y / (a * 1.3) * 260;
    let g = `<ellipse cx="340" cy="165" rx="${a / (a * 1.3) * 260}" ry="${b / (a * 1.3) * 260}" fill="none" stroke="#2457c5" stroke-width="2.4"/>`;
    g += `<circle cx="${X(-a * e)}" cy="165" r="10" fill="#b45309"/>`;
    g += `<circle cx="${X(a * (1 - e * e) / (1 + e * Math.cos(nu * D2R)) * Math.cos(nu * D2R) - a * e)}" cy="${Y(a * (1 - e * e) / (1 + e * Math.cos(nu * D2R)) * Math.sin(nu * D2R))}" r="6" fill="#059669"/>`;
    g += text(340, 320, 'central body at the occupied focus; the empty focus is a geometric point', 'text-anchor="middle"');
    g += text(340, 26, 'a = ' + fmt(value('orbit-r'), 1) + ' R⊕, e = ' + fmt(e, 2) + ', ν = ' + fmt(nu, 0) + '°', 'text-anchor="middle"');
    draw('orbit', g);
    summary('orbit', 'The vis-viva equation gives the speed at every point; the body is fastest at periapsis and slowest at apoapsis. '
      + `Here the speed ranges from ${fmt(m.vp, 2)} to ${fmt(m.va, 2)} km/s. Kepler's second law is the statement that the radius vector sweeps equal areas in equal times, so a shorter radius means a larger speed.`);
  });
}
init.orbit = initOrbit;
EXPORTS.orbitModel = orbitModel;
