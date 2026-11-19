# n — the schema follow-up's blind review: the `fidelity-ceiling` kind, the fidelity rule's alpha, ceiling and median rel, and the counter, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over the change's four files:
- from HEAD's files at `9f64305`, where all four are as `732a58f` left them: `valence_core/n/schema.py`,
  `valence_core/n/runner.py`, `valence_core/n/primitive.py` and `scripts/n_sessions.py`;
- to the second draft: `schema.py` `fdfc8466…4e97`, `runner.py` `10a33707…fabe`, `primitive.py` `56d6c509…e735` and
  `n_sessions.py` `94209826…3a32`;
- and the first draft's fix: the first draft's `runner.py` (`c615681c…f1ec`, whose self-test ran 400/403) to the
  second's.

**The reviewer's brief** (`c6505851…6cca`, 90 lines):
- gave the files, the `git diff --no-index` form for both deltas, and the specification:
  - ADDENDUM-n2 §1.1, §2.1, §2.2, §3 and §6.3 (3);
  - the seat's answers of 2026-11-18, fourth sitting, §4 and §5;
  - the form agreed with n-analyzer, in substance;
  - Code's two readings for the seat;
  - the constraint that `scripts/n_analyze.py` does not change;
  - the self-test's counts: 404/404, and the first draft's 400/403 with its output;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, that a glob is expanded and read before it is looped over, and the `rev-parse` form for a
  tracked-and-clean check;
- barred any interpreter, any write, any network, any guard marker in an argv, anything under `data/mf3`, any read,
  listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the six files it named (no
  listing, `find`, `grep` or glob there).

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (133 lines, sha256
`dc822457…2ea0`). It names no local path. Its line numbers in the TO files are the second draft's: the folder it
calls `S/step4b/schema/draft/` held that draft when it read it, and Code's scratch keeps those bytes, unchanged, as
the reviewed drafts; the committed files are the third draft's.

**Totals:** 0 BUG, 5 RISK, 3 NIT, 7 surviving one-line mutants, and 9 observations.

## 1. Dispositions

Every applied disposition is in the third draft's bytes: `schema.py` `5cbf60db…574c`, `runner.py` `e8e81ab0…f787`,
`primitive.py` `dca64c0f…8a2a` and `n_sessions.py` `e284a9f2…32b6`. They ran 409/409 in a battery window the
coordinating session granted for them, and the self-test raw holds the run.

- **F1** (RISK; the alpha refusal untested): applied. `runner.py`'s self-test runs a stage whose identity's alpha is
  0.05 under inputs of 0.01: it is refused before any read, with nothing written. This kills M3.
