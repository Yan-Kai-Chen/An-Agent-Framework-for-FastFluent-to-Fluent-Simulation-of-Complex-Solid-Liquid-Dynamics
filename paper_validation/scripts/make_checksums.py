from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main() -> int:
    out = ROOT / "SHA256SUMS.txt"
    files = sorted(p for p in ROOT.rglob("*") if p.is_file() and ".pyc" not in p.suffixes and p.name != "SHA256SUMS.txt")
    lines = []
    for path in files:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        lines.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(out)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
