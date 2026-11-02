/* 01.01 — dimensional analysis searchlight */
const DIMS = {
  pend: { M: 0, L: 1, T: 0 },
  kepler: { M: -1, L: 3, T: 0 },
  escape: { M: 0, L: 1, T: -2 },
  wrong: { M: 1, L: 2, T: -1 }
};
function sup(n) {
  const map = { '-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹' };
  return String(n).split('').map(c => map[c] || c).join('');
}
function dimString(d) {
  const parts = [];
  for (const k of ['M', 'L', 'T']) if (d[k]) parts.push(k + (d[k] === 1 ? '' : sup(d[k])));
  return parts.length ? parts.join(' ') : 'dimensionless';
}
function initUnits() {
  bind('units', () => {
    const key = $('units-formula').value, want = DIMS[key];
    const guess = { M: value('units-m'), L: value('units-l'), T: value('units-t') };
    const same = ['M', 'L', 'T'].every(k => guess[k] === want[k]);
    out('units', 'want', dimString(want));
    out('units', 'got', dimString(guess));
    out('units', 'verdict', same ? '✓ dimensions agree' : '✗ cannot equal the target');
    out('units', 'pi', same ? 'yes — a pure-number ratio' : 'not yet');
    let b = `<rect x="60" y="36" width="560" height="62" rx="8" fill="#eff6ff" stroke="#2457c5"/>`;
    b += text(80, 62, 'Target: ' + $('units-formula').selectedOptions[0].textContent, 'text-anchor="start"');
    b += `<text x="80" y="86" fill="#1e3a8a" font-size="15" font-weight="700">${esc(dimString(want))}</text>`;
    b += `<rect x="60" y="110" width="560" height="62" rx="8" fill="${same ? '#f0fdf7' : '#fef2f2'}" stroke="${same ? '#059669' : '#b91c1c'}"/>`;
    b += text(80, 136, 'Your candidate', 'text-anchor="start"');
    b += `<text x="80" y="160" fill="${same ? '#047857' : '#b91c1c'}" font-size="15" font-weight="700">${esc(dimString(guess))}</text>`;
    ['M', 'L', 'T'].forEach((k, i) => {
      const x = 90 + i * 180, base = 268, h = clamp(guess[k], -2, 4) * 15;
      b += line(x, base, x + 130, base, '#94a3b8');
      b += `<rect x="${x + 10}" y="${h >= 0 ? base - h : base}" width="110" height="${Math.abs(h) || 1}" fill="${guess[k] === want[k] ? '#a7f3d0' : '#fecaca'}"/>`;
      b += text(x + 65, base + 18, k + ' exponent', 'text-anchor="middle"');
      b += line(x + 10, base - want[k] * 15, x + 120, base - want[k] * 15, '#2457c5', 'stroke-dasharray="5 4"');
    });
    b += text(340, 312, 'Dashed line = the exponent the target demands', 'text-anchor="middle"');
    draw('units', b);
    summary('units', same
      ? 'Dimensions agree. Any dimensionless constant (2π, ½, a pure number) is still unknown — dimensions never fix it.'
      : 'Dimensions disagree, so no choice of constant can rescue the relation. Change one exponent and check again.');
  });
}
init.units = initUnits;
EXPORTS.dimString = dimString;
EXPORTS.DIMS = DIMS;
