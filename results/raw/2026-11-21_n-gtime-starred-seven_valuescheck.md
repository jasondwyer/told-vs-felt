# n — the seat's block on G-TIME-n's seven starred readings: the blind values-check, as returned, with every disposition

PI date 2026-11-21. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three drafts, at HEAD `c9d35e2`:
- T1, the block, sha256 `d6446163…2c26` (347 lines);
- T2, the head of G-TIME-n's spec raw, `8fc1f2bc…1283` (26 lines), and the raw built from it, `3459ce10…33a8` (539
  lines): the head's claims, and each fenced section against its source;
- T3, this commit's entry, `3ea89176…1ce8` (56 lines), its values-check line a placeholder not to be checked.

**The checker's brief** was given to the checker as its prompt: Code's scratch file `S/step4b/gtime/seat/vc_brief.md`
(`3fe1ebf0…7604`, 98 lines), which the prompt as sent, recovered from this session's transcript by `jq`, equals. It:
- named the texts and the sources. In the repository, the files the texts cite, at `c9d35e2`, each checked tracked and
  clean. In Code's scratch, by name and sha256 only: the readings as sent, the routing, the survey's brief in both
  forms, and its report. The shared note, by its sha256 alone;
- allowed `shasum` by name, and `jq` on committed JSON outside `data/*/ckpt`, `data/*/reports` and `data/mf3`. It
  barred any other interpreter (`awk` among them), any write, any network, any guard marker in an argv (a grep pattern
  included), and globs over the root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/mf3`, any read, listing, size or time of a ckpt or reports file, and anything in Code's
  scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the `data/mf3` exclusion on
  every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (186 lines, sha256 `4985a47d…4299`).
It names scratch files only by their paths inside the scratch folder, and the shared note as N/....

**Totals:** 94 items: 74 CONFIRMED, 12 IMPRECISE, 1 FAIL, 7 NOT CHECKABLE; and 10 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every IMPRECISE item and the FAIL are applied, in the words below or the checker's. Every observation is applied or
met. §2 gives the edits and their check by tool.

- **Item 23 (FAIL), T1:105–106.** The hash tail `…b8f` had three characters, typed by eye. It is `4c92f228…bb8f`, by
  tool, as the checker gives it.
- **Item 9, T1:54.** "(the PI's item 3 of 2026-11-20)" is now "(the PI's routing of 2026-11-20, second sitting, item
  3, "as ruled this morning": the first sitting's item 4, "[stays up]")". Both sittings' raws were read for it.
- **Item 15, T1:77.** Applied in the checker's words: the steered reads run under the same additive hook, and the
  unsteered ones (the shadows, N4-T and N4-Ts) through the same hook path with no injection placed.
- **Item 20, T1:98.** Applied: "about 10 s of model time at the extension's medians, A-n2:40, beside one load".
  12 × (309.0 + 357.1) + 6 × 309.0 = 9,847.2 ms.
- **Item 29, T1:121.** Applied: no cap, beside the identity, the runner's `hour_cap_ms` None (runner:266; the report's
  `cap.hour_cap_ms`, schema:1209). The block now says the cap is not an identity field and a resume refuses another
  cap (runner:413). With observation 6, Q2 asks the cap as its own clause.
- **Item 33, T1:148.** Applied in the checker's words: the identity is in every cell file and, with its sha256, in
  the report.
- **Item 45, T1:206.** Applied in the checker's words: about 4.9–5.0 GB at the campaign's 7,680 rows, schema:83–85,
  with A-n1:54's 4.7–4.8 GB at 7,360 reads. The build's draft 2 names the figure the same way (`GTIME_NOT_MEASURED`).
- **Item 60, T1:285.** Applied: the projections go to the PI for the cap (ans20b:71; the PI's item 2 of 2026-11-20,
  second sitting, "the projections to me"), and the coordinating session relays them, Code's reading.
- **Item 63, T1:296.** Applied: R:12800 and R:14163, "Stopped for the seat's read.", and the survey's §4.
- **Item 67, T1:319–320.** Applied: "as G-CAL-n's unstarred readings among GC1–GC22 were".
- **Item 68, T1:321.** Applied: "The survey's declared departures (five items)".
- **Item 80, T2:26.** Applied, with §3 added after reading it: "§1 names its one scratch file as S/...; §3 and §4
  name none."
- **Item 83, T3:9–10.** Applied: the readings went to the coordinating session, which put their routing to the PI.
- **O1 (the length count's source).** Met. The block now says the figures, counted over `data/n/ids/sessions.jsonl`,
  are the same as Code's ranking of 2026-11-20 over BK's skeleton files. The ranking's file in Code's scratch was read
  for it: the same counts by length, and the same six lengths.
- **O2 (the comparator's sharing).** Applied. GT10 now states that the comparator's band medians are computed once per
  random point and shared, and what per result would give: 4,464 calls, 44,640 fits, 418,500 in all. Q5 asks which.
- **O3 (one 160-row cell for every cell).** Applied. GT9 states it, why a 40-row cell's appends may cost less, and that
  k = 0 is fitted with the rest. Q4 asks it.
- **O4 (an example builder in a production path).** Applied in the build, not only in the text. Draft 1's benchmark
  called `schema.example_record`, and the schema says of its example builders that "no production path calls them"
  (schema:240–242). Draft 2's benchmark takes the stage's own first +1 read as its template, re-keyed to each session
  in turn (`rekeyed`). That is the campaign's record form, with its re-computation. The block's GT9 says so. The
  example builder stays in the self-test only.
- **O5 (GT5's last sentence).** Met. §2's PAUSE line now says that after the ruling a resume continues and the
  projection is written only at COMPLETE, which is GT5's "A ruling precedes any use of the projections". The two
  forms agree, and neither replaces the other.
- **O6 (the cap in Q2).** Applied with item 29.
- **O7 (§0.4's generations; A1).** Applied: the table counts the negative pole's generations and forwards under the
  PI's option A1 (L:986–987), G-CAL-n's 48 turns at −ρ among them.
- **O8 (Q14 and GT17 met).** Applied in "Where things stand". The notes commit `c9d35e2` holds the paste block and
  quotes items 2 and 3 (R:55–57).
- **O9 (the anchors' offsets).** Applied in the spec raw's head. The five insertions and their offsets were read by
  tool from `git diff -U0 deabf3f c9d35e2 -- RESULTS.md`'s hunk headers.
- **O10 (N4's longer sequences).** Applied: N4's reads add their told line's tokens, G-TIME-n reads no N4 arm, and the
  projection takes the sessions' lengths for N4's 320 reads, a few tokens short (Code's reading).

## 2. The edits, checked by tool

The edits were made to new versioned copies of the three drafts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once. The results are byte for
byte the revised drafts, so nothing else changed after the check:
- the block, 18 of 18 edits; the spec raw's head, 2 of 2; the entry, 6 of 6.

One edit to the entry is not a finding's: its sixth, the departures of Q-F3's folder named plainly in argvs, added
on the coordinating session's note of 2026-11-21. After the edits, two placeholders were filled by tool: the entry's
count of these edits, and this raw's hashes.

## 3. The report, as returned

```text
VALUES-CHECK of T1 (S/step4b/gtime/seat/block_src.md), T2 (S/step4b/gtime/seat/spec_head_src.md and S/step4b/gtime/seat/spec_v1.md) and T3 (S/step4b/gtime/seat/entry_src.md), at HEAD c9d35e2

