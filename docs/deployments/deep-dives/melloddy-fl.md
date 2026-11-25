# MELLODDY Cross-Pharma Federated Learning

!!! warning "Read the evidence levels"
    This case covers a completed consortium experiment with ten pharmaceutical partners. Design, results, and sources checked on 2026-11-25.

## Snapshot

| Field | Entry |
| --- | --- |
| Organization / project | MELLODDY (MachinE Learning Ledger Orchestration for Drug DiscoverY) consortium |
| Domain | Life sciences / pharmaceutical drug discovery |
| Problem | Let competing pharma companies jointly improve molecular-activity (QSAR-style) predictive models using their highly proprietary chemical and bioactivity data, without pooling or revealing that data |
| PETs used | Federated learning, orchestrated via the Substra framework (distributed-ledger-based task orchestration), plus secure aggregation of model updates |
| Deployment maturity | Completed consortium project (three-year IMI-funded effort, concluded 2022) |
| Source quality | Primary / official plus peer-reviewed / academic |
| Source | [JCIM consortium study](https://doi.org/10.1021/acs.jcim.3c00799), [platform paper](https://ojs.aaai.org/index.php/AAAI/article/view/26847), and [CORDIS project record](https://cordis.europa.eu/project/id/831472) |

## What Was Actually Deployed

Ten pharmaceutical partners trained a common feature extractor (the **shared trunk**) over separate datasets. Each company kept its own assay-specific prediction layers (the **private heads**) and associated labels. Substra orchestrated training on the consortium platform. *(Evidence: Deployment-backed. Source quality: Peer-reviewed / academic. [JCIM study](https://doi.org/10.1021/acs.jcim.3c00799).)*

Parties, scale, timeframe:

- **Participants:** ten pharmaceutical companies worked with technology and academic partners, with Owkin as coordinator. *(Evidence: Deployment-backed. Source quality: Primary / official. [CORDIS report](https://cordis.europa.eu/project/id/831472/reporting).)*
- **Data scale:** the study reports over 2.6 billion confidential experimental activity data points. *(Evidence: Deployment-backed. Source quality: Peer-reviewed / academic. [JCIM study](https://doi.org/10.1021/acs.jcim.3c00799).)*
- **Timeframe:** [CORDIS](https://cordis.europa.eu/project/id/831472) records the funded project ending on **31 May 2022**. The consortium announced results publicly in [July 2022](https://www.medical-valley-emn.de/en/press-release-melloddy-project-has-successfully-demonstrated-that-collaborating-in-ai-for-drug-discovery-is-possible-at-industrial-scale/).

Reported results:

- The [JCIM study](https://doi.org/10.1021/acs.jcim.3c00799) reports aggregate model improvements for each company on its classification or regression tasks. *(Evidence: Deployment-backed. Source quality: Peer-reviewed / academic. Results apply to the evaluated tasks.)*

## Maturity

**Completed consortium experiment.** The grant-funded project demonstrated cross-company FL at industrial scale. Ongoing operation by a consortium partner remains Needs evidence.

## Privacy Claim

The [platform paper](https://ojs.aaai.org/index.php/AAAI/article/view/26847) describes two views. The server receives masked trunk updates and combines them without seeing individual updates or the unmasked aggregate. Partners receive the masked aggregate through the server and recover the aggregate to update their shared trunk. Raw training data and private heads stay local. *(Evidence: Deployment-backed. Source quality: Peer-reviewed / academic. This is the consortium’s account of its design.)*


## Limitations

What FL plus secure aggregation did **not** fully protect, stated candidly by the project and independent analysts:

- **The aggregate and shared trunk may still reveal information.** Inference from the artifacts visible to partners remains a separate threat. The [platform paper](https://ojs.aaai.org/index.php/AAAI/article/view/26847) describes the participation and trust assumptions.
- **The DP utility result is from a separate experiment.** In their study of inference and attribution risks, [Pejó et al. (§6.1)](https://arxiv.org/abs/2205.06506) evaluated record-level DP in a centralized experiment on ChEMBL. They reported substantial accuracy loss at the tested privacy setting. This does not establish a consortium decision to reject DP. *(Evidence: Literature-backed. Source quality: Peer-reviewed / academic. The linked version is a preprint.)*
- **No composed DP bound is documented for the shared model.** The reported secure aggregation protocol controls access to updates under the stated server and participant trust assumptions.
- **Generalization remains unverified.** Measure utility, leakage, and operating cost for the tasks and partners in a new collaboration. *(Needs evidence.)*

## Builder Lessons

- **Separate "we did not share raw data" from "the data is private."** MELLODDY's honesty is the lesson: FL keeps raw data home and secure aggregation hides individual updates, but neither bounds what the shared model leaks. Name the residual leakage explicitly.
- **Test the privacy and utility tradeoff for your own tasks.** If you need a formal contribution bound, define the privacy unit and budget before measuring utility. The ChEMBL experiment is one tradeoff under specific settings.
- **Cross-competitor FL is as much governance as engineering.** A distributed ledger (Substra) was used partly to make the *process* auditable and trustworthy among rivals, mirroring the Boston MPC lesson that trust and orchestration dominate raw crypto performance.
- **Shared task definitions and data harmonization come first.** Cross-silo FL across companies needs agreed task definitions and an agreement about what model improvements may reveal, before any training runs.

## What Remains Unclear

- **Whether the platform is in ongoing production** at any partner after the 2022 conclusion is not established by the sources reviewed. *(Needs evidence.)*
- **Protections across runs.** The platform paper explains the design. Public sources here do not establish the operating controls for later deployments. *(Needs evidence.)*

## Sources

- Heyndrickx et al., [MELLODDY: Cross-pharma Federated Learning at Unprecedented Scale Unlocks Benefits in QSAR without Compromising Proprietary Information](https://pmc.ncbi.nlm.nih.gov/articles/PMC11005050/), J. Chem. Inf. Model., 2023.
- Oldenhof et al., [Industry-Scale Orchestrated Federated Learning for Drug Discovery](https://ojs.aaai.org/index.php/AAAI/article/view/26847), AAAI 2023.
- Pejó et al., [Collaborative Drug Discovery: Inference-level Data Protection Perspective](https://arxiv.org/abs/2205.06506), 2022.
- European Commission CORDIS, [MELLODDY project results](https://cordis.europa.eu/project/id/831472/results).
- [Substra: Our privacy strategy](https://docs.substra.org/en/0.32.0/additional/privacy-strategy.html).
