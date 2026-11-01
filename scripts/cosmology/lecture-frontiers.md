## 8. The thermal universe and the CMB

### Why expansion cools radiation

A blackbody spectrum is specified by a temperature. For freely streaming photons, every frequency scales as $\nu\propto a^{-1}$. The Planck distribution keeps its shape if the temperature also scales as $a^{-1}$:

$$
B_\nu(T)=\frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/k_{\rm B}T}-1},
\qquad
\boxed{T(z)=T_0(1+z)}.
$$

You can see the cancellation directly: replace $\nu$ by $\nu/(1+z)$ and $T$ by $T/(1+z)$. The exponential is unchanged, while the prefactor supplies the intensity dilution. The occupation of photon states is preserved; a thermal spectrum does not become an arbitrary collection of lower-energy photons merely because the universe expands.

The total radiation energy density and photon number density obey

$$
u_\gamma=a_{\rm rad}T^4=\frac{4\sigma_{\rm SB}}{c}T^4,
\qquad
n_\gamma=\frac{2\zeta(3)}{\pi^2}\left(\frac{k_{\rm B}T}{\hbar c}\right)^3
\simeq 20.29\,T^3\ \mathrm{cm^{-3}}.
$$

At $T_0=2.725\ \mathrm K$, $u_\gamma\simeq4.17\times10^{-14}\ \mathrm{J\,m^{-3}}$, $n_\gamma\simeq410\ \mathrm{cm^{-3}}$, and the mean photon energy is $u_\gamma/n_\gamma\simeq2.701k_{\rm B}T$. The peak of $B_\lambda$ is at $b_{\rm W}/T\simeq1.064\ \mathrm{mm}$. The peak of $B_\nu$ occurs at a different wavelength when plotted against wavelength: a peak is a property of the chosen spectral variable, not a unique photon colour.

{{LAB:cmb}}

### Recombination is not the first moment photons existed

At high temperature, matter is ionized and photons scatter frequently from free electrons. As the universe cools, electrons and nuclei combine into neutral atoms. This process is called **recombination**, although the electrons and nuclei had not previously been combined. Around $z\simeq1090$, the scattering rate falls enough for most CMB photons to stream freely. The **last-scattering surface** is a broad statistical shell in our past, not a material wall.

A crude Saha equilibrium estimate for hydrogen is

$$
\frac{x_e^2}{1-x_e}=\frac{1}{n_{\rm H}}
\left(\frac{m_ek_{\rm B}T}{2\pi\hbar^2}\right)^{3/2}
e^{-13.6\,\mathrm{eV}/k_{\rm B}T},
$$

where $x_e$ is the ionized fraction under the simplified assumptions. It illustrates why recombination occurs near a few thousand kelvin rather than at $13.6\ \mathrm{eV}/k_{\rm B}\simeq1.58\times10^5\ \mathrm K$: there are many photons per baryon, and the high-energy tail can keep hydrogen ionized. A precision calculation also follows the rates of reactions and the loss of equilibrium; the detailed ionization history is not obtained by putting $k_{\rm B}T=13.6\ \mathrm{eV}$.

At last scattering, $T\simeq2.725\times1091\simeq2970\ \mathrm K$. The photons were then near optical/infrared wavelengths. Expansion has moved that spectrum into microwaves. The CMB is therefore a relic of a hot, opaque phase—not light emitted by a cold shell at today's 2.725 K.

### A thermal bath with a few fingerprints

The CMB is astonishingly close to a blackbody and nearly isotropic. Its largest temperature pattern is a **dipole** associated mainly with our motion relative to the CMB rest frame. For small speed, $\Delta T/T\simeq(v/c)\cos\theta$. After subtracting the dipole and foreground emission, intrinsic fluctuations are of order $10^{-5}$. Those tiny variations are the seeds and tracers of cosmic structure.

Do not confuse three statements:

- **Spectral:** the distribution of intensity with frequency is nearly Planckian.
- **Isotropic:** the temperature is nearly the same in different directions.
- **Homogeneous:** the underlying large-scale matter distribution is statistically uniform.

They are related through cosmological physics, but they are not interchangeable measurements.

### The light-element recipe

