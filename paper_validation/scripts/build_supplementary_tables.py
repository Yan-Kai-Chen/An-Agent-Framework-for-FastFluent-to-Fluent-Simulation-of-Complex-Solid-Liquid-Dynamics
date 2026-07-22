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
    outdir = ROOT / "frozen_outputs" / "supplementary_tables"
    rows = []
    for slug in CASES:
        data = read_json(ROOT / "cases" / slug / "expected_results.json")
        rows.append({
            "case_id": data["case_id"],
            "title": data["title"],
            "headline_error": data["display"]["headline_error"],
            "speedup": data["display"]["headline_speedup"],
            "wall_time_reduction": data["display"]["wall_time_reduction"],
        })
    for name in ["S1_functional_positioning.csv", "S2_public_benchmarks.csv", "S3_literature_reproductions.csv"]:
        with open_text(outdir / name, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
    print(outdir)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
