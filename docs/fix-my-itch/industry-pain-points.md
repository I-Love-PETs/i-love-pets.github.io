# Industry Pain Points

Industry PET failures are rarely about theory alone. They come from procurement, unclear claims, infrastructure gaps, cost surprises, and outputs that still leak.

## Research Handoff

| Problem | Who benefits if solved | Why it is difficult | Starting directions |
| --- | --- | --- | --- |
| Procurement-ready privacy claims | Procurement teams, vendors, legal reviewers, and security reviewers | Claims must be comparable across PET families without flattening important assumptions | Draft a one-page evidence form; test it on product claims; separate customer controls from vendor guarantees |
| Operational readiness for PET deployments | Privacy engineers, SREs, security teams, and deployment owners | Production risk lives in keys, logs, rollback, monitoring, and output review, not just the PET mechanism | Write launch checklists by PET family; define rollback triggers; map controls to threat-model assumptions |
| Total cost of PET ownership | Product leaders, engineering managers, and funders | PET cost is nonlinear and often appears through integration, support, audits, latency, and education | Build scenario worksheets; compare rejected alternatives; include participant and audit costs |
| When governance beats cryptography | Product, legal, policy, and architecture teams | Teams often mislabel incentive or authority problems as data-movement problems | Classify constraints in real use cases; create a decision checklist; document when a PET adds complexity without reducing risk |

## Procurement-Ready Privacy Claims

| Field | Card |
| --- | --- |
| Problem | How can PET vendors and builders make privacy claims that procurement teams can evaluate? |
| The itch | Buyers receive claims like "data stays private" without threat models, assumptions, failure modes, or evidence. |
| Why it matters | Procurement, legal, and security teams either block useful tools or approve tools they do not understand. |
| Current workaround | Long questionnaires, one-off security calls, and contract language. |
| Why the workaround is insufficient | It does not produce comparable evidence across PETs. |
| What good progress would look like | A claim register format for PET products: protected assets, adversaries, guarantees, evidence, limitations, and required customer controls. |
| Difficulty | Medium |
| Good for | Privacy engineer, policy researcher, technical writer |
| Related PETs | All PETs |
| Possible first contribution | Draft a one-page procurement evidence form and test it against three PET product claims. |

## Operational Readiness For PET Deployments

| Field | Card |
| --- | --- |
| Problem | What operational checks should happen before a PET deployment goes live? |
| The itch | PET projects often prove the privacy mechanism but under-specify keys, logs, monitoring, incident response, upgrades, and rollback. |
| Why it matters | Production failures can invalidate the privacy story even when the PET is technically sound. |
| Current workaround | Borrow generic security launch checklists. |
| Why the workaround is insufficient | Generic checklists rarely ask about privacy units, output review, collusion assumptions, attestation, or DP accounting. |
| What good progress would look like | A PET-specific production readiness review with controls mapped to PET families. |
| Difficulty | Medium |
| Good for | Privacy engineer, systems builder, security engineer |
| Related PETs | FL, DP, MPC, HE, TEEs, synthetic data |
| Possible first contribution | Write a readiness checklist for one private inference deployment and include rollback triggers. |

## Total Cost Of PET Ownership

| Field | Card |
| --- | --- |
| Problem | How can teams estimate total cost before choosing a PET? |
| The itch | PET decisions often compare privacy properties but omit engineering effort, participant support, latency, cloud spend, audits, and user education. |
| Why it matters | Good ideas stall when cost appears after architecture commitment. |
| Current workaround | Prototype one candidate and extrapolate. |
| Why the workaround is insufficient | It misses rejected alternatives and operational costs. |
| What good progress would look like | A cost worksheet that covers build, operate, monitor, audit, scale, and explainability costs for each PET option. |
| Difficulty | Good first research problem |
| Good for | Systems builder, benchmark maintainer, privacy engineer |
| Related PETs | All PETs |
| Possible first contribution | Compare total cost drivers for HE inference, TEE inference, and client-side inference for one model provider scenario. |

## When Governance Beats Cryptography

| Field | Card |
| --- | --- |
| Problem | How can teams tell when the real problem is governance rather than needing a PET? |
| The itch | Organizations sometimes choose FL, MPC, or clean rooms to avoid hard conversations about purpose, authority, liability, and acceptable use. |
| Why it matters | A PET can add complexity without solving the actual blocker. |
| Current workaround | Let legal and technical teams negotiate separately. |
| Why the workaround is insufficient | The final design may satisfy neither privacy goals nor business needs. |
| What good progress would look like | A decision checklist that separates data-movement constraints from governance, incentive, and accountability constraints. |
| Difficulty | Good first research problem |
| Good for | Policy researcher, privacy engineer, product/security leader |
| Related PETs | FL, MPC, clean rooms, TEEs |
| Possible first contribution | Analyze three proposed PET use cases and identify which constraints are technical versus governance-driven. |