During the first several minutes, nuclear reactions produced much of the universe's helium-4, some deuterium and helium-3, and small amounts of lithium-7. This is **Big Bang nucleosynthesis (BBN)**. Most hydrogen nuclei survived as hydrogen. The heavier elements were made mainly later, in stars and stellar explosions or mergers.

A useful sequence is:

1. At high temperature, weak interactions interconvert neutrons and protons.
2. As the temperature falls, the neutron-to-proton ratio decreases and weak reactions freeze out.
3. Free neutrons decay while stable deuterium formation is delayed by energetic photons—the **deuterium bottleneck**.
4. Once deuterium survives, reactions rapidly assemble helium-4.
5. Expansion and falling density stop efficient fusion before large amounts of heavier elements form.

If the neutron-to-proton ratio just before nucleosynthesis is $r=n_n/n_p$, and essentially every available neutron enters helium-4, the helium mass fraction is

$$
Y_p=\frac{4n_{\rm He}}{n_{\rm H}+4n_{\rm He}}
=\frac{2r}{1+r}.
$$

For $r=1/7$, $Y_p=1/4$. This is a counting result, not a complete nuclear-reaction network. The baryon-to-photon ratio $\eta=n_b/n_\gamma\sim6\times10^{-10}$ controls how efficiently reactions occur. Deuterium is particularly sensitive to the baryon density; the observed abundances provide a remarkable consistency test with the CMB. The predicted and observed lithium-7 abundances do not agree perfectly—the unresolved **lithium problem** is a reason to distinguish a successful framework from a claim that every detail is solved.

### Thermal milestones, approximately

| Epoch | Redshift / temperature scale | Physical change |
|---|---|---|
| early radiation era | model-dependent | relativistic particles dominate the energy density |
| BBN | $T\sim10^9\ \mathrm K$, first minutes | light nuclei form |
| matter–radiation equality | $z\sim3400$ in the real universe | matter and radiation densities become equal |
| recombination / last scattering | $z\simeq1090$, age about $0.38\ \mathrm{Myr}$ | CMB photons begin free streaming |
| first stars and reionization | broadly $z\sim6$–20, source-dependent | ultraviolet light reionizes intergalactic gas |
| late-time acceleration | benchmark $z\simeq0.67$ | $\ddot a$ changes sign |

The order of BBN and recombination matters: **nuclei form first; neutral atoms form much later.** The numerical ages depend on the cosmological model, and “first stars” is not a single sharply defined instant.

## 9. Reading the CMB and the matter distribution

### From a map to a power spectrum

Write the fractional temperature fluctuation in direction $\hat{\mathbf n}$ as $\Delta T(\hat{\mathbf n})/T$. Decompose it into spherical harmonics:

$$
\frac{\Delta T}{T}(\hat{\mathbf n})=\sum_{\ell m}a_{\ell m}Y_{\ell m}(\hat{\mathbf n}),
\qquad
C_\ell=\left\langle |a_{\ell m}|^2\right\rangle.
$$

You do not need to memorize the special functions to understand the question: **how much fluctuation is present on each angular scale?** Large $\ell$ means small angular separation, roughly $\theta\sim180^\circ/\ell$. A plotted quantity is often $\ell(\ell+1)C_\ell/(2\pi)$ rather than $C_\ell$ itself. Always read the axes before comparing peak heights.

Before photons decouple, gravity pulls the photon–baryon fluid into overdensities while photon pressure resists compression. The result is acoustic oscillations. Modes caught at different phases produce a series of peaks. The sound horizon at the drag epoch is the characteristic comoving distance a pressure wave could travel:

$$
r_s=\int_0^{t_{\rm drag}}\frac{c_s(t)}{a(t)}dt,
\qquad
c_s\simeq\frac{c}{\sqrt{3(1+R)}},
\qquad
R=\frac{3\rho_b}{4\rho_\gamma}.
$$

The precise BAO ruler $r_d$ and the CMB sound horizon $r_*$ refer to closely related but not identical epochs. They are both of order $150\ \mathrm{Mpc}$ in the standard model; do not replace one by the other in a precision calculation without checking the definition.

### What different features tell us

