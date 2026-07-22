# BM02 Backward-facing step

SSTm turbulent 2D backward-facing-step separated flow.

## Status

Implemented and reproducible in the public `paper_validation` layer.

## Source

AIAA Turbulence Model Benchmarking Working Group / NASA Turbulence Modeling Resource.

## Frozen Paper Values

- Headline error: `0.168% reattachment deviation`
- Speedup: `2.655x`
- Wall-time reduction: `62.33%`

## Public Route

The case directory is
`paper_validation/cases/BM02_backward_facing_step`. Level 1 checks read the frozen
JSON outputs. Level 2 reruns the public FastFluent/Agent route. Level 3
provides optional Fluent-confirmation scripts for users with a licensed
Fluent installation.

## Public-Scope Guard

This page documents the public benchmark contract only. It does not publish
private industrial CAD, private meshes, commercial solver case/data files,
restart trees, real dewaxing outlet coordinates, or production process
records.
