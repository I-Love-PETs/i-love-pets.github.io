# Fix My Itch

Fix My Itch is the part of I Love PETs for problems that practitioners keep hitting and researchers can actually make progress on.

The goal is not to list research areas. Each entry should describe a specific itch, the workaround people use today, why that workaround is not good enough, and what good progress would look like.

## Card Standard

Every problem card should answer:

| Field | Standard |
| --- | --- |
| Problem | A concrete problem a team can recognize in the field |
| The itch | What is frustrating, brittle, expensive, or missing today |
| Why it matters | Who is blocked or harmed while this remains unsolved |
| Current workaround | What teams actually do now |
| Why the workaround is insufficient | The specific failure, not "more research is needed" |
| What good progress would look like | A measurable improvement or usable artifact |
| Who benefits if solved | The practitioner, researcher, maintainer, buyer, auditor, or affected population that can use the result |
| Why it is difficult | The technical, operational, incentive, measurement, or adoption reason the workaround persists |
| Starting directions | Two or three plausible paths that do not require solving the whole field |
| Difficulty | Good first research problem, medium, hard, or moonshot |
| Good for | The kind of contributor who can make progress |
| Related PETs | The PET families involved |
| Possible first contribution | A small starting point that could be published, shipped, or benchmarked |

## Problem Map

| Area | Strong starting point | Typical output |
| --- | --- | --- |
| [Federated learning](federated-learning.md) | Realistic non-IID benchmarks and update safety | Benchmark suites, poisoning tests, lightweight tooling |
| [Differential privacy](differential-privacy.md) | Budget selection and claim auditing | Decision aids, audits, DP fine-tuning baselines |
| [MPC](mpc.md) | Developer usability and deployment cost prediction | Cost estimators, backend abstractions, malicious-security examples |
| [Homomorphic encryption](homomorphic-encryption.md) | Practical HE inference boundaries | Model/operator benchmarks, debugging tools |
| [TEEs](tees.md) | Attestation and side-channel reasoning | Risk checklists, portability tests, developer explanations |
| [Synthetic data](synthetic-data.md) | Memorization, utility, and residual-risk communication | Evaluation harnesses, model cards, release reviews |
| [PET composition](pet-composition.md) | End-to-end guarantees across PET stacks | Trust-boundary diagrams, composition tests |
| [Benchmarks needed](benchmarks-needed.md) | Cost/privacy/utility suites for realistic deployments | Reproducible benchmark tasks and scorecards |

## What Counts As A Good Itch

- A hospital, bank, public agency, platform team, or model provider would recognize the problem.
- The problem has a clear failure mode.
- A first contribution can be done without building a full production system.
- Success can be measured by more than citations.
- The card says when the PET does not solve the problem.
- The card names who benefits, why the workaround persists, and where a contributor can start.
