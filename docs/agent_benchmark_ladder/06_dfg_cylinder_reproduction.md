# RP02 Schaefer-Turek cylinder reproduction

DFG 2D-2 unsteady laminar flow around a cylinder at Re=100.

## Status

Implemented and reproducible in the public `paper_validation` layer.

## Source

M. Schaefer et al., Benchmark computations of laminar flow around a cylinder (1996).

## Frozen Paper Values

- Headline error: `0.672% Strouhal error`
- Speedup: `2.037x confirmation-stage`
- Wall-time reduction: `50.91%`

## Public Route

The case directory is
`paper_validation/cases/RP02_dfg_cylinder`. Level 1 checks read the frozen
JSON outputs. Level 2 reruns the public FastFluent/Agent route. Level 3
provides optional Fluent-confirmation scripts for users with a licensed
Fluent installation.

## Public-Scope Guard

This page documents the public benchmark contract only. It does not publish
private industrial CAD, private meshes, commercial solver case/data files,
restart trees, real dewaxing outlet coordinates, or production process
records.
