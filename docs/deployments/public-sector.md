# Public-Sector Deployments

!!! warning "Deployment evidence"
    Public-sector PET deployments can be unusually visible, but they are still contested. Look for both implementation evidence and impact on data users.

## Measured Production And Recurring Deployments

### 2020 U.S. Census Disclosure Avoidance System

| Field | Entry |
| --- | --- |
| Organization / project | U.S. Census Bureau 2020 Disclosure Avoidance System |
| Domain | Public sector / official statistics |
| Problem | Release detailed census data while protecting respondent confidentiality against reconstruction and reidentification risks. |
| PETs used | Differential privacy, disclosure avoidance system, post-processing |
| Deployment maturity | Production |
| Source quality | Primary / official plus independent analysis |
| What worked | The Census Bureau used the Disclosure Avoidance System for 2020 Census data products and published extensive documentation. |
| Challenges | The deployment created major utility, communication, and stakeholder-trust debates, especially for small geographies and detailed counts. |
| Lessons for builders | DP deployments need public budget decisions, user education, demonstration data, and a plan for utility disputes. Formal privacy does not remove policy tradeoffs. |
| Source | [Census Bureau Decennial Census Disclosure Avoidance](https://www.census.gov/programs-surveys/decennial-census/disclosure-avoidance.2020.html) and [2020 Disclosure Avoidance FAQ](https://www.census.gov/about/policies/privacy/statistical_safeguards/data-protection-faq.html) |

*(Evidence: Deployment-backed / literature-backed. Source quality: Primary / official plus independent analysis. Reviewed 2026-06-17 — production use is clear, and public criticism is part of the evidence base.)*

### Boston wage-gap analysis using MPC

| Field | Entry |
| --- | --- |
| Organization / project | Boston Women's Workforce Council and Boston University Hariri Institute |
| Domain | Public sector / civic labor analytics |
| Problem | Measure gender and racial wage gaps across employers while protecting employer-submitted wage data. |
| PETs used | Secure multiparty computation |
| Deployment maturity | Production, batch / periodic civic analytics workflow |
| Source quality | Primary / official plus third-party case study |
| What worked | BWWC describes using MPC in its wage-gap analysis process and reports aggregated findings. |
| Challenges | MPC protects submitted inputs for the computation, but the released aggregate analysis still needs careful interpretation and cohort controls. |
| Lessons for builders | Civic analytics can use MPC for trust-building, but reporting design and participant communication remain central. |
| Source | [Boston Women's Workforce Council: Data Privacy](https://thebwwc.org/mpc) |

*(Evidence: Deployment-backed. Source quality: Primary / official plus UN case study. Reviewed 2026-06-17 — recurring batch deployment evidence is unusually strong for civic MPC; output privacy remains a separate question.)*

## Common Proposed Use Cases

| Use case | Candidate PETs | Why proposed | Caveats |
| --- | --- | --- | --- |
| Official statistics releases | DP, synthetic data | Agencies must publish useful data under confidentiality mandates | Utility loss and public communication are hard |
| Cross-agency benefit analytics | MPC, clean rooms, TEEs | Agencies need joint analysis across legal boundaries | Governance and purpose limitation may dominate |
| Public-health dashboards | Federated analytics, DP | Local data can stay with health departments | Small geographies and rare conditions leak |
| Digital identity and eligibility checks | PSI, verifiable credentials, MPC | Agencies need yes/no checks without broad data sharing | The match result can still be sensitive |

## Lessons Learned

- Public deployments need legitimacy, not only technical correctness.
- Formal privacy parameters become policy choices when outputs affect funding, representation, or rights.
- Demonstration data and stakeholder review are part of deployment, not afterthoughts.
- PETs can enable civic collaboration, but they cannot settle acceptable-use disputes by themselves.
