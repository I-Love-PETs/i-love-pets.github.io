# Japanese Banks Federated Fraud Detection

!!! warning "Read the evidence levels"
    This is a useful finance example because the paper names five banks and says the demonstration used real transaction data. It is still a demonstration experiment, not public evidence of a deployed production fraud-detection network. Reference date: 2026-06-17.

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | Privacy-preserving federated learning demonstration with five Japanese banks |
| Domain | Finance / fraud and financial-crime detection |
| Problem | Detect fraudulent financial transactions and criminal bank accounts across institutions without sharing transaction data with a third party |
| PETs used | Federated learning with the Deepprotect privacy-preserving protocol |
| Deployment maturity | Demonstration experiment |
| Source quality | Peer-reviewed / academic |
| Source | [Journal of Information Processing: Privacy-Preserving Federated Learning for Detecting Fraudulent Financial Transactions in Japanese Banks](https://www.jstage.jst.go.jp/article/ipsjjip/30/0/30_789/_article) |

## What Was Actually Deployed

The paper reports a demonstration experiment with five named banks: Chiba Bank, MUFG Bank, Chugoku Bank, Sumitomo Mitsui Trust Bank, and Iyo Bank. The authors state that the experiment used real transaction data and evaluated two fraud tasks: detecting fraudulent transactions in victim accounts and detecting criminal bank accounts. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic.)*

The underlying protocol, called Deepprotect, supports privacy-preserving deep-learning training with stochastic gradient descent. The paper frames the work as a response to two finance realities: local banks may not have enough fraud examples alone, and transaction data contains personal information that is legally restricted from ordinary third-party sharing. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic.)*

Reported outcome:

- The authors report that the federated system detected fraudulent transactions not detected by a single-bank model and detected some criminal bank accounts before the bank froze them. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. Treat as study-specific, not a general production lift.)*

## Maturity

**Demonstration experiment.** The source itself uses demonstration language. It is stronger than a synthetic benchmark because it involves named banks and real transaction data, but it does not establish a live, continuously operated cross-bank fraud system. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic.)*

## Privacy Claim

The supported claim is **collaborative model training without ordinary cross-bank data sharing**. The paper claims a privacy-preserving FL protocol for the training task and positions it against the legal and practical difficulty of sending transaction data to a third party.

The claim is not enough by itself to approve a production anti-fraud network. A production deployment would still need a threat model for collusion, malicious participants, identity alignment, inference from model outputs, false-positive handling, account-freeze governance, auditability, and customer-impact review. *(Evidence: Expert judgment. Source quality: Project analysis.)*

## Limitations

- **Production adoption is not established.** The public source is a demonstration paper, not a regulator filing, bank operations report, or production postmortem. *(Needs evidence.)*
- **Operational harm matters.** Fraud models can trigger investigations, freezes, or customer friction; privacy-preserving training does not solve false positives or appeal processes. *(Expert judgment.)*
- **Fraudsters are adaptive.** A cross-bank FL network must be tested against poisoning, drift, strategic behavior, and delayed labels, not only static accuracy. *(Expert judgment.)*
- **Privacy scope is narrower than "all fraud analytics are private."** The protected artifact is training data during the FL workflow; outputs and downstream decisions remain sensitive. *(Expert judgment.)*

## Builder Lessons

- **Treat real-bank demonstrations as valuable but bounded.** The result supports feasibility, not production readiness.
- **Measure detection lift per participant.** Cross-bank signal is most useful if it helps smaller or less fraud-rich institutions without harming others.
- **Make governance part of the benchmark.** False-positive workflows, data-subject rights, and investigator access are not afterthoughts in finance.
- **Test against adversarial participants.** Fraud detection is a strategic environment; benign cross-silo assumptions need stress testing before launch.

## What Remains Unclear

- Whether any participating bank put the trained approach into a live fraud-detection workflow. *(Needs evidence.)*
- The production-scale latency, bandwidth, model-maintenance, and participant-onboarding costs. *(Needs evidence.)*
- How the protocol behaves under collusion, malicious updates, label drift, or identity-resolution errors in production. *(Needs evidence.)*
- Whether customer-impact governance was evaluated alongside detection performance. *(Needs evidence.)*

## Sources

- Kanamori et al., [Privacy-Preserving Federated Learning for Detecting Fraudulent Financial Transactions in Japanese Banks](https://www.jstage.jst.go.jp/article/ipsjjip/30/0/30_789/_article), Journal of Information Processing, 2022.
