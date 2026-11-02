"""02.07 Magnetic fields and induction."""
from math import sin, cos, pi, sqrt, radians, exp


def f_biot_savart():
    body = t(340, 24, 'A current produces a circulating magnetic field', INK, 13, weight=700)
    body += line(340, 54, 340, 256, AMBER, 4) + t(340, 46, 'I', AMBER, 13, weight=700)
    for r in (34, 66, 98):
        body += circle(340, 155, r, BLUE, 'none', 2.2, '')
        # field circulates: arrow tangent to the circle at its right-hand point
        body += arrow('biot', 340 + r, 155 - 22, 340 + r, 155 + 22, BLUE, 1.8)
    body += t(452, 96, 'B = μ₀I/(2πr)', INK, 12.5, 'start', 700)
    body += t(452, 118, 'circles around the wire', GREY, 11.5, 'start')
    body += t(452, 140, 'right-hand rule: thumb = I,', GREY, 11.5, 'start')
    body += t(452, 160, 'fingers curl along B', GREY, 11.5, 'start')
    body += t(340, 292, 'Inside a long solenoid B = μ₀nI, nearly uniform; outside it is nearly zero.', GREY, 11.5)
    return wrap('biot', 'The field of a straight current',
                'Concentric circles of magnetic field around a straight wire, with the right-hand rule.',
                body, caption('Figure 1.', 'The field lines are closed loops with no start or end: there are no magnetic '
                             'monopoles, which is why ∇·B = 0.'), 306)


def f_force():
    from math import sin, cos, pi
    body = t(340, 24, 'A charge in a magnetic field bends; the force is perpendicular to the motion', INK, 13, weight=700)
    for x in range(110, 600, 60):
        for y in (56, 76):
            body += t(x, y, '×', GREY, 13)
    body += t(600, 100, 'B into the page', GREY, 11.5, 'end')
    cx, cy, R = 340, 205, 84
    body += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>'
    # particle at the top of the circle, moving right, force pointing to the centre
    px, py = cx, cy - R
    body += dot(px, py, 7, AMBER)
    body += arrow('force', px + 8, py, px + 86, py, GREEN, 2.6) + t(px + 44, py - 10, 'v', GREEN, 12, weight=700)
    body += arrow('force', px, py + 6, px, py + R - 16, PURPLE, 2.6) + t(px + 12, py + 44, 'F = qv × B', PURPLE, 11.5, 'start', 700)
    body += t(340, 318, 'The magnetic force does no work: it changes direction, never speed.', GREY, 11.5)
    body += t(340, 340, 'Radius of the circular path r = mv/(qB);   cyclotron frequency ω = qB/m.', GREY, 11.5)
    return wrap('force', 'Magnetic deflection of a moving charge',
                'A charge moving in a field pointing into the page follows a circle, with velocity tangent and force inward.',
                body, caption('Figure 2.', 'Because the force is always perpendicular to v, the magnetic field cannot change '
                             'a particle’s kinetic energy — a fact that solves many olympiad questions instantly.'), 380)


def f_induction():
    return chart(
        'induction', 'Faraday’s law: the emf is the rate of change of flux',
        'A loop rotating in a uniform field produces a sinusoidal emf; a coil entering a field experiences a growing then falling flux.',
        'time (arbitrary units)', 'flux and emf (arbitrary units)',
        [('flux Φ', BLUE, lambda t: cos(t)),
         ('emf −dΦ/dt', GREEN, lambda t: sin(t))],
        xr=(0, 6.2), yr=(-1.2, 1.2), xticks=(1, 2, 3, 4, 5, 6), yticks=(-1, 0, 1), height=340,
        xfmt='{:.0f}', yfmt='{:.0f}',
        notes=[(0.15, 1.05, 'emf peaks where the flux changes fastest', GREY)])