- **Angular acoustic scale:** the ratio of a known early-universe ruler to its distance tests geometry and expansion history. The first peak near $\ell\sim200$ is consistent with nearly flat spatial geometry in the full model.
- **Relative peak heights:** baryons add inertia to the photon–baryon fluid, changing compression and rarefaction peaks. Matter density affects the gravitational potentials and the epoch of equality.
- **Damping tail:** photon diffusion smooths very small-scale fluctuations, producing Silk damping. The finite thickness of last scattering also matters.
- **Large-angle patterns:** primordial fluctuations, gravitational potential effects and the integrated evolution of potentials all contribute. There is no single “Doppler-only” explanation of the entire map.
- **Polarization:** Thomson scattering with a quadrupolar incident radiation field generates linear polarization. Its pattern can be separated into E and B components. Lensing converts some E into B; primordial gravitational waves could also produce B modes, but a B-mode detection would require careful treatment of dust and other foregrounds.

A single beautiful CMB image is not a measurement of every cosmological parameter by itself. Parameter constraints come from a model fitted to spectra, with foreground cleaning, instrumental calibration, likelihoods and degeneracies.

### Baryon acoustic oscillations as a ruler

The same early pressure waves leave a preferred separation in the late-time matter distribution. It is not a sharp shell around every galaxy. It is a small statistical excess in pair separations—a feature in the correlation function or a sequence of wiggles in the power spectrum.

For a transverse BAO measurement,

$$
\theta_{\rm BAO}\simeq\frac{r_d}{D_M(z)}.
$$

For a radial measurement, a small redshift interval obeys

$$
\Delta z\simeq\frac{H(z)r_d}{c}.
$$

Thus BAO can constrain distances and $H(z)$, but the absolute scale requires a calibrated $r_d$. This is why BAO and supernova data are complementary: one is particularly sensitive to a physical ruler, the other to relative luminosity distances.

## 10. Dark matter, dark energy and the growth of structure

The words sound similar because both name inferred ingredients rather than directly identified laboratory substances. Their roles are very different.

| Question | Cold dark matter | Cosmological constant / dark energy |
|---|---|---|
| Clustering | clusters gravitationally | approximately smooth in ΛCDM |
| Pressure | approximately zero | $P=-u$ for Λ |
| Density scaling | $a^{-3}$ | constant for Λ |
| Main role here | helps structure grow | drives late-time acceleration |
| Typical evidence | rotation curves, lensing, clusters, CMB and structure | supernova distances combined with CMB/BAO and other probes |

Dark matter is not simply “dark ordinary gas.” BBN, the CMB and structure formation constrain the total baryon density and favour a dominant nonbaryonic matter component. Its particle identity remains unknown. Modified-gravity alternatives must address the full set of observations, not just one galaxy rotation curve.

### A simple growth calculation

Define the matter density contrast

$$
\delta(\mathbf x,t)=\frac{\rho_m(\mathbf x,t)-\bar\rho_m(t)}{\bar\rho_m(t)}.
$$

On subhorizon scales, after radiation pressure effects are negligible, linearized Newtonian gravity gives

$$
\ddot\delta+2H\dot\delta-4\pi G\bar\rho_m\delta=0.
$$

The three terms say: the overdensity accelerates inward, expansion supplies a drag-like term, and gravity amplifies the contrast. In an Einstein–de Sitter universe, try $\delta\propto t^n$. Since $H=2/(3t)$ and $4\pi G\bar\rho_m=2/(3t^2)$,

$$
n(n-1)+\frac43n-\frac23=0
\quad\Rightarrow\quad
n=\frac23,\ -1.
$$

The growing mode is $\delta\propto t^{2/3}\propto a$. Linear growth is slow, not an instantaneous collapse. Once $\delta\sim1$, nonlinear collapse and virialization require more than this equation. During strong radiation domination or Λ domination, matter growth is less efficient. Dark energy therefore affects not only distances but also the history of structure.

The observed cosmic web is a major constraint. A universe with only the tiny baryonic perturbations expected without an additional gravitating matter component has difficulty reaching today's structure by the available time. Modern analyses quantify the clustering amplitude with parameters such as $\sigma_8$ and $S_8=\sigma_8\sqrt{\Omega_{m0}/0.3}$; these are model- and scale-dependent summaries, not direct photographs of “the amount of dark matter.”

## 11. Inflation and the limits of the hot Big Bang

### Two puzzles in ordinary decelerating expansion

**Horizon puzzle.** Widely separated regions of the last-scattering surface have nearly the same temperature. In a universe that was always radiation- or matter-dominated after its beginning, many of those regions would not have had time to exchange a signal. Why do they share such similar conditions?