Hashes first. All ten named files match the brief's sha256s, checked by shasum against the brief's literals: the four texts, pins_gtime.md, routing_gtime.txt, spec_brief.md, brief_scrubbed.md, spec_report.md, and N/2026-11-20_n-build_gtime-pins.md (f3fa5f05…f42f, the same as pins_gtime.md). HEAD is c9d35e2. Every repository file the texts cite is tracked and clean (git rev-parse HEAD:<path> against git hash-object). That covers PROPOSAL-n-bk-reconciliation-v0_2.md, LOCK-n.md, the two addenda, the six cited raws, RESULTS.md, scripts/n_sessions.py, valence_core/n/{schema,runner,primitive,cells,probe,guard}.py, valence_core/echo/probe.py, data/n/ids/sessions.jsonl, data/n/gcal/{gcal,dose_map}.json, data/n/gvec/gvec.json, and results/raw/2026-11-20_n-lock-v0_1_fidsample_out.txt.

Short forms:
- rt:N = S/step4b/gtime/seat/routing_gtime.txt line N (= spec raw §2, spec_v1.md:189–206).
- pins:N = S/step4b/gtime/pins_gtime.md (= §1; pins line = spec_v1 line − 30).
- rep:N = S/step4b/gtime/spec_report.md (= §4; rep line = spec_v1 line − 293).
- R:N = RESULTS.md at c9d35e2.
- Other forms are as T1 defines them.

ITEMS

