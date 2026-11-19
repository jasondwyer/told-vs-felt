# n — G-CAL-n's BUILD: the blind review of draft 1, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over draft 1's five files and the BUILD's `.gitignore` draft, from
the brief's HEAD `1185e15` (HEAD was `99196e1` when it ran, the five FROM files the same bytes: the report's O1):
- `valence_core/n/gcal.py`, new (`be63ef41…1f5e`, 519 lines), read in full;
- the deltas to `valence_core/n/keys.py` (`6a0f9ad3…812e`), `valence_core/n/ids.py` (`cc614c75…8e76`),
  `valence_core/n/guard.py` (`ef3a7e5b…7a3e`) and `scripts/n_sessions.py` (`5258bcfc…6a02`);
- the `.gitignore` draft (`e1e73d76…6408`), HEAD's with one block added for `data/n/gcal/`.
Draft 1's self-test had run 524/524 before the brief went out.

**The reviewer's brief** (`406f111d…488b`, 86 lines):
- gave the six files and the `git diff --no-index` form;
- gave the specification: G-CAL-n's spec raw (Code's GC1–GC22, the coordinating session's routing, the survey), the
  seat's block on the starred readings, PROPOSAL-n v0.2's n:113, n:81, n:20 and n:130, ADDENDUM-n1 §1.1, §1.2 (v) and
  §1.4, and CLAUDE.md's rules 2 (its annotation), 13, 21, 25 and 28 (d);
- gave the code the change must match, with m's and p's G-CAL for comparison only;
- named the two departures Code already knew of from GC21's words, and asked whether either is unsound;
- asked for findings, surviving mutants, box risks and observations, and for any command a rule bars;
- quoted the list of record v2's items 1–5, verbatim, and barred any interpreter but shasum, any write, any network,
  any model or adapter code run, any guard marker in an argv, anything under `data/mf3`, any whole-tree git status,
  any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the files it named.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (221 lines, sha256
`75d4200f…cd5e`). It names no local path. Its line numbers are draft 1's: Code's scratch keeps those bytes, unchanged;
the committed files are draft 3's.

**Totals:** 0 BUG; 12 findings (5 RISK, 6 NIT and 1 NIT/RISK); 16 surviving one-line mutants; 6 box risks; 13
observations; 3 departures.

## 1. Dispositions

Draft 2 applies every finding but F1: `gcal.py` `5cd43ea0…fdaf` (685 lines) and `n_sessions.py` `34c5f037…bee5`;
`keys.py`, `ids.py` and `guard.py` are draft 1's. It ran 536/536. Draft 3 adds F1 as GC23, routed by the coordinating
session as a PIN declared in the BUILD entry: `gcal.py` `aba3700c…a3a0` (738 lines) and `n_sessions.py`
`37b8268d…f030`. It ran 540/540, and its bytes are the BUILD's. The `.gitignore`'s block is the reviewed draft's, its
comment naming the failed-run folder too (`908f447b…2f2c`).

**Findings:**
- **F1 (RISK), a failure discards every turn:** applied in draft 3, as Code's reading GC23, which goes to the seat
  before the run (the supplement to the starred readings, Q12):
  - (a) each turn is appended to the staging folder's log as it is generated, flushed and fsynced;
  - (b) on a failure, the staging folder is kept as the failed-run folder, never removed, and a later run refuses
    while it exists;
  - (c) a non-finite arrival stays a failure, its turns kept;
  - (d) the batches are generated −ρ last, by one line, `GENERATION_ORDER`; the record keeps n:113's order.
- **F2 (RISK), the generation loop:** applied. A scripted step, keyed on the sequence's length, checks the stop at the
  first end of turn, one forward per step, each step seeing its own output, and the cap.
- **F3 (RISK), compute's wiring:** applied. Every baseline turn equals `generate`'s own at TEMP from
  `keys.gcal_seed(i)`; two +ρ turns equal `generate`'s under +ρ's injection; each steered t equals `welch_t` of its
  scores against the baseline's.
- **F4 (RISK), the constants and boundaries:** applied. The seven constants are pinned. Each bar is checked from its
  other side: 36 coherent pass; a 4-word turn is coherent; 5/9 loops; 4/20 is low; |t| 2.05 passes and 1.95 fails at
  each sign; one scored turn fails arrival and the batch.
- **F5 (NIT), "one place":** applied. The docstring says where the texts live (`prompt_parts`, with its three callers)
  and where the stop is wired (the (v) render's eos_id, the load's assertion, `generate`). `CONVENTIONS`' rendering
  and prompts are derived from `prompt_parts("{zone}")` and `USER_PROMPT`.
