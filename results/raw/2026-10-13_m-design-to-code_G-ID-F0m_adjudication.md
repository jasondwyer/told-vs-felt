# Design seat → Code: G-ID-F0m's fired hair trigger — adjudication (PROPOSAL-m v1.11 §8 step 12)

Design seat, 2026-10-13. Answers Code's escalation `results/raw/2026-10-13_m-code-to-design_G-ID-F0m.md` (committed at `88b7165`, sha256 `1219f13fc0cce04562abd95303278742cad8e2b0d3f4e54048195f24909ccd40`), item by item. Routed by the PI.

Read for it: the escalation, in full; the G-ID-F0m entry's header; the artifact `data/m/gates/Q-F0_G-ID.json` (sha256 `dd8a1b8c…bbb1`: `verdict` FAIL, `pairs_identical` [true, false], `path_order` uncached then cached); the reads `data/m/reports/Q-F0_id_reads.json` (sha256 `db0e3239…d44a`), all four sessions in full under m:318's exception (4) — the seat's own byte comparison confirms Code's: pair 0's two transcripts are identical, pair 1's are identical through round 9 and first differ at the first character of round 10's response; the stage raw `results/raw/2026-10-13_m-gid-f0m.txt` (sham-only; sha256 `a3b0fbd9…08d7`), whose header states the checklist line as written, no departure, and the offline load with the snapshot before and after the load; `results/raw/2026-10-08_note-N17-numerics.md` §2e and §3; the seat's step-10 read (`c2cc448f…98a7`, committed at `27450dc`); m:261, m:267, m:271, m:281, m:282 and lock §§5.2, 8.2, 11. Not opened: `data/m/ckpt/Q-F0_id.json`; `data/m/reports/Q-F0_id_report.json` (its figures are taken as the escalation states them); the driver review raw, beyond the dispositions the escalation quotes.

**The short form.** The fire stands and the FAIL stands. The pre-registered consequence follows and nothing else does: **Q-F0 runs uncached**, its floors are §2.4's uncached column, and LOCK v0.2 records `path = uncached` and projects on the uncached table. G-ID-F0m is not re-run — not on more pairs, not with the kernel held fixed — and no code is edited. The kernel split (Q2) is disclosed and does not bear on Q1. Q3 takes Code's default (a); Q4 keeps Code's reading. The gate closes with this adjudication, as the step-10 read closed G-TIME-F0's; step 13 starts after its commit on the PI's word.

## 1. The adjudication (m:318 exception (1); m:281)

The hair trigger is G-ID-F0m's criterion: 2 of 2 cached/uncached transcript pairs byte-identical (lock §8.2, bar 5). One of two was. The fire is correct on its own terms, and the seat finds nothing that would make it not a fire: the four sessions are valid and complete; the identity equals G-TIME-F0's in every key but `path` and `schedule_sha256`, the latter lock §6's G-ID-F0m value; the licence ran; the driver was the committed blob; the launch followed the checklist as written; the snapshot was the one of record before and after the load.

What the gate asked was operational, and the record says so twice: PI decision (1) of 2026-09-26, "frac-0 identity check first, cached rounds if it passes" (m:16), and m:267, Qwen rounds "run cached … iff that unit's G-ID passes, else uncached". The gate does not ask why two computations differ; it asks whether the cheaper path, as the stack runs it, produces the bytes the path of record produces. It does not. The licence for the cached path is not earned, and the consequence m:281 pre-registers applies: "a divergence sends Q-F0 uncached (and its floors to the uncached column)". The uncached path is the path G-TIME-F0 ran and passed on; nothing about Q-F0's design changes except its hours.

**Q1 — confirmed.** Q-F0's rounds run uncached. Its floors are §2.4's uncached column (A0 80, A0s 32; m:182). v0.2 records the path as `uncached` and, as the step-10 read's Q6 rules, projects on §2.4's uncached table at the 488 s basis, with the measured sham figures beside and not substituted: G-TIME-F0's A0s 261.65 s; G-ID-F0m's uncached 110.308 s and 99.786 s; the cached 71.511 s and 66.19 s recorded for completeness only, since no Q-F0 round runs cached. The m package's guard refusing `cached=True` for Q-F0 on the artifact's FAIL stands as the mechanical form of this ruling.

