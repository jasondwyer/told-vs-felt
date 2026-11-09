# The A-m2 smoke — the values-check of Code's read and its entry

*Code's raw, PI date 2026-11-09.*
- *What was checked:* the drafts of Code's read (D1, committed as `2026-11-09_a-m2-smoke_code-read.md`) and of its
  RESULTS.md entry (D2), against the raw, the thirteen JSONs, A-m2 v0.3 and the repository.
- *How:* a blind agent, read-only.
  - It recomputed every reasoning line's class from each record's pieces, independently of the driver's classes. The
    result equals the driver's on all 67 lines.
  - It read all 115 task responses for counter (b) on its own.
- *The report:* the agent could not write its report file, because its tool refuses report files from a subagent. It
  returned the report as its hand-back, and Code extracted that text from the agent's transcript by script, byte for
  byte. It is below, verbatim, with one change: the session id's prefix, which the report quotes twice as a string it
  searched for, is shown as `<id>`. The report holds no local path.
- *Result:* 103 items: 78 PASS, 12 IMPRECISE, 0 FAIL, 13 NOT CHECKABLE.
  - Counter (b): no disagreement. The agent read the same 2 of 115 responses as (b), and all eight of the read's
    considered responses as not (b).
  - The NOT CHECKABLE items are Code's own conduct, events in chat, the drafts' placeholders, and acts still to come.
- *Nothing ran on a model.* Nothing under `data/m/ckpt`, `data/mf3/ckpt`, `data/mf3/reports` or `data/p/ckpt` was
  opened.

## Code's dispositions

Every IMPRECISE item was applied, all as wording. No value changed. Each new fact the fixes state is asserted against
the JSONs in the script that rebuilds the read.

| item | finding | disposition |
|---|---|---|
| 13 (D1), 80 (D2) | "The post-load check" names no check, and several checks follow the load. | Applied. Both now name the snapshot re-read, m:267's laptop checklist (the GATE line), the licence and the A-m2 check. |
| 24 (D1) | "Its output, verbatim" shows lines 2–8 of 214. | Applied. The block holds the first eight lines, the FILES line included. The text says the per-session listing follows in the full output. |
| 35 (D1) | The §3.4 quote opens with a capital "Any". | Applied: "In §3.4's words, "any answer attempt, …"". |
| 40 (D1) | 45 is also the task's second operand. | Applied. |
| 42 (D1) | The "1" may begin a restatement. | Applied. Both readings are stated, and either is an attempt. |
| 50 (D1) | "license nothing" is narrower than rule 11. | Applied: "under rule 11 they decide nothing, and could license a pre-registration, never a verdict". |
| 61 (D1) | "next task" appears in lines 5 and 6 only. | Applied, in the agent's wording. |
| 64 (D1) | The misstatement bullets read as the full set. | Applied. They are now examples ("for example"), with S7 line 9, S8 line 10, S9 line 10 and S11 line 9 added. "I met with ridge" moves to a note as garbled wording. |
| 93 (D2) | "not yet written" is untrue of S1 line 6 and S10 line 5. | Applied, in the read's wording ("had not written when the line was generated"). |
| 99 (D2) | The list of the read's contents leaves out the rule's choice, stated. | Applied. |
| 102 (D2) | Confirming or correcting (b) items is §3.4's. | Applied: "§3.3 and §3.4". |

**The notes:**
- **N1, the refused pre-launch check.** It is added to the read's "What ran": refused at HEAD `9c7062e` (ONE PROCESS:
  the pod session's model-free `p_analyze.py --selftest` from the jlens venv), followed by the CLEAR check at
  `0afd842`.
- **N2, the commit after the launch.** It is added as the read's §8 "Git" line: the pod session's `2258c52`. It touches
  `RESULTS.md`, `data/p/` and three `results/raw/2026-11-09_p-gtime*` files, none of them named by the raw's GATE,
  LICENCE or A-M2 lines.
- **N3, the agent's disclosure** (one sub-second `grep` whose pattern contained "qwen"). This is recorded here. A
  `grep` is not a Python process, so `pgrep -ifl python`, the process check the laptop guard uses, cannot match it.

**Filled after the check:** the read's and the entry's lines on other sessions' processes (`@@OTHERS@@`). They come
from the coordinating session's messages: the pod session's v2 list, which the coordinating session passed and
checked, and the coordinating session's own account.

## The agent's report (verbatim; the session id's prefix shown as `<id>`)

## Summary

I couldn't save the report to `<tmp>/smoke/vc/report.md`: the Write tool refused it ("Subagents should return findings as text, not write report files"). The full report is below, ready to save as is.

**Tallies (103 items):** PASS 78, IMPRECISE 12, FAIL 0, NOT CHECKABLE 13.
- D1, items 1–71: PASS 57, IMPRECISE 8, FAIL 0, NOT CHECKABLE 6.
- D2, items 72–103: PASS 21, IMPRECISE 4, FAIL 0, NOT CHECKABLE 7.

**Rule, scrub and hashes:** I re-derived the classes from each record's pieces myself, without using the driver's classes. My results equal the driver's on all 67 lines.
- (i): F-0 3, F-a 6, F-b 3, F-c 2. (ii): F-0 5, F-a 11, F-b 0, F-c 2.
- F-b is selected. The first stop does not fire; the second fires. Adopted: none.
- The scrub touches lines 4 and 6 only, and the committed raw holds no local path.
- The 13 JSON copies are byte-identical to `out/`, and all three sha256 prefixes in D2 match.

**FAIL:** none.

