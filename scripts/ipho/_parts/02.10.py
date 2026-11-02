"""02.10 Waves, sound and the Doppler effect."""
from math import sin, cos, pi, sqrt, radians, exp, log10


def f_wave():
    return chart(
        'wave', 'A travelling wave: the snapshot moves, the medium does not',
        'At a fixed time the wave is a sinusoid in space; at a fixed point it is a sinusoid in time.',
        'position (wavelengths)', 'displacement',
        [('t = 0', BLUE, lambda x: sin(2 * pi * x)),
         ('t = T/4', GREEN, lambda x: sin(2 * pi * (x - 0.25))),
         ('t = T/2', PURPLE, lambda x: sin(2 * pi * (x - 0.5)))],
        xr=(0, 2), yr=(-1.2, 1.2), xticks=(0.5, 1, 1.5, 2), yticks=(-1, 0, 1), height=350,
        xfmt='{:.1f}', yfmt='{:.0f}')


def f_superposition():
    body = t(340, 24, 'Superposition: two waves add point by point', INK, 13, weight=700)
    left, right = 100, 620
    rows = [('wave 1', BLUE, 92, lambda x: 0.55 * sin(2 * pi * x * 2)),
            ('wave 2', GREEN, 172, lambda x: 0.40 * sin(2 * pi * x * 2 + pi / 3)),
            ('sum', PURPLE, 252, lambda x: 0.55 * sin(2 * pi * x * 2) + 0.40 * sin(2 * pi * x * 2 + pi / 3))]
    for label, colour, base, fn in rows:
        pts = [(left + (right - left) * i / 200, base - 34 * fn(i / 200)) for i in range(201)]
        body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{colour}" stroke-width="2.4"/>'
        body += t(left - 12, base + 4, label, colour, 11.5, 'end', 700)
        if label == 'sum':
            body += line(left, base, right, base, LIGHT, 1.2)
    body += t(340, 316, 'where the waves are in step they reinforce; where they are opposite they cancel', GREY, 11.5)
    return wrap('superposition', 'Adding two waves',
                'Two sinusoids of different amplitudes and a phase difference, with their sum below.',
                body, caption('Figure 2.', 'The sum is still a sinusoid of the same frequency, with an amplitude between '
                             'the difference and the sum of the two. Only the phase and the amplitudes decide which.'), 330)


def f_standing():
    body = t(340, 24, 'A standing wave: nodes stay still, antinodes swing', INK, 13, weight=700)
    left, right = 110, 610
    for k, (amp, colour, dash) in enumerate(((1.0, BLUE, ''), (0.55, GREEN, '6 4'))):
        pts = [(left + (right - left) * i / 200, 158 - 70 * amp * sin(3 * pi * i / 200) * cos(k * pi / 4)) for i in range(201)]
        extra = ' stroke-dasharray="' + dash + '"' if dash else ''
        body += f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{colour}" stroke-width="2.2"{extra}/>'
    body += line(left, 158, right, 158, LIGHT, 1.2)
    for m in range(4):
        x = left + (right - left) * m / 3
        body += dot(x, 158, 4, AMBER)
    body += t(110, 246, 'node', AMBER, 11.5, 'start', 700)
    body += t(340, 262, 'nodes are half a wavelength apart; this string holds three half wavelengths, so f = 3v/(2L)', GREY, 11.5)
    body += t(340, 286, 'an octave is a factor of two in frequency, not in wavelength', GREY, 11.5)
    return wrap('standing', 'Standing waves on a string',
                'The string at two instants, with its nodes marked, carrying three half wavelengths.',
                body, caption('Figure 3.', 'A standing wave is not a wave travelling nowhere: it is two travelling waves '
                             'of equal amplitude moving in opposite directions, and only the frequencies that fit the '
                             'boundary conditions survive.'), 316)


