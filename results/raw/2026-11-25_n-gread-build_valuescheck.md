# n — G-READ-n's BUILD (the `gread` command in scripts/n_sessions.py): the blind values-check, as returned, with every disposition

PI date 2026-11-25. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the BUILD's drafted texts, at HEAD `05ac941`:
- T1, the BUILD's entry, `0afcdc44…8611` (214 lines), its four placeholders not to be checked;
- T2, the review raw's head and dispositions, `072fdf13…fb60` (109 lines), with the report to be appended verbatim
  as its §2;
- T3, the self-test raw, `068a8914…07e2` (61 lines), its one placeholder not to be checked;
- T4, draft 2's G-READ-n texts (`176aef3d…a826`, 9,021 lines): the module docstring's `gread` paragraph and its last
  line, the G-READ-n section's docstrings, comments and self-test check names, and main()'s gread messages;
- T5, the `.gitignore` draft (`3aac58be…6482`, 424 lines): the lines of its delta from HEAD's.

**The parent.** The BUILD commits on `b449ed6`, the Q-F3 campaign's record, committed on `05ac941` after the check
began and pushed with it in the coordinating session's push #28. From `05ac941`, outside item 3's exclusions and
Q-F3's folder, it changes `RESULTS.md` and adds two raws (`git diff --name-status`); the driver, the `.gitignore` and
every overlay path are unchanged, and no text cites `RESULTS.md` by line.

