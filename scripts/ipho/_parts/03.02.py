"""03.02 Uncertainty analysis."""
from math import sin, cos, pi, sqrt, radians, exp, log10


def f_histogram():
    from math import exp as _exp, sqrt as _sqrt
    def gauss(x, s=1.0):
        return _exp(-x * x / (2 * s * s)) / (_sqrt(2 * pi) * s)
    body = t(340, 24, 'Repeated readings scatter; the mean is the best estimate', INK, 13, weight=700)
    left, right, top, bottom = 110, 620, 62, 228
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda v: left + (v + 4) / 8 * (right - left)
    Y = lambda n: bottom - n * (bottom - top) / 0.45
    # histogram of 20 readings clustered about 0
    bins = [(-3, 1), (-2, 3), (-1, 6), (0, 7), (1, 5), (2, 3), (3, 1)]
    for a, n in bins:
        body += rect(X(a + 0.5), Y(n / 27), (right - left) / 9, Y(0) - Y(n / 27), '#dbeafe', BLUE, 3)
    # fitted gaussian
    pts = [(X(v), Y(0.62 * gauss(v))) for v in [(-4 + 8 * i / 120) for i in range(121)]]
    body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{RED}" stroke-width="2.4"/>'
    body += line(X(0), top + 10, X(0), bottom, AMBER, 1.8, '5 4') + t(X(0) - 8, top + 22, 'mean', AMBER, 11, 'end', 700)
    body += line(X(-1), Y(0.30), X(1), Y(0.30), GREEN, 2.4)
    body += t(X(1) + 6, Y(0.30) - 6, '±σ', GREEN, 11, 'start', 700)
    body += t(340, 276, 'the mean of N readings has uncertainty σ/√N, not σ', GREY, 11.5)
    body += t(340, 300, '68% of readings lie within ±σ, 95% within ±2σ', GREY, 11.5)
    return wrap('histogram', 'A distribution of repeated readings',
                'A histogram of twenty readings with a fitted Gaussian, its mean and its standard deviation.',
                body, caption('Figure 1.', 'The random part of an experiment shows up as a spread. The width of that spread '
                             'is a measurement in its own right: it tells you how precisely you measured, and it shrinks '
                             'as 1/√N when you average.'), 316)


def f_propagation():
    body = t(340, 24, 'Propagation: how an error in x becomes an error in f', INK, 13, weight=700)
    left, right, top, bottom = 110, 620, 64, 230
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    # steep region and its band vs shallow region
    pts = []
    for i in range(121):
        x = 0.15 + 2.7 * i / 120
        y = 1.6 / (1 + 2.2 * x)
        pts.append((left + (x - 0.1) / 2.9 * (right - left), bottom - (y / 1.7) * (bottom - top)))
    body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>'
    for x0, dx, col in ((0.35, 0.16, AMBER), (1.9, 0.16, GREEN)):
        y0 = 1.6 / (1 + 2.2 * x0)
        y1 = 1.6 / (1 + 2.2 * (x0 + dx))
        X = lambda v: left + (v - 0.1) / 2.9 * (right - left)
        Y = lambda v: bottom - (v / 1.7) * (bottom - top)
        body += line(X(x0), Y(y0), X(x0 + dx), Y(y0), col, 2)
        body += line(X(x0), Y(y0), X(x0), Y(y1), col, 2)
        body += t(X(x0 + dx / 2), Y(y0) + 18, 'Δx', col, 11, 'middle', 700)
        body += t(X(x0) - 8, Y((y0 + y1) / 2), 'Δf', col, 11, 'end', 700)
    body += t(340, 262, 'where the graph is steep, a small Δx gives a large Δf; where it is flat, it gives a small one', GREY, 11.5)
    body += t(340, 288, 'Δf ≈ (df/dx)·Δx, added in quadrature for independent sources', GREY, 11.5)
    return wrap('propagation', 'Uncertainty propagation as a slope',
                'A falling curve with two uncertainty boxes, one on a steep part and one on a shallow part.',
                body, caption('Figure 2.', 'The derivative is the exchange rate between an error in the input and an error '
                             'in the output. For a power law it turns the rules into one sentence: fractional errors add, '
                             'multiplied by the exponents.'), 306)


def f_combine():
    from math import sqrt as _sqrt
    return chart(
        'combine', 'Adding independent uncertainties in quadrature',
        'Two equal uncertainties combine to 1.41 times one of them, not twice.',
        'ratio of the two uncertainties  Δy/Δx', 'combined / larger one',
        [('quadrature', BLUE, lambda r: _sqrt(1 + r * r)),
         ('worst case (linear)', AMBER, lambda r: 1 + r)],
        xr=(0, 2), yr=(0, 3.05), xticks=(0.5, 1, 1.5, 2), yticks=(1, 2, 3), height=350,
        xfmt='{:.1f}', yfmt='{:.0f}',
        notes=[(0.08, 2.6, 'quadrature is the honest estimate for random errors', GREY)])


