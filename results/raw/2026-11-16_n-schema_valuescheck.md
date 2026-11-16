# n package — the read runner's record schema: the blind values-check, two passes, and Code's dispositions

*The n-build session (Code), PI date 2026-11-16. Checked: the RESULTS.md entry `n package — the read runner's record
schema`, and `valence_core/n/schema.py` with `valence_core/n/__init__.py`, before their commit. Two blind checkers,
both Code's subagents. Each was briefed to run no Python and to write nothing, under the list of record v2's items
1–5, quoted verbatim, and the coordinating session's lines on `data/mf3`. The second was blind to the first.*

*What each pass checked:*
- *Pass 1: the first drafts, `schema.py` sha256 `486c8aec56292ecf1d3a79e9e7f46a75962799530a1dc993024f74e407955422`
  and `__init__.py` `427f58ccf531d2d98bd76004e2ff8b2ece9514248328e12844156a659e711cfd`, at HEAD `41bfab4`. Both
  figures are its own.*
- *Pass 2: the revised drafts as they stood when it launched. `schema.py` was
  `164d56907542234aecd6a9abbf2809eaee095ae9f0ba92c1a711900193e432a9`, Code's copy taken after the launch and before
  any later edit. `__init__.py` was unchanged.*
- *The committed `schema.py` is pass 2's draft plus the edits its dispositions list:
  `77c12d6d0e7eee370291e0f5e587204f4ae613c65ce57f95c336f507273494bc`. Its self-test is 108/108 on these bytes.*

*Each report is reproduced as its checker returned it. Neither prints a local path, and nothing in them is changed.
In the reports, "E:" and "S:" are line numbers in the entry and module drafts the pass read.*

## Pass 1 (the first drafts), as returned

Blind values-check of the n schema drafts: 60 items. 40 CONFIRMED, 11 IMPRECISE, 2 FAIL, 7 NOT CHECKABLE. Checked at HEAD 41bfab4.

The drafts are cited as E:line (the entry draft) and S:line (the module draft). n:line is PROPOSAL-n-bk-reconciliation-v0_2.md. RESULTS.md anchors are at 41bfab4:
- "G-ACQ (n)" at :6668 (GA-4 :6740, GA-5 :6742)
- "G-DATA (n)" at :7215 (G-1 :7279, G-2 :7281)
- "PROPOSAL-n v0.2 COMMITTED" at :7295

**ITEMS**

1. The PI's item-10 quote (E:8–11) against the brief's text. After joining lines it is identical, including the en dash in "7–15". CONFIRMED.
2. "section N, item 10", "(evening)" and the PI's "Route as given" covering item 10 (E:2, E:8). The PI's block is not a repo file. It is consistent with the seat's own block, where item 10 sits under "N. n (two new sessions)" (answers raw :115–116; its wording differs, and the entry rightly quotes the PI's). It is also consistent with a215c28 and 97d160a, which cite "Route as given" for that evening's sections C and A. NOT CHECKABLE.
3. The seat's §5.1 quote (E:12–14, S:3–5). It is verbatim in results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md:60. The raw is committed at a215c28, and its sha256 1f3ce1f9…df84b re-hashes equal. CONFIRMED.
4. "committed first and alone", "n-analyzer builds … from this commit" and "BUILD entry with the session-count call" (E:1–6, E:53). These match seat §5.1 ("whose first commit is the read runner's record schema … built from that schema … Code's call, stated in the BUILD entry") and n:159 step 6. CONFIRMED.
5. One record per (arm, direction, dose point, session), with fidelity and identity riding inside, "each read counted once" (E:15–17, S:12–14). Sources: n:83, n:57 (C7/C15), n:77. CONFIRMED.
6. 136 cells before merges (E:17–18). From n:87–93: N1-V 5+1, N1-R 24×5, N1-P 2, N2-E/S/C 2 each, N4-T 1, N4-Ts 1 = 136. S:992–997 asserts it. CONFIRMED.
7. "Each cell file has a capture array" (E:18). The array is a separate .npy beside the cell file; the cell names it and records its sha256 (S:82–84; CELL_FIELDS capture_file, capture_sha256). IMPRECISE. Suggested: "Each cell file names a capture array (a .npy beside it) of the read position's residuals".
8. G-TIME-n and the BACKEND extension write records, citing GA-5 (E:18–19, S:14–16). GA-5 reads "the BACKEND extension's 24 fresh-versus-cached reads need n's cached read path"; see also n:109, n:118 and STAGES (S:104). CONFIRMED.
9. 7,360 reads with nothing merged, 6,240 with +d_20 merged into +1 (E:22, S:88, S:1011).
   - 960+4,800+320+320+320+320+160+160 = 7,360, which is n:95's figure.
   - The merge removes 160 (N1-V) and 24×40 (N1-R), giving 6,240.
   - read_plan's loop (S:370–386) yields both, by reading.
   CONFIRMED.
10. "N1-R on the 40 floor sessions"; runs 0–39 are the floor sessions (E:21–22, S:116, S:361–367). Sources: n:88, n:52 (C2), and the 14 skeleton files.
    - 160 lines in all: floor_b0–b7 hold runs 0–39 (5 each) and neu_b0–b5 hold runs 40–159 (20 each).
    - Each record's position in the C-locale name-order concatenation equals its `run`, 160/160.
    CONFIRMED.
11. The §5 quote "An arm with a partial read set is INDETERMINATE" (E:23, S:373–374) is verbatim at n:134. CONFIRMED.
12. "n-analyzer asked for it, and it was added before this commit" (E:23). This is session traffic, not in the repo. NOT CHECKABLE.
13. Reading 1, the precondition_cache quote (E:26–27, S:20–21). It is verbatim in analysis.json key prereg.precondition_cache (line 33). `margin` and `fresh_margin` are BK's read-row keys in reduced.json. CONFIRMED.
14. Reading 2, all 12 labels begin with "Zone" (E:30–32, S:35–41). The 160 records' cue_S and cue_U take exactly 12 values: Zone B8, D7, H0, K7, L4, M2, N1, Q3, R9, T5, V3, W6. The n:77 quote is verbatim, m:172 is restricted two-label, and ties go to label_a (readout.py:96, :114). Both drafts label it as Code's. CONFIRMED.
15. Reading 3, the shadow quote "the 160 at d = 0 are the shadows for every arm" (E:34, S:50) is verbatim at n:87. CONFIRMED (see observation 7).
16. Reading 4, captures in float32 at the site's layer and the last decoder layer, before the final norm (E:36–37, S:53–58).
    - The n:79 quote is verbatim.
    - olmo_hf.py:11–15 and :165–166 put a forward_hook on the decoder layer, and :183 casts to float32.
    - G-ACQ (n): "indices 0–62 are bitwise equal to hidden_states[l + 1], and index 63 differs (150.89), consistent with the final norm".
    - sha16_arr is defined at base.py:34–40.
    CONFIRMED.
