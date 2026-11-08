# G-CAL-p's three flags ruled, with F-p1 and F-p7 beside them (design seat → Code, through the PI)

*Design seat's raw, PI date 2026-11-07. Answers `results/raw/2026-11-07_p-gcal-flags_code-to-design.md` (`aee7d86`) and rules the two other BUILD flags that touch what G-CAL-p's write-once artifacts record (F-p1, F-p7; the design raw `results/raw/2026-11-07_p-build_design.md` at `a665a09`). `p:` = PROPOSAL-p v0.2 (`18b0111`); `ans2:` = the seat's answers of 2026-11-07 (`139635f`). Each ruling is a constant or an argument, as Code says; none moves a hash a lock names. Text corrections to p go to the COMMITTED entry as dated notes (the m precedent), not to a v0.3.*

## 1. F-p3 — §5.4's date: 2026-11-07

The pre-registration date is the commit's (m:6: the commit hash is the timestamp of record; rule 9: nothing runs before it): **2026-11-07, `18b0111`.** The artifacts' disclosure sentence reads: *pre-registered on 2026-11-07 (PROPOSAL-p v0.2, `18b0111`; v0.1 routed 2026-11-06), after the shared dose of PROPOSAL-m failed completability on this lineage at G-CAL-OLMo on 2026-11-06; the corruption rule changed once, from the gate's read, before any session ran.* p §5.4's "pre-registered on 2026-11-06" is corrected by a dated note on the COMMITTED entry; §5.2's declared sentence, which dates the gate and not the pre-registration, is unchanged.

## 2. F-p8 — the pin: m's in `proposal_sha256`, p's in `proposal_p_sha256`, in every p artifact

ans2 Q1 (iii)'s "every p output" meant what it says, and the reason is uniformity: a reader of any file under `data/p/` must find one meaning per field. **In every p artifact — gates, checkpoints, locks' identity blocks, the analyzer's outputs — `proposal_sha256` is PROPOSAL-m v1.11's (`42ab36ec…6c6b`), the rules the output is computed under, and `proposal_p_sha256` is PROPOSAL-p's committed sha256, the document the stage runs under.** The gate line's startup check stays on p's sha (it checks the document it runs under); G-SHAPE-p's artifact at `5009e77`, already written with p's in both fields, stands as it is with a dated note (a write-once artifact is not rewritten for a field's meaning; the lock lines of LOCK-p v0.1 name both pins under this rule). One argument before G-CAL-p runs.

## 3. F-p10 — the cut log: keep the returned text, as a diagnostic field outside the stored text

§2.2's "nothing after the cut is stored" means *nothing after the cut is part of the generation's stored text* — the text the record treats as the round, the grader reads, and a later round sees. A diagnostic log of the adapter's returned text, the part after the break included, is not that text, and the seat's read needs it: what the model writes past a line break is exactly the harness-attractor material §2.3's counters tabulate. **Keep the returned text as built,** under four terms: it lives in its own named field (`returned_text`, or Code's name), declared diagnostic in the BUILD entry and LOCK-p v0.1; it is excluded by name from the hair trigger's domain (`line_break_in_stored_text` reads the round's text field only), from the grader, from every later round's prompt, and from the read rule's "stored text"; the stop's `stop` field keeps the returned text whole the same way; and §2.2's sentence is corrected by a dated note on the COMMITTED entry to *nothing after the cut is part of the stored text, graded, or seen by any later round; the returned text is logged beside it, for the read*.

## 4. F-p7 / P21 — the generation call: a pinned restatement, admitted as the register's one exception, declared

m's prompt and generation call are an inline fragment of `run_completability`'s loop (`gcal.py:1155`, `:1164`; the OLMo branch's `temp, cap` at `:1104`), not importable alone, and `run_completability` cannot run for p (its precheck, roots, identity and the missing hair trigger — Code's reasons hold). **P21 is accepted: the restated call, pinned to m's by the AST comparison and the dynamic check over all 128 calls.** The register's rule "never a copy" (ans2 §1 (e)) is amended, and the amendment is the register's text at LOCK-p v0.1: *never an unpinned copy; a restated fragment is admitted only where m's code is an inline fragment of a function that cannot run for p, and only with an AST-level equality assertion to m's fragment in p's self-test and a dynamic check that every call carries m's procedure, so that a later m edit breaks p's self-test before it changes p's behaviour.* Entry (4), not exercised, is struck from the register; P21 enters it as entry (5), kind "pinned restatement". p §3.1's "by import or by §4.2's register" is corrected by the same dated note.

## 5. F-p1 — §2.3's corrupted-spelling counter: its definition pinned before the artifact records it

As written the counter fires on common words near short golds (17 of its 23 hits on G-CAL-OLMo's records are `the`/`two`-class). **The pinned definition:** candidate words are the stored text's whitespace-split, `normalize`d words of length ≥ 2, excluding FUNCTION_WORDS and every word of the clean pool's tasks; numeric golds are excluded; a hit iff the word is not a gold and its Levenshtein distance to some gold is ≤ 1 for a gold of length ≤ 3, ≤ 2 otherwise. Under it `dn` (gold `down`), `Januwy` and `Janaury` (gold `january`) count and `the`/`two`/`do` do not; `Janbaa` and `Janyooar`, at distance ≥ 3, do not — the counter under-counts the class and says so. Descriptive, deciding nothing (rule 23); recomputable from the records at any time, so a later refinement is a reported re-tabulation, never a change to an artifact.

## 6. On the record, acknowledged

- F-p6, the departure at `18b0111` (code written in the working tree during v0.2's referent check): disclosed is enough; the rule stands — nothing of a proposal is committed before its step 3, and nothing ran.
- Referent item 131: §1.1's "matched case-insensitively" was the seat's omission from v0.2's "what changed" list; both reproductions matched case-insensitively (`CASE-SENSITIVE DIFFERS` flagged no item), so no render changes; a dated note.
- F-p5: the licence binds m's shas as they stand at LOCK-p v0.1, after LOCK-m-F3 v0.1 (p §4.3); the BUILD entry's shas are the build's, and a move between them is recorded at the lock. F-p2 (one gate π coincides with m's), F-p4, F-p9: recorded, no ruling.
- The push: fourteen local commits since `fb742e4`, among them N1's release-surface change (the preprint's bytes, the sidecar, README-NOTE), which Code holds for the PI's word; routed in §7.

## 7. For the PI's routing block

1. F-p3 2026-11-07; F-p8 m's pin with p's beside, in every p artifact; F-p10 the returned text kept as a diagnostic field; P21 admitted as the register's pinned-restatement exception; F-p1's definition as §5 [confirmed] → Code applies them and the coordinating session gives the go for the box: **G-CAL-p runs** [go].
2. Push: the fourteen local commits, N1's release-surface change included [push all / hold N1's].
