# n — G-CAL-n's delta (the seat's three changes): the blind review of draft 4, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over draft 4, the delta from the committed BUILD (`89a55c3`'s
bytes, clean at HEAD `a33252a`) to the seat's three changes (the answers of 2026-11-19, first sitting: §1.9, §1.12
(d), §5 O7):
- `valence_core/n/gcal.py`, from `aba3700c…a3a0` to `8a1a90cd…e98c` (800 lines), read in full;
- `scripts/n_sessions.py`, from `37b8268d…f030` to `20b30972…4665` (3621 lines): G-CAL-n's section and its
  self-test read in full.
Draft 4's self-test had not yet run when the brief went out; it ran 542/542 while the review ran.

**The reviewer's brief** (`8a0a4aed…cf4b`, 75 lines):
- gave the two deltas' FROM and TO files, by sha256, and the `git diff --no-index -U3` form; the seat's answers
  (§1.9, §1.12, §5, §6), the BUILD entry's owed wording and departure (9), the BUILD values-check's O3, and the code
  the change must match (`ids.py`, `sessions.py`, `adapters/base.py`, `testing.py`, `schema.py`), read only;
- named the new departure (10) and the self-test seam (`figures_of`), and asked whether (10) is sound and required,
  whether production can reach a forced pass, and whether every patch is restored on every path;
- asked for findings, surviving mutants, box risks and observations, and for any command a rule bars;
- quoted the list of record v2's items 1–5, verbatim, and barred any interpreter but shasum, any write, any network,
  any model or adapter code run, any guard marker in an argv, anything under `data/mf3`, any whole-tree git status,
  any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the files it named.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (154 lines, sha256
`cdb6cade…a3b7`). It names scratch files only by their paths inside the scratch folder.

**Totals:** 0 BUG; 7 findings (2 RISK, 5 NIT); 5 surviving mutants; 3 box risks; 9 observations.

## 1. Dispositions, applied in draft 5

Draft 5: `valence_core/n/gcal.py` `5a4c7e80…e82a` (851 lines) and `scripts/n_sessions.py` `655430f3…d027` (3624
lines); `keys.py`, `ids.py` and `guard.py` stay at the BUILD's bytes. Draft 6, the bytes committed, adds one
self-test check to draft 5 for the delta's values-check's observation 2, and nothing else (`gcal.py` `61bcafc9…14fc`,
874 lines, +23 −0 on draft 5); this review's scope stays the draft 4 → 5 delta.

- **F1** (RISK), applied: +ρ's hurdles are evaluated once, at the early read, and the result's +ρ figures are that
  evaluation (`early_fig`), never a second computation. The early-STOP self-test records the evaluation's inputs: one
  call, +ρ's 48 turns, the baseline's scored arrivals, sign +1. This kills M1 and its two variants.
- **F2** (RISK), applied: the baseline's coherent count is checked against its turns; a new compute run, whose step
  draws the end of turn whenever it is handed no injection, makes every baseline turn empty and must PAUSE (O7), with
  all four batches and no early STOP; and the bar is one helper, `coherent_enough`, used by every batch and the
  baseline and tested at 35 and 36. This kills M2, M3 and M5.
- **F3** (NIT), applied: "Departures from GC1-GC23's words".
- **F4** (NIT), applied: the docstring says "at every dose generated (after an early STOP, +ρ alone)", and
  CONVENTIONS["arrival"] the same with "+rho".
- **F5** (NIT), applied: the non-early STOP line reads "a hurdle failed at -rho (n:113)", the one way a later STOP can
  happen under the seat's order, and both it and the PAUSE line name the dose map; the canned check's prefix moved
  with it.
- **F6** (NIT), applied: the HF check places the injection from `gcal.STEER_FROM`, and its words say so.
- **F7** (NIT), applied: `_gcal_selftest`'s docstring lists the failure at the first forward, the mid-run failure,
  the non-finite arrival score and the early STOP.
