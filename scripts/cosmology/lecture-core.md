## 1. What cosmology actually asks

Astronomy often asks, *What is that object?* Cosmology asks a larger question: **what rules describe the universe as a whole?** A star has a surface, a centre and surroundings. The universe need not have any of these. We cannot step outside it, look at its edge, or repeat the experiment with a second universe. Instead, we collect light from different places and different past times, then ask which simple model explains all of those observations together.

The surprising discovery is that very large scales can be simpler than small ones. A glass of water contains an enormous number of individually complicated molecules, yet a single density describes it very well. Likewise, galaxies are complicated, but averaging over sufficiently large volumes lets us describe the cosmic background by a density, a pressure and an expansion rate. Structure has not disappeared; we have chosen which questions to ask.

<div class="thm" markdown="1">
<span class="thm-head">The working picture.</span> On large scales the universe is approximately homogeneous and isotropic, its spatial geometry is close to flat, and its scale factor is increasing. The hot early universe left light nuclei and a microwave background. Small initial density variations grew into galaxies and clusters. A matter component that gravitates but is not ordinary luminous material, and a late-time accelerating component consistent with a cosmological constant, complete the minimal **ΛCDM** picture.
</div>

**Homogeneous** means “the same from place to place” at a specified cosmic time. **Isotropic** means “the same in every direction” about a point. These are not synonyms. A uniform magnetic field can be homogeneous without being isotropic: it selects a direction. A spherically symmetric distribution centred on us could look isotropic to us without being homogeneous. Isotropy about every position implies homogeneity. Our near-isotropic microwave sky, together with galaxy surveys and the Copernican assumption that we do not occupy a special central position, supports the large-scale model.

The **cosmological principle** is an approximation, not a claim that your room looks the same as a galaxy cluster. Homogeneity emerges only after substantial averaging; the precise scale depends on the statistic being measured. Cosmic time is the proper time measured by observers moving with the mean cosmic matter, called **comoving observers**. “The universe now” means a surface of equal cosmic time in this model, not everything that our telescope can see at once.

### Three different kinds of evidence

1. **Geometry and expansion:** redshifts, standardizable candles, standard rulers and gravitational-lens time delays test the relation between distance, redshift and cosmic time.
2. **Contents and history:** light-element abundances, the cosmic microwave background (CMB), and the growth of structure test the hot early universe and its ingredients.
3. **Consistency:** the same parameters must fit independent observations. A model that explains one graph but fails another is not yet a successful cosmology.

A measurement is not the same thing as an interpretation. We measure wavelengths, angles, fluxes, count rates and temperatures. “Dark energy,” “the age of the universe,” and “the curvature of space” are inferred within a framework. Good Olympiad solutions keep that chain of inference visible.

<div class="remark" markdown="1">
<span class="remark-head">Scope and notation.</span> This handout goes beyond the minimum IOAA syllabus. The core route uses algebra, geometry and physical reasoning. Sections labelled **Extension** introduce calculus, the FLRW metric and early-universe theory; they are enrichment, not a claim that tensor calculus is required in a standard IOAA solution. Throughout, $a_0=1$, $z$ is cosmological redshift unless stated otherwise, $\rho$ is mass density, $u=\rho c^2$ is energy density, and $P$ is pressure. An overdot means $d/dt$.
</div>

### Constants and a deliberately simple benchmark

| Quantity | Value used here | Meaning |
|---|---:|---|
| $c$ | $299\,792.458\ \mathrm{km\,s^{-1}}$ | speed of light |
| $G$ | $6.6743\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$ | gravitational constant |
| $1\ \mathrm{Mpc}$ | $3.0856776\times10^{19}\ \mathrm{km}$ | megaparsec |
| $1\ \mathrm{Gyr}$ | $3.15576\times10^{16}\ \mathrm{s}$ | Julian gigayear |
| $\sigma_{\rm SB}$ | $5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$ | Stefan–Boltzmann constant |
| $b_{\rm W}$ | $2.89777\times10^{-3}\ \mathrm{m\,K}$ | Wien constant for the peak of $B_\lambda$ |
| $k_{\rm B}$ | $1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$ | Boltzmann constant |
| $T_{\rm CMB,0}$ | $2.725\ \mathrm K$ | rounded present CMB temperature |
| $H_0$ | $70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ | teaching benchmark, not a consensus measurement |
| $\Omega_{m0},\Omega_{\Lambda0}$ | $0.3,\ 0.7$ | rounded flat benchmark |