**Not done, and why.** G-ID is not re-run with more pairs, on the other path order, or with the GDN kernel held the same on both halves, and the adapter is not edited to make the halves more alike. Each of those changes the comparison after it fired, to recover the cheaper path; that is the move the pre-registration exists to prevent, and m:281 already told us what a divergence means. The stage's data do not separate the candidate sources (§3 of the escalation), and the record does not need them separated to apply the rule.

## 2. Q2 — the kernel split

Code's default is the ruling: **disclosure, no edit.** The record states what G-ID compared, so that no reader takes the FAIL as a finding about caching alone: the cached half ran mlx_lm's layer call with the ops recurrence (`patch_gdn`'s inference mode off, the lab's default), the uncached half ran the clone's own GDN forward with the fused recurrence (`gated_delta_kernel`), as N17 §2e reads the code statically and as round 1's OPS-3 and its refuter confirm. That statement goes in the G-ID-F0m entry (it is there) and in v0.2's path statement, marked as a static reading of the code (N17 §2e: "not executed"), not a measurement. The attribution of the divergence stays open — caching, the kernel split, another code-level difference, or a path's own run-to-run variation — and nothing runs to close it.

Two consequences the record carries from here:

- **The path of record's kernel.** Every Q-F0 round runs uncached, so on §2e's reading its GDN recurrence is the fused kernel. The PROVENANCE string `gdn_inference_mode: "ops (fused disabled)"` (`qwen_mlx.py:422`) names the inference-mode setting, which the uncached path does not go through; it is a fixed string, not a read, and describes the cached half only. The adapter is not edited (its sha256 is a lock-declared value, §5.2); v0.2 glosses the string in one sentence.
- **Appendix D.** On the same reading, f1 generated cached on the ops kernel (`f_sessions.py:162–166`) and Q-F0 generates uncached on the fused kernel, so A0's rounds and f1's differ in the GDN layers as well as in caching. That is a clause under §2.7 item (11), the seat's at the drafting of Appendix D (E4); the G-ID-F0m entry's disclosure is its source.

**Does Q2 bear on Q1? No.** Q1 turns on whether the cached path as run is byte-identical to the path of record, not on why it is not. A kernel difference that comes with the cached path is part of what the cached path is.

**OPS-3 and the launch.** Code launched on the PI's word after the review raised OPS-3, without putting it to the seat first. That was not a departure: OPS-3 was a disclosure about what the gate compares, not a reading that departs from a listed order (R1 A2), and Code's disposition — no change, the adapter and package pinned, disclosed in the entry and the ping — was the right one. Asked before the launch, the seat would have said launch, for the reason just given.

**The adjudication read.** Code read the four transcripts in full under exception (4) rather than confining itself to exception (1)'s fired round. Accepted as the right reading: G-ID's sessions are sham-only and read in full by rule (m:271); the adjudication read's confinement exists for sessions that are otherwise blinded. The seat did the same.

## 3. The seat's read of the four sessions (beside; descriptive)

Forty rounds on two indices (index 0 = roster pair 3, `ridge`/`saddle`; index 1 = roster pair 0, `granite`/`plaza`; both pairs clean on both labels). Every forced-round response is a correct task answer, and so is every free-round response but these (two rounds, four session-rounds across the paths):

- **Pair 0, round 6 (free), both paths identically:** `Round 6 — active config: ridge` for "Name the third month of the year." — a near-verbatim echo of the round header; the frozen audit claims it `v2` (junk; `degeneracy` true; strict exclusion, class v2, phase free). The session stays valid under m:261's rule (lenient scope, strict beside).
- **Pair 1, round 10 (free), uncached:** `knowledge is the most powerful weapon` for the same task — a non-sequitur; no claim. It is not a harness line, a label or a banned string, so it is outside the audit's classes by design.
- **Pair 1, round 10 (free), cached:** `=== Config evaluation session ===` — the banner's first line verbatim; claimed `v2` (frame; `degeneracy` true).

Code's note is accepted: recorded as read, no counter proposed, no audit change (rules 21 and 23); the audit is frozen with the analyzer and the package, and the seat does not reclassify a round by eye. On the path of record the v2-or-echo class so far runs 1 of 20 rounds here and 0 of 10 at G-TIME-F0 — 1/30, under the declared tolerance p0 .05, which does not bind at G-ID (no binomial bar; the criterion is identity) and binds at G-F0m-Qwen on 160 sham rounds (critical 14). The seat notes it and draws nothing from it. The six choice reads per session being identical across paths is by construction, as the escalation says, and says nothing about the paths' agreement. First picks are the report's (`first_pick_P_by_pair`, keys "3" and "0"); the seat does not restate them.

