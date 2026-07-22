# BM02 Backward-facing step

## Physics

SSTm turbulent 2D backward-facing-step separated flow.

## Source

AIAA Turbulence Model Benchmarking Working Group / NASA Turbulence Modeling Resource.

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

- Headline error: `0.168% reattachment deviation`
- Headline speedup: `2.655x`
- Wall-time reduction: `62.33%`

## Commands

```powershell
python paper_validation/cases/BM02_backward_facing_step/postprocess.py --frozen
python paper_validation/cases/BM02_backward_facing_step/run_fastfluent.py --output paper_validation/reproduced/BM02
python paper_validation/cases/BM02_backward_facing_step/run_fluent.py --fluent-exe <path-to-fluent> --output paper_validation/reproduced/BM02_fluent
```
