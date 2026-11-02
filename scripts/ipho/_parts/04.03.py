"""04.03 Calculus."""
from math import sin, cos, pi, sqrt, radians, exp, log10, log, atan2


def f_derivative():
    body = t(340, 24, 'The derivative is the gradient of the tangent, and the limit of a chord', INK, 13, weight=700)
    left, right, top, bottom = 96, 596, 58, 232
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x / 3.0 * (right - left)
    Y = lambda y: bottom - y / 9.0 * (bottom - top)
    for v in (1, 2, 3):
        body += t(X(v), bottom + 19, f'{v}', GREY, 11)
    for v in (3, 6, 9):
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 11, 'end')
    body += t((left + right) / 2, bottom + 40, 't / s', GREY, 12)
    body += f'<g transform="translate(40,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 's / m', GREY, 12) + '</g>'
    f = lambda x: x * x
    pts = [(X(0.02 + 2.96 * i / 200), Y((0.02 + 2.96 * i / 200) ** 2)) for i in range(201)]
    body += polyline(pts, BLUE, 2.8)
    # tangents at t=1 and t=2
    for t0, col in ((1.0, GREEN), (2.0, RED)):
        slope = 2 * t0
        p1 = (t0 - 0.45, t0 * t0 - slope * 0.45)
        p2 = (t0 + 0.45, t0 * t0 + slope * 0.45)
        body += line(X(p1[0]), Y(p1[1]), X(p2[0]), Y(p2[1]), col, 2.0)
        body += dot(X(t0), Y(t0 * t0), 4.5, col)
        body += t(X(t0 + 0.30), Y(t0 * t0 + slope * 0.30) + 20, f'gradient {2 * t0:.0f}', col, 11, 'start', 700)
    # a chord
    t1, t2 = 1.4, 2.3
    body += line(X(t1), Y(t1 * t1), X(t2), Y(t2 * t2), AMBER, 1.8, '5 4')
    body += dot(X(t1), Y(t1 * t1), 4, AMBER) + dot(X(t2), Y(t2 * t2), 4, AMBER)
    body += t(X(1.85), Y(5.9), 'chord: average gradient', AMBER, 11, 'middle', 700)
    body += t(X(0.35), Y(7.6), 's = t²', BLUE, 12.5, 'start', 700)
    body += t(340, 286, 'shrink the chord until its ends merge: the average gradient becomes the tangent gradient',
              GREY, 11.5)
    return wrap('derivative', 'A derivative as the limit of a chord',
                'A parabola with two tangents and one chord drawn, showing the chord approaching the tangent.',
                body, caption('Figure 1.', 'The derivative is local information: it says how fast the quantity is changing '
                             'at one instant, not on average. That is exactly what Newton’s second law needs.'), 306)


def f_integral():
    body = t(340, 24, 'An integral is a sum of thin strips — and the area under a graph', INK, 13, weight=700)
    left, right, top, bottom = 96, 596, 58, 226
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x / 3.0 * (right - left)
    Y = lambda y: bottom - y / 10.0 * (bottom - top)
    f = lambda x: 2 + 6 * x * x / 9.0 + 2 * sin(2 * x)
    n = 10
    for i in range(n):
        x0, x1 = 0.1 + 2.9 * i / n, 0.1 + 2.9 * (i + 1) / n
        h = f((x0 + x1) / 2)
        body += rect(X(x0), Y(h), X(x1) - X(x0), Y(0) - Y(h), '#dbeafe', '#93b4e8', 0, 1.0)
    pts = [(X(0.1 + 2.9 * i / 240), Y(f(0.1 + 2.9 * i / 240))) for i in range(241)]
    body += polyline(pts, BLUE, 2.6)
    body += t(X(2.55), Y(f(2.55)) - 16, 'f(t)', BLUE, 12, 'start', 700)
    body += t(X(1.5), Y(1.2), 'total = Σ height × width', INK, 12, 'middle', 700)
    body += t(X(1.5), Y(0.35), '→ ∫ f dt as the strips narrow', GREY, 11, 'middle')
    body += t((left + right) / 2, bottom + 40, 't', GREY, 12)
    body += t(340, 258, 'the area means whatever the product of the axes means: a velocity-time area is a distance', GREY, 11.5)
    body += t(340, 284, 'an integral accumulates; a derivative measures the rate of accumulation', GREY, 11.5)
    return wrap('integral', 'An integral as a sum of strips',
                'The area under a curve filled with ten thin rectangles whose tops follow the curve.',
                body, caption('Figure 2.', 'Splitting a quantity into small pieces and adding them is the physical '
                             'definition of an integral. The calculus is only a way of taking the limit exactly.'), 306)


def f_exponential():
    body = t(340, 24, 'The exponential is its own derivative, which is why it describes decay', INK, 13, weight=700)
    left, right, top, bottom = 96, 620, 58, 216
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x / 5.0 * (right - left)
    Y = lambda y: bottom - y / 1.05 * (bottom - top)
    for v in (0, 1, 2, 3, 4, 5):
        body += t(X(v), bottom + 19, f'{v}', GREY, 11)
    for v in (0.5, 1.0):
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 11, 'end')
    body += t((left + right) / 2, bottom + 40, 't / τ', GREY, 12)
    body += f'<g transform="translate(40,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'N / N₀', GREY, 12) + '</g>'
    pts = [(X(5 * i / 200), Y(exp(-5 * i / 200))) for i in range(201)]
    body += polyline(pts, BLUE, 2.8)
    body += line(X(1), Y(exp(-1)) + 6, X(1), Y(0), RED, 1.6, '5 4')
    body += dot(X(1), Y(exp(-1)), 4.5, RED)
    body += t(X(1) + 10, Y(exp(-1)) - 8, 'half at t = 0.69τ', RED, 11, 'start', 700)
    body += t(X(2.55), Y(0.30), 'slope at t = 0 is −N₀/τ', GREY, 11, 'start')
    body += line(X(0), Y(1.0), X(1.0), Y(0), GREEN, 1.8, '6 4')
    body += t(X(0.30), Y(0.50), 'tangent', GREEN, 10.5, 'start', 700)
    body += t(340, 288, 'equal drops in equal times, but the drops shrink as the quantity shrinks', GREY, 11.5)
    return wrap('exponential', 'The exponential decay curve',
                'An exponentially decaying curve with its initial tangent and its half-value marked.',
                body, caption('Figure 3.', 'Anything whose rate of loss is proportional to what remains follows this '
                             'curve: radioactive nuclei, a cooling body, a discharging capacitor, a drug in the blood.'), 312)


