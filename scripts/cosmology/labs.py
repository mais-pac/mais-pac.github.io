"""Accessible, dependency-free experiment shells; behaviour is in labs.js."""

def shell(key,number,title,description,controls,outputs,prompt,height=310):
    return f'''<section class="cosmo-lab" id="lab-{key}" aria-labelledby="lab-{key}-title">
<div class="lab-heading"><span class="lab-kicker">Interactive experiment {number}</span><h3 id="lab-{key}-title">{title}</h3><p>{description}</p></div>
<div class="lab-controls">{controls}</div>
<div class="lab-outputs">{outputs}</div>
<svg class="lab-canvas" id="plot-{key}" viewBox="0 0 680 {height}" role="img" aria-labelledby="plot-{key}-title" xmlns="http://www.w3.org/2000/svg"><title id="plot-{key}-title">{title}: interactive vector plot</title><desc>Use the labelled controls to update the plot. Numerical results are also provided as text below.</desc></svg>
<p class="lab-summary" id="summary-{key}" aria-live="polite"></p>
<div class="lab-prompt"><strong>Try this.</strong> {prompt}</div>
<p class="print-only lab-print-note">This is a snapshot of the interactive experiment. Open the HTML edition to change its controls.</p>
<noscript><p class="lab-noscript">JavaScript is disabled. The lecture, figures, problems and solutions remain readable; enable JavaScript to use the experiments.</p></noscript>
</section>'''

def out(key,label,value='—'):
    return f'<div><span>{label}</span><output id="out-{key}">{value}</output></div>'

def reset(key):
    return f'<button type="button" class="print-btn" data-reset="{key}">Reset experiment</button>'

def expansion():
    controls=f'''<label for="expansion-a">Scale factor <i>a</i><input id="expansion-a" type="range" min="0.5" max="2" step="0.01" value="1"></label><output class="range-value" id="range-expansion">1.00</output><button type="button" class="print-btn" id="expansion-play">Animate expansion</button>{reset('expansion')}'''
    outputs=''.join([out('exp-a','Scale factor'),out('exp-da','Galaxy A: 100 Mpc × a'),out('exp-db','Galaxy B: 300 Mpc × a'),out('exp-ratio','Distance ratio B/A')])
    return shell('expansion',1,'Every separation grows. No galaxy is the centre.','The dots are ideal comoving galaxies. Their plotted sizes stay fixed while their separations scale. Galaxy A has χ = 100 Mpc; B has χ = 300 Mpc. This is a kinematic illustration, not a solution for H(t).',controls,outputs,'Double <i>a</i>. Do the galaxies get larger? Does B/A change? Move the conceptual observer to another dot: the same proportional stretching still applies.')

def dynamics():
    controls=f'''<label for="dynamics-om">Matter density Ω<sub>m0</sub><input id="dynamics-om" type="range" min="0.05" max="1" step="0.01" value="0.3"></label><output class="range-value" id="range-dynamics-om">0.30</output><label for="dynamics-h0">H₀ [km s⁻¹ Mpc⁻¹]<input id="dynamics-h0" type="range" min="50" max="90" step="1" value="70"></label><output class="range-value" id="range-dynamics-h0">70</output><button type="button" class="print-btn" data-preset="eds">Matter only</button><button type="button" class="print-btn" data-preset="benchmark">Benchmark</button>{reset('dynamics')}'''
    outputs=''.join([out('dyn-ol','ΩΛ0 = 1 − Ωm0'),out('dyn-age','Present age'),out('dyn-q','q₀'),out('dyn-zeq','Matter–Λ equality z'),out('dyn-zacc','Acceleration begins at z')])
    return shell('dynamics',2,'Change the contents. Change the cosmic clock.','A flat matter-plus-Λ model, with radiation neglected. Blue shows E(z) = H/H₀; green shows q(z). Negative q means accelerating expansion. The age integral includes the supplied matter and Λ components only.',controls,outputs,'Set Ω<sub>m0</sub> = 1. The age becomes 2/(3H₀). Return to 0.3: find the redshift where q crosses zero, and compare it with the lower redshift where the two densities are equal.',330)

