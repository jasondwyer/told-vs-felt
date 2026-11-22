# n — the seat's block on G-VER's seven starred readings: the blind values-check, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three drafts, at HEAD `cd6b30d`:
- T1, the block, sha256 `b3ade195…95d7` (269 lines);
- T2, the head of G-VER's spec raw, `952f1730…cb9e` (40 lines), and the raw built from it, `28a6a2ac…9ccd` (584
  lines): the head's claims, and each fenced section against its source;
- T3, this commit's entry, `9cbc6a11…4a07` (89 lines), its values-check and checker's-departures lines placeholders
  not to be checked.

**The checker's brief** was given to the checker as its prompt: Code's scratch file `S/step4b/gver/seat/vc_brief.md`
(`606a4ad0…cf9f`, 110 lines). It:
- named the texts and the sources. In the repository, the files the texts cite, at `cd6b30d`, each checked tracked and
  clean. In Code's scratch, by name and sha256 only: the readings and the addendum as sent, the routing, the survey's
  brief in both forms, and its report;
- allowed `shasum` by name; `jq` on committed JSON outside `data/*/ckpt`, `data/*/reports` and `data/m[f]3`; and `jq`
  on this session's transcript, for a sweep of Code's shell commands from `7d01b02`'s commit window to the brief's own
  hash. It barred any other interpreter (`awk` among them), any write, any network, any guard marker in an argv (a
  grep pattern and the command's own text included), and globs over the root, `results/raw/` or a folder of
  marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file, and anything in
  Code's scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim, and required item 3's pathspec and the campaign folder's
  exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (178 lines, sha256
`9657e8a3…0e39`). It names scratch files only by their paths inside the scratch folder, and the transcript as T. Its
times are T's UTC stamps, Code's own, which the brief asked for.

**Totals:** 114 items: 91 CONFIRMED, 9 IMPRECISE, 4 FAIL, 10 NOT CHECKABLE; and 12 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or the words below. Every observation is
applied or met. §2 gives the edits and their check by tool.

- **Item 23 (FAIL), T1:76–77.** Applied. The BACKEND extension's PASS was under the (i)–(iv) pin, before `516b60f`
  (R:6419); G-TIME-n's is at the current package, ids and pin; G-VEC and G-CAL-n run no G-VER. The block names the
  verifier's call sites more narrowly than the checker's wording: `verify.verify` at drv:438 (gver-trial) and
  drv:1073 (`_gver_tokenizer`, the two stages' G-VER at drv:1192 and :4292). The spec raw's head notes §1's claim.
- **Item 102 (FAIL), T3:47–48.** Applied: two closed paths (the report and the shadow cell), named by the verify run's
  `git show --name-status`.
- **Item 109 (FAIL), T3:41–42.** Applied: the kinds the sweep found missing are listed, as the checker suggested, in
  the survey's return, this block's line and one "throughout" line. The entry's departures end with a final sweep of
  the commands after the checker's window (observation 9).
- **Item 111 (FAIL), T3:76–77.** Applied in the checker's words.
- **Item 14, T1:52–54.** Applied in the checker's words.
- **Item 16, T1:57.** Applied: "as the routing names them", with GV13's re-run list named as open too.
- **Item 17, T1:58–59, :172 and :265.** Applied: "As GV5 pins it" in each place, and in §2's third end.
- **Item 26, T1:81–82.** Applied with observation 5: `verify` checks the pin, but its report carries neither the
  sha256 nor `pin_ok`, and a failed pin shows only as a problem line; the stages record the sha256 as their identity's
  `rendering_id`; what (c) adds is the comparison with the pin, in a G-VER record.
- **Item 51, T1:169–170.** Applied in the checker's words. The spec raw's head notes §1's citation.
- **Item 83, T2:30.** Applied: the head now notes four citations and one claim, observation 12's among them.
- **Items 93, 94 and 99, T3.** Applied in the checker's words, item 94's with GV4's correction beside it.
- **O1.** Applied: GV1's texts cite rt21b:30, the second sitting's [go].
- **O2.** Applied: GV9 sets G-TIME-n's GT6 (a refusal before any read shared exit 2 with G-VER's STOP, accepted at
  ans21b:38) beside ans21b:39, and Q4 asks whether a tokenizer file off its pin is a respawn INTEGRITY incident.
- **O3.** Applied: GV4's "Not held" names the rest of G-TIME-n's preparation and the benchmark folder's checks.
- **O4.** Applied: GV4 names `vocab.json` and `merges.txt`, and Q2 asks whether GV3's hash check should cover every
  file the load may read.
- **O5.** Applied with item 26.
- **O6.** Applied: "GV6 (what a STOP at step 12 means for step 13 and the campaign)".
- **O7.** Applied: the spec raw's head and the entry describe §3's extraction alike: `sed -n` of the message's record,
  through `jq` for its content, then `sed -n` of the content's lines 3–28.
- **O8.** Applied: drv:4249–4251 beside drv:1156–1158, and guard:4–5 beside guard:31–32.
- **O9.** Met: the entry's departures end with a final sweep, made just before this commit's window request.
- **O10.** Applied: one "throughout" line names the writes in scratch, beside `7d01b02`'s window's index and commit
  writes.
- **O11.** Met: the times are Code's own transcript stamps, which the brief asked for. They are kept verbatim, as in
  `91f0d35`'s second values-check raw (`results/raw/2026-11-21_n-gtime-build_valuescheck2.md`), and no PI date is
  computed from them.
- **O12.** Applied in the spec raw's head, with item 83.

**Beside the checker's items, two edits of Code's own,** found while drafting the BUILD:
- **GV4's correction.** L:543 names "the manifest's pin" among G-VER's own causes, so the block reads a MANIFEST.json
  off its pin as G-VER's STOP, with the record, and not as a refusal. §0, GV4, GV9, §2 and Q2 say so, and the spec
  raw's head names it.
- **GV9's refusal list** gains an ids file off MANIFEST.json's sha256 or record count (`ids.load`) and a session set
  that is not BK's (`sessions.load_sessions`).

## 2. The edits, checked by tool

The edits were made to new versioned copies of the three drafts. Each was recovered from this session's transcript by
`jq` and replayed on the draft the checker read, each change's old text found exactly once, by the replay script
`S/step4b/gver/seat/edits_check.sh`. The results are byte for byte the revised drafts, so nothing else changed after
the check:
- the block, 9 of 9 edits; the spec raw's head, 1 of 1; the entry, 8 of 8.

The entry's eight include its two placeholders, filled with this check's summary and the checker's departures, and
its departures' final sweep of the commands after the checker's window (observation 9). After the edits, one
placeholder was filled by tool: the entry's count of these edits.

## 3. The report, as returned

```text
VALUES-CHECK REPORT: T1 (S/step4b/gver/seat/block_src.md), T2 (S/step4b/gver/seat/spec_head_src.md and S/step4b/gver/seat/spec_v1.md), T3 (S/step4b/gver/seat/entry_src.md), at HEAD cd6b30d

Inputs. All ten named S files hash to the sha256s in the brief. Line counts are as stated: T1 269, T2 head 40, T2 assembled 584, T3 89 (and 136 / 46 / 26 / 79 / 79 / 232 for the five sources). Every cited repository file is tracked and clean at cd6b30d (`git rev-parse HEAD:<path>` = `git hash-object <path>`): the three n texts, LOCK-m-F3.md, CLAUDE.md, RESULTS.md, .gitignore, the driver, the analyzer, verify/ids/schema/guard, and the seven cited raws. Every hash abbreviation in the three texts matches its full value cut by tool (first 8 … last 4).

ITEMS

T1 (the block)
1. T1:3–4: PI date 2026-11-22; before the run at n §8 step 12; "The PI's word governs only the nudge to the seat." CONFIRMED. n:159; S/step4b/gver/seat/routing_gver.txt:17.
2. T1:7: LOCK-n v0.1 at `deabf3f`, sha256 `88d9fe7b…e9d5`. CONFIRMED. `git show deabf3f:LOCK-n.md | shasum -a 256` equals HEAD's. deabf3f adds LOCK-n.md, and no later commit touches it.
3. T1:7–8: G-TIME-n ran under v0.1, COMPLETE (`7d01b02`). CONFIRMED. 7d01b02's subject; drv:4240.
4. T1:8: the record was accepted at the third sitting (ans21c:15). CONFIRMED. ans21c:15 "Accepted as the run of record."; rt21c:17.
5. T1:8–9: a cap of 4 h of model time (rt21c:21). CONFIRMED.
6. T1:10–12: "the BUILD's site-check trial, never of record" (drv:16–20); drv:239's sentence; "likewise L:997–998". CONFIRMED. drv:19; drv:239; L:997–998.
7. T1:13–14: the survey at 7d01b02 returned 13 open questions; GV1–GV16 answer them as PINs; the addendum changes no PIN. CONFIRMED. The survey report's OPEN QUESTIONS 1–13; §1's header; §2's title.
8. T1:15–16: "Build on the PINs", relayed verbatim on 2026-11-22; the build is in the driver alone. CONFIRMED. routing_gver.txt:1, :3, :13; T's record at line 60268 is stamped 2026-11-22T14:51:16Z.
9. T1:17–18: `2ca24e8` (the block) before `91f0d35` (the BUILD). CONFIRMED. Commit times 2026-11-21 03:47:59 and 06:36:37 −0500. 2ca24e8 adds G-TIME-n's starred-seven STOP block and spec raw.
10. T1:19–21: N.3's quote (rt21c:22–23); C.7 (rt21c:39); the read list at ans21c:3. CONFIRMED.
11. T1:24–31: the sources are §1 `d73c2b8e…976e`/136, §2 `775ad17d…be51`/46, §5 `3a40ac89…8989`/232 compiled at 7d01b02, and the three texts' file names. CONFIRMED.
12. T1:34–40: the seven cited raws. CONFIRMED. Each is tracked and clean.
13. T1:41–44: R is at cd6b30d; no code has changed since 7d01b02; the driver's last change is 91f0d35. CONFIRMED. `git diff --name-status 7d01b02 cd6b30d` with item 3's pathspec lists .gitignore, RESULTS.md and three raws. `git log -- scripts/n_sessions.py` gives 91f0d35.
14. T1:52–54: "After the run, a change to any of them means running it again. That costs minutes of pod time". IMPRECISE. T1's own lines disagree: GV1 (T1:101) says that after a run, "not a step" leaves "the record as one more check"; GV9 (T1:195–196) allows re-deriving from the raw. §1's GV12 says "Seconds to minutes". Instead: "After the run, other pins (GV4) mean running it again; another record form (GV9) means running it again or re-deriving the field from the raw; and "not a step" (GV1) leaves the record as one more check. A re-run costs seconds to minutes of pod time: one tokenizer load and the decode (GV12)."
15. T1:55–56: the other four change no code and no read; GV6 binds only on a STOP. CONFIRMED. T1:151, :207, :219, :231.
16. T1:57: "The addendum's open points are in GV9 and GV11". IMPRECISE. The addendum's "Left open" section also has GV13 ("the list of what re-runs on a box change stays the seat's"), which T1:213–214 carries. The routing (routing_gver.txt:16) names only the two. Instead: "The addendum's open points, as the routing names them, are in GV9 and GV11 (it also leaves GV13's re-run list open, carried in GV13):".
17. T1:58–59, T1:172 and T1:265: "As built, a refusal before G-VER exits 1 and writes no record", "As built:", "as built". IMPRECISE. No G-VER command exists yet (drv:239; T1:10); the exits are GV5's PIN. Instead: "As GV5 pins it (not yet built), a refusal…" at :58; "As GV5 pins it:" at :172; "…with no record, as GV5 pins it." at :265.
18. T1:62–64: the wait is the coordinating session's reading, put to the PI; the quote is from ans21c's short form (:11); ans21c:3. CONFIRMED. routing_gver.txt:18; ans21c:5 (§0), :11, :3.
19. T1:65–67: the BUILD's commit; the relay; "[stays up]" (rt21c:39). CONFIRMED. routing_gver.txt:21.
20. T1:68 and T1:256–269: Q1–Q7, one per reading. CONFIRMED.
21. T1:72, :103, :139, :153, :198, :209, :221: the survey's question numbers 1, 3, 6, 4, 10, 12, 13. CONFIRMED. These match §1's bracketed Q numbers and the survey's OPEN QUESTIONS.
22. T1:74–75 and T1:96–101: the run as Code will build it; the other answers. NOT CHECKABLE (plan). "Its entry is "G-VER (n)"" matches n:161.
23. T1:76–77: "(the BACKEND extension's and G-TIME-n's, PASS at the current package, ids and pin)". FAIL. The BACKEND extension's G-VER ran before `516b60f` moved the pin. At its out raw's commit `9f64305`, ids.py has MANIFEST_OF_RECORD `fdf73d85…ef38`, the (i)–(iv) value (R:6419: "now (i)–(iv)"), and the package predates `ef105f1`'s `06b55761…1d39` (L:815–817). Only G-TIME-n's PASS is at the current package, ids and pin. "each stage" also overreaches: G-VEC and G-CAL-n run no G-VER (the driver calls the verifier only at drv:438, :1192 and :4292). Instead: "**What it adds** to the G-VERs the BACKEND extension and G-TIME-n run before their loads (the extension's PASS under the (i)–(iv) pin, before `516b60f`; G-TIME-n's at the current package, ids and pin):".
24. T1:78, (a): the stages' G-VER lines exist only in their raws. CONFIRMED. drv:1193–1194 and :4293–4294 print the JSON to stdout. The stage report has no G-VER record (schema:14–18), and G-TIME-n's artifact code names none.
25. T1:79–80, (b): the folder is checked by byte counts alone (drv:636–649). CONFIRMED.
26. T1:81–82, (c): "`verify` checks the pin but does not report it (verify:86–89)". IMPRECISE. verify:86–89 is the check, and a failed pin does appear, as a problem line (:87–89). What the report lacks is `pin_ok` and the sha256 (verify:142–144). Instead: "`verify` checks the pin (verify:86–89), but its report carries neither the sha256 nor `pin_ok` (verify:142–144); a failed pin shows only as a problem line".
27. T1:84–86: the m ruling, "G-VER is the verifier, not a step" (mF3ans:1) and "it has no entry of its own" (mF3ans:10). CONFIRMED.
28. T1:88–89: n:159 and n:161 quotes. CONFIRMED.
29. T1:90–91: "G-VER (n)" in GATE_STAGES (n_analyze:129); `clock:gate-stopped` (n_analyze:121–122). CONFIRMED. n_analyze:1041–1043 requires that cause's stage to be in GATE_STAGES.
30. T1:92: drv:216's GT7 quote, accepted at ans21b:38. CONFIRMED.
31. T1:93–95: rt21c:22–23's quote; mF3ans:1 and :10. CONFIRMED.
32. T1:104–105: G-TIME-n's preparation checks are at drv:4224–4290. CONFIRMED.
33. T1:106: `CHARACTERIZED_POD` is `emw1e4embiwe9b`. CONFIRMED. drv:578, :4227–4229.
34. T1:107–108: the weights folder; `36f05404…0fdb` (L §17); the tokenizer is read from that folder. CONFIRMED. drv:636–649, :3775, :4242–4246; L:773; drv:4292 → :1072.
35. T1:109: the driver of record (drv:1156–1158). CONFIRMED. G-TIME-n's own copy is drv:4249–4251 ("the driver of record as backend-ext's", drv:192).
36. T1:110: `ids.MANIFEST_OF_RECORD` is `53a8cd74…99d8` (L:187–189). CONFIRMED. ids:86; drv:4256–4257; L:188–189.
37. T1:111: LOCK-n.md is held at the lock's sha256. CONFIRMED. drv:3768, :3844, :3861–3862, called at :4258.
38. T1:112–113: the package `06b55761…1d39` and its twelve files (L §18); "`verify.py` is in the package (guard:31–32)". CONFIRMED. drv:3776–3777, :4271–4275; L:781, :802–813; guard:31–32.
39. T1:114–116: the R6 bridge to `4ed3f2c70fe8afbf`; the backend identifier `8264f719efd347a9` (L §17). CONFIRMED. drv:586, :3774, :4264–4270; L:753, :762–763.
40. T1:118–119: `ids.TOKENIZER_FILES`, `ids.pinned_tokenizer_sha256s`, L:196–203. CONFIRMED for the existing names and pins: ids:69, :117–119; L:201–203 equal the model manifest's three (data/olmo/manifest.json:251–262). The check itself is plan.
41. T1:121–123: cuBLAS and the stream's known answer are G-TIME-n checks (drv:4230–4234); `schema.STAGES` (schema:256); a schema stage would move L §18's pin. CONFIRMED. schema.py is inside the package hash's domain (guard:4–5; L:781–784).
42. T1:125–130: L:3–4; ans20b:57; A-n1:28; L:187–189 and :196–203; L:746–774 (§17) and L:781–813 (§18's package and closure); schema:17–18. CONFIRMED.
43. T1:131–137: plan and the other answers. NOT CHECKABLE.
44. T1:140–141: L:543's quote. CONFIRMED.
45. T1:142, :145, :149–151: Code's reading and plan. NOT CHECKABLE.
46. T1:143–144: D_n is 2026-12-15 (L:985); NOT-RUN under n:134; `clock:gate-stopped`; stage "G-VER (n)". CONFIRMED.
47. T1:146–147: "after G-VER's PASS" (rt21c:24; ans21c:72). CONFIRMED.
48. T1:148: L:543; ans20b:41; n:134's quote; L:985. CONFIRMED.
49. T1:154–166: what the record holds of verify (nine keys, `first_problems` masked as verify masks them, no token id). CONFIRMED. verify:142–144, :66–67, :104, :124, :26. The rest of the record's form is plan.
50. T1:167–168: the .gitignore lines, "as G-TIME-n's did". CONFIRMED. `git diff -U0 4fdcdcc 91f0d35 -- .gitignore` adds G-TIME-n's block.
51. T1:169–170: "the schema's report is for stages that read (schema:187–193)". IMPRECISE. schema:187–193 says that a G-VER-STOP's report "holds no record and no pause". The report's scope is set at schema:14–18 and :152–156. Instead: "**No stage report:** the schema's stage report is for the three stages that write read records (schema:14–18, :152–156; `STAGES`, schema:256), and G-VER of record reads nothing."
52. T1:171–172: N.3's quote. CONFIRMED.
53. T1:178–181: ans21b:39's quote; respawn step (i). CONFIRMED. The instruct entry's folder is under /workspace/models/ (data/olmo/manifest.json:176), the tree that CLAUDE.md's step (i) re-hashes.
54. T1:183–184: schema:1197; schema:187–193 (the quote is at :192–193). CONFIRMED.
55. T1:185–186: drv:58–59's reading, flagged and unruled (R:6452–6455). CONFIRMED. R:6452 reads "still flagged for the seat", and R:6455 is the reading. `git grep` of the reading's words at cd6b30d finds only the driver, that entry and two earlier review/check raws, with no ruling.
56. T1:187: `n-gtime-v1` is the driver's own form (GT11). CONFIRMED. drv:223, :3748; it is not in schema.py.
57. T1:188–196, :199–200, :206–207: plan, Code's reading and the other answers. NOT CHECKABLE.
58. T1:201 and :204: N.4's list is n:120's (rt21c:24–29) and names no G-VER record. CONFIRMED. rt21c:25 "carrying n:120's list", with the items at :26–29.
59. T1:203: n:120's quote. CONFIRMED.
60. T1:205: LOCK-m-F3.md:273's quote; that file is m's v1.0. CONFIRMED. LOCK-m-F3.md:1.
61. T1:210–213: ans21b:27; box:31; C.7 (rt21c:39). CONFIRMED.
62. T1:215: ans21b:27; n:101's quote; box:31; CLAUDE.md's respawn protocol. CONFIRMED.
63. T1:217–219: one pod pin serves every stage. CONFIRMED for the existing driver: CHARACTERIZED_POD (drv:578) is checked at :1135 and :4227. The exit 1 is plan.
64. T1:222–223 and :230–231. NOT CHECKABLE.
65. T1:225–229: ans21c:62's quote; rt21c:29's quote; neither says that G-VER's read comes before step 13's commit; ans21b:59. CONFIRMED.
66. T1:235–238: "Build on the PINs"; the build is in the driver alone, so the package stays at `06b55761…1d39`; the build's form. CONFIRMED. routing_gver.txt:1, :11–13; `git diff --name-only ef105f1 cd6b30d -- valence_core/n` is empty; L:781.
67. T1:239–242: the run waits for the seat's answers, the BUILD's commit and the relay. CONFIRMED. routing_gver.txt:18 ("Unless the PI says otherwise"; T1:62 carries that qualifier) and :21.
68. T1:243–246: the ends, pre-declared. NOT CHECKABLE (plan).
69. T1:248: the pass rule at verify:140–141. CONFIRMED.
70. T1:249–250: the nine unstarred readings; "as G-TIME-n's unstarred readings among GT1–GT17 were". CONFIRMED. §1 stars GV1, GV4, GV6, GV9, GV11, GV13 and GV14. 2ca24e8's subject stars GT1, GT4, GT8, GT9, GT10, GT12 and GT16.
71. T1:251–252: the survey's eight departures are in §5's last section. CONFIRMED.

T2 (the spec raw)
72. Assembly: the head is spec_head_src.md (lines 1–40), and the five fenced bodies (45–180, 186–231, 237–262, 268–346, 352–583) are byte for byte gv_readings_v1.md, gv_readings_v1_add1.md, routing_gver.txt, brief_scrubbed.md and survey_report_v1.md. CONFIRMED. `head | tail | shasum` of each range equals the named file's sha256.
73. T2:14–15 (§4): one change, on line 2. CONFIRMED. `diff` prints `2c2` only.
74. §3 is lines 3–28 of the content of T's record at line 60268. CONFIRMED. It is a "user" record whose string content has 31 lines; lines 3–28 hash to `503e7a99…e748`. Lines 1–2 are the wrapper naming the sender by session id; lines 29–31 are the closing tag and the harness note.
75. T2:7–9: §1 is 136 lines, sent by path and sha256, re-hashed equal, and in no other repository file. CONFIRMED. routing_gver.txt:11; `git grep -c -F` of two of §1's lines at cd6b30d (item 3's pathspec) finds 0 files.
76. T2:10–11: the same claims for §2. CONFIRMED (0 files).
77. T2:12–13: §3 is 26 lines and in no other repository file. CONFIRMED. Its first line is in 0 files. Its last line also ends results/raw/2026-11-21_n-gtime_spec.md:208, which is a different message.
78. T2:14–16: §4 is 79 lines, `8e39c8d7…c9a1` → `a4d46c63…4b9e`; §5 is 232 lines. CONFIRMED.
79. T2:16–19: §5 was compiled read-only at 7d01b02 and extracted by `jq` on 2026-11-21. CONFIRMED. The report's title line; the extraction ran at 03:18:04Z on 2026-11-22 UTC, which is PI date 2026-11-21 (−0500).
80. T2:21–23: §2's raw was untracked at 7d01b02 and is committed unchanged at cd6b30d; only RESULTS.md and .gitignore changed among the cited files. CONFIRMED. cd6b30d adds that raw at c9b1ee42…1f36, 82 lines, 20,564 bytes, the addendum's figures.
81. T2:24–26: 331 lines in three places; shifts of +304, +320 and +331; R:6121–6124 → R:6452–6455. CONFIRMED. The hunks are `-23,0 +24,304`, `-313,0 +618,16` and `-536,0 +857,11`; numstat is 331/0; spot checks of shifted lines match by hash.
82. T2:27–28: .gitignore gains one line after 172 (`.pytest_cache/`); :262–343 → :263–344. CONFIRMED. The hunk is `-172,0 +173`; spot checks match.
83. T2:30: "Two citations in §1, as sent, are imprecise." IMPRECISE. There is a third: GV9's "(schema.py:187–193)", the source of item 51, which T1 carries. §1's GV1 also has a slip that is not a citation (item 23). Instead: "**Three citations in §1, as sent, are imprecise, and one claim.**", adding: "- GV9's "(schema.py:187–193)": those lines say a G-VER-STOP's report holds no record and no pause; the stage report's scope is schema.py:14–18 and :152–156. - GV1's "(the BACKEND extension's and G-TIME-n's, PASS at the current package, ids and pin)": the extension's PASS was under the (i)–(iv) pin (R:6419)."
84. T2:31–32: the first note. CONFIRMED. mF3ans:1 is the title; :10 holds the second phrase.
85. T2:33–34: the second note. CONFIRMED. n:130 says stdout is "never a margin" and names no token id; T1:165 rests the claim on verify's report alone.
86. T2:36–37: §3 was taken by jq; it is the message's own 26 lines without the wrapper, which names a session by id. CONFIRMED (see observation 7).
87. T2:39–40: no home-folder path and no full scratch path. CONFIRMED. Counts in all three texts are 0 for the home prefix, "/private/", the scratch root's name and the session id.

T3 (the entry)
88. T3:1–4: the heading and the block's path. CONFIRMED. It is T1's destination and follows WORKFLOW.md:17's form.
89. T3:6–8: `deabf3f`, `88d9fe7b…e9d5`; COMPLETE (`7d01b02`, pushed); the cap is 4 h (cd6b30d). CONFIRMED. origin/main is 7d01b02.
90. T3:9–10: no stage command; drv:239's sentence. CONFIRMED.
91. T3:11–13: the readings and addendum went to the coordinating session; "Build on the PINs" was relayed on 2026-11-22. CONFIRMED.
92. T3:14–17: why now; the PI's word governs only the nudge; the run's wait. CONFIRMED. routing_gver.txt:14–18.
93. T3:19–20: "a change to any of them after it means running it again". IMPRECISE (as item 14). Instead: "§0, the short form. GV1, GV4 and GV9 shape the run: after it, other pins (GV4) mean running it again, another record form (GV9) running it again or re-deriving from the raw, and GV1's "not a step" leaves the record as one more check; the other four change no code and no read;"
94. T3:21–23: "The addendum's open points are in GV9 (with GV5: as built, …) and in GV11". IMPRECISE (as items 16 and 17). Instead: "…are in GV9 (with GV5: as GV5 pins it, a refusal before G-VER exits 1 with no record, against N.3's "…") and in GV11 (N.4's list names no G-VER record); GV13's re-run list stays open too;"
95. T3:24–26: §2's ends; §3's Q1–Q7. CONFIRMED. T1:243–246, :256–269.
96. T3:27–34: the spec raw's five sections and their hashes. CONFIRMED (item 72).
97. T3:36–37: the head gives the line shifts and two notes, which the block cites correctly. CONFIRMED. T1:84–85 and :165. (The head undercounts the notes: item 83.)
98. T3:38: "nothing ran on a model". CONFIRMED. None of the window's 62 shell commands runs python, pytest or a driver stage.
99. T3:43: "the kit's place, gate, commit and verify scripts". IMPRECISE. The commit was `git add` (02:49:15Z) and `git commit` (02:49:36Z) by the paths file, not a script, and a fourth script ran: the commit-message check (02:49:31Z). Instead: "the kit's place, gate and verify scripts and the commit-message check, with `git add` and `git commit` by the paths file, in the forms…".
100. T3:43–47: the forms the scripts ran. NOT CHECKABLE: the scripts are not among the files this check may read. What is visible is consistent. The verify run printed two name-status lists, one under item 3's exclusions and one naming the two closed paths. R:559–570 and :611–612 (the entry of 7d01b02) declare the verify's and the gate's forms.
101. T3:45–46: "per manifest path, none marker-named". CONFIRMED. 7d01b02's 17 open paths give a bracketed guard-word count of 0. The two closed names, as 7d01b02's message gives them, hold none.
102. T3:47–48: "The three closed paths were checked by digest and staged blob id, never read". FAIL. There are two. 7d01b02's message says "checks the two closed paths"; R:611 names "the report and the shadow cell"; the verify run lists two. Instead: "The two closed paths (the report and the shadow cell) were checked by digest and staged blob id, never read, and named by the verify run's `git show --name-status`;"
103. T3:48: "no package digest was wanted". NOT CHECKABLE. The last argument "none" to the gate (02:49:23Z) and the verify (02:49:44Z) is consistent with it.
104. T3:49–50: the commands after the window (02:50:08Z). CONFIRMED.
105. T3:51–55: the survey's brief (02:51:34Z–02:53:28Z). CONFIRMED.
106. T3:56: the survey's return (03:18:04Z). CONFIRMED as far as it goes; it is incomplete (item 109).
107. T3:57–65: the readings (03:18:05Z–03:20:21Z), the addendum (05:54:22Z–05:59:10Z), the citation check (06:51:17Z–06:51:34Z). CONFIRMED. The attribution "observation 3" is NOT CHECKABLE.
108. T3:66–74: this block (14:52:36Z–15:03:43Z). CONFIRMED for every form it names: four transcript lines through jq for their record types; one line through jq for §3; eleven commands printed (seven in full, one with the campaign name masked, three by their last arguments); one marker count by bracketed patterns.
109. T3:41–42: that the list names every kind outside item 1 ("Code knows of no others"). FAIL. Several kinds are missing (under THE SWEEP below). Instead: add the lines given there.
110. T3:76: no guard marker and no plain campaign name in any argv. CONFIRMED. Over the 62 commands: [0] markers, [0] plain campaign names.
111. T3:76–77: "Nothing under a ckpt or reports folder or Q-F3's folder was read, listed, sized or timed". FAIL. Two committed names, one under data/n/ckpt/ and one under data/n/reports/, were printed twice: by the verify run (02:49:44Z) and by `git show --name-status` of five commits with no pathspec (14:52:06Z). Both were names only (item 1's form); I viewed them with digits masked. Instead: "Nothing under a ckpt or reports folder or Q-F3's folder was read, sized or timed; two committed names under them (`7d01b02`'s shadow cell and report) were printed, names only, by the verify run in `7d01b02`'s window and by a `git show --name-status` of five commits;"
112. T3:78: the survey's departures are eight numbered items. CONFIRMED.
113. T3:80–81: the gate's id list. NOT CHECKABLE.
114. T3:82–88: committed by path, a home-prefix count of 0, not pushed, the BUILD next. NOT CHECKABLE (plan). The three texts currently hold no home-folder prefix (count 0).

THE SWEEP
The window runs from 02:49:00Z to 15:07:32Z on 2026-11-22 (T's UTC stamps), ending at the command that hashes this brief; it holds 62 Bash calls. Bracketed counts over their text: guard markers [0], the campaign folder's plain name [0]. No interpreter and no model ran.

Outside item 1's forms and not covered by T3's list:
- 02:49:31Z: `bash` of the commit-message check script in scratch. (T3's "commit … script" was in fact `git add` at 02:49:15Z and `git commit` at 02:49:36Z, by the paths file.)
- 02:54:21Z and 02:54:34Z: `wc -l` of the survey's brief in scratch.
- 03:18:04Z, beside the subagent-transcript `jq`: `jq` over this session's transcript for the report as delivered; `sed -n` (a range) and `sed` (a de-indent) over its output; `cmp` of the two scratch files; `wc -l` of the saved report.
- 05:58:51Z: `wc -l` of the addendum in scratch.
- 14:55:02Z, 14:55:15Z and 14:55:25Z: `wc -l` of the routing extract, of its 26-line take, and of the scrubbed brief. Also at 14:55:15Z, `sed -n '3,28p'` over the scratch extract.
- 15:04:16Z and 15:04:33Z: `zsh` running a scratch script that assembles the spec raw. At 15:04:33Z, `rm` of the first assembly.
- 15:04:33Z, 15:05:56Z, 15:06:16Z, 15:06:29Z and 15:07:32Z: `wc -l` of the block, the head, the assembled raw, the entry and this brief.
- 15:06:16Z: `tail -c 2` into `od -c` over the entry draft.
- 15:07:32Z: `head -c 300` of a scratch file (G-TIME-n's earlier values-check prompt).

In item 1's forms but with no pathspec, the class the entry of 7d01b02 declared as departures; not declared here:
- 14:52:06Z: `git show --name-status` of five commits. It printed the two closed names.
- 14:55:52Z: `git diff --name-only 7d01b02 cd6b30d`. No closed name was printed.
- 15:01:30Z: `git log -1 --format='%h %cI'` of three commits.

Suggested additions to T3's list:
- the survey's return: "…and `jq` over this session's transcript for the report as delivered, through `sed -n` and a `sed` de-indent, compared by `cmp` (equal)";
- this block: "`git show --name-status` of five commits, `git diff --name-only 7d01b02 cd6b30d` and `git log -1 --format` of three commits, each with no pathspec (the first printed two committed names under a ckpt and a reports folder); `sed -n` of lines 3–28 of the routing extract; `zsh` running the spec raw's assembly script in scratch, twice, with one `rm` of its first output; `tail -c 2` into `od -c` over the entry draft; `head -c` of a scratch file";
- once, for the whole list: "`wc -l` of scratch files (the brief, the addendum, the routing extracts, the scrubbed brief, the three texts and this check's brief)".

TOTALS (114 items): CONFIRMED 91, IMPRECISE 9, FAIL 4, NOT CHECKABLE 10.

OBSERVATIONS
1. T1:37 defines rt21b:, but no line of T1 cites it. Drop it, or cite rt21b:30 where GV1 rests on the second sitting's [go], as §1 does.
2. For Q4, a missing precedent. At G-TIME-n, a refusal before any read shared exit 2 with G-VER's STOP (drv:203–205 and :4342–4348; GT6, accepted at ans21b:38). §1's GV5 says so, but T1's GV9 quotes only ans21b:39. Q4 would be easier to rule with both in view. Q4 could also ask outright whether a tokenizer file off its pin is handled as a respawn INTEGRITY incident.
3. For Q2, an incomplete drop list. GV4's "Not held" names two of G-TIME-n's checks. Others in drv:4224–4290 are neither held nor named: the rulings files (:4235–4237); G-VEC's record and G-CAL-n's record and dose map (`gtime_lock_inputs`, drv:3863–3871, whose LOCK-n.md part GV4 does hold); the stage identity (:4276–4280); and the plan and the campaign's read plan (:4281–4290). The bench-folder checks sit just before the range (:4216–4223).
4. For Q2, a question the block does not ask. GV3's hash check covers `ids.TOKENIZER_FILES`' three files. The same folder holds `vocab.json` and `merges.txt`, pinned in the model manifest (data/olmo/manifest.json:263–266 and :187–190), and a tokenizer load from that folder may read them (the survey's §2, "What the box decodes with"). Should the check cover every file the load reads?
5. GV1's (c): the stages already record MANIFEST.json's sha256 as the identity's `rendering_id` (drv:1174 and :4277; L:218–220), and G-TIME-n's committed report carries it. What (c) adds is the comparison with the pin, in a G-VER record.
6. T1:55's "GV6 (what a STOP holds)" reads ambiguously. GV6 is what a STOP at step 12 means for step 13 and the campaign.
7. The texts describe §3's extraction differently. T2:36 says "by `jq`"; T3:68–69 says "`sed -n` of one into `jq`". Lines 3–28 were then taken by a further `sed -n` (14:55:15Z). The three should say the same thing.
8. Citation precision in GV4. G-TIME-n's own driver check is drv:4249–4251 (drv:192: "as backend-ext's"). The package hash's coverage of verify.py is guard:4–5. Citing those beside drv:1156–1158 and guard:31–32 would match GV4's frame.
9. T3's list was drawn from the sweep at 15:01:41Z. Nine commands ran after its prints (15:04:16Z–15:07:32Z), with four kinds the list does not name. Code also kept working after this brief's hash (from 15:08:21Z), which is outside this window. The entry needs a final sweep at its commit window.
10. Scratch writes are not named anywhere in T3: the redirects at 03:18:04Z, 14:55:02Z, 14:55:15Z, 14:55:25Z, 15:01:41Z and 15:01:51Z; `mkdir` at 14:55:02Z; and the assembly script's output. The index and commit writes in 7d01b02's window are also unnamed. One line would cover them if the seat counts writes.
11. This report gives the sweep's times as T's UTC stamps because the brief asks for times. If the report is committed whole, the project's no-times-in-committed-text convention may want them replaced by order and kind.
12. A minor point in §1 as sent: GV8's "expect_n is 160 (verify.py:77–78)". The 160 is verify:71's default (schema.N_SESSIONS, schema:278); :77–78 is the count check.

DEPARTURES
- `sed 's/^/ /'` was used once as a filter on printed lines of valence_core/n/schema.py. sed is not in the brief's interpreter list, but it runs a script language, so I declare it.
- One `jq` run's output went to /dev/null, so nothing was written.
- One command carried a stray environment assignment, `awk_free=1`, before `/usr/bin/grep`. No awk ran, but the word stood in that command's text.
- Git forms beyond item 1's list or without item 3's pathspec:
  - `git log --format` (ids, subjects, commit times) with no pathspec, for HEAD's last eight commits and for the cited ids;
  - `git log -n 1 --format=%B 7d01b02`, a commit-message read, piped to `grep -o`, which printed only the closed-paths phrase;
  - `git log` and `git diff --name-only` naming the code folders valence_core/n and valence_core in place of item 3's pathspec;
  - `git diff --numstat` of RESULTS.md and .gitignore.
- Reads of named committed files at other commits: deabf3f's LOCK-n.md, piped to shasum; one line of 9f64305's ids.py; the .gitignore diff from 4fdcdcc to 91f0d35.
- I printed the routing record's three closing lines (the closing tag and the harness note) unmasked, which is more than that finding needed.
- Not departures, within the brief's rules: I read the model manifest with the file-reading tool only; I viewed Code's closed-folder output lines only with digits masked; in S I read only the named files and this brief. No guard marker or plain campaign name stood in any of my commands, and I listed, read, sized or timed nothing under data/*/ckpt, data/*/reports or data/m[f]3.
```
