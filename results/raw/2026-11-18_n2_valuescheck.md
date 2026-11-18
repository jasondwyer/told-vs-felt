# n — N.2, the corpus of record committed: the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three drafts:
- the entry, sha256 `11acc38a…616f`;
- the close line on `fa96ccf`'s entry, `2b5dd23a…479a`, with the commit hash a placeholder;
- the `.gitignore` admit block, `f359d91d…b2ec`.

**The checker's brief:**
- named the sources: the corpus raw and the box raw, the PI's paste block of 2026-11-18 as the coordinating session
  saved it, the coordinating session's record-fix folder, the corpus files, the acceptance raw, RESULTS.md and
  `.gitignore`;
- quoted the list of record v2's items 1–5, verbatim;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3`, any write, and any printing of the
  as-checked record's line 72 or its value.

One of the brief's pointers was wrong: it sent the checker to the 2026-11-17 values-check raw for the block's per-part
figures, which that raw does not quote. The checker used the acceptance raw's §6 and §8 instead (its observation 1).

**The report** is in §3 below, extracted verbatim from the subagent's hand-back by `jq` (149 lines, sha256
`dec4bbb7…9493`). It writes `<repo>`, `<scratch>` and `<route18>` for the local roots. Its one `/Users/` is the bare
pattern of its own pickaxe search, with no user name after it.

**Totals:** 79 items — 73 CONFIRMED, 2 IMPRECISE, 0 FAIL, 4 NOT CHECKABLE — and 13 observations.

## 1. Dispositions

**The IMPRECISE items, both applied in the checker's words:**
- **8** (entry, the adoption's sections): "(§0–§1, committed at `26cf7d2`; this commit carries its §3 items 1, 2 and
  5)". The commit hash comes from observation 2.
- **11** (entry, which section N): "its section N for n-build, items 1–5, verbatim". The parenthetical of observation
  10 is added.

**The observations:**
1. **The block's figures.** Applied: the entry now cites the block "as the acceptance raw's §6 (G1) and §8 carry it".
2. **The coordinating session's commit.** Applied: the close line's hash is `26cf7d2`, and the entry cites it for the
   corpus raw. Code re-reads RESULTS.md at the splice: the gate rebuilds it from HEAD.
3. **The record-fix script's assertions.** Applied after Code read the script itself. It asserts, before replacing,
   the as-run extraction by its own split at the two fences; after replacing, it asserts the as-committed extraction
   and that the result compiles. The entry's script bullet now names all of these. The `awk` values are labelled as
   Code's re-check.
4. **G1's labels.** Applied: "As checked it was `323cf9d8…44b5`, 18,167 bytes, G1's". A sentence now says the
   committed record differs from G1's whole-file figures by the two lines.
5. **The fresh diff.** Applied. Code's regeneration used `diff -u` with the same two `--label`s and compared all 20
   lines with `cmp`, so the entry now says "under the same labels equal to the one above, line for line".
6. **The values-check raw.** Applied: this raw is committed with N.2 and listed in the entry.
7. **The model statement.** Applied: "Model-free: shell tools only; nothing ran on a model or in Python."
8. **"G-VEC builds the direction from them".** Applied to the `.gitignore` comment: "G-VEC builds the direction from
   the 544; the parts and the record are their provenance."
9. **The entry's Next.** Applied: it adds "(v), G-CAL-n's prompts, when that stage's prompts are fixed in its wiring".
10. **The paste block is not committed.** Applied: the entry's quote says it is the record of section N's items 1–5.
11. **The admit lines' effect.** Noted. This commit's gate runs `git check-ignore --no-index` on the staged paths after
    the admit lines.
12. **The CLOSE's restated rule.** Applied: the close line adds "G-DATA's venv is started only inside a battery
    window".
13. **A local path in an older entry, outside this commit.** Relayed to the coordinating session for the PI and the
    seat. Code confirmed it by count only, never displaying the line:
    - RESULTS.md's line 11646 holds the home-folder pattern four times;
    - the pickaxe, limited to RESULTS.md, names `de6dfc5` (2026-10-19), an ancestor of origin/main.

    This commit does not touch that entry.

