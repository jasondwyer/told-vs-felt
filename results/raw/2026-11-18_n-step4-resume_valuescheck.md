# n step 4 — the resume's STOP block and entry: the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over two drafts:
- T1, the block for the seat (`results/raw/2026-11-18_n-step4-resume_code-to-design_STOP.md` as drafted), sha256
  `fb610289…446f`;
- T2, its entry, `d83f09a1…cdd7`.

**The checker's brief:**
- named the sources:
  - the resume's output, its record, exit file and work files;
  - the first attempt's output, record and exit file;
  - the three box scripts and driver v2f;
  - the seat's answers of the third sitting, the ruling raw, ADDENDUM-n2 and ADDENDUM-n1;
  - `RESULTS.md`'s entries, and git history;
  - the coordinating session's words, which are in no file, quoted verbatim;
- said the resumed report was not yet on the laptop, and that its sha256 and its `p01` line are checkable from the
  output;
- quoted the list of record v2's items 1–5, verbatim;
- required item 3's pathspec and the `data/mf3` exclusion on every git command over the tree; that a glob is expanded
  and read before it is looped over; and tracked status by `rev-parse` against `hash-object`;
- barred any interpreter, any write, any network and any guard marker in an argv; anything under `data/mf3`,
  `data/*/ckpt` or `data/*/reports`; and, in Code's scratch, anything but the named files.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (207 lines, sha256
`e0652b68…afdde`). It names no local path.

**Totals:** 140 items — 121 CONFIRMED, 8 IMPRECISE, 3 FAIL, 8 NOT CHECKABLE — and 17 observations.

**The checker's departures,** as its report states them, for the seat to class. None touched `data/`, any guard
marker, or anything in Code's scratch beyond the named files:
- `git log -1 --format=%B 1272702` (with the pathspec), piped to a count of non-ASCII bytes: a commit body, beyond item
  1's ids, subjects and times;
- a name-only `ls results/raw` piped to a grep, to find the corpus answers;
- reads beyond the named sources: the corpus answers, the v2f self-test raw, `valence_core/n/ids.py` (a grep),
  `.gitignore` (a grep and `git show 6df2131 -- .gitignore`), `git diff --name-status 6df2131^ 6df2131 -- .gitignore
  .gitattributes`, and `git blame` on `RESULTS.md`;
- `wc -c` on the committed ruling raw;
- `/usr/bin/grep -P a /dev/null`, an option test;
- `sed`, `diff` and `cmp`, with no grep, on named scratch files.

## 1. Dispositions

**The three FAILs, all applied:**
- **60** (T1 §3). Now: "The fix was v4's plain `cp`. The check after the copy is v3's sha256 mismatch count,
  unchanged; v2 compared each copy by `cmp -s`, and v3, relayed after the hold, kept `cp -p` and never ran."
- **70** (T1 §4). Now: "to within 3.1e-7 (q3's 3.004e-7 the largest)".
- **97** (T1 §8). Now: "The resumed report's commit, with this block; the cell, unchanged, is not committed again
  (§9)."

**The IMPRECISE items, all applied, in the checker's words:**
- **31**: "§4.1's figures of record would be:";
- **37** and **81**: "the seat's corpus answers of 2026-11-18, §5.5", in §1 and §5. §1 also says that the printed
  line's "the seat's answers of 2026-11-18, §5.5" is the driver's citation of those answers;
- **47**: "G-VER PASS; the load (707/707); the backend line, … R6's bridge …, and the load at 12,150 ms";
- **65**: "0.038 and 0.039 nats";
- **73**: "The distribution is the run of record's": the resume is skip-only, its distribution comes from the same 24
  records, and its own forwards agree with them (in-band 6 of 6);
- **79**: "A count under another bound needs a driver that takes that bound (v2f's comparison takes R3's bound alone,
  `label.max`) and the comparison run again on the box";
- **121** (T2): "(the seat's corpus answers of 2026-11-18, §5.5)".

**The NOT CHECKABLE items:**
- **18**, the report's read. Done after the report arrived: Code checked its sha256, `dd217d78…ce79`, and read its
  `cells` record and its pauses only. The one cell is at `80770a19…78ea`, with 24 records and its 31 capture digests
  equal to `6df2131`'s. The one pause is `p01`, adjudicated under `e2b1c77a…2a8a`.
- **55**, the hold's timing. It now reads in the checker's suggested form.
- **23**, **129**, **132**, **134**, **136** and **140** are Code's own conduct, the harness, the gate and the commit
  to come. They stand as declared.

