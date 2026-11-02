"""02.16 Heat transfer, phase transitions and radiation."""
from math import sin, cos, pi, sqrt, radians, exp, log10, log


def f_conduction():
    body = t(340, 24, 'Conduction: heat flows down the temperature gradient', INK, 13, weight=700)
    body += rect(120, 96, 400, 96, '#fef3c7', '#fcd34d', 4)
    body += t(320, 128, 'material of conductivity k, length L, area A', INK, 11.5)
    for i in range(5):
        x = 140 + i * 84
        body += line(x, 100, x, 188, '#f59e0b', 1, '4 6')
    body += t(110, 96, 'T₁', RED, 13, weight=700)
    body += t(536, 96, 'T₂', BLUE, 13, weight=700)
    body += arrow('cond', 140, 216, 500, 216, AMBER, 2.4)
    body += t(320, 238, 'heat flow', AMBER, 11.5, weight=700)
    body += t(340, 286, 'rate = kA(T₁ − T₂)/L  —  a steady state, not a stored amount', GREY, 11.5)
    return wrap('conduction', 'Steady conduction through a slab',
                'A slab with a temperature gradient and a uniform heat flow from the hot to the cold face.',
                body, caption('Figure 1.', 'Once the steady state is reached, the same power crosses every cross-section — '
                             'otherwise energy would pile up. That is why layers of different materials add thermal '
                             'resistances, exactly like resistors in series.'), 306)


def f_convection_radiation():
    body = t(340, 24, 'Radiation carries energy without any medium at all', INK, 13, weight=700)
    body += dot(215, 160, 26, AMBER) + t(215, 214, 'hot object T', AMBER, 11.5, weight=700)
    for ang in range(195, 350, 15):
        x2 = 215 + 105 * cos(radians(ang))
        y2 = 160 + 105 * sin(radians(ang))
        body += arrow('rad', 215 + 30 * cos(radians(ang)), 160 + 30 * sin(radians(ang)), x2, y2, '#f59e0b', 1.6)
    body += t(400, 112, 'P = εσAT⁴', INK, 13.5, weight=700, anchor='start')
    body += t(400, 140, 'σ = 5.67×10⁻⁸ W m⁻² K⁻⁴', GREY, 11.5, 'start')
    body += t(400, 168, 'net loss = εσA(T⁴ − T₀⁴)', GREY, 11.5, 'start')
    body += t(400, 196, 'black body: ε = 1', GREY, 11.5, 'start')
    body += t(340, 286, 'the fourth power is why doubling the temperature multiplies the radiated power by sixteen', GREY, 11.5)
    return wrap('radiation', 'Thermal radiation from a hot body',
                'A hot object emitting radiation in all directions, with the Stefan-Boltzmann law written alongside.',
                body, caption('Figure 2.', 'Radiation is electromagnetic, so it needs no medium: the Sun warms the Earth '
                             'through a vacuum. A body both emits and absorbs, and the net exchange is the difference of '
                             'the two fourth powers.'), 306)


def f_phase():
    body = t(340, 24, 'Heating curve: temperature stalls while a phase change takes place', INK, 13, weight=700)
    left, right, top, bottom = 92, 620, 60, 230
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    # segments: ice warms, melting plateau, water warms, boiling plateau, steam warms
    segs = [(0.00, 0.18, 0.0, 0.16, BLUE), (0.18, 0.40, 0.16, 0.16, AMBER),
            (0.40, 0.62, 0.16, 0.50, BLUE), (0.62, 0.86, 0.50, 0.50, AMBER),
            (0.86, 1.00, 0.50, 0.80, BLUE)]
    for x1, x2, y1, y2, col in segs:
        body += line(left + x1 * (right - left), bottom - y1 * (bottom - top),
                     left + x2 * (right - left), bottom - y2 * (bottom - top), col, 3)
    body += t(left + 0.29 * (right - left), bottom - 0.16 * (bottom - top) + 16, 'melting', AMBER, 11, weight=700)
    body += t(left + 0.74 * (right - left), bottom - 0.50 * (bottom - top) + 16, 'boiling', AMBER, 11, weight=700)
    body += t(left + 0.09 * (right - left), bottom - 0.10 * (bottom - top) - 14, 'ice warms', BLUE, 11, weight=700)
    body += t(left + 0.66 * (right - left), bottom - 0.32 * (bottom - top), 'water warms', BLUE, 11, weight=700)
    body += t(right - 4, bottom - 0.78 * (bottom - top), 'steam', BLUE, 11, 'end', 700)
    body += t(340, bottom + 26, 'heat added at a constant rate', GREY, 12)
    body += t(340, 286, 'Q = mcΔT for a temperature change;  Q = mL for a phase change at constant T', GREY, 11.5)
    return wrap('phase', 'A heating curve for water',
                'Temperature against heat added, with plateaus at melting and boiling and slopes given by specific heats.',
                body, caption('Figure 3.', 'The plateaus are longer than the slopes by a large factor: melting a gram of '
                             'ice takes as much energy as heating a gram of water through $80^\circ\mathrm{C}$.'), 306)


