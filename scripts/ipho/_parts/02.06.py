"""02.06 Electrostatics and steady currents."""
from math import sqrt, pi, exp


def f_field():
    body = t(340, 24, 'Field lines start on positive charge and end on negative charge', INK, 13, weight=700)
    body += circle(200, 150, 22, RED, '#fee2e2', 2.4) + t(200, 158, '+', '#b91c1c', 22, weight=700)
    body += circle(480, 150, 22, BLUE, '#dbeafe', 2.4) + t(480, 158, '−', BLUE, 22, weight=700)
    for dy in (-52, -26, 0, 26, 52):
        body += arrow('field', 226, 150 + dy * 0.5, 452, 150 + dy * 0.5, BLUE, 1.8 if dy else 2.6)
    body += t(340, 262, 'Density of lines ∝ field strength; arrows point from + to −', GREY, 11.5)
    body += t(340, 286, 'E = F/q   and   V = W/q — field is force per charge, potential is energy per charge',
              INK, 12)
    return wrap('field', 'Electric field of a dipole',
                'Field lines leaving a positive charge and entering a negative one.',
                body, caption('Figure 1.', 'The field is a vector at every point; the potential is a scalar. The field '
                             'points along the downhill direction of the potential.'), 306)


def f_gauss():
    body = t(340, 24, 'Gauss’s law: the flux through a closed surface depends only on enclosed charge', INK, 13, weight=700)
    body += circle(340, 150, 34, RED, '#fee2e2', 2.4) + t(340, 156, '+Q', '#b91c1c', 13, weight=700)
    body += circle(340, 150, 76, BLUE, 'none', 2, '6 4')
    body += circle(340, 150, 112, BLUE, 'none', 2, '6 4')
    for ang in range(0, 360, 30):
        from math import cos, sin, radians
        a = radians(ang)
        body += arrow('gauss', 340 + 80 * cos(a), 150 + 80 * sin(a), 340 + 120 * cos(a), 150 + 120 * sin(a), BLUE, 1.6)
    body += t(340, 292, '∮E·dA = Q/ε₀ — the same flux for any surface around the charge', GREY, 11.5)
    body += t(470, 84, 'two surfaces,', GREY, 11.5, 'start')
    body += t(470, 102, 'same flux', GREY, 11.5, 'start')
    return wrap('gauss', 'Gauss’s law and enclosing surfaces',
                'Two closed surfaces of different sizes enclosing the same charge, penetrated by the same flux.',
                body, caption('Figure 2.', 'Gauss’s law is only useful when symmetry makes E constant over the surface: '
                             'spheres, cylinders, infinite planes.'), 306)


def f_coulomb():
    return chart(
        'coulomb', 'Coulomb’s law: inverse square, and potential as 1/r',
        'Force falls as 1/r² while potential energy falls only as 1/r — that difference is why bound states exist.',
        'separation r (arbitrary units)', 'force and potential (arbitrary units)',
        [('force ∝ 1/r²', BLUE, lambda r: 1 / (r * r) if r else None),
         ('potential ∝ 1/r', GREEN, lambda r: 1 / r if r else None)],
        xr=(0.5, 4), yr=(0, 4), xticks=(1, 2, 3, 4), yticks=(0, 1, 2, 3, 4), height=340,
        notes=[(0.6, 3.6, 'both diverge as r → 0; the force does so faster', GREY)])


