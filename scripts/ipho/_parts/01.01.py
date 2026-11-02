def legend(items, y, x0=96, dx=150, size=12):
    body = ''
    for i, item in enumerate(items):
        colour, label = item[0], item[1]
        dash = item[2] if len(item) > 2 else ''
        x = x0 + i * dx
        body += line(x, y, x + 26, y, colour, 3, dash)
        body += t(x + 33, y + 4, label, colour, size, 'start', 700)
    return body


def f_dimensions():
    rows = [('length', 'L', 'm'), ('mass', 'M', 'kg'), ('time', 'T', 's'),
            ('current', 'I', 'A'), ('temperature', 'Θ', 'K')]
    body = t(340, 30, 'Every physical quantity is a product of the five base dimensions', INK, 14, weight=700)
    cols = {'quantity': 70, 'dim': 290, 'unit': 430}
    body += t(cols['quantity'], 64, 'quantity', GREY, 11.5) + t(cols['dim'], 64, 'dimension', GREY, 11.5) + \
            t(cols['unit'], 64, 'SI unit', GREY, 11.5)
    for i, (name, dim, unit) in enumerate(rows):
        y = 88 + i * 36
        body += rect(40, y - 20, 600, 32, '#fbfcff', '#e2e8f0', 6, 1)
        body += t(cols['quantity'], y, name, INK, 13, 'start')
        body += t(cols['dim'] + 20, y, dim, PURPLE, 13, weight=700)
        body += t(cols['unit'] + 20, y, unit, GREEN, 13, weight=700)
    body += rect(40, 280, 600, 66, '#eff6ff', BLUE, 8)
    body += t(60, 305, 'Derived example:', BLUE, 12, 'start', 700)
    body += t(60, 328, 'force = mass × acceleration  →  [M L T⁻²]  →  newton = kg m s⁻²', INK, 12.5, 'start')
    return wrap('dimensions', 'Base dimensions and SI units',
                'Five base dimensions build every derived unit used in olympiad physics.',
                body, caption('Figure 1.', 'If two sides of an equation have different dimensions, the equation is wrong. '
                             'Dimensional checking is free, instant and exact.'), 366)


def f_scaling():
    box_ = (90, 46, 640, 220)
    X = lambda x: 90 + x / 3 * 550
    Y = lambda y: 220 - y / 3.2 * 178
    body = grid(box_, 3, 4) + frame('growth factor of the input, log scale', 'growth factor of the answer, log scale',
                                    box_, [(i, X(i)) for i in range(4)], [(i, Y(i)) for i in range(4)])
    body += polyline([(X(0), Y(0)), (X(3), Y(1.5))], BLUE)
    body += polyline([(X(0), Y(0)), (X(3), Y(3))], GREEN)
    body += polyline([(X(0), Y(0)), (X(2.4), Y(3.05))], PURPLE)
    body += t(340, 20, 'A power law becomes a straight line on log–log axes', INK, 13, weight=700)
    body += legend([(BLUE, 'y ∝ √x: slope ½'), (GREEN, 'y ∝ x: slope 1'), (PURPLE, 'y ∝ x²: slope 2')], 288, 110, 190)
    body += t(340, 320, 'Read the slope, and you have measured the exponent.', GREY, 12)
    return wrap('scaling', 'Scaling laws are straight lines in log–log space',
                'Three common powers plotted on logarithmic axes; the slope is the exponent.',
                body, caption('Figure 2.', 'Doubling the radius of a sphere multiplies its area by 4 and its volume by 8. '
                             'Reading the slope of a log–log graph tells you the exponent without any algebra.'), 330)


