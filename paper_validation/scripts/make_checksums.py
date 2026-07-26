from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from io_utils import iter_files, read_bytes, write_text

def main() -> int:
    out = ROOT / "SHA256SUMS.txt"
    files = sorted(p for p in iter_files(ROOT) if ".pyc" not in p.suffixes and p.name != "SHA256SUMS.txt")
    lines = []
    for path in files:
        digest = hashlib.sha256(read_bytes(path)).hexdigest()
        lines.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    write_text(out, "\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