**The observations, all applied:**
1. The report: read after it arrived (item 18), and T1's sources say so.
2. Q3 now says that running the comparison under another bound takes a driver change, its commit, and one load.
3. §5 quotes the corpus answers' §5.5 on the medians' purpose. It is quoted, not applied.
4. T1's sources are completed. They now include the third sitting's §1.2, ADDENDUM-n2 §0.2 and §3–§5, the corpus
   answers, the `RESULTS.md` entries of `1272702`, `7a54eb9` and `f3e7190`, the block of `6df2131`, the driver and
   the box scripts, ADDENDUM-n1's sha256 `e979f8f2…5e03`, and the first attempt's output by name.
5. v3 is named in T1's sources and §3: relayed after the hold, never run.
6. T1 §3 records the copy check's change from `cmp` to the digest form, both within the coordinating session's form.
7. T1 §2: the box's 389 is the count `1272702`'s self-test raw predicted.
8. T1 §2: n's identifier `8264f719efd347a9`, the load at 12,150 ms, and the two library warnings.
9. T1 §4 item 5, a measured fact declared without adjudicating. The margin's largest discordance printed in nats is
   0.0625. The seat's texts give "at most about 0.09", and on the printed figure ADDENDUM-n2 §2.1's "about three times"
   is four times.
10. Neutrality:
    - (a) "backend-ext-2 does not run now", in T1 and T2;
    - (b) item 1 reads "Code reads that as fitting the seat's §1.3";
    - (c) Q1's pointer to §4 is removed.
11. "under each space form".
12. "the extension median rel, 0.0132 (§3, §4.2)".
13. "launch-script defect" throughout.
14. T1 §3: the probe's `cp -p` created its destination, so the failed copy may hold the report's bytes; its cleanup is
    the PI's call.
15. Style, after `6df2131`'s forms:
    - (a) T1 §1 lists the reads the seat needs, the report as the read domain, and the cell as not for reading;
    - (b) T1 §9 gives the committed paths, sha256s and line counts;
    - (c) the short form says "Code adjudicates nothing";
    - (d) T2's header has its "Block:" link;
    - (e)–(h) T2 has a Model bullet, the box at the end, what Code read of the report, and that the pod session's
      records state no departure of its own.
16. T2: the two departures at `1272702`'s commit are "declared here for the first time (that commit's message names
    one departure)".
