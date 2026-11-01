## Foundations: worked solutions

<div class="solution" id="s1" markdown="1">
<span class="sol-head">Solution 1 — A rate disguised as a velocity.</span> [Return to problem →](06.01.html#p1)

**Idea.** A kilometre per second per megaparsec is a fractional rate. Convert the megaparsec to kilometres; the kilometres then cancel.

**(a)**

$$
H_0=\frac{70}{3.0856776\times10^{19}}\ \mathrm{s^{-1}}
=2.26855\times10^{-18}\ \mathrm{s^{-1}},
$$

$$
H_0^{-1}=4.40811\times10^{17}\ \mathrm s=13.97\ \mathrm{Gyr}.
$$

**(b)** $c/H_0=4282.75\ \mathrm{Mpc}=4.283\ \mathrm{Gpc}$. Since one parsec is $3.26156$ light-years, this is $13.97\ \mathrm{Gly}$. The equality of the numerical values in Gyr and Gly is a consequence of using light-travel units, not a new physical law.

**(c)** An object moving at constant speed has travel time $D/v$. If the expansion speed of a fixed pair had always been related to its separation through a constant $H$, then $D\propto e^{Ht}$ and there would be no finite time at which $D=0$. The exact coasting example is the empty, negatively curved Milne model, $a\propto t$, for which $t_0=H_0^{-1}$. The often-quoted “constant-speed since zero separation” picture gives the same scaling, but it is not a general solution of the Friedmann equation. In a matter-only flat model, for example, $t_0=2/(3H_0)$. **The age requires the history of $H$, not only its present value.**

**(d)**

$$
\rho_{\rm crit,0}=\frac{3H_0^2}{8\pi G}=9.20\times10^{-27}\ \mathrm{kg\,m^{-3}},
\qquad
\bar\rho_{m0}=0.3\rho_{\rm crit,0}=2.76\times10^{-27}\ \mathrm{kg\,m^{-3}}.
$$

**Checks.** $H_0$ has dimensions $T^{-1}$; multiplying it by a distance gives a speed. The mean matter density includes dark matter and is not a proton count.
</div>

<div class="solution" id="s2" markdown="1">
<span class="sol-head">Solution 2 — When does a galaxy trace the Hubble flow?</span> [Return to problem →](06.01.html#p2)

**(a)** $v_H=H_0D=140\ \mathrm{km\,s^{-1}}$. The peculiar contribution can be as large as $300/140=2.14$, or **214%** of the Hubble signal. The observed line-of-sight velocity could even have the opposite sign.

**(b)** Require $300/(H_0D)\le0.05$. The most conservative choice is the smallest $H_0$ allowed in the question. Here $H_0$ is fixed at 70, so

$$
D\ge\frac{300}{0.05\times70}=85.7\ \mathrm{Mpc}.
$$

**(c)** The measured velocity is approximately $H_0D+v_{\rm pec,los}$. Andromeda's negative total line-of-sight shift is compatible with a negative local peculiar velocity in the Milky Way–Andromeda system. The smooth Hubble flow is not a rule that every nearby object must recede from every other nearby object.

**(d)** Independent random velocities partly cancel in an average, with a statistical error that typically decreases as the sample grows. A shared bulk flow is correlated: every galaxy receives a similar offset, so averaging does not remove it. One needs a model, an appropriate reference-frame correction and an estimate of correlated uncertainties.

**Check.** A fractional-error requirement must be applied to the signal, not to the sum after the unknown peculiar velocity has already been added.
</div>

<div class="solution" id="s3" markdown="1">
<span class="sol-head">Solution 3 — One redshift, three different questions.</span> [Return to problem →](06.01.html#p3)

**(a)** The wavelength ratio is exactly three, so $1+z=3$, $z=2$, and $a_{\rm em}=1/3$.

**(b)** Every source-frame time interval is stretched by $1+z$. The feature lasts **60 days** in the observer's frame.

**(c)** For a pure radial special-relativistic Doppler interpretation,

$$
\beta=\frac{(1+z)^2-1}{(1+z)^2+1}=\frac{9-1}{9+1}=0.800.
$$

Thus the inferred local speed would be $0.800c$.

**(d)** That calculation compares two inertial frames in flat spacetime. A cosmological redshift compares two scale factors at separated emission and observation events. The proper-distance recession rate is $H(t)D(t)$ on a specified cosmic-time slice. It can be assigned today or at emission, and neither assignment is generally the same as the special-relativistic velocity constructed from $z$.

**Checks.** At low redshift all reasonable velocity definitions agree to first order. At $z=2$ they do not. The duration shift follows from the same crest-spacing argument as the wavelength shift.
</div>

<div class="solution" id="s4" markdown="1">
<span class="sol-head">Solution 4 — The ruler that did not stretch.</span> [Return to problem →](06.01.html#p4)

**(a)** With $a_0=1$, the comoving separation is $12{,}000\ \mathrm{Mpc}$. At $z=2$, $a=1/3$, so

$$
D_{\rm em}=aD_0=4000\ \mathrm{Mpc}=4.00\ \mathrm{Gpc}.
$$

**(b)** The proper separation grew by a factor of three. The comoving separation did not change.

**(c)** No. A bound group is not a pair of free comoving test particles. Its internal dynamics and local gravity determine its size; a metre ruler is held together by electromagnetic forces. Cosmological expansion is not a universal stretching command applied to every object.

**(d)** The benchmark gives $E(2)=\sqrt{0.3(3)^3+0.7}=\sqrt{8.8}=2.966$. Hence

$$
\frac{H(2)D_{\rm em}}{c}
=\frac{70(2.966)(4000)}{299792.458}
\simeq2.77.
$$

This is a rate of change of a large proper separation, not a local passage speed. Each galaxy can be locally at rest in its own comoving frame. No material object or signal overtakes a nearby light ray.

**Check.** The same result follows from $H_0D_0E(2)/(1+z)$. Keeping the factor $1+z$ in the denominator is essential: the separation at emission was smaller.
</div>

<div class="solution" id="s5" markdown="1">
<span class="sol-head">Solution 5 — Critical does not mean heavy.</span> [Return to problem →](06.01.html#p5)

**(a)** For zero curvature, and including Λ as one of the energy components, $H^2=8\pi G\rho_{\rm tot}/3$. Solving for the total mass-equivalent density gives the stated result. “Critical” refers to this total, not to matter alone.

**(b)** Multiply by $c^2$ with $c$ in metres per second:

$$
u_{\rm crit}=9.2039\times10^{-27}(2.99792458\times10^8)^2
=8.27\times10^{-10}\ \mathrm{J\,m^{-3}}.
$$

**(c)** $9.2039\times10^{-27}/1.67\times10^{-27}=5.51$ proton masses per cubic metre.

**(d)** Much of the cosmic energy budget is dark energy and nonbaryonic dark matter. Even the baryonic matter is not all free protons. This is an equivalent mass-density comparison, not a census of particles.

**Common unit trap.** Using $c=299792.458$ as though it were in metres per second makes the energy density wrong by $10^6$.
</div>

<div class="solution" id="s6" markdown="1">
<span class="sol-head">Solution 6 — A thermodynamic derivation of three eras.</span> [Return to problem →](06.01.html#p6)

**(a)** Expand $d(uV)=-P\,dV$:

$$
V\,du+(u+P)dV=0,
\qquad
\frac{dV}{V}=3\frac{da}{a}.
$$

Therefore $du/u=-3(1+w)da/a$, giving

$$
u(a)=u_0a^{-3(1+w)}.
$$

**(b)** Matter: $w=0$, so $\rho_m\propto a^{-3}$. Radiation: $w=1/3$, so $u_r\propto a^{-4}$. Λ: $w=-1$, so $u_\Lambda$ is constant.

**(c)** At $1+z=4$, the ratios are **64, 256 and 1**, respectively.

**(d)** Photon number per comoving volume is fixed in the ideal freely streaming case, so number density contributes $a^{-3}$. Each photon's energy is proportional to frequency and therefore to $a^{-1}$. The product is $a^{-4}$.

**(e)** The acceleration source is $u+3P=u(1+3w)$. For positive energy density, acceleration requires **$w<-1/3$**. At equality $w=-1/3$, the dominant component gives coasting expansion in a flat model.

**Checks.** Set $w=0$: the total mass in a comoving volume is constant. Set $w=-1$: the energy density is constant, so the energy in an increasing physical volume increases. That is allowed in the gravitational setting and is not a recipe for a perpetual-motion machine.
</div>

<div class="solution" id="s7" markdown="1">
<span class="sol-head">Solution 7 — The CMB was once warm.</span> [Return to problem →](06.01.html#p7)

**(a)**

$$
T_{\rm ls}=2.725(1091)=2973\ \mathrm K,
\qquad
\lambda_{\rm max}=\frac{2.89777\times10^{-3}}{2973}
=9.75\times10^{-7}\ \mathrm m=0.975\ \mu\mathrm m.
$$

**(b)** Because $u_\gamma\propto T^4\propto(1+z)^4$,

$$
u_{\gamma,\rm ls}=4.17\times10^{-14}(1091)^4
=5.91\times10^{-2}\ \mathrm{J\,m^{-3}}.
$$

**(c)** Every freely propagating photon's wavelength has increased by **1091**. Its individual energy has decreased by the same factor.

**(d)** The emitting plasma was hot. The present temperature is the result of subsequent expansion. The last-scattering surface labels where and when photons last scattered; it is not a cold material boundary surrounding us.

**(e)** $B_\nu$ and $B_\lambda$ are densities per unit frequency and per unit wavelength. They are related by $|d\nu/d\lambda|=c/\lambda^2$, which changes the location of the maximum. The temperature is unique; the numerical wavelength at “the peak” depends on the representation.

**Check.** Multiplying $0.975\ \mu\mathrm m$ by 1091 gives approximately $1.064\ \mathrm{mm}$, the present $B_\lambda$ peak.
</div>

<div class="solution" id="s8" markdown="1">
<span class="sol-head">Solution 8 — Equality is not acceleration.</span> [Return to problem →](06.01.html#p8)

**(a)** Equality requires $\Omega_{m0}(1+z)^3=\Omega_{\Lambda0}$, so

$$
z_{m\Lambda}=(0.7/0.3)^{1/3}-1=0.326.
$$

**(b)** For Λ, $\rho_\Lambda+3P_\Lambda/c^2=-2\rho_\Lambda$. The total acceleration source vanishes when $\rho_m=2\rho_\Lambda$:

$$
z_{\rm acc}=(2\times0.7/0.3)^{1/3}-1=0.671.
$$

**(c)** The acceleration transition occurs earlier, at larger redshift. Λ need only reach half the matter density to cancel the matter term in the acceleration equation; it must reach the full matter density for equality.

**(d)** $q_0=\Omega_{m0}/2-\Omega_{\Lambda0}=0.15-0.70=-0.55$.

**(e)** Yes. Acceleration means $\ddot a>0$, or $q<0$, which gives $\dot H/H^2>-1$. Thus $\dot H$ can be negative while remaining less negative than $-H^2$. In the benchmark $\dot H=-H^2(1+q)=-0.45H^2<0$, while $\ddot a/a=0.55H^2>0$.

**Check.** Do not identify a decreasing expansion rate $H$ with a decreasing recession speed for every fixed comoving pair. Their separation is also growing.
</div>

<div class="solution" id="s9" markdown="1">
<span class="sol-head">Solution 9 — A standard candle and a standard ruler.</span> [Return to problem →](06.01.html#p9)

**(a)** At $z=1$,

$$
d_L=2D_C=6.60\ \mathrm{Gpc},\qquad
d_A=D_C/2=1.65\ \mathrm{Gpc}.
$$

The emission-time proper distance is also $D_C/2=1.65\ \mathrm{Gpc}$ in this flat model. Equality of $d_A$ and emission-time proper distance follows from the definition of $d_A$, not from an accidental numerical coincidence.

**(b)** Convert $6.60\ \mathrm{Gpc}=2.037\times10^{26}\ \mathrm m$. Then

$$
F=\frac{4.00\times10^{36}}{4\pi(2.037\times10^{26})^2}
=7.67\times10^{-18}\ \mathrm{W\,m^{-2}}.
$$

**(c)**

$$
\theta=\frac{20.0\ \mathrm{kpc}}{1.65\times10^6\ \mathrm{kpc}}
=1.212\times10^{-5}\ \mathrm{rad}=2.50\ \mathrm{arcsec}.
$$

**(d)** $d_L/d_A=6.60/1.65=4=(1+z)^2$.

**(e)** Examples: a finite observed filter samples a different rest-frame wavelength interval, requiring a K-correction; dust or source evolution can alter the inferred luminosity. Detector calibration, lensing and the source's spectral shape can also matter.

**Check.** The flux uses luminosity distance; the angle uses angular-diameter distance. Using one in place of the other produces a factor-of-four error in flux at this redshift.
</div>

<div class="solution" id="s10" markdown="1">
<span class="sol-head">Solution 10 — The age is an integral.</span> [Return to problem →](06.01.html#p10)

**(a)** For matter only, $H=H_0a^{-3/2}$, so

$$
t_0=\int_0^1\frac{da}{aH}=\frac1{H_0}\int_0^1a^{-1/2}da=\frac2{3H_0}=9.31\ \mathrm{Gyr}.
$$

**(b)** For the flat matter-plus-Λ model,

$$
t_0=\frac1{H_0}\int_0^1\frac{da}{\sqrt{0.3/a+0.7a^2}}
=\frac{2}{3H_0\sqrt{0.7}}\operatorname{arsinh}\sqrt{\frac{0.7}{0.3}}.
$$

The result is **13.47 Gyr**. To obtain the closed form, substitute $u=a^{3/2}$; the integral becomes proportional to $\int du/\sqrt{\Omega_{m0}+\Omega_{\Lambda0}u^2}$.

**(c)** At earlier times the matter-only model expands faster relative to its present rate: $E(a)=a^{-3/2}$. Adding Λ lowers the past $E(a)$ relative to the same $H_0$, so more time is required to reach a given scale factor. The age is the accumulated $dt$, not the reciprocal of the final rate.

**(d)** Radiation grows as $a^{-4}$ and eventually dominates the early expansion. The real age integral should include it, along with the appropriate relativistic species. The correction to the total age is small compared with the difference between the two toy models, but it is not zero. Precision parameters also have uncertainties.

**Checks.** The integrand behaves as $a^{-1/2}$ near zero in the matter model, so the integral converges. Setting Λ to zero in the analytic expression must recover $2/(3H_0)$; use the limit rather than substituting into a formula containing $1/\sqrt{\Omega_\Lambda}$ blindly.
</div>

<div class="solution" id="s11" markdown="1">
<span class="sol-head">Solution 11 — A circle inside curved space.</span> [Return to problem →](06.01.html#p11)

**(a)** A geodesic radius $r$ corresponds to polar angle $\alpha=r/R$ on the sphere. The circle's embedding-space radius is $R\sin\alpha$, so

$$
C=2\pi R\sin(r/R).
$$

**(b)** Using $\sin x=x-x^3/6+\cdots$,

$$
C=2\pi r-\frac{\pi r^3}{3R^2}+\cdots,
\qquad
\frac{2\pi r-C}{2\pi r}\simeq\frac{r^2}{6R^2}.
$$

**(c)** Set the absolute deficit to $1\ \mathrm m$:

$$
r\simeq(3R^2\times1\ \mathrm m)^{1/3}
=[3(6.4\times10^6\ \mathrm m)^2]^{1/3}
=4.97\times10^4\ \mathrm m\approx49.7\ \mathrm{km}.
$$

This is an ideal one-metre total circumference difference. A real experiment would need a significance criterion and an error budget, not merely a nonzero predicted difference.

**(d)** The correction is small because $r/R\ll1$, not because it vanishes. With better precision, smaller circles can reveal curvature. Conversely, a null result places a lower bound on the curvature radius within the assumed geometry.

**Check.** At the north pole, a “circle of radius one metre” follows the surface, not a straight chord through the Earth. Confusing those radii changes the formula.
</div>

<div class="solution" id="s12" markdown="1">
<span class="sol-head">Solution 12 — Three horizons in one model.</span> [Return to problem →](06.01.html#p12)

**Idea.** A horizon is a cumulative light-travel question. Integrate along a null path; do not guess from the current Hubble radius.

**(a)** In EdS, $a=(t/t_0)^{2/3}$. Thus

$$
D_{\rm ph}(t)=a(t)c\int_0^t\frac{dt'}{a(t')}
=ct^{2/3}\int_0^t(t')^{-2/3}dt'=3ct.
$$

Since $H=2/(3t)$, $D_{\rm ph}=2c/H$.

**(b)** The future conformal-time integral is

$$
\int_t^\infty\frac{dt'}{a(t')}\propto\int_t^\infty(t')^{-2/3}dt'=\infty.
$$

There is **no finite future event horizon** in this ideal model. Any finite comoving separation can eventually be crossed by light.

**(c)** In pure de Sitter, $a=e^{H(t-t_0)}$, and

$$
D_{\rm eh,0}=c\int_{t_0}^{\infty}e^{-H(t-t_0)}dt=\frac cH.
$$

The equality with the Hubble radius is special to this model.

**(d)** The particle horizon is a present proper distance obtained by stretching all the small comoving steps traversed by the photon. Those steps were made when the scale factor was smaller. Their present total can exceed both the distance light would travel in a static space during the age and the instantaneous length $c/H_0$. No local light speed exceeds $c$.

**Checks.** The EdS particle horizon grows as $t$, while $c/H$ grows as $t$ with a different coefficient. In de Sitter, $c/H$ stays fixed while the comoving event horizon shrinks.
</div>

## Website-sourced problems: worked solutions

<div class="solution" id="s13" markdown="1">
<span class="sol-head">Solution 13 — When do distance definitions matter?</span> [Return to problem →](06.01.html#p13)

**Source.** Sheffield PHY306, Problem 4. The following is an independent worked adaptation.

**(a)** Distance duality gives $d_L/d_A=(1+z)^2$. Relative to $d_A$, the fractional difference is $(1+z)^2-1$. Setting this equal to 0.05 gives

$$
z=\sqrt{1.05}-1=0.0247\approx0.025.
$$

The leading estimate $2z=0.05$ gives the same result to this accuracy.

**(b)** Require $v_{\rm pec}/(H_0D)<0.1$. The smallest $H_0$ gives the largest required distance:

$$
D>\frac{1000}{0.1\times50}=200\ \mathrm{Mpc}.
$$

**(c)** At $D=200\ \mathrm{Mpc}$, $z\simeq H_0D/c$ gives $0.0334$ for $H_0=50$ and $0.0667$ for $H_0=100$. The corresponding leading distance-definition differences are about 6.7% and 13%, both larger than 5%.

**(d)** “Matters” depends on the target precision, the observable and the acceptable systematic error. Also, $d_L$ and $d_A$ are not two noisy measurements of one distance; they answer different operational questions. The 5% comparison is a useful scale estimate, not a law that says one definition may be ignored below a particular redshift.

**Check.** The two parts identify different systematics: confusing definitions and contaminating velocities. Solving one does not remove the other.
</div>

<div class="solution" id="s14" markdown="1">
<span class="sol-head">Solution 14 — Count the photons, not just their energies.</span> [Return to problem →](06.01.html#p14)

**Source.** Sheffield PHY306, Problem 3, rebuilt as a photon-counting argument.

**(a)** The received photon energy is $N\bar E_{\rm em}/(1+z)$. The arrival interval is $\Delta t_{\rm obs}=(1+z)\Delta t_{\rm em}$. Divide by area and time:

$$
F=\frac{N\bar E_{\rm em}}{4\pi D_C^2(1+z)^2\Delta t_{\rm em}}
=\frac{L}{4\pi[(1+z)D_C]^2}.
$$

Comparison with $F=L/(4\pi d_L^2)$ gives $d_L=(1+z)D_C$.

**(b)** At emission, a small angle $d\theta$ subtends proper length $\ell=a_{\rm em}D_Cd\theta$ in flat space. Thus $d_A=\ell/d\theta=a_{\rm em}D_C=D_C/(1+z)$.

**(c)** Eliminating $D_C$ gives $d_L=(1+z)^2d_A$.

**(d)** Photon conservation enters when the received number is taken to be the emitted number. If photons disappear, the flux acquires an additional transmission factor. Spatial flatness is a geometric statement; it does not guarantee that photons cannot be absorbed or converted. Distance duality assumes the relevant photon conservation and metric propagation conditions.

**Check.** Each factor of $1+z$ has a separate physical origin. Remembering “two factors” without knowing energy versus arrival rate makes it easy to lose one in a new problem.
</div>

<div class="solution" id="s15" markdown="1">
<span class="sol-head">Solution 15 — The Einstein–de Sitter toolkit.</span> [Return to problem →](06.01.html#p15)

**Source.** Yale ASTR 610, Problem Set 1, Problem 1.

**(a)** The Friedmann equation gives $\dot a/a=H_0(a/a_0)^{-3/2}$. Let $A=a/a_0$. Then $A^{1/2}dA=H_0dt$, so $(2/3)A^{3/2}=H_0t$ after choosing $A=0$ at $t=0$. Therefore $A=(3H_0t/2)^{2/3}$.

**(b)** Matter conservation gives $\rho=\rho_{\rm crit,0}A^{-3}$. Since $A^3=(3H_0t/2)^2$,

$$
\rho=\frac{3H_0^2}{8\pi G}\frac{4}{9H_0^2t^2}=\frac{1}{6\pi Gt^2}.
$$

Also $H=\dot A/A=2/(3t)$, so $Ht=2/3$.

**(c)** The particle horizon is $D_{\rm ph}=a c\int_0^t dt'/a=3ct=2c/H$, as derived in Solution 12.

**(d)** At $H_0=70$, $t_0=9.31\ \mathrm{Gyr}$ and $D_{\rm ph}=27.94\ \mathrm{Gly}=8.57\ \mathrm{Gpc}$. The horizon exceeds $ct_0=9.31\ \mathrm{Gly}$ because it is a present proper distance, accumulated while the universe expanded.

**Checks.** The density result contains no $H_0$: in this model, specifying the cosmic age fixes the density. That is a strong dimensional and physical consistency check.
</div>

<div class="solution" id="s16" markdown="1">
<span class="sol-head">Solution 16 — Can tired light pass every test?</span> [Return to problem →](06.01.html#p16)

**Source.** Yale ASTR 610, Problem 3, extended with duration and spectral checks.

**(a)** Integration gives $E(r)=E_0e^{-Kr}$. Since photon energy is inversely proportional to wavelength,

$$
1+z=\frac{E_0}{E(r)}=e^{Kr},\qquad z=e^{Kr}-1.
$$

**(b)** For $Kr\ll1$, $z\simeq Kr$. Matching $cz\simeq H_0r$ gives $K=H_0/c$, hence

$$
K=\frac{70}{299792.458}=2.33\times10^{-4}\ \mathrm{Mpc^{-1}}.
$$

**(c)** The stipulated toy model predicts **20 days**, because it does not change clock rates. Expansion predicts **40 days** at $z=1$. Thus matching a low-redshift distance–redshift line is not enough to make the models equivalent.

**(d)** A blackbody is not specified by a shifted wavelength alone. Its photon occupation, spectral intensity and temperature normalization must also match. Free expansion preserves the Planck form with $T\propto a^{-1}$ and produces the associated surface-brightness dimming. The simple tired-light rule gives no mechanism for all of these relations. A rival model would have to specify how photon number, arrival rates, angular propagation and spectral intensity transform, and then pass the corresponding observations.

**Check.** We have ruled out the particular toy model under the stated assumptions, not proved that no imaginable alternative theory could ever be constructed. Scientific comparisons must specify the model being tested.
</div>

<div class="solution" id="s17" markdown="1">
<span class="sol-head">Solution 17 — Equality in a different thermal universe.</span> [Return to problem →](06.01.html#p17)

**Source.** Yale ASTR 610, Problem 2. The unusually hot photon background and permanently relativistic neutrinos are deliberate hypothetical inputs.

**(a)** Matter scales as $(1+z)^3$; both relativistic components scale as $(1+z)^4$. Equality gives $1+z_{\rm eq}=\Omega_{m0}/\Omega_{r0}$, with $\Omega_{r0}=\Omega_{\gamma0}+\Omega_{\nu0}=2.5\Omega_{\gamma0}$.

**(b)** Using $u_\gamma=4\sigma T^4/c$ and $\rho_{\rm crit}=3(100h)^2/(8\pi G)$ in consistent units gives

$$
\Omega_{\gamma0}h^2=4.482\times10^{-3}\quad(T_0=10.0\ \mathrm K).
$$

This is much larger than the photon contribution at 2.725 K because radiation density scales as $T^4$.

**(c)**

$$
1+z_{\rm eq}=\frac{\Omega_{m0}h^2}{2.5(4.482\times10^{-3})}
=89.3\,\Omega_{m0}h^2.
$$

The question asks for the coefficient in terms of $\Omega_{m0}h^2$; no numerical matter density was supplied.

**(d)** A relativistic gas has $P=u/3$ and its energy density falls as $a^{-4}$. Nonrelativistic neutrinos would instead contribute approximately to matter, changing both the equality condition and the expansion history. “Neutrino” names a particle, not a permanent equation of state.

**Check.** Do not import the real universe's equality redshift or neutrino temperature ratio into a problem that explicitly replaces the thermal assumptions.
</div>

<div class="solution" id="s18" markdown="1">
<span class="sol-head">Solution 18 — Why flatness needs an explanation.</span> [Return to problem →](06.01.html#p18)

**Source.** MIT 8.286, Quiz 3 Review, Problem 9. Sign conventions follow Section 4.

**(a)** Divide the Friedmann equation by $H^2$ and move the curvature term to the other side:

$$
\Omega_{\rm tot}-1=-\Omega_k=\frac{kc^2}{a^2H^2}.
$$

**(b)** Since $H^2\Omega_{\rm tot}=8\pi G\rho/3$,

$$
\frac{\Omega_{\rm tot}-1}{\Omega_{\rm tot}}=\frac{3kc^2}{8\pi G\rho a^2}.
$$

For matter, $\rho a^2\propto a^{-1}$, so the ratio is proportional to $a\propto t^{2/3}$.

**(c)** For radiation, $\rho a^2\propto a^{-2}$, so the ratio is proportional to $a^2\propto t$.

**(d)** With constant $H$ and $a\propto e^N$,

$$
|\Omega_{\rm tot}-1|\propto e^{-2N}.
$$

Inflation drives the observable universe very close to flatness by increasing $aH$. It does not change the constant curvature sign or the underlying spatial identifications; it makes the curvature radius enormous compared with the scales we probe.

**Check.** During decelerating expansion the comoving Hubble radius grows and the flatness deviation grows. During inflation it shrinks and the deviation is suppressed. The same geometric quantity explains both statements.
</div>

<div class="solution" id="s19" markdown="1">
<span class="sol-head">Solution 19 — A very distant quasar.</span> [Return to problem →](06.01.html#p19)

**Source.** MIT 8.286, Quiz 3 Review, Problem 10. The historical redshift is used as a mathematical example; no “most distant object” status is claimed today.

**Idea.** Keep four quantities separate: age now, age then, present proper distance and emission-time proper distance. They are related, but they are not interchangeable.

**(a)** Let $E(z)=\sqrt{0.35(1+z)^3+0.65}$. Then

$$
t_0=\frac1{H_0}\int_0^\infty\frac{dz}{(1+z)E(z)},
$$

$$
t_e=\frac1{H_0}\int_{5.82}^\infty\frac{dz}{(1+z)E(z)},
\qquad
D_0=\frac c{H_0}\int_0^{5.82}\frac{dz}{E(z)},
\qquad
D_e=\frac{D_0}{6.82}.
$$

Equivalently, integrate $t_e$ from $a=1/6.82$ to zero using $da/(aH)$. The upper limit infinity is a compact way to include all earlier times in this idealized model.

**(b)** The present proper-distance recession rate is $v_{\rm rec,0}=H_0D_0$. It uses the present separation and the present rate.

**(c)** Numerical evaluation gives

$$
t_0\simeq13.9\ \mathrm{Gyr},\qquad t_e\simeq0.95\ \mathrm{Gyr},
$$

$$
D_0\simeq27.2\ \mathrm{Gly},\qquad D_e\simeq3.99\ \mathrm{Gly}.
$$

The present recession rate is about $1.81c$ with the stated definition. The lookback time is $t_0-t_e\simeq12.9\ \mathrm{Gyr}$.

**(d)** During the photon's journey the source and observer became farther apart. The photon traversed a sequence of local intervals at $c$ while the distance scale changed. A present proper distance is a snapshot quantity; it is not the distance the photon travelled through a static space.

**Checks.** $D_e(1+z)=D_0$. The emission age is positive and smaller than the present age. The superluminal proper-distance rate is not a locally measured velocity.
</div>

<div class="solution" id="s20" markdown="1">
<span class="sol-head">Solution 20 — A BAAO calculation and its approximation.</span> [Return to problem →](06.01.html#p20)

**Source.** BAAO 2015 Round 2, Question 12. Parts (a)–(c) retain its deliberately simple low-redshift model; parts (d)–(e) expose the approximation.

**(a)** $\lambda_{\rm obs}=486.1(1.30)=631.93\ \mathrm{nm}$, or **632 nm**.

**(b)** $D=cz/H_0=299792.458(0.30)/72=1249\ \mathrm{Mpc}$, approximately **1.25 Gpc**.

**(c)** In the same linear model, $t=D/c=z/H_0=4.07\ \mathrm{Gyr}$.

**(d)** In the specified flat $(0.3,0.7)$ model with $H_0=72$, numerical integration gives approximately

$$
t_{\rm LB}(0.30)=3.32\ \mathrm{Gyr},\qquad d_L(0.30)=1.51\ \mathrm{Gpc}.
$$

The linear law replaces a curved distance–redshift relation by its tangent and also fails to distinguish distance definitions. At $z=0.30$, those differences are already appreciable. The original short question is a useful estimate exercise, not a precision cosmological inference.

**(e)** The special-relativistic formula gives $\beta=(1.3^2-1)/(1.3^2+1)=0.2565$. Treating that as the present $HD_0/c$ would mix a local inertial-frame Doppler construction with a cosmological proper-distance rate.

**Check.** We have not “corrected the BAAO answer” by changing its assumptions. We solved the stated approximation first, then compared it with a richer model. That distinction is essential when using past papers.
</div>
