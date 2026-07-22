# Paper Method Mapping

| Paper object | Code object | Required output |
| --- | --- | --- |
| Campaign `C={G,P,Theta,Q,B}` | `CaseSpec`, candidate set, budget/route plan | `campaign.json` |
| Candidate fields `Phi_k` | FastFluent/Fluent field artifacts | field manifest or field summary |
| Quantities `q_k` | QoI extractors | `qoi.json` |
| Readiness `Pi_k` | physics passport, mesh gate, execution gate | `readiness.json` |
| Numerical trust `eta_k` | convergence, residual, sensitivity, stop criteria | `diagnostics.json` |
| Cost `c_k` | measured wall-time receipt | `cost.json` |
| Evidence `E_k` | `EvidenceBundle` | `evidence_bundle.json` |
| repair/rescreen/promote | Agent decision policy | `agent_decision.json` |
| top-K confirmation | route plan and promoted run set | `promotion_manifest.json` |
| discrepancy `Delta q_k` | comparison/postprocessing | `discrepancy.json` |
| final paper evidence | claim ledger and result pack | `result_pack.json` |

Every `paper_validation` case writes or emulates this evidence chain in
compact machine-readable form. Case-specific solvers and postprocessors
are allowed, but final paper claims are validated through the common
claim registry.
