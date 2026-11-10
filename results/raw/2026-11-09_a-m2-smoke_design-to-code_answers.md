# The seat's read of the A-m2 smoke (A-m2 v0.3 §3.3, §3.4): the rule's computation confirmed, counter (b) confirmed, and the re-specification — ADDENDUM-m2 v0.4

*Design seat, 2026-11-09 (evening). On the smoke entry (`6cfd3db`), its raw `results/raw/2026-11-09_a-m2-smoke.txt` (1,047 lines; every transcript, response, read and reasoning line read in full — the smoke is of no unit and readable in full, A-m2 v0.3 §3.2), the thirteen JSON outputs as the raw prints them, Code's read `_a-m2-smoke_code-read.md` and its values-check. The seat recounted every figure below from the raw's session blocks before quoting it. Placed untracked under `results/raw/` over the jspace-lab bridge (the PI verifies the sha256; the PI commits by path; Code adds the smoke entry's close line). Calendar dates only; the commit hash is the record.*

## 0. The short form

**The rule's computation is confirmed line by line: F-b is selected (3 defect lines against F-a's 6); the second stop fires (3 of 18 ≥ 3); nothing is adopted; the seat re-specifies.** The two (b) responses stand as Code read them, and the eight read as not (b) stand. The re-specification is **ADDENDUM-m2 v0.4** (delivered beside, untracked, for the F3 session's commit; v0.3 to `archive/` at that commit): **the reasoning block is F-b's exact bytes, and the cap is 120 from the re-run of G-TIME-F3 on** — m:174's own trigger value, applied one stage early because the smoke met the trigger's condition under the selected form (3 lines at the cap of 60); m:294's trigger is reported at the re-run and moves nothing. No second smoke. The alternative the PI may take instead — F-b at cap 60, m:174's trigger as written — is in the routing block with its risk stated (§3). The smoke's one cost the PI must see before routing: **F-b's sessions ran 1,294–1,621 s each, 4.7× F-0's** (§2.4), which lengthens every uncached Q-F3 stage.

## 1. The rule, recomputed from the raw (A-m2 v0.3 §3.3)

Per session, from the `line k (ci …): classes […]` and `(a) …` fields the raw prints (the seat's count; Code's cross-check and the values-check agree):

| session | form / template | lines | (i): echo, cap, empty | counter (a) |
|---|---|---|---|---|
| S1 | F-0 A1s | 6 | 0 | 0 |
| S2 | F-0 A2s | 6 | 3: 3, 0, 0 (lines 5, 6, 10 — the session banner verbatim) | 5 (lines 5–8, 10) |
| S3 | F-0 A3s | 6 | 0 | 0 |
| S4 | F-a A1s | 6 | 4: 3, 1, 0 (echo 5, 7, 10; cap 9) | 4 (5, 7, 8, 10) |
| S5 | F-a A2s | 6 | 2: 2, 0, 0 (5, 6) | 2 |
| S6 | F-a A3s | 6 | 0 | 5 (6–10: each contains a round header) |
| S7 | F-b A1s | 6 | 1: 0, 1, 0 (line 9) | 0 |
| S8 | F-b A2s | 6 | 2: 0, 2, 0 (lines 5, 10) | 0 |
| S9 | F-b A3s | 6 | 0 | 0 |
| S10 | F-c A1s | 1 | 0 | 0 |
| S11 | F-c A2s | 6 | 0 | 0 |
| S12 | F-c A3s | 6 | 2: 2, 0, 0 (8, 10) | 2 |

- **By form:** F-0 18 lines, (i) 3 (echo 3), (a) 5; F-a 18, (i) 6 (echo 5, cap 1), (a) 11; F-b 18, (i) 3 (cap 3), (a) 0; F-c 13, (i) 2 (echo 2), (a) 2. Equal to the driver's four TALLY lines and to `summary.json`'s tally, key by key.
- **Task responses:** 30, 30, 30, 25 (S10 ended at round 5) = 115; free responses 18, 18, 18, 13.
- **Selection** among F-a and F-b by fewest (i): **F-b** (3 < 6); no tie, so (ii) and the departure order are not reached. **Stop 1** (F-0 below 3): does not fire, F-0 is at 3. **Stop 2** (the selected form at 3 or more of ≤ 18): **fires**, F-b at 3. **Adopted: none.** §3.3: "no change is made and the seat re-specifies again before any re-run." Confirmed as the driver computed it.
- **Session seconds** (the raw's headers): F-0 306.2 / 279.1 / 215.0 = 800.3; F-a 848.9 / 761.5 / 586.0 = 2,196.4; F-b 1,621.5 / 1,323.8 / 1,294.5 = 4,239.9; F-c 130.8 / 574.9 / 318.4 = 1,024.1; total 8,260.7 s. F-b's mean is 1,413.3 s against F-0's 266.8 s.

## 2. The read (every line and response; §3.4's counter (b); observations under rule 11)

**2.1 Counter (b), confirmed.** Two responses attempt no task and are claimed by no class: S3 round 7 (`Based on the performance history and logical deduction regarding the configurations:` — a preamble; A3s round 8's kind at G-TIME-F3) and S6 round 8 (`Perfect.` to the bicycle item — an evaluative remark on the session; it attempts nothing, so it is (b) whatever its nearest named kind). **(b) = 2: F-0 1, F-a 1, F-b 0, F-c 0; both free rounds.** The eight Code read as not (b) are confirmed as answer attempts, including the weakest, S5 round 10 (`1 direct.`: a leading numeral in a session that restates its tasks — an attempt under §3.4's "partial or to another item" clause; under the other reading it would be (b) and fit none of the named kinds, so nothing turns on it). The three claimed responses (S4 r10 lexical, S10 r5 lexical, S11 r8 v2) are outside (b) by definition. The seat found no further candidate among the 115.

**2.2 What the forms drew, by the seat's eye** (descriptive; the rule selected, this did not): lines that state a reason about the configs — F-0 **4 of 18** (S1 lines 7–10; S2 none; S3 none), F-a **5 of 18** (S4 line 9, S5 lines 7–10; S6's six are bracketed meta-requests), **F-b 18 of 18**, F-c **2 of 13** (S11 line 9, S12 line 6). The non-reasoning lines no class catches: `...` ×5 (S3), a bare `===` ×5 (S11), header-like lines the harness had not written (S1 ×2, S10, S12 ×3), `Task: Compute 90 minus 44.` (S2), `Config choice (one word):` (S4), `Q: What is the main difference between the two configs?` (S3), S6's six `[Please provide reasoning …]` lines. None is reclassified (rule 11; the classes are the pre-registration's); recorded here so the re-specification rests on the whole picture, not on the bar's numerator alone.

