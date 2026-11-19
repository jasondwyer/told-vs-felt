# n — G-VEC's BUILD texts: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over four drafts, before draft 2's self-test had run:
- T1, the entry (`RESULTS.md`, the Log's head), sha256 `91575200…44be`;
- T2, the spec raw, `177d6191…db53`;
- T3, the self-test raw, built before run 2, `8fb07878…1346`;
- T4, the review raw's head and dispositions, `47185de1…3ffd`.
Run 2's result (its placeholders in T1, T3 and T4) was marked not to be checked.

**The checker's brief** (`d74cdad3…e5ee`, 90 lines, given to the checker as a file, with its sha256 to verify):
- named the change's files (HEAD's four, the five final drafts, the five reviewed drafts), the new `.gitignore`, and
  the `git diff --no-index` form;
- named the sources:
  - in the repository: PROPOSAL-n v0.2, ADDENDUM-n1, the seat's corpus-adoption answers, `RESULTS.md`, HEAD's
    `valence_core/` code, `scripts/box_e0_corpus.py`, `scripts/box_a3_extract.py`, `scripts/n_analyze.py`,
    `.gitignore`, the corpus and the ids of record, BK's `analysis.json` (its member selected by prefix only), and git
    history;
  - in Code's scratch, by name only: the drafts and reviewed drafts, run 1's output and exit file, the review's report
    and brief, the survey's report and brief, the two verbatim messages, the coordinating session's four G-VEC
    messages verbatim, and the shell form of the package digest, which it could run on the repository's package and on
    the self-test overlay's;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, that a glob is expanded and read before it is looped over, and the `rev-parse` form for a
  tracked-and-clean check;
- barred any interpreter, any write, any network and any guard marker in an argv; anything under `data/mf3`; any
  content read, listing, size or time of a ckpt or reports file; and, in Code's scratch, anything but the named files,
  its brief itself excepted.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (226 lines, sha256
`2dff8c72…33e0`). It names no local path.

**Totals:** 114 items: 89 CONFIRMED, 15 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE; and 11 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **The IMPRECISE items**, each applied, in the checker's words or near them:
  - 16 (T1, extract's imports): "which imports, beyond the standard library, only numpy and `adapters.base`";
  - 24 (T1) and 91 (T4), where F1's fix sits: F1's admit lines are the BUILD commit's `.gitignore`, and every other
    finding is in draft 2's bytes;
  - 38 (T1) and 95 (T4), which sha16s are the Injection's: every direction's; U's sha16 and A3's freeze_sha stay
    `sha16_arr` digests;
  - 43 (T1) and 109 (T4), the departures from G1–G14: G12's smoke form and G14's ‖h̄₊ − h̄₋‖ added to the entry's list,
    in the entry alone (observation 10);
  - 45 (T1) and 111 (T4): O5, O6, O7 and O9 "as Code listed them, on the coordinating session's word";
  - 53 (T1), the survey's departures: "printing raw names, a count, or nothing";
  - 62 (T2): "with a citation for its claims (file:line, or the commit or search for a claim of absence), as its brief
    asked";
  - 71 (T3): hftiny's skip by the driver's docstring, the vanilla score's by its own branch in the driver;
  - 72 (T3): 160 files, HEAD's 159 on those paths with four replaced and `valence_core/n/gvec.py` added;
  - 79 (T4): `5ef276df…d1e7`;
  - 108 (T4): the site rule's two readings declared in G2, and the tie rule also in the departures.
- **The NOT CHECKABLE items** (1, 4, 14, 18, 20, 22, 46, 52, 55, 73) stand: the PI's calendar, Code's own acts, the
  plans for the launch files, files not yet made, and run 2, pending when the check ran.
- **The observations:**
  1. Applied: the entry's review bullet adds what is declared (O2, O3), what is in this entry (O5, O6, O7, O9) and
     what needs no action (O4).
  2. Applied: the entry says the same computation over HEAD's files reproduces `f09898ee…b8f9`, and that neither
     digest has yet been printed by the package's own `hashes`.
  3. Applied: `.gitignore`'s sha256 and its thirteen lines' composition in the entry.
  4. Applied: the starred four's place at the top of LOCK-n v0.1's list is stated as the coordinating session's
     recommendation, pending the PI's word, in the entry and in the spec raw's head.
  5. Applied: the second fragile point (two SVDs of one array held bit-equal) is stated in the review raw.
  6. Applied: the review raw's head notes its report's first-line slip ("…e2ee" for "…ee2e").
  7. Settled by run 3: 462/462, so the box's 473 stands (run 2 failed one driver check's list of expected files,
     which draft 3 fixes).
  8. Applied: the after-load refusals (another provenance, another shape) in the entry's stage list.
  9. Applied: "its brief itself excepted" in the spec raw's head and the review raw's head.
  10. Followed: the two added departures are in the entry, not in `gvec.py`.
  11. Applied: "(given in full in the module's and the driver's docstrings)".

