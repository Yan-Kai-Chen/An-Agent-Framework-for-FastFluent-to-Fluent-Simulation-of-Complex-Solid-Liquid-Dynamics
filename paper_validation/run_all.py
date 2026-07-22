from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CASES = [
    "BM01_laminar_channel",
    "BM02_backward_facing_step",
    "BM03_heated_blocked_channel",
    "BM04_lid_driven_cavity",
    "RP01_ghia_cavity",
    "RP02_dfg_cylinder",
]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backend", choices=["fastfluent", "fluent"], required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--fluent-exe", default=None)
    args = parser.parse_args()
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=True)
    results = []
    for case in CASES:
        script = ROOT / "cases" / case / ("run_fastfluent.py" if args.backend == "fastfluent" else "run_fluent.py")
        case_out = out / case
        cmd = [sys.executable, str(script), "--output", str(case_out)]
        if args.backend == "fluent" and args.fluent_exe:
            cmd.extend(["--fluent-exe", args.fluent_exe])
        completed = subprocess.run(cmd, check=True, text=True, capture_output=True)
        results.append({"case": case, "returncode": completed.returncode})
    (out / "run_all_summary.json").write_text(json.dumps({"backend": args.backend, "results": results}, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"backend": args.backend, "case_count": len(results), "output": str(out)}, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
