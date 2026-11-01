"""Original inline SVG teaching diagrams for Basic Astrophysics."""
from math import sin,cos,pi

def wrap(key,title,desc,body,caption,h=300):
    return f'<figure class="cosmo-figure" id="fig-{key}"><svg viewBox="0 0 680 {h}" role="img" aria-labelledby="fig-{key}-title fig-{key}-desc" xmlns="http://www.w3.org/2000/svg"><title id="fig-{key}-title">{title}</title><desc id="fig-{key}-desc">{desc}</desc><defs><marker id="arrow-{key}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#2457c5"/></marker></defs>{body}</svg><figcaption>{caption}</figcaption></figure>'
def text(x,y,s,color='#1e3a8a',size=13,anchor='middle',weight=400):
    return f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>'
def arrow(x1,y1,x2,y2,key,color='#2457c5'):
    return f'<path d="M{x1} {y1}L{x2} {y2}" fill="none" stroke="{color}" stroke-width="2.5" marker-end="url(#arrow-{key})"/>'
def orbit():
    b='<ellipse cx="325" cy="145" rx="210" ry="108" fill="#eff6ff" stroke="#2457c5" stroke-width="2.5"/><path d="M415 145L535 145L493 225Z" fill="#bfdbfe" fill-opacity=".8"/><path d="M415 145L145 83L115 145Z" fill="#d1fae5"/><circle cx="415" cy="145" r="13" fill="#f59e0b"/><circle cx="115" cy="145" r="7" fill="#2457c5"/><circle cx="535" cy="145" r="7" fill="#7c3aed"/>'
    b+=arrow(115,145,115,75,'orbit')+arrow(535,145,535,188,'orbit','#7c3aed')
    b+=text(415,178,'focus: central mass')+text(115,174,'periapsis')+text(535,174,'apoapsis')+text(95,65,'fast','#2457c5')+text(560,207,'slow','#7c3aed')+text(325,35,'Equal time intervals sweep equal areas',weight=700)+text(325,278,'rₚ = a(1 − e)                         rₐ = a(1 + e)')
    return wrap('orbit','Elliptical orbit and equal areas','The central mass occupies a focus. A body moves faster near periapsis so that equal time intervals sweep equal areas.',b,'<strong>Figure 1.</strong> The force points toward a focus, not toward the centre of the ellipse. The two shaded sectors illustrate equal areas in equal times; the ellipse is schematic.')
def tides():
    b='<circle cx="170" cy="145" r="51" fill="#dbeafe" stroke="#2457c5" stroke-width="2"/><circle cx="535" cy="145" r="27" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>'+arrow(220,145,320,145,'tides')+arrow(170,94,170,53,'tides','#7c3aed')+arrow(170,196,170,237,'tides','#7c3aed')
    b+=text(170,149,'primary')+text(535,149,'satellite')+text(345,125,'tidal stretching')+text(170,270,'Near side pulled more; far side less',weight=700)+text(345,37,'Difference in gravity, not a new outward force',weight=700)+text(345,292,'Rigid rocky body: coefficient ≈ 1.26 R (ρM/ρm)¹ᐟ³ · fluid: ≈ 2.44 R (ρM/ρm)¹ᐟ³',size=11)
    return wrap('tides','Tidal stretching and the Roche scale','Gravity differs across an extended satellite, stretching it along the line to the primary. The Roche estimate depends on the material model.',b,'<strong>Figure 2.</strong> The Roche limit is a scale, not a universal sharp boundary. Material strength, spin and orbit matter; the quoted coefficients are idealized models.',315)
def planck():
    b='<path d="M65 245H630M65 245V38" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    for j,(T,col,lab) in enumerate([(3500,'#b45309','3500 K'),(5800,'#2457c5','5800 K'),(9000,'#7c3aed','9000 K')]):
        def f(lam):return 1/(lam**5)*1/(2.7182818**(14387.77/(lam*T))-1)
        peak=2897.77/T;mx=f(peak);pts=[]
        for i in range(240):
            lam=.08+i*2.92/239;pts.append(f'{65+lam/3*550:.1f},{245-185*f(lam)/mx:.1f}')
        b+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.5"/>'+text(470,65+j*24,lab,col,12,'start',700)
    b+=text(350,278,'wavelength λ (μm)')+text(25,150,'shape',size=12)+text(345,22,'Hotter: peak shifts blueward',weight=700)+text(350,298,'Each curve is normalized to its own peak; heights do not compare total power.',size=11)
    return wrap('planck','Blackbody spectra at three temperatures','Hotter blackbodies peak at shorter wavelengths. Curves are normalized individually so their shapes can be compared.',b,'<strong>Figure 3.</strong> Wien’s law locates the peak of the wavelength spectrum. Stefan–Boltzmann’s law gives the total surface flux; the normalized heights here are not flux measurements.',315)