- **F2** (RISK; the ceiling's boundary and reach): applied. Three checks:
  - a discordance of exactly 0.25 (|2.125 − 1.875|) fires nothing;
  - a keyed-sample and a timing re-computation above C each fire it;
  - the optional case: a resume through a ruled `fidelity-ceiling` pause. The pause is reproduced on replay and
    adjudicated, and the next steered re-computation above C pauses again, with the counter at 2.
  These kill M1 and M2.
- **F3** (RISK; the identity check's `<=` unpinned): applied. The schema accepts a d = 0 read whose absdiff equals the
  bound, 0.25, and the primitive reads the shadow under a bound of 0.0 and finds it within. These kill M6 and M7.
- **F4** (RISK; one-sided tests): applied. The schema refuses a bound of 0.25 under a ceiling of 0.3 and accepts a
  median rel of 0.0. These kill M4 and M5.
- **F5** (RISK; p0_count of at least 1 after the lock): not applied. It is outside the form agreed with n-analyzer
  ("p0 stays p0_count and p0_n"), and it would move n-analyzer's fixtures. The coordinating session: "F5: not in this
  commit, as you propose. It's outside the agreed form and would move n-analyzer's fixtures. Carry it to LOCK-n v0.1's
  list for the seat, and tell n-analyzer." Carried, and n-analyzer is told.
- **F6** (NIT; docstrings): applied:
  - in `schema.py`: the IDENTITY paragraph (ADDENDUM-n2 §2.2, the inclusive bound, what backend-ext measures), the
    identity check's `bound` field, and `example_identity`'s docstring;
  - in `runner.py`: the comment on `StageInputs.alpha`;
  - in `n_sessions.py`: the backend-ext identity check's name, and a paragraph on why the two stages can no longer be
    resumed or re-printed.
- **F7** (NIT; the median rel's floor is Code's): declared, in the code's comment, in the entry and on LOCK-n v0.1's
  list; n-analyzer is told.
- **F8** (NIT; two names for the fidelity rule): applied. One name, `fr`.
- **M1–M7:** each is now killed by the check its finding names.
- **O1:** the three tests still test what they tested. The ceiling run's check now also asserts `also_fired == []` and
  `arms_in_scope == ["N1-V"]`. The guard that was lost with the bound of 0.0 is not restored: the schema requires the
  bound to equal the ceiling.
- **O2:** R10 reaches the committed cells as well as the reports. This is stated in `schema.py`'s new VERSIONS
  paragraph, in the driver's docstring and in the entry.
- **O3:** R11's precedent, which is already the entry's ground.
- **O4:** for n-analyzer; relayed with the sha.
- **O5:** noted in the entry. hftiny's box-only identity (bound 1e-3) is never checked against the stage-identity
  rules, and the box's next self-test, at G-VEC's launch, is its first run under this schema. The coordinating
  session: "O5: note it in the entry. State the box's expected self-test count after this commit (your laptop 409 plus
  the box-only HF cases), so G-VEC's launch files can require it exactly." By arithmetic, 420.
- **O6:** R12, declared in `runner.py`'s docstring and in the entry, and carried to LOCK-n v0.1's list: the batch
  nests, §4 describes per-evaluation counts, and the lock states which form binds. The citation now stands in a
  sentence of its own, on alpha's value, followed by the reading that the evaluations nest and that LOCK-n states
  which form binds. The coordinating session: "F7, R10 and R12–R14: as declared, Code's readings in the entry and on
  the lock's list. R12 especially, since it is how alpha's per-evaluation count reads against nested batches."
- **O7:** noted in `runner.py`'s docstring. Where the bound is C, a finite d = 0 read above it fires
  `fidelity-ceiling` first and `identity-bound` after it.
- **O8:** R13 and R14, declared in `runner.py`'s docstring and in the entry, and carried to the lock's list.
- **O9:** left; the two lines are harmless.
- **The reviewer's departures** are in the entry's departures, for the seat to class.

## 2. The report as returned

```text
BLIND REVIEW — n schema follow-up (fidelity-ceiling, alpha, ceiling, median rel, counter, batch alpha)

I checked the inputs first. The five scratch files hash to the given sha256s: S/step4b/schema/draft/{schema,runner,primitive,n_sessions}.py and S/step4b/schema/draft1_runner.py. The four FROM files and valence_core/n/hftiny.py are tracked and clean at HEAD 9f64305 (rev-parse equals hash-object). I got the deltas with `git diff --no-index -U3`, read the TO files in full where they change, and read ADDENDUM-n2 v0.1 and the fourth-sitting answers in full.

**Conformance to the agreed form.** Every item is present:
- PAUSE_KINDS at schema.py:1115.
- fidelity_rule.alpha, ceiling and median_rel: tables at schema.py:486-491, checks at :835-845.
- identity_bound == ceiling: schema.py:846-848.
- Batch alpha == the identity's: schema.py:1452.
- The counter, null exactly where no ceiling is set: schema.py:1198-1201 and :1503-1508; runner.py:363.
- example_identity values: schema.py:1605-1608.
- Runner fire: runner.py:194-197, in PAUSE_KINDS order. Alpha refusal: runner.py:381-383.
- Driver identity: n_sessions.py:597-599.

I found no BUG.

---

FINDINGS

F1 — RISK — runner.py:381-383. The alpha refusal the agreed form requires has no test anywhere. Every StageInputs carries alpha 0.01, equal to its identity's: runner.py:719 (inputs_for) and n_sessions.py:1083. Deleting or weakening the guard passes 404/404 (M3). Without it, a mismatched alpha is caught only if a batch fires, and then only at the end, by check_report, after the reads are on disk and with no report written.
Fix: in runner._selftest, `chk("runner: a stage whose inputs' alpha is not its identity's fidelity_rule.alpha is refused before any read", refused(lambda: run(inputs_for("alpha", identity=dict(ident, fidelity_rule=dict(ident["fidelity_rule"], alpha=0.05))), plan, resume=False)) and not (tmp / "alpha").exists(), "")`.

F2 — RISK — runner.py:194-197. Two parts of the ceiling rule are untested:
- The boundary: ADDENDUM-n2 §2.1 says "above C". The checks use discordances of 0.5, 0.2 and about 2 nats, never exactly C (M1).
- The reach, "on every re-computed read, at any dose": every ceiling check uses a dose-rule re-computation (+1 or d = 0). None uses a keyed "sample" or a G-TIME-n "timing" one (M2).
- Also untested: a resume through an adjudicated fidelity-ceiling pause. It rides the generic replay match at runner.py:440.
Fix: `m6.observe(rec_at(22, fresh_shift=0.25))[0] == []`. example_record's dyadic literals make the absdiff exactly 0.25 (margin 1.875, fresh margin 2.125). Add `Monitors(..., ceiling=0.25).observe(schema.example_record(ident0, "N1-R", "rand_05", "+1/2", 12, fidelity="sample", fresh_shift=0.5))[0] == ["fidelity-ceiling"]`. Optionally add a run → ruling → resume through rep_c.

F3 — RISK — primitive.py:261 and schema.py:1061 (both unchanged lines). The identity check's `<=` lost its only kill in this change.
- At HEAD, the example bound 0.0 met the test double's exact absdiff 0.0. That pinned `<=` through primitive.py's shadow check `{"bound": 0.0, "within": True}`, the schema's "N1-V 0" accept, and every runner small run.
- With the bound at 0.25, no record anywhere has absdiff == bound, so `<` now survives in both files (M6, M7).
- An exact tie is unlikely on the box, but "within at exactly C" is the seat's semantics and should stay pinned.
Fix: in the schema self-test, accept `example_record(ident, "N1-V", "none", "0", 3, fresh_shift=0.25)` (absdiff exactly 0.25 = bound, within True). In primitive._selftest, add one `read(..., identity_bound=0.0)` on the unbiased double, expecting `{"bound": 0.0, "within": True}`.

F4 — RISK — schema.py:846-848 and :844-845. The tests are one-sided:
- The only bound/ceiling mismatch refused has bound 0.3 above ceiling 0.25, so `!=`→`>` survives (M4).
- No median_rel of 0.0 is accepted, so `>= 0.0`→`> 0.0` survives (M5).
Fix: refuse identity_bound 0.25 with ceiling 0.3; accept median_rel 0.0.

F5 — RISK — schema.py:859, :1605, :1759. The PI adopted Laplace's rule, decision (n-3) (RESULTS.md:786): p0 = (k+1)/(n+2), so p0_count ≥ 1 after the lock.
- The schema still admits p0_count = 0 at the campaign and time stages.
- example_identity's campaign keeps BK's (0, 2400), and example_pause's batch does too.
- So every campaign-shaped test (schema, runner, and n-analyzer's battery) exercises the zero-base-rate form that §1.1 replaced. A lock that carried 0/2400 at the campaign would pass check_stage_identity.
This goes beyond the agreed form ("p0 stays p0_count and p0_n"), so it is for the seat and n-analyzer. Fix: refuse `p0_count < 1` where stage != "backend-ext"; make the example campaign p0 (1, 26) (k = 0 of 24); give example_pause's batch its identity's p0.

F6 — NIT — docstrings not carried along:
- schema.py:101-104 (the IDENTITY paragraph) still gives only n §2.1's "within the backend's measured nondeterminism", and "At backend-ext, which measures the bound". Under ADDENDUM-n2 §2.2 the bound is C; backend-ext measures the discordance C is derived from.
- schema.py:415 (`bound`) cites n §2.1 only; add ADDENDUM-n2 §2.2.
- schema.py:1585-1588 (example_identity's docstring) should add "ceiling and median rel null at backend-ext; alpha 0.01 at both".
- runner.py:259 `# the binomial's alpha (the lock's)` should say it must equal the identity's fidelity_rule.alpha and that run() refuses another.
- n_sessions.py:1172-1173: the check's name omits the alpha 0.01 and the null ceiling and median rel it now asserts.
- n_sessions.py:113-125: the backend-ext-2 text still reads as resumable. After this change, a resume or re-print of either committed stage is refused at :862 or :897 ("not a valid report"); see O2.

F7 — NIT — schema.py:844-845. The median_rel ≥ 0 refusal is Code's addition, not in the agreed form. n-analyzer inherits it at its pin move. Declare it in the entry.

F8 — NIT — schema.py:835 `fr0` and :858 `fr` name the same object; use one name.

---

SURVIVING MUTANTS (one line each; by my reading every check passes, laptop and box alike)

- M1 — runner.py:195: `f["absdiff"] > self.ceiling` → `>=`. Killed by F2's exact-0.25 check.
- M2 — runner.py:195: append `and f["reason"] == "dose-rule"`. Killed by F2's "sample" check.
- M3 — runner.py:381: `if float(inputs.alpha) != float(fr["alpha"]):` → `if False:` (or `>`). Killed by F1's check.
- M4 — schema.py:847: `identity["identity_bound"] != fr0["ceiling"]` → `>`. Killed by refusing bound 0.25 with ceiling 0.3.
- M5 — schema.py:844: `not fr0["median_rel"] >= 0.0` → `> 0.0`. Killed by accepting median_rel 0.0.
- M6 — schema.py:1061: `f["absdiff"] <= idc["bound"]` → `<`. Killed at HEAD; survives now. Killed by F3's schema accept.
- M7 — primitive.py:261: `a <= identity_bound` → `a < identity_bound`. Killed at HEAD by the bound-0.0 shadow check and the runner's small runs; survives now. Killed by F3's identity_bound=0.0 read.

The other mutants I tried are killed, among them:
- the counter always an int (the driver's backend-ext flow writes a null-counter report that check_report would refuse);
- the ceiling not passed to Monitors (rep_c and "ok");
- a dropped `absdiff is not None` guard (k_nf6);
- the ceiling appended after identity-bound (k_d0);
- a ceiling compared on rel instead of nats (k_c, rep_c);
- a changed BEXT_ALPHA (n_sessions.py:1179 asserts the literal 0.01).

---

OBSERVATIONS

O1 — The draft-1 runner fix (S/step4b/schema/draft1_runner.py → S/step4b/schema/draft/runner.py). All three failed checks still test what they were written to test. Their assertions are byte-identical to HEAD's; only the identities changed.
- The +2.0 bias on logit 9 of every fresh row at steered reads gives a margin discordance of 2 − L₂(S) + L₂(U), where L = log(1 + p₉(e²−1)) ∈ [0, 2). So it is always below 4 nats, and the ceiling of 10.0 in ident4 and ident_hi can never fire.
- "binomial fire at a cadence point" (runner.py:814-819) again fires at read 3 on N1-P and N1-V.
- "an exceedance short of the cadence" (:920-926) again fires read-less at the run's end, n = 4.
- "after its ruling…" (:929-933) resumes the same stage under the same identity, as its sha check requires.
- The identity bound moves with the ceiling only because the schema now requires them equal. The shadows are unbiased (`if injections:`), so the move is inert.
- One incidental guard is lost: at HEAD, bound 0.0 meant these runs would have shown a bias leaking into a shadow, since identity-bound would fire first; at 10.0 they would not.
- The new rep_c check (:913-919) restores the ceiling's run-level case. It does not assert also_fired == [] or arms_in_scope.

O2 — Code's reading (4)(i), no version marker, reaches further than reports.
- cells.load_cell → check_cell (valence_core/n/cells.py:148) → check_stage_identity will also refuse the committed backend-ext and backend-ext-2 cells. Their embedded fidelity_rule lacks alpha, ceiling and median_rel. I know this from the code; I read no ckpt or report file.
- "n-report-v1" and "n-cell-v1" now each name two shapes, and only the identity's package_sha256 tells them apart.
- Consequences: the figures of record stand as printed at 9f64305. Re-deriving them from the committed cell, or resuming or re-printing either stage, needs the package from 9f64305's tree.
- I find the reading defensible (n_analyze binds the schema by sha256). One docstring sentence stating it would close it; a v2 bump would only make the refusal's message clearer.

O3 — Code's reading (4)(ii), the counter null where no ceiling is set, follows the module's own precedent: label_mass_below_floor is null where no floor is set. It is implemented at schema.py:1503-1505 and runner.py:363 and tested both ways (schema.py:2362-2367).

O4 — For n-analyzer at its pin move. scripts/n_analyze.py pins 0ea39600…, which is HEAD's schema and is unchanged here.
- `_bt_report_for`'s counters (:4243-4246) lack fidelity_ceiling_exceeded, so its battery's check_report calls will refuse.
- Battery case F14 (:3931-3961) relies on "the identity bound 0": d = 0 shifts of 0.01 and 1e-9 counted as "identity bound exceeded == 2". Under the bound of 0.25 both reads are within. Any d = 0 shift that exceeds the bound now also exceeds the ceiling.
- §6.3 (4)'s reader check for the new kind is still to come, like :5440's identity-bound check: a fidelity-ceiling pause's read carries a re-computation whose absdiff exceeds the ceiling.

O5 — valence_core/n/hftiny.py:102-103 (unchanged, runs on the box only) builds `dict(test_identity(...), identity_bound=1e-3)`.
- Under the TO schema that identity breaks two rules: its ceiling stays 0.25 ≠ 1e-3, and 1e-3 is below the 0.25 floor. check_stage_identity would refuse it.
- It passes only because hftiny calls check_record, which does not re-check the stage identity.
- It has not run under the TO files (skipped on the laptop). It is expected to pass on the box, but it exercises an identity no valid stage can hold.

O6 — Pre-existing, not introduced here. The fourth sitting §4 describes each evaluation as "the count above TAU in the evaluation's reads", with a family-wise rate of 1 − 0.99^E and "an evaluation of 160 reads fires at 13 or more".
- The runner's batch is cumulative since the last adjudicated fire (runner.py:33-44), so the evaluations are nested, not disjoint windows.
- Now that p0 > 0 makes alpha decisive, the two forms differ in power and in the family-wise rate.
- The delta places §4's citation inside that PIN sentence (:38-40), which could read as a ruling on the batch form. LOCK-n should pin which form applies.

O7 — How the new kind sits beside the old ones:
- With bound == C, a finite d = 0 read above C always fires fidelity-ceiling first. So identity-bound is never a pause's kind at the campaign or G-TIME-n, only an also_fired entry.
- fidelity-ceiling's place relative to nonfinite cannot be observed: a non-finite read has no absdiff, so the two never fire together, and any mutant swapping them is equivalent.

O8 — Two implicit readings for the seat:
- The ceiling binds at G-TIME-n too: it is non-null at every stage but backend-ext (schema.py:836-838), so a "timing" re-computation above C pauses G-TIME-n.
- A ceiling ruling clears nothing in the binomial: the read above C stays in the batch (clear_batch runs only on a binomial fire, runner.py:443-444).

O9 — runner.py:406-407 is now unreachable. Three earlier checks already force the prior report's alpha to equal the stage's: the identity sha check at :322, schema.py:1452, and :381. It is harmless.

---

DEPARTURES

1. Five `/usr/bin/grep -n` runs, each over a single named TO file in S: primitive.py once, runner.py once, n_sessions.py three times. No recursion, glob or other file. Your rule says "no grep" in S; each read only a file I was allowed to read in full.
2. Three `git grep` commands used a narrower positive pathspec in place of `.`, each with all three exclusions (':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'): 'valence_core/n/*.py'; 'scripts/*.py' with 'valence_core/**/*.py'; 'RESULTS.md' with 'results/raw/*.md'.

Nothing else. No interpreter, no write, no network, no marker in any argv, nothing under data/mf3, ckpt or reports touched.

```
