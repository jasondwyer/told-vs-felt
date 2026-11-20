# n — G-CAL-n's launch files v1: the blind launch review, as returned, with every disposition

PI dates 2026-11-19 to 2026-11-20. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over G-CAL-n's launch files v1, at ADDENDUM-n3's commit
`0744136`, before the relay:
- the box script `gcal_v1.sh` `7089e932…634a` (383 lines), its manifest `f958d830…71d6` (63 lines), its hashes file
  `8d9307b0…212a` (13 lines) and the launch note `eb8ddb72…b971`;
- the laptop tests as they then stood: the harness `9eab8f86…5cec` with its stand-in `120620df…d4f8` (435 of 435),
  and the snippet test v2 `46eb6c61…f941` (69 cases, 30 mutants, not yet run with Python; its v1 had run in a battery
  window, 57 of 57 cases and 20 of 25 mutants killed);
- the template, G-VEC's re-run script `gvec_v2.sh` `e5f76f5b…c49e`, and its committed output,
  `results/raw/2026-11-19_n-gvec-v2_out.txt`.

**The reviewer's brief** (`880de004…d511`, 121 lines):
- named those files by sha256, to be verified and read in full, and the code they must match at `0744136`
  (`scripts/n_sessions.py`'s G-CAL-n section, `gcal.py`, `schema.py`, `gvec.py`, `guard.py`, `ids.py`,
  `directions.py`, `box_e0_corpus.py`, `extract.py`), G-VEC's outputs of record and run entry, ADDENDUM-n3 §2–§4,
  the two sittings' answers (the GC items; §1.4 (i), §2.5 and §3), the PI's routing of the third sitting (item
  N.3), the gcal delta's entry and its review's box risks B1–B4, and `.gitignore`'s block for `data/n/gcal/`;
- asked ten questions: the literals on each of the five ends; the record checks against what the stage writes, with
  no hurdle's value gated; the exits and the end-line-to-path mapping; a false PASS; a false FAIL, stderr under
  `2>&1 | tee` among the examples; the manifest; the writes; the order and the gates; the note; the harness's and the
  snippet test's reach;
- asked for findings, surviving mutants, observations and any command a rule bars, and quoted the list of record v2's
  items 1–5 and the rules on interpreters, writes, guard markers, `data/mf3`, and ckpt and reports files.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (120 lines, sha256
`0af5bc8f…1a9a`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 0 BUG; 8 findings (3 RISK, 5 NIT); 7 surviving mutants, each a class; 13 observations.

## 1. Code's changes before the review

- **The commit filled:** `COMMIT=0744136…`; the harness 428 of 428; mutant G16 rewritten and killed alone.
- **The 111-mutant pass,** on the script before the fill: all 111 killed.
- **The snippet test v1, in a battery window, run once, FAILED:** 57 of 57 cases passed; of 25 mutants 20 were
  killed and 5 survived (i, j, o, p, s), exit 1. Each survivor was a sub-condition that every fixture broke only
  beside a sibling in the same conjunct. The window was released and reported; the snippets were unchanged.
- **The snippet test v2:** nine fixtures that each break one sub-condition alone or sit on the gate's bar, 69 cases,
  30 mutants; the gate's own `of == 48` mutated rather than declared equivalent, on the coordinating session's point
  that the test compares the exact set of failing conjuncts.
- **C1** (NIT): the script's header said the manifest holds G-VEC's six outputs of record; it holds the two the stage
  reads. **C2** (RISK): the driver prints unflushed, so behind `2>&1 | tee` its block-buffered stdout could take a
  stderr line inside a counted line; the two stage runs got `PYTHONUNBUFFERED=1` (the review's F1 then took the fix
  further). Mutants U1, U2, Q1 and Q2, and the harness's `smokeexit1` and `runexit1` cases (a smoke or a run whose
  prints are right but whose exit fails), harness 435 of 435.

## 2. Dispositions

