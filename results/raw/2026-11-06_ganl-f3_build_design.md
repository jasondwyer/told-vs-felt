# G-ANL-F3 (m:291): Code's build design, the PIN register and the dated notes (2026-11-06)

*Code's raw, committed with the build. The routing is the PI's of 2026-11-06 on the seat's answers (`results/raw/2026-11-06_ganl-f3_design-to-code_answers.md`, sha256 `4edfbb8e…ca42e`; the STOP's close at `54bbfe5`), relayed by the coordinating session (in its message, not a file): "G-ANL-F3, to A1–A5: Build it in scratch, per C1. Apply B as written." Order (a): no `LOCK-m-OLMo-*.md` exists (checked again immediately before the commit). The commit follows the PI's ruling of 2026-11-06 on N9, in chat, relayed: "Commit with flag". Before the commit a blind code review found no MAJOR defect and five MINOR ones; all five are fixed here, as are the NOTEs that changed a text a reader would trust, but for two items of NOTE 7 (§5). A follow-up review of the fixes found no MAJOR or MINOR defect and four NOTEs: three applied, one recorded as N11 (§5). The values-check's third pass reviewed the last code delta and found no MAJOR or MINOR defect, four NOTEs and one observation, all applied (§5). Its fourth pass checked those fixes and found no MAJOR or MINOR defect and two NOTEs: one is N13, a FLAG, and one is disclosed (§5). `m:N` = PROPOSAL-m v1.11 (sha256 `42ab36ec…6c6b`); `A-m1:N` = ADDENDUM-m1 v0.1 (sha256 `ea08322d…9001`); `answers:N` = the F3 prebuild answers; "the answers" = the seat's G-ANL-F3 answers. Code is cited by function or constant name in `scripts/m_analyze.py` (the analyzer) unless another file is named.*

## 1. What is built, against each ruling

