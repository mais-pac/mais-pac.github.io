"""04.01 Algebra, functions and geometry."""
from math import sin, cos, pi, sqrt, radians, exp, log10, log, atan2


def f_functions():
    body = t(340, 24, 'Three functions that every olympiad problem is built from', INK, 13, weight=700)
    left, right, top, bottom = 96, 620, 54, 232
    body += grid((left, top, right, bottom), 4, 4)
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x / 2.0 * (right - left)
    Y = lambda y: bottom - y / 4.0 * (bottom - top)
    for v in (0.5, 1.0, 1.5):
        body += line(X(v), bottom, X(v), bottom + 6, GREY, 1.4)
        body += t(X(v), bottom + 19, f'{v:.1f}', GREY, 11)
    for v in (1, 2, 3, 4):
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 11, 'end')
        body += line(left - 6, Y(v), left, Y(v), GREY, 1.4)
    body += t((left + right) / 2, bottom + 40, 'x', GREY, 12)
    body += t(44, (top + bottom) / 2, 'y', GREY, 12)
    # the three curves
    pts = [(X(0.02 + 1.96 * i / 120), Y((0.02 + 1.96 * i / 120) ** 2)) for i in range(121)]
    body += polyline(pts, BLUE, 2.6)
    body += line(X(0), Y(0), X(2), Y(2), GREEN, 2.6)
    pts = [(X(1.98 * i / 120), Y(sqrt(1.98 * i / 120))) for i in range(121)]
    body += polyline(pts, PURPLE, 2.6)
    body += t(X(1.42), Y(3.55), 'y = x²', BLUE, 12, 'start', 700)
    body += t(X(1.60), Y(1.05), 'y = x', GREEN, 12, 'start', 700)
    body += t(X(0.10), Y(2.55), 'y = √x', PURPLE, 12, 'start', 700)
    body += t(340, 286, 'power laws, straight lines and square roots: sketch their shapes until they are automatic',
              GREY, 11.5)
    return wrap('functions', 'Families of functions',
                'A parabola, a straight line and a square root drawn on the same axes.',
                body, caption('Figure 1.', 'Knowing the shape, the gradient and the growth of the basic functions lets '
                             'you sketch a solution before you calculate anything — and spot at once when an answer must '
                             'be wrong.'), 300)


def f_quadratic():
    body = t(340, 24, 'A parabola: two roots, one vertex, one line of symmetry', INK, 13, weight=700)
    left, right, top, bottom = 96, 620, 60, 236
    X = lambda x: left + (x + 1.0) / 6.0 * (right - left)
    Y = lambda y: bottom - (y + 3.0) / 8.0 * (bottom - top)
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, Y(0), GREY, 1.6)
    body += line(left, Y(0), right, Y(0), LIGHT, 1.4)
    # y = x^2 - 4x + 3
    pts = []
    for i in range(161):
        x = -0.7 + 5.4 * i / 160
        y = x * x - 4 * x + 3
        if y <= 4.6:
            pts.append((X(x), Y(y)))
    body += polyline(pts, BLUE, 2.8)
    body += line(X(2), Y(-2.6), X(2), Y(4.6), GREY, 1.3, '5 4')
    body += dot(X(1), Y(0), 5, RED) + dot(X(3), Y(0), 5, RED)
    body += dot(X(2), Y(-1), 5, GREEN)
    body += t(X(1) - 4, Y(0) + 22, 'x = 1', RED, 11.5, 'end', 700)
    body += t(X(3) + 8, Y(0) + 22, 'x = 3', RED, 11.5, 'start', 700)
    body += t(X(2) - 12, Y(-1) + 20, 'vertex (2, −1)', GREEN, 11.5, 'end', 700)
    body += t(X(0.02), Y(4.3), 'y = x² − 4x + 3 = (x − 1)(x − 3)', BLUE, 12, 'start', 700)
    body += t(X(3.02), Y(3.4), 'axis x = b/2a', GREY, 11, 'start')
    body += t(340, 286, 'roots where y = 0, vertex where the symmetry axis cuts the curve: three facts, one sketch',
              GREY, 11.5)
    return wrap('quadratic', 'The parabola and its anatomy',
                'A downward-opening parabola crossed by its axis of symmetry, with roots and vertex marked.',
                body, caption('Figure 2.', 'Completing the square, y = a(x + b/2a)² + c − b²/4a, puts the vertex and the '
                             'axis of symmetry on show, and the discriminant b² − 4ac counts the real roots.'), 300)


