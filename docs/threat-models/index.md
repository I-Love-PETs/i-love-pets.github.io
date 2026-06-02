# Threat Models

Privacy claims are meaningless without a threat model.

A useful threat model states:

- What data or behavior is protected
- Who the adversary is
- What the adversary can observe
- What the adversary can change
- Which parties may collude
- What output is intentionally revealed
- Which assumptions must hold

## Fast Checklist

| Question | Example |
| --- | --- |
| Who sees inputs? | Clients, silos, coordinator, cloud operator |
| Who sees outputs? | Analyst, model owner, all participants, public |
| Who can deviate? | Malicious client, curious coordinator, compromised enclave |
| What metadata leaks? | Timing, query volume, participant presence, cohort size |
| What repeats? | Queries, training rounds, release cycles |
