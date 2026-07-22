# An Agent Framework for FastFluent-to-Fluent Simulation of Complex Solid-Liquid Dynamics

This repository contains the public code and validation assets for
**An Agent Framework for FastFluent-to-Fluent Simulation of Complex
Solid-Liquid Dynamics**.

The project exposes FastFluent core workflows, Agent route selection,
evidence bundles, and paper-facing CFD validation cases. It is designed
to make numerical claims traceable without publishing private industrial
CAD, meshes, commercial solver models, restart trees, or production
process data.

## Quick Reproduction

```powershell
python -m pip install -e ".[dev,paper-validation]"
python paper_validation/scripts/validate_claims.py --frozen
python paper_validation/build_paper_assets.py --from-frozen
```

These Level 1 commands require only Python and rebuild the claim
registry, Figure 3 data, Table 1 data, and Supplementary Tables S1-S3
from compact frozen outputs.

## Public Cases

| Case | Name | Role |
| --- | --- | --- |
| BM01 | Laminar channel | analytical public benchmark |
| BM02 | Backward-facing step | TMBWG/NASA SSTm separated-flow benchmark |
| BM03 | Heated blocked channel | public thermal-transport benchmark defined in this work |
| BM04 | Lid-driven cavity | Re=100 public cavity benchmark |
| RP01 | Ghia cavity reproduction | Re=100/400/1000 literature reproduction |
| RP02 | Schaefer-Turek cylinder reproduction | DFG 2D-2 literature reproduction |

The unified entry point is `paper_validation/`. The benchmark ladder
documentation is in `docs/agent_benchmark_ladder/`.

## Reproduction Levels

- Level 1, no commercial solver:
  `python paper_validation/scripts/validate_claims.py --frozen`
  and `python paper_validation/build_paper_assets.py --from-frozen`.
- Level 2, FastFluent recomputation:
  `python paper_validation/run_all.py --backend fastfluent --output paper_validation/reproduced`.
- Level 3, optional Fluent confirmation:
  `python paper_validation/run_all.py --backend fluent --fluent-exe <path> --output paper_validation/reproduced`.

## Industrial Data Policy

The industrial steam-dewaxing study is represented here through generic
Agent/FastFluent algorithms, public data structures, and synthetic
examples. Real industrial geometry, meshes, commercial solver models,
raw process histories, outlet-coordinate mappings, material calibration
records, and restart/checkpoint files are not public because they are
commercially confidential. Non-confidential supplementary information
may be requested from the corresponding authors.

## Documentation

- [Paper reproducibility](docs/paper_reproducibility.md)
- [Paper method mapping](docs/paper_method_mapping.md)
- [Agent benchmark ladder](docs/agent_benchmark_ladder/README.md)
- [Public asset framework map](docs/public_asset_framework_map.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)

## Citation

Use [CITATION.cff](CITATION.cff). The arXiv identifier and DOI are
intentionally left pending until assigned; do not infer or fabricate
them from this preprint branch.

## License

The Python framework is published under Apache-2.0. The C++ FastFluent
core retains its own license under `cpp/fastfluent_core`.
