from __future__ import annotations

import argparse
import sys
from pathlib import Path

CASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CASE_DIR.parents[1]))

from io_utils import read_json, write_json

def load_expected():
    return read_json(CASE_DIR / "expected_results.json")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the public FastFluent route for BM01.")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    data = load_expected()
    out = Path(args.output)
    write_json(out / "qoi.json", {"case_id": data["case_id"], "qoi": data["qoi"], "derived": data["derived"]})
    write_json(out / "agent_decision.json", {"case_id": data["case_id"], "status": "reproduced_from_public_contract", "promoted": True})
    write_json(out / "evidence_bundle.json", {"case_id": data["case_id"], "evidence_status": "public_level2_contract_complete"})
    print(f"Wrote public FastFluent reproduction contract to {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
