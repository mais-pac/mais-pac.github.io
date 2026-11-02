/* 02.06 — loaded potential divider */
function dividerModel(V, R1, R2, RL) {
  const ideal = V * R2 / (R1 + R2);
  const parallel = RL === 0 ? 0 : (R2 * RL) / (R2 + RL);
  const real = V * parallel / (R1 + parallel);
  const current = V / (R1 + parallel);
  const power = V * current;
  const delivered = (real * real) / (RL || Infinity);
  return { ideal, real, err: ideal === 0 ? 0 : (real - ideal) / ideal, power, delivered, current };
}
function initDivider() {
  bind('divider', () => {
    const m = dividerModel(value('div-v'), value('div-r1'), value('div-r2'), value('div-rl'));
    out('divider', 'ideal', fmt(m.ideal, 3) + ' V');
    out('divider', 'real', fmt(m.real, 3) + ' V');
    out('divider', 'err', fmt(100 * m.err, 1) + ' %');
    out('divider', 'power', fmt(m.power * 1000, 1) + ' mW');
    out('divider', 'eff', fmt(100 * m.delivered / m.power, 1) + ' %');
    let b = axes('load resistance R_L (kΩ, log scale)', 'output voltage (V)');
    const pts = [];
    for (let i = 0; i <= 60; i++) {
      const RL = 1000 * Math.pow(10, i / 60 * 3);
      const mm = dividerModel(value('div-v'), value('div-r1'), value('div-r2'), RL);
      pts.push([60 + i / 60 * 585, 275 - mm.real / value('div-v') * 250]);
    }
    b += path(pts);
    const yIdeal = 275 - m.ideal / value('div-v') * 250;
    b += line(60, yIdeal, 645, yIdeal, '#059669', 'stroke-dasharray="6 4"');
    draw('divider', b);
    summary('divider', `With a heavy load the output sags below the ideal ${fmt(m.ideal, 2)} V: the divider's own Thevenin `
      + `resistance R₁∥R₂ sets how much current it can supply. The error is ${fmt(100 * m.err, 1)}% at R_L = ${fmt(value('div-rl') / 1000, 0)} kΩ.`);
  });
}
init.divider = initDivider;
EXPORTS.dividerModel = dividerModel;
