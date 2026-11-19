# n step 4 — driver v2g's blind review: the fourth sitting's two aggregate lines against BK's recorded d = 0 values, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over the driver's delta:
- from HEAD's `scripts/n_sessions.py`, sha256 `e29839c8…1152` (v2f, committed at `1272702`, unchanged since);
- to v2g's reviewed draft, sha256 `b8ebc595…66b5`: §2.3's two lines, (b) per label with the pooled figure beside
  under R8's kind (the seat's answers of 2026-11-18, fourth sitting, §2.3).

**The reviewer's brief:**
- gave the two files, the `git diff --no-index` form for the delta, and the specification: §2.3, with §1.3, §2.1,
  §2.2 and §2.4 for context; the coordinating session's instructions for v2g and for (b), quoted (the latter without
  its last sentence); the driver's
  docstring as changed; BK's `reduced.json`, with how to select its member without naming its key; the constraint that
  nothing under `valence_core/` changes; and the self-test's count, 394/394;
- named the code the driver calls (the runner, the schema, the primitive, the cells, the sessions, the test doubles);
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, that a glob is expanded and read before it is looped over, and the `rev-parse` form for a
  tracked-and-clean check;
- barred any interpreter, any write, any network, any guard marker in an argv (paths and jq filters included, and
  BK's skeleton folders, named for the model, not listed or globbed), anything under `data/mf3`, and, in Code's
  scratch, anything but the one file under review (no listing, `find`, `grep` or glob there).

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (109 lines, sha256
`0561eed3…fb33`). It names no local path but one generic, elided folder, `~/.claude/projects/…/tool-results/`, in its
first disclosure.

**Totals:** 0 BUG, 2 RISK, 3 NIT, 6 surviving one-line mutants, and 5 observations.

## 1. Dispositions

The fixes are in v2g's final bytes, sha256 `7aefd06b…5b67`: the reviewed draft plus 52 lines and minus 30, every one
a disposition below.
- **F1** (RISK; nothing checked which sessions the BK seam receives) and **M1**. Applied in the reviewer's form.
  `env_for`'s `bk_reads` seam records the session ids of every call, by the environment's tag. Three checks pin it:
  - the first stage's full run asks once, for the plan's 24 sessions in launch order;
  - the first-stage smoke of 2 asks for its 2 sessions alone, the plan's first two;
  - backend-ext-2's smoke of 2 does the same.

  In the toy flow the floor sessions are the plan's 24, so the full-run check cannot tell M1 from the code; the two
  smokes can, and they kill M1 and its `ss` variant.
- **F2** (RISK, low; refusal gaps) and **M2–M5**. Applied, with the optional type check. `bk_d0_reads` takes a value
  only if it is a JSON number (`type(v) in (int, float)`, which excludes booleans) and finite. A string or a boolean
  is refused, where the draft passed numeric strings and booleans through `float()`. The `try`/`except` is gone, so
  M5 has no line left to mutate. The refusal check goes from 7 cases to 13: the other cue (M2), a "random" kind beside
  "valenced" (M3), -Infinity beside NaN (M4), a non-numeric and a numeric string (M5's class), and a boolean; no
  message quotes a value.
- **F3** (NIT; "in any cell"). Applied: the docstring's step 7 now says a session "of any cell, floor or not", and
  `bk_d0_reads` "of any cell (floor or not)"; in both, its read is the one for "the session's own cell and run".
- **F4** (NIT; the readings' parenthetical). Applied: "each flagged in its entry for the seat, which accepted R7 and R8
  at its fourth sitting, §5; R8's last sentence, added in v2g, is pending it".
- **F5** (NIT; a short line). Applied: the paragraph is reflowed.
- **M6** (the BK read moved after G-VER). Killed: the check of a BK table lacking a session gives its environment a
  G-VER seam that records its calls, and requires that it was not called.
- **O1–O5** ask for nothing.
  - O1's counts agree with this session's own count by `jq` before the draft: 240 reads at point 0, all "none", 240
    distinct cells and runs, none of their values not finite; over the 160 session reads, the margin equal to S − U
    exactly.
  - O2 and O3 are declared in the docstring.
  - O4 is the pooled figure's sentence under R8, pending the seat.
  - O5 is noted.
- **Departures.** None barred, by the report. Its four disclosures go to the seat to class, with v2g's entry:
  - the harness saved the diff's output to a tool-results file, which the reviewer read there;
  - one `git show -s --format=%B` of `1272702`'s message body, piped to a grep;
  - the `valence_core` cleanliness checks took `-- valence_core` with the three exclusions, not `-- .`;
  - greps on single named files, and `wc -l` on six `valence_core/n` files.

## 2. The report as returned

```text
BLIND REVIEW: driver v2g delta, scripts/n_sessions.py (v2f e29839c8…1152 to v2g b8ebc595…66b5)

Checks before the review, all run by tool:
- HEAD's scripts/n_sessions.py is tracked and clean: `git rev-parse HEAD:<path>` equals `git hash-object <path>` (ecd94ed6…).
- Both sha256s match the brief.
- The delta was taken with `git diff --no-index -U3 scripts/n_sessions.py <TO>` from the repository root.
- The delta changes only the driver:
  - the docstring (steps 3 and 7, backend-ext-2, the readings' header, R8);
  - three new functions: `bk_d0_reads` (L693), `bk_compare` (L727), `bk_lines` (L759);
  - one new BextEnv seam, `bk_reads` (L929), wired at L966;
  - two call sites in run_backend_ext (L1058, L1096-1097);
  - 16 new self-test checks. v2f's commit message records 378/378, and 378 + 16 = 394, which matches the stated count. I did not run it.

Verdict: the production change does what §2.3 and the coordinating session's text specify. Nothing in the read path changes, and neither the package digest nor the import closure can move. No BUG found. One RISK (F1, mutant M1) should be fixed before the commit.

Spec conformance, checked line by line:
- (a), L745-746: the record's `margin` (primitive.read's cached `lps - lpu`) against BK's recorded `margin`, absolute value. It prints median (np.median), max, `compared` and `of`.
- (b), L747-749: the cached `logprob_S` and `logprob_U` against BK's `logprob_S` and `logprob_U`. S and U are printed separately, each with median, max and count. The pooled figure sits beside them (L756, `of` = 2n), declared under R8 (L109-111).
- Placement, L1095-1097: only on COMPLETE (the PAUSE branch returns at L1086-1091), right after the distribution line and before the finiteness check, in both stages.
- What is printed: json.dumps(sort_keys) of {compared, of, median, max}. No margin, no value, nothing per session.
- BK's value, L700-723: the one point-0 read for the session's (cell, run), direction_kind "none", with matching cues.
- Read path: runner.StageInputs, runner.run and primitive are untouched. The BK read sits in step 3 (L1058), before G-VER and the load.
- Digest: valence_core/ has no tracked change and no untracked file. The closure is taken from sys.modules at L1046, before L1058. `bk_d0_reads` imports nothing new and `bk_compare` imports only numpy. So package_sha256 and imported_sha256 do not change, and backend-ext-2's first-stage identity precheck is unaffected.

FINDINGS

F1 RISK. L1058, with the flow self-test at L1472, L1526-1547 (seam L1539) and L1728-1731.
- The flow's 24 sessions are `toy_session(r) for r in range(BEXT_N)`: all floor sessions (runs 0-23).
- So in every flow run, `floor_all` is the same 24 sessions as the plan's (a superset for the smokes, whose extra rows go unused). The bkmiss case refuses whatever list it is given.
- Nothing checks which sessions `bk_reads` receives. M1 (`env.bk_reads(floor_all)`) passes all 394 checks.
- In production, R1's 24 include non-floor sessions; the self-test asserts this itself at L1315.
- So under M1, on the box, `bk_compare` raises SystemExit at the first non-floor record. That happens after runner.run has written a COMPLETE report and after the distribution line. The §2.3 lines never print, the exit is 1, and any resume fails the same way.
- Fix: have env_for's `bk_reads` seam record its argument, and check it equals the plan's session ids in launch order (`[s.session_id for s in fss]` for full runs, `fss[:2]` for the smokes).

F2 RISK (low). L711-721.
- The refusal tests at L1337-1345 do not cover:
  - a cue_U mismatch (bk_d0_floor's tests do have one, `one_cue`);
  - a non-"none" kind other than "valenced";
  - ±Infinity;
  - a non-numeric string.
- These gaps are why M2-M5 survive.
- Also, `float(r[f])` at L717 accepts JSON booleans (true becomes 1.0) and numeric strings. bk_d0_floor refuses both, because it reads the recorded text through half_unit.
- All of this is inert on the committed file (O1).
- Fix: add `with0(cue_U="Zone Q9")`, `with0(direction_kind="random")`, a `-Infinity` text case and `with0(logprob_S="abc")`, taking the count from 7 to 11. Optionally require `type(r[f]) in (int, float)` before the float.

F3 NIT. L72-73 and L697: "in any cell" reads as if BK's read could come from any cell. The code correctly takes only the session's own (cell, run). Suggested wording: "for a session of any cell, floor or not".

F4 NIT. L82-83: the edited parenthetical still says "each flagged in its entry, pending the seat". The fourth sitting accepted R7 and R8 as declared (answers §5). Only R8's new v2g sentence (L109-111) is pending, and the parenthetical could say so.

F5 NIT. L121-123: the reflow leaves a short line, "no in-band count and no comparison. Exit 0".

SURVIVING MUTANTS (by reading the code, not by running it)

M1. L1058: change `env.bk_reads([p.session for p in plan])` to `env.bk_reads(floor_all)`.
- This is wrong on the box, as F1 describes.
- Killed by the recording-seam check in F1.
- `env.bk_reads(ss)` also survives, but gives the same output on the committed file, which records all 160 sessions. The same check kills it.
- `floor` is not a valid variant: it is assigned only at L1059, so using it at L1058 raises UnboundLocalError.

M2. L711: delete `or r.get("cue_U") != s.cue_U`. Killed by a `with0(cue_U="Zone Q9")` refusal whose message quotes no value.

M3. L712: change `!= "none"` to `== "valenced"`. A point-0 "random" read would then be accepted. Killed by `with0(direction_kind="random")`.

M4. L720: change `not math.isfinite(v)` to `math.isnan(v)`. Killed by replacing `"logprob_S": -9.5` with `-Infinity` in the synth text; json.loads accepts that token.

M5. L718: drop ValueError from the except tuple. A non-numeric string would then escape as a ValueError that quotes the recorded text, instead of the SystemExit that names the session. Killed by `with0(logprob_S="abc")`, refused with no "abc" in the message.

M6 (a move of one line). Move L1058 to after G-VER's PASS check (between L1070 and L1071). The docstrings put BK's values before G-VER, but the bkmiss check only asserts "before the load". Killed by giving the bkmiss env a gver seam that records its call and asserting it was not reached.

Mutants I checked that are killed:
- dropping abs;
- swapping the labels, or the margin for S;
- comparing fresh-path values instead of cached ones;
- dropping the point filter or the duplicate check;
- printing before the distribution line, or after the finiteness check;
- printing in one stage only;
- moving the BK read after the load;
- np.mean in place of the median;
- a wrong pooled `of`.

OBSERVATIONS

O1. What BK's reduced.json holds (the member selected by `startswith("ol")`, 5,040 reads, read with jq):
- 240 reads are at point 0, all direction_kind "none":
  - 160 in the 14 session cells, one per (cell, run), runs 0-159, arm "neutral";
  - 80 in the ste_n/ste_p cells.
- No (cell, run) appears twice at point 0.
- margin, logprob_S and logprob_U are JSON numbers in all 240 reads, and margin equals logprob_S − logprob_U exactly (largest deviation 0).
- Every (cell, run) also has reads at ±0.5 and ±1. A looser point filter therefore collides at once.
- Consequences:
  - every refusal branch of bk_d0_reads is unreachable on the committed bytes;
  - §2.3 (b)'s "where reduced.json records the label values" holds for all 160 sessions, so the counts reflect only what is non-finite on this box;
  - line (a) per session is |ΔS − ΔU|, so the shared first token cancels, as §2.3 expects.

O2. If BK lacked a value, the code refuses before the load rather than printing a smaller count. This is declared in the docstring and inert on the committed file. It does mean a figure that binds nothing could stop the stage, but only if reduced.json changed, and the self-test's L1316 check would fail first.

O3. The two lines also print in the first stage: on any COMPLETE backend-ext invocation, for example a resume, under "bare". The docstring declares this and the self-test checks it (L1577-1582). There, line (b) would show the 9.7-nat convention gap, not a cross-hardware figure. It is inert unless the first stage is resumed.

O4. The pooled figure is newly declared under R8 and pending the seat. Its np.median equals label_counts' statistics.median on finite lists.

O5. Judging by the field names (margin beside fresh_margin), BK's `margin` is the cached-path value, so line (a) compares cached with cached.

DEPARTURES: none that a rule bars. Disclosures:
1. The harness saved the diff's stdout (33 KB) to a tool-results file under ~/.claude/projects/…/tool-results/, and I read it there. I wrote no file.
2. `git show -s --format=%B 1272702 | /usr/bin/grep -o …` read one commit message body, with no patch and nothing under data/, to get v2f's self-test count. Item 1 lists git log formats of ids, subjects and times, not a body.
3. The valence_core cleanliness checks (`git diff --name-only HEAD`, `git ls-files --others`) used `-- valence_core` plus the three exclusions, not `-- .`.
4. Greps were on single named files only (schema.py, cells.py, guard.py, RESULTS.md). I also ran `wc -l` on six valence_core/n files.

No interpreter, no write, no network. No guard marker appeared in any argv; the jq filters used `startswith("ol")`. Nothing under data/mf3, any ckpt folder or any reports folder was touched. In the scratch folder I touched only the TO file, by Read, shasum and the diff.
```
