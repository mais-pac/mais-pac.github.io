# Errata — MAIS Physics & Astronomy Club handouts

**Audit cycle:** 2 (corrections verified)  
**Scope:** Basic Astrophysics 01.01–01.05; Cosmology 06.01; extended curriculum 07.01–10.04; legacy Physics P1–P3 and Astronomy A1–A3; generated figures and interactive laboratories.  
**Method:** source reading, independent numerical recomputation, SVG/reference checks, and interactive-model inspection. External source links are checked for reachability; this is not a re-derivation of every cited official marking scheme.

The table names each finding **Errata E##**. “Fixed” means the source was corrected, the affected HTML/PDF was rebuilt, and the item was re-checked in cycle 2.

## Handout errata

| ID | Location | Finding | Correction | Status |
|---|---|---|---|---|
| E01 | 01.01 lecture §6; solutions 13 | The formula $2GMR/d^3$ was labelled “near–far” differential acceleration. It is the centre-to-near-side difference; the near-to-far difference is $4GMR/d^3$. | Define the centre-to-near convention explicitly and label the Moon/Sun numbers with that convention. | Fixed |
| E02 | 01.03 solution 13 | Photon random-walk time was $1.63\times10^{12}$ s / $5.2\times10^4$ yr, a factor of ten too large. | Correct to $1.63\times10^{11}$ s $\approx5.2\times10^3$ yr for the stated mean free path. | Fixed |
| E03 | 01.04 solution 6 | The quoted 7.96 MHz linewidth was a half-width convention but was not identified as such. | State that $1/(4\pi\tau)$ is the HWHM under the stated convention; the corresponding FWHM is 15.9 MHz. | Fixed |
| E04 | 07.02 §4 and problem 5; 09.04 §2 and problem 1 | SNR formula and worked read-noise term used a per-pixel read noise without stating the aperture pixel count. | Define $S,B,D$ as aperture totals and use $n_{\rm pix}\sigma_{\rm read}^2$; state that the worked numbers assume a one-pixel-equivalent aperture or give the total read variance. | Fixed |
| E05 | 09.01 solution 8 | “Halfway in brightness” was ambiguous and the flux-midpoint magnitude was rounded to 5.2. | Define the arithmetic mean of the two comparison fluxes and give 5.26 mag; note that a magnitude midpoint would be 5.30. | Fixed |
| E06 | 09.03 §4; airmass figure; coordinates lab | Text said the true airmass is larger than $\sec z$ near the horizon, and the lab/figure used the divergent plane-parallel formula there. | Explain that $\sec z$ overestimates/diverges; use the finite Kasten–Young (1989) approximation in the lab and figure, with its low-altitude limits stated. | Fixed |
| E07 | 09.03 problem/solution 10 | The problem asked for information already supplied and the solution omitted the computable azimuth/airmass. | Ask for altitude, azimuth and airmass from the given hour angle, latitude and declination; give 60.86°, 242.8°, 1.145. | Fixed |
| E08 | 09.03 solution 8 | A 30-day sidereal drift was rounded to exactly 20:00. | Use 3 min 56 s per day: about 1 h 58 min earlier, near 20:02. | Fixed |
| E09 | 09.04 problem/solution 9 | “Minimum total observing time” confused 40 min of integration with the elapsed session needed to sample a 2 h eclipse plus baseline. | Separate integration time from elapsed time: 40 min integration, about 4 h session for 2 h eclipse plus 1 h baseline on each side, with ≤6 min eclipse cadence. | Fixed |
| E10 | 09.04 problem 2 | Dark current was omitted without being declared negligible. | State that dark current and read noise are neglected. | Fixed |
| E11 | 09.04 problem 8 | Exposure scaling answer assumed source-dominated noise without saying sky/dark/read terms were negligible. | State the source-dominated assumption explicitly. | Fixed |
| E12 | 09.04 solution 10 | 0.02 mag was described as “about 2%” without the exact conversion. | Give $1-10^{-0.4(0.02)}\approx1.82\%$ (about 2%). | Fixed |
| E13 | 10.04 §5 | A real target eclipse was said to appear in comparison stars “only if it is real,” reversing the control logic. | A real target eclipse should **not** appear in stable comparison stars; a shared dip indicates a systematic. | Fixed |
| E14 | 10.04 differential-photometry discussion | Differential magnitude was treated as an absolute magnitude without a zero-point caveat. | State that $\Delta m$ is relative to the comparison ensemble and needs a zero point for an absolute magnitude. | Fixed |
| E15 | 10.01 §1–3 | “Error” and “uncertainty” were used interchangeably. | Distinguish a mistake/known offset from a quantified uncertainty; known biases are corrected, residual calibration uncertainty is propagated. | Fixed |
| E16 | 08.03 lecture/problems | Unit-vector definition omitted the nonzero condition; flux wording omitted sign/uniform-field assumptions; one problem said “vectors” where “angle” was meant. | Add $\mathbf v\ne0$, define signed flux through an oriented surface in a uniform field, and correct the angle wording. | Fixed |
| E17 | 08.04; 10.03 §3 and solutions | “Finer plate scale” was ambiguous and sometimes inverted. | Define plate scale as $k$ in arcsec/mm: smaller $k$ means more mm per arcsec and a smaller angular error for the same ruler error. | Fixed |
| E18 | 08.04 parallax discussion | The annual parallax baseline was not distinguished from the full peak-to-peak shift. | State that the parsec definition uses the 1 AU radius (half the 2 AU peak-to-peak baseline). | Fixed |
| E19 | 08.05; 10.01 uncertainty budget | Calibration terms were described as random errors to be averaged away. | Treat independent, zero-mean standard uncertainties in quadrature; correlated or known systematic offsets require separate treatment. | Fixed |
| E20 | 10.02 fitting lecture/problems | Ordinary least-squares assumptions and transformations were under-specified. | State equal-variance $y$ errors and $n-2$ degrees of freedom for $s$; logarithms require positive variables; pendulum linearization requires small amplitude. | Fixed |
| E21 | 09.02 catalogue lecture/problems | Epoch and equinox were conflated; a small-angle separation problem omitted its approximation; a 25″ offset in a 1′ field was not contextualized. | Distinguish proper-motion epoch from reference-frame equinox; state same-declination/small-angle assumptions; note 25″ is about 42% of a 1′ field. | Fixed |
| E22 | 08.01 solution 2; numerical integration remark | A Newton iterate was claimed to have three correct digits; Simpson’s rule did not state its even-interval requirement. | Remove the digit overclaim and state that composite Simpson’s rule needs an even number of subintervals. | Fixed |
| E23 | 08.02 calculus lecture | A one-dimensional stationary point was called a saddle; antiderivatives omitted the constant of integration. | Use local maximum/minimum/inflection language for 1-D; write $+C$ for indefinite integrals. | Fixed |
| E24 | 09.01 naked-eye lecture/solutions | Polaris distance was measured from the wrong reference; dark adaptation was said to be fully reset by white light; synthetic field was not labelled. | Use the Dubhe-to-Polaris pointer distance (~28°); say white light undoes much of the adaptation; label the practice field as synthetic. | Fixed |
| E25 | 10.03 procedure/problems | “Centred” typo; resolved-image assumption and constant position-angle rate were implicit. | Correct to “Centre”; state that the method assumes resolved images and that a constant PA rate is an approximation over short arcs. | Fixed |
| E26 | 08.03, 09.03, 10.03 figures | Four SVG arrowheads referenced marker IDs containing underscores while the generated IDs used hyphens. | Normalize marker references and add an automated unresolved-SVG-reference check. | Fixed |
| E27 | 10.02 fit laboratory | The lab promised a residual panel but drew none; negative fitted values could be clipped. | Add a residual subplot and a symmetric, data-aware y-range. | Fixed |
| E28 | 10.04 photometry laboratory | “Recovered depth scale” was only the input slider; deterministic ripple was called noise. | Relabel the output as the input depth scale and describe the ripple as deterministic synthetic scatter. | Fixed |
| E29 | 09.01 limiting-magnitude figure | The figure used a power-law star count while the lecture used the Euclidean $10^{0.6m}$ model. | Label the figure as schematic or align it with the stated model. | Fixed |
| E30 | Extended figures (07.01, 08.01–08.05, 09.01, 09.03, 10.02–10.04) | Several diagrams were geometrically inconsistent or unlabelled schematics: non-tangent “tangent,” mismatched shaded area, triangulation angle labels, vector-add title, distribution normalization, horizon-coordinate angle, double-star north arrow, differential-photometry curves, and wavelength-band spacing. | Redraw/label the affected diagrams so the geometry matches the caption and the teaching model. | Fixed |
| E31 | P1 problem/solution 3 | A local pressure ratio was presented as the fraction of Earth’s whole atmosphere below 1350 m. | Reframe as the fraction of an idealized sea-level air column below that altitude; global mass fraction requires topography. | Fixed |
| E32 | A1 lecture §1 | “Earth moves … on a baseline of 1 AU” blurred the parallax radius and full annual shift. | State that annual parallax uses the 1 AU orbital radius; the peak-to-peak shift is twice the parallax angle. | Fixed |
| E33 | A2 solution 1 | A 13.3 mag idealized limit was said to be “easily bright enough” for Pluto at ~14.3 mag. | Correct the comparison: Pluto is fainter than that limit; larger aperture, detector integration or other gains are needed. | Fixed |
| E34 | A2 lecture §3 | Fusion energy notation double-counted the efficiency if $\Delta m$ was already the converted mass. | Write $E\simeq\epsilon m_{\rm fused}c^2$ for fused mass, or $E=\Delta m c^2$ for actual mass defect. | Fixed |
| E35 | A2 solution 4 | The $M^{-2.5}$ lifetime scaling was extrapolated to a 0.2 $M_\odot$ star without noting the changing mass–luminosity slope and fuel fraction. | Label the 560 Gyr value as the result of the stated crude scaling, not a reliable low-mass stellar model. | Fixed |
| E36 | A3 solution 3 | A $10^{13}L_\odot$ quasar was compared to “a hundred” Milky Way galaxies. | Use a defensible order-of-magnitude comparison (hundreds to about a thousand Milky-Way-like galaxies) or remove the count. | Fixed |
| E37 | A3 lecture §1/§3 | “Isolated black holes are completely dark” and “up to 42%” spin efficiency lacked classical/ideal-limit qualifiers. | Say classically dark apart from negligible Hawking radiation; identify ~42% as the ideal extremal-Kerr estimate, not a generic astrophysical value. | Fixed |
| E38 | 06.01 solution 27(d) | A 2% increase in the BAO ruler $r_d$ was said to increase both $D_M$ and $H$. Since $H=c\Delta z/r_d$, $H$ decreases. | Correct to $D_M$ increases by 2%, $H$ decreases by about 1.96% (to $H/1.02$). | Fixed |
| E39 | 06.01 solution 1(c) | The answer did not name the coasting model that makes $t_0=H_0^{-1}$ exact. | Add the empty Milne / $a\propto t$ example while keeping the warning that $H_0^{-1}$ is not a general age. | Fixed |
| E40 | 08.03 vectors laboratory | The angle between vectors was reported as 90° when either vector had zero magnitude. | Return an undefined angle for a zero vector and display “—”. | Fixed |
| E41 | 10.01 errors laboratory | A known systematic offset was combined with random scatter as though it were automatically a standard uncertainty. | Relabel the RSS output and explain that a known bias should be corrected; only an uncertainty on the residual bias is combined. | Fixed |

## Requested site changes (tracked separately from errata)

| ID | Request | Implementation | Status |
|---|---|---|---|
| S01 | Add a navigation item called **Club**. | Add a Club page and a Club link to every main site navigation and the Teaching template, preserving sticky behavior and mobile wrapping. | Fixed |
| S02 | Remove the Mechanics Playground card from **Explore**. | Delete the Explore feature section and patch `integrate_mechanics.py` so it cannot reinsert it; keep the Mechanics Lab navigation item and page. | Fixed |

## Cycle log

- **Cycle 1:** full source and generated-artifact inspection; 41 handout/figure/lab errata and 2 requested site changes recorded.
- **Cycle 2:** all 41 errata corrected at source; affected HTML and PDFs rebuilt. Structural audit PASS (54 handout HTML files, 9 navigation pages; no unresolved templates, KaTeX errors, duplicate IDs, broken SVG references, broken internal links, or problem/solution count mismatches). Basic, Cosmology, Extended-curriculum and Mechanics browser tests PASS offline/live. SVG text-bounds check PASS. PDF bounds check: 54 PDFs, 285 pages, 0 out-of-bounds text blocks. Club navigation present on all main pages; Explore Mechanics feature card absent. No new errata found in cycle 2.
