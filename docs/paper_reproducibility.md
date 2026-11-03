# Paper Reproducibility

These instructions accompany
[FastAgent: A Physics-Aware FastFluent-to-Fluent Workflow for Rapid CFD Screening and Industrial Steam Dewaxing Design](https://arxiv.org/abs/2611.00645).
The preprint contains the final figures, matched Generic Agent comparison,
and industrial steam-dewaxing results.

## Level 1: no commercial solver

```powershell
python paper_validation/scripts/validate_claims.py --frozen
python paper_validation/build_paper_assets.py --from-frozen
```

This validates the six public case sources, frozen outputs, and claim values,
then rebuilds the repository's benchmark summary and supplementary tables.
Generated files retain historical names such as `figure3_data.csv` and
`table1_data.csv`; these filenames do not specify the final preprint figure
or table numbers.

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

## Industrial Case Availability

The steam-dewaxing study includes startup screening, full-cycle fidelity
allocation, and outlet-layout selection. Public algorithms and synthetic
examples are included in the repository. Case-specific industrial geometry,
commercial-solver models, and proprietary process data remain commercially
confidential. Further non-confidential information may be requested from the
authors through the contact details in the preprint.
