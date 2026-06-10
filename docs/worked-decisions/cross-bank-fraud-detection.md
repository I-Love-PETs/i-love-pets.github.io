# Worked Decision: Banks Jointly Detecting Fraud Rings

!!! info "Review status"
    Last reviewed: 2026-06-10
    Evidence level: Expert judgment
    Snapshot scope: A worked reasoning example. Figures are illustrative and labeled. Validate detection lift, collusion assumptions, and latency against real transaction flows before deployment.

Several banks suspect the same fraud rings are moving money across their institutions, but no single bank sees the whole pattern. They want to combine signal — which accounts and entities appear on multiple sides of suspicious flows — without exposing customer lists or raw transactions to each other. The hard part is that the *overlap itself* can be sensitive: revealing that an entity is under investigation at Bank A is itself a leak.

## 1. Decision Context

| Dimension | Detail |
| --- | --- |
| Data | Per-bank transaction graphs, customer/entity identifiers, internal fraud labels and investigation flags. Highly sensitive and competitively confidential. |
| Parties | Several banks (mutually distrustful competitors), possibly a consortium operator or regulator as coordinator, fraud analysts as end users. |
| Constraints | No bank will share raw transactions or full customer lists. Collusion between a subset of banks (or with the coordinator) must be considered. Decisions are time-sensitive — fraud windows are short. Outputs feed human analysts and possibly account actions, so false positives are costly. |
| What success looks like | A measurable lift in detecting cross-institution fraud rings, with raw data never leaving any bank, the shared output limited to what is contractually and legally permitted, and a clear bound on what a colluding subset can learn. |

!!! note "The overlap is not neutral data"
    A frequent mistake is treating the intersection of entities as non-sensitive because "it's just the matches." Knowing an entity is flagged at another institution can tip off investigations or expose customers. Treat the match set itself as a protected output.

## 2. Candidate PETs

| Candidate | Why it is on the shortlist |
| --- | --- |
| Private set intersection (PSI) | Lets two or more banks find shared entities without revealing non-matching customers. The natural first tool when the core task is entity overlap. See [Private Set Intersection](../pet-patterns/private-set-intersection.md). |
| Secure multi-party computation (MPC) | Computes a joint function (e.g., a cross-bank risk score on shared entities) without any party seeing others' inputs. Fits when the goal is a sensitive *joint computation*, not just overlap. |
| Differential privacy (DP) | Bounds leakage on any *published* aggregate metric (e.g., "fraud rings detected this quarter"). Protects the reporting layer, not the operational matching. |
| Federated learning (FL) | If the goal becomes a shared fraud *model* rather than a specific joint computation, FL keeps training data local. A divergent path, kept for completeness. |
| Clean-room governance | Contractual and audit controls around match use, repeated-query limits, and logging. Often the difference between a safe and an unsafe deployment regardless of the cryptography. |

## 3. Rejected Options

| Rejected option | Why rejected |
| --- | --- |
| **Centralize transactions in a shared utility** | Operationally simplest and analytically richest, but no competitor bank will pool raw transaction data, and it concentrates catastrophic breach and liability risk. Rejected on confidentiality and risk-concentration grounds. |
| **Hash-and-share customer identifiers** | A common "lightweight PSI" shortcut: each bank shares hashed IDs and compares. It leaks badly — identifiers are low-entropy and brute-forceable, and it reveals the full hashed set, not just the agreed intersection. Rejected as false privacy. |
| **PSI alone as the whole solution** | PSI finds overlap, but if one party can run repeated PSI with crafted sets, it can probe the other's membership over time. PSI without query governance and minimum-cohort controls leaks via repetition. Rejected as incomplete — PSI stays, but only with governance. |
| **FL shared fraud model as the first move** | Tempting, but it answers a different question. The immediate need is identifying cross-institution entities, not training a global classifier. FL also does not, by itself, protect the sensitivity of which entities are flagged. Deferred, not adopted now. |
| **HE for the joint computation** | For a narrow scoring step HE is conceivable, but a multi-party fraud computation with several banks maps more naturally onto MPC, and HE latency would struggle with operational fraud windows. Rejected on latency/fit. |

## 4. Final Recommendation

Match the tool to which question dominates:

- **If the task is primarily entity overlap:** lead with **PSI**, hardened by **clean-room governance** — repeated-query limits, minimum-cohort thresholds before any match is actioned, and audit logging of who queried what. Add **DP** on any aggregate that gets published or reported.
- **If the task is a sensitive joint computation** (e.g., a combined risk score over shared entities, or counts over joint flows): lead with **MPC** for that bounded computation, using PSI as the entity-alignment step feeding it, and **DP** on published metrics.