- **F6 (NIT), undeclared departures:** applied. They are declared in gcal.py's docstring as departures (4)–(8), against
  GC2, GC9, GC15, GC19 and GC21's sampler, and in the BUILD entry. GC21's HF-path clause is now met by an hftiny check.
- **F7 (NIT), the generation window:** applied. `GENERATION_WINDOW = 4096` is declared apart from `schema.MAX_WINDOW`
  (rule 28(d)(c)). The longest forward is a prompt's ids and the cap − 1, refused before the load above the window, and
  the record holds `generation_window` and `longest_forward`.
- **F8 (NIT/RISK), the prompts check:** applied. The v block's `prompt_template` and each record's `user_sha256` are
  checked against `prompt_parts`, with a refusal case for each.
- **F9 (RISK), gcal-decode:** applied. It checks the record's schema and stage, and prints both files' sha256s. It
  gives each difference's three flags and verdict under both decodes, the count whose flags differ, and each batch's
  coherent count under both.
- **F10 (NIT), the shift:** applied. Each batch's arrival carries the mean, the SD (ddof 1), the baseline's mean and
  SD, and the difference; each batch's stops are recorded (eos, cap, empty).
- **F11 (NIT), non-SystemExit errors:** applied. `gcal_gvec_inputs` parses every field inside its try, and the dose
  map's ValueError is refused like its SchemaError; four refusal cases.
- **F12 (NIT), main()'s refusals:** applied. All nine of gcal's foreign flags and all ten of gcal-decode's;
  gcal-decode missing either folder; --gcal-dir under gcal; render-ids-v with --model-dir or --ids-dir.

**Surviving mutants:** each now meets a check.
- M1 and M2: F2's scripted check. M3 and M4: F3's baseline and +ρ equalities. M5: F3's t re-derivation.
- M6: F4's single-score case. M7–M11: F4's two-sided cases.
- M12: the HF seams over a recording stand-in on the laptop; on the box, the hftiny check, and the steering check
  before each batch at a positive dose.
- M13: committed_bytes of a path HEAD does not hold is None. M14: the site-block case. M15: one case for each clause.
- M16: F12's foreign flags.
- The sampler mutant of O4: the sampler's 200 draws equal an independent inverse CDF at 0.7, which differs from 1.0's.

**Box risks:**
- B1: applied. Every main() call in G-CAL-n's self-test runs with no pod id and a cuBLAS setting the stage refuses, and
  the swapped module is asserted to be cmd_gcal's.
