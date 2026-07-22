# BM01 Laminar channel

Plane Poiseuille laminar channel flow.

## Status

Implemented and reproducible in the public `paper_validation` layer.

## Source

Defined in this work; analytical plane-Poiseuille profile is the reference.

## Frozen Paper Values

- Headline error: `0.008656 outlet-profile RMS`
- Speedup: `>2.595x`
- Wall-time reduction: `>61.47%`

## Public Route

The case directory is
`paper_validation/cases/BM01_laminar_channel`. Level 1 checks read the frozen
JSON outputs. Level 2 reruns the public FastFluent/Agent route. Level 3
provides optional Fluent-confirmation scripts for users with a licensed
Fluent installation.

## Public-Scope Guard

This page documents the public benchmark contract only. It does not publish
private industrial CAD, private meshes, commercial solver case/data files,
restart trees, real dewaxing outlet coordinates, or production process
records.
