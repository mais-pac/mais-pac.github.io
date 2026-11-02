"""02.05 Hydrodynamics and surface tension."""
from math import sqrt, pi, cos, sin, radians


def f_pressure():
    body = t(340, 24, 'Pressure is force per area, and it acts in every direction', INK, 13, weight=700)
    body += rect(120, 90, 180, 130, '#dbeafe', BLUE, 4)
    body += t(210, 150, 'fluid', INK, 13, weight=700)
    body += arrow('pressure', 210, 90, 210, 34, BLUE, 2.4)
    body += arrow('pressure', 210, 220, 210, 276, BLUE, 2.4)
    body += arrow('pressure', 120, 155, 64, 155, BLUE, 2.4)
    body += arrow('pressure', 300, 155, 356, 155, BLUE, 2.4)
    body += arrow('pressure', 160, 120, 118, 78, BLUE, 2.0)
    body += arrow('pressure', 260, 190, 302, 232, BLUE, 2.0)
    body += t(340, 96, 'p = F/A', INK, 14, weight=700, anchor='start')
    body += t(340, 122, 'same in all directions', GREY, 11.5, anchor='start')
    body += t(340, 148, 'p increases with depth:', GREY, 11.5, anchor='start')
    body += t(340, 174, 'p = p₀ + ρgh', PURPLE, 13, anchor='start', weight=700)
    body += t(340, 200, 'The shape of the container', GREY, 11.5, anchor='start')
    body += t(340, 220, 'does not matter.', GREY, 11.5, anchor='start')
    body += t(340, 290, 'A fluid transmits pressure without a preferred direction; a solid transmits force along its axis.',
              GREY, 11.5)
    return wrap('pressure', 'Pressure is isotropic; force is not',
                'A fluid element feels pressure on every face; the pressure grows linearly with depth.',
                body, caption('Figure 1.', 'Pascal’s principle follows from this isotropy: a pressure change applied '
                             'at one point is transmitted undiminished throughout an enclosed fluid.'), 306)


def f_continuity():
    body = t(340, 24, 'Continuity: what goes in must come out', INK, 13, weight=700)
    body += poly([(60, 130), (250, 130), (330, 160), (600, 160), (600, 220), (330, 220), (250, 190), (60, 190)],
                 '#dbeafe', BLUE, 2)
    for i in range(4):
        x = 90 + i * 42
        body += arrow('continuity', x, 160, x + 30, 160, BLUE, 2)
    for i in range(5):
        x = 380 + i * 42
        body += arrow('continuity', x, 190, x + 26, 190, GREY, 1.8)
    body += t(150, 116, 'wide, slow', BLUE, 11.5, weight=700)
    body += t(470, 146, 'narrow, fast', AMBER, 11.5, weight=700)
    body += t(340, 258, 'A₁v₁ = A₂v₂ for an incompressible fluid', INK, 13, weight=700)
    body += t(340, 284, 'Halve the area and you double the speed; the pressure then drops by Bernoulli’s law.',
              GREY, 11.5)
    return wrap('continuity', 'The continuity equation',
                'A pipe narrowing from a wide to a narrow section; the flow speeds up.',
                body, caption('Figure 2.', 'Continuity is mass conservation for an incompressible fluid. It is why a '
                             'river runs faster in a narrow gorge than over a wide floodplain.'), 300)


def f_bernoulli():
    return chart(
        'bernoulli', 'Bernoulli: where the speed is high, the pressure is low',
        'Along a streamline p + ½ρv² + ρgh is constant. Raising the pipe raises the pressure term by ρgh; narrowing it lowers it.',
        'distance along the pipe (m)', 'pressure head and speed head (kPa)',
        [('pressure p (kPa)', BLUE, lambda x: 24 - 0.5 * 1000 * (2 + 1.6 * sin(x / 3)) ** 2 / 1000),
         ('dynamic term ½ρv² (kPa)', GREEN, lambda x: 0.5 * 1000 * (2 + 1.6 * sin(x / 3)) ** 2 / 1000)],
        xr=(0, 12), yr=(0, 30), xticks=(2, 4, 6, 8, 10), yticks=(0, 10, 20, 30), height=340,
        notes=[(0.25, 27, 'p + ½ρv² is constant along a level pipe', GREY)])