### A1 — the regression, (R1)
- **The battery case** `_bt_qf0_regression`: Q-F0's VERDICTS and secondary-DV computations run in-process through `run_verdicts` on Q-F0's committed inputs, with the identity of record:
  - the analyzer bytes from `git cat-file blob ed8e886:scripts/m_analyze.py`, asserted to hash to `655e0f7f…c16f` (`RECORD_ANALYZER_SHA256`);
  - the package and closure shas LOCK-m-F0.md:147–149 names (`RECORD_PACKAGE_SHA256` `5f646db6…d771`, `RECORD_CLOSURE_SHA256` `a3bc7bb9…b22b`);
  - PIN-14's check runs inside `run_verdicts` against those three (the lock text names all three);
  - `inputs.lock` = LOCK-m-F0.md as the record has it.
  - The outputs are written to a temp directory and compared byte for byte with `data/m/verdicts/Q-F0_VERDICTS.json` and `Q-F0_secondary.json`. **Both are identical** (sha256 `ec7d2082…`, 81,084 bytes; `dcaaaac3…`, 12,052 bytes). A difference fails the check, and a failing battery writes no artifact (a STOP, A-m1 §2.5 (3)).
  - The report (`REGRESSION_REPORT`, in the artifact): it shows that the extended analyzer, on m's moved package, recomputes Q-F0's computation to the byte with the identity fields bound to the record's; it does not show that the extended blob satisfies LOCK-m-F0's binding (only `655e0f7f…` does); the v1 `posting` command records the three shas and does not refuse on them (PIN-42's binding; referent check N2).
- **The preprint of record** — dated note N1 below.
- **PIN-29's exception, by blob** (`PIN29_RELEASED`, `_OpenHook._check` / `_blob_ok`): the battery's open hook admits exactly the seven Q-F0 files, each only while its bytes hash to the sha256 pinned in the source; the regression check asserts each pin equals HEAD's blob. `BLOCKED_REL` adds `data/mf3/ckpt`, `data/mf3/reports` and `data/mf3/verdicts`; the no-canonical-write snapshot (`_bt_snapshot`) covers `data/mf3` too. Checks: the hook admitted exactly the seven; another file under data/m's roots, each mf3 root, and a released path whose bytes do not match its pin are refused.
- **"The OLMo v1 outputs unchanged"** (`_bt_v1_unchanged`): the analyzer of record (ed8e886's blob, executed in-process as a module) and the extended file give equal `v1_outputs` for all 1,080 tuples under both flag values (2,160 evaluations), with one NOT-RUN phrase and again with a distinct reason per unit; the two placeholder tables are equal.

### A2 — PENDING at v2, (P1)
- `check_tuple_v2` raises `PendingAtV2` with `PENDING_AT_V2`'s text, naming m:324's closure and its two branches. The battery asserts that refusal on the 218,855 PENDING-bearing tuples under each flag value, and the full output set on the other 300,625.
- The closure runs upstream, as the seat's A2 has it ("as a PI-stop record or a NOT-RUN record"): a checkpoint with sessions is PI-stopped through its campaign driver (a PI-STOP terminal) and `verdicts` analyzes it as obtained (m:324), as before; one whose campaign recorded no session is closed by `not-run --v2-closure`, which writes the NOT-RUN with cause `pending-closed-at-v2` (only that cause; refused without the flag and for Q-F0). `--v2-closure` requires `--campaign`: the unit's campaign checkpoint, committed at HEAD and read once, its identity (unit, stage campaign) checked and its session count read, refused if it records a session; or `none`, a declaration that the unit has no campaign checkpoint, refused while `data/m/ckpt/{U}_campaign.json` exists in the tree or at HEAD. The output records which (`v2_closure`). `crosscheck_coordinate(..., v2=True)` admits `pending-closed-at-v2` at v2 and refuses PENDING.

### A3 — the scope, all three now
- **`verdicts --unit Q-F3`** (`run_verdicts_f3`, dispatched from `run_verdicts` after V0's gate line):
  - V1 refusals before any pick-bearing byte: the pinned proposal; the Clock dates; the committed analyzer and lock; the lock naming the analyzer sha256, m's `package_sha256` and the **Q-F3 closure** sha256; the v1 posting on the posted text committed and PASSing C7's bar (decision (10′); N6); Q-F0's inputs refused; the v2 table of record declared, committed and accepted (PIN-V2-24); the declared adjudication-reads file, its entries `[stage, template, s]`. A Q-F0 or OLMo run given Q-F3's inputs is refused.
  - V2: the shared structure refusals (`_campaign_structure`: run_verdicts' V2 checkpoint-structure refusals, moved unchanged but for parameter names; the floors and gate-checkpoint checks stay in each reader); six-arm floors.
  - V3: `mf3.readrule.release_full` names the release.
  - V4: `_f3_check_record` STOPs on any record defect.
  - V5: the unit is NOT-RUN iff no session of any arm reached a first read (`f3_unit_state`).
  - V6–V7: per contrast arm the outcome, attained power, sentence, rates and tests, and the guard at the last look; per arm the beside block (`f3_beside_blocks`: m:308's whole-session validity and m:330's reported items, F3's pre-pick and the reasoning phase among the hair-trigger phases).
  - Outputs, write-once, in `data/mf3/verdicts`: `Q-F3_VERDICTS.json`, `Q-F3_secondary.json` (m:312 (a)–(f)) and `Q-F3_blind-read.json`, or `Q-F3_NOT-RUN.json`.
- **`posting --posting v2`** (`run_posting_v2`): a declared v2 tuple with f2's outcome a declared input recorded as given; cross-checks as PIN-23 with Q-F3's own outputs (`crosscheck_f3`); a v2 table (`table_problems(..., posting="v2")`), an of-record one only if it is the table Q-F3's VERDICTS (or its no-first-read NOT-RUN) read (PIN-V2-24, PIN-40 carried); outputs `POSTING-v2_outputs.{of-record,posted}.json`; C7's bar on the posted re-run, its comparator the v2 of-record output (`posting_comparator_v2`); the rewrite list carries `posting v2` (`rewrite_ids(..., posting="v2")`).
- **The v2 placeholder table** (`placeholder_table_v2`, file `data/m/gates/m_posting_sentences.placeholder-v2.json`): v1's 21 rows plus P22–P26 on Q-F3's cells A2 and A3, two of them carrying a thesis. The battery asserts the file is the builder's bytes.
- **The battery** (m:291 (ii)): every one of the 519,480 tuples asserted (`_bt_v2_pass`), the 300,625 full ones against an independent oracle (`_bt_oracle_v2`), checks V1–V12 per flag value. Aggregates hand-derived from the coordinate counts:
  - A3*: 30,000 × 3 / 10,000 / 40,000 × 2 / 120,000 / 625 (NOT-RUN);
  - ceiling: Main 375, Fallback-1 21,250, Fallback-2 279,000;
  - withholding and the v1-note's six values;
  - L1 75,000; §8.2 closed 1,875; Step 6 "none" 225,625;
  - each of the 26 rows' (a, b, c) fires (`PLACEHOLDER_FIRES_V2`) and (b)'s treatments by A3* (`BTREAT_V2`).
  - A second pass reproduces the outputs' sha256.
- **The one-round rule** (answers:26; the answers' A3): one hash-moving round, not two, and no in-place analyzer commit while an OLMo unit is open ("open" from its LOCK v0.1 to its VERDICTS entry). This round lands before any OLMo lock (order (a)); none exists, and after `6ce8b9a` (G-CAL-OLMo condition (4) failed on all three) one follows only if the seat's adjudication leaves a checkpoint to lock.

### A4 — the riding texts
- (1) The CLI-path reading: `_prod_committed` decides "outside the repository" from the resolved path, and `main` resolves every path argument against the repository root (`_cli_path`), ganl's `--out` included (an empty argument as before); `~` is expanded first, and a `~name` that names no user is refused (exit 2). A relative `--flag-source` now reads TRUE, as its absolute form does. The committed-blob check (`stages._committed`) is unchanged.
- (2) The Clock dates: `D1` (= `CLOCK_DATE`, 2026-10-30, unchanged), `D_O_PRIME` (2026-11-30) and `D2` (2026-12-22) are constants. `clock_problems` verifies D_O′ (A-m1:28) and D2 (A-m1:40) against ADDENDUM-m1, pinned by sha256 (`ADDENDUM_M1_SHA256`); `constants_by_line` checks D1 and D2 on m:16 in the battery, and the proposal's pinned sha256 (PIN-31) holds m:16 at every run. `_clock_refusal` runs at every `verdicts`, `not-run` and `posting` before an input is read. `clock_of_record` gives D1 for Q-F0, D_O′ for each OLMo checkpoint and D2 for Q-F3; `run_not_run`'s `date_is_clock_of_record` reads against it. The era rule (`pending_era`, PIN-V2-10) is N8's.
- (3) = A1.
- Round 2's misparaphrase rule: dated note N4.

### A5 — the eleven PIN readings
Each is built as the STOP's §3 wrote it, with the two notes applied:
- item 1's NULL sentence quotes the attained power at the realised n, with the planned-floor figure beside (`f3_sentence`, `F3_SENTENCE["null"]`);
- item 9 (2)'s dates are verified by sha256 at every run, and the D_O-era PENDING keeps its name (`pending_state`).

Ten of the eleven are declared among PIN-V2-1 to PIN-V2-24 (§2), beside the readings the build and the review added; item 10, round 2's rule, is a procedure, carried out as N4.

### B — the F3 build's flags
- **F-6** (applied to `valence_core/mf3`, on the coordinating session's "Apply B as written"):
  - G-TIME-F3's contrast sessions report no per-line list before VERDICTS (`readrule.strip_contrast`'s time form, `TIME_SESSION_KEYS`, `_contrast_block_time`).
  - The stage's line prints "CAP TRIGGER …: k of <= 36 reasoning lines reached the cap" (printed by `stages._finish_gate` from `stages.cap_trigger`'s report, which has no `lines` key).
  - A contrast session's per-line booleans and realised totals stay in the checkpoint. A sham session withholds nothing: each line's `cap_hit` is in the stage's reads file (`readrule.redact_sham`, `_LINE_KEEP`), and the report's sham block carries the counts. Code reads the seat's "in the report" as met by the reads file (Code's reading).
  - The module docstrings of `readrule.py` and `stages.py` say so.
- **F-7**: `guard.GID_CRITERION` is m's criterion plus "per reasoning line, an identical (n_tok, cap_hit, stop_reason) triple". In `stages._gid_pair`, `identical` requires both. A transcript-identical pair with a differing triple is a G-ID fire (FAIL; Q-F3 uncached). `stages`' self-test asserts the triple-only divergence FAILs. The seat PIN is set at LOCK-m-F3 v0.1, before G-ID-F3 runs.
- **F-1 to F-5** and finding 3 need no build change at this step: F-5's `scripts/mf3_gpwr.py` comes at its step.

## 2. The PIN register (`PINS_F3`; the battery asserts site ↔ entry exactly)
PIN-V2-1 to PIN-V2-24. Each is Code's reading, declared at LOCK-m-F3 v0.1, listed as a flag in the BUILD entry and strikable by the seat until LOCK-m-F3 v1.0 (answers:50). The cost of striking one: the analyzer's sha256 moves, G-ANL-F3 is rebuilt and re-run and its artifact superseded, and after LOCK-m-F3 v0.1 a hash that lock names moves too. Each entry's text is in `PINS_F3`, and each has at least one site, a `# PIN (Code, declared at LOCK-m-F3 v0.1 …): PIN-V2-n --` comment (PIN-V2-9 two):

| PIN | Subject |
|---|---|
| V2-1 | A3's NO-READ sub-reason; arm grain vs unit grain |
| V2-2 | the power figure of record per Q-F3 arm |
| V2-3 | the labels of cells A2 and A3 (Step 3) |
| V2-4 | the v2 sentence table |
| V2-5 | A3*, the withholding value, the v1-note; Q-F3 NOT-RUN's outputs |
| V2-6 | Step 6 rendered from m:342's own texts; "[stages]" and the power slot |
| V2-7 | §8.1 and §8.2 at v2; Step 7 |
| V2-8 | A-m1 §2.5 (1), the CLI paths |
| V2-9 | A-m1 §2.5 (2), the Clock dates |
| V2-10 | N8's era rule for PENDING |
| V2-11 | the regression's identity and the preprint of record |
| V2-12 | the Q-F3 reader's V1 (the Q-F3 closure; the posted v1 precondition; Q-F0's inputs refused) |
| V2-13 | counter (c)'s scorer (punctuation replaced by a space) |
| V2-14 | the blind-read draw (seed 20261106; staged adjudication reads) |
| V2-15 | the shared V2 helper; Q-F3's V4 |
| V2-16 | the Q-F3 arm sentence |
| V2-17 | valid-through at F3; Q-F3's secondaries |
| V2-18 | Q-F3's counters |
| V2-19 | Q-F3's NOT-RUN causes |
| V2-20 | `not-run` for Q-F3 and `--v2-closure` (`--campaign` required: the committed checkpoint, or `none` only while none exists; no campaign session) |
| V2-21 | `posting --posting v2` |
| V2-22 | the v2 enumeration's (b) treatment by A3* |
| V2-23 | the G-ANL-F3 artifact and PIN-39's widened commit check |
| V2-24 | the v2 table of record bound at Q-F3's VERDICTS (PIN-40 carried) |

The seat's rulings are recorded beside, as `SEAT_RULED_F3` (A1–A5). The two PIN-29 sites carry the seat's marker ("the seat's A1, 2026-11-06; acknowledged by the PI").

## 3. Dated notes and FLAGs, 2026-11-06 (the e9b5022 precedent; N1, N9, N10, N12 and N13 are FLAGs for the seat)

- **N1. The preprint of record.**
  - `PREPRINT-v1_0-draft.md` at HEAD carries the note release's status banner since `32aefcc` (sha256 `5d677a72…4467`; the banner says the file is not a text of record).
  - The table of record (`data/m/gates/m_posting_sentences.json`) binds its preprint by sha256, bytes and lines (`45b67246…7a41`, 88,668, 468). LOCK-m-F0 names that sha256 (PIN-40).
  - `table_problems` reads the file at HEAD, so at HEAD it refuses the table of record.
  - The regression serves the preprint of record by its committed blob (`git cat-file blob 1523cce:PREPRINT-v1_0-draft.md`, asserted to the table's sha256). This is Code's reading (PIN-V2-11), by analogy with the seat's A1 on the analyzer blob ("no blob but `655e0f7f…` can satisfy LOCK-m-F0's binding"): no preprint blob but 1523cce's can satisfy the table's binding.
  - With it, both outputs reproduce byte for byte. Without it the in-process run refuses before computing anything.
  - **FLAG, not adjudicated, outside G-ANL-F3's scope:** at HEAD, the v1 `posting` command over the table of record refuses on either analyzer ("the preprint's sha256 / bytes / lines differ from the table's"), as would any re-run of Q-F0's `verdicts`. No analyzer change is made for it (A-m1 §2.5: "No other change to the analyzer is licensed"; the answers' A4: "Nothing else rides").
  - With the three OLMo checkpoints NOT-RUN "dose not completable" on the record at `6ce8b9a` (G-CAL-OLMo condition (4); escalated to the seat; which NOT-RUN records and posting text follow is the seat's and the PI's), the v1 posting (A-m1 §4 step 6) is the next step after the OLMo track once those records exist, and this flag blocks it.
  - Which fix to make (for example, restoring the preprint of record's bytes in the tree for the posting) is the seat's or the PI's call.
- **N2. `QF3_WORDS["A3*"]`.** The analyzer of record listed nine values, POSITIVE and REVERSE among them. It now lists m:340's seven, as the STOP's §3 item 3 (corrected by its values-check, not struck) has it. On the verdicts and not-run paths the list is read only for a decision naming Q-F3's other_state; the G-ANL-F3 manifest also records it. Q-F0's decisions file is empty, so the regression is unaffected.
- **N3. G-SHAPE-F3 re-runs before LOCK-m-F3 v0.1.** B's mf3 edits move mf3's package hash (`readrule.py`, `stages.py` and `guard.py` are in G-SHAPE-F3's sources map). This is the referent check's N3, as amended by its values-check. The re-run is not G-ANL-F3's.
- **N4. Round 2's rule (A4 (iii)).**
  - The search: `git grep -i misparaphras` over `results/raw`, `RESULTS.md` and `LOCK-m-*.md`, and `git grep -i paraphrase` over the raws of 2026-10-15 onward, restricted to lines naming PINs, the analyzer or m_analyze.
  - It found no misparaphrase of the seat's rulings flagged in the analyzer's PIN texts. Under round 2's rule, the paraphrases were accepted as the entry listed them.
  - The candidates seen, and why none qualifies:
    - FID-3 and FID-6 of `results/raw/2026-10-15_m-analyzer-round2-step15_review.txt` were recorded "for v1.0's notes". FID-6 concerns SEAT_ROUTED's paraphrases, which round 2 accepted as listed.
    - The stale texts the LOCK-m-F0 v0.1 entry lists (`RESULTS.md@54bbfe5:4290–4305`: the battery labels "Code's guard for the seat's C9(ii)"; "flagged" on accepted items), whose correction it leaves open; Code read the like texts in PIN-9 and PIN-10 as not misparaphrases at the R2 3 analyzer round of 2026-10-14 (`RESULTS.md@54bbfe5:2569–2575`).
  - Under the answers' A4 ("Nothing else rides"), none is changed. The search is not a completeness proof.
- **N5. Behaviour kept for v1 by construction.**
  - `table_problems`, `rewrite_ids` and `crosscheck_coordinate` take a `posting` / `v2` keyword whose default is v1's behaviour.
  - `run_verdicts`' V2 checkpoint-structure refusals moved into `_campaign_structure` unchanged but for parameter names; the floors and gate-checkpoint checks stay in `run_verdicts`, unchanged.
  - `main` calls `production_env()` with no argument for every unit but Q-F3.
  - The base closure is unchanged: `a3bc7bb9…b22b`, recomputed on the build. The battery's v1 groups, the regression and the v1-unchanged check pass.
- **N6. The Q-F3 VERDICTS precondition.** "The Q-F3 VERDICTS session … runs only after the `POSTING v1` entry exists" (A-m1:40) is enforced as the v1 posting's re-run on the posted text, `POSTING-v1_outputs.posted.json`, committed at HEAD with schema `m-posting-v1-outputs-v1`, posting v1, table kind posted and C7's bar PASS (PIN-V2-12): the of-record output alone is written before the PI's rewrites, and a FAIL writes nothing. The analyzer cannot see entries. With N1 open, the v1 posting cannot complete at HEAD, so Q-F3's VERDICTS path waits on N1 too.
- **N7. f2.** f2's outcome and its control are declared inputs of the v2 tuple, recorded as given. No f2 output exists to cross-check: f2 is a future pre-registration (m:340).
- **N8. The blind read's agreement.** The analyzer writes the draw and the rule's key. The agreement between the seat's scores and the rule (m:312) is computed at the Q-F3 VERDICTS entry; no command for it is built.
- **N9. FLAG, not adjudicated: with this analyzer, `scripts/m_sessions.py --selftest` fails one case that it passes without it.**
  - The counts: 845/846 on the build's first base (`273ca8f`). On the commit's base (`e7e070f`), 843/846 with this analyzer and 844/846 without it; N12's two cases fail either way.
  - The failing check is "time --unit Q-F0 on the Qwen path (main, no factory) refuses with exit 2 … in 31 cases". In one case, "a lock-named non-proposal", the driver is given `scripts/m_analyze.py` as its "proposal", a committed file LOCK-m-F0 names (`scripts/m_sessions.py`'s self-test). The case expects the refusal "startup: banner".
  - The extended analyzer's sha256 is not in LOCK-m-F0's text: LOCK-m-F0 binds the analyzer of record, `655e0f7f…`. So the driver refuses earlier, on lock §1's proposal binding applied to the file passed as `--proposal-file` ("…: its sha256 … is not named in full in LOCK-m-F0.md's committed text (lock §1 binds the proposal of record)").
  - Code's reading: the driver's behaviour is right -- it refuses a `--proposal-file` whose sha256 LOCK-m-F0's committed text does not name in full, and the extended analyzer's is not named there; Q-F0's stages are finished. What moved is the test case's premise. Any in-place G-ANL-F3 commit moves it, under order (a) or (b).
  - A fix (another lock-named non-proposal file in the case) changes `scripts/m_sessions.py`, a TOOLING_FILES entry. The step-10 read's Q2 clears only a subcommand-wiring edit, so under PIN-S10 ("any difference re-runs G-SHAPE-F0 first", `valence_core/m/gshape.py:233–236`) the change re-runs G-SHAPE-F0. Whether and when to make it is the seat's call; nothing is changed here.
  - The PI's ruling of 2026-11-06, in chat, relayed: to the coordinating session's question "Commit G-ANL-F3 with the self-test case flagged for the seat?", "Commit with flag". The question was put on the 845/846 count; the case this analyzer moves is the same one on either base.
  - The other nine suites of the site check pass (the site-check raw).

- **N10. FLAG, not adjudicated: m:312's nearest-term rule on a natural attribution.** Counter (c)'s rule, as m:312 writes it and the scorer applies it, scores "prism is clean, slate is corrupted" ambiguous: slate's nearest polarity term is "clean", one token back, so both labels take the positive polarity. The battery records the case (F3C-SCORER). The rule is m:312's, not Code's; whether to revise it before LOCK-m-F3 v0.1 freezes the lexicons (m:292) is the seat's call. (Found by the blind code review.)

- **N11. `data/mf3/verdicts/*.json` is ignored.** `.gitignore`'s `/data/mf3/*` (line 273) has no admit line for `verdicts/`, so `git check-ignore` matches `Q-F3_VERDICTS.json` and `Q-F3_NOT-RUN.json`. The v2 posting now reads them for the table binding (PIN-V2-24). The commit that first writes them needs an admit block, as PIN-25's practice has it for data/m. `data/m/gates/*.json` is admitted, so the v2 placeholder and G-ANL-F3.json commit as they are. (Found by the follow-up review.)

- **N12. FLAG, not adjudicated: two G-CAL-OLMo cases of `scripts/m_sessions.py --selftest` fail at HEAD, without this build.** (Found by the site check.)
  - At `e7e070f`, m_sessions' self-test with the analyzer of record is 844/846 (Code's run in a second scratch worktree; the site-check raw's last sections). The two FAILs:
    - gcal's own self-test case "gcal-olmo: a non-stub precheck without the pod id is refused (POD ID ABSENT, no laptop checklist on OLMo); …", in `valence_core/m/gcal.py`;
    - "m_sessions-olmo: gcal completability --unit OLMo-sft on the stub writes G-CAL_completability_olmo-sft.json …; on the box path without the pod id or the weights it is refused before any load (exit 2) naming both", in `scripts/m_sessions.py`.
  - Each reaches the G-CAL precheck on the canonical paths with the pod id unset, and expects its refusal before any load: the pod id's, and in the driver's case the weights' too. `6ce8b9a` committed G-CAL-OLMo's checkpoints (`data/m/ckpt/G-CAL_olmo-{sft,dpo,instruct}.json`), so the precheck now refuses first: "CHECKPOINT EXISTS at …/data/m/ckpt/G-CAL_olmo-sft.json" (and `…olmo-instruct.json`; Code's probe, in the site-check raw). On `273ca8f`, before that commit, both pass.
  - This build touches neither file nor those paths. As with N9, the cases' premise moved, here with the G-CAL-OLMo commit. A fix to the first edits m's package (`valence_core/m/*.py`, sha256 `60199b36…feec`), and a fix to the second edits a TOOLING_FILES entry, as N9's fix would. Both are the seat's call; nothing is changed here.

- **N13. FLAG, not adjudicated: `--campaign none` beside a set-aside campaign checkpoint.** (Found by the values-check's fourth pass, its NOTE A'1.)
  - After a box change, `resume._set_aside` renames a checkpoint to `{name}.podchange-{stamp}` and never deletes it (`valence_core/m/resume.py:840–848`). The `none` check (PIN-V2-20) looks only for `data/m/ckpt/{U}_campaign.json`, in the tree and at HEAD. So it passes when only a set-aside exists, whatever sessions the set-aside records.
  - Code's reading: the respawn protocol's consistency clause (CLAUDE.md:127–130: "a mid-campaign box change aborts and restarts the campaign on the new backend; campaigns are never spliced across backends") puts a set-aside's sessions outside the campaign of record. A unit whose only campaign checkpoint is a set-aside therefore has no session in m:324's sense, and `none` is a true declaration.
  - If the seat reads it otherwise, the fix refuses `none` beside a set-aside. That moves the analyzer's bytes, a second hash-moving round, which is the seat's to authorize. No change is made here.

## 4. Counts and runs (Code's scratch worktree at `e7e070f`, the five files byte-identical to the commit's; the raws beside this one are verbatim, paths scrubbed)
- The analyzer battery: 525/525 checks. All 538 coverage ids are reached; at G-ANL-F0 there were 448 checks and 461 ids. `EXPECTED_CHECKS` = 525.
- The base closure is `a3bc7bb9…b22b` (unchanged). The Q-F3 closure is `d19f336d…f039`: 22 modules, the base's 15 plus seven mf3 modules (`__init__`, `banner`, `keys`, `lines`, `readrule`, `scaffold`, `schedule`). m's package_sha256 is `60199b36…feec` (unchanged).
- mf3's module self-tests: 124/124 over thirteen modules (`testing`, a helper, has none). The ten-suite site check: nine suites pass, and m_sessions is 843/846 (N9's case and N12's two; 844/846 at HEAD without this build). See the site-check raw.

## 5. Changes made on the blind code review (its raw holds the report and Code's dispositions)
- **Finding 1** (the decision-(10′) guard): V1 now requires the v1 posting's re-run on the posted text, committed and PASSing C7's bar, not the of-record output's presence (N6; PIN-V2-12).
- **Finding 2** (nothing bound the v2 table of record): `verdicts --unit Q-F3` takes the v2 table of record as a required, committed input and records it; the v2 posting refuses an of-record table other than the one Q-F3's VERDICTS or no-first-read NOT-RUN read (PIN-V2-24, PIN-40 carried).
- **Finding 3** (adjudication reads without a stage): entries are `[stage, template, s]`; only campaign entries exclude a session from the draw (PIN-V2-14).
- **Finding 4** (the v2 closure's "no session" unchecked): `--v2-closure` refuses a checkpoint whose campaign records a session (read for the count alone; `--campaign` names it, by default `data/m/ckpt/{U}_campaign.json`) (PIN-V2-20).
- **Finding 5** (the tokenizer joined words): Unicode punctuation is replaced by a space, not deleted; the reviewer's cases are in F3C-SCORER; its observation on m:312's rule is N10 (PIN-V2-13).
- **NOTE 6** (the oracle's Step 6 shared the implementation's strings): Step 6 renders m:342's own texts (`S6_*`, each checked on m:342 by `constants_by_line`), and the oracle reads m:342 from the proposal at run time (`_bt_m342`). Three texts changed with it: FAIL now reads m:342's "scoped at this scaffolding and stimulus strength", REVERSE carries m:342's parenthesis, and the NULL clause's power slot takes m:342's dash ("… for the realised n — f2's" or "— the screen's") (PIN-V2-6).
- **NOTE 7** (stale texts): PIN-29's register text names the exception and the mf3 roots; the artifact's g_anl_f3 block records the unlocked sub-state by era, Q-F3's gate-stop stages and its counters; `pending_state`'s message names both eras' unlocked sub-states. Two items are kept, disclosed: the era boundary (PIN-V2-10: the commit day counts as D_O′'s); and COUNTERS (the manifest's counters field), which stays Q-F0's declarations, unchanged, with Q-F3's in the block (`counters_q_f3`).
- **NOTE 8** (CLI loose ends): ganl's `--out` resolves against the repository root; each reader refuses the other's inputs; the help texts name G-ANL-F3 and v2.
- **NOTE 9**: PIN-V2-21 states that the v2 posting's binding records the base closure; the manifest check recomputes the Q-F3 closure's sha256; F3V-DETERMINISM's text counts the 601,250 non-PENDING evaluations its sha covers.
- **NOTE 10** (N1 confirmed): no change; with finding 1's guard, Q-F3's VERDICTS path also waits on N1 (N6).
- **The follow-up review** (on the fixes; no MAJOR or MINOR, four NOTEs):
  - NOTE 1 (a quoted `~/x` would land inside the repository): `_cli_path` expands `~` first.
  - NOTE 2 (`--v2-closure` read an absent file as no session; `--campaign` unchecked; one message for two reasons): `--campaign` is required with the flag, as the unit's campaign checkpoint (identity unit and stage checked; refused if it records a session) or `none`, declared and recorded. A malformed or another unit's file is refused with one identity message, apart from the sessions refusal, and an absent path as unreadable (PIN-V2-20). The suggestion's other half (the file committed; `none` checked against the tree) was completed on the third pass's NOTE A1, below.
  - NOTE 3 (F3R-READER-REFUSALS asserted only a refusal): each case's reason is asserted.
  - NOTE 4 (`.gitignore` ignores `data/mf3/verdicts/*.json`): dated note N11; no change here.
- **The values-check's third pass** (its review of the last code delta; no MAJOR or MINOR, four NOTEs and one observation, all applied):
  - A1 (`--campaign none`, and any identity-matching file, were taken on the operator's word): `none` is refused while `data/m/ckpt/{U}_campaign.json` exists in the tree or at HEAD (`Env.head_has`; in production `git cat-file -e HEAD:<rel>`), and a passed checkpoint must be committed at HEAD, its bytes as read equal to HEAD's blob (PIN-V2-20). F3N-V2-CLOSURE gains four cases (c13–c16).
  - A2 (the campaign file was read twice): it is read once, and the check, the parse and the recorded sha256 use the same bytes; an absent file is a refusal (exit 2), never a traceback.
  - A3 (a `~name` that names no user raised RuntimeError, exit 1): `_cli_path` refuses it (exit 2), and `main` resolves ganl's `--out` inside its try; F3R-CLI-PATHS asserts exit 2 from `ganl` and `not-run` (PIN-V2-8).
  - A4 (the module docstring's usage line lacked `--campaign`): it reads `[--v2-closure --campaign P|none]`.
  - The observation (PIN-V2-12's site comment still described the guard as it was before finding 1's fix): it now reads as the code does.
  - The battery's check count and coverage ids are unchanged (525 checks; 538 ids): the new cases are sub-cases of existing checks.
- **The fourth pass** (the third pass's agent on those fixes; no MAJOR or MINOR, two NOTEs; its seven text items confirmed):
  - A'1 (the `none` check does not look for a `.podchange-*` set-aside): N13, a FLAG for the seat; no change.
  - A'2 (F3R-CLI-PATHS's `main(["ganl", "--out", "~nosuchuser_zz9_m/x"])` would run the battery inside the battery, and recurse instead of failing, if a later edit let `_cli_path` accept that argument): disclosed, no change. Any later edit to `_cli_path` should first stub `run_ganl` in that check.