The benchmark sets radiation and curvature to zero **only when studying late-time expansion**. That approximation must be switched off when discussing the early universe or matter–radiation equality. For those calculations we supply a radiation density explicitly. Parameters taken from an individual past-paper question override this table. Modern precision cosmology quotes uncertainties and correlations; these rounded numbers are for transparent calculations, not a fit to the latest data.

## 2. Expansion without a centre

Imagine marks on a rubber sheet. Increase every separation by the same factor, and each mark sees the other marks recede. No mark is the centre of the stretching. This is a useful analogy for a mathematical relation, not a claim that space is made of rubber, that the universe expands into a room, or that a two-dimensional sheet is the whole universe.

Let $\boldsymbol{\chi}$ be a fixed **comoving coordinate** and $a(t)$ the dimensionless **scale factor**. In flat space the proper separation of two comoving galaxies is

$$
D(t)=a(t)\,\chi,
\qquad
H(t)\equiv\frac{\dot a}{a},
\qquad
\dot D=H D.
$$

The last equality applies to the separation of ideal comoving galaxies, not to the size of a ruler or an atom. The coordinate $\chi$ is the separation the pair would have today because $a_0=1$. The quantity $H$ is a fractional growth rate. If $H=70\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$, a separation of one megaparsec grows by 70 kilometres in a second, while two megaparsecs grow by 140 kilometres in that second. The units are those of inverse time.

$$
H_0^{-1}=13.97\ \mathrm{Gyr},
\qquad
\frac{c}{H_0}=4.283\ \mathrm{Gpc}=13.97\ \mathrm{Gly}
\quad (H_0=70).
$$

The **Hubble time** $H_0^{-1}$ is a timescale, not automatically the age. The age depends on the entire history $H(t)$. The **Hubble radius** $c/H$ is a local expansion length, not automatically the edge of the observable universe.

{{LAB:expansion}}

### What expands, and what does not?

Freely moving, widely separated galaxies participate in the mean Hubble flow. Galaxies, stars, planets and atoms are not miniature copies of that flow. They are bound or otherwise locally governed systems. The Earth does not double in size when the cosmic scale factor doubles. Even the separation of two galaxies in a bound group need not follow $D=a\chi$.

A real galaxy's proper distance has a background part and a **peculiar velocity** part:

$$
\dot D=H D+v_{\rm pec}.
$$

Peculiar velocities arise from local gravitational interactions. A few hundred kilometres per second can overwhelm the Hubble velocity of a nearby galaxy. Andromeda is blueshifted: its motion toward us is not a failure of cosmology, because it is not an isolated comoving test particle in the smooth Hubble flow.

<div class="thm" markdown="1">
<span class="thm-head">Example 1 — changing the observer does not create a centre.</span> Suppose galaxies have positions $\mathbf r_i=a\boldsymbol\chi_i$. Relative to galaxy $j$,

$$
\mathbf r_i-\mathbf r_j=a(\boldsymbol\chi_i-\boldsymbol\chi_j),
\qquad
\dot{\mathbf r}_i-\dot{\mathbf r}_j=H(\mathbf r_i-\mathbf r_j).
$$

Every comoving galaxy sees the same linear law. The origin was a coordinate choice. **Check:** setting $H=0$ removes the Hubble flow without moving any coordinate labels.
</div>

### A first map of cosmic history

The ordering is much more important than memorizing a dozen uncertain decimal places. The diagram is a timeline, **not a size-to-scale drawing**.

{{FIG:timeline}}