**The NOT CHECKABLE items (4)** rest on Code's own runs and the commit still to come. No change.

## 2. The edits after the check, checked by tool

- A full `diff` of each final text against its checked draft holds only the dispositions above, and Code read each
  diff in full. The finals:
  - the entry, sha256 `9c39d120…63ba`, 78 lines;
  - the close line, `e8539a02…4fc6`, 12 lines;
  - the admit block, `0bce8511…0f5d`, 9 lines.
- The entry's diff block equals the coordinating session's `record.diff`, by `cmp`.
- The commit's gate rebuilds RESULTS.md and `.gitignore` from HEAD with these texts and compares both the working
  files and the staged blobs.

## 3. The report as returned

```text
VALUES-CHECK: N.2's ENTRY (<scratch>/entry_n2.md), CLOSE (<scratch>/close_fa96ccf.md) and GITIGNORE (<scratch>/gitignore_block.txt). Blind and read-only.

Tools: shasum, wc, /usr/bin/grep, awk, sed, cut, tr, fold, sort, cat, cmp, diff, a name-only ls (and `ls -A`), git log/show --name-only, git rev-parse and hash-object compared in the shell, git diff --name-only, git ls-files, git status on named paths, and the Read tool.

Beyond the brief's list (all read-only):
- one pickaxe, `git log -1 -S'/Users/' -- RESULTS.md`, limited by pathspec to RESULTS.md;
- `git rev-parse @{u}`;
- `git merge-base --is-ancestor`.

No interpreter ran. No argv carried a guard marker. Nothing under data/mf3, ckpt or reports was touched. No file was written.

The as-checked record's line 72 and <route18>/record.diff.raw were never displayed. Line 72 was reached only by digest, `grep -c`, line number and cmp/diff with the output discarded.

Abbreviations:
- corpus raw = <repo>/results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md
- paste = <route18>/paste_block_2026-11-18.txt
- acceptance raw = <repo>/results/raw/2026-11-17_n-corpus_acceptance.md
- record = <repo>/data/n/passages.prompt.md
- as-checked copy = <route18>/passages.prompt.as-checked.md

**Midway through this check the coordinating session committed 26cf7d2, and RESULTS.md moved.** Line numbers for RESULTS.md below are as of 26cf7d2.

ENTRY
1. ENTRY — "2026-11-18" — CONFIRMED — paste :1, "PI date 2026-11-18"; corpus raw :3.
2. ENTRY — "the passage corpus of record committed (N.2)" — CONFIRMED — corpus raw :7, "the corpus of record for G-VEC"; §3 :47, "N.2, in order"; paste item 4.
3. ENTRY — "the nine part files" — CONFIRMED — `ls data/n/passages.parts` gives nine names; `ls -A` gives 9 entries.
4. ENTRY — "data/n/passages.jsonl (ef6b00dc…3cc3)" — CONFIRMED — shasum.
5. ENTRY — "the prompt record as corrected, by path" — CONFIRMED — the record equals <route18>/passages.prompt.as-committed.md (cmp). Its two changed lines are the seat's (items 31, 40).
6. ENTRY — "`.gitignore`'s three admit lines" — CONFIRMED — GITIGNORE :6–8; paste item 4, "the three .gitignore admit lines".
7. ENTRY — "The adoption is the seat's answers of 2026-11-18, [link]" — CONFIRMED — the file exists: sha256 5843a9bd…7165, 16,470 B, equal to paste :5. Corpus raw §3 item 2 (:50) asks the entry to cite "this raw as the adoption".
8. ENTRY — "(§3 items 1, 2 and 5)", attached to the adoption — IMPRECISE — §3 (:47–53) is N.2's order: item 1 the record's edits, item 2 the commit, item 5 the close lines. The adoption itself is §0 (:7) and §1 (:14–22), so the parenthetical reads as locating the adoption.
9. ENTRY — "the check is `fa96ccf`'s raw, [link]" — CONFIRMED — `git log` on the acceptance raw gives fa96ccf only, and `git show --name-only fa96ccf` lists it. Its sha256 2fac6fd0…3c05 equals the final raw in the 2026-11-17 values-check raw :65.
10. ENTRY — "The PI's routing of 2026-11-18, 'Route as given'" — CONFIRMED — paste :1 and :31–32.
11. ENTRY — "its section N, verbatim" — IMPRECISE — the paste has two sections headed "N.": :9 n-build (items 1–5) and :16 n-analyzer (items 6–7). The quote is the first section only.
12. ENTRY — quoted item 1, "The corpus adopted on the every-tenth read; … no corpus edit [as ruled]." — CONFIRMED — entry :8 with "    > " removed against paste :10 with its leading space removed: diff empty.
13. ENTRY — quoted item 2, "G8's set is the brief's twelve; … ledger (80) [as ruled]." — CONFIRMED — entry :9 equals paste :11.
14. ENTRY — quoted item 3, "The record's two lines (§2.2), … ledger (81) [as ruled]." — CONFIRMED — entry :10 equals paste :12.
15. ENTRY — quoted item 4, "N.2: the nine parts, … G-VEC on the box ruling [go]." — CONFIRMED — entry :11 equals paste :13.
16. ENTRY — quoted item 5, "The four argv departures inert; … battery window [as ruled]." — CONFIRMED — entry :12 equals paste :14.
17. ENTRY — "The files, re-hashed before this commit (shell tools)" — NOT CHECKABLE — Code's own run. Every value it reports is reproduced below.
18. ENTRY — "the nine parts: each one's sha256, bytes and lines equal the block of 2026-11-17, G1's figures" — CONFIRMED — shasum, wc -c and wc -l of the nine, compared by diff (9 rows, identical) with:
    - the acceptance raw's §6 G1 rows :171–179, each "= the block";
    - its §8 BLOCK :433–441, headed :431 "The PI's block of 2026-11-17 as the coordinating session relayed it";
    - the record's §4 table :35–43 (also equal).
19. ENTRY — "sha256 ef6b00dc…3cc3" — CONFIRMED — shasum.
20. ENTRY — "157,520 bytes" — CONFIRMED — wc -c.
21. ENTRY — "544 lines" — CONFIRMED — wc -l.
22. ENTRY — "the corpus adopted" — CONFIRMED — corpus raw :7.
23. ENTRY — "data/n/passages.prompt.md, as committed: sha256 6d64eaae…8781" — CONFIRMED — shasum of the record and of the <route18> as-committed copy; cmp identical.
24. ENTRY — "18,591 bytes" — CONFIRMED — wc -c.
25. ENTRY — "As checked it was 323cf9d8…44b5" — CONFIRMED — shasum of the as-checked copy; acceptance raw :180 (G1, "= the block"); corpus raw :3; fix_record.py :12.
26. ENTRY — "18,167 bytes" — CONFIRMED — wc -c of the as-checked copy; acceptance raw :180.
27. ENTRY — "the seat's §2.2, applied by the coordinating session under §2.4, routed as item 3; the seat's ledger (81)" — CONFIRMED — corpus raw §2.2 :28–41, §2.4 :45 ("By the coordinating session"), (81) :76; paste item 3 (:12) and section header :9 ("the coordinating session for item 3"). The edit's files sit in <route18>, which the brief names as the coordinating session's folder.
28. ENTRY — "Its script asserted, before replacing: the file was the record as checked" — CONFIRMED — fix_record.py :12 asserts sha256 323cf9d8…44b5 and 18167 bytes before the replacement at :24. The as-checked copy satisfies it. The run's output is not among the sources.
29. ENTRY — "exactly one line began `ROOT = "`, and it was line 72" — CONFIRMED — fix_record.py :14–15 (roots == [71], 0-based). On the as-checked copy, `grep -c '^ROOT = "'` gives 1, and awk gives line number 72.
30. ENTRY — "the old §6 heading occurred once, at line 54" — CONFIRMED — fix_record.py :16–17 (whole-line equality, heads == [53]). On the as-checked copy, `grep -c -x -F` of the seat's old heading (corpus raw :35) gives 1, at line 54; as a substring, also 1.
31. ENTRY — "Two lines changed, each replaced whole by the seat's text" — CONFIRMED:
    - `diff <(sed '54d;72d' as-checked) <(sed '54d;72d' record)`: same;
    - lines 54 and 72 differ (per-line digests);
    - record :54 equals corpus raw :38, and record :72 equals corpus raw :32 (cmp);
    - as-checked :54 equals corpus raw :35;
    - both files have 237 lines.