def f_slope():
    body = t(340, 24, 'A best-fit line through scattered points: the gradient is the measurement', INK, 13, weight=700)
    left, right, top, bottom = 110, 620, 62, 232
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    pts = [(0.1, 0.12), (0.18, 0.25), (0.26, 0.22), (0.34, 0.42), (0.42, 0.38),
           (0.52, 0.55), (0.60, 0.52), (0.70, 0.72), (0.80, 0.68), (0.90, 0.86)]
    X = lambda x: left + x * (right - left)
    Y = lambda y: bottom - y * (bottom - top)
    body += line(X(0.05), Y(0.08), X(0.95), Y(0.90), RED, 2.4)
    body += line(X(0.05), Y(0.13), X(0.95), Y(0.83), RED, 1.2, '5 4')
    body += line(X(0.05), Y(0.03), X(0.95), Y(0.97), RED, 1.2, '5 4')
    for x, y in pts:
        body += dot(X(x), Y(y), 4, BLUE)
        # error bars
        body += line(X(x), Y(y - 0.04), X(x), Y(y + 0.04), BLUE, 1.2)
    body += t(X(0.9) - 6, Y(0.80) + 16, 'best fit', RED, 11, 'end', 700)
    body += t(340, 262, 'gradient = Δy/Δx from the line, never from two scattered points', GREY, 11.5)
    body += t(340, 288, 'the dashed lines show the steepest and shallowest lines consistent with the error bars', GREY, 11.5)
    return wrap('best-fit', 'A graph with a best-fit line',
                'Scattered points with vertical error bars and a straight line of best fit with uncertainty lines.',
                body, caption('Figure 3.', 'Drawing the line is a way of averaging all the points with proper weights. '
                             'The intercept often carries physics too: a non-zero intercept where theory demands zero is a '
                             'systematic error.'), 306)


def f_abs_vs_rel():
    body = t(340, 24, 'Absolute and relative uncertainty', INK, 13, weight=700)
    rows = [('L = 25.00 m', '± 0.05 m', '0.2 %'),
            ('L = 2.500 m', '± 0.005 m', '0.2 %'),
            ('L = 0.025 m', '± 0.005 m', '20 %'),
            ('t = 120.0 s', '± 0.2 s', '0.17 %'),
            ('t = 1.2 s', '± 0.2 s', '17 %')]
    body += t(120, 76, 'measurement', GREY, 11, 'start', 700)
    body += t(320, 76, 'absolute', GREY, 11, 'start', 700)
    body += t(460, 76, 'relative', GREY, 11, 'start', 700)
    for i, (a, b, c) in enumerate(rows):
        y = 100 + i * 28
        body += rect(110, y - 16, 470, 26, '#f8fafc' if i % 2 == 0 else '#ffffff', '#e2e8f0', 3)
        body += t(120, y + 3, a, INK, 11, 'start', 700)
        body += t(320, y + 3, b, BLUE, 11, 'start')
        body += t(460, y + 3, c, AMBER if c.startswith('1') or c.startswith('2') else GREY, 11, 'start')
    body += t(340, 270, 'a small object measured with a good instrument can still have a poor relative uncertainty', GREY, 11.5)
    body += t(340, 300, 'quote absolute uncertainty for a single value, relative when combining measurements', GREY, 11.5)
    return wrap('absolute-relative', 'Absolute versus relative uncertainty',
                'A table of measurements with their absolute and percentage uncertainties.',
                body, caption('Figure 4.', 'The same absolute uncertainty can be negligible or fatal depending on the size '
                             'of the quantity. That is why the choice of instrument must be matched to the size of what you '
                             'are measuring.'), 320)


FIGURES = {
    'histogram': f_histogram,
    'propagation': f_propagation,
    'combine': f_combine,
    'best-fit': f_slope,
    'absolute-relative': f_abs_vs_rel,
}


def lab_uncertainty():
    controls = (
        slider('unc-a', 'Measurement a', 0.1, 100, 0.1, 20.0, ' [m]')
        + slider('unc-da', 'Uncertainty in a', 0.01, 5.0, 0.01, 0.2, ' [m]')
        + slider('unc-n', 'Power n in f = aⁿ', 1, 3, 1, 2, '')
    )
    return shell(
        'uncertainty', 'Propagation through a power law',
        'For f = aⁿ the relative uncertainty is |n| times the relative uncertainty in a. The experiment shows the value, '
        'the absolute uncertainty and the number of significant figures you should quote, for any a, Δa and n.',
        controls,
        [('f', 'Value of f'), ('df', 'Absolute uncertainty'), ('rel', 'Relative uncertainty'),
         ('quoted', 'Correctly quoted result'), ('digits', 'Significant figures justified')],
        'Make the uncertainty in a 10% and look at f = a³. How many digits are justified? Then reduce Δa to 1% and see '
        'how the quoted result changes.'
    )


LABS = {'uncertainty': lab_uncertainty}
