# G-PWR (Q-F3)'s run of record: its values-check

*Code's raw, PI date 2026-11-14.*
- *What was checked:* the draft of the RESULTS.md entry for G-PWR (Q-F3)'s run of record; the record
  `data/mf3/gates/Q-F3_G-PWR.json` (sha256 `75d1d46b…01e5`, untracked at the check); the run raw
  `results/raw/2026-11-14_mf3-gpwr.txt` (`fb61d87a…70e2`); and Code's block
  `results/raw/2026-11-14_mf3-gpwr_code-to-design.md` (`d37316a5…4d06` at the first pass, `e609b432…b06e` at the
  second, `96ec20f9…3e90` as committed).
- *Against:* the seat's answers of 2026-11-14 (at `cdccc66`); PROPOSAL-m v1.11; F-5; Q7; LOCK-m-F3 v0.2; the seat's
  `pq:` raw, §5; RESULTS.md (the G-F3 entry, the program's entry at `46be7aa`, G-PWR for Q-F0's run of record); the
  committed program at `46be7aa` with its three raws, `scripts/m_gpwr.py`, `scripts/m_analyze.py` and mf3's modules.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written. Under
  `data/` it read only the record, which is in `data/mf3/gates` (not a ckpt or reports directory). It ran no
  repository program and no model. Its recomputations are its own standard-library code, from the spec.
- *Outcome:*
  - the first pass, 53 items: 45 CONFIRMED, 3 IMPRECISE, 3 FAIL, 2 NOT CHECKABLE. Every figure equals its own
    recomputation; the three FAILs are in the block's account of the readings;
  - the second pass, on the ten changed passages: 6 CONFIRMED, 3 IMPRECISE, 0 FAIL, 1 NOT CHECKABLE.
  - HEAD was `46be7aa` at the start and the end of each pass.
- *Code's masked scan of the checker's transcript* (counts only; no command text printed): 210 distinct tool calls.
  None names a ckpt or reports path, and no metadata form names `data/`. Nothing under `data/` but the record is
  named. Nothing under the tasks folder is touched, and no transcript is opened.
- *This raw:* Code's dispositions, then the two reports verbatim.
  - Code extracted each report by script from the agent's hand-backs: the first sha256 `ea9e504e…67d0`, 262 lines, no
    final newline; the second sha256 `33d3d03a…c402`, 72 lines, no final newline.
  - Code's leak check found no local path, user name, session id or temp-dir id, and no clock time.

## Code's dispositions

- **The first pass's three FAILs and three IMPRECISE items are applied, as its fixes have them** (items 8, 13, 29,
  32, 38 and 43).
  - On item 32, the block's R2 now states its alternative's effect: a strike to F-5's literal 96/32 would make A1's
    L 160, with 864 launches, 22 looks and 154–171 h at m:230's basis. Code recomputed these figures by tool, and the
    second pass recomputed them by its own scan.
- **The second pass's three IMPRECISE items are applied** (1, the closure's binding; 3 and 7, R2's alternative,
  which is the review's round-1 NOTE 6). Items 3 and 7 correct the first pass's own wording of item 29.
- **NOT CHECKABLE** (the first pass's 34 and 36, the second's 5): future acts, and Code's reads. No change.
- **The checker's disclosures:** no change needed.
  - In the first pass, the harness saved two long outputs to the session's own tool-results folder, and the checker
    did not open them: part of the record's projection case, and PROPOSAL-m's lines 300–372.
  - One names-only `git status --porcelain` had a pathspec that included `data/mf3/gates`.
  - In the second pass, `diff -u` printed the modification times of files outside `data/`; none is reproduced.

## The checker's first-pass report (verbatim)

VALUES-CHECK: G-PWR (Q-F3), run of record. The draft entry (S/entry_run.md), the record, the raw and Code's block to the seat. Blind check, read-only.

I found 3 FAILs, 3 IMPRECISE items and 2 NOT CHECKABLE items. Every figure checks out. The errors are in claims about the readings and their attribution (items 32, 38, 43).

HEAD at my start: 46be7aa. HEAD at my end: 46be7aa.

