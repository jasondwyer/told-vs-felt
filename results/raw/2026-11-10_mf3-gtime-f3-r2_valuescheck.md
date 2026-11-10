# G-TIME-F3's re-run — the values-check of the block, the entry and the scrubbed raws

*Code's raw, PI date 2026-11-10.*
- *What was checked:* Code's block for the seat, the entry draft, the stage's scrubbed raw and the scrubbed output of the
  mf3 self-test after the lock's re-issue.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written (brief sha256
  `e19d7302…`, 51 lines).
  - It read the stage's two report files for the drafts' figures, and hashed the checkpoints.
  - It saw Code's transcript only through Code's extract script, which masks the end notice's clock times.
  - By its report, the main checkout's HEAD was `f674583` at its start and end.
- *Outcome:* 100 items: 80 CONFIRMED, 8 IMPRECISE, 2 FAIL, 10 NOT CHECKABLE.
  - The FAIL and every IMPRECISE item are applied (below).
  - One NOT CHECKABLE item (28) led Code to withdraw a reading.
- *After the pass:* Code added facts from the coordinating session's messages of 2026-11-10, and its answer on PID
  18391. These are the stamp relays, the harness listing at a compaction, and the block's Q3 and Q4. The same agent checked them in a second pass: 38 items (101–138), 27 CONFIRMED, 5 IMPRECISE, 1 FAIL, 5 NOT CHECKABLE.
  - It found all ten of the first pass's applied items resolved.
  - Code applied the second pass's findings (below), each by the checker's stated fix or by narrowing the text to its source. No third pass was run.
- *Code's scan of the checker's transcript* (masked; no output text printed): 82 distinct Bash calls, none in a barred
  metadata form. The calls that name `data/` are of four kinds:
  - `shasum` digests;
  - reads of the two report files;
  - `git check-attr` and `git rev-parse` (its disclosures 1 and 2);
  - `git grep` with `':!data/**'`.
- *This raw:* Code's dispositions, then the report verbatim. It was extracted by script from the agent's hand-back. It
  holds no local path and no clock time.
- *Nothing ran on a model.*

## Code's dispositions

- **35 and 83, FAIL: "Code has computed no bound from it".** Agreed.
  - The end notice as sent stated a five-minute window on the end, from the end-wait's poll.
  - The checker could not see that Code's own reasoning, weighing why the stamp mattered, also worked out the interval
    from the launch to the end-wait's stamp. From it and the sham seconds, that reasoning reached a loose upper bound on
    the contrast sessions' combined seconds. No tool printed either figure, and no message carried one.
  - Applied in the block (§0) and the entry: both are disclosed as Code's departures from the seat's G-TIME-F0 read,
    Q4, and go to the seat as the block's Q4.
- **32 and 81, IMPRECISE: the stamps the end notice carried.** Agreed. Applied: the notice carried the launch time,
  the end-wait's stamp and a later `pgrep` check's stamp, beside the window.
- **21, IMPRECISE: the process-line quote drops a byte.** Agreed: raw:3 holds a backspace byte (0x08) before `u`.
  Applied: the quote marks it as `␈`, with a note. The committed raw keeps the byte, verbatim.
- **23 and 28, NOT CHECKABLE: PID 18391's identity and "the tool shell's preamble".** Code checked its own tool
  shell's argv after the run. It begins `/bin/zsh -c source <home>/.claude/shell-snapshots/…`, the form the checker
  found for its own shell.
  - So the `{ case "${BASH_VERSINFO-}"…` form is not Code's tool shell's, and Code withdraws its reading that PID 18391
    was its launch shell.
  - No other `zsh -c` shell was running to compare when Code checked.
  - Code asked the coordinating session whether the shell was its own or the pod session's. Its answer: neither, "as far as both transcripts show". The block records PID 18391 as unidentified.
  - None of Code's own background calls was open at the launch (Code's check; the extract's sections (12) and (13)).
- **79, IMPRECISE: the entry states Code's reading as fact.** Superseded by 28's withdrawal. The entry now follows the
  block's corrected bullet.
- **62, IMPRECISE: A1s round 4, "an answer to another item".** Agreed. The 16-item task pool has no "60 divided by 4"
  (`valence_core/m/readrule.py:828–834`; its order matches the reads' item fields). Applied: "a wrong answer: it
  divides by 4, not by the task's 5. §3.4's 'wrong' names it".
- **71, IMPRECISE: the m:296 anchor.** Agreed. Applied: "v0.5 §4.1 has LOCK-m-F3 v0.2 record it with this count beside
  (m:296)".
- **73, IMPRECISE: "(rule 25)".** Agreed. Applied: these are "the stripped and redacted reads, which m:271 declares a
  rule-25 departure for the pre-VERDICTS window".
- **85, IMPRECISE: the backend identifier's anchor.** Agreed. Applied: "(the report's identity)".
- **58's and 65's notes.** Applied:
  - the seat's "attempts nothing" quote is anchored to S6 round 8 (`Perfect.`; the smoke answers, §2.1);
  - S12 round 7 is named as the nearest precedent the other way for rounds 9 and 10;
  - A1s round 5's live alternative is given (the "31 + 4 config…" opening, claimed lexical in the first run and in the
    smoke's S10 round 5, each with a label after it). Q2 points to it.
- **36, NOT CHECKABLE: the keep-it-out request.** It is in Code's message to the coordinating session of 2026-11-10.
  The block quotes that session's reply.
- **48 and 53, NOT CHECKABLE: Code's own runs.** The checker reproduced both results with its own code (items 47, 52 and
  54). The block's §3 says so.