“Big Bang” names the hot, dense early state and the subsequent expansion. Extrapolating classical equations all the way to $a=0$ produces a singularity, but that extrapolation exceeds the tested theory. It is not a demonstrated description of a literal first instant, and it is not an explosion at a particular location in pre-existing space.

## 3. Redshift: a clock carried by light

Define redshift using a rest-frame spectral feature:

$$
1+z\equiv\frac{\lambda_{\rm obs}}{\lambda_{\rm em}}
=\frac{\nu_{\rm em}}{\nu_{\rm obs}}.
$$

For light propagating through the smooth expanding background,

$$
\boxed{1+z=\frac{a(t_{\rm obs})}{a(t_{\rm em})}},
\qquad
a_{\rm em}=\frac{1}{1+z}\quad(a_{\rm obs}=1).
$$

Here is the idea without machinery. Send two successive wave crests. Both follow the same kind of light path, but the second starts a little later and arrives a little later. In an expanding universe the interval between arrivals is stretched by the same ratio as the scale factor. A wave's period is a clock; its wavelength is that clock multiplied by $c$.

{{FIG:redshift}}

**Extension: a short derivation.** For radial light in the metric of Section 4, $d\chi=c\,dt/a(t)$. The comoving separation of source and observer is fixed, so the integral for the first crest equals the integral for the next. For small crest intervals, $\delta t_{\rm obs}/a_{\rm obs}=\delta t_{\rm em}/a_{\rm em}$. Hence periods, wavelengths and observed durations all acquire the factor $a_{\rm obs}/a_{\rm em}$.

A supernova at $z=1$ therefore has its light-curve timescales stretched by two. This **cosmological time dilation** is an observationally important consequence, not an optional decoration of the redshift formula.

### Redshift is not one unique kind of velocity

For a purely radial special-relativistic Doppler shift in flat spacetime,

$$
1+z_{\rm Dop}=\sqrt{\frac{1+\beta}{1-\beta}},
\qquad
\beta=\frac{v}{c},
\qquad
\frac{v}{c}=\frac{(1+z)^2-1}{(1+z)^2+1}.
$$

At small $z$, $v\simeq cz$. At large cosmological redshift, inserting $cz$ into this formula and calling the result “the galaxy's velocity” is generally wrong. Cosmological redshift compares the scale factor at two events. A recession rate $HD$ compares proper distances on a chosen cosmic-time slice. They are different constructions. In curved spacetime there is no unique, distance-independent way to compare remote velocity vectors.

Observed shifts multiply rather than simply add:

$$
1+z_{\rm obs}=(1+z_{\rm cos})(1+z_{\rm pec})(1+z_{\rm grav})\cdots.
$$

For small shifts the fractional changes approximately add, which explains the familiar low-redshift formula. A careful high-redshift analysis also accounts for the observer's motion, the source's environment and the measurement band.

<div class="remark" markdown="1">
<span class="remark-head">A useful trap.</span> A source at $z=2$ is **not** moving through its local neighbourhood at $2c$. Its light is emitted locally at $c$, and every local observer measures light at $c$. The scale factor at emission was $1/3$. Its proper distance then, its proper distance now, and its light-travel time are three different quantities.
</div>

## 4. Geometry: measuring a universe from inside

### Extension — the FLRW metric

A metric is a rule for turning coordinate differences into measured distances and times. You already use one on a map: a centimetre on the map corresponds to a particular distance on the ground. In cosmology the conversion factor changes with time.

For a homogeneous and isotropic universe, the Friedmann–Lemaître–Robertson–Walker (FLRW) line element can be written

$$
ds^2=-c^2dt^2+a^2(t)\left[d\chi^2+S_k^2(\chi)\left(d\theta^2+\sin^2\theta\,d\phi^2\right)\right],
$$

$$
S_k(\chi)=
\begin{cases}
R_c\sin(\chi/R_c), & k=+1,\\
\chi, & k=0,\\
R_c\sinh(\chi/R_c), & k=-1.
\end{cases}
$$

