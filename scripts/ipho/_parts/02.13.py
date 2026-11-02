"""02.13 Quantum physics: waves, atoms and spectra."""
from math import sin, cos, pi, sqrt, radians, exp, log10

H = 6.626e-34
C = 3.0e8


def f_photoelectric():
    from math import sqrt as _sqrt
    f0 = 5.0            # threshold frequency, in units of 1e14 Hz
    def ke(f):
        return max(0.0, 0.26 * (f - f0))
    return chart(
        'photoelectric', 'The photoelectric effect: kinetic energy rises linearly in frequency',
        'Below the threshold frequency nothing is emitted however bright the light; above it, only the frequency sets the energy.',
        'frequency (10¹⁴ Hz)', 'maximum kinetic energy (arbitrary units)',
        [('K_max', BLUE, ke)],
        xr=(0, 15), yr=(0, 3.4), xticks=(5, 10, 15), yticks=(1, 2, 3), height=355,
        xfmt='{:.0f}', yfmt='{:.0f}',
        notes=[(5.3, 0.12, 'threshold f₀ = φ/h', GREY)])


def f_energy_levels():
    levels = [(-13.6, 'n = 1'), (-3.40, 'n = 2'), (-1.51, 'n = 3'), (-0.85, 'n = 4'), (-0.54, 'n = 5'), (0.0, 'n = ∞')]
    body = t(340, 24, 'Hydrogen: Eₙ = −13.6 eV/n²  (levels spaced by n for clarity)', INK, 13, weight=700)
    ys = [262, 196, 150, 118, 96, 68]
    for (e, label), y in zip(levels, ys):
        body += line(160, y, 530, y, LIGHT, 1.6)
        body += t(540, y + 4, label, GREY, 11, 'start')
        body += t(150, y + 4, f'{e:.2f} eV' if e else '0 eV', GREY, 11, 'end')
    # Lyman alpha, Balmer alpha, and the ionisation limit
    for (y1, y2, col, lab) in ((262, 196, PURPLE, 'Lyman α 122 nm'), (196, 150, BLUE, 'Balmer α 656 nm'), (196, 68, GREEN, 'ionisation 364 nm')):
        body += arrow('levels', 300, y1, 300, y2, col, 2.2)
        body += t(312, (y1 + y2) / 2 + 4, lab, col, 11, 'start', 700)
    body += t(340, 296, 'the real gaps shrink towards zero; the series crowd together and stop at the ionisation limit', GREY, 11.5)
    return wrap('energy-levels', 'Energy levels of hydrogen',
                'A ladder of negative energy levels with arrows for the Lyman and Balmer transitions.',
                body, caption('Figure 2.', 'Every downward arrow is a photon of energy equal to the level difference, so '
                             'hydrogen’s spectrum is a set of sharp lines — a fingerprint of the atom.'), 310)


def f_debroglie():
    return chart(
        'de-broglie', 'Matter waves: λ = h/p falls with momentum',
        'An electron at 100 eV has a wavelength of about 0.12 nm, comparable with atomic spacings.',
        'kinetic energy (eV)', 'de Broglie wavelength (nm)',
        [('electron', BLUE, lambda e: 1.226 / sqrt(max(e, 1e-6))),
         ('proton', GREEN, lambda e: 0.0286 / sqrt(max(e, 1e-6)))],
        xr=(1, 1000), yr=(0, 1.8), xticks=(1, 10, 100, 1000), yticks=(0.5, 1, 1.5), height=355,
        xfmt='{:.0f}', yfmt='{:.1f}')


def f_bohr():
    body = t(340, 24, 'The Bohr model: quantised orbits and standing electron waves', INK, 13, weight=700)
    cx, cy = 290, 158
    for n, r, col in ((1, 30, BLUE), (2, 54, GREEN), (3, 82, PURPLE), (4, 112, '#94a3b8')):
        body += circle(cx, cy, r, col, 'none', 1.8, '' if n == 1 else '5 4')
    body += dot(cx, cy, 6, AMBER) + t(cx - 10, cy - 10, 'p⁺', AMBER, 11, 'end', 700)
    body += dot(cx + 30, cy, 5, BLUE)
    body += t(cx + 38, cy - 8, 'n = 1', BLUE, 11, 'start', 700)
    body += t(490, 96, 'rₙ = n²a₀,  a₀ = 0.053 nm', INK, 12, 'start', 700)
    body += t(490, 124, 'mvr = nh/2π', GREY, 11.5, 'start')
    body += t(490, 148, 'Eₙ = −13.6 eV/n²', GREY, 11.5, 'start')
    body += t(490, 172, '2πr = nλ', GREY, 11.5, 'start')
    body += t(340, 300, 'an orbit is allowed only if a whole number of de Broglie wavelengths fits round it', GREY, 11.5)
    return wrap('bohr', 'The Bohr model of the hydrogen atom',
                'Concentric orbits for n = 1 to 4 around a proton, with the quantisation rules listed.',
                body, caption('Figure 4.', 'Bohr’s assumption looked arbitrary in 1913, but it is exactly the condition '
                             'that the electron forms a standing wave round the nucleus — the first hint that matter waves '
                             'are real.'), 312)


