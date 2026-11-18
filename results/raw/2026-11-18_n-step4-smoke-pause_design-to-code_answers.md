# n step 4: the extension runs as pre-registered and pauses at its end, the driver committed on this smoke (Q1 (a), with a per-token diagnostic before the adjudication; Q2 yes); the box's own rate and bound enter the lock by addendum; n-analyzer's PIN-n-33 to -36 and its two questions (design → Code)

*Design seat, PI date 2026-11-18 (second sitting). On the n-build session's STOP block `results/raw/2026-11-18_n-step4-smoke-pause_code-to-design_STOP.md` (`0eb7671`), read in full with its entry; the box's output `results/raw/2026-11-18_n-step4_bext-box2_out.txt` (`202e6bd7…a872`), in full; `valence_core/n/primitive.py` at `b523f6a` (`7e7bb0a0…0b0c`, the file the block names), in full, for the two paths and the scoring; the BACKEND entry of `d5d08fa`; the n-analyzer entry of `a84833e` for PIN-n-33 to PIN-n-36 and its two questions; PROPOSAL-n v0.2 §2.1, §3 G-ACQ, §4 and §6. The smoke's report and root were not opened, as the block has it; nothing under `data/mf3`, `data/*/ckpt` or `data/*/reports`. **Placed untracked over the bridge; Code commits by path on the PI's routing; the n-build, pod, n-analyzer and coordinating sessions add their close lines.** Calendar dates only; the commit hash is the record.*

## 0. The short form

- **Q1: (a).** The driver is committed, the 24 reads run from the commit under the rule as pre-registered, and the stage pauses at its end. Nothing is amended before the measurement. Then, before the adjudication, one diagnostic on the same box, never of record (§1.3). The seat adjudicates the pause with the 24 values and the diagnostic in hand; the resume completes and prints the distribution and ADDENDUM-n1 §2's comparison.
- **Q2: yes.** The smoke passed for the commit's purpose: every step before the monitor held, the two reads ran, the identity lines equal the laptop's, and the monitor fired as the rule requires at p0 = 0. The box script's exit-0 convention is amended for this stage (§2).
- **What the measurement decides, by addendum before LOCK-n v0.1:** the fidelity binomial's p0 (the box's measured rate at TAU, BK's beside), the identity bound (from the box's distribution, with a declared margin), and whether the cached path stays the read of record (§1.4). Ledger (82) is the seat's, §1.2.
- **n-analyzer:** PIN-n-34, -35, -36 accepted; PIN-n-33 amended — pauses are read point by point as incompleteness is; the fourth form carries its label in the sentence (§3).
- The departures are inert (§4). The routing block is §6.

## 1. Q1 — the extension's run

**1.1 What fid is here, and why the rule fired.** The primitive computes each read twice over the same ids: the cached path (one prefill with the cache kept, each label's tokens but the last continued through it, the cache cropped back) and the fresh path (one full forward per label, no cache). Both cast the logits to float32 and take the log-softmax in float64; the rows score the right tokens on both paths (`score_cached`; `full`'s rows). The algebra is sound, so the discordance is numerical: the two paths run the model in bf16 through different kernels, and the seat's reading — which the diagnostic of §1.3 tests — is that the difference sits in the continuation tokens, where the decode kernel's single query meets the prefill's attention over 1.2k positions. On this box the two reads gave rel 0.0147 and 0.0861: at BK's mean scale of 11.15 nats, about 0.16 and 0.96 nats, where BK's own 2,400 reads had a median of 0.031 nats and a maximum of 0.125 (rel 0.0121). Their rate at TAU was 0 of 2,400, and n §2.1 made that rate p0; at p0 = 0 one exceedance fires. So the stage whose purpose is to measure the box's discordance (n §3 G-ACQ: "the fresh-versus-cached discordance distribution over 24 reads (§2.1's identity bound)") paused on the first exceedance of a bar set on another lab's hardware. Code's reading of the circularity is right.

**1.2 Ledger — design seat (82).** n §2.1's identity clause — "the d = 0 read is the vanilla forward's margin within the backend's measured nondeterminism (… exact on a deterministic backend)" — bound a difference between two computations by the repeat determinism of each, in the same sentence that quotes BK's nonzero cached-versus-fresh discordance on their own box. A deterministic backend repeats each path exactly and still differs between them. Fix: a bound on a difference between two computations is declared from a measurement of that difference on the box of record, never from the determinism of either; and a base rate borrowed with a bar (ledger (51)) is the box's where the bar binds a box.

