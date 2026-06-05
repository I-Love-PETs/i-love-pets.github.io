# Tool Evaluation Framework

This page is for evaluating PET tools without turning the guide into an awesome list.

A tool belongs here only when the evaluation helps a reader decide whether the tool fits a concrete PET architecture, threat model, or benchmark.

## Evaluation Summary

| Question | Why it matters |
| --- | --- |
| What does this help build? | Tools should map to patterns and architectures, not vague PET categories. |
| What protected asset does it cover? | Inputs, updates, prompts, embeddings, outputs, logs, or model weights need different controls. |
| What adversary is in scope? | Honest-but-curious, malicious, colluding, platform, inference, or side-channel attackers change the conclusion. |
| What evidence supports the claim? | Documentation is not the same as a benchmark, proof, deployment, or audit. |
| What breaks in production? | Setup, keys, logs, latency, upgrades, and debugging are part of fit. |
| What benchmark should be run first? | A tool review should produce a first measurement, not just a vibe. |

## Fit Matrix

| Tool fit | Use this label when... | Review action |
| --- | --- | --- |
| Strong fit | The tool supports the architecture, threat model, and workload with evidence | Link to benchmark or deployment evidence |
| Promising fit | The tool supports the pattern but evidence is thin | Mark as expert judgment and define first benchmark |
| Narrow fit | The tool works for a constrained workload | State constraints clearly |
| Poor fit | The tool solves a different problem than the page needs | Do not list it as a recommendation |
| Unknown fit | The review lacks evidence | Move to claim register or Fix My Itch |

## Evidence Checklist

- Is there a security proof, specification, or design document?
- Are supported threat models explicit?
- Are limitations and non-goals documented?
- Are benchmarks reproducible?
- Are deployment examples named and maturity-labeled?
- Are operational requirements documented: keys, logs, monitoring, upgrades, incident response?
- Has the tool been evaluated by someone other than the vendor or maintainer?

## First Benchmark By Tool Type

| Tool type | First benchmark |
| --- | --- |
| FL framework | Non-IID cross-silo training with dropouts, per-site utility, and update leakage review |
| DP library | Privacy accounting and utility curve for a specific release |
| MPC framework | Private aggregate or join with parties, rounds, bandwidth, and dropout behavior |
| HE inference tool | End-to-end latency, ciphertext size, supported operators, and accuracy loss |
| TEE platform | Attestation verification, log review, side-channel assumptions, and failure behavior |
| Synthetic data tool | Memorization tests, downstream utility, DP parameters if claimed |
| Clean-room platform | Query controls, minimum thresholds, output review, repeated-query tests |

## Red Flags

- The tool says "privacy-preserving" but does not name a protected asset.
- The threat model is missing or only appears in a paper, not product documentation.
- Benchmarks omit hardware, data shape, parameter settings, or failed cases.
- The tool requires plaintext logs, support bundles, or debugging paths that violate the claim.
- The tool is recommended for a page even though it only supports a different workload.
- The review lists features but never says when not to use the tool.

## Review Output

A tool review should end with:

- best-fit architecture or pattern;
- threat model support;
- evidence level;
- first benchmark to run;
- operational risks;
- when not to use it;
- whether the tool should be recommended, watched, or rejected for this guide.