- **74, NOT CHECKABLE: "Code did not open the checkpoint".** It is Code's statement. Code ran on it only `shasum`,
  `git check-attr` and a bare `git status --porcelain` (names), all within the list's item 1. It runs `git add` at
  the commit.
- **34, 76, 90 and 92, NOT CHECKABLE: the commit message, the placeholders and the future commit statements.** These
  are filled at the commit. The commit message carries no clock time (checked before the commit).
- **The checker's own disclosures** (the end of its report):
  - Its `git rev-parse` and `git check-attr` on the checkpoints are within the list's item 1. They fall outside the
    brief's narrower bullet.
  - Its mental computation printed and reported no figure (its words). It is the same kind as Code's own (the block's
    Q4).
  - It read the first 60 bytes of each harness shell snapshot. Those files are outside the sources, and it reproduced
    nothing from them.
  - None of its disclosures touches a checkpoint's content, size or time.

## Code's dispositions of the second pass

- **138, FAIL: the commit-message draft still said the opposite of both fixes.** Agreed. It is rewritten to match the
  block and the entry:
  - PID 18391 is a `zsh -c` shell, unidentified, and Code's first reading is withdrawn;
  - the end notice's stamps and window, and Code's reasoning's bound, are disclosed as departures (the block's Q4);
  - the harness listing is disclosed (Q3);
  - the questions are Q1–Q4.
  The message carries no stamp and no window.
- **105, IMPRECISE: the coordinating session's answer, as restated.** Agreed. Applied, in the checker's wording:
  - neither session had a foreground call in flight at the launch;
  - every call of either session whose text named python had ended before it;
  - the coordinating session's own shells take the `source …` form.
- **114 and 133, IMPRECISE: "no committed text restates … the window".** Agreed. Applied: no committed text restates
  the stamps, so nothing committed places the window; the block and the entry give only its width.
- **123, IMPRECISE: Q3 left out the listing at a session's or subagent's start.** Agreed. Applied in §0, in Q3 and in
  the entry:
  - the same status arrives at a start, as it did for the values-check, after the end;
  - Code started no subagent during the stage;
  - the coordinating session's scan looked for compactions, not for starts.
- **128, IMPRECISE: counter (a) "over the redacted reads".** Agreed. Applied.
- **109's residual: the notice's first-line time.** It is the end-wait's stamp, the same one the notice gives later.
  Applied: "the end-wait's stamp (twice)".
- **117 and 135, NOT CHECKABLE: "none applied during the run".** The coordinating session's message names an interval
  that covers the run. The block gives no times. Applied: the scan's scope is now stated, as the transcripts touched in
  the six hours before it, and compactions only.
- **124's two points.** Added to Q4:
  - the stamps also reached the pod session and the PI's chat;
  - the option offered would change the coordinating session's request for a UTC stamp.
- **110, 113 and 132, NOT CHECKABLE.**
  - Code's reasoning is Code's own statement (110, 132).
  - The coordinating session's messages are of 2026-11-10, PI-local, in Code's session (113).
- **The observation, not graded:** Code's earlier note to the coordinating session said the drafts disclose "that no
  bound was computed from it". Code sends the correction with the commit's hash.

## The checker's report (verbatim)

**Values-check of the G-TIME-F3 re-run drafts: 100 items, 80 CONFIRMED, 8 IMPRECISE, 2 FAIL, 10 NOT CHECKABLE.**

- **Brief:** sha256 prefix `e19d7302d2d39728`, 51 lines (`shasum`, `wc -l`).
- **HEAD:** `f674583` at my start and at my end. No commit landed while I worked, and `git status --porcelain` shows no tracked change.

The FAIL appears twice, once in each draft. Both say "Code has computed no bound from it". Code's own end notice states a five-minute window for the stage's end.

**Abbreviations used below:**
- **R:** the brief's scratch dir.
- **Drafts:** blk = R/2026-11-10_mf3-code-to-design_G-TIME-F3-r2.md; ent = R/entry_gtime_r2.md; raw = R/2026-11-10_mf3-gtime-f3-r2.txt; st = R/2026-11-10_mf3-selftest_after-lock-reissue.txt.
- **Stage outputs:** rep = data/mf3/reports/Q-F3_time-r2_report.json; rd = data/mf3/reports/Q-F3_time-r2_reads.json, whose sessions are [0] A1, [1] A1s, [2] A2, [3] A2s, [4] A3, [5] A3s.
- **Extracts:** x(1)…x(7) = the sections tx_extract.py prints.
- **First run and rulings:** gt / gtraw = the first run's block and raw (acc3b52); rul = results/raw/2026-11-08_gtime-f3_design-to-code_answers.md; sk-code / sk-seat = the smoke's Code read and seat read.
- **Documents:** A2 = ADDENDUM-m2-f3-reasoning-block-v0_5.md; L = LOCK-m-F3.md.

All quotes below were matched byte for byte against their sources, after joining line wraps.

## The block (blk)

1. CONFIRMED. blk:1 anchors. m:288 opens "### 3.2 Q-F3" and m:293 is G-TIME-F3.
2. CONFIRMED. blk:3 dates. raw:2 carries the launch stamp's date.
3. CONFIRMED. blk:5-6 (the first run was stopped: 9/13 under m:265 fires). rul:11 reads "The bar reads 9/13 against a critical of 4 at n = 13, and fires. G-TIME-F3 is STOPPED before G-ID-F3".
4. CONFIRMED. blk:6, the re-run that v0.5 §4.3 declares (A2:75).
5. CONFIRMED. blk:6-7, A5's quote, is verbatim from the routing block at RESULTS.md:523. L:9 and RESULTS.md:27-28 quote it the same way.
6. CONFIRMED. blk:9-10, the block's form, matches gt:5-7.
7. CONFIRMED. blk:14-15 (LOCK).
   - `git show --name-status f674583` shows `M LOCK-m-F3.md`.
   - The blob at f674583 equals the working tree's.
   - sha256 is 70da4a70…1d3f.
