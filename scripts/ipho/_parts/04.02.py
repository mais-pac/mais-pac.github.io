"""04.02 Vectors and complex numbers."""
from math import sin, cos, pi, sqrt, radians, exp, log10, atan2, degrees


def f_components():
    body = t(340, 24, 'A vector is a magnitude and a direction — and a pair of components', INK, 13, weight=700)
    left, right, top, bottom = 110, 560, 60, 232
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x / 10.0 * (right - left)
    Y = lambda y: bottom - y / 8.0 * (bottom - top)
    for v in (2, 4, 6, 8):
        body += t(X(v), bottom + 19, f'{v}', GREY, 11)
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 11, 'end')
    body += t((left + right) / 2, bottom + 42, 'east / m', GREY, 12)
    body += f'<g transform="translate(40,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'north / m', GREY, 12) + '</g>'
    A = (4.8, 5.4)
    ax, ay = X(A[0]), Y(A[1])
    body += line(X(0), Y(0), ax, Y(0), BLUE, 1.8, '6 4')
    body += line(ax, Y(0), ax, ay, GREEN, 1.8, '6 4')
    body += line(X(0), Y(0), ax, ay, INK, 2.8)
    body += arrow('comp', ax - 26, Y(0), X(A[0]) - 0.1, Y(0), BLUE, 2.0)
    body += arrow('comp2', ax, Y(0) - 26, ax, ay + 2, GREEN, 2.0)
    body += rect(ax, Y(0) - 14, 14, 14, 'none', GREY, 0, 1.2)
    body += t(X(2.4), Y(1.05), 'A cos θ', BLUE, 12, 'middle', 700)
    body += t(ax + 12, Y(2.7), 'A sin θ', GREEN, 12, 'start', 700)
    body += t(X(2.05), Y(3.45), 'A', INK, 13, 'end', 700)
    body += f'<path d="M {X(1.3):.1f} {Y(0):.1f} A 46 46 0 0 0 {X(1.3 * cos(radians(48))):.1f} {Y(1.3 * sin(radians(48))):.1f}" fill="none" stroke="{AMBER}" stroke-width="1.8"/>'
    body += t(X(1.75), Y(0.55), 'θ', AMBER, 12, 'start', 700)
    body += t(X(6.05), Y(4.55), 'A = A cos θ î + A sin θ ĵ', INK, 12.5, 'start', 700)
    body += t(X(6.05), Y(3.75), '|A| = √(Aₓ² + A_y²)', GREY, 11.5, 'start')
    body += t(X(6.05), Y(3.05), 'tan θ = A_y / Aₓ', GREY, 11.5, 'start')
    body += t(340, 286, 'components add separately, so a two-dimensional problem becomes two one-dimensional ones', GREY, 11.5)
    return wrap('components', 'Resolving a vector into components',
                'A vector drawn from the origin with its horizontal and vertical components dashed in.',
                body, caption('Figure 1.', 'Resolution and composition are the same operation read in two directions. '
                             'Because components along perpendicular axes never mix, every vector problem splits into '
                             'independent one-dimensional problems.'), 306)


def f_addition():
    body = t(340, 24, 'Adding vectors head to tail: the parallelogram rule', INK, 13, weight=700)
    left, right, top, bottom = 110, 570, 58, 234
    body += line(left, bottom, right, bottom, GREY, 1.4) + line(left, top, left, bottom, GREY, 1.4)
    X = lambda x: left + x / 10.0 * (right - left)
    Y = lambda y: bottom - y / 8.0 * (bottom - top)
    O = (1.0, 1.2)
    P = (6.2, 3.4)
    Q = (3.6, 6.2)
    S = (P[0] + Q[0] - O[0], P[1] + Q[1] - O[1])
    body += arrow('add1', X(O[0]), Y(O[1]), X(P[0]), Y(P[1]), BLUE, 2.6)
    body += arrow('add2', X(O[0]), Y(O[1]), X(Q[0]), Y(Q[1]), GREEN, 2.6)
    body += arrow('add3', X(P[0]), Y(P[1]), X(S[0]), Y(S[1]), BLUE, 2.2, '6 4')
    body += arrow('add4', X(Q[0]), Y(Q[1]), X(S[0]), Y(S[1]), GREEN, 2.2, '6 4')
    body += arrow('add5', X(O[0]), Y(O[1]), X(S[0]), Y(S[1]), RED, 3.0)
    body += dot(X(O[0]), Y(O[1]), 4.5, INK) + dot(X(S[0]), Y(S[1]), 4.5, RED)
    body += t(X(O[0]) - 10, Y(O[1]) + 6, 'O', INK, 12, 'end', 700)
    body += t(X(P[0]) + 8, Y(P[1]) + 16, 'P', BLUE, 12, 'middle', 700)
    body += t(X(Q[0]) - 12, Y(Q[1]) - 4, 'Q', GREEN, 12, 'end', 700)
    body += t(X(S[0]) + 10, Y(S[1]) - 6, 'P + Q', RED, 12, 'start', 700)
    body += t(X(3.0), Y(1.6), '|P + Q| is not |P| + |Q|', GREY, 11.5, 'start')
    body += t(340, 262, 'the resultant is the diagonal of the parallelogram on the two vectors', GREY, 11.5)
    body += t(340, 288, '|P + Q|² = |P|² + |Q|² + 2|P||Q| cos φ, with φ the angle between them', GREY, 11.5)
    return wrap('addition', 'Adding two vectors',
                'Two vectors drawn from a common origin and their resultant along the diagonal of the parallelogram.',
                body, caption('Figure 2.', 'Only when the vectors are parallel does the sum have length equal to the sum '
                             'of the lengths. The angle between them decides everything, and the cosine rule quantifies it.'), 306)


