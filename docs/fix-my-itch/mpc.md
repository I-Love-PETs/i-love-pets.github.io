# MPC

MPC can compute across private inputs without a single trusted operator, but normal backend teams often experience it as protocol-heavy, expensive, and hard to reason about before deployment.

## MPC For Normal Backend Engineers

| Field | Card |
| --- | --- |
| Problem | Why is MPC still too hard for normal backend engineers? |
| The itch | Developers who can ship APIs, queues, and databases still struggle with parties, circuits, preprocessing, threat models, and deployment ceremonies. |
| Why it matters | Useful private collaboration remains trapped in specialist teams. |
| Current workaround | Hire cryptographers, use vendor black boxes, or avoid MPC. |
| Why the workaround is insufficient | It slows adoption and makes security claims hard for application teams to inspect. |
| What good progress would look like | Developer abstractions that expose parties, allowed outputs, collusion assumptions, and cost without requiring protocol expertise. |
| Difficulty | Hard |
| Good for | Systems builder, cryptographer, backend engineer |
| Related PETs | MPC, PSI, clean rooms |
| Possible first contribution | Build a small MPC service template for one analytics task with deployment diagrams, cost estimates, and failure-mode docs. |

## Cost Before Deployment

| Field | Card |
| --- | --- |
| Problem | How can MPC systems explain cost before deployment? |
| The itch | Teams often discover round trips, bandwidth, preprocessing, and cloud costs after they have already designed the workflow. |
| Why it matters | A technically correct MPC design can be commercially unusable. |
| Current workaround | Run prototypes late or ask vendors for estimates. |
| Why the workaround is insufficient | Estimates are workload-specific and often omit availability, retries, and operational overhead. |
| What good progress would look like | A cost model that predicts latency, bandwidth, compute, and failure sensitivity from a high-level computation. |
| Difficulty | Medium |
| Good for | Systems builder, benchmark maintainer, cryptographer |
| Related PETs | MPC, PSI, HE |
| Possible first contribution | Create a cost calculator for private sum, private join, and logistic-regression inference across two and three parties. |

## Malicious Security Usability

| Field | Card |
| --- | --- |
| Problem | What developer abstractions make malicious security usable? |
| The itch | Honest-but-curious demos are easier, but real deployments may involve parties that send malformed inputs or deviate from the protocol. |
| Why it matters | Finance, ad measurement, and public-sector collaborations often cannot rely on all parties behaving perfectly. |
| Current workaround | Use semi-honest protocols plus contracts, audits, or manual input checks. |
| Why the workaround is insufficient | It leaves protocol deviation and adaptive abuse outside the technical guarantee. |
| What good progress would look like | APIs and examples that make malicious-security choices visible, testable, and explainable to non-cryptographers. |
| Difficulty | Hard |
| Good for | Cryptographer, systems builder, privacy engineer |
| Related PETs | MPC, PSI |
| Possible first contribution | Write two versions of the same MPC task, semi-honest and malicious-secure, with measured overhead and developer-facing explanations. |

## MPC Output Governance

| Field | Card |
| --- | --- |
| Problem | How should MPC deployments control outputs that are technically correct but privacy-invasive? |
| The itch | MPC protects inputs during computation, but the result may still reveal sensitive facts. |
| Why it matters | Teams can overclaim privacy while releasing tiny cohorts, sensitive matches, or commercially revealing metrics. |
| Current workaround | Add manual review after protocol design. |
| Why the workaround is insufficient | Output policy is often not encoded in the computation or test plan. |
| What good progress would look like | MPC workflows with built-in thresholding, allowed-output schemas, DP options, and audit logs. |
| Difficulty | Medium |
| Good for | Privacy engineer, systems builder, policy researcher |
| Related PETs | MPC, DP, clean rooms |
| Possible first contribution | Implement a private aggregate with configurable suppression thresholds and document which outputs remain unsafe. |