8. CONFIRMED. blk:16 (ADDENDUM).
   - 7589c1d shows `A ADDENDUM-m2-f3-reasoning-block-v0_5.md`.
   - The blob at 7589c1d equals the working tree's.
   - sha256 is f27505c5…5354.
9. CONFIRMED. blk:17-18, the reads' sha256 859031b0…a066.
10. CONFIRMED. blk:21-22, the r2 checkpoint's sha256 ff644fa1…51b8. `shasum -a 256` was the only thing run on it.
11. CONFIRMED. blk:22-23, the first checkpoint is unchanged.
    - Its shasum is b809c087…8fc7, equal to gt:17's full value.
    - `git rev-parse` gives the same blob id at acc3b52 and at HEAD.
    - It is not modified in porcelain.
12. CONFIRMED. blk:26-31: Qwen, the re-issued lock, uncached, F-b at cap 120, PASS with exit 0, no hair trigger, both bars silent at 0/30 and 0/18 with critical 5, all six valid, the shams at 10 rounds, all six through G-VER.
    - raw:9, :11-21, :25.
    - rep $.status, $.stop and $.stage_report.templates.A*s.hair_triggers; $.bars[0..1]; …A*s.all.rounds.
    - rd $.sessions[*].verified; verify.py:248-252.
13. CONFIRMED. blk:32-33.
    - Counter (a) is 0/18.
    - The first run had 9 of 13 banners plus 2 frames (gt:128-130; A2:13).
    - Every sham line stopped at a newline, and the longest is 78 tokens (rd …reasoning_lines[*].stop_reason / n_tok).
14. CONFIRMED. blk:34-35. raw:20 and A2:71 (§4.1, including "with the re-run's trigger count beside (m:296)").
15. CONFIRMED. blk:36-38, the counter (b) summary (detail in items 51-65).
16. CONFIRMED. blk:44-45, the launch.
    - It used m:267's line: launcher:5 fills m:267's `nohup caffeinate -is … & disown`.
    - x(2) tests that HEAD is f674583.
    - The ACK (x(1), transcript row 22585) precedes the launch (row 22591).
17. CONFIRMED. blk:46-48, :71, :77: all four ACK quotes are verbatim in x(1).
18. CONFIRMED. blk:49-51.
    - The wrapper exports and unsets at :9-10 and writes the raw at :21.
    - raw:1-3 records AC 140 W and "635Gi available on /".
    - raw:8 is the driver's gate line.
19. CONFIRMED. blk:52-54, the self-test passed 182/182 after f674583.
    - x(3) shows rc=0 and "182/182".
    - st:159-161 pass only on the committed re-issued lock. Their BUILD-time counterparts failed at results/raw/2026-11-10_a-m2-v05_build_selftest.txt:161-162, and that raw's last line is 180/182.
    - Both runs list the same 182 check names in the same order; only those two changed from FAIL to PASS.
    - L:187-188 and RESULTS.md:69-70 promised this.
20. CONFIRMED. blk:55-56, the dry check.
    - x(4) shows four empty problem lists and "PRELAUNCH CLEAR".
    - time/prelaunch_check.py:1-9, :17-18 and :23 block the model imports and null the loader, so nothing is loaded.
21. IMPRECISE. blk:57-58, the header's process-line quote, drops one byte.
    - The problem: raw:3 holds a backspace byte (0x08) between `'3') ` and `u`, in both the original and the scrubbed copy. The bracket holds 59 bytes.
    - The cause: `cut -c1-60` kept 60 characters ending in `\bu`, and zsh's `echo` (wrapper:16) rendered `\b` as one byte.
    - Fix: mark the omitted control byte, for example `'3') ␈u;]`. The same byte will sit in the committed raw.
22. CONFIRMED. blk:58: PID 18391's argv begins `/bin/zsh -c`, so it is not a Python process.
23. NOT CHECKABLE. blk:59, "It is the shell that ran Code's launch command". No source records PID 18391's identity. It is consistent with x(2), the launcher and man pgrep, and the block labels it Code's reading at :66.
24. CONFIRMED. blk:59-61. x(2)'s command contains `test -z "$(pgrep -ifl python)"`. Its output prints "no python process" before the launch stamp and PID; strictly, the chained `echo` printed it.
25. CONFIRMED. blk:61-62. man pgrep, under -a: "By default, the current pgrep or pkill process and all of its ancestors are excluded (unless -v is used)."
26. CONFIRMED. blk:63-65, the mechanism.
    - `-f` matches full argument lists, and `-l` with `-f` prints them.
    - The launcher exits right after `echo "PID=$!"` (launcher:6). The wrapper runs git, shasum, pmset, system_profiler and df before its pgrep (wrapper:15-16).
    - x(2) shows `sleep 2`, then `kill -0` and `ps` after the launch.
    - The launcher's exit before the pgrep is an inference; no source records its timing.
27. CONFIRMED. blk:66-67.
    - x(2) gives PID=18397, and `ps` shows it is the wrapper; 18397 − 18391 = 6.
    - The wrapper cuts at 60 characters (`cut -c1-60`); see item 21 for the byte detail.
