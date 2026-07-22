# Agent Benchmark Ladder

The paper-facing ladder now contains four public capability benchmarks
and two literature reproductions. All six cases are implemented in
`paper_validation/` with common source manifests, expected results,
frozen outputs, postprocessors, and optional Fluent confirmation plans.

| Case | Name | Status | Entry |
| --- | --- | --- | --- |
| BM01 | Laminar channel | implemented/reproducible | `paper_validation/cases/BM01_laminar_channel` |
| BM02 | Backward-facing step | implemented/reproducible | `paper_validation/cases/BM02_backward_facing_step` |
| BM03 | Heated blocked channel | implemented/reproducible | `paper_validation/cases/BM03_heated_blocked_channel` |
| BM04 | Lid-driven cavity | implemented/reproducible | `paper_validation/cases/BM04_lid_driven_cavity` |
| RP01 | Ghia cavity reproduction | implemented/reproducible | `paper_validation/cases/RP01_ghia_cavity` |
| RP02 | Schaefer-Turek cylinder reproduction | implemented/reproducible | `paper_validation/cases/RP02_dfg_cylinder` |

The prior dewaxing-inspired public fixture is no longer counted as a
benchmark-ladder case. Dewaxing-related code is documented as a
synthetic method demonstration under `docs/dewaxing_agent/` and
`paper_validation/industrial_methods/`.
