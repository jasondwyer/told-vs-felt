# n step 4 — the BACKEND extension's smoke on n's box paused on n §2.1's fidelity rule (code → design)

*The n-build session (Code), PI date 2026-11-18. For the PI to route.*

*What ran. The step-4 box check v2, run by the pod session on n's box: pod `emw1e4embiwe9b`, the H100 SXM of the
BACKEND entry `d5d08fa`. No lock was in force: LOCK-n v0.1, which is to name this backend (the box answers of
2026-11-18, §2 item 7), is not placed.*
- *The driver was `scripts/n_sessions.py` v2d (`18f19b8e…4f5c`), uncommitted. The order is the coordinating
  session's: the box smoke, then the driver's commit, then the run of record from the commit.*
- *The package was HEAD `d5d08fa`'s `valence_core/n/` (`f927608c…3c03`, committed at `b523f6a`).*
- *The box script ran steps 0–3 (the copy, the manifest, the self-test, the hashes), then a smoke of **two reads
  only**, which is never of record.*

*Sources read, by sha256:*
- *the box's output `bext_box_v2_out.txt` (`202e6bd7…a872`) and the pod session's run record `bext2_box_run.txt`
  (`7933fb33…2590`), each in full; both are committed beside this raw;*
- *the box's `hashes.txt` (`93783db0…7b36`), compared by `diff` with the laptop's;*
- *the smoke's report `smoke-report.json` (`206264c8…bb9a`): its key names, `pauses`, `end_state` and
  `stage_identity.fidelity_rule`, and nothing else;*
- *the driver v2d (`18f19b8e…4f5c`), and, at `b523f6a`, `valence_core/n/runner.py` (`69d73d77…d896`), `schema.py`
  (`0ea39600…0db6`) and `primitive.py` (`7e7bb0a0…0b0c`);*
- *`PROPOSAL-n-bk-reconciliation-v0_2.md` (`30a3d0f5…04f4`) :47, :77, :109 and :130;*
- *the seat's answers of 2026-11-18: on the box (`f46815fb…6d5a`), §2 items 3, 4, 5 and 7; on the corpus
  (`5843a9bd…7165`), §5.5;*
