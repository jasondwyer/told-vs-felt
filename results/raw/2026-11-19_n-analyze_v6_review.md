# n_analyze.py, the seat's ruling of 2026-11-18 (third sitting) on PIN-n-37 and ADDENDUM-n2's ceiling kind and second sensitivity row: the blind review, its mutants and the dispositions (PI date 2026-11-19)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's ruling of the third sitting and ADDENDUM-n2
carried in`.

- **What changed under review.** The draft is compared against the committed analyzer (`bfc869f`, sha256
  `3d22da1d…d048`). It carries:
  - §6 of the seat's answers of the third sitting,
    `results/raw/2026-11-18_n-step4-run-pause_design-to-code_answers.md` (sha256 `d51279ec…0bf4`, committed at
    `3b2b855`): PIN-n-37 amended to the conservative form;
  - ADDENDUM-n2 v0.1 (`41f76c49…bb3f`, committed at `7a54eb9`) §2.1 and §3, the `fidelity-ceiling` kind and the
    second sensitivity row, with the addendum bound by sha256 (PIN-n-38, PIN-n-39);
  - the schema pin moved to n-build's follow-up at `003ae7d` (`5cbf60db…574c`), whose names the seat's fourth sitting
    accepted (`results/raw/2026-11-18_n-step4-resume_design-to-code_answers.md` §5).

  It was drafted in one step and run in a battery window the coordinating session granted: 227/227 (d1).
- **The review, blind** (§1). A reviewer read that draft, frozen as a read-only copy at sha256 `0e459d7d…fddc` (227/227
  on those bytes, every one of its 230 coverage ids reached).
  - It was a subagent of this session. Its brief (sha256 `b0079a19…2323`) quoted the list of record v2's items 1–5 with
    item 4's two amendments (C.2 of 2026-11-16, and the fourth sitting's §6.2), the standing lines (item 3's pathspec
    with `':!data/mf3/**'`, even for a named file; a glob expanded and read before it is looped over; no listing of
    `results/raw`; a tracked-and-clean check by `rev-parse` against `hash-object`), and it allowed no interpreter.
  - Its specification: the third sitting's §6 and §8 item 5, and the PI's routing of it; the entry of `bfc869f`, for
    what the seat ruled on; ADDENDUM-n2 §2.1, §2.2, §3 and §6.3 (4); the second sitting's §1.4 and §3.1; the fourth
    sitting's §4 and §5; PROPOSAL-n v0.2 §2.1, §4 (f), §5 and §6; `valence_core/n/schema.py` and
    `valence_core/n/runner.py` at `003ae7d`.
  - It executed no code. It read files, ran `shasum`, `wc -l`, name-only `ls`, `/usr/bin/grep` inside named files, and
    git in the brief's tracked-and-clean form, and it wrote no file. Its report lists those commands, and it opened
    nothing under `data/`.
  - It returned:
    - production findings F1–F6: F1 and F2 MINOR, F3–F6 NOTEs, no MAJOR;
    - battery findings B1–B9: B1–B4 MINOR, B5–B9 NOTEs;
    - 35 mutants, V01–V35. It predicted that 14 would survive the frozen copy (V08, V11, V13, V14, V19, V22, V23,
      V24, V25, V26, V28, V29, V32 and V35), V11 as equivalent on runner reports.
- **The dispositions** (§2). Every finding is taken. F1 is kept, as PIN-n-37's reading (b), with the reviewer's
  scenario put to the seat. F3's converse for the non-finite and identity-bound kinds is not applied, and is put to
  the seat. Everything else is applied. In the production code:
  - the guard flag is read at its points (F2, now PIN-n-37's reading (c));
  - the ceiling is bound both ways (F3);
  - the texts are changed (F4–F6).

  In the battery, three new checks (VD-SECOND-ROW-TRIGGER, VD-SECOND-ROW-PAUSE, VD-BATCH-CLEARS), new inputs and
  pinned figures (B1–B9).
- **The mutants** (§3). The set is the reviewer's 35, V35 re-expressed on the fixed draft's text, and ten of Code's
  (C08, C10, C11, C13, C18 and C23–C27). They ran once each, on the fixed draft (sha256 `b605b91f…4c2c`, 230/230, every
  one of its 233 coverage ids reached): **44 of 45 killed.** V11 survived, as the reviewer predicted: it is
  equivalent on runner reports. The other 13 it predicted would survive are killed, each by a check the dispositions
  added or extended.
- **The battery runs** (§4) and **the committed bytes** (§5). The committed file differs from the mutation-tested base
  in the repository line and, from the values-check, in seven texts (§5).
- **The tallies** (§6): unchanged from `bfc869f`'s, and so is the forms' digest.

Every Python run here was inside a battery window the coordinating session granted, on bytes named to it first by
sha256. Each ran as one process at a time, at `nice -n 19` with `-I`, with its temp folders in Code's scratch, in the
foreground. The interpreter was reached by `cd` into the venv's bin by glob, so no argv named its path. Nothing ran on
a model or on the box.

Each mutant was applied to a copy of its base as an exact text replacement (`.old` → `.new`), asserted to occur once
and to change the file. Before the mutants ran, the base's and the manifest's sha256 were named to the coordinating
session, which checked them. Each file was checked against that manifest before its battery ran with `--selftest`.
"Killed" means a non-zero exit.

## 1. The reviewer's report, as saved from its hand-back (unedited)

The report is reproduced whole, as the reviewer's hand-back message gave it, taken from the subagent's transcript by
script (sha256 `acdc099d…55cd` as saved). It names Code's scratch folder and the repository by description, as its
brief asked.

## Blind review of scripts/n_analyze.py, draft v6

**Inputs checked first.**
- The frozen copy's sha256 matched the one in the starting message: 0e459d7d…cfddc. The brief's matched too: b0079a19…2323.
- `ADDENDUM2_SHA256` equals the sha256 of the root file `ADDENDUM-n2-fidelity-on-the-box-of-record-v0_1.md` (41f76c49…bb3f). That file is tracked and clean at HEAD.
- `SCHEMA_SHA256` equals `valence_core/n/schema.py`'s sha256 (5cbf60db…574c).
- `schema.py` and `runner.py` at HEAD are the same blobs as at 003ae7d, and the working tree matches HEAD.

**Overall.** I found no MAJOR. There are 2 MINOR and 4 NOTE findings in the production code, and 4 MINOR and 5 NOTE findings in the battery. Of the 35 mutants, 14 are predicted to survive; one of those (V11) is equivalent on runner reports.

## What checks out

**PIN-n-37 as amended (`paused_points`, lines 5813–5843)**
- It implements §6's conservative form:
  - a binomial pause stands on every read launched in its range, re-computed or not;
  - a single-read pause stands on its read, and through a shadow on that session's reads;
  - the shadow extension also runs through any shadow inside a range, reaching N1-R only on floor sessions;
  - adjudicated pauses are skipped, and N4 is read per arm.
- I checked all 15 RD-PAUSE-POINTS cases by hand; each expectation is what the code returns.

**The draft's two readings**
- *Points read whatever the scope.* This matches §6 and is needed by it. The runner's SCOPE adds the paired arms only for a shadow that itself fired. So a batch whose range holds shadows has a narrower scope than §6's points. Example: a batch from the stage's start that fires at an N1-V +1 trial has scope [N1-V], while its points cover every steered arm. The reading contradicts the schema's sentence "A pause stands on the arms in its scope", but §6 is the later ruling. Its knock-on effects are in F2.
- *Range from the batch's first trial.* This matches §6's words ("the trials and the reads between them") and `BINOMIAL_FIELDS`. It is narrower than the runner's own batch; see F1.

**`report_problems`' binding** is still the runner's at 003ae7d:
- The replay calls `clear_batch` at every matched pause that has a batch (all are adjudicated by the time a resume runs) and at a reproduced end-of-run fire. A read-less adjudicated fire is always the last pause, so leaving it out of `cleared` is safe.
- R13: a ceiling ruling clears nothing, and `cleared` reads only pauses that carry a batch.
- R12: batches nest since the last clear, so `first_w` is the first trial after `cleared`. n, k and the scope agree with `Monitors`.
- VD-PAUSE-POINTS B pins "a non-binomial ruling clears nothing".

**The ceiling**
- `above_ceiling` is exactly `Monitors.observe`'s test: strict `>`, and false when absdiff or the ceiling is None.
- `report_counters` gives a null counter exactly where no ceiling is set, matching the schema and `runner._report`.
- The `counters` per-arm count is right, and `report_problems` compares the report's counter.
- The kind check reads `[kind] + also_fired`; the precedence itself (the ceiling directly after nonfinite) is `check_report`'s.
- `_bt_files` / `_bt_report_for` agree with the runner on strictness and nulls.

**The second row**
- `median_drop` is strict and null-safe, mirroring `tau4_drop`.
- `row_drops` counts drops as `build_state` makes them: a read's own re-computation, or for a steered read its shadow's; N4 by its own only.
- `over_half` is strict, and the trigger is §3's (more than half of an arm's reads at a point in the TAU/4 row), not "where it empties".
- The `emptied` parameter reaches every `arm_emptied` and `emptied_at` call, and `median-emptied` flows through `_causes`.

**ADDENDUM-n2's binding**
- VERDICTS and the secondary carry `addendum2_sha256` through `base`; the NOT-RUN output through `not_run_doc`; the G-ANL-n artifact through `ganl_artifact`.
- `BOUND_RELS` includes the addendum, and the structure check reads its bytes.

**Battery arithmetic and counts**
- `_bt_sec_shift`'s rel values come out as stated:

  | Reads | rel |
  |---|---|
  | +1 reads, 0.015 shift | ≈ 0.0068–0.0073 |
  | N1-P at −1, 0.015 shift | ≈ 0.013 |
  | 0.004 shift | ≈ 0.0034 |
  | 1e-5 shift | ≈ 8.9e-6 |

  So the counts 81, 160, 82, 25 and 24 hold.
- VD A–D, VD-CEILING and the VD-REFUSE cases `kind-ceiling` and `ceiling-count` all test what their descriptions say. `EXPECTED_CHECKS` is 227, which is 222 plus 5 new checks, with 5 new coverage ids.
- F14 now expects 0 identity-bound exceedances out of 480. The positive case moved to RD-CEILING and VD-CEILING (1 each at N1-V|0).

## Findings: production code

**F1 — MINOR (a reading for the seat). `paused_points`, lines 5830–5833; PIN-n-37 at 2515–2517.**
- *What is wrong:* the range starts at the batch's recorded first trial. Reads launched after a cleared fire and before the next batch's first trial therefore stand under no pause.
  - The runner's own batch includes them. Its FIDELITY BINOMIAL pin says "the reads since the last adjudicated binomial fire", and `batch_reads` advances on them.
  - §6's reason for the conservative form ("produced in the same span … carry no re-computation to clear them") fits them equally well.
- *Scenario (reachable under PI-STOP, given the session-keyed sample):*
  1. The seat clears a binomial fire at N2-E's last keyed-sample read at f = 0.20, session s < 159.
  2. Later a run's-end batch stands, from N2-S's first keyed-sample read to N4-Ts's last read.
  3. N2-E's f0.20 reads of sessions after s were launched after the ruling, inside the new batch's span. Under the draft no pause stands on them, so N2 is decided.
  4. Under the runner's batch, N2 is INDETERMINATE (pause:N2-E). The same happens at f0.10 when the cap binds.
- *Fix:* put the choice to the seat explicitly. If the runner's batch is meant, start the range at `cleared + 1` (or the stage's start) and keep the binding. VD-PAUSE-POINTS A's expectation would then gain N1-P@+d_20 and N1-P@+d_eq. Today A pins the draft's reading (V05 is killed).

**F2 — MINOR. `n2_outcome` line 581 (the guards' flag), `paused_from` 5808–5810, PIN-n-37 2519–2526.**
- *What is wrong:* the points are no longer capped by scope, but a guard's beside flag still reads the scope (`st.paused`).
  - One VERDICTS can therefore list a guard's points in `figures.pause_points` (and the other f's `paused` list reads points) while `beside.guards.<guard>.paused` is False.
  - Separately, N2's cause `pause:N2-E` can name an arm that no standing pause holds in scope (VD A does this). That reads against the schema's sentence about scope.
- *Scenario (synthetic campaign without keyed-sample reads in the guards' cells; the cap binds):*
  - A standing run's-end batch starts at a keyed-sample N2-E f0.20 read.
  - It covers N2-S and N2-C, which have no trial of their own in it.
  - N2 is decided at f0.10, the beside reads `paused: ["N2-E"]`, and the guards read `paused: False` while `pause_points` lists their four points.
  - Under the runner's session-keyed sample a guard with reads in a range has trials there, so runner reports don't reach this.
- *Fix:* when a point map exists, read the guard flag through its points (V35's text), or state in the PIN that the flag is the scope's. Consider naming N2's pause causes by point (`pause:N2-E@f0.20`), as its incompleteness causes already are.

**F3 — NOTE. `report_problems` 5745–5751.**
- *What is wrong:* the kind checks run one way only. ADDENDUM-n2 §2.1's "pauses at once", and the runner's replay refusal ("fired … with reads after it and no pause"), make every record above C some pause's read. The reader never checks this. The same gap exists for nonfinite and identity-bound.
- *Scenario:* a PI-STOP report that lost its standing ceiling pause passes every check, and PIN-n-37 then stands nothing on that read.
- *Fix:* add `{rid for rid, r in camp.records.items() if above_ceiling(r, C)} <= {q["read_id"] for q in rep["pauses"]}`, and the same for the other two kinds.

**F4 — NOTE. `report_problems` 5715–5730.**
- *What is wrong:* the binding follows the runner's R12 (batches nest) and R13 (a ceiling ruling clears nothing). Both are Code's readings still pending with the seat.
- *Scenario:* if the lock states tiling, or rules that a ceiling ruling clears, every standing batch after a non-firing evaluation (or after an adjudicated ceiling pause) is refused, and `paused_points`' range is wrong.
- *Fix:* say in PIN-n-37 or the entry that `cleared` and `first_w` move with those rulings.

**F5 — NOTE (texts).**
- *(a)* The PINS header (2396–2398) and the module docstring (16–20) present PIN-n-37 as the seat's amended text. But it now carries two new Code readings: the range from the first trial, and the points whatever the scope. Mark them as Code's, strikable until LOCK-n v1.0.
- *(b)* PIN-n-37 (2513) and the `paused_points` docstring (5816) say a single-read pause stands "on that read alone" before giving the shadow extension. §6 says it stands "on its read and, through a shadow, on that session's reads", so "alone" reads against it. Suggest "on that read (not a range)".
- *(c)* The `paused_points` docstring (5822–5823) says "the steered arms only, N1's and N4's pauses being read per arm". The function does return N1's points, which N2 reads. The per-arm reading belongs to `paused_from`.

**F6 — NOTE.**
- PIN-n-38 (2538) cites PIN-n-20 for the point cause. PIN-n-20 names the arm cause; the point cause is PIN-n-36's.
- PIN-n-38 does not say that the second row also marks an arm `median-emptied` when a slope keeps no common session.
- PIN-n-20's text, PIN-n-36's text and `n2_outcome`'s docstring (547: "emptied in the TAU/4 row") still name the TAU/4 row only.

## Findings: battery

**B1 — MINOR. VD-SECOND-ROW (4786–4814) and VD-SENSITIVITY (4619–4642).**
- *What is wrong:* the battery cannot tell §3's trigger from the second sitting's point-level "where it empties". cs2 both empties N1-P@-1 and drops over half at two points, while VD-SENSITIVITY empties no point (rand_00 empties N1-R through its slope, at the arm level). So V26 passes.
- It also cannot tell a trigger computed on the second row's own drops (V28).
- *Fix:*
  - Add a verdicts case that is over half without emptying any point, with rel between TAU/4 and 0.01 (for example only N1-V's +1 reads of runs 79–159 shifted 0.015, at the default median 0.01), expecting a second row.
  - Run pw5's shape (one N1-R direction's 40 reads at +1 dropped, 40 of 960) through verdicts, expecting none.

**B2 — MINOR. RD-SECOND-ROW.** No point anywhere drops exactly half, so `>=` passes (V25). *Fix:* literal checks that `over_half({"x": {"reads": 160, "dropped": 80}})` gives `[]` and 81 gives `["x"]`.

**B3 — MINOR. VD-SECOND-ROW.** No pause stands in cs2, so the second row's pause inputs are untested (V29). *Fix:* run cs2 under PI-STOP with a standing single-read pause at one of N2's reads, and check the second row's `pause_points` and N2 causes.

**B4 — MINOR.** R13 is pinned only for a nonfinite ruling (VD B's `pz_adj`). No case puts an adjudicated fidelity-ceiling pause before a standing batch, so V13 passes. *Fix:* on cvc, follow `pc1` with a standing run's-end batch from the stage's first trial, expecting acceptance; and from the first trial after `li8`, expecting refusal.

**B5 — NOTE. RD-SECOND-ROW 4050–4063.** `row_drops`' set of points is not pinned.
- The expectation dict is built over d4's own keys. If N4 were dropped from both, the comparison holds vacuously, and "N4's none" is then a claim about nothing (V24 passes).
- Counting the shadows as a point gives the matching `N1-V@0 = 1` (V23 passes).
- No campaign has a non-finite read, so counting them passes (V22).
- *Fix:* assert `sorted(d4)` equals the 22 literal `arm@label` keys, and add a non-finite read to cs.

**B6 — NOTE.** VD-SECOND-ROW reads only the arm-level marks (N1's causes, `figures.unusable`), never `point_causes`, so V32 passes. *Fix:* check `point_causes["N1-P@-1"] == ["median-emptied"]`.

**B7 — NOTE.** Every read-less standing batch in the battery ends on a trial that is also the stage's last read, so V14 passes. A CAP report later PI-STOPped, whose last reads carry no re-computation, would be refused by V14. *Fix:* add a run's-end batch on a campaign whose last cell is sample-only.

**B8 — NOTE.** C is 0.25 in every battery identity (`rule={CEILING_KEY: 0.25}` is a no-op), so reading the schema's floor instead of the identity's ceiling passes (V19). This is equivalent on the lock's expected C, since backend-ext-2's 0.0625 leaves the 0.25 floor binding. *Fix:* use C = 0.30 in RD-CEILING.

**B9 — NOTE.**
- RD-PAUSE-POINTS' "a rendering pause's read" (3961–3962) is not a rendering pause: `pq` carries no kind, and its read is on disk, so it repeats "a read alone".
- The guard flag's reading is not pinned (V35).
- The shadow extension over planned reads not on disk is untested (V08).

## Mutants

```
@@ V01 | paused_points | the range's reads narrowed to its trials (the struck form) | predicted: killed by RD-PAUSE-POINTS (a range of one read with no re-computation; N1-P's +d_20 to −1) and VD-PAUSE-POINTS (A, C)
            rids += sorted(rid for rid, r in camp.records.items()
                           if b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
~~
            rids += sorted(rid for rid, r in camp.records.items() if r["fidelity"] is not None
                           and b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
```
```
@@ V02 | paused_points | the shadow extension capped by the pause's scope | predicted: killed by RD-PAUSE-POINTS (the same shadow, its scope N1-V alone; a binomial batch of one shadow)
                for a in STEERED_ARMS:
~~
                for a in sorted(set(q["arms_in_scope"]) & set(STEERED_ARMS)):
```
```
@@ V03 | paused_points | a read's point capped by the scope | predicted: killed by RD-PAUSE-POINTS (the same batch, its scope N1-V; the range to N4-T's first read) and VD-PAUSE-POINTS A
            elif arm in STEERED_ARMS:
~~
            elif arm in STEERED_ARMS and arm in q["arms_in_scope"]:
```
```
@@ V04 | paused_points | the range's last read left out | predicted: killed by RD-PAUSE-POINTS (a range of one read; a binomial batch of one shadow)
                           if b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
~~
                           if b["first_launch_index"] <= r["launch_index"] < b["last_launch_index"])
