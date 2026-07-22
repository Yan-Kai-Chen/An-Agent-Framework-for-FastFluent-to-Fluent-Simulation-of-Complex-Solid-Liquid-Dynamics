# RP01 Ghia cavity reproduction

## Physics

Literature reproduction for lid-driven cavity at Re=100, 400, and 1000.

## Source

U. Ghia, K. N. Ghia and C. T. Shin, Journal of Computational Physics 48, 387-411 (1982).

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

- Headline error: `0.0095285 corrected mean RMS`
- Headline speedup: `2.512x`
- Wall-time reduction: `60.19%`

## Commands

```powershell
python paper_validation/cases/RP01_ghia_cavity/postprocess.py --frozen
python paper_validation/cases/RP01_ghia_cavity/run_fastfluent.py --output paper_validation/reproduced/RP01
python paper_validation/cases/RP01_ghia_cavity/run_fluent.py --fluent-exe <path-to-fluent> --output paper_validation/reproduced/RP01_fluent
```
