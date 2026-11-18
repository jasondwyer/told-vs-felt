# n step 4 — driver v2e's blind review: §1.4's distribution and `backend-ext-2` (ADDENDUM-n2 §4.1), as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over the driver's delta:
- from HEAD's `scripts/n_sessions.py`, sha256 `18f19b8e…4f5c` (committed at `ad856f0`, unchanged since);
- to V2E, sha256 `43a01b36…090d`: §1.4's distribution printed whole and `backend-ext-2` wired, on the coordinating
  session's choice (b) (the seat's answers of 2026-11-18, third sitting, §1.4; ADDENDUM-n2 v0.1 §4.1).

**The reviewer's brief:**
- gave the two files, the `git diff --no-index` form for the delta, and the specification: §1.4's words, §4.1's words,
  the coordinating session's instructions for v2e (quoted), the driver's readings R1–R8, and the constraint that
  nothing under `valence_core/` changes;
- named the code the driver calls (the runner, the schema, the cells, the primitive, the ids, the test doubles, the
  guard);
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, and that a glob is expanded and read before it is looped over;
- barred any interpreter, any write, any network, any guard marker in an argv, anything under `data/mf3`, and, in
  Code's scratch, anything but the one file under review (no listing, `find`, `grep` or glob there).

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (152 lines, sha256
`8192136c…6f2a`). It names no local path.

**Totals:** 0 BUG, 7 RISK, 3 NIT, 12 surviving one-line mutants, and 10 observations.

## 1. Dispositions

