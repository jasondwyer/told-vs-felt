# n step 4 — the smoke-pause STOP: the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over two drafts:
- the block (`results/raw/2026-11-18_n-step4-smoke-pause_code-to-design_STOP.md` as drafted), sha256 `4aa08919…2ed7`;
- its entry, sha256 `79806530…a6b4`.

**The checker's brief:**
- named the sources:
  - the box's output, the pod session's run record, the box's hashes and the laptop's;
  - the smoke's report, restricted to its key names, `pauses`, `end_state` and `stage_identity.fidelity_rule`;
  - the driver v2d and the box files, and the A100 output of 2026-11-16;
  - the n package's `runner.py`, `schema.py`, `primitive.py` and `sessions.py`;
  - PROPOSAL-n v0.2, WORKFLOW.md and RESULTS.md;
  - the seat's box and corpus answers of 2026-11-18, the box block of 2026-11-17 and the respawn raw;
  - the package digest rule;
- said that the coordinating session's words quoted in Q2 are not in the tree;
- quoted the list of record v2's items 1–5, verbatim;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3`, any write, and any search outside
  the repository, the HF cache and the scratch folders.

**The report** is in §3 below, extracted verbatim from the subagent's hand-back by `jq` (286 lines, sha256
`cf3bb49e…7830`). It writes `R/…` for the repository and `S/…` for Code's scratch.

**Totals:** 60 items — 46 CONFIRMED, 6 IMPRECISE, 2 FAIL, 6 NOT CHECKABLE — and 12 observations.

**The checker's departures,** as its report's DEPARTURES section states them. All were model-free, and nothing under
`data/mf3`, `data/*/ckpt` or `data/*/reports` was listed or read.
- One names-only `ls` whose argv carried a guard marker, through a glob in Code's scratch overlay. The checker then
  stopped running commands, which left items 55–57 unreached.
- One `git log --all --find-object` without list of record item 3's pathspec. It matched one blob id and named no
  commit. It is for the seat to class.
- Reads of Code's scratch outside the brief's list: two self-test outputs, their exit files, and names-only listings.

## 1. Dispositions

**The FAIL items, both applied:**
- **13** (block §4): "the first run, on any box, of the extension's reads and of R6's bridge" is now "the first
  run, on any box, of the extension's reads, and the first in which R6's bridge held (on the A100 it ran before the
  load and refused)". These are the checker's words.
- **43** (block Q1 (a)): the stage report carries no per-read fidelity block. The text now reads "with every read's
  fidelity value in hand from stdout (one line per read, rel to six decimals against TAU), beside the report's
  per-cell fidelity counters (trials, exceedances at TAU and at TAU/4)". These are the checker's words.

**The IMPRECISE items, all applied:**
- **12** (block §0; entry). The bridge's line now reads "R6's bridge, as retargeted, held on its first run". The
  block adds that on the A100 on 2026-11-16, R6's check against `641ee466f4553b6a` refused before the load, with CUDA
  unavailable (§4).
- **34** (block §6): "R5 declares the binomial's alpha, which does not matter here: at p0 = 0 one exceedance fires
  whatever alpha is (§3)". These are the checker's words.
- **42** (block Q1): "At 24 reads, the binomial can fire only at its end-of-run evaluation, and that is an open flag
  (§6)". These are the checker's words.
- **45** (block, the recommendation): "Every read's fid value reaches the seat in stdout before any ruling, without
  changing the rule; the distribution in nats, the in-band count and the comparison print on the resume". These are
  the checker's words.
- **46** (block, the recommendation): "It costs the run and, after the ruling, a resume, each with one load (the
  smoke's took 12,722 ms; its reads 973 and 712 ms)". These are the checker's words.
- **49** (block Q2): "no smoke of two or more reads (the box script runs `--smoke 2`) exits 0 on this box". These are
  the checker's words.

