"""02.11 Optics: lenses, gratings and interferometers."""
from math import sin, cos, pi, sqrt, radians, exp, log10, atan


def f_refraction():
    body = t(340, 24, 'Refraction bends a ray towards the normal in a denser medium', INK, 13, weight=700)
    # boundary
    body += rect(100, 168, 480, 96, '#e0f2fe', '#bae6fd', 2)
    body += line(100, 168, 580, 168, GREY, 2)
    body += line(340, 60, 340, 280, LIGHT, 1.4, '5 4')
    body += t(340, 52, 'normal', GREY, 11)
    # incident ray from upper left
    body += arrow('refr', 210, 76, 340, 168, AMBER, 2.6)
    body += t(240, 96, 'incident', AMBER, 11, 'end')
    # refracted ray, steeper (towards normal)
    body += arrow('refr', 340, 168, 424, 262, AMBER, 2.6)
    body += t(432, 250, 'refracted', AMBER, 11, 'start')
    # reflected ray
    body += arrow('refr', 340, 168, 470, 76, GREY, 1.8, '6 4')
    body += t(470, 64, 'weak reflection', GREY, 11, 'start')
    body += t(112, 116, 'n₁ (air)', GREY, 11, 'start')
    body += t(112, 222, 'n₂ (glass)', INK, 12, 'start', 700)
    body += t(340, 292, 'n₁ sin θ₁ = n₂ sin θ₂:  the ray bends, the frequency does not change', GREY, 11.5)
    return wrap('refraction', 'Refraction at a plane surface',
                'An incident ray, the normal, the weaker reflected ray and the refracted ray bending towards the normal.',
                body, caption('Figure 1.', 'The wavelength shortens inside the denser medium while the frequency stays the '
                             'same, because it is the frequency that is set by the source. The ray bends because the wave '
                             'slows down — the marching-band analogy.'), 306)


def f_lens():
    body = t(340, 24, 'A converging lens: parallel rays meet at the focal point', INK, 13, weight=700)
    # lens as an ellipse-ish shape
    body += f'<path d="M340,60 Q406,150 340,240 Q274,150 340,60 Z" fill="#e0f2fe" stroke="{BLUE}" stroke-width="2"/>'
    body += line(60, 150, 620, 150, GREY, 1.4, '6 4')
    for y in (86, 118, 182, 214):
        body += arrow('lens', 100, y, 334, y, AMBER, 1.8)
        # continue from lens to focus
        body += arrow('lens', 346, y, 560, 150, AMBER, 1.8)
    body += dot(560, 150, 5, RED) + t(560, 174, 'F', RED, 12, weight=700)
    body += dot(120, 150, 5, RED) + t(120, 174, 'F', RED, 12, weight=700)
    body += t(340, 268, 'thin lens:  1/f = 1/u + 1/v,   m = −v/u', GREY, 11.5)
    body += t(340, 292, 'a converging lens has f > 0; a diverging lens has f < 0 and spreads parallel rays', GREY, 11.5)
    return wrap('lens', 'Rays through a converging lens',
                'Parallel rays entering a converging lens and meeting at the far focal point.',
                body, caption('Figure 2.', 'The whole of geometrical optics is the statement that all rays from a point '
                             'object arrive at one image point. The thin-lens equation is the algebraic version of that '
                             'picture, with the sign conventions doing the bookkeeping.'), 306)


def f_magnification():
    return chart(
        'magnify', 'Magnification and image distance for a converging lens',
        'As the object approaches the focal point the image runs off to infinity; inside f the image becomes virtual.',
        'object distance / f', 'image distance / f  and magnification',
        [('v/f', BLUE, lambda u: u / (u - 1) if abs(u - 1) > 1e-6 else 0),
         ('|m|', GREEN, lambda u: abs(1 / (u - 1)) if abs(u - 1) > 1e-6 else 0)],
        xr=(0.25, 3.2), yr=(-4.5, 8), xticks=(0.5, 1, 1.5, 2, 2.5, 3), yticks=(-4, -2, 0, 2, 4, 6, 8),
        height=350, xfmt='{:.1f}', yfmt='{:.0f}',
        notes=[(1.05, 6.6, 'u < f: image is virtual and on the same side', GREY)])


def f_snell_total():
    from math import asin, degrees, sin as _sin, cos as _cos
    body = t(340, 24, 'Total internal reflection above the critical angle', INK, 13, weight=700)
    body += rect(100, 168, 480, 100, '#e0f2fe', '#bae6fd', 2)
    body += line(100, 168, 580, 168, GREY, 2)
    body += line(340, 60, 340, 282, LIGHT, 1.4, '5 4')
    crit = asin(1 / 1.5)
    # three rays from inside: below critical (refracts out), at critical, above (total reflection)
    for ang, col, note in ((28, AMBER, 'refracts'), (45, GREEN, 'critical'), (60, PURPLE, 'reflects')):
        a = radians(ang)
        sx, sy = 340 - 90 * _sin(a), 168 + 90 * _cos(a)
        body += arrow('tir', sx, sy, 340, 168, col, 2.4)
        if ang < 45:
            body += arrow('tir', 340, 168, 340 + 120 * _sin(asin(1.5 * _sin(a)) or 0), 168 - 120 * _cos(asin(min(1, 1.5 * _sin(a)))), col, 2.4)
        elif ang == 45:
            body += line(340, 168, 470, 168, col, 2.4)
        else:
            body += arrow('tir', 340, 168, 340 + 90 * _sin(a), 168 + 90 * _cos(a), col, 2.4)
    body += t(430, 96, 'refracts out', AMBER, 11, 'start')
    body += t(452, 160, 'grazes the surface', GREEN, 11, 'start')
    body += t(430, 240, 'totally reflected', PURPLE, 11, 'start')
    body += t(340, 300, 'sin θ_c = n₂/n₁ = 1/1.5, so θ_c = 42°  —  the reason optical fibres work', GREY, 11.5)
    return wrap('tir', 'Total internal reflection',
                'Three rays inside glass meeting the boundary at increasing angles: one refracts, one grazes, one reflects entirely.',
                body, caption('Figure 4.', 'Beyond the critical angle there is no refracted ray at all: the light cannot '
                             'leave, and the surface becomes a perfect mirror. This is total internal reflection, and it is '
                             'why a diamond sparkles.'), 316)