def f_taylor():
    box_ = (90, 46, 640, 214)
    X = lambda x: 90 + x / 3.1 * 550
    Y = lambda y: 214 - (y + 1.3) / 3.0 * 172
    body = grid(box_, 4, 4) + frame('x (radians)', 'sin x', box_,
                                    [(1, X(1)), (2, X(2)), (3, X(3))],
                                    [(-1, Y(-1)), (0, Y(0)), (1, Y(1))])
    body += curve(sin, 0, 3.1, -1.3, 1.7, box_, 160, INK, 3.2)
    body += curve(lambda x: x, 0, 3.1, -1.3, 1.7, box_, 160, GREEN, 2.2, '7 5')
    body += curve(lambda x: x - x ** 3 / 6, 0, 3.1, -1.3, 1.7, box_, 160, PURPLE, 2.2, '7 5')
    body += curve(lambda x: x - x ** 3 / 6 + x ** 5 / 120, 0, 3.1, -1.3, 1.7, box_, 160, AMBER, 2.2, '7 5')
    body += t(340, 20, 'Successive Taylor approximations close in on the exact curve', INK, 13, weight=700)
    body += legend([(INK, 'sin x (exact)'), (GREEN, 'x'), (PURPLE, 'x − x³/6'), (AMBER, 'three terms')], 288, 92, 148)
    body += t(340, 320, 'The three-term curve hides under the exact one: adding terms buys range, not looks.',
              GREY, 12)
    return wrap('taylor', 'Successive Taylor approximations close in on the exact curve',
                'The sine function compared with one, two and three terms of its Taylor series.',
                body, caption('Figure 3.', 'Each extra term buys accuracy over a wider range. Estimate the error before you '
                             'decide whether the approximation is good enough for the precision you need.'), 330)


def f_limits():
    box_ = (90, 46, 640, 210)
    X = lambda x: 90 + x / 1.2 * 550
    Y = lambda y: 210 - y / 12 * 164
    body = grid(box_, 4, 4) + frame('angle θ (radians)', 'error in sin θ ≈ θ  (%)', box_,
                                    [(0.3, X(0.3)), (0.6, X(0.6)), (0.9, X(0.9)), (1.2, X(1.2))],
                                    [(0, Y(0)), (4, Y(4)), (8, Y(8)), (12, Y(12))], xfmt='{:.1f}')
    body += curve(lambda x: 100 * (x / sin(x) - 1) if x else 0, 0.001, 1.2, 0, 12, box_, 240, BLUE, 2.8)
    body += line(X(0.26), 46, X(0.26), 210, GREEN, 1.6, '6 4')
    body += line(X(0.5), 46, X(0.5), 210, AMBER, 1.6, '6 4')
    body += t(340, 20, 'How small is “small” for the small-angle approximation?', INK, 13, weight=700)
    body += legend([(GREEN, '0.26 rad ≈ 15°: 0.3% error'), (AMBER, '0.5 rad ≈ 29°: 4% error')], 290, 120, 250)
    body += t(340, 318, 'An approximation without an error estimate is a guess.', GREY, 12)
    return wrap('limits', 'How small is “small” for the small-angle approximation?',
                'Relative error introduced by replacing sin θ with θ, as a function of angle.',
                body, caption('Figure 4.', 'The error is below 1% only for angles under about 0.4 rad (23°). Quote that '
                             'number instead of claiming the angle is “small enough”.'), 320)


def f_fermi():
    steps = ['Area of the sky covered|by one photograph',
             'Number of photographs|needed for the whole sky',
             'Galaxies per photograph|above the plate limit',
             'Total galaxies|≈ product']
    body = t(340, 28, 'A Fermi estimate is a chain of ratios, each known to a factor of a few', INK, 13.5, weight=700)
    for i, label in enumerate(steps):
        x = 28 + i * 162
        body += box(x, 60, 146, 84, label, PALE if i < 3 else '#f0fdf7', BLUE if i < 3 else GREEN, 11.5)
        if i < 3:
            body += arrow('fermi', x + 147, 102, x + 160, 102, GREY, 2)
    body += t(340, 186, 'Each factor is uncertain by ×2 or ×3.  Four such factors give a total spread of about ×10.', GREY, 12)
    body += t(340, 214, 'That is enough to decide whether the answer is “millions” or “billions” — and to know why.', GREY, 12)
    body += rect(60, 240, 560, 62, '#fbfcff', '#dce4f2', 8)
    body += t(80, 264, '1. Expose for a known time   2. Count sources   3. Scale to the sky   4. State the uncertainty', BLUE, 11.5, 'start', 700)
    body += t(80, 288, 'Write every step as a fraction with named units, so mistakes cancel visibly.', INK, 11.5, 'start')
    return wrap('fermi', 'How an order-of-magnitude estimate is built',
                'Four chained ratios turn a hard counting question into arithmetic.',
                body, caption('Figure 5.', 'The point of a Fermi estimate is not the third digit; it is a defensible power of ten '
                             'plus an honest uncertainty.'), 320)


