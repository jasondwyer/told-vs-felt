# ADDENDUM-p1 to PROPOSAL-p v0.2 — a p checkpoint's outcome enters the posting its VERDICTS entry reaches
## v0.1 — design seat, PI date 2026-11-15 (the PI confirms the date at routing)

*An addendum, not a new version: PROPOSAL-p v0.2 (tracked at root, the file its `PROPOSAL-p v0.2 — COMMITTED` entry names) stays the proposal of record. `p §N` is a section of that file; `m:N` a line of PROPOSAL-m v1.11 at root (sha256 `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b`); `A-m1 §N` a section of ADDENDUM-m1 v0.1 at root (`f26bc59`). It changes one thing: the posting at which a p unit's outcome is used. p's design, arms, floors, bars, keys, schedules, locks (LOCK-p-OLMo-{sft,dpo,instruct} v1.0, `038bf3e`), campaigns, analyzer and VERDICTS computation are untouched, and no hash moves. It is written with every p outcome unknown: no `PROPOSAL-p OLMo-{ckpt} — VERDICTS` entry exists, and the campaigns' picks, where campaigns have run, are in checkpoint files that no seat and no PI reads before VERDICTS (m:318). Placed untracked over the bridge at root; Code commits by path on the PI's routing; the pod session adds its close line. Calendar dates only; the commit hash is the record.*

---

## §0 What this addendum does, and why now

**0.1 The record.** p §5.1 labels the OLMo rows at v1 by m's units (*concluded, not answered — the told control at this stage was not run: dose not completable*, m:338) and says in its heading that v1 comes "(before any p VERDICTS, by construction)"; p §5.2 makes p's unit the told control of m:338's rule at v2; p §8 step 7 calls the VERDICTS entries "the v2 posting's inputs under §5.2". As registered, then, a p outcome is used at v2 only, and v2 follows Q-F3's VERDICTS (m:349; A-m1 §2.3).

**0.2 What changed.** The construction no longer holds. LOCK-p v1.0 ×3 were committed on 2026-11-14 (`038bf3e`); the replacement box was characterized on 2026-11-15 at the locks' identifier (`7ab4d2f`); the three campaigns are hours long (G-PWR (p), `3e1b614`: 3.35 h at m:205's basis); and the PI's v1 is aimed at early December (§3 item 2). p's VERDICTS can therefore exist weeks before v1. Under p §5.1 as written, that v1 would call three rows *not run* that had been run, and p §5.1's declared sentence has no member for their state.

**0.3 The rule already exists in m.** m:349: "An OLMo checkpoint's VERDICTS entry records its row state; its sentences enter the enumeration of the posting it reaches." m:338 labels a post-training row *Answered* "iff its own L0-OLMo-c" and otherwise *concluded, not answered — the told control at this stage [did not pass: outcome | was not run: reason | is pre-registered and pending at this posting]*. This addendum applies m's rule to p's units at v1 as p §5.2 applies it at v2.

**0.4 Why this is a staging change and not an outcome-dependent one.** No p outcome exists at this writing or at this addendum's commit (§4 step 2 records it). The rule is total over outcomes: PASS, DEAD, REVERSE, INDETERMINATE and NOT-RUN each have their label and their status sentence, and nothing is included or left out by result. It is A-m1 §0.3's case: a schedule change made with every outcome unknown, visible in this document, its commit and one disclosure sentence (§2.3).

## §1 Decision (p-1), proposed (the PI's routing block is its record)

*A p checkpoint's outcome enters the posting its `PROPOSAL-p OLMo-{ckpt} — VERDICTS` entry, or its `— NOT-RUN` record, reaches, v1 included: from that entry's commit, p's unit is "the told control at this stage" in m:338's rule at every later posting. A checkpoint with neither at a posting keeps p §5.1's form there.* The heading clause of p §5.1 and the last clause of p §8 step 7 are replaced by this rule. Everything else in p §5 stands: §5.2's rule and its declared sentence, m's three NOT-RUN rows beside p's as text, §5.3's Clock, §5.4's disclosure. Q-F3 is untouched: A-m1 (10′) stands, its VERDICTS session runs only after `POSTING v1`, and §8.2's v1 text is A-m1 §2.4 (a)'s.