The fixes are in V2F, sha256 `e29839c8…1152`: V2E plus 219 lines and minus 47, every one a disposition below.
- **F1** (RISK; the self-test's environments could reach the repository). Applied. `env_for` gives every environment
  temporary defaults for `root2` and `report2`, as for `root` and `report`. It refuses, before the environment is
  made, any of the four stage paths inside the repository. A check pins the guard: an environment pointing `root2` at
  `BEXT2_ROOT`, or `report` at `BEXT_REPORT`, is refused.
- **F2** (RISK; the CLI's `--convention` hand-off). Applied in the reviewer's form. The module's `run_backend_ext` is
  swapped for a recorder, restored in a `finally`, and `main()` is driven on three argv lists:
  - `backend-ext-2 --convention space --resume --ruling p01=…`;
  - `backend-ext`;
  - `backend-ext-2 --convention bare+eot --smoke 2 --root … --report …`.

  The check requires the three recorded calls to carry every stage option as given and the convention, `None` for
  backend-ext. This kills M1 and M2.
- **F3** (RISK; backend-ext-2's PAUSE, ruling and resume). Applied.
  - backend-ext-2 under "space", on a double whose fresh path biases token 9 (the space S label's second token), ends
    PAUSE with exit 1, the line "BACKEND extension (backend-ext-2): PAUSE; no distribution until it completes", and no
    distribution line. The check asserts the PAUSE; that it falls at the run's end follows from p0 = 0 and a cadence
    of 160 reads against 24.
  - Its resume under a ruling ends COMPLETE with p01 adjudicated, one distribution line and exit 0, the first stage's
    root and report byte for byte as they were.
  - The first stage's PAUSE line is pinned the same way. This kills M11.
- **F4** (RISK; backend-ext-2's smoke). Applied. A smoke of 2 whose environment names a first-stage report that is not
  on disk ends COMPLETE with 2 records. Its SMOKE line, without the floor sessions (F10), comes before its STAGE line;
  it prints the distribution alone and no first-stage line. This kills M3.
- **F5** (RISK; the first-stage check). Applied, with the reviewer's three cases and M7's:
  - a report whose identity sha256 is stale, so not a valid report (M4);
  - backend-ext-2's own COMPLETE report, under "space", as the first stage (M5);
  - another value in each of seven identity fields (the weights, the package, the closure, the backend identifier,
    the pod, the rendering, the fidelity rule), each refused naming that field alone (M6). The stage field is left
    out: another stage makes the report invalid, which the first case covers;
  - 23 obtained of 24 planned, and 24 obtained of 25 planned, each a valid report outside the campaign, as a guard
    check confirms (M7, both conjuncts).
- **F6** (RISK; the repository paths). Applied. The four stage paths, as `_shown` prints them, are pinned:
  `data/n/ckpt/backend-ext`, `data/n/reports/backend-ext.json`, `data/n/ckpt/backend-ext-2` and
  `data/n/reports/backend-ext-2.json`. This kills M9 and M10.
- **F7** (RISK; the non-finite exit). Applied, in both stages. One read's cached path made non-finite pauses the stage
  at that read (nonfinite). Under its ruling the resume ends COMPLETE, prints the distribution with 23 finite of 24,
  and exits 1 with "a read has no finite discordance" (backend-ext-2) or "a read has no finite discordance: no
  comparison" (backend-ext). This kills M12.
- **F8** (NIT; the list as printed). Applied as a declaration. R8 now names what is printed beside §1.4's list: the
  absdiff's p90, label's median beside its max, and the counts of reads and of finite reads, the list's denominators.
  A second known answer gives label's median as 0.25 over 0.1, 0.2, 0.3 and 0.4, where the least is 0.1. This kills
  M8.
- **F9** (NIT; the docstring). Applied:
  - (a) the readings block follows backend-ext's paragraph, retitled "Code's readings for the BACKEND extension",
    naming R1–R6 as backend-ext's, R7 as backend-ext-2's and R8 the distribution's in both; backend-ext-2's paragraph
    follows it;
  - (b) backend-ext's step 1 names the STAGE line;
  - (c) backend-ext-2's paragraph speaks of the STAGE line naming backend-ext-2, not of a first line;
  - (d) it says the first stage's root and report are kept and nothing is written to either: the report is read and
    its cells hashed (O6).
- **F10** (NIT; backend-ext-2's wording). Applied. Its SMOKE line drops the floor sessions. The distribution's prefix
  is now "(absdiff and label in nats, rel = absdiff / the read's scale; fidelity values, no margin; R3's bound is
  label.max)" at the first stage, and the same without the bound at backend-ext-2.

**Mutants** — each now has its killing test: M1 and M2 (F2), M3 (F4), M4–M7 (F5), M8 (F8), M9 and M10 (F6), M11 (F3)
and M12 (F7). The mutants themselves were not run.

**Observations** (for the seat; noted):
- **O1.** R7's premise holds at HEAD: no commit since `ad856f0` touches `valence_core/`, and the driver change moves
  neither `package_sha256` nor `imported_sha256`.
- **O2.** backend-ext-2's report and cell carry stage "backend-ext"; `label_convention` and the path tell the two stages
  apart. LOCK-n's drafting takes the convention of record's report by path. (n-analyzer, told of R7: backend-ext-2
  never reaches its reader, which loads the campaign only.)
- **O3.** `.gitignore` admits exist only for backend-ext. backend-ext-2's commit needs its own; `.gitattributes`'
  `/data/n/ckpt/** -diff` already covers its cell. The seat's §4 names backend-ext's cell and report as what is
  pushed, and words the screen's clearance over `data/n/ckpt/**`; whether it reaches backend-ext-2's cell and report is
  for the seat.
- **O4.** backend-ext-2 runs in the copy that holds the resumed, COMPLETE first-stage report: the fresh copy after
  the resume. A copy without that report is refused.
- **O5.** The driver cannot check that the comparison named `--convention`: the comparison is printed, never written.
  The entry carries the comparison's line and the word that launched backend-ext-2.
- **O6.** Taken in part, as above: the first stage's cells are hashed against its report's record, and its report's
  sha256 is printed on a line of its own before G-VER (not on the STAGE line), since the report is rewritten at each
  resume. The check of p01's ruling sha256 is not taken: a COMPLETE report holds no standing pause (`check_report`),
  and the printed sha256 names the report that records the ruling's.
- **O7.** §4.1's figures of record are on the line: `exceed_tau` of `reads`, `absdiff.max` (C's input) and
  `rel.median`.
- **O8.** For the seat (blinding): where `absdiff.max` and `rel.max` fall on one read, their ratio is that read's scale
  at d = 0. v2d's maxima already allowed it, and §1.4 asks for both.
- **O9.** The count: +23 for v2e, 356 on the laptop, which Code's run gave (356/356).
- **O10.** backend-ext-2 still loads BK's table and checks every candidate's ids before the load, as backend-ext's
  steps 1–6 do. Harmless.

**The reviewer's departures**, as its report states them, for the seat to class (model-free; nothing under `data/mf3`,
`data/*/ckpt` or `data/*/reports` listed or read):
- its reading of one long diff from the harness's own tool-results folder, where the harness had saved it (the seat
  classed the same act inert at `6df2131`, the answers' §7);
- three git commands with a narrower positive pathspec in place of `.`, each with all three exclusions.

## 2. The report as returned

```text
BLIND REVIEW — driver v2e of scripts/n_sessions.py

Hashes re-checked by tool and equal to the brief. FROM is HEAD's blob 5a83fa0, and the working copy matches it: sha256 18f19b8e…4f5c, git hash-object = rev-parse HEAD:path. TO is 43a01b36…090d. I took the delta with the brief's `git diff --no-index -U3`. I read the whole TO file (1,599 lines) and runner.py. From cells.py, guard.py, testing.py and parts of schema.py, ids.py and primitive.py I read the parts I needed (table under O9).

Bottom line: I found no BUG in the production change.
- The distribution prints §1.4's items:
  - absdiff and rel, each as min/q1/median/q3/max;
  - exceed_tau and exceed_tau4;
  - R3's bound as label.max;
  - p90, declared in R8.
- backend-ext-2 follows §4.1 and the coordinating session's lines:
  - the same plan;
  - its own root and report;
  - p0 = 0 of 2,400 and identity_bound None;
  - the first stage's report checked before the load;
  - the distribution only;
  - no chaining.
- The first stage's read path is unchanged (cands[conv] and the convention are "bare").
- The findings below are untested paths, one self-test seam left pointing at repository paths, and missing declarations.

FINDINGS

F1 RISK — the self-test can reach repository paths, lines 1296–1303 with 831–832. env_for's base sets root and report to tmp but not root2 and report2. Every env_for env therefore carries BextEnv's defaults, BEXT2_ROOT and BEXT2_REPORT, which are inside the repository, and refuse_out admits data/n.
- Today only env7 and cases2 run backend-ext-2, and both override the two paths.
- A future case that calls run_backend_ext(env_for(tag)[0], convention=…) without the override would write a toy stage into data/n/ckpt/backend-ext-2 and data/n/reports/backend-ext-2.json of whatever checkout the self-test runs in.
  - On the box, that is the copy the run of record uses.
  - On the laptop, the files are gitignored, so nobody would see them.
- This breaks cmd_selftest's own contract (lines 10–13, "writes only under a fresh temporary directory") and the box-safety rule (scratch roots).
- Fix: add root2=tmp/tag/"root2" and report2=tmp/tag/"report2.json" to env_for's base. Optionally assert that all four paths of every env_for env are outside REPO.

F2 RISK — the CLI's --convention wiring is never exercised.
- Line 1579 (main → cmd_backend_ext(…, a.convention)) and line 1002 (cmd_backend_ext → convention=convention) are reached by no check; every argv case ends in an argparse error.
- If either argument is dropped (M1, M2), nothing refuses. `backend-ext-2 --convention space --resume` would then resume the FIRST stage:
  - its report is rewritten (loads_ms appended), which breaks "the first kept";
  - its distribution, in-band count and comparison are printed, and it exits 0;
  - only the STAGE line ("STAGE backend-ext: label convention bare") would show what happened.
- Fix: swap the module-global run_backend_ext for a recorder, restored in a finally. Then call main(["backend-ext-2","--convention","space"]) and main(["backend-ext"]), and assert the convention arrives as "space" and as None.

F3 RISK — backend-ext-2's PAUSE, ruling and resume path is untested (lines 975–980). Under p0 = 0 this is the path §4.1 expects ("its end-of-run pause, if it fires"). No check reads either stage's PAUSE line; pf_env (1389–1393) checks only rc and end_state (M11).
- Fix: run backend-ext-2 on testing.CausalDouble(fresh_bias=(9, 2.0)); token 9 is the second token of the space S label [6, 9, 17]. Expect:
  - rc 1 and end state PAUSE;
  - the line "BACKEND extension (backend-ext-2): PAUSE; no distribution until it completes", and no distribution line.
- Then resume with rulings={"p01": r_md} and expect rc 0, COMPLETE, one distribution line, and the first stage byte-for-byte unchanged.

F4 RISK — the backend-ext-2 smoke is untested. No call passes both convention= and smoke=, so line 944's `smoke is None` is not pinned (M3). The same goes for the docstring's "a smoke is not checked against the first stage" (83–84) and for the SMOKE-then-STAGE order.
- Fix: a backend-ext-2 smoke of 2 whose env.report names a missing file. Expect rc 0, COMPLETE, and the distribution only.

F5 RISK — first_stage_check (789–811) is only partly tested. Three guards survive mutation:
- check_report at 799 (M4): there is no invalid-report case.
- The first stage's convention conjunct at 804 (M5).
- The identity diff at 807–808 beyond weights_sha256 (M6).
- Separately, the obtained and planned conjuncts at 803 mask each other in the one fewer-reads case (the smoke, 2 of 2). They are not redundant, because check_report enforces COMPLETE ⇒ every arm complete only at the campaign (schema.py:1450) (M7).
- Fix — add three cases:
  - (a) other_first without the stage_identity_sha256 recompute, expecting "not a valid report";
  - (b) env7's own report used as the first stage, expecting "…under 'bare'";
  - (c) the identity case repeated over package_sha256, imported_sha256, pod_id, backend_identifier, rendering_id, fidelity_rule and stage.

F6 RISK — the repository paths are not pinned. No check reads BEXT2_ROOT or BEXT2_REPORT (426–427), and every STAGE line in the self-test is outside the repository, so _shown's relative branch at 1008 never runs (M9, M10).
- A BEXT2 constant set equal to the first stage's would survive the self-test. At run time it is refused: by prior_state, or, for the root alone under --resume, by load_cell's identity check after the load.
- Fix: check that _shown(BEXT_ROOT) == "data/n/ckpt/backend-ext", _shown(BEXT2_ROOT) == "data/n/ckpt/backend-ext-2" and _shown(BEXT2_REPORT) == "data/n/reports/backend-ext-2.json".

F7 RISK — the non-finite exit at line 985 is untested (M12). The condition predates v2e, but it is now the whole of backend-ext-2's exit rule (docstring line 82). No case reaches COMPLETE with a non-finite read.
- Fix: put a NaN on one read's fresh path, rule its nonfinite pause and resume. Expect rc 1 and "a read has no finite discordance".

F8 NIT — the printed list is not exactly §1.4's.
- The line also prints label.median (line 620; docstring 63–64), reads and finite. R8 (109–110) declares only p90, and the coordinating session asked for "exactly §1.4's list".
- Fix: declare label.median, and the two counts as the list's denominators, in R8, or drop label.median.
- Its known answer is also degenerate: the eight label values have median 0.0, which equals their min and q1 (M8).

F9 NIT — docstring:
- (a) The "Code's readings" block (85–110) now sits under backend-ext-2's paragraph, so R1–R6, which are backend-ext's readings, read as backend-ext-2's. Move the paragraph or retitle the block.
- (b) backend-ext prints the STAGE line too (line 915; the self-test asserts it at 1328–1331), but its steps (44–71) don't mention it. It is a new, undeclared first line in the first stage's resume output.
- (c) "a STAGE line first" (line 81) is not true for a smoke, where the SMOKE line (913–914) comes first.
- (d) Lines 77–78 and 791–792 say the first stage's root is "only read". first_stage_check reads only the report; the root is never opened.

F10 NIT — backend-ext-2's wording:
- Its SMOKE line (914) counts "floor sessions", but the stage runs no comparison.
- The distribution prefix (626) names "R3's bound", which is the comparison's bound, in a stage with no comparison.
- "(nats; …)" also covers rel, which is a ratio.

SURVIVING MUTANTS

| # | Line | Change | Killed by |
|---|---|---|---|
| M1 | 1579 | `return cmd_backend_ext(a.root, a.report, a.resume, rulings, a.smoke)` | F2's recorder |
| M2 | 1002 | `)` in place of `convention=convention)` | F2's recorder |
| M3 | 944 | `if second:` | F4's smoke case |
| M4 | 799 | `pass` in place of `schema.check_report(rep, where=p.name)` | F5(a) |
| M5 | 804 | `        or False):` | F5(b) |
| M6 | 808 | `if k not in ("label_convention", "package_sha256") and …` (any exclusion other than weights_sha256) | F5(c) |
| M7 | 803 | delete `per.get("obtained") != BEXT_N or` (or, symmetrically, the `planned` conjunct) | an edited COMPLETE report at planned 24, obtained 23 (cells entry 23 records, complete false), which is valid outside the campaign |
| M8 | 620 | `"median": float(g.min())` | a label known answer whose median differs from its min |
| M9 | 426 | `BEXT2_ROOT = REPO / "data" / "n" / "ckpt" / BEXT_STAGE` (or line 427 with `{BEXT_STAGE}`) | F6's path checks |
| M10 | 1008 | `return str(p)` | F6's path checks |
| M11 | 976 | `if not second:` (swaps the two PAUSE lines) | asserting the PAUSE line in pf_env and in F3's case |
| M12 | 985 | `if disc["label"] is None:` | F7's case |

OBSERVATIONS

O1 — R7's premise holds at HEAD.
- No commit since ad856f0 touches valence_core/, and the working tree's valence_core/ matches HEAD (names-only git log and git diff).
- guard.closure_from_modules hashes valence_core modules only, so the driver change moves neither package_sha256 nor imported_sha256.
- v2e's "bare" identity is v2d's field for field (line 579: str(convention) = "bare"), and v2e adds no import before bext_identity.
- So the first stage's resume under v2e matches its report's identity, provided the box checkout's valence_core/ is the same.
- The addendum's order keeps this true: the resume, then backend-ext-2, then the schema commit for fidelity-ceiling. A schema commit first would make first_stage_check refuse, as declared.

O2 — R7's consequence: backend-ext-2's report and cell carry stage "backend-ext". Only label_convention (hence stage_identity_sha256) and the file path tell the two stages apart. Today no code in scripts/ or valence_core/ reads a backend-ext report by stage (git grep). LOCK-n drafting and n-analyzer will need to take the report of the convention of record by path.

O3 — .gitignore admits exist only for backend-ext (.gitignore:287–294). As the file stands, data/n/ckpt/backend-ext-2/ and data/n/reports/backend-ext-2.json are ignored. Rule 27's commit therefore needs new admits. .gitattributes' `/data/n/ckpt/** -diff` already covers the new cell. The seat's §4 clearance of the screen's halt names backend-ext's cell only.

O4 — first_stage_check reads REPO/data/n/reports/backend-ext.json of the checkout the driver runs from.
- Run 3 ran from a fresh sparse copy that excludes data/*/reports (run3 raw §4).
- backend-ext-2 must run in the copy that holds the resumed, COMPLETE report; a fresh copy is correctly refused "not on disk".
- The copy committed at 6df2131 is the PAUSE-state report.