```
```
@@ V05 | paused_points | the range from the read after the last cleared batch (F1's alternative) | predicted: killed by RD-PAUSE-POINTS and VD-PAUSE-POINTS A (N1-P@+d_20, @+d_eq added): the battery pins the draft's reading
                           if b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
~~
                           if max((x["binomial"]["last_launch_index"] for x in rep["pauses"] if x["adjudicated"]
                                   and x["binomial"] is not None and x["read_id"] is not None), default=-1)
                           < r["launch_index"] <= b["last_launch_index"])
```
```
@@ V06 | paused_points | adjudicated pauses read as standing | predicted: killed by RD-PAUSE-POINTS (an adjudicated pause)
        if q["adjudicated"]:
            continue
        rids = [] if q["read_id"] is None else [q["read_id"]]
~~
        rids = [] if q["read_id"] is None else [q["read_id"]]
```
```
@@ V07 | paused_points | N4's reads read point by point | predicted: killed by RD-PAUSE-POINTS (N4's pause; an N4 trial is no shadow)
            elif arm in STEERED_ARMS:
~~
            elif arm in ARMS:
```
```
@@ V08 | paused_points | the shadow extension over reads on disk only (a planned point not on disk not stood on) | predicted: survives
                    for pa, _pd, plab, psid in (p.split("|") for p in camp.planned[a]):
