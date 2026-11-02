"""04.04 Approximation, Taylor series and numerical methods."""
from math import sin, cos, pi, sqrt, radians, exp, log10, log, atan2


def f_small():
    body = t(340, 24, 'Small-angle physics: the linear regime is where the equations are solvable', INK, 13, weight=700)
    left, right, top, bottom = 110, 420, 62, 226
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda a: left + a / 1.3 * (right - left)
    Y = lambda v: bottom - v / 1.3 * (bottom - top)
    for a in (0.5, 1.0, 1.3):
        body += t(X(a), bottom + 19, f'{a:.2f}', GREY, 10.5)
    body += t((left + right) / 2, bottom + 34, 'angle θ / rad', GREY, 11.5)
    pts_s = [(X(1.3 * i / 120), Y(sin(1.3 * i / 120))) for i in range(121)]
    body += polyline(pts_s, BLUE, 2.6)
    body += line(X(0), Y(0), X(1.3), Y(1.3), GREEN, 2.2, '7 5')
    pts_c = [(X(1.3 * i / 120), Y(1 - (1.3 * i / 120) ** 2 / 2)) for i in range(121)]
    body += polyline(pts_c, PURPLE, 2.0, '2 4')
    body += t(X(0.78), Y(0.86), 'sin θ', BLUE, 11.5, 'start', 700)
    body += t(X(1.05), Y(1.02), 'θ', GREEN, 11.5, 'start', 700)
    body += t(X(0.62), Y(0.30), 'cos θ ≈ 1 − θ²/2', PURPLE, 11, 'start', 700)
    body += box(446, 74, 210, 128, 'θ → 0:  sin θ ≈ θ|tan θ ≈ θ|cos θ ≈ 1 − θ²/2|(1+ε)^n ≈ 1 + nε|1/(1+ε) ≈ 1 − ε', '#f8fafc', GREY, 10.5)
    body += t(340, 276, 'the error in sin θ ≈ θ is θ³/6: 0.13% at 0.2 rad', GREY, 11.5)
    body += t(340, 298, 'linearise only when the neglected term is far below the precision you claim', GREY, 11.5)
    return wrap('small', 'Small-angle approximations',
                'The sine curve, the identity line and the quadratic cosine approximation near the origin.',
                body, caption('Figure 1.', 'Approximation is not sloppiness: it is the deliberate discarding of a term '
                             'you can bound. The bound is what makes the answer defensible, and quoting it is what earns '
                             'the mark.'), 312)


def f_iteration():
    body = t(340, 24, 'Iteration: feed the answer back in until the digits stop changing', INK, 13, weight=700)
    left, right, top, bottom = 110, 560, 118, 226
    body += line(left, bottom, right, bottom, GREY, 1.6)
    body += line(left, bottom, left, top, GREY, 1.4)
    body += t((left + right) / 2, bottom + 38, 'iteration number n', GREY, 11.5)
    body += f'<g transform="translate(56,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'value of xₙ', GREY, 11.5) + '</g>'
    xs = [1.0]
    for i in range(9):
        xs.append(0.5 * (xs[-1] + 2.0 / xs[-1]))
    X = lambda i: left + i / 9.0 * (right - left)
    Yv = lambda v: bottom - (v - 1.38) / 0.07 * (bottom - top)
    target = sqrt(2)
    body += line(left, Yv(target), right, Yv(target), RED, 1.4, '5 4')
    body += t(right - 4, Yv(target) - 8, 'exact √2', RED, 11, 'end', 700)
    for i in range(9):
        body += dot(X(i + 1), Yv(max(1.39, min(1.45, xs[i + 1]))), 4.5, BLUE)
        if i < 8:
            body += line(X(i + 1), Yv(max(1.39, min(1.45, xs[i + 1]))), X(i + 2), Yv(max(1.39, min(1.45, xs[i + 2]))), BLUE, 1.6)
    body += t(X(1.0), Yv(1.44) + 4, 'x₁ = 1', BLUE, 10.5, 'start')
    body += box(576, 96, 88, 100, 'x₀ = 1|x₁ = 1.5|x₂ = 1.4167|x₃ = 1.4142', '#f0fdf7', GREEN, 10)
    body += t(340, 278, 'each step roughly doubles the number of correct digits', GREY, 11.5)
    body += t(340, 300, 'the fixed point is where the curve crosses the line y = x', GREY, 11.5)
    return wrap('iteration', 'Convergence of an iterative method',
                'Successive iterates of the Newton square-root method converging on the exact value.',
                body, caption('Figure 2.', 'Numerical methods replace an algebraic solution by a sequence of better '
                             'guesses. The two questions to ask are always: does it converge, and how fast — because a '
                             'method that converges is useless if it needs a million steps.'), 314)