**The checker's brief** was a file the checker read itself, as its prompt directed: Code's scratch file
`S/step4b/gread/build/vc_brief.md` (`fba045d7…010b`, 145 lines). It:
- named the texts and the sources. In the repository: the files the texts cite, at `05ac941`. In Code's scratch, by
  a sources list at its sha256 (`fbc6eba7…1a69`, 28 files): the five texts; draft 1 and HEAD's driver as copied; the
  three deltas; the review's brief and report; the runs' outputs (each run's `.txt`, `.err` and `.exit`); the two
  closure files the `hashes` run was compared through; HEAD's `.gitignore` as copied; the two overlay scripts
  (G-READ-n's and G-VER's); Code's readings GR1–GR14 as sent; and launch set v1's `camp_hashes_v1.txt`. Beside
  them, the two self-test overlays by their names, `diff -rq` and their drivers' hashes only. In the sessions' notes
  folder: Code's two battery-window requests and the seat block's window request. In this session's transcript: the
  coordinating session's relays, for the texts' claims about the windows;
- allowed `shasum`; `jq` on committed JSON and on this session's transcript; and `sed -n`, `/usr/bin/grep`, `cut`,
  `diff`, `cmp`, `od`, `wc -l`, `tr`, `sort`, `uniq` and `git diff --no-index` on the named scratch files. It barred
  any other interpreter (`awk` among them), any write, any network, any guard marker in an argv (a grep pattern and
  the command's own text included), and globs over the root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file, anything outside the
  repository but the named files (the staging folder above all), and any naming of G-TIME-n's holding folder in an
  argument;
- asked for a sweep of Code's shell commands from the seat block entry's final sweep (2026-11-25T23:39:31.244Z, T's
  UTC stamp) to the command that hashed the brief, in T1's three spans with T1's counts, and the kinds after the
  draft's sweep (2026-11-26T00:54:56.023Z), for T1's list of them; and T1's counts of markers and folder names in
  commands and outputs;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (448 lines, sha256
`d27748db1a79efbe5c62383c7f7ce20b4b0f18b71158ae5fbb5b2d8959c265f4`). It names scratch files as S/..., the sessions'
notes folder as N and the transcript as T. Its times are T's UTC stamps: 23:xx on 2026-11-25, 00:xx on 2026-11-26.

**Totals:** 108 items: 89 CONFIRMED, 14 IMPRECISE, 1 FAIL, 4 NOT CHECKABLE; and 11 observations.

**The checker's departures,** as its report states them, are in the BUILD entry's departures, for the seat to class.

## 1. Dispositions

Each text was edited as a v2 copy of the draft the checker read (S/step4b/gread/build/entry_v2.md, review_head_v2.md
and selftest_raw_v2.txt), by the file tools only, and each edit is replayed by tool in §2. The driver's three changes
are draft 3's (`35c4c73e…4808`, +10 −6 from draft 2), with its own self-test window.

**The FAIL item:**
- **Item 54, T1's file-tools line.** Applied in the checker's words, "Across the spans", with the spans' one subagent
  named (the review); the values-check's own call is among the commands after the draft's sweep.

**The fourteen IMPRECISE items:**
- **Items 10 and 32, the second reads (T1).** Applied in the checker's words: the 128 cells the fits use (the shadow,
  N1-R's 120, N1-V's five valence cells and N2-E's two) are read a second time, and the ten others (N1-P's four, N2-S's
  two, N2-C's two, N4-T's and N4-Ts') once. Code checked the count against `schema.ARM_CELLS` and the fit loop.
- **Items 19 and 87, "every line count" (T1, T3).** Applied in the checker's words: "every count of lines added and
  removed".
- **Item 26, the runs' mode (T1).** Applied: the self-tests as the harness's background task, `hashes` in the
  foreground after run 1. Window 1's note named the background task for the self-test, and `hashes` by its command.
- **Items 28 and 70, F7 (T1, T2).** Applied in the checker's words: "F7 in part (four refusal cases, its sentence
  narrowed)" and "the wording of F8–F10".
- **Item 33, GR13's words (T1).** Applied: "not by the package's own writer, as GR13 says (`cells.append_record`,
  record by record)".
- **Item 53, the parts no span names (T1).** Applied as a new item, "Also, in the spans", with the parts the sweep
  lists, `git status --porcelain -- results/raw` among them.
- **Item 57, the outputs with marker words (T1).** Applied in the checker's words: four commands' outputs, the sweep's
  own among them.
- **Items 82 and 97, "fifteen in all" (T2, T3).** Applied in the checker's words: fifteen refused argvs.
- **Item 102, `_gread_prepare`'s docstring (T4).** Applied in draft 3 in the checker's words, with "the artifact and
  its temporary file absent" (Code's, as T1's list of refusals has it).
- **Item 103, `_gread_err`'s docstring (T4).** Applied in draft 3 in the checker's words; T2's F4 says so too.

**The eleven observations:**
- **1.** Applied: a Declared item in T1, GR13's "every refusal of GR8 and GR2, one tampered input each", built for the
  refusals a tampered input can reach.
- **2.** Applied: a Declared item in T1, GR3's sentinels, where GR3 as sent says every margin field.
- **3.** Applied in draft 3: one refusal case, a relative staging folder naming the tampered stand-in copy `st_byte`
  from the repository's root (`os.path.relpath(st_byte, REPO)`), refused at its byte check. Read against a working
  folder other than the root, the same string names another path, and the run is refused otherwise. The self-test now
  has 33 refusal cases and 854 checks, and T1 and T2 say so.
- **4.** Applied with item 103: T1's exits item says "stricter where an OSError has no strerror", and T2's F4 names
  the difference.
- **5.** Applied: T1 says "adapted", with the two differences (the report's cells where the analyzer has `camp.cells`;
  the messages without its example names and merge lists), checked by Code against anl:6459–6484 and the driver's
  function.
- **6.** Applied in T1: "`--selftest`, which the driver takes before any command, runs the self-test, here as
  everywhere".
- **7.** Applied: T1's code-read item names the `grep` of `valence_core/adapters/base.py` and no `sed -n` of the
  analyzer (the review item's, of `_err_where`, is the only one; the code read's was a `grep`). Code checked both
  against its sweep's list.
- **8.** Applied: span 1's heading says the note gives the kinds but for its own check's, by `grep -c` where the note
  says `wc -l`.
- **9.** Applied in T3: `hashes` after run 1's end, run in the foreground.
- **10.** Applied in T2: the "In sum" item names the reviewer's third departure whole.
- **11.** Applied in T1: the staging folder is checked fourth, before the driver, the lock, the package, the close
  list, the report and the seeds.

**The four NOT CHECKABLE items** (41, 61, 62 and 98) are Code's plans and the box's not having run this BUILD. Item
61, the gate's id list: the gate is v20, its list holding the review's and this checker's agent ids beside v19's,
and the commit's verify checks the rest.

**The sweep.**
- Its parts that no span names are in T1's new item (item 53), and its two file-tool calls in the notes folder are in
  the file-tools line (item 54).
- Its span counts are T1's: 11, 8 and 45.
- Its kinds after the draft's sweep, to the brief's hash, open T1's list of Code's commands after that sweep, which
  runs to this entry's final sweep.

**Code's own changes beside the items** (no check read them):
- the windows' closes (T1, T3), from the coordinating session's relays, and the parent `b449ed6` (T1, T3), by
  `git diff --name-status`;
- in T1: the file-tools line's one subagent for the spans; the values-check's summary; the values-checker's
  departures; draft 3's lines; and the list of Code's commands after the draft's sweep, with the final counts;
- in T2: draft 3 in "The draft after it", and under F3, F4 and F11; in T3: run 3 and overlay3.

**Draft 3** (`35c4c73e…4808`, +10 −6 from draft 2), the BUILD's driver, carries items 102 and 103 and observation 3.
No check reads it but its self-test: it passed, 854/854, in its own battery window (run 3; its output `17e27be2…68a4`),
and the coordinating session's close found its files at Code's sha256s and the overlay and the draft unchanged.

## 2. The edits, replayed

The edits were made to new versioned copies of the three texts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/gread/build/edits_check.sh`. The results are byte for byte the revised texts, so nothing else changed after
the check:
- the entry, 24 of 24 edits; the review raw's head, 7 of 7; the self-test raw, 11 of 11.

They are, in order of time: the windows' closes and the parent, made while the check ran; this check's dispositions,
with draft 3's lines; after draft 3's window, its run and the third window's close; and the commit-time fills (the
list of Code's commands after the draft's sweep and the final counts). After the edits, three placeholders were filled
by tool: this raw's sha256 and length in the entry, and the entry's count of these edits.

## 3. The report as returned

```text
VALUES-CHECK REPORT: G-READ-n's BUILD texts (T1–T5), at HEAD 05ac941

Inputs checked first: the brief at its sha256 (fba045d7…010b, 145 lines). The sources list, S/step4b/gread/build/vc_sources.txt, is at fbc6eba7…1a69 (28 lines), and `shasum -a 256 -c` returned 28 of 28 OK. The three N files are at their sha256s and line counts (909ac27f…ec67, 79; 7aeaa863…cc92, 69; e909f487…9820, 117). HEAD is 05ac941. Every repository source is clean at HEAD, except that RESULTS.md has a working-tree change, so I read it with `git show 05ac941:RESULTS.md`.

Short forms used below:
- D1 = S/step4b/gread/draft/n_sessions.py
- D2 = S/step4b/gread/draft2/n_sessions.py
- drv = scripts/n_sessions.py at 05ac941 (equal to S/step4b/gread/draft/head_driver.py by blob)
- anl = scripts/n_analyze.py
- GR = S/step4b/gread/spec/gr_readings_v1.md
- RR = S/step4b/gread/review_report.md
- STOP = results/raw/2026-11-25_n-gread-starred-two_code-to-design_STOP.md
- spec = results/raw/2026-11-25_n-gread_spec.md
- ans4 = results/raw/2026-11-25_n-campaign-close-read_design-to-code_answers.md
- ans21b = results/raw/2026-11-21_n-gtime-starred-seven_design-to-code_answers.md
- Times are T's, in UTC: 23:xx is 2026-11-25 and 00:xx is 2026-11-26.

ITEMS

T1 (S/step4b/gread/build/entry_src.md)

1. T1:1–3. G-READ-n is n v0.2 §8 step 15, built on the PI's "build on the pins", in the driver alone (package at the lock's digest, analyzer at v7), and not run.
   CONFIRMED. n:159 ("15. G-READ-n from the captures; …"). spec §2 quotes the PI's "push both and build on the pins". T holds no gread invocation.

