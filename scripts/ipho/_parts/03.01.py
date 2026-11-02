"""03.01 Measurement, apparatus and accuracy."""
from math import sin, cos, pi, sqrt, radians, exp, log10


def f_vernier():
    body = t(340, 24, 'A vernier scale: the line that matches reads the extra digit', INK, 13, weight=700)
    # main scale: 10 divisions of 30 px, mm marks
    for i in range(11):
        x = 120 + i * 40
        body += line(x, 96, x, 120, INK, 1.6)
        body += t(x, 136, f'{i}', GREY, 10.5)
    body += line(120, 108, 520, 108, INK, 1.2)
    body += t(320, 80, 'main scale (mm)', GREY, 11)
    # vernier: 10 divisions spanning 9 mm, offset by 0.3 mm
    offset = 0.3 * 40
    for j in range(11):
        x = 120 + offset + j * 36
        body += line(x, 160, x, 184, BLUE, 1.6)
        body += t(x, 200, f'{j}', BLUE, 10)
    body += t(320, 222, 'vernier scale: 10 divisions over 9 mm', GREY, 11)
    body += t(340, 262, 'the reading is 3.3 mm: 3 on the main scale plus the vernier division that lines up', GREY, 11.5)
    body += t(340, 288, 'least count = 1 mm / 10 = 0.1 mm — a tenth of the smallest main-scale division', INK, 11.5)
    return wrap('vernier', 'Vernier callipers',
                'A main scale and a sliding vernier scale drawn on top of each other, showing the matching division.',
                body, caption('Figure 1.', 'The vernier works by comparing two scales of slightly different pitch: exactly '
                             'one division coincides, and its index gives the fraction of a main-scale division.'), 306)


def f_micrometer():
    body = t(340, 24, 'A micrometer: a screw converts a small length into a large rotation', INK, 13, weight=700)
    body += rect(120, 120, 260, 34, '#e2e8f0', GREY, 4)
    body += rect(380, 112, 150, 50, '#dbeafe', BLUE, 4)
    body += t(455, 142, 'thimble', INK, 11.5)
    body += t(250, 88, 'barrel (mm)', GREY, 11)
    for i in range(9):
        x = 130 + i * 28
        body += line(x, 120, x, 108, INK, 1.2)
        body += t(x, 100, f'{i}', GREY, 9.5)
    for j in range(10):
        y = 114 + j * 5
        body += line(530, y, 546, y, BLUE, 1)
    body += t(560, 140, '0–9', BLUE, 11, 'start')
    body += t(340, 220, 'pitch = 0.50 mm per turn, with 50 divisions on the thimble', GREY, 11.5)
    body += t(340, 244, 'reading = barrel + (division × 0.01 mm)  →  a least count of 0.01 mm', INK, 12)
    body += t(340, 286, 'the screw thread is the analogue amplifier: one turn is a length you can see', GREY, 11.5)
    return wrap('micrometer', 'The micrometer screw gauge',
                'A barrel with millimetre marks, a rotating thimble and the reading rule written below.',
                body, caption('Figure 2.', 'Both instruments beat the ruler by using a second scale rather than a finer one: '
                             'the precision comes from comparison, not from sharper eyesight.'), 306)


def f_random_systematic():
    body = t(340, 24, 'Random and systematic errors are different animals', INK, 13, weight=700)
    # random scatter about the true value
    import math
    xs = [0.20, 0.32, 0.44, 0.56, 0.70, 0.30, 0.50, 0.62]
    ys = [0.45, 0.60, 0.36, 0.68, 0.52, 0.72, 0.40, 0.58]
    body += rect(90, 80, 220, 170, '#f8fafc', '#e2e8f0', 6)
    body += t(200, 72, 'random error', GREY, 11.5, weight=700)
    body += line(90, 165, 310, 165, RED, 2)
    body += t(300, 154, 'true', RED, 10.5, 'end')
    for x, y in zip(xs, ys):
        body += dot(90 + x * 220, 80 + (1 - y) * 170, 4, BLUE)
    # systematic offset
    body += rect(370, 80, 220, 170, '#f8fafc', '#e2e8f0', 6)
    body += t(480, 72, 'systematic error', GREY, 11.5, weight=700)
    body += line(370, 165, 590, 165, RED, 2)
    body += t(580, 154, 'true', RED, 10.5, 'end')
    for x, y in zip(xs, ys):
        body += dot(370 + x * 220, 80 + (1 - (y * 0.25 + 0.28)) * 170, 4, PURPLE)
    body += t(340, 276, 'random errors scatter about the true value and average out; systematic errors all push the same way', GREY, 11.5)
    body += t(340, 300, 'repeating the measurement shrinks the random part but never removes the systematic part', INK, 11.5)
    return wrap('errors', 'Random versus systematic error',
                'Two panels of repeated measurements: one scattered about the true value, one offset from it.',
                body, caption('Figure 3.', 'Random error affects precision (repeatability); systematic error affects '
                             'accuracy (closeness to the truth). A calibration check, not more repeats, is what catches '
                             'the systematic kind.'), 316)