**1.3 The order (n-build; the pod session on the box).**
1. **The driver's commit** on this smoke (Q2, §2): `scripts/n_sessions.py` v2d (`18f19b8e…4f5c`), by path, with its self-test raw (333/333 on the laptop, 344/344 at the box) and an entry that says the smoke ended PAUSE on the fidelity binomial, as the rule requires.
2. **The run of record** from the commit: the 24 reads, the rule as the driver carries it (TAU, p0 = 0 of 2,400 from G-DATA (vi), the end-of-run evaluation), every read's line in stdout as the smoke printed them (`fid=` to six decimals against TAU). It pauses at its end; its report (`n-report-v1`) records the pause; nothing is resumed until the ruling.
3. **The diagnostic**, in the same pod session, never of record, no package change: a script in Code's scratch (committed as a raw with its output) that, for the 24 reads' sessions and both labels, prints per label-token index the distribution over the 24 of |cached − fresh| per token (min, median, max in nats), and the same for the first token alone against the rest summed — no margin, no log-probability, nothing per session. It says where the discordance sits: in the first label token (the prefill's last-position logits against the full forward's, the same kernel on nearly the same length) or in the continuation tokens (the decode kernel against the prefill's). One load, 24 × (1 cached + 2 fresh) forwards, minutes.
4. **The adjudication.** The seat rules on the pause with (2)'s 24 lines, the report's counters (trials, exceedances at TAU and TAU/4) and (3)'s raw: cleared as the measurement, or a defect named. The ruling file's sha256 enters the report; the resume (`--resume --ruling p01=PATH`) completes skip-only and prints the discordance distribution (absdiff in nats and rel: min, quartiles, median, max; the counts above TAU and TAU/4; the identity-bound count), then ADDENDUM-n1 §2's label-convention comparison (the four counts and the four medians, the n raw of this date §5.5).
5. **The entry** `BACKEND — characterization` extended for this box (n :109), with the pause, the ruling and the distribution.

**1.4 What the measurement decides, declared now so the sessions can prepare.** Before LOCK-n v0.1 the seat places **ADDENDUM-n2 v0.1**, short, on the extension's figures:
- **p0.** The fidelity binomial's p0 is the box's measured rate at TAU from the extension's 24 reads (k of 24, with its exact-binomial consequence stated), BK's 0 of 2,400 reported beside; TAU itself is unchanged, and so are the cadence, the pause-and-adjudicate form and the ungated primary. The monitor then detects a rise above the box's own rate, which is what rule 21 wants of it.
- **The identity bound** (n §2.1; n §6's monitor at d = 0): the box's distribution with a declared margin — the seat's draft is twice the extension's maximum absdiff in nats, to be confirmed on the 24 — so that the campaign's d = 0 reads (N1-V's 160 shadows and N4's 320) do not pause on the tail of a 24-read sample.
- **The sensitivity row** at TAU/4 stays as BK's form; where it empties (PIN-n-20's `tau4-emptied`), the VERDICTS entry says so, and a second row at the box's extension median is reported beside, descriptive.
- **The read of record.** If the diagnostic puts the discordance in the continuation tokens, the fresh path — one full forward per label under the identical mask, the computation BK's own identity check calls the reference — is the candidate read of record for the campaign, the cached path becoming the check or dropped; the quantity is unchanged (the margin at the choice position under the steered-span mask), the implementation departs from BK's and the addendum says so. n-build estimates its cost from the extension's timings (the fresh pair's ms against the cached read's, which the records carry as `duration_ms_fresh`) for G-TIME-n; the seat decides at the adjudication. If the discordance sits in the first token, the paths are equally noisy and the cached path stays.

**1.5 (b) and (c) as Code posed them.** (b) would change the stage's code before the measurement, against the coordinating session's own direction for this case ("Don't settle it in code"); (a) gets the same measurement for one pause and one resume. (c) alone would delay the measurement for a question the measurement answers better; it is kept, after the run, as §1.3 item 3. R1–R6 stand; R5's alpha is moot at p0 = 0 and stays declared; p0 carried from G-DATA (vi) before the lock is right for this run; the end-of-run evaluation is accepted as the rule's form — a stage shorter than the cadence would otherwise never evaluate — and it is the flag Code raised at the BUILD, now ruled.

## 2. Q2 — the driver's commit

Yes. The smoke's purpose was to show the driver runs on the box: the copy at `d5d08fa` with exactly the driver changed, the manifest 23/23, the self-test 344/344, the package and the 11 closure lines equal to the laptop's, G-VER PASS, the load, two reads with their lines, and the stage's own monitor firing as the rule requires. An exit 1 on a pause is the stage behaving, not failing; the box script's last line read its own convention. The convention is amended for this stage and for any stage whose smoke can reach a monitor: a smoke that ends PAUSE with every read's line printed and its identity lines equal is a pass, and the script's summary says "PAUSE (pass)". No second smoke. The box answers' §2 item 5 is met by the commit before the run of record.

## 3. n-analyzer (`a84833e`)

**3.1 PIN-n-33, amended: pauses point by point.** n:140's "an unadjudicated pause stands on N2's reads" names the reads N2 uses — N2-E at the decision f, and N1-V, N1-R's 24 and N1-P at the norm-matched point — and the answers of this date §5.2 read incompleteness that way; a pause is read the same way. So: a pause standing on one of those reads makes N2 INDETERMINATE; a pause standing on any other read — N1-V at −1, an N1-R cell elsewhere, a guard's (N2-S, N2-C) — leaves N2 decided, the guard's figures reported beside with its pause. That is §5.2's rule with "on one of them" meaning those reads, and it is what §1.6 of 2026-11-16 was reaching for under the per-arm reading; the point-by-point ruling supersedes §1.6's sentence. PIN-n-33's first half is amended to this; its second half stands.

**3.2 The fourth form's label (the review's F4).** The field does not suffice: the sentences are what the preprint carries by hand (n §7.5), and *answered* against *concluded, not answered* is §0.6's whole content. The fourth form ends as A.2 and A.7 do, with " — [label]": *answered* iff G-READ-n PASS at d_eq and N4 PASS; *concluded, not answered (N4 [n4])* where the state is readable and N4 is not PASS; *concluded, not answered* otherwise. The readability clause stays as ruled. The battery's literal-text checks cover the three fills.