T1
1. T1:3–4. "The PI's word governs only the nudge to the seat." CONFIRMED. rt:11.
2. T1:7. LOCK-n v0.1 is committed at deabf3f, sha256 88d9fe7b…e9d5, and G-TIME-n (n §8 step 11) runs under it. CONFIRMED. `git show --name-status deabf3f` lists "A LOCK-n.md". shasum of LOCK-n.md gives 88d9fe7b…e9d5, and the file is unchanged since deabf3f. n:159 has step 11. L:740 says "G-TIME-n runs under v0.1".
3. T1:8–9. The drv:182 quotation. CONFIRMED. scripts/n_sessions.py:182 matches verbatim.
4. T1:10–11. The survey was run at deabf3f and returned 17 open questions, and GT1–GT17 answer them. CONFIRMED. rep:1 says "at HEAD deabf3f", and rep:217–235 numbers OPEN QUESTIONS 1–17. The bracket tags in §1 cover Q1–Q17, with GT2 and GT14 untagged.
5. T1:12–13. The PI's answer, "Build on the PINs", was relayed verbatim on 2026-11-21, and the build is in the driver alone (GT3). CONFIRMED. rt:1, rt:3, rt:8.
6. T1:14–15. The starred readings go before the run, not before the build, and 99196e1 went in before 89a55c3. CONFIRMED. rt:9–10. 99196e1 (2026-11-19 07:05, "eleven starred readings for the seat before G-CAL-n's run") is an ancestor of 89a55c3 (09:08, "G-CAL-n's BUILD").
7. T1:19, :22. §1 is f3fa5f05…f42f with 153 lines. §4 is a23831e4…05e7 with 245 lines, compiled at deabf3f. CONFIRMED. Checked by shasum and wc -l, and against rep:1.
8. T1:23–35. The texts and the cited forms exist; R is RESULTS.md at c9d35e2 (HEAD); no code changed since deabf3f. CONFIRMED. `git diff --name-status deabf3f c9d35e2` (item-3 pathspec plus the mf3 exclusion) shows only RESULTS.md modified and two raws added.
9. T1:54. "(the PI's item 3 of 2026-11-20)". IMPRECISE. There were two sittings that day. The PI's second-sitting item 3 (results/raw/2026-11-20_second-sitting_pi-routing.md) says "[as ruled this morning]", restating the first sitting's item 4. Put instead: "(the PI's routing of 2026-11-20, second sitting, item 3, "as ruled this morning": the first sitting's item 4)".
10. T1:55. "Q1–Q7 in §3, one per reading." CONFIRMED. T1:326–347.
11. T1:61–62. The six runs are 0, 32, 64, 95, 127 and 159, which is round(k·159/5); two are floor sessions (0 and 32) and four are neutral. CONFIRMED.
    - Shell arithmetic: k·159/5 = 0, 31.8, 63.6, 95.4, 127.2, 159.
    - In data/n/ids/sessions.jsonl, bk_run follows file order 0..159: floor_b0/0, floor_b6/32, neu_b1/64, neu_b2/95, neu_b4/127, neu_b5/159.
    - schema.bk_cell_of (schema:576–582) puts floor at runs 0–39.