A pragmatic combined stack: **PSI to align entities → MPC for the joint risk computation on aligned entities → DP on any externally reported aggregate → clean-room controls (query limits, thresholds, audit) wrapping the whole thing.** See [MPC Analytics Pipeline](../pet-architectures/mpc-analytics-pipeline.md).

!!! tip "Start with the question, not the cryptography"
    "Do we need overlap, or do we need a joint computation?" decides whether PSI or MPC is the spine. Many programs over-engineer toward MPC when a governed PSI plus thresholds would meet the need at a fraction of the cost.

## 5. Threat Model

| Element | Position |
| --- | --- |
| Adversary | A curious-but-competitive partner bank trying to learn another's customers; a colluding subset of banks; a curious coordinator; an external attacker. |
| Trust boundaries | Each bank trusts only its own systems. The coordinator is at most semi-trusted. PSI/MPC are chosen precisely so no party (including the coordinator) sees another's raw inputs. |
| What this design protects | Non-matching customers stay hidden (PSI). Raw transactions and inputs to the joint computation stay private (MPC). Published aggregates carry a formal leakage bound (DP). Query governance limits probing via repetition. |
| What is **not** protected | The *agreed output* — the match set or joint score — is revealed by design and is itself sensitive; governance, not cryptography, controls its use. A **colluding majority** can break standard MPC/PSI assumptions; the design must state the collusion threshold it tolerates. Repeated legitimate queries still leak slowly unless rate-limited. Weak or inconsistent identifiers cause false matches that harm customers. See [Collusion](../threat-models/collusion.md) and [Inference Attacks](../threat-models/inference-attacks.md). |

!!! warning "Collusion assumptions are the load-bearing wall"
    PSI and MPC guarantees are stated relative to a collusion bound (e.g., "secure against any minority of colluding parties"). If real-world incentives make majority collusion plausible — or if the coordinator can collude with one bank — the guarantee you are relying on may not hold. Write the tolerated collusion threshold down and check it against reality.

## 6. What To Measure

| Question | Metric | Evidence level (illustrative target) |
| --- | --- | --- |
| Privacy | Smallest released cohort size; leakage from repeated queries; DP budget on published metrics | Needs evidence |
| Utility | Detection lift over each bank's standalone fraud detection; precision/recall on known rings | Expert judgment (2026-06-10): cross-institution signal should add real lift on ring-type fraud; quantify it |
| False positives | False-positive rate and downstream cost of wrongly flagged accounts | Needs evidence — operationally critical |
| Latency | Time-to-decision for PSI/MPC round vs. the operational fraud window | Needs evidence — short windows can rule out heavy MPC |
| Collusion safety | Documented collusion threshold and what a colluding subset learns | Expert judgment (2026-06-10): must be stated explicitly per protocol |
| Cost | Per-query compute/communication; analyst workflow integration effort | Expert judgment (2026-06-10): governance and integration often cost more than the crypto |
| Complexity | Operational burden of running multi-party protocols across competing institutions | Expert judgment (2026-06-10): inter-org coordination dominates |

## 7. What Would Change The Decision

| Tripwire | New direction |
| --- | --- |
| The need shifts from "who overlaps" to "a shared predictive model" | Move toward **federated learning** for a joint fraud model, layering secure aggregation and DP. |
| Latency budget cannot absorb MPC | Fall back to **governed PSI plus thresholds** for the operational path and reserve MPC for periodic offline analytics. |
| Collusion analysis shows majority collusion is realistic | Standard PSI/MPC guarantees weaken; strengthen governance, reduce the party set, or introduce a strongly trusted (e.g., regulator-operated, TEE-backed) coordinator. |
| Regulators permit a supervised central utility | Re-evaluate a **governed central clean room** — sometimes the lawful, audited path beats multi-party cryptography on cost and speed. |
| Identifier quality is poor | Fix identifier hygiene first; bad matches make any PET output untrustworthy. |
| Only the *reported statistics* leave the consortium | The crypto can be lighter; invest in **DP and small-cell suppression** on the release rather than heavyweight joint computation. |

!!! note "The honest summary"
    PSI tells you who overlaps; MPC lets you compute on the overlap without revealing inputs; DP protects what you publish. None of them decide *whether you are allowed to act on a match* — that is governance, and it is where this kind of program most often fails.
