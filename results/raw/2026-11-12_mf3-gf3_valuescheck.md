# G-F3: the values-check of its entry, its block for the seat and its raw

*Code's raw, PI date 2026-11-12.*
- *What was checked:* three drafts, before the commit:
  - G-F3's RESULTS.md entry;
  - Code's block for the seat (`results/raw/2026-11-12_mf3-code-to-design_G-F3.md`);
  - the stage's scrubbed stdout raw (`results/raw/2026-11-12_mf3-gf3.txt`).
- *Against:*
  - the stage's report and reads (the read domain), and the checkpoint by digest only;
  - the run's records in Code's scratch;
  - the coordinating session's ack and its post-run message, as Code received them;
  - Code's order-only scan of the session transcripts;
  - m, A-m2 v0.5, LOCK-m-F3, the seat's answers, RESULTS.md and git.
- *How:* two blind agents in turn, read-only, each under a brief quoting the list of record v2's items 1–5 as written.
  Neither ran a model or either driver.
  - The first pass checked all three drafts: 69 items, 55 CONFIRMED, 7 IMPRECISE, 2 FAIL, 5 NOT CHECKABLE.
  - The second checked the changes only: 28 items, 23 CONFIRMED, 3 IMPRECISE, 0 FAIL, 2 NOT CHECKABLE, and one
    consistency finding, graded IMPRECISE.
  - HEAD was `0190c6d` at each pass's start and end.
  - Every FAIL and IMPRECISE item is applied (below).
- *Not run:* a third pass. Each change after the second pass applies that checker's own fix and carries no figure.
- *Code's masked scan of each checker's transcript* (counts only; no command text printed):
  - **The first:** 209 distinct command texts over every row of its transcript.
    - Ten of them name a ckpt path: five commands, each in two row forms. Two are `shasum` digest runs, one of them
      with `git check-attr`. The other three are the name-only listings its departure 2 and its departure 1's checks
      disclose (`git ls-files`, `git status --porcelain -- data`, a pruned `find`, an `ls -d` glob, a `print -l` glob).
    - None opens, reads or sizes a checkpoint.
    - No metadata form names `data/`. Nothing under the tasks directory was touched, and no transcript was opened
      outside the scan script.
  - **The second:** 103 distinct command texts. Two name a ckpt path, both its disclosed digest run (`git show
    HEAD:<path> | shasum -a 256`). It is clean on the other counts.
- *This raw:* Code's dispositions for each pass, then each report verbatim.
  - Code extracted each report by script from the agent's hand-back. Neither text has a final newline.
    - The first: sha256 `2b852a07…d1fc`, 286 lines.
    - The second: sha256 `24ba5ee3…34ea`, 168 lines.
  - Code's leak check found no local path, user name, session id or temp-dir id in either, and no clock time.
- *Nothing ran on a model* in either pass.

## Code's dispositions: the first pass

- **23 and 58, FAIL: the third-month item.** Agreed.
  - By item, it was presented 18 times in the read domain (17 clean; once corrupted, A3 s=4 round 2) and claimed 6
    times (4 sham, 2 contrast). So 6 of the 11 exclusions fell on it.
  - Code's count had matched the clean text only. Both drafts are corrected, the counts taken by tool (an item-id
    recount).
  - "Seen in the sham sessions" is dropped: two of the six are contrast sessions. The four of rule 28(c)'s item-shape
    kind are named.
- **6, IMPRECISE.** Applied: "each with its grounds, five with an alternative".
- **21, IMPRECISE.** Applied in the entry and the block, in G-F0m-Qwen's form: free-round events and picks to the
  VERDICTS entry or NOT-RUN record (m:271), seconds to the VERDICTS entry (m:318).
- **31, IMPRECISE.** Applied with 62 (below). The write-time stamps leave §0's list and the questions. The block's
  intro and short form now say "two facts of the run" and "two questions".
- **42, IMPRECISE.** Applied. The listings are "recorded here as facts of the run", with r2 Q3's ruling quoted: "Not
  a departure, mid-stage or after; nothing is needed." "Under item 8" is dropped.
- **49, IMPRECISE.** Applied: the quote leads with "… ".
- **54, IMPRECISE.** Applied. `Triangle`'s grounds now quote r2's form exactly, name the session's one-word round 3,
  and mark the reading as Code's extension of that form.
- **62, IMPRECISE.** Agreed, and it changes Q3 in substance.
  - The seat's G-TIME-F0 read (Q4, its line 49) already counts "the entry's own stamps, which are no tighter than the
    commit times" among the unavoidable records that remain.
  - r2 §4 notes "the entry's write-time stamp bounds the end for every reader anyway".
  - So the stamp lines on Code's two G-TIME-F3 entries are within that ruling, not a departure. Q3 is withdrawn.
  - The block's §3 now records the G-F3 entry's missing stamp line with both quotes, and says the commit time stands
    for it. The entry says the same.
  - Code's draft had asked about a class the seat had already ruled on, and the first pass's reading of the record
    caught it.
- **14, NOT CHECKABLE: Code's own process claims.** The answer-key check behind "checked this by script" is now saved
  in scratch (`answer_key_check.py` and its output). It gives 218 and 18, as the checker's own key did.
- **16, NOT CHECKABLE: "during the run".** The coordinating session's post-run message, received after the first pass,
  places its second compaction during the run, with `0190c6d` as its top commit. Both drafts now cite it. No time is
  stated.
- **41, NOT CHECKABLE: "both reports".** Code re-ran its scan with the report and the reads flagged apart
  (`scan_window2.py`, one line changed). Code's compaction, the pod session's compaction after the end and the
  values-checker's start each name the checkpoint, the report and the reads. The block says so.
- **28, NOT CHECKABLE.** The placeholder, filled at the commit.
- **66, NOT CHECKABLE.** The raw's header line is the wrapper's own text; the raw is not edited.

**The checker's observations:**
- **NOTE-6.** Applied. The entry now records both digests at launch in full, with LOCK-m-F3 v0.2's lines (73, 81).
- **The commit "during the run".** Kept. It states an order and no time, and the seat's G-TIME-F0 read (Q4) counts
  commit times among the unavoidable records. For the seat's (65) check.