- **M1–M5:** M1 (and its variants) by F1; M2, M3 and M5 by F2; M4 by new assertions that a smoke's `early_stop` is
  false, in both self-tests, and that it prints no "early STOP" line, in the driver's.
- **B1**, applied as the reviewer's pin: on the HF path, an injection placed from position 0 must give other
  last-position logits than one placed from position 1. It is folded into G-CAL-n's existing HF check (one line at
  either site, a skip on the laptop), so the box's count stays 11 above the laptop's; it runs on the box only.
- **B2** asks for nothing. **B3** stands as the reviewer reads it: a non-finite step is refused by `sample`, so it
  ends as a failure with its turns kept.
- **O1** and **O2** go to the seat as readings, in the delta's entry: a STOP takes precedence over O7's PAUSE, by
  (d)'s words, and an incoherent baseline does not end the run early ("otherwise all four batches are generated").
- **O3**, applied: `constants.generation_order` names the order run, so after an early STOP or in a smoke it is +ρ
  and the baseline (§1.12: "`constants.generation_order` names the order run"). An early STOP's record is tested.
- **O4** stands: no `n-gcal-v1` record exists yet, and the fields it names are new in this delta.
- **O5** goes to the seat in the delta's entry: G-CAL-n steers position 0 in every steered turn; the campaign does
  so only in a session whose first turn is an S turn, and in the SU arms.
- **O6:** departure (10) is declared in the delta's entry, as the reviewer reads it.
- **O7**, applied: the seam's restore is asserted after the last patch, and the mid-run failure's unused patch is
  dropped.
- **O8** confirms the owed wording. **O9:** the decode check's flip case now states its precondition (the record's
  first turn has an emitted id); the non-finite case rests on its count of 48 rows, which a double with no emitted id
  at +ρ would fail visibly.
- **The reviewer's departures,** as its report states them, are in the delta's entry, for the seat to class.

## 2. The report as returned

G-CAL-n draft 4: blind review of the delta against 89a55c3

I checked the inputs before reading anything:
- All five sha256s match the brief: FROM gcal.py aba3700c…a3a0, FROM n_sessions.py 37b8268d…f030, TO gcal.py 8a1a90cd…e98c, TO n_sessions.py 20b30972…4665, and the seat's answers e6ff066d…6d5a.
- HEAD is a33252a. Both FROM files are clean at HEAD (rev-parse against hash-object), and so are ids.py, sessions.py, base.py, testing.py, schema.py, RESULTS.md and the values-check raw.

Shorthand below: G = S/step4b/gcal/draft4/gcal.py, D = S/step4b/gcal/draft4/n_sessions.py.

Verdict: no BUG. Draft 4 makes the seat's three changes as worded:
- **§1.9 (Q9):** `STEER_FROM = 0` (G:137) is used at G:210 and G:229. It is recorded as `constants.first_steered_position` (G:466) and in CONVENTIONS (G:160).
- **§1.12 (d):** the order is set at G:134. The early STOP is at G:396–402, with status STOP and exit 2 (G:420, D:2830–2837). The record, the turns and the dose map are written, no −ρ turn is generated, and the record keeps n:113's order (G:403).
- **§5 (O7):** an incoherent baseline is a PAUSE (G:330, G:407).
The owed wording is all applied. The risks are coverage gaps opened by the forced-pass seam.

FINDINGS

F1. RISK, G:396–402 against G:408–412.
- The early-STOP decision `fig(turns["+rho"], base0, 1)` (G:398) is a separate call from the +ρ figures recorded at G:412.
- Every run that reaches G:398 forces "pass": G:609, G:624 and G:673 force True, G:689 forces False, and the driver patches at D:3079 and D:3239. The smoke skips G:396.
- So no check ever sees the early call's inputs: which batch, which baseline list, which sign (M1).
- A defect there would STOP a passing port at +ρ, or let a failing one spend 48 −ρ turns. The recorded figures, recomputed at G:412, would then contradict the record's own status.
- Fix: compute `figures["+rho"]` once at the early read and reuse it in the G:408–419 loop. The existing checks at G:637–638 (count, sign) and G:652 (t) then cover the decision's inputs. Alternatively, give the es run a recording `figures_of` that asserts its first call is (+ρ's 48 rows, the baseline's scored arrivals, +1).

