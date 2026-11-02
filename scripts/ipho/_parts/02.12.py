"""02.12 Special relativity."""
from math import sin, cos, pi, sqrt, radians, exp, log10, atan, tanh


def f_postulates():
    body = t(340, 24, 'Two postulates and the train that shrinks', INK, 13, weight=700)
    body += rect(90, 70, 200, 74, '#eff6ff', BLUE, 6)
    body += t(190, 100, '1. Physics is the same', INK, 11.5, weight=700)
    body += t(190, 122, 'in every inertial frame', GREY, 11)
    body += rect(390, 70, 200, 74, '#eff6ff', BLUE, 6)
    body += t(490, 100, '2. c is the same for', INK, 11.5, weight=700)
    body += t(490, 122, 'every observer', GREY, 11)
    # moving train with a light clock inside
    body += rect(140, 172, 400, 84, '#dbeafe', BLUE, 8)
    body += t(340, 216, 'v →', BLUE, 14, weight=700)
    body += arrow('rel', 140, 268, 540, 268, GREEN, 2.4) + t(340, 288, 'the flash travels a longer path in the frame where the train moves', GREY, 11)
    body += dot(250, 214, 5, AMBER) + dot(432, 214, 5, AMBER)
    body += line(250, 214, 432, 214, AMBER, 2, '6 4')
    return wrap('postulates', 'The two postulates of special relativity',
                'Two statements in boxes above a moving train with a light flash bouncing inside it.',
                body, caption('Figure 1.', 'The second postulate is the revolutionary one: the speed of light does not '
                             'depend on how fast you chase it. Everything else in this topic — time dilation, length '
                             'contraction, the twin paradox — follows from those two sentences.'), 306)


def f_gamma():
    xmax = 0.999
    return chart(
        'lorentz-factor', 'The Lorentz factor: almost flat until v approaches c',
        'γ stays within 1% of unity up to 0.14c, but diverges as v → c.',
        'v / c', 'γ = 1/√(1 − v²/c²)',
        [('γ', BLUE, lambda x: 1 / sqrt(max(1e-9, 1 - x * x)))],
        xr=(0, xmax), yr=(0, 8), xticks=(0.2, 0.4, 0.6, 0.8, 0.95), yticks=(2, 4, 6, 8), height=350,
        xfmt='{:.2f}', yfmt='{:.0f}')


def f_timedilation():
    return chart(
        'time-dilation', 'Clocks in relative motion run slow',
        'A clock moving at 0.8c ticks once while an identical clock at rest ticks 1.67 times.',
        'time in the moving frame (proper time)',
        'time measured in the lab',
        [('β = 0.5', BLUE, lambda t: t / sqrt(1 - 0.25)),
         ('β = 0.8', GREEN, lambda t: t / sqrt(1 - 0.64)),
         ('β = 0.95', PURPLE, lambda t: t / sqrt(1 - 0.9025))],
        xr=(0, 4), yr=(0, 14), xticks=(1, 2, 3, 4), yticks=(2, 4, 6, 8, 10, 12, 14), height=355,
        xfmt='{:.0f}', yfmt='{:.0f}')


def f_length():
    body = t(340, 24, 'A moving rod is measured short', INK, 13, weight=700)
    body += line(90, 108, 620, 108, LIGHT, 1.2)
    body += t(76, 112, 'at rest', GREY, 11, 'end', 700)
    body += rect(120, 84, 420, 46, '#e0f2fe', BLUE, 6)
    body += t(330, 112, 'proper length L₀', INK, 11.5)
    body += t(76, 226, 'moving', GREY, 11, 'end', 700)
    body += line(90, 222, 620, 222, LIGHT, 1.2)
    body += rect(120, 198, 252, 46, '#dbeafe', BLUE, 6)
    body += t(246, 226, 'L = L₀/γ', INK, 11.5)
    body += t(400, 226, 'the rod is the same object, drawn at 0.6 L₀ for v = 0.8c', GREY, 11, 'start')
    body += t(340, 286, 'contraction happens only along the direction of motion; transverse lengths are unchanged', GREY, 11.5)
    return wrap('length-contraction', 'Length contraction',
                'A rod at rest and the same rod measured while moving, drawn shorter in the direction of motion.',
                body, caption('Figure 3.', 'The rod does not squash: the two ends are not measured at the same time in the '
                             'rod frame, and simultaneity is relative. Length contraction is time dilation seen from the '
                             'other side.'), 306)