Here $\chi$ is a radial **geodesic coordinate distance** in the comoving spatial geometry and $R_c$ is its curvature radius today. Some books instead use a dimensionless $\chi$ and put dimensions into $a$: the physics is identical, but mixing conventions causes errors. This handout keeps $a_0=1$ and gives $\chi$ and $R_c$ units of length. With this convention the curvature constant $k$ has units of inverse length squared: $k=+1/R_c^2$, $0$, or $-1/R_c^2$. Only its sign is the usual label $+1,0,-1$.

- $ds^2<0$: a timelike separation; a massive observer can experience it, with $d\tau^2=-ds^2/c^2$.
- $ds^2=0$: light propagation.
- On a $dt=0$ slice, $ds$ is a proper spatial distance.
- At fixed $t$ and $\chi$, a small transverse angle $d\theta$ corresponds to proper length $a S_k(\chi)d\theta$.

For $k=+1$, the spatial geometry is locally like a three-dimensional sphere. Its finite volume has no boundary, just as the two-dimensional surface of a ball has no edge. For $k=0$ it is locally Euclidean. For $k=-1$ it is locally hyperbolic. **Geometry does not by itself settle topology:** a flat space can have identifications, and a negatively curved space need not be infinite. Do not infer the entire universe's shape from the sign of $k$ alone.

{{FIG:curvature}}

On a sphere of radius $R_c$, a circle drawn at geodesic radius $r$ has circumference

$$
C(r)=2\pi R_c\sin(r/R_c)
=2\pi r\left[1-\frac{r^2}{6R_c^2}+O\!\left(\frac{r^4}{R_c^4}\right)\right].
$$

A small enough patch looks flat. This is why local measurements can be exquisitely Euclidean even if the curvature radius is finite. The relevant small parameter is $r/R_c$, not $r$ measured in metres.

### Curvature is not the centre of an explosion

The curvature refers to relations among distances and angles **inside space**. It does not require a physical fourth spatial direction into which our universe bends. Embedding pictures can help intuition, but the intrinsic measurements—circumferences, triangle angles and volumes—are what matter.

## 5. Why the expansion changes

### A Newtonian route to the Friedmann equation

First imagine a uniform sphere of pressureless matter. Follow a test galaxy at its edge, at physical radius $R=a\chi$. The enclosed mass $M=(4\pi/3)\rho R^3$ stays fixed as the sphere expands. Newton's shell theorem lets us treat that mass as if it were concentrated at the centre. The test galaxy's energy per unit mass is

$$
\frac12\dot R^2-\frac{GM}{R}=E.
$$

Divide by $R^2/2$ and use $R=a\chi$:

$$
H^2=\frac{8\pi G}{3}\rho+\frac{2E}{\chi^2a^2}.
$$

Identifying the last term with spatial curvature gives the first Friedmann equation. This argument builds intuition; the full result, including pressure and the meaning of the metric, belongs to general relativity.

$$
\boxed{H^2=\frac{8\pi G}{3}\rho-\frac{kc^2}{a^2}+\frac{\Lambda c^2}{3}}.
$$

With the length-valued comoving coordinates above, $a$ is dimensionless and the signed $k$ carries units of inverse length squared. Other books make $k$ dimensionless by a different coordinate choice. To avoid convention errors in calculations, **use the density-parameter form below**.

Define the critical density and density parameters by

$$
\rho_{\rm crit}(t)=\frac{3H^2}{8\pi G},
\qquad
\Omega_i=\frac{\rho_i}{\rho_{\rm crit}},
\qquad
\Omega_k=-\frac{kc^2}{a^2H^2},
\qquad
\Omega_\Lambda=\frac{\Lambda c^2}{3H^2}.
$$

Then, exactly within FLRW cosmology,

$$
1=\Omega_m+\Omega_r+\Omega_\Lambda+\Omega_k.
$$

For the normalized scale factor $a_0=1$,

$$
\boxed{E^2(z)\equiv\frac{H^2(z)}{H_0^2}
=\Omega_{r0}(1+z)^4+\Omega_{m0}(1+z)^3+\Omega_{k0}(1+z)^2+\Omega_{\Lambda0}}.
$$

