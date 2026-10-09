# Evidence Coverage

## What Was Available

The original package used a best-effort local collection of public X records, public thread mirrors, an interview, and product reporting. The retained collection covers January 2024 through April 2026. Counts recomputed from its JSONL on 2026-10-09:

- 662 records, with 662 unique post URLs;
- 637 records with nonempty text;
- 25 records without text, which cannot independently support text-based principles;
- 176 records with at least 100 characters; length alone is not relevance or quality.

On 2026-10-09, a direct page-metadata recovery pass fetched 658 nonempty descriptions from the 662 public X URLs. All 25 records that were previously empty received nonempty metadata; some recovered rows are only @mentions or replies, and four already-nonempty rows hit transient TLS errors. The recovery improves verification of selected posts but does not make the corpus complete, representative, or context-complete. The recovered raw output is not shipped.

This collection includes replies, jokes, and platform commentary as well as product advice. Record count is not a count of useful growth principles. It excludes the earlier founder thread and does not establish complete historical coverage.

Nikita announced joining X as Head of Product on 2025-06-30 and stepping down on 2026-08-05, with a stated plan to remain an advisor. The collection includes some public expression during that tenure, but ends in April 2026 and does not cover the full tenure or departure. Dated biographical references in [sources.md](sources.md#biographical-context) supplement the reader introduction without expanding or recounting the 662-record corpus.

The local artifact checked had SHA-256 `494f86a0cc127b3dee96539e381b1d9cf9878a351cbd7d49b475fe09c570e0a7`. This identifies the reviewed collection; it is not an authentication of each post. The raw corpus is not shipped or required for installation. The repository provides selected summaries, original URLs, and access notes in [sources.md](sources.md), so readers do not depend on an author's local file paths.

The repository now ships a metadata-only [corpus index](corpus-index.md). This improves auditability without presenting every harvested record as a verified product insight. The manually reconstructed cases and claims are intentionally smaller than the index.

## How To Weight Evidence

Use a relevant original statement or accessible faithful mirror for attribution. Prefer a fuller explanation when a short post omits conditions. Treat interviews as the speaker's reported experience, product reporting as context, and this package's method as author synthesis.

Multiple posts by the same person, a mirror of those posts, and an interview repeating the same argument are not independent product experiments. Recurrence can identify an important theme; it does not establish a universal causal law.

## Representation And Evaluation

The seventeen principle-source entries have uneven review depth:

| Review depth | Entries |
| --- | --- |
| Official interview summary and chapters plus a readable third-party transcript; no independent audio review | S01 |
| Complete thread text available through a mirror | S02, S03 |
| Retained local harvested text; no fresh original-page verification | S04, S06, S07, S08, S09, S10 |
| Partial mirror excerpts | S05, S11 |
| Institutional event report | S12 |
| Independent media profile | S13 |
| Direct X page metadata; short posts, no full conversation context | S14, S15, S16 |
| Official episode listing plus a public transcript excerpt; full episode not reviewed | S17 |

This supports selected attributed learning material, not a representative model of the person. The package has not systematically reconstructed failed launches, alternatives considered, changing constraints, or changes in his views. The February 2026 Out of Office interview is partly reviewed through public metadata and an excerpt, but its full content has not been reviewed or distilled. See [pending material](sources.md#located-but-not-yet-distilled).

The recorded regression run passed 10/10 cases both with the revised skill and without a skill. It checks common advisory failures, not fidelity to Nikita's reasoning, and demonstrates no incremental benefit on that suite. The grouped, single-run design cannot establish equivalence or general effectiveness either.

## Distillation Standard

The package now treats a “complete” public distillation as a chain with four required links:

1. **Corpus:** locate the relevant public material and preserve its URL, date, and access status.
2. **Case:** reconstruct the situation, constraint, choice, mechanism, observation, and transfer limit.
3. **Claim:** state the reusable mechanism with its precondition and a way it could be falsified.
4. **Holdout:** test whether the model can apply the claim to a case that was not used while writing the rule.

The repository currently contains the first three links for the cases in [casebook.md](casebook.md) and the claims in [claim-ledger.md](claim-ledger.md). The fourth link has a protocol but no successful fidelity result yet. This is why the package can be substantially more useful and auditable without claiming to be a complete replica of a living person's private judgment.

Further research should preserve decisions as cases: goal and constraints -> alternatives -> choice and stated rationale -> reported outcome and limitations. Cover multiple products and career stages, including failures and counterexamples. Cross-reference each inferred pattern to its actual passages and distinguish a recurring preference from a context-specific tactic.

Before claiming fidelity, reserve real source cases from the distillation process and compare the resulting analysis with his documented choices and reasons, using only information available before the choice. Test helpfulness separately against the same model without the skill, and measure whether readers make better supported decisions. Neither test can certify access to his private thinking.

## Known Limits

- The harvest's search queries and completeness are not documented sufficiently to reproduce the full collection.
- Some X pages and mirrors are inaccessible. A retained local record is distinguished from a newly checked original.
- Empty records and missing media may omit important context.
- Most examples concern consumer-social products, including tightly connected teen networks; transfer to other markets requires checking the mechanism.
- Public commentary, memorable successes, and selected examples can introduce survivorship and selection bias.
- Platform constraints change. Dates belong to the evidence, not to a guarantee that an old tactic still works.
- Neither source provenance nor a behavioral test establishes business outcomes or forecasts success.

## Updating The Package

When adding a principle, include a dated source, a concise supported claim, the access status, and its application limits. Label new workflows as author synthesis. When a source conflicts with an existing rule, preserve the useful counterexample and narrow the rule rather than discarding it.

Behavioral evaluation should compare the same requests, model settings, and context with and without the skill; judge factual fidelity, diagnosis, scope, and actionable learning. Retain the actual answers and report failures as well as passes. Use [benchmarks.md](benchmarks.md) as a small regression suite, not as a claim of predictive accuracy.
