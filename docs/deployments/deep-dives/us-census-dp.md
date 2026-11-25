# US Census Bureau 2020 Differential Privacy

!!! warning "Read the evidence levels"
    This case documents differential privacy in production for 2020 Decennial Census products.

## Policy update

!!! info "Policy update checked 2026-11-25"
    The Department of Commerce issued DAO 216-26 on June 4, 2026. The Census Bureau states that future statistical products will no longer use noise infusion under this policy. Bureau guidance prefers coarsening, with suppression allowed where necessary. That changes what teams can plan for future releases. The 2020 products remain historical evidence of production DP. See [Census Bureau notice on noise infusion](https://www.census.gov/programs-surveys/susb/about/glossary.operations.html) and [Census Bureau guidance on statistical safeguards](https://www.census.gov/about/policies/privacy/statistical_safeguards.html).

*(Evidence: Deployment-backed. Source quality: Primary / official. The cited notices establish Bureau policy, not what every future product design will be.)*

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | U.S. Census Bureau, 2020 Decennial Census Disclosure Avoidance System (DAS) |
| Domain | Public sector / official statistics |
| Problem | Publish detailed population tables down to the census-block level while provably limiting what any attacker can reconstruct about individual respondents |
| PETs used | Differential privacy via the TopDown Algorithm (TDA), using zero-concentrated differential privacy (zCDP) for privacy-loss accounting |
| Deployment maturity | Historical production across multiple 2020 Census data products. Future releases follow current policy. |
| Source quality | Primary / official plus independent analysis |
| Source | [Census Bureau working paper: The 2020 Census DAS TopDown Algorithm](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html) |

## What Was Actually Deployed

The Census Bureau replaced its long-standing disclosure-avoidance methods (swapping and suppression) with a formal differential privacy system for the 2020 Decennial Census. The core engine is the **TopDown Algorithm (TDA)**: it ingests the edited confidential census data, generates noisy versions of key queries ("measurements") using zero-concentrated differential privacy, then runs a post-processing optimization that distributes counts top-down through the geographic hierarchy (nation to state to county and on down to block) so that the released tables are internally consistent and non-negative. *(Deployment-backed — [Census working paper CED-WP-2022-002](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html).)*

Scale and timeframe:

- **Geographic reach:** the entire United States, down to the census block, the finest published geography. *(Deployment-backed.)*
- **First production output:** the P.L. 94-171 redistricting data files were released in **August 2021** using the TDA. *(Deployment-backed — Census release schedule and [TDA working paper](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html).)*
- **Privacy-loss budget for redistricting data:** the Bureau set a total of **epsilon = 17.14 for persons and epsilon = 2.47 for housing units** (the Bureau's published epsilon values for this product). *(Evidence: Deployment-backed. Source quality: Primary / official. See the [2021 production settings announcement](https://www.census.gov/newsroom/press-releases/2021/2020-census-key-parameters.html). These values do not describe later products or demonstration data.)*

A defining design choice is the use of **invariants**: certain statistics the Bureau decided, as a matter of policy, to release exactly with no noise. For redistricting data, these included state population totals, block-level housing unit counts, and block-level counts of group-quarters facilities for specified types. Block population and the number of people in group quarters were not invariants. *(Evidence: Deployment-backed. Source quality: Primary / official. See the [Bureau’s disclosure avoidance FAQ](https://www.census.gov/programs-surveys/decennial-census/decade/2020/planning-management/process/disclosure-avoidance/2020-das-updates/2020-das-faqs.html).)*

## Maturity

**Production, batch / periodic.** Treat the files as separate releases. The [2021 redistricting files](https://www.census.gov/newsroom/press-releases/2021/2020-census-key-parameters.html) and the [2023 Demographic and Housing Characteristics File](https://www.census.gov/data/tables/2023/dec/2020-census-dhc.html) describe different products. Earlier [demonstration files](https://www.census.gov/newsroom/press-releases/2021/census-bureau-releases-latest-privacy-protection-demonstration-data.html) used 2010 Census data to illustrate the method. Check which release an evaluation used before carrying its accuracy findings forward.

## Privacy Claim

The claimed property is **differential privacy with a published, accountable privacy-loss budget**. Concretely, the Bureau accounts for privacy loss using zero-concentrated differential privacy and publishes the total budget and its allocation across geographic levels and query types. The motivating threat is the **database reconstruction theorem**: the Bureau's own internal experiments indicated that the volume of exact tabulations historically published could be combined to reconstruct and re-identify a meaningful share of individual records, which is what formal DP is meant to bound. *(Deployment-backed for the mechanism; the reconstruction motivation is documented by the Bureau and discussed in [the academic literature](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/).)*

Two honest caveats on the claim itself:

- The guarantee applies to the **noised** statistics. Invariant quantities (for example, state total population) are released exactly and are explicitly **outside** the privacy-loss accounting. *(Deployment-backed.)*
- A single epsilon number is not directly comparable to epsilon values from other systems, because the per-query allocation, the unit of privacy, and the use of invariants all change what the number means. *(Expert judgment.)*

## Limitations

What DP did **not** do, and the criticisms it drew:

- **It did not protect invariants.** State totals and several housing/group-quarters counts are exact by design, so no privacy is claimed for them. *(Deployment-backed.)*
- **Error varies by geography and subgroup.** [Kenny et al. (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/) studied the April 2021 DAS 12.2 demonstration on 2010 Census data. The earlier Harvard evaluation is a related version of the same research. A [separate rural and subgroup study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11105149/) used the final demonstration on 2010 Census data, which applied the production redistricting epsilon settings. Neither analyzed the actual 2020 production counts. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic.)*
- **Post-processing can introduce bias.** Kenny et al. found systematic discrepancies by geography and demographic group under the April demonstration settings. Check the post-processing rules and product version before carrying those results forward. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. [Kenny et al. (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/).)*
- **Redistricting and voting rights.** Kenny et al. examined how the April demonstration data affected analyses of majority-minority districts and partisan bias in simulated plans. The results describe those simulations. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. [Kenny et al. (2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/).)*
- **Litigation.** The State of Alabama challenged the disclosure avoidance method and the timing of the redistricting release in [Alabama v. U.S. Department of Commerce, No. 3:21-cv-00211](https://storage.courtlistener.com/recap/gov.uscourts.almd.75040/gov.uscourts.almd.75040.27.0.pdf). The cited filing documents the dispute. *(Evidence: Deployment-backed. Source quality: Primary / official.)*

## Builder Lessons

- **Plan for policy change.** A method that shipped can later become unavailable under a new mandate. Record the authority for the method, the date checked, and a fallback before the next release cycle. *(Evidence: Expert judgment, informed by the Bureau policy update above.)*
- **Formal privacy forces an explicit, public utility tradeoff.** The Census fight is what honest DP looks like at scale: you must publish the budget, and stakeholders can then argue about it. That transparency is a feature, but be ready for the argument.
- **Invariants are a pragmatic escape hatch with a cost.** Releasing some quantities exactly preserved critical legal correctness, but every invariant is a hole in the guarantee and can leak information that interacts with the noised release. Name your invariants explicitly.
- **Post-processing is part of your privacy and utility story.** Non-negativity and consistency constraints change the error distribution. Do not treat post-processing as a cosmetic final step; analyze its bias.
- **Small cells are where DP hurts most.** If your use case depends on accurate counts for tiny populations, budget, parameterize, and communicate for that case specifically, or reconsider whether the data should be published at that granularity at all.
- **A single epsilon is not a portable quality score.** Document the unit of privacy, the allocation, and the invariants. An epsilon without that context is close to meaningless for comparison.

## What Remains Unclear

- **The product-specific design for 2030 remains open in this case study.** Check the policy in force and the Bureau’s product documentation before assuming any statistical method will carry over. *(Needs evidence.)*
- **The "right" epsilon was, and remains, a policy judgment, not a derived constant.** There is no consensus figure; the 17.14 / 2.47 split reflects the Bureau's negotiated balance, not an objective optimum. *(Expert judgment.)*
- **Effects on actual districting and funding decisions** remain unverified by the evaluations cited here. *(Needs evidence.)*

## Sources

- U.S. Census Bureau, [The 2020 Census Disclosure Avoidance System TopDown Algorithm](https://www.census.gov/library/working-papers/2022/adrm/CED-WP-2022-002.html) (working paper, 2022).
- Kenny et al., [The use of differential privacy for census data and its impact on redistricting](https://pmc.ncbi.nlm.nih.gov/articles/PMC8494446/), PNAS, 2021 (April DAS 12.2 demonstration on 2010 data).
- [The 2020 US Census Differential Privacy Method Introduces Disproportionate Discrepancies](https://pmc.ncbi.nlm.nih.gov/articles/PMC11105149/) (final demonstration on 2010 data with the production redistricting epsilon settings).
- [Alabama v. U.S. Dept. of Commerce, M.D. Ala., No. 3:21-cv-00211, court filing](https://storage.courtlistener.com/recap/gov.uscourts.almd.75040/gov.uscourts.almd.75040.27.0.pdf).