def f_error():
    body = t(340, 24, 'Two kinds of numerical error, and the step size that balances them', INK, 13, weight=700)
    left, right, top, bottom = 110, 600, 62, 226
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda h: left + (log10(h) + 7) / 6.0 * (right - left)
    Y = lambda e: bottom - (log10(e) + 8) / 7.0 * (bottom - top)
    for dec in (-7, -5, -3, -1):
        body += t(X(10 ** dec), bottom + 19, f'10^{dec}', GREY, 10.5)
    for dec in (-8, -6, -4, -2):
        body += t(left - 8, Y(10 ** dec) + 4, f'10^{dec}', GREY, 10.5, 'end')
    body += t((left + right) / 2, bottom + 36, 'step size h', GREY, 11.5)
    body += f'<g transform="translate(52,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'error', GREY, 11.5) + '</g>'
    def clipped(fn):
        pts = []
        for i in range(161):
            h = 10 ** (-7 + 6 * i / 160)
            e = fn(h)
            if 1e-8 <= e <= 1e-1:
                pts.append((X(h), Y(e)))
        return polyline(pts, BLUE, 2.4)
    body += polyline([(X(10 ** (-7 + 6 * i / 160)), Y(10 ** (-7 + 6 * i / 160)))
                      for i in range(161) if 1e-8 <= 10 ** (-7 + 6 * i / 160) <= 1e-1], BLUE, 2.4)
    body += polyline([(X(10 ** (-7 + 6 * i / 160)), Y(1e-8 / 10 ** (-7 + 6 * i / 160)))
                      for i in range(161) if 1e-8 <= 1e-8 / 10 ** (-7 + 6 * i / 160) <= 1e-1], RED, 2.4)
    body += dot(X(1e-4), Y(1e-4), 5.5, GREEN)
    body += line(X(1e-4), Y(1e-4), X(1e-4), bottom, GREEN, 1.2, '4 3')
    body += t(X(1e-4) + 10, Y(1e-4) - 14, 'best h', GREEN, 11, 'start', 700)
    body += t(X(2e-7), Y(3e-8), 'round-off ∝ 1/h', RED, 11, 'start', 700)
    body += t(X(2e-6), Y(2e-3), 'truncation ∝ h', BLUE, 11, 'start', 700)
    body += t(340, 288, 'a smaller step is not always better: differences of nearly equal numbers destroy digits', GREY, 11.5)
    return wrap('error', 'Truncation error against round-off error',
                'Two error curves crossing on log-log axes at an optimal step size.',
                body, caption('Figure 3.', 'Every numerical estimate trades a truncation error, which falls with a finer '
                             'step, against a round-off error, which grows as the step shrinks and differences of nearly '
                             'equal numbers lose significant digits. The crossing point is the best step.'), 306)


