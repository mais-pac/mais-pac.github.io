"""02.02 Statics: figures and experiment."""
from math import cos, sin, radians, sqrt, atan2, degrees


def f_torque():
    body = t(340, 22, 'Torque is force times lever arm', INK, 13, weight=700)
    body += line(110, 214, 570, 214, GREY, 4) + dot(340, 214, 7, INK) + t(340, 240, 'pivot O', GREY, 11.5)
    body += arrow('torque', 340, 214, 340, 92, BLUE, 2.6) + t(328, 120, 'r', BLUE, 12, 'end')
    body += arrow('torque', 340, 92, 492, 92, GREEN, 2.6) + t(416, 80, 'F (perpendicular)', GREEN, 11.5)
    body += circle(340, 92, 22, AMBER, 'none', 1.4, '5 4')
    body += t(200, 150, 'τ = r F sin φ', INK, 13, weight=700)
    body += t(200, 174, 'doubling r doubles τ', GREY, 11)
    body += t(200, 192, 'only the perpendicular', GREY, 11)
    body += t(200, 210, 'part of F turns it', GREY, 11)
    body += t(340, 272, 'Equilibrium: ΣF = 0 and Στ = 0 about any chosen point.', GREY, 11.5)
    return wrap('torque', 'Torque is force times lever arm',
                'A force applied at distance r from a pivot; only its perpendicular component turns the body.',
                body, caption('Figure 1.', 'Pick the pivot so that unknown forces pass through it. Their torque is then '
                             'zero and they vanish from the equation.'), 292)


def f_beam():
    body = t(340, 22, 'A loaded beam: two supports, three unknowns, two equations', INK, 13, weight=700)
    body += rect(80, 150, 520, 14, '#e2e8f0', GREY, 3)
    for x, label in ((170, 'A'), (510, 'B')):
        body += poly([(x, 164), (x - 12, 186), (x + 12, 186)], '#f1f5f9', GREY, 1.6)
        body += t(x, 204, label, GREY, 12, weight=700)
        body += arrow('beam', x, 164, x, 118, BLUE, 2.4)
        body += t(x + 10, 128, 'R', BLUE, 12, 'start')
    body += arrow('beam', 380, 150, 380, 232, AMBER, 2.6)
    body += t(380, 250, 'W = 600 N', AMBER, 12, weight=700)
    body += line(80, 150, 600, 150, GREY, 1)
    body += line(170, 214, 380, 214, GREY, 1.2, '5 4') + line(380, 214, 510, 214, GREY, 1.2, '5 4')
    body += t(275, 230, '2.0 m', GREY, 11.5) + t(445, 230, '3.0 m', GREY, 11.5)
    body += t(340, 300, 'Taking torques about A removes R_A and gives R_B at once.', GREY, 11.5)
    return wrap('beam', 'A beam on two supports',
                'A 600 N load hangs 2 m from support A on a 5 m beam.',
                body, caption('Figure 2.', 'Two force equations and one torque equation are available in two dimensions; '
                             'a beam with three unknown reactions is exactly determined.'), 318)


def f_friction():
    from math import radians, cos, sin, tan
    body = t(340, 22, 'A block on an incline: the flat-ground intuition fails', INK, 13, weight=700)
    ang = 25.0
    a = radians(ang)
    ox, oy = 110, 252
    run = 456.0
    slope = lambda x: oy - (x - ox) * tan(a)
    body += poly([(ox, oy), (ox + run, oy), (ox + run, slope(ox + run))], '#f8fafc', GREY, 2)
    body += f'<path d="M {ox + 150} {oy} A 150 150 0 0 0 {ox + 150 * cos(a):.1f} {oy - 150 * sin(a):.1f}" fill="none" stroke="{INK}" stroke-width="1.6"/>'
    body += t(ox + 162, oy - 12, 'θ', INK, 13, weight=700, anchor='start')

    ux, uy = cos(a), -sin(a)          # unit vector up the slope
    nx, ny = -sin(a), -cos(a)         # outward normal (up and left)
    cx = 316.0
    bx, by = cx, slope(cx) - 1.0
    half, height = 38.0, 34.0
    def P(su, sn):
        return (bx + su * ux + sn * nx, by + su * uy + sn * ny)
    body += poly([P(-half, 0), P(half, 0), P(half, height), P(-half, height)], '#dbeafe', BLUE, 2)
    cxg = bx + 0 * ux + 0 * nx
    cyg = by

    body += arrow('friction', cxg, cyg, cxg, cyg + 92, AMBER, 2.6)
    body += t(cxg + 10, cyg + 108, 'mg', AMBER, 12, 'start', 700)
    body += arrow('friction', cxg, cyg, cxg + 92 * nx, cyg + 92 * ny, BLUE, 2.6)
    body += t(cxg + 100 * nx - 10, cyg + 100 * ny - 6, 'N', BLUE, 12, 'end', 700)
    sx, sy = cxg - 24 * ux, cyg - 24 * uy
    body += arrow('friction', sx, sy, sx + 86 * ux, sy + 86 * uy, GREEN, 2.6)
    body += t(sx + 92 * ux + 14, sy + 92 * uy + 14, 'f', GREEN, 12, 'start', 700)

    body += t(392, 60, 'At the limit:  tan θ = μ', BLUE, 13, weight=700)
    body += t(392, 80, 'the mass cancels out', GREY, 11.5)
    body += t(300, 300, 'Tilt until sliding starts and you have measured μ.', GREY, 11.5)
    return wrap('friction', 'Forces on a block at the point of sliding',
                'Weight down, normal reaction perpendicular to the slope, friction up the slope.',
                body, caption('Figure 3.', 'Resolve along and perpendicular to the slope, never horizontally and '
                             'vertically. The normal reaction is mg cos θ, not mg.'), 318)


