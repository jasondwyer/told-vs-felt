# p's counters at VERDICTS: `task_correct` over every stage of the unit (R1 (c)); the proxy's contrast counts computed from the call logs (R2 (b)) (design → Code)

*Design seat, PI date 2026-11-16 (second sitting). On the dpo VERDICTS session's block `results/raw/2026-11-16_p-verdicts-counters_code-to-design.md` (`9464f61`), read in full, with its entry and the three close lines on `9189623`'s entry. Re-opened: the ruling of record the block cites, the seat's answers of 2026-11-09, §3 and §7 item 3 (`results/raw/2026-11-09_p-gtime_design-to-code_answers.md`), and the seat's answers of 2026-11-16, §3–§4 and §6 (`01ae2ae7…1b0f`, `18102d0`). Not opened: any checkpoint, call log, report or p output. `data/p/verdicts` was listed by name only: the three `_VERDICTS.json` and `_secondary.json` files exist beside the inputs, untracked, so the three runs have ended and the counters step is what stands between them and their entries. Section C answers the coordinating session's dated note on the push (`e5aba51`), owed since the last sitting. **Placed untracked over the bridge; Code commits by path on the PI's routing; the dpo VERDICTS session and the coordinating session add their close lines.** Calendar dates only; the commit hash is the record.*

## 0. The short form

- **R1: (c), every stage.** At the unit's VERDICTS, `task_correct` runs over every recorded round of every recorded session of the unit — G-TIME-OLMo (p)'s, G-F0m-OLMo (p)'s and the campaign's; sham and contrast; forced and free. The gate stages' sham rows are recounted and asserted against their committed figures, as Code built it; the campaign's sham row has no committed figure, and the step's is its first. Reported as k of n per stage, arm and phase, beside the bar; it decides nothing.
- **R2: (b), computed.** The reports withheld the proxy's contrast counts "to the unit's VERDICTS", which is a promise to report them there. The step reads each unit's three call logs by exact path, applies p's `attribute_calls` unchanged, and prints for the contrast arm the cells p's report gives the sham arm. Nothing per call, no text.
- Both change the script before its first read of a released record: `TC_STAGES`, and the call-log read with its checks. Reviewed, self-tested and committed; then the counters step runs once for the three units; then the outputs, the raws and the three entries, each open at "the reads".
- Ledger (76), the seat's, is §4. Section C rules on the push note. The routing block is §6.

## 1. R1 — why (c)

**1.1 The ruling of 2026-11-09 §3 has two clauses with two scopes.** The first names where the sham rows are reported: "over the sham sessions' rounds at every gate-stage entry (forced and free …)", because the sham reads files are released at those entries. The second names VERDICTS: "the contrast sessions' rounds at the unit's VERDICTS, where the free rounds are released". What is released at a unit's VERDICTS is the unit's records whole — the campaign's included, and the campaign is the unit: its 112 sessions carry the outcome the gate stages serve. "From G-F0m-OLMo (p) on" names the first entry that reports the counter, not the last stage it covers; the same paragraph records G-TIME's sham row "now as the first row", one stage earlier.

**1.2 The counter's stated use decides it.** The ruling gives the counter one reading for the paper: "task competence across the lineage's stages is not the confound the told control guards against". That is a sentence about the sessions the paper reports, which are the campaign's 112 per unit. A counter that stops at the 26 gate-stage sessions says nothing about them.

**1.3 Code's (a) read the reporting cadence as the domain.** That reading is the seat's wording's doing: the campaign's sham sessions fall under neither clause — not "a gate-stage entry" (so no row at `41bfab4`, rightly, since their rounds were not released there) and not "the contrast sessions". Ledger (76).

**1.4 What (c) means in the script.** `TC_STAGES = ("time", "qual", "campaign")`. Per unit: G-TIME's 1 sham and 1 contrast session; G-F0m's 16 and 8; the campaign's 32 and 80 — the 138 the seat's §6 names. The gate stages' sham rows are asserted against G-TIME's 3/4 + 6/6, 4/4 + 6/6, 4/4 + 6/6 and G-F0m's 63/64 + 96/96, 63/64 + 96/96, 64/64 + 96/96; the campaign's sham row is counted and printed with no assertion, pass 1's other checks on the campaign checkpoints standing as built (identity, the report's sha256 and p package, the read domain recomputed, the corrupted renders). The key table and the match rule are the committed raw's (`57e9c7dc…56e2`; the script `9aa0e2d9…4e0f`), unchanged. The (b) option, which would leave G-TIME's one contrast session out, has nothing to recommend it once the campaign is in.

## 2. R2 — why (b)

**2.1 Withheld is owed.** `CONTRAST_WITHHELD_QUAL` and `CONTRAST_WITHHELD` say, in the reports' own words, "withheld to the unit's VERDICTS or NOT-RUN record (m:318; the seat's ruling (h))". A withheld cell is a cell the record names and defers; the deferral ends at VERDICTS. Under (a) each VERDICTS entry would carry the cell as "not computed", and ADDENDUM-p1 would carry that hole into the posting's OLMo rows.

**2.2 "Each unit's three checkpoints" was the block's framing, not a boundary.** The seat's Q4 (b) answered a question put about the checkpoints; the clause that governs is "for the counts the record names and nothing beyond them". The proxy's contrast counts are named by the record. The call logs (`data/p/ckpt/OLMo-{ckpt}_{time,qual,campaign}_p-calls.jsonl`) sit beside the checkpoints under the same list-of-record binding, and reading them by exact path, for these counts, is the same act under the same rule. The coordinating session amends the three briefs' second sentence accordingly: "each unit's three checkpoints and three call logs".

**2.3 What the step does.** Nine call logs by exact path, never a listing; `stage.attribute_calls(sessions, events)` as p ships it; for each stage and the contrast arm, the cells p's report gives the sham arm (attributed of n, cuts), and per contrast session the number of its calls, which is its free-round exclusion position and is released at VERDICTS with the rest of the unit's records. The proxy's STOP message, where one exists, is quoted from the report, never from the log (the seat's ruling (c) of 2026-11-09). No call's text, index or timing is printed. A log whose sessions are not its checkpoint's, or an event p's function neither attributes nor counts as a cut, is a STOP (exit 4) with its line.

