# ADDENDUM-n2 to PROPOSAL-n v0.2 — the fidelity rule, the identity bound and the read of record on the box of record
## v0.1 — design seat, PI date 2026-11-18 (the PI confirms the date at routing)

*An addendum, not a new version: PROPOSAL-n v0.2 (tracked at root, sha256 `30a3d0f5…04f4`) stays the proposal of record, with ADDENDUM-n1 v0.1 (`a61f13d`, sha256 `e979f8f2…5e03`). `n §N` is a section of v0.2; `A-n1 §N` a section of ADDENDUM-n1. It answers the BACKEND extension's run of record on n's box (`6df2131`: 24 reads, 10 above TAU under the "bare" convention, pause `p01`; its per-token diagnostic) and the seat's ruling on `p01` (`results/raw/2026-11-18_n-step4-p01_ruling.md`). It changes how the fidelity binomial's p0 and the identity bound are declared, adds one absolute ceiling, extends the sensitivity row, and settles the read of record. It changes no arm, dose, bar or sentence of n §5, and not the Clock (D_n 2026-12-15). Its figures are filled in LOCK-n v0.1 from the extension's figures of record (§4). Placed untracked over the bridge at root; Code commits by path on the PI's routing; the n-build and n-analyzer sessions add their close lines. Calendar dates only; the commit hash is the record.*

---

## §0 What this addendum does, and why now

**0.1** n §2.1 adjudicates each read's cached-versus-fresh discordance by BK's TAU, 0.0178835444 of the read's scale, with the class bound "by exact binomial against p0 declared in LOCK v0.1 from BK's measured rate at TAU on the 160 sessions (G-DATA (vi))": 0 of 2,400. Under p0 = 0 one exceedance fires (rule 21's zero-base-rate form). On n's box the extension's 24 reads, under the "bare" label convention, gave 10 above TAU; the stage paused at its end, and the seat cleared the pause as the measurement.

**0.2** The diagnostic beside the run shows what the discordance is: the first label token agrees exactly between the paths in 24 of 24 reads; the divergent label token carries all of it (medians 0.0031 and 0.0086 nats, maxima 0.0375 and 0.0492); the third token is below 2e-06 nats. In nats the margin's discordance is at most about 0.09 — below BK's own maximum of 0.125 on their box. It reads as large against TAU because TAU is scale-relative and the scale under "bare" is small: BK's recorded label log-probabilities are near −10 (for example −9.69 and −11.47 at d = 0 for `floor_b0` run 0), a scale of about 11 nats, where probable bare labels give a scale near 1. So the rule, as borrowed, binds about ten times tighter in nats on "bare" than it did on BK's reads, and whether this box's rate at TAU resembles BK's depends on the label convention of record, which A-n1 §2's check settles on the same resume.

**0.3** Two things follow and are fixed here: a base rate for the binomial that is the monitored box's (ledger (82)); and an absolute ceiling in nats, convention-independent, that catches a defect of the cache path at once, which the relative rule was never built to do. Why an addendum: v0.2 is not STOPPED; the lock chain pins the figures.

## §1 The fidelity binomial's p0 (amends n §2.1 and §0.10 B2)

**1.1** p0 is the box's measured per-read rate at TAU under the label convention of record, from the extension's reads of record (§4): with k exceedances of TAU in n reads, p0 = (k + 1)/(n + 2), Laplace's rule, so that a zero count does not make one exceedance fire. BK's 0 of 2,400 is reported beside it in the lock and in VERDICTS. TAU, the cadence of 160 reads, the exact-binomial test at the lock's alpha, the pause-and-adjudicate form and the ungated primary are unchanged.

**1.2** What the monitor then detects is a rise above the box's own rate — a batch whose exceedance count is improbable under p0 — which is what rule 21 asks of it. A defect that makes every read gross is §2's.

## §2 The absolute ceiling, and the identity bound (amends n §2.1 "Identity" and n §6)

