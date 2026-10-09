# Corpus Index

The accompanying [corpus-index.csv](corpus-index.csv) contains 698 unique post URLs: the original 662 plus 36 non-overlapping posts extracted from five complete mirrors on 2026-10-09. These are S02's 25 posts, S05's four, S11's four, S03's two, and S24's one. Some sources were previously read but absent from the original collection; corpus additions are not necessarily newly discovered interviews or principles.

The index is deliberately metadata-only. It does not redistribute the harvested post text, claim that every URL is a product lesson, or replace reading the original page. `local_text_present` means the research artifact had text at the time of review. `page_metadata_present` means the direct X page returned a nonempty public description during the 2026-10-09 recovery pass. A recovered description can be a mention, reply, or truncated page summary.

`collection_source` separates the original harvest from the five added sources. `text_access` distinguishes harvested records from complete mirror text. The 36 additions were not included in the direct X metadata recovery pass: `False` with `not_attempted` means unchecked, not inaccessible. A mirror may omit deleted posts or attached media. Post dates are decoded from X snowflake IDs. S03's joking reply is retained for context, not counted as a product principle.

The podcast audio and machine transcripts are counted separately in the [acquisition manifest](acquisition-manifest.json). They are not X records. [Collection instructions](interview-notes.md#reproduce-the-collection) explain how to acquire readable local source text.

Use this file to locate primary material and to audit coverage. Use [casebook.md](casebook.md) and [claim-ledger.md](claim-ledger.md) for the smaller set of evidence that has been manually connected to a mechanism and a limit.
