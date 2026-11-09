# G-TIME-OLMo (p) ×3: the seat's read, and Code's readings for the seat's word (Code → design)

*Code's raw, PI date 2026-11-09. Code STOPS here for the seat's read, in the order of the seat's answer of 2026-11-08
(`de729c4`, §4): "G-TIME-OLMo (p) ×3 on the box, batched, then the seat's read under PROPOSAL-m §3's rule (the sham
session redacted; the contrast session's forced rounds only) once for the three". Nothing follows until the seat
answers and the PI routes. Nothing is pushed.*

## 1. What ran

- **The chain, on the PI's routing of 2026-11-09** (relayed by the coordinating session; `6b63973`, item 2):
  - entry (9) flipped on `resume.Identity`, `e8779b1`;
  - G-SHAPE-p re-run, `fdd79d8` (`5009e77`'s artifact superseded);
  - G-ANL-p, `f8b16d5`;
  - LOCK-p-OLMo-{sft,dpo,instruct} v0.1, `0afd842`.
- **G-TIME-OLMo (p) ×3 on the box**, under the routing of 2026-11-08 quoted in `de729c4`'s close lines, item 2.
  - Pod `qny1x4v8padeke`, backend identifier `641ee466f4553b6a`, box repo at `0afd842`.
  - Back to back through a wrapper: sft 18:10:46Z–18:14:31Z, dpo to 18:18:16Z, instruct to 18:22:04Z. Each exited
    0, and each was one run with no `--resume`.
  - Raw: [`_p-gtime`](2026-11-09_p-gtime.txt).
- **Each checkpoint: PASS.**
  - m:302's two uncached sessions, A0-OLMo-{ckpt} (contrast) and A0s-OLMo-{ckpt} (sham), both valid and verified.
  - No hair trigger fired: m's three, and p's `line_break_in_stored_text` at 0 over every round of every session.
  - `round_degeneracy@G-TIME-OLMo-{ckpt}` is silent at 0/10, critical 2 at n = 10; `gtime_pause` is silent.
  - Register entries (1), (2) and (6)–(9) were entered in that order.
  - Each m stage report's identity carries the lock's backend identifier, `641ee466f4553b6a`.
  - Term (d) at the stage's end, before restoration, is recorded as `single_threaded: false`, with threads
    `MainThread` and `tqdm_monitor`. It is recorded, never raised, as the seat's Q4 has it (the loader's progress-bar
    thread alive after the load).

## 2. What the seat reads (m:271's pre-VERDICTS read rule; m:302)

- **The reads, one file per checkpoint** (m's `readrule`, written by m's stage):
  - [`OLMo-sft_time_reads.json`](../../data/p/reports/OLMo-sft_time_reads.json) `294361ed…408d`;
  - [`OLMo-dpo_time_reads.json`](../../data/p/reports/OLMo-dpo_time_reads.json) `b44035be…639e`;
  - [`OLMo-instruct_time_reads.json`](../../data/p/reports/OLMo-instruct_time_reads.json) `c7045474…75ad`.
- **What each holds:**
  - The contrast session as `strip_contrast` leaves it: the banner and the four forced rounds with their responses,
    each round as {phase, ri, n, text}, with no class field (ruling (h)'s G-TIME form). Its free rounds are absent.
  - The sham session as `redact_sham` leaves it: the full transcript, with the chosen config tag redacted to
    `[config]` in every free round's header. On OLMo the stored transcript carries no menu.
- **Beside them:**
  - m's pick-free stage report, `data/p/reports/OLMo-{ckpt}_time_report.json` (sft `2ccd028d…`, dpo `fb90c5a1…`,
    instruct `7f536976…`);
  - p's report on the read domain, `data/p/reports/OLMo-{ckpt}_time_p-report.json` (sft `2070c00c…`, dpo
    `1623f1cb…`, instruct `edf90bc2…`). It binds m's two files by their sha256s, and it carries `proposal_p_sha256`
    and p's four identity fields. On sft it also carries the declared SFT sentence.
