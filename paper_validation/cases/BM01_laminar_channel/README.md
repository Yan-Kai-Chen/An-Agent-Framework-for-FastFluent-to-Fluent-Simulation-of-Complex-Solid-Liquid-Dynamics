# BM01 Laminar channel

## Physics

Plane Poiseuille laminar channel flow.

## Source

Defined in this work; analytical plane-Poiseuille profile is the reference.

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

- Headline error: `0.008656 outlet-profile RMS`
- Headline speedup: `>2.595x`
- Wall-time reduction: `>61.47%`

## Commands

```powershell
python paper_validation/cases/BM01_laminar_channel/postprocess.py --frozen
python paper_validation/cases/BM01_laminar_channel/run_fastfluent.py --output paper_validation/reproduced/BM01
python paper_validation/cases/BM01_laminar_channel/run_fluent.py --fluent-exe <path-to-fluent> --output paper_validation/reproduced/BM01_fluent
```
