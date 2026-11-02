"""02.15 Thermodynamics and the ideal gas."""
from math import sin, cos, pi, sqrt, radians, exp, log10, log


def f_pv():
    body = t(340, 24, 'A pV diagram: work is the area under the path', INK, 13, weight=700)
    left, right, top, bottom = 110, 620, 58, 236
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    body += t(right - 8, bottom + 20, 'V', GREY, 12, 'end') + t(left - 8, top + 4, 'p', GREY, 12, 'end')
    X = lambda v: left + (v / 2.0) * (right - left)
    Y = lambda p: bottom - p * (bottom - top)
    for k, col in ((0.20, '#bfdbfe'), (0.32, BLUE), (0.50, INK)):
        pts = []
        for i in range(1, 160):
            v = 0.12 + 1.85 * i / 159
            p = k / v
            if 0.06 < p < 1.06:
                pts.append((X(v), Y(p)))
        body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{col}" stroke-width="2"/>'
    # cycle: isothermal expansion A->B along pV = 0.32, then isobaric compression B->C, then isochoric C->A
    a = (X(0.50), Y(0.64)); b = (X(1.60), Y(0.20)); c = (X(0.42), Y(0.20))
    pts = [(X(v), Y(0.32 / v)) for v in [0.50 + 1.10 * i / 40 for i in range(41)]]
    body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{GREEN}" stroke-width="2.8"/>'
    body += arrow('pv', X(1.30), Y(0.32 / 1.30), X(1.45), Y(0.32 / 1.45), GREEN, 2.6)
    body += arrow('pv', X(1.2), Y(0.20), X(0.75), Y(0.20), PURPLE, 2.6)
    body += line(X(0.75), Y(0.20), X(0.42), Y(0.20), PURPLE, 2.6)
    body += line(X(0.42), Y(0.20), X(0.50), Y(0.20), AMBER, 2.6)
    body += arrow('pv', X(0.50), Y(0.26), X(0.50), Y(0.52), AMBER, 2.6)
    for pt, lab, col in ((a, 'A', GREEN), (b, 'B', PURPLE), (c, 'C', AMBER)):
        body += dot(*pt, 5, col) + t(pt[0] - 12, pt[1] - 8, lab, col, 12, weight=700)
    body += t(X(0.98), Y(0.42), 'isothermal', GREEN, 11, 'middle', 700)
    body += t(X(0.38), Y(0.40), 'isochoric', AMBER, 11, 'end', 700)
    body += t(X(1.00), Y(0.255), 'isobaric compression', PURPLE, 11, 'middle', 700)
    body += t(340, 286, 'work done by the gas = area under the curve; a closed cycle encloses the net work', GREY, 11.5)
    return wrap('pv', 'A cycle on a pV diagram',
                'Three isotherms with a closed cycle drawn on top of them, made of three different processes.',
                body, caption('Figure 1.', 'The area under a path is the work done in that process, and the area enclosed by '
                             'a cycle is the net work. The direction of travel matters: clockwise means the engine does work '
                             'on the outside world.'), 306)


def f_maxwell():
    from math import exp as _exp, sqrt as _sqrt, pi as _pi
    def maxwell(T):
        def f(v):
            # Maxwell-Boltzmann speed distribution, each curve scaled to its own peak
            return (v * v / (2 * T)) * _exp(1 - v * v / (2 * T))
        return f
    return chart(
        'maxwell', 'The Maxwell–Boltzmann distribution of molecular speeds',
        'Raising the temperature shifts the peak to higher speed; each curve is scaled to its own peak to compare shapes.',
        'molecular speed (arbitrary units)', 'number of molecules',
        [('T = 200 K', BLUE, maxwell(200)),
         ('T = 400 K', GREEN, maxwell(400)),
         ('T = 800 K', PURPLE, maxwell(800))],
        xr=(0, 90), yr=(-0.02, 1.05), xticks=(20, 40, 60, 80), yticks=(0.25, 0.5, 0.75, 1), height=355,
        xfmt='{:.0f}', yfmt='{:.2f}')


def f_first_law():
    body = t(340, 24, 'The first law: heat in, work out, internal energy changes', INK, 13, weight=700)
    body += rect(200, 90, 280, 120, '#f8fafc', BLUE, 10)
    body += t(340, 132, 'ΔU = Q − W', INK, 17, weight=700)
    body += t(340, 162, 'internal energy change = heat added', GREY, 11)
    body += t(340, 182, 'minus work done by the gas', GREY, 11)
    body += arrow('firstlaw', 130, 250, 196, 250, RED, 2.6) + t(130, 232, 'Q in', RED, 11.5, weight=700)
    body += arrow('firstlaw', 550, 250, 484, 250, GREEN, 2.6) + t(550, 232, 'W out', GREEN, 11.5, weight=700)
    body += t(340, 254, 'gas', GREY, 12)
    body += t(340, 292, 'signs are a convention: Q > 0 means heat flows into the system, W > 0 means work done by it', GREY, 11.5)
    return wrap('first-law', 'Energy bookkeeping in the first law',
                'A box representing a gas, with heat entering on the left and work leaving on the right.',
                body, caption('Figure 2.', 'The first law is just energy conservation with a sign convention. The second '
                             'law, which is not about energy at all, says that not all of Q can be turned into W.'), 306)