32. ENTRY — "The diff below is the whole difference" — CONFIRMED — a fresh `diff -u` has exactly two hunks, each with one '-' line and one '+' line.
33. ENTRY — "so G1's record half stands: the §4 table, the stated order and the stated concatenation are untouched" — CONFIRMED — the record's §4 is :31–45 (table :35–43, order and concatenation :45), outside lines 54 and 72. The words are the seat's §2.4 (:45). See observation 4.
34. ENTRY — "The old line 72's value is elided" — CONFIRMED — the entry's '-' line is `ROOT = "<the laptop's checkout>"`. `grep -c Users` over ENTRY, CLOSE and GITIGNORE gives 0 each.
35. ENTRY — the diff headers "--- data/n/passages.prompt.md (as checked, 323cf9d8…44b5, 18,167 B)" and "+++ … (as committed)" — CONFIRMED — the values are those of items 25–26. These two lines are labels, identical to <route18>/record.diff :1–2.
36. ENTRY — the hunk headers "@@ -51,7 +51,7 @@" and "@@ -69,7 +69,7 @@" — CONFIRMED — fresh `diff -u` of the as-checked copy against the record.
37. ENTRY — the diff body (entry :29–46) — CONFIRMED — the fresh `diff -u`, with its '-ROOT' line elided by sed (Users count 0 before any compare), equals entry :29–46 de-indented and <route18>/record.diff :3–20 (cmp). Entry :27–46 de-indented equals <route18>/record.diff entire, which equals <scratch>/record.diff.
38. ENTRY — "+## 6. The validator, as run but for its `ROOT` line (line 72 of this file) … as run, sha256 cc1fad61…f269, 8889 bytes … as committed, sha256 95c93878…0bc5, 9008 bytes" — CONFIRMED — equals corpus raw :38 (cmp against record :54). A shell pattern match finds both full digests and both byte counts of items 41–42 on record :54.
39. ENTRY — "-ROOT = "<the laptop's checkout>"" — CONFIRMED — the elision form that corpus raw §2.4 (:45) prescribes.
40. ENTRY — "+ROOT = os.environ.get("JSPACE_LAB_ROOT", "")  # recover mode's path prefix; …" — CONFIRMED — record :72 equals corpus raw :32 (cmp).
41. ENTRY — "The validator, extracted by the acceptance check's `awk`: as run cc1fad61…f269, 8,889 bytes" — CONFIRMED — `awk '/^```/{n++; next} n==1'` on the as-checked copy (two fences, at :56 and :237), piped to shasum and wc -c: cc1fad61…f269, 8889. The acceptance raw :53–56 describes the extraction the same way; it does not print the exact awk.
42. ENTRY — "as committed 95c93878…0bc5, 9,008 bytes" — CONFIRMED — the same awk on the record gives 95c93878…0bc5, 9008. It is cmp-equal to <route18>/validate.as-committed.py.
43. ENTRY — "the seat's §2.3 values" — CONFIRMED — corpus raw §2.3 :43 (8889 B cc1fad61…f269; 9008 B 95c93878…0bc5, in full); also :9.
44. ENTRY — "Code's re-check, by tool: the record's sha256 and bytes; the extraction's; lines 54 and 72 equal to the seat's §2.2 lines; the record identical to the as-checked copy outside those two lines; and a fresh elided `diff -u` equal to the one above" — CONFIRMED as facts — each one reproduced (items 23–24, 41–42, 31, 37). The diff equality holds from the first @@ line; see observation 5.
45. ENTRY — that Code ran those checks — NOT CHECKABLE — Code's own run.
46. ENTRY — "`.gitignore` admits data/n/passages.parts/, data/n/passages.jsonl and data/n/passages.prompt.md, each on its own line under one comment, after the ids' block" — CONFIRMED — GITIGNORE :2–5 is one comment and :6–8 the three lines. The anchor .gitignore :271 ends the ids' block (:266–271).
47. ENTRY — "Next (the corpus raw's §3 items 3 and 4)" — CONFIRMED — corpus raw :51–52.
48. ENTRY — "the render of ADDENDUM-n1 §1.2 (iv), gvec_passages.jsonl from the committed file and a3_contexts.jsonl (the 1,344)" — CONFIRMED — <repo>/ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md :22, "(iv) `gvec_passages.jsonl` (the 544 of `data/n/passages.jsonl`) and `a3_contexts.jsonl` (the 1,344)"; corpus raw :51.
49. ENTRY — "in G-DATA's environment in a battery window, MANIFEST.json extended, as `n — ids of record`'s second commit" — CONFIRMED — corpus raw :51. RESULTS.md :1816 holds the "n — ids of record" entry.
50. ENTRY — "G-VEC, on the box raw's ruling" — CONFIRMED — corpus raw :52; paste item 4, "G-VEC on the box ruling [go]"; box raw §0 :7–9.
51. ENTRY — "Committed by path: the nine parts, data/n/passages.jsonl, data/n/passages.prompt.md, .gitignore, and RESULTS.md (this entry, and n-build's close line on fa96ccf's entry)" — CONFIRMED as the commit's declared scope — corpus raw §3 item 2 (:50, by path in one commit) and item 5 (:53); paste item 4. See observation 6.
52. ENTRY — "Not pushed." — NOT CHECKABLE — the commit is still to come. It is consistent with paste item 12, "push behind the screen when you say".