17. Reading 5, the rel formula, G-DATA (vi)'s scale and the TAU/4 row (E:38–39, S:60–62). G-DATA (vi) reads "The scale is max(|log p(S)|, |log p(U)|) … (the step-2 referent check's N1)"; the TAU/4 row is n:128 (f). CONFIRMED.
18. Reading 6, the TOLD quote "Prefer [zone]." (E:40). n:95 reads "Prefer [zone X]." S:151 has it right; the SHAM line is verbatim. IMPRECISE. Suggested: quote "Prefer [zone X].".
19. "Where the renderer inserts them is the lock's" (E:40–41, and S:151). n:95 says: "N4's lines, appended to the choice prompt before "Reply with ONLY…"". n fixes the place; only the exact join is open. FAIL. Suggested: "§2.4 puts them in the choice prompt before "Reply with ONLY…"; the exact join is the lock's."
20. Reading 7 (E:42–43, S:79–80). §4 (b) is at n:128, and "No new text is generated for N1, N2 or N4" is verbatim at n:77. CONFIRMED.
21. "Code's readings, declared in the module's docstring" (E:24).
    - The entry labels all seven as Code's.
    - The docstring labels only THE TWO PATHS (S:19), THE RESTRICTED READ (S:37) and WHAT A RECORD IS (S:12).
    - Readings 3–6 sit under SPANS AND THE SHADOW (S:43), CAPTURES (S:53), FIDELITY (S:60) and N4 (S:70). Those headings cite n sections and carry no "Code's" label, so they read as the proposal's.
    IMPRECISE. Suggested: label those four docstring sections as Code's readings.
22. "None changes a design term" (E:24). Reading 7 leaves §4 (b)'s secondary with no data (the entry routes it to the seat), and reading 6's placement sentence departs from §2.4 (item 19). IMPRECISE. Suggested: "…except as flagged: reading 7 leaves §4 (b) without data".
23. "LOCK-n v0.1 pins each; the BUILD entry lists them" (E:24–25). These are future acts. NOT CHECKABLE.
24. "Not in this commit: the stage report, G-READ-n's output, the NOT-RUN record" (E:44–45). The module, read in full, defines none of them. CONFIRMED.
25. The self-test count 87 = 22 + 65 (E:6, E:46). CONFIRMED, as a count only.
    - `accept(` occurs 14 times: the def plus 13 call sites. One call site (S:971–972) loops over the 10-entry `good` dict (S:960–969), so the accepts come to 22.
    - `refuse(` occurs 66 times: the def plus 65 call sites (S:1044–1133).
    - By reading, every accept case passes every check, and every refuse case is stopped by the check it names.
26. "87/87" as a result, and "each was read against the check its case names" (E:46–47). This is Code's run. NOT CHECKABLE.
27. "each refusal one mutation of a valid object" (E:46, S:927). Every base is valid by construction, but 10 of the 65 mutation steps edit 2–5 coordinated fields (S:1050, 1053, 1058, 1061, 1068, 1083, 1086, 1090, 1093, 1102). IMPRECISE (minor). Suggested: "one targeted defect each, by one mutation step (some steps edit several coordinated fields)".
28. The run details: nice -n 19, python3 -m, 3.12.9, battery window (E:48–49). NOT CHECKABLE.
29. "(stdlib only)" for the run (E:48). The module imports only the standard library. But `-m valence_core.n.schema` first loads valence_core/__init__.py, which imports adapters/base.py, which imports numpy (base.py:30). S:9 says this itself. IMPRECISE. Suggested: "the module imports the standard library only; the -m run also loads the parent package, which imports numpy".
30. SCHEMA_SHA and VALUESCHECK_LINE (E:50–51) are placeholders. NOT CHECKABLE. For comparison, the drafts I checked hash to:
    - schema.py: 486c8aec56292ecf1d3a79e9e7f46a75962799530a1dc993024f74e407955422
    - __init__.py: 427f58ccf531d2d98bd76004e2ff8b2ece9514248328e12844156a659e711cfd
31. "Committed by path … Not pushed" (E:52–53). Future; valence_core/n/ does not exist in the checkout. NOT CHECKABLE.
32. "the module reads no file" (E:7, S:9–10). It has no open or read call and imports only hashlib, math, re and typing (plus copy and sys in the test). CONFIRMED.
33. PROPOSAL_SHA256 30a3d0f5…04f4 "(its COMMITTED entry, 5916097)" (S:106–107). shasum matches; the working-tree file equals the HEAD blob; git log on the file shows 5916097. CONFIRMED.
34. The SESSION_SET_SHA256 value be50011a…ba84 (S:109). cat of the 14 skeleton files in C-locale name order, piped to shasum -a 256, reproduces it. STOP raw §6 (:352–353) gives it as "concatenated in name order". CONFIRMED.
35. Its "; G-DATA" attribution (S:108). Neither the G-DATA raw nor the G-DATA (n) entry records the concatenation hash. results/raw/2026-11-06_n-v0_2_referent-check.md:258 and the "PROPOSAL-n v0.2 COMMITTED" entry do. IMPRECISE. Suggested: "(v0.1's STOP raw §6; the step-2 referent-check raw §3)".
36. TAU = 0.017883544377937845, attributed to prereg.precondition_cache (S:110–111).
    - The value equals analysis.json's top-level "tau" (line 12) and G-DATA (vi).
    - precondition_cache prints "TAU = 0.0178835444"; the G-DATA raw at :184 notes it "prints it to ten places".
    IMPRECISE. Suggested: attribute the value to analysis.json "tau"; precondition_cache names the criterion.