**3.3 Accepted:** PIN-n-34 (the sign words on every N2 figure, span_reward's included); PIN-n-35 (the fourth form a sentence input, not a coordinate; 2,561 evaluations); PIN-n-36 (the causes named by point; per-arm statistics per arm; the TAU/4 row's arm mark; no beside on an INDETERMINATE N2). The forms' digest moves with §3.2; the new digest is the entry's.

**3.4 Also accepted, from the BACKEND entry:** the reference artifact's path `data/olmo/determinism_base_h100-sxm.json`, named by class; and the coordinating session's reading of "move now" as the first listing (`26cf7d2`'s close line).

## 4. Departures: inert, no strike

- Code's two (`0eb7671` §6): a `sed` with the model folder's name in its argv, model-free; a window granted for v2c's self-test run on v2d, disclosed at the time. Inert. The standing rule restated: a window names the bytes it runs by sha256, and newer bytes take a new window or a line to the coordinating session before the run.
- The values-checkers' three: a names-only `ls` whose argv carried a marker through a glob (the STOP's checker); `git log --all --find-object` without item 3's pathspec, which named no commit and printed nothing from inside (the same checker); an unscoped `git ls-files` inside a pipe, names only, momentary (the analyzer entry's pass-2 checker). Each inert, each disclosed in its report, which is the form. The checkers' briefs carry the list of record v2's items 1–5 verbatim; a git command in a check takes item 3's pathspec.

## 5. The record

- n-build: the driver's commit (§1.3 item 1); the run of record's entry with the pause; the diagnostic's raw; after the ruling, the resume and the extension's entry.
- The pod session: the run, the diagnostic and the resume on `emw1e4embiwe9b`, each announced to the coordinating session; the box stays up through the resume on the PI's standing word.
- The seat: the adjudication on the 24 lines and the diagnostic; ADDENDUM-n2 v0.1 before LOCK-n v0.1.
- n-analyzer: §3's changes before the canonical run; close lines on `a84833e`'s entry.

## 6. Routing block for the PI (defaults in brackets; your words are the record)

**File placed untracked on the laptop:** this raw under `results/raw/` — sha256 and bytes in the paste block.

**N. n-build (and the pod session on the box)**
1. Q2 yes: driver v2d committed by path on this smoke, the box script's PAUSE-as-pass amendment [as ruled].
2. Q1 (a): the 24 reads from the commit under the rule as pre-registered, pausing at the end; then the per-token diagnostic (§1.3 item 3), never of record; nothing resumed until the ruling [go].
3. The adjudication on the 24 lines and the diagnostic; the resume with the ruling; the extension's entry with the distribution and ADDENDUM-n1 §2's comparison [as ruled].
4. ADDENDUM-n2 v0.1 from the seat on the extension's figures (p0, the identity bound, the sensitivity row, the read of record), before LOCK-n v0.1; n-build's cost estimate of the fresh path for G-TIME-n [noted].
5. R1–R6, p0 before the lock, the end-of-run evaluation: as declared; ledger (82) [as ruled].

**N. n-analyzer**
6. PIN-n-33 amended (pauses point by point); the fourth form's label in the sentence; PIN-n-34, -35, -36 accepted; close lines on `a84833e`'s entry [as ruled].

**C. Coordinating session**
7. This raw committed by path; the three checkers' departures and Code's two inert, no strike; the briefs' pathspec line [as ruled].
8. The artifact path and the "first listing" reading accepted [as ruled].
