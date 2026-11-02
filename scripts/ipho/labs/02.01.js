/* 02.01 — projectile range and time of flight */
function projectileModel(v0, angle, g) {
  const a = angle * D2R, vx = v0 * Math.cos(a), vy = v0 * Math.sin(a);
  const t = 2 * vy / g;
  return { vx, vy, t, range: vx * t, apex: vy * vy / (2 * g), tApex: vy / g };
}
function initProjectile() {
  bind('projectile', () => {
    const v0 = value('proj-v'), ang = value('proj-a'), g = value('proj-g');
    const m = projectileModel(v0, ang, g);
    out('projectile', 'range', fmt(m.range, 2) + ' m');
    out('projectile', 'apex', fmt(m.apex, 2) + ' m');
    out('projectile', 'time', fmt(m.t, 2) + ' s');
    out('projectile', 'vx', fmt(m.vx, 2) + ' m/s');
    const xmax = Math.max(10, projectileModel(v0, 45, g).range * 1.1);
    const ymax = Math.max(5, m.apex * 1.25);
    const X = x => 70 + x / xmax * 560, Y = y => 268 - y / ymax * 210;
    let b = line(70, 268, 640, 268, '#64748b') + line(70, 268, 70, 40, '#64748b');
    b += text(350, 300, 'horizontal distance (m)', 'text-anchor="middle"');
    b += text(20, 40, 'height (m)');
    const pts = [];
    for (let i = 0; i <= 160; i++) {
      const t = m.t * i / 160;
      pts.push([X(m.vx * t), Y(m.vy * t - 0.5 * g * t * t)]);
    }
    b += path(pts, '#2457c5');
    b += dot(X(m.range), 268, 5) + dot(X(m.vx * m.tApex), Y(m.apex), 4, '#059669');
    b += line(X(m.range), 268, X(m.range), 60, '#94a3b8', 'stroke-dasharray="5 4"');
    b += text(X(m.range), 52, fmt(m.range, 1) + ' m', 'text-anchor="middle"');
    draw('projectile', b);
    const pair = 90 - ang;
    summary('projectile', 'Time of flight 2v₀sinθ/g grows with angle, but horizontal speed v₀cosθ falls: the product peaks at 45°. '
      + `At ${fmt(ang, 0)}° the range is ${fmt(m.range, 1)} m; at the complementary ${fmt(pair, 0)}° it is the same (${fmt(projectileModel(v0, pair, g).range, 1)} m).`);
  });
}
init.projectile = initProjectile;
EXPORTS.projectileModel = projectileModel;
