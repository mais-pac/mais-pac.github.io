"""Registry for the IPhO HTML-first curriculum.

The codes mirror the numbering of the IPhO syllabus (2014, amended 2015):
codes 01.* mirror Section 1 (introduction), 02.* Section 2 (theoretical
skills), 03.* Section 3 (experimental skills), 04.* Section 4 (mathematics).
`group` is the Teaching-page grouping index and `group_name` its heading.

Each topic is one file `scripts/ipho/<code>.md` in the same authoring format as
the IOAA extended curriculum: lecture sections, `{{FIG:...}}` and `{{LAB:...}}`
components, then `<!-- PROBLEMS -->` and `<!-- SOLUTIONS -->` blocks.
"""
TOPICS = [
    {'code': '01.01', 'key': 'iphogeneral', 'title': 'Working as a Physicist: Approximation, Symmetry and Units',
     'group': 0, 'group_name': 'Introduction and Approach'},
    {'code': '02.01', 'key': 'kinematics', 'title': 'Kinematics: Describing Motion',
     'group': 1, 'group_name': 'Mechanics'},
    {'code': '02.02', 'key': 'statics', 'title': 'Statics: Forces, Torques and Equilibrium',
     'group': 1, 'group_name': 'Mechanics'},
    {'code': '02.03', 'key': 'dynamics', 'title': 'Dynamics: Energy, Momentum and Rotation',
     'group': 1, 'group_name': 'Mechanics'},
    {'code': '02.04', 'key': 'celestial', 'title': 'Celestial Mechanics and Gravitation',
     'group': 1, 'group_name': 'Mechanics'},
    {'code': '02.05', 'key': 'hydro', 'title': 'Hydrodynamics and Surface Tension',
     'group': 1, 'group_name': 'Mechanics'},
    {'code': '02.06', 'key': 'electrostatics', 'title': 'Electrostatics and Steady Currents',
     'group': 2, 'group_name': 'Electromagnetic Fields'},
    {'code': '02.07', 'key': 'magnetic', 'title': 'Magnetic Fields and Induction',
     'group': 2, 'group_name': 'Electromagnetic Fields'},
    {'code': '02.08', 'key': 'circuits', 'title': 'Circuits, Capacitors and Inductors',
     'group': 2, 'group_name': 'Electromagnetic Fields'},
    {'code': '02.09', 'key': 'oscillations', 'title': 'Oscillations and Resonance',
     'group': 3, 'group_name': 'Oscillations and Waves'},
    {'code': '02.10', 'key': 'waves', 'title': 'Waves, Sound and the Doppler Effect',
     'group': 3, 'group_name': 'Oscillations and Waves'},
    {'code': '02.11', 'key': 'optics', 'title': 'Optics: Lenses, Gratings and Interferometers',
     'group': 3, 'group_name': 'Oscillations and Waves'},
    {'code': '02.12', 'key': 'relativity', 'title': 'Special Relativity',
     'group': 4, 'group_name': 'Modern Physics'},
    {'code': '02.13', 'key': 'quantum', 'title': 'Quantum Physics: Waves, Atoms and Spectra',
     'group': 4, 'group_name': 'Modern Physics'},
    {'code': '02.14', 'key': 'matter', 'title': 'Structure of Matter and Nuclear Physics',
     'group': 4, 'group_name': 'Modern Physics'},
    {'code': '02.15', 'key': 'thermo', 'title': 'Thermodynamics and the Ideal Gas',
     'group': 5, 'group_name': 'Thermodynamics and Statistical Physics'},
    {'code': '02.16', 'key': 'heat', 'title': 'Heat Transfer, Phase Transitions and Radiation',
     'group': 5, 'group_name': 'Thermodynamics and Statistical Physics'},
    {'code': '03.01', 'key': 'measurement', 'title': 'Measurement, Apparatus and Accuracy',
     'group': 6, 'group_name': 'Experimental Skills'},
    {'code': '03.02', 'key': 'uncertainty', 'title': 'Uncertainty Analysis',
     'group': 6, 'group_name': 'Experimental Skills'},
    {'code': '03.03', 'key': 'dataanalysis', 'title': 'Data Analysis and Linear Fitting',
     'group': 6, 'group_name': 'Experimental Skills'},
    {'code': '04.01', 'key': 'algebra', 'title': 'Algebra, Functions and Geometry',
     'group': 7, 'group_name': 'Mathematics'},
    {'code': '04.02', 'key': 'complex', 'title': 'Vectors and Complex Numbers',
     'group': 7, 'group_name': 'Mathematics'},
    {'code': '04.03', 'key': 'calculus', 'title': 'Calculus',
     'group': 7, 'group_name': 'Mathematics'},
    {'code': '04.04', 'key': 'approximation', 'title': 'Approximation, Taylor Series and Numerical Methods',
     'group': 7, 'group_name': 'Mathematics'},
]
BY_CODE = {t['code']: t for t in TOPICS}
PROBLEMS_PER_TOPIC = 10
GROUPS = []
for topic in TOPICS:
    if not GROUPS or GROUPS[-1][0] != topic['group_name']:
        GROUPS.append((topic['group_name'], []))
    GROUPS[-1][1].append(topic)