def f_buoyancy():
    body = t(340, 24, 'Archimedes: the buoyant force equals the weight of displaced fluid', INK, 13, weight=700)
    body += rect(80, 96, 520, 172, '#dbeafe', '#93c5fd', 4)
    body += line(80, 96, 600, 96, '#60a5fa', 2)
    body += rect(250, 156, 160, 96, '#fef3c7', AMBER, 4)
    body += t(330, 212, 'block', INK, 12, weight=700)
    body += arrow('buoyancy', 330, 160, 330, 110, GREEN, 2.6) + t(346, 126, 'upthrust ρ_f V g', GREEN, 11.5, 'start', 700)
    body += arrow('buoyancy', 330, 250, 330, 300, AMBER, 2.6) + t(346, 286, 'weight ρ_b V g', AMBER, 11.5, 'start', 700)
    body += t(120, 130, 'ρ_f', BLUE, 13, weight=700)
    body += t(340, 82, 'It floats when ρ_b < ρ_f and sinks when ρ_b > ρ_f.', GREY, 11.5)
    body += t(340, 306, 'The upthrust depends on the fluid and the displaced volume — never on the body’s own mass.',
              GREY, 11.5)
    return wrap('buoyancy', 'Buoyancy on a submerged block',
                'A block in a fluid with the upthrust and its weight drawn separately.',
                body, caption('Figure 4.', 'Archimedes’ principle is a pressure-integration result: the pressure at '
                             'the bottom of the block exceeds that at the top, and the difference is the weight of displaced fluid.'), 320)


def f_surface():
    body = t(340, 24, 'Surface tension: a liquid behaves as if it had a skin', INK, 13, weight=700)
    pts = [(120 + 460 * (i / 60), 150 - 46 * sin(pi * i / 60)) for i in range(61)]
    body += polyline(pts, BLUE, 3)
    body += arrow('surface', 200, 128, 200, 96, GREY, 2.2)
    body += arrow('surface', 340, 104, 340, 72, GREY, 2.2)
    body += arrow('surface', 480, 128, 480, 96, GREY, 2.2)
    body += t(340, 60, 'surface tension γ pulls the surface into the smallest area it can reach', GREY, 11.5)
    body += t(340, 196, 'γ has units N/m or J/m²  —  force per unit length or energy per unit area', INK, 12.5, weight=700)
    body += t(340, 224, 'pressure difference across a curved surface:  Δp = 2γ/r  (a bubble, two surfaces)', GREY, 11.5)
    body += t(340, 250, 'capillary rise:  h = 2γcosθ/(ρgr)', GREY, 11.5)
    body += t(340, 276, 'both follow from balancing γ against pressure or weight — no extra physics is needed', GREY, 11.5)
    return wrap('surface', 'Surface tension in one picture',
                'A liquid surface curved like a membrane, with the tension forces and the resulting formulas.',
                body, caption('Figure 5.', 'Small objects can float on water not because they are light but because '
                             'deforming the surface costs energy γΔA.'), 300)


FIGURES = {
    'pressure': f_pressure,
    'continuity': f_continuity,
    'bernoulli': f_bernoulli,
    'buoyancy': f_buoyancy,
    'surface': f_surface,
}


def lab_torricelli():
    controls = (
        slider('tor-h', 'Water depth h', 0.05, 5, 0.05, 1.0, ' [m]')
        + slider('tor-H', 'Hole height above ground', 0, 5, 0.05, 0, ' [m]')
        + slider('tor-d', 'Hole diameter d', 2, 40, 1, 10, ' [mm]')
    )
    return shell(
        'torricelli', 'A tank with a hole: Torricelli’s law and the jet',
        'Bernoulli’s equation between the free surface and the hole gives v = √(2gh). The jet then follows projectile '
        'motion, so the range is 2√(h(H)) where the geometry allows.',
        controls,
        [('v', 'Jet speed'), ('range', 'Horizontal range'), ('flow', 'Volume flow rate'), ('time', 'Time to empty')],
        'Hold d fixed and double h: what happens to the speed, the range and the flow rate? Then put the hole at the '
        'bottom (H = 0): why does the range not go to zero even though the jet is fastest there?'
    )


LABS = {'torricelli': lab_torricelli}
