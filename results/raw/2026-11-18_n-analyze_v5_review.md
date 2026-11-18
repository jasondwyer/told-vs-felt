# n_analyze.py, the seat's ruling of 2026-11-18 (second sitting) on PIN-n-33 to PIN-n-36 and its two questions: the blind review, its mutants and the dispositions (PI date 2026-11-18)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's ruling of the second sitting carried in`.

- **What changed under review.** The draft is compared against the committed analyzer (`a84833e`, sha256
  `509a62ad…85f6`). It carries §3 of the seat's answers of the second sitting,
  `results/raw/2026-11-18_n-step4-smoke-pause_design-to-code_answers.md` (sha256 `cdecf39e…01d3`, committed at
  `dc6a1cf`):
  - pauses read point by point (§3.1, PIN-n-33 amended), with a new reading of Code's on which points a pause stands
    on (PIN-n-37);
  - the fourth form's label in its sentence, in three fills (§3.2);
  - PIN-n-34 to PIN-n-36 accepted (§3.3);
  - the forms' digest moved.

  It was drafted in one step and run in a battery window the coordinating session granted: 219/221, then 221/221.
- **The review, blind** (§1). A reviewer read that draft, frozen as a read-only copy at sha256 `6f2dd349…301e` (221/221
  on those bytes, every one of its 224 coverage ids reached).
  - It was a subagent of this session. Its brief quoted the list of record v2's items 1–5 and the standing line that
    a git command in a check takes item 3's pathspec, and it allowed no Python.
  - Its specification: the answers raw's §3 and §6 item 6; the entry of `a84833e`, for what the seat ruled on; the
    first sitting's §5.2 and §5.6; PROPOSAL-n v0.2 §0.6, §2.1, §5 and §6; `valence_core/n/schema.py`; and the
    runner's pins and monitor in `valence_core/n/runner.py`.
  - It executed no code: it read files, ran `shasum`, `diff`, `grep`, `sed`, `awk` and `xxd`, and ran git with item 3's
    pathspec. It wrote one file, in its own scratch folder: the patterns it used to check that each mutant's old text
    occurs once. It opened nothing under `data/` and reported no departure.
  - It returned:
    - production findings F1–F6: F1 MINOR (a standing batch not bound to the runner's), F2–F6 NOTEs, no MAJOR;
    - battery findings B1–B7: B1–B4 MINOR, B5–B7 NOTEs;
    - 34 mutants, V01–V34. It predicted that 10 would survive the frozen copy (V03, V07, V08, V15, V16, V18, V24,
      V26, V27 and V28), V03 as equivalent on reports the runner writes.
- **The dispositions** (§2). Every finding is taken. F1 binds a standing batch to the runner's, and F2–F6 change
  registers and wording. B1–B7 give the battery new inputs:
  - two reader cases and a keyed-sample campaign;
  - three accepted standing batches, each bound as the runner counts a batch;
  - a new check (VD-PAUSE-RENDERING);
  - a guard paused at either f, and the beside's figures pinned;
  - two refusal inputs naming a planned read not on disk;
  - in VD-REFUSE, three new refusals and three rebuilt.
- **The mutants** (§3). The set is the reviewer's 34, five of them re-expressed on the fixed draft's text, and 16 of
  Code's. They ran once each, on the fixed draft (sha256 `83f54ec6…d04c`, 222/222, every one of its 225 coverage ids
  reached): **49 of 50 killed.** V03 survived, as the reviewer predicted: it is equivalent on reports the
  runner writes. The other nine it predicted would survive are killed, each by a check the dispositions added or
  extended.
- **The battery runs** (§4) and **the committed bytes** (§5). The committed file differs from the mutation-tested base
  in the repository line and, from the values-check, in ten texts (§5).
- **The tallies** (§6): unchanged from `a84833e`'s, except for the fourth form's form string. The fourth form's 640
  evaluations are split by its label's fill.

Every Python run here was inside a battery window the coordinating session granted, on bytes named to it first by
sha256. Each ran as one process at a time, at `nice -n 19` with `-I`, with temp folders outside the repository, in the
foreground. The interpreter was reached by `cd` into the venv's bin by glob, so no argv named its path. Nothing ran on
a model or on the box.

Each mutant was applied to a copy of its base as an exact text replacement (`.old` → `.new`), asserted to occur once.
Before its window, the mutated file's sha256 was entered in a manifest named to the coordinating session. Each file was
checked against that manifest before its battery ran with `--selftest`. "Killed" means a non-zero exit.

## 1. The reviewer's report, as saved from its hand-back (unedited)

The reviewer returned its report as its final message. Code saved it by script from the subagent's transcript, as
`review/reviewer/report.md` in its scratch (sha256 `6010bc30…da87`). Its headings are moved down two levels here, and
nothing else is changed. Line numbers in it are the frozen copy's.

Blind review of the n_analyze.py v5 draft (the frozen copy 6f2dd349…301e)

I verified the inputs first. The brief hashes to f7fee979…f6eb and the frozen copy to 6f2dd349…301e, both as given. Regenerating `diff -u` from base to frozen copy reproduces the supplied diff (38 hunks) byte for byte. The base hashes to 509a62ad…85f6, a84833e's sha256 as the RESULTS entry gives it. `valence_core/n/schema.py` has no diff against d791bd9 and hashes to the analyzer's pin (0ea39600…0db6).

I ran no Python. I worked by reading, plus `shasum`, `diff`, `grep`, `sed`, `awk` and `xxd`. Every git command I ran carried item 3's pathspec. I touched nothing under `data/`. I wrote one file, `SCRATCH/review/reviewer/patterns.txt`, which I used to check that each mutant's old text occurs exactly once. No departures to report.

#### What checks out

- **§3.1 is applied at every place it should be.**
  - `State.paused_on` looks up the point. A literal state still reads the pause per arm.
  - `n2_outcome` takes its pause causes at N2-E at the decision f, and at N1-V, N1-R and N1-P at the norm-matched point m.
  - The beside's new `paused` list checks the other f's four reads.
  - `build_state` copies the map into `State`.
  - `run_verdicts` builds both the primary row and the TAU/4 row from the same `paused_points` map.
  - N1 (through `_causes`), dose (through N1), N4 and the guards' flag stay per arm, as PIN-n-37 says.
  - An INDETERMINATE N2 still reports no beside.
  - In reports the runner writes, every steered arm in a standing pause's scope gets at least one point. So "per arm" equals "any point" for N1, N4 and the guards.
- **PIN-n-37 is consistent with the schema, the runner and §3.1.**
  - It narrows the schema's "a pause stands on its scope's arms" to points inside that scope.
  - It matches the runner's pins:
    - trials are the reads that carry a re-computation (dose rule and keyed sample);
    - a batch runs from the first trial after the last adjudicated fire and ends at the read that fired it;
    - a shadow pause's scope adds the arms paired with that session.
  - Both stated alternatives are accurate, and the launch-order claim holds (it needs the 160 cadence; see F4).
  - Its keys match `State.at` (`label_values` plus the f labels).
  - `report_problems` runs before `paused_points`, so a pause read outside the plan never reaches the `lv[...]` lookup.
- **The new bindings accept everything the runner writes.** I traced `Monitors.observe`, `evaluate` and `clear_batch`. A standing batch's ends are trials, and its n and k are the trials in its range, because no clear falls inside a batch. Every runner pause names a read of the plan.
- **§3.2, character for character:**
  - `LABEL_TAIL` is " — [label]": an em dash (U+2014) with a space each side, byte-equal to the raw's quoted tail.
  - `CNA_N4` equals the raw's italic fill.
  - `F4` is each readability branch plus `LABEL_TAIL`; `D_FOURTH` adds the merge slot.
  - `sentence_dose` has the three fills:
    - "answered" exactly when `label()` gives answered;
    - `CNA_N4` with N4's state when G-READ-n passes;
    - CNA otherwise.
  - The oracle's `_ORC_TAIL`, `_ORC_N4` and its fill agree.
  - The three copies of the form string (`FORM_FOURTH`, the oracle's, the tallies') are identical, and no copy of the first sitting's form string is left.
  - `[label]` and `[n4]` are in `SLOTS`, so `fill()` stops on any slot left.
  - The 64 / 256 / 320 split of the 640 evaluations re-derives by hand. T2 compares all 2,561 evaluations against the oracle.
