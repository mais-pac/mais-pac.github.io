"""Original inline SVG figures. No raster images or external assets."""
from math import sin, pi

def wrap(name, title, desc, body, caption, box='0 0 680 300'):
    return f'''<figure class="cosmo-figure" id="fig-{name}">
<svg viewBox="{box}" role="img" aria-labelledby="fig-{name}-title fig-{name}-desc" xmlns="http://www.w3.org/2000/svg">
<title id="fig-{name}-title">{title}</title><desc id="fig-{name}-desc">{desc}</desc>
<defs><marker id="arrow-{name}" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0 0L7 3.5L0 7Z" fill="#2457c5"/></marker></defs>
{body}</svg><figcaption>{caption}</figcaption></figure>'''

def wave(x,y,width,amp,cycles,color):
    pts=[]
    for i in range(181):
        t=i/180;pts.append(f'{x+width*t:.1f},{y+amp*sin(2*pi*cycles*t):.1f}')
    return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{color}" stroke-width="2.5"/>'

def timeline():
    nodes=[(65,'Hot early state','before the first nuclei'),(185,'First minutes','light nuclei form'),(315,'0.38 Myr','CMB released'),(455,'First stars','reionization begins'),(610,'Today','accelerating expansion')]
    b='<rect x="1" y="1" width="678" height="278" rx="8" fill="#fbfcff"/><path d="M45 145H638" stroke="#2457c5" stroke-width="3" marker-end="url(#arrow-timeline)"/>'
    for i,(x,label,sub) in enumerate(nodes):
        col=['#4338ca','#2457c5','#059669','#7c3aed','#1e3a8a'][i]
        b+=f'<circle cx="{x}" cy="145" r="7" fill="{col}"/><path d="M{x} 145V{95 if i%2==0 else 190}" stroke="#c7d2fe"/>'
        yy=65 if i%2==0 else 218
        b+=f'<text x="{x}" y="{yy}" text-anchor="middle" font-weight="700" fill="{col}">{label}</text><text x="{x}" y="{yy+20}" text-anchor="middle" fill="#526079" font-size="11">{sub}</text>'
    b+='<text x="340" y="266" text-anchor="middle" fill="#6e767d" font-size="11">Sequence shown; time intervals and physical sizes are not to scale.</text>'
    return wrap('timeline','A sequence of cosmic thermal milestones','The hot early state precedes nucleosynthesis, CMB release, the first stars and the present accelerating universe.',b,'<strong>Figure 1.</strong> A thermal history, not a map of an explosion. The CMB is released long after the light elements form.')

def redshift():
    b='<rect x="1" y="1" width="678" height="288" rx="8" fill="#fbfcff"/><text x="170" y="34" text-anchor="middle" font-weight="700" fill="#4338ca">Emitted: a = 1/3</text><text x="510" y="34" text-anchor="middle" font-weight="700" fill="#2457c5">Observed: a = 1</text>'
    b+=wave(45,100,250,24,5,'#4338ca')+wave(385,100,250,24,5/3,'#2457c5')
    b+='<path d="M310 100H365" stroke="#2457c5" stroke-width="2" marker-end="url(#arrow-redshift)"/><path d="M45 155H95M385 155H535" stroke="#526079" stroke-width="1.5"/><text x="70" y="177" text-anchor="middle">λ emitted</text><text x="460" y="177" text-anchor="middle">λ observed = 3 λ emitted</text><rect x="75" y="207" width="530" height="55" rx="6" fill="#f3f6ff" stroke="#c7d2fe"/><text x="340" y="230" text-anchor="middle" font-weight="700" fill="#1e3a8a">The same stretching applies to clocks.</text><text x="340" y="250" text-anchor="middle" fill="#526079" font-size="12">20 days at the source → 60 days for the observer when z = 2.</text>'
    return wrap('redshift','Wavelength and time intervals stretch together','Five wave cycles emitted in a compact interval are observed across three times the width; a twenty-day event is observed for sixty days.',b,'<strong>Figure 2.</strong> Redshift stretches wavelength and duration by the same factor. The wave amplitudes are schematic and are not an intensity calculation.')