def f_doppler():
    import math
    body = t(340, 24, 'The Doppler effect: wavefronts bunch up in front, spread out behind', INK, 13, weight=700)
    src = (250, 152)
    for m in range(5):
        r = 18 + 23 * m
        cx = src[0] + 27 * m          # centres of the circles, not the source: the source has moved
        body += circle(cx, src[1], r, BLUE if m % 2 == 0 else '#7ea6f0', 'none', 1.8, '')
    body += dot(src[0], src[1], 7, AMBER) + t(src[0] - 8, src[1] - 12, 'source', AMBER, 11, 'end', 700)
    body += arrow('doppler', 120, 232, 270, 232, GREEN, 2.4) + t(195, 250, 'v_s', GREEN, 12, weight=700)
    body += t(560, 84, 'shorter λ,', INK, 11.5, 'start', 700) + t(560, 104, 'higher f', INK, 11.5, 'start', 700)
    body += t(120, 84, 'longer λ,', INK, 11.5, 'start', 700) + t(120, 104, 'lower f', INK, 11.5, 'start', 700)
    body += t(340, 284, 'f_obs = f_source · v/(v ∓ v_s),  the sign choosing approach or recession', GREY, 11.5)
    return wrap('doppler', 'Wavefronts from a moving source',
                'Concentric circles emitted at equal intervals by a source moving to the right.',
                body, caption('Figure 4.', 'The frequency does not change at the source: what changes is how many crests '
                             'per second reach the observer. The same rule gives the redshift of receding galaxies and the '
                             'change of pitch of an ambulance siren.'), 300)


def f_sound_intensity():
    return chart(
        'intensity', 'Sound level falls by 6 dB each time the distance doubles',
        'The intensity itself falls as 1/r², which is a straight line once it is expressed in decibels.',
        'log₁₀ (distance / 1 m)', 'level relative to 1 m  (dB)',
        [('6 dB per doubling', BLUE, lambda x: -20 * x)],
        xr=(0, 3), yr=(-66, 6), xticks=(0, 1, 2, 3), yticks=(-60, -40, -20, 0), height=340,
        xfmt='{:.0f}', yfmt='{:.0f}')


def f_resonance_tube():
    from math import sin as _sin, pi as _pi
    body = t(340, 24, 'Resonance in a pipe closed at one end', INK, 13, weight=700)
    for m in range(3):
        x0 = 118 + m * 160
        w = 90
        body += rect(x0, 74, w, 186, '#f8fafc', GREY, 2)
        body += line(x0 - 6, 74, x0 + w + 6, 74, GREY, 5)
        body += line(x0 + w / 2, 76, x0 + w / 2, 258, LIGHT, 1.2, '4 4')
        body += dot(x0 + w / 2, 76, 3.5, AMBER)
        colour = (BLUE, GREEN, PURPLE)[m]
        pts = []
        for i in range(101):
            sfrac = i / 100
            yy = 76 + 182 * sfrac
            xx = x0 + w / 2 + 34 * _sin((2 * m + 1) * _pi * sfrac / 2)
            pts.append((xx, yy))
        body += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" stroke="{colour}" stroke-width="2"/>'
        body += t(x0 + w / 2, 64, f'n = {m + 1}', colour, 11.5, weight=700)
        body += t(x0 + w / 2, 282, ('λ/4', '3λ/4', '5λ/4')[m], GREY, 11)
    body += t(340, 306, 'closed end: node;  open end: antinode  ⟹  L = (2n − 1)λ/4 and f = (2n − 1)v/(4L)', GREY, 11.5)
    return wrap('pipe', 'Standing waves in a closed pipe',
                'The first three standing-wave patterns in a pipe closed at one end and open at the other.',
                body, caption('Figure 6.', 'A closed end must be a node and an open end an antinode, so the pipe holds an '
                             'odd number of quarter wavelengths — the odd harmonics only. A pipe open at both ends holds '
                             'any number of half wavelengths, which is why it sounds brighter.'), 326)


FIGURES = {
    'wave': f_wave,
    'superposition': f_superposition,
    'standing': f_standing,
    'doppler': f_doppler,
    'intensity': f_sound_intensity,
    'pipe': f_resonance_tube,
}


def lab_doppler():
    controls = (
        slider('dop-f', 'Source frequency', 200, 1200, 10, 500, ' [Hz]')
        + slider('dop-vs', 'Source speed', 0, 120, 1, 30, ' [m/s]')
        + slider('dop-vo', 'Observer speed', 0, 120, 1, 0, ' [m/s]')
    )
    return shell(
        'doppler', 'Doppler shift for a moving source and observer',
        'The experiment uses the exact one-dimensional Doppler formulas for sound, with the observer either stationary, '
        'chasing the source or moving away, and also shows what would be heard if the wave were light, where the '
        'relativistic formula is needed.',
        controls,
        [('fa', 'Frequency approaching'), ('fr', 'Frequency receding'),
         ('df', 'Shift when approaching'), ('light', 'Fractional shift if it were light'), ('ratio', 'Ratio high/low')],
        'Set the observer speed to zero and the source to 30 m/s: how big is the shift at 500 Hz? Now make the source '
        'move at 120 m/s and compare with the light formula — why does the sound formula fail so badly there?'
    )


LABS = {'doppler': lab_doppler}
