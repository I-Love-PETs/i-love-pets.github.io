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

### Chrome Privacy Sandbox Attribution Reporting

| Field | Entry |
| --- | --- |
| Organization / project | Chrome Privacy Sandbox Attribution Reporting API |
| Domain | Advertising |
| Problem | Enable conversion measurement without third-party cookies. |
| PETs used | Browser-mediated attribution, event-level and aggregate reports, noise for summary reports |
| Deployment maturity | Production / evolving platform feature |
| Source quality | Primary / official vendor documentation plus platform documentation |
| What worked | The API is documented for web developers and supports attribution flows with privacy controls. |
| Challenges | Adoption, debugging, noise, reporting limits, and ecosystem readiness remain major issues. |
| Lessons for builders | Platform PETs must be evaluated as product migrations: developer ergonomics and business utility can dominate cryptographic elegance. |
| Source | [Privacy Sandbox Attribution Reporting overview](https://privacysandbox.google.com/private-advertising/attribution-reporting/web) and [MDN Attribution Reporting API](https://developer.mozilla.org/en-US/docs/Web/API/Attribution_Reporting_API) |

*(Evidence: Deployment-backed. Source quality: Primary / official vendor documentation plus MDN platform documentation. Reviewed 2026-06-17 — browser support and ecosystem behavior are fast-moving; re-check before migration.)*

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
