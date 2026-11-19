# n — a supplement to the eleven starred readings: G-CAL-n's GC23, three notes on Q1 and Q11 from G-CAL-n's review, and three items for LOCK-n v0.1's list (code → design)

*The n-build session (Code), PI date 2026-11-19. For the PI to route, in the same sitting as the eleven (`99196e1`).*

*Where things stand. No lock is in force.*
- *The eleven starred readings are committed at `99196e1`: E: is
  `results/raw/2026-11-19_n-starred-eleven_code-to-design_STOP.md`, and S: is G-CAL-n's spec raw,
  `results/raw/2026-11-19_n-gcal_spec.md`, committed beside it.*
- *G-VEC is built at `da7bdec` and has not run. Its launch files are drafted in Code's scratch and held until the PI
  answers on its run order.*
- *G-CAL-n's draft 1 had one blind review, which found no BUG. Its findings are applied in Code's later drafts. One of
  them, F1, became Code's reading GC23. The coordinating session routed GC23 as a PIN declared in G-CAL-n's BUILD
  entry, to go to the seat before G-CAL-n's run; §5 quotes that routing. G-CAL-n's build is in Code's scratch, not
  committed. The files this supplement cites as built are its draft 3: `valence_core/n/gcal.py` (`aba3700c…a3a0`) and
  `scripts/n_sessions.py` (`37b8268d…f030`).*

*Sources:*
- *PROPOSAL-n v0.2 (`PROPOSAL-n-bk-reconciliation-v0_2.md`, cited n:line);*
- *ADDENDUM-n1 v0.1 (`ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md`, cited A-n1 §);*
- *CLAUDE.md (C:line);*
- *the code at `99196e1` (file:line), and G-CAL-n's build by name, as above;*
- *G-CAL-n's review of draft 1 (sha256 `75d4200f…cd5e`), which goes into the repository with G-CAL-n's BUILD.*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules each one; Code adjudicates none.*

## 0. The short form

- **Q12, one more reading before G-CAL-n's run: GC23.** A failed run keeps the turns it generated, and the batches are
  generated −ρ last. The order, (d), is the one part that touches n:113's words. It is one line, which a ruling flips
  back, with the self-test's pin of the order changed to match.
- **Three notes from the review bear on Q1 and Q11** (§2). They are what an answer against G1's centring costs G-CAL-n,
  and two properties of the arrival hurdle's form.
- **Three items for LOCK-n v0.1's list** (§3).
- **The dependencies** are E §3's, with Q12 added: G-CAL-n's run waits for all twelve answers.

## 1. GC23: a failed run keeps its turns, and −ρ is generated last (Q12)

