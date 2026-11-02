"""02.14 Structure of matter and nuclear physics."""
from math import sin, cos, pi, sqrt, radians, exp, log10, log2


def f_rutherford():
    from math import sin as _sin, cos as _cos, radians as _rad
    body = t(340, 24, 'Rutherford scattering: most alphas pass, a few bounce back', INK, 13, weight=700)
    # gold foil
    body += line(300, 70, 300, 260, '#fcd34d', 6)
    body += t(300, 62, 'gold foil', AMBER, 11)
    body += dot(300, 165, 4, RED)
    # paths
    paths = [(-4, 6, AMBER), (0, 0, AMBER), (3, -8, AMBER)]
    for dy_in, dy_out, col in paths:
        body += arrow('ruth', 90, 165 + dy_in * 6, 296, 165, col, 1.6)
        body += arrow('ruth', 304, 165, 560, 165 + dy_out * 10, col, 1.6)
    # backscattered path
    body += arrow('ruth', 120, 236, 296, 168, PURPLE, 2.2)
    body += arrow('ruth', 296, 168, 120, 100, PURPLE, 2.2)
    body += t(150, 96, 'backscattered (1 in 8000)', PURPLE, 11, 'start', 700)
    body += t(430, 250, 'deflected slightly', AMBER, 11, 'start')
    body += t(340, 292, 'the nucleus is small and dense: most of the atom is empty space', GREY, 11.5)
    return wrap('rutherford', 'Rutherford’s alpha-particle scattering',
                'Alpha particles crossing a thin gold foil: most go straight on, a few are deflected or reflected.',
                body, caption('Figure 1.', 'A diffuse positive charge could not turn an alpha particle round. Only a tiny, '
                             'heavy, positively charged nucleus can, which is how the nuclear model was established in 1911.'), 306)


def f_decay():
    return chart(
        'decay-curve', 'Radioactive decay is exponential: a constant fraction per unit time',
        'After each half-life half the nuclei remain, whatever the starting number.',
        'time (half-lives)', 'fraction remaining',
        [('N/N₀', BLUE, lambda t: 0.5 ** t),
         ('activity A/A₀', GREEN, lambda t: 0.5 ** t, '6 4')],
        xr=(0, 5), yr=(-0.02, 1.02), xticks=(1, 2, 3, 4, 5), yticks=(0, 0.25, 0.5, 0.75, 1), height=355,
        xfmt='{:.0f}', yfmt='{:.2f}')


def f_binding():
    def ba(a):
        if a < 2:
            return 0
        return 8.8 * (1 - exp(-a / 8.0)) - 0.0065 * a
    return chart(
        'binding-energy', 'Binding energy per nucleon peaks near iron',
        'Fusion of light nuclei and fission of heavy ones both climb towards the peak, and both release energy.',
        'mass number A', 'binding energy per nucleon (MeV)',
        [('B/A', BLUE, ba)],
        xr=(0, 250), yr=(0, 9.5), xticks=(50, 100, 150, 200, 250), yticks=(2, 4, 6, 8), height=355,
        xfmt='{:.0f}', yfmt='{:.0f}',
        notes=[(56, 8.6, 'Fe-56: the peak', GREY)])


def f_decay_chain():
    body = t(340, 24, 'A decay chain: alpha steps go down-left, beta steps go up', INK, 13, weight=700)
    body += line(110, 250, 610, 250, GREY, 1.6) + line(110, 66, 110, 250, GREY, 1.6)
    body += t(610, 268, 'neutron number N', GREY, 11, 'end') + t(102, 74, 'Z', GREY, 12, 'end', 700)
    # (N, Z) positions: x = 120 + (N-134)*11, y = 248 - (Z-84)*13
    chain = [('²³⁸U', 146, 92), ('²³⁴Th', 144, 90), ('²³⁴Pa', 143, 91), ('²³⁴U', 142, 92),
             ('²³⁰Th', 140, 90), ('²²⁶Ra', 138, 88), ('²²²Rn', 136, 86)]
    pts = []
    for name, N, Z in chain:
        x, y = 250 + (N - 141) * 36, 252 - (Z - 84) * 24
        pts.append((x, y, name))
    for k in range(len(pts) - 1):
        x1, y1, _ = pts[k]
        x2, y2, _ = pts[k + 1]
        body += line(x1, y1, x2, y2, GREY, 1.6, '4 3')
    for k, (x, y, name) in enumerate(pts):
        body += dot(x, y, 5.5, BLUE)
        anchor = 'end' if k % 2 else 'start'
        dx = -10 if k % 2 else 10
        body += t(x + dx, y + 4, name, INK, 11, anchor, 700)
    body += t(470, 88, 'α decay:  Z − 2,  A − 4', PURPLE, 12, 'start', 700)
    body += t(470, 112, 'β⁻ decay:  Z + 1,  A unchanged', GREEN, 12, 'start', 700)
    body += t(340, 292, 'each step conserves charge and nucleon number; the chain ends at a stable isotope of lead', GREY, 11.5)
    return wrap('decay-chain', 'An alpha and beta decay chain',
                'A staircase of nuclides in the neutron-number versus proton-number plane.',
                body, caption('Figure 2.', 'Alpha decay removes two protons and two neutrons, so it moves a nuclide down and '
                             'to the left; beta decay turns a neutron into a proton, moving it up. The chain zigzags towards '
                             'the line of stability.'), 306)