def curvature():
    b='<rect x="1" y="1" width="678" height="278" rx="8" fill="#fbfcff"/>'
    b+='<g transform="translate(113 123)"><ellipse rx="78" ry="76" fill="#f5f5ff" stroke="#4338ca" stroke-width="1.7"/><ellipse rx="78" ry="24" fill="none" stroke="#c7d2fe"/><path d="M0 -76Q-60 -5 -48 58Q5 78 61 43Q48 -32 0 -76Z" fill="#e0e7ff" fill-opacity=".6" stroke="#4338ca" stroke-width="2"/><circle cy="-76" r="3" fill="#4338ca"/><circle cx="-48" cy="58" r="3" fill="#4338ca"/><circle cx="61" cy="43" r="3" fill="#4338ca"/></g>'
    b+='<g transform="translate(340 130)"><path d="M-90 55L0 -72L87 55Z" fill="#eff6ff" stroke="#2457c5" stroke-width="2"/><path d="M-20 -43Q0 -32 20 -43" fill="none" stroke="#93c5fd"/><text x="0" y="30" text-anchor="middle" fill="#2457c5">180°</text></g>'
    b+='<g transform="translate(567 127)"><path d="M-88 -40Q0 65 88 -40L70 60Q0 5 -70 60Z" fill="#f0fdf7" stroke="#059669" stroke-width="1.6"/><path d="M-88 -40Q0 -80 88 -40M-70 60Q0 95 70 60M-50 -54Q-30 5 -42 64M0 -61V48M50 -54Q30 5 42 64" fill="none" stroke="#a7f3d0"/><path d="M0 -48Q-34 -6 -52 38Q0 17 52 38Q32 -5 0 -48Z" fill="#d1fae5" fill-opacity=".75" stroke="#047857" stroke-width="2"/></g>'
    for x,lab,sub,col in [(113,'Positive','angle sum &gt; 180°','#4338ca'),(340,'Flat','angle sum = 180°','#2457c5'),(567,'Negative','angle sum &lt; 180°','#047857')]:
        b+=f'<text x="{x}" y="231" text-anchor="middle" font-weight="700" fill="{col}">{lab}</text><text x="{x}" y="252" text-anchor="middle" font-size="12" fill="#526079">{sub}</text>'
    return wrap('curvature','Three local spatial geometries','A spherical triangle has an angle sum above 180 degrees, a Euclidean triangle 180 degrees, and a hyperbolic triangle below 180 degrees.',b,'<strong>Figure 3.</strong> Curvature is measured by relations inside space. These are local geometry sketches, not claims about the global topology of the universe.','0 0 680 280')

def distances():
    b='<rect x="1" y="1" width="678" height="298" rx="8" fill="#fbfcff"/><circle cx="75" cy="133" r="10" fill="#2457c5"/><text x="75" y="165" text-anchor="middle" font-weight="700">Observer</text><rect x="563" y="83" width="14" height="100" rx="4" fill="#4338ca"/><text x="570" y="62" text-anchor="middle" font-weight="700">Source</text><path d="M563 85L85 128M563 181L85 138" fill="none" stroke="#2457c5" stroke-width="2"/><path d="M90 128L563 85L563 181L90 138Z" fill="#dbeafe" fill-opacity=".45"/><path d="M95 215H560" stroke="#526079" stroke-dasharray="5 4"/><text x="328" y="238" text-anchor="middle">D_C: the separation on a present-day cosmic-time slice</text><text x="328" y="115" text-anchor="middle" fill="#2457c5">angle → d_A</text><text x="328" y="161" text-anchor="middle" fill="#4338ca">energy + arrival rate → d_L</text><rect x="65" y="257" width="550" height="30" rx="5" fill="#f3f6ff"/><text x="340" y="277" text-anchor="middle" font-weight="700" fill="#1e3a8a">Flat space: d_L = (1 + z) D_C and d_A = D_C / (1 + z)</text>'
    return wrap('distances','Two operational definitions of distance','A source and observer are connected by a light bundle. Its angular extent defines angular-diameter distance, while received energy and photon arrival rate define luminosity distance.',b,'<strong>Figure 4.</strong> The same source can have different distances because a flux measurement and an angular-size measurement ask different questions.')

