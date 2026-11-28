# n — the N-pod VERDICTS entries: the blind values-check, its dispositions and the replay (the n-analyzer session)

PI date 2026-11-28. One blind values-check ran over the draft of the two entries, `entry_draft1.md` (sha256 `facbc518a452a2a496e366bed9d962f10f534c10afb17fb9de9eb67eb451d3d7`, 323 lines), against the outputs of record, the kit, the named raws and the committed files. Its report came back as text, since a subagent's file tool refuses report files; it is carried below verbatim, extracted from the hand-back with `decode_json` (sha256 `9977f6da710fa465371bdc20bf4ac4964e3d612133bac312b70ee006cbbcb086`), in a fence, with the repository's root printed as <repo> and the scratch folder as <scratch>, and a final newline added. It found 83 items (58 CONFIRMED, 13 IMPRECISE, 3 FAIL, 9 NOT CHECKABLE) and 11 observations. The dispositions follow it. The replay checked each disposition by tool over the entry as assembled after them (`entry_pre2.md`, sha256 `14d911732d07783a748fb2e3bad9e7a9deb080b455ccc7e51ec5bc2f16cd367a`); the entry of record differs from it in one value alone, this raw's sha256.

## The values-check's report, verbatim

````text
BLIND VALUES-CHECK: entry_draft1.md ("PROPOSAL-n N-pod — VERDICTS" and "— secondary DVs")

1. Draft sha256 (shasum -a 256): facbc518a452a2a496e366bed9d962f10f534c10afb17fb9de9eb67eb451d3d7

2. ITEMS

