# Privacy Benchmarks

!!! info "Review status"
    Last reviewed: 2026-09-16

    Evidence level: Expert judgment

    Source quality: Unsourced / illustrative

    Snapshot scope: Editorial measurement guidance. Validate the method and acceptance thresholds for your workload; examples are illustrative.

## Definition

A privacy benchmark tests a specific claim about a protected asset against a defined adversary. An attack evaluation describes what happened under the tested conditions. A formal guarantee depends on its stated model and implementation assumptions; a failed attack does not prove that guarantee.

## What to measure

| Claim | Measurement or review |
| --- | --- |
| Model updates are protected | Gradient leakage and reconstruction tests with explicit coordinator visibility |
| Training records are protected | Membership inference evaluation and, where applicable, DP accounting |
| Synthetic records resist disclosure | Memorization, nearest-neighbor audits, and attacks with nonmember baselines |
| Query outputs limit disclosure | Differencing, small-cell, repeated-query tests, and release accounting |
| Runtime is confidential | Attestation checks, plaintext/log inspection, and scoped side-channel review |

For DP, record the privacy unit, adjacency relation, contribution bounds, epsilon, delta where applicable, accountant, and composition across releases. For HE/MPC, record the security parameters, adversary model, key holders, collusion threshold, and allowed output. For TEEs, record the trusted components, attestation policy, software image, and excluded attack classes.

## Measurement methodology

1. State the asset, attacker access, auxiliary information, allowed output, and query or compute budget. Identify what the test cannot observe.
2. Choose attacks that address the claim. Use a vulnerable control to check that the test can detect leakage, and a nonmember or other appropriate negative control to estimate false positives.
3. Keep attack tuning separate from evaluation. Match member and nonmember distributions as far as possible; record sampling, sample size, seeds, and any distribution mismatch.
4. Report success and false-positive rates at a fixed operating point, not just aggregate attack accuracy. For reconstruction, define the similarity metric and what counts as sensitive recovery before running the attack.
5. Repeat under relevant stress conditions: repeated queries, small cohorts, collusion, dropouts, changed permissions, or compromised logging. Review formal assumptions and implementation controls separately from empirical attack results.

The distinction between empirical testing and a formal DP guarantee follows the definitions in Dwork and Roth, [The Algorithmic Foundations of Differential Privacy](https://www.cis.upenn.edu/~aaroth/Papers/privacybook.pdf). *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. The book supports the DP definition and composition principles; it does not validate the illustrative experiment below.)*

## Worked comparison

!!! warning "Illustrative arithmetic, not a benchmark"
    Evidence level: Needs evidence. Source quality: Unsourced / illustrative. These invented counts describe one membership-inference operating point, not the privacy of a real model.

Assume an attacker has prediction access, a fixed query budget, and thresholds selected on a separate tuning set. Evaluate each system on the same 1,000 members and 1,000 nonmembers, at a 1% false-positive rate.

| Attack outcome | Vulnerable control | Protected candidate |
| --- | ---: | ---: |
| Members identified | 300 / 1,000 = 30% TPR | 80 / 1,000 = 8% TPR |
| Nonmembers incorrectly identified | 10 / 1,000 = 1% FPR | 10 / 1,000 = 1% FPR |
| TPR minus FPR at this threshold | 29 percentage points | 7 percentage points |

The candidate reduces attack success at this operating point but still shows a membership signal in the example. This does not establish a DP guarantee or rule out stronger attacks. A real comparison needs uncertainty intervals, attack details, model/data versions, utility results, and a justified acceptance rule. An attack that fails even against the vulnerable control provides little evidence about the candidate.

## Pitfalls

- Treating zero observed disclosures as zero risk or as a proof of privacy.
- Reporting membership attack accuracy without class balance, false-positive rate, or attacker access.
- Comparing epsilon values across different privacy units or composition scopes.
- Treating low nearest-neighbor similarity as proof that synthetic data is safe to publish.
- Inferring output privacy from encrypted computation or runtime isolation.
- Running only weak attacks, omitting failed controls, or generalizing beyond the tested threat model.

## Reporting

State the adversary, auxiliary information, query budget, and success metric. Attach control results, attack configuration, uncertainty, assumptions, and untested leakage channels to the [shared reporting template](scorecards.md#shared-reporting-template). Evaluate [utility](utility.md) and [cost](cost.md) under the same configuration.
