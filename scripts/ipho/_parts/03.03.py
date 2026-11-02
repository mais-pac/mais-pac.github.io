"""03.03 Data analysis and linear fitting."""
from math import sin, cos, pi, sqrt, radians, exp, log10, log


def f_linearise():
    body = t(340, 24, 'Linearisation turns a curve into a straight line you can measure', INK, 13, weight=700)
    # left: the curve, right: the linearised plot
    body += rect(80, 74, 220, 150, '#f8fafc', '#e2e8f0', 5) + rect(380, 74, 220, 150, '#f8fafc', '#e2e8f0', 5)
    body += t(190, 64, 'raw data: curve', GREY, 11, weight=700)
    body += t(490, 64, 'linearised: straight', GREY, 11, weight=700)
    pts = []
    for i in range(1, 60):
        L = 0.1 + 0.9 * i / 58
        T = 2 * pi * sqrt(L / 9.81)
        pts.append((80 + (L / 1.0) * 220, 224 - (T / 2.05) * 145))
    body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{BLUE}" stroke-width="2.4"/>'
    pts = []
    for i in range(0, 60):
        L = 0.1 + 0.9 * i / 59
        T2 = 4 * pi * pi * L / 9.81
        pts.append((380 + (L / 1.0) * 220, 224 - (T2 / 4.1) * 145))
    body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{GREEN}" stroke-width="2.4"/>'
    body += t(190, 244, 'T against L', GREY, 11)
    body += t(490, 244, 'T² against L: gradient 4π²/g', GREY, 11)
    body += t(340, 286, 'plot the combination that theory says is linear, then measure its gradient', GREY, 11.5)
    return wrap('linearise', 'Linearising data',
                'A square-root curve next to the same data plotted so that it lies on a straight line.',
                body, caption('Figure 1.', 'A gradient can be measured with a ruler and compared with theory; a curvature '
                             'cannot. Linearising is the single most valuable data-handling skill in the practical exam.'), 306)


def f_residuals():
    body = t(340, 24, 'Residuals: the vertical gaps between the points and the line', INK, 13, weight=700)
    left, right, top, bottom = 100, 620, 62, 236
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    pts = [(0.10, 0.14), (0.20, 0.22), (0.30, 0.36), (0.40, 0.39), (0.50, 0.52),
           (0.60, 0.58), (0.70, 0.72), (0.80, 0.78), (0.90, 0.91)]
    X = lambda x: left + x * (right - left)
    Y = lambda y: bottom - y * (bottom - top)
    # least squares fit y = 0.95x + 0.02
    body += line(X(0.05), Y(0.96 * 0.05 + 0.02), X(0.95), Y(0.96 * 0.95 + 0.02), RED, 2.2)
    for x, y in pts:
        b = 0.96 * x + 0.02
        body += line(X(x), Y(y), X(x), Y(b), '#f59e0b', 1.6, '4 3')
        body += dot(X(x), Y(y), 4.5, BLUE)
    body += t(340, 262, 'the best line minimises the sum of the squared residuals — hence "least squares"', GREY, 11.5)
    body += t(340, 288, 'a systematic pattern in the residuals means the model is wrong, not the data', GREY, 11.5)
    return wrap('residuals', 'Residuals of a straight-line fit',
                'Data points with vertical residual segments drawn to the best-fit line.',
                body, caption('Figure 2.', 'If the residuals wander systematically — all positive at one end, all '
                             'negative at the other — a straight line is the wrong model, or there is a systematic error '
                             'in one of the variables.'), 306)


def f_uncertainty_slope():
    body = t(340, 24, 'Which points pin down the gradient most strongly?', INK, 13, weight=700)
    left, right, top, bottom = 100, 620, 64, 232
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x * (right - left)
    Y = lambda y: bottom - y * (bottom - top)
    # a tight cluster in the middle gives a poorly determined slope
    for i, (x, y) in enumerate(((0.35, 0.42), (0.45, 0.52), (0.55, 0.58), (0.62, 0.66))):
        body += dot(X(x), Y(y), 4.5, RED)
        body += line(X(x), Y(y - 0.05), X(x), Y(y + 0.05), RED, 1.2)
    body += line(X(0.30), Y(0.30), X(0.70), Y(0.68), RED, 2)
    body += line(X(0.30), Y(0.42), X(0.70), Y(0.76), '#fca5a5', 1.4, '5 4')
    body += line(X(0.30), Y(0.18), X(0.70), Y(0.60), '#fca5a5', 1.4, '5 4')
    # widely spread points
    for i, (x, y) in enumerate(((0.08, 0.14), (0.26, 0.30), (0.55, 0.60), (0.92, 0.96))):
        body += dot(X(x), Y(y), 4.5, BLUE)
        body += line(X(x), Y(y - 0.03), X(x), Y(y + 0.03), BLUE, 1.2)
    body += line(X(0.05), Y(0.10), X(0.95), Y(0.99), BLUE, 2)
    body += t(left + 10, bottom + 24, 'clustered: uncertain', RED, 11, 'start', 700)
    body += t(right - 10, bottom + 24, 'spread points: well set', BLUE, 11, 'end', 700)
    body += t(340, 282, 'to measure a gradient well, span the whole range: more points help, but range helps more', GREY, 11.5)
    return wrap('span', 'Spread of readings and the precision of a gradient',
                'A tight cluster of points with a poorly determined line beside widely spread points with a well determined one.',
                body, caption('Figure 3.', 'This is why an experiment sweeps the full range: ten points in a narrow interval '
                             'determine a gradient worse than three points spread across the whole scale.'), 312)