def f_similar():
    body = t(340, 24, 'Similar triangles turn a geometry problem into a ratio', INK, 13, weight=700)
    A = (120, 220)
    B = (420, 220)
    C = (330, 78)
    # altitude from C to AB
    foot = (330, 220)
    body += poly([A, B, C], '#f8fafc', BLUE, 2.2, 0.9)
    body += line(*C, *foot, GREY, 1.6, '5 4')
    body += line(*A, *C, BLUE, 2.4) + line(*C, *B, BLUE, 2.4)
    body += rect(foot[0] - 12, foot[1] - 12, 12, 12, 'none', RED, 0, 1.4)
    body += dot(*C, 5, INK) + dot(*A, 5, INK) + dot(*B, 5, INK) + dot(*foot, 4, GREY)
    body += t(A[0] - 12, A[1] + 6, 'A', INK, 12, 'end', 700)
    body += t(B[0] + 12, B[1] + 6, 'B', INK, 12, 'start', 700)
    body += t(C[0], C[1] - 14, 'C', INK, 12, 'middle', 700)
    body += t(foot[0] + 8, foot[1] - 8, 'H', GREY, 11, 'start')
    body += t(225, 236, 'c₁', BLUE, 11.5) + t(375, 236, 'c₂', BLUE, 11.5)
    body += t(345, 152, 'h', GREY, 11.5, 'start')
    body += t(215, 145, 'a', BLUE, 11.5, 'end') + t(385, 145, 'b', BLUE, 11.5, 'start')
    body += box(470, 80, 180, 118, 'ACH ~ CBH|h² = c₁c₂|a² = c₁c, b² = c₂c', '#f0fdf7', GREEN, 11.5)
    body += t(340, 262, 'the altitude creates two triangles similar to the original and to each other', GREY, 11.5)
    body += t(340, 288, 'write the ratio of corresponding sides, and every length follows', GREY, 11.5)
    return wrap('similar', 'Similar triangles and the altitude rule',
                'A triangle with an altitude drawn, the two smaller triangles being similar to the original.',
                body, caption('Figure 3.', 'Similarity is the olympiad workhorse: once two angles agree, every length ratio '
                             'is fixed, and a single proportion replaces pages of trigonometry.'), 306)


def f_trig():
    body = t(340, 24, 'Sine and cosine: same shape, shifted by a quarter of a cycle', INK, 13, weight=700)
    left, right, top, bottom = 96, 620, 62, 212
    mid = (top + bottom) / 2
    X = lambda ang: left + ang / (2 * pi) * (right - left)
    Y = lambda v: mid - v * (bottom - top) / 2.6
    body += line(left, mid, right, mid, LIGHT, 1.4)
    body += line(left, top, left, bottom, GREY, 1.6) + line(left, bottom, right, bottom, GREY, 1.6)
    for k, lab in ((0, '0'), (1, 'π/2'), (2, 'π'), (3, '3π/2'), (4, '2π')):
        body += line(X(k * pi / 2), bottom, X(k * pi / 2), bottom + 6, GREY, 1.4)
        body += t(X(k * pi / 2), bottom + 20, lab, GREY, 11)
    for v in (-1, 0, 1):
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 11, 'end')
    pts = [(X(2 * pi * i / 240), Y(sin(2 * pi * i / 240))) for i in range(241)]
    body += polyline(pts, BLUE, 2.8)
    pts = [(X(2 * pi * i / 240), Y(cos(2 * pi * i / 240))) for i in range(241)]
    body += polyline(pts, GREEN, 2.8, '7 5')
    body += t(X(0.42 * pi), Y(1.28), 'sin θ', BLUE, 12, 'end', 700)
    body += t(X(0.10), Y(-1.40), 'cos θ', GREEN, 12, 'start', 700)
    body += arrow('trig', X(0.62 * pi), Y(1.34), X(0.96 * pi), Y(1.34), GREY, 1.8)
    body += t(X(1.42 * pi), Y(1.34) + 4, 'shifting cos left by π/2 gives sin', GREY, 11, 'start')
    body += t(340, 258, 'cos θ = sin(θ + π/2), so a phase shift is all that separates them', GREY, 11.5)
    body += t(340, 284, 'sin²θ + cos²θ = 1 is Pythagoras seen from the unit circle', GREY, 11.5)
    return wrap('trig', 'Sine and cosine on one cycle',
                'A sine curve and a cosine curve on the same axes, the cosine shifted by a quarter cycle.',
                body, caption('Figure 4.', 'Phase, amplitude and period are the three numbers that describe any harmonic '
                             'quantity; a graph showing all three is quicker to read than a formula.'), 300)


