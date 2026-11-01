## 1. The nucleus in symbols

A nuclide $^A_ZX$ has $Z$ protons and $N=A-Z$ neutrons. Chemical identity is set by $Z$; isotopes share $Z$ but differ in $N$. Nuclear reactions conserve charge and nucleon number (and, more fundamentally, energy, momentum and other quantum numbers).

Alpha decay lowers $A$ by 4 and $Z$ by 2. Beta-minus decay converts a neutron into a proton, emitting an electron and an antineutrino, so $A$ stays fixed and $Z$ rises by 1. Gamma emission changes nuclear energy state without changing $A$ or $Z$.

Use $1u=931.494\ \mathrm{MeV}/c^2$, $N_A=6.02214076\times10^{23}\ \mathrm{mol^{-1}}$, $c=2.99792458\times10^8$ m/s and one year $=3.15576\times10^7$ s.

## 2. Missing mass is binding energy

A bound nucleus weighs less than its separated constituents. The mass defect is

$$
\Delta m=Zm_p+Nm_n-m_{\rm nucleus},\qquad B=\Delta mc^2.
$$

When using neutral atomic masses, replace proton masses with hydrogen-atom masses for reactions whose total electron count balances; electron masses then cancel to excellent accuracy. Binding energy per nucleon $B/A$ measures how tightly bound a nucleus is.

{{FIG:binding}}

## 3. Why fusion and fission can both release energy

Light nuclei can release energy by fusing into more tightly bound products. Very heavy nuclei can release energy by splitting into intermediate-mass products. The energy release is

$$
Q=(m_{\rm initial}-m_{\rm final})c^2.
$$

Positive $Q$ is exothermic. The binding-energy curve gives the trend; actual masses give the answer. Hydrogen-to-helium fusion converts about 0.7% of the initial rest mass into energy, far more per kilogram than chemical burning.

## 4. Radioactivity is a probability law

For a large sample, the decay rate is proportional to the number remaining:

$$
\frac{dN}{dt}=-\lambda N,\qquad N=N_0e^{-\lambda t}=N_0\,2^{-t/T_{1/2}}.
$$

Activity is $A=\lambda N$, measured in becquerels (decays/s). The half-life is $T_{1/2}=\ln2/\lambda$; the mean lifetime is $\tau=1/\lambda$. The exponential is optional enrichment: the half-life form is enough for most Olympiad calculations.

{{FIG:decay}}

{{LAB:decay}}

## 5. Decay chains and equilibrium

A radioactive daughter can be produced while it is also decaying. Its abundance depends on both rates. If the parent is much longer-lived than the daughter, secular equilibrium can develop: daughter activity becomes approximately equal to parent activity even though the daughter contains far fewer nuclei.

For a parent $p$ feeding a daughter $d$ from an initially pure parent sample,

$$
N_d(t)=\frac{\lambda_pN_{p0}}{\lambda_d-\lambda_p}\left(e^{-\lambda_pt}-e^{-\lambda_dt}\right).
$$

This formula assumes a simple two-member chain and no initial daughter. It is enrichment beyond the minimum syllabus requirement.

## 6. Neutrinos: the missing energy carriers

Neutrinos interact weakly and can escape dense stellar cores. In beta decay they carry energy, momentum and lepton number. In the solar proton–proton chain, two neutrinos are produced per helium nucleus assembled. The photon luminosity therefore does not include all the nuclear energy release.

Neutrinos are marked qualitative in the IOAA syllabus, but simple counting and flux estimates are useful. A neutrino flux at distance $d$ from an isotropic source is its production rate divided by $4\pi d^2$.

## 7. Dating and fuel clocks

Radiometric dating compares remaining parent with accumulated daughter, assuming a closed system and known initial daughter content. A stellar fuel clock divides available nuclear energy by luminosity. Neither clock is just a half-life: the relevant reservoir and loss rate must be identified.

<div class="thm" markdown="1"><span class="thm-head">Solar fuel estimate.</span> If a fraction $f$ of a star’s mass can burn and a fraction $\epsilon$ of that mass becomes energy, $t\sim f\epsilon Mc^2/L$. For the Sun, $f\sim0.1$ and $\epsilon\sim0.007$ give about $10^{10}$ years at the present luminosity.</div>

## 8. Check conservation and the energy destination

Balance $A$ and $Z$ before computing masses. Keep track of whether a quoted $Q$ includes neutrino energy, annihilation energy or kinetic energy of a particular product. Activity is not the number of nuclei; it is the number remaining multiplied by a rate.

<div class="remark" markdown="1"><span class="remark-head">Common traps.</span> After three half-lives, one eighth remains, not zero. Atomic masses include electrons. A reaction can be energetically allowed yet slow because of a barrier or a weak interaction. “Qualitative” neutrino coverage does not mean neutrinos are optional in the underlying physics.</div>
