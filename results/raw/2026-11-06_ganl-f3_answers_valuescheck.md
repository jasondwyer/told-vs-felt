# G-ANL-F3's close: blind values-check of Code's referent check and close line (2026-11-06)

*Code's raw. Before the close commit, a blind values-check agent (fresh context, read-only, at HEAD `273ca8f`) checked Code's referent check of the seat's answers (`results/raw/2026-11-06_ganl-f3_answers_referent-check.md`) and the close line drafted for the G-ANL-F3 STOP entry in RESULTS.md, against their sources. Its report follows verbatim, local paths scrubbed (`<tmp>` = Code's session scratch). Code's dispositions follow it: every flagged item was re-checked at source before it was applied. HEAD moved to `b9a26ef` (the pod session's apparatus smoke) while the check ran; no file it read changed.*

## 1. The report (verbatim)

81 items, 67 CONFIRMED, 1 FAIL, 10 IMPRECISE (plus 3 NOT CHECKABLE: no file holds them).

Labels used here:
- RC = `results/raw/2026-11-06_ganl-f3_answers_referent-check.md` (uncommitted; sha256 `f60bd7f3…8261` as read).
- CL = `<tmp>/ganl/close_line.md`.
- GA:N = line N of the new answers file, `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md`.
- `answers:N` keeps its meaning: line N of the F3 prebuild answers.

The check was read-only at HEAD `273ca8f`. Every cited source file is tracked, and `git status --short` is empty for each.

## Claim-by-claim check

### RC header (RC:3)
1. **CONFIRMED.** The answers file's sha256: `shasum -a 256` gives `4edfbb8e3d08844e47a329a951f9c2dd381115f0fd92c8b2b77f2207777ca42e`.
2. **CONFIRMED.** HEAD is `273ca8f`: `git rev-parse HEAD` gives `273ca8fc3fc9…`.
3. **CONFIRMED.** m is v1.11 at root, sha256 `42ab36ec…6c6b`. `shasum` gives `42ab36ecc814…c96c6b`, the same as the HEAD blob.
4. **CONFIRMED.** A-m1 v0.1 is at root (`f26bc59`). `git cat-file blob f26bc59:ADDENDUM-m1-…v0_1.md | shasum -a 256` gives `ea08322d…9001`, the same as the working file. f26bc59's subject is "ADDENDUM-m1 v0.1 COMMITTED".
5. **CONFIRMED.** The STOP is at `958e762` (also RC:8): `git log` on the STOP raw lists 958e762 only.
6. **IMPRECISE.** "It covers sections A, B and C, C's included as the routing asks."
   - RC §1 also checks D (RC:68).
   - The routing block as CL quotes it (CL:24–32) asks only "Run the answers as written. STOP on anything unresolved; minor residues as dated notes …". It makes no request about C.
   - If the request came in the coordinating session's relay, it cannot be checked here.

### RC §1, header items
7. **CONFIRMED.** F-1 to F-7 are at `mf3-build_design.md:155–161`: §10's heading is at :153, F-1 at :155, F-7 at :161.
8. **CONFIRMED.** Finding 3 is in §1 of `mf3-build_review.md`. §1 spans :5–86, and "3. MINOR — readrule.py:325-326" is at :32.
9. **CONFIRMED.** The BACKEND flag is quoted verbatim. It is at RESULTS.md:83, and `git show 190ba90:RESULTS.md` has it at :83. 190ba90 adds the entry (RESULTS.md +69).

### RC A1
10. **CONFIRMED.** A-m1:44 ends "a non-reproduction is a STOP (rule 26's form)".
11. **CONFIRMED.** `git cat-file blob ed8e886:scripts/m_analyze.py | shasum -a 256` gives `655e0f7f6743d0bf497f5ba97ce37f7febf9fcf6a45e068b5385ee945c5dc16f`. HEAD's file is the same blob.
12. **CONFIRMED.** LOCK-m-F0.md:147 names the analyzer `655e0f7f…`, :148 the package `5f646db6…d771`, :149 the closure `a3bc7bb9…b22b`.
13. **CONFIRMED.** `Q-F0_VERDICTS.json`'s `inputs.lock` is {`LOCK-m-F0.md`, `fc7e9db8ecfa…015c`}. `shasum` of LOCK-m-F0.md gives `fc7e9db8…`.
14. **CONFIRMED.** PIN-14 is at m_analyze.py:1934–1944: a loop over the three shas, with the raise "(PIN-14, PIN-1)" at :1944. It sits in `run_verdicts` (:1907).
15. **CONFIRMED.** The seven files are those at STOP:39. Each is tracked, and each HEAD blob hash equals its working-tree hash: dd389eca, 483f32ea, 9a187fbc, 93cf4964, c8320eff, ec7d2082, dcaaaac3.
16. **CONFIRMED.** m:318: "Neither the seat nor the PI reads any pick-bearing artifact … before that unit's VERDICTS are computed".
17. **CONFIRMED.** answers:26: "and asserts the OLMo v1 outputs unchanged".
18. **CONFIRMED.** m:278 has "5 × 6³ = 1,080 tuples [S]". m_analyze.py:9–10 has "the 5 x 6^3 = 1,080 v1 tuples under both values of the 0.12-artifact flag".