12. T1:63, :89. v0.1 names no G-TIME-n key (L:397–404), and the keys are LOCK-n v0.1's item (n:117). CONFIRMED. The keys table lists n-rand, n-fid, n-n4, n-gcal, n-boot and n-bext only.
13. T1:65–74. Reads (a), (b) and (c), and the kinds: shadow 6, steered 12 (6 cached only), fidelity re-compute 12, capture-on 18. CONFIRMED. Arithmetic, plus schema:1042–1050 and :1071–1082, :1086–1087 (duration_ms_fresh is null exactly without a re-computation) and :88–89.
14. T1:76–77. "Every arm's read is the same forwards: one prefill and two label continuations, and with a re-computation two full forwards." CONFIRMED. primitive:219–221 and :239–240.
15. T1:77. "All of them run under the same additive hook." IMPRECISE. Unsteered reads (the shadows, N4-T and N4-Ts) place no injection: primitive:180–187 leaves spans and `placed` empty unless the read is steered. Put instead: "The steered reads run under the same additive hook; the unsteered ones (the shadows, N4-T and N4-Ts) run through the same hook path with no injection placed."
16. T1:78–80. 144 of the 160 sessions are 1273 tokens and the rest 1266–1272; of the six, five are 1273 and run 127 is 1268, counted over data/n/ids/sessions.jsonl. CONFIRMED. jq histogram: 1266×1, 1267×1, 1268×4, 1269×1, 1270×4, 1271×2, 1272×3, 1273×144. See O1.
17. T1:82–88. The quotations and citations for GT1: n:118, schema:88–89, schema:1042–1050, schema:1071–1082, primitive:213–217. CONFIRMED. Each matches allowing for wrapping.
18. T1:92–93. The plan order is GT2's and the runner's ORDER (runner:18–22). CONFIRMED. runner:18–22 puts shadows first and is arm-major. N1-V's ARM_CELLS order is +1 then +1/2 (schema:303). pins:32–34.
19. T1:94–95. Each record carries its cell, run, seq_len, duration_ms and duration_ms_fresh. CONFIRMED. primitive:264–284: arm, direction_id, dose_label, bk_run, seq_len, duration_ms, duration_ms_fresh.
20. T1:98. "(18 reads, a few minutes of model time on the box at the extension's figures)". IMPRECISE. At A-n2:40's medians, 12 × (309.0 + 357.1) + 6 × 309.0 = 9,847 ms, so about 10 s of model time. Put instead: "(18 reads: about 10 s of model time at the extension's medians, A-n2:40, beside one load)".
21. T1:103. Stage `time`; lock_sha256 88d9fe7b…e9d5. CONFIRMED.
22. T1:104–105. ρ 0.3, R 25.54500811131038, R_ℓ 21.98789170395024, d_eq 0.2869170055735837, d_20 0.5738340111471674, and all seven points kept (L:360–374). CONFIRMED. L:360–374. jq on gcal.json shows dose_map with the same figures and seven points, each with an empty merged list; dose_map.json carries the five figures.
23. T1:105–106. "status PASS (`4c92f228…b8f`)". FAIL: the hash tail is three characters, not the form's four. gcal.json's sha256 is 4c92f228684d…26fdbb8f (shasum; L:377), whose first 8 … last 4 by cut is 4c92f228…bb8f. Status PASS and pinnable true are confirmed by jq. Put instead: "status PASS (`4c92f228…bb8f`)".
24. T1:106. dose_map.json is d4a73b54…efb3, and both files were committed at db00d6d (L:375–379). CONFIRMED. shasum, and `git log` over the two paths shows only db00d6d.
25. T1:107–109. The fidelity rule: TAU; p0 1 of 26; cadence 160; alpha 0.01; C 0.25; median rel 0.0013026706058596332; key n-fid|{s}; sample_rule per L:406–410; identity_bound = C. CONFIRMED. L:486, L:491–494, L:505–511, L:662–664 ("every 160 reads"), L:406–410; schema:860–862.
26. T1:110. Directions {valence: ba4da67fb717b5bb} (L:302–303). CONFIRMED. L:302–303; gvec.json of_record.directions.valence.
27. T1:112–118. Read window 4,096; site 32 and band 33–63; weights 36f05404…0fdb; identifier 8264f719efd347a9 bridged to 4ed3f2c70fe8afbf; pod emw1e4embiwe9b; MANIFEST 53a8cd74…99d8; label convention "space". CONFIRMED. L:456–459, L:295, L:474, L:770–774, L:761–763, L:752–753, L:187–189, L:230–236. The tails were checked by cut.
28. T1:119–120. The package 06b55761…1d39 and its twelve-file closure (L:781–813). CONFIRMED.
29. T1:121. "No cap: `hour_cap_ms` is None", listed as part of the identity. IMPRECISE. hour_cap_ms is not a stage-identity field (STAGE_IDENTITY_FIELDS, schema:448–481). It is the runner's input (runner:266) and the report's cap.hour_cap_ms (schema:1209), and a resume must keep it (runner:413). Put instead: "No cap, beside the identity: the runner's `hour_cap_ms` is None (runner:266; the report's `cap.hour_cap_ms`, schema:1209)."
30. T1:123–131. GT4's texts: ans20b:58; ans19:50 with L:560; L:740–742; schema:448–481, :845–852, :876–878, :507–508; L:554 (the cap row's where is "campaign"); drv:95 ("R5 no cap"). CONFIRMED. Each says what T1 claims.
31. T1:135–142. The facts the run-of-record checks rest on. CONFIRMED.
    - LOCK-n.md's HEAD bytes give 88d9fe7b…e9d5.
    - gcal.json and dose_map.json are clean at their sha256s, and gcal.json is PASS and pinnable.
    - gcal.dose_map exists (gcal.py:400), and L:366–367 records that d_eq is the same double.
    - The valence sha16 is G-VEC's and the lock's.
    - schema.check_stage_identity exists (schema:833).
    - The checks themselves are Code's plan.