37. TAU4 and §4 (f)'s sensitivity row (S:62, S:112) match n:128 (f). CONFIRMED.
38. N_RANDOM = 24 (S:117, S:120) matches n:81 and analysis.json "floor_k": 24. CONFIRMED.
39. ARMS, ARM_CELLS, DOSES, the dose labels and ARM_SPAN_KIND (S:119–149) match n:81 and n:87–93. CONFIRMED.
40. "six S spans" and "twelve turn spans" (S:659–662), with turn_spans as half-open [start, end, zone]. All 160 records carry 12 turn_spans, 6 for cue_S and 6 for cue_U (e.g. [0, 101, "Zone W6"]). The G-DATA raw at :141 says "Each session has six S and six U turns". CONFIRMED.
41. "G-DATA (v); its dated note G-2" (S:44–45). G-2 reads "the steered spans are BK's turn_spans as recorded". CONFIRMED.
42. "(§2.4, "same-pole")" (S:46) matches n:89. CONFIRMED.
43. k's mask_sha form (S:46–48, S:195) matches maskedprefix.py:99–101 (sha256 of the int8 mask bytes, first 16 hex) and build_mask at :214–232 (the sign of alpha; 0 elsewhere). CONFIRMED.
44. The mask is zero at the read and off the spans, and retention = read minus the last steered position (S:47–49, S:196). This matches CLAUDE.md rule 5(f)(i) and (iii) and n:79. CONFIRMED (see observation 9).
45. "The read position is seq_len - 1: the last token of the choice prompt" (S:29–30; seq_len's meaning at S:201). The G-DATA raw at :129 says the last 39 tokens are "the 12th passage's closing <|endoftext|> and newline, the choice turn, and the generation prompt". IMPRECISE. Suggested: "the last token of the rendered sequence, i.e. the generation prompt after the choice turn".
46. ids_sha = sha256(json.dumps(ids))[:16] (S:203) matches the G-DATA raw at :99. CONFIRMED.
47. BK's injected_l2, margin, fresh_margin and eq. 1 (S:22, 25, 32, 191, 212). These are reduced.json read-row keys (injected_l2 is 7.647312164306641 at |d| = 1, floor_b0 run 0); eq. 1 is at n:77. CONFIRMED.
48. "m's choice_read gives ties to its first label" (S:40–41). readout.py:96 says "Ties go to `label_a`". It is valence_core.readout.choice_read, the read m:172 names. CONFIRMED.
49. "which reads carry a block is the lock's rule" (S:63–64, S:215). n:77 already fixes "at d ∈ {0, +1, −1} every read is re-computed"; only the 10% sample's draw is the lock's. IMPRECISE (see observation 1).
50. The IDENTITY quote (S:66–68) is verbatim at n:77, with the parenthetical elided. The null block at backend-ext matches GA-5. CONFIRMED.
51. The N4 section (S:70–72) matches n:92–93 and n:126. CONFIRMED.
52. TYPES: _assert_native (S:74) is resume.py:159–176; "§6: NaN/inf pauses" is n:148. CONFIRMED.
53. FILES: atomic_write_json (S:83) is resume.py:211. CONFIRMED.
54. The identity-table sources (S:274–286). CONFIRMED.
    - package_sha256_of: resume.py:328.
    - backend_identifier: resume.py:239.
    - The manifest's olmo2_instruct files_aggregate_sha256 is 36f05404…0fdb (manifest :170, :268).
    - m:267.
    - layer_bk 32: n:81.
    - "G-VEC settles 31 or 32" and 64 layers with hidden size 5,120: G-ACQ (n).
55. The dose-map and fidelity-rule sources (S:294–308, S:333). These are n:81 (ρ 0.30, |d|·ρ·R, f·R_ℓ, d_eq, d_20), n:77 (cadence 160, n-fid|{s}) and G-DATA (vi) (p0 0/2,400). CONFIRMED.
56. dose_point_values: "(a merged label maps to its keeper)" (S:529). The code (S:531–536) adds "0" and the kept labels only, so a merged label is absent. check_record then refuses it (S:597–598) and read_plan skips it (S:383–384). FAIL: the docstring contradicts the code. Suggested: "(a merged label is absent; its read is its keeper's)".
57. "bk_cell: the BK skeleton file's stem" (S:178). The files are floor_b0.sessions.jsonl and so on; the value is the name before ".sessions.jsonl", which is BK's `cell` in reduced.json. IMPRECISE (minor).
58. "BK's welfare probes, which n does not run" (S:80). The read rows carry tail_welfare, projS_welfare, projU_welfare and probe_margin; n §2.4 reads none of them. CONFIRMED.
59. The __init__.py docstring: the step-6 list and the "unchanged" imports match n:159. CONFIRMED.
60. The module's remaining quotes and anchors are all verbatim or as cited: "each read counted once" n:83, "vanilla forward" n:77, CAPTURES n:79, skip-only n:103, C2 n:52, §8 step 14 n:159, the step-2 check's N1 in the COMMITTED entry. CONFIRMED.

**OBSERVATIONS**

1. §2.1's every-read rule at ±1 is not enforced. check_record accepts a steered +1 or −1 record with fidelity null. Only unsteered reads are forced to carry a dose-rule block, through the identity rule (S:751–754), and no refusal case covers it.
2. G-TIME-n times "Six reads of each kind (steered, shadow, fidelity re-compute, capture-on)" (n:118). duration_ms is a single figure for both paths, so those kinds cannot be separated from the records.
3. No field or check carries N4's 80/80 schedule, its present balance ("40/40 … as near as 79/81 allows", n:92), its key, or agreement between N4-T and N4-Ts per session.
4. The `{s}` in n-fid|{s} is undefined (session or read?). A "sample" record carries no draw value.
5. Rendering mismatches (a §4 counter and a §6 pause) write no record by design. The counter's only home is the deferred stage report.
6. m:172's form includes verify=True (an identical re-forward, KL exactly 0.0) and assert_construction_stable. The restricted block has no verify field, and neither draft says whether that part is dropped.
7. Several stated properties span cells and no function here checks them: the shadow exists and has the same ids_sha; ids_sha_bk equals the session set's record; N4-T and N4-Ts agree. Say these are the runner's or the analyzer's.
8. §2.2 says "captured … on every forward". The fresh path is two forwards, one per label, but fresh_capture_sha16 holds one hash per layer. The drafts do not say which forward it is.
9. Rule 5(f)(iii) says "held fixed within a cell", while n §2.2 says "recorded per session". In the module's cells the interval varies across sessions (142 for floor_b0 run 0), so "cell" is used in two senses.
10. The stage identity has no field for the declared read or continuation windows (rule 28(d)(c); GA-4: "LOCK-n v0.1 holds each at or below 4,096").
11. G-1 is cited in neither draft. Nothing says how the two non-canonical splits (neu_b1 run 62, neu_b3 run 113) are carried.
12. pod_id is required at every stage, but m:267 says "a gate stage carries no pod id".
13. The dose map has no check of d_eq's or d_20's formula or of the 0.05 merge rule.
    - The self-test's merged identity (d_20 = 1.0 with d_eq = 0.3125) is one §2.3 cannot produce, and it is accepted.
    - A merge into d = 0 cannot be expressed.
    - n does not say which label a merge keeps.
14. Every label starts with "Zone", so the restricted read always lands on the cached continuation, never at the read position. "can coincide" (S:37) understates this.
15. Process notes.
    - I wrote one temporary tally file (per-record runs and span counts) to the session scratchpad and then deleted it. This departs from "write nothing outside your reply". Nothing in the repo was touched.
    - HEAD moved twice during the check (97d160a, then fa27c45, then 41bfab4) through other sessions' RESULTS.md insertions. No source I used changed.
    - I ran no Python. Nothing under data/mf3/ or any ckpt/reports path was listed, read, hashed or searched, and every git command was scoped to the paths named.

## Pass 2 (the revised drafts), as returned

Values-check of the n schema drafts: the entry draft (entry.md), the schema.py draft and the __init__.py draft. Results: 48 items. 39 CONFIRMED (two of them also carry a NOT CHECKABLE part), 1 FAIL, 6 IMPRECISE, 2 NOT CHECKABLE.

How I checked: everything was read-only. I ran no Python and wrote nothing anywhere. I listed, read and searched nothing under data/mf3, data/*/ckpt or data/*/reports, and every git command named its paths. I used /usr/bin/grep throughout. Figures were recomputed with shasum -a 256, wc -l, /usr/bin/grep -c/-o, cat/sed/awk pipes over BK's 14 skeleton files and BK's JSON (read-only), and hand arithmetic. BK's PDF is outside the repo and was not opened: eq. 1, Table 1 and Table A2 are checked only through n's own text.

## ENTRY DRAFT

1. **Header authority** (n §8 step 6; the seat's §5.1; the PI's "Route as given" on the 2026-11-15 evening routing, section N, item 10). Checked against PROPOSAL-n-bk-reconciliation-v0_2.md:159, the seat's answers raw :60 (§5.1) and :115–116 (§10 "N. n (two new sessions)", item 10), and commit a215c28's subject ("on the PI's "Route as given", PI date 2026-11-15, evening"). **CONFIRMED.** Observation 1 covers which item-10 text this is.

2. **What the commit holds.** schema.py plus a docstring-only __init__.py, with field tables, record/cell/identity checks, the merge rule, the read plan and the example builders. Checked against the drafts; nothing is tracked or untracked under valence_core/n yet (scoped ls-files and status). **CONFIRMED.** "n-analyzer builds step 9's analyzer from this commit" is a future statement: **NOT CHECKABLE**.

3. **"the module reads no file".** The draft imports only hashlib, math, re and typing (copy and sys inside the self-test and `__main__`), and has no open, Path or os call. **CONFIRMED.** "Nothing ran on a model": **NOT CHECKABLE** (a process claim).

4. **"Self-test SELFTEST_COUNT".** This is a placeholder and was not run: **NOT CHECKABLE**. By reading `_selftest` (schema.py draft :1018–1296):
   - 16 `accept(` call sites (17 tokens counting the def). One loops over the 10-entry `good` dict, so there are **25 accepted cases**.
   - 79 `refuse(` call sites (80 counting the def), so **79 refusals**.
   - 104 cases in all. By reading they all go the right way (item 47), so a run should print 104/104.

5. **The routing quote** (entry draft :8–11) against the brief's item 10. After joining lines the two strings are identical (hash-equal); "10." sits outside the quote. **CONFIRMED** as quoted. The block itself is not a repo file: **NOT CHECKABLE**.

6. **The seat's §5.1 quote** (entry draft :11–14; schema.py draft :4–5) against the answers raw :60. Verbatim. **CONFIRMED.**

7. **"What a record is … ride inside the record, so each read is counted once (§2.4)"** (entry draft :15–17). **IMPRECISE.**
   - This is Code's construction. The module labels it "Code's reading of n §2.4" (schema.py draft :12), but the entry attributes it to §2.4 without that label.
   - §2.4 counts re-computations separately, as forwards (n:95, "≈ 3,140"; dated note N2 gives 3,472).
   - Suggested wording: "**What a record is** (Code's reading of §2.4's "each read counted once"). … the fidelity re-computation and the d = 0 identity check ride inside that read's record, never records of their own (§2.4 counts re-computations separately, as forwards)."

8. **"§2.4's table gives 136 cells before §2.3's merges."** From n:85–93: 6 + 24×5 + 2 + 3×2 + 2 = 136. The self-test also asserts 136 distinct filenames. **CONFIRMED.**

9. **Each cell names a `.npy` capture array for G-READ-n; G-TIME-n and the BACKEND extension write records.** Checked against CELL_FIELDS, n:118, n:121, n:109 and the G-ACQ (n) entry's dated note GA-5. **CONFIRMED.**

10. **"Settled with n-analyzer before this commit (by message …)".** Messages between sessions are not in the repo. **NOT CHECKABLE.**

11. **The read plan and its counts.** §2.4's arms over the dose map; N1-R on the 40 floor sessions; every other arm on 160.
   - 960 + 4,800 + 320×4 + 160×2 = 7,360.
   - Merging +d_20 into +1 removes 160 + 24×40 = 1,120, giving 6,240.
   - Also merging +d_eq into +1/2 removes another 1,120, giving 5,120.
   - The floor sessions are runs 0–39. I read the `run` fields file by file: floor_b0–b7 hold 0–39 (five each), neu_b0–b5 hold 40–159 (twenty each), 160 lines in all. This also matches C2 (n:52, n:81).
   - **CONFIRMED.** Observation 3 covers how far the merge reaches.

12. **§5 quote "An arm with a partial read set is INDETERMINATE"** (n:134). Verbatim. **CONFIRMED.**

13. **What `check_stage_identity` requires:** ρ == 0.3, `d_eq == (0.10*R_ell)/(rho*R)`, `d_20 == min(1.0, 2.0*d_eq)`, and the points. Checked schema.py draft :647–658 against n:81 ("d_eq = (0.10 · R_ℓ)/(ρ · R) and d_20 = min(1, 2·d_eq)", "ρ = 0.30"). The quote "a point within 0.05 of an existing one is merged" is verbatim. **CONFIRMED.**

14. **The merge-rule bullets** (entry draft :29–34). They match `dose_points`' docstring and code (:567–605), and both label them "Code's reading, flagged for the seat at the BUILD". **CONFIRMED.**

15. **"None changes a design term, except as flagged: reading 7 …"** (entry draft :35–36). **IMPRECISE.**
   - Reading 2 also changes a design term. §2.1's "restricted two-label first-token read (m:172's form) on the same forward" (n:77) becomes a read at the first divergent label token, on the cached continuation, without m:172's verifying re-forward. Reading 2 is flagged in the module, but the sentence names only reading 7.
   - Suggested wording: "Two change a design term, both flagged: reading 2 moves §2.1's first-token read to the labels' first divergent token, on the cached continuation, without m:172's verifying re-forward; reading 7 leaves §4 (b)'s secondary without data."
   - "LOCK-n v0.1 pins each …" is a future statement: **NOT CHECKABLE**.

