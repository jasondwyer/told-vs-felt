# PROPOSAL-m v1.11 §8 steps 7-8 -- the build inputs the G-SHAPE-F0 and G-ANL-F0 tools were built from (rule 27: the PINs and build raws cite them).

Compiled by Code 2026-10-10 11:44:12 UTC (date -u). Verbatim copies of Code's scratch files. Precedence for each build: Code's decisions > the critic's corrections for that gate > the build spec > the readers' reports. The readers' five reports are not reproduced; the specs synthesize them and cite their checks.


---

## FILE: decisions_gshape.md (sha256 bc5129aae5fea4f59b2bbfd1bb3d66d20b511ee8ff13dbb12e63bef4e787f7f6)

# Code's decisions for the G-SHAPE-F0 build (step 7) — these override spec_gshape.md where they differ

Precedence: this file > critic.md's G-SHAPE items > spec_gshape.md > readers' reports. m:277 is the governing text.

1. **Layers in the artifact of record: A, C (trimmed), S. Layer B is dropped.**
   - Layer A: m:277's placements, as spec §5 (PIN-S1, PIN-S2), through each substrate's classifier stack; fire predicate PIN-S3 (strictest: any ROUND_FIRE_FIELDS field).
   - Layer S: the static check of the four production classify call sites and `SessionLog.add_round` (spec §8), in the artifact. It must be mutation-sensitive (the self-test proves each scope mutation is caught).
   - Layer C: trimmed to ONE scope-widened control scorer per substrate (seg+gold), which must fire on 100% of its placements, else STOP. Render-as-response stays a reported-only figure.
   - Layer B (real runners on doubles) is dropped from the artifact AND from the self-test. The entry names the existing runner self-test checks that exercise classify on generated text as the dynamic evidence; find them and cite them by check name. If, and only if, no existing check asserts that the runners hand classify the generation text (not the segment, banner or render), add exactly ONE dynamic self-test check for that, and say so in the build report.
2. **Renders**: read the 16 from the committed `data/m/gates/G-CAL_model-free.json`; assert they equal `scaffold.pool_and_renders()`'s and that their sha256 is `a04f67b0e5105a0514a0f33e64a4545ef3a3a3c75cece320d78434e853cd4372` (also the completability identity's and the seat read's cited line); STOP on any mismatch. Cite the "never computed as G-SHAPE's own" record as RESULTS.md@e60b633:919–920.
3. **OLMo**: one computation run per checkpoint on byte-identical inputs. Record per-unit rows AND `olmo_grids_identical: true` (digest of the rows with the unit stripped, equal across the three), STOP if not. The only per-checkpoint input is the `data/olmo/scaffold_{ckpt}.json` string check; the ban-id half is checked on the box (LOCK-m-OLMo-{ckpt} v0.1, m:302) — record it as not exercised here.
4. **Preconditions**: refuse (exit 2, nothing written) unless every file in SCORING_STACK_FILES and TOOLING_FILES is committed at HEAD and identical in the working tree. Add the three b3_screen files to the sources map.
5. **Self-test** prints `package_sha256` and the digest of the SCORING_STACK_FILES/TOOLING_FILES sources map in its check note, so the run of record pairs with a self-test pass from the raws alone.
6. **No `__init__.py` edit.** Register gshape in the self-test the way the existing modules are (`"gshape" in MODULES` or the equivalent), so the valence_core/m diff for step 7 is `gshape.py` alone.
7. **Write-once and supersession**: the artifact `data/m/gates/G-SHAPE-F0.json` is write-once (gcal/gport conventions: never overwritten with different bytes; no timestamp; no HEAD in the artifact). Declare in a PIN and the build report: on the seat's ruling only, an artifact is moved by hand (`git mv`) to a dated superseded name recorded in an entry, and the re-run writes the canonical name. A re-run on unchanged inputs is byte-identical.
8. Exit codes: 0 PASS (written or identical), 2 refusal, 4 STOP (a fire, a coverage gap, a silent control, a shape failure, a Layer-S problem: artifact written with evidence; precondition STOPs: no artifact). Code escalates; never self-adjudicates.
9. Everything else as spec_gshape.md states (PIN-S1..S12 minus those replaced above).