def f_fission_fusion():
    body = t(340, 24, 'Both ends of the curve release energy — but only one is easy on Earth', INK, 13, weight=700)
    # fusion panel
    body += rect(80, 74, 240, 150, '#eff6ff', BLUE, 8)
    body += t(200, 100, 'fusion', BLUE, 13, weight=700)
    body += dot(150, 140, 7, AMBER) + dot(176, 140, 7, AMBER) + dot(250, 140, 9, GREEN)
    body += t(200, 176, '²H + ³H → ⁴He + n', INK, 11)
    body += t(200, 198, '+ 17.6 MeV', GREEN, 11.5, weight=700)
    # fission panel
    body += rect(360, 74, 240, 150, '#fff7ed', AMBER, 8)
    body += t(480, 100, 'fission', AMBER, 13, weight=700)
    body += dot(440, 140, 9, AMBER) + dot(470, 140, 4, GREY)
    body += dot(520, 128, 6, GREEN) + dot(520, 156, 6, GREEN)
    body += t(480, 176, '²³⁵U + n → Ba + Kr + 3n', INK, 11)
    body += t(480, 198, '+ 200 MeV', GREEN, 11.5, weight=700)
    body += t(340, 250, 'fusion releases more energy per kilogram; fission is easier to start and control', GREY, 11.5)
    body += t(340, 288, 'in both cases the products are more tightly bound, and the missing mass appears as kinetic energy', GREY, 11.5)
    return wrap('fission-fusion', 'Fission and fusion',
                'Two panels comparing a fusion reaction and a fission reaction with their energy releases.',
                body, caption('Figure 3.', 'The energy comes from the mass difference: the products are lighter than the '
                             'reactants by about 0.1% (fission) to 0.4% (fusion) of the total mass, and $E = \Delta mc^2$.'), 306)


def f_quarks():
    body = t(340, 24, 'Protons and neutrons are made of up and down quarks', INK, 13, weight=700)
    for cx, label, parts, colour in ((200, 'proton  uud  (+1)', (('u', +2 / 3), ('u', +2 / 3), ('d', -1 / 3)), BLUE),
                                     (470, 'neutron  udd  (0)', (('u', +2 / 3), ('d', -1 / 3), ('d', -1 / 3)), GREEN)):
        body += circle(cx, 160, 62, '#f8fafc', colour, 2.4, '')
        for i, (q, charge) in enumerate(parts):
            ang = radians(-90 + 120 * i)
            x, y = cx + 30 * cos(ang), 160 + 30 * sin(ang)
            body += dot(x, y, 11, AMBER if q == 'u' else PURPLE)
            body += t(x, y + 4, q, '#ffffff', 11, weight=700)
        body += t(cx, 250, label, colour, 11.5, weight=700)
    body += t(340, 288, 'u = +2/3 e, d = −1/3 e;  gluons hold them together, and the strong force is what binds nuclei', GREY, 11.5)
    return wrap('quarks', 'Quark structure of the nucleons',
                'A proton and a neutron drawn as circles containing three quarks each.',
                body, caption('Figure 4.', 'The quark charges add to the observed nucleon charges: $2/3+2/3-1/3 = +1$ for '
                             'the proton, and $2/3-1/3-1/3 = 0$ for the neutron. Quarks never appear alone.'), 306)


def f_halflife_table():
    return chart(
        'decay-activity', 'Activity falls with the same half-life as the number of nuclei',
        'A short half-life means a high activity, and a sample decays away quickly.',
        'time (years)', 'fraction of nuclei remaining',
        [('T½ = 1 year', BLUE, lambda t: 0.5 ** t),
         ('T½ = 5 years', GREEN, lambda t: 0.5 ** (t / 5)),
         ('T½ = 20 years', PURPLE, lambda t: 0.5 ** (t / 20))],
        xr=(0, 20), yr=(-0.02, 1.02), xticks=(5, 10, 15, 20), yticks=(0, 0.5, 1), height=350,
        xfmt='{:.0f}', yfmt='{:.1f}')


FIGURES = {
    'rutherford': f_rutherford,
    'decay-curve': f_decay,
    'binding-energy': f_binding,
    'decay-chain': f_decay_chain,
    'fission-fusion': f_fission_fusion,
    'quarks': f_quarks,
    'decay-activity': f_halflife_table,
}


def lab_decay():
    controls = (
        slider('dec-h', 'Half-life', 0.5, 20, 0.5, 5, ' [s]')
        + slider('dec-n', 'Initial number of nuclei', 100, 10000, 100, 2000, '')
        + slider('dec-t', 'Elapsed time', 0, 60, 0.5, 10, ' [s]')
    )
    return shell(
        'decay', 'Radioactive decay and activity',
        'The experiment simulates a sample of nuclei decaying with a given half-life, reports how many are left and the '
        'activity, and draws both the smooth exponential and the actual random decay of a finite sample.',
        controls,
        [('left', 'Nuclei remaining'), ('frac', 'Fraction remaining'), ('A', 'Activity (Bq)'),
         ('lambda', 'Decay constant'), ('tau', 'Mean lifetime')],
        'Set the initial number to 100 and run the time forward: why is the actual decay jagged while the smooth curve is '
        'not? Then double the half-life and see what happens to the activity.'
    )


LABS = {'decay': lab_decay}
