## 1. Atoms leave fingerprints in light

Electrons in atoms occupy quantized energy states. A transition between two states absorbs or emits a photon with

$$
\Delta E=hf=\frac{hc}{\lambda}.
$$

The same energy gap produces the same rest wavelength whether the line appears in emission or absorption. Spectroscopy turns light into a measurement of composition, motion, temperature, density, magnetic fields and geometry.

Useful lines for the exercises are Hα at 656.28 nm, Hβ at 486.13 nm and Na D near 589.0 nm. Use $c=299792.458$ km/s and $k_B=8.617333262\times10^{-5}$ eV/K.

## 2. Three spectra, three geometries

A hot dense source produces an approximate continuum. A thin excited gas emits bright lines. Cooler gas in front of a continuum source removes photons at matching wavelengths, producing absorption lines. The spectrum depends on the source and the material along the line of sight, not only on the chemical element.

{{FIG:spectra}}

## 3. A shift measures line-of-sight motion

Define $z=(\lambda_{\rm obs}-\lambda_0)/\lambda_0$. For $|v|\ll c$, $v_r\simeq cz$, with positive velocity meaning recession. For a pure radial special-relativistic Doppler shift,

$$
\frac{\lambda_{\rm obs}}{\lambda_0}=\sqrt{\frac{1+\beta}{1-\beta}},\qquad \beta=v_r/c.
$$

A shift moves the whole pattern. It does not by itself measure transverse motion. Binary orbits, rotation, expansion and gravitational shifts require different interpretations; identify the physical cause before assigning a velocity.

{{LAB:spectrum}}

## 4. Width is a different observable

Thermal motion produces a distribution of line-of-sight velocities. For atoms of mass $m$,

$$
\sigma_v=\sqrt{\frac{k_BT}{m}},\qquad \sigma_\lambda=\lambda\frac{\sigma_v}{c},\qquad \Delta\lambda_{\rm FWHM}=2\sqrt{2\ln2}\,\sigma_\lambda.
$$

The instrument also broadens the line. Resolving power $R=\lambda/\Delta\lambda$ describes an instrumental width. Independent Gaussian contributions add in variance, so their FWHMs add in quadrature. Natural, pressure, rotational and bulk-flow broadening need not be Gaussian.

{{FIG:broadening}}

## 5. Line strength and optical depth

A line’s centre can be shifted while its equivalent width stays nearly fixed. Equivalent width measures the area removed from, or added to, the continuum in wavelength units. In the optically thin limit it grows approximately with the number of absorbers. Saturated lines grow more slowly; strong damping wings change the growth again.

For pure absorption through a uniform screen,

$$
I=I_0e^{-\tau}.
$$

Optical depth $\tau=1$ leaves $1/e$ of the background intensity. A deeper line does not always mean a proportionally larger abundance.

## 6. Splitting: magnetic fields and level populations

A magnetic field can split a line. In the normal Zeeman effect, the frequency shift of each shifted component is

$$
\Delta\nu=\frac{eB}{4\pi m_e}.
$$

Real atoms can show more complicated anomalous patterns. Level populations also matter: in thermal equilibrium, $n_2/n_1=(g_2/g_1)e^{-\Delta E/(k_BT)}$. A line can be weak because few atoms occupy the relevant lower level, not because the element is absent.

## 7. Polarisation and scattering

Polarisation describes the orientation of the electric-field oscillation. An ideal polarizer transmits $I=I_0\cos^2\theta$ from already polarized light (Malus’s law). Unpolarized light loses half its intensity through the first ideal polarizer. Scattering can polarize light, especially near a 90° scattering angle. Reflection at Brewster’s angle, $\tan\theta_B=n_2/n_1$, is fully polarized in the ideal dielectric case.

## 8. Build an interpretation from several clues

Use line identification for composition, centroid for bulk motion, width for thermal/instrumental/dynamical effects, depth and equivalent width for populations and radiative transfer, splitting for magnetic fields, and polarization for geometry. No single number tells the whole story.

<div class="remark" markdown="1"><span class="remark-head">Check before claiming.</span> Subtract the instrumental width before inferring temperature. Correct velocities to a stated reference frame. Distinguish a line shift from a line width, and a wavelength shift from a change in the photon’s speed in vacuum.</div>