def f_plane():
    body = t(340, 24, 'A vector in air: along-track and across-track, then an arrow on the map', INK, 13, weight=700)
    left, right, top, bottom = 96, 470, 56, 226
    body += line(left, bottom, right, bottom, GREY, 1.4) + line(left, top, left, bottom, GREY, 1.4)
    X = lambda x: left + x / 240.0 * (right - left)
    Y = lambda y: bottom - y / 200.0 * (bottom - top)
    for v in (60, 120, 180):
        body += t(X(v), bottom + 19, f'{v}', GREY, 10.5)
    for v in (50, 100, 150):
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 10.5, 'end')
    body += t((left + right) / 2, bottom + 40, 'east / km', GREY, 11.5)
    body += f'<g transform="translate(30,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'north / km', GREY, 11.5) + '</g>'
    # air vector 160 east, 90 north; wind 40 east
    body += arrow('plane1', X(0), Y(0), X(160), Y(90), BLUE, 2.6)
    body += arrow('plane2', X(160), Y(90), X(200), Y(90), AMBER, 2.4)
    body += arrow('plane3', X(0), Y(0), X(200), Y(90), RED, 2.8)
    body += line(X(160), Y(90), X(160), Y(0), GREY, 1.2, '4 3')
    body += line(X(0), Y(90), X(160), Y(90), GREY, 1.2, '4 3')
    body += t(X(80), Y(0) - 8, '160', GREY, 10.5)
    body += t(X(166), Y(45), '90', GREY, 10.5, 'start')
    body += t(X(120), Y(120), 'air: 160 E, 90 N', BLUE, 11, 'middle', 700)
    body += box(486, 74, 186, 136, 'air 160 E + 90 N|wind 40 E|ground 200 E + 90 N||resultant 219 km/h|24° north of east', '#f0fdf7', GREEN, 10.5)
    body += legend([(BLUE, 'air velocity'), (AMBER, 'wind'), (RED, 'ground velocity')], 272, 100, 165, 10.5)
    return wrap('plane', 'Vector addition in a navigation problem',
                'An aircraft velocity, a wind vector and the resultant ground velocity drawn on a map grid.',
                body, caption('Figure 3.', 'Components make the addition mechanical: add the east components, add the '
                             'north components, then recombine. The angle of the resultant comes from its two components, '
                             'not from the two lengths.'), 300)


def f_argand():
    body = t(340, 24, 'The complex plane turns a rotation into a multiplication', INK, 13, weight=700)
    cx, cy, r = 250, 150, 105
    body += line(cx - r - 26, cy, cx + r + 30, cy, GREY, 1.5) + line(cx, cy - r - 22, cx, cy + r + 24, GREY, 1.5)
    body += circle(cx, cy, r, LIGHT, 'none', 1.4, '5 4')
    body += t(cx + r + 40, cy + 4, 'Re', GREY, 11.5, 'start')
    body += t(cx + 8, cy - r - 6, 'Im', GREY, 11.5, 'start')
    ang = radians(40)
    zx, zy = cx + r * cos(ang), cy - r * sin(ang)
    body += line(cx, cy, zx, zy, BLUE, 2.6)
    body += dot(zx, zy, 5, BLUE)
    body += line(zx, zy, zx, cy, GREY, 1.2, '4 3') + line(cx, cy, zx, cy, GREY, 1.2, '4 3')
    body += f'<path d="M {cx + 38:.1f} {cy:.1f} A 38 38 0 0 0 {cx + 38 * cos(ang):.1f} {cy - 38 * sin(ang):.1f}" fill="none" stroke="{AMBER}" stroke-width="1.8"/>'
    body += t(cx + 52, cy - 14, 'θ', AMBER, 12, 'start', 700)
    body += t(zx + 10, zy - 10, 'z = r cos θ + i r sin θ', BLUE, 11.5, 'start', 700)
    body += t((cx + zx) / 2, cy + 34, 'r cos θ', GREY, 10.5, 'middle')
    body += t(zx + 10, (cy + zy) / 2, 'r sin θ', GREY, 10.5, 'start')
    body += t(340, 268, 'modulus = amplitude, argument = phase: a phasor carries both numbers of a wave', GREY, 11.5)
    body += t(340, 292, 'multiplying by cos θ + i sin θ rotates by θ without changing the length', GREY, 11.5)
    body += box(500, 62, 158, 74, 'z₁z₂: lengths multiply|angles add|z₁/z₂: lengths divide', '#f8fafc', GREY, 10.5)
    return wrap('argand', 'A complex number as a rotating vector',
                'A vector in the complex plane with its real and imaginary parts and its argument marked.',
                body, caption('Figure 4.', 'Phasors are the practical form of complex numbers: adding waves means '
                             'adding their phasors, and a phase shift becomes a rotation. In AC circuit theory this turns '
                             'trigonometry into bookkeeping.'), 312)