- *the n package's BUILD entry (`83a50a0`): its flags for the seat;*
- *the box block of 2026-11-17 (`80b7cacf…2fc8`), §1 item 1, and the A100 check's output of 2026-11-16, its lines
  43–51 (`e2d9774c…831f`, in Code's scratch, uncommitted);*
- *`WORKFLOW.md` (`e7195706…b061`), §4.*

*Not opened: the smoke's root, which holds its records and captures (never copied, listed or read); anything under
`data/mf3`, `data/*/ckpt` or `data/*/reports`.*

## 0. The short form

- **Steps 0–3 held:**
  - the copy at `d5d08fa`, with exactly the driver changed;
  - the manifest, 23/23;
  - the self-test, 344/344;
  - the package `f927608c…3c03` and the 11 closure lines, equal to the laptop's by `diff`.
- **The smoke ran its two reads and stopped at the stage's own monitor:**
  - R6's bridge, as retargeted, held on its first run: n's identifier `8264f719efd347a9` under the 4,096-token window,
    and the characterization's `4ed3f2c70fe8afbf` under the default window. On the A100 on 2026-11-16, R6's check
    against `641ee466f4553b6a` refused before the load, with CUDA unavailable (§4);
  - G-VER PASS; the weights loaded;
  - read 0 (BK run 0): fid 0.014660, at or below TAU, about 0.82 × TAU;
  - read 1 (BK run 5): fid 0.086070, above TAU (0.0178835444), about 4.8 × TAU;
  - the fidelity binomial's end-of-run evaluation fired under p0 = 0/2400, and the stage PAUSED (`p01`). So there was
    no discordance distribution and no comparison.
- **The box script's last line reads FAIL, on the smoke's exit 1.** That is reported here, not decided.
- **This is the extension's first run with reads on any box** (§4). It is two reads only, and never of record.
- **The questions.** Q1 asks how step 4's run of record proceeds; Q2 asks whether the driver's commit may go on this
  smoke (§7). **Code adjudicates nothing.**

## 1. The reads the seat needs (m:271's form)

- **This raw,** in full.
- **The box's output,** committed as `results/raw/2026-11-18_n-step4_bext-box2_out.txt`, in full.
  - Under n's blinding (n :130), stdout prints "session index, arm, dose, the fidelity value against TAU, timing —
    never a margin".
  - The run holds no pick and no contrast session.
  - So nothing in it is redacted or stripped.
- **The pod session's run record,** committed as `results/raw/2026-11-18_n-step4_bext-box2_run.txt`, in full.
- **For §4:** the box block of 2026-11-17, §1 item 1, committed at `e48c7d0`.
- **Not for reading.** The smoke's report stays out of the tree, as a smoke is never of record (its sha256 is above).
  Its pause record and fidelity rule are quoted in §3. Nothing from the smoke's root is read.

## 2. The smoke's lines, verbatim

These are lines 47–63 of the box's output. The scrub found nothing to remove:
- The whole output was scanned for the laptop's paths, session ids, the PI's user name and any IPv4 address. None
  was found.
- The progress bar's line carries carriage returns, so it is abbreviated in brackets.
- Nothing else is changed.

```text
== 4 the smoke (2 reads; never of record)
SMOKE: 2 of the 24 reads and 2 floor sessions, outside the repository; never of record
WEIGHTS: allenai/OLMo-2-0325-32B-Instruct revision b96024342a77, files_aggregate_sha256 36f05404dc39ec1759e711f560dc41dcb155f10c0230b671ded9b597fc830fdb; 22 files at /workspace/models/olmo2_instruct, each at the manifest's byte count (the full re-hash is respawn step (i))
DRIVER scripts/n_sessions.py 18f19b8e7a49f1ddacacfb286938431f56a9f8f5534b38fcc9d4d9db8a1b4f5c: a smoke's, not HEAD's committed bytes (unchecked)
G-VER (the BACKEND extension's start; ADDENDUM-n1 §1.3):
{"first_problems": [], "ids_ok": 160, "labels_kept": 4, "labels_ok": 4, "manifest_ok": true, "n4_ok": 160, "sessions": 160, "spans_ok": 160, "status": "PASS"}
[Loading weights: the progress bar, 707/707]
[transformers] Calling `crop` with a positive value is deprecated and will be removed in version 5.18. Please use a negative integer to remove that number of tokens from the cache instead.
backend: n's identifier 8264f719efd347a9 (window 4096); the characterization's 4ed3f2c70fe8afbf under the default window (R6); pod emw1e4embiwe9b; load 12722 ms
read 0 s=0 N1-V none 0 fid=0.014660 <= TAU ms=973
read 1 s=5 N1-V none 0 fid=0.086070 > TAU ms=712
PAUSE fidelity-binomial at the run's end
end PAUSE: 2/2 reads; report smoke-report.json
BACKEND extension: PAUSE; no distribution and no comparison until it completes
smoke exit=1
smoke identity: its package and closure lines equal step 3's
bext box v2 FAIL: copy OK, manifest OK, selftest exit=0, hashes exit=0, smoke exit=1, smoke identity 0
```

In a read line, `s=` is the session's BK run index (`bk_run`), and the next three fields are the arm, the direction
and the dose.

## 3. What fid measures, TAU's source, and the rule that fired

- **What fid measures here.**
  - Each read is computed twice over the same token ids: once by the 5(f) primitive's cached path, and once by a
    fresh full forward for each label.
  - `primitive.py`'s docstring quotes the pair from BK's `prereg.precondition_cache`: "the
    prefill-plus-cached-continuation margin against a fresh full forward over the identical ids under the identical
    additive mask".
  - `fid` is `rel`, from `schema.fidelity_numbers` ("exactly as both sides compute them"): |margin − fresh_margin| /
    max(|logprob_S|, |logprob_U|). It is the cached-versus-fresh discordance as a fraction of the read's scale.
  - `exceeds_tau` is `rel` > TAU.
  - These reads are at d = 0, with nothing injected (R4).
- **TAU's source, n §2.1 (:77), verbatim:** "**Fidelity (B2):** at d ∈ {0, +1, −1} every read is re-computed from a
  fresh cache construction (and on a 10% keyed sample of the other points, `n-fid|{s}`); |cached − fresh| is
  adjudicated by BK's frozen scale-relative criterion, TAU = 0.0178835444 of the read's scale (the scale as
  `analysis.json`'s `prereg.precondition_cache` defines it; BK's own reads: median 0.031 nats, maximum 0.125, 23.9%
  above 0.05 nats, at a mean scale of 11.15 nats [C]); the class binds by exact binomial against p0 declared in LOCK
  v0.1 from BK's measured rate at TAU on the 160 sessions (G-DATA (vi)), cadence every 160 reads; a fire pauses and
  the seat adjudicates (rule 21); the primary analysis is ungated, a sensitivity row drops reads above TAU/4."
- **B2's row of n §0.10's table (:47), verbatim:** "§2.1: fidelity adjudicated by BK's frozen scale-relative criterion TAU
  = 0.0178835444 per read (the scale as `analysis.json` defines it, extracted at G-DATA (vi)); the class binds by
  exact binomial against p0 = BK's measured per-read rate at TAU on the 160 neutral sessions (G-DATA (vi); declared
  in LOCK v0.1), cadence every 160 reads; a fire pauses and adjudicates, never STOPs an arm; the primary is reported
  ungated with a sensitivity row at TAU/4, as BK report theirs; the d = 0 identity bound is the backend's measured
  nondeterminism; ledger (51)".
