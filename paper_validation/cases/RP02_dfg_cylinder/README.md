# RP02 Schaefer-Turek cylinder reproduction

## Physics

DFG 2D-2 unsteady laminar flow around a cylinder at Re=100.

## Source

M. Schaefer et al., Benchmark computations of laminar flow around a cylinder (1996).

## Public Input

The case uses a deterministic public definition, public reference data, or a
public mesh/generator. It does not require or include private industrial
CAD, industrial meshes, Fluent case/data files, Abaqus outputs, or ProCAST
model data.

## Agent Action

The wrapper builds the candidate set, evaluates the FastFluent/public
screen, applies the readiness and QoI gates, and writes a common evidence
chain: `campaign.json`, `qoi.json`, `readiness.json`, `diagnostics.json`,
`cost.json`, `evidence_bundle.json`, `agent_decision.json`,
`promotion_manifest.json`, `discrepancy.json`, and `result_pack.json`.

## Expected Result

- Headline error: `0.672% Strouhal error`
- Headline speedup: `2.037x confirmation-stage`
- Wall-time reduction: `50.91%`

## Commands

```powershell
python paper_validation/cases/RP02_dfg_cylinder/postprocess.py --frozen
python paper_validation/cases/RP02_dfg_cylinder/run_fastfluent.py --output paper_validation/reproduced/RP02
python paper_validation/cases/RP02_dfg_cylinder/run_fluent.py --fluent-exe <path-to-fluent> --output paper_validation/reproduced/RP02_fluent
```
