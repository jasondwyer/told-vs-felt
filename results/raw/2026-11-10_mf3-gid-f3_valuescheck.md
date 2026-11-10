# G-ID-F3: the values-check of Code's block, the entry and the scrubbed raw

*Code's raw, PI date 2026-11-10.*
- *What was checked:* Code's block for the seat, the entry draft and the stage's scrubbed raw, after the stage had
  ended.
- *How:* one blind agent, read-only, under a brief quoting the list of record v2's items 1–5 as written.
  - It read three files for the drafts' figures: the stage's report and reads (item 2's read domain), and the
    artifact.
  - It hashed the checkpoints.
  - It rendered the configs by role, as the block does.
- *Outcome:* 73 items: 57 CONFIRMED, 8 IMPRECISE, 1 FAIL, 7 NOT CHECKABLE.
  - The FAIL and every IMPRECISE item are applied (below), most in the checker's own words.
  - Two of its observations are applied as well: m:271's sentence for Q3, and the end-wait's file-name match.
- *Not run:* a second pass. The changes apply the checker's own fixes. Code checked each one against its source by
  tool: the lock's sha256, `guard.py:93–102`, and m:271's sentence.
- *Code's masked scan of the checker's transcript* (no output text printed):
  - 101 distinct Bash calls, 26 of them naming `data/`.
  - The ones naming a `ckpt` file are of two kinds only:
    - `shasum -a 256` with `git check-attr`;
    - a `git grep` carrying item 3's tested pathspec.
  - The ones naming a `reports` file name only `Q-F3_id_report.json` and `Q-F3_id_reads.json`, the two the brief
    permitted.
  - None is in a barred metadata form.
- *This raw:* Code's dispositions, then the report verbatim.
  - The report was extracted by script from the agent's hand-back (the text's sha256 `79ff11dd…`, 262 lines).
  - One line of it is scrubbed: its abbreviation for the scratch directory, whose local root becomes `<tmp>`.
  - The raw holds no other local path, no clock time and no config label. Its `v0.5:N` references are line numbers.
- *Nothing ran on a model.*

## Code's dispositions

- **4, FAIL: the lock's sha256 tail.** Agreed: the tail is `…1d3f`, and `…3d81f` was a transposition. Applied in the
  block.
- **17, IMPRECISE: the item-2 paraphrase.** Agreed. Applied in the block and the entry, in the checker's words: item 2
  has the checkpoint "read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen, and a dry
  check is none of them". The raw's header is the run's record and stays as written.
- **27, IMPRECISE: the re-read line's cut.** Agreed. It is now marked: `…unchanged (c000ac2c…); …`.
- **31, IMPRECISE: `[False]`.** Agreed. Applied in both texts: `[false]`, the artifact's JSON literal.
- **44, IMPRECISE: "no reasoning-line bar … so".** Agreed. Bar 1, `scaffold_absorption`, applies at every stage. Applied:
  "G-ID-F3 has no reasoning-line defect bar (lock §8). Counter (a) is descriptive at every stage (§3.4)."
- **50, IMPRECISE: the `_gid_pass` line.** Agreed. It is now marked as Code's description, not a quote. It is
  anchored at `valence_core/mf3/guard.py:97–102`, and lists what the function checks.
- **53, IMPRECISE: "There is no bar at G-ID-F3 … run uncached".** Agreed. Applied: "G-ID-F3 has no reasoning-line
  defect bar. The record's consequence (§4) is that Q-F3 runs uncached, which Q1 puts to the seat."
- **55, IMPRECISE: the outputs.** Agreed. The entry's header now names the checkpoint, its report and reads under
  `data/mf3/reports/`, and the artifact.