- **The rule as the driver carries it.**
  - The stage identity's `fidelity_rule`, as the smoke's report holds it, verbatim:
    `{"cadence":160,"p0_count":0,"p0_n":2400,"sample_key":"n-fid|{s}","sample_rule":"every read is at d = 0 and re-computed (dose-rule); no sample","tau":0.017883544377937845}`.
  - The driver's self-test pins it as "the fidelity rule n §2.1's with G-DATA (vi)'s p0".
- **R5's p0 = 0 rule.**
  - The driver's reading R5, verbatim: "R5 no cap; the binomial's alpha ``BEXT_ALPHA`` (at p0 = 0 any exceedance
    fires whatever alpha is)".
  - The runner's PIN, for any stage: "``p0 = 0`` makes any exceedance fire at the next evaluation (rule 21's
    zero-base-rate form)."
- **Why it evaluated at all.**
  - The cadence is 160 reads and this stage has 24, so the binomial never reaches a cadence point.
  - It fired at the runner's end-of-run evaluation. Its PIN, verbatim: "When no read remains to launch (the plan
    done, or the cap spent), a batch with trials since its last evaluation is evaluated once more: the end-of-run
    evaluation, whose fire has no read."
  - That evaluation is one of the n package's open flags for the seat (§6).
- **The pause record,** the smoke report's `pauses`, verbatim:
  `[{"adjudicated":false,"also_fired":[],"arms_in_scope":["N1-V"],"binomial":{"alpha":0.01,"first_launch_index":0,"k":1,"last_launch_index":1,"n":2,"p0_count":0,"p0_n":2400},"kind":"fidelity-binomial","launch_index":null,"pause_id":"p01","read_id":null,"resumed_at_launch_index":null,"ruling_sha256":null}]`.
  Its `end_state` is "PAUSE".
- **What waits.**
  - The discordance distribution, the in-band count and ADDENDUM-n1 §2's comparison (the counts and the medians)
    print only on COMPLETE.
  - The driver's docstring: "a PAUSE ends the invocation with the report (the seat adjudicates; ``--resume`` with
    ``--ruling PAUSE_ID=PATH`` continues, skip-only)."

