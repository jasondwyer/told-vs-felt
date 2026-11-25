# n — the N-pod campaign's close entry and n-build's three close lines: the blind values-check, as returned, with every disposition

PI date 2026-11-25. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafted texts, at HEAD `78cd6eb`:
- T1, the close entry, `9ec73231…c1a6` (251 lines), its four placeholders not to be checked;
- T2, n-build's close line on `9792e14`'s entry, `1057229e…3eaa` (5 lines);
- T3, n-build's close line on `e1be6d9`'s entry, `a5a2f33a…7bcf` (5 lines);
- T4, n-build's close line on `fcab1e5`'s entry, `665d0554…9ab8` (6 lines).

**The checker's brief** was a file the checker read itself, as its prompt directed: Code's scratch file
`S/step4b/camp/close/vc_brief.md` (`6f9c5964…0ee2`, 129 lines). It:
- named the texts and the sources. In the repository: the files the texts cite, at `78cd6eb`. In Code's scratch, by
  a sources list at its sha256 (`36c8e419…3b79`, 37 files): the start's nine files copied back and its pod record;
  the seven files of names and its pod record; launch set v1's files; the commit kit's next versions, their fixture
  harness and its output, and the kit before them. The staged report in the staging folder, by `jq`, for the
  figures T1 states, counts and states only. In the sessions' notes folder: `9792e14`'s window request. In this
  session's transcript: the coordinating session's relays, where a text claims what one said;
- asked for each claim against its source: numbers, hashes and their abbreviations, the out raw's line ranges by
  `sed -n` and `cmp`, quotations, citations, the report's figures, what the scripts and records say, T1's checks by
  tool re-run, and T2–T4's claims against the seat's raw and the coordinating session's close lines;
- allowed `shasum`, and `jq` on committed JSON, the staged report and this session's transcript. It barred any
  other interpreter (`awk` among them), any write, any network, any guard marker in an argv (a grep pattern and the
  command's own text included), and globs over the root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file in the repository or
  the staging folder (but the one staged report, as above), anything in Code's scratch or the notes folder but the
  named files, and any look for G-TIME-n's two steered cells or any naming of their holding folder in an argument;
- asked for a sweep of Code's shell commands from `9792e14`'s entry's final sweep (2026-11-24T21:18:51.237Z, T's UTC
  stamp) to the command that hashed the brief, in five spans with T1's counts, and the kinds after it;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq`, the harness's frame and its
two-space indent removed (238 lines, sha256 `f90d43b9d5d87a64b8ba6067d6d86ae5ae3356627da9230ce4cbebad6147a848`). It
names scratch files as S/..., B/..., L/... or K/..., the sessions' notes folder as N and the transcript as T. Its
times are T's UTC stamps.

**Totals:** 84 items: 68 CONFIRMED, 10 IMPRECISE, 3 FAIL, 3 NOT CHECKABLE; and 12 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Each text was edited as a v2 copy of the draft the checker read (S/step4b/camp/close/entry_v2.md and
S/step4b/camp/close/notes/n1_points_v2.md, n2_build_v2.md, n3_eight_v2.md), by the file tools only, and each edit is
replayed by tool in §2.

**The three FAIL items,** each in the entry's departures:
- **Item 67, span 1's `awk`.** Applied in the checker's words: "the sweep's python lines located by `grep -n`, and
  by an `awk` filter of the sweep file by timestamp into `grep -o` and `sed`". `9792e14`'s window request's note left
  it out too (observation 10); the entry now names it.
- **Item 69, the recursive grep's output.** Applied in the checker's words: "its output, 33 lines from 18 memory
  notes, named none that holds a marker". The draft's "some marker-named file names in its output" was wrong.
- **Item 71, span 5.** Applied: its count is 13, the brief's hash included; the `git grep`'s output is "its first 20
  lines (`head -n 20`)"; and the five commands' kinds the draft left out are named in the checker's words. The span's
  "counts and states only" is now "counts, states, ids and digests only" (observation 11).

**The ten IMPRECISE items:**
- **Item 14.** Applied in the checker's words: the steered cells at their pins (L:386).
- **Item 20.** Applied in the checker's words: the report's counters are `exceed_tau` and `exceed_tau4`, and
  `exceeds_tau4` is the records' field.
- **Item 29.** Applied in the checker's words: the arrays stay "beside G-TIME-n's", and G-READ-n's input layout is
  step 15's BUILD question (the seat's §1.5).
- **Item 35.** Applied in the checker's words: torch as the launch's wrapper printed it.
- **Item 42.** Applied in the checker's words: as at G-TIME-n's run; at G-CAL-n's, the stage's stderr held the bar
  alone.
- **Item 53.** Applied in the checker's words: the coordinating session checked the nine against the pod session's
  copy-back report.