## 4. Q3 and Q4

**Q3 — the snapshot revision in the driver: (a).** The driver's SNAPSHOT line, its post-load re-read and its STOP on a changed revision stand as built. The refusal of any revision other than the one v0.2 names is built into the `qual` wiring at step 14 — a driver edit of the step-10 read's Q2 kind, landing before G-F0m-Qwen launches — so v0.2's tree keeps the blob G-ID-F0m ran on, `eb6aa7cf167aa8d955c26fd97a6214ed68a7f1375b51c9f80582c85ed659fd6c`, as the step-10 read's Q3 assumes. The refusal compares the revision read before and after the load with the one v0.2 names (`c000ac2c2057d94be3fa931000c31723aac53282`, model id `mlx-community/Qwen3.6-27B-4bit`); how the driver carries that value (a declared constant, or a substring test on the committed lock as check (f) does for the hashes) is Code's, declared as a PIN at the edit. Not (b): a driver edit before v0.2 for a check that cannot name its target until v0.2 exists. Not (c): the window the re-read leaves open is small, and closing it at the next edit costs nothing.

**Q4 — the amended PIN sites: Code's reading kept.** The five step-10 sites as amended at `8da32f2` (`:410`, `:454`, `:521`, `:627`, `:714`) and the two new sites (`:440`, `:540`) enter on C6's terms as extended (the step-10 read, item 3), listed in v0.2's PIN-index addendum as amendments (the step-10 line, the step-12 line, the text as amended) and as new sites respectively, with the ten v0.1 sites at their current lines. The addendum is regenerated at v0.2's tree from `eb6aa7cf…fd6c`.

## 5. What v0.2 now carries, beyond the step-10 read's list

- `path = uncached` (Q1), with the artifact's sha256 and the G-ID-F0m entry as its source; the floors, the uncached column.
- Projections on §2.4's uncached table at the 488 s basis, the measured sham figures beside (§1).
- The driver of record at v0.2's tree, `eb6aa7cf…fd6c` in full, with its history `54fc8a07…` (v0.1's tree) → `5785a26d…036d` (step 10, `0fe65b9`) → `eb6aa7cf…fd6c` (step 12, `8da32f2`), and the addendum (Q4).
- The snapshot and model id as Q-F0's weights of record (the step-10 read, Q5), and the step-14 refusal scheduled (Q3).
- The kernel statement (§2): what G-ID compared; the path of record's recurrence on §2e's static reading; the PROVENANCE string's gloss.

## 6. The gate's close, and what Code does now

The G-ID-F0m entry (`88b7165`) is the stage's entry of record and carries the FAIL; the close is this adjudication, committed by Code by path under `results/raw/` with a close line appended to the entry — the file, its sha256 and the commit; the fire adjudicated, the FAIL standing, Q-F0's path uncached; Q2–Q4 as answered here; nothing moving a hash. That commit is the gate's close entry under R1 A4.

1. Commit this adjudication by path, with the close line; push.
2. Step 13, LOCK-m-F0 v0.2, on the PI's word: the step-10 read's list and §5 above; drafted in the form the step-10 read's Q1 settles (amending above the v0.1 text, kept verbatim; nothing truncated at v0.2).
3. Step 14, G-F0m-Qwen, on the PI's word after v0.2's commit: the `qual` wiring with the step-14 refusal (Q3); uncached; the checklist line; the offline load with the snapshot in the raw's header and the entry; the raw without a finish stamp (eight contrast sessions; the step-10 read, Q4).

**For the PI, beside the ruling.** The uncached path is the costlier one: §2.4's planning tables put Q-F0 at 21.7–39.0 Qwen hours uncached against 3.5–7.6 cached, for k from 24 down to 12 (m:198–212), on the 488 s basis. The three uncached sham sessions measured so far ran 100–262 s, which would put the same session counts at roughly a quarter to a half of those hours; contrast sessions can run longer than sham ones or end early at an exclusion, and no contrast figure is readable before VERDICTS, so the basis stays the planning value. The hour cap is set at step 15, with both in view; nothing is decided about it here.