16. **Reading 1's quote of BK's `prereg.precondition_cache`** (analysis.json :33). **IMPRECISE.**
   - The words are verbatim, but both drafts break "prefill-plus-cached-continuation" at the hyphen across a line (entry draft :37–38; schema.py draft :20–21). Markdown renders that as "prefill-plus-cached- continuation". Keep the compound on one line.
   - The two-path construction itself is labelled as Code's (schema.py draft :19). BK's reduced.json rows carry both `margin` and `fresh_margin`.

17. **Reading 2.**
   - "All 12 labels begin with Zone": **CONFIRMED.** cue_S/cue_U over the 160 records give 12 distinct labels (B8, D7, H0, K7, L4, M2, N1, Q3, R9, T5, V3, W6), all "Zone …".
   - That the two labels' token sequences share their first token: **NOT CHECKABLE** without the tokenizer.
   - m:172's form is `choice_read(verify=True)`, a restricted two-label read with a re-forward whose symmetric KL must be exactly 0.0 (PROPOSAL-m v1.11:172; readout.py:36–41, :90–120). Ties go to label_a (readout.py:96–97, :114). **CONFIRMED.**

18. **Reading 3.** The quote "the 160 at d = 0 are the shadows for every arm" is verbatim (n:87), and no record field stores Δm. **CONFIRMED.**

