# m package — BUILD (OLMo): the blind code review and Code's dispositions (2026-11-06)

*Code's raw. One blind reviewer (a general-purpose agent with no access to Code's reasoning) read the uncommitted diff of `valence_core/m/gcal.py`, `valence_core/m/resume.py` and `scripts/m_sessions.py` against HEAD `dc1ffe1`, with the governing texts: the seat's prebuild answers §0, Q2 and Q6; m:176; m:302; the carry-overs' sources; and the unchanged stage machinery. It worked read-only. The report is reproduced verbatim except that the session scratch path is shown as `<scratch>/`. Code re-checked every finding at its source before applying it (§2). Every finding is applied or disclosed, and the self-test of record ran after the last edit.*

## 1. The report (verbatim, the scratch path replaced)

Line numbers are for the working tree as it stood at 03:09. The tree changed twice while I was reviewing (a resume.py comment at 02:33, and the `who` wording of m_sessions' `--out` refusal at 02:35). Both changes are covered below. I edited nothing in the repo; my scratch files are under `<scratch>/olmo_review/`.

**Findings**

1. **gcal.py:897–940 (`_load_ckpt`) and :1126 — SPEC, bug-grade. G-CAL-OLMo can be resumed across pods, splicing generations from two boxes.**
   - The pod id goes into the provenance entry only. Nothing compares it on `--resume`.
   - The identity's `backend_identifier` drops `path` and `seed`. Two pods of the same GPU class and image therefore produce the same identifier, and the resume is accepted.
   - Scenario: pod A writes 70 of 128 generations and is pre-empted. On pod B (also an A100), `gcal completability --unit OLMo-sft --resume` passes the precheck, finds no identity diff, and generates the other 58. The artifact mixes two boxes.
   - This contradicts m:267 ("interrupted by a pod change, it restarts from its first session on the new box") and CLAUDE.md's consistency clause. resume.load_or_init implements the restart for stages via `pod_id_seen`; G-CAL-OLMo has no equivalent.
   - Fix: on OLMo, refuse `--resume` (or set the checkpoint aside and restart) when the pod id recorded by the record-bearing provenance entries differs from `pod_id()`. Still allow a re-derivation that generates nothing.

2. **m_sessions.py:848–862 (`stage_identity_extra`, OLMo branch) — SPEC. G-F0m-OLMo runs under LOCK-m-OLMo-{ckpt} v0.1.**
   - The branch requires only the proposal sha256 and the weights sha256 in the lock text. v0.1 must already carry both for G-TIME-OLMo.
   - Nothing in the driver or in stages (`prior_gate` allows a prior under an earlier lock) checks for v0.2. m:302 orders G-TIME-OLMo → LOCK v0.2 (acceptance; projections) → G-F0m-OLMo.
   - Q-F0's precedent refused v0.1's blob at qual, by requiring `path = uncached`, the revision and the model id in the lock.
   - Scenario: after G-TIME-OLMo-sft passes, `qual --unit OLMo-sft` runs 24 sessions before v0.2 is committed.
   - Fix: declare a v0.2-only line form for the OLMo qual and require it, or keep the OLMo qual refused until v0.2 is written (Q-F0's step-14 precedent).

3. **m_sessions.py:1186–1189 (RM4-1) with :1500–1526 — BUG. The RM4-1 note can never print on the Qwen or box path.**
   - On those paths the RULING line prints only after `stage_precheck` passes.
   - Every state where the note applies is refused by `campaign_ruling_problems` first: the last pause already adjudicated (NO PAUSE TO ADJUDICATE), a reuse (RULING REUSED), a pending end (O4-1), or an ended campaign. I confirmed this on synthetic scratch states.
   - So the note appears only on the stub path. Two texts are false in production as a result:
     - the help and module-docstring sentence "the RULING line notes an adjudication the checkpoint already records";
     - O4-1's message for an adjudication that is already recorded ("it would not apply the seat's adjudication … then offer a ruling"). That adjudication actually needs nothing.
   - Fix: print the RULING line (or the note) before the REFUSED line, or add "already recorded (sha16 …): needs nothing" to those three refusals; correct the sentence.

4. **m_sessions.py:6556, 6603–6610, 6658–6678, 6818–6831 against 6949+ — TEST-WEAKENING (vacuous). The OLMo wiring runs come after every stdout scan.**
   - Affected runs: G-TIME-OLMo-sft and G-F0m-OLMo-sft through `_run_stage`, the box-path runs, and the prior-adjudication runs.
   - Every scan of stdout and of the ruling texts runs before them: the pick/roster/menu check, the line-form and no-clock whitelist, the ruling-texts-printed-nowhere check, and the PROVENANCE-origin check (`prov_spy` is closed at 6824).
   - The new whitelist regexes (G-TIME-OLMo/G-F0m-OLMo BAR and STAGE lines, the WEIGHTS line) are therefore never exercised. The prior-adjudication text is never checked for non-printing. Only the two stderr checks at 7181 and 7187 cover these runs.
   - The design note (§5) claims these lines are in the scan.
   - Fix: move the OLMo block before line 6554 (`n_outs_c_end`), or re-run the scans over its outputs; add the prior-adjudication file's token to `rul_tok`.

5. **m_sessions.py:5998–6009 (`mq`) — TEST-WEAKENING (coverage gap). Neither new refusal is tested end to end on the Qwen path.**
   - RULING BESIDE AN END PENDING and RULING REUSED have no check of exit 2, "ruling: …" in the REFUSED line, and nothing loaded or created. The 70-case mirror calls `campaign_ruling_problems` directly and runs the stage on the stub.
   - The pre-load refusal is the whole point of O4-1 ("it would save the 27B load"), and it is untested.
   - Fix: add `time_qwen(..., cmd="campaign")` cases: `c_pending` with `adj_f`, and `b_2p` with `adj_f` and `--resume`.

6. **NIT (docs; item 4) — docstrings not rewritten and now false:**
   - `stage_precheck` docstring, 1225–1229 ("…the stage making each again after the load") and 1236–1242 ("Not made here: … NOT APPLIED … the precheck lets it through").
   - `campaign_ruling_problems` docstring, 1073: "the refusals stages.run_campaign makes". O4-1 and O1-3 are not among them.
   - `ruling_line`, 1161–1166, and module docstring 116–119: a ruling beside an end pending "stand[s] on the RULING line alone". On the Qwen path it is now refused before any RULING line, so its sha16 is printed nowhere.
   - Module docstring:
     - 205–207: OLMo time and qual "refuse (exit 2)";
     - 62–72: gcal completability lacks `--unit`;
     - 87–89: no OLMo units and no `--prior-adjudication-file`;
     - 209: "No stage runs on a model at step 4".
   - Comment 542–544: "The OLMo units keep the step-9 track's refusal".
   - Argparse description at 7237: no OLMo stages.

7. **m_sessions.py:1110–1127 — NIT. O4-1 fires slightly more widely than the stage's NOT APPLIED.**
   - On a pending checkpoint whose design, licence, prior or floors differ, the stage never reaches `_refinish_campaign`; it STOPs on CHECKPOINT MISMATCH.
   - The precheck still says RULING BESIDE AN END PENDING and advises a re-run that will then STOP after the load.
   - On checkpoints the stage would re-finish, the match is exact.

8. **m_sessions.py:679–714 (`olmo_weights_problems`) — NIT.**
   - A KeyError traceback (exit 1) if a manifest entry lacks `files`, or a file entry lacks `bytes`.
   - `is_file()` follows symlinks, so "regular file" is not checked.
   - Extra unlisted files in the model directory are not refused. box_respawn_check refuses EXTRA files. An `adapter_config.json`, for example, would be picked up by `from_pretrained` when PEFT is installed.

9. **m_sessions.py:430–508 and the precheck/stage chain — NIT.**
   - G-CAL-OLMo, whose FAIL makes a checkpoint NOT-RUN, runs without `driver_problems()` and prints no DRIVER line (as Q-F0's G-CAL did).
   - Nothing in code requires the G-CAL-OLMo artifact to be PASS before G-TIME-OLMo, or the weights sha256 to match across G-CAL-OLMo, G-TIME-OLMo and G-F0m-OLMo. `prior_gate` compares only unit, stage and proposal. The order rests on the lock existing.

10. **gcal.py:1029–1070, tally (iv) — NIT.** It is case-sensitive, and it counts corrupted words that are ordinary English as mirroring: "on" (item 15) and "thy" (item 2). An OLMo answer containing "based on" would count. It reproduces Qwen's 11 (9 hits), but it can over- or under-count on OLMo. It is descriptive only.

11. **gcal.py:1007 — NIT.** The OLMo artifact's procedure text carries a literal `{ckpt}` and a hard-coded `2dd86a453a2275ef`, not the identity's values. Stub artifacts therefore misstate their ban ids.

12. **m_sessions.py:7065 — NIT.** `main(["time", "--unit", "OLMo-sft", "--prior-adjudication-file", …])` redirects only stderr. Its INVOCATION line, with a temp path, lands in the self-test's own stdout (the raw of record).

13. **Design note §2 item 12 — NIT.** "13 new checks (gcal 10; resume 3; driver 7)" adds up to 20.

14. **Flag for the seat — NIT.** The build reads §0's "OLMo stage wiring" as time and qual only. The OLMo campaign is refused until each checkpoint's v1.0, which means another driver edit later. The seat should confirm this reading.

**Q-F0 differences found** (item 1). All trace to Q6's carry-overs or to the package moving, so I expect they're acceptable, but they are behaviour changes:
- O4-1 and O1-3 now refuse before the load on the Q-F0 campaign path. Previously the stage re-finished and then refused NOT APPLIED (exit 4), or applied the reused text.
- The RULING line can carry the RM4-1 note (stub path only; see finding 3).
- Q-F0 STOP and REFUSED lines, and m_analyze's refusal text, now carry `TOTALS_SEALED` instead of `TOTALS_REDACTED`.
- `--prior-adjudication-file` on Q-F0 qual is now refused with a REFUSED line (exit 2). At HEAD argparse rejected it (also exit 2).
- The package hash has moved. Any Q-F0 resume, re-finish or `gcal --resume` is now refused on `package_sha256`, and the licence fails against LOCK-m-F0 v1.0.

**Checked and found correct**
- **Q-F0 G-CAL unchanged:**
  - The Qwen `completability_artifact` from data/m/ckpt/G-CAL_qwen.json equals both HEAD's and the committed artifact.
  - `_canonical`, `_paths`, `canonical_files`, `gate_line` and `key_set` equal HEAD's. I loaded HEAD's module in memory to compare.
  - Prints, the `GcalStop` text, the identity and the `who` wording are identical by reading.
- **Q-F0 driver functions:** `stage_identity_extra` (time, id, qual, campaign; real lock and another lock), `refusal` (Q-F0 and Q-F3), `campaign_ruling_problems` and `ruling_line` (on the committed Q-F0 campaign checkpoint) all equal HEAD's.
- **resume:**
  - All four committed Q-F0 checkpoints read and pass `_validated`; the Q-F0 key set is unchanged, and a Qwen identity refuses a `weights_sha256`.
  - Every OLMo identity goes through `Identity`, which always adds `weights_sha256`; `_validated` enforces the per-unit key set.
  - No committed OLMo checkpoint exists that would lack the key.
- **O4-1** equals `_refinish_campaign`'s NOT APPLIED set on well-formed checkpoints: the adjudication always; a PI stop only when none is recorded; a recorded stop passes; a different stop hits CHECKPOINT MISMATCH first.
- **O1-3** fires only for an open pause, comparing the stripped text's sha16 with the (already stripped) recorded rulings, all of which belong to earlier pauses. It runs after SCHEDULE EXHAUSTED and PI STOP REFUSED.
- **VC4-1 and VC4-2** sentences are true of the code, and the help pins appear on both help pages (I ran `--help`).
- **OLMo stage wiring:** `olmo_counts` matches the committed OLMo gate schedules and `keys.templates`' order. The precheck reads the same prior the stage reads, and `prior_gate` accepts the prior adjudication only for an OLMo qual after a PAUSE; it is recorded in the checkpoint only.
- **Refusal before any load or write:** the box path refuses before the load without a pod id or with a weights problem. The precheck, driver and weights checks are combined, and no refusal path writes under data/m.
- **G-CAL-OLMo:**
  - Banner, generation path and keys: the banner is `SESSION_BANNER` (banner.py), TEMP 0.7, STOP_CAP 60, uncached, `injections=()`, with the same 128 keys and seeds, grader and bars.
  - Startup and failure: the tokenizer probe runs before any checkpoint write and its logic is sound; the NOT-RUN wording matches m:176 and m:302; the pod id is required non-stub; FAIL exits 4.
  - The model-free artifact's proposal hash equals v1.11's.
- **Tallies (iii) and (iv)** reproduce the Qwen record on the committed artifact (I ran it): 1 termination at `CORR_corrupted i=6 s=1`; 11 mirroring, 9 of them hits.
- **Sealed totals line:** `TOTALS_SEALED` prints neither figure, and the existing needle checks still pass.
- **Existing self-test checks:** none was weakened. The `m_pend` flip and the O4-1 exception are stricter; the O1-3 exception (`not refused`) is as strong as those cases were at HEAD.
- **Self-test scaffolding:** the new self-test helpers and variables are defined in scope, and all three files compile.

## 2. Code's dispositions (each re-checked at source first)

| # | re-check | disposition |
|---|---|---|
| 1 | m:267: "a gate stage carries no pod id: interrupted by a pod change, it restarts from its first session on the new box ... and G-CAL's identity is its key set and this document's hash"; `gcal.run_completability` compared no pod | **applied.** An OLMo resume that would generate on a pod other than the one(s) its recorded generations came from is refused (POD CHANGED: move the checkpoint aside by hand and run again). A complete checkpoint re-derives its artifact anywhere. Self-test check added: 49 generations on pod A; a resume on pod B is refused with nothing generated; pod A completes; pod B then re-derives. |
| 2 | m:302: "port acceptance recorded at v0.2) → LOCK-m-OLMo-{ckpt} v0.2 (acceptance; projections) → G-F0m-OLMo"; Q-F0's QUAL_LOCK_PATH_TEXT | **applied.** `OLMO_QUAL_LOCK_LINE` = "G-TIME-OLMo-{ckpt} port acceptance recorded" must be in the governing lock's committed text at qual. Its form is Code's PIN for LOCK-m-OLMo-{ckpt} v0.2's text. Self-test: `stage_identity_extra` admits time under v0.1's text and refuses qual under it. |
| 3 | traced: on the Qwen path each state the note marks is refused before the RULING line (no OLMo campaign path exists yet) | **applied.** RM4-1's note stays on the RULING line where one prints (the stub path). O4-1's refusal now names an adjudication the checkpoint already records ("which needs nothing"). The help names the three refusals that carry the information (RULING REUSED, RULING BESIDE AN END PENDING, and NO PAUSE TO ADJUDICATE by the last pause's ruling digest). The module docstring says it appears on the RULING line where one prints, and otherwise in the pre-load refusal that meets it. `ruling_line`'s docstring records O4-1's refusal before the line. The pins are regenerated from the same sentences. |
| 4 | the block sat after `n_outs_c_end` scans | **applied.** The OLMo block now runs after the campaign's runs and before the scans (the stdout scan, the line-form and no-clock whitelist, the ruling-texts check). The prior-adjudication text carries a token, added to `rul_tok`. The design note's §5 is corrected. |
| 5 | `mq` had neither case | **applied.** Two Qwen-path cases: an adjudication beside a pending end (RULING BESIDE AN END PENDING), and an earlier pause's ruling re-offered (RULING REUSED). Each is exit 2, "ruling: …" in the REFUSED line, nothing loaded or written. |
| 6 | each text read | **applied.** The module docstring (gcal's `--unit`, the qual flag, the RULING-line sentence, the OLMo paragraph, the step-4 line); the driver's stage-constants comment; `stage_precheck`'s (completed after the values-check, its item 131: the precheck-only refusals and the four mirrored ones), `campaign_ruling_problems`' and `ruling_line`'s docstrings; the argparse description. |
| 7 | the stage's CHECKPOINT MISMATCH precedes `_refinish_campaign` | **disclosed** in O4-1's PIN. There the refusal stands where the stage would have refused anyway. |
| 8 | `olmo_weights_problems` read | **applied.** A malformed files block is a problem, not a traceback. A listed file that is a symlink is refused, and so is an unlisted file in the directory (box_respawn_check's EXTRA). Self-test cases added. |
| 9 | m:176: "before that checkpoint's G-TIME-OLMo; failure → that checkpoint NOT-RUN" | **applied.** G-CAL-OLMo's box path checks the driver and prints the DRIVER line. G-TIME-OLMo's box path refuses before the load without G-CAL-OLMo's artifact on disk, PASS, on the weights of record (`olmo_gcal_problems`). Self-test cases added. Beyond G-TIME, cross-stage weights rest on each stage's identity (`weights_sha256`) and each lock naming them; `prior_gate` does not compare them. |
| 10 | items 2 and 15's renders | **disclosed** in `olmo_tallies`' PIN. The keys are printed so the entry can name such restatements; the tally is descriptive only. |
| 11 | `completability_artifact` (OLMo) | **applied.** The procedure text names the unit's scaffold file and the identity's ban-ids sha16. |
| 12 | the call's redirections | **applied.** stdout is redirected too. |
| 13 | the design note | **applied** (21, after the values-check: gcal 11 with finding 1's pod check, resume 3, driver 7). |
| 14 | §0 and m:302 | **carried** to the seat in the BUILD entry, as the readiness reading (PIN O12). |
| Q-F0 differences | — | **disclosed** in the BUILD entry, each traced to Q6's carry-overs, to the package moving or, for the qual flag, to the OLMo wiring. Q-F0's records are complete and its campaign ended; its record stands on its own lock. |