32. T1:144. "a cap … would let the stage end early as CAP". CONFIRMED. runner:467–469 and :536–537.
33. T1:148. "the identity's sha256 is in every cell and in the report". IMPRECISE. A cell file carries the identity itself (CELL_FIELDS stage_identity, schema:434), and the report carries the identity with stage_identity_sha256 (schema:1154, :1386–1387). Put instead: "the identity is in every cell file and, with its sha256, in the report".
34. T1:152–154. c = duration_ms − duration_ms_fresh (or duration_ms without a re-computation) and f = duration_ms_fresh; c comes from all 18 reads and f from the 12 re-computed ones. CONFIRMED. schema:1086–1089 (0 ≤ fresh ≤ duration) and the plan's counts.
35. T1:155. N = 7,680. CONFIRMED. L:446, L:464–466.
36. T1:156–161. K = 3,637 = 3,040 + 597, with the parts as given. CONFIRMED.
    - The rule is runner:147.
    - ARM_CELLS is schema:302–311, and N1-R reads the 40 floor sessions only (runner:154).
    - The fidsample raw lists 15 sampled sessions, six of them floor_.
    - Shell arithmetic: 480 + 1,920 + 320 + 320 = 3,040, and 15×11 + 6×72 = 165 + 432 = 597.
37. T1:163–164. runner.campaign_order exists, and the lock's read_plan_sha256 is 7f7d7301…88a6 (L:467). CONFIRMED. runner:140; L:467. How the stage computes K is plan.
38. T1:166–169. The cap counts model time as the runner computes it; the PI sets the cap in hours at v1.0; the extension's figures are 309.0 and 357.1 ms, "used by nothing". CONFIRMED. L:600–601, box:31, A-n2:40.
39. T1:171–180. GT8's texts: n:120, L:591–592, L:600–604, runner:66–70, schema:121–124, primitive:205–207, :237–241 and :283–284, A-n2:40, n:101. CONFIRMED. All quotations are verbatim, allowing for wrapping and markup.
40. T1:182. drv:1157–1160: after COMPLETE, the BACKEND extension's own code reads its records. CONFIRMED. cells.load_cell, then discordance over cell["records"].
41. T1:194. The loads are the report's loads_ms. CONFIRMED. runner:66–70, :548; schema:197–200.
42. T1:196–197. guard.refuse_test_out keeps the output outside the repository. CONFIRMED. guard.py:84–88.
43. T1:201. 138 cells, 18 of 160 rows and 120 of 40, and Σ = 7,680·a + 322,560·b. CONFIRMED. ARM_CELLS plus capture_capacity (schema:540–544). Shell arithmetic: 18·160 + 120·40 = 7,680, and 18·12,720 + 120·780 = 322,560.
44. T1:203–205. The per-read line comes per read, and the cells hold at most six rows. CONFIRMED. runner:511 prints after the append at :503; GT1's plan puts 6 reads in each cell.
45. T1:206. "the captures' copy-back (about 5 GB, A-n1:54)". IMPRECISE. A-n1:54 says "about 4.7–4.8 GB" (over 7,360 reads); schema:83–85 says "about 4.9–5.0 GB at the 7,680 rows". Put instead: "(about 4.9–5.0 GB at the campaign's 7,680 rows, schema:83–85; A-n1:54's 4.7–4.8 GB at 7,360 reads)".
46. T1:206–207. G-VER of record is step 12. CONFIRMED. n:159.
47. T1:212–219. GT9's texts: ans20b:44; R:5921–5922, inside the "n package — BUILD" entry headed at R:5723; rv3:196; cells:200–249 (check_cell at :240–243, atomic JSON at :248); L:587–590; box:31; A-n1:54. CONFIRMED. All quotations are verbatim.
48. T1:223–224. The benchmark cell's form ("the larger record form, so the fit is an upper bound"). NOT CHECKABLE. It is plan and reasoning; the cell's capacity of 160 fits 160 appends.
49. T1:233. "Where they run is Code's call (A-n1:56)." CONFIRMED.
50. T1:236–239. fit_lr at seed 7, 300 iterations, rate 0.1, l2 0.01, and cv_seed 20261116. CONFIRMED. valence_core/echo/probe.py:19; schema:1139; probe.py:49; L:428–430.
51. T1:240. ans16b:42, "About 404,000 fits in all". CONFIRMED.
52. T1:241–243. Six primary results × 31 layers × 201 calls over 320 rows = 37,386 calls, or 373,860 fits. CONFIRMED.
    - GREAD_AXES is schema:1135, and the band of 31 is L:474.
    - probe.py:45–46 and :63–71 set the calls.
    - echo/probe.py:95–114 fits once per fold, so a call is 10 fits.
    - contrast_rows makes two rows per session.