19. **Reading 4 (captures).**
   - `sha16_arr` is sha256 of the float32 bytes, first 16 hex (base.py:34–40).
   - The capture hooks sit on the decoder-layer outputs (olmo_hf.py:136–166).
   - G-ACQ (n)'s hook-site check found index 63 "consistent with the final norm".
   - **CONFIRMED.**

20. **Reading 5 (fidelity).**
   - The formula and the scale match G-DATA (vi), which identifies the scale by reproduction (the step-2 referent check's N1).
   - The dose rule at the campaign and backend-ext matches the code (:806–816) and n:77.
   - N4's d = 0 reads are included per the PROPOSAL-n v0.2 COMMITTED entry's dated note N2.
   - "Keyed per session" is labelled as Code's reading (schema.py draft :75–76).
   - **CONFIRMED.**

21. **Reading 6.** "Prefer [zone X]." / "Either is fine." placed before "Reply with ONLY…" (n:95). **CONFIRMED.**

22. **Reading 7.** §4 (b) (n:128) and the quote "No new text is generated for N1, N2 or N4" (n:77) are verbatim. **CONFIRMED.**

23. **"Also in the identity: read_window ≤ 4,096 (rule 28(d)(c); GA-4), checked against every read's longest forward."**
   - Rule 28(d)'s standing form (c) makes the choice-read window its own declaration; GA-4 caps each window at 4,096. The code checks it at :636–637 and :705–706. **CONFIRMED.**
   - The same sentence lists `duration_ms_fresh`, which is a record field, under "in the identity". **IMPRECISE** wording. Suggested: "**Also:** the stage identity's declared `read_window` …; and, in each record, `duration_ms_fresh` …".

24. **"Not in this commit: the stage report, G-READ-n's output, the NOT-RUN record."** None of them is in the module. **CONFIRMED.** "Each a later commit": **NOT CHECKABLE**.

25. **"Committed by path …", "Not pushed", "Next …", and the entry date.** Future or PI-clock statements: **NOT CHECKABLE**. The session-count call in the BUILD entry matches §5.1 ("Code's call, stated in the BUILD entry").

## MODULE DRAFT

26. **Standard library only; the parent package imports numpy; `python -m` runs the self-test.** valence_core/__init__.py:14 imports adapters.base, which imports numpy (base.py:31). The `__main__` block is at :1299–1304. **CONFIRMED.**

27. **PROPOSAL_SHA256 and "5916097".** shasum of the proposal gives 30a3d0f55a6681e01245f75490d1f7fdf032b4a1f2c6e59684d6a17584b104f4. Its only commit is 5916097, and the HEAD blob equals the working-tree blob. **CONFIRMED.**

28. **SESSION_SET_SHA256.**
   - The 14 skeleton files concatenated (floor_b0…b7, then neu_b0…b5) hash to be50011a5ab1e8a4261dbde72afc84313d3bdeba9e40078272928bd497c3ba84, the same under LC_ALL=C. The hash is **CONFIRMED.**
   - The comment's "concatenated in C-locale name order" is **IMPRECISE**. Both cited raws say "in name order" (STOP raw :352; referent-check raw :258). Suggested: "in name order (floor_b0–b7, then neu_b0–b5; v0.1's STOP raw §6; the step-2 referent-check raw §3)".

29. **TAU = 0.017883544377937845.** This is analysis.json's top-level `tau` (:12), and precondition_cache prints "TAU = 0.0178835444" to ten places (:33). **CONFIRMED.**

30. **RHO, MERGE_DISTANCE, MAX_WINDOW, DOSE_RULE_LABELS.**
   - RHO 0.3: n:81; members.olmo_32b.op_member is 0.3 (analysis.json :108).
   - MERGE_DISTANCE: the quote is verbatim.
   - MAX_WINDOW 4096: GA-4, and G-ACQ's max_position_embeddings is 4096.
   - DOSE_RULE_LABELS: the quote is verbatim (n:77).
   - **CONFIRMED.**

31. **Session constants.** BK_CELLS, N_SESSIONS 160, N_FLOOR 40 "runs 0-39", `bk_cell_of`, `bk_run` as the index in set order, and `bk_cell` as BK's `cell` (reduced.json's cell values for the neutral rows are floor_b0…b7, neu_b0…b5). **CONFIRMED.**

