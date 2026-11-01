## 1. Gravity: a force that points somewhere

A planet does not keep moving in a straight line around the Sun because something pushes it forward. It keeps falling toward the Sun while its sideways motion carries it past the Sun. Gravity supplies the inward acceleration; inertia supplies the continued motion.

For two point masses, or outside spherically symmetric bodies,

$$
F=\frac{Gm_1m_2}{r^2},\qquad g(r)=\frac{GM}{r^2}.
$$

The distance $r$ is measured between centres, not between surfaces. The force is equal and opposite on the two bodies. A small acceleration can still describe a large orbit if it acts for a long time.

<div class="thm" markdown="1"><span class="thm-head">Constants and useful shortcuts.</span> Use $G=6.6743\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$, $M_\odot=1.98847\times10^{30}\ \mathrm{kg}$, $1\ \mathrm{AU}=1.495978707\times10^{11}\ \mathrm m$, and one Julian year $=365.25$ days. For solar orbits, $T^2=a^3/M$ when $T$ is in years, $a$ in AU and the **total** mass $M$ in solar masses. The circular speed at 1 AU around one solar mass is $29.7847\ \mathrm{km\,s^{-1}}$.</div>

## 2. Both bodies move: the barycentre

The centre of mass is the balance point of the system. For two masses separated by $r$,

$$
m_1r_1=m_2r_2,\qquad r_1+r_2=r.
$$

The heavier body has the smaller orbit. In the centre-of-mass frame the relative separation obeys a one-body gravitational problem with $G(m_1+m_2)$. This is why a binary’s period measures the **sum** of its masses. A star’s small wobble can reveal an unseen companion.

## 3. Circular motion and escape

For a circular orbit, gravity is exactly the required centripetal acceleration:

$$
v_c=\sqrt{\frac{GM}{r}},\qquad T=2\pi\sqrt{\frac{r^3}{GM}}.
$$

The orbital radius is the distance from the centre. Escape is an energy condition, not a requirement to keep firing an engine. With zero potential energy at infinity,

$$
\epsilon=\frac{v^2}{2}-\frac{GM}{r},\qquad v_{\rm esc}=\sqrt{\frac{2GM}{r}}=\sqrt2\,v_c.
$$

Negative $\epsilon$ means bound; zero is the parabolic escape limit; positive means a nonzero speed at infinity. Here $\epsilon$ is energy per unit mass in the one-body approximation.

{{LAB:orbit}}

## 4. Ellipses: the same orbit, two conservation laws

An ellipse has semimajor axis $a$, eccentricity $e$, periapsis $a(1-e)$ and apoapsis $a(1+e)$. The central mass is at a focus. Kepler’s equal-area law is angular-momentum conservation: the body moves faster when closer.

$$
T^2=\frac{4\pi^2a^3}{G(m_1+m_2)},\qquad
v^2=G(m_1+m_2)\left(\frac2r-\frac1a\right).
$$

The second expression is the **vis-viva equation**. At $r=a$, the speed is $\sqrt{GM/a}$ whatever the eccentricity. The direction is different, but the energy is fixed by $a$. At the two apsides the velocity is perpendicular to the radius, so $r_pv_p=r_av_a$.

{{FIG:orbit}}

## 5. Changing an orbit costs energy

A short tangential burn changes the speed at one radius, and therefore the opposite side of the orbit. A Hohmann transfer between circular coplanar orbits uses half an ellipse tangent to both. If the radii are $r_1<r_2$, its semimajor axis is $(r_1+r_2)/2$. Use vis-viva to find the transfer speeds, then subtract the local circular speeds. The transfer time is half the transfer period. This idealization ignores launch, planetary gravity, inclination changes and timing.

## 6. Tides and the Roche limit

Tides arise because gravity is not identical across an extended body. For a small radius $R$ at distance $d$, the centre-to-near-side differential acceleration is approximately

$$
\Delta g\simeq \frac{2GMR}{d^3}.
$$

The near-to-far difference across the whole diameter is twice this value, $4GMR/d^3$. The inverse cube makes tides much more sensitive to distance than the force itself. The Roche limit estimates where tidal stretching overwhelms a satellite’s self-gravity. For an ideal fluid satellite,

$$
d_{\rm Roche}\simeq2.44R_M\left(\frac{\rho_M}{\rho_m}\right)^{1/3}.
$$

A simple rigid, strengthless estimate uses a coefficient near 1.26. Real material strength, spin, shape and orbital history matter. The formula is a model-dependent scale, not a universal destruction switch.

{{FIG:tides}}

## 7. Lagrange points: balance in a rotating frame

In a frame rotating with a circular binary, five stationary points exist. L1, L2 and L3 lie on the line through the masses; L4 and L5 form equilateral triangles with them. These are not places where gravity vanishes. Gravity and the rotating-frame centrifugal term combine to permit a shared angular speed.

For a small mass ratio $q=m_2/(m_1+m_2)$, the Hill scale $a(q/3)^{1/3}$ estimates the distance from the smaller body to L1 or L2. L4 and L5 are linearly stable only for sufficiently unequal masses, approximately $q<0.03852$. Station-keeping may still be needed in a real many-body system.

## 8. What an orbit can tell you

A measured period and physical orbital size give a mass. An angular size also needs a distance. A radial-velocity curve gives projected speeds, so inclination matters. Before substituting, ask: Is the orbit circular? Is the companion mass negligible? Is the quoted radius a separation, altitude or semimajor axis? Are the units physical or astronomical?

<div class="remark" markdown="1"><span class="remark-head">A reliable method.</span> Draw the two bodies and the focus. Mark the known radius and velocity direction. Choose energy, angular momentum or the period–mass relation according to the question. Check the circular limit $e\to0$, the equal-mass barycentre, and the dimensions of the final expression.</div>