For a more general non-interacting component with constant equation-of-state parameter $w_i=P_i/u_i$, replace its contribution by $\Omega_{i0}(1+z)^{3(1+w_i)}$.

<div class="thm" markdown="1">
<span class="thm-head">Example 2 — the density that goes with the benchmark.</span> Convert $H_0$ before using SI constants:

$$
H_0=\frac{70}{3.0856776\times10^{19}}\ \mathrm{s^{-1}}
=2.26855\times10^{-18}\ \mathrm{s^{-1}},
$$

$$
\rho_{\rm crit,0}=9.20\times10^{-27}\ \mathrm{kg\,m^{-3}},
\qquad
u_{\rm crit,0}=8.27\times10^{-10}\ \mathrm{J\,m^{-3}}.
$$

That is only a few hydrogen masses per cubic metre. “Critical” does not mean dense in everyday terms. It marks the density needed for spatial flatness at a given expansion rate, after all energy contributions are included.
</div>

### Conservation: the first law applied to expansion

Take a comoving volume $V\propto a^3$. For a uniform fluid with no matter flowing across its boundary and no heat exchange between separate components, $d(uV)=-P\,dV$. This gives

$$
\boxed{\dot u+3H(u+P)=0}.
$$

For $P=w u$ with constant $w$,

$$
u\propto a^{-3(1+w)},
\qquad
\rho_m\propto a^{-3},
\qquad
u_r\propto a^{-4},
\qquad
u_\Lambda=\mathrm{constant}.
$$

Matter dilution is a counting argument: the same particles occupy a larger volume. Radiation loses photon energy as well: number density falls as $a^{-3}$ and each photon's energy falls as $a^{-1}$. A cosmological constant has $w=-1$, so its energy density remains constant as volume grows. This does **not** mean that a small box is an unlimited source of extractable useful energy; global gravitational energy is not bookkept like the energy of a gas cylinder in a laboratory.

### Pressure gravitates too

The acceleration equation is

$$
\boxed{\frac{\ddot a}{a}=-\frac{4\pi G}{3}\left(\rho+\frac{3P}{c^2}\right)+\frac{\Lambda c^2}{3}}.
$$

If $\Lambda$ is included as a fluid with $u_\Lambda=\rho_\Lambda c^2$ and $P_\Lambda=-u_\Lambda$, omit the separate $\Lambda$ term and include that fluid in the sum. **Choose one bookkeeping convention.** Combining the two equations with local conservation shows that they are not three unrelated assumptions.

For a component to accelerate expansion by itself, it needs

$$
u+3P<0
\quad\Longleftrightarrow\quad
w<-\frac13.
$$

Radiation has $w=1/3$ and decelerates expansion more strongly, at fixed energy density, than pressureless matter. Negative pressure is not a gas “sucking from outside.” It is a term in the stress-energy that tells gravity how that component behaves. Uniform pressure has no pressure-gradient force; its gravitational effect remains.

Define the deceleration parameter

$$
q\equiv-\frac{a\ddot a}{\dot a^2}=-1-\frac{\dot H}{H^2}.
$$

Positive $q$ means slowing expansion; negative $q$ means accelerating expansion. An expanding universe can have a decreasing $H$ while $\dot D=a\chi H$ increases. Do not confuse $\dot H<0$ with $\ddot a<0$.

## 6. Solving the expansion history

The first Friedmann equation is an energy-like equation. Once the contents are specified, it determines how rapidly $a$ changes. The useful conversion is

$$
dt=\frac{da}{aH(a)}=-\frac{dz}{(1+z)H(z)}.
$$

### Single-component universes

For a flat universe dominated by one constant-$w$ component, with $w>-1$,

$$
a(t)\propto t^{\frac{2}{3(1+w)}},
\qquad
H=\frac{2}{3(1+w)t}.
$$