def f_chain():
    body = t(340, 24, 'The chain rule: a rate multiplied by a rate', INK, 13, weight=700)
    body += box(70, 74, 150, 74, 'x changes|at 3 per s', '#f8fafc', GREY, 11.5)
    body += box(272, 74, 150, 74, 'y depends on x|y = x²', PALE, BLUE, 11.5)
    body += box(474, 74, 150, 74, 'y changes at|2x × 3 per s', '#f0fdf7', GREEN, 11.5)
    body += arrow('chain', 222, 111, 268, 111, GREY, 2.2)
    body += arrow('chain2', 424, 111, 470, 111, GREY, 2.2)
    body += t(340, 58, 'differentiate the outside, then the inside', GREY, 11.5)
    body += t(340, 184, 'dy/dt = (dy/dx)(dx/dt) = 2x · 3', INK, 13, 700)
    body += t(340, 214, 'at x = 4: dy/dt = 8 × 3 = 24 per s', BLUE, 12)
    body += t(340, 240, 'almost every physical formula is a chain: force depends on radius, radius on time', GREY, 11)
    return wrap('chain', 'The chain rule as a chain of rates',
                'Three boxes linked by arrows showing how a rate in x becomes a rate in y.',
                body, caption('Figure 4.', 'The chain rule is the workhorse of related-rates problems: a balloon '
                             'inflating, a shadow lengthening, a satellite losing altitude. Write the chain, then '
                             'substitute.'), 268)


def f_series():
    body = t(340, 24, 'A Taylor series replaces a curve by a polynomial near a point', INK, 13, weight=700)
    left, right, top, bottom = 100, 560, 56, 200
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + (x + 3.0) / 6.0 * (right - left)
    Y = lambda y: bottom - (y + 2.0) / 4.0 * (bottom - top)
    for v in (-2, -1, 1, 2):
        body += t(X(v), bottom + 18, f'{v}', GREY, 10.5)
    body += line(left, Y(0), right, Y(0), LIGHT, 1.2)
    body += t((left + right) / 2, bottom + 38, 'x', GREY, 12)
    body += f'<g transform="translate(46,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'f(x)', GREY, 12) + '</g>'
    f = lambda x: sin(x)
    body += polyline([(X(-3 + 6 * i / 240), Y(f(-3 + 6 * i / 240))) for i in range(241)], INK, 2.8)
    body += line(X(-3), Y(-3), X(3), Y(3), BLUE, 2.0, '7 5')
    cubic = []
    for i in range(241):
        xx = -3 + 6 * i / 240
        yy = xx - xx ** 3 / 6
        if -1.9 <= yy <= 1.9:
            cubic.append((X(xx), Y(yy)))
    body += polyline(cubic, GREEN, 2.2, '7 5')
    body += t(X(-2.9), Y(-1.55), 'sin x', INK, 11.5, 'start', 700)
    body += t(X(-1.9), Y(-1.05), 'x', BLUE, 11.5, 'start', 700)
    body += t(X(-0.55), Y(1.85), 'x − x³/6', GREEN, 11.5, 'start', 700)
    body += t(340, 290, 'near the origin one term is enough; farther out you need the next term, then the next', GREY, 11.5)
    return wrap('series', 'A Taylor series and its truncation',
                'A sine curve with its linear and cubic approximations overlapping it near the origin.',
                body, caption('Figure 5.', 'A Taylor series is not an approximation to be ashamed of — it is how '
                             'small-angle motion, the linear regime of a spring, and almost every "small quantity" '
                             'argument in physics are justified.'), 322)


FIGURES = {
    'derivative': f_derivative,
    'integral': f_integral,
    'exponential': f_exponential,
    'chain': f_chain,
    'series': f_series,
}


def lab_calculus():
    controls = (
        slider('calc-a', 'Amplitude A', 0.2, 2.0, 0.1, 1.0, '')
        + slider('calc-w', 'Angular frequency ω', 0.2, 1.5, 0.1, 0.6, '')
        + slider('calc-t0', 'Time t (marker)', 0.0, 12.0, 0.1, 4.0, 's')
    )
    return shell(
        'calc', 'Displacement, gradient and area',
        'A sinusoidal displacement is drawn with its gradient (derivative) and its running area (integral) beneath. '
        'The marker slides along the time axis so you can see that the gradient is the slope of the tangent and the '
        'area is the accumulated displacement.',
        controls,
        [('y', 'Displacement y'), ('dy', 'Gradient dy/dt'), ('area', 'Area under y up to t'),
         ('peak', 'Velocity amplitude ωA'), ('when', 'First maximum of y')],
        'Put the marker at a peak of y: what is the gradient there? Put it where y crosses zero and compare the '
        'gradient with ωA.'
    )


LABS = {'calc': lab_calculus}
