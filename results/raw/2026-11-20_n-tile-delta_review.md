# n — the R12, F5 and R13 runner delta: the blind review of draft 1, as returned, with every disposition

PI date 2026-11-20. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over draft 1, the delta from HEAD `db00d6d`'s bytes (both files
unchanged since `003ae7d`):
- `valence_core/n/runner.py`, from `e8e81ab0…f787` (1022 lines) to `db18cb48…81dd` (1058 lines);
- `valence_core/n/schema.py`, from `5cbf60db…574c` (2428 lines) to `21cbe294…b389` (2492 lines).
Draft 1's self-test ran once, in a battery window, before the review: 575/575, exit 0.

**The reviewer's brief** (`fda516b3…e1ff`, 82 lines):
- gave the two deltas' FROM files (HEAD's, by path) and TO files (by sha256), and the `git diff --no-index -U3` form;
  for what the change must do, the seat's answers of 2026-11-19, first sitting (§3: R12, R13 and F5; §4 (b); the
  routing block's item 4), the schema follow-up's values-check for R13's two texts (its observations 9 and 10), the
  form agreed with n-analyzer, and Code's declared readings and additions;
- asked whether the tile matches R12 exactly, on a resume too, and where `clear_batch` was called; whether the new
  form checks can refuse a report the runner can write; whether F5 and the moved example values leave every other
  module's cases testing what they were written to test; and whether the R13 texts are right;
- asked for findings, surviving mutants and observations, and for any command a rule bars;
- quoted the list of record v2's items 1–5, verbatim, and barred any interpreter, any write, any network, any guard
  marker in an argv, anything under `data/mf3`, any whole-tree git status, any read, listing, size or time of a ckpt
  or reports file, and, in Code's scratch, anything but the files it named.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (175 lines, sha256
`dbe9cce8…0517`). It names scratch files only by their paths inside the scratch folder. Its line numbers are draft
1's: the report's TO files are `S/step4b/tile/draft/`'s, which held draft 1 at the review (kept since at
`S/step4b/tile/draft1/`). Against the committed bytes they shift: M1's runner :240 is :247, M4's and M5's :514 is
:524, and M6's schema :1472 is :1477, for example.

**Totals:** 0 BUG; 5 findings (3 RISK, 2 NIT); 8 surviving mutants; 8 observations.

## 1. Dispositions, applied in draft 2

