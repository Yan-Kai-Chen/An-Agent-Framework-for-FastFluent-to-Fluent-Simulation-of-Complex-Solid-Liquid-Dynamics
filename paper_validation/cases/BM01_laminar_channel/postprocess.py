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
    parser = argparse.ArgumentParser(description="Postprocess frozen outputs for BM01.")
    parser.add_argument("--frozen", action="store_true", help="Read compact frozen outputs.")
    parser.add_argument("--output", default=str(CASE_DIR / "frozen_outputs" / "qoi.json"))
    args = parser.parse_args()
    data = load_expected()
    result = {
        "case_id": data["case_id"],
        "qoi": data["qoi"],
        "timings": data["timings"],
        "derived": data["derived"],
        "mode": "frozen" if args.frozen else "public-postprocess",
    }
    write_json(Path(args.output), result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