**2.3 F-b's three defects are length, not degeneracy.** S7 line 9, S8 lines 5 and 10 are coherent prose cut at token 60 (`…while saddle has only completed two`; `…(wait, no, round 2 task was "State`; `…Both have 4/4 correct`). F-b's token counts, in order: 48, 50, 57, 59, 60, 53, 60, 30, 44, 23, 57, 60, 59, 53, 54, 38, 40, 44 (mean 49.4; 7 of 18 at 57 or more). The smoke's condition is the trigger's own: m:174/m:294 move the cap from 60 to 120 when 3 or more lines reach it. S8 lines 6, 7 and 8 ended at a model-written newline mid-sentence (30, 44, 23 tokens; `…prism had "State the number of`, `…"State the number of`, `prissing has 5/5 correct … Let`): not (i) as the class is written; one of them garbles the label (`prissing`); noted, not classed.

**2.4 Cost.** The uncached path re-encodes the context for every generated token, so the line's length sets the session's time: from the F-0/F-b difference, ≈ 4 s per reasoning token [E: (1,413 − 267) s over ≈ 6 × 44 extra tokens]. At cap 120 with lines running longer than at 60, an uncached F3 session is ≈ 25–35 min [E]. G-TIME-F3's six sessions ≈ 2.5–3.5 h; G-ID-F3's uncached members ≈ 0.5–1 h per pair; G-F3's 40 sessions ≈ 2 h cached or ≈ 20 h uncached; the campaign's 448–704 launches (m §2.4's table) ≈ 20–35 h cached or **≈ 190–370 h uncached** [E]. The campaign's path is G-ID-F3's to decide (m:295), so the uncached figure binds only if the cached/uncached pair diverges. The PI sets the hour cap at LOCK-m-F3 v1.0 (m:298); the figures are for that decision, not this one.

**2.5 Processes during the window** (the entry's §8): no model process ran beside the smoke; the pod session's model-free Python on the laptop after 18:23Z is a departure from nothing in the standing rule (one *model* process; announced runs), recorded as Code states it.

## 3. The re-specification (ADDENDUM-m2 v0.4, delivered beside)

- **The form:** F-b, bytes exactly as the smoke ran them (`[round {n} | reasoning]\nReasoning (one line): So far,`; the stored line is the model's text after the opener, stripped as a task response is; the boundary assertion at the new offset). The opener's missing trailing space (the model mostly supplied none, `So far,ridge …`) is cosmetic and is not changed: a changed byte is an untested form.
- **The cap: 120 at the re-run of G-TIME-F3 and every later Q-F3 stage** — m:174's trigger value, applied from the re-run on because the smoke met the trigger's own condition under the selected form; m:294's trigger is reported at the re-run (lines at the cap, of ≤ 36) and moves nothing, there being no further value. The bar is untouched: a line at 120 without a newline is a defect line; the re-run's bar reads its realised n (critical 5 at n = 18, p0 .10, α .05); a fire STOPs before G-ID-F3 and the seat re-specifies (m:293). The campaign's look bar (lock §8 bar 10) keeps the cap member, so pauses for the seat's adjudication are possible if F-b's cap-reach rate at 120 sits near p0; a pause is never a verdict (m:330).
- **Why not the alternative** (F-b at cap 60, the trigger as written): the trigger would almost surely fire at the re-run (the smoke's 3 of 18 at 60 projects to ≈ 6 of 36), moving the cap to 120 from G-ID-F3 on — the same end state — but the re-run itself would carry a ≈ 20–50% chance of the sham bar firing first (≥ 5 of 18 at the smoke's 3/18–7/18 rates), a second STOP on a length artifact. The alternative departs from m:174 by nothing, which is its merit; it is offered as [alt].
- **No second smoke.** F-b's defect class is length; a form that bounds length by instruction ("one sentence") is untested and no more likely to hold at temperature than "(one line)" did. The evidence for the opener is 18 of 18.
- **What re-runs** is §4.3's chain unchanged, with the cap stated at the lock's re-issue: the mf3 build (F-b in `banner.py`'s constants; §1's class in `lines.py`; the cap in `scaffold.f3_config`'s stage table) → self-tests → G-SHAPE-F3 and G-ANL-F3 re-runs → LOCK-m-F3 v0.1 re-issued → G-TIME-F3 re-run into `Q-F3_time-r2.json` (announced under the laptop rule; ≈ 2.5–3.5 h) → the seat's read under m:263's printed form and PROPOSAL-m §3's rule → G-ID-F3 → LOCK-m-F3 v0.2. The driver's `--smoke` form, pinned to v0.3's sha, is re-pinned to v0.4 or retired at the build; Code names which in the BUILD entry. D2 (2026-12-22) stands.

## 4. The record

- **Code (F3 session):** a close line on the smoke entry (`6cfd3db`) citing this file by path and sha256 — "the rule's computation confirmed; (b) = 2 confirmed; re-specified at ADDENDUM-m2 v0.4" — then v0.4's referent check of the delta (§6 item 1 of v0.4) and its commit on the PI's word; v0.3 to `archive/` at that commit.
- **The seat:** reads the G-TIME-F3 re-run when it lands; owes nothing else on this track.

## 5. For the PI — the routing block (the seat's defaults in brackets)

1. The smoke's result acknowledged: F-b selected, the second stop fired, nothing adopted; the seat's read confirms the computation and (b) [as ruled].
2. The re-specification: ADDENDUM-m2 v0.4 — F-b's bytes, **cap 120 from the re-run on** [adopted]; or the alternative, F-b at cap 60 with m:174's trigger as written [alt — if taken, the seat re-drops v0.4 with §4.1's cap sentence reverted before Code's commit].
3. v0.4 to Code's referent check and commit (v0.3 to `archive/`) → the mf3 build → G-SHAPE-F3 and G-ANL-F3 re-runs → LOCK-m-F3 v0.1 re-issued → G-TIME-F3 re-run on the laptop, announced, ≈ 2.5–3.5 h [go].
4. The hour figures of §2.4 are for the PI's cap at LOCK-m-F3 v1.0, not for now [noted].
5. D2 2026-12-22 [stands].