def f_mass_energy():
    from math import sqrt as _sqrt
    def ke(beta):
        if abs(beta) >= 1:
            return 0
        return 1 / _sqrt(1 - beta * beta) - 1
    return chart(
        'mass-energy', 'Kinetic energy blows up near the speed of light',
        'The classical ½mv² agrees at low speed but is hopeless above 0.5c.',
        'v / c', 'kinetic energy (in units of mc²)',
        [('relativistic (γ − 1)', BLUE, ke),
         ('classical ½β²', AMBER, lambda x: 0.5 * x * x)],
        xr=(0, 0.99), yr=(0, 1.6), xticks=(0.2, 0.4, 0.6, 0.8), yticks=(0.5, 1, 1.5), height=355,
        xfmt='{:.1f}', yfmt='{:.1f}',
        notes=[(0.30, 1.45, 'v can never reach c', GREY)])


def f_spacetime():
    body = t(340, 24, 'A spacetime diagram: light is always at 45°', INK, 13, weight=700)
    ox, oy, w, h = 340, 300, 200, 178
    body += line(ox - w, oy, ox + w, oy, GREY, 1.6) + line(ox, oy, ox, oy - h - 26, GREY, 1.6)
    body += t(ox + w - 4, oy + 18, 'x', GREY, 12, 'end') + t(ox + 10, oy - h - 14, 'ct', GREY, 12, 'start')
    # light cone
    body += line(ox, oy, ox + w, oy - h, AMBER, 2.2) + line(ox, oy, ox - w, oy - h, AMBER, 2.2)
    body += t(ox + w - 12, oy - h + 4, 'light (45°)', AMBER, 11, 'end')
    body += line(ox, oy, ox + 90, oy - h, BLUE, 2) + t(ox + 96, oy - h - 4, 'v = 0.45c', BLUE, 11, 'start')
    body += line(ox, oy, ox + 34, oy - h, PURPLE, 2) + t(ox + 40, oy - h - 4, 'slow', PURPLE, 11, 'start')
    # the future inside the cone, shaded
    body += f'<path d="M{ox},{oy} L{ox + w},{oy - h} L{ox - w},{oy - h} Z" fill="#eff6ff" opacity="0.55"/>'
    body += dot(ox, oy, 5, INK) + t(ox - 8, oy + 18, 'now, here', GREY, 11, 'end')
    body += t(340, 330, 'the future of the origin lies inside the cone; outside it there is no causal contact', GREY, 11.5)
    return wrap('spacetime', 'The light cone',
                'A spacetime diagram with the world lines of light at 45 degrees and slower particles inside the cone.',
                body, caption('Figure 5.', 'Because every inertial observer agrees on c, the light rays are the same 45° lines '
                             'in every frame; that is what forces the Lorentz transformation, and with it the loss of absolute '
                             'simultaneity.'), 342)


FIGURES = {
    'postulates': f_postulates,
    'lorentz-factor': f_gamma,
    'time-dilation': f_timedilation,
    'length-contraction': f_length,
    'mass-energy': f_mass_energy,
    'spacetime': f_spacetime,
}


def lab_relativity():
    controls = (
        slider('rel-b', 'Speed as a fraction of c', 0.01, 0.999, 0.001, 0.80, ' [c]')
        + slider('rel-d', 'Distance travelled (lab frame)', 1, 100, 1, 10, ' [light years]')
        + slider('rel-m', 'Rest mass', 1, 1000, 1, 1, ' [kg]')
    )
    return shell(
        'relativity', 'Relativistic travel',
        'The experiment reports the Lorentz factor, the time dilation, the length contraction and the kinetic energy for '
        'a journey, and shows what the travellers would measure with their own clocks.',
        controls,
        [('gamma', 'Lorentz factor'), ('clock', 'Traveller’s proper time'), ('length', 'Contracted length'),
         ('energy', 'Kinetic energy'), ('mass', 'Relativistic mass equivalent')],
        'Set the speed to 0.999c and look at the traveller’s clock over ten light years. Then try to explain why the '
        'traveller can cross a thousand light years in a human lifetime.'
    )


LABS = {'relativity': lab_relativity}