~~
                    for pa, _pd, plab, psid in (p.split("|") for p in camp.present[a]):
```
```
@@ V09 | report_problems | the report's ceiling counter not held to the records | predicted: killed by VD-REFUSE (ceiling-count)
    for k in ("fidelity", "nonfinite_reads", "identity_out_of_bound", CEILING_COUNTER):
~~
    for k in ("fidelity", "nonfinite_reads", "identity_out_of_bound"):
```
```
@@ V10 | report_problems | a ceiling pause held to the identity bound (refused at a steered read) | predicted: killed by VD-CEILING (accepted)
            if "fidelity-ceiling" in kinds and not above_ceiling(rec, ceiling_of(ident)):
~~
            if "fidelity-ceiling" in kinds and not (rec["identity"] is not None and not rec["identity"]["within"]):
```
```
@@ V11 | report_problems | the ceiling checked only as the pause's kind, not in also_fired | predicted: survives (equivalent on runner reports)
            if "fidelity-ceiling" in kinds and not above_ceiling(rec, ceiling_of(ident)):
~~
            if q["kind"] == "fidelity-ceiling" and not above_ceiling(rec, ceiling_of(ident)):
```
```
@@ V12 | report_problems | any ruling clears the batch | predicted: killed by VD-PAUSE-POINTS B
    cleared = max((q["binomial"]["last_launch_index"] for q in rep["pauses"]           # an adjudicated batch's ruling
                   if q["adjudicated"] and q["binomial"] is not None and q["read_id"] is not None), default=-1)