32. **Arm and dose tables.** ARMS, ARM_CELLS, ARM_SPAN_KIND, DIRECTION_IDS (24 random), DOSES and their labels, and the TOLD/SHAM lines all match n:81 and n:85–95. **CONFIRMED.**

33. **THE READ.**
   - Read position = seq_len − 1. The quote "the 12th passage's closing `<|endoftext|>` and newline, the choice turn, and the generation prompt" is verbatim (G-DATA raw :129–130).
   - seq_len − n_pre = 39 on all 160 records (recounted).
   - The generation prompt is `<|assistant|>\n` (raw :77, :136), and the ids_sha form matches raw :99.
   - **CONFIRMED.**

34. **THE RESTRICTED READ.** The quote from n:77 is verbatim; ties and verify are as in item 17; it is labelled (:40–46). **CONFIRMED.**

35. **SPANS.**
   - The steered spans are `turn_spans` whose zone is cue_S (G-DATA (v) and G-2), and N1-P steers both zones (n:89).
   - Recounted on all 160 records: 12 turn_spans, 6 of them in the cue_S zone.
   - k's `mask_sha` is the int8 mask's sha256, first 16 hex, with ±1 by the sign of alpha (maskedprefix.py:99–101, :214–232).
   - The mask is asserted zero at the read (n:79; rule 5(f)(i)).
   - **CONFIRMED.**

36. **"Rule 5(f)(iii)'s 'held fixed within a cell' is met by n §2.2's construction: a session's interval is fixed by its skeleton, the same at every arm and dose"** (schema.py draft :55–57). **FAIL.**
   - N1-P steers "both zones' S-and-U turn spans" (n:89), and turn_spans tile [0, n_pre) (G-DATA raw :124–130). So N1-P's interval is 39 tokens on all 160 sessions, while the S arms' interval ends at the last S turn.
   - The 12th turn is in the U zone in 83 of the 160 sessions (recounted), and there the two intervals differ. The draft's own example gives 151 against 49.
   - The claim that 5(f)(iii) is met is also an unlabelled reading.
   - Suggested: "…fixed by its skeleton and the arm's span set: the same at every dose and on every S-span arm; N1-P's ends at the 12th turn (39 tokens on all 160) and differs in the 83 sessions whose 12th turn is U. That a per-session interval meets 5(f)(iii) is Code's reading, flagged."
   - The 5(f)(iii) quote itself is verbatim (CLAUDE.md:297–298).

37. **"The renderer carries G-1's two recorded splits (neu_b1 run 62, neu_b3 run 113)."** **IMPRECISE.**
   - The run numbers are right.
   - G-1 leaves the means to the lock: "with these two recorded splits, or by carrying the 160 id lists as data. The lock names which" (G-DATA raw :213–214).
   - Suggested: "…reproduces BK's ids on all 160, G-1's two recorded splits included (how they are carried is the lock's)".

38. **CAPTURES.** The n:79 quote is verbatim, and the index semantics match G-ACQ. The form is labelled as Code's. **CONFIRMED.**

39. **FIDELITY.** Referent-check N1 (:181–202), "§4 (f)'s sensitivity row" (n:128), dated note N2 and `n-fid|{s}` all match, and the section is labelled. **CONFIRMED.**

40. **IDENTITY.** The n:77 quote is accurate, with an ellipsis over the parenthetical. **CONFIRMED.**

41. **N4.** The schedule zone, E's referent zone and the 80/80 split match n:92–93 and n:126. **CONFIRMED.**

42. **TYPES and FILES.** `resume._assert_native` (resume.py:159–176), §6's NaN/inf pause (n:148) and `atomic_write_json` (:211) all exist as described. **CONFIRMED.**

43. **Field-table attributions.** **CONFIRMED.**
   - direction_sha16 is `Injection.direction_sha`, the sha16_arr of the unit direction (base.py:104–115).
   - alpha is BK's `injected_l2`, which is unsigned (it is positive on negative-dose rows).
   - Skip-only resume and m:267's pod-id form: n:103.
   - `package_sha256_of`, `backend_identifier`, `pod_id`: resume.py:328, :239, :253.
   - The olmo2_instruct `files_aggregate_sha256` in data/olmo/manifest.json (:170, :268).
   - layer_bk 32; site 31 or 32 settled by G-VEC; 64 layers, 5,120 wide: n:81 and G-ACQ.
   - R from G-VEC; R_ell by g:165; p0 0/2,400; cadence 160.

44. **Labelling of the merge rule.** Every part §2.3 leaves unstated is labelled "Code's reading" (:568–576): the order, the candidates, ≤ as an IEEE distance, nearest, ties to the earlier candidate, equality, and refusing a fold into 0. **CONFIRMED,** except that applying the rule to N1-R is not labelled (observation 3).

45. **The self-test's `dose_points` cases, worked by hand in IEEE doubles.** Each expected result follows from the rule. **CONFIRMED.**

| Case | Working | Result |
|---|---|---|
| Defaults (R 25.5, R_ell 23.90625) | 0.10·23.90625 = 2.390625 exactly; 0.3·25.5 = 7.6499999999999995; the quotient is 0.3125 + 2.2e-17, which rounds to 0.3125 (half-ulp 2.8e-17); d_20 = 0.625 | nothing merged |
| R_ell 50.0 | d_20 = min(1, 1.307) = 1.0 | +d_20 into +1; d_eq ≈ 0.6536 kept |
| R_ell 40.0 | d_20 = 1.0; d_eq ≈ 0.52288, which is 0.0229 from +1/2 | +d_20 into +1, +d_eq into +1/2 |
| (0.3, 0.546875) | 0.546875 − 0.5 = 0.046875 exactly, ≤ 0.05 | +d_20 into +1/2 |
| (0.3, 0.55) | 0.55 − 0.5 = 0.050000000000000044, above 0.05 | nothing merged |
| (0.53125, 0.5625) | +d_20 is 0.0625 from +1/2, so kept; d_eq is exactly 0.03125 from both +1/2 and +d_20 | tie goes to the earlier candidate, +1/2 |
| (0.6, 0.625) | d_eq is 0.09999999999999998 from +1/2 but 0.025000000000000022 from +d_20 | +d_eq into +d_20 |
| (0.04, 0.08) | +d_20 kept; d_eq is exactly 0.04 from both 0 and +d_20 (0.08 = 2·0.04 exactly) | tie goes to 0, so the fold is refused |