- **Item 68.** Applied in the checker's words: span 2's `comm -23`, `cat` and `shasum` into `cut`.
- **Item 70.** Applied in the checker's words, both parts: `wc -c` of one line, `cat -n`, `tail`, and the check and
  sweep folders made by `mkdir -p`; and the G-TIME-n raws' search, four matched, none an out raw.
- **Item 72.** Applied, close to the checker's words: the reads add Code's own drafts in scratch (the entry's and its
  v2 copies, the launch points' values-check brief and replay script); the writes add the launch points commit's
  drafts and message, the close's v2 copies, and the launch points' window request in the sessions' notes folder.
- **Item 78.** Applied in the checker's words, in T2: the close's steps 2 and 3 ran on the box before the window.

**The three NOT CHECKABLE items** (16, 19, 22) are the staged report's sha256 and three of its figures. The checker
could not read the staged report (observation 2). Code had read it at 2026-11-25T08:04Z, its sha256 the close list's
first line, and `camp_place_v1.sh` checks it again in the window: its step 1 by the list's sha256s, its step 2 by
`jq`. The entry says so beside the values-check's raw.

**The observations:**
1. **Gate v18 after the sources list.** The gate gained the checker's agent id after the list was written, as its
   header says. The entry now says the fixture tests passed again after that edit (22 of 22, the harness's third
   run). The window request names the gate at its final sha256.
2. **The staged report.** Met as above; no change to the figures, which the checker found consistent with the out
   raw, the plan, the lock and Code's recorded outputs.
3. **The sweep's totals.** Applied: span 5's count, 13. The total and the last span's count are this entry's final
   sweep's.
4. **Commands the list did not cover.** Applied through items 67, 68, 70 and 71.
5. **The kinds after the brief.** Applied as the entry's last span, with the commands since, to its final sweep.
6. **Q2 in T4.** Applied: "Q2: no look while it ran; the end-wait was on the PID alone."
7. **"one invocation".** Applied: "COMPLETE in its one stage invocation, the start".
8. **The quoted relays' case.** Applied: "LAUNCH CLEARED" and "LAUNCH AS ANNOUNCED", as the record has them.
9. **"each read whole".** Applied: the sentence now says the two records were read whole and the other files as
   §"Code's reading" lists them.
10. **The window note's span 1.** Met by item 67: the entry names the `awk`.
11. **Span 5's "counts and states only".** Applied: "counts, states, ids and digests only".
12. **Four abbreviations held only as the records abbreviate them.** Applied: the entry says the pod session's
    scripts' digests are as its records abbreviate them.

## 2. The edits, replayed

The edits were made to new versioned copies of the four texts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/camp/close/edits_check.sh`. One Edit call whose result was an error (its old text not found; it changed
nothing) is skipped by the script, which names it. The results are byte for byte the revised texts, so nothing else
changed after the check:
- the entry, 40 of 40 edits, one failed call skipped; the three close lines, 2 of 2 (1, 0 and 1).

They are, in order of time: the close lines' two; the entry's wording (items 14, 20, 29, 35, 42 and 53, and
observations 6–9 and 12); its departures (items 67–72 and observations 3–5 and 11); its values-check paragraph and
the checker's departures; and the final sweep's counts. After the edits, the counts of these edits and the
values-check raw's own digest and length were filled by tool in the entry and here.

## 3. The report as returned

```text
BLIND VALUES-CHECK: the N-pod campaign's close entry (T1) and n-build's three close lines (T2–T4)

Setup
- The brief is at its sha256 (6f9c5964…0ee2, 129 lines). The sources list is at 36c8e419…3b79 (37 lines).
- `shasum -a 256 -c` on the sources list gave 36 OK and 1 FAILED: K/kit_gate_v18.sh. See Observation 1.
- HEAD is 78cd6eb. RESULTS.md, LOCK-n.md, CLAUDE.md, the seat's raw, the runner, the schema, the analyzer and .gitignore are each clean at HEAD (rev-parse equals hash-object).
- N/2026-11-24_n-build_launch-points-commit-window.md is at 1686e792…9386 (159 lines).
- The staged report was not read: the permission system refused its `shasum`. See Observation 2.

ITEMS

T1, the head and headline
1. T1:1–2. The run of record is from the BUILD `e1be6d9`: COMPLETE in one invocation, 7680 of 7680 reads, no pause, no STOP. CONFIRMED. B/start/camp_v1_out.txt line 8 (copy HEAD e1be6d9), :7807, :7817, :7821 and :7824. The wording "one invocation" is Observation 7.
2. T1:2–3. The citations n v0.2 §8 step 14, LOCK-n v1.0 §13, and the seat's raw of the third sitting (PI date 2026-11-24, committed at `78cd6eb`, §1.5, CP11). CONFIRMED. Out :104; LOCK-n.md:363–389; `git log` of the raw gives 78cd6eb; the raw's line 3.
3. T1:3–5. The report, 138 cell JSONs and two steered cells committed before the pod stops; 4278 arrays held outside the repository (CP10). CONFIRMED. The close list holds 138 cell .json and 4278 .npy (138 × 31). CP10 is at the spec raw lines 186–193.
4. T1:7. `camp_v1.sh start` (`16485a25…58f5`) ended COMPLETE, exit 0, on `emw1e4embiwe9b`. CONFIRMED. Sources line 22; out :7824 and :112; B/start/camp_v1.exit reads "exit 0".
5. T1:7–9. The launch came on "launch cleared" and "launch as announced" (PI date 2026-11-24). CONFIRMED against B/start/camp_v1_start_box_run.txt lines 4–6. The case of the quoted words is Observation 8.
6. T1:9–12. The last line, verbatim. CONFIRMED. Out :7824; `grep -F` on the unwrapped T1 finds it.
7. T1:13–14. The CP6 line, verbatim. CONFIRMED. Out :7819.
8. T1:14. 1.0518 h of 4 h (26.29%). CONFIRMED by shell arithmetic.
9. T1:14–15. G-TIME-n's projection is 1.0494 h at the medians. CONFIRMED. RESULTS.md:3907–3909 gives "= 1.0494022222222221 h".
10. T1:15–16. The sum of the 7680 reads' `ms` is 3786451. CONFIRMED on re-run: 3786451 over the 7680 lines 127–7806.
11. T1:17–18. The runner's-lines quotation; 22 report checks, each "holds"; G-VER's STOP record absent. CONFIRMED. Out :7816 and :7817. Line :7821 holds 22 " holds" and no other item.
12. T1:19–20. COMPLETE is the one end that need not go to the seat and the PI first (§1.6), so the close followed (§1.5). CONFIRMED. Seat raw lines 33 and 31.
13. T1:21–22. No smoke (Q1, §1.1). Reads 0–159 are the shadows, direction none and dose 0, by ORDER (L:1252). CONFIRMED on re-run:
    - 160 of 160 read "N1-V none 0";
    - the indexes equal 0..159 by `cmp`;
    - LOCK-n.md:1252 holds ORDER.

T1, the outputs of record
14. T1:23–24. "each at the sha256 the box's close list gives". IMPRECISE: the steered cells are not in the close list; their sha256s are pins (L:386; L/camp_place_v1.sh:36–37).
    Wording: "…, each at the sha256 the box's close list gives, G-TIME-n's two steered cells at their pins (L:386):"
15. T1:25. The report's path, `1cabeadf…c4e3`, `n-report-v1`. CONFIRMED. B/names/camp_close_names.txt line 1; schema.py:1129; camp_place_v1.sh:77.
16. T1:25. That the staged report is at that sha256. NOT CHECKABLE: my `shasum` was refused. Code's own recorded check in T (08:04:14Z) printed equality; I tested that as a boolean only.
17. T1:26–27. These figures are CONFIRMED:
    - end_state COMPLETE, no pause and no stop;
    - used_ms 3786451 of hour_cap_ms 14400000, not hit;
    - loads_ms [125924], one load.
    Evidence: out :7819 and :7821 ("cap's hit holds", "one load holds", "no stop holds"), and out :126 (load 125924 ms). Code's recorded `jq` outputs in T match each figure (booleans only).
18. T1:27–28. The binomial's 3637 trials, 0 above TAU and 0 fires. CONFIRMED. The plan has 3637 reads marked R; the out raw has no "> TAU" and no PAUSE line.
19. T1:27. "48 evaluations". NOT CHECKABLE against the report. It is consistent with 7680/160 = 48 tiles (schema.py:1203) and with Code's recorded output.
20. T1:28–29. The values hold:
    - 23 arm|dose rows in the plan;
    - 0 reads above TAU;
    - by re-run, 707 of the 3637 printed `rel` values are above TAU/4 (0.0044708…), with none at the rounding boundary.
    IMPRECISE on the names: the report's counters are `exceed_tau` and `exceed_tau4` (schema.py:1216, :1320); `exceeds_tau4` is the per-record field (schema.py:420; L:885).
    Wording: "the declared counters, `exceed_tau` 0 in each of the 23 rows of arm and dose (3637 trials), `exceed_tau4` (the records' `exceeds_tau4`, rel > TAU/4, L:885) 707 of the 3637 (the analyzer's TAU/4 row reads it),"
21. T1:29. "the analyzer's TAU/4 row reads it". CONFIRMED. scripts/n_analyze.py:3650 and :3669 read the records' `exceeds_tau4`.
22. T1:30–31. Ceiling 0, identity bound 0, non-finite 0, rendering 0, label-mass null. NOT CHECKABLE against the report. Each nonzero would have paused (L:946; schema.py:200–205), and the run had no pause. Code's recorded output holds each value.
23. T1:31–32. Each arm complete, the per-arm counts, 7680 in all. CONFIRMED. The plan by arm; LOCK-n.md:859–861; out :7821 "per arm holds"; Code's recorded per-arm output (booleans).
24. T1:32. 138 cells, 7680 records, 40 to 160 a cell. CONFIRMED. Out :7820; the plan has 120 cells of 40 and 18 of 160.
25. T1:33–34. `read_plan_sha256` is the lock's `7f7d7301…88a6`; `stage_identity_sha256` is `d566764f…7f8a`. CONFIRMED. LOCK-n.md:862; out :113–114 and :7821.
26. T1:35–36. The 138 cell JSONs, at json_sha256, 7680 records; the quotation; check 2. CONFIRMED. Out :7820; camp_place_v1.sh:76–89.
27. T1:37–41. The steered cells' paths and pins, their placement from the holding folder, check 2b, ans21b §1.8 and v1.0 §13. CONFIRMED as to the script and the lock: camp_place_v1.sh:35–37, :91–101 and :116–123; LOCK-n.md:385–388; seat raw line 31; .gitignore:343–344. The placement itself is the window's.
28. T1:42. G-VER's STOP record: none. CONFIRMED. Out :7816; record lines 16–17 and 141.
29. T1:43–46. The arrays. The count, not committed, at the close list's sha256s and ignored (check 4) are confirmed. IMPRECISE: "where G-READ-n reads them" goes beyond the seat's §1.5, which leaves G-READ-n's input layout as "step 15's BUILD question" (seat raw line 31).
    Wording: "They stay in the staging folder outside the repository, `../jspace-lab-box.noindex/n/campaign-v1/`, beside G-TIME-n's (CP10; the seat's §1.5, LQ3, where G-READ-n's input layout is step 15's BUILD question)."

T1, the provenance
30. T1:48–49. The weights, revision, aggregate, 22 files and eight pins (CP7). CONFIRMED. Out :105 and :115–122; LOCK-n.md:1166–1169.
31. T1:50–51. The driver and the lock are "HEAD's committed bytes" at `e1be6d9`. CONFIRMED. Out :8 and :106–107.
32. T1:52–56. The ids, MANIFEST, G-VEC (site 32), G-CAL-n, the dose map, d_eq and d_20, the valence sha16, the sample and N4's schedule. CONFIRMED. Out :108–111; LOCK-n.md:697, :806 and :812.
33. T1:57–59. The identifier (window 4096, L §17), the R6 bridge, the package and its 12-file closure (L §18), and `hashes` equal. CONFIRMED. Out :99, :112 and :126; LOCK-n.md:1157 and :1176.
34. T1:60–62. The identity and the plan. CONFIRMED. Out :113–114.
35. T1:63. The libraries, "from the out raw". IMPRECISE: torch appears in no line of the out raw. Out :112 has python, transformers and tokenizers. torch 2.8.0+cu128 is the wrapper's print (start record line 116). "G-VER v2's" holds (RESULTS.md:2333 and :2396).
    Wording: "python 3.12.3, transformers 5.15.0 and tokenizers 0.22.2, and torch 2.8.0+cu128 as the launch's wrapper printed it (the start's record, §6), G-VER v2's;"
36. T1:64. CUBLAS before the script and as exported; git 2.43.0. CONFIRMED. Out :2 and :7.

T1, Code's reading
37. T1:65–67. These are CONFIRMED:
    - the nine files at the pod session's sha256s;
    - the seven files of names;
    - the records' lengths, 227 and 243 lines.
    The sources list equals the records' digests (start record lines 175–183; names record lines 160–165). T shows both records read whole by the file tool, with no offset or limit. "each read whole" is Observation 9.
38. T1:68–70. CONFIRMED on re-run:
    - the read heads (with R/- marks) equal L/camp_plan_v1.txt by `cmp`;
    - 3637 lines read "fid=… <= TAU" and 4043 read "fid=-", matching the plan's marks;
    - no line has "> TAU".
39. T1:71–74. The seven work files equal out lines 11–76, 78, 80–81, 85–97, 104–7808, 7812–7813 and 7819–7821 by `cmp`. Also: 66 OK; "785/785 …"; hashes.txt equals camp_hashes_v1.txt. CONFIRMED.
40. T1:75–76. The campaign's own G-VER, the tokenizer's load 17120 ms. CONFIRMED. Out :123–125.
41. T1:77–80. These are CONFIRMED:
    - load 125924 ms (out :126);
    - G-TIME-n's 12365 and 12375 ms (RESULTS.md:4011);
    - wall times 8050944 ms (2.2364 h) and 8134187 ms (out :7810 and :7823);
    - the note's planning values (L/camp_launch_note_v1.md:244 and :246).
42. T1:80–82. The stderr files "as at G-CAL-n's and G-TIME-n's runs". IMPRECISE: at G-CAL-n's run the stage's stderr held the bar alone (RESULTS.md:6732–6733). G-TIME-n's matches (RESULTS.md:3981–3983).
    Wording: "…hold transformers' "Loading weights" bar (707 of 707) and its warnings, as at G-TIME-n's run (at G-CAL-n's, the stage's stderr held the bar alone)."

T1, the run, from the records
43. T1:84–88. The launch set's files, sha256s and line counts, the new folder, and the note and place script on the laptop. CONFIRMED. Start record lines 25–41; `wc -l`; camp_v1.sh:57–58.
44. T1:89–93. The box before. CONFIRMED. Record lines 43–59.
45. T1:94–95. /tmp overlay; 151 GiB on /workspace (158938112 KiB = 151.58 GiB). CONFIRMED. Record lines 61–74.
46. T1:96–97. The sync. CONFIRMED. Record lines 76–83.
47. T1:98–102. The fresh copy, its sparse patterns and pins, eighteen tools. CONFIRMED. Record lines 85–101.
48. T1:103–106. The wrapper, the command's sha256, `cmp`, PID 17386, +3 s and +30 min, 180 s, check 46. CONFIRMED. Record lines 103–132.
49. T1:107–110. The end read three ways; to the coordinating session first. CONFIRMED. Record lines 130–148.
50. T1:111–112. After the run. CONFIRMED. Record lines 150–165.
51. T1:113. The departures are in §11. CONFIRMED.

T1, the copy-backs
52. T1:115–118. The start's copy-back. CONFIRMED. Record lines 167–188.
53. T1:118–119. "…as the coordinating session did". IMPRECISE: the coordinating session checked the nine against the pod session's copy-back report (abbreviated digests), before the record existed (relay at 2026-11-25T07:28:11.091Z).
    Wording: "Code checked the nine by name against the record's digests; the coordinating session had checked them against the pod session's copy-back report (first 8 … last 4)."
54. T1:120–124. The names invocation. CONFIRMED. Names record lines 1–15, 44–63 and 81–118.
55. T1:124–128. Names' out raw (16 lines) and its quotations. CONFIRMED. B/names/camp_v1_out.txt lines 1–16.
56. T1:129–133. Into Code's scratch, and Code's checks. CONFIRMED on re-run:
    - 4417 lines in the list;
    - 139 JSON paths, the report first, then 138 cells;
    - 4278 arrays;
    - close_paths.txt equals the list's paths;
    - close_check.txt equals names' out lines 13–15;
    - close.err is empty.
57. T1:134–141. The close's step 3: v2, 30 of 30, 16 of 16, tar 1.35, 4417 of 4417 at both ends, the holding folder untouched. CONFIRMED. Names record lines 180–213; relay at 08:02:54.787Z.
58. T1:142–147. What camp_place_v1.sh checks and places. CONFIRMED as to the script (camp_place_v1.sh:6–26 and :54–135). The run and its done report are the window's and not checkable now.
59. T1:147–149. 141 paths (139 + 2) and eight raws. CONFIRMED by count.

T1, the raws and close lines
60. T1:150–160. The raws' names, sha256s, line counts and "exit 0". CONFIRMED. Sources list lines 5, 6 and 15–17; `wc -l`; the exit files.
61. T1:161–167. The records' sha256s and lengths. The scratch folder's word appears only at start record line 25, and G-TIME-n's holding folder's name only at names record line 194 (bracketed pattern; 0 in the start record). CONFIRMED.
62. T1:170–171. The other work files, close_paths.txt and close.err. CONFIRMED.
63. T1:172–174. The close lines per the seat's head, items 1, 2 and 3. CONFIRMED. Seat raw lines 3 and 80–82. The three entries end with the coordinating session's close lines at RESULTS.md 354, 614 and 867.
64. T1:175–179. Notes carried, (a) and (b), run as granted. CONFIRMED by these sources:
    - the relay at 2026-11-24T21:37:59.022Z, observations 1 and 2;
    - results/raw/2026-11-24_n-campaign-launch-points_code-to-design_STOP.md:190–191;
    - CLAUDE.md:120–121;
    - camp_launch_note_v1.md:203–205;
    - seat raw line 47;
    - the window's six steps, which ran at 21:38:20Z–21:38:43Z with the note's hashes.
65. T1:180–184. The kit. CONFIRMED by these sources:
    - kit_lib_v4.sh:3–8 and :63–93;
    - kit_place_v5.sh:10–12 and :31–38;
    - kit_gate_v18.sh:38–42 and :62–68 (the dry run asserts a placed path absent);
    - kit_verify_v4.sh:10–11;
    - K/test/r2_out.txt, "22 passed, 0 failed";
    - v18's id list has one id more than v17's.
    The gate's hash is Observation 1.

T1, the departures sweep
66. T1:186–188. None of the commands holds a guard marker, the campaign folder's plain name or the holding folder's name. CONFIRMED: [0], [0] and [0] over the 80 commands swept, and over the 3 after the brief's hash.
67. T1:189–195. Span 1. The count, 17, holds. FAIL: the first command (2026-11-24T21:19:03.493Z) ran `awk` over a scratch sweep file. Neither this list nor the window note it points to names it.
    Wording: "the sweep's python lines located by `grep -n`, and by an `awk` filter of the sweep file by timestamp into `grep -o` and `sed`;"
68. T1:196–203. Span 2. The count, 12, holds. IMPRECISE: at 21:24:31.496Z the abbreviation check also ran `comm -23`, with `cat` and `shasum` into `cut`.
    Wording: "the request note's `shasum` and `wc -l`, and its abbreviations by `grep -h -o` into `sed` and `sort -u`, compared by `comm -23` with the known files' digests (`cat`, `shasum` into `cut`);"
69. T1:204–212. Span 3. The count, 7, holds, and so do `git log -3`, the `ls` count (0) and the 14 `touch -c` files. FAIL: the output of the recursive grep (02:37:05.008Z) is 33 lines from 18 memory notes, with no marker in any line [0].
    Wording: "(no glob, so no file name in an argv; its output, 33 lines from 18 memory notes, named none that holds a marker)"
70. T1:213–231. Span 4. The count, 31, holds; the "four patterns, one matching nothing" and "24 … 22 of 22" hold. IMPRECISE:
    - `tail` (07:28:51.326Z) and `wc -c` of one out-raw line (07:29:06.089Z) are not named;
    - `mkdir -p` of the check and sweep folders in scratch, with files written there (07:29:32.732Z and 07:52:00.451Z), is not named;
    - the "no match" is wrong: at 07:30:11.299Z the search printed four G-TIME-n raws' names, and only the out-raw pattern found none.
    Wording, part 1: "… by `shasum`, `wc -l`, `wc -c` (one line's bytes), `cat` and `cat -n`, `head`, `tail`, `sed -n`, `cut`, `cmp`, `grep`, `sort`, `uniq -c`, `paste` and `bc`, and a `while read` with `case` (…), their intermediate files in a check folder made in scratch by `mkdir -p`; `grep -o` of `RESULTS.md`'s lines 3895–4201 for G-TIME-n's raws' names (four matched, none an out raw, so the `wc -l`, `head` and `tail` of a committed raw beside it did not run);"
    Wording, part 2: "`jq` over this session's transcript for this sweep, into a sweep folder made in scratch by `mkdir -p`, its listing …"
71. T1:232–240. Span 5. @NSPAN5@ = 13: from 08:03:37.306Z through the brief's hash at 08:09:03.573Z, that command included. FAIL: the kinds of the last five commands are not named (Observation 4 lists them). The git grep also printed only its first 20 lines (`head -n 20`, exactly 20).
    Wording: replace "which matched LOCK-n.md, … and two raws, their lines printed" with "whose first 20 lines (`head -n 20`) named LOCK-n.md, `RESULTS.md`, a G-ANL-n file under `data/n/gates/` and two raws". Then append to the bullet:
    "; `cp` of the three close lines' drafts to their final names in scratch, a name-only `ls` of their folder, and the drafts' widths and placeholders by `grep -n -E` and `grep -o` into `sort`, `uniq -c` and `tr`; `sed -n` of three of the entry draft's lines; `sed -n` and `cut -f1` of the sweep's listing for nine times; `shasum` and `wc -l` of the entry, the three close lines, the kit's six files and the screen script; the values-check's sources list by `shasum` over 37 scratch files into scratch, after a `cd` into scratch, with its `wc -l`, `shasum` and a bracketed marker count, the window request's note by `shasum` and `wc -l`, and `git rev-parse HEAD`; and the check's brief by `shasum`, `wc -l` and a bracketed marker count."
72. T1:242–245. Reads and writes by the file tools. IMPRECISE. The reads' line ranges check against T's offsets and limits. But the writes leave out the window request's note in the sessions' notes folder (Write at 21:24:14Z, Edit at 21:24:25Z) and the launch points commit's scratch drafts. The reads leave out Code's own scratch drafts (the entry's at 08:06:37–43Z; the launch points' values-check brief at 08:07:14Z).
    Wording: "Reads by the file tools: …; memory notes; and Code's own drafts in scratch (the entry's, and the launch points' values-check brief). Writes by them: in scratch (the launch points commit's drafts and message, the kit's next versions and its tests, the close's drafts, facts and checks), in the sessions' notes folder (the window request's note), and in memory notes; none in the repository."
73. T1:246. The pod session's declarations, start §11 and names §12. CONFIRMED.
74. T1:248–250. What follows. CONFIRMED as citations: §1.5 (5), §1.8, seat §3 for CP18, and seat §5. The events are not checkable.

T2, n-build's close line on 9792e14
75. T2:1. The header (third sitting, n-build's, item 2). CONFIRMED. Seat routing item 2 (line 81); the close line's header (RESULTS.md:343).
76. T2:1–2. The ruling is the close line above (the raw at 78cd6eb, §2 and §1.6). CONFIRMED. RESULTS.md:343–354.
77. T2:3–4. No v2 and no file changed; COMPLETE, exit 0; no pause, STOP, resume or PI stop; the LQ1 and LQ4 routes not taken. CONFIRMED. The six set files are at their sha256s; the out raws; both records.
78. T2:4–5. "The close followed in the close's commit window, by `camp_place_v1.sh`". IMPRECISE: the close's steps 2–3 (names and the copy-back) ran on the box before the window.
    Wording: "The close followed: `camp_v1.sh names` and the copy-back by its list, then `camp_place_v1.sh` in the close's commit window (the N-pod campaign's close entry, PI date 2026-11-25)."

T3, n-build's close line on e1be6d9
79. T3:1. The header, item 3. CONFIRMED. Routing line 82.
80. T3:2–3. CP4: the driver `47abe489…c21a` on the DRIVER line, unchanged. CONFIRMED. RESULTS.md:607–608; out :106; seat §3.
81. T3:3–5. CP15, CP17 ("N-pod campaign (n)") and CP18 (nothing removed). CONFIRMED. Seat raw lines 55–56; spec CP17; the records' "LEFT ON THE BOX, nothing removed".

T4, n-build's close line on fcab1e5
82. T4:1–2. The header, item 1; the raw at 78cd6eb, §1. CONFIRMED. Routing line 80; RESULTS.md:856–867.
83. T4:2–4. The driver unchanged; Q1, Q3, Q4, Q6 and Q7 as stated. CONFIRMED. Out raw lines 8, 106, 123–125, 127–286 and 7817; both records.
84. T4:4–6. Q5 and Q8: the close as §1.5, the push on the PI's word. CONFIRMED. Seat §1.5 and §1.8.

TOTALS
- 84 items.
- 68 CONFIRMED.
- 10 IMPRECISE: 14, 20, 29, 35, 42, 53, 68, 70, 72, 78.
- 3 FAIL: 67, 69, 71.
- 3 NOT CHECKABLE: 16, 19, 22.

OBSERVATIONS
1. K/kit_gate_v18.sh is not at the sources list's sha256.
   - It is now 5710c47e…44ae (171 lines); the list has 83ecdb74…bb8c.
   - T shows two file-tool Edits of it, at 2026-11-25T08:09:34Z and 08:09:37Z. Both came after the list was written (08:08:16Z) and after this check started.
   - The version I read differs from v17 by one added id in its scanned list. Its header names the close values-checker's id.
   - T1's "22 of 22" (K/test/r2_out.txt) ran before that edit. Code's third run (08:09:42Z) came after it.
   - Re-freeze the list, or cite the run that matches the committed gate.
2. The staged report was not read.
   - The permission system refused my `shasum` of it: it is outside this session's folders. I attempted nothing further on it.
   - Its figures were checked against B/start/camp_v1_out.txt (the script reads the report for the CP6 line and the checks), the plan, LOCK-n.md, schema.py and the per-read `rel` values.
   - They were also checked against Code's own recorded `jq` outputs in T (08:04:14Z, 08:04:21Z and 08:04:48Z). I tested those as booleans only and printed nothing of them. They hold every figure T1 states, and Code's "the staged report is at the list's sha256".
   - A direct re-hash and read is still owed.
3. Sweep totals.
   - The span counts 17, 12, 7 and 31 hold.
   - @NSPAN5@ = 13, with the brief's hash command included (12 without it).
   - 80 commands up to the brief's hash, plus 3 after it at this check, so @NCMD@ = 83 now. It grows with Code's later commands.
   - Guard markers [0]; the campaign folder's plain name [0]; G-TIME-n's holding folder's name [0].
   - `awk` [1]. "python" appears plainly only in the printed label at 21:23:24.079Z.
4. Commands outside item 1's forms that T1's list does not cover, by time and kind:
   - 2026-11-24T21:19:03.493Z: `awk` (a timestamp filter), into `grep -o` and `sed`.
   - 2026-11-24T21:24:31.496Z: `comm -23`, with `cat` and `shasum` into `cut`.
   - 2026-11-25T07:28:51.326Z: `tail -n 3` of the out raw's numbered read lines.
   - 2026-11-25T07:29:06.089Z: `wc -c` of one out-raw line, with `cut` and `tr`.
   - 07:29:32.732Z and 07:52:00.451Z: `mkdir -p` of scratch folders, with redirected writes into them.
   - 08:06:57.957Z: `cp` of three scratch drafts to their final names; a name-only `ls`; `grep -n -E` with `cut` and `tr`; `grep -o` into `sort`, `uniq -c` and `tr`.
   - 08:07:02.303Z: `sed -n` of three entry-draft lines.
   - 08:07:36.006Z: `sed -n` and `cut -f1` of the sweep listing; `shasum` and `wc -l` of eleven scratch files.
   - 08:08:16.692Z: `shasum` over 37 scratch files into a new scratch file after a `cd` into scratch; its `wc -l` and `shasum`; a bracketed marker count; the note's `shasum` and `wc -l`; `git rev-parse HEAD`.
   - 08:09:03.573Z: the brief's `shasum`, `wc -l` and a bracketed marker count.
   - Span 1's `bash -n`, `tee`, `mkdir`, `printf` into scratch and `git rev-parse HEAD` are covered only through the window note T1 points to.
5. @REST@ kinds, for Code. The three shell commands after the brief's hash:
   - 08:09:42.076Z: `bash -n` of the gate v18. The fixture harness's third run by `bash`, into a new scratch folder, its output to a file, with `tail -n 1`. The id count by `sed -n` into `grep -o -E` and `grep -c`. `diff` of the v17 and v18 id lists, counted by `grep -c`. The screen script over the gate, the close list, the start's out raw, both records and names' out raw, filtered by `grep -v`.
   - 08:10:39.320Z: `bash -n` of a new scratch script, the kit maker. Its run with the check's brief and the three close lines into a new scratch folder. `sed -n` of its manifest masked by `sed -E` and `cut`. `cut` of its notes list.
   - 08:10:54.255Z: the maker again, into another scratch folder, output to /dev/null. A shell function. A `cd` into the repository. The gate v18's dry run (DRY=1, with a notes list) over the manifest, the entry draft and the package digest, output into scratch. `sed -E`, `tail` and `cut` of that output. `wc -l` of the dry run's RESULTS.md beside `git show HEAD:RESULTS.md` into `wc -l`. `diff` of the two into `grep -E`.
   - Since then the file tools also ran, for the entry's lines:
     - two Edits of the gate v18;
     - Writes of S/step4b/camp/close/make_kit.sh, …/edits_check.sh and …/msg_src.txt;
     - a Read of S/step4b/camp/points/edits_check.sh;
     - an Edit of a memory note.
6. T4 covers Q1 and Q3–Q8 but not Q2. The start record gives it (line 11 and §6). Suggested addition: "Q2: no look while it ran; the end-wait on the PID alone."
7. T1:1 says "COMPLETE in one invocation", while T1:154 says "each invocation's out file" (start and names). Suggested: "COMPLETE in its one stage invocation, the start".
8. T1:8 quotes "launch cleared" and "launch as announced" in lower case. The record (lines 5–6) has "LAUNCH CLEARED" and "LAUNCH AS ANNOUNCED", and T1:121 uses the upper case.
9. T1:67's "each read whole" is true of the two records. The close list and camp.txt were checked by tool, not read whole.
10. N's "My commands since the entry's sweep" also omits the `awk`. T1's span 1 relies on that note, which the repository does not hold.
11. T1 span 5's "counts and states only": the 08:04:21Z `jq` also printed the stage identity's digests and parameters. These are item 1's ids and digests.
12. Four abbreviations in T1 match only the pod records' own abbreviations: `4c768abd…dcc4`, `605242c2…ad2e`, `98e27969…91c1` and `f1f36bd3…86ae`. No source here holds their full sha256s.

DEPARTURES
- One `shasum` of the staged report, as the brief directs, was refused by the permission system and did not run. Nothing of the staged report was read.
- One command, a zsh word-count expansion over L/camp_plan_v1.txt, was refused by a built-in safety check and did not run.
- `git log -1 --format='%h %ci'` was run without item 3's pathspec.
- Beyond the Bash items and the relays, I read with `jq` the tool_result content of about twenty of Code's commands in T, to check T1's statements about their outputs. I printed counts, booleans, names or masked lines. For the three outputs of the staged report, I printed booleans only.
- From one of those outputs, I printed 18 memory notes' file names where a count would have served.
- I read these as the texts' citations, beyond the brief's named files: 9792e14's raw (by `sed -n` and `grep -n`), the spec raw (CP6–CP18), .gitignore, valence_core/n/runner.py, valence_core/n/schema.py and scripts/n_analyze.py.
- No guard marker, plain campaign-folder name or holding-folder name was in any argv. No other interpreter, no write, no network, no listing in S or N, and nothing read under data/*/ckpt or data/*/reports.
```