53. T1:244–246. The comparator: 24 directions × 4 points × 31 layers = 2,976 calls over 80 rows, or 29,760 fits. CONFIRMED. schema:280 and :229–231; N1-R is 40 floor sessions. See O2.
54. T1:247–248. 403,620 fits in all, and the projection's form. CONFIRMED. Shell arithmetic.
55. T1:250–258. GT10's texts: L:598, A-n1:56, L:600–604, probe:44–49 (AUC_BAR … CV_SEED), n:121. CONFIRMED.
56. T1:260. probe.contrast_rows exists and groups rows by session. CONFIRMED. probe.py:52–60.
57. T1:271. No read below d = 0; the 12 steered reads are valence at +1 and +1/2. CONFIRMED. Against T1:65–67's plan.
58. T1:272. §0.4's table counts the negative pole's forwards under the PI's option, "struck beyond d = −1". CONFIRMED. n:16–26; the PI's A1 is at L:986. See O7.
59. T1:275–276. n:16–28, and the n:14 quotation for ledger (53). CONFIRMED.
60. T1:285. "The coordinating session relays the projections to the PI for the cap at v1.0 (ans20b:71)." IMPRECISE. ans20b:71, and the PI's own item 2 (results/raw/2026-11-20_second-sitting_pi-routing.md, "the projections to me for the cap at v1.0"), name only the destination, not who relays. Put instead: "The projections go to the PI for the cap at v1.0 (ans20b:71; the PI's item 2 of 2026-11-20, second sitting: "the projections to me"); the coordinating session relays them (Code's reading)."
61. T1:288–290. n:101 has "gate stages may span boxes", and ans20:58 has a new box re-run the characterization and the BACKEND extension first. CONFIRMED.
62. T1:292–295. The ans20b:71 quotation, and n:118, n:120, n:101, ans20:58. CONFIRMED.
63. T1:296. "m's and p's G-TIME stages, which stopped for the seat's read (the survey's §2.7)". IMPRECISE (the citation). The fact holds: R:12800 (G-TIME-OLMo (p) ×3) and R:14163 (G-TIME-F3) both say "Stopped for the seat's read." But the survey states it in its §4 (rep:215), not §2.7, which gives the templates. Put instead: "(R:12800, R:14163: "Stopped for the seat's read."; the survey's §4, rep:215)".
64. T1:303–308. Build on the PINs, driver only, with valence_core/n/ at 06b55761…1d39; self-tests in battery windows, one blind review, one values-check, the commit window; the run after the seat's answers, the BUILD's commit and the launch files' relay. CONFIRMED. rt:6–10, rt:14.
65. T1:311–316. The ends are pre-declared in GT5–GT7: 0 COMPLETE, 3 PAUSE, 2 G-VER-STOP or a refusal before any read, 1 anything else; G-VER's STOP comes before the weights load, with no read and no report. CONFIRMED. pins:51–71. The runner writes the report at a PAUSE (runner:549–552). See O5.
66. T1:318. There is no pass rule: n:118 states no bar, and schema:1131's END_STATES hold no PASS. CONFIRMED.
67. T1:319–320. The ten unstarred readings are Code's, "as G-CAL-n's GC1–GC22 were". IMPRECISE. The count (17 − 7) and the list are right, but seven of GC1–GC22 were starred for the seat (results/raw/2026-11-19_n-gcal_spec.md:79: GC3, GC4, GC5, GC6, GC8, GC11, GC12). Put instead: "are Code's, as G-CAL-n's unstarred readings among GC1–GC22 were".
68. T1:321. "The survey's three departures". IMPRECISE. The report's DEPARTURES section (rep:237–244) declares five items and then "Otherwise none":
    - the `sed -n` prints;
    - shasum;
    - one git grep with ':!data/**';
    - one git grep output saved by the harness;
    - wc -l and cut.
    Counting three classes them, and classing is the seat's. Put instead: "The survey's declared departures (five items) are in the spec raw's §4, the report's last section, for the seat to class."
69. T1:326–347. The figures in Q1–Q7: 18 reads; T = 7,680·median(c) + 3,637·median(f); 138 cells; 403,620 fits; 12 positive-pole reads. CONFIRMED. They match the items above.
70. T1:37, :41–49, and the "As Code will build it" and "Another answer" lines not itemized above. NOT CHECKABLE. These are plan and reasoning.

T2
71. T2 head. spec_head_src.md equals spec_v1.md:1–26 byte for byte. CONFIRMED. shasum of the line range gives 8fc1f2bc…1283.
72. T2:7–9. §1 is as sent: f3fa5f05…f42f, 153 lines; the note is byte for byte Code's scratch copy and sits outside the repository; the text is in no other repository file. CONFIRMED.
    - shasum of N/2026-11-20_n-build_gtime-pins.md equals pins_gtime.md, which equals spec_v1.md:31–183.
    - git grep (item-3 pathspec plus mf3) finds the pins' text in no tracked file. R:61 names the PINs but does not hold their text.