**IMPRECISE, one line each:**
- **13 (D1):** "The post-load check passed (the raw's GATE line)". The GATE line is m:267's laptop checklist (`stages._laptop_preflight`). It is one of several checks after the load, and the driver calls the snapshot re-read "the post-load re-read". Name the check.
- **24 (D1):** "Its output, verbatim:" shows only `listing.txt` lines 2–8 of 214. The FILES line and the per-session listing are left out.
- **35 (D1):** the §3.4 quote begins "Any answer attempt"; the source has a lower-case "any".
- **40 (D1):** S2 round 8, "it contains the task's result". 45 is also the task's second operand.
- **42 (D1):** S5 round 10, "the numeral in the answer position". In S5 that position opens restatements (rounds 4, 5, 7), so the "1" may be the first digit of "14". It is an attempt either way.
- **50 (D1):** the §7 heading's "license nothing" is narrower than rule 11, which says post-hoc analyses "license pre-registrations, never verdicts".
- **61 (D1):** S9 "next task" appears only in lines 5–6. Lines 7–8 say "The task is…".
- **64 (D1):** the "misstates the record" bullets read as the full set. S7 line 9, S8 line 10, S9 line 10 and S11 line 9 also misstate the record, and "I met with ridge" is garbled wording, not a misstatement.
- **80 (D2):** the same post-load/GATE wording as item 13.
- **93 (D2):** "Header-like lines the harness had not yet written" is untrue of S1 line 6 (never written) and S10 line 5 (S10 ended at round 5).
- **99 (D2):** the list of the read's contents leaves out D1 §3, the rule's choice stated, which A-m2 §6 item 3 names.
- **102 (D2):** "(§3.3: … confirms or corrects each (b) item)". The confirm-or-correct of (b) items is §3.4.

**Counter (b):** no disagreements.
- I read 2 (b) responses, the same as D1: S3 round 7 and S6 round 8.
- I read none of D1's (b) responses otherwise, and found no (b) response that D1 does not list.
- All eight "considered" responses are not (b) on my reading. Only the grounds for S2 round 8 and S5 round 10 are loose (items 40 and 42), and S10 round 4 is borderline.

---

# Values-check: the A-m2 smoke, Code's read (D1) and its entry (D2)

Blind values-check, PI date 2026-11-09. I checked two drafts:
- **D1:** `<tmp>/smoke/read/code-read.draft.md` (371 lines).
- **D2:** `<tmp>/smoke/read/entry.md`.

`<tmp>` is the session scratchpad, as in the raw's header. Repository paths are relative to the repository root. This report contains no local path.

The placeholders `@@STAMP@@`, `@@OTHERS@@` and `@@VC@@` were ignored, and every item that depends on them is marked NOT CHECKABLE.

## Method

**Sources read in full:**
- ADDENDUM-m2 v0.3. Its sha256 is `83093812afdd513a9522024e8b766254e47d9aa226d5894577baf69855d9fa67`, at the working tree and at `HEAD:`.
- The committed raw: all 1,047 lines, every transcript, round line, read line and reasoning line.
- The original raw.
- The 13 JSONs in `out/` and their copies in `commit/`.
- `read_aid.py` and `listing.txt`.

**Repository sources:**
- git log and git show (read-only).
- CLAUDE.md (rule 11).
- PROPOSAL-m v1.11, line 267.
- LOCK-m-F3.md.
- RESULTS.md: the smoke driver's entry and the v0.3 entry.
- `results/raw/2026-11-08_open50-entry9_design-to-code_answers.md` (ans3).
- `scripts/mf3_sessions.py`, `valence_core/mf3/stages.py` and `valence_core/mf3/runner.py`.

**Independent recomputation** (`<tmp>/smoke/vc/check.py`, standard library, run with `python3 -I`). It does not reuse the driver's per-line classes.
- **Domain.** For each reasoning line, §1's domain is rebuilt from the record's `pieces` and `transcript`: the `\n`-terminated lines that end before the start of the line's own `reasoning_text` piece. A line is dropped if a model-written piece (`generation` or `reasoning_text`) touches it. Lines are kept distinct, in first-occurrence order.
- **Echo** is equality after whitespace normalization (runs of whitespace collapsed, ends stripped; case-sensitive).
- **Empty** means the normalized text is empty.
- **Cap** means `n_tok` ≥ the cap and a stop other than `newline`.
- **Counter (a)** means that some normalized domain line is a substring of the normalized line, or that `re.search(r"=== .+? ===")` matches.

The result, on all 67 lines: my classes, `contains`, `frame`, (a) flag and domain size equal the driver's (0 mismatches), and my tally equals `summary.json`'s `tally` key for key.

**Other scripts:**
- `vc/fmt.py` rebuilt every line of D1's code blocks in §4, §5 and §6 from the JSONs and searched D1 for each one.
- `vc/quotes.py` byte-checked D1's inline quotations.
- `vc/rawvsjson.py` checked the raw's 12 transcripts, 115 round lines, 67 line lines and session seconds against the JSONs. It found 0 differences.
- `vc/scrub.py` checked the scrub.
- `vc/responses.py` listed all 115 responses with their tasks, for the (b) read.

---

## Part A: D1 (Code's read)

1. **PASS.** Header: "ADDENDUM-m2 v0.3 §3 (sha256 `83093812…fa67`)".
   - `shasum -a 256` gives `83093812…d9fa67`, at the working tree and at `git show HEAD:`.
   - `summary.json` has the same value under `"addendum_m2_sha256"`.
   - So does the driver's `ADDENDUM_M2_SHA256` (`scripts/mf3_sessions.py:547`).
2. **PASS.** "the smoke is never of record, and its sessions, sham only and of no unit, are readable in full (§3.2)".
   - §3.2: "Sham templates only, and nothing of the smoke is of record: its sessions belong to no unit, so this document declares them readable in full".
3. **NOT CHECKABLE.** "This read is Code's (rule 25: every line of the raw was read)."
   - This is a statement about Code's own reading.