def f_impedance():
    body = t(340, 24, 'An impedance diagram: resistance along, reactance up', INK, 13, weight=700)
    left, right, top, bottom = 120, 540, 62, 224
    body += line(left, bottom, right, bottom, GREY, 1.6) + line(left, top, left, bottom, GREY, 1.6)
    X = lambda x: left + x / 12.0 * (right - left)
    Y = lambda y: bottom - y / 12.0 * (bottom - top)
    for v in (3, 6, 9):
        body += t(X(v), bottom + 19, f'{v}', GREY, 11)
        body += t(left - 8, Y(v) + 4, f'{v}', GREY, 11, 'end')
        body += line(X(v), bottom, X(v), top, '#eef2fa', 1)
        body += line(left, Y(v), right, Y(v), '#eef2fa', 1)
    body += t((left + right) / 2, bottom + 40, 'R / Ω', GREY, 12)
    body += f'<g transform="translate(44,{(top + bottom) / 2}) rotate(-90)">' + t(0, 0, 'X / Ω', GREY, 12) + '</g>'
    body += arrow('imp1', X(0), Y(0), X(8), Y(0), BLUE, 2.6)
    body += arrow('imp2', X(8), Y(0), X(8), Y(6), GREEN, 2.6)
    body += arrow('imp3', X(0), Y(0), X(8), Y(6), RED, 3.0)
    body += dot(X(8), Y(6), 4.5, RED)
    body += t(X(4), Y(1.15), 'R', BLUE, 12, 'middle', 700)
    body += t(X(8) + 12, Y(3), 'X', GREEN, 12, 'start', 700)
    body += t(X(5.5), Y(5.3), 'Z', RED, 12.5, 'start', 700)
    body += f'<path d="M {X(1.6):.1f} {Y(0):.1f} A 44 44 0 0 0 {X(1.6 * cos(atan2(6, 8))):.1f} {Y(1.6 * sin(atan2(6, 8))):.1f}" fill="none" stroke="{AMBER}" stroke-width="1.8"/>'
    body += t(X(1.95), Y(0.55), 'φ', AMBER, 12, 'start', 700)
    body += box(552, 84, 118, 104, '|Z| = √(R²+X²)|tan φ = X/R|X_L = ωL|X_C = 1/ωC', '#f8fafc', GREY, 10.5)
    body += t(340, 288, 'the phase angle between current and voltage is the argument of the impedance', GREY, 11.5)
    return wrap('impedance', 'Impedance as a complex vector',
                'A resistance and a reactance drawn at right angles with the impedance as the hypotenuse.',
                body, caption('Figure 5.', 'Impedance behaves exactly like a two-dimensional vector, except that the '
                             'vertical axis is reactance. Because the two axes are perpendicular, the magnitudes do not '
                             'simply add: the impedance magnitude is the hypotenuse of R and X.'), 312)


FIGURES = {
    'components': f_components,
    'addition': f_addition,
    'plane': f_plane,
    'argand': f_argand,
    'impedance': f_impedance,
}


def lab_vector():
    controls = (
        slider('vec-ax', 'Vector A: east component', -10.0, 10.0, 0.5, 6.0, '')
        + slider('vec-ay', 'Vector A: north component', -10.0, 10.0, 0.5, 4.0, '')
        + slider('vec-bx', 'Vector B: east component', -10.0, 10.0, 0.5, -2.0, '')
        + slider('vec-by', 'Vector B: north component', -10.0, 10.0, 0.5, 6.0, '')
    )
    return shell(
        'vector', 'Vector addition and resolution',
        'Set the components of two vectors and watch the resultant, the angle between them and the dot and cross '
        'products. The parallelogram is drawn as an aid to the head-to-tail addition.',
        controls,
        [('magA', '|A|'), ('dirA', 'Direction of A'), ('magB', '|B|'), ('sum', 'Resultant'),
         ('angle', 'Angle between A and B'), ('dot', 'A · B'), ('cross', '|A × B|')],
        'Set B opposite to A: what happens to the resultant and to the angle between the vectors? Then make the '
        'vectors perpendicular and check that the resultant is the hypotenuse.'
    )


LABS = {'vector': lab_vector}
