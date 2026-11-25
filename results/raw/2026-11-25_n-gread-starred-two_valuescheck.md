# n — G-READ-n's seat block (the block on GR3 and GR5, the spec raw, the entry and n-build's close line): the blind values-check, as returned, with every disposition

PI date 2026-11-25. Code (the n-build session).

**What was checked.** One blind pass by a subagent over the drafted texts, at HEAD `0081351`:
- T1, the block on GR3 and GR5, `0803c5cf…5167` (163 lines);
- T2, the spec raw's head, `4ab1b70b…97cd` (39 lines), and T2b, the spec raw as assembled from it and its four
  sources, `c5089010…449f` (773 lines);
- T3, the entry, `8e3dbb40…bd13` (171 lines), its three placeholders not to be checked;
- T4, n-build's close line on `95cd461`'s entry, `2d3aa48a…3961` (10 lines).

**The checker's brief** was a file the checker read itself, as its prompt directed: Code's scratch file
`S/step4b/gread/seat/vc_brief.md` (`c496ab22…89f3`, 134 lines). It:
- named the texts and the sources. In the repository: the files the texts cite, at `0081351` (and `RESULTS.md` at
  `95cd461` for R: lines). In Code's scratch, by a sources list at its sha256 (`9489239d…5faf`, 11 files): the four
  texts, the assembled spec raw, its four sources and its build script. In the sessions' notes folder: the readings
  as sent and the close's window request. In this session's transcript: the coordinating session's relays, where a
  text claims what one said (the spec raw's §2 among them);
- asked for each claim against its source: numbers, hashes and their abbreviations, citations, quotations, and what
  the texts and the code say; T1's readings against the readings as sent; each section of T2b against its source
  byte for byte; T2b's imprecise points, and any other the head does not name;
- allowed `shasum`, and `jq` on committed JSON and this session's transcript. It barred any other interpreter (`awk`
  among them), any write, any network, any guard marker in an argv (a grep pattern and the command's own text
  included), and globs over the root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file, anything outside the
  repository but the named files (the staging folder above all), and any naming of G-TIME-n's holding folder in an
  argument;
- asked for a sweep of Code's shell commands from the campaign close entry's final sweep (2026-11-25T08:47:11.192Z,
  T's UTC stamp) to the command that hashed the brief, in six spans with T3's counts, the kinds after the draft's
  sweep, and T3's counts of markers and folder names in commands and outputs;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (147 lines, sha256
`73a0aea1ec32809f6dba4e797dfe5a2635a20a4c872758e134bed269142392e3`). It names scratch files as S/..., the sessions'
notes folder as N and the transcript as T. Its times are T's UTC stamps.

**Totals:** 81 items: 73 CONFIRMED, 5 IMPRECISE, 1 FAIL, 2 NOT CHECKABLE (its TOTALS line corrects itself to these);
and 11 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Each text was edited as a v2 copy of the draft the checker read (S/step4b/gread/seat/block_v2.md, spec_head_v2.md,
entry_v2.md and notes/n4_close_v2.md), by the file tools only, and each edit is replayed by tool in §2.

**The FAIL item:**
- **Item 69, the departures' item on the file tools.** Applied in the checker's words: the Reads of memory notes
  and the memory index are named, and the sessions' notes folder's calls are a Read of `9792e14`'s window note and
  a Write and an Edit of the close's window note.

**The five IMPRECISE items:**
- **Item 31.** Applied in the checker's words: LOCK:965–966.
- **Item 39.** Applied in the checker's words: "§1's section "Notes for the seat" holds four citations and no
  question, beside the survey's departures". The block now also says which imprecise points of the readings the
  spec raw's head names (observation 7).
- **Item 52.** Applied: the head's heading is "Points in §1 and §4, as sent, that are imprecise or since
  superseded", and §4's 1.5 is listed as true at `95cd461` and superseded since.
- **Item 60.** Applied, with observations 7 and 8: the entry says the head notes four imprecise points in §1 and one
  in §4, and three superseded since, and that the block carries GR3's and GR5's.
- **Item 65.** Applied in the checker's words: 14 Edits shortening lines, one line folded into another, after one
  that added to a line.

**The observations:**
- **1.** Met: the four commands and the file tools before the brief's hash are in the entry's departures, after the
  draft's sweep. The Read of the close's values-check brief, whose output holds the five marker words, is counted
  among the reads with marker words.
- **2.** Met: the five commands after the brief's hash are in the entry's departures, with the rest after this
  check.