## 2. The texts changed after the check, and the edits checked by tool

- **All four texts changed after the check:** by the dispositions above; by run 2's failure and draft 3's fix (a
  driver check's list of expected files); by run 3's figures filled in (the entry's and the review raw's run
  placeholder, and the self-test raw's run 2 and run 3 sections, rebuilt from the runs' own files); and, in the entry,
  by run 3's three `find`s in the self-test overlay, added to Code's departures.
- **The edits, checked by tool:**
  - a fixed-string search over the unwrapped final texts: each edit's new wording present, and the wording it replaced
    absent, 51 of 51;
  - the spec raw's three sections byte-equal to their sources, by `cmp`;
  - the self-test raw rebuilt by its script from the drafts, the overlay and the runs' own files.
- **The finals:** the entry `84c2ab74…7f79`; the spec raw `c88c3173…2a6a`; the self-test raw `33cea75b…8cc5`; the review
  raw `393cad86…2630`.

## 3. The report as returned

```text
VALUES-CHECK — G-VEC's BUILD texts T1–T4 (blind; read-only). Brief S/step4b/gvec/vc_brief_final.md checked: sha256 d74cdad3…e5ee, 90 lines. T1–T4 hash to their stated sha256s. HEAD is 003ae7d9a12b…; every named HEAD file is tracked and clean (rev-parse against hash-object). All four texts are judged against the five final drafts in S/step4b/gvec/draft/, and against S/step4b/gvec/draft_reviewed/ where a text speaks of draft 1.

ITEMS

T1 = S/step4b/gvec/commit/entry.md
1. T1:1 (also T2:3, T3:2, T4:3). PI date 2026-11-19. NOT CHECKABLE: it is the PI's calendar. It is consistent across all four texts and with the session date.
2. T1:1–2. Citations "n v0.2 §8 step 7; the G-VEC paragraph of n §3; ADDENDUM-n1 §1.1 and §6.1–§6.2". CONFIRMED. PROPOSAL-n-bk-reconciliation-v0_2.md:105 "## §3 Gates…", :111 "**G-VEC.**", :154 "## §8 Code's block", :159 "7. G-VEC."; ADDENDUM-n1…:20 (1.1), :52 (6.1), :54 (6.2).
3. T1:2–3. A new module `valence_core/n/gvec.py` and a `gvec` command in the driver. CONFIRMED: the draft gvec.py exists, and the driver diff adds "gvec" to main()'s choices and adds cmd_gvec.
4. T1:3. "Nothing has run on the box." NOT CHECKABLE.
5. T1:3–4. The run waits for the PI's word on the starred G1, G3, G6 and G9. CONFIRMED: routing_reply.txt says "…is the PI's call…" and "Don't launch G-VEC until I relay the PI's answer."
6. T1:6. Six paths on HEAD 003ae7d, with git's numstat. CONFIRMED.
7. T1:7. gvec.py `a620349f…ec71`, new, 694 lines. CONFIRMED: shasum, and `git diff --no-index --numstat /dev/null S/…/draft/gvec.py` gives 694 0.
8. T1:8. n_sessions.py `9ecb4951…eda1` (+571 −4). CONFIRMED.
9. T1:9. directions.py `f9d0114c…2db4` (+20 −2). CONFIRMED.
10. T1:10. testing.py `f1840be7…6aeb` (+14 −0). CONFIRMED.
11. T1:11. guard.py `3bf0f0d5…1f50` (+2 −2). CONFIRMED.
12. T1:12. `.gitignore` (+13). CONFIRMED: numstat is 13 0. The new file is HEAD's plus one hunk (S/…/commit/gitignore:303–315), inserted after HEAD's line 301. Its admits are tested at item 93.
13. T1:13. The digest moves from `f09898ee…b8f9` to `882c9217…5ca7`, by shell in package_sha256_of's form. CONFIRMED.
   - bash S/step4b/schema/pkgsha.sh gives f09898eee3e3…88e8b8f9 on valence_core/n and 882c9217cc3f…c3b55ca7 on S/step4b/gvec/overlay/valence_core/n.
   - A shell recomputation from HEAD's eleven unchanged files plus the four drafts gives the same 882c9217…. Over HEAD's fourteen files it gives f09898ee….
   - The form follows valence_core/m/resume.py:328–350.
14. T1:14–15. The package's own `hashes` runs at the launch files, and the box compares against it. NOT CHECKABLE: this is a plan.
15. T1:15–16. The closure gains valence_core/extract.py (`2405b1a6…07fe`), which gvec imports at module level. CONFIRMED.
   - gvec.py:78 has `from .. import extract`.
   - S/…/draft/guard.py:127–129 adds extract.py to the closure's expected set, and PRODUCTION adds "gvec".
   - No HEAD module in valence_core/n imports extract.
16. T1:16. "which imports only numpy and `adapters.base`". IMPRECISE: valence_core/extract.py:25–28 also imports `__future__`, `dataclasses` and `typing`. Replace with: "which imports, beyond the standard library, only numpy and `adapters.base`".
17. T1:17. Draft 1's 451/451. CONFIRMED: S/step4b/gvec/selftest_run1.txt reads "  451/451 n selftest checks pass" (sha256 630360970b…7c95), and the .exit file reads "exit 0".
18. T1:18, :27, :90. The raw names results/raw/2026-11-19_n-gvec-build_{selftest.txt, spec.md, review.md}. NOT CHECKABLE: these are future files, and no existing name holds "n-gvec-build".
19. T1:18–20. Box 473 = 462 + 11, with 11 = 13 HF checks in place of 2 skip lines. CONFIRMED by arithmetic.
   - RESULTS.md:42–43 gives 420 = 409 + 11 "(its 13 HF checks in place of the laptop's two skip lines)". RESULTS.md:255–257 gives 408 against 397.
   - The skip lines are hftiny.py:56 and scripts/n_sessions.py:1479.
   - No new check sits behind hftiny.available().
   - 462 = 451 + 7 + 4 (item 76). That 462 is run 2's expected count.
20. T1:21. Nothing ran on a checkpoint's weights. NOT CHECKABLE.
21. T1:21–23. Both battery windows were granted for their bytes. CONFIRMED.
   - S/step4b/gvec/commit/cs_words_gvec.md:1–9 is draft 1's grant with its hashes; :21–22 is its "go"; :24–31 is draft 2's grant with its hashes.
   - `nice -n 19` matches T3:28.
22. T1:21–23. Run 2 ran inside its window, under "Q-F3's standing rules". NOT CHECKABLE: run 2 is pending, and no named source covers those rules.
23. T1:24–25. Review totals: 0 BUG, 5 RISK, 5 NIT, 22 mutants, no self-test risk, 10 observations. CONFIRMED by review_report.md: F1–F5 are RISK, F6–F10 are NIT, mutants run M1–M22, it says "SELF-TEST RISKS - None found", and observations run O1–O10.
24. T1:25. "Every finding is applied in draft 2". IMPRECISE: F1's fix is the BUILD commit's `.gitignore` block, and only G7's wording sits in gvec.py:45. Replace with: "Every finding is applied, in draft 2 or, for F1's admit lines, in the BUILD commit's `.gitignore`, and each mutant is killed by a check;".
25. T1:25. Each mutant is killed by a check. CONFIRMED, line by line in the draft:
   - M1 and M2: gvec.py:616–621.
   - M3: :547–549 (R_TOLERANCE == 0.02 and the 1.019/1.03 case), plus the driver's seam check.
   - M4: :546.
   - M5 and M6: :642–644 and :667–669.
   - M7: :626–627.
   - M8: :611–613 and :677.
   - M9: :622–624.
   - M10 and M11: :590–594.
   - M12: :629–633.
   - M13: the context ids_sha refusal case.
   - M14: cases x22–x24.
   - M15: cases x25 and x26.
   - M16: :566–574.
   - M17: the smoke check against r_s and rl_s.
   - M18: the nine argvs.
   - M19: the pv["backend_identifier"] check.
   - M20: :603–604.
   - M21: :601–602 with _bk_literals_hold.
   - M22: :637–641.
26. T1:26–27. The spec raw holds the specification, the message and the routing, verbatim. CONFIRMED (items 59–61).
27. T1:29–32. The refusals before the load. CONFIRMED. run_gvec refuses, all before make_adapter:
   - an existing out folder or staging folder;
   - the pod not CHARACTERIZED_POD (HEAD scripts/n_sessions.py:456, "emw1e4embiwe9b");
   - CUBLAS_WORKSPACE_CONFIG;
   - stream_known_answer;
   - the weights, through weights_of_record and check_weights_folder (HEAD :514–543, SystemExit);
   - the driver bytes not HEAD's, for a run of record.
28. T1:33–34. The ids of record, manifest `fdf73d85…ef38`; ids_sha re-derived; longest input ≤ 4,096. CONFIRMED.
   - ids.py:74 holds the pin, and shasum of data/n/ids/MANIFEST.json matches it.
   - The ids_sha re-derivation covers `ps + cs`.
   - schema.py:268 has MAX_WINDOW = 4096.
29. T1:35–36. The corpus `ef6b00dc…3cc3` and its composition. CONFIRMED.
   - ids.py:78 holds the pin, and shasum of data/n/passages.jsonl matches it.
   - gvec_passages_check and gvec.passage_groups both run before the load.
   - jq over data/n/passages.jsonl finds 544 lines: 56 of each state (+: contentment, flow_engagement, relief, serenity; −: distress, dread, frustration, weariness) and 96 "0" neutral.
30. T1:37–38. A3's frozen inputs, hygiene, and the (iv) record's digests, code sha256s, contexts' digest and per-record place and texts. CONFIRMED.
   - gvec_a3_check performs these checks.
   - MANIFEST.json's iv.a3 has the keys code_sha256, contexts, contexts_sha256 and input_shas.
   - Its code_sha256 equals HEAD's scripts/box_e0_corpus.py (66c18554…ab57) and extract.py.
   - box_e0_corpus.py:95–106 and :183–211 raise on failure.
31. T1:39. The axis order and the R6 bridge. CONFIRMED: run_gvec checks both (CHARACTERIZED_IDENTIFIER is at HEAD :464).
32. T1:40. The provenance is recorded whole. CONFIRMED: the code sets prov_rec["adapter_provenance"] = m_resume.provenance_record(prov), and resume.py:271–276 describes that as "VERBATIM".
33. T1:41–43. One forward per passage at 31 and 32; the site rule; a STOP writes the record alone and exits 2. CONFIRMED.
   - gvec.py:84, :128–148, :156–164 (min over (rel, −i)), :341–343, :416–436.
   - run_gvec returns 2 on a STOP.
34. T1:44. v, and v under an uncentred U, at both indices. CONFIRMED: gvec.py:167–184, :349–358.
35. T1:45–46. A3 runs on the committed ids with no tokenization: N2, the fit-only family, R_ℓ and the guard profile, at both indices. CONFIRMED: gvec.py:188–215, :360–386.
36. T1:47. Six pairs, plus all 378 pairs among 28 directions, at the site. CONFIRMED: gvec.py:388–392 (4 named + 24 random; C(28,2) = 378).
37. T1:48–50. Staging, then rename; the six output files. CONFIRMED: run_gvec does the os.replace; gvec.py:97, :102–107, :416–436.
38. T1:51–52. "and every sha16 is the Injection's". IMPRECISE.
   - The rows and every direction's sha16 are the Injection's (gvec.py:238–263; adapters/base.py's Injection; runner.py:294's at_frac expect_sha).
   - The record also carries U_sha16 (gvec.py:182, a sha16_arr of the ten PCs) and A3's freeze_sha (gvec.py:379). Neither is the Injection's.
   - Replace with: "…and every direction's sha16 is the Injection's: what the campaign's `expect_sha` checks;".
39. T1:53–54. The smoke. CONFIRMED: run_gvec's branch takes N in 1..N_NEUTRAL, requires a new --out outside the repository, takes neu[:N] and cs[:N] (A3's order, as held by gvec_a3_check), and writes status "SMOKE".
40. T1:55–56. The quote "Start building G-VEC in scratch now, on G1–G14 as you've written them." CONFIRMED: routing_reply.txt line 1.
41. T1:56–58. The two requests are built. CONFIRMED: routing_reply.txt:8–10 against gvec.py:373–383, ALT and :43–44.
42. T1:59–71. G1–G14 in brief. CONFIRMED.
   - They match S/step4b/gvec/pins_sent.txt and gvec.py:28–60.
   - The starred four, G9's figures and G13's pin all agree.
   - BK's figures were read with jq on strength_ladder/analysis.json, selecting the one member by its "ol" prefix: [[25.491040760519905, 2.319276809692383, 32]].
43. T1:73–75. The departures list. IMPRECISE: it equals gvec.py:62–65, but the review's O3 also names two departures from the routed words.
   - G12 ("`--smoke N` works as backend-ext's"): the build has `--smoke N --out` with N in 1..96, where backend-ext uses `--root`/`--report` and 1..24 (HEAD scripts/n_sessions.py:995–1002).
   - G14: ‖h̄₊ − h̄₋‖ is added beside ‖v‖.
   - Append: "; G12's smoke (`--out`, N in 1..96, where backend-ext's takes `--root` and `--report`, N in 1..24); and G14's ‖h̄₊ − h̄₋‖ beside ‖v‖".
44. T1:76–77. The PI's call; the coordinating session asked, recommending the run on them as PINs. CONFIRMED: routing_reply.txt line 1.
45. T1:78. "as the coordinating session set them". IMPRECISE: cs_words_gvec.md:33 reads "The entry carries O5, O6, O7 and O9 as you list them." Replace with: "(the review's O5, O6, O7 and O9, as Code listed them, on the coordinating session's word):".
46. T1:79. 473 is restated at the launch files. NOT CHECKABLE: this is a plan (the arithmetic is item 19).
47. T1:80–81. STOP and re-run mechanics, and the staging folder refused before the load. CONFIRMED: write's STOP branch; the refusals precede the pod check; the except-branch rmtree cannot run on a hard kill.
48. T1:82. The smoke is the HF seam's first run. CONFIRMED as declared: the draft driver's docstring says so, and the review's O7 notes no check exercises the seam.
49. T1:83. G3 matters only if the site is 31; both indices are recorded. CONFIRMED (review O9; code).
50. T1:84–85. The review bullet's pass and totals. CONFIRMED.
51. T1:86–89. The applied F1–F10, O1, O8 and O10, with their glosses. CONFIRMED (items 93–113).
52. T1:93–96. Code's departures. NOT CHECKABLE.
53. T1:97–100. The survey's departures. IMPRECISE: S/step4b/gvec/spec_report.md's last section says the five "printed raw names (2, 3, 3) and a count (899), or nothing". Replace with: "…or with one only, printing raw names, a count, or nothing;". The git log over four paths and the two git greps are confirmed.
54. T1:101–104. The reviewer's departures. CONFIRMED: review_report.md:291–305.
55. T1:107–113. The paths committed, the commit-time count of 0, "Not pushed". NOT CHECKABLE.
56. T1:112. "(the third sitting's answers, §5.2)". CONFIRMED: results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md:3 says "(third sitting)", and :38 is "5.2 The Code-side form…".
57. T1:114–116. Next. CONFIRMED against the last paragraph of routing_reply.txt (a STOP block if the PI sends the four); the rest is plan.

T2 = S/step4b/gvec/commit/spec_raw.md
58. T2:5–6. Written for the seat's LOCK-n v0.1 sitting, with the starred four at the top of its list. CONFIRMED as the coordinating session's recommendation (routing_reply.txt line 1) and as gvec.py:26–27 declares it. See observation 4.
59. T2:7–8. §1 is verbatim (`18d31729…fae1`, 42 lines) and in no other file. CONFIRMED.
   - `sed -n 23,64p | cmp - S/step4b/gvec/pins_sent.txt` reports equal; the sha256 and 42 lines match.
   - A git grep of its phrase over the tree, with item 3's pathspec, finds nothing. S cannot be searched.
60. T2:9. §2 is verbatim (`9287c339…825a`, 13 lines, the 13th blank). CONFIRMED: lines 70–82 equal S/step4b/gvec/routing_reply.txt by cmp; the sha256 matches; git grep finds nothing.
61. T2:10–12. §3 is the report verbatim (`07511f94…9f90`, 362 lines), compiled at HEAD 003ae7d. CONFIRMED: lines 88–449 equal S/step4b/gvec/spec_report.md by cmp, and the report's first line names the HEAD. "By a subagent" and "by jq" are not checkable.
62. T2:11. "with a file:line citation for every claim". IMPRECISE: some claims cite a commit or a search, or nothing — "It was done at b523f6a."; "(by `git grep`)"; "It loads no model and holds no A3 path." Replace with: "with a citation for its claims (file:line, or the commit or search for a claim of absence), as its brief asked".
63. T2:12–15. Its brief (`e2771848…800b`, 58 lines) and its bars. CONFIRMED.
   - spec_brief.md:3–4 and :38–58 carry the bars.
   - Its items 1–5 are byte-equal to this check's brief's: sha256 2373155c…c185 for spec_brief.md:54–58, review_brief_final.md:79–83 and vc_brief_final.md:86–90.
64. T2:15–16. The departures are in its last section and in T1. CONFIRMED.
65. T2:18. "None of the three names a local path." CONFIRMED: scratch appears only as S/…, and the only absolute paths are the box's /workspace/models ones.

T3 = S/step4b/gvec/commit/selftest_raw.txt
66. T3:1. Citations. CONFIRMED (as item 2).
67. T3:4–9. Five full sha256s, gvec.py new. CONFIRMED.
68. T3:10–13. f09898ee…8b8f9 (as RESULTS.md:35–37 records it) to 882c9217…b55ca7, both by shell. CONFIRMED (item 13).
69. T3:13–14. "The self-test prints no digest". CONFIRMED: HEAD's cmd_selftest prints only FAIL lines and the count; run_gvec's lines go to a list; run 1's whole output is one line.
70. T3:14–15. The closure gains extract.py, imported at module level. CONFIRMED (item 15); the `hashes` plan is not checkable.
71. T3:17–19. "(the driver's docstring)". IMPRECISE: the docstring (scripts/n_sessions.py:7–9) covers hftiny's cases only. The vanilla score's skip is the driver's own branch (:1466–1479). The schema's single aggregated line is confirmed (:195–196). Replace with: "…are skipped and counted as skipped (hftiny's by the driver's docstring, the vanilla score's by its own branch in the driver); …".
72. T3:20–25. "160 files, the five above replaced by each run's drafts". IMPRECISE: `git ls-files -- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`, filtered to the listed paths, counts 159 at HEAD, and gvec.py is new (cs_words:4: "Exactly four differ and one is new"). Replace with: "160 files: HEAD's 159 on those paths, four of the five above replaced and `valence_core/n/gvec.py` added by each run's drafts."
73. T3:26–31. The command, venv, re-hashes and temp folder. NOT CHECKABLE.
74. T3:33–36. Run 1 used the bytes the review read. CONFIRMED: review_brief_final.md:8–13 and the draft_reviewed/ hashes agree.
75. T3:36–38. Exit 0, the output's sha256, the indent. CONFIRMED: T3 line 38, less five spaces, hashes to 630360970b….
76. T3:40–42. Eleven checks more: seven from gvec and four from the driver's flags (5 to 9). CONFIRMED.
   - gvec._selftest runs 22 chk calls in draft_reviewed (gvec.py:393–529) and 29 in draft (:484–683).
   - The driver's only new checks are the argv loop's four: --report, --ruling, --tokenizer-dir and --ids-dir.
   - 451 = 409+1+22+18+1 (the review brief); 462 = 409+1+29+22+1.
77. T3:45–47. 473, and no box-only check added. CONFIRMED (item 19). "The box has not run" is not checkable.

T4 = S/step4b/gvec/commit/review_head.md
78. T4:5–6. Draft 1's files: gvec.py new, 529 lines, read in full. CONFIRMED: wc -l, and review_report.md:6.
79. T4:6. "`5ef276df…55d1e7`". IMPRECISE: the form is first 8 … last 4. Replace with: "`5ef276df…d1e7`".
80. T4:7–8. The four deltas' hashes. CONFIRMED.
81. T4:9. The self-test had not run when the brief went out; it then ran 451/451. CONFIRMED: review_brief_final.md:15–17 and selftest_run1.txt. "While the review was in progress" is not checkable (cs_words:16–19 is consistent).
82. T4:11. Brief `10f9e31f…ee2e`, 83 lines. CONFIRMED.
83. T4:12–15. The brief's specification list. CONFIRMED: review_brief_final.md:14 and :19–38.
84. T4:16–19. The two verbatim copies, the departures question, the self-test risks. CONFIRMED: :39–46 and :54–55.
85. T4:20–22. Items 1–5 verbatim, the pathspec, the glob rule, the rev-parse form. CONFIRMED: :73–83 (item 63).
86. T4:23–25. The bars, and seven named scratch files. CONFIRMED: :61–72.
87. T4:27–28. 306 lines, `b50cbcaf…d5d4`, no local path. CONFIRMED. "By jq" is not checkable.
88. T4:28–29. The line numbers are draft 1's. CONFIRMED: driver:2054, :2081, :2153, :2175, :2198, :2473, :2515 and gvec.py:203–209 and :279 read in draft_reviewed as the report cites them.
89. T4:31. Totals. CONFIRMED.
90. T4:35–36. Draft 2's hashes and 694 lines; directions, testing and guard are draft 1's. CONFIRMED.
91. T4:35. "Every applied disposition is in draft 2's bytes". IMPRECISE: F1's admit lines are the BUILD commit's `.gitignore`. Replace with: "Every applied disposition is in draft 2's bytes, but F1's admit lines, which are the BUILD commit's `.gitignore`: …".
92. T4:36–37. Draft 2's window was granted for its bytes. CONFIRMED: cs_words:24–31. The run itself is pending.
93. T4:39–41. F1. CONFIRMED.
   - At HEAD, check-ignore names `.gitignore:263:/data/n/*` for data/n/gvec/ paths.
   - The new block is `!/data/n/gvec/`, `/data/n/gvec/*` and six `!` admits, in 9f64305's form (HEAD .gitignore:298–301).
   - With S/…/commit/gitignore as the only patterns, the six outputs are re-included (its :309–314), any other name under data/n/gvec/ is ignored (:308), and data/n/.gvec.staging and its contents stay ignored (:263). The block admits exactly the six.
   - gvec.py:45 carries G7's new wording.
94. T4:42–44. unit32 is a fixed point with four passes, else a refusal. CONFIRMED: gvec.py:244–263.
95. T4:43–44. "every sha16 the record carries … through the Injection". IMPRECISE: U_sha16 (gvec.py:182) and freeze_sha (:379) are sha16_arr digests. Replace with: "every direction sha16 the record carries, the 24 random directions' among them, is taken through the Injection itself (`injection_sha16`); U's sha16 and A3's freeze_sha stay `sha16_arr` digests".
96. T4:44–45. The at_frac check. CONFIRMED: gvec.py:597–600.
97. T4:46. F3. CONFIRMED (item 25).
98. T4:47–48. F4. CONFIRMED: gvec.py:92, :376, :380–383, :397, :422–429.
99. T4:49–51. F5. CONFIRMED: the staging refusal precedes the pod check; passage_groups and the axis order run before the bridge; the "a staging folder a hard stop left" case requires len(made) == n_made.
100. T4:52–53. F6. CONFIRMED: gvec.py:296–308, :336–337.
101. T4:54–55. F7. CONFIRMED: gvec.py:334, :406–413; extract.py:227.
102. T4:56–57. F8. CONFIRMED: resume.py:271–276.
103. T4:58–60. F9. CONFIRMED: gvec.py:29–31, :50–52, :98–99, :371–372; box_a3_extract.py:101–103.
104. T4:61–62. F10: the list is in the docstring and the entry. CONFIRMED that both carry it; its completeness is item 43.
105. T4:63–71. The M1–M22 groupings. CONFIRMED (item 25).
106. T4:72–73. No self-test risk; the "ids" print test is replaced. CONFIRMED: gvec.py:645–648.
107. T4:74–75. O1. CONFIRMED: gvec.py:167–174, :352, :356–358.
108. T4:76. O2. IMPRECISE: the departures name only "G2's tie rule" (gvec.py:62–65). Replace with: "the site rule's two readings (nearer in R; an exact tie to 32) are declared in G2, and the tie rule also in the departures."
109. T4:77. O3. IMPRECISE: as item 43, O3 also names G12's smoke form and G14's added ‖h̄₊ − h̄₋‖. Replace with: "O3: the departures listed in the docstring and in the entry; G12's smoke form and G14's ‖h̄₊ − h̄₋‖, which O3 also names, stand declared in the driver's docstring and in G14's own line." Or align with how item 43 is settled.
110. T4:78. O4, no action. CONFIRMED.
111. T4:79–81. "as the coordinating session set them". IMPRECISE (as item 45; the content is confirmed). Replace with: "in the BUILD entry, as Code listed them, on the coordinating session's word: …".
112. T4:82–83. O8. CONFIRMED: gvec.py:399–400.
113. T4:84. O10. CONFIRMED: the driver's smoke line and its docstring.
114. T4:85. The reviewer's departures are in the entry. CONFIRMED: T1:101–104.

TOTALS: 114 items. 89 CONFIRMED, 15 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE.

OBSERVATIONS
1. Style against 003ae7d (RESULTS.md:165–173). T1's Review bullet names only the applied items. Add, for example: "Declared: O2 (in G2; the tie rule also in the departures) and O3 (the departures). In this entry: O5, O6, O7 and O9 (For the run). No action: O4."
2. T1:13 could carry 003ae7d's sentence that the same computation over HEAD's files reproduces `f09898ee…b8f9` (reproduced here). Neither digest has yet been printed by the package's own `hashes`.
3. T1:12 gives `.gitignore` no digest. S/step4b/gvec/commit/gitignore is `a0124153…90ee`, and its 13 lines are a four-line comment, the folder admit, the contents ignore, six admits and a blank line.
4. T1:55 and T2:5–6 present the starred four's place at the top of LOCK-n v0.1's list as settled. It is the coordinating session's recommendation, pending the PI. If the PI sends the four now, a STOP block reaches the seat first.
5. The reviewer named two fragile points (review_report.md:222–224), and T4 answers one. The other — two SVDs required bit-equal (draft 1 gvec.py:436–437) — stands at gvec.py:530–532.
6. review_report.md:1, which will be §2's first line verbatim, abbreviates its brief's sha256 as "10f9e31f…e2ee". The hash ends "…ee2e", as T4:11 has it. T4's head could note the slip.
7. "the 462" (T1:19, T3:45) is run 2's expected count, and T1:21–23 and T3:30–31 describe run 2 as done. When @RUN2@ is filled, confirm 462/462, or move 473 with it.
8. T1's stage list (T1:40) omits the after-load refusals: the provenance must be the one checked before the load, and the shape must be (64, 5120); neither writes anything.
9. T2:13–15 and T4:23–25 state the briefs' bars on Code's scratch. Both reports show their subagent hashed its own brief there, presumably on its invocation's word, and neither lists it. "its brief itself excepted" would close this.
10. For item 43: the entry alone can carry the two additions. Adding them to gvec.py:62–65 moves the package digest, which would need a new window, self-test and re-check of the figures here.
11. T1:28's "(the module's and the driver's docstrings in full)" reads as if the docstrings were reproduced. "(given in full in the module's and the driver's docstrings)" is clearer.

DEPARTURES
- `git log -3 --format='%H %s'` with no path; it printed ids and subjects only.
- Two `git ls-files` runs with a narrower pathspec in place of `.`: `git ls-files valence_core/n`, with no exclusions (14 names), and `git ls-files -- '*.gitignore'` with all three exclusions (1 name).
- Two `git check-ignore --no-index -v -n` runs beyond the permission's letter:
  - (a) in the repository, against HEAD's `.gitignore`, naming six non-existent paths under data/n/gvec/ and data/n/.gvec.staging/;
  - (b) reading S/step4b/gvec/commit/gitignore as the patterns via `-c core.excludesFile`, with `--git-dir` at the repository's git directory and `--work-tree` at an empty system folder outside the repository and S (cd'd into). It also named data/n/.gvec.staging itself and one path outside both folders, data/n/backend-ext.json. For (b) I read `.git/info/exclude`: 10 patterns, all `**/.claude/…`.
- `jq` beyond the BK member: pole and state counts over data/n/passages.jsonl; `.iv.a3` keys and code_sha256 of MANIFEST.json; keys and non-id fields of the two (iv) files' first lines.
- Not barred by my reading, for the record:
  - a shell recomputation of the package digest from named files, beside pkgsha.sh;
  - direct reads of HEAD's scripts/n_sessions.py (its docstring, cmd_selftest, _e0_corpus, check_weights_folder, weights_of_record, driver_bytes and the vanilla-score branch, plus greps);
  - RESULTS.md:1–23;
  - one grep of results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md;
  - `od`, `tail -c`, `wc -l`, `sed -n`, `cut` and `cmp` on named scratch files and the brief;
  - `/usr/bin/grep` over `git ls-files` output and over the output of `ls results/raw`;
  - `head -c` on data/n/passages.jsonl.
- No interpreter, no write, and no network. No guard marker reached an argv. Nothing under data/mf3, ckpt or reports was touched. In S, I read only the named files plus the brief, and the only listing was pkgsha.sh's own `ls` of the overlay folder.
```
