# n — G-CAL-n's delta (second sitting): the blind review of draft 1, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over draft 1, the delta from HEAD `616e940`'s bytes to the seat's
three changes (the answers of 2026-11-19, second sitting: §1.4 (i), §2.5, §3):
- `valence_core/n/gcal.py`, from `61bcafc9…14fc` to `17defa3f…21db` (1091 lines), read in full;
- `scripts/n_sessions.py`, from `2728146e…570c` to `47b12b3e…737b` (3737 lines): G-CAL-n's section and its self-test
  read in full.
Draft 1's driver changes were built on G-VEC's draft 1 and rebased onto `616e940`'s driver (+129 −54 there, by
numstat). Draft 1's self-test did not run; draft 2 is the delta's first run.

**The reviewer's brief** (`bc23af8e…eacc`, 91 lines):
- gave the two deltas' FROM and TO files, by sha256, and the `git diff --no-index -U3` form; the seat's answers of
  the second sitting (§1.4 (i), §2.5, §3, §5), with the PI's routing slot for the gate's batch ("Go"), and of the
  first (§1.9, §1.11, §1.12, §5), for what the delta must do; and the code it must match (`schema.py`'s `DOSES` and
  `expected_alpha`, `runner.py`'s `_injection`, `gvec.py`, `adapters/base.py`, `testing.py`), read only;
- asked whether each of Code's declared readings is sound; whether the self-tests' suffix decoders hide a defect,
  and whether every flow that depends on the baseline's coherent count is determined by construction; whether the
  gate's injection is the campaign's N2-E injection at f0.20 and its row checked before the load; whether a smoke can
  generate a gate turn, or a run with −ρ run without one; whether the early PAUSE follows +ρ's evaluation, a STOP
  there taking precedence, with no later forward; and whether the self-test count of 569 holds;
- asked for findings, surviving mutants, box risks and observations, and for any command a rule bars;
- quoted the list of record v2's items 1–5, verbatim, and barred any interpreter but shasum, any write, any network,
  any model or adapter code run, any guard marker in an argv, anything under `data/mf3`, any whole-tree git status,
  any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the files it named.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (190 lines, sha256
`44dbda82…3c30`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 0 BUG; 10 findings (5 RISK, 5 NIT); 4 surviving mutants; 4 box risks; 8 observations.

## 1. Dispositions, applied in draft 2

Draft 2: `valence_core/n/gcal.py` `4bd8f8bf…c376` (1117 lines, +63 −37 on draft 1) and `scripts/n_sessions.py`
`313aa240…8e96` (3772 lines, +64 −29 on draft 1). Draft 3, the bytes committed, follows on the values-check (the
delta's entry): `gcal.py` `2b99902b…a430` (1117 lines, +8 −8 on draft 2) and `scripts/n_sessions.py` `593a140d…a549`
(3777 lines, +22 −17 on draft 2); every disposition below holds in it.

- **F1** (RISK), applied: the main flows' step never draws the end of turn at an unsteered turn's first step
  (`base_logits` in gcal.py's self-test, `base_step` in the driver's), so every baseline turn has an id and, under
  the suffix decoder, is coherent: the flows reach every batch by construction, not by the double's seed. The
  driver's mid-run failure and early-STOP steps use the same step, so their turns stay the run of record's.
- **F2** (RISK), applied: three flows now run on the plain decode with non-empty incoherent turns, so "coherent" and
  "has an id" are told apart:
  - the O7-at-the-bar flow: a baseline turn at i ≥ k is one id then the end of turn; b35 is 48 non-empty turns, 35
    coherent, the early PAUSE;
  - the gate's fail flow: every gate turn one id then the end of turn, 0 of 48 coherent and 48 one-id stops, the
    baseline six distinct words in every turn (48 coherent), the status PASS;
  - the driver's early-PAUSE flow: every baseline turn one id, none coherent, the early PAUSE (exit 3).
- **F3** (RISK), applied: the driver's fake G-VEC record has R 3.0 and R_ell 4.0, so no check takes one for the other.
- **F4** (RISK), applied: the gate's injection is checked at the site's layer, and every steered step's layer is the
  site in the main flow (M3); a new driver check regenerates +ρ's turn 0 from G-VEC's valence row and its injection at
  R, and recomputes a scored +ρ turn's arrival on that row over positions 1..n (M4).
- **F5** (RISK), applied: `ARRIVAL_FROM = directions.CAPTURE_FROM`, one constant for both ("built alike"), with a
  self-test equality.
- **F6** (NIT), applied: "the same prompt and seed in every batch, the gate's among them"; the raise's batches include
  the gate's.
- **F7** (NIT), applied: the non-early PAUSE line reads "a hurdle failed at +rho/2 alone (GC14; an incoherent baseline
  ends the run at the early read)"; `stage_status` is unchanged, as the seat ruled.
- **F8** (NIT), applied: the gate's batch line prints its one-id stops; after the exposure line the stage prints the
  gate's result in the lock's form, "reward axis 5(d) gate, coherence: k of 48, PASS" (or FAIL), whose line
  n-analyzer's delta after G-CAL-n's run reads from the lock (§2.5), pinned by the driver's check (its place after
  the exposure line by draft 3's print-order check).
- **F9** (NIT), applied: `RECORD_SCHEMA` is `n-gcal-v2`, declared; no `n-gcal-v1` record exists.
- **F10** (NIT), applied: `_gcal_selftest`'s docstring names the early PAUSE, the gate's flows and the tie to G-VEC's
  rows; the command's docstring reflowed.
- **M1–M4**, each killed: M1 by F3; M2 by F2's flows; M3 by the layer checks; M4 by the new driver check.
- **B1** and **B4** ask for nothing. **B2**, its cheap cover applied: the box's HF check runs the gate's steering
  check on the tiny model, so the gate's injection meets an HF forward before the run of record; its second clause
  (the smoke could run the gate's two-forward check with no turn) goes to the seat in the delta's entry. **B3** goes
  to G-CAL-n's launch files: 240 turns instead of 192, up to 3,840 more uncached forwards plus 2.
- **O1–O4** and **O7** ask for nothing in the code. **O5** (a baseline with fewer than two scored turns leaves Welch's t
  undefined, a +ρ fail, so the early STOP precedes the early PAUSE even for an incoherent baseline) and **O6** (a
  one-id turn's `arrival_all` is the position-0 projection alone) go to the seat in the delta's entry, for
  ADDENDUM-n3 and the read. **O8** stands: the addendum's commit binds through G-CAL-n's launch files.
- **The reviewer's departures,** as its report states them, are in the delta's entry, for the seat to class.

## 2. The report as returned

BLIND REVIEW: G-CAL-n's second-sitting delta (gcal and the driver)

I found no BUG. Three self-test gaps let one-line wrong edits survive (M1–M4), and the main flows rest on an unshown property of the test double (F1). Count agreed at 569.

Inputs, verified first
- Brief sha256 bc23af8e4356784cf0e0be832c463a16adb55f0a0f4df185720bb2af3bebeacc.
- HEAD is 616e9407c724f47b47fd018e5ddc8c9f2ad89103 (616e940).
- Both FROM files are clean at HEAD: rev-parse HEAD:<path> = 616e940:<path> = hash-object <path> (gcal.py 011901ffd37f07dc4db7c58efb056f4b2ead050f, n_sessions.py a9baaf7ec2c4d988f74bb8992f59a2c8b38b845b).
- Every sha256 equals the brief's:
  - FROM gcal 61bcafc923ab97a762a332858cdd00208fc20b60cc3d4c5e65068dca152d14fc
  - FROM driver 2728146e85a726850bbb0a3c4cca1ea650c9dd6a131a687960532e3d6c6f570c
  - TO gcal 17defa3f90ca73ca367c2cd60605b1da066b7d57260bce644677a7f624a321db
  - TO driver 47b12b3ea0f9d05c13ecc6f2d6fa342b5c4aab5fb9f328bfbeab8a666d9b737b
  - second sitting 887b764696c71f34784157d20f49fec5bc43ac135b349ea488ae00d3a312dc87 and first sitting e6ff066d6b1a857e32555ec431066d7c18d9e71b6a6185de3b4f5c79da636d5a (both clean at HEAD).
- Deltas: `git diff --no-index -U3 <from> <to>` from the root.
- Notation:
  - G = S/step4b/gcal2/d1/gcal.py, read in full, 1091 lines.
  - D = S/step4b/gcal2/d1/n_sessions.py: the G-CAL-n section D:2608-3637 in full, plus D:1-370.

FINDINGS

F1 RISK — the main flows depend on a property of the double that the code does not show.
- With the suffix decoders (G:681-683, D:3104-3105), a turn is coherent iff it has an id. So these flows reach every batch only if, of the 48 unsteered baseline prompts, at most 12 draw the end of turn first:
  - res, again, the gate's steering-check flow, res_o and gm (G:739, 756, 839, 844, 917);
  - the driver's run of record env1 (D:3144), and everything read from it: D:3151-3194 and the decode comparison D:3489-3509.
- Only the first draw matters: at cap 6 a later end of turn leaves a non-empty, coherent turn. Both self-tests share this one fact (same double, prompt ids, seeds, eos and cap; the baseline is unsteered).
- The outcome is seeded (seed 20261119, keys.gcal_seed) but not constructed.
- If it fails:
  - G:742 and G:750 fail, then G:778-779 raises KeyError 'reward_f020';
  - D:3151 fails, then D:3159 raises KeyError;
  - each self-test is then counted once as "ran to its end" (D:259-262, D:350-353), and the total falls short of 569.
- Fix, either one:
  - build it in: e.g. in those flows' step, put the eos logit at −50 on an unsteered turn's first step (both sides of every comparison use the same step);
  - or assert it in a named check before the flows, and index the gate's batch so that a miss is a counted failure, not a crash.

F2 RISK — G:491 (and G:504, G:522): the decoder change makes "coherent" and "non-empty" one predicate in every flow (M2).
- Fix: one flow with non-empty incoherent turns.
- In the O7-at-the-bar flow (G:937-958), give the flow its own suffix-free decoder and make step_k's i ≥ k baseline turns emit one id then the end of turn. b35 is then 48 non-empty turns with 35 coherent.
- Do the same in gm (G:911-924) for the gate's count: gate turns of one id, then eos.
- env8 (D:3336-3363) can mirror it.

F3 RISK — D:3054 `R_t, Rl_t = 3.0, 3.0`: the driver's fake G-VEC record has R = R_ell, so no driver check can tell the two apart (M1).
- Fix: Rl_t = 4.0. The dose map stays unfolded: d_eq ≈ 0.444, d_20 ≈ 0.889.

F4 RISK — two things go unchecked:
- the gate injection's layer (G:425; M3);
- the driver's compute arguments, which are never tied to G-VEC's rows (D:2862; M4).

F5 RISK — G:179 `ARRIVAL_FROM = 1` is a second literal of directions.CAPTURE_FROM (valence_core/n/directions.py:50). The seat's reason for the change is "built alike".
- Fix: take it from directions, or add a self-test equality between the two.

F6 NIT — two stale docstring lines:
- G:29-30 "the same prompt and seed in all four batches": the gate makes five;
- G:97 "before +ρ/2 and −ρ are generated": add the gate's batch.

F7 NIT — D:2895-2896, the non-early PAUSE line's "or the baseline is incoherent (O7)", is unreachable after O2. The early read always runs before stage_status and catches an incoherent baseline. G:392's baseline clause is likewise unreachable from compute; that is fine, since the seat ruled stage_status unchanged.

F8 NIT — two places where a reader can miss the gate's figures:
- G:527-529: the gate's batch line omits one_id, which the steered lines print (G:520);
- D:2898: the final PASS line is silent on the gate's k of 48 and PASS/FAIL, which the lock pins (§2.5).

F9 NIT — G:139 RECORD_SCHEMA stays "n-gcal-v1" though the arrival's quantity changed. G-VEC bumped to v2 for the same convention change. `constants.arrival_from` (G:578) disambiguates, and no G-CAL-n record exists yet. Bump, or say why not.

F10 NIT — two docstrings need touching:
- D:3020-3024, the `_gcal_selftest` docstring, lists the early STOP but not the early PAUSE or the gate's flows;
- D:163-170 needs a reflow ("the\n ids of record", "the dose map (a fold\n into 0").

SURVIVING MUTANTS

M1 D:2861 `"R_ell": gv["R_ell"]` → `"R_ell": gv["R"]`.
- Same blind spot: D:2863 `R=gv["R"]` → `R=gv["R_ell"]`; D:2686 `float(ofr["R_ell"])` → `float(ofr["R"])`; D:2816 dose_map's two arguments swapped.
- Why it survives: with R_t = Rl_t (D:3054), these checks compare equal numbers: D:3157, D:3164, D:3228, and the alpha sets D:3333 and D:3361. gcal's own self-test passes R_ell itself.
- Wrong behaviour: the gate is dosed at 0.20·R instead of 0.20·R_ℓ.
- Killed by: F3's Rl_t = 4.0, which makes D:3164 and D:3228 fail (and D:3157 / D:3361 for the variants).

M2 G:491 `if r["coherence"]["coherent"]` → `if r["n_tok"]` (or `if not r["coherence"]["length_collapse"]`).
- The same edit at G:504 and G:522 also survives.
- Why it survives: every flow has coherent ⟺ non-empty, so b35, mute, env8 and the main flows count identically.
- Wrong behaviour: a non-empty incoherent baseline (loops, collapse) passes the early read. +ρ/2, the gate and −ρ are then generated (the exposure O2 exists to avoid), and the run ends a PAUSE through stage_status with early_pause false.
- Killed by: F2's flows.

M3 G:425 `int(site), float(f), {int(site): R_ell},` → `int(site) - 1, float(f), {int(site) - 1: R_ell},`.
- Why it survives:
  - the gate check's reference injection comes from the same function (G:800, G:806);
  - `seen` (G:675) records kind, start and alpha, not the layer;
  - site − 1 is a layer of the double in both self-tests (1 and 2), so every steering check passes.
- Wrong behaviour: the gate steers the layer below the campaign's.
- Killed by: adding `inj_g.layer == site` to G:802's check, or recording `i.layer` in `seen` and asserting every steered layer is the site. The driver can check a layer carried in the gate's figures.

M4 D:2862 `v_unit=gv["v_unit"], v_sha16=gv["v_sha16"]` → `v_unit=gv["g_unit"], v_sha16=gv["g_sha16"]`.
- With this edit the valence batches are steered and scored on span_reward. The delta's new g pair makes the swap a one-line edit.
- Variant: `site=gv["site"]` → `site=gv["site"] - 1`.
- Why it survives: the driver's checks read provenance built from gv (D:2838-2839), the gate's sha16 and alpha, counts, order and exits. They never read a turn or score recomputed from rows[0] at the record's site.
- Killed by: in the run-of-record checks,
  - regenerate one +ρ turn with gcal.generate on the double's step under gcal.injection_for(1.0, rows[0], site, R_t, v_sha), and compare its ids;
  - compare one scored turn's arrival with the mean of (forward_all(ids,(site,))[site] @ rows[0])[1:].

BOX RISKS

B1 — The self-test cannot load a model or write a canonical folder, even on the box with RUNPOD_POD_ID set and the weights present.
- Every run_gcal call goes through env_for (D:3107-3124): the stub adapter, a pod lambda, and an out folder asserted outside the repository.
- The in-repository smoke case is refused at D:2762, before guard.refuse_out or any mkdir.
- production_gcal_env() is only constructed (D:3125).
- main()'s gcal calls run with run_gcal swapped for a recorder (D:3558-3560). As a backstop, they run with no pod id and a refused cuBLAS setting (D:3555-3556), which D:2780-2786 refuses before any load or write; D:2769 only reads.
- committed_bytes only runs `git show`.
- The new flows (canned fourth D:3209; env8) use env_for.

B2 — The gate's injection first meets the HF forward at its steering check in the run of record, after 144 turns (Code's reading g).
- The smoke has no gate turn, and the box self-test's HF case (D:3610-3634) builds only the valence injection.
- Construction (sha16, R_ell, alpha) is checked before any forward (G:459). The forward path is the one +ρ's and +ρ/2's checks have just passed, so a refusal is unlikely.
- If it does come, D:2868-2875 keeps 144 turns in data/n/.gcal.failed, and a re-run waits for the seat.
- Cheap cover: in the hftiny case, add steering_check under gcal.gate_injection({"unit": v_t, "sha16": gvec.injection_sha16(v_t), "R_ell": 3.0}, 1).
- For the seat: the smoke could run the gate's two-forward check with no turn.

B3 — Time and memory.
- 240 turns instead of 192: up to 3,840 more uncached forwards plus 2, about +25% of the generation. The early STOP/PAUSE can save up to 144 turns.
- The launch files' time estimate should be redone for 240.
- No capture on gate turns (G:484), so memory is as before.

B4 — Non-finite values.
- The gate has no arrival figure, and its alpha is finite by G:423-428.
- A non-finite logits row raises in sample (G:235-236) and takes the failure path with the turns kept.
- allow_nan=False refuses NaN at append_turn and write.

OBSERVATIONS

O1 — The brief's "also check" items all hold.
- The gate is the campaign's N2-E injection at f0.20:
  - G:416-429 mirrors runner.py:278-300: at_frac on the row with expect_sha, frac = 0.20 on the program scale, table {layer: R_ell}, sign applied after, and |alpha| asserted equal to schema.expected_alpha.
  - Direction span_reward (schema.py:301); sign +1, value 0.20 (schema.py:290); alpha 0.20·R_ell (schema.py:541-550).
  - R_ell is G-VEC's of_record value (gvec.py:516-517), which is also the dose map's (G:397-405). The layer is the site.
  - Only the positions differ (whole turn from 0, as Q9 ruled).
- The row is read and checked before the load (D:2687, 2700-2708 at D:2814, versus make_adapter at D:2842), and at_frac re-checks it before any forward (G:425-426, G:459).
- No gate turn in a smoke: G:451-452, G:458-460, D:2861.
- −ρ needs the gate: G:453-455, before any injection or forward.
- The early ends:
  - The early read runs once, right after the baseline (G:488).
  - STOP (G:492) is tested before PAUSE (G:497), and status G:530 keeps that order.
  - Each early end breaks before the next iteration's steering check (G:465-466), so no +ρ/2, gate or −ρ forward follows.
  - The self-tests confirm it: G:878, G:898, D:3333, D:3361.

O2 — Code's readings (G:115-120):
- (a) arrival_all for a one-id turn: sound. §1.4 (i) requires the None score and records arrival_all "per turn". It neither requires nor bars the value. See O6.
- (b) one_id in every batch's stops: sound. "With its count recorded" requires a count; the place is Code's. In the gate's stops it is a rule-23 counter only.
- (c) gate turns with d None and arrival fields None: sound. "No arrival hurdle" requires no score, and d has no meaning off BK's scale. Nothing in the repository reads "d"; gcal_decode_compare keys on batch.
- (d) the gate's extra figures: sound. Count, pass and stops are required; the rest is provenance. coherence_pass duplicates pass.
- (e) early_pause: required by §3 ("`early_pause` recorded").
- (f) sign +1: sound, and required in substance. §2.5 ties the batch to "the campaign's own injection norm for f = 0.20", and the campaign's sign there is +1. The text names no sign.
- (g) no gate turn in the smoke: sound. It keeps GC19's batches, and §2.5 does not speak to the smoke. The consequence is B2.
- Undeclared but harmless:
  - every injection is built and sha-checked before the first forward (G:456-460);
  - the gate runs whatever +ρ/2 gave (as built);
  - a smoke also checks span_reward's sha16 and records gate_sha16.

O3 — Brief item 5.
- Does the suffix hide a defect any check should catch? Yes: it hides the coherent-versus-non-empty confusion (M2, F2).
  - Before the delta, a turn of 1-3 ids was a length collapse, so G:785 told the two apart.
  - Still covered: the heuristic itself (by the literal strings), and coherence computed on the wrong text (by G:762-763).
- Is every count-dependent flow now determined by construction? No.
  - By construction: mute, both, b36/b35, env8.
  - Independent of the count: es, env7, the smokes, env4-env6, the canned exits.
  - Not by construction: the flows in F1.

O4 — The count: I agree with 569.
- gcal's chk call sites go from 39 to 46: added at G:702, 802, 836, 906, 919, 925, 1073.
- The driver's go from 148 to 150: added at D:3160 and D:3355. x46 and x47 are cases inside D:3469's single check.
- Nothing is removed, and none of the nine is in a loop or a branch.
- I expect no failures if F1's precondition holds. If it does not, the failures are as F1 describes.

O5 — Under §1.4 (i), a baseline with fewer than two turns of two or more ids leaves Welch's t undefined. That is a +ρ fail, so the early STOP precedes the early PAUSE even for an incoherent baseline (G:904-909). Worth a line in ADDENDUM-n3.

O6 — A one-id turn's arrival_all is the position-0 (sink) projection alone. Any pooled arrival_all summary at the read should split out or drop n_tok = 1.

O7 — The gate's turns share the 48 seeds with every batch (common random numbers); each row carries index and seed, so the read can pair them.

O8 — Nothing in the code checks ADDENDUM-n3's commit. §2.5's "runs on nothing before the addendum's commit" binds through the launch files.

DEPARTURES
None of the brief's rules breached, by my reading. Stated plainly for the seat to class:
1. `git rev-parse HEAD` and `git rev-parse 616e940`: revision names with no path, so no pathspec.
2. The gcal diff's output was too long for the console, so the harness saved it to this session's tool-results folder (outside S and the repository). I read that saved copy with the file-reading tool and counted its +/- `chk(` lines with `/usr/bin/grep -c`. This is the kind of read classed for 035947e's reviewer.
3. Reads beyond the brief's named symbols:
   - gvec.py :1-140 and :440-574;
   - schema.py :741-790, :880-939, :1625-1649;
   - a grep of directions.py for CAPTURE_FROM;
   - greps of the n package's guard, ids and keys modules;
   - D:1-370;
   - one `git grep -l -E 'gcal' -- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'`, filtered to .py names.

No interpreter but shasum. Nothing written. No guard marker in any argv. Nothing under data/ listed or read. In S, only the brief and the two TO files, each by name.