def f_grating():
    from math import sin as _sin, cos as _cos
    body = t(340, 24, 'A diffraction grating: maxima where the path difference is a whole number of wavelengths', INK, 13, weight=700)
    body += line(90, 244, 590, 244, GREY, 4)
    for x in range(110, 590, 16):
        body += line(x, 244, x, 256, GREY, 1.6)
    body += t(340, 272, 'grating: many slits, spacing d', GREY, 11)
    for m, col in ((0, INK), (1, BLUE), (-1, BLUE), (2, PURPLE), (-2, PURPLE)):
        ang = radians(19 * m)
        ex, ey = 340 + 168 * _sin(ang), 244 - 168 * _cos(ang)
        body += line(340, 244, ex, ey, col, 2.4)
        label = 'm = 0' if m == 0 else f'm = {m}'
        dy = -10 if m == 0 else (-6 if m > 0 else 14)
        dx = 0 if m == 0 else (8 if m > 0 else -8)
        body += t(ex + dx, ey + dy, label, col, 11.5, 'middle' if m == 0 else ('start' if m > 0 else 'end'), 700)
    body += t(340, 300, 'd sin θ = mλ;  longer wavelengths are diffracted further, so each order is a spectrum', GREY, 11.5)
    return wrap('grating', 'Diffraction by a grating',
                'A grating with many slits, and the central and first two orders of diffracted beams.',
                body, caption('Figure 5.', 'With N slits the maxima become N times narrower and N² times brighter, which is '
                             'why gratings, not prisms, are used to measure wavelengths precisely.'), 316)


def f_interference():
    body = t(340, 24, 'Young’s double slit: bright fringes where the paths differ by mλ', INK, 13, weight=700)
    # barrier with two slits
    body += line(120, 96, 288, 96, GREY, 4) + line(296, 96, 384, 96, GREY, 4) + line(392, 96, 520, 96, GREY, 4)
    body += t(340, 84, 'two slits, spacing d', GREY, 11)
    s1, s2 = (292, 96), (388, 96)
    body += dot(*s1, 3.5, AMBER) + dot(*s2, 3.5, AMBER)
    # screen
    body += line(560, 56, 560, 300, GREY, 3)
    body += t(568, 68, 'screen', GREY, 11, 'start')
    # rays to the central bright fringe and to the next one above it
    for target in (173, 217):
        body += line(s1[0], s1[1], 558, target, BLUE, 1.4)
        body += line(s2[0], s2[1], 558, target, GREEN, 1.4)
    # fringe pattern on the screen: bright dots at even offsets, pale at the dark fringes
    for k in range(-2, 3):
        yy = 173 + k * 44
        body += dot(560, yy, 5, AMBER)
    body += t(340, 300, 'Δ = d sin θ = mλ for a bright fringe;  spacing on the screen  y = mλL/d', GREY, 11.5)
    return wrap('double-slit', 'Young’s double-slit experiment',
                'Two slits, rays reaching a screen, and the resulting pattern of equally spaced fringes.',
                body, caption('Figure 6.', 'The fringes are equally spaced for small angles, and their spacing gives a way of '
                             'measuring a wavelength with a ruler — the experiment that settled the wave nature of light.'), 320)


FIGURES = {
    'refraction': f_refraction,
    'lens': f_lens,
    'magnify': f_magnification,
    'tir': f_snell_total,
    'grating': f_grating,
    'double-slit': f_interference,
}


def lab_lens():
    controls = (
        slider('lens-f', 'Focal length', 5, 50, 1, 15, ' [cm]')
        + slider('lens-u', 'Object distance', 2, 120, 1, 40, ' [cm]')
        + slider('lens-h', 'Object height', 1, 10, 1, 3, ' [cm]')
    )
    return shell(
        'thin-lens', 'A thin converging lens',
        'Move the object and watch the image form. The experiment reports the image distance, the magnification and '
        'whether the image is real or virtual, and draws the three principal rays to scale.',
        controls,
        [('v', 'Image distance'), ('m', 'Magnification'), ('type', 'Nature of the image'),
         ('hi', 'Image height'), ('power', 'Power of the lens')],
        'Put the object just inside the focal length. What happens to the image distance, and where would you look to see '
        'the image? That is the arrangement of a magnifying glass.'
    )


LABS = {'thin-lens': lab_lens}