Draft 2: `valence_core/n/runner.py` `9bf75cbb…d61e` (1104 lines, +65 −19 on draft 1) and `valence_core/n/schema.py`
`bedba2c7…c66a` (2524 lines, +67 −35 on draft 1). Its self-test, in a battery window of its own: 578/578, exit 0.
The bytes committed are draft 3, after the values-check (its observations 2 and 3, in the schema only): the runner
unchanged, the schema `1cab28df…edff` (2527 lines, +6 −3 on draft 2); its self-test, in a window of its own:
578/578, exit 0 (the values-check's raw).

- **F1** (RISK), applied: "a fire's batch not ending at its read" is single-defect again. On the example fire at
  read 479 (the tile 320–479) its batch moves to the whole tile 160–319, with `expect="ends its batch at that read"`;
  it kills M6.
- **F2** (RISK), applied: a fire's tile is exact at a read.
  - The records on disk are the plan's reads 0..M−1 by construction, and `run()` now refuses any other set before a
    launch (O3's assert). Its case is a copy of a finished stage with one cell's file removed.
  - `check_report`'s form checks: a fire's batch begins at a multiple of the cadence; a fire at a read spans exactly
    the cadence's reads, ending there, and a read-less fire (the tail) fewer, its end not bound to the stage's last
    read (the values-check's observation 4; of the family of F3's optional bound, not taken); n is at most the span;
    the fires' tiles are disjoint, in launch order.
  - `check_stage_identity` refuses a cadence that is not positive (the alignment divides by it).
  - The binomial fixtures sit on aligned tiles: fires at 159, 319 and 479, and the tail from 0 or 160. One refuse
    case, a batch on a non-finite pause that did not fire it, still injects `example_pause`'s default batch, 341–500;
    draft 3 pins it to its check's message (the values-check's observation 2). `example_pause`'s docstring says a
    whole tile needs L + 1 to be a multiple of the cadence.
- **F3** (RISK), applied: the fires' trials and exceedances are summed and checked against the stage's state after the
  pause loop. `example_report` derives trials and `exceed_tau` from those sums (two fires: 320 trials, 2 exceedances).
  The optional bound on evaluations against the reads on disk is not taken. M4 is killed in the runner instead
  (the spent cap's evaluations are 0), and the bound would tie `example_report`'s and n-analyzer's fixtures to read
  counts beyond this delta.
- **F4** (NIT), applied: "(Code's reading, for the seat)" on the tile with no trial and on the tail of any reads, in
  `runner.py`'s PIN and in `BINOMIAL_STATE_FIELDS.evaluations`.
- **F5** (NIT), applied: "two exceedances in a tail shorter than a tile (2 of its 4 trials)" in the check's name, and
  "two fidelity exceedances" in its comment. A note beside the run-level binomial cases gives P = 0.00843 (2 of 4)
  and 0.00148 (2 of 2) against alpha 0.01 under p0 = 1/26, and 0.145 for one of 4.
- **M1–M8**, each met by a case that kills it:
  - M1: the first of the monitors' ten-read tiles is N1-P's reads; its fire's arms are ["N1-P"], and the tail's
    ["N1-V"], none carried over;
  - M2: the monitors' tile at a read with no re-computation has N2-E's reads without one; its fire's arms are
    ["N1-V"];
  - M3: a tile opening on a read with no re-computation has the batch (0, 3, 1, 1);
  - M4: a cap spent before any read reports 0 evaluations;
  - M5: a run whose tail (reads 4–5, at +1/2) has no re-computation ends COMPLETE with 2 evaluations;
  - M6: F1's case;
  - M7: n 161 over a tile of 160 is refused ("above the tile's span");
  - M8: a read-less tail of 159 reads is accepted, and one of 160 refused.
- **The observations:**
  - O1, O2, O5 and O7 ask for nothing: the tile matches R12; no report the runner can write is refused; p0 reaches no
    other check; and the R13 texts are right;
  - O3: applied, as the assert under F2;
  - O4, for the seat, in the runner's SCOPE PIN and in the entry: a binomial fire at a read with no re-computation
    stands on that read's arm too, though it had no trial in the tile (the schema holds a pause's read's arm in its
    scope);
  - O6, for the seat, in the entry, not applied: F5 as asserted admits p0 = 1 (3 of 3, say), which Laplace's rule
    excludes; at p0 >= 1 the binomial cannot fire, and `p0_count < p0_n` would close it;
  - O8: applied: two fires on adjacent tiles (160–319, 320–479) are accepted in the schema's own cases.
- **The reviewer's departures,** as its report states them, are in the delta's entry, for the seat to class.

## 2. The report as returned

BLIND REVIEW: the n runner delta (R12's tile, F5, R13's two texts)

Line numbers are the TO files' (S/step4b/tile/draft/runner.py and S/step4b/tile/draft/schema.py) unless a repository path is named.

Checked first:
- The brief's sha256 is fda516b3…e1ff, as the caller asked.
- The TO hashes match the brief: runner db18cb48…81dd, schema 21cbe294…b389.
- HEAD is db00d6d. Both FROM files are clean (rev-parse = hash-object) and last changed at 003ae7d.
- S/step4b/tile/selftest_run1.txt is 79c2940f…ef94 and reads "575/575 n selftest checks pass".
- My count of the runner's added checks agrees with 570 + 5: the monitors block stays at 5 checks, the tile block goes from 1 to 5 (+4), and the wbinom block from 1 to 2 (+1).

No BUG found.

FINDINGS

F1 — RISK — schema.py:2366-2367, with :1472-1473. The moved example leaves an existing case no longer testing what it was written to test.
- example_pause's fire at 500 is now the tile 341-500 with n 160, so n equals the span exactly.
- "a fire's batch not ending at its read" sets last_launch_index=499. That now breaks two checks: last ≠ li (:1472) and n 160 above the span 159 (:1474).
- The case has no `expect`, so :1472 can be disabled and the span clause still refuses it (M6).
- At HEAD the batch was 0-500 and the case was single-defect.
- Fix: `update(first_launch_index=340, last_launch_index=499)` (span 160 = n) with `expect="ends its batch at that read"`.

F2 — RISK — schema.py:1474-1479 (docstring :183-185; example_pause :1786-1798; rep_two :2382-2385). Code's tile checks are necessary but not exact, though the runner's tiles are exact.
- The records on disk are always launch indices 0..M−1 (O3). So tile j is exactly [j·c, (j+1)·c−1] and the tail is [J·c, M−1].
- So every fire at a read has first ≡ 0 (mod c) and span == c, and every read-less fire has first ≡ 0 (mod c) and span < c.
- The schema accepts batches no runner can write: a 4-read "tile" ending at a read (497-500, n 4), or a read-less "tail" over 0-300 with n 100. It checks the tail's shortness on n (trials), where R12 measures it in reads.
- Its own fixtures are such batches:
  - 341-500 and 141-300 are unaligned (real tiles end at 159, 319, 479, …).
  - example_pause(L) for L < 159 gives a short tile at a read, which its docstring calls "the cadence reads ending there".
- Fix: inside `if b is not None`, require `first % cadence == 0`; `span == cadence` when li is set; `span < cadence` when li is None. This subsumes :1477 and the cadence half of :1474.
- Put the binomial fixtures on aligned tiles: fires at 159 + 160·j (rep_binom_read at 479; rep_two at 319 and 479), and the tail starting at a multiple of 160.
- Pair this with O3's assert, so a gapped record set is refused before any launch rather than at the report.

F3 — RISK — schema.py:1484-1488, example_report :1763-1777, rep_two :2382-2385. The disjointness check at :1480 now bounds the fires' sums, but only each batch is checked alone.
- The bounds are Σn ≤ binomial_state.trials and Σk ≤ exceed_tau.
- The accept case "two fires on disjoint tiles" is a report no runner writes: two 160-trial tiles, each with k 1, in a stage of 160 trials and 1 exceedance. (example_report sets trials 160 and exceed_tau = max k.)
- Fix: sum n and k over the batches in the pause loop and compare after it. example_report should derive trials, exceed_tau and the N1-V|0 counter from those sums.
- Optional, same family: bind evaluations to the reads on disk, with R = Σ per_arm obtained: R//c ≤ evaluations ≤ R//c + (1 if R%c else 0). That kills M4 in the schema. The exact form (+1 iff R%c and the end is COMPLETE/CAP or the last pause is read-less) kills M5 too.

F4 — NIT — runner.py:33-47 (and schema.py:1200-1201). The brief declares two readings as Code's, for the seat, but the PIN states both as fact:
- a tile with no trial is evaluated and counted ("A tile with no trial is evaluated too, and cannot fire");
- the tail is evaluated whatever its trials ("however few").
- HEAD's paragraph marked its own readings "(Code's reading, for the seat)", and schema.py:183 marks Code's form checks the same way. Add the marker at both places.

