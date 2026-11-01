## 16. Lecture + Problems: how to use the set

There are **30 problems**: twelve foundations, eight explicitly sourced website adaptations, and ten original Olympiad-level challenges. Difficulty follows the handout convention: **[1]** is a warm-up, **[2]** requires a multi-step Olympiad argument, and **[3]** is a challenge or mathematical extension. The extensions are enrichment beyond the minimum IOAA requirement to avoid differential equations.

Use the constants in Section 1 unless a problem supplies different values. Keep units until the last line. A calculator is useful; a computer is not required except for optional data exploration. Give reasons alongside numerical answers. A correct number without its assumptions is an incomplete cosmological answer.

<div class="remark" markdown="1">
<span class="remark-head">Suggested routes.</span> **First reading:** Problems 1, 3, 5–9. **Olympiad training:** 2, 4, 10–16, 20–27. **Beyond-syllabus enrichment:** 17–19 and 28–30. For a roughly 90-minute mock paper, try 3, 7, 8, 13, 20 and 22 before opening the solutions. The [interactive Hubble laboratory](06.01.html#lab-hubble) uses a clearly labelled synthetic catalogue, not real survey measurements.
</div>

**Attribution key.** “Adapted from” identifies the source of the underlying exercise; numbers, scaffolding and wording may have been changed. “MAIS original — IOAA-inspired” means an independently constructed problem motivated by the listed past-material topic, not an official or reproduced IOAA question. The [Solutions](06.01-solutions.html) restate the tasks, derive the results and explain the strategy for the difficult originals.

## 17. Foundations: from units to cosmic history

<div class="problem" id="p1" markdown="1">
<span class="prob-head">[1] Problem 1 — A rate disguised as a velocity.</span> *MAIS original foundation.*

(a) Convert $H_0=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ to $\mathrm{s^{-1}}$ and find $H_0^{-1}$ in Gyr.
(b) Find the Hubble radius $c/H_0$ in Gpc and Gly.
(c) A student says, “The universe must be 13.97 billion years old.” Explain what extra assumption would make that statement valid, and why it is not generally valid.
(d) If the benchmark density parameters are $\Omega_{m0}=0.3$ and $\Omega_{\Lambda0}=0.7$, find the present critical mass density and the mean matter mass density in SI units.

[Worked solution →](06.01-solutions.html#s1)
</div>

<div class="problem" id="p2" markdown="1">
<span class="prob-head">[2] Problem 2 — When does a galaxy trace the Hubble flow?</span> *MAIS original foundation.*

A galaxy has a line-of-sight peculiar velocity whose magnitude may be as large as $300\ \mathrm{km\,s^{-1}}$. Take $H_0=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ and use the low-redshift law.

(a) At $D=2\ \mathrm{Mpc}$, find the Hubble velocity and the largest possible fractional contamination of the inferred velocity.
(b) How far away must a galaxy be for this contamination to be at most 5%?
(c) Explain why a nearby blueshift does not disprove expansion.
(d) Why does averaging many galaxies help with random peculiar velocities but not automatically remove a coherent bulk flow?

[Worked solution →](06.01-solutions.html#s2)
</div>

<div class="problem" id="p3" markdown="1">
<span class="prob-head">[2] Problem 3 — One redshift, three different questions.</span> *MAIS original foundation.*

A rest-frame line at $486.1\ \mathrm{nm}$ is observed at $1458.3\ \mathrm{nm}$. Ignore peculiar and gravitational shifts.

(a) Find $z$ and the scale factor at emission.
(b) A rest-frame 20-day supernova feature occurs at the same redshift. How long does it appear to last?
(c) If the shift were instead interpreted as a pure special-relativistic radial Doppler effect, what speed would be inferred?
(d) Explain why the answer to (c) is not, by itself, the proper-distance recession rate of a cosmological source.

[Worked solution →](06.01-solutions.html#s3)
</div>

<div class="problem" id="p4" markdown="1">
<span class="prob-head">[2] Problem 4 — The ruler that did not stretch.</span> *MAIS original foundation.*

Two ideal comoving galaxies have a present proper separation of $12{,}000\ \mathrm{Mpc}$. A galaxy group lies between them and is gravitationally bound.

(a) What was the comoving galaxies' proper separation at $z=2$?
(b) By what factor did it change between emission and observation?
(c) Does a $1\ \mathrm{m}$ ruler inside the bound group also change by that factor? Explain.
(d) In the flat $(0.3,0.7)$ benchmark, $H(z=2)\simeq2.97H_0$. Find the Hubble-flow rate corresponding to the galaxies' separation then, in units of $c$, and state why a value above $c$ would not violate special relativity.

[Worked solution →](06.01-solutions.html#s4)
</div>

<div class="problem" id="p5" markdown="1">
<span class="prob-head">[1] Problem 5 — Critical does not mean heavy.</span> *MAIS original foundation.*

Use $H_0=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$.

(a) Derive $\rho_{\rm crit}=3H_0^2/(8\pi G)$ from the flat-space Friedmann equation.
(b) Express the corresponding energy density in $\mathrm{J\,m^{-3}}$.
(c) Using $m_p=1.67\times10^{-27}\ \mathrm{kg}$, express the critical mass density as an equivalent number of proton masses per cubic metre.
(d) Explain why this number is not a count of the actual protons in space.

[Worked solution →](06.01-solutions.html#s5)
</div>

<div class="problem" id="p6" markdown="1">
<span class="prob-head">[2] Problem 6 — A thermodynamic derivation of three eras.</span> *MAIS original foundation.*

A non-interacting uniform fluid has constant $w=P/u$ in a comoving volume $V\propto a^3$.

(a) Use $d(uV)=-P\,dV$ to derive $u(a)$.
(b) Specialize to matter, radiation and Λ.
(c) At $z=3$, find the ratios $u_m/u_{m0}$, $u_r/u_{r0}$ and $u_\Lambda/u_{\Lambda0}$.
(d) Explain physically why radiation has one extra power of $a^{-1}$.
(e) For a constant-$w$ component, find the range of $w$ that accelerates a flat universe when that component dominates.

[Worked solution →](06.01-solutions.html#s6)
</div>

<div class="problem" id="p7" markdown="1">
<span class="prob-head">[2] Problem 7 — The CMB was once warm.</span> *MAIS original foundation.*

Take $T_0=2.725\ \mathrm K$, $z_{\rm ls}=1090$, and the present photon energy density $u_{\gamma0}=4.17\times10^{-14}\ \mathrm{J\,m^{-3}}$.

(a) Find the CMB temperature and the wavelength of the peak of $B_\lambda$ at last scattering.
(b) Find the photon energy density then.
(c) By what factor has the wavelength of an individual freely propagating CMB photon increased?
(d) Why is it wrong to say that the CMB was emitted by a shell that was already at $2.725\ \mathrm K$?
(e) Explain why a temperature obtained from the peak of $B_\nu$ need not use the same numerical Wien constant.

[Worked solution →](06.01-solutions.html#s7)
</div>

<div class="problem" id="p8" markdown="1">
<span class="prob-head">[2] Problem 8 — Equality is not acceleration.</span> *MAIS original foundation.*

Use a flat matter-plus-Λ model with $\Omega_{m0}=0.3$, $\Omega_{\Lambda0}=0.7$.

(a) Find the redshift at which the matter and Λ energy densities are equal.
(b) Find the redshift at which $\ddot a=0$.
(c) Which event occurs earlier? Explain the factor of two that distinguishes them.
(d) Find $q_0$.
(e) Can $H(z)$ decrease while the expansion accelerates? Justify your answer using $q=-1-\dot H/H^2$.

[Worked solution →](06.01-solutions.html#s8)
</div>

<div class="problem" id="p9" markdown="1">
<span class="prob-head">[2] Problem 9 — A standard candle and a standard ruler.</span> *MAIS original foundation.*

At $z=1$, a flat model gives $D_C=3.30\ \mathrm{Gpc}$. A source has bolometric luminosity $L=4.00\times10^{36}\ \mathrm W$ and proper transverse diameter $\ell=20.0\ \mathrm{kpc}$.

(a) Find $d_L$, $d_A$ and the emission-time proper distance.
(b) Find the observed bolometric flux in SI units.
(c) Find the angular diameter in arcseconds.
(d) Verify distance duality.
(e) State two reasons a real finite-band observation may need corrections beyond this calculation.

[Worked solution →](06.01-solutions.html#s9)
</div>

<div class="problem" id="p10" markdown="1">
<span class="prob-head">[2] Problem 10 — The age is an integral.</span> *MAIS original foundation.*

Take $H_0=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$.

(a) Derive the age of a flat matter-only universe.
(b) For a flat matter-plus-Λ model with $(\Omega_{m0},\Omega_{\Lambda0})=(0.3,0.7)$, write the age as a definite integral and evaluate it using the closed form in Section 6.
(c) Explain physically why the second age is larger even though the present expansion rate is the same.
(d) Why should neither calculation be extrapolated unchanged through the radiation era when asking for a precision age?

[Worked solution →](06.01-solutions.html#s10)
</div>

<div class="problem" id="p11" markdown="1">
<span class="prob-head">[2] Problem 11 — A circle inside curved space.</span> *MAIS original foundation.*

On a two-dimensional sphere of radius $R$, a circle is drawn at geodesic radius $r$ from its centre.

(a) Derive its circumference $C(r)$.
(b) Expand the result for $r\ll R$ to the first non-Euclidean correction.
(c) For $R=6400\ \mathrm{km}$, estimate the radius of a circle whose circumference differs from $2\pi r$ by $1\ \mathrm m$.
(d) Explain why the result does not mean that small curved spaces are exactly Euclidean.

[Worked solution →](06.01-solutions.html#s11)
</div>

<div class="problem" id="p12" markdown="1">
<span class="prob-head">[3] Problem 12 — Three horizons in one model.</span> *MAIS original foundation; extension.*

Consider an Einstein–de Sitter universe.

(a) Derive $D_{\rm ph}(t)=3ct$ and express it in terms of $c/H$.
(b) Does this model possess a finite future event horizon? Prove your answer using a conformal-time integral.
(c) Contrast this with pure de Sitter expansion at constant $H$, for which the present event horizon is $c/H$.
(d) Explain why the particle horizon of the benchmark ΛCDM model can exceed both $ct_0$ and $c/H_0$.

[Worked solution →](06.01-solutions.html#s12)
</div>

## 18. Website-sourced problems: beyond the IOAA lists

<div class="problem" id="p13" markdown="1">
<span class="prob-head">[3] Problem 13 — When do distance definitions matter?</span> *Adapted from [Sheffield PHY306, Problem 4](https://www.hep.shef.ac.uk/roszkowski/phy306/pdf/phy306_probs.pdf).*

(a) Suppose distance measurements have a 5% systematic uncertainty. Using the leading fractional difference between $d_L$ and $d_A$, estimate the redshift above which confusing these two definitions matters at least as much as that uncertainty.
(b) For a line-of-sight peculiar velocity of $1000\ \mathrm{km\,s^{-1}}$, find the minimum distance for a velocity contamination below 10% if $H_0$ lies between 50 and 100 in the usual units. Use the most conservative value.
(c) At that distance, estimate the low-redshift $z$ for both endpoint values of $H_0$. Is the distinction between $d_L$ and $d_A$ then larger or smaller than 5%?
(d) Explain why the answer to (a) is an estimate rather than a universal sharp boundary.

[Worked solution →](06.01-solutions.html#s13)
</div>

<div class="problem" id="p14" markdown="1">
<span class="prob-head">[3] Problem 14 — Count the photons, not just their energies.</span> *Adapted from [Sheffield PHY306, Problem 3](https://www.hep.shef.ac.uk/roszkowski/phy306/pdf/phy306_probs.pdf).*

A source emits $N$ photons of emitted-frame mean energy $\bar E_{\rm em}$ during proper time $\Delta t_{\rm em}$. Assume photon conservation and a spatially flat background. At observation, the photons are spread over a sphere of area $4\pi D_C^2$.

(a) Derive the observed bolometric flux and hence $d_L=(1+z)D_C$.
(b) Use the transverse size of a ruler to derive $d_A=D_C/(1+z)$.
(c) Combine the results to obtain distance duality.
(d) Which step in (a) would fail if photons disappeared into an unobserved channel? Does spatial flatness alone guarantee photon conservation?

[Worked solution →](06.01-solutions.html#s14)
</div>

<div class="problem" id="p15" markdown="1">
<span class="prob-head">[3] Problem 15 — The Einstein–de Sitter toolkit.</span> *Adapted from [Yale ASTR 610, Problem Set 1, Problem 1](http://www.astro.yale.edu/vdbosch/astro610_problem_set1.pdf).*

A flat universe contains pressureless matter only, with no radiation or Λ at any epoch in this idealized model.

(a) Derive $a/a_0=(3H_0t/2)^{2/3}$.
(b) Show that $\bar\rho(t)=1/(6\pi Gt^2)$ and $Ht=2/3$.
(c) Derive the proper particle horizon.
(d) Evaluate the age and horizon for $H_0=70$, and explain why the horizon exceeds $ct_0$ without superluminal local light propagation.

[Worked solution →](06.01-solutions.html#s15)
</div>

<div class="problem" id="p16" markdown="1">
<span class="prob-head">[3] Problem 16 — Can tired light pass every test?</span> *Adapted from [Yale ASTR 610, Problem 3](http://www.astro.yale.edu/vdbosch/astro610_problem_set1.pdf), with additional observational checks.*

A static-space toy model proposes that photon energy obeys $dE/dr=-K E$ along its path.

(a) Solve for $E(r)$ and obtain $z(r)$.
(b) Show that the model reproduces a linear low-redshift Hubble law, and find $K$ in $\mathrm{Mpc^{-1}}$ if that law has $H_0=70$.
(c) The model merely reduces each photon's energy and does not alter emission or arrival clock rates. What duration would it predict for a 20-day rest-frame supernova feature at $z=1$? What does expansion predict?
(d) Explain why merely shifting a blackbody's photons in energy is not generally sufficient to preserve its observed temperature and intensity normalization. What additional assumptions would a competing model need?

[Worked solution →](06.01-solutions.html#s16)
</div>

<div class="problem" id="p17" markdown="1">
<span class="prob-head">[3] Problem 17 — Equality in a different thermal universe.</span> *Extension adapted from [Yale ASTR 610, Problem 2](http://www.astro.yale.edu/vdbosch/astro610_problem_set1.pdf).*

A hypothetical universe has $\Omega_\Lambda=0$, a photon background at $T_0=10.0\ \mathrm K$, and a neutrino background that remains relativistic with energy density $1.5$ times the photon energy density. Write $H_0=100h\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$.

(a) Show that $1+z_{\rm eq}=\Omega_{m0}/(\Omega_{\gamma0}+\Omega_{\nu0})$.
(b) Calculate $\Omega_{\gamma0}h^2$ for this temperature.
(c) Express $1+z_{\rm eq}$ as a numerical coefficient times $\Omega_{m0}h^2$.
(d) Why is it essential that the neutrinos remain relativistic in this hypothetical model?

[Worked solution →](06.01-solutions.html#s17)
</div>

<div class="problem" id="p18" markdown="1">
<span class="prob-head">[3] Problem 18 — Why flatness needs an explanation.</span> *Extension adapted from [MIT 8.286, Quiz 3 Review, Problem 9](https://web.mit.edu/8.286/www/quiz13/q3rp-euf13.pdf).*

For a universe with nonzero $k$, define $\Omega_{\rm tot}$ excluding the curvature contribution.

(a) Show that $\Omega_{\rm tot}-1=kc^2/(a^2H^2)$ in the convention of Section 4.
(b) In an exactly matter-dominated era, find how $(\Omega_{\rm tot}-1)/\Omega_{\rm tot}$ scales with $t$.
(c) Repeat for an exactly radiation-dominated era.
(d) During inflation with nearly constant $H$, how does $|\Omega_{\rm tot}-1|$ scale with the number of e-folds? Explain why this helps the flatness problem without proving that $k$ has changed.

[Worked solution →](06.01-solutions.html#s18)
</div>

<div class="problem" id="p19" markdown="1">
<span class="prob-head">[3] Problem 19 — A very distant quasar: check the meaning of “distance.”</span> *Extension adapted from [MIT 8.286, Quiz 3 Review, Problem 10](https://web.mit.edu/8.286/www/quiz13/q3rp-euf13.pdf). The historical source parameters are retained as a calculation, not a current record claim.*

Use $z=5.82$, $H_0=65\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$, $\Omega_{m0}=0.35$, $\Omega_{\Lambda0}=0.65$, and neglect radiation.

(a) Write definite integrals for the present age, the age at emission, the present proper distance and the emission-time proper distance.
(b) Write the present proper-distance recession rate in terms of one of those distances.
(c) Evaluate the distances and times to two significant figures; numerical integration or the interactive distance lab is allowed.
(d) Explain how a present distance of roughly 27 billion light-years is compatible with a light-travel time below 14 billion years.

[Worked solution →](06.01-solutions.html#s19)
</div>

<div class="problem" id="p20" markdown="1">
<span class="prob-head">[2] Problem 20 — A BAAO redshift calculation, with its approximation exposed.</span> *Adapted from [BAAO 2015 Round 2, Question 12](https://www.bpho.org.uk/baao/Papers/R2/BAAO_2015.pdf).*

A galaxy has $z=0.30$ and a rest-frame hydrogen line at $486.1\ \mathrm{nm}$. Take $H_0=72\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$. For parts (a)–(c), deliberately use the low-redshift approximation $v=cz=H_0D$.

(a) Find the observed wavelength.
(b) Find the inferred distance in Mpc.
(c) Find the corresponding light-travel time in Gyr.
(d) Now use the flat $(0.3,0.7)$ model with the same $H_0$ to estimate the lookback time and luminosity distance. Why do the answers differ?
(e) Which use of the relativistic Doppler formula would still not give the model's present proper-distance recession rate?

[Worked solution →](06.01-solutions.html#s20)
</div>

## 19. Original Olympiad challenges, inspired by IOAA materials

<div class="problem" id="p21" markdown="1">
<span class="prob-head">[3] Problem 21 — A rocket against the Hubble flow.</span> *MAIS original — inspired by IOAA 2022 Theory 4, “Journey Between Galaxies.” New distances, speed choices and limiting-case analysis.*

A destination galaxy is initially $D_0=10.0\ \mathrm{Mpc}$ away and comoving with a background for which $H=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ remains constant. A rocket leaves us toward it with constant **peculiar speed** $u$ relative to the local comoving frame. Its proper separation $D(t)$ from us obeys

$$
\frac{dD}{dt}=H D-u.
$$

Ignore gravity, acceleration time and fuel limits.

(a) Solve for $D(t)$.
(b) Find the threshold launch speed for eventual arrival. Can a $1000\ \mathrm{km\,s^{-1}}$ rocket arrive?
(c) Find the travel time for $u=1500\ \mathrm{km\,s^{-1}}$.
(d) Describe the limiting behaviour as $u$ approaches the threshold from above.
(e) Why is $D_0/u$ not the correct general answer? State one reason the constant-$H$ assumption is not a full model of our universe.

[Worked solution →](06.01-solutions.html#s21)
</div>

<div class="problem" id="p22" markdown="1">
<span class="prob-head">[3] Problem 22 — Weighing dark energy, then asking when it wins.</span> *MAIS original — inspired by IOAA 2023 Theory 5, “Dark Energy.” Adds a pressure and acceleration diagnostic.*

Assume spatial flatness, $H_0=70$, and present matter density $\rho_{m0}=2.8\times10^{-27}\ \mathrm{kg\,m^{-3}}$. Neglect radiation for this late-time exercise. The remaining density is a cosmological constant.

(a) Find the dark-energy mass-equivalent density and energy density.
(b) Find $\Omega_{m0}$ and $\Omega_{\Lambda0}$.
(c) Find the redshift of matter–Λ equality and the redshift at which acceleration begins.
(d) Find the present deceleration parameter.
(e) A student argues that negative pressure produces an inward pressure-gradient force, so it cannot accelerate expansion. Identify the conceptual error.

[Worked solution →](06.01-solutions.html#s22)
</div>

<div class="problem" id="p23" markdown="1">
<span class="prob-head">[3] Problem 23 — A warm spectrum and a deliberately wrong clock.</span> *MAIS original — inspired by IOAA 2024 Theory 5, “CMB.” The matter-only assumption is supplied explicitly and then tested.*

An idealized observation identifies a CMB spectrum whose $B_\lambda$ peak is at $0.500\ \mathrm{mm}$. Use $T_0=2.725\ \mathrm K$ and $b_{\rm W}=2.898\times10^{-3}\ \mathrm{m\,K}$.

(a) Find its temperature, redshift and scale factor relative to today.
(b) In a flat matter-only model with $H_0=70$ and no other components at any time, estimate the cosmic age at that redshift.
(c) Explain why this is not a precision estimate for the real universe at that epoch.
(d) If the same wavelength shift were instead a local special-relativistic Doppler shift, calculate the corresponding speed. Why is this not the preferred interpretation of the CMB redshift?

[Worked solution →](06.01-solutions.html#s23)
</div>

<div class="problem" id="p24" markdown="1">
<span class="prob-head">[3] Problem 24 — A small scar on a blackbody.</span> *MAIS original — inspired by IOAA 2020 Team 14, “Spectral Distortions of the CMB.” This is a simplified fixed-photon-number energy-budget model, not a thermalization calculation.*

Suppose an episode injects energy into the CMB after processes that change photon number have become ineffective. Assume the radiation subsequently relaxes to a Bose–Einstein spectrum

$$
n(x)=\frac{1}{e^{x+\mu}-1},\qquad x=\frac{h\nu}{k_{\rm B}T}.
$$

For small positive $\mu$, the fractional changes relative to a blackbody at the same temperature are given as

$$
\frac{\Delta N}{N}\simeq-1.368\mu,
\qquad
\frac{\Delta u}{u}\simeq-1.111\mu.
$$

Photon number is fixed, so the temperature is allowed to adjust. Blackbody scalings are $N\propto T^3$ and $u\propto T^4$.

(a) Show that an injected fractional energy $\epsilon=\Delta u_{\rm inj}/u_i$ produces $\mu\simeq1.40\epsilon$ to first order.
(b) Estimate $\mu$ for $\epsilon=10^{-5}$ and the fractional temperature adjustment.
(c) Why would it be inconsistent to keep both photon number and temperature fixed after a positive energy injection?
(d) Explain why this estimate cannot be applied unchanged to an early epoch when photon-producing reactions remain efficient.

[Worked solution →](06.01-solutions.html#s24)
</div>

<div class="problem" id="p25" markdown="1">
<span class="prob-head">[3] Problem 25 — Counting neutrons into helium.</span> *MAIS original — inspired by the BBN topic of IOAA 2025 Theory 10. The assumptions below define a standalone neutron-counting exercise.*

At a stage just before efficient nucleosynthesis, the neutron-to-proton ratio is $r_0=1/6$. For the next $200\ \mathrm s$, assume no weak interconversion, a free-neutron mean lifetime $\tau_n=880\ \mathrm s$, and negligible expansion of the comoving volume. Then assume all surviving neutrons are incorporated into helium-4, with the remaining protons becoming hydrogen.

(a) Find the neutron-to-proton ratio at the end of the delay.
(b) Find the helium-4 mass fraction $Y_p$, neglecting small nuclear mass defects.
(c) Find the number ratio $n_{\rm He}/n_{\rm H}$.
(d) Why is the helium mass fraction not $r/(1+r)$?
(e) Explain qualitatively how a higher baryon density could change the delay and hence the helium abundance. Why is the real calculation more involved than this model?

[Worked solution →](06.01-solutions.html#s25)
</div>

<div class="problem" id="p26" markdown="1">
<span class="prob-head">[3] Problem 26 — A hidden magnitude error is a hidden Hubble constant.</span> *MAIS original — IOAA-style data and error reasoning, informed by the distance-ladder themes of IOAA 2023–2024 materials.*

A low-redshift supernova sample has accurately measured relative distances, but every assumed absolute magnitude is too bright by $0.050\ \mathrm{mag}$: $M_{\rm assumed}-M_{\rm true}=-0.050$.

(a) Does the analysis overestimate or underestimate luminosity distances? Find the fractional bias.
(b) Find the corresponding fractional bias in $H_0$.
(c) If the biased estimate is $70.0$, estimate the calibration-corrected value.
(d) Explain why the shape of a relative supernova Hubble diagram can still constrain acceleration even with an unknown constant magnitude offset.
(e) Would a magnitude error that grows with redshift be equally harmless? Explain.

[Worked solution →](06.01-solutions.html#s26)
</div>

<div class="problem" id="p27" markdown="1">
<span class="prob-head">[3] Problem 27 — One ruler, two expansion measurements.</span> *MAIS original — IOAA-style standard-ruler inference; connects CMB/BAO concepts rather than copying an official question.*

At $z=0.50$, a galaxy survey measures a transverse BAO angle $\theta=0.0300\ \mathrm{rad}$ and a radial BAO redshift separation $\Delta z=0.0450$. The comoving ruler is $r_d=147\ \mathrm{Mpc}$. Assume small angles and intervals, and a flat geometry.

(a) Find $D_M(z)$ from the transverse signal.
(b) Find $H(z)$ from the radial signal.
(c) Find $d_A$ and $d_L$ at this redshift.
(d) If the assumed $r_d$ were 2% too large, how would the inferred $D_M$ and $H$ change?
(e) Explain why these measurements alone do not uniquely identify the microscopic nature of dark energy.

[Worked solution →](06.01-solutions.html#s27)
</div>

<div class="problem" id="p28" markdown="1">
<span class="prob-head">[3] Problem 28 — Designing a curvature experiment.</span> *MAIS original — IOAA-style geometric estimation, extending the website-sourced curved-space problem.*

A positively curved spatial geometry has curvature radius $R_c=20.0\ \mathrm{Gpc}$. Ideal observers measure a circle at geodesic radius $r=2.00\ \mathrm{Gpc}$ on one cosmic-time slice. Ignore expansion during the measurement and all observational systematics.

(a) Estimate the circumference deficit relative to $2\pi r$ using the first non-Euclidean term.
(b) Express the fractional deficit.
(c) If the circumference can be measured to 1% fractional precision, is this a convincing detection?
(d) Suggest two reasons a real cosmic curvature test is harder than this idealized circle.
(e) Why does failure to detect curvature not prove that the entire universe is spatially infinite?

[Worked solution →](06.01-solutions.html#s28)
</div>

<div class="problem" id="p29" markdown="1">
<span class="prob-head">[3] Problem 29 — The last message that can arrive.</span> *MAIS original — IOAA-style horizon reasoning, inspired by the expanding-background ideas in IOAA 2022 Theory 4.*

Assume the future universe is exactly de Sitter with constant $H=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$. Two galaxies are comoving and initially separated by $D_0$.

(a) A light signal is sent toward us now. Solve for its proper distance $D(t)$ from us.
(b) Find the maximum $D_0$ for which it ever arrives, and express the answer in Gpc and Gly.
(c) For $D_0=0.8c/H$, find the arrival time.
(d) What happens at exactly $D_0=c/H$?
(e) Distinguish this event horizon from the particle horizon and from the maximum distance of objects whose old light we see today.

[Worked solution →](06.01-solutions.html#s29)
</div>

<div class="problem" id="p30" markdown="1">
<span class="prob-head">[3] Problem 30 — How much inflation is enough?</span> *MAIS original — inspired by early-universe themes across IOAA materials and the Sheffield/MIT inflation exercises. A simplified, self-contained estimate.*

During inflation, $H$ is approximately constant and the scale factor grows by $e^N$. Immediately afterward, suppose the universe is radiation-dominated until a matter-dominated era; for this estimate, use the supplied net result that the comoving Hubble radius grows by a factor $10^{26}$ between the end of inflation and today. Assume inflation starts with $|\Omega_{\rm tot}-1|\sim1$ and that the pre-inflationary region is causally connected on the initial Hubble scale.

(a) By what factor does $|\Omega_{\rm tot}-1|$ decrease during $N$ e-folds?
(b) Find the minimum $N$ for it to be below $10^{-5}$ immediately after inflation, before the later growth.
(c) Including the supplied later growth factor, find the minimum $N$ for a present deviation below $10^{-5}$.
(d) Explain why the two bounds are so different, and why neither is a model-independent measurement of the actual number of e-folds.
(e) Explain how the same shrinking comoving Hubble radius addresses the horizon problem. Why does inflation not predict a perfectly smooth universe with no density perturbations?

[Worked solution →](06.01-solutions.html#s30)
</div>

## 20. After the problems: explain what you learned

For each challenge, write a three-sentence explanation without equations: what changes, what stays fixed, and which observation would test the claim. Then compare your explanation with the **Idea** and **Checks** paragraphs in the Solutions. The aim is not to recognize a formula quickly; it is to know why that formula is the right description.

**Download the practice data:** [synthetic Hubble catalogue (CSV)](data/hubble-practice.csv). The catalogue's generating value is $H_0=72$ with fixed, non-random perturbations added for teaching. It must not be cited as an observational measurement of the real Hubble constant.