- **62, IMPRECISE: "recorded … at LOCK-m-F3 v0.2".** Agreed. Applied: "recorded here, and to be recorded at LOCK-m-F3
  v0.2 (the seat's §5 items 1 and 3)".
- **The NOT CHECKABLE items.**
  - 8 and 24: Code's handling of the files, and its session while the stage ran. These are Code's statements. The
    checker was barred from transcripts.
  - 12: the announcement as sent. Code sent it to the coordinating session, and its as-sent text is in Code's
    transcript. The scratch file the checker read was the draft before it.
  - 14: the first dry check's CLEAR. It printed in Code's tool output before the announcement, and was not saved as a
    file; the second check's output is.
  - 56, 67 and 69: the placeholders and the commit still to come, filled at the commit.
- **The observations.**
  - **m:271 for Q3:** applied. The block's Q3 now quotes m:271 beside F14: "G-ID's sham-only sessions are read in full
    at G-ID (nothing to blind; §4 exception (4))".
  - **The end-wait matched the wrapper's file name, not its path** (item 21's note): applied in the block.
  - **The prior intact:** noted (`ff644fa1…51b8`, unchanged).
  - **`_gid_pair`'s PIN and m:281's "floors to the uncached column":** as the checker says, it concerns a pair whose
    transcripts are identical but whose line triples differ. This pair differs in both, so m:295's sentence is the
    operative one. Not added.
- **The checker's departure.** In its reasoning it once worked out the interval between the raw's launch stamp and its
  PROVENANCE stamp, against the brief's "compute no duration from any pair of times".
  - Nothing printed it, and no figure from it appears in its report.
  - Both stamps are start-side, before any session ran, and G-ID-F3 has no contrast session.
  - Disclosed here.

## The checker's report (verbatim; one line scrubbed, as above)

# Values-check of the G-ID-F3 drafts: the block, the entry and the raw

**HEAD at start: `fb82daa`. HEAD at end: `fb82daa`.**

**Result: 73 items. 57 CONFIRMED, 8 IMPRECISE, 1 FAIL, 7 NOT CHECKABLE.**

**Abbreviations:**
- G = `<tmp>/gid`
- B:n = line n of `G/2026-11-10_mf3-code-to-design_G-ID-F3.md`
- E:n = line n of `G/entry_gid.md`
- R:n = line n of `G/2026-11-10_mf3-gid-f3.txt` (the original is `G/run/gid_f3_raw.txt`)
- S:n = line n of `results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md`
- m:n = line n of PROPOSAL-m v1.11
- lock:n = line n of `LOCK-m-F3.md`
- v0.5:n = line n of ADDENDUM-m2 v0.5
- In the reads file, `sessions[0]` is the uncached half and `sessions[1]` the cached one.

Configs are named by role only, P and Q. Where an item in the entry repeats an item in the block, it is graded once, under the block's item.

## A. The block (with the entry's repeats)

1. **CONFIRMED.** B:1, the title. In the artifact, `verdict` is FAIL and `indices[0]` is template A2s, j 0, `identical` false. The identity's `reasoning_cap` is 120.
2. **CONFIRMED.** B:4: m:295, Qwen, the laptop, "the cap of record, 120". S:21 says "The cap of record is 120". The report's `provenance[0].record` is mlx on macOS arm64.
3. **CONFIRMED.** B:5, the commit `f674583`. Its subject is "LOCK-m-F3 v0.1 -- RE-ISSUED…", and it modifies LOCK-m-F3.md.
4. **FAIL.** B:5, the lock's sha256 written as `70da4a70…3d81f`.
   - `shasum -a 256 LOCK-m-F3.md` equals the identity's `lock_sha256`, which is `70da4a70aeeff434…3872e81d3f` (full at RESULTS.md:370).
   - Its tail is `81d3f`. `3d81f` is not a suffix of it (the characters are transposed).
   - Fix: `70da4a70…81d3f`. The r2 block wrote `…1d3f`.
