# Finance Deployments

!!! warning "Deployment evidence"
    Financial PET projects are often described through vendor case studies, consortium announcements, or research demonstrations. Treat maturity labels conservatively.

## Documented Real Deployments And Studies

### TriBank / Amlytic privacy-preserving financial-crime analytics

| Field | Entry |
| --- | --- |
| Organization / project | Amlytic, Secretarium, FutureFlow, and TriBank Initiative references |
| Domain | Finance |
| Problem | Pool cross-institution transaction intelligence for financial-crime detection without exposing raw institutional transaction data. |
| PETs used | Secure multiparty pseudonymisation, privacy-preserving matching, de-identified graph analytics |
| Deployment maturity | Pilot / unclear production maturity |
| What worked | Public materials describe use of privacy-preserving matching and analytics to combine financial-institution contributions. |
| Challenges | Source material is vendor-operated and does not provide an independent production evaluation, false-positive analysis, or detailed threat model. |
| Lessons for builders | Cross-bank analytics needs privacy-preserving entity resolution, governance over outputs, and careful distinction between de-identified analytics and formal privacy guarantees. |
| Source | [Amlytic product and TriBank description](https://amlytic.com/) |

### Japanese banks federated fraud-detection demonstration

| Field | Entry |
| --- | --- |
| Organization / project | Demonstration experiment with five Japanese banks |
| Domain | Finance |
| Problem | Test privacy-preserving federated learning for fraudulent financial transaction detection using real transaction data across banks. |
| PETs used | Federated learning |
| Deployment maturity | Research prototype / demonstration experiment |
| What worked | The paper reports a multi-bank demonstration using real transaction data and names participating banks. |
| Challenges | The authors describe it as a demonstration experiment; it should not be treated as evidence of production deployment. |
| Lessons for builders | Fraud FL needs real data, cross-bank governance, and operational design beyond model training. |
| Source | [IPSJ Journal of Information Processing: Privacy-Preserving Federated Learning for Detecting Fraudulent Financial Transactions in Japanese Banks](https://www.jstage.jst.go.jp/article/ipsjjip/30/0/30_789/_article) |

## Common Proposed Use Cases

| Use case | Candidate PETs | Why proposed | Caveats |
| --- | --- | --- | --- |
| Cross-bank fraud detection | FL, secure aggregation, MPC, DP | Fraudsters move across institutions | Poisoning, false positives, and latency can matter more than raw accuracy |
| AML graph analysis | MPC, PSI, privacy-preserving pseudonymisation, clean rooms | Institutions need joint network signals | Entity resolution and output governance are hard |
| Credit-risk benchmarking | Federated analytics, DP, clean rooms | Banks want peer comparison without exposing portfolios | Aggregates can reveal business-sensitive information |
| Customer overlap analysis | PSI, clean rooms | Institutions need match counts or permitted overlaps | The intersection itself may be sensitive |

## Lessons Learned

- Financial deployments need adversarial thinking: participants, customers, fraudsters, and insiders may all be strategic.
- Entity resolution is often the hidden hard problem.
- PETs can protect inputs while still producing outputs that reveal investigations or competitive data.
- Vendor case studies are useful leads, but production maturity and independent evaluation often remain unclear.
