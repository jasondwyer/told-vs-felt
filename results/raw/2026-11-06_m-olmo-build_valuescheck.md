# m package — BUILD (OLMo): blind values-check of the BUILD entry, the design raw and the review's dispositions (2026-11-06)

*Code's raw. One blind refuter (a general-purpose agent with no access to Code's reasoning) checked three texts read-only, against the working-tree diff, the governing texts and the raws of record: the BUILD entry in RESULTS.md, `results/raw/2026-11-06_m-olmo-build_design.md`, and §2 of `results/raw/2026-11-06_m-olmo-build_review.md`. Result: 4 FAIL and 25 IMPRECISE, the rest CONFIRMED. Code re-checked every FAIL and IMPRECISE item at its source before applying it (§2). One FAIL changed code: VC4-2, mislabelled, is now built. So the self-test of record and the site check were re-run on the final bytes. The report is reproduced verbatim except that the session scratch path is shown as `<scratch>/`.*

## 1. The report (verbatim, the scratch path replaced)

## Claim-by-claim check

### A. RESULTS.md, entry "m package — BUILD (OLMo)" (RESULTS.md:24–91)

1. **Built under the answers' §0, Q2 and Q6, as "the first node of ADDENDUM-m1 §4 step 4".** CONFIRMED.
   - Answers :7: "The OLMo track's first node is therefore its own build".
   - A-m1:58: step 4 is the OLMo track.
2. **Builds G-CAL-OLMo, wires `time` and `qual` for the three OLMo units, and binds the weights of record in the identity.** CONFIRMED.
   - gcal.run_completability takes `unit=` (gcal.py:1088).
   - `_run_stage` dispatches the OLMo units to `_run_stage_olmo` (m_sessions.py:1552–1559, 1673).
   - The weights binding is in IDENTITY_KEYS_OLMO in both resume.py:106 and gcal.py:156.
3. **Seals the CHECKPOINT STATE INCONSISTENT line at the package.** CONFIRMED: resume.py:592–599 calls `bad(TOTALS_SEALED)`, which prints neither total.
4. **Builds the carry-overs O4-1, O1-3, RM4-1, VC4-1 and VC4-2.**
   - O4-1, O1-3, RM4-1 and VC4-1: CONFIRMED (m_sessions.py:1191–1215, 1226–1237, 1271–1279; module docstring :129–157; camp_pauses).
   - VC4-2: **FAIL** (see 109).
5. **Those carry-overs were addressed to "the next unit".** CONFIRMED: answers :40–42; G-F0m-Qwen_read.md:42; step17.md:86; VERDICTS_read.md:86.
6. **Declares O2-3's listing forms for the OLMo checklists.** CONFIRMED (design raw §4). Q6 says "the README and the checklist".
7. **The OLMo campaign stays refused until each LOCK v1.0.** CONFIRMED: `refusal()` at m_sessions.py:278–284; self-test raw :827.
8. **Self-test 846/846.** CONFIRMED: 846 [PASS] lines, 0 [FAIL].
9. **Site check passes all seven suites.** CONFIRMED: 154/154, 67/67, 21/21, 20/20, 46/46, 18/18 and 24/24, every one EXIT=0.
10. **14 findings, all applied or disclosed, two of them spec departures.** CONFIRMED as a tally.
    - Findings 1 and 2 are tagged SPEC.
    - Findings 7 and 10 are disclosed; finding 14 is carried to the seat.
    - Caveats on dispositions 13, 6 and 3 are at 138, 131 and 128.
11. **"A blind values-check ran before commit."** PENDING. It looks ahead: `…_valuescheck.md` does not exist yet.
12. **package_sha256 moves from 5f646db6… to 60199b36…feec.** CONFIRMED.
    - I hashed HEAD's 18 package blobs by `package_sha256_of`'s rule: 5f646db6e82c…d771.
    - The working tree gives 60199b36557a…e7feec.
    - LOCK-m-F0.md:148 names 5f646db6….