5. **CONFIRMED.** B:6–7: the driver is the one committed at `fb82daa`, and the prior is the re-run's checkpoint, taken by path.
   - R:6 shows the driver. `git rev-parse fb82daa:scripts/mf3_sessions.py` equals `git hash-object` of the working-tree file.
   - The driver takes the prior by path at :121, :143, :361–368 and :430. `prelaunch_final.txt:4` records `Q-F3_time-r2.json`.
6. **CONFIRMED.** B:8–9: the seat reads the pairs before v0.2 (§5 items 2–3). S:46 says "the seat reads before v0.2 is written"; S:47 is item 3.
7. **CONFIRMED.** B:10–11: the FAIL is the stage's computed verdict. It is the report's `status`, computed at `stages.py:1317–1321`.
8. **NOT CHECKABLE.** Three claims about how Code handled the files:
   - B:12–14, "read after the invocation had ended … the checkpoint was hashed only";
   - E:47 and E:66, "Code did not open" the checkpoint.

   No source shows what Code did with the files. The claimed basis, item 2, is right: reports are item 2's read domain, and the artifact lies outside `ckpt` and `reports`.
9. **CONFIRMED.** B:15–16: the sessions are sham-only, and the reads hold their full records (lock F14).
   - The F14 text is at lock:652. The reads file's form is written at `stages.py:1348–1352`.
   - The reads carry `cell` and `choices`.
10. **CONFIRMED.** B:20–22 and E:18–20, the routing quote and "Route as given" (PI, 2026-11-10). The quote is verbatim from S:65. "Route as given" is at RESULTS.md:356–357, and the quote also appears at :362.
11. **CONFIRMED.** B:23–24: the wiring is at `fb82daa`, with the full blob `8d878f4a…d200e7`. It matches `shasum` of the working-tree file.
    - R:6 (DRIVER) comes before R:8 ("after the load").
    - RESULTS.md:66–67 says "The DRIVER line prints it before the load".
