/* 02.03 — one-dimensional collisions with restitution e */
function collisionModel(m1, v1, m2, v2, e) {
  const p = m1 * v1 + m2 * v2, M = m1 + m2;
  const vcm = p / M;
  // Relative velocity reverses and shrinks by e.
  const uRel = v1 - v2;
  // The relative velocity reverses and shrinks by e: v1f - v2f = -e (v1 - v2).
  const v1f = vcm - (m2 / M) * e * uRel;
  const v2f = vcm + (m1 / M) * e * uRel;
  const keIn = 0.5 * m1 * v1 * v1 + 0.5 * m2 * v2 * v2;
  const keOut = 0.5 * m1 * v1f * v1f + 0.5 * m2 * v2f * v2f;
  return { v1f, v2f, keIn, keOut, lost: keIn - keOut, p, vcm, pf: m1 * v1f + m2 * v2f };
}
function initCollision() {
  bind('collision', () => {
    const eKey = $('col-type').value;
    const e = eKey === 'elastic' ? 1 : eKey === 'inelastic' ? 0 : 0.5;
    const m = collisionModel(value('col-m1'), value('col-v1'), value('col-m2'), value('col-v2'), e);
    out('collision', 'v1f', fmt(m.v1f, 2) + ' m/s');
    out('collision', 'v2f', fmt(m.v2f, 2) + ' m/s');
    out('collision', 'pf', fmt(m.pf, 2) + ' kg m/s');
    out('collision', 'ke', fmt(m.lost, 2) + ' J of ' + fmt(m.keIn, 2) + ' J');
    out('collision', 'com', fmt(m.vcm, 2) + ' m/s');
    const X = t => 340 + t * 62;
    let b = line(60, 190, 640, 190, '#64748b');
    b += text(340, 300, 'position (arbitrary units)', 'text-anchor="middle"');
    b += text(340, 34, 'before and after: the centre of mass moves at a constant speed', 'text-anchor="middle"');
    b += dot(X(-1.6), 170, 4 + 5 * value('col-m1'), '#2457c5');
    b += dot(X(0.6), 210, 4 + 5 * value('col-m2'), '#7c3aed');
    b += dot(X(-1.6 + 2.2 * 0), 120, 6, '#94a3b8');
    b += `<line x1="${X(-2.4)}" y1="120" x2="${X(2.4)}" y2="120" stroke="#cbd5e1" stroke-dasharray="5 4"/>`;
    b += text(X(-2.4) + 4, 108, 'centre of mass track', 'text-anchor="start"');
    const arrowAt = (t, y, v, col) => {
      const len = clamp(Math.abs(v) * 16, 0, 90) * Math.sign(v || 1);
      return `<line x1="${X(t)}" y1="${y}" x2="${X(t) + len}" y2="${y}" stroke="${col}" stroke-width="3"/>`;
    };
    b += arrowAt(-1.6, 152, value('col-v1'), '#2457c5');
    b += arrowAt(0.6, 232, value('col-v2'), '#7c3aed');
    b += text(X(-1.6), 140, 'v₁', 'text-anchor="middle"');
    b += text(X(0.6), 250, 'v₂', 'text-anchor="middle"');
    draw('collision', b);
    summary('collision', e === 1
      ? `Perfectly elastic: momentum ${fmt(m.pf, 2)} kg m/s is conserved and the kinetic energy loss is ${fmt(m.lost, 3)} J — zero, as it must be.`
      : `Momentum is still conserved (${fmt(m.pf, 2)} kg m/s) but ${fmt(m.lost, 2)} J of kinetic energy has gone into deformation and heat. In the centre-of-mass frame the total momentum is always zero, however the collision ends.`);
  });
}
init.collision = initCollision;
EXPORTS.collisionModel = collisionModel;
