from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    "BM01_laminar_channel",
    "BM02_backward_facing_step",
    "BM03_heated_blocked_channel",
    "BM04_lid_driven_cavity",
    "RP01_ghia_cavity",
    "RP02_dfg_cylinder",
]

def main() -> int:
    out = ROOT / "frozen_outputs" / "figure3_data.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["case_id", "headline_error", "speedup", "wall_time_reduction_percent", "display_speedup", "display_wall_reduction"])
        writer.writeheader()
        for slug in CASES:
            data = json.loads((ROOT / "cases" / slug / "expected_results.json").read_text(encoding="utf-8"))
            writer.writerow({
                "case_id": data["case_id"],
                "headline_error": data["display"]["headline_error"],
                "speedup": f"{data['derived']['speedup']:.6f}",
                "wall_time_reduction_percent": f"{data['derived']['wall_time_reduction_percent']:.6f}",
                "display_speedup": data["display"]["headline_speedup"],
                "display_wall_reduction": data["display"]["wall_time_reduction"],
            })
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
