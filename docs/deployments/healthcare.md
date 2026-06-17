# Healthcare Deployments

!!! warning "Deployment evidence"
    Healthcare PET claims often mix research studies, clinical pilots, and vendor platform stories. Do not assume clinical production use unless the source clearly says so.

## Published Studies And Pilots

### EXAM federated learning for COVID-19 oxygen prediction

| Field | Entry |
| --- | --- |
| Organization / project | EXAM, a federated learning study across 20 institutions |
| Domain | Healthcare |
| Problem | Train a model to predict future oxygen requirements for symptomatic COVID-19 patients using EMR, labs, vital signs, and chest X-rays without centralizing all institutional data. |
| PETs used | Federated learning |
| Deployment maturity | Research prototype / demonstration experiment |
| Source quality | Peer-reviewed / academic |
| What worked | The study demonstrated multi-institution FL across 20 institutions and reported performance across sites. |
| Challenges | Research success does not prove clinical workflow integration, privacy from updates, poisoning resistance, or ongoing operations. |
| Lessons for builders | FL can coordinate real healthcare institutions, but clinical utility, local data quality, update leakage, and governance must be evaluated separately. |
| Source | [Nature Medicine: Federated learning for predicting clinical outcomes in patients with COVID-19](https://www.nature.com/articles/s41591-021-01506-3) |

*(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. Reviewed 2026-06-17 — the paper reports a 20-institution study and AUC results, but it is evidence for research feasibility rather than routine clinical production.)*

### MELLODDY cross-pharma federated learning

| Field | Entry |
| --- | --- |
| Organization / project | MELLODDY consortium |
| Domain | Healthcare / life sciences |
| Problem | Let pharmaceutical companies improve QSAR models using sensitive proprietary chemical and bioactivity data without pooling data. |
| PETs used | Federated learning, privacy-preserving platform controls |
| Deployment maturity | Completed consortium pilot / demonstration experiment |
| Source quality | Primary / official plus peer-reviewed / academic |
| What worked | The project ran a large cross-company FL experiment and reported aggregated model improvements for participating companies. |
| Challenges | The result is strong evidence for cross-company feasibility, not a generic proof that FL protects all proprietary information or works for every discovery task. |
| Lessons for builders | Cross-silo FL needs shared task definitions, platform trust, data harmonization, and agreement about what model improvements can reveal. |
| Source | [MELLODDY paper in Journal of Chemical Information and Modeling](https://pmc.ncbi.nlm.nih.gov/articles/PMC11005050/) |

*(Evidence: Deployment-backed / literature-backed. Source quality: Primary / official plus peer-reviewed / academic. Reviewed 2026-06-17 — MELLODDY is strong feasibility evidence for cross-pharma FL; ongoing production after the consortium remains unverified.)*

## Common Proposed Use Cases

| Use case | Candidate PETs | Why proposed | Caveats |
| --- | --- | --- | --- |
| Hospital quality metrics without sharing patient records | Federated analytics, MPC, DP | Hospitals can compute comparable metrics locally | Small cohorts and inconsistent coding can leak or mislead |
| Multi-hospital model training | FL, secure aggregation, DP | Data cannot centralize across institutions | FL alone does not provide privacy; non-IID data can hurt smaller sites |
| Private clinical trial matching | PSI, TEEs, clean rooms | Match patients to eligibility criteria without broad data exposure | Match output may be sensitive; governance matters |
| Synthetic patient datasets for research | DP synthetic data | Researchers need data-like artifacts | Synthetic data can memorize or lose rare-case utility |

## Lessons Learned

- Healthcare deployments need clinical validation, not only privacy-preserving computation.
- The protected artifact must be named: records, updates, identifiers, model weights, outputs, logs, or all of them.
- Cross-institution projects often fail on data definitions before they fail on PET mechanics.
- Small cohorts, rare diseases, and site-specific patterns need special treatment.
