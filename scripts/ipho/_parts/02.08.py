"""02.08 Circuits, capacitors and inductors."""
from math import sin, cos, pi, sqrt, radians, exp


def f_rc():
    body = t(340, 24, 'A capacitor charges and discharges exponentially', INK, 13, weight=700)
    body += line(120, 250, 600, 250, GREY, 1.6)
    body += line(120, 250, 120, 62, GREY, 1.6)
    # charge curve q = 1 - exp(-t) and discharge exp(-t)
    n = 60
    ch = [(120 + 480 * i / n, 250 - 150 * (1 - exp(-3.2 * i / n))) for i in range(n + 1)]
    di = [(120 + 480 * i / n, 250 - 150 * exp(-3.2 * i / n)) for i in range(n + 1)]
    body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in ch)}" fill="none" stroke="{BLUE}" stroke-width="2.6"/>'
    body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in di)}" fill="none" stroke="{GREEN}" stroke-width="2.6" stroke-dasharray="6 4"/>'
    body += line(270, 250, 270, 66, GREY, 1.4, '4 4') + t(276, 78, 't = RC', GREY, 11, 'start')
    body += t(600, 262, 'time', GREY, 11.5, 'end') + t(112, 70, 'q', GREY, 12)
    body += t(340, 292, 'after each time constant the gap to the final value shrinks by the factor 1/e', GREY, 11.5)
    return wrap('rc', 'Exponential charging and discharging',
                'Charge rising towards C-epsilon and decaying away, with the time constant RC marked.',
                body, caption('Figure 1.', 'The two curves are mirror images: whatever fraction of the way you still have to '
                             'go, one time constant later you have covered 63% of it.'), 306)


def f_rc_circuit():
    body = t(340, 24, 'An RC circuit: the resistor sets the current, the capacitor stores the charge', INK, 13, weight=700)
    # loop: left leg x=160, top y=112, right leg x=520, bottom y=258
    body += line(160, 112, 300, 112, GREY, 2.2) + line(420, 112, 520, 112, GREY, 2.2)
    body += line(520, 112, 520, 258, GREY, 2.2) + line(520, 258, 352, 258, GREY, 2.2)
    body += line(308, 258, 160, 258, GREY, 2.2) + line(160, 258, 160, 210, GREY, 2.2)
    body += line(160, 150, 160, 112, GREY, 2.2)
    # resistor on the top leg
    body += rect(300, 90, 120, 44, '#f8fafc', GREY, 5)
    body += t(360, 116, 'R', INK, 13.5, weight=700)
    # capacitor in the bottom leg: two plates
    body += line(330, 232, 330, 284, INK, 3) + line(352, 232, 352, 284, INK, 3)
    body += t(341, 302, 'C', INK, 13, weight=700)
    # battery in the left leg
    body += line(138, 168, 182, 168, INK, 2.6) + line(148, 182, 172, 182, INK, 4.4)
    body += t(196, 174, 'ε', INK, 14, weight=700)
    body += t(360, 330, 'ε = IR + q/C  ⟹  q = Cε(1 − e^(−t/RC));   the current starts at ε/R and dies away', GREY, 11.5)
    return wrap('rc-circuit', 'Series RC circuit',
                'A battery, a resistor and a capacitor in one loop, with the voltage law written along the loop.',
                body, caption('Figure 2.', 'At t = 0 the capacitor is empty, so it behaves like a plain wire; after a long time it '
                             'is full and behaves like a break. Those two limits answer most RC questions without algebra.'), 342)


def f_rl():
    body = t(340, 24, 'An inductor delays the current: the RL circuit', INK, 13, weight=700)
    body += line(120, 250, 600, 250, GREY, 1.6) + line(120, 250, 120, 62, GREY, 1.6)
    n = 60
    cur = [(120 + 480 * i / n, 250 - 150 * (1 - exp(-3.2 * i / n))) for i in range(n + 1)]
    body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in cur)}" fill="none" stroke={chr(34)}{AMBER}{chr(34)} stroke-width="2.6"/>'
    body += line(270, 250, 270, 66, GREY, 1.4, '4 4') + t(276, 78, 't = L/R', GREY, 11, 'start')
    body += t(600, 262, 'time', GREY, 11.5, 'end') + t(112, 70, 'I', GREY, 12)
    body += t(340, 292, 'the current rises to ε/R with time constant L/R; the inductor voltage falls from ε to 0', GREY, 11.5)
    return wrap('rl', 'Current growth in an inductor',
                'Current rising towards its final value with time constant L over R.',
                body, caption('Figure 3.', 'Compare with the capacitor: there the *voltage* rises with τ = RC, here the '
                             '*current* rises with τ = L/R. An inductor is inertia for current.'), 306)


