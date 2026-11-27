# rocketsim

[![tests](https://github.com/alexxberrocal/rocketsim/actions/workflows/tests.yml/badge.svg)](https://github.com/alexxberrocal/rocketsim/actions/workflows/tests.yml)

A planar (3-DOF) ascent flight simulator for small rockets, coupled to a
solid-propellant motor model. Every physical model is checked against an
analytical solution, published data or OpenRocket, and the scripts that
reproduce each comparison live in [`validation/`](validation/).

> **Status (27 November 2026):** phase 1 in progress. Repository, CI and
> report outline set up in October 2026; model development started on
> 23 November 2026 with the atmosphere model (U.S. Standard Atmosphere 1976).
> No physical model is implemented yet.
>
> **Planned:** v0.1, 3-DOF ascent with analytical validations (end of
> December 2026); v1.0, solid-motor model, comparison with OpenRocket and
> technical report (February 2027).

## Goals

- Simulate the ascent of a rocket from launch to ground impact: thrust,
  drag with a Mach-dependent drag coefficient, variable mass and the
  International Standard Atmosphere.
- Predict a solid motor's chamber pressure and thrust curve from its grain
  geometry and propellant properties; verify it against openMotor and
  validate it against a published static test whose inputs are all public
  (R. Nakka's KSB-002).
- Fly the simulated rocket on the simulated motor and compare apogee and
  burnout velocity with OpenRocket.
- State clearly what the models do not capture.

## Scope

**In scope (v1):** 3-DOF planar ascent, ISA atmosphere, Cd(Mach) drag,
solid motor (BATES-type grain, r = a·Pcⁿ burn rate, ideal nozzle,
thin-wall casing check), validation.

**Out of scope (v1):** thrust-vector control, 6-DOF dynamics, wind,
Monte Carlo dispersion, structural simulation beyond the casing check,
liquid engines.

## Installation

Requires Python 3.11 or later.

```bash
git clone https://github.com/alexxberrocal/rocketsim.git
cd rocketsim
python -m venv .venv
.venv/Scripts/activate      # Windows; on Linux/macOS: source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Repository layout

```
src/rocketsim/   simulator package
tests/           unit tests (pytest)
validation/      scripts that reproduce every validation figure
data/            published data files, sources in data/SOURCES.md
docs/            figures
report/          technical report (LaTeX): main.tex, sections/, appendices/, references.bib
```

## References

- COESA, *U.S. Standard Atmosphere, 1976*, NOAA-S/T 76-1562,
  NOAA, NASA and USAF, Washington, D.C., 1976.
- M. Martinez-Sanchez, *16.50 Introduction to Propulsion Systems*,
  MIT OpenCourseWare, Spring 2012 (lecture notes originally by
  J. L. Kerrebrock).
- M. Martinez-Sanchez, *16.512 Rocket Propulsion*, MIT OpenCourseWare,
  Fall 2005.

## Licence

[MIT](LICENSE)