4. **PASS.** "The rule, not the read, selects (§3.3)" and "The seat reads every reasoning line and response and confirms the computation in its own raw."
   - §3.3: "The seat reads every reasoning line and every response of the twelve sessions and confirms the rule's computation in a raw; the rule, not the read, selects".
   - §6 item 3: "the seat's read raw".
5. **PASS.** The driver `scripts/mf3_sessions.py` `c9393a48…4d9b`, committed at `9c7062e`, run as `time --smoke` on HEAD `0afd842`.
   - Raw line 2: "HEAD 0afd842; driver scripts/mf3_sessions.py sha256 c9393a482001270e4564b940c17fa982f711aa9cf1a08e72ec239f16a0884d9b".
   - Raw line 5: "committed at HEAD 0afd84217508eacfdaf6d8d46c5a379ac622ae3d, working tree identical".
   - `git show 9c7062e:scripts/mf3_sessions.py` hashes to `c9393a48…4d9b`, and `9c7062e~1` hashes to `890084e6…90af`. So `9c7062e` committed these bytes. They are unchanged at `0afd842` and at `2258c52`.
   - Raw line 4: "scripts/mf3_sessions.py time --smoke --smoke-out …".
6. **PASS.** "launched 2026-11-09 18:14:32 UTC (Code's `date -u` stamp, in the raw's header)".
   - Raw line 2: "# Code stamp at launch: 2026-11-09 18:14:32 UTC (date -u)".
7. **PASS.** "with m:267's line as written".
   - Raw line 1: "Launched with m:267's line as written: `nohup caffeinate -is /bin/zsh <tmp>/smoke/run_smoke.sh > /dev/null 2>&1 & disown`".
   - m:267's laptop checklist: "`nohup caffeinate -is … & disown`".
   - `<tmp>/smoke/launch_smoke.sh` runs that line.
8. **NOT CHECKABLE.** "on the coordinating session's go".
   - This happened in chat. No source records it.
9. **PASS.** "after a CLEAR dry pre-launch check".
   - Raw line 1: "A dry pre-launch check (…) returned CLEAR just before the launch."
   - `<tmp>/smoke/prelaunch_out2.txt` ends "PRELAUNCH CLEAR", and its DRIVER line names HEAD `0afd842…`.
   - Note N1 below covers an earlier check that was refused.
10. **PASS.** Qwen `mlx-community/Qwen3.6-27B-4bit`, "snapshot `c000ac2c2057…`, unchanged after the load".
    - Raw line 6: "SNAPSHOT mlx-community/Qwen3.6-27B-4bit c000ac2c2057d94be3fa931000c31723aac53282".
    - Raw line 7: "SNAPSHOT re-read after the load: unchanged (c000ac2c2057d94be3fa931000c31723aac53282)".
11. **PASS.** "uncached, reasoning cap 60".
    - All 12 records have `"path": "uncached"` and `"reasoning_cap": 60`, and every reasoning entry has `"cap": 60`.
12. **PASS.** "under LOCK-m-F3 v0.1's licence (`377c5d60…`)".
    - Raw line 9: "lock LOCK-m-F3.md 377c5d602709004c: committed at HEAD 0afd84217508eacfdaf6d8d46c5a379ac622ae3d, working tree identical".
    - LOCK-m-F3.md hashes to `377c5d60…ecf6ce7`, at the working tree and at `0afd842`. Its last commit is `1e79955`, and its title line begins "# LOCK-m-F3.md — v0.1".
13. **IMPRECISE.** "The post-load check passed (the raw's GATE line)".
    - **What the GATE line is.** Raw line 8 is m:267's gate line. `stages._laptop_preflight` prints it (`valence_core/mf3/stages.py:263–275`), and only when "m:267's laptop checklist (power, one model process, disk; guard.preflight_laptop, imported) and the gate line's files committed" pass.
    - **When it runs.** The smoke calls it after the load: `scripts/mf3_sessions.py:1151` loads, and `:998` calls the preflight.
    - **Why the wording is loose.** It is only one of the checks after the load.
      - The driver calls its snapshot re-read "the post-load re-read" (`scripts/mf3_sessions.py:50`; raw line 7). RESULTS.md also uses "post-load" for that re-read.
      - The LICENCE, A-M2 and BACKEND lines also follow the load. The driver's entry in RESULTS.md says: "The order after the load: 1. the startup checks, the laptop checklist and the licence … 2. the A-m2 check, PROVENANCE and the BACKEND STOP".
      - "The post-load check" names none of these in particular.
    - **Fix:** "After the load, m:267's laptop checklist passed (the raw's GATE line), as did the snapshot re-read, the licence and the A-m2 check (their lines)."
14. **PASS.** "the backend is `a734dadec8f8ce9b`, the backend of record (§3.2)".
    - Raw line 12: "BACKEND a734dadec8f8ce9b".
    - §3.2: "Qwen, the backend of record (`a734dadec8f8ce9b`)".
    - The driver STOPs on any other backend (`scripts/mf3_sessions.py:1012–1014`).
15. **PASS.** "Twelve sham sessions, form-major", and the Sk mapping.
    - The raw's `SMOKE SESSION 1/12` to `12/12` run F-0 A1s to F-c A3s in order. The JSONs `01_F-0_A1s` to `12_F-c_A3s` match.
    - Every record has `"contrast": false`.
16. **PASS.** "All twelve ran, with G-VER clean in each. No driver refusal fired, and the wrapper printed `EXIT=0`."
    - All 12 session headers say "G-VER clean".
    - Every JSON has `"g_ver": []` and `"lines_error": null`, and every record has `"verified": true`.
    - Raw line 1047: "EXIT=0".
    - The tally and rule lines are printed. Per §3.3, a smoke stopped by a refusal prints "no tally and no rule".