F5 — NIT — runner.py:988-989 (and the comment at :955). The check name says "an exceedance in a tail shorter than a tile fires".
- The tail fires on two exceedances (reads 2 and 3) of four trials. Under the example's p0 = 1/26, one alone would not fire (P(X≥1|4) = 0.145).
- Fix: say "two exceedances". A note at :851-853 would also help: the run-level fires (rep_wb's 0-3 and rep7's tail, both 2 of 4) sit at P = 0.00843 against alpha 0.01.

SURVIVING MUTANTS (each passes the 575 and the schema's own battery, by my reading)

M1 — runner.py:240 `self.tile_arms = set()` → `pass`.
- Effect: a fire's scope accumulates every earlier tile's trial arms.
- Why it survives: all Monitors cases are N1-V only, and both of rep_wb2's tiles have the trial arms {N1-P, N1-V}.
- Kill: in m3c, make reads 0-3 `example_record(ident0, "N1-P", "valence", "+1", 3, launch=i)` and assert `a_tail == ["N1-V"]`.

M2 — runner.py:204 `self.tile_reads += 1` → `self.tile_reads += 1; self.tile_arms.add(rec["arm"])`.
- Effect: arms of non-trial reads enter the scope, against SCOPE ("the arms with a trial in its tile").
- Why it survives: m3's non-trial reads share the trial's arm and m3 never checks arms. rep_wb2's non-trial N2-E reads end at the firing read 7, whose arm is in scope anyway.
- Kill: in m3, make reads 1-3 `example_record(ident0, "N2-E", "span_reward", "f0.10", 3, launch=i)` and assert `k3[3][2] == ["N1-V"]`.

M3 — runner.py:205 `if self.tile_first is None:` → `if self.tile_first is None and f is not None:`.
- Effect: the batch's first becomes the tile's first trial, which is the old cumulative form. This contradicts the agreed "first and last are the tile's reads" and BINOMIAL_FIELDS.
- Why it survives: every fired tile in every test (m, m3, m3c, m9, rep_wb, rep_wb2, rep7, the driver's) opens on a trial. Only `last` is ever pinned at a non-trial read.
- Kill: an m3 variant with plain_at(0), rec_at(1, fresh_shift=0.5), plain_at(2), plain_at(3), expecting (0, 3, 1, 1).

M4 — runner.py:514 `if mon.pending():` → `if True:`.
- Effect: an empty tail is evaluated and counted. A COMPLETE campaign (7,680, 6,400 or 5,280 reads, all whole multiples of 160) would report 49, 41 or 34 evaluations, misreporting the lock's E.
- Why it survives: only rep10 (cap 0) ends with an empty tail, and its check reads end_state, obtained and hit. The driver never checks evaluations.
- Kill: assert `rep10["binomial_state"]["evaluations"] == 0`.

M5 — runner.py:514 `if mon.pending():` → `if mon.tile_trials > 0:`.
- Effect: a tail of reads with no trial goes unevaluated, against Code's declared reading.
- Why it survives: m3d tests pending() on the Monitors only, and every run that ends COMPLETE/CAP has trials in its tail. The driver's backend-ext reads are all trials.
- Kill: run `plan` (6 reads, unbiased backend) under ident with cadence 4, so reads 4-5 at +1/2 form a trial-less tail, and assert COMPLETE with evaluations 2.

M6 — schema.py:1472 `if li is not None and b["last_launch_index"] != li:` → `if False:`.
- Why it survives: see F1. The runner never writes last ≠ li.
- Kill: F1's fix.

M7 — schema.py:1474 `… - b["first_launch_index"] + 1` → `+ 2`.
- Effect: accepts n = span + 1, more trials than reads.
- Why it survives: the span case uses n 160 over a span of 101, far from the boundary; the accepts pin only n == span.
- Kill: refuse rep_binom_read with `first_launch_index=342` (span 159, n 160, within the cadence), `expect="the tile's span"`.

M8 — schema.py:1477 `b["n"] >= fr["cadence"]` → `>= fr["cadence"] - 1`.
- Effect: refuses a 159-trial tail, which the runner can write (a CAP after 159 d = 0 shadows, or a G-TIME-n tail). That would make run() refuse its own report.
- Why it survives: the cases pin 160 refused and 100 accepted.
- Kill: accept rep_end_binom with `last_launch_index=158, n=159`.

OBSERVATIONS

O1 (Q1) — The tile matches R12.
- The tile is the reads observed since the last evaluation (:204-207).
- It is evaluated at its cadence-th read outside the trial branch (:220-224).
- evaluate() resets after every evaluation, fired or not (:238-240), so the next tile starts after a fire just as after none.
- The tail is evaluated at a COMPLETE/CAP end when it holds any read (:513-523, :245).
- Every read lies in exactly one window.

Replay and the removed clear_batch:
- On a resume, replay (:424-441) re-observes the records from scratch and so rebuilds the same tiles.
- A prior fire is reproduced with the identical batch (:439), and the next record opens the next tile. That is what HEAD's clear_batch did at its :450-451, now done for every evaluation.
- The end-of-run pause is reproduced at :514-519. HEAD's clear after it (its :530) acted on nothing, so dropping it changes nothing.
- The self-test's clear_batch use was replaced by the next-tile checks (:615-625). rep_wb2 (:859-872) and rep8 (:993-999) exercise both replay paths.
- Outside HEAD's runner, no code in the repository references clear_batch, next_due or batch_* (git grep), and the TO runner has none.

O2 (Q2) — I found no report the runner can write that the new checks refuse.
- n ≤ the tile's reads ≤ cadence, and the reads sit at consecutive launch indices, so n ≤ span.
- A tail has fewer than cadence reads.
- Tiles are disjoint and in order, and the pause list is in launch order with the read-less fire last.

On the named cases:
- Rendering pauses skip no index: the invocation halts (:471-475) and the resume retries that place first (:454-456).
- A CAP end mid-tile evaluates the tail (:513-515), whose n < cadence, after the previous tile.
- A resume after an end-of-run fire reproduces that fire in place rather than appending it, so it stays last.
- A tile whose last read fires another kind carries the binomial in also_fired, with last == li.
- A stage whose first evaluation is the tail's has prev_last None and n < cadence.

O3 — R12's "reads launched since the previous evaluation" equals the runner's "records in launch-index order since the last evaluation" only because records on disk are always indices 0..M−1.
- That holds by construction: every pause halts, a rendering place is retried first, and CAP ends the stage.
- But replay asserts only unique indices and plan membership (:394-400). An assert `[r["launch_index"] for r in on_disk] == list(range(len(on_disk)))` would state the premise and refuse a damaged record set before any launch.

O4 — For the seat: R12's "a trial or not" lets a binomial fire stand on a read without a re-computation.
- SCOPE then puts that read's arm in scope though it had no trial in the tile. rep_wb2's fire at read 7 has scope [N1-P, N1-V, N2-E], and N2-E had no trial.
- The schema requires the read's arm in scope (:1435-1436), so the runner cannot drop it without a schema change.
- At HEAD a fire always stood on a trial. Under PIN-n-37 (a), this binds an arm that contributed nothing to the fire.

O5 (Q3) — p0 reaches no check outside the runner.
- valence_core/n/cells.py:268-269 and valence_core/n/gcal.py:655-660 run check_stage_identity on example identities, which F5 would refuse at (0, 2400). The move to (1, 26) was required.
- valence_core/n/primitive.py (test_identity :356-365), valence_core/n/hftiny.py:102 and valence_core/n/probe.py:176 use the example identity for geometry and the band only.
- The driver's p0 sites (scripts/n_sessions.py:662, :1244, :1840) are backend-ext's, pre-lock, so F5 does not apply. :1840's p0_count=1 still differs from 0.

The runner's run-level binomial cases now run under 1/26 (via test_identity, stage "time") and still test what they were written to test:
- rep_wb fires on 2 of 4 (P = 0.00843).
- rep_wb2 fires on 2 of 2 (P = 0.00148).
- rep7 and rep8 fire on 2 of 4.
- They would fail loudly, not pass silently, if p0 or alpha moved.
- The p0 = 0 form (backend-ext's real value) is now exercised only at the Monitors level.

scripts/n_analyze.py:
- It pins the schema at 003ae7d (:2766, refusal at :2789-2790), so it refuses this schema until its own pin-move commit.
- Its cumulative "from the clear" fixtures (:4718-4738; pb at :4752-4755) would be refused by the new checks.
- example_pause's read-less default (tail 0-99) cannot follow an earlier fire unless the batch is overridden.
- All of this is the move §8 item 6 assigns to n-analyzer.

O6 — F5 as asserted still admits p0 = 1 after the lock (e.g., 3 of 3), which Laplace's rule excludes (k ≤ n gives p0_count ≤ p0_n − 1). At p0 ≥ 1, binom_tail returns 1 (runner.py:90-91), so the binomial never fires. If the seat wants it, the clause `p0_count < p0_n` closes this.

O7 (Q4) — Both R13 texts are right.
- :43-45 is R13's sentence with "tile" in place of "window".
- :979-980 now reads "adjudicated".
- No text in either file says a ruling clears a batch. The runner's other uses are "a ruling clears nothing" (:39, :956).
- schema.py:166-167 ("An adjudicated pause is cleared, whatever the ruling …") and the case name at :2212 ("an adjudicated pause, cleared: COMPLETE") refer to the pause's standing. That is the sense of R12's own "a cleared fire".

O8 — The schema's own battery refuses first == prev_last but never accepts adjacent tiles (first == prev_last + 1), which the runner writes whenever consecutive tiles fire.
- A mutant `<= prev_last + 1` at :1480 dies only through the runner's rep_wb2 (tiles 0-3 and 4-7, checked at runner.py:540).
- The schema module's battery alone, which n-analyzer imports, would pass it.

DEPARTURES

1. shasum and Read of S/step4b/tile/review_brief.md, at the caller's instruction. That file is outside the brief's own list of S files. shasum is item 1's tool, though here it is a Perl script.
2. `sed -n 'a,bp'` line-range prints, with no substitution, on named repository files: valence_core/n/primitive.py, scripts/n_sessions.py (3 ranges), valence_core/n/cells.py, valence_core/n/gcal.py, valence_core/n/probe.py, valence_core/n/hftiny.py and scripts/n_analyze.py. Stated in case the seat counts sed as an interpreter.
3. Reads beyond the named sources, which I do not read as barred:
   - HEAD's runner.py and schema.py, by /usr/bin/grep -n and wc -l;
   - the modules in item 2, and scripts/n_analyze.py (read only);
   - all of the first sitting's answers raw;
   - the values-check raw's head and its full observation and departure lists.
4. Git commands, all in the brief's forms:
   - `git diff --no-index` on the named pairs;
   - rev-parse / hash-object and `log --format=%h` on the two named files;
   - two `git grep` runs with `-- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`, their output piped to grep for `.py` lines.

Otherwise none:
- No interpreter from the brief's list was run, nothing was written, and there was no network.
- No guard marker appeared in any argv, path or pattern.
- Nothing under data/*/ckpt, data/*/reports or data/mf3 was read, listed, sized or timed.
- In S I did no listing, glob, find or grep.
