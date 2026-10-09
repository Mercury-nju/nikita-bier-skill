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

## Content Acquired In The Latest Pass

The [corpus index](corpus-index.md) now has **698 unique X URLs**: the original 662 plus **36 non-overlapping post texts** extracted from complete S02, S03, S05, S11, and S24 mirrors. The latest continuation adds three URLs to the previous 695. S02/S03 were already known sources, but their complete posts were absent from the indexed corpus. The five mirrors contain 1,315 whitespace-separated words, including a non-substantive joking reply in S03. Attached media were not reviewed.

Four complete publisher audio files were also acquired and locally machine-transcribed:

| Source | Published | Acquired audio | Attribution/review status |
| --- | --- | --- | --- |
| S17, Out of Office | 2026-02-10 | 75:17 | Full ASR text read; no independent listening verification |
| S18, Where It Happens | 2022-02-15 | 72:50 | Substantive guest segment 06:56–26:46 read; later hosts-only content excluded |
| S19, Three Cartoon Avatars #2 | 2022-02-05 | 41:23 | Full ASR collected; reliable speaker attribution pending |
| S20, Three Cartoon Avatars #11 | 2022-04-09 | 54:22 | Full ASR collected; reliable speaker attribution pending |

Total acquired audio is approximately **4 hours 4 minutes**, including other speakers, ads, and non-product conversation. It is not four hours of Nikita's own statements. Dynamic ads can change future episode bytes and timing.

Three complete official video-caption exports were subsequently acquired:

| Source | Video | Caption words, all speakers | Review status |
| --- | --- | --- | --- |
| S01, Lenny's Podcast, 2024-08-25 | 98:21 | 15,566 | Selected first-person passages reviewed; upgrade to an existing source, not a new interview |
| S21, Solana Ship or Die, 2025-05-22 | 17:33 | 2,792 | Nikita's answer boundaries identified through moderator prompts; other participants excluded |
| S22, TEDxBoston, published 2013-07-11 | 11:43 | 1,789 | Full caption text read; single-presenter context, with transcriber/reviewer credits |

These are **caption exports, not additional downloaded audio**. Registered durations are whole seconds from publisher/player metadata, unlike the precisely probed audio durations. The 20,147 words include hosts, advertisements, introductory repetition, and audience cues. No net Nikita word count or coverage percentage is claimed.

Two complete early article bodies were also acquired: S23's company announcement and S25's university report (690 words combined). S25's saved representation is browser-visible body text in an HTML wrapper after CLI HTTP 403 responses; it is not raw publisher HTML. Contemporary records clarify what the products were, but do not explain every failure or establish repeat use.

The Solana consumer-page card embeds S21, despite a different title. It is counted once. The previously associated tutorial URL and non-substantive NFT/mock-lessons threads were rejected as learning-source additions.

[The acquisition manifest](acquisition-manifest.json) records the exact durations, source URLs, hashes, ASR counts, and review boundaries. [Interview notes](interview-notes.md) provide passage-level findings. [The collector](../scripts/collect_sources.py) obtains full thread text and official audio so a reader can build a local corpus. The repository ships original notes and metadata, not full copyrighted transcripts or audio.

This is a substantive content expansion, but not an exhaustive historical harvest. It exposed omissions in the old corpus: even the four Death Clock posts from 2025 were missing. Record count cannot establish representativeness.

## How To Weight Evidence

Use a relevant original statement or accessible faithful mirror for attribution. Prefer a fuller explanation when a short post omits conditions. Treat interviews as the speaker's reported experience, product reporting as context, and this package's method as author synthesis.

Multiple posts by the same person, a mirror of those posts, and an interview repeating the same argument are not independent product experiments. Recurrence can identify an important theme; it does not establish a universal causal law.

## Representation And Evaluation

The twenty-five source entries have uneven review depth; two cohost episodes are collected but not used to justify principles. C24 also records an unknown early-product outcome rather than supporting a growth principle.

