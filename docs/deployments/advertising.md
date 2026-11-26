---
title: "Advertising Deployments"
---

# Advertising Deployments

!!! warning "Deployment evidence"
    Advertising PET deployments are often platform-controlled. They may be production systems, but the privacy and utility evidence can still be difficult for outsiders to inspect.

## Production Platform Deployments

### Google Ads Data Hub

| Field | Entry |
| --- | --- |
| Organization / project | Google Ads Data Hub |
| Domain | Advertising |
| Problem | Let advertisers run customized analysis on Google advertising data while enforcing privacy checks on query outputs. |
| PETs used | Data clean room, privacy checks, controlled query environment |
| Deployment maturity | Production |
| Source quality | Primary / official vendor documentation |
| What worked | Ads Data Hub is a documented Google product with UI/API workflows and privacy checks on query results. |
| Challenges | It is platform-governed; users must learn the operating model, and privacy depends on query rules, access, and output checks. |
| Lessons for builders | Clean rooms are as much governance and workflow as technology. Query approval, thresholds, and output review are core product features, not add-ons. |
| Source | [Google Ads Data Hub documentation](https://developers.google.com/ads-data-hub) and [Ads Data Hub introduction](https://developers.google.com/ads-data-hub/guides/intro) |

*(Evidence: Deployment-backed. Source quality: Primary / official vendor documentation. Reviewed 2026-06-17 — strong evidence the product and controls exist; weaker evidence for independent privacy or utility outcomes.)*

### Apple SKAdNetwork / AdAttributionKit

| Field | Entry |
| --- | --- |
| Organization / project | Apple SKAdNetwork and AdAttributionKit |
| Domain | Advertising |
| Problem | Measure app-install and post-install campaign performance without exposing user-level identifiers in the same way as traditional attribution. |
| PETs used | Privacy-preserving attribution framework, aggregation/delay/thresholding concepts |
| Deployment maturity | Production |
| Source quality | Primary / official vendor documentation |
| What worked | SKAdNetwork is part of Apple's developer ecosystem and is used for iOS app attribution workflows. |
| Challenges | Measurement is less granular; conversion-value design, delays, thresholds, and interoperability create operational pain for advertisers. |
| Lessons for builders | Privacy-preserving attribution changes the optimization workflow, not only the data transport. Expect utility loss and new measurement practices. |
| Source | [Apple Developer: SKAdNetwork](https://developer.apple.com/documentation/storekit/skadnetwork?post_type=advertisers&who=support) and [Apple Ads attribution overview](https://ads.apple.com/app-store/help/attribution/0094-ad-attribution-overview) |

*(Evidence: Deployment-backed. Source quality: Primary / official vendor documentation. Reviewed 2026-06-17 — production framework evidence is strong; exact measurement utility depends on campaign setup and current Apple platform behavior.)*

## Historical Platform Deployments

### Chrome Privacy Sandbox Attribution Reporting

| Field | Entry |
| --- | --- |
| Organization / project | Chrome Privacy Sandbox Attribution Reporting API |
| Domain | Advertising |
| Problem | Enable conversion measurement without third-party cookies. |
| PETs used | Browser-mediated attribution, event-level and aggregate reports, noise for summary reports |
| Deployment maturity | Historical production feature. Google announced retirement on 2025-10-17. |
| Source quality | Primary / official |
| What worked | Chrome shipped browser-mediated conversion reporting with privacy controls. The documentation remains useful as a record of the design. |
| Challenges | Google cited limited adoption and ecosystem feedback when announcing retirement. Google’s current feature status lists Chrome Attribution Reporting as deprecated and removed. Check the status page for platform-specific details. |
| Lessons for builders | Platform PETs must be evaluated as product migrations: developer ergonomics and business utility can dominate cryptographic elegance. |
| Source | [Google retirement announcement](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies) and [Privacy Sandbox feature status](https://privacysandbox.google.com/overview/status) |

*(Evidence: Deployment-backed. Source quality: Primary / official. Status checked 2026-11-25. The October 2025 announcement records the retirement decision. The feature status page tracks browser removal separately.)*

## Common Proposed Use Cases

| Use case | Candidate PETs | Why proposed | Caveats |
| --- | --- | --- | --- |
| Cross-platform campaign measurement | Clean rooms, attribution APIs, private aggregation | Advertisers need measurement after cookie and identifier loss | Noisy or thresholded outputs can hurt optimization |
| Audience overlap | PSI, clean rooms | Brands and platforms need match counts without exposing full lists | Match sets and repeated queries can leak |
| Incrementality testing | Clean rooms, DP, MPC | Parties need controlled experiment results | Experimental design can fail even if privacy controls work |
| Retail media collaboration | Clean rooms, DP, query governance | Retailers and brands need joint analytics | Platform incentives and output policy matter |

## Lessons Learned

- Advertising PETs often trade user-level observability for aggregate measurement.
- Clean rooms do not automatically solve consent, purpose limitation, or platform power.
- Delays, noise, and thresholds are product constraints, not minor implementation details.
- Interoperability across platforms remains a practical barrier.