~~
    cleared = max((q["launch_index"] for q in rep["pauses"]           # an adjudicated batch's ruling
                   if q["adjudicated"] and q["read_id"] is not None), default=-1)
```
```
@@ V13 | report_problems | a fidelity-ceiling ruling clears the batch (R13 reversed) | predicted: survives
    cleared = max((q["binomial"]["last_launch_index"] for q in rep["pauses"]           # an adjudicated batch's ruling
                   if q["adjudicated"] and q["binomial"] is not None and q["read_id"] is not None), default=-1)
~~
    cleared = max((q["launch_index"] for q in rep["pauses"]           # an adjudicated batch's ruling
                   if q["adjudicated"] and q["read_id"] is not None
                   and (q["binomial"] is not None or "fidelity-ceiling" in [q["kind"]] + list(q["also_fired"]))),
                  default=-1)
```
```
@@ V14 | report_problems | a run's-end batch bound to end at the stage's last read, not its last trial | predicted: survives
            last_w = (trial_li[-1] if trial_li else None) if q["read_id"] is None else q["launch_index"]
~~
            last_w = (m - 1) if q["read_id"] is None else q["launch_index"]
```
```
@@ V15 | report_problems | a standing batch bound from the stage's first trial, clears ignored | predicted: killed by VD-PAUSE-POINTS (A, C, D)
            first_w = next((i for i in trial_li if i > cleared), None)
~~
            first_w = trial_li[0] if trial_li else None
```
```
@@ V16 | above_ceiling | a discordance equal to C counted above it | predicted: killed by RD-CEILING (strict)
    return bool(ceiling is not None and f is not None and f["absdiff"] is not None and f["absdiff"] > ceiling)
~~
    return bool(ceiling is not None and f is not None and f["absdiff"] is not None and f["absdiff"] >= ceiling)
```
```
@@ V17 | counters | the per-arm ceiling counter read off the identity check (d = 0 only) | predicted: killed by RD-CEILING (counters) and VD-CEILING
        c["fidelity ceiling exceeded"] += above_ceiling(r, ceil)
~~
        c["fidelity ceiling exceeded"] += bool(r["identity"] is not None and not r["identity"]["within"])
```
```
@@ V18 | report_counters | the report's ceiling count over dose-rule re-computations only | predicted: killed by VD-CEILING (accepted)
        over_c += above_ceiling(r, ceil)
~~
        over_c += above_ceiling(r, ceil) and r["fidelity"]["reason"] == "dose-rule"
```
```
@@ V19 | ceiling_of | C read as the schema's floor, not the identity's ceiling | predicted: survives
    return identity["fidelity_rule"][CEILING_KEY]
~~
    return None if identity["fidelity_rule"][CEILING_KEY] is None else 0.25
```
```
@@ V20 | median_drop | a read at the median dropped | predicted: killed by RD-SECOND-ROW (filter)
        return bool(f is not None and f["rel"] is not None and f["rel"] > median_rel)
~~
        return bool(f is not None and f["rel"] is not None and f["rel"] >= median_rel)
```
```
@@ V21 | row_drops | a shadow no longer drops its session's steered reads | predicted: killed by RD-SECOND-ROW and VD-SECOND-ROW
            x["dropped"] += bool(drop(rid) or (a in STEERED_ARMS and drop(f"N1-V|none|0|{sid}")))
~~
            x["dropped"] += bool(drop(rid))
```
```
@@ V22 | row_drops | non-finite reads counted among an arm's reads at a point | predicted: survives
            if (a, lab) == ("N1-V", "0") or not camp.records[rid]["finite"]:
~~
            if (a, lab) == ("N1-V", "0"):
```
```
@@ V23 | row_drops | the shadows counted as N1-V's point 0 | predicted: survives
            if (a, lab) == ("N1-V", "0") or not camp.records[rid]["finite"]:
~~
            if not camp.records[rid]["finite"]:
```
```
@@ V24 | row_drops | N4's arms left out, so N4 never triggers the second row | predicted: survives
            if (a, lab) == ("N1-V", "0") or not camp.records[rid]["finite"]:
~~
            if lab == "0" or not camp.records[rid]["finite"]:
```
```
@@ V25 | over_half | "more than half" read as at least half | predicted: survives
    return [k for k, x in drops.items() if 2 * x["dropped"] > x["reads"]]
~~
    return [k for k, x in drops.items() if 2 * x["dropped"] >= x["reads"]]
```
```
@@ V26 | run_verdicts | the trigger read as the second sitting's "where it empties" (a point emptied) | predicted: survives
    if over:                                       # ADDENDUM-n2 §3: reported where the TAU/4 row drops over half
~~
    if any("tau4-emptied" in v for v in st_s.at.values()):
```
```
@@ V27 | run_verdicts | the trigger widened to an arm the TAU/4 row empties | predicted: killed by VD-SENSITIVITY (no second row)
    if over:                                       # ADDENDUM-n2 §3: reported where the TAU/4 row drops over half
~~
    if over or "tau4-emptied" in st_s.unusable.values():
