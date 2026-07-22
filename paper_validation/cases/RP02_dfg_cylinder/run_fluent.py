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
        parser = argparse.ArgumentParser(description="Prepare optional Fluent confirmation for RP02.")
        parser.add_argument("--fluent-exe", default=None, help="Path to Fluent executable.")
        parser.add_argument("--output", required=True)
        args = parser.parse_args()
        out = Path(args.output)
        payload = {
            "case_id": "RP02",
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
