/* 02.11 — the thin lens, with a ray diagram drawn to scale */
function lensModel(f, u, h) {
  // all lengths in cm; real-is-positive convention for a converging lens
  const inv = 1 / f - 1 / u;
  const v = Math.abs(inv) < 1e-9 ? Infinity : 1 / inv;
  const m = Number.isFinite(v) ? -v / u : -Infinity;
  const real = Number.isFinite(v) && v > 0;
  return { v, m, real, hi: m * h, power: 100 / f, vertex: 0 };
}
function initThinLens() {
  bind('thin-lens', () => {
    const f = value('lens-f'), u = value('lens-u'), h = value('lens-h');
    const m = lensModel(f, u, h);
    out('thin-lens', 'v', Number.isFinite(m.v) ? fmt(m.v, 1) + ' cm' : 'at infinity');
    out('thin-lens', 'm', fmt(m.m, 2));
    out('thin-lens', 'type', m.real ? (Math.abs(m.m) > 1 ? 'real, magnified, inverted' : 'real, diminished, inverted')
      : 'virtual, upright');
    out('thin-lens', 'hi', fmt(Math.abs(m.hi), 2) + ' cm');
    out('thin-lens', 'power', fmt(m.power, 2) + ' D');
    // geometry: put the lens at x = 430, 1 cm = 3.2 px
    const sx = 3.2, lx = 430, axis = 150;
    let b = line(40, axis, 660, axis, '#cbd5e1', 'stroke-dasharray="6 4"');
    b += `<path d="M${lx},${axis - 95} Q${lx + 34},${axis} ${lx},${axis + 95} Q${lx - 34},${axis} ${lx},${axis - 95} Z" fill="#e0f2fe" stroke="#2457c5" stroke-width="2"/>`;
    b += dot(lx + f * sx, axis, 4, '#b91c1c') + text(lx + f * sx + 4, axis + 16, 'F', 'text-anchor="start"');
    b += dot(lx - f * sx, axis, 4, '#b91c1c') + text(lx - f * sx - 4, axis + 16, 'F′', 'text-anchor="end"');
    // object
    const ox = lx - u * sx;
    b += `<line x1="${ox.toFixed(1)}" y1="${axis}" x2="${ox.toFixed(1)}" y2="${(axis - h * sx).toFixed(1)}" stroke="#b45309" stroke-width="3"/>`;
    b += text(ox, axis + 16, 'object', 'text-anchor="middle"');
    if (Number.isFinite(m.v)) {
      const ix = lx + m.v * sx;
      const ih = -m.hi;
      b += `<line x1="${ix.toFixed(1)}" y1="${axis}" x2="${ix.toFixed(1)}" y2="${(axis - ih * sx).toFixed(1)}" stroke="${m.real ? '#059669' : '#7c3aed'}" stroke-width="3" stroke-dasharray="${m.real ? '' : '6 4'}"/>`;
      b += text(ix, axis + (m.real ? 34 : 16), m.real ? 'real image' : 'virtual image', 'text-anchor="middle"');
      // principal rays: parallel then through F, and through the centre
      b += line(ox, axis - h * sx, lx, axis - h * sx, '#f59e0b', 'stroke-dasharray="4 3"');
      b += line(lx, axis - h * sx, Math.max(30, Math.min(650, ix)), axis - ih * sx, '#f59e0b', 'stroke-dasharray="4 3"');
      b += line(ox, axis - h * sx, Math.max(30, Math.min(650, ix)), axis - ih * sx, '#f59e0b', 'stroke-dasharray="2 3"');
    } else {
      b += text(560, 90, 'is = ∞: parallel rays leave the lens', 'text-anchor="middle"');
    }
    draw('thin-lens', b);
    summary('thin-lens', m.real
      ? `The image is real and inverted, ${fmt(Math.abs(m.v), 1)} cm beyond the lens, with magnification ${fmt(m.m, 2)}. `
        + `It could be caught on a screen there.`
      : `The image is virtual and upright, ${fmt(Math.abs(m.v), 1)} cm on the same side as the object, with magnification `
        + `${fmt(m.m, 2)} — this is the magnifying-glass case, and you must look through the lens to see it.`);
  });
}
init['thin-lens'] = initThinLens;
EXPORTS.lensModel = lensModel;
