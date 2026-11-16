# The blind values-check of the R1/R2 script commit's texts, with Code's dispositions (Code, the dpo VERDICTS session; PI date 2026-11-16)

*The coordinating session asked for one blind values-check pass before this commit, in the form the entries have had. Scope: the dated note on `9464f61`'s entry; the review raw's own text (its header, headings, dispositions, run record and runner's description), the review itself reproduced verbatim and kept as returned; and the self-test raw's header. The checker was a fresh subagent with no part in the drafting. Its brief quoted the list of record v2, items 1–5 (item 4 with C.2's amendment of 2026-11-16, second sitting) and the rules of Q-F3's campaign on this laptop, and allowed no interpreter. It opened nothing under `data/p/ckpt`, `data/p/verdicts` or `data/mf3`; from `data/p/reports` it read only the nine p reports' `call_log` and `proxy` fields. Its report is reproduced verbatim (sha256 `74fa4e97e91ee8761c646a251a02b00d4d1177c63ee0d727cf9ff0c73afdc031`); Code's dispositions follow. The edits after it were checked by tool, not by a second blind pass. Calendar dates only; the commit hash is the record.*

## The report, verbatim

# Blind values-check: the dated note on `9464f61`'s entry, the r1r2 review raw and the r1r2 self-test raw (p's counters at VERDICTS; the checker's report, PI date 2026-11-16)

**Result:** 133 claims: 114 CONFIRMED / 6 IMPRECISE / 1 FAIL / 12 NOT CHECKABLE. All six reproductions are verbatim (`cmp`-identical), and every sha256 in Code's text equals its file's, checked by tool.

Sources: HEAD `a61f13d`. RESULTS.md: the entry at :629–727 and the coordinating session's close at :1080–1114 (committed at `52b2c97`). The seat's raw: sha256 `aea918c5…0395` by `shasum`, blob equal to HEAD's. `scripts/p_verdicts_counters.py` in the working tree: sha256 `a87749e9…d6f6`, compared against HEAD's blob `e641f812` (`8e7fbed3…6905`). p's `stage.py` and `proxy.py`. The scratch files named in the brief. Script line numbers are the working tree's. SCR is the brief's scratch directory.

## Text 1: `SCR/note_9464f61_final.md`

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | 1 | "PI date 2026-11-16" | C | The routing the note applies is dated "PI date 2026-11-16, second sitting" (RESULTS.md:1080, :1085). |
| 2 | 1 | the script changed for the seat's answer on R1 and R2 | C | `git diff`: `TC_STAGES` (HEAD :117 `("time", "qual")`, now :139) and the call-log read in pass 1 (:495–528). |
| 3 | 1–2 | "the dpo VERDICTS session" | C | Section B is "relayed verbatim to the dpo VERDICTS session, which does the counters for the three units" (RESULTS.md:1108–1109). The entry is that session's (:632). |
| 4 | 2 | "the seat's raw §3 item 3" | C | §3 item 3: "Committed by path: the script, the self-test raw, the review raw, and a dated note on `9464f61`'s entry citing this raw." |
| 5 | 2 | the PI's routing, "Route as given", section B | C | "Route as given", verbatim, at RESULTS.md:1085. "the paste block's section B (the raw's §6 block B)" at :1108. |
| 6 | 2 | "items 1–3" (of section B) | NC | The paste block is not in the repo. The raw's §6 block B items 1–3 are R1 (c), R2 (b) and the change with this note, so the content matches. The block's numbering is not the raw's everywhere (NOTE 6). |
| 7 | 3 | the answer is `results/raw/2026-11-16_p-verdicts-counters_design-to-code_answers.md` | C | The file is tracked at that path. It answers R1 and R2 (§0–§2). |
| 8 | 4 | sha256 `aea918c5…0395` (in full) | C | Equal by tool to `shasum -a 256` of the file. `git hash-object` equals `HEAD:` (`153f1df5…`). |
| 9 | 4–5 | the coordinating session committed it by path at `52b2c97` | C | `git show --name-status 52b2c97` shows `A` for the raw. The coordinating session's close says "are committed by path here" (RESULTS.md:1080–1084). |
| 10 | 5–6 | "Committed with this note: the script as changed, its self-test raw and its review raw." | NC | This is a future commit. It matches §3 item 3's list. |
| 11 | 7 | `TC_STAGES` is now `("time", "qual", "campaign")` | C | :139. HEAD :117 had `("time", "qual")`. |
| 12 | 7–8 | the gate stages' sham rows are still asserted against their committed figures | C | :529–533 (`if s in committed_tc`). `COMMITTED_SHAM_TC` holds qual and time (:160–167). HEAD asserted them too. |
| 13 | 8 | the campaign's sham row is counted and printed with no assertion | C | :529–534 count it for every stage in `TC_STAGES`. :608–609 print "no committed figure: this is its first, not asserted". |
| 14 | 9–10 | each stage's call log is read by exact path, through p's `read_calls`, `log_consistency_problems` and `attribute_calls`, unchanged | C | `CALLS_REL` (:143) is p's own path (stage.py:673). p's functions are called directly at :504, :512 and :379. The only wrapper is one self-test case (:1223–1242), and it restores the function. |
| 15 | 10–11 | for each arm, the cells p's report gives the sham arm | C | `proxy_cells` (:389–395) gives `n_rounds`, `n_attributed`, `n_cuts`, `cut_keys` and `unattributed_keys` per arm: build_report's `proxy.sham` (stage.py:998–1001). |
| 16 | 11 | "and the calls per contrast session; nothing per call" | C | :396–402. `emit` (:591–604) prints counts and round keys only. The self-test asserts that no call's number, seed, digest or returned text prints (:989–998). |
| 17 | 12 | the sham arm's cells are asserted equal to the committed report's | C | :523–524, with `committed_proxy` at :415–418. |
| 18 | 13 | "A STOP, with its line and never a log line's position" | C | A `Stop` prints its line to stderr and exits 4 (:1304–1306). The call-log STOP messages carry paths, counts, keys and session indices (:380–401, :498–526). See NOTE 2. |
| 19 | 14 | "a log its report does not record by sha256 and path" | C | :501–503. |
| 20 | 15 | "a log of another stage, or one run by a p package its report does not name" | C | :512–514 (`gate=s`) and :515–519. |
| 21 | 16 | "malformed lines the report does not record" | C | :509–511 (`well_formed`, `n_malformed_lines`). |
| 22 | 17 | "a call attributed to no round" | C | :383–384. |
| 23 | 18 | "a call matching a round already attributed" | C | :385–387. |
| 24 | 13–18 | the five items as the STOPs on a call log | I | The list reads as the whole set, but the script has six more: an absent or unreadable log (:498–499, :505–506); bytes that change while read (:507–508); a run count the report records otherwise (:520–521); the attribution flag (:525–526); p's `attribute_calls` problems (:380–381); and a contrast session index that is not an int, or occurs twice (:400–401). **Fix 1** below. |
| 25 | 19 | the script's sha256 `a87749e9…d6f6` (in full) | C | Equal by tool to `shasum` of the working-tree file. |
| 26 | 20 | "Self-test: 44/44, exit 0, the run of record" | C | `SCR/selftest_r2_2.stdout` has 44 `[PASS]`, 0 `[FAIL]` and "44/44 selftest checks pass". The source has 44 `chk` calls. Exit 0 is inferred (NOTE 7). |
| 27 | 20–21 | "the change before its review passed 43/43" | C | `SCR/selftest_r2_1.stdout` has 43 `[PASS]`, 0 `[FAIL]` and "43/43". |
| 28 | 21 | link to `results/raw/2026-11-16_p-verdicts-counters-r1r2_selftest.txt` | NC | The file is not yet in `results/raw` (NOTE 1). |
| 29 | 22 | "One blind review round (the raw's §3 item 2)" | C | §3 item 2: "One blind review round on the changed lines, with its mutants; a MAJOR comes to the seat." |
| 30 | 22 | "no MAJOR, 4 MINOR and 6 NOTE" | C | The review: "MAJOR 0 / MINOR 4 / NOTE 6". Findings 1–4 are MINOR and 5–10 are NOTE. |
| 31 | 22–23 | "each applied but one NOTE answered with no change" | C | Dispositions 1–5 and 7–10 are applied, each checked in the source (Text 2, rows 32–66). Disposition 6 is "no change". |
| 32 | 24 | the 16 mutants each ran once through the self-test on the script as committed | C | `result_r2.txt` line 1 reads "script sha256 a87749e9…; 16 mutant(s)", equal by tool to the working tree. The runner runs each mutant once. |
| 33 | 24–25 | "all killed, the baseline passing" | C | "summary: 16 killed, 0 survived, 0 invalid, baseline PASS". |
| 34 | 25 | link to `results/raw/2026-11-16_p-verdicts-counters-r1r2_review.md` | NC | The file is not yet in `results/raw` (NOTE 1). |
| 35 | 26–27 | Code's reading, declared in the docstring: a contrast round with no attributed call is printed, not stopped, as the sham arm's cells print one | C | Docstring :60–62 ("CODE'S READING, for the seat: …"). The self-test asserts it (:1259–1266). |
| 36 | 28 | "(the raw's §3 items 4–6)" | F | Items 4 and 5 are the counters step and the entries. Item 6 is the seat's reads ("one thread per unit, 138 sessions each, … each closes its entry"), which the bullet does not describe. The close line with ledger (76) comes from §6 block B item 4. **Fix 2** below. |
| 37 | 28–29 | the counters step for the three units, in one window, its stdout committed as a raw | C | §3 item 4. |
| 38 | 29–30 | then each unit's outputs and entries, each open at "the reads" | C | §3 item 5 ("each entry open at "the reads""). |
| 39 | 30 | "this session's close line, with ledger (76), at dpo's entries" | I | The record puts this close line on `9464f61`'s entry. §6 block B item 4: "close lines on `9464f61`'s entry citing this raw; ledger (76)". The coordinating session's close: "the dpo session adds its close line on `9464f61`'s entry, with ledger (76)" (RESULTS.md:1113–1114). "dpo's entries" names other entries, or none exactly. **Fix 2** below. |

**Fix 1** (replaces note lines 13–18):

```
      - A STOP, with its line and never a log line's position:
        - a log its report does not record by sha256 and path, an absent or unreadable log, or one whose bytes
          change while it is read;
        - a log of another stage, or one run by a p package its report does not name;
        - malformed lines the report does not record, or a run count or attribution flag it records otherwise;
        - a call attributed to no round;
        - a call matching a round already attributed;
        - a problem p's `attribute_calls` reports (two rounds sharing a seed, a round with no int seed), or a
          contrast session index not an int, or twice.
```

**Fix 2** (replaces note lines 28–30):

```
    - **Next** (the raw's §3 items 4–5 and §6 block B item 4): the counters step for the three units, in one window,
      its stdout committed as a raw; then each unit's outputs and entries, each open at "the reads"; and this
      session's close line on `9464f61`'s entry, citing the raw, with ledger (76).
```

## Text 2: `SCR/raw_r2_review.md` (Code's text only)

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | 1 | title: the blind review round of the script as changed for R1 (c) and R2 (b), its mutants, and Code's dispositions | C | §1–§5 hold exactly these. |
| 2 | 1 | "(Code, the dpo VERDICTS session; PI date 2026-11-16)" | C | As Text 1, rows 1 and 3. |
| 3 | 3 | the seat's raw, at that path, committed at `52b2c97` | C | `git show --name-status 52b2c97`. |
| 4 | 3 | §3 item 2, verbatim: "One blind review round on the changed lines, with its mutants; a MAJOR comes to the seat." | C | `/usr/bin/grep -c -F` on the raw finds 1 match, at §3 item 2, character for character. |
| 5 | 5 | the reviewer was a fresh subagent with no part in the change | NC | No file records the session's agents. |
| 6 | 5 | it read the change against HEAD, the seat's raw, the rulings that raw cites, and p's call-log functions | C | The review's header says "against HEAD's blob e641f812 (HEAD 52b2c97)". Its citations include §2.3, §1.4, "ruling (c) of 2026-11-09" and stage.py. It also cites m's code (NOTE 3). |
| 7 | 5 | "It ran no Python." | C | The review's closing paragraph: "I ran no Python." |
| 8 | 5 | its brief bound it to the list of record v2, items 1–5, and to Q-F3's rules, both quoted | NC | The brief is not among the sources. |
| 9 | 5 | it opened nothing under `data/p/ckpt`, `data/p/verdicts`, `data/p/reports` or `data/mf3` | C | The review's own statement: "I opened, listed and searched nothing under …". |
| 10 | 5 | it reviewed the script at sha256 `f148bf3f…9996` | C | String-equal by tool to the review's header. |
| 11 | 5 | it wrote 16 mutants | C | `jq length` of `SCR/mutants/mutants_r2.json` gives 16 (M01–M16). |
| 12 | 5 | "It found no MAJOR." | C | "MAJOR 0". |
| 13 | 7 | "Code applied each finding." | I | Disposition 6 is "no change", and the note says "each applied but one NOTE answered with no change". Replace with: "Code applied each finding but one: finding 6, a NOTE, is answered with no change, as its fix proposes." |
| 14 | 7 | the script as committed is sha256 `a87749e9…d6f6` | C | Equal by tool to the working tree. |
| 15 | 7 | the mutants ran on it, each once through the self-test | C | `result_r2.txt` line 1 names that sha256. The runner (§5) runs each mutant once. |
| 16 | 7 | "in a battery window the coordinating session granted" | NC | A session act. No file records it. |
| 17 | 7 | "16 of 16 killed, baseline PASS" | C | The summary line of `result_r2.txt`. |
| 18 | 9 | the sections, in order: the review, the dispositions, the mutants, the run's output, the runner | C | Headings at :11, :203, :252, :371 and :395. |
| 19 | 9 | each reproduction verbatim, "the local root shown as `<repo>`" | C | `cmp` is identical after the substitution (Verbatim checks). The runner holds the only occurrence of the root (1). |
| 20 | 9 | "Calendar dates only" | C | Code's text has no time of day. |
| 21 | 11 | §1: the review, verbatim, sha256 `8415b249…a055` | C | Equal by tool to `SCR/review_r2_report.md`; `cmp` identical. |
| 22 | 203 | §2: "Code's dispositions" | C | Holds the ten dispositions and the run. |
| 23 | 252 | §3: `mutants_r2.json`, verbatim, sha256 `fc31a0ab…98b1` | C | Equal by tool; `cmp` identical. |
| 24 | 371 | §4: `result_r2.txt`, verbatim, sha256 `fbe975ac…2201` | C | Equal by tool; `cmp` identical. The runner's stdout file (`SCR/mutants/run_r2.stdout`) is `cmp`-identical to it. |
| 25 | 371 | "the runner's exit 0" | C | Inferred (NOTE 7): the runner returns 0 only when the baseline passed with 0 survived and 0 invalid, as the summary records. |
| 26 | 371 | "stderr empty" | C | `SCR/mutants/run_r2.stderr` is empty. |
| 27 | 395 | §5: `run_mutants.py`, verbatim, sha256 `6c69daa7…f9b9` "before the root was shown as `<repo>`" | C | Equal by tool on the unsubstituted file; `cmp` identical after the substitution. |
| 28 | 205 | "The review found no MAJOR." | C | "MAJOR 0". |
| 29 | 205 | "Each MINOR and each NOTE is applied as follows." | I | Item 6 is "no change". Replace with: "Each MINOR and each NOTE is disposed of as follows: each applied but finding 6, answered with no change." |
| 30 | 205 | "Line numbers are the reviewed version's." | C | The review's header names the reviewed bytes (`f148bf3f…9996`). §2 itself cites no line numbers (NOTE 4). |
| 31 | 207–240 | the ten dispositions' labels and titles (1–4 MINOR, 5–10 NOTE) | C | Each matches the review's finding of the same number. |
| 32 | 207 | finding 1: "applied as given" | I | The check's two lines are the review's (:502–503). But the review put the check "right after the changed-while-read check (line 494)", and the script puts it before `read_calls` (:500–504), as the next bullet says. Replace "applied as given." with: "applied, the check as given, placed before `read_calls` (the review placed it after the changed-while-read check)." |
| 33 | 208 | pass 1 checks `call_log.sha256` and `call_log.path` against the log's bytes and p's path form | C | :501–503. p's form is `ckpt/{U}_{gate}_p-calls.jsonl` (stage.py:673, :980, :988). |
| 34 | 208 | "right after reading those bytes and before `read_calls`" | C | The bytes are read at :500, checked at :501–503, and `read_calls` runs at :504. |
| 35 | 210 | each synthetic report records the path and the sha256 | C | :797. |
| 36 | 211 | `edit_log` and `append_line` re-record an edited log's sha256 | C | :1122–1133. `edit_log` skips it only when `record=False`. |
| 37 | 212 | a new case, "an unrecorded log", STOPs with "does not record" | C | :1142–1143; the expected text is at :1192. |
| 38 | 213 | the reading is declared in the docstring as Code's reading | C | :60–62. |
| 39 | 213 | "The printed case's check names it so." | C | :1259: "printed, not stopped (Code's reading of the sham cells' form)". |
| 40 | 215 | `stops_silently` returns the STOP's message | C | :1066 returns "stop: " followed by the message. |
| 41 | 215 | "each case asserts its own text: the reviewer's table, made exact, with the five earlier cases given theirs too" | I | The five earlier cases have texts (:1106–1110). Nine of the table's ten rows are kept or lengthened (:1192–1206). The malformed row is not: the review's "not JSON" is replaced by finding 4's message (:1197), and its absence is asserted from every message (:1221). Replace "the reviewer's table, made exact," with: "the reviewer's table, made exact (its malformed row now finding 4's message, "not JSON" asserted absent from every message)," |
| 42 | 217 | new case: "a round with no int seed, its call removed" | C | `seed_none`, :1179–1181. |
| 43 | 218 | new case: "a contrast session index `"1"`" | C | `index_not_int`, :1183–1184; expected text at :1205. |
| 44 | 219 | new case: "a contrast session twice" | C | `session_twice`, :1186–1190; expected text at :1206. |
| 45 | 220 | new case: a log whose bytes change while `read_calls` reads it, p's function wrapped and restored in a `finally` | C | :1223–1246. |
| 46 | 222 | the run, call and end lines are in p's form: `"call": n`, and cut events with `returned_text` carrying `SENTINEL` and `stored_text` the round's text | C | :757–771 match stage.py:1347–1351 and :1399–1405, and proxy.py:87–88 and :138. |
| 47 | 223 | the proxy check asserts that `SENTINEL` and `"call"` never print | C | :997 (and "seed"). |
| 48 | 224 | a STOP call line in proxy.py's form (seed 999, `"stop"` carrying `SENTINEL`) STOPs as an orphan, with no `SENTINEL` in its message | C | :1139–1140 and :1148–1149, expected texts at :1194 and :1221. proxy.py:131–132. |
| 49 | 225 | finding 4: "applied, the reviewer's second option" | C | :509 is the second option's condition, verbatim. The message differs only in wording. |
| 50 | 226 | a STOP fires only when the count or `well_formed` differs from what the report records | C | :509–511. |
| 51 | 227 | "The count is printed." | C | :594. |
| 52 | 227 | "Every one of the nine reports records 0 at this writing" | C | `jq .call_log.n_malformed_lines` on the nine reports gives 0 for each. |
| 53 | 227 | "Code read their `call_log` fields with `jq`" | NC | A session act. |
| 54 | 228 | "The STOP message prints counts, never a line's position." | C | :510–511. |
| 55 | 228 | "This also covers finding 10." | C | No message prints `read_calls`' positioned problems (:505–511), and "not JSON" is asserted absent (:1221). |
| 56 | 230 | the line reads "STOP marks in the p report's run rows" | C | :595–596. |
| 57 | 231 | the docstring says that a STOP's message, where one exists, is the stage entry's verbatim quote | C | :58–59. |
| 58 | 232 | finding 6: "no change" | C | The re-run and orphan STOPs stand (:383–387). The finding's own fix says "No code change". |
| 59 | 233 | each of the nine reports records `call_log.n_runs` 1, no STOP mark, `well_formed` true and 0 malformed lines | C | `jq` on the nine: `n_runs` 1, one run row with `stop` false, `well_formed` true and `n_malformed_lines` 0, in every report. |
| 60 | 234 | "Code read only those fields, with `jq`." | NC | A session act. |
| 61 | 236 | `load_ruling(raw=None)`, with a refusal case (the raw plus a newline) | C | :617 and :849–854. |
| 62 | 237 | gate 4 now requires the ruling raw, as well as the script, to be committed at HEAD | C | :445–456 and :641–643. |
| 63 | 237 | "The raw was committed by path at `52b2c97`." | C | As row 3. |
| 64 | 238 | "A run ending at the last index is now tested." | C | :1012. |
| 65 | 239 | the check now reads "against the hand-computed sham cells (build_report's rule)" | C | :1001, a verbatim substring. |
| 66 | 240 | finding 10 "applied with 4" | C | As row 55. |
| 67 | 243 | each `old` text re-counted with `/usr/bin/grep -o -F` | NC | A session act. |
| 68 | 243 | "Each occurs exactly once, so none needed re-anchoring." | C | Re-counted here with `/usr/bin/grep -o -F` against the working-tree script: once each, 16 of 16. The runner's own count found 0 invalid. |
| 69 | 244 | run by `<scratchpad>/mutants/run_mutants.py` (below) | C | The file exists, and its sha256 is the one §5 names. |
| 70 | 244 | each mutant runs once, as a fresh module whose `__file__` is the script's path | C | The runner uses `types.ModuleType`, sets `mod.__file__ = str(REAL)`, and calls `run_one` once per mutant. |
| 71 | 244 | "The script file is never written." | C | The runner only reads `REAL`; the one file it writes is `OUT`. |
| 72 | 245 | "A baseline runs first and must pass." | C | The runner's `main`. |
| 73 | 248 | "Baseline PASS; 16 killed, 0 survived, 0 invalid." | C | `result_r2.txt`. |
| 74 | 248 | M07, M09 and M13 are killed by the fixes for findings 2 and 8 | C | M07 and M09 fail the call-log STOP check on its messages (finding 2). M13 fails the `calls_by_count` check (finding 8). |
| 75 | 249 | under M11 and M12 the proxy check fails cleanly | C | Each run prints the proxy check's FAIL line. |
| 76 | 249 | the `proxy_cells` check cannot render its GOT value (tuple keys), so a TypeError is raised, which the wrapper records as the FAIL "the self-test ran to its end without raising" | C | `chk` renders GOT with `json.dumps` (:811), and `per_session` is keyed by tuples (:396). The wrapper is :814–817. The M11 and M12 result lines read "TypeError: keys must be str, int, float, bool or None, not tuple". |
| 77 | 250 | "The mutant is killed either way." | C | Both runs return rc 1. |
| 78 | 250 | the rendering matters only on a failing self-test, which closes gate 5 before any record is read | C | Gate 5 (:653–658) comes before `collect_guarded` (:669). |

## Text 3: `SCR/raw_r2_selftest.txt` (header and headings)

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | 1 | title: the self-test of the script as changed for R1 (c) and R2 (b) | C | The file holds the two runs. |
| 2 | 1 | "(Code, the dpo VERDICTS session; PI date 2026-11-16)" | C | As Text 1, rows 1 and 3. |
| 3 | 3 | the command, run from the repository root at `nice -n 19` | NC | A session act. The interpreter path exists (`ls`), and the form is the docstring's usage line (:98–99). |
| 4 | 3 | "each run in a battery window the coordinating session granted" | NC | A session act. |
| 5 | 3 | run 2 is the run of record, on the script as committed (sha256 `a87749e9…d6f6`) | C | The hash is the working tree's, by tool. All 24 fixed check names in run 2's stdout appear in this source (`grep -F`). The 20 interpolated names match :826–889. The source has 44 `chk` calls. Nothing else records which bytes ran. |
| 6 | 3 | "44/44" | C | 44 `[PASS]`, 0 `[FAIL]`. |
| 7 | 3 | run 2: "exit 0" | C | Inferred (NOTE 7). |
| 8 | 3 | run 2: "stderr empty" | C | `SCR/selftest_r2_2.stderr` is empty. |
| 9 | 3 | run 1 was on the change before its review (sha256 `f148bf3f…9996`, "the version the review names") | C | String-equal by tool to the review's header. Consistent with the review's line "The self-test's printed check names match this source, 43/43". |
| 10 | 3 | run 1: "43/43, exit 0, stderr empty" | C | 43 `[PASS]`, 0 `[FAIL]`. `SCR/selftest_r2_1.stderr` is empty. Exit 0 is inferred (NOTE 7). |
| 11 | 3 | "The self-test reads no checkpoint, call log or p output" | C | `_selftest_body` (:823–1270) reads the task_correct raw, the pools, the lexicon, the ruling raw, the six qual and time reads files and p reports, its own source, and a temporary root. "p output" is meant in the docstring's sense (:64–68); see NOTE 5. |
| 12 | 3 | "its call logs are synthetic, in a temporary directory outside the repository" | C | `tempfile.TemporaryDirectory` (:948) and `_synthetic_root` (:966, :779–803). |
| 13 | 3 | "Each run's stdout is reproduced verbatim." | C | Both are `cmp`-identical (Verbatim checks). |
| 14 | 3 | "Calendar dates only" | C | No time of day. |
| 15 | 5 | run 2 stdout sha256 `58062a64…7591` | C | Equal by tool. |
| 16 | 56 | run 1 stdout sha256 `4a551675…65fd` | C | Equal by tool. |

## Verbatim checks of the reproductions

Method: each raw line range was extracted with `sed -n` and compared with `cmp` against its source after `sed` replaced the repository root with `<repo>` and SCR with `<scratchpad>`. The sources contain no SCR path. Only `run_mutants.py` contains the repository root, once.

| Reproduction | Raw lines | Source (lines) | Result |
|---|---|---|---|
| §1, the review | `raw_r2_review.md`:13–201 (189) | `SCR/review_r2_report.md` (189) | identical |
| §3, the mutants | `raw_r2_review.md`:255–368 (114) | `SCR/mutants/mutants_r2.json` (114) | identical |
| §4, the run | `raw_r2_review.md`:374–392 (19) | `SCR/mutants/result_r2.txt` (19) | identical |
| §5, the runner | `raw_r2_review.md`:398–467 (70) | `SCR/mutants/run_mutants.py` (70), root substituted | identical |
| run 2 | `raw_r2_selftest.txt`:8–53 (46) | `SCR/selftest_r2_2.stdout` (46) | identical |
| run 1 | `raw_r2_selftest.txt`:59–103 (45) | `SCR/selftest_r2_1.stdout` (45) | identical |

Each block's fences sit on the lines around it: :254/:369, :373/:393 and :397/:468 in the review raw, and :7/:54 and :58/:104 in the self-test raw. All nine sha256s in the two raws' Code text, and the two in the note, were compared with `shasum` output by tool. All are equal.

## NOTES

1. **The two raw links.** The note links `results/raw/2026-11-16_p-verdicts-counters-r1r2_selftest.txt` and `results/raw/2026-11-16_p-verdicts-counters-r1r2_review.md`. Neither is in `results/raw` yet; the scratch raws are `raw_r2_selftest.txt` and `raw_r2_review.md`. Place them under exactly those names, or change the links. The link texts follow the entry's own `_…` form (RESULTS.md:671, :682).
2. **"never a log line's position".** The "is not this stage's" STOP (:514) prints up to three of `log_consistency_problems`' messages. These name a run line by its ordinal among the run lines: "run line 1: not this stage's (…)" (stage.py:868); M06's line in §4 shows one. That ordinal is not a line number in the file, so the claim holds as written. It is noted so the seat can read it the same way. No change proposed.
3. **What the reviewer read (review raw line 5).** The review also cites m's code (`runner_olmo.py`, `verify.py`, `stages.py` and `readrule.py`, all under `valence_core/m`) and p's `proxy.py`. Optional addition: "…, and p's call-log functions, with the p and m code they rest on."
4. **Review raw lines 205 and 9.** "Line numbers are the reviewed version's" governs §1's line numbers; §2 cites none. Optional rewording: "The review's line numbers are the reviewed version's." The reviewed bytes (`f148bf3f…9996`, blob `68f76049`) are not in the object store, and neither scratch copy of the script I digested is that version. So claims about them rest on the review's header. Line 9 defines `<repo>` but not `<scratchpad>`, which §2 uses at line 244. Optional addition to line 9: "and the session's scratch directory as `<scratchpad>`".
5. **Self-test raw line 3.** "reads no checkpoint, call log or p output" is true in the docstring's sense, where "p output" means the VERDICTS and NOT-RUN outputs. The self-test does read the six qual and time reads files and p reports under `data/p/reports` (the read domain), as its docstring lists (:65–68). Optional clarity.
6. **"section B, items 1–3"** (note line 2; the script's docstring :15–16). This is checked against the raw's §6 block B, which the coordinating session's close identifies with the paste block's section B (RESULTS.md:1108). The paste block numbers at least one item differently from the raw: its item 11 is the raw's §6 item 6 (RESULTS.md:1085–1087). The session that received section B verbatim can confirm its numbers.
7. **Exit statuses.** No exit-status file exists in SCR for the two self-test runs or the mutant run, so "exit 0" is confirmed by inference. `main` returns `run_selftest()`, which returns 0 only when every check passes (:806–820, :1295–1296). The runner returns 0 only when the baseline passed with 0 survived and 0 invalid (§5, `main`). The stdout files record both outcomes.
8. **The reproduced review's headings.** The review keeps its own `#` title and its `## 1.`–`## 10.`, `## Checked, no finding` and `## Mutants` headings. These sit at the level of the raw's own `## 1.`–`## 5.`, so there are two `## 1.` headings. No edit to the review is proposed; Code's header could say that the review's headings follow inside §1. The review's title, "Blind review r2", may also read as "round 2" beside the note's "One blind review round".
9. **Code's reading.** The reading (note lines 26–27; review raw §2 item 1) is implemented in the run path and asserted by the self-test. The note also lists the counters step as next. Neither text says whether the step waits for the seat's word on the reading. Flagged only; that is not mine to adjudicate.

**What I did not open or run.** I ran no Python, node, perl or ruby. I opened, listed, searched and digested nothing under `data/p/ckpt`, `data/p/verdicts` or `data/mf3`. From `data/p/reports` I read only the nine p reports' `call_log` and `proxy` fields, with `jq`: `n_runs`, the run rows' `stop`, `well_formed` and `n_malformed_lines`. I also read `proxy.attribution_complete` and the count of `proxy.sham.unattributed_keys`, which I do not report. I ran no whole-tree `git status` (one, scoped to five paths). My content searches were `/usr/bin/grep` and `sed` on named files only. In the scratch directory I read the named files, listed the other names with a name-only `ls`, and digested two scratch copies of the script (hashes only). I compared the runner's stdout file by `cmp` and tested the stderr files for emptiness. I ran `git cat-file -t` on the reviewed blob id, which is absent. I wrote only `SCR/vc_r2_report.md`.

## Code's dispositions

The FAIL and each IMPRECISE are applied in the checker's terms. Line numbers are the checked versions'.

**The dated note**
- **#36 (FAIL) and #39:** applied as the checker's Fix 2. The "Next" bullet now cites the raw's §3 items 4–5 and §6 block B item 4, and puts this session's close line on `9464f61`'s entry, citing the raw, with ledger (76).
- **#24:** applied as Fix 1. The STOP list is now the script's whole set.
- **NOT CHECKABLE items** (#6, #10, #28, #34): #28 and #34 resolve at this commit, which places the two raws under exactly the linked names (NOTE 1). #10 is this commit's own list. #6 is NOTE 6.

**The review raw**
- **#13:** applied in the checker's words.
- **#29:** applied in the checker's words.
- **#32:** applied in the checker's words.
- **#41:** applied in the checker's words.

**NOTES**
1. **No change:** the raws are placed under exactly the linked names.
2. **No change:** the checker reads the claim as written. "Run line 1" is an ordinal among the run lines, not a position in the file.
3. **Applied:** "with the p and m code they rest on".
4. **Applied:**
   - "The review's line numbers are the reviewed version's."
   - The header now defines `<scratchpad>`.
5. **Applied:** the self-test raw's header now names the read-domain files the self-test reads.
6. **No change.** The coordinating session relayed section B to this session verbatim, with items 1–4:
   - 1 is R1 (c);
   - 2 is R2 (b);
   - 3 is the script changed, self-tested, reviewed and committed with the dated note, then the counters step;
   - 4 is the outputs, the entries and the close lines.

   The note's "items 1–3" are that relay's numbers.
7. **No change.** The exit statuses were printed by the commands that ran each process, in this session's tool output. No exit file was kept.
8. **Applied.** The review raw's header now says two things:
   - the review keeps its own headings, which follow inside §1;
   - its title's "r2" names this phase's files, not a second round.
9. **Applied, in part.** The note now says that the reading bears only where a contrast round has no call, and that the step's output would show any such round.
   - The counters step's go is the routing's section B item 3 ("then the counters step in one window; its raw [go]").
   - Code's reading does not hold the step. Whether the seat's word on it is wanted first is the coordinating session's and the seat's to say.

**The edits after the check, checked by tool**
- Each fix's text was confirmed present, and each replaced phrase absent, in the note and the rebuilt raws: 17 `/usr/bin/grep -F` checks, all PASS.
- The rebuilt review raw's four reproductions were compared by `cmp` with their sources (the runner with its root as `<repo>`), and §2 with the dispositions file. All are equal.
- The builder asserts each source's sha256 before it builds.
- No second blind pass was run.
