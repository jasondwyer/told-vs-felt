# n_analyze.py, the seat's answers to G-ANL-n's nine questions: the blind values-check, three passes (PI date 2026-11-16)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's answers to G-ANL-n's nine questions`. Three
blind values-checkers, each a subagent of this session under a brief quoting the list of record v2's items 1–5 and
allowing no Python, checked the entry, the two close lines (on `8e3bf91`'s entry and on ADDENDUM-n1's) and the review
raw against their sources, claim by claim.
- The first pass checked the first drafts.
- Each later pass checked the drafts as revised after the pass before it, and whether each of that pass's
  dispositions was carried and is true.

Besides the texts, the passes changed texts in the analyzer: PIN-n-30's (passes 1, 2 and 3), PIN-n-32's (pass 3) and
`plan_cells`'s docstring (pass 2); and after pass 3 PIN-n-31's text came to cite n-build's BUILD (`83a50a0`). No logic
changed, and the run of record is on the final bytes. With pass 1's dispositions Code also applied a correction from
the coordinating session: one batch of mutants ran in the background (the review raw's §4).

Each report is reproduced whole, its headings moved down two levels, and is followed by Code's dispositions. The
reports are the checkers' hand-back messages, taken from the subagents' transcripts by script. The checkers write
SCRATCH for Code's scratch folder and REPO for the repository.

## Pass 1: the report

### Blind values-check: the v3 entry, two close lines and the review raw

**Method.** I used read-only commands only: cat, sed, awk, cut, wc, grep, diff, shasum, `test -w`, and git log/show/rev-parse on named commits and paths. I ran no Python and no repository code, and touched nothing under data/. `git status --porcelain` was scoped to named paths. My extraction files are in SCRATCH/vc/checker/.

**Anchor digests** (shasum -a 256, abbreviated with cut):

| File | sha256 |
|---|---|
| SCRATCH/final/n_analyze.py | ae11063d…74c4 |
| REPO scripts/n_analyze.py = `git show bedc198:` = SCRATCH/review/base-bedc198.py | 34a513f9…98b6 |
| Frozen review copy (= SCRATCH/n_analyze.step2-198.py) | 1316f93a…dd06 |
| Mutant base (= SCRATCH/step2/n_analyze.py now) | 9e7faea1…e4ce |
| Schema, working tree = `git show d791bd9:` | 0ea39600…0db6 |
| Schema, `git show 14e65d8:` | 4bed3f9a…4665 |
| Addendum (tree = a61f13d) | e979f8f2…5e03 |
| Proposal | 30a3d0f5…04f4 |
| Answers raw (tree = 52b2c97) | ff2e5d89…ebec, equal to the full hash in close_8e3bf91 |

`diff` of the mutant base against the final file gives one hunk, at line 55 (the REPO line).

#### 1. entry.md

- **E1, L1–2.** The nine questions are at 8e3bf91 and the answers raw at 52b2c97. **CONFIRMED** (8e3bf91's subject; `git show --name-status 52b2c97` adds the raw).
- **E2, L2.** ADDENDUM-n1 v0.1 is at a61f13d. **CONFIRMED** (name-status; blob hash).
- **E3, L2–3.** The pin moved from 14e65d8 to d791bd9, n-build's follow-up commit. **CONFIRMED.** SCHEMA_SHA256 is 4bed3f9a… "# 14e65d8" at base:1882 and 0ea39600… "# d791bd9" at final:2258. d791bd9's subject reads "the schema's follow-up commit (v5)".
- **E4, L3.** "Battery 207/207". **CONFIRMED, pending the run of record.** r1base1 ends 207/207, EXPECTED_CHECKS = 207 (final:968), and the final file differs from the base only in the REPO line.
- **E5, L3.** 62 of 62 mutants killed. **CONFIRMED.** Every out_r1/Mnn.out has at least 2 [FAIL] lines, and the runner counts a non-zero exit as killed.
- **E6, L4.** PIN-n-27 to -32 are Code's readings, flagged for the seat. **CONFIRMED** (final:1981–1982, 2029–2058).
- **E7, L4–5.** Model-free; nothing ran on a model or the box; no stage ran. **NOT CHECKABLE** (session conduct). Supporting evidence: r1base1 PASS "no model library is imported", and every INVOCATION line is `--selftest`.
- **E8, L6–7.** The full sha256 ae11063d…. **CONFIRMED, pending the commit.**
- **E9, L7.** 34a513f9…98b6 at bedc198. **CONFIRMED.**
- **E10, L7–8.** Pinned to the schema at d791bd9, 0ea39600…0db6. **CONFIRMED.**
- **E11, L8.** 4bed3f9a…4665 at 14e65d8. **CONFIRMED.**
- **E12, L8–9.** Binds PROPOSAL-n v0.2, 30a3d0f5…04f4. **CONFIRMED** (final:61).
- **E13, L9–10.** New: binds ADDENDUM-n1 by sha256 in VERDICTS, in a NOT-RUN output, in G-ANL-n's artifact, and among the files the canonical run requires committed. **CONFIRMED.**
  - VERDICTS: final:4798. NOT-RUN: final:3468. Artifact: final:4188.
  - BOUND_RELS (final:4148) feeds committed_problems through ganl_precheck (4230–4234) and again at 4278.
  - The base contains no "ADDENDUM" at all.
- **E14, L10.** Its commands are unchanged. **CONFIRMED.** main() is byte-identical between base and final (62 lines).
- **E15, L11–12.** The run of record gives 207/207, all 210 coverage ids reached, exit 0. **CONFIRMED, pending the run of record.** r1base1 prints "210 required ids reached" and "check count 207 == 207"; `--selftest` returns 0 iff ok (final:4904).
- **E16, L12–13.** The self-test raw's link. **NOT CHECKABLE** (pending the run of record and the commit).
- **E17, L14–15.** The OPEN register records each ruling. **CONFIRMED** (OPEN-Q1–Q9, final:2061–2084).
- **E18, L16–18.** Slopes through the origin over the nonzero points: N1-V's slope, the 24 random slopes of its floor, N2's slope over (d_eq, 2·d_eq), its floor at the kept points, and the mismatch printed. **CONFIRMED** (session_slopes_origin:182; build_state:2536, 2565–2584, 2608–2612; n2_slope_points:353).
- **E19, L18.** A point at d = 0 is refused. **CONFIRMED** (final:189–190).
- **E20, L18–19.** The with-intercept slope is beside, marked descriptive. **CONFIRMED** (final:2555).
- **E21, L19–20.** The two fits coincide per session and per random direction to 1e-12. **CONFIRMED** (check at 1950–1953; r1base1:144 gives a largest gap of 1.39e-17).
- **E22, L20.** BK's reproduction (slope 0.9164, floor 0.3641) is unchanged. **CONFIRMED.** The want-dicts are identical (base:1623–1624, final:1961–1962).
- **E23, L21.** N1-P reads +1, +d_20, +d_eq and −1. **CONFIRMED** (PLAN_TABLE; n1p_points:347).
- **E24, L21–22.** The analyzer derives the read plan and keepers itself and refuses a schema plan that differs. **CONFIRMED** (plan_cells:2298, own_plan:2317, refusal at 2401–2402).
- **E25, L22–23.** 7,680 reads in 138 cells with nothing merged. **CONFIRMED** (RD-POSITIVE; r1base1:155).
- **E26, L23–25.** P(d) is computed at each N1-P point and required at every certification point; its absence STOPs; no accepted plan can produce that STOP. **CONFIRMED.** ceiling_cert (373) is used at 444, 476, 478, 507 and 512. An incomplete N1-P makes N1, dose and N2 INDETERMINATE before any ceiling is computed.
- **E27, L25.** "+1/2, which N1-P does not read, keeps L alone in G-LEAK-n's table". **IMPRECISE.** This holds on shapes (a), (b) and (d). On shape (c), d_eq folds into +1/2 and N1-P reads +1/2 (r1base1:146 "N1-P at +1, +1/2 and −1"), so the table's ceiling there is max(L, P). The code's own comment (366–370) says "+1/2 unless a point merges there".
- **E28, L26–27.** *Answered* is applied by §0.6 to N1 (valence +1), dose (d_eq) and N2 (span_reward at its decision f). **CONFIRMED** (outcomes:548–551).
- **E29, L28.** 385 tuples, 1,921 evaluations, the sentence functions total. **CONFIRMED** (r1base1:114–124).
- **E30, L28–29.** Reachability per shape, now four: 28, 25, 24 and 17. **CONFIRMED** (r1base1:128–131). bedc198 had shapes a, b and d only.
- **E31, L30–31.** N1-P is among N2's and dose's causes; an INDETERMINATE dose gives its d_20 beside as "not computed". **CONFIRMED** (final:470–474, 498).
- **E32, L32–34.** The cap binds iff 2·d_eq > 1. N2 is then decided at f = 0.10 against d_eq, with f = 0.20 beside against d = 1 and the ratio 2·d_eq; otherwise at f = 0.20. **CONFIRMED** (final:330–345).
- **E33, L34.** The beside carries both estimates, each certified on its own. **CONFIRMED** (final:510–512).
- **E34, L35–37.** The §7.6 forms are asserted character for character against the addendum's italic spans. **CONFIRMED.** SENT-ADDENDUM passes (r1base1:105), and I found each form's text verbatim exactly once in the addendum (lines 73–76).
- **E35, L37–39.** The sign rule, and an "against" movement goes to NOT-DETECTABLE or NOT-REPLICATED with its sentence naming it. **CONFIRMED** (n1_outcome; dose_outcome:479–480; fill; failing_text).
- **E36, L39.** The forms' digest is 209d7b46…92f5. **CONFIRMED** (final:2675; equal to the value printed at run1:104).
- **E37, L40–41.** Secondary (b)'s text. **CONFIRMED** (B_STRUCK, byte-equal to the quote).
- **E38, L42–44.** The schema at d791bd9 carries keepers, N1-P's row, the capture band, kfold10 with cv_seed and loads_ms, settled with this session. **CONFIRMED** (schema.py:295, 773, 788, 821, 1100, 1192–1193, 1118, 1161; d791bd9's subject says "settled with n-analyzer").
- **E39, L44.** VERDICTS carries loads_ms in its counters. **CONFIRMED** (final:4848; VD-COMPLETE checks it at 3709).
- **E40, L44–46.** Captures are bound by per-layer hashes that must equal the stage report's and the artifact's; no array is read or needed; an unnamed file is refused. **CONFIRMED** (load_campaign:2375–2392; report_problems; gread_problems).
- **E41, L47–48.** The review raw's link. **CONFIRMED, pending the commit** (the scratch file bears that name).
- **E42, L49.** The frozen copy is 1316f93a…dd06 and passed 198/198. **CONFIRMED** (s2run2; the copy is read-only).
- **E43a, L50.** The reviewer's brief quotes the list of record v2, items 1–5. **CONFIRMED** (review BRIEF:76–83).
- **E43b, L49.** "a subagent of this session". **NOT CHECKABLE.**
- **E44, L50–51.** It found every ruling implemented as ruled. **CONFIRMED.**
- **E45, L51.** No MAJOR defect; F5 MINOR; NOTEs F1–F4 and F6–F11. **CONFIRMED** (see observation 3).
- **E46, L51–53.** B1–B3 MAJOR, as described. **CONFIRMED.**
- **E47, L53–54.** B4–B8 MINOR, B9–B10 NOTEs; 40 mutants, 19 predicted to survive and 21 killed. **CONFIRMED.**
- **E48, L55.** F4–F6, F8–F10 and B1–B10 fixed. **CONFIRMED** (diff from frozen copy to fixed draft; see the §2 items below).
- **E49, L55–56.** Nine new checks. **CONFIRMED.** The count went 198→207 and the coverage ids 201→210; the nine new ids are N1-NOTREP-iii-sign, DOSE-ND-NEG-CI, DOSE-ND-NEG-UNCERT, N2-BESIDE-FIELDS, GLEAK-N1P-INCOMPLETE, the three SENT-FILLED ids and RD-CAP-SLOPES.
- **E50, L56.** "among them six dose sentences, two N1 sentences and four N2 sentences". **IMPRECISE.** The 6, 2 and 4 are right, but they are sentences inside three of the nine checks, not checks among the nine.
- **E51, L56–57.** F1, F2 and F7 registered (their PIN texts amended), F3 as PIN-n-32, F11 kept. **CONFIRMED.**
- **E52, L57–58.** Code added a refusal case for a schema plan that differs. **CONFIRMED.** The refusal already existed in the frozen copy (2281–2282) with no case; the fixed draft adds `_SmPlan` (the plan one read short); M51 is killed by it.
- **E53, L59.** M01–M40 re-express V01–V40, with M17 on its changed line. **CONFIRMED.** 39 of the .old/.new pairs are byte-identical to the V blocks.
- **E54, L59–60.** M41–M62 are "on changed code the reviewer's mutants did not reach". **IMPRECISE.** M54.old is identical to M38.old (V38), and M62.old to M27.old (V27).
- **E55, L60–61.** One run on 9e7faea1…e4ce, 207/207. **CONFIRMED** (r1base1; its INVOCATION names SCRATCH/step2/n_analyze.py, whose bytes now have that hash).
- **E56, L61.** 62 of 62 killed. **CONFIRMED.**
- **E57, L61–62.** "each by its predicted check, directly or through its group's exception". **IMPRECISE.**
  - It holds for M20–M62. M27's predicted check fails at M27.out:80, M43's at M43.out:134, and the reader checks RD-POSITIVE and RD-MERGED never print in M34, M35, M47 or M52.
  - M01–M19 were predicted to survive, so they had no predicted check.
- **E58, L63.** The committed bytes differ from the mutated base in the repository line only. **CONFIRMED, pending the commit.**
- **E59, L64–65.** PIN-n-7 to -26 are accepted per the answers raw's §2. **CONFIRMED.** The block's nine §3 readings are PIN-n-7, -8, -11, -12, -14, -16, -17, -18 and -19, plus PIN-n-20 to -26 (see observation 4).
- **E60–E65, L66–82.** The summaries of PIN-n-27 to -32. **CONFIRMED** (6 items; each matches final:2029–2058; see observation 5).
- **E66, L83–85.** F11's sentence is the seat's §5 form. **CONFIRMED** (T_DOSE_ND_ANSWERED, n:138).
- **E67, L86–87.** Run conditions: granted windows, one at a time, nice, -I, foreground, temp folders outside the repository. **NOT CHECKABLE.** Supporting evidence: run_mutants.sh uses `nice -n 19 "$PY" -I` in a sequential loop, and the battery creates TemporaryDirectory with no dir=.
- **E68, L87–89.** The run counts. **CONFIRMED** (from the five run files and the 62 .out files); the run of record is pending.
- **E69, L89–90.** Q-F3 ran beside them; no other window was open. **NOT CHECKABLE.**
- **E70, L91–92.** The committed-by-path list. **NOT CHECKABLE** (pending the commit).
- **E71, L92.** "Not pushed". **NOT CHECKABLE** (pending).
- **E72, L92–93.** "Next" (the canonical run, then LOCK-n v0.1). **CONFIRMED** (answers raw §3 item 4).

#### 2. close_8e3bf91.md

All nine items are **CONFIRMED**.
- **C1, L1.** Second sitting; the line is the n-analyzer session's, per the raw's header (answers raw:3).
- **C2, L2–4.** The answers raw's path, full sha256 and commit 52b2c97.
- **C3, L5–7.** The routing raw was committed at a61f13d.
- **C4, L9.** Item 9 is byte-identical to the routing raw's line 29 (whole-line `grep -F -x`).
- **C5, L11–13.** The order follows the raw's §3, steps 1–3.
- **C6, L13.** ae11063d…74c4 (pending the commit).
- **C7, L13–14.** The OPEN and PINS registers (final:16, 1981).
- **C8, L14–16.** PIN-n-27 to -32, and the entry's title.
- **C9, L16–17.** §3 step 4.

#### 3. close_a61f13d.md

All seven items are **CONFIRMED**.
- **A1, L1.** The addendum's header (line 4) says the n-analyzer session adds a close line.
- **A2, L2–4.** The four binding sites, as in E13.
- **A3, L5.** B_STRUCK is in §4's words (addendum:40).
- **A4, L6–7.** §5.2 and §5.3.
- **A5, L8–9.** §6, through the schema.
- **A6, L10–11.** §7.1–§7.6 map to slopes, *answered*, sign, causes, N2's slope and forms.
- **A7, L13–14.** PIN-n-27 to -32.

#### 4. 2026-11-16_n-analyze_v3_review.md

**Opening section**
- **R1, L3.** The entry's title. **CONFIRMED.**
- **R2, L5–8.** bedc198's hash and the commits. **CONFIRMED.**
- **R3a, L8–9.** Built in two steps. **CONFIRMED.**
- **R3b, L8–9.** "In a granted window". **NOT CHECKABLE.**
- **R4, L10–12.** Step 1 against 14e65d8, its contents, and 192/197 then 197/197. **CONFIRMED.** The step-1 file pins 4bed3f9a at 2111 and already carries the rulings.
- **R5, L13–14.** Step 2's contents, and 197/198 then 198/198. **CONFIRMED.** The step-1→frozen diff adds the N1-P row, the keepers, the per-layer captures, loads_ms, ceiling_cert and the new pin.
- **R6, L15–16.** The frozen copy is read-only, 1316f93a…dd06, 198/198. **CONFIRMED.**
- **R7a, L17.** A brief quoting the list of record v2, with no Python. **CONFIRMED.**
- **R7b, L17.** "A subagent of this session". **NOT CHECKABLE.**
- **R8, L18–19.** The reviewer's spec. **CONFIRMED** (BRIEF:14–24).
- **R9, L19–20.** "It ran nothing". **IMPRECISE.** This is the reviewer's self-report, and that same report says "I confirmed by digest", so it ran digest commands; it executed no code.
- **R10, L21–23.** The findings, severities and the 40 mutants. **CONFIRMED.**
- **R11, L24–26.** The dispositions summary. **CONFIRMED.**
- **R12, L27–28.** 39 verbatim, M17 re-expressed. **CONFIRMED.**
- **R13, L28–29.** "On changed code the reviewer's mutants did not reach". **IMPRECISE** (M54 and M62, as E54).
- **R14 and R15, L29.** 9e7faea1…, 207/207; 62 of 62 killed. **CONFIRMED** (2 items).
- **R16, L29–30.** "each by its predicted check". **IMPRECISE** (as E57; the next sentence qualifies it).
- **R17, L30–31.** The 19 are "each killed by a check the dispositions added". **IMPRECISE.** M11 was killed by DOSE-BESIDE-D20 and M18 by STR-GANL-ARTIFACT, both checks already in the frozen copy that B6 and B9 extended.
- **R18, L32–33.** The repository line only. **CONFIRMED, pending the commit.**
- **R19, L35–36.** The run conditions. **NOT CHECKABLE.**
- **R20, L37–38.** How mutants were applied, and what "killed" means. **CONFIRMED** (run_mutants.sh).

**§1: the reviewer's report**
- **R21a, L42.** "Saved by script from the transcript". **NOT CHECKABLE.**
- **R21b, L42–43.** Headings moved down two levels, nothing else changed. **CONFIRMED.** After shifting the headings back, raw lines 45–391 equal SCRATCH/review/reviewer/report.md, apart from that file's missing final newline.
- **R21c, L43.** Line numbers are the frozen copy's. **CONFIRMED** (13 cited ranges checked).

**§2: the dispositions**

§2 equals SCRATCH/review/dispositions.md apart from its heading. Each described change is in the frozen→fixed diff. All 22 items are **CONFIRMED**:
- **F1, F2, F7, F8.** The PIN texts are extended (2033–2057).
- **F3.** PIN-n-32 is added; the forms and their digest are unchanged.
- **F4.** final:2555 and the RD-ASYM check at 3167.
- **F5.** final:474, OPEN-Q6, and the DOSE-INDET-POINTS check.
- **F6.** final:510–512 and N2-BESIDE-FIELDS.
- **F9.** final:403.
- **F10.** final:4185.
- **F11.** Unchanged.
- **B1–B3.** The literal cases, 6, 2 and 4 sentences.
- **B4.** The case rows at 1112–1114 and 1183–1185.
- **B5.** final:3113–3127.
- **B6.** 0.06 against L 0.05 and P 0.07.
- **B7, B8, B9.** As described.
- **B10.** Its four items.
- **"Beyond the findings".** As described.

**§3: the mutants and their run**
- **R23, L449–452.** Application of M01–M40, M17's re-expression, and M41–M62 written against the fixed draft. **CONFIRMED.** Each old text occurs once; M41–M62 are byte-identical to their files.
- **R24, L454–456.** The base is read-only, 207/207, 210 ids. **CONFIRMED.**
- **R25, L456.** "Each mutant ran once, one process at a time". **NOT CHECKABLE.** The runner's loop is sequential, and there is one .out file per mutant.
- **R26, L456.** All 62 killed. **CONFIRMED.**
- **R27, L456–458 and the table header at L470.** "killed" lists the unreached ids "and any group that raised". **FAIL.**
  - Seven rows omit the "reader path" group's exception: M34, M35, M44, M47 and M52 show only the verdicts group, and M48 and M55 show no exception at all.
  - The .out files show it in each: M34:165 KeyError '+d_20'; M35:155 STOP no P(d) at 0.3125; M44:165 KeyError; M47:165 plan refusal; M48:176 refusal of a file beside the cells; M52:155 KeyError 0.0; M55:168 KeyError 'descriptive'.
  - The table is an exact copy of kill_table.txt, which evidently drops the two-word group name.
- **R28–R33, the bullets.** **CONFIRMED** (6 items).
  - **M03:** out:112; N1-AGAINST runs before N2-CAP.
  - **M27:** out:2 and 39 (the group STOPs), 53–56, and 80. The reachability group also raised (out:58), as the table says.
  - **M43:** out:134 and 55.
  - **M34, M35, M47, M52:** both groups raised, with the stated exception kinds; 0.3125 is d_eq.
  - **M55:** the lookup at 3167.
  - **M57:** the lookup at 4372.
- **R34a, the table's descriptive columns.** **CONFIRMED** (equal to headers.txt for all 62 rows; "From" is right).
- **R34b, the table's unreached-id lists.** **CONFIRMED** (equal to kill_table.txt and to every .out's coverage line).
- **R35, the M41–M62 blocks.** **CONFIRMED.**
- **R36, M17 as re-expressed.** **CONFIRMED.**

