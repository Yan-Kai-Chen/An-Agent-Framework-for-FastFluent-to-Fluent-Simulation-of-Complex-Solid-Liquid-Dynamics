# Paper Reproducibility

## Level 1: no commercial solver

```powershell
python paper_validation/scripts/validate_claims.py --frozen
python paper_validation/build_paper_assets.py --from-frozen
```

This validates six case sources, frozen outputs, claim values, Figure 3
data, Table 1 data, and Supplementary Tables S1-S3.

## Level 2: FastFluent recomputation

```powershell
python paper_validation/run_all.py --backend fastfluent --output paper_validation/reproduced
```

This reruns the public FastFluent/Agent contract and writes compact
evidence bundles.

## Level 3: optional Fluent confirmation

```powershell
python paper_validation/run_all.py --backend fluent --fluent-exe <path> --output paper_validation/reproduced
```

Fluent confirmation requires the user's own licensed installation. The
public repository supplies cleaned scripts and frozen outputs, not
commercial solver payloads.