28. NOT CHECKABLE. blk:67, "which are the tool shell's preamble". No source shows the argv of Code's tool shell.
    - My own Bash tool shell's argv begins `/bin/zsh -c source <home>/.claude/shell-snapshots/…`.
    - The snapshot files begin "# Snapshot file".
    - So the `{ case "${BASH_VERSINFO-}"…` text could not be traced from here.
29. CONFIRMED. blk:68. x(6)'s command names no "python", and gtraw:3 reads `[]`.
30. CONFIRMED. blk:69: x(1)'s check and x(2)'s check both found no python process, raw:3's one entry is a zsh, and m:267's item is "no other model process running".
31. CONFIRMED. blk:72-76, while the stage ran (x(5)).
    - Row 22605 is the end-wait: `kill -0` with a `ps` guard on the wrapper, then a pgrep loop. This is the PID-alone form of list v2 item 5 and RESULTS.md:5242.
    - Row 22605 also has a SendMessage to the coordinating session. The extract prints only its recipient, not its text.
    - Rows 22617 and 22623 are `grep -c` and `sed` on gt, and `git show --name-status acc3b52`. Row 22628 is a wrap_up.
    - No python or model process ran. rul:40 is §7. HEAD is still f674583.
32. IMPRECISE. blk:78, "Code's notice to it carried the end-wait's stamp".
    - The problem: x(7) carries four masked clock times: a "by … UTC" on its first line, the launch time, the end-wait's reported time, and "pgrep for both was empty at … UTC".
    - Fix: say it carried the end-wait's stamp and a later pgrep check's stamp.
33. CONFIRMED. blk:79: neither blk nor ent contains any clock time (pattern search).
34. NOT CHECKABLE. blk:79, "or the commit message": it is not written yet.
35. **FAIL.** blk:80, "Code has computed no bound from it".
    - What the source shows: x(7), as sent, reads "It reported the wrapper gone and no `mf3_sessions.py time` process at <time> UTC, so the end lies within the five minutes before that stamp".
    - That is a bound on the end, from the stamp and the 300 s poll, in the same message as the launch time.
    - What is true: Code computed no duration and no figure for any session.
    - Fix: disclose the window as sent, and keep "no duration, no bound on any session's seconds".
36. NOT CHECKABLE. blk:80-81, "Code has asked the coordinating session to keep it out of committed text". It is not in the end notice as sent, and no extract covers Code's later messages.
37. CONFIRMED. blk:83-94: all 16 backticked stdout lines are full lines of raw (:5-9, :11-21).
38. CONFIRMED. blk:95-96.
    - raw:10 holds the PROVENANCE values.
    - rep $.identity.backend_identifier = a734dadec8f8ce9b. gt:66-67 records the same value and calls it G-TIME-F0's; A2:46 also gives it.
39. CONFIRMED. blk:97-103, the identity.
    - The rep $.identity fields match: lock, proposal, package, weights revision and sha, renders, pool, audit, ban, cap, path and schedule.
    - The schedule is the first run's (gt:73).
    - The quote "the same schedule cells and keys" is verbatim from A2:75.
40. CONFIRMED. blk:104-111, the bars.
    - $.bars[0..1] give n 30/18 and critical 5/5; the planned values are m:271's and m:293's.
    - by_class is 0/0/0, the union of m:265's three classes.
    - The echo class's domain and match follow A2:27.
    - The m:271 quote is verbatim.
41. CONFIRMED. blk:112-115.
    - rep A1/A2/A3 per_session shows 4 forced rounds each and excluded_at_forced false.
    - $.cap_trigger.rule cites F-6; $.timing.contrast_seconds is withheld.
    - F-6 is at results/raw/2026-11-06_ganl-f3_design-to-code_answers.md:29. gt:81-83 uses the same form.
42. CONFIRMED. §1.1 (blk:119-127).
    - The three contrast sessions answered `3` `24` `44` `12` (rd [0,2,4]); rounds 3-4 ran on the Q-role label with corrupted task text.
    - The cells and banners match m:254-257 and gt:89-96.
43. CONFIRMED. A1s (blk:133-153).
    - Every quoted text, `response:` ×12, the token counts 23/23/12/12/12/78, and the advisory on rounds 9-10 with claim null match rd [1].
    - rep shows 1/1 and advisory_rounds 2; 1175.869 s rounds to 1175.9.
    - gt:100-106 has the first run's forced responses and the round-5 `lexical@free`.
44. CONFIRMED. A2s (blk:154-162).
    - The ten responses, the 22–51 range, the round-5 example, and rounds 8 and 10 (the double space included) match rd [3].
    - 1/1; 1041.442 s rounds to 1041.4.
45. CONFIRMED. A3s (blk:163-175): every quote, the 33–49 range, the `provided` lines, 0/1, and 1118.295 s rounding to 1118.3 match rd [5].
46. CONFIRMED. blk:176-179.
    - The shares are rep …first_pick_P, m:318 exception (2).
    - The reads counts match rep …reads, and the first run's match gt:123-124.
47. CONFIRMED. blk:183, counter (a) 0/18 (raw:19). My own containment and echo check over the redacted reads also gives 0/18.
48. NOT CHECKABLE. blk:183, "Code's own containment check … agrees". No extract shows Code running it; its result is reproduced in item 47.
49. CONFIRMED. blk:185-186.
50. CONFIRMED. blk:187-192.
    - A2:71 gives both "no trailing space is added: a changed byte is an untested form" and "stripped as a task response is".
    - In all six transcripts, nothing separates the opener or `Response:` from the model's text.
    - A2s round 8's opening matches.
