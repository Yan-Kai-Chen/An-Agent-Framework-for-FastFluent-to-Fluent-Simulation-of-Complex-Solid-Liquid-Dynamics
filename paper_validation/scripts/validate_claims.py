from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from io_utils import read_json, write_json

def get_value(source: dict, section: str, quantity: str):
    return source[section][quantity]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--frozen", action="store_true")
    parser.add_argument("--output", default=str(ROOT / "reports" / "claim_validation.json"))
    args = parser.parse_args()
    claims = read_json(ROOT / "paper_claims.yaml")
    results = []
    failures = []
    for claim in claims:
        source_path = ROOT / claim["source_files"][0]
        source = read_json(source_path)
        value = get_value(source, claim["source_section"], claim["quantity"])
        expected = claim["reported_value"]
        tol = claim.get("tolerance", 5e-6)
        passed = abs(float(value) - float(expected)) <= tol
        row = {
            "claim_id": claim["claim_id"],
            "case_id": claim["case_id"],
            "quantity": claim["quantity"],
            "reported_value": expected,
            "recomputed_value": value,
            "tolerance": tol,
            "status": "pass" if passed else "fail",
        }
        results.append(row)
        if not passed:
            failures.append(row)
    payload = {"mode": "frozen" if args.frozen else "standard", "total": len(results), "failed": len(failures), "results": results}
    out = Path(args.output)
    write_json(out, payload)
    print(json.dumps({"total": len(results), "failed": len(failures), "output": str(out)}, indent=2))
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main())