**The NOT CHECKABLE items:**
- **4** (the coordinating session's order, block :8–9 and Q2). Code checked the phrase "the box smoke first, then the
  driver's commit window, then the run of record from the commit" by a fixed-string search of this session's
  transcript, where the coordinating session's message holds it verbatim. No change.
- **35** (the `sed` departure). This is Code's own; it was disclosed to the coordinating session at the time, and it
  stands as declared. No change.
- **55** (nothing pushed). Code checked it: `origin/main` is at `fa96ccf`, HEAD is five commits past it, and HEAD is
  not an ancestor of `origin/main`. No change.
- **56** (m:271's form). m:271 sets the strip-and-redact form of a pre-VERDICTS read. The block's §1 applies it and
  finds nothing to strip: no pick, no contrast session, and no margin in stdout (item 21). No change.
- **57** (the form against WORKFLOW.md §4). Code read §4 against the block and found each part in place:
  - the path;
  - the header: the session, the PI date, "For the PI to route.", what ran with the lock and the driver's hash, and
    the sources read and not opened, by sha256;
  - the body: the short form, the reads, the declared items, Q1 and Q2 with their readings, "Not questions", and
    "Code adjudicates nothing";
  - the entry says "STOP for the seat's read".

  No change.
- **58** (what Code opened). This is Code's own conduct, and it stands as declared. No change.

**The observations:**
1. Applied: §2 now reads "The scrub found nothing to remove".
2. Applied: §4 quotes the run record's line 72 and adds that R6 had run on the A100 and refused.
3. No text change. The commit's gate admits the scratch folder's name only inside the run record's relative fragment
   on its line 14, which the report quotes. Line 89's fragment does not name the folder, and neither line holds a
   root, a user name or an id.
4. Applied: the row is now "B2's row of n §0.10's table (:47)".
5. Applied: `d5d08fa`'s own words, "A, B and C exact at 0.0", now stand beside the seat's criterion.
6. Applied: the Q1 bullet now separates §5.5's measure, the label check's, from the within-box rate that the fidelity
   rule binds.
7. Applied with item 12.
8. Applied: the fidelity rule is quoted whole, verbatim from `jq -c`.
9. Applied: the crop line now reads "after each label's continuation (a one-token label needs none)".
10. Applied in two places:
    - §8 opens with "Code's reading of what needs no ruling; the seat may take any of them up";
    - §6's departures line now says where they happened, "Both happened on the laptop, before the box run", instead
      of judging their effect.
11. Applied: the entry names the coordinating session's order.
12. Not applied, as it does not hold. The checked drafts end with a newline: `tail -c 3 | od -c` shows a final `\n`,
    and `wc -l` (254 and 39) agrees with `awk`'s record count. The entry has since gained a final blank line, for its
    place in RESULTS.md; that is Code's change, not the observation's.

## 2. The edits after the check, checked by tool

- **The diffs.** `diff -U0` of each final text against its checked draft holds only the dispositions above, and Code
  read each diff in full.
  - The block has 15 hunks: items 12, 13 (with observation 2), 34, 42, 43, 45 and 46 (one hunk), and 49; and
    observations 1, 4, 5, 6, 8, 9, and 10 (two hunks).
  - The entry has 4 hunks: item 12, observation 11, the values-check and departures lines, and the final blank line.
- **The checks on the final block:**
  - Every verbatim quote is found, joined across wrapped lines, in the block and in its source: 25 of 25. The count
    includes the four quotes the edits added: `d5d08fa`'s words, the fidelity rule and the pause record by `jq -c`,
    and the run record's line 72.
  - The 17-line block equals the output's lines 47–63, with the progress bar abbreviated.
  - The scrub scan is clean.
- **The finals:** the block, sha256 `84fb8b3b…03a5`, 265 lines; the entry, `a621da69…d74c`, 52 lines.
- **The commit's gate** re-runs these checks on the staged blobs. It also rebuilds RESULTS.md from HEAD with the entry
  and compares both the working file and the staged blob.

## 3. The report as returned

```text
Blind values-check of T1 = S/step4b/stop_v2.md (sha256 4aa08919094e1c0b2f523882d56503b467011335c32d201cd9bbf5bac77f2ed7) and T2 = S/step4b/entry_stop.md (sha256 79806530ca84862371344028a437c274b9c0d4f2ae7319e54c47930a618ea6b4), checked against the sources the brief names. R is at HEAD d5d08fa (branch main). Date: 2026-11-18. I noticed one guard-marker departure of my own (see Commands) and then stopped running commands, as the brief requires. The few items I had not reached are marked "NOT CHECKABLE (not reached)". Line numbers are each file's own: T1 has 255 lines as read and T2 has 40.

ITEMS

1. T1 :5–6, T2 :4–5. The pod session ran it on pod emw1e4embiwe9b, the H100 SXM of the BACKEND entry d5d08fa. CONFIRMED: box out :55 (the pod); run record :1–5; d5d08fa's commit subject ("pod emw1e4embiwe9b, an H100 SXM in US-CA-2").

2. T1 :6–7, T2 :8. No lock was in force; LOCK-n v0.1 is to name this backend (box answers §2 item 7) and is not placed. CONFIRMED: there is no LOCK-n file at R's root or in git ls-files (only LOCK-g, -h, -m-F0, -m-F3 and three LOCK-p-…); box answers :30; v2d :551 (lock_sha256 None at backend-ext).

3. T1 :8, :254; T2 :6, :38. Driver v2d is 18f19b8e…4f5c and uncommitted. CONFIRMED: sha256 of S/step4b/n_sessions.v2d.py; box out :50. Its git blob differs from HEAD:scripts/n_sessions.py, which the working tree equals, and git log --all --find-object on v2d's blob names no commit.

4. T1 :8–9, :222–223; T2 :6–7. The order (box smoke, then the driver's commit [window], then the run of record from the commit) is attributed to the coordinating session. NOT CHECKABLE: the quote is not in the tree, per the brief. It is consistent with box answers §2 item 5 (:28, commit before step 4's run of record) and §3.3 (:40, smoke then the driver's commit, on the A100 path).

5. T1 :10, T2 :8. Package f927608c…3c03, HEAD d5d08fa's valence_core/n/, committed at b523f6a. CONFIRMED:
   - the brief's digest rule over R/valence_core/n/*.py gives f927608c…3c03;
   - git status --porcelain -- valence_core/n is empty, and git diff --name-only b523f6a d5d08fa -- valence_core/n is empty;
   - b523f6a is the last commit to touch valence_core/n, and its subject records the move to f927608c…3c03;
   - box out :34.

6. T1 :11–12, :35–39; T2 :9–10. Steps 0–3 held (the copy at d5d08fa with exactly the driver changed; manifest 23/23; self-test 344/344; the package and 11 closure lines equal to the laptop's by diff), then a two-read smoke. CONFIRMED:
   - box out :1–3, :5–27 (23 OK lines), :31–32, :34–46 (1 package line and 11 imported lines);
   - S/step4b/box/out/hashes.txt and smoke-identity.txt each show no difference from S/iv/out/hashes_run4.txt by diff, and all three hash to 93783db0…7b36;
   - bext_box_v2.sh :70 runs --smoke 2.

7. T1 :15–28, :247–253. The sha256s. CONFIRMED: each was computed and abbreviated by cut.
   - bext_box_v2_out.txt 202e6bd7…a872; bext2_box_run.txt 7933fb33…2590; hashes.txt 93783db0…7b36; smoke-report.json 206264c8…bb9a; v2d 18f19b8e…4f5c.
   - At b523f6a (git show) and in the working tree: runner.py 69d73d77…d896, schema.py 0ea39600…0db6, primitive.py 7e7bb0a0…0b0c.
   - PROPOSAL-n-bk-reconciliation-v0_2.md 30a3d0f5…04f4; box answers f46815fb…6d5a; corpus answers 5843a9bd…7165; the box block of 2026-11-17 80b7cacf…2fc8; the A100 output e2d9774c…831f; WORKFLOW.md e7195706…b061.
   - bext_drafts_v2.tar f0bc9dac…3b0a; bext_manifest_v2.txt 18b4c619…c986; bext_box_v2.sh 2bde09d9…af51.
   - Every committed source is clean in a scoped git status --porcelain.

8. T1 :26–27. The A100 check's output of 2026-11-16, its lines 43–51, is in Code's scratch, uncommitted. CONFIRMED:
   - S/step4/box/out/bext_box_out.txt has 51 lines, and :43–51 are its step 4;
   - its :2 records HEAD 977b78b, and no commit in 83a50a0..HEAD (977b78b, fa96ccf, e48c7d0, 26cf7d2, b4522ae, b523f6a, d5d08fa) adds such a file outside data/ (git log --name-only);
   - the date matches the box block §1 item 1 (:57).

9. T1 :25, :136, :177–181; T2 :23. The BUILD entry (83a50a0) lists the fidelity binomial among its open flags; both quotes are verbatim. CONFIRMED:
   - RESULTS.md :624 is the entry's head ("n package — BUILD", 2026-11-16);
   - :784–785 hold "Each is Code's interim reading. By the PI's routing of 2026-11-16 (N.9), the build proceeds on them.", exact once the wrapped lines are joined;
   - :791 reads "Open:", and :797–798 hold the flag, exact;
   - git blame -s -L 784,798 RESULTS.md attributes every line to 83a50a05.

10. T1 :182. "None of the seat's answers since the BUILD names it." CONFIRMED:
    - R/results/raw holds six *design-to-code* raws dated 2026-11-16 or later. Four were committed before 83a50a0, by git merge-base --is-ancestor: n-build, n-ganl and p-verdicts-counters at 52b2c97, and p-verdicts-decisions at 18102d0. Two came after it: the box and corpus answers, both at 26cf7d2.
    - I searched all six (case-insensitive) for binomial, end-of-run, end of run, run's end, cadence, fidelity, p0 and TAU.
    - The two later raws have no hit.
    - Of the earlier raws, the n-build answers name "the fidelity binomial" only in the pause kinds' precedence (:50) and accept "the fidelity rel and its scale" (:48); n-ganl :48 names "the TAU/4 row's handling". Neither touches the batches, the cadence or the end-of-run evaluation.
    - All other raws committed since the BUILD are Code's or the pod session's.

11. T1 :41–42, T2 :12–13. R6's bridge held, with n's identifier 8264f719efd347a9 under the 4,096-token window and the characterization's 4ed3f2c70fe8afbf under the default window. CONFIRMED: box out :55; v2d :420 (CHARACTERIZED_IDENTIFIER); v2d :855–857 and :884–885 (refusals, not taken); v2d :888–889 (the line's form); d5d08fa's subject.

12. T1 :41 and T2 :12, "on its first run on hardware". IMPRECISE.
    - Evidence: R6's check ran on the A100 pod on 2026-11-16 and refused before the load. See A100 output :48 ("… (R6)") and box block :59–60 ("The stage refused before the load, at R6's check"). T1 :149 and T2 :18–19 say so themselves.
    - It is the first run of R6 as retargeted (box answers §2 item 4) and the first time R6 held.
    - Fix, T1 :41 (and T2 :12 likewise): "R6's bridge, as retargeted, held on its first run (on the A100 on 2026-11-16, R6's check against 641ee466f4553b6a refused before the load, CUDA unavailable): n's identifier …".

13. T1 :156, "The smoke above is the first run, on any box, of the extension's reads and of R6's bridge." FAIL for "and of R6's bridge"; the evidence is item 12's. The part about the reads holds (item 17).
    - Fix: "The smoke above is the first run, on any box, of the extension's reads, and the first in which R6's bridge held (on the A100 it ran before the load and refused)."

14. T1 :43–47, :203; T2 :14–17. The smoke's values: G-VER PASS; weights loaded; read 0 fid 0.014660 ≤ TAU (≈ 0.82 × TAU); read 1 fid 0.086070 > TAU (0.0178835444; ≈ 4.8 × TAU); the end-of-run evaluation fired under p0 = 0/2400, G-DATA (vi)'s figure; pause p01; no distribution and no comparison. CONFIRMED:
    - box out :51–60;
    - by awk, 0.014660/0.0178835444 = 0.8197 and 0.086070/0.0178835444 = 4.8128;
    - schema.py :248 has TAU = 0.017883544377937845;
    - jq .pauses shows p01, fidelity-binomial, read_id and launch_index null, k 1 of n 2, p0 0/2400; jq .end_state is "PAUSE";
    - v2d :895–897;
    - RESULTS.md :10828 (G-DATA (vi): "p0 = 0 / 2,400").

15. T1 :44–45 ("BK run 0", "BK run 5") and :94–95 (s= is bk_run, followed by arm, direction and dose). CONFIRMED:
    - runner.py :450 prints "read {launch_index} s={s.bk_run} {arm} {direction_id} {dose_label}";
    - sessions.py :65–66 and :134: bk_run is the session's index in the set;
    - box out :56–57. "The dose" field is the dose label.

16. T1 :48, T2 :17. The box script's last line reads FAIL, on the smoke's exit 1. CONFIRMED: box out :63 (selftest 0, hashes 0, smoke 1, identity 0); bext_box_v2.sh :92–95; bext_box_v2.exit holds 1.

17. T1 :49, :62, :148–153; T2 :18–19. This is the extension's first run with reads on any box. The A100's v1 smoke (pod m43y3deb1gq3rp) refused before the load at R6, with CUDA unavailable (error 802): no G-VER, no load, no read. The box block's §1 item 1, committed at e48c7d0, reports it, and T1 quotes the output's line 48 verbatim. CONFIRMED:
    - A100 output :44 (error 802), :48, no G-VER line, :50 ("no smoke report"), :51 ("bext box FAIL", no "v2");
    - box block :57–61;
    - git show --name-only e48c7d0 lists the block;
    - the pod id is in box answers :30 and in e48c7d0's subject;
    - :48 equals T1 :152–153 (joined) character for character. I compared this by reading, not by tool.

18. T1 :154. The A100 has run nothing for n since. CONFIRMED as far as the committed record goes:
    - box block :68–70 (802 again after the restart; stopped 2026-11-16);
    - e48c7d0's subject (its start was refused at every attempt on 2026-11-17);
    - 26cf7d2's subject (the A100's retries ended at the word);
    - no later entry records an A100 run.

19. T1 :157. No other measurement of n's cached-versus-fresh discordance on the model's weights exists, on any GPU. CONFIRMED as far as the committed record goes:
    - the A100 loaded nothing (item 17);
    - G-DATA was model-free (RESULTS.md :10769);
    - the self-tests' HF cases use hftiny, with "no weights" (v2d :6–9).
    - Absence beyond the record cannot be checked.

20. T1 :57–58, the n :130 quote. CONFIRMED: it is an exact substring of the proposal's :130 (awk index 191).

21. T1 :59–60. No pick and no contrast session; nothing redacted or stripped. CONFIRMED: the plan is N1-V d = 0 reads only (v2d :447–451), and stdout prints fid, never a margin (runner.py :8–10, :484–486; box out :56–57).

22. T1 :68, :71–72, :74–92. The block is lines 47–63 verbatim, except the bracketed progress bar, which carries carriage returns. CONFIRMED: diff of T1 :75–91 against box out :47–63 reports one difference, T1 :81 against out :53, and od -c shows two CRs in out :53.

23. T1 :69–70, and the brief's scrub check of both files to be committed. CONFIRMED for bext_box_v2_out.txt and bext2_box_run.txt:
    - /usr/bin/grep finds none of the following in either file: home-directory and temporary-folder path prefixes (macOS and Linux forms) or ~/; the user name (either part, any case); claude-<digits>; the scratch session's id; any UUID-form id; local_; a dotted-quad IPv4 form; a port.
    - The port-like hits are CUBLAS_WORKSPACE_CONFIG's ":4096:8", the progress bar's "00:00", the words "report" and "imported", and the run record's own statements that it holds no address or port (:3–4, :91).
    - The run record does name two relative scratch fragments (observation 3).

24. T1 :99–108, what fid measures. CONFIRMED:
    - primitive.py :219–221 is the cached path (prefill, then continue_label for each label);
    - primitive.py :239–240 is the fresh path (backend.full for each label, over the same ids);
    - primitive.py :21–22 holds the docstring quote, exact;
    - schema.py :529–536 is fidelity_numbers, whose docstring says "… exactly as both sides compute them"; rel = |margin − fresh_margin| / max(|logprob_S|, |logprob_U|) of the cached read (:91–94), and exceeds_tau = rel > TAU;
    - runner.py :484–486 prints rel as fid;
    - v2d :79 (R4, nothing injected) and :450–451 (dose 0.0).

25. T1 :109–121 and :175. The n §2.1 (:77) and B2-row (:47) quotes are verbatim, and so is p0 "declared in LOCK v0.1 …". CONFIRMED: each is an exact substring once the wrapped lines are joined (awk index 1453 in :77 and 8 in :47). :77 is §2.1, under the §2 heading at :75.

26. T1 :123–124, the fidelity_rule as the report holds it. CONFIRMED: jq .stage_identity.fidelity_rule gives tau 0.017883544377937845, p0_count 0, p0_n 2400, cadence 160 and the quoted sample_rule. It also holds sample_key "n-fid|{s}", which T1 does not list.

27. T1 :125, :176. The self-test pins the rule; with no lock, G-DATA (vi)'s 0 of 2,400 is carried directly. CONFIRMED:
    - v2d :557–558 sets the identity's fidelity_rule;
    - at v2d :965–971 the check's name holds the quote, and the check compares the whole fidelity_rule;
    - RESULTS.md :10828 and :10920 record the figure.

28. T1 :127–128, R5 verbatim. CONFIRMED: v2d :82, with its closing ";" dropped.

29. T1 :129–135. The runner's two PIN quotes; cadence 160 against 24 reads; the fire at the end-of-run evaluation. CONFIRMED:
    - runner.py :38–41: both quotes are exact once joined;
    - runner.py :175, :206, :216: a cadence evaluation needs 160 reads in the batch;
    - runner.py :496–509: the end-of-run evaluation, whose printed line equals box out :58;
    - runner.py :77–78: binom_tail(k ≥ 1, n, 0) = 0, which is at or below any alpha;
    - v2d :397: BEXT_N = 24.

30. T1 :137–139, the pause record verbatim and end_state. CONFIRMED: diff of T1 :138 (backticks and the final period stripped) against jq -c '.pauses' shows no difference; jq .end_state is "PAUSE".

31. T1 :140–144, what waits, and the docstring quote. CONFIRMED: v2d :895–911; the quote is exact at v2d :69–70.

32. T1 :159–167. §5.5 verbatim; it was written for ADDENDUM-n1 §2's check, and box answers §2 item 4 cite it so. CONFIRMED: corpus answers :69 (exact substring, awk index 245; its heading is "ADDENDUM-n1 §2's check, one figure added"); box answers :27.

33. T1 :171, :173. R1–R6 stand as the docstring states them, and R6 was retargeted by §2 item 4. CONFIRMED: v2d :71–89; box answers :27 ("R6 is retargeted … it is not dropped").

34. T1 :172, "R5 is the reading under which one exceedance fires (§3)." IMPRECISE.
    - R5 declares the alpha and itself says that at p0 = 0 "any exceedance fires whatever alpha is".
    - The single exceedance fires because p0 = 0 (G-DATA (vi)'s figure, carried before the lock) at the end-of-run evaluation (runner.py :38–41, :77–78).
    - Fix: "R5 declares the binomial's alpha, which does not matter here: at p0 = 0 one exceedance fires whatever alpha is (§3)."

35. T1 :185–186, the first departure: one sed call carried the model folder's name, and it was disclosed at the time. NOT CHECKABLE: no record of it is in the sources.

36. T1 :187–189, the second departure: v2d's laptop self-test gave 332/333, then 333/333 from the completed overlay. CONFIRMED for the figures:
    - S/step4b/out/selftest_v2d.txt reads "332/333" and its exit file holds 1. Its one FAIL is the check "the characterization's literals are its committed record's …", which reads the committed artifact and raw (v2d :421–425).
    - selftest_v2d_2.txt reads "333/333", exit 0.
    - These files are outside the brief's list; I read them in S.
    - Not checkable: the window grant, the delta review, and that the overlay lacked the two files at the time (it holds both now). The same goes for "None of them touched the run" (:184).

37. T1 :196–197. The smoke's two reads are the run's first two. CONFIRMED:
    - v2d :864 runs bext_plan(ss)[:smoke];
    - v2d :438–451 builds R1's 24 sessions in the set's order, launch indices 0..23;
    - runner.py :363–364 and :439 launch in plan order;
    - the pause's binomial covers launch indices 0 to 1.

38. T1 :197–198. The respawn (ii) quote, and PASS at d5d08fa. CONFIRMED: the quote is exact at box answers :26 (§2 item 3). The PASS rests on d5d08fa's subject ("(ii) BACKEND PASS on the box's own determinism (A, B and C exact at 0.0)"). I did not open d5d08fa's entry or its raw. See observation 5.

39. T1 :198–199. If read 1 repeats, the run of record pauses at its end. CONFIRMED by reading the code: runner.py :496–509 and :217, with p0 = 0.

40. T1 :200–201, the n §3 G-ACQ (:109) quote. CONFIRMED: exact (awk index 285), and :109 lies in §3 (headings at :105 and :124).

41. T1 :202. p0 = 0 is BK's rate, and §5.5 expects this box's numerics to differ. CONFIRMED: RESULTS.md :10828 and :10920 give BK's per-read rate at TAU on the 160 sessions, from BK's reads; corpus answers :69. See observation 6.

42. T1 :204, "At 24 reads, only the end-of-run evaluation can fire". IMPRECISE.
    - It is true of the binomial's evaluations, but the rendering and non-finite monitors can still pause any read (runner.py :182–184, :455–460; schema.py :1085).
    - Fix: "At 24 reads, the binomial can fire only at its end-of-run evaluation, and that is an open flag (§6)."

43. T1 :208–209, "… with every read's fidelity value in hand: one line per read in stdout, and the fidelity blocks in the report." FAIL for "the fidelity blocks in the report".
    - n-report-v1 carries no per-read fidelity block.
    - Its fields are schema, stage_identity, stage_identity_sha256, read_plan_sha256, end_state, per_arm, cells (per file: json_sha256, capture_sha256, records), pauses, binomial_state, stop, cap and counters.
    - Its counters' fidelity entry is keyed by 'arm|dose' and holds only {trials, exceed_tau, exceed_tau4} (schema.py :1103–1120, :1165; runner.py :316–352). The smoke report's keys are exactly these fields.
    - Each read's fidelity block is in its record, in the stage's cell. For a run of record that cell is under data/n/ckpt/backend-ext (v2d :402), which list-of-record item 2 closes.
    - Fix: "… with every read's fidelity value in hand from stdout (one line per read, rel to six decimals against TAU), beside the report's per-cell fidelity counters (trials, exceedances at TAU and at TAU/4)."
    - T2 :26–27 is correct as worded.

44. T1 :209–210. A resume with the ruling completes, skip-only, and prints the distribution, the in-band count and the comparison. CONFIRMED by reading the code:
    - runner.py :391–401: the ruling adjudicates p01;
    - runner.py :430–433, :439–441: reads already on disk are skipped;
    - runner.py :496–505: the end-of-run evaluation reproduces the batch and clears it;
    - v2d :894–911;
    - the runner's self-test at :859–879 covers this case.

45. T1 :216, "The full distribution reaches the seat before any ruling, without changing the rule." IMPRECISE.
    - Under (a), the driver's distribution (discordance: |margin − fresh_margin| in nats, rel median and max, per-label differences) prints only on COMPLETE, after the resume with the ruling (v2d :895–902; T1's own :141–142 and :209–210).
    - Before the ruling, the seat has only each read's rel against TAU, from stdout.
    - Fix: "Every read's fid value reaches the seat in stdout before any ruling, without changing the rule; the distribution in nats, the in-band count and the comparison print on the resume."

46. T1 :217, "It costs one box session; the smoke's reads took 973 and 712 ms each."
    - The milliseconds are CONFIRMED: box out :56–57, and duration_ms covers both paths (schema.py :370; primitive.py :284–285).
    - "One box session" is IMPRECISE. (a) as written needs two invocations: the run and, after the ruling, the resume. Each runs G-VER and loads the weights before runner.run (v2d :874–882); the smoke's load took 12,722 ms (box out :55).
    - Fix: "It costs the run and, after the ruling, a resume, each with one load (the smoke's took 12,722 ms; its reads 973 and 712 ms)."

47. T1 :223. The box script counts a smoke exit 0 as its pass. CONFIRMED: bext_box_v2.sh :19 and :92–95. Its PASS needs the self-test's, the hashes', the smoke's and the identity's exit 0.

48. T1 :224–225. The smoke exited 1 on the stage's own pause; every step before the monitor ran as expected; its identity lines equal the laptop's. CONFIRMED: box out :58–62; v2d :895–897; run record :57–78; item 6.

49. T1 :226–227, "if the box repeats, no smoke of this stage exits 0 on this box." IMPRECISE.
    - It is true of every smoke of two or more reads, since each includes read 1 (s=5; v2d :864).
    - A --smoke 1, which the driver admits (v2d :809–810), reads only read 0 (fid ≤ TAU). Its end-of-run evaluation does not fire (k = 0 gives binom_tail 1.0 > alpha; runner.py :75–76, :217), so it would go on to the comparison and exit 0.
    - Fix: "no smoke of two or more reads (the box script runs --smoke 2) exits 0 on this box."

50. T1 :228–229, the box answers §2 item 5 quote. CONFIRMED: :28, exact.

51. T1 :233–235. The bridge held; 333/333 on the laptop and 344/344 on the box; the package and closure are equal by diff. CONFIRMED: items 6, 11 and 36.

52. T1 :236–238, the crop notice. CONFIRMED:
    - primitive.py :341 is cache.crop(n), and :342–343 is the assert;
    - git grep 'crop(' over valence_core and scripts finds only :329 (an error message) and :341;
    - nothing refused (box out :55–59).
    - See observation 9.

53. T1 :240–241, the pod session's copy. CONFIRMED: run record :93–97.

54. T1 :245–253. The record's names, line counts (63, 106, 23, 95), "one member, v2d" and "unedited". CONFIRMED:
    - the line counts by wc -l, and the hashes as in item 7;
    - T1 :245 and T2 :3 name the same raw;
    - "one member, v2d" rests on run record :15–17 and :40–41 (I did not list the tar);
    - "unedited" rests on run record :4.

55. T1 :254 and T2 :38, nothing pushed. NOT CHECKABLE (not reached). d5d08fa's subject says "Not pushed".

56. T1 :53, "(m:271's form)". NOT CHECKABLE (not reached).

57. T1's form against WORKFLOW.md §4. NOT CHECKABLE (not reached). Only WORKFLOW.md's hash was checked (item 7).

58. T1 :19 and :30–31, what Code opened and what it left unopened (from the report only the key names, pauses, end_state and fidelity_rule; not the smoke's root, data/mf3, ckpt or reports). NOT CHECKABLE: this is Code's own conduct. The pod session's side agrees (run record :85–86, :91–92).

59. T2 against T1. CONFIRMED: every figure, hash, identifier, commit and question in T2 equals T1's. T2 :12 carries item 12's imprecision, and T2 drops the order's attribution (observations 7 and 11).

60. T2 :30: the smoke loaded the weights once, on the box, and nothing ran on a model on the laptop. CONFIRMED for the box: box out :53–55 shows one load. The laptop half agrees with v2d :6–9 (the HF cases are skipped off the box) and is otherwise not checkable.

ADJUDICATION. Nothing in T1 or T2 decides the fired pause p01, the box script's FAIL or a departure. See T1 :48 ("reported here, not decided"), :51, :169 and :216 ("not a ruling"), and T2 :20 and :28. Observation 10 covers the borderline classifications.

OBSERVATIONS

1. T1 :68 says "scrubbed", but nothing was found or removed. "Scanned" would match :69–70 and §9's "unedited".

2. The run record, which will be committed unedited, has the pod session's own "R6's bridge held on hardware, its first run there" (:72). That is item 12's reading, and the seat will read it beside T1's.

3. Run record :14 ("n-build's scratchpad/step4b/box/") and :89 ("n-build's step4b/box/out/") name relative fragments of Code's scratch path. They hold no absolute path, user name or session id. Whether the pre-commit screen admits them is the committing session's call.

4. T1 :116, "B2's row of n's table": the table is n §0.10's dispositions of Code's STOP on v0.1 (proposal :40 and after). Naming §0.10 would help the seat find it.

5. T1 :197–198 quotes the seat's pass criterion (box answers §2 item 3) as what respawn (ii) "found". d5d08fa's own words for the result are "A, B and C exact at 0.0".

6. T1 :202: §5.5 is about the vanilla forward's values against BK's published d = 0 values (the label check's tolerance). It is not about the within-box cached-versus-fresh rate that the fidelity rule binds. T1 §5 :166–167 draws that line, but the Q1 bullet read alone could suggest §5.5 covers the fidelity rate.

7. As worded, T2 :12 ("first run on hardware") contradicts T2 :18–19 ("refused before the load, at R6"). The same pair appears in T1 at :41 and :149.

8. T1 :123–124 lists four of the fidelity_rule's six fields (sample_key "n-fid|{s}" is missing) but reads as the whole rule.

9. T1 :237, "after each label": a one-token label returns before any continuation or crop (primitive.py :337–338).

10. T1 §8 ("Not questions") classes three matters on Code's reading alone: R6 and the re-pin, the crop notice, and the pod session's first copy script. T1 §6 :184 also judges that the departures did not touch the run. None of these decides a fired gate, the pause or a departure's standing, but the seat may want them as declared items.

11. T2 :6–7 drops T1's attribution of the order to the coordinating session.

12. Neither draft ends with a newline: wc -l gives 254 and 39, against 255 and 40 lines.

TOTALS: CONFIRMED 46; IMPRECISE 6 (items 12, 34, 42, 45, 46, 49); FAIL 2 (items 13, 43); NOT CHECKABLE 6 (items 4, 35, 55, 56, 57, 58). 60 items in all.

COMMANDS (classes)
- shasum -a 256, with cut for abbreviations, on files in S and R. git show b523f6a:<path> | shasum for runner, schema, primitive and sessions. The brief's package digest loop over R/valence_core/n/*.py (ls, wc -c, cat, shasum).
- wc -l on files in S and R. tail -c 1 | od -c and sed -n | od -c in S. awk on files in S and R (line selection, substring-index checks, ratio arithmetic). tr, fold, cut and rev in pipelines.
- sed -n on files in S and R, none of them under data/.
- diff with sed process substitution: T1's block against the box output; hashes.txt and smoke-identity.txt against the laptop's hashes; T1's pause record against jq's output.
- /usr/bin/grep (-n, -i, -E, -F) on single files in S and R. No recursive grep.
- git grep -n 'crop(' -- valence_core scripts ':!data/**'.
- jq on smoke-report.json: 'keys', -c '.pauses', '.end_state', '.stage_identity.fidelity_rule', '.stage_identity | keys'. Nothing else from it.
- git read commands:
  - rev-parse HEAD and HEAD:scripts/n_sessions.py; hash-object on the v2d draft and the working-tree driver;
  - status --porcelain, scoped to named paths only; diff --name-only b523f6a d5d08fa -- valence_core/n;
  - log with --format of ids, short dates and subjects, scoped to paths; log --name-only 83a50a0..HEAD -- . ':!data/**'; log --diff-filter=A on six named raws;
  - show --name-only for 83a50a0 and e48c7d0; merge-base --is-ancestor; blame -s -L 784,798 RESULTS.md;
  - ls-files piped to /usr/bin/grep; log --all --find-object=<v2d's blob id>.
- ls, names only, in S (step4b and its subfolders) and in R (the root and results/raw).
- cat of S's exit files and self-test outputs.
- The Read tool on T1, T2, the box output, the run record, the A100 output, parts of v2d, bext_box_v2.sh, bext_manifest_v2.txt, the box answers and parts of runner.py.

No Python, no model, no network, no ssh, no edits, no commits. Nothing under data/mf3, data/*/ckpt or data/*/reports was listed or read.

DEPARTURES
1. Guard marker in argv. From S/step4b I ran `for d in overlay/data/*; do echo "[$d]"; ls "$d"; done`. The glob expanded to the overlay's model-family data folder, so one names-only `ls` call carried a guard word in its argv. It printed two file names, determinism_base_h100-sxm.json and manifest.json. The call was read-only and model-free, in Code's scratch overlay, outside any ckpt or reports folder. When I noticed it I stopped running commands, as the brief requires. Not reached as a result: items 55–57, d5d08fa's entry and raw (item 38), and a listing of the tar's members (item 54).
2. For the seat to class: git log --all --find-object=<v2d's blob id> ran without the ckpt/reports exclusion pathspec. It matches one exact blob id, not text, and it named no commit.
3. I read sources outside the brief's list, all in S: S/step4b/out/selftest_v2d.txt, selftest_v2d_2.txt and their exit files (item 36), plus names-only listings of S/step4b/chk, out, overlay, tmp5 and tmp6.
```