Files checked (sha256), all unchanged from my start to my end:
- record `data/mf3/gates/Q-F3_G-PWR.json`: 75d1d46bdfffe52f2704cd9ad5d87bc8627342f49ca1629977ba793370e001e5. This equals the draft's value.
- raw `results/raw/2026-11-14_mf3-gpwr.txt`: fb61d87a3958bb64df38aa94220bd7cd31235ffa465fb81bc4707171c1c470e2.
- block `results/raw/2026-11-14_mf3-gpwr_code-to-design.md`: d37316a541942a01337d3f91e51dbba56dfc191f511d1494a920ec542b8c4d06.
- draft, as read: 83b2c0166545e0dd7f8e476cecc3be8e9d54031b4af2fd94433c14677dae846c. I hashed it at my end only.

Method. My own standard-library code, in the brief's notes folder V (vc_lib.py, vc_part1–5.py and their stdout files), run as `python3 -I`. It imports no repository code. It works from the spec: m:184–192, m:230, m:271, m:297, m:316, m:330, and m:190's base case as defined by the analyzer's `power_exact` and `f3_power_block`. Results were compared to the record's exact "num/den" strings as Fractions. Displays use half-up rounding.

Anchors used below:
- D:N is the draft's line N.
- B:N is the block's line N.
- W:N is the raw's line N.
- seat:N is `results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md`.
- rev:N is `results/raw/2026-11-14_mf3-gpwr-program_review.txt`.
- RESULTS.md lines are at HEAD.

THE DRAFT

1. D:1–2, the citations. CONFIRMED.
   - m:285 is G-PWR; m:298 is G-VER, G-PWR and LOCK-m-F3 v1.0. F-5 is ganl-f3 raw:28. §A.7 is seat:50; §D items 3–4 are seat:92–93.
   - cdccc66 is the seat raw's first commit. Its RESULTS.md hunk quotes the PI's "Route as given" of 2026-11-14.
   - 46be7aa is the program's commit.

2. D:3–6. CONFIRMED by recomputation:
   - m:238's row: 128/64/224/96/224/96, 832 launches, 21 looks.
   - Power .878, .862 and .927; 148–165 h.
   - "The cap is the PI's" (seat:46).

3. D:7–8, the record's path, its sha256, and "written once". CONFIRMED. The shasum is equal. The record was absent at launch (W:15), and the run wrote it once (W:258).

4. D:9–10: venv Python 3.12.9, `-I -B`, a pycache prefix that does not exist, `env -i`. CONFIRMED.
   - W:4–8. The wrapper refuses if the prefix exists (W:348). It runs under ENVI (W:346, W:372).
   - The record's provenance gives python 3.12.9 and isolated true.
   - The raw's "as at G-PWR (p)" (W:6) is also confirmed: `results/raw/2026-11-13_p-gpwr.txt`:4 and :6.

5. D:11–16, the launch checks. CONFIRMED.
   - W:9–15 and the wrapper's source (W:332–390). The git config check is empty now. The working-tree blob fbbb2831… equals HEAD's.
   - The "no git fsck" line repeats Code's reading already committed at RESULTS.md:145, of list v2 item 2 ("read by nothing but…", list-v2 raw:19). It is not a new rule.

6. D:17–18, the self-test. CONFIRMED.
   - 28 PASS lines plus the summary, no other line (W:19–47).
   - These lines are identical to the committed self-test raw's 29 lines (`results/raw/2026-11-14_mf3-gpwr-program_selftest.txt`:11–39).
   - It runs in its own process from the load commit's blob (`_selftest_child`, scripts/mf3_gpwr.py:2069).

7. D:19–22, the provenance hashes. CONFIRMED.
   - HEAD 46be7aa; script 2b575ef8…d161; m_gpwr 1d7c0fe3…111c from blob 6d05c8e6…; analyzer d347ea0c…5e48. Each recomputed from 46be7aa's blobs.
   - m's package 7756dcf4…49bb (18 files) and mf3's 098455d9…da13 (15 files), by my own code for `package_sha256_of`'s formula (valence_core/m/resume.py:328).

