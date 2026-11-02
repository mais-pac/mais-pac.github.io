"""02.03 Dynamics: energy, momentum and rotation."""
from math import cos, sin, radians, sqrt, exp


def f_energy():
    height = lambda x: 1.8 + 3.4 * cos(x / 4.4) * exp(-x / 30) + 0.9 * cos(x / 2.1) * exp(-x / 34)
    top = 6.0
    return chart(
        'energy-diagram', 'A roller coaster: speed comes from the lost height',
        'Ignoring friction, ½mv² = mg(h₀ − h), so the speed peaks in the valleys and vanishes at the highest crest.',
        'horizontal position (m)', 'height (m), speed (m s⁻¹)',
        [('track height h(x)', BLUE, height),
         ('speed / 2 (from energy)', GREEN, lambda x: sqrt(max(0.0, 2 * 9.81 * (top - height(x)))) / 2)],
        xr=(0, 34), yr=(0, 15), xticks=(5, 10, 15, 20, 25, 30), yticks=(0, 5, 10, 15), height=340,
        yfmt='{:.0f}',
        notes=[(0.3, 14.2, 'released from rest at h₀ = 6 m', GREY)])


def f_momentum():
    body = t(340, 24, 'Momentum is a vector: collisions are not one-dimensional bookkeeping', INK, 13, weight=700)
    body += t(340, 48, 'before', GREY, 11.5, weight=700)
    body += circle(180, 96, 22, BLUE, '#dbeafe', 2.4) + t(180, 101, 'm₁', INK, 12, weight=700)
    body += arrow('momentum', 206, 96, 292, 96, BLUE, 2.6) + t(248, 82, 'p₁', BLUE, 12)
    body += circle(500, 96, 30, PURPLE, '#f3e8ff', 2.4) + t(500, 101, 'm₂', INK, 12, weight=700)
    body += arrow('momentum', 468, 96, 400, 96, PURPLE, 2.6) + t(434, 82, 'p₂', PURPLE, 12)
    body += t(340, 146, 'total momentum  p₁ + p₂  is conserved in every collision', GREY, 11.5)
    body += line(80, 166, 600, 166, '#e2e8f0', 1.4)
    body += t(340, 192, 'after', GREY, 11.5, weight=700)
    body += circle(320, 244, 34, '#94a3b8', '#e2e8f0', 2.4) + t(320, 249, 'm₁+m₂', INK, 11.5, weight=700)
    body += arrow('momentum', 348, 232, 470, 196, GREEN, 2.6) + t(486, 192, "p′", GREEN, 12, 'start')
    body += t(340, 296, 'Same vector sum; kinetic energy may be lost to heat, sound or deformation.', GREY, 11.5)
    return wrap('momentum', 'A collision in the momentum picture',
                'Two masses approach along one line and leave together along the direction of the total momentum.',
                body, caption('Figure 2.', 'Momentum is conserved in every collision; kinetic energy is conserved only in '
                             'elastic ones. Energy lost becomes heat, sound or deformation.'), 312)


def f_rotation():
    body = t(340, 24, 'The same mass distribution has different moments of inertia', INK, 13, weight=700)
    items = [('hoop', 0.35), ('disc', 0.5), ('sphere', 0.4), ('rod', 1 / 12)]
    labels = {'hoop': 'thin hoop\nI = MR²', 'disc': 'solid disc\nI = ½MR²',
              'sphere': 'solid sphere\nI = ⅖MR²', 'rod': 'rod about centre\nI = MR²/12'}
    values = [1.0, 0.5, 0.4, 1 / 12]
    for i, (name, _) in enumerate(items):
        x = 110 + i * 150
        body += circle(x, 116, 44, BLUE if i % 2 == 0 else GREEN, '#f8fafc', 2.6)
        body += dot(x, 116, 4, INK)
        body += t(x, 186, labels[name].split('\n')[1], INK, 11.5)
        body += t(x, 96, name, GREY, 11.5)
    body += t(340, 232, 'Rolling without slipping: v = ωR, so the kinetic energy splits between translation and rotation.',
              GREY, 11.5)
    body += t(340, 258, 'A hoop converts the largest share into rotation, so it loses a race down a slope.',
              GREY, 11.5)
    return wrap('rotation', 'Moments of inertia of equal masses',
                'Four rigid bodies with the same mass and radius but different mass distributions.',
                body, caption('Figure 3.', 'I is the rotational refusal to accelerate: it is to rotation what mass is to '
                             'translation, and it depends on how far the mass sits from the axis.'), 280)


def f_impulse():
    return chart(
        'impulse', 'Impulse is the area under a force–time graph',
        'A short, large force and a long, small force can deliver the same impulse — but only one of them breaks things.',
        'time (ms)', 'force (kN)',
        [('hard impact', RED, lambda t: 12 * exp(-((t - 2) / 0.55) ** 2)),
         ('cushioned impact', GREEN, lambda t: 4 * exp(-((t - 4) / 1.9) ** 2))],
        xr=(0, 10), yr=(0, 13), xticks=(2, 4, 6, 8), yticks=(0, 3, 6, 9, 12), height=330,
        notes=[(0.4, 12.2, 'same area ⇒ same Δp', GREY)])


def f_work():
    return chart(
        'work-area', 'Work is the area under an F–x graph',
        'A spring obeys F = kx, so the work stored is the triangular area ½kx².',
        'extension x (m)', 'force F (N)',
        [('spring F = kx, k = 40 N/m', BLUE, lambda x: 40 * x),
         ('constant 20 N', GREEN, lambda x: 20.0)],
        xr=(0, 0.5), yr=(0, 25), xticks=(0.1, 0.2, 0.3, 0.4), yticks=(0, 5, 10, 15, 20), height=330,
        xfmt='{:.1f}',
        notes=[(0.02, 22.5, 'area under the line = work done', GREY)])


FIGURES = {
    'energy-diagram': f_energy,
    'momentum': f_momentum,
    'rotation': f_rotation,
    'impulse': f_impulse,
    'work-area': f_work,
}


def lab_collision():
    controls = (
        slider('col-m1', 'Mass m₁', 0.2, 5, 0.1, 1.0, ' [kg]')
        + slider('col-v1', 'Velocity v₁', -6, 6, 0.1, 3.0, ' [m/s]')
        + slider('col-m2', 'Mass m₂', 0.2, 5, 0.1, 2.0, ' [kg]')
        + slider('col-v2', 'Velocity v₂', -6, 6, 0.1, -1.0, ' [m/s]')
        + select('col-type', 'Collision type', [('elastic', 'Perfectly elastic'),
                                                ('inelastic', 'Perfectly inelastic'),
                                                ('half', 'Half-elastic (e = 0.5)')])
    )
    return shell(
        'collision', 'One-dimensional collisions, measured not guessed',
        'Two trolleys collide head-on. The experiment solves momentum conservation together with the coefficient of '
        'restitution e, then reports the energy lost and checks the e = 1 and e = 0 limits.',
        controls,
        [('v1f', 'Final v₁'), ('v2f', 'Final v₂'), ('pf', 'Final momentum'),
         ('ke', 'Energy lost'), ('com', 'Centre-of-mass speed')],
        'Make the collision elastic and confirm the energy loss falls to zero. Then set equal masses and one trolley at '
        'rest: in the elastic case the first stops dead. Why?'
    )


LABS = {'collision': lab_collision}
