"""02.09 Oscillations and resonance (mechanical)."""
from math import sin, cos, pi, sqrt, radians, exp


def f_shm():
    return chart(
        'shm', 'Position, velocity and acceleration in simple harmonic motion',
        'Velocity leads position by a quarter of a cycle and acceleration is exactly opposite to position.',
        'time (in periods)', 'displacement and its derivatives',
        [('x', BLUE, lambda t: cos(2 * pi * t)),
         ('v', GREEN, lambda t: -sin(2 * pi * t)),
         ('a', PURPLE, lambda t: -cos(2 * pi * t))],
        xr=(0, 2), yr=(-1.15, 1.15), xticks=(0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2), yticks=(-1, 0, 1),
        height=360, xfmt='{:.2f}', yfmt='{:.0f}')


def f_spring():
    body = t(340, 24, 'A mass on a spring: the restoring force is proportional to the displacement', INK, 13, weight=700)
    # ceiling
    body += line(200, 62, 480, 62, GREY, 4) + t(340, 52, 'fixed support', GREY, 11)
    # helical spring from the ceiling down to the block
    coil = ''
    x, y0, y1, turns, width = 340, 66, 168, 9, 22
    pts = [(x, y0)]
    for k in range(turns):
        yy = y0 + (y1 - y0) * (k + 0.5) / turns
        pts.append((x + (width if k % 2 == 0 else -width), yy))
    pts.append((x, y1))
    body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{GREY}" stroke-width="2.2"/>'
    # equilibrium block, dashed outline
    body += rect(292, 168, 96, 78, 'none', BLUE, 6, 1.4, '6 4')
    body += t(340, 200, 'm', BLUE, 14, weight=700)
    body += t(340, 226, 'x = 0', GREY, 11)
    # displaced block
    body += rect(430, 168, 96, 78, '#dbeafe', BLUE, 6)
    body += t(478, 200, 'm', INK, 14, weight=700)
    body += t(478, 226, 'x', INK, 12, weight=700)
    # arrows: restoring force, displacement
    body += arrow('spring', 560, 128, 432, 128, AMBER, 2.6)
    body += t(496, 114, 'F = −kx', AMBER, 11.5, weight=700)
    body += arrow('spring', 340, 128, 424, 128, PURPLE, 2.2, '5 4')
    body += t(382, 114, 'x', PURPLE, 12, weight=700)
    body += t(340, 292, 'ω = √(k/m) and T = 2π√(m/k); the period is independent of the amplitude', GREY, 11.5)
    return wrap('spring', 'A mass on a spring',
                'A block on a spring, displaced from equilibrium and pulled back by a force proportional to x.',
                body, caption('Figure 2.', 'The larger the displacement, the larger the restoring force, so the acceleration '
                             'grows in proportion and the motion repeats in exactly the same time. That is what makes the '
                             'oscillation isochronous.'), 306)


def f_pendulum():
    from math import sin, cos, pi
    body = t(340, 24, 'A simple pendulum: the same equation, provided the swing is small', INK, 13, weight=700)
    body += line(210, 62, 470, 62, GREY, 4) + t(210, 52, 'pivot', GREY, 11, 'start')
    L = 150
    ang = radians(26)
    x, y = 340 + L * sin(ang), 62 + L * cos(ang)
    body += line(340, 62, x, y, INK, 2)
    body += line(340, 62, 340, 62 + L + 26, LIGHT, 1.4, '5 4')
    body += f'<path d="M340,122 A60,60 0 0,1 {340 + 60 * sin(ang):.1f},{62 + 60 * cos(ang):.1f}" fill="none" stroke="{GREY}" stroke-width="1.4"/>'
    body += t(354, 118, 'θ', INK, 12, 'start')
    body += dot(x, y, 9, AMBER)
    body += arrow('pend', x, y + 10, x, y + 76, RED, 2.4) + t(x + 10, y + 88, 'mg', RED, 12, 'start', 700)
    # tangential component: perpendicular to the string, towards the lowest point
    tx, ty = x - 56 * cos(ang), y + 56 * sin(ang)
    body += arrow('pend', x, y, tx, ty, PURPLE, 2.4)
    body += t(tx - 104, ty + 14, 'mg sinθ', PURPLE, 11.5, 'start', 700)
    body += line(x, y, x + 54 * sin(ang), y - 54 * cos(ang), BLUE, 2, '4 4')
    body += t(x + 58 * sin(ang) + 4, y - 54 * cos(ang) - 4, 'T', BLUE, 12, 'start', 700)
    body += t(340, 316, 'T = 2π√(L/g) for small angles; a larger swing is slower, because sinθ < θ', GREY, 11.5)
    return wrap('pendulum', 'Forces on a pendulum bob',
                'A pendulum displaced through an angle theta, with the weight, its tangential component and the tension.',
                body, caption('Figure 3.', 'Only the tangential component of the weight drives the motion, and it is '
                             'mg sinθ. Dividing by the mass gives a = −g sinθ ≈ −(g/L)s, which is the spring equation with '
                             'k/m = g/L.'), 328)