def f_lc():
    return chart(
        'lc', 'An LC circuit oscillates for ever (in the ideal case)',
        'Energy shuttles between the capacitor and the inductor with angular frequency 1/sqrt(LC).',
        'time (periods)', 'energy (arbitrary units)',
        [('electric ½CV²', BLUE, lambda t: cos(pi * t) ** 2),
         ('magnetic ½LI²', PURPLE, lambda t: sin(pi * t) ** 2)],
        xr=(0, 3), yr=(-0.05, 1.1), xticks=(0.5, 1, 1.5, 2, 2.5, 3), yticks=(0, 0.5, 1), height=345,
        xfmt='{:.1f}', yfmt='{:.1f}',
        notes=[(0.05, 1.02, 'total energy is constant', GREY)])


def f_resonance():
    from math import log10
    def response(Q):
        def f(x):
            # x is log10(omega/omega_0); amplitude of a driven series RLC current
            w = 10 ** x
            return 1 / sqrt((1 - w * w) ** 2 + (w / Q) ** 2)
        return f
    def shape(Q):
        def f(x):
            return response(Q)(x) / Q       # scale each curve to its own peak
        return f
    return chart(
        'resonance', 'Resonance: the current peaks at ω₀ = 1/√(LC)',
        'Higher Q gives a narrower peak; the full width of the peak is ω₀/Q, so a sharp resonance means a small R.',
        'log₁₀(ω/ω₀)', 'current (each curve scaled to its peak)',
        [('Q = 1', BLUE, shape(1)),
         ('Q = 5', GREEN, shape(5)),
         ('Q = 20', PURPLE, shape(20))],
        xr=(-1, 1), yr=(0, 1.05), xticks=(-1, -0.5, 0, 0.5, 1), yticks=(0, 0.5, 1), height=350,
        xfmt='{:.1f}', yfmt='{:.1f}',
        notes=[(0.02, 1.02, 'all curves pass through the same peak at ω = ω₀', GREY)])


def f_phasor():
    body = t(340, 24, 'Phasors: the same circuit drawn as rotating arrows', INK, 13, weight=700)
    cx, cy, R = 210, 160, 96
    body += circle(cx, cy, R, LIGHT, '#ffffff', 1.4, '')
    body += line(cx - R - 20, cy, cx + R + 30, cy, LIGHT, 1.4) + line(cx, cy - R - 20, cx, cy + R + 20, LIGHT, 1.4)
    body += arrow('phasor', cx, cy, cx + R * cos(radians(-35)), cy + R * sin(radians(-35)), AMBER, 2.8)
    body += t(cx + R * cos(radians(-35)) + 14, cy + R * sin(radians(-35)) - 6, 'V_R = IR', AMBER, 11.5, 'start', 700)
    body += arrow('phasor', cx, cy, cx, cy - R * 0.75, PURPLE, 2.8)
    body += t(cx - 8, cy - R * 0.78, 'V_L', PURPLE, 12, 'end', 700)
    body += arrow('phasor', cx, cy, cx + R * cos(radians(105)) * 0.8, cy + R * sin(radians(105)) * 0.8, BLUE, 2.8)
    body += t(cx + R * cos(radians(105)) * 0.8 - 10, cy + R * sin(radians(105)) * 0.8 - 10, 'V_C', BLUE, 12, 'end', 700)
    body += t(500, 118, 'V_L leads the current by 90°', GREEN, 11.5, 'start')
    body += t(500, 142, 'V_C lags by 90°', GREEN, 11.5, 'start')
    body += t(500, 166, 'V_R is in phase', GREEN, 11.5, 'start')
    body += t(500, 196, 'Z = √(R² + (X_L − X_C)²)', INK, 12, 'start', 700)
    body += t(340, 292, 'add the voltages as vectors, not as numbers: the phases matter', GREY, 11.5)
    return wrap('phasor', 'Phasor diagram for a series RLC circuit',
                'Three rotating arrows for the voltages across R, L and C, with the impedance triangle in words.',
                body, caption('Figure 5.', 'At resonance X_L = X_C, the two reactive arrows cancel, and the current is limited '
                             'only by R — which is why a high-Q circuit can carry enormous currents.'), 306)


FIGURES = {
    'rc': f_rc,
    'rc-circuit': f_rc_circuit,
    'rl': f_rl,
    'lc': f_lc,
    'resonance': f_resonance,
    'phasor': f_phasor,
}


def lab_rlc():
    controls = (
        slider('rlc-r', 'Resistance', 1, 100, 1, 10, ' [Ω]')
        + slider('rlc-l', 'Inductance', 1, 200, 1, 50, ' [mH]')
        + slider('rlc-c', 'Capacitance', 1, 200, 1, 20, ' [μF]')
    )
    return shell(
        'rlc', 'Resonance in a series RLC circuit',
        'Change R, L and C and watch the resonant frequency, the quality factor and the peak current. The output also '
        'reports the voltages across each element at resonance, so you can see how they can exceed the supply voltage.',
        controls,
        [('f0', 'Resonant frequency'), ('q', 'Quality factor'), ('bw', 'Bandwidth'),
         ('imax', 'Peak current'), ('vc', 'Voltage across C at resonance')],
        'Set R = 1 Ω and note how large the voltage across the capacitor becomes. Where does that energy come from, and '
        'what limits the current in a real circuit?'
    )


LABS = {'rlc': lab_rlc}