def f_lorentz():
    body = t(340, 24, 'A conductor moving through a field: motional emf', INK, 13, weight=700)
    body += rect(100, 80, 480, 150, '#f8fafc', '#e2e8f0', 4)
    for x in range(130, 580, 56):
        body += t(x, 70, '×', GREY, 13)
    body += rect(250, 104, 14, 120, AMBER, AMBER, 3)
    body += arrow('lorentz', 264, 190, 372, 190, GREEN, 3) + t(318, 208, 'v', GREEN, 12, weight=700)
    body += circle(268, 132, 4, PURPLE) + circle(268, 212, 4, PURPLE)
    body += t(340, 256, 'motional emf  ε = Bℓv,  with a current driven by the Lorentz force on the charges', GREY, 11.5)
    body += t(340, 282, 'Lenz’s law: the induced current opposes the change in flux that created it', INK, 12.5)
    return wrap('lorentz', 'Motional emf in a moving rod',
                'A conducting rod sliding on rails through a field into the page.',
                body, caption('Figure 3.', 'The rod experiences a retarding force BIℓ, so pushing it at constant speed '
                             'requires mechanical power exactly equal to the electrical power I²R.'), 306)


def f_magnetic_energy():
    body = t(340, 24, 'Inductance opposes change: it is electrical inertia', INK, 13, weight=700)
    body += rect(120, 96, 190, 110, '#f3e8ff', PURPLE, 6)
    body += t(215, 132, 'inductor', INK, 12.5, weight=700)
    body += t(215, 158, 'V = L dI/dt', INK, 13.5, weight=700)
    body += t(215, 182, 'U = ½LI²', GREY, 11.5)
    body += rect(370, 96, 190, 110, '#dbeafe', BLUE, 6)
    body += t(465, 132, 'resistor', INK, 12.5, weight=700)
    body += t(465, 158, 'V = IR', INK, 13.5, weight=700)
    body += t(465, 182, 'U = none (heat)', GREY, 11.5)
    body += arrow('magnetic-energy', 312, 151, 368, 151, GREY, 2.4)
    body += t(340, 240, 'Current in an inductor cannot change instantaneously — the same way velocity cannot.', INK, 12.5)
    body += t(340, 266, 'Time constant L/R replaces RC; the energy sits in the magnetic field.', GREY, 11.5)
    return wrap('magnetic-energy', 'The inductor as electrical inertia',
                'An inductor and a resistor side by side with their voltage laws.',
                body, caption('Figure 4.', 'An inductor stores energy in its field and resists current change; a resistor '
                             'dissipates energy and does not resist change, only flow.'), 296)


FIGURES = {
    'biot': f_biot_savart,
    'force': f_force,
    'induction': f_induction,
    'lorentz': f_lorentz,
    'magnetic-energy': f_magnetic_energy,
}


def lab_cyclotron():
    controls = (
        slider('cyc-m', 'Particle mass (proton units)', 1, 40, 1, 1, ' [u]')
        + slider('cyc-q', 'Charge (e)', 1, 3, 1, 1, ' [e]')
        + slider('cyc-B', 'Magnetic field', 0.05, 2.0, 0.05, 0.5, ' [T]')
        + slider('cyc-v', 'Speed', 0.5, 20, 0.5, 5, ' [Mm/s]')
    )
    return shell(
        'cyclotron', 'Circular motion in a magnetic field',
        'A charged particle enters a uniform field perpendicular to its velocity. The experiment reports the radius, '
        'the cyclotron frequency and the kinetic energy, and draws the orbit to scale.',
        controls,
        [('r', 'Orbit radius'), ('f', 'Cyclotron frequency'), ('T', 'Period'),
         ('k', 'Kinetic energy'), ('check', 'Radius ∝ momentum?')],
        'Keep the speed fixed and double the field: what happens to the radius and the frequency? Then double the mass: '
        'which of the two stays unchanged?'
    )


LABS = {'cyclotron': lab_cyclotron}