def f_damping():
    def under(t):
        return exp(-0.6 * t) * cos(2 * pi * 1.4 * t)
    return chart(
        'damping', 'Damped oscillations: three regimes',
        'Weak damping lets the swing decay slowly; critical damping returns to rest fastest without overshooting.',
        'time (arbitrary units)', 'displacement',
        [('underdamped', BLUE, under),
         ('critically damped', GREEN, lambda t: (1 + 2.4 * t) * exp(-2.4 * t)),
         ('overdamped', AMBER, lambda t: 0.55 * exp(-0.8 * t) + 0.45 * exp(-4.0 * t))],
        xr=(0, 6), yr=(-1.1, 1.1), xticks=(1, 2, 3, 4, 5, 6), yticks=(-1, 0, 1), height=355,
        xfmt='{:.0f}', yfmt='{:.0f}',
        notes=[(0.1, 1.06, 'all three start from the same displacement', GREY)])


def f_energy():
    return chart(
        'energy-shm', 'Energy in simple harmonic motion',
        'The total energy is constant; kinetic and potential exchange twice per oscillation.',
        'time (in periods)', 'energy (fraction of the total)',
        [('kinetic ½mv²', GREEN, lambda t: sin(2 * pi * t) ** 2),
         ('potential ½kx²', BLUE, lambda t: cos(2 * pi * t) ** 2)],
        xr=(0, 2), yr=(-0.05, 1.1), xticks=(0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2), yticks=(0, 0.5, 1),
        height=345, xfmt='{:.2f}', yfmt='{:.1f}')


def f_driven():
    body = t(340, 24, 'A driven oscillator: the amplitude peaks near the natural frequency', INK, 13, weight=700)
    left, right, top, bottom = 92, 640, 52, 218
    umax = 2.0
    X = lambda u: left + u / umax * (right - left)
    Y = lambda a: bottom - min(a, 4.0) / 4.0 * (bottom - top)
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    for u in (0, 0.5, 1.0, 1.5, 2.0):
        body += line(X(u), top, X(u), bottom, '#eef2f7') + t(X(u), bottom + 18, f'{u:.1f}', GREY, 11)
    for a in (1, 2, 3, 4):
        body += line(left, Y(a), right, Y(a), '#eef2f7') + t(left - 8, Y(a) + 4, f'{a}', GREY, 11, 'end')
    body += t(340, bottom + 40, 'driving frequency / natural frequency', GREY, 12)
    body += f'<g transform="translate(24,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'amplitude / static response', GREY, 12) + '</g>'
    for q, col in ((0.25, BLUE), (1.0, GREEN), (4.0, PURPLE)):
        def amp(u, q=q):
            return 1 / sqrt((1 - u * u) ** 2 + (u / q) ** 2)
        pts = [(X(i / 200 * umax), Y(amp(i / 200 * umax))) for i in range(0, 201)]
        body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{col}" stroke-width="2.4"/>'
    body += legend([(BLUE, 'Q = 0.25', ''), (GREEN, 'Q = 1', ''), (PURPLE, 'Q = 4', '')], 276, 130, 200)
    body += t(340, 330, 'high Q: a tall, narrow peak; above resonance the response is almost out of phase', GREY, 11.5)
    return wrap('driven', 'Amplitude response of a driven oscillator',
                'Resonance curves for three amounts of damping, plotted against the frequency ratio.',
                body, caption('Figure 6.', 'With weak damping the peak sits at ω ≈ ω₀ and its height is about Q times the '
                             'static response; stronger damping lowers the peak and shifts it slightly downwards.'), 342)


FIGURES = {
    'shm': f_shm,
    'spring': f_spring,
    'pendulum': f_pendulum,
    'damping': f_damping,
    'energy-shm': f_energy,
    'driven': f_driven,
}


def lab_pendulum():
    controls = (
        slider('swing-l', 'Pendulum length', 0.20, 3.00, 0.05, 1.00, ' [m]')
        + slider('swing-a', 'Amplitude', 1, 60, 1, 10, ' [°]')
        + slider('swing-g', 'Gravity', 1.6, 25.0, 0.1, 9.81, ' [m/s²]')
    )
    return shell(
        'pendulum-swing', 'A simple pendulum, exactly',
        'The experiment solves the full nonlinear equation for the period by numerical quadrature, so you can see how far '
        'the small-angle formula T = 2π√(L/g) departs from the truth at large amplitudes, and what happens on the Moon or '
        'on Jupiter, where g is different.',
        controls,
        [('T', 'Small-angle period'), ('Tex', 'Exact period'), ('err', 'Error of the formula'),
         ('f', 'Frequency'), ('vmax', 'Maximum speed')],
        'Push the amplitude to 60°: how large is the error of the small-angle formula? Then set g = 1.6 m/s² (the Moon) and '
        'explain why a pendulum clock would run slow there.'
    )


LABS = {'pendulum-swing': lab_pendulum}