12. **NOT CHECKABLE.** B:25, "Code announced the run with the wiring's hash".
    - No as-sent announcement is among the sources.
    - `G/announce_gid.txt` (outside the brief's list, read for this item) is a draft: its l.3 holds the placeholders `@@WIRECOMMIT@@` and `@@NEWBLOB16@@`.
    - ack:2–5 names `fb82daa` and the blob, which is consistent with the claim.
13. **CONFIRMED.** B:25–29 and E:31, the ack's four quotes. Each is verbatim: ack:1; ack:7; ack:8 (first sentence); ack:9.
14. **NOT CHECKABLE.** B:30 and E:23: the dry check "returned CLEAR twice: once before the announcement, and once just before the launch".
    - Only the last output is a source: `prelaunch_final.txt:10`, PRELAUNCH CLEAR.
    - R:1 says only "returned CLEAR just before the launch". The announcement draft says a check "runs just before the launch".
    - The first CLEAR, and the order of ack and launch in E:23, rest on Code's word alone.
15. **CONFIRMED.** B:31–32, what the dry check covered.
    - `prelaunch_final.txt:1–9`: `locked_path` absent, `reasoning_cap` 120, no precheck problems, the driver committed at `fb82daa` with the working tree identical, and the snapshot at the lock's revision.
    - Nothing was loaded: `prelaunch_check_id.py:19–25`.
16. **CONFIRMED.** B:33–34, the recorder and what it showed: `Q-F3_time-r2.json`, `require_real` on, cap 120. The recorder is at `prelaunch_check_id.py:29–34`; the result is `prelaunch_final.txt:4`, and the CLEAR condition at :55–56 requires it.
17. **IMPRECISE.** B:33–34 and E:23–24 give the reason as "the list's item 2 has only the stage's own code read the checkpoint".
    - Item 2 has `ckpt` files "read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4".
    - Fix: "item 2 has the checkpoint read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen, and a dry check is none of them".
    - R:1 carries the same paraphrase, but it is the run's record and stays as written.
18. **CONFIRMED.** B:35: "The run's own precheck ran the gate". The driver at :428–432 calls `stages.prior_gate("id", id_prior_checkpoint(paths), …, require_real=True, reasoning_cap=…)`; RESULTS.md:47–48 says the same, and the raw shows no refusal.
19. **CONFIRMED.** B:36–38 and E:21–22, the launch.
    - It used m:267's line, as written in `launch_gid_f3.sh:5`, at HEAD `fb82daa` (R:2, and the `test` in `launch_and_endwait.txt:2`).
    - The launch command carries no literal "python" (`pytho[n]` only), and its `test -z` refuses to launch on any match.
    - Its output reads "no matching process before the launch" (`launch_and_endwait.txt:4`).
20. **CONFIRMED.** B:39–40 and E:28: the launch PID's command line, read once, was caffeinate's.
    - `ps -p $P -o command=` runs once (`launch_and_endwait.txt:2`). Its output (:7) is `caffeinate -is /bin/zsh <tmp-path>`; the block renders that path as `<wrapper>`.
    - The launcher's comment says "the wrapper's" (`launch_gid_f3.sh:2`).
21. **CONFIRMED.** B:41–42 and E:29, the end-wait and "it is the PID alone".
    - The loop is at `launch_and_endwait.txt:9` and its ENDED line at :11.
    - Its form is O3-1's PID loop with a command guard, then O3-2's pgrep (`results/raw/2026-10-13_m-gf0m-qwen-driver_review.txt:4649–4653`). It touches no file.
    - Note: the guard matches the wrapper's file name, `run_gid_f3.sh`, not its full path.
22. **CONFIRMED.** B:43–44, the power line. Verbatim from R:3, minus its "# Power: " prefix.
23. **CONFIRMED.** B:45–46 and E:26–27, the probe line.
    - The quote is verbatim from R:4, and no match line follows (R:5 is INVOCATION).
    - The change is the seat's (§8 item 7 at S:68; §3 at S:36).
    - In r2's raw (`results/raw/2026-11-10_mf3-gtime-f3-r2.txt:3`) the probe sat inside the Power line; here it has its own line. `run_gid_f3.template.sh` differs from the wrapper only at `@@WIRECOMMIT@@`. r2's wrapper itself is not a source.
24. **NOT CHECKABLE.** B:47–52 and E:32–33, "While the stage ran": no model or Python process, the reads, the read script, no compaction, no subagent, and other sessions' processes unknown. No source shows Code's session during the run, and transcripts are out of scope.
25. **CONFIRMED.** B:53–54 and E:35, the end notice.
    - The quote is verbatim from `end_notice_sent.txt:1`. Its form follows S:41 and ack:10.
    - Its header carries a PI date only. `EXIT_CODES` maps FAIL to 5 (`stages.py:73`).
26. **CONFIRMED.** B:56–57, the DRIVER line and the first SNAPSHOT line. Both are verbatim from R:6–7, with the elisions marked.
27. **IMPRECISE.** B:58 renders the re-read line as `SNAPSHOT re-read after the load: unchanged (c000ac2c…)`.
    - R:8 goes on with "; adapter model_id mlx-community/Qwen3.6-27B-4bit", and the cut is unmarked.
    - Fix: mark the cut, for example `…unchanged (c000ac2c…); …`.
28. **CONFIRMED.** B:59–61 and E:40–41, the GATE, LICENCE and PROVENANCE lines (R:9–11).
    - `shasum` of PROPOSAL-m v1.11, LOCK-m-F3.md, `scripts/m_analyze.py`, A-m2 v0.5 and CLAUDE.md matches every printed prefix.
    - The package prefix matches the identity's `package_sha256`.
    - The raw says "the 11 m files"; the drafts say "eleven". The versions are MLX 0.31.2 and mlx-lm 0.31.3.
29. **CONFIRMED.** B:62–65 and E:42–43, the stage lines in order: two `valid` lines, BAR, STAGE, the four path lines, `EXIT=5` (R:12–20). The uncached half runs first: the artifact's `path_order`, and `guard.py:80–82`.
30. **CONFIRMED.** B:66–67 and E:44–45, the identity: backend `a734dadec8f8ce9b`, cap 120, path `cached+uncached`.
    - These are the report's `identity` fields.
    - "As at G-TIME-F3's two runs and G-TIME-F0": RESULTS.md:271–272 (r2: "as at the first run and at G-TIME-F0"), RESULTS.md:2829 (the first run: "as at G-TIME-F0"), and S:11.
31. **IMPRECISE.** B:71 and E:48 write `pairs_identical` `[False]`. The artifact's literal is the JSON `[false]`, and the block itself writes `false` for the pair record's fields at B:77. Fix: `[false]`. The rest is right: verdict FAIL, `n_pairs` 1, and the criterion "(the seat's F-7)".
32. **CONFIRMED.** B:73 and E:49: the bar fired at k = 1 of n = 1. This is the report's `bars[0]`, bar 6 at lock:599, computed at `stages.py:1320`.
33. **CONFIRMED.** B:74, E:49 and E:2–3: "stops at the first divergence (m:281, m:295)", and A3s did not run.
    - The quote is verbatim from lock:599. The stop is coded at `stages.py:1188–1190` and :1304–1308.
    - The report and the reads hold A2s only, and the artifact's `n_pairs` is 1.
34. **CONFIRMED.** B:75–77 and E:50–51, the pair.
    - Both halves have the same `cell`, `keys` and `banner`.
    - Both are `complete` and `verified`, with `excluded` false and `exclusion` null, and no hair trigger. Each half's `valid_sessions` is 1.
    - The report's `pairs[0]` fields are as quoted.
35. **CONFIRMED.** B:78–87, the forced-round table.
    - `rounds[0..3]`: each round's record is identical across the two halves. Tasks, roles and responses are as tabled.
    - `9` for the days in a week is wrong on both paths.
36. **CONFIRMED.** B:88–91 and E:52, the transcript comparison.
    - The lengths are 3,103 and 3,424 characters.
    - The first differing 0-based index is 658, so the shared prefix is 658 characters.
    - Index 658 lies in round 5's `reasoning_text` piece. That piece directly follows the harness's `reasoning` piece, F-b's opener `Reasoning (one line): So far,` (v0.5:42).
    - Both quoted continuations are verbatim from `reasoning[0].text` (role-rendered).
37. **CONFIRMED.** B:92–94 and E:53, the reasoning lines.
    - All six differ in both text and `n_tok`.
    - The token counts are exactly as listed.
    - `cap_hit` is false and `stop_reason` is "newline" on all 12; the report's `cap_reached` is 0.
38. **CONFIRMED.** B:95–105 and E:54–56, the free-round table: picks, tasks and responses. Round 9's `n_tok` is 2 uncached and 1 cached.
    - Note: round 9's texts are identical, so the entry's "differ at round 7 … and at round 10" is true of the texts.
39. **CONFIRMED.** B:106–107 and E:11, the picks.
    - `first_free_pick_P` is true on both halves, and the report's `first_pick_P` agrees.
    - The picks agree through round 9.
    - At round 10 the cached half's `choices[5].picked_role` is Q, and its `rounds[9]` is Q's item, "Compute 11 + 33.".
40. **CONFIRMED.** B:108–110, the reads at round 10.
    - `label_mass` rounds to .368 and .682.
    - `top1_is_label` is false (uncached) and true (cached).
    - The picks are P and Q, and `verify_kl` is 0.0 on every read.
41. **CONFIRMED.** B:112–114 and E:57–58, the counters' anchor and domain. v0.5:50's blinding scope reports (a) over sham lines and (b) over sham rounds, and both sessions are sham.
42. **CONFIRMED.** B:116–121, E:12 and E:59, counter (a).
    - The report's `counter_a` is 0 uncached and 2 cached.
    - I recomputed it with stdlib Python, re-implementing the rule in `lines.py:49–84` and :182–189. Only the cached half's lines 5 and 6 (rounds 9 and 10) count. Each contains the domain's first line, the banner line the drafts quote, and each matches `FRAME_RX`.
    - Both quoted tails are verbatim.
43. **CONFIRMED.** B:122–124 and E:60: the echo class does not claim the two lines.
    - Their audits show no class, `defect` false and `echo_line` null.
    - v0.5:27's "equality after whitespace normalization" is quoted verbatim, and containment goes to counter (a) (v0.5:27, :50).
    - `echo_match` (`lines.py:136–139`) finds no equal line.
44. **IMPRECISE.** B:125: "G-ID-F3 has no reasoning-line bar (lock §8), so the count is descriptive".
    - Bar 1 in lock §8, `scaffold_absorption` (lock:594), applies at every stage, and its unit is "a task round or a reasoning line".
    - What G-ID-F3 lacks is a `reasoning_line_defect` bar. Those exist only at G-TIME-F3, G-F3 and the campaign (lock:598, :601, :603).
    - Counter (a) is descriptive at every stage by declaration (v0.5:50), not because a bar is missing.
    - Fix: "G-ID-F3 has no reasoning-line defect bar (lock §8); counter (a) is descriptive at every stage (§3.4)".
45. **CONFIRMED.** B:126–130, E:12–13 and E:61–62: counter (b) = 0 of 20.
    - The domain is 10 rounds in each of the two records, each with `audit.claim` null. That is `b_candidates`' domain (`lines.py:197–226`), and the report's claims are all zero.
    - Under v0.5:50's sentence, every response attempts its own round's task. Round 4's `9` is "wrong", not (b).
    - None is a preamble, a description, a header or reasoning about the choice.
46. **CONFIRMED.** B:134, E:14 and E:63, the timing: 1,942.675 s and 208.347 s. These are the report's and the artifact's `timing`, and the reads' `seconds`.
47. **CONFIRMED.** B:135–137, the basis.
    - The re-run's sham mean, 1,111.9 s, is at S:35 and S:47.
    - The uncached half's line lengths run from 35 to 95 tokens.
    - The cached seconds are the basis S:47 names.
48. **CONFIRMED.** B:138: Code computes no projection. Neither text carries one.
49. **CONFIRMED.** B:140–145, B:147–148 and E:6–7, §4's quotes.
    - m:295, lock:599 bar 6, the PRIOR_STAGE PIN (`stages.py:417–419`, the quote joining a comment line break) and S:47 are each quoted verbatim.
    - §4 rules on nothing.
50. **IMPRECISE (minor).** B:146, "`guard._gid_pass` admits the cached path only on an artifact whose verdict is PASS".
    - The claim is true: `guard.py:97` checks `g.get("verdict") == "PASS"`, together with `n_pairs` 2, both pairs identical, this backend and this cap (:97–102).
    - But it is the one line under a header that says "quoted" that is Code's description, and it gives no anchor.
    - Fix: anchor guard.py:97–102, or quote its PIN at :93–96.
51. **CONFIRMED.** B:152–157, Q1 and Q2.
    - Both components of the pair differ.
    - The record's consequence is cited to §4.
    - 208.3 s is 208.347 rounded.
    - Q2 is (b) = 0 of 20.
52. **CONFIRMED.** B:158–164 and E:72–76, Q3.
    - The seat's §5 item 2 quote is verbatim (S:46). The F14 quote is verbatim (lock:652).
    - The reads hold the labels and the picks.
    - F14's site column is `stages._finish_gid`, which writes the reads file (`stages.py:1350–1352`, :1369). That supports reading F14 as governing the file the stage writes.
53. **IMPRECISE.** B:165–166: "There is no bar at G-ID-F3, and Q-F3's sessions run uncached under §4."
    - G-ID-F3 has bars: bar 6 (the one that fired) and hair triggers 1–3 (lock:594–596, :599).
    - "run uncached" states as settled what Q1 asks the seat to rule.
    - Fix: "G-ID-F3 has no reasoning-line defect bar; the record's consequence (§4) is that Q-F3 runs uncached, which Q1 puts to the seat".

## B. The entry (claims not already graded in A)

54. **CONFIRMED.** E:1–4 and E:8–15, the header's anchors and the summary.
    - m:295 sits in §3.2, which opens at m:288.
    - §5 items 1–2 are at S:45–46, and §8 item 4 is at S:65.
    - The summary bullets are covered by items 33–46 and 51–52.
55. **IMPRECISE.** E:4–5: "Its outputs are `data/mf3/ckpt/Q-F3_id.json` and the artifact".
    - The stage wrote four outputs (R:16–19), and R:1 also names "its report and reads".
    - Fix: "the checkpoint, its report and reads under `data/mf3/reports/`, and the artifact".
56. **NOT CHECKABLE.** E:17, `@@STAMP@@`: it is a placeholder.
57. **CONFIRMED.** E:18–20, the routing. Same as item 10.
58. **CONFIRMED.** E:24–25: "The block quotes the ack (§0)". B:25–29 does.
59. **CONFIRMED.** E:30, "the seat's laptop rule of 2026-11-08, §7". It is at `results/raw/2026-11-08_gtime-f3_design-to-code_answers.md:40`.
60. **CONFIRMED.** E:34: "no commit landed on main between the launch and the end".
    - HEAD was `fb82daa` at my start and at my end. That is the launch's HEAD (R:2).
    - The reflog's newest entry is `fb82daa`'s own commit.
61. **CONFIRMED.** E:36–39, the raw link and the DRIVER and SNAPSHOT lines.
    - The full sha matches.
    - The SNAPSHOT line is the snapshot sha, unchanged after the load (R:7–8).
62. **IMPRECISE.** E:38: "the `id` wiring's blob, recorded here and at LOCK-m-F3 v0.2".
    - v0.2 is not written yet. The record has it to be recorded there: S:45 ("recorded at v0.2"), S:47, and RESULTS.md:68–69.
    - Fix: "recorded here, and to be recorded at LOCK-m-F3 v0.2 (the seat's §5 items 1, 3)".
63. **CONFIRMED.** E:46: "These are read from the report, the reads and the artifact". Every figure in the drafts traces to those three files.
64. **CONFIRMED.** E:66–68, the hashes. `shasum -a 256` gives:
    - the checkpoint `4244c7fc…e519`, and `git check-attr diff` gives "unset", that is, -diff;
    - the report `b3b00428…ed48`;
    - the reads `79da1b71…e44f`;
    - the artifact `ea8f7d3a…9260`.
65. **CONFIRMED.** E:69–71: the raw, and the block rendering the configs by role. The block carries no label (see item 72).
66. **CONFIRMED.** E:72–74, the block's questions. They match B:152–164, including "whether v0.2 carries a cached projection under a FAIL" (B:155–156).
67. **NOT CHECKABLE.** E:77, `@@VC@@`: it is a placeholder.
68. **CONFIRMED.** E:78: LOCK-m-F3 v0.2 (m:296) waits for the seat's read and the PI's word. m:296 reads "LOCK-m-F3 v0.2. Cap; path; projections", and S:46 has the seat read first.
69. **NOT CHECKABLE.** E:65 ("Committed with this entry") and E:79 ("Not pushed. Committed by path."). Both are about a commit that has not happened yet.

## C. The raw

70. **CONFIRMED.** The scrub.
    - Substituting `<repo>` 5 times and `<home>` once into the original reproduces the scrubbed raw exactly, character for character. Both files have 20 lines.
    - The `<tmp>` at R:1 is already in the original: it is the wrapper's own header text (`run_gid_f3.sh:14`). So no `<tmp>` substitution was made.
71. **CONFIRMED.** No local path, user name, session id, temp id or PID survives. The HF cache path is rooted at `<home>`.
72. **CONFIRMED.** No clock time, no finish stamp and no config label in the texts.
    - The block and the entry carry no clock time and no label. I scanned case-insensitively for both G-ID labels, their four-letter stems, and the other sessions' labels that the seat's read names: zero hits.
    - The raw carries no label and no finish stamp. Its two clock stamps are both from the start: the header's launch stamp (R:2, in m:267's form, accepted at S:41), and the PROVENANCE record's stamp (R:11, the same form as in r2's raw).
