"""Original inline SVG figures for the extended curriculum (07–10)."""
from math import sin, cos, pi, exp, log10

def wrap(key, title, desc, body, caption, h=300):
    key = key.replace('_', '-')
    return f'<figure class="cosmo-figure" id="fig-{key}"><svg viewBox="0 0 680 {h}" role="img" aria-labelledby="fig-{key}-title fig-{key}-desc" xmlns="http://www.w3.org/2000/svg"><title id="fig-{key}-title">{title}</title><desc id="fig-{key}-desc">{desc}</desc><defs><marker id="arrow-{key}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#2457c5"/></marker></defs>{body}</svg><figcaption>{caption}</figcaption></figure>'

def text(x, y, s, color='#1e3a8a', size=13, anchor='middle', weight=400):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'

def dot(x, y, r=5, fill='#2457c5'):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'

def line(x1, y1, x2, y2, stroke='#94a3b8', extra=''):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{stroke}" stroke-width="2" {extra}/>'

def arrow(x1, y1, x2, y2, key, color='#2457c5'):
    key = key.replace('_', '-')
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2.4" marker-end="url(#arrow-{key})"/>'

def box(x, y, w, h, label, fill='#eff6ff', stroke='#2457c5'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" stroke="{stroke}"/>' + text(x + w / 2, y + h / 2 + 5, label, stroke, 12)

def em_spectrum():
    bands = [('Radio', '#dbeafe'), ('Microwave', '#e0e7ff'), ('IR', '#fee2e2'), ('Visible', '#d1fae5'), ('UV', '#ede9fe'), ('X-ray', '#fce7f3'), ('Gamma', '#f1f5f9')]
    b = '<rect x="35" y="70" width="610" height="60" rx="6" fill="#f8fafc"/>'
    for i, (lab, col) in enumerate(bands):
        x = 35 + i * 87.1
        b += f'<rect x="{x}" y="70" width="85" height="60" fill="{col}"/>' + text(x + 42, 105, lab, size=11)
    b += arrow(45, 160, 635, 160, 'em-spectrum') + text(340, 185, 'Increasing frequency and photon energy →', weight=700) + text(340, 45, 'One electromagnetic spectrum, many physical processes', weight=700) + text(340, 215, 'Band order only; widths are not to scale.', size=12) + text(340, 240, 'Thermal peaks, spectral lines, synchrotron and accretion emission occupy different bands.', size=12)
    return wrap('em-spectrum', 'The electromagnetic spectrum as a multi-wavelength toolkit', 'Different bands trace different temperatures and physical processes.', b, '<strong>Figure 1.</strong> Band boundaries are conventional. A complete picture of an object usually requires several wavelength regimes.', 270)

def atmo_windows():
    b = '<path d="M55 245H635M55 245V35" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    windows = [(70, 180, 'Optical'), (235, 120, 'Near-IR'), (430, 70, 'Radio')]
    for x, w, lab in windows:
        b += f'<rect x="{x}" y="55" width="{w}" height="190" fill="#d1fae5" opacity=".55"/>' + text(x + w / 2, 45, lab, size=12)
    b += text(340, 275, 'Wavelength → (schematic, not to scale)') + text(8, 140, 'Transmission', size=12, anchor='start') + text(340, 295, 'Water vapour, ozone and oxygen shape real windows.', size=11)
    return wrap('atmo-windows', 'Why some astronomy must leave the ground', 'The atmosphere is transparent in some bands and opaque in others.', b, '<strong>Figure 2.</strong> Optical and radio windows are broad; much UV, X-ray and gamma-ray astronomy requires space telescopes.', 315)

def telescope_optics():
    b = box(60, 90, 120, 110, 'Objective / mirror') + box(260, 110, 110, 70, 'Focal plane', '#f0fdf7', '#059669') + box(450, 110, 120, 70, 'Eyepiece / detector', '#faf5ff', '#7c3aed')
    b += arrow(180, 145, 260, 145, 'telescope-optics') + arrow(370, 145, 450, 145, 'telescope-optics') + text(340, 55, 'Aperture collects light; focal length sets image scale', weight=700) + text(340, 245, 'f/ratio = focal length / aperture · magnification = f objective / f eyepiece', size=12)
    return wrap('telescope-optics', 'The basic telescope chain', 'Light is collected, focused and then recorded or magnified.', b, '<strong>Figure 3.</strong> Aperture controls light grasp and diffraction; focal length and detector or eyepiece control scale and field.', 270)

def resolution():
    b = '<path d="M55 245H635M55 245V35" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    for sig, col, lab in [(22, '#7c3aed', 'Diffraction limit'), (55, '#2457c5', 'Seeing-limited')]:
        pts = [f'{x},{245 - 180 * exp(-.5 * ((x - 340) / sig) ** 2):.1f}' for x in range(60, 626, 3)]
        b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.5"/>' + text(480, 80 if col == '#7c3aed' else 120, lab, col, 12, 'start', 700)
    b += text(340, 275, 'Angular offset →') + text(340, 295, 'The wider profile is the practical ground-based limit.', size=11)
    return wrap('resolution', 'Diffraction versus seeing', 'A telescope may be capable of finer detail than the atmosphere delivers.', b, '<strong>Figure 4.</strong> Adaptive optics, space telescopes or interferometry can recover finer angular resolution.', 315)

def iteration():
    b = '<path d="M70 250H620M70 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    X = lambda n: 90 + n * 85
    Y = lambda e: 245 - (max(0.0, min(6.0, -log10(max(e, 1e-7)))) / 6) * 195
    series = [('Bisection', lambda n: 0.5 ** n, '#2457c5'), ('Fixed-point', lambda n: 0.8 ** n, '#059669'), ('Newton (local)', lambda n: 0.5 ** (2 ** n), '#7c3aed')]
    for lab, f, col in series:
        pts = [f'{X(n):.1f},{Y(f(n)):.1f}' for n in range(7)]
        b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.5"/>'
        for n in range(7):
            b += dot(X(n), Y(f(n)), 3.5, col)
    b += text(340, 285, 'Iteration number →') + text(8, 140, 'log error', size=12, anchor='start') + text(340, 25, 'Convergence is a sequence of improving guesses', weight=700)
    b += text(110, 55, 'Bisection', '#2457c5', 11, 'start') + text(230, 55, 'Fixed-point', '#059669', 11, 'start') + text(370, 55, 'Newton (near root)', '#7c3aed', 11, 'start')
    return wrap('iteration', 'Iterative methods approach a solution', 'Successive approximations can converge rapidly, slowly or not at all.', b, '<strong>Figure 5.</strong> Schematic convergence histories. Newton’s method is fast near a root; bisection is slower but robust when a sign change is bracketed.', 310)

def linearization():
    f = lambda x: 230 - 0.0006 * (x - 90) ** 2
    x0 = 300; y0 = f(x0); m = -0.0012 * (x0 - 90)
    pts = [f'{x},{f(x):.1f}' for x in range(90, 601, 4)]
    b = '<path d="M70 250H620M70 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>' + f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2457c5" stroke-width="2.5"/>'
    b += line(160, y0 + m * (160 - x0), 480, y0 + m * (480 - x0), '#7c3aed', 'stroke-width="2.5"') + dot(x0, y0, 6, '#059669')
    b += text(340, 285, 'x →') + text(340, 25, 'A curve is locally almost a straight line', weight=700) + text(470, 150, 'tangent', '#7c3aed', 12, 'start')
    return wrap('linearization', 'Linearization and Taylor approximation', 'Near a point, a smooth function is well approximated by its tangent.', b, '<strong>Figure 6.</strong> Small-angle and binomial approximations are the workhorses of Olympiad estimation.', 310)

def derivative_integral():
    f = lambda x: 220 - 90 * (1 - ((x - 340) / 250) ** 2)
    pts = [f'{x},{f(x):.1f}' for x in range(90, 591, 4)]
    area = [f'{x},{f(x):.1f}' for x in range(200, 481, 4)]
    b = '<path d="M70 250H620M340 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    b += f'<polygon points="200,250 {" ".join(area)} 480,250" fill="#2457c5" opacity=".12"/>'
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2457c5" stroke-width="2.5"/>' + line(220, 130, 460, 130, '#7c3aed', 'stroke-width="2.5"') + dot(340, 130, 5, '#059669')
    b += text(340, 285, 'x →') + text(340, 25, 'Slope and accumulated area', weight=700)
    return wrap('derivative-integral', 'Derivatives and integrals answer different questions', 'The derivative is local; the integral accumulates a quantity over an interval.', b, '<strong>Figure 7.</strong> In astronomy, derivatives give rates and integrals give totals such as flux, mass or lookback time.', 310)

def ode_decay():
    b = '<path d="M70 250H620M70 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    pts = [f'{70 + 540 * t / 6:.1f},{245 - 190 * exp(-t):.1f}' for t in [i / 40 for i in range(241)]]
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2457c5" stroke-width="3"/>' + text(340, 285, 'Time →') + text(340, 25, 'Exponential decay: rate proportional to amount', weight=700)
    return wrap('ode-decay', 'A simple differential equation with an exponential solution', 'Many physical relaxation and decay processes share the same mathematical form.', b, '<strong>Figure 8.</strong> The half-life or e-folding time sets the scale; initial conditions set the normalization.', 310)

def vector_add():
    b = arrow(120, 240, 300, 120, 'vector-add') + arrow(300, 120, 470, 190, 'vector-add', '#059669') + arrow(120, 240, 470, 190, 'vector-add', '#7c3aed')
    b += line(120, 240, 290, 310, '#059669', 'stroke-dasharray="6 4" opacity=".45"') + line(290, 310, 470, 190, '#2457c5', 'stroke-dasharray="6 4" opacity=".45"')
    b += text(200, 160, 'A', '#2457c5', 14) + text(390, 140, 'B', '#059669', 14) + text(300, 225, 'A+B', '#7c3aed', 14) + text(340, 45, 'Head-to-tail addition (parallelogram equivalent)', weight=700)
    return wrap('vector-add', 'Vectors add geometrically', 'Displacements, velocities and forces combine by vector addition.', b, '<strong>Figure 9.</strong> Components make the same rule algebraic: add x with x and y with y.', 330)

def dot_cross():
    b = arrow(140, 220, 420, 220, 'dot-cross') + arrow(140, 220, 330, 90, 'dot-cross', '#059669') + '<path d="M250 220A110 110 0 0 0 231 158" fill="none" stroke="#7c3aed" stroke-width="2"/>'
    b += text(430, 225, 'A', '#2457c5', 14, 'start') + text(335, 85, 'B', '#059669', 14) + text(260, 185, 'θ', '#7c3aed', 14) + text(340, 45, 'Projection and oriented area', weight=700) + text(340, 275, 'A·B = |A||B|cos θ · |A×B| = |A||B|sin θ', size=13)
    return wrap('dot-cross', 'Dot product and cross product', 'The dot product measures alignment; the cross product measures perpendicularity and orientation.', b, '<strong>Figure 10.</strong> Flux uses a dot product; angular momentum and torque use cross products.', 300)

def scale_drawing():
    b = '<path d="M90 230H590" stroke="#64748b" stroke-width="2"/>'
    for i in range(11):
        b += f'<path d="M{90 + i * 50} 225V235" stroke="#64748b"/>'
    b += text(340, 265, 'A scale converts paper distance to physical distance', weight=700) + text(340, 60, 'Scale: 1 cm on paper = 10 m on the ground', size=14) + box(190, 110, 300, 70, 'Measured length × scale = true length')
    return wrap('scale-drawing', 'Scale drawings preserve ratios', 'Rulers and maps are useful only when the scale is known.', b, '<strong>Figure 11.</strong> Always state the scale and propagate the ruler’s reading uncertainty.', 290)

def triangulation():
    b = '<path d="M120 240L560 240L340 70Z" fill="#eff6ff" stroke="#2457c5" stroke-width="2.5"/>' + dot(120, 240, 5) + dot(560, 240, 5) + dot(340, 70, 6, '#7c3aed')
    b += '<path d="M170 240A50 50 0 0 0 159 209" fill="none" stroke="#7c3aed" stroke-width="2"/><path d="M510 240A50 50 0 0 1 521 209" fill="none" stroke="#7c3aed" stroke-width="2"/>'
    b += text(340, 265, 'Baseline b') + text(178, 222, 'α', '#7c3aed', 14) + text(502, 222, 'β', '#7c3aed', 14) + text(340, 45, 'Triangulation turns angles and a baseline into distance', weight=700)
    return wrap('triangulation', 'Distance from a baseline and two angles', 'The sine rule solves the triangle once one side and two angles are known.', b, '<strong>Figure 12.</strong> The same geometry underlies surveying, parallax and some astronomical distance methods.', 300)

def distributions():
    b = '<path d="M70 250H620M70 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    for mu, sig, col in [(280, 55, '#2457c5'), (400, 85, '#7c3aed')]:
        pts = [f'{x},{245 - 180 * (55 / sig) * exp(-.5 * ((x - mu) / sig) ** 2):.1f}' for x in range(80, 621, 3)]
        b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.5"/>'
    b += text(340, 285, 'Measured value →') + text(8, 140, 'Density', size=12, anchor='start') + text(340, 25, 'Mean sets location; scatter sets width', weight=700)
    return wrap('distributions', 'Distributions summarize repeated measurements', 'Two samples can have different means, spreads or shapes.', b, '<strong>Figure 13.</strong> Normalized density curves: a narrower distribution is taller. Mean, median and standard deviation answer different questions.', 310)

def error_propagation():
    b = box(70, 80, 150, 70, 'x ± σx') + box(270, 80, 150, 70, 'y ± σy') + box(470, 80, 150, 70, 'f(x,y) ± σf', '#f0fdf7', '#059669')
    b += arrow(220, 115, 270, 115, 'error-propagation') + arrow(420, 115, 470, 115, 'error-propagation') + text(340, 200, 'Independent standard uncertainties add in quadrature', weight=700) + text(340, 235, 'σf² ≈ (∂f/∂x)²σx² + (∂f/∂y)²σy²', size=13)
    return wrap('error-propagation', 'Uncertainties propagate through calculations', 'A result is incomplete without an uncertainty budget.', b, '<strong>Figure 14.</strong> Known systematic offsets are corrected; correlated terms need separate treatment.', 270)

def hand_angles():
    b = box(70, 80, 120, 90, '1 finger ≈ 1°') + box(210, 80, 120, 90, '3 fingers ≈ 5°') + box(350, 80, 120, 90, 'Fist ≈ 10°') + box(490, 80, 120, 90, 'Spread ≈ 20°')
    b += text(340, 225, 'Hold your hand at arm’s length; these are rough calibrations.', size=13) + text(340, 45, 'Your hand is a portable angular ruler', weight=700)
    return wrap('hand-angles', 'Naked-eye angular scales', 'Hand spans provide quick estimates of angular separation.', b, '<strong>Figure 15.</strong> Calibrate your own hand against known separations such as the Big Dipper.', 260)

def limiting_magnitude():
    b = '<path d="M70 250H620M70 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    denom = 10 ** 4.2 - 1
    pts = [f'{70 + 540 * m / 7:.1f},{245 - 200 * (10 ** (0.6 * m) - 1) / denom:.1f}' for m in [i / 10 for i in range(71)]]
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2457c5" stroke-width="3"/>' + text(340, 285, 'Limiting magnitude →') + text(8, 140, 'Star count', size=12, anchor='start') + text(340, 25, 'Fainter limits reveal many more stars', weight=700) + text(340, 65, 'Euclidean model N ∝ 10^(0.6m), normalized (schematic)', size=11)
    return wrap('limiting-magnitude', 'Why dark skies matter', 'The number of visible stars rises steeply with limiting magnitude.', b, '<strong>Figure 16.</strong> Light pollution lowers the limiting magnitude and removes the faint majority. Real counts depend on sky position and extinction.', 310)

def celestial_grid():
    b = '<ellipse cx="340" cy="155" rx="250" ry="110" fill="#eff6ff" stroke="#2457c5" stroke-width="2"/><ellipse cx="340" cy="155" rx="250" ry="35" fill="none" stroke="#93c5fd"/><path d="M340 45V265" stroke="#93c5fd"/><path d="M215 60Q340 155 215 250M465 60Q340 155 465 250" fill="none" stroke="#93c5fd"/>'
    b += text(340, 30, 'RA and Dec form a sky grid', weight=700) + text(600, 155, 'RA', '#2457c5', 12, 'start') + text(340, 285, 'Dec', size=12)
    return wrap('celestial-grid', 'The equatorial coordinate grid', 'Right ascension and declination label positions on the celestial sphere.', b, '<strong>Figure 17.</strong> Charts project this grid; the projection distorts shapes and areas.', 310)

def catalogue_fields():
    rows = [('Name', 'Human label'), ('RA / Dec', 'Position'), ('Magnitude', 'Brightness'), ('Epoch', 'Coordinate date'), ('Identifier', 'Catalogue key')]
    b = ''
    for i, (a, c) in enumerate(rows):
        b += box(90, 50 + i * 42, 220, 34, a) + box(330, 50 + i * 42, 260, 34, c, '#f8fafc', '#64748b')
    b += text(340, 285, 'A catalogue is a database; a chart is a visualization.', weight=700)
    return wrap('catalogue-fields', 'What a star catalogue records', 'Catalogues store standardized measurements and identifiers.', b, '<strong>Figure 18.</strong> Always check epoch, equinox, band and uncertainty when comparing catalogue entries.', 310)

def horizon_coords():
    b = '<path d="M100 250A240 240 0 0 1 580 250" fill="#eff6ff" stroke="#94a3b8" stroke-width="2"/><path d="M80 250H600" stroke="#64748b" stroke-width="2"/>' + arrow(340, 250, 470, 105, 'horizon-coords', '#7c3aed')
    b += '<path d="M420 250A80 80 0 0 0 394 191" fill="none" stroke="#059669" stroke-width="2"/>' + text(430, 215, 'h', '#059669', 14) + text(340, 275, 'Horizon plane') + text(480, 95, 'Line of sight', '#7c3aed', 12, 'start') + text(340, 40, 'Altitude h is above the horizon; azimuth is along it', weight=700)
    return wrap('horizon-coords', 'Altitude and azimuth are local coordinates', 'The same star has different alt/az for different observers and times.', b, '<strong>Figure 19.</strong> Hour angle links the catalogue grid to the local meridian.', 310)

def airmass():
    b = '<path d="M70 250H620M70 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    def ky(h):
        return 1 / (sin(h * pi / 180) + 0.50576 * (h + 6.07995) ** -1.6364)
    pts = [f'{70 + (90 - h) / 90 * 540:.1f},{245 - min(ky(h), 40) / 40 * 200:.1f}' for h in range(0, 91)]
    sec = [f'{70 + (90 - h) / 90 * 540:.1f},{245 - min(1 / sin(h * pi / 180), 40) / 40 * 200:.1f}' for h in range(2, 91)]
    b += f'<polyline points="{" ".join(sec)}" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="6 4"/><polyline points="{" ".join(pts)}" fill="none" stroke="#2457c5" stroke-width="3"/>'
    b += text(340, 285, 'Altitude decreasing →') + text(8, 140, 'Airmass', size=12, anchor='start') + text(340, 25, 'Low altitude means a long atmospheric path', weight=700) + text(430, 65, 'Kasten–Young', '#2457c5', 11, 'start') + text(430, 82, 'sec z (diverges)', '#64748b', 11, 'start')
    return wrap('airmass', 'Airmass grows near the horizon', 'Extinction and seeing worsen as the line of sight passes through more atmosphere.', b, '<strong>Figure 20.</strong> The plane-parallel sec z approximation overestimates the finite airmass near the horizon; the empirical curve remains finite.', 310)

def snr_budget():
    b = box(70, 70, 150, 70, 'Source signal', '#eff6ff', '#2457c5') + box(270, 70, 150, 70, 'Sky + dark + read', '#faf5ff', '#7c3aed') + box(470, 70, 150, 70, 'SNR', '#f0fdf7', '#059669')
    b += arrow(220, 105, 270, 105, 'snr-budget') + arrow(420, 105, 470, 105, 'snr-budget') + text(340, 200, 'SNR = S / √(S + B + D + n_pix R²)', weight=700) + text(340, 235, 'Aperture totals; longer exposure helps until systematics dominate.', size=12)
    return wrap('snr-budget', 'The exposure-time noise budget', 'Signal grows linearly with time while photon noise grows as the square root.', b, '<strong>Figure 21.</strong> Bright sky, dark current and read noise set different limits.', 270)

def filters_detectors():
    b = box(70, 80, 150, 80, 'Filter') + box(270, 80, 150, 80, 'Detector') + box(470, 80, 150, 80, 'Calibrated data', '#f0fdf7', '#059669')
    b += arrow(220, 120, 270, 120, 'filters-detectors') + arrow(420, 120, 470, 120, 'filters-detectors') + text(340, 215, 'Bias · dark · flat · standard stars', weight=700)
    return wrap('filters-detectors', 'From photons to calibrated measurements', 'Filters select bands; detectors count photons; calibration removes instrumental signatures.', b, '<strong>Figure 22.</strong> Raw counts are not magnitudes until zero points and extinction are handled.', 260)

def error_types():
    b = box(80, 80, 240, 90, 'Random error', '#eff6ff', '#2457c5') + box(360, 80, 240, 90, 'Systematic error', '#fff7ed', '#b45309')
    b += text(200, 205, 'Scatter; reduced by averaging', size=12) + text(480, 205, 'Offset; needs calibration', size=12) + text(340, 45, 'Precision and accuracy are different', weight=700)
    return wrap('error-types', 'Two broad families of measurement error', 'Random noise and systematic bias behave differently under repetition.', b, '<strong>Figure 23.</strong> A precise measurement can still be inaccurate.', 260)

def error_budget():
    rows = [('Photon noise', '√N'), ('Sky background', 'aperture + sky'), ('Read noise', 'per exposure'), ('Calibration', 'zero point / flat'), ('Atmosphere', 'extinction / seeing')]
    b = ''
    for i, (a, c) in enumerate(rows):
        b += box(90, 45 + i * 42, 240, 34, a) + box(350, 45 + i * 42, 240, 34, c, '#f8fafc', '#64748b')
    b += text(340, 285, 'List every term before quoting a final uncertainty.', weight=700)
    return wrap('error-budget', 'An error budget is a checklist', 'A final uncertainty should identify the dominant terms.', b, '<strong>Figure 24.</strong> Quadrature applies to independent standard uncertainties; correlated terms need covariance.', 310)

def linearization_plot():
    b = '<path d="M70 250H300M70 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/><path d="M380 250H620M380 250V40" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    pts = [f'{70 + 230 * t:.1f},{240 - 180 * t ** 2.5:.1f}' for t in [i / 60 for i in range(61)]]
    b += f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2457c5" stroke-width="2.5"/>' + line(390, 230, 610, 70, '#7c3aed', 'stroke-width="2.5"')
    b += text(185, 285, 'Original x, y') + text(500, 285, 'log x, log y') + text(340, 25, 'Choose axes that make the relation straight', weight=700) + text(185, 55, 'Power-law curve', '#2457c5', 11) + text(500, 55, 'Straight line', '#7c3aed', 11)
    return wrap('linearization-plot', 'Linearizing a physical law', 'Logarithms and powers can turn curves into straight lines.', b, '<strong>Figure 25.</strong> The slope and intercept of the transformed plot have physical meaning.', 310)

def residuals():
    b = '<path d="M70 160H620" stroke="#64748b" stroke-width="1.5"/>'
    for i, x in enumerate(range(100, 601, 50)):
        b += dot(x, 160 + ((i * 37) % 60 - 30), 4, '#2457c5')
    b += text(340, 45, 'Residuals should look like noise, not structure', weight=700) + text(340, 285, 'x →') + text(8, 160, 'Residual', size=12, anchor='start')
    return wrap('residuals', 'Residual plots diagnose a fit', 'Patterns in residuals reveal curvature, outliers or changing variance.', b, '<strong>Figure 26.</strong> A high R² does not guarantee a good model.', 310)

def double_star_measure():
    b = dot(250, 160, 10, '#f59e0b') + dot(430, 110, 7, '#2457c5') + line(250, 160, 430, 110, '#94a3b8', 'stroke-dasharray="6 4"')
    b += arrow(250, 160, 250, 70, 'double-star-measure', '#64748b') + '<path d="M250 110A50 50 0 0 1 293 136" fill="none" stroke="#7c3aed" stroke-width="2"/>'
    b += text(250, 190, 'A') + text(435, 95, 'B') + text(238, 62, 'N', '#64748b', 12) + text(300, 120, 'PA', '#7c3aed', 12) + text(340, 45, 'Separation and position angle describe a double star', weight=700) + text(340, 275, 'PA is measured from north through east.', size=12)
    return wrap('double-star-measure', 'Measuring a visual double star', 'A ruler gives separation; a protractor gives position angle.', b, '<strong>Figure 27.</strong> Plate scale converts chart millimetres into arcseconds.', 300)

def position_angle():
    b = arrow(340, 250, 340, 60, 'position-angle', '#64748b') + arrow(340, 250, 500, 150, 'position-angle', '#7c3aed') + '<path d="M340 190A60 60 0 0 1 391 218" fill="none" stroke="#2457c5" stroke-width="2"/>'
    b += text(340, 45, 'N') + text(520, 150, 'B', '#7c3aed', 14, 'start') + text(395, 205, 'PA', '#2457c5', 13) + text(340, 285, 'East is 90°, south 180°, west 270°.', size=12)
    return wrap('position-angle', 'Position angle convention', 'Position angle is an oriented angle on the sky.', b, '<strong>Figure 28.</strong> State the convention and the epoch when reporting measurements.', 310)

def differential_photometry():
    def trend(p):
        return 8 * sin(2 * pi * p)
    def dip(p):
        return 34 * exp(-.5 * ((p - .5) / .06) ** 2)
    target = [f'{70 + 550 * p / 300:.1f},{90 + trend(p / 300) + dip(p / 300):.1f}' for p in range(301)]
    comp = [f'{70 + 550 * p / 300:.1f},{170 + trend(p / 300):.1f}' for p in range(301)]
    diff = [f'{70 + 550 * p / 300:.1f},{245 + dip(p / 300):.1f}' for p in range(301)]
    b = f'<polyline points="{" ".join(target)}" fill="none" stroke="#2457c5" stroke-width="2.5"/><polyline points="{" ".join(comp)}" fill="none" stroke="#059669" stroke-width="2.5"/><polyline points="{" ".join(diff)}" fill="none" stroke="#7c3aed" stroke-width="2.5"/>'
    b += text(65, 70, 'Target (trend + eclipse)', '#2457c5', 11, 'start') + text(65, 155, 'Comparison (trend only)', '#059669', 11, 'start') + text(65, 232, 'Differential (eclipse remains)', '#7c3aed', 11, 'start') + text(340, 35, 'Shared trends cancel; the target eclipse does not', weight=700) + text(340, 305, 'Magnitude increases downward (schematic).', size=12)
    return wrap('differential-photometry', 'Differential photometry cancels common trends', 'Dividing by a comparison star removes shared atmospheric and instrumental variations.', b, '<strong>Figure 29.</strong> The comparison must be stable and close enough to share the same systematics.', 325)

def experiment_design():
    steps = ['Question', 'Variables', 'Controls', 'Calibration', 'Repeat', 'Uncertainty', 'Report']
    b = ''
    for i, s in enumerate(steps):
        b += box(45 + i * 86, 110, 80, 60, s, '#eff6ff' if i % 2 == 0 else '#f0fdf7', '#2457c5' if i % 2 == 0 else '#059669')
    b += text(340, 60, 'A measurement is a designed argument', weight=700) + text(340, 230, 'State what would change your conclusion.', size=12)
    return wrap('experiment-design', 'The structure of an experimental technique', 'Good technique connects a question to a calibrated, repeatable measurement.', b, '<strong>Figure 30.</strong> The final report includes method, data, uncertainty and limitations.', 270)

FIGURES = {
    'em-spectrum': em_spectrum, 'atmo-windows': atmo_windows, 'telescope-optics': telescope_optics, 'resolution': resolution,
    'iteration': iteration, 'linearization': linearization, 'derivative-integral': derivative_integral, 'ode-decay': ode_decay,
    'vector-add': vector_add, 'dot-cross': dot_cross, 'scale-drawing': scale_drawing, 'triangulation': triangulation,
    'distributions': distributions, 'error-propagation': error_propagation, 'hand-angles': hand_angles, 'limiting-magnitude': limiting_magnitude,
    'celestial-grid': celestial_grid, 'catalogue-fields': catalogue_fields, 'horizon-coords': horizon_coords, 'airmass': airmass,
    'snr-budget': snr_budget, 'filters-detectors': filters_detectors, 'error-types': error_types, 'error-budget': error_budget,
    'linearization-plot': linearization_plot, 'residuals': residuals, 'double-star-measure': double_star_measure, 'position-angle': position_angle,
    'differential-photometry': differential_photometry, 'experiment-design': experiment_design}

import re
for _i, (_k, _v) in enumerate(FIGURES.items()):
    FIGURES[_k] = re.sub(r'<strong>Figure \d+\.</strong>', f'<strong>Figure {_i % 2 + 1}.</strong>', _v())
