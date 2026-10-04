# rocketsim

[![tests](https://github.com/alexxberrocal/rocketsim/actions/workflows/tests.yml/badge.svg)](https://github.com/alexxberrocal/rocketsim/actions/workflows/tests.yml)

A planar (3-DOF) ascent flight simulator for small rockets, coupled to a
solid-propellant motor model. Every physical model is checked against an
analytical solution, published data or OpenRocket, and the scripts that
reproduce each comparison live in [`validation/`](validation/).

> **Status:** phase 0, repository set-up. No physical models are implemented yet.

## Goals

- Simulate the ascent of a rocket from launch to ground impact: thrust,
  drag with a Mach-dependent drag coefficient, variable mass and the
  International Standard Atmosphere.
- Predict a solid motor's thrust curve from its grain geometry and
  propellant properties, and compare it with a published commercial motor.
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

- M. Martinez-Sanchez, *16.50 Introduction to Propulsion Systems*,
  MIT OpenCourseWare, Spring 2012.
- *16.512 Rocket Propulsion*, MIT OpenCourseWare, Fall 2005.

## Licence

[MIT](LICENSE)
