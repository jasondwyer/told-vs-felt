# n package — BUILD: the blind review with mutants, and Code's dispositions

*The n-build session (Code), PI date 2026-11-16. The BUILD's blind review (PROPOSAL-n v0.2 §8 step 6). One blind
reviewer, a Code subagent, read the n package's drafts against n v0.2, rule 5(f) and the committed schema. It was
briefed to run no Python and to write nothing, under the list of record v2's items 1–5, quoted verbatim, and the
coordinating session's lines on `data/mf3`. It returned 21 findings and 20 mutants. Code then ran those mutants, and
five of its own, against the n package's self-test in battery windows the coordinating session granted.*

*What it read: the drafts in Code's scratch build folder, with `valence_core/n/schema.py` at v4.4 (`4bed3f9a…4665`,
the bytes `14e65d8` committed while the review ran). The drafts the BUILD commits carry the dispositions below and,
after them, the step-3 changes and the second review's fixes (the companion raw). The BUILD entry gives the package
sha256; the second site check's inputs raw gives each draft's.*

*The report is reproduced as the reviewer returned it. It names the drafts as build/<path>, Code's scratch copies,
with the line numbers it read.*

*After this review, the drafts, with the dispositions below applied, went to the box's first site check (`645bd3f`'s three site-check raws). Mutant
m05 was killed there (below), and the G-VER trial stopped the BUILD for the seat. The seat's answers (`52b2c97`) and
ADDENDUM-n1 (`a61f13d`) then changed the package at step 3: the ids of record, G-VER on committed data, the capture
band in per-layer arrays written in place, the keepers, kfold10 and the PASS rule. Those changes had their own blind
review with mutants, recorded in the companion raw. The dispositions below stand as they were at this review; where
the seat has since ruled, the BUILD entry says so.*

## The review, as returned

## Blind review of the n package build (build/valence_core/n/*, build/scripts/n_sessions.py)

I read every named build file in full, and the spec parts the brief names. I ran no Python, wrote nothing, and read nothing under data/. The only commands I ran were scoped digests, scoped greps and sed over spec files.

The core 5(f) construction checks out against its sources:
- **Mask:** built from the record's spans. The read position and every non-span position are zero, and every PositionSpec is checked position by position. build_mask and the schema both refuse a span that reaches the read position.
- **Shadow:** each steered read is paired with its shadow by ids_sha.
- **Dose:** `at_frac` against the dose map, rechecked by `expected_alpha` and `check_record`. Sign and site are also checked.
- **Read paths:** the cached and fresh constructions compute the same quantity.
- **Renderer and N4:** the two recorded re-splits, the told-line insertion and N4's prefix assertion are right.
- **Dose map and cells:** the merge rule is right, and cells write the array before the JSON and recover from a crash between the two.
- **Hashes:** PROPOSAL_SHA256 equals the sha256 of the proposal file at the root. The build's schema.py is not the committed 5a97527 blob: it adds the report and G-READ forms. I reviewed the build's version.

### PART 1 — Defects, most damaging first

1. **DEFECT — G-READ-n cannot PASS, whatever the data.** (build/valence_core/n/probe.py:16-17, 58-68; schema.py:741-742; primitive.py:225)
   - **What the code does:** the band is the captured layers, `[layer, n_layers-1]`, which `check_stage_identity` forces. PASS needs the band median ≥ .90 and every layer above its shuffle null.
   - **Why that fails:** at index `layer`, the read position's residual is computed before the hook adds the state at earlier positions. So the steered capture equals the shadow's bit for bit; the primitive's own self-test asserts this (primitive.py:407-409).
   - **Consequence:** every site-layer contrast has identical paired rows. Its LOSO AUC is exactly 0.5 and never above its null, so the two-layer median is at most 0.75.
   - **Spec:** n:121 asks for "k's bar"; n:48 (B3) asks for "k's form". k's band (G3, L51–L62, k:261-264) lies wholly after k's site (L48, n:10). Rule 5(f)(ii) needs a gate that can open.
   - **Damage:** every null is "concluded, not answered" (n:32, n:138) by construction, and G-ANL-n's PASS branch is unreachable. Code flagged the capture layer (Q5 at 718c48e; the primitive self-test's "BUILD flag"), but the band and the PASS rule still build it in.
   - **Fix:** capture a post-site layer (layer+1, or a declared post-site band as in k), and change the schema's `capture_layers` rule with it. Keep the site out of the band. Add a probe self-test on the CausalDouble's real captures that reaches PASS.