The bytes for the relay: `gcal_v1.sh` `f3261901…9d66` (388 lines), `gcal_manifest_v1.txt` `f958d830…71d6` (63 lines),
`gcal_hashes_v1.txt` `8d9307b0…212a` (13 lines) and `gcal_launch_note_v1.md` `a3463cfd…d0ae` (180 lines). Every
surviving mutant below, and every finding but F7, was met before the relay; F7 was not taken.

- **F1** (RISK), applied: the stage's two runs put their stdout alone through `tee` into the file the script counts,
  and their stderr into `<work>/smoke.err` and `<work>/run.err`, which the script prints after each run;
  `PYTHONUNBUFFERED=1` stays. The harness's `smokebar`, `runbar` and `runwarnmid` cases write a progress bar or a
  warning with no newline to stderr just before a counted line, and each run passes; the mutants that merge stderr
  back (Y56, Y57), that never print a stderr file (Y58, Y59) and that print the run's when it is empty (Y60) are
  killed. The note's claim is restated.
- **F2** (RISK), applied in the note: the smoke's three files are copied back by name, each at the sha256 its file
  line prints, and committed with the stage's entry as raws; a failed smoke's turns log likewise.
- **F3** (RISK), applied: the stand-in prints each counted line twice, with a suffix or with a prefix (`dup_KEY`,
  `sfx_KEY`, `pfx_KEY`); two different end lines on every path (`runendother`; `runend2` on all five paths); a
  malformed line under a counted prefix (`smokedosebad`, `rundosebad`, `runpepbad`); a file line under another prefix
  (`smokefileother`, `runfileother`); a line after the self-test's count line (`sttrail`); and stderr during the stage
  (as for F1). The harness grows from 435 to 604 checks; the note's harness line is reworded to what is covered.
- **F4** (NIT), applied in the script's header and the note: the manifest is what the box's copy must hold, G-VEC v2's
  61, six of them read by neither the stage nor the self-test and kept as a superset, and the two outputs of record.
  `make_manifest4.sh` is left as it ran; the note's wording supersedes its header's.
- **F5** (NIT), applied in the script's header and the note: the stage unlinks its own turns log in each of its
  staging folders on a clean end, before the rename; nothing that existed before the launch is removed.
- **F6** (NIT), applied in the note: the "Loading weights" bar of G-VEC v2's smoke and run (its out raw, lines 94 and
  114) is the evidence; with F1, `run.txt` holds stdout alone, so the backend line's count no longer depends on the
  bar's newline.
- **F7** (NIT), not taken: the driver's bytes are pinned by sha256 (its DRIVER line and the manifest), so its print
  forms cannot vary, and the record check already binds each batch's figures and turns by name. For the batch lines,
  by-name counts beside the restricted total would also be mutually redundant: any two imply the third. The
  disposition goes to the seat with the run's entry.
- **F8** (NIT), applied: the mkdir of the self-test's temporary folder prints "gcal v1 FAIL: the self-test's temporary
  folder" before its exit. No laptop case can make that mkdir fail (the folder is new, in a work folder the script has
  just made), so it has no mutant.
- **M1–M7**, each met: every member of each class is a mutant of its own in the final pass, Y1–Y6 for M1 and M2,
  Y10–Y16 and Y20–Y29 for M3, Y30–Y46 for M4, Y50 for M5, Y51–Y52 for M6 and Y53–Y55 for M7, 46 in all, each killed
  by F3's cases (each mutant's harness output, in its lane's folder, names the cases that failed). The reviewer's one
  further snippet change, dropping `and gv == "-"`, is equivalent as it says: GK and GV are always set together.
- **The observations:** O1–O7, O12 and O13 ask for nothing. O8: the entry quotes the record's `weights`,
  `backend_identifier`, `characterized_identifier`, `load_ms` and `adapter_provenance` from its provenance. O9: the
  note's box step 3 checks `command -v awk sed`. O10: the note's time adds the smoke and the self-test. O11: the note's
  copy-back takes whichever of the two files a failed-run folder holds.
- **The reviewer's departures,** as its report states them, are in the run's entry, for the seat to class.