## 4. The extension's first run with reads on any box

- **2026-11-16, the A100 pod `m43y3deb1gq3rp`.**
  - The v1 box check's smoke refused before the load, at R6, with CUDA unavailable (error 802). There was no G-VER,
    no load and no read.
  - The box block of 2026-11-17 reports it (§1 item 1, committed at `e48c7d0`).
  - That output's line 48, verbatim: "before the load: the environment's provenance under the default window hashes
    to bcb9d44161b4a3d0, not the characterization's 641ee466f4553b6a (R6)".
  - The A100 has run nothing for n since.
- **2026-11-18, the H100.**
  - The smoke above is the first run, on any box, of the extension's reads, and the first in which R6's bridge held
    (on the A100 it ran before the load and refused).
  - The pod session's run record (its line 72) reads "R6's bridge held on hardware, its first run there"; R6 had run
    on the A100 and refused (above).
  - No other measurement of n's cached-versus-fresh discordance on the model's weights exists, on any GPU.

## 5. The seat's own sentence on numerics off BK's box

The corpus answers of 2026-11-18, §5.5, verbatim: "The reason is the box raw's: on a Hopper box, and on any box but
BK's, the forward's numerics differ from theirs by an amount the tolerance of §2 may not cover, and a zero match count
then says nothing about the convention; the medians separate a convention that is wrong by nats from one that is right
to within hardware."

The sentence was written for ADDENDUM-n1 §2's label-convention check; the box answers' §2 item 4 cite it so. The rule
that fired here is n §2.1's fidelity rule, with BK's TAU and G-DATA (vi)'s p0.

## 6. Items Code declares, without adjudicating

- **Readings.** R1–R6 stand as the driver's docstring states them; this smoke changes none.
  - R5 declares the binomial's alpha, which does not matter here: at p0 = 0 one exceedance fires whatever alpha is
    (§3).
  - R6 was retargeted by the box answers' §2 item 4, and it held.
- **p0 before the lock.**
  - n §2.1 has p0 "declared in LOCK v0.1 from BK's measured rate at TAU on the 160 sessions (G-DATA (vi))".
  - No lock is placed, so the driver carries G-DATA (vi)'s figure, 0 of 2,400, directly. The self-test pins it (§3).
- **The end-of-run evaluation, an open flag.**
  - The n package's BUILD entry (`83a50a0`) lists it among its flags for the seat, of which it says: "Each is Code's
    interim reading. By the PI's routing of 2026-11-16 (N.9), the build proceeds on them."
  - The flag, verbatim: "**The fidelity binomial.** It is counted in batches that a ruling clears, and evaluated every
    160 reads at the next re-computation, with an end-of-run evaluation."
  - None of the seat's answers since the BUILD names it.
  - It is the evaluation that fired here (§3).
- **Departures,** with their class. Both happened on the laptop, before the box run.
  - *Guard-marker argv, read-only, model-free.* While Code built the v2 box manifest, one `sed` call carried the
    model folder's name in its argv. It was disclosed at the time.
  - *A battery window used for newer bytes, disclosed at the time.* The window granted for v2c's laptop self-test ran
    v2d, which had the delta review's fixes applied. That run gave 332/333, because its overlay lacked the two
    committed files the new provenance check reads. A second run, from the completed overlay, gave 333/333.

## 7. Questions

**Q1. How does step 4's run of record proceed?**

*The readings to weigh:*
- **The run would likely repeat the pause.** The smoke's two reads are the run's first two (the smoke runs
  `bext_plan(ss)[:smoke]`). Respawn (ii) passed on the box's own determinism, "A, B and C exact at 0.0" (`d5d08fa`),
  against the seat's criterion "A, B and C exact on repetition within the box" (the box answers' §2 item 3). If the
  reads repeat as A, B and C did, the run of record's read 1 exceeds TAU again, and under the rule as it stands the
  run PAUSES at its end.