2. **RISK (high) — no check binds label ids to their cues.**
   - runner.py:380-389 passes `labels[s.cue_S]` and `labels[s.cue_U]` from a callable. schema.py:331-332 says `label_ids_S` is "cue_S's token ids", but `check_record` (802-807) checks only that the sequences are non-empty, distinct and not prefixes.
   - The identity's `label_convention` (417-418) is a name only, and verify.py checks no labels.
   - **Damage:** a swapped or mis-tokenized table flips every margin and pick. It does so identically on both paths, so fidelity and identity never notice (mutant 1 survives).
   - **Fix:** put the label table or its sha256 in the identity, assert it in `run()`, and have G-VER decode each label. Give the runner self-test asymmetric labels with a known margin sign.

3. **RISK — the fidelity criterion has no known-answer test.**
   - `TAU` (schema.py:228) and `fidelity_numbers` (483-490) are shared by the writer (primitive.py:247) and the checker (schema.py:935).
   - Every self-test value comes from the same function, so `scale = 1` (rel in nats: ledger (51)'s exact failure, n:14), a min/max swap, or TAU÷10 all survive.
   - **Spec:** n:77, TAU = 0.0178835444 "of the read's scale" as `precondition_cache` defines it.
   - **Fix:** add a known-answer test from a BK read in the committed G-DATA inputs (the sessions self-test already reads data/n/bk), and assert `f"{TAU:.10f}" == "0.0178835444"`.

4. **RISK — the binomial's p0 path.** (runner.py:62-70, 172)
   - **(a) Overflow:** `binom_tail` multiplies `math.comb(n, k)`, an int, by a float. For 0 < p0 < 1 and a batch of roughly 1,030 or more trials this raises OverflowError ("int too large to convert to float"). A campaign that never fires accumulates about 3,500 trials, so the invocation would crash with no report. This is latent while p0 = 0/2400 (schema.py:442).
   - **(b) Untested at real n:** p0 is only tested at n = 4. A floor such as `max(p0_count, 1)` still fires there, but at n = 160 a single exceedance gives a tail of about 0.065 and never fires (mutant 10).
   - **Fix:** compute the tail with exact Fractions or in log space. Test n = 3,200 with p0 = 1/2400, and one exceedance at cadence 160 under p0 = 0.

5. **DEFECT (minor) — the cadence counts re-computations, not reads.**
   - runner.py:163 evaluates at every 160th re-computation (its PIN, runner.py:31-37). n:77 says "cadence every 160 reads", and schema.py:444 says "cadence in reads".
   - **Damage:** in stretches where only about 10% of reads re-compute, an exceedance waits up to about 1,000 launches (N2's 960 reads carry about 96 trials), and the scope widens to later arms.
   - **Fix:** evaluate every 160 launches, or reword the field and the lock.

6. **RISK — the HF backend's steered paths are never tested.**
   - hftiny.py:69-99 runs `full` only unsteered and `read` only for the shadow. Mutant 5, which drops the injection from `HFBackend.full`, survives on both sites.
   - hftiny.py:65-66 and 82-83 compare `logits_to_keep=1` logits with the full forward by exact equality. CPU BLAS (GEMV vs GEMM) need not match bit for bit, so the box site check could fail spuriously.
   - **Fix:** add a steered cached-vs-fresh hftiny case and a steered read, both within a tolerance.

7. **RISK — the runner's self-test never drives a −1, N2, N1-P or N4 read.**
   - The toy plan is only N1-V at 0, +1 and +1/2 (runner.py:513-517).
   - Untested: `_injection`'s sign (226) and program-scale (220-221) branches, the told-line naming (367-369), and N4's rendering and identity path.
   - A fault there is loud: a SchemaError or SystemExit at the first such read, with no report, recurring on every resume. But it would only surface mid-campaign.

8. **RISK, with a doc DEFECT — the keyed draws are neither known-answered nor bound.**
   - keys.py:51-64 never calls m's `stream_known_answer` (valence_core/m/keys.py:37-49, whose PIN is a STOP on both sites).
   - Only the random directions are sha-checked (runner.py:223). N4's schedule and the fidelity sample are not in the identity.
   - schema.py:100-104 says the runner checks N4's 80/80 split and present-order balance. `campaign_order` (runner.py:89-113) checks neither.
   - **Fix:** call the known-answer check at stage start, put the schedule's and the sample's sha256 in the identity, and assert 80/80 plus the 40/40 and 39/41 split.

9. **RISK — three schema refuse cases are not single-defect.**
   - "a span reaching the read position" is caught by the n_steered check (847), not the span bound (838).
   - "N1-P with the S spans only" is caught by the retention check (850), not the SU check (845).
   - "COMPLETE over a standing pause" is caught by the incomplete-arm check (1349), not 1343.
   - So weakening 838, 845 or 1343 survives (mutants 15 and 16).
   - **Fix:** coordinate the other fields in those cases, as schema.py:1650-1653 intends, and assert the targeted message in verbose mode.

10. **RISK — reads can be launched after a read-less end-of-run fire.**
    - After a CAP end whose end-of-run evaluation fired (runner.py:411-424), a resume with a larger cap launches more reads (359-364). schema.py:157-159 says such a pause "resumes nothing".
    - Its batch is never cleared on replay (349-350), so the old exceedance fires again. `check_report` then refuses the report (schema.py:1294-1295) after the reads are already on disk.
    - The cap and the binomial's alpha are StageInputs (runner.py:200-201), not identity fields, so a resume can change both unchecked.

11. **RISK — G-VER's span check is weaker than its docstring.**
    - The docstring (verify.py:7-8) says each span ends on "a non-empty piece of the passage's tail". The code (verify.py:34-35) only needs one of the span's last two tokens to decode non-blank, and skips the check entirely when `decode` is None.
    - Spans shifted inside a passage would pass.

12. **NOTE —** G-READ-n's assembly is unbuilt. Nothing yet builds the pole or shadow contrasts from cells, picks the norm-matched comparator (+d_eq/+d_20 for span_reward), or handles merged points and NOT-COMPUTED (schema.py:187-196).

13. **NOTE —** a pause on a shadow stands only on N1-V (SCOPE pin, runner.py:29-30). Every other arm's Δm pairs with that shadow (n:87, n:136-140).

14. **NOTE — blinding on error paths.** `_check_type` prints `{v!r}` (schema.py:584) and the pick check prints "should be 'S'" (900). Both reach SystemExit text (cells.py:97, runner.py:248) and so stdout and raws (n:130).

15. **NOTE —** primitive.py:145-146 divides by the label mass with no guard (ZeroDivisionError on underflow). Separately, `Monitors.observe` counts a re-computation whose fresh path is non-finite as a trial with no exceedance (runner.py:148-162).

16. **NOTE —** the read window is checked only at append (schema.py:808-809), after the forward. Rule 28(d)(c) wants it checked before.

17. **NOTE —** `append_record` (cells.py:119-138) never checks the record's capture sha16 against the rows it writes; that is first checked at the next load.

18. **NOTE — I/O outside the cap.** Every append rewrites the whole array and JSON (cells.py:130-137): about 12 GB fsynced over the campaign, plus O(rows²) `check_record` calls. None of it counts toward `used_ms`.

19. **NOTE —** the fidelity sample is per session. N1-R's 2,880 non-±1 reads depend on Binomial(40, 0.1) floor sessions (none sampled with p ≈ 0.015), and nothing checks the ≈ 420 at n:95. `label_mass_below_floor` is always null (runner.py:290).

20. **NOTE —** no production writer calls `guard.refuse_out` (runner.py:302-303, 441-442; cells.py:135-137). `run()` does not assert unique, increasing plan launch indices, or that the indices on disk match the plan's.

21. **NOTE (spec, for the seat) —** N2-E reads at exactly f = 0.20. Rule 5(f)(iv) says "below dose 0.20" unless 5(d)'s gate passes; n:48 and n:81 read it as "never above". The code follows n.

### PART 2 — Mutants (all files under build/valence_core/n/)

14 of the 20 are expected to survive the self-test.

| # | file | old text | new text | invariant broken | expected killing check |
|---|---|---|---|---|---|
| 1 | runner.py | `labels[s.cue_S], labels[s.cue_U]` | `labels[s.cue_U], labels[s.cue_S]` | m = log p(S) − log p(U) (n:77); every margin and pick flips, identically on both paths | none expected |
| 2 | schema.py | `"N1-P": "SU"` | `"N1-P": "S"` | N1-P steers both zones' 12 turns (n:89); otherwise P(d) equals the valenced effect and G-LEAK-n never certifies | chk("primitive: N1-P steers all twelve turn spans") (the schema's refuse case still refuses, via retention) |
| 3 | schema.py | `scale = max(abs(logprob_S), abs(logprob_U))` | `scale = 1.0` | TAU is scale-relative (n:77, ledger 51); in nats most re-computations exceed | none expected |
| 4 | primitive.py | `backend.full(ids, ls, placed, capture_layers)` | `backend.full(ids, ls, [], capture_layers)` | the fresh path runs under the identical mask | chk("runner: a small run completes and obtains its plan") (the toy +1 reads exceed TAU, so the end-of-run fire gives PAUSE) |
| 5 | primitive.py | `self._run(seq, injections, capture_layers` | `self._run(seq, (), capture_layers` | the same, on the HF backend | none expected (hftiny is skipped on the laptop and unsteered on the box) |
| 6 | primitive.py | `if shadow["ids_sha"] != _sha(ids):` | `if shadow["ids_sha"] is None:` | 5(f)(i): shadow over identical token ids | chk("primitive: a shadow over other token ids is refused") |
| 7 | primitive.py | `rows_S[k]` | `rows_S[0]` | the restricted read sits at the first divergent token | none expected |
| 8 | probe.py | `np.percentile(null, 95)` | `np.percentile(null, 50)` | above the 95th percentile of the shuffle null (k:263-264, n:121) | none expected |
| 9 | directions.py | `N_PCS = 10` | `N_PCS = 1` | U is the first ten neutral PCs (n:36, BK §3.1) | none expected |
| 10 | runner.py | `self.p0_count / self.p0_n` | `max(self.p0_count, 1) / self.p0_n` | exact binomial against p0 = 0 (rule 21); one exceedance in 160 no longer fires | none expected |
| 11 | runner.py | `if f["exceeds_tau"]:` | `if f["exceeds_tau4"]:` | the binomial and counters count rel > TAU; TAU/4 is only the sensitivity row | none expected |
| 12 | runner.py | `if not rec["finite"] or (f is not None and not f["finite"]):` | `if not rec["finite"]:` | NaN/inf on either path pauses (n:148) | none expected |
| 13 | cells.py | `not m_resume.same_json(cell["stage_identity"], dict(identity))` | `not m_resume.same_json(cell["stage_identity"], cell["stage_identity"])` | a resume is never spliced across identities (n:103) | chk("cells: a resume under another identity is refused (never spliced)") |
| 14 | runner.py | `halted = True` | `halted = False` | a fire found on replay is a pause, and nothing launches | chk("runner: a fire whose invocation ended before its report is a pause found on replay; nothing launched") |
| 15 | schema.py | `b0 <= rec["read_position"]:` | `b0 <= rec["seq_len"]:` | 5(f): no span reaches the read position (record-level check) | none expected (the refuse case is caught by n_steered) |
| 16 | schema.py | `if standing and end not in ("PAUSE", "PI-STOP"):` | `if standing and end not in ("PAUSE", "PI-STOP", "COMPLETE"):` | no COMPLETE over a standing pause (n:136) | none expected (the refuse case is caught by the incomplete-arm check) |
| 17 | keys.py | `FID_FRACTION = 0.10` | `FID_FRACTION = 0.01` | the 10% keyed sample (n:77, n:95) | none expected |
| 18 | schema.py | `TOLD_LINE = "Prefer {zone}."` | `TOLD_LINE = "Prefer {zone}"` | N4-T's pre-registered line (n:95, n:50) | none expected |
| 19 | verify.py | `"PASS" if (ok_ids == ok_spans == ok_n4 == n and not problems) else "STOP"` | `"PASS" if ok_ids == n else "STOP"` | G-VER STOPs on any mismatch (n:119) | none expected |
| 20 | runner.py | `[pr.arm] + list(arms)` | `[pr.arm]` | SCOPE: a binomial fire stands on all of its batch's arms | none expected |

I confirmed each old text occurs exactly once in its file with `grep -c -F`.

### Could not check
- **BK's records under data/n/bk** (off-limits): the scale definition and TAU in `precondition_cache`, the positions and ids of the G-1 re-splits, the 39-token tail, the turn_spans tiling, whether BK's ids carry a BOS, and the label convention.
- **The seat answers and dated notes the schema cites** (G-1/G-2, GA-4/GA-5, N1/N2, the Q1–Q5 block) and the m anchors: these were outside my reading list, so I relied on the schema's quotations of them.
- **Anything that needs Python:** whether the self-tests pass as built and the exact kills. Mutant 4's kill assumes the double's +1 state moves label S's log-prob by more than about 0.25 nats; I estimate O(1).
- **Pod-side behaviour:** numpy QR sign conventions, and transformers on the pod (`logits_to_keep`, `DynamicCache.crop` on inference tensors).
- **valence_core/discrim.py** (`auc_from_scores`' tie rule) was not read.


## Code's dispositions

The review read the drafts as they stood in Code's scratch build folder, with the schema at v4.4 (`4bed3f9a…4665`,
the bytes `14e65d8` committed while the review ran). Every change below is in the n drafts or the driver; `schema.py` is unchanged. Each
reading left open is flagged in the BUILD entry, pending the seat (the PI's routing of 2026-11-16, N.9).

- **1, DEFECT (G-READ-n cannot PASS under the encoded capture layers).** Not changed. This is Q5 of n-build's early
  block (`718c48e`), before the seat. The encoded reading, `[layer, n_layers - 1]`, stands as Code's interim reading.
  It is the first flag of the BUILD. The fix waits on the seat's ruling on Q5: a post-site capture, the schema's
  `capture_layers` check moved in its own commit, and a probe test on the double's captures that reaches PASS.
- **2, RISK (no check binds label ids to their cues).** Applied in part. The runner's self-test checks a known answer:
  a record's `logprob_S` is its cue_S label's, recomputed on the double's full forward. This kills mutant m01.
  Binding the label table in the stage identity is a schema change. It waits on Q4 (BK's label convention, recovered
  on the box) and is flagged.
- **3, RISK (no known answer for the fidelity criterion).** Applied. The primitive's self-test checks
  `fidelity_numbers` against hand-computed values on both sides of TAU, and TAU's printed value 0.0178835444. Kills m03.
- **4, RISK (the binomial).**
  - (a) Overflow: applied. `binom_tail` takes the exact distribution's terms in log space and sums the smaller side.
    A known answer at n = 3,200, and at n = 7,360 a check that the tail is a probability (no overflow).
  - (b) Untested at real n: applied. Under p0 = 0 one exceedance in 160 fires at the cadence; under p0 = 1/2400 it
    does not. Kills m10.
- **5, DEFECT (the cadence counted re-computations, not reads).** Applied. The cadence is now in reads, as the
  identity's field and n §2.1 have it. A batch is evaluated at its first trial on or after each multiple of the
  cadence, so a fire's batch still ends at a read it counts, as the schema requires. A test crosses a boundary at
  reads with no re-computation. Kills m22.
- **6, RISK (the HF backend's steered paths untested; exact float equality).** Applied. hftiny compares within 1e-4,
  recording the deviation. It adds a steered cached-versus-fresh comparison under the same injection, and a steered
  read paired with its shadow. hftiny runs only where torch is: m05 survives on the laptop and is the box site
  check's to kill.
- **7, RISK (the runner never drives a −1, N2, N1-P or N4 read).** Applied. The runner's self-test drives a plan
  through all of them, checking the sign, the twelve N1-P spans, N2-E's f·R_ℓ alpha, and N4-T's and N4-Ts's lines.
- **8, RISK (the keyed draws neither known-answered nor bound).** Applied in part:
  - `run()` checks m's stream known answer at every start, and so does keys' self-test;
  - `campaign_order` checks N4's schedule (80/80, 40 told-S per present-order group);
  - `FID_FRACTION` is pinned, and the realized sample's size is range-checked. Kills m17.
  The schedule's and the sample's sha256 in the stage identity are a schema change, flagged for LOCK-n.
- **9, RISK (three schema refuse cases are not single-defect).** Applied outside `schema.py`. The package self-test
  carries single-defect versions:
  - the record-level span bound, in the primitive's self-test. Kills m15;
  - a COMPLETE report over a standing pause with every arm complete, in the runner's. Kills m16.
  The schema's own cases are fixed at its next commit (flagged). m02 is killed by the schema's own self-test as well
  as by the primitive's.
- **10, RISK (reads after a read-less end-of-run fire; cap and alpha not bound).** Applied. A resume under another cap
  or alpha than the stage's report records is refused (kills m23). After a read-less end-of-run fire, a resume that
  would launch is refused. Cap and alpha stay inputs, read from the lock by the stage command at its step (flagged).
- **11, RISK (G-VER's span check weaker than its docstring).** Applied:
  - each turn span must decode to exactly its turn's rendered text;
  - G-VER cannot PASS without a decoder;
  - a synthetic session under a character tokenizer exercises the PASS path and each failure branch. Kills m19 and
    m25.
  G-VER on BK's ids, with the real tokenizer, is the box site check's trial.
- **12, NOTE (G-READ-n's assembly unbuilt).** Stated in the BUILD entry. The probe's arithmetic, the result builder
  and the artifact builder are built, the artifact checked by `check_gread`. The assembly from the campaign's cells
  is wired at step 15 with its stage, as every stage is wired at its own step.
- **13, NOTE (a pause on a shadow stands only on N1-V).** Applied. A pause on a shadow also stands on every arm whose
  steered reads of that session pair with it (5(f)(i)). Kills m21. It is part of the flagged SCOPE pin.
- **14, NOTE (blinding on error paths).** Applied. Cells stop a refused record or cell with the failing field's path
  only, never the message's values. Kills m24, once the test planted a type error whose message quotes the value.
- **15, NOTE (division by the label mass; a non-finite fresh path counted as a trial).** The first is applied: the
  restricted read takes a sigmoid of the two logits' difference. Known answers check its row (kills m07) and an
  underflowed mass. The second is kept: such a read pauses as nonfinite (a test kills m12), and counting its trial
  changes no decision.
- **16, NOTE (the read window checked after the forward).** Applied. The runner checks the forward's length against
  `read_window` before it launches.
- **17, NOTE (the capture's sha16 unchecked at the write).** Applied, with a test.
- **18, NOTE (I/O outside the cap).** Noted. The cap's `used_ms` counts model work only, a flagged reading. Rewriting
  whole arrays costs I/O, not reads; G-TIME-n measures the wall-clock.
- **19, NOTE (the per-session fidelity sample; N1-R's share; `label_mass_below_floor` null).** Noted and flagged. The
  sample is per session (keys' PIN), and its realized size is reported at G-TIME-n and in LOCK-n. The label-mass
  floor is the lock's.
- **20, NOTE (`refuse_out` unused; plan indices unasserted).** Applied in part. `run()` asserts that the plan's launch
  indices are 0, 1, …, and that each record on disk is the plan's read at its place. `refuse_out` is for the stage
  commands, wired at their steps.
- **21, NOTE (N2-E at f = 0.20 against 5(f)(iv)).** Flagged for the seat. Rule 5(f)(iv) says "below dose 0.20 for the
  reward axis unless 5(d)'s own gate is separately passed"; n §0.10's B3 and §2.3 read it as never above 0.20. The
  code follows n.

## The mutant runs

Each mutant was one asserted-unique edit to a fresh scratch copy of the overlay: HEAD's `valence_core` and
`data/n/bk`, with the drafts on top. Each ran the n package self-test (`scripts/n_sessions.py --selftest`) under the
jlens venv at nice 19, in battery windows the coordinating session granted. KILLED means the self-test failed.

- Mutants: the reviewer's 20 (m01–m20), adapted where the fixes changed the code (m11's comparison, m20's call), and
  5 of Code's for the new guards:
  - m21, the shadow scope;
  - m22, the read cadence;
  - m23, the resume's cap check;
  - m24, the redaction;
  - m25, G-VER's span decode.
- Batch 1 used a symlinked `data/`. That moved the guard's refuse-out checks outside each copy, so they failed in
  every mutant. Its verdicts were void and are not reported as results. For the record, from the script, the code
  and its output (the coordinating session asked):
  - **Where the symlink pointed.** Each copy's `data/` linked to the scratch overlay's `data/` (the script's
    `ln -s "$S/overlay/data" "$M/data"`, `$S` the scratch folder), not to the repository's `data/`. The overlay's
    `data/` was made by `git archive HEAD valence_core data/n/bk | tar -x` and held `data/n/bk` alone. No path
    through the symlink reached the repository's `data/`, and no `data/mf3`, `ckpt` or `reports` directory existed
    under its target.
  - **What was read.** The package reads data only through `sessions.load_sessions()`: BK's 14 skeleton files under
    `data/n/bk/`, here the overlay's copies. The guard's checks build paths such as `data/m/x.json`, then resolve and
    compare them; `refuse_out` also asks whether each refused root exists. That is a stat of a path that did not
    exist under the overlay. Under any `data/`, nothing listed a directory but BK's skeleton folder, which
    `load_sessions` lists (here the overlay's copy), and nothing read `data/mf3`, a `ckpt` or a `reports` directory,
    in the repository or the overlay.
  - **What was written.** Nothing, under any `data/`. The self-test writes only under its `TemporaryDirectory`,
    which the driver asserts is outside the repository. `refuse_out` and `refuse_test_out` only return a path or
    raise; they open nothing.
  - **What the failures mean.** The guard did not refuse. Resolved through the symlink, `data/m/x.json` and the
    others lay outside the copy's root and outside every refused root, so `refuse_out` returned them and the checks
    failed with "accepted". The checks only call the function and never write to the returned path, so nothing was
    written. With `data/` copied (batches 2 and 3), the guard refused every one, as its checks require.
- Batch 2 copied `data/`: 23 killed. m05 survived, as expected, and so did m24, whose test planted a value the
  schema's message does not quote.
- Batch 3 ran after the redaction test was fixed: **24 of 25 killed**. 23 were first caught by a check naming the
  invariant the mutant breaks; m04 was first caught by the runner's small run, which names none.
  **m05 survives on the laptop**: the HF backend's fresh path runs only where torch is, so the box site check runs
  it. The first site check killed it there (below).

**The 25 mutants, batch 3** (the edit; the invariant it breaks; the result and the first check that failed):

- **m01** (`runner.py`): `spec, labels[s.cue_S], labels[s.cue_U],` → `spec, labels[s.cue_U], labels[s.cue_S],`. Breaks: labels bound to their cues (m = log p(S) - log p(U), n §2.1). **KILLED**, first by "runner: a record's logprob_S is its cue_S label's (a known answer on the double: labels bound to cues)".
- **m02** (`schema.py`): `"N1-P": "SU"` → `"N1-P": "S"`. Breaks: N1-P steers both zones' twelve turns (n §2.4). **KILLED**, first by "refuse N1-P with the S spans only".
- **m03** (`schema.py`): `scale = max(abs(logprob_S), abs(logprob_U))` → `scale = 1.0`. Breaks: TAU is scale-relative (n §2.1). **KILLED**, first by "primitive: BK's fidelity criterion, a known answer".
- **m04** (`primitive.py`): `backend.full(ids, ls, placed, capture_layers)` → `backend.full(ids, ls, [], capture_layers)`. Breaks: the fresh path runs under the identical mask. **KILLED**, first by "runner: a small run completes and obtains its plan".
- **m05** (`primitive.py`): `self._run(seq, injections, capture_layers` → `self._run(seq, (), capture_layers`. Breaks: the same, on the HF backend. **SURVIVED on the laptop**, where hftiny runs only if torch is present. **KILLED at the box** in the first site check (`results/raw/2026-11-16_n-build_sitecheck_out.txt`, `645bd3f`): 164/166, by "hftiny: steered: cached continuation rows == the full forward's under the same injection (tol 1e-4)" and "hftiny: the steered read's re-computation agrees with its cached read (below TAU)".
- **m06** (`primitive.py`): `if shadow["ids_sha"] != _sha(ids):` → `if shadow["ids_sha"] is None:`. Breaks: 5(f)(i): a steered read's shadow over identical token ids. **KILLED**, first by "primitive: a shadow over other token ids is refused".
- **m07** (`primitive.py`): `row = np.asarray(rows_S[k], dtype=np.float64)` → `row = np.asarray(rows_S[0], dtype=np.float64)`. Breaks: the restricted read at the labels' first divergent token. **KILLED**, first by "primitive: the restricted read uses the first divergent token's row (a known answer)".
- **m08** (`probe.py`): `np.percentile(null, 95)` → `np.percentile(null, 50)`. Breaks: above the shuffle null's 95th percentile (k's G1/G3 form). **KILLED**, first by "probe: the null's bar is the shuffles' 95th percentile (k's G1/G3 form)".
- **m09** (`directions.py`): `N_PCS = 10` → `N_PCS = 1`. Breaks: U is the ten leading neutral PCs (n §0.8). **KILLED**, first by "directions: U is the ten leading neutral PCs, and v is orthogonal to all ten (n §0.8, BK §3.1)".
- **m10** (`runner.py`): `self.p0_count / self.p0_n` → `max(self.p0_count, 1) / self.p0_n`. Breaks: the exact binomial against p0 = 0 (rule 21). **KILLED**, first by "runner: under p0 = 0 one exceedance in 160 fires at the cadence; under p0 = 1/2400 it does not".
- **m11** (`runner.py`): `if f["exceeds_tau"] is True:` → `if f["exceeds_tau4"] is True:`. Breaks: the binomial counts rel > TAU; TAU/4 is the sensitivity row. **KILLED**, first by "runner: a re-computation above TAU/4 and below TAU is no exceedance; it counts in the TAU/4 row".
- **m12** (`runner.py`): `if not rec["finite"] or (f is not None and not f["finite"]):` → `if not rec["finite"]:`. Breaks: NaN/inf on either path pauses (n §6). **KILLED**, first by "runner: a finite read whose re-computation is not finite fires nonfinite".
- **m13** (`cells.py`): `not m_resume.same_json(cell["stage_identity"], dict(identity))` → `not m_resume.same_json(cell["stage_identity"], cell["stage_identity"])`. Breaks: a resume is never spliced across identities. **KILLED**, first by "cells: a resume under another identity is refused (never spliced)".
- **m14** (`runner.py`): `            halted = True` → `            halted = False`. Breaks: a fire found on replay is a pause, and nothing launches. **KILLED**, first by "runner: a fire whose invocation ended before its report is a pause found on replay; nothing launched".
- **m15** (`schema.py`): `if not prev <= a0 < b0 <= rec["read_position"]:` → `if not prev <= a0 < b0 <= rec["seq_len"]:`. Breaks: no span reaches the read position (5(f)). **KILLED**, first by "primitive: a record whose span reaches the read position is refused by the span bound (5(f))".
- **m16** (`schema.py`): `if standing and end not in ("PAUSE", "PI-STOP"):` → `if standing and end not in ("PAUSE", "PI-STOP", "COMPLETE"):`. Breaks: no COMPLETE over a standing pause. **KILLED**, first by "runner: a COMPLETE report over a standing pause, every arm complete, is refused by the standing rule".
- **m17** (`keys.py`): `FID_FRACTION = 0.10` → `FID_FRACTION = 0.01`. Breaks: the 10% keyed fidelity sample (n §2.1). **KILLED**, first by "keys: the fidelity sample is n §2.1's 10%, drawn per session".
- **m18** (`schema.py`): `TOLD_LINE = "Prefer {zone}."` → `TOLD_LINE = "Prefer {zone}"`. Breaks: N4-T's line "Prefer [zone X]." (n §0.10, B5). **KILLED**, first by "sessions: N4's lines are n §0.10 B5's".
- **m19** (`verify.py`): `"PASS" if (ok_ids == ok_spans == ok_n4 == n and not problems) else "STOP"` → `"PASS" if ok_ids == n else "STOP"`. Breaks: G-VER STOPs on any mismatch (n §3). **KILLED**, first by "verify: a turn span shifted by one token STOPs G-VER".
- **m20** (`runner.py`): `_scope(pr.arm, pr.dose_label, s.session_id, plan, arms), also=kinds[1:],` → `_scope(pr.arm, pr.dose_label, s.session_id, plan), also=kinds[1:],`. Breaks: a binomial fire stands on its batch's arms (the SCOPE pin). **KILLED**, first by "runner: a binomial fire at a cadence point stands on its batch's arms".
- **m21** (`runner.py`): `arms |= {p.arm for p in plan if p.session.session_id == session_id and schema.DOSES[p.dose_label][1] != 0}` → `arms |= set()`. Breaks: a shadow's pause stands on the steered arms that pair with it. **KILLED**, first by "runner: a pause on a shadow stands on every arm whose steered reads of that session pair with it".
- **m22** (`runner.py`): `if self.batch_reads >= self.next_due:` → `if self.batch_trials >= self.next_due:`. Breaks: the binomial's cadence is in reads (n §2.1). **KILLED**, first by "runner: a cadence boundary crossed at reads with no re-computation is evaluated at the next trial".
- **m23** (`runner.py`): `if prior["cap"]["hour_cap_ms"] != inputs.hour_cap_ms:` → `if False:`. Breaks: a resume keeps the stage's cap. **KILLED**, first by "runner: a resume under another cap than the stage's is refused".
- **m24** (`cells.py`): `the schema refuses the record, at {redacted(e)}` → `the schema refuses the record, at {e}`. Breaks: blinding: a refusal prints no value (n §4). **KILLED**, first by "cells: a refused record stops with its field's path alone, no value (n §4)".
- **m25** (`verify.py`): `if z != zone or decode(list(ids[a:b])) != turn_text(zone, passage):` → `if z != zone:`. Breaks: G-VER: each turn span decodes to its own turn. **KILLED**, first by "verify: a turn span shifted by one token STOPs G-VER".
