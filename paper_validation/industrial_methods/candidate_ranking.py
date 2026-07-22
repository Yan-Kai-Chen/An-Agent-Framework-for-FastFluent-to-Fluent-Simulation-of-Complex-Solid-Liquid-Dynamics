from __future__ import annotations

def rank_candidates(candidates, weights):
    scored = []
    for item in candidates:
        score = sum(float(item.get(k, 0.0)) * float(v) for k, v in weights.items())
        scored.append({**item, "score": score})
    return sorted(scored, key=lambda row: row["score"], reverse=True)