CLOSE
53. CLOSE — "Close (PI date 2026-11-18)" — CONFIRMED — paste :1.
54. CLOSE — "n-build's" — CONFIRMED — corpus raw :3 (n-build adds close lines) and §3 item 5 (:53); 26cf7d2's close line (RESULTS.md :73–75), "n-build's on `fa96ccf`'s entry (§3 item 5)".
55. CLOSE — "the seat's adoption" and its link to 2026-11-18_n-corpus-adoption_design-to-code_answers.md — CONFIRMED — the file is at results/raw and tracked since 26cf7d2.
56. CLOSE — "sha256 5843a9bd…7165" — CONFIRMED — shasum; paste :5. The blob at 26cf7d2 equals the working file (git rev-parse against git hash-object).
57. CLOSE — "routed by the PI's 'Route as given'" — CONFIRMED — paste :31–32.
58. CLOSE — "the corpus is adopted on the every-tenth read" — CONFIRMED — corpus raw :1 and :7; paste item 1.
59. CLOSE — "CR1–CR10 are accepted as written" — CONFIRMED — corpus raw §1.3 :20.
60. CLOSE — "Code's proposal on the naming is adopted, so G-VEC's wiring maps `flow_engagement` to BK's words, with no corpus edit" — CONFIRMED — corpus raw §1.4 :22; paste item 1.
61. CLOSE — "G8's set is the brief's twelve" — CONFIRMED — corpus raw :8; paste item 2.
62. CLOSE — "CR6 stands and G8 holds" — CONFIRMED — corpus raw :8.
63. CLOSE — "the broader reading (cedar ×1, gravel ×6) is not adopted" — CONFIRMED — corpus raw :8. `grep -c -w -i` over data/n/passages.jsonl gives:
    - cedar 1 (serenity-17);
    - gravel 6 (serenity-15, serenity-51, weariness-21, weariness-29, dread-48, neutral-15);
    - plurals 0.
    The acceptance raw :111–118 agrees.