| Review depth | Entries |
| --- | --- |
| Complete official video captions, selected passages reviewed; no independent audio review | S01 |
| Complete thread/post text available through a mirror | S02, S03, S05, S11, S24 |
| Retained local harvested text; no fresh original-page verification | S04, S06, S07, S08, S09, S10 |
| Institutional event report or independent profile | S12, S13 |
| Direct X page metadata; short posts, no full conversation context | S14, S15, S16 |
| Complete official audio plus local ASR; relevant text reviewed, no independent listening verification | S17, S18 |
| Complete official audio plus local ASR; reliable speaker attribution pending | S19, S20 |
| Complete automatic captions; answer boundaries inferred from moderator prompts | S21 |
| Complete official captions, single-presenter context with transcriber/reviewer credits | S22 |
| Direct contemporaneous company announcement; interested testimony | S23 |
| Contemporaneous institutional report; full visible article body read | S25 |

New data adds concrete platform choices, an early model-boundary explanation, crypto-product hypotheses, naming decisions, and specific early-product records. It does not systematically reconstruct the individual failed apps, all alternatives considered, or every change of view. The paywalled Alex Heath interview remains unacquired; the Solana panel is acquired and its duplicate card is excluded. Neither discovered links nor hosts' statements inflate the attributed evidence.

The recorded regression run passed 10/10 cases both with the revised skill and without a skill. It checks common advisory failures, not fidelity to Nikita's reasoning, and demonstrates no incremental benefit on that suite. The grouped, single-run design cannot establish equivalence or general effectiveness either.

## Distillation Standard

The package now treats a “complete” public distillation as a chain with four required links:

1. **Corpus:** locate the relevant public material and preserve its URL, date, and access status.
2. **Case:** reconstruct the situation, constraint, choice, mechanism, observation, and transfer limit.
3. **Claim:** state the reusable mechanism with its precondition and a way it could be falsified.
4. **Holdout:** test whether the model can apply the claim to a case that was not used while writing the rule.

The repository currently contains 24 reconstructed cases and 26 claims for the first three links. See the cases in [casebook.md](casebook.md) and [claim-ledger.md](claim-ledger.md). The fourth link has a protocol but no successful fidelity result yet. This is why the package can be substantially more useful and auditable without claiming to be a complete replica of a living person's private judgment.

Further research should preserve decisions as cases: goal and constraints -> alternatives -> choice and stated rationale -> reported outcome and limitations. Cover multiple products and career stages, including failures and counterexamples. Cross-reference each inferred pattern to its actual passages and distinguish a recurring preference from a context-specific tactic.

Before claiming fidelity, reserve real source cases from the distillation process and compare the resulting analysis with his documented choices and reasons, using only information available before the choice. Test helpfulness separately against the same model without the skill, and measure whether readers make better supported decisions. Neither test can certify access to his private thinking.

## Known Limits

- The original 662-record harvest's search queries and completeness are not documented sufficiently to reproduce it. The fourteen-input manifest documents a separate selected collection: threads/audio/articles use the collector, while video captions and browser-only article bodies require the explicitly documented imports.
- Some X pages and mirrors are inaccessible. A retained local record is distinguished from a newly checked original.
- Empty records, missing media, replies without their parent, and ASR errors may omit or distort important context. ASR word counts include all speakers and can contain repetitions; they are not verified Nikita-word counts.
- Most examples concern consumer-social products, including tightly connected teen networks; transfer to other markets requires checking the mechanism.
- Public commentary, memorable successes, and selected examples can introduce survivorship and selection bias.
- Platform constraints change. Dates belong to the evidence, not to a guarantee that an old tactic still works.
- Neither source provenance nor a behavioral test establishes business outcomes or forecasts success.

## Updating The Package

When adding a principle, include a dated source, a concise supported claim, the access status, and its application limits. Label new workflows as author synthesis. When a source conflicts with an existing rule, preserve the useful counterexample and narrow the rule rather than discarding it.

Behavioral evaluation should compare the same requests, model settings, and context with and without the skill; judge factual fidelity, diagnosis, scope, and actionable learning. Retain the actual answers and report failures as well as passes. Use [benchmarks.md](benchmarks.md) as a small regression suite, not as a claim of predictive accuracy.