73. T2:10–11. §2 is 64323d4b…50fe, 18 lines, verbatim, and in no other repository file. CONFIRMED. spec_v1.md:189–206 equals routing_gtime.txt; git grep "Build on the PINs" finds no tracked match.
74. T2:12–13. §3 is af5357e7…4aab, 77 lines, with one change on its second line, `<repo>` (2060f18e…c1e8). CONFIRMED. diff spec_brief.md brief_scrubbed.md shows one hunk only (2c2: the full repository path against `<repo>`). spec_v1.md:212–288 equals brief_scrubbed.md.
75. T2:14–17. §4 is a23831e4…05e7, 245 lines, compiled read-only at deabf3f, with its departures in the last section. CONFIRMED. spec_v1.md:294–538 equals spec_report.md; rep:1 and rep:237.
76. T2 as assembled. The four fenced bodies are byte for byte the four S files. CONFIRMED. Line-range shasums equal at :31–183, :189–206, :212–288 and :294–538.
77. T2:16, :22–23. The jq extractions (from the hand-back, and from the transcript, with the wrapper dropped). NOT CHECKABLE. The 18 lines are confirmed, and the departure is declared at T3:40–41.
78. T2:19–20. Every file:line is deabf3f's, and since then only RESULTS.md has changed among the cited files. CONFIRMED. The diff is as in item 8. Spot check: R:2996 at deabf3f, cited at pins:129 and rep:167, is the n_analyze verdicts-path loader line; it is R:3253 at c9d35e2.
79. T2:25–26. No section names a path in the home folder or the scratch folder's full path. CONFIRMED. A grep of spec_v1.md for the home-folder prefix, the private tmp root, the user name, Library and '~/' finds nothing.
80. T2:26. "§4 names scratch files only as S/...." IMPRECISE. §4 names no scratch file; §1 names one, S/step4b/gtime/spec_report.md (spec_v1.md:33). Put instead: "§1 names its one scratch file as S/...; §4 names none."

T3
81. T3:6–7. Committed at deabf3f, sha256 88d9fe7b…e9d5, pushed (origin c9d35e2), and G-TIME-n runs under it. CONFIRMED. `git rev-parse origin/main` gives c9d35e2, whose parent is deabf3f.
82. T3:8. The stage command is not built (scripts/n_sessions.py:182). CONFIRMED.
83. T3:9–10. "Code's readings GT1–GT17 … went to the PI." IMPRECISE. They went to the coordinating session as a note ("for routing"), and it put their routing to the PI (R:61–62; rt:3). Put instead: "went to the coordinating session, which put their routing to the PI".
84. T3:10. "Build on the PINs", relayed verbatim on 2026-11-21. CONFIRMED. rt:1, rt:3.
85. T3:11–13. As G-CAL-n's: 99196e1 before 89a55c3; the block ahead of the BUILD's commit; the PI's word governs only the nudge. CONFIRMED. rt:10–11; git, as in item 6.
86. T3:15–20. The block's §0–§3 as described. CONFIRMED. T1:39–55, 57–299, 311–316, 324–347.
87. T3:21–27. The spec raw's §1–§4 as described, with their hashes. CONFIRMED. Items 72–76.
88. T3:29–30. §3 and §4 were owed; the quotation is "Still owed in your next entry". CONFIRMED. rt:16.
89. T3:31. "nothing ran on a model". NOT CHECKABLE.
90. T3:33–41. The departures of 2026-11-20 and the transcript reads. NOT CHECKABLE.
91. T3:42–44. Each root glob expanded to addenda whose names hold no guard marker. CONFIRMED as far as checkable: the three ADDENDUM-n1/n2/n3 file names (git ls-files, filtered) give 0 hits on bracketed marker patterns.
92. T3:45. The survey's own departures are in the spec raw's §4, the report's last section. CONFIRMED.
93. T3:47–48. The gate's id list. NOT CHECKABLE. The gate script is not among the named files. The three texts hold no agent-id-like or session-id-like string (grep).
94. T3:49–55. Committed by path, the commit-time count of 0, not pushed, the BUILD follows. NOT CHECKABLE. It is future. The three texts hold no home-folder prefix (grep).

TOTALS: 94 items. 74 CONFIRMED, 12 IMPRECISE (items 9, 15, 20, 29, 33, 45, 60, 63, 67, 68, 80, 83), 1 FAIL (item 23), 7 NOT CHECKABLE.

