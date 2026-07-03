# Threat Models

Privacy claims are meaningless without a threat model. In PET systems, the threat
model is also the handoff between privacy engineering, security engineering, and
product governance: it says which leakage paths the PET is expected to reduce and
which ones need separate controls.

A useful threat model states:

- What data or behavior is protected
- Who the adversary is
- What the adversary can observe
- What the adversary can change
- Which parties may collude
- What output is intentionally revealed
- Which assumptions must hold

## Fast Checklist

| Question | Example |
| --- | --- |
| Who sees inputs? | Clients, silos, coordinator, cloud operator |
| Who sees outputs? | Analyst, model owner, all participants, public |
| Who can deviate? | Malicious client, curious coordinator, compromised enclave |
| What metadata leaks? | Timing, query volume, participant presence, cohort size |
| What repeats? | Queries, training rounds, release cycles |

## Failure Review

| If you discover... | Revisit... | Why |
| --- | --- | --- |
| The output itself is sensitive | [Inference attacks](inference-attacks.md) | Input privacy does not make released statistics, models, or answers safe. |
| One party can learn across repeated runs | [Collusion](collusion.md) and query controls | Repetition can turn safe-looking outputs into reconstruction signals. |
| Participants can submit bad inputs | [Malicious adversary](malicious-adversary.md) | Honest-but-curious assumptions do not cover poisoning or selective aborts. |
| Metadata is observable | [Side channels](side-channels.md) | Timing, cohort size, and error paths can reveal participation or attributes. |
| Membership is sensitive | [Membership inference](membership-inference.md) | A model or synthetic dataset may leak inclusion even without exposing full records. |

## Practical Output

A useful threat model should leave a reviewer with a table like this:

| Asset | Adversary | Observations | Allowed output | Out of scope |
| --- | --- | --- | --- | --- |
| Site-level model updates | Curious coordinator | Aggregate update, round metadata, final model | Global model and public metrics | Malicious local training code unless robust aggregation is added |