- **The rule gates the very thing the extension measures.** n §3 G-ACQ (:109): "the fresh-versus-cached discordance
  distribution over 24 reads (§2.1's identity bound)".
- **p0 = 0 is BK's rate on BK's hardware** (§3). §5.5 expects this box's forward to differ from BK's published
  values; that is the label check's measure, not the within-box cached-versus-fresh rate the fidelity rule binds (§5).
- **The values are thin.** They are 0.82 × TAU and 4.8 × TAU, from two reads only.
- **At 24 reads, the binomial can fire only at its end-of-run evaluation,** and that is an open flag (§6).

*The options as Code sees them:*
- **(a) Run as pre-registered.** Commit the driver, run the 24 reads and let the stage pause at its end. The seat
  then rules on that pause with every read's fidelity value in hand from stdout (one line per read, rel to six
  decimals against TAU), beside the report's per-cell fidelity counters (trials, exceedances at TAU and at TAU/4). A
  resume with the ruling completes, skip-only, and prints the distribution, the in-band count and the comparison.
- **(b) Amend the extension's fidelity rule first:** for example, make it descriptive at this stage, or drop the
  evaluation short of the cadence. That means a new driver version, its self-test, a review and a new box check.
- **(c) Run a diagnostic first:** for example, find which of the two paths moves on this box, with the kernel path
  recorded.

*Code's recommendation, not a ruling:* (a). Every read's fid value reaches the seat in stdout before any ruling,
without changing the rule; the distribution in nats, the in-band count and the comparison print on the resume. It
costs the run and, after the ruling, a resume, each with one load (the smoke's took 12,722 ms; its reads 973 and
712 ms).

**Q2. May the driver's commit go on this smoke?**

*The readings to weigh:*
- **The order.** The coordinating session's order is "the box smoke first, then the driver's commit window, then the
  run of record from the commit". The box script counts a smoke exit 0 as its pass.
- **What the smoke did.** It exited 1 on the stage's own pause. Every step before the monitor ran as expected, and
  its identity lines equal the laptop's.
- **What a re-run would do.** Under the rule as it stands, if the box repeats, no smoke of two or more reads (the box
  script runs `--smoke 2`) exits 0 on this box.
- **The box answers' §2 item 5.** The driver is "committed by path before step 4's run of record, the entry saying
  so".

## 8. Not questions

Code's reading of what needs no ruling; the seat may take any of them up.

- **R6 and the re-pin.** The bridge held on hardware. The box's characterization stands as `d5d08fa` recorded it.
- **The self-tests and the hashes.** 333/333 on the laptop and 344/344 at the box; the package and the closure are
  equal by `diff`.
- **The transformers notice on `crop`.** It comes from the HF backend's `cache.crop(n)` (`primitive.py` :341), which
  cuts the cache back to the prefill's length after each label's continuation (a one-token label needs none). The
  primitive asserts that length after each crop (:342–343), and nothing refused.
- **The two fid values.** They are data from two reads only, never of record, and no verdict rests on them.
- **The pod session's copy.** Its first copy script stopped at its own hash check, before any file reached the
  destination. A corrected script made the copy, and the run was not touched (its run record, item 8).

## 9. The record

- **This raw:** `results/raw/2026-11-18_n-step4-smoke-pause_code-to-design_STOP.md`.
- **The H100 check:**
  - `results/raw/2026-11-18_n-step4_bext-box2_out.txt` (`202e6bd7…a872`, 63 lines), the box's stdout and stderr as
    the pod session copied it, unedited;
  - `…_run.txt` (`7933fb33…2590`, 106 lines), the pod session's record of the run.
- **The box files,** frozen in Code's scratch:
  - `bext_drafts_v2.tar` (`f0bc9dac…3b0a`), one member, v2d;
  - `bext_manifest_v2.txt` (`18b4c619…c986`), 23 lines;
  - `bext_box_v2.sh` (`2bde09d9…af51`), 95 lines.
- **Not committed:** the driver. **Nothing is pushed.**
