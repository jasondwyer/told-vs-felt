# n step 4 — the driver's second blind review: the delta from v1 (the merge onto (iv), item 7's medians, the re-pin), as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over the driver's delta:
- from V1, sha256 `64cf6ee1…16cb`: the step-4 driver as frozen after the first review (which read its first draft,
  `80d30846…b03d`), and box-tested on 2026-11-16;
- to V2C, sha256 `491584aa…c63d`: V1's change carried onto the driver as committed at `b523f6a`, plus item 7's medians
  (the corpus answers of 2026-11-18, §5.5) and the re-pin to n's box (the box answers of 2026-11-18, §2 items 4–5;
  the BACKEND entry `d5d08fa`).

**The reviewer's brief:**
- gave the files and the specifications;
- quoted the list of record v2's items 1–5, verbatim;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3`, and any write.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (236 lines, sha256 `85f52a0b…8cc6`).
It writes `<repo>` and `<scratch>`.

**Totals:** 0 BUG, 2 RISK, 8 NIT, 10 surviving one-line mutants, and 6 observations.

## 1. Dispositions

The fixes are in V2D, sha256 `18f19b8e…4f5c`: V2C plus 119 lines and minus 21, every one a disposition below.
- **F1** (RISK; the median's known answer). Applied. A second known answer moves BK's values 3, 1 and 0 nats on the
  three toy sessions. The differences are 0, 0, 1, 1, 3 and 3, so the median is 1.0; the mean would be 4/3, the
  midrange 1.5, and the first or last session alone 3.0 or 0.0. The count at bound 0 is 1. This kills M1 and M2.
- **F2** (RISK; the order "committed before the run of record"). Applied in the reviewer's form.
  - A `driver` seam on `BextEnv` gives this file's bytes and HEAD's committed bytes of its path
    (`driver_bytes`, `weights_of_record`'s `git show` form).
  - A run of record refuses, before G-VER and the load, unless they are equal. A smoke runs any driver.
  - Either way a DRIVER line prints the sha256, and says whether the bytes are HEAD's.
  - Tests:
    - the flow's DRIVER line comes before G-VER's;
    - a smoke's DRIVER line says "(unchecked)";
    - two refusals: a driver that is not HEAD's, and a HEAD that shows none;
    - the refusal's text.
- **F3** (NIT). Applied. The printed median is pinned at 6 significant digits: `0.0123456789` prints as "median
  0.0123457". The header's value count is pinned in the flow ("over its 48 values") and the smoke ("over its 4
  values"). This kills M3 and M4.
- **F4** (NIT). Applied: `if not (math.isfinite(v) and d <= half + bound)`, with `d = inf` kept for the median.
- **F5** (NIT). Applied: two blank lines before the BACKEND extension's comment.
- **F6** (NIT). Applied: `_decoder`'s docstring names the BUILD's second site check of 2026-11-16, on the A100 pod.
- **F7** (NIT). Applied: R6 reads "retargeted by the box answers of 2026-11-18, §2 item 4, not dropped". The command's
  opening cites the box answers (§2 items 4–5) and the corpus answers (§5.5).
- **F8** (NIT). Applied: `main()` is driven on six argv lists under `redirect_stderr`. Each must exit 2 with its
  message:
  - render-ids-iv without its options;
  - render-ids-iv with `--resume`, and with `--smoke 0`;
  - `hashes --root ""`;
  - backend-ext with `--out`;
  - a `--ruling` with no `=`.

  This kills M8–M10.
- **F9** (NIT). Applied: the stage-only options are listed by `is not None` (`--root`, `--report`, `--smoke`) and by
  truth (`--resume`, `--ruling`). `--smoke 0` and `--root ""` are now refused for any other command.
- **F10** (NIT). Applied. The self-test reads the characterization's committed artifact
  (`data/olmo/determinism_base_h100-sxm.json`, its sha256 pinned as `1dd9199f…d3c1`) and requires its provenance to
  equal `CHARACTERIZED_PROVENANCE` field for field. It also requires the raw's BOX line to begin with
  `# BOX: pod emw1e4embiwe9b `. The `--selftest` docstring lists the files the self-test reads. This kills M5 and M6.

**Mutants** — each now has its killing test: M1 and M2 (F1), M3 and M4 (F3), M5 and M6 (F10), M7, and M8–M10 (F8).
M7 is killed by the pod refusal's text, which must name `emw1e4embiwe9b` and `d5d08fa`. The mutants themselves were
not run.

**Observations** (for the seat; noted):
- **O1.** Item 7's conventions for the entry: the even-count median is the mean of the middle two; a non-finite value
  enters as +inf; six significant digits, in nats.
- **O2.** At small k a smoke prints per-session figures. The smoke is never of record; whether §5.5's "nothing per
  session" covers it is the seat's call, and the planned smoke is k = 2.
- **O3.** A wrong re-pin fails closed. The reviewer read the H100 smoke as R6's first run on hardware. R6 had run on
  the A100 on 2026-11-16 and refused before the load; the H100 smoke is the first in which its bridge held (the STOP
  of `0eb7671`, §4).
- **O4.** `rendering_id` is now the (i)–(iv) manifest, `fdf73d85…ef38`, and the box's checkout must be at or after
  `b523f6a`. The box script v2 asserts `d5d08fa`.
- **O5.** The likely outcome on a box other than BK's is 0 of 40 for every candidate, and the seat rules on the four
  counts and the four medians.
- **O6.** The citations name the box answers and the corpus answers by role. Both files are committed at `26cf7d2`.

## 2. The report as returned

```text
**Blind review: `scripts/n_sessions.py` V2C (item 7, the re-pin, the merge)**

**Files.**
- V1 = `<scratch>/step4/scripts/n_sessions.py`, sha256 64cf6ee1…16cb.
- v2pre = `<scratch>/step4b/n_sessions.v2pre.py`, sha256 6a434948…259a.
- V2C = `<scratch>/step4b/n_sessions.v2c.py`, sha256 491584aa…c63d.
- base = `<scratch>/step4/n_sessions.base.py`, sha256 aa0b5404…e05f. It is 83a50a0's driver.
- HEAD = `<repo>/scripts/n_sessions.py` at b523f6a (git blob 4922c09). The working copy is identical to HEAD.

Line numbers are V2C's unless another file is named.

**Method.**
- Read-only commands only: diff, cmp, grep, sed, awk, wc, od, shasum, and git log/show/diff/grep/ls-files/rev-parse, plus `git status --porcelain` on two named paths.
- No Python was run and no file was written.
- The one path carrying a guard marker (data/olmo/) was reached by cd plus a glob.
- For the hand hash in item 3 below, the adapter's name was assembled in the shell from single letters, so no argv carried a marker.
- One `git diff --stat` ran over valence_core/n/, which is outside every ckpt and reports directory.
- Nothing under data/mf3, data/*/ckpt or data/*/reports was listed, read or searched.

## What checks out (no finding)

**1. The merge.** By tool, V2C = HEAD + V1's change + item 7 + the re-pin.
- The changed lines of diff(base→HEAD) equal those of diff(v2pre→V2C), except for:
  - the re-pin's eight lines (:79, :400–403, :406, :411, :801);
  - one check string re-wrapped at :1046–1047, its text unchanged;
  - the `choices` line split across :1247–1248;
  - two lost blank lines (F5).
- Byte-for-byte equal to HEAD:
  - V2C:305–383 = HEAD:251–329;
  - V2C:178–239 = HEAD:127–188;
  - V2C:25–35 = HEAD:25–35.
- V1→v2pre is item 7 alone, so V1's backend-ext lines stand in V2C unchanged apart from item 7 and the re-pin.
- The bext self-test call (:240–245) sits inside the temp-dir block and after HEAD's render-ids-iv checks. HEAD's "tokenizer libraries not yet imported" check is therefore unaffected.
- main() offers and dispatches all five commands.
  - The stage-only refusal (:1262–1265) covers render-ids-iv.
  - backend-ext still refuses the folder options.
- The file has no conflict markers, tabs, CRs or trailing whitespace, and no line over 120 characters.
- HEAD's ids.py moved MANIFEST_OF_RECORD to the (i)–(iv) manifest, fdf73d85…ef38. The merged code still fits HEAD's package:
  - `verify.verify`, `ids.ids_of` and `ids.label_ids` keep their signatures;
  - the flow test's stand-in uses that constant (see O4).

**2. Item 7 against §5.5.**
- Per candidate, `count` is as before. `median_abs_diff` is `statistics.median` of |v − BK's value| over both labels of every floor session passed in: 80 values at 40 sessions. BK's half unit and the bound stay out of it.
- `counts_line` prints only "name count/n, median x" per candidate, under a header naming n and 2n. It prints no value, no margin and no per-session figure, and nothing is written.
- `convention_line` keys on `v["count"] == n_floor`. Exactly one candidate at n of n names the convention; otherwise the line sends it "to the seat with the four counts and the four medians".
- Every caller of `label_counts` and `convention_line` is updated. The driver is their only user (git grep over the tree with data excluded), and no tool parses the printed lines.
- A non-finite vanilla value enters as +inf and never matches.
- The B/C known answer (1/32) pins `statistics.median`'s even-count convention: median_low or median_high would give 0 or 1/16.

**3. The re-pin.**
- V2C:404–410 equals, token for token (42 tokens: 15 keys, 6 library versions, every value):
  - the raw's printed block (results/raw/2026-11-18_respawn_determinism.txt:11–37);
  - the provenance block of the committed artifact data/olmo/determinism_base_h100-sxm.json (sha256 1dd9199f…d3c1, as raw :8 records).
- Against V1's literal, only `gpu` and `capability` changed. Those are the two fields the raw's own check lists at :78.
- I recomputed m's identifier by hand: sha256 of the sort_keys, compact-separator JSON, without `path` and `seed` (resume.py:147, :239–245).
  - V2C's literal gives 4ed3f2c70fe8afbf.
  - V1's literal, as a control, gives 641ee466f4553b6a.
  - So the R6 known answer (:963–965) will pass, and it binds every hashed field to the identifier.
- CHARACTERIZED_POD (emw1e4embiwe9b) is the raw's pod (:1–2).
- d5d08fa is the commit of the raw and of the BACKEND entry. The docstring (:79), the comment (:400–402) and the refusal (:801) all cite it.
- No reference remains in V2C to 7ab4d2f, m43y3deb1gq3rp, 641ee466f4553b6a, "A100" or the 2026-11-15 raw.
- Unchanged code underneath:
  - valence_core/adapters/ and resume.py since 7ab4d2f;
  - the n package since b523f6a;
  - the model manifest since 9662468.

## Findings

**F1 — RISK (low).** :1043–1048 (the check); :637–649 (the code).
- **What is wrong:** the median's known answer cannot tell the median from the mean, or every session from one session.
- **Evidence:**
  - `testing.toy_session` gives every toy session the same cues: "Zone W6" and "Zone H0" (valence_core/n/testing.py:106).
  - So B's and C's six differences are one 1/16 and one 0 per session. The median, the mean, the midrange and any single session's median are all 1/32.
  - The check's name claims "over both labels and every session (§5.5)". Only "both labels" is tested, and §5.5's "the 40 floor sessions" is not.
- **Fix:** add a second known answer with offsets that differ per session.
  - Score candidate A against `table`, with BK's values moved +3, +1 and 0 nats (both labels) on tss[0], tss[1] and tss[2].
  - Sorted, the differences are 0, 0, 1, 1, 3, 3, so the median is exactly 1.0.
  - The mutants give other values: the mean 4/3, the midrange 1.5, the first session alone 3.0, the last session alone 0.0.
  - The count at bound 0 is 1.
  - This kills M1 and M2.

**F2 — RISK.** :519–538, :773–857.
- **What is wrong:** nothing in the driver enforces the box answers' §2 item 5 order ("committed by path before step 4's run of record"). Nothing in the stage's report or records would show a breach either.
- **Evidence:**
  - The stage identity binds valence_core/n through `package_sha256`.
  - It binds the valence_core modules outside n through `guard.closure_from_modules` (valence_core/n/guard.py:48–63).
  - It does not bind scripts/n_sessions.py. That file holds CHARACTERIZED_*, R1's key, the plan and the comparison.
  - A run of record from the smoke's overlay, or from an edited copy, would write records and a report under the same identity as the committed driver's.
  - The gap is pre-existing in V1; the re-pin's required order makes it matter.
  - m's driver has one form for this: `driver_problems` (scripts/m_sessions.py:983, via `stages._committed`). At :508–516 it refuses an uncommitted driver and prints a DRIVER line before the load. Whether n adopts that form is for Code or the seat to decide.
- **Fix:**
  - In the run-of-record branch, before G-VER, refuse unless this file's bytes equal `git show HEAD:scripts/n_sessions.py`. That is `weights_of_record`'s form.
  - Print `DRIVER scripts/n_sessions.py <sha256>: committed at HEAD <head>`.
  - A smoke prints the sha256, marked unchecked.
  - A BextEnv seam for the bytes keeps the check testable.

**F3 — NIT.** :681–683; the checks at :1072–1075, :1161–1165, :1199–1202.
- **What is wrong:** the printed median's precision and the header's value count are not pinned by any test.
- **Evidence:**
  - The exact-text check uses medians 0.0 and 2.5, which print the same at .2g, .3g and g.
  - Only n_floor 40 is checked for "over its 80 values". The flow and smoke checks never read the header.
- **Fix:**
  - Put a median such as 0.0123456789 in `one`, expecting "median 0.0123457".
  - Require "over its 48 values" in the flow check and "over its 4 values" in the smoke check.
  - This kills M3 and M4.

**F4 — NIT.** :644–647.
- **What is wrong:** V1 refused a non-finite value explicitly (`math.isfinite(v) and …`). V2C maps it to inf and relies on `inf <= half + bound` being False.
- **Evidence:** on the stage's path the bound (a max over finite fidelity values) and BK's half unit are both finite, so behaviour is unchanged. But "a non-finite value never matches" now depends on that.
- **Fix:** `if not (math.isfinite(v) and d <= half + bound): ok = False`, keeping `d = inf` for the median.

**F5 — NIT (merge).** :383–384.
- **What is wrong:** there are no blank lines between `cmd_render_ids_iv`'s last line and the "# --- the BACKEND extension" comment.
- **Evidence:**
  - HEAD has two blank lines after the function, and V1 has two before the comment.
  - The merge put HEAD's block between V1's two blank lines and the comment, so both now precede `def _e0_corpus`.
  - The effect is cosmetic (PEP 8 E305).
- **Fix:** insert two blank lines before the comment.

**F6 — NIT (stale reference).** :417.
- **What is wrong:** `_decoder`'s docstring says "gver-trial's form, which PASSed at the box". After the re-pin, "the box" in this file means n's H100 pod.
- **Evidence:** that PASS was on the A100 pod, at the BUILD's second site check of 2026-11-16 (results/raw/2026-11-16_n-build_sitecheck2_out.txt:46, :62; RESULTS.md:629).
- **Fix:** "which PASSed at the BUILD's second site check (2026-11-16, the A100 pod)".

**F7 — NIT.** :65, :77–82, and :36–39.
- **What is wrong:** R6 still stands among "Code's readings … pending the seat", and the backend-ext entry's authority line cites only the 2026-11-16 answers.
- **Evidence:** the box answers' §2 item 4 ruled on R6: "R6 is retargeted … it is not dropped". The comment at :402 says this; the readings list does not.
- **Fix:**
  - add "(retargeted by the box answers of 2026-11-18, §2 item 4)" to R6;
  - add that citation to the entry's opening at :36–39.

**F8 — NIT (merge).** :1244–1293.
- **What is wrong:** no self-test exercises main().
- **Evidence:** any of the following merge errors would pass the self-test:
  - dropping "render-ids-iv" or "backend-ext" from `choices`;
  - dropping either dispatch block;
  - exempting render-ids-iv from the stage-only refusal.

  I checked all of these by reading only.
- **Fix:** call main() on argv lists under `contextlib.redirect_stderr`, expecting SystemExit 2 and these messages:
  - `["render-ids-iv"]` → "render-ids-iv needs";
  - `["render-ids-iv", "--resume", "--tokenizer-dir", t, "--out", o, "--pi-date", d]` → "backend-ext's options only";
  - `["backend-ext", "--out", o]` → "takes no folder options".

  This kills M8–M10.

**F9 — NIT.** :1262–1265.
- **What is wrong:** falsy stage options pass the stage-only refusal.
- **Evidence:**
  - `--smoke 0`, `--root ""` and `--report ""` are not listed by `if v`.
  - So `render-ids-iv --smoke 0 …`, and every other non-backend-ext command, runs with the option silently ignored.
  - The gap is pre-existing in V1; the merge extends it to render-ids-iv.
- **Fix:** list the options by `a.root is not None`, `a.report is not None` and `a.smoke is not None`.

**F10 — NIT.** :403–411, :963–965.
- **What is wrong:** some of the re-pin's literals are bound by nothing:
  - CHARACTERIZED_POD;
  - `path` and `seed`, the two fields `backend_identifier` drops;
  - and an edit of `gpu` (or `capability`) made together with the identifier also passes.

  So the comment's claim ("the provenance its raw prints") is unchecked.
- **Evidence:** the known answer binds only the hashed fields to the identifier. All of these errors either fail closed on the box or have no effect.
- **Fix:**
  - in the self-test, read data/olmo/determinism_base_h100-sxm.json with its sha256 pinned, and require its provenance == CHARACTERIZED_PROVENANCE;
  - require the raw's BOX line (:2) to name CHARACTERIZED_POD;
  - add the two files to the `--selftest` docstring's list of what it reads.

  This kills M5 and M6.

## Surviving mutants

Each is a one-line change in the delta that the self-test passes, by my reading.

- **M1** — :649 `statistics.median(diffs)` → `statistics.mean(diffs)` (or `fmean`, or `max(diffs) / 2`). Killed by F1's offsets test (1.0 against 4/3 or 1.5).
- **M2** — :640 `ok = True` → `ok, diffs = True, []`, so the median covers only the last session's two values. Killed by F1's offsets test (1.0 against 0.0).
- **M3** — :683 `:.6g` → `:.2g` (or `:.3g`, `:g`). Killed by F3's 0.0123456789 → "median 0.0123457".
- **M4** — :682 `{2 * n_floor}` → `80`. Killed by F3's "over its 48 values" in the flow check.
- **M5** — :403 CHARACTERIZED_POD → any other id. Every check uses the constant on both sides. Killed by F10's raw-line check. It would fail closed on the box.
- **M6** — :405 `"path"` or :407 `"seed"` → any value (both are in BACKEND_DROP). Killed by F10's artifact check. It has no effect at run time.
- **M7** — :801 "the BACKEND entry d5d08fa" → "7ab4d2f". The refusal checks only test for SystemExit. Killed by asserting that the "a pod that is not the characterized one" refusal names d5d08fa and CHARACTERIZED_POD.
- **M8** — :1248 drop "render-ids-iv" (or "backend-ext") from `choices`. Killed by F8.
- **M9** — :1282 `"render-ids-iv"` → `"render-ids_iv"`. The dispatch block goes dead and the command falls through to print_help with exit 2. Killed by F8.
- **M10** — :1264 `a.command != "backend-ext"` → `a.command not in ("backend-ext", "render-ids-iv")`. Killed by F8.

**Killed by existing checks (my reading):**

| Mutant | Killed by |
|---|---|
| `median` → `median_low` / `median_high` | B/C median 1/32, against 0 or 1/16 |
| median over the S differences only | B's median 1/16 |
| `d = abs(v - ref)` with no isfinite guard | NaN case: the median is NaN, not inf |
| `else 0.0` for a non-finite value | NaN case: count 3, not 0 |
| `len(full) == 1` → `>= 1` | the two-at-40 case |
| `counts_line`'s "; " → ", " | the exact-text check |
| any hashed field of the literal, or the identifier | the R6 known answer |
| `counts_line(counts, len(floor))` → `len(ss)` | the smoke's "bare 2/2, median " |
| `v["count"] == n_floor` → `== 40` | the flow test's last line |

## Observations for the design seat

**O1 — Item 7's conventions that §5.5 leaves open, for the entry.**
- The median of an even count is the mean of the 40th and 41st sorted values (`statistics.median`; the self-test pins this).
- A non-finite vanilla value enters as +inf, so a median is infinite only if at least 40 of the 80 values are non-finite.
- Medians print to 6 significant digits, in nats.

**O2 — Smokes print per-session figures.**
- A smoke's comparison runs over the first k floor sessions.
- At k = 1, each candidate's median is the mean of one session's two differences, and its count is that session's match. Those are per-session figures, and they land in the smoke's raw.
- §5.5's "nothing per session" binds the stage. It is the seat's call whether a smoke (never of record) is exempt, or should print counts only below some k.

**O3 — A wrong re-pin fails closed.**
- A pod or identifier that is not the box's refuses before the load. The cost is a lost box session, never a wrong record.
- As far as the committed record shows, R6's bridge has never run on hardware:
  - the A100 failed CUDA initialization (error 802) on 2026-11-16 and has not run since;
  - d5d08fa's entry lists the extension as next (RESULTS.md :133–135, :320–353).
- So the H100 smoke is R6's first test on real hardware. If `environment_provenance` differs from the adapter's own provenance, the stage will refuse there, either before the load or just after it.

**O4 — The merge changes the stage identity's `rendering_id`.**
- `rendering_id` is `loaded["manifest_sha256"]`. It is now the (i)–(iv) manifest fdf73d85…ef38 (HEAD's `ids.MANIFEST_OF_RECORD`), not V1's (i)–(iii) 7f51bd91…821d.
- `ids.load` now also reads the two (iv) files.
- The box checkout must be at or after b523f6a, or the stage refuses ("not the render of record's").
- The entry should name the new digest.

**O5 — Expected outcome, as in V1's review.**
- On a box other than BK's, the tolerance is BK's half unit (about 5e-16) plus a per-label bound that is 0.0 if cached and fresh agree bitwise.
- That will likely give 0 of 40 for every candidate, so the stage goes to the seat with the four counts and the four medians. That is the case §5.5 added the medians for.

**O6 — Which "answers of 2026-11-18".**
- Two seat files of 2026-11-18 were committed at 26cf7d2. The driver says "the seat's answers" for the corpus answers (§5.5, §3 item 3) and "the box answers" for the box file.
- §5.5 exists only in the corpus answers, so every citation resolves. Naming the file once would remove the reliance on section numbers.

## Totals

- 0 BUG, 2 RISK (F1, F2), 8 NIT (F3–F10).
- 10 surviving one-line mutants (M1–M10), each with a test that would kill it; 9 further mutants killed by existing checks.
- The merge kept both sides intact apart from two blank lines. Item 7 and the re-pin match their specifications.
```