| Dominant component | $w$ | $a(t)$ | Age–rate relation |
|---|---:|---|---|
| radiation | $1/3$ | $t^{1/2}$ | $t=1/(2H)$ |
| pressureless matter | $0$ | $t^{2/3}$ | $t=2/(3H)$ |
| cosmological constant | $-1$ | $e^{Ht}$ | no finite Big Bang age within this pure model |
| curvature-dominated toy model | effective $-1/3$ | $t$ | $t=1/H$ |

The last row is not an ordinary fluid dominating a flat universe; it describes the behaviour of an empty, negatively curved Milne model. These exact models are benchmarks. The real universe passes through different regimes and cannot be assigned one power law for its entire history.

<div class="thm" markdown="1">
<span class="thm-head">Example 3 — why Einstein–de Sitter is not the benchmark age.</span> In a flat, matter-only model, $H=H_0a^{-3/2}$. Thus

$$
t_0=\frac{1}{H_0}\int_0^1\frac{da}{a\,a^{-3/2}}
=\frac{1}{H_0}\int_0^1a^{-1/2}da
=\frac{2}{3H_0}.
$$

For $H_0=70$, this is $9.31\ \mathrm{Gyr}$, not $13.97\ \mathrm{Gyr}$. The missing ingredient is the expansion history, not a numerical conversion error.
</div>

### The flat matter-plus-Λ benchmark

Neglect radiation at late times. With $\Omega_{m0}+\Omega_{\Lambda0}=1$ and positive densities,

$$
a(t)=\left(\frac{\Omega_{m0}}{\Omega_{\Lambda0}}\right)^{1/3}
\sinh^{2/3}\left(\frac32H_0\sqrt{\Omega_{\Lambda0}}\,t\right),
$$

$$
\boxed{t_0=\frac{2}{3H_0\sqrt{\Omega_{\Lambda0}}}
\operatorname{arsinh}\sqrt{\frac{\Omega_{\Lambda0}}{\Omega_{m0}}}}.
$$

For $(0.3,0.7,70)$ this gives approximately $13.47\ \mathrm{Gyr}$. The expression is a useful check on numerical integration, but it is not valid through the radiation era without modification.

The lookback time to redshift $z$ and the cosmic age at emission are

$$
t_{\rm LB}(z)=\frac{1}{H_0}\int_0^z\frac{dz'}{(1+z')E(z')},
\qquad
t(z)=t_0-t_{\rm LB}(z).
$$

### Equality is not acceleration

Matter and Λ have equal densities when

$$
1+z_{m\Lambda}=\left(\frac{\Omega_{\Lambda0}}{\Omega_{m0}}\right)^{1/3}.
$$

Acceleration starts when the active gravitational density vanishes: $\rho_m+\rho_\Lambda+3P_\Lambda/c^2=\rho_m-2\rho_\Lambda=0$. Thus

$$
\boxed{1+z_{\rm acc}=\left(\frac{2\Omega_{\Lambda0}}{\Omega_{m0}}\right)^{1/3}}.
$$

For the benchmark, $z_{m\Lambda}\simeq0.327$ and $z_{\rm acc}\simeq0.672$. Acceleration begins earlier, at a higher redshift, because Λ acquires dynamical importance before its density actually exceeds the matter density. **Never use “domination” as a synonym for “the onset of acceleration.”**

{{LAB:dynamics}}

### Curvature and cosmic fate

Spatial geometry and future expansion were once treated as almost the same question. With Λ they are not. A positively curved universe can expand forever if Λ is large enough; a flat universe containing only matter decelerates forever. To decide the fate, examine whether $H^2(a)$ can reach zero at a future $a>1$, and then use the acceleration equation. The sign of curvature alone is insufficient.

A static solution requires both $H=0$ and $\ddot a=0$. The Einstein static universe balances matter, positive curvature and Λ, but the balance is unstable: a small expansion lowers the matter density and lets Λ win; a small contraction does the reverse. This is a valuable limiting-case problem, not the model we observe.

## 7. Five distances, five different questions

At large redshift, “How far away is it?” is incomplete. Ask **which operation defines the distance?** The following definitions reduce to the same familiar distance nearby but differ substantially far away.

| Distance | Operational question | Flat-universe relation |
|---|---|---|
| lookback distance $ct_{\rm LB}$ | how long has the light travelled? | integrate $dt$ |
| comoving radial distance $D_C$ | what would a present-day ruler measure? | $c\int_0^z dz'/H(z')$ |
| proper distance then $D_{\rm em}$ | how far was it when the light left? | $D_C/(1+z)$ |
| angular-diameter distance $d_A$ | how large does a known ruler look? | $D_C/(1+z)$ |
| luminosity distance $d_L$ | how faint does a known luminosity appear? | $(1+z)D_C$ |