2. T1:4–5. LOCK-n.md is the same at 098218c and HEAD; "L §N" is v0.1's section form.
   CONFIRMED. The blob is 2f865790… at 098218c, 05ac941 and HEAD. Its sha256 is 59e0b1bc…00aa = LOCK_SHA256 (drv:3894). v0.1 starts at LOCK-n.md:396, and the driver writes "L §18" and "L §6".

3. T1:6–9. ans4 §3 points 1–2. `valence_core/n/` stays at 06b55761…1d39 (L §18). `scripts/n_analyze.py` is v7, 735da934…a7a8 (LOCK-n.md:212–215).
   CONFIRMED. ans4:29–30; LOCK-n.md:1176; LOCK-n.md:212–213 hold the sha. The overlay script printed "package by shell 06b55761…1d39" for both overlays (T 00:09:32, 00:47:41). `shasum` of anl gives 735da934…a7a8.

4. T1:10–11. GREAD_CLOSE_LIST_SHA256 is the close list's sha256 as committed at 95cd461, 42682630…fe6d.
   CONFIRMED. `shasum`; `git log --format` names 95cd461 alone; D2:7737.

5. T1:11–13. The seeds are the lock's (LOCK-n.md:322, :823–825) and are held to probe.py's. The band is 33–63 (LOCK-n.md:869), the cells 138, the matching LOCK-n.md:964–965's.
   CONFIRMED. LOCK-n.md:322, :823–824, :869, :964–965; valence_core/n/probe.py:48–49; D2:7740–7747 and :8027–8028.

6. T1:14–16. `gread --staging DIR` (run_gread) is one invocation. A relative DIR is read from the repository's root. A refusal exits 1 with a REFUSED line and nothing written.
   CONFIRMED. D2:7967 and :8194–8218. Nothing is written before gread_write.

