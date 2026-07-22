from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

CASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CASE_DIR.parents[1]))

from io_utils import read_json, write_json

def load_expected():
    return read_json(CASE_DIR / "expected_results.json")


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare optional Fluent confirmation for BM04.")
    parser.add_argument("--fluent-exe", default=None, help="Path to Fluent executable.")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    out = Path(args.output)
    payload = {
        "case_id": "BM04",
        "status": "prepared",
        "requires_user_fluent_license": True,
        "fluent_exe_supplied": bool(args.fluent_exe),
        "public_inputs": ["case.json", "source.yaml", "agent_config.json", "expected_results.json"],
    }
    write_json(out / "fluent_confirmation_plan.json", payload)
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
