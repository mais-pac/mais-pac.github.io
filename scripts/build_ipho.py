"""Build the introductory IPhO study sheets. Content is original club material."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parents[1]
source='https://physicscup.ee/wp-content/uploads/2019/10/Syllabus-new.pdf'
data={
'ipho-theory':('Theoretical Skills',[
('2.1 General','Model the system before calculating: identify scales, make justified approximations and exploit symmetry. Check dimensions and limiting cases.'),
('2.2 Mechanics','Kinematics relates displacement, velocity and acceleration. Apply force and torque balance, Newton’s laws, conservation of energy and momentum, and angular momentum. For gravitation use the potential −GM/r and orbital energy; fluids require pressure, buoyancy, continuity and Bernoulli’s equation. Surface tension adds an energy cost for area.'),
('2.3 Electromagnetic fields','Use superposition, Coulomb’s law and Gauss’s law for symmetric charge distributions. Magnetic forces act perpendicular to velocity; induction follows Faraday’s and Lenz’s laws. In circuits, Kirchhoff’s rules and Ohm’s law determine currents; capacitor and inductor energies are CV²/2 and LI²/2. For sinusoidal AC, combine complex impedances.'),
('2.4 Oscillations and waves','For a mass and spring, ω = √(k/m); near a stable equilibrium small oscillations are often harmonic. Waves satisfy v = fλ. Interference depends on path difference, diffraction limits resolution, and refraction obeys n₁ sin θ₁ = n₂ sin θ₂. Thin lenses obey 1/f = 1/u + 1/v with consistent signs.'),
('2.5 Relativity','In inertial frames the spacetime interval is invariant. The Lorentz factor is γ = 1/√(1−v²/c²); a moving clock’s elapsed time is dilated by γ. Total energy and momentum satisfy E² = p²c² + m²c⁴.'),
('2.6 Quantum physics','Photons carry E = hf and p = h/λ. Atomic transitions emit or absorb energy equal to the level difference. The uncertainty relation ΔxΔp ≥ ħ/2 limits simultaneous localization and momentum precision. Nuclear decay follows N = N₀e^(−λt), with half-life ln 2/λ.'),
('2.7 Thermodynamics and statistical physics','The ideal gas law is pV = nRT. With work done by the gas W, the first law is ΔU = Q − W. An ideal reversible heat engine between temperatures Tₕ and T꜀ has efficiency 1 − T꜀/Tₕ. Radiation from a black body has power σAT⁴; phase changes involve latent heat.')], [
('A body starts from rest and accelerates uniformly at 2 m/s² for 3 s. Find its speed and displacement.','v = at = 6 m/s; x = at²/2 = 9 m.'),
('A 2 kg mass moves at 3 m/s. Find its kinetic energy.','K = mv²/2 = 9 J.'),
('A 12 V ideal battery is connected across a 4 Ω resistor. Find current and power.','I = V/R = 3 A; P = VI = 36 W.'),
('A wave travels at 12 m/s with frequency 3 Hz. Find its wavelength.','λ = v/f = 4 m.'),
('A thin converging lens has f = 10 cm and an object at u = 30 cm. Find the image distance.','1/v = 1/10 − 1/30 = 1/15 cm⁻¹, so v = 15 cm, a real image.'),
('A clock moves at 0.6c relative to a lab. How much lab time passes during 4 s of proper time?','γ = 1/√(1−0.6²) = 1.25, so Δt = γΔτ = 5 s.'),
('A radioactive sample has a half-life of 2 hours. What fraction remains after 6 hours?','Three half-lives pass, leaving (1/2)³ = 1/8.'),
('An ideal heat engine operates between 600 K and 300 K. What is its maximum efficiency?','The Carnot limit is 1 − 300/600 = 0.50, or 50%.')]),
'ipho-mathematics':('Mathematics',[
('4.1 Algebra','Factor and solve equations, retaining only physically meaningful roots. Arithmetic and geometric series simplify repeated contributions; for ratio r ≠ 1, Σₖ₌₀ⁿ⁻¹rᵏ = (1−rⁿ)/(1−r).'),
('4.2 Functions','Use trigonometric identities, inverse functions, exponentials and logarithms. For example, ln(ab) = ln a + ln b and sin(a+b) = sin a cos b + cos a sin b.'),
('4.3 Geometry and stereometry','Use radians in calculus, similarity, sine and cosine rules, and standard areas and volumes. Recognize circles, ellipses, parabolas and hyperbolas as conic sections.'),
('4.4 Vectors','Resolve vectors into components. The dot product is ab cos θ and the cross product has magnitude ab sin θ. Their signs and directions encode work and torque; the derivative of a rotating vector may change direction without changing its magnitude.'),
('4.5 Complex numbers','Write z = a + ib = re^(iφ). Multiplication adds phases, while division subtracts them. Complex amplitudes simplify sinusoidal steady-state circuits; the observable is the real part.'),
('4.6 Statistics','For independent observations, the mean is x̄ = Σxᵢ/n. The sample standard deviation is s = √[Σ(xᵢ−x̄)²/(n−1)]; the estimated standard error of the mean is s/√n.'),
('4.7 Calculus','A derivative measures local rate; a definite integral accumulates change. Apply product and chain rules, use initial conditions to determine integration constants, and interpret the gradient as the direction of steepest increase.'),
('4.8 Approximate and numerical methods','For |x| ≪ 1, (1+x)ᵅ ≈ 1+αx. Bisection brackets a root by repeatedly halving an interval with opposite endpoint signs. The trapezoidal rule approximates an integral by a sum of trapezoid areas.')], [
('Solve x² − 5x + 6 = 0.','Factor as (x−2)(x−3) = 0; x = 2 or 3. A physical problem may rule out a root.'),
('Solve e^(−t/2) = 1/4 for t.','Taking logarithms gives −t/2 = −ln 4, hence t = 2 ln 4.'),
('Find the area of a circle of radius 3 m.','A = πr² = 9π m².'),
('For a = (1, 2) and b = (3, 4), find a · b.','a · b = 1×3 + 2×4 = 11.'),
('Express (1+i)² in algebraic form.','(1+i)² = 1 + 2i + i² = 2i.'),
('Measurements are 2, 4 and 6. Find their mean and sample standard deviation.','The mean is 4. The squared deviations sum to 8, so s = √(8/2) = 2.'),
('If x(t) = 3t² + 2, find velocity and displacement from t = 0 to t = 2.','v = dx/dt = 6t. The displacement is x(2) − x(0) = 12.'),
('Approximate √1.04 to first order in 0.04.','Using (1+x)¹ᐟ² ≈ 1+x/2 gives 1.02; this is close to 1.0198.')]),
'ipho-experimental':('Experimental Skills and Data Analysis',[
('3.2 Safety','Identify hazards before measuring; use safe voltages, avoid viewing bright sources directly, and follow equipment instructions. Do not improvise with hazardous apparatus.'),
('3.3 Measurement techniques and apparatus','Choose suitable instruments and ranges, account for zero offsets and instrument loading, and record units. Plan repeated measurements and a control where practical.'),
('3.4 Accuracy','Measure many periods rather than one to reduce timing uncertainty. Sample enough points to resolve the behaviour, especially near rapid changes; report sensible significant figures.'),
('3.5 Experimental uncertainty analysis','Separate random scatter from systematic bias. Repetition can reduce random uncertainty in the mean but does not eliminate a common calibration error. Propagate uncertainties using a stated method and identify the dominant contribution.'),
('3.6 Data analysis','Linearize a model when useful. Plot measured points and error bars with labeled axes and units; fit a line, interpret its slope and intercept, and estimate uncertainty using a reasonable graphical or statistical method.')],[
('Twenty oscillations take 40.0 s. Find the period.','T = 40.0/20 = 2.00 s. Timing many cycles reduces the relative effect of start–stop reaction time.'),
('A length is (10.0 ± 0.1) cm. What is its relative uncertainty?','0.1/10.0 = 0.01, or 1%. State whether the uncertainty is absolute or relative.'),
('For y = ax + b, two points on a fitted line are (1, 3) and (3, 7). Find slope and intercept.','a = (7−3)/(3−1) = 2 and b = 3−2×1 = 1. These points are on the fitted line, not necessarily raw data.'),
('Every reading has the same unknown zero offset. Will repeating the measurement remove it?','No. Repetition reduces random scatter but the shared offset is systematic; calibrate or measure the zero independently.')])}

# Explanations and challenges are original club material, not Savchenko extracts.
title, sections, problems = data['ipho-theory']
sections.extend([
('A physicist’s toolkit: why symmetry and limits matter', 'Imagine balancing two identical pulls. If nothing distinguishes left from right, the answer cannot choose one side. Symmetry can make components vanish before any algebra. A model is a simplified story, not reality itself: state what is neglected, then test the story in an extreme case. For example, if friction tends to zero, a result should approach the frictionless answer.'),
('Mechanics: the accounting of motion', 'A force is not needed to keep an object moving; it changes momentum. Imagine keeping two separate books: momentum changes only by external impulse, while energy may move between kinetic, potential and thermal forms. Momentum can be conserved in a collision even when kinetic energy is not. For rotation, replace mass by moment of inertia and speed by angular speed; torque changes angular momentum.'),
('Fields and circuits: local pushes, global bookkeeping', 'An electric field says what force a small positive test charge would feel at a location. Gauss’s law counts flux through a closed surface; it finds the field easily only when symmetry also tells us its direction and magnitude. A circuit is not a reservoir that uses up charge: charge flows around a loop, while energy is transferred to components. A capacitor stores energy in its electric field, and an inductor resists changes in current.'),
('Waves: adding disturbances, not intensities', 'A wave transports a disturbance. When two coherent waves meet, add their displacements first: equal in-phase displacements reinforce, opposite ones cancel. Intensity depends on the square of the resulting amplitude. A standing wave is built from oppositely travelling waves; its nodes do not mean that each individual travelling wave has stopped.'),
('Relativity: compare events before comparing clocks', 'An event has a time and a place. A clock measures proper time between events on its own worldline, but different observers disagree about simultaneity. Time dilation applies to a moving clock between two ticks, with both ticks at the same place in that clock’s frame. The invariant interval lets observers agree on the relationship between events even when their coordinates differ.'),
('Quantum and thermal physics: probabilities and energy flow', 'Quantum theory predicts probabilities for outcomes, not merely a tiny classical orbit that we have failed to see. The energy of a photon depends on frequency, not on intensity; increasing intensity at fixed frequency increases photon flux. Temperature is not heat: temperature describes thermal state, whereas heat is energy transferred because of a temperature difference. The first law is energy bookkeeping; the second law limits which transformations are possible.')])
problems.extend([
('Challenge 1 — A small block is released from rest at height h on a frictionless fixed track. At the bottom it collides and sticks to a stationary block of equal mass on a horizontal frictionless surface. Find their common speed and the fraction of the original mechanical energy converted to internal energy in the collision.', 'Before impact, energy gives v = √(2gh). During the short collision, horizontal momentum is conserved: mv = 2mV, so V = √(2gh)/2. The final kinetic energy is (1/2)(2m)V² = mgh/2, half the initial mgh. Thus half is converted to internal energy. Kinetic energy is not conserved in the sticking collision.'),
('Challenge 2 — A satellite is in a circular orbit of radius r around a spherical body of mass M. A brief tangential impulse reduces its speed to a fraction α of the original circular speed, where 0 < α < 1. Find the semimajor axis a of the new orbit and identify whether the impulse point is periapsis or apoapsis.', 'Initially v₀² = GM/r. The specific energy after the impulse is ε = α²GM/(2r) − GM/r = −GM(2−α²)/(2r). Using ε = −GM/(2a) gives a = r/(2−α²). Radial speed is zero at the impulse and speed is below circular, so this point is apoapsis. The α → 1 limit gives a → r; α = 0 is excluded because the orbit degenerates into radial fall.'),
('Challenge 3 — Two identical capacitors of capacitance C are isolated. One initially has voltage V; the other is uncharged. They are connected in parallel with matching polarities by idealized conducting wires. Find the final voltage and the energy dissipated during redistribution.', 'Charge is conserved: initial charge CV becomes 2CVf, so Vf = V/2. Initial energy is CV²/2; final energy is 2 × C(V/2)²/2 = CV²/4. The difference CV²/4 is dissipated or radiated during the transient. An exactly lossless, zero-inductance connection cannot describe this transient physically.'),
('Challenge 4 — A source emits light of vacuum wavelength λ. In a double-slit experiment with slit separation d and screen distance L ≫ d, determine the distance between neighbouring bright fringes near the centre. State the approximation.', 'At angle θ the path difference is approximately d sin θ. Adjacent maxima differ by λ in path difference. For small θ, sin θ ≈ tan θ ≈ y/L, so Δy ≈ λL/d. This assumes coherent slits and paraxial geometry.'),
('Challenge 5 — A particle at rest of rest mass M decays into two photons travelling in opposite directions. Find each photon’s energy. What changes if the photon energies are unequal in the laboratory?', 'In the rest frame initial momentum is zero. Opposite photon momenta must have equal magnitudes, so their energies are equal. Energy conservation gives E₁ = E₂ = Mc²/2. In a laboratory frame where the parent moves, photon energies need not match; the total energy and momentum still transform and are conserved.'),
('Challenge 6 — One mole of a monatomic ideal gas expands quasistatically and isothermally from V to 2V at temperature T. Find the work done by the gas and heat absorbed. Then compare its entropy change with that of a reservoir at the same T.', 'Since p = RT/V′, W = ∫ᵥ²ᵥ RT dV′/V′ = RT ln 2. For an ideal gas internal energy depends only on temperature, so ΔU = 0 and Q = W. Gas entropy rises by Qrev/T = R ln 2; a reservoir at the same temperature loses R ln 2. In the reversible limit total entropy change is zero.')])
data['ipho-theory'] = title, sections, problems


title, sections, problems = data['ipho-mathematics']
problems.extend([
('Challenge 1 — A positive solution of x + εx² = 1 is close to 1 when |ε| is small. Find it to first order in ε.', 'Put x = 1 + aε + O(ε²). Substitution gives 1 + (a+1)ε + O(ε²) = 1, so a = −1 and x = 1−ε + O(ε²). This is the branch continuous at ε = 0.'),
('Challenge 2 — An ideal series RC circuit has resistance R, capacitance C and angular frequency ω. Find the magnitude of the voltage across the capacitor divided by the source voltage.', 'With the e^(iωt) convention, ZC = 1/(iωC). The voltage-divider ratio is ZC/(R+ZC) = 1/(1+iωRC). Its magnitude is 1/√(1+ω²R²C²). It approaches 1 at low frequency and 0 at high frequency.')])
data['ipho-mathematics'] = title, sections, problems

title, sections, problems = data['ipho-experimental']
problems.extend([
('Challenge 1 — A pendulum has T² = (4π²/g)L. A line fit of T² versus L gives slope (4.00 ± 0.08) s²/m. Estimate g and its uncertainty using first-order propagation.', 'g = 4π²/slope = 9.87 m/s². Since g is inversely proportional to slope, the relative uncertainty is 0.08/4.00 = 0.02. Therefore Δg ≈ 0.20 m/s² and g = (9.87 ± 0.20) m/s². This assumes the slope uncertainty captures the relevant errors and the model is valid.'),
('Challenge 2 — A resistor is measured with a voltmeter of finite resistance connected in parallel with it, and an ammeter measuring the total current supplied to both branches. Does V/I overestimate or underestimate the resistor’s true resistance? Explain.', 'The ammeter reads I = V/R + V/Rv. Thus V/I = RRv/(R+Rv), smaller than R for finite positive Rv. A high-resistance voltmeter reduces this loading bias; repeated readings alone cannot remove it.')])
data['ipho-experimental'] = title, sections, problems

def page(key,title,sections,problems,solutions):
    label='Worked Solutions' if solutions else 'Lecture + Problems'
    nav=f'<a href="../teaching/#ipho">← IPhO curriculum</a> · <a href="{key}{"" if solutions else "-solutions"}.html">{"Lecture + Problems" if solutions else "Worked solutions →"}</a>'
    content=''
    if not solutions:
        content=''.join(f'<section><h2>{escape(h)}</h2><p>{escape(t)}</p></section>' for h,t in sections)
        content+='<h2>Problems</h2><p>Try each problem before opening the worked solutions. Exercises are original MAIS PAC teaching material, not official IPhO problems.</p>'
    else: content='<p>These worked solutions accompany the original MAIS PAC problems. Check your assumptions and units.</p>'
    content+='<ol>'+''.join(f'<li class="{"solution" if solutions else "problem"}"><p>{escape(q)}</p>'+ (f'<p><strong>Solution.</strong> {escape(a)}</p>' if solutions else '')+'</li>' for q,a in problems)+'</ol>'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>IPhO {escape(title)}: {label} · MAIS PAC</title><link rel="stylesheet" href="../style.css"><link rel="stylesheet" href="../scripts/cosmology/cosmology.css"></head><body><div class="handout-bar"><div class="handout-bar__inner">{nav} <button class="print-btn" onclick="window.print()">Print / PDF</button></div></div><main class="sheet-page cosmology-lecture"><div class="running-head">MAIS PAC · IPhO</div><header class="sheet-title-block"><h1>{escape(title)}</h1><p class="sheet-subtitle">International Physics Olympiad · {label}</p><p class="cosmo-meta">Introductory study guide · {len(problems)} original problems</p></header><div class="sheet-intro"><p>Organized around the IPhO syllabus. This guide is not exhaustive; consult the <a href="../teaching/pdf/ipho-syllabus.pdf">syllabus study PDF</a> and the <a href="https://www.ipho-new.org/statutes-syllabus/">IPhO syllabus webpage</a> for the full scope and qualifications.</p></div>{content}<nav class="sheet-nav">{nav}</nav></main></body></html>'''

for key,(title,sections,problems) in data.items():
    for sol in (False,True):
        (R/'handouts'/f'{key}{"-solutions" if sol else ""}.html').write_text(page(key,title,sections,problems,sol))
