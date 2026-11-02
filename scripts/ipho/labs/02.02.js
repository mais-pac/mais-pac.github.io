/* 02.02 — ladder equilibrium */
function ladderModel(L, m, angle, muWall, muFloor = 0.45, g = 9.81) {
  const a = angle * D2R, W = m * g;
  // Torque about the foot: the wall reaction Ww acts horizontally at height L sin a (lever arm L sin a),
  // the wall friction mu*Ww acts vertically at horizontal distance L cos a, and the weight
  // acts at horizontal distance (L/2) cos a.  Hence Ww L sin a + muW Ww L cos a = W (L/2) cos a.
  const denom = Math.sin(a) + muWall * Math.cos(a);
  const Ww = denom > 1e-9 ? W * 0.5 * Math.cos(a) / denom : Infinity;
  const fNeeded = Ww, fMax = muFloor * W;
  // Critical angle: Ww = muFloor W  =>  0.5 cos a / (sin a + muW cos a) = muFloor
  // 0.5 cos a = muF sin a + muF muW cos a  =>  tan a = (0.5 - muF muW) / muF
  const k = 0.5 - muFloor * muWall;
  const critical = k > 1e-9 ? Math.atan(k / muFloor) * R2D : 90;
  return { W, Ww, fNeeded, fMax, stable: fNeeded <= fMax, critical, nf: W };
}
function initLadder() {
  bind('ladder', () => {
    const m = ladderModel(value('ladder-l'), value('ladder-m'), value('ladder-a'),
      value('ladder-mu'));
    out('ladder', 'nf', fmt(m.nf, 1) + ' N');
    out('ladder', 'ffloor', fmt(m.fNeeded, 1) + ' N');
    out('ladder', 'fmax', fmt(m.fMax, 1) + ' N');
    out('ladder', 'status', m.stable ? 'holds' : 'slips');
    out('ladder', 'angle', fmt(m.critical, 1) + '°');
    let b = line(80, 260, 640, 260, '#64748b') + line(80, 260, 80, 40, '#64748b');
    const L = value('ladder-l'), ang = value('ladder-a') * D2R;
    const px = x => 80 + x / (L * 1.15) * 520, py = y => 260 - y / (L * 1.15) * 210;
    b += text(350, 300, 'horizontal distance (m)', 'text-anchor="middle"');
    b += text(20, 40, 'height (m)');
    b += `<line x1="${px(0)}" y1="${py(0)}" x2="${px(L * Math.cos(ang))}" y2="${py(L * Math.sin(ang))}" stroke="#2457c5" stroke-width="5"/>`;
    b += dot(px(0), py(0), 6, '#1e3a8a');
    b += dot(px(L * Math.cos(ang)), py(L * Math.sin(ang)), 6, '#1e3a8a');
    b += `<line x1="${px(0)}" y1="${py(0)}" x2="${px(0.35)}" y2="${py(0.35 * Math.tan(ang))}" stroke="#b45309" stroke-width="3" stroke-dasharray="5 4"/>`;
    b += text(px(0.38), py(0.38 * Math.tan(ang)), 'friction', 'text-anchor="start"');
    draw('ladder', b);
    summary('ladder', m.stable
      ? `Friction needed ${fmt(m.fNeeded, 0)} N is below the ${fmt(m.fMax, 0)} N available, so the ladder holds. The critical angle is ${fmt(m.critical, 1)}°: below it the required friction exceeds the limit.`
      : `Friction needed ${fmt(m.fNeeded, 0)} N exceeds the ${fmt(m.fMax, 0)} N available, so the ladder slips. The critical angle is ${fmt(m.critical, 1)}°.`);
  });
}
init.ladder = initLadder;
EXPORTS.ladderModel = ladderModel;