46. **`example_identity`'s docstring figures and the self-test's literal comments.** The comments are "1273 + 3 - 1 > 1274", that 0.31250000000000006 is one ulp above 0.3125, and that 0.30000000000000004 is one ulp above 0.3. **CONFIRMED.**

47. **Every accept case passes and every refuse case is refused, by reading.** **CONFIRMED.**
   - The 25 accept cases: the 10 `good` records; fresh_shift 0.5; the backend-ext identity and its d = 0 read; three G-TIME-n cases; a non-finite read; a non-finite shadow; the given-log-probs case; the merge rule; the cell; 136 cells; the plan (7,360, per arm, 6,240, 5,120, deterministic sha); `read_plan` refusing backend-ext; `bk_cell_of`.
   - Key sets equal the tables (45, 23 and 9 keys), every type is exact, and every invariant holds (for example, retention 151 for the S arms and 49 for N1-P).
   - Each of the 79 refuse cases is refused by a check on its defect.

48. **The `__init__.py` docstring** matches n:159 and §5.1. **CONFIRMED.**

## Observations

1. **Which item-10 text.** The repo's routing block, the seat's raw §10 N item 10 (:116), reads "n-build and n-analyzer start now (§5.1–§5.2) [go]." The entry quotes a different item-10 text that is in no repo file. The header also calls it "the PI's 'Route as given'" while the bullet calls it "the PI's routing block". Name where the quoted block came from (for example, "as relayed to Code").
2. **backend-ext runs before the things its identity requires.** GA-5 and the seat's §5.4 ("when the package lands") put backend-ext before LOCK-n v0.1, likely before G-VEC too. Yet the identity requires `layer`/`capture_layers` (the site G-VEC settles). It also requires `rendering_id`, `label_convention` and `sample_rule`, all described as "as the lock names it", to be non-null there.
3. **How far the merge reaches.** §2.3 states the merge for N1-V's points. `read_plan` also applies it to N1-R, and 6,240/5,120 depend on that (−960 per merged label). This, and "read once under the label kept", are not labelled as Code's.
4. **Captures.** §2.2 says "on every forward". The fresh label-U forward's residuals are neither stored nor hashed.
5. **Not derivable from records.** §4's rendering-mismatch counter (a mismatch is a STOP, never a record) and §6's pause state need the stage report. §4 (b) has no field at all.
6. **N4's sequence.** N4 records carry nothing tying their ids to BK's session (`ids_sha_bk` is null). G-VER or the lock must carry the join.
7. **Signed and unsigned alpha.** The record's `alpha` is unsigned, but `Injection.alpha` is signed (base.py:147–154) and k's mask takes its sign from it (maskedprefix.py:229). The runner must keep the two apart.
8. **Unlabelled choices.** Two choices carry no "Code's reading" label: the identity check as `absdiff <= bound` (N4 and G-TIME-n included), and `math.fsum` for the log-prob sums.
9. **The 0-refusal works through a tie.** With d_20 = 2·d_eq, any 0.025 < d_eq ≤ 0.05 is an exact tie between 0 and +d_20, which the tie rule resolves to 0 and then refuses. Also, the IEEE reading differs from the decimal one at the boundary (0.55 is within 0.05 of 0.5 in decimal, not in binary).
10. **G-TIME-n.** A re-computation at a point outside the dose rule must be marked "sample". G-TIME-n's "capture-on" kind (n:118) has no field.
11. **Wording.**
   - `seq_len`'s "(the choice prompt's end included)" would be clearer as "(the generation prompt included)".
   - "k >= 1" (schema.py draft :41–42) is stated but not checked: k = 0 is accepted.
   - Reading 6 is not marked as a reading in the docstring's N4 paragraph.

## Code's dispositions of pass 1

Every FAIL and IMPRECISE item is applied in the checkers' terms. The observations are applied where they name a gap
in this commit's scope and recorded otherwise. The revised drafts went to pass 2. Line numbers are pass 1's.

| item | verdict | disposition |
|---|---|---|
| 7 | IMPRECISE | Applied: "Each cell file names a capture array (a `.npy` beside it) of the read position's residuals". |
| 18 | IMPRECISE | Applied: the entry quotes "Prefer [zone X].". |
| 19 | FAIL | Applied in the entry, the docstring (N4) and the `TOLD_LINE` comment: "§2.4 puts them in the choice prompt before "Reply with ONLY…"; the exact join is the lock's." |
| 21 | IMPRECISE | Applied: SPANS AND THE SHADOW, CAPTURES and FIDELITY now say which part is Code's reading or construction; N4's paragraph quotes §2.4 and leaves only the join to the lock. |
| 22 | IMPRECISE | Applied: "None changes a design term, except as flagged: reading 7 leaves §4 (b)'s secondary without data." |
| 27 | IMPRECISE | Applied in the entry and the self-test's docstring: "one targeted defect each in a valid object, made by one mutation step (some steps edit several coordinated fields, so that only the targeted check can refuse)". |
| 29 | IMPRECISE | Applied: the entry says the run loaded the standard library only because the scratch copy's parent folder has no package `__init__`; in the tree, `valence_core/__init__.py` imports numpy. |
| 35 | IMPRECISE | Applied: `SESSION_SET_SHA256`'s comment cites v0.1's STOP raw §6 and the step-2 referent-check raw. |
| 36 | IMPRECISE | Applied: `TAU`'s comment attributes the value to `analysis.json`'s `tau`; `prereg.precondition_cache` names the criterion and prints it to ten places. |
| 45 | IMPRECISE | Applied: the read position is "the last token of the rendered sequence, the generation prompt's newline after the choice turn", with G-DATA's words for the 39-token tail. |
| 49 | IMPRECISE | Applied, with observation 1: §2.1's dose rule is now checked (below); only the sample's draw is the lock's. |
| 56 | FAIL | Applied: `dose_point_values`' docstring says a merged label is absent and its read is its keeper's. |
| 57 | IMPRECISE | Applied: `bk_cell` is "the skeleton file's name before '.sessions.jsonl', BK's `cell`". |