**Flatness puzzle.** The curvature contribution relative to the total density obeys

$$
|\Omega_{\rm tot}-1|=\frac{|k|c^2}{a^2H^2}.
$$

During radiation domination, $aH\propto a^{-1}$ decreases, so the fractional curvature deviation grows approximately as $a^2$. During matter domination it grows approximately as $a$. A universe close to flat today would have had to be extraordinarily close to flat in the early decelerating era. This is a question about initial conditions, not a logical contradiction.

### The key idea: shrink the comoving Hubble radius

Inflation is a proposed early interval of accelerated expansion,

$$
\ddot a>0
\quad\Longleftrightarrow\quad
\frac{d}{dt}\left(\frac{c}{aH}\right)<0.
$$

Physical wavelengths grow with $a$, while the Hubble radius $c/H$ changes comparatively slowly in near-exponential expansion. A small region can be stretched until it encompasses the scales that later become our observable universe. If that region was causally connected before inflation, the horizon puzzle is alleviated. At the same time, increasing $aH$ suppresses $|\Omega_{\rm tot}-1|$.

{{FIG:inflation}}

The number of **e-folds** is

$$
N=\ln\frac{a_{\rm end}}{a_{\rm start}}=\int H\,dt.
$$

For constant $H$, $N=H\Delta t$. Sixty e-folds means a linear stretch by $e^{60}\sim10^{26}$, not by 60. The required number is model-dependent because reheating and the inflationary energy scale affect the mapping from today's scales back to inflation. “Exactly 60” is a useful estimate, not a universal constant.

### Extension — a scalar-field realization

A homogeneous scalar field with canonical kinetic energy has

$$
u_\phi=\frac12\dot\phi^2+V(\phi),
\qquad
P_\phi=\frac12\dot\phi^2-V(\phi),
$$

in units with $c=1$ and a suitably normalized field. If the potential dominates, $P_\phi\simeq-u_\phi$ and the field behaves approximately like a cosmological constant. Its equation of motion is

$$
\ddot\phi+3H\dot\phi+V_{,\phi}=0.
$$

The $3H\dot\phi$ term acts like friction. Under slow-roll conditions, define

$$
\epsilon_H=-\frac{\dot H}{H^2}<1,
\qquad
\epsilon_V\simeq\frac{M_{\rm Pl}^2}{2}\left(\frac{V_{,\phi}}{V}\right)^2,
$$

where the second expression uses the reduced Planck mass and the slow-roll approximation. Inflation ends when the accelerated-expansion condition fails. **Reheating** transfers energy from the inflationary sector into particles and radiation, connecting this episode to the hot Big Bang. The details are not known.

Quantum fluctuations of the field and metric can be stretched into classical-looking primordial perturbations. Many models predict nearly scale-invariant, nearly Gaussian, predominantly adiabatic fluctuations. A small departure from exact scale invariance is described by a spectral index $n_s$, with $n_s=1$ meaning exact scale invariance for the conventional scalar spectrum. Tensor fluctuations are possible, but their amplitude is model-dependent.

<div class="remark" markdown="1">
<span class="remark-head">What inflation does not say.</span> It is not an explosion into empty space. It does not mean every part of the entire universe must be exactly uniform. It does not prove what happened at a mathematical first instant. Nor is every inflationary model confirmed: the framework addresses important initial-condition problems, while particular potentials, reheating histories and primordial gravitational-wave signals remain under test.
</div>

## 12. Horizons: what can be seen, and what can be reached?

Three lengths are often confused because each is measured in billions of light-years.

1. **Hubble radius:** $R_H=c/H$, an instantaneous expansion scale.
2. **Particle horizon:** the greatest present proper distance from which light emitted in the earliest accessible past could have reached us.
3. **Cosmic event horizon:** the greatest present proper distance from which a signal emitted now could ever reach us in the future.

For a flat universe, the present particle-horizon distance and event-horizon distance are

$$
D_{\rm ph,0}=c\int_0^{t_0}\frac{dt}{a(t)}
=\frac{c}{H_0}\int_0^\infty\frac{dz}{E(z)},
$$

$$
D_{\rm eh,0}=c\int_{t_0}^{\infty}\frac{dt}{a(t)}
=\frac{c}{H_0}\int_{-1}^{0}\frac{dz}{E(z)},
$$