def photons():
    b='<path d="M55 75H625" stroke="#94a3b8"/>'
    bands=[('radio','#dbeafe'),('microwave','#e0e7ff'),('infrared','#fee2e2'),('visible','#d1fae5'),('UV','#ede9fe'),('X-ray','#fce7f3'),('γ-ray','#f1f5f9')]
    for i,(lab,col) in enumerate(bands):
        x=55+i*81.4;b+=f'<rect x="{x}" y="85" width="79" height="56" rx="3" fill="{col}"/>'+text(x+39,118,lab,size=11)
    b+=arrow(65,165,615,165,'photons')+text(340,190,'increasing frequency and photon energy →')+text(340,50,'c = λf                    E = hf = hc/λ',weight=700)+text(340,237,'A photon is counted whole. Brightness also depends on how many arrive.',weight=700)+text(340,268,'Band boundaries are conventional; the spectrum is continuous.',size=11)
    return wrap('photons','One spectrum, two descriptions','Electromagnetic bands form a continuous sequence. Higher frequency means higher energy per photon.',b,'<strong>Figure 4.</strong> Wavelength tells you the energy of each photon, not the total luminosity. A detector’s area, exposure and efficiency determine how many photons it records.',290)
def pv():
    b='<path d="M95 245H600M95 245V35" fill="none" stroke="#64748b" stroke-width="1.5"/><path d="M165 75H480V215H165Z" fill="#eff6ff" stroke="#2457c5" stroke-width="2.5"/>'
    b+=arrow(260,75,360,75,'pv')+arrow(480,120,480,175,'pv')+arrow(370,215,270,215,'pv')+arrow(165,175,165,120,'pv')
    b+=text(340,58,'expand: W &gt; 0')+text(533,150,'cool at fixed V',size=11)+text(340,239,'compress: W &lt; 0')+text(83,135,'heat at fixed V',size=11)+text(340,151,'net work = enclosed area',weight=700)+text(605,267,'V')+text(78,32,'P')+text(340,292,'Clockwise cycle: positive net work done by the gas',weight=700)
    return wrap('pv','Work is the area under a path','A clockwise rectangular cycle does positive net work. Heat input and output are determined using the first law.',b,'<strong>Figure 5.</strong> Pressure and volume describe the state; heat and work describe energy transfer along a process. The sign convention is ΔU = Q − W, with W done by the gas.',310)
def planet():
    b='<circle cx="90" cy="145" r="37" fill="#fef3c7" stroke="#f59e0b" stroke-width="2"/><circle cx="490" cy="145" r="50" fill="#dbeafe" stroke="#2457c5" stroke-width="2"/>'
    for y in [115,145,175]:b+=arrow(140,y,427,y,'planet','#d97706')
    b+=arrow(475,96,440,48,'planet','#7c3aed')+arrow(515,102,555,45,'planet','#059669')+text(270,92,'incoming flux F')+text(475,32,'reflected: AFπR²',size=12)+text(540,223,'emitted: 4πR²σT⁴',size=12)+text(300,267,'(1 − A)FπR² = 4πR²σT⁴',weight=700)+text(340,294,'Intercepting disk ≠ emitting sphere',size=12)
    return wrap('planet','A planet’s whole-sphere energy budget','A planet intercepts light over a disk and emits over its whole surface in the uniform-temperature model.',b,'<strong>Figure 6.</strong> The factor of four is geometric. Effective radiating temperature need not equal surface temperature when an atmosphere is present.',315)
def spectra():
    b=''
    for j,(lab,kind) in enumerate([('Continuum','continuous'),('Emission','emission'),('Absorption','absorption')]):
        y=62+j*83;b+=text(80,y+25,lab,anchor='start',weight=700)
        if kind=='continuous':b+='<rect x="210" y="y" width="400" height="38" fill="url(#spec)"/>'.replace('y',str(y))
        else:
            b+=f'<rect x="210" y="{y}" width="400" height="38" fill="{"#111827" if kind=="emission" else "url(#spec)"}"/>'
            for x,col in [(285,'#22c55e'),(390,'#facc15'),(525,'#ef4444')]:b+=f'<rect x="{x}" y="{y}" width="5" height="38" fill="{col if kind=="emission" else "#111827"}"/>'
    b+='<defs><linearGradient id="spec"><stop stop-color="#7c3aed"/><stop offset=".35" stop-color="#3b82f6"/><stop offset=".6" stop-color="#22c55e"/><stop offset=".8" stop-color="#facc15"/><stop offset="1" stop-color="#ef4444"/></linearGradient></defs>'+text(340,294,'Same atomic energy gaps → same line wavelengths',weight=700)
    return wrap('spectra','Three spectra, one atomic fingerprint','A hot dense source gives a continuum; thin excited gas emits lines; cooler gas in front of a continuum removes matching wavelengths.',b,'<strong>Figure 7.</strong> Colours are schematic. Absorption requires a background source and a population able to absorb; it does not mean the atom ceases to exist.',315)