13. **Analyzer unchanged, 655e0f7f….** CONFIRMED: 655e0f7f…c16f, and no diff against HEAD.
14. **"Not done" list.** CONFIRMED.
    - There is no `LOCK-m-OLMo-*`.
    - There is no OLMo file in data/m/gates or data/m/ckpt.
    - scripts/m_gpwr.py contains no "olmo".
15. **Stamp 08:23:03 UTC.** CONFIRMED as consistent with the record.
    - The raw headers say 08:23.
    - RESULTS.md was modified at 08:23:28; the driver was last edited at 08:17:09.
    - The self-test ran 5:01.
16. **The design raw holds "the hashes".** IMPRECISE: §6 gives only the old package prefix and the analyzer prefix. The new package hash and the file hashes are only in the entry.
17. **gcal.py sha256 d60b78e5…02fe.** CONFIRMED.
18. **resume.py sha256 78f2fc8e…bfb7.** **FAIL.**
    - The real hash is 78f2fc8eb8b3…c4540f22bf8fb7: it ends **8fb7**.
    - package_sha256 still equals the self-test's, so these are the bytes of the run and the error is a typo.
    - The self-test raw's header line 1 has the same typo.
19. **m_sessions.py sha256 6db190fc…1643.** CONFIRMED.
20. **"Nothing else" edited.** CONFIRMED: git status shows only these three code files modified, and nothing untracked under valence_core/ or scripts/.
21. **No SCORING_STACK_FILES entry edited.** CONFIRMED: gshape.py:92–104 lists 26 entries, none of them the three files.
22. **m_sessions.py is in TOOLING_FILES.** CONFIRMED: gshape.py:105.
23. **G-SHAPE-F0 re-runs before the first LOCK-m-OLMo v0.1 (N5), with supersession under PIN-S9 on Q2's word.** CONFIRMED: referent check :33–37; gshape.py:1508–1517; answers :19.
24. **The model-free G-SHAPE-F0 trial passes.** CONFIRMED: sitecheck :398–412 shows PASS on package 60199b36…, exit 0.
25. **Readiness: G-CAL-OLMo built.** CONFIRMED.
26. **Readiness: G-TIME-OLMo wired; its box path needs G-CAL-OLMo's PASS on the weights of record.** CONFIRMED: `olmo_gcal_problems` (m_sessions.py:762–789) is called at :1440.
27. **Readiness: G-F0m-OLMo needs v0.2's line and takes `--prior-adjudication-file`.** CONFIRMED: m_sessions.py:678 and :930–934; the flag reaches `stages.prior_gate` (stages.py:831–836).
28. **Readiness: G-PWR for OLMo not built, owed before each v1.0.** CONFIRMED: m:302 has "→ G-PWR; the PI sets that checkpoint's cap share → … v1.0".
29. **Readiness: campaign refused, later wired as a step-10 Q2-kind driver edit.** CONFIRMED as a stated intention (m_sessions.py:679).
30. **BACKEND tooling and the F0m-OLMo verifier predate this build.** CONFIRMED: commits 91ca822 and ba67acb (2026-08-19); verify.py is unchanged.
31. **"What each OLMo stage now requires, before any load."** IMPRECISE.
    - G-CAL-OLMo needs no lock: m_sessions.py:500–517 checks only precheck, weights and driver, and m:302 puts LOCK v0.1 after G-CAL-OLMo.
    - The lock must also name analyzer_sha256 and package_sha256: licence check (f), stages.py:537–586, run inside stage_precheck.
    - G-TIME-OLMo's need for G-CAL-OLMo's PASS is missing from this list.
    - The pod id, driver and weights items are CONFIRMED.
