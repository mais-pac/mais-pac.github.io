## Celestial Mechanics: worked solutions

<div class="solution" id="s1" markdown="1">
<span class="sol-head">Solution 1 — A different planet.</span> [Return →](01.01.html#p1)

**Idea.** Compare ratios so Earth’s mass and radius cancel. $g'/g=(M'/M)/(R'/R)^2=2/9$, so **$g'=0.222g$**. Escape speed scales as $\sqrt{M/R}$, giving $v'_{\rm esc}/v_{\rm esc}=\sqrt{2/3}=0.816$. For Earth’s 11.2 km/s this is **9.13 km/s**. A larger planet can have weaker surface gravity if its mass does not grow fast enough.

**Check.** Both results are below Earth’s; the radius increase wins in both scalings.
</div>
<div class="solution" id="s2" markdown="1">
<span class="sol-head">Solution 2 — One Earth radius up.</span> [Return →](01.01.html#p2)

The orbital radius is $r=2R_\oplus$, not $R_\oplus$. Thus $g'=g_0/4=\mathbf{2.45\ m\,s^{-2}}$. Using $GM=g_0R_\oplus^2$,

$$v=\sqrt{g_0R_\oplus/2}=5.59\ \mathrm{km\,s^{-1}},\qquad T=2\pi r/v=1.436\times10^4\ \mathrm s=3.99\ \mathrm h.$$

**Check.** A higher orbit is slower and has a longer period than a near-surface orbit.
</div>
<div class="solution" id="s3" markdown="1">
<span class="sol-head">Solution 3 — A comet’s two speeds.</span> [Return →](01.01.html#p3)

In AU–yr–solar-mass units, $T=\sqrt{4^3}=\mathbf{8\ yr}$. The distances are $r_p=4(0.25)=\mathbf{1\ AU}$ and $r_a=4(1.75)=\mathbf{7\ AU}$. With $v_0=29.7847$ km/s,

$$v_p=v_0\sqrt{\frac{1+e}{a(1-e)}}=39.40\ \mathrm{km\,s^{-1}},\quad v_a=v_0\sqrt{\frac{1-e}{a(1+e)}}=5.629\ \mathrm{km\,s^{-1}}.$$

**Check.** $r_pv_p=r_av_a$; the speed ratio is 7, the inverse of the distance ratio.
</div>
<div class="solution" id="s4" markdown="1">
<span class="sol-head">Solution 4 — The hidden wobble.</span> [Return →](01.01.html#p4)

The period uses total mass: $T=\sqrt{3^3/3}=\mathbf{3\ yr}$. The barycentre divides the separation inversely with mass: the $2M_\odot$ star has $r_1=1$ AU and the $1M_\odot$ star $r_2=2$ AU. Their speeds are $2\pi r/T$, namely 2.094 and 4.189 AU/yr. Since 1 AU/yr = 4.74047 km/s, these are **9.93 and 19.9 km/s**.

**Check.** $m_1v_1=m_2v_2$ in the barycentric frame.
</div>
<div class="solution" id="s5" markdown="1">
<span class="sol-head">Solution 5 — Weighing an eclipsing binary.</span> [Return →](01.01.html#p5)

**Idea.** The semiamplitude ratio gives the mass ratio; the sum gives the physical scale. $m_2/m_1=K_1/K_2=0.5$. For an edge-on circular binary, $a=(K_1+K_2)P/(2\pi)$, so

$$m_1+m_2=\frac{P(K_1+K_2)^3}{2\pi G}=6.04M_\odot.$$

Therefore **$m_1=4.03M_\odot$ and $m_2=2.01M_\odot$**. The star with the smaller velocity is the heavier one.

**Check.** The ratio is 2:1 and the sum is 6.04. No inclination correction is needed because $i=90^\circ$.
</div>
<div class="solution" id="s6" markdown="1">
<span class="sol-head">Solution 6 — At the semimajor axis.</span> [Return →](01.01.html#p6)

Substitute $r=a$: $v^2=GM(2/a-1/a)=GM/a$. The result is independent of $e$ because the total energy depends only on $a$. Eccentricity fixes angular momentum and therefore the velocity’s direction and the orbit’s shape. Equal speed at one radius does not imply equal velocity or a circular path.

**Check.** For $e=0$, the body stays at $r=a$; for $e>0$, it crosses that radius while moving inward or outward.
</div>
<div class="solution" id="s7" markdown="1">
<span class="sol-head">Solution 7 — An ideal Earth–Mars transfer.</span> [Return →](01.01.html#p7)

**Idea.** Use the transfer ellipse at both endpoints. $a_t=(1+1.524)/2=\mathbf{1.262\ AU}$ and $t=\frac12\sqrt{a_t^3}=\mathbf{258.9\ days}$. With $v_0=29.7847$ km/s,

$$\Delta v_1=v_0\left(\sqrt{\frac{2(1.524)}{2.524}}-1\right)=2.95\ \mathrm{km\,s^{-1}},$$
$$\Delta v_2=\frac{v_0}{\sqrt{1.524}}\left(1-\sqrt{\frac2{2.524}}\right)=2.65\ \mathrm{km\,s^{-1}}.$$

The ideal total is **5.60 km/s**. **Check.** Both burns speed the craft up heliocentrically. This is not the launch cost from Earth’s surface.
</div>
<div class="solution" id="s8" markdown="1">
<span class="sol-head">Solution 8 — A sideways boost.</span> [Return →](01.01.html#p8)

Let $v_c^2=GM/r_0$. Then $\epsilon=(1.44-2)v_c^2/2=\mathbf{-0.28GM/r_0}$. Since $\epsilon=-GM/(2a)$, $a=r_0/0.56=\mathbf{1.786r_0}$. The burn point is periapsis, so $e=1-r_0/a=\mathbf{0.44}$ and $r_a=a(1+e)=\mathbf{2.571r_0}$.

**Check.** The speed is below $\sqrt2v_c$, so the orbit remains bound. A tangential burn at an apsis leaves that point an apsis.
</div>
<div class="solution" id="s9" markdown="1">
<span class="sol-head">Solution 9 — Can we separate the stars?</span> [Return →](01.01.html#p9)

By the definition of a parsec, 1 AU at 1 pc subtends 1 arcsecond. Thus $\theta=2/100=\mathbf{0.020''}$, or 20 mas, for a favourably projected separation. The period is $\sqrt{2^3/2}=\mathbf{2\ yr}$.

**Check.** Projection can reduce the apparent separation; the distance is essential. Angular separation alone would not give a mass.
</div>
<div class="solution" id="s10" markdown="1">
<span class="sol-head">Solution 10 — A moon too close.</span> [Return →](01.01.html#p10)

$d_R=2.44R_M(1.5/3.0)^{1/3}=2.44(0.7937)R_M=\mathbf{1.94R_M}$. The rigid strengthless coefficient 1.26 would give exactly $1.00R_M$ for this density ratio. A fluid body deforms more readily, so the ideal fluid disruption scale is farther out.

**Check.** These are model estimates. Real cohesion can allow a small solid body to survive inside the fluid limit.
</div>
<div class="solution" id="s11" markdown="1">
<span class="sol-head">Solution 11 — The Earth–Sun neighbourhood.</span> [Return →](01.01.html#p11)

The Hill estimate is $a(q/3)^{1/3}=1\,\mathrm{AU}\times(10^{-6})^{1/3}=\mathbf{0.0100\ AU}=\mathbf{1.50\times10^6\ km}$. This is an approximation, not the exact L1 distance. Since $3\times10^{-6}<0.03852$, the ideal circular restricted three-body problem satisfies the L4/L5 linear-stability criterion.

**Check.** L1 is not a zero-gravity point; it co-rotates with Earth.
</div>
<div class="solution" id="s12" markdown="1">
<span class="sol-head">Solution 12 — Density from a low orbit.</span> [Return →](01.01.html#p12)

Set $r=R$ and $M=4\pi R^3\rho/3$ in $T^2=4\pi^2R^3/(GM)$. The radius cancels, giving $\rho=3\pi/(GT^2)$. With $T=5400$ s, **$\rho=4.84\times10^3\ \mathrm{kg\,m^{-3}}$**.

**Check.** The result has density units. A real orbit above the surface would make this simple surface-radius estimate an approximation.
</div>
<div class="solution" id="s13" markdown="1">
<span class="sol-head">Solution 13 — Moon versus Sun in the tides.</span> [Return →](01.01.html#p13)

**Idea.** Compare $M/d^3$, not $M/d^2$. Using the centre-to-near-side convention $2GMR/d^3$ gives $\Delta g_M=\mathbf{1.10\times10^{-6}\ m\,s^{-2}}$ and $\Delta g_\odot=\mathbf{5.05\times10^{-7}\ m\,s^{-2}}$. Their ratio is **2.18**. The Sun’s direct gravitational pull on Earth is much larger, but its greater distance makes its field more nearly uniform across Earth.

**Check.** Tides depend on a gradient. Actual ocean tides also depend on basin geometry and resonance.
</div>
<div class="solution" id="s14" markdown="1">
<span class="sol-head">Solution 14 — Borrowing a planet’s motion.</span> [Return →](01.01.html#p14)

In the planet frame the initial relative velocity is $-10$ km/s and the final one $+10$ km/s. Add the planet’s 13 km/s to return to the heliocentric frame: initial 3 km/s, final **23 km/s**, a gain of **20 km/s**. The ideal 180° turn gives the maximum change $2V_p$.

**Check.** Relative speed is unchanged in this ideal planet-frame encounter; heliocentric kinetic energy is not. The planet loses an immeasurably small amount of orbital energy and momentum. A real turn is less than 180°.
</div>
<div class="solution" id="s15" markdown="1">
<span class="sol-head">Solution 15 — The inclination degeneracy.</span> [Return →](01.01.html#p15)

**Idea.** The observables constrain a combination of companion mass and inclination. Substitution gives $f=\mathbf{0.12475M_\odot}$. Let $x=m_2/M_\odot$ and $m_1=1M_\odot$. For $i=90^\circ$, solve $x^3/(1+x)^2=0.12475$, yielding **$x=0.716$**. For $i=30^\circ$, the right-hand side is $f/\sin^3i=0.99797$, yielding **$x=2.145$**.

**Check.** A smaller inclination requires a larger companion to produce the same observed wobble. The minimum is not a measurement of the actual mass unless the inclination is known. This is the standard spectroscopic mass-function degeneracy.
</div>
