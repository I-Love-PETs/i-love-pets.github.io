# Google Ads Data Hub and Data Clean Rooms

!!! warning "Read the evidence levels"
    This page describes Google’s documented controls. Privacy mode and control descriptions checked on 2026-11-25.

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | Google Ads Data Hub (ADH); the broader data clean room pattern (Google BigQuery data clean rooms, and comparable offerings from other vendors) |
| Domain | Advertising and marketing measurement |
| Problem | Let an advertiser join its first-party data with a platform's event-level ad logs for measurement and analytics, without either party exposing raw user-level records to the other |
| PETs used | Static query checks, data access budgets, aggregation checks, and a choice of noise injection or legacy difference checks. |
| Deployment maturity | Commercial production, widely used |
| Source quality | Primary / official vendor documentation |
| Source | [Ads Data Hub methodology](https://developers.google.com/ads-data-hub/resources/description-of-methodology); [Privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks) |

## What Was Actually Deployed

Ads Data Hub lets an advertiser run SQL queries that join their own customer data with Google's event-level ad data inside Google's BigQuery-backed environment. The advertiser never receives the raw event-level rows; they receive only query *outputs* that pass a set of privacy checks. The general "data clean room" pattern is the same shape: two or more parties bring data into a governed environment where only approved, aggregated outputs leave. *(Deployment-backed — [ADH introduction](https://developers.google.com/ads-data-hub/guides/intro); [BigQuery data clean rooms](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms).)*

Ads Data Hub applies two sets of controls. [Static checks and data access budgets](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks) screen SQL and limit repeated access to underlying data. Aggregation thresholds apply to results and vary by mode and input data.

- **Aggregation thresholds.** Google documents approximately 20 unique users per row in noise mode, 50 in difference-check mode, and 10 for click- and conversion-only queries. Check the current requirements for your query. *(Evidence: Deployment-backed. Source quality: Primary / official. [Privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).)*
- **Legacy difference-check mode.** The service compares results with past query results to limit disclosure from combining them. Rows may be removed when a check fails. *(Evidence: Deployment-backed. Source quality: Primary / official. [Difference checks](https://developers.google.com/ads-data-hub/marketers/guides/legacy-diff-checks).)*
- **Noise mode (the documented default).** Google adds calibrated noise to aggregates and uses implicit or explicit clamping to bound user contributions. Noise mode does not rely on difference checks. Google states that its MRC accreditation does not extend to queries in noise mode. *(Evidence: Deployment-backed. Source quality: Primary / official. [Noise injection](https://developers.google.com/ads-data-hub/marketers/guides/noise-injection).)*
- **Restricted SQL surface.** Both modes retain static SQL checks and data access limits. Use sandbox data to iterate on queries without drawing conclusions about production disclosure from that testing. *(Evidence: Deployment-backed. Source quality: Primary / official. [Privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).)*

## Maturity

**Commercial production, at very large scale.** Ads Data Hub is a live, supported Google product used by advertisers and measurement vendors, and BigQuery data clean rooms are a generally available capability. This is the most "productionized" entry in this deep-dive set. The maturity caveat is different here: the system is mature precisely because it is a vendor-operated walled garden, which shapes both its strengths and its trust assumptions. *(Deployment-backed — Google product documentation.)*

## Privacy Claim

The honest framing of the claim is: **the consuming party cannot retrieve raw user-level rows, and outputs are constrained so that small-cohort results that could single out an individual are blocked, noised, or refused.** It is an *output-disclosure-control* model layered on *access control* — you query inside the owner's environment and only aggregated results come out. *(Deployment-backed — [methodology](https://developers.google.com/ads-data-hub/resources/description-of-methodology) and [privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).)*

The public docs describe controls and API behavior. They do not establish a composed privacy-loss budget for the full sequence of queries an advertiser runs. An `ANON_*` aggregation or a data access budget is insufficient evidence of that guarantee. *(Evidence: Expert judgment, based on the scope of the [documented mechanics](https://developers.google.com/ads-data-hub/marketers/guides/noise-injection).)*

## Limitations

- **The platform owner is fully trusted and sees everything.** The clean room protects the parties *from each other*, not from the operator. Google (or any clean-room host) has access to the underlying data and the infrastructure. If your threat model includes the operator, a clean room does not address it. *(Expert judgment, inherent to the architecture.)*
- **Threshold-and-difference controls are not a formal privacy guarantee.** Minimum-aggregation rules plus difference checks reduce trivial singling-out, but they are not equivalent to differential privacy; sophisticated multi-query reconstruction risk is mitigated operationally rather than provably bounded. *(Expert judgment / literature-backed in the general clean-room critique literature.)*
- **Mode affects what you can measure.** Expect noise and contribution clamping in noise mode, and possible redaction in difference-check mode. Measure the effect of each behavior on the decision the output supports. *(Evidence: Expert judgment, informed by the [privacy checks documentation](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).)*
- **"Clean room" is a marketing umbrella.** Different vendors mean different things by the term, ranging from "encrypted match plus aggregate" to "trusted-execution-backed compute" to "just a governed SQL sandbox." The label alone tells you almost nothing about the actual guarantee. *(Expert judgment.)*

## Builder Lessons

- **Name the operator in your threat model first.** A clean room's core assumption is a trusted host. Decide explicitly whether that is acceptable before adopting one; if not, you need MPC, TEEs, or HE, not a clean room.
- **Treat thresholds and difference checks as disclosure controls, not proofs.** They are sensible engineering, but do not represent them to stakeholders as differential privacy unless a formal budget is actually published and composed.
- **Design queries for the privacy checks, not against them.** Vendor best-practice guidance (develop against sandbox/test data, minimize layered cross-user aggregations) exists because queries routinely fail privacy checks; budget engineering time for it. *(Deployment-backed — [Best practices](https://developers.google.com/ads-data-hub/guides/best-practices).)*
- **Watch for lock-in.** The convenience comes from operating inside the data owner's environment. That same property concentrates control and portability with the host.

## What Remains Unclear

- **Exact thresholds and noise behavior** depend on the mode and query. Confirm the current [thresholds and controls](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks) and measure utility with the approved configuration.
- **A composed privacy guarantee for the intended set of queries** is not established by the cited product documentation. *(Needs evidence.)*
- **Independent third-party evaluations of re-identification resistance** for production clean rooms are scarce relative to vendor self-description. *(Needs evidence.)*

## Sources

- Google for Developers, [Ads Data Hub: Description of methodology](https://developers.google.com/ads-data-hub/resources/description-of-methodology).
- Google for Developers, [Ads Data Hub: Introduction](https://developers.google.com/ads-data-hub/guides/intro).
- Google for Developers, [Privacy checks in Ads Data Hub](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).
- Google for Developers, [Noise injection](https://developers.google.com/ads-data-hub/marketers/guides/noise-injection).
- Google for Developers, [Allowed SQL functions](https://developers.google.com/ads-data-hub/marketers/reference/allowed-functions) and [Ads Data Hub Policies](https://developers.google.com/ads-data-hub/resources/policies).
- Google Cloud, [Share sensitive data with data clean rooms (BigQuery)](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms).
