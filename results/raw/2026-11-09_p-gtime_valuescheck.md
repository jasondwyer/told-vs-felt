# G-TIME-OLMo (p) ×3 -- the blind values-check of the entry, the block to the seat and the run's raw

*Code's raw, PI date 2026-11-09. A blind values-check of the G-TIME entry's draft, the block to the seat
(`_p-gtime_code-to-design_read`) and the run's raw (`_p-gtime`), against HEAD `0afd842`, the stage's outputs and the
box copies. The checker hashed the checkpoints and the call logs and read nothing in them. 91 items: 81 PASS, 4
IMPRECISE, 0 FAIL, 6 NOT CHECKABLE (Code's own conduct, the pod's state, box-side events). No value was wrong. Each of
the four was applied before the commit:*

- *#9: the entry says the box precheck ran in a process that imports the driver as its `time` command does.*
- *#24: "byte-identical to the box's" now qualifies the per-checkpoint outputs alone, not the raw and the block.*
- *#68: the raw's header quotes the routing with its own characters (→, ×). The wrapper's comments, whose bytes are
  pinned, are noted in its heading as quoting in ASCII.*
- *#82: the launch call's capture (Code's session) shows the INVOCATION line alone, so the raw now reads "(no other
  line had been written yet)", followed by the capture's own "[exited with code 0]".*

