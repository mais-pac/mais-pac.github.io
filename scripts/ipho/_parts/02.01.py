"""02.01 Kinematics: figures."""
from math import tan, cos, radians, sqrt

SPEED = 14


def _trajectory(angle):
    a = radians(angle)
    return lambda x: x * tan(a) - 9.81 * x ** 2 / (2 * SPEED ** 2 * cos(a) ** 2)


def f_vt():
    return chart(
        'vt-graphs', 'The v–t graph describes the whole motion',
        'Slope is acceleration; signed area under the curve is displacement.',
        'time t (s)', 'velocity v (m s⁻¹)',
        [('uniform velocity', BLUE, lambda x: 2.0),
         ('constant acceleration', GREEN, lambda x: 1 + 0.8 * x),
         ('steady deceleration', AMBER, lambda x: 3 - 0.7 * x),
         ('increasing acceleration', PURPLE, lambda x: 0.4 * x * x)],
        xr=(0, 3.2), yr=(0, 4), xticks=(1, 2, 3), yticks=(0, 1, 2, 3, 4), height=340,
        notes=[(1.34, 3.55, 'area = displacement', GREY)])


def f_projectile():
    return chart(
        'projectile', 'Same launch speed, three launch angles',
        'Complementary angles reach the same range; 45° maximizes it when air resistance is negligible.',
        'horizontal distance x (m)', 'height y (m)',
        [('45°: maximum range', BLUE, _trajectory(45)),
         ('60°: high and short', GREEN, _trajectory(60)),
         ('30°: low and fast', PURPLE, _trajectory(30))],
        xr=(0, 21), yr=(0, 9), xticks=(5, 10, 15, 20), yticks=(0, 3, 6, 9), height=340,
        notes=[(0.3, 8.3, 'v₀ = 14 m s⁻¹, g = 9.81 m s⁻²', GREY)])


def f_relative():
    body = t(340, 22, 'Velocity depends on the observer: choose the frame first', INK, 13, weight=700)
    body += t(180, 58, 'Crossing a river', BLUE, 12.5, weight=700)
    body += rect(56, 74, 252, 116, '#dbeafe', '#93c5fd', 4)
    body += line(56, 190, 308, 190, GREY, 2)
    body += arrow('relative', 86, 178, 186, 178, GREY, 2.4) + t(136, 200, 'current u', GREY, 11.5)
    body += arrow('relative', 86, 178, 86, 96, GREEN, 2.6) + t(64, 132, 'row v', GREEN, 11.5, 'end')
    body += arrow('relative', 86, 178, 186, 96, PURPLE, 2.6) + t(202, 92, 'ground track', PURPLE, 11.5, 'start')
    body += t(56, 224, 'sin θ = u / |v + u|', INK, 12, 'start', 700)
    body += t(520, 58, 'Vector addition', BLUE, 12.5, weight=700)
    body += arrow('relative', 396, 160, 486, 160, BLUE, 2.6) + t(441, 182, 'u', BLUE, 12)
    body += arrow('relative', 486, 160, 556, 92, GREEN, 2.6) + t(534, 134, 'v', GREEN, 12)
    body += arrow('relative', 396, 160, 556, 92, PURPLE, 2.6, dash='6 4') + t(568, 110, 'v + u', PURPLE, 11.5, 'start')
    body += t(396, 224, 'add as vectors, never as lengths', INK, 12, 'start', 700)
    body += t(340, 258, 'Only relative quantities are physical here: no frame is preferred in Newtonian mechanics.', GREY, 11.5)
    return wrap('relative', 'Galilean velocity addition',
                'A boat crossing a current, and the vector triangle that gives its ground track.',
                body, caption('Figure 3.', 'Switch to the frame in which the motion is simplest, solve, then transform back. '
                             'That single habit solves most “two moving objects” problems.'), 278)


def f_acceleration():
    return chart(
        'acceleration', 'Position, velocity and acceleration are three views of one motion',
        'For x(t) = 6 − ½(t − 2)² m the velocity is −(t − 2) m s⁻¹ and the acceleration is constant at −1 m s⁻².',
        'time t (s)', 'x (m), v (m s⁻¹)',
        [('position x', BLUE, lambda t: 6 - 0.5 * (t - 2) ** 2),
         ('velocity v', GREEN, lambda t: -(t - 2)),
         ('acceleration a', AMBER, lambda t: 0 * t - 1)],
        xr=(0, 5), yr=(-2, 6.5), xticks=(1, 2, 3, 4), yticks=(-2, 0, 2, 4, 6), height=330,
        notes=[(0.15, 5.7, 'turn-around at t = 2 s', GREY)])


def f_freefall():
    return chart(
        'free-fall', 'Free fall: height falls quadratically, speed rises linearly',
        'A ball dropped from 5 m; air resistance is neglected.',
        'time t (s)', 'metres, metres per second',
        [('height h = h₀ − ½gt²', BLUE, lambda t: max(0.0, 5 - 0.5 * 9.81 * t * t)),
         ('speed v = gt', GREEN, lambda t: min(9.95, 9.81 * t))],
        xr=(0, 1.05), yr=(0, 10.5), xticks=(0.25, 0.5, 0.75, 1.0), yticks=(0, 3, 6, 9),
        height=330, xfmt='{:.2f}',
        notes=[(0.03, 9.3, 'impact at t = √(2h/g) ≈ 1.01 s', GREY)])


def lab_projectile():
    controls = (
        slider('proj-v', 'Launch speed v₀', 5, 30, 1, 14, ' [m/s]')
        + slider('proj-a', 'Launch angle θ', 5, 85, 1, 45, ' [deg]')
        + slider('proj-g', 'Gravity g', 1.6, 24.8, 0.1, 9.8, ' [m/s²]')
    )
    return shell(
        'projectile', 'Range, apex and time of flight',
        'The projectile is drawn to scale for the chosen speed and gravity. Complementary angles give the same range; '
        'the apex moves to the left of the midpoint as the angle grows.',
        controls,
        [('range', 'Range'), ('apex', 'Maximum height'), ('time', 'Time of flight'), ('vx', 'Horizontal speed')],
        'Set the angle to 30°, note the range, then set 60°: the range repeats while the flight time doubles. '
        'Now change g to a lunar value and watch the range scale as 1/g.'
    )


FIGURES = {
    'vt-graphs': f_vt,
    'projectile': f_projectile,
    'relative': f_relative,
    'acceleration': f_acceleration,
    'free-fall': f_freefall,
}

LABS = {'projectile': lab_projectile}
