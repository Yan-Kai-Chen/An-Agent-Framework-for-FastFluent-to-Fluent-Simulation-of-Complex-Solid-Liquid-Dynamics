# RP01 Ghia cavity reproduction

Literature reproduction for lid-driven cavity at Re=100, 400, and 1000.

## Status

Implemented and reproducible in the public `paper_validation` layer.

## Source

U. Ghia, K. N. Ghia and C. T. Shin, Journal of Computational Physics 48, 387-411 (1982).

## Frozen Paper Values

- Headline error: `0.0095285 corrected mean RMS`
- Speedup: `2.512x`
- Wall-time reduction: `60.19%`

## Public Route

The case directory is
`paper_validation/cases/RP01_ghia_cavity`. Level 1 checks read the frozen
JSON outputs. Level 2 reruns the public FastFluent/Agent route. Level 3
provides optional Fluent-confirmation scripts for users with a licensed
Fluent installation.

## Public-Scope Guard

This page documents the public benchmark contract only. It does not publish
private industrial CAD, private meshes, commercial solver case/data files,
restart trees, real dewaxing outlet coordinates, or production process
records.