O5 — The driver cannot check that A-n1 §2's comparison actually named --convention, because the comparison is printed and never written. It admits any of space, bare+eot and space+eot. The STAGE line records what ran; the entry has to carry the comparison line and the seat's and PI's word.

O6 — first_stage_check validates the report alone.
- It does not hash the first stage's cell against the report's cells entry.
- It does not check p01's ruling sha (e2b1c77a…2a8a).
- Optional: add both checks, and print the first report's sha256 on backend-ext-2's STAGE line. The first report is rewritten at every resume, so this would record which state backend-ext-2 followed.

O7 — All of §4.1's figures of record are on the line: exceed_tau of reads, absdiff.max (the input to C) and rel.median.

O8 — Blinding, for the seat: where absdiff.max and rel.max fall on the same read, their ratio is that read's scale, max(|log p(S)|, |log p(U)|), at d = 0. v2d's max pair already allowed this, and §1.4 asks for both. Noted, not a defect.

O9 — Self-test count: I count +23 checks, so 333 + 23 = 356, the laptop figure.

| Group | New checks |
|---|---|
| Distribution and its line | 4 |
| backend-ext-2 flow | 8 |
| backend-ext-2 refusals | 6 |
| argv | 5 |

At the box, starting from v2d's 344, I would expect 367 if the HF-path cases are unchanged. That is arithmetic only; I ran nothing.

O10 — backend-ext-2 still loads BK's table and checks every candidate's ids (946–953), although it runs no comparison. This is harmless and keeps steps 1–6 identical to backend-ext.

DEPARTURES
- The diff's output was large, so the harness saved it to its tool-results folder, and I read that one file there. The seat classed the same act as a disclosed checker departure at 6df2131 (answers §7).
- Three git commands used a narrower positive pathspec in place of '.', each with all three exclusions:
  - `git log --format='%h %s' ad856f0..HEAD -- valence_core …`
  - `git diff --name-only HEAD -- valence_core …`
  - `git grep -n -I -e backend-ext -- scripts valence_core …`
  These are for the seat to class.
- No other departures:
  - no interpreter, no write and no network;
  - no guard marker in any argv;
  - nothing under data/mf3, data/*/ckpt or data/*/reports listed or read;
  - in the scratch folder, only the TO file was touched (shasum, wc -l, Read, the diff).

```