64. CLOSE — "(the seat's ledger (80))" — CONFIRMED — corpus raw §6 :75 and §0 :8; paste item 2.
65. CLOSE — "its ROOT line and its §6 heading are replaced by the seat's lines before the commit" — CONFIRMED — corpus raw :9 and §2.2. The record's :54 and :72 are the seat's lines (item 31), and the record is not yet tracked (`git ls-files`: 0).
66. CLOSE — "(the seat's ledger (81))" — CONFIRMED — corpus raw §6 :76 and :9; paste item 3.
67. CLOSE — "the four argv departures are inert" — CONFIRMED — corpus raw §4 :55–57 ("inert, no strike"); paste item 5.
68. CLOSE — "N.2's commit carries the corpus of record (its entry at the top of this log)" — NOT CHECKABLE — the commit is still to come. It is consistent: the log is newest-first (RESULTS.md :15–16), and 26cf7d2 added only a close line, so e48c7d0's entry (:24) is still the top one.
69. CLOSE — target entry "- 2026-11-17 — **n — the corpus's acceptance check and assembly" — CONFIRMED — one match, at RESULTS.md :108; the entry ends at :180 with "…as for `data/n/ids/`. Not pushed."

GITIGNORE
70. GITIGNORE — insertion "right after the line !/data/n/ids/" — CONFIRMED — `grep -c -x -F` gives 1, at :271, the last line of the ids' block (:266–271), followed by the blank line :272. The block's leading blank line keeps the separation.
71. GITIGNORE — "PROPOSAL-n's passage corpus (Route B; n v0.2 §0.8 and §3 G-VEC" — CONFIRMED — <repo>/PROPOSAL-n-bk-reconciliation-v0_2.md:
    - :2, v0.2;
    - :36, §0.8, "Route B (the default, run regardless)";
    - :105, §3 Gates;
    - :111, G-VEC, "the passage corpus committed (`data/n/passages.jsonl`, 544 passages …)".
