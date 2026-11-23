# n — LOCK-n v1.0's draft 9, entry and two raws: the second blind values-check, as returned, with every disposition

PI date 2026-11-22. Code (the n-build session).

**What was checked.** One blind pass by a subagent over four texts, at HEAD `d714372`:
- T1, LOCK-n v1.0's draft 9, sha256 `c3316e62…45fd` (1438 lines: the v1.0 part 380, v0.1's text 1058), its changes from
  draft 7 above all;
- T2, the entry as then revised, `96c3b578…bdd5` (166 lines), with placeholders not to be checked: the placement's
  three (then with the PI), later drafts, this check's summary and its departures, and one count for the final sweep;
- T3, draft 9's checks raw as staged, `099033cf…2ff7` (37 lines);
- T4, the first values-check's raw as staged, `62a6d626…43b0` (331 lines).

**The checker's brief** was its prompt by reference: Code's scratch file `S/step4b/lock10/vc2_brief.md`
(`1ffb07d5…ed45`, 136 lines), which the checker read whole and hashed first. It:
- named the texts and the sources: in the repository, the files the texts cite, at `d714372` (BK's 26 files by
  `shasum -c` alone, the report by `shasum` alone); in Code's scratch, the tools, the entry's two sources, the first
  values-check raw's head before and after its fill, the first report and brief, the kept drafts 1–9, draft 7's
  checks raw, the generator's re-run and the commit kit's library; and the first checker's transcript, by `jq`, for
  its hand-back alone;
- asked above all for draft 9's changes from draft 7, every claim the new HEAD could move, the analyzer's rules, the
  routing items one by one, and each of the first raw's dispositions against the text it says was changed;
- allowed `shasum` by name, and `jq` on the sweep records, on this session's transcript, on the first checker's
  transcript for its hand-back, and on committed JSON and JSONL outside `data/*/ckpt`, `data/*/reports` and
  `data/m[f]3`;
- set the transcript's use: a sweep of Code's tool calls from the first brief's hash to this brief's own hash, with
  Code's extraction of the span up to its last record (104 calls) beside it;
- barred any other interpreter, any write, any network and any redirect to a device or into a file; any guard marker
  in an argv (a path, a grep pattern, a variable or glob that expands to one, a loop, the command's own text);
  anything under `data/m[f]3` and any whole-tree git status; any read, listing, size or time of a ckpt or reports
  file, and any `--stat` form over a commit that holds one; and anything in Code's scratch but the named files;
- quoted the list of record v2's items 1–5 verbatim (byte-equal to the first brief's, by `cmp`), and required item 3's
  pathspec and the campaign folder's exclusion on every git command over the tree.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (250 lines, sha256
`70b65a3e…7802`). It names scratch files by their paths inside the scratch folder (L is `S/step4b/lock10`), this
session's transcript as T and the first checker's as X.

**Totals:** 106 items: 82 CONFIRMED, 14 IMPRECISE, 5 FAIL, 5 NOT CHECKABLE; and 8 observations. Code counted them
again by tool, by the verdict on each item's line inside the report's ITEMS section.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

Every FAIL and every IMPRECISE item is applied, in the checker's words or near them; every observation is applied,
met or put to the seat. "Draft 10" is the draft that applies them, and the draft placed.

- **Items 80, 82 and 85 (FAIL), the entry's departures list.** Applied: eight redirects to `/dev/null`, not six; five
  command outputs and one file-tool read printing the campaign folder's plain name, not four outputs; and the
  generator's read loop that passed `SHA256SUMS`'s marker-named paths in a variable to builtin `printf`, at every run,
  declared, with observation 1.
- **Items 97 and 105 (FAIL), the first values-check raw's head.** Applied: "draft 8" is the draft that applies the
  first check, and the second check read draft 9.
- **Items 5, 32 and 38 (IMPRECISE), the draft.** Applied in draft 10, in the checker's words: the header names the
  driver's `LOCK_SHA256` line alone as placed by its text; v1.0 §10's sentence keeps v0.1's text verbatim by
  WORKFLOW.md:43 and has the seat make the dated notes in its raw (ans21a:8, :15); v1.0 §13's order of reads says the
  second sitting read G-VER's entry, record and out raw (ans22b:3), with observation 8.
- **Item 52 (IMPRECISE), the checks raw.** Applied: its section 2 says "outside its tables and blockquotes", in the
  checks-raw script, which draft 10's checks raw runs.
- **Items 65, 66, 69, 70, 71, 76 and 79 (IMPRECISE), the entry.** Applied in the checker's words: the placement's
  quotation and its sources; RESULTS.md's cited lines and the driver's `LOCK_SHA256` line; rt22b among draft 8's
  sources; draft 9's two lines and its re-ordered item; "tables and blockquotes"; the reads it had not named; and the
  scratch kinds it had not named.