def f_log_plot():
    from math import log10 as _log10
    def lin(x):
        return 2.0 - 1.5 * x
    return chart(
        'log-plot', 'A power law becomes a straight line on a log–log plot',
        'If y = a·xⁿ then log y = log a + n log x: the gradient is the exponent n and the intercept is log a.',
        'log₁₀ x', 'log₁₀ y',
        [('n = −1.5', BLUE, lin)],
        xr=(0, 2), yr=(-1.2, 2.2), xticks=(0.5, 1, 1.5, 2), yticks=(-1, 0, 1, 2), height=350,
        xfmt='{:.1f}', yfmt='{:.0f}')


def f_error_bars():
    body = t(340, 24, 'Error bars decide whether a trend is real', INK, 13, weight=700)
    left, right, top, bottom = 100, 620, 64, 232
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x * (right - left)
    Y = lambda y: bottom - y * (bottom - top)
    for i in range(6):
        x = 0.12 + 0.14 * i
        y = 0.10 + 0.15 * i + (0.02 if i % 2 else -0.02)
        body += dot(X(x), Y(y), 4.5, BLUE)
        body += line(X(x), Y(y - 0.045), X(x), Y(y + 0.045), BLUE, 1.4)
        body += line(X(x) - 6, Y(y - 0.045), X(x) + 6, Y(y - 0.045), BLUE, 1.4)
        body += line(X(x) - 6, Y(y + 0.045), X(x) + 6, Y(y + 0.045), BLUE, 1.4)
    body += line(X(0.05), Y(0.04), X(0.95), Y(0.90), RED, 2.2)
    body += t(340, 262, 'the line must pass through every error bar, or the model is excluded', GREY, 11.5)
    body += t(340, 288, 'error bars also show which points deserve the most weight in the fit', GREY, 11.5)
    return wrap('error-bars', 'Error bars and the line of best fit',
                'Six points with vertical error bars and a line that threads through all the bars.',
                body, caption('Figure 4.', 'Without error bars there is no way to tell a real deviation from scatter. '
                             'Drawing them forces you to think about the uncertainty of every point, which is where most '
                             'of the physics of a practical question actually lies.'), 306)


FIGURES = {
    'linearise': f_linearise,
    'residuals': f_residuals,
    'span': f_uncertainty_slope,
    'log-plot': f_log_plot,
    'error-bars': f_error_bars,
}


def lab_fit():
    controls = (
        slider('fit-slope', 'True gradient', 0.2, 3.0, 0.1, 1.4, '')
        + slider('fit-int', 'True intercept', -1.0, 2.0, 0.1, 0.4, '')
        + slider('fit-noise', 'Scatter of the data', 0.01, 0.40, 0.01, 0.12, '')
        + slider('fit-n', 'Number of points', 3, 20, 1, 7, '')
    )
    return shell(
        'fit', 'Least-squares fitting',
        'The experiment generates data from a known straight line with a chosen amount of scatter, fits the best line by '
        'least squares and compares the fitted gradient and intercept with the true values. Repeated, it shows how the '
        'uncertainty of the gradient shrinks as the scatter falls or the number of points grows.',
        controls,
        [('m', 'Fitted gradient'), ('c', 'Fitted intercept'), ('r2', 'Coefficient of determination R²'),
         ('dm', 'Uncertainty in the gradient'), ('verdict', 'Is the fit consistent?')],
        'Keep the gradient fixed and increase the scatter: what happens to R² and to the uncertainty of the gradient? '
        'Then increase the number of points and compare.'
    )


LABS = {'fit': lab_fit}