72. GITIGNORE — "the seat's answers of 2026-11-18, §3 item 2" — CONFIRMED — corpus raw :50.
73. GITIGNORE — "the nine part files the seat thread wrote" — CONFIRMED — record :3 ("A seat thread …") and :15 ("The seat wrote the 544 passages itself, directly into the nine files"); fa96ccf's entry, "The inputs" bullet ("the seat thread's nine part files").
74. GITIGNORE — "their concatenation in the brief's order" — CONFIRMED — a `cat` of the nine in the record's stated order (:45), piped to cmp against data/n/passages.jsonl: equal.
75. GITIGNORE — "(544 passages, the corpus of record for G-VEC's direction)" — CONFIRMED — wc -l gives 544; corpus raw :7; PROPOSAL-n :36 and :111.
76. GITIGNORE — "the thread's prompt record" — CONFIRMED — record :1–3.
77. GITIGNORE — "Record, not cache (ledger 27)" — CONFIRMED — CLAUDE.md :354 (ledger 27, "the repo, not any machine, is the record"). The bk and ids blocks use the same form (.gitignore :258–259 and :269).
78. GITIGNORE — "G-VEC builds the direction from them" — CONFIRMED — PROPOSAL-n :111, "the direction built by §0.8's recipe" on the committed corpus. See observation 8.
79. GITIGNORE — the three admit lines and their effect — CONFIRMED by reading the rules: `/data/*` (:5), `!/data/n/` (:262) and `/data/n/*` (:263). The new lines take the same form as `!/data/n/ids/` (:271), and no later rule matches *.jsonl, *.md or these names. Today `git status --porcelain --ignored` gives "!!" for each of the three, and `git ls-files` gives 0.

Replacement wording for the IMPRECISE items
- Item 8: "The adoption is the seat's answers of 2026-11-18, [`2026-11-18_n-corpus-adoption_design-to-code_answers.md`](results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md) (§0–§1; this commit carries its §3 items 1, 2 and 5); the check is `fa96ccf`'s raw, [`2026-11-17_n-corpus_acceptance.md`](results/raw/2026-11-17_n-corpus_acceptance.md)."
- Item 11: "**The PI's routing of 2026-11-18,** "Route as given"; its section N for n-build, items 1–5, verbatim:"

Observations
1. **The brief's pointer for the 2026-11-17 block finds nothing.** "Files placed untracked" does not occur in results/raw/2026-11-17_n-corpus_valuescheck.md (grep, case-insensitive: no match), and that raw does not quote the block's file list. The per-part figures are in the acceptance raw: §6's G1 rows (:171–179) and §8's BLOCK (:431–441). Items 18 and 25 were checked against those. The entry could cite them, for example "the block of 2026-11-17, as the acceptance raw's §6 and §8 carry it".
2. **COORD_COMMIT now exists: 26cf7d2** (parent e48c7d0). It commits RESULTS.md, both seat raws and results/raw/2026-11-18_box-gpu-close_valuescheck.md. Its corpus-raw blob equals the working file.
   - RESULTS.md moved during this check: fa96ccf's entry is now :108–180 (it was :64–136), and the new close line on e48c7d0's entry is :63–106.
   - Insert the drafts against the current file; the tree is shared, so re-read it first.
   - The entry's link to the corpus raw resolves only from 26cf7d2 on; the entry could cite 26cf7d2, as the CLOSE will.