def f_resolution():
    from math import sqrt as _sqrt
    def slope(x):
        return 1 / (2 * _sqrt(x)) if x > 0 else 0
    return chart(
        'resolution', 'Averaging N readings shrinks the random uncertainty as 1/√N',
        'Four times as many readings halve the uncertainty — a slow return for a lot of work.',
        'number of readings N', 'uncertainty of the mean (relative to one reading)',
        [('σ/√N', BLUE, lambda n: 1 / sqrt(max(n, 1)))],
        xr=(1, 100), yr=(0, 1.05), xticks=(10, 25, 50, 75, 100), yticks=(0.25, 0.5, 0.75, 1), height=350,
        xfmt='{:.0f}', yfmt='{:.2f}',
        notes=[(40, 0.62, 'N = 4 gives ½;  N = 100 gives 1/10', GREY)])


def f_choice():
    body = t(340, 24, 'Choose the instrument to match the question', INK, 13, weight=700)
    rows = [('metre rule', '±1 mm', 'lengths above ~10 cm'),
            ('vernier callipers', '±0.05 mm', 'diameters, depths, small gaps'),
            ('micrometer', '±0.005 mm', 'thin foils, wire diameters'),
            ('stopwatch (manual)', '±0.2 s', 'intervals above a few seconds'),
            ('digital balance', '±0.01 g', 'masses above a gram'),
            ('thermometer', '±0.5 K', 'temperatures, with a stirrer')]
    body += t(140, 76, 'instrument', GREY, 11, 'start', 700)
    body += t(340, 76, 'typical uncertainty', GREY, 11, 'start', 700)
    body += t(480, 76, 'best used for', GREY, 11, 'start', 700)
    for i, (a, b, c) in enumerate(rows):
        y = 100 + i * 28
        body += rect(120, y - 16, 460, 26, '#f8fafc' if i % 2 == 0 else '#ffffff', '#e2e8f0', 3)
        body += t(130, y + 3, a, INK, 11, 'start', 700)
        body += t(330, y + 3, b, BLUE, 11, 'start')
        body += t(470, y + 3, c, GREY, 10.5, 'start')
    body += t(340, 292, 'the quoted uncertainty should be about one unit of the last digit you record', GREY, 11.5)
    return wrap('instruments', 'A comparison of common instruments',
                'A table of instruments, their typical uncertainties and the measurements they suit.',
                body, caption('Figure 5.', 'There is no "best" instrument, only an appropriate one: a micrometer used on a '
                             'metre-long plank gives four meaningless digits, and a ruler used on a hair gives none.'), 306)


FIGURES = {
    'vernier': f_vernier,
    'micrometer': f_micrometer,
    'errors': f_random_systematic,
    'resolution': f_resolution,
    'instruments': f_choice,
}


def lab_reading():
    controls = (
        slider('read-main', 'Main scale reading', 0, 10, 0.5, 3.0, ' [mm]')
        + slider('read-vern', 'Vernier coincidence', 0, 9, 1, 3, '')
        + slider('read-zero', 'Zero error', -0.5, 0.5, 0.1, 0.0, ' [mm]')
    )
    return shell(
        'vernier-reading', 'Reading a vernier calliper',
        'Set the main scale and the vernier division that lines up, and the experiment reports the raw reading, the '
        'correction for zero error and the final value with its uncertainty. It draws the two scales so you can check '
        'the alignment yourself.',
        controls,
        [('raw', 'Raw reading'), ('corrected', 'Corrected reading'), ('digits', 'Significant digits'),
         ('unc', 'Uncertainty'), ('verdict', 'Is the reading sensible?')],
        'Introduce a zero error of +0.3 mm and take a reading of 4.0 mm. What is the true length, and why does the '
        'error matter more for small objects than large ones?'
    )


LABS = {'vernier-reading': lab_reading}
