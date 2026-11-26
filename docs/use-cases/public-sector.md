# Public Sector

--8<-- "decision-guidance.md"

Public-sector PET decisions must balance public benefit, confidentiality, legitimacy, accessibility, procurement, and the need for understandable tradeoffs.

## Scenario Playbook

| Scenario | Primary PET | Supporting PETs | Why | What can go wrong | What to measure |
| --- | --- | --- | --- | --- | --- |
| Official statistics release | Differential privacy | Post-processing, utility evaluation, public documentation | A formal contribution bound can support publication where the mandate permits DP | Utility disputes, misunderstood epsilon, small-area harm | Error by geography/group, privacy budget, stakeholder impact |
| Agencies compute joint eligibility or outcomes | MPC or clean room | Audit logs, purpose controls, thresholds | Agencies can collaborate without broad raw-data pooling | Governance is unclear, outputs affect rights | Accuracy, appeals process, allowed use, auditability |
| Public-health dashboard | Federated analytics | DP, suppression, grouping | Local agencies can keep source data local | Rare conditions and small geographies leak | Small-cell risk, timeliness, interpretability |
| Open-data exploration | DP synthetic data | Residual-risk labels, utility tests | Public users get a data-like artifact | Synthetic data is treated as ground truth | Utility for intended tasks, memorization, misuse risk |

## Use This When

- The public benefit is specific and documented.
- The output can be explained to non-specialists.
- The privacy/utility tradeoff is reviewable.
- The deployment includes public communication and recourse where decisions affect people.

## Avoid This When

- The PET hides a policy decision that should be debated publicly.
- The output affects benefits, enforcement, or rights without appeal.
- Utility loss will fall hardest on small communities.
- Accessibility and documentation are treated as optional.

## Recommended Starting Stack

For public statistics, consider **differential privacy** when the publication mandate permits it. Report task-level utility, including error for small geographies and groups. The [U.S. Census policy update](../deployments/deep-dives/us-census-dp.md#policy-update) shows why a historical deployment does not determine what is allowed today. For interagency computation, start with **MPC or a governed clean room**, then add thresholds and audit controls.

These sketches assume a trusted curator for central DP and public recipients who can combine releases. If the curator must not see raw contributions or the mandate forbids noise, reconsider the processing and release model before choosing a mechanism.

## Failure Modes

- Formal privacy parameters become opaque policy choices.
- Small-area statistics become unreliable without clear communication.
- Synthetic data is reused outside intended purposes.
- Procurement selects a PET tool without a threat model.
- Public trust is damaged because tradeoffs were hidden.

## Evaluation Checklist

- Who benefits, who bears utility loss, and who can challenge decisions?
- Are privacy parameters and release rules publicly documented?
- Are small populations analyzed separately?
- Does the system meet accessibility and transparency expectations?
- Are deployment claims independently reviewable?

## Related Pages

- [Public-sector deployments](../deployments/public-sector.md)
- [Differential privacy](../start-here/pet-taxonomy.md#differential-privacy)
- [Benchmarks](../benchmarks/index.md)