3. **The coordinating script is not in the repo and the entry omits some of its assertions.**
   - The script is <route18>/fix_record.py (sha256 ae89347a…9dde, 2,495 B, untracked). Its run output (the print at :31–32) is not among my sources, so items 28–30 rest on its text plus the inputs meeting each assertion.
   - Two more of its assertions are not in the entry. Before replacing, it checks the as-run extraction (:22–23). After replacing, it checks the as-committed extraction (:25–27) and that the result compiles (:28), which is the seat's §2.2 "The new script parses".
   - Its extraction is a Python split at the fences (:18–21), not the acceptance check's awk; the awk values in items 41–42 are the re-check's. Under "The record's correction" the extraction bullet can read as the script's own act. A clearer form: "…extracted by the acceptance check's `awk` (Code's re-check; the script's own split at the fences asserted the same values)…".
4. **G1's labels and scope.** §2.4 asks the entry to name the record as checked "(323cf9d8…44b5, 18,167 B, G1's)". The entry gives the values, in the files bullet and the diff header, but not as G1's. G1 also compared the record's whole-file sha256 and bytes with the block (CR1; acceptance raw :180), and the committed record no longer matches those. "G1's record half stands" is limited to the table, order and concatenation, as the seat wrote it, but the seat may want the whole-file change named beside G1.
5. **"a fresh elided `diff -u` equal to the one above".** diff -u's own two header lines carry paths and times; the block's header lines are labels. My regeneration equals the block from the first @@ line (18 lines). Unless Code's fresh diff used --label, the exact form is "whose hunks equal those above".
6. **No values-check raw in "Committed by path".** fa96ccf, e48c7d0 and 26cf7d2 each committed theirs. If this report is to be committed, add it to the list.
7. **No model statement.** The entry has no "Model-free" or "Nothing ran on a model" line, which neighbouring entries carry.
8. **"G-VEC builds the direction from them" is loose.** G-VEC builds from the 544, as ids rendered by (iv); the parts and the record are their provenance, and G-VEC's gate text requires the corpus committed and the prompt recorded. An optional precise form: "G-VEC builds the direction from the 544; the parts and the record are their provenance."
9. **Next omits one sentence.** §3 item 4's second sentence ("(v), G-CAL-n's prompts, is rendered when that stage's prompts are fixed in its wiring") is not in the entry's Next; optional.
10. **The paste block is not committed.** The entry's quote of section N, items 1–5, is the tree's only record of the PI's N items, as 26cf7d2's quote is for section B. The PI's items expand the seat's §7 wording, and the entry correctly quotes the PI's.
11. **The .gitignore effect was checked by reading the rules,** not by `git check-ignore`, which is outside the brief's tools. The parts folder holds exactly nine entries (`ls -A`), so the folder admit lets in nothing else.
12. **The CLOSE leaves out one restated rule.** The seat's §4 restates "G-DATA's venv is started only inside a battery window", and the CLOSE does not carry it. It is in the entry's quoted item 5 and in the Next item's "battery window"; optional.
13. **Outside these drafts — for the seat and the PI: RESULTS.md already carries the home-folder path.** RESULTS.md :11646, in an older entry, contains four occurrences of the laptop's home-folder path, which names the user. I counted them against $HOME with `grep -o -F | wc -l` and never displayed the line. The pickaxe names de6dfc5 (2026-10-19), which is an ancestor of origin/main (local tracking ref, fa96ccf). This is the class that ledger (81) addresses.

Totals: 79 items — 73 CONFIRMED, 2 IMPRECISE (8, 11), 0 FAIL, 4 NOT CHECKABLE (17, 45, 52, 68) — and 13 observations.
```
