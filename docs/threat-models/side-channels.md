# Side Channels

Side channels leak information through indirect signals rather than intended data paths.

## Examples

- Timing differences
- Cache behavior
- Memory access patterns
- Error messages
- Query volume
- Output size
- Power or resource usage

## Practical Example

A TEE protects plaintext during inference, but timing behavior reveals which branch of a model or retrieval pipeline was used.

## PET Implications

TEEs, HE, MPC, and RAG systems need metadata and implementation review, not just high-level architecture diagrams.
