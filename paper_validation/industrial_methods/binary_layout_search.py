from __future__ import annotations

def enumerate_masks(n_positions):
    for mask in range(1 << n_positions):
        yield {"mask": mask, "active": [i for i in range(n_positions) if mask & (1 << i)]}

def top_k_layouts(layouts, k, score_key="score"):
    return sorted(layouts, key=lambda row: row[score_key], reverse=True)[:k]