def f_limitcheck():
    body = t(340, 24, 'Checking an answer by its limiting cases', INK, 13, weight=700)
    cases = [
        ('m₂ ≫ m₁', 'a → g', 'heavy mass free-falls'),
        ('m₁ = m₂', 'a = 0', 'strings balance'),
        ('m₁ → 0', 'T → 0', 'light mass cannot pull'),
        ('θ → 0', 'N → mg', 'flat floor'),
    ]
    y = 74
    for left_label, mid, right_label in cases:
        body += box(70, y, 150, 54, left_label, PALE, BLUE, 11.5)
        body += arrow('lim', 224, y + 27, 262, y + 27, GREY, 2)
        body += box(266, y, 148, 54, mid, '#f0fdf7', GREEN, 12)
        body += arrow('lim2', 418, y + 27, 456, y + 27, GREY, 2)
        body += box(460, y, 190, 54, right_label, '#f8fafc', GREY, 11)
        y += 66
    body += t(340, 62, 'general result → special case → physically obvious answer', GREY, 11.5)
    body += t(340, 348, 'if a limit gives nonsense, the algebra is wrong — this catches more errors than dimensional analysis alone',
              GREY, 11.5)
    return wrap('limitcheck', 'Testing a general result in limiting cases',
                'A table of parameter limits mapped to the physical answer each should give.',
                body, caption('Figure 4.', 'A general formula must reproduce the obvious special cases. Checking two or '
                             'three limits takes twenty seconds and catches most sign errors and inverted factors.'), 366)


def f_estimate():
    body = t(340, 24, 'Order-of-magnitude estimation: the first answer, to one digit', INK, 13, weight=700)
    steps = [
        ('what is asked', 'how many', ''),
        ('model it', 'a simple shape', ''),
        ('one dimension', 'measure or recall', ''),
        ('powers of ten', 'round hard', ''),
        ('one digit', 'answer ± factor 3', ''),
    ]
    x = 60
    for i, (head, detail, _) in enumerate(steps):
        fill = '#f0fdf7' if i == len(steps) - 1 else PALE
        stroke = GREEN if i == len(steps) - 1 else BLUE
        body += box(x, 82, 106, 92, head + '|' + detail, fill, stroke, 10.5)
        if i < len(steps) - 1:
            body += arrow('est', x + 108, 128, x + 122, 128, GREY, 1.8, head=7)
        x += 124
    body += t(340, 62, 'the aim is the exponent, not the digits', GREY, 11.5)
    body += t(340, 202, 'example: people in a city × water used per person per day × days', GREY, 11.5)
    body += t(340, 228, '≈ 10⁶ × 10² L × 1 ≈ 10⁸ litres a day — good to a factor of a few', INK, 11.5)
    body += t(340, 258, 'state the assumptions, because they dominate the uncertainty', GREY, 11)
    body += t(340, 284, 'an estimate is a physics argument in miniature: model, data, result', GREY, 11)
    return wrap('estimate', 'The estimation pipeline',
                'Five boxes in a row tracing an order-of-magnitude estimate from question to answer.',
                body, caption('Figure 5.', 'Fermi estimation is examined because it reveals physical intuition. The '
                             'grader wants the model, the numbers and the exponent — and a comment on which assumption '
                             'dominates the error.'), 306)


FIGURES = {
    'small': f_small,
    'iteration': f_iteration,
    'error': f_error,
    'limitcheck': f_limitcheck,
    'estimate': f_estimate,
}


def lab_approximation():
    controls = (
        slider('apx-x', 'Value of x', 0.0, 1.4, 0.01, 0.30, 'rad')
    )
    return shell(
        'apx', 'How good is the small-angle approximation?',
        'Compare sin x, tan x and cos x with their leading approximations at a chosen angle, and read off the '
        'fractional error and the size of the first neglected term.',
        controls,
        [('sinx', 'sin x'), ('approx', 'x'), ('err', 'Error in sin x ≈ x'), ('rel', 'Relative error'),
         ('cosx', 'cos x'), ('cosapprox', '1 − x²/2'), ('cube', 'θ³/6 term'), ('verdict', 'Verdict')],
        'Increase x until the relative error reaches 1%. Is x then closer to 0.1, 0.2 or 0.3 rad? Compare that with '
        'the size of the first neglected term.'
    )


LABS = {'apx': lab_approximation}
