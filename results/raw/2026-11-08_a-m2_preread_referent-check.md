# ADDENDUM-m2 v0.1 — the pre-read's referent check (A-m2 §7), with Code's dispositions

*Code's raw, PI date 2026-11-08. A blind referent check of `ADDENDUM-m2-f3-reasoning-block-v0_1.md` (untracked at root, sha256 `cdcc8e86…53f0`) by a fresh agent. It worked read-only at HEAD `daca8b0`, hashed the checkpoint `data/mf3/ckpt/Q-F3_time.json` without opening it (m:318), and was given A-m2 §7's list, the preamble's anchors and nine families of claims to check. Its report follows verbatim (the harness's indentation removed). Code then re-checked every item not marked PASS at source; its dispositions close the file. The block this raw serves: `results/raw/2026-11-08_a-m2_code-to-design_preread.md`.*

---

## The agent's report (verbatim)

**Referent check of ADDENDUM-m2-f3-reasoning-block-v0_1.md (v0.1), HEAD daca8b0: 35 PASS, 15 IMPRECISE, 2 FAIL, 7 OPEN (59 items)**

The facts the stage ruling rests on all hold: 9 of 13, critical 4 at n = 13, the fire, the A3s quote, the Q8 quote, the m:258 and m:265 quotes, and lock PINs F25/F28.

The two FAILs:
- **The keys anchor (item 22).** `keys.py:96–154` in §3.2 points at mf3's file, but that range only holds key families in m's file.
- **The re-issue list (item 51).** It omits the Q-F3 closure and G-ANL-F3, both of which move when mf3 moves.

The four OPENs that matter most:
- §1's domain is written for F-0 only (item 53).
- Count (i) in the selection rule has no defined scope (item 54).
- Counter (b) cannot be computed mechanically (item 55).
- m:261 and m:258 are left unaddressed if F-c is selected (item 59).

I worked read-only: nothing was edited, staged, committed or written under data/. `data/mf3/ckpt/Q-F3_time.json` was hashed only, never opened; its sha256 is b809c087…f8fc7, matching gt:17. I read the lock with `git show 1e79955:LOCK-m-F3.md`, which matches the working tree. `A:N` means line N of the addendum.

**A. Identity and anchors**
1. **Document sha256** (preamble, §7): PASS. cdcc8e8619801b357f79103ab74b9f419a3c2b21b2ffe9367014733a913f53f0; the file is untracked at root.
2. **The anchors** (A:5, A:76): PASS.
   - PROPOSAL-m v1.11 is 42ab36ec…6c6b, committed at 05c4636.
   - The lock at 1e79955 is 377c5d60…6ce7.
   - A-m1 was committed at f26bc59; its sha ea08322d… is at lock :91.
   - gt, the stage raw and the reads file were all added by acc3b52. The reads file is 2efd9470…, as gt:12–13 says.
   - The RESULTS entries exist: G-TIME-F3 at :248 (acc3b52) and the wiring at :345 (acde2d8).
   - ans exists (f683f5d2…ee19, committed at daca8b0).
   - The Q8 file was added at dc1ffe1 (aec58440…4df3); §8 is at :48–58 and its PI date 2026-11-06 is at :3.
3. **Anchor-list hygiene** (A:5, A:76): IMPRECISE.
   - `ans:` is defined but never used in the body.
   - Rule 21 is listed but never invoked.
   - Rule 28(d)(a) is used at A:52 but not listed.
   - §7 lists m:294 and m:296, which the body never cites, although §7 says "only what this document quotes". m:294 is "Cap fixed (§2.2's trigger)." and m:296 is "LOCK-m-F3 v0.2. Cap; path; projections."

**B. PROPOSAL-m lines**
4. **m:6, "Dating as m:6"** (A:3, A:5): PASS. m:6 is the dating convention.
5. **§3.1's rendering of m:174's block** (`[round {n} | reasoning]\nReasoning (one line):\n` + line + `\n`, with `{n}`, the joiner and the menu unchanged; A:35, A:52): PASS.
   - m:174 says: "the line `[round {n} | reasoning]`, a newline, the line `Reasoning (one line):`, a newline … then `"\n"`, then the unchanged menu block".
   - The code matches: mf3/banner.py:98–101, the verifier docstring at lock :333–358, and mf3/runner.py:170–172.
