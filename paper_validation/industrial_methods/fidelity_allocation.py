from __future__ import annotations

def choose_route(routes, max_error, max_cost):
    feasible = [r for r in routes if r["error"] <= max_error and r["cost"] <= max_cost]
    if not feasible:
        return min(routes, key=lambda r: (r["error"], r["cost"]))
    return min(feasible, key=lambda r: r["cost"])
