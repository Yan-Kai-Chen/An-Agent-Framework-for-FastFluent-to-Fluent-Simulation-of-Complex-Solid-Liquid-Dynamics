from __future__ import annotations

def deterministic_gain_grid(base_score, gains):
    return [{"gain": gain, "score": base_score * gain} for gain in gains]
