"""Authored theory notes and official IOAA problem identifiers for Basic Astrophysics.

Problem statements are intentionally not reproduced: this source keeps only the
exam year, round and question identifier.  The lecture text below is original
MAIS PAC teaching material.
"""

LECTURES = {
    "01.01": {
        "title": "Celestial Mechanics",
        "accent": "#2457C5",
        "subtitle": "From Newton's law of gravity to orbital motion",
        "intro": (
            "This lecture builds orbital mechanics from the ground up. We begin with the force between two masses, "
            "then use conservation laws to understand circular orbits, ellipses, binaries, tidal disruption and the "
            "equilibrium points of a rotating system. Unless stated otherwise, bodies are treated as point masses and "
            "external perturbations are neglected."
        ),
        "outcomes": [
            "Translate Newton's law of gravitation into orbital acceleration and speed.",
            "Use a barycentre to describe two-body and binary-star motion.",
            "Connect Kepler's laws, orbital energy and angular momentum.",
            "Interpret the Roche limit and the five Lagrange points.",
        ],
        "sections": [
            {
                "title": "1 · Gravity is a central force",
                "blocks": [
                    ("text", "Newton's law of universal gravitation says that two point masses attract one another. The force grows with either mass and falls with the square of their separation. It points along the line joining the bodies, so it is a central force."),
                    ("formula", "F = G m₁m₂ / r²     ·     g(r) = GM / r²"),
                    ("text", "Here G = 6.674 × 10⁻¹¹ m³ kg⁻¹ s⁻², r is the separation, F is the magnitude of the force, and g(r) is the gravitational acceleration produced by a central mass M. The force on the smaller body is directed inward. Newton's third law gives an equal and opposite force on the central body; both objects move."),
                    ("callout", "Field and potential", "Outside a spherical, non-rotating body, its gravity is the same as if all its mass were concentrated at its centre. The gravitational potential per unit mass is Φ = −GM/r, chosen to be zero infinitely far away. Potential energy is U = mΦ. The negative sign marks a bound configuration."),
                    ("text", "For an isolated system, the total linear momentum and angular momentum are conserved. These conservation laws are more useful than treating gravity as a memorized list of orbit formulas: they explain why a comet speeds up near its star and why the two stars in a binary share one period."),
                ],
            },
            {
                "title": "2 · The barycentre and the two-body problem",
                "blocks": [
                    ("text", "The centre of mass, or barycentre, is the mass-weighted average position. For two bodies of masses m₁ and m₂ separated by distance r, the barycentre lies on the line between them. If their distances from it are r₁ and r₂, then m₁r₁ = m₂r₂ and r₁ + r₂ = r."),
                    ("formula", "r₁ = [m₂ / (m₁ + m₂)] r     ·     r₂ = [m₁ / (m₁ + m₂)] r"),
                    ("text", "The more massive body is closer to the barycentre. A planet does not sit perfectly still while a satellite orbits it; the planet and satellite both orbit their common barycentre. For a binary star, measuring both orbital sizes and the period can reveal the mass ratio and total mass."),
                    ("callout", "Relative motion", "Instead of following both position vectors separately, define the separation vector r = r₂ − r₁. The relative coordinate obeys the same inverse-square orbit equation as a test particle around a central mass M = m₁ + m₂. For a circular binary with separation a, the period is P² = 4π²a³/[G(m₁ + m₂)]."),
                    ("text", "A useful physical check is that the two bodies have the same angular speed and period, but not the same linear speed. Since v₁/v₂ = r₁/r₂ = m₂/m₁, the lighter object moves on the larger, faster orbit."),
                ],
            },
            {
                "title": "3 · Circular orbits, orbital periods and escape",
                "blocks": [
                    ("text", "In a circular orbit, gravity supplies the centripetal acceleration. Equating GM/r² with v²/r gives the orbital speed. The period follows by dividing the orbit's circumference by that speed."),
                    ("formula", "v_circ = √(GM/r)     ·     P = 2π√[r³/(GM)]"),
                    ("text", "The formulas assume a negligible-mass satellite orbiting a central mass M. For two comparable masses, replace M by m₁ + m₂ and use their separation as the relative-orbit radius. The third-law form P² ∝ a³ means that distant orbits take much longer: doubling a increases the period by 2^(3/2), not by two."),
                    ("formula", "E = K + U = −GMm/(2r)     ·     v_esc = √(2GM/r) = √2 v_circ"),
                    ("text", "A circular orbit is bound because its total mechanical energy is negative. Escape speed is the launch speed for which the final speed approaches zero at infinity, with no further propulsion or energy loss. It is larger than circular speed at the same radius by √2. An orbiting astronaut is not beyond gravity; the astronaut and spacecraft are in continuous free fall together."),
                    ("callout", "Dimensional and limiting checks", "GM/r has units of m² s⁻², so its square root is a speed. Increasing M raises orbital speed; increasing r lowers it. Escape speed tends to zero far from the mass. These checks catch many algebra and unit errors."),
                ],
            },
            {
                "title": "4 · Ellipses and Kepler's laws",
                "blocks": [
                    ("text", "A gravitationally bound orbit is an ellipse with the attracting mass at one focus. The closest point is periapsis and the farthest is apoapsis; for a star, the names are periastron and apastron. The semimajor axis a is half the longest diameter, and eccentricity e measures how stretched the ellipse is, from e = 0 for a circle to e < 1 for a bound ellipse."),
                    ("formula", "r_peri = a(1 − e)     ·     r_apo = a(1 + e)"),
                    ("text", "Kepler's first law describes the ellipse. His second law says that the line from the focus to the orbiting body sweeps out equal areas in equal times. Gravity exerts no torque about the focus, so angular momentum is conserved; the body must move faster when it is closer in order to sweep the same area."),
                    ("formula", "dA/dt = constant     ·     v² = GM(2/r − 1/a)"),
                    ("text", "The second expression is the vis-viva equation. At periapsis and apoapsis the velocity is perpendicular to the radius, so it also follows that v_peri/v_apo = r_apo/r_peri. Kepler's third law relates period to semimajor axis: P² = 4π²a³/(GM) for a negligible-mass orbiting body, or with M = m₁ + m₂ for the relative orbit of two bodies."),
                    ("callout", "Energy viewpoint", "For any bound two-body Kepler orbit, total orbital energy depends on a, not on the body's location along the ellipse: E = −GMm/(2a). At periapsis kinetic energy is greatest and gravitational potential energy is lowest; at apoapsis the reverse is true."),
                ],
            },
            {
                "title": "5 · Tides, the Roche limit and Lagrange points",
                "blocks": [
                    ("text", "A planet's pull is stronger on the near side of a moon than on its far side. This difference in gravitational acceleration is a tidal force. A self-gravitating moon can remain intact only if its own gravity and material strength can resist the differential pull. A fluid satellite can be disrupted inside an approximate Roche distance."),
                    ("formula", "d_Roche ≈ 2.44 R_p (ρ_p / ρ_s)^(1/3)"),
                    ("text", "Here R_p and ρ_p are the planet's radius and density, and ρ_s is the satellite's density. This coefficient applies to an ideal fluid satellite in a simplified circular orbit; rigidity, spin, internal structure and orbital eccentricity change the result. The key trend is robust: a larger density contrast pushes the disruption distance outward."),
                    ("text", "In a frame rotating with a two-body system, centrifugal effects combine with the two gravitational fields. The five Lagrange points are locations where the net effective force on a small test object is zero in that rotating frame. L1 lies between the two masses; L2 beyond the smaller mass; L3 on the far side of the larger mass; L4 and L5 lead and trail the smaller mass by 60 degrees."),
                    ("callout", "Equilibrium is not the same as stability", "L1, L2 and L3 are saddle points: a small displacement in some directions grows. L4 and L5 can be stable when μ = m₂/(m₁ + m₂) is below about 0.0385. The Sun–Jupiter and Earth–Moon systems satisfy this idealized condition. Real perturbations and radiation pressure can still alter a particle's motion."),
                ],
            },
            {
                "title": "6 · A reliable orbital calculation",
                "blocks": [
                    ("text", "First draw the geometry and decide which distance is meant: altitude above a surface, distance from a centre, or separation between two orbiting bodies. Convert all quantities to SI units. Then identify whether the orbit is circular, elliptical or a two-body relative orbit, and state the mass that belongs in Kepler's law."),
                    ("text", "Use conservation of energy for speed changes and escape, angular momentum for areal motion and periapsis-to-apoapsis comparisons, and the barycentre for binary sizes. Keep intermediate units: a period computed from SI values emerges in seconds. Round only at the end, and test the answer against a limiting case such as e → 0 or m₂ ≪ m₁."),
                    ("callout", "Model limits", "Kepler's two-body model is an approximation. Additional planets, non-spherical mass distributions, atmospheric drag, radiation pressure and relativistic corrections can perturb real trajectories. In introductory IOAA-style calculations, the statement normally tells you when those effects may be ignored."),
                ],
            },
        ],
        "problem_ids": [
            (2007, "TH", "1.6"), (2007, "TH", "1.7"),
            (2009, "TH", "P3"), (2009, "TH", "P6"), (2009, "TH", "P12"), (2009, "TH", "P14"),
            (2010, "TH", "S6"), (2011, "TH", "S1"), (2011, "TH", "S3"),
            (2014, "TH", "P1"), (2014, "TH", "L3"),
            (2015, "TH", "S1"), (2015, "TH", "S5"), (2015, "TH", "S13"),
            (2016, "TH", "T9"), (2019, "TH", "9"),
            (2021, "TH", "Q3"), (2021, "TH", "Q9"), (2021, "TH", "Q11"), (2021, "TH", "Q12"),
            (2022, "TH", "8"), (2022, "TH", "12"), (2023, "TH", "Q12"), (2024, "TH", "T3"),
        ],
    },
    "01.02": {
        "title": "Electromagnetic Theory & Quantum Physics",
        "accent": "#7540B8",
        "subtitle": "Light, radiation and the quantum packet",
        "intro": (
            "Astronomy is built from light: nearly everything we know about a distant object arrives as electromagnetic "
            "radiation. This lecture starts with waves and photons, develops flux and luminosity, and derives the "
            "blackbody laws used to infer temperatures and energy output."
        ),
        "outcomes": [
            "Move between wavelength, frequency and photon energy.",
            "Distinguish luminosity, flux and intensity at an observing distance.",
            "Use Planck, Wien and Stefan–Boltzmann laws in their proper roles.",
            "Explain the quantum meaning of radiation and the photoelectric threshold.",
        ],
        "sections": [
            {
                "title": "1 · Electromagnetic waves and the spectrum",
                "blocks": [
                    ("text", "An electromagnetic wave is a changing electric field and magnetic field that carries energy through space. In vacuum every frequency travels at the speed of light c = 2.998 × 10⁸ m s⁻¹. Wavelength λ is the distance between successive wave crests; frequency ν is the number of cycles passing a point per second."),
                    ("formula", "c = λν"),
                    ("text", "The electromagnetic spectrum is ordered by wavelength or, equivalently, by frequency: radio, microwave, infrared, visible, ultraviolet, X-ray and gamma ray. Shorter wavelength means higher frequency and greater photon energy. The boundaries between bands are conventional, not physical discontinuities."),
                    ("callout", "Astronomical meaning", "Different wavelengths reveal different physical conditions. Cool dust is prominent in the infrared; neutral hydrogen emits a famous radio line near 21 cm; hot gas can shine in X-rays. Earth's atmosphere transmits some windows well and blocks much of the ultraviolet, X-ray and gamma-ray sky."),
                    ("text", "A measured wavelength is often quoted in nanometres (1 nm = 10⁻⁹ m), micrometres (1 μm = 10⁻⁶ m) or centimetres. Convert to metres before using SI constants, unless the formula is deliberately written in matching units."),
                ],
            },
            {
                "title": "2 · Photons: the quantum of electromagnetic energy",
                "blocks": [
                    ("text", "Quantum physics assigns electromagnetic radiation energy in packets called photons. A photon has no rest mass, but it carries energy and momentum. The energy depends on frequency, not on how many photons are present."),
                    ("formula", "E_γ = hν = hc/λ     ·     p_γ = h/λ"),
                    ("text", "Planck's constant is h = 6.626 × 10⁻³⁴ J s. A useful conversion is hc ≈ 1240 eV nm, so a photon of wavelength λ in nanometres has energy E in electronvolts given by E(eV) ≈ 1240/λ(nm). One electronvolt is 1.602 × 10⁻¹⁹ joule."),
                    ("callout", "Intensity versus photon energy", "Increasing the intensity of a monochromatic beam usually increases the number of photons arriving per second; it does not change the energy of each photon. Changing the wavelength changes each photon's energy. Keep these ideas separate when reasoning about detectors and the photoelectric effect."),
                    ("text", "In the photoelectric effect, one photon gives energy hν to one electron. If the photon energy exceeds a material's work function φ, the electron can escape; the maximum kinetic energy is K_max = hν − φ. Below the threshold frequency ν₀ = φ/h, increasing intensity alone cannot eject electrons in the ideal one-photon model."),
                ],
            },
            {
                "title": "3 · Luminosity and flux: source power versus received power",
                "blocks": [
                    ("text", "Luminosity L is the total radiant energy emitted by a source per second, measured in watts. Flux F is energy arriving per second per unit area, also measured in W m⁻². For an isotropic source, its power spreads over larger and larger spherical surfaces as the distance grows."),
                    ("formula", "F(r) = L / (4πr²)     ·     L = 4πr²F"),
                    ("text", "This inverse-square law does not mean the star's luminosity decreases with distance; it means the same emitted power is distributed over an area proportional to r². If distance doubles, flux falls by a factor of four. Interstellar absorption or beaming can change the measured flux from the simple isotropic prediction."),
                    ("callout", "Observed band and bolometric output", "A detector usually measures only a wavelength interval. Bolometric flux is the total flux integrated over all wavelengths. A source can be bright in one band and faint in another, so state whether a flux or luminosity is monochromatic, band-limited or bolometric."),
                    ("text", "For a spherical star, surface area is 4πR². If the emitted surface flux is F_surface, its luminosity is L = 4πR²F_surface. This connects measurements at Earth to the physical size and temperature of the emitting surface."),
                ],
            },
            {
                "title": "4 · Thermal radiation and the blackbody model",
                "blocks": [
                    ("text", "A blackbody is an ideal object that absorbs all incident radiation and emits a spectrum determined only by its temperature. Real stars are not perfect blackbodies, but their broad continua are often close enough for a first estimate. The Planck distribution describes how energy is spread across wavelength."),
                    ("formula", "B_λ(T) = [2hc²/λ⁵] · 1/[exp(hc/(λk_BT)) − 1]"),
                    ("text", "In this expression B_λ is spectral radiance per unit wavelength and solid angle, and k_B = 1.381 × 10⁻²³ J K⁻¹. The full formula need not be evaluated in every problem. Its two most useful consequences are Wien's displacement law and the Stefan–Boltzmann law."),
                    ("formula", "λ_max T = b     ·     F_surface = σT⁴     ·     L = 4πR²σT⁴"),
                    ("text", "Wien's constant is b = 2.898 × 10⁻³ m K. Hotter blackbodies peak at shorter wavelengths. The Stefan–Boltzmann constant is σ = 5.670 × 10⁻⁸ W m⁻² K⁻⁴; total emitted surface flux rises very steeply with temperature. If radius is fixed and temperature doubles, luminosity increases by 2⁴ = 16."),
                    ("callout", "Choosing the right law", "Use Wien's law to connect temperature with the peak wavelength. Use Stefan–Boltzmann to relate temperature to total emitted flux or luminosity. Use Planck's law when a question asks for a spectrum at a specific wavelength. These are related laws, but they answer different questions."),
                ],
            },
            {
                "title": "5 · Radiation pressure and energy transport",
                "blocks": [
                    ("text", "Radiation carries momentum as well as energy. When a beam of flux F is completely absorbed by a surface, its radiation pressure is F/c; for ideal reflection the momentum change doubles and the pressure is 2F/c. For most planets and ordinary stars, gravity dominates the motion of large bodies, but radiation pressure can matter for dust grains and very luminous stars."),
                    ("formula", "P_rad = F/c  (absorption)     ·     P_rad = 2F/c  (ideal reflection)"),
                    ("text", "Radiation can move energy through empty space, while conduction requires material contact and convection transports energy through bulk fluid motion. In a star, photons can be absorbed and re-emitted many times before escaping; the surface spectrum therefore reflects the outer layers, not an instantaneous view of the core."),
                    ("callout", "A useful three-step measurement", "(1) Infer a colour or peak wavelength. (2) Estimate temperature with Wien's law. (3) Combine the temperature with a radius or flux measurement through Stefan–Boltzmann and the inverse-square law. Check that every quantity refers to the same wavelength coverage and distance."),
                ],
            },
        ],
        "problem_ids": [
            (2007, "TH", "1.8"), (2007, "TH", "1.9"), (2007, "TH", "1.10"), (2007, "TH", "1.11"), (2007, "TH", "1.15"),
            (2008, "TH", "L2"), (2009, "TH", "P2"), (2010, "TH", "S1"),
            (2011, "TH", "S8"), (2011, "TH", "S9"), (2012, "TH", "S9"), (2012, "TH", "L1"),
            (2013, "TH", "S13"), (2014, "TH", "P7"), (2014, "TH", "P8"), (2014, "TH", "P9"),
            (2015, "TH", "S6"), (2015, "TH", "S8"), (2017, "TH", "T4"), (2017, "TH", "T6"),
            (2018, "TH", "T6"), (2019, "TH", "5"), (2021, "TH", "Q4"), (2022, "TH", "11"),
            (2023, "TH", "Q2"), (2025, "TH", "T04"),
        ],
    },
    "01.03": {
        "title": "Thermodynamics",
        "accent": "#0C8275",
        "subtitle": "Temperature, energy and equilibrium in astronomical systems",
        "intro": (
            "Thermodynamics describes the macroscopic state of matter and how energy is stored and transferred. "
            "Starting with temperature, pressure and the ideal gas, we build the first law, common gas processes, "
            "radiative balance and the three ways energy moves through an astrophysical environment."
        ),
        "outcomes": [
            "Distinguish temperature, heat, internal energy and work.",
            "Use the ideal-gas law and first law with a consistent sign convention.",
            "Analyze isothermal, isochoric, isobaric and adiabatic changes.",
            "Set up radiative equilibrium and compare energy-transport mechanisms.",
        ],
        "sections": [
            {
                "title": "1 · Thermodynamic states and equilibrium",
                "blocks": [
                    ("text", "A thermodynamic system contains many particles, but it can often be described by a few measurable state variables. For a gas these include pressure P, volume V, temperature T and amount of matter. Pressure is force per unit area; temperature measures the thermal state and determines the direction in which energy flows when two systems are brought into contact."),
                    ("callout", "Thermal equilibrium", "Two systems in thermal equilibrium have no net heat flow between them when placed in contact. Temperature is the property that is equal at equilibrium. Heat is not a substance stored inside an object; it is energy crossing a boundary because of a temperature difference."),
                    ("text", "An equation of state connects state variables. The ideal-gas model assumes particles are small compared with their separations, move randomly, and interact mainly through brief elastic collisions. It is a good approximation for a dilute gas when the mean particle spacing is large compared with the interaction scale."),
                    ("formula", "PV = Nk_BT = nRT"),
                    ("text", "N is the number of particles, k_B is Boltzmann's constant, n is the amount in moles, and R = 8.314 J mol⁻¹ K⁻¹. Use kelvins, not degrees Celsius, in gas-law ratios. If N is fixed, doubling the absolute temperature at fixed volume doubles pressure."),
                ],
            },
            {
                "title": "2 · Internal energy, work and the first law",
                "blocks": [
                    ("text", "Internal energy U is microscopic energy stored in random motion and interactions of a system's particles. For a monatomic ideal gas, the internal energy is entirely translational kinetic energy and depends only on temperature. Heat Q and work W are two ways energy can cross the system boundary."),
                    ("formula", "U = (3/2)Nk_BT = (3/2)nRT   (monatomic ideal gas)"),
                    ("callout", "Sign convention used here", "Q is positive when energy enters the gas as heat. W is positive when the gas does work on its surroundings. With this convention the first law is ΔU = Q − W, or Q = ΔU + W. Some textbooks choose work done on the gas as positive; always state the convention before substituting signs."),
                    ("text", "For a quasi-static pressure change, work done by the gas is W = ∫P dV: the area under a pressure–volume curve. Expansion has positive W; compression has negative W. At constant pressure, W = PΔV. At fixed volume, no boundary work is done."),
                    ("formula", "ΔU = Q − W     ·     W = ∫ P dV"),
                    ("text", "For an ideal gas, a change in internal energy depends on the temperature change, not on the path. The heat needed to cause that change does depend on the path because different processes do different amounts of work."),
                ],
            },
            {
                "title": "3 · The four standard gas processes",
                "blocks": [
                    ("text", "An isochoric process keeps volume constant: W = 0, so all added heat changes internal energy. An isobaric process keeps pressure constant: the gas can expand and do work PΔV. An isothermal process keeps temperature constant; for an ideal gas ΔU = 0, so heat entering the gas equals the work it performs."),
                    ("formula", "Isochoric: V constant, W = 0     ·     Isobaric: P constant, W = PΔV"),
                    ("formula", "Isothermal ideal gas: T constant, ΔU = 0, Q = W"),
                    ("text", "An adiabatic process exchanges no heat with the surroundings, Q = 0. A reversible adiabatic change of an ideal gas satisfies PV^γ = constant, with γ = C_P/C_V. For a monatomic ideal gas γ = 5/3. Expansion cools the gas because it does work while no heat is supplied."),
                    ("callout", "Molecular heat capacity", "For a monatomic ideal gas C_V = 3R/2 and C_P = 5R/2 per mole, so C_P − C_V = R. The extra heat at constant pressure is needed partly to raise internal energy and partly to do expansion work. More complex molecules store energy in rotational and vibrational modes as well."),
                    ("text", "A good calculation method is to identify the process first, write what stays fixed, then apply the equation of state and first law. Do not assume Q = ΔU: that is only true when no work is done."),
                ],
            },
            {
                "title": "4 · Radiative equilibrium: an astronomical energy balance",
                "blocks": [
                    ("text", "A planet intercepts starlight over its projected disk, area πR², but emits thermal radiation over its entire spherical surface, area 4πR². Let the incident stellar flux at the planet be F and the Bond albedo be A, the fraction of incoming power reflected back to space. In a simple uniform-temperature model, absorbed and emitted powers balance."),
                    ("formula", "(1 − A) F πR² = 4πR² σT⁴     ⇒     T = [(1 − A)F/(4σ)]^(1/4)"),
                    ("text", "The radius cancels. The factor of four comes from comparing the illuminated disk to the full sphere; it is not an arbitrary correction. If the planet radiates only on its day side, has strong temperature contrasts, an atmosphere, internal heat or wavelength-dependent emissivity, this simple effective temperature is not the local surface temperature."),
                    ("formula", "For a star: F = L/(4πd²)     ·     For a blackbody surface: F_surface = σT⁴"),
                    ("callout", "Greenhouse warming", "An atmosphere can absorb outgoing infrared radiation and emit it both upward and downward. This changes the relation between the planet's effective radiating temperature and its surface temperature. The energy balance still applies to the whole planet at the top of the atmosphere, but the surface need not behave as a bare blackbody."),
                ],
            },
            {
                "title": "5 · How energy moves: conduction, convection and radiation",
                "blocks": [
                    ("text", "Conduction transfers energy through microscopic interactions between neighboring particles. It is important in solids and across thin interfaces. In a fluid, convection transports energy when warmer, often less-dense material moves and cooler material replaces it. The rising parcel can continue upward if it remains buoyant compared with its surroundings."),
                    ("text", "Radiation transfers energy through photons and does not require matter in between. A temperature gradient drives net radiative flow because hotter regions emit more energy and the radiation field is not balanced in every direction. In an optically thick stellar interior, photons are repeatedly absorbed and re-emitted; near a transparent surface, radiation can escape."),
                    ("callout", "Optical depth", "Optical depth is a measure of how difficult it is for radiation to pass through a medium. Small optical depth means the medium is mostly transparent; large optical depth means photons are likely to interact many times. The photosphere is the layer from which most of the visible light we observe escapes."),
                    ("text", "In many stars, radiation transports energy through some layers and convection through others. Which mechanism dominates depends on opacity, temperature gradient, density and the way energy is produced. A complete stellar model uses local balance laws; qualitative problems often ask only which transport mechanism is plausible and why."),
                ],
            },
            {
                "title": "6 · Thermal time scales and model checks",
                "blocks": [
                    ("text", "A time scale compares an energy reservoir with the rate at which energy is lost or supplied. If a body contains usable thermal or gravitational energy E and radiates with luminosity L, a characteristic time is t ≈ E/L. For a star, the Kelvin–Helmholtz estimate compares gravitational binding energy with luminosity and is of order GM²/(RL)."),
                    ("text", "This is not a prediction that a real star must contract uniformly: nuclear energy can replenish the radiated energy, and the star can settle into hydrostatic and thermal equilibrium. The estimate is a useful comparison, not a replacement for stellar structure equations."),
                    ("callout", "Checklist", "Keep temperature in kelvins, distinguish flux from total luminosity, and track the surface area over which power is absorbed or emitted. On a P–V diagram, expansion work is the signed area under the path. Check energy conservation with ΔU = Q − W before judging whether a result is physically plausible."),
                ],
            },
        ],
        "problem_ids": [
            (2007, "TH", "1.9"), (2007, "TH", "Q2"), (2008, "TH", "S4"), (2008, "TH", "S9"),
            (2010, "TH", "S5"), (2010, "TH", "S12"), (2012, "TH", "S7"),
            (2013, "TH", "S1"), (2013, "TH", "S3"), (2014, "TH", "P7"), (2014, "TH", "P8"),
            (2014, "TH", "P10"), (2014, "DA", "D2"), (2015, "TH", "L3"), (2015, "TH", "S9"),
            (2016, "TH", "T2"), (2019, "TH", "5"), (2020, "TH", "2"), (2021, "TH", "Q2"),
            (2022, "TH", "5"), (2022, "TH", "11"), (2023, "TH", "Q4"),
        ],
    },
    "01.04": {
        "title": "Spectroscopy and Atomic Physics",
        "accent": "#C23C68",
        "subtitle": "Reading the fingerprints carried by starlight",
        "intro": (
            "Spectroscopy turns light into evidence about atoms, motion, temperature and material between the stars. "
            "This lecture builds the atomic picture first, then explains continua and spectral lines, Doppler shifts, "
            "line broadening and polarization."
        ),
        "outcomes": [
            "Explain how quantized atomic energies create absorption and emission lines.",
            "Recognize continuum, emission-line and absorption-line spectra.",
            "Infer line-of-sight velocity from a Doppler shift and state the limits.",
            "Separate line shifts from broadening and describe common broadening mechanisms.",
            "Use polarization as a clue to scattering and source geometry.",
        ],
        "sections": [
            {
                "title": "1 · Atoms, energy levels and photons",
                "blocks": [
                    ("text", "An atom contains a small, positively charged nucleus surrounded by electrons. Quantum mechanics allows an electron in an atom to occupy only certain energy states. The allowed energies depend on the element and its physical environment. A transition between two states must exchange a photon whose energy matches the energy difference."),
                    ("formula", "|ΔE| = hν = hc/λ"),
                    ("text", "When an electron moves to a higher-energy state, the atom absorbs a photon. When it moves to a lower-energy state, the atom emits a photon. Since each element has its own pattern of energy levels, its set of spectral lines acts like a fingerprint. Ionization, pressure and magnetic fields can modify the pattern."),
                    ("callout", "Wavelength and energy", "A larger transition energy corresponds to a higher-frequency, shorter-wavelength photon. Use E(eV) ≈ 1240/λ(nm) as a convenient conversion. The same transition has the same rest wavelength in emission and absorption, although its observed wavelength can be shifted by motion or altered by the source environment."),
                ],
            },
            {
                "title": "2 · Continuous spectra, emission lines and absorption lines",
                "blocks": [
                    ("text", "A hot, dense object produces a broad, nearly continuous spectrum because many interactions blend together. A thin, hot gas can produce bright emission lines at particular wavelengths. If a continuous source is viewed through a cooler, thinner gas, atoms in the gas remove photons at selected wavelengths and create dark absorption lines."),
                    ("callout", "Three idealized spectral situations", "Dense hot material → continuous spectrum. Thin hot gas against a dark background → emission lines. Continuous light passing through cooler gas → absorption lines. Real stars combine these effects: a photospheric continuum is modified by absorption in their atmospheres, and hot outer gas can add emission."),
                    ("text", "A spectrum is a plot of intensity against wavelength or frequency. The continuum shape carries information about temperature and extinction; line positions identify elements and reveal motion; line depths and ratios depend on temperature, density, ionization and the number of atoms along the path."),
                    ("text", "A line is not a perfectly narrow spike. Atoms move, collide and have finite lifetimes, while telescopes and spectrographs have finite resolving power. These effects spread the signal over a small range of wavelength."),
                ],
            },
            {
                "title": "3 · Doppler shifts: motion along the line of sight",
                "blocks": [
                    ("text", "If a source moves toward or away from an observer, the spacing of its wave crests changes. For speeds much smaller than c, the fractional wavelength shift is approximately the radial velocity divided by c. Define Δλ = λ_observed − λ_rest. With this convention positive radial velocity means recession and a redshift; negative means approach and a blueshift."),
                    ("formula", "v_r/c ≈ Δλ/λ_rest     ·     Δν/ν_rest ≈ −v_r/c"),
                    ("text", "A single spectral shift measures only the component of velocity along the line of sight. It cannot reveal the transverse motion without other information such as proper motion. For speeds comparable to c, the classical approximation fails and a relativistic Doppler relation is needed."),
                    ("callout", "Avoid sign confusion", "Always write down the rest wavelength and compute observed minus rest before interpreting the sign. A line observed at a longer wavelength is redshifted and, in the low-speed approximation, the source is receding. A shift of a whole line profile is different from the line merely becoming wider."),
                ],
            },
            {
                "title": "4 · Why spectral lines broaden",
                "blocks": [
                    ("text", "Thermal Doppler broadening comes from random motions of emitting or absorbing atoms: atoms moving toward us contribute slightly shorter wavelengths and atoms moving away contribute slightly longer wavelengths. Higher gas temperature produces a broader distribution of velocities. Turbulent motions can add another Doppler contribution."),
                    ("text", "Pressure or collisional broadening occurs when close encounters perturb atomic energy levels and shorten the time an atom emits or absorbs coherently. Natural broadening follows from the finite lifetime of an excited state. Rotation broadens a stellar line because one limb approaches while the other recedes. Instrumental broadening is imposed by the spectrograph and detector."),
                    ("formula", "Resolving power R = λ/Δλ"),
                    ("text", "Here Δλ is the smallest wavelength separation the instrument can distinguish near λ. A larger R means finer spectral resolution. If a line is Doppler-broadened by a characteristic speed v, its fractional width is roughly Δλ/λ ≈ v/c, but exact definitions depend on the width convention and line profile."),
                    ("callout", "Shift versus width", "A common velocity of the whole source shifts the line centre. A spread of velocities broadens the line. A line may be shifted and broadened at the same time; fit or inspect the centre and width separately."),
                ],
            },
            {
                "title": "5 · Scattering and polarization",
                "blocks": [
                    ("text", "Light is a transverse electromagnetic wave: its electric field oscillates perpendicular to its direction of travel. Unpolarized light has electric-field directions that vary without a preferred orientation. A linear polarizer transmits one orientation and absorbs or rejects the perpendicular component."),
                    ("formula", "Malus's law: I = I₀ cos²θ"),
                    ("text", "Malus's law applies when the incident beam is already linearly polarized and θ is the angle between its polarization direction and the analyzer axis. Unpolarized light passing through an ideal first polarizer has average intensity I₀/2. Scattering can polarize light because the scattered intensity depends on the direction of the electric-field oscillation relative to the scattering geometry."),
                    ("callout", "Astronomical use", "Polarization can reveal scattering by dust, reflection from a surface, magnetic-field geometry or an asymmetric source. It is a vector property of light, so the instrument's orientation and the sky position angle matter. Ordinary intensity alone does not specify polarization."),
                ],
            },
            {
                "title": "6 · A practical spectrum-reading workflow",
                "blocks": [
                    ("text", "Calibrate wavelength using known reference lines, subtract the detector background, and identify the continuum before measuring lines. Compare candidate rest wavelengths in a consistent unit. For a small shift, calculate Δλ/λ_rest, multiply by c, and state whether the result is radial velocity, line width or instrumental resolution."),
                    ("text", "Use multiple lines when possible: a single feature can be misidentified, blended or affected by calibration error. Compare line ratios only after checking that the lines are not saturated and that dust extinction has been considered. Report uncertainties and significant figures that match the data."),
                    ("callout", "What a spectrum cannot say by itself", "A spectrum does not automatically give the full three-dimensional velocity, distance or unique temperature. Those inferences need a model, additional observables or independent data. Distinguish a directly measured quantity from a quantity inferred under assumptions."),
                ],
            },
        ],
        "problem_ids": [
            (2007, "TH", "1.8"), (2007, "TH", "1.12"), (2008, "TH", "L2"), (2009, "TH", "P2"),
            (2012, "TH", "S9"), (2013, "TH", "S13"), (2014, "TH", "P7"), (2014, "TH", "P8"),
            (2015, "TH", "S6"), (2015, "TH", "S8"), (2015, "DA", "D2"), (2016, "TH", "T8"),
            (2017, "TH", "T4"), (2018, "TH", "T6"), (2019, "TH", "5"), (2021, "TH", "Q4"),
            (2023, "TH", "Q2"), (2025, "TH", "T04"),
        ],
    },
    "01.05": {
        "title": "Nuclear Physics",
        "accent": "#C16A20",
        "subtitle": "The atomic nucleus, binding energy, radioactivity and stellar reactions",
        "intro": (
            "Nuclear physics explains how the nucleus is assembled, why reactions release energy and how unstable "
            "nuclei decay. The same ideas power stars, produce neutrinos and set the composition of the universe. "
            "This lecture begins with nuclear notation and mass–energy, then develops binding, decay and stellar fusion."
        ),
        "outcomes": [
            "Read proton, neutron and nucleon numbers from a nuclide symbol.",
            "Relate mass defect to nuclear binding energy and reaction energy.",
            "Use the exponential decay law, half-life and activity consistently.",
            "Describe fusion, fission and the role of neutrinos in stellar physics.",
        ],
        "sections": [
            {
                "title": "1 · The nucleus and the language of nuclides",
                "blocks": [
                    ("text", "An atom consists of a nucleus and electrons. The nucleus contains protons, with positive electric charge, and neutrons, which have no electric charge. The atomic number Z is the number of protons and identifies the element. The neutron number is N; the mass number A counts all nucleons, so A = Z + N."),
                    ("formula", "Nuclide label: mass number A, proton number Z     ·     N = A − Z"),
                    ("text", "Nuclides of one element with different neutron numbers are isotopes. The atomic mass in a periodic table is usually a weighted average over naturally occurring isotopes, not the mass of one nucleus. For nuclear calculations, use masses from a consistent convention and track whether the quoted value includes electrons."),
                    ("callout", "Forces inside the nucleus", "The strong nuclear interaction binds nearby nucleons and overcomes the electric repulsion between protons at short distances. The strong force is attractive over a limited range and becomes repulsive at very short separation. Nuclear radius grows approximately as R ≈ r₀A^(1/3), with r₀ about 1.2 femtometres."),
                ],
            },
            {
                "title": "2 · Mass defect and binding energy",
                "blocks": [
                    ("text", "A bound nucleus has less mass than the same protons and neutrons separated far apart. The missing mass is the mass defect. The energy equivalent of that mass is the binding energy: it is the energy that would have to be supplied to separate the nucleus completely into its constituent nucleons."),
                    ("formula", "Δm = Zm_p + Nm_n − m_nucleus     ·     E_bind = Δm c²"),
                    ("text", "The conversion factor 1 atomic mass unit × c² is approximately 931.5 MeV. Binding energy is commonly quoted per nucleon, E_bind/A, to compare nuclei of different sizes. A larger binding energy per nucleon generally means a more tightly bound nucleus, although stability also depends on proton-to-neutron balance."),
                    ("callout", "Mass conventions matter", "If neutral atomic masses are used, the electron masses must be handled consistently. In many reaction equations the electron numbers cancel on both sides, making atomic masses convenient. Never subtract a nuclear mass from an atomic mass without checking what each number includes."),
                    ("text", "The binding-energy-per-nucleon curve rises rapidly for light nuclei, peaks near iron and nickel, and declines slowly for very heavy nuclei. This pattern explains why combining light nuclei (fusion) and splitting very heavy nuclei (fission) can release energy."),
                ],
            },
            {
                "title": "3 · Nuclear reactions, fusion and fission",
                "blocks": [
                    ("text", "A nuclear reaction must conserve electric charge, total nucleon number and energy–momentum. It also obeys additional particle-number rules, such as lepton-number conservation in weak interactions. Write every reactant and product explicitly before comparing masses."),
                    ("formula", "Q = (m_initial − m_final)c²"),
                    ("text", "A positive Q means the final products have less rest mass and the difference can emerge as kinetic energy, radiation or energy carried by neutrinos. A negative Q reaction requires energy input. One atomic mass unit corresponds to about 931.5 MeV; 1 MeV = 1.602 × 10⁻¹³ J."),
                    ("text", "Fusion joins light nuclei. In stars, the net conversion of four protons into a helium-4 nucleus releases energy through a chain of reactions; positrons and electron neutrinos are also produced. Fission splits a heavy nucleus into smaller fragments, often releasing neutrons and energy. The detailed reaction path depends on temperature, density and composition."),
                    ("callout", "Why fusion can release energy", "The helium nucleus is more tightly bound per nucleon than hydrogen. The final bound products therefore have less total rest mass than the starting particles. The mass difference is not destroyed; it appears as released energy according to E = mc²."),
                ],
            },
            {
                "title": "4 · Radioactivity and the decay clock",
                "blocks": [
                    ("text", "An unstable nucleus can transform spontaneously into a more stable configuration. Radioactive decay is probabilistic for an individual nucleus, but a large sample follows a predictable exponential law. The decay constant λ is the probability per unit time for a nucleus to decay."),
                    ("formula", "N(t) = N₀e^(−λt)     ·     t₁/₂ = ln 2 / λ"),
                    ("text", "The half-life t₁/₂ is the time for half of the undecayed nuclei to remain. After n half-lives, the remaining fraction is (1/2)^n. Half-life does not depend on how much of the sample you start with or on ordinary changes in temperature and pressure."),
                    ("formula", "Activity: A = λN     ·     1 becquerel = 1 decay s⁻¹"),
                    ("text", "Activity is the rate of decays in the sample; it decreases with time along with N. To estimate an age, compare a measured parent-to-daughter ratio or remaining parent fraction with a known decay law, while accounting for any daughter material present at formation and any later gains or losses."),
                    ("callout", "Common radioactive emissions", "Alpha decay emits a helium-4 nucleus; beta-minus decay converts a neutron into a proton, electron and antineutrino; beta-plus decay converts a proton into a neutron, positron and neutrino; gamma emission releases a high-energy photon as a nucleus loses excitation energy. Conservation laws determine the balanced reaction equation."),
                ],
            },
            {
                "title": "5 · Nuclear energy in stars",
                "blocks": [
                    ("text", "A star's core is hot and dense enough for some nuclei to approach closely despite electric repulsion. Quantum tunnelling allows fusion even when the typical thermal energy is below the classical Coulomb barrier. The proton–proton chain is the main hydrogen-fusion pathway in Sun-like stars; the carbon–nitrogen–oxygen cycle is important in hotter, more massive stars."),
                    ("text", "Fusion supplies energy that helps support a star against gravity. The core must be hot enough for reactions, but energy does not leave the surface immediately: it is transported outward through radiation and convection. The rate depends strongly on temperature and composition, so stellar fusion is a regulated process rather than a simple burn like a chemical flame."),
                    ("callout", "Neutrinos: direct messengers from the core", "Photons scatter many times inside the Sun and can take a very long time to diffuse outward. Neutrinos interact only weakly with matter, so most escape almost directly from the reaction site. Detecting solar neutrinos therefore tests nuclear reactions in the core. The same weak interaction makes neutrinos difficult to detect: enormous detectors and long observing times are needed."),
                    ("text", "When a massive star exhausts its available nuclear fuel, the balance between pressure and gravity can fail. Collapse and explosive events create conditions for additional nucleosynthesis and produce neutrinos. The observed neutrino signal, elemental abundances and remnant compact objects each probe a different stage of that history."),
                ],
            },
            {
                "title": "6 · A dependable nuclear calculation",
                "blocks": [
                    ("text", "Balance the reaction first, including neutrinos, electrons or positrons. Count protons and nucleons on each side. Then choose a consistent mass table, find the mass difference, convert to energy and check the sign. For radioactive samples, convert the time and half-life to the same units before evaluating the exponential."),
                    ("formula", "1 u = 1.6605 × 10⁻²⁷ kg     ·     1 u c² ≈ 931.5 MeV"),
                    ("text", "For astrophysical scale estimates, distinguish energy per reaction from total power. Multiply the reaction rate by the energy released per reaction, and state whether energy carried by neutrinos is included in the observable luminosity. Report whether a quantity is per nucleus, per mole or per kilogram."),
                    ("callout", "What the 'Q' tag means", "Some nuclear topics are marked qualitative in the IOAA syllabus. That means deep quantitative proficiency is not required by the syllabus; the physical ideas and conservation reasoning still matter. Follow the information and constants supplied by the particular problem."),
                ],
            },
        ],
        "problem_ids": [
            (2008, "TH", "S4"), (2009, "TH", "P10"), (2009, "TH", "P11"), (2010, "TH", "S5"), (2011, "TH", "S14"),
            (2012, "TH", "S6"), (2013, "TH", "S3"), (2014, "TH", "P3"), (2014, "TH", "P6"),
            (2015, "TH", "S12"), (2017, "TH", "T6"), (2018, "TH", "T11"),
            (2023, "TH", "Q8"), (2024, "TH", "T4"), (2025, "TH", "T07"), (2025, "TH", "T10"),
        ],
    },
}

# Every entry is only a public exam identifier, not a reproduced problem statement.