17. **PASS.** The two exclusions.
    - S4 and S10 both have `"exclusion": {"class": "lexical", "detail": "lexical:ridge", "phase": "free"}`.
    - S4's only claim is at round 10. It has `"complete": true` and 10 rounds.
    - S10 has `"complete": false`, 5 rounds, 1 line and 1 choice.
    - §3.4: "both counters tabulated over all sessions, excluded ones included".
18. **PASS.** "the raw, 1,047 lines, with every reasoning line and every response".
    - `wc -l` gives 1047.
    - The raw has 115 round lines, 67 line lines and 12 transcripts, all equal to the JSONs.
19. **PASS.** The scrub (lines 4 and 6; `<repo>`, `<tmp>`, `<home>`; "as the header already was by the wrapper; no other byte changes").
    - `diff` shows lines 4 and 6 only.
    - Three substitutions reproduce each committed line byte for byte: the repository root to `<repo>` and the scratchpad root to `<tmp>` on line 4, and the home directory to `<home>` on line 6.
    - Line 1 is identical in both files and already carries `<tmp>`.
20. **PASS.** "the driver's thirteen outputs, byte-identical. They hold no local path."
    - `cmp` of each file in `out/` with its `commit/2026-11-09_a-m2-smoke_` copy: 13 of 13 identical.
    - None of these strings occurs in the copies: "/Users/", "/private/", "claude-501", "jasondwyer", "<id>", "/tmp", "scratchpad", "Documents".
21. **PASS.** §1, "verbatim (the raw's last seven lines)".
    - D1 lines 32–38 are byte-identical to raw lines 1041–1047 (`cmp`).
22. **NOT CHECKABLE.** "Before reading the raw, Code ran `read_aid.py`".
    - This is the order of Code's own actions. `listing.txt` is stamped 15:33 local time, a minute after `summary.json`.
23. **PASS.** Appendix A, "verbatim; standard library only, reading the thirteen JSONs", and what the script does.
    - D1 lines 287–370 are byte-identical to `read_aid.py` (84 lines, `cmp`).
    - It imports only json, sys and pathlib.
    - It re-tallies from the 12 session JSONs, re-applies the rule, and compares both with `summary.json`.
24. **IMPRECISE.** "Its output, verbatim:".
    - The block (D1 lines 48–54) is lines 2–8 of the 214-line `listing.txt`, verbatim.
    - It leaves out the output's first line ("FILES ['01_F-0_A1s.json', … 'summary.json']") and the per-session listing (lines 9–214).
    - **Fix:** "The head of its output, verbatim (after its FILES line; the per-session listing follows it):".
25. **PASS.** "`summary.json`'s `tied_on_i_ii` is `[]`, its `i_key` is `union`, and its `selectable` is `['F-a', 'F-b']`", with the same numbers as §1.
26. **PASS.** §3, count (i): F-0 3 (echo 3); F-a 6 (echo 5, cap 1); F-b 3 (cap 3); F-c 2 (echo 2); "No form has an empty line."
    - This matches the independent recomputation.
    - §3.3's (i) is "the union of m:265's three classes: empty line, cap reached without a newline, and echo under §1".
27. **PASS.** Count (ii): F-0 5, F-a 11, F-b 0, F-c 2.
28. **PASS.** The selection: F-b, with 3 against F-a's 6. There is no tie on (i), so neither (ii) nor the departure order is reached.
    - The keys are F-a (6, 11, 0) and F-b (3, 0, 1).
29. **PASS.** The first stop does not fire, since F-0 is at 3.
    - §3.3: "if **F-0 shows fewer than 3 defect lines**".
30. **PASS.** The second stop fires, with F-b at 3 of 18.
    - §3.3: "if **the selected form shows 3 or more defect lines** of its ≤ 18".
31. **PASS.** The quote "no change is made and the seat re-specifies again before any re-run" (§3.3); "Adopted: none"; §6 item 4 does not start.
    - The quote is an exact substring of §3.3.
    - `summary.json` has `"adopted": null`.
32. **PASS.** §4's 14 lines.
    - I rebuilt each from the JSONs as `S{k} {form} {template} line {n}: {classes} (n_tok {n_tok}, stop {stop_reason}): {text!r}` and found it in D1 byte for byte (14 of 14).
    - These are all the lines that carry a class.
33. **PASS.** §5's 18 lines, the definitions, and "the driver's test is the pattern `=== .+? ===`".
    - All 18 were found byte for byte, and they are all the lines with (a) true.
    - The driver defines `SMOKE_FRAME_RX = re.compile(r"=== .+? ===")` (`scripts/mf3_sessions.py:568`) and applies it with `.search` (`:698`).
34. **PASS.** §6's domain: 115 responses (30, 30, 30 and 25 by form).
35. **IMPRECISE (trivial).** The quote "Any answer attempt, correct, wrong, partial or to another item, is not (b)" (§3.4).
    - §3.4 has "any answer attempt, correct, wrong, partial or to another item, is not (b)", with a lower-case "any". The rest is exact.
    - **Fix:** lower-case it, or write "[A]ny".
36. **PASS.** "(b): 2 responses. F-0 1, F-a 1, F-b 0, F-c 0. Both are free rounds; no forced round is (b)."
    - See the counter (b) section.
37. **PASS.** The two (b) blocks, and item 1: "A preamble to reasoning about the choice, which ends at a colon and answers nothing. It is A3s round 8's kind at G-TIME-F3 (§2)."
    - Both blocks match byte for byte.
    - A-m2 §2 quotes A3s round 8: "Based on the pattern established in previous rounds, here is the evaluation and reasoning for the final round:".
    - §3.4 names "reasoning about the choice (A3s round 8's kind)".
38. **PASS.** Item 2 (S6 round 8).
    - "a description of the session or its configs" is §3.4's wording exactly.
    - S6 line 8 ends "based on `prism`'s correct answers to all its tasks so far]".