**§4: the battery runs**
- **R37, L681–682.** The run conditions. **NOT CHECKABLE.**
- **R38, L684–687.** 192/197; the digest moved; the two reader expectations. **CONFIRMED** (run1:104, 155, 162).
- **R39, L687.** "and the coverage and count checks followed from those". **FAIL for the count check.**
  - run1:198 reads "check count 197 == EXPECTED_CHECKS 185": the constant was still bedc198's 185, independent of the other failures.
  - The coverage failure did follow from them (run1:197).
  - The next sentence also omits that EXPECTED_CHECKS was raised to 197 before run 2.
- **R40, L687–688.** The digest was set from run 1's printed value; run 2 gave 197/197. **CONFIRMED.**
- **R41, L688–689.** Step 2's first run failed on the count alone. **CONFIRMED** (s2run1's only FAIL is the count).
- **R42, L690.** One run of the fixed draft, then the 62 mutants. **CONFIRMED.**
- **R43, L690–693.** The failed first batch attempt. **NOT CHECKABLE.** There is no log, but the account is consistent: both frozen copies are read-only, and the runner now has `chmod u+w` and a `continue` that skips Python on an apply failure.
- **R44, L694.** The run of record. **NOT CHECKABLE** (pending).

**§5: the committed bytes**
- **R45, L698.** The committed file differs from the base in the repository line only. **CONFIRMED, pending the commit.**
- **R46, L698–704.** The quoted line is what the committed analyzer always had. **CONFIRMED** (5c0ae6b:49, 2822721:49, bedc198:54).