- **3.** Applied: the Counts item names Q-F3's folder's name in its `data/` form, and its bare short name in one more
  output, a comment in the commit gate's head.
- **4.** Applied: the Counts item names G-TIME-n's holding folder in its `noindex/n/` form, and its bare name in one
  command output, the close's window note's point 2, which quotes the names record.
- **5.** Applied: the file tools' item names the three messages to the coordinating session and the two subagents,
  and the strings the texts written or sent hold.
- **6.** Applied: a new departures item names the small parts of commands that the spans do not.
- **7.** Applied: the spec raw's head names GR5's, GR7's and GR8's points as imprecise in §1, each checked by Code at
  the lines the checker gives (`valence_core/n/guard.py`:74–81; `valence_core/echo/probe.py`:78–92 and :97).
- **8.** Applied: the head names (a) as imprecise in §4, its four lines found by `git grep` with item 3's pathspec,
  and (b) as true at `95cd461` and superseded since.
- **9.** Applied: the head says ans4 was untracked at `95cd461` and is committed unchanged at `13ca2fe`.
- **10.** Applied in the checker's words.
- **11.** Applied: `load_cell(staging, arm, direction_id, dose_label, …)`, cells:135's names.

**The two NOT CHECKABLE items** (76 and 77, the gate's next version and the commit itself): met at the commit. The
gate is v19, its id list holding the survey's and this checker's agent ids, and the commit's verify checks the rest.

## 2. The edits, replayed

Every edit after the check was made in a v2 copy by the Edit tool alone. A script (S/step4b/gread/seat/edits_check.sh)
recovers those Edit calls from this session's transcript by `jq`, applies them in order to the drafts the checker
read (each at its sha256 in the checker's sources list), each old text found exactly once, and compares the result
with the v2 copy byte for byte:
- the block, 3 of 3 edits; the spec raw's head, 1 of 1; the entry, 7 of 7; the close line, 1 of 1.

They are, in order of time: the block's (items 31 and 39, observation 11); the spec raw's head's (item 52,
observations 7–9); the close line's (observation 10); the entry's (items 60, 65 and 69, observations 5 and 6, the
values-check's summary and the checker's departures), then its departures after the draft's sweep and the final
counts (observations 1–4).

## 3. The report as returned

```text
VALUES-CHECK REPORT: G-READ-n's seat block (T1), spec raw head (T2), assembled raw (T2b), entry (T3), close line (T4)

Preliminaries: the brief hashed to c496ab22…89f3 (134 lines). S/step4b/gread/seat/vc_sources.txt hashed to 9489239d…5faf (11 lines), and all 11 files it names were OK under `shasum -c`. N/2026-11-25_n-build_gread-pins.md is 17d66da9…9b43 (195 lines) and N/2026-11-25_n-build_campaign-close-commit-window.md is 48b438eb…2b4f (132 lines). HEAD = origin/main = 0081351. Every repository source I read was clean, checked by `git rev-parse HEAD:<path>` against `git hash-object`.

ITEMS

T1 (S/step4b/gread/seat/block_src.md)
1. T1:3–5. Claim: the block is for the seat's next sitting, before the run (rt4 item 2), and rtp item 4 says "G-READ-n's spec raw and starred block take precedence when they land". CONFIRMED: rt4:29; rtp:22 word for word.
2. T1:8. Claim: `95cd461` is committed and on origin. CONFIRMED: `git log 95cd461..0081351` lists 13ca2fe, 5ceb8dd and 0081351, and origin/main is 0081351.
3. T1:8–10. Claim: the seat accepted the run and close as committed (ans4 §1; rt4 item 1) and named six points (ans4 §3). CONFIRMED: ans4:12–18, :27–34 and :54; rt4:19–23.
4. T1:11–13. Claim: the drv:351 quote; gread-bench at drv:235–237 and :4533–4604; the campaign start's refusals and pins. CONFIRMED: drv:351 is word for word; drv:235–237 is the docstring, and :4533 (`gread_counts`) to :4604 (`return 0`) holds the bench; `_camp_prepare` is at drv:6554–6669.
5. T1:14–15. Claim: the survey ran at 95cd461 and left 15 open questions; GR1–GR14 answer them and carry the six points. CONFIRMED: report:3 and :359–375; readings:5–7.
6. T1:16–20. Claim: the readings went to the PI first, as the campaign's did; the PI's answer, "push both and build on the pins", was relayed verbatim; "push both" was push #27 of 5ceb8dd and 0081351. CONFIRMED: the T relay at 2026-11-25T18:10:07.057Z says "The readings go to the PI first, as the campaign's did"; routing:1, :3, :8 and :12; the campaign block at results/raw/2026-11-23_n-campaign-starred-eight_code-to-design_STOP.md:18.
7. T1:21–23. Claim: rt4's bracket "[go, on the seat's ruling before the run]" (rt4:24–29); fcab1e5 came before e1be6d9. CONFIRMED: the bracket is at rt4:29, and e1be6d9's parent is fcab1e5.
8. T1:26–30. Claim: the sources' digests, line counts and compiling HEAD. CONFIRMED: `shasum` and `wc` of the three S files; report:3.
9. T1:31–33. Claim: the file names; LOCK:line means the file's line, which ans4 writes L:line; v0.1's L:k is LOCK:395+k. CONFIRMED: ans4:3 defines L:N as LOCK-n.md's line N at 098218c; v0.1's heading is LOCK:396; LOCK:57; the LOCK-n.md blob is the same at 098218c, 95cd461 and HEAD.
10. T1:36–44. Claim: the commits that hold ans4, rt4 (13ca2fe) and rtp (5ceb8dd); the ans21b and ans18c paths; R: anchors at 95cd461; the parent is 0081351. CONFIRMED: `git log --diff-filter=A` for each raw.
11. T1:45–47. Claim: the drv, anl (v7) and package digests, and no code file changed between 95cd461 and 0081351. CONFIRMED: `shasum`; LOCK:212–215 and :1176; drv:3903. `git diff --name-only 95cd461 0081351` with item 3's pathspec lists only RESULTS.md and 7 raws.
12. T1:54. Claim: the two are ruled before the run, not before the build. CONFIRMED: rt4:29.
13. T1:59–63. Claim: `check_cell` holds `margin` to `logprob_S − logprob_U` and the fidelity numbers to their formula, in memory, and prints only a field path on a refusal. CONFIRMED: schema:1017–1018 and :1063–1067 sit in `check_record`, which `check_cell` calls at :1115. Refusals are formatted "path: message" (schema:608–609), and cells:72–75 keeps only the part before ": ". readings:55 and :58 hold the two quotes.
14. T1:64–67. Claim: the run waits for the seat's answers, the PI's routing, the BUILD's commit and a battery window beside Q-F3. CONFIRMED: routing:15–16; ans4:32.
15. T1:72. Claim: GR3 is the survey's open question 6. CONFIRMED: report:366.
16. T1:73–74. Claim: `load_cell(…, identity=None, keep_arrays=…)` at cells:135–174, as the PIN of record has it. CONFIRMED: cells:135–174; R:11583.
17. T1:75–77. Claim: the cell's JSON is parsed whole (cells:146) and checked by `check_cell` (cells:148), field by field (schema:893, :1092–1124). CONFIRMED: schema:893 is `check_record` ("Every field and every local invariant of one read record"); `check_cell` runs from :1092 to :1125.
18. T1:77–79. Claim: the command keeps each record's session_id and row; the cells are the labels and the session ids the groups. CONFIRMED: agrees with readings:56–59.
19. T1:81–82. Claim: the ans4:32 quote. CONFIRMED: word for word.
20. T1:83–84. Claim: the two n:130 quotes. CONFIRMED: word for word.
21. T1:85–87. Claim: the PIN declared to n-analyzer at R:11583–11585. CONFIRMED: R:11582–11585 at 95cd461, word for word.
22. T1:88–89. Claim: the cells:139–140 docstring quote. CONFIRMED: word for word.
23. T1:90–94. Claim: the list of `check_cell`'s numeric checks, and refusals redacted to the field path (cells:72–75, :150). CONFIRMED: schema:1013–1031 (non-positive log-probabilities, fsum, margin, the restricted probabilities, their sum to 1, the pick) and :1056–1067 (the fresh margin; `fidelity_numbers`).
24. T1:95–98. Claim: as Code will build GR3: identity=None on all 138 cells, arrays kept only for probed cells, two cells open at a time, planted values consistent with `check_cell`. CONFIRMED: readings:43, :46–47, :59–60, :124–125 and :157. The consistency requirement holds because `load_cell` refuses any cell that `check_cell` rejects (cells:147–150).
25. T1:99–103. Claim: GR3's other answer is the driver's own parse (the package cannot change), superseding the PIN for G-READ-n. CONFIRMED: agrees with readings:61–63, narrowing "skips the margins" to "never checks"; ans4:30; R:11583.
26. T1:105. Claim: GR5 is the survey's open question 5. CONFIRMED: report:365.
27. T1:106–110. Claim: Code's GR5 reading: at +1, +1 against its own −1 on the 40 floor sessions; span_reward takes +d_eq's and +d_20's comparators. CONFIRMED: LOCK:834; LOCK:964–965; drv:4536–4538; readings:85–88 and :98–99.
28. T1:112–114. Claim: the probe:32–33 quote, which LOCK:1261 pins. CONFIRMED: probe:29 and :32–33 are word for word; LOCK:1261 sits under §21, "Code's PINs that the package gives the lock to pin" (LOCK:1249).
29. T1:115–116. Claim: the A-n1:56 and LOCK:962–964 quotes. CONFIRMED: both phrases appear in A-n1:56 and in LOCK:963–964.
30. T1:117–118. Claim: the ans21b:23 quote (Q5, "Stands as built"). CONFIRMED: word for word.
31. T1:119–120. Claim: "LOCK:966–967: "The comparator's band medians are over each random direction's 40 floor sessions against the axis's 160"". IMPRECISE: the sentence spans LOCK:965–966, not 966–967. Write instead: "LOCK:965–966: "The comparator's band medians are over each random direction's 40 floor sessions against the axis's 160";".
32. T1:121–122. Claim: 4 × 24 × 31 = 2,976 calls on 80 rows (ans21b:23; drv:4533–4547). CONFIRMED: ans21b:23; drv:4542–4547.
33. T1:123–125. Claim: as Code will build GR5: N1-R's +1 and −1 cells at +1; N1-V's shadow rows for the 40 floor sessions by session id; each point's medians computed once. CONFIRMED: readings:94–97; schema:278–279 and :594; ans4:15; ans21b:23.
34. T1:126–128. Claim: GR5's other answer: N1-R's −1 cells are checked but never probed; the count is unchanged. CONFIRMED: agrees with readings:89–91 and corrects their "never reads" by GR2 (readings:46). The count is drv:4544.
35. T1:132–138. Claim: the build runs on GR1–GR14 as PINs, in the driver alone; the package and anl stay unchanged; the new pins and self-tests; battery windows only, no Python outside one while Q-F3 runs; one review, one values-check, the BUILD's window. CONFIRMED: routing:12 and :15; ans4:29–30; readings:34, :103–104, :149–160 and :191–193.
36. T1:139–142. Claim: the run comes only after the seat's answers, the PI's routing, the BUILD's commit and a battery window. CONFIRMED: routing:16; readings:163–164.
37. T1:143–145. Claim: the pre-declared ends: exit 0 whatever the six statuses; 1 with no artifact; a crash or stop means a whole repeat. CONFIRMED: readings:117–118, :123–124 and :134.
38. T1:146–147. Claim: twelve unstarred readings, which are Code's, as the campaign's were. CONFIRMED: the count is twelve; campaign block:306–307.
39. T1:147–148. Claim: "§1's last section, "Notes for the seat", holds four citations and no question". IMPRECISE: "Notes for the seat" (readings:171) is the next-to-last section; the last is "The route from here" (readings:189). It also holds a fifth bullet, the survey's departures (readings:183–187). Write instead: "§1's section "Notes for the seat" holds four citations and no question, beside the survey's departures:".
40. T1:148–150. Claim: ans18c:40 is Q-F3's git exclusion; the window's texts are ans21b:23 and :80; and R:12996. CONFIRMED: ans18c:40 (§5.3); ans21b:23 and :80; readings:173–182; R:12996 at 95cd461.
41. T1:151–153. Claim: the survey's departures are in §4's last section. CONFIRMED: report:377–394.
42. T1:156–163. Claim: Q1's and Q2's citations. CONFIRMED: see items 21, 28 and 30.

T2 (S/step4b/gread/seat/spec_head_src.md) and T2b (S/step4b/gread/seat/spec_v1.md)
43. T2:3–6. Claim: the PI date and what the raw serves. CONFIRMED.
44. T2:7. Claim: §1 is the readings verbatim, 17d66da9…9b43, 195 lines. CONFIRMED: T2b:44–238 is equal by `cmp`.
45. T2:7–11. Claim: the note in the notes folder is a byte copy; Code's message named its path, sha256 and line count; the coordinating session checked and read it whole before going to the PI. CONFIRMED: the N file is equal by `cmp`. T's SendMessage at 18:08:30.065Z gives the path, sha256 and 195 lines on its lines 4–5. The relay at 18:10:07.057Z says "the PINs 17d66da9…9b43 (195 lines, read whole)", then "What I'm asking the PI".
46. T2:10–11 and :13. Claim: §1 and §2 are in no other repository file. CONFIRMED: `git grep -l -F` of their opening lines (item 3's pathspec plus Q-F3's exclusion) finds 0 files.
47. T2:12–13. Claim: §2 is the relay verbatim, 4e686ed0…1dd0, 18 lines. CONFIRMED: T2b:244–261 equals the source by `cmp`, and the source equals lines 3–20 of T's relay record at 22:44:22.329Z, also by `cmp`.
48. T2:14–15. Claim: §3, d1fa766e…13fb, 107 lines, with line 2's path written <repo>, 43eca2d5…72ce. CONFIRMED: `diff` shows only "2c2"; T2b:267–373 is equal by `cmp`.
49. T2:16–19. Claim: §4 verbatim; HEAD 95cd461 at start and end; taken out with `jq` on 2026-11-25. CONFIRMED: T2b:379–772 is equal by `cmp`; report:3; T command at 17:58:22.104Z.
50. T2:21–23. Claim: every file:line is the repository's at 95cd461, and only RESULTS.md and raws changed since. CONFIRMED: the diff name list; every cited code and text file has the same blob at 95cd461 and HEAD. See observation 9.
51. T2:25–30. Claim: GR3's "No margin … is computed on" sentence is imprecise as stated. CONFIRMED: schema:1013–1018, :1026–1029 and :1063–1067 compute on the log-probabilities, the margin, the pick and the fidelity numbers inside `check_record`, which `check_cell` runs.
52. T2:25 and :31–32. Claim: §4's 1.5 is "imprecise". IMPRECISE: its facts hold (rt4:24–29 at 13ca2fe matches the brief's quotation word for word), but the survey's sentence was true at its HEAD, as the head itself says. It is superseded, not imprecise. Write the heading as "**Points in §1 and §4, as sent, that are imprecise or since superseded.**" and the bullet as "§4's 1.5, "The PI's routing item 2, as the brief quotes it, is not committed at HEAD": true at `95cd461`, superseded since. It is committed at `13ca2fe`, in `results/raw/2026-11-25_fourth-sitting_pi-routing.md`:24–29, in the brief's words."
53. T2:34–36. Claim: how §2 was taken out of T. CONFIRMED: T command at 22:48:17.160Z. The record's wrapper (its lines 1–2 and 21 onward) names a session by its id.
54. T2:38–39. Claim: no home-folder path or full scratch path appears. CONFIRMED: a `grep -c` for local roots and ids over T2b gives 0. The two 40-character hex runs (T2b:246 and :381) are commit ids.
55. T2b. Claim: the head equals T2 and each section equals its source byte for byte. CONFIRMED: `sed -n` into `cmp` for 1–39, 44–238, 244–261, 267–373 and 379–772; 8 fence lines; 773 lines.

T3 (S/step4b/gread/seat/entry_src.md)
56. T3:1–4. Claim: the heading and the block's link follow fcab1e5's form. CONFIRMED: RESULTS.md:1595.
57. T3:6–15. Claim: where things stand (95cd461 on origin, ans4 §1 and §3, the readings to the PI first, the relayed answer, push #27). CONFIRMED: see items 2, 3, 6 and 10.
58. T3:16–22. Claim: why now (rt4 item 2's bracket; fcab1e5 before e1be6d9; rtp item 4's quote). CONFIRMED: see items 1 and 7.
59. T3:23–39. Claim: the block's sections, "the readings' four citation notes", and the spec raw's sections and digests. CONFIRMED: see items 39 and 44–49.
60. T3:41. Claim: "two imprecise points as sent, one in §1 and one in §4". IMPRECISE, as item 52. Write instead: "Its head notes one imprecise point in §1 and one point in §4 true at `95cd461` and superseded since, which the block carries correctly."
61. T3:42. Claim: nothing ran on a model, and no Python ran. CONFIRMED: none of the 97 Bash calls in the sweep names an interpreter (bracketed `jq` test). The bodies of the scripts those calls ran are outside the sources.
62. T3:43–45. Claim: the values-check brief quoted items 1–5 and allowed `shasum`, plus `jq` for the sweep. CONFIRMED: brief:3–6 and :129–134.
63. T3:52–70. Claim: span 1 is 17 commands of the kinds the note gives, plus one after the note; the six build runs as described (the first stopped at the replay's counts, BSD sed's ERE having no backreference); the 18 files; the bracketed counts "0 and 0". CONFIRMED: 08:47:28.738Z to 08:54:49.667Z holds 18 Bash calls; the note's lines 112–129 give the kinds. The build outputs were "FAIL: the replay's counts", "no commit folder yet", four width FAILs, then "build exit 0". The Edit at 08:48:44Z removed an ERE `\1`.
64. T3:71–80. Claim: span 2, 10 commands, with step 2's echo in double quotes as the coordinating session corrected it at the grant. CONFIRMED: 09:04:24.595Z to 09:06:11.110Z. The grant relay at 09:04:06.570Z (its lines 3, 13 and 15–16) has the correction.
65. T3:81–84. Claim: span 3 runs "while Code shortened its own lines in the index (15 Edits, one line folded into another)". IMPRECISE: the six commands and the two relays (09:10:56.839Z VERIFY PASS; 14:26:56.645Z push #25) hold. But of the 15 index Edits between 09:06:46Z and 09:08:16Z, the first (09:06:46.196Z) lengthened a line by 285 characters. Only 14 shortened lines or folded one line into another. Write instead: "(14 Edits, one line folded into another, after one that added to a line)".
66. T3:85–102. Claim: span 4, 18 commands and one read-only subagent, with the kinds listed (9, 12 and 10 named files). CONFIRMED: 17:29:56.864Z to 18:08:40.442Z; the Agent call at 17:32:58Z.
67. T3:103. Claim: span 5, one command. CONFIRMED: 21:07:14.641Z, after the push #26 relay at 21:06:28.848Z.
68. T3:104–138. Claim: span 6 is 40 commands, the draft's sweep included, of the kinds listed. CONFIRMED: 22:45:00.769Z to 22:58:30.232Z. Each call matches a listed kind ("== not found"; nothing staged; ADDENDUM-n1.md, then three names from `git ls-files`; `grep -P` refused). No command in any span falls outside T3's kinds; small parts it does not name are in observation 6.
69. T3:140–142. Claim: "In every span, the file tools: Edits and Writes of memory notes and the memory index (outside scratch); Reads and Writes in the sessions' notes folder (the close's window note); …". FAIL: the item misses the Reads of memory notes and the memory index (MEMORY.md at 09:06:40Z, 09:07:26Z, 09:11:08Z and 14:27:46Z; memory notes at 14:27:45Z, 22:45:01Z and 22:45:24Z). It also misnames the notes-folder calls. Those were a Read of 9792e14's window note (N/2026-11-24_n-build_launch-points-commit-window.md, 08:52:27Z), and a Write (08:54:37Z) and an Edit (08:54:47Z) of the close's note. Write instead: "**In every span, the file tools:** Reads, Edits and Writes of memory notes and the memory index (outside scratch); in the sessions' notes folder, a Read of `9792e14`'s window note and a Write and an Edit of the close's window note; Reads of repository files and of scratch files; Writes and Edits in scratch."
70. T3:143–145. Claim: no marker and no plain Q-F3 folder name in any argv; the holding folder's name in one argv, step 1. CONFIRMED: bracketed `jq` tests over the 97 commands and every file-tool path give markers 0, `data/m[f]3` 0, and the holding folder once (09:04:29.574Z).
71. T3:145–148. Claim: marker words in five file-tool reads and six command outputs. CONFIRMED (through the draft's sweep). The reads are at 14:27:46Z, 17:30:18Z, 17:31:08Z, 22:45:41Z (RESULTS.md, offset 20) and 22:46:37Z. The outputs are at 17:30:58Z, 18:01:52Z, 22:52:39Z, 22:53:31Z, 22:56:00Z and 22:57:56Z.
72. T3:149–151. Claim: Q-F3's folder's name in three reads and four command outputs. CONFIRMED with Code's pattern, `data/m[f]3`. The reads are at 17:29:57Z, 22:46:25Z and 22:46:37Z; the outputs at 18:01:52Z, 18:02:10Z, 22:48:51Z and 22:52:39Z. See observation 3.
73. T3:151–152. Claim: the holding folder's name in three reads. CONFIRMED in its `noindex/n/` form: 14:27:46Z, 22:47:39Z (S/step4b/camp/close/TODO.md) and 22:54:07Z. It is in no command output; see observation 4.
74. T3:153–159. Claim: the survey's departures (four numbered items) and those declared beside them. CONFIRMED: report:377–394.
75. T3:161. Claim: n-build's close line, which the seat's raw asks of each session, covers items 1–2. CONFIRMED: ans4:3; rt4:18–29.
76. T3:162–163. Claim: the commit gate's id list carries both agent ids. NOT CHECKABLE: the gate's next version is outside the sources.
77. T3:164–170. Claim: committed by path, home-folder count 0, not pushed. NOT CHECKABLE: these are future.

T4 (S/step4b/gread/seat/notes/n4_close.md)
78. T4:1–2. Claim: PI date 2026-11-25, the fourth sitting, items 1–2; the coordinating session's close line above (`13ca2fe`, its §1 and §3). CONFIRMED: RESULTS.md:977–990 was added at 13ca2fe (absent at 95cd461) and cites the raw with its §1 and §3. See observation 10 on wording.
79. T4:3–5. Claim: item 1's figures and acceptance; nothing in the driver changed. CONFIRMED: rt4:19–23; the driver last changed at e1be6d9.
80. T4:6–10. Claim: item 2: the build on GR1–GR14 under "build on the pins" with the six points carried in; spec raw and block first; the run's place and its wait. CONFIRMED: rt4:24–29; routing:8 and :12–16; readings:5–7.
81. T4 placement. Claim: the line goes after the entry's last non-blank line, which is the coordinating session's close line. CONFIRMED: RESULTS.md:990 is that last line, and :992 opens the next entry.

TOTALS: 81 items: 72 CONFIRMED, 5 IMPRECISE (31, 39, 52, 60, 65), 1 FAIL (69), 3 NOT CHECKABLE (76, 77, and none other). Correction: NOT CHECKABLE is 2 (76 and 77), so the totals are 73 CONFIRMED, 5 IMPRECISE, 1 FAIL, 2 NOT CHECKABLE.

OBSERVATIONS
1. What "@REST@" should hold: four commands ran after the draft's sweep and up to this brief's hash.
   - 22:59:37.654Z: checks of the four texts. Line counts by `grep -c ''`; widths by `grep -n -E` under LC_ALL=en_US.UTF-8, filtered by `grep -v` with `cut` and `tr`; placeholders by `grep -o -E` and `sort`; local-root and id counts and bracketed marker counts by `grep -c`; and `tail -c 2` of the entry into `od -An -c`.
   - 22:59:55.552Z: `grep -F` with a tab over the draft sweep's file in scratch, with `tail -n 1`, `sed -n '54p'` and `cut -f1`.
   - 23:00:02.285Z: a `cd` into scratch; `shasum` of 11 named scratch files into the sources list (a write in scratch); `shasum -c` counted by `grep -c`; the list's `shasum` and `grep -c ''`; and `shasum` and `grep -c ''` of the close's window note in the notes folder.
   - 23:00:57.902Z: `diff` of `sed -n` ranges (by process substitution) of the close's values-check brief against this brief; this brief's line count, widths (`grep -v -F`, then `grep -c -E`) and `shasum`.
   Across the four, the bracketed counts are 0 for markers, Q-F3's folder and the holding folder, in both the argv and the outputs. The file tools in the same interval were a Read of S/step4b/camp/close/vc_brief.md, five Edits of the entry draft, and the Write of this brief. That Read's output holds all five marker words, so it is a sixth file-tool read with marker words for the Counts item.
2. Five more Bash calls ran after the brief's hash (23:01:20.970Z to 23:03:13.844Z), outside this check's range. They made the gate's next version by `cp` (with `cmp`, `shasum`, `bash -n` and `diff`), viewed the close's display source, ran `cat` of check_msg.sh and the close's message source plus a `git log -1`, and ran `bash -n` and `zsh -n` of the seat scripts. Item 76's gate is among them. The entry's sweep takes them in if it is to reach the commit.
3. Counts, Q-F3: the bare short name, without "data/", appears in a fifth command output: the `sed -n` of the kit scripts' heads at 22:47:46.779Z, in one line of a kit comment. Code's pattern was the `data/` form. Say which form "short name" means.
4. Counts, holding folder: its bare name (the stage name plus "-v1", without `noindex/n/`) appears in one command output: the `grep -n -A3 -E` of the close's window note at 22:54:43.533Z, whose point 2 quotes the names record. That is not the name as the brief defines it.
5. Inputs written or sent, which are text and never argv, also hold these strings:
   - The holding folder's full name: the close's window note (Write, 08:54:37Z) and its request (SendMessage, 08:55:04Z).
   - Q-F3's folder name and one marker word: the readings (Write, 18:07:12Z) and the readings message (SendMessage, 18:08:30Z).
   - Marker words: the survey brief (17:32:39Z), a memory note (18:09:16Z), the entry draft (22:57:22Z, and an Edit at 22:59:44Z), and this brief (23:00:50Z).
   T1–T4 themselves hold none; T2b holds marker words on four lines, as T3:127–128 declares. The three SendMessage calls are named nowhere in T3's departures.
6. Small command parts outside item 1 that T3 does not name. Each command is otherwise covered.
   - A `cd` into scratch at 22:47:31.180Z and 22:47:35.089Z.
   - At 09:06:11.110Z, the manifest-versus-blob loop (`cut`, `grep`, `while read` of `git show HEAD:<path>` into `shasum`) and `--no-renames`.
   - `wc -l` of the verify output at 09:05:45.626Z.
   - A `sed -n '1,40p'` filter of `grep -n` output at 22:49:42.655Z.
   - `sed` trimming `shasum` output at 18:07:54.016Z.
   - `test ! -e` at 08:48:46.434Z and 08:52:42.108Z.
7. Points in §1 as sent that are imprecise and that the head does not name:
   - (a) GR8 (readings:115), "the output absent (`guard.refuse_out`, guard:74–81)". `refuse_out` refuses paths under its refused roots, or inside the repository but outside data/n/; it never tests whether the output exists. The existence test is GR12's "refused if it exists".
   - (b) GR5 (readings:91) says the shadow reading "never reads N1-R's −1 cells", but GR2 (readings:46) reads and checks all 138. T1 has it right.
   - (c) GR7 (readings:102) cites probe:41 for `fit_lr`. probe:41 imports only `kfold_auc` and `kfold_shuffle_null`; `fit_lr` arrives through `kfold_scores` (kprobe:78–92).
8. Points in §4 as sent:
   - (a) report:320 says "The only `VECLIB_MAXIMUM_THREADS` is in … :1156". `git grep` (item 3's pathspec) finds 4 lines: scripts/audit_note_N3_compute.py:710, :1156 and :1184, and results/raw/2026-10-08_note-N3-echo-compute.md:9. None is in n's code, so the survey's point stands.
   - (b) Superseded in the way §4's 1.5 is: report:3 and readings:6 call the seat's raw untracked (it was committed at 13ca2fe, sha256 unchanged), and report:116 says "The latest committed routing raw is 2026-11-24's" (two 2026-11-25 raws are now committed).
9. T2:21: ans4's lines are those of a file that was untracked at 95cd461 and committed unchanged at 13ca2fe. The head could say so.
10. T4:2, "The seat's raw is the coordinating session's close line above", reads as if the raw were the line. Write instead: "The seat's raw is the one the coordinating session's close line above cites (`13ca2fe`; its §1 and §3)."
11. T1:74 writes `load_cell(staging, arm, direction, dose, …)`, while the readings' GR2 writes `label` and cells:135 has `dose_label`. This is harmless.

DEPARTURES
1. Reads beyond the brief's source list, made to check citations in T2b's §1 and §4:
   - ADDENDUM-n3 (four cited lines) and ADDENDUM-n2 (one count).
   - results/raw/2026-11-23_first-sitting_pi-routing.md:27–31 and ans21b:70, printed.
   - 15 further seat and PI raws under results/raw/, one cited line each, printing only the words a `grep -o` found.
   - valence_core/discrim.py: its def and import lines, and `shasum`.
   - valence_core/m/guard.py:85–96.
   - data/n/gates/G-ANL-n.json: `shasum`, `wc -l`, and `jq` of its keys (a committed JSON outside the barred folders, which the brief allows for `jq`).
   - results/raw/2026-11-25_n-campaign_close-names.txt: `shasum` and `wc -l` only.
   - Three `git grep` content searches: two with item 3's pathspec and Q-F3's exclusion, one over named n files.
2. A slip in three commands: a shell variable or environment prefix whose name starts with the letters "awk" (`awk_free=1`, and `awk_never=1` and `awk_no=1` placed before `/usr/bin/grep` and `tail`). No awk ran, and no marker was involved. Declared for the seat to class.
3. Three commands errored and did nothing more: `cat -A` and `head -0` (refused by the BSD tools) and one `grep -o -E` (repetition count too large). Two outputs went to /dev/null; no file was written.
Otherwise none:
- No interpreter ran but `shasum` and `jq`; nothing was written; no network was used.
- No guard marker was in any argv (patterns bracketed). Q-F3's folder was written only bracketed, and the holding folder was never named in an argument.
- Nothing under data/*/ckpt, data/*/reports or data/m[f]3 was read, listed, sized, timed or hashed.
- In S and N, only the named files were read.
```
