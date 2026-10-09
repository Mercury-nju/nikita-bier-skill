# Corpus Index

The [metadata index](corpus-index.csv) contains **699 unique Nikita post URLs**: the original 662, 36 non-overlapping posts from five complete mirrors, and the recovered Explode launch post. S15's complete MVP mirror and the other selected proxy rechecks duplicate existing URLs; they do not inflate the unique count. Parent posts by other people are context, not Nikita corpus additions.

## Text screening on 2026-10-10

The assistant read the retained text of the previous 698 records in four batches and selected supported cases for reconstruction. This is text screening, not independent human review, full reply-context review or attachment verification.

| Retained text length, before the Explode addition | Records |
| --- | ---: |
| Empty | 25 |
| 1–9 whitespace-separated tokens | 309 |
| 10–29 | 252 |
| 30–59 | 87 |
| 60 or more | 25 |

Those 698 records contain 11,875 whitespace-separated tokens, including mentions and URLs. Explode adds 122, bringing the retained total to 11,997. Many short records are jokes or replies; length is not a relevance label. All 25 empty records were retried through public third-party JSON: their recovered textual payloads consist only of mentions and include media. The attachments remain unknown, and no substantive statement was recovered. The original retained text is preserved rather than silently replacing missing text with mentions.

## Fields and access

The index ships metadata only, not harvested text. `local_text_present` and `local_text_chars` describe the local artifact; neither implies a useful product claim. `page_metadata_present` describes the earlier direct-X recovery, which can return a mention or truncated description. `False` with `not_attempted` means unchecked.

`collection_source` and `text_access` preserve original acquisition provenance. Selected rechecks are linked through `distillation_sources`, which maps original URLs cited in source entries; it is not a claim that every sentence in a linked record supports a principle. `text_words` is the retained whitespace count. `review_status` is `assistant_text_screened` or `missing_harvest_text`; neither certifies complete conversation context. `mention_only_recovery_media` marks the 25 successful retries without recovered substantive text.

The complete mirrors can omit deleted posts and attachments. The FxTwitter responses are third-party representations: matching ID, author and date improves traceability but does not authenticate every sentence against the current original page. Hashes and access distinctions appear in the [manifest](acquisition-manifest.json). Podcast audio, captions and parent context are counted separately.

Use [casebook.md](casebook.md) and [claim-ledger.md](claim-ledger.md) for the smaller set of source-backed mechanisms, counterpoints and limits. [Collection instructions](interview-notes.md#reproduce-the-collection) explain how readers can build local readable source artifacts.