17. All nine copied-back files are committed, on the coordinating session's word. T1 §2 gives the independent checks
    (the hashes file equals the identity file; `resume.txt` is the output's lines 54–65).

## 2. The edits after the check, checked by tool

- **The diffs.** T1 was rewritten whole to take the dispositions. Code read the full `diff -U0` of each final text
  against its checked draft:
  - T1 has 24 hunks, and each is one of §1's dispositions, two of them a renumbered cross-reference (§4 items 6 and 7);
  - T2 has 8 hunks, each a disposition or the filled lines of this check.
- **The block's verbatim lines** equal the resume's output lines 61–65.
- **The quotes.** Every quote in T1 is found, joined across wrapped lines, in its source: 24 of 24. The sources are
  the seat's answers, the ruling raw, both addenda, the corpus answers, `RESULTS.md`, the box outputs, and the
  coordinating session's words as filed in Code's scratch. T2's are found too, 2 of 2.
- **The finals:** T1, sha256 `bbab730e…bcfb`, 211 lines; T2, `b5bea2f7…ab95`, 87 lines.
- **The commit's gate** re-runs these checks on the staged blobs. It also checks the nine raws against the pod
  session's sha256s, and the report by blob id and by its read domain. Its scrubs print counts only, and the
  commit-time count of the home-folder prefix must be 0.

## 3. The report as returned

```text
BLIND VALUES-CHECK of T1 (stop.md) and T2 (entry.md)

Both texts hash to the digests in the brief: T1 is fb610289…446f and T2 is d83f09a1…dd7. I did not check the placeholders @VC_DEPARTURES@ and @VC_LINE@.

Abbreviations used below:
- v4out = S/step4b/resume4/out/bext_resume_v4_out.txt
- v4rec = resume4_box_run.txt
- v2out = S/step4b/resume2/out/bext_resume_v2_out.txt
- v2rec = resume2_box_run.txt
- v2.sh, v3.sh, v4.sh = the frozen box scripts
- ans3 = results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md
- corpus-ans = results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md
- A-n1, A-n2 = the two addenda
- drv = scripts/n_sessions.py at HEAD (tracked and clean; equal to 1272702's blob)
- STOP-6df = the 6df2131 block

ITEMS

T1:
1. L1, the title (resumed under the ruling, COMPLETE, no candidate at 40 of 40). CONFIRMED: v4out L61, L65, L69.
2. L3, "The n-build session (Code), PI date 2026-11-18. For the PI to route." CONFIRMED: same form as STOP-6df L3.
3. L5, pod emw1e4embiwe9b, the H100 SXM of the BACKEND entry d5d08fa. CONFIRMED: v4out L60; v4rec L1; the subject of d5d08fa ("BACKEND -- characterization … pod emw1e4embiwe9b, an H100 SXM").
4. L5–6, run on the third sitting's §1.4 and the PI's "Route as given". CONFIRMED: v4rec L1–4; ans3 L20; RESULTS.md L153; (c1).
5. L6, "No lock is in force." CONFIRMED: drv L580 has lock_sha256 None; A-n2 §6.3 (5) still has the lock to be drafted.
6. L7, driver v2f committed at 1272702, e29839c8…1152. CONFIRMED: `git show 1272702:scripts/n_sessions.py | shasum` gives e29839c8…1152; v4out L56.
7. L7–8, the committed texts at 7a54eb9 and f3e7190 call it v2e. CONFIRMED: RESULTS.md L223–226 (blame 7a54eb9) and L473–481 (blame f3e7190).
8. L8, box script v4 is 4fec8670…dd78. CONFIRMED: shasum.
9. L8–10, a fresh sparse copy at 1272702 holding byte copies of the report, the cell file and 31 arrays, checked by sha256 with 0 mismatches. CONFIRMED: v4out L4 and L8; v4.sh L101–117; v4rec §3.
10. L10, the command `backend-ext --resume --ruling p01=…`. CONFIRMED: v4.sh L145.
11. L10–11, the ruling raw committed at 3b2b855, e2b1c77a…2a8a. CONFIRMED: `git show 3b2b855:<ruling>` hashes equal; 3b2b855 touches that path.
12. L11, the run copy at ad856f0 was only read. CONFIRMED: v4.sh only rev-parses, hashes and copies from $RR; v4out L2 and L73.
13. L12–13, v2 (f166e7ce…19f2) failed at its copy-in on `cp -p`, and nothing of the stage ran. CONFIRMED: shasum; v2out L7–9; exit file 1; v2rec L8–12.
14. L16, v4 output 8d286ce4…2a39, 74 lines. CONFIRMED: shasum; wc -l gives 74.
15. L17, the pod record of it, c86e812a…be14. CONFIRMED: shasum.
16. L18, the v2 output 0c926ca3…bf79 (9 lines) and its record 2f606ca7…1ce9. CONFIRMED: shasum; wc -l gives 9.
17. L19, the resumed report's sha256 dd217d78…ce79. CONFIRMED: v4out L71.
18. L19, that Code read the report's "cells record and its pauses only". NOT CHECKABLE: the report is not in S. v4rec L111–112 says it "goes later, by hash only".
19. L20, ans3 is d51279ec…0bf4 (third sitting), and its §1.3, §1.4 and §3 exist. CONFIRMED: shasum; blob at 3b2b855 equal.
20. L21, A-n2 is 41f76c49…bb3f, committed at 7a54eb9, with §1, §2 and §4. CONFIRMED: shasum; 7a54eb9 blob equal; 7a54eb9 touches the file.
21. L22, A-n1 §2 is the rule. CONFIRMED: A-n1 L30–32.
22. L24, the cell path and 80770a19…78ea, unchanged by the resume. CONFIRMED: v4.sh L71; v4out L72.
23. L24, "hashed only". NOT CHECKABLE: no source records Code's handling of the cell.
24. L24–25, the 31 arrays stay on the box's volume. CONFIRMED: v4rec §7 (only 5 files copied back) and §8.
25. L29–30, COMPLETE skip-only, no read re-launched, p01 adjudicated under the ruling's sha256, cell and arrays unchanged. CONFIRMED: v4out L61, L67, L69, L72.
26. L31–32, §1.4's list was printed, with the in-band count 6 of 6. CONFIRMED: ans3 L20; v4out L62–64.
27. L33, the counts bare 0, space 16, bare+eot 0, space+eot 16. CONFIRMED: v4out L64.
28. L34, the quote "none, or more than one, goes to the seat with the four counts". CONFIRMED: A-n1 L32.
29. L34–35, "no backend-ext-2, and nothing more runs on the box". CONFIRMED: (c3). See observation 10a on neutrality.
30. L36–37, the 24 reads ran under "bare". CONFIRMED: v4out L54.
31. L37, "§4.1's candidates are". IMPRECISE: A-n2 L34 calls these "the extension's figures of record", and "candidates" is A-n1 §2's word for the four conventions. Put instead: "§4.1's figures of record would be:".
32. L38–40, k = 10 of n = 24; 0.0625 nats; median rel 0.0132. CONFIRMED: exceed_tau 10 and reads 24; absdiff.max 0.06250021525822458; rel.median 0.013228265542717183.
33. L46 and L48–54, "lines 61–65, verbatim". CONFIRMED: a `diff` of T1 L49–53 against v4out L61–65 is empty.
34. L56, "The output carries no margin and no pick." CONFIRMED: v4out L54–74; v4out L62's own "no margin".
35. L56–57, the values behind the counts and medians are written to no file. CONFIRMED: drv L72 ("nothing of it is written") and L704; A-n1 L32.
36. L57, the quote "per candidate its match count of 40 and nothing else". CONFIRMED: A-n1 L32.
37. L57–58, "the seat's answers of 2026-11-18, §5.5, added the median". IMPRECISE (citation): this §5.5 is corpus-ans L69. ans3's §5 ends at 5.3, and every other "the seat's answers of 2026-11-18" in T1 is the third sitting. drv L41–42 names it "the corpus answers of 2026-11-18, §5.5". Put instead: "and the seat's corpus answers of 2026-11-18 (`results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md`), §5.5, added the median beside it."
38. L63–64, the run copy at ad856f0, with its report and cell at 6df2131's bytes. CONFIRMED: v4out L2–3.
39. L64–65, the fresh copy at 1272702, clean, with neither stage's root or report. CONFIRMED: v4out L4–5; v4.sh L86–94.
40. L65, the ruling beside the script at its committed sha256 and byte count. CONFIRMED: v4out L6; `wc -c` on the committed raw gives 2515.
41. L66–67, the copy-in quote. CONFIRMED: substring of v4out L8.
42. L67, the names came from the committed record, with no listing. CONFIRMED: v4.sh L9–13 and L70–73; v4out L7.
43. L68, the manifest 23 of 23. CONFIRMED: v4out L10–32, 23 OK lines.
44. L68, the quote "389/389 n selftest checks pass". CONFIRMED: v4out L36.
45. L68–69, the hashes equal the laptop's. CONFIRMED: v4out L52. Independently, hashes.txt is 93783db0…7b36, the laptop file's digest per v4rec L22.
46. L71, the STAGE line, the weights, then "DRIVER … HEAD's committed bytes". CONFIRMED: v4out L54–56.
47. L72, "G-VER PASS; R6's bridge; the load." IMPRECISE (order): v4out has L58 (PASS), then L59 (the load, 707/707), then L60 (the backend line with R6's bridge and "load 12150 ms"). Put instead: "G-VER PASS; the load (707/707); the backend line, R6's bridge, with the load at 12,150 ms."
48. L73, no read line, then "end COMPLETE: 24/24 reads". CONFIRMED: v4out L67 and L61.
49. L74, "The prints above." CONFIRMED: v4out L62–65; L68 shows each print 1.
50. L75–76, the report-line quote. CONFIRMED: v4out L69.
51. L76–77, the identity lines equal the hashes step's, and the sha256 after the resume is dd217d78…ce79. CONFIRMED: v4out L70–71. cmp shows hashes.txt equals resume-identity.txt.
52. L78, the cell file and its 31 arrays are unchanged, and the run copy's two files are still the committed bytes. CONFIRMED: v4out L72–73.
53. L79, the summary quote and exit 0. CONFIRMED: v4out L74; exit file 0.
54. L83, "The box script v2 ran first". CONFIRMED: v2rec; (c4).
55. L83, "the coordinating session's hold on it crossed with its launch". NOT CHECKABLE: (c4) says only that v2 "had already gone to the pod session", then a HOLD, then v3. v2rec L6 says the launch was announced before it started. Suggested wording: "The box script v2 ran first. It had already gone to the pod session when the coordinating session sent a hold on it, and then v3, which never ran (the coordinating session's words; the pod session's record)."
56. L83, "Step 0 held." CONFIRMED: v2out L1–6; v2rec L11.
57. L83–86, the first `cp -p` (the report into the fresh copy) was refused, with both quotes and exit 1. CONFIRMED: v2.sh L100–102; v2out L8–9 (path elided); exit file 1.
58. L87, nothing after it ran. CONFIRMED: v2.sh exits at L102; v2rec L11–12.
59. L88, the probe. CONFIRMED: (c2); v4rec §3.
60. L89, "The fix was v4's plain `cp`, with the sha256 check after it unchanged." FAIL: v2 compared each copy with `cmp -s` (v2.sh L103) and had no sha256 check. The sha256 mismatch count is v3's (v3.sh L110–112), kept in v4 (v4.sh L112–114); v4rec L17–20 confirms. Put instead: "The fix was v4's plain `cp`. The check after the copy is v3's sha256 mismatch count, unchanged; v2 compared each copy by `cmp -s`, and v3, relayed after the hold, kept `cp -p` and never ran."
61. L90, the failed run's copy and work folder stay on the box, unread. CONFIRMED: v2rec §6 and §8; v4rec §8.
62. L91, a launch-script defect of Code's, declared in the entry, and no gate of the stage. CONFIRMED: T2 L39–47.
63. L95, the bare forms sit about 9.7 nats from BK's at the median (9.73594 and 9.73506). CONFIRMED: v4out L64.
64. L96–97, the §1.3 quote. CONFIRMED: ans3 L18. The minus sign is U+2212 in both.
65. L98, "sit 0.038 nats … (0.0382264 and 0.0388117)". IMPRECISE: 0.0388117 rounds to 0.039. Put instead: "sit 0.038 and 0.039 nats from BK's at the median (0.0382264 and 0.0388117)".
66. L98–99, below R3's bound as run (0.0492). CONFIRMED: label.max is 0.04924420372226734.
67. L99–100, 24 of the 40 sessions fall outside on at least one label. CONFIRMED: drv L711–719 (a session counts only if both labels match); 40 − 16 = 24, under each space form.
68. L100, 16 of 40 each, medians within 0.0006. CONFIRMED: the difference is 0.0005853.
69. L101, absdiff median 0.0312498, q3 0.0312503, max 0.0625002. CONFIRMED: v4out L62.
70. L101–102, "2^-5, 2^-5 and 2^-4 to within 3e-7". FAIL (marginal): q3 − 2^-5 = 0.03125030038608245 − 0.03125 = 3.004e-7, which is above 3e-7. The median (1.62e-7) and max (2.15e-7) are within. Put instead: "to within 3.1e-7 (q3's 3.004e-7 the largest)".
71. L102–103, consistent with the seat's §1.2 reading (bf16 rounding on either path). CONFIRMED: ans3 L16.
72. L104–105, rel max 0.0860698 is read 1's 0.086070, and TAU exceedances are 10, as at 6df2131. CONFIRMED: v4out L62; STOP-6df L62 and L92.
73. L104, "The resume reproduces the run of record". IMPRECISE: the resume is skip-only, and its distribution is computed from the same 24 records (drv L994–1003: load_cell, then discordance), so the agreement is by construction. Its own fresh forwards are the in-band check (drv L1010–1012, 6 of 6). Put instead: "**The distribution is the run of record's:** skip-only, it is computed from the same 24 records, so rel's max 0.0860698 is read 1's 0.086070 and the exceedances of TAU are 10 (TAU/4: 15), as at `6df2131`. The resume's own forwards agree with those records: the in-band count is 6 of 6."
74. L107, p0 = (k+1)/(n+2) = 11/26 (§1.1). CONFIRMED: A-n2 L18.
75. L108, C = max(0.25, 2×0.0625) = 0.25 (§2.1). CONFIRMED: A-n2 L24; 2 × 0.0625002 = 0.1250004.
76. L109, the median rel 0.0132 (§3). CONFIRMED: A-n2 L30 and §4.2. See observation 12 on the wording.
77. L111, these stand if the seat names "bare" (§4.1). CONFIRMED: A-n2 L34.
78. L112–113, no count is derivable from the record; values are printed only as counts and medians, and none is written. CONFIRMED: drv L699–721 and L1013–1015.
79. L113–114, "A count under another bound needs the comparison run again on the box: one load and the vanilla forwards". IMPRECISE: v2f's comparison takes R3's bound alone (drv L1013: `float(disc["label"]["max"])`), and main() has no bound option (L1710–1751). Put instead: "A count under another bound needs a driver that takes that bound (v2f's comparison takes R3's bound alone, `label.max`) and the comparison run again on the box: one load and the vanilla forwards, as at this resume."
80. L118–119, the A-n1 §2 quote. CONFIRMED: A-n1 L32 (bold markup only).
81. L119, "The seat's answers of 2026-11-18, §5.5, add the four medians." IMPRECISE (citation, as item 37): corpus-ans L69 ("otherwise the seat rules on the four counts and the four medians"). Put instead: "The seat's corpus answers of 2026-11-18, §5.5, add the four medians."
82. L119–120, none is at 40 of 40. CONFIRMED: v4out L65.
83. L122, the four candidate names. CONFIRMED: valence_core/n/ids.py L84–85.
84. L127–128, the §4.1 quote with its elision. CONFIRMED: A-n2 L34.
85. L129, "The check named none." CONFIRMED.
86. L133–134, backend-ext-2 --convention NAME for space, bare+eot or space+eot, with its own root and report, the fidelity rule as the first run carried it, and R7. CONFIRMED: drv L103–114, L429–431, L579–588 (stage "backend-ext", p0 0/2400, identity_bound None), L894–899, L1740–1742.
87. L134–135, launch files go through the coordinating session. CONFIRMED: RESULTS.md L97–99.
88. L139, the tolerance quote. CONFIRMED: A-n1 L32.
89. L139–140, §2.2 makes the identity bound C, which is 0.25 under bare. CONFIRMED: A-n2 L26.
90. L140–141, R3's bound is the largest per-label |cached − fresh| over 24 reads, 0.0492. CONFIRMED: drv L81–83, L620–624, L1013.
91. L141–143, the §1.4 quote. CONFIRMED: ans3 L20. The em-dashes are U+2014 in both.
92. L145–146, 7a54eb9's entry gives the coordinating session's reading, with the quote. CONFIRMED: RESULTS.md L196–198 (blame 7a54eb9). That entry's "Code" is the coordinating session (L224–225).
93. L147, C's 0.25 floor does not depend on the convention. CONFIRMED: A-n2 L14 and L24.
94. L150–151, Code cannot say from the record. CONFIRMED: follows item 78.
95. L155, the resume's pass (§2). CONFIRMED.
96. L156, the first attempt's failure is declared in the entry. CONFIRMED: T2 L39.
97. L157, "The cell's and the resumed report's commit, with this block." FAIL: this contradicts T1 L170 ("The cell is not committed again") and T2 L62–63. Put instead: "The resumed report's commit, with this block; the cell, unchanged, is not committed again (§9)."
98. L158, the schema follow-up and LOCK-n v0.1 wait. CONFIRMED: RESULTS.md L100–103; A-n2 §6.3.
99. L159, the box is idle and nothing runs on it. CONFIRMED: v4rec §6; (c3).
100. L166, report dd217d78…ce79, which the admit of 6df2131 covers. CONFIRMED: .gitignore L292–294, added at 6df2131 (`git show 6df2131 -- .gitignore`).
101. L170, the cell is not committed again, and the arrays stay on the box. CONFIRMED: v4out L72.

T2:
102. L1–4, the header (e2b1c77a…2a8a, third sitting §1.4, COMPLETE, list printed, none at 40, the STOP path). CONFIRMED.
103. L5–6, p01 was the end-of-run fire at 6df2131: 10 of 24 above TAU, under p0 = 0 of 2,400. CONFIRMED: STOP-6df L31–32.
104. L6–8, cleared as the measurement; the link, the full sha256 and 3b2b855. CONFIRMED: ruling L1 and L7; git blob.
105. L8–9, the report records p01 adjudicated under that sha256. CONFIRMED: v4out L69.
106. L10–11, the pod, the H100 SXM of d5d08fa, run by the pod session on the coordinating session's relay. CONFIRMED: v4rec L1–4.
107. L12, v4 4fec8670…dd78, from 1272702. CONFIRMED.
108. L13–14, the fresh sparse copy, taken by name from the committed record, checked by sha256 with 0 mismatches. CONFIRMED: v4.sh L9–13, L101–117; v4out L8.
109. L15, the command. CONFIRMED.
110. L17–18, the manifest 23/23, self-test 389/389, hashes equal, G-VER PASS, R6's bridge, no read re-launched. CONFIRMED: v4out.
111. L18–19, COMPLETE, cell and arrays unchanged, the run copy only read, dd217d78…ce79. CONFIRMED.
112. L20, lines 61–65 are in the block's §1. CONFIRMED.
113. L22, the absdiff figures 6.65e-08, 3.60e-07, 0.03125, 0.03125, 0.0531, 0.0625. CONFIRMED: v4out L62.
114. L23, the rel figures 2.20e-08, 3.34e-07, 0.0132, 0.0295, 0.0861. CONFIRMED.
115. L24, the label median 0.00776 and max 0.0492 (R3's bound). CONFIRMED.
116. L25, 10 above TAU, 15 above TAU/4, of 24 reads, all finite. CONFIRMED.
117. L26, in-band 6 of 6. CONFIRMED.
118. L27–28, the four counts and medians. CONFIRMED: v4out L64.
119. L28–29, the convention-line quote. CONFIRMED: v4out L65.
120. L30–31, by A-n1 §2's words the four counts go to the seat. CONFIRMED.
121. L31, "(§5.5)". IMPRECISE: the header cites the third sitting, which has no §5.5; it is corpus-ans L69. Put instead: "(the seat's corpus answers of 2026-11-18, §5.5)".
122. L32–33, Q1–Q3. CONFIRMED: they match T1 §5–§7.
123. L34, backend-ext-2 does not run, and nothing more runs. CONFIRMED: (c3).
124. L35–36, k = 10 of 24, 0.0625, 0.0132, p0 = 11/26 and C = 0.25. CONFIRMED.
125. L37, the follow-up and LOCK-n wait. CONFIRMED.
126. L39–40, v2 f166e7ce…19f2 failed at its copy-in; "Operation not permitted". CONFIRMED.
127. L41, nothing of the stage ran and no model loaded. CONFIRMED: v2rec L11–12.
128. L42–43, fixed in v4 by a plain cp; the probe confirmed it. CONFIRMED: v4.sh L109; (c2).
129. L44–45, the stand-in harness, its stand-in `cp`, and "fails under it". NOT CHECKABLE: no source.
130. L45, v3 also used `cp -p`. CONFIRMED: v3.sh L107.
131. L46–47, the failed copy and work folder stay on the box, unread. CONFIRMED: v2rec §8; v4rec §8.
132. L49–50, the gate's first run failed on a byte-count cut, then a prefix match, then the second run passed. NOT CHECKABLE.
133. L51, `grep -P`, "that BSD grep lacks". CONFIRMED: `/usr/bin/grep -P` gives "invalid option -- P" (BSD grep 2.6.0-FreeBSD).
134. L51–52, it errored, was chained with ";", and the commit ran without it. NOT CHECKABLE.
135. L52, 0 non-ASCII bytes after the commit. CONFIRMED: a count over 1272702's message gives 0.
136. L54, "From here, every pre-commit check asserts…". NOT CHECKABLE: it is a commitment.
137. L55, the guard marker is declared in v2f's entry (1272702). CONFIRMED: RESULTS.md L105–108 (blame 1272702).
138. L59–64, the commit list; 6df2131's admit covers the report; the cell is unchanged and not committed again. CONFIRMED: .gitignore L294 at 6df2131; v4out L72.
139. L66, "(the answers' §5.2)". CONFIRMED: ans3 L38.
140. L66, "is 0. Not pushed." NOT CHECKABLE: the commit has not happened yet.

TOTALS: 140 items. 121 CONFIRMED, 8 IMPRECISE, 3 FAIL, 8 NOT CHECKABLE.
- IMPRECISE: items 31, 37, 47, 65, 73, 79, 81, 121.
- FAIL: items 60, 70, 97.
- NOT CHECKABLE: items 18, 23, 55, 129, 132, 134, 136, 140.

OBSERVATIONS
1. The resumed report is not on the laptop yet. v4rec §7 says "it goes later, by hash only, through the coordinating session". T1 L19 lists it as read, and T1 §9 and T2 L62 commit it. Before the commit, check it against dd217d78…ce79 on arrival and read only what L19 states. Until then, cite v4out L69–71 instead.
2. v2f cannot run the comparison under any bound but R3's (item 79). Q3's "run again under it" therefore implies a driver change and its commit first. A neutral line in §7 would give the seat that cost.
3. corpus-ans §5.5 also gives the medians' purpose: "the medians separate a convention that is wrong by nats from one that is right to within hardware". It bears on Q1. If used, quote it; do not apply it.
4. The sources list is incomplete:
   - T1 cites ans3 §1.2 (L102), A-n2 §3 (L109), corpus-ans §5.5, RESULTS.md at 7a54eb9 and f3e7190 (L7–8, L145), STOP-6df's read lines (L104), the driver (§4 item 6, §6) and the box scripts (§3). None is under "Sources read".
   - ADDENDUM-n1 is listed without its sha256 (e979f8f2…5e03), under a heading that says "by sha256".
   - The first attempt's output is not named (bext_resume_v2_out.txt).
5. v3 does not appear in T1. The sequence was v2, then the hold, then v3 (relayed, never run per v4rec L6 and (c4)), then v4. T2 names v3 only inside a departure and never mentions the hold.
6. The copy check's form changed from the committed texts without saying so. The 1272702 entry (RESULTS.md L90–94) and f3e7190's close line (L472–475, "by n-build's `bext_resume_v2` … `cmp`") say `cmp`. v3 and v4 check by sha256 counts. Both forms are within the coordinating session's line (L534–535); one sentence would record the change.
7. The box's 389/389 is the count the committed self-test raw predicted (results/raw/2026-11-18_n-step4-driver-v2f_selftest.txt L32–35: 378 + 11). One clause would answer a reader comparing it with the laptop's 378.
8. Not stated, though STOP-6df L89–90 gave its equivalents: n's identifier 8264f719efd347a9 (window 4096) and the load of 12,150 ms. The two transformers warnings in the self-test step (v4out L34–35, noted in v4rec L67–68) are also unmentioned.
9. A measured fact for the seat, to declare without adjudicating. The margin discordance's max is now printed in nats: absdiff 0.0625002. The seat's texts say "at most about 0.09" nats (ans3 §1.3; ruling item 3; A-n2 §0.2 and §5), which is the sum of the per-label maxima. A-n2 §2.1's "about three times this box's under bare" is four times on the measured figure.
10. Neutrality:
    - (a) T1 L35 "There is no backend-ext-2" reads as a ruling on Q2. T2's form, "does not run (now)", keeps Q2 open.
    - (b) §4 item 1's "That fits the seat's §1.3" states Code's reading as fact. Item 3's form, "Code reads that as…", would fit.
    - (c) Q1's "read with §4's items 1–2" points the seat to Code's readings.
11. In §4 item 2, "24 of the 40 sessions" holds under each space form separately. Say "under each space form".
12. Item 76: A-n2 §4.2 calls the figure "the extension median rel". "The second sensitivity row's median rel" can be misread as the median of that row.
13. Naming: §3 and T2 say "launch-script defect", while T1 §8 says "launch-tooling departure". Pick one.
14. The volume refuses cp -p's permission-preserving step. The probe's cp -p exits 1 but still creates its destination (v4rec L35–36). The failed copy may therefore hold a copy of the report (v2rec L70–71). That matters for any later cleanup, which is the PI's call.
15. Style breaks against 6df2131:
    - (a) T1 §1 ("The reads the seat needs") gives output lines, not the files to read in full, the report as the read domain, and "Not for reading: the cell".
    - (b) T1 §9 gives no committed raw paths, hashes or line counts.
    - (c) The short form has no "**Code adjudicates nothing.**".
    - (d) T2's header uses a backticked path where 6df2131 has "Block: [link]".
    - (e) T2 has no "**Model:**" bullet. That would be one load on the box, the resume's; none at the first attempt; none on the laptop.
    - (f) T2 does not give the box's state at the end.
    - (g) T2 does not say what Code read of the report.
    - (h) The pod session's departures (none in its records) are not stated.
16. T2's two departures at 1272702's commit are not in that entry, and that commit's message says "Code's one departure". Say they are declared here for the first time, and name which gate.
17. The record lists do not cover the two exit files or the three copied-back work files. Say whether they are committed. They also serve as an independent check: hashes.txt equals resume-identity.txt (93783db0…7b36), and resume.txt equals v4out L54–65.

DEPARTURES: none that the brief's rules bar. Disclosed for completeness, none of them touching data/, S beyond the named files, or any guard marker:
- `git log -1 --format=%B 1272702` (with the pathspec), piped to a count of non-ASCII bytes. That is a commit body, beyond item 1's ids, subjects and times.
- A name-only `ls results/raw` piped to grep, to find corpus-ans.
- Reads beyond the named sources: corpus-ans, the v2f self-test raw, valence_core/n/ids.py (grep), .gitignore (grep and `git show 6df2131 -- .gitignore`), `git diff --name-status 6df2131^ 6df2131 -- .gitignore .gitattributes`, and `git blame` on RESULTS.md.
- `wc -c` on the committed ruling raw.
- `/usr/bin/grep -P a /dev/null`, an option test.
- `sed`, `diff` and `cmp` (no grep) on named S files.
```
