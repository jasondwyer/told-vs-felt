# The fourth sitting's texts of the coordinating session: the blind values-check (PI date 2026-11-18)

Code's raw (the coordinating session). One fresh blind checker, a subagent of the coordinating session, checked three
texts this commit adds:
- D1, the close line on `cf318c5`'s note;
- D2, the dated note on `7a54eb9`'s entry;
- D3, the raw on the amended screen classifier and its test (`2026-11-18_screen-amended_test.md`).

Its brief:
- quoted the list of record v2's items 1–5 with C.2's amendment;
- carried the briefs' two lines, the `data/mf3` exclusion and no listing of `results/raw`;
- barred every gitleaks JSON report in the scratch;
- allowed no interpreter.

The report is reproduced whole, as its hand-back message gave it, with the harness's two-space indent removed. It is
byte-identical to the unindented copy of the report that the session's record also holds, and it holds no local path.
Its line numbers index the drafts it read. The committed texts are the drafts after the dispositions below.

## 1. The report, whole

VALUES-CHECK: the fourth sitting's close line on cf318c5, dated note on 7a54eb9, and the screen-test raw
78 items: 66 CONFIRMED, 7 IMPRECISE, 0 FAIL, 5 NOT CHECKABLE; 12 observations.

**Header**
- **What I read.** In the scratch: `close_cf318c5.md` (D1), `dated_7a54eb9.md` (D2), `screen_test_raw.md` (D3), `RESULTS.new` (:1–130 and :411–562, and the whole file by diff), `gl5_test_out.txt`, `pi-routing-saved.txt`, `../push4/gl5.py` and `../push4/gl4.py` (as text) and `../push10/push_record10.txt`. In the repo:
  - the fourth sitting's answers, whole;
  - the third sitting's answers :1–20;
  - the p01 ruling raw, whole;
  - ADDENDUM-n2, whole;
  - the resume STOP block :36–149;
  - the 2026-11-16 answers' §C (:43–50);
  - the referent-check raw's claim 16 (:168–174) and its §2 (:450–489);
  - WORKFLOW.md §5;
  - RESULTS.md at HEAD, through `git show HEAD:RESULTS.md`;
  - git history.