- **Registers.**
  - PIN-n-33's new text carries §3.1's amended first half and keeps the guard half. "Superseding §1.6's sentence" is §3.1's own wording.
  - PIN-n-34 to -36 are marked accepted in the header, the same way -27, -28 and -31 were; their texts are unchanged.
  - PIN-n-37 is strikable.
  - The module docstring and the forms comment are updated. The comment's raw digest (cdecf39e…01d3) matches the raw.
  - `CODE_FORMS_SHA256` moved along with `RULING_FORMS`. I did not recompute it; per the brief, SENT-CODE-FORMS passed on these bytes.
  - `EXPECTED_CHECKS` is 221, which is 217 plus the four new checks, each with its coverage id.

#### Findings: production code

**F1, MINOR.** `report_problems`, lines 5283–5290 (docstring 5235–5237), read by `paused_points` at 5384–5387.
- **What's wrong:** A standing batch is checked only against the records inside its own range: its ends must be trials, and n and k must be the range's. It is not checked against the batch the runner would have counted. That batch is fixed by the records and the earlier pauses:
  - it starts at the first trial after the latest adjudicated binomial pause's batch, or the stage's first trial if there is none;
  - a fire at a read ends it at that read (the schema checks this);
  - a read-less run's-end fire ends it at the stage's last trial.

  So the start, and a read-less batch's end, are unbound. An outcome now reads that range, so this matters where it didn't before.
- **Failure scenario:**
  1. p01 fires and is adjudicated at read 159 (batch [0, 159]).
  2. The run completes. The run's-end evaluation fires p02, with the runner's batch [160, last N4-Ts read]. That batch includes N2-E's keyed-sample reads at the decision f.
  3. The PI stops the unit.

  A report giving p02's batch as [first N2-S trial, last N4-Ts read], with that range's own n and k, passes `report_problems`. `paused_points` then stands p02 on N2-S, N2-C and N4 only, so N2 is decided where the runner's batch makes it INDETERMINATE. The battery's own VD-PAUSE-POINTS input has this shape (see B6).
- **Fix:** Also require:
  - `first_launch_index` is the first trial after the latest adjudicated binomial batch's `last_launch_index` (or the stage's first trial);
  - for a read-less batch, `last_launch_index` is the stage's last trial;
  - optionally, `arms_in_scope` holds the arms of the batch's trials (the runner's SCOPE).

**F2, NOTE.** PINS["PIN-n-24"], lines 2414–2421.
- **What's wrong:** Its accepted clause "a pause standing (under PI-STOP only) making the arms in its scope INDETERMINATE" is the per-arm reading. PIN-n-33 as amended replaces that reading for N2.
- **Scenario:** In VD-PAUSE-POINTS the scope is N1-P, yet N2, which reads N1-P, is decided. The register now states two rules.
- **Fix:** Annotate PIN-n-24, or say in PIN-n-37 that PIN-n-24's clause means N1 and N4 per arm and N2 by the points PIN-n-37 reads. Flag it to the seat rather than rewriting an accepted PIN.

**F3, NOTE.** OPEN-Q8 (2536–2539), OPEN-Q3 (2519–2522), the OPEN header (2511–2513) and the module docstring (16–21).
- **What's wrong:**
  - OPEN-Q8 lists the form amendments up to §5.6 but not §3.2 (the label in the sentence).
  - OPEN-Q3 describes the fourth form in the cell where G-READ-n passes and N4 does not, but without its new "(N4 [n4])".
  - The OPEN header and the docstring name the first sitting's raw by path, but the second sitting's only as "those of its second sitting, §3".
- **Scenario:** A reader of the registers won't find where the fourth form's label was ruled.
- **Fix:** Add §3.2 to OPEN-Q8 and to OPEN-Q3's cell, and add the second sitting's path to the OPEN header and the docstring.

**F4, NOTE.** PIN-n-37, lines 2501–2504.
- **What's wrong:** "A batch from the stage's start holds every shadow… a later batch holds none" is true only at n §2.1's cadence of 160 reads (the identity's `fidelity_rule.cadence`). At that cadence the first evaluation falls on the 160th read, which is the last shadow. A cap reached before read 159 also leaves a run's-end batch holding only the shadows launched. The PIN states neither condition.
- **Scenario:** At a cadence below 160, a first batch could fire before every shadow is launched, and a later batch would then hold the rest.
- **Fix:** Add "at n §2.1's cadence of 160 reads".

**F5, NOTE.** PIN-n-37 (2497–2500) and `paused_points` (5388–5394), against the runner's `_scope` (runner.py 290–296, 487–491, 507).
- **What's wrong:** The runner applies its shadow clause only to the read that fired. A binomial fire's scope is that read's arm and pairing plus the arms of the batch's trials. PIN-n-37's extension through a batch's shadows is therefore Code's own, capped by the runner's scope, not "the runner's SCOPE carried to the point".
- **Scenario:** In the runner's order the first evaluation is at read 159, which is the shadow of neu_b5/159, a neutral session. That fire's scope is N1-V, N1-P, N2-E, N2-S and N2-C, with no N1-R. Yet its batch holds the 40 floor shadows that N1-R's reads pair with, so the analyzer stands it on no N1-R read. No outcome changes: N1 is INDETERMINATE through N1-V, and N1-R is incomplete at that point.
- **Fix:** Say in the PIN that the extension is Code's and capped by the scope. Tell n-build that its binomial-fire scope does not follow its own shadow clause through the batch.

**F6, NOTE.** `sentence_dose` line 785 and `oracle_set` lines 1063–1064.
- **What's wrong:** The fills chain conditionals without parentheses (`a if c1 else b if c2 else c`, and the oracle's `x + y if c else z`).
- **Scenario:** None; both evaluate as §3.2 requires.
- **Fix:** Add parentheses so the precedence is visible.

#### Findings: the battery

**B1, MINOR.** RD-PAUSE-POINTS (3811–3855) and VD-PAUSE-POINTS (4449–4466).
- **What's wrong:** Every batch range tested is a single dose-rule cell or a single shadow. The synthetic campaign re-computes only at 0 and ±1 (`example_record`'s "auto") and has no keyed-sample reads. So no tested range contains a read without a re-computation.
- **Scenario:** PIN-n-37's reading ("the reads carrying a re-computation in its range") can't be told apart from its own first alternative ("every read launched in its range"). V16 survives, so the check's description asserts the reading without testing it.
- **Fix:** Add a range spanning N1-P's +d_20, +d_eq and −1 cells (only −1 re-computed), wanting {(N1-P, −1)}. Add a few reads written with `fidelity="sample"` at a non-dose-rule point inside a range.

**B2, MINOR.** The same checks; the shadow test at line 5390.
- **What's wrong:** No batch range holds an N4 read under a steered scope.
- **Scenario:** `(arm, lab) == ("N1-V", "0")` can't be told from `lab == "0"`. V18 survives: N4's d = 0 reads are taken for shadows and the batch then stands on every session's reads. In the runner's order every run's-end batch ends in N4's dose-rule reads, so this is the realistic shape at a PI-STOP.
- **Fix:** Add a batch over the first N4-T reads with scope ["N1-V", "N4-T"], wanting the empty set.

**B3, MINOR.** VD-REFUSE's batch cases (4703–4731) and VD-PAUSE-POINTS.
- **What's wrong:**
  - Only the last end is ever tested on its own.
  - Every standing batch tested is read-less.
  - The only standing batch accepted is a pure dose-rule cell.
- **Scenario:** V26 (dropping the first-end check), V28 (binding read-less batches only) and V27 (requiring every read in the range to be a trial) all survive. "Nothing refuses a report the runner can write" is never shown for a runner-shaped batch.
- **Fix:**
  - Add a "batch-start" refusal: `first_launch_index` moved back onto a read with no re-computation, n and k unchanged.
  - Accept a standing batch over N1-P's +1 through −1 cells (n 320, k 0).
  - Add a read-bearing standing batch at launch index m − 1.