## 3. The order from here

1. The edit: `TC_STAGES`; the call-log read in pass 1 with §2.3's checks; the printing. The self-test extended: the campaign's sham row and the contrast rounds on synthetic records; the call logs on synthetic events through `attribute_calls`; the committed G-TIME and G-F0m sham figures still reproduced from the reads files.
2. One blind review round on the changed lines, with its mutants; a MAJOR comes to the seat.
3. Committed by path: the script, the self-test raw, the review raw, and a dated note on `9464f61`'s entry citing this raw.
4. The counters step for the three units, in one window: `nice -n 19 $PY -B scripts/p_verdicts_counters.py run --exit OLMo-sft=0 --exit OLMo-dpo=0 --exit OLMo-instruct=0`; its stdout committed as a raw. A STOP in pass 1 comes to the seat with its line and nothing else.
5. The outputs, the secondaries, the raws and the three entries committed by path, each entry open at "the reads" with the counters beside the analyzer's outputs (the seat's §5 step 5 of 2026-11-16).
6. The seat's reads (that raw's §6): one thread per unit, 138 sessions each, in the form of Q-F0's read; each closes its entry.

## 4. Ledger — design seat (76)

The ruling of 2026-11-09 §3 stated where each part of a counter is reported ("at every gate-stage entry"; "at the unit's VERDICTS") and let the reporting cadence stand in for the domain; the campaign's sham rounds fell under neither clause, and Code read the cadence as the domain. Fix: a counter's declaration states its domain — which sessions, which rounds — in one sentence, apart from where and when each part is reported.

## C. The coordinating session's note on the push (`e5aba51`), under the list of record v2's item 8

- **C.1 The first pass's halt, cleared by the session's own re-run: inert, no strike.** The matches were pod values inside longer tokens; the bounded pattern's re-runs over `16c99d5..97d160a` and `16c99d5..fa27c45` found none; nothing from inside a `ckpt` or `reports` file was printed. The form from here: a halt under item 4 is put to the seat with the re-run beside it, whatever the session takes its cause to be; the seat clears it, in a line.
- **C.2 The shape class printed for the three matches inside `data/mf3/reports`: inert, and item 4 is amended.** For a match inside, the screen may print the rule's name and a shape class (length and alphabet) beside the count by path class — never a value, a key, a path's content or a line.
- **C.3 The three gitleaks matches** are 64-character hexadecimal strings in report JSON, which the reports carry as sha256 digests by their own schema: false positives by class. The PI's "Push, with a note" stands as the push's word. From here the screen classifies a 64-hex token under a key whose name carries `sha` as a digest and reports it as a count; any other 64-hex match inside stays a halt.
- **C.4 The `data/mf3` hazard: the coordinating session's form is the standing rule while Q-F3's campaign runs.** The five paths (`m_analyze.py`'s battery; `p_analyze.py ganl` and `--selftest`; `mf3_sessions.py --selftest`; the regression suite's `check_adapter_consolidation`; `audit_note_N8.py`) run on the box, whose `data/mf3` holds committed files only, or after the campaign; never on the laptop meanwhile. The window rule for a p VERDICTS run — closed before each launch or resume, reopened on the F3 session's report that the PID is alive 30 minutes after it — stands as written.
- **C.5 The two later pushes.** The reflog records `fa27c45..645bd3f` and `645bd3f..bedc198` pushed today. The note's close line records each push's screen in one line (its range, the classes matched, the halts, the PI's word), so that the record of the pushes is complete.

## 6. Routing block for the PI (defaults in brackets; your words are the record)

**File placed untracked on the laptop:** this raw under `results/raw/` — sha256 and bytes in the paste block.

**B. p (the dpo VERDICTS session, for the three units)**
1. R1 (c): every stage; `TC_STAGES = ("time", "qual", "campaign")`; the gate stages' sham rows asserted, the campaign's counted and printed [as ruled].
2. R2 (b): the nine call logs by exact path; `attribute_calls` unchanged; the contrast arm's cells as the sham arm's; nothing per call [as ruled].
3. The script changed, self-tested, one blind review round, committed by path with a dated note on `9464f61`'s entry; then the counters step in one window; its raw [go].
4. Then the outputs, the secondaries, the raws and the three entries, each open at "the reads"; close lines on `9464f61`'s entry citing this raw; ledger (76) [as ruled].

**C. Coordinating session**
5. This raw committed by path; the three briefs amended for §2.2 ("three checkpoints and three call logs") [as ruled].
6. The push note: C.1 and C.2 inert, item 4 amended as C.2; C.3's digest rule; C.4 the standing rule; a close line on `e5aba51`'s entry citing this raw, with C.5's two lines [as ruled].
