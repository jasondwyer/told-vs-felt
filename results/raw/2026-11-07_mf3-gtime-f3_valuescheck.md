# G-TIME-F3 -- the blind values-check of the entry, the ping and the raw, with Code's dispositions (2026-11-07)

*Code's raw. One blind pass by an agent given the drafts, the stage's pick-free outputs and the sources (it hashed the checkpoint and did not open it): 66 items, 61 PASS, 5 IMPRECISE, 0 FAIL. Code's dispositions follow the report. Local roots are scrubbed.*

---

# Blind values-check: the G-TIME-F3 entry (E) and Code's ping to the design seat (P)

Checked versions (sha256): E = `entry_gtime.md` 856f6532…7bbd (the version with the 38f9974 disclosure at E:24-28);
P = `2026-11-07_mf3-code-to-design_G-TIME-F3.md` a5ce512c…9018 (disclosure at P:48-51);
W = `2026-11-07_mf3-gtime-f3.txt` 643653fc…f369; pre-scrub raw `gtime_raw.txt` 7045c618…3852.
Line anchors are to these versions. Repo: HEAD is 38f9974 (another session's commit on top of the run's acde2d8);
nothing under `valence_core/mf3`, `valence_core/m`, the driver, the analyzer, the lock or the proposal differs
from acde2d8 (`git diff --quiet acde2d8 -- …` clean).

Blinding kept: `data/mf3/ckpt/Q-F3_time.json` was only hashed (`shasum -a 256`), never opened or listed with size or
time; no size/time listing of `data/mf3/ckpt` or `data/mf3/reports`; no bound on any contrast session's duration
computed or stated (38f9974's commit time was compared with the launch stamp only as a boolean, never printed). The
report and the reads were read in full. Nothing in the repo was edited, staged or run (`time` never run).

Helper: `vc/import_closure.py` (static transitive import closure at a given revision).

## Items

1. **Claim:** six uncached sessions on Qwen under LOCK-m-F3 v0.1, on the committed driver (acde2d8); PASS, exit 0.
   **Location:** E:1-2; P:20. **Verdict:** PASS. **Evidence:** W:5, W:8, W:9 (HEAD acde2d837a17…); W:20
   `STAGE G-TIME-F3 PASS path=uncached`; W:24 `EXIT=0`; report `status` PASS, `stop` null, `identity.path`
   uncached, `planned` = `recorded` = 1 per template (six); the reads hold six sessions.

2. **Claim:** both binomial bars silent on the three sham sessions, 0/25 rounds (A1s 5, A2s 10, A3s 10) and 0/13
   lines (A1s 1, A2s 6, A3s 6). **Location:** E:3-4, E:40-42; P:21, P:73-78. **Verdict:** PASS. **Evidence:**
   W:17-18; report `bars`: k 0, n 25, crit 4 and k 0, n 13, crit 4, both `fired` false; `stage_report.templates`
   `all.rounds` 5/10/10 and `reasoning_lines.lines` 1/6/6.

3. **Claim:** no hair trigger fired. **Location:** E:3; P:21. **Verdict:** PASS. **Evidence:** report
   `hair_triggers` [] for A1s, A2s, A3s; status PASS with `stop` null (m:271: a hair-trigger fire anywhere stops the
   stage, and template_breakage / schedule_mismatch are hair triggers).

4. **Claim:** all six records passed G-VER. **Location:** E:43; P:22. **Verdict:** PASS. **Evidence:** reads
   `verified` true on all six; `verify.verify_and_mark` sets `rec["verified"] = not problems`
   (valence_core/mf3/verify.py:246-250), called by `stages._launch` before the record is written.

5. **Claim:** the cap trigger counted 1 of ≤ 36 lines (threshold 3), so the cap fixed is 60; E's quote of the CAP
   TRIGGER line. **Location:** E:5, E:44-45; P:23-24. **Verdict:** PASS. **Evidence:** W:19; report `cap_trigger`
   {cap_reached 1, max_lines 36, threshold 3, fixed_cap 60}; m:174 (≥ 3 → 120). E's quote, unwrapped, is a
   substring of W:19 and of the pre-scrub line.

6. **Claim:** "LOCK-m-F3 v0.2 records it (m:296)" (E:45); "m:296 records it at v0.2, and from G-ID-F3 on the stage
   refuses any other cap" (P:192). **Verdict:** PASS. **Evidence:** m:296 "LOCK-m-F3 v0.2. Cap; path;
   projections."; W:19 "recorded at LOCK-m-F3 v0.2 (m:296)"; valence_core/mf3/stages.py:466-477 (id and qual
   re-compute the trigger from G-TIME-F3's checkpoint and raise "NOT THE FIXED CAP"; the campaign checks G-F3's cap).
   Optional wording: "m:296 has v0.2 record it".