In a curved universe the transverse comoving distance is $D_M=S_k(\chi)$, while the radial geodesic distance remains $\chi$. Then $d_A=D_M/(1+z)$ and $d_L=(1+z)D_M$. Using $D_C$ instead of $D_M$ in those two formulas is a common but avoidable mistake.

$$
\boxed{d_L=(1+z)^2d_A}
$$

is **Etherington's distance-duality relation**. It holds when photons travel on null geodesics, their number is conserved, and the spacetime description is metric; it does not require spatial flatness.

{{FIG:distances}}

### Why luminosity distance has two factors of $1+z$

Suppose a source emits bolometric luminosity $L$. Today its photons are spread over area $4\pi D_M^2$. Each photon has lost an energy factor $1/(1+z)$, and the arrival rate is lower by another factor $1/(1+z)$. Thus

$$
F=\frac{L}{4\pi D_M^2(1+z)^2}
\equiv\frac{L}{4\pi d_L^2}.
$$

This is a **bolometric** statement. A real detector measures a finite band. Comparing emitted and observed bands requires a filter-dependent **K-correction**, and sometimes a luminosity-model correction. A redshifted spectrum does not keep the same flux inside a fixed blue filter.

### Why angular size need not shrink forever

For a ruler of proper transverse length $\ell$ at emission, the small-angle relation is $\theta=\ell/d_A$. As redshift increases, $D_M$ grows but the universe was smaller at emission. The competition can make $d_A$ reach a maximum and then decrease. Beyond that redshift a ruler of fixed proper size can subtend a **larger** angle. There is no contradiction: the light left when the ruler was much closer in proper separation.

Surface brightness provides another powerful check. Bolometric flux falls as $d_L^{-2}$ while apparent solid angle is set by $d_A^{-2}$. Therefore

$$
I_{\rm obs}=\frac{I_{\rm em}}{(1+z)^4},
$$

for corresponding bolometric surface brightness, before practical bandpass effects. This **Tolman dimming** is a consequence of expansion and distance duality, not simply dust making galaxies fainter.

### The distance ladder and standard rulers

Parallax calibrates distances geometrically. Those distances calibrate stellar indicators such as Cepheids, which can calibrate Type Ia supernovae in nearby host galaxies. Supernovae then extend the relative distance scale to much larger redshifts. Different rungs overlap; no single method spans the entire range. Other routes, including gravitational-lens time delays and the early-universe sound horizon, test the calibration independently.

Type Ia supernovae are **standardizable**, not identical candles. Light-curve shape and colour help reduce the scatter in inferred luminosity. Dust, population evolution and calibration systematics still matter. Baryon acoustic oscillations (BAO) provide a comoving standard ruler; a measured angle constrains $r_d/D_M(z)$, while a redshift separation constrains roughly $H(z)r_d/c$. The absolute ruler scale $r_d$ depends on early-universe physics.

For a calibrated luminosity distance,

$$
m-M=5\log_{10}\!\left(\frac{d_L}{10\ \mathrm{pc}}\right)
=5\log_{10}\!\left(\frac{d_L}{\mathrm{Mpc}}\right)+25.
$$

A constant fractional distance error is a constant magnitude offset. At low redshift, where $d\simeq cz/H_0$, an unknown candle calibration trades directly against $H_0$. The **shape** of a supernova Hubble diagram can reveal acceleration even when the absolute normalization is uncertain.

{{LAB:distances}}