## §2 What follows

**2.1 At v1, for a row whose p VERDICTS entry exists:** the label by m:338 on p's L0-OLMo-c; §8.1's status sentence (m:343) with p's outcome, then A-m1 §2.4 (b)'s sentence, then p §5.2's declared sentence; the abstract's OLMo clause in m:338's form for the number of passing stages. The ceiling does not move: "L0-OLMo-c never enters the ceiling" (m:341), and v1's is Fallback-1 iff L0.

**2.2 The enumeration's path at v1.** p §5.2 brings p's states into the v2 posting through `p_analyze` (p §4.4). Code states at its pre-read whether the analyzers of record resolve p's states at the v1 posting as they stand. If they do, v1 runs through them. If they do not, **no hash-moving change is licensed by this addendum**: for the OLMo rows, the abstract's OLMo clause and §8.1's sentences, the v1 enumeration is derived by hand from the p VERDICTS entries under m:338 and m:343 and values-checked by Code at the `POSTING v1` entry — the form m:349 gives a posting no analyzer reached, declared here for these rows — and the analyzer's own v1 output for those rows is recorded beside it as superseded by this addendum.

**2.3 The disclosure sentence, the PI's words, declared here,** in §8.1 at the first posting it applies to: *PROPOSAL-p registered its outcomes for the second posting; ADDENDUM-p1 ([hash]), committed before any p outcome was computed, moved them to the posting they reach.* It asserts no null and no thesis and is outside §7.5's enumeration; Code values-checks it at the `POSTING` entry against this document and the VERDICTS entries' commits.

**2.4 Order.** This addendum's commit entry precedes the first p VERDICTS session. Each p VERDICTS entry records, in m:318's form, that it was computed with Q-F0's outcome known and after this re-specification.

## §3 The PI's routing block — what it must carry

1. The date; decision (p-1) adopted or declined. Declined: p §5 stands as written, p's outcomes enter at v2, and a v1 posted before v2 reads its OLMo rows as p §5.1 has them.
2. The PI's target for v1, in his words (2026-11-15, to the seat: "the most solid paper I could drop on Arxiv early Dec").
3. The word for the three p VERDICTS sessions, to follow this addendum's commit.

## §4 Code's block, in order

1. Referent check (§5), and the answer to §2.2 (which path v1 takes). An unresolved substantive item → STOP.
2. **Commit `ADDENDUM-p1 v0.1 — COMMITTED`**: this file tracked at root, its sha256; the PI's routing quoted verbatim as the record of (p-1); the statement that no `PROPOSAL-p OLMo-{ckpt} — VERDICTS` entry exists at this commit, with each campaign's state at it.
3. On the PI's word: `PROPOSAL-p OLMo-{ckpt} — VERDICTS` and `— secondary DVs` ×3 as p §8 step 7 has them, each entry carrying §2.4's sentence; then the seat's reads.

Entries this addendum adds to p §8's list: `ADDENDUM-p1 v0.1 — COMMITTED`.

## §5 Referents Code verifies at commit — only what this document quotes

**PROPOSAL-p v0.2 at root:** §5.1 (its heading clause; the row label), §5.2 (its rule and declared sentence), §5.3, §5.4, §4.4, §8 step 7. **PROPOSAL-m v1.11 at root:** m:318, m:338, m:341, m:343, m:349. **ADDENDUM-m1 v0.1 at root:** §0.3, §2.3, §2.4 (a) and (b). **Entries:** `038bf3e` (LOCK-p v1.0 ×3), `7ab4d2f` (the box), `3e1b614` (G-PWR (p): 3.35 h).