- B2: applied. A steering check runs before each batch at a positive dose (the smoke's +ρ included). Each steered
  batch's stop counts (eos, cap, empty) are printed on its batch line; the baseline's are recorded in the figures, and
  every turn's stop is printed on its turn line.
- B3, B4 and O13: for G-CAL-n's launch files, as the coordinating session routed them.
- B5: F9. B6: F1.

**Observations:**
- O1 and O2: noted.
- O3, O5 and O6: in the supplement to the starred readings, §2, for Q1 and Q11.
- O7, O8 and O12: in the supplement, §3, for LOCK-n v0.1's list.
- O4: applied. O9: applied (the exposure's draws).
- O10 and O11: for (v)'s render commit.

**The reviewer's departures,** as its report states them, for the seat to class (the BUILD entry carries them):
- it read `valence_core/n/runner.py:270–309`, grepped runner.py and schema.py once, and ran `wc -l` over runner.py and
  primitive.py; runner.py and primitive.py are not in the brief's list (schema.py is);
- it grepped all of `scripts/n_analyze.py` once, printing lines outside the `--dose-map` reader and DoseMap, which the
  brief named;
- it read its own over-large diff in the harness's tool-results folder, outside Code's scratch and the repository.

## 2. The report as returned

```text
BLIND REVIEW: G-CAL-n BUILD (n)

The brief (406f111d…) and all eight named scratch files matched their stated sha256s; I checked each by a shell comparison of shasum output. Below, gcal.py, keys.py, ids.py, guard.py and n_sessions.py mean the TO files at S/step4b/gcal/draft/, and gitignore means S/step4b/gcal/commit/gitignore. I took every delta with `git diff --no-index -U3 <from> <to>` from the repository root.

I found no BUG-class defect. The main problem is the failure path (F1): one stage failure throws away the −ρ turns, and those cannot be generated again without new exposure. The self-test also has gaps that leave the generation loop and compute's wiring untested; M1–M6 survive because of them.

FINDINGS

F1 RISK: a failure discards every turn, the 48 −ρ turns included.
- Where: gcal.py:78, 261-277, 207-208; n_sessions.py:2786-2796; the self-test asserts this behaviour at 3073-3084.
- What happens: compute keeps all 192 turns in memory. All four batches are generated first, with −ρ second, and the arrival pass runs after them. Nothing is written until compute returns.
- Any failure clears the staging folder with rmtree: a CUDA or OOM error, the raise on a non-finite arrival score, an error in write, an interrupt. A pod kill leaves an empty staging folder.
- After the −ρ batch, the realised exposure then exists only as stdout's per-turn lines. The turns cannot be read (rule 25), and a re-run adds 48 more −ρ turns (n:20, n:28, PIN-n-23, GC20).
- G-VEC's one-shot form (GC19) came from a stage whose forwards cost nothing irreversible. m's and p's G-CAL saved an atomic checkpoint after every generation (valence_core/p/gcal.py:509-538).
- Fix:
  - Append each turn to the staging folder as it is generated (one flushed JSON line).
  - On a failure, rename the staging folder to an ignored failed-run folder instead of deleting it.
  - Record a non-finite arrival as None plus a STOP instead of raising.
  - Optionally generate −ρ last.
- This consequence of GC19 is for the seat or the PI.

F2 RISK: the generation loop's history and its stop are untested.
- Where: gcal.py:143-149; self-test 412-414, 424-434.
- `step()` records len(ids), but no check reads it.
- The only eos case (428-434) puts eos at every step, so it cannot tell `break` from `continue`.
- Result: M1 and M2 survive both the laptop and the box self-test.
- Fix: a scripted step_logits that returns one-hot logits keyed on len(ids), for example the script [5, 6, eos, 9]. Assert ids == [5, 6], stop "eos", 3 calls, and call lengths n, n+1, n+2.

F3 RISK: compute's wiring of seed, TEMP and the baseline is untested.
- Where: gcal.py:265 and 280; self-test 438-469.
- The check at 465-469 is named "Welch's t against the baseline", but it tests only the coherent count and the sign.
- The seed check reads the recorded seed (row field, 270), not the seed that drove the generation.
- Result: M3, M4 and M5 survive.
- Fix: assert each steered batch's t equals welch_t(its non-None scores, the baseline's scores). Assert one baseline turn's ids equal a direct `generate(step, ids, 3, None, keys.gcal_seed(i), eos_id=eos, cap=6)`.

F4 RISK: the hurdle constants are not pinned, and each boundary is tested from one side only.
- Where: gcal.py:83-87 and 217; self-test 368-380, 481-488.
- TEMP and CAP are pinned as literals (427), but COHERENT_MIN, T_BAR, MIN_WORDS, TRIGRAM_REPEAT_MAX and DIVERSITY_MIN are not.
- The cases sit far from the bars: t ≈ 35, 35 coherent, a trigram fraction of 0.769, a diversity of 1/20.
- Departure (1)'s branch (undefined t counts as a fail) is never exercised through batch_figures.
- Result: M6–M11 survive.
- Fix: pin the literals, and add two-sided cases: 36 coherent passes; t just above 2 passes; a 4-word turn is coherent; a trigram fraction of 5/9 loops; 4/20 is low; one scored turn fails arrival.

F5 NIT: the "one place" claim is overstated for GC6.
- Where: gcal.py:14-18 and 90-105.
- "Its only caller is the (v) render" is not true: n_sessions.py:2672 calls prompt_parts on the box.
- "…and nothing else" is not true either. Under rule 13, GC7's stop belongs to the template family. The stop is wired to the chat form's end of turn in three places: gcal.py:145, ids.py:532-535 and n_sessions.py:2779-2781.
- CONVENTIONS["rendering"] and CONVENTIONS["prompts"] restate the chat form by hand. block.md's GC6 itself says the stop and the bans re-open with it.
- Fix: reword the docstring, and derive CONVENTIONS from prompt_parts("{zone}") as render_v does (ids.py:571, 576).

F6 NIT: some departures are not in gcal.py:51-54's list.
- GC2 says "the record alone", but on a STOP or PAUSE the build writes the record, the turns and dose_map.json. block.md §3 declares the turns; it does not mention dose_map.json.
- GC9 says "mirrors the adapter's (softmax, multinomial)", but the sampler is a numpy inverse-CDF draw.
- GC15 orders "the batch figures and the map", but the map is printed before the load (n_sessions.py:2753-2755).
- GC19 says "2 prompts", but the build accepts `--smoke 1..4` (2564, 2694-2696).
- Each departure is sound. Fix: list them in the docstring and the BUILD entry.

F7 NIT: rule 28(d)(c) wants the generation window declared on its own.
- Where: n_sessions.py:2742-2744, 1004-1007 and 2769.
- The generation is bounded by schema.MAX_WINDOW, which is GA-4's choice-read window. No GC reading declares a generation window.
- "longest" is computed as seq_len + cap, one more than the longest forward.
- Fix: a named generation-window declaration in the BUILD entry and the record.

F8 NIT/RISK: gcal_prompts_check does not check the steering boundary's text.
- Where: n_sessions.py:2671-2677.
- It checks text_sha256 of u+g, but neither user_sha256 against prompt_parts' user text nor v["prompt_template"]. gen_start is the render's split.
- Fix: assert both.

F9 RISK: gcal-decode does not identify the files it compared.
- Where: n_sessions.py:2875-2896.
- It prints no sha256 of gcal.json or of the turns file, and never checks gcal.json itself.
- The hurdle was decided on the box's decode, and the command does not say whether a differing decode flips any of the three flags.
- Fix: print both sha256s, and print each difference's flags under both decodes.

F10 NIT: the record omits the shift itself.
- Where: gcal.py:218-221.
- Only t is recorded, not the shift n:113 names (mean difference, the means, the SDs).
- Per-batch counts of cap hits and empty turns are not in the figures either (rule 23); they can be derived from the turns file.

F11 NIT: some malformed inputs raise errors other than SystemExit.
- n_sessions.py:2642, 2647 and 2651 sit outside the try. The handler at 2746-2749 catches SchemaError but not gcal.py:236-237's ValueError.
- None of these can be reached from a G-VEC PASS record.

F12 NIT: main()'s refusals are under-tested.
- gcal's foreign flags are tested for 4 of 9 (n_sessions.py:3209-3212 against 3262-3266); G-VEC's self-test tests all nine (2540-2545).
- gcal-decode is tested for --out only. render-ids-v's `or a.model_dir or a.ids_dir` (3322) is not tested.

SURVIVING MUTANTS

| # | File:line | Change | What would kill it |
|---|---|---|---|
| M1 | gcal.py:147 | `break` → `continue` (eos is rejected and the turn runs on) | F2's scripted logits |
| M2 | gcal.py:149 | delete `ids.append(tok)` (no step sees its own output) | F2's call-length check |
| M3 | gcal.py:265 | `rec["seed"]` → `int(rec["index"])` | F3's direct-generate equality |
| M4 | gcal.py:265 | `temp=temp` → `temp=1.0` | F3's direct-generate equality |
| M5 | gcal.py:280 | `turns["baseline"]` → `turns["+rho"]` | F3's t re-derivation |
| M6 | gcal.py:217 | `t is not None and` → `t is None or` | batch_figures with one scored turn |
| M7 | gcal.py:83 | 36 → 37 | 36 coherent passes |
| M8 | gcal.py:84 | 2.0 → 3.0 | t in (2, 3) passes |
| M9 | gcal.py:85 | 4 → 5 (or 179 `<` → `<=`) | a 4-word turn is coherent |
| M10 | gcal.py:86 | 0.5 → 0.6 | a fraction of 5/9 loops |
| M11 | gcal.py:87 | 5/20 → 4/20 | 4/20 is low |
| M12 | n_sessions.py:2595 | `injections=list(injections)` → `injections=()` (the HF step seam drops steering; untested on the laptop and the box) | an hftiny check against `a.forward(ids, injections=[inj]).logits` and the unsteered logits, or B2's smoke assertion |
| M13 | n_sessions.py:2608 | → `return Path(path).read_bytes()` (rule 27's check becomes the working copy) | `committed_bytes(REPO/"data"/"n"/"gcal"/"absent.json") is None` |
| M14 | n_sessions.py:2642 | drop `or rec["site"]["site"] != site` | of_record.site 3 with site.site 2 |
| M15 | n_sessions.py:2647 | drop `committed(dp) != db or` (or the sha256 clause; case x32 trips both) | one case for each clause |
| M16 | n_sessions.py:3266 | drop `("--pi-date", …)` (likewise --report, --ruling, --model-dir, --ids-dir) | test all nine flags |

A sampler mutant that ignores TEMP may also survive (see O4).

BOX RISKS

B1: a failed swap in the self-test's dispatch check would start the real run of record.
- Where: n_sessions.py:3223-3233 runs `main(["gcal"])` after 3177-3182 restored CUBLAS to the box's characterized value.
- It relies on the global swap of run_gcal. On the box after the commit, every precondition holds: pod id set, weights present, (v) and G-VEC committed, data/n/gcal/ absent.
- If the swap failed to take effect, the self-test would load the model, generate 48 −ρ turns and write data/n/gcal/. On the laptop the same failure is harmless, because no pod id means a refusal.
- The swap is robust as written; G-VEC uses the same pattern.
- Fix: set CUBLAS to ":16:8" around the two main() calls, or assert `cmd_gcal.__globals__ is g` first.

B2: the HF step seam and decoder are first exercised by the smoke, and the smoke asserts nothing.
- Where: n_sessions.py:2591-2600.
- The seeds are paired, so a dropped injection (M12) would make every +ρ turn byte-identical to its baseline twin, and only a read would notice.
- An end token other than the tokenizer's eos would show up only as every stop being "cap".
- Fix: the smoke asserts that some +ρ turn, or the first-step logits, differ from the baseline, and its entry reports the stop-reason counts.

B3: the box's checkout HEAD must hold all the inputs.
- Where: committed_bytes, driver_bytes and weights_of_record all use `git show HEAD:`.
- HEAD must hold this BUILD, the (v) render with MANIFEST_OF_RECORD moved, and G-VEC's committed outputs.
- A copy-in launch that does not move HEAD is refused at n_sessions.py:2634-2635. That is safe, but the refusal comes only after the WEIGHTS and DRIVER lines. This applies to the smoke too.

B4: the exit codes need care in the launch script.
- Exit 2 is both the STOP (2804) and argparse's usage error (3268, 3278, 3323). Exit 3 (PAUSE) is new, and it means the outputs were written.
- Fix: the launch script keys on the record file or the "G-CAL-n STOP/PAUSE:" lines, not on the code alone.

B5: the coherence hurdle is decided on the box's decode.
- The box decodes with transformers 5.15.0 (n_sessions.py:511); the laptop comparison runs 5.5.0 (ids.ENV_OF_RECORD).
- A difference is printed but not re-scored (F9).
- The box tokenizes nothing for inputs (A-n1 §1.1 holds); the eos id is asserted (2779-2781).

B6: the run's scale and the window.
- One invocation does up to about 15,400 uncached forwards of roughly 110 positions, plus 192 arrival forwards, and persists nothing until the end (F1).
- The window: forwards stay well inside the declared 4,096 and nothing truncates. The only window issue is F7's declaration.

OBSERVATIONS

O1: HEAD and the self-test count.
- HEAD is 99196e1, not 1185e15. It is one commit later and touches RESULTS.md and three raws.
- The spec raw and the block raw are byte-equal by blob id to the committed results/raw/2026-11-19_n-gcal_spec.md and …_n-starred-eleven_code-to-design_STOP.md.
- The five FROM files are unchanged and clean.
- I count 62 new checks on a passing run (gcal 24, keys 3, ids 19, driver 15, environment line 1), so 524 = 462 + 62 holds.
- The change adds no HF-gated check, so the box count of 535 holds.

O2: GC1–GC22, reading by reading.

| Reading | Code does it? | Notes |
|---|---|---|
| GC1 | yes | gitignore mirrors G-VEC's block; the staging folder stays ignored |
| GC2 | yes (n_sessions.py:2802-2804) | departure F6 |
| GC3, GC4 | yes (gcal.py:75-76) | |
| GC5, GC6 | yes (gcal.py:108-119; ids.py:501-602; n_sessions.py:2826-2855) | F5 |
| GC7 | yes (gcal.py:143-150) | |
| GC8 | yes (gcal.py:139, 244-249) | runner._injection's arithmetic: \|d\|·ρ of R, sign applied after |
| GC9 | yes (n_sessions.py:2591-2596) | sampler departure, O4 |
| GC10 | yes (keys.py:57-68) | |
| GC11 | yes | departure (3) is sound and declared; F4 |
| GC12 | yes | departures (1) and (2) are sound and declared; M6 |
| GC13, GC14 | yes | |
| GC15 | yes | F6 |
| GC16 | yes | the five-float file passes n_analyze.py:5453-5463 and DoseMap.problems by construction |
| GC17 | yes | F9 |
| GC18 | yes | ids.load accepts (i)-(v); (i)-(iv)'s check is byte-unchanged |
| GC19 | yes | F1, F6 |
| GC20, GC22 | n/a | process only, no code |
| GC21 | yes | O4; F2–F4 |

O3: where each starred reading sits in the build.
- GC3 and GC4: one constant each (CAP also sets the window margin and §0.4's token bound).
- GC5: prompt_parts and plan, plus the (v) re-render, which moves MANIFEST_OF_RECORD and the package digest.
- GC6: not one place (F5).
- GC8: one line, gcal.py:139. The gen_start guard can stay.
- GC11: one function plus four constants; it can be re-applied after the run.
- GC12: one function. A paired-t answer would have batch_figures pair scores by prompt, which 215 currently drops.
- G-VEC's four reach G-CAL-n only through of_record:
  - G3 and G9 flow through unchanged code.
  - G6 does not reach G-CAL-n.
  - G1's uncentred alternative moves the valence sha16 to the ALT file's row. gcal_gvec_inputs reads only row 0 of directions_L{site}.npy (n_sessions.py:2644-2652), so it would refuse, safely, until changed. The block's G1 paragraph does not name this reader.

O4: the two known departures. Both are sound.
- The sampler (gcal.py:122-128) is a correct inverse-CDF draw from softmax(logits/TEMP) in float64. It is reproducible from the logits and the seed alone, and the self-test now exercises the production sampler itself.
  - Declare it against GC9 too.
  - Caveat: the frequency check (348-356) uses a 0.12 tolerance, and on its 4-logit example softmax(lg) and softmax(lg/0.7) differ by at most 0.119. A mutant that ignores TEMP may pass, depending on default_rng(5)'s draws, which I did not compute. An exact re-derivation of the 200 draws would pin it.
- The smoke as the HF path's first run follows G-VEC's precedent. But this is the first n seam that carries an injection; see B2.

O5: the seeds are paired across batches, so prompt i's steered and baseline turns share their uniform draws (common random numbers). Welch's unpaired t is therefore conservative for them. Relevant to Q11.

O6: the arrival mean includes position 0 of a context-free forward, which is typically the high-norm attention-sink position. Its weight is 1/n_tok, so it matters most for short turns. G1 counts every token the same way. Relevant to Q11 and Q1.

O7: the baseline's coherent count binds nothing (gcal.py:281-282). Under rule 21's annotation, which is on the lock's list, the baseline is the unprovoked domain. A baseline below 36 would point at the prompt, the rendering or TEMP, not at the dose.

O8: dose_map.json carries no status, yet it is written and admitted on a STOP or PAUSE. ganl accepts any map whose formulas hold (n_analyze.py:5501-5511). The lock step should take the map only when gcal.json says pinnable.

O9: the exposure "tokens" count is emitted ids; the eos draws are not counted (≤ 80 draws per turn either way). The entry should say which count it reports.

O10: render_v could cross-check (v)'s ids against the matching prefix of any session of record that opens with the same label.

O11: when (v) lands, MANIFEST_OF_RECORD moves. The ids check "the committed data/n/ids/ is (i)-(iv)" (ids.py:1017-1027) must change, and G-VER (verify.py, which I did not read) is untested on an (i)-(v) folder.

O12: gcal-decode prints the text of any differing turn into a committed raw before the analyzer's output. n:130's ordering is GC1's lock item.

O13: the smoke's turns land outside the repository on the box. For rule 25's full read, the launch files must bring them back.

DEPARTURES
- I read valence_core/n/runner.py:270-309 (`_injection`), grepped runner.py and schema.py once for `def _injection|at_frac|with_sign|expected_alpha`, and ran `wc -l` over runner.py and primitive.py. Neither file is in the brief's named list.
- One grep of all of scripts/n_analyze.py for `class DoseMap|dose.map|dose_map` printed lines outside the --dose-map reader and DoseMap.
- The n_sessions.py diff was too large for the tool result, so the harness saved it to the session's tool-results folder (outside S and the repository). I read it there with the file-reading tool; I wrote no file myself.
- Otherwise none:
  - shasum was the only interpreter-class program, and no argv held a marker.
  - Nothing under data/mf3, ckpt or reports was touched, and no whole-tree git status was run.
  - Every git command over the tree carried the pathspec and the mf3 exclusion.
  - In S, only the named files were read.
  - Nothing was written, and nothing used the network.
```
