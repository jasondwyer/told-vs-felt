# n — G-TIME-n's launch files v1: the blind launch review, as returned, with every disposition

PI date 2026-11-21. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over G-TIME-n's launch files v1, at G-TIME-n's BUILD `91f0d35`,
before the relay:
- the box script `gtime_v1.sh` as it then stood, `1418ea82…d203` (427 lines); its manifest `84550072…957b` (66 lines,
  unchanged since) with its builder `make_manifest_gtime_v1.sh` `6fe3871e…9d01`, which is G-CAL-n's
  `make_manifest4.sh` `3831b530…4e17` with three files added and Q-F3's folder written bracketed; and the launch
  note's draft `cc978e1a…3215` (172 lines), its slots for the script's, the hashes file's and the tests' figures not
  yet filled;
- the laptop tests as they then stood: the harness `ed322ae1…9333` with its stand-in `49f14328…4ee1` (389 of 389); the
  mutation pass `6a4f2850…c6a8` (124 mutants, all killed); and the snippet test v1, its runner `c2f886e0…a3f5` and its
  fixture builder `fee3c682…01cf` (51 cases, 40 mutants), not yet run, since its battery window came after the review;
- the template, G-CAL-n's launch script `gcal_v1.sh` `f3261901…9d66`, with its committed outputs and launch review.

The hashes file was not yet made; the brief asked for it to be reviewed by its source. Each file as reviewed is kept
in Code's scratch.

