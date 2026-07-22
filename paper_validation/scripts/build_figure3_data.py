from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from io_utils import open_text, read_json

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
    with open_text(out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["case_id", "headline_error", "speedup", "wall_time_reduction_percent", "display_speedup", "display_wall_reduction"])
        writer.writeheader()
        for slug in CASES:
            data = read_json(ROOT / "cases" / slug / "expected_results.json")
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