```
```
@@ V28 | run_verdicts | the trigger read on the second row's own drops | predicted: survives
    if over:                                       # ADDENDUM-n2 §3: reported where the TAU/4 row drops over half
~~
    if over_half(row_drops(camp, median_drop(camp, median_of(camp.identity)))):
```
```
@@ V29 | run_verdicts | the second row reads pauses per arm, not at PIN-n-37's points | predicted: survives
        st_m, fig_m = build_state(camp, paused=paused, gread=g, drop=median_drop(camp, med), paused_at=pat,
                                  emptied="median-emptied")
~~
        st_m, fig_m = build_state(camp, paused=paused, gread=g, drop=median_drop(camp, med),
                                  emptied="median-emptied")
```
```
@@ V30 | run_verdicts | the second row drops at TAU/4 | predicted: killed by VD-SECOND-ROW (N1-V|+1 n 78)
        st_m, fig_m = build_state(camp, paused=paused, gread=g, drop=median_drop(camp, med), paused_at=pat,
                                  emptied="median-emptied")
~~
        st_m, fig_m = build_state(camp, paused=paused, gread=g, drop=tau4_drop(camp), paused_at=pat,
                                  emptied="median-emptied")
```
```
@@ V31 | run_verdicts | the second row's emptied cause left at tau4-emptied | predicted: killed by VD-SECOND-ROW
        st_m, fig_m = build_state(camp, paused=paused, gread=g, drop=median_drop(camp, med), paused_at=pat,
                                  emptied="median-emptied")
~~
        st_m, fig_m = build_state(camp, paused=paused, gread=g, drop=median_drop(camp, med), paused_at=pat)
```
```
@@ V32 | build_state | a point any sensitivity row empties named tau4-emptied | predicted: survives
            st.at[(arm, key)] = [emptied]
~~
            st.at[(arm, key)] = ["tau4-emptied"]
```
```
@@ V33 | build_state | an arm any sensitivity row empties named tau4-emptied | predicted: killed by VD-SECOND-ROW
        st.unusable[arm] = emptied
~~
        st.unusable[arm] = "tau4-emptied"
```
```
@@ V34 | median_of | the second row's median read as the ceiling | predicted: killed by VD-SECOND-ROW (median_rel 1e-6)
    return identity["fidelity_rule"][MEDIAN_KEY]
~~
    return identity["fidelity_rule"][CEILING_KEY]
```
```
@@ V35 | n2_outcome | a guard's beside flag read through PIN-n-37's points, not the scope | predicted: survives
                         | {"paused": bool(st.paused.get(a))}
~~
                         | {"paused": any(st.paused_on(a, f) for f in (F10, F20))}
