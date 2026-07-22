# Paper Validation

This directory is the public reproducibility layer for the arXiv
manuscript. It provides six public CFD validation cases, compact frozen
outputs, claim-to-evidence mapping, and solver-independent asset
builders.

## Levels

```powershell
python paper_validation/scripts/validate_claims.py --frozen
python paper_validation/build_paper_assets.py --from-frozen
python paper_validation/run_all.py --backend fastfluent --output paper_validation/reproduced
python paper_validation/run_all.py --backend fluent --fluent-exe <path> --output paper_validation/reproduced
```

Level 1 does not require Fluent, Abaqus, ProCAST, or any private
industrial model. Level 3 only prepares optional Fluent confirmation
plans unless the user supplies and runs a licensed Fluent installation.
