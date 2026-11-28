# n — G-READ-n's run of record: the blind values-check, as returned, with every disposition

PI date 2026-11-27. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the record's drafted texts, at HEAD `e114b3a`:
- T1, the entry `G-READ-n`, `754bacdc…ccdb` (222 lines), its one placeholder not to be checked;
- T2, the close line on `0cc301d`'s entry, `b798f822…95fd` (11 lines);
- T3, the close line on `05ac941`'s entry, `935296c4…8a04` (9 lines);
- T4, the out raw, `32172dc4…0056` (24 lines);
- T5, the launch review raw, `a39ed81b…aa5c` (362 lines);
- T6, the expected RESULTS.md, `20812f17…6942` (41,981 lines): HEAD's, with T1 at the Log's head and T2 and T3 at the
  ends of the entries they close, built by Code's `make_results.sh`.

**The parent.** The record commits on `e114b3a`, the coordinating session's notes on the seat's two raws of
2026-11-26 (raw (A) and the PI's routing raw among the paths it adds), committed on `0cc301d` after the run's window
closed. The texts cite raw (A) and the routing raw at `e114b3a`.

**The checker's brief** was a file the checker read itself, as its prompt directed: Code's scratch file
`S/step4b/gread/record/vc_brief.md` (`d9bc674d…b59b`, 150 lines). It:
- named the texts and the sources. In the repository: the files the texts cite, at `e114b3a`, and the artifact, by
  `jq`, `shasum`, `wc -l` and `wc -c` only; the campaign's report never read, hashed, sized or timed. In Code's
  scratch, by a sources list at its sha256 (`f694633d…ce7c`, 20 files): the six texts and their builder; the run's
  out, err and exit files; the step scripts v1 and v2, v1's stand-in test, the stand-in maker, and the launch review's
  brief, report and dispositions; `pkgsha.sh`; Code's readings GR1–GR14 as sent; and the record's sweep script.
  Beside them, name-only listings of the run's and launch folders, and the creation times of the out and exit files.
  In the sessions' notes folder: Code's two launch-files notes. In this session's transcript: the coordinating
  session's relays, and the outputs of Code's calls the texts rest on;
- allowed `shasum`; `jq` on the artifact, on committed JSON and on this session's transcript; and `sed -n`,
  `/usr/bin/grep`, `cut`, `diff`, `cmp`, `od`, `wc -l`, `wc -c` (never under ckpt or reports), `tr`, `sort`, `uniq`,
  `head`, `tail`, `fold` and the shell's arithmetic. It barred any other interpreter (`awk` among them), any write,
  any network, any guard marker in an argv (a grep pattern and the command's own text included), and globs over the
  root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size, time or hash of a ckpt or reports file, anything
  outside the repository but the named files (the staging folder above all), and any naming of G-TIME-n's holding
  folder in an argument;
- asked for a sweep of Code's shell commands from the BUILD entry's final sweep (2026-11-26T01:48:39.235Z, T's UTC
  stamp) to the command that hashed the brief, in T1's seven spans with T1's counts, and the kinds after the draft's
  sweep (2026-11-27T23:48:46Z), for T1's list of them; and T1's two departures and its counts of markers and folder
  names in commands and outputs;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (202 lines, sha256
`2990ba43f5fa8735a36e565552d7fc377fee1017cd7f9ea21f901b13489640c6`). It names scratch files as S/..., the sessions'
notes folder as N and the transcript as T. Its times are T's UTC stamps: 01:xx and 02:xx on 2026-11-26 (the evening of
2026-11-25, PI-local), and 20:xx and 23:xx on 2026-11-27.

**Totals:** 98 items: 88 CONFIRMED, 6 IMPRECISE, 1 FAIL, 3 NOT CHECKABLE; and 6 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Each text was edited as a v2 copy of the draft the checker read (S/step4b/gread/record/entry_v2.md,
close_0cc301d_v2.md, close_05ac941_v2.md, out_raw_v2.txt and review_raw_v2.md), by the file tools only, and each
edit is replayed by tool in §2.

**The FAIL item:**
- **Item 91, the review raw's "about 5 GB of reads" (T5).** Applied in the checker's words: the report says "roughly
  5 GB of reads", and the raw now quotes that, with GR9's own words beside it ("the reads of about 5 GB").

**The six IMPRECISE items:**
- **Item 15, check's assertions on the report (T1).** Applied in the checker's words: "the report committed and clean
  and at the close list's first line (by blob id and digest; nothing else of it read)".
- **Item 55, the dates of the spans on the evening of 2026-11-25 (T1).** Applied: "PI date 2026-11-25" for the first
  departure and for the BUILD-commit, launch-files v1, launch-review and launch-files v2 spans, the dates convention's
  PI-local dates; the sweep's start keeps its UTC stamp, so labeled.
- **Item 60, the 19 paths touched (T1).** Applied in the checker's words: "17 files, the run's folder and its temporary
  folder".
- **Item 63, `stat -f`'s times (T1).** Applied: "creation and modification times".
- **Item 64, `e114b3a`'s show (T1).** Applied in the checker's words, with its whole message
  (`--format='%H%n%ci%n%B'`, into `fold` and `head`).
- **Item 90, how the report names scratch files (T5).** Applied in the checker's words: by their paths inside the
  scratch folder or by bare file name; it holds no full local path.

**The three NOT CHECKABLE items** (51, 70, 71) are Code's plans for the commit: "Not pushed", gate v21's id list, and
the commit by path with its home-folder count. Gate v21 is v20 with its checks unchanged and two agent ids added, the
launch reviewer's and this checker's; the commit's gate and verify check the rest.

**The six observations:**
1. **The venv's folder, as the v2 note promised.** Applied: the launch-files v2 span now says that v2's `pre`, in its
   rehearsals and in each stand-in's `run`, tested `jl*/.venv/bin` by builtins, and that the stand-ins' wrapper ran
   `cd` into that folder and `[[ -x ./python ]]` there, outside a window; no interpreter ran, and nothing in the folder
   was read. The note's "one `kill`" is noted beside the span's two.
2. **The fit stages' times.** Applied: each stage's time is stated with its cells' second reads (and, at +1, the repeat
   check's second call), as the driver's `t0` before `probe_cell` has it (scripts/n_sessions.py:8110, :8143), and
   GR9's projection is stated as the fits' alone, without "between".
3. **`after`'s power line.** Applied: printed, not asserted.
4. **"hashed".** Applied, in the review raw's account of the brief.
5. **The task-list calls.** Applied: 21 task-list updates and 8 wrap-ups in the spans to the draft's sweep; the later
   ones in the list after it.
6. **The counts after the draft's sweep.** Met, in the entry's list after the draft's sweep, from Code's final sweep.

**The sweep's uncovered kinds** are added to their spans in the checker's terms: the BUILD-commit span's print of the
entry draft's file-tools lines, its fixed-string counts of the scratch folder's word (twice), the delta's added lines
written to a scratch file, and the `grep -n -F` prints of the staging folder's last name (twice); the launch-files v1
span's `grep -n -E` of RESULTS.md for G-ANL-n's launch lines, and the launch-set note's `grep -c ''` and headings; and
the after-the-run span's `mkdir -p` of the record's two folders, the out's last byte by `tail -c 1 | od`, the two
launch notes' `shasum` and line counts, `cat -n` as a numbering filter, `e114b3a`'s whole message (item 64) and the
sweep script's `diff`. The 12 commands after the draft's sweep, the `awk` among them, are in the entry's list after
it.

## 2. The edits, replayed

The edits after the check were recovered from this session's transcript by `jq` and replayed on the drafts the checker
read, each change's old text found exactly once, by the replay script `S/step4b/gread/record/edits_check_rec.sh`. The
results are byte for byte the revised texts, so nothing else changed after the check:
- the entry, 20 of 20 edits;
- the close line on 0cc301d's entry, 0 of 0;
- the close line on 05ac941's entry, 0 of 0;
- the out raw, 0 of 0;
- the launch review raw, 3 of 3.

They are, in order of time: this check's dispositions; the commit-time fills (the list of Code's commands after the
draft's sweep, and the final counts); and one from Code's read of the first full build, the launch review raw's sha256
and length in the entry, updated to the revised raw's. After the edits, three placeholders were filled by tool: this
raw's sha256 and length in the entry, and the entry's count of these edits.

## 3. The report as returned

```text
BLIND VALUES-CHECK: G-READ-n's run of record, texts T1–T6 (HEAD e114b3a)

Set-up. The brief is at its stated sha256 (d9bc674d…b59b). The sources list S/step4b/gread/record/vc_sources.txt is at f694633d…ce7c with 20 lines, and `shasum -a 256 -c` gives 20 of 20 OK. HEAD is e114b3abfc17…. Every repository file cited is clean at HEAD (`git rev-parse HEAD:<path>` equals `git hash-object`): raw (A), the routing raw, LOCK-n.md, PROPOSAL-n-bk-reconciliation-v0_2.md, ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md, the close list, .gitignore, scripts/n_sessions.py, valence_core/n/probe.py, valence_core/n/cells.py, scripts/n_analyze.py, results/raw/2026-11-20_n-ganl_out.txt, results/raw/2026-11-25_n-gread-build_review.md and RESULTS.md. Every hash abbreviation in T1–T5 (19 distinct) and every full hash in them was checked by tool against its full value: all match.

== ITEMS ==

T1, the entry

1. T1:1. "n v0.2 §8 step 15; n:161's entry". CONFIRMED. PROPOSAL-n-bk-reconciliation-v0_2.md:159 has step "15. G-READ-n from the captures", and :161 lists the entry `G-READ-n`.
2. T1:1–3. From the BUILD 0cc301d: COMPLETE, exit 0 with the artifact; valence +1 FAIL and the other five PASS. CONFIRMED. S/step4b/gread/run/out.txt:23; exit.txt reads "EXIT=0"; T's after step prints "HEAD now 0cc301d…" and "after PASS".
3. T1:3–4. The command, run once, model-free on the laptop's CPU. CONFIRMED. gread_steps_v2.sh:127; T has one `run` call (2026-11-27T20:47:26Z); out:1; scripts/n_sessions.py:7956–7957 refuses on a pod.
4. T1:4–5. The window (on AC power) was granted on the PI's routing of 2026-11-26 (item 5, "[go]"). CONFIRMED. T's relay at 2026-11-27T20:47:05Z: "THE RUN'S WINDOW (ON AC POWER) GRANTED … on the PI's routing of 2026-11-26 (item 5, "[go]"; "Route as given")".
5. T1:5–6. The artifact enters by the admit committed with the BUILD. CONFIRMED. `git diff 05ac941 0cc301d -- .gitignore` adds `!/data/n/gates/G-READ-n.json` (.gitignore:333), and `git check-ignore -v` names that line.
6. T1:6. Nothing ran on a model or on the box. CONFIRMED, as far as T shows. The window's only calls are the four steps, no pod tool is called in the spans, and the driver refuses on a pod.
7. T1:7–8. The headline quoted verbatim; exit 0; stderr empty. CONFIRMED. out:23; exit.txt; `wc -c` of err.txt is 0.
8. T1:8–10. The artifact: `n-gread-v1`, 378f9972…f519, 384,120 B, 6,382 lines, and the printed sha256 equals the file's. CONFIRMED by `shasum`, `wc -c`, `wc -l` and `jq .schema`, against out:22.
9. T1:11–15. The routing raw is at 311ffdc0…8322 and was added at e114b3a; the quotation is its line 19. CONFIRMED. `shasum`; `git show --name-status e114b3a`; results/raw/2026-11-26_two-raws_pi-routing.md:19, verbatim.
10. T1:15. "Route as given". CONFIRMED (routing raw:38).
11. T1:16–19. Raw (A) is at cd6ba27f…0209, added at e114b3a; the §5 quotation. CONFIRMED. The quotation is raw (A):52.
12. T1:20. The step script v2 is at 85dfa911…a023 with 201 lines. CONFIRMED.
13. T1:20–22. The four steps ran once each, each its own call. Steps 1, 2 and 4 were each reported in a message of its own, then the end notice. CONFIRMED. T's Bash calls: 20:47:15Z, 20:47:26Z, 20:47:41Z (background) and 23:37:56Z. Messages: 20:47:21Z, 20:47:37Z, 23:38:53Z and 23:38:56Z ("ended, EXIT=0", "after PASS"). The grant says "one step to a message".
14. T1:22–23. HEAD was 0cc301d from check to after; PI date 2026-11-27. CONFIRMED. check printed HEAD 0cc301d; after printed "HEAD now 0cc301d…" with no NOTE. e114b3a was committed at 2026-11-27T18:41:57-05:00, after the after step.
15. T1:24–26. Among check's assertions: "the driver, `LOCK-n.md` and the close list committed, clean and at their pins, and the report at the close list's first line (by digest; nothing else of it read)". IMPRECISE. pre/pins also requires the report committed and clean at HEAD (v2:66, `clean "$REP"`, by blob ids), and requires the close list's first line to name the report (v2:64). Put instead: "the driver, `LOCK-n.md` and the close list committed, clean and at their pins, and the report committed and clean and at the close list's first line (by blob id and digest; nothing else of it read);"
16. T1:26–34. The rest of check: pkgsha.sh and the package digest; valence_core by count; scripts/ clean; the .gitignore's admit and its ignore of `.tmp`; gates holding G-ANL-n.json alone; the venv glob tested by builtins in a subshell; the run's folder; the processes; GR10's five variables; AC power; Low Power Mode off; each assertion silent when it holds. Printed: AC, "Sleep Count:1 Dark Wake Count:0 User Wake Count:1", the five variables unset, and HEAD. CONFIRMED. v2:57–112 and :116–121; T's check output.
17. T1:35–39. run repeats the assertions, then the command as quoted, with <run> and <repo>. At 2 s the PID named the run: PASS. CONFIRMED. v2:123–134; T's run output (the command line and "run PASS").
18. T1:40–41. wait as a background task: `kill -0` plus the command line every 600 s, then no process naming the run: "ended; polls off AC power: 0". CONFIRMED. v2:136–157; T's background call, whose task output was read at 23:37:53Z.
19. T1:42–47. after: each assertion and each printed value as listed, including `git status --porcelain --ignored -uall -- data/n/gates` with item 3's and Q-F3's exclusions (v2:47, :177), out 23 lines, err 0, then PASS. CONFIRMED. v2:159–195; T's after output. See observation 3.
20. T1:48. Nothing of the run's files was read, listed or timed until the wait ended. CONFIRMED. T has no tool call between 2026-11-27T20:47:58Z and the task notification at 23:37:43Z.
21. T1:49–50. The fits 9,832,753 ms (2.731 h): the comparator points 270,536 ms and the results 9,562,217 ms. CONFIRMED by shell arithmetic over out:12–21 (9,832,753 / 3,600,000 = 2.7313). See observation 2.
22. T1:50–51. GR9's projection: 2.650 h at the medians and 2.769 h at the maxima (LOCK-n.md:94–95). CONFIRMED. LOCK-n.md:94–95; S/step4b/gread/spec/gr_readings_v1.md:121.
23. T1:51–52. 3,751 ms, 4,728 ms and 133 ms. CONFIRMED (out:7, :8, :10).
24. T1:52. 9,842 s from the out file's creation to the exit file's. CONFIRMED. `stat -f '%SB'` gives out.txt Nov 27 15:47:27 and exit.txt Nov 27 18:31:29, which is 9,842 s.
25. T1:52–53. AC power at check, at after and at every poll; the counts equal; no pause. CONFIRMED by the check and after outputs and the wait's "polls off AC power: 0".
26. T1:54–55. The inputs as printed (out lines 2–8), each held by the command's refusals before any fit. CONFIRMED. out:2–8; scripts/n_sessions.py:7942–8070 (`_gread_prepare`) runs before the first fit.
27. T1:56–57. The driver 35c4c73e…4808 and LOCK-n.md 59e0b1bc…00aa (LOCK-n v1.0's), each HEAD's committed bytes. CONFIRMED (out:2–3; both clean at those digests).
28. T1:58–59. The package 06b55761…1d39 and its closure of 12 files, the lock's (L §18). CONFIRMED. out:4; LOCK-n.md:1176–1213 gives the digest and twelve files.
29. T1:60–61. The close list 42682630…fe6d, 4,417 lines, HEAD's committed bytes. CONFIRMED.
30. T1:62–64. The report 1cabeadf…c4e3 is the close list's first line; COMPLETE; identity d566764f…7f8a; read plan 7f7d7301…88a6; 138 cells and 4,278 arrays; band 33–63; the seeds are the lock's. CONFIRMED. The close list's line 1 holds out:6's full digest (`grep -c` gives 1); out:6; the artifact's campaign fields; LOCK-n.md:322 and :823–825.
31. T1:65. 4,417 of 4,417 staged files, each opened by name. CONFIRMED. out:7; scripts/n_sessions.py:8045–8056.
32. T1:66–67. The cells through `cells.load_cell` (`check_cell`, the layers' rows against `capture_sha256`, each row against its sha16), each at the report's values. CONFIRMED. out:8; scripts/n_sessions.py:8059–8068; valence_core/n/cells.py:135–169.
33. T1:68–70. The environment line and the repeat check. CONFIRMED. out:9 and :11; scripts/n_sessions.py:8090–8092 and :8128–8135.
34. T1:71–72. The comparator as the seat ruled it (raw (A) §2). CONFIRMED. raw (A):25; scripts/n_sessions.py:7815–7823.
35. T1:72–74. 24 directions, 31 layers each, no shuffles. Largest band medians: +1 1.0 (all 24 at 1.0), 0.99375, 0.998125, 0.953125. CONFIRMED. out:12–15; in the artifact by jq, +1's 24 band medians are all 1.0.
36. T1:75–77. `probe.result` with 200 shuffles, 320 rows, the lock's seeds; the PASS rule (`probe.verdict`, ADDENDUM-n1 §6.4); 31 of 31 layers above their null. CONFIRMED. probe.py:45, :78–83, :104; ADDENDUM-n1…:58; out:16–21; jq gives above_null at 31 of 31 for all six.
37. T1:79–86. The table. CONFIRMED. out:16–21; jq of each result's axis, dose label, contrast, band median, comparator max and status.
38. T1:88–89. valence +1's FAIL as computed (`bm > comp_max`, probe.py:82); AUC 1.0 at all 31 layers. CONFIRMED. probe.py:82; jq finds 31 layers at auc 1.0.
39. T1:89–90. The quotation at probe.py:162. CONFIRMED.
40. T1:90–92. The raw (A) §5 quotation "Its result enters n §5 only where n §0.6 says". CONFIRMED (raw (A):53).
41. T1:93–94. `probe.artifact`; `check_gread` and the analyzer's binding conditions (anl:6459–6484) hold, per the out's line 22. CONFIRMED. out:22; scripts/n_analyze.py:6459–6484 (`gread_problems`); scripts/n_sessions.py:8157–8171; probe.py:116–135.
42. T1:94–95. G-ANL-n.json's form: sorted keys, a one-space indent, a final newline. CONFIRMED. `jq -S --indent 1 .` of each file reproduces its sha256 (378f9972…; e775cbb4…); scripts/n_sessions.py:8161.
43. T1:95–101. The artifact field by field, with no margin or per-session value. CONFIRMED by jq:
   - campaign: 138 cells, each with json_sha256 and capture_sha256 at layers 33–63, plus read_plan_sha256 and stage_identity_sha256.
   - probe: bar 0.9, kfold10, cv_seed 20261116, layers 33..63, lr {iters 300, l2 0.01, rate 0.1, seed 7}, package_sha256, shuffle_seed 20260905, shuffles 200.
   - results: six, each with axis, dose_label, contrast, bar, band_median_auc, status, merged [], comparator {24 band_medians, max}, and 31 per_layer rows {layer, auc, null_p95, above_null}.
   - The artifact's distinct key names and string values hold no margin or session field.
44. T1:102–104. The out holds no local root, no guard marker and no margin or per-session value; its paths are relative to the root; its only non-ASCII bytes are its two "§". CONFIRMED. Bracketed marker count 0; root-pattern count 0; margin/session-word count 0; the printed paths are repo-relative; the non-ASCII bytes are 4, `c2 a7` twice.
45. T1:104–106. The err is 0 bytes, so there is no err raw; the out raw 32172dc4…0056 has 24 lines, a header and then the stdout. CONFIRMED (`wc -c`; the sources list; `tail -n +2` is cmp-equal to out.txt).
46. T1:106. The temporary folder was empty before and after the run. CONFIRMED. v2:103 and :174 held (check and after PASS); `ls -1A` of the run's tmp is empty now.
47. T1:107–110. The launch review raw a39ed81b…aa5c, 362 lines: one pass over v1 at 0cc301d; no BUG; F1–F10 RISK and F11–F15 NIT; "both"; 9 run risks and 10 observations; no departure. CONFIRMED (T5's §2, which is the report).
48. T1:110–112. v2 built in every finding; the coordinating session read v2 and its note whole, checked them by tool, and set the window's power words from the review's. CONFIRMED. T's relay at 2026-11-26T02:49:43Z ("read whole and checked by tool"; "The window's words on power, which I'll set at the grant, are the reviewer's"); the grant at 20:47:05Z.
49. T1:112–114. The stand-ins' four tests (§1, F10). CONFIRMED. The dispositions' F10 and F1. T's outputs from 2026-11-26T02:44:15Z to 02:46:53Z:
   - the 45 s job exited 3;
   - the glob-that-matches-nothing stand-in failed run at 2 s;
   - with the wrapper killed, wait named the child, after refused, and no exit file was written;
   - run naming another HEAD launched nothing.
50. T1:115–117. "Next" (raw (A) §5), including `--gread` and CP18. CONFIRMED (raw (A):53–54).
51. T1:117. "Not pushed." NOT CHECKABLE (Code's plan for the record's commit).
52. T1:119–120. The sweep runs from the BUILD entry's final sweep (T's 01:48:39 UTC) by jq; "Code knows of no others". CONFIRMED. T's Bash call at 2026-11-26T01:48:39.235Z ran the BUILD's sweep script; S/step4b/gread/record/sweep/sweep_rec.sh has that START and uses jq. No other guard marker, plain Q-F3 name or holding-folder name is in any argv in the spans. See observation 1.
53. T1:122–125. Departure 1: a marker in an argv once, from four memory notes read by `sed -n '1,60p'` in a `for` loop. CONFIRMED. T 2026-11-26T02:01:16Z; bracketed count 1.
54. T1:126–129. Departure 2: the holding folder's name in its `noindex/n/` form in a `grep -E` pattern, over the out and the artifact only. CONFIRMED. T 2026-11-27T23:39:46Z; the loop runs over those two files; bracketed count 1.
55. T1:122, :130, :145, :156, :159. The date "2026-11-26" for departure 1 and for the BUILD-commit, launch v1, review and launch v2 spans. IMPRECISE. Those calls ran 2026-11-26T01:49Z–02:48Z, which is 20:49–21:48 local on 2026-11-25 (the commits' offset is -05:00). T5:3 says "PI date 2026-11-25", and both notes are dated 2026-11-25. Put instead:
   - "(PI date 2026-11-25, at the launch files' drafting)";
   - "(27 commands, PI date 2026-11-25)", "(13 commands, PI date 2026-11-25)", "(4 commands, PI date 2026-11-25)", "(26 commands, PI date 2026-11-25)".
   (Alternatively, mark each date "UTC".)
56. T1:130–144. The BUILD-commit span: 27 commands, with the three builds as described. CONFIRMED. The count is from T. Build 1: "FAIL: entry.md: 1 lines over 120 characters…". The Edit at 01:52:43Z put @EDITS@ on its own line. The Edit at 01:53:35Z changed "two overlays" to "three". `cmp` and `diff` ran at 01:53:41Z. Uncovered kinds are under THE SWEEP.
57. T1:145–155. The launch v1 span: 13 commands, with kinds as named. CONFIRMED (count; exceptions under THE SWEEP).
58. T1:156–158. The launch review span: 4 commands. CONFIRMED (02:08:54Z, 02:10:10Z, 02:10:23Z, 02:37:15Z).
59. T1:159–172. The launch v2 span: 26 commands. CONFIRMED. Includes the two kills (02:42:30Z, 02:45:23Z), the background waits and the `after` refusal.
60. T1:173–175. "`stat -f '%Sm'` of the 19 scratch files to touch". IMPRECISE. The 19 paths are 17 files plus the run's folder and its temporary folder (T 2026-11-27T20:46:29Z). Put instead: "`stat -f '%Sm'` of the 19 scratch paths to touch (17 files, the run's folder and its temporary folder)".
61. T1:176. The window span: 4 commands. CONFIRMED.
62. T1:177–192. The after-the-run span: 35 commands, the sweep's run included. CONFIRMED (count; exceptions under THE SWEEP).
63. T1:178–180. "`stat -f` of their creation and change times". IMPRECISE. The format was `'%N born %SB modified %Sm'` (T 23:41:56Z). Put instead: "`stat -f` of their creation and modification times and the temporary folder's".
64. T1:182–184. "`git log` (ids, dates and subjects) and `git show --name-status` of `1641948` and of `e114b3a`". IMPRECISE. The e114b3a show used `--format='%H%n%ci%n%B'` into `fold` and `head` (T 23:47:38Z), printing the whole message; that output is the Counts item's "e114b3a's message". Put instead: "`git log` (ids, dates and subjects) and `git show --name-status` of `1641948`, and of `e114b3a` with its whole message (`--format='%H%n%ci%n%B'`, into `fold` and `head`), with item 3's pathspec".
65. T1:193–200. The file tools: 25 Edits (6, 8, 7, 4), 15 Reads (4, 2, 5, 4), 11 Writes (3 notes, 6 scratch, 2 heads), 8 messages, one subagent, one ToolSearch. CONFIRMED (T's calls, each by time and masked path).
66. T1:201–202. Over the commands and file-tool paths: one marker, one holding-folder name, no plain Q-F3 name. CONFIRMED (jq, bracketed; hits only at 02:01:16Z and 23:39:46Z).
67. T1:202–206. Marker words in eight commands' outputs and four file-tool reads, as named. CONFIRMED.
   - Commands: 02:00:48Z, 02:01:16Z, 02:08:54Z, 23:40:10Z, 23:40:25Z, 23:40:29Z, 23:41:43Z, 23:47:38Z.
   - Reads: raw (A) at 20:46:15Z and 23:41:21Z; the review brief at 23:42:51Z; RESULTS.md (offset 24) at 23:47:43Z.
68. T1:206–208. Q-F3's repository path in three outputs (once, twice, once); the holding folder in none. CONFIRMED: 02:00:48Z (1), 23:40:10Z (2), and the Read of RESULTS.md at offset 7679, the G-ANL-n entry, at 23:40:45Z (1). Holding-folder name: 0 in all outputs.
69. T1:209–212. The reviewer's departures: none; its commands as listed. CONFIRMED (T5:352–361).
70. T1:214–215. Gate v21 and its id list. NOT CHECKABLE (Code's plan). T does show the reviewer's id appended to the gate's new-id list at 2026-11-26T02:10:23Z.
71. T1:216–221. Committed by path; the prefix count of 0; "Not pushed". NOT CHECKABLE (plan). The citation "raw (A) §5's last bullet" is CONFIRMED (raw (A):56).

T2, the close line on 0cc301d's entry

72. T2:1–2. "PI date 2026-11-26, the thread's second sitting", n-build's items 1–5; GR3 and GR5 stand; ran on this BUILD. CONFIRMED. raw (A):3; raw (A) §6 "N (n)" items 1–5; the routing raw's A items 1–5; the relay at 20:44:26Z: "Items 1–5 are yours".
73. T2:2–4. The raw's path, cd6ba27f…0209, committed by path at e114b3a on "Route as given". CONFIRMED (`git show --name-status e114b3a`; its subject).
74. T2:5. The §1 quotation. CONFIRMED (raw (A):14).
75. T2:6–7. The §2 quotation. CONFIRMED (raw (A):25).
76. T2:8–9. §3: declared items accepted, O6 not required (a note for N-lap), R:12996 a disclosure; §4: departures inert. CONFIRMED (raw (A):32–48).
77. T2:10–11. The BUILD's bytes unchanged, and the run ran on them. CONFIRMED. At e114b3a the driver is 35c4c73e… and the .gitignore 3aac58be…, both the BUILD's; out:2; raw (A):10.

T3, the close line on 05ac941's entry

78. T3:1–2. n-build's items 1–2: Q1 and Q2 ruled. CONFIRMED (raw (A) §0 and §6 items 1–2).
79. T3:2–4. Path, sha256 and e114b3a. CONFIRMED.
80. T3:5–8. Both quotations. CONFIRMED (raw (A):14, :25).
81. T3:9. The run went on the readings as built. CONFIRMED. The driver is unchanged, and `gread_comparator_cells` is as ruled (scripts/n_sessions.py:7815–7823).

T4, the out raw

82. T4:1. The header: step and n:161; the command; driver sha256; model-free; `nice -n 19`; `-I -B`; cd into the venv's bin by glob; TMPDIR in scratch; `nohup caffeinate -is` through `/bin/zsh -f`; the step script's sha256; the window; PI date; exit 0; stderr 0 bytes; 23 lines; no local root. CONFIRMED. v2:127; T's run output; exit.txt; `wc -c`/`wc -l`; my screen; scripts/n_sessions.py:7974–7975.
83. T4:2–24. Equal to S/step4b/gread/run/out.txt byte for byte. CONFIRMED (cmp).

T5, the launch review raw

84. T5:3. PI date 2026-11-25; Code (n-build). CONFIRMED. The review ran 2026-11-26T02:08:54Z–02:37:15Z, the evening of 2026-11-25 local.
85. T5:3–5. The line conventions. CONFIRMED. "Lines 83–86" and "Line 87" are v1's run block. The driver lines 855, 1428, 2897, 3954, 3963, 7888, 7968, 7975, 8170 and 8204 are as the report reads them.
86. T5:7–13. What was reviewed: v1 3d6a031f…7346 (133 lines); pkgsha.sh 4edcf928…6465 (13); the test 01dbf0c7…1c03 (28); the note 83cd30a4…2a74 (99). CONFIRMED (`shasum` and `wc -l`; v1:2–3, :20).
87. T5:15–16. The reviewer read the brief itself, as its prompt directed; 2eefa873…415e, 105 lines. CONFIRMED. The Agent prompt at 02:10:17Z begins "Your whole task is in a brief file. Read it…".
88. T5:17–31. The summary of the brief. CONFIRMED (review_brief_v1.md:12–23, :26–50, :64–105). See observation 4.
89. T5:33–34. §2 saved verbatim by jq from the hand-back; 250 lines; 72103a37…469a. CONFIRMED. T 02:37:15Z (`tail -n 2 | head -n 1 | jq` of the SubagentHandback message); cmp-equal.
90. T5:34. "It names scratch files only by their paths inside the scratch folder (`S/…`), and the notes file as `N/…`." IMPRECISE. The report's line 3 (T5:115) names "gread_steps_v1.sh" and "test_steps_v1.sh" by bare name. Put instead: "It names scratch files by their paths inside the scratch folder (`S/…`) or by bare file name, and the notes file as `N/…`; it holds no full local path."
91. T5:35. Its "about 5 GB of reads". FAIL. The report says "roughly 5 GB of reads on top" (T5:226; report line 114); "about 5 GB" is GR9's wording (gr_readings_v1.md:122). Put instead: "Its "roughly 5 GB of reads" is GR9's figure for the reads ("the reads of about 5 GB")."
92. T5:37–44. "In sum". CONFIRMED (the report's sections).
93. T5:46–49. "What came of it": v2 85dfa911…a023 (201 lines) and its note e6d52c71…f446 (105 lines), both read whole and checked by tool; the window's power words are the reviewer's. CONFIRMED. N/…-v2.md checked by `shasum` and `wc -l`; T's relay at 02:49:43Z; the grant's power text equals the report's "Window text".
94. T5:53–54. §1's source: e898a9d0…dc73, 60 lines, without its heading and first paragraph. CONFIRMED.
95. T5:56–109. Equal to the dispositions' lines 7–60. CONFIRMED (diff).
96. T5:113–362. Equal to the report. CONFIRMED (cmp).

T6, the expected RESULTS.md

97. T6 is HEAD's RESULTS.md with three insertions and nothing else. CONFIRMED. `diff` against `git show e114b3a:RESULTS.md` gives hunks 23a24,245, 479a702,712 and 1004a1238,1246, each cmp-equal to T1, T2 and T3; 41,739 + 242 = 41,981 lines.
98. T6's positions. CONFIRMED. T1 sits after the blank line below "## Log — Phase 2" (HEAD line 23). 0cc301d's entry runs from HEAD line 172 to 480, and T2 follows its last text line, 479. 05ac941's entry runs from 778 to 1005, and T3 follows its last text line, 1004.

== TOTALS ==
98 items: 88 CONFIRMED, 6 IMPRECISE (15, 55, 60, 63, 64, 90), 1 FAIL (91), 3 NOT CHECKABLE (51, 70, 71).

== OBSERVATIONS ==
1. A promised declaration is missing. N/2026-11-25_n-build_gread-launch-files-v2.md:90–93 ("Declared for my next entry") says: "the stand-ins' wrapper ran `cd` into the venv's bin folder and `[[ -x ./python ]]` there (no interpreter, nothing read), outside a battery window". T1's launch-v2 span names the stand-ins and "no Python", but not this. The read-only rehearsals' `pre` also tested the venv glob by builtins outside a window (02:40:28Z, 02:44:15Z). Suggest adding both to the v2 span item.
2. "The fits 9,832,753 ms" includes the fit stages' second reads of their cells. Each stage's `t0` is set before `probe_cell`, which reloads every cell through `load_cell` with arrays (scripts/n_sessions.py:8110–8140, :8143–8156). GR9's 2.650 and 2.769 h are fits alone. Suggest "the fit stages (each with its cells' second reads) 9,832,753 ms".
3. after prints the power source and the sleep and wake counts (v2:195) but asserts neither. In T1:47, "the power source AC and the sleep and wake counts equal to check's: PASS" reads as part of the PASS. Suggest "printed the power source, AC, and sleep and wake counts equal to check's; PASS".
4. T5:27–29's summary of the brief's bar on ckpt and reports files leaves out "hashed" (review_brief_v1.md:85–86: "read, listed, sized, timed or hashed").
5. "Besides them" leaves out the app's turn-plan calls (update_plan, wrap_up) in the spans. They are harmless, but the list claims to name every kind of call.
6. T1's Counts end at the draft's sweep. The file tools after it, and three reads whose outputs hold marker words, still need adding (listed below).

== THE SWEEP ==
Window: T's main-chain assistant records, Bash tool_use items, after 2026-11-26T01:48:39.235Z through the brief's hash at 2026-11-27T23:57:18.548Z: 124 commands, none duplicated.

Spans' counts, all equal to T1's: 27, 13, 4, 26, 3, 4, 35 (sum 112), with 12 after the draft's sweep. Every command in the window falls in a span.

Guard markers and names in argv and file-tool paths (bracketed, through 23:57:18Z):
- one marker (02:01:16Z) and one holding-folder name (23:39:46Z), which are T1's two departures;
- no plain Q-F3 name;
- nothing in the 12 later commands or in any file-tool path.

Kinds outside item 1 that T1's span lists do not name (time, kind):
- 2026-11-26T01:50:41Z: `grep -n -F`, `sed -n` and `cat -n` printing the BUILD entry draft's file-tools lines.
- 01:52:14Z: an unbracketed `grep -c -F` count of the scratch folder's name over the driver delta's added lines (T1 calls the counts there "bracketed").
- 01:55:31Z: the driver delta's added lines written to a build-folder scratch file by a `grep` redirect; `grep -n -F` line prints (cut to 40 characters) of the staging folder's last name in the commit folder's entry and review raw.
- 01:55:36Z: the same `grep -n -F` of that name in the same two texts, excerpted by `sed -E`.
- 02:00:55Z: `grep -n -E` of RESULTS.md for G-ANL-n's launch lines, into `cut` and `head`.
- 02:02:11Z: `grep -c ''` and `grep -n -E` of the launch-set note's headings, beside its `sed -n` (minor).
- 2026-11-27T23:41:38Z: `mkdir -p` of the record folder.
- 23:44:35Z: `tail -c 1 | od -An -c` of the out's last byte.
- 23:45:03Z: `shasum` and `grep -c ''` line counts of the two N notes, beside the launch files (minor).
- 23:47:05Z and 23:47:56Z: `cat -n` of RESULTS.md line ranges (minor).
- 23:47:38Z: e114b3a's whole message printed by `--format=%B` (item 64).
- 23:48:39Z: `mkdir -p` of the record's sweep folder, and `diff` of the BUILD's sweep script against its copy.

The 12 commands after the draft's sweep, for Code's list:
1. 23:49:03: bracketed `grep -n -i -E` and `grep -n -o -E` over the sweep's call list, with marker words and the holding-folder name masked by `sed -E` in the output.
2. 23:49:12: `sed -n` of one call-list line, `cut`, `sed -E` masking, `fold`.
3. 23:49:56: `grep -F` counts of command words over the call list (a `for` over fixed words), and `sed -n` of four of its lines.
4. 23:50:07: `nl -ba` numbering of the Bash calls, `grep -E`, `sed -E`, and a `while read` loop with `grep -o -E`, `tr` and `cut`.
5. 23:50:22: `git ls-files -- . ':!data/**'` into `grep -E` and `head`; `sed -n '161p'` and `sed -n '1,3p'` of PROPOSAL-n v0.2; `fold`.
6. 23:50:46: the Bash calls numbered by `nl -ba`, masked by `sed -E`, and written to a sweep-folder file; `grep -c` and `grep -n -E`.
7. 23:54:20: quotation checks (`sed` stripping bold from raw (A), then `grep -c -F` of four quotations; `sed -n` of the routing raw's lines 19 and 38 compared in the shell); width counts of the three texts; `jq` over the artifact.
8. 23:54:26: a width check of T3's draft (`grep -n -E`, `grep -v -F`, `cut`); one `awk` over /dev/null with its output discarded; a `while read` loop with `wc -m`.
9. 23:55:04: `bash -n` of make_results.sh and its run, writing a draft in scratch.
10. 23:56:08: line, width and placeholder counts of the three texts; make_results.sh run, writing S/step4b/gread/record/results_vc.md.
11. 23:56:20: the sources list written by `shasum` of its 20 files; `grep -c`; `shasum -c` into `grep -c`; `shasum` of the list; line counts.
12. 23:57:18: `diff` of the two values-check briefs' list-of-record sections; line count, sha256, width count and bracketed marker count of this brief.

File tools after the sweep, to the hash:
- 5 Reads: the sweep's output twice, the numbered call list twice, and the BUILD values-check brief.
- 5 Writes: T1, T2, T3, make_results.sh, and this brief.
- 9 Edits: T1's draft 7, T3's draft 1, make_results.sh 1.
- No message, subagent or ToolSearch.
- Outputs: marker words in three Reads (the sweep output at 23:49:19Z, 1 match; at 23:49:28Z, 26 matches over all five words; the BUILD values-check brief at 23:55:08Z, 7). None in any command output. No Q-F3 path or holding-folder name in any output.

Rule breaches after the sweep, as written: none found. The one call to flag is the `awk` at 23:54:26Z. No rule in the texts bars it for Code, but Code's v2 note calls an `awk` "my `awk` slip" and its BUILD entry declared one, so declare it.

== DEPARTURES ==
None that the brief's rules bar, as I read them. Disclosed for completeness:
- (a) one `cat` of exit.txt, a named S file, into `od` (`cat` is not among the brief's named tools; it is not an interpreter);
- (b) two commands carried environment prefixes named `awk_free` and `gsub_free` on `cut` (no `awk` ran);
- (c) one jq output went `> /dev/stdout` inside a pipe (zsh duplicated the stream; no file was written);
- (d) one stray `grep -c`, its pattern bracketed, named a file operand that does not exist (error to /dev/null; nothing read);
- (e) `git check-ignore -v` on the artifact's path (ignore rules only; its bytes were not read), and `git diff 05ac941 0cc301d -- .gitignore`, a cited, named file;
- (f) one transcript search printed parts of unrelated records (record metadata, the opening line of a compaction summary, and a later tool result's head) beyond what a finding needed.
I wrote no file anywhere and used no network.
```
