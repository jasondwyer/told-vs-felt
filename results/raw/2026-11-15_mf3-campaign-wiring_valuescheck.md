# The campaign wiring (Q-F3): the blind values-check (its brief, the checker's report, Code's dispositions)

*F3 session, Code's date 2026-11-15, HEAD `a89a4fa`. One blind pass, by a subagent under the brief below, which quotes
the list of record v2's items 1–5. The brief is verbatim, its local paths scrubbed (`<tmp>` is the scratch root; `A` in
the brief and the report is Code's scratch folder for this commit). The report is verbatim, extracted by script from
the checker's hand-back (sha256 `fe56c927…8577`, its final newline included; 114 lines). It needs no scrub: it names no
local path. Code's dispositions follow it.*

----------------------------------------------------------------------------------------------------
The brief (verbatim; local paths scrubbed)
----------------------------------------------------------------------------------------------------
You are a blind values-checker for a research project's records, in the git repository at <repo>. Other sessions share this working tree and may commit while you work; do not modify it.

You are read-only:
- no git writes of any kind (no add, commit, stash, checkout, reset, worktree or switch; `git hash-object` only without `-w`);
- no file written or edited anywhere;
- no model run, and no run of `scripts/mf3_sessions.py` in any form. Its self-test output is given to you as a file.

Return your report as text in your final message, between a line `=== BEGIN REPORT ===` and a line `=== END REPORT ===`, and give its sha256 (over the text between the markers, as UTF-8, ending in one newline). Write it to no file.

## The list of record v2, items 1–5 (verbatim; they bind you)

1. **Permitted (names, ids, digests):** a bare `git status --porcelain`; a name-only `ls` (no `-l`, `-t`, `-s`, `-la`); `git ls-files`; `git ls-tree --name-only`; `git diff --name-status` and `--name-only`; `git show --name-only` and `--name-status`; `git log --name-only`; `git log` with `--format` of ids, subjects and commit times over any path; `shasum`/`sha256sum` and any program's digest that prints no byte, size or time; `git rev-parse <rev>:<path>` compared in the shell; `git check-attr`; a `find` that prunes every `*/ckpt` and `*/reports` directory (`find … \( -path '*/ckpt' -o -path '*/reports' \) -prune -o … -print`).
2. **Content.** Files under `data/*/ckpt` (the checkpoints and call logs) are read by nothing but the stage's own code, G-VER, the analyzer and the pre-push screen of item 4: no `cat`, `head`, `tail`, `json.load`, editor or search over them. Files under `data/*/reports` are the read domain (m:271; the stage writes them redacted) and may be read for their content by Code and by the seat — for a stage entry's figures, a declared counter, or a read — with nothing from them printed into a raw beyond what the entry's form reports. **Metadata:** no size or time of either directory or any file in them, in any form (`--stat`, `--numstat`, `ls -l/-t/-s/-la`, `du`, `wc -c`, `stat`, `git ls-tree -l`, `git cat-file -s`, any unpruned `find`, `mdfind` over them).
3. **Content searches** over a checkout or a tree — `git grep`, recursive `grep`, `rg`, `mdfind -onlyin`, and the pickaxe (`git log -S` / `-G`) over any range — exclude the checkpoint and report files with a form tested on this git: `-- . ':!data/*/ckpt/**' ':!data/*/reports/**'` (equivalently `':(exclude,glob)data/*/ckpt/**' ':(exclude,glob)data/*/reports/**'`, or `':!data/**'` where nothing under `data/` is wanted), or the prune for `find`-driven greps. The bare `':!data/*/ckpt'` form is not an exclusion on git 2.39.5 and is not used. A pickaxe search without the pathspec can name a commit whose checkpoint matched, which is content; it is a departure.
4. **The pre-push screen** may read every file in the range, `ckpt` and `reports` included, and prints only a per-class verdict, range totals, and one line per distinct match outside those directories; a match inside one is a count by path class and a halt for the seat.
5. **A running stage:** the end-wait is on the PID alone (O3-1); no `stat`, listing, `tail`, `Monitor` or read of its raw, checkpoint or reports until the invocation has ended — in every session, including the coordinating one.

