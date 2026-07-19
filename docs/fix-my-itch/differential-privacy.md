# Differential Privacy

Differential privacy gives the clearest formal privacy language in this guide, but deployed teams still struggle with budgets, audits, and utility under real constraints.

## Research Handoff

| Problem | Who benefits if solved | Why it is difficult | Starting directions |
| --- | --- | --- | --- |
| Privacy budgets people can defend | Privacy reviewers, product owners, policy teams, and data scientists | Epsilon is not intuitive, and budget choice depends on privacy unit, cadence, utility, and harm model | Build a worksheet; connect budgets to attack examples; plot utility and release-count tradeoffs |
| Auditing DP claims in deployed systems | Auditors, regulators, buyers, and platform owners | DP depends on implementation details, composition, sampling, clipping, and release lineage | Define required artifacts; audit two open runs; include accounting and implementation tests |
| Useful DP fine-tuning for LLMs | Enterprises, ML researchers, and privacy engineers | DP training can be costly and low-utility, especially for small sensitive datasets | Benchmark adapters; report compute and utility; include memorization probes and budget accounting |
| DP for small cohorts | Public agencies, healthcare analytics teams, advertisers, and clean-room users | Small groups are where utility and privacy collide most sharply | Compare suppression, grouping, and hierarchical releases; report which groups lose utility; document decision rules |

## Privacy Budgets People Can Defend

| Field | Card |
| --- | --- |
| Problem | How can teams choose privacy budgets without pretending epsilon is intuitive? |
| The itch | Reviewers ask whether an epsilon is "good," but the answer depends on the privacy unit, release count, neighboring relation, and harm model. |
| Why it matters | Teams either pick arbitrary budgets or avoid DP because they cannot explain it. |
| Current workaround | Copy values from papers, choose round numbers, or bury the decision in a privacy review. |
| Why the workaround is insufficient | It produces claims that are hard to compare, audit, or defend after repeated releases. |
| What good progress would look like | A decision aid that connects budget choice to examples, attack simulations, utility loss, and release accounting. |
| Difficulty | Medium |
| Good for | Privacy engineer, policy researcher, ML researcher |
| Related PETs | DP, synthetic data, federated analytics |
| Possible first contribution | Build a budget-selection worksheet for one use case, including privacy unit, release cadence, utility curves, and reviewer questions. |

## Auditing DP Claims In Deployed Systems

| Field | Card |
| --- | --- |
| Problem | How can we audit DP claims in deployed ML systems? |
| The itch | A model or report may say it used DP, but auditors need to verify implementation details, accounting, and release history. |
| Why it matters | False or unverifiable DP claims can create regulatory, user-trust, and safety failures. |
| Current workaround | Trust vendor statements, inspect code informally, or review one training run. |
| Why the workaround is insufficient | DP depends on composition, sampling, clipping, random seeds, privacy unit choices, and all releases over time. |
| What good progress would look like | An audit checklist and artifact format that captures DP parameters, accounting, implementation tests, and release lineage. |
| Difficulty | Medium |
| Good for | Privacy engineer, benchmark maintainer, policy researcher |
| Related PETs | DP, FL, synthetic data |
| Possible first contribution | Create an audit template for DP-SGD runs and apply it to two open implementations. |

## Useful DP Fine-Tuning For LLMs

| Field | Card |
| --- | --- |
| Problem | How can DP fine-tuning for LLMs be made useful under realistic compute budgets? |
| The itch | DP-SGD can be expensive and can hurt utility, especially when teams fine-tune large models on small sensitive datasets. |
| Why it matters | Enterprises want adaptation without memorizing sensitive records, but many cannot afford large experiments. |
| Current workaround | Redact data, fine-tune without DP, or rely on vague memorization checks after training. |
| Why the workaround is insufficient | Redaction misses secrets, non-DP fine-tuning can memorize, and post-hoc checks do not provide a formal guarantee. |
| What good progress would look like | Practical recipes for adapters, clipping, accounting, and evaluation that show privacy/utility/compute tradeoffs. |
| Difficulty | Hard |
| Good for | ML researcher, privacy engineer, systems builder |
| Related PETs | DP, private LLM fine-tuning, TEEs |
| Possible first contribution | Benchmark DP adapter fine-tuning on a small domain dataset with memorization probes, utility tasks, and compute reporting. |

## DP For Small Cohorts

| Field | Card |
| --- | --- |
| Problem | How should teams handle DP when cohorts are too small for useful noisy outputs? |
| The itch | Real deployments often need local statistics for small hospitals, rare diseases, small advertisers, or niche user groups. |
| Why it matters | Suppressing all small groups can make a system useless, but releasing them can leak sensitive facts. |
| Current workaround | Use minimum thresholds, merge groups manually, or release noisy values with weak utility. |
| Why the workaround is insufficient | It is ad hoc and often hides which groups lost utility or protection. |
| What good progress would look like | A playbook for grouping, suppression, hierarchical release, and utility reporting under DP. |
| Difficulty | Good first research problem |
| Good for | Privacy engineer, benchmark maintainer, policy researcher |
| Related PETs | DP, federated analytics, clean rooms |
| Possible first contribution | Compare thresholding, grouping, and hierarchical DP on one small-cohort analytics task and publish failure cases. |
