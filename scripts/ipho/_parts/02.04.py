"""02.04 Celestial mechanics and gravitation."""
from math import sqrt, pi, cos, sin, radians, log10


def f_orbits():
    from math import cos, sin, pi, sqrt
    body = t(340, 24, 'Conic sections are the only allowed orbits', INK, 13, weight=700)
    fx, fy = 250, 150           # occupied focus
    e = 0.55
    a = 120.0
    b = a * sqrt(1 - e * e)
    # ellipse centred at distance a*e from the focus
    cx = fx + a * e
    pts = [(cx + a * cos(2 * pi * i / 120), fy + b * sin(2 * pi * i / 120)) for i in range(121)]
    body += polyline(pts, GREEN, 2.6)
    body += dot(fx, fy, 9, AMBER) + t(fx - 30, fy + 26, 'focus', AMBER, 11.5, 'end')
    # parabola with the same focus, opening right: y² = 4p(x - fx + p)
    ppar = 46.0
    par = [(fx - ppar + (yy * yy) / (4 * ppar) + ppar, fy + yy) for yy in [(-150 + 3 * i) for i in range(101)]]
    body += polyline([(x, y) for x, y in par if fy - 130 < y < fy + 130], GREY, 2.2, '6 4')
    # hyperbola branch (left side) joining the family
    ah, eh = 70.0, 1.6
    bh = ah * sqrt(eh * eh - 1)
    hyp = [(fx + ah * eh - ah * __import__('math').cosh(t / 40), fy + bh * __import__('math').sinh(t / 40))
           for t in range(-46, 47)]
    body += polyline([(x, y) for x, y in hyp if 60 < x < 620 and 30 < y < 270], PURPLE, 2.2, '6 4')
    body += t(470, 62, 'ellipse  e < 1', GREEN, 11.5, 'start', 700)
    body += t(470, 84, 'parabola  e = 1', GREY, 11.5, 'start', 700)
    body += t(470, 106, 'hyperbola  e > 1', PURPLE, 11.5, 'start', 700)
    body += t(340, 292, 'The shape is fixed by one number: the eccentricity, or equivalently the total energy.', GREY, 11.5)
    return wrap('orbits', 'One focus, three orbit shapes',
                'Elliptic, parabolic and hyperbolic paths with a common focus at the attracting body.',
                body, caption('Figure 1.', 'Bound orbits close (E < 0), parabolic orbits just escape (E = 0), and '
                             'hyperbolic orbits always escape (E > 0).'), 306)


def f_orbit_speed():
    from math import sqrt
    GM = 398600.4418
    R = 6371.0
    return chart(
        'orbit-speed', 'Orbital speed falls as 1/√r; escape speed is √2 times larger',
        'Circular speed v_c = √(GM/r) and escape speed v_e = √(2GM/r) around an Earth-mass body.',
        'orbital radius (Earth radii)', 'speed (km s⁻¹)',
        [('circular orbit', BLUE, lambda r: sqrt(GM / (r * R))),
         ('escape speed', GREEN, lambda r: sqrt(2 * GM / (r * R)))],
        xr=(1, 12), yr=(0, 12), xticks=(2, 4, 6, 8, 10, 12), yticks=(0, 3, 6, 9, 12), height=340,
        notes=[(1.15, 11.1, 'at the surface: 7.9 and 11.2 km s⁻¹', GREY)])


def f_kepler():
    return chart(
        'kepler-third', 'Kepler’s third law is a straight line on log–log axes',
        'T² ∝ a³ for every body orbiting the same mass; the slope is exactly 3/2.',
        'log₁₀(a / AU)', 'log₁₀(T / yr)',
        [('planets and dwarf planets', BLUE, lambda x: 1.5 * x)],
        xr=(-0.4, 1.8), yr=(-0.6, 2.7), xticks=(0, 0.5, 1, 1.5), yticks=(0, 1, 2), height=330,
        xfmt='{:.1f}', yfmt='{:.0f}',
        notes=[(-0.35, 2.3, 'slope 3/2 ⇒ T² = a³', GREY)])


