# Deployments

!!! warning "Treat deployment claims carefully"
    Deployment claims should be treated carefully. Many PET projects are pilots, proof-of-concepts, research prototypes, or vendor case studies rather than independently evaluated production systems.

This section tracks PET deployments as evidence, not as marketing proof. A useful entry should say who used what, how mature the deployment appears to be, how good the source is, what worked, what was hard, and what builders should learn.

## Sort Deployments Before Reading Them

Do not flatten every example into "real-world use." The useful first question is what kind of evidence the entry provides.

| Bucket | Meaning | How to use it |
| --- | --- | --- |
| Measured deployment | A named production or recurring workflow with public parameters, outputs, or evaluation detail | Strongest source for operational lessons, still scoped to its domain |
| Pilot or demonstration | Real organizations or real data, but limited or time-boxed operation | Useful feasibility evidence; do not generalize production readiness |
| Vendor case study | A vendor or platform describes a customer/product deployment | Useful lead; require independent validation before procurement-grade conclusions |
| Proposed use case | Plausible use with no named deployment evidence on the page | Treat as design space, not evidence |

## Deployment Entry Format

| Field | What to record |
| --- | --- |
| Organization / project | The named organization, consortium, product, or public project |
| Domain | Healthcare, finance, advertising, public sector, or another domain |
| Problem | The concrete collaboration, release, measurement, or inference problem |
| PETs used | PET families and supporting controls |
| Deployment maturity | Production, production batch/periodic, pilot, demonstration experiment, research prototype, vendor case study, proposed use case, or unclear |
| Source quality | Primary/official, peer-reviewed/academic, independent analysis, vendor case study, press/secondary, or illustrative/unsourced |
| What worked | Evidence-backed benefits or claimed benefits with source-quality caveats |
| Challenges | Utility, cost, governance, usability, trust, attacks, operations, or public criticism |
| Lessons for builders | Transferable design lessons |
| Source | Link to primary documentation, paper, regulator report, or credible case study |

## Maturity Labels

| Label | Meaning |
| --- | --- |
| Production | Used in a live public, commercial, or institutional workflow |
| Production, batch / periodic | Used in a real workflow, but run as a periodic release or recurring study rather than an always-on service |
| Pilot | Tested with real organizations or real data but not clearly sustained as production |
| Demonstration experiment | Tested with real partners or realistic data to prove feasibility; operational adoption is not established |
| Research prototype | Published experiment, demo, or study, often with real partners or data |
| Vendor case study | Described mainly by a vendor, platform operator, or customer story |
| Proposed use case | Plausible application without named deployment evidence on the page |
| Unclear | The source does not provide enough information to classify maturity |

## Source Quality Labels

| Label | Meaning |
| --- | --- |
| Primary / official | The deploying organization, regulator, standards body, or project team documents the system |
| Peer-reviewed / academic | A paper or technical report provides methods, results, and limitations |
| Independent analysis | A non-operator evaluates utility, privacy, or impact |
| Vendor case study | Product or marketing material from the vendor or platform operator |
| Press / secondary | News, blog, analyst, or conference coverage |
| Unsourced / illustrative | Maintainer-created example with no decision-grade source |

*(Evidence: Expert judgment. Source quality: Project standard. Reviewed 2026-06-17 — the labels are an editorial calibration scheme; they do not by themselves prove a claim.)*

## How To Read These Pages

- Prefer primary sources, peer-reviewed papers, regulator documents, and official documentation.
- Treat vendor case studies as useful but incomplete evidence.
- Look for the output that was actually released or used.
- Ask whether the PET protected inputs, outputs, both, or neither.
- Check whether the deployment was independently evaluated.
- Keep proposed use cases separate from measured deployments when making a decision memo.

## Domain Pages

- [Healthcare](healthcare.md)
- [Finance](finance.md)
- [Advertising](advertising.md)
- [Public Sector](public-sector.md)

## Use Deployment Evidence Carefully

| If you see... | Treat it as... | Next check |
| --- | --- | --- |
| A named production workflow with parameters and outputs | Useful operational evidence | Whether your data shape, adversary, and output match |
| A pilot with real partners | Feasibility evidence | Whether sustained operations, cost, and governance were measured |
| A vendor case study | A lead worth investigating | Independent validation, benchmark details, and customer controls |
| A proposed use case | Design inspiration | Do not cite it as deployment proof |

## Related Guides

- [Evidence Policy](../project-standards/evidence-policy.md) for source-quality labels.
- [Claim Register](../project-standards/claim-register.md) for unresolved evidence gaps.
- [Worked Decisions](../worked-decisions/index.md) for adapting evidence to a concrete PET choice.