39. **PASS.** The eight "considered" blocks.
    - All 8 match byte for byte: phase, role, item, claim, stop, n_tok, task and response.
40. **IMPRECISE.** The S2 round 8 ground, "it contains the task's result".
    - It is true, but 45 is also the task's second operand ('Compute 90 minus 45.'). So "and 45" could be a fragment restating the operands as much as a result.
    - **Fix:** "it contains 45, the task's result (and also its second operand)".
    - The not-(b) reading stands either way.
41. **PASS.** The grounds for S4 round 9, S5 round 3 and S5 round 4.
42. **IMPRECISE.** S5 round 10: "Code reads the numeral in the answer position as a wrong answer attempt."
    - In S5, the start of the response is where the model restates the task in rounds 4, 5 and 7: '60 divided by 15 is 12.', '31 + 46 = 77.', '90 minus 45 is 45.'.
    - So the "1" could just as well be the first digit of "14", in a restatement that breaks off, as a wrong result.
    - Either way it is an attempt under the read's own convention: it reads S10 round 4 and S12 rounds 3 and 7, broken restatements, as attempts.
    - **Fix:** state both readings. For example: "Code reads the leading numeral as a wrong answer, or as the start of a restatement ('14 times 2'); either is an attempt."
43. **PASS.** S10 round 4: "after 4 rounds of evaluation" is repeated (2 occurrences), and "the banner's Note says "after the first four rounds"".
    - S10's banner: "Note: after the first four rounds you will choose which config runs each remaining round."
44. **PASS.** S12 round 3: "The driver records scaffold `[]` and claim None". S12 round 7: "S2's reasoning line 9 is 'Task: Compute 90 minus 44.'".
45. **PASS.** "Plainly wrong or loose answers are not listed: S6 round 4 (`'64'` …), S7 round 10 (`'31'` …), S12 round 4 (`'60 divided by 12'`) and S12 round 9 (`'close'`)."
    - I read all 115 responses. These four are every wrong or loose unclaimed response that is not already in D1's other lists.
46. **PASS.** The claimed blocks, "every claimed response of the smoke".
    - All 3 blocks match byte for byte.
    - The only non-null `audit.claim` values among the 115 rounds are S4 round 10 (lexical), S10 round 5 (lexical) and S11 round 8 (v2).
47. **PASS.** "S4 round 10 is round 9's reasoning line again, word for word, up to the cap. It is the session's exclusion (`lexical:ridge`)."
    - Round 10's text equals line 9's text exactly. Both have n_tok 60 and stop `cap`.
    - `audit.detail` is "lexical:ridge".
48. **PASS.** S10 round 5 is "the session's exclusion (`lexical:ridge`), and the session ends there".
49. **PASS.** S11 round 8 is "reasoning about the choice, at the cap, claimed `v2`. The session stays valid."
    - Its claim is "v2", its detail "audit:frame:evaluation session", its stop `cap` and its n_tok 60.
    - S11 has `"excluded": false`.
50. **IMPRECISE.** §7's heading: "(post-hoc and descriptive under rule 11; they decide nothing and license nothing)".
    - Rule 11 reads: "Post-hoc analyses labeled post-hoc; they license pre-registrations, never verdicts. Stop rules honored."
    - "license nothing" is narrower than the rule it cites. §3.3 also says "F-c's result is reported and informs any later re-specification".
    - **Fix:** either "(post-hoc and descriptive; under rule 11 they decide nothing, and could license a pre-registration, never a verdict)" or drop "and license nothing".
51. **PASS.** §7 item 1: "F-b's three (i) lines are all cap-reach. It has no echo, and counter (a) is 0." and "Each of its 18 lines is prose about the two configs."
52. **PASS.** The token counts "[48, 50, 57, 59, 60, 53, 60, 30, 44, 23, 57, 60, 59, 53, 54, 38, 40, 44]".
    - These are the JSON `n_tok` values in S7, S8, S9 line order.
53. **PASS.** "four lines ended at a newline within three tokens of it: S7 lines 7 and 8 (57 and 59), S8 line 9 (57) and S9 line 5 (59)".
    - These are the only F-b lines at 57–59, and each has stop `newline`.
54. **PASS.** "the longest line elsewhere runs 12 tokens in F-0 and 52 in F-c. In F-a it is S4 line 9, at the cap; the next longest runs 37."
    - S3 line 7 has 12, S11 line 9 has 52, S4 line 9 has 60, and S5 line 7 has 37.
55. **PASS.** §7 item 2.
    - S8 lines 6, 7 and 8 have n_tok 30, 44 and 23, all with stop `newline`.
    - The quoted endings match byte for byte.
    - They are the only F-b lines that end mid-sentence at a newline.
    - "cap reached without a newline" is §3.3's wording.
56. **PASS.** §7 item 3, the header-like lines: 6 lines (F-0 2, F-c 4), their texts, and "S1 line 6 is no header the harness writes".
    - The texts match byte for byte, including the en dash in '[round rounds 6–10 | choice]'.
    - None equals a line of its own domain.
57. **PASS.** `'...'` on S3 lines 5, 6, 8, 9 and 10; `'==='` on S11 lines 5–8 and 10; "a bare `===` does not keep the frame".
58. **PASS.** "Others that give no reasoning": S2 line 9, S4 line 6, S6 line 5 and S3 line 7.
    - The 45 lines in neither (i) nor (a) are D1's 20 grouped lines plus 25 lines of prose, so the grouping is complete.
59. **PASS.** §7 item 4.
    - Lines 6–10 each contain a `[round k | reasoning]` header and have (a) true. Line 5 contains none.
    - '格式错误' means "format error".
    - Line 9's bracket is never closed. The item's last sentence covers this.
60. **PASS.** §7 item 5.
    - Lines 7–10 match the claim, and line 8 matches byte for byte.
    - S5's rounds 3 and 4 are slate's. Their tasks and responses are as quoted.