#### Counts

| Text | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE | Total |
|---|---|---|---|---|---|
| entry.md | 62 | 4 | 0 | 7 | 73 |
| close_8e3bf91.md | 9 | 0 | 0 | 0 | 9 |
| close_a61f13d.md | 7 | 0 | 0 | 0 | 7 |
| review raw | 58 | 4 | 2 | 8 | 72 |
| **All** | **136** | **8** | **2** | **15** | **161** |

#### Observations outside the claims

1. **Table against bullets (the FAIL in R27).** The raw's bullets add the reader-group exception back for M34, M35, M47, M52 and M55, but not for M44 or M48. The bullets also leave out M29 and M50, which raised in the verdicts group (as the table shows). The entry points readers to this table ("the raw's §3").
2. **The reviewer's bottom line contradicts its own findings.** The reproduced report says "no MAJOR or MINOR defect in the production code" yet lists F5 as MINOR. The entry and raw summaries follow the findings list. A one-line note would stop a reader taking "no MINOR" as Code's summary.
3. **The PIN range has gaps.** "PIN-n-7 to PIN-n-26" (entry L64–65; close_8e3bf91 L14) covers 16 registered PINs; PIN-n-9, -10, -13 and -15 exist nowhere (analyzer, schema or RESULTS.md). The range is the analyzer's own wording.
4. **PIN-n-30 has an unstated condition.** "N1-V moving against the zone … gives SPECIFIC" holds only when span_reward is not certified; otherwise the outcome is SHARED. This is elided in both the register and the entry.
5. **Two mutants were killed by a different mechanism than predicted.** M34 and M52 were predicted to die by a schema refusal and a STOP; both actually raised a KeyError. The predicted checks were still left unreached, so the claim holds, but the table cannot show the difference.
6. **Which file the runs used.** The 198/198 and 207/207 runs were invoked on SCRATCH/step2/n_analyze.py, not on the read-only frozen copies. That file now hashes 9e7faea1…, and SCRATCH/n_analyze.step2-198.py hashes 1316f93a….
7. **No forbidden text.** None of the four texts contains a clock time, a local path or the user name.
8. **My own conduct.**
   - One mistyped redirect created a temp file directly in SCRATCH/vc/, outside SCRATCH/vc/checker/. I deleted it at once; nothing else was written outside checker/.
   - SCRATCH/vc/pending_corrections.md appeared during the check (it was absent at the start). I did not open it.

### Code's dispositions of pass 1

Pass 1: 161 claims; 136 CONFIRMED, 8 IMPRECISE, 2 FAIL, 15 NOT CHECKABLE; eight observations. Every IMPRECISE and
FAIL is applied; the observations are applied where they name a defect.

- **E27 (IMPRECISE), the entry's "+1/2, which N1-P does not read".** Now: "At +1/2, which N1-P does not read unless
  d_eq merges there, G-LEAK-n's table keeps L alone."
- **E50 (IMPRECISE), "nine new checks, among them six dose sentences...".** Now: "nine new checks, three of which
  compare filled sentences with literal text: six dose sentences, two N1 and four N2".
- **E54 and R13 (IMPRECISE), M41–M62 "on changed code the reviewer's mutants did not reach".** Now, in the entry and
  the raw: on the fixes and on changed code, mostly lines the reviewer's mutants did not touch (M54 and M62 mutate
  V38's and V27's lines another way).
- **E57 and R16 (IMPRECISE), "each by its predicted check".** Now: M20–M62 each by its predicted check, directly or
  through the exception its group raised; M01–M19, predicted to survive the frozen copy, each by a check the
  dispositions added or extended.
- **R17 (IMPRECISE), "a check the dispositions added".** Now "added or extended", naming M11 (DOSE-BESIDE-D20) and
  M18 (STR-GANL-ARTIFACT).
- **R9 (IMPRECISE), "It ran nothing".** Now: "It executed no code (it read files and computed digests)".
- **R27 (FAIL), the table's group exceptions.** Code's kill-table script took a group's name as one word, so the
  "reader path" group was dropped from seven rows. The script now takes the whole name and the exception's type;
  the table was regenerated (thirteen rows with a group exception), and §3's notes now cover all thirteen
  (observation 1).
- **R39 (FAIL), run 1's count check.** Now: the count check failed on its own (EXPECTED_CHECKS still 185 against 197
  checks); EXPECTED_CHECKS was set to 197 with the digest before run 2.
- **Observation 2, the reviewer's bottom line.** The raw's §1 notes that the bottom line says "no MAJOR or MINOR
  defect" while the findings list F5 as MINOR, and that the entry and §2 follow the findings.
- **Observation 3, "PIN-n-7 to PIN-n-26".** The entry and the close line on `8e3bf91` now say "the sixteen PINs
  registered from PIN-n-7 to PIN-n-26" (git grep finds no PIN-n-9, -10, -13 or -15 in the repository outside data/).
- **Observation 4, PIN-n-30's unstated condition.** Applied in the code: the register's text says "span_reward not
  certified". The committed file therefore differs from the mutant base in PIN-n-30's text as well as the repository
  line; the entry, the close lines (the new sha256 `a279a72d…e2a2`) and the raw's §5 say so. No check reads a PIN's
  words; the run of record runs on these bytes.
- **Observation 5, M34 and M52's mechanism.** §3's notes say the KeyError came before the predicted refusal and STOP.
- **Observation 6, which file the runs used.** The raw's §4 says the runs ran on the working copy, each frozen copy
  made from it unchanged after its run; the header says the 198/198 run was on the working copy before it was frozen.
- **The coordinating session's point (not the checker's), the foreground claim.** The first mutant batch (M01–M09)
  reached the tool's 10-minute limit during M08 and was moved to the background by the harness, where M08 and M09
  finished, one process at a time. The entry's "Runs" bullet, the raw's header paragraph and its §4 now say so.