**B4, MINOR.** "pause-not-planned" (4706–4709) and RD-PAUSE-POINTS's "a rendering pause's read" case (3832–3833).
- **What's wrong:** No accepted report has a pause whose read is not on disk, and the "rendering pause" case uses a read that is on disk.
- **Scenario:** V24 survives: replacing the plan with the reads on disk would refuse every PI-STOP report with a standing rendering pause. V15 survives: a standing rendering pause would stand on nothing, so PIN-n-37's "not on disk, by its id" is untested.
- **Fix:** Run VERDICTS under PI-STOP on a campaign with N2-C's f0.20, N4-T and N4-Ts cells omitted, plus a standing rendering pause at m naming N2-C's first f0.20 read. Expect it accepted, with pause_points ["N2-C@f0.20"], the guard flag set and N2 decided.

**B5, NOTE.** N2-PAUSE-POINTWISE (1405–1429).
- **What's wrong:** The guard's flag is tested only for a guard paused at N2's decision f. The beside is tested only by its `paused` list, not by its figures.
- **Scenario:** V07 (a pointwise guard flag) and V08 (beside figures turned "not computed" where a pause stands) both survive, though PIN-n-37 keeps the flag per arm and the figures computed.
- **Fix:** Add a case pausing N2-S at the other f (f_o), wanting the flag True. In the N2-E-at-f_o and N1-P-at-mo cases, compare the beside's figures with the unpaused state's.

**B6, NOTE.** VD-PAUSE-POINTS's input.
- **What's wrong:** It is a read-less "run's end" batch that ends mid-campaign at N1-P's −1 cell. The runner never writes that; its run's-end batch runs to the stage's last trial.
- **Scenario:** The check still tests the wiring, but it rests on F1's gap and would be refused once F1's binding is added.
- **Fix:** Rebuild the input:
  - first an adjudicated fire ending at N1-P's +1 cell;
  - then a run's-end batch from N1-P's −1 cell to the end;
  - pause_points stays ["N1-P@-1"], and N4 becomes INDETERMINATE through its scope.

**B7, NOTE.** The `bz` and `rs` refusal inputs (4584–4586, 4595–4596).
- **What's wrong:** They name N1-V|valence|-1/2|floor_b0/3, which is not a read of the plan, so each now also trips the new plan check.
- **Scenario:** Both still pass on their own message, but each input now has two defects instead of one.
- **Fix:** Name a planned read that is not on disk, from a campaign with a cell omitted.

#### Mutants

34 mutants; 10 predicted to survive (V03, V07, V08, V15, V16, V18, V24, V26, V27, V28). V03 is equivalent on reports the runner writes. The other survivors map to B1–B5.

```
@@ V01 | State.paused_on | a literal state's pause stands on nothing | predicted: killed by N2-INDET-pause:N2-E, N2-INDET-pause:N1-V, N2-INDET-pause:N1-R, N2-INDET-pause:N1-P, RD-PAUSE
            return bool(self.paused.get(arm))
~~
            return False
@@ V02 | State.paused_on | a point lookup widened to any point of the arm (per arm again) | predicted: killed by N2-PAUSE-POINTWISE, VD-PAUSE-POINTS
        return bool(self.paused_at.get((arm, key)))
~~
        return any(v for (a, _k), v in self.paused_at.items() if a == arm)
@@ V03 | State.paused_on | an empty point map read as a literal state (per arm) | predicted: survives (equivalent on reports the runner writes: every steered arm in a standing pause's scope gets a point, so an empty map means no steered arm is paused)
        if self.paused_at is None:
~~
        if not self.paused_at:
@@ V04 | n2_outcome | N2's pause causes read per arm | predicted: killed by N2-PAUSE-POINTWISE, VD-PAUSE-POINTS
    causes = [f"pause:{a}" for a, k in reads if st.paused_on(a, k)] + [c for a, k in reads for c in st.named_at(a, k)]
~~
    causes = [f"pause:{a}" for a, k in reads if st.paused.get(a)] + [c for a, k in reads for c in st.named_at(a, k)]
@@ V05 | n2_outcome | the beside's paused list taken at the decision f's reads (always empty on a decided N2) | predicted: killed by N2-PAUSE-POINTWISE
                      "paused": [a for a, k in n2_reads(st, f_bes) if st.paused_on(a, k)]},       # PIN-n-37
~~
                      "paused": [a for a, k in n2_reads(st, f_dec) if st.paused_on(a, k)]},       # PIN-n-37
@@ V06 | n2_outcome | the beside's paused list per arm | predicted: killed by N2-PAUSE-POINTWISE
                      "paused": [a for a, k in n2_reads(st, f_bes) if st.paused_on(a, k)]},       # PIN-n-37
~~
                      "paused": [a for a, k in n2_reads(st, f_bes) if st.paused.get(a)]},       # PIN-n-37
@@ V07 | n2_outcome | a guard's flag read at N2's decision f only (a guard paused at the other f shows unpaused) | predicted: survives
                         | {"paused": bool(st.paused.get(a))}
~~
                         | {"paused": st.paused_on(a, f_dec)}
@@ V08 | n2_outcome | a pause at the beside's reads turns its figures 'not computed' | predicted: survives
    ok = {a: not st.causes_at(a, k) for a, k in n2_reads(st, f_bes)}
~~
    ok = {a: not st.causes_at(a, k) and not st.paused_on(a, k) for a, k in n2_reads(st, f_bes)}
@@ V09 | build_state | the reader's points dropped (every pause read per arm) | predicted: killed by VD-PAUSE-POINTS
               unusable=unusable, paused_at=None if paused_at is None else dict(paused_at))
~~
               unusable=unusable, paused_at=None)
@@ V10 | run_verdicts | the primary row built without the points | predicted: killed by VD-PAUSE-POINTS
    st, fig = build_state(camp, paused=paused, gread=g, paused_at=pat)
~~
    st, fig = build_state(camp, paused=paused, gread=g)
@@ V11 | run_verdicts | the TAU/4 row built without the points | predicted: killed by VD-PAUSE-POINTS
    st_s, fig_s = build_state(camp, paused=paused, gread=g, drop=tau4_drop(camp), paused_at=pat)
~~
    st_s, fig_s = build_state(camp, paused=paused, gread=g, drop=tau4_drop(camp))
@@ V12 | paused_points | adjudicated pauses still stand | predicted: killed by RD-PAUSE-POINTS
        if q["adjudicated"]:
~~
        if q["adjudicated"] is None:
@@ V13 | paused_points | N4's arms kept in the scope (N4 marked at d = 0) | predicted: killed by RD-PAUSE-POINTS
        scope = sorted(set(q["arms_in_scope"]) & set(STEERED_ARMS))
~~
        scope = sorted(set(q["arms_in_scope"]))
@@ V14 | paused_points | N2's f labels swapped | predicted: killed by RD-PAUSE-POINTS
    lv = label_values(camp.identity) | {"f0.10": F10, "f0.20": F20}
~~
    lv = label_values(camp.identity) | {"f0.10": F20, "f0.20": F10}
@@ V15 | paused_points | a pause's read marked only when its record is on disk (a standing rendering pause stands on nothing) | predicted: survives
        rids = [] if q["read_id"] is None else [q["read_id"]]
~~
        rids = [] if q["read_id"] not in camp.records else [q["read_id"]]
@@ V16 | paused_points | a batch stands on every read launched in its range (PIN-n-37's first alternative) | predicted: survives
            rids += sorted(rid for rid, r in camp.records.items() if r["fidelity"] is not None
                           and b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
~~
            rids += sorted(rid for rid, r in camp.records.items()
                           if b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
@@ V17 | paused_points | a batch's last read excluded | predicted: killed by RD-PAUSE-POINTS ("a binomial batch of one shadow")
            rids += sorted(rid for rid, r in camp.records.items() if r["fidelity"] is not None
                           and b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
~~
            rids += sorted(rid for rid, r in camp.records.items() if r["fidelity"] is not None
                           and b["first_launch_index"] <= r["launch_index"] < b["last_launch_index"])
@@ V18 | paused_points | any d = 0 read taken for a shadow (N4's reads pair with every session's reads) | predicted: survives
            if (arm, lab) == ("N1-V", "0"):                # a shadow (N1-V|none|0): its session's reads pair with it
~~
            if lab == "0":                # a shadow (N1-V|none|0): its session's reads pair with it
@@ V19 | paused_points | a batch's shadows not carried to their sessions (only the pause's own read) | predicted: killed by RD-PAUSE-POINTS ("a binomial batch of one shadow")
            if (arm, lab) == ("N1-V", "0"):                # a shadow (N1-V|none|0): its session's reads pair with it
~~
            if (arm, lab) == ("N1-V", "0") and rid == q["read_id"]:  # a shadow (N1-V|none|0): its session's reads pair with it
@@ V20 | paused_points | a shadow's pairing leaves the pause's scope (every steered arm) | predicted: killed by RD-PAUSE-POINTS ("the same shadow, its scope N1-V alone")
                for a in scope:
~~
                for a in STEERED_ARMS:
@@ V21 | paused_points | the shadow's own point (N1-V at 0) marked | predicted: killed by RD-PAUSE-POINTS (the shadow cases)
                        if psid == sid and (pa, plab) != ("N1-V", "0"):
~~
                        if psid == sid:
@@ V22 | paused_points | a read outside the pause's scope marked | predicted: killed by RD-PAUSE-POINTS ("the same batch outside its scope", "N4's pause")
            elif arm in scope:
~~
            else:
@@ V23 | report_problems | a rendering pause's read outside the plan accepted | predicted: killed by VD-REFUSE ("pause-not-planned")
        if rid not in planned:
~~
        if rid not in planned and q["kind"] != "rendering":
@@ V24 | report_problems | the plan replaced by the reads on disk (refuses a standing rendering pause, whose read is not launched) | predicted: survives
    planned = set().union(*camp.planned.values())
~~
    planned = set(camp.records)
@@ V25 | report_problems | a standing batch's k not compared | predicted: killed by VD-REFUSE ("batch-exceedances")
                    or (len(trials), sum(x for _, x in trials)) != (b["n"], b["k"]):
~~
                    or len(trials) != b["n"]:
@@ V26 | report_problems | a standing batch's first end not compared | predicted: survives
            if not trials or (trials[0][0], trials[-1][0]) != (b["first_launch_index"], b["last_launch_index"]) \
~~
            if not trials or trials[-1][0] != b["last_launch_index"] \
@@ V27 | report_problems | over-refusal: every read in the range must carry a re-computation (refuses the runner's batches) | predicted: survives
                    or (len(trials), sum(x for _, x in trials)) != (b["n"], b["k"]):
~~
                    or (len(trials), sum(x for _, x in trials)) != (b["n"], b["k"]) \
                    or len(trials) != b["last_launch_index"] - b["first_launch_index"] + 1:
@@ V28 | report_problems | only read-less standing batches bound | predicted: survives
        if b is not None and not q["adjudicated"]:
~~
        if b is not None and not q["adjudicated"] and q["read_id"] is None:
@@ V29 | sentence_dose | the fourth form's fill is the bare §0.6 label (no "(N4 [n4])") | predicted: killed by TUP-T2, SENT-FOURTH-FILLS, SENT-FILLED-DOSE-FOURTH
            fill = lab if lab == ANSWERED else CNA_N4.replace("[n4]", n4) if gr == "PASS" else CNA
~~
            fill = lab
@@ V30 | sentence_dose | the parenthetical gated on N4 not PASS instead of G-READ-n PASS | predicted: killed by TUP-T2, SENT-FOURTH-FILLS, SENT-FILLED-DOSE-FOURTH
            fill = lab if lab == ANSWERED else CNA_N4.replace("[n4]", n4) if gr == "PASS" else CNA
~~
            fill = lab if lab == ANSWERED else CNA_N4.replace("[n4]", n4) if n4 != "PASS" else CNA
@@ V31 | LABEL_TAIL | an en dash for the em dash | predicted: killed by SENT-RULING, TUP-T2, SENT-FOURTH-FILLS
LABEL_TAIL = " — [label]"
~~
LABEL_TAIL = " – [label]"
@@ V32 | F4 | the not-readable branch loses its tail | predicted: killed by SENT-RULING, TUP-T2
      "not readable": FOURTH.replace(READ_ALT, NOT_READABLE) + LABEL_TAIL}
~~
      "not readable": FOURTH.replace(READ_ALT, NOT_READABLE)}
@@ V33 | CNA_N4 | the fill's parenthetical changed to "(N4: [n4])" | predicted: killed by SENT-RULING, TUP-T2, SENT-CODE-FORMS
CNA_N4 = "concluded, not answered (N4 [n4])"
~~
CNA_N4 = "concluded, not answered (N4: [n4])"
@@ V34 | FORM_FOURTH | the first sitting's form string restored | predicted: killed by TUP-T2, TUP-T10
FORM_FOURTH = "the seat's answers of 2026-11-18 §5.6, with §5.4's note and the second sitting's §3.2 label"
~~
FORM_FOURTH = "the seat's answers of 2026-11-18 §5.6, with §5.4's note"
```

