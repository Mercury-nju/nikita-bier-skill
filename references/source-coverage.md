# Source Coverage and Reliability

This package reconstructs selected public product reasoning. The material is broader than a collection of viral-growth quotes, but it does not establish exhaustive public coverage, complete private judgment or incremental effectiveness.

## Current material

The [corpus index](corpus-index.md) contains **699 unique X URLs**: the original 662, 36 non-overlapping posts from five mirrors, and one recovered Explode launch. The assistant screened all retained text. Before Explode, 25 records had no text and 309 had fewer than ten whitespace-separated tokens. Retrying the 25 recovered mentions with media, not new substantive statements. Missing attachments and parents can still carry important context. The index and manifest preserve that distinction.

Six complete mirrors supply 37 post texts and 1,439 words; S15 repeats an existing corpus URL. Six selected third-party X JSON clusters supply 14 post texts and 937 words, with matching author, ID and date; only Explode adds a new unique URL. Original direct-page metadata often corroborates only a prefix. These rechecks improve access and provenance rather than establish independent causal evidence. Selected immediate parents are retained separately, including parents by other people.

Eight complete publisher audio files were downloaded and locally machine-transcribed:

| Source | Published | Audio | Text review and attribution |
| --- | --- | --- | --- |
| S17, Out of Office | 2026-02-10 | 75:17 | Full ASR text read; no independent listening verification |
| S18, Where It Happens | 2022-02-15 | 72:50 | Guest segment 06:56–26:46 read; later hosts excluded |
| S19, Three Cartoon Avatars #2 | 2022-02-05 | 41:23 | Selected Wordle answers contextually bounded |
| S20, Three Cartoon Avatars #11 | 2022-04-09 | 54:22 | Selected Twitter answers contextually bounded |
| S26, Three Cartoon Avatars #7 | 2022-03-12 | 44:07 | Selected domain and podcast answers contextually bounded |
| S27, Three Cartoon Avatars #9 | 2022-03-26 | 45:00 | Behavioral-dependency answer contextually bounded |
| S36, Three Cartoon Avatars #1 | 2022-01-29 | 53:09 | Selected discussion screened; no new product claim promoted |
| S37, Three Cartoon Avatars #5 | 2022-02-26 | 49:36 | Narrative and tbh-expansion answers contextually bounded |

Total audio is about **7 hours 16 minutes**, with **79,064 all-speaker ASR words**. The latest two episodes add about 1 hour 43 minutes and 19,334 words. Other speakers, advertising, financial opinions and banter are included in those counts. No net Nikita speech count, diarization or independent listening verification is claimed. Dynamic ads can change subsequent bytes and timing.

Three complete official video-caption exports are separate from downloaded audio:

| Source | Video | Caption words, all speakers | Review |
| --- | --- | ---: | --- |
| S01, Lenny, 2024-08-25 | 98:21 | 15,566 | Selected first-person passages, now including role qualifications, crisis response, monetization and exit choices |
| S21, Solana panel, 2025-05-22 | 17:33 | 2,792 | Moderator-bounded Nikita answers; other participants excluded |
| S22, TEDxBoston, published 2013-07-11 | 11:43 | 1,789 | Full caption text read; single-presenter context with transcriber/reviewer credits |

They cover about 2 hours 8 minutes of video and 20,147 all-speaker words. Lenny upgrades an existing source; the other two add about 29 minutes. Registered video durations are whole seconds, unlike precisely probed audio. Captions can contain repetition and recognition errors. No conversion from duration or word count to thinking coverage is supported.

Three complete article bodies supply 890 words: S23's company announcement, S25's institutional Five report and S28's company closure context. S25 is a browser-visible body saved in an HTML wrapper after CLI access failed, not raw publisher HTML. S38 is a narrowly reviewed company-spokesperson passage, not an acquired full decision record.