7. T1:17–36. The thirteen refusal conditions, in this order.
   CONFIRMED. Each is at its line in D2, in the stated order:
   - pod: 7955
   - known answer: 7957–7959
   - artifact and .tmp absent: 7960–7966
   - staging folder: 7967–7972
   - driver and LOCK: 7976–7982 (gver_lock_check, drv:5239–5246)
   - package: 7983–7989
   - close list: 7990–7995, with gread_close_list at 7763–7782
   - report: 7996–8025 (HEAD's bytes, the first line, check_report, COMPLETE and per_arm, stage and lock, package equal to the pin and the process's, layers, the plan pin and the plan's own sha256, the identity sha256, 138 cells)
   - dose map: 8026 (gread_points, 7785–7801)
   - seeds: 8027–8028
   - paths and json_sha256: 8029–8037
   - re-hash by name, symlink or non-file refused: 8043–8055
   - cells: 8056–8064 (load_cell with identity=None; FileNotFoundError becomes a refusal at 7834–7835)

8. T1:37–41. The shadow's rows are read once and held. The comparator comes first: 4 points × 24 directions × each layer, layer_auc without shuffles, then a band median. At +1 each direction's +1 is against its own −1; the other points use the shadow's rows for the 40 floor sessions. The first call is computed twice, and unequal AUCs refuse the run before the primary fits.
   CONFIRMED. D2:8101–8139 and :7815–7823; schema.py:279–283 (24 RANDOM_IDS) and :540–544 (N1-R 40).

9. T1:41–43. Six results by probe.result at 200 shuffles and the lock's seeds, pole or shadow, N2-E's cells, matched as stated.
   CONFIRMED. D2:8140–8155 and :7746–7747; probe.py:45, :48–49, :104.

10. T1:44–45. "Each cell is read a second time, arrays kept, held to the report again, its rows copied before the next cell is opened."
    IMPRECISE. Only the cells the fits use are read again, 128 of them: the shadow, N1-R's 120, N1-V's five valence cells and N2-E's two. The ten others are read once, in the first pass: N1-P's four, N2-S's two, N2-C's two, N4-T's and N4-Ts'. Evidence: D2:8058–8064 against :8093–8145; schema.py ARM_CELLS; RR R4.
    Instead: "Each cell the fits use (128 of the 138: the shadow, N1-R's 120, N1-V's five valence cells and N2-E's two) is read a second time, arrays kept, held to the report again, its rows copied before the next cell is opened."

11. T1:45. From each record the command keeps its session_id and capture row alone (GR3 ★).
    CONFIRMED. D2:7838–7850.

12. T1:46–49. The artifact is built by probe.artifact and checked by check_gread. It is held to anl:6459–6484 (gread_binding_problems) and written in G-ANL-n.json's form (sorted keys, one-space indent, final newline), through a temporary file renamed onto an absent path. It is read back, and a failed read-back removes it. The .gitignore admits it.
    CONFIRMED. probe.py:116–135 (check_gread at :134); anl:6459–6484 (gread_problems) and :4603–4606 (json_text, the same json.dumps arguments as D2:8160); D2:7853–7910 and :8156–8179; T5.

13. T1:50–54. The printing (GR11), with the staging folder printed relative to the repository and never a margin or a per-session value.
    CONFIRMED. D2:7973–7975, 7980–8067, 8089–8091 (python, numpy, BLAS, CPUs, five variables set or unset), 8104–8105, 8133–8139, 8152–8155, 8169–8171. The folder is printed by os.path.relpath (7974).

14. T1:55–58. The exits: 0 when written, 1 on a refusal or failure with no artifact. A refusal prints its reason and a failure its cause through _gread_err. Warnings come after the end line by category and message. 2 is argparse's.
    CONFIRMED (see O4). D2:8183–8218; main's ap.error at 8879–8894.

15. T1:59–60. main(): `--staging DIR` is gread's only option and every other option is refused; `--staging` is refused for every other command; no smoke, no --out, no resume.
    CONFIRMED (see O6). D2:8868–8895; the self-test's argvs at 8799–8813.

16. T1:61–69. The self-test's content: in cmd_selftest after the campaign's; the pins; the stand-in campaign (138 cells, 7,680 records, three layers of width four, sentinels in the margin, its two log-probability sums and their fresh copies); the flow with a recorder, inputs row for row, band medians in order; the artifact's form and binding; 32 cases; a stale .tmp; a failure; a failed read-back; the writer; six tampered copies; layer_auc twice on 80 rows; main()'s options behind the traps.
    CONFIRMED. D2:589–598 and :8274–8831. Cells: 6 + 120 + 4 + 2 + 2 + 2 + 1 + 1 = 138. Reads: 960 + 4,800 + 640 + 3 × 320 + 2 × 160 = 7,680 (schema.py ARM_CELLS and read_plan, nothing merged; D2:8296–8299). Sentinels at D2:8327–8328, with 6.9375 = −0.109375 − (−7.046875); fresh copies at schema.py:1710–1712.

17. T1:70–71. The docstring lists GR1–GR14 in short as sent, GR9's line carrying the departure; its last line names VERDICTS as the analyzer's, with `--gread`.
    CONFIRMED. D2:380–406 against GR and spec:26–41.

18. T1:72. Draft 2 is 176aef3d…a826, 9,021 lines, +1,188 −3 from 47abe489…c21a.
    CONFIRMED. Sources list; line count; numstat 1188/3. head_driver.py equals drv (blob 0a7cdab3…, sha256 47abe489…c21a).

19. T1:72–73. "Every line count in this entry is `git diff --no-index --numstat`'s."
    IMPRECISE. 9,021 and 8,834 are file lengths, not numstat figures.
    Instead: "Every count of lines added and removed in this entry is `git diff --no-index --numstat`'s."

20. T1:74–75. Draft 1 is 5a1d84a3…24e8, 8,834 lines, +1,001 −3; draft 2 is +260 −73 from draft 1.
    CONFIRMED. Numstat 1001/3 and 260/73. The saved deltas' bodies equal fresh diffs by `cmp`.

21. T1:76–78. The .gitignore is 3aac58be…6482, +3 −0: after G-ANL-n.json's admit, a comment and the admit line. The .tmp and any other gates file stay ignored.
    CONFIRMED. The diff from head_gitignore (blob 353474d1 = HEAD:.gitignore) adds lines 331–333 after line 330: a two-line comment and the admit.

22. T1:78–79. The dry-run test in a throwaway repository: the draft admits the artifact and G-ANL-n.json alone, and HEAD's admits G-ANL-n.json alone.
    CONFIRMED. T 00:09:01: four stand-ins (G-READ-n.json, its .tmp, G-ANL-n.json, other.json). The output adds G-ANL-n.json and G-READ-n.json under the draft, and G-ANL-n.json alone under HEAD's.

23. T1:80–82. Draft 1 printed "833/833 n selftest checks pass": 774 + 59 (58 + the environment check).
    CONFIRMED. S/step4b/gread/selftest_run1.txt (e9488af8…). results/raw/2026-11-23_n-campaign-build_selftest.txt:68–76 shows 47abe489…c21a at 774/774. D1 has 27 static `chk(` calls, two of them in loops, with 26 cases and 7 argvs: 25 + 26 + 7 = 58. The wrapper is at D2:598.

24. T1:83–84. `hashes` printed the lock's package digest and twelve closure lines equal to LOCK_CLOSURE by `cmp`, so the package check passes on this laptop.
    CONFIRMED. hashes_run1.txt line 1 holds 06b55761…1d39. closure_lock = closure_laptop by `cmp` (3a0a5988…). My rebuild of drv:3905–3916 equals closure_lock. cmd_hashes (drv:396–402) and _package_closure (drv:4297–4299) call the same guard functions after the same imports.

25. T1:85. Draft 2 printed "853/853", 20 checks more.
    CONFIRMED. selftest_run2.txt (7898ee01…). D2 has 33 static calls, 32 cases and 15 argvs: 31 + 32 + 15 = 78, and 774 + 1 + 78 = 853.

26. T1:86–87. "Each run had exit 0 and an empty stderr, … as the harness's background task; the temporary folder was empty before and after each."
    IMPRECISE. The self-tests ran as background tasks (T 00:13:26, 00:49:38), but `hashes` ran in the foreground (T 00:14:15). The rest holds: three "exit 0" files, empty .err files, and TMPDIR counts of 0 at 00:10:07, 00:13:56, 00:14:27, 00:47:41 and 00:50:10 and in both grants.
    Instead: "Each run had exit 0 and an empty stderr, in a battery window the coordinating session granted for its bytes, the two self-tests as the harness's background task and `hashes` in the foreground after run 1; the temporary folder was empty before and after each."

27. T1:88–91. The review found no BUG, and 12 findings (6 RISK, 6 NIT), 10 surviving mutants, 8 run risks and 9 observations.
    CONFIRMED. RR:16, F1–F12, M1–M10, R1–R8, O1–O9.

28. T1:92–93. "draft 2 builds in F1–F6 and F12, R5 and O6, the wording of F7–F10, and a kill for every mutant …"
    IMPRECISE. F7 was also built in code: four of its refusal cases are in D2:8659–8666 (the listed JSON's sha256, a cell's identity, the shuffle seed, a staged symlink). T2's own disposition says "Applied in part". No mutation run appears in T.
    Instead: "draft 2 builds in F1–F6 and F12, F7 in part (four refusal cases, its sentence narrowed), R5 and O6, the wording of F8–F10, and a kill for every mutant by Code's reading (no mutant has been run)."

29. T1:95. Nothing ran on a model.
    CONFIRMED, as far as T shows. The only interpreter runs are the two self-tests and `hashes`, and the HF cases are skipped on the laptop (valence_core/n/hftiny.py:6, :56).

30. T1:96–99. The twelve unstarred readings stand as §1 has them, with the head's points: GR7's classifier reaches the probe through kfold_scores, and GR8's absence test is the command's own beside guard.refuse_out.
    CONFIRMED (see O1–O2). spec:36–41; valence_core/echo/probe.py:78–97; valence_core/n/guard.py:74–81; D2:7960–7966.

31. T1:100–101. GR9 as built opens one cell's maps at a time, with the shadow held; GR9 as sent says two at a time.
    CONFIRMED. GR:124–125; D2:8093–8100 and :7838–7850.

32. T1:102–103. "Every cell is read twice through `load_cell`: all 138 before any fit, and the probed ones again …"
    IMPRECISE. The ten unprobed cells are read once (as in item 10).
    Instead: "Every cell is read through `load_cell` before any fit (all 138), and the 128 probed ones a second time, arrays kept, each held to the report again (the review's F5)."

33. T1:104–106. The stand-in's file forms are as stated (D2:8343–8363, read back at 8380). The text adds: "not record by record through `cells.append_record`, as GR13 says".
    IMPRECISE. GR13 says "by the package's own writer" (GR:151–153) and names neither append_record nor "record by record".
    Instead: "…; not through the package's own writer as GR13 says ("by the package's own writer": `cells.append_record`, record by record), for the self-test's time."

34. T1:107–109. The recorder follows probe.py's own self-test's pattern; result and artifact run for real; the 200-shuffle fits are probe.py's self-test's.
    CONFIRMED. probe.py:180–197; D2:8409–8423.

35. T1:110–112. The binding conditions are copied into the driver, which does not import the analyzer. The writer is the section's own, not atomic_write_json.
    CONFIRMED (see O5). D2 holds no n_analyze import; atomic_write_json appears only in the self-test (8358, 8589); D2:7881–7910.

36. T1:113–114. The staging folder is checked before the driver, the lock and the package, where GR8 lists it last (F11).
    CONFIRMED. D2:7967–7972 before 7976; GR:114–117; RR F11.

37. T1:115–117. "Or their merged points" is not built and a map that drops a point is refused (O7); a second repeat check at 320 rows is not built (O6).
    CONFIRMED. LOCK-n.md:965; D2:7785–7801; RR O6 and O7.

38. T1:118–119. Each starred reading sits in one place: GR3 in gread_load with gread_rows, GR5 in gread_comparator_cells.
    CONFIRMED. D2:7815–7850; STOP:99–103 and :126–128; RR O3.

39. T1:121–123. GR14's steps as carried; ans4's "beside Q-F3"; Q-F3 has ended (the coordinating session's fact).
    CONFIRMED. GR:162–169; ans4:32. T relay 23:46:40: "the Q-F3 campaign has ended (f3-build's report: ended, EXIT=0)".

40. T1:124–125. `--staging` given relative to the root reaches the staging folder, and no local root reaches the raw.
    CONFIRMED as to the code (D2:7967, with the folder printed relative at 7974). The launch files themselves are Code's plan.

41. T1:126–127. The out and err raws are screened (R7), and the run comes after the ruling and the routing.
    NOT CHECKABLE (plan).

42. T1:129–130. The sweep runs from T's 23:39:31 UTC on 2026-11-25, by `jq` over T.
    CONFIRMED. T 00:51:07 and 00:54:56.

43. T1:131–140. Span 1: 10 commands whose kinds the note gives, then one more. The bracketed grep's output named the holding folder once, at its line 97.
    CONFIRMED (counts; see THE SWEEP for unnamed parts). T shows 11 Bash calls from 23:40:28.952 to 23:44:01.048. The N request's section lists nine commands and the note's check. My bracketed count gives one match, at LOCK-n.md:97.

44. T1:141–147. Span 2: 8 commands.
    CONFIRMED (see THE SWEEP). T 23:47:04.444–23:48:02.465.

45. T1:148. The BUILD span: 45 commands, the sweep included.
    CONFIRMED. T 23:49:44.685 to 00:54:56.023.

46. T1:149–155. The code read, including one `cat -A` that BSD cat refused, run again with `sed -n`.
    CONFIRMED (see O7 and THE SWEEP). The 23:53:12 output reads "cat: illegal option -- A"; the rerun is at 23:53:21.

47. T1:156–163. Draft 1's commands.
    CONFIRMED (see THE SWEEP). The overlay script ran on commit 05ac941232bc… (00:09:32).

48. T1:164–168. Window 1. One `ps` count found one python process that was not Code's, and the coordinating session's later scan found none.
    CONFIRMED. The ps output was 1, after both runs had ended. Relay 00:15:41: "no process whose executable is python is running".

49. T1:169–171. The review's commands.
    CONFIRMED. T 00:17:04 and 00:41:32 (`tail -n 2 | head -n 1` into `jq`; `sed -n` of anl:4606–4625).

50. T1:172–176. Draft 2's commands, including one `grep -P` that BSD grep refused, with its fallback `echo` printed.
    CONFIRMED. The 00:47:09 output reads "no -P", and relay 00:49:31 notes the slip.

51. T1:177–178. Window 2.
    CONFIRMED. T 00:49:38 (background) and 00:50:10.

52. T1:179–182. The commands for these texts, and the sweep.
    CONFIRMED (see THE SWEEP). T 00:50:27–00:54:56.

53. T1:129–183, the list as complete ("Code knows of no others").
    IMPRECISE. Parts outside item 1 that no span names are listed with their times in THE SWEEP.
    Instead, add before @REST@: "- **Also, in the spans:** `head` and `tail` on command outputs and on files (the close list's first lines and last byte, the entry's last bytes, the gate's and the verify's outputs, the saved report); `od -An -c` of two last bytes; `fold -w 200` on two definitions greps; `cat` of an earlier known-hashes file in scratch; `mkdir -p` of six scratch folders; `grep -n -E`, `sed -n` and `cmp` of `.gitignore`; and the verify output's `wc -l` and `shasum`."

54. T1:184–186. The file-tools line.
    FAIL. To the sweep, T shows:
    - memory files: Reads of MEMORY.md (3) and Edits of MEMORY.md (2) and of the memory note (6), with no Write of any memory file;
    - in N: three Writes, plus an Edit of the seat block's request at 23:43:14 (before its sha256 at 23:43:17 and the message at 23:43:36) and a Read of the campaign's self-test window request of 2026-11-23 at 23:49:47; the line names neither;
    - span 2 had no file-tool call at all.
    Instead: "**Across the spans, the file tools:** Reads and Edits of the memory index and Edits of a memory note (outside scratch); in the sessions' notes folder, Writes of the three window requests, one Edit of the seat block's request before its sha256 was taken, and one Read of the campaign BUILD's self-test window request of 2026-11-23; Reads of repository files and of scratch files; Writes and Edits in scratch."

55. T1:186–188. Seven messages and two subagents.
    CONFIRMED. SendMessage at 23:43:36, 23:48:21, 00:11:20, 00:14:10, 00:14:53, 00:48:28 and 00:50:25 (three window requests, the seat block's done report, three window reports). Agent at 00:17:09 (the review) and 00:57:13 (this check).

56. T1:189–190. No guard marker, no plain name of Q-F3's folder and no name of G-TIME-n's holding folder in any argv.
    CONFIRMED. A `jq` scan of every tool input from 23:39:31.244 to 00:57:09, commands and file paths, with bracketed patterns, gives 0 in each class, the bare short name included.

57. T1:191–193. Marker words in five file-tool reads and "three commands' outputs".
    IMPRECISE. The five reads hold: 23:50:21, 23:51:01, 23:51:30, 23:53:57 and 00:15:51. So do the three outputs: 23:53:43 (one marker word), 23:55:42 (two) and 23:55:46 (one). But the sweep's own output (00:54:56.023, inside the span) holds all five, as the list of words it found.
    Instead: "…and four commands' outputs (`sed -n` of the driver's lines with `guard.py`'s; `grep` of `valence_core/adapters/base.py`; `sed -n` of m's `resume.py`; and the sweep's own, which lists the words it found);"

58. T1:194. Q-F3's folder's bare short name, in one read and one output.
    CONFIRMED. 23:53:57 (the read) and 23:53:43 (the output); guard.py:30.

59. T1:195–196. G-TIME-n's holding folder's bare name in two reads and two outputs, the close window note's also in its noindex/n/ form.
    CONFIRMED. Reads at 23:50:11 and 23:50:21; outputs at 23:40:28 (1) and 23:42:15 (1, plus 1 in the noindex/n/ form).

60. T1:197–202. The reviewer's departures.
    CONFIRMED. RR DEPARTURES 1–3.

61. T1:204–206. The gate's id list.
    NOT CHECKABLE (a future gate version). The N seat-block request (lines 57–59) confirms that v19 holds the survey's and that values-checker's ids.

62. T1:207–213. The commit by path, the home-folder count of 0, not pushed, and the launch's order.
    NOT CHECKABLE (plan).

T2 (S/step4b/gread/build/review_head_src.md)

63. T2:3–4. LOCK-n.md is the same at both commits, and TO:N is a line of draft 1.
    CONFIRMED. Blob as in item 2; RR:3.

64. T2:6–9. Driver 47abe489…c21a to draft 1 5a1d84a3…24e8 (8,834 lines); .gitignore fe865233…03ed to 3aac58be…6482, three lines after the G-ANL-n admit.
    CONFIRMED. Sources list; head_gitignore = HEAD:.gitignore by blob.

65. T2:11–12. The review followed the 833/833 run and `hashes`.
    CONFIRMED. Window 1 ran at 00:13–00:14; the review was spawned at 00:17:09.

66. T2:14–26. The brief: S/step4b/gread/review_brief.md, 458aa49b…5cfd, 132 lines, read by the reviewer as its prompt directed. Its contents, including twelve known items, the bars, the verbatim items 1–5 and the pathspec with `data/m[f]3`.
    CONFIRMED. review_brief.md:28–62, :63–85 (12 bullets), :87–100, :103–132; prompt at T 00:17:09.

67. T2:28–31. The report is in §2, extracted verbatim by `jq`, 234 lines, 690b5daf…1d32, naming scratch files by S paths only. Its slip "458aa49b…fcfd" is 5cfd by tool, and the prompt gave the sha256 in full.
    CONFIRMED. T 00:41:32; line count; local-path count 0; RR:6; the prompt gives 458aa49b…5cfd in full.

68. T2:33–40. The "In sum" list.
    CONFIRMED (see O10). RR.

69. T2:42–45. Draft 2: 176aef3d…a826, 9,021 lines, 20 checks more (6 chk calls, 6 cases, 8 options), checks extended, a three-layer band, 853/853 in its own window.
    CONFIRMED. delta_from_draft1.diff (six new chk calls, six cases, eight argvs); T 00:49:38.

70. T2:42–43. "the wording of F7–F10".
    IMPRECISE (as item 28).
    Instead: "builds in F1–F6 and F12, F7 in part (four refusal cases, its sentence narrowed), R5 and O6, the wording of F8–F10, and a kill for every mutant, …"

71. T2:49–51. F1.
    CONFIRMED. D2:7963–7966 and :8680–8688.

72. T2:52–55. F2.
    CONFIRMED. D2:7891–7910, :8163–8179 and :8690–8717.

73. T2:56–59. F3, including "which a reading against the working folder would not give".
    CONFIRMED for the runs of record (see O3). In an overlay, REPO is the overlay (drv:366), while the working folder, the venv's bin folder, lies inside the repository but outside the overlay; so a working-folder reading of `data` gives "not a folder". D2:356, :7967, :8893–8894, :8657–8658.

74. T2:60–63. F4.
    CONFIRMED (see O4). D2:8183–8217; anl:4611–4619.

75. T2:64–65. F5.
    CONFIRMED. D2:8093–8100.

76. T2:66–69. F6.
    CONFIRMED. D2:8323–8326 and :8492–8505.

77. T2:70–75. F7.
    CONFIRMED. D2:8656–8666, :8718–8748, :8235–8238.

78. T2:76–78. F8.
    CONFIRMED. D2:8228–8229; schema.py:1702–1703.

79. T2:79–82. F9 and F10.
    CONFIRMED. D2:8238–8239, :8763–8766, :396–397; T1:68.

80. T2:83–86. F11 and F12.
    CONFIRMED. T1:113–114; D2:8402 and :8427–8429; guard.py:36 (GuardStop is a SystemExit) and :84–88.

81. T2:87–91. Each of M1–M10 is killed, by reading.
    CONFIRMED. M1 and M9: 8502–8505; M2: 8693–8698; M3: 8699–8717; M4: 8388; M5: 8799–8813; M6: 8718–8734; M7: 8656; M8: 8735–8748; M10: 8532.

82. T2:89–90. "eight more refused options in main()'s loop, fifteen in all".
    IMPRECISE. The fifteen are argvs, not options: gread without --staging, eleven gread argvs carrying a foreign option, and three other commands with --staging (D2:8799–8813). The N draft-2 request (lines 64–65) itself says "15 refused argvs".
    Instead: "M5 by eight more refused options in main()'s loop, whose refused argvs are fifteen in all;"

83. T2:92–98. R1–R8.
    CONFIRMED. RR R1–R8; D2:8149.

84. T2:99–106. O1–O9, and the reviewer's departures declared in the BUILD entry.
    CONFIRMED. RR O1–O9; D2:8086–8091; T1:197–202.

T3 (S/step4b/gread/build/selftest_raw_src.txt)

85. T3:1–2. The header.
    CONFIRMED.

86. T3:4–5. HEAD is 05ac941 and the driver's last change e1be6d9; 47abe489…, +1188 −3.
    CONFIRMED. `git log -1` on the path gives e1be6d9; numstat.

87. T3:6. "Every line count here is git diff --no-index --numstat's."
    IMPRECISE. "its 13 lines" (T3:44) is an output's length, not a numstat figure.
    Instead: "Every count of lines added and removed here is git diff --no-index --numstat's."

88. T3:6–7. The .gitignore is +3 −0 and is not part of the self-test.
    CONFIRMED.

89. T3:8–12. The package digest, computed by shell over both overlays, and G-TIME-n's in-process check.
    CONFIRMED. T 00:09:32 and 00:47:41 outputs; drv:4690–4693.

90. T3:13–18. The laptop's conditions; two layers in run 1 and three in run 2.
    CONFIRMED. hftiny.py:6 and :56; adapters/base.py imports numpy alone; D1's band is [2, 3] (delta_from_draft1.diff:253–256) and D2's is [2, 3, 4].

91. T3:19–24. The overlays.
    CONFIRMED. A pruned find gives 176 files each and no ckpt or reports folder, with the same names in both. `diff -rq` shows that only scripts/n_sessions.py differs. The two drivers' sha256s equal draft 1's and draft 2's. LOCK-n.md, the close list and the manifest are present. The script is G-VER's with the close-list path added (+10 −8 including comments and usage). Both overlays were built from commit 05ac941232bc….

92. T3:25–29. The command form.
    CONFIRMED. T 00:13:26 and 00:49:38; the N requests' command lines.

93. T3:30–33. The windows, the background tasks and exit notices, the grants' empty TMPDIR and absent output files, and empty stderr and TMPDIR after each run.
    CONFIRMED. Task notifications at 00:13:50 and 00:50:05 precede Code's checks; relays at 00:13:14 and 00:49:31.

94. T3:35–41. Run 1.
    CONFIRMED.

95. T3:43–47. `hashes`.
    CONFIRMED (see O9).

96. T3:49–59. Run 2, all of it except "(15 in all)".
    CONFIRMED.

97. T3:55. "(15 in all)".
    IMPRECISE (as item 82).
    Instead: "and 8 refused options in main()'s loop (15 refused argvs in all)".

98. T3:61. The box has not run this BUILD.
    NOT CHECKABLE.

T4 (D2's G-READ-n texts)

99. The module docstring's gread paragraph and last line (D2:350–406).
    CONFIRMED. The n:159 quote; ans21b §1.5 (ans21b:23); the STOP path; steps 1–7 in code order; the exits; the PIN lines against GR and spec:26–41; the last line against ans4:58.

100. The section comment and the constants' comments (D2:7728–7751).
    CONFIRMED. The close list is committed at 95cd461 with 4,417 lines = 1 + 138 × 32, the report first and each JSON followed by its 31 arrays. The citations LOCK-n.md:322, :823–825, :869 and :964–965 hold. drv:4533–4604 sets no thread variable.

101. The function docstrings and their citations: anl:6477–6483, LOCK-n.md:763–765, probe.py:32–33, LOCK-n.md:1261, PIN-n-25 and anl:6459–6484.
    CONFIRMED. As cited; anl:6460 names PIN-n-25.

102. _gread_prepare's docstring (D2:7943), "Everything before the first fit, in GR8's order".
    IMPRECISE. The function lists and runs the staging folder's checks fourth, before the driver, while GR8 lists the staging folder last (GR:114–117; F11).
    Instead: "Everything before the first fit, in GR8's order but for the staging folder's location, checked fourth (a declared departure, the review's F11); …"

103. _gread_err's docstring (D2:8184–8186), "as the analyzer prints one (``_err_where``, anl:4611-4619)".
    IMPRECISE. For an OSError without a strerror, anl:4618 prints its message (`e.strerror or s`), which can hold a path; D2:8190 prints "no strerror".
    Instead: "A failure's cause without its values or its paths, in the analyzer's form (``_err_where``, anl:4611-4619) but for an OSError with no strerror, printed "no strerror" where the analyzer prints its message; …"

104. The citations in the refusal and print messages (ans21b §1.5; anl:6473-6474; LOCK-n.md:869; L §6; LOCK-n.md:322, :823-825; anl:6459-6484).
    CONFIRMED. L §6 is LOCK-n.md:827–878, the plan's sha256 at :862.

105. _gread_selftest's docstring.
    CONFIRMED. D2:8226–8239 against the code that follows it.

106. The self-test's check names and counts.
    CONFIRMED. Each count or citation in a check's name matches its assertion: 4,417, 139 and 4,278 = 138 × 31; LOCK lines read at indexes 321, 868, 963 and 964; 4 × 24 × 3 + 1 = 289; 6 × 3 = 18; 80 rows of four; the sentinels. The counts are 27 and 33 static calls, 26 and 32 cases, 7 and 15 argvs, giving 58 and 78 run-time checks.

107. main()'s gread messages (D2:8878–8894).
    CONFIRMED.

T5 (S/step4b/gread/build/gitignore_v1)

108. Lines 331–333: n v0.2 §3 G-READ-n (n:121) and §8 step 15 (n:159); scripts/n_sessions.py gread; ledger 27; the .tmp name (D2:7888, :7963) stays ignored under /data/n/gates/*; the admit line; +3 −0 after line 330.
    CONFIRMED.

TOTALS: 108 items. 89 CONFIRMED, 14 IMPRECISE, 1 FAIL, 4 NOT CHECKABLE.

OBSERVATIONS

1. GR13 as sent says the self-test checks "every refusal of GR8 and GR2, one tampered input each" (GR:155). Draft 2 cases only the refusals a tampered input can reach (D2:8235–8238; F7). T1's "Declared" says the unstarred readings stand as sent; a line for this narrowing would close it.

2. GR3's and the block's "values it can recognize in every margin field" (GR:59–60; STOP:96–98) are built as sentinels in the margin, its two log-probability sums and their fresh copies only; the restricted read and the per-token values keep example_record's defaults (F8). T1:64 states the built form but does not declare the narrowing.

3. F3's `data` case tells the two readings apart only because the self-test runs in an overlay, where REPO is the overlay and the working folder lies outside it. Run against the committed driver from the venv's bin folder, which sits inside the repository (no root link, a real .venv folder), both readings give "inside the repository", and the kill is lost. A relative DIR naming the stand-in staging folder from REPO would keep the kill from any working folder.

4. `_gread_err` is stricter than `_err_where` (item 103). T1:56's "in the analyzer's form" is close; T2's "after anl:4611–4619" is exact.

5. gread_binding_problems binds the artifact to the report's cells, where anl binds it to `camp.cells`, and its messages drop anl's example names and merged labels. "Adapted" would be more exact than "copied" (T1:47 and :110).

6. main() checks `--selftest` first (D2:8870–8871). So `gread --staging DIR --selftest` runs the self-test rather than refusing; T1:59's "every other option is refused" holds for every option but that one.

7. The code-read bullet (T1:152–153) names a `sed -n` of the analyzer, but the only one is the review bullet's `_err_where` (00:41:32); the code read used a `grep` of the analyzer (23:53:12). The `grep` of valence_core/adapters/base.py (23:55:42) appears only in the Counts item.

8. T1:131 says span 1's kinds are "as the request's note gives" them. The note says "shasum and wc -l" for its post-note check, but the command used `grep -c`; T1's own words match T.

9. T3:43–44's "the same form" for `hashes`: it ran in the foreground, not as a background task. T3:30's "Each run" correctly refers to runs 1 and 2, but a word on `hashes` would close the gap.

10. T2's "In sum" gives three of the reviewer's departures. RR's third departure has four bullets (also the close-list commands, the HF adapter module's read and `wc -l`); T1 lists them all.

11. T1:113–114: the staging folder's checks also precede the close list, the report and the seeds, not only the driver, the lock and the package.

THE SWEEP

Spans' counts:
- 11 commands, 23:40:28.952–23:44:01.048 (ten to the note's check, one after).
- 8 commands, 23:47:04.444–23:48:02.465.
- 45 commands, 23:49:44.685–00:54:56.023, the sweep included.
- 64 Bash calls in all. To the sweep T also shows Read 34, Edit 46, Write 8, SendMessage 7, Agent 1, ToolSearch 1.

Each of the 64 commands maps to an item in T1's list. Parts outside item 1 that the list does not name:
- 23:40:28: `head -3` on the bracketed grep.
- 23:41:20: `cat` of an earlier known-hashes file in scratch, with `sort -u`, `tr` and a `printf` loop.
- 23:41:53: `tail -n 4` of the gate's dry-run output.
- 23:42:21: `tail -c 2` of the entry's draft into `od -An -c`.
- 23:48:02: `wc -l`, `shasum` and `tail -n 4` of the verify output; `git status --porcelain -- results/raw`, loosely covered by "scoped status".
- 23:50:03 and 23:50:56: `fold -w 200`.
- 23:53:12: `head -8`; `head -n 2` of the committed close list (piped to the refused `cat -A`); `tail -c 1` of the close list into `od -An -c`.
- 23:55:42: `grep` of valence_core/adapters/base.py, with `head`.
- 00:02:30: `head -20`.
- 00:08:42: `grep -n -E` of .gitignore. The whole command is unnamed.
- 00:08:47: `sed -n` of .gitignore and `cmp` of its copy.
- `mkdir -p` in scratch at 23:59:07, 00:08:47, 00:09:01, 00:10:07 (TMPDIR, with its count before window 1), 00:42:31 and 00:51:07.
- 00:41:32: `head -n 1` and `tail -n 1` of the saved report.
- 00:50:10: `head -20`.
- 00:50:34 and 00:53:01: `head -30` and `head -40`.
- File tools: an Edit in N at 23:43:14 and a Read in N at 23:49:47 are unnamed; no Write of a memory file occurred, though T1 names one.

Kinds after the draft's sweep, to this brief's hash, for @REST@ (bracketed argv counts all 0):
- 00:55:18: `grep -F` of the sweep's call list in scratch for six timestamps, through `cut` and `sed -E`.
- 00:55:34: `grep` and `tail -n 1` of the sweep's id list into `jq -r`, and two `grep -c` counts (messages, subagents).
- 00:56:14: `grep -F` and `cut` of the call list; `cd` into scratch; the sources list written there by a `for` loop of `shasum`; `shasum -a 256 -c` into `grep -c`; `grep -c` and `shasum` of the list; `grep -c` line counts of four texts.
- 00:57:08: `diff` of this brief's list-of-record section against the campaign BUILD's values-check brief's (`sed -n` ranges in process substitutions), then `grep -c` and `shasum` of this brief.
- File tools in that interval: two Edits of S/step4b/gread/build/entry_src.md, two Reads of S/step4b/camp/build/vc_brief.md, one Write of S/step4b/gread/build/vc_brief.md. After the hash: this check's Agent call, a Write of S/step4b/gread/gate_new_ids.txt and two Edits of the memory note.

DEPARTURES: none. For the record, none of these is barred:
- two pruned `find`s at the repository root printing counts only: maxdepth 1 with ckpt and reports pruned, and maxdepth 3 with ckpt, reports, data and .git pruned. They established that the venv's bin folder lies inside the repository.
- `diff -rq` of the two overlays, as the brief allows.
- reading Code's command texts and some outputs from T, with paths masked and digit runs masked on ckpt/reports lines.

```