```

Every old text above appears exactly once in the frozen copy as a whole line; I checked each with a fixed-string, whole-line count.

## Commands beyond reading files and the brief's git forms

- `shasum -a 256` on the scratch files and on five named repository files (none under `data/`).
- Name-only `ls` of the scratch review folder and of the empty reviewer folder.
- `wc -l` on the frozen copy, the base copy, the diff and the eight named specification files.
- `git rev-parse HEAD:<path>` for the addendum, the schema and the runner, and `git rev-parse 003ae7d:<path>` for the schema and the runner, compared against `git hash-object -- <path>`. This is the brief's tracked-and-clean form; the `003ae7d:` revision is a variant of it, and neither form takes item 3's pathspec.
- `/usr/bin/grep -n` inside single named files: `RESULTS.md`, `valence_core/n/schema.py`, `valence_core/n/runner.py`, `scripts/n_sessions.py`, the frozen copy and the base copy. Some were piped to `head`. One was aimed at a path that does not exist in the review folder, with its error suppressed. None was recursive and none touched `data/`.
- A shell loop over a literal list of strings running `/usr/bin/grep -c -F -x` on the frozen copy, to check that each mutant's old text is unique.

I ran no interpreter, wrote no file, and read, listed or stat'ed nothing under `data/`.

## 2. Code's dispositions

Every finding is taken: applied, or kept as a reading of Code's with the finding's scenario put to the seat. The fixed
draft (d2) carries them all.

### Production code

- **F1 (MINOR), the range from the batch's first trial.** Kept, as PIN-n-37's reading (b), now marked as Code's: §6
  names the reads "between" the trials, and the report records the range from the first trial (`BINOMIAL_FIELDS`).
  The reviewer's scenario goes to the seat with the entry. Under PI-STOP, after a fire cleared at a keyed-sample read
  mid-cell, the reads of that cell launched after it and before the next trial lie in no range. N2 can then be
  decided where the runner's batch, counted from the clear, would make it INDETERMINATE. VD-PAUSE-POINTS A pins the
  reading (V05).
- **F2 (MINOR), the guard flag and the scope.** Applied. A guard's beside flag reads its points, as N2 does
  (PIN-n-37's reading (c), Code's): §6 names N1's and N4's pauses alone as per arm. With no point map (the battery's
  literal states), the flag reads the arm, as before. The second half, N2's pause cause naming an arm rather than a
  point, is left as PIN-n-36 has it (accepted by the seat): the cause names the arm whose read the pause stands on,
  in its scope or not. The entry says so.
- **F3 (NOTE), the kind checks one way only.** Applied for the new kind. `report_problems` now also requires every
  record above the ceiling to be the read of a pause naming `fidelity-ceiling` (§2.1: "pauses at once"; PIN-n-39).
  The same converse for the non-finite and identity-bound kinds is not applied: PIN-n-24 binds them one way, as the
  seat accepted it. It is put to the seat in the entry.
- **F4 (NOTE), the binding's dependence on the runner's R12 and R13.** Applied in text. PIN-n-37 states that the
  binding follows the runner's batch, cumulative since the last cleared fire, which a ceiling ruling does not clear
  (R12, R13, Code's readings for the seat), and that it moves with their rulings.
- **F5 (NOTE), texts.** Applied:
  - (a) the module docstring and the PINS header mark PIN-n-37's three readings as Code's, strikable until LOCK-n
    v1.0;
  - (b) PIN-n-37's "on that read alone" and the docstring's "on that alone" (the reviewer quotes both as the first)
    are now "on that read" and "on that read, not a range";
  - (c) `paused_points`' docstring says that N4's pauses are read per arm, and that N1's rule reads its pauses per arm
    through `paused` while N2 reads N1's arms at these points.
- **F6 (NOTE), the second row's causes.** Applied in PIN-n-38: a point it leaves with no session, and an arm whose
  slope it leaves with no common session, are marked `median-emptied`, as the TAU/4 row marks them `tau4-emptied`.
  It cites PIN-n-20 and PIN-n-36 for those. PIN-n-20's and PIN-n-36's own texts, both accepted, are unchanged.
  `n2_outcome`'s docstring now says "emptied in a sensitivity row".

### The battery

- **B1 (MINOR), the trigger.** Applied: a new check, VD-SECOND-ROW-TRIGGER, on two campaigns.
  - ct1 is over half at N1-V's +1 with no point emptied, so the second row is reported, at the example median 0.01,
    and drops none of them.
  - ct2 empties N1-R at +1 in the TAU/4 row with 40 of 960 dropped, so no second row is reported.
- **B2 (MINOR), exactly half.** Applied in RD-SECOND-ROW: 2 of 4 is not over half, and 3 of 4 is.
- **B3 (MINOR), the second row's pauses.** Applied: a new check, VD-SECOND-ROW-PAUSE (cs3). The cap binds, and a
  ceiling pause stands on N2-E at f = 0.20, the other f. In the primary, the TAU/4 row and the second row alike, N2 is
  decided and its beside names N2-E paused.
- **B4 (MINOR), R13.** Applied: a new check, VD-BATCH-CLEARS (cr). After a ceiling pause adjudicated at a shadow, a
  run's-end batch from the stage's first trial is accepted, and one from the first trial after the shadow is refused.
- **B5 (NOTE), the set of points.** Applied: RD-SECOND-ROW pins the 22 `arm@label` keys literally, the shadows none.
  VD-PISTOP-STANDING pins N4-Ts's 159 finite reads, the non-finite one left out.
- **B6 (NOTE), the emptied point.** Applied: VD-SECOND-ROW reads `point_causes` (`median-emptied`, and the TAU/4 row's
  `tau4-emptied`).
- **B7 (NOTE), a run's-end batch's end.** Applied in VD-BATCH-CLEARS: its last trial is not the stage's last read.
- **B8 (NOTE), C at the floor everywhere.** Applied: RD-CEILING sets C = 0.30, with one read 0.27 apart, above the
  schema's floor and not above C.
- **B9 (NOTE).** Applied:
  - RD-PAUSE-POINTS' case is renamed "an N2-E read alone (f0.10)";
  - VD-PAUSE-POINTS D no longer samples an N2-C read (it samples N2-E's last read and N2-S's first), so N2-C's reads
    lie in the range with no trial of N2-C's in it, and both guards' flags read paused at their points;
  - RD-PAUSE-POINTS gains a sixteenth case, a shadow whose session's N1-P −1 cell is planned and not on disk.
- **Code's own additions, made while the review ran** and so absent from the frozen copy, are in the fixed draft too:
  in RD-SECOND-ROW, 'more than half' strict; VD-SECOND-ROW's `point_causes`; VD-PISTOP-STANDING's 159 finite reads.
  B2, B5 and B6 then asked for the same. VD-REFUSE's `ceiling-unpaused` is F3's, added with its fix.

### The mutants

The reviewer's 35 ran on the fixed draft. V35's old text is d2's base text no more (d2 carries V35's change, F2's
fix), so it is re-expressed as the reverse: the flag read per arm. Code's own 26 were written before the review. The
17 that the reviewer's duplicate are dropped (C01–C07, C09, C12, C14–C17, C19–C22), and the other nine (C08, C10,
C11, C13, C18, C23–C26) run beside C27, which mutates d2's F3 check: 45 in all.

## 3. The mutants and their run

- **The base:** the fixed draft d2, `review/n_analyze.mutant-base.py` in Code's scratch, sha256 `b605b91f908cdd65dc50f047c7f9f7d452267934de152e43463e6b4ed6a44c2c`.
  It is 230/230 on its own run, every one of its 233 coverage ids reached.
- **The manifest:** `review/mutants_manifest.txt`, 45 files, sha256 `abc1355e…20a8`. The coordinating session checked
  it with the base before the first mutant ran.
- **The runs:** three mutants per foreground call, fifteen calls. One window covered them, reopened after n-build's
  G-VEC self-test had the battery; no mutant ran before that. Each run's output is in Code's scratch; the table below
  is built from them by script.

The table's "Predicted" column is each mutant's author's: the reviewer's for V01–V35, on the frozen copy (d1), and
Code's for its own, on the fixed draft. V35 ran re-expressed, as the reverse of the reviewer's text (below), since d2
carries that text as F2's fix; its row keeps the reviewer's header.

| Mutant | From | Function | What breaks | Predicted (by its author) | Result: the coverage ids the run left unreached (the battery prints the first six, sorted), and any group exception |
|---|---|---|---|---|---|
| V01 | reviewer | `paused_points` | the range's reads narrowed to its trials (the struck form) | killed by RD-PAUSE-POINTS (a range of one read with no re-computation; N1-P's +d_20 to −1) and VD-PAUSE-POINTS (A, C) | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V02 | reviewer | `paused_points` | the shadow extension capped by the pause's scope | killed by RD-PAUSE-POINTS (the same shadow, its scope N1-V alone; a binomial batch of one shadow) | killed: RD-PAUSE-POINTS |
| V03 | reviewer | `paused_points` | a read's point capped by the scope | killed by RD-PAUSE-POINTS (the same batch, its scope N1-V; the range to N4-T's first read) and VD-PAUSE-POINTS A | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V04 | reviewer | `paused_points` | the range's last read left out | killed by RD-PAUSE-POINTS (a range of one read; a binomial batch of one shadow) | killed: RD-PAUSE-POINTS |
| V05 | reviewer | `paused_points` | the range from the read after the last cleared batch (F1's alternative) | killed by RD-PAUSE-POINTS and VD-PAUSE-POINTS A (N1-P@+d_20, @+d_eq added): the battery pins the draft's reading | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V06 | reviewer | `paused_points` | adjudicated pauses read as standing | killed by RD-PAUSE-POINTS (an adjudicated pause) | killed: RD-PAUSE-POINTS, VD-CEILING, VD-PAUSE-POINTS |
| V07 | reviewer | `paused_points` | N4's reads read point by point | killed by RD-PAUSE-POINTS (N4's pause; an N4 trial is no shadow) | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V08 | reviewer | `paused_points` | the shadow extension over reads on disk only (a planned point not on disk not stood on) | survives | killed: RD-PAUSE-POINTS |
| V09 | reviewer | `report_problems` | the report's ceiling counter not held to the records | killed by VD-REFUSE (ceiling-count) | killed: VD-REFUSE |
| V10 | reviewer | `report_problems` | a ceiling pause held to the identity bound (refused at a steered read) | killed by VD-CEILING (accepted) | killed: VD-CEILING, VD-SECOND-ROW-PAUSE |
| V11 | reviewer | `report_problems` | the ceiling checked only as the pause's kind, not in also_fired | survives (equivalent on runner reports) | survived |
| V12 | reviewer | `report_problems` | any ruling clears the batch | killed by VD-PAUSE-POINTS B | killed: VD-BATCH-CLEARS, VD-PAUSE-POINTS |
| V13 | reviewer | `report_problems` | a fidelity-ceiling ruling clears the batch (R13 reversed) | survives | killed: VD-BATCH-CLEARS |
| V14 | reviewer | `report_problems` | a run's-end batch bound to end at the stage's last read, not its last trial | survives | killed: VD-BATCH-CLEARS |
| V15 | reviewer | `report_problems` | a standing batch bound from the stage's first trial, clears ignored | killed by VD-PAUSE-POINTS (A, C, D) | killed: VD-PAUSE-POINTS |
| V16 | reviewer | `above_ceiling` | a discordance equal to C counted above it | killed by RD-CEILING (strict) | killed: RD-CEILING |
| V17 | reviewer | `counters` | the per-arm ceiling counter read off the identity check (d = 0 only) | killed by RD-CEILING (counters) and VD-CEILING | killed: RD-CEILING, VD-CEILING |
| V18 | reviewer | `report_counters` | the report's ceiling count over dose-rule re-computations only | killed by VD-CEILING (accepted) | killed: VD-CEILING, VD-SECOND-ROW-PAUSE |
| V19 | reviewer | `ceiling_of` | C read as the schema's floor, not the identity's ceiling | survives | killed: RD-CEILING |
| V20 | reviewer | `median_drop` | a read at the median dropped | killed by RD-SECOND-ROW (filter) | killed: RD-SECOND-ROW |
| V21 | reviewer | `row_drops` | a shadow no longer drops its session's steered reads | killed by RD-SECOND-ROW and VD-SECOND-ROW | killed: RD-SECOND-ROW, VD-SECOND-ROW |
| V22 | reviewer | `row_drops` | non-finite reads counted among an arm's reads at a point | survives | killed: VD-PISTOP-STANDING |
| V23 | reviewer | `row_drops` | the shadows counted as N1-V's point 0 | survives | killed: RD-SECOND-ROW |
| V24 | reviewer | `row_drops` | N4's arms left out, so N4 never triggers the second row | survives | killed: RD-SECOND-ROW, VD-PISTOP-STANDING |
| V25 | reviewer | `over_half` | "more than half" read as at least half | survives | killed: RD-SECOND-ROW |
| V26 | reviewer | `run_verdicts` | the trigger read as the second sitting's "where it empties" (a point emptied) | survives | killed: VD-SECOND-ROW-PAUSE, VD-SECOND-ROW-TRIGGER |
| V27 | reviewer | `run_verdicts` | the trigger widened to an arm the TAU/4 row empties | killed by VD-SENSITIVITY (no second row) | killed: VD-SECOND-ROW-TRIGGER, VD-SENSITIVITY |
| V28 | reviewer | `run_verdicts` | the trigger read on the second row's own drops | survives | killed: VD-SECOND-ROW-PAUSE, VD-SECOND-ROW-TRIGGER |
| V29 | reviewer | `run_verdicts` | the second row reads pauses per arm, not at PIN-n-37's points | survives | killed: VD-SECOND-ROW-PAUSE |
| V30 | reviewer | `run_verdicts` | the second row drops at TAU/4 | killed by VD-SECOND-ROW (N1-V\|+1 n 78) | killed: VD-SECOND-ROW |
| V31 | reviewer | `run_verdicts` | the second row's emptied cause left at tau4-emptied | killed by VD-SECOND-ROW | killed: VD-SECOND-ROW |
| V32 | reviewer | `build_state` | a point any sensitivity row empties named tau4-emptied | survives | killed: VD-SECOND-ROW |
| V33 | reviewer | `build_state` | an arm any sensitivity row empties named tau4-emptied | killed by VD-SECOND-ROW | killed: VD-SECOND-ROW |
| V34 | reviewer | `median_of` | the second row's median read as the ceiling | killed by VD-SECOND-ROW (median_rel 1e-6) | killed: VD-SECOND-ROW, VD-SECOND-ROW-TRIGGER |
| V35 | reviewer, re-expressed | `n2_outcome` | a guard's beside flag read through PIN-n-37's points, not the scope | survives | killed: VD-PAUSE-POINTS |
| C08 | Code | `report_problems` | a ceiling pause's read is not checked | killed by VD-REFUSE (kind-ceiling) | killed: VD-REFUSE |
| C10 | Code | `report_counters` | the recount counts every re-computed read | killed by RD-CEILING (the report's) | killed: RD-CEILING, VD-BATCH-CLEARS, VD-CEILING, VD-COMPLETE, VD-EXPOSURE, VD-GREAD-MIXED; FileNotFoundError raised in the verdicts group |
| C11 | Code | `counters` | the per-arm ceiling counter never counts | killed by RD-CEILING (counters) and VD-CEILING | killed: RD-CEILING, VD-CEILING |
| C13 | Code | `row_drops` | a shadow drops N4's reads too | killed by RD-SECOND-ROW (second row: N4's none) | killed: RD-SECOND-ROW |
| C18 | Code | `run_verdicts` | the second row reported everywhere | killed by VD-SENSITIVITY (no second row) | killed: VD-SECOND-ROW-TRIGGER, VD-SENSITIVITY |
| C23 | Code | `run_verdicts` | VERDICTS do not name ADDENDUM-n2 | killed by VD-COMPLETE (bindings) | killed: VD-COMPLETE |
| C24 | Code | `not_run_doc` | the NOT-RUN output does not name ADDENDUM-n2 | killed by CMD-NOTRUN | killed: CMD-GANL-REFUSE, CMD-NOTRUN, CMD-NOTRUN-REFUSE, STR-GANL-ARTIFACT; KeyError raised in the commands group |
| C25 | Code | `BOUND_RELS` | G-ANL-n's committed check leaves ADDENDUM-n2 out | killed by STR-GANL-ARTIFACT | killed: STR-GANL-ARTIFACT |
| C26 | Code | `the pins` | a wrong ADDENDUM-n2 pin | killed by STR-ADDENDUM2-SHA | killed: STR-ADDENDUM2-SHA |
| C27 | Code | `report_problems` | the ceiling bound one way only: a read above C that no pause names passes | killed by VD-REFUSE (ceiling-unpaused) | killed: VD-REFUSE |

**Notes on the table.**
- **V11 survived**, as the reviewer predicted. It checks the ceiling only as a pause's kind, not in `also_fired`. With
  the kind directly after `nonfinite` in `PAUSE_KINDS`, a ceiling trigger sits in `also_fired` only behind `nonfinite`
  or `rendering`. A non-finite read has no comparison, so it is never above C, and a rendering pause's read is not
  launched. So the mutant is equivalent on reports the runner writes.
- **The 13 others the reviewer predicted would survive d1** are killed on d2, each by a check the dispositions added
  or extended:
  - V08 by RD-PAUSE-POINTS' sixteenth case;
  - V13 and V14 by VD-BATCH-CLEARS;
  - V19 by RD-CEILING at C = 0.30;
  - V22 and V24 by VD-PISTOP-STANDING's 159 reads;
  - V23 and V24 by RD-SECOND-ROW's 22 points;
  - V25 by RD-SECOND-ROW's strict half;
  - V26 and V28 by VD-SECOND-ROW-TRIGGER;
  - V29 by VD-SECOND-ROW-PAUSE;
  - V32 by VD-SECOND-ROW's `point_causes`;
  - V35, re-expressed, by VD-PAUSE-POINTS D.
- **C10 and C24** raised in a group as well as failing checks: C10's miscounted ceiling made later cases' outputs
  absent (a `FileNotFoundError` in the verdicts group), and C24's NOT-RUN output lost the key a check reads (a
  `KeyError` in the commands group). Each is killed by a non-zero exit, as every other is.

### V35, re-expressed on the fixed draft

```
@@ V35 | n2_outcome | re-expressed on the fixed draft, which carries V35's text: a guard's beside flag read per arm (its scope), not at its points | predicted: killed by VD-PAUSE-POINTS (D: span_character paused at its points, N2-C not in the scope)
                         | {"paused": any(st.paused_on(a, f) for f in (F10, F20))}