- **Free-round exclusions visible through r.** This is m's pre-registered form (m:192, m:318); no change.
- **Counter (b).**
  - Items 2–3 now carry the "to another item" alternative.
  - `Triangle`'s alternative notes that the checker would read it and `any` alike.
  - Q2's wording is now neutral.
  - `11 + caused an error.` is unchanged: its alternative was listed.
- **A new file in the shared tree** (`results/raw/2026-11-12_p-qual_design-to-code_answers.md`). Another session's.
  Code did not open it, and it is not in this commit.

**The checker's departures** (its "Conduct"), for the seat:
1. **One recursive grep** over the checkout, restricted to `*.md`, ran without the `data/` exclusion of item 3's form.
   - It printed one match line, from the seat's r2 answers raw.
   - Its name-only checks found no `.md` file in any ckpt or reports directory. Three tracked `.md` files under
     `data/m/gates` and `data/n/bk` were within its scope.
   - No checkpoint or report file was searched.
2. **Two name-only commands under `data/`**, neither in item 1's literal form:
   - `git status --porcelain -- data` printed the three untracked `data/mf3` names;
   - an `ls -d` glob printed only the shell's "no matches found".
   - Neither printed a size or a time.

**Additions after the first pass** (graded by the second):
- the coordinating session's post-run check, in the block's §0 and the entry;
- the scan's split of the report and the reads;
- the stamp note in the block's §3 and the entry;
- NOTE-6's digests in the entry.

## Code's dispositions: the second pass

- **6, IMPRECISE.** Applied: "and the start of this block's first values-checker (a subagent of Code's session,
  after the end)".
- **8, IMPRECISE.** Applied: "after the coordinating session's ack".
- **15, IMPRECISE.** Applied, in the checker's words. "The two labels and A1s s=6's frame are config- or session-topic
  responses of the kind rule 28(c) describes. Whether A3 s=5's banner counts is the seat's tally, on the contrast
  forced rounds (§1.1)."
- **C1, IMPRECISE.** Applied: "the four project transcripts active during the run; its re-run after the first
  values-check adds that checker's, started after the end".
- **5, NOT CHECKABLE: "Code's own order-only comparison agrees".** This is Code's own step, in its session.
  - It compared `0190c6d`'s commit time with Code's launch call and its end-wait's notification, in code.
  - It printed two booleans, both true ("after the launch call", "before the end-wait notification"), and no time.
  - Kept.
- **28, NOT CHECKABLE.** The placeholder, filled at the commit.

**The checker's observations:**
- **The commit's lower bound.** As at the first pass: for the seat's (65) check. It states an order and no time.
- **"Item-8 disclosures".** The drafts follow r2's Q3 ruling and quote neither framing. No change.
- **A precedent for the block's §3** (the Q-F0 campaign entry's "the entry's own stamps (here its calendar date
  alone)"). Not added; it is recorded here.
- **The pod session's stamp line** is no longer named, as intended.
- **The brief's "four sub-bullets".** The brief's count was off. The block carries the check as one bullet with three
  sub-bullets; its fourth item, Code's compaction after the end, sits just above.
- **The entry's placement.** Applied: "One item." is now its own sub-bullet beside "Contrast" and "Sham".
- **Q2's `clean`.** Applied: "`clean`, read as a wrong answer: …".

**The checker's departure** (its "Conduct"), for the seat:
- It ran `git show HEAD:<path> | shasum -a 256` on the committed prior checkpoint (under `data/mf3/ckpt`) and on
  G-ID-F3's artifact (under `data/mf3/gates`).
- It printed only the two digests, both equal to the lock's values.
- Item 1's form for a committed blob is `git rev-parse <rev>:<path>`, and this form is not on its list.

## The first checker's report (verbatim)

# Blind values-check of G-F3's three drafts (read-only)

- **HEAD at start:** `0190c6d`. **HEAD at end:** `0190c6d`.
- **The brief:** its sha256 `36210e4f…c6f6` was verified before I started.
- **Drafts as checked, by sha256:**
  - E = `G/entry_gf3.md`, `76d94b2e…431f`
  - B = `results/raw/2026-11-12_mf3-code-to-design_G-F3.md`, `9e774b9c…5664`
  - R = `results/raw/2026-11-12_mf3-gf3.txt`, `e0fb80ed…55d9`
- **Names used below:** G and Q are the brief's labels for Code's two scratch folders. "report" and "reads" are the two files under `data/mf3/reports/`. The checkpoint was hashed and nothing else.

**How I checked:**
- Every figure was re-derived from the report and the reads with stdlib Python.
- The bars were re-derived by exact binomial.
- Counters (a) and (b) were re-derived with `valence_core.mf3.lines` in the project venv: `counter_a_of_record`, `b_candidates`, `tabulate_b`.
- The 224 answers were checked against my own key over the 16 items.
- Every quote was string-matched against its source and against the draft.
- A script matched all 62 contrast renders, with their `*` marks, and all 8 sham exclusion responses against B.

## The entry (E)

1. **CONFIRMED.** E:1–3, the header: PASS, 40 uncached sessions at cap 120, `05ef75d`, `b427f82`, the checkpoint's path.
   - Report: status PASS; identity path uncached, `reasoning_cap` 120. R:56–57.
   - Lock :269–272 is v0.2 §9 item 2. G-ID-F3 answers :56 (§8) and :67 (§9 item 5).
   - "Route as given" of 2026-11-11 is in `b427f82`'s message and ACK :9.
2. **CONFIRMED.** E:4–7 and E:53–58, the bars.
   - Report bars: k 7, n 189, critical 16; k 2, n 98, critical 16. R:53–54.
   - Exact recompute: P = .8380, critical 16 (.0286); P = .9996, critical 16 (.0339). At the planned n: 240 → 19 (.0336) and 144 → 22 (.0296), as m:271 and m:297 state.
   - The 7 claims, all frames:
     - forced, each its session's last round: A1s s=0 r4, A1s s=6 r2, A2s s=3 r4, A2s s=5 r4;
     - free: A3s s=2 r8 and r9, A3s s=3 r8. Both sessions ran to round 10, per m:271's "a free-round v2 claim ending nothing".
   - The defect lines: A1s s=1 and A3s s=6, line n=5 ci 0 in each, n_tok 120, stop cap, class `cap_no_newline`. No empty line and no echo.
   - All 40 records have `verified` true.