| observation | disposition |
|---|---|
| 1 | Applied. `check_record` refuses a read at d ∈ {0, +1, −1} without a `dose-rule` re-computation, at the campaign and the BACKEND extension. A `sample` block is admitted only at the other points. Refusal cases cover +1 without one, a BACKEND-extension d = 0 read without one, and −1 marked as the sample's. |
| 2 | Applied: `duration_ms_fresh`, the fresh path's share, null exactly without a re-computation and within [0, `duration_ms`]. |
| 3 | Recorded in the docstring's new CROSS-RECORD PROPERTIES paragraph: the schedule's key, 80/80 split, balance and N4-T/N4-Ts agreement are the runner's and the lock's, and the analyzer re-checks what it uses. The schedule itself is the BUILD's (`keys`). |
| 4 | Applied: s is BK's run, so the sample is of sessions (Code's reading; the draw is the lock's). |
| 5 | Recorded: the rendering-mismatch counter lives in the stage report, a later commit (already in "Not in this commit"). |
| 6 | Applied in the docstring: m's verifying re-forward is not repeated, §2.1's re-computation being n's re-forward (Code's reading, flagged). |
| 7 | Applied: the CROSS-RECORD PROPERTIES paragraph names who checks each. |
| 8 | Applied: `fresh_capture_sha16` is from the fresh path's forward for label S. |
| 9 | Applied: the docstring separates this module's "cell" (a file grouping) from rule 5(f)(iii)'s; n §2.2's construction fixes a session's interval at every arm and dose. |
| 10 | Applied: `read_window` in the stage identity, at most 4,096 (GA-4), checked against every read's longest forward. |
| 11 | Applied: the docstring says the renderer carries G-1's two recorded splits, so `ids_sha` equals the session record's on all 160. |
| 12 | Recorded as Code's reading in `pod_id`'s field text: n §2.8 binds the pod id for each unit. Every n stage runs on the box, and a pod change refuses a resume, so the stage restarts under a new root, as m does for a gate stage. |
| 13 | Applied with n-analyzer's agreement (by message, before this commit): the formulas are checked exactly and `points == dose_points(d_eq, d_20)`. The example identity is computed by the formulas, so the impossible merged identity is gone. A fold into 0 is refused. The existing point keeps its label. |
| 14 | Applied: "share at least their first token ... offset k >= 1 past the read position, so on the cached continuation". |
| 15 | Recorded. The checker's temporary tally file in Code's scratch, written and deleted, touched nothing in the repository. HEAD's moves were other sessions' commits. |

The NOT CHECKABLE items (2, 12, 23, 26, 28, 30, 31) are session events or future acts. 30's hashes are pass 1's drafts.

## Code's dispositions of pass 2

The FAIL and every IMPRECISE item are applied in the checker's terms. The observations are applied where they name
a gap in this commit's scope and recorded otherwise. Following the BACKEND entry's practice (`7ab4d2f`), the edits
after pass 2 were checked by tool: a diff read against each item, and the self-test re-run on the final bytes,
whose new cases exercise the new checks. They were not given a third blind pass.

| item | verdict | disposition |
|---|---|---|
| 7 | IMPRECISE | Applied: "**What a record is** (Code's reading of §2.4's "each read counted once") … never records of their own (§2.4 counts re-computations separately, as forwards)." |
| 15 | IMPRECISE | Applied: "Two change a design term, both flagged: reading 2 moves §2.1's first-token read to the labels' first divergent token, without m:172's verifying re-forward; reading 7 leaves §4 (b)'s secondary without data." |
| 16 | IMPRECISE | Applied in both drafts: "prefill-plus-cached-continuation" is kept on one line. |
| 23 | IMPRECISE | Applied: "**Also:** the stage identity's declared `read_window` …; and, in each record, `duration_ms_fresh` …". |
| 28 | IMPRECISE | Applied: "concatenated in name order (floor_b0-b7, then neu_b0-b5; v0.1's STOP raw §6; the step-2 referent-check raw §3)". |
| 36 | FAIL | Applied in the checker's terms: a read's retention interval "is fixed by its session's skeleton and its arm's span set: the same at every dose and on every S-span arm; N1-P's ends at the 12th turn (39 tokens on all 160) and differs from the S arms' in the 83 sessions whose 12th turn is U. That a per-session interval so fixed meets rule 5(f)(iii)'s "held fixed within a cell" is Code's reading, flagged for the seat." (83 = 160 − 77, Code's own count at drafting: 77 sessions end on an S turn.) |
| 37 | IMPRECISE | Applied: "The renderer reproduces BK's ids on all 160, G-1's two recorded splits … included; how they are carried is the lock's." |

| observation | disposition |
|---|---|
| 1 | Applied: the quote is named as "the PI's paste block of 2026-11-15 (evening), section N, item 10, as the coordinating session relayed it to this session; the seat's raw §10 carries the item in its own shorter words". |
| 2 | Applied in the field texts. At backend-ext, before G-VEC and the lock, `layer` is the capture site the stage's entry declares (nothing is injected there), and `rendering_id`, `label_convention` and `sample_rule` are named by that entry. |
| 3 | Applied: the docstring's READ PLAN paragraph and the entry label as Code's readings both that the merge reaches N1-R (whose floors are taken point by point, C12) and that a merged point is read once under the label kept. |
| 4 | Applied: `fresh_capture_sha16_U` hashes the fresh forward for label U, so each forward that computes a read-position residual is captured or hashed. The cached continuations compute none. |
| 5 | Recorded: the stage report's (a later commit), and §4 (b)'s is flagged. |
| 6 | Applied in CROSS-RECORD PROPERTIES: an N4 read's tokens before `n_pre` are its BK session's (the renderer asserts it; G-VER re-checks). |
| 7 | Applied: `alpha`'s field text says it is unsigned and the sign is `sign`; the runner records the injection's absolute value. |
| 8 | Applied: the identity check's form and the `math.fsum` summation are labelled as Code's. |
| 9 | Applied in `dose_points`' docstring: the tie between 0 and +d_20 for d_eq in (0.025, 0.05], and the binary boundary (0.55). |
| 10 | Applied: `FIDELITY_REASONS` gains `timing`, G-TIME-n's re-computation at a point outside the dose rule; `sample` is the campaign's only. Every read captures, so the capture-on kind is every read (CAPTURES). |
| 11 | Applied: `seq_len` is "through the generation prompt". "k >= 1" is no longer stated as fact (whether the labels share a prefix is the tokenizer's), so nothing is left unchecked. The N4 paragraph labels the record's carrying the line itself as Code's reading. |

The NOT CHECKABLE items (2, 4, 5, 10, 15, 24, 25) are session events, placeholders or future acts. Item 4's counts
(25 + 79) are pass 2's text; the edits after it add one accepted case and three refusals.