~~
                         | {"paused": bool(st.paused.get(a))}
```

### Code's mutants, as run

Code wrote them before the review, on the draft d1, and checked their anchors on d2 (each occurs once). C27 was written
on d2, for F3's check. The 17 of Code's that duplicate the reviewer's (C01–C07, C09, C12, C14–C17, C19–C22) were
dropped before the manifest.

```
@@ C08 | report_problems | a ceiling pause's read is not checked | predicted: killed by VD-REFUSE (kind-ceiling)
            if "fidelity-ceiling" in kinds and not above_ceiling(rec, ceiling_of(ident)):
                p.append(f"{q['pause_id']}: a fidelity-ceiling pause at a read not above the ceiling")
~~
@@ C10 | report_counters | the recount counts every re-computed read | predicted: killed by RD-CEILING (the report's)
        over_c += above_ceiling(r, ceil)
~~
        over_c += r["fidelity"] is not None
@@ C11 | counters | the per-arm ceiling counter never counts | predicted: killed by RD-CEILING (counters) and VD-CEILING
        c["fidelity ceiling exceeded"] += above_ceiling(r, ceil)
~~
@@ C13 | row_drops | a shadow drops N4's reads too | predicted: killed by RD-SECOND-ROW (second row: N4's none)
            x["dropped"] += bool(drop(rid) or (a in STEERED_ARMS and drop(f"N1-V|none|0|{sid}")))