6. **§4.1, "the newline stop, the ban list, and the menu block are m:174's unchanged"** (A:52): IMPRECISE. m:174 has no ban list. The reasoning line's ban list comes from m:265 ("the frozen ban list applies to its generation"), which is m:261's e2a list.
7. **m:258's eight strings are "the hygiene set" and the session banner is not among them** (A:13): PASS.
   - m:258: "Six banner lines (COMMON; TOLD-MAP ×2; TOLD-MAP-SHAM ×2; TOLD-OBJ); with the two reasoning-block lines, eight declared harness strings … Roster admissibility of … the eight strings against both rosters".
   - m:253 puts SESSION_BANNER before them as "the template's banner".
   - m/banner.py:24–25 and :64–68 confirm the eight are used for roster admissibility.
8. **The m:265 quote "any complete harness-written line of the session", and the class's other two members** (A:13, A:23): PASS. Both are verbatim from m:265.
9. **"Match — m:265's: verbatim equality after whitespace normalization"** (A:23): IMPRECISE.
   - m:265 says "verbatim, whitespace-normalized reproduction", not equality.
   - The same words in m:261 are implemented as containment (m/audit.py:119–121), and Q8 also read m:265 as containment. So equality is the seat's reading, presented as m:265's text.
   - The normalisation described matches ws_norm (audit.py:99–102).
   - The count is unaffected: containment over m:265's domain also gives 9/13 (gt:145).
10. **m:263, "the seat's read under m:263's printed form"** (A:72): PASS. This is the record's own phrase (gt:5, RESULTS.md:260, ans:5).
11. **m:271** (A:13, A:56): PASS. It sets the sham-only bar domain, says a fire stops the stage, and sends contrast picks to the checkpoint for the VERDICTS read.
12. **"STOPPED before G-ID-F3 and the seat re-specifies (m:293)"** (A:13): IMPRECISE.
   - m:293 defines G-TIME-F3 "as G-TIME-F0" with its bars. It contains neither "STOP" nor "re-specifies".
   - The wording is the lock's on-fire cell for bar 5 (lock :405), which rests on m:271 and m:280.
13. **m:318** (A:5, the checkpoint not opened; A:13): PASS.
14. **"its picks and texts are readable (m:318 exception (2); rule 25)"** (A:42): IMPRECISE.
   - Exception (2) covers only "the sham-template first-pick shares reported at G-TIME and qualification stages".
   - Gate-stage sham transcripts are read redacted (m:271; exception (3)).
   - The smoke's full read actually rests on its being outside every unit, plus rule 25.
   - The phrase "a sham session carries no contrast information" is m:318's words, used without quote marks.

**C. LOCK-m-F3 v0.1 (1e79955)**
15. **§6, banner and reasoning-block bytes:** PASS (lock :310–331).
16. **§7, the classes:** PASS (lock :361–390; CLASSES are empty, cap_no_newline, echo).
17. **§8 bars 5, 8 and 10 are the reasoning-line defect bars:** PASS. They are at lock :405 (G-TIME-F3, 18/5), :408 (G-F3, 144/22) and :410 (the campaign). No other row is one.
18. **§9 PINs F25 and F28 implement the echo set:** PASS.
   - F25 is the domain: `lines.echo_lines`, "the eight strings as rendered for the session + the headers written so far" (lock :470).
   - F28 is the match: `classify_line` echo, "containment, case-sensitive, ws_norm, first match" (lock :473).
   - The same two rows are in results/raw/2026-11-06_mf3-build_design.md:82 and :85.
   - In the code: mf3/lines.py:37–43 and :98–100, with the call at :115.

