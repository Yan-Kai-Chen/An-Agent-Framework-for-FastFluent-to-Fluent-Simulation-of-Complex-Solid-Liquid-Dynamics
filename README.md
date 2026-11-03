# FastAgent

[![arXiv](https://img.shields.io/badge/arXiv-2611.00645-b31b1b.svg)](https://arxiv.org/abs/2611.00645)

Official code repository for **FastAgent: A Physics-Aware FastFluent-to-Fluent Workflow for Rapid CFD Screening and Industrial Steam Dewaxing Design**.

[Paper](https://arxiv.org/abs/2611.00645) |
[PDF](https://arxiv.org/pdf/2611.00645) |
[Citation](#citation) |
[Reproducibility](docs/paper_reproducibility.md)

FastAgent is a physics-aware controller for CFD campaigns, built around
FastFluent, a lightweight numerical engine for rapid physical screening.
FastFluent generates fields and quantities of interest. FastAgent uses this
evidence to select physical models, numerical resolution, simulation horizons,
and candidates for high-fidelity confirmation. In the paper, Fluent provides
CFD confirmation and Abaqus evaluates shell fracture. Discrepancies returned
from these calculations guide subsequent screening and design decisions.

## Results Reported in the Preprint

- Across six CFD benchmark campaigns, FastAgent with FastFluent reduces
  normalised worst-QoI error by **5.68-99.14%** and accelerates
  decision-relevant computation by **1.53-15.36 times** relative to a matched
  Generic Agent workflow.
- In full-cycle steam dewaxing, the rapid route localises the risk window
  with **81.39% fewer cell-time updates** than a fine-grid, small-time-step
  reference, while Fluent confirms melt completion.
- Screening **131,072 outlet layouts**, followed by selective CFD and
  structural evaluation, identifies a six-outlet design that reduces
  simulated crack opening by **96.0%** and connected crack extent by
  **66.7%** relative to the original design.

## Quick Reproduction

```powershell
python -m pip install -e ".[dev,paper-validation]"
python paper_validation/scripts/validate_claims.py --frozen
python paper_validation/build_paper_assets.py --from-frozen
```

These Level 1 commands require only Python. They validate frozen public
benchmark outputs and rebuild the repository's benchmark summaries and
tables. See the [reproducibility guide](docs/paper_reproducibility.md) for
the generated files and their relation to the preprint.

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

If this work supports your research, please cite the
[preprint](https://arxiv.org/abs/2611.00645). GitHub's **Cite this repository**
button uses the paper metadata in [CITATION.cff](CITATION.cff).

```bibtex
@misc{chen2026fastagent,
  title = {{FastAgent}: A Physics-Aware {FastFluent}-to-{Fluent} Workflow for Rapid {CFD} Screening and Industrial Steam Dewaxing Design},
  author = {Chen, YanKai and Yu, QiuHeng and Yuan, Man and Zou, Ting and Wu, Lin and He, Jian and Zhang, QiongYuan and Jing, Tao and Xu, QingYan},
  year = {2026},
  eprint = {2611.00645},
  archivePrefix = {arXiv},
  primaryClass = {cs.AI},
  doi = {10.48550/arXiv.2611.00645},
  url = {https://arxiv.org/abs/2611.00645}
}
```

## License

The Python framework is published under Apache-2.0. The C++ FastFluent
core retains its own license under `cpp/fastfluent_core`.
