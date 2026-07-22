# BM03 Heated blocked channel

Transient thermal transport through a blocked/porosity-mapped channel.

## Status

Implemented and reproducible in the public `paper_validation` layer.

## Source

Defined in this work as a public thermal-transport benchmark.

## Frozen Paper Values

- Headline error: `0.1956% front error`
- Speedup: `1.710x`
- Wall-time reduction: `41.52%`

## Public Route

The case directory is
`paper_validation/cases/BM03_heated_blocked_channel`. Level 1 checks read the frozen
JSON outputs. Level 2 reruns the public FastFluent/Agent route. Level 3
provides optional Fluent-confirmation scripts for users with a licensed
Fluent installation.

## Public-Scope Guard

This page documents the public benchmark contract only. It does not publish
private industrial CAD, private meshes, commercial solver case/data files,
restart trees, real dewaxing outlet coordinates, or production process
records.