- **Not read before VERDICTS:**
  - the checkpoints `data/p/ckpt/OLMo-{ckpt}_time.json`, which are -diff and may hold a contrast pick;
  - the call logs `data/p/ckpt/OLMo-{ckpt}_time_p-calls.jsonl`, which are withheld.

  Code opened neither.

## 3. The read domain, per checkpoint (the reports; the checkpoints unopened)

| | sham rounds | sham bar | pause | hair triggers | sham counters (p) | contrast forced rounds | contrast forced control chars | sham proxy | sham seconds | sham first-pick share |
|---|---|---|---|---|---|---|---|---|---|---|
| sft | 10 (4 forced, 6 free) | 0/10 | silent | 0 | all 0 | 4 generated, not excluded | 0 of 4 | 10 of 10 attributed, 0 cuts | 3.528 | 1/1 |
| dpo | 10 (4, 6) | 0/10 | silent | 0 | all 0 | 4, not excluded | 0 of 4 | 10 of 10, 0 cuts | 3.972 | 0/1 |
| instruct | 10 (4, 6) | 0/10 | silent | 0 | all 0 | 4, not excluded | 0 of 4 | 10 of 10, 0 cuts | 5.289 | 1/1 |

- **The sham sessions**, in m's stage report and the reads:
  - no exclusion, strict or tolerant, and no claim (audit, echo or lexical);
  - no advisory round, no cap hit, no degeneracy, no termination.
  - Every response stopped at a newline. In the forced rounds that came after 1 to 14 tokens: sft 2, 1, 1, 1; dpo 1,
    1, 1, 1; instruct 5, 14, 5, 1.
  - p's sham counters are `control_chars`, `harness_first_line`, `cap_hits`, `refusals` and `corrupted_spelling`
    (forced rounds), each 0.
- **The contrast sessions**, in ruling (h)'s G-TIME form:
  - only that each generated its four forced rounds and was not excluded at them;
  - and p's count of their control characters, 0 of 4.
  - Their texts are in the reads. Every other count over them is withheld to VERDICTS (p's report's `withheld`
    line).