- **Observation 7** (no forbidden text) and **observation 8** (the checker's own conduct): noted; nothing to apply.

## Pass 2: the report

### Values-check, pass 2: the v3 entry, two close lines and the review raw

**Result.** 176 claims: 155 CONFIRMED, 4 IMPRECISE, 1 FAIL, 16 NOT CHECKABLE. Of the 15 dispositions, all 15 are carried. 14 are true. One (E27) is not wholly true: its revised wording is the FAIL.

**Method.** I used read-only commands only: cat, sed, awk, grep, diff, cmp, od, wc, `shasum -a 256`, `test -w`, name-only `ls`, git log/show/rev-parse on named commits and paths, and one `git grep … -- . ':!data/**'`. `git status --porcelain` was scoped to named paths. I ran no Python and no repository code, and read nothing under data/. My extraction files are only under SCRATCH/vc/checker2/.

**Anchor digests** (abbreviated by `cut`):

| File | sha256 |
|---|---|
| SCRATCH/final/n_analyze.py | a279a72d…e2a2 (the full value equals entry L7) |
| REPO scripts/n_analyze.py = `git show bedc198:` = SCRATCH/review/base-bedc198.py | 34a513f9…98b6 |
| Frozen review copy = SCRATCH/n_analyze.step2-198.py (read-only) | 1316f93a…dd06 |
| Mutant base SCRATCH/review/n_analyze.round1-base.py (read-only) | 9e7faea1…e4ce (the full value equals raw L459) |
| Step-1 draft = SCRATCH/n_analyze.py (the step-1 runs' file) | 520b5112…1599 |
| SCRATCH/step2/n_analyze.py (the later runs' working copy) | 4f64e228…92e6 |
| Schema: working tree = `git show d791bd9:` | 0ea39600…0db6 |
| Schema: `git show 14e65d8:` | 4bed3f9a…4665 |
| Addendum: tree = a61f13d | e979f8f2…5e03 |
| Proposal | 30a3d0f5…04f4 |
| Answers raw: tree = 52b2c97 | ff2e5d89…ebec |
| Routing raw: tree = a61f13d | ec54c56b…6a53 |

- **Base against final.** `diff` gives exactly two hunks: line 55 (the REPO line) and lines 2045–2047 (PIN-n-30's text).
- **step2 working copy against final.** It differs only in line 55. So the PIN-n-30 edit went into the working copy after the mutant run.
- **History.** HEAD is 9662468. The last commit to touch each file: analyzer bedc198, schema d791bd9, addendum a61f13d. Scoped status is clean.

#### 1. entry.md

- **E1–E3, L1–2.** The nine questions are at 8e3bf91, the answers raw at 52b2c97, and ADDENDUM-n1 v0.1 at a61f13d. **CONFIRMED** (subjects; `--name-status` shows each file added there).
- **E4, L2–3.** The pin moved from 14e65d8 to d791bd9, n-build's follow-up commit. **CONFIRMED** (base:1882 against final:2258; d791bd9's subject).
- **E5, L3.** "Battery 207/207". **CONFIRMED, pending the run of record.** r1base1 gives 207/207; EXPECTED_CHECKS = 207 (final:968). See observation 5.
- **E6, L3.** Reviewed blind; 62 of 62 mutants killed. **CONFIRMED.** Every out_r1/Mnn.out has [FAIL] lines and fewer passes than its total; `--selftest` returns 1 unless ok (final:4897).
- **E7, L4.** PIN-n-27 to -32 are Code's readings, flagged for the seat. **CONFIRMED** (register comment, final:1981–1982).
- **E8, L4–5.** Model-free; no stage ran. **NOT CHECKABLE.** Supporting: STR-NO-HEAVY passes, and every INVOCATION is `--selftest`.
- **E9, L6–7.** The full sha256. **CONFIRMED, pending the commit.**
- **E10–E13, L7–9.** bedc198's hash; the schema pin 0ea39600 at d791bd9; 4bed3f9a at 14e65d8; the proposal 30a3d0f5. **CONFIRMED** (final:61, 2258).
- **E14, L9–10.** New: the addendum is bound by sha256 in VERDICTS, NOT-RUN, the artifact and the canonical run's committed files. **CONFIRMED.**
  - VERDICTS final:4798; NOT-RUN final:3468; artifact final:4188.
  - BOUND_RELS (final:4148) feeds committed_problems at final:4230–4234 and 4278.
  - The base has no "ADDENDUM" at all.
- **E15, L10.** The commands are unchanged. **CONFIRMED** (main() is byte-identical, 61 lines).
- **E16, L11–12.** The run of record: 207/207, 210 ids, exit 0. **CONFIRMED, pending the run of record** (r1base1:207–209).
- **E17, L12–13.** The self-test raw's link. **NOT CHECKABLE** (pending; the file does not exist yet).
- **E18, L14–15.** The sources carried, and the OPEN register records each ruling. **CONFIRMED** (OPEN-Q1–Q9, final:2061–2084).
- **E19, L16–18.** Slopes through the origin over the nonzero points: N1-V, the 24 random slopes, N2's slope over (d_eq, 2·d_eq), its floor at the kept points, and the mismatch. **CONFIRMED** (final:182–193, 2531–2584, 2608–2612; n2_slope_points:353–358).
- **E20, L18.** d = 0 is refused. **CONFIRMED** (final:189–190).
- **E21, L18–19.** The with-intercept slope is beside, marked descriptive. **CONFIRMED** (final:2555).
- **E22, L19–20.** The two fits coincide per session and per direction to 1e-12. **CONFIRMED** (final:1950–1953; r1base1 gap 1.39e-17).
- **E23, L20.** BK's 0.9164 and 0.3641 are unchanged. **CONFIRMED** (want-dicts identical at base:1623–1624 and final:1961–1962).
- **E24, L21.** N1-P reads +1, +d_20, +d_eq and −1. **CONFIRMED** (PLAN_TABLE; final:351).
- **E25, L21–22.** The analyzer derives the plan's keepers itself and refuses a schema plan that differs. **CONFIRMED** (plan_cells:2298; own_plan:2317; load_campaign refusal).
- **E26, L22–23.** 7,680 reads in 138 cells. **CONFIRMED.** RD-POSITIVE asserts both; by arithmetic, 960 + 4,800 + 640 + 960 + 320 reads and 6 + 120 + 4 + 6 + 2 cells.
- **E27, L23–25.** P(d) is computed at every N1-P point and required at the listed points; its absence STOPs; no accepted plan produces it. **CONFIRMED.** ceiling_cert is used at final:444, 476, 478, 505, 510. Any unusable N1-P makes N1, dose and N2 INDETERMINATE first.
- **E28, L25.** "At +1/2, which N1-P does not read unless d_eq merges there, G-LEAK-n's table keeps L alone." **FAIL.**
  - N1-P also reads +1/2 when **d_20** sits there, i.e. d_eq in [0.225, 0.275]. Example: d_eq 0.25, so d_20 = 0.5 = +1/2. The battery itself names this case: final:1848, and final:4349 ("d_20 at +1/2 is (a)").
  - Then kept_label("d_20") is "+1/2" (final:305–312). n1p_points includes 0.5 (final:351), so P(0.5) is computed and gleak_table's ceiling there is max(L, P) (final:766–767).
  - The code's own comment (final:369) says "+1/2 unless a point merges there".
- **E29, L26–27.** *Answered* by §0.6 for N1, dose and N2 (at its decision f). **CONFIRMED** (outcomes:548–551; label:641).
- **E30, L28.** 385 tuples and 1,921 evaluations; the sentence functions are total. **CONFIRMED** (r1base1 TUP lines).
- **E31, L28–29.** Four shapes with Q7: 28, 25, 24, 17. **CONFIRMED** (r1base1:128–131). bedc198 had shapes a, b and d only (base:892).
- **E32, L30–31.** N1-P is among N2's and dose's causes; an INDETERMINATE dose gives its d_20 beside as "not computed". **CONFIRMED** (final:470–474, 498).
- **E33, L32–34.** The cap rule; f = 0.10 against d_eq; f = 0.20 beside against d = 1 with the ratio 2·d_eq; otherwise the reverse. **CONFIRMED** (final:330–345, 500–517).
- **E34, L34.** The beside carries both estimates, each certified on its own. **CONFIRMED** (final:510–513).
- **E35, L35–37.** §7.6's forms are asserted against the italic spans. **CONFIRMED.** SENT-ADDENDUM passes, and each form occurs as a `*…*` span in the addendum (lines 73–76).
- **E36, L37–39.** The sign rule, and an against-movement named in NOT-DETECTABLE or NOT-REPLICATED. **CONFIRMED** (final:441–459, 479–481, 649–652, 2711).
- **E37, L39.** The forms' digest 209d7b46…92f5. **CONFIRMED** (final:2675).
- **E38, L40–41.** Secondary (b)'s text. **CONFIRMED** (B_STRUCK, final:588; used at 2802).
- **E39, L42–43.** The schema at d791bd9 carries keepers, N1-P's row, the capture band, kfold10 with cv_seed and loads_ms, settled with this session. **CONFIRMED** (schema:286, 295, 773, 788, 821, 1100, 1118, 1161, 1192–1193; d791bd9's subject).
- **E40, L43–44.** VERDICTS carries loads_ms in its counters. **CONFIRMED** (final:4848; VD-COMPLETE at 3709).
- **E41, L44–46.** Captures are bound by per-layer hashes equal to the report's and the artifact's; no array is read; an unnamed file is refused. **CONFIRMED** (load_campaign:2375–2392; report_problems; gread_problems:4616; no np.load).
- **E42, L47–48.** The review raw's link. **CONFIRMED, pending the commit.**
- **E43, L49.** The frozen copy 1316f93a…dd06, at 198/198. **CONFIRMED** (s2run2; the copy is read-only).
- **E44, L49–50.** "A subagent of this session". **NOT CHECKABLE.**
- **E45, L50.** The brief quotes list v2, items 1–5. **CONFIRMED** (review/BRIEF.md:76–83).
- **E46–E48, L50–54.** Every ruling as ruled; no MAJOR in production; F5 MINOR; the B severities; 40 mutants, 19 survive and 21 are killed. **CONFIRMED** (report.md; counted by grep).
- **E49, L55.** F4–F6, F8–F10 and B1–B10 fixed. **CONFIRMED** (the frozen→base diff, 39 hunks).
- **E50, L55–56.** Nine new checks, three of them literal-sentence checks: 6 dose, 2 N1 and 4 N2 sentences. **CONFIRMED.**
  - Coverage ids went 201→210 and checks 198→207.
  - Literal cases: 3 forms × 2 dose sentences, 2 N1 cases, 4 N2 cases.
- **E51, L56–57.** F1, F2 and F7 registered; F3 as PIN-n-32; F11 kept. **CONFIRMED.**
- **E52, L57–58.** A refusal case added for a schema plan that differs. **CONFIRMED** (`_SmPlan`; M51 is killed by it).
- **E53, L59.** M01–M40 re-express V01–V40, with M17 on its changed line. **CONFIRMED.** 39 .old/.new pairs are byte-equal to the V blocks; M17 makes V17's f_bes→f_dec change on the fixed line.
- **E54, L59–61.** M41–M62: on the fixes and on changed code, mostly lines the reviewer did not touch; M54 and M62 on V38's and V27's lines. **CONFIRMED.**
  - No M41–M62 old line exists in bedc198.
  - M45, M46 and M55 are on lines the fixes added.
  - Only M54.old = M38.old and M62.old = M27.old share lines with V mutants.
- **E55–E56, L61.** One run on 9e7faea1, 207/207; 62 of 62 killed. **CONFIRMED.** Each out_r1/Mnn.py is the base plus exactly one hunk equal to .old→.new, and its first old line occurs once.
- **E57, L62.** M20–M62 each killed by its predicted check, directly or through the group's exception. **CONFIRMED.**
  - M27 directly at out:80; M43 at out:134; M44 at out:152.
  - M34 and M47: the reader-path exception at RD-MERGED's slot (out:165).
  - M35 and M52: the exception at RD-POSITIVE's slot (out:155).
  - The rest are in the unreached lists.
- **E58, L62–63.** M01–M19 each killed by an added or extended check. **CONFIRMED** (kill_table.txt).
- **E59, L64–65.** The commit differs from the base in two places. **CONFIRMED, pending the commit.**
- **E60, L66–67.** Strikable until LOCK-n v1.0; the sixteen PINs from PIN-n-7 to -26 are accepted. **CONFIRMED.**
  - Register: PIN-n-7, 8, 11, 12, 14, 16, 17, 18, 19, then 20–26.
  - The nine §3 readings of the prebuild block match PIN-n-7/8/11/12/14/19/16/17/18 in content.
- **E61–E63, L68–75.** The summaries of PIN-n-27, -28 and -29. **CONFIRMED** (final:2025–2041; n1_outcome; failing_text; n2_outcome reads).
- **E64, L76–79.** PIN-n-30's summary. **IMPRECISE.**
  - "where the cap binds, the dose sentence names the same movement as against the zone" holds only if the CI at d_eq also excludes 0.
  - Dose's `against` = CI excludes 0 ∧ certified ∧ mean < 0 (final:481). N2's cert_v is |mean| > ceiling alone (final:506).
  - With a CI that includes 0, the dose sentence says "the margin's movement is not certified" instead. See observation 2.
- **E65–E67, L80–87.** PIN-n-31, PIN-n-32 and F11. **CONFIRMED** (final:2048–2058; fill:2709–2712; T_DOSE_ND_ANSWERED).
- **E68, L88–91.** The run conditions and the background batch. **NOT CHECKABLE.** Supporting: run_mutants.sh runs `nice -n 19 "$PY" -I` in a sequential loop; the battery's TemporaryDirectory has no dir=; M08.out and M09.out are complete.
- **E69, L91–93.** The run counts. **CONFIRMED** (run1 192/197, run2 197/197, s2run1 197/198, s2run2 198/198, r1base1 207/207, 62 .out files). The run of record is pending.
- **E70, L93–94.** Q-F3 ran beside them; no other window was open. **NOT CHECKABLE.**
- **E71–E72, L95–96.** The committed-by-path list; "Not pushed". **NOT CHECKABLE** (pending).
- **E73, L96–97.** "Next". **CONFIRMED** (answers raw §3 item 4).

#### 2. close_8e3bf91.md

All ten claims are **CONFIRMED**.
- **C1, L1.** The n-analyzer session's line, per the n-ganl raw's header (answers raw:3).
- **C2, L2–4.** The link, the full sha256, and 52b2c97.
- **C3, L4–5.** "Rule this block's nine questions".
- **C4, L5–7.** The routing raw was added at a61f13d.
- **C5, L9.** Item 9 is byte-identical to the routing raw's line 29, once the quote marker and the leading space are stripped (`cmp`).
- **C6, L11–13.** The order follows answers raw §3, steps 1–3.
- **C7, L13.** a279a72d…e2a2 (pending the commit).
- **C8, L13–14.** The OPEN register, and the sixteen accepted PINs.
- **C9, L14–16.** PIN-n-27 to -32, and the entry's title.
- **C10, L16–17.** §3 step 4.

#### 3. close_a61f13d.md

- **A1, L1.** Per the addendum's header (line 4). **CONFIRMED.**
- **A2, L2.** The sha256, committed with this line. **CONFIRMED, pending the commit.**
- **A3, L2–4.** The four binding sites. **CONFIRMED** (as E14).
- **A4, L5.** §4 in the section's words. **CONFIRMED** (B_STRUCK's clauses are §4's, the first letter's case aside; final:1395–1397).
- **A5, L6–7.** §5.2–§5.3: the keepers derived, the schema plan asserted equal, and the decision f. **CONFIRMED.**
- **A6, L8–9.** §6 through the schema. **CONFIRMED.**
- **A7, L10–11.** §7.1–§7.6, mapped. **CONFIRMED.**
- **A8, L13–14.** "Where the addendum leaves the form to Code, its readings are PIN-n-27 to PIN-n-32". **IMPRECISE.**
  - Only PIN-n-28 and -32 are about form.
  - PIN-n-29 reads §7.4's "at the norm-matched point" per arm; the reviewer's F1 notes that on the literal reading N2 is evaluated.
  - PIN-n-27, -30 and -31 are readings of content (the sign's definition, unsigned N2, and the capture binding).

#### 4. The review raw

**Opening section**
- **R1, L3.** The entry's title. **CONFIRMED.**
- **R2, L5–8.** bedc198's hash and the commits. **CONFIRMED.**
- **R3a, L8.** Two steps. **CONFIRMED.**
- **R3b, L8–9.** Granted windows. **NOT CHECKABLE.**
- **R4, L10–12.** Step 1's contents; 192/197, then 197/197. **CONFIRMED.**
  - The step-1 draft pins 4bed3f9a (line 2111) and EXPECTED_CHECKS 197.
  - It has session_slopes_origin, n2_decision_f, n1p_points, MOVE_AGAINST and B_STRUCK.
  - N1-P's row is still (+1, −1).
- **R5, L13–14.** Step 2's contents. **CONFIRMED.** The step1→frozen diff adds ceiling_cert, N1-P's four-point row, the keepers, per-layer captures, loads_ms and the d791bd9 pin.
- **R6, L15–16.** The frozen read-only copy at 198/198. **CONFIRMED.**
- **R7a, L17.** "A subagent of this session". **NOT CHECKABLE.**
- **R7b, L17.** The brief quotes list v2 and allows no Python. **CONFIRMED** (BRIEF:61, 76–83).
- **R8, L18–19.** The spec list. **CONFIRMED** (BRIEF:15–24).
- **R9, L19–20.** "Executed no code (read files, computed digests)", nothing under data/. **CONFIRMED** as the reviewer's own report (report.md:10–14).
- **R10, L21–23.** The findings and predictions. **CONFIRMED.**
- **R11, L24–26.** The dispositions summary. **CONFIRMED.**
- **R12–R17, L27–32.** **CONFIRMED** (as E53–E58). M11 and M18 are the only kills by extended checks.
- **R18, L33–34.** Two places. **CONFIRMED, pending the commit.**
- **R19, L36–38.** The run conditions. **NOT CHECKABLE.**
- **R20, L39–40.** How a mutant is applied, and "killed" means a non-zero exit. **CONFIRMED** (run_mutants.sh:11–21).

**§1: the reviewer's report**
- **R21, L44.** "Saved by script from the transcript". **NOT CHECKABLE.**
- **R22, L44–45.** Headings moved down two levels, nothing else changed. **CONFIRMED.** Raw L49–395, with the headings shifted back, equal report.md apart from its missing final newline.
- **R23, L45.** The line numbers are the frozen copy's. **CONFIRMED** (12 citations checked).
- **R24, L45–47.** The bottom line against F5, followed by the entry and §2. **CONFIRMED.**

**§2: the dispositions.** §2 equals review/dispositions.md apart from its heading.
- **R25, and F1–F11, B1–B10 and "Beyond".** **CONFIRMED** (23 items).
  - PIN texts: final:2033–2047, 2054–2058.
  - Code: descriptive at 2555; "not computed" at 474 plus OPEN-Q6; V and certified_V at 510–513; the comment at 403; the spec at 4185.
  - Checks: DOSE-INDET-POINTS at 1203–1206; DOSE-BESIDE-D20 (0.06 against L 0.05 and P 0.07); the literal cases at 1453–1522; RD-CAP-SLOPES at 3113–3127; GLEAK-N1P-INCOMPLETE; N2-BESIDE-FIELDS.
  - STR-GANL-ARTIFACT at 4441–4442; the B10 texts at 1967, 3100–3102, 1418–1420, 2921–2931, 3173–3174; `_SmPlan`.

**§3: the mutants and their run**
- **R26, L453–456.** **CONFIRMED.**
- **R27, L458–460.** The base is read-only, 207/207, 210 ids. **CONFIRMED.**
- **R28, L460.** "Ran once, one at a time". **NOT CHECKABLE** (one .out each; the loop is sequential).
- **R29–R31.** All killed; the meaning of "killed"; thirteen runs with a group exception. **CONFIRMED.**
- **The 11 bullets** (M03, M27, M29, M34/M44/M52, M35, M43, M47, M48, M50, M55, M57). **CONFIRMED** against the .out lines. For example:
  - M27: out:2, 39, 53–56, 58, 80, with d = 1/3, MAP_A's d_eq.
  - M29: out:53, 164, 190, with 0.625 = d_20 at R_ell 23.90625.
  - M44: KeyErrors 0.49 and 0.5229, both d_eq merged into +1/2; out:152.
  - M50: out:176 and 184.
- **R43.** The table's descriptive columns equal mutants_r1/headers.txt, and "From" is consistent. **CONFIRMED.**
- **R44.** The result column equals kill_table.txt, which equals every .out's coverage line and its "group raised" lines in order (rebuilt by tool: 0 differences). It now shows "reader path" for M34, M35, M44, M47, M48, M52 and M55. **CONFIRMED.**
- **R45–R46.** The M41–M62 blocks and the M17 block are byte-equal to the files. **CONFIRMED.**

**§4: the battery runs**
- **R47, L697–698.** The run conditions. **NOT CHECKABLE.**
- **R48, L699.** The runs used the working copy, frozen afterwards. **CONFIRMED** as far as checkable. INVOCATIONs name SCRATCH/n_analyze.py (= the step-1 draft) and step2/n_analyze.py; the timing is not checkable.
- **R49, L701–704.** Run 1 failures. **CONFIRMED.** The FAILs are at run1:104 (digest), 155, 162 (expectations), 197 (coverage) and 198 ("197 == EXPECTED_CHECKS 185").
- **R50, L704–705.** "The digest was set … and EXPECTED_CHECKS to 197; the second run: 197/197". **IMPRECISE.** The two reader expectations were also edited before run 2: run1:155 against run2:155, where RD-SHADOW gains "shadow:N1-P". The account lists only two edits.
- **R51, L706–707.** Step 2's runs. **CONFIRMED** (s2run1's only FAIL is the count).
- **R52, L708.** One 207/207 run, then the mutants. **CONFIRMED.**
- **R53, R54, L709–714.** The failed first attempt and the background batch. **NOT CHECKABLE.**
  - Consistent: the base copies are read-only, and the runner now has `chmod u+w` and a `continue` on apply failure.
  - The batch arithmetic works: M10–M57 is 8 × 6, and M58–M62 is 5.
- **R55, L715.** The run of record. **NOT CHECKABLE** (pending).

**§5: the committed bytes**
- **R56, L719.** Two places. **CONFIRMED, pending the commit.**
- **R57, L720–725.** The quoted line equals final:55, and the repository line is the same at 5c0ae6b:49, 2822721:49 and bedc198:54. **CONFIRMED.**
- **R58, L726–727.** Pass 1's finding, and the register now says "span_reward not certified". **CONFIRMED** (final:2045–2047).
- **R59a, L727.** "No check reads a PIN's words". **CONFIRMED.**
  - STR-PINS regex-matches names outside the registers.
  - STR-GANL-ARTIFACT compares `art["pins"] == PINS`, the same object.
  - The only hard-coded digests are the proposal, addendum, schema and CODE_FORMS ones.
- **R59b, L727–728.** "STR-PINS counts the registered names and their citations". **IMPRECISE.** It compares sets of names (final:2240–2245); it counts nothing.
- **R60, L728–729.** No outcome, sentence or form changes; the register goes into the outputs as text. **CONFIRMED.**

#### 5. Pass 1's dispositions

The header (161 claims; 136/8/2/15; eight observations; every IMPRECISE and FAIL applied) is true.

- **E27: CARRIED (entry L25). NOT TRUE as written.** It still misses d_20 at +1/2 (see E28).
- **E50: CARRIED (L55–56). True.**
- **E54/R13: CARRIED (entry L60–61; raw L28–29). True.**
- **E57/R16: CARRIED (entry L62–63; raw L30–31). True.**
- **R17: CARRIED (raw L31–32). True.**
- **R9: CARRIED (raw L19–20). True** as the reviewer's self-report.
- **R27: CARRIED.** The table was regenerated, with 13 exception rows and 13 notes. **True** for the fix. The stated cause (the old kill-table script read a group name as one word) is not checkable: no such script is in SCRATCH, and raw/gen_table.pl now uses `([^=]+)`.
- **R39: CARRIED (raw L703–705). True.** The same sentence omits the expectation edits (R50).
- **Obs 2: CARRIED (raw L45–47). True.**
- **Obs 3: CARRIED (entry L66–67; close L14). True.** The register has 16 + 6 PINs, and `git grep -- . ':!data/**'` finds no PIN-n-9, -10, -13 or -15.
- **Obs 4: CARRIED** (the code, the entry, both closes' new sha, raw §5). **True.** A second unstated condition remains (observation 2).
- **Obs 5: CARRIED (raw L472–473). True.**
- **Obs 6: CARRIED (raw L15–16, L699). True** as far as checkable.
- **The coordinating session's foreground point: CARRIED** (entry L89–91; raw L37–38; §4 L697–698, L711–714). Not checkable as conduct; consistent with SCRATCH/vc/pending_corrections.md and the complete M08 and M09 outputs.
- **Obs 7/8:** nothing to apply. **True.**

#### Counts

| Text | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE | Total |
|---|---|---|---|---|---|
| entry.md | 64 | 1 | 1 | 7 | 73 |
| close_8e3bf91.md | 10 | 0 | 0 | 0 | 10 |
| close_a61f13d.md | 7 | 1 | 0 | 0 | 8 |
| review raw | 74 | 2 | 0 | 9 | 85 |
| **All** | **155** | **4** | **1** | **16** | **176** |

#### Observations outside the claims

1. **E28 is a wording error, not a code defect.** A fix: "+1/2, which N1-P reads only where d_20 or d_eq sits there". Two analyzer docstrings narrow the same way: plan_cells (final:2301, "+1/2 where d_eq folds there") and NUM-N1P-POINTS's description (final:1916). The ceiling comment (final:369) has it right.
2. **For the seat (PIN-n-30, the same class as F2 and F11).** Where the cap binds, N2 and dose read the same point and ceiling.
   - N2's certification has no CI condition; the seat's §1.8 calls a CI that includes 0 "not certified".
   - So a V(d_eq) beyond the ceiling with a CI including 0, of either sign, gives N2 SPECIFIC ("the valence direction … does" move BK's apparatus beyond the leak ceiling).
   - Beside it, the dose sentence then says "the margin's movement is not certified" at that same point.
   - PIN-n-30 names only the "against" case, and that case also needs the CI to exclude 0 (E64).
3. **No values-check bullet in the entry.** It lists the values-check raw among the files committed but has no values-check bullet with counts and dispositions, as the 8e3bf91 and a61f13d entries do.
4. **No time stamp.** The entry gives no time for the run of record; none is needed under the dates rule.
5. **The run-of-record prediction is sound.**
   - The final file differs from the base only in the REPO line, which resolves to the same repository when run from REPO/scripts, and in PIN-n-30's text, which no check reads.
   - The battery's committed-blob checks use `bound=` handles (final:4373–4377), so the file's location changes no check.
   - When the run lands, check that its INVOCATION names REPO's scripts/n_analyze.py and that the committed blob hashes to a279a72d…e2a2.
6. **Pass 1's E57 evidence was partly wrong.** It said RD-POSITIVE never prints in M34 or M47; it prints once in each. The claims don't depend on it: their predicted RD-MERGED never prints.
7. **Cosmetic.** Entry L91–92 wraps early ("…(192/197, then" / "197/197)").
8. **No forbidden text.** None of the four texts contains a local path, the user name or a clock time.
9. **My conduct.** My only writes were extraction files under SCRATCH/vc/checker2/. A glob `rm` on an empty folder failed and deleted nothing. I read SCRATCH/vc/pending_corrections.md as supporting evidence for the foreground disposition.

### Code's dispositions of pass 2

Pass 2: 176 claims; 155 CONFIRMED, 4 IMPRECISE, 1 FAIL, 16 NOT CHECKABLE; all 15 of pass 1's dispositions carried,
14 true (E27's not wholly: it is this pass's FAIL). Every IMPRECISE and FAIL is applied.

- **E28 (FAIL), the entry's +1/2 wording.** Now: "At +1/2, which N1-P reads only where d_20 or d_eq sits there,
  G-LEAK-n's table otherwise keeps L alone." Observation 1's code text applied too: `plan_cells`'s docstring now says
  "+1/2 where d_20 or d_eq folds there". NUM-N1P-POINTS's description is left as it is: it describes shape (c), where
  d_eq folds into +1/2.
- **E64 (IMPRECISE) and observation 2, PIN-n-30.** The register's text (in the code) and the entry's summary now say
  that G-LEAK-n's certification has no CI condition, so SPECIFIC also follows a valence movement beyond the ceiling
  whose CI includes 0, and that where the cap binds the dose sentence names the movement as against the zone (its CI
  excluding 0) or as not certified (its CI including 0).
- **A8 (IMPRECISE), the close line on `a61f13d`'s entry: "where the addendum leaves the form to Code".** Now: "Its
  readings on what the addendum leaves to Code ...: of form, PIN-n-28 and PIN-n-32; of content, PIN-n-27, PIN-n-29,
  PIN-n-30 and PIN-n-31", each named.
- **R50 (IMPRECISE), the review raw's account of the edits before run 2.** Now names the two reader expectations with
  the digest and EXPECTED_CHECKS.
- **R59b (IMPRECISE), "STR-PINS counts".** Now: STR-PINS scans the source only for PIN and OPEN names and compares the
  registered names with those cited; the edits add or remove none (checked by tool: the counts of every PIN and OPEN
  name are equal between the mutant base and the final file).
- **Observation 3, no values-check bullet in the entry.** Added: the passes' figures and FAILs, the last pass's after
  it runs.
- **Observation 7, the early wrap in the entry's Runs bullet.** Reflowed.
- **The final file** now differs from the mutant base in three places: the repository line, PIN-n-30's text and
  `plan_cells`'s docstring. Its sha256 is `0ea4f894…be72` (full in the entry); both close lines carry it; the raw's
  head and §5 say three places.
- **Observations 4, 5, 6, 8 and 9:** nothing to apply (no time stamp is needed; the run-of-record prediction holds,
  and its INVOCATION and the committed blob will be checked when it lands; pass 1's E57 evidence is superseded;
  no forbidden text; the checker's conduct). **R27's cause:** the old kill table was made by an inline script in a
  shell command of this session, not a file, so pass 2 found none in SCRATCH; the regenerated table is from
  `raw/gen_table.pl` and the rebuilt `review/out_r1/kill_table.txt`.

## Pass 3: the report

### Values-check, pass 3: the v3 entry, two close lines and the review raw

**Result.** I checked 182 claims: 160 CONFIRMED, 3 IMPRECISE, 0 FAIL and 19 NOT CHECKABLE. Pass 2's dispositions are 11 items, counting its header. 10 are carried and true. The eleventh (R27's cause) is not checkable, but what can be checked of it is consistent. I did not grade the `__PASS3__` placeholder.

**Method.** I used read-only commands only: cat -n, sed -n, awk for extraction and line numbers, /usr/bin/grep, diff, cmp, `shasum -a 256`, wc, cut, sort, uniq, and name-only ls. On the git side I used rev-parse, `log --format` (ids, dates, subjects), `show --name-status` on six named commits, `show <commit>:<path>` (analyzer, schema, addendum, answers raw), ls-files on results/raw, and `status --porcelain` scoped to nine named paths (clean).
- I ran no Python, no perl and no repository code.
- I read, listed and searched nothing under data/.
- My extraction files are only under SCRATCH/vc/checker3/.

**Anchors** (abbreviated by cut):

| File | sha256 |
|---|---|
| SCRATCH/final/n_analyze.py | `0ea4f894…be72`, equal in full to entry L7 |
| REPO scripts/n_analyze.py = `git show bedc198:` = SCRATCH/review/base-bedc198.py | `34a513f9…98b6` |
| Frozen review copy, read-only (= SCRATCH/n_analyze.step2-198.py) | `1316f93a…dd06` |
| Mutant base SCRATCH/review/n_analyze.round1-base.py, read-only | `9e7faea1…e4ce`, equal in full to raw L460 |
| Step-1 draft (= SCRATCH/n_analyze.py) | `520b5112…1599` |
| SCRATCH/step2/n_analyze.py, now | `f073f7ad…72a3` |
| Schema: working tree = `d791bd9` | `0ea39600…0db6` |
| Schema at `14e65d8` | `4bed3f9a…4665` |
| Addendum | `e979f8f2…5e03` |
| Proposal | `30a3d0f5…04f4` |
| Answers raw | `ff2e5d89…ebec`, full value equal to close L4 |
| Routing raw | `ec54c56b…6a53` |

HEAD is `9662468`.

**Diffs.**
- Mutant base against final: exactly three hunks. They are `55c55` (the REPO line), `2045,2047c2045,2049` (PIN-n-30) and `2301c2303` (the `plan_cells` docstring).
- SCRATCH/step2 against final: line 55 only. So the two text edits were made in the working copy after the mutant run.

Below, "final:N" is SCRATCH/final/n_analyze.py, "base" is the mutant base and "frozen" is the review copy.

#### 1. entry.md

- **E1, L1.** Date 2026-11-16. **CONFIRMED** (every cited commit is dated 2026-11-16).
- **E2–E4, L1–2.** The nine questions at `8e3bf91`, the answers raw at `52b2c97`, ADDENDUM-n1 v0.1 at `a61f13d`. **CONFIRMED.** `--name-status` shows each file added there, and the subjects match.
- **E5, L2–3.** The pin moved from `14e65d8` to n-build's follow-up commit `d791bd9`. **CONFIRMED.** base-bedc198:1882 against final:2260; `d791bd9`'s subject reads "the schema's follow-up commit (v5) … settled with n-analyzer".
- **E6, L3.** Battery 207/207. **CONFIRMED, pending the run of record.** r1base1 has 207 PASS and 0 FAIL; final:968 sets `EXPECTED_CHECKS` = 207.
- **E7, L3.** Reviewed blind; 62 of 62 mutants killed. **CONFIRMED.**
  - All 62 .out files are complete and each has at least one [FAIL].
  - Each last line is x/y with x < y.
  - `--selftest` returns 1 unless ok (main, final:4900).
- **E8, L4.** PIN-n-27 to PIN-n-32 are Code's readings, flagged for the seat. **CONFIRMED** (final:1981–1982).
- **E9, L4–5.** Model-free; nothing ran on a model or the box; no stage ran. **NOT CHECKABLE.** Supporting: module-level imports are numpy and the standard library only, STR-NO-HEAVY passes, and every INVOCATION is `--selftest`.
- **E10, L6–7.** The full sha256. **CONFIRMED, pending the commit.**
- **E11–E13, L7–9.** `34a513f9…98b6` at `bedc198`; the schema pins; the proposal's sha. **CONFIRMED** (final:61, 2259–2260; git show hashes).
- **E14, L9–10.** The addendum, new, is bound by sha256 in four places. **CONFIRMED.**
  - VERDICTS: final:4800.
  - NOT-RUN: `not_run_doc`, final:3470, used by both NOT-RUN paths.
  - The artifact: final:4190.
  - `BOUND_RELS`: final:4150, used at 4232 and 4280.
  - The base contains no "ADDENDUM" at all, and already bound the proposal at all four sites.
- **E15, L10.** The commands are unchanged. **CONFIRMED.** main() (62 lines) and the docstring's command block are byte-identical to bedc198's.
- **E16, L11–12.** The run of record: 207/207, 210 ids, exit 0. **CONFIRMED, pending the run of record** (r1base1:207–209; see observation 5).
- **E17, L12–13.** The self-test raw's link. **NOT CHECKABLE** (pending; the file is not yet in REPO).
- **E18, L14–15.** The sources, and the OPEN register records each ruling. **CONFIRMED** (final:2061–2086).
- **E19–E21, L16–19.** Slopes through the origin over the nonzero points, the zero point refused, the with-intercept slope beside and marked descriptive. **CONFIRMED.**
  - Slopes: final:182–192, 2549, 2569, 2578–2584, 2607–2611, 353–358.
  - Zero point refused: final:190–191.
  - Descriptive flag: final:2554–2557.
- **E22, L19–20.** The two fits coincide to 1e-12. **CONFIRMED** (final:1948–1953; r1base1:144 shows a gap of 1.39e-17).
- **E23, L20.** 0.9164 and 0.3641 unchanged. **CONFIRMED.** The want dicts are identical (base-bedc198:1623–1624 against final:1961–1962); r1base1:145.
- **E24–E25, L21–22.** N1-P's four points; the plan derived with its keepers; a different schema plan refused. **CONFIRMED** (final:2268, 347–351, 2300–2322, 2402–2404).
- **E26, L22–23.** 7,680 reads in 138 cells. **CONFIRMED.**
  - Reads: 960 + 4,800 + 640 + 960 + 320.
  - Cells: 6 + 120 + 4 + 6 + 2.
  - RD-POSITIVE asserts both (final:2968–2973).
- **E27, L23–25.** P(d) is required at the certification points; its absence STOPs; no accepted plan can produce that. **CONFIRMED.**
  - `ceiling_cert` is used at final:444, 477, 479, 504 and 509.
  - An accepted plan gives N1-P exactly `n1p_points`, which holds every one of those points.
  - An incomplete or TAU/4-emptied N1-P makes N1, dose and N2 INDETERMINATE first.
- **E28, L25.** The +1/2 wording. **CONFIRMED.**
  - N1-P reads 0.5 only when d_20's or d_eq's resolved point is 0.5 (final:351).
  - Otherwise `st.P.get` gives L alone (final:766–767), which agrees with the comment at final:369.
- **E29, L26–27.** Q3. **CONFIRMED** (final:641–646, 548–549).
- **E30–E31, L28–29.** 385 tuples and 1,921 evaluations; four coupling shapes with 28, 25, 24 and 17 triples. **CONFIRMED.**
  - r1base1:114–131 and 179.
  - Recounted by hand from `map_reach_by_hand`: 24+4, 21+4, 20+4 and 6+3+4+4.
  - bedc198 had shapes a, b and d only (base-bedc198:1421).
- **E32, L30–31.** Q6. **CONFIRMED** (final:471–474, 498).
- **E33–E34, L32–34.** Q7, and the beside certified each on its own. **CONFIRMED** (final:330–345, 496–517).
- **E35, L35–37.** §7.6's forms asserted against the addendum's italic spans. **CONFIRMED** (final:1387–1403 and 895–907, against addendum L73–76).
- **E36, L37–39.** The sign rule. **CONFIRMED** (final:453, 456–457, 480–481, 2714, 649–652).
- **E37, L39.** The forms' digest `209d7b46…92f5`. **CONFIRMED** (final:2677).
- **E38, L40–41.** Secondary (b)'s text. **CONFIRMED.** It is identical to `B_STRUCK` (final:588–589), which is used at 2804.
- **E39–E40, L42–44.** The schema's forms; `loads_ms` in VERDICTS' counters. **CONFIRMED.**
  - Schema: 286, 295, 773, 788, 77, 821, 1100, 1118, 1161, 1192–1193.
  - Analyzer: final:4849–4851; VD-COMPLETE at 3711.
- **E41, L44–46.** The captures are bound by hashes, no array is read, and an unnamed file is refused. **CONFIRMED.** final:2377–2395, 4555, 4618–4621; there is no `np.load` in the file.
- **E42, L47–48.** The review raw's link. **CONFIRMED, pending the commit.**
- **E43, L49.** The frozen copy at 198/198. **CONFIRMED.** Its hash matches, its mode is read-only, s2run2 gives 198/198, and frozen:967 sets 198.
- **E44a, L49–50.** "A subagent of this session". **NOT CHECKABLE.**
- **E44b, L50.** The brief quotes the list of record v2, items 1–5. **CONFIRMED.** SCRATCH/review/BRIEF.md:79–83 are byte-equal to REPO's list-of-record raw, L18–22.
- **E45–E47, L50–54.** The reviewer's findings, severities and predictions. **CONFIRMED** (report.md; grep counts 19 survive and 21 killed).
- **E48, L55–56.** The fixes, and nine new checks of which three compare filled sentences with literal text (6 dose, 2 N1, 4 N2). **CONFIRMED.**
  - The frozen-to-base diff has 39 hunks.
  - Nine coverage ids were added (201 to 210), and checks went from 198 to 207.
  - The literal-text checks are at final:1457–1522.
- **E49–E50, L56–58.** F1, F2, F7 and F3 registered; F11 kept; the plan-refusal case added. **CONFIRMED** (`_SmPlan`, final:3368–3377; the frozen copy has no such case).
- **E51, L59.** M01–M40 re-express V01–V40. **CONFIRMED.**
  - I extracted all 40 V blocks from report.md: 39 are byte-equal to the M files.
  - M17 differs only on its fixed line, which occurs once in the base.
- **E52, L59–61.** M41–M62 are on the fixes and changed code; only M54 and M62 share lines with the reviewer's mutants. **CONFIRMED.**
  - No M41–M62 old line exists in bedc198.
  - M45, M46 and M55 sit on lines that are absent from the frozen copy.
  - M54.old = M38.old and M62.old = M27.old; there is no other overlap.
- **E53, L61.** One run on `9e7faea1…e4ce` at 207/207, and 62 of 62 killed. **CONFIRMED.**
- **E54, L62.** M20–M62 each killed by its predicted check, directly or through its group's exception. **CONFIRMED.**
  - 37 of the predicted checks are among the first six unreached ids.
  - M27 failed directly at out:80, and M43 at out:134.
  - M34 and M47: RD-MERGED never prints; the reader path raised at out:165.
  - M35 and M52: RD-POSITIVE never prints; the group raised at out:155.
- **E55, L62–63.** M01–M19 each killed by an added or extended check. **CONFIRMED.** Each list is complete (two ids at most); M11 and M18 are the two killed by extended checks.
- **E56, L64–66.** The committed bytes differ from "the mutated base" in three places. **IMPRECISE.**
  - The three places are right (pending the commit).
  - "Mutated base" misnames it: the base was never mutated. The raw calls it the "mutant base" or the "mutation-tested base", and the entry uses "mutated" only here.
  - Fix: "the mutant base".
- **E57, L67–68.** The values-check raw's link. **NOT CHECKABLE** (pending).
- **E58a, L68–70.** The briefs quote list v2 items 1–5, allow no Python, cover the four texts, and each later pass checks the last pass's dispositions. **CONFIRMED.**
  - All five items are byte-equal in BRIEF.md, BRIEF2.md and BRIEF3.md.
  - No Python: each brief's line 51.
  - Dispositions check: BRIEF2 and BRIEF3, lines 83–85.
- **E58b.** "Each a subagent of this session". **NOT CHECKABLE.**
- **E59, L71.** Every IMPRECISE and FAIL was applied. **CONFIRMED for passes 1 and 2.** Pass 1's 8 and 2, and pass 2's 4 and 1, are each in the current texts. Pass 3 is pending.
- **E60–E61a, L72–74.** Pass 1's figures, and its two FAILs. **CONFIRMED** (pass1.md:216, 175–178, 194–197).
- **E61b, L72–73.** "Group exceptions Code's table script cut to one word". **NOT CHECKABLE.** The script was inline; see observation 2 on the wording.
- **E62–E63, L75–76.** Pass 2's figures, all 15 carried, and its FAIL. **CONFIRMED** (pass2.md:3, 55, 233–241).
- **E64, L78–79.** Strikable until LOCK-n v1.0, and the sixteen PINs accepted. **CONFIRMED.**
  - The register keys are 7, 8, 11, 12, 14 and 16–26.
  - Answers raw §2 accepts the prebuild's nine §3 readings (PIN-n-7, 8, 11, 12, 14, 16, 17, 18 and 19 by content), plus PIN-n-20 to -26 with -12 and -16 amended.
- **E65–E71, L80–100.** The summaries of PIN-n-27 to -32 and of F11. **CONFIRMED.**
  - Register text: final:2029–2059.
  - Code paths: 457, 481, 637–638, 498–500, 382–384, 504–507, 2711.
  - The forms: 564–565 and 590.
  - The proposal's G-LEAK-n rule (L122) has no sign and no CI condition. See observation 1.
- **E72, L101–104.** The run conditions and the background batch. **NOT CHECKABLE.**
  - run_mutants.sh:18 runs `nice -n 19 … -I` in a sequential loop.
  - The battery's TemporaryDirectory calls have no `dir=` (2964, 3620, 4357).
  - The M08 and M09 outputs are complete.
- **E73, L104–105.** The run counts. **CONFIRMED.** These are the only INVOCATION-bearing outputs in SCRATCH/n9/v3: 192/197, 197/197, 197/198, 198/198, 207/207, and 62 mutant outputs. The run of record is pending.
- **E74–E76, L105–108.** Q-F3 running beside the battery runs; the committed-by-path list; "Not pushed". **NOT CHECKABLE.**
- **E77, L108–109.** "Next". **CONFIRMED** (answers raw L59).

#### 2. close_8e3bf91.md

All 11 claims are **CONFIRMED.**
- **C1, L1.** PI date, second sitting (routing raw L6).
- **C2, L1.** The n-analyzer session's line, per the n-ganl raw's header. Both n-ganl raws' headers name the n-analyzer session, and the coordinating session's close (RESULTS.md L2527) says the n-analyzer session adds its close line here.
- **C3, L2–4.** The link, the full sha256, and `52b2c97`.
- **C4, L4–5.** "Rule this block's nine questions".
- **C5, L5–7.** The routing raw was added at `a61f13d`.
- **C6, L9.** Item 9 is byte-identical to the routing raw's L29 once the quote marker and its single leading space are stripped (cmp).
- **C7, L11–13.** The order follows answers raw §3, items 1–3 (L56–58).
- **C8, L13.** `0ea4f894…be72` (pending the commit).
- **C9, L13–14.** The OPEN register, and the sixteen PINs as accepted (final:1981–1982).
- **C10, L14–16.** Six readings, PIN-n-27 to -32, and the entry's title.
- **C11, L16–17.** §3 step 4 waits for G-CAL-n's dose map.

#### 3. close_a61f13d.md

All 8 claims are **CONFIRMED.**
- **A1, L1.** Per the addendum's header (L4; RESULTS.md L1436).
- **A2, L2.** The sha256, committed with this line (pending the commit).
- **A3, L2–4.** The four binding sites (as E14).
- **A4, L5.** §4 in the section's words: `B_STRUCK`'s two clauses are addendum L40's, the first letter's case aside.
- **A5–A7, L6–11.** §5.2–§5.3, §6 (the schema enforces `kfold10` at schema:1482) and §7.1–§7.6.
- **A8, L13–15.** PIN-n-28 and -32 are about form; PIN-n-27, -29, -30 and -31 are about content.

#### 4. The review raw

**Head**
- **R1–R3, L1–8.** The title, the entry's title, the hashes and the commits. **CONFIRMED.**
- **R4a, L8.** Two steps. **CONFIRMED.**
- **R4b.** Each step ran in a granted window. **NOT CHECKABLE.**
- **R5–R6, L10–14.** Step 1's and step 2's contents and runs. **CONFIRMED.**
  - The step-1 draft pins `4bed3f9a` (step1:2111) and keeps N1-P's row as (+1, −1) (step1:2119).
  - The frozen copy adds `ceiling_cert`, N1-P's four-point row, the keepers, per-layer `capture_files`, `loads_ms` and the `d791bd9` pin.
- **R7, L15–16.** The frozen read-only copy at 198/198 on the working copy. **CONFIRMED.** That it was frozen unchanged after its run cannot be checked: the working copy has since changed.
- **R8a.** "A subagent". **NOT CHECKABLE.**
- **R8b–R9, L17–19.** The brief quotes list v2, allows no Python, and lists the spec. **CONFIRMED** (BRIEF.md:61, 76–83, 15–24).
- **R10, L19–20.** Executed no code. **CONFIRMED as the reviewer's self-report.**
- **R11–R15, L21–32.** **CONFIRMED** (as E45–E55).
- **R16, L33–35.** Three places. **CONFIRMED, pending the commit.**
- **R17, L37–39.** The run conditions. **NOT CHECKABLE.**
- **R18, L40–41.** One unique replacement per fresh copy; "killed" means a non-zero exit. **CONFIRMED.** run_mutants.sh:11–21, and each Mnn.py is the base plus exactly one hunk equal to .old → .new.

**§1, the reviewer's report**
- **R19, L45.** "Saved by script". **NOT CHECKABLE.**
- **R20, L45–46.** Headings moved down two levels, nothing else changed. **CONFIRMED.** Raw L50–396 with the headings shifted back equals report.md, apart from report.md's missing final newline.
- **R21, L46.** The line numbers are the frozen copy's. **CONFIRMED** (11 citations checked).
- **R22, L46–48.** The bottom line against F5. **CONFIRMED.**

**§2, the dispositions**
- **R23.** §2 equals review/dispositions.md apart from its heading and a trailing blank line. **CONFIRMED.**
- **R24, F1.** **CONFIRMED.**
- **R25, F2 (L406–408).** **IMPRECISE.**
  - It reads "PIN-n-30 now names … its co-occurrence, when the cap binds, with a dose sentence naming the same movement as against the zone".
  - That is the base's wording, and the same condition-free claim pass 2 graded IMPRECISE in the entry (E64).
  - Under the cap, the dose sentence names it as against the zone only when the CI excludes 0 (final:481). With a CI that includes 0, it says "not certified".
  - The committed register (final:2045–2049) states both, and §5 records the change, but §2 still says "now".
  - Fix: add "(amended twice since by the values-check: §5)", or state the two alternatives.
- **R26–R45: F3–F11, B1–B10 and "Beyond".** **CONFIRMED.**
  - Code: 474, 510–512, 2054, 403, 4187, 2557.
  - Checks: 1198–1206, 1210–1215, 1277–1291, 1358–1366, 1457–1522, 3113–3129, 4443–4444.
  - B10's texts: 3100–3102, 1418–1420, 1967, 2931, 3175–3176.
  - `_SmPlan`; M51 is killed by RD-REFUSE alone.

**§3, the mutants**
- **R46–R47, L454–461.** **CONFIRMED.**
- **R48.** Each mutant ran once, one process at a time. **NOT CHECKABLE.**
- **R49–R51, L461–464.** All killed; what the "killed" column means; thirteen runs with a group exception. **CONFIRMED.** The battery prints `unreached[:6]` of a sorted list (4135–4136), and marks an id reached only on a PASS (1034–1038). Thirteen outputs have "group raised".
- **R52, M03.** **CONFIRMED** (out:112).
- **R53, M27 (L467–469).** **IMPRECISE.**
  - It says "the reachability checks before the raise had failed". Only four of the six did: out:53–56, the no-raise check and shapes (a) to (c).
  - REACH-DOSE-IFF-N1 (out:52) and shape (d) (out:57, where d_eq sits at +1 and P exists) passed.
  - The rest of the note is right: out:2, 39 and 58; d = 1/3; NUM-N1P-POINTS at out:80.
  - Fix: "four of the six reachability checks before the raise had failed (shape (d)'s and the dose-iff-N1 check passed)".
- **R54–R62: M29, M34, M44, M52, M35, M43, M47, M48, M50, M55, M57.** **CONFIRMED.**
  - M29: 0.625 is d_20 at R_ell 23.90625 and R 25.5.
  - M44: 0.49000000000000005 and 0.5228758169934641 are d_eq on the R_ell 37.485 and 40.0 maps, each folded into +1/2; NUM-N2-POINTS failed at out:152.
  - M48: the accepted case at 3366 is not wrapped, so it raised.
  - M50: the SchemaError comes from `check_gread` via `_bt_gread_for` (3597).
- **R63.** The table's descriptive columns. **CONFIRMED.** Rebuilt, they equal headers.txt for all 62 rows, and "From" is right.
- **R64.** The Result column. **CONFIRMED.** Rebuilt from every .out's coverage line and its "group raised" lines: 0 differences. kill_table.txt also equals the rebuild.
- **R65–R66.** The M41–M62 blocks and the M17 block. **CONFIRMED.** They are byte-equal to mutants_r1 and mutants_c, and M41's empty new text deletes.

**§4, the battery runs**
- **R67, L698–700.** The run conditions. **NOT CHECKABLE.**
- **R68, L700.** The runs used the working copy. **CONFIRMED** from the INVOCATION lines.
- **R69, L702–707.** Run 1's failures and the edits before run 2. **CONFIRMED.**
  - run1:104 is the digest; 155 and 162 are the two reader expectations; 197 is coverage, listing exactly those three; 198 reads "197 == EXPECTED_CHECKS 185".
  - base-bedc198:866 sets 185.
- **R70, L708–709.** Step 2's runs. **CONFIRMED** (s2run1's only FAIL is the count).
- **R71, L710.** One run, then the 62 mutants. **CONFIRMED.**
- **R72–R74, L711–717.** The failed first attempt, the background batch, and the run of record. **NOT CHECKABLE.**
  - Consistent with the files: `cp -f` copies of a read-only base, and the runner now does `chmod u+w` and an `APPLY-FAIL` continue.
  - The batch arithmetic works: 8 × 6 + 5.

**§5, the committed bytes**
- **R75, L721.** Three places. **CONFIRMED, pending the commit.**
- **R76, L722–727.** The quoted line equals final:55 (cmp), and every commit of the file uses it: bedc198:54, 2822721:49, 5c0ae6b:49. **CONFIRMED.**
- **R77–R78, L728–733.** The two text edits and their sources. **CONFIRMED** (pass1.md:223; pass2.md:100–103, 245–250; final:2045–2049, 2303).
- **R79–R81, L735–737.** No logic changes and no check reads these words. **CONFIRMED.**
  - STR-PINS (2240–2247) strips the registers and compares name sets.
  - The PIN and OPEN name counts are equal between base and final, and the changed lines contain none.
  - PINS appears only at 2246, 3471, 4197, 4446 and 4804.

#### 5. Pass 2's dispositions

- **D0, the header** (176 claims; 155/4/1/16; 15 carried, 14 true; all applied). **True.**
- **D1, E28.** **Carried** (entry L25, word for word). **True.** The `plan_cells` docstring (final:2303) is applied too. Leaving NUM-N1P-POINTS alone is right: its text (1915–1917) describes the test maps shape by shape.
- **D2, E64 and observation 2.** **Carried** into the code (2045–2049) and the entry (L88–92). **True.** It does not claim raw §2, which keeps the earlier wording (R25).
- **D3, A8.** **Carried** (close L13–15). **True.**
- **D4, R50.** **Carried** (raw L705–706). **True.**
- **D5, R59b.** **Carried** (raw L735–736). **True**; I repeated the count check by tool.
- **D6, observation 3.** **Carried** (entry L67–77). **True.**
- **D7, observation 7.** **Carried** (reflowed). **True.**
- **D8, the final file.** **Carried.** **True**: three places, the sha256, both closes, and the raw's head and §5.
- **D9, observations 4, 5, 6, 8 and 9.** **True.** I re-checked observation 8, and observation 5 still holds with the third difference (observation 5 below).
- **D10, R27's cause.** **NOT CHECKABLE**: the inline script left no file. What can be checked is consistent: gen_table.pl uses `([^=]+)`, and kill_table.txt equals the rebuild from the .out files.

#### Counts

| Text | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE | Total |
|---|---|---|---|---|---|
| entry.md | 69 | 1 | 0 | 10 | 80 |
| close_8e3bf91.md | 11 | 0 | 0 | 0 | 11 |
| close_a61f13d.md | 8 | 0 | 0 | 0 | 8 |
| review raw | 72 | 2 | 0 | 9 | 83 |
| **All** | **160** | **3** | **0** | **19** | **182** |

#### Observations outside the claims

1. **PIN-n-30 has a third, edge condition** (the code's text and the entry's L91–92). I did not grade it.
   - A standing pause on N1-V's, N1-R's or N1-P's reads, with those arms complete, is possible only at a PI-STOP end (PIN-n-24).
   - Then N1, and so dose, are INDETERMINATE while N2 is still evaluated (final:499–500; r1base1:52 asserts this "when the cap binds").
   - So, where the cap binds, SPECIFIC's "does" can stand beside a dose sentence that names no movement at all.
   - Nothing contradictory gets printed. For completeness the PIN could add "where the dose question is evaluated".
2. **Entry L72–73 wording.** "Whose group exceptions Code's table script cut to one word" reads as truncation, but the rows lost the exception entirely (pass 1's R27). Suggest: "whose kill-table script read a group's name as one word, dropping the 'reader path' group's exceptions from seven rows".
3. **PIN-n-32 nit (and entry L95–96).** The text says the NOT-DETECTABLE forms "print Δm(d_eq)". Under the sign rule the clause is `MOVE_AGAINST`, which prints "Δm = [x]" without "(d_eq)". The point about the missing "read at d = …" note is unaffected.
4. **§2 of the raw.** F2's line (R25) is the only disposition there that no longer describes the committed register. F1, F3, F7 and F8 still do.
5. **The run-of-record prediction holds for all three differences.**
   - The REPO line resolves to REPO when run from REPO/scripts.
   - No check reads the PIN text or the docstring: the forms digest covers forms only, and `analyzer_sha256` is compared only with itself at run time.
   - The committed-blob checks use `bound=` handles (4091–4095, 4376–4377, 4400–4402).
   - When the run lands, check that its INVOCATION names REPO's scripts/n_analyze.py, that it shows 207/207 with 210 ids, and that the committed blob hashes to `0ea4f894…be72`.
6. **"The n-ganl raw's header"** (close_8e3bf91 L1) could mean either n-ganl raw. Both headers name the n-analyzer session, and the coordinating session's close uses the same form, so this is harmless.
7. **No forbidden text.** None of the four texts contains a local path, the user name, an IP or port, or a clock time (grep).
8. **My conduct.**
   - I ran `ls -l`, piped to print only mode and name, on three SCRATCH analyzer copies to check their read-only mode. Nothing under data/ was involved.
   - The harness refused one compound shell loop: it could not parse a zsh expansion, and the command contained no removal. I rewrote it without that expansion.
   - Two zsh slips (`echo ======`, and `$c:scripts`) printed errors and ran nothing else.
   - My only writes are under SCRATCH/vc/checker3/.

### Code's dispositions of pass 3

Pass 3: 182 claims; 160 CONFIRMED, 3 IMPRECISE, 0 FAIL, 19 NOT CHECKABLE; pass 2's dispositions carried and true,
one (R27's cause) not checkable. With no FAIL it is the last pass. Its three IMPRECISE and three of its observations
are applied, with one change from outside the check, and each edit after it is checked by tool rather than by a
fourth pass:

- **E56 (IMPRECISE), "the mutated base".** Now "the mutant base".
- **R25 (IMPRECISE), the raw's §2 on F2.** The disposition now adds that the values-check amended PIN-n-30's text twice
  since, pointing to §5 for the text as committed; F8's disposition likewise points to §5 for PIN-n-31.
- **R53 (IMPRECISE), the raw's §3 note on M27.** Now: four of the six reachability checks before the raise had failed;
  the dose-iff-N1 check and shape (d)'s passed. Checked by tool: M27's output, lines 52–58 (two PASS, four FAIL, then
  the group's raise).
- **Observation 1, PIN-n-30's edge condition.** The register's text and the entry's summary now say the dose sentence
  names the movement "if the dose question is evaluated".
- **Observation 2, the entry's account of pass 1's table FAIL.** Now: the kill-table script read a group's name as
  one word, dropping the "reader path" group's exceptions from seven rows.
- **Observation 3, PIN-n-32's "print Δm(d_eq)".** The register's text and the entry's summary now say the forms print
  the figure of the point read as Δm(d_eq), or as Δm under the sign rule.
- **Observations 4–8:** observation 4 is R25's; 5 holds (the run of record is checked when it lands); 6 is left as it
  is (both n-ganl raws' headers name this session, and the coordinating session's close line uses the same form);
  7 and 8, nothing to apply.
- **From outside the check: PIN-n-31's dependency.** n-build's BUILD, committed at `83a50a0` (parent `9662468`),
  declares the PIN PIN-n-31 rests on (its entry: "G-READ-n's driver reads captures only through `cells.load_cell(...,
  keep_arrays=True)`"). PIN-n-31's text, the entry's summary, the raw's §5 and its §2 note on F8 now cite it. (n-build
  first committed it as `824fc3f` and amended that unpushed tip at the coordinating session's verification, to scrub a
  session id from its values-check raw; `git diff --name-only 824fc3f 83a50a0` names that raw alone.)

**The edits after this pass, checked by tool:**
- the analyzer (`SCRATCH/final/n_analyze.py`, sha256 `97097ce0…251e`): against the mutant base, `diff` gives the
  repository line and the hunks of PIN-n-30's, PIN-n-31's and PIN-n-32's texts and `plan_cells`'s docstring, nothing
  else; every PIN and OPEN name occurs as often as in the base; the working copy equals it but for the repository
  line; no line in the changed register exceeds 120 characters;
- PIN-n-31's citation: RESULTS.md at `83a50a0` holds the declaration (`git show 83a50a0:RESULTS.md`; its lines 229 and
  717);
- the texts: the entry, both close lines and the review raw carry the new sha256 and no earlier one, "three places"
  and "the mutated base" nowhere (grep).