61. **IMPRECISE.** "S9 lines 5 to 8 (F-b A3s) predict a "next task" (division, subtraction, division, division), and no such task comes next."
    - "next task" appears only in lines 5 and 6: "The next task is a division." and "The next task is subtraction."
    - Lines 7 and 8 read "The task is a simple division." and "The task is a basic arithmetic division."
    - The four kinds, and "no such task comes next", are right. Rounds 5–8 are 'Compute 31 + 46.', "Write the opposite of 'hot'.", "Write the opposite of 'up'." and 'Compute 90 minus 45.'.
    - **Fix:** "lines 5 and 6 name "the next task", and lines 7 and 8 "the task", as division, subtraction, division and division; no such task comes".
62. **PASS.** "S8 line 5 misquotes round 2's task."
    - Line 5 has "State the task text exactly as given.". Round 2's task is 'State the number of hours in a day.'.
    - The line itself goes on "(wait, no, round 2 task was "State".
63. **PASS** (the quotation). "S7 line 10 reads "I met with ridge"." Item 64 covers where this sits.
64. **IMPRECISE.** The three bullets under "Reasoning that misstates the record" read as the full set, but other lines misstate the record too:
    - **S7 line 9** credits ridge's 6/6 with "arithmetic (11+33, 31+4, 90-45)". 11 + 33 was saddle's round 3, and round 5's task was 'Compute 31 + 46.'.
    - **S8 line 10** says "Prism rounds: 1,5,6,7 (4 rounds)". Prism ran rounds 1, 2, 5, 6 and 7.
    - **S9 line 10** says "Prism 5/5". Prism had run six rounds: 1, 2, 5, 6, 8 and 9.
    - **S11 line 9** says "both configurations have demonstrated 100% accuracy on the previous tasks". Prism's round 8 response was the claimed v2 text, not an answer.
    - Meanwhile, S7 line 10's figures match the record (ridge 7/7, saddle two rounds). Its "I met with ridge" is garbled wording, not a misstatement of the record.
    - **Fix:** introduce the bullets as examples ("for example"), or list these lines too.
65. **PASS.** §7 item 7, the runtime.
    - Session seconds by form: F-0 800.322, F-a 2,196.415, F-b 4,239.865, F-c 1,024.102.
    - The total is 8,260.704 s, or 137.7 min.
    - The F-b sessions ran from 1,294.5 s (S9) to 1,621.527 s (S7).
    - §3.2's words are quoted exactly.
66. **PASS.** §7 item 8, the choice reads.
    - Counted from the raw's read lines, and the JSONs agree: `low_label_mass` True in 4/18, 2/18, 1/18 and 2/13 reads; `top1_not_label` True in 6, 7, 2 and 3.
67. **PASS.** §7 item 9.
    - It matches §0.1 ("9 of the 13 … verbatim (A2s five of six, A3s four of six)") and §3.2 ("F-0 is a fresh draw on the stage's cells").
    - F-0's echo lines are S2 lines 5, 6 and 10, and S3 has '...' five times.
68. **NOT CHECKABLE.** §8, Code's own processes.
69. **NOT CHECKABLE.** §8, "Other sessions: @@OTHERS@@". Note N2 has information for filling it.
70. **PASS.** §9: the STOP, and the three asks of the seat (§3.3, §3.4).
71. **NOT CHECKABLE.** "Nothing of §4 or of §6 item 4 starts. Nothing is pushed."
    - These are acts still to come. They are consistent with the state now: `origin/main` is at `da1e1b8`, and `main` is ahead by 12 commits.

## Part B: D2 (the entry)

72. **PASS.** "The A-m2 smoke (ADDENDUM-m2 v0.3 §3; §6 item 3; never of record)".
73. **PASS.** The routing: "Route as given", and ans3's item 1 ending "then the smoke driver's commit and the smoke's laptop go [go]".
    - ans3 line 18 ends that way.
    - RESULTS.md's v0.3 entry: "the PI's chat text of 2026-11-09, "Route as given" … The routing is therefore ans3's §3 as drafted."
74. **PASS.** The headline: all twelve ran, F-b was selected, the second stop fired at 3 of 18, nothing is adopted, and the STOP goes to the seat.
75. **NOT CHECKABLE.** `@@STAMP@@`.
76. **PASS.** The driver, its commit and HEAD. The evidence is item 5's.
77. **PASS.** The launch stamp, m:267's line, and the CLEAR check. The evidence is items 6, 7 and 9.
78. **NOT CHECKABLE.** "on the coordinating session's go".
79. **PASS.** Qwen, uncached, cap 60, the snapshot unchanged after the load, LOCK-m-F3 v0.1's licence, and A-m2 v0.3 (`83093812…fa67`) pinned.
    - Raw line 10: "A-M2 ADDENDUM-m2-f3-reasoning-block-v0_3.md 83093812afdd513a: committed at HEAD, working tree identical".
    - The pin is at `scripts/mf3_sessions.py:547`.
80. **IMPRECISE.** "The post-load check passed (the GATE line)." This is item 13's wording, with item 13's fix.
81. **PASS.** BACKEND `a734dadec8f8ce9b`, the backend of record.
82. **PASS.** Twelve sessions ran, with G-VER clean in each, no driver refusal, and `EXIT=0`.
83. **PASS.** The exclusions: F-a A1s at round 10 (complete), and F-c A1s at round 5 (ended there).
84. **PASS.** "The driver's tally and choice, re-derived from the thirteen JSONs by Code's cross-check, equal the driver's in every key".
    - Note: the cross-check re-tallies "each reasoning line's classes and (a) flag as the driver wrote them" and does not re-derive the classes themselves.
    - My independent re-derivation of the classes agrees on all 67 lines, so the sentence holds on either reading.