def f_blackbody():
    def planck(lam_um, T):
        # spectral radiance shape, arbitrary units
        from math import exp as _exp
        lam = lam_um * 1e-6
        h, c, k = 6.626e-34, 3.0e8, 1.381e-23
        x = h * c / (lam * k * T)
        if x > 700:
            return 0
        return (1 / lam ** 5) / (_exp(x) - 1)
    def scaled(T):
        peak = max(planck(0.05 + 0.005 * i, T) for i in range(1200))
        return lambda lam: planck(lam, T) / peak
    return chart(
        'blackbody', 'Black-body spectra: hotter objects peak at shorter wavelengths',
        'Wien’s law λ_max T = 2.9×10⁻³ m K links the peak wavelength to the temperature.',
        'wavelength (μm)', 'intensity (scaled to each peak)',
        [('T = 3000 K', AMBER, scaled(3000)),
         ('T = 5000 K', GREEN, scaled(5000)),
         ('T = 7000 K', BLUE, scaled(7000))],
        xr=(0.1, 3.0), yr=(-0.02, 1.05), xticks=(0.5, 1, 1.5, 2, 2.5, 3), yticks=(0.25, 0.5, 0.75, 1),
        height=355, xfmt='{:.1f}', yfmt='{:.2f}')


def f_layers():
    body = t(340, 24, 'Building insulation: thermal resistances in series', INK, 13, weight=700)
    layers = [('brick', 0.84, 0.10, '#fca5a5'), ('insulation', 0.04, 0.10, '#fde68a'), ('plaster', 0.50, 0.02, '#bfdbfe')]
    x = 150
    for name, k, d, col in layers:
        w = 90
        body += rect(x, 90, w, 110, col, GREY, 3)
        body += t(x + w / 2, 130, name, INK, 11, weight=700)
        body += t(x + w / 2, 152, f'k = {k}', GREY, 10.5)
        body += t(x + w / 2, 170, f'd = {d} m', GREY, 10.5)
        x += w + 6
    body += t(150, 78, 'inside 20 °C', RED, 11, 'start', 700)
    body += t(470, 78, 'outside 0 °C', BLUE, 11, 'end', 700)
    body += t(340, 240, 'R = d/k for each layer; the total R adds, and the flux is ΔT/ΣR', GREY, 11.5)
    body += t(340, 272, 'the insulation dominates even though it is only 10 cm: its k is twenty times smaller', GREY, 11.5)
    body += t(340, 300, 'double glazing works the same way, with an air gap as the low-k layer', GREY, 11.5)
    return wrap('layers', 'Composite wall',
                'Three layers of different conductivity and thickness, with the temperature difference across the wall.',
                body, caption('Figure 4.', 'Choosing insulation means choosing a small $k$ over a large $d$: the resistance '
                             '$d/k$ is what matters, and it adds like electrical resistance.'), 316)


def f_latent():
    bars = [('water 0→100 °C', 419, BLUE), ('melt ice', 334, AMBER), ('boil water', 2260, RED)]
    body = t(340, 24, 'Latent heats dwarf sensible heating', INK, 13, weight=700)
    top, bottom, left = 66, 216, 150
    maxv = 2260
    for i, (label, v, col) in enumerate(bars):
        y = top + i * 50
        w = (v / maxv) * 400
        body += rect(left, y, w, 32, col, col, 3, 0)
        body += t(left - 10, y + 21, label, GREY, 11, 'end', 700)
        body += t(left + w + 8, y + 21, f'{v} kJ/kg', INK, 11, 'start', 700)
    body += t(340, 262, 'boiling a kilogram of water takes more than five times the energy of heating it from 0 to 100 °C', GREY, 11.5)
    body += t(340, 290, 'that is why steam burns are so severe: the latent heat is released on contact', GREY, 11.5)
    return wrap('latent', 'Energy needed to heat, melt and boil water',
                'Horizontal bars comparing the energy to heat water, melt ice and boil water per kilogram.',
                body, caption('Figure 5.', 'Phase changes involve breaking bonds between molecules, not speeding them up, '
                             'which is why the energy is large and the temperature does not change during the change.'), 306)


FIGURES = {
    'conduction': f_conduction,
    'radiation': f_convection_radiation,
    'phase': f_phase,
    'blackbody': f_blackbody,
    'layers': f_layers,
    'latent': f_latent,
}


def lab_cooling():
    controls = (
        slider('cool-t0', 'Initial temperature', 40, 95, 1, 80, ' [°C]')
        + slider('cool-amb', 'Room temperature', 10, 35, 1, 20, ' [°C]')
        + slider('cool-k', 'Cooling constant', 0.005, 0.10, 0.005, 0.03, ' [s⁻¹]')
    )
    return shell(
        'cooling', 'Newton’s law of cooling',
        'A hot object loses heat at a rate proportional to its excess temperature, so it approaches room temperature '
        'exponentially. The experiment shows the curve, the initial cooling rate and the time to fall halfway to ambient.',
        controls,
        [('rate', 'Initial cooling rate'), ('half', 'Time to halve the excess'), ('tau', 'Time constant'),
         ('t20', 'Time to reach 20% of surplus'), ('final', 'Final temperature')],
        'Set the room temperature to 20 °C and start at 80 °C. Why does the curve flatten out instead of dropping at a '
        'constant rate? Then make the cooling constant ten times larger and see what the time constant does.'
    )


LABS = {'cooling': lab_cooling}