~~
            x["dropped"] += bool(drop(rid) or drop(f"N1-V|none|0|{sid}"))
@@ C18 | run_verdicts | the second row reported everywhere | predicted: killed by VD-SENSITIVITY (no second row)
    if over:                                       # ADDENDUM-n2 §3: reported where the TAU/4 row drops over half
~~
    if True:
@@ C23 | run_verdicts | VERDICTS do not name ADDENDUM-n2 | predicted: killed by VD-COMPLETE (bindings)
            "addendum2_sha256": ADDENDUM2_SHA256, "analyzer_sha256": asha,
~~
            "analyzer_sha256": asha,
@@ C24 | not_run_doc | the NOT-RUN output does not name ADDENDUM-n2 | predicted: killed by CMD-NOTRUN
            "addendum2_sha256": ADDENDUM2_SHA256, "analyzer_sha256": analyzer_sha256(), "pins": PINS, "open": OPEN,
~~
            "analyzer_sha256": analyzer_sha256(), "pins": PINS, "open": OPEN,
@@ C25 | BOUND_RELS | G-ANL-n's committed check leaves ADDENDUM-n2 out | predicted: killed by STR-GANL-ARTIFACT
BOUND_RELS = (PROPOSAL_REL, ADDENDUM_REL, ADDENDUM2_REL, SCHEMA_REL, f"{BK_NP_REL}/prereg.json",
~~
BOUND_RELS = (PROPOSAL_REL, ADDENDUM_REL, SCHEMA_REL, f"{BK_NP_REL}/prereg.json",
@@ C26 | the pins | a wrong ADDENDUM-n2 pin | predicted: killed by STR-ADDENDUM2-SHA
ADDENDUM2_SHA256 = "41f76c49d756e09481a70f398469d9febc96bb534f28cd18d265ea87add2bb3f"
~~
ADDENDUM2_SHA256 = "41f76c49d756e09481a70f398469d9febc96bb534f28cd18d265ea87add2bb3e"
@@ C27 | report_problems | the ceiling bound one way only: a read above C that no pause names passes | predicted: killed by VD-REFUSE (ceiling-unpaused)
    if unpaused:
        p.append(f"{len(unpaused)} read(s) above the ceiling are no fidelity-ceiling pause's read, e.g. {unpaused[0]} "
                 "(ADDENDUM-n2 §2.1: 'pauses at once'; PIN-n-39)")
~~
```

## 4. The battery runs

Every run was in a battery window the coordinating session granted, on bytes named to it first by sha256, with the
terms above.

| Run | Bytes (sha256) | Result | Exit | Output (sha256) |
|---|---|---|---|---|
| d1, the first draft (window 1) | `0e459d7d…fddc` | 227/227, 230 coverage ids reached | 0 | `a10d5229…9c6b` |
| d2, the fixed draft, the mutant base (window 2) | `b605b91f…4c2c` | 230/230, 233 coverage ids reached | 0 | `795b5f5a…8138` |
| the 45 mutants (window 2, reopened) | the manifest, `abc1355e…20a8` | 44 killed, 1 survived (V11), 0 not run | 1 for each killed | the kill tally, `362a3b60…9f01` |
| the run of record (window 3), `scripts/n_analyze.py` | `418c2136…072d` | 230/230, 233 coverage ids reached | 0 | the self-test raw |

The coordinating session closed window 2 after d2's run, for n-build's one G-VEC self-test, and reopened it for the
mutants. Q-F3's campaign ran on the laptop beside these runs, as the coordinating session's windows allow; by its
grants, no other battery window was open during any of them.

## 5. The committed bytes against the mutation-tested base

The committed file, `scripts/n_analyze.py` (sha256 `418c2136fe4fc3875b6cc3e0e81221f0f4628fdc49e959fce38b2cc7d915072d`), differs from the mutant base (`b605b91f…4c2c`) in
nine change regions, as `diff` counts them:
- the repository line, `REPO = Path(__file__).resolve().parents[1]`, which the committed file computes and the
  scratch drafts gave as an absolute path;
- the module docstring's paragraph on PINS and OPEN, rewrapped (the values-check's pass 1, observation 6);
- PIN-n-37's text, where the shadow extension reaches "every planned steered read" (pass 2, observation 2), rewrapped,
  in two regions;
- PIN-n-38's text: a read's session's shadow drops it only for a steered read (pass 1, its item on PIN-n-38); and the
  arms a slope marks emptied are named, N1-V's or an N1-R direction's (pass 2, observation 3);
- the comment above CEILING_KEY, which now cites the fourth sitting's answers by path (pass 1, FAIL 2);
- the descriptions of VD-CEILING and STR-GANL-ARTIFACT, rewrapped (pass 1, observation 6);
- `paused_points`' docstring, where the shadow extension reaches "every planned steered read" (pass 2, observation
  2).

No mutant's change lies in a region that differs. The repository line runs in every battery run; at the committed
path it computes the root that the drafts' absolute line gave. The forms' digest, CODE_FORMS_SHA256, is the base's.

## 6. The tallies

Unchanged from `bfc869f`'s. No sentence form changed, so the forms' digest is unchanged (`41d0d654…b1da`), and the
tuple pass's 2,561 evaluations and its hand tallies are the same.