def f_eliminate():
    body = t(340, 24, 'Two equations, two unknowns: the geometry of elimination', INK, 13, weight=700)
    left, right, top, bottom = 96, 620, 58, 226
    body += grid((left, top, right, bottom), 4, 4)
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x / 5.0 * (right - left)
    Y = lambda y: bottom - y / 5.0 * (bottom - top)
    for v in (1, 2, 3, 4):
        body += t(X(v), bottom + 19, f'{v}', GREY, 11)
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 11, 'end')
    body += t((left + right) / 2, bottom + 42, 'x', GREY, 12) + t(44, (top + bottom) / 2, 'y', GREY, 12)
    # y = 4 - x and y = x - 1, intersection (2.5, 1.5)
    body += line(X(0), Y(4), X(4.4), Y(0), BLUE, 2.6)
    body += line(X(0), Y(-1), X(4.3), Y(3.3), PURPLE, 2.6)
    body += line(X(0), Y(3.0), X(4.2), Y(-1.2), GREEN, 2.0, '6 4')
    body += dot(X(2.5), Y(1.5), 6, RED)
    body += t(X(2.5) + 12, Y(1.5) + 22, 'unique solution', RED, 11.5, 'start', 700)
    body += legend([(BLUE, 'x + y = 4'), (GREEN, 'x + y = 3: parallel, no solution', '6 4'),
                    (PURPLE, 'y − x = −1')], 292, 110, 190, 11.5)
    body += t(340, 318, 'subtract the equations to kill one unknown; the intersection survives', GREY, 11.5)
    return wrap('eliminate', 'Solving a pair of linear equations',
                'Two crossing straight lines with their intersection marked, and a parallel line showing no solution.',
                body, caption('Figure 5.', 'A pair of linear equations is a pair of lines: one intersection, no '
                             'intersection, or a whole line of them. Elimination is arithmetic; the picture tells you which '
                             'case you are in.'), 306)


FIGURES = {
    'functions': f_functions,
    'quadratic': f_quadratic,
    'similar': f_similar,
    'trig': f_trig,
    'eliminate': f_eliminate,
}


def lab_quadratic():
    controls = (
        slider('quad-a', 'Coefficient a', -2.0, 3.0, 0.1, 1.0, '')
        + slider('quad-b', 'Coefficient b', -6.0, 6.0, 0.1, -4.0, '')
        + slider('quad-c', 'Coefficient c', -6.0, 6.0, 0.1, 3.0, '')
    )
    return shell(
        'quad', 'The quadratic explorer',
        'Change the three coefficients of y = ax² + bx + c and watch the discriminant, the roots and the vertex move. '
        'The plot rescales itself, so extreme coefficients remain visible.',
        controls,
        [('disc', 'Discriminant b² − 4ac'), ('nature', 'Nature of the roots'),
         ('x1', 'Root 1'), ('x2', 'Root 2'), ('vertex', 'Vertex'), ('factor', 'Completed square form')],
        'Set a negative and note how the parabola turns over. Push c until the discriminant passes through zero and '
        'watch the two roots merge into a double root.'
    )


LABS = {'quad': lab_quadratic}