def f_energy():
    return chart(
        'effective-potential', 'The effective potential explains every orbit',
        'U_eff(r) = −GMm/r + L²/(2mr²). The minimum is a circular orbit; a higher energy gives an ellipse, zero gives a parabola.',
        'radius r (arbitrary units)', 'energy (arbitrary units)',
        [('gravitational −1/r', GREY, lambda r: -1 / r if r else None),
         ('centrifugal +L²/2mr²', PURPLE, lambda r: 0.5 / (r * r) if r else None),
         ('effective total', BLUE, lambda r: -1 / r + 0.5 / (r * r) if r else None)],
        xr=(0.4, 6), yr=(-1.2, 1.2), xticks=(1, 2, 3, 4, 5), yticks=(-1, -0.5, 0, 0.5, 1), height=340,
        xfmt='{:.0f}', yfmt='{:.1f}',
        notes=[(1.15, -0.95, 'circular orbit at the well minimum', GREY)])


def f_lagrange():
    from math import sqrt
    body = t(340, 24, 'Five Lagrange points where two gravity fields and rotation balance', INK, 13, weight=700)
    x1, x2, y0 = 250, 430, 200
    body += line(150, y0, 566, y0, '#e2e8f0', 1.2)
    mid = (x1 + x2) / 2
    h = min((x2 - x1) * sqrt(3) / 2, 86.0)
    body += poly([(x1, y0), (x2, y0), (mid, y0 - h)], 'none', '#cbd5e1', 1.4, 1, '5 4')
    body += poly([(x1, y0), (x2, y0), (mid, y0 + h)], 'none', '#cbd5e1', 1.4, 1, '5 4')
    body += circle(x1, y0, 30, AMBER, '#fef3c7', 2.4) + t(x1, y0 + 5, 'M₁', INK, 12, weight=700)
    body += circle(x2, y0, 17, BLUE, '#dbeafe', 2.4) + t(x2, y0 + 4, 'M₂', INK, 10, weight=700)
    body += dot(x2 + 26, y0, 5, GREEN) + t(x2 + 26, y0 - 14, 'L1', GREEN, 11.5, weight=700)
    body += dot(x1 - 50, y0, 5, GREEN) + t(x1 - 50, y0 - 14, 'L3', GREEN, 11.5, weight=700)
    body += dot(x2 + 62, y0, 5, GREEN) + t(x2 + 62, y0 - 14, 'L2', GREEN, 11.5, weight=700)
    body += dot(mid, y0 - h, 6, PURPLE) + t(mid, y0 - h - 12, 'L4', PURPLE, 11.5, weight=700)
    body += dot(mid, y0 + h, 6, PURPLE) + t(mid, y0 + h + 20, 'L5', PURPLE, 11.5, weight=700)
    body += t(340, 322, 'L1–L3 are unstable saddles; L4 and L5 are stable when the mass ratio exceeds about 25.', GREY, 11.5)
    return wrap('lagrange', 'The five Lagrange points of a two-body system',
                'The collinear points L1–L3 and the equilateral triangular points L4 and L5.',
                body, caption('Figure 5.', 'A small body at a Lagrange point corotates with the two larger masses; '
                             'L4 and L5 can trap dust, asteroids and spacecraft.'), 352)


FIGURES = {
    'orbits': f_orbits,
    'orbit-speed': f_orbit_speed,
    'kepler-third': f_kepler,
    'effective-potential': f_energy,
    'lagrange': f_lagrange,
}


def lab_orbit():
    controls = (
        slider('orbit-r', 'Semi-major axis a', 1, 12, 0.1, 4.0, ' [R⊕]')
        + slider('orbit-e', 'Eccentricity e', 0, 0.9, 0.01, 0.0)
        + slider('orbit-nu', 'True anomaly ν', 0, 360, 1, 30, ' [deg]')
    )
    return shell(
        'orbit', 'Orbit geometry: a, e and the vis-viva speed',
        'The ellipse is drawn with the central body at the occupied focus. Speed follows the vis-viva equation '
        'v² = GM(2/r − 1/a); the drawing is to scale in units of Earth radii.',
        controls,
        [('r', 'Current radius'), ('v', 'Speed there'), ('peri', 'Periapsis speed'),
         ('apo', 'Apoapsis speed'), ('T', 'Orbital period')],
        'Set e = 0: the speed is constant and the orbit is a circle. Raise e to 0.8 and step ν through a full turn: '
        'where is the body fastest, and how does Kepler’s second law show up?'
    )


LABS = {'orbit': lab_orbit}
