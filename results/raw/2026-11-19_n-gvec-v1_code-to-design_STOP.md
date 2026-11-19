# n — G-VEC's run of record STOPPED: R within 2% of 25.49 at neither candidate index (code → design; STOP for the seat)

PI date 2026-11-19. Code (the n-build session). For the seat, through the coordinating session. Nothing is re-run,
and Code adjudicates nothing: the figures are as printed, and no cause below is weighed.

## 0. The short form

- **G-VEC ran as built** (the seat's answers of 2026-11-19, first sitting, §0: "G-VEC runs as built", with G1, G3, G6
  and G9 standing at §1.1–§1.4), from its BUILD's commit `da7bdec`, on pod `emw1e4embiwe9b`, and **STOPPED at its R
  check**: R is 44.04 at adapter index 31 and 45.11 at index 32, against 25.49; |R/25.49 − 1| is 0.728 and 0.770, so
  R is about 1.73 and 1.77 times 25.49. Neither index is within 2%, and that is a STOP (n §2.3: "reproduced at G-VEC
  within 2%, else STOP"; ADDENDUM-n1 §6.1).
- **The record alone is written:** `data/n/gvec/gvec.json` (`3331da71…ee95`), status STOP, site null. No direction,
  cosine or R_ℓ of record exists; the stage stopped before the contexts.
- **The answers' §1.1 pre-declared an alternative, which has no figure yet.** R over positions 1..n was not added to
  the STOP record: the launch files were already checked, and frozen at the hashes sent to the coordinating session,
  so G-VEC ran as built, and that figure "comes from the re-run" (the answers' §1.1).
- **The seat chooses the path** (§3): a diagnostic re-run never of record, a ruled convention change that re-runs
  G-VEC of record, or another. The questions are Q1–Q3 (§5).
- G-CAL-n's launch files wait for G-VEC's PASS. The box stays up and idle (routing item 5).

## 1. The figures, as printed

From the run of record's output (the stage's lines, `run.txt`; the record):
- "passages: 544 (224 positive, 224 negative, 96 neutral), one forward each, captured at (31, 32)";
- the neutral passages: "96 passages, min 35, mean 43.36, max 57" tokens; 4,163 neutral tokens (the record's
  `passages.neutral_tokens`);
- the longest input of the ids of record (the 544 passages and the 1,344 contexts): 90 tokens, within the window 4096
  (the inputs line; the record's `longest_input`);
- "R at index 31: 44.04249774012646 (|R/25.49 - 1| = 0.727834356223086; outside 2%)";
- "R at index 32: 45.107750142385356 (|R/25.49 - 1| = 0.7696253488578015; outside 2%)";
- "G-VEC STOP: R is within 2% of 25.49 at neither candidate index (n §2.3: "else STOP"); the seat rules".

By arithmetic only, R/25.49 = 1 + the printed figure: 1.727834356223086 at 31 and 1.7696253488578015 at 32.

The smoke, never of record (two neutral passages and two contexts, on a load of its own, before the run's):
- "SMOKE R at index 31 over the first 2 neutral passages: 42.62270212364156; R_ell over the first 2 contexts in A3's
  order: 22.23089391504287";
- "SMOKE R at index 32 over the first 2 neutral passages: 43.66884683035452; R_ell over the first 2 contexts in A3's
  order: 22.167402391674045".

BK's figures beside them, as the record carries them: `bk.resid_rms` 25.491040760519905 and `bk.pole_l2`
2.319276809692383 (BK's `strength_ladder/analysis.json`, layer 32). BK's records give ‖ṽ(+1)‖ = 7.6473 at ρ = 0.30
(`reduced.json`'s `injected_l2`, 7.647312164306641 at |d| = 1; n §2.3), which is 0.30 × 25.491.

The apparatus, from the record's provenance: `allenai/OLMo-2-0325-32B-Instruct` at revision `b96024342a77` (files
aggregate `36f05404…0fdb`); bf16 on an H100 80GB HBM3, deterministic, `CUBLAS_WORKSPACE_CONFIG=:4096:8`, seed
20260818; torch 2.8.0+cu128, transformers 5.15.0; the backend identifier `8264f719efd347a9`, as at backend-ext-2,
bridged to the characterization's `4ed3f2c70fe8afbf`; the package `882c9217…5ca7`; the driver `fecde87a…3958`; the
ids of record `fdf73d85…ef38`; the corpus `ef6b00dc…3cc3`.

## 2. What the texts fix, and what the answers' §1.1 pre-declared

- n §0.8 (n:36): "per-passage mean residual at layer 32 over the passage's tokens; … R the RMS residual norm over the
  neutral corpus's tokens at layer 32 (BK §3.1)".
- n §2.3 (n:81): "their records give ‖ṽ(+1)‖ = 7.6473 on Instruct at layer 32, so R ≈ 25.49 there [C] — reproduced
  at G-VEC within 2%, else STOP."
- ADDENDUM-n1 §6.1: "The injection index is the adapter's index for "layer 32" as G-VEC's R check confirms it (within
  2% of 25.49)."
- The capture convention, as ruled (the answers' §1.1, Q1): "each passage forwarded alone from its committed ids, no
  special token and no template; every token in the passage mean and in R; the PCA centred; R the pooled RMS over all
  neutral tokens."
- The answers' §1.1, pre-declared: "If R misses 2% at both indices, the first alternative the seat will weigh is the
  sink position (position 0) left out of both the means and R, so a STOP's record carries, beside R at both indices, R
  over positions 1..n at both, descriptive — one more figure in the STOP record if the change is cheap before the
  launch files; if it is not, G-VEC runs as built and that figure comes from the re-run." The launch files were
  checked, and frozen at the hashes sent to the coordinating session, when the answers came, so G-VEC ran as built
  (Code's call, recorded in n-build's close line on `99196e1`'s entry), and the STOP record holds R at both indices
  alone.

## 3. The paths, and what each would take

- **(a) A diagnostic re-run, never of record.** It would print figures from the same 96 neutral forwards at both
  indices, for example R over positions 1..n (the figure of the answers' §1.1) and a per-position norm profile; the
  seat names the set (Q2). It means:
  - a small `gvec` delta, a diagnostic command beside the stage that writes nothing under `data/`;
  - its self-test in a battery window, one blind review on the delta, a values-check, and a commit;
  - launch files v2 (the script, its manifest and the `hashes` run in a battery window of their own), checked and
    relayed by the coordinating session;
  - one box run by the pod session: one load and 96 forwards;
  - the copy-back, and an entry with its figures, for the seat's ruling.
- **(b) A ruled convention change, and G-VEC re-run of record under it.** The seat names the convention; G-VEC
  re-runs of record with the smoke. It means:
  - a `gvec` delta that makes the ruled convention the capture of record, with its self-test, one blind review, a
    values-check and a commit. A token left out of the means and R changes the arithmetic over the same ids. A
    special token or a template changes the ids the box forwards, and every input id is rendered on the laptop and
    committed under `data/n/ids/` (ADDENDUM-n1 §1.1: "The box tokenizes nothing for n's inputs"), so a new render
    and its commit would come first;
  - launch files v2, as in (a);
  - the box run of record: the 544 passages and the 1,344 contexts, about 1,900 forwards, as the eleven readings'
    block put it for any capture clause struck but the centring (`99196e1`, G1);
  - then, on a PASS, G-CAL-n's launch files.
- **(a) then (b)** is the two in turn: the diagnostic first, then a ruling on its figures.
- Under any path: G-CAL-n's launch waits for G-VEC's PASS, and LOCK-n v0.1's dose map waits with it (d_eq uses R).
  G-CAL-n's own delta and (v)'s render go on meanwhile. The box stays up and idle until the PI's word on it.

## 4. Other candidate causes the texts name (listed, not weighed)

- **The sink position**, the answers' §1.1's first alternative: position 0 counted in the passage means and in R.
- **The forward's framing:** the eleven readings' block (`99196e1`, G1, "Another answer") lists the clauses whose
  striking changes R: "for example a special token, a template, a token left out of the mean and R, or R as a mean of
  per-passage RMS". G-VEC forwards each passage alone, with no special token and no template.
- **R's form:** the pooled RMS of the per-token residual norm over all 4,163 neutral tokens (§1.1), not a mean of
  per-passage RMS.
- **A capture convention's size:** n §2.3 quotes OLMo-3.1 DPO's 55.45 under A3's span-mean convention "only to show
  the two conventions may differ by 2×".
- **The index:** BK's "layer 32" read as adapter index 31 or 32 (ADDENDUM-n1 §6.1; G2); both were measured (§1).
- **BK's scale:** BK's ‖ṽ(+1)‖ = 7.6473 at ρ = 0.30, from which n §2.3 takes R ≈ 25.49 (n:81); BK's `resid_rms`
  25.491 is in §1.
- Not named: BK's own capture code, which n §0.8 says BK's repository does not hold ("BK's repository holds neither
  the steering vectors nor the experiment code").

## 5. Questions for the seat

- **Q1.** Which path: (a), (b), (a) then (b), or another?
- **Q2.** Under (a), which figures, at both indices: R over positions 1..n (the answers' §1.1); a per-position norm
  profile, and over which positions; R as a mean of per-passage RMS; any other the seat names.
- **Q3.** Under (b), the convention of record, and whether G1's other clauses stand as ruled (§1.1).

The box, pod `emw1e4embiwe9b`, is up and idle on routing item 5; whether it stays up while the seat rules is the PI's.
