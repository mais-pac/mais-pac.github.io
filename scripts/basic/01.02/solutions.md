## Radiation and Quanta: worked solutions

<div class="solution" id="s1" markdown="1">
<span class="sol-head">Solution 1 — Count the packets.</span> [Return →](01.02.html#p1)

$f=c/\lambda=\mathbf{5.996\times10^{14}\ Hz}$. $E=1239.84/500=\mathbf{2.480\ eV}=3.973\times10^{-19}$ J. A joule per second divided by joules per photon gives **$2.52\times10^{18}$ photons/s**.

**Check.** Higher power at the same colour means more photons, not more energy per photon.
</div>
<div class="solution" id="s2" markdown="1">
<span class="sol-head">Solution 2 — Ten parsecs away.</span> [Return →](01.02.html#p2)

$F=4L_\odot/[4\pi(10\,\mathrm{pc})^2]$. With $d=3.08568\times10^{17}$ m, **$F=1.28\times10^{-9}\ \mathrm{W\,m^{-2}}$**. This is bolometric flux, not a visual-band measurement.

**Check.** Doubling the distance would reduce the flux fourfold.
</div>
<div class="solution" id="s3" markdown="1">
<span class="sol-head">Solution 3 — A green-ish peak.</span> [Return →](01.02.html#p3)

$T=2.89777\times10^{-3}/(500\times10^{-9})=\mathbf{5796\ K}$. The surface flux is $\sigma T^4=\mathbf{6.40\times10^7\ W\,m^{-2}}$. A blackbody emits a broad range of wavelengths; human colour perception integrates that range. A peak in green does not make a star monochromatic green.

**Check.** This temperature is close to the Sun’s, whose integrated visible light is approximately white.
</div>
<div class="solution" id="s4" markdown="1">
<span class="sol-head">Solution 4 — Infer a radius.</span> [Return →](01.02.html#p4)

Use $L\propto R^2T^4$. Thus $R/R_\odot=\sqrt{9/2^4}=\sqrt{9/16}=\mathbf{0.75}$. The hotter surface compensates for the smaller area.

**Check.** $(0.75)^2(2)^4=9$.
</div>
<div class="solution" id="s5" markdown="1">
<span class="sol-head">Solution 5 — Same temperature, different size.</span> [Return →](01.02.html#p5)

At equal temperature, flux ratio equals area ratio, $2^2=4$. Therefore $\Delta m=-2.5\log_{10}4=\mathbf{-1.505}$. The larger star has the smaller magnitude.

**Check.** Brighter means more negative magnitude difference.
</div>
<div class="solution" id="s6" markdown="1">
<span class="sol-head">Solution 6 — The stopping voltage.</span> [Return →](01.02.html#p6)

$\phi=1239.84/400=\mathbf{3.100\ eV}$. At 250 nm, $E_\gamma=4.959$ eV, so $K_{\max}=\mathbf{1.860\ eV}$ and $V_{\rm stop}=\mathbf{1.860\ V}$. Doubling intensity doubles the available photon rate and, in the unsaturated ideal case, the emission rate; it does not change $K_{\max}$.

**Check.** The incident photon energy exceeds the threshold.
</div>
<div class="solution" id="s7" markdown="1">
<span class="sol-head">Solution 7 — A photon budget.</span> [Return →](01.02.html#p7)

The collecting area is $\pi(1)^2=3.1416$ m². Counts $N=1000\times3.1416\times0.25\times60=\mathbf{4.71\times10^4}$; ideal SNR $=\sqrt N=\mathbf{217}$. A 4 m telescope has four times the area, so SNR becomes **434**.

**Check.** SNR grows with diameter, not diameter squared, when photon shot noise dominates.
</div>
<div class="solution" id="s8" markdown="1">
<span class="sol-head">Solution 8 — A solar sail.</span> [Return →](01.02.html#p8)

$p_{\rm abs}=F/c=\mathbf{4.54\times10^{-6}\ Pa}$; perfect reflection gives **$9.08\ \mu$Pa**. On 100 m² the absorbing force is $pA=\mathbf{4.54\times10^{-4}\ N}$.

**Check.** Radiation pressure is small because $c$ is large. Oblique incidence changes the projected area and momentum direction.
</div>
<div class="solution" id="s9" markdown="1">
<span class="sol-head">Solution 9 — Which peak?</span> [Return →](01.02.html#p9)

$B_\lambda d\lambda$ and $B_\nu d\nu$ describe the same power in corresponding intervals, so $B_\lambda= B_\nu|d\nu/d\lambda|=B_\nu c/\lambda^2$. The extra Jacobian changes the shape and shifts the maximum. **Integrated power over corresponding intervals is conserved**, not the numerical location of a density maximum.

**Check.** Always state whether a peak is per unit wavelength or per unit frequency.
</div>
<div class="solution" id="s10" markdown="1">
<span class="sol-head">Solution 10 — Compensating changes.</span> [Return →](01.02.html#p10)

$L'/L=(1/2)^2(2)^4=\mathbf{4}$: the luminosity quadruples, not stays fixed. Wien’s law gives $\lambda'_{\max}/\lambda_{\max}=1/2$. Radius affects total area, not the peak wavelength.

**Check.** Surface flux grows sixteenfold while area falls fourfold.
</div>
<div class="solution" id="s11" markdown="1">
<span class="sol-head">Solution 11 — From angle to temperature.</span> [Return →](01.02.html#p11)

**Idea.** Convert angular diameter to physical diameter before using the luminosity law. At 100 pc, $0.002''$ corresponds to diameter $0.002\times100=0.2$ AU, so $R=0.1$ AU $=\mathbf{21.50R_\odot}$. Then

$$T=5772\left(\frac{100}{21.50^2}\right)^{1/4}=\mathbf{3936\ K}.$$

**Check.** This is a large, cool luminous star. Using the angular diameter as an angular radius would double the radius and lower the inferred temperature incorrectly.
</div>
<div class="solution" id="s12" markdown="1">
<span class="sol-head">Solution 12 — Do not saturate.</span> [Return →](01.02.html#p12)

Electron rate $=0.8\times10^5=8.0\times10^4$ s⁻¹. Thus $t_{\max}=50000/80000=\mathbf{0.625\ s}$. Short exposures avoid full-well saturation; stacking can restore total counts and improve SNR, though read noise and overheads must be included in a real instrument.

**Check.** The limit is set by electrons stored, not photons incident.
</div>
<div class="solution" id="s13" markdown="1">
<span class="sol-head">Solution 13 — A moving photon source.</span> [Return →](01.02.html#p13)

For $v/c=0.001$, $\Delta\lambda/\lambda\simeq+0.001$ and $\Delta E/E\simeq-0.001$: **0.1% redder and 0.1% less energetic per photon**. The photon still travels at $c$ in vacuum. The energy difference is frame-dependent, not a slowing photon.

**Check.** The exact relativistic shift differs only at order $(v/c)^2$ here.
</div>
<div class="solution" id="s14" markdown="1">
<span class="sol-head">Solution 14 — Dust at the blowout scale.</span> [Return →](01.02.html#p14)

Substitution in $\beta=3L/(16\pi cGM\rho s)$ gives **$\beta=0.287$**. Since $\beta\propto1/s$, the radius for $\beta=0.5$ is $1\,\mu\mathrm m\times(0.287/0.5)=\mathbf{0.574\ \mu m}$.

**Check.** Smaller grains feel more radiation force per unit mass. Actual blowout also depends on the grain’s release orbit and optical properties.
</div>
<div class="solution" id="s15" markdown="1">
<span class="sol-head">Solution 15 — An eclipse in two bands.</span> [Return →](01.02.html#p15)

**Idea.** An eclipse removes the planet’s light. Bolometrically, the contrast is area ratio times $T^4$ ratio:

$$\delta_{\rm bol}=(0.1)^2(1500/6000)^4=\mathbf{3.91\times10^{-5}}=39.1\ \mathrm{ppm}.$$

At the same wavelength, the Planck prefactor cancels. With $x=14387.77/(\lambda_{\mu\mathrm m}T)$,

$$\delta_{10\mu\mathrm m}=0.01\frac{e^{x_*}-1}{e^{x_p}-1}=\mathbf{1.68\times10^{-3}}=1684\ \mathrm{ppm}.$$

**Check.** In the infrared the cool planet is much less disadvantaged relative to the star than in total power. A real bandpass requires integration over the filter and stellar/planetary spectra.
</div>
