/* 02.05 — Torricelli jet from a tank */
function torricelliModel(h, H, d, g = 9.81, rho = 1000) {
  const A = Math.PI * (d / 2000) ** 2;       // m²
  const v = Math.sqrt(2 * g * h);
  const Q = A * v;                            // m³/s
  const t = (v * v) / (2 * g);                // fall time from the hole at height H
  const range = v * Math.sqrt(2 * Math.max(H, 0) / g);
  const empty = Q > 0 ? (1.0 * A) / Q : Infinity; // placeholder tank volume = A_tank*h with A_tank = 1 m² reference
  return { v, Q, range, t, empty };
}
function initTorricelli() {
  bind('torricelli', () => {
    const m = torricelliModel(value('tor-h'), value('tor-H'), value('tor-d'));
    out('torricelli', 'v', fmt(m.v, 2) + ' m/s');
    out('torricelli', 'range', fmt(m.range, 2) + ' m');
    out('torricelli', 'flow', sci(m.Q, 2) + ' m³/s');
    out('torricelli', 'time', Number.isFinite(m.empty) ? fmt(m.empty / 60, 1) + ' min*' : '—');
    let b = line(60, 270, 640, 270, '#64748b');
    const h = value('tor-h'), H = value('tor-H'), d = value('tor-d');
    const scale = 200 / Math.max(2, h + H);
    const tankTop = 270 - (h + H) * scale, holeY = 270 - H * scale;
    b += `<rect x="120" y="${tankTop}" width="120" height="${(h + H) * scale}" fill="#dbeafe" stroke="#2457c5" stroke-width="2"/>`;
    b += `<rect x="120" y="${holeY}" width="120" height="${h * scale}" fill="#93c5fd"/>`;
    b += `<circle cx="242" cy="${holeY}" r="${Math.max(2, d / 2)}" fill="#1e3a8a"/>`;
    // jet parabola
    const pts = [];
    for (let i = 0; i <= 60; i++) {
      const t = (m.t * i / 60);
      pts.push([242 + m.v * t * 18, holeY + 0.5 * 9.81 * t * t * 18]);
    }
    b += path(pts, '#059669');
    b += text(340, 40, 'jet from a hole of diameter ' + d + ' mm', 'text-anchor="middle"');
    b += text(340, 300, 'tank drawn to scale; time marked * assumes a 1 m² tank section', 'text-anchor="middle"');
    draw('torricelli', b);
    summary('torricelli', 'Torricelli’s law gives v = √(2gh): the speed depends only on the depth, not on the hole size. '
      + 'A bigger hole gives more volume per second but the same speed, and the jet falls as a projectile, so the horizontal range is v√(2H/g).');
  });
}
init.torricelli = initTorricelli;
EXPORTS.torricelliModel = torricelliModel;
