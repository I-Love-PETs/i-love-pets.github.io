# I ❤️ PETs

A practical field guide to Privacy-Enhancing Technologies.

I ❤️ PETs helps privacy engineers, platform engineers, and architects decide which privacy-enhancing technology fits a real system they may need to scope in the next few weeks.

Researchers, product teams, policy teams, and students are welcome secondary readers, but the editorial center is the builder responsible for a PET decision.

This is not another awesome list. Existing repositories already collect papers, frameworks, tools, datasets, tutorials, and links. This project focuses on guidance: decision support, architecture patterns, threat models, real-world deployment lessons, open research problems, and implementation tradeoffs.

## What This Project Helps You Answer

- Which PET should I use for this data-sharing or privacy problem?
- What architecture fits the trust boundaries?
- What tradeoffs should I expect across privacy, utility, cost, latency, and complexity?
- What can still go wrong after a PET is deployed?
- What evidence should I collect before committing to a design?

## Main Sections

- **Start Here**: a practical taxonomy of PETs and the problems they solve.
- **PET Compass**: decision matrices and tradeoff guides for choosing a PET.
- **PET Patterns**: reusable implementation patterns with failure modes.
- **PET Architectures**: end-to-end architecture sketches with trust boundaries.
- **Use Cases**: domain-specific guidance for healthcare, finance, advertising, public sector, and AI.
- **Threat Models**: practical adversary models and privacy attack examples.
- **Fix My Itch**: actionable research and engineering problems worth solving.
- **Benchmarks**: ways to measure privacy, utility, cost, latency, and developer effort.
- **Deployments**: lessons from real-world PET deployments.

## Fix My Itch

Fix My Itch is the project's catalog of meaningful open problems. Each problem should explain the pain, why it matters, what is unsolved, plausible directions, difficulty, and who it is good for. The goal is to turn vague "future work" into concrete work someone can start.

## Trust And Currency

Decision support is only useful if readers can see why a claim should be trusted and whether it may be stale. Fast-moving claims about cost, performance, tooling maturity, and production readiness should be dated and backed by evidence wherever possible.

The project uses evidence levels:

- **Measured**: benchmarked with stated workload, environment, and date.
- **Deployment-backed**: supported by a named deployment, postmortem, or case study.
- **Literature-backed**: supported by papers, standards, or technical reports.
- **Expert judgment**: editorial judgment that needs review and may change.
- **Needs evidence**: useful claim, but not yet trustworthy enough for decision support.

See the Project Standards section in the site for the full evidence and review policy.

## Run Locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open <http://127.0.0.1:8000>.

## Build

```bash
mkdocs build
```

## Deploy

The site is designed for GitHub Pages. The deployment workflow builds the MkDocs site and publishes it through GitHub Actions.

## Contribute

Contributions should explain decisions, tradeoffs, and failure modes. Prefer practical guidance over link dumping. Every pattern should say when not to use it, every architecture should state a threat model, and every research problem should be actionable.