def f_stability():
    body = t(340, 22, 'Stable, neutral and unstable: read the curvature of U(x)', INK, 13, weight=700)
    X = lambda x: 80 + x / 10 * 560
    box_ = (80, 44, 640, 190)
    Y = lambda u: 190 - (u + 1.6) / 2.8 * 146
    body += grid(box_, 4, 3)
    body += line(80, 190, 640, 190, GREY, 1.4) + t(640, 206, 'x', GREY, 12, 'end')
    body += curve(lambda x: 0.02 * (x - 5) ** 2 - 1.4, 0, 10, -1.6, 1.2, box_, 200, BLUE, 2.8)
    body += curve(lambda x: 0.012 * (x - 5) ** 4 - 0.19 * (x - 5) ** 2 + 0.25, 0, 10, -1.6, 1.2,
                  box_, 200, PURPLE, 2.8)
    body += dot(X(5), Y(-1.4), 6, BLUE)
    body += t(X(5) + 12, Y(-1.4) - 8, 'stable: minimum of U', BLUE, 11.5, 'start', 700)
    body += dot(X(5), Y(0.25), 6, PURPLE)
    body += t(X(5) + 12, Y(0.25) - 10, 'unstable: maximum of U', PURPLE, 11.5, 'start', 700)
    body += t(96, 36, 'U(x)', INK, 13, 'start', 700)
    body += t(240, 296, 'Near a minimum the well is a parabola: ω² = U″(x₀)/m.', GREY, 11.5)
    body += t(240, 318, 'Near a maximum, small displacements grow exponentially — instability.', GREY, 11.5)
    return wrap('stability', 'Stability is the sign of the curvature of the potential',
                'A parabolic well (stable) and a quartic double well with a hump (unstable).',
                body, caption('Figure 4.', 'Expand U about an equilibrium: the linear term vanishes, the quadratic term '
                             'decides everything, and ω² = U″/m.'), 340)


def f_com():
    body = t(340, 22, 'The centre of mass is a weighted average of position', INK, 13, weight=700)
    body += line(80, 120, 640, 120, GREY, 2.4)
    for x, m, colour in ((160, 1, BLUE), (300, 2, GREEN), (520, 3, PURPLE)):
        r = 12 + 6 * m
        body += circle(x, 120 - r - 26, r, colour, '#ffffff', 2.4)
        body += line(x, 120, x, 120 - r - 26 + r, GREY, 1.2, '4 4')
        body += t(x, 196, f'{m} kg', colour, 12, weight=700)
    body += dot(386, 120, 8, AMBER)
    body += t(386, 96, 'centre of mass', AMBER, 11.5, weight=700)
    body += t(340, 226, 'x_cm = Σ mᵢxᵢ / Σ mᵢ = (1·0 + 2·1.4 + 3·3.6)/6 = 2.27 m', INK, 12.5)
    body += t(340, 252, 'measuring from the 1 kg mass; separations are drawn to scale.', GREY, 11.5)
    return wrap('com', 'Centre of mass of three unequal masses',
                'Masses 1, 2 and 3 kg at increasing separations; the weighted mean lies nearest the heaviest mass.',
                body, caption('Figure 5.', 'A rigid body acts like a point mass at its centre of mass for translation; '
                             'for rotation, the distribution matters and you need the moment of inertia.'), 292)


FIGURES = {
    'torque': f_torque,
    'beam': f_beam,
    'friction': f_friction,
    'stability': f_stability,
    'com': f_com,
}


def lab_ladder():
    controls = (
        slider('ladder-l', 'Ladder length L', 2, 8, 0.1, 4.0, ' [m]')
        + slider('ladder-m', 'Mass of ladder m', 5, 40, 1, 12, ' [kg]')
        + slider('ladder-a', 'Lean angle θ', 20, 85, 1, 65, ' [deg]')
        + slider('ladder-mu', 'Wall friction μ_wall', 0, 0.6, 0.01, 0.0)
    )
    return shell(
        'ladder', 'A ladder against a smooth wall',
        'The floor has friction coefficient 0.45; the wall is smooth unless you give it friction. The experiment '
        'solves the equilibrium equations and reports the friction the floor must supply, compared with the maximum '
        'available.',
        controls,
        [('nf', 'Floor reaction N_f'), ('ffloor', 'Friction needed'), ('fmax', 'Maximum friction'),
         ('status', 'Status'), ('angle', 'Critical angle')],
        'Raise the lean angle towards vertical: what happens to the friction demanded? Now set m to its minimum and '
        'compare the critical angle. Does mass matter?'
    )


LABS = {'ladder': lab_ladder}
