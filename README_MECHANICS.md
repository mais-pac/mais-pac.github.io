# Mechanics Playground

A visual-first mechanics lab for the MAIS PAC website. The goal is simple: students should enjoy learning physics by pulling, launching, colliding, balancing, and rolling things before they meet the equations. Every experiment has:

- interactive controls (sliders, planet presets, toggles, action buttons);
- four live readouts;
- a short challenge;
- an optional **Show the physics** panel;
- a “Mark explored” lab passport saved in `localStorage`.

The page is built as one self-contained HTML file with inline CSS, JavaScript, and SVG. It makes no network requests and works offline.

## Experiments

| ID | Experiment | Core idea |
|---|---|---|
| `pendulum` | Pendulum lab | Nonlinear pendulum, damping, planet gravity, measured vs small-angle period |
| `projectile` | Projectile launcher | Quadratic air drag, vacuum ghost path, target game |
| `ramp` | Ramp & friction | Static vs kinetic friction, force vectors on an incline |
| `cart` | Force & motion cart | Newton’s second law, friction, mass vs acceleration |
| `spring` | Spring & resonance | Damped driven oscillator, natural frequency |
| `collisions` | Collision carts | Momentum conservation, restitution, kinetic energy loss |
| `coaster` | Energy roller coaster | Potential/kinetic/thermal energy accounting |
| `orbits` | Orbit builder | Newtonian gravity, circular/escape speed, bound vs unbound orbits |
| `torque` | Balance & torque | Seesaw equilibrium, moment arms |
| `atwood` | Atwood machine | Connected masses, ideal pulley acceleration/tension |
| `rolling` | Rolling race | Sphere vs disk vs hoop, rotational inertia |
| `cradle` | Newton’s cradle | Equal-mass elastic transfer, lift-count pattern |
| `waves` | Standing waves | String harmonics, tension/density, nodes and antinodes |

## Build and test

```bash
npm run build:mechanics
npm run integrate:mechanics
npm run test:mechanics
BASE_URL="file://$(pwd)/mechanics/index.html" npm run test:mechanics
```

`build_mechanics.py` reads `scripts/mechanics/page-template.html`, `mechanics.css`, and `mechanics.js`, then writes `mechanics/index.html`. `integrate_mechanics.py` adds the Mechanics Lab navigation link and featured pendulum cards to the home, explore, teaching, about, resources, and teaching-template pages without reformatting them.

## Models and limitations

These are teaching simulations, not research-grade solvers. They use small fixed-step integration (RK4 for the pendulum, semi-implicit/Verlet-style steps elsewhere), simplified friction and drag, ideal pulleys/strings, and 2D motion. The Newton’s cradle uses an idealized equal-mass transfer model rather than a full many-body contact solver. The rolling race assumes rolling without slipping. The orbit builder uses a point-mass planet and stops if the satellite crashes or escapes the view.

## Accessibility and classroom use

- Keyboard: `Space` plays/pauses, `R` resets when focus is not in a control.
- Reduced motion: the lab starts paused when `prefers-reduced-motion` is set.
- Mobile: the layout stacks and the stage supports pointer dragging.
- Suggested routine: **predict → play → explain → challenge**. Ask students to describe the pattern in words before opening the optional physics panel.