85. **PASS.** The table: all 24 numbers, with F-0 marked "control" and F-c "diagnostic".
86. **PASS.** The selection.
87. **PASS.** The stops.
88. **PASS.** "Adopted: none", and the §3.3 quote.
89. **PASS.** Counter (b) is 2 of 115, both in free rounds: F-0 A3s round 7 and F-a A3s round 8 ("Perfect.").
90. **PASS.** "The read also lists the eight responses it reads as not (b), and the three responses an audit class claims."
91. **PASS.** Observation 1.
92. **PASS.** Observation 2.
93. **IMPRECISE.** "Header-like lines the harness had not yet written, `'...'` and a bare `'==='` fall in neither (i) nor (a)."
    - "not yet written" is untrue of two of the six header-like lines:
      - S1 line 6, '[round rounds 6–10 | choice]', is no header the harness writes.
      - S10 line 5, '[round 6 | reasoning]', was never written in S10, which ended at round 5.
    - **Fix:** use D1's wording, "Header-like lines the harness had not written when the line was generated".
94. **PASS.** "The session seconds total 8,260.7 s (about 138 min), against §3.2's estimate of ≈ 50 min."
    - Note: §3.2's words are "≈ 50 min of generation at the stage's observed rate".
    - A session's `seconds` is "perf_counter wall-clock of the whole session (generations, reasoning lines and reads)" (`valence_core/mf3/runner.py:203–204`).
    - D1 quotes §3.2 in full.
95. **NOT CHECKABLE.** Code's own processes.
96. **NOT CHECKABLE.** `@@OTHERS@@`.
97. **PASS.** The raw: 1,047 lines; lines 4 and 6 scrubbed; sha256 `8e90f59b…66dd` before the scrub and `cd1416fc…e775` committed.
98. **PASS.** The thirteen outputs are byte-identical and hold no local path, and the summary's sha256 is `4c3ea332…73ef`.
99. **IMPRECISE (minor).** The list of what Code's read contains leaves out D1 §3, "The rule's choice, stated". That is the item A-m2 §6 item 3 names: "the rule's choice stated".
    - **Fix:** add "the rule's choice, stated".
100. **NOT CHECKABLE.** The link targets, `results/raw/2026-11-09_a-m2-smoke_code-read.md` and `…_valuescheck.md`, and the paths the raw and JSONs will be committed under.
     - None is in the repository yet. Of the smoke's files, `results/raw/` holds only the driver's three `a-m2-smoke-driver_*` files.
101. **NOT CHECKABLE.** `@@VC@@`.
102. **IMPRECISE.** "(§3.3: it confirms the computation in a raw and confirms or corrects each (b) item)".
     - The first half is §3.3's: "confirms the rule's computation in a raw".
     - The second half is §3.4's: "a declared read: Code lists every (b) response by session and round, the seat confirms or corrects each".
     - Of (b), §3.3 says only "counter (b) (§3.4) is reported and breaks no tie".
     - **Fix:** "(§3.3, §3.4: …)".
103. **NOT CHECKABLE.** "The laptop is free. Not pushed. Committed by path."
     - This is the state at write time, plus acts still to come. It is consistent with the state now: `origin/main` is at `da1e1b8`, and `main` is ahead by 12 commits.

## The selection rule, recomputed from the JSONs

This uses my own classes, not the driver's.

| form | lines | echo | empty | cap | (i) | (ii) | sessions (valid, complete) | responses (free) |
|---|---|---|---|---|---|---|---|---|
| F-0 | 18 | 3 | 0 | 0 | 3 | 5 | 3 (3, 3) | 30 (18) |
| F-a | 18 | 5 | 0 | 1 | 6 | 11 | 3 (2, 3) | 30 (18) |
| F-b | 18 | 0 | 0 | 3 | 3 | 0 | 3 (3, 3) | 30 (18) |
| F-c | 13 | 2 | 0 | 0 | 2 | 2 | 3 (2, 2) | 25 (13) |

- **(i) by line:**
  - F-0: echo at S2 lines 5, 6 and 10.
  - F-a: echo at S4 lines 5, 7 and 10 and S5 lines 5 and 6; cap at S4 line 9.
  - F-b: cap at S7 line 9 and S8 lines 5 and 10.
  - F-c: echo at S12 lines 8 and 10.
- **(ii) by line:**
  - F-0: S2 lines 5, 6, 7, 8 and 10.
  - F-a: S4 lines 5, 7, 8 and 10; S5 lines 5 and 6; S6 lines 6–10.
  - F-c: S12 lines 8 and 10.
- **Selection among F-a and F-b:** the keys are F-a (6, 11, 0) and F-b (3, 0, 1). **F-b is selected**, with no tie on (i).
- **Stop 1** (F-0 shows fewer than 3 defect lines): F-0 shows 3. **Does not fire.**
- **Stop 2** (the selected form shows 3 or more defect lines): F-b shows 3 of 18. **Fires.**
- **Adopted: none.**

All of this agrees with the driver's printed lines, with `summary.json`, and with D1 §1–§3 and D2's table.

## Scrub and hashes

- **The scrub.** The committed raw differs from the original on lines 4 and 6 only, exactly the stated path substitutions.
  - It holds none of "/Users/", "/private/", "claude-501", "jasondwyer", "<id>" or other parts of the session id.
  - One home-relative fragment remains: `<home>/.cache/huggingface/hub/…` on line 6.
- **Full sha256 values:**
  - Original raw: `8e90f59bf0d26beeaa56001555ffec5f2952713eac50b57b93549769b18566dd`.
  - Committed raw: `cd1416fccc8b0555cc82cad060f74b758b09228010809bc639d4dd1d8b73e775`.
  - `summary.json`: `4c3ea3322eacdd9433ba2a757682e8213a935e0357d980e7102ae11ed97573ef`.
