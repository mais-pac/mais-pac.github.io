"""Reading list shared by the IPhO handouts.

Each topic page ends with the same provenance note plus a short, honestly
described reading list. Entries are places to *learn and practise*, not
sources that the handouts copy from: every problem, figure and experiment in
this repository is original MAIS PAC material.
"""

CORE = [
    ("IPhO syllabus and statutes", "https://www.ipho-new.org/statutes-syllabus/",
     "The coverage checklist this curriculum follows: accepted 2014, amended 2015. Read it once for scope, "
     "not for depth."),
    ("IPhO past problems and solutions", "https://www.ipho-new.org/documentations/",
     "The only honest test of readiness. Work recent theoretical and experimental papers under time, then compare "
     "with the official marking schemes."),
]

BY_GROUP = {
    'Introduction and Approach': [
        ("Fermi problems (order-of-magnitude practice)", "https://en.wikipedia.org/wiki/Fermi_problem",
         "Background and examples for the estimation habits used in 01.01."),
    ],
    'Mechanics': [
        ("HyperPhysics mechanics map", "http://hyperphysics.phy-astr.gsu.edu/hbase/hframe.html",
         "A compact concept map for revising definitions and standard results quickly."),
    ],
    'Electromagnetic Fields': [
        ("MIT OpenCourseWare 8.02, Electricity and Magnetism", "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/",
         "Full lecture notes and problem sets for fields, circuits and induction."),
    ],
    'Oscillations and Waves': [
        ("MIT OpenCourseWare 8.03, Vibrations and Waves", "https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/",
         "Oscillators, resonance, superposition and optics with demonstrations."),
    ],
    'Modern Physics': [
        ("PHYSNET / modern physics overview", "https://www.physnet.org/",
         "Short modules on quanta, spectra, relativity and nuclear physics written for students."),
    ],
    'Thermodynamics and Statistical Physics': [
        ("MIT OpenCourseWare 8.01/8.02 thermodynamics notes", "https://ocw.mit.edu/",
         "Kinetic theory, the first and second laws, and heat transfer worked examples."),
    ],
    'Experimental Skills': [
        ("BIPM: SI brochure and uncertainty guidance", "https://www.bipm.org/en/publications/guides",
         "The GUM is the reference behind the uncertainty rules used in 03.02 and 03.03."),
        ("Particle Data Group: mathematical tools review", "https://pdg.lbl.gov/",
         "A compact professional summary of means, errors, fits and confidence intervals."),
    ],
    'Mathematics': [
        ("Paul's Online Math Notes", "https://tutorial.math.lamar.edu/",
         "Calculus, series and approximation practice at exactly the level the syllabus expects."),
    ],
}


def references(group):
    entries = CORE + BY_GROUP.get(group, [])
    rows = ''.join(
        f'<div class="ipho-ref"><a href="{url}">{title}</a><span>{note}</span></div>'
        for title, url, note in entries
    )
    return f'<div class="ipho-refs">{rows}</div>'