**The finding** (the review's F1, RISK, on draft 1):
- G-CAL-n held all 192 turns in memory until its end.
- Any failure raised once the staging folder was made, after the load and its checks, removed it: a CUDA or memory
  error, the non-finite-arrival raise, an error in writing, or an interrupt. A pod kill left it in place, empty.
- The −ρ turns generated before such a failure would be lost to the seat's read (rule 25, C:348–349), and §0.4's count
  of them (n:20: "48 turns at −ρ (≤ 80 tokens each)") would rest on stdout's per-turn lines alone.
- A re-run, which GC19 allows only on the seat's word (S:59), would add up to 48 more.
- m's and p's G-CAL wrote a checkpoint after every generation (valence_core/m/gcal.py:1152–1174;
  valence_core/p/gcal.py:509–538).

**The reading, GC23,** in four parts. G-CAL-n stays one shot under GC19: a new out folder, no resume, a re-run only on
the seat's word.
- **(a)** Each turn is appended to the staging folder's log, `gcal_turns.partial.jsonl`, as soon as it is generated: one
  JSON line, flushed and fsynced before the next turn starts. The log is removed only on a clean end, once the record,
  the turns and the dose map are written.
- **(b)** On any failure raised after the staging folder is made, the folder is renamed to the failed-run folder and
  never removed. On a run of record that is `data/n/.gcal.failed`, which git ignores. A hard stop that skips the
  handler, such as a pod kill, leaves the staging folder in place, with its log. A later run refuses, before the load,
  while either folder exists.
- **(c)** A non-finite arrival score stays a failure, a raise after every turn is generated; (b) keeps all its turns.
- **(d)** The batches are generated in the order +ρ, +ρ/2, the baseline, then −ρ, so that a failure in another batch
  spends no −ρ turn. The record and the turns file keep the build's order of record: n:113's ("48 conditioning turns
  generated under steering at +ρ, −ρ and +ρ/2", n:113), then the baseline. n:113 names the baseline in its arrival
  clause, so its place last is the build's reading. Each turn's seed fixes its draws, so the order changes no turn's
  inputs.

**(d)'s text, as built,** is one line in `valence_core/n/gcal.py`:
`GENERATION_ORDER = ("+rho", "+rho/2", "baseline", "-rho")`. The record carries it as `constants.generation_order`.

**What another answer would change:**
- Striking (a)–(c) restores draft 1's form: a failure leaves no turn on disk, and any −ρ turns it had generated are lost
  to the read, their count left to stdout's per-turn lines.
- The review's own form of (c), in place of the raise: a non-finite arrival recorded as None, and the stage a STOP. The
  record, the turns and the dose map would then be written, and the seat would read the failure as a STOP. As built,
  the seat gets only the failed-run folder, whose log holds all 192 turns, each with its arrival not yet scored.
- Flipping (d) sets that one line to the order of record, `("+rho", "-rho", "+rho/2", "baseline")`, together with the
  self-test's pin of the order and the docstring's sentence; the record's `constants.generation_order` follows the
  line. Nothing else changes. A failure in +ρ/2 or in the baseline would then come after the 48 −ρ turns were spent.
  Ruled after G-CAL-n's BUILD commit, a flip is a code change, a self-test run in its own window and a commit, and it
  moves the n package's digest, which G-CAL-n's launch files hash.
- After a failure, with (a)–(c) standing and under either answer on (d):
  - G-CAL-n's launch files, not yet drafted, are to bring back by hash whichever folder the run left: the failed-run
    folder, or the staging folder after a hard stop;
  - its turns are then read and counted against §0.4's exposure, and the seat rules on a re-run (GC19);
  - a re-run also needs that folder moved aside on the box first, on the seat's word;
  - the kept turns carry no arrival score. Any score after a failure is a re-computation from the recorded ids, which
    adds no generation (E:229–230);
  - how those turns are kept in the repository is not built; it is the seat's.

## 2. Notes on Q1 and Q11, from the review

- **O3, on Q1 (G1's centring clause).** G-VEC stores the uncentred valence direction in its ALT file, as the
  `valence_uncentred` row of `directions_alt_L{i}.npy` (valence_core/n/gvec.py:92, 352). If the seat strikes the
  centring, the valence direction of record moves to that row, and its sha16 with it (E:70–73).
  - G-CAL-n's reader of G-VEC's outputs, `gcal_gvec_inputs` in scripts/n_sessions.py as built, reads only row 0 of
    `directions_L{site}.npy` and checks that row against of_record's sha16.
  - So G-CAL-n would refuse, safely, until that reader is changed and re-tested.
  - E's G1 paragraph does not name this reader.
- **O5, on Q11 (GC12's arrival form).** Prompt i's steered and baseline turns share seed_i, so their draws share their
  uniforms (common random numbers).
  - Where the paired scores correlate positively, Welch's unpaired t overstates the standard error of the difference,
    and |t| ≥ 2 is a stricter bar than its nominal one.
  - A paired t is the alternative (the review's O3, on GC12), over the prompts scored on both sides: a turn with no
    arrival score drops its pair. batch_figures would then keep each score's prompt, which it now drops.
- **O6, on Q11 and Q1.** A turn's arrival score is the mean over every position of an unsteered forward over its
  emitted ids alone.
  - So position 0, typically the high-norm attention-sink position, is in every mean, with weight 1/n_tok, and so
    weighs most in short turns.
  - G-VEC's capture counts every token the same way (G1: "every token counts in the passage mean and in R").

## 3. For LOCK-n v0.1's list

- **O7.** The baseline's coherent count is recorded and binds nothing. Rule 21's annotation (C:338–341) is already on
  the list (E §3, against GC2). Under it the baseline is the unprovoked domain: a baseline below 36 coherent would point
  at the prompt, the rendering or TEMP, not at the dose.
- **O8.** `dose_map.json` carries no status, and it is written on a STOP or a PAUSE too.
  - `ganl --dose-map` accepts any map whose formulas hold (scripts/n_analyze.py:5500–5511).
  - Its input check takes exactly the five keys (scripts/n_analyze.py:5453–5463), so a status field in the map would
    make ganl refuse it.
  - The lock should take the map only where gcal.json says pinnable, which is a PASS.
- **O12.** `gcal-decode`, the laptop's one decode comparison (A-n1 §1.4), prints each differing turn's two decodes. Its
  raw therefore carries turn text before the analyzer's output exists. When the seat reads the turns (GC1, S:37, on the
  list; n:130) bears on where that raw goes, and when.

## 4. The question for the seat

- **Q12 (GC23).** Do GC23's (a)–(c) stand: each turn persisted as it is generated; a failed run's staging folder kept
  as the failed-run folder; and a non-finite arrival a failure whose turns are kept, or, in the review's form, a None
  and a STOP? And is (d) the order of generation, −ρ last with the record in the order of record, or does generation
  follow the order of record (the one line, with its pin)?

## 5. The coordinating session's routing of GC23, verbatim

As Code received it. Its "draft 2" became draft 3 by the coordinating session's next message, whose line on GC23
follows it.

```text
Routing on F1/GC23:
- Build (a)–(d) in draft 2 as GC23, a PIN declared in G-CAL-n's BUILD entry.
  - (a)–(c) keep G-CAL-n one shot under GC19 and only stop a failure from destroying turns that rule 25 and §0.4's count need. That's the conservative form, with m's and p's G-CAL as precedent.
  - (d) is the one that touches n:113's wording, so keep it to a single ordering line that a ruling can flip back.
- Yes, GC23 goes to the seat before G-CAL-n's run. Draft a short supplement to 99196e1 for the same sitting, `…_n-starred-eleven-supplement_code-to-design_STOP.md` or your name for it, holding:
  - Q12, GC23 (a)–(d), with (d)'s text and what flipping it changes;
  - notes on Q1 and Q11 from the review: O3 (the uncentred alternative moves the valence row to the ALT file, which gcal_gvec_inputs doesn't read, so G-CAL-n refuses until it's changed), O5 (paired seeds make Welch's t conservative) and O6 (position 0 in the arrival mean);
  - for LOCK-n v0.1's list: O7, O8 and O12.
  Give it one values-check pass, then ask me for a commit window. It can land before G-CAL-n's BUILD. The PI's nudge to the seat should then cover both blocks, and I'm telling the PI to wait for it.
- B3, B4 and O13 go to G-CAL-n's launch files, later.
- G-VEC: agreed, no change for the B1 pattern; its self-test's dispatch check covers it.
- The reviewer's three departures go in G-CAL-n's BUILD entry.
```

```text
My routing of F1 is in your queue: build (a)–(d) as GC23 in draft 3, and send a Q12 supplement to the seat. Draft 3 gets its own window.
```