**2.1 The ceiling.** On every re-computed read, at any dose, |cached margin − fresh margin| above **C nats pauses at once** (n §6's pause-and-adjudicate form; a new kind, `fidelity-ceiling`, after `non-finite` in the precedence of the seat's answers of 2026-11-16, second sitting, §3). C = max(0.25, 2 × the extension's largest |cached − fresh| margin discordance in nats under the convention of record), stated in LOCK-n v0.1. 0.25 is twice BK's maximum of 0.125 nats and about three times this box's under "bare"; no bf16 realization of either path reaches it, and a cache-path defect does.

**2.2 The identity bound** of n §2.1 — "the d = 0 read is the vanilla forward's margin within the backend's measured nondeterminism" — is read as the same quantity at d = 0, the cached shadow against the fresh forward, and its bound is C. The clause "exact on a deterministic backend" is struck: a deterministic backend repeats each path exactly and still differs between them (ledger (82)). n §6's "the identity bound exceeded at d = 0" is this check with this bound.

## §3 The sensitivity rows (amends n §2.1 and §4 (f))

The row at TAU/4 stays as BK's form. Where it drops more than half of an arm's reads at a point, the VERDICTS entry says so, and a second row is reported beside it, descriptive, dropping the reads whose rel is above the box's extension median under the convention of record. Neither row gates anything.

## §4 The figures of record

**4.1** The extension's figures of record — k of n at TAU, the largest margin discordance in nats, the median rel — are taken under the label convention of record (A-n1 §2). If the check names "bare", the run of record of `6df2131` gives them on its resume. If it names another candidate, the extension's 24 reads are run once more under that convention, in the same session, as a second stage (`backend-ext-2`: its own root and report, the first kept, both in the entry), with the fidelity rule as the first run carried it; its end-of-run pause, if it fires, is adjudicated by the seat on the same ground as `p01`'s ruling unless the figures show otherwise. One load and 24 reads.

**4.2** LOCK-n v0.1 declares, from those figures: p0 (§1.1); C (§2.1); the extension median rel (§3); the convention of record; and BK's figures beside each.

## §5 The read of record (settles A-n1 §1.4's reservation, the seat's answers of 2026-11-18, second sitting, §1.4)

The cached path — one prefill under the mask, each label's tokens continued through the cache — stays the read of record, as BK's design has it. The fresh forward is another bf16 realization of the same quantity, not a reference: the diagnostic shows the two paths agreeing exactly where a label token is near certain and differing by rounding where it is not, on both paths alike. The margin's per-read discordance (at most about 0.09 nats on this box) is small against the session SD BK report at d = +1 (0.623 nats) and the effects n §2.5 sizes, and it averages across sessions. The fresh pair's cost, measured at the extension (median 357.1 ms against the cached read's 309.0 ms), is recorded for G-TIME-n and used by nothing.

## §6 What changed, the PI's routing block, Code's block, the referents

**6.1 What changed, by section of v0.2:** §2.1 (p0's source; the identity clause's bound and its struck parenthetical; the sensitivity row); §0.10 B2 (p0's source); §4 (f) (the second row); §6 (the ceiling as a pause kind; the identity bound as C). Unchanged: TAU, the cadence, alpha, the arms, doses, bars, sentences, the Clock.

**6.2 The PI's routing block carries:** (1) the date; (2) decision (n-3), §1's p0 from the box's figures with Laplace's rule, adopted or declined — declined, p0 stays BK's 0 of 2,400 and the campaign pauses at its first exceedance for the seat's adjudication each time; (3) decision (n-4), §2's ceiling and identity bound, adopted or declined — declined, the identity bound is the extension's largest discordance of record with no margin; (4) §5 as the seat's ruling.

**6.3 Code's block, in order:** (1) referent check of 6.4; an unresolved substantive item → STOP. (2) **Commit `ADDENDUM-n2 v0.1 — COMMITTED`** with the PI's routing verbatim. (3) n-build: the resume of `6df2131`'s run with the seat's ruling; the comparison; §4.1's second run if the convention is not "bare"; the `fidelity-ceiling` kind in the runner and the schema (a follow-up schema commit settled with n-analyzer: the kind, its place in the precedence, the report's and the lock's fields for p0, C and the median), the pin moving as before; the extension's entry. (4) n-analyzer: §3's second row and the ceiling's pause kind in the reader, before the canonical run. (5) LOCK-n v0.1 with §4.2's declarations, drafted to the seat. Entries this addendum adds to n §8's list: `ADDENDUM-n2 v0.1 — COMMITTED`.

**6.4 Referents Code verifies at commit — only what this document quotes.** PROPOSAL-n v0.2 at root: §0.10 B2, §2.1 (fidelity; identity), §2.5 (0.623), §3 G-ACQ, §4 (f), §6. ADDENDUM-n1 v0.1 at root: §1.4 (as the seat's answers of 2026-11-18, second sitting, carry it), §2. The seat's answers of 2026-11-16, second sitting, §3 (the pause precedence). `6df2131`'s block and the two outputs it commits: the 24 fid lines (10 above TAU; 0.086070 the largest); the diagnostic's medians 0.00314801 and 0.00860631, maxima 0.0375112 and 0.0492441, token 2 below 2e-06, the first token exact in 24 of 24, the timings 357.1 and 309.0 ms. `718c48e`'s block, Q4: −9.69, −11.47. G-DATA (vi) as n §2.1 quotes it: median 0.031 nats, maximum 0.125, mean scale 11.15; 0 of 2,400 at TAU. CLAUDE.md rule 21. The ruling raw `results/raw/2026-11-18_n-step4-p01_ruling.md` by path.