32. **A G-CAL-OLMo resume on another pod is refused (m:267).** CONFIRMED: gcal.py:1121–1137; self-test raw :635.
33. **"For the seat": the time/qual reading (finding 14); PIN O12 strikable until v1.0.** CONFIRMED.
34. **Q-F0 change: "a ruling beside an end pending … refused before the load".** IMPRECISE (minor): a PI stop the checkpoint records still passes (m_sessions.py:1207–1209).
35. **"The RULING line can carry RM4-1's note."** IMPRECISE (minor): true only on the stub path. On the Qwen path every such state is refused first (finding 3).
36. **"STOP and REFUSED lines carry the sealed sentence."** CONFIRMED for CHECKPOINT STATE INCONSISTENT lines. IMPRECISE as "the review's list": it drops the review's item on m_analyze's refusal text, which changes through `read_checkpoint` → `_check_state` (m_analyze.py:1996).
37. **`qual --unit Q-F0 --prior-adjudication-file` is refused.** CONFIRMED: m_sessions.py:1564–1567. At HEAD argparse already exited 2.
38. **"A Q-F0 resume, re-finish or `gcal --resume` is now refused on package_sha256."** IMPRECISE.
    - It holds for the four Q-F0 stage checkpoints (identity 5f646db6…, each already ended).
    - `gcal --resume` was already refused at HEAD: G-CAL_qwen.json's identity records package_sha256 4b496587…, and gcal.py:914–919 refuses any identity difference.
39. **"Each traced to Q6's carry-overs or to the package moving."** IMPRECISE: the prior-adjudication refusal comes from the OLMo wiring's new flag, not from Q6 or the package.
40. **Q-F0's campaign ended; its record stands on its lock.** CONFIRMED: terminal status COMPLETE.
41. **Q3's calendar fact and the seat's recommendation (b).** CONFIRMED: answers :26; no OLMo lock exists; the analyzer is unchanged.
42. **"Q2's commit order: … before the F3 build and before LOCK-m-F3 v0.1".** IMPRECISE (minor).
    - Q2 (:20) requires only "before LOCK-m-F3 v0.1", and only for a shared module that mf3 imports; Code is to state the order in the F3 BUILD entry.
    - "Before the F3 build" is Code's own ordering.
    - gcal and resume are not on Q1's import list (:12).
43. **Records exist.** CONFIRMED for the self-test, site check and review raws; the values-check raw is pending (see 11).
44. **"Local absolute paths are scrubbed … as each header says."** The scrub itself is CONFIRMED: no /Users, /private, /var/folders or /tmp in the four raws. IMPRECISE: the self-test raw carries `<home>` at :621 and :752, but its header declares only `<repo>` and `<tmp>` and says "nothing else changed".
45. **Forward: PIN-14 refuses Q-F0 `verdicts` on the moved package; A-m1 §2.5 (3) meets it.** CONFIRMED: m_analyze.py:1933–1944 with :1786; A-m1:44.
46. **Forward: G-PWR, the campaign wiring, O2-3's text.** CONFIRMED as forward items.

### B. Design raw (results/raw/2026-11-06_m-olmo-build_design.md)

47. **Header: answers file aec58440…4df3, committed at dc1ffe1.** CONFIRMED.
48. **§0 quotation.** CONFIRMED, verbatim (bold dropped).
49. **Q2 and Q6 paraphrases.** CONFIRMED.
50. **Readings are PINs declared at v0.1 and strikable until v1.0, "as at Q-F0's build".** CONFIRMED (answers Q8 :50).
51. **Ledger (55)'s rule.** CONFIRMED (answers :7).
52. **Respawn/BACKEND row.** The scripts exist and are unchanged: CONFIRMED. The label "(Phase-2 step 2)" is IMPRECISE: box_determinism.py:2 says "Phase 0 step 2", and box_respawn_check.py is the respawn protocol's step (i) (the 2026-08-19 amendment).
53. **G-CAL-OLMo row.** CONFIRMED (argparse `--unit` at :7497).
54. **LOCK v0.1 row.** The driver reads it at time and qual: CONFIRMED. The anchor "(§2.3)" is IMPRECISE: the raw has no §2.3, and m §2.3 is the dose (m:176).
55. **G-TIME-OLMo row.** CONFIRMED.
56. **G-F0m-OLMo row.** CONFIRMED (self-test raw :828).
57. **G-PWR row.** CONFIRMED.
58. **Campaign row.** CONFIRMED.
    - The OLMo branch is stub-tested: self-test raw :731, :732, :737.
    - The cap share at v1.0 is m:249's.