def f_uncertainty():
    from math import log10
    body = t(340, 24, 'The uncertainty principle sets a floor on how well you can know both', INK, 13, weight=700)
    left, right, top, bottom = 100, 620, 66, 236
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    n = 120
    pts = []
    for i in range(n + 1):
        x = 0.12 + 1.9 * i / n            # log10(delta x)
        y = 0.12 + 1.9 * 0.5 / 10 ** x    # log10(delta p) = log10(hbar/2) - log10(delta x)
        X = left + (x - 0.1) / 2.0 * (right - left)
        Y = bottom - (y - 0.1) / 1.05 * (bottom - top)
        pts.append((X, Y))
    body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>'
    for xd, pd in ((0.2, 0.5), (1.0, 0.1), (0.5, 0.2)):
        X = left + (xd - 0.1) / 2.0 * (right - left)
        Y = bottom - (pd - 0.1) / 1.05 * (bottom - top)
        body += rect(X - 22, Y - 14, 44, 28, '#dbeafe', BLUE, 4, 1.2, '4 3')
    body += t(340, bottom + 26, 'uncertainty in position  (arbitrary log scale)', GREY, 12)
    body += f'<g transform="translate(26,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'uncertainty in momentum', GREY, 12) + '</g>'
    body += t(360, 90, 'Δx·Δp ≥ ℏ/2', INK, 13, weight=700)
    body += t(340, 296, 'the boxes may slide along the curve but can never shrink to a point', GREY, 11.5)
    return wrap('uncertainty', 'The Heisenberg uncertainty relation',
                'A hyperbola in the position-momentum plane, with three allowed uncertainty boxes.',
                body, caption('Figure 5.', 'The relation is not about clumsy instruments: it is a property of waves. A '
                             'wave packet that is narrow in space must contain a wide range of wavelengths, and hence a '
                             'wide range of momenta.'), 316)


def f_spectra():
    body = t(340, 24, 'Emission and absorption: the same lines, opposite directions', INK, 13, weight=700)
    rainbow = ['#7f00ff', '#4b00ff', '#0000ff', '#0066ff', '#00b3ff', '#00ffcc', '#00ff33',
               '#66ff00', '#ccff00', '#ffee00', '#ff9900', '#ff3300', '#cc0000']
    lines = [(180, '#7c3aed'), (280, '#2457c5'), (360, '#059669'), (470, '#b45309')]
    for row, label in ((92, 'continuous'), (150, 'emission'), (208, 'absorption')):
        body += rect(120, row - 13, 400, 26, '#f8fafc', '#e2e8f0', 3)
        body += t(110, row + 4, label, GREY, 11, 'end', 700)
    for i, col in enumerate(rainbow):
        body += rect(120 + i * 30, 84, 30, 16, col, col, 0, 0)
    for x, col in lines:
        body += rect(x, 86, 6, 12, '#0f172a', '#0f172a', 0, 0)      # dark gaps marking the absorption lines
        body += rect(x, 144, 6, 12, col, col, 0, 0)                  # emission lines
    for i, col in enumerate(rainbow):
        body += rect(120 + i * 30, 202, 30, 16, col, col, 0, 0)
    for x, col in lines:
        body += rect(x, 202, 6, 16, '#0f172a', '#0f172a', 0, 0)
    body += t(340, 254, 'the dark lines of an absorption spectrum sit exactly where the bright emission lines are', GREY, 11.5)
    body += t(340, 290, 'E = hf = hc/λ, so a spectrum is a direct map of the energy levels', GREY, 11.5)
    return wrap('spectra', 'Line spectra',
                'Three strips: a continuous spectrum with dark lines, bright emission lines, and the same lines in absorption.',
                body, caption('Figure 6.', 'Astronomers read composition, temperature and motion from these lines: the pattern '
                             'identifies the element, the brightness the abundance, and the Doppler shift the velocity.'), 310)


FIGURES = {
    'photoelectric': f_photoelectric,
    'energy-levels': f_energy_levels,
    'de-broglie': f_debroglie,
    'bohr': f_bohr,
    'uncertainty': f_uncertainty,
    'spectra': f_spectra,
}


def lab_photoelectric():
    controls = (
        slider('pe-w', 'Work function of the metal', 1.5, 5.0, 0.1, 2.3, ' [eV]')
        + slider('pe-l', 'Wavelength of the light', 200, 800, 5, 400, ' [nm]')
        + slider('pe-i', 'Intensity', 1, 100, 1, 50, ' [%]')
    )
    return shell(
        'photoelectric', 'The photoelectric effect',
        'The experiment reports the photon energy, the maximum kinetic energy of the electrons, the stopping voltage and '
        'the number of electrons per second, and draws the energy balance as a bar chart.',
        controls,
        [('E', 'Photon energy'), ('K', 'Maximum kinetic energy'), ('V', 'Stopping voltage'),
         ('f0', 'Threshold wavelength'), ('n', 'Electrons per second (relative)')],
        'Double the wavelength: does the current stop smoothly or suddenly? Now raise the intensity at a wavelength beyond '
        'the threshold — why does nothing happen? These two observations killed the wave theory of light.'
    )


LABS = {'photoelectric': lab_photoelectric}