**The tests after,** on the bytes for the relay: the harness 604 of 604; a mutation pass of 166 one-line mutants, all
killed, in one pass run in three lanes (the 115 from before the review; 46 for M1–M7, one for each member, each killed
by at least one of F3's cases; and five for F1); and the snippet test v2, in a battery window, run once: 69 of 69
checks, 30 mutants of `check_outputs`, all killed, exit 0 (`run2.txt` `6c64636f…38ad`, 102 lines).

## 3. The report as returned

BLIND REVIEW: G-CAL-n launch files v1 (S/step4b/gcal2/launch/), at repository HEAD 0744136

Before reading, I verified the sha256 of the brief and of all ten named scratch files. Each one equals the value in the brief. HEAD is 07441363e6b650dcd0964ef2536244b9b4b75a79. All 19 repository files I read are clean at that commit.

Totals: 0 BUG; 8 findings (3 RISK, 5 NIT); 7 surviving mutants (by class); 13 observations.

FINDINGS

F1 (RISK): S/step4b/gcal2/launch/gcal_v1.sh lines 41-43, 241, 283; S/step4b/gcal2/launch/gcal_launch_note_v1.md lines 89-91.
- What is wrong: the claim that PYTHONUNBUFFERED=1 means "no stderr line ... can land inside a stdout line this script counts" does not hold in general.
  - Under -u, CPython's print() makes two separate writes to fd 1: the text, then "\n".
  - A write to fd 2 between those two, from another thread (write(2) releases the GIL) or from C/C++ code, lands at the end of the counted line.
  - The result is a false FAIL on any -x -F count (INPUTS_LINE, STAGE, DRIVER, the end lines, file lines). It cannot produce a false PASS.
  - The probability is low: generation is single-threaded, and logging and warnings each write one line in a single call. But the guarantee is overstated, and the bash stand-in cannot exercise it.
- Fix: count from stdout alone. For example, at lines 241 and 283: `( … ) 2> >(tee "$W/run.err" >&2) | tee "$W/run.txt"` (and the same for the smoke). Add run.err and smoke.err to the copy-back. Alternatively, soften the claim in both places.

F2 (RISK): gcal_launch_note_v1.md lines 107-123 ("The smoke's record stays on the box").
- What is wrong: the smoke generates four turns. Their only text is in $W/smoke/gcal_turns.jsonl; smoke.txt carries no turn text (the driver prints none).
  - Rule 25: "full-transcript reads of all smokes and pilots".
  - Ledger 27: nothing verdict-relevant lives only on the box.
  - G-VEC's precedent (smoke record left on the box) had no transcripts.
- Fix: copy back $W/smoke/gcal_turns.jsonl, gcal.json and dose_map.json by name, each checked against the smoke record's files_sha256 and smoke.txt's file lines. If a smoke fails inside the stage, also copy $W/.smoke.failed/gcal_turns.partial.jsonl. Or ask the seat to rule that the smoke's turns are not read.

F3 (RISK): S/step4b/gcal2/launch/test/harness_gcal.sh and test/standin_gcal_py.sh; gcal_launch_note_v1.md lines 135-137.
- What is wrong: the 435 checks (my count by reading agrees: 435) leave these classes unexercised, so M1-M7 below survive:
  - no run prints two different end lines (runend2 doubles only the PASS line, and only on the pass path);
  - no SMOKE, STAGE, DRIVER, inputs, dose map, backend or smoke end line is printed twice. The note's "each print missing, doubled or miscounted" is therefore true only for steering, turn, batch, file, exposure, gate and early lines;
  - no counted literal appears with extra text before or after it;
  - no line follows the self-test's count line;
  - nothing is written to stderr during the stage runs. The real box does write there: results/raw/2026-11-19_n-gvec-v2_out.txt lines 94 and 114 show the "Loading weights" bar, carriage returns inside, just before the backend line.
- Fix: add stand-in modes and cases for each class:
  - path+runend-other, e.g. pass with the STOP-at-−ρ line, and stopminus/stopearly/pausehalf/pauseearly with an extra PASS line; all want "path none";
  - rundupN and smokedupN;
  - a prefixed or suffixed counted literal;
  - a line after the count line;
  - a stderr progress bar ("\r…\r…\n") before the backend line and a warning line between turn lines.

F4 (NIT): gcal_v1.sh lines 17-18; S/step4b/gcal2/launch/make_manifest4.sh lines 2-4; gcal_launch_note_v1.md lines 25-28.
- What is wrong: the manifest is described as "the files the stage and its self-test read". Six of G-VEC v2's 61 are read by neither G-CAL-n's stage nor the package self-test at 0744136:
  - scripts/box_e0_corpus.py;
  - data/corpus/e0_tasks.jsonl and data/corpus/e2a_tasks.jsonl;
  - data/configs/e0_frames.json and data/configs/e0_probes.json;
  - data/n/passages.jsonl.
  The only loader of these is `_e0_corpus()` (n_sessions.py:413, 483, 2078) or `PASSAGES_FILE.read_bytes()` (:486, :2089). Neither runs in G-CAL-n's stage. In the self-test, render-ids-iv refuses before reaching them, and the G-VEC self-test uses stubs (:2351-2364).
- The superset is harmless: extra lines can only add a refusal.
- Fix: reword, e.g. "G-VEC v2's 61 (six of them read by neither, kept as a superset) and the two outputs of record".

F5 (NIT): gcal_v1.sh lines 12-14; gcal_launch_note_v1.md line 122.
- What is wrong: "What it removes: only the self-test's temporary folder" and "Nothing on the box is removed" both omit one removal. On a clean end, the stage unlinks its own gcal_turns.partial.jsonl inside its staging folder (scripts/n_sessions.py:2868, `log_p.unlink`) before the rename. This happens in the smoke ($W/.smoke.staging) and in the run (data/n/.gcal.staging).
- Fix: add that clause. Nothing that existed before the launch is touched.

F6 (NIT): gcal_launch_note_v1.md lines 90-91.
- What is wrong: "G-VEC's re-run printed two such warnings, both in its self-test" leaves out the stage's own stderr. G-VEC's smoke and run each printed the transformers "Loading weights" bar (out raw lines 94 and 114), which landed in smoke.txt and run.txt.
- Why it matters: P5 (gcal_v1.sh:307, '^backend: ') holds only because that bar ends with a newline (tqdm's leave), which it did on this box at these library versions.
- Fix: state this as the evidence for P5.

F7 (NIT): gcal_v1.sh lines 308, 312, 327, 334-335.
- What is wrong: the run counts steering checks and valence batch lines only in total (PSC=3, PBV=3 on the full path). A misnamed line would pass. The smoke, by contrast, checks +ρ's steering line by name (line 250), and the note (lines 81-82) names the three steering checks.
- Fix: count each by name ('^steering check \+rho: ', '…\+rho/2: ', '…reward_f020: '; '^batch \+rho: ', '^batch -rho: ', '^batch \+rho/2: '), each =1 on the full path. Low value, since the driver is pinned.

F8 (NIT): gcal_v1.sh lines 51 and 132; gcal_launch_note_v1.md lines 103-105.
- What is wrong: `mkdir "$W/tmp_selftest" || exit 1` exits 1 with mkdir's message as the last line, which is neither "gcal v1 FAIL" nor "REFUSED". Only the refusals before step 0 are documented this way.
- Fix: print "gcal $V FAIL: the self-test's temporary folder" before exiting.

SURVIVING MUTANTS (each passes every harness check, by my reading)

- M1: line 296, `PASS:10000) PATHK=full ;;` → `PASS:1*) PATHK=full ;;`. An exit-0 run that also prints the STOP-at-−ρ or a PAUSE end line would end PASS. Killed by a pass-path mode adding a second, different end line (want "path none").
- M2: line 298, `STOP:00100)` → `STOP:?0100)`; the same class applies on lines 297, 299 and 300. A STOP at −ρ plus a PASS line would be accepted. Killed by stopminus+runend2 (and stopearly/pausehalf/pauseearly+runend2); runend2 now runs only with the pass path.
- M3: line 260, `[ "$S3" -eq 1 ]` → `[ "$S3" -ge 1 ]`. The same class applies to S0-S4 (line 260), SE (line 263) and P1-P5 (lines 327, 334). Killed by modes that print the line twice.
- M4: line 247, `c -x -F "$INPUTS_LINE"` → `c -F "$INPUTS_LINE"`; the same applies to any -x -F count (lines 244-246, 256, 258, 291-293, 303-305, 314, 319, 345). Killed by a mode printing the literal with a prefix or suffix.
- M5: line 137, the `tail -n 1` test → `if grep -q -x -F "$SELFTEST_LINE" "$W/selftest.txt"; then`. Killed by an "sttrail" mode that writes a line after the count line (want "count 1").
- M6: line 255, `cpre "file $W/smoke/"` → `cpre "file "`; the same applies to line 317. Killed by a mode printing one file line with another prefix in place of one of the three.
- M7: line 315, PEP's `of 48 coherent` → `of [0-9]+ coherent`, or line 248/306's dose-map regex → `'^dose map: '`. Killed by a malformed-but-prefixed line case.

The two Python heredocs are emulated by jq in the stand-in, so any change to their Python survives the harness by construction; they are the snippet test's to kill. v2's 30 mutants and its 9 new fixtures cover the five v1 survivors correctly by my reading (g_gate35/36, b_dose_deq2, b_dose_R2, b_dose_Rell2, b_dose_rho, b_files_extra2, b_turns_order, b_gate_of). The only further snippet change I found that v2 does not kill is dropping `and gv == "-"` in the no-gate branch, and it is equivalent: GK and GV are always set together (lines 351-356).

OBSERVATIONS

- O1 (Q1, literals): every literal the script greps or compares matches the driver and gcal.py at 0744136, on the smoke and on all five ends.
  - SMOKE_LINE, smoke STAGE, STAGE_RUN: shown_b lists BATCHES' order plus the gate, TEMP 0.7, cap 80, out "data/n/gcal" via _shown of refuse_out's resolved path. The smoke's path is "$W/smoke" because W is physical.
  - DRIVER, and all five end lines and EARLY_STOP_LINE, character for character.
  - PEP and GATE_RE: GATE_RE matches ADDENDUM-n3 §3.3's lock form and the print at n_sessions.py:2884-2885.
  - The turn, batch, steering, file and exposure forms.
  - The inputs line, figure by figure: the manifest sha 53a8cd74… equals ids.MANIFEST_OF_RECORD; all 48 (v) prompts have seq_len 31, so the longest forward is 31+80−1 = 110; gvec.json's of_record gives R 25.54500811131038, R_ℓ 21.98789170395024, valence ba4da67fb717b5bb, span_reward 8f32921fcd1798db and site 32; the directions file sha is 33cc0ef6…c0c5.
  - Byte checks: lines 53-78 of the script hold exactly two non-ASCII characters, both "§", where the driver has them. The driver and gcal.py contain no U+2019, and their apostrophes match as ASCII.
- O2 (Q2, record checks): identity_of and check_outputs match gcal.compute, gcal.write and run_gcal.
  - Schema n-gcal-v2; the 13 row keys; RECORD_ORDER rows with indices 0..47; figures keys equal to the batches run (the gate's figures only on the full path).
  - dose_map.json's five sorted keys; the exposure dict; files_sha256 over two files; 13 provenance fields.
  - No hurdle value is gated. The gate conjunct only checks k against 36 for consistency, and accepts FAIL.
  - Exact float comparisons cannot fail on a good record. R and R_ℓ round-trip through repr; d_eq is computed by the identical expression with schema.RHO = 0.3; d_20 = min(1, 2·d_eq) involves only an exact doubling; f = 0.20 is a literal.
- O3 (Q3, exits): no refusal, failure or crash can end the script 0, 2 or 3.
  - The stage's refusals are SystemExit(msg), which exit 1.
  - An argparse error or a missing script exits 2 but prints no end line, so PATHK=none and the script ends FAIL.
  - The stage returns 0, 2 or 3 only after its end line. Every legitimate (exit, end line) pair maps to exactly one PATHK.
- O4 (Q6, manifest): I checked 62 of the 63 digests against the working tree at 0744136: 46 by diff, and the 14 skeletons and two data-folder files by cd through a glob and redirects. olmo_hf.py I did not hash, because its name holds a marker; its line equals gcal_hashes_v1.txt's and gvec.json's imported_sha256, and the file is unchanged since 616e940.
  - The stage reads data/n/gvec/gvec.json and directions_L32.npy only, plus their HEAD blobs through git show. The self-test reads nothing in data/n/gvec/: its G-CAL-n and G-VEC inputs are fakes under its temporary folder, and production paths are only compared, never read.
- O5 (Q7, writes): the script writes only under $W. The stage writes $W/smoke (via $W/.smoke.staging) and the copy's data/n/.gcal.staging, which ends as data/n/gcal or data/n/.gcal.failed. The self-test's only temporary directory is under TMPDIR. git status runs without optional locks; git show is read-only. Caches go to the home folder, as declared.
- O6 (Q8, order and gates): order and gates hold as built. The smoke runs SMOKE_BATCHES only, and compute refuses a gate in a smoke. The run needs SM, SMQ, SMID and SMC all 0.
- O7 (self-test count): 581 is arithmetic (570 + 11). No code changed between bc50244 and 0744136. data/n/gvec/ is present now and was absent at the laptop run; it touches no check. The gate's HF steering check runs on the box for the first time; if it fails, the launch stops safely at step 2.
- O8 (provenance gaps): check_outputs does not check provenance.weights, backend_identifier, characterized_identifier, load_ms or adapter_provenance. The stage refuses before the load if those are wrong. The entry should quote them from the record.
- O9 (new box dependencies): awk (cpre, line 111) and sed (lines 354-355) are new on this box relative to G-VEC's template. A missing one fails the smoke's checks safely. The pod session could run `command -v awk sed` first.
- O10 (time section): the arithmetic checks out (19,200 × 0.083 s ≈ 26.6 min; 192 arrival forwards; n §2.7 is quoted correctly; the loads match e3b48ed). The section leaves out the smoke's ≤320 + 6 forwards and the self-test, both small.
- O11 (failed-run edge case): if a failure struck between the log's unlink and the rename (n_sessions.py:2868-2869), the failed folder would hold no partial log, and its turns would be in gcal_turns.jsonl instead. Very unlikely.
- O12 (gate FAIL on a PASS run): a full-path PASS with the gate's coherence at FAIL ends "gcal v1 PASS", exit 0, as ruled. The gate line is in run.txt for the entry (routing item N.3).
- O13 (draft state): the note still carries @SNIPV2@ (line 151), and snippet test v2 has not run. Its fixture, case and mutant counts (57 + 1, 69, 30) match the brief.

DEPARTURES

- For the clean checks I used `git rev-parse 0744136:<path>` rather than `HEAD:<path>`, after `git rev-parse HEAD` printed that commit.
- Several git grep runs named code directories (valence_core/, valence_core/n/, valence_core/m/, valence_core/echo/, valence_core/adapters/) instead of item 3's pathspec. None can reach data/.
  - Three of them (valence_core/, valence_core/m/, valence_core/adapters/) cover files whose names hold a guard marker, so git searched those files' contents.
  - No marker was in any argv, and no line from such a file was printed.
- Other reads, stated plainly:
  - head, tail, wc -l, od and diff on named S files (no listing, grep or glob in S);
  - wc -l on code and raw files;
  - shasum of 46 named repository files, data files among them (none under ckpt, reports or mf3);
  - grep -o over data/n/ids/gcal_prompts.jsonl's seq_len, gen_start and label fields;
  - reads beyond the named symbols: driver lines 1-660 and other ranges, guard.py whole, RESULTS.md lines 1-363, both sittings' raws, the review raw, G-VEC v2's out and self-test raws, the delta's self-test raw, PROPOSAL-n §2.7's line, and .gitignore's data/n lines.
- One git grep failed on argument order, and one ugrep regex errored; neither printed anything.
- I ran no interpreter beyond shasum, which list item 1 names; no awk, sed or jq; no writes.
