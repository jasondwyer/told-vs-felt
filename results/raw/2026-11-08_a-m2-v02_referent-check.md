# ADDENDUM-m2 v0.2 — the referent check of §7 and the "what changed" list (A-m2 v0.2 §6 item 1), with Code's dispositions

*Code's raw, PI date 2026-11-08. A blind referent check of `ADDENDUM-m2-f3-reasoning-block-v0_2.md` (untracked at root, sha256 `69e23212…cb47`) by a fresh agent, read-only, with HEAD `de729c4` at the start and at the end. It checked five things: the full v0.1 → v0.2 diff against the "what changed" list and the seat's answers (`ans2`, `09d856ef…ea29`); ans2 §9's referent items; ans2's rulings against v0.2's text; every §7 referent; and v0.2's internal consistency. It hashed the checkpoint without opening it (m:318). Its report follows verbatim (the harness's indentation removed). Code re-checked every item not CONFIRMED at source; the dispositions close the file.*

---

## The agent's report (verbatim)

**Referent check of ADDENDUM-m2 v0.2 (`69e23212…cb47`): HEAD `de729c4` at the start and at the end**

I worked read-only. Nothing was edited, staged or written, and Python ran from stdin only. `data/mf3/ckpt/Q-F3_time.json` was hashed and never opened; its sha256 is `b809c087…f8fc7`, matching gt:17.

While I ran, another session changed p-track files in the tree:
- modified: `scripts/p_sessions.py` and `valence_core/p/{proxy,register,report}.py`;
- new, untracked: `valence_core/p/{analysis,identity}.py` and `results/raw/2026-11-08_p-step6_entry9_code-to-design.md`.

None of these is a referent here, and every file I cite is clean against HEAD.

**Totals:** 51 items: 35 CONFIRMED, 13 IMPRECISE, 3 OPEN, 0 FAIL, 0 NOT CHECKABLE. Items 21 and 44 are one defect, so there are 12 distinct IMPRECISE defects; item 46 restates item 19.

**Headline:** three OPENs.
- **#48:** P4 pins v0.1's sha.
- **#49:** the rule has no clause for a smoke that stops.
- **#50:** §3.4's counters at gate stages have no blinding scope.

Every fact the ruling rests on reproduces, among them 9/13 and 11/13, recomputed independently.

### 1. The "What changed" list (v0.2:7) against the full diff (18 hunks from `diff`)

1. **The documents' identity.** CONFIRMED.
   - Hashes:
     - v0.2 `69e23212…cb47`; v0.1 `cdcc8e86…53f0`;
     - ans2 `09d856ef…ea29`, added at `de729c4`;
     - pre `0ff4fdb5…c088` and the referent raw `21d43e41…87cb`, both added at `da1e1b8`;
     - PROPOSAL-m `42ab36ec…6c6b`;
     - LOCK-m-F3 `377c5d60…6ce7`, with no diff from `1e79955` to HEAD.
   - `git log --all` shows neither A-m2 version ever committed, and neither path is ignored.

2. **Every listed change is made.** CONFIRMED, at the lines the list names:
   - §1's match and header kinds: :25;
   - §3.2's keys anchor and read licence: :44;
   - §3.3's (i) as the union, and (iii) struck: :46;
   - F-c as a diagnostic arm: :42 and :46;
   - §4.1's ban list: :54;
   - §4.2 by P3: :56;
   - §4.3's closure, G-ANL-F3 and the r2 checkpoint: :58;
   - §0.2's STOP anchor: :15;
   - §6 and §7: :71–74 and :78.

3. **"§4.3 names … the counters' VERDICTS path (pre:F-A)".** IMPRECISE.
   - The path is §3.4's closing bold sentence (:48), and ans2:22 places it at "v0.2 §3.4".
   - §4.3 (:58) carries only "F29's correction" in the re-issue list.

4. **Hunks the list does not name, each with an ans2 basis.** IMPRECISE: the list under-reports, though every change below is ruled.
   - :5, the preamble: `ans:` becomes `pre:` and `ans2:`, rule 21 goes, 28(d)(a) comes in (#3).
   - :13, §0.1's cap (#45).
   - :15, the rule-11 clause (#32).
   - :19, §0.4 (#41).
   - :25, §1's domain rewritten to P1 (label line by form, pick line, the operational sentence, the m:261 clause) (ans2:15, :38).
   - :44, the item-key and fresh-draw sentence (ans2:38 reading 3; #57).
   - :46, "Counts, not rates" and "(b) … breaks no tie" (ans2:11, :7).
   - :48, (b) rewritten (ans2:7).
   - :56, m's `audit.py` untouched, and the driver sentence (ans2:17–18).
   - :58, F29's correction, the first run's VERDICTS release, and the piece-check sentence (ans2:22, :26).
   - :65, §5 item 2 (ans2:46).
   - :71–74, §6 items 1, 2 and 4 beyond anchors (ans2:3, :26, :30, :47).
   - The list's source note names pre:§1 and pre:§3 only, though its own items cite pre:§2 (P3) and pre:§4 (F-A to F-D).

5. **Hunks with neither a list item nor a ruling.** IMPRECISE (minor; no rule moves).
   - (a) :3's supersession sentence. It is administrative and true: `da1e1b8`'s entry is headed "ADDENDUM-m2 v0.1 — PRE-READ (A-m2 §6 item 1): STOP", and ans2:3 says "v0.1 to `archive/` then".
   - (b) :46 changes "confirms the rule's choice" to "confirms the rule's computation".
   - (c) :56 drops v0.1:54's "Code states the exact files in its pre-read; the alternative — editing m's constants — is declined for its cost (…)". The decision stays; the reason goes.
   - (d) §7 adds m:159 (see item 12).

### 2. ans2 §9: each referent item against the raw's proposal

6. **#22, the keys anchor** (:44). CONFIRMED. The analyzer's line (m_analyze.py:3979) is not given, a minor omission. At HEAD:
   - m/keys.py:52–58 is `cal_seed` (`m-cal|`), and :96–154 runs from `item_key` to `gate_sched_key`;
   - mf3/keys.py:76–113 runs from `item_key` to `gate_sched_key`;
   - p/keys.py:24 is `FAMILIES`;
   - no `m-smoke` string appears in `valence_core/` or `scripts/`.
7. **#6** (:54). CONFIRMED. v0.2 reads "the frozen ban list applies to the line's generation as m:265 has it", and m:265 ends "the frozen ban list applies to its generation".
8. **#9** (:25). CONFIRMED. "the seat's reading of m:265's 'verbatim, whitespace-normalized reproduction'" quotes m:265 verbatim. m:261's containment is at m/audit.py:119–121.
9. **#12** (:15). CONFIRMED. v0.2 attributes the consequence to bar 5's row (lock:405: "STOP before G-ID-F3; the seat re-specifies (m:293)"), and m:293 sets the bar.
10. **#14** (:44). CONFIRMED. The full read rests on the smoke's sessions belonging to no unit. m:318 exception (2) is named only as "not the licence here", and the unquoted m:318 phrase is gone.
11. **#32** (:15). IMPRECISE. The quote "post-hoc analyses … license pre-registrations, never verdicts; stop rules honored" differs from CLAUDE.md:311–312, "Post-hoc analyses labeled post-hoc; they license pre-registrations, never verdicts. Stop rules honored.": two capitals are lowered and ". " becomes "; " inside the quotation marks.
12. **#3** (:5, :78). IMPRECISE.
    - Its four sub-items are applied: no `ans:` remains, rule 21 is gone, 28(d)(a) is listed, and m:294 and m:296 are out of §7.
    - But §7 now lists m:159, which the body never cites (the only m:159 is at :78). That is the defect #3 named.
13. **#41** (:19). CONFIRMED.
14. **#42** (:5, :65). IMPRECISE: half applied.
    - §5 item 2 now reads "Code's commit (§6 item 2)".
    - The preamble still says "before Code's step-3 commit", while §6 makes the commit item 2 (:72) and the smoke item 3 (:73). "Step 3" for the commit is A-m1's numbering (A-m1:58).
15. **#43** (:72). CONFIRMED. `daca8b0`'s RESULTS hunk adds the dated correction, in the seat's words.
16. **#45** (:13). CONFIRMED.
17. **#46** (:74). CONFIRMED. m:271, in §3 (heading at m:269), holds "The pre-VERDICTS read rule".
18. **#47** (:25). CONFIRMED. The task headers' four forms are at session_e2a.py:71–76, and the menu header `[round {n} | choice]` at :79–86.
19. **#49** (:56). CONFIRMED. The list equals P3's (pre:131–151): nine mf3 files, plus the driver once for the smoke.
20. **#51** (:58, :74). CONFIRMED. The closure, G-ANL-F3's superseding re-run, both new artifacts in the re-issue, and the chain are all there. One wording issue remains: item 41.
21. **#44, "is Q1"** (:46, :48). IMPRECISE.
    - Q1 (T) removes (b) from the ties.
    - But tie-break (ii) is counter (a), which §3.4 still calls "descriptive, deciding nothing".
    - The raw's reading, "at the smoke the counters break ties; at the stages they decide nothing" (referent raw:219), is not carried.
22. **#53, P1** (:25). CONFIRMED.
    - The rule as written: pieces up to the line's own piece; "touches"; `Response:` never complete; the label line by form; the pick line as rendered; distinct lines in first-occurrence order.
    - I recomputed it on the reads file (`2efd9470…`): 9/13 lines equal (A2s 5, A3s 4).
    - A minor point: ":25's Note lines (COMMON and the arm's TOLD line)" does not fit A3 and A3s, which carry COMMON only. The operational sentence governs.
23. **#56, P2.** CONFIRMED. It is accepted at ans2:16, though :48 does not restate `=== .+? ===`. I recomputed 11/13.
24. **#57, P4** (:44, :56, :72). CONFIRMED.
    - Only the arm key is replaced; the item key stays `m-f3-items-time|0`, as in the reads file.
    - F-0 is a fresh draw.
    - The sha pin is item 48.
25. **#59, P3 and F-D** (:56, :46). CONFIRMED.
    - The segment is roster-checked "as m:258's eight strings are".
    - F-c is not selectable, citing audit.py:64 and :171–176; audit.py is among the licence's eleven (lock:107).

### 3. ans2's rulings against v0.2's text

26. **Q1 (T).** CONFIRMED. :46 ties go to (ii), then to the departure order; "(b) … breaks no tie". :48 makes (b) (R)'s reading, over all rounds with its phase, listed by Code and confirmed by the seat. Nothing is added or narrowed.
27. **Q2 (U).** CONFIRMED. :46 makes (i) the union, with the members beside; both stops read defect lines, on counts.
28. **P1 to P4.** CONFIRMED: :25, :56, and :44/:56/:72. P2 stays in pre and ans2.
29. **F-A (ii).** CONFIRMED. :48 matches ans2:22. The F29 quote is verbatim (lock:474), and F29's correction is in :58's re-issue list.
30. **F-B.** IMPRECISE (minor).
    - Present at :58:
      - the r2 checkpoint, with its report and reads named after it (stages.py:109–126);
      - the precheck's refusal to overwrite (mf3_sessions.py:315);
      - id/qual taking r2 by path, and `--time` naming it;
      - the first run released by Code through `readrule.release_full` (readrule.py:518);
      - the piece-check sentence.
    - Narrowed or left implied:
      - v0.2 says "free-round events" where ans2:26 says "gate-stage events";
      - "one analyzer invocation, no second output set" and `prior_gate`'s recompute are implied, not stated.
    - An aside that is ans2's, not v0.2's: ans2:26 quotes "reported at Q-F3's VERDICTS" as m:271, but those words are m:293's.
31. **F-C.** CONFIRMED. :58 and :74 match ans2:30; `02dadb3`'s artifact records the old closure (G-ANL-F3.json:1307). A note: PIN-37 (m_analyze.py:1917–1920) and the precedent `G-SHAPE-F3.superseded-2026-11-07.json` keep the superseded file in the tree under a dated name, which "kept in history" understates.
32. **F-D.** CONFIRMED (:42, :46 against ans2:34).
33. **ans2 §8 readings 2, 3, 4, 6 and 7.** CONFIRMED: :46, :44, moot by :46, :25, and :44.
34. **ans2 §8 readings 1 and 5** ("v0.2 carries each"). IMPRECISE.
    - Reading 1's rendering is absent from v0.2. That rendering is `Reasoning (one line):<line>` with no space, as `Response:3` reads, and F-b's `So far,<line>` (pre:328–330).
    - :39 keeps the flagged phrase "the model's first token supplies it" (referent raw:131–134). Only the strip survives, at :54.
    - Reading 5 is implied by :46 and :72, not stated.

### 4. v0.2 §7's referents

35. **Quotes.** CONFIRMED, all verbatim:
    - m:265's two quotes (:15, :25);
    - the Q8 quote (prebuild answers :51);
    - F29's "the analyzer tabulates it" (lock:474);
    - A3s round 8 (gt:114–115).
36. **m:N paraphrases.** CONFIRMED: m:6, m:174 (block, cap 60, the trigger at ≤ 36), m:258, m:261, m:263, m:271, m:293 (≤ 18 lines, critical 5, the union) and m:318 (exception (2)).
37. **Lock sections and PINs.** CONFIRMED.
    - §6 is lock:310–331 and §7 is :361–390.
    - Bars 5, 8 and 10 are at :405, :408 and :410; bar 5 reads "18 / 5" with its consequence.
    - F25 :470, F28 :473, F29 :474.
    - The closure line at :94 reads `d19f336d…f039`, "22 modules".
38. **RESULTS entries.** CONFIRMED.
    - `acc3b52`: the G-TIME-F3 entry, with gt, the raw, the reads file and the checkpoint;
    - `daca8b0`: the dated correction;
    - `acde2d8`: the wiring;
    - `02dadb3`: G-ANL-F3's canonical run;
    - `da1e1b8`: the pre-read and its referent check.
39. **Files and ranges.** CONFIRMED.
    - mf3/lines.py:34–51: `echo_lines` is :34–49, then blank lines.
    - mf3/banner.py:95–101: `reasoning_block` is :98–101.
    - m/banner.py: `REASONING_HEADER` :61, `REASONING_LINE` :62; `SESSION_BANNER` is only imported, at :29.
    - m/audit.py:64 and :158–176.
    - qwen_mlx.py:292–305 and :343 (`.strip()`).
40. **Figures [S].** CONFIRMED.
    - 9/13 and 11/13, recomputed.
    - Critical 4 at n = 13: P(X≥4) = .0342 and P(X≥3) = .1339 (gt:78–79).
    - Twelve sessions and ≤ 72 lines (N_FREE = 6, session_e2a.py:89).
    - The backend `a734dadec8f8ce9b` (gt:66–67).
41. **:58, "`LAZY_F3_MODULES`, which includes mf3's banner, keys, lines, readrule, scaffold and schedule".** IMPRECISE.
    - `LAZY_F3_MODULES` is `("valence_core.mf3.scaffold", "valence_core.mf3.readrule")` (m_analyze.py:3430).
    - The six named modules are among the closure's 22 (`G-ANL-F3.json`, `f3_closure.modules`).
    - The fact the re-issue needs, that the closure moves, holds.
42. **Body claims outside §7.** CONFIRMED.
    - The precheck refusal and r2's admissibility.
    - readrule's piece check (:136–138) and `release_full`.
    - Write-once (m_analyze.py:1914–1942).
    - m's banner.py and audit.py among the eleven (lock:107–108).
    - The A-m1 pin (m_analyze.py:136–137, :570).
    - The three sham schedule files.

### 5. Internal consistency

43. **§0.4 against §4.3 and §6.** CONFIRMED: :19, :58 and :74 give the same chain.
44. **§3.3 against §3.4.** IMPRECISE. Tie-break (ii) uses counter (a), which §3.4 calls "deciding nothing". Same defect as item 21.
45. **§3.1's "F-b is the fallback if an inline slot alone does not draw prose"** (:42) against the rule (:46). IMPRECISE (minor). The rule picks F-b on fewer defects whatever F-a does, and the rule governs.
46. **§4.2 against P3.** CONFIRMED, as item 19.
47. **§5 against ans2 §10.** IMPRECISE.
    - (a) Time:
      - :66 and :44 say "≈ 50 min", where ans2:47 and the PI's routing at `de729c4` say "≈ 1 h".
      - 47.4 min is whole-session wall clock, reads included, at a sham mean that A1s's round-5 end lowers.
      - At the complete sessions' mean it is ≈ 60 min.
    - (b) F-B and F-C, confirmed at ans2:46, have no §5 line.
    - (c) The driver's commit before the go is only in §6 item 2.
    - (d) §5 item 1's acknowledgement was already routed at `daca8b0`, and neither it nor item 4 (D2) has an ans2 §10 counterpart.

### 6. Unresolved and substantive

48. **P4's sha pin.** OPEN (minor; it binds the smoke driver).
    - P4 checks "A-m2 committed, with sha256 `cdcc8e86…53f0`" (pre:164).
    - ans2:18 accepts P4 as proposed but says only "A-m2's sha".
    - v0.1 is never committed (v0.2:3, :72), so a driver built to P4's words cannot pass.
    - A dated note should set the pin to v0.2's sha, `69e23212…cb47`.
49. **A stopped smoke.** OPEN (minor).
    - P4 stops the smoke on a G-VER failure or a task-round scaffold fire (pre:181, :183), and runs the forms in form-major order (pre:175).
    - §3.3 has no clause for a stopped smoke. With counts, not rates, a form cut short offers fewer lines and could be selected over a complete one, and F-b or F-c may not have run.
    - One sentence would close it, for example "a smoke stopped under P4 selects nothing; the seat rules".
50. **§3.4's counters at the gate stages.** OPEN. It does not bind the smoke, which is sham-only and declared readable at :44. It binds from the re-run on, and the commit carries the text.
    - :48 declares (a) and (b) "for every Q-F3 stage from the re-run on", "tabulated over all sessions … reported at each stage's entry".
    - For (b) it adds "over all rounds", with Code listing every (b) response and the seat confirming each.
    - Before VERDICTS the record withholds exactly that material for contrast sessions:
      - m:271 withholds their "free-round events — exclusions, degeneracy, any class", and reads them "with its free rounds removed entirely";
      - m:263 prints a contrast free-round exclusion as its phase alone;
      - m:318 bars the seat from pick-bearing transcripts;
      - F-6 (lock:512–513) allows no per-line list of a contrast session's reasoning lines.
    - v0.2 gives the stage-entry tabulation no blinding scope.
51. **The rule's other terms.** CONFIRMED: each is operational.
    - (i) by P1 with F26 and F27 (lock:471–472); (ii) by P2; the departure order; the two stops, read on counts.
    - Not OPEN, but worth the seat's awareness:
      - Under the ruled counts-not-rates (ans2:11), a form scores fewer defects when its sessions end early. A reasoning-line scaffold fire (runner.py:173–175) and a task-round exclusion (m:271) both end a session, and both are outside (i).
      - The rule does not read round_degeneracy, which the re-run also binds (m:293, critical 5 at ≤ 30).

**HEAD:** `de729c4a41f137dc305efecfc03afa28e182f6b4` at the start and at the end.

---

## Code's dispositions

**What decides the commit.** No item changes a form's bytes, a bar, a key, a cell or the selection rule, nor a figure the ruling or the rule reads. OPEN #50 is substantive, though, and v0.2 §6 item 1 reads "any unresolved substantive item → STOP". Whether that STOP fires is the PI's to rule, on Code's question through the coordinating session, and v0.2's commit waits for that ruling. If the PI rules no STOP, v0.2 is committed as delivered, as at PROPOSAL-p's v0.2 commit (`18b0111`), and the items go to the seat as dated notes. #50 goes to the seat in its own block, `results/raw/2026-11-08_a-m2-v02_code-to-design_open50.md`. The three OPENs are disposed as follows.

**The OPENs:**

| Item | Re-checked at source | Disposition |
|---|---|---|
| 48 | pre:164 reads "A-m2 committed, with sha256 `cdcc8e86…53f0`"; ans2:18 reads "A-m2's sha and the four literals checked"; v0.1 is never committed (v0.2:3, :72). Confirmed. | Dated note, Code's reading: P4's pin is the committed A-m2's sha, v0.2's `69e23212…cb47`. The smoke driver pins it, and its self-test asserts it. |
| 49 | P4 stops the smoke on a G-VER failure or a task-round `scaffold_absorption` (pre:181, :183); §3.3 has no clause for a stopped smoke. Confirmed. | Dated note, Code's reading: a smoke stopped under P4 selects nothing. The driver prints no tally and no rule after a STOP (the session loop raises before them). Code reports the stop, and the seat rules, as at any STOP. |
| 50 | v0.2:48 declares (a) and (b) "for every Q-F3 stage from the re-run on … reported at each stage's entry"; m:271 withholds a contrast session's free-round events before VERDICTS. Confirmed. | **To the seat in its own block, to be ruled before the G-TIME-F3 re-run** (the first stage it binds); whether it is a FLAG or fires v0.2 §6 item 1's STOP is the PI's. It binds neither this commit nor the smoke, whose sessions are sham-only and declared readable (v0.2:44). Code's proposed fix is in the block's §4, before the unit's VERDICTS entry or NOT-RUN record: a gate stage reports (a) over its sham sessions' lines (and its contrast first lines where it reports their class, F60) and (b) over its sham rounds and its contrast forced rounds; the campaign's looks report neither (m:318); the rest comes at the VERDICTS entry or NOT-RUN record (m:271). The seat rules. |

**The IMPRECISE items** (12 distinct; each re-checked at source and confirmed as the agent states; each a dated note for the seat; none moves a rule):

| Item | Note |
|---|---|
| 3 | The counters' VERDICTS path is §3.4's (v0.2:48), not §4.3's; §4.3 carries F29's correction. |
| 4, 5 | The "what changed" list under-reports. Every unlisted hunk but four has an ans2 basis. The four are 5(a)–(d), and none changes a rule: 5(b) "computation" for "choice"; 5(c) a reason dropped; 5(d) m:159 in §7. |
| 11 | v0.2:15's rule-11 quote departs from CLAUDE.md:311–312 in two capitals and one stop. |
| 12 | §7 lists m:159, which the body does not cite. |
| 14 | The preamble's "step-3 commit" is §6's item 2. Code reads it as the commit, as the record does. |
| 21, 44 | Counter (a) breaks ties at the smoke (§3.3's (ii)) and decides nothing at the stages (§3.4). Code reads §3.4's "deciding nothing" as the stages' scope, as the pre-read's referent raw did (row 44). |
| 30 | The first run's release at VERDICTS: Code's step releases every gate-stage event of `Q-F3_time.json` through `release_full`, which returns the records whole (ans2:26's "gate-stage events"), not only the free-round ones. |
| 34 | ans2 §8's readings 1 and 5 stand from ans2. The smoke driver follows both: the strip and the inline rendering, and P1's classes printed beside the package's. |
| 41 | The six modules are in the Q-F3 closure (`f3_closure.modules`, 22), not in `LAZY_F3_MODULES` (two). That the closure moves holds. |
| 45 | §3.3's rule governs over §3.1's "F-b is the fallback". |
| 47 | The smoke's time is ≈ 1 h of Qwen (ans2:47; "~1 h Qwen", the routing at `de729c4`), about an hour of wall clock (pre:190), the figure Code announces. F-B and F-C have no §5 line, but ans2 §10 confirms them. |

**An anchor in the report:** its item 50 places F-6 at "lock:512–513"; the ruling stands at lock:513–515 (line 512 is F59's).

**The awareness notes (item 51):** the counts-not-rates consequence, and the rule's silence on `round_degeneracy`, are the seat's as written; Code changes nothing. The smoke's raw reports both: every session's end and every task round's claim.

