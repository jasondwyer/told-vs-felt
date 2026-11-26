# The Q-F3 campaign's record (its raw and its entry): the blind values-check, two passes (their briefs, the checker's reports, Code's dispositions)

*F3 session, Code's date 2026-11-25. Two blind passes checked the record, each by a subagent under its own brief. Each
brief quotes the list of record v2's items 1–5 and bars any count of the contrast arms' free-round exclusions.*

*The first pass began at HEAD `0081351`. The entry changed while it ran: the coordinating session's points on the run
list arrived. So it graded a 263-line state of the draft. The second pass, at HEAD `05ac941`, checked the revised
text, v3 (`a3e185d8…e13b`), whole, and was not given the first report. The committed entry is v4: v3 with the second
pass's findings applied.*

*The briefs are verbatim, their local paths scrubbed: `<tmp>` is the scratch root and `<repo>` the repository. The
briefs' sha256 as given to the checkers, before the scrub, were `77c8862b…d5aa` (64 lines) and `55353e80…7dfd` (68
lines). The reports are verbatim and hold no local path. Each report's sha256 is the checker's own, re-derived by Code
from the checker's hand-back: `859e0d22…90d6` (165 lines) and `9f152681…ed39` (166 lines). Code's dispositions follow
each report.*

----------------------------------------------------------------------------------------------------
Pass 1: the brief (verbatim; local paths scrubbed)
----------------------------------------------------------------------------------------------------
You are a blind values-checker for a research project's records, in the git repository at <repo>. Other sessions share this working tree and may commit while you work; do not modify it.

You are read-only:
- no git writes of any kind (no add, commit, stash, checkout, reset, worktree or switch; `git hash-object` only without `-w`);
- no file written or edited anywhere;
- no model run, and no run of any repository script (`scripts/*`, `valence_core/*`) in any form;
- no Python at all, not even `python3 --version` or `python3 -c`: shell utilities only (jq, awk, sed, /usr/bin/grep, shasum, diff, cmp, wc -l, sort, uniq, git). A Python start on this laptop needs a window you do not have.

Return your report as text in your final message, between a line `=== BEGIN REPORT ===` and a line `=== END REPORT ===`, and give its sha256 (over the text between the markers, as UTF-8, ending in one newline), computed in the shell, for example by a quoted here-document piped to `shasum -a 256`. Write it to no file.

## The list of record v2, items 1–5 (verbatim; they bind you)

1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.

Also binding:
- **For any file under `data/*/ckpt`, digest forms only** (the seat's ruling of 2026-11-15): `shasum -a 256`, or `git hash-object -- <path>` compared with `git rev-parse <rev>:<path>`. Never open, read, search or `git show` such a file, and never print its size or time. This check needs one: `data/mf3/ckpt/Q-F3_campaign.json` (untracked), by `shasum -a 256` only.
- **The reports are the read domain** (item 2). You may read the content of `data/mf3/reports/Q-F3_campaign_report.json` (untracked) and `data/mf3/reports/Q-F3_qual_report.json` with `jq`, to check the draft's figures. Print from them only what you need to confirm or refute a claim in the draft. Never print the `sham_generation_ms` values, a `provenance` stamp, or any size or time of a file.
- **The blinding of the contrast arms' free rounds (m:271, m:263, m:318).** The contrast arms are A1, A2 and A3. Their session lines in the raw that end in `excluded:excluded@free` are free-round exclusions whose count is withheld until VERDICTS. Do not count, tally, list or derive them in any form: not per arm, not in total, not as "valid" against "excluded", not by subtraction from launches. For a contrast arm, work only with its launches, its lines ending in `@forced`, its pre-pick exclusions and its domain (the report's `arms`). The sham arms (A1s, A2s, A3s) carry no contrast information: you may split them fully, every label included. The draft states the same rule; it binds your commands and your report.
- `jlens-qwen36/` is a separate repository: run no git command inside it.
- No clock time, time stamp or span in your report, and nothing computed from two stamps.

In practice, for this task:
- Every content search over the checkout or a tree carries item 3's tested form. `grep -r` and `rg` prune the `ckpt` and `reports` directories under `data/`.
- Use no `--stat`, `--numstat` or `--shortstat` form anywhere.
- Do not open anything under `<tmp>/../tasks/`, any session transcript (`*.jsonl`), or any memory folder.
- The Bash tool's `grep` is ugrep: use `/usr/bin/grep`.

If you break any of this by accident, say so at the end of your report: give the command's kind and what printed, without reproducing anything that printed.

## What to check

Code (another session) has drafted the record of a finished campaign, the Q-F3 campaign. Nothing is committed yet. Check every factual claim against its sources: every quote, figure, hash, path, commit id, line count, date and attribution.

C = <tmp>/a6/record . The drafts:
1. `C/entry_draft.md`: the RESULTS.md entry, to go at the head of RESULTS.md's "## Log — Phase 2". `@@RUNLIST@@` and `@@VCRAW@@` are placeholders (the second names this check's own raw): grade each NOT CHECKABLE.
2. `C/2026-11-15_mf3-campaign-qf3.txt`: the raw, to be committed as `results/raw/2026-11-15_mf3-campaign-qf3.txt`.

The sources:
- **The wrapper's raw as the run left it:** `<tmp>/a6/launch/campaign_raw_1.txt`. The draft claims its sha256 and line count, and that the committed raw is this file with four local roots scrubbed, then the (d) block. Check that exactly: which lines changed, and how.
- **(d)'s output:** `<tmp>/a6/launch/d_1.txt`.
- **The report:** `data/mf3/reports/Q-F3_campaign_report.json` (read domain, above); G-F3's, `data/mf3/reports/Q-F3_qual_report.json`, for the identity comparison.
- **The checkpoint:** `data/mf3/ckpt/Q-F3_campaign.json` (digest only).
- **LOCK-m-F3.md:** v1.0 §1, §2, §4, §5, §6, §12, §13; v0.2 §8; lock §8's bar table, rows 9–13; lock §9's row F35.
- **The seat's raw** `results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md`: §0, §2.2, §2.3, §2.4, §9.
- **The PI's routing,** section A item 3, verbatim as the committed values-check raw `results/raw/2026-11-15_qf3-close-lines-campaign-go_valuescheck.md` quotes it (its lines 65–68). That is the only record of it in the repository.
- **RESULTS.md** at HEAD: the campaign wiring's entry (it begins "- 2026-11-15 — **The campaign wiring: `campaign`") with its close, and the Q-F0 campaign's entry (it begins "- 2026-10-19 — **THE Q-F0 CAMPAIGN"), whose form the draft follows.
- **The code,** read-only: `scripts/mf3_sessions.py` (the PIN at line 227 and the constants below it), and `valence_core/mf3/stages.py` (`_schedules_sha` at line 579, and the schedule loader just above it).
- **git:** the commits named (`3f017d8`, `a89a4fa`, `a215c28`, `41bfab4`, `0081351`, `fa27c45`), ancestry, and `git diff --name-only 41bfab4 HEAD` over the paths the draft names.
- **Not in the repository (grade NOT CHECKABLE unless a repository record bears on it):** the coordinating session's messages ("launch cleared", "windows closed", the +30 min form), and Code's attestation of its own calls during the run, made from its session transcript, which you may not open.

Pay special attention to:
- every number in the entry's tables and lists, against the raw's lines and the report: launches, `s=` ranges, pre-pick exclusions, domains, BAR figures and critical values, the smallest P per bar and the look it falls at, read flags, `beside` counts, and the sham arms' label splits;
- that the draft counts none of the contrast arms' free-round exclusions anywhere, and that nothing you write does;
- the identity: the report's identity keys against G-F3's report identity, the lock's sha256, the schedule hash (rebuild it in the shell from the six campaign schedule files by `_schedules_sha`'s definition), and `schedule_n`;
- the scrub: that the committed raw differs from the wrapper's raw only on the lines the draft names, only by the scrubbed roots, plus the appended block;
- that every quote is verbatim, and that the draft states nothing as a rule or a precedent that no record states;
- no clock time, time stamp or `$` figure in the entry (file:line anchors such as `m:267` are not clock times). The raw's PROVENANCE line carries the report's start stamp, which the draft names as one of Q4's records: do not print it;
- line widths: no entry line over 120 characters, except table rows and the verbatim block quote.

Grade each claim CONFIRMED, IMPRECISE (true in substance, but the wording or anchoring is off; say the fix), FAIL (wrong; say what is right) or NOT CHECKABLE (say why). Number your items and give file:line evidence. End with a tally and the list of everything not CONFIRMED. State HEAD (`git log --format='%h' -1`) at your start and at your end.
----------------------------------------------------------------------------------------------------
Pass 1: the checker's report (verbatim)
----------------------------------------------------------------------------------------------------
Blind values-check: the Q-F3 campaign's record (entry draft and raw draft)