**The reviewer's brief** (`a5b070fd…ae54`, 158 lines):
- named those files by sha256, to be verified and read in full, and the code they must match at `91f0d35`: the
  driver's G-TIME-n section, `main()`'s dispatch, `cmd_hashes`, `cmd_selftest`, the weights check and G-VER's call;
  `runner.py`, `schema.py`, `cells.py` and `verify.py`, and the names the stage takes from `guard.py`, `ids.py`,
  `gvec.py` and `gcal.py`; the committed inputs the stage checks (`LOCK-n.md`, `gvec.json`, `gcal.json` and
  `dose_map.json`); and the rulings and routing (GT1–GT17's spec raw, Q1–Q7's block and Q8's supplement, the BUILD's
  review and entry, `.gitignore`'s block for G-TIME-n's outputs, `.gitattributes`, and CLAUDE.md's respawn protocol);
- quoted the coordinating session's routing for the launch files: B1, B2 and B6, the copy-back in Q8's default (ii),
  and its three items for the box;
- asked eleven questions: the literals on each end; the record checks and `identity_of` against what the runner and
  the artifact write, with no timing's value gated, and BARRED; the exits; a false PASS; a false FAIL; the manifest;
  the writes and removals; the order and the gates; B1, B2 and B6; the note; and the reach of the harness, the
  stand-in, the snippet test and the mutation pass;
- asked for findings, surviving mutants, observations and any command a rule bars, and quoted the list of record v2's
  items 1–5 and the rules on interpreters, writes, guard markers, `data/m[f]3`, and ckpt and reports files.

**The report** is in §3, as returned: the subagent's hand-back message, byte for byte (264 lines, sha256
`bba5bb47…8c06`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 12 findings (1 BUG, 4 RISK, 7 NIT), 8 surviving mutants, 13 observations.

## 1. Dispositions

Every finding was checked against the code at `91f0d35` before it was applied: the stage's smoke path has no branch
after its refusals, so G-VER and the 18 reads run at the smoke (`_gtime_prepare`); the runner prints a rendering pause
only as `read … RENDERING MISMATCH: not launched; PAUSE`, and a missing cell is never written by `load_cell`;
`run.txt` prints the artifact's sha256 alone; the six superset files are reached only by render-ids-iv and G-VEC's
production environment.

**Findings**

- **F1 (BUG), applied: the snippet test v2.** `run_snippet_test_v2.sh` and `make_fixtures_v2.sh` (`cases_2`, 95 cases):
  m28 is dropped and declared equivalent in the runner's header; `r_loads` sets the artifact's loads to the report's
  two, so the one-load test fails alone (m21); `p_arm` adds a PAUSE arm (m38).
- **F2 (RISK), applied.** BARRED holds the 19 names (the record's margin and log-probabilities and their token lists,
  the restricted block and its keys `tok_S`, `tok_U`, `p_S`, `p_U`, `label_mass`, `pick`, `top1_id`,
  `top1_is_label`, and the fidelity block's `fresh_margin`, `fresh_logprob_S`, `fresh_logprob_U`, `absdiff`, `scale`).
  None is a key of the report, the stage identity or the artifact at `91f0d35` (checked by name against `_report`,
  `gtime_identity`, `gtime_artifact` and `gtime_figures`). `fidelity`, `k` and `n` stay unbarred, as the review says.
  The fixtures hold one case per barred key in the report and one in the artifact (38), and the runner one mutant per
  key (b01–b19). The note names what is barred instead of "no margin or log-probability key".
- **F3 (RISK), applied as its first option.** The smoke has its own ends: at exit 3 its prints are checked for a PAUSE
  (`check_end_prints`), its report (PAUSE, no artifact, the identity lines step 3's); at exit 2 its prints for G-VER's
  STOP and nothing in `<work>/smoke`. If those hold, with the copy unchanged and the benchmark's folder empty, the
  launch ends `gtime v1 PAUSE (the smoke)` (exit 3) or `gtime v1 STOP (the smoke)` (exit 2), for the seat, and the run of
  record does not start. A refusal at the smoke stays a FAIL. The header, the note's steps and its ends say so, with
  what follows: the seat's ruling and a next version of the files.
- **F4 (RISK), applied.** The runner's PAUSE lines count the rendering-mismatch line (`RENDER_RE`); check_outputs at a
  PAUSE accepts no cell exactly when the first pause is a rendering pause at launch index 0, and checks that the
  report names exactly the cell files on disk ("cells on disk"); the changed set expects the root only when the shadow
  cell, the first read's and the root's one admitted file, is on disk.
- **F5 (RISK), applied.** The I/O benchmark line is matched as a fixed string (`-x -F`).
- **F6 (NIT), applied.** `}` and `]` are written bare in ID_RE and PODH_RE.
- **F7 (NIT), applied.** The PAUSE branch holds the run's identity to the smoke's and counts the runner's end line;
  the STOP branch holds the identity too.
- **F8 (NIT), applied.** The PAUSE branch prints each present cell's sha256; the note's copy-back names where each
  sha256 is printed (the out file) and what cross-checks it.
- **F9 (NIT), applied.** G-CAL-n's superset sentence, in the header's step 1 and in the note.
- **F10 (NIT), applied.** Both mkdirs end on a `REFUSED:` line.
- **F11 (NIT), applied** in the note's "If the run is killed".
- **F12 (NIT), applied:** the I/O line is now exact (F5); "in launch order" is now "each by its launch index and
  content", the order being the stage's own self-test's; the hashes window is the snippet test's; the time names the
  benchmarks' fsyncs and rewrites and the unmeasured self-test, G-VER and benchmark times.

**Surviving mutants**

- **M1**, killed: `ok_tau`, a COMPLETE run with one re-computed read above TAU (mutant G35).
- **M2**, moot (F5).
- **M3**, killed: the harness asserts PACKAGE, POD and LOCK_SHA256 among the draft's literals, and the stand-in
  compares check_outputs' five fixed arguments (G36–G38).
- **M4**, killed in the snippet test (F2's fixtures; b01–b19).
- **M5**, killed in the snippet test: `p_cellfull` (m44). `r_cellextrafull`, the same at COMPLETE, keeps m11 killed
  now that "cells on disk" would also catch the v1 fixture.
- **M6**, killed: a stranger in the benchmark's folder is left and said (`file_is …/bench/other.txt yes`, "left in
  place"), in four cases (B5).
- **M7**, killed: `hashes_stderr` (G34).
- **M8**, killed: `hasnt ok "note: the benchmark left"` (B4).

**Observations**

- **O1–O3, O5–O8, O10–O12:** noted. O5's three conditions: the laptop's `hashes` file is its stdout alone (the window
  command writes stderr to its own file); overlay91 is the archive the window uses; `core.autocrlf` is checked on the
  laptop before the window, and on the box any eol change in the 66 files fails step 1.
- **O4**, noted and kept: the self-test's stderr joins its counted file (2>&1), G-CAL-n's form, which held twice on
  this box; a late stderr line would fail step 2 before anything loads.
- **O6**, applied in part: the script says git's version at step 0, so the box's git is recorded.
- **O9**, applied: dropping SMC or SMB from step 5's guard is no longer declared equivalent. The smoke-check cases
  assert the run of record never started (`file_is … work/run.txt no`), and the mutation pass runs both (S32, S33).
- **O13**, applied: cases for the mkdir failures (a read-only parent; a mkdir shim), git-status failures at the first,
  second and third calls (a git shim; at COMPLETE and at a PAUSE), step 0's existence test (empty output folders),
  the PAUSE branch without its report, rendering pauses (read 0 with the root empty or absent; read 3), the smoke at
  exit 2 (G-VER's STOP and a refusal), a read above TAU, and ERE metacharacters in the work path. The harness asserts
  its .gitignore is `91f0d35`'s (`git rev-parse` against `git hash-object`).

**The reviewer's departures,** as its report states them, are in the run's entry, for the seat to class.

## 2. The tests after, on the bytes for the relay

- **The script, final:** `gtime_v1.sh` `eeee8c2e…39b6`, 519 lines; the manifest unchanged.
- **The harness** (`harness_gtime.sh` `8db61b7b…0a02`, its stand-in `f1d957e3…bd60`): 513 of 513 on the final script,
  and 513 of 513 again as a null mutant in the mutation pass's mode.
- **The mutation pass** (`mutants_gtime.sh` `f1df4cb6…d5eb`): 184 mutants in four lanes, every one killed, but 16 of the
  kills were a harness artifact: the rresolve case's folder was made under the test folder, so in a mutation run,
  with its own runs folder, the case refused for another reason ("the work folder's parent is not a folder") and
  failed under every mutant that reached it. The first pass had 15 such kills. The case now makes its folder beside
  the runs folder, and nohash now asserts that the smoke never starts. The 15 were re-run, each killed by its intended
  case. P11, check_prints' exact identity-line count, is declared equivalent (the identity's sha256 is taken by the
  same pattern, and check_outputs or the smoke-and-run comparison fails on an empty one). So: 183 mutants, all killed
  by their intended cases.
- **The snippet test v2** (`run_snippet_test_v2.sh` `9bfc3917…3dfc`, `make_fixtures_v2.sh` `84cdf4b8…e96a`), run once
  in a battery window the coordinating session granted at `91f0d35`, after `hashes`: 95 of 95 fixtures as wanted;
  `identity_of`'s three lines as wanted; 62 of 62 mutants of the outputs check killed; exit 0 (its output
  `14816ff4…636d`, 67 lines). One kill is broader than its mutant's aim: m32 also drops the cells-sum test, by
  `and`/`or` precedence, so `a_ccells` killed it first. The recomputations test it aims at is isolated by its fixture's
  construction (`a_crec`). Left declared, on the coordinating session's word.
- **`hashes`,** in the same window, from a `git archive` of `91f0d35`: `gtime_hashes_v1.txt` `a853932b…522b`, 13 lines,
  exit 0, stderr empty. Its twelve closure lines are the driver's LOCK_CLOSURE pins, and its package line is
  LOCK_PACKAGE_SHA256.

## 3. The report as returned

BLIND REVIEW: G-TIME-n launch files v1 (S/step4b/gtime/launch/), at repository HEAD 91f0d35

**Checked by tool before reading**
- The brief's sha256 (a5b070fd…ae54) matches.
- All eleven named scratch files match the brief's sha256s.
- HEAD is 91f0d35efd73ee5754b6c69a742689a89abea995.
- Every repository file I read is tracked and clean (rev-parse HEAD:<path> = hash-object <path>).

**Totals:** 12 findings (1 BUG, 4 RISK, 7 NIT), 8 surviving mutants, 13 observations.

## FINDINGS

**F1 (BUG) — the snippet test cannot end 0 as built.**
- Where: S/step4b/gtime/launch/snippet/run_snippet_test_v1.sh lines 69, 76 and 86; S/step4b/gtime/launch/snippet/make_fixtures_v1.sh lines 98 and 121–126.
- By my reading of the 51 fixtures, three of its 40 mutants survive:
  - **m28** (drop `len(reads) == 18 and`) is equivalent. gtime_v1.sh:230's `[r.get("launch_index") for r in reads] == list(range(18))` already requires 18 rows, so a_reads and a_order fail either way.
  - **m21** (drop gtime_v1.sh:221's one-load conjunct) is not isolated. r_loads puts two loads in the report alone. `bad` re-hashes only report_sha256, so the artifact keeps `[28510]` and "artifact loads" fails too.
  - **m38** (gtime_v1.sh:212's PAUSE arm set changed to True) has no fixture. r_arm is a COMPLETE fixture, and no PAUSE fixture adds an arm.
- So the test would print "killed 37, survived 3 (m21 m28 m38)" and "mutants 37/40", and exit 1.
- Fix:
  - drop m28, or list it in the header as equivalent, as the mutation pass does;
  - make r_loads also set the artifact's `.pod_hours.loads_ms` to the same two loads;
  - add `bad p_arm PAUSE null report '.per_arm["N1-R"] = {planned: 0, obtained: 0, complete: true}'`.

**F2 (RISK) — BARRED misses margin- and log-probability-bearing keys.**
- Where: S/step4b/gtime/launch/gtime_v1.sh lines 184–185; S/step4b/gtime/launch/gtime_launch_note_v1.md line 97.
- What is missing (valence_core/n/schema.py:393–425):
  - the fidelity block's `fresh_margin`, `fresh_logprob_S` and `fresh_logprob_U`, plus `scale` (the larger cached |log p|) and `absdiff`;
  - the restricted block's `label_mass`, `tok_S`, `tok_U`, `top1_id` and `top1_is_label`. Barring `restricted` covers that block only while it stays nested.
- None of these is a legitimate key of the report (schema.py:1151–1230; runner.py:356–373) or of the artifact (GTIME_KEYS, GTIME_READ_KEYS, gtime_figures), so all can be added.
- Two keys cannot be barred by name: `fidelity` (the report's counters.fidelity is legitimate) and `k`/`n` (BINOMIAL_FIELDS).
- No leak exists today. But the note's "no margin or log-probability key anywhere" overstates the check, and the fixtures test only `margin` (r_margin, a_margin) and `pick` (a_pick). See M4.
- Fix: add the names, and one fixture per barred key, in the report and in the artifact.

**F3 (RISK) — a G-VER STOP or a monitor PAUSE will end the launch FAIL, at the smoke.**
- Where: gtime_v1.sh lines 42–46 and 321–353; the note lines 109–112 and 126–135.
- On this deterministic backend, a G-VER STOP or a monitor PAUSE fires at the smoke first:
  - the smoke runs the same G-VER and the same 18 reads (GT14; `_gtime_prepare`, n_sessions.py:4185–4323, has no smoke branch after its refusals);
  - step 5 needs the smoke at exit 0.
- So the launch ends "gtime v1 FAIL: … smoke exit=2" (or 3), exit 1, and the note routes FAIL as "stop … no retry".
- The header's STOP (exit 2) and PAUSE (exit 3) ends are reachable only if the run of record diverges from its smoke.
- The note says this for a PAUSE (line 134) but not for G-VER's STOP.
- A smoke never resumes (n_sessions.py:4199–4200), so after a smoke PAUSE no pause of record exists for the seat to rule on.
- Fix, either:
  - give the smoke its own ends: exit 2 with GVER_STOP last and no REFUSED line → "gtime v1 STOP (the smoke)", exit 2; exit 3 with END_PAUSE last and a runner PAUSE line → "gtime v1 PAUSE (the smoke)", exit 3; both for the seat; or
  - state both cases in the header and the note, with their routing and what follows: a v2 whose run of record pauses at the same read and resumes under the ruling.

**F4 (RISK) — a rendering PAUSE of record ends FAIL.**
- Where: gtime_v1.sh lines 388–402.
- The PAUSE branch needs a line beginning "PAUSE " (n2 ≥ 1). The runner prints a rendering pause only as "read N s=… RENDERING MISMATCH: not launched; PAUSE" (runner.py:483).
- At read 0 no cell is written, so two more checks fail: check_outputs' `0 < len(done)` (line 214), and R2, since an empty root lists nothing.
- After G-VER's PASS and a passing smoke this is unreachable in practice. But GT5 lists rendering first, and no stand-in mode prints it.
- Fix: count that line as the runner's PAUSE line, and accept an empty root and empty `cells` at a read-0 rendering pause.

**F5 (RISK) — the I/O benchmark line breaks on most ERE metacharacters in the work path.**
- Where: gtime_v1.sh line 304.
- The line is matched as an ERE with only `.` escaped in $B (`${B//./\\.}`). Any other ERE metacharacter in the work folder's path (`+ ( ) [ ] { } * ? | ^ $`) makes a good run FAIL.
- The escape itself is never exercised: no harness path holds a dot, and neither does the proposed /workspace/nsite/work-gtime-v1.
- The line holds no variable figure. Fix: `c -x -F "I/O benchmark (GT9 (i)): 160 appends of the stage's read 6 (N1-V|valence|+1), re-keyed to BK's runs 0.. in turn, in a temporary folder under $B, removed at its end"`.

**F6 (NIT) — likely GNU grep warnings on two escapes.**
- Where: gtime_v1.sh line 58 (ID_RE's `\}`) and line 65 (PODH_RE's `\]`).
- `}` and `]` are ordinary characters in an ERE outside an interval or a bracket.
- GNU grep 3.8 and later warns "stray \ before }" and "stray \ before ]". BSD grep, the harness's, does not.
- If the box's grep is 3.8 or later (an inference: Ubuntu 24.04 ships 3.11, and the box's python 3.12.3 is 24.04's), each use writes one warning to the out file. That is about six lines in all; no count changes.
- Fix: write `}` and `]` bare; keep `\{` and `\[`.

**F7 (NIT) — the PAUSE branch checks less than the COMPLETE branch.**
- Where: gtime_v1.sh lines 387–404.
- It does not hold the run's identity sha to the smoke's, as line 366 does at COMPLETE.
- It does not check the runner's end line ("end PAUSE: k/18 reads; report time.json").
- Fix: add `[ "$RID" = "$SID" ]`, and a count of 1 for `^end PAUSE: [0-9]+/18 reads; report time\.json$`.

**F8 (NIT) — the copy-back points at the wrong source for the report's sha256.**
- Where: the note lines 152–155 (the copy-back to rec/).
- It checks the report "at the sha256s run.txt prints". But run.txt, the stage's stdout, prints only the artifact's sha256 (n_sessions.py:4393).
- Where the sha256s actually are:
  - the report's: in the out file (gtime_v1.sh:374) and in the artifact's report_sha256;
  - the shadow cell's: in the out file's "cell … sha256 …" line (375).
- At a PAUSE the script prints the report's sha256 (397) but no cell line, and the note says nothing of the missing artifact.
- Fix: name those sources, and print the cell lines in the PAUSE branch too.

**F9 (NIT) — the manifest's superset is no longer declared.**
- Where: gtime_v1.sh line 19; the note lines 26–30; S/step4b/gtime/launch/make_manifest_gtime_v1.sh line 2.
- G-CAL-n's F4 wording was dropped. Six of the 66 files are read by neither the stage nor its self-test at 91f0d35, and are kept as a superset:
  - scripts/box_e0_corpus.py;
  - data/corpus/e0_tasks.jsonl and data/corpus/e2a_tasks.jsonl;
  - data/configs/e0_frames.json and data/configs/e0_probes.json;
  - data/n/passages.jsonl.
- Only render-ids-iv and G-VEC's production environment reach them (n_sessions.py:545–548, 2140–2144). G-VEC's self-test uses stubs (2413–2457).
- Fix: carry S/step4b/gcal2/launch/gcal_v1.sh:18–20's sentence.

**F10 (NIT) — two mkdir failures end without the documented last line.**
- Where: gtime_v1.sh lines 99–100.
- `mkdir "$W" || exit 1` and B1's new `mkdir "$W/bench" || exit 1` end on mkdir's own message. That is neither the note's "REFUSED: …" (lines 131–132) nor "gtime v1 FAIL: …".
- G-CAL-n's F8 was applied only to the self-test folder's mkdir (line 142).
- Fix: echo a REFUSED line before each exit.

**F11 (NIT) — "If the run is killed" (the note lines 137–139) misses three things.**
- Killing the script's PID alone can leave the stage running. Its python is a descendant behind tee, so it can stay on the GPU and keep writing into the copy. The note should say to stop the process group, and to confirm by pgrep that no stage process remains before any copy-back or re-launch.
- The copy then holds partial outputs. v1 refuses that copy at step 0, and this script has no resume path, so a resume or a fresh copy means a v2.
- A kill during the benchmark leaves a COMPLETE report and no artifact. The recovery is the stage's resume after COMPLETE, which reloads the weights (the BUILD review's F4).

**F12 (NIT) — the note's wording.**
- Lines 86–87 list the I/O benchmark line among those that must appear "exactly". It is matched as an ERE (F5).
- Lines 88–90 say the read lines are checked "in launch order". The script checks each line's index, its content and the totals; only the end line's place is checked (gtime_v1.sh:315).
- Lines 31–32 say `hashes` runs "in a battery window of its own"; the brief says the snippet test's window.
- Lines 162–168 omit three costs:
  - the two benchmarks' time: 160 appends, each 31 fsynced rows plus a whole-cell JSON rewrite, on the network volume (the BUILD review's B2);
  - the self-test;
  - G-VER.

## SURVIVING MUTANTS

One-line changes to S/step4b/gtime/launch/gtime_v1.sh that every harness check passes, by my reading.

**M1 — line 292:** `fre='[0-9]+\.[0-9]{6} (<=|>) TAU'` → `fre='[0-9]+\.[0-9]{6} <= TAU'`.
- Wrong: a COMPLETE run with one re-computed read above TAU ends FAIL, though one exceedance fires nothing (the tail binomial needs 3 of 12).
- Every stand-in read prints "<= TAU".
- Kill: a stand-in mode with one re-computed read at `fid=0.020000 > TAU` on an otherwise COMPLETE run, want COMPLETE.

**M2 — line 304:** `${B//./\\.}` → `${B//./\\\\.}`.
- Wrong: a work path holding a dot fails a good run.
- No harness path holds a dot.
- Kill: a case whose work folder holds a dot, want COMPLETE. Moot if F5's form is taken.

**M3 — line 52** `PACKAGE=…` (or line 53 `POD=…`) → any other value; or swap two of the five fixed arguments on line 175.
- Wrong: check_outputs fails every good report on the box.
- The stand-in's check_outputs ignores `$7`–`$11`. The harness asserts neither literal: it asserts PLAN_SHA256 and DRIVER_SHA256, and the STAGE line holds LOCK_SHA256.
- Kill: assert PACKAGE and POD among the draft checks, and have the stand-in compare `$7`–`$11`.

**M4 — line 184:** delete `"logprob_S", ` (or `"logprob_U"`, either `_tokens` key, `"restricted"`, `"p_S"` or `"p_U"`).
- Wrong: a leaked key passes.
- The harness never runs the snippet, and the snippet's fixtures bar only margin and pick.
- Kill: one fixture per barred key (F2).

**M5 — line 214:** `else 0 < len(done) and set(done) <= set(CELLS)` → `else 0 < len(done)`.
- Wrong: a PAUSE report naming a cell outside the plan passes.
- p_cellname does not isolate it: its extra cell has no file, so "cell digests" and "capture arrays" fail too.
- Kill: a PAUSE fixture whose extra cell has its file, its 31 arrays and a right json_sha256.

**M6 — line 419:** `rmdir "$B" 2>/dev/null && …` → `rm -rf -- "$B" && …`.
- Wrong: a foreign file the stage left in the bench folder is destroyed, and "left in place" never prints.
- The bench-other cases end FAIL either way, and none checks the file or the note.
- Kill: `file_is smoke_benchother work/bench/other.txt yes`, or a `has` check for "left in place".

**M7 — line 154:** `> "$W/hashes.txt"` → `> "$W/hashes.txt" 2>&1`.
- Wrong: an import-time stderr warning during `hashes` on the box fails a good launch at step 3.
- The stand-in's hashes writes nothing to stderr.
- Kill: a stand-in hashes mode that writes to stderr, want COMPLETE.

**M8 — line 120:** `[ -e "$n" ] || continue` → `true`.
- Wrong: on every clean run, after both the smoke and the run, the unmatched glob prints a false "note: the benchmark left n-gtime-bench-* under … (its cleanup failed; B2): removed" into the raw. The rm -rf of the literal name does nothing.
- No case checks that the note is absent.
- Kill: `hasnt ok "note: the benchmark left"`.

## OBSERVATIONS

**O1 (Q1, literals).** Every literal the script greps or compares matches the driver and runner at 91f0d35, on the smoke and on the run:
- **SMOKE** (n_sessions.py:4239), with argparse's int 18.
- **STAGE** (4240–4241): the smoke's paths are the resolved paths' str, and W is physical; the run's go through `_shown` and print relative.
- **WEIGHTS** (4243–4244), checked against G-CAL-n's box line.
- **DRIVER** (4252–4253).
- **The inputs line** (4260–4262): every figure occurs in LOCK-n.md and equals the committed files' sha256s; d_eq and d_20 are dose_map.json's reprs.
- **The identity line** (4279–4280).
- **The plan lines** (4283–4284, via schema.read_id). The session ids by bk_cell_of are floor_b0/0, floor_b6/32, neu_b1/64, neu_b2/95, neu_b4/127 and neu_b5/159.
- **The campaign line** (4288–4290), **G-VER and its STOP** (4293–4296), **the backend line** (4306–4307).
- **The read lines** (runner.py:475, 509–511). `nonfinite` prints only on a non-finite read, which always pauses.
- **The runner's end line** (runner.py:554).
- **The I/O line** (4367–4369): its template is read 6.
- **The model time, beside and pod hours lines** (4381–4392), with GTIME_NOT_MEASURED joined by "; ".
- **The artifact line** (4393) and **the three end lines** (4394–4395, 4352).
- The script requires only the end line's place in the output. The self-test holds the order of the lines on the double (4777–4787).

**O2 (Q2, record checks).** check_outputs matches runner._report (runner.py:335–373) and gtime_artifact (n_sessions.py:4071–4084).
- The cell and array names are right.
- No timing's value is gated.
- No exact comparison fails a good record:
  - read_plan_sha256 is null off the campaign (runner.py:359);
  - per_arm has exactly three keys (353);
  - a fresh run has one load;
  - smoke is an int;
  - recomputations equals dose_rule + sample.

**O3 (Q3, exits).** The script ends 0, 2 or 3 only through VD.
- The stage's exit 2 is told apart in every case: G-VER's STOP line comes last; every refusal, before or after the load, prints a REFUSED line; argparse's exit 2 prints neither.
- The runner's CAP and STOP kinds give exit 1, so FAIL, as GT6 says.

**O4 (Q5, the self-test count).** 645 holds by the code.
- hftiny.run gives 12 checks on the box for its one skip line (hftiny.py:55–124).
- The driver's two HF branches each give one check for one skip line (n_sessions.py:1588–1601, 3710–3738). There is no other torch-dependent branch.
- On this box the count line comes last in G-CAL-n's and bext2's out raws.
- The self-test's stderr reaches its counted file by design (2>&1), so a late stderr line would fail it; neither raw shows one.

**O5 (Q5, hashes).** The `git archive` and the box's sparse copy give the same bytes:
- .gitattributes has no export or eol rule for code;
- the package hash is over valence_core/n/*.py relative to REPO (m/resume.py:328–342);
- the closure prints in module-name order (guard.py:51), which for these twelve files is identity_of's path order. G-CAL-n's box hashes show the same.

Three conditions:
- the laptop's file must be `hashes`' stdout alone (see M7);
- an archive of scripts/ and valence_core/ alone suffices, and keeps item 2's files and data/m[f]3 out of it;
- core.autocrlf on either side would change the bytes.

**O6 (Q5, the changed-set forms).** They agree with git's documented behaviour:
- porcelain v1 prints paths from the root, sorted;
- `-unormal` collapses data/n/gtime/ and data/n/ckpt/time/, which have no index entries;
- it lists time.json alone because data/n/reports/ holds skip-worktree entries;
- `:!data/n/ckpt/time/**` matches the directory itself by fnmatch, so neither A nor B2 lists the root;
- non-cone mode builds no sparse index.

The box's git version is not recorded. Any divergence fails; none can pass falsely, except inside the root, which is never listed (declared).

**O7 (Q6, the manifest).** I verified 65 of the 66 digests:
- 49 by `shasum -c -`;
- the 14 skeletons and the 2 model-folder files through cd and redirects;
- olmo_hf.py's line equals LOCK_CLOSURE's pin (n_sessions.py:3781) and G-CAL-n's box hashes line.

Every committed file the stage and its self-test read is listed.

**O8 (Q7, writes).** The script and stage write only under W, the copy's three outputs, and caches under $HOME.
- bench_clean's rm -rf reaches only direct children of $W/bench named n-gtime-bench-*.
- Nothing that existed before the launch is removed.

**O9 (Q8, order and gates).** Order and gates hold. The mutation header calls dropping SMC or SMB "equivalent". The verdict is the same, but the run of record would start, load the weights, read and write into the copy, and only then fail.

**O10 (Q9, B1, B2, B6).** All three are met.
- Stderr cannot reach run.txt or smoke.txt; only its interleaving with stdout is lost.
- The box puts the "Loading weights" bar on stderr (G-CAL-n's run-err raw).
- The cache-crop warning bext2 printed once (its out raw, line 63) will land once in run.err.

**O11 (Q10, the note).** Its respawn statement matches CLAUDE.md's protocol and adds the restart case. Neither the script nor the note holds a pod IP or port.

**O12 (K and the cells).** The campaign line takes K and the cell count as `[0-9]+`, and LOCK-n.md does not state K. But the box's self-test, which gates the smoke, asserts 7,680; 3,637 = 3,040 + 597; and 138 cells (n_sessions.py:4598–4606).

**O13 (Q11, the tests).** My counts of the harness (389) and the mutation pass (124) agree with the brief.
- No case reaches:
  - the three mkdir failures;
  - a git-status failure (lines 114, 131, 379, 401);
  - step 0's existence REFUSED, reachable only through an empty output folder, which git status does not list;
  - the PAUSE branch with the report absent;
  - a rendering PAUSE;
  - a smoke ending at exit 2;
  - a read above TAU;
  - an ERE metacharacter in the work path.
- The stand-in's prints mirror the stage's forms, but its records are minimal, so only the snippet test exercises the Python checks.
- The harness takes its .gitignore from S/step4b/gtime/commit/gitignore_v2, which I did not read because the brief does not name it. Nothing asserts that it equals 91f0d35's (dee52f42…b272).

## DEPARTURES

- **grep in S,** which the brief bars; each ran on scratch files the brief names, with no listing and no glob in S:
  - two searches for IP or port text in S/step4b/gtime/launch/gtime_v1.sh and the note;
  - one `grep -v` over the manifest, piped to `shasum -c -`;
  - sixteen one-line greps of the manifest during the redirect check.
- **Outside the repository, the HF cache and S:**
  - a name-only `ls` of Homebrew's bash folder, and `ls -d` of its opt link;
  - `git --version`;
  - the shell builtins command -v, whence and type, to learn the harness's bash, grep and git.
- **Globs in grep arguments,** valence_core/n/*.py in six commands, not listed before use. They expand to the 16 package files, none with a marker.
- **Stated plainly:**
  - cd through a glob into the skeleton folder and the model's data folder, the brief's form;
  - `diff` of the two named builders;
  - `sed -n`, `cut`, `cat` and `wc -l` on named repository files and committed raws.
- **Otherwise none:** no interpreter but shasum, no write, no network, no marker in any argv, and nothing under data/m[f]3, data/*/ckpt or data/*/reports read or listed.