3. **CONFIRMED.** E:8 and E:72, counter (a): R:55. The report's `counter_a` is 0 for each sham template, and 0 in `reasoning_line_1` for A1/A2/A3, whose lines are 3+4+6 = 13.
4. **CONFIRMED.** E:9–10, r = 29/40 and the per-template split.
   - Matches the reads' valid and domain flags and the report's `valid_sessions`.
   - m:192; m:297's "r for Q-F3 = pooled over all 40".
   - Same form as G-F0m-Qwen's entry, RESULTS.md:7410.
   - 8 sham and 3 contrast sessions are excluded, and all 3 contrast exclusions are at forced rounds.
5. **CONFIRMED.** E:11–12 and E:73–76, counter (b).
   - Domain 189 + 62 = 251. 15 claimed, 12 sham + 3 contrast. `b_candidates` gives 236.
   - The four items are as the reads hold them (see 51).
6. **IMPRECISE.** E:77, "Eight are read as not (b), each with its alternative (the block, §1.5)".
   - Only five carry an alternative (B:350–366): `direct`, `clean`, `Triangle`, `11 + caused an error.`, `The opposite of常识`.
   - `31 + 4 model`, `half a kilogram of feathers` and `A kilogram of trick` give grounds but no alternative.
   - Fix: "each with its grounds, five with an alternative".