**D. Files and line ranges**
19. **valence_core/mf3/lines.py:34–51 (echo_lines):** PASS. The function runs from :34 to :49; :50–51 are blank.
20. **valence_core/mf3/banner.py:95–101:** PASS. :95 is reasoning_header's return; reasoning_block is :98–101.
21. **valence_core/m/banner.py (SESSION_BANNER, REASONING_HEADER, REASONING_LINE):** PASS, with one note. REASONING_HEADER (:61) and REASONING_LINE (:62) are defined there. SESSION_BANNER is only imported there (:29), from session_e2a.py:69.
22. **"keys.py:96–154; mf3's" (§3.2) against "valence_core/m/keys.py:96–154" (§7)** (A:42, A:76): FAIL on the anchor.
   - The range is exactly m's key builders: item_key at :96 through the end of gate_sched_key at :154. These are Q-F0 and OLMo only; m refuses Q-F3 at :66–67.
   - In mf3/keys.py, lines 96–154 are the tail of arm_key, sched_key, gate_sched_key, key_templates and the self-test (:124–154). mf3's Q-F3 families are at :76–113 (listed at :7–11).
   - Neither range covers every family: m's `m-cal|` is at m/keys.py:52–58, and p's families are at p/keys.py:24.
23. **`m-smoke-f3|{form}|{template}|0` lies outside every family:** PASS. Its first field matches no family in either file:
   - m: `m|`, `m-time|`, `m-id|F0m|`, `m-f0m|`, `m-olmo*|`, `m-items*|`, `m-olmo-items*|`, `m-sched|`, `m-cal|`.
   - mf3: `m|`, `m-time|`, `m-id|F3|`, `m-f3|`, `m-f3-items*|`, `m-sched|Q-F3|`.
   - p: `p-sched|`, `p-olmo*|`.
   - The analyzer's `m-f3-blind|` (m_analyze.py:3979).
   - No `m-smoke` string appears anywhere in valence_core/ or scripts/.

**E. The G-TIME-F3 facts**
24. **9 of 13 lines are the banner verbatim, A2s five of six and A3s four of six** (A:11, A:23): PASS. The reads file has 13 sham lines (A1s 1, A2s 6, A3s 6). Nine equal the banner: A2s rounds 5, 6, 8, 9 and 10, and A3s rounds 5, 6, 7 and 10 (gt:109, :118, :128–129).
25. **Two frame lines, one `>` and one rationale:** PASS.
   - The frame lines are A2s round 7 and A3s round 8 (`=== Config selection ===`).
   - The `>` is A1s round 5 (1 token).
   - The rationale is A3s round 9 (30 tokens).
   - gt:103, :110, :118–120.
26. **0/13 as computed; critical 4 at n = 13; 9/13 fires:** PASS.
   - The stage raw says it at :18; gt says it at :63 and :78–79.
   - The exact binomials: P(X≥4 | 13, .10) = .0342 and P(X≥3) = .134, so the critical is 4. P(X≥9) = 4.9e-7.
27. **Cap 1 of ≤ 36; round_degeneracy 0/25; G-VER clean; no hair trigger; the 2026-11-07 date:** PASS.
   - The raw has these at :17 and :19–20; gt at :20–23.
   - Code's stamp, 2026-11-08 03:41Z, is 2026-11-07 on the PI's clock.
   - No sham line hit the cap, so the one cap-reach is a contrast line.