provided the integrals converge. In the second expression, $E(z)$ means the analytic continuation of the specified expansion model into the future. If the integral diverges, there is no finite event horizon of that type.

For the rounded matter-plus-Λ benchmark, $D_{\rm ph,0}$ is roughly $14\ \mathrm{Gpc}$, or $46\ \mathrm{Gly}$, while $D_{\rm eh,0}$ is roughly $4.9\ \mathrm{Gpc}$, or $16\ \mathrm{Gly}$. These values are model-dependent. The particle horizon is not $ct_0$: the distances between the emitting matter and us changed while the light was travelling.

### Three clean examples

- **Einstein–de Sitter:** $D_{\rm ph}=3ct=2c/H$. There is no finite future event horizon; given enough time, light can cross any fixed comoving separation.
- **Pure de Sitter with constant $H$:** a signal emitted now can reach us only if its present proper distance is below $c/H$. The Hubble radius and event horizon coincide in this special model.
- **Our approximate matter-plus-Λ model:** the Hubble radius, particle horizon and event horizon are all different. As Λ comes to dominate, the event horizon approaches an approximately constant proper size while the comoving horizon shrinks.

{{FIG:horizons}}

### Can we see galaxies receding faster than light?

Yes. The rate $HD$ is the change of a proper distance defined across a cosmic-time slice. It is not a locally measured speed past a nearby observer, so special relativity's local speed limit is not violated. Light always moves locally at $c$. Whether a photon reaches us depends on the entire future behaviour of the intervening expansion.

For an incoming radial light ray, its proper distance $D$ from us obeys

$$
\dot D=H D-c.
$$

If it begins outside the Hubble radius, $D$ can initially increase even though the photon is aimed toward us. If the comoving Hubble radius later grows enough, the photon can enter the region where $HD<c$ and then approach us. This is how a “Hubble crossing” can occur. The Hubble sphere is not a one-way visibility wall.

### Extension — conformal time makes light rays straight

Define conformal time by $d\eta=dt/a(t)$. The radial FLRW metric becomes

$$
ds^2=a^2(\eta)\left[-c^2d\eta^2+d\chi^2+S_k^2(\chi)d\Omega^2\right].
$$

Radial light obeys $d\chi=\pm c\,d\eta$, so it travels on straight 45-degree lines when the axes are $\chi$ and $c\eta$. The particle horizon is the amount of conformal time accumulated since the beginning; the event horizon is the amount remaining. This turns a difficult-sounding causal question into an area-under-a-curve question.

## 13. Measuring cosmology without fooling yourself

### The low-redshift Hubble diagram

At sufficiently low redshift, $cz\simeq H_0D$ after correcting to an appropriate cosmic reference frame. A galaxy's peculiar velocity adds scatter. For a line constrained through the origin, the least-squares slope is

$$
\widehat H_0=\frac{\sum_i D_i v_i}{\sum_iD_i^2},
\qquad
v_i\simeq cz_i.
$$

If the velocity uncertainties are unequal, use inverse-variance weights. Averaging the individual ratios $v_i/D_i$ is not the same estimator and can give very noisy nearby galaxies excessive influence. A real analysis also treats distance uncertainties, correlated peculiar motions, selection effects, reference-frame corrections and calibration errors.

{{LAB:hubble}}

### Expansion, acceleration and supernova magnitudes

For a smooth distance–redshift relation in a flat universe,

$$
D_C(z)=\frac{c}{H_0}\left[z-\frac{1+q_0}{2}z^2+O(z^3)\right],
$$

$$
d_L(z)=\frac{c}{H_0}\left[z+\frac{1-q_0}{2}z^2+O(z^3)\right].
$$

The second-order term contains the acceleration information. A single distant supernova cannot establish acceleration: one needs a calibrated population, a redshift baseline and a model for systematics. Relative supernova distances can constrain the shape of the expansion history even when the absolute value of $H_0$ is marginalized over.

A fractional distance error $\epsilon$ gives a magnitude shift

$$
\Delta\mu=5\log_{10}(1+\epsilon)
\simeq\frac{5}{\ln10}\epsilon.
$$

Thus a 1% distance-calibration error is about $0.0217$ mag. Small magnitude offsets matter. If all supernova absolute magnitudes are shifted by $\Delta M$, the inferred low-redshift Hubble constant changes according to

