# Fidelity Evaluation — 2026-10-10

The frozen skill did **not demonstrate an improvement** on this exploratory pilot. Baseline received 45/56 criterion points and the frozen skill 44/56. These are source-mechanism agreement points, not fidelity percentages or business outcomes. A one-point difference in one run establishes neither harm nor equivalence.

The [raw record](../examples/fidelity-2026-10-10.json) includes the protocol, frozen file hashes, all 14 answers, blinded input, unmodified judge scores/caveats, and the condition mapping revealed after scoring.

## Method

The input package was frozen at commit `29a3f044a95eff60090d8b439ff640e412e4b89b`, before adding C25–C31 or the reasoning atlas. Treatment could read only that commit's `SKILL.md` and `references/`; baseline received the same scenario without those files. Each case/condition used a fresh agent with `fork_turns=none`, the same inherited model, and a requested 350-word maximum. No browsing or original-source lookup was allowed by the evaluation instructions.

These are seven **real-source reasoning probes**, not seven predictions of implemented decisions. Some sources explain a mechanism; others interpret another founder's choice or express a prospective opinion. Agreement with those explanations cannot establish reproduction of every consideration behind a private decision.

H01–H04 use S19/S20 passages: full audio had been collected, but these explanations were not distilled into the frozen input. H05/H06 use newly acquired S26 and H07 newly acquired S27, both absent from the snapshot. Related themes were already present. Source-disjointness applies only to S26/S27; no pretraining-disjointness is established.

Criteria were defined before their corresponding generations, in three batches. Later batches were added after earlier responses began. This was not a globally preregistered benchmark. Product names were removed, but recognizable scenarios remain.

An independent fresh-context judge received anonymous A/B responses, randomized per case, and four source-backed criteria per probe. Each criterion received 0 (absent/contradicted), 1 (partial/implicit), or 2 (explicit and correct). Merely suggesting an experiment did not count as matching a particular mechanism.

## Result

| Probe | Reference passage | Baseline / 8 | Frozen skill / 8 |
| --- | --- | --- | --- |
| H01 — daily game sharing and return | S19, 07:35–08:54 | 6 | 5 |
| H02 — solo-founder exit interpretation | S19, 10:10–11:36 | 6 | 5 |
| H03 — interest graph vs. contacts | S20, 16:39–19:05 | 7 | 7 |
| H04 — reader preference vs. author exposure | S20, 21:57–23:23 | 8 | 8 |
| H05 — adjacent podcast feature | S26, 33:03–34:53 | 5 | 5 |
| H06 — conditional domain access | S26, 08:18–11:28 selected turns | 7 | 8 |
| H07 — NFT game dependency chain | S27, 11:12–12:53 | 6 | 6 |
| **Total** | Four episodes, all from 2022 | **45 / 56** | **44 / 56** |

Both conditions omitted particular explanations: repeated exposure on outside networks as a reminder, growth during acquisition negotiations as an interpretation of apparent underpricing, and an explicit extension from live audio into recording/distribution. Both listed many H07 assumptions without making the dependency chain central. Both matched H04's network tradeoff. Conditional product advice and matching a specific source explanation are different outcomes.

## Limits

- **Reference quality:** package-author paraphrases of local ASR, with contextual question/answer attribution. No independent listening or voice diarization.
- **Weak elicitation:** the judge notes that H01's notification qualification, H03's following-structure explanation, H05's historical date and H06's pivot-specific reversion were not directly requested. These weaken absolute-score interpretation. Scores and caveats remain unchanged after seeing results.
- **Sample and controls:** seven probes from four early cohost episodes, one answer per cell, no exported sampling settings. File restrictions were instructions, not an audited filesystem sandbox. Two probes from one episode are correlated.
- **Blinding:** labels were hidden, but citations/style could suggest the treatment. One model judge, no independent human scoring.
- **Prior exposure:** model pretraining and scenario recognition cannot be excluded. Similar themes already existed in the skill. No clean estimate of incremental learning follows.
- **Claim flags:** the judge flags a baseline switching-cost assertion and a treatment X citation. The citation was unverifiable from the restricted judge input, not established as false; the frozen skill includes that source. Neither flag became a separate automatic score penalty.

## Revision and remaining work

The current skill adds C25–C31, five claims and a stronger source basis for Q13, passage notes, and a [reasoning atlas](reasoning-atlas.md). The atlas separates decision owners, binding constraints, considered vs. proposed alternatives, costs and reversal conditions. It covers founder capacity, network-wide exposure, conditional asset access and behavioral dependencies rather than forcing every question through a signup funnel.

**The current skill has not passed a fresh fidelity holdout.** The seven incorporated passages are now learning material. Rerunning them would test recall or regression, not unseen generalization.

A credible public reconstruction still requires reproducible source coverage, source-verified cases across stages, failed-product and commercial records, explicit view comparisons, repeated untouched-case evaluations and independent human review. No corpus-completeness denominator or universal preference weights are available. Internal alternatives, failed-app metrics, full X-tenure tradeoffs and acquisition economics remain incomplete.

Future criteria must be fixed before a new run; rubric improvements cannot retroactively convert this pilot into success. Public-source agreement and usefulness should be tested separately. Neither certifies complete private thinking.
