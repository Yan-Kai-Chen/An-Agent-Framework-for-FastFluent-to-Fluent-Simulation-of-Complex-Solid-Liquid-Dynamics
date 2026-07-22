# BM03 Heated blocked channel

## Physics

Transient thermal transport through a blocked/porosity-mapped channel.

## Source

Defined in this work as a public thermal-transport benchmark.

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

- Headline error: `0.1956% front error`
- Headline speedup: `1.710x`
- Wall-time reduction: `41.52%`

## Commands

```powershell
python paper_validation/cases/BM03_heated_blocked_channel/postprocess.py --frozen
python paper_validation/cases/BM03_heated_blocked_channel/run_fastfluent.py --output paper_validation/reproduced/BM03
python paper_validation/cases/BM03_heated_blocked_channel/run_fluent.py --fluent-exe <path-to-fluent> --output paper_validation/reproduced/BM03_fluent
```
