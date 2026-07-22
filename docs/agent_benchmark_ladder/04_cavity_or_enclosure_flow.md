# BM04 Lid-driven cavity

Two-dimensional lid-driven cavity at Re=100.

## Status

Implemented and reproducible in the public `paper_validation` layer.

## Source

Standard cavity benchmark with Ghia et al. 1982 centreline references.

## Frozen Paper Values

- Headline error: `0.003452 Ghia centreline RMS`
- Speedup: `1.283x`
- Wall-time reduction: `22.08%`

## Public Route

The case directory is
`paper_validation/cases/BM04_lid_driven_cavity`. Level 1 checks read the frozen
JSON outputs. Level 2 reruns the public FastFluent/Agent route. Level 3
provides optional Fluent-confirmation scripts for users with a licensed
Fluent installation.

## Public-Scope Guard

This page documents the public benchmark contract only. It does not publish
private industrial CAD, private meshes, commercial solver case/data files,
restart trees, real dewaxing outlet coordinates, or production process
records.