### RC A2
19. **CONFIRMED.** m:324 is quoted verbatim (the bold dropped).
20. **CONFIRMED.**
   - :413–415 has `"units": "olmo", "v2_only": True`.
   - :2467–2468 (`crosscheck_coordinate`) has "pending-closed-at-v2 is the v2 posting's (G-ANL-F3)".
   - :2925–2927 is PIN-38: "pending-closed-at-v2 is refused at v1".
21. **CONFIRMED.** 481 × 5 = 2,405. Times 91 is 218,855, times 125 is 300,625, and the two sum to 519,480, m:291's figure.

### RC A3
22. **CONFIRMED.** Q7's heading is answers:44 and its text answers:46.
23. **CONFIRMED.** RESULTS.md:599–600, the F3 STOP close (dc1ffe1), reads "v2's sentence table is built at the / Q-F3 VERDICTS session against the posted v1: [confirmed]." It is quoted again at :370–371.
24. **CONFIRMED.** answers:26: "The rule: G-ANL-F3's in-place commit lands only when no OLMo unit is open".

### RC A4
25. **CONFIRMED.** A-m1:44 is §2.5, with items (1)–(3).
26. **CONFIRMED.** VERDICTS_read.md:83 is §4 item 2.
27. **IMPRECISE.** RC says "`_prod_committed` is at `scripts/m_analyze.py:1768–1775`".
   - The function starts at :1768 and its last line, `return stages._committed(rel)`, is :1773. Lines :1774–1775 are blank.
   - GA:18 and the source (VERDICTS_read.md:83) both give 1768–1773, so the check replaced a correct anchor without saying so.
28. **CONFIRMED.** `_repo_rel` (:1742–1746) returns the repo-relative path, which equals `str(p)` for a repo-relative input, so :1771–1772 reports it "outside the repository".
29. **CONFIRMED.** `flag_of_record` calls `committed(p)` at :1657. At :1658–1660 it sets the reason and returns with value False.
30. **CONFIRMED.** round2.md:19 has the quote verbatim.

### RC A5
31. **CONFIRMED.** m:64 is in §0.10 (heading at m:60), and the quote is verbatim.
32. **CONFIRMED.** m:190 has ".927 at P = .65" (A3 (144, 56)) and the attained-power sentence verbatim.
33. **CONFIRMED.** N8 is `m1-v0_1_referent-check.md:213–217`.

