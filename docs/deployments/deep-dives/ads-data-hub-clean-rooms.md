# Google Ads Data Hub and Data Clean Rooms

!!! warning "Read the evidence levels"
    "Clean room" is a product and governance pattern, not a single cryptographic guarantee. This page separates what the platform enforces from what marketing language implies. Reference date: 2026-06-10.

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | Google Ads Data Hub (ADH); the broader data clean room pattern (Google BigQuery data clean rooms, and comparable offerings from other vendors) |
| Domain | Advertising and marketing measurement |
| Problem | Let an advertiser join its first-party data with a platform's event-level ad logs for measurement and analytics, without either party exposing raw user-level records to the other |
| PETs used | Output-side **aggregation thresholds**, **difference checks**, optional **noise injection**, plus **query restrictions** (allowed-SQL controls). A clean room is primarily an access-control and output-control pattern, not strong cryptographic input privacy |
| Deployment maturity | Commercial production, widely used |
| Source quality | Primary / official vendor documentation |
| Source | [Ads Data Hub methodology](https://developers.google.com/ads-data-hub/resources/description-of-methodology); [Privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks) |

## What Was Actually Deployed

Ads Data Hub lets an advertiser run SQL queries that join their own customer data with Google's event-level ad data inside Google's BigQuery-backed environment. The advertiser never receives the raw event-level rows; they receive only query *outputs* that pass a set of privacy checks. The general "data clean room" pattern is the same shape: two or more parties bring data into a governed environment where only approved, aggregated outputs leave. *(Deployment-backed — [ADH introduction](https://developers.google.com/ads-data-hub/guides/intro); [BigQuery data clean rooms](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms).)*

The privacy enforcement is on the **output**, via several layered mechanisms:

- **Aggregation thresholds.** Results generally must aggregate a minimum number of users before they can be returned. Google's documentation describes a baseline requirement on the order of **50 users** for most queries, with **click and conversion** queries able to report on as few as **~10**. *(Deployment-backed — [Privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).)*
- **Difference checks.** ADH compares the results of successive/related queries to block attempts to isolate an individual by differencing two nearly identical aggregates. *(Deployment-backed — [Privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).)*
- **Noise injection (optional).** Random noise can be added to aggregation results, which in turn permits lower user thresholds (documented on the order of ~20 for impressions and ~10 for clicks/conversions when noise is applied). *(Deployment-backed — [Noise injection](https://developers.google.com/ads-data-hub/marketers/guides/noise-injection).)*
- **Restricted SQL surface.** Only an allow-listed set of SQL functions is permitted, and the system blocks queries that look like re-identification attempts. Rate limits also apply (documented as ~10 concurrent queries and ~10 queries per minute per advertiser). *(Deployment-backed — [Allowed functions](https://developers.google.com/ads-data-hub/marketers/reference/allowed-functions); [Policies](https://developers.google.com/ads-data-hub/resources/policies).)*

## Maturity

**Commercial production, at very large scale.** Ads Data Hub is a live, supported Google product used by advertisers and measurement vendors, and BigQuery data clean rooms are a generally available capability. This is the most "productionized" entry in this deep-dive set. The maturity caveat is different here: the system is mature precisely because it is a vendor-operated walled garden, which shapes both its strengths and its trust assumptions. *(Deployment-backed — Google product documentation.)*

## Privacy Claim

The honest framing of the claim is: **the consuming party cannot retrieve raw user-level rows, and outputs are constrained so that small-cohort results that could single out an individual are blocked, noised, or refused.** It is an *output-disclosure-control* model layered on *access control* — you query inside the owner's environment and only aggregated results come out. *(Deployment-backed — [methodology](https://developers.google.com/ads-data-hub/resources/description-of-methodology) and [privacy checks](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).)*

What it is generally **not** claimed to be: a formal differential privacy system with a published, end-to-end privacy-loss budget across all queries. Thresholds, difference checks, and optional noise are heuristic and policy-driven disclosure controls, not a single composed DP guarantee. *(Expert judgment, based on the absence of a published global epsilon in the [official methodology](https://developers.google.com/ads-data-hub/resources/description-of-methodology).)*

## Limitations

- **The platform owner is fully trusted and sees everything.** The clean room protects the parties *from each other*, not from the operator. Google (or any clean-room host) has access to the underlying data and the infrastructure. If your threat model includes the operator, a clean room does not address it. *(Expert judgment, inherent to the architecture.)*
- **Threshold-and-difference controls are not a formal privacy guarantee.** Minimum-aggregation rules plus difference checks reduce trivial singling-out, but they are not equivalent to differential privacy; sophisticated multi-query reconstruction risk is mitigated operationally rather than provably bounded. *(Expert judgment / literature-backed in the general clean-room critique literature.)*
- **Noise is optional and is a utility tradeoff.** Lower thresholds are unlocked by adding noise, so practitioners face the familiar accuracy-versus-disclosure tension; turning noise off raises thresholds. *(Deployment-backed — [Noise injection](https://developers.google.com/ads-data-hub/marketers/guides/noise-injection).)*
- **"Clean room" is a marketing umbrella.** Different vendors mean different things by the term, ranging from "encrypted match plus aggregate" to "trusted-execution-backed compute" to "just a governed SQL sandbox." The label alone tells you almost nothing about the actual guarantee. *(Expert judgment.)*

## Builder Lessons

- **Name the operator in your threat model first.** A clean room's core assumption is a trusted host. Decide explicitly whether that is acceptable before adopting one; if not, you need MPC, TEEs, or HE, not a clean room.
- **Treat thresholds and difference checks as disclosure controls, not proofs.** They are sensible engineering, but do not represent them to stakeholders as differential privacy unless a formal budget is actually published and composed.
- **Design queries for the privacy checks, not against them.** Vendor best-practice guidance (develop against sandbox/test data, minimize layered cross-user aggregations) exists because queries routinely fail privacy checks; budget engineering time for it. *(Deployment-backed — [Best practices](https://developers.google.com/ads-data-hub/guides/best-practices).)*
- **Watch for lock-in.** The convenience comes from operating inside the data owner's environment. That same property concentrates control and portability with the host.

## What Remains Unclear

- **Exact, current thresholds and noise parameters can change** and are version-dependent; the figures above (~50 users baseline, ~10 for clicks/conversions, ~20/~10 with noise) reflect Google's documentation as reviewed and should be re-checked against the live docs. *(Deployment-backed at time of review; treat specific numbers as Needs evidence going forward.)*
- **The precise noise mechanism and whether it composes to any formal guarantee** are not fully specified in the public marketer docs; absent a published epsilon, assume it does not provide a composed DP guarantee. *(Needs evidence.)*
- **Independent third-party evaluations of re-identification resistance** for production clean rooms are scarce relative to vendor self-description. *(Needs evidence.)*

## Sources

- Google for Developers, [Ads Data Hub: Description of methodology](https://developers.google.com/ads-data-hub/resources/description-of-methodology).
- Google for Developers, [Ads Data Hub: Introduction](https://developers.google.com/ads-data-hub/guides/intro).
- Google for Developers, [Privacy checks in Ads Data Hub](https://developers.google.com/ads-data-hub/marketers/guides/privacy-checks).
- Google for Developers, [Noise injection](https://developers.google.com/ads-data-hub/marketers/guides/noise-injection).
- Google for Developers, [Allowed SQL functions](https://developers.google.com/ads-data-hub/marketers/reference/allowed-functions) and [Ads Data Hub Policies](https://developers.google.com/ads-data-hub/resources/policies).
- Google Cloud, [Share sensitive data with data clean rooms (BigQuery)](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms).