## 2. Code's dispositions

Every finding is taken. None changes an outcome, a sentence or a form on a report the runner writes. F1 adds bindings,
and the rest are registers, wording and battery inputs.

### Production code

- **F1 (MINOR), a standing batch bound to the runner's.** Taken. `report_problems` now requires a standing pause's
  batch to be the one the runner counts:
  - its first read is the first trial after the last cleared batch, or the stage's first trial where none was
    cleared. A cleared batch is an adjudicated pause's batch with a read; the runner clears a batch when it replays
    such a pause;
  - its last read is the fire's read, or the stage's last trial for a fire at the run's end;
  - its n and k are those of the trials in that range, k counting those above TAU;
  - its scope holds the arms of those trials (the review's optional clause).

  The draft's conjunct "the last read is a trial" is dropped. The runner fires only at a trial, and the bindings
  above fix the batch. The docstring and PIN-n-37 say so.
- **F2 (NOTE), PIN-n-24's per-arm clause.** Taken in PIN-n-37, not in PIN-n-24, which the seat accepted. PIN-n-24's "a
  pause standing (under PI-STOP only) making the arms in its scope INDETERMINATE" is read as N1's and N4's per-arm
  rules, and for N2 through PIN-n-37's points. It is flagged for the seat with PIN-n-37.
- **F3 (NOTE), the registers.** Taken:
  - OPEN-Q8 names the second sitting's §3.2, the label in the sentence in three fills.
  - OPEN-Q3 names the fourth form's label in the cell of §7.2.
  - The OPEN header and the module docstring name the second sitting's raw by path.
- **F4 (NOTE), the launch-order claim.** Taken. PIN-n-37 now reads "Under the runner's launch order (…) and n §2.1's
  cadence of 160 reads, a batch from the stage's start holds every shadow launched".
- **F5 (NOTE), the shadow extension through a batch.** Taken. PIN-n-37 now calls the extension Code's own, capped by
  the scope, and so, after the values-check, does `paused_points`' docstring. The runner's SCOPE applies its shadow
  clause only to the read that fired. That point is n-build's: Code sent it to the coordinating session, which
  relayed it to n-build as information. It is flagged for the seat in PIN-n-37 and applied nowhere.
- **F6 (NOTE), precedence.** Taken. `sentence_dose`'s fill and the oracle's are parenthesized. The behaviour is
  unchanged.

### The battery

- **B1 (MINOR), ranges holding reads with no re-computation.** Taken. RD-PAUSE-POINTS adds two cases on a range over
  N1-P's +d_20, +d_eq and −1 cells:
  - on the battery's campaign, where −1 alone is re-computed: {N1-P at −1};
  - on a new campaign with two +d_eq reads on the keyed sample: {N1-P at d_eq, N1-P at −1}. The campaign builder gains
    the option `sampled` for this.

  Code had already added two cases before the report: a range holding no trial, and an N4 trial under a steered scope.
  RD-PAUSE-POINTS now has fourteen cases.
- **B2 (MINOR), an N4 read under a steered scope.** Taken, by a case Code had already added: "an N4 trial is no shadow",
  N4-Ts's d = 0 read under the scope [N1-V, N4-Ts], wanting the empty set.
- **B3 (MINOR), runner-shaped standing batches.** Taken. VD-PAUSE-POINTS now accepts three standing batches, each
  bound as the runner counts a batch:
  - **A.** A fire adjudicated at N1-P's last +1 read, then the run's-end batch from N1-P's first −1 read to the stage's
    last trial, on a campaign with one N1-P −1 read above TAU (k = 1). Its range holds N2's reads, none of them
    re-computed.
  - **C.** The same clear, then a non-finite read at m − 1 that also fires the binomial, its batch ending at that read.
  - **B.** A run's-end batch from the stage's first trial, after an adjudicated pause with no batch. It holds 80 reads
    above TAU/4 and none above TAU, so k = 0, and one re-computation non-finite on the fresh path, which counts as a
    trial.

  Their extent, n, k and scope follow the runner's counting. Their fires are not ones the runner would write on these
  campaigns. Under p0 = 0 no fire comes at k = 0, and A's k = 1 batch would fire at its cadence point, at N1-P's last
  −1 read, not at the run's end. The analyzer binds a batch, not the schedule or the condition of its fire (the
  values-check's O2).

  VD-REFUSE adds three refusals:
  - batch-start, the first read moved back onto a read with no re-computation;
  - batch-scope, the scope without N1-P;
  - batch-read-count, C's batch with its count one more.

  It rebuilds the draft's batch-count, batch-exceedances and batch-end on A's batch. batch-end now ends one trial
  short of the stage's last.
- **B4 (MINOR), a standing pause whose read is not on disk.** Taken. VD-PAUSE-RENDERING is a new check: under PI-STOP, a
  rendering pause stands at m, its read N1-P's first −1 read, planned and not on disk because the cell is omitted. It
  is accepted, it stands on N1-P at −1, and N2 is decided.
- **B5 (NOTE), the guard's flag and the beside's figures.** Taken. N2-PAUSE-POINTWISE adds a guard paused at the other
  f, and compares a decided N2's beside figures with the unpaused state's.
- **B6 (NOTE), a batch no runner writes.** Taken, as B3's scenario A. The draft's read-less batch ending inside the
  campaign is gone. A batch on N1-V's +1 cell alone, which Code added to its working copy after the freeze and never
  ran, went with it.
- **B7 (NOTE), bz and rs.** Taken. Both now name N1-P's −1 read of session 3. It is planned and not on disk in the
  campaign whose −1 cell is omitted, so each input trips only its own check.

### The mutants

The mutant set is the reviewer's 34 (V01–V34) and 16 of Code's.
- **Re-expressed.** Five of the reviewer's mutants target lines that F1 or F6 rewrote: V25, V26, V27, V29 and V30.
  Their old text no longer occurs in the fixed draft, so each is re-expressed on the new text with its intent kept.
- **Code's.** Code drafted 28 mutants before the report arrived. Of these:
  - eleven are kept: eight as drafted (C01, C06, C11, C16, C17, C20, C25, C27), and C14, C15 and C19 re-expressed on
    the fixed draft. C19 targets F6's parenthesized line. C14 and C15 are kept because no other mutant covers the
    batch's count, or exceedances counted at TAU/4;
  - sixteen are dropped as the reviewer's own;
  - C13 (both ends unbound) is dropped as covered by V26 and C30.

  Five are added on F1's binding (C29–C33).

## 3. The mutants and their run

**The set.** There are 50 mutants: the reviewer's 34 and 16 of Code's.
- The reviewer's V01–V34 are applied as written, except V25, V26, V27, V29 and V30. Those five target lines that F1
  or F6 rewrote, so their old text no longer occurs in the fixed draft. Each is re-expressed on the new text, with its
  intent kept, and reproduced below the table.
- Code's sixteen are reproduced whole below the table.
  - Code wrote 28 while the review ran. Sixteen of them duplicate one of the reviewer's, and were dropped:
    - twelve make the reviewer's change: C02, C04, C07, C08, C09, C10, C12, C21, C23, C24, C26 and C28, as V04, V13,
      V18, V17, V16, V14, V25, V05, V11, V10, V32 and V21 do;
    - four make it another way, with the same effect: C03, C05, C18 and C22, on the lines of V12, V20, V29 and V09.

    C13 (both ends unbound) was dropped too, as V26 and C30 cover it.
  - The eleven kept are C01, C06, C11, C14, C15, C16, C17, C19, C20, C25 and C27. C14 and C15 are re-expressed on the
    fixed draft, and C19 on F6's parenthesized line.
  - Five are new, on F1's binding: C29–C33.

All 28 as first written are in Code's scratch. Code checked them, when written, against the working draft they were
written on. Before the window, the old text of each of the 50 run was checked to occur exactly once in the mutant base.

The predictions in the table are their authors': the reviewer's as written, and Code's from the spec it ran. Code
revised three of its own when the dispositions added checks after the mutants were drafted. C01's and C25's now name
VD-PAUSE-RENDERING, and C17's names the batch cases in place of three of them. The five re-expressed blocks below the
table carry Code's predictions on the fixed draft; the table gives the reviewer's.

**The run.** The base was the fixed draft, frozen as a read-only copy at sha256
`83f54ec6e51cd9ffd70f92a427e865290dce27651b125cfad32e604187c1d04c`.
- Its battery passed 222/222, with every one of its 225 coverage ids reached.
- Each mutated file was entered in the manifest by its sha256 (`e2cf9684…d6d0`). Each was checked against the manifest
  before its run, and each ran once, one battery process at a time, in four batches.
- **49 of 50 were killed.** V03 survived, as the reviewer predicted: it is equivalent on reports the runner
  writes. The other nine it predicted would survive are killed, each by a check the dispositions added or extended.

In the table, "killed" lists the coverage ids the mutant's run left unreached, then any group that raised and its
exception. A group that raises stops its later checks, so their ids appear unreached too.

| Mutant | From | Function | What breaks | Predicted (by its author) | Result: the coverage ids the run left unreached (the battery prints the first six, sorted), and any group exception |
|---|---|---|---|---|---|
| V01 | reviewer | `State.paused_on` | a literal state's pause stands on nothing | killed by N2-INDET-pause:N2-E, N2-INDET-pause:N1-V, N2-INDET-pause:N1-R, N2-INDET-pause:N1-P, RD-PAUSE | killed: N2-INDET-pause:N1-P, N2-INDET-pause:N1-R, N2-INDET-pause:N1-V, N2-INDET-pause:N2-E, N2-POINT-CAUSES, RD-PAUSE |
| V02 | reviewer | `State.paused_on` | a point lookup widened to any point of the arm (per arm again) | killed by N2-PAUSE-POINTWISE, VD-PAUSE-POINTS | killed: N2-PAUSE-POINTWISE, VD-PAUSE-POINTS, VD-PAUSE-RENDERING |
| V03 | reviewer | `State.paused_on` | an empty point map read as a literal state (per arm) | survives (equivalent on reports the runner writes: every steered arm in a standing pause's scope gets a point, so an empty map means no steered arm is paused) | survived |
| V04 | reviewer | `n2_outcome` | N2's pause causes read per arm | killed by N2-PAUSE-POINTWISE, VD-PAUSE-POINTS | killed: N2-PAUSE-POINTWISE, VD-PAUSE-POINTS, VD-PAUSE-RENDERING |
| V05 | reviewer | `n2_outcome` | the beside's paused list taken at the decision f's reads (always empty on a decided N2) | killed by N2-PAUSE-POINTWISE | killed: N2-PAUSE-POINTWISE |
| V06 | reviewer | `n2_outcome` | the beside's paused list per arm | killed by N2-PAUSE-POINTWISE | killed: N2-PAUSE-POINTWISE |
| V07 | reviewer | `n2_outcome` | a guard's flag read at N2's decision f only (a guard paused at the other f shows unpaused) | survives | killed: N2-PAUSE-POINTWISE |
| V08 | reviewer | `n2_outcome` | a pause at the beside's reads turns its figures 'not computed' | survives | killed: N2-PAUSE-POINTWISE |
| V09 | reviewer | `build_state` | the reader's points dropped (every pause read per arm) | killed by VD-PAUSE-POINTS | killed: VD-PAUSE-POINTS, VD-PAUSE-RENDERING |
| V10 | reviewer | `run_verdicts` | the primary row built without the points | killed by VD-PAUSE-POINTS | killed: VD-PAUSE-POINTS, VD-PAUSE-RENDERING |
| V11 | reviewer | `run_verdicts` | the TAU/4 row built without the points | killed by VD-PAUSE-POINTS | killed: VD-PAUSE-POINTS |
| V12 | reviewer | `paused_points` | adjudicated pauses still stand | killed by RD-PAUSE-POINTS | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V13 | reviewer | `paused_points` | N4's arms kept in the scope (N4 marked at d = 0) | killed by RD-PAUSE-POINTS | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V14 | reviewer | `paused_points` | N2's f labels swapped | killed by RD-PAUSE-POINTS | killed: RD-PAUSE-POINTS |
| V15 | reviewer | `paused_points` | a pause's read marked only when its record is on disk (a standing rendering pause stands on nothing) | survives | killed: VD-PAUSE-RENDERING |
| V16 | reviewer | `paused_points` | a batch stands on every read launched in its range (PIN-n-37's first alternative) | survives | killed: RD-PAUSE-POINTS |
| V17 | reviewer | `paused_points` | a batch's last read excluded | killed by RD-PAUSE-POINTS ("a binomial batch of one shadow") | killed: RD-PAUSE-POINTS |
| V18 | reviewer | `paused_points` | any d = 0 read taken for a shadow (N4's reads pair with every session's reads) | survives | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V19 | reviewer | `paused_points` | a batch's shadows not carried to their sessions (only the pause's own read) | killed by RD-PAUSE-POINTS ("a binomial batch of one shadow") | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V20 | reviewer | `paused_points` | a shadow's pairing leaves the pause's scope (every steered arm) | killed by RD-PAUSE-POINTS ("the same shadow, its scope N1-V alone") | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V21 | reviewer | `paused_points` | the shadow's own point (N1-V at 0) marked | killed by RD-PAUSE-POINTS (the shadow cases) | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V22 | reviewer | `paused_points` | a read outside the pause's scope marked | killed by RD-PAUSE-POINTS ("the same batch outside its scope", "N4's pause") | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| V23 | reviewer | `report_problems` | a rendering pause's read outside the plan accepted | killed by VD-REFUSE ("pause-not-planned") | killed: VD-REFUSE |
| V24 | reviewer | `report_problems` | the plan replaced by the reads on disk (refuses a standing rendering pause, whose read is not launched) | survives | killed: VD-PAUSE-RENDERING |
| V25 | reviewer, re-expressed | `report_problems` | a standing batch's k not compared | killed by VD-REFUSE ("batch-exceedances") | killed: VD-REFUSE |
| V26 | reviewer, re-expressed | `report_problems` | a standing batch's first end not compared | survives | killed: VD-REFUSE |
| V27 | reviewer, re-expressed | `report_problems` | over-refusal: every read in the range must carry a re-computation (refuses the runner's batches) | survives | killed: VD-PAUSE-POINTS |
| V28 | reviewer | `report_problems` | only read-less standing batches bound | survives | killed: VD-REFUSE |
| V29 | reviewer, re-expressed | `sentence_dose` | the fourth form's fill is the bare §0.6 label (no "(N4 [n4])") | killed by TUP-T2, SENT-FOURTH-FILLS, SENT-FILLED-DOSE-FOURTH | killed: SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, TUP-T2 |
| V30 | reviewer, re-expressed | `sentence_dose` | the parenthetical gated on N4 not PASS instead of G-READ-n PASS | killed by TUP-T2, SENT-FOURTH-FILLS, SENT-FILLED-DOSE-FOURTH | killed: SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, TUP-T2 |
| V31 | reviewer | `LABEL_TAIL` | an en dash for the em dash | killed by SENT-RULING, TUP-T2, SENT-FOURTH-FILLS | killed: SENT-CODE-FORMS, SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, SENT-RULING, TUP-T2 |
| V32 | reviewer | `F4` | the not-readable branch loses its tail | killed by SENT-RULING, TUP-T2 | killed: SENT-CODE-FORMS, SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, SENT-RULING, TUP-T2 |
| V33 | reviewer | `CNA_N4` | the fill's parenthetical changed to "(N4: [n4])" | killed by SENT-RULING, TUP-T2, SENT-CODE-FORMS | killed: SENT-CODE-FORMS, SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, SENT-RULING, TUP-T2 |
| V34 | reviewer | `FORM_FOURTH` | the first sitting's form string restored | killed by TUP-T2, TUP-T10 | killed: TUP-T10, TUP-T2 |
| C01 | Code | `State.paused_on` | the points ignored: the arm decides on the reader path too | killed by VD-PAUSE-POINTS, VD-PAUSE-RENDERING | killed: N2-PAUSE-POINTWISE, VD-PAUSE-POINTS, VD-PAUSE-RENDERING |
| C06 | Code | `paused_points` | a shadow read as a plain read | killed by RD-PAUSE-POINTS | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| C11 | Code | `paused_points` | a binomial pause's batch ignored | killed by RD-PAUSE-POINTS, VD-PAUSE-POINTS | killed: RD-PAUSE-POINTS, VD-PAUSE-POINTS |
| C14 | Code | `report_problems` | a standing batch's count not bound (re-expressed on the fixed draft) | killed by VD-REFUSE (batch-count, batch-read-count) | killed: VD-REFUSE |
| C15 | Code | `report_problems` | a batch's exceedances counted at TAU/4 (re-expressed on the fixed draft) | killed by VD-PAUSE-POINTS (B: 80 reads above TAU/4, none above TAU) | killed: VD-PAUSE-POINTS |
| C16 | Code | `report_problems` | a pause's read not held to the plan | killed by VD-REFUSE (pause-not-planned) | killed: VD-REFUSE |
| C17 | Code | `report_problems` | no standing batch bound | killed by VD-REFUSE (the batch cases) | killed: VD-REFUSE |
| C19 | Code | `sentence_dose` | the N4 fill where the state is not readable too | killed by SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, TUP-T2 | killed: SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, TUP-T2 |
| C20 | Code | `sentence_dose` | the label slot left in the fourth form | killed by SENT-FILLED-DOSE-FOURTH, RD-FILLED, TUP-T2 | killed: SENT-FILLED-DOSE-FOURTH, SENT-FILLED-DOSE-ND, SENT-FILLED-N1-AGAINST, SENT-FILLED-N2-CAP, SENT-FILLED-N2-ZONE, SENT-FOURTH-FILLS; AnlStop raised in the sentences group |
| C25 | Code | `state_figures` | the pause points not listed | killed by VD-PAUSE-POINTS, VD-PAUSE-RENDERING | killed: VD-PAUSE-POINTS, VD-PAUSE-RENDERING |
| C27 | Code | `State.paused_on` | a point looked up by its arm | killed by N2-PAUSE-POINTWISE | killed: N2-PAUSE-POINTWISE, VD-PAUSE-POINTS |
| C29 | Code | `report_problems` | a standing batch's start taken from the report | killed by VD-REFUSE (batch-start) | killed: VD-REFUSE |
| C30 | Code | `report_problems` | a run's-end batch's end taken from the report | killed by VD-REFUSE (batch-end) | killed: VD-REFUSE |
| C31 | Code | `report_problems` | a standing batch's scope not bound | killed by VD-REFUSE (batch-scope) | killed: VD-REFUSE |
| C32 | Code | `report_problems` | the clear point taken from any adjudicated pause, a batch or none | killed by VD-PAUSE-POINTS (B: the adjudicated non-finite pause carries no batch) | killed: VD-PAUSE-POINTS |
| C33 | Code | `report_problems` | no batch cleared: every standing batch from the stage's first trial | killed by VD-PAUSE-POINTS (A, C) | killed: VD-PAUSE-POINTS |

**The survivor, V03, equivalent on reports the runner writes**, as the reviewer predicted.
- V03 reads an empty point map as a literal state, and so falls back to the per-arm pauses.
- Under the runner's SCOPE, every steered arm in a standing pause's scope gets at least one point: its read's, a
  trial's, or a shadow's pairing. So the map is empty only when no steered arm is paused.
- The fallback then marks none of N2's reads, so the outcome is the same. No battery input that reaches
  `State.paused_on` holds a scope arm with no point, since the runner writes none. RD-PAUSE-POINTS's direct cases do
  hold one, but they test `paused_points` alone.

**The run with a group exception.** C20 left the fourth form's label slot unfilled. The sentences group raised
`fill()`'s AnlStop: "STOP: a sentence keeps slots ['[label]'] after filling (dose, NOT-DETECTABLE)". The group's later
checks did not run, so their ids appear unreached.

**The reviewer's predicted survivors, killed.** Nine of the ten are killed, each by a check the dispositions added or
extended:
- V07 (a guard's flag read at N2's decision f only) and V08 (a pause at the beside's reads blanking its figures): by
  N2-PAUSE-POINTWISE's new cases, a guard paused at the other f and the beside's figures against the unpaused state's
  (B5);
- V15 (a pause's read marked only when on disk) and V24 (the plan replaced by the reads on disk): by
  VD-PAUSE-RENDERING, whose rendering pause stands on a read of the plan that is not on disk (B4);
- V16 (a batch standing on every read in its range): by RD-PAUSE-POINTS's range over N1-P's +d_20 to −1 cells and its
  keyed-sample campaign (B1);
- V18 (any d = 0 read taken for a shadow): by RD-PAUSE-POINTS's N4 trial under a steered scope (B2), and by
  VD-PAUSE-POINTS;
- V26 (the batch's first end unbound) and V28 (only read-less batches bound): by VD-REFUSE's batch-start and
  batch-read-count (B3);
- V27 (every read in the range required to be a trial): by VD-PAUSE-POINTS, whose scenario A accepts a batch whose
  range holds N2's reads, none of them re-computed (B3).

**The refusals that caught the binding mutants** (VD-REFUSE's failed cases, as its failing line prints them):
- C14: batch-count and batch-read-count;
- C16 and V23: pause-not-planned;
- C29 and V26: batch-start;
- C30: batch-end;
- C31: batch-scope;
- V25: batch-exceedances;
- V28: batch-read-count.

The refusals share one output folder, written once. Where a case ran to an output instead of refusing, each later case
that also did not refuse met that output, and failed on its write-once message rather than its own.
- C14's batch-read-count failed this way, after its batch-count.
- C17 binds no standing batch. Its first batch case, batch-count, ran to an output, and the batch cases after it
  failed on that message. The printed list is cut short.

**The reviewer's five mutants re-expressed on the fixed draft** (V25, V26, V27, V29 and V30, as run). Their intent is
the report's, their old text the fixed draft's, and their predictions Code's:

```
@@ V25 | report_problems | a standing batch's k not compared (re-expressed on the fixed draft) | predicted: killed by VD-REFUSE ("batch-exceedances")
                    or (len(ins), sum(r["fidelity"]["exceeds_tau"] is True for r in ins)) != (b["n"], b["k"]):
~~
                    or len(ins) != b["n"]:
```
```
@@ V26 | report_problems | a standing batch's first end not compared (re-expressed on the fixed draft) | predicted: killed by VD-REFUSE ("batch-start")
            if (b["first_launch_index"], b["last_launch_index"]) != (first_w, last_w) \
~~
            if b["last_launch_index"] != last_w \
```
```
@@ V27 | report_problems | over-refusal: every read in the range must carry a re-computation (re-expressed on the fixed draft) | predicted: killed by VD-PAUSE-POINTS (A's batch holds N2's reads, none re-computed)
                    or (len(ins), sum(r["fidelity"]["exceeds_tau"] is True for r in ins)) != (b["n"], b["k"]):
~~
                    or (len(ins), sum(r["fidelity"]["exceeds_tau"] is True for r in ins)) != (b["n"], b["k"]) \
                    or len(ins) != b["last_launch_index"] - b["first_launch_index"] + 1:
```
```
@@ V29 | sentence_dose | the fourth form's fill is the bare §0.6 label (re-expressed on the parenthesized line) | predicted: killed by TUP-T2, SENT-FOURTH-FILLS, SENT-FILLED-DOSE-FOURTH
            fill = lab if lab == ANSWERED else (CNA_N4.replace("[n4]", n4) if gr == "PASS" else CNA)
~~
            fill = lab
```
```
@@ V30 | sentence_dose | the parenthetical gated on N4 not PASS instead of G-READ-n PASS (re-expressed on the parenthesized line) | predicted: killed by TUP-T2, SENT-FOURTH-FILLS, SENT-FILLED-DOSE-FOURTH
            fill = lab if lab == ANSWERED else (CNA_N4.replace("[n4]", n4) if gr == "PASS" else CNA)
~~
            fill = lab if lab == ANSWERED else (CNA_N4.replace("[n4]", n4) if n4 != "PASS" else CNA)
```

**Code's mutants, whole** (sixteen, from C01 to C33, as run; the old text, then the new, each applied to the base
exactly once):

```
@@ C01 | State.paused_on | the points ignored: the arm decides on the reader path too | predicted: killed by VD-PAUSE-POINTS, VD-PAUSE-RENDERING
        if self.paused_at is None:
            return bool(self.paused.get(arm))
~~
        if True:
            return bool(self.paused.get(arm))
```
```
@@ C06 | paused_points | a shadow read as a plain read | predicted: killed by RD-PAUSE-POINTS
            if (arm, lab) == ("N1-V", "0"):                # a shadow (N1-V|none|0): its session's reads pair with it
~~
            if False:
```
```
@@ C11 | paused_points | a binomial pause's batch ignored | predicted: killed by RD-PAUSE-POINTS, VD-PAUSE-POINTS
        if b is not None:
            rids += sorted(rid for rid, r in camp.records.items() if r["fidelity"] is not None
~~
        if False:
            rids += sorted(rid for rid, r in camp.records.items() if r["fidelity"] is not None
```
```
@@ C14 | report_problems | a standing batch's count not bound (re-expressed on the fixed draft) | predicted: killed by VD-REFUSE (batch-count, batch-read-count)
                    or (len(ins), sum(r["fidelity"]["exceeds_tau"] is True for r in ins)) != (b["n"], b["k"]):
~~
                    or sum(r["fidelity"]["exceeds_tau"] is True for r in ins) != b["k"]:
```
```
@@ C15 | report_problems | a batch's exceedances counted at TAU/4 (re-expressed on the fixed draft) | predicted: killed by VD-PAUSE-POINTS (B: 80 reads above TAU/4, none above TAU)
                    or (len(ins), sum(r["fidelity"]["exceeds_tau"] is True for r in ins)) != (b["n"], b["k"]):
~~
                    or (len(ins), sum(r["fidelity"]["exceeds_tau4"] is True for r in ins)) != (b["n"], b["k"]):
```
```
@@ C16 | report_problems | a pause's read not held to the plan | predicted: killed by VD-REFUSE (pause-not-planned)
        if rid not in planned:
            p.append(f"{q['pause_id']}: its read {rid} is not a read of the plan")
~~
```
```
@@ C17 | report_problems | no standing batch bound | predicted: killed by VD-REFUSE (the batch cases)
        if b is not None and not q["adjudicated"]:
~~
        if False:
```
```
@@ C19 | sentence_dose | the N4 fill where the state is not readable too | predicted: killed by SENT-FILLED-DOSE-FOURTH, SENT-FOURTH-FILLS, TUP-T2
            fill = lab if lab == ANSWERED else (CNA_N4.replace("[n4]", n4) if gr == "PASS" else CNA)
~~
            fill = lab if lab == ANSWERED else CNA_N4.replace("[n4]", n4)
```
```
@@ C20 | sentence_dose | the label slot left in the fourth form | predicted: killed by SENT-FILLED-DOSE-FOURTH, RD-FILLED, TUP-T2
            t, form = D_FOURTH["readable" if gr == "PASS" else "not readable"].replace("[label]", fill), FORM_FOURTH
~~
            t, form = D_FOURTH["readable" if gr == "PASS" else "not readable"], FORM_FOURTH
```
```
@@ C25 | state_figures | the pause points not listed | predicted: killed by VD-PAUSE-POINTS, VD-PAUSE-RENDERING
    pp = None if st.paused_at is None else sorted(name(a, k) for (a, k), v in st.paused_at.items() if v)
~~
    pp = None if st.paused_at is None else []
```
```
@@ C27 | State.paused_on | a point looked up by its arm | predicted: killed by N2-PAUSE-POINTWISE
        return bool(self.paused_at.get((arm, key)))
~~
        return bool(self.paused_at.get(arm))
```
```
@@ C29 | report_problems | a standing batch's start taken from the report | predicted: killed by VD-REFUSE (batch-start)
            first_w = next((i for i in trial_li if i > cleared), None)
~~
            first_w = b["first_launch_index"]
```
```
@@ C30 | report_problems | a run's-end batch's end taken from the report | predicted: killed by VD-REFUSE (batch-end)
            last_w = (trial_li[-1] if trial_li else None) if q["read_id"] is None else q["launch_index"]
~~
            last_w = b["last_launch_index"] if q["read_id"] is None else q["launch_index"]
```
```
@@ C31 | report_problems | a standing batch's scope not bound | predicted: killed by VD-REFUSE (batch-scope)
            if not {r["arm"] for r in ins} <= set(q["arms_in_scope"]):
~~
            if False:
```
```
@@ C32 | report_problems | the clear point taken from any adjudicated pause, a batch or none | predicted: killed by VD-PAUSE-POINTS (B: the adjudicated non-finite pause carries no batch)
    cleared = max((q["binomial"]["last_launch_index"] for q in rep["pauses"]           # an adjudicated batch's ruling
                   if q["adjudicated"] and q["binomial"] is not None and q["read_id"] is not None), default=-1)
~~
    cleared = max((q["launch_index"] for q in rep["pauses"]
                   if q["adjudicated"] and q["read_id"] is not None), default=-1)
```
```
@@ C33 | report_problems | no batch cleared: every standing batch from the stage's first trial | predicted: killed by VD-PAUSE-POINTS (A, C)
    cleared = max((q["binomial"]["last_launch_index"] for q in rep["pauses"]           # an adjudicated batch's ruling
                   if q["adjudicated"] and q["binomial"] is not None and q["read_id"] is not None), default=-1)
~~
    cleared = -1
```

## 4. The battery runs

All ran in battery windows the coordinating session granted, each on bytes named to it first by sha256. Each ran as one
process at a time, at `nice -n 19` with `-I`, with temp folders outside the repository, in the foreground. The
interpreter was reached by `cd` into the venv's bin by glob, so no argv named its path. Nothing ran on a model or on
the box.

The runs named here ran on copies of the draft (`runs/d1.py`, `d2.py` and `d3.py` in Code's scratch). Each was made
before its run and is unchanged since: its sha256 is the one named to the coordinating session, and the copies are now
read-only. Each ran through `run_battery2.sh`, the cd-glob form. v5's `run_battery.sh`, v4's form copied at the
cycle's start, was read and never run. That is from Code's transcript, as the values-check's O1 asked.

- **The draft's window: two runs.**
  - d1 (`cca2acb4…9057`): 219/221. Two checks failed: the forms' digest, which moved with §3.2 as the seat said, and the
    coverage check, which depends on it.
  - The digest pin was then set by tool from that run's printed value. That was d2's one change, named to the
    coordinating session before it ran.
  - d2 (`6f2dd349…301e`): 221/221. Those bytes were frozen for the review.
- **The mutant window.**
  - d3, the fixed draft (`83f54ec6…d04c`): 222/222, every one of its 225 coverage ids reached. Those bytes were frozen
    as the mutant base.
  - Then the 50 mutants, in four batches (12, 12, 12 and 14). Each batch ran its mutants one after another. Each
    mutated file was checked against the manifest (`e2cf9684…d6d0`, 50 files) before it ran.
  - The manifest first named to the coordinating session held 48 files. It was replaced by a line to that session
    before any run, adding C14 and C15, and the session confirmed the 50.
- **The run of record** is the entry's, from `scripts/n_analyze.py` on the committed bytes.

Q-F3's campaign ran on the laptop beside these windows, as the coordinating session's windows allow. By its grants, no
other battery window was open during any of these runs.

## 5. The committed bytes against the mutation-tested base

The committed `scripts/n_analyze.py` differs from the mutant base (`83f54ec6…d04c`) in twelve change regions, as `diff`
counts them: the repository line, and ten texts from the values-check.

- **The repository line.** The base, a scratch file, read the repository at its absolute path. The committed file
  reads it from its own location, as the committed analyzer always has:

  ```
  REPO = Path(__file__).resolve().parents[1]                     # scripts/n_analyze.py -> the repository
  ```
- **Six texts, from the values-check's first pass** (seven change regions; the values-check raw, pass 1):
  - the module docstring, whose OPEN clause now names the second sitting's §3 beside the first sitting's §5 (A1);
  - the comment above the oracle's copies, which now names the label's copies among what SENT-RULING compares (A13);
  - PIN-n-37, where "(flagged to n-build)" is now "(relayed to n-build)", the route the point took (O4);
  - the comment above VD-PAUSE-POINTS and its description (the description in two change regions), which now say each
    standing batch is bound as the runner counts a batch, not that each is the runner's, and that C repeats A's
    outcomes for N1 and N2 and its point, not all of A (R33, A28);
  - `paused_points`' docstring, which now calls the shadow extension through a batch Code's, capped by the scope, as
    PIN-n-37 does, where it credited the runner's SCOPE (A19).
- **Four texts, from the second pass** (four change regions; the values-check raw, pass 2):
  - the comment on `State.paused_at` and `state_figures`' docstring, which now say "no point map" where they said
    "the battery's literal states", since a literal state can carry one (O5);
  - `code_forms`' docstring, which now names the second sitting's §3.2 and the label's fill for N4 among the forms it
    pins (O6);
  - the G-ANL-n artifact's "spec" string, which now names the second sitting's §3 beside the first sitting's §5. No
    check reads it, and G-ANL-n's canonical run is still to come (O6).

No outcome, sentence or form changes. The forms' digest is the same, since none of the ten texts is a form. The run of
record covers the committed bytes.

## 6. The tallies

The tuple pass's 2,561 evaluations and their tallies by state, form and label are `a84833e`'s, derived in that
commit's review raw (`results/raw/2026-11-18_n-analyze_v4_review.md` §6). The one change is the fourth form's form
string, which now names the second sitting's §3.2 label. The fourth form's fill is in its text, not in the tally's key,
which carries the record's label, so the tally still counts its 640 evaluations as 64 answered and 576 concluded, not
answered.

SENT-FOURTH-FILLS splits the 640 by the fill in the sentence. A tuple with dose NOT-DETECTABLE takes N1's four states,
N2's four and N4's four (64 tuples) under each of G-READ-n's two states at d_eq. Each tuple runs under the four
G-READ-n inputs, doubled where N4 is INDETERMINATE (no read obtained, or terminal):

| The fill | Its cell | Tuples | Evaluations |
|---|---|---|---|
| answered | G-READ-n PASS at d_eq, N4 PASS | 16 | 16 × 4 = 64 |
| concluded, not answered (N4 [n4]) | G-READ-n PASS, N4 REVERSE, DEAD or INDETERMINATE | 48 | 48 × 4 + 16 × 4 = 256 |
| concluded, not answered | G-READ-n FAIL, N4 any | 64 | 64 × 4 + 16 × 4 = 320 |

That is 640 in all, the fourth form's share of the 2,561.
