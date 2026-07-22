from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PV = ROOT / "paper_validation"

CASES = [
    "BM01_laminar_channel",
    "BM02_backward_facing_step",
    "BM03_heated_blocked_channel",
    "BM04_lid_driven_cavity",
    "RP01_ghia_cavity",
    "RP02_dfg_cylinder",
]

def test_case_contract_files_exist():
    for slug in CASES:
        base = PV / "cases" / slug
        for name in ["README.md", "source.yaml", "case.json", "agent_config.json", "expected_results.json", "postprocess.py", "run_fastfluent.py", "run_fluent.py"]:
            assert (base / name).exists(), f"{slug}/{name}"

def test_expected_results_schema_shape():
    for slug in CASES:
        data = json.loads((PV / "cases" / slug / "expected_results.json").read_text(encoding="utf-8"))
        assert {"case_id", "title", "qoi", "timings", "derived", "display", "tolerances"} <= set(data)

def test_claim_validator_passes():
    completed = subprocess.run([sys.executable, str(PV / "scripts" / "validate_claims.py"), "--frozen"], cwd=ROOT, text=True, capture_output=True)
    assert completed.returncode == 0, completed.stdout + completed.stderr

def test_asset_builder_outputs_tables():
    completed = subprocess.run([sys.executable, str(PV / "build_paper_assets.py"), "--from-frozen"], cwd=ROOT, text=True, capture_output=True)
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert (PV / "frozen_outputs" / "figure3_data.csv").exists()
    assert (PV / "frozen_outputs" / "table1_data.csv").exists()
    assert (PV / "frozen_outputs" / "supplementary_tables" / "S1_functional_positioning.csv").exists()

def test_public_scope_scan_passes():
    scan = json.loads((PV / "reports" / "public_scope_scan.json").read_text(encoding="utf-8"))
    assert scan["status"] == "pass"
    assert scan["forbidden_payloads_found"] == 0
