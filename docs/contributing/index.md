# Contributing

Contributions should make the guide more useful for decisions. Prefer a small, specific improvement over a broad shallow page.

## Before You Add A Page

- Check whether an existing page should be improved instead.
- Identify the primary reader and decision.
- Name the threat model or explain why the page is not making a privacy claim.
- Include at least one decision table, worked example, failure mode, checklist, concrete research problem, or tradeoff matrix.
- Run `mkdocs build`.

## General Review Checklist

- Does this help someone choose, design, evaluate, or debug a PET?
- Does it state assumptions and threat model?
- Does it include when not to use the approach?
- Does it name failure modes?
- Does it avoid pretending the PET solves everything?
- Does it link to related pages only when the link adds context?
- Are claims sourced, measured, or labeled as expert judgment?

## Pattern Page Checklist

- Does it say when NOT to use the pattern?
- Does it state a threat model?
- Does it explain failure modes?
- Does it avoid pretending the PET solves everything?
- Does it include evaluation criteria?

## Architecture Page Checklist

- Are actors named?
- Are trust boundaries explicit?
- Are data flows clear?
- Are assumptions listed?
- Are operational risks included?

## Fix My Itch Checklist

- Is the problem concrete?
- Is the current workaround described?
- Is success measurable?
- Is there a possible first contribution?
- Is the difficulty level clear?

## Deployment Checklist

- Is deployment maturity clear?
- Are claims sourced?
- Are limitations included?
- Is this a real deployment or only a proposed use case?

## Templates

Use the templates in this section for new patterns, use cases, architectures, Fix My Itch problems, and tool reviews:

- [Pattern template](pattern-template.md)
- [Use case template](use-case-template.md)
- [Architecture template](architecture-template.md)
- [Fix My Itch template](fix-my-itch-template.md)
- [Tool review template](tool-template.md)