73. **CONFIRMED.** R:1's other claims.
    - Its anchors are right.
    - "No departure from the checklist" holds against m:267: AC at 140 W, the probe at 0, `caffeinate -is`, 630Gi free, and the GATE line.

## D. Observations (ungraded)

- **For Q3.** m:271 itself says "G-ID's sham-only sessions are read in full at G-ID (nothing to blind; §4 exception (4))". That sentence is the direct anchor for F14 and for the reads file's form. The block could cite it beside F14, since the seat's §5 item 2 invokes "m:271's rule".
- **The prior is intact.** `Q-F3_time-r2.json` still hashes to the r2 entry's `ff644fa1…51b8` (RESULTS.md:298).
- **Another consequence sentence.** `_gid_pair`'s PIN (`stages.py:1208–1212`) carries m:281's "its floors to the uncached column" for a pair whose transcripts are identical but whose line triples differ. This pair differs in both, so m:295's sentence is the operative one.

## E. Everything not CONFIRMED

- **FAIL:** 4 (the lock hash's tail).
- **IMPRECISE:**
  - 17: the item-2 paraphrase (B:33–34, E:23–24);
  - 27: the re-read line's unmarked cut (B:58);
  - 31: `[False]` for `[false]` (B:71, E:48);
  - 44: "no reasoning-line bar … so" (B:125);
  - 50: the unquoted, unanchored `_gid_pass` line (B:146);
  - 53: "There is no bar at G-ID-F3 … run uncached" (B:165–166);
  - 55: the outputs (E:4–5);
  - 62: "recorded … at LOCK-m-F3 v0.2" (E:38).
- **NOT CHECKABLE:**
  - 8: Code's handling of the reads and the checkpoint;
  - 12: the announcement as sent;
  - 14: CLEAR "twice";
  - 24: "While the stage ran";
  - 56: `@@STAMP@@`;
  - 67: `@@VC@@`;
  - 69: the commit not yet made.

## F. What I did, and one departure

- **What I read:**
  - Under `data/`, only the three permitted files.
  - I hashed the three checkpoints with `shasum -a 256` and nothing else.
  - In G, I also read `announce_gid.txt` and `run/launch_pid.txt`. Neither is on the brief's list, but no rule bars them.
- **Searches and listings:**
  - My one tree search was `git grep` for "O3-1", with item 3's tested pathspec.
  - Python was stdlib only, run as `python3 -I`, fed through here-documents; it imported no repository code.
  - I ran one reflog listing, in ids and subjects only.
  - I ran `wc -l` on the two scratch raws, which are outside `data/`.
  - r2's raw header was printed with its clock times masked.
- **No writes.** I made no git write and edited no file. The shell's here-documents use temporary files of its own.
- **Departure (no command involved).** Once, in my reasoning, I worked out the interval between the raw's launch stamp and its PROVENANCE stamp. Both are start-side, before any session ran. Nothing printed it, and no figure from it appears here. This breaks the brief's "compute no duration from any pair of times".

Clock stamps did appear in my tool output while reading: the raw's header, the provenance records, and RESULTS.md's write-time stamps. None is reproduced here.
