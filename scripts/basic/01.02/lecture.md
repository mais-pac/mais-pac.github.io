## 1. Light carries both a wave scale and an energy packet

Radio waves, visible light and gamma rays are the same kind of electromagnetic phenomenon. They differ in wavelength and frequency. In vacuum,

$$
c=\lambda f,\qquad E_\gamma=hf=\frac{hc}{\lambda}.
$$

A convenient conversion is $E(\mathrm{eV})=1239.84/\lambda(\mathrm{nm})$. A blue photon carries more energy than a red photon. But a bright red lamp can deliver more total power than a faint blue lamp because it sends more photons.

Use $c=2.99792458\times10^8\ \mathrm{m\,s^{-1}}$, $h=6.62607015\times10^{-34}\ \mathrm{J\,s}$, $1\ \mathrm{eV}=1.602176634\times10^{-19}$ J, $\sigma=5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$, $R_\odot=6.957\times10^8$ m and $L_\odot=3.828\times10^{26}$ W.

{{FIG:photons}}

## 2. Luminosity is not flux

A star’s luminosity $L$ is the energy it emits per second. The flux $F$ at a distance $d$ is the power crossing each square metre of a sphere around it:

$$
F=\frac{L}{4\pi d^2}.
$$

The inverse square is geometry: the same power spreads over an area growing as $d^2$. Flux is not surface brightness, and neither is luminosity. A telescope collects power $FA$ through area $A$, then loses some to throughput and detector efficiency.

## 3. A blackbody is a thermal reference, not a colour label

An ideal blackbody absorbs incident radiation and emits a spectrum determined only by temperature. Real stars are approximate blackbodies with spectral lines and wavelength-dependent opacity. Planck’s law per unit wavelength is

$$
B_\lambda(T)=\frac{2hc^2}{\lambda^5}\frac{1}{e^{hc/(\lambda k_BT)}-1}.
$$

It is a surface brightness per steradian per wavelength interval. You rarely need to evaluate the full expression in an Olympiad problem: Wien’s and Stefan–Boltzmann’s laws extract the peak and total power.

{{FIG:planck}}

## 4. Two shortcuts with different jobs

Wien’s displacement law for the wavelength spectrum is

$$
\lambda_{\max}T=2.897771955\times10^{-3}\ \mathrm{m\,K}.
$$

The Stefan–Boltzmann law integrates over all wavelengths:

$$
F_{\rm surface}=\sigma T^4,\qquad L=4\pi R^2\sigma T^4.
$$

A hotter star is bluer and emits much more power per unit area. A larger star can be cooler yet more luminous. The peak of $B_\lambda$ is not the peak of $B_\nu$ expressed at the same wavelength; the two densities use different interval variables.

{{LAB:blackbody}}

## 5. Counting photons

If a detector receives power $P$ at wavelength $\lambda$, the ideal photon arrival rate is $P/E_\gamma$. With quantum efficiency $\eta$, the electron rate is $\eta P/E_\gamma$. For $N$ independent detected photons, Poisson shot noise has standard deviation $\sqrt N$, so the photon-limited signal-to-noise ratio is $\sqrt N$. Doubling telescope diameter quadruples collecting area and doubles this ideal SNR for the same exposure.

## 6. The photoelectric threshold

A photon can eject an electron only if its energy exceeds the material’s work function $\phi$. Einstein’s energy balance is

$$
K_{\max}=hf-\phi,\qquad eV_{\rm stop}=K_{\max}.
$$

Increasing intensity at fixed frequency increases the number of photons, not the maximum energy of each electron. Below the threshold frequency, more intensity does not fix the energy deficit in the simple one-photon effect.

## 7. Radiation pushes, and dust feels it differently

Absorbed light transfers momentum at rate $P/c$; perfect reflection reverses the photon momentum and doubles the force. For a spherical grain, radiation pressure and stellar gravity both fall as $1/d^2$, so their ratio is independent of distance in the simple model:

$$
\beta=\frac{F_{\rm rad}}{F_{\rm grav}}=\frac{3LQ_{\rm pr}}{16\pi cGM\rho s}.
$$

Here $s$ is grain radius, $\rho$ its density and $Q_{\rm pr}$ an efficiency factor. Smaller grains have larger area per unit mass and are more easily blown out. Real optics, charging and gas drag complicate the picture.

## 8. Choose the measurement before the formula

A spectrum’s peak constrains temperature; total flux plus distance gives luminosity; luminosity and temperature give radius. Photon counts constrain detector exposure. A transit depth gives an area ratio, while an eclipse depth also depends on surface brightness at the observed wavelength.

<div class="remark" markdown="1"><span class="remark-head">Common traps.</span> Use metres in Planck’s and Wien’s laws. Distinguish a wavelength interval from a frequency interval. Do not call $hc/\lambda_{\max}$ the average photon energy. Do not use a bolometric $T^4$ contrast for a narrow infrared band without checking the spectrum.</div>
