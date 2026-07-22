from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-frozen", action="store_true")
    args = parser.parse_args()
    for script in ["build_figure3_data.py", "build_supplementary_tables.py", "make_checksums.py"]:
        subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True)
    # Table 1 mirrors the Figure 3 compact numerical source.
    src = ROOT / "frozen_outputs" / "figure3_data.csv"
    dst = ROOT / "frozen_outputs" / "table1_data.csv"
    dst.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Built paper assets from {'frozen' if args.from_frozen else 'current'} outputs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