- **Abbreviations.** A4 = the fourth sitting's answers; A3 = the third sitting's answers; RUL = the p01 ruling; AN2 = ADDENDUM-n2; STOP = 6e3474d's block; C16 = the 2026-11-16 answers; REF = the referent-check raw; RN = RESULTS.new; PI = pi-routing-saved.txt; P10 = push_record10.txt; OUT = gl5_test_out.txt.
- **Line numbers.** D1:n is RN:(n+85), D2:n is RN:(n+543), and D3:n is the raw's own line n.
- **Tools.**
  - The Read tool, plus `diff`, `head`/`tail`, `wc` and `shasum | cut`.
  - `/usr/bin/grep` on named files only.
  - Git: `git show <rev>:<path>`; `git show --name-status`, `git log --format` (ids and dates) and `git rev-list --count`, each under item 3's pathspec plus `':!data/mf3/**'`; `git grep -l` under the same pathspec.
  - Tracked status by `git rev-parse HEAD:<path>` against `git hash-object`; `test -e` on one named path.
- **What I did not do.**
  - No interpreter ran, and I did not run gl4.py, gl5.py or gitleaks.
  - Nothing under `data/` was opened, and no `*.json` in the scratch was opened.
  - No listing of results/raw or of a scratch folder, and no git status.
  - No `--stat` or `--numstat`, no write of any kind and no network.
- **State.** HEAD was c7d0009 throughout. RESULTS.md and the addendum are each clean against it.

**D1: the close line on cf318c5's note**

1. **Placement (RN:86–123 = D1, after the note's last line).** CONFIRMED.
   - `diff` of RN:86–123 against D1 exits 0.
   - RN:85 is the note's last line, "Committed by path: this note and its values-check raw … Not pushed."
2. **D1:1, "Close (PI date 2026-11-18, fourth sitting)".** CONFIRMED. PI:1: "PI date 2026-11-18 (fourth sitting)".
3. **D1:2–4, the answers raw, "sha256 `c265797f…61a5`".** CONFIRMED.
   - `git show c7d0009:<path> | shasum` gives c265797f…61a5, by cut.
   - The file is 20,924 bytes, and it is tracked and clean.
   - PI:5 gives the same hash.
4. **D1:4, "committed at `c7d0009`".** CONFIRMED. `git show --name-status c7d0009` shows A for this raw and for the conditional ruling, and `--diff-filter=A` names c7d0009.
5. **D1:4, "rule on this note in their §6".** CONFIRMED. A4:45: "## 6. The push note (`cf318c5`): C.3 and the halt".
6. **D1:4–5, "The PI routed that ruling as item 6 ("route as given")".** CONFIRMED. PI:17 is item 6, and PI:21 reads "PI: route as given".
7. **D1:7, the quoted item 6.** CONFIRMED. It is byte-identical to PI:17 (`diff` of PI:17 against D1:7 less its "    > " prefix). It is the PI's text, not A4:79's (see observation 7).
8. **D1:9, "C.3 read by nesting, and the digest class adopted (§6.1)".** CONFIRMED. A4:47: "C.3 is read by nesting … The digest class is adopted".
9. **D1:9–10, "The screen's gitleaks classifier is amended to both."** CONFIRMED. gl5.py:1–3 (the docstring) and :95–113 (the code).
10. **D1:10–11, the three clearances** (the key just before it carries "sha"; any key on its JSON path does; it equals the sha256 of the tracked file its key names at the commit screened). CONFIRMED.
    - gl5.py :95–97 is the immediate test, :99–106 the nesting test, and :73–81 with :109–112 the file test.
    - For "the commit screened", see observation 4.
11. **D1:11–12, "Each is counted by class."** CONFIRMED.
    - gl5.py:114–116; A4:47 says "Both are reported as counts by class".
    - The count's label joins the clearances that held (observation 3).
12. **D1:13, "on six cases".** CONFIRMED. OUT:1–2: "(6 findings)", "gitleaks findings: 6".
13. **D1:13, "in a scratch repository … with real gitleaks output".** NOT CHECKABLE.
    - The repository was thrown away (D3:25), and the synthetic report is barred.
    - The outputs fit: gl5 read gitleaks' report fields, with the rule, commits and StartLine.
14. **D1:13–14, the `imported_sha256` digest "cleared by nesting and by file".** CONFIRMED. OUT:10 (inside 2) gives no/yes/yes → digest, and OUT:6 gives 'digest:nesting+file'. This is D3:28–29's mapping.
15. **D1:14–15, a value under a sha-named key, "by immediate key and by nesting".** CONFIRMED. OUT:12 (inside 4) gives yes/yes/no, and OUT:5 gives 'digest:immediate+nesting'.
16. **D1:15, a file digest in a map with no "sha" in its name, "by file".** CONFIRMED. OUT:13 (inside 5) gives no/no/yes, and OUT:4 gives 'digest:file'.
17. **D1:15–16, a random value in the reports folder and one on a text line in the ckpt folder "halted".** CONFIRMED. OUT:11 (inside 3) and OUT:9 (inside 1) each end "-> HALT"; OUT:15–16.
18. **D1:16, "a match outside was listed to read".** CONFIRMED. OUT:14: "READ scripts/conf.txt@010cb68:1 … hex64-other shape 64:hex-lower".
19. **D1:16–17, "The previous classifier cleared only the immediate case."** CONFIRMED (see item 77).
20. **D1:18–19, push #9's and push #10's reports: both digests "by nesting and by file, with no halt".** CONFIRMED.
    - OUT:28–38: 'digest:nesting+file' x 1 at 6df2131 and again at 6e3474d; "gl5 exit=0" twice, with no HALT line.
    - The ranges agree with RH:26 and P10:24.
21. **D1:20, the raw link `results/raw/2026-11-18_screen-amended_test.md`.** CONFIRMED.
    - This is D3's target path, per the brief.
    - It is absent at HEAD (`git rev-parse --verify` exits 1) and absent in the working tree, so there is no collision.
22. **D1:21–22, the re-run.** CONFIRMED. It is verbatim A4:47: "the helper's examination serves as the re-run C.1 asks to see beside this halt, and the second run over the whole range was the push's own screen".
23. **D1:23–25, the helper's prints as the screen's form.** CONFIRMED.
    - A4:49: "the rule's name, the path class, the commit, two yes/no classes; never a value, a key or a line … are inert as a departure and are adopted … C.2 is amended to include them".
    - gl5.py:117–121 prints these; on the count of the yes/no classes, see observation 2.
24. **D1:26–27, the copy-back count.** CONFIRMED. A4:51: "the address-and-port count over copied files before their commit, counts only … is inert and allowed … never a line".
25. **D1:28–30, the tooling reading.** CONFIRMED. This is A4:53, verbatim in substance.
26. **D1:31, "The departures of the answers' §7 are inert."** CONFIRMED. A4:57: "Inert; the standing lines stand."
27. **D1:31–33, "They add one standing line: "a bundle … where the entry says"".** IMPRECISE.
    - The quote is verbatim from A4:57.
    - But the departures do not add the line. The seat's §7 does: "One line is added to the list of record v2's reading, for the pod session's transport: …".
    - **Fix:** "The departures of the answers' §7 are inert, and §7 adds one line to the list of record v2's reading, for the pod session's transport: "…"."
28. **D1:33, "The §8 dated notes are on `7a54eb9`'s entry, in this commit."** CONFIRMED.
    - RN:411 is the head of "ADDENDUM-n2 v0.1 — COMMITTED", and RN:533–534 reads "committed it by path at `7a54eb9`".
    - `git show --name-status 7a54eb9` shows A for the addendum and the referent-check raw, and M for RESULTS.md.
    - D2 sits at RN:544–559. For placement, see observation 8.
29. **D1:34, "(gitleaks 8.30.1, default rules): `1272702..cf318c5`, 3 commits".** CONFIRMED.
    - `git log` under the pathspec gives cf318c5, 303953c and 6e3474d, and `rev-list --count` gives 3.
    - P10:12 and P10:24 agree.
30. **D1:34–35, on the PI's word "Push, with a note" (2026-11-18).** CONFIRMED. P10:1 has the word, verbatim; P10:25 reads "pushed 2026-11-18".
31. **D1:35, "The screen's classes were CLEAR, with nothing inside `ckpt` or `reports`."** IMPRECISE.
    - P10:4–9 print "inside: 0 -> CLEAR" for each class, so no match inside.
    - The range did carry a reports file: 6e3474d's resumed report (P10:22), which gitleaks matched in the next sentence.
    - **Fix:** "with no match inside `ckpt` or `reports`". cf318c5's note has "with nothing matched inside" (RN:34).
32. **D1:36, one `generic-api-key` match inside `data/n/reports`, "`6e3474d`'s resumed report's module digest".** CONFIRMED.
    - P10:13–14 give one finding, ('data/n/reports', 'generic-api-key', 'hex64-other').
    - P10:19 gives the helper's yes/yes.
    - P10:22 reads "a 64-hex value … at 6e3474d (the resumed report) … a module digest in imported_sha256". "Module" is the note's inference (RN:50–56).
33. **D1:37, "a halt under C.3 as it then stood, pushed with a note".** CONFIRMED.
    - P10:15 reads "HALT … (C.3)", and P10:22 "HALT disposition: on the PI's "Push, with a note" … C.3 halts it".
    - C.3 itself is at C16:47.
34. **D1:37–38, "Under the amended classifier it is a digest by nesting and by file."** CONFIRMED. OUT:34–38.

**D2: the dated note on 7a54eb9's entry**

35. **Placement (RN:544–559 = D2, after the entry's last close line).** CONFIRMED.
    - `diff` exits 0.
    - n-build's close line, RN:532–543, is the entry's last. RN:560 is blank, and RN:561 is the next entry.
36. **RN differs from HEAD's RESULTS.md by these two insertions alone.** CONFIRMED.
    - HEAD has 30,512 lines and RN has 30,566.
    - `diff` removes 0 lines and adds 54 (38 + 16).
    - Region checks: HEAD :1–85 = RN :1–85; HEAD :86–505 = RN :124–543; HEAD :506–end = RN :560–end. (On the three hunks `diff` prints, see observation 1.)
37. **D2:1–2, the header: two corrections to the third-sitting figures, and the FAIL regraded.** CONFIRMED.
    - A4:59–61 makes them.
    - PI:18: "(0.09 → 0.0625; "three times" → four; the referent FAIL regraded not substantive)".
38. **D2:2–4, the answers raw, its sha256 and c7d0009.** CONFIRMED (as items 3 and 4).
39. **D2:4, "make the corrections by dated note in their §8".** CONFIRMED. A4:61: "These are dated notes on committed texts (WORKFLOW §5)"; A4:11 agrees.
40. **D2:4–5, "The PI routed them as item 7 ("route as given")".** CONFIRMED. PI:18 and PI:21.
41. **D2:5, "The addendum is not edited (WORKFLOW §5)".** CONFIRMED.
    - WORKFLOW.md:43 reads "a dated note: a RESULTS.md entry, never an edit of … any committed file", and :44 reads "a correction is the next raw or a dated note". A4:61 says the same.
    - The addendum is clean at HEAD with sha256 41f76c49…bb3f, the hash RN:416 gives.
42. **D2:5–6, the answers' §8: "a later version carries both".** CONFIRMED. It is verbatim A4:61.
43. **D2:7, the third sitting's texts put it "at most about 0.09 nats".** IMPRECISE.
    - That wording is verbatim only at RUL:9 and AN2:40 (§5).
    - A3:18 (§1.3) and AN2:12 (§0.2) read "In nats the margin's discordance is at most about 0.09".
    - STOP:136 quoted it as "at most about 0.09" nats. A4:61 put "nats" inside the quotation marks, and D2 follows it.
    - **Fix:** "put it "at most about 0.09" nats".
44. **D2:7–8, the four places** (A3 §1.3; the ruling raw's item 3; AN2 §0.2 and §5). CONFIRMED. A3:18, RUL:9, AN2:12 and AN2:40 each hold the figure.
45. **D2:8–9, "an upper bound from the per-token maxima, 0.0375 + 0.0492".** CONFIRMED.
    - It is verbatim A4:61.
    - The maxima appear at A3:16, RUL:9 and AN2:12, and their sum is 0.0867.
46. **D2:9–10, "The printed maximum under "bare" is 0.0625 nats (`6e3474d`'s block, §4 item 5)".** CONFIRMED.
    - STOP:136: "The margin's largest discordance is now printed in nats: 0.0625." STOP:48 agrees.
    - The printed absdiff max at STOP:69 is 0.0625002…
47. **D2:11, AN2 §2.1's "about three times this box's under "bare"".** CONFIRMED. It is verbatim AN2:24.
48. **D2:11–12, "is four times on the printed figure".** CONFIRMED.
    - 0.25 / 0.0625 = 4.
    - A4:61 says "is four times", and STOP:138 "On the printed figure it is four times."
49. **D2:12, "C's formula is unchanged, and its floor binds at 0.25."** CONFIRMED.
    - A4:61 says "The formula is unchanged (C's floor binds at 0.25)".
    - STOP:141 gives C = max(0.25, 2 × 0.0625) = 0.25. (See observation 9.)
50. **D2:13, "this entry's claim 16, §5's heading citing "A-n1 §1.4's reservation"".** CONFIRMED.
    - REF:168–169 is claim 16, graded "FAIL (the citation only; not substantive)", and REF was added at 7a54eb9.
    - AN2:38 is the heading. RN:461–466 agrees.
51. **D2:13–15, "regraded by the seat as Code graded it" and the quote.** CONFIRMED.
    - It is verbatim A4:61.
    - Code's grading is at REF:455 ("graded not substantive") and REF:463 ("a citation error … The seat may regrade it").
52. **D2:16, "Ledger (83), on cross-hardware comparisons, is the seat's (the answers' §9)".** CONFIRMED. A4:63–65: "Ledger — design seat (83)", "drawn from the cross-hardware class".

**D3: the screen-test raw**

53. **D3:1, the title** (the classifier amended as the seat ruled, the answers' §6, PI date 2026-11-18). CONFIRMED. A4:45; PI:1.
54. **D3:3, "The screen lives in the coordinating session's scratch, not in the tree."** CONFIRMED for the classifier.
    - gl4.py and gl5.py were read from the scratch.
    - `git grep -l -F` for their definitions ('def json_paths', 'def file_digest', 'def line_of(commit, path, n)') over the tracked tree, under the pathspec, finds nothing (exit 1).
    - screen4.py (P10:2) is not a named file and was not opened.
55. **D3:3–4, "amended from `gl4.py` to `gl5.py`".** CONFIRMED.
    - P10:12 shows push #10 "classified by gl4.py".
    - gl5.py:1–3 reads "in the form the seat amended on 2026-11-18 (fourth sitting …)".
56. **D3:4, gl5.py's sha256.** CONFIRMED. It equals `shasum` of gl5.py, compared whole in the shell: 9d108e99…c325. (gl4.py is b9528e4f…dd48.)
57. **D3:5–6, per A4 §6.1–§6.2 and the PI's routing item 6.** CONFIRMED. A4:47 and A4:49; PI:17.
58. **D3:6–7, "Nothing here prints a matched value, a key, a path's content or a line."** IMPRECISE.
    - The outputs (D3:41–78) print none of these.
    - But §2 names the synthetic report's keys: `imported_sha256` (D3:28), `api_key` (D3:30) and `manifest` (D3:32).
    - **Fix:** "No output here prints a matched value, a key, a path's content or a line; the keys §2 names are the synthetic report's, which Code wrote."
59. **D3:11–12, the opening sentence: "a 64-character hexadecimal token is a digest when any of these holds, each reported as a yes/no class and counted by class".** IMPRECISE.
    - The 64-hex and any-of conditions are right (gl5.py:88 and :113).
    - But the yes/no classes print only for a finding inside (gl5.py:117–121).
    - Every finding is counted under one label that joins the clearances that held (gl5.py:114–116).
    - **Fix:** "… each counted by class (the label names the clearances that held, e.g. `digest:nesting+file`) and, for a finding inside, reported as a yes/no class".
60. **D3:13, immediate: "the key just before the value on its line carries "sha" (C.3's first form, as `gl4.py` had it)".** CONFIRMED.
    - gl5.py:95–97 against gl4.py:53–54: it is the same capture rule.
    - gl5 admits "/" in the key, and tests "sha" on the key's last path segment only. That is gl4's behaviour, since gl4 could not capture across a "/" (observation 5).
61. **D3:14–15, nesting.** CONFIRMED. gl5.py:61–70 and :99–106: json.loads of the whole blob; on every key path to a string leaf equal to the value (case-insensitively), "sha" in any key.
62. **D3:16–17, file** (the leaf's key, else the line's key; a tracked file at the commit screened; the sha256 of its blob equals the value). CONFIRMED.
    - gl5.py:107–112 does the keys; gl5.py:73–81 does `cat-file -e`, the type check for blob, and the sha256 of the blob.
    - For "the commit screened", see observation 4.
63. **D3:19, "Any other finding inside `data/*/ckpt` or `data/*/reports` is a halt for the seat."** CONFIRMED. gl5.py:36–38 (the path class), :122–124 and :135–137 ("HALT …", exit 2).
64. **D3:19–20, "For each finding inside, one line in the amended C.2 form (§6.2): the path class, the commit, the rule's name and the three yes/no classes."** IMPRECISE.
    - What §6.2 adopted was the helper's form, with "two yes/no classes" (A4:49). The helper's two were "key is a tracked repo path" and "secret equals that file's sha256" (P10:18–19).
    - gl5.py:119–121 prints three yes/no classes of different content (immediate, nesting, file), and ends the line with the verdict ("-> digest" or "-> HALT").
    - **Fix:** "For each finding inside, one line in the form §6.2 adopted, carried to the amended classes: the path class, the commit, the rule's name, three yes/no classes (immediate, nesting, file; the helper printed two) and the verdict; never a value, a key, a path's content or a line." (See observation 2.)
65. **D3:20–21, "Findings outside are listed to read as before."** IMPRECISE.
    - Only non-digest findings outside reach READ (gl5.py:122–126; docstring :13–14, "Any other finding outside them"). A digest outside is only counted, as in gl4.py:57–61.
    - **Fix:** "Non-digest findings outside are listed to read, as before."
66. **D3:25, "one commit (`010cb68`, thrown away)".** NOT CHECKABLE.
    - It fits: all six findings are at 010cb68 (OUT:9–14), and `git rev-parse --verify` finds no such commit in this repo.
67. **D3:25–27, the repository's contents** (two small tracked modules, a JSON report under `data/x/reports/`, a text file under `data/x/ckpt/` and a config file under `scripts/`). NOT CHECKABLE.
    - The path classes fit: four in reports, one in ckpt, and one outside at scripts/conf.txt.
    - Nesting "yes" needs a JSON parse.
    - There are two file digests (observation 12).
68. **D3:27, "each value a fresh random or computed 64-hex token".** NOT CHECKABLE.
    - The 64-hex part fits: every finding is classed hex64-other or digest:*, never "other", and that needs a 64-hex secret (gl5.py:88). The READ shape is 64:hex-lower.
    - Whether each value was random or computed cannot be seen from the outputs.
69. **D3:27, "gitleaks 8.30.1 (default rules)" for the synthetic run.** NOT CHECKABLE.
    - Neither gl5 nor the outputs print it.
    - It agrees with the laptop's gitleaks of record (RN:31–33; P10:12).
70. **D3:27, "found six matches".** CONFIRMED. OUT:2 and OUT:19.
71. **D3:28–29 → inside 2, digest by nesting and by file.** CONFIRMED. OUT:10 gives no/yes/yes, and OUT:6. This is what gl5's logic gives for a path key under `imported_sha256`.
72. **D3:30 → inside 3, halt.** CONFIRMED. OUT:11 gives no/no/no → HALT.
73. **D3:31 → inside 4, digest by immediate key and by nesting.** CONFIRMED. OUT:12 gives yes/yes/no, and OUT:5.
74. **D3:32 → inside 5, digest by file.** CONFIRMED. OUT:13 gives no/no/yes, and OUT:4.
75. **D3:33 → inside 1, halt.** CONFIRMED. OUT:9 gives data/x/ckpt, no/no/no → HALT.
76. **D3:34, read, outside.** CONFIRMED. OUT:14 and OUT:8.
77. **D3:36, "`gl4.py` on the same report cleared only the immediate case."** CONFIRMED.
    - OUT:20–23 show reports 'digest' x 1 and 'hex64-other' x 3.
    - gl4's test is gl5's immediate test in effect (item 60), and of the four reports findings only inside 4 is immediate "yes" (OUT:12).
78. **D3:38–79, §3 "verbatim".** CONFIRMED.
    - `diff` of D3:41–78 against OUT:1–38 exits 0; D3:40 and D3:79 fence it.
    - The lines match gl5.py's print formats and sort order (observation 10).
    - **§1 against the code:** faithful in substance; items 59, 64 and 65 are its imprecisions.
    - **§2 against the outputs:** all six cases fit.

**OBSERVATIONS**
1. `diff` prints three hunks (85a86,90 / 86a92,124 / 505a544,559) because D1's blank line, D1:6 = RN:91, aligns with HEAD's blank line :86. The region checks in item 36 show two contiguous insertions.
2. **For the seat (the form of the inside line).** gl5's line for a finding inside prints three yes/no classes where the form §6.2 adopted names two, and it adds the verdict.
   - gl5's file class merges the helper's two classes.
   - No value, key or line is printed, so C.2's bar holds, but the form is not §6.2's in words.
   - D1:23–25 is silent on the count; D3:19–20 is item 64.
   - The coordinating session may want to declare the change.
3. Counts are keyed by the combination of clearances, e.g. 'digest:nesting+file' (gl5.py:114–116), not one count per class. A per-class tally can be read off the labels.
4. "The commit screened" (D1:11, D3:16–17) is, in gl5, the finding's own commit, gitleaks' Commit field (gl5.py:86 and :110): the commit gitleaks attributes the line to, not the range's tip. That fits A4:47's words.
5. **Key reading, for the seat's awareness.**
   - The immediate test reads only a path key's last segment (gl5.py:97), but the nesting test reads whole key strings (gl5.py:105).
   - "sha" is a substring test, so keys such as "shape…", "shared…" or "shadow…" also carry it. Under nesting, every 64-hex leaf beneath such a key clears.
   - This is within C.3's words.
6. "push #10" appears only at D1:18 (RN:103). D1's C.5 bullet (D1:34) is that push, 1272702..cf318c5, but gives it no number. Either name the range at D1:18 or number the bullet.
7. **The fourth sitting's PI routing is not in the tree.**
   - It is the source of D1:7's quote and of D2:4–5's "item 7". It exists only in pi-routing-saved.txt: `git grep` finds "fourth sitting" in A4 and the conditional ruling only.
   - The third sitting's routing was committed as a raw at 7a54eb9 (RN:421–424).
   - Committing this one by path would give D1's quote a tracked source.
   - PI:17 differs from A4:79: "C.3 read by nesting" against "C.3 by nesting", and a backticked cf318c5. D1 quotes the PI's text.
8. **Placement of D2.**
   - 3b2b855, which committed A3 and RUL, touched no RESULTS.md. 7a54eb9's entry records it (RN:419–420).
   - The close lines on A3 sit on 6df2131's entry (RN:751 and RN:844).
   - D2 on 7a54eb9's entry fits D1:33. A pointer from 6df2131's entry is optional.
9. D2:12's "its floor binds at 0.25" holds on the printed "bare" figure. Under the convention of record ("space"), C comes from backend-ext-2, which has not yet run (A4 §1.3 and §2.4). The seat expects the same absdiffs (A4:21).
10. D3's outputs match gl5.py's print formats exactly, in the tuple repr, the sorted keys, the inside numbering and the READ form. That is consistent with gl5.py at 9d108e99…c325 having produced them. They were not re-run here, since no interpreter was used.
11. D1's "Item 7's other parts" names §7 and §8 but not ledger (83), which D2:16 carries.
12. If both file digests sit in the one JSON report (D3:26), inside 5's nesting "no" means its value differs from inside 2's (gl5 searches every path to the value). That is consistent with "two small tracked modules".

**DEPARTURES**
- **Kind:** two git commands that take no pathspec, run without item 3's pathspec plus `':!data/mf3/**'`. Both are offered for the seat to class.
  - `git rev-parse --short HEAD` printed one abbreviated commit id, c7d0009.
  - `git rev-parse --verify --quiet '010cb68^{commit}'` printed nothing (exit 1).
  - Neither read a tree, a path or anything under `data/`.
- **HEAD:** c7d0009.
- **Otherwise none.**

TOTALS: 78 items: 66 CONFIRMED, 7 IMPRECISE (27, 31, 43, 58, 59, 64, 65), 0 FAIL (none), 5 NOT CHECKABLE (13, 66, 67, 68, 69), and 12 observations.

## 2. Dispositions

**The seven IMPRECISE items, each applied in the checker's words or sense:**
- 27: §7 adds the bundle line, not the departures.
- 31: "with no match inside `ckpt` or `reports`".
- 43: "at most about 0.09" nats, the unit outside the quotation.
- 58: no output prints a value, key, path's content or line; the keys §2 names are the synthetic report's.
- 59: each finding is counted under a label naming the clearances that held, and for a finding inside each clearance
  is a yes/no class.
- 64: the inside line's form, with three yes/no classes and the verdict, where the helper printed two classes.
- 65: non-digest findings outside are listed to read.

**The observations:**
- applied:
  - 2: D1 declares the inside line's form for the seat;
  - 4: D3 says the commit screened is the finding's own;
  - 5: D3 notes that "sha" is a substring test;
  - 6: D1 numbers push #10;
  - 7: the fourth sitting's paste block is committed as a raw, `2026-11-18_fourth-sitting_pi-routing.md`, its fenced
    block byte-identical to the copy saved on receipt, and D1 links it;
  - 9: D2 says C's floor binds on the "bare" run's figure, and that under "space" C comes from backend-ext-2;
  - 11: D1 names ledger (83) with the dated notes.
- 1, 3, 8, 10 and 12 needed no text.

**The edits after the check** were checked by tool: each new text found once in its draft, each replaced text gone,
and the PI-routing raw's fenced block equal to the saved copy by `cmp`. The PI-routing raw and the additions from
observations 2, 4, 5, 6, 9 and 11 came after the check; the checker did not see them.

**The checker's departures**, as its report states them, for the seat to class: two `git rev-parse` calls that take
no pathspec, printing one short id and nothing.
