# FastFluent Public Capabilities

FastFluent is the framework's bounded, low-cost CFD evidence layer. It helps
the Agent inspect a case, select an appropriate route, run public or synthetic
screening cases, compile evidence, and prepare a traceable Fluent handoff.
It does not replace final high-fidelity validation.

## Workflow Surface

The public workflow is organized around durable contracts:

1. `CaseSpec v3` describes geometry, materials, boundaries, units, and requested
   quantities of interest.
2. The mesh gateway inspects supported structured or unstructured inputs and
   records mesh evidence.
3. Native and adapter routes compile an `EvidenceBundle v3` with provenance,
   physics passports, checks, and limitations.
4. The route selector, route-plan compiler, execution gate, and controlled
   runner make the Agent's execution decision explicit.
5. The result-pack compiler creates machine-readable outputs for validation,
   post-processing, and downstream handoff.
6. Fluent adapters consume the bounded evidence as setup guidance or optional
   confirmation input.

The primary implementation lives under `src/fromcad2cfd_fastcfd/`. Contract
and workflow details are documented in:

- `CASESPEC_V3.md`
- `EVIDENCE_BUNDLE_V3.md`
- `BOUNDARY_AND_MATERIAL_CONTRACTS.md`
- `MESH_GATEWAY_V2.md`
- `ROUTE_SELECTOR.md`
- `ROUTE_PLAN_COMPILER.md`
- `EXECUTION_GATE.md`
- `CONTROLLED_RUNNER.md`
- `RESULT_PACK_COMPILER.md`
- `WORKFLOW_RUNNER.md`

## Public Validation Surface

The repository contains three validation levels:

- frozen public outputs for claim reproduction without a commercial solver;
- FastFluent recomputation for supported public and synthetic cases;
- optional Fluent confirmation when a licensed executable is supplied by the
  user.

The canonical validation entry point is `paper_validation/`. The benchmark
ladder is documented in `docs/agent_benchmark_ladder/`.

## Supported Public Roles

The public modules cover:

- case validation and explanation;
- unit, boundary, material, and motion contracts;
- structured and selected unstructured mesh inspection;
- native reduced-order evidence generation;
- physics-passport and solver-hint compilation;
- route selection, execution gating, and controlled runs;
- result-pack validation and post-processing;
- FastFluent-to-Fluent plan and handoff generation;
- synthetic dewaxing workflow assets with explicit claim boundaries.

Individual solvers and adapters remain subject to the limitations recorded in
their evidence bundles and capability matrices.

## Data Boundary

Public source code, tests, compact fixtures, and frozen validation outputs are
versioned. Private CAD, industrial meshes, commercial solver cases, restart
trees, raw process histories, runtime output directories, and local deployment
records are intentionally excluded.

Generated runs belong under ignored output directories such as
`sandbox/output/` or `paper_validation/reproduced/`.