51. CONFIRMED. blk:196-197: §3.4's blinding-scope quote is verbatim (A2:50), and 30 + 12 = 42.
52. CONFIRMED. blk:198: no audit class claims any of the 42.
    - Every sham round has audit.claim null.
    - The contrast sessions have excluded_at_forced false, so lines.py:209-212 claims none.
    - My stdlib copy of `b_candidates` gives 4+10+4+10+4+10 = 42.
53. NOT CHECKABLE. blk:198-199 and :206, Code's runs of `b_candidates` and `tabulate_b`. No extract shows them. R/counter_b.py makes exactly these calls; I did not run it, since it imports repository code.
54. CONFIRMED. blk:206-207: the code's logic (lines.py:229-253) applied to the three A1s free items gives {"A1s": {"free": 3}}.
55. CONFIRMED. blk:200-201 (L:145; lines.py:205-212).
56. CONFIRMED. blk:202-203: the §3.4 quote is verbatim.
57. CONFIRMED. blk:209-219: ci 3/4/5, claim null, the advisories, the newline stops and the tasks match rd [1].rounds[7..9] and its transcript.
58. CONFIRMED. blk:221-223.
    - The response is `response:` 12 times, and "a header" is one of §3.4's named kinds.
    - The quote is verbatim from sk-seat:35, where the seat said it of S6 round 8 (`Perfect.`). Naming that anchor would help.
59. CONFIRMED. blk:224-229.
    - `90 minus 44` is S12 round 7 and `11 + 3assistant` is S12 round 3 (sk-code:175, :178). Both are among the eight responses that sk-seat:35 confirms as attempts.
    - lines.py:219-221 drops a response only for a claim.
60. CONFIRMED. blk:230.
61. CONFIRMED. blk:235-245 (rd [1].rounds[3], [4]; rd [5].rounds[7]).
62. IMPRECISE. blk:247-248, A1s round 4 "an answer to another item (60 divided by 4)".
    - The problem: no item of the 16-item pool asks 60 divided by 4. valence_core/m/readrule.py:828-834 lists the pool, in the order of the reads' item fields.
    - Fix: "a wrong answer (it divides by 4, not the task's 5); §3.4's 'wrong' names it".
63. CONFIRMED. blk:249-251: S12 round 3 and S10 round 4 (sk-code:172, :175) are among the eight sk-seat:35 confirms.
64. CONFIRMED. blk:252-253: S4 round 9 `A kilogram of trick question` (sk-code:160) is confirmed at sk-seat:35.
65. CONFIRMED. blk:255.
    - The 36 correct answers: the contrast sessions' 12, A1s rounds 1-3 and 6-7, all of A2s, and A3s rounds 1-7 and 9-10. 12 + 5 + 10 + 9 = 36.
    - No other response of the 42 attempts nothing.
    - Notes for the seat, not grades:
      - A1s round 5 ends on the configs' word. The same "31 + 4 config…" opening was claimed lexical in the first run (gt:104) and in the smoke's S10 round 5 (sk-code:209). Reading it as "a description of … its configs" is therefore a live alternative; Code already lists it.
      - For rounds 9-10, the nearest precedent pointing the other way is S12 round 7, a restatement with no result that was read as an attempt. Code's Q2 asks exactly this.
66. CONFIRMED. blk:259-263.
    - DEGEN_CLAIMS["qwen"] is {"v2","echo"} (m/bars.py:85, :897; mf3/bars.py:47).
    - 1 is below the critical of 5.
    - The audit-not-edited sentence is A2:73.
67. CONFIRMED. blk:264-269.
    - The Q5 quote is verbatim (rul:35), as is the §4.4 quote (A2:77).
    - The sham seconds sum to 3335.606 (rep $.timing.sham_seconds) and average 1111.869.
    - m:230 gives the basis; gt:106, :111 and :121 give the first run's seconds.
    - Contrast seconds are withheld.
68. CONFIRMED. blk:273-279: the §4.3 order quote is verbatim (A2:75), and the laptop rule is rul:40.
69. CONFIRMED. blk:281-284: neither sk-code §6 nor sk-seat §2.1 lists an echoed instruction.
70. CONFIRMED. blk:288-289 (A2:71, :84).
71. IMPRECISE. blk:289-290, "m:296 has LOCK-m-F3 v0.2 record it with this count".
    - The problem: m:296 reads only "LOCK-m-F3 v0.2. Cap; path; projections." The count comes from v0.5 §4.1, and "after G-ID-F3" from rul:31.
    - Fix: "v0.5 §4.1 (m:296) has v0.2 record it with this count".
72. CONFIRMED. blk:291-292 (A2:75, A2:50).
73. IMPRECISE (minor). blk:293, "(rule 25)".
    - The problem: m:271 says these stripped and redacted reads "are not the full-transcript reads rule 25 names … a declared rule-25 departure". gt:195 used the same form.
    - Fix: "(rule 25, as m:271's departure scopes it)".
74. NOT CHECKABLE. "Code did not open the checkpoint" (blk:21, :293; ent:52, :69). The extracts cover only the stage window, in which no call touched the checkpoint.

## The entry (ent)