Also binding:
- **For any file under `data/*/ckpt` or `data/*/reports`, digest forms only** (the seat's ruling of 2026-11-15): `shasum -a 256`, or `git hash-object -- <path>` compared with `git rev-parse <rev>:<path>`. Never `git show` or `git cat-file -p` of such a blob. You need no such file for this check.
- `jlens-qwen36/` is a separate repository: run no git command inside it.

In practice, for this task:
- None of the texts concerns a stage's outputs. You need nothing under `data/` but `data/mf3/gates/Q-F3_G-PWR.json` (outside `ckpt` and `reports`): open, read, list, size or traverse nothing else there.
- Every content search over the checkout or a tree carries item 3's tested form, here `':!data/**'`. `grep -r` and `rg` exclude the `data` directory.
- Use no `--stat`, `--numstat` or `--shortstat` form anywhere. To see which files a commit changed, use `git show --name-only` or `--name-status`.
- Python, if you use it: stdlib only, run as `python3 -I`, importing no repository code.
- Do not open anything under `<tmp><tmp>tasks/`, and no session transcript.
- In the scratch directory A (below), do not open, list or search `A/r2/work/clone/`. You need nothing in it.
- The Bash tool's `grep` is ugrep: use `/usr/bin/grep`.

If you break any of this by accident, say so at the end of your report: give the command's kind and what printed, without reproducing anything that printed.

## What to check

Code (another session) has edited `scripts/mf3_sessions.py` to wire its `campaign` subcommand (Q-F3's campaign), had the edit blind-reviewed, and fixed it after the review. The edit is uncommitted. Code asks you to check every factual claim in its drafts against their sources: every quote, file:line reference, figure, count, hash prefix, commit id, date and attribution.

The scratch directory A = <tmp>/a6 . The drafts:
1. `A/r2/entry_filled.md`, the RESULTS.md entry for the wiring's commit. `@@VC@@` is a placeholder: grade it NOT CHECKABLE. The entry's links name the raws by their committed paths; the drafts of those raws are items 2 and 3.
2. `results/raw/2026-11-15_mf3-campaign-wiring_review.md` (untracked), the review raw: Code's header, Code's dispositions, round 2's section and table, then the reviewer's report verbatim.
   - Check the header and the dispositions against the reviewer's report (the same file's verbatim part) and against the code (HEAD's driver and the working tree's).
   - Check the round-2 section and table against `A/r2/work/` (the harness `harness.py`, the generator `gen_mutants_r2.py`, the mutants `mutants/` with `manifest.tsv`, the run list `round2_list.txt`, the runs `runs/`, and `round2_results.txt`, plus any `confirm_*` files there). Round 2's first pass, on an intermediate candidate (`candidate_9aedead9.py`), is kept beside them: `mutants_9aedead9/`, `runs_9aedead9/` and `round2_results_9aedead9.txt`.
   - The verbatim part is the reviewer's: check only that it is intact, against `A/r2/report_verbatim.md` (sha256 `8fe80358…7c48`, of the text with its final newline) and against the reviewer's own copy, `A/review/report_text.txt`.
   - The header's transcript-scan claims rest on a transcript you may not open: grade them against `A/r2/scan_reviewer.py` and its output `A/r2/scan_reviewer.txt`, and say that this is all you checked them against.
3. `results/raw/2026-11-15_mf3-campaign-wiring_selftest.txt` (untracked), the self-test's output, scrubbed, under Code's one-line header. Check the header's claims. Check that the rest differs from the original, `A/r2/selftest_full_4.txt`, only where a local path became `<repo>` or `<tmp>`. Check that no local path, user name, session id or temp id survives. Check its last line.

The sources (all readable under the rules above):
- **The edit:** the working tree's `scripts/mf3_sessions.py` against HEAD's (`git diff scripts/mf3_sessions.py`; `git show HEAD:scripts/mf3_sessions.py`). The candidate the review read is `A/candidate_r1.py` (the same bytes as `A/r2/pre_fix.py`). The fixes after the review were applied by `A/r2/apply_fixes.py`, a rewrap of four over-long lines (an inline script, not kept; `A/r2/fix_full.diff`, the review candidate against the final bytes, shows every change), then `A/r2/apply_fixes_2.py` and `A/r2/apply_fixes_3.py`, in that order. The final bytes are the working tree's file and `A/r2/work/candidate.py`.
- **The self-test on the final bytes:** `A/r2/selftest_full_4.txt` (the run the raw is made from). Earlier runs: `A/selftest_full_1.txt` (the review's candidate, 233/233); `A/r2/selftest_full_2.txt` and `A/r2/selftest_full_3.txt` (intermediate candidates, before `apply_fixes_2.py` and before `apply_fixes_3.py`); and `A/r2/part_campaign_4.txt` (the campaign part alone on the final bytes). The `qual` wiring's committed self-test raw, `results/raw/2026-11-12_mf3-qual-wiring_selftest.txt`, gives the count before this edit.
- **The routing:**
  - The seat's answers of 2026-11-15, `results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md` (committed at `a89a4fa`): §2 (a), §5 item 2.
  - The PI's paste block, relayed by the coordinating session. It is not in the repository; its section A item 6, verbatim, and the PI's word, are the only source for the items they bear on:

    > 6. After v1.0's commit: the campaign wiring (F-1's kind; its entry names the edit and the new DRIVER blob and notes that v1.0 §6's value is the driver at the lock; NOTE-7's gap closed; G-SHAPE-F3 not re-run) [go; order as given].
    >
    > PI: "Route as given"

    The block's header reads "DESIGN → PI → CODE (master session) — PI date 2026-11-15".
- **The spec:**
  - `LOCK-m-F3.md` (v1.0, committed at `a89a4fa`): §1, §2, §4, §5, §6 (the driver, its PIN texts and sites), and v0.2's text below it (§2, §3);
  - `PROPOSAL-m-gating-campaign-v1_11.md` (`m:N` = its line N; m:192, m:298, m:330, m:361);
  - the stage library, `valence_core/mf3/stages.py` (`run_campaign`, `_refinish_campaign`, `_campaign_outputs`, `_paused_unadjudicated`, `prior_gate`, `gid_artifact_problems`, `out_paths`, `checkpoint_path`, `ANALYZER_PATH`, `PRIOR_STAGE`), `valence_core/mf3/schedule.py` (`FLOORS`), and `data/mf3/gates/Q-F3_G-PWR.json`;
  - `scripts/m_sessions.py`: its campaign wiring (`camp_pauses` in `main`; `_campaign_state`, `campaign_ruling_problems`, `ruling_line`, `ruling_texts`; its self-test's ruling-file guard case near its line 5510 and its FIFO cases near its lines 6280 and 6363).
- **The earlier wirings, for the form claimed:** RESULTS.md, the `qual` wiring's entry (search "The `qual` wiring:"), and its review raw `results/raw/2026-11-12_mf3-qual-wiring_review.md` (NOTE-5, NOTE-7).
- **The review:** the brief `A/brief_review_filled.md`; round 1's work directory `A/review/` (`harness.py`, `gen_mutants.py`, `mutants/`, `runs/`, `screen_results.txt`, `confirm_results.txt`); round 2's `A/r2/work/` as above; Code's dispositions draft `A/r2/dispositions.md`.

Grade each claim CONFIRMED, IMPRECISE (true in substance, but the wording or anchoring is off; say the fix), FAIL (wrong; say what is right) or NOT CHECKABLE (say why). Number your items, and give file:line evidence.

Pay special attention to:
- whether each quote is verbatim: the seat's, the PI's, the lock's, m's and the code's, including both forms (before and after) of the revised WIRED_CMDS sentence, against HEAD's file and the working tree's;
- every count: the self-test's checks (the total, the campaign block's, the new ones), the refusal cases, the PIN sites and their anchors on both blobs, the mutants and their results in both rounds;
- whether each claimed fix is in the final bytes and does what the disposition says (MINOR-1 to MINOR-3, NOTE-2 to NOTE-5, NOTE-7, and the kill cases for P03, S03, L02, M03, G01);
- whether "the rest of `time`'s, `id`'s and `qual`'s PIN texts is unchanged" holds against HEAD's driver;
- whether "the edit touches no scoring-stack function; every change is in the driver" holds;
- the outputs, the exit codes and the refusal behaviour claimed, against the code (not against any file under `data/` but G-PWR's record);
- whether CAMPAIGN_PAUSES now equals m's `camp_pauses` exactly, and whether each restored piece is true of Q-F3 as the dispositions say;
- whether the drafts state anything as a rule or a precedent that no committed record states;
- whether the drafts claim anything Code did that the sources do not show;
- no clock time, time stamp or `$` figure in the entry, the review raw's Code parts or the self-test raw's header (file:line anchors such as `m:298` are not clock times).

End with a tally and the list of everything not CONFIRMED. State HEAD (`git log --format='%h' -1`) at your start and at your end.

----------------------------------------------------------------------------------------------------
The checker's report (verbatim; sha256 fe56c927be0feabb62b764bebef0f36ba75491e2fd84e8cacf83e5b8159e8577)
----------------------------------------------------------------------------------------------------
Values-check of the Q-F3 campaign wiring's drafts (blind, read-only)

Conventions. A is the scratch directory the brief names. "entry" is A/r2/entry_filled.md; "raw" is results/raw/2026-11-15_mf3-campaign-wiring_review.md; "st-raw" is results/raw/2026-11-15_mf3-campaign-wiring_selftest.txt. "driver :N" is the working tree's scripts/mf3_sessions.py (sha256 7bb6f7ca…28a4, equal to A/r2/work/candidate.py); "HEAD :N" is HEAD's blob of it (sha256 285eed04…0e44); "cand :N" is A/candidate_r1.py (sha256 206dc3fc…98b9, equal to A/r2/pre_fix.py and A/review/candidate.py); "stages.py" is valence_core/mf3/stages.py; "m :N" is scripts/m_sessions.py; "answers" is results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md (sha256 49b82ff0…0885).

HEAD at start: a89a4fa. HEAD at end: a89a4fa.

The entry (A/r2/entry_filled.md)

1. entry :1–5, the headline: F-1's kind; only the driver changes (285eed04…0e44 → 7bb6f7ca…28a4); mf3's package, m's, the analyzer and the lock stand; 235/235; 50 mutants, no MAJOR; three MINORs and five NOTEs applied, one flagged; round 2 kills every survivor. CONFIRMED: `git status --porcelain` shows the driver as the only changed tracked file; the digests above; st-raw :252; raw :176–180; A/r2/work/round2_results.txt.
2. entry :1, "(Q-F3's campaign, m:298, m:361)". CONFIRMED as the unit's usage: m:361 names the campaign; m:298 is the LOCK-m-F3 v1.0 line, which the lock's title (LOCK-m-F3.md:1) and the seat's §A.7 heading as v1.0 quotes it (LOCK-m-F3.md:9, "(m:361; m:298; …)") cite for what v1.0 licenses, as the driver's own docstring and STAGE_HELP now do.
3. entry :6–7, the routing: "Route as given", PI date 2026-11-15, on the seat's answers of 2026-11-15, 49b82ff0…0885, committed at a89a4fa. CONFIRMED: shasum of answers; `git log` names a89a4fa as the commit that adds it; the PI date is the paste block header's, as the brief gives it.
4. entry :9, section A item 6. CONFIRMED: string-equal to the brief's copy.
5. entry :11, :13, the seat's §5 item 2, "verbatim (bold markers aside)". IMPRECISE: verbatim through "G-SHAPE-F3 is not re-run." (answers :43), but the item goes on with a sentence the quote drops unmarked: "(If the PI would rather the lock name the campaign's own driver, as p's locks do, the wiring goes first and the draft regenerates once more; the seat's default is the order above, which locks the unit now.)". Fix: quote the item whole, or mark the cut and say so ("its closing parenthesis aside").
6. entry :15, §2 (a). CONFIRMED: string-equal to answers :22 with the bold and the list marker dropped.
7. entry :17–19, the DRIVER line. CONFIRMED: v1.0 §6's value is 285eed04…0e44 (LOCK-m-F3.md:164); the full hash at entry :19 is the working tree's sha256; `git check-attr -a` sets no attribute on the driver, so the committed blob will carry those bytes; "the unit's convention since the `time` wiring" is the seat's phrase (answers :43).
8. entry :21–23, the stage. CONFIRMED: stages.run_campaign (stages.py:1450–1581), unchanged (nothing under valence_core/ changed); the interleave over keys.TEMPLATES; looks at LOOK_EVERY = 40 (valence_core/m/resume.py:91); cap 120 (driver :255); m:330 opens "Cadence every 40 launches".
9. entry :24–29, the values. CONFIRMED: driver :250–251, :425–430; LOCK-m-F3.md:55, :57, :71, :101; data/mf3/gates/Q-F3_G-PWR.json (sha256 75d1d46b…01e5): launch.L and inputs.floors equal them; valence_core/mf3/schedule.py:44 (A1 uncached 80); m:192 "L is a projection, not a bound".
10. entry :30–33, the lock. CONFIRMED: driver :500–511; QUAL_LOCK_LINES :225; CAMPAIGN_LOCK_LINES :252–253; the committed lock (sha256 fe9518c7…1aa6) carries both v1.0 lines as whole lines (LOCK-m-F3.md:71, :101) and v0.2's two lines at a line's start (:413, :431); v0.2's blob is refused (the variants check, driver :3444). Note: §2 (a) also says "the `qual` wiring's line test", a line-start test; the driver's whole-line test is stricter, as its PIN (driver :437–443) and the reviewer (raw :270) say. The entry's "as the seat's §2 (a) has it" rests on (a)'s "whole lines" and stands.
11. entry :34, the identity. CONFIRMED: driver :254–255, :516–525; the self-test asserts it equals G-F3's (driver :3415).
12. entry :35–36, the prior. CONFIRMED: driver :256, :557–573, :874–882 (require_real=True), :897–900; stages.py:460–523 (the status must be PASS), :435–438 (no artifact, no problem), :1484–1487 (the stage's re-check).
13. entry :37–41, the rulings and carry-overs. CONFIRMED: ruling_texts driver :752–785; ruling_line :721–749; O4-1, O1-3, RM4-1, VC4-1 and VC4-2 in the module docstring (:86–100, :113–115); CAMPAIGN_PAUSES (:261–292) equals m's camp_pauses (m :7427–7462) exactly (both literal-evaluated from their source by ast; 3,012 characters each).
14. entry :42–46, before the load. IMPRECISE (minor): "each in the words the stage uses after the load" — two of the mirrored refusals carry a declared suffix: CHECKPOINT MISMATCH's "(the stage makes this refusal after the load)" (driver :671–672) and NO PAUSE TO ADJUDICATE's last-pause tail (:711–717). Fix: "each in the stage's words, two with a declared suffix". The rest CONFIRMED (driver :848–900; `shown` :864–866; stages.py:1492, :1520).
15. entry :47–48, the outputs. CONFIRMED: stages.out_paths (stages.py:100–111); the excerpt only when the checkpoint records a pause or a hit (stages.py:1717–1756); no reads file (stages.py:1695–1698; reads None at :1468).
16. entry :49, the exit codes. CONFIRMED: stages.py:73; run_stage returns 2 before the load and 4 on a SystemExit (driver :1025–1169).
17. entry :51–53, WIRED_CMDS, the four campaign branches, run_stage's two parameters. CONFIRMED: driver :163–164 (REFUSED_CMDS empty), :472, :500–525, :557–573, :848–900, :1025–1028, :1080–1081, :1097–1165.
18. entry :54–58, "New: …" (the edit, named). IMPRECISE (completeness): every name listed is new (the top-level diff adds 8 functions and 8 constants), but the list leaves out `_lines_prefixed` (driver :1197; named under NOTE-7) and `_selftest_campaign` (:3297; named under Self-test), and the edit's changes to existing code and text go unnamed: `main`'s description and no-action line (:4280–4281, :4344); the module docstring's Q6 and INVOCATION sentences (:112–117, :126–127); `_selftest`'s wiring check, now "none refused", in place of HEAD's "campaign is refused" check (HEAD :786; driver :1236–1240); `_selftest_id`'s not-wired case, now `gshape` (driver :2195–2197; HEAD :1744 used `campaign`). The `qual` entry named its like change (RESULTS.md:1716–1717). Fix: one more line naming them.
19. entry :59–64, the revised WIRED_CMDS sentence, both forms, its anchors, and "the rest … is unchanged". CONFIRMED: the old form is verbatim at HEAD :108–109 and in v1.0 §6 (LOCK-m-F3.md:177, :180); the new form is verbatim at driver :162; PIN :102 → :156, sentence :108 → :162. Each of the 17 other earlier PIN texts is byte-equal (lines joined) between HEAD and the working tree, and the :102/:156 PIN differs by that sentence alone. "What the three do, print and refuse" holds by reading every shared hunk: the line-start refusal names stages.stage_name("qual"), "G-F3", as HEAD's literal did; PRIOR PATH REFUSED for id and qual reads as at HEAD; `shown` short-circuits off the campaign; ruling_texts(None, None) reads nothing; the RULING line is campaign-only; the qual branch keeps its arguments.
20. entry :65–73, the PIN sites. CONFIRMED: grep on the new blob gives exactly the nine new sites, each "declared at the Q-F3 campaign wiring", and the 18 earlier ones at the anchors given; grep on HEAD gives the 18 "from" anchors, which are v1.0 §6's (LOCK-m-F3.md:177–178, :187–190, :196–207).
21. entry :74, F-1. CONFIRMED: the driver is the only changed tracked file (the `qual` entry's same claim, RESULTS.md:1718).
22. entry :75–78, NOTE-7 closed. CONFIRMED: driver :2785–2818 (HEAD :2334–2335 replaced the first occurrence only); the new check (:2813) asserts qual's acceptance, the line-wise variant's refusal and a first-occurrence count of 1.
23. entry :79–81, the counts. CONFIRMED: 214 (results/raw/2026-11-12_mf3-qual-wiring_selftest.txt); 235/235 (A/r2/selftest_full_4.txt, st-raw :252); by check names the final run adds exactly 21 (the 20 chk calls of `_selftest_campaign`, driver :3388–4245, and NOTE-7's, :2813) and replaces one (the wiring check).
24. entry :82–84, :86–100, what the campaign's checks assert. CONFIRMED: 44 refusals (driver :4064); the FIFO case (:4067–4097); the joined line (:4098–4111); the seam and ruling-file cases (:4112–4153); five loader reaches (:4154–4183); three post-load STOPs (:4223); the post-load call (:4231); nothing loaded or written (:4244–4250).
25. entry :85, "The help gives the flags and m's `camp_pauses`, read from m's source, at both levels." IMPRECISE (minor): the top-level --help gives the campaign's help line with CAMPAIGN_PAUSES, not its flags (driver :3474–3484). Fix: "campaign --help gives the flags and camp_pauses, the top-level --help camp_pauses".
26. entry :103–104, round 1. CONFIRMED: A/review/screen_results.txt and confirm_results.txt, recounted against the baselines (18/18, 88/89, 232/233): 43 killed, S02 and T02 by fewer checks (6 and 5 of 18); 7 survived (K05, K03; S03, L02, P03, M03, G01).
27. entry :106–107, "the self-test's ruling-file guard call now runs as m's does, on fresh roots with a stub factory inside the traps". IMPRECISE: m's case (its round 1's M1-7, m :5510–5520) is three calls (qual and id with the adjudication file, time with the PI stop's), each on a fresh root with a stub factory, inside no trap stack; the driver's six calls inside the trap stack (:4112–4138) go beyond it. Fix: "in m's form (fresh roots, a stub factory), now inside the traps".
28. entry :108–111, MINOR-2 and MINOR-3 applied. CONFIRMED (items 50–51).
29. entry :112–117, the NOTEs. CONFIRMED (items 52–58).
30. entry :118–120, NOTE-8. IMPRECISE (one word): "The report's identity prints it" — the report, a file, carries backend_identifier in its identity (stages.py:863–867, :1713); no line the stage prints names it (its STAGE line, stages.py:874–875). Fix: "carries it". The rest holds: nothing in the driver or under valence_core/ names a734dadec8f8ce9b (grep); mf3's load_or_init refuses any identity difference on a resume (valence_core/mf3/resume.py:233–240), a pending end's re-finish aside, which may differ in backend and generates nothing.
31. entry :121–125, round 2. CONFIRMED (items 61–73).
32. entry :126, @@VC@@. NOT CHECKABLE (placeholder).
33. entry :127–128, committed by path; nothing ran on a model; not pushed. NOT CHECKABLE: a future commit; "nothing ran on a model" agrees with blocked_imported=[] in every harness run and with the self-test's trap counts, and can be checked no further.
34. entry :129–130, "Next (section A, item 7)". NOT CHECKABLE: the brief gives the paste block's item 6 only. The content agrees with answers :44 (§5 item 3) and :55 ("[your go, at your timing]") and m:330.
35. The entry carries no clock time, stamp or $ figure. CONFIRMED.

The review raw

36. raw :3, "Code's raw, PI date 2026-11-15". CONFIRMED (the paste block's date; the `qual` review raw's form).
37. raw :4–6, what was reviewed. CONFIRMED (the digests above; raw :182).
38. raw :7–11, how. CONFIRMED: A/brief_review_filled.md :11–15 quote items 1–5, each found verbatim in results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md; the sparse patterns (the brief :41; the scan's first flagged command); the import block (raw :455); 50 mutants (A/review/mutants/manifest.tsv).
39. raw :12–14, outcome. CONFIRMED (item 26).
40. raw :15–19, after the review. CONFIRMED: A/r2/fix_full.diff; 235/235 in A/r2/selftest_full_4.txt; 233/233 in A/selftest_full_1.txt; A/r2/work/round2_list.txt.
41. raw :20–21, 60 distinct Bash commands over every row. CONFIRMED against A/r2/scan_reviewer.py and A/r2/scan_reviewer.txt only (463 rows, 60 distinct commands, none held only in request blobs).
42. raw :22–25, two name a ckpt or reports path and neither reads such a file. CONFIRMED against the scan only: its two flagged commands are the clone's set-up with its sparse patterns, and a /usr/bin/grep over the candidate whose pattern carries "It writes data/mf3/ckpt/Q-F3_campaign.json".
43. raw :26–28, "Three more name `data/` …". NOT CHECKABLE against the scan: scan_reviewer.py has no data/ category and scan_reviewer.txt names none of the three commands. The reviewer's own Method says the same (raw :428, :450–451), but the scan the raw credits does not show it. Fix: keep the scan that found them beside the others, or cite the report.
44. raw :29, git status. CONFIRMED against the scan only (one command, a `git -C` on the clone with `status --porcelain`).
45. raw :30–32, the git commands in the main checkout. CONFIRMED against the scan only: its four "git commands without the clone in their text" are those forms (rev-parse HEAD; show HEAD:scripts/mf3_sessions.py into shasum; log --format='%h %s' -3, piped to cut; diff -- scripts/mf3_sessions.py into edit.diff), each allowed by the brief (A/brief_review_filled.md :22–23). The scan's test is textual: a command that also names the clone is not listed.
46. raw :34–36, the report's sha256 8fe80358…7c48 (final newline included), 317 lines, equal to the reviewer's copy; no local path, no clock time. CONFIRMED: shasum and cmp of A/r2/report_verbatim.md and A/review/report_text.txt; the raw's text after its heading equals them; grep finds no home, private, var or tmp path and no HH:MM.
47. raw :34, "extracted by script from the agent's hand-back in its transcript". NOT CHECKABLE (the transcript is off-limits; A/r2/extract_report.py exists and does that).
48. raw :37, "Nothing ran on a model". NOT CHECKABLE (as item 33).
49. raw :41–48, MINOR-1. IMPRECISE: "The case is now m's form (m's round 1's M1-7)" heads six calls inside the trap stack; m's form is item 27's. The details hold: six calls (driver :4129–4138); fresh roots and stub factories; the stack now traps run_gate_stage and run_gid_pair_f3 (:4121–4122; cand :3969–3976 trapped run_campaign alone); ValueError; argparse refuses both flags at time, id and qual (:4140–4144); m's argparse check uses --adjudication-file alone (m :5521–5528).
50. raw :49–55, MINOR-2. CONFIRMED: driver :4017–4023; 40 → 44 (cand :3948; driver :4064); the object {"x": 1} without --resume, the number 7 with it; the reviewer's probe used a non-empty dict and an int (A/review/probe_k03.py:28–29); a non-empty dict makes _paused_unadjudicated raise KeyError (stages.py:1595).
51. raw :56–66, MINOR-3. CONFIRMED: the three words (cand :667, :692, :697 → driver :671, :696, :701) now equal stages.py:1507, :1516, :1523–1524 and differ from m's stage (valence_core/m/stages.py:2096–2097, :2111, :2122); only the two suffixes remain; the words check (driver :3653–3684) reads run_campaign's source by inspect and ast; the clause is struck (driver :662).
52. raw :67–68, NOTE-1. CONFIRMED (items 19–20).
53. raw :69–78, NOTE-2. CONFIRMED: the equality (item 13); the three pieces are exactly those the review's candidate lacked (difflib against m); each is true of Q-F3: stages.ANALYZER_PATH is scripts/m_analyze.py (stages.py:63), whose C9(i) is the declared adjudication (scripts/m_analyze.py:2183); run_campaign passes the PI stop to the re-finish only when unrecorded (stages.py:1511) and _refinish_campaign declines the seat's adjudication and that stop (stages.py:1790); it raises NOT APPLIED after the re-finish (stages.py:1781–1801), exit 4 through run_stage. The help check reads m's source by ast as the constants check does (driver :1425–1432; :3471–3484); G01 and M03 fail it in round 2; the PIN says so (:257–260).
54. raw :79–80, NOTE-3. CONFIRMED: verbatim at driver :1041–1043; prior_gate reads the artifact at "qual" alone (stages.py:517–522); run_campaign re-checks it (stages.py:1484–1487).
55. raw :81–83, NOTE-4. CONFIRMED: driver :3401; the `qual` wiring's NOTE-7 disposition (results/raw/2026-11-12_mf3-qual-wiring_review.md:66–67); swap, drop and _lines_prefixed edit every such line (driver :3424–3439).
56. raw :84–96, NOTE-5. CONFIRMED: m :6280–6315 and :6365–6378 carry M2-2, O3-3 and F4-9 in that form; one thread, 20 s, the four calls (driver :3496–3520); the mirror's reads recorded (:3506–3509) and asserted empty (:3650); the RULING line's FIFO case (:3698); the O3-3 port in its own thread, 30 s (:4067–4097); the streams restored (:4076, :4089); round 2's first pass (item 73).
57. raw :97–98, NOTE-6. CONFIRMED: REFUSED_CMDS's derived line and the refused-subparser loop enter at acde2d8 (the `time` wiring), which also gave refusal() its present text; refusal() itself dates from cd9756e.
58. raw :99–100, NOTE-7. CONFIRMED (driver :109; stages.py:1717–1756).
59. raw :101–104, NOTE-8. IMPRECISE ("prints"), as item 30.
60. raw :105–110, the survivors' kill cases. CONFIRMED: P03 (driver :4024–4026), S03 (:3580–3582), L02 (:3696–3697), M03 and G01 (the help check); each is the reviewer's kill (raw :374, :377, :387, :411, :241).
61. raw :114–115, "a fresh sparse clone at HEAD `a89a4fa` (unchanged since the review), made with the brief's commands". NOT CHECKABLE: the clone is off-limits (HEAD is a89a4fa). The harness unchanged (A/review/harness.py and A/r2/work/harness.py share a sha256) and the import block (blocked_imported=[] in all 14 runs) are CONFIRMED.
62. raw :116–118, the generator "with two changes: its candidate's digest is the final bytes', and its list is cut to the mutants below". IMPRECISE: A/r2/work/gen_mutants_r2.py differs from A/review/gen_mutants.py by the digest (:10), a cut to ten round-1 mutants with W01 appended (:174–179), and a header comment; the list is cut and extended. Fix: "its list cut to round 1's ten, with W01 added". "Every anchor matched once, outside the self-test" is CONFIRMED (the generator asserts both; each of the 11 mutants is one one-line hunk of the final bytes, its digest the manifest's).
63. raw :119, W01. CONFIRMED (manifest; driver :696).
64. raw :120–121, sequential runs; each mutant copied over and the candidate restored, digest-checked. CONFIRMED: A/r2/work/run_one.sh refuses while a harness runs; run_batch.sh copies, restores and checks the digest; no "RESTORE FAILED" line.
65. raw :122–127, the scope. CONFIRMED.
66. raw :128, "The other 39 round-1 kills were not re-run." FAIL: round 1 killed 43 and round 2 re-ran three of them (X01, S02, T02), so 40 were not re-run.
67. raw :129–130, the edits since round 1. CONFIRMED by reading A/r2/fix_full.diff (whose hunks equal a fresh diff of A/r2/pre_fix.py against the final bytes): the one relaxed conjunct is the count (==1 → >=1, driver :3401); every other assertion change adds a case or a conjunct; round 1's mirror and help checks rested on refusal classes and on the constant, not on the changed words.
68. raw :131–132, the five values-check kills. CONFIRMED: in round 1's screens exactly C01, C03, C05, C07 and F01 FAIL the values check; each breaks a conjunct other than the count (driver :3395–3405, by reading).
69. raw :133, every round-1 anchor once in the final bytes, outside the self-test. CONFIRMED: all 50, read from A/review/gen_mutants.py by ast, occur once in the final bytes and outside _short…run_selftest.
70. raw :134–136, the baselines (20/20, 90/91, 234/235; the one FAIL the constants check). CONFIRMED.
71. raw :138–150, the table. CONFIRMED row by row: the defects are the manifest's; round 1 from A/review's results and raw :374–412; round 2 from round2_results.txt — K05 18/20, K03 12/13 ("harness: campaign part raised KeyError: -1" after 12 passes), S03 18/20, L02 19/20, M03 19/20, G01 19/20, P03 89/91, X01 88/91, S02 14/20 in 100 s, T02 16/20 in 63 s, W01 19/20, each by the checks named. S02's final-check reason is by reading: its tuple shows 5 loader reaches, one stage call and no escape, and the hung thread never leaves q_c's patches.
72. raw :152–157, the outcome, hygiene and timings. CONFIRMED: no "CLONE STATUS UNEXPECTED" or "RESTORE FAILED" line; 14 HARNESS END lines, each with blocked_imported=[]; the screens 31–32 s, K03 21, S02 100, T02 63, integration 127–128, full baseline 166. Note: the campaign baseline took 33 s, so "the campaign screens" reads as the mutants' alone.
73. raw :158–163, the first pass. CONFIRMED: A/r2/work/candidate_9aedead9.py (sha256 9aedead9…7324); all eleven killed (round2_results_9aedead9.txt); S02 printed 13 checks and no end line; the final bytes differ from it by the streams restore alone (driver :4076, :4087–4089; A/r2/apply_fixes_3.py).
74. raw :165–484, the reviewer's report. CONFIRMED intact (item 46).
75. The raw's Code parts carry no clock time, stamp or $ figure. CONFIRMED (durations in seconds only).

The self-test raw

76. st-raw :1, the header: the driver's sha256 in full; the main checkout; HEAD a89a4fa; exit status 0. CONFIRMED: A/r2/selftest_full_4.txt ends "EXIT=0"; its INVOCATION runs the main checkout's interpreter on a relative script path; HEAD at the run is consistent with the files, not independently checkable.
77. st-raw :1, "Local roots scrubbed (<repo>, <tmp>); the output below is otherwise unchanged", and the rest against A/r2/selftest_full_4.txt. IMPRECISE: lines 2–252 equal the original's lines 1–251 except lines 2, 131, 132, 135, 173, 174, 236 and 244, where a local root or a cut fragment of one became <repo> or <tmp> and nothing else changed; but the original's last line, the wrapper's "EXIT=0", is dropped (it is the header's "exit status 0"). The committed `qual` raw has the same form. Fix: say so in the header, or keep the line.
78. No local path, user name, session id or temp id survives. FAIL as the brief words it: no home, repository, scratch or per-user temporary path survives, nor the user's name, a session id, the per-user temporary folder's id or any five-character run of these; but five per-run temporary directory names (Python's "tmp" and eight characters) survive after "<tmp>/", at lines 135 (twice), 173, 174, 236 and 244. The committed `qual` raw keeps three such names the same way. If "temp id" covers them, replace them too.
79. st-raw :252, the last line "  235/235 mf3 selftest checks pass", one final newline; 235 [PASS] and no [FAIL] lines. CONFIRMED.

Tally: 79 items. CONFIRMED 60; IMPRECISE 10; FAIL 2; NOT CHECKABLE 7.

Not CONFIRMED:
- FAIL 66: raw :128, "39" (40).
- FAIL 78: st-raw, five per-run temporary directory names survive.
- IMPRECISE 5: entry :13, §5 item 2 cut unmarked.
- IMPRECISE 14: entry :42–46, "each in the words the stage uses".
- IMPRECISE 18: entry :54–58, the edit's naming incomplete.
- IMPRECISE 25: entry :85, "at both levels".
- IMPRECISE 27: entry :106–107, "as m's does … inside the traps".
- IMPRECISE 30: entry :120, "prints".
- IMPRECISE 49: raw :41–48, "m's form".
- IMPRECISE 59: raw :104, "prints".
- IMPRECISE 62: raw :116–118, "two changes".
- IMPRECISE 77: st-raw :1, the dropped EXIT=0 line.
- NOT CHECKABLE 32 (entry :126, @@VC@@), 33 (entry :127–128), 34 (entry :129, item 7), 43 (raw :26–28, the data/ commands), 47 (raw :34, the extraction from the transcript), 48 (raw :37), 61 (raw :114–115, the clone).

The transcript-scan claims (items 41–45) were checked against A/r2/scan_reviewer.py and A/r2/scan_reviewer.txt alone.

Departures: none. Every command was read-only; each content search carried ':!data/**' or named paths outside data/; nothing under data/ was opened but data/mf3/gates/Q-F3_G-PWR.json; A/r2/work/clone/ was not opened, listed or searched; no file was written.

----------------------------------------------------------------------------------------------------
## Code's dispositions

Every FAIL and IMPRECISE item is applied, and NOT CHECKABLE item 43 is answered. The edits are Code's, made after the
check; the pre-commit check asserts the facts they state.

- **FAIL 66** (the review raw, round 2's scope): "39" is corrected to 40. Round 1 killed 43, and X01, S02 and T02 are
  re-run in round 2.
- **FAIL 78** (the self-test raw): the five per-run temporary directory names (six occurrences) are replaced by `<run>`,
  and the header says so. The committed `qual` raw keeps three such names; it is not edited.
- **IMPRECISE 77** (the self-test raw's header): it now says the run wrapper's closing `EXIT=0` line is not kept below.
- **IMPRECISE 5** (the entry): the seat's §5 item 2 is quoted whole, its closing parenthesis included.
- **IMPRECISE 14** (the entry): the mirrored refusals are "each in the stage's own words, two with a declared suffix".
- **IMPRECISE 18** (the entry): `_lines_prefixed` and `_selftest_campaign` join the new names. An "Also changed" list
  names the module docstring's Q6 and INVOCATION sentences, `main`'s description and no-action line, `_selftest`'s
  wiring check and `_selftest_id`'s not-wired case.
- **IMPRECISE 25** (the entry): "`campaign --help` gives the flags and m's `camp_pauses` (read from m's source); the
  top-level `--help` gives `camp_pauses` too."
- **IMPRECISE 27** (the entry) **and 49** (the review raw's MINOR-1): the guard calls "take m's form (fresh roots, a stub
  factory), and run inside the traps". The disposition says that m's case is three calls outside any trap stack, and
  that the driver's six, inside it, extend it.
- **IMPRECISE 30** (the entry) **and 59** (the review raw's NOTE-8): the report's identity "carries" the backend
  identifier; no line prints it.
- **IMPRECISE 62** (the review raw, round 2): the generator has three changes: the digest, the list cut to round 1's ten
  mutants, and W01 added (with a header comment).
- **NOT CHECKABLE 43** (the review raw's three `data/` commands): the second pass that found them is kept beside the
  first, as `scan_reviewer_data.py` and its output in Code's scratch, and the header names it as a second pass.
- **Item 72's note** (the campaign baseline's 33 s): the timing line now separates the mutants' campaign screens from the
  baseline.
- **The other NOT CHECKABLE items stand as graded:**
  - 32: a placeholder;
  - 33: a future commit;
  - 34: the paste block's item 7, which the brief does not carry;
  - 47: the extraction from a transcript the checker may not open;
  - 48: "nothing ran on a model";
  - 61: the clone, which the checker may not open.