Hard rules for every agent: no model or tokenizer loads (no mlx/mlx_lm/torch/transformers imports at runtime of the gate or self-test beyond what the existing m self-test already does); no git commits, adds, stashes or checkouts; never git inside jlens-qwen36/; never touch scripts/audit_note_*, results/raw/*note-*, README-NOTE.md, RESEARCH-NOTE-*, AUDIT-note-*, LICENS*, *.svg at the root (a parallel session's work); never write under data/m/ except through a temp-dir test path (the canonical run of record is Code's, after the build commit); mutation probes only on scratch copies, never in the repo tree; the Bash tool's grep is ugrep — use /usr/bin/grep; scratch under /private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step7/ . The G-ANL-F0 build (scripts/m_analyze.py) runs concurrently in the same tree: do not touch scripts/m_analyze.py or data/m/gates/m_posting_sentences*.

## Round-2 additions (Code, after the first verification)
10. Confirmed: the committed-sources refusal binds the canonical run only; `--out` runs skip it and say so (gcal's precedent).
11. Extend the canonical run's committed-sources precondition to EVERY file of the m package (`valence_core/m/*.py`, the files `package_sha256` covers), in addition to SCORING_STACK_FILES and TOOLING_FILES: the run of record must not record a package hash of an uncommitted tree.
12. Close the verifier's residual defects 1–6 (the self-test must pass pre-commit when any scoring-stack file has an uncommitted edit; a single-field fire check, e.g. a termination-only scorer; no negative test may be able to write the real `data/m/gates` — route them through temp canonical dirs; artifact `inputs`/`stacks` values checked; must-fail cases for the listed input checks and `score()`'s item argument; wrap every self-test `write()` so one failure cannot hide the rest), and its non-equivalent mutation survivors.


---

## FILE: decisions_ganl.md (sha256 df948d1e560e3ede6ce581b6fc5e94238ebe207d1018bc8e4720abd5cef2108a)

# Code's decisions for the G-ANL-F0 build (step 8) — these override spec_ganl.md where they differ

Precedence: this file > critic.md's G-ANL items > spec_ganl.md > readers' reports. m:278 is the governing text, with §4, §5, §7 and the lines they cite.

1. **Home (PIN-1, reworded per the critic).** All verdict logic lives in `scripts/m_analyze.py`; step 8 edits nothing under `valence_core/`. The PIN reads: "the analyzer's sha256, package_sha256 and the import closure outside the package together bind the verdict logic". Compute the closure mechanically after import (sha256 of `__file__` for every loaded `valence_core.*` module outside `valence_core/m`, plus every data file the verdict path opens); record it in the G-ANL-F0 artifact; refuse (exit 2) a verdict run whose closure differs from the one passed/declared (the lock's, later). Import `stages`/`testing` lazily where only the battery or gate-line helpers need them, to shrink the closure.
2. **Seat-routed defaults (blocking LOCK v0.1, NOT step 8).** Build the conservative default now for each, mark it with a PIN that says it awaits the seat's ruling before LOCK v0.1 hashes the analyzer, and list it in the build report:
   - PIN-8: a campaign ended by a scaffold_absorption hair-trigger STOP is refused unless a declared PI-stop record (path + sha256 recorded) names it; with it, m:324's PI-stop rule applies.
   - PIN-9: VERDICTS refuses while the last pause is unadjudicated; the seat's adjudication enters as a declared `--adjudication` file (path + sha256 recorded). Code never self-adjudicates. Flag the build gap (no recording path in stages.py) in the report.
   - PIN-17: §8.1 at v1 covers the controls with a v1 coordinate (A0, A0-OLMo-sft/-dpo/-instruct); A1 belongs to §8.2, "open" at v1.
   - Also seat (non-blocking for step 8): the Clock boundary-day comparison (declared input `clock_passed` + date, recorded); the f1 7-vs-1 reference column (interim PIN-12 adds `sessions_excluded_any_phase` beside the pre-pick column); analyzer versioning for G-ANL-F3 (PIN-14); the posting re-run's pass bar.
3. **Secondaries now (PIN-13)**, in m_analyze.py, output to a separate `{unit}_secondary.json`; secondary (d) uses `habit.break_rates(<the arm's domain sessions>)` (no `arm` key), reports the weighted-form identity beside Δ_c, omits frame()'s e2d powered-effect block; recompute b+, bs and the weighted form in Fractions; battery check (both directions) that weighted form + ½ reproduces the arm's P exactly on crafted records.
4. **Power (PIN-3)**: the figure of record is m:190's base case at the realised n — the arm at n/2 per map (odd n: ⌊n/2⌋ and ⌈n/2⌉, declared), the sham pooled; report the realised-split figure beside it, labelled. Descriptive only.
5. **m:318 decisions input**: a required declared input `decisions_with_other_outcomes_known: [{decision, date, other_unit, other_state}]` (may be empty), emitted in `{U}_NOT-RUN.json` and `{U}_VERDICTS.json`; battery: non-empty carried verbatim, missing key refused.
6. **Guard at the last look (PIN-10, trimmed)**: no end-of-data recomputation. For a STOP-ended campaign the sentence names the last cadence look as the last look, and the missing end look on STOP is flagged to the seat as a build gap (not patched in the analyzer).
7. **Counters**: pre-pick rates via `stages._prepick` (or the identical definition, cited) so the sentence and the guard share one denominator; battery check (both directions) that the analyzer's counters summed over property equal `audit.tally` on the same records.
8. **Defer** the `.gitignore` block for `data/m/verdicts/` (and any `-diff`) to the commit that first writes there. Drop the roster-word refusal on sentence-table text (keep the forbidden-literal check).
9. **The 0.12-artifact flag (PIN-19)**: TRUE iff `data/m/gates/G-CAL_model-free.json` is committed at HEAD and identical in the working tree, has schema `m-gcal-model-free-v1`, and has an `f1_012` block; record `renders_sha_matches_calib` beside the flag (not part of it). Cite m:349's "iff" as PIN-21's basis.
10. **Signed numbers**: print as sign + `_dec(|x|)` (or an equivalent signed helper), half-up on the magnitude, declared; battery: −1/20 → "-0.0500", +1/20 → "+0.0500".
11. **VERDICTS tree rule (PIN-14)**: when HEAD's analyzer sha, package_sha256 and closure equal the lock's, VERDICTS runs at HEAD with no worktree; otherwise from a worktree with every data input/output passed as an absolute path into the main tree, and only on the PI's word for the worktree. Declare it; do not implement worktree creation now.
12. **Artifacts**: `data/m/gates/G-ANL-F0.json` (write-once manifest: analyzer, placeholder and proposal shas, closure, battery counts, coverage, tallies, outputs_sha256, flag of record, counters, vocabularies, PINs; no timestamp; no HEAD) and `data/m/gates/m_posting_sentences.placeholder.json` (synthetic placeholder, PIN-20). The 2,160-row output table is not committed (regenerates byte-identically from its recorded sha). Supersession as G-SHAPE's: on the seat's ruling only, `git mv` to a dated superseded name recorded in an entry; a re-run on unchanged inputs is byte-identical.
13. **Raws** for Code's commit: `results/raw/<date>_m-ganl-f0-build_review.txt` and `_sitecheck.txt` (Code produces them; the site check adds the m_analyze suite to the eight).
14. The analyzer reads no checkpoint or contrast pick in step 8 (synthetic battery only); blinding m:318 governs every later read.
15. Everything else as spec_ganl.md states.

Hard rules for every agent: no model or tokenizer loads; no git commits, adds, stashes, checkouts or worktrees; never git inside jlens-qwen36/; never touch scripts/audit_note_*, results/raw/*note-*, README-NOTE.md, RESEARCH-NOTE-*, AUDIT-note-*, LICENS*, root *.svg (a parallel session's work); edit nothing under valence_core/ and do not edit scripts/m_sessions.py (the G-SHAPE-F0 build edits it concurrently); never write under data/m/ except the placeholder file and temp-dir test paths (the G-ANL-F0 manifest of record is Code's, after the build commit); mutation probes only on scratch copies, never in the repo tree; the Bash tool's grep is ugrep — use /usr/bin/grep; scratch under /private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step8/ .


---

## FILE: critic.md (sha256 1cbfc119a8b98ac14f7d6bde8bbcd481695e5ef22d69d38b36324a08d46c21a6)

### [G-ANL-F0: PIN-1, §1 imports, §5 V1, §14 `sources`. Also a LOCK-m-F0 v0.1 / v1.0 hazard.] PIN-1 says the hash of the single file binds the verdict logic. It does not. The analyzer imports `stages`, `guard` and `audit` at module level, and through them the whole m package plus at least 11 files outside the package. §14 records only 2 of those outside files, and V1 at VERDICTS checks only the analyzer sha and package_sha256. An edit to an imported file outside the package after the lock would change VERDICTS while every pinned hash stays the same.
EVIDENCE: [S] m:279 has LOCK v0.1 pin the "analyzer hash and the placeholder sentence table's hash". m:286 has LOCK v1.0 hash "the analyzer". m:318: "VERDICTS are computed by the pre-committed analyzer".

[C] Read in the code (no import run):
- stages.py:120-129 imports bars, banner, corr, guard, keys, readrule, resume, scaffold, schedule, verify, runner_olmo and runner_qwen.
- runner_qwen.py:54-57 imports e2d.config, e2d.runner, session and session_e2a.
- guard.py:72-73 imports readout and session.
- audit.py:50-53 imports e2d.config, contentclass_v5, audit_v3 and session.
- session.py:38 imports stats.
- e2d/runner.py:42-48 imports readout, session, session_e2a and config.
- readout.py:33 imports adapters.base.
- contentclass_v4 imports contentclass.

[I] So the closure outside the package is at least: session.py, stats.py, readout.py, session_e2a.py, adapters/base.py, e2d/{config,runner,audit_v3,contentclass,contentclass_v4,contentclass_v5,habit}.py. §14 lists only session.py and e2d/habit.py.
CORRECTION: Reword PIN-1: "the analyzer's sha256, package_sha256 and the import closure outside the package together bind the verdict logic".
- Compute the closure mechanically after import: sha256 of `__file__` for every loaded `valence_core.*` module outside valence_core/m, plus every data file the verdict path opens.
- Record it in G-ANL-F0.json and carry it in LOCK v0.1 and in each LOCK v1.0.
- Add a V1 refusal (exit 2) when it differs.
- Optional: import stages and testing lazily. They are needed only for gate_line, _committed, _bar_set, STUB_MARK and _ROSTER_RX, and for the battery's C3 writers, so a lazy import shrinks the closure.

Route: PIN (Code). Do this at step 8; it does not need the seat.

### [G-ANL-F0: OPEN routing for PIN-8, PIN-9 and PIN-17. Also a LOCK-m-F0 v0.1 hazard.] Three questions whose answers would change m_analyze.py are marked non-blocking, and two of them are routed as Code PINs. LOCK v0.1 freezes the analyzer hash. So a seat ruling after the lock forces a new analyzer, a new battery run, and a new G-ANL-F0.json, which its write-once rule refuses.
EVIDENCE: [S] m:279: LOCK v0.1 carries the "analyzer hash". m:278: "`m_analyze.py`, pre-committed".

[S] PIN-9 (whether VERDICTS may be computed over an unadjudicated last pause) sits between two texts:
- m:330: "A fired bar pauses; Code never self-adjudicates"; "pauses are not verdicts";
- m:316: "a fire pauses that unit for adjudication and never changes a verdict".

[S] PIN-17 (does §8.1 at v1 cover A1?):
- m:326 opens "Positive controls (A0, A0-OLMo-{ckpt}, A1)";
- m:343: "§8.1's sentences state each control's outcome (PASS / DEAD / REVERSE / INDETERMINATE / not run / pending)".

[I] PIN-8 (hair-trigger STOP) is routed SEAT but marked blocking:false, although the spec itself says the seat must confirm it "before LOCK v0.1 hashes the analyzer".
CORRECTION: Re-route two questions from PIN to SEAT:
- PIN-9's "may VERDICTS run while the last pause is unadjudicated";
- PIN-17's "does §8.1 at v1 carry A1 (as 'pending')".

Mark these two, and PIN-8, as "blocking LOCK v0.1, not step 8". Build the conservative defaults now.

Send all of them in ONE Code-to-seat block committed under results/raw before step 9, together with:
- G-SHAPE's PIN-S3, S5 and S6;
- G-CAL's owed items;
- the third order question.

This keeps them out of chat (the memory rule) and lets the seat rule before the hash is frozen.

### [G-ANL-F0: §8 secondary (d), PIN-13, PIN-2.] `habit.frame(domain sessions, arm)` cannot run on m records, and it is the wrong function for this use.
EVIDENCE: [C] habit.py:168 filters `s["arm"] == arm`. m session records carry `template`, not `arm` (scaffold.py:437-447), so the call raises KeyError.

[C] frame() embeds e2d-only constants: delta_first 0.15, a required b+−bs of 0.30, and an e2a base break rate of 1−156/187 (habit.py:171-179). It also returns floats, which contradicts PIN-2's "Floats are refused".

[S] m:312 asks only for "`e2d/habit.py`'s within-arm identity at F0m/F0m-OLMo".

[C] m records do carry the fields that `break_rates` reads:
- rounds[].pole and choices[].picked_pole, mapped through scaffold.ROLE_POLE {P: pos, Q: neg} (scaffold.py:64, :387, :406).
CORRECTION: Replace frame() with `habit.break_rates(<the arm's domain sessions>)`, which needs no `arm` key.
- Report its weighted-form identity beside the arm's Δ_c.
- Leave out frame()'s e2d powered-effect block.
- Either exempt these descriptive floats from PIN-2 explicitly, or recompute b+, bs and the weighted form in Fractions.
- Add a battery check, in both directions, that the weighted form + ½ reproduces the arm's P exactly on crafted records.

Route: PIN.

### [G-ANL-F0: PIN-3, attained power.] PIN-3 computes power at the realised per-map counts and says this "reproduces m:190". It does so only when the two maps are equal. m:190 states a different base case: an n/2 split per map. The two readings diverge on unbalanced or empty maps; with a map empty, PIN-3 gives 0.
EVIDENCE: [S] m:190: "base case … each arm split n/2 per map at clean share P in both maps, its sham split m/2 per map at .5". Also m:190: "Attained power at the realised n … is the power figure of record for the verdict sentences".

[C] Re-run exactly here:
- (48,48,32) gives .9161 and (40,40,32) gives .8784, matching m:190's .916 and .878 only because those splits are balanced.
- Under PIN-3, power is 0 whenever n0 = 0. Under m:190's split it is not.
CORRECTION: Make the power figure of record the m:190 base case at the realised n: the arm at n/2 per map, the sham pooled.
- Declare an odd-n rule, e.g. ⌊n/2⌋ and ⌈n/2⌉.
- Report the realised-split figure beside it, labelled.
- If Code prefers the realised split as the figure of record, PIN-3 must instead say it departs from m:190's stated base case.

Route: PIN. The figure is descriptive, so this needs no escalation.

### [G-ANL-F0: §4.2 NOT-RUN record schema, §5 V11 and the `not-run` command (m:318 and m:358 not covered).] Neither the NOT-RUN record nor the VERDICTS output has a field for the m:318 declaration about decisions taken with another unit's outcome known.
EVIDENCE: [S] m:318: "A decision about one unit taken after another unit's VERDICTS exist (an OLMo cap, a PI stop, a declined v1.0 after A0 is known) is permitted and **recorded in that unit's VERDICTS entry or NOT-RUN record**" as taken with that outcome known.

[S] m:358, step 17: each OLMo VERDICTS "recording any decision taken with another unit's outcome known".

[I] The spec's record is `{schema "m-not-run-v1", unit, cause, also[], date, detail}`. It has no such field, and the VERDICTS output has none either.
CORRECTION: Add a required declared input, `decisions_with_other_outcomes_known: [{decision, date, other_unit, other_state}]`, which may be an empty list.
- Emit it in {U}_NOT-RUN.json and {U}_VERDICTS.json.
- Battery: a non-empty case is carried verbatim, and a missing key is refused.

Route: PIN.

### [G-ANL-F0: OPEN routing and §16. Also consistency with G-SHAPE-F0 PIN-S10.] Three problems:
- (a) The G-CAL / steps-7-8 item is routed to the PI. It belongs to the seat.
- (b) The 'analyzer_sha256 optional' item is routed to the SEAT, but it is Code hardening its own tool.
- (c) G-ANL twice says any package edit forces G-SHAPE to re-run. That contradicts G-SHAPE PIN-S10, under which only edits to SCORING_STACK_FILES force a re-run.
EVIDENCE: [S] 2c50e03 entry: "Whether starting 7 and 8 before G-CAL closes is acceptable is for the seat to rule". Commit message: "a third order question for the seat". The PI's go ("Go for steps 7 and 8") is already on record.

[I] G-ANL says a stages.py change "must land before G-SHAPE-F0's run of record or force that run to repeat". §16 says G-SHAPE "would need a re-run under a new name". But stages.py is not in G-SHAPE's SCORING_STACK_FILES, and PIN-S10 says only a difference in the sources map re-runs G-SHAPE.

[C] stages.py:899 and :966-969: analyzer_sha256 is optional in identity_extra. This is Code's own wiring.
CORRECTION: Fix each:
- (a) Route to SEAT, non-blocking for step 8, consistent with G-SHAPE's last OPEN item.
- (b) Route as a PIN for the LOCK v0.1 build (step 9 wiring): require analyzer_sha256 and package_sha256 on non-stub runs, and list it in the lock.
- (c) Align with PIN-S10. A package edit outside SCORING_STACK_FILES does not re-run G-SHAPE. LOCK v0.1 states each gate artifact's package_sha256 and the mechanical diff between them.

### [G-ANL-F0: PIN-10's end-of-data guard; counters (§7) built as a second implementation.] Over-built, and at risk of disagreeing with the stage drivers:
- PIN-10 adds a guard result recomputed at analysis. The spec asks only for the guard "at that unit's last look".
- The analyzer re-implements both the pre-pick and counter logic that stages.campaign_look and audit.tally already compute, so stage reports and VERDICTS could disagree.
EVIDENCE: [S] m:326: the sentence states the rate "with the guard's result at that unit's last look". m:316: a fire "never changes a verdict". m:33: "an answer to a check first asks whether the mechanism it repairs is needed".

[C] stages.py:1851-1855 `_prepick` (forced-phase exclusion), and :1877-1906 campaign_look (Fisher plus the absolute guard over len(con) records).

[C] audit.py:547-603 `tally`, the rule-23 counters keyed without property.

[C] stages.py:2160-2171 already evaluates an end look for terminal campaigns. Only a STOP-ended campaign lacks one.
CORRECTION: Drop the end-of-data recomputation.
- For a STOP-ended campaign, the sentence says the last cadence look is the last look, and the missing end look on STOP is flagged to the seat as a build gap. It is not patched in the analyzer.
- Compute the pre-pick rates with stages._prepick, or the same definition, so the sentence and the guard share one denominator.
- Add a battery check that the analyzer's counters, summed over property, equal audit.tally on the same records, in both directions.

Route: PIN.

### [G-ANL-F0: §1 item 4, PIN-25 `.gitignore` block; §9.4 table refusals.] Over-built for step 8:
- The analyzer's `.gitignore` admit block for data/m/verdicts is written at step 8, but nothing writes there until step 17.
- The sentence-table validator refuses roster words. That refusal has no blinding role: a table carries no pick, and a gated preprint sentence may legitimately name a label.
EVIDENCE: [S] m:358: VERDICTS outputs first exist at step 17. CLAUDE.md memory: a parallel session shares the tree, so .gitignore is a shared file.

[C] .gitattributes puts `-diff` only on /data/m/ckpt/**. Whether VERDICTS JSON, which carries role-coded picks, needs the same is a question for the step that creates it.

[C] PREPRINT-v1_0-draft.md contains no roster word today, so the refusal currently repairs nothing (m:33).
CORRECTION: Defer the `.gitignore` (and any `-diff`) edit to the commit that first writes data/m/verdicts. Re-read the file then.

Drop the roster-word refusal on table text, or make it a warning. Keep the forbidden-literal check.

Route: PIN.

### [G-ANL-F0: PIN-19 flag_of_record; PIN-21's citation.] Two wording problems:
- The flag predicate includes `renders_sha_matches_calib is True`. That is a content test, which contradicts the spec's own "keyed on existence, not content".
- PIN-21 grounds the two-sided (c) on ledger 41. The spec's own "iff" already gives it directly.
EVIDENCE: [S] m:338: "f1's CORR line carries its dose note iff G-CAL's 0.12 artifact exists (input flag)". m:349 (c): "carried iff G-CAL's 0.12 artifact exists".

[C] G-CAL_model-free.json has f1_012 with renders_sha_matches_calib true, items (a list of 16), n_cond1 4, n_cond2 16, and renders_sha16 2c2c227395ea9f2d.

[S] m:41 concerns states placed in an ordered evaluation, not clause (c).
CORRECTION: Define the flag as TRUE iff:
- the file is committed at HEAD and identical in the working tree;
- schema is m-gcal-model-free-v1;
- an f1_012 block is present.

Record renders_sha_matches_calib beside the flag, or declare it explicitly as an identity clause ("this is f1's replay").

Cite m:349's "iff" as PIN-21's basis.

Route: PIN.

### [G-ANL-F0: §2, displayed numbers.] The spec prints signed values (Δ_c, CI bounds, P_arm − P_sham) "through `bars._dec`" with an ASCII sign. `_dec` is defined for non-negative Fractions and mis-prints negative ones.
EVIDENCE: [C] bars.py:214-224: "Exact half-up decimal display of a non-negative Fraction".

[I] For x = −1/20 it computes v = −500, so divmod(−500, 10000) gives "-1.9500".

[C] Precedent: gcal.dec4(q, signed=True), at gcal.py:166.
CORRECTION: Print signed values as sign + _dec(|x|), or use gcal.dec4(signed=True).
- Declare that rounding is half-up on the magnitude.
- Battery: −1/20 prints "-0.0500", and +1/20 prints "+0.0500".

Route: PIN.

### [G-ANL-F0: PIN-14, VERDICTS from the lock commit's worktree.] The worktree mechanism breaks the spec's relative default paths, and it needs a git write that the spec does not disclose.
EVIDENCE: [I] In a worktree at the lock commit, these resolve inside the worktree:
- `--campaign data/m/ckpt/{U}_campaign.json`, `--time` and `--qual`;
- `--out data/m/verdicts`;
- the flag source.

Campaign checkpoints are committed after the lock, so they are absent there.

[I] `git worktree add` writes to .git. Under the workflow, that is a git write that needs the PI's word.
CORRECTION: Declare the rule:
- When the HEAD analyzer sha, package_sha256 and closure (see the first correction) equal the lock's, VERDICTS runs at HEAD with no worktree.
- Otherwise it runs from a worktree, with every data input and output passed as an absolute path into the main tree, and with the PI's word for the worktree.

The step-19 question (m:291, "`m_analyze.py` extended") stays with the SEAT, as the spec has it.

### [G-ANL-F0: §14 commits; §0 notation.] The record is missing two raws the G-CAL build had:
- the build review raw;
- a post-build site-check raw.

Also, the proposal has 372 lines, not 373.
EVIDENCE: [C] Precedent: results/raw/2026-10-08_m-gcal-build_review.txt, _selftest.txt, _sitecheck.txt and _sitecheck_post.txt.

[C] `wc -l` gives 372. The file ends in \n, and the 373 is a split() artifact. The byte count, 151,231, is correct.
CORRECTION: Add `results/raw/<date>_m-ganl-f0-build_review.txt` and `_sitecheck.txt` to commit #1. The site check must include the new m_analyze suite and the unchanged m suite.

Correct the line count to 372.

### [G-SHAPE-F0: PIN-S7 and the OPEN item for it.] Two problems:
- The cite "RESULTS:919-920" has no commit pin. At HEAD 2c50e03 those lines are about review rounds, because the 110-line insert moved the text.
- The renders that Layer A places come from `scaffold.pool_and_renders()`. They should come from G-CAL's record, with the computed renders asserted equal to them, not the other way round.
EVIDENCE: [S] m:42 (ledger 42): "an anchor into RESULTS.md carries its commit (`RESULTS.md@<hash>:N`)".

[C] The cited text, "`renders_sha16` must come from G-CAL's record and the lock, never be computed by the run itself", is at RESULTS.md@e60b633:919–920, which is HEAD :1029–1030.

[C] G-CAL_model-free.json carries renders_of_record.items[i].render.
CORRECTION: Cite it as RESULTS.md@e60b633:919–920.

Place the 16 renders read from the committed model-free artifact, and assert that `scaffold.pool_and_renders()` equals them, with a STOP on mismatch.

Route: PIN.

### [G-SHAPE-F0: §5 enumeration, §10 artifact, §13 entry and §15 results.] The three OLMo units are presented as three results ("OLMo 0/2,816 per checkpoint"). They are one computation, run three times on byte-identical inputs.
EVIDENCE: [C] Code:
- schedule.py:174-178: `roster_for` returns olmo_roster() for every OLMo unit.
- banner.build_banner takes no checkpoint (banner.py:85-106).
- OLMoTaskRoundAudit() takes no checkpoint (audit.py:464-474).

[C] My probe, critic/probe_a.py, run model-free with -B:
- Q-F0: 0/2,816 fired. Every OLMo unit: 0/2,816 fired.
- render-as-response: 256 on Qwen, 0 on each OLMo unit. This reproduces the spec's figures.
- The sha256 over every (placement, fire fields, RoundAudit) row is identical for sft, dpo and instruct.

[S] m:174: "**F0m-OLMo** (per checkpoint)". Keeping per-unit rows is therefore literal-compliant.
CORRECTION: Keep the per-unit rows, but compute and record `olmo_grids_identical: true`: the digests of the rows with the unit stripped, which must be equal, with a STOP if not.

In the entry, say it is one OLMo computation. The only input that differs by checkpoint is the scaffold_{ckpt}.json string check. The ban-id half is checked on the box (LOCK-m-OLMo-{ckpt} v0.1, m:302).

Route: PIN.

### [G-SHAPE-F0: Layer B (PIN-S5, PIN-S11, self-test #10), Layer C (PIN-S6) and PIN-S12.] Over-built:
- There are three mechanisms for the runner half: Layer S (static, in the artifact), Layer B (dynamic, in the self-test), and the existing runner self-tests that already exercise the same path.
- Layer B adds new keys (`m-shape|…`), a gold oracle, a 1,000-session cap and a coverage loop.
- PIN-S12 (MODULES equals the module stems) is driver hygiene, outside the gate's "nothing else".

PIN-S5 and PIN-S6 change what the gate artifact contains and what its verdict logic is. The readers split on PIN-S5. A seat strike after the run forces a re-run that the write-once rule refuses.
EVIDENCE: [S] m:277: "It tests scoring scope, nothing else." m:33: "an answer to a check first asks whether the mechanism it repairs is needed".

[C] runner_qwen.py:274-288 already asserts that 8 clean scripted sessions over {A0, A0s} × start × clause are valid and complete with no exclusion. runner_qwen.py:409 asserts "contrast Q rounds deliver the corrupt_m render". runner_olmo has the analogue.

So the dynamic case (a corrupted render beside its header, a clean response, no fire) is already exercised through the real runner code.
CORRECTION: Keep ONE runner-half mechanism in the record. Preferred: Layer S in the artifact, with the entry naming the existing runner self-test checks as the dynamic evidence (ledger 30). Then drop Layer B and its keys.

If Layer B is kept, drop Layer S.

Trim Layer C to what instrument validity needs: one scope-widened scorer per unit, for example seg+gold, or justify each of the four.

Replace PIN-S12 with `"gshape" in MODULES`.

Route: PIN-S5 and PIN-S6 stay Code PINs, but must reach the seat before LOCK v0.1 (blocking LOCK v0.1, not step 7).

### [G-SHAPE-F0: §4 preconditions and §10 provenance.] §12 requires "a clean tree for every file in SCORING_STACK_FILES and TOOLING_FILES", but no precondition enforces it. So the artifact could record working-tree shas that are not committed blobs.

Also, the data/olmo/b3_screen_{ckpt}.json files are read at §4 step 10 but are not in the sources map.
EVIDENCE: [S] CLAUDE.md, rule 27: "the repo, not any machine, is the record".

[C] Precedent: stages._committed (stages.py:408) is already used for the proposal at §4 step 3. G-ANL's `ganl` refuses an analyzer or placeholder that is not committed.

[C] b3_screen_{sft,dpo,instruct}.json ban_list = {n_ids 9, sha16 2dd86a453a2275ef}.
CORRECTION: Add a refusal (exit 2, nothing written) unless every file in SCORING_STACK_FILES and TOOLING_FILES is committed at HEAD and identical in the working tree.

Add the three b3_screen files to the sources map.

Route: PIN.

### [G-SHAPE-F0: PIN-S5 and §12 pairing of the self-test with the run of record.] The entry is to pair the run of record with a full self-test pass "at the same package_sha256". But the m self-test raw never prints package_sha256, so the pairing cannot be checked from committed raws.
EVIDENCE: [C] m_sessions.py:2376-2387: run_selftest prints only per-check lines and "N/N m selftest checks pass".

[S] G-SHAPE PIN-S5: "The run of record is made only after the m self-test passes in full at the same package_sha256, and the entry pairs the two."
CORRECTION: Have gshape._selftest print package_sha256, and the digest of the SCORING_STACK_FILES/TOOLING_FILES sources map, in its check note. The pairing then reads directly off results/raw/<date>_m-gshape-build_selftest.txt and the run raw.

Route: PIN.

### [Both: write-once artifacts. A LOCK-m-F0 v0.1 hazard.] Neither spec declares what happens when an artifact must be replaced: G-ANL says nothing, and G-SHAPE says only "moves only on the seat's ruling". Several pending events could force a re-run:
- the seat strikes a PIN (S3, S5, S6, or an analyzer item);
- G-CAL's owed 128-generation read, or O2/O3, re-specifies the renders;
- the seat answers the third order question;
- a scoring-stack or analyzer edit.

Each would hit the write-once refusal.
EVIDENCE: [C] gcal.py:206-222 states the rule: never overwritten, "move it aside by hand if it must be replaced".

[C] The 2c50e03 entry lists what is still owed: the read of the 128 generations, and O3, "whether item 2's 0/4 on `thiru` bears on (3) or (4)". Either could re-specify the renders.

[I] Neither artifact carries a HEAD or a timestamp. So a re-run on unchanged inputs returns "identical".
CORRECTION: Declare the procedure in both specs and entries. On the seat's ruling, the old artifact is moved by hand with `git mv` to a dated superseded name, recorded in an entry, and the re-run then writes the canonical name.

Also state in both entries that a re-run after G-CAL closes, on unchanged inputs, is byte-identical. That makes it the zero-cost remedy if the seat rules that steps 7 and 8 must follow the close.

Route: PIN, plus notice to the SEAT in the consolidated block.

### [LOCK-m-F0 v0.1 hazard, spanning both specs.] LOCK v0.1 will bind gate artifacts produced under two different package_sha256 values, and neither spec says how the lock reconciles them. G-PORT and G-CAL were produced at 4b49…02ac. G-SHAPE will be produced at the post-step-7 package.

The docstring sentence added to `__init__.py` also widens the diff for no functional reason.
EVIDENCE: [S] m:279: LOCK v0.1 carries "Port acceptance; calibration (§2.3 artifacts); G-SHAPE-F0; keys; module homes".

[C] Recomputed here: package_sha256 at HEAD = 4b49658739523c60951910dd80c04983fbc01cf8e7abc351be6baadec84202ac. This equals G-CAL_model-free.json and completability identity.package_sha256. m_sessions.py:208 writes the package sha into G-PORT's artifact.

[C] Nothing in stages, guard or resume reads the G-PORT or G-CAL artifacts' package sha (grep shows no reader).
CORRECTION: LOCK v0.1 should state:
- each gate artifact's package_sha256;
- the mechanical `git diff --stat c75d4d8..<lock commit> -- valence_core/m`, which must show only gshape.py (and `__init__.py` if kept) and no SCORING_STACK_FILES;
- G-ANL's closure from the first correction.

Drop the `__init__.py` docstring edit, so the diff is gshape.py alone.

Route: PIN for the lock build. List it in the consolidated seat block.

---

## FILE: spec_gshape.md (sha256 d9d8626e4aea9bee605d03edcf13b9571cff21d99cb99b969d644cd719bbeaa6)

# G-SHAPE-F0: build spec (PROPOSAL-m v1.11, §8 step 7)

**Basis.**
- HEAD is **`2c50e03`**, not the `e60b633` the readers saw. That commit added the entry "G-CAL — THE SEAT'S LEGIBILITY READ OF RECORD … PASS, 16/16". It committed `data/m/gates/G-CAL_seat_read_of_record.md` and added `.gitignore:247`, the line that admits it.
- File hashes:
  - seat read: sha256 `39990bae8481ee313274e3b37ed6332026d936f2f4db55454c62a5d67fea878a`. The gshape reader wrote "…a10546", which is wrong.
  - spec `PROPOSAL-m-gating-campaign-v1_11.md`: sha256 `42ab36ec…6c6b`.
- Two reader items are already closed by `2c50e03`: the read is admitted and committed, and its entry is written.
- That entry also says:
  - G-CAL stays open. It is owed the read of the 128 generations (m:271) and the two order rulings.
  - Steps 7 and 8 start now "on the PI's word".
  - Starting them before G-CAL closes is "a third order question for the seat".
  - LOCK-m-F0 v0.1 waits on G-CAL closing.
- Nothing below needs a model, a tokenizer or the box.

Tags used below: **[S]** = the spec states it, with an m:N cite and an exact quote. **[I]** = inferred, or Code's reading. **[C]** = a figure this synthesis re-ran in a tool from scratch (scripts in `…/scratchpad/step78/`; `git status` unchanged afterwards).

---

## 1. What the spec states

**What G-SHAPE-F0 is.**
- [S] m:277 (the whole criterion): "Model-free: every corrupted render placed inside each F0m and F0m-OLMo round template beside its bracketed header, a clean gold as the response, run through the full scoring stack of both substrates; asserts that no class fires on harness bytes or the render itself. It tests scoring scope, nothing else."
- [S] m:264: "`lexical_hit` on model-generated task-round text only; harness-written lines are not its input" … "G-SHAPE is a plumbing check only."
- [S] m:56: "G-SHAPE as the item-shape check → a scoring-scope plumbing test". The item-shape half belongs to the qualification stages' contrast sessions.

**Order, lock and entries.**
- [S] m:358: "7. G-SHAPE-F0. 8. G-ANL-F0 … 9. Commit LOCK-m-F0 v0.1."
- [S] m:279: LOCK v0.1 carries "G-SHAPE-F0; keys; module homes".
- [S] m:363: the entry is named `G-SHAPE-F0`, and "Values-check pre-commit as the record does."
- [S] m:290: "As G-SHAPE-F0 for the F3 templates, the reasoning header included" (step 19).
- [S] m:357: "No F3 code".

**Templates, rosters and renders.**
- [S] m:159: "round templates `ROUND_TEMPLATES[(s + i) % 4]` for the i-th round and menus `MENU_TEMPLATES[(s + c) % 4]`". Round templates and menus are distinct.
- [S] m:172: "Templates: e2a's (`SESSION_BANNER`, `ROUND_TEMPLATES`, `MENU_TEMPLATES` …) on Qwen; b3's on OLMo"; also "Sham arms serve `CORR_clean` to both labels."
- [S] m:174: "**F0m-OLMo** (per checkpoint): b3's alternating apparatus, uncached, banner lines of §2.5."
- [S] m:176: "the read of record is repeated at G-CAL on the renders of record"; LOCK v0.1 carries "the renders' sha256".

**The two scoring stacks.**
- [S] m:261 (Qwen):
  - "Audit v3's `task_text` on a corrupted round is the render as delivered";
  - "Claiming order (rule 28(b)): v2 → echo → v4 content → own-pair lexical";
  - the Qwen `scaffold_absorption` set is "the e2a ban list as `e2d.config` loads it".
- [S] m:262 (OLMo):
  - "Claiming order b3 audit → echo → lexical";
  - the six strings are "asserted at startup equal to the ban-list strings and to b3's id sha16".
- [S] m:271: `scaffold_absorption` is "(a banned string, from the substrate's set, in any model-generated text)".

**Ledger lines that bind this build.**
- [S] m:30 (ledger 30): "every stage that "meets" a check names the sessions or artifacts that contain the thing checked".
- [S] m:33 (ledger 33): "an answer to a check first asks whether the mechanism it repairs is needed".

**What the spec does not state.** It names no consequence for a fire (G-PORT, by contrast, has "64/64 or STOP", m:275). It also names no artifact, exit code, provenance or module home.

## 2. How the gate is shaped (Code's reading)

**Templates are the same objects on both substrates.** [I], verified:
- Both substrates build every task round through `scaffold.SessionScaffold._round` (`scaffold.py:154–161`): `seg = ROUND_TEMPLATES[ti].format(n=n, tag=label, task=task_text)`.
- `ROUND_TEMPLATES` is `valence_core/session_e2a.py:71–76`, four bracketed headers each followed by `\nTask: {task}\nResponse:`.
- b3 imports the same object (`scripts/box_b3_sessions.py:65–66`).
- So "each F0m and F0m-OLMo round template" means `ROUND_TEMPLATES[0..3]` on both substrates.

**What the runners score.** [I] The four production call sites:
- Qwen: `runner_qwen.py:161, :192`, `audit.classify(g.text, render=spec.task_text, item=spec.item, earlier=earlier, own_pair=own, echo_lines=echo_lines, phase=…)`;
- OLMo: `runner_olmo.py:139, :166`, `audit.classify(g.text, own_pair=own, echo_lines=echo_lines, phase=…)`;
- termination is computed in `SessionLog.add_round` (`scaffold.py:392`) on `g.text`.

**Scope has two ends** [I]:
- (a) The classifier, given a clean gold and the render as `task_text`, must not fire.
- (b) The runner must hand the classifier the generation alone, never the segment, banner or render.

A classify-level walk alone tests only (a). Its "no class fires on harness bytes" half is vacuous, because harness bytes never reach a classifier that is handed only the gold.

[C] Scoring the render as the response fires on Qwen in 256 of 2,816 placements (v5 `task_echo`, items 2 and 8 only) and on OLMo in 0 of 8,448. So a runner that scored the render would pass a classifier-only gate on OLMo.

**Resolution (PIN-S5).** The artifact of record carries three layers:
- **Layer A**: m:277's placements through each substrate's classifier stack.
- **Layer C**: must-fire controls, proving the stack can fire.
- **Layer S**: a static check of the four classify call sites and `add_round`.

**Layer B** drives the real runners on `testing`'s doubles with a gold oracle. It runs in `gshape._selftest` only.

**Why Layer B stays out of the artifact.**
- `scripts/box_selftest_stub.py`'s docstring says the stub is "Not imported by `valence_core` and not on any run path: the runners import it only under `--selftest`", and that a stub result reaching a canonical path "would be indistinguishable from a measurement".
- The PIN at `stages.py:149–152` routes every output of a stub run through `resume.refuse_canonical_out`.
- Readers *code* and *records* recommended keeping the stub out. Reader *gshape* preferred Layer B in the artifact.
- This spec keeps the existing convention. Static Layer S puts runner scope into the artifact without the stub. m:33 is satisfied: Layer S repairs the one thing a classifier walk cannot test.

## 3. Code homes and changes

**New module `valence_core/m/gshape.py`.**
- Model-free. No module-level import of `testing`; `_selftest` imports it lazily, as `gcal`, `stages` and the runners do.
- Imports: `audit, banner, corr, gcal, guard, keys, resume, scaffold, schedule, stages`, `valence_core.session_e2a.ROUND_TEMPLATES`, `numpy`, `ast`, `hashlib`, `json`.
- No `generate` / `forward` calls outside `_selftest`.

**`valence_core/m/__init__.py`.** Add one docstring sentence: "step 7 adds ``gshape`` (G-SHAPE-F0: scoring-scope plumbing, model-free)".

**`scripts/m_sessions.py`.**
- Add `"gshape"` to `MODULES`, after `"gcal"`.
- Add `run_gshape(out)` and a `gshape [--out DIR]` subparser, mirroring `gcal model-free`.
- Document the command in the module docstring.
- Add integration checks (§11.2).

**Files not touched:**
- `testing.py`, `runner_qwen.py`, `runner_olmo.py`, `audit.py`, `scaffold.py`, `gcal.py`, `stages.py`;
- every file in `SCORING_STACK_FILES` (§9);
- the parallel session's files: `scripts/audit_note_*`, `results/raw/*note-*`, `README-NOTE.md`, `RESEARCH-NOTE-*`, `AUDIT-note-*`.

**Effect on `package_sha256`.** It moves off `4b49658739523c60…02ac`, the value recorded by G-CAL, because `gshape.py` and `__init__.py` change. The write-once G-PORT and G-CAL artifacts are not invalidated, and nothing reads their package sha downstream. Disclose this in the entry.

**Constants in `gshape.py`:**

```python
SCHEMA = "m-gshape-f0-v1"
STAGE = "G-SHAPE-F0"
ARTIFACT_NAME = "G-SHAPE-F0.json"
SPEC_REF = "PROPOSAL-m v1.11 §3.1 G-SHAPE-F0 (m:277); §8 step 7 (m:358)"
CRITERION_HEAD = "**G-SHAPE-F0 (plumbing).**"
CRITERION = ("Model-free: every corrupted render placed inside each F0m and F0m-OLMo round template "
             "beside its bracketed header, a clean gold as the response, run through the full scoring "
             "stack of both substrates; asserts that no class fires on harness bytes or the render "
             "itself. It tests scoring scope, nothing else.")
RENDERS_SHA256_OF_RECORD = "a04f67b0e5105a0514a0f33e64a4545ef3a3a3c75cece320d78434e853cd4372"
MODEL_FREE_REL = "data/m/gates/G-CAL_model-free.json"
COMPLETABILITY_REL = "data/m/gates/G-CAL_completability_qwen.json"
SEAT_READ_REL = "data/m/gates/G-CAL_seat_read_of_record.md"
UNITS = keys.UNITS_BUILT            # ("Q-F0", "OLMo-sft", "OLMo-dpo", "OLMo-instruct")
ROUND_FIRE_FIELDS = ("claim", "advisory", "v3.exclusion", "v3.content_label", "v3.advisory",
                     "echo_line", "lexical_raw", "scaffold", "degeneracy", "ends", "strict",
                     "termination")
CONTROLS_REQUIRED = ("seg+gold", "banner+seg+gold", "header+gold", "taskline+gold")
CONTROLS_REPORTED = ("render-as-response",)
SCORING_STACK_FILES = (
  "valence_core/m/audit.py", "valence_core/m/banner.py", "valence_core/m/corr.py",
  "valence_core/m/keys.py", "valence_core/m/schedule.py", "valence_core/m/scaffold.py",
  "valence_core/m/runner_qwen.py", "valence_core/m/runner_olmo.py",
  "valence_core/session.py", "valence_core/session_e2a.py",
  "valence_core/e2d/audit_v3.py", "valence_core/e2d/contentclass.py",
  "valence_core/e2d/contentclass_v4.py", "valence_core/e2d/contentclass_v5.py",
  "valence_core/e2d/config.py",
  "data/configs/e2b_audit_v2.json", "data/configs/e2a_ban_list.json",
  "data/configs/f_termination_patterns.json", "data/f/pools.json",
  "data/olmo/a1_repair_roster.json",
  "data/olmo/scaffold_sft.json", "data/olmo/scaffold_dpo.json", "data/olmo/scaffold_instruct.json")
TOOLING_FILES = ("valence_core/m/gshape.py", "scripts/m_sessions.py")
FIRES_LISTED_MAX = 50               # per unit; n_fired always exact

class GshapeRefusal(SystemExit): ...   # exit 2: decided before any scoring; nothing written
class GshapeStop(SystemExit): ...      # exit 4: a pinned figure does not reproduce; no artifact
```

**Public functions:**

```python
def inputs_of_record(*, proposal_rel=stages.PROPOSAL_REL) -> dict      # §4, in order
def qwen_stack(pool) -> audit.QwenTaskRoundAudit                         # PIN-S4
def olmo_stack() -> audit.OLMoTaskRoundAudit                             # PIN-S4
def template_shape_problems(templates=ROUND_TEMPLATES, renders=..., labels=...) -> list[str]
def placements(unit, renders, pool) -> Iterator[Placement]               # §5
def round_fires(ra, text, term_rx) -> list[str]                          # §6
def grid(units=UNITS, *, scorer=None) -> dict                            # Layers A and C
def runner_scope_problems(sources: Mapping[str, str] | None = None) -> list[str]   # Layer S, §8
def evaluate(*, seams...) -> dict                                        # the artifact dict, verdict
def write(out_dir=None) -> dict   # {"artifact","path","how" in {"written","identical"}}
def _selftest(chk) -> None
```

**Seams.** `scorer`, `templates`, `sources` and an inputs override exist for the self-test only. A run with any seam set refuses a canonical path, as gport's supplied `rows` do.

## 4. Preconditions, in order

Each step is a refusal (exit 2, nothing written) or a STOP (exit 4, no artifact).

1. **`--out`.** An empty `--out` is a refusal. `--out` under `data/m`, `/workspace/models` or `data/olmo` is refused through `resume.refuse_canonical_out`. Without `--out`, the path is `guard.GATES_DIR / ARTIFACT_NAME`.
2. **numpy stream.** `keys.stream_known_answer() == []`, else **GshapeStop**.
3. **Proposal.**
   - `stages._committed(PROPOSAL_REL)` must succeed: committed at HEAD and identical in the working tree. Otherwise **refusal**.
   - `proposal_sha256` = sha256 of the committed bytes.
   - The line starting with `CRITERION_HEAD` must contain `CRITERION` verbatim. Otherwise **refusal**: "not the governing proposal".
4. **Banners.** `banner.spec_problems(<proposal path>) == []`, else **GshapeStop**. The banners placed must be §2.5's bytes.
5. **G-CAL model-free artifact.**
   - `_committed(MODEL_FREE_REL)` must succeed; then `gcal._model_free_check(path, RENDERS_SHA256_OF_RECORD, proposal_sha256)`.
   - Absent, uncommitted, wrong schema, or proposal sha different from G-CAL's provenance → **refusal**.
   - Renders sha different → **GshapeStop**.
   - Conditions "1" and "2" must have verdict PASS, else **GshapeStop**.
6. **G-CAL completability.** Committed, `verdict == "PASS"` and `identity.renders_sha256 == RENDERS_SHA256_OF_RECORD`, else **refusal**.
7. **Seat read.** Committed, and its line `renders_sha256: \`…\`` equals the pin, else **refusal**.
8. **Renders.**
   - `scaffold.pool_and_renders()` renders must equal `renders_of_record.items[i].render` in order.
   - sha256 of `"\n".join(renders)` must equal the pin.
   - `resume.pool_sha16(pool)` must equal the artifact's provenance `pool_sha16` (`711deec1c2645194`).
   - Otherwise **GshapeStop**.
9. **32 distinct texts.** The 16 renders together with the 16 clean tasks must be 32 distinct strings. Golds: 16 items, 22 variants, all distinct. Otherwise **GshapeStop**.
10. **Stacks** (PIN-S4). Any `SystemExit` from a pinned-sha mismatch → **GshapeStop**. Qwen:
    - `audit3, cfg = audit.qwen_audit_of_record()`, which checks v2 sha16 `7aa235d25eeb66dc` and the e2a ban-list sha256 `9a2f0744…31c4`;
    - `audit.assert_qwen_scaffold(file["ids"], file["strings"], audit3)` on `data/configs/e2a_ban_list.json`;
    - `QwenTaskRoundAudit(audit3, pool, file["strings"])`.

    OLMo:
    - `OLMoTaskRoundAudit()`;
    - for each ckpt, `sorted(json(data/olmo/scaffold_{ckpt}.json)["ban_strings"]) == sorted(audit.OLMO_SCAFFOLD_STRINGS)`;
    - `b3_screen_{ckpt}.json["ban_list"]` must equal `{"n_ids": 9, "sha16": "2dd86a453a2275ef"}`. This is recorded, not exercised.
11. **Termination patterns.** `term_rx = scaffold.load_term_rx()` (sha16 `014b3940d62401b0`).

## 5. Layer A: the enumeration (PIN-S1, PIN-S2)

For each `unit` in `UNITS`:
- substrate is `qwen` if `unit == "Q-F0"`, else `olmo`;
- `tA = keys.templates(unit)[0]` (`A0`, or `A0-OLMo-{ckpt}`);
- `roster = schedule.roster_for(unit)`.

For each `pi` in 0..3, `mp` in (0, 1) and `cl` in (0, 1):
- `P, Q = roster[pi][mp], roster[pi][1-mp]`;
- `bnr, notes = banner.build_banner(tA, P, Q, cl)`;
- echo set: `audit.qwen_echo_lines(notes)` on Qwen, `audit.olmo_echo_lines(notes)` on OLMo.

Then for each `t` in 0..3, item `i` in 0..15, gold `g` in `pool[i]["gold"]` (verbatim) and `phase` in (`"forced"`, `"free"`):
- `n = t + 1` if forced, else `t + 5`;
- `seg = ROUND_TEMPLATES[t].format(n=n, tag=Q, task=renders[i])`;
- score `g`:
  - Qwen: `Q.classify(g, render=renders[i], item=i, earlier=(), own_pair=(P, Q), echo_lines=el, phase=phase)`;
  - OLMo: `O.classify(g, own_pair=(P, Q), echo_lines=el, phase=phase)`;
- evaluate `round_fires(ra, g, term_rx)`;
- score each control text (§7) with the same arguments.

**Size.** 16 banners × 4 × 22 × 2 = **2,816 placements per unit, 11,264 in all**. The spec-literal minimum would be 16 × 4 × 2 = 128.

**Placement keys.**
- `placements_sha256` = sha256 of `resume.json_text([[unit, pi, mp, cl, t, n, i, g, phase], …])`, in enumeration order, per unit.
- Coverage must be exact:
  - every (`i`, `t`, `phase`) present;
  - all 22 gold variants present;
  - all 16 banners present;
  - all four units present.
- Any shortfall is verdict STOP with reason `coverage:<unit>`.

**Template shape** (`template_shape_problems`). Over every template, every n in 1..10, every render and each unit's Q labels:
- `seg.split("\n") == [header, "Task: " + render, "Response:"]`;
- `header.startswith("[round ")` and `header.endswith(f": {Q}]")`;
- no newline in any render.

Any problem is verdict STOP with reason `shape`.

## 6. The fire predicate (PIN-S3)

```python
def round_fires(ra, text, term_rx):
    f = []
    if ra.claim is not None: f.append("claim")
    if ra.advisory: f.append("advisory")
    if ra.v3 is not None:
        if ra.v3.get("exclusion") is not None: f.append("v3.exclusion")
        if ra.v3.get("content_label") is not None: f.append("v3.content_label")
        if ra.v3.get("advisory"): f.append("v3.advisory")
    if ra.echo_line is not None: f.append("echo_line")
    if ra.lexical_raw is not None: f.append("lexical_raw")
    if ra.scaffold: f.append("scaffold")
    if ra.degeneracy: f.append("degeneracy")
    if audit.ends_session(ra): f.append("ends")
    if audit.strict_excludes(ra): f.append("strict")
    if scaffold.termination(text, term_rx): f.append("termination")
    return f
```

**A placement fires iff `round_fires(...) != []`.** Any firing placement makes the verdict STOP, with reason `fire:<unit>`.

The artifact lists up to 50 fires per unit, each as {placement key, fields, `ra.detail`}. `n_fired` is always exact.

## 7. Layer C: controls (PIN-S6)

These are instrument validity, not criteria. For every placement, score these texts with the same arguments as the gold:
- `seg+gold` = `seg + g`
- `banner+seg+gold` = `bnr + seg + g`
- `header+gold` = `header + " " + g`
- `taskline+gold` = `"Task: " + render + " " + g`
- `render-as-response` = `render` (reported only)

**Required.** Each of the four required controls fires on **2,816/2,816 for every unit**. Otherwise verdict STOP, reason `control-silent:<unit>:<name>`.

[C] All four fire 100% on both stacks. Every template's header line alone fires `frame:[round` on both v2 and AuditSpec.

**Reported.** `render-as-response`: [C] Qwen 256/2,816 (v5 `task_echo` advisory only, items 2 and 8); OLMo 0/2,816 per unit. The entry explains that Layer S, not Layer A, covers this case.

## 8. Layer S: static runner scope (PIN-S5)

`runner_scope_problems(sources=None)` parses `valence_core/m/runner_qwen.py`, `runner_olmo.py` and `scaffold.py` with `ast`. With `sources=None` it reads the package files. It returns `[]` iff all of the following hold.

**Inside `run_session_qwen` and `run_session_olmo`:**
- **R1.** Exactly two calls `audit.classify(...)`, where `audit` is the function's parameter.
- **R2.** Each call's only positional argument is `G.text`. In the same statement list, the nearest earlier statement binding `G` is `G = adapter.generate(<prefix>, S.seg, injections=(), …)`, with no rebinding of `G` or `S` in between.
- **R3.** The two calls carry `phase="forced"` and `phase="free"` (string constants), one each.
- **R4 (Qwen).**
  - `render=S.task_text` and `item=S.item`, with `S` the name whose `.seg` went to `generate`;
  - `earlier=earlier`;
  - every `earlier.append(x)` in the function has `x` = `<gen>.text`.
- **R5.** `own_pair=own` and `echo_lines=echo_lines`, where:
  - `own` is bound by `own = (sc.P, sc.Q)`;
  - `echo_lines` is bound by `_audit.qwen_echo_lines(sc.note_lines)` on Qwen, or `_audit.olmo_echo_lines(...)` on OLMo.
- **R6.** The statement after `RA = audit.classify(...)` is `log.add_round(S, G, RA, term_rx)`.

**Inside `SessionLog.add_round`:**
- **R7.** The record's `"text"` value is `str(g.text)` and its `"termination"` value is `termination(g.text, term_rx)`, with `g` the parameter.

**Across the package:**
- **R8.** No other `.classify(` call exists in `valence_core/m/*.py` outside `_selftest` functions and `gshape.py`.

**Result.** Any problem is verdict STOP, with reason `scope-static`. The artifact records `layer_s = {"files": {path: sha256}, "rules": ["R1", …, "R8"], "problems": [...]}`.

[C] A prototype of R1–R6 (`synth_scope_static.py`) returns `[]` on the current sources. It catches `prefix + g.text`, `spec.seg + g.text`, `spec.task_text` as the scored text, `render=spec.seg`, and a swapped phase.

## 9. Verdict, outcomes, exit codes (PIN-S8)

**PASS** iff all of these hold:
- preconditions passed;
- `template_shape_problems == []`;
- every unit has n = 2,816 with full coverage and `n_fired == 0`;
- every required control fired 100% for every unit;
- `runner_scope_problems == []`.

**Otherwise STOP.** `stop_reasons` is a sorted list of the codes `shape`, `fire:<unit>`, `coverage:<unit>`, `control-silent:<unit>:<name>` and `scope-static`.

**Exit codes**:

| Code | When | Artifact |
|---|---|---|
| 0 | PASS | written, or identical bytes already there |
| 2 | Refusal (`GshapeRefusal`): any §4 refusal, or an existing different artifact or a symlink at the path (on STOP too) | not written; existing file untouched; verdict reported as "not recorded" |
| 4 | STOP verdict | written with its evidence (G-PORT's precedent) |
| 4 | `GshapeStop` from §4 | none |
| 4 | Any other `SystemExit` (gcal's PIN) | none |

**On STOP.** Code escalates to the seat and does not adjudicate (CLAUDE.md: "Code escalates fired gates, never self-adjudicates"). LOCK-m-F0 v0.1 does not commit. The STOP artifact is committed as evidence and moves only on the seat's ruling.

## 10. The artifact (PIN-S9, PIN-S10)

- **Path.** `data/m/gates/G-SHAPE-F0.json`. It is already admitted by `.gitignore:235` (`!/data/m/gates/*.json`). gcal's `canonical_files()` globs `G-CAL*`, so the name does not collide.
- **Serialisation.** `resume.json_text(art, indent=1)`.
- **Write-once.** gcal's `_write_once_text` rule, re-implemented with `GshapeRefusal`:
  - identical bytes give "identical";
  - different bytes, or a non-file, are refused and left untouched;
  - the write is atomic (temp file, fsync, rename, directory fsync);
  - it never writes through a symlink.
- **Determinism.** No timestamp and no HEAD, so re-runs are byte-identical.

```json
{
 "schema": "m-gshape-f0-v1", "stage": "G-SHAPE-F0", "spec": SPEC_REF, "criterion": CRITERION,
 "inputs": {
   "renders_sha256": "a04f67b0…4372", "n_renders": 16,
   "gcal_model_free": {"path": MODEL_FREE_REL, "sha256": "aad8096a…34af"},
   "gcal_completability": {"path": COMPLETABILITY_REL, "sha256": "46afd364…c15b", "verdict": "PASS"},
   "seat_read": {"path": SEAT_READ_REL, "sha256": "39990bae…878a", "renders_sha256_cited": "a04f67b0…"},
   "pools_file": "data/f/pools.json", "pools_file_sha256": "8547d9a1…17a0", "pool_sha16": "711deec1c2645194",
   "golds": {"n_items": 16, "n_variants": 22, "sha256": "<sha256 of json_text of the 16 gold lists>"},
   "round_templates_sha256": "<sha256 of json_text(list(ROUND_TEMPLATES))>",
   "olmo_round_templates": "valence_core.session_e2a.ROUND_TEMPLATES (b3 imports it; m's scaffold builds from it)",
   "session_banner_sha256": "…", "roster_sha256": {"Q-F0": "…", "OLMo": "…"}},
 "stacks": {
   "qwen": {"claim_order": ["v2","echo","content","lexical"], "audit_v2_sha16": "7aa235d25eeb66dc",
            "e2a_ban_list_sha256": "9a2f0744…31c4", "n_scaffold_strings": 12, "term_sha16": "014b3940d62401b0",
            "end_rule": "qwen_ends (lenient); strict beside"},
   "olmo": {"claim_order": ["audit","echo","lexical"], "audit_sha16": "<runner_olmo.olmo_audit_sha16()>",
            "scaffold_strings": [six], "term_sha16": "014b3940d62401b0", "end_rule": "olmo_ends",
            "ban_ids_sha16": "2dd86a453a2275ef", "ban_ids_n": 9,
            "ban_ids_note": "generation-side (m:262 'asserted at startup'); olmo_startup asserts it on the box before any OLMo session; not exercised by G-SHAPE-F0"}},
 "fire_predicate": {"round": ROUND_FIRE_FIELDS},
 "grid": {"<unit>": {"template": "A0…", "n": 2816, "n_fired": 0, "fires": [], "placements_sha256": "…",
                     "coverage": {"renders": 16, "templates": 4, "phases": 2, "banners": 16, "gold_variants": 22}}},
 "grid_total": 11264,
 "controls": {"<unit>": {"seg+gold": {"n": 2816, "n_fired": 2816, "required": true}, …,
                         "render-as-response": {"n": 2816, "n_fired": 256, "required": false}}},
 "template_shape": {"problems": []},
 "layer_s": {"files": {…}, "rules": ["R1",…,"R8"], "problems": []},
 "runner_layer": "dynamic check in gshape._selftest at this package_sha256 (testing's doubles; selftest-only, PIN-S5)",
 "verdict": "PASS", "stop_reasons": [],
 "provenance": {"package_sha256": "…", "sources": {SCORING_STACK_FILES → sha256}, "tooling": {TOOLING_FILES → sha256},
                "proposal_file": "PROPOSAL-m-gating-campaign-v1_11.md", "proposal_sha256": "42ab36ec…6c6b (committed blob)",
                "numpy": "<version>", "numpy_stream_known_answer": "clean (f|CORR|0 permutation)"}
}
```

## 11. Driver and self-test

### 11.1 Driver

- **Command of record.** `jlens-qwen36/.venv/bin/python scripts/m_sessions.py gshape`.
- **Refusals** (exit 2): `--selftest`, `--build-schedules` or a top-level `--out` with `gshape`; an empty `--out`.
- **`run_gshape(out)`** maps `GshapeRefusal` → 2, `GshapeStop` → 4, any other `SystemExit` → 4, and the verdict through {PASS: 0, STOP: 4}.
- **Stdout, counts only.** It must pass the driver's `stdout_problems`: no roster word, no menu fragment, no pick line.

```
INVOCATION: …
G-SHAPE-F0 inputs: renders sha256 <64>; G-CAL model-free sha256 <64>; proposal sha256 <64>; package sha256 <64>
G-SHAPE-F0 grid <unit>: <n> placements, <k> fired          (x4)
G-SHAPE-F0 controls <unit>: seg+gold n/n, banner+seg+gold n/n, header+gold n/n, taskline+gold n/n; render-as-response k/n (reported)   (x4)
G-SHAPE-F0 template shape: <clean|N problems>; runner scope (static): <clean|N problems>
G-SHAPE-F0 verdict <PASS|STOP> [<reason codes>]
G-SHAPE-F0 artifact: <path> (<written|identical>)
```

### 11.2 Self-test checks

Every check runs in both directions: the real case passes and a planted defect fires.

**`gshape._selftest(chk)`:**

1. **Real inputs, temp `--out`.** PASS, 2,816 per unit, 11,264 in all, controls 100%, Layer S `[]`. Then a second run returns "identical", with equal bytes and exit 0.
2. **Predicate completeness.**
   - For each independently settable field (claim, advisory, v3.exclusion, v3.content_label, v3.advisory, echo_line, lexical_raw, scaffold, termination), a synthetic `RoundAudit` or text with only that field set returns exactly that field.
   - The same probe returns `[]` under a predicate copy with that field removed, so every field is mutation-sensitive.
   - degeneracy, ends and strict co-fire with claim.
   - An all-empty probe returns `[]`.
3. **Real classes reachable** through `round_fires`. Inputs verified [C] in `synth_mustfire.py`.

   Qwen:

   | Input | Fires |
   |---|---|
   | `"<|im_end|>"` | claim v2 special + scaffold |
   | COMMON line | echo |
   | `"Reasoning (one line):"` | echo |
   | TOLD line | echo + lexical_raw |
   | `"* * *"` | content null_response |
   | `"77"` with `earlier=("77",)` | content stuck_attractor |
   | `"Sure, I'll answer."` | content preamble_without_content |
   | another item's clean task | advisory wrong_task |
   | item 2's render with `render`=it | advisory task_echo |
   | `"77 <own label>"` | lexical |
   | `"77. End of session."` | termination only |
   | `""` | v2 empty |

   OLMo:

   | Input | Fires |
   |---|---|
   | `"<|pad|>"` | scaffold only |
   | `"<think>"` | audit + scaffold |
   | COMMON minus final period at end | echo (stem) |
   | `"77 <own label>"` | lexical |
   | `"77. End of session."` | termination only |

   Qwen's COMMON line without its final period fires nothing; this is the existing PIN, asserted as a silent case.
4. **Scope-widened scorers.** `scorer=seg+gold` and `scorer=banner+seg+gold` each give STOP with n_fired = 2,816 per unit. `scorer=render` gives Qwen 256 and OLMo 0, which is reported.
5. **Silent control.** A control table whose `seg+gold` text is the gold gives STOP `control-silent`.
6. **Coverage.** Each of these gives STOP `coverage`: one render dropped, one template dropped, one phase dropped, one unit dropped, one gold variant dropped, one banner dropped.
7. **Inputs** (temp copies through the inputs seam):
   - a render altered by one byte → `GshapeStop` before any scoring, no file written;
   - model-free artifact absent → refusal;
   - completability verdict FAIL → refusal;
   - seat-read sha line altered → refusal;
   - proposal sha different from G-CAL's → refusal;
   - `keys.stream_known_answer` patched to report a problem → `GshapeStop`;
   - `banner.spec_problems` patched to non-empty → `GshapeStop`.
8. **Template shape.** Templates without the bracketed header, with the Task line not second, or with the tag missing → STOP `shape`.
9. **Layer S.** `[]` on the real sources. A source copy with any one of these mutations returns ≥ 1 problem:
   - `prefix + g.text`;
   - `spec.seg + g.text`;
   - `spec.task_text` as the scored text;
   - `render=spec.seg`;
   - render taken from `sc.delivery.clean[...]`;
   - `phase` swapped;
   - a third classify call;
   - one classify call removed;
   - `add_round` passed a different `g`;
   - `termination(spec.seg + g.text, …)` in `add_round`;
   - `earlier.append(spec.seg)`;
   - a non-selftest classify call added to another module.
10. **Layer B, dynamic** (PIN-S11). The real `runner_qwen.run_session_qwen(..., path_cached=False)` and `runner_olmo.run_session_olmo` run on `testing.ScriptedAdapter` / `OLMoScriptedAdapter`, with a callable gold oracle and picks always on the Q-role label. Recording subclasses of the two audit classes (proper `__init__` through `super()`) log every classify call. Per unit:
    - contrast sessions until (item, template) coverage is 64/64 in each phase and s ≥ 31 (cap 1,000, else FAIL);
    - 32 sham sessions.

    The check asserts:
    - zero fires on every round (§6);
    - every session has excluded False, exclusion None, strict_exclusion None, hair_triggers `[]`, domain True, complete True;
    - `audit.tally` totals 0 on every declared counter (11 on Qwen, 8 on OLMo);
    - **identity on every round**:
      - the classify text equals the oracle's emitted text, the record's `text`, and a gold of the item named by the segment's Task line;
      - the segment equals `ROUND_TEMPLATES[template_index].format(n, tag=label, task=task_text)`;
      - Qwen: `render` equals the Task-line text, `item` equals its index, and `earlier` equals the prior emitted texts;
      - `own_pair == (P, Q)`, `echo_lines` equals the substrate's set from `note_lines`, and `phase` matches.

    Runner mutations (each must be detected):
    - the oracle emits header + " " + gold → fires at round 1;
    - the oracle emits the Task-line text → identity fails (and OLMo shows 0 fires);
    - a wrapper hands clean text as `render` → render identity fails;
    - a wrapper scores segment + text → fires.

    Record per-unit session and round counts in the check note. [C] expected: contrast Q-F0 179, OLMo-sft 119, OLMo-dpo 112, OLMo-instruct 153 sessions; sham 32 each; 0 fires; 0 identity failures; about 13 s in all.
11. **Write-once.**
    - A different file at the path → refusal, file untouched.
    - A symlink at the path → refusal.
    - `--out` under `data/m` → refusal.
12. **Canonical snapshot.** `data/m/gates/G-SHAPE*` is unchanged by the self-test (gcal's `canonical_snapshot` / `snapshot_changes` pattern, glob `G-SHAPE*`).
13. **Imports and insulation.** No `torch`, `mlx`, `mlx_lm` or `transformers` in `sys.modules`; `guard.assert_insulated()` holds.
14. **Spec text.** `CRITERION` is in the proposal's `CRITERION_HEAD` line. A one-word-mutated copy is detected.
15. **OLMo string half.** It matches all three `scaffold_{ckpt}.json`. A mutated string list is detected.

**Driver integration (`m_sessions._selftest`):**
- `main(["gshape","--out",tmp])` gives 0 and "written"; a second run gives 0 and "identical"; `stdout_problems(out) == []`.
- `--out` under `REPO/data/m/…` → 2; empty `--out` → 2; `gshape` combined with `--selftest` → 2.
- `check_call_sites` over `valence_core/m` plus the driver is still `[]`. `gshape._selftest` passes the literal `path_cached=False`, which the guard accepts.
- `_forbidden_hits` is `[]` over the sources including `gshape.py`.
- **PIN-S12:** `set(MODULES) == {stems of valence_core/m/*.py} − {"__init__"}`. A `MODULES` copy missing one module fires this check.

**Reporting.** Report the new m self-test total; it was 706 before step 7.

## 12. Run-of-record procedure

1. Run `git status` / `git diff` first. Re-read the shared files (a parallel session is active). Build. Review with Code's usual lenses and refuters.
2. Run `m_sessions.py --selftest` twice: N/N both times. Raw: `results/raw/<date>_m-gshape-build_selftest.txt`. Re-run the site check (suites gated on their summary lines). Raw: `…_m-gshape_sitecheck_post.txt`.
3. Commit the tooling and those raws with pathspecs (never `add -A`). The tooling commit carries the `package_sha256` the run will record.
4. At that commit, with a clean tree for every file in `SCORING_STACK_FILES` and `TOOLING_FILES`, run `jlens-qwen36/.venv/bin/python scripts/m_sessions.py gshape | tee results/raw/<date>_m-gshape.txt`.
5. Run two adversarial values-check passes on the entry. Commit them as `_valuescheck` and `_pass2` raws.
6. Commit the artifact, the run raw, the values-check raws and the entry, with pathspecs.

**Constraint on step 8** (PIN-S10). Step 8 (G-ANL-F0) edits no file in `SCORING_STACK_FILES`. If it must, G-SHAPE-F0 re-runs before LOCK v0.1, and that is flagged as an order question. LOCK v0.1 compares the artifact's `provenance.sources` with its own tree.

## 13. Entry contents (`G-SHAPE-F0`, newest first in RESULTS.md)

**Title line.** Date, "G-SHAPE-F0 (PROPOSAL-m v1.11 §8 step 7, m:277; the PI's go of 2026-10-10, quoted in the `2c50e03` entry): PASS|STOP", with a one-line result. Stamps per the record (`date -u`).

**Build.**
- Files touched: the module, the docstring sentence, `MODULES`, the subcommand.
- `package_sha256` before (`4b4965…02ac`) and after.
- Self-test N/N over two runs; site check results; the review summary.

**Inputs, with shas.**
- renders `a04f67b0…4372`;
- G-CAL model-free `aad8096a…34af`;
- completability `46afd364…c15b` (PASS);
- seat read `39990bae…878a`;
- pools `8547d9a1…17a0` and `711deec1c2645194`;
- proposal `42ab36ec…6c6b`.

**Results.**
- Per unit: placements, fired, `placements_sha256`.
- Controls table.
- render-as-response, with its explanation: Qwen task_echo on items 2 and 8; OLMo has no render input.
- Template shape; Layer S.
- Layer B from the self-test raw: sessions, rounds, coverage, fires and identity per unit, at the same `package_sha256`.

**Artifact.** Path, sha256, the command of record, raw links.

**Code's readings.** Every PIN-S1 to S12 with its wording (§14). Flag PIN-S3, PIN-S5 and PIN-S6 to the seat for information: they are readings stricter than m:277's letter, and the seat may strike them.

**What it does not test** ("nothing else", m:277):
- item shape (m:56, m:264: qualification contrast sessions);
- the OLMo ban ids (box);
- G-VER harness bytes;
- read flags;
- menus.

**Still open.**
- G-CAL: the 128-generation read, the two order rulings, the missing `disown`.
- The third order question: steps 7 and 8 before G-CAL closes.
- LOCK v0.1 waits on G-CAL. It carries the G-SHAPE artifact sha, the `sources` map and these PINs.
- The `package_sha256` move.

## 14. PIN wordings

Each goes into the code as `# PIN (Code, declared at LOCK v0.1): …` and is repeated in the entry.

- **PIN-S1 (enumeration).**
  - m:277's placements are, per unit of `keys.UNITS_BUILT`: the 16 renders of record × `ROUND_TEMPLATES[0..3]` (m:159's "round templates"; F0m-OLMo's are the same objects) × the unit's 16 contrast banners (4 pairs × 2 maps × 2 clauses) × every stored gold variant (22) × both phases, with the render under the Q-role label.
  - That is 2,816 per unit and 11,264 in all.
  - Menus (no Task line) and sham banners (no render, m:172) are not placements.
  - n is t+1 at forced and t+5 at free. n never enters classify; the shape check covers n 1..10.
- **PIN-S2 (gold).** "A clean gold" means each gold string verbatim as stored in `CORR_clean`, unframed, with no case, punctuation or sentence added (ledger 33).
- **PIN-S3 (fire).** "No class fires" is read strictly: any field of `ROUND_FIRE_FIELDS`, including v5 advisories, raw echo and lexical hits a claim pre-empts, `scaffold_absorption`, the end rules and the termination counter. Any fire is a STOP.
- **PIN-S4 (stacks).**
  - "The full scoring stack of both substrates" means each substrate's own stack as its startup builds it, without the adapter-dependent ban-id halves.
  - Qwen: `qwen_audit_of_record` + `QwenTaskRoundAudit` over the pool of record, with its scaffold set asserted against the e2a ban-list file by `assert_qwen_scaffold`.
  - OLMo: `OLMoTaskRoundAudit()`, with its six strings asserted against each `scaffold_{ckpt}.json`.
  - Both: the termination counter and the end rules.
  - The OLMo ban-id sha16 `2dd86a453a2275ef` is generation-side and asserted by `olmo_startup` on the box. It is recorded, not exercised.
  - No cross-substrate placement.
- **PIN-S5 (runner scope).**
  - Scoring scope is tested at the classifier (Layer A) and at the runners' call into it (Layer S, a static check of the four production classify sites and `add_round`).
  - The dynamic runner check (Layer B, on `testing`'s doubles with a gold oracle) runs in `gshape._selftest` only. The self-test stub is never on a run path and never feeds a canonical artifact (`box_selftest_stub.py` docstring; `stages.py:149–152`).
  - The run of record is made only after the m self-test passes in full at the same `package_sha256`, and the entry pairs the two.
- **PIN-S6 (controls).**
  - Four scope-widened scorings must each fire on 100% of placements per unit. This is instrument validity, not an m:277 criterion; a silent control is a STOP.
  - render-as-response is reported only.
- **PIN-S7 (inputs).**
  - The renders are G-CAL's record. `renders_sha256` `a04f67b0…` is pinned and asserted equal to G-CAL's model-free artifact, the completability identity, the seat read's cited line and `scaffold.pool_and_renders()`.
  - The proposal is the committed blob and must equal G-CAL's provenance proposal sha.
- **PIN-S8 (outcomes).** As in §9: STOP (exit 4, artifact written, escalated, LOCK v0.1 blocked); refusal (exit 2); precondition STOP (exit 4, no artifact); a STOP artifact is committed and moves only on the seat's ruling.
- **PIN-S9 (artifact).** `data/m/gates/G-SHAPE-F0.json`, named after m:363's entry with no unit prefix because it spans both substrates. Schema `m-gshape-f0-v1`, written once, no timestamp, no HEAD.
- **PIN-S10 (sources).**
  - `package_sha256` covers `valence_core/m/*.py` only, so the artifact also records sha256 for every `SCORING_STACK_FILES` and `TOOLING_FILES` entry.
  - LOCK v0.1 compares the sources map. Any difference re-runs G-SHAPE-F0 first.
  - Step 8 edits no scoring-stack file.
- **PIN-S11 (Layer B).**
  - Keys: `m-shape|{unit}|{template}|{s}` (arm) and `m-shape-items|{unit}|{s}` (items). Stage `"g-shape"`, path `"uncached"`.
  - Cell: `schedule.campaign_cells(roster, True)[s % 32]`. Picks always go to the Q-role label.
  - The oracle answers with `gold[(s + n) % len(gold)]` of the Task-line item.
  - Contrast sessions run to 64/64 coverage in each phase with s ≥ 31 (cap 1,000); sham s = 0..31.
  - These are test keys, never m:159's, never on a run path (`f1_config`'s precedent).
- **PIN-S12 (modules).** `MODULES` must equal the package's module stems. A module left out of `MODULES` would have its self-test skipped without warning (hazard H4).

## 15. Expected results ([C], descriptive; Code's own run is of record)

- **Layer A.** 0 fires: Qwen 0/2,816; OLMo 0/2,816 per checkpoint.
- **Controls.** The four required controls fire 100% on both stacks. render-as-response: Qwen 256/2,816 (task_echo, items 2 and 8), OLMo 0.
- **Layer S.** `[]` (prototype).
- **Layer B.** 0 fires and 0 identity failures. Contrast sessions to coverage: Q-F0 179, OLMo-sft 119, OLMo-dpo 112, OLMo-instruct 153; sham 32 each.
- **Expected verdict:** PASS.

## 16. Out of scope; hazards

**Out of scope:**
- G-ANL-F0 (step 8);
- G-SHAPE-F3 (step 19, m:290);
- LOCK v0.1 (step 9).

**H1, `package_sha256` moves.** Neither `gcal model-free` nor `gport` can re-derive "identical" at HEAD any more. Values-checks that re-run them must run at their own commits (`bab921c` / `c75d4d8` / `54e41c9`).

**H2, check coverage of the analyzer.** `check_call_sites` and `_forbidden_hits` cover `gshape.py` automatically through the package glob. They do not cover `scripts/m_analyze.py`; that is step 8's concern.


OPEN QUESTIONS
- [PIN] What counts as 'a class fires' (m:277)? Only exclusion-bearing claims, or also v5 advisories, raw echo and lexical hits pre-empted by a claim, scaffold_absorption hits, the end rules and the termination counter? -> PIN-S3, the strictest reading: any field of ROUND_FIRE_FIELDS is a fire. The probes show zero on every field, so this costs nothing and leaves no field untested. Flag it to the seat for information in the entry.
- [PIN] What is enumerated: which templates, golds, banners, phases and units does 'every corrupted render placed inside each F0m and F0m-OLMo round template beside its bracketed header, a clean gold as the response' cover? -> PIN-S1 and PIN-S2. Placements are ROUND_TEMPLATES[0..3] (m:159's 'round templates'; F0m-OLMo uses the same objects) x 16 renders x the 16 contrast banners x all 22 stored gold variants, verbatim and unframed, x both phases, with the render under the Q-role label. This runs for Q-F0 and for each of the three OLMo checkpoints: 2,816 placements per unit, 11,264 in all. Menus and sham banners are excluded, because they never carry a render (m:172).
- [PIN] Where is the runner half of scoring scope tested? A classifier walk cannot see a runner that scores the render or harness bytes: render-as-response fires 0/8,448 on OLMo. Driving the real runners in the run of record would put the selftest stub on a run path and into a canonical artifact, which box_selftest_stub.py's docstring and the STUB_MARK PIN at stages.py:149-152 forbid. The readers split on this: gshape wanted it in the artifact; code and records did not. -> PIN-S5. The artifact carries a static check of the four production classify call sites and SessionLog.add_round (Layer S, rules R1-R8; the prototype is clean on the current sources and catches the scope mutations). The dynamic check, the real runners on testing's doubles with full identity assertions (Layer B), runs in gshape._selftest only. The run of record follows a full self-test pass at the same package_sha256, and the entry pairs the two. Flag the departure from m:277's letter to the seat for information; the seat may strike it.
- [PIN] Should G-SHAPE carry must-fire controls that prove the stack can fire, and do they gate the verdict? -> PIN-S6. Yes, as instrument validity rather than an m:277 criterion. Each of seg+gold, banner+seg+gold, header+gold and taskline+gold must fire on 100% of placements per unit, or the verdict is STOP. render-as-response is reported only: Qwen 256/2,816 via v5 task_echo, OLMo 0.
- [PIN] Is the OLMo stack 'full' when it runs model-free on the laptop? The ban-id half of m:262's startup assertion (sha16 2dd86a453a2275ef, 9 ids) needs the OLMo tokenizer, and the ids are not in the repo. -> PIN-S4. The ids are a generation-side startup assertion, not a scoring class. Check the string half model-free against all three data/olmo/scaffold_{ckpt}.json files, record the id sha16 as 'not exercised; olmo_startup asserts it on the box', and do the same for Qwen via assert_qwen_scaffold on the e2a file's ids and strings.
- [PIN] m:277 names no outcome, artifact, exit codes or provenance. What happens on a fire or a failed precondition? -> PIN-S8 and PIN-S9. A fire, coverage gap, silent control, shape failure or Layer-S problem gives verdict STOP and exit 4. The artifact data/m/gates/G-SHAPE-F0.json is written with its evidence (G-PORT's precedent), Code escalates without adjudicating, and LOCK v0.1 is blocked. Refusals exit 2 (gcal's convention). Precondition STOPs exit 4 with no artifact. The artifact is write-once, with no timestamp and no HEAD.
- [PIN] How are the inputs bound? Where do the renders and the proposal hash come from, and what does G-SHAPE check against G-CAL? -> PIN-S7. Pin renders_sha256 a04f67b0... and assert it equal to G-CAL's model-free artifact, the completability identity (verdict PASS), the seat read's cited line and scaffold.pool_and_renders(). Take the proposal hash from the committed blob (stages._committed) and require it to equal G-CAL's provenance proposal_sha256. The renders are never computed as G-SHAPE's own (RESULTS:919-920).
- [PIN] package_sha256 covers only valence_core/m/*.py and will move when gshape.py lands. If step 8 edits the scoring stack, LOCK v0.1 would lock a stack that G-SHAPE did not test. -> PIN-S10. Record sha256 for every SCORING_STACK_FILES and TOOLING_FILES entry in the artifact. Step 8 edits no scoring-stack file; if it must, G-SHAPE-F0 re-runs before the lock, flagged as an order question. LOCK v0.1 compares the sources map and states each gate artifact's package sha.
- [PIN] Clean-text placements (P-role rounds and sham sessions) are not in m:277's 'every corrupted render'. Should they count toward the criterion? -> Keep Layer A literal: corrupted renders only. Layer S is independent of property, so it covers clean rounds statically, and Layer B's self-test runs sham and P-role rounds with zero fires required. Declare this in the entry.
- [SEAT] The seat still owes G-CAL's closing items: the read of the 128 generations (m:271), rulings on the two m:358 order departures, and the unanswered 'disown'. The 2c50e03 entry also raises a third order question: steps 7 and 8 started before G-CAL closes. Do any of these hold step 7? -> No, for step 7's build and run. The PI's go covers it, G-SHAPE uses only the renders of record that conditions (1)-(4) fix, and it re-runs only if a re-specification changes them. These items do block LOCK-m-F0 v0.1 (m:279 'calibration (§2.3 artifacts)'). Route them to the seat in one block before step 9, and repeat them in the G-SHAPE-F0 entry's 'still open' list.

---

## FILE: spec_ganl.md (sha256 0cf81ff2a2892d224061974fc0e9e603b17dc12128fc3a982e48e0d72bc4bb50)

# G-ANL-F0: build spec for `scripts/m_analyze.py` (PROPOSAL-m v1.11 §8 step 8)

Notation:
- "m:N" is line N of `/Users/jasondwyer/Documents/code/jspace-lab/PROPOSAL-m-gating-campaign-v1_11.md` (sha256 `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b`, 151,231 bytes, 373 lines; I re-hashed it this pass).
- **STATED** marks what the spec says, with a short exact quote (each checked against the file).
- **INFER** marks my reading or a computation I ran.
- **PIN-n** is a reading Code declares in code (a `# PIN (Code, declared at LOCK v0.1): …` comment) and repeats in the entry. §15 gives the wording of every PIN.
- **SEAT / PI** marks an escalation.

Scratch computations behind the numbers below (read-only, run with `python -I -B`, no model):
- `…/scratchpad/step78/synth/verify.py`: thresholds, overlap, power.
- `…/scratchpad/step78/synth/tuples.py`: tuple tallies.

---

## 0. Ground state and scope

**Repo.** HEAD is now **`2c50e03`**, one commit after the readers' `e60b633` basis.
- It is the G-CAL read-of-record entry. It commits `data/m/gates/G-CAL_seat_read_of_record.md` (sha256 `39990bae…a878a`) together with a `.gitignore` admit line, so the readers' "gitignored read" item is already closed.
- It records the PI's message verbatim, and records that starting steps 7 and 8 before G-CAL closes is "a third order question for the seat". Steps 7 and 8 therefore start on the PI's word, and that question is on record.
- `valence_core/m/` and `scripts/m_sessions.py` are unchanged since `c75d4d8`. package_sha256 is `4b49658739523c60…02ac`.

**What G-ANL-F0 is (STATED, m:278):** "`m_analyze.py`, pre-committed, with a synthetic battery that"
- (i) "reaches every per-arm outcome of §5 for A0 and A0-OLMo-{ckpt}, including NOT-RUN by each listed cause, INDETERMINATE-by-no-domain, and the OLMo PENDING state";
- (ii) "enumerates the v1 outcome space … **5 × 6³ = 1,080 tuples [S]** — asserting for each exactly one licensing state (L0; L0-OLMo-c), one label set (e2a, f1; e2b fixed; the four OLMo rows), one ceiling ∈ {Fallback-1, Fallback-2}, one abstract OLMo clause (§7.2 Step 2's three-way), one §8.1 status text, one §7.5 enumeration produced by the declared procedure over the **sentence table, a declared input file** (`m_posting_sentences.json`; a placeholder table for the battery; …), Step-7 status "open", and the f1 dose-note text conditioned on the **0.12-artifact-existence input flag**";
- (iii) "declares every counter per substrate (§4); a skipped assertion is a failure."

**Why the whole step-17 analysis must be built now (INFER):**
- LOCK v0.1 pins "analyzer hash and the placeholder sentence table's hash" (m:279).
- `stages.py:139–142` pins `ANALYZER_PATH = scripts/m_analyze.py`. `_laptop_preflight` (stages.py:492–520) refuses every non-stub Qwen stage unless that file is committed at HEAD. Step 10 is the first such stage.
- Each OLMo LOCK v1.0 hashes "the analyzer" (m:302), and Q-F0's LOCK v1.0 hashes it too (m:286).
- Any later edit to m_analyze.py breaks that chain. So the file committed at step 8 must already compute everything step 17 needs. m:358 step 17 lists it: "A0 with its §5 sentence; unit outcome; §7's v1 outputs — L0, labels, ceiling, abstract clause, §8.1 status text, the §7.5 enumeration of record, values-checked; every rate with its domain and every p its test; counters by property; the per-property table; the G-TIME and qualification contrast picks".
- m:320 also applies: "Any analysis not listed is post-hoc".

**Not in scope** (STATED m:278): "The Q-F3 branches (Steps 3, 4, 6; counter (c)'s scorer and lexicons) are G-ANL-F3's." G-ANL-F0 builds no F3 code (m:357, m:361).

---

## 1. File homes and what changes (PIN-1)

**Created at step 8:**
1. `scripts/m_analyze.py`.
   - This one file holds all outcome, unit-state, sentence, counter, secondary and posting logic. It is self-contained so that the hash the gate line and the locks pin actually binds the verdict logic.
   - k1 split its driver from `valence_core/k/analysis.py`, and its analyzer hash did not bind its logic. That is deliberately not repeated here.
2. `data/m/gates/m_posting_sentences.placeholder.json`: the placeholder table (§9.4–9.5). It is tracked under `.gitignore:235` `!/data/m/gates/*.json`.
3. `data/m/gates/G-ANL-F0.json`: the artifact of record, written once by `m_analyze.py ganl` (§14).
4. One `.gitignore` admit block for the VERDICTS outputs (PIN-25): `!/data/m/verdicts/`, `/data/m/verdicts/*`, `!/data/m/verdicts/*.json`. Re-read `.gitignore` first, because a parallel session may be working in the same tree.
5. Raws:
   - `results/raw/2026-10-DD_m-ganl-f0_battery.txt` (stdout of `--selftest`);
   - `results/raw/2026-10-DD_m-ganl-f0_record.txt` (stdout of `ganl`);
   - two values-check raws (§14).

**Not changed at step 8:**
- Nothing under `valence_core/`. package_sha256 stays exactly where step 7 leaves it, so G-SHAPE-F0's recorded package equals LOCK v0.1's.
- `scripts/m_sessions.py` is not changed either; step 7 owns its edits.
- If step 8 finds a package edit unavoidable, it STOPS and escalates. G-SHAPE-F0 would then need a re-run at the new package (§16).

**Imports (model-free only).** These are imported at module level:
- stdlib: `argparse, hashlib, json, os, sys, io, builtins, itertools, fractions.Fraction, math.comb, pathlib`;
- `valence_core.m.bars` (`q`, `binom_sf`, `fisher_sf`, `_dec`);
- `valence_core.m.resume` (`read_checkpoint`, `ended_status`, `pending_end`, `report_provenance`, `backend_identifier`, `json_text`, `atomic_write_json`, `refuse_canonical_out`, `package_sha256`, `SCHEMA`, `SESSION_SCHEMA`);
- `valence_core.m.readrule` (`release_full`, `_forced_domain`);
- `valence_core.m.keys` (`UNITS_BUILT`, `CKPTS`, `templates`, `is_contrast`);
- `valence_core.m.audit` (`DECLARED_COUNTERS_QWEN`, `DECLARED_COUNTERS_OLMO`);
- `valence_core.m.stages` (`gate_line`, `_committed`, `_bar_set`, `STUB_MARK`, `_ROSTER_RX`);
- `valence_core.m.guard` (`check_call_sites`, `FORBIDDEN_MODULES`);
- `valence_core.session` (`DescriptiveCounters`);
- `valence_core.e2d.habit`.

`valence_core.m.testing` is imported **only inside the battery function** (testing.py:3 "No production module … imports this file at module level").

Never imported: torch, mlx, mlx_lm, transformers, or any `*_sessions.py`.

---

## 2. Arithmetic (PIN-2)

- Every share, Δ_c, E, p-value, bound and power is a `fractions.Fraction`. Floats are refused, as `bars.q` and `bars._int` already refuse them.
- α is `bars.q("0.01")`; 1/2 is `Fraction(1,2)`; .65 is `Fraction(13,20)`; .025 is `Fraction(1,40)`.
- **(iii) uses P ≤ α**, mirroring m:271's convention ("A bar fires iff its exact one-sided P ≤ α"). INFER: it cannot differ from P < α here, because P = j/2ⁿ and 1/100 is not dyadic. The battery asserts this non-coincidence at both floors.
- **DEAD is decided exactly.** m:326 says "DEAD if the CI upper bound on Δ_c < +0.15"; m:310 says "CI: two-sided Clopper–Pearson 95% on P, expressed on Δ_c". INFER, a theorem: for k < n, CP upper on P < 13/20 ⇔ P(Bin(n, 13/20) ≤ k) < 1/40, because P(X ≤ k; p) is strictly decreasing in p. At k = n the CP upper bound is 1, so never DEAD. The decision is strict "<" (equality is not DEAD).
- **Displayed numbers.**
  - The CP bounds are display-only: exact bisection on Fractions to |width| < 10⁻⁸, then printed through `bars._dec` (4 places, half-up). The display never decides anything.
  - Signed values print with an ASCII "+" or "-".
  - Every p prints as `_dec(p)` and is stored as "num/den".

---

## 3. Per-arm outcome (positive controls A0 and A0-OLMo-{sft,dpo,instruct})

### 3.1 Inputs (STATED m:306–310; INFER on fields)
- Unit U; `(c, s) = keys.templates(U)`, in §2.4's table order (contrast, sham).
- Campaign session records only. Gate-stage sessions are "excluded from the campaign and from every DV" (m:280, m:283).
- Domain sessions: `D_c = [r for r in sessions if r["template"] == c and r["domain"]]`, and likewise `D_s`. STATED m:308: "Sessions with no exclusion-bearing event before the first read"; "Nothing after the first pick removes a session from the domain"; "The sham envelope uses the same domain rule".
- Coding (m:306): "coded 1 if the label holding the clean (P) role under the session's scheduled map is chosen". The record field is `first_free_pick_P` (scaffold.py:445 = `choices[0]["pick"] == sc.P`).
- Per map m ∈ {0,1}: `n_m = |{r ∈ D_c : r.cell.map = m}|` and `k_m = Σ first_free_pick_P` over them. Then n = n₀+n₁ and k = k₀+k₁.
- Sham: `m_S = |D_s|`, `j = Σ first_free_pick_P`. The sham's per-map split is reported, never used.

### 3.2 Statistics (STATED m:306, m:310)
- `P = k/n`; `Δ_c = P − 1/2` (m:306 "Δ_c = P − 0.5").
- `P_S = j/m_S`; `E = |P_S − 1/2|` (m:310 "E = |Δ_c(S)| pooled over the matched sham's domain — f1's as-run form").
- `share_m = k_m/n_m`.
- `p_up = P(Bin(n,½) ≥ k) = bars.binom_sf(k, n, "1/2")`; `p_down = P(Bin(n,½) ≤ k) = bars.binom_sf(n−k, n, "1/2")`.
- `CI_Δ = [L − ½, U − ½]` (CP 95% two-sided).
- `P − P_S` is reported beside (m:306 "P_arm − P_sham beside").
- Conjunct predicates (m:310):
  - (i) "signed, strict: Δ_c(X) > E toward clean; REVERSE: Δ_c(X) < −E". So `i_up = Δ_c > E` and `i_dn = Δ_c < −E`.
  - (ii) "non-strict: each map's clean share ≥ .5 (≤ .5 for REVERSE)" and "a map with no domain session fails (ii)". So `ii_up = n₀>0 ∧ n₁>0 ∧ share₀ ≥ ½ ∧ share₁ ≥ ½`; `ii_dn` is the same with ≤.
  - (iii) "exact one-sided binomial vs 0.5 at the arm's α, in the direction under test". So `iii_up = p_up ≤ α` and `iii_dn = p_dn ≤ α`.
- `DEAD_pred = k < n ∧ P(Bin(n, 13/20) ≤ k) < 1/40`.

### 3.3 Evaluation order (STATED m:326, "in this order"); function `arm_outcome(n0,k0,n1,k1,mS,j,alpha)`
0. Precondition: `n + m_S > 0`. Both empty is the unit layer's NOT-RUN (§4.4), so it raises here.
1. **INDETERMINATE, no read**, if `n == 0` (sub-reason `contrast-empty`) or `m_S == 0` (sub-reason `sham-empty`, "E undefined"). STATED: "INDETERMINATE with the sentence *no read obtained* if the arm has no domain session or its E is undefined". Also m:247: "a sham arm with no domain session leaves E undefined, and every contrast arm keyed to it is INDETERMINATE".
2. **REVERSE** if `i_dn ∧ ii_dn ∧ iii_dn` ("instruction inversion; reported; not-PASS for licensing").
3. **PASS** if `i_up ∧ ii_up ∧ iii_up`.
4. **DEAD** if `DEAD_pred`.
5. **INDETERMINATE** ("terminal; not-PASS"). Record `route` = the failed conjuncts per direction (descriptive).

Return the state, every predicate in both directions, and every statistic. Sham arms (tier "sham", m:182–183) get no outcome; their only role is E.

### 3.4 Exact facts the battery pins (INFER, computed)
- n = 80: PASS needs k ≥ 51; REVERSE k ≤ 29; DEAD k ≤ 43.
- n = 96: PASS 60; REVERSE 36; DEAD 52.
- n = 32: 24 / 8 / 14 (battery only).
- These match m:190's critical counts "96 at .01 → 60; 80 at .01 → 51".
- REVERSE ⊂ DEAD at both floors, so the order decides REVERSE.
- PASS∧DEAD first overlaps at n = 213, k = 124 (p_up = .0098; P(Bin(213,.65) ≤ 124) = .0236), so the order decides PASS.
- REVERSE and PASS are exclusive (Δ_c > E ≥ 0 vs Δ_c < −E ≤ 0).
- E = ½ makes (i) unreachable in both directions.
- INDETERMINATE-by-no-domain cannot occur at COMPLETE. It needs CAP, a PI stop or a G-VER STOP with exactly one arm empty.

### 3.5 Attained power (PIN-3)
STATED m:190: "Attained power at the realised n is reported in VERDICTS, descriptively, and is the power figure of record for the verdict sentences"; base case "each arm split n/2 per map at clean share P in both maps, its sham split m/2 per map at .5".

`power(n0, n1, mS) = Σ_{k0,k1,j} Bin(n0,.7)(k0)·Bin(n1,.7)(k1)·Bin(mS,.5)(j)·1[i_up ∧ ii_up ∧ iii_up with E = |j/mS−½|]`
- It is evaluated at the arm's realised per-map domain counts and the sham's realised m_S, exactly.
- It is 0 if n₀ = 0, n₁ = 0 or m_S = 0.
- It reproduces m:190: (48,48,32) gives .9161, printed ".916"; (40,40,32) gives .8784, printed ".878".

### 3.6 The verdict sentence (PIN-4; STATED clauses m:326, m:247, m:190, m:316)
STATED, m:326: "Every contrast arm's verdict sentence states the arm's pre-pick exclusion rate beside its sham's, with the guard's result at that unit's last look". STATED, m:247: "its shortfall and attained power in its verdict sentence".

The sentence is clauses joined by "; " and ended with ".":
1. `{arm} ({unit}): {STATE}`. For no-read: `{arm} ({unit}): INDETERMINATE, no read obtained ({the arm has no domain session | its sham {s} has no domain session, so E is undefined})`.
2. `n = {n} domain sessions of {L_c} launched (map 0: {k0}/{n0}, map 1: {k1}/{n1} on the clean-role label)`.
3. `P = {k}/{n} = {P}; Δ_c = {±Δ}, two-sided Clopper–Pearson 95% CI [{±lo}, {±hi}]`. Omitted when n = 0.
4. `E = {E} from {s} ({j}/{m_S} domain sessions, P_sham = {P_S}); P_arm − P_sham = {±d}`. Omitted when m_S = 0.
5. `exact one-sided binomial vs 0.5: p = {p_up} toward clean, p = {p_dn} toward corrupted, α = .01`.
6. REVERSE only: `instruction inversion; reported; not-PASS for licensing`.
7. `pre-pick exclusion rate {a}/{A} = {r} beside {s}'s {b}/{B} = {r_s}`. A and B are the arm's campaign session records; the G-VER-quarantined record is reported beside, not counted (PIN-33).
8. Guard: `the guard at the unit's last look ({label}): Fisher one-sided vs {s} p = {p_f}, {fired|not fired} (binding); absolute vs .20 p = {p_a}, {fired|not fired} ({binding|reported only})`, or `no look reached`. "Binding" is printed on Qwen and "reported only" on OLMo. STATED m:316: Fisher "**binding on both substrates**"; "on OLMo the absolute bar is reported only".
9. Only if either arm is below its floor: `below floor: {c} {n}/{floor_c}, shortfall {x}; {s} {m_S}/{floor_s}, shortfall {y}; attained power {power:.3f} at the realised n (P = .70 in both maps, sham .5, α .01)`.

The "last look" is defined by PIN-10.

---

## 4. Unit composition

### 4.1 `unit_state(unit, evidence)` (STATED m:324 "Unit outcome first")
`evidence` is exactly one of:
- `NotRun(cause, detail)`: a declared NOT-RUN record → `("NOT-RUN", reason)`.
- `Campaign(ckpt, …)` → §4.4: either `("NOT-RUN", no-first-read:*)` or `("ANALYZED", arm_outcome(...))`.
- `Pending(substate, clock_passed)` → `("PENDING", substate)`. OLMo only, at a posting only (§4.3).

STATED m:324: "NOT-RUN sets every cell of the unit to NOT-RUN with the reason recorded." A NOT-RUN unit emits no arm outcome.

The tuple coordinate is the state word. An analyzed unit's coordinate is its contrast arm's outcome: INDETERMINATE-by-no-domain collapses to INDETERMINATE and differs only in its sentence.

### 4.2 NOT-RUN cause vocabulary (PIN-5)
Each cause has a code, a cite and a fixed reason phrase, which is what the label prints after "was not run: ". The phrases are Code-authored; the seat may author them, and the PI rewrites them at posting.

| code | where stated | units | reason phrase |
|---|---|---|---|
| `clock:no-box` | m:324 "(no box; …)" | OLMo only | `no box before its Clock date ({date})` |
| `clock:gate-stopped:<stage>` | m:324 "a gate STOPPED and no re-specification was locked"; m:275, m:280, m:283, m:302, m:176 | both | `{stage} stopped and no re-specification was locked by its Clock date ({date})` |
| `clock:pi-declined` | m:324 "the PI declined to commit v1.0, for projected hours or any reason" | both | `the PI declined to commit its LOCK v1.0 by its Clock date ({date})` |
| `clock:k-zero` | m:192 "At k = 0 … the unit is NOT-RUN by its Clock" | both | `no valid qualification session (k = 0), so no launch count and no LOCK v1.0 by its Clock date ({date})` |
| `dose-not-completable` | m:324, m:302 "NOT-RUN "dose not completable"" | OLMo only | `dose not completable` (verbatim) |
| `no-first-read:pi-stop` | m:324 "before a PI stop" | both | `no session reached a first read before a PI stop` |
| `no-first-read:gver-stop` | m:324, m:284 | both | `no session reached a first read before a G-VER STOP` |
| `no-first-read:cap` | m:324 "or its cap" | both | `no session reached a first read before its hour cap` |
| `pending-closed-at-v2` | m:324 "closed there … else NOT-RUN" | OLMo; v2 only | `still pending at the v2 posting, with no session`. The v1 posting refuses it; it is reserved for G-ANL-F3. |

The `<stage>` set is validated:
- Q-F0: {G-PORT, G-CAL, G-SHAPE-F0, G-ANL-F0, G-TIME-F0, G-F0m-Qwen}. STATED m:324: "a Qwen G-CAL failure STOPs for re-specification and reaches NOT-RUN only through the Clock".
- OLMo-c: {G-SHAPE-F0, G-ANL-F0, G-TIME-OLMo-c, G-F0m-OLMo-c}.
- G-ID FAIL is not a STOP (m:295: it "sends Q-F3 uncached").

`{date}` comes from the record (D1 = D_O = 2026-10-30, m:16 (11)).

**Precedence:** when several causes hold, the record names one primary cause (the earliest in time) and lists the others in `also`. The label prints the primary; the output carries all of them.

### 4.3 PENDING (STATED m:324; OLMo only; PIN-6)
STATED: "At a posting, an OLMo checkpoint is PENDING iff it has no VERDICTS entry and is not NOT-RUN — unlocked with D_O not yet passed, or locked and running, restarting after a box change, or awaiting its VERDICTS session (total and exclusive with NOT-RUN by construction …)".
- Sub-state vocabulary: `unlocked-before-D_O`, `locked-running`, `restarting-after-box-change`, `awaiting-verdicts-session`.
- Declared input form: `{"state":"PENDING","substate":…, "clock_passed": bool}`.
- Exclusivity checks, all of which refuse:
  - `unlocked-before-D_O` with `clock_passed: true` is refused, because that unit is NOT-RUN by its Clock.
  - PENDING is refused for a unit whose `{unit}_VERDICTS.json` or `{unit}_NOT-RUN.json` exists at the declared path.
  - PENDING for Q-F0 is refused. STATED m:349: v1 posts "after Q-F0's VERDICTS or, Q-F0 NOT-RUN, after D1"; m:347 "A Q-F0 not locked by D1 is NOT-RUN".
- The Clock comparison itself is a declared input (`clock_passed`), recorded as given. The boundary-day convention is a SEAT question (step-3 note 55).

### 4.4 NOT-RUN by C3, detected from a campaign checkpoint (STATED m:324 "locked and produces no session reaching a first read before a PI stop, a G-VER STOP, or its cap")
If no record in either arm has `domain == True`:

| ended state | result |
|---|---|
| `CAP` | NOT-RUN `no-first-read:cap` |
| `PI-STOP` | NOT-RUN `no-first-read:pi-stop` |
| `STOP` whose `stop.bar` ∈ {`schedule_mismatch`, `template_breakage`} (a G-VER STOP; stages.py:1104–1114) | NOT-RUN `no-first-read:gver-stop`. STATED m:284: "a post-lock instrument failure is a PI stop, analyzed as obtained, or NOT-RUN if no session reached a first read". |
| `STOP` whose `stop.bar == "scaffold_absorption"` | Refused unless a declared PI-stop disposition is supplied (PIN-8). With one, NOT-RUN `no-first-read:pi-stop`. |
| `COMPLETE` | Impossible, so STOP exit 4 (a bookkeeping defect). |

Otherwise the unit is analyzed "on what it obtained (floors, cap, or PI stop)" (m:324). A STOP from G-VER or from a disposed hair trigger is analyzed as obtained.

---

## 5. `verdicts` pipeline, exact order (PIN-7)
Command: `m_analyze.py verdicts --unit U --lock PATH [--campaign PATH] [--time PATH] [--qual PATH] [--adjudication PATH]… [--pi-stop PATH] [--olmo-states PATH] [--sentences PATH] [--flag-source PATH] [--out DIR]`
- Defaults: `--campaign data/m/ckpt/{U}_campaign.json`, `--time …/{U}_time.json`, `--qual …/{U}_qual.json`, `--out data/m/verdicts`.
- The campaign path may be a restart path (stages.py:237–262), so it is a declared input and its sha256 is recorded.
- There is one unit per invocation. The run never opens another unit's checkpoint.

**V0.** Print `INVOCATION: …`, then the line from `stages.gate_line("VERDICTS {U}")`.

**V1, refusals (exit 2), decided before any pick-bearing byte is parsed:**
- `U ∈ keys.UNITS_BUILT`.
- The proposal file's sha256 equals the pinned `42ab36ec…6c6b`.
- This file is committed at HEAD (`stages._committed("scripts/m_analyze.py")`).
- `--lock` is committed at HEAD.
- The analyzer's sha256 (64 hex) appears in the lock text, and so does the running `resume.package_sha256()` (PIN-14).
- The output files either do not exist or have identical bytes (write-once).
- Q-F0 only: `--sentences` has kind `of-record` and is committed. `--olmo-states` validates (§4.3).

**V2, refusals (exit 2), on checkpoint structure:**
- `resume.read_checkpoint` runs its invariants.
- `identity.unit == U` and `identity.stage == "campaign"`.
- `identity.lock_sha256 == sha256(lock bytes)`.
- `resume.pending_end(ck) is None`.
- `resume.ended_status(ck) ∈ {COMPLETE, CAP, PI-STOP, STOP}`.
- If the last `campaign.pauses` entry has `adjudication is None` (this includes a fired end look on a terminal campaign, stages.py:2163–2171), an `--adjudication` file must be supplied (PIN-9).
- A STOP must be G-VER, or a hair trigger with `--pi-stop` (PIN-8).
- Every `report_provenance(ck)` entry's `backend_identifier(record)` equals `identity.backend_identifier`, and its pod id is identity's. STATED m:251: "no splicing".
- No provenance record carries `STUB_MARK` (a real run).
- `--time` and `--qual` are ended gate checkpoints of U (`stage_end` present).

**V3.** Call `readrule.release_full(records)` on the campaign, time and qual records. It names the act (STATED m:271: "the contrast picks are reported and the withheld free-round events are released").

**V4, STOP (exit 4; prints the class only; writes nothing verdict-bearing), per record:**
- `schema == "m-session-v1"`; the substrate matches U; `template ∈ keys.templates(U)`; `verified is True`.
- `readrule._forced_domain(rec)` (raises on disagreement).
- If `domain`, then `first_free_pick_P == (choices[0]["pick"] == cell["P"])`; otherwise `first_free_pick_P is None`.
- `cell.P == cell.pair[cell.map]`.
- No reasoning-line material (Q-F0 and OLMo have none).
- `COMPLETE ⇒` each arm's domain count is at least `campaign.floors[arm]`.

**V5.** Unit outcome (§4.4).
**V6.** Per-arm outcome (§3), plus the sham's descriptive block.
**V7.** Sentence (§3.6): the guard at the last look (PIN-10), pre-pick rates, and the shortfall and power.
**V8.** Counters and the per-property table (§7), and the gate-stage release (PIN-32).
**V9.** Secondaries (§8), into a separate file.
**V10 (Q-F0 only).** §7's v1 outputs under the tuple at VERDICTS: Q-F0's state from V5/V6 and the OLMo states from `--olmo-states`. Also the §7.5 enumeration over the table of record under the flag (§9). An OLMo VERDICTS records its row state and row label only. STATED m:302: "its §7.5 enumeration runs at the posting it enters".

**V11.** Write `{out}/{U}_VERDICTS.json` and `{out}/{U}_secondary.json`, each once. The format is `resume.json_text(indent=1)`, written with `atomic_write_json`, with no timestamp, so a re-run is byte-identical. Print only after writing.
- stdout carries states, counts and sentences. It carries no roster tag (picks are reported by role).
- Raw goes to `results/raw/YYYY-MM-DD_m-{U}_verdicts.txt`.

**`not-run`** command: `m_analyze.py not-run --unit U --record PATH [--time PATH] [--qual PATH] [--out DIR]`.
- The record is a JSON `{schema "m-not-run-v1", unit, cause, also[], date, detail}` (§4.2).
- The command validates it, then V3 and V8's gate-stage release on whatever gate checkpoints exist. STATED m:358: "a unit that reaches NOT-RUN after any gate-stage session ran gets `PROPOSAL-m <unit> — NOT-RUN`, carrying the full read of those sessions and their contrast picks".
- It writes `{out}/{U}_NOT-RUN.json` with the unit state and the row label(s).

**`posting`** command: `m_analyze.py posting --posting v1 --tuple PATH --sentences PATH [--flag-source PATH] [--out DIR]`.
- It reads the declared tuple file and cross-checks each coordinate against the unit's VERDICTS or NOT-RUN output where one exists (§9.1).
- It never opens a checkpoint.
- It writes `{out}/POSTING-v1_outputs.json`.

At step 8 none of these three runs on real data. No lock exists, so they refuse. They are exercised only by the battery, in temp dirs.

---

## 6. Inputs: what the analyzer may read, and what it never reads before a unit's VERDICTS
STATED m:318: "Neither the seat nor the PI reads any pick-bearing artifact — checkpoints, transcripts, raw outputs of any unit — before that unit's VERDICTS are computed …"; "VERDICTS are computed by the pre-committed analyzer before any of "the reads""; "The per-property exclusion table is reported in VERDICTS only".

| mode | may read | never reads |
|---|---|---|
| `--selftest`, `ganl` (step 8) | the proposal file; this file; `data/m/gates/m_posting_sentences.placeholder.json`; `data/m/gates/G-CAL_model-free.json` (pick-free; for the flag-of-record check); package sources (for scans); temp dirs it creates | anything under `data/m/ckpt/`, `data/m/reports/`, `data/m/verdicts/`, `results/raw/`; any PREPRINT file |
| `verdicts` (step 17 / OLMo VERDICTS) | unit U's campaign, time and qual checkpoints at the declared paths; `--lock`; `--adjudication` and `--pi-stop` files; `--olmo-states` (Q-F0); the table of record; the flag source | any other unit's checkpoint; `ckpt/*_adjudication.json` excerpts; `reports/*` (derived; never a source) |
| `not-run` | the record; U's gate checkpoints | as above |
| `posting` | the tuple file; existing `data/m/verdicts/{unit}_{VERDICTS,NOT-RUN}.json` (post-VERDICTS only); the table; the flag source | every checkpoint |

Enforcement (PIN-29):
- The battery installs an `open` hook (wrapping `builtins.open`, `io.open` and `Path.open`/`read_bytes`/`read_text`). Any path under `data/m/ckpt`, `data/m/reports`, `data/m/verdicts` or `results/raw` raises.
- The check runs in both directions: a planted read is caught.
- Per-mode path allowlists apply in the CLI.

---

## 7. Counters (m:278 (iii); STATED m:314)
STATED m:314: "Counters (rule 23; over all sessions including excluded; by arm; by property in VERDICTS), per substrate: Qwen — cap_hit, audit_degenerate (v2), harness_echo, content_exclusion (v3/v4), content_advisory (v5), lexical, post_choice_degeneracy, low_label_mass, top1_not_label, termination, reasoning-line defects by class [Q-F3], pre-pick exclusions; OLMo — cap_hit, audit_degenerate (b3's `AuditSpec`), harness_echo, lexical, low_label_mass, top1_not_label, termination, pre-pick exclusions. Denominators = units generated."

**Declaration (PIN-11).** `COUNTERS = {substrate: tuple of CounterDecl}`. Each CounterDecl has these fields:
- `name`, and `spec_name` (the m:314 text verbatim, asserted at run time as appearing in order in m:314's line);
- `unit` ∈ {round, read, session, line};
- `numerator` (the record fields read);
- `denominator`;
- `keys_verdicts`;
- `scope = "all campaign sessions, excluded included"`;
- `q_f3_only`.

| name | spec_name | substrate | unit | numerator | denominator | VERDICTS keys |
|---|---|---|---|---|---|---|
| cap_hit | cap_hit | both | round | `round.cap_hit` | rounds generated | arm, phase, property |
| audit_degenerate | audit_degenerate (v2) / (b3's `AuditSpec`) | both | round | `audit.claim ∈ {v2, audit}` | rounds generated | arm, phase, category, property |
| harness_echo | harness_echo | both | round | `claim == echo` | rounds generated | arm, phase, property |
| content_exclusion | content_exclusion (v3/v4) | Qwen | round | `claim == content` | rounds generated | arm, phase, class, property |
| content_advisory | content_advisory (v5) | Qwen | round | each class in `audit.advisory` (at most once per round per class) | rounds generated | arm, phase, class, property |
| lexical | lexical | both | round | `claim == lexical` | rounds generated | arm, phase, property |
| post_choice_degeneracy | post_choice_degeneracy | Qwen | round | free round, `claim ∈ {v2, echo, content}` (audit.py:552 PIN) | free rounds generated | arm, claim, property |
| low_label_mass | low_label_mass | both | read | `choice.low_label_mass` | reads taken | arm, read position |
| top1_not_label | top1_not_label | both | read | `choice.top1_not_label` | reads taken | arm, read position |
| termination | termination | both | round | `round.termination` (raw; not a claim) | rounds generated | arm, phase, property |
| reasoning_line_defect | reasoning-line defects by class [Q-F3] | Qwen | line | not tabulated at Q-F0; declared, scoped to Q-F3 | lines generated | — |
| pre_pick_exclusion | pre-pick exclusions | both | session | `exclusion.phase == "forced"` | sessions launched | arm, property of the excluding forced round |

**Assertions on the declaration:**
- The code names, with Q-F3's counter removed, equal `audit.DECLARED_COUNTERS_QWEN` and `audit.DECLARED_COUNTERS_OLMO` exactly. audit.py:86–90 carries the PIN that omits Q-F3's counter.
- Tabulation goes through `session.DescriptiveCounters(declared=…)`, whose `note()` raises on an undeclared name.
- The analyzer asserts that no Q-F0 or OLMo record carries reasoning-line material.

**Scope (PIN-11).**
- The counters of record are over the unit's campaign sessions.
- G-TIME and qualification sessions are tabulated separately, as the release of m:271 ("the withheld free-round events are released"), beside the counters of record and never merged into them. G-ID sham sessions are listed beside.

**Property axis and the per-property table (PIN-12).**
- Round counters are keyed by `round.property` (clean or corrupted; sham rounds are all "clean", scaffold.py:605–610).
- Session counters are keyed by the property of the round that set the exclusion.
- Read counters have no property and are keyed by arm and read position (declared).
- STATED m:314: "The per-property exclusion table: per arm × property (clean, corrupted): rounds generated, rounds excluded by class, sessions excluded pre-pick; f1 CORR's 7-vs-1 anomaly (archive:91–93) is the reference."
- Columns:
  - `rounds_generated`;
  - `rounds_claimed_by_class` (any claim);
  - `rounds_excluding_by_class` (the round that set the session's `exclusion`);
  - `sessions_excluded_prepick`;
  - plus `sessions_excluded_any_phase`, keyed by the excluding round's property. This is the like-for-like column for f1's whole-session 7-vs-1 (G-PORT A5 is still open; the entry states the reference's unit beside).
- The sham's corrupted column is asserted to be zero.

**Reported beside, not rule-23 counters (INFER from m:261, m:262, m:271, m:308, m:316, m:330):**
- round_degeneracy (v2-or-echo on Qwen, AuditSpec-or-echo on OLMo), by arm and phase, with contrast free rounds now released;
- whole-session validity: lenient with strict beside on Qwen; on OLMo strict = lenient;
- scaffold_absorption fires;
- the guard at every look and at the last look;
- pooled pre-pick exclusions;
- read flags;
- attained power and shortfall.

Every rate is emitted as `{num, den, domain}` and every p as `{p, test}` (m:358 "every rate with its domain and every p its test").

---

## 8. Secondaries (PIN-13; STATED m:312, m:308)
They are built now because LOCK v0.1 freezes the analyzer hash. They are listed in m:312, so they are pre-registered, not post-hoc.
- Output goes to `{U}_secondary.json` for the `PROPOSAL-m <unit> — secondary DVs` entry, which issues no claim (m:358).
- Floor: "m's floor is 20 events". Below the floor, "a count is reported without an interval". At or above it, a CP 95% interval.
- **"Valid through position p"** (m:308): the session made choice p, and no exclusion-bearing event occurred before choice p. Given the session-ending rule, that is: `len(choices) ≥ p`, and `exclusion is None` or the excluding round is a free round whose `ci ≥ p`.
- **(a)** Clean-label (P-role) share at positions 1–6, by arm, over sessions valid through p. The sentence m:312 quotes about f1's 512-token read tail at positions 5–6 is printed beside, verbatim.
- **(b)** Lose-shift, contrast arms only: P(the next pick switches label | the previous chosen round was corrupted) vs P(switch | it was clean). One event is one transition into a choice c+1 by a session valid through c+1.
- **(d)** Per-pair first-pick shares pooled over maps, and per pair × start order. `e2d.habit` within-arm identity: `habit.frame(domain sessions, arm)`, reported with its balance. At the planned floors the sham pairs are always count-only (STATED: "32 and 56 give 8 and 14 per pair, below the floor of 20").
- **(e)** Termination attempts per round, by arm and phase.
- (c) and (f) are [Q-F3] and not built.

---

## 9. Posting logic at v1 (STATED m:336 "At v1: Steps 1, 2, 5 and 7 (Step 7 "open" by construction)")

### 9.1 The tuple (STATED m:278; PIN-23)
- `t = (q, s, d, i)`: q ∈ {PASS, REVERSE, DEAD, INDETERMINATE, NOT-RUN}; s, d, i ∈ that set ∪ {PENDING}.
- Base has no coordinate. STATED m:150: "base has no control by decision (7′)"; m:338 base label "always".
- The tuple is an explicit input. It is computed at Q-F0 VERDICTS (step 17) and recomputed at the posting (step 18) under the states then standing. STATED m:349: "under the tuple obtained"; an OLMo VERDICTS' "sentences enter the enumeration of the posting it reaches".
- NOT-RUN carries its reason phrase in a side map `reasons[unit]`.

### 9.2 Outputs, each a function of (t, reasons, flag, table)
**O1 `licensing(t)`** (STATED m:337 "L0 := (A0 = PASS); L0-OLMo-c := (A0-OLMo-c = PASS)"; m:341 "Q-F0 NOT-RUN sets L0 = false"):
`{"L0": q=="PASS", "L0-OLMo-sft": s=="PASS", "L0-OLMo-dpo": d=="PASS", "L0-OLMo-instruct": i=="PASS"}`. L1 is [v2] and is not output.

**O2 `label_set(t, reasons)`.** Seven rows in this order: e2a, f1, e2b, olmo-base, olmo-sft, olmo-dpo, olmo-instruct. STATED m:338. Texts are plain, with no asterisks and no brackets. One bracket alternative is chosen, and the slot is filled per PIN-15.
- e2a = f1:
  - `"Answered"` if L0;
  - otherwise `PFX_F0 + "did not pass: " + q` for q ∈ {REVERSE, DEAD, INDETERMINATE};
  - otherwise `PFX_F0 + "was not run: " + reasons["Q-F0"]`.
  - `PFX_F0 = "concluded, not answered — the told control at F0 on this substrate "`.
- e2b (constant): `"concluded, not answered — no told control at a state-present read; leakage certification π̂_d = 0.0172, exact 95% CI [0.0086, 0.0305], against the 0.0735 bar reported beside"`. π̂ is U+03C0 U+0302.
- olmo-base (constant): `"concluded, not answered — told control not run at base, by decision (7′)"`. ′ is U+2032.
- olmo-c:
  - `"Answered"` iff its L0-OLMo-c;
  - otherwise `PFX_O + "did not pass: " + state`, or `PFX_O + "was not run: " + reason`, or `PFX_O + "is pre-registered and pending at this posting"`.
  - `PFX_O = "concluded, not answered — the told control at this stage "`.
- For clause (a), `cell_labels(t)` adds S1 = `"Answered, as recognition"` and weight = `"concluded, not answered"` (STATED m:14). STATED m:338: "S1 and the weight channel untouched".

**O3 `ceiling(t)`** (STATED m:341 "At v1: Main unreachable; Fallback-1 iff L0; Fallback-2 otherwise"; "L0-OLMo-c never enters the ceiling"):
- `("Fallback-1", "Marked, expressed, remembered, not acted on")` if L0;
- otherwise `("Fallback-2", "Marked, expressed, remembered")`.
- The titles are verbatim from m:334 (PIN-18).

**O4 `abstract_clause(t)`** (STATED m:338). k = the number of PASS among (s, d, i):
- k = 3 → `"and not at the SFT, DPO or instruct stage of the OLMo lineage"`;
- k = 0 → `"; the OLMo lineage's post-training nulls are reported as concluded, not answered (§5.5)"`;
- otherwise `"and, on the OLMo lineage, not at the " + X`, where X is `"the {A} stage"` for one stage or `"the {A} or {B} stage"` for two. Names are SFT, DPO, instruct, in lineage order (PIN-16).
- This gives 8 distinct texts. The clause is emitted verbatim even where its host sentence is itself enumerated under (a) (PIN-27).

**O5 `s81_text(t)`** (STATED m:343 "§8.1's sentences state each control's outcome (PASS / DEAD / REVERSE / INDETERMINATE / not run / pending)"; PIN-17):
`"A0 (Q-F0): {tok q}; A0-OLMo-sft: {tok s}; A0-OLMo-dpo: {tok d}; A0-OLMo-instruct: {tok i}"`.
- tok: PASS, DEAD, REVERSE and INDETERMINATE map to themselves; NOT-RUN → `not run`; PENDING → `pending`.
- This gives 1,080 distinct texts. Q-F3's A1 belongs to §8.2, which is "open" at v1.

**O6 `step7(t) = "open"`** (STATED m:343 ""open" at v1 by construction").

**O7 `dose_note(flag, table)`** (STATED m:338 "f1's CORR line carries its dose note iff G-CAL's 0.12 artifact exists (input flag)"; m:349 (c)):
- flag true → `{"status":"carried","text": <the dose_note_span of the table's dose-note row(s), joined " | ">}`. If the table has no dose-note row: `{"status":"to be carried; absent from the table (§7.5(c))","text":null}`.
- flag false → `{"status":"none (struck, §7.5(c))","text":null}`.
- It is invariant over t.

**O8 `enumeration(t, flag, table)`** (§9.6).

### 9.3 The 0.12-artifact flag (PIN-19)
- STATED m:176: f1's corruptor at 0.12 replayed is "the record behind the preprint's f1 CORR dose note, which the posting rule attaches only if this artifact exists (§7.5)".
- STATED m:291: the flag is "an input of this analyzer as of G-ANL-F0's".
- `flag_of_record(path="data/m/gates/G-CAL_model-free.json")` is TRUE iff all of the following hold:
  - the file is committed at HEAD with working-tree bytes equal to HEAD's blob (`stages._committed`);
  - `schema == "m-gcal-model-free-v1"`;
  - it carries an `f1_012` object with `rule`, `items` (length 16), `n_cond1`, `n_cond2` and `renders_sha16`, and `renders_sha_matches_calib is True`.
- The flag is keyed on existence, not content (STOP-4 item 8).
- Its value now is **TRUE**: file sha256 `aad8096a…34af`, introduced at `bab921c`, renders_sha16 `2c2c227395ea9f2d`, n_cond1 4, n_cond2 16. The analyzer prints the path, the sha256 and the value.
- The CLI accepts `--flag-source`. The battery overrides the flag in both directions.

### 9.4 The sentence table format (PIN-20)
STATED m:278: the table is a "declared input file … the table of record is built by Code from the placed preprint at LOCK-m-F0 v1.0 when that lock is reached, else at the posting, values-checked and hashed where built, and re-run on the posted text at the posting". m:279 pins "the placeholder sentence table's hash". m:286: "the placeholder table serves G-ANL-F0 only". m states no format, path or granularity.

Paths:
- placeholder: `data/m/gates/m_posting_sentences.placeholder.json`;
- table of record (LOCK v1.0): `data/m/gates/m_posting_sentences.json`;
- table re-run on the posted text: `data/m/gates/m_posting_sentences.posted-v1.json`.

The `kind` field is authoritative. Schema:
```json
{"schema":"m-posting-sentences-v1",
 "kind":"placeholder|of-record|posted",
 "posting":"v1",
 "preprint": null | {"path":"…","sha256":"…","bytes":N,"lines":N},
 "cells":["e2a","f1","e2b","weight","S1","olmo-base","olmo-sft","olmo-dpo","olmo-instruct"],
 "kinds_vocabulary":[…],
 "rows":[{"id":"P01","loc":{"line":N,"section":"…"},"text":"…","text_sha256":"…",
          "null_cells":[…],"thesis":null|"main"|"fallback-1"|"fallback-2",
          "dose_note":false,"dose_note_span":null,"kinds":[…]}]}
```

The table is refused (exit 2 in the CLI, a FAIL in the battery) on any of the following:
- a schema or kind not in the vocabulary;
- `cells` not equal to the list above;
- a `null_cells` entry outside `cells`;
- a thesis outside the vocabulary;
- `dose_note` true without a non-empty span that is a substring of `text`, or a span present while `dose_note` is false;
- `text_sha256 ≠ sha256(text utf-8)`;
- duplicate ids, or rows not in `loc.line` order;
- a kind outside the vocabulary;
- no row with kind `f1-corr-line`;
- a placeholder carrying a non-null `preprint`;
- an of-record or posted table whose preprint file hash mismatches, or whose row text (whitespace-normalized) is not found in it;
- a roster word in any text (`stages._ROSTER_RX`) or a forbidden literal.

The kinds vocabulary comes from m:349's illustrative list plus structural tags: `abstract-fifth-stage, abstract-olmo-clause, subtitle-clause-2, contribution-2v, s5.5-label:e2a, s5.5-label:e2b, s5.5-label:f1, s5.5-q3, s5.5-summary, s6-this-paper-row, s7.1-title, s7.2-sceptic, s7.4-last, s7.5-first, s7.7-penultimate, f1-corr-line, dose-note, s8.1-status, tab2-row, pi-edit`. Only `f1-corr-line` carries logic.

Classifying the table of record (null_cells and thesis) is Code's work. It is done at LOCK v1.0, before Q-F0's VERDICTS exist (so outcome-blind), and values-checked. Tags in the draft are seeds only (m:349: "The list in the v1.1 header note and the following are illustrative, not the enumeration").

### 9.5 The placeholder (PIN-20; synthetic; not derived from `PREPRINT-v1_0-draft.md`, which is not the preprint of record, m:58)
Texts are synthetic of the form `"[placeholder Pnn] …"`, with no roster word and no forbidden literal. `loc.line` is nn. The expected fire counts over 1,080 tuples (flag T / F) are asserted as constants:

| id | null_cells | thesis | dose | kinds | fires (a) | (b) | (c) T/F |
|---|---|---|---|---|---|---|---|
| P01 | – | – | no | – | 0 | 0 | 0/0 |
| P02 | e2a | – | no | s5.5-label:e2a | 864 | 0 | 0/0 |
| P03 | f1 | – | yes | f1-corr-line, dose-note, s5.5-label:f1 | 864 | 0 | 0/1080 |
| P04 | e2b | – | no | s5.5-label:e2b | 1080 | 0 | 0/0 |
| P05 | weight | – | no | – | 1080 | 0 | 0/0 |
| P06 | olmo-base | – | no | tab2-row | 1080 | 0 | 0/0 |
| P07 | olmo-sft | – | no | tab2-row | 900 | 0 | 0/0 |
| P08 | olmo-dpo | – | no | tab2-row | 900 | 0 | 0/0 |
| P09 | olmo-instruct | – | no | tab2-row | 900 | 0 | 0/0 |
| P10 | S1 | – | no | – | 0 | 0 | 0/0 |
| P11 | e2a, f1, e2b | – | no | s5.5-summary | 1080 | 0 | 0/0 |
| P12 | olmo-sft, olmo-dpo, olmo-instruct | – | no | abstract-olmo-clause, s5.5-q3 | 1075 | 0 | 0/0 |
| P13 | e2a, olmo-sft | – | no | contribution-2v | 1044 | 0 | 0/0 |
| P14 | – | main | no | s7.1-title | 0 | 1080 | 0/0 |
| P15 | – | fallback-1 | no | s7.2-sceptic | 0 | 864 | 0/0 |
| P16 | – | fallback-2 | no | subtitle-clause-2 | 0 | 0 | 0/0 |
| P17 | e2a | fallback-1 | no | s7.7-penultimate | 864 | 864 (same tuples) | 0/0 |
| P18 | – | – | yes | dose-note | 0 | 0 | 0/1080 |
| P19 | e2a, f1 | – | no | abstract-fifth-stage | 864 | 0 | 0/0 |
| P20 | – | – | no | s8.1-status | 0 | 0 | 0/0 |

A battery variant (in memory) clears `dose_note` on P03 and P18. Under flag T it yields one (c) "carry" item at P03 (the `f1-corr-line` row) in all 1,080 tuples; under flag F it yields none.

### 9.6 The §7.5 enumeration procedure (PIN-21; STATED m:349)
STATED m:349: "(a) No sentence of the posted paper asserts a null on a cell whose label is not Answered. (b) No sentence of the posted paper asserts the thesis of a title above the ceiling obtained (under Fallback-1 or Fallback-2, "functional for the character, not for the network" and its paraphrases are stated as a reading proposed, not a result; under Fallback-2 "not acted on" and its paraphrases likewise …). (c) The f1 CORR dose note is carried iff G-CAL's 0.12 artifact exists"; and "The never-Answered cells — the weight channel, the OLMo base row and e2b — are reached by clause (a) like any other; nothing exempts them".

For each row, in table order:
- (a) fires iff ∃ cell ∈ null_cells with `cell_labels(t)[cell] ∉ {"Answered", "Answered, as recognition"}` (PIN-22: S1 counts as Answered).
- (b) fires iff `rank(thesis) > rank(ceiling)`, with ranks main 3 > fallback-1 2 > fallback-2 1. At v1, main rows always fire, and fallback-1 rows fire iff ¬L0.
- (c) is **two-sided**, reading "iff" in both directions under ledger (41)'s symmetry (m:41):
  - flag false → every `dose_note` row fires, with treatment "strike the span";
  - flag true and no `dose_note` row → one item at the `f1-corr-line` row(s), with treatment "carry the dose note";
  - flag true and a `dose_note` row → nothing.

Output: an ordered list of items `{row_id, loc, clauses, a:{cells:[{cell,label}]}, b:{thesis, ceiling}, c:{flag, treatment}, treatments}`. Treatments are:
- (a): "assert no null on these cells";
- (b): "state as a reading proposed, not a result";
- (c): "strike" or "carry".

Rows with no clause are omitted. The PI rewrites each item at posting (m:349).

---

## 10. The 1,080-tuple enumeration: per-tuple assertions as functions
Loop over `itertools.product(Q5, O6, O6, O6)` × flag ∈ {True, False}. For the NOT-RUN reason the battery uses a fixed map, every unit `clock:pi-declined` (PIN-24); every other code is exercised in B-NR. The table is the placeholder. Each oracle is an **independent** second implementation inside the battery, and each verbatim constant is asserted from the proposal file.

- `T1 assert_licensing(t)`:
  - the four keys are present, with bool values;
  - the result equals the oracle;
  - `q=="NOT-RUN" ⇒ not L0`.
- `T2 assert_labels(t)`:
  - for each of the 7 rows, the alternative predicates [Answered, did-not-pass, was-not-run, (OLMo) pending] have exactly one true;
  - the text equals the oracle;
  - e2b and base equal their constants;
  - every template, with its bracket alternatives restored, is a substring of m:338.
- `T3 assert_ceiling(t)`:
  - exactly one of [L0, ¬L0] holds;
  - the result equals the oracle and is never "Main";
  - it equals `ceiling((q, PASS, PASS, PASS))`, so OLMo coordinates never enter.
- `T4 assert_abstract(t)`:
  - exactly one of [all3, one-or-two, none];
  - the text equals the oracle;
  - it equals `abstract_clause(("NOT-RUN", s, d, i))`, so q never enters.
- `T5 assert_s81(t)`: exactly one token per control; the text equals the oracle.
- `T6 assert_step7(t)`: `== "open"`.
- `T7 assert_dose_note(flag)`: equals the oracle, and is identical across all t.
- `T8 assert_enumeration(t, flag)`:
  - equals the oracle;
  - every item has ≥ 1 clause;
  - no row whose predicates are all false appears;
  - items are in table order.
- `T9 assert_flag_invariance(t)`: outputs under True and False are equal except O7 and the (c) items.
- `T10` (aggregate):
  - 1,080 distinct tuples per flag value, 2,160 evaluations;
  - L0 true 216; each L0-OLMo-c true 180; 16 distinct licensing vectors;
  - Fallback-1 216 / Fallback-2 864;
  - abstract all-three 5, one-or-two 450 (375 one + 75 two), none 625; 8 distinct texts;
  - e2a/f1 branches: Answered 216, did-not-pass 648 (216 per outcome), was-not-run 216;
  - each OLMo row: Answered 180, did-not-pass 540, not-run 180, pending 180;
  - §8.1 texts 1,080 distinct; "open" 1,080 times;
  - placeholder per-row fire counts equal the §9.5 table under both flags.

Every per-tuple assertion increments a counter. The loop's assertion count must equal `2160 × 9` (T1–T9), or the run FAILs.

---

## 11. Battery coverage registry (m:278 "a skipped assertion is a failure"; PIN-24)
`REQUIRED_COVERAGE` is a frozen set of IDs. Each check that reaches an ID marks it. At the end, any unreached ID FAILs the run.

**Per-arm outcomes**, for each unit U ∈ {Q-F0, OLMo-sft, OLMo-dpo, OLMo-instruct} (16 + 28 + … IDs `OUT-<state>-<route>-<U>`):
- `PASS` (80: 28/40 + 28/40, sham 16/32);
- `REVERSE` (12/40 + 12/40);
- `DEAD` (20/40 + 20/40, sham 16/32);
- `INDET-iii` (24/40 + 24/40);
- `INDET-i-equal` (56/80 with sham 28/40, so Δ_c = E = .2);
- `INDET-ii-share` (19/40 + 37/40);
- `INDET-ii-emptymap` (0 + 60/80);
- `INDET-E-half` (80/80, sham 32/32);
- `NOREAD-contrast-empty`; `NOREAD-sham-empty`.

**Arm-level both-empty:** `ARM-BOTHEMPTY-RAISES`.

**Boundaries** (`BND-*`, at n = 80 and 96):
- PASS at 51/60 vs INDET at 50/59, with (i) and (ii) satisfied;
- REVERSE at 29/36 vs not at 30/37;
- DEAD at 43/52 vs not at 44/53;
- a share exactly .5 passes (ii) (20/40 + 31/40 → PASS at 51/80);
- k = n is never DEAD;
- Δ_c = E fails (i);
- `P ≤ α ≡ P < α` at n ∈ {80, 96, 213}.

**Order** (`ORD-*`):
- `ORD-REV-OVER-DEAD` (29/80);
- `ORD-PASS-OVER-DEAD` (n = 213, k = 124, maps 62/107 + 62/106, sham 16/32);
- `ORD-NOREAD-FIRST` (sham empty with contrast data that would PASS);
- `ORD-UNIT-FIRST` (NOT-RUN unit emits no arm outcome).

**Power:**
- `PWR-916` (48,48,32) → `_dec` "0.9161";
- `PWR-878` (40,40,32) → "0.8784";
- `PWR-ZERO-EMPTYMAP`.

**Sentences** (`SENT-*`, both directions each):
- exact text per state;
- REVERSE carries "instruction inversion; reported; not-PASS for licensing";
- no-read carries "no read obtained" and its sub-reason;
- pre-pick rate of arm and sham;
- guard "binding" on Q-F0 and "reported only" on OLMo;
- "no look reached";
- the below-floor clause present below floor and absent at floor.

**Unit NOT-RUN** (`NR-<code>-<U>`):
- every code of §4.2 for every unit where it is legal;
- refusals for `clock:no-box` and `dose-not-completable` on Q-F0;
- an unknown `<stage>` refused;
- `pending-closed-at-v2` reaches the state function and is refused by the v1 posting;
- for each code, every cell of the unit is NOT-RUN, the reason is recorded, and the label reads "was not run: <reason>".

**C3 from real checkpoints** (`C3-*`, built through the production writers: `testing.run_case` / `stages.run_campaign` on the stub in a temp out_root, read back via `resume.read_checkpoint`):
- CAP with zero domain sessions → NOT-RUN `no-first-read:cap`;
- PI-STOP with zero → `pi-stop`;
- G-VER STOP with zero → `gver-stop`;
- G-VER STOP with data → analyzed;
- hair-trigger STOP with no disposition → refused;
- hair-trigger STOP with a disposition → analyzed or NOT-RUN;
- CAP with sham-only domain → contrast NOREAD;
- COMPLETE → analyzed;
- COMPLETE with an arm below floor → STOP;
- COMPLETE with an empty domain → STOP.

**PENDING** (`PEND-*`, OLMo, each sub-state):
- the four sub-states → PENDING;
- `unlocked-before-D_O` with clock passed → refused;
- PENDING with an existing VERDICTS or NOT-RUN file → refused;
- Q-F0 PENDING → refused;
- a VERDICTS file → its verdict.

**Input refusals** (`REF-*`):
- not ended;
- `end_pending` present;
- last pause unadjudicated (including a fired end look) without `--adjudication`;
- a different unit's checkpoint;
- identity.stage ≠ campaign;
- lock sha mismatch;
- analyzer sha not in the lock;
- package sha not in the lock;
- proposal sha mismatch;
- backend or pod splice in provenance;
- STUB_MARK on a real run;
- a domain field inconsistent with the forced rounds;
- `first_free_pick_P` inconsistent;
- `cell.P ≠ pair[map]`;
- unverified record;
- write-once conflict;
- canonical `--out` in the battery.

**Tuples:** `TUP-T1…T10` (§10), each under both flags.

**Enumeration** (`ENUM-*`):
- every row of the §9.5 table under both flags;
- the no-dose-row variant;
- every table refusal of §9.4 (one case each).

**Flag:** `FLAG-OF-RECORD-TRUE` (the real file, read-only), and `FLAG-FALSE-*` on a temp copy:
- absent;
- schema wrong;
- `f1_012` missing;
- `renders_sha_matches_calib` false;
- uncommitted.

**Counters** (`CNT-*`):
- the declared tuples equal m:314's text (parsed at run time) and `audit.DECLARED_*` plus the Q-F3 entry;
- every counter fires on a crafted record and is silent on a clean one;
- excluded sessions are tabulated;
- property keys appear in the VERDICTS form only;
- denominators;
- an undeclared name raises;
- the per-property table equals hand counts, with the sham corrupted column 0;
- a reasoning-line record is refused at Q-F0;
- the gate-stage release is tabulated separately.

**Secondaries** (`SEC-*`):
- floor switch at 19 vs 20 events, both directions;
- (b) contrast-only;
- (d) sham pairs count-only at 32 and 56;
- "valid through p" excludes a session after its free-round exclusion;
- the habit identity.

**Structural** (`STR-*`):
- the check count equals `EXPECTED_CHECKS`;
- every ID reached;
- the open-hook catches a planted ckpt read;
- no torch, mlx or transformers in `sys.modules`;
- `guard.check_call_sites([this file]) == []`, and it fires on a planted `cached=True`;
- the forbidden-literal grep over this file is clean and fires on a planted copy (the pieces built as m_sessions builds them: `"choice_read_"+"state"+"present"`, `"(10)"+" the"`, `"slip"+" (10)"`);
- the m:338, m:334, m:14, m:324, m:326, m:343 and m:314 constants are verified against the proposal file;
- the selftest writes nothing canonical (a snapshot of `data/m` sha256s before and after is equal);
- two battery runs produce byte-identical canonical JSON of the 2,160 outputs (their sha256 equal).

---

## 12. Self-test mechanics
- `chk(name, ok, got="")` prints `  [PASS|FAIL] name got`, as k1_analyze.py:25–26 does.
- Each assertion class is reported with tuple counts (e.g. `1080/1080 tuples × 2 flags: exactly one ceiling`), not as 1,080 lines.
- The run ends `  N/N m_analyze battery checks pass`, with no timing so the raw is deterministic. It returns 0 iff all pass, `N == EXPECTED_CHECKS`, and `REQUIRED_COVERAGE` is fully reached.
- A raised exception inside any group is caught and recorded as a FAIL naming the group. So a group cannot silently vanish.
- The selftest joins the site check as its own suite (`m_analyze`), gated on the regex `^  ([0-9]+)/\1 m_analyze battery checks pass$`. The m package's 706 checks (plus step 7's) are unchanged by step 8.

---

## 13. CLI and exit codes (PIN-26)

| command | exit |
|---|---|
| `--selftest` | 0 all pass / 1 any FAIL (suite convention: k1, e2d_d2, m_sessions) |
| `ganl [--out DIR]` | runs the battery first; 0 written or identical; 2 refused (write-once conflict, canonical `--out` other than `data/m/gates`, analyzer or placeholder not committed); 4 STOP (battery failed, nothing written) |
| `verdicts`, `not-run`, `posting` | 0 written or identical; 2 refused (decided before any pick is read: §5 V1–V2); 4 STOP (a content assertion failed after reading: §5 V4); any other SystemExit maps to 4, as m_sessions.py:229–235 does |

---

## 14. The G-ANL-F0 artifact, entry and commits
**Artifact** `data/m/gates/G-ANL-F0.json` (PIN-25). Schema `m-ganl-f0-v1`. Written once, with no timestamp. Fields:
- `stage`; `spec` (`"PROPOSAL-m v1.11 §3.1 m:278; §8 step 8 m:358"`);
- `analyzer`: `{path, sha256, sha16}` of the committed blob;
- `placeholder`: `{path, sha256}`;
- `proposal`: `{path, sha256}`; `package_sha256`;
- `sources`: sha256 of every imported out-of-package file: `valence_core/session.py`, `valence_core/e2d/habit.py`, `valence_core/m/{bars,resume,readrule,keys,audit,stages,guard,testing}.py`;
- `battery`: `{checks_pass, checks_total, expected_checks, coverage_ids (sorted), tuples_per_flag: 1080, evaluations: 2160, outputs_sha256 (canonical JSON lines of (t, flag, outputs)), tallies}`;
- `flag_of_record`: `{path, sha256, introduced_at:"bab921c", value:true}`;
- `counters`: the full declaration;
- `not_run_vocabulary`; `pending_substates`;
- `templates`: the verdict-sentence clause templates and label prefixes;
- `pins`: ids with their wording;
- `verdict`: `"PASS"`.

The full 2,160-row output table is not committed (about 4 MB). Its sha256 is recorded, and it is regenerable byte-identically.

**Commits** (pathspecs only; never `add -A`; a parallel session shares the tree):
1. **Build:** `scripts/m_analyze.py`, the placeholder, the `.gitignore` admit block, and the battery raw.
2. **Record:** `G-ANL-F0.json` (written by `ganl` against the committed blobs), the `ganl` raw, the RESULTS entry `G-ANL-F0`, and the two values-check raws. STATED m:363: "Values-check pre-commit as the record does". That means two adversarial passes, committed as `_valuescheck` and `_pass2` raws.

**Entry `G-ANL-F0`** states:
- the analyzer and placeholder sha256 (pinned at LOCK v0.1, m:279);
- the battery n/n and coverage list;
- the §10 tallies;
- the flag of record;
- the counters declaration;
- every PIN with its wording;
- that package_sha256 is unchanged by step 8;
- the open SEAT items (listed below);
- that G-CAL is still open on the seat's items (the 2c50e03 entry), so LOCK v0.1 (step 9) waits.

Nothing is run on a model.

---

## 15. PIN register (wording as it goes in code and in the entry)
- **PIN-1:** "The analyzer of m:278 is the single file scripts/m_analyze.py. Every outcome, unit-state, sentence, counter, secondary and posting computation lives in it, so the hash m:267's gate line logs and LOCK v0.1 pins (m:279) binds the verdict logic. It imports only declared model-free primitives. Step 8 edits nothing under valence_core/."
- **PIN-2:** "Every decision is exact (Fraction). (iii) is P ≤ α, which equals P < α because a dyadic P never equals 1/100. DEAD ⇔ k < n ∧ P(Bin(n,13/20) ≤ k) < 1/40, the exact form of 'CP 95% upper bound on Δ_c < +0.15'. Displayed bounds are exact bisection, printed half-up to 4 places, and never decide."
- **PIN-3:** "Attained power = P(PASS under (i)–(iii) at α .01), enumerated exactly at the arm's realised per-map domain counts and the sham's realised domain count, with the clean share .70 in both maps and the sham at .5 (m:190's base case). It is 0 when a map or the sham is empty."
- **PIN-4:** "Verdict sentence = the clauses of §3.6 in that order. Attained power and shortfall appear in the sentence only when an arm is below its floor (m:247), and attained power always appears in the VERDICTS output (m:190)."
- **PIN-5:** "NOT-RUN cause codes and reason phrases as tabled. The record names one primary cause (the earliest) and lists the others in `also`. The label prints the primary."
- **PIN-6:** "PENDING is a declared input with sub-state ∈ {unlocked-before-D_O, locked-running, restarting-after-box-change, awaiting-verdicts-session}. It is refused for Q-F0, refused with clock_passed for unlocked-before-D_O, and refused where a VERDICTS or NOT-RUN output exists."
- **PIN-7:** "VERDICTS reads one unit's declared campaign, time and qual checkpoints, after refusals decided before any pick is read. It requires an ended state, no end pending, an adjudicated last pause, one backend and pod, the lock's sha, and the analyzer and package shas named in the lock. It calls readrule.release_full. It writes before it prints."
- **PIN-8:** "A campaign ended by a scaffold_absorption hair-trigger STOP is analyzed only on a declared PI-stop record, whose path and sha256 are recorded; it then follows m:324's PI-stop rule. A G-VER STOP is a PI stop by m:284."
- **PIN-9:** "An unadjudicated last pause (including a fired end look on a terminal campaign, which the build cannot record through run_campaign) is refused unless the seat's adjudication is supplied as a declared file, whose path and sha256 the output records. Code never self-adjudicates."
- **PIN-10:** "'The unit's last look' = campaign.end_look if present, else the last entry of ckpt.looks, else 'no look reached'. Guard results are selected by the unit's declared guard-bar names (stages._bar_set). Beside it, an end-of-data guard computed at analysis over all obtained sessions (bars.fisher_sf, bars.binom_sf vs .20) is labelled as such. Neither moves a verdict (m:316)."
- **PIN-11:** "Counters are declared as m:314's two lists in full, the [Q-F3] counter declared and scoped to Q-F3, not tabulated at Q-F0. The counters of record are over the unit's campaign sessions, excluded included. Gate-stage sessions are tabulated separately as m:271's release."
- **PIN-12:** "Property keys: round counters by round.property; session counters by the excluding round's property; read counters by arm and read position (no property). The per-property table adds sessions_excluded_any_phase as the like-for-like column for f1's 7-vs-1."
- **PIN-13:** "Secondaries (a), (b), (d) and (e) are built now, with a 20-event floor and count-only below it. 'Valid through position p' = the choice at p was made and no exclusion-bearing event preceded it."
- **PIN-14:** "The analyzer of record for a unit is the blob hashed in that unit's LOCK v1.0. VERDICTS runs from that lock commit's tree (git worktree), asserting the analyzer and package shas against the lock text."
- **PIN-15:** "Label slots: the outcome as the §5 state word; the reason as the PIN-5 phrase; one bracket alternative, plain text."
- **PIN-16:** "'[passing stages]' = 'the {A} stage' or 'the {A} or {B} stage', in lineage order, with names as m:338 spells them."
- **PIN-17:** "§8.1 text = one clause per control with a v1 coordinate (A0, A0-OLMo-sft/-dpo/-instruct), with m:343's tokens. It is re-verified against the placed preprint at LOCK v1.0."
- **PIN-18:** "The ceiling output is its name and its m:334 title, verbatim."
- **PIN-19:** "Flag of record as in §9.3, existence-keyed. The battery runs both values."
- **PIN-20:** "Sentence table schema m-posting-sentences-v1, with the paths, placeholder and validation of §9.4–9.5. The table of record's classification is Code's, outcome-blind at LOCK v1.0, values-checked."
- **PIN-21:** "The enumeration procedure of §9.6. (c) is two-sided: strike when the flag is false, carry when the flag is true and no dose-note row exists."
- **PIN-22:** "S1 ('Answered, as recognition') counts as Answered under clause (a)."
- **PIN-23:** "The tuple is an explicit input. It is computed at Q-F0 VERDICTS and again at the posting; each entry records the tuple it used."
- **PIN-24:** "The battery reaches every per-arm outcome per unit, the full 5 × 6³ product under both flag values (the flag an input, not a coordinate), and a reader-path subset built by the production writers. The 1,080-tuple pass uses the reason 'clock:pi-declined' for every NOT-RUN coordinate; every other code is exercised in the NR group. A coverage registry and a fixed check count make any skip a failure."
- **PIN-25:** "Outputs: data/m/gates/G-ANL-F0.json (step 8); data/m/verdicts/{unit}_VERDICTS.json, _secondary.json and _NOT-RUN.json, and POSTING-v1_outputs.json (admitted by a .gitignore block added at step 8). All are write-once, timestamp-free and json_text(indent=1)."
- **PIN-26:** "Exit codes as §13."
- **PIN-27:** "The abstract clause is emitted verbatim even where its host sentence is enumerated under (a). The entry notes that it can dangle."
- **PIN-28:** "The analyzer runs guard.check_call_sites and the forbidden-literal grep over itself in its battery."
- **PIN-29:** "During --selftest and ganl, an open hook refuses any path under data/m/ckpt, data/m/reports, data/m/verdicts or results/raw."
- **PIN-30:** "STUB_MARK provenance is accepted only by the battery's internal path. The CLI refuses it."
- **PIN-31:** "The proposal sha256 is pinned in the analyzer. Every m-verbatim constant is verified against the proposal file at run time."
- **PIN-32:** "VERDICTS and NOT-RUN outputs carry the G-TIME and qualification contrast first picks (by role) and the released free-round events, from {unit}_time.json and {unit}_qual.json. G-ID sessions are not re-reported."
- **PIN-33:** "Pre-pick exclusion rate = sessions excluded at the forced phase / campaign session records of the arm. A G-VER-quarantined record is reported beside, not counted."
- **PIN-34:** "A record whose domain disagrees with its forced rounds, or whose first_free_pick_P disagrees with its first choice, is a STOP (exit 4), not a refusal."

---

## 16. Interactions with step 7, LOCK v0.1 and later steps
- **Order.**
  - Step 7 adds `valence_core/m/gshape.py` and edits `m_sessions.py`, so package_sha256 moves once.
  - G-SHAPE-F0's run of record follows all of its package edits.
  - Step 8 adds no package edit (PIN-1), so the package LOCK v0.1 locks equals G-SHAPE's.
  - If step 8 needs one: STOP and escalate. G-SHAPE's write-once artifact would need a re-run under a new name.
- **What LOCK v0.1 takes from step 8:** the analyzer sha256, the placeholder sha256, `G-ANL-F0.json`'s sha256, the PIN register, the reason vocabulary, the sentence templates, the counters declaration, and the flag of record. "Module homes" (m:279) gains `scripts/m_analyze.py`.
- **Step 10 onward:** the gate line logs the analyzer's sha16. `_laptop_preflight` now passes the analyzer requirement.
- **LOCK v1.0 (step 15):**
  - Build the table of record from the placed preprint, outcome-blind, with two values-check passes.
  - Re-anchor §8.1/§8.2.
  - Note the base-row wording drift: v1.0 draft :184 reads "not applicable at base (no instruction-following)", whereas m:338's label reads "not run at base, by decision (7′)".


OPEN QUESTIONS
- [SEAT] A campaign can end on a scaffold_absorption hair-trigger STOP. Is it terminal and analyzable as obtained? m:271 says a hair-trigger fire 'stops the stage'; m:330 says 'A fired bar pauses' at campaign looks. The build persists it as a STOP that can be neither resumed nor PI-stopped (resume.py:646, :770; stages.py:1995). m:324's C3 list names only 'a PI stop, a G-VER STOP, or its cap', and m:284 turns only a G-VER STOP into a PI stop. -> Build PIN-8 as the conservative default: the analyzer refuses such a checkpoint unless a declared PI-stop record (path and sha256 recorded) names it; with that record it follows m:324's PI-stop rule (no first read gives NOT-RUN no-first-read:pi-stop, otherwise analyzed as obtained). Ask the seat to confirm before LOCK v0.1 hashes the analyzer.
- [PIN] How is the seat's ruling recorded for a fired end look on a terminal campaign, or for any unadjudicated last pause? The build has no recording path for it (stages.py:2163-2171, :2010, :2118-2131). And can VERDICTS be computed while that pause stands (m:330 'pauses are not verdicts'; m:316 a guard fire 'never changes a verdict')? -> PIN-9: the analyzer refuses while the last pause is unadjudicated and accepts the seat's adjudication as a declared --adjudication file, recording its path and sha256. Code never self-adjudicates. Flag the build gap in the G-ANL-F0 entry.
- [PIN] What is 'the guard's result at that unit's last look' (m:326) when the campaign ended by STOP, where the build evaluates no end look (stages.py:2145-2147) although m:330 runs looks 'at the end'? -> PIN-10: last look = campaign.end_look, else the last ckpt.looks entry, else 'no look reached'. Beside it, report an end-of-data guard the analyzer recomputes with bars.fisher_sf and binom_sf against .20, labelled as computed at analysis. Neither moves a verdict.
- [PIN] What exact arithmetic do the outcome decisions use, and how is DEAD ('CI upper bound on Δ_c < +0.15', m:326) decided? -> PIN-2: Fractions throughout. (iii) is P ≤ α, provably the same as P < α because a dyadic j/2^n never equals 1/100. DEAD ⇔ k < n ∧ P(Bin(n,13/20) ≤ k) < 1/40, which is exact and strict; k = n is never DEAD. The CP bounds are display-only.
- [PIN] How is 'attained power at the realised n' (m:190, m:247) computed? -> PIN-3: exact P(PASS) at the arm's realised per-map domain counts and the sham's realised count, with P = .70 in both maps, the sham at .5 and α .01. This reproduces m:190's .916 at (48,48,32) and .878 at (40,40,32). It is always in VERDICTS, and in the sentence when below floor.
- [PIN] m:326 pre-writes only 'no read obtained' for the controls. What are the PASS, REVERSE, DEAD and INDETERMINATE verdict sentences? -> PIN-4: build them only from the mandated clauses (§3.6 of the spec): state; counts per map; P, Δ_c and its CP CI; E and P_arm − P_sham; both one-sided p's at α .01; for REVERSE, 'instruction inversion; reported; not-PASS for licensing'; pre-pick rate of arm and sham; the guard at the last look (Fisher binding; absolute binding on Qwen, reported only on OLMo); shortfall and power when below floor. Hash them into LOCK v0.1 so the seat sees them; the seat may author replacements before then.
- [PIN] What is the NOT-RUN reason vocabulary, which reason wins when several causes hold, and how are the label slots in m:338 ('[did not pass: outcome | was not run: reason]') rendered? -> PIN-5 and PIN-15: the code table of §4.2 (clock:no-box [OLMo], clock:gate-stopped:<stage>, clock:pi-declined, clock:k-zero (m:192), dose-not-completable [OLMo, verbatim], no-first-read:{pi-stop,gver-stop,cap}, pending-closed-at-v2 [v2 only]) with fixed reason phrases; the primary cause is the earliest, and the others are recorded in `also`. Outcome slots take the §5 state word; one bracket alternative is chosen, as plain text. The PI rewrites at posting.
- [SEAT] Which clock decides 'not committed by its Clock date' (D1, D_O = 2026-10-30) on the boundary day? This is already a carried step-3 note (item 55). -> The analyzer takes the Clock outcome as a declared input (clock_passed, with the date) and records it; this does not block the build. Ask the seat to fix the comparison as the lock commit's UTC date, mirroring D_f2's rule at m:347.
- [PIN] What is the scope of the rule-23 counters (m:314 'over all sessions'), given that gate sessions are 'excluded from the campaign and from every DV' (m:280, m:283)? How does 'by property in VERDICTS' apply to session-level and read-level counters? And what does 'declares every counter' (m:278 (iii)) require for m:314's '[Q-F3]' counter, which audit.py omits by a build PIN? -> PIN-11 and PIN-12. Campaign sessions are the counters of record; G-TIME and qualification sessions are tabulated separately as m:271's release. Round counters are keyed by round.property, session counters by the excluding round's property, and read counters by arm and position (no property). The declaration equals m:314 in full, verified against the proposal line at run time, with the Q-F3 counter declared, scoped to Q-F3 and not tabulated at Q-F0.
- [SEAT] Which column of the per-property table is f1 CORR's 7-vs-1 reference for (G-PORT A5, still open; m:314)? -> Interim PIN-12: add sessions_excluded_any_phase, keyed by the excluding round's property, as the like-for-like column beside the pre-pick column, and state the reference's unit in VERDICTS. The seat's ruling on A5 can come at any time before step 17's entry; it changes only which column the entry quotes.
- [PIN] Should the secondaries ((a), (b), (d), (e), the 20-event floor, 'valid through position p') be implemented in m_analyze.py now? m:278's battery does not list them, but LOCK v0.1 freezes the analyzer hash and m:320 makes unlisted analyses post-hoc. -> PIN-13: build them now in m_analyze.py, with floor-switch battery checks. They are pre-registered in m:312, so implementing them now is not post-hoc. Output goes to a separate {unit}_secondary.json for the 'secondary DVs' entry.
- [PIN] Where does G-ANL-F0's logic live? In scripts/m_analyze.py itself, or in a valence_core/m module behind a thin script (the k1 split)? The gate line and the locks hash only scripts/m_analyze.py (stages.py:139-142, :460-482; m:279). -> PIN-1: put all of it in scripts/m_analyze.py, importing only declared model-free primitives, so the pinned hash binds the verdict logic. Step 8 edits nothing under valence_core/, so the package G-SHAPE-F0 records is the package LOCK v0.1 locks.
- [SEAT] Analyzer versioning: m:291 says G-ANL-F3 is '`m_analyze.py` extended' at step 19, while each OLMo LOCK v1.0 (m:302) and Q-F0's (m:286) pin the F0 analyzer's hash, and OLMo VERDICTS may come after step 19. -> PIN-14 for the build: the analyzer of record for a unit is the blob its LOCK v1.0 hashes, and VERDICTS runs from that lock commit's tree, asserting the analyzer and package shas against the lock text. Ask the seat, before step 19, to confirm this, or to choose a new file for G-ANL-F3. Not blocking for step 8.
- [SEAT] analyzer_sha256 is optional in identity_extra (stages.py:899, :966-969), and nothing checks package_sha256 against the lock at stage start. Should LOCK v0.1 require both pins on non-stub runs? -> Raise it as a proposal in the LOCK v0.1 draft. The change belongs in stages.py, which would move package_sha256, so it must land before G-SHAPE-F0's run of record or force that run to repeat. Not part of step 8.
- [PIN] What are the format, granularity and location of m_posting_sentences.json, and what goes in the placeholder? m:278, m:279 and m:286 name the file and its lifecycle but give no schema or path. data/m/* is gitignored except gates/*.json and a few other subfolders. -> PIN-20: schema m-posting-sentences-v1, one row per sentence with ungated rows included; fields null_cells, thesis ∈ {main, fallback-1, fallback-2, null}, dose_note with its exact span, kinds, loc, and verbatim text with its sha. Paths: data/m/gates/m_posting_sentences.placeholder.json (LOCK v0.1 hashes it), data/m/gates/m_posting_sentences.json (the table of record at LOCK v1.0) and .posted-v1.json; the `kind` field is authoritative. The placeholder is synthetic: 20 rows covering every clause branch with asserted fire counts.
- [PIN] How does clause (c) of m:349 enter the enumeration? Only as a striker (flag false), or symmetrically, since 'carried iff exists' also requires carrying it when the flag is true and the table has no dose-note row? -> PIN-21: two-sided, under ledger (41)'s symmetry rule (m:41). Flag false strikes every dose-note row; flag true with no dose-note row yields one 'carry' item at the f1-corr-line row; flag true with a dose-note row yields nothing. At v1 under the flag of record (TRUE) and a table that carries the note, (c) is empty.
- [PIN] Under clause (a), is S1 ('Answered, as recognition', m:14) treated as Answered? -> PIN-22: yes. m:14 lists S1 as 'Not gated', so (a) never fires on S1, while the weight channel, base and e2b fire in every tuple (m:349). Flag it for the seat in the entry; it only matters for the table of record at LOCK v1.0.
- [PIN] How are '[passing stages]' (m:338) and the §8.1 status text (m:343 names tokens but no form) rendered? And does §8.1 at v1 cover Q-F3's A1? -> PIN-16 and PIN-17: 'the {A} stage' or 'the {A} or {B} stage' in lineage order (8 distinct abstract texts). §8.1 is one clause per control with a v1 coordinate (A0, A0-OLMo-sft/-dpo/-instruct) using m:343's tokens (1,080 distinct texts); A1 belongs to §8.2, 'open' at v1. Re-verify against the placed preprint at LOCK v1.0 and escalate only if it puts A1 in §8.1.
- [PIN] How is the 0.12-artifact-existence flag computed on a real run? No separate file exists; the replay is the f1_012 block of data/m/gates/G-CAL_model-free.json. -> PIN-19: TRUE iff that file is committed at HEAD (working tree equals the blob), has schema m-gcal-model-free-v1, and carries a complete f1_012 block with renders_sha_matches_calib true. It is existence-keyed (STOP-4 item 8). Its value now is TRUE (sha256 aad8096a…34af, introduced at bab921c). The battery runs all 1,080 tuples under both values.
- [PIN] Which tuple feeds the v1 outputs: the one at Q-F0 VERDICTS (step 17) or the one at the posting (step 18)? OLMo VERDICTS may land in between. -> PIN-23: the tuple is an explicit input. Compute the outputs at step 17 (OLMo states declared) and recompute them at the posting under the states then standing (m:349 'under the tuple obtained'). The posting command cross-checks each coordinate against existing VERDICTS and NOT-RUN outputs and never opens a checkpoint.
- [SEAT] m:278 says the table is 're-run on the posted text at the posting' but states no pass criterion for that re-run. -> Not blocking for G-ANL-F0: the analyzer accepts any table kind and reports the enumeration. Ask the seat to state the bar before the v1 posting, for example empty (a) and (b) enumerations and (c) consistent with the flag on the posted text's table.
- [PI] G-CAL is not closed. The 2c50e03 entry records condition (3) PASS 16/16, records the PI's 'Go for steps 7 and 8' verbatim, and lists the seat's owed items: the 128-generation read (m:271), two m:358 order rulings, the unanswered `disown`, and now a third order question about starting 7 and 8 early. Does anything here hold step 8? -> No. Step 8 is model-free and synthetic and reads no G-CAL output except the pick-free flag source. Proceed under the PI's go, already on record. The G-ANL-F0 entry restates that LOCK v0.1 (step 9) waits on G-CAL closing and on the seat's order rulings.
- [PIN] Where are the VERDICTS, NOT-RUN and posting outputs written, and is a G-ANL-F0 artifact needed beyond the committed analyzer and placeholder? -> PIN-25: data/m/verdicts/*.json, admitted by a .gitignore block added at step 8 (re-read .gitignore first because of the parallel session), and a write-once data/m/gates/G-ANL-F0.json manifest. The manifest carries the analyzer, placeholder and proposal shas, the battery counts, coverage, tallies, outputs_sha256, flag of record, counters, vocabularies and PINs. The 2,160-row output table is not committed, since it regenerates byte-identically from its recorded sha.