75. CONFIRMED. ent:1-10.
76. NOT CHECKABLE. ent:12, the `@@STAMP@@` placeholder. Once filled, it will be a write-time stamp after the launch. Q4 (driver review :325) lists "the entry's own stamps" among the unavoidable records.
77. CONFIRMED. ent:13-15 (RESULTS.md:523; rul:11).
78. CONFIRMED. ent:16-22 (as items 16-20; "promised here" is RESULTS.md:69-70).
79. IMPRECISE. ent:23-24, "It is the shell that ran the launch command".
    - The problem: the entry states this as fact, while blk:66 labels it Code's reading.
    - Fix: "on Code's reading, the shell …".
80. CONFIRMED. ent:25-29.
81. IMPRECISE. ent:30, "carried the end-wait's stamp", for the reason in item 32.
82. CONFIRMED. ent:30-31, "No committed text restates it" (as item 33).
83. **FAIL.** ent:31, "Code has computed no bound from it", for the reason and fix in item 35.
84. CONFIRMED. ent:32-41.
    - raw has no finish stamp and ends at :25 with EXIT=0.
    - The DRIVER blob at 5d40d59, which modified it, equals HEAD's and the working tree's.
    - The SNAPSHOT, LICENCE and session lines match raw:6-9 and :11-16.
85. IMPRECISE (minor). ent:42-43, the backend identifier.
    - The problem: it is listed under "The run (raw)", but raw does not print it. It is rep $.identity.backend_identifier.
    - Fix: "(the report's identity)".
86. CONFIRMED. ent:44-51: the CAP TRIGGER quote is the tail of raw:20.
87. CONFIRMED. ent:52-59 (rul:35).
88. CONFIRMED. ent:60-67.
89. CONFIRMED. ent:69-72.
    - The hashes match shasum.
    - `git check-attr diff` gives "unset", so the file is -diff.
    - m:271 places contrast picks in the stage's checkpoint.
90. NOT CHECKABLE. The future-tense commit statements (blk:18, :54; ent:68-78, :82): the commit does not exist yet.
91. CONFIRMED. ent:79, :81-82 (m:295, m:296).
92. NOT CHECKABLE. ent:80, the `@@VC@@` placeholder.

## The raw and the self-test, scrubbed

93. CONFIRMED. raw differs from time/gtime_r2_raw.txt only at lines 4, 6 and 22-24: the repo root became `<repo>`, and at 6 the home root became `<home>`. Substituting those two roots back reproduces the original exactly.
94. CONFIRMED. raw keeps no local path, user name, session id or temp id. Line 1's `<tmp>` comes from the wrapper's own header text (wrapper:13).
95. CONFIRMED. raw has no finish stamp. Its only clock times are the launch stamp (:2) and the PROVENANCE record's `stamp` (:10).
    - That second stamp is a start stamp, later than the launch; I do not reproduce it.
    - gtraw:10 carries the same field, and Q4 names "the report's PROVENANCE start stamp" as an unavoidable record.
96. CONFIRMED. st differs from selftest_after_lock.txt only at lines 1, 130, 131, 134, 172 and 173.
    - The repo root became `<repo>`.
    - The per-user temp root, including the heads and tails the self-test itself cut mid-path, became `<tmp>`.
    - Reversing these reproduces the original exactly.
97. CONFIRMED. st keeps no local path, user name, session id or per-user temp id. The random mkdtemp leaf names survive after `<tmp>/` (:134, :172, :173). The committed BUILD self-test raw (:135, :173-174) keeps them the same way, and they identify no one.
98. CONFIRMED. st's last line is "  182/182 mf3 selftest checks pass" (st:190, identical to the original and to x(3)).

## Across the drafts

99. CONFIRMED. No draft has a finish stamp or any figure that would give the contrast sessions' seconds: only the sham seconds and their sum appear, and $.timing.contrast_seconds is withheld. blk and ent contain no clock time.
100. CONFIRMED. I found no rule or precedent stated without a committed source. Each one I checked traces to:
     - A2:71 and :73;
     - rul:40;
     - list v2 item 5 and RESULTS.md:5242;
     - F-6 (:29) together with gt:81;
     - lines.py:219-221;
     - m:271;
     - sk-code and sk-seat.

     The only anchoring problems are items 71 and 73.

## Tally

| Grade | Count |
|---|---|
| CONFIRMED | 80 |
| IMPRECISE | 8 |
| FAIL | 2 |
| NOT CHECKABLE | 10 |