- **Session JSONs.** These are identical in `out/` and `commit/`, and equal to Code's `read/commit_shas.txt`:

  | file | sha256 |
  |---|---|
  | 01 | `9a66d4bc…6a50` |
  | 02 | `b989184a…4130` |
  | 03 | `ec8b0350…44c8` |
  | 04 | `d4b9feee…f5d7` |
  | 05 | `dce7b60e…c839` |
  | 06 | `977d9c70…586d` |
  | 07 | `de8b50ab…58ee` |
  | 08 | `760f178d…0113` |
  | 09 | `2e330416…39be` |
  | 10 | `bb9054a6…71e8` |
  | 11 | `1acdd56b…d84b` |
  | 12 | `93035417…432b` |

- **D2's three prefixes** match.

## Counter (b), read independently

**What I read.** Every task response, 115 in all, in the raw's transcripts and its `round n (…)` lines, which equal the JSONs. I read each against its task.

**My partition of the 115:**
- **3 are claimed,** so outside (b): S4 round 10 (lexical), S10 round 5 (lexical), S11 round 8 (v2).
- **98 are correct answers.**
- **4 are wrong or loose answers:** S6 round 4 '64', S7 round 10 '31', S12 round 4 '60 divided by 12', S12 round 9 'close'.
- **8 are malformed attempts:** D1's eight.
- **2 are (b):** S3 round 7 and S6 round 8.

**Responses I read as (b) that D1 does not list as (b):** none.

**Responses D1 lists as (b) that I read otherwise:** none.
- **S3 round 7**, 'Based on the performance history and logical deduction regarding the configurations:'. It is (b): a preamble with no attempt at "Write the opposite of 'hot'.".
- **S6 round 8**, 'Perfect.'. It is (b): it makes no attempt at the bicycle task. It is an evaluative interjection.

**My reading of D1's eight "considered, read as not (b)":**
1. **S2 round 8**, 'and 45'. **Not (b).** It is a task-directed fragment, whether its 45 is the result or the operand. The ground is loose (item 40).
2. **S4 round 9**, 'A kilogram of trick question'. **Not (b).** A partial answer that begins the right one.
3. **S5 round 3**, 'DAILY ROUTINE : 11 + 33 = 44'. **Not (b).** A correct answer behind a stray prefix.
4. **S5 round 4**, '60 divided by 15 is 12.'. **Not (b).** The right result, with a wrong operand.
5. **S5 round 10**, '1 direct.'. **Not (b), but weakly.** The "1" is either a wrong numeral or the start of the restatement "14 times 2"; either is an attempt. The ground is loose (item 42).
6. **S10 round 4**. **Not (b).** It restates "60 divided by … 60 divided by 5." with no result. The repeated "after 4 rounds of evaluation" echoes the banner's Note but describes nothing. This is the borderline case.
7. **S12 round 3**, '11 + 3assistant'. **Not (b).** It begins the restatement "11 + 33" and breaks off.
8. **S12 round 7**, '90 minus 44'. **Not (b).** A restatement with a wrong operand.

**Outcome:** my count of (b) is 2 (F-0 1, F-a 1, F-b 0, F-c 0), both in free rounds. This is D1's count and D1's items.

## The observations' wording

Nothing in D1 §7 is presented as more than descriptive:
- Item 8 says "Code draws nothing from these".
- The selection rests on the rule's counts alone.

The wording findings are items 50, 61 and 64 for D1, and item 93 for D2.

## Tallies

| | PASS | IMPRECISE | FAIL | NOT CHECKABLE | items |
|---|---|---|---|---|---|
| D1 (items 1–71) | 57 | 8 | 0 | 6 | 71 |
| D2 (items 72–103) | 21 | 4 | 0 | 7 | 32 |
| **Total** | **78** | **12** | **0** | **13** | **103** |

The IMPRECISE items are 13, 24, 35, 40, 42, 50, 61, 64, 80, 93, 99 and 102.

The NOT CHECKABLE items are 3, 8, 22, 68, 69, 71, 75, 78, 95, 96, 100, 101 and 103.

## Notes (information, not findings)

- **N1. The pre-launch checks.** `<tmp>/smoke/prelaunch_out.txt` comes from an earlier dry check whose DRIVER line names HEAD `9c7062e…`. It ends "PRELAUNCH REFUSED". Its precheck line reads "preflight: ONE PROCESS: another model process is running: 8052 <repo>/jlens-qwen36/.venv/bin/python scripts/p_analyze.py --selftest" (the path is scrubbed here). The CLEAR check (`prelaunch_out2.txt`, at HEAD `0afd842`) came later. Neither draft mentions the refused check; both claim only the CLEAR one, which is accurate.
- **N2. For `@@OTHERS@@`: a commit inside the window.** Commit `2258c52` (G-TIME-OLMo (p) x3) has author and commit date `2026-11-09T13:51:56-05:00`, which is 18:51:56 UTC.
  - That is inside the window: the launch was at 18:14:32 UTC, and the last output, `summary.json`, is stamped 15:32 local time.
  - Its message gives box runs from 18:10:46Z to 18:22:04Z.
  - So HEAD moved from `0afd842` to `2258c52` during the smoke. The drafts' "on HEAD `0afd842`" is the launch-time HEAD, which is correct.
- **N3. Disclosure.**
  - One command line in this check broke the brief: a sub-second grep over `scripts/mf3_sessions.py` used the pattern `adapter = _load_qwen()`, which contains the word "qwen". No other command line carried mlx, jlens, qwen, olmo or ipykernel.
  - Nothing under `data/m/ckpt`, `data/mf3/ckpt`, `data/mf3/reports` or `data/p/ckpt` was opened, listed or hashed.
  - No git command that changes state was run, and no model was loaded.
  - The only files I wrote are the helper scripts under `<tmp>/smoke/vc/`. The report file itself was refused by the tool.