$$
\frac{H_{0,\rm fit}}{H_{0,\rm true}}=10^{\Delta M/5},
$$

with the sign defined as assumed minus true absolute magnitude. This is a calibration degeneracy, not evidence that the universe changes when we relabel a candle.

### What a “tension” means

Different measurements of $H_0$ can disagree more strongly than their quoted uncertainties would suggest. This is called the **Hubble tension**. It could indicate unrecognized systematics, a missing ingredient in the assumed model, or a combination of effects. It is not permission to declare any preferred value correct.

A useful comparison asks:

1. Are the measurements genuinely independent, or do they share a calibration?
2. Is the inferred quantity model-dependent?
3. Are uncertainties statistical, systematic, or correlated?
4. Does a proposed new model improve the full data set, or only the one discrepancy?
5. How many extra parameters were introduced to obtain the improvement?

The minimal ΛCDM model is remarkably economical and successful, but it is not a final theory. It does not identify the dark matter particle, explain the microscopic origin of Λ, or supply a tested quantum theory of the earliest epoch. Observations can also test whether the accelerating component evolves with time. A constant $w=-1$ is a benchmark hypothesis, not a logical necessity. This handout uses it because its consequences can be calculated cleanly.

### A compact chain of inference

| Observation | Directly measured | Inference requiring a framework |
|---|---|---|
| galaxy spectra | line wavelengths and shifts | expansion history after distances and peculiar motions are treated |
| supernovae | fluxes, colours, light curves | relative distances and acceleration |
| CMB | intensity, frequency spectrum, anisotropies | contents, geometry and primordial initial conditions |
| BBN spectra/abundances | light-element abundances | baryon density and early expansion conditions |
| galaxy clustering | positions, redshifts and shapes | growth, bias and the matter power spectrum |
| gravitational lenses | image positions, shapes and time delays | mass distribution and distance combinations |

## 14. The Olympiad problem-solving toolkit

### First decide what kind of quantity you have

- A **redshift** gives a ratio of scale factors.
- A **lookback time** requires an integral over expansion history.
- A **flux** calls for luminosity distance and bandpass care.
- An **angular size** calls for angular-diameter distance.
- A **causal limit** calls for a horizon integral, not just $c/H$.
- A **density comparison** needs the appropriate power of $1+z$.

Write the definition before substituting numbers. Most difficult cosmology problems become manageable when the correct distance or epoch is identified.

### A reliable five-step method

1. **Draw the events:** emission, observation, equality or acceleration. Mark $a$, $z$ and $t$ separately.
2. **Choose the model:** matter-only, radiation-only, flat matter-plus-Λ, constant $H$, or a supplied $H(z)$. State neglected components.
3. **Find the governing relation:** conservation, Friedmann, distance duality, a null path or a horizon integral.
4. **Check limits and dimensions:** $z\to0$, $a\to1$, $\Omega_\Lambda\to0$, equal densities, or a pure-component universe.
5. **Interpret the result:** is it a time, a present proper distance, an emission-time distance, or an observable angle? Explain what the number means.

### Essential results, with their conditions

| Result | Conditions / warning |
|---|---|
| $D=a\chi$ | flat geometry, comoving separation |
| $1+z=a_0/a_{\rm em}$ | smooth-background cosmological redshift |
| $E^2=\sum_i\Omega_{i0}(1+z)^{3(1+w_i)}+\Omega_{k0}(1+z)^2$ | FLRW; separate non-interacting constant-$w$ fluids |
| $u\propto a^{-3(1+w)}$ | local conservation, constant $w$, no energy exchange |
| $d_L=(1+z)^2d_A$ | photon conservation and metric propagation; not restricted to flat space |
| $t_0=2/(3H_0)$ | flat, matter-only throughout |
| $T=T_0(1+z)$ | freely cooled radiation / thermal CMB temperature |
| $D_{\rm ph}=3ct$ | Einstein–de Sitter, not ΛCDM at all times |
| $D_{\rm eh}=c/H$ | pure de Sitter with constant $H$, not every cosmology |

### Common mistakes that cost marks

