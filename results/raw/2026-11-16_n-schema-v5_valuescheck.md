# n — the schema's follow-up commit (v5): the blind values-check

*The n-build session (Code), PI date 2026-11-16.*

- **What was checked:**
  - the change to `valence_core/n/schema.py` from v4.4 (`4bed3f9a…4665`, at `14e65d8`) to the v5 draft
    (`33419938…111d`), as a unified diff;
  - the entry (`1f46d107…4ee4`), whose values-check line was then a placeholder;
  - the close line on `718c48e`'s entry (`9325f6ef…14de`).
- **The checker:** one blind pass by a fresh agent. Its brief quoted the list of record v2's items 1–5 verbatim with
  the coordinating session's lines, and added: no Python, no guard marker in any argv, no writes, no token id.
- **Its report** came back as the agent's hand-back message. Code extracted it with `jq` into this raw, unedited:
  112 lines, sha256 `ca85544c…ddf0`. Its paths are the checker's, with S for Code's scratch folder of check
  materials. It cites the v5 draft as V5:line.
- **The counts:** 64 items: 45 CONFIRMED, 11 IMPRECISE, 0 FAIL and 8 NOT CHECKABLE.

## The checker's report, as returned

Values-check of D (S/schema_v5.diff, cited as V5:line in S/schema_v5.py), E (the entry) and C (the close line on 718c48e's entry).

**Totals:** 64 items: 45 CONFIRMED, 11 IMPRECISE, 0 FAIL, 8 NOT CHECKABLE.

**Method.** No Python was run and nothing was written. The texts were scanned for clock times, local paths, addresses and token ids, and nothing in data/n/ids was opened. Hashes were taken with shasum and abbreviated with cut. The diff's body was re-derived with `diff -u` and is identical to D. Quotes were matched as fixed strings with whitespace collapsed. Plan counts and storage were computed with shell arithmetic.

**E — the entry**
1. Hashes: v5 is `33419938…111d`, v4.4 was `4bed3f9a…4665` at 14e65d8 (E:2–3). Checked with shasum on both scratch files and `git show 14e65d8:valence_core/n/schema.py | shasum`. HEAD's blob equals 14e65d8's. **CONFIRMED.**
2. Self-test 213/213: 50 accepted, 163 refused (E:3). S/selftest_verbose.txt:1–164 has 163 refusal lines, then "213/213". S/schema_v5.py has 26 direct accept calls plus loops of 10, 7, 5 and 2, which makes 50. Its 163 refuse names match the output in order. **CONFIRMED.**
3. "Nothing ran on a model" (E:3). Consistent with V5:10–11 and RESULTS.md:60–70. **NOT CHECKABLE.**
4. The order and §5 item 2's list (E:1–5). Checked against the answers raw (results/raw/2026-11-16_n-build_design-to-code_answers.md) :58–62, ADDENDUM-n1:84 and RESULTS.md:24. **CONFIRMED.**
5. `capture_layers` is `list(range(layer + 1, n_layers))`, asserted (E:6). V5:817–819; ADDENDUM-n1:54. **CONFIRMED.**
6. One float32 array per layer per cell; capacity 40 for N1-R and 160 otherwise; rows written in place (E:7–9). V5:76–79, 417–419, 506–510. **CONFIRMED.**
7. "The array form and the row hash are Code's, for I/O" (E:10–11). **IMPRECISE.**
   - The seat's own words (answers raw :41; ADDENDUM-n1:54) fix "one array per cell per layer, each hashed per layer in its cell".
   - V5:79 labels only the in-place row form as Code's.
   - Suggested wording: "One array per cell per layer, hashed per layer, is the seat's (§2.5; ADDENDUM-n1 §6.2). The capacity rows written in place, and the hash's byte form (rows [0, capture_rows), float32 little-endian, row order), are Code's, for I/O."
8. "The report's and G-READ-n's artifact's cell entries carry the same maps" (E:12). **IMPRECISE.**
   - They carry the per-layer `capture_sha256` map only: V5:1107–1109, 1181, 1227, 1235–1236. Neither carries `capture_files`.
   - Suggested wording: "…carry the per-layer `capture_sha256` map."
9. kfold10 with `cv_seed`; PASS at median ≥ .90 and above the largest of the 24; no per-layer condition (E:13–14). V5:1094–1096, 1188–1189, 1509; ADDENDUM-n1:56, 58. **CONFIRMED.**
10. N1-P reads +1, +d_20, +d_eq and −1 under the merge (E:15–16). V5:284; ADDENDUM-n1:46. **CONFIRMED.**
11. "7,680 … 6,400 with +d_20 merged and 5,280 with both merged" (E:17–18). **IMPRECISE.**
    - 7,680 is right. 6,400 and 5,280 hold only for +d_20 merging into +1 and +d_eq into +1/2, which are the self-test's maps (V5:1538–1539, 1824–1825).
    - In v5 N1-P's count depends on where points merge. With +d_20 into +1/2, N1-P keeps four points and the plan is 6,560. With both into +1, it is 5,120.
    - Suggested wording: "…6,400 with +d_20 merged into +1 and 5,280 with +d_eq also merged into +1/2."
12. `check_record` and `check_report` test against `arm_cells` (E:19). V5:852–854, 1342–1350. **CONFIRMED.**
13. Cap: `loads_ms` reported beside and outside it; `used_ms` stays the records' `duration_ms` (E:20–21). Answers raw :50; V5:1155–1158. **CONFIRMED.**
14. Restricted block and pause precedence unchanged, the precedence already the seat's order (E:22). `RESTRICTED_FIELDS`, the restricted checks and `PAUSE_KINDS` (V5:1081) are outside every diff hunk. The order matches answers raw :50. **CONFIRMED.**
15. "…those it did not address stay flagged" (E:23). **IMPRECISE.**
    - The SCOPE pin lost its "flagged": v4.4 had "(its SCOPE pin, flagged)" (S/schema_v5.diff:131–132); V5:155–156 now omits it.
    - The seat ruled only "(the pause stands on its scope's arms; the resume after the ruling continues all)" (answers raw :50). It did not rule which other arms a scope holds, or a read-less fire's scope.
    - Every reading §3 does list now carries the seat's label.
16. Four refusal cases are single-defect and assert their message with `expect=` (E:24–26). V5:1934–1935, 1949–1953, 1955–1959, 2117–2118; output lines 7, 14, 16, 101. **CONFIRMED.**
17. "the three the BUILD review flagged" (E:24). No committed record of that review exists and it is not among the sources. **NOT CHECKABLE.**
18. Items settled with n-analyzer, PIN-n-31, and Code's PIN for step 15 (E:27–31). These were settled by message. n §8 step 15 is "G-READ-n from the captures" (PROPOSAL-n-bk-reconciliation-v0_2.md:159), and the draft valence_core/n/cells.py defines `load_cell`. **NOT CHECKABLE.**
19. "No ADDENDUM-n1 field joins the stage identity" (E:32). The keys of `STAGE_IDENTITY_FIELDS` are unchanged; only the meaning of `capture_layers` changed (V5:448–449). **CONFIRMED.**
20. "flagged for the seat at the BUILD; n-analyzer moves its pin … next" (E:32–33). Future events. **NOT CHECKABLE.**
21. Windows (E:34–35). **IMPRECISE.**
    - RESULTS.md:63–66 says of the second run: "That invocation was not the granted one; the coordinating session found it harmless."
    - Suggested wording: "…213/213 on its second run, a script invocation that was not the granted one, which the coordinating session found harmless."
22. "Committed by path … Not pushed" (E:37–38). Future. **NOT CHECKABLE.**
23. E cites "the seat's raw's §5" and "the seat's §3" without naming the raw. **IMPRECISE.**
    - results/raw holds four `2026-11-16_*_design-to-code_answers.md` files.
    - Suggested fix: link `results/raw/2026-11-16_n-build_design-to-code_answers.md` at E:1.

**C — the close line**
24. Seat's raw sha256 `a49801523a09…ba6151a` (full), committed by path at 52b2c97 (C:2–4). shasum matches; `git show --name-status 52b2c97` shows it added; the blob is unchanged since. **CONFIRMED.**
25. Q1 (a); Q2 (b) struck; Q3 (a); Q4 the comparison (ADDENDUM-n1 §2); Q5 a band (ADDENDUM-n1 §6) (C:5–9). Answers raw :9, :31–44; ADDENDUM-n1:30–58. **CONFIRMED.**
26. Item 8 quoted verbatim from the routing raw committed at a61f13d (C:10–13). One exact fixed-string match at results/raw/2026-11-16_second-sitting_pi-routing.md:28; a61f13d adds that raw. **CONFIRMED.**
27. The follow-up commit carries Q1's block unchanged, Q3's keepers, Q5's band and the amended readings (C:16–17). Checked against the diff, answers raw :61 and routing raw :28. **CONFIRMED.**
28. "Q2 needs no form, since the schema records no reply" (C:18). V5:122–123; there is no reply field. **CONFIRMED.**
29. Q4's comparison runs in the BACKEND extension's session over the label candidates under data/n/ids/ (d76f34f) (C:19–20). Answers raw :37; d76f34f adds data/n/ids/labels.json. **CONFIRMED.**
30. Ledger (77) and (78), quoted verbatim from §4 (C:21–28). Identical to answers raw :54–55 with whitespace collapsed; only the bold markers on "(77)" and "(78)" are dropped. **CONFIRMED.**

**D — the schema's changed text**
31. V5:22, two paths accepted, §3. Answers raw :48 item 1. **CONFIRMED.**
32. V5:22, first citation of "the seat's answers of 2026-11-16, §3": which document? **IMPRECISE.**
    - The path is given only later, at V5:46. The n-ganl raw of the same date also has a §3 ("What moves, and the order").
    - Suggested fix: name the raw at its first use, as V5:3 does for the 2026-11-15 answers.
33. V5:43–53, the restricted read "as the seat ruled" (§2.1; ADDENDUM-n1 §3); no re-forward, "the same ruling". Answers raw :31; ADDENDUM-n1:36. **CONFIRMED.**
34. V5:55–56, shadow by reference accepted. Answers raw :48 item 3. **CONFIRMED.**
35. V5:72–80, the n §2.2 quote is verbatim; read as a band, 31 or 32 layers, one array per cell per layer, capacities. PROPOSAL-n:79; ADDENDUM-n1:54; answers raw :41. **CONFIRMED.**
36. V5:81–82, "about 4.7–4.8 GB over a campaign (ADDENDUM-n1 §6.2's figure)". **IMPRECISE.**
    - That figure is for 7,360 reads (ADDENDUM-n1:54).
    - The arrays as V5 defines them hold 7,680 rows with nothing merged: 157,286,400 B per layer, so 4.88 GB at 31 layers and 5.03 GB at 32.
    - Suggested wording: "about 4.7–4.8 GB at 7,360 reads (ADDENDUM-n1 §6.2's figure); about 4.9–5.0 GB at the 7,680 rows."
37. V5:82–83, kept on the volume, copied before the pod stops, never in git, the lock pins the hash lists. ADDENDUM-n1:54. **CONFIRMED.**
38. V5:89–90, fidelity form accepted. Answers raw :48 item 5. **CONFIRMED.**
39. V5:104–109 and V5:297–298, `told_line` accepted; the join after the first sentence with one space each side. Answers raw :18, :48 item 6; ADDENDUM-n1:22. **CONFIRMED.**
40. V5:122–123, §4 (b) struck (ADDENDUM-n1 §4), and the quoted §2.1 sentence. ADDENDUM-n1:40; PROPOSAL-n:77. **CONFIRMED.**
41. V5:125–128, FILES. Consistent with V5:76–81 and `CELL_FIELDS`. **CONFIRMED.**
42. V5:135–140, the read plan: N1-P's four points, 7,680, the merge reaching N1-R point for point (C12) and N1-P. ADDENDUM-n1:44, 46; answers raw :35; PROPOSAL-n:62. **CONFIRMED.**
43. V5:148–150, "accepted, with PIN-n-20's consequence". Answers raw :50. **CONFIRMED.**
44. V5:153–156, the SCOPE pin. **IMPRECISE.** Same finding as item 15. Suggested wording: "(its SCOPE pin, flagged; the pause stands on its scope's arms, as the seat's answers of 2026-11-16, §3 accept)".
45. V5:156–160, a fired monitor ends the invocation and the resume continues all, accepted; quotes "the arm's launches". Answers raw :50; PROPOSAL-n:148. **CONFIRMED.**
46. V5:163–165, the precedence the seat fixed. Answers raw :50. **CONFIRMED.**
47. V5:169–171, rendering pause and G-VER-STOP accepted; the n §6 and n §3 quotes. Answers raw :50; PROPOSAL-n:119, 148. **CONFIRMED.**
48. V5:179–182, the cap clause as the seat ruled it. Answers raw :50. **CONFIRMED.**
49. V5:200–203, `GREAD_LR` accepted ("k's form and bar" is in §0.10's B3 row); kfold10 replaces loso; `cv_seed` is the lock's. Answers raw :50; PROPOSAL-n:48, 121; ADDENDUM-n1:56. **CONFIRMED.**
50. V5:211–214, comparator accepted, with §5.3. Answers raw :50; ADDENDUM-n1:48. **CONFIRMED.**
51. V5:216–219 and V5:1465–1466, the PASS rule is the seat's; the every-layer clause is not adopted; the n §3 quote. ADDENDUM-n1:58; answers raw :43; PROPOSAL-n:121. **CONFIRMED.**
52. V5:279–280 and V5:284, the comment on N1-P's amended row and the row itself. ADDENDUM-n1:46. **CONFIRMED.**
53. V5:291–293, `KEEPER_CANDIDATES`. Matches `dose_points` (V5:717–746) and the requirement that R > 0 (V5:831–836). **CONFIRMED.**
54. Field descriptions V5:362, 384, 417–423, 448–449, 1114, 1157–1158, 1175, 1188–1189. Each matches its check. **CONFIRMED.**
55. Docstrings V5:492, 499–500, 507: `.L{layer}.npy` and the C2 floor sessions. PROPOSAL-n:52. **CONFIRMED.**
56. V5:715, merge rule accepted. Answers raw :48. **CONFIRMED.**
57. V5:770–772 and 785–787, `keeper` and `arm_cells` docstrings. Match the code at V5:773–796. **CONFIRMED.**
58. V5:1088–1089, 139 names. 6 + 120 + 5 + 6 + 2 = 139. **CONFIRMED.**
59. V5:1094–1095, the ADDENDUM-n1 §6.3 quote. Exact match at ADDENDUM-n1:56. **CONFIRMED.**
60. Messages V5:502, 509, 818–819, 1051–1057, 1349–1352, 1433, 1477. Output lines 67–69, 75–76, 148, 157–159, 163. **CONFIRMED.**
61. V5:1772–1773, the `refuse` docstring for `expect`. Code at V5:1782–1784. **CONFIRMED.**
62. V5:1870, "138 distinct cell files": 6 + 120 + 4 + 6 + 2 = 138. **CONFIRMED.**
63. V5:1895–1896, accept-case name "6,400 with +d_20 merged; 5,280 with both merged". **IMPRECISE.**
    - Same target dependence as item 11.
    - "7,680 reads by §2.4's table, N1-P 640" also omits that the 640 comes from ADDENDUM-n1 §5.2's amended row.
    - Suggested wording: "…by §2.4's table as ADDENDUM-n1 §5.2 amends N1-P's row, N1-P 640; 6,400 with +d_20 merged into +1; 5,280 with +d_eq also into +1/2, N1-P reading +1/2."
64. Other new or changed case names, and the check for IP addresses, ports, local paths, clock times and token ids. **CONFIRMED.**
    - Case names checked: V5:1898, 1934, 1949, 1955, 2032–2045, 2117, 2264–2297. Example: [31, 63] is the old [layer, n_layers − 1]. gr_low's median over 32 layers is 0.96, above 0.615.
    - None of the prohibited items appear in E, C or the file's changed text. Only the diff's own header lines (D:1–2) carry local paths and a clock time.

**Observations**
- Some unchanged text now lags the change:
  - V5:315–317's type list omits `layer_sha256` and `layer_names`.
  - V5:1232's "(cell_filename over ARM_CELLS)" leaves out the keeper names, such as N1-P's +1/2.
  - V5:151–152 says "a point the stage's dose map keeps", but the check is now per arm (V5:1342–1350).
- V5:69–70 ("how they are carried is the lock's") and V5:441 (`rendering_id`, "G-DATA (iv)") predate ADDENDUM-n1 §1. E:32's BUILD flag could name them.
- ADDENDUM-n1:56 counts G-READ-n's fits "in the cap where it runs on the box". V5's cap (`used_ms` from the records, plus `loads_ms`) has no clause for that time.
- Six refuse calls carry `expect=`, including V5:2035–2036 and V5:2279–2282. E names four, which is accurate but not the full count.
- The verbose output carries no file hash, so tying it to `33419938…111d` rests on the case names and counts.
- V5:95–96 still calls the 10% sample keyed per session Code's reading. The seat's §3 item 5 accepted "the fidelity `rel` and its scale", and 5a97527's reading 5 (RESULTS.md:1322–1325) also covered the sample. Whether that acceptance reaches the sample is for the seat to say.
- C:8 omits the seat's "form (b)" for Q4 (answers raw :9). Harmless.

## Code's dispositions

Each IMPRECISE item is applied in the checker's terms unless the disposition says otherwise. Line numbers are the
checked texts'.

- **Item 7, E:10–11.** Applied. One array per cell per layer, hashed per layer, is the seat's (§2.5; ADDENDUM-n1
  §6.2). The capacity rows written in place, and the hash's byte form, are Code's, for I/O.
- **Item 8, E:12.** Applied. The report's and the artifact's cell entries carry the per-layer `capture_sha256` map
  only.
- **Item 11, E:17–18.** Applied. The counts now name their merges: 6,400 with +d_20 merged into +1, and 5,280 with +d_eq
  also merged into +1/2.
- **Items 15 and 44, E:23 and V5:155–156.** Applied. The SCOPE pin keeps "flagged" beside the part the seat accepted.
  E's "those it did not address stay flagged" then holds.
- **Item 21, E:34–35.** Applied: "a script invocation that was not the granted one, which the coordinating session
  found harmless".
- **Item 23, E:1.** Applied. The entry links the seat's raw at its first mention.
- **Item 32, V5:22.** Applied. The docstring names the raw's path at its first citation.
- **Item 36, V5:81–82.** Applied: "about 4.7–4.8 GB at 7,360 reads (ADDENDUM-n1 §6.2's figure), about 4.9–5.0 GB at
  the 7,680 rows".
- **Item 63, V5:1895–1896.** Applied. The accept case's name gives §5.2's amended row and the merges' targets.
- **The observations.**
  - Applied:
    - the field tables' type list names `layer_sha256` and `layer_names`;
    - the cell-name refusal message names `KEEPER_CANDIDATES`;
    - the report paragraph's cell clause is per arm (`arm_cells`);
    - V5:69–70 says the ids of record carry the recorded splits (`d76f34f`);
    - `rendering_id`'s description cites ADDENDUM-n1 §1;
    - the entry names all six refusal cases that assert their message;
    - the close line gives Q4's "form (b)".
  - Not applied:
    - G-READ-n's fits counted in the cap where they run on the box (ADDENDUM-n1 §6.3) concern G-READ-n's own stage,
      not this schema's cap. They go to the BUILD's flags.
    - V5:95–96, the per-session sample, stays flagged; whether the seat's acceptance of `rel` reaches it is the
      seat's to say.
    - The verbose output carries no file hash. The self-test is re-run on the final bytes in its own window, and the
      entry names that run's hash.
- **Items 3, 17, 18, 20 and 22, and the other NOT CHECKABLE items.** No change. They concern the model, a review raw
  not yet committed, messages, and events to come.

## The edits after the check, checked by tool

- **The diff.** From the checked texts to the final ones it holds exactly the dispositions above. The schema has
  9 hunks, all of them text (docstrings, a field description, a refusal message and an accept case's name), and
  no behaviour changed. The entry has 5 hunks besides its placeholders, and the close line 1.
- **The re-run.** The schema's self-test was re-run on the final bytes in a battery window: 213/213, exit 0, no FAIL, 50 accepted and 163 refused, its refusal lines the same as the first run's.
- **Each changed claim,** asserted against its source, one assertion each; all 14 hold:
  1. V5:22 names the raw, and the raw's §3 accepts the two paths;
  2. `d76f34f` commits `data/n/ids/`;
  3. the storage arithmetic, 7,680 × 5,120 × 4 B × 31 and × 32;
  4. `check_report` tests cells against `arm_cells`;
  5. the SCOPE pin keeps "flagged";
  6. the type list names the two map types;
  7. `rendering_id` cites ADDENDUM-n1 §1;
  8. the refusal message names `KEEPER_CANDIDATES`;
  9. the accept case's name gives §5.2 and the merges' targets;
  10. the entry's raw link exists in git;
  11. the report's and the artifact's cell entries carry `layer_sha256` only;
  12. the plan identities, R_ell 50 and 40, merge as the entry says;
  13. six refusal calls carry `expect=`;
  14. Q4's "form (b)" is in the seat's raw.
- **The final schema:** sha256 `0ea39600919aceb43ee25962314e4239f609ef8da7536b12063372dfdfb30db6`.