7. **CONFIRMED.** E:13: B:166–190 quotes all 62 forced-round responses.
8. **CONFIRMED.** E:14: E carries no stamp line.
9. **CONFIRMED.** E:16–18: the routing quote is verbatim from G-ID-F3 answers :56; `a6c6297` adds that file.
10. **CONFIRMED.** E:19–21, the launch line, HEAD and the ack.
    - The launcher is Q's `run/launch_gf3.sh`:5. The launch command's HEAD test is `b427f82` (Q's `run/launch_and_endwait.txt`:2).
    - The ack quote is ACK :3. The launch record :15 says the ack came before the launch.
    - Note: m:267 itself reads `nohup caffeinate -is … & disown`. The quoted command fills the "…", the form of RESULTS.md:402, :724, :3310.
11. **CONFIRMED.** E:22–24, the wrapper and the raw's header.
    - The wrapper (Q's `run/run_gf3.sh`) is consistent at :8–10, :15–22 and :27, and R:3–5 match.
    - "630 GiB free" is R:4's "630Gi available on /".
12. **CONFIRMED.** E:25–26, the dry check and the refusal.
    - `prelaunch_final.txt` :1–10 reads CLEAR.
    - `prelaunch_check_qual.py` :19–25 blocks the model imports and the loader; :29–34 is the recorder.
    - The launch record :2 and :4–5 show the refusal test.
13. **CONFIRMED.** E:28 and B:88–93: the end-wait, the launched line with no stamp, the launch record, and no subagent.
    - The end-wait is at launch record :10 and :12. Its form is O3-1's PID loop with a command guard, then a `pgrep` wait. It touches no file.
    - That is the form G-ID-F3's entry calls "on the PID alone" (RESULTS.md:411), confirmed at G-ID-F3's values-check :143–145.
    - "No subagent": in G's scan output, no subagent transcript of Code's session was modified since the launch. My re-run adds only this checker's, started after the end.
14. **NOT CHECKABLE.** Code's process claims: E:28–30 (memory note, ended its turn, no model or Python process, read nothing of the outputs), E:59, E:80–81, B:15, B:18, B:94–95, B:377 ("checked this by script"), B:440.
    - No listed source records them. The transcripts are closed to me except through the scan, which prints compactions and status attachments only.
    - G holds no answer-key script or output; `b_cands.py` only lists candidates.
    - Nothing I read contradicts them.
15. **CONFIRMED.** E:32–33 and B:97–100, the commit's facts.
    - `0190c6d` touches RESULTS.md only. Its parent is `b427f82`, the HEAD the launch command asserted, so it landed after the launch.
    - R:11 says "hashed at stage start". Neither the report's identity fields nor the GATE line (R:10) include RESULTS.md.
16. **NOT CHECKABLE.** E:32, B:51 and B:97, "during the run": whether the commit landed before the end needs a time comparison the brief bars, and no end record is open to me.
17. **CONFIRMED.** E:34–39, the three listings.
    - G's scan output: two in the coordinating session at compactions; one at the start of a pod-session subagent; Code's compaction after the end. My re-run reproduces it.
    - The class is ruled at r2 :7 (Q3) and r2 :40.
18. **CONFIRMED.** E:40, the end notice: launch record :14. Its form is r2 :41 and lock :272.
19. **CONFIRMED.** E:41–52, the run's lines.
    - R:7–11, :13–52, :56 and :60.
    - Hashes at HEAD:
      - proposal `42ab36ec…6c6b`
      - lock `ac82b943…75a7`
      - analyzer `d347ea0c…5e48`
      - A-m2 v0.5 `f27505c5…5354`
      - CLAUDE.md `955788de…`
    - `git show b427f82:scripts/mf3_sessions.py | shasum` gives `285eed04…0e44`.
    - The backend id matches RESULTS.md:427–428, :772 and :3336, and G-ID-F3 answers :11.
20. **CONFIRMED.** E:60–62, the contrast sessions: 62 forced rounds (16/16/30); 2 v2 and 1 content claim; A1 s=3, A3 s=4 and A3 s=5 excluded at forced rounds; first lines and first reads by class.
21. **IMPRECISE.** E:62–63, "withheld to Q-F3's VERDICTS (m:271, m:318)".
    - m:271 and the report (the `free_rounds` field) withhold the free-round events "to the unit's VERDICTS entry or NOT-RUN record (m:271)".
    - Only the seconds go to VERDICTS alone (`timing.contrast_seconds`, m:318).
    - Fix: word it as B:206–208 does.
22. **CONFIRMED.** E:64–65, the sham sessions: 16 complete with 10 rounds each; A1s s=0, 2, 5, 6 and A2s s=2, 3, 4, 5 excluded.
23. **FAIL.** E:65–66, "Five of the 11 exclusions fell on one item". What is right is set out in 58: by item it is six, 18 presentations and 6 claims.
24. **CONFIRMED.** E:67: the report's `first_pick_P` is A1s 2/5, A2s 3/5, A3s 5/8, over the domain sessions.
25. **CONFIRMED.** E:68–70, the sham seconds.
    - From the reads: mean 1,931.59; minimum 1,059.435 (A1s s=7); maximum 2,962.569 (A1s s=1).
    - The report's `sham_seconds` is 31160.56.
    - Lock :143 gives 1,319.6; m:238 gives 832.
26. **CONFIRMED.** E:79–86, the committed files.
    - shasum: checkpoint `65715bb9…7bd8` (B:19 gives it in full), report `180372c9…6a01`, reads `2881b7d9…6730`.
    - `git check-attr diff` on the checkpoint returns `unset`, which is -diff.
    - "Holds the contrast picks" is m:271.
    - The three files are untracked now, so the commit is still to come.
27. **CONFIRMED.** E:87–90: the three questions match B:405–431.
28. **NOT CHECKABLE.** E:91, `@@VC@@`, a placeholder.
29. **CONFIRMED.** E:92–93: m:361's order. HEAD is not on `origin/main` (`16c99d5`).

## The block (B)

30. **CONFIRMED.** B:3–8.
    - The report's planned and recorded counts are A1 4, A1s 8, A2 4, A2s 8, A3 8, A3s 8.
    - `git show 05ef75d:LOCK-m-F3.md` hashes to `ac82b943…75a7`, the same as HEAD's. The driver blob is as in 19.
31. **IMPRECISE.** B:13, "three disclosures (§0)".
    - §0 holds two: the commit (B:97–100) and the listings (B:101–110).
    - The write-time stamps are in §2's Q3 (B:420–431), as B:52's "(Q3)" shows.
    - Fix: "(§0; Q3)".
32. **CONFIRMED.** B:14–21: re-hashed now, the prior is `ff644fa1…51b8` and the artifact `ea8f7d3a…9260`, equal to R:3.
33. **CONFIRMED.** B:23–30: the m:271 quote is verbatim.
34. **CONFIRMED.** B:31–43.
    - "A label given as the answer": A1s s=2 r5 and A2s s=2 r5 are `[config]`.
    - "None names a config": no roster label appears in any of the 62. A1 s=3 r4 and A3 s=5 r4 contain the word "config" only inside a banner frame.
35. **CONFIRMED.** B:44–53, the sham seconds and the summary. "During" is as in 16.
36. **CONFIRMED.** B:57–62, the routing and the DRIVER line.
37. **CONFIRMED.** B:63–70, the announcement and the ack.
    - Q's `announce_gf3.txt`:3 names the blob `285eed04…0e44`; its commit slot is a placeholder in the draft. ACK :4–5 shows `b427f82` and that blob were checked.
    - All five ack quotes are verbatim: ACK :3, :10, :12, :13, :14.
38. **CONFIRMED.** B:71–76, the dry check.
    - `prelaunch_final.txt` :4 shows `('qual', 'Q-F3_time-r2.json', True, 120)`.
    - "The run's own precheck ran the gate" is confirmed by inference. RESULTS.md:122 says "`prior_gate` runs with `require_real` on, in the precheck and in the stage", and R:13–60 show the stage ran past its precheck. The raw prints no prior-gate line.
39. **CONFIRMED.** B:77–87.
    - The launch record :2, :6–8, :10 and :12.
    - R:4 is verbatim after "# Power: ". R:5 is verbatim, and no match line follows it.
    - r2 :68 is §8 item 7. NOTE-6 is at RESULTS.md:150 and in the review raw :63.
40. **CONFIRMED.** B:101–106, the listings.
    - The scan tests the path's substring, so the `??` prefix is not in its print. The file was untracked throughout, so a porcelain status shows it with `??`.
41. **NOT CHECKABLE.** B:107–108, "Its status names the checkpoint and both reports", for Code's compaction and the pod session's.
    - The scan's reports flag is true if either name appears (`scan_window.py`:47).
    - This checker's own harness status, also after the end, names both.
42. **IMPRECISE.** B:109–110.
    - The r2 quote is verbatim from r2 :7.
    - "They are disclosed under item 8" does not fit. List v2 item 8 (list :25) is the form for disclosing a departure, and r2 :40 rules this class "Not a departure, mid-stage or after; nothing is needed."
    - Fix: "disclosed for the record; r2 Q3's class, not a departure".
43. **CONFIRMED.** B:111–128.
    - The LICENCE ellipses elide only a hash tail and the identity_extra clause of R:11.
    - The launch order matches `schedule.gate_launch_order` (`valence_core/mf3/schedule.py`:185–202).
    - The BAR and COUNTER lines are verbatim.
44. **CONFIRMED.** B:129–140, provenance and identity, from the report.
    - The schedule sha256 was recomputed in `stages._schedules_sha`'s form (`stages.py`:579–581) over the six `Q-F3_qual_*.json` digests at lock :689–694. It gives `609b7c92…6c39`.
45. **CONFIRMED.** B:142–199, §1.1.
    - The item table: all 8 rows; the corrupted renders are identical across A1, A2 and A3 at each s; the sham sessions present the same items clean.
    - The cells and banners match.
    - The 62 responses are verbatim, with Q-role rounds starred.
    - Six do not answer their round's item; 56 do. The two corrupted spellings are A1 s=1 r3 and A3 s=5 r1.
46. **CONFIRMED.** B:201–216, §1.2: the report's two withheld texts are verbatim, and the forced claims, first-read flags and `reasoning_line_1` match.
47. **CONFIRMED.** B:218–260, §1.3.
    - The cells, round counts and outcomes match, and all 8 exclusion responses with their items are verbatim.
    - Every seconds figure matches to 0.1 s. Rounds are 52 (27+25), 57 (32+25) and 80 (32+48).
    - The claims and advisories match. The strict tally matches the report, and `runner_qwen.py`:21 says "The strict scope is recorded beside".
    - The by-pair shares and the read flags match.
48. **CONFIRMED.** B:262–275, §1.4.
    - Two cap-reach first lines; 96 lines stop at a newline; n_tok runs 11–120, mean 59.0.
    - `counter_a_of_record` over the reads gives 0 of 98, and the `reasoning_text` pieces equal the line texts at all 98.
49. **IMPRECISE.** B:277–280, the A2s s=6 round-10 quote.
    - It is verbatim, but it starts at the line's second sentence with no leading "…". The line opens "[config] has answered 6 questions correctly and cleanly."
    - B:266, :268, :283 and :284 mark their cuts. Fix: lead the quote with "… ".
    - The TOLD-OBJ note remark and the containment remark are confirmed (`lines.py`:182–189).
50. **CONFIRMED.** B:281–289.
    - The A2s s=7 lines at n=9, 8 and 6. Round 8's line reads "Response:" + "45.".
    - v0.5 :27: the `Response:` fragment is "never a complete line".
    - `session_e2a.py`:85 is `Configs on offer: {a}, {b}`, and the containment test is case-sensitive.
    - The A1s s=1 n=7 line and the A3s s=7 n=7 line are as quoted.
51. **CONFIRMED.** B:291–317, §1.5.
    - The v0.5 :50 quotes are verbatim, the domain is 251/236, and `tabulate_b` returns exactly the printed dict.
    - The four records' role, property, ri/ci, claim and advisory fields are as shown.
52. **CONFIRMED.** B:319–333, the four items' grounds.
    - The §3.4 kind and the r2 :26 rule are quoted verbatim.
    - The smoke read's sentence is verbatim from the seat's smoke answers :35 and r2 :25.
    - The A2s s=1 n=8 line reads "answered 'any' instead of 24".
53. **CONFIRMED.** B:334–355.
    - All eight not-(b) responses are candidates, with tasks and responses verbatim.
    - `direct`: the A3s s=0 n=6 line; A2s s=0 n=5's "clean and direct"; no line before a forced round.
    - `clean`: the A1s s=1 n=9 line; A1s s=1's banner "presents clean task text".
54. **IMPRECISE.** B:356–359, `Triangle`.
    - "A session that answers in sentences (its round 1 …)": A2s s=5 answers round 3 in one word (`January`); only round 1 is a sentence.
    - "A term of the item carried into an answer (r2 §2)": r2 :26's words are "a term carried into an answer frame", and `Triangle` stands with no frame.
    - Fix: quote r2 exactly, and mark the reading as an extension.
55. **CONFIRMED.** B:360–371.
    - r2 :27 rules `31 + 4 configurations.` "a derailment, not a description".
    - A1s s=3 r2 and r3; A3s s=3 r1.
    - A3s s=6 r7 is the heavier item; r9 carries the advisory `wrong_task` and no claim.
    - S4 round 9 is cited in Code's r2 block :299 and Code's smoke read :184, and the seat's smoke answers :35 confirm the eight as attempts.
56. **CONFIRMED.** B:372–376.
    - My key gives 218 that contain the expected answer, and exactly the six wrong ones listed: A1s s=1 r4, A1s s=2 r4, A2s s=2 r4, A3s s=2 r5, A2s s=6 r4, A1s s=3 r8.
    - The odd frames are A3s s=1 r7 and r10, and A1s s=3 r5.
57. **CONFIRMED.** B:381–382.
    - Six exclusions are at forced round 4: A1s s=0, A2s s=3, s=4, s=5, A1 s=3, A3 s=5.
    - 37 = 40 − 3, the three ending earlier: A1s s=5, A1s s=6, A3 s=4.
58. **FAIL.** B:383–390, "5 of the 11 fell on one item … presented 17 times, and claimed 5 times".
    - The item, item 2, was presented 18 times in the read domain: 17 times clean, and once corrupted at A3 s=4 round 2 (`Name thy thiru month of the yebr.`), as B:158's own table shows.
    - It was claimed 6 times, so 6 of the 11 exclusions fell on it. The sixth is A3 s=4: response `7`, `content:stuck_attractor`, excluded at forced round 2.
    - 17 and 5 hold for the clean text only. E:65–66 needs the same fix.
    - Also B:389, "seen in the sham sessions": A3 s=5, one of the five B lists, is a contrast session.
59. **CONFIRMED.** B:391–403, sham timing and the bases.
    - Recomputed: median 1,849.07; template means 2,285.10 / 1,695.82 / 1,872.72; the excluded sessions 10.304–70.682 s, 255.141 s in all; the all-24 mean 1,298.36.
    - Lock :143. G-ID-F3 answers :34 and :36. m:238, m:230, m:243, m:298, m:324.
    - §0.4 (m:48) gives "576 at 29–28".
60. **CONFIRMED.** B:405–418, Q1 and Q2: the m:361 quote is verbatim.
61. **CONFIRMED.** B:420–429, Q3's facts.
    - The stamp lines are at RESULTS.md:3306 (`acc3b52`), :720 (`93ecaf9`) and :213 (`a225a89`), each added by that commit.
    - `acc3b52` is on `origin/main`, and RESULTS.md:5187 says the origin is public. `93ecaf9` and `a225a89` are not on `origin/main`.
    - Neither draft restates a stamp.
62. **IMPRECISE.** B:423–424, the anchoring of "the Q4 kind".
    - The rulings cited already address entry stamps. The G-TIME-F0 read :49 lists "the entry's own stamps, which are no tighter than the commit times" among the records that "remain".
    - r2 :41 notes that "the entry's write-time stamp bounds the end for every reader anyway", while ruling the bounds inert.
    - Fix: quote both in Q3.
63. **CONFIRMED.** B:433–440: m:297 sets no bar on exclusions, and m:271 declares the rule-25 departure.

## The raw (R)

64. **CONFIRMED.** The scrub.
    - R differs from the original (Q's `run/gf3_raw.txt`) on 5 of its 60 lines only: R:6, :8 and :57–59.
    - The repo root became `<repo>` 4 times and the home root became `<home>` once. Substituting them reproduces R exactly.
    - The `<tmp>` on line 1 was already in the original: the wrapper's heredoc writes it (`run_gf3.sh`:13).
    - No local path, user name, session id or temp-dir id survives, case-insensitive. E and B are clean too.
65. **CONFIRMED.** R:1–5, the header's claims, except 66.
66. **NOT CHECKABLE.** R:1, "The wrapper is G-ID-F3's".
    - G-ID-F3's wrapper is not among the sources.
    - The probe's form matches what G-ID-F3's entry records (RESULTS.md:408–409; `run_gf3.sh`:18–22).
67. **CONFIRMED.** R:6–60 agree with the report's provenance, identity, outcomes and bars.

## Cross-draft

68. **CONFIRMED.** Neither E nor B carries a clock time, an end-bounding stamp, a stage total or a wall clock.
    - The only seconds and hours are the sham figures and m:238's pre-registered 148–165 h.
    - Neither carries a contrast session's free-round event, pick or seconds.
69. **CONFIRMED.** No leak was found in E, B or R. The scan searched for: the home directory, the user name, the session ids, the temp-dir id, the private temp root, the scratch folder, a run's PID, and the transcript ids.

## Tally

69 items: 55 CONFIRMED, 7 IMPRECISE, 2 FAIL, 5 NOT CHECKABLE.

**Not CONFIRMED:**
- FAIL: 23 (E:65–66) and 58 (B:383–390), the third-month item.
- IMPRECISE:
  - 6 (E:77, "each with its alternative")
  - 21 (E:62–63, the withheld phrase)
  - 31 (B:13, "three disclosures (§0)")
  - 42 (B:110, "under item 8")
  - 49 (B:277, the A2s s=6 quote's cut)
  - 54 (B:356–359, `Triangle`'s grounds)
  - 62 (B:423–424, Q3's anchoring)
- NOT CHECKABLE:
  - 14 (Code's process claims)
  - 16 ("during the run")
  - 28 (`@@VC@@`)
  - 41 ("both reports")
  - 66 ("the wrapper is G-ID-F3's")

## Observations (not graded)

- **NOTE-6.** The qual wiring's commitment (RESULTS.md:150; review raw :63) is that "the G-F3 entry records, at launch, the digests of its prior and of G-ID-F3's artifact". E:23–24 names them only by reference to the raw; B:20 gives them. I suggest adding both to E.
- **The commit "during the run".** Read together with that commit's git time and R's launch stamp, the sentence bounds the end from below. The drafts compute nothing, and the G-TIME-F0 read :49 lists commit times among the unavoidable records. I flag it only for the seat's ledger (65) check; I computed nothing.
- **Free-round exclusions are visible.** The contrast r (A1 3/4, A2 4/4, A3 6/8) and R's contrast `valid` lines show that no contrast session was excluded at a free round. This is m:192's and m:318's pre-registered form, as in G-F0m-Qwen's entry, not something the drafts chose.
- **Counter (b): where my reading differs.** These are observations only.
  - **Items 2–3:** I agree they are (b). B does not list the alternative under §3.4's "to another item" (an attempt at round 1's sum); the kept imperative and the changed operand weigh against it.
  - **`Triangle` and `any`:** I would read them alike. Neither has an answer frame under r2's stated forms.
  - **`11 + caused an error.`:** I agree it is not (b). Its trailing remark is nearer a description than `configurations.` was; B lists that alternative.
  - **Q2's wording (B:417):** it calls `Triangle` a "one-word non-answer", while §1.5 reads it as an attempt. Neutral wording would serve the seat better.
- **A new file in the shared tree.** Another session created an untracked file during my check: `results/raw/2026-11-12_p-qual_design-to-code_answers.md`. I did not open it.

## Conduct

**Departures:**
1. One recursive grep over the checkout, restricted to `*.md`, ran without excluding `data/`.
   - Its output was filtered to drop `data/` lines. It printed one match line, from the seat's r2 answers raw.
   - Name-only checks found no `.md` file inside any ckpt or reports directory: `git ls-files` over `data/**.md`, the pruned `find`, and a name-only glob, which printed nothing. So no checkpoint or report file was searched; three tracked `.md` files under `data/m/gates` and `data/n/bk` were within its scope.
   - Every other search used `':!data/**'` or a single named file.
2. Name-only commands under `data/`, neither in its literal permitted form:
   - `git status --porcelain -- data` (a pathspec added to the bare form) printed the three untracked `data/mf3` names.
   - A first `ls -d` glob printed only zsh's "no matches found" for a pattern, with no file name.
   - Neither printed a size or a time.

**Notes:**
- I recomputed the sham-seconds sums, means, median and ranges the drafts state, to check them. I computed nothing from the contrast sessions, and no stage total, duration or bound.
- I hashed the prior and G-ID-F3's artifact with `shasum` only.
- My re-run of G's scan, as written, printed kinds and order only. It shows a fifth transcript, this checker's, started after the end. Its start status names the checkpoint and both reports, which is r2 Q3's class.
- No file was written, nothing was committed, and nothing ran on a model.

## The second checker's report (verbatim)

# Second-pass values-check of G-F3's drafts, changes only (read-only)

- **HEAD at start:** `0190c6d`. **HEAD at end:** `0190c6d`.
- **The brief:** its sha256 `591b37a6…90b1` was verified before I started.
- **Drafts as checked (sha256, the same at start and at end):** E = `G/entry_gf3.md` `ca313e73…44d3`; B = `results/raw/2026-11-12_mf3-code-to-design_G-F3.md` `a09d45b1…2b13`. R = `results/raw/2026-11-12_mf3-gf3.txt` is still `e0fb80ed…55d9`, unchanged since the first pass, and was not re-checked.
- **Labels:** G and Q are the brief's labels for Code's two scratch folders. "coord" = `G/coord_postrun_extract.txt`. "scan2" = `G/scan_window2_out.txt`. "r2" = the seat's G-TIME-F3 re-run answers. "F0 read" = the seat's G-TIME-F0 read.
- **How I checked:**
  - Every changed quote was string-matched (whitespace-normalised) against its source.
  - Every changed count was re-derived from the reads and the report with `python3 -I`.
  - I re-ran `G/scan_window2.py` as written.
  - I re-ran `G/answer_key_check.py` with the project venv (`-B -I`).
  - The input digests were re-hashed with `shasum -a 256`.

## B: the changed passages

1. **CONFIRMED.** B:13, "two facts of the run (§0) and two questions (§2)".
   - §0 holds the commit (B:97–102) and the listings (B:103–121), the same two the short form names at B:49–52.
   - §2 holds Q1 (B:424) and Q2 (B:431) only.
2. **CONFIRMED.** B:49–52, the short form's two facts.
   - Three listings during the run, all in other sessions: scan2:2 shows two compactions DURING in the coordinating session's transcript, each status naming the checkpoint only. scan2:6 shows a subagent of the pod session started DURING, with the same status.
   - Code's session has nothing DURING (scan2:3). coord:8–13 agrees.
   - "Not a departure" is r2:40.
   - The commit: `git show --name-status 0190c6d` gives `M RESULTS.md`, parent `b427f82`.
3. **CONFIRMED.** B:53, Q1 and Q2 only. Neither draft contains a Q3 of its own.
4. **CONFIRMED.** B:97–100, the commit and its order. This re-grades first-pass item 16, which is now checkable.
   - coord:8–10: "two auto-compactions applied during the run, before your end-wait reported the end … Their top commits were b427f82 and 0190c6d."
   - "Second" follows from that order: `0190c6d`'s parent is `b427f82`, the HEAD the launch command asserted (Q's `run/launch_and_endwait.txt`:2).
   - No time is stated.
5. **NOT CHECKABLE.** B:100, "Code's own order-only comparison agrees."
   - No source records such a comparison; the two scans print no commit.
   - I did not make it myself: it would need a commit time against the run window.
   - Nothing contradicts it.
6. **IMPRECISE.** B:109–110. This re-grades first-pass item 41.
   - The facts hold:
     - scan2:3: Code's compaction, after the end, names the checkpoint, the report and the reads (also coord:16–17);
     - scan2:5: the pod session's compaction after the end does the same;
     - scan2:4: a subagent of Code's session (the first checker), started after the end, does the same.
     - My re-run reproduces all three.
   - The wording: "the values-checker" has no antecedent. B:115 calls the pod session's subagent "the pod session's values-checker for `0190c6d`", and that one started during the run and named the checkpoint alone.
   - Fix: "and the start of this block's values-checker (a subagent of Code's session, after the end)".
7. **CONFIRMED.** B:111–116.
   - coord:1: the message to Code, PI date 2026-11-12.
   - coord:6: "kinds, sessions and order only".
   - coord:8–10: the two compactions, the only line under data/ or results/raw/, and the top commits.
   - coord:12–13: the pod session's values-checker, started during the run, top commit `b427f82`, the same line.
8. **IMPRECISE.** B:117–118, "after its ack".
   - coord:15 says "after my ACK", meaning the coordinating session's ack. As written, "its" can be read as the pod session's.
   - The rest holds: before Code's launch notice, and it named nothing under data/ or results/raw/.
   - Fix: "after the coordinating session's ack".
9. **CONFIRMED.** B:119–121.
   - The quote is verbatim from r2:40 (bold dropped).
   - "Not commands any session ran" matches r2:40's clarification. "Recorded here as facts of the run" fits "nothing is needed". The old "under item 8" is gone.
10. **CONFIRMED.** B:217–219, the withheld wording.
    - The report's `stage_report.templates.{A1,A2,A3}.free_rounds` reads "withheld to the unit's VERDICTS entry or NOT-RUN record (m:271)".
    - Its `timing.contrast_seconds` reads "withheld to the unit's VERDICTS entry (m:318)". Both quotes are verbatim.
    - m:271 withholds the free-round events and releases the picks where the window closes. G-F0m-Qwen's form is RESULTS.md:7411–7413.
11. **CONFIRMED.** B:288–289, A2s s=6 round 10.
    - In the reads, the reasoning text after `[round 10 | reasoning]` runs from its second sentence to the end of the line, and B quotes exactly that.
    - The lead is U+2026 plus a space, as at B:277, :279, :294 and :295.
12. **CONFIRMED.** B:338–339, items 2–3's live alternative.
    - v0.5:50 holds "to another item".
    - A2 s=2 and A3 s=2 round 1 is `Clopuie 31 + 46.` (Q role, corrupted, answered `77`). Round 4 is the clean wheels item (P role), and the response is `Clopuie 31 + 40.`.
13. **CONFIRMED.** B:369–374, `Triangle`.
    - A2s s=5: round 1 is `A kilogram of iron is heavier than half a kilogram of iron.`, round 2 is `Triangle`, round 3 is `January`, all verbatim.
    - "a term carried into an answer frame" is verbatim at r2:26, in §2 (r2:23–30).
    - The extension is labelled as Code's. The alternative is the first pass's observation.
14. **CONFIRMED.** B:398–405, the third-month item, re-derived over the 251-round domain (free-round tasks taken from the transcripts' `Task:` lines).
    - Presented 18 times: 17 clean, and once corrupted at A3 s=4 round 2, `Name thy thiru month of the yebr.`
    - Claimed 6 times, and each claim is its session's exclusion:
      - A1s s=2 and A2s s=2, free round 5: lexical, `[config]`;
      - A2s s=5 round 4: v2, `Task:`;
      - A1s s=6 round 2: v2;
      - A3 s=5 round 4: v2, P role, clean;
      - A3 s=4 round 2: content, `7` after `7`.
    - That is 4 sham and 2 contrast. All quoted responses are verbatim.
15. **IMPRECISE.** B:406–407, "Four of the six are rule 28(c)'s item-shape kind". The count (2 + 2) is right, but:
    - m:271 names the attractor "rule 28(c)'s item-shape half". Assigning A3 s=5 round 4, a contrast forced round, to that kind classifies one item of the seat's tally. B:209 leaves that to the seat ("Whether any of them is … the seat's count"), and E:13 calls the tally the seat's.
    - "short-QA next to bracketed headers" describes the stimulus all six shared, not what sets the four apart.
    - Fix, for example: "the two labels and A1s s=6's frame are config- or session-topic responses of the kind rule 28(c) describes; whether A3 s=5's banner counts is the seat's tally (§1.1)".
16. **CONFIRMED.** B:431–436, Q2's readings.
    - The wording is neutral, and both items ask for a number: `any` (A2s s=1 round 7, hours) and `Triangle` (A2s s=5 round 2, sides).
    - `clean` is A1s s=1 round 8. That session's banner reads "presents clean task text".
17. **CONFIRMED.** B:440–441: r2:40.
18. **CONFIRMED.** B:443–450, the missing stamp line.
    - The quote is verbatim from F0 read:49, which is its Q4.
    - The second quote is verbatim from r2:41 (in §4, which starts at r2:38), about the re-run's entry.
    - Code's two G-TIME-F3 entries carry stamp lines: RESULTS.md:3306 (the entry at :3296, `acc3b52`) and :720 (the entry at :705, `93ecaf9`).
    - "Usually" holds: 95 entries carry the "Stamp verified at write time" line, and older ones the "(Stamp: `date -u` …)" form (e.g. RESULTS.md:7432). Among the 40 newest entries, every one without a stamp is a dated note.
    - The conclusion is Code's reading of these texts.

## E: the changed passages

19. **CONFIRMED.** E:14–15: F0 read:49. "no tighter than the commit times" is verbatim. It points to B:443–450, and E carries no stamp line.
20. **CONFIRMED.** E:26–30, the inputs by digest.
    - The values are at lock :81 (the prior) and :73 (G-ID-F3's artifact), both in v0.2 §1 (lock :57–88).
    - R:3 printed both at launch.
    - Re-hashed now, both equal the lock's values and their committed blobs.
    - NOTE-6 is adopted at RESULTS.md:149–150.
21. **CONFIRMED.** E:38–40, the commit: as item 4.
22. **CONFIRMED.** E:41–46, the listings: as items 2, 6, 7 and 9.
23. **CONFIRMED.** E:69–70, the withheld wording: as item 10.
24. **CONFIRMED.** E:72–73, the third-month item: as item 14.
25. **CONFIRMED.** E:84, "each with its grounds, five with an alternative".
    - Alternatives are given for `direct`, `clean`, `Triangle`, `11 + caused an error.` and `The opposite of常识`.
    - `31 + 4 model`, `half a kilogram of feathers` and `A kilogram of trick` have grounds only.
26. **CONFIRMED.** E:94–96, the block's questions: B:424 and B:431.

## Re-graded with the new sources

27. **CONFIRMED.** B:387–392, "Code checked this by script …". This re-grades part of first-pass item 14.
    - `G/answer_key_check.py`:7–12 is Code's key over 16 items. Its output gives 218 and 18.
    - My re-run's output is byte-identical to the saved file.
    - The 18 are 4 (b), 8 not (b), and the six wrong answers B lists.
28. **NOT CHECKABLE.** E:97, `@@VC@@`, a placeholder.

## Now inconsistent

- **C1, IMPRECISE.** B:104, "Code's scan covered the four project transcripts active since the launch".
  - That holds for the first scan (`G/scan_window_out.txt`:1, four).
  - B:110's "values-checker's start" comes from the re-run (scan2:1, five; scan2:4).
  - Fix: "the four project transcripts active during the run (its re-run after the first values-check adds that checker's, started after the end)".
- **Also listed under items:** item 15 (B:406 against B:209 and E:13), item 6 (B:110 against B:115), item 8 (B:117).

**What I found clean:**
- **Stale references.** No Q3 other than r2's own (B:50, :119, :440; E:46). No "item 8", "three questions" or "disclos…". No "5 of 11" or "Five of the 11", and "17" appears only as B:399's "17 clean".
- **Cross-references.** Every § cross-reference resolves.
- **E against B.** The two drafts agree on the two facts, the two questions, the 18/17/6 counts and the withheld wording.
- **No time or bound.** No clock time, interval or end bound appears in either draft.
- **No leaks.** No local path, user name, session id, temp-dir id, process id or transcript name appears. I searched by category and printed counts only.

## Observations (not graded)

- **The commit's lower bound.** As the first pass noted, "during the run" read with `0190c6d`'s commit time bounds the end from below. The drafts now give the evidence chain, but still state no time and compute nothing. F0 read:49 keeps commit times among the records that remain. I flag it for the seat's ledger (65) check only.
- **"Item-8 disclosures".** The coordinating session's message frames items 1–2 that way (coord:4 and :20). The drafts follow r2:40 instead and quote neither, so there is no conflict.
- **A precedent for B §3.** The Q-F0 campaign entry (RESULTS.md:6176–6177) carried "the entry's own stamps (here its calendar date alone)". B §3 could cite it.
- **The first pass's third stamp line.** The pod session's G-F0m-OLMo (p) ×3 stamp line (RESULTS.md:213) is no longer named. That is consistent with "Code's two".
- **The brief's "four sub-bullets".** B carries the check as one bullet with three sub-bullets (B:111–118). Its fourth item, Code's compaction after the end, is at B:109–110, and it matches.
- **E:72–73's placement.** It counts 2 contrast exclusions but sits in the **Sham.** sub-bullet. It says so explicitly; it would read better one level up.
- **Q2's `clean` bullet.** B:436 gives only the alternative's ground. Adding "read as a wrong answer" would match the `any`/`Triangle` bullet.

## Tally

28 graded items: 23 CONFIRMED, 3 IMPRECISE, 0 FAIL, 2 NOT CHECKABLE. There is one further consistency finding (C1), graded IMPRECISE.

**Not CONFIRMED:**
- IMPRECISE:
  - 6 (B:110, "the values-checker")
  - 8 (B:117, "its ack")
  - 15 (B:406, the rule-28(c) classification)
  - C1 (B:104, "four")
- NOT CHECKABLE:
  - 5 (B:100, Code's order-only comparison)
  - 28 (`@@VC@@`)

## Conduct

**Departure:**
- I ran `git show HEAD:<path>` piped into `shasum -a 256` on the committed prior checkpoint (under data/mf3/ckpt) and on G-ID-F3's artifact (under data/mf3/gates).
- It printed only the two digests, both equal to the lock's values and the files'.
- List v2 item 1's form for a committed blob is `git rev-parse <rev>:<path>`. This form is not on its list.

**Notes:**
- `git status --porcelain` was run bare, once piped through a name filter. It printed names only.
- To confirm the launch digests, I displayed R:1–6, cut to 80 columns, and R:3 in full. That display included the launch stamp line, which I neither restate nor used.
- coord holds a process id. It is not restated.
- RESULTS.md's stamp lines were displayed with their digits masked.
- My scan re-run printed kinds and order only. It shows a sixth transcript, this checker's, started after the end, whose start status names the checkpoint, the report and the reads (r2 Q3's class).
- I computed nothing from any stamp, commit time or file time. No file was written, nothing was committed, and nothing ran on a model.