V1 CONFIRMED 1–2, 4. The tuple, `n_analyze.py verdicts` at v7 b6ea27f, run once, exit 0, stderr empty, 1 s. Sources: run/out.txt line 2; exit.txt 0; err.txt 0 lines (raw header: "stderr 0 bytes"); secs.txt 1; check.txt line 3 ("last touched at b6ea27f…"); b6ea27f's subject is "scripts/n_analyze.py v7"; one `run` call (3814).
V2 CONFIRMED 1. "n v0.2 §8 step 15; n:161's entry". §8 opens at n:154, step 15 is at n:159, and n:161 names "PROPOSAL-n N-pod — VERDICTS".
V3 CONFIRMED 2–4. Run in the window on AC power, on the PI's routing of 2026-11-27, N item 5 "[go]". Routing raw line 21 ends "[go]"; head.txt = b23f91d; check.txt has "PASS AC power". The grant itself is taken as context.
V4 NOT CHECKABLE 5, 173–174. "this commit's .gitignore lines admit…; the block is 6 lines". .gitignore is clean at HEAD (d53c400b both ways) and `git check-ignore` still reports N-pod_VERDICTS.json as ignored, so the lines are not written yet.
V5 CONFIRMED 6. N1 REPLICATED, so the FAIL at +1 changes no sentence. Raw (D) §2 item 3 (line 38).
V6 CONFIRMED 8. The VERDICTS line equals out.txt line 2 and out raw line 39, byte for byte.
V7 CONFIRMED 9–10. sha256s 4f29f294…c4c68c0 and 4133c48b…889c05 by shasum; schemas n-verdicts-v1 and n-secondary-v1; 8,363 and 5,539 lines; `.secondary` names the secondary's sha256.
V8 CONFIRMED 10–11. The tuple's coordinates. n_analyze.py:672 (G-READ-n coordinate = valence at d_eq).
V9 CONFIRMED 12–14, 16. Routing raw 248ba6fe…948d, tracked and clean at HEAD = b23f91d. Item 5 is at line 21. Line 51 reads " Route as given" (leading space).
V10 NOT CHECKABLE 15. "@@ITEM5@@" is a placeholder.
V11 CONFIRMED 16–19. Raw (D) 6b5be7a3…e420, tracked at b23f91d. §5 item 1 (line 58) lists the entry's contents. §5 item 4 (line 61) says this session "carries §2 items 3 and 6".
V12 CONFIRMED 20–22. Steps v2 cba11176…b0de, 325 lines; pins ec8cdd74…5f04; notes 290539f9…17ab; manifest 41876a62…163a, 13 lines, listing all three. `shasum -c` gives 13 of 13 OK now. The coordinating session's read is context.
V13 CONFIRMED 23. Four steps, once each, each in its own call: check 3812, run 3814, wait 3816, after 3822.
V14 NOT CHECKABLE 24. The messages' content, including "ended, exit status 0". The sweep shows two SendMessage calls to one recipient (3820 after the wait, 3825 after `after`), which fits.
V15 CONFIRMED 25. HEAD b23f91d from check to after: head.txt; check 3812 ran at 04:20Z, after b23f91d's commit at 04:14:16Z; HEAD is b23f91d now. PI date 2026-11-27 (date.txt).
V16 NOT CHECKABLE 26–27. The read-only step before check (3810). Its command does read the manifest count, ioreg AppleClamshellState, pmset and the date, but its output is in no source.
V17 CONFIRMED 28–41. check's 23 PASS lines and what they say. Sources: run/check.txt and the two pre-grant checks (check_v2_final.txt at 7ab1cf6, check_v2_at_b23f91d.txt), each 23 PASS / 0 FAIL; steps v2 lines 83–148. The window's own check (3812) left no file.
V18 CONFIRMED 36–37. The venv's bin is checked by builtins alone (steps line 132).
V19 CONFIRMED 42–45. run: check kept; the nohup caffeinate line is verbatim (steps line 175); PID 57594 (pid.txt); the caffeinate/PID note matches steps line 18 and the dispositions; inner writes secs, then exit (lines 199–200).
V20 NOT CHECKABLE 46–48. wait's printed line went to the harness's task file (read in 3818), which is not a source. Its form (POLL 5, kill -0, ps -o command=, the say line) is steps lines 203–222.
V21 CONFIRMED 50–57, re-derived now. On the out raw: home-prefix count 0; 0 lines with /private/ or /tmp/; the bracketed marker screen hits line 38 only, which is the INVOCATION line; stdout 2 lines; stderr 0 bytes; <repo> printed 7 times. data/n/verdicts holds exactly the two outputs at the printed sha256s. The six pins and the secondary's sha256 each appear once in VERDICTS. Neither output names a local root. Nine pins pass `shasum -c` (the report's value is bound in VERDICTS and in the close list's line 1). HEAD is unchanged; valence_core/ and scripts/ have 0 status lines; tmp/ is empty.
V22 NOT CHECKABLE 49, 57. `after` printing ALL PASS, and its sleep/wake note. after's stdout is in no source.
V23 CONFIRMED 58. Between 3814 and 3818 there are only plan, wait and wrap-up calls. The first read of run/ is 3818 (cat of the wait's task output, then run/exit.txt), after the turn closed at 3817. The tsv does not record when the end notice arrived.
V24 CONFIRMED 59–61. The INVOCATION line equals out raw line 38 byte for byte. The venv folder is kept as printed, the same form as the G-ANL-n out raw's line 2.
V25 CONFIRMED 62–63. No --out means data/n/verdicts (6633–6645). L:711 names gvec_cosines.json fc8877be…; L:716–718 calls it "the analyzer's `--gvec` file". --date comes from `date +%F` at run.
V26 CONFIRMED 63–69. Refused nothing (exit 0). The cited checks: verdicts_precheck 6625–6650 calls committed_problems (5892–5906) at 6641 on the analyzer plus lock, report, artifact and cosines (main passes them at 6826); 6687–6693; 6702–6706; 6722–6725.
V27 CONFIRMED 70–84. The table equals inputs_v2.sha256 line for line (tool diff). The pins file was written by shasum from the root (3766). 10 OK lines at run's check and in both pre-grant checks; the window's check and after left no file.
V28 CONFIRMED 85–92. env.txt's five lines verbatim; they are in the raw's header line 2; the sweep shows no query of the interpreter's own version.
V29 CONFIRMED 93–97. All four sentences equal `.sentences[7.1|7.2|7.3|N4].text` (tool compare).
V30 CONFIRMED 98–111. G-LEAK-n table rebuilt from `.gleak` with half-away rounding equals lines 101–111.
V31 CONFIRMED 112–121. G-READ-n table equals `.gread.table` (tool diff); artifact 378f9972…f519; `gread.auc.d_eq` = 0.9917578125.
V32 CONFIRMED 122–126. Raw (D) §2 item 3; PI item 4's condition (routing line 20); 7.1's label is null; dose keys on d_eq (PASS); N2 is decided at f = 0.20 (PASS); 7.3 ends "— answered".
V33 CONFIRMED 127–130. The totals equal the sums over `counters.records` (23 cells): 0/0/707/3637/0/0/0/0/7680. binomial_state, cap, stop and pauses come from the report (n_analyze.py:6758–6760) and match as given; the report's counters match; 23 fidelity rows.
V34 CONFIRMED 131–132. Exposure: 160/160/160, 160/160/160, 960/960/960; totals 320 and 960; the generations string verbatim.
V35 CONFIRMED 133–142. Cosines source and the six values at 4 dp (tool diff); identical in both outputs and in secondary (e).
V36 CONFIRMED 143–148. Rule string, tuple, over_half [], second_row null and the drops line match (tool); dropped reads sum to 1921; PIN-n-16's text is in `.pins`.
V37 CONFIRMED 150. v1 = 445d65fb…c681 (frozen.sha256; review §1).
V38 IMPRECISE 150–151. "extracted verbatim from the hand-back". The extraction (3759: JSON::PP->new->decode on undecoded bytes, then a UTF-8 output layer) double-encoded every non-ASCII character. report.md has 52 lines with "â" plus two control bytes where "–" should be, and "Â§" once; it has no correct en dash. Correction: the words are verbatim but the non-ASCII characters are double-encoded; say so, or re-extract with decode_json.
V39 CONFIRMED 152. "0 BUG, 6 RISK, 12 NIT (18 in all), plus one uncounted observation" (report.md line 3).
V40 CONFIRMED 153. F11 and F16 were adopted in part; the rest adopted; F17 was settled, with NOTES_v2:143 citing the PI's item 4.
V41 IMPRECISE 154–156. runs3 found two defects in v2 (the venv glob: noglob ended at 98, not 97; the scrub: a scratch path in the raw) and also a wrong stand-in (interrupted killed nothing; its after FAILed on 13 lines). See the dispositions' last section and NOTES_v2:120. Correction: "found two defects of its own and a wrong stand-in, all fixed before v2 went to anyone".
V42 CONFIRMED 154–156. 19 variants in each run (19 summary lines per log); fake git roots for v2. runs4 (3785) ran after the last edits (steps 3784, stand-in 3782, harness 3783), and every variant behaves as NOTES_v2:123–133 designs it.
V43 CONFIRMED 157. The raw holds the review, the dispositions and the logs (raw §§5, 6, 11, 12, 18).
V44 CONFIRMED 159–161. Docstring at 5893–5894; the report is among the checked paths at 6635–6641 (main 6826).
V45 CONFIRMED 162–166. The three names forms, each counted (steps v2 lines 122–124). The coordinating session's reading of them is in no source.
V46 NOT CHECKABLE 167–168. The grant's "ec8cdd74…5d04" is in no source. By tool the pins file is ec8cdd74…5f04, and the manifest checks 13 of 13 now.
V47 CONFIRMED 170–172. The outputs' full sha256s.
V48 CONFIRMED 175–177. Out raw 34f88cce…5ed8, 39 lines, built by after (steps 250–260): line 1 the parameters, line 2 the environment, lines 3–37 the check, then the two stdout lines; root as <repo>.
V49 IMPRECISE 178–182. Review raw ece65bab…e061, 1,850 lines; all 18 parts equal their files under the two substitutions (tool diff, 18 of 18). Missing qualifier, which the raw's own header states: the review's report lacks a final newline and gains one. V38's double-encoding carries into §5.
V50 NOT CHECKABLE 183–185. The values-check raw's sha256 is a placeholder; "at the Log's head" is still to come.
V51 CONFIRMED 186–190. G-ANL-n's last sweep ran 3404–3545 (RESULTS.md:8559–8560). The notes appended at 3584 say "Next entry's sweep starts at call 3546". final_draft1.tsv runs 3546–3875 with no gap. gen_departures.sh uses Perl JSON::PP, prints counts and call numbers only, and matches tolower text with bracketed patterns.
V52 IMPRECISE 187. "from 1641948 (2026-11-20)". 1641948 was made by call 3578 (git commit at 17:20:52Z = 12:20:52 -0500), so calls 3546–3577 ran at its parent b6ea27f. Correction: "from b6ea27f (2026-11-20; 1641948 from call 3578) to b23f91d".
V53 CONFIRMED 191–192. 330 calls: Bash 122, Read 61, Edit 55, update_plan 48, wrap_up 20, Write 16, SendMessage 5, Agent 1, ReadNotifications 1, ToolSearch 1.
V54 CONFIRMED 194–197. The lowered bracketed search matches only 3841, 3845 and 3870 (none of the reviewer's calls). Each carries JLENS|QWEN|MLX|OLMO|Olmo|OLMo|Qwen (seven words, four markers) through awk -v p=. 04:25–04:33Z is PI date 2026-11-27.
V55 IMPRECISE 197–198. "read-only, over this session's own extraction files in the scratch… printed call numbers only". In fact: 3841 wrote since3546.tsv. 3845 listed the session's subagents folder (`ls "$P"`), read the reviewer's transcript there by Perl, and wrote reviewer_calls.tsv. Between them the three calls printed counts by tool and by date, the first and last call numbers with timestamps (3841, 3870), and the transcript's file name (3845). No Python ran.
V56 CONFIRMED 198–199. gen_departures.sh lines 21–22 and 25 use the stated form.
V57 IMPRECISE 200–205. The five runs (3766, 3798, 3806, 3812, 3814) and 3564/3580's `--ignored -uall -- data/n $X` are right. But 3580 also ran `git status --porcelain -uall -- .gitignore RESULTS.md data/n/gates/G-ANL-n.json results/raw/2026-11-20_n-ganl_out.txt results/raw/2026-11-20_n-ganl_valuescheck.md`, which is not the bare form either. Add it.
V58 CONFIRMED 207–208. 3738's `git log --format=%h -n 3 -- "$p"` over the six inputs, the report among them; check's `git log --format=%H -n 1` (steps v2 line 95).
V59 IMPRECISE 209–211. check also ran `git rev-parse --verify -q <rev>:<path>` (v2 line 99, v1 line 55). And "nothing of the report was printed but OK lines" is inexact: 3738 printed the report's abbreviated sha256 with its count in the close list; check printed a PASS line naming the report and its full commit id; 3738's git log printed commit ids. None of its content was printed. Correction: "nothing of its content: ids, an abbreviated digest (3738), OK and PASS lines".
V60 CONFIRMED 212–213. Steps lines 122/124, each counted; 3806's diff over scripts, valence_core, data and 'LOCK-*', counted.
V61 CONFIRMED 214–215. 3655 and 3679 run `git log -1 --format=%h` with no pathspec. RESULTS.md:2591–2592 (that checker's "one `git log -1 --format` without item 3's pathspec") and 2612 ("This commit's departures (§4; item 4): inert") support the seat's classing. The raw itself is not among my sources.
V62 FAIL 216–233, 241. "The rest" plus "Code knows of no others" omits kinds that ran in the span.
  (a) G-ANL-n's commit window, 2026-11-20:
    - zsh -n checks and zsh runs of scratch scripts: check_edits.sh (3559, 3561); commit_steps.sh -n (3564); commit_steps.sh place/gate/stage/count (3571, 3573, 3575, 3576), which placed and staged five paths in the repository;
    - `git commit -q -F … -- <five paths>` (3578);
    - `git rev-list` (3579, 3580); `git cat-file blob|commit` into cmp and shasum (3579, 3580);
    - `git diff -U0 HEAD^ HEAD -- RESULTS.md` and `-- .gitignore` (content hunks); `git diff --stat … -- . $X`; `git diff --cached --name-only` (3564, 3580);
    - `od -c` (3561); `cat >>` heredoc notes (3566, 3584).
  (b) Elsewhere:
    - name-only `ls` (3727, 3754 at the repo root, 3775, 3845 the subagents folder);
    - `find -type f` in the scratch (3728);
    - `mv` (3856) and `sed -i ''` (3776);
    - `cat`, `head` and `tail` reads, including the harness's task-output files (3795, 3818), run/exit.txt (3818), run/secs.txt (3823), and `tail` of a committed raw (3727);
    - `perl -CSD -ne` over a named file (3644);
    - `git log --format=%h -n 1` over four package files (3762); `git diff --name-only 7ab1cf6 HEAD -- . <exclusions>` (3806); `git show --name-only --format= b23f91d -- results/raw` (3849);
    - `/bin/bash -c` (3761) and bash -n syntax checks (3741, 3747, 3766, 3770, 3785, 3798, 3875);
    - Writes and Edits of scratch files and of memory notes, by name (counted in the totals, never classed).
V63 IMPRECISE 217. "wc… of named raws and scratch files, none under data/". 3564 counted lines of data/n/gates/G-ANL-n.json; 3655 of LOCK-n.md and scripts/n_analyze.py; 3661 ran `wc -l -c` on a memory note; 3758 counted the reviewer's task-output file. None are under ckpt or reports.
V64 IMPRECISE 221. jq over the outputs ran in ten calls: 3827, 3828, 3829, 3830, 3831, 3832, 3833, 3852, 3854, 3855. Correction: "calls 3827–3833, 3852, 3854 and 3855".
V65 IMPRECISE 222. Besides JSON::PP over the transcripts, 3644 ran `perl -CSD -ne` over LOCK-n-v1.0-draft.md, printing line numbers, heads and a count.
V66 CONFIRMED 223, 225–226. pgrep (bracketed), ps, pmset, ioreg (3810), sysctl (3761); sw_vers runs only inside run's env_lines; the steps' modes at the stated calls.
V67 IMPRECISE 224. readlink, basename and dirname ran on the venv's python link after a builtin cd into the venv's bin (3761, 3764), not in the scratch.
V68 IMPRECISE 227–230. The description fits v2's harness (3770, 3785). v1's (3744, 3747) used plain fake folders with no git and ran `bash steps.sh run` in the foreground (standin_test.sh lines 12–23).
V69 CONFIRMED 231. 3776 is a traced nohup caffeinate launch in the scratch.
V70 FAIL 232–233. "the word python in three commands' text (3656, 3761, 3764)". The word stands in sixteen Bash commands:
  - grep/awk patterns: 3546, 3547, 3845;
  - echo/print strings: 3644, 3656, 3761, 3764, 3841, 3844, 3845;
  - `readlink python`: 3761, 3764;
  - stand_python*.in file names: 3749, 3750, 3770, 3785, 3799, 3800, 3864.
  It is also in four Write/Edit paths (3742, 3767, 3781, 3782). No interpreter ran in any of them.
V71 CONFIRMED 234–239. No Read under data/; no Write or Edit on a repository path; no python invocation besides the run; no ls or find of results/raw; memory files only by name. The repository writes made by Bash fall under V62.
V72 CONFIRMED 242–249. Reviewer: 58 calls (29 Bash, 27 Read, 1 Write, the hand-back). Call 28 is `git log --name-only` and call 29 `git grep`, both with item 3's exclusions. ckpt and reports are named only inside those exclusions; no Read under data/; no python; no marker; one mkdir (call 56); §3 is at raw line 769.
V73 CONFIRMED 250–251. Raw (D) §5 item 2 (line 59); routing item 5.
V74 NOT CHECKABLE 251. "The push is the PI's word": no source names this commit's push.
V75 CONFIRMED 253–256. n:159, §4 at n:128; the claim string; the secondary named by sha256; (f) at n_analyze.py:3716–3717.
V76 FAIL 261, 273, 280. Three (a) shares at exact decimal ties are not rounded half-away:
  - N1-P|+1: 0.44375 should be 0.4438 (draft 0.4437);
  - N1-V|+d_eq: 0.54375 should be 0.5438 (draft 0.5437);
  - N2-S|f0.10: 0.53125 should be 0.5313 (draft 0.5312).
  This is printf's binary rounding. 0.53125 is exact in binary and went to even, so it is wrong under any half-away reading.
V77 CONFIRMED 257–283, the other rows. Every n, pick S and below-floor value, and the other 20 shares, match (tool diff); 3720–3729.
V78 CONFIRMED 284. (b) equals B_STRUCK (n_analyze.py:709), with a closing period added.
V79 CONFIRMED 285–309. (c) equals `c_groups` (tool diff); means appear at n ≥ 20 only; 3731–3743.
V80 CONFIRMED 310. n = 160, r = 0.056254487770442306.
V81 IMPRECISE 311. "N2's three guard arms": N2-E is the evaluative arm (span_reward); the guards are N2-S and N2-C (PIN-n-33). The code's GUARD_DIRS (3065) holds all three. Correction: "N2's three arms (N2-E, span_reward; the guards N2-S, N2-C)".
V82 CONFIRMED 311–322. (e) means and CIs match (tool diff); level 95 for all; 3752–3759; the cosines equal VERDICTS'.
V83 CONFIRMED 323. floor_events = 20 (FLOOR_EVENTS; PIN-n-22); the claim string, with a period added.

3. OBSERVATIONS

O1. The sweep's class patterns pass `\\n` through awk -v. That becomes a real newline in the regex, which never matches the literal "\n" the extraction writes, so a command at the start of a line is missed. This is why V64's and V70's lists came out short. Use gsub(/\\n/,";") before matching at the final sweep.
O2. JSON::PP->new without ->utf8 (gen_departures.sh line 15, call 3759) double-encodes non-ASCII text. It shows in report.md, the raw's §5, and the tsv commands ("â¦").
O3. The launch review raw carries a guard marker on lines 1234 and 1376 (the stand-in's INVOCATION line, "jlens-stand"), besides the out raw's line 38. The commit screen will see these.
O4. The counters' totals and "1921" are sums over `counters.records` and `sensitivity.drops`, not output fields; say they are summed.
O5. The G-LEAK-n heading says "four decimals", but the match ratio is shown at two.
O6. The run was actually `TMPDIR=<kit>/tmp nice -n 19 ./python -I -B …` from the venv's bin (steps 192–196). The entry could say so beside the INVOCATION line.
O7. VERDICTS' `campaign` block (identity d566764f…7f8a, read plan 7f7d7301…88a6, 138 cells) could be cited beside the pins.
O8. 3840 printed the first 90 characters of the commands of calls 3540–3550 (to locate the span's start). The opening's "what they printed" and "the commit at each call" are not given per call.
O9. 3849 printed raw names under results/raw (one commit's names, unmasked).
O10. 3766 ran v2 before its edits at 3777–3784, so the "five v2 runs" covered two versions of the file.
O11. Dated note 3's "13 of 13" rests on call 3810's output; cite the call.

4. COMMANDS I RAN
- shasum -a 256 / -c: the draft, kit files, four named raws, the outputs, the proposal; the manifest (13 OK) and nine pins from the root (the report's line removed first with grep -v). Printed digests and OK lines only.
- ls, names only: kit folders, review/, standin runs3/runs4, K/n9, K/n9/ganl, K/n9/ganl/commit (empty), data/n/verdicts. Printed names.
- cat: run/'s six small files, the manifest, inputs_v2, frozen.sha256. Printed contents.
- wc -l and wc -c: kit, run, outputs, named raws (including the whole close list, 4,417 lines), the sweep files. Printed counts.
- Read (file tool): the draft; run files; steps v1 and v2; the out raw; report.md, dispositions, NOTES_v2; the routing raw and raw (D); n_analyze.py 655–679, 3700–3765, 5886–5909, 6600–6846; gen_departures.sh; both harnesses.
- head -n 1 of the close list: its first line.
- git rev-parse and hash-object (raws, proposal, analyzer, lock, .gitignore, RESULTS.md); rev-parse HEAD and 1641948^; merge-base --is-ancestor. All equal; yes.
- git log ids and times: 1641948^..HEAD and -n 3 with item 3's exclusions; -n 1 of five revs with no pathspec.
- git status --porcelain -- valence_core scripts with the exclusions: 0 lines.
- git check-ignore -q on N-pod_VERDICTS.json: ignored.
- jq over the two outputs: fields and rebuilt tables (one jq error, nothing printed from it).
- awk, sed, diff and [ ] comparisons and table rebuilds: EQUAL, apart from V76.
- /usr/bin/grep counts and -n over n_analyze.py, LOCK-n.md, the proposal, .gitignore, RESULTS.md, the G-ANL-n out raw, the out raw and review raw (screens and byte patterns), stand-in files and logs.
- awk over both sweep tsv files: counts, call numbers, timestamps, command-word tallies, and the truncated, root-masked text of about 60 records; records 3841, 3845 and 3870 printed whole.
- Review-raw part diffs: 18 of 18 EQUAL.
- My departures:
  - wc -l of the whole close list (beyond its first line);
  - git check-ignore, git log -n 1 <rev>, and a scoped porcelain status without the exact `-- .` form;
  - one glob (`reviewer/*`) used in the same command that first listed its folder (it expanded to report.md alone);
  - printed record text beyond counts while checking the departures;
  - guard markers appeared in my output only (records 3841/3845/3870, .gitignore line 42, review raw lines 1234/1376), never in an argv;
  - the word "python" in my own awk patterns; no interpreter ran.
  Nothing under data/*/ckpt, data/*/reports or data/mf3 was read, listed or stat'ed. I wrote nothing except to /dev/null.

5. TOTALS
83 items: 58 CONFIRMED, 13 IMPRECISE, 3 FAIL, 9 NOT CHECKABLE. 11 observations.
````

## Dispositions (Code, 2026-11-28 PI date; every item not CONFIRMED, and every observation)

Each fix went into the entries' sources (the template, its fragments, the launch review raw's build, the sweep), and
the entries were assembled again. The replay at the end of this raw checks each one by tool.

- **V4 (NOT CHECKABLE; the `.gitignore` lines not yet written):** met at the commit. The gate asserts the 6 added
  lines, the two outputs admitted, and the analyzer's temporary name ignored.
- **V10 (NOT CHECKABLE; `@@ITEM5@@` left in the draft): fixed.** The assembler's placeholder pattern held no digits,
  so this one line was not filled and the count of what was left missed it. The item now stands verbatim, the routing
  raw's line 21.
- **V14 (NOT CHECKABLE; the messages' content):** stands as context. The entry cites the calls.
- **V16, V20, V22 (NOT CHECKABLE; the pre-step's, wait's and after's printed lines): met.** The launch review raw's
  part 19 carries what calls 3810, 3812, 3814, 3818 and 3822 printed, extracted verbatim from the transcript's tool
  results. The entry cites them.
- **V38 (IMPRECISE; the review's report encoded twice): applied.** It was re-extracted with `decode_json` as
  `report_v2.md`. That file equals `report.md` with the double encoding undone, byte for byte. The raw carries
  `report_v2.md`, part 5's heading names `report.md`'s sha256, and the entry says so.
- **V41 (IMPRECISE): applied:** "two defects of its own and a wrong stand-in, all three fixed".
- **V46 (NOT CHECKABLE; the grant's `…5d04`):** stands. The coordinating session's message named it its own slip,
  and the entry says so.
- **V49 (IMPRECISE): applied.** The record names the final newline and the decoded report.
- **V50 (NOT CHECKABLE; this raw's sha256 a placeholder):** met at assembly.
- **V52 (IMPRECISE): applied:** `b6ea27f` at call 3546, `1641948` from call 3578.
- **V55 (IMPRECISE): applied.** The entry now gives what 3841, 3845 and 3870 wrote, read and printed.
- **V57 (IMPRECISE): applied.** It adds 3580's `git status --porcelain -uall -- <five named paths>`.
- **V59 (IMPRECISE): applied.** It adds check's `git rev-parse --verify -q <rev>:<path>`, and now reads "nothing of
  its content: ids, an abbreviated digest (3738), OK and PASS lines".
- **V62 (FAIL): fixed.** "The rest" is rewritten by kind from a tally of every command segment's first word
  (`gen_departures_v2.sh`). It covers G-ANL-n's commit window (zsh runs of the commit steps, which placed and staged
  five paths; the commit; the verification's `rev-list`, `cat-file`, content hunks and `--cached --name-only`; `od`;
  heredoc notes) and every other kind the item lists.
- **V63, V64, V65, V67, V68 (IMPRECISE): applied:**
  - the `wc` targets, listed by class;
  - the jq calls, 3827–3833, 3852, 3854 and 3855, and 3894 since;
  - 3644's `perl -CSD -ne`;
  - the venv's link, read after a builtin `cd`;
  - v1's harness and v2's, described apart.
- **V70 (FAIL): fixed.** The word "python" stands in sixteen Bash commands and four Write or Edit paths, each listed.
- **V74 (NOT CHECKABLE; the push):** stands. The coordinating session's messages say the push is the PI's.
- **V76 (FAIL): fixed.** The shares are now rounded half-away from pick S / n by integer arithmetic: 0.4438, 0.5438
  and 0.5313.
- **V81 (IMPRECISE): applied:** N2's three arms, named.
- **O1: applied.** `gen_departures_v2.sh` turns escaped newlines into separators before it matches. Its lists equal
  V64's and V70's.
- **O2: applied.** `decode_json` in `extract.pl` and in `gen_departures_v2.sh`.
- **O3: applied.** The record names the five lines whose content holds a marker: the out raw's INVOCATION line, the
  stand-in logs' two printed INVOCATION lines in the launch review raw, and two lines of this raw (the report's V54
  and O3).
- **O4–O7: applied:**
  - the totals and the reads dropped are marked "summed";
  - the match ratio is shown at two decimals;
  - the run's form stands beside the INVOCATION line;
  - VERDICTS' `campaign` block is cited.
- **O8: applied.** 3840's printing is in the departures. The departures give each kind with its calls, not a line
  per call.
- **O9: applied.** 3849 is among the sweep method's classes.
- **O10: applied.** The five runs are split: one before v2's last edits, four on the final bytes.
- **O11: applied.** Call 3810 is cited.
- **The checker's own departures:** carried into the entry's departures section, as its report lists them.
- **Code's, after the check:** call 3894 wrote a stray file in `/tmp`, holding secondary (a)'s shares, and call 3895
  listed and removed it. It is declared in the entry, against the rules as written. The final sweep runs through the
  last call before the commit.

## The replay (`replay.sh`, over `entry_pre2.md`)

````text
PASS V10: present (1)
PASS V10b: absent
PASS V16-V22: present (1)
PASS V38: present (1)
PASS V41: present (1)
PASS V49: present (1)
PASS V52: present (1)
PASS V55: present (1)
PASS V57: present (1)
PASS V59a: present (1)
PASS V59b: present (1)
PASS V62: present (1)
PASS V63: present (1)
PASS V64: present (1)
PASS V65: present (1)
PASS V67: present (1)
PASS V68: present (1)
PASS V70: present (1)
PASS V76a: present (1)
PASS V76b: present (1)
PASS V76c: present (1)
PASS V76d: absent
PASS V81: present (1)
PASS V81b: absent
PASS O1-O2: present (1)
PASS O3: present (1)
PASS O4a: present (1)
PASS O4b: present (1)
PASS O5: present (1)
PASS O6: present (1)
PASS O7: present (1)
PASS O8: present (1)
PASS O9: present (1)
PASS O10: present (1)
PASS O11: present (1)
PASS stray: present (1)
replay: 36 of 36
````
