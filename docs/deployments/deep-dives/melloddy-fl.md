# MELLODDY Cross-Pharma Federated Learning

!!! warning "Read the evidence levels"
    MELLODDY is the largest cross-pharma federated learning experiment to date and is unusually honest about what federated learning alone does and does not protect. Reference date: 2026-06-10.

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | MELLODDY (MachinE Learning Ledger Orchestration for Drug DiscoverY) consortium |
| Domain | Life sciences / pharmaceutical drug discovery |
| Problem | Let competing pharma companies jointly improve molecular-activity (QSAR-style) predictive models using their highly proprietary chemical and bioactivity data, without pooling or revealing that data |
| PETs used | Federated learning, orchestrated via the Substra framework (distributed-ledger-based task orchestration), plus secure aggregation of model updates |
| Deployment maturity | Completed consortium project (three-year IMI-funded effort, concluded 2022) |
| Source quality | Primary / official plus peer-reviewed / academic |
| Source | [MELLODDY Year 3 announcement](https://www.melloddy.eu/y3announcement); [JCIM 2023 paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11005050/) |

## What Was Actually Deployed

Ten pharmaceutical companies, together with technology and academic partners, trained a shared multi-task machine learning model across their separate datasets without moving raw data out of each company's control. The platform used the **Substra** framework to orchestrate federated training and record the workflow on a distributed ledger, and applied **secure aggregation** so the central orchestrator could combine model updates without reading any single company's individual gradients. *(Deployment-backed — [MELLODDY Year 3 announcement](https://www.melloddy.eu/y3announcement); [Privacy @ MELLODDY](https://www.melloddy.eu/blog/protected-privacy-melloddy).)*

Parties, scale, timeframe:

- **Participants:** **10 pharmaceutical companies** plus seven technology and academic partners; the project was led by Owkin. *(Deployment-backed — [MELLODDY Year 3 announcement](https://www.melloddy.eu/y3announcement).)*
- **Data scale:** the consortium reported training across **over 2.6 billion** confidential activity data points, described as the world's largest collection of small molecules with known biochemical or cellular activity. *(Deployment-backed — [Year 3 announcement](https://www.melloddy.eu/y3announcement); [tech.eu coverage](https://tech.eu/2022/07/13/eu-backed-healthcare-project-rolls-out-platform-for-federated-learning-in-drug-discovery/).)*
- **Timeframe and funding:** a three-year project under the EU Innovative Medicines Initiative (IMI), running roughly 2019–2022 and concluding in **July 2022**. *(Deployment-backed — [CORDIS project record](https://cordis.europa.eu/project/id/831472/results); [Medical Valley press release](https://www.medical-valley-emn.de/en/press-release-melloddy-project-has-successfully-demonstrated-that-collaborating-in-ai-for-drug-discovery-is-possible-at-industrial-scale/).)*

Reported results:

- The collaborative ("federated") model was, on average, about **4% more accurate** at classifying molecular activity than each company's standalone model, and expanded the model's applicability domain by about **10%**. *(Deployment-backed for the reported figures — [Year 3 announcement](https://www.melloddy.eu/y3announcement); peer-reviewed details in [JCIM 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC11005050/). Treat the exact percentages as consortium-reported.)*

## Maturity

**A completed, large-scale consortium experiment — not a standing production service.** MELLODDY decisively proved feasibility at industrial scale and produced peer-reviewed results, but it was a time-boxed, grant-funded project that concluded in 2022. It is best read as the strongest available *feasibility demonstration* for cross-silo, cross-competitor FL, not as evidence of an ongoing operational platform. Follow-on productization by individual partners or vendors is a separate question. *(Deployment-backed for "completed consortium"; ongoing-production status is Needs evidence.)*

## Privacy Claim

The claimed property is **collaborative model improvement without sharing raw proprietary data**, with secure aggregation hiding any individual company's model updates from the orchestrator. The consortium's own privacy write-up describes the secure-aggregation guarantee as **k-anonymity-like**: it makes attributing a given contribution to a specific partner difficult, rather than providing a formal differential-privacy bound. *(Deployment-backed — [Privacy @ MELLODDY](https://www.melloddy.eu/blog/protected-privacy-melloddy); [Substra privacy strategy](https://docs.substra.org/en/0.32.0/additional/privacy-strategy.html).)*

Crucially, the protected artifacts are **raw datasets and individual model updates**. The shared model and the aggregate gradients are still computed and exchanged.

## Limitations

What FL plus secure aggregation did **not** fully protect, stated candidly by the project and independent analysts:

- **Federated learning alone is not a privacy guarantee.** Model updates and the trained model can leak information about training data; secure aggregation hides *individual* contributions but does not eliminate gradient- and model-level leakage. The MELLODDY privacy team explicitly acknowledges ongoing gradient/model leakage as a residual concern. *(Deployment-backed / literature-backed — [Privacy @ MELLODDY](https://www.melloddy.eu/blog/protected-privacy-melloddy).)*
- **Differential privacy was considered but found impractical here.** The team reports that adding DP, while effective in theory against membership inference, caused unacceptable accuracy loss for drug-discovery models, so a formal DP bound was not adopted. The result is feasibility and utility, but without a composed DP guarantee. *(Deployment-backed — [Privacy @ MELLODDY](https://www.melloddy.eu/blog/protected-privacy-melloddy).)*
- **Secure aggregation's guarantee is informal.** A "k-anonymity-like" property is weaker and less composable than differential privacy, and depends on assumptions about non-collusion among parties. *(Literature-backed — independent analysis by CrySyS Lab, [Collaborative Drug Discovery: Inference-level Data Protection Perspective, arXiv 2205.06506](https://ar5iv.labs.arxiv.org/html/2205.06506).)*
- **Feasibility is not generality.** A 4% average accuracy gain on QSAR-style tasks across these specific partners does not prove FL helps every discovery task, nor that it protects every category of proprietary information. *(Expert judgment, consistent with the project's own framing.)*

## Builder Lessons

- **Separate "we did not share raw data" from "the data is private."** MELLODDY's honesty is the lesson: FL keeps raw data home and secure aggregation hides individual updates, but neither bounds what the shared model leaks. Name the residual leakage explicitly.
- **DP is not free, and sometimes not viable.** When accuracy is the entire point (predictive drug models), a formal DP budget may degrade utility past usefulness. Decide early whether you need a provable bound or an informal one, and design the threat model accordingly.
- **Cross-competitor FL is as much governance as engineering.** A distributed ledger (Substra) was used partly to make the *process* auditable and trustworthy among rivals, mirroring the Boston MPC lesson that trust and orchestration dominate raw crypto performance.
- **Shared task definitions and data harmonization come first.** Cross-silo FL across companies needs agreed task definitions and an agreement about what model improvements may reveal, before any training runs.

## What Remains Unclear

- **Whether the platform is in ongoing production** at any partner after the 2022 conclusion is not established by the sources reviewed. *(Needs evidence.)*
- **The exact secure-aggregation threat model and collusion assumptions** (how many colluding parties break the k-anonymity-like property) are not fully pinned down in the public consortium materials; the independent CrySyS analysis raises but does not exhaustively resolve this. *(Needs evidence / partially literature-backed via [arXiv 2205.06506](https://ar5iv.labs.arxiv.org/html/2205.06506).)*
- **Generalizability of the ~4% / ~10% gains** beyond MELLODDY's partners and task set is unverified; these are consortium-reported aggregate figures. *(Needs evidence for generalization; Deployment-backed only as reported.)*

## Sources

- MELLODDY, [Year 3 Announcement: Largest-ever pharma industry AI collaboration utilizing a federated model](https://www.melloddy.eu/y3announcement).
- Heyndrickx et al., [MELLODDY: Cross-pharma Federated Learning at Unprecedented Scale Unlocks Benefits in QSAR without Compromising Proprietary Information](https://pmc.ncbi.nlm.nih.gov/articles/PMC11005050/), J. Chem. Inf. Model., 2023.
- MELLODDY (Pejó, Remeli, Ács / CrySyS Lab), [Privacy @ MELLODDY](https://www.melloddy.eu/blog/protected-privacy-melloddy).
- Oldenhof et al., [Industry-Scale Orchestrated Federated Learning for Drug Discovery](https://ojs.aaai.org/index.php/AAAI/article/view/26847), AAAI 2023.
- Pejó et al., [Collaborative Drug Discovery: Inference-level Data Protection Perspective](https://ar5iv.labs.arxiv.org/html/2205.06506), arXiv:2205.06506.
- European Commission CORDIS, [MELLODDY project results](https://cordis.europa.eu/project/id/831472/results).
- [Substra: Our privacy strategy](https://docs.substra.org/en/0.32.0/additional/privacy-strategy.html).
