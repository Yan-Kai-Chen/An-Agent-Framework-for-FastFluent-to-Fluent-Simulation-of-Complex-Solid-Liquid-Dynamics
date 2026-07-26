from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from io_utils import read_text, write_text

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--from-frozen", action="store_true")
    args = parser.parse_args()
    for script in ["build_figure3_data.py", "build_supplementary_tables.py"]:
        subprocess.run([sys.executable, str(ROOT / "scripts" / script)], check=True)
    # Table 1 mirrors the Figure 3 compact numerical source.
    src = ROOT / "frozen" / "figure3_data.csv"
    dst = ROOT / "frozen" / "table1_data.csv"
    write_text(dst, read_text(src, encoding="utf-8"), encoding="utf-8")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "make_checksums.py")], check=True)
    print(f"Built paper assets from {'frozen' if args.from_frozen else 'current'} outputs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
