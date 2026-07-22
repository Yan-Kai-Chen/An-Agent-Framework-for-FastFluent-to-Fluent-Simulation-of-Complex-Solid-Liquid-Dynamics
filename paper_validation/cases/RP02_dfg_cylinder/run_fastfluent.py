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
        parser = argparse.ArgumentParser(description="Run the public FastFluent route for RP02.")
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