def f_carnot():
    def eff(r):
        return lambda T: 1 - r
    return chart(
        'carnot', 'Carnot efficiency depends only on the two temperatures',
        'No engine working between these two reservoirs can beat the Carnot limit.',
        'cold reservoir temperature (K), hot = 600 K', 'maximum efficiency',
        [('Carnot limit', BLUE, lambda t: 1 - t / 600 if t < 600 else 0)],
        xr=(200, 600), yr=(0, 0.75), xticks=(250, 350, 450, 550), yticks=(0.2, 0.4, 0.6), height=350,
        xfmt='{:.0f}', yfmt='{:.1f}',
        notes=[(300, 0.6, 'a colder sink raises the efficiency', GREY)])


def f_entropy():
    body = t(340, 24, 'The second law: entropy of the universe never decreases', INK, 13, weight=700)
    body += rect(90, 80, 200, 100, '#eff6ff', BLUE, 8)
    body += t(190, 112, 'hot reservoir', INK, 12.5, weight=700) + t(190, 142, 'T₁, Q out', GREY, 11.5)
    body += rect(390, 80, 200, 100, '#f0fdf7', GREEN, 8)
    body += t(490, 112, 'cold reservoir', INK, 12.5, weight=700) + t(490, 142, 'T₂, Q in', GREY, 11.5)
    body += arrow('entropy', 292, 130, 388, 130, AMBER, 2.6)
    body += t(340, 118, 'heat', AMBER, 11, weight=700)
    body += t(340, 210, 'ΔS = −Q/T₁ + Q/T₂ > 0 when T₂ < T₁', INK, 13, weight=700)
    body += t(340, 250, 'reversible processes keep the total unchanged; real ones increase it', GREY, 11.5)
    body += t(340, 292, 'entropy counts the number of microscopic arrangements: S = k ln W', GREY, 11.5)
    return wrap('entropy', 'Heat flow and entropy',
                'Two reservoirs at different temperatures joined by a flow of heat, with the entropy change written below.',
                body, caption('Figure 3.', 'Heat flows spontaneously from hot to cold, and the entropy increase is the '
                             'quantitative statement of that arrow of time. An engine between the reservoirs can extract '
                             'work, but the total entropy still rises.'), 306)


def f_boltzmann():
    from math import exp as _exp
    def pop(E, T):
        return _exp(-E / T)
    return chart(
        'boltzmann', 'The Boltzmann factor: higher levels are exponentially less populated',
        'At low temperature almost every particle sits in the ground state; at high temperature the levels fill up.',
        'energy above the ground state (in units of kT at 300 K)', 'relative population',
        [('T = 300 K', BLUE, lambda e: pop(e, 1.0)),
         ('T = 600 K', GREEN, lambda e: pop(e, 2.0))],
        xr=(0, 6), yr=(-0.03, 1.03), xticks=(1, 2, 3, 4, 5, 6), yticks=(0.25, 0.5, 0.75, 1), height=345,
        xfmt='{:.0f}', yfmt='{:.2f}',
        notes=[(2.2, 0.9, 'N₂/N₁ = e^(−(E₂−E₁)/kT)', GREY)])


FIGURES = {
    'pv': f_pv,
    'maxwell': f_maxwell,
    'first-law': f_first_law,
    'carnot': f_carnot,
    'entropy': f_entropy,
    'boltzmann': f_boltzmann,
}


def lab_gas():
    controls = (
        slider('gas-n', 'Amount of gas', 0.1, 3.0, 0.1, 1.0, ' [mol]')
        + slider('gas-v', 'Volume', 0.005, 0.050, 0.001, 0.0224, ' [m³]')
        + slider('gas-t', 'Temperature', 100, 1000, 10, 273, ' [K]')
    )
    return shell(
        'gas', 'The ideal gas law',
        'The experiment computes the pressure, the rms speed of the molecules, their mean kinetic energy and the number '
        'of collisions per second with a unit area of wall, and draws the speed distribution for the chosen temperature.',
        controls,
        [('p', 'Pressure'), ('vrms', 'rms speed'), ('ek', 'Mean kinetic energy'),
         ('n', 'Number density'), ('vmp', 'Most probable speed')],
        'Halve the volume at fixed temperature: what happens to the pressure and to the rms speed? Then double the '
        'temperature at fixed volume and explain why the pressure changes while the number of molecules does not.'
    )


LABS = {'gas': lab_gas}