def broadening():
    b='<path d="M60 235H625M340 235V35" fill="none" stroke="#94a3b8" stroke-width="1.3"/>'
    for sig,col in [(24,'#7c3aed'),(55,'#2457c5'),(95,'#059669')]:
        pts=[f'{x},{235-175*2.7182818**(-.5*((x-340)/sig)**2):.1f}' for x in range(60,626,3)]
        b+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2.5"/>'
    b+=text(340,24,'A shift moves the centre; broadening changes the width',weight=700)+text(340,263,'wavelength →')+text(340,288,'Thermal motion, instrumental resolution and other effects can widen a line.',size=11)+text(505,80,'broader', '#059669')+text(420,110,'narrower','#7c3aed')
    return wrap('broadening','Shift and width are different measurements','Profiles with the same centre can have different widths. A centroid shift measures bulk line-of-sight motion; width contains other information.',b,'<strong>Figure 8.</strong> These are schematic emission profiles. For independent Gaussian contributions, variances add; full widths at half maximum add in quadrature only when all contributions are Gaussian.',310)
def binding():
    pts=[(70,205,'²H','1.11'),(135,89,'⁴He','7.07'),(220,77,'¹²C','7.68'),(350,57,'⁵⁶Fe','8.79'),(565,93,'²³⁵U','7.59')]
    b='<path d="M55 245H625M55 245V35" fill="none" stroke="#64748b" stroke-width="1.5"/><path d="M70 205Q100 90 135 89Q180 78 220 77Q290 50 350 57Q470 64 565 93" fill="none" stroke="#2457c5" stroke-width="2.5"/>'
    for x,y,lab,val in pts:b+=f'<circle cx="{x}" cy="{y}" r="5" fill="#7c3aed"/>'+text(x,y-15,lab,weight=700)+text(x,y+22,val,size=11)
    b+=text(340,273,'nucleon number A →')+text(25,145,'B/A',size=12)+text(340,24,'Higher binding energy per nucleon = more tightly bound',weight=700)+text(185,180,'fusion of light nuclei →','#047857')+text(500,180,'← fission of heavy nuclei','#7c3aed')
    return wrap('binding','Why both fusion and fission can release energy','Selected nuclei illustrate the rise and slow fall of binding energy per nucleon. Reactions release energy when the products are more tightly bound.',b,'<strong>Figure 9.</strong> Selected approximate values in MeV per nucleon; the connecting curve is schematic. Energy release is determined by the actual initial and final masses, not by the curve alone.',305)
def decay():
    b='<path d="M70 245H620M70 245V35" fill="none" stroke="#64748b" stroke-width="1.5"/>'
    pts=[f'{70+540*t/6:.1f},{245-190*2**(-t):.1f}' for t in [i/40 for i in range(241)]]
    b+=f'<polyline points="{" ".join(pts)}" fill="none" stroke="#2457c5" stroke-width="3"/>'
    for n in range(4):
        x=70+90*n;y=245-190*2**(-n);b+=f'<path d="M70 {y}H{x}V245" fill="none" stroke="#c7d2fe" stroke-dasharray="5 4"/><circle cx="{x}" cy="{y}" r="5" fill="#7c3aed"/>'+text(x,266,f'{n} T½',size=12)+text(x+20,y-12,f'{100/2**n:g}%',size=11)
    b+=text(340,24,'Each half-life halves what remains',weight=700)+text(340,294,'A probability law for many nuclei, not a schedule for one nucleus.',size=12)
    return wrap('decay','Exponential decay and constant half-life','The surviving fraction is one half after one half-life, one quarter after two, and one eighth after three.',b,'<strong>Figure 10.</strong> Activity is proportional to the number remaining, so it follows the same exponential. Individual decay times remain unpredictable.',315)
FIGURES={k:v for k,v in list(globals().items()) if k in ['orbit','tides','planck','photons','pv','planet','spectra','broadening','binding','decay']}