def f_symmetry():
    body = t(340, 22, 'Two identical pulls cannot make the block drift sideways', INK, 13, weight=700)
    cx, cy = 200, 148
    body += rect(cx - 44, cy - 44, 88, 88, '#e2e8f0', GREY, 10)
    body += t(cx, cy + 6, 'm', INK, 16, weight=700)
    body += arrow('symmetry', cx - 46, cy, cx - 152, cy, BLUE, 3)
    body += arrow('symmetry', cx + 46, cy, cx + 152, cy, BLUE, 3)
    body += t(cx - 136, cy - 12, 'T', BLUE, 14, weight=700) + t(cx + 136, cy - 12, 'T', BLUE, 14, weight=700)
    body += arrow('symmetry', cx, cy - 46, cx, cy - 108, AMBER, 2.4)
    body += t(cx + 16, cy - 112, 'N', AMBER, 13, 'start', 700)
    body += line(cx, cy + 46, cx, cy + 92, GREY, 2.4) + t(cx, cy + 108, 'mg', GREY, 13, weight=700)
    body += rect(420, 62, 232, 150, '#fbfcff', '#dce4f2', 8)
    body += t(536, 86, 'Reasoning, not algebra', BLUE, 12.5, weight=700)
    lines = ['Mirror symmetry about the', 'vertical axis forbids any', 'left–right net force.',
             '⇒ horizontal components', 'cancel before we solve', 'anything.']
    for i, text_line in enumerate(lines):
        body += t(432, 108 + i * 17, text_line, INK, 11.5, 'start')
    body += t(340, 280, 'Divide by symmetry first: it removes unknowns instead of solving for them.', GREY, 12)
    return wrap('symmetry', 'Symmetry removes unknowns before any calculation',
                'A block under two equal horizontal tensions, its weight and the normal force from the floor.',
                body, caption('Figure 6.', 'Olympiad problems are often built so that one symmetry kills most of the algebra. '
                             'Look for what the configuration cannot distinguish.'), 306)


def lab_units():
    controls = (
        select('units-formula', 'Candidate relation', [(k, v[0]) for k, v in FORMULAE_LAB.items()])
        + slider('units-m', 'Mass exponent you guess', -2, 2, 1, 0)
        + slider('units-l', 'Length exponent you guess', -2, 4, 1, 1)
        + slider('units-t', 'Time exponent you guess', -3, 1, 1, -1)
    )
    return shell(
        'units', 'Dimensional analysis as a searchlight',
        'Each quantity carries powers of mass [M], length [L] and time [T]. Pick a target relation, then dial the '
        'exponents until the dimensions of your guess match it. Only a dimensionless group can equal a pure number.',
        controls,
        [('want', 'Target dimensions'), ('got', 'Your guess'), ('verdict', 'Verdict'), ('pi', 'Dimensionless group')],
        'Choose the mistaken relation: the verdict turns against it immediately. Then set M = 0, L = 3, T = −2 — '
        'which familiar quantity is that? Change one exponent at a time and watch the verdict flip.'
    )


FIGURES = {
    'dimensions': f_dimensions,
    'scaling': f_scaling,
    'taylor': f_taylor,
    'limits': f_limits,
    'fermi': f_fermi,
    'symmetry': f_symmetry,
}

FORMULAE_LAB = {
    'pend': ('pendulum period T = 2π√(L/g)', (0, 0.5, -0.5)),
    'kepler': ('Kepler III  T = 2π√(a³/GM)', (0, 1.5, -1.0)),
    'escape': ('escape speed v = √(2GM/R)', (0, 1.5, -0.5)),
    'wrong': ('a mistaken guess T = 2π√(L·g)', (0, 0.5, 0.5)),
}

LABS = {'units': lab_units}