- **Timing:** the sham seconds are m's report's. The contrast seconds are withheld (m:318). m:205's OLMo basis is
  19.5 s per session at instruct and 22.7 s at SFT/DPO (b3's figures, the model load amortized). Each stage, load
  included, took 225–228 s of wall clock (the stamps).

## 4. Code's read of the sham reads (descriptive and post-hoc, no bar; rules 11 and 23)

Code read each sham response against its task. 29 of the 30 answer it. The one that does not is sft's round 1:
"State the number of wheels on a bicycle." was answered "4". No declared counter at G-TIME covers whether a response
answers its task, so this is recorded as seen and adjudicates nothing (Q3).

## 5. Code's readings for the seat's word (each in force until ruled)

The BUILD entry's (a)–(i), verbatim from RESULTS.md at `d215d5b`, with a correction to (h); then (j), from the LOCK
entry at `0afd842`. The seat's answer at `6b63973` predates the BUILD, so none of these has been before the seat.

- (a) `contrast_forced_control_chars` lists the contrast forced rounds' control-character texts by key. This is
  F-p13 (a)'s listing; ruling (h) keeps class fields out of m's G-TIME report, though the read shows the same texts.
- (b) Q5's "over the checkpoint" is read as the seat's read domain. Every other contrast count is withheld to
  VERDICTS.
- (c) The proxy's STOP messages carry no text and no call index. The detail is in the withheld call log; Q5's "the
  entry records the exception verbatim" holds for the message.
- (d) The contrast forced rounds' cut counts are withheld too, under ruling (h)'s extension (no class field).
- (e) A p re-run on unchanged inputs is refused (write-once) where m's own reports "identical" (PIN-37). The seeded
  copy is p's file, with its two added keys.
- (f) The driver prints any STOP raised inside a session verbatim, as m's driver does. m's BOUNDARY INCIDENT message
  carries the prefix's token count, and at a contrast free round that count depends on the transcript, picks
  included. It is the one STOP text p can print that carries contrast information: inherited, unchanged, flagged.
- (g) m's own G-TIME report and reads, written under `data/p/reports`, keep m's form, with no `proposal_p_sha256`.
  F-p8's "every p artifact" is read as p's own artifacts. p's report binds m's two files by their sha256s and carries
  `proposal_p_sha256`.
- (h) The backend identifier of record is the lock's one `BACKEND OF RECORD` line. A box change before the lock means
  writing the lock with the new box's identifier, with no code edit. A box change after the lock STOPs the stage
  before it generates. m:302 has a new `BACKEND` entry supersede the lock's field. p reads no superseding record yet,
  so its form, a lock re-issue or a declared record, is the seat's to route.
  - **Correction (2026-11-09; the LOCK-p v0.1 values-check, item #17).** "A box change after the lock STOPs the stage"
    overstates it. The stage compares the adapter's backend identifier with the lock's line. A new box of the same
    class gives the same identifier (m:267: "the backend identifier cannot tell two boxes of one class apart"), so
    only a *backend* change STOPs the stage. The three locks say so (§0). The stage's PIN (`stage.py:36-38`) still
    reads "a box change" and is left as written until a package move the seat rules.
- (i) The STOP rule's reach. Every SystemExit that ends a run once its run line is written makes the stage STOPPED,
  m's refusals inside m's stage included. That extends m's "a resume never lifts a STOP" to cases m would let re-run
  once the cause is fixed. The way out is the seat's ruling. A restart needs the call log, the marker and m's
  checkpoint moved aside by hand, as m's PIN-37 has it. No adjudication input is defined, and a ruling to resume has
  no path in this build.
- (j) **G-SHAPE-p's drift check depends on the calling process.** `stage.gshape_drift_problems` (the fix of round 2's
  MINOR m-3 in step 6's BUILD review) compares G-SHAPE-p's recorded import closure with `gshape.import_closure`. That
  function reads the `valence_core` modules loaded in the calling process, outside `valence_core/p` and
  `valence_core/m`.
  - In the stage's own process the closure is the recorded 14 files. The driver's `time` runs the precheck first, with
    the same module-level imports as G-SHAPE-p's run. Code re-checked this on the box before the launch: 14 files,
    equal.
  - A process that has loaded another such module sees drift that is not there. Code's lock generator imported
    `m_analyze`, which loads `valence_core/e2d/habit.py`, and was refused on its first try. It now computes every
    `lock_required` before importing `m_analyze`.
  - m's analyzer closure is computed in a fresh interpreter (PIN-1). Code's proposed fix is a fresh-interpreter
    closure for p's check. That would move p's package, so nothing is changed before the seat's word.

## 6. Questions for the seat

- **Q1. The read.** On the seat's read of the three reads files, do G-TIME-OLMo (p)'s three PASSes stand (m:302: "a
  fire → STOP, a pause → the seat's adjudication, before that checkpoint's qualification")?
- **Q2. LOCK-p v0.2 ×3.** m:302 has LOCK v0.2 carry "acceptance; projections", with port acceptance recorded at
  v0.2. Code asks for LOCK-p v0.2's contents in p's terms:
  - which acceptance it records;
  - which per-session basis its projections use: m:205's 19.5 s and 22.7 s, or these sessions' measured sham seconds
    (3.528, 3.972 and 5.289 s; one sham session each; contrast seconds withheld).
  Code computes the projections by m's rule at whatever basis the seat names.
- **Q3. A correctness counter (rule 23)?** Whether the seat wants §4's observation made a pre-declared descriptive
  counter from G-F0m-OLMo (p) on, over the sham sessions and recomputable from the records, or wants nothing.
- **Q4. (a)–(j).** The ten readings, as listed, for the seat's word; and (j)'s fix, now or at the next package move.

*Committed with the outputs it describes (rule 27). The pod stays up and idle: the routing kept it up through LOCK-p
v0.1, and whether it stays up through LOCK-p v0.2 and G-F0m-OLMo (p) is the PI's call. Nothing is pushed.*