OBSERVATIONS
O1. The source of the length count differs between the texts.
- T1:79–80 attributes the count to data/n/ids/sessions.jsonl.
- T3:35–37 declares a `cd` into BK's skeleton folder "to rank the 160 sessions' seq_len with jq and sort".
- If the count of record came from the skeleton files, T1 should name them, or both. The figures hold over sessions.jsonl.
O2. GT10's 2,976 comparator calls assume one shared set of band medians per point. That is, the 24 random directions' band medians are computed once for each of +1, +1/2, +d_20 and +d_eq, and shared by the results matched to the same point (valence +d_20/+d_eq and span_reward f0.20/f0.10, schema:229–231). Computed per result, it is 6 × 24 × 31 = 4,464 calls (44,640 fits; 418,500 in all), which would not reproduce the seat's "About 404,000". The sharing should be stated as part of Code's reading, and Q5 could ask it.
O3. GT9's one 160-row benchmark cell stands for 120 cells of 40 rows.
- A cell's first append creates its 31 capture arrays at the cell's capacity and fsyncs the folder (cells:190–191, :246–247).
- Every later append maps the whole [capacity, d_model] array (cells:193).
- Q4 does not ask whether that cell stands for the 40-row cells, or whether the k = 0 append is fitted with the rest.
O4. GT9's "160 example records" may conflict with the schema. The schema's example builders are for self-tests, and "no production path calls them" (schema:240–242). If the benchmark, inside the run of record, uses schema.example_record, that sentence is crossed. The block could say what the records are.
O5. §1's GT5 (as sent, pins:59) says "A ruling precedes any use of the projections", while T1:313 says "The report is written and no projection". The block could say that its form replaces GT5's last sentence.
O6. Q2 asks the cap together with the identity, but the cap is not an identity field (item 29). A cap change would not move the identity's sha256, though a resume refuses another cap (runner:413). Q2 could ask the cap as its own clause.
O7. GT12: §0.4's table also counts generations under negative steering (G-CAL-n's 48 turns at −ρ, n:20, n:24), not only forwards. The PI's A1 is on record at L:986 (R:15472 there), which T1 could cite for "the PI's option".
O8. The survey's OPEN QUESTION 14 (rep:232, with rep:214) and §1's GT17 (pins:152–153) are now met at c9d35e2.
- R:55–57 quotes the PI's items 2 and 3 verbatim.
- The paste block is committed as results/raw/2026-11-20_second-sitting_pi-routing.md.
- Neither T1 nor T3 says so, and a seat reading §4 (compiled at deabf3f) sees the question as still open.
O9. RESULTS anchors in §1 and §4 are deabf3f's. c9d35e2 inserted lines in five places (`git diff -U0` hunk headers), so the offset depends on where an anchor falls:
- old lines ≤283 move +204;
- old lines 284–460 move +223;
- old lines 461–739 move +234;
- old lines 740–869 move +249;
- old lines ≥870 move +257 (for example R:5664–5665 becomes R:5921–5922, and R:2996 becomes R:3253).
T2:19–20 says the lines moved; the offsets would help the seat.
O10. N4's reads carry the told line, so their sequences run a few tokens past the session's seq_len (schema:113: "N4's token sequence is its own"). "The choice of sessions does not move the cost" holds for sessions; the arm adds the line's tokens.

DEPARTURES
1. One `awk`, a barred interpreter. It was a numeric filter over grep's line-numbered output of RESULTS.md's entry headings (keeping lines 5700–5930), run to find the entry that holds R:5921–5922. It read nothing but grep's output of a tracked file.
2. `sed`, three times. sed is not on the brief's list; I declare it for classing as a scripting stream editor.
   - a line-range print of RESULTS.md, lines 5917–5925;
   - a substitution over jq's session-id output;
   - a substitution masking the notes folder's path in my own hash-check output.
3. `git log --format='%h %ad'`, which prints author dates; item 1 names commit times. It ran over the two committed files under data/n/gcal/, outside ckpt and reports.
4. For classing, not barred by name:
   - one `git merge-base --is-ancestor 99196e1 89a55c3` (a graph test that prints nothing);
   - `diff` of the two named brief files in S;
   - `git show deabf3f:RESULTS.md` piped to head and tail for one line;
   - `git diff -U0 deabf3f c9d35e2 -- RESULTS.md` filtered to its hunk headers;
   - `wc -l` on named files;
   - shasum ran twice on N/2026-11-20_n-build_gtime-pins.md (the second time inside the all-files comparison), and nothing else in that folder was touched.
Otherwise none:
- no guard marker reached any argv (the one marker search used bracketed patterns);
- nothing under data/mf3, a ckpt or a reports folder was listed, read, sized or timed;
- in S, only the named files were read, with no listing or glob;
- no whole-tree git status was run, and no file was written.
```