- **Items 91, 103 and 104 (IMPRECISE), the first values-check raw's head.** Applied in the checker's words.
- **The five NOT CHECKABLE items** (7, 45, 59, 87 and 93) are plans or limits of the checker's sources, left as stated.
  Item 93's own check stands: the second brief's items 1–5 equal the first's by `cmp`.
- **Observation 1, the generator's loop.** Applied: from draft 10 the table is built by `sed` over the file's stream,
  the same 26 rows byte for byte (by `cmp` against draft 9's), and the loop's runs are declared for the seat to class.
- **Observation 2, the interval after step 13's commit.** Applied in v1.0 §12, and put to the seat in the entry.
- **Observation 3, the committed status line.** Applied: v1.0 §13 shows its two lines in a fenced block, wrapped as
  v0.1's are at L:3–4.
- **Observation 4, the order of reads.** Put to the seat in the entry: whether the draft's sitting re-reads G-VER's
  record (ans22a:7; ans22b:3).
- **Observation 5, the fill script's version.** Applied: every fill in the entry and in the two raws' heads was made
  again by the fill script's final version, whose sha256 the entry gives.
- **Observation 6, the stale comment.** Applied in the checks-raw script.
- **Observation 7, the final sweep.** Met: Code's final sweep runs from this brief's hash to the commit kit, and the
  entry's departures carry what it finds.
- **Observation 8, "this raw".** Applied in v1.0 §13: "this raw" being ans22b.

## 2. The edits, checked by tool

The edits after this check's brief were made to the seven sources its texts are built from, each snapshotted first
(`S/step4b/lock10/vc2_snap/`). The replay script `S/step4b/lock10/replay_vc2.sh` recovers each Edit call made after the
brief's hash from this session's transcript by `jq` and replays it on its file's snapshot, each old text found exactly
once, and compares each result with the file as it now stands, byte for byte:

32 of 32 edits over the seven files, each old text found exactly once, each result its file byte for byte.

The texts were then made again from those sources by the generator, the checks-raw script and the fill script.

## 3. The report, as returned

```text
**Values-check of LOCK-n v1.0's draft 9 (T1), the entry (T2), the checks raw (T3) and the first values-check raw (T4)**

I read the brief whole and confirmed its sha256 (1ffb07d5…ed45, 136 lines). HEAD is `d714372` and did not move while I worked. T1–T4, L/vc_report.md, L/vc_brief.md, L/check_raw_draft7.txt, L/sweep2.jsonl, L/sweep2_view.txt, S/step4b/kit2/kit_lib_v3.sh, the tools at T3's sha256s and drafts 1–9 at T2's abbreviations all match. Every repository file the texts cite is tracked and clean at `d714372`.

Overall: T1 holds up. Every sha256, commit id, anchor and quotation checks out. Committed as the lock, it passes `lock_route`, `lock_gate` and `lock_names`, and its tail is v0.1 byte for byte. The problems are mostly in T2's departures list: 3 FAILs, plus one undeclared loop that passed marker-named paths. T4 has 2 FAILs: twice it says this check reads draft 8, when it reads draft 9.

## ITEMS

**T1, the v1.0 part (lines 1–380) and the tail**

1. **T1 (whole)**: sha256 `c3316e62…45fd`, 1438 lines (380 + 1058). **CONFIRMED.** By `shasum` and `sed -n '$='`.
2. **T1:7**: drafted at HEAD `d714372`. **CONFIRMED.** By `git rev-parse HEAD`.
3. **T1:7–8**: routed by rt21c item 4, rt22a item 3 and rt22b item 2. **CONFIRMED.** rt21c:24–29, rt22a:29–31, rt22b:20–24.
4. **T1:8–10**: the form quote "re-issued above the prior version's text kept verbatim" (WORKFLOW.md:43), as LOCK-m-F3 v1.0's form. **CONFIRMED.** WORKFLOW.md:43 sits in §5 (:39). LOCK-m-F3.md's v1.0 part ends at :321 and v0.2 starts at :323.
5. **T1:10–12**: a tool placed "the cited lines of RESULTS.md and of the driver from their text". **IMPRECISE.**
   - gen_v10.sh places every 64-hex value (v10_part_src.md types none) and RESULTS.md's three anchors (@RLA@–@RLC@).
   - Of the driver's four cited anchors, only :3820 (@NSL@) is placed by its text. :4373, :3913–3914 and :5167–5168 are typed, though all are correct at `d714372`.
   - Instead: "…the two tables (v1.0 §7, v1.0 §9) from their committed sources, and the cited lines of RESULTS.md and the driver's `LOCK_SHA256` line (v1.0 §12) from their text."
6. **T1:12–14**: a tool found every quotation and BK's ids, and checked that each named commit is the file's last change. **CONFIRMED.**
   - Every quotation in the part is one of check_quotes.sh's 61 rows (:24–84). My own shell loop over the rows, whitespace collapsed and blockquote markers stripped, found 61 of 61 in T1:1–380 and in their sources.
   - The commit check is check_ids.sh's 12 rows, with my own `git log -1` per path.
7. **T1:14**: "Code typed the prose. Nothing in this file has run." **NOT CHECKABLE.**
8. **T1:30–32**: rt22b:20–24, verbatim. **CONFIRMED.** Joined lines are string-equal.
9. **T1:34–36**: ans22b:30, verbatim. **CONFIRMED.** String-equal.
10. **T1:38–51**: the section list, including §11–§13. **CONFIRMED.** It matches the headings at T1:335, :348 and :356.
11. **T1:55**: anchors are at HEAD `d714372`. **CONFIRMED.**
12. **T1:65–70**: the short forms ans22b, rt21a–c and rt22a–b, with their paths and sittings. **CONFIRMED.** Paths are tracked; ans22b:3 says "second sitting".
13. **T1:86–87**: the ans21c:26 loads quote, "beside the cap". **CONFIRMED.** ans21c:26 is in §1.3, "The pod hours beside the cap".
14. **T1:107–109**: `hour_cap_ms` (runner.py:266) is 14,400,000 ms; ans20b:39's quote; G-TIME-n's stage passed none (n_sessions.py:4373); a resume keeps the cap (runner.py:413–414). **CONFIRMED.**
    - :4373 is `hour_cap_ms=None`, inside `_gtime_prepare` (:4237).
    - No campaign command is wired (n_sessions.py:285).
    - The BUILD's passing of the cap is a plan.
15. **T1:112–115**: L:602–603's words; ans21b:23 "on the laptop they are outside the cap by the same sentence". **CONFIRMED.**
16. **T1:138–160, :174–190, :211–212, :229**: every "at `d714372`" claim. **CONFIRMED.**
    - 31 files are clean, by `git rev-parse` against `git hash-object`.
    - Each sha256, recomputed, equals T1's.
    - time.json is `3ae33a39…d8a7`, by `shasum` alone.
17. **T1:145–146**: "WORKFLOW.md v1.0, whose §5 sets this file's form (WORKFLOW.md:43)" and `e7195706…b061`. **CONFIRMED.** WORKFLOW.md:1 says v1.0.
18. **T1:161–166**: the driver is at `2834c2d` (`55885e65…385f`); the package is `06b55761…1d39`, by pkg_rev over `d714372`'s 16 `.py` blobs. **CONFIRMED.**
    - My own pipeline in pkg_rev's form gives the same digest.
    - It equals gver.json's `pins.package_sha256`.
    - `git log -1` of n_sessions.py gives `2834c2d`.
19. **T1:174–191**: the chain's commits. **CONFIRMED.** Last changes by `git log -1`: `e3b48ed` (gvec.json, directions_L32.npy), `db00d6d` (gcal.json, dose_map.json, gcal_turns.jsonl), `1641948`, `deabf3f` (LOCK-n.md's only commit) and `fd5d61c`.
20. **T1:185–186**: G-TIME-n's artifact carries `lock_sha256` and G-VER's record carries `pins.lock_sha256`. **CONFIRMED.** jq paths to v0.1's sha256: gtime.json `[["lock_sha256"]]`; gver.json `[["pins","lock_sha256"]]`.
21. **T1:188–189**: accepted as the gate of record (ans22b:7; rt22b item 1). **CONFIRMED.** The quote is in ans22b:7; see rt22b:17.
22. **T1:192–195**: R2 with its "where" cell, and "the seat's "§10" is v0.1's numbering". **CONFIRMED.** L:541–543 carry the head and the row; v0.1 §10 is at L:533; v1.0 §10 is at T1:309.
23. **T1:197–199**: the end line is the stage raw's line 20 (its last) and the out raw's line 118. **CONFIRMED.** By `sed -n`.
24. **T1:211–212**: schema.py at `d714372`, `1cab28df…edff`. **CONFIRMED.**
25. **T1:219–220**: rt21c:32, rt22a:34 and rt22b:30 each hold the quote. **CONFIRMED.**
26. **T1:229–259**: `shasum -c` prints 26 lines ending ": OK", and the 26 table rows. **CONFIRMED.**
    - Exit 0, 26 OK, 0 other lines.
    - `diff` against rows rebuilt from SHA256SUMS by `sed` is empty.
27. **T1:270–273**: the route line is L:844 (in §20, from L:837) and the gate line L:935 (in §21, from L:854); the ans20b:50 and rt21c item 4 quotes. **CONFIRMED.**
28. **T1:274–276**: the analyzer reads the one stripped line by its head and refuses none or two or more; blockquoted lines do not count. **CONFIRMED.** n_analyze.py:6248–6251, :6268–6272, and the docstring at :6264–6265.
29. **T1:278–282**: the blockquote's three lines. **CONFIRMED.** They equal `LOCK_V10_LINE` (:6236), L:844 and L:935.
30. **T1 under the analyzer's rules** (grep, no Python). **CONFIRMED.**
    - `lock_route`: one stripped whole line `lock: LOCK-n v1.0` (T1:267), and exactly one line starting "direction of record: Route" (T1:1224 = L:844), so it returns B.
    - `lock_gate`: exactly one head line (T1:1315 = L:935), well formed, giving Gate(48, PASS).
    - `lock_names`: `735da934…` stands between backticks at T1:210 and :898.
    - The blockquote's lines strip to ">…" and count for no rule.
    - T1 holds no tab, CR, VT, FF, FS/GS/RS, NEL, NBSP, LS/PS or U+2000–200A/202F/205F/3000. So Python splits and strips its lines as grep does.
31. **T1:295–296**: RESULTS.md:2014–2015 and :2026, in G-TIME-n's entry (`7d01b02`). **CONFIRMED.**
    - The text is equal to `fd5d61c`'s :1651–1652 and :1663, shifted by `d714372`'s hunks (+349 at :24, +14 at :715).
    - The entry's head is RESULTS.md:1973, with no entry head between.
32. **T1:315–317**: "stands below, verbatim, as a dated note (WORKFLOW.md:43)". **IMPRECISE.**
    - WORKFLOW.md:43 supports "kept verbatim", but defines a dated note as "a RESULTS.md entry, never an edit of the lock".
    - The seat made the sentences dated notes in its own raw (ans21a:8, "each is a dated note here"; :15).
    - The ans21a:8 quote and the :40 citation are correct.
    - Instead: "Each of v0.1's sentences stands below, verbatim, as v0.1's text is kept (WORKFLOW.md:43); the seat made each a dated note in its raw (ans21a:8, :15), and v1.0 carries the corrected words (ans21a:8, "LOCK-n v1.0 carries the corrected words at step 13"; ans21a:40), these:"
33. **T1:320–321**: note (b), with "for a crashed invocation". **CONFIRMED.** L:870–873; A-n3:60.
34. **T1:337–342**: §11's list of Code's readings. **CONFIRMED** as to the texts: L:543, ans22a:31, ans20b:18.
35. **T1:343–346**: what v0.1 left to v1.0. **CONFIRMED.**
    - L:75 ("hole 18 … is v1.0's (§16)"); §16 at L:729; §22 at L:944, with :947–948.
    - L:554 (the cap row); L:587–607 (§11; the sentence ends at :608 with "(ans19b:41).").
    - L:847, L:852, L:985, L:996.
36. **T1:350–351**: VERDICTS refuses a lock that is not the identity's `lock_sha256`. **CONFIRMED.** n_analyze.py:6687–6689; the campaign's own identity is still to come.
37. **T1:352–354**: `LOCK_SHA256` (n_sessions.py:3820) is v0.1's; the refusal quote at :3913–3914 (`gtime_lock_inputs`) and :5167–5168 (`gver_lock_check`). **CONFIRMED.**
38. **T1:358–360**: "ans22a §1.7 sets the order: the seat's next sitting reads G-VER's entry, record and out raw first and the draft second". **IMPRECISE.**
    - This is ans22a:35's text, but it is stale at `d714372`: the next sitting (the second of 2026-11-22) read the three without the draft (ans22b:3).
    - Instead: "ans22a §1.7 set the order, G-VER's entry, record and out raw first and the draft second, both before the commit; the seat's second sitting of 2026-11-22 read the first three (ans22b:3), and the draft is read whole in one sitting (ans22b:30)."
39. **T1:361–368**: the n:159 quote; "this file's lines 3–5"; L:3–4; ans20b:18 for the status line and "the first italic paragraph stays as history". **CONFIRMED.** The proposed status line's words are Code's.
40. **T1:369–374**: after the seat's handoff (ans22b:31); the three requirements and the correction (ans22b §1.3–§1.4, :22 and :24; rt22b:25–27); step 15. **CONFIRMED.** See n:159.
41. **T1:376–379**: `---` and the precedence sentence, as LOCK-m-F3.md:321 has them. **CONFIRMED.** LOCK-m-F3.md:319 and :321.
42. **T1:381–1438**: against `git show d714372:LOCK-n.md`. **CONFIRMED.** `cmp` finds them equal; both are `88d9fe7b…e9d5`, 1058 lines.
43. **T1 against rt22b item 2, item by item.** **CONFIRMED** for all eleven items:
    - the projections (§1), the cap 4 h (§2), D_n (§3), the hashes (§4) and the chain (§5);
    - the analyzer v7 (§6), its gate line once at L:935 and quoted in §8 (Code's reading);
    - BK's files (§7) and the G-VER row with `fd5d61c` and "PASS, 160 of 160" (§5);
    - the zero line (§9), the dated notes (§10), v0.1 beneath, and the whole read (§13).
    - The placement and the sha256 and line count belong to T2 and wait on the PI.
44. **T1 against ans22b:30, item by item.** **CONFIRMED.**
    - Every figure is present: 1.0494 h, 1.6334 h, 0.9–2.6 h and its shape, 15.5 MB/s, 2.650 h.
    - Also present: the cap, D_n, the four documents' hashes, the chain, v7 and the gate line, BK, and the G-VER row's record with the entry, sha256, "PASS, 160 of 160" and end line (in v1.0 §5, R2).
    - Also present: the zero line, the three notes corrected, A-n3 §7's notes and ans22a §3's two, `lock: LOCK-n v1.0` with the route line, v0.1 verbatim, and the read "in one sitting".
45. **T1:3–5, :108 ("is to pass it"), :354 ("moves the pin"), :361–366, :369–371**: the commit and BUILD steps. **NOT CHECKABLE.** These are plans.

**T3, the checks raw**

46. **T3**: `099033cf…2ff7`, 37 lines; the title at `d714372`. **CONFIRMED.**
47. **T3:3**: draft 9, `c3316e62…45fd`, 1438 = 380 + 1058. **CONFIRMED.**
48. **T3:5–10**: the six tools' sha256s. **CONFIRMED.** All six recomputed.
49. **T3:14–16**: the re-run's lines. **CONFIRMED.** My greps (item 30), RESULTS.md at `d714372`, n_sessions.py:3820 and `shasum -c` agree.
50. **T3:17**: "gen exit: 0". **CONFIRMED** by consequence: gen_v10.sh:101 moves the output into place only after every assertion, and L/regen_draft9.md exists.
51. **T3:18**: `cmp` finds them equal. **CONFIRMED.** L/regen_draft9.md equals T1.
52. **T3:20–22**: no line over 120 characters "outside its tables and quotations". **IMPRECISE.**
    - make_check_raw.sh:38 exempts every line starting with `|` or `>`.
    - T1:366 (151 characters) is a blockquote of Code's proposed status line, not a quotation.
    - Instead: "## 2. Lines of the v1.0 part over 120 characters (UTF-8), outside its tables and blockquotes".
53. **T3:26–28**: 61 quotations found, 0 not; exit 0. **CONFIRMED.** See item 6.
54. **T3:32–33**: 12 last changes, 0 not; exit 0. **CONFIRMED.**
    - 11 paths by `git log -1`.
    - The report by `git rev-parse` alone: its blob at `7d01b02` equals the one at `d714372`, and is absent at `7d01b02^`.
55. **T3:37**: the tail. **CONFIRMED.**

**T2, the entry**

56. **T2**: `96c3b578…dbdd5`, 166 lines. **CONFIRMED.**
57. **T2:1–3**: the routings; `c3316e62…45fd`, 1438 lines; anchors at `d714372`. **CONFIRMED.**
58. **T2:3–5**: read whole (rt21c:29); the ans22b:30 quote; "after G-VER's entry, record and out raw (ans22a §1.7)". **CONFIRMED.** That reading was done at ans22b (see Obs 4).
59. **T2:5–6**: committed by path; step 13 commits the draft. **NOT CHECKABLE.**
60. **T2:8–14**: the headline. **CONFIRMED.**
61. **T2:15–31**: what v1.0 carries, section by section. **CONFIRMED.**
62. **T2:33–35**: what v0.1 left to v1.0. **CONFIRMED.** It abbreviates T1:343–346.
63. **T2:36–40**: the rules as the generator asserts them, and "No Python read the draft". **CONFIRMED.** gen_v10.sh:91–97; no Python ran in the span.
64. **T2:41–49**: Code's readings, and two readings now rulings. **CONFIRMED** as to the texts.
65. **T2:50–52**: the placement, quoting "untracked at root under the lock's name". **IMPRECISE.**
    - Those exact words are rt21c:24–25's. ans22b:30 and rt22b:20 say "at the root".
    - The rest holds: `deabf3f` is LOCK-n.md's only commit, and the driver checks are at n_sessions.py:3913–3914 and :5167–5168.
    - Instead: "so "untracked at root under the lock's name" (rt21c item 4; "at the root", ans22b:30 and the second sitting's item 2) cannot hold in both words."
66. **T2:53–57**: "RESULTS.md's and the driver's cited lines by their text". **IMPRECISE.** Same fault as item 5. Instead: "RESULTS.md's cited lines and the driver's `LOCK_SHA256` line by their text".
67. **T2:57–59**: the final generator and source make draft 9; the abbreviations of drafts 1–9. **CONFIRMED.**
    - Every abbreviation recomputed.
    - gen_v10.sh was last edited at 03:26:14; the source's last change is the 04:24:04 `sed -i`. Both come before draft 9's run (04:24:04).
68. **T2:60–70**: drafts 2–7. **CONFIRMED.** My `diff` of drafts 3→4's parts shows every listed change.
69. **T2:71–73**: draft 8, "with ans22b and WORKFLOW.md among the sources and hashes". **IMPRECISE.**
    - The 7→8 diff also adds rt22b: its short form (T1:69–70), its sha256 (T1:160) and rt22b:30 (T1:219).
    - Everything else listed is in the diff.
    - Instead: "with ans22b, rt22b and WORKFLOW.md among the sources and hashes;".
70. **T2:74–75**: "9 rewraps the two lines that 8's hashes widened". **IMPRECISE.**
    - Draft 8's only over-wide lines were 145 and 188.
    - Draft 9 moves 145's hash to its own line but re-orders §5's item 7: the acceptance clause now comes before the record, and "; PASS:" became ", PASS,"; no value changed.
    - Draft 9 also changes the header (12–14) and drops draft 8's blank line 380.
    - Instead: "9 moves WORKFLOW.md's hash to a line of its own and re-orders v1.0 §5's item 7 (the acceptance before the record; no value changed), the two lines that 8's hashes widened past 120 characters; says the driver's cited line is placed by its text too; and drops a second blank line before v0.1's text."
71. **T2:77–84**: the checks. **IMPRECISE** only in "outside its tables and quotations" (see item 52). Instead: "…outside its tables and blockquotes".
    - The rest is confirmed: the re-run `cmp`, 61 quotations, 12 files with 8 commits, and the tail.
    - Draft 7's raw `16a1fb92…4fa7` is in scratch and was made twice. Its first copy, `ddfdce0a…69d5`, appears in T's tool result at 02:33:54.
72. **T2:85–89**: the first check. Brief `5c22ca32…6ef4`; T4 `62a6d626…43b0`; 127 items: 104 CONFIRMED, 11 IMPRECISE, 3 FAIL, 9 NOT CHECKABLE; 12 observations; the dispositions. **CONFIRMED.** grep over vc_report.md's ITEMS finds 127 item lines with one verdict each.
73. **T2:91–96**: "104 calls, 32 of them shell commands"; bracketed counts 0 and 0. **CONFIRMED.**
    - My extraction from T equals L/sweep2.jsonl byte for byte: 02:36:59.971Z to 04:25:17.513Z.
    - Over all 35 commands in the span: markers [0], the campaign folder's plain name [0].
    - To this brief's hash (04:28:17.952Z) the span is 115 calls, 35 of them shell commands.
74. **T2:97–104**: the steps before `fd5d61c`'s window and the window itself. **CONFIRMED.** The first report's items 116 and 103 are applied in its terms.
75. **T2:105–106**: three memory notes. **CONFIRMED.** Item 104 is applied.
76. **T2:107–112**: reads of committed files, and the file tool's reads. **IMPRECISE.**
    - 03:12:29: `wc -l` (with `shasum`) of the seat's raw of the second sitting while it was untracked. That is neither "committed" nor "by the file tool".
    - The file tool also read the PI's routing raw of the second sitting (04:21:45) and one memory note (02:38:05), neither named.
    - Instead: add "; `wc -l` and `shasum` of the seat's raw of the second sitting before its commit; by the file tool also the PI's routing raw of the second sitting and one memory note".
77. **T2:113–115**: the git forms. **CONFIRMED.** The span uses `rev-parse` (with `origin/main` and `HEAD~1`), `hash-object`, `log -2`/`-3` with ids and subjects, quoted `ls-files`, `show --name-status` with the pathspec, and check_ids.sh's 11 paths.
78. **T2:116–122**: the report's digest, pkg_rev and `shasum -c`. **CONFIRMED.** The generator ran them again at 04:22:52, 04:24:04 and 04:24:18.
79. **T2:123–129**: the scratch kinds. **IMPRECISE.** The enumerations omit:
    - 03:20:39: `wc -c` of L/vc_report.md.
    - 03:27:09 and 04:24:18: `bash -n` of the generator, the two checks and the checks-raw script.
    - 04:26:54: `rm` of L/entry_v3_pre.md and L/entry_v3.md before they were made again.
    - Writes by redirect: L/entry_v3_pre.md by `sed` (04:26:28, 04:26:54); T4 by a grouped `cat`/`printf` (04:24:31, 04:24:55); the brief's items file by a grouped `head`/`sed`/`tail` (04:28:17).
    - Instead: add these to its parentheticals.
80. **T2:130**: "redirects to /dev/null, in six commands". **FAIL.**
    - There are eight: six before the first brief (01:58:20 to 02:23:12) and two after it, at 04:24:31 and 04:24:55, each `>/dev/null` on the fill script's output.
    - Instead: "redirects to `/dev/null`, in eight commands (six before the first brief; two after it, on the fill script's output);".
81. **T2:131–138**: the narrow grep, the recursive grep, the root glob and the zsh slips. **CONFIRMED.** None of these recurs in span 2.
82. **T2:139–140**: "four of Code's command outputs printed it". **FAIL.**
    - Span 2 adds 02:37:11 [1], a comment line of the commit kit's gate script in scratch.
    - The file tool's read of the seat's raw at 03:12:33 printed the name [3] times, in that raw's own text.
    - Instead: "five of Code's command outputs printed it — four before the first brief, in lines read from committed files and memory notes, and one after it, in a comment line of the commit kit's gate script in scratch — and the file tool's read of the seat's raw of the second sitting printed it three times; never in a command's text;".
83. **T2:141–147**: "since the first brief". **CONFIRMED.**
    - 02:37:33: gate v13.
    - 03:13:37: root `ls` into grep.
    - 04:21:42: `show --name-status`.
    - 03:20:27 and 03:20:39: jq over X.
    - 03:28:36: `mv`.
    - 04:24:04: `sed -i ''`.
    - 03:28:21: the temporary file.
    - 04:24:55: `rm`.
    - `EXPECT_HEAD` exported three times.
84. **T2:6–7 and :149**: "Model-free"; "No Python ran; nothing went to the box". **CONFIRMED** for span 2. No interpreter or box tool appears in the 35 commands or among the call kinds.
85. **T2:149**: "Code knows of no others." **FAIL.**
    - gen_v10.sh:64–65 (`while read -r s p; do printf … "$p" "$s"; done < data/n/bk/SHA256SUMS`) passes SHA256SUMS's 26 paths in a variable to bash's builtin `printf`. 14 of them are marker-named.
    - It does so at every generator run: the loop is in the 02:08:09 Write, and runs in span 2 at 04:22:52, 04:24:04 and 04:24:18.
    - No process was exec'd with the paths, but this is the loop-and-variable form the rules name.
    - Instead: add "the generator's BK table, built by a `while read` loop that passed SHA256SUMS's paths, 14 marker-named, in a variable to bash's builtin `printf` (no process exec'd with them), at each run". Add the corrections of items 76, 79, 80 and 82 too, and only then "Code knows of no others".
86. **T2:150–156**: the first checker's departures. **CONFIRMED.** All seven of its report's departures are there.
87. **T2:158–165**: placement, the commit-time count, "Not pushed", and Next. **NOT CHECKABLE.**

**T4, the first values-check raw**

88. **T4**: `62a6d626…43b0`, 331 lines. **CONFIRMED.** Lines 1–95 equal L/vc1_head.md byte for byte; the fences are at 96 and 331.
89. **T4:5–10**: what was checked. **CONFIRMED.** Draft 7 is `5cadc821…5908` (316 + 1058); the entry `4a49984b…be65` (111 lines, per L/vc_brief.md:24); the checks raw `16a1fb92…4fa7` (36 lines); HEAD `fd5d61c`.
90. **T4:12–13**: the brief, `5c22ca32…6ef4`, 136 lines, read whole. **CONFIRMED.**
91. **T4:14–16**: in Code's scratch, the brief named "the tools, the seven kept drafts and the generator's re-run". **IMPRECISE.**
    - L/vc_brief.md:48–52 also named T2's source, two notes of values, the fill script and the kit's library.
    - Instead: "…in Code's scratch, the tools (the fill script and the commit kit's library among them), T2's source and Code's two notes of values, the seven kept drafts and the generator's re-run;".
92. **T4:17–24**: the brief's allowances and bars. **CONFIRMED.** L/vc_brief.md:5–9, :78–92, :105–125.
93. **T4:25–26**: items 1–5 are byte-equal to the G-VER entry's brief's. **NOT CHECKABLE.** That brief is not among my sources; L/vc_brief.md:132–136 does equal L/vc2_brief.md:132–136 by `cmp`.
94. **T4:28–30**: the report extracted from the hand-back, 234 lines, `844739d2…0a08`. **CONFIRMED.** X holds one SubagentHandback call; its `input.message` (with jq's newline) equals L/vc_report.md byte for byte.
95. **T4:32–33**: the totals. **CONFIRMED.**
96. **T4:35**: the checker's departures are in the entry. **CONFIRMED.** T2:150–156.
97. **T4:39–41**: ""Draft 8" is the draft the second values-check reads". **FAIL.** This check reads draft 9. Instead: ""Draft 8" is the draft that applies them; draft 9, which carries them unchanged, is the draft the second values-check reads; "the entry" is the entry as revised."
98. **T4:43–44**: items 104, 106 and 116. **CONFIRMED** as stated.
99. **T4:45–50**: items 45, 50 and 74. **CONFIRMED.** T1:185–186, :192–193, :320–321.
100. **T4:51–60**: items 91, 94, 96, 97, 99, 101, 103 and 110. **CONFIRMED.** T2:34, :53–57 with :78–79, :60–67, :77, :81, :101–104, :123–129.
101. **T4:61–64**: items 21, 49 and 80 acted on, six left as stated. **CONFIRMED.** The six are items 2, 8, 30, 85, 87 and 117.
102. **T4:65–79**: observations 1–8. **CONFIRMED** as stated.
103. **T4:80–82**: observations 9–12 "applied in the entry's departures". **IMPRECISE.**
    - The made-twice statement is in T2's checks paragraph (:82–84); only the removal is in the departures (:125–126).
    - Instead: "Applied in the entry: the checks raw made twice (…) in its checks paragraph, its removal in the departures; and in the departures, the campaign folder's plain name in four of Code's command outputs, output only; the file tool's calls in scratch; and the steps before `fd5d61c`'s window."
104. **T4:89**: "v1.0 §4 hashes the raw and WORKFLOW.md". **IMPRECISE.** It also hashes rt22b. Instead: "v1.0 §4 hashes the raw, the PI's routing raw of that sitting and WORKFLOW.md;".
105. **T4:91**: "A second blind values-check reads draft 8". **FAIL.** Instead: "A second blind values-check reads draft 9 and the entry as revised:".
106. **T4:97–330**: the report. **CONFIRMED.** It equals L/vc_report.md and X's hand-back byte for byte.

## TOTALS

| Verdict | Count |
|---|---|
| CONFIRMED | 82 |
| IMPRECISE | 14 |
| FAIL | 5 |
| NOT CHECKABLE | 5 |

## OBSERVATIONS

1. **The generator's loop** (item 85) ran at every draft. The first check said "No loop, variable or glob passed a marker-named path", so it missed this too. A `sed -n 's/…/…/p' data/n/bk/SHA256SUMS` rebuild keeps the paths in a stream. The seat should class the runs.
2. **A gap after the commit.** Between step 13's commit and step 14's BUILD, the driver's G-TIME-n and G-VER commands refuse on this tree, because they check for v0.1's `LOCK_SHA256` (n_sessions.py:3913–3914, :5167–5168). v1.0 §12 could say so. A question for the seat: can any gate re-run fall in that interval?
3. **The status line's width.** The width check's blockquote exemption covers Code's status line (T1:366, 151 characters). v0.1's committed form wraps at L:3–4, and the seat sets those committed bytes.
4. **The order of reads.** ans22a:7 put G-VER's record read in "the sitting that reads v1.0's draft"; ans22b read it on its own. The seat may want to say its draft sitting need not re-read it.
5. **The fill script's version.** fill_entry.sh was edited at 04:27:15, after it filled T2 (04:26:54) and T4's head (04:24:55); it is now `9fec8f76…18fc`. No text records the version that made those fills.
6. **A stale comment.** make_check_raw.sh:4 says "at HEAD fd5d61c". The script checks `EXPECT_HEAD`, and its run of record was at `d714372`.
7. **For the final sweep.** After this brief's hash come the Agent launch (04:28:25), gate v14 (04:28:34, v13's kind), a scratch edit (04:29:25) and two memory-note edits (04:28:41, 04:29:27).
8. **An ambiguous quotation.** In T1:359, the seat's "against this raw" reads as the lock itself. Saying it means ans22b would avoid that.

## DEPARTURES

1. `cat` of T1 into `shasum`, once, by its own path. That is a tool beyond the four allowed on a file whose text holds a marker.
2. One unquoted `echo ==`. Zsh refused it ("= not found"), and the rest of that command line did not run.
3. `bc`, twice, to sum per-call counts. It is a calculator language, so an interpreter beyond `shasum` and `jq`. Both sums were 0.
4. One `> /dev/stdout` on a `jq` over T, piped to a `head -n 0` that failed. Nothing was written or printed.
5. Two environment assignments named with "awk" (`awk_free=1` before `cut`, `awk_never=0` before `sed`). No awk ran.
6. One `git diff --numstat fd5d61c d714372 -- RESULTS.md`. It printed 363 and 0, for RESULTS.md alone.
7. `shasum -c`'s output in data/n/bk/ (14 lines with a marker) was held in a variable and passed twice to zsh's builtin `printf`, each into `grep -c`. Only the counts printed, and no process was exec'd with the paths.
8. Prints from T possibly beyond need: the full text of the span's 35 Bash commands (local roots masked), so I could classify them, and the 04:28:34 command, printed while I located the span's end.

For the record, not counted: `[ … = … ]` tests with a lone `=`; searches of T1, T3, T4 and SHA256SUMS used patterns holding no marker word, and marker words were searched only bracketed. No file was written and nothing went over the network.
```
