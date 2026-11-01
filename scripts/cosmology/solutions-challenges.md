## Original Olympiad challenges: worked solutions and reasoning

<div class="remark" markdown="1">
<span class="remark-head">How to read these solutions.</span> Problems 21–30 are **new MAIS PAC exercises**, not official IOAA questions. Each identifies the past-material theme that inspired it. The “Idea” paragraph explains how to recognize the governing physics; the derivation supplies the calculation; the “Checks” paragraph tests the result. The solutions are independent and are not official IOAA marking schemes.
</div>

<div class="solution" id="s21" markdown="1">
<span class="sol-head">Solution 21 — A rocket against the Hubble flow.</span> [Return to problem →](06.01.html#p21)

**IOAA connection.** IOAA 2022 Theory 4 studies travel between galaxies while the background expands. This version adds a threshold, a new travel-time calculation and a limiting-case discussion.

**Idea.** The rocket's peculiar speed is measured locally, but the distance to the destination also grows. Write an equation for the **remaining proper distance**, rather than subtracting a constantly changing recession speed by hand. The supplied differential equation already contains both effects.

**(a)** Solve $\dot D-HD=-u$ using the integrating factor $e^{-Ht}$:

$$
\frac{d}{dt}(De^{-Ht})=-u e^{-Ht}.
$$

Integrating from zero to $t$ gives

$$
D(t)=\frac uH+\left(D_0-\frac uH\right)e^{Ht}.
$$

The destination itself is at $D_{\rm dest}=D_0e^{Ht}$. The rocket's actual proper position is $D_{\rm dest}-D(t)$; $D(t)$ in the solution is the remaining separation.

**(b)** If $u>HD_0$, the coefficient of $e^{Ht}$ is negative and the remaining separation eventually reaches zero. If $u<HD_0$, the expression instead reaches a minimum and then grows without bound. The threshold is

$$
u_{\rm th}=HD_0=70\times10=700\ \mathrm{km\,s^{-1}}.
$$

A $1000\ \mathrm{km\,s^{-1}}$ rocket **can** arrive under the idealized assumptions.

**(c)** Set $D(t)=0$:

$$
e^{Ht}=\frac{u}{u-HD_0},\qquad
t=\frac1H\ln\left(\frac{u}{u-HD_0}\right).
$$

For $u=1500$,

$$
t=\frac1H\ln\left(\frac{1500}{800}\right)
=0.6286H^{-1}=8.78\ \mathrm{Gyr}.
$$

**(d)** As $u\to(HD_0)^+$, the denominator approaches zero and the arrival time diverges. At equality the remaining distance approaches $D_0$ asymptotically rather than reaching zero. Just exceeding the threshold is not enough for a practically short journey.

**(e)** $D_0/u=6.98\ \mathrm{Gyr}$ ignores the increasing separation. It is recovered only in the limit $H\to0$. Constant $H$ is an exact de Sitter-like idealization, whereas the real expansion rate changes with the cosmic contents; local gravity, fuel and relativistic trajectory details are also neglected.

**Checks.** For $u\gg HD_0$, expand the logarithm to obtain $t\simeq D_0/u$. At $u=HD_0$, the formula correctly signals no finite arrival time. A negative time would indicate that the wrong branch or the wrong sign was used.

**Why this is hard.** The phrase “constant speed” refers to a local peculiar speed, not a constant rate of change of the remaining distance. Separating those two ideas is the whole problem.
</div>

<div class="solution" id="s22" markdown="1">
<span class="sol-head">Solution 22 — Weighing dark energy, then asking when it wins.</span> [Return to problem →](06.01.html#p22)

**IOAA connection.** The density-budget and equality calculation is inspired by IOAA 2023 Theory 5. The pressure and acceleration parts are new conceptual extensions.

**Idea.** Flatness fixes the total density. Subtract matter to find Λ, then use the different redshift scalings. Equality compares densities; acceleration compares the gravitational source $\rho+3P/c^2$.

**(a)** The critical density is $9.2039\times10^{-27}\ \mathrm{kg\,m^{-3}}$. Therefore

$$
\rho_\Lambda=\rho_{\rm crit}-\rho_{m0}=6.404\times10^{-27}\ \mathrm{kg\,m^{-3}},
$$

$$
u_\Lambda=\rho_\Lambda c^2=5.76\times10^{-10}\ \mathrm{J\,m^{-3}}.
$$

**(b)** $\Omega_{m0}=2.8/9.2039=0.304$, and $\Omega_{\Lambda0}=0.696$. These are close to, but not exactly, the rounded $(0.3,0.7)$ benchmark.

**(c)** Equality:

$$
1+z_{m\Lambda}=(\rho_\Lambda/\rho_{m0})^{1/3}=1.318,
\qquad z_{m\Lambda}=0.318.
$$

Acceleration begins when $\rho_m=2\rho_\Lambda$, so

$$
1+z_{\rm acc}=(2\rho_\Lambda/\rho_{m0})^{1/3}=1.660,
\qquad z_{\rm acc}=0.660.
$$

**(d)**

$$
q_0=\frac12\Omega_{m0}-\Omega_{\Lambda0}=-0.544.
$$

**(e)** A homogeneous cosmological component has no spatial pressure gradient, so there is no ordinary pressure-gradient force of the kind the student imagines. In general relativity, pressure itself contributes to the gravitational source. For Λ, $\rho_\Lambda+3P_\Lambda/c^2=-2\rho_\Lambda$, giving an accelerating contribution.

**Checks.** The two densities sum to the critical density. The acceleration redshift exceeds the equality redshift by the factor $2^{1/3}$ in $1+z$. The negative value of $q_0$ agrees with the stated accelerating universe.

**Why this is hard.** The same symbol ρ appears in two different equations with different weights. Keeping the bookkeeping explicit prevents the common “equal densities means acceleration starts” error.
</div>

<div class="solution" id="s23" markdown="1">
<span class="sol-head">Solution 23 — A warm spectrum and a deliberately wrong clock.</span> [Return to problem →](06.01.html#p23)

**IOAA connection.** IOAA 2024 Theory 5 combines a CMB wavelength shift with an explicitly matter-dominated age estimate. This version uses a different wavelength and asks why the assumption matters.

**Idea.** The spectrum gives a temperature ratio, hence a scale-factor ratio. The age requires a separate cosmological model. Do not let a successful temperature calculation smuggle in an unjustified expansion history.

**(a)**

$$
T=\frac{2.898\times10^{-3}}{5.00\times10^{-4}}=5.796\ \mathrm K,
$$

$$
1+z=\frac{T}{T_0}=2.1268,
\qquad z=1.127,
\qquad a=0.470.
$$

**(b)** In the stipulated matter-only model, $H=H_0(1+z)^{3/2}$ and

$$
t(z)=\frac{2}{3H_0}(1+z)^{-3/2}
=9.312(2.1268)^{-3/2}\ \mathrm{Gyr}
\simeq3.00\ \mathrm{Gyr}.
$$

**(c)** At $z\simeq1.13$, Λ is dynamically important in the benchmark model. Ignoring it changes the inferred age substantially: the flat $(0.3,0.7)$ model with the same $H_0$ gives about **5.28 Gyr** at this redshift. Radiation is not the dominant missing ingredient here; Λ is. At much higher redshift, radiation would also need to be included.

**(d)** A pure radial Doppler interpretation gives

$$
\beta=\frac{(2.1268)^2-1}{(2.1268)^2+1}=0.638.
$$

The CMB's near-isotropy, blackbody spectrum, relation to the hot early universe and consistency with other cosmological probes support cosmological expansion, not a shell of material moving away from us at that local speed. Our actual peculiar motion produces a much smaller dipole pattern.

**Checks.** The temperature is only about twice today's value, so this is a low-redshift CMB exercise, not last scattering. The age is smaller than the model's present age. The matter-only answer is correct **for the supplied toy model**, even though it is not a realistic precision estimate.

**Why this is hard.** Olympiad questions sometimes impose an approximation that is not physically exact. The right response is to use it where requested, then identify its domain of validity—not silently replace the question with a different model.
</div>

<div class="solution" id="s24" markdown="1">
<span class="sol-head">Solution 24 — A small scar on a blackbody.</span> [Return to problem →](06.01.html#p24)

**IOAA connection.** IOAA 2020 Team 14 investigates CMB spectral distortions. This exercise isolates one small piece of that physics: an energy budget at fixed photon number. It does not reproduce the official problem or model the full reaction network.

**Idea.** A chemical potential changes both number and energy at fixed temperature. But the problem fixes photon number, so the temperature must adjust. Include that adjustment before relating the injected energy to μ.

**(a)** Let $\tau=\Delta T/T_i$. To first order,

$$
\frac{N_f}{N_i}\simeq1+3\tau-1.368\mu.
$$

Fixed photon number gives $\tau=(1.368/3)\mu=0.456\mu$. For energy,

$$
\frac{u_f}{u_i}\simeq1+4\tau-1.111\mu.
$$

Therefore the injected fractional energy is

$$
\epsilon=(4\times0.456-1.111)\mu=0.713\mu,
\qquad
\boxed{\mu\simeq1.40\epsilon}.
$$

The coefficients 1.368 and 1.111 are the small-μ expansions of the photon-number and energy integrals; they were supplied so that no advanced integration is required.

**(b)** For $\epsilon=10^{-5}$,

$$
\mu\simeq1.40\times10^{-5},
\qquad
\frac{\Delta T}{T_i}=0.456\mu\simeq6.40\times10^{-6}.
$$

The final temperature is slightly higher, while the positive chemical potential suppresses the low-frequency occupation relative to a blackbody at that final temperature.

**(c)** Holding $N$ fixed determines the temperature adjustment. Holding $T$ fixed as well would leave no freedom to satisfy both conservation and the added energy. The three requirements would generally be incompatible.

**(d)** If photon-producing reactions are efficient, the chemical potential can relax toward zero by creating photons. The final spectrum may remain nearly Planckian despite energy injection. The relevant outcome depends on the competition between injection and thermalization rates, so a fixed-$N$ estimate is not valid at arbitrary early times.

**Checks.** Positive injected energy gives positive μ and a positive temperature adjustment in this model. The result is first order in tiny quantities; products such as $\mu\tau$ have been neglected.

**Why this is hard.** The tempting one-line answer uses the energy distortion at fixed temperature and forgets the constraint. Writing the two linearized conservation equations makes the hidden degree of freedom visible.
</div>

<div class="solution" id="s25" markdown="1">
<span class="sol-head">Solution 25 — Counting neutrons into helium.</span> [Return to problem →](06.01.html#p25)

**IOAA connection.** The topic is inspired by IOAA 2025 Theory 10 on BBN. The numerical delay and assumptions here define a new, standalone counting problem.

**Idea.** Follow neutrons until they are locked into nuclei. A helium-4 nucleus contains two neutrons and two protons, so a neutron fraction is not the same as a helium mass fraction.

**(a)** With only radioactive decay during the delay,

$$
r=r_0e^{-\Delta t/\tau_n}=\frac16e^{-200/880}=0.1328.
$$

**(b)** Take $n_p=1$ and $n_n=r$. All neutrons form $n_{\rm He}=r/2$ helium nuclei, consuming $r$ protons. The remaining hydrogen count is $1-r$. The helium mass fraction is

$$
Y_p=\frac{4(r/2)}{(1-r)+4(r/2)}=\frac{2r}{1+r}=0.234.
$$

Thus about **23.4%** of the baryonic mass is helium-4 in this simplified model.

**(c)**

$$
\frac{n_{\rm He}}{n_{\rm H}}=\frac{r/2}{1-r}=\frac{r}{2(1-r)}=0.0764.
$$

Equivalently, there is roughly one helium nucleus per 13.1 hydrogen nuclei. The intermediate ratio $r/2=0.0664$ is helium nuclei per **initial** proton count, not per remaining hydrogen nucleus; the distinction matters.

**(d)** $r/(1+r)$ is the fraction of baryon **number** in neutrons. Helium mass counts four nucleons per nucleus, including the protons bound with those neutrons. Counting nuclei, nucleons and mass are three different operations.

**(e)** A higher baryon density generally lets deuterium survive and nucleosynthesis proceed earlier, leaving less time for neutron decay and tending to increase the helium yield. The real calculation also includes expansion, weak freeze-out, nuclear reaction rates, the photon-to-baryon ratio and the destruction and production of several light nuclides.

**Checks.** As $r\to0$, $Y_p\to0$. If $r=1$, all nucleons can be placed in helium and $Y_p=1$. The answer lies between zero and one, as a mass fraction must.

**Why this is hard.** The physics is mostly bookkeeping, but the bookkeeping changes when neutrons become bound. Drawing a small ledger of protons, neutrons, helium nuclei and hydrogen nuclei is more reliable than memorizing a fraction.
</div>

<div class="solution" id="s26" markdown="1">
<span class="sol-head">Solution 26 — A hidden magnitude error.</span> [Return to problem →](06.01.html#p26)

**IOAA connection.** This original data exercise develops the distance-ladder and standard-candle reasoning that appears across IOAA materials. It is not a reproduction of a particular official data-analysis question.

**Idea.** A magnitude error is a logarithmic distance error. Propagate it through the distance modulus, then through the low-redshift relation $H_0\simeq cz/d$.

**(a)** The inferred distance modulus is too large by 0.050 mag, because $\mu=m-M$ and the assumed $M$ is more negative. Since $\mu=5\log_{10}(d_L/10\ \mathrm{pc})$,

$$
\frac{d_{\rm assumed}}{d_{\rm true}}=10^{+0.050/5}=10^{+0.01}=1.02329.
$$

Distances are overestimated by **2.33%**. An assumed candle that is intrinsically brighter than reality must be placed farther away to explain a given flux.

**(b)** At fixed measured redshift, $H_0\propto1/d$, so

$$
\frac{H_{\rm assumed}}{H_{\rm true}}=10^{-0.01}=0.97724.
$$

The Hubble constant is underestimated by **2.28%**. The two percentages differ slightly because they use different denominators.

**(c)**

$$
H_{\rm corrected}=70.0\times10^{+0.01}=71.6\ \mathrm{km\,s^{-1}\,Mpc^{-1}}.
$$

**(d)** A constant magnitude offset multiplies all inferred distances by the same factor. It changes the normalization but not the shape of the relative distance–redshift relation. Acceleration is inferred from curvature in that relation, so the shape can remain informative after marginalizing over the unknown absolute calibration.

**(e)** No. A redshift-dependent error changes the shape and can mimic or hide acceleration. That is why population evolution, dust, selection and filter corrections are not interchangeable with a single harmless zero-point offset.

**Checks.** The sign passes a physical test: brighter assumed candles imply larger distances and a smaller inferred $H_0$. The correction raises, rather than lowers, the biased value.

**Why this is hard.** It is easy to lose the sign in a logarithm. Reconstructing the physical candle argument provides an independent check on the algebra.
</div>

<div class="solution" id="s27" markdown="1">
<span class="sol-head">Solution 27 — One ruler, two expansion measurements.</span> [Return to problem →](06.01.html#p27)

**IOAA connection.** This original problem combines angular, radial and distance-duality reasoning in the style of IOAA multi-part questions. No official BAO dataset is reproduced.

**Idea.** The same comoving length is viewed across the sky in one measurement and along the line of sight in the other. The transverse observation gives a distance; the radial observation gives an expansion rate.

**(a)**

$$
D_M=\frac{r_d}{\theta}=\frac{147}{0.0300}=4900\ \mathrm{Mpc}=4.90\ \mathrm{Gpc}.
$$

**(b)** A radial proper separation at that epoch is $r_d/(1+z)$, and $dD\simeq c\,dz/H(z)$. Equivalently, the comoving interval is $c\,dz/H$. Thus

$$
H(z)=\frac{c\Delta z}{r_d}
=\frac{299792.458(0.0450)}{147}
=91.8\ \mathrm{km\,s^{-1}\,Mpc^{-1}}.
$$

**(c)** At $1+z=1.5$,

$$
d_A=\frac{4900}{1.5}=3267\ \mathrm{Mpc},
\qquad
d_L=4900(1.5)=7350\ \mathrm{Mpc}.
$$

**(d)** The transverse distance is proportional to the assumed ruler, $D_M=r_d/\theta$, so a 2% increase in $r_d$ increases $D_M$ by 2%. The radial result is inversely proportional to it, $H=c\Delta z/r_d$, so the same increase decreases $H$ by the factor $1/1.02$ (about 1.96%). The measured angle and redshift interval themselves do not change.

**(e)** Different dark-energy models can produce similar distances and expansion rates over a limited redshift range, especially after other parameters are adjusted. One needs a broader redshift baseline, complementary probes and a growth/geometry comparison to distinguish explanations. A ruler measurement does not directly identify a microscopic field or vacuum mechanism.

**Checks.** $H(0.5)$ is larger than the benchmark $H_0$, as expected. $d_A<D_M<d_L$ at positive redshift. The radial result would be absurdly small if the supplied interval were off by a large factor; checking the expected scale is part of the solution.

**Why this is hard.** The factor $1+z$ is already accounted for when $r_d$ is treated as a comoving ruler. Adding it again is a common error. Start from a proper or comoving interval and stay in that convention.
</div>

<div class="solution" id="s28" markdown="1">
<span class="sol-head">Solution 28 — Designing a curvature experiment.</span> [Return to problem →](06.01.html#p28)

**IOAA connection.** An original geometric-estimation problem in the Olympiad tradition, extending the Yale curved-space exercise. It tests whether a proposed measurement is actually sensitive enough.

**Idea.** Curvature appears through the dimensionless ratio $r/R_c$. Use the first correction to the circumference, then compare the predicted signal with the stated measurement precision.

**(a)** For a positively curved space,

$$
C\simeq2\pi r\left(1-\frac{r^2}{6R_c^2}\right).
$$

The deficit is

$$
\Delta C=\frac{\pi r^3}{3R_c^2}
=\frac{\pi(2.00)^3}{3(20.0)^2}\ \mathrm{Gpc}
=0.0209\ \mathrm{Gpc}=20.9\ \mathrm{Mpc}.
$$

**(b)**

$$
\frac{\Delta C}{2\pi r}=\frac{r^2}{6R_c^2}
=\frac{4}{2400}=1.67\times10^{-3}=0.167\%.
$$

**(c)** No. A 1% fractional measurement is much coarser than a 0.167% signal. The enormous absolute deficit in megaparsecs is irrelevant if the circumference itself cannot be measured accurately enough.

**(d)** Examples: constructing a common cosmic-time slice across gigaparsecs; measuring geodesic distances rather than observables such as redshift and angle; peculiar velocities, evolution, lensing and selection effects; and the limited number of independent large-scale modes. Any real analysis must specify a model connecting these observables to spatial curvature.

**(e)** A small or undetected curvature could mean a curvature radius much larger than the surveyed region. It could also be compatible with different global topologies. Local geometry constrains, but does not by itself determine, the universe's total size or topology.

**Checks.** The fractional signal scales as $(r/R_c)^2$. Doubling the survey radius quadruples the leading sensitivity. The expansion of the sine is valid here because $r/R_c=0.1$.

**Why this is hard.** The problem asks for an experimental conclusion, not only a formula. Comparing signal to fractional uncertainty is the decisive step.
</div>

<div class="solution" id="s29" markdown="1">
<span class="sol-head">Solution 29 — The last message that can arrive.</span> [Return to problem →](06.01.html#p29)

**IOAA connection.** This new problem turns the expanding-background reasoning of IOAA 2022 Theory 4 into a null-propagation and event-horizon question.

**Idea.** For an incoming photon, the proper distance changes through two terms: expansion increases it at $HD$, while light reduces it at $c$. Solve $\dot D=HD-c$ with the initial condition, then ask whether the solution ever reaches zero.

**(a)** The solution is

$$
D(t)=\frac cH+\left(D_0-\frac cH\right)e^{Ht}.
$$

**(b)** A finite arrival requires $D_0<c/H$. The limiting present proper distance is

$$
D_{\rm eh}=\frac cH=4.283\ \mathrm{Gpc}=13.97\ \mathrm{Gly}.
$$

This is the event horizon for signals emitted **now** in the stipulated constant-$H$ future.

**(c)** Setting $D(t)=0$ gives

$$
t_{\rm arr}=-\frac1H\ln\left(1-\frac{HD_0}{c}\right).
$$

For $D_0=0.8c/H$,

$$
t_{\rm arr}=\frac{\ln5}{H}=1.609H^{-1}=22.48\ \mathrm{Gyr}.
$$

**(d)** At exactly $D_0=c/H$, $D(t)=c/H$ for all finite $t$. The photon remains at the horizon and never reaches us at a finite arrival time. It is the limiting boundary between arriving and non-arriving signals.

**(e)** The particle horizon concerns signals emitted in the past that arrive now. The event horizon concerns signals emitted now that may arrive in the future. Objects whose old light we see today can now be much farther away than the current event horizon; seeing their past does not mean a message sent now will reach us.

**Checks.** As $D_0\to0$, $t_{\rm arr}\simeq D_0/c$. As $D_0\to(c/H)^-$, the arrival time diverges. Both limits agree with physical intuition.

**Why this is hard.** “Can we see it?” and “can it signal us now?” refer to different emission events and different integrals. A spacetime sketch prevents the two questions from being merged.
</div>

<div class="solution" id="s30" markdown="1">
<span class="sol-head">Solution 30 — How much inflation is enough?</span> [Return to problem →](06.01.html#p30)

**IOAA connection.** An original enrichment problem inspired by early-universe themes in IOAA materials and the cited Sheffield/MIT exercises. The later growth factor is deliberately supplied, so no hidden thermal-history model is required.

**Idea.** During inflation, $H$ is nearly constant while $a$ grows exponentially. The curvature deviation is proportional to $(aH)^{-2}$, so it is exponentially suppressed. After inflation, ordinary decelerating evolution partly restores that deviation.

**(a)**

$$
\frac{|\Omega_{\rm tot}-1|_{\rm end}}{|\Omega_{\rm tot}-1|_{\rm start}}
=e^{-2N}.
$$

**(b)** Starting from order unity and requiring a final value below $10^{-5}$ immediately after inflation gives

$$
e^{-2N}<10^{-5}
\quad\Rightarrow\quad
N>\frac12\ln(10^5)=11.51.
$$

Thus **12 e-folds** suffice for this isolated flatness requirement if an integer count is requested.

**(c)** The later evolution multiplies the deviation by $10^{26}$. The present requirement is

$$
10^{26}e^{-2N}<10^{-5}
\quad\Rightarrow\quad
N>\frac12\ln(10^{31})=71.38.
$$

Thus **72 e-folds** are required under the supplied estimate.

**(d)** The first bound ignores the long later interval during which the comoving Hubble radius grows. The second includes it. The actual required number depends on the inflationary energy scale, the reheating history, the expansion history and the precise scale whose causal origin is being matched. These are bounds in a simplified model, not a measurement of how many e-folds nature produced.

**(e)** A shrinking comoving Hubble radius lets a region that was initially causally connected expand to encompass the scales that later re-enter our horizon. This addresses the horizon problem. Quantum fluctuations are stretched as well, so inflation generically leaves small perturbations rather than perfect smoothness; those perturbations are essential seeds for later structure.

**Checks.** More e-folds make the universe flatter, not more curved. The later growth requirement increases the required $N$. The factor is $e^{-2N}$, not $e^{-N}$, because curvature appears divided by $(aH)^2$.

**Why this is hard.** The calculation is short once the correct variable is identified. The challenge is to distinguish the curvature constant, the curvature density parameter and the observable fractional deviation, and to keep the post-inflationary history in the budget.
</div>

## Final review: the ideas worth retaining

1. **Expansion is a changing relation between coordinates and proper distances.** It is not an explosion from a central point.
2. **Redshift is a ratio of scale factors.** Velocity, lookback time and distance require additional definitions.
3. **Gravity responds to pressure as well as energy density.** This is why radiation and Λ behave so differently.
4. **The CMB is a thermal record, not merely a faint glow.** Its spectrum, anisotropies and relation to light elements test different parts of the same history.
5. **Horizons are integrals over causal paths.** The Hubble radius is not a universal boundary.
6. **A difficult solution should end with checks.** Limits, units, signs and alternative derivations are how you know that the algebra describes the intended universe.

Return to the [Lecture + Problems](06.01.html), repeat a challenge without looking at the derivation, and try to explain the result to another student in ordinary language.