The [manifest](acquisition-manifest.json) registers **26 acquired inputs** with artifact hashes, dates, access methods and review windows. The **37 source entries** include other selected records and reporting; these are not 38 fully acquired interviews. Original notes and metadata are shipped; full copyrighted audio/transcripts and proxy responses stay in ignored local research. [The collector](../scripts/collect_sources.py) and [instructions](interview-notes.md#reproduce-the-collection) let readers acquire their own artifacts.

## Evidence weighting

| Access or review depth | Entries |
| --- | --- |
| Complete official captions, selected passages, no independent audio review | S01 |
| Complete mirror text | S02, S03, S05, S11, S15, S24 |
| Retained local text without fresh full original-page verification | S04, S06, S07, S08, S09, S10 |
| Institutional event report or independent profile | S12, S13 |
| Direct X metadata, limited conversation context | S14, S16 |
| Complete official audio and ASR, relevant text reviewed | S17, S18 |
| Complete official audio and ASR, bounded selected cohost answers | S19, S20, S26, S27, S37 |
| Complete official audio and ASR, no new product claim promoted | S36 |
| Complete automatic captions, answer boundaries inferred from prompts | S21 |
| Complete captions, single presenter with track credits | S22 |
| Direct contemporaneous company release, interested testimony | S23 |
| Complete contemporaneous institutional article | S25 |
| Direct company context with no underlying outcome dataset | S28 |
| Selected third-party X JSON, ID/author/date checked | S30, S31, S32, S33, S34, S35 |
| Narrow reported spokesperson context | S38 |

A mirror, proxy, repeated post and interview retelling do not create independent experiments. Evidence tiers describe access, not causal strength. Self-reported conversion forecasts, revenue, deletion reductions and client returns remain unverified; advisory promotion has an additional self-interest. S36 demonstrates why complete acquisition is insufficient for attribution. S37 also explicitly distinguishes a simplified origin narrative from an iterative product process.

The latest expansion adds actual costs and exceptions: restricting tbh exposure during rebuilding, the qualified PM critique, Gas rumor spillovers and response, payment demand versus financial proof, temporary vendor credits, financing access, complementary partnerships, foregone platform revenue, public-space costs and authentic expression. It also corrects the Outline data interpretation and preserves unresolved differences among retrospective contract accounts. C24 still has no Five outcome.

## Distillation and evaluation

A usable reconstruction needs four links:

1. **Corpus:** relevant material with URL, date and access status.
2. **Case:** situation, constraint, choice, explanation, observation and transfer limit.
3. **Claim:** a mechanism with preconditions and a way it could be wrong.
4. **Holdout:** a case excluded while writing the rules, with a fair comparison to documented reasoning.

The package has **45 cases and 42 conditional claims**. Counts differ because context records, negative outcomes and additional examples need not create new rules. The [reasoning atlas](reasoning-atlas.md) connects stakeholder outcomes, alternatives, costs and view changes; it does not supply universal preference weights.

The [behavioral regression](../examples/evaluation-2026-10-09.json) passed 10/10 with and without the revised skill, demonstrating no incremental benefit on that suite. The [frozen-version fidelity pilot](fidelity-evaluation.md) compares 14 answers on seven real-source probes: baseline 45/56, frozen skill 44/56. It demonstrates no improvement and does not validate this subsequently expanded version. Its source passages are now learning material, not fresh holdouts. A separate [two-prompt expansion check](../examples/expansion-check-2026-10-10.json) retains raw answers, self-review and repairs. It uses one independent agent session, with no baseline, blind judge or frozen input, and is not a new holdout or an effectiveness test.

## Remaining coverage gaps

- The original 662-record harvest is not reproducible from documented search queries and is not an exhaustive history. The indexed years are uneven and the harvest ends before the end of the X tenure.
- Five and most other failed apps lack individual decision logs, cohorts, costs, alternatives and stopping reasons. Closure context does not identify a precise causal failure.
- Deal terms, recurring unsubsidized financials, internal experiments and unpublished advisory knowledge remain absent. Public material cannot reproduce the whole advertised service.
- Multiparty attribution is contextual; independent listening, missing parent chains and attachments remain incomplete. The augmentation parent article is unavailable.
- The Alex Heath interview remains unacquired: its normal free-post offer requires an account/subscription and the app; that offer was not claimed. Discord's historical acquisition page redirects to its general blog and is not counted as an acquired announcement.
- A Solana card embeds S21 and is counted once. The unrelated tutorial, non-substantive threads and media-only Explode follow-up were excluded from text claims.
- Fresh diverse holdouts, repeated generations, independent human judgments and actual learning/product outcomes remain needed. Model pretraining may already include source cases.

Full discoverable public coverage is unproven, and public explanations are not a complete private decision log. Preserve unresolved tensions instead of explaining every difference away. Before adding a rule, supply the dated passage, access status, case, precondition and limit. Reserve genuinely new cases before distillation if evaluating fidelity; measure practical usefulness separately against the same model without the skill.