def inflation():
    b='<rect x="1" y="1" width="678" height="318" rx="8" fill="#fbfcff"/><rect x="90" y="40" width="205" height="218" fill="#f5f5ff"/><text x="192" y="28" text-anchor="middle" font-weight="700" fill="#4338ca">Inflation</text><text x="470" y="28" text-anchor="middle" font-weight="700" fill="#2457c5">Hot expansion afterwards</text><path d="M65 258H630M65 258V45" fill="none" stroke="#6e767d" stroke-width="1.5" marker-end="url(#arrow-inflation)"/><path d="M90 82L295 220Q325 237 355 220L600 65" fill="none" stroke="#4338ca" stroke-width="3"/><path d="M95 224L595 65" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="7 4"/><circle cx="177" cy="165" r="5" fill="#059669"/><circle cx="473" cy="144" r="5" fill="#059669"/><text x="170" y="145" text-anchor="end" fill="#047857" font-size="12">horizon exit</text><text x="483" y="132" fill="#047857" font-size="12">horizon re-entry</text><text x="443" y="206" fill="#4338ca" font-size="12">comoving Hubble radius c/(aH)</text><text x="410" y="78" fill="#047857" font-size="12">a fixed comoving scale</text><text x="350" y="282" text-anchor="middle" fill="#526079">logarithmic expansion →</text><text x="24" y="155" transform="rotate(-90 24 155)" text-anchor="middle" fill="#526079">logarithmic scale</text><text x="340" y="306" text-anchor="middle" font-size="11" fill="#6e767d">Schematic trends; slopes and transition sharpness are not a fitted model.</text>'
    return wrap('inflation','The comoving Hubble radius shrinks during inflation','A fixed comoving scale exits the shrinking Hubble radius during inflation and re-enters the growing comoving Hubble radius during the later hot expansion.',b,'<strong>Figure 5.</strong> Inflation stretches a small causal patch. The same shrinking comoving Hubble radius suppresses the observable curvature deviation.','0 0 680 320')

def horizons():
    b='<rect x="1" y="1" width="678" height="358" rx="8" fill="#fbfcff"/><path d="M340 190L150 30H530Z" fill="#dbeafe" fill-opacity=".7"/><path d="M340 190L240 30H440Z" fill="#d1fae5" fill-opacity=".7"/><path d="M105 310H605M105 310V22" stroke="#6e767d" stroke-width="1.5" fill="none"/><path d="M150 30L340 190L530 30M240 30L340 190L440 30" stroke="#2457c5" stroke-width="2" fill="none"/><path d="M340 310V30" stroke="#4338ca" stroke-width="2" stroke-dasharray="4 4"/><path d="M115 190H590" stroke="#94a3b8" stroke-dasharray="5 4"/><circle cx="340" cy="190" r="6" fill="#1e3a8a"/><text x="352" y="184" font-weight="700" fill="#1e3a8a">us, now</text><text x="348" y="328" fill="#526079" font-size="12">comoving radius χ</text><text x="52" y="171" transform="rotate(-90 52 171)" text-anchor="middle" fill="#526079">conformal time cη</text><text x="120" y="52" fill="#2457c5" font-size="12">past light cone</text><text x="447" y="52" fill="#047857" font-size="12">future reach</text><text x="455" y="286" fill="#2457c5" font-size="12">particle-horizon scale</text><path d="M150 293H530" stroke="#2457c5" stroke-width="1.5"/><text x="449" y="112" fill="#047857" font-size="12">event-horizon scale</text><path d="M240 95H440" stroke="#059669" stroke-width="1.5"/><text x="340" y="348" text-anchor="middle" font-size="11" fill="#6e767d">A finite beginning and a finite future conformal time are assumed in this sketch.</text>'
    return wrap('horizons','Particle and event horizons in conformal coordinates','The past light cone determines what can be observed now. The future light cone determines where a signal sent now can eventually reach. Their comoving widths need not be equal.',b,'<strong>Figure 6.</strong> Radial light rays are straight in conformal coordinates. The particle horizon looks backward; the event horizon looks forward.','0 0 680 360')

FIGURES={'timeline':timeline,'redshift':redshift,'curvature':curvature,'distances':distances,'inflation':inflation,'horizons':horizons}
