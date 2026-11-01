## 1. Temperature is a state; heat is a transfer

A gas has a temperature. It does not “contain heat” in the same sense. Heat is energy crossing a boundary because of a temperature difference; work is another way to transfer energy. Thermal equilibrium means no net heat flow between systems in contact.

For a dilute ideal gas,

$$
PV=Nk_BT=nRT.
$$

Use kelvins. Here $N$ counts particles, $n$ counts moles, $k_B=1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$ and $R=8.314462618\ \mathrm{J\,mol^{-1}\,K^{-1}}$. The model neglects molecular volume and long-range interactions; it is a useful approximation, not a universal law.

## 2. The first law is an energy account

We take $Q>0$ when heat enters the gas and $W>0$ when the gas does work on its surroundings:

$$
\Delta U=Q-W,\qquad W=\int P\,dV.
$$

For a monatomic ideal gas, $U=\frac32nRT$. Internal energy depends only on temperature; heat and work depend on the path. A $P$–$V$ diagram makes this visible: work is the signed area under the curve.

{{FIG:pv}}

## 3. Four processes, four energy bills

| Process | Constraint | Ideal-gas consequence |
|---|---|---|
| Isochoric | $V$ fixed | $W=0$, $Q=\Delta U$ |
| Isobaric | $P$ fixed | $W=P\Delta V=nR\Delta T$ |
| Isothermal | $T$ fixed | $\Delta U=0$, $Q=W=nRT\ln(V_2/V_1)$ |
| Reversible adiabatic | $Q=0$ | $PV^\gamma$ fixed, $TV^{\gamma-1}$ fixed |

For a monatomic gas, $C_V=3R/2$, $C_P=5R/2$ and $\gamma=5/3$ per mole. At constant pressure, added heat must both raise internal energy and pay for expansion work.

{{LAB:gas}}

## 4. Cycles and engines

Over a complete cycle, the gas returns to its initial state, so $\Delta U=0$ and net heat equals net work. A clockwise loop on a $P$–$V$ diagram does positive work. Efficiency is useful work divided by **heat input**, not by the net heat:

$$
\eta=\frac{W_{\rm net}}{Q_{\rm in}}.
$$

Identify which legs absorb heat before computing efficiency. The Carnot limit $1-T_c/T_h$ applies to a reversible engine between two reservoirs, not to every arbitrary cycle.

## 5. A planet’s energy balance

A planet intercepts starlight over a disk $\pi R^2$ and, in a uniform-temperature model, emits over $4\pi R^2$. With incident flux $F$ and Bond albedo $A$,

$$
(1-A)F\pi R^2=4\pi R^2\sigma T_{\rm eff}^4.
$$

The radius cancels. The factor of four is geometry. The effective radiating temperature need not equal the surface temperature: an atmosphere can change where radiation escapes.

{{FIG:planet}}

## 6. Three ways energy moves

Conduction transfers energy through microscopic interactions, with Fourier’s law $\dot Q=kA\Delta T/\ell$ for a uniform slab. Convection carries energy with moving fluid; a rising parcel cools as pressure falls. Radiation transfers energy by photons and works through vacuum. In stars, opacity and temperature gradients help determine whether radiation or convection dominates.

## 7. Atmospheric and stellar scales

For an isothermal ideal atmosphere in constant gravity, hydrostatic balance gives

$$
P(z)=P_0e^{-z/H},\qquad H=\frac{k_BT}{\mu m_u g}.
$$

A scale height is the distance for a factor-$e$ pressure drop. For a dry ideal atmosphere, the adiabatic temperature gradient is approximately $g/c_p$. Comparing a lifted parcel with its surroundings diagnoses buoyant stability.

A thermal timescale compares an energy reservoir with a loss rate. The Kelvin–Helmholtz scale $GM^2/(RL)$ estimates how long gravitational contraction could power a luminosity. It is not the nuclear main-sequence lifetime.

## 8. Check the model, not only the arithmetic

Ask whether the gas is ideal, whether a process is reversible, whether temperature is uniform, and which surface emits. Keep the first-law sign convention fixed. A numerical answer should pass an energy balance and a limiting-case check.

<div class="remark" markdown="1"><span class="remark-head">A useful habit.</span> Before calculating, write the fixed quantity and the energy pathway. “No heat” does not mean “no temperature change”; adiabatic expansion cools a gas because it does work.</div>