### RC B
34. **CONFIRMED.** G-TIME-F0_read.md:1 calls itself "the step-10 read". Its Q2 is at :45, and the quote is verbatim.
35. **CONFIRMED.** m:277 names no tokenizer.
36. **CONFIRMED.** `valence_core/m/gshape.py:29` (module docstring): "No model, no tokenizer, no generation."
37. **CONFIRMED.** At 1bf94a6, `data/mf3/gates/G-SHAPE-F3.json` (sha256 `0f9b7bb9…6e9c`) has a `layer_r.scope` text.
38. **CONFIRMED.** answers:14 is "Its licence (C2)".
39. **CONFIRMED.** scripts/m_gpwr.py exists.
40. **CONFIRMED.** The m:184–186 rows are quoted verbatim.
41. **CONFIRMED.** m:190 has "Power floors: A2 ≥ .85 at P = .65; every control ≥ .85 at P = .70", "A2/A3 by the grid rule" and the attained-power sentence.
42. **CONFIRMED.** answers:33 is Q5's heading.
43. **CONFIRMED.** m:174 has "(≤ 36)".
44. **CONFIRMED.** m:271: "their free-round events — exclusions, degeneracy, any class — are withheld to the unit's VERDICTS entry or NOT-RUN record".
45. **CONFIRMED.** Both m:281 quotes are verbatim, and m:295 has "criterion 2/2 as above".
46. **IMPRECISE.** RC says "F35 and ruling (h) are as the build's values-check recorded them."
   - The values-check records three things: ruling (h), `excluded@free` at G-TIME-F3, and `excluded@reasoning` gone from `_PRINTED_RX` / `_LINE_RX` (C9 #3 at `mf3-build_valuescheck.md:228`; A27 at :87).
   - It never names F35, and it has no "after the first pick" (grep finds neither).
   - The answers' "every contrast line after the first pick printing `excluded@free`" comes from F35's register row (`mf3-build_design.md:92`) and the code's PIN (`valence_core/mf3/readrule.py:323–329`).
   - This is also an answers anchor the check missed: GA:31 credits F35's clause to "The values-check".
47. **CONFIRMED.** m's `announce_stop` is defined at `stages.py:1211`. In :1218–1238, a contrast session's free-phase trigger is withheld (:1226–1230), and every other trigger names `hit['bar']` (:1231–1238).

### RC C
48. **CONFIRMED.** RESULTS.md:24–27 has pod `qny1x4v8padeke` and BACKEND PASS, added by 190ba90.
49. **CONFIRMED.** There is no `LOCK-m-OLMo-*` file in the tree (`find`) or at HEAD (`git ls-tree`).
50. **CONFIRMED.** A-m1:51 (§3 item 4) is quoted verbatim.
51. **CONFIRMED.** m:302 has the OLMo units per checkpoint.
52. **CONFIRMED.** m:302 has "(two sessions, one per arm;" and "(24 sessions,". Times 3 gives 6 and 72.
53. **CONFIRMED.** m:251 is quoted verbatim.
54. **CONFIRMED.** RESULTS.md:33 has "price.secure **$1.79/hr**".
55. **CONFIRMED.** RESULTS.md:36–37 has "(466 G, 242 G used)", and 466 − 242 = 224.
56. **CONFIRMED.** `PROPOSAL-n-bk-reconciliation-v0_2.md:101` (§2.7; sha256 `30a3d0f5…04f4`) has "bf16 (≈ 64 GB; …)" and the headroom sentence verbatim. 2 × 64 = 128. The record gives no fp32 size, and the check claims none.
57. **CONFIRMED.** `resume.py:253–259`: `pod_id()` returns `_env_pod()` (:248–250), which reads `POD_ENV = "RUNPOD_POD_ID"` (:92). The docstring says "(empty or whitespace = absent)".
58. **CONFIRMED.** The m:267 quote is verbatim.
59. **CONFIRMED.** RESULTS.md:62–63: "differs from this run's only in `path`, which the identifier drops". `resume.py:147` has `BACKEND_DROP = ("n_encodes_clipped", "path", "seed")`.

### RC D
60. **IMPRECISE** (not checkable against a file). RC says "The routing block answers D's five items in order … The PI's choice on G-ACQ is 'Now, in parallel'."
   - In the block as CL quotes it (CL:30), the G-ACQ line keeps both options: "[now, in parallel / after the campaigns]".
   - The choice came in chat (CL:34).
   - The order holds, with a Pod line between the batching and G-ACQ.

### RC §2 notes
61. **CONFIRMED.** N1: GA:28 has "A1 96/32"; m:184 has "96 cached, 80 uncached / 32"; the m:190 quote is verbatim.
62. **IMPRECISE.** N1 says "`scripts/mf3_gpwr.py` re-derives the column of the path LOCK-m-F3 v0.2 fixes, as `scripts/m_gpwr.py` does for Q-F0."
   - `ls scripts/mf3_gpwr.py` finds no such file. F-5 builds it after G-F3.
   - The m_gpwr half holds. m_gpwr.py:16 has "the floors A0 80, A0s 32 (uncached; schedule.FLOORS)", which is LOCK-m-F0 v0.2's path (LOCK-m-F0.md:431).
   - m:296 has LOCK-m-F3 v0.2 fix the path.
63. **CONFIRMED.** N2:
   - `analyzer_binding` is at :2370–2387, with PIN-42 at :2373–2379.
   - It refuses only on the proposal pin (:2380–2382) and an uncommitted analyzer (:2383–2385), and returns the three shas (:2386–2387).
   - `run_posting` (:2636) has no refusal on the three shas.
   - PIN-14 is `run_verdicts`' binding (:1934–1944; register text at :2836).
64. **CONFIRMED.** N3: the F-6 and F-7 sites are in the three files N3 names.
   - readrule.py:200, :472 and :486 (`reasoning_cap_reached`).
   - stages.py:1089 (the CAP TRIGGER line) and :1101–1143 (`gid_decide`, `_gid_pair`'s `meta_identical`).
   - guard.py:46 (`GID_CRITERION`) and :91–94 (the licence's criterion test).
   - All three files are in G-SHAPE-F3's sources map at 1bf94a6, and the package hash covers every `*.py` (answers:14).
65. **IMPRECISE.** N3 says: "On the step-10 read's ground (`G-TIME-F0_read.md:45`: an edit that moves neither the package hash nor the analyzer 'does not re-run')".
   - The quote is there, but the subject at :45 is "an edit to `scripts/m_sessions.py` that wires a subcommand, with no change under `valence_core/m`".
   - Concluding from it that a package-moving edit re-runs denies the antecedent.
   - :45 itself says "no change under `valence_core/m` (an edit there moves the package and is outside this answer)".
   - The re-run rule is G-SHAPE-F0's PIN-S10, "any difference re-runs G-SHAPE-F0 first" (`valence_core/m/gshape.py:233–236`). mf3's gshape.py does not restate it.
66. **CONFIRMED.** m:292 names "G-SHAPE-F3's result".
67. **IMPRECISE.** N3 says: "superseded by hand … (mf3's `gshape.py:654`: 'never overwritten'), on the word that the routing of LOCK-m-F3 v0.1 can carry."
   - The quote is right.
   - The same docstring goes on, "supersession is a hand git mv on the seat's ruling" (:654–655).
   - PIN-S9 says "Supersession is by hand only, on the seat's ruling" (m gshape.py:1515–1516).
   - The note never says whose word it is. CL:18–19 repeats the gap.
68. **NOT CHECKABLE.** N3 says "LOCK-m-F3 v0.1 waits for the coordinating session's word in any case." No file says so. The record's own reason is m:292: that lock names "G-ANL-F3's analyzer and lexicon hashes".

### Answers anchors the check missed
69. **IMPRECISE** (missed). GA:41 (C2) says "so the seat's reads come twice, not six times", and its chain has no read after G-CAL-OLMo ×3.
   - m:271 says "G-CAL's and each G-CAL-OLMo's generations are read by the seat at the stage (they carry no pick)", and m:72 says the same.
   - So the batched chain has three seat reads (G-CAL-OLMo, G-TIME-OLMo, G-F0m-OLMo), and the unbatched one nine. A G-TIME-OLMo pause would add an adjudication (m:302).
   - RC's C2 item (RC:56–59) checks only the session counts.
   - Item 46 (GA:31) is the other miss. The other two answers anchors wrong at source are already N1 and N2.

### CL
70. **CONFIRMED.** The file name and sha256 at CL:3–4 and CL:25–26 match the file on disk.
71. **CONFIRMED.** The A1 summary matches GA:9.
72. **CONFIRMED.** A2: (P1), GA:14.
73. **CONFIRMED.** A3: "all three now", GA:16.
74. **IMPRECISE.** CL says "A4 and A5: … Code's eleven PIN readings confirmed, with two notes."
   - A5 says "None struck" (GA:20), and the readings stay strikable until LOCK-m-F3 v1.0 (answers:50; STOP:84).
   - A4 is "confirmed by anchor" (GA:18).
75. **CONFIRMED.** "B: F-1 to F-7 ruled. F-6 and F-7 change `valence_core/mf3`": GA:24–30, with the sites as in item 64.
76. **FAIL.** "… and are applied with G-ANL-F3." The answers never say when F-6 or F-7 lands.
   - F-6 (GA:29) gives no timing.
   - F-7 (GA:30) says "A seat PIN at LOCK-m-F3 v0.1; set before G-ID-F3 has run".
   - C1 has Code build G-ANL-F3 "to A1–A5 above" (GA:37), not to B.
   - The line also contradicts the check it summarizes: RC:78 says "None of this is G-ANL-F3's".
77. **CONFIRMED.** C1 matches GA:35–38.
78. **IMPRECISE.** "What they rule" leaves out B's finding 3 (GA:31) and C2–C4 (GA:41, :43, :45), including C4's STOP condition on G-CAL-OLMo's provenance.
79. **CONFIRMED.** CL:13–19 matches RC:3 and RC:72–78; it inherits item 67's gap.
80. **NOT CHECKABLE.** The routing block (CL:24–32) was relayed from another session. Only its file name and sha256 can be checked, and they match (item 70). The e9b5022 it cites exists (PROPOSAL-k v1.1 COMMITTED).
81. **NOT CHECKABLE.** "The PI's choice on the G-ACQ line, in chat: 'Now, in parallel'" (CL:34).

I skipped @@VC@@ as instructed. Its link target, `results/raw/2026-11-06_ganl-f3_answers_valuescheck.md`, does not exist yet.

## FAIL items and corrections

**76 (CL:11).** Replace the line with:

"- B: F-1 to F-7 ruled, and the review's finding 3 confirmed as the rule at every stage. F-6 and F-7 change `valence_core/mf3` (F-7 a seat PIN at LOCK-m-F3 v0.1, set before G-ID-F3 runs); the answers do not say when either edit lands."

If Code plans to land the edits with G-ANL-F3, say so outside "What they rule", as Code's plan, and reconcile it with RC:78.

## IMPRECISE items and corrections

**6 (RC:3).** Write: "It covers sections A to D (D against the routing block as relayed)." Drop "C's included as the routing asks" unless the relay's words are quoted.

**27 (RC:31).** Write: "`_prod_committed` is at `scripts/m_analyze.py:1768–1773`".

**46 (RC:50).** Write: "Ruling (h), `excluded@free` for every G-TIME-F3 contrast line, and `excluded@reasoning` gone from `_PRINTED_RX` / `_LINE_RX` are as the build's values-check recorded them (C9 #3, `results/raw/2026-11-06_mf3-build_valuescheck.md:228`; A27, :87). 'Every contrast line after the first pick printing `excluded@free`' is F35's register row (`results/raw/2026-11-06_mf3-build_design.md:92`) and the code's PIN (`valence_core/mf3/readrule.py:323–329`); the values-check names neither." Then note that the answers' finding-3 line credits this to the values-check.

**60 (RC:68).** Write: "The routing block, as relayed, takes D's five items in order (the go for G-CAL-OLMo, the order, the batching, G-ACQ, the PIN-29 acknowledgement), with a Pod line between the batching and G-ACQ. Its G-ACQ line keeps both options ('[now, in parallel / after the campaigns]'); the PI chose 'Now, in parallel' in chat."

**62 (RC:72).** Write: "`scripts/mf3_gpwr.py`, built at F-5's step (after G-F3), will re-derive the column of the path LOCK-m-F3 v0.2 fixes, as `scripts/m_gpwr.py` did for Q-F0 on its uncached path (A0 80, A0s 32; `scripts/m_gpwr.py:16`; LOCK-m-F0.md:431)."

**65 (RC:76).** Write: "On the step-10 read's own terms (`G-TIME-F0_read.md:45`: its clearance covers a subcommand-wiring driver edit 'with no change under `valence_core/m`', and 'an edit there moves the package and is outside this answer') and G-SHAPE-F0's PIN-S10 ('any difference re-runs G-SHAPE-F0 first', `valence_core/m/gshape.py:233–236`, not restated in mf3's gshape.py), G-SHAPE-F3 re-runs on the new package before LOCK-m-F3 v0.1 names its result (m:292)."

**67 (RC:77).** Write: "… superseded by hand, as G-SHAPE-F0's PIN-S9 has it (mf3's `gshape.py:654–655`: 'never overwritten'; 'supersession is a hand git mv on the seat's ruling'), on the seat's ruling, which the routing of LOCK-m-F3 v0.1 can carry."
In CL:18–19, write: "… its `1bf94a6` artifact superseded by hand on the seat's ruling (PIN-S9), which that routing can carry."

**69 (new dated note in RC §2).** Add:

"N4. C2's count. m:271 (and m:72) also has the seat read each G-CAL-OLMo's generations 'at the stage' (they carry no pick). C2's chain names two reads, after G-TIME-OLMo ×3 and after G-F0m-OLMo ×3; batched, the G-CAL-OLMo read is a third (nine unbatched, not six), and a G-TIME-OLMo pause adds an adjudication (m:302). The batching ruling is otherwise unaffected."

Then change "three minor residues" to "four" at RC:3 and CL:15, and add to CL: "N4: C2's chain also carries the seat's G-CAL-OLMo read (m:271)."

**74 (CL:10).** Write: "- A4: the riding texts confirmed by anchor. A5: none of Code's eleven PIN readings struck (they stay strikable until LOCK-m-F3 v1.0), with two notes for the register."

**78 (CL, after the C1 line).** Add:

"- C2: the three checkpoints batched per stage. C3: the pod stays up through the OLMo track; G-ACQ (PROPOSAL-n) may start on the same box on the PI's word, Code checking volume headroom first (PROPOSAL-n §2.7). C4: the pod-id PIN stands; one line in `/workspace/env.sh` exports `RUNPOD_POD_ID` from `/proc/1/environ`, quoted in the G-CAL-OLMo entry, whose provenance must print `qny1x4v8padeke` or STOP."

Finding 3 goes into B, as in the FAIL correction.

## NOT CHECKABLE items

**68 (RC:78).** If this comes from the record, write: "LOCK-m-F3 v0.1 names G-ANL-F3's analyzer and lexicon hashes (m:292), so it follows G-ANL-F3's commit in any case." Otherwise, cite the coordinating session's word.

**80 and 81.** These are relayed or chat-only. Only the file name and sha256 can be checked, and they match.

## 2. Code's dispositions

Every item marked FAIL, IMPRECISE or NOT CHECKABLE was re-checked at source before it was applied. The 67 CONFIRMED items need no change.

| Item | Verdict | Re-checked at source | Disposition |
|---|---|---|---|
| 6 | IMPRECISE | The request is in the coordinating session's relay of 2026-11-06: "Run your referent check of the whole answers file, every anchor at source, C's included." | Applied. RC's header now reads "sections A to D: C's included, as the coordinating session's relay asks (…), and D against the routing block as relayed". |
| 27 | IMPRECISE | `scripts/m_analyze.py:1773` is `return stages._committed(rel)`; :1774–1775 are blank. | Applied: 1768–1773. |
| 46 | IMPRECISE | `mf3-build_valuescheck.md:228` (C9 #3) and :87 (A27); `mf3-build_design.md:92` (F35's row); `readrule.py:323–329` (the PIN). "F35" and "after the first pick" occur 0 times in the values-check. | Applied: RC's finding-3 item rewritten as proposed; the answers' attribution carried as dated note N5. |
| 60 | IMPRECISE | Not checkable against a file: the block and the PI's chat choice are as relayed (CL). | Applied: RC's D item rewritten as proposed. |
| 62 | IMPRECISE | `scripts/mf3_gpwr.py` does not exist; `scripts/m_gpwr.py:16` and `LOCK-m-F0.md:431` read as cited; m:296 has LOCK-m-F3 v0.2 fix the path. | Applied: N1 states the script as future, with the anchors. |
| 65 | IMPRECISE | `G-TIME-F0_read.md:45` (the clearance's subject and "outside this answer"); `valence_core/m/gshape.py:233–236` (PIN-S10). | Applied: N3's second bullet rewritten as proposed. |
| 67 | IMPRECISE | mf3 `gshape.py:654–655` ("never overwritten … supersession is a hand git mv on the seat's ruling"); m `gshape.py:1515–1516` (PIN-S9). | Applied in RC (N3's third bullet) and CL (the N3 line). |
| 68 | NOT CHECKABLE | m:292 names G-ANL-F3's analyzer and lexicon hashes; the coordinating session's relay of 2026-11-06: "LOCK-m-F3 v0.1, and anything that runs Qwen on the laptop, wait for my word". | Applied: N3's last bullet cites both, and scopes "not G-ANL-F3's" to the re-run and the supersession. |
| 69 | IMPRECISE (missed) | m:271, m:72 (the G-CAL-OLMo read at the stage); m:302 ("a pause → the seat's adjudication, before that checkpoint's qualification"). | Applied as dated note N4 (the residues are now five, N1–N5). |
| 74 | IMPRECISE | answers file :18 ("confirmed by anchor") and :20 ("None struck"). | Applied: CL's A4/A5 line as proposed. |
| 76 | FAIL | answers file :29–30 give no timing for F-6 or F-7; :37 has G-ANL-F3 built "to A1–A5 above". The timing is the coordinating session's relay ("Apply B as written"). | Applied: CL's B line as proposed; a separate "Code's plan for B" bullet outside "What they rule" names the relay; RC's N3 states the plan and its source, and its last bullet no longer reads as contradicting it. |
| 78 | IMPRECISE | answers file :31 (finding 3), :41, :43, :45 (C2–C4). | Applied: finding 3 in CL's B line; C2–C4 added after C1. |
| 80, 81 | NOT CHECKABLE | Relayed or chat-only; the answers file's name and sha256 match (item 70). | No change: the routing block and the PI's chat choice are quoted as the coordinating session relayed them. |
