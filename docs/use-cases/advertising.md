# Advertising

Advertising PET decisions usually involve measurement under identifier loss, platform governance, small-segment leakage, and incentives that are not always aligned.

## Scenario Playbook

| Scenario | Primary PET | Supporting PETs | Why | What can go wrong | What to measure |
| --- | --- | --- | --- | --- | --- |
| Advertiser measures campaign performance in a platform | Clean room | DP thresholds, query review, audit logs | Platform can enforce controlled queries and output rules | Platform sees too much, segments are tiny, query rules are gamed | Minimum cohort size, query history, measurement lift |
| Two parties estimate audience overlap | PSI | Clean-room controls, DP counts | Nonmatching users need not be revealed | Repeated matching learns user lists | Match precision, repeat-query limits, output granularity |
| Attribution without user-level tracking | Attribution API / private aggregation | DP-style noise, delay, thresholds | Measurement survives without raw user-level identifiers | Utility drops, debugging becomes hard, incentives shift | Attribution error, delay, conversion-value loss |
| Retail media collaboration | Clean room or federated analytics | DP, purpose controls | Retailers and brands need joint measurement | Output policy follows platform incentives, not user expectations | Segment sizes, allowed use, advertiser workflow fit |

## Use This When

- The output is aggregate measurement, attribution, or overlap.
- Small segments can be thresholded, grouped, or noised.
- Query history and repeated joins are controlled.
- Platform governance is explicit and reviewable.

## Avoid This When

- The proposal recreates user-level tracking through repeated queries.
- "Clean room" is used as a brand label without technical output controls.
- The audience segment is too small to protect.
- Consent, purpose limitation, or platform power is the real issue.

## Recommended Starting Stack

For platform measurement, start with a **clean room + output thresholds**. For list overlap, start with **PSI + strict output limits**. Add DP or private aggregation when repeated aggregate releases need stronger protection.

## Failure Modes

- Small segments reveal sensitive behavior.
- Identity normalization leaks more than the analysis requires.
- Repeated queries reconstruct user-level signals.
- Noise and delay make optimization unstable.
- Platform rules are opaque to advertisers or users.

## Evaluation Checklist

- What is the smallest segment that can be queried or reported?
- Can users or devices be tracked across repeated analyses?
- Is the platform operator inside the trust model?
- What measurement utility is lost from noise, delay, or thresholds?
- Are allowed uses and retention limits enforced?

## Related Pages

- [Federated analytics](../pet-patterns/federated-analytics.md)
- [Private set intersection](../pet-patterns/private-set-intersection.md)
- [Advertising deployments](../deployments/advertising.md)