8. D:23, "every repository module loaded, 18 beside the script, bound to its blob". IMPRECISE.
   - True: the record's closure has 18 entries, and each sha256 equals its 46be7aa blob.
   - Off: `closure_files` (scripts/m_gpwr.py:1426) leaves out m_gpwr, the analyzer and valence_core/m/*.py. The run also loads those (READINGS items 12 and 20; the power comes through the analyzer). They are bound by name and by m's package sha256.
   - Fix: "every other repository module loaded (the closure: 18, beside the script, m_gpwr, the analyzer and valence_core/m), bound to its blob".

9. D:24–25, the sources. CONFIRMED.
   - Seven entries. I recomputed each sha256 at its own commit and all are equal.
   - main() checks the sources in the run itself (mf3_gpwr.py:2116), not only in the self-test.
   - cdccc66 and 2193832 resolve to the pinned full shas. The seat's raw first appears at cdccc66.

10. D:26–27, the second run. CONFIRMED.
    - W:261–264.
    - The scratch second-run record's sha256 equals the record's.
    - The two stdout .cmp files have equal digests. The WROTE lines name the same sha256.
    - Same command (W:378).

11. D:28, verifier 55/55 on 3.9.6 with `-I -S`. CONFIRMED. W:266–323 holds 55 PASS lines and no other; W:7.

12. D:29–31 and D:34, the verifier's scope. CONFIRMED by its source (W:392–656).
    - It recomputes launch(), all rows, the looks, the bars (with half_up and n_j_exact), the absolute halves, 1 − Π(1 − union) from the record's unions, and the hours.
    - It does not compute the Fisher half or the union.
    - It checks the power only against 17/20, its display, n/mS and the gate flags.

13. D:32–33, "The blind review recomputed those". IMPRECISE.
    - What the review recomputed:
      - all nine unions (rev:515);
      - the Fisher half for five of the nine pairs: the projection's three and A1's two floor cases (rev:253–255);
      - six grid points (rev:256).
    - The full grids, the refined maxima and the union grid came from the builder's recomputation (RESULTS.md:84–87).
    - The digest pin is true. REVIEWED_EXACT_SHA256 ab9f2fc8… (mf3_gpwr.py:527, `exact_figures` :1041) covers the power, the bars, every half and union, the full grids, the maxima and the hours. The record's exact values hash to it by my own hash.
    - Fix: "The blind review recomputed the nine unions, five of the Fisher halves and six grid points. The builder's recomputation of all of them is pinned by the self-test's digest." Optionally add that this values-check recomputed all of them (items 21–23).

14. D:34–35, the power displays held to m:190 and bound to its text. CONFIRMED. POWER_ORACLE (mf3_gpwr.py:150) is checked at :1101, and `build_sources` quotes m:190's sentences (:605–608).

15. D:36–39: WRAPPER EXIT 0, the raw's contents, paths scrubbed, the "wrapper rc=0" note. CONFIRMED.
    - W:325–330.
    - After scrubbing, the raw's wrapper and verifier sections equal the scratch files that ran, and its output part equals the wrapper's captured output.
    - No local path, user name or session id appears in the raw, the block or the draft.

16. D:40–41: r is one rate; per-template A1 3/4, A2 4/4, A3 6/8, A1s 4/8, A2s 4/8, A3s 8/8. CONFIRMED (m:192; seat:15; the record's inputs).

17. D:43–47, the launch table. CONFIRMED by exact recomputation:
    - floors 80/32/144/56/144/56;
    - ⌈1.15 floor⌉ 92/37/166/65/166/65;
    - N90 119/50/210/84/210/84;
    - units 32/32/16/16/16/16;
    - L 128/64/224/96/224/96.

18. D:49: total 832, 21 looks, the same row at k = 28–29 (m:238). CONFIRMED.

19. D:49–50, rows k = 1–40. CONFIRMED. All 40 equal the record's rows_by_k. They agree with:
    - m:234–241, including each row's hours at m:230's basis;
    - m:243's 992, 1,088, 1,152, 1,184 and 23,328;
    - m:330's uncached look counts 17/19/20/20/21/22/23/24.

20. D:51–53, the power. CONFIRMED. My implementation of m:190's base case follows the analyzer's PASS definition: (i)–(iii), a floor/ceil split per map, the sham pooled at .5 (scripts/m_analyze.py:359 and :3402).
    - A1 (80, 32) .878 (.8784); A2 (144, 56) .862 (.8620); A3 (144, 56) .927 (.9273); A1 at 96/32 .916 (.9161). Each exactly equal to the record.
    - The same code reproduces m:190's (144, 48) .848, A3's .665 at P .60 and .990 at P .70, and the critical counts 87, 83, 60 and 51.
    - The program calls f3_power_block (mf3_gpwr.py:820).

21. D:54–61, the false-pause table, all four rows. CONFIRMED. Every n_j, crit_j and exact sequential false pause equals the record's:
    - projection: .1703, .1584, .1641;
    - floors at r (45, 78, 78): .1547, .1441, .1482;
    - floors (32, 56, 56): .1370, .1225, .1354;
    - realised: .1553, .1601, .1333, with the half-up counts and the n_j_exact strings.
    - The looks are 21, 20, 18 and 21 by the campaign rule, which is the lock's interleave PIN (LOCK-m-F3.md:740–748).
    - Guard unions .2094/.2401/.2327, .2050/.2355/.2297 and .1925/.2265/.2162. Unit figures .5390, .5318 and .5105.
    - All by my own 2-D DP. abs crit_j, Fisher cells_j and looks_n1_n2 are also equal at every look.

22. D:63, the halves. CONFIRMED: A1 .1599/.1070, A2 .1781/.1320, A3 .1682/.1322.

23. D:64–65, the grid maxima. CONFIRMED.
    - I recomputed the full grids exactly: all 3 × 99 values equal the record's.
    - Unique maxima at 11/20, 31/50 and 14/25.
    - Refined ±.01 by .001: unique maxima at 11/20, 309/500 and 559/1000.
    - The union over p = j/100 ≤ .20 rises strictly to .20.

24. D:66–68, the joint. CONFIRMED. Each bar's own figure, with the unions and .5390 beside (READINGS item 17). The record's not-computed text is one sentence (Q7 (c)).

25. D:69–70, "Not figured". CONFIRMED (m:271; m:330's three reported items).

26. D:71–72, the hours. CONFIRMED. 166816/1125 and 185536/1125 give 148.28–164.92, so 148–165. The "m:205" quotes match §A.7 (seat:50) and §D item 3 (seat:92).

27. D:72–80, §A.5 beside. CONFIRMED.
    - Each of the record's six rows is a byte-substring of the seat raw at cdccc66.
    - The short forms match seat:35–44.
    - "as the realised basis of record" is seat:50.
    - Aside: §A.5's own arithmetic is consistent (300.1, 325.7, 446.4, 684.7, 305.0 h).

28. D:81–82, READINGS. CONFIRMED. Items 1–6 are each verbatim in their sources (§A.7; F-5; Q7's opening sentence and (a)–(c), step-15 raw:46–51). Items 7–20 are Code's 14 readings.

29. D:82–84, "lists R1–R9 with the review's alternatives". IMPRECISE.
    - The review names alternatives for R1 and R3–R7 only.
    - R9 is not in the review.
    - R5's listed alternatives are not the review's (item 43).
    - Fix: "lists R1–R9, with the alternatives the review named (R1, R3–R7)", once R5 is corrected.

30. D:85–91, the one-line summaries of R1–R9. CONFIRMED.

31. D:92, "Q1 (R1) and Q2 (R9) are for the seat. Neither blocks the PI's cap". CONFIRMED (B:76–81; §D item 4).

32. D:92 "none of R1–R9 moves the launch counts or the looks", and B:27 "None of them moves the launch counts or the looks". FAIL.
    - R2 (READINGS item 8) puts A1 at 80/32 "in the power (.878) and the launch rule alike".
    - A strike to F-5's literal 96/32 would change the launch rule: ⌈1.15·96⌉ = 111 and N90 = 142 at r = 29/40, so A1's L = 160. The total becomes 864 and the looks 22, which is m:224's row.
    - Correct form: "none of R1 and R3–R9 moves the launch counts or the looks; a strike of R2 would (A1 160, total 864, 22 looks)".

33. D:94–97, the cap: the PI's, at G-PWR's entry (§D item 4), written into LOCK-m-F3 v1.0 (m:298, m:249); none set; v1.0 by D2 2026-12-22 (§D item 5). CONFIRMED (seat:46, :93–94; the record's cap field).

34. D:95–96 and D:99–100: the figures go to the coordinating session, the track STOPs, committed by path, not pushed. NOT CHECKABLE (future acts). The run's model-free nature is supported by the wrapper's source.

THE BLOCK

35. B:3–10, the header facts. CONFIRMED.
    - The seat raw's path, cdccc66 and 6b963adf…0db3a; §A.7 and §D items 3–4; "Route as given".
    - The script's sha and 46be7aa; the record 75d1d46b…01e5.
    - LOCK-m-F3.md at v0.2; F-5's "Nothing of it touches a file a lock names" is verbatim.

36. B:8–9, "Read: …; Not opened: …". NOT CHECKABLE (Code's process). Note: if "Read" is meant as the program's inputs, it omits valence_core/mf3/resume.py, the seventh source.

37. B:14–27, §0's figures, the cap, and Q7's quote. CONFIRMED. B:27's last sentence is item 32.

38. B:31, "Each is in the record's READINGS (items 7–20 …)". FAIL.
    - R9 is in no READINGS item. No item names G-VER. Items 7–20 are: form, A1's floor, power floors, launch rule, projection, bar domains, floor case, realised case, rounding, guard, joint, hours, cap, LOOK_EVERY.
    - Correct form: "R1–R8 are in the record's READINGS (items 18, 8, 13, 14, 15, 16, 17, 20); R9 is this block's own".

39. B:34–40, R1. CONFIRMED.
    - item 18; m:205, m:230 and m:238; §A.5's last row.
    - The review's NOTE 1 alternatives, (b) and (c), are at rev:153–158.
    - 832 × 488 s = 112.78 h, and the record has no 112.78.

40. B:41–43, R2. CONFIRMED (item 8; F-5's "A1 96/32"; m:184's "96 cached, 80 uncached / 32"; LOCK-m-F3.md:107–110).

41. B:44–47, R3. CONFIRMED.
    - item 13; 45/78/78 and 32/56/56.
    - The review's NOTE 4 (rev:161): A1s 64, A2s would need 112 against its L of 96, A3s 56. Recomputed.

42. B:48–52, R4. CONFIRMED.
    - item 14; §A.1's 189/98 and its per-template 52/57/80 and 25/25/48 (seat:13).
    - NOTE 2 (rev:159); "not of record" per Code's disposition (rev:353).

43. B:53–54, R5, read with B:31–32's "the alternatives are the ones the blind review named". FAIL.
    - The review's NOTE 3 names "Floor, or a fractional-n mixture" (rev:160). Code's disposition names none (rev:354).
    - The block's "ceiling" and "whole units per launch" are not the review's, and it drops the fractional-n mixture.
    - Correct form: "Alternatives (the review's NOTE 3): floor, or a fractional-n mixture". Any others should be marked as Code's.

44. B:55–59, R6. CONFIRMED.
    - m:316: per contrast arm, against its matched sham. m:285's quote is verbatim.
    - The figure is exact because the pairs are disjoint; my 1 − Π(1 − u) equals the record's.
    - The per-arm alternative is round 2's NOTE 1 (rev:437).

45. B:60–63, R7. CONFIRMED (item 17; NOTE 5, rev:162). "with the other two bars beside" is Code's harmless gloss on the review's "round_degeneracy's own figure".

46. B:64–68, R8. CONFIRMED (item 20; RESULTS.md:63–68).

47. B:69–72, R9. CONFIRMED.
    - The quotes are verbatim: seat:50 and pq: raw:53. m:284 is G-VER.
    - mf3 runs G-VER on every session before its record is written (valence_core/mf3/stages.py:24, :736–745).
    - "All 40 records are verified" is RESULTS.md:930–931 and :989; "every record verified" is seat:13.
    - The reading itself is Code's and goes to the seat as Q2.

48. B:74–81, §2's questions and "None blocks the PI's cap". CONFIRMED.

49. B:85–87, the cap, and "R2–R8 stand on Q7's terms". CONFIRMED as Code's committed reading.
    - Q7 is the seat's ruling for Q-F0's G-PWR (step-15 raw:46).
    - Carrying it to Q-F3 is recorded at RESULTS.md:55–57 and in READINGS item 3.
    - No seat text extends it in words.

50. B:88–91, the observation. CONFIRMED.
    - .16–.17 and .21–.24 round the projection's figures, and .5390 is the unit figure.
    - Q-F0's G-PWR: 5 looks (RESULTS.md:7788), .0976 (:7794), .1496 (:7802).
    - The "rule 11" form follows seat:48.

51. B:92, the run's facts are in the entry. CONFIRMED.

THE RAW AND THE RECORD

52. W:48–258, the report section, and W:17–18, the PROVENANCE and SOURCES lines. CONFIRMED.
    - My line-by-line rendering from the record equals every line: header, POWER, LAUNCH, TOTAL, all 40 rows, every case's looks, bars, guard regions, figures, grid (99 points × 3), maxima, unit line, JOINT and its sentence, HOURS, BESIDE, CAP, NOT FIGURED, the 20 READINGS and WROTE.
    - The PROVENANCE and SOURCES JSON parses equal to the record's.

RULES AND PRECEDENTS

53. Is anything stated as a rule or precedent that no committed record or the seat's raw states? CONFIRMED, none found.
    - The "no git fsck" line is committed at RESULTS.md:145.
    - Q7's terms: item 49.
    - "Code's Q-F0 reading kept": RESULTS.md:7795–7796.
    - "As at G-PWR (p)": item 4.
    - "Rule 11": seat:48.

TALLY: 53 items. 45 CONFIRMED, 3 IMPRECISE, 3 FAIL, 2 NOT CHECKABLE.

NOT CONFIRMED:
- 8 IMPRECISE: D:23, the closure's wording.
- 13 IMPRECISE: D:32–33, what the blind review recomputed.
- 29 IMPRECISE: D:82–84, "with the review's alternatives".
- 32 FAIL: D:92 and B:27, "none moves the launch counts or the looks". A strike of R2 does: A1 160, total 864, 22 looks.
- 38 FAIL: B:31, "Each is in the record's READINGS". R9 is not.
- 43 FAIL: B:53–54, R5's alternatives are not the review's ("floor, or a fractional-n mixture").
- 34 NOT CHECKABLE: D:95–96 and D:99–100, future acts.
- 36 NOT CHECKABLE: B:8–9, Code's Read and Not-opened lists.

DISCLOSURES. No breach of the brief or of list v2 that I know of.
- Two of my command outputs were too long to show inline. The harness saved them to its own results folder in this session's project directory, outside V. One held part of the permitted record's projection case; the other held PROPOSAL-m lines 300–372. I did not write or open those files.
- In the brief's scratch folder S (run subfolder) I read the wrapper, the verifier, the first-run stdout and the captured wrapper output. I hashed the second-run record and the two .cmp files, digest only.
- In V I wrote `.txt` copies of the committed scripts/mf3_gpwr.py, scripts/m_gpwr.py and scripts/m_analyze.py, from `git show`. I read them and never ran or imported them.
- I used `wc -l` on non-data texts only, and one names-only `git status --porcelain` with a pathspec that included data/mf3/gates.
- My only content search was a `git grep` carrying ':!data/**'.
- Nothing under tasks/, no transcript, no repository program, no git write.

## The checker's second-pass report (verbatim)

VALUES-CHECK, SECOND PASS: the ten changed passages of the G-PWR (Q-F3) draft entry and of Code's block. Read-only, under the same brief.

Result: no FAIL. 6 CONFIRMED, 3 IMPRECISE and 1 NOT CHECKABLE. Two of the IMPRECISE grades (3 and 7) come from my own first-pass wording, which Code applied and which was too narrow.

HEAD at start: 46be7aa. HEAD at end: 46be7aa.

Files checked (sha256), unchanged through the pass:
- block: e609b43223a0b5b16ec7ea67ace31b61eca546e940711ce4c8179beed209b06e. This is the value you gave.
- draft (S/entry_run.md): 067ee26e40a8edbf282e8ce4ce2f06ffee1711ac73b72b563c3a3e776c1f37af.
- record: 75d1d46b…01e5, unchanged.
- raw: fb61d87a…70e2, unchanged.

Nothing else changed:
- I rebuilt both earlier versions in my notes folder V from my first-pass reads. The rebuilt block hashes to d37316a5…4d06 and the rebuilt draft to 83b2c016…846c, so both are byte-exact and the diffs below are complete.
- The block's diff has six hunks, which are exactly passages 5 to 10. The draft's diff has four hunks, exactly passages 1 to 4.

Anchors: D:N is the new draft's line N, B:N the new block's line N, rev:N the review raw's line N.

1. D:23–24, the closure. IMPRECISE (minor).
   - Confirmed: the closure has 18 entries beside the script, each bound to its 46be7aa blob. "The closure of the repository modules this process loaded" is the program's own term (scripts/mf3_gpwr.py:2024, :2032, :2065).
   - Off: "by m's package sha256" holds only for valence_core/m (mf3_gpwr.py:2056–2059). m_gpwr and the analyzer are bound by name (scripts/m_gpwr.py:1421–1423) and by their own sha256s and blob, which D:21–22 already give.
   - Fix: "`m_gpwr` and the analyzer are bound by name (their sha256s above), and `valence_core/m` by name and by m's package sha256."

2. D:33–35, what the review, the builder and this values-check recomputed. CONFIRMED.
   - The review: the nine unions (rev:515), five of the nine Fisher halves (rev:253–255) and six grid points (rev:256).
   - The builder: "every printed figure but the unit's guard figure", pinned by the digest (RESULTS.md:84–87). REVIEWED_EXACT_SHA256 (mf3_gpwr.py:527) is taken over exact_figures (:1041–1062), which holds every half and union, the full grids and the maxima.
   - This values-check: in the first pass I recomputed all of them, including the 3 × 99 grid values and the refined maxima.

3. D:85–86, "with the alternatives the review named (R1, R3–R7)". IMPRECISE.
   - The review's round-1 NOTE 6 (rev:163) also names R2's alternative. It sits under the heading "readings with alternatives, for the seat" (rev:151) and is titled "A1 at 80/32 rather than F-5's literal "A1 96/32"". Code's disposition carries it to the seat as a declared reading (rev:349–356).
   - This corrects my first-pass item 29: I said there that the review named alternatives for R1 and R3–R7 only, and Code applied that wording.
   - Fix: "(R1–R7)".

4. D:94–97, the R2-strike figures. CONFIRMED. I recomputed them with a fresh linear scan:
   - ⌈1.15 · 96⌉ = ⌈110.4⌉ = 111.
   - N90 = 142 at r = 29/40 (141 fails).
   - L = 160 at unit 32; 864 launches; 22 looks. This is m:224's cached row at k 29–28 (160/64/224/96, 864, 22).
   - At m:230's basis, 864 × 641.6–713.6 s = 153.98–171.26 h, so 154–171 h; m:239's 864 row gives the same.
   - "None of R1 and R3–R9 moves the launch counts or the looks" holds.
   - "§A.5 figures its hours on 832 launches with A1 at 128" holds: the seat raw's line 35 says "832 launches (A1 128, …)" and "832 launches × the basis".
   - "Neither blocks the PI's cap" is unchanged and holds.

5. B:8–10, the "Read:" sentence. NOT CHECKABLE: the acts of reading and not opening are Code's, as in the first pass. The list itself is now right:
   - the seven named are exactly the record's seven sources, in the record's order (raw line 18);
   - the review raw is the one B:34 cites;
   - my first-pass note about the missing mf3 `resume.py` is resolved.

6. B:26–28, the §0 last bullet. CONFIRMED, on item 4's figures.

7. B:32–34, the §1 opening paragraph. IMPRECISE, for the same reason as item 3.
   - Confirmed: "R1–R8 are in the record's READINGS (items 18, 8, 13, 14, 15, 16, 17 and 20)". Each maps correctly, in R order, and no READINGS item names G-VER, so "R9 is this block's own" holds.
   - Off: "R2's is F-5's literal text" is true, but set against "the ones the blind review named" it implies the review did not name R2's alternative. NOTE 6 does (rev:163).
   - Fix: "The alternatives for R1–R7 are the ones the blind review named (…); R2's, F-5's literal text, is its round-1 NOTE 6."

8. B:43–48, R2. CONFIRMED.
   - The figures are item 4's.
   - "The alternative is F-5's literal 96/32" matches F-5 (the G-ANL-F3 answers raw, line 28).
   - "LOCK-m-F3 v0.2 §3 takes the campaign's launches from the uncached table (m:234–241)" is LOCK-m-F3.md:129, inside v0.2 §3 (lines 107–131): "The campaign's launches are the uncached table's, m:234–241 (v0.2 §4)."

9. B:58–60, R5's alternatives. CONFIRMED. The review's round-1 NOTE 3 has "Floor, or a fractional-n mixture, are alternatives" (rev:160), and rev:153–168 are round 1's NOTEs.

10. B:93–94, the §3 R2–R8 bullet. CONFIRMED.
    - Of R2–R8, only R2's strike moves the launch counts and the looks (item 4).
    - The hours the cap is set on are §A.5's (§D item 4), computed on 832 launches (seat raw line 35), so they would move with the launch count.

TALLY: 10 passages. 6 CONFIRMED (2, 4, 6, 8, 9, 10), 3 IMPRECISE (1, 3, 7), 0 FAIL, 1 NOT CHECKABLE (5).

DISCLOSURES:
- I wrote two rebuilt files in V (the earlier block and the earlier draft) and diffed them.
- `diff -u` printed the modification times of the files it compared. These are files in V, in the scratch folder and under results/raw, none under data/. No time is reproduced in this report.
- Under data/ I only hashed the record this pass.
- I ran no repository program, made no git write and searched no content.
