from __future__ import annotations

import argparse
import json
from pathlib import Path

CASE_DIR = Path(__file__).resolve().parent

def load_expected():
    return json.loads((CASE_DIR / "expected_results.json").read_text(encoding="utf-8"))

def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


    def main() -> int:
        parser = argparse.ArgumentParser(description="Postprocess frozen outputs for RP02.")
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