F2. RISK, G:405–407 and G:330 (O7's PAUSE path).
- O7 is exercised only on literal figures (G:709–720) and through the driver's canned compute (D:3125–3147). No compute run ever has an incoherent baseline.
- The baseline's coherent count is checked only against its own pass flag (G:640, where both values come from G:405–407). It is never checked against its turns, because G:636–638 cover STEERED only.
- Hence M2, M3 and conditionally M5 survive.
- Fix:
  - add the baseline to the count check at G:637;
  - add one compute run under `forced(True)` whose step returns eos-dominant logits whenever it is handed no injection. Every baseline turn is then empty with coherent 0, and the steering checks still differ. Assert status PAUSE, `coherence_pass` False, four batches;
  - take the 36 bar from one helper shared with `batch_figures` (G:318/322), tested at 35 and 36.

F3. NIT, G:79. The heading reads "Departures from GC1-GC22's words". But (10) at G:90–91 departs from GC23 (c)'s words (supplement :57). It should read "GC1-GC23's words".

F4. NIT, G:57 and G:165–167. "Both hurdles are computed at every dose whatever the other gave", and CONVENTIONS["arrival"] says "at every dose". After an early STOP, +ρ/2 and −ρ have no turns and no hurdles. Suggest "at every dose generated (after an early STOP, +ρ alone)".

F5. NIT, D:2835–2836 and D:2839–2840.
- Under the seat's order a +ρ fail always ends the run early: the G:412 recompute equals the G:398 decision. So a non-early STOP is always a −ρ fail.
- Both lines also say "the record and the turns are written", but `write()` always writes the dose map too (G:455–457), and the early message (D:2832–2833) names it.
- Suggest "a hurdle failed at -rho (n:113); the record, the turns and the dose map are written", and the same three files in the PAUSE line. The canned check's prefix at D:3144 would move with it.

F6. NIT, D:3505 and D:3509–3511 (the box-only HF check).
- `ls_t` is placed with `gcal.placed(inj_t, 3)`, and the check text says "an injection placed from gen_start moves them". Production places from `STEER_FROM`.
- Suggest `gcal.placed(inj_t, gcal.STEER_FROM)` and the words "placed from STEER_FROM (the whole turn)". B1 has a further pin.

F7. NIT, D:2964–2967. `_gcal_selftest`'s docstring does not list the non-finite-arrival run (D:3218–3230) or draft 4's early-STOP run (D:3231–3252).

SURVIVING MUTANTS

M1. G:398, change `fig(turns["+rho"], base0, 1)` to `..., -1)`.
- Every check still passes: pass is forced on every path that reaches the line (F1), and G:412 recomputes +ρ with +1.
- In production, a +ρ batch that arrives (t ≥ 2) fails the early read: an early STOP of a passing port.
- Variants that survive the same way: G:397 `turns["baseline"]` → `turns["+rho"]`, and G:398 `turns["+rho"]` → `turns["baseline"]`.
- Killed by F1's single computation, after which G:638, G:652 and G:637 kill these, or by a recording `figures_of` in the es run.

M2. G:405, change `turns["baseline"]` to `turns["+rho"]` in `bk`.
- O7 would then read +ρ's coherence.
- It survives because G:640 compares `coherence_pass` with the same mutated count, and D:3087 takes the expected exit from the record's own status.
- Killed by the baseline count assertion in F2.

M3. G:407, change `bk >= COHERENT_MIN` to `bk > COHERENT_MIN`.
- A baseline at exactly 36 of 48 (a pass under §5's "below 36") becomes a PAUSE.
- It survives unless the double's baseline happens to have exactly 36 coherent turns.
- Killed by the shared helper tested at 35/36 (F2).

M4. G:396, delete `not smoke and `.
- In a smoke, +ρ always fails the coherence bar (at most 4 turns), so compute sets early_stop True and prints "early STOP: …". The status stays SMOKE and the exit stays 0.
- The smoke checks (G:770–772, D:3152–3157) read neither field.
- Killed by asserting `smk["early_stop"] is False`, `rec3["early_stop"] is False`, and no "early STOP" line in l3.

M5 (conditional). G:407, change to `"coherence_pass": True`.
- O7's PAUSE could then never fire.
- It survives if the double's baseline has at least 36 coherent turns; env1's status shows which (PASS means coherent).
- Killed by the incoherent-baseline run in F2.

No driver production mutant survives: the message branch and the exit codes are pinned at D:3141–3147 and D:3246–3252.

BOX RISKS

B1 (low). No box check shows that the HF hooks steer position 0 itself.
- The HF check (D:3503–3518) reaches the from-0 placement only through `steering_check` (D:3514) and `generate` (D:3507). Their assertions would hold for any start position.
- By reading, the placement is correct. `valence_core/adapters/olmo_hf.py` builds the mask from `positions.contains(base + p)` with base 0 on the uncached forward (:142–150, :176). `from_index(0)` contains every position (`valence_core/adapters/base.py:76–77`). There is no falsy-start trap.
- Cheap pin: on the tiny adapter, show that the logits under `placed(inj_t, 0)` differ from those under `placed(inj_t, 1)`.

B2. None of the box self-test's cases can load the weights of record or write a canonical folder, by my reading.
- Every `run_gcal` call goes through `env_for`: stub weights, pod and adapter, an out folder under tmp, and an in-repository out refused at D:3059.
- The one in-repository `--out` (x4) is refused at D:2713, before `refuse_out` and before any mkdir.
- `production_gcal_env()` is constructed (D:3062) but never run.
- The `main()` calls run with RUNPOD_POD_ID popped and cuBLAS set to ":16:8", so any call that slipped past the swap would refuse at D:2730–2732.
- `committed_bytes` only runs a read-only `git show`.
- `hftiny`'s adapter is a randomly initialised tiny Olmo2 on the CPU (`valence_core/n/hftiny.py:36–50`).
- The new env7 run is an `env_for` run like the others.

B3 (low). Every steered forward now adds ρ·R·v at position 0, the sink the seat names in §1.1. The double cannot show bf16 behaviour there. A non-finite step is refused by `sample` (G:185–186), so it ends as a failure with its turns kept, never silently.

OBSERVATIONS

O1. The seat did not rule on precedence between STOP and O7's PAUSE.
- Code chose STOP first (G:328–331), pinned by G:719. The early STOP (G:396–402) never looks at the baseline's coherence.
- So an incoherent baseline with a +ρ arrival fail exits 2 as a port-defect STOP. A baseline of all-empty turns gives an undefined t and does exactly this.
- §5 says that against an incoherent baseline "neither hurdle can be read". The seat may want O7 to take precedence.

O2. An incoherent baseline does not end the run early. With +ρ passing, all 48 −ρ turns are generated before the PAUSE. That is the seat's wording ("otherwise all four batches"), but §1.12's §0.4 reasoning would apply equally after batch 2. Changing it is one condition at G:396.

O3. `constants.generation_order` (G:466) always lists all four batches. After an early STOP, and in a smoke, the order actually run is a prefix of it, which `batches` and `early_stop` give.

O4. RECORD_SCHEMA stays "n-gcal-v1" (G:110), while the record gains `early_stop`, `first_steered_position` and the baseline's `coherence_pass`. No v1 record exists yet.

O5. Position 0 is always steered in G-CAL-n but not always in the campaign.
- `STEER_FROM = 0` is the user turn's first token: the encoder adds no special token (D:420–421) and render_v encodes the text whole (`valence_core/n/ids.py:549`).
- Every steered G-CAL-n turn therefore steers position 0. In the campaign, an S span includes position 0 only when the session's first turn is an S turn (turn spans tile from 0, `valence_core/n/sessions.py:142–144`); the SU arms always include it.
- Q9's wording covers this. It matters if G-CAL-n STOPs at +ρ on coherence.

O6. Departure (10) is sound, and the seat's words require it.
- It quotes GC23 (c) verbatim (supplement :57).
- The code matches: batches are scored at G:393–394, the raise is at G:292–293, the log is kept by the rename at D:2817–2824, and D:3218–3230 pins 48 +ρ rows.
- §1.12 (d) reads +ρ's hurdles "as soon as a steered batch and the baseline exist". That needs both batches' scores before +ρ/2 is generated. The same sentence covers +ρ/2, which is now scored before −ρ, so a non-finite +ρ/2 score spends no −ρ turn. −ρ is unchanged.
- The seat restated (c) without the timing, so (10) departs only from Code's own GC23 wording.
- Draft 4's entry should declare (10); the BUILD entry lists only (1)–(9).

O7. The seam (brief item 5): production cannot reach a forced pass.
- `run_gcal` never passes `figures_of`; the canned compute's `kw_seen` check at D:3123–3147 pins that.
- The only other route is the module attribute. It is assigned only at D:3079, D:3185 and D:3239, each followed directly by a try/finally that restores `real_bf` (D:3080–3083, D:3186–3192, D:3240–3243). Nothing sits between the assignment and the try, so every exit path restores it.
- The compute and `run_gcal` swaps are also restored in finally blocks (D:3139–3140, D:3447–3448). `gcal._selftest` passes the seam only as an argument and patches no global.
- Not pinned: a final `gcal.batch_figures is real_bf` check after D:3243 would make the restore explicit.
- D:3185's patch is never consulted: the 61st forward always fails before the early read, which needs at least 98 forwards. It can be dropped.
- A forced figure keeps `coherence_pass` and `arrival.pass` as computed, so forced records are internally inconsistent. These are written only under tmp.

O8. The owed wording is all applied:
- D:154–159: GC1-GC23, and the failed-run folder in the refusals;
- G:69–70: "on every PASS, STOP and PAUSE";
- G:88–89: departure (9), worded as in the entry;
- the values-check's O3: the mid-run check now pins its count `k5` exactly as O3 described (D:3197–3217).
The gcal-decode docstring (D:172–175) also changed, beyond the owed list; it matches D:2950–2959. §1.12's results/raw/ placement for a failed-run folder is a commit-time step, and `.gcal.failed` stays ignored.

O9. Self-test expectation: I expect no check to fail.
- By arithmetic only, the count is 542 on the laptop and 553 on the box: two new checks (G:690, D:3246) and none removed.
- Two checks rest on facts about the re-drawn turns that the code does not assert:
  - the decode check's flip case (D:3380, D:3392) needs the record's first turn (+ρ index 0) to be non-empty;
  - the nanarr check (D:3218–3230) needs at least one non-empty +ρ turn.
- Both are expected to hold, but the from-0 placement re-draws every steered turn on the double.

DEPARTURES

1. One `awk -F: '$1 >= 2540'` filter over grep's listing of D's top-level definitions. awk is an interpreter, which the first rule bars. It read only grep's output of D.
2. One read, with the file-reading tool, of the harness's saved copy of the brief's own gcal.py `git diff --no-index` output, which was too large to print inline. It sits in the harness's tool-results folder, outside S and the repository. No rule names that folder; I state it as the BUILD's reviewer did.

Not departures under the rules, listed for completeness, are reads beyond the brief's named files:
- the supplement raw (one grep, for GC23 (c));
- `olmo_hf.py`, read with the file-reading tool only;
- `guard.py` and `hftiny.py`, one grep each plus a partial read of `hftiny.py`;
- one name-only `ls` of `valence_core/adapters/`, with no marker in its argv.

Otherwise: no write, no network, no model code run, no marker in any argv or pattern, nothing under data/ read, and no listing or glob in S.