59. **G-VER row.** CONFIRMED.
60. **The table as m:302's stage list.** IMPRECISE (minor): LOCK-m-OLMo v0.2 is missing, though v0.1 and v1.0 are listed.
61. **gcal.py is not in the sources map.** CONFIRMED.
62. **Item 1: banner, generation path, keys, seeds, grader, bars, covariate.** CONFIRMED.
    - banner.py:5–6.
    - runner_olmo.py:43, :48, :98–105, :137–138.
63. **Item 1: "Qwen's branch is unchanged byte for byte".** CONFIRMED. I re-derived the Qwen artifact from the committed checkpoint with the new code; it is byte-identical to the committed G-CAL_completability_qwen.json.
64. **Item 2: file names.** CONFIRMED.
65. **Item 3: the five keys; `ban_ids_sha16` is 2dd86a453a2275ef in stages' form; `ban_sha256` is the scaffold file's.** CONFIRMED (stages.py:952–955; audit.py:62).
66. **Item 4: FAIL wording.** CONFIRMED (ON_FAIL; m:176).
67. **Items 5–6.** CONFIRMED (gcal.py:748–812, :866–890; stages.py:135 is the seam precedent).
68. **Item 7: tallies.** CONFIRMED; they are not in the artifact (gcal.py:1199–1202).
69. **resume.py is not in the sources map.** CONFIRMED.
70. **Item 8.** CONFIRMED: all four Q-F0 identities pass `_validated` with 18 keys and no weights_sha256.
71. **Item 9.** CONFIRMED.
72. **m_sessions.py is in the tooling map.** CONFIRMED.
73. **Item 10.** The names exist: CONFIRMED. "Q-F0's paths unchanged" is IMPRECISE (minor): `_run_stage`'s Q-F0 path gained the prior-adjudication refusal (:1564–1567).
74. **Item 12: "20 new checks (gcal 10, resume 3, driver 7; 825 → 845)".** **FAIL.**
    - I diffed the check lists of the 2026-10-18 self-test of record (825 checks) and this one (846): 21 checks were added and none removed.
    - resume: 3 (raw :331, :332, :360).
    - gcal-olmo: 11 (raw :628–638; the 11th is finding 1's pod check at :635).
    - m_sessions-olmo: 7 (raw :827–833).
75. **Item 12: the updated Q-F0 checks.** CONFIRMED.
76. **PIN register O1–O28.** Each entry has exactly one site marked "PIN (Code, declared at LOCK-m-OLMo-{ckpt} v0.1…)", 28 sites in all. Readings CONFIRMED unless listed under 77:
    - gcal.py: O1 :93, O2 :145, O3 :160, O4 :719, O5 :767, O6 :839, O7 :996, O8 :1048, O9 :1139, O25 :1123.
    - resume.py: O10 :97, O11 :592.
    - m_sessions.py: O12 :661, O13 :710, O14 :874, O15 :1337, O16 :1552, O17 :1683, O18 :278, O20 :834, O21 :1191, O22 :1226, O23 :1271, O26 :674, O27 :765, O28 :719.
    - O3's anchor RESULTS.md@9cbacdb:5680–5685 is the "For the box" item: CONFIRMED.
    - O8: I re-ran `olmo_tallies` on the committed artifact. (iii) gives 1, "CORR_corrupted i=6 s=1"; (iv) gives 11 with 9 hits. This matches RESULTS.md@9cbacdb:5032–5041. CONFIRMED.
77. **O19 and O24.**
    - O19 (:456–461): IMPRECISE. The reading, and the PIN text at the site, omit the driver check and DRIVER line (:507, :512) added under finding 9.
    - O24 (:7405–7407): IMPRECISE. It inherits the VC4-2 mislabel (see 109).
104. **§4 sealed message; redact_totals stays.** CONFIRMED (G-F0m-Qwen_read.md:42).
105. **§4 O4-1.** CONFIRMED.
     - Sources :213–219 are correct.
     - `run_campaign` passes a recorded stop as None (stages.py:2094–2102); NOT APPLIED cases at stages.py:2502–2520.
     - stages.py is unmodified.
     - "Exactly the NOT APPLIED cases" is IMPRECISE (minor): finding 7's CHECKPOINT MISMATCH case is disclosed in the PIN (m_sessions.py:1199–1202) but not here.
106. **§4 O1-3.** CONFIRMED: `ruling_sha16s` at :1138–1140; the stage applies the reused text at stages.py:2129.
107. **§4 RM4-1.** The note's text, its condition and the pre-load refusals' digests: CONFIRMED (say_ruling runs after the precheck, :1619). IMPRECISE (minor): "Qwen and box paths" — the box half is vacuous, because no OLMo campaign path exists (:1694 refuses it).
108. **§4 VC4 anchor :200–207.** CONFIRMED.
109. **§4 "VC4-2: the adjudication re-run sentence names a finish completed before the kill".** **FAIL.**
     - In the record, VC4-2 is the module docstring's reason for never re-offering an adjudication offered beside an end pending (review raw :205–207, :8164–8172, :8471–8474).
     - That reason was "declared for the module docstring … at a next driver edit".
     - It is unchanged at m_sessions.py:166–169 ("it rules on no pause the end re-finishes -- … or a ruling on a pause not yet shown").
     - The finish-before-kill text is the refuter's missed item (:8483–8485). It was added, but tagged "(VC4-2)" at :137.
110. **§4 VC4-1 text.** CONFIRMED.
111. **§4 "_run_stage's docstring rewritten" for VC4.** IMPRECISE (minor): only its O4-1 sentence changed (:1536–1539).
112. **§4 O2-3.** CONFIRMED in substance. IMPRECISE (minor) on sources:
     - :86 names only `git status --porcelain` and name-only `ls`.
     - `ls-files` and `shasum` come from O2-3's own text, which also names name-status (m-campaign-qf0_launchchecks.txt:2373).
113. **§4 weights binding.** CONFIRMED.
114. **§5 "no check removed".** CONFIRMED.
115. **§5 bare `--unit` and run_time/run_qual/run_campaign pins.** CONFIRMED.
116. **§5 qual help pin; the four step-14 Q3 checks.** CONFIRMED (self-test raw :810, :811, :821, :826).
117. **§5 whitelist additions.** CONFIRMED.
118. **§5 the OLMo block sits before the scans.** CONFIRMED: block at :6659–6925, scans start at :6926; the stdout scan, line-form and no-clock check, ruling-texts check (token zq7prioradjtokenq9) and PROVENANCE check (raw :834, :835, :839, :840) cover it. IMPRECISE (minor) if "the no-clock check" means the canary-clock check (raw :837): that check reads only outs[n_outs_c:n_outs_c_end] (:7117).
119. **§5 `ruling_sha16s` key.** CONFIRMED.
120. **§5 70-case mirror.** CONFIRMED. IMPRECISE (minor): "O1-3's must meet the stage applying the ruling", but the code checks only `not refused` (:6031–6032).
121. **§5 VC3-5 pins.** CONFIRMED.
122. **§5 as the full list of changed existing checks.** IMPRECISE: it omits two changed checks.
     - The Qwen-path mirror check (raw :816) gained finding 5's two cases.
     - The ended-campaign check (raw :817) now expects RM4-1's note.
123. **§6 package moves and analyzer unchanged.** CONFIRMED.
124. **§6 G-SHAPE-F0 conditions and PIN-S9.** CONFIRMED.
125. **§6 PIN-14, A-m1 §2.5 (3), and the posting recording the shas without refusing.** CONFIRMED (answers :21).

### C. Review raw §2 (Code's dispositions)

126. **#1.** CONFIRMED.
     - The m:267 quotation is verbatim, with an ellipsis for "under its deterministic keys,".
     - HEAD compared no pod.
     - The self-test (49 generations on A; B refused with 0 generated; A completes 79; B re-derives an identical artifact) is at gcal.py:2350–2385.
127. **#2.** The quotation and QUAL_LOCK_PATH_TEXT (:593): CONFIRMED. "Self-test: G-TIME-OLMo runs under v0.1" is IMPRECISE (minor): only `stage_identity_extra('time')` is tested with a lock lacking the line (:6723); the G-TIME-OLMo run itself uses a lock that carries it.
128. **#3.** Applied: CONFIRMED. IMPRECISE: the claim that "the help, module docstring and `ruling_line` docstring" name RULING REUSED, RULING BESIDE AN END PENDING and NO PAUSE TO ADJUDICATE.
     - Only camp_pauses names them.
     - The module docstring (:155–157) does not name them.
     - ruling_line's docstring (:1249–1256) says nothing about it.
     - The re-check's "box path" half is vacuous (see 107).
129. **#4.** CONFIRMED (:6658–6661, :7187).
130. **#5.** CONFIRMED (:6103–6108; `q_ref_ok` at :5190).
131. **#6 "applied".** IMPRECISE: stage_precheck's docstring was not updated.
     - It still lists four `campaign_ruling_problems` refusals that "the stage [makes] each again after the load", with no RULING REUSED (:1316–1318).
     - It still says "except two that only this precheck makes" (:1287), though RULING REUSED, RULING BESIDE AN END PENDING and `olmo_gcal_problems` are now also precheck-only.
     - The other items of #6 were applied: CONFIRMED.
132. **#7.** CONFIRMED (stages.py:2083–2096 runs before :2098).
133. **#8.** CONFIRMED (box_respawn_check.py:71–72; self-test raw :832).
134. **#9.** CONFIRMED: :507/:512; :762–789; `prior_gate` compares only unit, stage and proposal (stages.py:814–822).
135. **#10.** CONFIRMED: item 2 has "thy" and item 15 has "on".
136. **#11.** CONFIRMED (gcal.py:1005–1009).
137. **#12.** CONFIRMED (:6787).
138. **#13 "applied (20)".** **FAIL**: the self-test of record adds 21 checks.
139. **#14.** CONFIRMED.
140. **Q-F0 differences.** "Each traced to Q6 or the package" is IMPRECISE (see 39). Records complete and campaign ended: CONFIRMED.

## FAIL items and corrections

- **18:** write `78f2fc8e…8fb7`, in the entry and in the self-test raw's header.
- **74:** write "21 new checks (gcal 11, resume 3, driver 7; 825 → 846)".
- **138:** write "applied (21; gcal 11 with finding 1's pod check)".
- **4 / 109** (also O24, the PIN at :7405–7407 and the "(VC4-2)" tag at :137). Either:
  - build VC4-2 by rewriting m_sessions.py:166–169 to the record's form: "it rules on no pause shown when it was offered: it is the previous pause's ruling, already recorded, or one written before the pause it would rule on was shown"; or
  - relabel the finish-before-kill text as "the refuter's missed item (:8483–8485)" and list VC4-2 as not built.

## IMPRECISE items and corrections

- **16:** say the new hashes are in the entry, not the design raw.
- **31:** scope the lock requirement to time and qual; add licence (f) (analyzer_sha256 and package_sha256 named in the lock); add G-TIME-OLMo's need for G-CAL-OLMo's PASS.
- **34:** "a ruling the stage would not apply beside an end pending".
- **35:** add "(stub path only)".
- **36:** add m_analyze's refusal text.
- **38:** "gcal --resume was already refused (checkpoint package 4b496587…)".
- **39 / 140:** "…or, for the qual flag, the OLMo wiring".
- **42:** "Q2 requires before LOCK-m-F3 v0.1; Code also orders it before the F3 build".
- **44:** declare `<home>` in the self-test raw's header.
- **52:** "(Phase 0 step 2; the respawn protocol of 2026-08-19)".
- **54:** drop "(§2.3)" or cite O14.
- **60:** add a LOCK v0.2 row.
- **73:** "unchanged except the --prior-adjudication-file refusal".
- **O19:** add the driver check and DRIVER line, in the register and in the site's PIN.
- **105:** "exactly, where the stage reaches the re-finish (finding 7)".
- **107 / 128:** "on the Qwen path (no OLMo campaign path yet)".
- **111:** "_run_stage's docstring for O4-1 only".
- **112:** cite O2-3's own line for `ls-files`/`shasum`, and add name-status.
- **118:** name the line-form check's date/time clause, not the canary clock.
- **120:** "meet the stage not refusing".
- **122:** add the checks at raw :816 and :817.
- **127:** "identity_extra admits time under v0.1's text".
- **128:** "the help names the three refusals".
- **131:** update stage_precheck's docstring at :1287 and :1316–1318, or narrow the disposition to what was applied.

All checks were read-only; nothing in the repository was written. My scratch files (the three diffs, the old and new check lists, RESULTS.md@9cbacdb) are in `<scratch>/vc_olmo/`.

## 2. Code's dispositions (each re-checked at source first)

| item | re-check at source | disposition |
|---|---|---|
| 18 (FAIL) | `shasum` of resume.py: `78f2fc8e…f22bf8fb7` | the entry and the self-test raw's header now carry `…8fb7` |
| 74, 138 (FAIL) | the two self-tests' check lists: 825 → 846 | "21 new checks (gcal 11, finding 1's pod check among them; resume 3; driver 7)" in the design raw and the review's disposition 13 |
| 4, 109, O24 (FAIL) | the campaign driver review raw :8164–8172 (VC4-2: the module docstring's reason), :8471–8474 ("declared for the module docstring"), :8483–8485 (the missed item) | **built**: the module docstring's reason now reads "it rules on no pause shown when it was offered -- it is the previous pause's ruling, already recorded, or one written before the pause it would rule on was shown (VC4-2; the seat rules on a pause once shown)". The finish-before-kill text is relabelled as the review's missed item. camp_pauses' PIN and the design raw's §4 and O24 say so. |
| 131 | `stage_precheck`'s docstring at :1287 and :1316–1318 | **applied**: it names the precheck-only refusals (RULING BESIDE AN END PENDING, RULING REUSED, `olmo_gcal_problems`) beside the two it named, and the mirrored list says which ones the stage does not make |
| O19 | the PIN text at `run_gcal_completability` | **applied**: the driver check and the DRIVER line are in the PIN text and in the register |
| 31, 34, 35, 36, 38, 39, 42 | each against the code and the record | **applied** in the BUILD entry: the requirements split into every stage, `time` and `qual`, `time` only and `qual` only (with licence (f)); the Q-F0 list reworded as suggested; Q2's order stated as Q2's and Code's |
| 44 | the self-test raw's lines with `<home>` | **applied** to the regenerated raw's header |
| 16, 52, 54, 60, 73, 105, 107, 111, 112, 118, 120, 122 | each against its source | **applied** in the design raw |
| 127, 128, 140 | each against the code | **applied** in the review's dispositions |
| 11, 43 | — | resolved by this raw |