7. **Claim:** "The PI's routing of 2026-11-07, item 1, quoted at RESULTS.md@139635f:81, ends '… LOCK-m-F3 v0.1 →
   G-TIME-F3 [go]'". **Location:** E:12-13. **Verdict:** IMPRECISE. **Evidence:** RESULTS.md@139635f:81 is item 1
   and carries the quoted words, but the item goes on: "… → LOCK-m-F3 v0.1 → G-TIME-F3 [go]; N10 m:312 stands
   [confirmed]; N13 no change [confirmed]." The chain ends there; the item does not. **Fix:** "whose chain ends
   '… → LOCK-m-F3 v0.1 → G-TIME-F3 [go]'" (or quote it with a trailing "; …"). P:3-4's "ends at G-TIME-F3" reads as
   the chain of steps and can stand.

8. **Claim:** the seat's answers of 2026-11-07, §9 item 1: "G-TIME-F3's six sessions (the seat's read under m:263's
   printed form and §3's rule)". **Location:** E:13; P:4-5. **Verdict:** PASS. **Evidence:**
   results/raw/2026-11-07_p-preread_design-to-code_answers.md:64, item 1's last element, verbatim.

9. **Claim:** the coordinating session's instruction, "Stop after G-TIME-F3's six sessions and report, because the
   seat reads them." **Location:** E:13-14. **Verdict:** PASS (consistency only; chat, not in the repo).
   **Evidence:** consistent with §9 item 1 (the seat reads the six sessions) and with the routing's chain ending
   at G-TIME-F3; E and P stop there.

10. **Claim:** launched with m:267's line as written, `nohup caffeinate -is /bin/zsh <wrapper> > /dev/null 2>&1 &
    disown`. **Location:** E:15; P:38-39. **Verdict:** PASS. **Evidence:** m:267's checklist "`nohup caffeinate -is
    … & disown`"; launch_gtime.sh:5 runs exactly that line with the scratch path of run_gtime.sh; W:1 records it
    with `<tmp>`.

11. **Claim:** the wrapper writes the raw, exports `HF_HUB_OFFLINE=1` and unsets `MLXLM_USE_MODELSCOPE`.
    **Location:** E:16; P:40. **Verdict:** PASS. **Evidence:** run_gtime.sh:8-10 and :21 (`} > $RAW 2>&1`).

12. **Claim (E):** the raw's header records the launch line and the checklist's items (AC at 140 W, 637 GiB free,
    no other Python process); the gate line is the driver's own. **Location:** E:16-18. **Verdict:** PASS.
    **Evidence:** W:1 (launch line; "the gate line is the driver's own"); W:3 "Now drawing from AC Power; Wattage
    140 W; disk: 637Gi available on /; python processes before the run: []"; W:8 is the driver's GATE line; m:267's
    items (≥ 96 W on AC; one process; caffeinate; display sleep; disk; the gate line logged).

13. **Claim (P):** "The raw's header records the launch and the checklist's items: AC at 140 W; 637 GiB free; no other
    Python process; the gate line, which is the driver's own." **Location:** P:41-42. **Verdict:** IMPRECISE (low).
    **Evidence:** the header (W:1-3) does not record the gate line; it says the gate line is the driver's own, and the
    driver logs it at W:8. E:16-18 words this correctly. **Fix:** "…; no other Python process. The gate line (W:8)
    is the driver's own."

14. **Claim:** a dry pre-launch check returned CLEAR just before the launch: the identity, the precheck, the driver and
    snapshot checks, with the lock's values and nothing loaded. **Location:** E:19-20; P:43-44. **Verdict:** PASS
    (description verified; the CLEAR itself is not on file). **Evidence:** prelaunch_check.py calls
    `time_identity_extra`, `time_precheck`, `driver_problems`, `qwen_snapshot` and the revision check, blocks
    mlx/jlens imports and sets `_load_qwen = None`, and prints `PRELAUNCH CLEAR|REFUSED`. Its output was not saved;
    W:1 states CLEAR.

15. **Claim:** a false start: the first launcher call failed for lack of execute permission and started nothing (no
    raw, no process); the launch of record followed seconds later; the raw's header does not mention it.
    **Location:** E:21-22; P:45-47, P:191. **Verdict:** PASS (history not checkable from files; consistent).
    **Evidence:** launch_gtime.sh is now `-rwxr-xr-x`; W is one run's output (one header, one EXIT); W has no
    mention of it.

16. **Claim:** no other session had touched the repository in the hour before the launch. **Location:** E:23.
    **Verdict:** PASS (as far as files show). **Evidence:** reflog: the only entry in the hour before W:2's launch
    stamp is acde2d8 itself (Code's wiring commit), 1e79955 being earlier; working-tree mtimes in that hour
    (excluding .git, jlens-qwen36/ and data/mf3/): only acde2d8's six files (scripts/mf3_sessions.py and the five
    2026-11-07_mf3-time-wiring raws); W:2 "tracked changes: []".

17. **Claim:** during the run another session committed 38f9974 (PROPOSAL-p's flags close: RESULTS.md and a raw) and
    began editing valence_core/p in the working tree. **Location:** E:24-25; P:48-49. **Verdict:** PASS on content
    (the "during" half is not checkable without the run's end, which is withheld). **Evidence:** 38f9974's parent
    is acde2d8; `git diff --stat acde2d8 38f9974` = RESULTS.md and
    results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md; its message is the G-CAL-p flags block's close;
    its committer time is later than the launch stamp (boolean only); the six valence_core/p files were modified
    at this check's start and W:2 shows no tracked change at launch. Note: scripts/p_sessions.py is now modified as
    well (it was not at this check's start); nothing in the mf3 closure reaches it (item 19).

18. **Claim:** the same sentence, "During the run, another session committed `38f9974`". **Location:** E:24; P:48.
    **Verdict:** IMPRECISE (blinding hygiene, not accuracy). **Evidence:** 38f9974's committer time is in git (and
    public once pushed to the public origin). Saying it fell inside the stage ties a dated record to the stage's
    end. With W:2's launch stamp and the sham seconds this entry prints (711.0 s), that gives anyone a derivable
    lower bound on the contrast sessions' combined time. The seat's G-TIME-F0 read, Q4
    (results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md:49) keeps finish stamps out of contrast-stage raws
    and commit messages. It admits only the "unavoidable records" (the commit times, the PROVENANCE start stamp,
    the entry's own stamps, "no tighter than the commit times"), "not computed against each other by anyone before
    VERDICTS". A commit dated inside the run is not on that list, and the wording that makes it one can be avoided.
    I computed no bound. **Fix (Code's or the seat's call):** (a) keep it and add one line for the seat: the
    sentence dates 38f9974 inside the stage, and under Q4 nobody computes it against the launch stamp before
    VERDICTS; or (b) say "after the launch" (true by the boolean) and keep "not known to Code" for processes. (b)
    gives up the overlap claim.

19. **Claim:** mf3 and its driver import nothing from valence_core/p (checked by search). **Location:** E:26;
    P:49. **Verdict:** PASS, both directly and transitively. **Evidence:** a static transitive closure at acde2d8
    from scripts/mf3_sessions.py and valence_core/mf3/*.py, function-level and lazy imports included
    (vc/import_closure.py), reaches 47 repo files: the driver plus 46 modules in valence_core/{__init__,
    adapters/*, e2d/*, m/*, mf3/*, readout, session, session_e2a, stats}. None of them is under valence_core/p or is scripts/p_sessions.py, and
    none mentions `valence_core.p`, `valence_core/p` or `p_sessions`. Its dynamic-import sites reach no p module:
    qwen_mlx's mlx/jlens; m/audit.py's probe of scripts/box_b3_sessions.py, which imports no p; the driver's
    `valence_core.mf3.{m}`. At runtime, a fresh `-I` interpreter that imports all 14 mf3 modules and the driver
    (mlx/jlens blocked, nothing called) holds no `valence_core.p*` module. The stage also has no non-comment
    reference to RESULTS.md or results/raw, the two paths 38f9974 touched.

20. **Claim:** the stage's licence was checked at its start, on acde2d8. **Location:** E:27; P:50. **Verdict:** PASS.
    **Evidence:** W:9 "committed at HEAD acde2d837a17…, working tree identical; … hashed at stage start".

21. **Claim:** whether that session ran a process during the run is not known to Code. **Location:** E:28; P:50-51.
    **Verdict:** PASS (a disclosure; nothing to check).

22. **Claim:** the raw: local roots scrubbed, no finish stamp (the seat's G-TIME-F0 read, Q4). **Location:** E:29-30;
    P:52. **Verdict:** PASS. **Evidence:** item 50; W's only stamps are the launch stamp (W:2) and the PROVENANCE
    start stamp (W:10), both of which Q4 admits.

23. **Claim:** DRIVER line, verbatim; 890084e6…90af committed at HEAD acde2d8, working tree identical. **Location:**
    E:31; P:53. **Verdict:** PASS. **Evidence:** W:5, a full line; `git show acde2d8:scripts/mf3_sessions.py |
    shasum -a 256` = 890084e6c626a3ced2007c4285c255fb73978c07aeca15427172fc17028690af, the same at HEAD and in the
    working tree.

24. **Claim:** "It is the blob that LOCK-m-F3 v0.2 records." **Location:** E:31-32. **Verdict:** IMPRECISE (low;
    tense). **Evidence:** v0.2 does not exist (LOCK-m-F3.md at HEAD is v0.1, 377c5d60…). The record is the step-10
    read's Q2 condition as Code reads F-1 (driver PINs :72, :334), and P's Q4 puts v0.2's form, this record
    included, to the seat. **Fix:** "the blob LOCK-m-F3 v0.2 is to record (P, Q4)". E:45's "v0.2 records it
    (m:296)" is the proposal's own step and the stage's printed text, so it is fine.

25. **Claim:** the SNAPSHOT lines, verbatim; refs/main, one snapshot, `HF_HUB_OFFLINE=1`; the re-read unchanged, with
    the adapter's model_id the model of record. **Location:** E:33-34; P:54-55. **Verdict:** PASS. **Evidence:**
    W:6-7, full lines (W:6 differs from the pre-scrub line only by `<home>`). Recomputed now: the cache's refs/main
    is c000ac2c…, with one snapshot directory.

26. **Claim:** the GATE and LICENCE lines, verbatim, and E's LICENCE paraphrase (proposal 42ab36ec…, lock 377c5d60…,
    analyzer d347ea0c…, mf3's package f30ad505…, the eleven m files and the weights, hashed at stage start).
    **Location:** E:35-36; P:56-57. **Verdict:** PASS. **Evidence:** W:8-9, full lines. At acde2d8 the proposal's
    sha256 starts 42ab36ecc814c9c4 and CLAUDE.md's 955788dec22ee820; the analyzer is d347ea0c…5e48 in full; mf3's
    package hash recomputed is f30ad5053904ac22…6310; the report's eleven `m_module_sha256` values each stand
    beside their file in the lock's §1 table.

27. **Claim:** the six session lines, verbatim; A1s, a sham, prints class and phase (m:263). **Location:**
    E:37-38; P:58-60. **Verdict:** PASS. **Evidence:** W:11-16; m:263 "sham sessions print class and phase, no tag".

28. **Claim:** the two BAR lines, the CAP TRIGGER line and the STAGE line, verbatim. **Location:** P:61-64; E:39.
    **Verdict:** PASS. **Evidence:** each is a full line of W (17-20) and of the pre-scrub raw.

29. **Claim:** PROVENANCE `qwen3.6-27b-4bit-mlx`; MLX 0.31.2, mlx-lm 0.31.3, numpy 2.5.1; Python 3.12.9; macOS
    15.6.1; backend identifier a734dadec8f8ce9b, the same as G-TIME-F0's. **Location:** P:65-66; E:39.
    **Verdict:** PASS. **Evidence:** W:10; the report's `identity.backend_identifier` is a734dadec8f8ce9b, and
    data/m/reports/Q-F0_time_report.json:22 has the same value. Note: the identifier comes from the report, not
    from W's PROVENANCE line or the raw E:29 cites, which is the placement G-TIME-F0's values-check noted (R9).
    Optional: "(the report's identity)".

30. **Claim:** the identity read from the report: lock 377c5d60…6ce7, proposal 42ab36ec…6c6b, mf3's package
    f30ad505…6310, weights revision c000ac2c… with sha256 03922eed…1e26, renders a04f67b0e5105a05, pool
    711deec1c2645194, audit 7aa235d25eeb66dc, ban list a934f1ad2b702245, reasoning cap 60, path uncached, schedule
    sha256 25e2d23c…f31f. **Location:** P:67-72. **Verdict:** PASS. **Evidence:** the report's `identity`, field by
    field.

31. **Claim:** the bars (m:293; lock §8): planned ≤ 30 with critical 5 and ≤ 18 with critical 5; at the realised
    n = 25 and n = 13 the critical is 4; evaluated once at stage end on the sham sessions; the numerator is the union
    of m:265's three classes under the seat's Q8 echo set. **Location:** P:73-78; E:40-42. **Verdict:** PASS.
    **Evidence:** m:293; LOCK-m-F3.md §8 rows 4-5 (30 / 5 and 18 / 5; "once at stage end on the realised n");
    valence_core.m.bars.critical_k gives (25, .05) → 4 (P = .0341; 3 → .1271), (30, .05) → 5, (13, .10) → 4
    (P = .0342; 3 → .1339) and (18, .10) → 5.

32. **Claim:** "On Qwen the G-TIME bars bind alone" (m:271). **Location:** P:79. **Verdict:** PASS. **Evidence:**
    m:271, verbatim.

33. **Claim:** "Reported beside (m:293): the three contrast sessions' rounds and lines. Per the seat's F-6, the
    contrast sessions report no per-line list, and their free-round events and picks stay in the checkpoint until
    VERDICTS." **Location:** P:80-81. **Verdict:** IMPRECISE. **Evidence:** m:293 says so, but the seat's Q5
    (prebuild answers:36) narrowed it to "for the contrast sessions the forced rounds beside". F-6 (ganl-f3
    answers:29) then ruled that the session "contributes to the CAP TRIGGER total only … never the realised line
    total; the per-line booleans and the realised totals go to the checkpoint". The report carries, per contrast
    session, only `forced_rounds_generated` 4 and `excluded_at_forced` false. Their lines appear only inside W:19's
    "1 of <= 36". As written, the bullet implies the contrast sessions' rounds and lines were reported beside, with
    only the per-line list withheld. **Fix:** "Reported beside (m:293, as the seat's Q5 and F-6 narrow it): the
    contrast sessions' forced rounds (4 each, none excluded at a forced round); their lines only inside the CAP
    TRIGGER's k of ≤ 36, with no per-line list and no realised total (F-6); their free-round events and picks stay
    in the checkpoint until VERDICTS."

34. **Claim:** each contrast session generated its four forced rounds, none excluded at a forced round; the
    responses were identical (3, 24, 44, 12) and correct; rounds 3-4 presented corrupted task text under the Q-role
    config (`Cnmzote 11 + 33.`, `Coepqte 60 diyided by 5.`). **Location:** P:87-89; E:48. **Verdict:** PASS.
    **Evidence:** reads A1/A2/A3 `n_forced_rounds` 4, `excluded_at_forced` false, round texts 3/24/44/12. In the
    transcripts, the round 3-4 headers name the Q-role label (saddle, saddle, plaza), with those Task lines. Report
    `per_session` `forced_rounds_generated` 4.

35. **Claim:** the contrast banners and cells: A1 (pair 3, P ridge, Q saddle, clause 0) carries TOLD-MAP, quoted; A2
    (the same pair) carries TOLD-OBJ, quoted; A3 (pair 0, P granite, Q plaza) carries COMMON only. **Location:**
    P:89-94. **Verdict:** PASS. **Evidence:** the reads' `cell` and `banner` / `note_lines`; both quotes are exact
    (TOLD-MAP's first variant at m:255 with L_clean ridge and L_corr saddle; TOLD-OBJ at m:257).

36. **Claim:** the contrast sessions' free-round events and picks are withheld to Q-F3's VERDICTS (m:271, m:318;
    F-6). **Location:** E:48-49. **Verdict:** PASS. **Evidence:** the report's contrast `free_rounds` is "withheld to
    the unit's VERDICTS entry or NOT-RUN record (m:271)"; `timing.contrast_seconds` is "withheld … (m:318)".

37. **Claim (A1s):** pair 3, ridge/saddle, TOLD-MAP-SHAM; in domain; excluded `lexical@free`. Forced responses as
    quoted, the fourth "60 divided by 4 = 15." for a task of 60 divided by 5. One reasoning line `>` (round 5): 1
    token, ended by a newline. Round 5's response "31 + 4 `config: [config]` 31 + 46 = 77." names a label, is the
    lexical claim, and ends the session. First pick the P-role label (1/1); 109.1 s. **Location:** P:98-104; E:50.
    **Verdict:** PASS. **Evidence:** reads: `domain` true; `exclusion` {lexical, free}; round texts and
    `task_text` exact; the reasoning line has n 5, n_tok 1 and stop_reason newline; round 5's `audit.claim` is
    lexical; the session has 5 rounds; report `first_pick_P` 1/1; `seconds` 109.109. m:261 gives the claiming order
    (v2 → echo → v4 content → own-pair lexical). Note: the response's inner backticks are bytes-exact in the
    markdown source but render as a code span. P:108 uses a double-backtick span for the same reason (optional,
    for consistency).

38. **Claim (A2s):** pair 1, prism/slate, TOLD-OBJ; complete and valid, 10 rounds; responses "3", "24", "44", "12",
    "down", "77", "cold", "45", "2", "close", all correct and terse. Six reasoning lines: the banner at rounds 5, 6,
    8, 9 and 10, and `` === Config `[config]` evaluation === `` at round 7. First pick not P (0/1); 209.4 s.
    **Location:** P:105-109; E:51. **Verdict:** PASS. **Evidence:** reads (`complete` true, `excluded` false), exact
    texts, `n` per line; each answer fits its task; report `first_pick_P` 0/1; `seconds` 209.44.

39. **Claim (A3s):** pair 1, prism/slate, COMMON; complete and valid, 10 rounds; responses as quoted. Round 8's
    response to "Write the opposite of 'hot'." answers no task and no class claims it. Six reasoning lines: the
    banner at rounds 5, 6, 7 and 10, `=== Config selection ===` at 8, and at 9 the rationale, quoted (30 tokens).
    First pick not P (0/1); 392.5 s. **Location:** P:110-119; E:51. **Verdict:** PASS. **Evidence:** reads: exact
    texts; round 8's `audit.claim` is null; report A3s `degeneracy_rounds` 0; the line at n 9 has n_tok 30;
    `first_pick_P` 0/1; `seconds` 392.494.

40. **Claim:** the sham-template first-pick shares (m:318 exception (2)): A1s 1/1, A2s 0/1, A3s 0/1. **Location:**
    E:52; P:120. **Verdict:** PASS. **Evidence:** report `first_pick_P`; m:318 exception (2), verbatim in substance.

41. **Claim:** the reads, descriptive: A1s 1 read (1 at low label mass, 1 with a non-label top-1), A2s 6 (2), A3s 6
    (2). **Location:** P:121-122. **Verdict:** PASS. **Evidence:** report `reads` {n, low_label_mass,
    top1_not_label}: {1, 1, 1}, {6, 0, 2}, {6, 0, 2}.

42. **Claim:** the sham seconds 109.1, 209.4 and 392.5 (711.0 in all; 237.0 per session); the contrast sessions'
    seconds stay in the checkpoint. **Location:** E:53; P:183-184, P:186-187. **Verdict:** PASS. **Evidence:** the
    reads' `seconds` 109.109 / 209.44 / 392.494; the report's `timing.sham_seconds` 711.043 with `sham_sessions` 3,
    and `contrast_seconds` withheld (m:318); 711.043 / 3 = 237.01.

43. **Claim:** of the 13 sham reasoning lines, 9 contain (reproduce verbatim) the session banner (A2s 5, A3s 4); 2
    keep its frame; 1 is `>`; 1 is a selection rationale; "in the two complete sham sessions, most". **Location:**
    E:6, E:55-56; P:25-27, P:126-130. **Verdict:** PASS. **Evidence:** my count from the reads, using
    `valence_core.m.audit.ws_norm` and `valence_core.mf3.banner.SESSION_BANNER` ("=== Config evaluation session
    ===\n", normalized "=== Config evaluation session ==="). It finds 9 by containment, all 9 also exact (A2s n 5,
    6, 8, 9, 10; A3s n 5, 6, 7, 10). Frame only: 2 (A2s n 7, A3s n 8). A1s n 5 is `>` and A3s n 9 is the rationale.
    That is 9 of the 12 lines in A2s and A3s.

44. **Claim:** the audit gave every sham line the classes `[]`: none empty, none at the cap, none an echo.
    **Location:** P:131. **Verdict:** PASS. **Evidence:** all 13 lines have `classes` [], `defect` false,
    `cap_hit` false and stop newline; the report's `by_class` is all 0. Re-running `m_audit.harness_echo` over
    `lines.echo_lines(P, Q, n)` returns None for all 13.

45. **Claim:** the echo set (`valence_core/mf3/lines.py`, `echo_lines`; Code's PIN at LOCK-m-F3 v0.1, carrying the
    seat's Q8 and Code's N4) is m:258's eight strings: COMMON, TOLD-MAP ×2, TOLD-MAP-SHAM ×2, TOLD-OBJ, "Reasoning
    (one line):" and the "[round k | reasoning]" header for each k so far. It does not hold the session banner.
    **Location:** E:7, E:57-58; P:132-134, P:153. **Verdict:** PASS. **Evidence:** lines.py:34-48 (headers for k in
    5..n); its PIN at :37 cites Q8 and N4 and is listed at LOCK-m-F3.md:601; the build design's F25 reads "(Q8;
    N4)".

46. **Claim:** the seat's Q8, verbatim. **Location:** E:52-53; P:28-29, P:135-137. **Verdict:** PASS.
    **Evidence:** results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md:51, §8's first bullet, word
    for word.

47. **Claim:** m:258's quote, "Six banner lines (COMMON; TOLD-MAP ×2; TOLD-MAP-SHAM ×2; TOLD-OBJ); with the two
    reasoning-block lines, eight declared harness strings"; the session banner is not among them. **Location:**
    P:138-139. **Verdict:** PASS. **Evidence:** m:258 verbatim. m:253 names `SESSION_BANNER` separately, as "the
    template's banner".

48. **Claim:** m:265's quote ("reasoning-line echo = a verbatim, whitespace-normalized reproduction of any complete
    harness-written line of the session (v1.3's definition)") and its short forms. **Location:** E:59; P:30-31,
    P:140-141, P:154. **Verdict:** PASS. **Evidence:** m:265, verbatim except for its bold markup.

49. **Claim:** the session banner is written by the harness as each session's first line. **Location:** P:141-142.
    **Verdict:** PASS. **Evidence:** m:253's bytes `SESSION_BANNER + COMMON + …`; `banner.build_banner`; every
    transcript in the reads begins with it.

50. **Claim:** under m:265's wording the bar would read 9/13 against a critical of 4 at n = 13 and fire, with "STOP
    before G-ID-F3; the seat re-specifies (m:293)". **Location:** E:8, E:59-60; P:31-32, P:143-145, P:155.
    **Verdict:** PASS. **Evidence:** `valence_core.m.bars.critical_k(13, "0.10", "0.05")` = 4, and
    `fires(9, 13, "0.10", "0.05")` = True (P = 4.9e-7). Under m:265's full wording I tested every complete
    harness-written line of each sham session: the banner and Note lines, every round header and Task line, both
    reasoning-block lines, all four menu templates' lines for n = 5..10 in both label orders, and the pick line with
    either label. Only SESSION_BANNER is contained in any of the 13 lines, so the count is exactly 9 (the other two
    classes are 0). The quote is valence_core/mf3/bars.py:196's `on_fire`, which is LOCK-m-F3.md §8 row 5.

51. **Claim:** Code has not adjudicated; the PASS is computed under Q8's set as LOCK-m-F3 v0.1 declares. **Location:**
    E:61; P:146-147. **Verdict:** PASS. **Evidence:** item 45; nothing in E or P rules on it.

52. **Claim:** the contrast sessions' reasoning lines are withheld (F-6), so the pattern there is unknown before
    VERDICTS. **Location:** P:148-149. **Verdict:** PASS. **Evidence:** the reads' contrast sessions carry no
    reasoning lines (no `reasoning_lines` key; blinding "no per-line list"); F-6.

53. **Claim:** the three output files' sha256: checkpoint b809c087…8fc7, report 0c0563cf…bcce, reads 2efd9470…c5cb.
    **Location:** E:63-65; P:12-13, P:16-17. **Verdict:** PASS. **Evidence:** `shasum -a 256`:
    b809c0873840ee29878d7e09733a3771e8d13b0456cbe16bac5ca5edb87f8fc7 (checkpoint, hashed only);
    0c0563cfea64c2c5ff5185c931739ef49a89357bbe3b338dad7db48658b8bcce;
    2efd9470f03768dad6df867024e91fb046c9b4a43f9c3619296c5bfb6aeec5cb.

54. **Claim:** the checkpoint "is -diff". **Location:** E:63. **Verdict:** PASS. **Evidence:** .gitattributes
    `/data/mf3/ckpt/** -diff`; `git check-attr diff` gives unset.

55. **Claim:** LOCK-m-F3.md, committed at 1e79955, sha256 377c5d60…6ce7. **Location:** P:11; E:35. **Verdict:** PASS.
    **Evidence:** 377c5d602709004c862e7f8b5ae6b70a9d441b558697c47b0bf585ceaecf6ce7 at 1e79955, at HEAD and in the
    working tree.

56. **Claim:** the weights: revision c000ac2c…, sha256 03922eed…1e26. **Location:** P:69; E:36. **Verdict:** PASS.
    **Evidence:** the report's identity; the lock's WEIGHTS line (LOCK-m-F3.md:121). Recomputed now, read-only, with
    `valence_core.mf3.resume.weights_binding` on the cache's snapshot c000ac2c…: sha256
    03922eed43c73bf4af06cf4c51982005d95640dc6f39b57caf604749cf001e26, 6 files.

57. **Claim:** Q5's bases: 641.6–713.6 s per session for Q-F3 uncached, from §2.4 (m:230: "1.6 × 401–446 s"); 488 s is
    Q-F0's (m:205); A1s ended at round 5 and the other two ran all 10. **Location:** E:74; P:183-186. **Verdict:**
    PASS. **Evidence:** m:230 "641.6–713.6 s per session = 1.6 × 401–446 s" (m:230 lies in §2.4, m:178-252);
    1.6 × 401 = 641.6 and 1.6 × 446 = 713.6; m:205 "Qwen basis 488 s per session"; rounds 5 / 10 / 10.

58. **Claim:** Q5 carries the seat's G-TIME-F0 read, Q6: report beside the bases, not in place of them.
    **Location:** P:183, P:186. **Verdict:** PASS. **Evidence:** G-TIME-F0 read:53 ("reports the measured sham
    figures beside them, not substituted").

59. **Claim:** Q2: counter (c)'s domain is A3's first reasoning lines, and a banner line there is "not scored" (no
    stage-1 term). **Location:** P:161-166. **Verdict:** PASS. **Evidence:** m:312 (c). In scripts/m_analyze.py,
    :3441 holds `STAGE1_TERMS`, :3475 is the scored rule and :3961-3969 has the class "not scored". The banner
    tokenizes to ['===', 'config', 'evaluation', 'session', '===' ] ('=' is Sm, not punctuation), with no stage-1
    term.

60. **Claim:** Q3: m's remaining pre-load check was built at `time` as routed ("Build at time"), and the seat's F-2
    places it with the campaign subcommand's wiring. **Location:** P:168-170. **Verdict:** PASS. **Evidence:** F-2
    (ganl-f3 answers:25) "… and the rest of m's pre-load check arrive with the campaign subcommand's wiring";
    acde2d8's message ("Build at time"; the dated note quoting F-2).

61. **Claim:** Q4's particulars: v0.2 above the verbatim v0.1 (the G-TIME-F0 read, Q1); the driver history
    fad31c20…0cbb → 890084e6…90af; nine PIN sites at the driver's :72, :81, :98, :108, :221, :284, :334, :359 and
    :442; the revision refusal at `time` (REVISION_STAGES extended); the plural at :72. **Location:** P:172-181.
    **Verdict:** PASS. **Evidence:** G-TIME-F0 read:43. acde2d8's message gives the history and REVISION_STAGES.
    In the driver at acde2d8, "PIN (Code, declared at LOCK-m-F3 v0.2" opens exactly those nine lines. :72 reads
    "the step-10 read's Q2 condition" (singular), and the wiring values-check (item 33) left the plural to v0.2.

62. **Claim:** Q1's consequence: widening the set changes valence_core/mf3/lines.py, which moves mf3's package and so
    the lock's licence; G-ID-F3 needs the PI's word in any case. **Location:** P:157-159. **Verdict:** PASS.
    **Evidence:** lines.py is in the package `package_sha256` hashes (the licence compares it); the PI's routing
    item 1 ends its chain at G-TIME-F3.

63. **Claim:** the dates: Code, 2026-11-07 (PI-local), Code's stamps UTC 2026-11-08. **Location:** P:3. **Verdict:**
    PASS. **Evidence:** W:2 "2026-11-08 03:41:55 UTC" falls on 2026-11-07 PI-local.

64. **Claim:** Code did not open the checkpoint; the sessions are read from the report and the reads. **Location:**
    E:46-47; P:16, P:193. **Verdict:** PASS (not checkable; consistent). **Evidence:** every session figure in E and
    P is in the report or the reads. Neither contains a contrast free-round event, a contrast pick or contrast
    seconds.

65. **Claim (W):** W holds no local path, user name, session id, macOS temp-dir id or finish stamp, and differs from
    the pre-scrub raw only in path scrubs. **Location:** W. **Verdict:** PASS. **Evidence:** replacing
    `<repo>` → `<repo>`, then `<home>` → `<home>`, in gtime_raw.txt
    reproduces W byte for byte (159 bytes fewer; the diff is at lines 4, 6 and 21-23). The header's `<tmp>` was
    written by the wrapper itself (run_gtime.sh:13). A case-insensitive search for the identifying strings (the user's
    names, the home, private, var and tmp roots, the sandbox user directory, the session's id, the scratch folder's
    name, and pod and hostname patterns) finds nothing. (Code reworded this list before the commit so the raw does
    not spell them out.) The only stamps
    are the launch stamp (W:2) and the PROVENANCE start stamp (W:10); there is no finish stamp. Both files have 24
    lines and end in a newline.

66. **Claim:** E and P agree. **Location:** E throughout; P throughout. **Verdict:** PASS. **Evidence:** every figure
    E gives (bars, cap, counts, first picks, seconds, hashes, Q1-Q5, the disclosure) matches P. The disclosure's
    three points match, E adding "(checked by search)".

## Totals

66 items: 61 PASS, 5 IMPRECISE, 0 FAIL.

Non-PASS: 7 (E:12-13, "ends"), 13 (P:41-42, the header and the gate line; low), 18 (E:24 / P:48, "During the run":
blinding hygiene), 24 (E:31-32, "v0.2 records"; low), 33 (P:80-81, "Reported beside").

## Code's dispositions (2026-11-07; each item re-checked at source before it was applied)

- **7:** the entry now says item 1 "has the chain '… → LOCK-m-F3 v0.1 → G-TIME-F3 [go]; …'". Item 1 continues past the
  chain.
- **13:** the ping now says the gate line is the driver's own, logged by the stage. The header does not record it.
- **18 (blinding):** option (b). The entry and the ping now say "After the launch, another session committed
  `38f9974`", and that the commit is placed only after the launch, since Q4 of the seat's G-TIME-F0 read keeps
  records from bounding the stage's time. Nothing dates the commit against the stage's end.
- **24:** "the blob LOCK-m-F3 v0.2 is to record (the ping, Q4)".
- **33:** the ping's "Reported beside" now reads as the seat's Q5 and F-6 narrow m:293:
  - the contrast sessions' forced rounds;
  - their lines only inside the CAP TRIGGER's k of ≤ 36, with no per-line list and no realised total;
  - their free-round events and picks in the checkpoint.
- **The optional notes:**
  - item 29: the entry names the backend identifier's source, the report's identity;
  - item 37: the A1s round-5 quote is a double-backtick span;
  - item 6: "m:296 has v0.2 record it";
  - item 14: the entry says the dry check's output is in Code's session only, as at G-TIME-F0;
  - item 15: no change.