**Not confirmed:**
- **FAIL:** 35 (blk:80) and 83 (ent:31), both "computed no bound".
- **IMPRECISE:** 21 (the process-line quote's 0x08 byte), 32 and 81 (the stamps the end notice carried), 62 (A1s round 4 "another item"), 71 (the m:296 anchor), 73 (the rule-25 anchor), 79 (the entry states Code's reading as fact), 85 (the backend identifier's anchor).
- **NOT CHECKABLE:** 23 and 28 (PID 18391's identity and the tool-shell preamble), 34 (the commit message), 36 (the keep-it-out request), 48 and 53 (Code's containment and counter (b) runs), 74 (not opening the checkpoint after the stage), 76 and 92 (the placeholders), 90 (the future commit statements).

## Where I may have departed from the brief

None of these printed or reproduced any content, size or time from a checkpoint.

1. **`git rev-parse` on the first checkpoint.** I ran it at acc3b52 and at HEAD on `data/mf3/ckpt/Q-F3_time.json`; it printed two equal blob ids. Item 1 of the list allows this, but the brief's narrower bullet allows only `shasum` on that file.
2. **`git check-attr diff` on both checkpoints and the reads path.** It printed only "unset" or "unspecified". The same narrow-bullet caveat applies.
3. **A mental computation.** While reading, I noticed the interval between the launch stamp and the PROVENANCE stamp. I also worked out in my head how loose a same-day date bound is. No command ran, nothing was printed or written, and I report no figure from either.
4. **Files outside the listed sources.** None is under data/ or tasks/, and none is the transcript.
   - I read time/prelaunch_check.py and r2read/counter_b.py, and ran neither.
   - I ran `ps -o command=` on my own shell.
   - I listed ~/.claude/shell-snapshots/ and read the first 60 bytes of each file.
5. **A file the harness wrote.** It saved one oversized output, the committed ADDENDUM v0.5 text from a `cat`, to the session's tool-results folder. I wrote no file myself.

## The second pass (verbatim)

**Second pass: all ten of your items are resolved in the block and entry, but `R/commit_msg.txt` still says the opposite of both fixes.** It still calls PID 18391 "the launching shell", still says "no bound computed", and still lists only Q1–Q2. It needs updating before the commit (item 138).

- **Extract script:** sha256 prefix `9a70ce7c8f15ac98`, matching yours. I read it before running it.
- **HEAD:** `f674583` at the start and at the end of this pass. No tracked change.

**Blinding.** I checked the extract's masking by running a second, stricter clock mask over its output. It found nothing the script had left unmasked in sections (7)–(13), and I viewed only those sections, through that mask. The revised block, the entry and the commit-message draft hold no clock time. The only new figures are the window's width ("300 s", "five minutes", "five-minute"), which places nothing without a stamp, and calendar dates. Nothing in the new text bounds the end.

Abbreviations: blk / ent = the two revised drafts; x(N) = section N of the extract; gt = the first run's block; sk-code / sk-seat = the smoke reads.

## Your ten items

| Item | Status |
|---|---|
| 21 | Resolved. The `␈` quote, with the mark set back to 0x08, is a byte substring of raw line 3. |
| 32 | Resolved. Residual in item 109. |
| 35 | Resolved in blk. Residual in 114; still open in the commit message (138). |
| 62 | Resolved. |
| 71 | Resolved. |
| 73 | Resolved. |
| 79 | Resolved. |
| 81 | Resolved. |
| 83 | Resolved in ent. Residual in 133; still open in the commit message (138). |
| 85 | Resolved. |

Two first-pass items not on your list: 23 and 28 are superseded by the withdrawal. Item 36 is now confirmed: x(9) row 23174 shows Code asking the coordinating session to keep the end stamp out of committed text.

## The block

101. CONFIRMED. blk:39-42 (disclosures and question list) match §0's three bullets and §2's Q1–Q4.
102. CONFIRMED. blk:59-62 (the `␈` quote and its explanation). A local test, `/bin/zsh -c 'v="x\\bu"; echo "[$v]"'`, shows zsh's `echo` turning `\b` into byte 0x08. That fits wrapper:16 and the 59-byte entry.
103. CONFIRMED. blk:63-64. `man pgrep` says `-f` matches full argument lists and `-i` ignores case. The 60 characters kept contain no "python".
104. CONFIRMED. blk:65-70.
     - x(11) (row 23365, after the notice at row 22639) shows Code's tool shell argv as `/bin/zsh -c source …/shell-snapshots`. My first-pass check found the same form.
     - x(9) row 23394 shows Code's own statement of that form.
     - No member of the x(2) launch chain has the `{ case` form.
     - x(12) reports 2 of 94 background, Monitor or Agent calls not completed before the launch; x(13) shows both ending on 2026-11-07.
     - Caveats: the shell form was observed after the run, not at the launch. x(12) gives the check's result, not its method. Its link from the Monitor row to `b57wm58wz` is the script's.
105. IMPRECISE. blk:71-73. The quote "as far as both transcripts show" is verbatim (x(8) row 23556). Two parts say more than that message:
     - **"Neither had a call in flight":** for the pod session the message says no foreground call was in flight and its four background calls had ended. Of its two Monitors it says only that they "name no python".
     - **"Both sessions' Bash shells take the `source …` form":** the message says this of the coordinating session's own shells only.
     - **Fix:** "neither had a foreground call in flight, and every call whose text named python had ended; the coordinating session's own shells take the `source …` form."
106. CONFIRMED. blk:74-75 (x(8) row 23556: "I'll tell the PI, in case it was theirs").
107. CONFIRMED. blk:76-81 (x(2); x(1) verbatim; raw:3; gtraw:3).
108. CONFIRMED. blk:87-88 (the seat's ruling of 2026-11-08, §7, at line 40; raw:3).
109. CONFIRMED. blk:92-94. The quote "so the end lies within the five minutes before that stamp" is verbatim from x(7), and "300 s" matches it.
     - Residual: x(7)'s first line also carries a masked "by … UTC" time. The coordinating session's relay speaks of "the notice's stamp and the pgrep stamp" (x(8)), which suggests it is the end-wait's stamp. The extract cannot tell; if it is a separate time, name it.
110. NOT CHECKABLE. blk:95-97 (Code's reasoning). No extract holds it. What can be checked holds: no message carries an interval or bound figure (x(7); x(9) rows 23174 and 23394), and no extracted tool output shows one.
111. CONFIRMED. blk:98-99. "not computed against each other by anyone before VERDICTS" is verbatim from the driver review, line 325. The text labels it Code's reading.
112. CONFIRMED. blk:100-104 (the relay to the pod session and the request to it; the PI chat; the memory notes; no bound; nothing read). All from x(8) row 23332.
113. NOT CHECKABLE. The new dates "of 2026-11-10" (blk:71, :104, :108; ent:32). The extract prints no dates for the x(8) messages. They are consistent with blk:3.
114. IMPRECISE. blk:105, "No committed text restates any of these stamps or the window: not this block…".
     - blk:93 quotes the window's sentence, and ent:40-41 gives its width.
     - What is true: no stamp is committed, so nothing places the window.
     - **Fix:** "No committed text restates any of these stamps, so none places the window; the drafts give only its width."
     - The current commit-message draft does carry no stamp and no window.
115. CONFIRMED. blk:106-107. The reply quote is verbatim (x(8) row 23332).
116. CONFIRMED. blk:108-114 and :117.
     - The mechanism is x(8).
     - x(10) gives the order: notification at row 22639, compaction at row 22648, then the attachment at row 22650 naming the three files.
     - No compaction or listing appears before the notification.
     - "On these facts both listings fall after the run's end" is x(8)'s.
117. NOT CHECKABLE. blk:115-116, "found that none applied during the run".
     - x(8) says the transcripts "had none in <time>–<time> UTC". The interval is masked, so whether it spans the run cannot be checked here.
     - The message also limits the scan to recently touched transcripts, which the draft drops.
     - It scanned for compactions only (see 123).
118. CONFIRMED. blk:257-259. The anchor is now sk-seat:35 (§2.1, on S6 round 8, `Perfect.`).
119. CONFIRMED. blk:260-267. S12 rounds 3 and 7 are at sk-code:175 and :178, and sk-seat:35 confirms both. "A restatement with no result" fits sk-code.
120. CONFIRMED. blk:285-286. The 16-item pool has no "60 divided by 4" (valence_core/m/readrule.py:828-834).
121. CONFIRMED. blk:287-292. A label followed "31 + 4 config…" in the first run (gt:104) and in the smoke's S10 round 5 (sk-code:209); none follows it here.
122. CONFIRMED. blk:326.
123. IMPRECISE (fairness). blk:328-333, Q3.
     - What it states is accurate: the mechanism, the item-5 reading, and that the listing is the harness's, not a command.
     - It omits that the same whole-tree status arrives at a session's or subagent's start. This values-check's own starting context, spawned after the end, carried one naming `Q-F3_time-r2.json` and both report files, by name only.
     - So any session or subagent started mid-stage would receive the listing. x(5) shows Code started no subagent during the stage, and the coordinating session's scan covered compactions only.
     - **Fix:** add the start-of-session case to Q3's statement of the mechanism.
124. CONFIRMED (fair). blk:335-340, Q4. "No committed text holds a figure from either" holds: neither an endpoint nor an interval figure appears. Two points the seat may want beside it:
     - The coordinating session asked for the UTC stamp (x(1)), and the option offered would change that request.
     - The stamps also reached the pod session and the PI's chat (x(8)). §0 discloses this, but Q4 does not put it to the seat.
125. CONFIRMED. blk:344.
126. CONFIRMED. blk:345-346 (A2:71; the 2026-11-08 ruling at line 31).
127. CONFIRMED. blk:349-350 (m:271's phrase, verbatim). "Code did not open the checkpoint" remains NOT CHECKABLE, as my first-pass item 74.
128. IMPRECISE (minor). blk:351-352, "The values-check reproduced counter (a)…". My item 47 checked counter (a) over the redacted reads, with menus removed.
     - **Fix:** say "counter (a) over the redacted reads".
     - The sentence "Code's runs are its own steps" remains NOT CHECKABLE, as items 48 and 53.

## The entry

129. CONFIRMED. ent:10-13.
130. CONFIRMED. ent:27-33 (x(8) row 23556; x(11)).
131. CONFIRMED. ent:39-41 and ent:45-47 (x(7); x(8) row 23332).
132. NOT CHECKABLE. ent:42-44, as item 110.
133. IMPRECISE. ent:48, "No committed text restates any of the stamps or the window." ent:40-41 states the five-minute width. The fix is as item 114.
134. CONFIRMED. ent:49-50 and :52 (x(10); x(8)).
135. NOT CHECKABLE. ent:50-51, "none applied during the run in the transcripts it scanned", as item 117.
136. CONFIRMED. ent:63-64.
137. CONFIRMED. ent:100-104.

## Outside the changed set

138. **FAIL.** R/commit_msg.txt is unchanged and contradicts the revised drafts in three places:
     - It says the process-line entry "is the launching shell"; that reading is now withdrawn.
     - It says the end notice was "restated in no committed text, no bound computed"; the drafts now disclose the window and Code's reasoning bound.
     - It lists the block's questions as Q1–Q2 and omits the harness listing.
     - It carries no stamp or window, so blk:105's claim about the commit message holds for stamps.
     - **Fix:** align it with the revised block and entry.

**One observation, not graded.** Code's x(9) row 23174 message told the coordinating session that the drafts disclose "that no bound was computed from it". No extract shows Code sending the coordinating session the correction.

## Tally (items 101–138)

| Grade | Count | Items |
|---|---|---|
| CONFIRMED | 27 | — |
| IMPRECISE | 5 | 105, 114, 123, 128, 133 |
| NOT CHECKABLE | 5 | 110, 113, 117, 132, 135 |
| FAIL | 1 | 138 |

## Departures

- I ran the extract twice. The first run sent its output to `/dev/null` and printed only per-section mask counts. The second showed only sections (7)–(13), through the stricter mask.
- I ran one local zsh `echo` test that wrote no file.
- I read R/commit_msg.txt, which is outside your changed set.

Nothing under `data/` was opened. Nothing was computed from any record.