- Treating $cz$ as a special-relativistic velocity at every redshift.
- Using today's CMB temperature in a last-scattering calculation.
- Forgetting the arrival-rate factor in luminosity distance.
- Comparing an emission-time ruler with a present-day angular-diameter distance.
- Saying matter–Λ equality is the start of acceleration.
- Assuming positive curvature forces recollapse even with Λ.
- Treating the Hubble radius as an absolute observational boundary.
- Calling the Big Bang an explosion from a point in space.
- Mixing mass density $\rho$ with energy density $u$.
- Applying a matter-only age formula to a radiation-era problem.
- Adding a cosmological-constant term twice, once as Λ and once as a fluid.
- Quoting five significant figures from two-significant-figure input data.

<div class="thm" markdown="1">
<span class="thm-head">A final physical picture.</span> Expansion changes the relation between coordinates and rulers. Light carries a record of that change. Gravity and pressure determine how the expansion rate evolves. The contents cool, decouple and cluster. Our observations are a past-light-cone view of that history, not a snapshot of the entire universe today. Keep those five sentences in mind and the formulas become a connected story rather than a list to memorize.
</div>

## 15. Sources, attribution and further exploration

The explanations, diagrams, simulations and original exercises in this handout were prepared for MAIS PAC. The problem set distinguishes **website-sourced adaptations**, **original IOAA-inspired challenges**, and **original club foundations**. Adaptations are not official IOAA questions, and the worked solutions are independent explanations, not official marking schemes.

### Website problem sources beyond the IOAA archive

- [University of Sheffield, PHY306: Introduction to Cosmology — Practice Problems](https://www.hep.shef.ac.uk/roszkowski/phy306/pdf/phy306_probs.pdf): distance definitions, systematic errors, fluid scaling, CMB and inflation. Problems 4 and 3 are adapted here; Problems 6, 13 and 43 provide further practice on the same concepts.
- [Yale University, ASTR 610: Problem Set 1](http://www.astro.yale.edu/vdbosch/astro610_problem_set1.pdf): Einstein–de Sitter cosmology, radiation equality, tired light and curved geometry. Problems 1–4 provide source material for several exercises.
- [MIT OpenCourseWare, 8.286 Fall 2013: Quiz 3 Review Problems](https://web.mit.edu/8.286/www/quiz13/q3rp-euf13.pdf): Problem 9 on flatness and Problem 10 on distance definitions at high redshift informed the extensions. The source's historical “most distant quasar” wording is not presented as a current record.
- [BAAO 2015 Round 2, Question 12](https://www.bpho.org.uk/baao/Papers/R2/BAAO_2015.pdf) and [official solutions](https://www.bpho.org.uk/baao/Papers/R2/BAAO_2015_solutions.pdf): a school-to-international-level redshift and expansion problem. Our version supplies its own assumptions and independently worked answers.

### IOAA connections, with direct materials

- [IOAA 2022, Theory 4, “Journey Between Galaxies”](https://olimpicos.net/files/ioaa/IOAA_2022_Q1-13.pdf): motion relative to an expanding background.
- [IOAA 2023, Theory 5, “Dark Energy”](https://olimpicos.net/files/ioaa/IOAA_2023_Q1-5.pdf): critical density, dark-energy density and matter–Λ equality.
- [IOAA 2024, Theory 5, “CMB”](https://olimpicos.net/files/ioaa/IOAA_2024_Q1-11.pdf): Wien scaling and an explicitly matter-dominated age estimate.
- [IOAA 2020, Team 14, “Spectral Distortions of the CMB”](https://olimpicos.net/files/ioaa/IOAA_2020_Q14.pdf): blackbody radiation and energy injection. Our simplified fixed-photon-number exercise is not the full thermalization problem.
- [IOAA 2025, Theory 10, “Big Bang Nucleosynthesis”](https://olimpicos.net/files/ioaa/IOAA_2025_Q1-12.pdf): the topic inspiration for the neutron-counting extension; the exercise here is independently constructed.
- [Official IOAA past-materials archive](https://ioaastrophysics.org/resources/problems-from-past-ioaa) and [searchable year-by-year collection](https://olimpicos.net/ioaa/).

For deeper study, use Barbara Ryden's *Introduction to Cosmology*, Steven Weinberg's *Cosmology*, and the public lecture notes of MIT 8.286. The first develops the physical picture; the later sources go further into relativity and perturbations. The purpose of the extension sections is to make those texts approachable—not to pretend that a short handout replaces them.
