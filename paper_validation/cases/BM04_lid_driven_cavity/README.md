# BM04 Lid-driven cavity

## Physics

Two-dimensional lid-driven cavity at Re=100.

## Source

Standard cavity benchmark with Ghia et al. 1982 centreline references.

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

- Headline error: `0.003452 Ghia centreline RMS`
- Headline speedup: `1.283x`
- Wall-time reduction: `22.08%`

## Commands

```powershell
python paper_validation/cases/BM04_lid_driven_cavity/postprocess.py --frozen
python paper_validation/cases/BM04_lid_driven_cavity/run_fastfluent.py --output paper_validation/reproduced/BM04
python paper_validation/cases/BM04_lid_driven_cavity/run_fluent.py --fluent-exe <path-to-fluent> --output paper_validation/reproduced/BM04_fluent
```