HEAD at start: 0081351. HEAD at end: 05ac941 (another session's commit landed during the check; see O2).

Graded:
- E = C/entry_draft.md as it stood from mid-check to the end: 263 lines, sha256 bed2aa80…4b37 (it changed once during the check; see O3).
- R = C/2026-11-15_mf3-campaign-qf3.txt: 789 lines, sha256 c402e79d…cbb7, unchanged throughout.

Sources: W = <scratch>/a6/launch/campaign_raw_1.txt; D = <scratch>/a6/launch/d_1.txt; REP = data/mf3/reports/Q-F3_campaign_report.json; QREP = data/mf3/reports/Q-F3_qual_report.json; LOCK = LOCK-m-F3.md (untouched since a89a4fa); m:N = PROPOSAL-m-gating-campaign-v1_11.md line N; SEAT = results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md; VC15 = results/raw/2026-11-15_qf3-close-lines-campaign-go_valuescheck.md; r2 = results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md; GT0 = results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md; A7 = results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md; RES = RESULTS.md at 0081351 (every RES anchor is there; see O4); STG = valence_core/mf3/stages.py; DRV = scripts/mf3_sessions.py. The checkpoint was hashed only. For the contrast arms I used launches, lines ending "@forced", pre-pick counts and REP's arms; only the sham arms were split.

The header (E:1–5)
1. CONFIRMED. E:1–2, the anchors and "COMPLETE, exit 0, in one invocation": m:298; m:361 (step 19 runs to the campaign); VC15:56, :65–68; REP status COMPLETE, terminal COMPLETE at 596; R:781 is R's only EXIT line and R:40 its only INVOCATION line; R:1 "its first invocation".
2. CONFIRMED. E:2–3, 596 launches (A1 95, A1s 40, A2 162, A2s 70, A3 165, A3s 64) and each domain at its floor: R's session lines per arm = REP arms.launched; REP arms.domain = REP floors (80, 32, 144, 56, 144, 56).
3. CONFIRMED. E:3–4, fifteen looks, 135 BAR lines, all silent, no pause, no STOP: R has 135 BAR lines, labels look=1 to 14 and end, nine each, "silent" in all 135; REP looks_count 15, fired false at every look, pauses [], stop null; no PAUSE or STOP line in R.
4. CONFIRMED. E:4–5, (a′) and (d) EQUAL at a734dadec8f8ce9b, and the VERDICTS session's wait: R:39, R:789; REP identity.backend_identifier; LOCK:153; LOCK:317 (v1.0 §13 item 4).

The words (E:6–20)
5. CONFIRMED. E:7–8: VC15:56 (the relay's header, PI date 2026-11-15, and the PI's "Route as given"); SEAT's sha256 is 1f3ce1f9…f84b; SEAT was added at a215c28.
6. CONFIRMED. E:10, section A item 3: byte-equal to VC15:65–68 with the wrapped lines joined by single spaces (shell comparison).
7. CONFIRMED. E:12–14, the seat's §2.3: SEAT:31–34.
8. CONFIRMED (in substance). E:16: RES:14884–14887 (the push moved origin/main to fa27c45); RES:15312–15314 (the PI's "Auto updates are off.", the setting read back); RES:15323 (the launch waits for the push and for the PI's word on item 1). The message "launch cleared" itself is not in the repository.
9. CONFIRMED (in substance). E:17–18: RES:15321 (every window closes before each launch or resume); RES:14847 ("when the windows closed for Q-F3's launch"); LOCK:314–315 (announced to the coordinating session). The messages are not in the repository.
10. CONFIRMED (in substance). E:19, a PID-only mid-run check reported to the coordinating session: RES:15321–15322 (the windows reopen when the F3 session reports the PID alive after the launch, read by the PID alone). The message is not in the repository.
11. NOT CHECKABLE. E:20, (d) first, then the outcome to the coordinating session: no repository record of that order.

The run (E:21–53)
12. CONFIRMED. E:21, the raw's path and link: the brief's commit path; the link in the Q-F0 entry's form (RES:23322). The date in the file name was not checked: that would set it against Q4's records.
13. CONFIRMED. E:21–23: R:2, R:41 (committed at HEAD 41bfab4, working tree identical), R:44–45, R:778 (path=uncached); 3f017d8 is the driver's last change and its blob equals the working tree; LOCK at a89a4fa hashes to fe9518c7…1aa6; REP identity path uncached, reasoning_cap 120.
14. CONFIRMED. E:24–26: R:42 (refs/main; "1 snapshot(s) in the model's cache repo"; HF_HUB_OFFLINE=1), R:43 (re-read after the load, unchanged); REP weights_revision; LOCK:157.
15. CONFIRMED. E:27–28: R:40–46 in that order, R:47 the first session line; GT0:49 lists the report's PROVENANCE start stamp among the records; R:46's record and stamp equal REP provenance[0]'s (compared, not printed).
16. CONFIRMED. E:29–38: in R, each arm's s runs from 0 to 94, 39, 161, 69, 164 and 63, each value once, with the counts tabled. "Interleaved by §2.1's rule" as R:1 and RES:15461 state it; R's first 24 launches rotate A1, A1s, A2, A2s, A3, A3s (not re-derived further).
17. CONFIRMED. E:40–41: LOCK:55–56 and :67 (m:192 verbatim); REP launch_counts_projection; DRV:250; m:330 ("21 at 832").
18. CONFIRMED. E:42–43: REP floors and arms; LOCK:57; valence_core/mf3/schedule.py:44 (A1 80 uncached); 95−15, 40−8, 162−18, 70−14, 165−21, 64−8 give the domains.
19. CONFIRMED. E:45–50: REP terminal, hour_cap_reached false, pauses [], stop null; R:778 verbatim, R:779–781; no RULING string in R; a names-only listing of data/mf3/ckpt shows no excerpt beside Q-F3_campaign.json.
20. CONFIRMED. E:51–52: each named kind counts 0 over R's non-header lines (and 0 in its header); each exists in the code (STG, valence_core/mf3/resume.py, DRV).
21. CONFIRMED. E:53: R's header lines are 1–39 and 782–789 (47); the other 742 open with INVOCATION, DRIVER, SNAPSHOT (2), GATE, LICENCE, PROVENANCE, STAGE, CHECKPOINT, REPORT, EXIT=0 (11), campaign (596) and BAR (135).

The looks and the monitors (E:54–106)
22. CONFIRMED. E:54: REP's 135 bar messages (looks 1–14, then the end) are byte-equal, in order, to R's BAR lines (cmp).
23. CONFIRMED. E:55: the session lines before each look's first BAR line number 40, 80, … 560, then 596; REP looks[].at_launches and end_look.at_launches agree; m:330.
24. CONFIRMED. E:56: nine per look in R and in REP's results, all silent: the three sham bars and two guard bars per contrast arm.
25. CONFIRMED. E:57: LOCK:1205–1209 ("PAUSE the unit for the seat's adjudication; never a verdict").
26. CONFIRMED. E:58: LOCK:1205–1207 ("cumulative count, alpha .05 per look, no alpha spending"); m:330.
27. CONFIRMED. E:59–62: R:769–771; REP end_look.results (critical 92, 101, 33); domains LOCK:1205–1207; REP beside: sham rounds 342+601+587 = 1530 with degeneracy 7+14+14 = 35, and A2s+A3s rounds 601+587 = 1188 with lexical 4+2 = 6.
28. CONFIRMED. E:64–65: in R the three sham bars read 35/1530, 25/853 and 6/1188 at looks 10 to 14 and the end, against 34/1470, 24/817 and 6/1128 at look 9; the sham arms' last launches fall at launch 236 (A1s), 360 (A3s) and 383 (A2s); look 10 is at 400.
29. CONFIRMED. E:66–67: m:316; LOCK:1208–1209; R's guard lines.
30. CONFIRMED. E:69–73: R:772–777; REP end_look.results (k, n, critical 27, 42, 43).
31. CONFIRMED. E:75–87: each minimum over R's fifteen looks and its look are as tabled, in ascending order.
32. CONFIRMED. E:89.
33. CONFIRMED (by inference). E:90–91: status COMPLETE, stop null and no STOP line (REP carries no hair-trigger rows); LOCK:1197–1199 ("STOP the stage (m:271)"); m:271; m:284.
34. CONFIRMED. E:92–96: REP arms.prepick_excluded (15, 18, 21; 8, 14, 8) equals R's per-arm count of lines ending "@forced"; no session line contains "reason"; m:318; LOCK:1208 (pre-pick means at a forced round or at reasoning line 1).
35. IMPRECISE. E:97, "each look's values are in its `looks`": REP's looks holds 14 entries, looks 1 to 14; the end look's values are only in end_look (looks_count 15). Fix: "looks 1–14's values are in its `looks`, the end's in `end_look`".
36. CONFIRMED. E:98–102: REP end_look.arms read_flags as stated; scopes "first reads of domain sessions" and "all reads"; the contrast reads equal the domains; STG:1396–1407 counts a contrast arm's first read per domain session only.
37. CONFIRMED. E:103–106: REP end_look.beside as stated; scopes "forced rounds only" and "all task rounds"; STG:1430–1436.

m:271's redactions (E:107–131)
38. CONFIRMED. E:107–109: m:271 (free-round events "withheld to the unit's VERDICTS entry or NOT-RUN record"); m:263; m:318; the Q-F0 entry's form, RES:23408.
39. CONFIRMED. E:110–111: LOCK:1276 (F35, ruling (h)); m:263; R's form `excluded:<reason>` (sham lines, e.g. R:48).
40. CONFIRMED. E:112–113, the entry counts none of them and gives the domains pooled: no contrast free-round figure appears anywhere in E.
41. FAIL. E:113, "(below, item 2)": the withheld-count departure is item 3 (E:247); item 2 is "(d) ran in shell" (E:245). Right: "(below, item 3)".
42. CONFIRMED. E:114–115: a names-only listing of data/mf3/reports holds no campaign reads file; REP has no first-pick key; RES:15488 ("No reads file."); m:318's exception (2) names G-TIME and qualification stages only; m:361 lists the reads among VERDICTS' contents.
43. CONFIRMED. E:116–122: R, sham arms split by label: A1s 31 valid, audit@forced 3, content@forced 4, lexical@forced 1, lexical@free 1 (40); A2s 53, 7, 6, 1, 3 (70); A3s 55, 4, 3, 1, 1 (64).
44. CONFIRMED. E:124: m:318 ("picks go to checkpoint files"); RES:15487; its digest at item 83. "Not opened" is an attestation.
45. CONFIRMED. E:125–128: E quotes no seconds, duration or millisecond figure; sham_generation_ms is a key of REP (name only), not quoted; LOCK:235.
46. CONFIRMED. E:129–130: GT0:49 (the commit times, the report's PROVENANCE start stamp, the entry's own stamps); r2:41 carries the rule to the campaign; LOCK:568–572 (v0.2 §8 cites r2 §4, Q4).
47. CONFIRMED. E:131, no launch stamp and no finish stamp: located by line number only, R's one time stamp is R:46's, the report's start stamp; R:1 "No stamp."; R's other dates (R:1, R:7, R:782) are the seat's and the PI's calendar dates.
48. NOT CHECKABLE. E:131, "The commit message restates no stamp.": the commit is future.

The launch (E:132–186)
49. CONFIRMED. E:133–135: R:7–39; R:11–36's G-F3 values equal QREP's provenance record (compared without its stamp); SEAT:27.
50. IMPRECISE. E:136–137, "The identifier from the fields now": R:37 has "from the fields now, n_layers as G-F3 recorded it". Fix: add "with n_layers as G-F3 recorded it (the header's line 37)". The two equalities hold (QREP identity; LOCK:153).
51. CONFIRMED. E:138–139: R:1, R:6 (a_prime.py, 66e7d72d…f617), R:8 (the model libraries blocked), R:7–39.
52. CONFIRMED. E:140–141: R:1.
53. CONFIRMED. E:142–148: R:1 ("No departure from the checklist"; "caffeinate -is leaves display sleep only; the gate line is the driver's own"), R:4, R:5, R:44; m:267's checklist.
54. CONFIRMED. E:149–150, the command as written: R:1 verbatim; m:267.
55. NOT CHECKABLE. E:150–151, the PID echo on the next line, both in launch_campaign.sh, run with /bin/zsh: the launcher is gone; Code's transcript.
56. NOT CHECKABLE. E:152, PID=7989 and ps -p: in neither R nor any committed record.
57. CONFIRMED (in substance). E:153: R:1 (the wrapper "writes this raw"; (a′) "runs below, right before the campaign; nothing launches unless it is EQUAL"). The exit-0 mechanism is not checkable: the wrapper is gone.
58. NOT CHECKABLE. E:154–158: session actions. R:782 bears on the last part ("Before it ran, the PID and the campaign's processes were gone (ps, pgrep)").
59. NOT CHECKABLE. E:159–160: the coordinating session's check.
60. NOT CHECKABLE. E:161–170: Code's attestation from its transcript.
61. NOT CHECKABLE. E:171–174, the run list's scope as the coordinating session set it: no committed record states it.
62. CONFIRMED. E:175–177: r2:41 verbatim; r2:1 and :38 (the seat's read of G-TIME-F3's re-run, §4).
63. NOT CHECKABLE. E:177–180: the coordinating session's reading and "No stamp was compared with the end". The cross-reference "(below, item 4)" is right (E:255).
64. CONFIRMED. E:181–184: RES:9904–9906 (732a58f's entry: a name-only ls by a glob put a guard marker in ls's argv; non-Python, read-only, names only; logged for Q-F3's run list); RES:10426–10429 (1272702's entry: a git show … | shasum -a 256 call in a loop; non-Python, model-free, read-only; logged for Q-F3's run list). Both commits lie in 41bfab4..0081351.
65. IMPRECISE. E:185–186 with E:181: RES:10885–10888 (f3e7190, the pod session's close line on 6df2131's entry) says the output and exit status "were discarded" and that it "loaded no model and carried no marker word in its argv". Fixes: "loaded no model", not "loaded nothing"; it is disclosed in a close line on 6df2131's entry, not in an entry of its own (E:181's "each … in its own entry"); and unlike the other two, its record does not say it was logged for Q-F3's run list (that part is not checkable).

The tree (E:187–191)
66. CONFIRMED. E:187: git rev-list --count 41bfab4..0081351 is 104. No subject in that range names the F3 session, and no data/mf3 or mf3 raw path changed in it; attribution beyond that is not checkable. HEAD has since moved (O2).
67. CONFIRMED. E:188–189: git log over those paths in 41bfab4..0081351 lists no commit, and git diff --name-only 41bfab4 0081351 over them lists no file.
68. IMPRECISE. E:190, "Among the paths checked, only valence_core/n changed": E does not name the paths checked. Under valence_core/ only valence_core/n changed (16 files), but scripts/n_analyze.py, scripts/n_sessions.py, scripts/p_verdicts_counters.py and files under data/n, data/p and data/olmo changed in the range too. Fix: "Under valence_core/, only valence_core/n changed", or name the set.
69. CONFIRMED. E:191: git status --porcelain over the named paths shows only the two untracked campaign outputs; DRV hashes to 7bb6f7ca…28a4.

The driver and the identity (E:192–213)
70. CONFIRMED. E:192–194: R:41; RES:15443 and :15457–15459; DRV at a89a4fa hashes to 285eed04…0e44; LOCK:164.
71. CONFIRMED. E:196–197: REP lock_sha256; LOCK's sha256; git hash-object equals git rev-parse 0081351:LOCK-m-F3.md (and at the later HEAD).
72. CONFIRMED. E:198–200: rebuilt in shell by STG:579–581's definition (one line "name sha256" per file, sorted by name, sha256 of the UTF-8 body) over the six campaign files: 8e2b1193…ffba, REP's value. Each file is committed-clean, and its sha256 equals the manifest's and LOCK:122–127's.
73. CONFIRMED. E:201: REP identity.
74. CONFIRMED. E:202–204: REP identity; R:782–789; SEAT:28 verbatim ("in the campaign's raw").
75. CONFIRMED. E:205–206: compared key by key with QREP's identity, the nine keys named are equal; path, reasoning_cap and backend_identifier are equal too; lock_sha256 and schedule_sha256 differ, as they should (G-F3 ran under v0.2 on its own schedules).
76. CONFIRMED. E:207–210: REP unit, stage, hour_cap (v1.0 §2's cap), form verbatim, schedule_n equal to LOCK:122–127's n and to each schedule file's n.
77. CONFIRMED. E:212–213: R:45 printed ("hashed at stage start") and R has no REFUSED line; git log a89a4fa..0081351 -- LOCK-m-F3.md lists no commit (a89a4fa touched it; 05ac941 did not). "The checkpoint's identity was not opened" is an attestation.

The outputs (E:214–228)
78. CONFIRMED. E:215–216: shasum and wc -l on R.
79. CONFIRMED. E:217–218: shasum and wc -l on W.
80. NOT CHECKABLE. E:218–219, the copy in the shared notes folder: outside this check's sources.
81. CONFIRMED. E:220–222, the scrub: C/raw_scrubbed.txt (781 lines, sha256 25e9954c…6349) equals R:1–781 (cmp). W and R differ on exactly lines 40, 42, 779 and 780, one root each; W with the repository root replaced by <repo>/ and then the home folder by <home>/ equals R:1–781 (cmp); no local root remains in R (the <tmp>/ on R:1 and R:6 is W's own). G-F3's raw, results/raw/2026-11-12_mf3-gf3.txt, has <repo>/ on its INVOCATION, CHECKPOINT, REPORT and READS lines and <home>/ on its SNAPSHOT line.
82. IMPRECISE. E:223, "Then come (d)'s eight lines.": the appended block, R:782–789 (equal to C/d_block.txt), is a header line written for the raw (R:782) and (d)'s seven output lines (D has 7 lines), each prefixed "#   " (cmp). Fix: "Then the (d) block's eight lines: a header line and (d)'s seven output lines".
83. CONFIRMED. E:224–227: REP b4b48567…98d3 and the checkpoint 5ef02616…f92f, the checkpoint by shasum only.
84. NOT CHECKABLE. E:228: a placeholder.

The departures (E:229–258)
85. CONFIRMED. E:230–231, a scratch cleanup by age: results/raw/2026-11-06_gcal-olmo_valuescheck.md:489 and results/raw/2026-11-22_n-gver-v1_launch-review.md:315 state the age rule; results/raw/2026-11-09_a-m2-smoke-driver_reviews.md:139 names the scratchpad's cleanup. See O1.
86. NOT CHECKABLE. E:231, "by their modification time": in no repository record.
87. NOT CHECKABLE. E:232–235, what was removed and found missing: consistent with <scratch>/a6/launch/ now holding only campaign_raw_1.txt and d_1.txt (names only), with R:1 and R:6 placing run_campaign.sh and a_prime.py there, and with R:782–783 on d_check.py; launch_campaign.sh, prelaunch_check_campaign.py and the outputs appear in no record.
88. CONFIRMED. E:237 and E:240–241: R:6–39; DRV and STG committed-clean; R:781.
89. NOT CHECKABLE. E:238–239, the wrapper's body and zsh's parse: the wrapper is gone.
90. NOT CHECKABLE. E:243, the kit's bytes in Code's transcript.
91. CONFIRMED. E:244: R:6–39.
92. CONFIRMED. E:245: R:782–783.
93. IMPRECISE. E:246, "Its output is the raw's last eight lines.": (d)'s output is seven lines (D), R:783–789; the last eight include the block's header line, R:782. Fix: "Its output is the raw's last seven lines, under a one-line header".
94. NOT CHECKABLE. E:248–252: terminal output and messages.
95. CONFIRMED. E:253–254: RES:23414 verbatim ("This entry counts none of them"); m:271, m:263, m:318 as at item 38.
96. NOT CHECKABLE. E:255–256: the coordinating session's reading.
97. NOT CHECKABLE. E:257–258: R:782 bears on ps and pgrep only.

What follows (E:259–262)
98. CONFIRMED. E:260: LOCK:314.
99. IMPRECISE. E:261: the quote is verbatim (LOCK:317; A7:50, sha256 6b963adf…db3a), but "the seat's §A.7" is the seat's answers of 2026-11-14, while E's other "seat's §" anchors (E:12, E:133, E:203) are to the answers of 2026-11-15, which have no §A.7. Fix: "(the seat's answers of 2026-11-14, §A.7, as v1.0 §13 item 4 quotes it)".
100. NOT CHECKABLE. E:262: future.

Form (E)
101. CONFIRMED. Line widths: only E:10, the verbatim block quote, exceeds 120; every other line is at most 120 bytes, so at most 120 characters.
102. CONFIRMED. No clock time, time stamp or $ figure: none; the one "$" is shell text (E:150); the dates are calendar dates. See O1 on one span.

The raw draft beyond the scrub (R)
103. CONFIRMED. R:782–789 equals C/d_block.txt, and R:783–789 equal D's lines prefixed "#   " (cmp); R:782's anchor (SEAT:28) and "jq and grep, no interpreter" stand.
104. NOT CHECKABLE. R:782, "the PID and the campaign's processes were gone (ps, pgrep)" and the cleanup's removal of d_check.py.
105. CONFIRMED. R:784–789, (d)'s values: HEAD 0081351 was HEAD at this check's start; LOCK-m-F3.md was committed-clean there; exactly one lock line has v1.0 §5's form (LOCK:153; three lines name the identifier); both identifiers are a734dadec8f8ce9b.
106. CONFIRMED. R's header records checkable now: R:2 (HEAD, the driver's sha256); R:3 (G-F3's checkpoint digest equals LOCK:139; G-ID-F3's artifact hashes to LOCK:138's value); R:9 (qwen_mlx.py last changed at 7da9509 and __init__.py at 1465b34, both before 2193832; QREP clean at 41bfab4, its sha256 LOCK:140's); R:10 (QREP has one provenance record); R:11–36 (G-F3's values are QREP's); R:38 (LOCK:153 byte for byte); R:40, R:44, R:45 (the analyzer, package, renders, proposal, CLAUDE.md and A-m2 v0.5 digests equal the files and LOCK:116–132).
107. CONFIRMED. R:46: its record and stamp equal REP provenance[0]'s (compared, not printed); REP's entry adds a "launched" key.
108. NOT CHECKABLE. R:4–5: readings at the launch (power, disk, HF_HUB_OFFLINE, the process probe); R:5's probe is G-F3's form (results/raw/2026-11-12_mf3-gf3.txt:5).

Tally: 108 items: 79 CONFIRMED, 7 IMPRECISE, 1 FAIL, 21 NOT CHECKABLE.

Not CONFIRMED:
- FAIL: 41.
- IMPRECISE: 35, 50, 65, 68, 82, 93, 99.
- NOT CHECKABLE: 11, 48, 55, 56, 58, 59, 60, 61, 63, 80, 84, 86, 87, 89, 90, 94, 96, 97, 100, 104, 108.

Observations
O1. Timing, for the drafter and the seat. E:230–231 state the cleanup's age threshold, and E:232–235 say the outputs written at the launch were removed by it and found missing at the end, the raw alone kept fresh by its session lines. Read together, they let a reader set a lower bound on the run's length from time records (the outputs' write times and the cleanup's pass before the end): the kind of bound E:175–178 declines to encode, quoting r2:41. Consider naming the cleanup without its threshold, or putting the sentence to the seat with the run list. This report states neither the threshold nor any bound.
O2. HEAD moved during the check: 05ac941 (n's G-READ-n starred readings; RESULTS.md and three results/raw files, none of E:188–189's paths) now sits on 0081351. At commit time E:187's HEAD and count need re-deriving (41bfab4..05ac941 holds 105), and the entry goes above 05ac941's new entry at the Log's head.
O3. E changed during the check. My first read had 236 lines, with the @@RUNLIST@@ placeholder at its line 169, no E:159–160, a compaction sentence after the call list, and three departures. Every item above grades the 263-line version (sha256 bed2aa80…4b37), unchanged at my end. R did not change.
O4. RES anchors are at 0081351. At 05ac941 they sit 239 lines lower (the campaign wiring's entry is at RES:15441, the Q-F0 entry at RES:23292).
O5. Neither E nor this report counts the contrast arms' free-round exclusions, and none of my commands counted, listed or derived them.

My own departures (each read-only and model-free; nothing under data/*/ckpt was read; no file was written)
- Shell tools outside the brief's list: cut once (trimming a grep over R; it printed R:1's opening and two sham session lines); tail -c 1 with od -c once (the last byte of three scratch files; it printed three newlines); tee once, into /dev/null; printf and echo; ls by name only (item 1's form).
- In my first schedule-hash pipeline, a zsh redirect (> /dev/stdout before a pipe) doubled the body; it printed one wrong digest, which I discarded and rebuilt without the redirect (item 72).
- git status --porcelain with pathspecs (names only), beside the bare form; git rev-list --count and git merge-base --is-ancestor (counts and ids only); git show of RESULTS.md diffs and of two non-checkpoint blobs piped to shasum.
- Four git greps over RESULTS.md and results/raw at 0081351 without item 3's exclusion pathspec; their pathspecs named nothing under data/, and they printed lines or file names from those files only.
- One equality test of R:46's stamp against REP's provenance stamp (one record, two copies), printed only as "stamp equal": no stamp printed, nothing computed from it.
- jq printed REP's end-look bar P values as exact rationals (read domain; more than the draft needed), and one structure check printed the opening fields of R:46's provenance record (backend fields, no stamp).
----------------------------------------------------------------------------------------------------
## Pass 1: Code's dispositions

Every FAIL and IMPRECISE item is applied, in the checker's terms, in v3, the draft the second pass checked. The draft
changed while this pass ran (O3). The coordinating session's points on the run list arrived, and three parts of the
entry were revised: its run-list section, its two plainly declared departures, and the wording of its attestation. So
the second pass checks v3 whole.

- **FAIL 41:** "(below, item 2)" now reads "(below, item 3)".
- **IMPRECISE 35:** "These are from the report's end look (`end_look`); looks 1–14's values are in its `looks`."
- **IMPRECISE 50:** "The identifier from the fields now, with `n_layers` as G-F3 recorded it (the header's line 37),
  is …".
- **IMPRECISE 65:**
  - the slip now reads "loaded no model and carried no marker word in its argv";
  - each departure is disclosed "where it is cited: in an entry, or in the pod session's close line";
  - the section no longer says the three were logged for Q-F3's run list. On the coordinating session's direction,
    it now lists by kind what committed entries declare.
- **IMPRECISE 68:** "Under `valence_core/`, only `valence_core/n` changed."
- **IMPRECISE 82:** "Then the (d) block's eight lines: a header line and (d)'s seven output lines."
- **IMPRECISE 93:** "Its output is the raw's last seven lines, under a one-line header."
- **IMPRECISE 99:** "v1.0 §13 item 4, quoting the seat's answers of 2026-11-14, §A.7."
- **NOT CHECKABLE:**
  - 55, 56, 58–60, 87, 89, 90, 94, 97, 104 and 108 stand as Code's attestation or the coordinating session's words;
  - 11 is the coordinating session's form;
  - 48 is the commit, 84 a placeholder and 100 the future;
  - 61, 63 and 96 are the coordinating session's scope and reading, which the entry cites as such;
  - 80 is the copy in the notes folder;
  - 86 is the cleanup's rule (O1).
- **O1:** applied. The entry no longer states the cleanup's rule: "Its rule is left out of this record (the
  values-check's O1)."
- **O2:** the tree bullet's range is fixed: "104 commits landed between `41bfab4` and `0081351`, the HEAD when (d)
  ran". At the commit, the entry goes at the Log's head, above every newer entry.
- **O3:** the second pass checks v3 whole.
- **O4 and O5:** noted.
- **The checker's own departures,** as its report states them, for the seat to class:
  - `git grep`s over RESULTS.md and `results/raw` at `0081351`, with a positive pathspec and without item 3's
    exclusion form;
  - one equality test of the raw's PROVENANCE stamp against the report's, printed only as equal;
  - `jq` printing the end look's P values as exact rationals (the read domain);
  - shell tools beyond the brief's list;
  - `git status` with pathspecs.

----------------------------------------------------------------------------------------------------
Pass 2: the brief (verbatim; local paths scrubbed)
----------------------------------------------------------------------------------------------------
You are a blind values-checker for a research project's records, in the git repository at <repo>. Other sessions share this working tree and may commit while you work; do not modify it.

You are read-only:
- no git writes of any kind (no add, commit, stash, checkout, reset, worktree or switch; `git hash-object` only without `-w`);
- no file written or edited anywhere;
- no model run, and no run of any repository script (`scripts/*`, `valence_core/*`) in any form;
- no Python at all, not even `python3 --version` or `python3 -c`: shell utilities only (jq, awk, sed, /usr/bin/grep, shasum, diff, cmp, wc -l, sort, uniq, git). A Python start on this laptop needs a window you do not have.

Return your report as text in your final message, between a line `=== BEGIN REPORT ===` and a line `=== END REPORT ===`, and give its sha256 (over the text between the markers, as UTF-8, ending in one newline), computed in the shell, for example by a quoted here-document piped to `shasum -a 256`. Write it to no file.

## The list of record v2, items 1–5 (verbatim; they bind you)

1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.

Also binding:
- **For any file under `data/*/ckpt`, digest forms only** (the seat's ruling of 2026-11-15): `shasum -a 256`, or `git hash-object -- <path>` compared with `git rev-parse <rev>:<path>`. Never open, read, search or `git show` such a file, and never print its size or time. This check needs one: `data/mf3/ckpt/Q-F3_campaign.json` (untracked), by `shasum -a 256` only.
- **The reports are the read domain** (item 2). You may read the content of `data/mf3/reports/Q-F3_campaign_report.json` (untracked) and `data/mf3/reports/Q-F3_qual_report.json` with `jq`, to check the draft's figures. Print from them only what you need to confirm or refute a claim in the draft. Never print the `sham_generation_ms` values, a `provenance` stamp, or any size or time of a file.
- **The blinding of the contrast arms' free rounds (m:271, m:263, m:318).** The contrast arms are A1, A2 and A3. Their session lines in the raw that end in `excluded:excluded@free` are free-round exclusions whose count is withheld until VERDICTS. Do not count, tally, list or derive them in any form: not per arm, not in total, not as "valid" against "excluded", not by subtraction from launches. For a contrast arm, work only with its launches, its lines ending in `@forced`, its pre-pick exclusions and its domain (the report's `arms`). The sham arms (A1s, A2s, A3s) carry no contrast information: you may split them fully, every label included. The draft states the same rule; it binds your commands and your report.
- `jlens-qwen36/` is a separate repository: run no git command inside it.
- No clock time, time stamp or span in your report, and nothing computed from two stamps.

In practice, for this task:
- Every content search over the checkout or a tree carries item 3's tested form. `grep -r` and `rg` prune the `ckpt` and `reports` directories under `data/`.
- Use no `--stat`, `--numstat` or `--shortstat` form anywhere.
- Do not open anything under `<tmp>/../tasks/`, any session transcript (`*.jsonl`), or any memory folder.
- The Bash tool's `grep` is ugrep: use `/usr/bin/grep`.

If you break any of this by accident, say so at the end of your report: give the command's kind and what printed, without reproducing anything that printed.

Also for this check: do not state the scratchpad cleanup's rule (its age threshold or how it decides), nor any bound on the run's length or on when it ended, anywhere in your report. Compute nothing from two stamps.

## What to check

Code (another session) has drafted the record of a finished campaign, the Q-F3 campaign. Nothing is committed yet. An earlier draft of the entry had a first blind pass; you are not given its report. Check this text whole: every factual claim against its sources, every quote, figure, hash, path, commit id, line count, date and attribution.

C = <tmp>/a6/record . The drafts:
1. `C/entry_draft_v3.md` (frozen for this check; sha256 a3e185d8fd4c7ff7bd2bab9f8cf427d4c2d84a05a615fc904a9e6ca99478e13b): the RESULTS.md entry, to go at the head of RESULTS.md's "## Log — Phase 2". `@@VCTALLY@@` is a placeholder for this check's tallies: grade it NOT CHECKABLE.
2. `C/2026-11-15_mf3-campaign-qf3.txt`: the raw, to be committed as `results/raw/2026-11-15_mf3-campaign-qf3.txt`.

The sources:
- **The wrapper's raw as the run left it:** `<tmp>/a6/launch/campaign_raw_1.txt`. The draft claims its sha256 and line count, and that the committed raw is this file with four local roots scrubbed (`C/raw_scrubbed.txt` is the scrubbed text alone), then the (d) block (`C/d_block.txt`). Check that exactly: which lines changed, and how.
- **(d)'s output:** `<tmp>/a6/launch/d_1.txt`.
- **The report:** `data/mf3/reports/Q-F3_campaign_report.json` (read domain, above); G-F3's, `data/mf3/reports/Q-F3_qual_report.json`, for the identity comparison.
- **The checkpoint:** `data/mf3/ckpt/Q-F3_campaign.json` (digest only).
- **LOCK-m-F3.md:** v1.0 §1, §2, §4, §5, §6, §12, §13; v0.2 §8; lock §8's bar table, rows 9–13; lock §9's row F35.
- **The seat's raw** `results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md`: §0, §2.2, §2.3, §2.4, §9. **The seat's answers of 2026-11-14,** `results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md`, §A.7. **The seat's read of G-TIME-F3's re-run,** `results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md`, §4.
- **The PI's routing,** section A item 3, verbatim as the committed values-check raw `results/raw/2026-11-15_qf3-close-lines-campaign-go_valuescheck.md` quotes it (its lines 65–68). That is the only record of it in the repository.
- **RESULTS.md** at the HEAD you find (another session may commit while you work): the campaign wiring's entry (it begins "- 2026-11-15 — **The campaign wiring: `campaign`") with its close; the Q-F0 campaign's entry (it begins "- 2026-10-19 — **THE Q-F0 CAMPAIGN"), whose form the draft follows; and, for the run-list section, the entries and close lines of the commits it cites (`8a7cdf8`, `5c0ae6b`, `9464f61`, `f3e7190`, `fa96ccf` and its close, `101026c`, `ad856f0`, `1272702`, `732a58f`, `b523f6a`). For each, check that the text that commit added declares what the draft says of it, by kind; `git blame` and `git show --format= <commit> -- RESULTS.md` are fit tools.
- **The code,** read-only: `scripts/mf3_sessions.py` (the PIN at line 227 and the constants below it), and `valence_core/mf3/stages.py` (`_schedules_sha` at line 579, and the schedule loader just above it).
- **git:** the commits named, ancestry, and `git diff --name-only 41bfab4 0081351` over the paths the draft names.
- **Not in the repository (grade NOT CHECKABLE unless a repository record bears on it):** the coordinating session's messages and words ("launch cleared", "windows closed", the +30 min form, its own process check, its reading on the run list, its word that it relayed none of the withheld counts), and Code's attestation of its own calls during the run, made from its session transcript, which you may not open.

Pay special attention to:
- every number in the entry's tables and lists, against the raw's lines and the report: launches, `s=` ranges, pre-pick exclusions, domains, BAR figures and critical values, the smallest P per bar and the look it falls at, read flags, `beside` counts, and the sham arms' label splits;
- that the draft counts none of the contrast arms' free-round exclusions anywhere, and that nothing you write does;
- the identity: the report's identity keys against G-F3's report identity, the lock's sha256, the schedule hash (rebuild it in the shell from the six campaign schedule files by `_schedules_sha`'s definition), and `schedule_n`;
- the scrub: that the committed raw differs from the wrapper's raw only on the lines the draft names, only by the scrubbed roots, plus the appended block, and the hashes and line counts the draft gives for each stage;
- the run-list section: each cited commit, what it declares, and the kinds and counts the draft gives;
- that every quote is verbatim, and that the draft states nothing as a rule or a precedent that no record states;
- that the draft places no event of its own against the campaign's end, beyond the end procedure itself (the end-wait, the process checks, (d));
- no clock time, time stamp or `$` figure in the entry (file:line anchors such as `m:267` are not clock times). The raw's PROVENANCE line carries the report's start stamp, which the draft names as one of Q4's records: do not print it;
- line widths: no entry line over 120 characters, except table rows and the verbatim block quote.

Grade each claim CONFIRMED, IMPRECISE (true in substance, but the wording or anchoring is off; say the fix), FAIL (wrong; say what is right) or NOT CHECKABLE (say why). Number your items and give file:line evidence. End with a tally and the list of everything not CONFIRMED. State HEAD (`git log --format='%h' -1`) at your start and at your end.
----------------------------------------------------------------------------------------------------
Pass 2: the checker's report (verbatim)
----------------------------------------------------------------------------------------------------
Blind values-check of the Q-F3 campaign's record: C/entry_draft_v3.md (the entry) and C/2026-11-15_mf3-campaign-qf3.txt (the raw), by a fresh checker with shell tools only.

HEAD at start: 05ac941. HEAD at end: 05ac941.
The brief's sha256 checked (55353e80…7dfd) and the brief read whole. The entry draft's sha256 checked (a3e185d8…e13b).

Conventions. E:n is the entry draft's line n; R:n is the raw's line n; W is the wrapper's raw (<tmp>/a6/launch/campaign_raw_1.txt); d_1 is (d)'s output (<tmp>/a6/launch/d_1.txt); C is the brief's record folder. The contrast arms (A1, A2, A3) were worked only by their launches, their `@forced` lines, their pre-pick exclusions and the report's `arms`: no free-round exclusion of a contrast arm was counted, listed or derived, and none is in this report. The sham arms were split fully. The campaign checkpoint was hashed with `shasum -a 256` only.

Headline (E:1–5)
1. E:1–2, the anchors (m:298, m:361; LOCK-m-F3 v1.0; the PI's routing of 2026-11-15, evening, section A item 3). CONFIRMED: PROPOSAL-m-gating-campaign-v1_11.md:298 and :361 (step 19 names the campaign); results/raw/2026-11-15_qf3-close-lines-campaign-go_valuescheck.md:56 (the routing's header: PI date 2026-11-15, evening; "Route as given") and :65–68 (item 3).
2. E:2 and E:21, COMPLETE, exit 0, one invocation. CONFIRMED: R:778 (STAGE … COMPLETE), R:781 (EXIT=0), a single INVOCATION line (R:40); the report's `status` COMPLETE and `terminal` {at_launches 596, COMPLETE}.
3. E:2–3, 596 launches: A1 95, A1s 40, A2 162, A2s 70, A3 165, A3s 64. CONFIRMED: 596 session lines, each of the form `campaign <arm> s=<n> <status>`; the per-arm counts as stated; the report's `arms.*.launched` equal.
4. E:3, each domain at its floor (80, 32, 144, 56, 144, 56). CONFIRMED: the report's `arms.*.domain` and `floors`.
5. E:3–4, fifteen looks, 135 BAR lines, all silent. CONFIRMED: nine BAR lines at each of looks 1–14 and `end`, 135 in all, each `silent`; the report's `looks_count` 15.
6. E:4, no pause and no STOP. CONFIRMED: the report's `pauses` [] and `stop` null; no STOP or PAUSE line in the raw.
7. E:4–5, (a′) and (d) both EQUAL at a734dadec8f8ce9b. CONFIRMED: R:37, R:39, R:787–789.
8. E:5 and E:277–278, the VERDICTS session "waits for `POSTING v1` (10′)" (v1.0 §13 item 4, quoting §A.7). CONFIRMED: LOCK-m-F3.md:317; the phrase byte-equal at results/raw/2026-11-14_gf3-and-lock-p-v1_design-to-code_answers.md:50, §A.7 (that file's sha256 6b963adf…db3a, as LOCK-m-F3.md:3 cites it).

The words (E:6–20)
9. E:7–8, "Route as given" (PI date 2026-11-15, evening) on the seat's answers of that date, 1f3ce1f9…f84b, committed at a215c28. CONFIRMED: that raw's sha256 is 1f3ce1f9…f84b and a215c28 is its only commit; its header (its line 3) reads "PI date 2026-11-15 (evening)"; the close at RESULTS.md:15824–15829 says the same.
10. E:10, section A item 3, verbatim. CONFIRMED: byte-equal to the values-check raw's lines 65–68 joined at their line breaks. See O1.
11. E:12–14, the seat's §2.3 and its two conditions. CONFIRMED: results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md:31–34.
12. E:16, after the push (origin fa27c45), with automatic macOS updates off. CONFIRMED: the push moved origin/main to fa27c45 (RESULTS.md:15123–15126, e5aba51), and fa27c45 is 41bfab4's parent; the coordinating session's condition "the launch waits for the push (item 12)" (RESULTS.md:15562, a215c28); the PI's "Auto updates are off" with the four automatic-update keys read back at 0 (RESULTS.md:15550–15553, a215c28).
13. E:16–17, the word "launch cleared" and the announcement of the launch. NOT CHECKABLE: not in the repository.
14. E:17–18, "the coordinating session closed the commit windows ("windows closed") before it". IMPRECISE: the windows the record closes before each launch are the battery windows. a215c28's entry: "This session gives each battery a window, its own form (§9's windows are for commits)" (RESULTS.md:15555) and "every window closes before each launch or resume" (RESULTS.md:15560); RESULTS.md:15165–15166 (e5aba51) extends that form to p's VERDICTS runs. No record has the commit windows closed before the launch. Fix: "the battery windows" (or "the windows"); if the word itself named commit windows, say both and cite a215c28's form for the battery windows.
15. E:19, the PID-only liveness check during the run and its report. CONFIRMED as the form of record: a215c28's entry has the windows reopen on the F3 session's report of the PID alive, "read by the PID alone (list v2 item 5)" (RESULTS.md:15560–15561). The quoted words are the coordinating session's and are not in the repository.
16. E:20, "(d) first, then the outcome to the coordinating session before anything else". NOT CHECKABLE: no committed text sets this order (not a215c28's entry, v1.0 §13 item 3 or the seat's §2.2). See O3.

The run (E:21–53)
17. E:21–23, the driver 7bb6f7ca…28a4 (3f017d8) at HEAD 41bfab4, under LOCK-m-F3 v1.0 (fe9518c7…1aa6, a89a4fa), uncached, at cap 120. CONFIRMED: R:2, R:41, R:45, R:778; 3f017d8's blob hashes to 7bb6f7ca…28a4 and 41bfab4's blob is the same; a89a4fa is the last commit on LOCK-m-F3.md.
18. E:24–26, the snapshot of record c000ac2c…3282 on refs/main, offline, the cache's only snapshot; its SNAPSHOT line before the load and the re-read unchanged. CONFIRMED: R:42 ("1 snapshot(s)", HF_HUB_OFFLINE=1), R:43.
19. E:27–28, the lines before the sessions, in order; the PROVENANCE start stamp one of Q4's records. CONFIRMED: R:40–46. The stamp on R:46 equals the report's `provenance[0].stamp`, and the record parts are equal (compared silently; nothing printed).
20. E:29, "interleaved by §2.1's rule". CONFIRMED: R:1; scripts/mf3_sessions.py:231; RESULTS.md:15700.
21. E:31–38, the launch table. CONFIRMED: per arm the `s=` indices run 0–94, 0–39, 0–161, 0–69, 0–164 and 0–63, each once, none missing.
22. E:40–41, the projection, 832 in all over 21 looks (v1.0 §1; m:192). CONFIRMED: LOCK-m-F3.md:55–56 and :67; m:192; the report's `launch_counts_projection`; scripts/mf3_sessions.py:250.
23. E:42–43, the domains at the floors (v1.0 §1; mf3's `schedule.FLOORS` under the path), each the launches less the pre-pick exclusions. CONFIRMED: LOCK-m-F3.md:57; valence_core/mf3/schedule.py:44 (A1's uncached floor 80); 95−15, 40−8, 162−18, 70−14, 165−21 and 64−8 give the six domains.
24. E:45–49, the end: terminal COMPLETE at 596; the cap not reached; the STAGE, CHECKPOINT, REPORT and EXIT=0 lines, EXIT=0 the only EXIT line; `pauses` empty and `stop` null. CONFIRMED: the report's `terminal`, its `hour_cap_reached` false and its `hour_cap` equal to v1.0 §2's line; R:778–781; "EXIT" occurs on R:781 alone.
25. E:50, no RULING line and no adjudication excerpt. CONFIRMED: no RULING line in the raw; a names-only listing of data/mf3/ckpt shows no excerpt beside the checkpoint.
26. E:51–52, no problem line outside the header. CONFIRMED: over the 742 non-header lines, none of STOP, PAUSE, REFUSED, RULING, NOT APPLIED, LAPTOP PREFLIGHT REFUSES, traceback (either case) or CHECKPOINT STATE INCONSISTENT; the 47 header lines carry none either.
27. E:53, 742 non-header lines: 11 identity and end lines (R:40–46, R:778–781), 596 session lines, 135 BAR lines. CONFIRMED.

Looks and monitors (E:54–107)
28. E:55, looks every 40 launches (m:330), 14 at 40–560, and the end at 596. CONFIRMED: the report's `looks[].at_launches` 40, 80, … 560 (14 entries) and `end_look.at_launches` 596; m:330.
29. E:56, nine BAR lines a look: three sham bars and two guard bars per contrast arm. CONFIRMED: R:87–95 and each later look.
30. E:57–58, a fire pauses the unit for the seat, never a verdict; cumulative counts, α .05 per look, no α spending. CONFIRMED: LOCK-m-F3.md:1205–1209 (lock §8 rows 9–13).
31. E:59–62, the sham bars at the end: 35/1530, P 1.0000, p0 .05, critical 92; 25/853, P 1.0000, p0 .10, critical 101; 6/1188, P 1.0000, p0 .02, critical 33; their domains as stated. CONFIRMED: R:769–771; the report's `end_look.results`; LOCK-m-F3.md:1205–1207; the sham `beside` rounds sum to 1530 (342+601+587), and A2s's and A3s's to 1188.
32. E:64–65, the sham counts unchanged from look 10 on; A2s the last sham arm to reach its floor, its last launch before look 10. CONFIRMED: R:528–530 equal R:769–771 and differ from R:479–481; A2s's last session line is R:510, launch 383, between look 9 (at 360) and look 10 (at 400); A3s's last is launch 360, A1s's launch 236.
33. E:66–67, the guard (m:316): one-sided Fisher against the sham arm and alone against p0 .20, at α .05. CONFIRMED: m:316; LOCK-m-F3.md:1208–1209; the BAR lines.
34. E:69–73, the guard table at the end. CONFIRMED: R:772–777, every cell.
35. E:75–87, the smallest P per bar and its look. CONFIRMED: an awk pass over all 135 BAR lines gives the same nine minima at the same looks, in the table's ascending order, with no tie at any minimum.
36. E:90–91, no hair trigger and no G-VER mismatch; any would have stopped the campaign (m:271, m:284). CONFIRMED: the report's `stop` null and terminal COMPLETE, and no STOP line; m:271 ("a hair-trigger fire anywhere stops the stage"); m:284 (a mismatch is a STOP); LOCK-m-F3.md:1197–1199. The report has no hair-trigger row; the statement rests on `stop` and the terminal state, as the Q-F0 entry's did.
37. E:92–94, the pooled pre-pick exclusions. CONFIRMED: the report's `arms.*.prepick_excluded` 15, 18, 21, 8, 14 and 8; the end look's guard lines.
38. E:96, every pre-pick exclusion at a forced round; no session line names a reasoning line. CONFIRMED: in each arm the count of `@forced` lines equals `prepick_excluded`; no session line holds "reason" or "line" (F35's reasoning-line form, `scaffold@reasoning`, is never printed).
39. E:97–98, the end look's values from `end_look`, looks 1–14's in `looks`. CONFIRMED: `looks` has 14 entries; `end_look` stands apart.
40. E:97, "Reported, not bars (m:330)". CONFIRMED: m:330 ("reported: low label mass, top-1-not-a-label, pooled pre-pick exclusions"; round degeneracy "reported on its contrast arms").
41. E:99–103, the read flags. CONFIRMED: `end_look.arms.*.read_flags`, scope "first reads of domain sessions" (reads 80, 144, 144) for the contrast arms and "all reads" for the sham arms; every figure as stated.
42. E:104–107, degeneracy and lexical (`beside`). CONFIRMED: scopes "forced rounds only" and "all task rounds"; every figure as stated.

m:271's redactions (E:108–132)
43. E:109–110, the contrast sessions' free-round events withheld to the VERDICTS entry. CONFIRMED: m:271 ("withheld to the unit's VERDICTS entry or NOT-RUN record"); m:263; m:318.
44. E:111–112, the free-round exclusion printed without its class, as `excluded:excluded@free` (lock §9, F35; ruling (h)). CONFIRMED: LOCK-m-F3.md:1276 (F35: the printed reason `excluded@free`, "ruling (h): no class"); valence_core/mf3/readrule.py:348 builds the status as `excluded:` plus the printed reason, and :64 admits no other free-round form on a contrast arm. Not counted.
45. E:113–114, this entry counts none of them; the domains pooled. CONFIRMED: no figure in the entry splits a contrast domain or counts a contrast free round, and none follows from its launches, pre-pick exclusions, domains, read flags (first reads, n = the domain) or `beside` (forced rounds only).
46. E:115–116, no reads file and no first-pick share, sham included; the reads are the VERDICTS entry's (m:318). CONFIRMED: a names-only listing of data/mf3/reports holds no campaign reads file; no key path in the report names a pick or a share but `prepick_excluded`; RESULTS.md:15727 ("No reads file").
47. E:119–123, the sham table. CONFIRMED: A1s 31 valid, `audit@forced` 3, `content@forced` 4, `lexical@forced` 1, `lexical@free` 1; A2s 53, 7, 6, 1 and 3; A3s 55, 4, 3, 1 and 1; each row sums to the arm's launches.
48. E:125, the checkpoint holds the picks and is hashed, not opened. CONFIRMED: m:318 ("picks go to checkpoint files"); its sha256 is E:240's.
49. E:126–129, timing. CONFIRMED: no seconds or duration in the entry; `sham_generation_ms` is in the report and is not quoted; LOCK-m-F3.md:235 ("The contrast sessions' seconds stay in the checkpoint (m:318)").
50. E:130–131, the records not computed against (Q4; r2:§4; v0.2 §8). CONFIRMED: results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md:41; LOCK-m-F3.md:570–572; the list in the Q-F0 entry's form (RESULTS.md:23667–23669).
51. E:132, no launch stamp and no finish stamp in the raw. CONFIRMED: R:46's is the raw's only stamp; R:1 says "No stamp."
52. E:132, "The commit message restates no stamp." NOT CHECKABLE: the commit is not made.

The launch (E:133–198)
53. E:134–138, (a′) EQUAL: every field derivable without the load equal to G-F3's record, `n_layers` named not derived, the identifier on the header's line 37 equal to G-F3's report identity and to v1.0 §5's line. CONFIRMED: R:7–39 (R:31–32, R:37, R:39); LOCK-m-F3.md:153; G-F3's report `identity.backend_identifier` a734dadec8f8ce9b.
54. E:139–140, inside the wrapper, model-free (the model libraries' imports blocked), on `a_prime.py` 66e7d72d…f617, its output in the header. CONFIRMED: R:6 (the full sha256), R:8, R:7–39.
55. E:141–142, the dry pre-launch check: CLEAR just before the launch, its coverage, nothing loaded. CONFIRMED: R:1.
56. E:143–149, the checklist (m:267). IMPRECISE: m:267's checklist is power ≥ 96 W on AC; one process, no other model process (preflight check); the nohup line; display sleep only; disk headroom checked; the gate line logged (PROPOSAL-m-gating-campaign-v1_11.md:267). `HF_HUB_OFFLINE=1` is not one of its items: it is the licence's (g) (LOCK-m-F3.md:157–158), shown on R:4 beside power and disk. Fix: take it out of the m:267 list, for example "beside it, `HF_HUB_OFFLINE=1` (the licence's (g))". The other five items match R:1, R:4, R:5 and R:44, and "no departure" is R:1's.
57. E:150–151, the command as m:267's line as written. CONFIRMED: E:150–151 joined equals R:1's command; m:267's form.
58. E:151–152, `echo "PID=$!"` on the next line, both lines in `launch_campaign.sh`, run by the Bash tool with /bin/zsh. NOT CHECKABLE: the launcher is not in the repository.
59. E:153, `PID=7989`, and `ps -p` naming the wrapper. NOT CHECKABLE: no tracked record names PID 7989. See O2.
60. E:154, the wrapper wrote the raw, ran (a′), and ran the campaign only on (a′)'s exit 0. CONFIRMED in substance: R:1 ("the command is this wrapper, which writes this raw"; "nothing launches unless it is EQUAL"). The exit-code form of that gate is the wrapper's, which is gone.
61. E:155, the start check. NOT CHECKABLE.
62. E:156 and E:169, the liveness check's result and the message. NOT CHECKABLE (the form is item 15's).
63. E:157–159 and E:273–274, the end-wait, its output file found empty, and the `ps` and `pgrep` checks. NOT CHECKABLE; R:782 ("Before it ran, the PID and the campaign's processes were gone (ps, pgrep)") is consistent.
64. E:160–161, the coordinating session's own check. NOT CHECKABLE.
65. E:162–172, the calls between the launch and the end-wait's notification, and no Python, `git status`, listing, stat or read. NOT CHECKABLE: Code's attestation from its transcript. Its form follows the Q-F0 entry's (RESULTS.md:23599–23606, :23731–23735). See item 116.
66. E:174–176, the run list's scope as the coordinating session set it. IMPRECISE: a repository record bears on it. RESULTS.md:10145 (732a58f) and RESULTS.md:10668 (1272702) record the coordinating session logging non-Python commands with a guard marker in their argv "for Q-F3's run list", and E:192–198 treats such processes as run-list matter ("waits for the run list, which enumerates every one"); the scope sentence names only processes started with python or the venv's interpreter. Fix: give the scope as set and say where the non-Python guard-marker class stands (in the list or beside it), so that E:174–176, E:192–198 and the record agree.
67. E:177–179, the seat's §4: "no session computes a stage total or a bound from any pair of stamps before VERDICTS". CONFIRMED: verbatim at results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md:41.
68. E:179–180, the coordinating session's reading. NOT CHECKABLE; it is labelled a reading, not a ruling, and is not stated as a rule.
69. E:177 and E:181–182, the list not built here, built after VERDICTS or as the seat rules, and no stamp compared with the end. NOT CHECKABLE: Code's attestation.
70. E:183–184, each declared item model-free and disclosed where it is cited. CONFIRMED: RESULTS.md:13276–13279, :14555–14557, :14645–14651, :11124–11127, :12127–12133, :5661–5662 with :5685 ("None of the 58 processes, nor the 30, was Python"), :11263–11267, :10665–10668, :10143–10146 and :11823–11826, each blamed to the commit the draft cites.
71. E:186, 8a7cdf8: one Python start outside a window, its command line holding a marker word. CONFIRMED: RESULTS.md:13276–13279: one run of the shell's `python3`, disclosed "before any window was asked"; its command line held its unit's name, which carries m's guard marker, "so it counted under the window rule".
72. E:187, 5c0ae6b: two, with no marker. CONFIRMED: RESULTS.md:14555–14557 ("Two starts of the system interpreter outside any window"; "neither command line named a model marker").
73. E:188, 9464f61: two, with marker words. CONFIRMED: RESULTS.md:14645–14649: two `python3 -c` "without a battery window", their command lines naming the two units, which m's guard would have counted.
74. E:189, f3e7190: one `/usr/bin/python3 --version`, no marker, in the pod session's close line. CONFIRMED: RESULTS.md:11124–11127 (f3e7190, whose subject names the pod session's close line on 6df2131's entry).
75. E:190–191, fa96ccf: three Python starts with a guard marker in their argv, run outside `nice -n 19`. CONFIRMED: RESULTS.md:12127–12133 (four marker commands: an `ls`, the venv interpreter's `-c 1` and two `python3 -c`; "The last three ran outside `nice -n 19`").
76. E:191, "whose close records the seat's "the four argv departures are inert"". IMPRECISE: the quoted words are the close's, RESULTS.md:12153 (n-build's close on fa96ccf's entry, added at b4522ae). The seat's raw (results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md, sha256 5843a9bd…7165) says "the four departures are inert" (its line 10) and heads its §4 "Departures (`fa96ccf` §4): inert, no strike" (its line 55). Fix: quote the seat's "the four departures are inert", or give the quoted words as the close's.
77. E:192–196, non-Python processes with a guard marker in their argv: the kinds and the cited examples. CONFIRMED: 101026c, 58 (RESULTS.md:5661–5662 and :5685; 40 `git`, 1 `grep` and 17 `git`); ad856f0 (RESULTS.md:11263–11267: two `grep`, a `git diff` and a `sed`); 1272702 (RESULTS.md:10665–10668: a `git show` in a loop); 732a58f (RESULTS.md:10143–10146: an `ls`); b523f6a (RESULTS.md:11823–11826: the values-checker's 36 `git` calls). The `shasum` kind is of record at 83a50a0, in the range (RESULTS.md:12439: "Five `shasum` processes … two of them carrying m's guard markers"). "Among them" marks the list partial.
78. E:197–198, what the notes log waits for the run list. NOT CHECKABLE.
79. E:199–200, 104 commits between 41bfab4 and 0081351, the HEAD when (d) ran, none of them this session's. CONFIRMED: `git rev-list --count 41bfab4..0081351` is 104, with no merge; R:784; no subject in the range is an F3-session commit (they are n's, p's, the pod session's, the seat's and the coordinating session's).
80. E:201–202, none touched the eleven named paths. CONFIRMED: `git log` over the range on them lists none; `git diff --name-only 41bfab4 0081351` on them is empty; 0081351..HEAD touches none either.
81. E:203, under valence_core/ only valence_core/n changed. CONFIRMED: 16 paths, all under valence_core/n; no commit in the range touches valence_core/ outside it.
82. E:204, no tracked change on those paths; the driver re-hashes to 7bb6f7ca…28a4. CONFIRMED: `git status --porcelain` on them shows none (data/mf3 holds only the two untracked outputs); `shasum` gives 7bb6f7ca…28a4 and `git hash-object` equals HEAD's blob.

The driver (E:205–207)
83. CONFIRMED: R:41; RESULTS.md:15682 and :15696–15698 (3f017d8: the blob from 285eed04…0e44 to 7bb6f7ca…28a4, and v1.0 §6's value "is the driver at the lock"); LOCK-m-F3.md:164.

The identity (E:208–226)
84. E:209–210, `lock_sha256` fe9518c7…1aa6, the sha256 of LOCK-m-F3.md, committed-clean at HEAD. CONFIRMED: `shasum` equal; `git hash-object` equals `git rev-parse HEAD:LOCK-m-F3.md`.
85. E:211–213, `schedule_sha256` 8e2b1193…ffba, rebuilt in shell by `_schedules_sha` from the six campaign files v1.0 §4 names, each committed-clean; equal. CONFIRMED: this check rebuilt it by valence_core/mf3/stages.py:579–581's definition (the name-sorted lines "<name> <sha256>", each ending in a newline, the names as valence_core/mf3/schedule.py:245–251 forms them) and got 8e2b1193…ffba; each file's sha256 equals LOCK-m-F3.md:122–127 and the manifest's entry, and each file is committed-clean.
86. E:214, `path` uncached and `reasoning_cap` 120. CONFIRMED.
87. E:215–217, `backend_identifier` a734dadec8f8ce9b, (d) EQUAL; its lines appended after the end "in the campaign's raw" (the seat's §2.2); in shell. CONFIRMED: the report's identity; R:782–789; the seat's raw, its line 28 (the quoted words verbatim); R:782–783 give the shell form.
88. E:218–219, every other key equal to G-F3's report identity, the nine named. CONFIRMED: a jq diff of the two identities differs in `lock_sha256` and `schedule_sha256` only (`path`, `reasoning_cap` and `backend_identifier` are equal too).
89. E:220–223, `unit`, `stage`, `hour_cap`, `form` and `schedule_n` (v1.0 §4's n). CONFIRMED: the report's top level, `form` byte-equal to E:222's quote and `hour_cap` equal to E:221's value; `schedule_n` equals each schedule file's `n` and LOCK-m-F3.md:122–127.
90. E:225–226, the LICENCE line at stage start; no commit on LOCK-m-F3.md since a89a4fa. CONFIRMED: R:45; `git log`.
91. E:225, "The checkpoint's identity was not opened." NOT CHECKABLE: a statement of practice.

The outputs (E:227–243)
92. E:228–229, the raw: c402e79d…cbb7, 789 lines. CONFIRMED.
93. E:230–231, before the scrub: 781 lines, 75ed4cf5…795b. CONFIRMED (W).
94. E:231–232, "A copy is in the sessions' shared notes folder." NOT CHECKABLE: not a source of this check.
95. E:233–235, after the scrub: 781 lines, 25e9954c…6349; four local roots in G-F3's raw's forms, `<repo>/` on lines 40, 779 and 780 and `<home>/` on line 42. CONFIRMED: W and C/raw_scrubbed.txt differ on exactly those four lines; the two substitutions (the repository root to `<repo>/`, then the home folder to `<home>/`) applied to W reproduce C/raw_scrubbed.txt byte for byte; W holds the home-folder prefix four times, once on each of those lines; the `<tmp>` forms on R:1 and R:6 are W's own; the committed raw holds no home-folder prefix, no user name and no /private path; G-F3's raw uses the same forms (results/raw/2026-11-12_mf3-gf3.txt:6, :8, :57, :58).
96. E:236, "Then the (d) block's eight lines: a header line and (d)'s seven output lines." IMPRECISE: the committed raw is exactly C/raw_scrubbed.txt followed by C/d_block.txt (cmp), and d_block's first line is R:782; but its seven output lines are d_1's seven lines each prefixed `#   ` (cmp), not the bare output. Fix: "(d)'s seven output lines, each under the raw's `#   ` prefix". The same holds for E:261 ("the raw's last seven lines") and for R:782's "Its output, verbatim:".
97. E:237–238, the report: b4b48567…98d3. CONFIRMED.
98. E:239–240, the checkpoint: 5ef02616…f92f, hashed only. CONFIRMED (`shasum -a 256` only).
99. E:241–243, the values-check raw's link and `@@VCTALLY@@`. NOT CHECKABLE: a placeholder, and the file is still to be written.

For the seat (E:244–274)
100. E:245–246, the routine cleanup as the cause, and "the values-check's O1". NOT CHECKABLE: the cause is not of record, and the first pass's report is not given to this check.
101. E:247–250, what the cleanup removed, and that only the raw stayed. CONFIRMED in what the record holds: a names-only listing of <tmp>/a6/launch shows the raw and (d)'s later output only; R:1, R:6 and R:782–783 attest that `run_campaign.sh`, `a_prime.py` and `d_check.py` existed.
102. E:247–249, `launch_campaign.sh`, `prelaunch_check_campaign.py`, the outputs named, and "Code found them missing at the end". NOT CHECKABLE.
103. E:249–250, the clause after "Only the raw stayed". IMPRECISE: it gives the raw's survival a reason, and that reason rests on how the cleanup decides, which E:245–246 says is left out of this record. Fix: end the sentence at "Only the raw stayed."
104. E:251–256, how the run stayed unaffected. CONFIRMED in what the record holds: (a′) at the launch (R:6–39); the driver and the stage's code in the repository; `EXIT=0` (R:781).
105. E:253–254, the wrapper's body as one compound command, parsed whole before it began. NOT CHECKABLE: its bytes are not in the repository.
106. E:259, `a_prime.py`'s sha256 and its launch output in the raw's header. CONFIRMED: R:6–39.
107. E:258, the kit's bytes in Code's session transcript. NOT CHECKABLE.
108. E:260–261, (d) in shell, not by `d_check.py`; its output under a one-line header. CONFIRMED: R:782–789 (the prefix as item 96).
109. E:262–268, the count made at the end, its disclosure, and the coordinating session's word. NOT CHECKABLE (this session's terminal and messages). Its "This entry carries none of them" is item 45's.
110. E:269–270, a departure in form from m:271, m:263 and m:318 and from the Q-F0 entry's practice ("This entry counts none of them"). CONFIRMED: those lines say what the draft says of them; the quote is verbatim at RESULTS.md:23653 (de6dfc5, the Q-F0 campaign's entry). See O4.
111. E:271–272, item 4 and its timing on the coordinating session's reading. NOT CHECKABLE.

What follows (E:275–279)
112. E:276, the campaign (v1.0 §13 item 3) ends here. CONFIRMED: LOCK-m-F3.md:314–316.
113. E:279, the push waits for the PI's word. CONFIRMED as the record's practice: the seat's raw of 2026-11-15, its line 78 ("when is his"); the push to fa27c45 on the PI's word (RESULTS.md:15123–15125).

Form
114. Line widths. CONFIRMED: only E:10, the verbatim block quote (364 characters), is over 120; no table row is; the widest other line, E:56, is 118.
115. No clock time, time stamp or `$` figure. CONFIRMED: the only `$` is the shell's `$!` (E:151); the PROVENANCE stamp is named (E:28, E:131) and never printed; the dates are calendar dates.
116. No event of the draft's own placed against the end beyond the end procedure. IMPRECISE: E:162–168 places this session's two edits of a memory file and two task-list updates, which are not part of the end procedure, between the launch and the end-wait's notification, that is, before the end. By the coordinating session's reading at E:179–180, a list whose membership is set against the end encodes a bound, and these calls form such a list. The Q-F0 entry carried calls of the kind (RESULTS.md:23599–23606). Fix: keep to the procedure's own calls and E:171–172's negative statement, or say for the seat why E:179–180's reading does not reach this session's attestation. Everything else the draft places at the end is the end procedure ((d), the process checks, the end-wait) or comes after it.
117. The raw's own header claims, beside the draft. CONFIRMED: R:2 (HEAD, driver, no tracked change); R:3's two input digests equal LOCK-m-F3.md:138–139 (G-F3's checkpoint committed-clean by `git hash-object` against `git rev-parse`); R:9's adapter histories (last changes 7da9509 and 1465b34 at 41bfab4, each before 2193832); R:783–788's values (LOCK-m-F3.md committed-clean, one §5 identifier line, both identifiers a734dadec8f8ce9b).
118. E:1, the entry's date 2026-11-25. CONFIRMED: a calendar date, the session's own; the values-check raw's name carries the same.

Observations (post hoc; none graded)
O1. E:10's routing text has its only repository record at results/raw/2026-11-15_qf3-close-lines-campaign-go_valuescheck.md:65–68. The entry calls it verbatim without naming that record; a pointer would let a reader check it.
O2. No tracked record names PID 7989. RESULTS.md:3947 and :4020 (2834c2d) and :5685 (101026c) name Q-F3's campaign process as PID 8051. If 7989 is the launched command's PID (the end-wait's target) and 8051 the driver's process, one clause at E:153 or E:160 would keep the record consistent.
O3. E:20 gives the form "(d) first, then the outcome to the coordinating session before anything else"; E:263–265 has Code's first per-arm extraction come first and the end notice "then". If the extraction preceded the notice, the entry should say whether it was part of making the notice or a step before it; the seat classes item 3.
O4. Item 3's end notice also bears on v1.0 §13 item 3 (LOCK-m-F3.md:316: "Its end notice carries "ended" and the exit status, with no stamp and no window") and on r2:§4's form (results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md:41); the draft classes it against m:271, m:263, m:318 and Q-F0's practice only. For the seat.
O5. A scan of every line added to RESULTS.md in 41bfab4..0081351 found no Python start outside a window beyond E:186–189's four entries: ecf349d's "its Python start" points back to f3e7190's, and 679122e's runs outside the window were shell-only.

Tally: 118 items. 89 CONFIRMED, 7 IMPRECISE, 0 FAIL, 22 NOT CHECKABLE.

Not CONFIRMED:
- IMPRECISE: 14 (the windows closed before the launch are the battery windows of record); 56 (`HF_HUB_OFFLINE=1` is not an m:267 checklist item); 66 (the run list's scope against the record's non-Python logs "for Q-F3's run list"); 76 (the quoted "argv departures" words are the close's, not the seat's); 96 ((d)'s seven output lines carry the `#   ` prefix); 103 (the clause after "Only the raw stayed"); 116 (this session's own non-procedure calls placed before the end).
- NOT CHECKABLE: 13, 16, 52, 58, 59, 61, 62, 63, 64, 65, 68, 69, 78, 91, 94, 99, 100, 102, 105, 107, 109, 111.

This check's own departures:
- A Read of the raw's first 60 lines, to check its header, displayed R:46, the PROVENANCE line with the report's start stamp, in a tool output. Nothing of it is in this report.
- A grep listing the calendar dates in the raw printed the date part of R:46's stamp in a tool output. Nothing of it is in this report.
- Noted, not departures: one `git log` carried the adapter module's path, whose file name holds two of m's guard-marker words, in a non-Python process's argv, with no stage running; one digest-form check (`git hash-object` against `git rev-parse HEAD:`) of G-F3's committed checkpoint, beside the campaign checkpoint's `shasum`, opened nothing; a names-only listing of C showed the first pass's files, and none was opened.
----------------------------------------------------------------------------------------------------
## Pass 2: Code's dispositions

Every IMPRECISE item is applied, in the checker's terms, in v4, the text committed. The edits after this pass were
checked by tool:
- each new quote against its source: `a215c28`'s entry, the seat's corpus-adoption raw, the lock's licence line, and
  the relay as the close-lines values-check quotes it;
- each new anchor by `git blame` (`a215c28`, `2834c2d`);
- the widths, the forms and the placeholders.

- **IMPRECISE 14:** "the coordinating session closed its windows before it ("windows closed"). That is the form
  `a215c28`'s entry gives for the battery windows: "every window closes before each launch or resume"."
- **IMPRECISE 56:** `HF_HUB_OFFLINE=1` leaves the m:267 list: "Beside it, on the same header line as the power and
  the disk: `HF_HUB_OFFLINE=1` (the licence's (g))."
- **IMPRECISE 66:** a sentence follows the scope. The coordinating session's log also holds non-Python commands with a
  guard marker in their argv (`732a58f` and `1272702` say so). Whether the list takes that class in, or that class
  stands beside it, is part of item 4 for the seat.
- **IMPRECISE 76:** the seat's words, with their raw: "The seat ruled that entry's four departures inert: "the four
  departures are inert" (`results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md`)."
- **IMPRECISE 96:**
  - the entry now says "(d)'s seven output lines, each under the raw's `#   ` prefix", and so does item 2 of "For the
    seat";
  - the raw's (d) header line, which ended "Its output, verbatim:", now ends "Its output, verbatim, each line under
    the prefix "#   ":";
  - the raw's sha256 moves from `c402e79d…cbb7` to `23f1b48e…1caa`, still 789 lines.
- **IMPRECISE 103:** the clause is struck: "Only the raw stayed."
- **IMPRECISE 116:** the list stays, on the coordinating session's word ("keep the list, in Q-F0's form"). The entry
  gives that session's reading for the seat: "listing these calls by kind sets no bound that the report "PID alive at
  +30 min" does not already give. The seat may read this beside item 4, below."
- **NOT CHECKABLE:** each stands as one of these:
  - Code's attestation;
  - the coordinating session's words;
  - the commit to come;
  - a placeholder, filled at the commit with this raw's path and the tallies.
- **O1:** applied. The routing quote names its one record in the repository.
- **O2:** applied: "The campaign's own Python process, the driver, appears in other sessions' entries as PID 8051 (for
  example `2834c2d`)."
- **O3:** applied. The extraction was "made in composing the end notice", which was "sent after it".
- **O4:** applied. Departure item 3 adds that it "bears also on v1.0 §13 item 3's end notice … and on r2 §4's form".
- **O5:** noted.
- **The checker's own departures,** as its report states them, for the seat to class:
  - a Read of the raw's first 60 lines displayed its PROVENANCE line, with the report's start stamp, in a tool output;
  - a grep listing the raw's calendar dates printed that stamp's date part in a tool output.

  Nothing of either is in the report. The checker noted three more and called them not departures: a `git log` with
  the adapter module's path in its argv, with no stage running; a digest-form check of G-F3's committed checkpoint;
  and a names-only listing of the record folder.