28. **Backend identifier a734dadec8f8ce9b:** PASS (gt:66–67, the report's identity, RESULTS.md:288).
29. **The A3s round-8 quote** (A:29): PASS, verbatim. Its audit claim is None and its advisory list is empty (gt:114–115). One note: "writes its reasoning in the response slot" is the seat's gloss. The response announces reasoning but gives none.

**F. Q8**
30. **The Q8 quote** (A:13): PASS, verbatim (prebuild answers :51; also gt:137–139).

**G. CLAUDE.md rules**
31. **"Nothing … runs before Code's step-3 commit (rules 9 and 11)"** (A:5): PASS, by m:8's reading "9 and 11 together (commit before data)".
32. **"rule 11: the pre-registration licenses the correction"** (A:13): IMPRECISE. That is not rule 11's wording ("Post-hoc analyses … license pre-registrations, never verdicts. Stop rules honored."). The clause that applies is "Stop rules honored".
33. **Rule 23 for counters (a) and (b)** (A:46): PASS on form. See item 44.
34. **Rule 25 for the smoke** (A:33, A:42, A:44): PASS. Minor: "every reasoning line and every response" is narrower than a full-transcript read.

**H. The smoke's design claims**
35. **Twelve sessions, ≤ 72 lines, ≤ 18 per form:** PASS. That is 4 forms × 3 sham templates, with N_FREE = 6 (m:172; session_e2a.py:89).
36. **"≈ 50 min" at the stage's rate:** PASS, with notes.
   - 12 × 237.0 s (the sham mean, gt:186) = 47.4 min.
   - That mean includes A1s's end at round 5. At the complete sessions' mean of 301 s, twelve sessions take ≈ 60 min.
   - The seconds are whole-session wall clock including reads (mf3/runner.py:203–205), not generation alone.
37. **"The stage's own schedule cells", and the templates' banners:** PASS.
   - Q-F3_time_A1s.json is pair 3 ridge/saddle, clause 0. A2s and A3s are pair 1 prism/slate, clause null. All have start 0 and map 0.
   - session_keys are arm `m-time|{t}|{s}` and items `m-f3-items-time|{s}`.
   - The banners match m:184–186, m:256–257 and mf3/banner.py:9–12.
   - Note: item streams are drawn per role (m/corr.py:350–371), so the realised free-round items follow the picks.
38. **F-a, "the model's first token supplies it, as at `Response:`"** (A:37; also A:38, A:52): IMPRECISE.
   - The adapter returns `decode(generated).strip()` (qwen_mlx.py:343), and the transcript is seg + stored text + "\n" (runner.py:145–147, :170–172).
   - So the context later rounds see has no space: the reads show "Response:A triangle has 3 sides.".
   - Under F-b the context would read "So far,<text>". F-b's join is not stated anywhere.
39. **"So far," holds no counter-(c) word and is label-neutral:** PASS.
   - "so" and "far" match no STAGE1_TERMS, POLARITY_NEG or POLARITY_POS entry (m_analyze.py:3441–3445).
   - It contains no roster word: neither the Qwen roster (e2d/config.py:36–37) nor any word in data/olmo/a1_repair_roster.json.
   - F-c's line is also roster-free.
40. **The smoke under "the lock's licence is checked at the smoke's start", with "one mf3 move, not two"** (A:42, A:70): PASS (feasible), with an implicit consequence.
   - The licence hashes mf3's package (lock :47–55). So the four forms and §1's count must live in the `--smoke` driver.
   - mf3's runner takes its segment from banner.reasoning_block (scaffold.py:87) and classifies with the current echo set (runner.py:163–167).
   - The driver is in G-SHAPE-F3's sources (gshape.py:91).

**I. Internal consistency**
41. **§0.4, "§5 sequences the re-issue … and the re-run"** (A:17): IMPRECISE. §5 holds the PI's decisions; the sequence is in §4.3 and §6. ans:19 and RESULTS.md:342–343 repeat the pointer.
42. **"Code's step-3 commit"** (A:5, A:63) against §6, where item 2 is the commit and item 3 the smoke: IMPRECISE. The record treats step 3 as the commit (RESULTS.md:339, :342; A-m1 at f26bc59, "s4 step 3").
43. **§6 item 2, "the G-TIME-F3 entry's dated correction"** (A:70): IMPRECISE. It was already committed at daca8b0 (RESULTS.md:330–336).
44. **§3.4, "descriptive, deciding nothing"** (A:46): IMPRECISE. §3.3 uses counters (a) and (b) as tie-breakers (ii) and (iii), so they decide the selected form whenever (i) ties.
45. **§0.1 "(cap 60 fixed, m:174)" against §4.3 "the trigger's count is the re-run's"** (A:11, A:56): IMPRECISE, minor. §0.1 does not note that §4.3 voids the stage's fixing.
46. **§6 item 4, "§3's rule"** (A:72): IMPRECISE. In the record it means PROPOSAL-m §3's read rule (gt:5; A-m1:60). Inside this document, §3 is the smoke's selection rule.
47. **§1, "every round header of either kind (`[round k | config: x]`, …)"** (A:23): IMPRECISE, minor. Task headers rotate over four forms (session_e2a.py:71–76), and the menu header `[round k | choice]` is a third bracket kind.
48. **§4.2: is leaving m/banner.py untouched feasible?** PASS.
   - mf3 renders from m's constants by import (mf3/banner.py:36–37). Its identity assert (:200) and its m:174 spec check (:161–163) are mf3-side, so mf3 can hold its own constants without touching m's.
   - The stated cost of editing m instead holds: m/banner.py is one of the licence's eleven (lock :108; its sha is unchanged) and is in G-SHAPE-F0's sources (m/gshape.py:92–93).
49. **§4.2's file list, "banner.py, scaffold, lines.py and gshape"** (A:54): IMPRECISE; the exact list is deferred to Code. F-0 literals also sit in:
   - mf3/runner.py:242–245
   - testing.py:148–151
   - verify.py:281
   - stages.py:1854
   - gshape.py:102 and :754
   - readrule.py:138 and verify.py:127, which move through calls into banner and lines.
50. **§4.3, "scripts/m_analyze.py is not touched"** (A:56): PASS on the narrow claim.
   - The analyzer holds no form literal and never recomputes the echo class.
   - It reads stored line classes and texts (:3845–3849, :3939, :3964, :3985).
   - Its lexicons (:3441–3446) do not depend on the form.
51. **§4.3's re-issue contents and §6's chain** (A:56, A:72): FAIL, a material omission.
   - The lock names "the Q-F3 closure (PIN-V2-12) … 22 modules", d19f336d… (lock :94). Those modules include mf3's banner, keys, lines, readrule, scaffold and schedule (G-ANL-F3.json g_anl_f3.f3_closure.modules), so §4.2's move changes the closure.
   - Q-F3's VERDICTS run refuses unless the lock names the current closure sha (m_analyze.py:4130–4134).
   - G-ANL-F3's artifact (lock :98, b91a8c67…) embeds the old closure, and its battery imports mf3's testing, stages and scaffold (:10545, :10591, :10718). `ganl` is write-once and compares its block (:11106–11124, :11231–11235).
   - Neither a new closure line nor a G-ANL-F3 re-run or supersession appears in §4.3 or §6.
52. **D2 = 2026-12-22:** PASS (A-m1:40; m:16).

**J. Unresolved definitions**
53. **§1's domain across the four forms** (A:23 against A:44): OPEN.
   - §1 lists `Reasoning (one line):` as a complete line and removes only the `Response:` fragment.
   - Under F-a and F-b the model continues that line, so by §1's own principle it is not complete. Under F-c the complete line is `Give one line of reasoning.`.
   - A per-piece split also needs two fixes. Empty strings from the "\n" joiners must be dropped: "" is contained in every line for counter (a), and audit.py:105–108 refuses empty echo lines. The menu line must be joined with the pick piece, or a bare label becomes a "line".
   - A mechanical rule is available from the record's pieces: a line every character of which lies in harness pieces.
54. **Count (i)** (A:44): OPEN.
   - It is unclear whether (i) is the echo member alone or the bar's union of empty, cap and echo (m:293; lock :405). As written, empty and cap-reach lines enter neither the selection nor the stops. A run-on inline form could be selected and then fire the re-run's bar (critical 5 at 18) or move the cap to 120 (m:174).
   - (i) is a raw count over a realised n that differs by form (A1s yielded one line at the stage). The rule does not say count or rate, and this affects stop (1)'s "fewer than 3".
55. **Counter (b), tie-breaker (iii)** (A:44, A:46): OPEN.
   - "No audit class claims" is mechanical: the claim is None.
   - "Answers no task" is not defined. Records carry no grade, and a grader miss is a different thing: A1s's "60 divided by 4 = 15" answers its task, wrongly.
   - A deep tie would therefore be settled by the read, against "the rule, not the read, selects".
56. **Counter (a)'s "keep the banner's `=== … ===` frame", tie-breaker (ii):** OPEN, minor. No operational test is given (for example, a line starting "=== " and ending " ===", or a partial frame).
57. **The smoke key's role** (A:42): OPEN, minor.
   - Sessions carry two keys, arm and items. The one key form given must replace the arm key only, or the claim that item streams are G-TIME-F3's fails.
   - With {form} in the arm key, the seeds and menu orders differ across forms (mf3/keys.py:85–97). There are no common random numbers, and F-0 is a fresh-seed replication, not a re-run of the stage's sessions.
58. **The re-run's checkpoint and VERDICTS** (A:56): OPEN, minor.
   - The default path data/mf3/ckpt/Q-F3_time.json (mf3/stages.py:98–106) already holds the first run's checkpoint.
   - The VERDICTS run takes one `--time` path (m_analyze.py:4189), yet §4.3 keeps the first run "of the record … their reads at VERDICTS".
   - After the move, mf3.readrule's piece check (readrule.py:136–139) rejects records in the old form.
59. **m:261 and m:258 under a new form** (A:52–54): OPEN.
   - §4 re-specifies m:174 only. m:261's task-round echo literal `Reasoning (one line):` is hard-wired in m/audit.py:64 and enforced at :171–176 (used at mf3/runner.py:130).
   - Under F-c that class keeps a string the session never writes and misses the new line. Fixing it means editing m/audit.py, one of the licence's eleven files, which contradicts §4.2.
   - m:258's roster admissibility runs only on m's eight strings (m/banner.py:67–68). F-b's opener and F-c's line are new harness strings with no declared check (both pass item 39).

**Totals:** 59 items — 35 PASS, 15 IMPRECISE, 2 FAIL (items 22 and 51), 7 OPEN (items 53–59).

---

## Code's dispositions (every item not marked PASS, re-checked at source)

The block's sections are cited as `block §x`.

| Item | Verdict | Re-checked at source | Disposition |
|---|---|---|---|
| 3 | IMPRECISE | A:5, A:76: `ans:` defined, unused; rule 21 listed, uninvoked; rule 28(d)(a) used at A:52, unlisted; m:294 and m:296 listed in §7, uncited in the body. Confirmed. | For the seat's v0.2, if one is issued; otherwise a dated note at the commit. Nothing here is Code's to change. |
| 6 | IMPRECISE | m:174 names no ban list; m:265 ends "the frozen ban list applies to its generation". Confirmed. | As item 3. The build applies m:265's ban list, as today (`runner.py:163–164`). |
| 9 | IMPRECISE | m:265: "a verbatim, whitespace-normalized reproduction"; m:261's echo is containment (`valence_core/m/audit.py:119–121`); Q8 read containment. Confirmed. | The seat's ruling, routed with A-m2: block §2 P1 implements equality as §1 states it, and block §5 item 6 names it as the seat's reading. The count is 9/13 either way. |
| 12 | IMPRECISE | m:293 (read in full) has no "STOP" or "re-specifies"; the lock's bar-5 row carries the on-fire wording. Confirmed. | As item 3. |
| 14 | IMPRECISE | m:318's exception (2): "the sham-template first-pick shares reported at G-TIME and qualification stages". Confirmed. | Block §5 item 7: Code's reading is that the smoke's sessions are outside every unit, so the read is full, as A-m2 §3.2 says; it is the seat's to strike before the smoke. |
| 22 | FAIL | `valence_core/m/keys.py:96–154` holds m's item_key through gate_sched_key; mf3's builders are `valence_core/mf3/keys.py:76–113`; `m-cal\|` at m/keys.py:52–58; the analyzer's `m-f3-blind\|` at `scripts/m_analyze.py:3979`. Confirmed. | For the seat's v0.2, or a dated note at the commit: §3.2's anchor points at mf3's keys.py:76–113, m's :52–58 and :96–154, p's keys.py:24 and the analyzer's `m-f3-blind\|` (`scripts/m_analyze.py:3979`). The key is outside every family (item 23). |
| 32 | IMPRECISE | CLAUDE.md rule 11: "Post-hoc analyses labeled post-hoc; they license pre-registrations, never verdicts. Stop rules honored." Confirmed. | As item 3. |
| 36 | PASS, noted | 12 × 237.0 s = 47.4 min; the complete sessions' mean ≈ 301 s gives ≈ 60 min; the seconds are whole-session (`runner.py:203–205`). | The smoke's announcement gives about an hour of wall clock, plus the load (block §2 P4, §6). |
| 38 | IMPRECISE | `qwen_mlx.py:343` strips; the reads show `Response:3`. Confirmed. | Block §5 item 1 states the join for F-a and F-b. |
| 41, 42, 43, 45, 46, 47 | IMPRECISE | Each confirmed as the agent states. | As item 3. Code reads §6 item 4's "§3's rule" as PROPOSAL-m §3's read rule, as gt:5 does. Code reads "step 3" as the commit, as the record does. |
| 44 | IMPRECISE | §3.3's (ii) and (iii) are §3.4's counters. Confirmed. | Raised with Q1 (block §3): at the smoke the counters break ties; at the stages they decide nothing. |
| 49 | IMPRECISE | Each anchor confirmed: `runner.py:242–245`, `testing.py:148–151`, `verify.py:281`, `stages.py:1854`, `gshape.py:102` and `:754`, `readrule.py:136–138`, `verify.py:126–127`. | Block §2 P3's file list includes `stages.py`, `readrule.py` and `scaffold.py`'s self-test (`:273`, found by the values-check). |
| 51 | FAIL | Lock line 94 names `d19f336d…`; `m_analyze.py:4131–4134` refuses a lock that does not name the run's closure; G-ANL-F3.json's `g_anl_f3` block records it; `write_texts_once` refuses a different artifact (`m_analyze.py:1930–1934`). Confirmed. | Block §4 F-C. Code found it independently. |
| 53 | OPEN | §1 (A:23) as quoted. Confirmed. | Block §2 P1, as Code's PIN: a mechanical rule over the pieces, as the agent suggests. It differs from the agent's wording on any line that holds a zero-length model piece: an empty response's `Response:` line, and, under F-a and F-b, the label line of an empty reasoning line. P1 keeps such a line out (consequence (a)); "every character in harness pieces" would keep it in. |
| 54 | OPEN | §3.3 (A:44): "(i) echo-class lines under §1"; m:293's bar is the union. Confirmed. | Block §3 Q2. |
| 55 | OPEN | Confirmed (A3s round 8: claim None, no advisory; "60 divided by 4 = 15." is A1s round 4). | Block §3 Q1. |
| 56 | OPEN | Confirmed. | Block §2 P2: the frame `=== .+? ===`, as Code's PIN. |
| 57 | OPEN | Confirmed. | Block §2 P4 (the arm key only; the item key is G-TIME-F3's); block §5 item 3. |
| 58 | OPEN | `stages.py:98–106`; `m_analyze.py:11319` (`--time`); `readrule.py:136–138` compares each reasoning piece with `banner.reasoning_block(n)`. Confirmed. | Block §4 F-B, readrule's check among its points. The values-check corrected the block's first draft here: the check does not run at the VERDICTS release (`release_full`, `readrule.py:518–520`), so the move does not refuse the first run's records there. |
| 59 | OPEN | `valence_core/m/audit.py:64` (`REASONING_LABEL`), `:158–163`, `:171–176`; m:258's admissibility runs in `valence_core/m/corr.py:447–467` over the eight strings of `valence_core/m/banner.py:67–68`. Confirmed. | Block §4 F-D, the m:261 half, conditional on F-c being selected. The m:258 half becomes Code's PIN: the smoke's forms (block §2 P4) and, at the build, the selected form (block §2 P3) are asserted roster-free at every start. |

**Totals after Code's re-check:** the agent's counts stand: 35 PASS, 15 IMPRECISE, 2 FAIL, 7 OPEN. No verdict is changed. Of the OPENs, two become questions (Q1, Q2), two FLAGs (F-B, F-D) and three Code's PINs (P1, P2, P4); #59's m:258 half is also answered by PINs (P3, P4).
