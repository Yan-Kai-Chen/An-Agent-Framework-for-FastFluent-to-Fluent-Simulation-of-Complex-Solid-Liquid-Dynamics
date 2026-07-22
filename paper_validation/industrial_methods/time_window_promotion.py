from __future__ import annotations

def promote_windows(windows, threshold):
    return [w for w in windows if w["risk"] >= threshold]