*Three of the checker's optional notes were applied too: the backend identifier is said to be in each m stage report's
identity (p's reports carry none); (j) reads "the `valence_core` modules loaded in the calling process"; the raw says
where each copied file went. The fixes were checked by tool (each replaced string asserted unique), not by a second
blind pass. The report is verbatim, its local paths scrubbed (`<tmp>`) and its headings set one level down.*

## G-TIME-OLMo (p) ×3: blind values-check of the entry draft, the block to the seat and the run's raw

I checked 91 claims: **81 PASS, 4 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE**. No value I could reach is wrong. That covers:

- the 15 OUTPUTS sha256s, the three stdout sha256s, and the wrapper, bundle and sync-script hashes;
- every table cell, checked against m's and p's reports and the reads;
- the stamps: 225, 225 and 228 s;
- the backend identifier, recomputed from each run's printed provenance;
- the quotes from m:267, m:302 and `de729c4`, which are exact in the block, and the m:205 figures;
- readings (a)–(i), which equal the BUILD entry's character for character once line wrapping is removed.

I read all 30 sham responses myself, and 29 answer their task. The one that does not is sft's round 1: "4" for the wheels on a bicycle.

The four IMPRECISE items are all wording:

- The raw's header quotes the PI's routing with ASCII `->` and `x` for `→` and `×`.
- The raw's launch section says the omitted head lines were "the loader's progress bar". The order of the stdout file rules that out.
- The entry says the box precheck ran "in the driver's own process state". It actually ran in a helper process that imports the driver.
- In the entry, "each byte-identical to the box's" also covers the raw and the block, which have no box copy.

The six NOT CHECKABLE items are Code's own conduct (not opening the checkpoints and call logs), the pod's current state, and box-side events that no file on the laptop records.

**Texts.** E = `<tmp>/scratchpad/podwatch/gtime_entry.md` (placeholders `@@STAMP@@` and `@@VC@@` skipped). B = `<repo>/results/raw/2026-11-09_p-gtime_code-to-design_read.md`. R = `<repo>/results/raw/2026-11-09_p-gtime.txt`. "E:12" means line 12 of E.

**Method and blinding.**

- **Read:**
  - the three reports, the three reads and the three p-reports (all fields, including all six transcripts);
  - the scratch box copies (`gtime_box/`) and the wrapper;
  - RESULTS.md, the cited commits, PROPOSAL-m and PROPOSAL-p, both seat raws, the LOCK values-check raw and the three locks;
  - the code: `readrule.py`, `stage.py`, `report.py`, `register.py`, `p_sessions.py`, `gshape.py`, `resume.py` and `olmo_hf.py`.
- **Also read, because the raw describes them:** the scratch `box_sync_lock.sh`, `box_precheck_gtime.py`, the bundle (with `git bundle list-heads`) and `gtime_preflight.txt`. The last is identical to R's pre-flight section and adds nothing.
- **Blinding:** the six `data/p/ckpt/OLMo-*_time.json` and `*_p-calls.jsonl` files were only hashed (`shasum -a 256`, plus one hashlib digest in a comparison script). Nothing was parsed, printed or grepped from them.
- **One Python call:** the venv python, `-B` under `nice -n 19`, imported `valence_core.m.resume` to recompute the backend identifier. No model, tokenizer, driver or stage command ran.
- **Repository untouched:** `git status` shows the same 40 untracked entries and no tracked changes, with HEAD at `0afd842`.
- **One stray file:** I wrote one intermediate file to the scratch `podwatch/` folder by mistake (`vc_gtime_hashes.txt`, the 15 sha256 lines) and deleted it at once.

### E — the draft RESULTS.md entry (`gtime_entry.md`)

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 1 | Refs: PROPOSAL-p v0.2 §4.1, §8 step 6; m:302's G-TIME-OLMo-{ckpt}; the routing of 2026-11-08 in `de729c4`'s close lines, item 2 (E:1-2) | PASS | p v0.2 :84 (§4.1 chain "… LOCK-p-OLMo-{ckpt} v0.1 → G-TIME-OLMo-{ckpt} …"), :129 (§8 step 6, "LOCK-p v0.1 → G-TIME-OLMo (the seat's read, m:§3)"); m:302; RESULTS.md:914 and :970 quote item 2 ending "→ G-TIME-OLMo (p) on the box [go]". |
| 2 | PASS ×3 on the box, under LOCK-p v0.1 (`0afd842`) (E:2) | PASS | R stdout "STAGE G-TIME-OLMo-{ckpt} PASS path=uncached" and "P-REPORT … (p): PASS" ×3; m reports `status` PASS, `stop` null; p reports `status` PASS. LICENCE lines name the locks 9cc9045a…, efcba384…, c03a1ef9… committed at HEAD 0afd842; `git log` adds all three locks in 0afd842. |
| 3 | Each checkpoint ran its two uncached sessions, both valid (E:3) | PASS | "time A0-OLMo-{ckpt} s=0 valid" and "time A0s-… valid" ×3; m reports planned = recorded = 1 per template; identity `path` "uncached". |
| 4 | No hair trigger fired; the sham bar is silent at 0/10; the pause is silent (E:3-4) | PASS | m reports: `round_degeneracy@…` k 0, n 10, crit 2, fired false; `gtime_pause@…` k 0, fired false; sham `hair_triggers` []. p reports: `line_break_in_stored_text` n 0, domain "every round of every session". A fire stops the stage (m:271), and all three PASS. |
| 5 | Box unchanged since characterization; pod `qny1x4v8padeke`; backend identifier `641ee466f4553b6a` (BACKEND, `190ba90`) (E:6-7) | PASS | `resume.backend_identifier` on each run's printed PROVENANCE record gives 641ee466f4553b6a ×3. BACKEND entry (RESULTS.md:2647-2651): pod created 00:17:14Z, characterization 00:23:05Z–00:33:38Z, same identifier. stamps: RUNPOD_POD_ID=qny1x4v8padeke. |
| 6 | PID 1 since 2026-11-07T00:17:16Z; env.sh `f5174faa…`; torch 2.8.0+cu128 and transformers 5.15.0, as at G-CAL-p (E:7-8) | PASS | R:192-194 (pre-flight capture); each run's PROVENANCE `library_versions`; G-CAL-p raw :561 (`f5174faa745eca6e…`), :569, :571 ("Sat Nov 7 00:17:16 2026"). Today's PID 1 time rests on the capture. |
| 7 | Repo brought to `0afd842` by a git bundle, with no network remote (E:9) | PASS | Scratch `p-lock-0afd842.bundle`: 1,850,880 bytes, sha256 a4bc7968…285a. `list-heads` gives one head, 0afd842… refs/heads/main, with prerequisite e03fbe4. `box_sync_lock.sh` (57336926…) says "bundle, no network remote" and fetches from the bundle. |
| 8 | First, the six untracked G-CAL-p outputs, each identical to its committed blob, were set aside in `/workspace/gcal_p/box-untracked-2026-11-09` (E:9-10) | PASS | The six sha256s at R:202-207 equal HEAD's blobs (6/6). The sync script `cmp`s each against the target's blob, moves them to that ASIDE path, then fast-forwards; R:214 is its echo. |
| 9 | Precheck + weights-files check CLEAR for all three units on the box, "in the driver's own process state" (E:12-13) | IMPRECISE | Values PASS: R:219-221, lock prefixes = the locks' sha256s. But the check ran in a helper process, `/workspace/gtime_p/box_precheck_gtime.py`, which imports `p_sessions` first. It did not run in the driver's process, and R:216-217 says so. Wording below. |
| 10 | G-SHAPE-p's closure there is the recorded 14 files (E:13) | PASS | `data/p/gates/G-SHAPE-p.json` (3c4125a3…1554) `provenance.import_closure` has 14 entries. R:218: "14 files; equal to the recorded one: True". Each run's own precheck also ran the check (`lock_required` → `gshape_drift_problems`, stage.py:266-268) and cleared. |
| 11 | The wrapper's chain rule, dry-tested on nine cases (E:14) | PASS | R:226-234 holds nine cases. Each outcome follows from the wrapper's two continue tests (rc 0 + PASS line + no `^STOP:`; rc 3 + PAUSE line + no `^STOP:`). EXIT_CODES give PAUSE 3 and STOP 4. |
| 12 | `p_sessions.py time --unit OLMo-{ckpt}`, one run each, no `--resume`, back to back through `run_gtime_p.sh` (`6c2ace2c…`), on DRIVER `d91e41e1…` at `0afd842` (E:15-16) | PASS | INVOCATION lines; p reports `call_log` n_runs 1, `resume` false. `run_gtime_p.sh` sha256 6c2ace2c…34d7. `git show 0afd842:scripts/p_sessions.py` sha256 d91e41e1…a943 = the DRIVER lines. |
| 13 | sft 18:10:46Z–18:14:31Z, dpo to 18:18:16Z, instruct to 18:22:04Z; each exited 0 (E:17) | PASS | stamps.txt (scratch copy sha256 9b307adb… = box_sha256.txt), exit=0 ×3. |
| 14 | Link to the raw (E:17-18) | PASS | `results/raw/2026-11-09_p-gtime.txt` exists. |
| 15 | Disclosure: the launch call's `&` backgrounded its whole `&&` list, so the ssh call stayed open until the chain ended; the wrapper ran in its own session under nohup (E:19-20) | PASS | Matches R:181. Shell grammar: `&` ends the whole AND-OR list, so the backgrounded list's subshell holds the channel's stdout while it waits on `nohup setsid bash …`. The wrapper's stdio are files. The observed duration is box-side (#91). |
| 16 | Table, sft: 0/10; silent; 0; all 0; 4, not excluded, control chars 0; 10/10 attributed, 0 cuts; 3.528; 1/1 (E:25) | PASS | m report: bar k 0/n 10, crit 2; pause silent; `forced_rounds_generated` 4, `excluded_at_forced` false; `sham_seconds` 3.528; `first_pick_P` k 1, n 1. p report: five sham counters n 0; `contrast_forced_control_chars` n 0 of 4; proxy 10 of 10 attributed, 0 cuts. |
| 17 | Table, dpo: … 3.972; 0/1 (E:26) | PASS | As #16. `sham_seconds` 3.972; `first_pick_P` k 0, n 1. |
| 18 | Table, instruct: … 5.289; 1/1 (E:27) | PASS | As #16. `sham_seconds` 5.289; `first_pick_P` k 1, n 1. |
| 19 | Each sham session ran 4 forced + 6 free rounds, no exclusion, no claim, no cap hit; every response stopped at a newline (E:29-30) | PASS | m reports: forced.rounds 4, free.rounds 6, every exclusion count 0, claims 0, cap_hit 0. Reads: `stop_reason` "newline" in 30/30 sham rounds; exclusion and strict_exclusion None. |
| 20 | Contrast seconds and every other contrast count withheld (m:318; ruling (h)) (E:30-31) | PASS | m reports `contrast_seconds` "withheld to the unit's VERDICTS entry (m:318)"; p reports' `withheld` string. |
| 21 | Register entries (1), (2) and (6)–(9) entered (E:32) | PASS | `register_entered` [1, 2, 6, 7, 8, 9] in each p report and stdout. |
| 22 | Each report's backend identifier is the lock's line (E:32) | PASS | m reports' `identity.backend_identifier` 641ee466f4553b6a ×3 = the single "BACKEND OF RECORD 641ee466f4553b6a" line in each lock. p reports carry no backend field, so "each report" holds for m's (note below). |
| 23 | Term (d): `single_threaded` false with `tqdm_monitor` alive; recorded, never raised (the seat's Q4) (E:33-34) | PASS | p reports `term_d_at_stage_end` ×3. `de729c4` raw Q4: a library thread alive after the load "does not offend the term … a failure there is recorded in the entry". stage.py docstring: "recorded … never raised". |
| 24 | "Committed with this entry, each byte-identical to the box's (sha256 at both ends)", over the per-checkpoint outputs **and** "the raw, and the block to the seat" (E:35-39) | IMPRECISE | The values are fine: 15/15 sha256s match; `git check-attr diff` is unset (-diff) for the ckpt JSONs and call logs; `.gitignore` admits all 15. But the heading's "each byte-identical to the box's" also governs the raw and the block, which were written on the laptop and have no box copy. Wording below. |
| 25 | 29 of the 30 sham responses answer their task; sft's round 1 answered "4" to "State the number of wheels on a bicycle." (E:40-41) | PASS | My own read of all 30. **sft:** 4 (wrong), March, 24, 7, 3, 28, 64, closed, 44, 77. **dpo:** cold, 12, 44, down, 28, 2, March, a kilogram of iron, 24, 3. **instruct:** "A triangle has three sides", "A kilogram of iron is heavier than half a kilogram of feathers", "A bicycle has two wheels", Closed, Down, 77, March, Seven, 45, January. The task text is exact. |
| 26 | The block's Q1–Q4 as summarized, including m:205's 19.5 s and 22.7 s and the (h) correction "(a *backend* change STOPs the stage, not a box change; m:267)" (E:42-49) | PASS | B:129-141; m:205; B:107-111. |
| 27 | Whether the pod stays up through LOCK-p v0.2 is the PI's call (E:51-52) | PASS | The PI's routing kept it up only "through LOCK-p v0.1" (RESULTS.md:1002). |
| 28 | "Code did not open the checkpoints"; "not opened" ×2 (E:21, E:37) | NOT CHECKABLE | Code's conduct. The outputs themselves are consistent: the p reports name them as withheld. |
| 29 | "The pod stays up and idle" (E:51) | NOT CHECKABLE | Current state; not queried. |

### B — the block to the seat (`2026-11-09_p-gtime_code-to-design_read.md`)

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 30 | PI date 2026-11-09; the quote of `de729c4` §4, "G-TIME-OLMo (p) ×3 on the box, batched, then the seat's read under PROPOSAL-m §3's rule (…) once for the three" (B:3-5) | PASS | Exact substring of `results/raw/2026-11-08_p-step6_design-to-code_answers.md`:26 (§4). |
| 31 | The chain on the PI's routing of 2026-11-09 (`6b63973`, item 2): entry (9) at `e8779b1`; G-SHAPE-p re-run at `fdd79d8` (`5009e77`'s artifact superseded); G-ANL-p at `f8b16d5`; LOCK-p ×3 at `0afd842` (B:10-14) | PASS | Commit subjects as stated. `6b63973` raw §3 item 2 is the routing. `fdd79d8` moved 5009e77's artifact to `G-SHAPE-p.superseded-2026-11-09.json`. |
| 32 | G-TIME under the routing of 2026-11-08 in `de729c4`'s close lines, item 2 (B:15) | PASS | RESULTS.md:970 (and :914). |
| 33 | Pod, backend identifier, box repo at `0afd842`; the times; each exited 0; one run each, no `--resume`; raw link (B:16-19) | PASS | As #5, #12, #13 and #14. R:182 "tree clean at 0afd842". |
| 34 | m:302's two uncached sessions, A0 (contrast) and A0s (sham), both valid and verified (B:21) | PASS | m:302 "two sessions, one per arm"; stdout "valid" ×6; reads `verified` True ×6. |
| 35 | No hair trigger (m's three; p's `line_break_in_stored_text` 0 over every round of every session); `round_degeneracy` silent 0/10, critical 2 at n = 10; `gtime_pause` silent (B:22-23) | PASS | m:271 names the three (`scaffold_absorption`, `template_breakage`, `schedule_mismatch`). Values as #4. |
| 36 | Register entries (1), (2), (6)–(9) entered **in that order** (B:24) | PASS | `stage.stage_substitutions` (stage.py:397-411) enters them in loop order 1, 2, 6, 7, 8, 9 and STOPs if the list differs from `ENTERED` (:127). The reports record that list. |
| 37 | Each report's backend identifier is the lock's line (B:25) | PASS | As #22. |
| 38 | Term (d) recorded as `single_threaded: false`, threads `MainThread` and `tqdm_monitor`; recorded, never raised, as the seat's Q4 has it (B:26-28) | PASS | As #23. |
| 39 | The reads, one file per checkpoint (m's `readrule`, written by m's stage), `294361ed…408d`, `b44035be…639e`, `c7045474…75ad` (B:30-35) | PASS | sha256s recomputed. m's stages.py:1338 writes the reads via `readrule.strip_contrast` / `redact_sham`. Schema `m-stage-reads-v1`. |
| 40 | Contrast as `strip_contrast` leaves it: banner + four forced rounds, each {phase, ri, n, text}, no class field; free rounds absent (B:37-38) | PASS | readrule.py:370-393 (`TIME_ROUND_KEEP`). In all three reads, round keys are exactly {n, phase, ri, text}, `n_forced_rounds` is 4, and the transcript ends after round 4. |
| 41 | Sham as `redact_sham` leaves it: the full transcript, chosen tag `[config]` in every free round's header; no menu in OLMo's stored transcript (B:39-40) | PASS | 6/6 free headers per sham read end in `[config]]`. Piece kinds are banner, round, generation and joiner only. readrule.py:20-24 and :66-77 (OLMo writes no menu or pick line). |
| 42 | m's reports: sft `2ccd028d…`, dpo `fb90c5a1…`, instruct `7f536976…` (B:41-43) | PASS | sha256s recomputed. Form "pick-free stage report (m:271, m:318)". |
| 43 | p's reports `2070c00c…`, `1623f1cb…`, `edf90bc2…`; bind m's two files by sha256; carry `proposal_p_sha256` and p's four identity fields; the SFT sentence on sft only (B:44-46) | PASS | Recomputed sha256s of the bound files equal `m_outputs` (6/6). `proposal_p_sha256` 42f2977b…3b32. `identity_p` = {p_package_sha256, proposal, proposal_p_sha256, renders_sha256_p}. `declared_sentences` is ["G-CAL-p passed at the bar, 47/64 against 47"] on sft and [] on dpo and instruct. |
| 44 | Checkpoints are -diff and may hold a contrast pick; call logs withheld (B:47-49) | PASS | `git check-attr diff`: unset. p reports' `call_log.form` "withheld like the checkpoint (m:318)". |
| 45 | Table, sft: 10 (4 forced, 6 free); 0/10; silent; 0; all 0; 4 generated, not excluded; 0 of 4; 10 of 10 attributed, 0 cuts; 3.528; 1/1 (B:57) | PASS | As #16 and #19. |
| 46 | Table, dpo: … 3.972; 0/1 (B:58) | PASS | As #17. |
| 47 | Table, instruct: … 5.289; 1/1 (B:59) | PASS | As #18. |
| 48 | Sham sessions: no exclusion (strict or tolerant), no claim (audit, echo, lexical); no advisory round, cap hit, degeneracy or termination (B:61-63) | PASS | m reports: `excluded_sessions` and `strict_excluded_sessions` all 0; claims 0/0/0; advisory_rounds, cap_hit, degeneracy_rounds and termination all 0. Reads agree. |
| 49 | Every response stopped at a newline, after 1 to 14 tokens in the forced rounds: sft 2, 1, 1, 1; dpo 1, 1, 1, 1; instruct 5, 14, 5, 1 (B:64-65) | PASS | Reads `n_tok` exactly so. `n_tok` = `len(token_ids)`, the tokens generated before the stop token (scaffold.py:390; olmo_hf.py:249-255, 265-278, 286). `stop_reason` "newline" ×30. |
| 50 | p's sham counters `control_chars`, `harness_first_line`, `cap_hits`, `refusals`, `corrupted_spelling` (forced rounds), each 0 (B:66-67) | PASS | report.py:101 `COUNTERS`; p reports: n 0 each; corrupted_spelling's domain is "the sham sessions' forced rounds". |
| 51 | Contrast: four forced rounds generated, not excluded; control characters 0 of 4; texts in the reads; every other count withheld (p report's `withheld` line) (B:68-72) | PASS | m reports `per_session`; p reports `contrast_forced_control_chars` {n 0, n_forced_rounds 4}; the `withheld` string. |
| 52 | Timing: sham seconds from m's report; contrast withheld (m:318); m:205's basis 19.5 s at instruct, 22.7 s at SFT/DPO (b3's, load amortized); each stage 225–228 s from the stamps (B:73-75) | PASS | m:205: "OLMo basis 19.5 s per session at instruct and 22.7 s at SFT/DPO [C], which amortize one model load over a whole b3 run". Stamps: 225, 225 and 228 s. |
| 53 | 29 of 30 answer; sft round 1 "4"; no declared counter at G-TIME covers whether a response answers its task (B:79-81) | PASS | As #25. m's report classes (audit categories, claims, degeneracy, termination, advisory, cap) and p's `COUNTERS` include no correctness count. |
| 54 | (a)–(i) "verbatim from RESULTS.md at `d215d5b`"; (j) from the LOCK entry at `0afd842`; the seat's answer at `6b63973` predates the BUILD, so none has been before the seat (B:85-86) | PASS | The BUILD entry at d215d5b (RESULTS.md:407 at HEAD) records that answer as already in the tree, untracked. None of (a)–(i) appears in the seat-facing blocks `c9acd66` and `9624f70`. FLAG (j) is at RESULTS.md:57. |
| 55 | Readings (a)–(i) verbatim (B:88-116) | PASS | Scripted comparison after joining wrapped lines: (a)–(i) are 9/9 equal to d215d5b:RESULTS.md's list (:278 on). That list is byte-identical at HEAD (:646-672). The Correction sub-bullet was compared separately. |
| 56 | Correction's source: the LOCK-p v0.1 values-check, item #17 (B:107) | PASS | `results/raw/2026-11-09_p-lock-v01_valuescheck.md`:8 and :85 (#17). |
| 57 | Correction: the stage compares the adapter's backend identifier with the lock's line; a same-class new box gives the same identifier (m:267 quote); only a *backend* change STOPs; it quotes (h)'s "A box change after the lock STOPs the stage" (B:107-110) | PASS | stage.py:833-837. `resume.backend_identifier` hashes provenance minus `BACKEND_DROP` ("n_encodes_clipped", "path", "seed"), with no host or pod field. The m:267 quote is exact. The (h) quote is an exact substring. |
| 58 | "The three locks say so (§0)" (B:110) | PASS | §0 of each lock (sft :11; dpo and instruct :10): "a backend change after this lock … STOPs the stage …; a new box of the same class gives the same identifier (m:267)". |
| 59 | The stage's PIN (`stage.py:36-38`) still reads "a box change" (B:110-111) | PASS | stage.py:37: "a box change after the lock STOPs the stage before it generates". The PIN opens at the end of :35 (same citation as the LOCK values-check). |
| 60 | (j) matches the LOCK entry's FLAG (j) (B:117-127) | PASS | Same substance as RESULTS.md:57-70. Code facts checked: `gshape.import_closure` reads loaded `valence_core.*` modules outside p and m (gshape.py:168-187); `m_analyze` imports `valence_core.e2d.habit` (:91); PIN-1's closure runs in a fresh `python -I -B` (:1829-1836); 14 recorded files. B drops three things: "valence_core" before "modules", "no value depends on that order", and "not a defect in the locks" (note below). |
| 61 | "Code re-checked this on the box before the launch: 14 files, equal." (B:121-122) | PASS | R:218 (box capture); `box_precheck_gtime.py` compares `import_closure` with the recorded one. |
| 62 | Q1's quote of m:302, "a fire → STOP, a pause → the seat's adjudication, before that checkpoint's qualification" (B:131-132) | PASS | Exact substring of m:302. |
| 63 | Q2: m:302 has LOCK v0.2 carry "acceptance; projections", with port acceptance recorded at v0.2; bases 19.5 s / 22.7 s or 3.528, 3.972 and 5.289 s, one sham session each (B:133-138) | PASS | m:302 (both phrases exact); m:205; m reports' `timing`, sham_sessions 1. |
| 64 | Q3 under rule 23; Q4 "the ten readings" (B:139-141) | PASS | CLAUDE.md:344 (rule 23, anecdote governance). (a)–(j) are ten. |
| 65 | "The routing kept it up through LOCK-p v0.1" (B:143-144) | PASS | RESULTS.md:1002: "Pod: [keep up through LOCK-p v0.1]". |
| 66 | "Code opened neither" (B:51); "the checkpoints unopened" (B:53) | NOT CHECKABLE | Code's conduct. |
| 67 | "The pod stays up and idle" (B:143) | NOT CHECKABLE | Current state; not queried. |

### R — the run's raw (`2026-11-09_p-gtime.txt`)

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 68 | Title refs, and the quote of the PI's routing in `de729c4`'s close lines, item 2: ("build -> G-SHAPE-p re-run -> G-ANL-p -> LOCK-p v0.1 x3 -> G-TIME-OLMo (p) on the box [go]") (R:1) | IMPRECISE | The refs pass. The source (RESULTS.md:914, :970) reads "build → G-SHAPE-p re-run → G-ANL-p → LOCK-p v0.1 ×3 → G-TIME-OLMo (p) on the box [go]". R's header is pure ASCII, so `→` became `->` and `×` became `x`: substance identical, not byte-exact. (G-CAL-p's raw header did the same.) The wrapper's own comment (R:154) quotes `de729c4` §4 as "G-TIME-OLMo (p) x3 on the box, batched" (the source has ×3). Its bytes are pinned by 6c2ace2c…, so only a note can fix it. Wording below. |
| 69 | BOX: pod `qny1x4v8padeke` (jspace-olmo-m), 1 x A100-SXM4-80GB, US-CA-2; identifier 641ee466f4553b6a (BACKEND entry, `190ba90`; each lock's line; each report's identity); container since 2026-11-07T00:17:16Z (PID 1), before that characterization; box repo at 0afd842, tree clean (R:2) | PASS | BACKEND entry (RESULTS.md:2647-2670): name, GPU, region, characterization 00:23:05Z–00:33:38Z. Recomputed identifier ×3. Locks; m reports' identity. R:192 and G-CAL-p raw :571. R:182. |
| 70 | COMMAND: via `/workspace/gtime_p/run_gtime_p.sh`, sha256 6c2ace2c…34d7, appended; env.sh sourced; cwd /workspace/repo/jspace-lab; the per-ckpt command, one run, no `--resume` (R:3-4) | PASS | The scratch wrapper's sha256 matches, and it equals R:152-175 byte for byte. The wrapper sources env.sh and `cd`s there. INVOCATION lines. |
| 71 | Chain rule: continue on PASS (0 + P-REPORT PASS, no STOP line) or PAUSE (3 + PAUSE line, no STOP line); halt on 2, a STOP or any other exit; declared before launch; dry-tested on 9 cases (R:5) | PASS | Wrapper :168-173; EXIT_CODES (PAUSE 3, STOP 4); the driver returns 2 on refusals and prints `STOP: …` on its STOP paths; R:226-234. |
| 72 | RESULT: PASS ×3; two uncached sessions, valid and verified; no hair trigger (m's three, p's 0); `round_degeneracy` silent 0/10 (critical 2 at n=10); `gtime_pause` silent; exit 0; the three intervals (R:6) | PASS | As #3, #4, #13 and #34. |
| 73 | OUTPUTS: 15 paths with sha256 (R:8-22) | PASS | `shasum -a 256` on all 15 matches all 15. The copy-back lines (R:237-251) match as well. |
| 74 | Committed byte-identical to the box's, sha256 at both ends; checkpoints may hold a pick and are -diff; call logs withheld and -diff (R:7) | PASS | The local side is #73, and -diff as #44. The box side rests on Code's copy-back lines but is corroborated: each run's box-written stdout prints its checkpoint's sha256, equal to the local file. Each p report binds the local m report, reads, checkpoint and call log by equal sha256s. |
| 75 | Stdout sha256s: sft 861e787b…, dpo d475a8c9…, instruct 594dd587… (R:23) | PASS | Scratch copies hash so, and so does `box_sha256.txt`. |
| 76 | Verbatim sections; "the loader's carriage returns shown as line breaks"; stamps; order of sections (R:23-149) | PASS | Scratch stdout with CR → LF equals R's sections exactly (sft 4,542, dpo 4,476, instruct 4,512 chars; 14/13/12 CRs). R:25-32 equals stamps.txt. The section order is as listed. Elisions in the launch and pre-flight sections are marked ("verbatim unless marked", R:189). |
| 77 | "Host and port scrubbed; no laptop path occurs." (R:23) | PASS | Scan of R: no IPv4 address, no `31165`, no `/Users/` or `/private/`. Hosts appear as `<host>`. |
| 78 | The wrapper appended, sha256 6c2ace2c… (R:151-175) | PASS | Byte-equal to the scratch `run_gtime_p.sh` (sha256 6c2ace2c…34d7). |
| 79 | `wrapper.out` 0 bytes, "(empty)" (R:177-178) | PASS | Scratch copy is 0 bytes; box_sha256 e3b0c442… (the empty-file hash). |
| 80 | Launch output: "tree clean at 0afd842"; first stamp; pgrep line; INVOCATION (R:182-185) | PASS | Consistent: R:183 = stamps line 1; R:185 = stdout line 1; pid 13362 > setsid pid 13356. |
| 81 | Disclosure: `&` backgrounds the whole `&&` list; the call stayed open; setsid/nohup, stdio on files; the call's life did not bound the wrapper (R:181) | PASS | The mechanism follows from shell grammar and the command at R:180. The pid/sid and the observed duration are box-side (#91). |
| 82 | "(the head's other lines: the loader's progress bar, cut at 200 columns; omitted)" (R:186) | IMPRECISE | This cannot be right as worded. In the run's stdout (R:35-40; scratch `gtime_p-sft.txt`), INVOCATION is followed by DRIVER, WEIGHTS and GATE, and the bar's first bytes ("\rLoading weights: 0%") come after GATE's newline. The wrapper sends stdout and stderr to one open file (`> file 2>&1`, shared offset), and the driver flushes every print. So the file at the head's moment (8 s) was a prefix of the final one: a head that reached the bar also held DRIVER, WEIGHTS and GATE, and a head holding only INVOCATION had no other lines. The capture is not on disk, so the exact head is not checkable. Wording below. |
| 83 | Pre-flight (1): pod; pid1_start 2026-11-07T00:17:16Z; env.sh f5174faa745eca6e; torch/transformers; GPU; annotation "as at G-CAL-p … the BACKEND characterization ran on this container after it" (R:189-199) | PASS | Consistent with G-CAL-p raw :561-573, each run's PROVENANCE and the BACKEND entry's times. The capture itself is box-side. |
| 84 | Pre-flight (2): box repo at e03fbe4 with six untracked files, each sha256 equal to the committed blob (R:200-207) | PASS | 6/6 equal HEAD's blobs. e03fbe4 is G-CAL-p's box HEAD (G-CAL-p raw :2) and the bundle's prerequisite. |
| 85 | Pre-flight (3): `git bundle create … main ^e03fbe4` (1,850,880 bytes, sha256 a4bc7968…; one head 0afd842… refs/heads/main); sync script 57336926…; wrapper 6c2ace2c…; what the script does; SYNC OK; exit=0 (R:208-215) | PASS | Scratch bundle: size, sha256, one head and prerequisite as stated. Script sha256 57336926…; its steps match the description (fetch into `refs/bundles/p-lock`, exact untracked set, `cmp` per blob, move aside, `--ff-only`, re-checks). R:214 is its echo text. Wording note below. |
| 86 | Pre-flight (4): precheck + weights-files check in a process that imports the driver as its time command does; "closure at precheck time: 14 files; equal … True"; three PRECHECK CLEAR lines with backend 641ee466f4553b6a and lock_sha256 prefixes (R:216-222) | PASS | `box_precheck_gtime.py` does exactly this, and its print format matches. Prefixes 9cc9045a57dc8abc, efcba384b68d2365, c03a1ef9d8fc3ccb equal the locks' sha256s. |
| 87 | Pre-flight (5): nine dry-test outcomes (R:223-234) | PASS | Each outcome follows from the wrapper's conditions (#11). |
| 88 | Copy-back: 15 "identical" lines (R:236-251) | PASS | Local sha256 equals the line in 15/15. The paths are exactly the stage's 15 non-ignored outputs. The lock file and reservations are ignored by `.gitignore`:305. |
| 89 | Time arithmetic (task item): 225–228 s per stage | PASS | 18:10:46→18:14:31 = 225 s; 18:14:31→18:18:16 = 225 s; 18:18:16→18:22:04 = 228 s (chain 678 s). |
| 90 | "never opened by Code" / "never opened" (R:7) | NOT CHECKABLE | Code's conduct. |
| 91 | Box-side events: "each re-hashed on the box equal" (R:210); setsid pid/sid 13356 (R:181); "[exited with code 0, at the chain's end]" (R:187) | NOT CHECKABLE | No laptop file records them. They are consistent with everything that is checkable. |

### Suggested corrections (the 4 IMPRECISE items)

**#9 (E:12-13).** Now: "the stage's precheck and the driver's weights-files check, CLEAR for all three units on the box, in the driver's own process state (G-SHAPE-p's closure there is the recorded 14 files; FLAG (j) of the LOCK entry);"
Suggested: "the stage's precheck and the driver's weights-files check, CLEAR for all three units on the box, in a process that imports the driver as its `time` command does (G-SHAPE-p's closure there is the recorded 14 files; FLAG (j) of the LOCK entry);"

**#24 (E:35-39).** Now: "**Committed with this entry**, each byte-identical to the box's (sha256 at both ends):" heading both sub-bullets.
Suggested:
```
  - **Committed with this entry:**
    - per checkpoint, each byte-identical to the box's (sha256 at both ends): m's checkpoint
      `data/p/ckpt/OLMo-{ckpt}_time.json` (-diff; it may hold a contrast pick; not opened); p's call log
      `…_time_p-calls.jsonl` (withheld; -diff; not opened); m's report and reads, and p's report, under
      `data/p/reports/`;
    - the raw, and the block to the seat.
```

**#68 (R:1).** Now: `("build -> G-SHAPE-p re-run -> G-ANL-p -> LOCK-p v0.1 x3 -> G-TIME-OLMo (p) on the box [go]")`.
Suggested, either the exact bytes:
`("build → G-SHAPE-p re-run → G-ANL-p → LOCK-p v0.1 ×3 → G-TIME-OLMo (p) on the box [go]")`
or, keeping the header ASCII, mark the transliteration:
`("build -> G-SHAPE-p re-run -> G-ANL-p -> LOCK-p v0.1 x3 -> G-TIME-OLMo (p) on the box [go]"; ASCII for → and ×)`
For the wrapper's comment (R:154), whose bytes are pinned, extend R:151's heading:
`# ==== the wrapper, /workspace/gtime_p/run_gtime_p.sh (sha256 6c2ace2c01ff97d6547354d04c93477c4c0e4ffbfce09933549efece0fad34d7; its comments quote in ASCII, x for ×) ====`

**#82 (R:186).** Now: "(the head's other lines: the loader's progress bar, cut at 200 columns; omitted)".
Suggested, matching whichever the launch call's capture shows:
- If the capture showed lines after INVOCATION: "(the head's other lines -- the DRIVER, WEIGHTS and GATE lines, then the start of the loader's progress bar, each cut at 200 columns -- omitted; all are in the run's stdout above)". Drop "then the start of the loader's progress bar" if the capture stops at GATE.
- If it showed INVOCATION alone: "(no other line had been written yet)".

### Notes on PASS items (optional; nothing wrong)

- **#22 and #37.** p's reports carry no backend identifier. Tighter wording: "Each m stage report's identity carries the lock's backend identifier, 641ee466f4553b6a."
- **#60.** B's (j) says "reads the modules loaded in the calling process, outside `valence_core/p` and `valence_core/m`". The function counts only loaded `valence_core.*` modules. "reads the `valence_core` modules loaded in the calling process, outside …" would keep the LOCK entry's precision. B also leaves out "no value depends on that order" and "not a defect in the locks"; the substance stands without them.
- **#85.** R:208-210, "copied to /workspace/tmp_bundles/ with the sync script (…) and the wrapper (…)", reads as if all three files went to `tmp_bundles/`. The scripts ran from `/workspace/gtime_p/` (R:3, R:211). One clearer form: "copied to /workspace/tmp_bundles/, and the sync script (…) and the wrapper (…) to /workspace/gtime_p/, each re-hashed on the box equal".
- **#59.** The PIN text runs from the end of stage.py:35 to :38; "a box change" is on :37.