def cmb():
    controls=f'''<label for="cmb-log">log₁₀(1 + z)<input id="cmb-log" type="range" min="0" max="9" step="0.0001" value="3.0378"></label><output class="range-value" id="range-cmb">3.04</output><button type="button" class="print-btn" data-cmb="0">Today</button><button type="button" class="print-btn" data-cmb="3.0378">Last scattering</button><button type="button" class="print-btn" data-cmb="8.564666">BBN scale</button>{reset('cmb')}'''
    outputs=''.join([out('cmb-z','Redshift z'),out('cmb-t','Temperature'),out('cmb-peak','Bλ peak wavelength'),out('cmb-u','Energy density / today')])
    return shell('cmb',3,'Watch a blackbody cool without losing its shape.','The solid blue curve is the selected epoch; the dashed grey curve is today. Both are normalized to their own peak so that the shift is visible across many orders of magnitude. Their actual intensities are very different.',controls,outputs,'Choose last scattering. Was the CMB then microwave-coloured? Move to the BBN temperature scale and compare the wavelength shift with the energy-density ratio. The BBN preset is a temperature scale, not a claim that a free-streaming CMB already existed then.',330)

def distance_lab():
    controls=f'''<label for="distances-z">Observed redshift z<input id="distances-z" type="range" min="0" max="10" step="0.01" value="1"></label><output class="range-value" id="range-distances">1.00</output>{reset('distances')}'''
    outputs=''.join([out('dist-dc','Comoving / present proper'),out('dist-dl','Luminosity distance'),out('dist-da','Angular-diameter distance'),out('dist-time','Lookback time'),out('dist-v','Present recession rate HD₀ / c'),out('dist-horizons','Particle / event horizon')])
    return shell('distances',4,'Ask which distance you mean.','Flat benchmark: H₀ = 70, Ω<sub>m0</sub> = 0.3, Ω<sub>Λ0</sub> = 0.7; radiation is neglected. The curves are computed by numerical integration, not by cz/H₀. Horizon values are present-day proper distances for this same model.',controls,outputs,'Compare z = 1 and z = 3. The luminosity distance keeps increasing, but the angular-diameter distance turns over. Find the approximate turnover by moving the slider. Why does a more distant ruler not always look smaller?',350)

def hubble():
    controls=f'''<label for="hubble-cut">Minimum redshift included<select id="hubble-cut"><option value="0">All galaxies</option><option value="0.02">z ≥ 0.020</option><option value="0.03">z ≥ 0.030</option><option value="0.05">z ≥ 0.050</option></select></label><label class="lab-check"><input type="checkbox" id="hubble-errors" checked> Show ±200 km s⁻¹ error bars</label><button type="button" class="print-btn" id="hubble-export">Download selected CSV</button>{reset('hubble')}'''
    outputs=''.join([out('hub-h','Fitted H₀ [km s⁻¹ Mpc⁻¹]'),out('hub-err','Formal statistical error'),out('hub-n','Galaxies included'),out('hub-rms','Velocity RMS residual')])
    return shell('hubble',5,'Fit the Hubble law—and notice what the fit cannot tell you.','These twelve observations are <strong>synthetic teaching data</strong>, generated with H₀ = 72 and fixed velocity perturbations. The fit is constrained through the origin with equal velocity uncertainties. It is not a measurement of the real universe.',controls,outputs,'Exclude the nearest galaxies. Does the scatter decrease? The formal error does not include a shared distance-calibration error or correlated bulk flow. Why should those be reported separately?',350)

LABS={'expansion':expansion,'dynamics':dynamics,'cmb':cmb,'distances':distance_lab,'hubble':hubble}
