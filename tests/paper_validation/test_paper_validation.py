from __future__ import annotations

import ast
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PV = ROOT / "paper_validation"
sys.path.insert(0, str(PV))

from io_utils import exists, iter_files, read_json, read_text, write_text

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
            assert exists(base / name), f"{slug}/{name}"


def test_long_path_aware_recursive_file_iteration(tmp_path):
    target = tmp_path / "nested" / "deeper" / "payload.txt"
    write_text(target, "payload\n")
    assert set(iter_files(tmp_path)) == {target}


def test_expected_results_schema_shape():
    for slug in CASES:
        data = read_json(PV / "cases" / slug / "expected_results.json")
        assert {"case_id", "title", "qoi", "timings", "derived", "display", "tolerances"} <= set(data)

def test_paper_validation_scripts_parse():
    scripts = [
        PV / "build_paper_assets.py",
        PV / "run_all.py",
        *sorted((PV / "scripts").glob("*.py")),
        *sorted((PV / "industrial_methods").glob("*.py")),
    ]
    for slug in CASES:
        scripts.extend(sorted((PV / "cases" / slug).glob("*.py")))
    for script in scripts:
        ast.parse(read_text(script, encoding="utf-8-sig"), filename=str(script))

def test_claim_validator_passes():
    completed = subprocess.run([sys.executable, str(PV / "scripts" / "validate_claims.py"), "--frozen"], cwd=ROOT, text=True, capture_output=True)
    assert completed.returncode == 0, completed.stdout + completed.stderr

def test_asset_builder_outputs_tables():
    completed = subprocess.run([sys.executable, str(PV / "build_paper_assets.py"), "--from-frozen"], cwd=ROOT, text=True, capture_output=True)
    assert completed.returncode == 0, completed.stdout + completed.stderr
    assert exists(PV / "frozen_outputs" / "figure3_data.csv")
    assert exists(PV / "frozen_outputs" / "table1_data.csv")
    assert exists(PV / "frozen_outputs" / "supplementary_tables" / "S1_functional_positioning.csv")

def test_public_scope_scan_passes():
    scan = read_json(PV / "reports" / "public_scope_scan.json")
    assert scan["status"] == "pass"
    assert scan["forbidden_payloads_found"] == 0

def test_run_all_public_contract_backends(tmp_path):
    for backend in ["fastfluent", "fluent"]:
        out = tmp_path / backend
        completed = subprocess.run([sys.executable, str(PV / "run_all.py"), "--backend", backend, "--output", str(out)], cwd=ROOT, text=True, capture_output=True)
        assert completed.returncode == 0, completed.stdout + completed.stderr
        summary = read_json(out / "run_all_summary.json")
        assert summary["backend"] == backend
        assert len(summary["results"]) == len(CASES)