def f_circuit():
    body = t(340, 24, 'Kirchhoff’s rules are charge and energy conservation in disguise', INK, 13, weight=700)
    body += rect(140, 76, 400, 170, 'none', GREY, 4, 2)
    body += rect(300, 66, 70, 20, '#e2e8f0', GREY, 2) + t(335, 60, 'ε', INK, 13, weight=700)
    body += rect(156, 100, 16, 60, '#fef3c7', AMBER, 2) + t(130, 134, 'R₁', AMBER, 12, 'end', 700)
    body += rect(508, 100, 16, 60, '#fef3c7', AMBER, 2) + t(540, 134, 'R₂', AMBER, 12, 'start', 700)
    body += rect(280, 238, 120, 16, '#dbeafe', BLUE, 2) + t(340, 272, 'R₃', BLUE, 12, weight=700)
    body += arrow('circuit', 240, 84, 300, 84, GREEN, 2) + t(268, 74, 'I', GREEN, 12)
    body += arrow('circuit', 370, 86, 430, 86, GREEN, 2)
    body += arrow('circuit', 470, 130, 470, 200, GREEN, 2)
    body += arrow('circuit', 200, 200, 200, 130, GREEN, 2)
    body += arrow('circuit', 340, 246, 420, 246, GREEN, 2) + t(380, 236, 'I₃', GREEN, 12)
    body += t(340, 300, 'Σ I into a node = Σ I out (charge),   Σ ΔV around a loop = 0 (energy)', GREY, 11.5)
    return wrap('circuit', 'A two-loop circuit',
                'A battery driving current through three resistors with two junctions and three loops.',
                body, caption('Figure 4.', 'Choose a current direction for each branch, apply the junction rule, then the '
                             'loop rule. A negative answer simply means the current flows the other way.'), 320)


def f_energy_density():
    body = t(340, 24, 'Where the energy of a capacitor and an inductor is stored', INK, 13, weight=700)
    body += rect(120, 90, 190, 120, '#dbeafe', BLUE, 6)
    body += t(215, 130, 'capacitor', INK, 12.5, weight=700)
    body += t(215, 156, 'U = ½CV²', INK, 14, weight=700)
    body += t(215, 182, 'energy in the field', GREY, 11)
    body += rect(370, 90, 190, 120, '#f3e8ff', PURPLE, 6)
    body += t(465, 130, 'inductor', INK, 12.5, weight=700)
    body += t(465, 156, 'U = ½LI²', INK, 14, weight=700)
    body += t(465, 182, 'energy in the field', GREY, 11)
    body += arrow('energy-density', 312, 150, 368, 150, GREY, 2.4)
    body += t(340, 244, 'LC circuit: energy sloshes between them at ω = 1/√(LC)', INK, 12.5, weight=700)
    body += t(340, 270, 'time constant RC = τ for charging, L/R for current rise', GREY, 11.5)
    return wrap('energy-density', 'The LC analogy',
                'A capacitor and an inductor exchanging energy, with the formulas for stored energy.',
                body, caption('Figure 5.', 'A capacitor is the electrical analogue of a spring, an inductor the analogue of '
                             'mass: the oscillation frequency is 1/√(LC) exactly as 1/√(m/k) in mechanics.'), 296)


FIGURES = {
    'field': f_field,
    'gauss': f_gauss,
    'coulomb': f_coulomb,
    'circuit': f_circuit,
    'energy-density': f_energy_density,
}


def lab_divider():
    controls = (
        slider('div-v', 'Supply voltage', 1, 24, 0.5, 12, ' [V]')
        + slider('div-r1', 'R₁', 100, 10000, 100, 2200, ' [Ω]')
        + slider('div-r2', 'R₂', 100, 10000, 100, 4700, ' [Ω]')
        + slider('div-rl', 'Load R_L', 1000, 100000, 1000, 100000, ' [Ω]')
    )
    return shell(
        'divider', 'The loaded potential divider',
        'The divider sets the output voltage from the ratio R₂/(R₁+R₂), but only when nothing draws current. '
        'The experiment adds a load and reports the error the ideal formula makes.',
        controls,
        [('ideal', 'Ideal output'), ('real', 'Loaded output'), ('err', 'Error'),
         ('power', 'Power in divider'), ('eff', 'Fraction delivered')],
        'Start with R_L very large: the loaded and ideal outputs agree. Now drop R_L below R₂ and watch the output '
        'collapse. Why is a divider unsuitable as a power supply?'
    )


LABS = {'divider': lab_divider}
