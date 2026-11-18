# n step 4 — the BACKEND extension's run of record paused at its end, as pre-registered, with the per-token diagnostic beside it: `p01` for the seat's adjudication (code → design)

*The n-build session (Code), PI date 2026-11-18. For the PI to route.*

*What ran, on n's box (pod `emw1e4embiwe9b`, the H100 SXM of the BACKEND entry `d5d08fa`), by the pod session, on the
seat's answers of 2026-11-18, second sitting, §1.3 items 2–3, and the PI's "Route as given". No lock is in force.*
- *The run of record. The driver committed at `ad856f0` (`18f19b8e…4f5c`), run by the box script v3
  (`f56fd61d…5369`) in a fresh copy at `ad856f0`, clean, with nothing extracted over it.*
- *The diagnostic, never of record. `n_bext_diag.py` (`c0ac67e4…08d1`, committed with this block as a raw), run by the
  box script `bext_diag_v1.sh` (`64384fa4…8e55`) in a second copy at `ad856f0`, after the run had ended. Nothing was
  resumed.*

*Sources read, by sha256:*
- *the run's whole output `bext_run_v3_out.txt` (`910e20a7…0e48`) and the pod session's record of it
  (`3a3fef2e…d44c`);*
- *the diagnostic's whole output `bext_diag_v1_out.txt` (`0d311f01…fc8b`) and the pod session's record of it
  (`61e73ce4…07c5`);*
- *the stage report `data/n/reports/backend-ext.json` (`27bc906a…2496`): its `cells` record only, for the cell's
  sha256 and record count;*
- *the seat's answers of 2026-11-18, second sitting (`cdecf39e…01d3`), §1.1–§1.5 and §2;*
- *`valence_core/n/primitive.py` (`7e7bb0a0…0b0c`), the two paths;*
- *`data/n/ids/labels.json` (`43a32a1b…49da`): counts of distinct ids per label token, no id.*

*Not opened: the cell `data/n/ckpt/backend-ext/N1-V__none__0.json` (`80770a19…78ea`; copied back by hash and hashed
only); its 31 capture arrays, which stay on the box's volume; anything under `data/mf3`.*

## 0. The short form

- **The run of record paused at its end, as pre-registered.**
  - Every step before the reads held. The 24 reads all ran, each line printed.
  - 10 reads are above TAU and 14 at or below it; 7 of the 14 read fid 0.000000.
  - The fidelity binomial's end-of-run evaluation fired under p0 = 0 of 2,400: pause `p01`. Nothing was resumed.
  - The box script's summary reads "PAUSE (pass)". That is the seat's §2 convention, which speaks of a smoke; Code
    reads its "for this stage" as covering the run of record.
- **The diagnostic places the discordance in the first continuation row.**
  - The first label token's |cached − fresh| is 0 in all 24 reads, for both labels.
  - Token 1 carries the discordance; token 2 is below 2e-06 nats.
  - Its rel reproduces the run's fid line to six decimals in 24 of 24 reads.
- **The questions.** Q1 is `p01`'s adjudication (§1.3 item 4); Q2 is the read of record, which the seat's §1.4 says it
  decides at the adjudication (§6). **Code adjudicates nothing.**

## 1. The reads the seat needs (m:271's form)

- **This raw**, in full.
- **The run's output and the pod session's record of it**, committed as
  `results/raw/2026-11-18_n-step4_bext-run3_{out,run}.txt`, in full. Under n's blinding (n :130) stdout prints "the
  fidelity value against TAU, timing — never a margin", and the run's stdout carries no margin and no pick (the
  records' margins and restricted-read picks are in the cell, under `data/n/ckpt`), so nothing in it is redacted.
- **The stage report**, committed as `data/n/reports/backend-ext.json`: the read domain. It holds the counters §1.3
  item 4 names (trials, exceedances at TAU and at TAU/4), `p01` and the binomial's state. Code did not read them.
- **The diagnostic's output, the pod session's record of it, and the script**, committed as
  `results/raw/2026-11-18_n-step4_bext-diag_{out,run}.txt` and `results/raw/2026-11-18_n-step4-diag_n_bext_diag.py.txt`,
  each in full. They hold no margin, no log-probability and nothing per session.
- **Not for reading:** the cell under `data/n/ckpt/backend-ext/` (item 2), committed for the record.

## 2. The run of record

The 24 read lines, verbatim (the run's output, lines 57–80):

```text
read 0 s=0 N1-V none 0 fid=0.014660 <= TAU ms=973
read 1 s=5 N1-V none 0 fid=0.086070 > TAU ms=666
read 2 s=10 N1-V none 0 fid=0.013781 <= TAU ms=683
read 3 s=22 N1-V none 0 fid=0.000000 <= TAU ms=657
read 4 s=26 N1-V none 0 fid=0.066629 > TAU ms=681
read 5 s=27 N1-V none 0 fid=0.011441 <= TAU ms=662
read 6 s=42 N1-V none 0 fid=0.007772 <= TAU ms=688
read 7 s=44 N1-V none 0 fid=0.022938 > TAU ms=635
read 8 s=46 N1-V none 0 fid=0.042895 > TAU ms=655
read 9 s=59 N1-V none 0 fid=0.000000 <= TAU ms=657
read 10 s=60 N1-V none 0 fid=0.029491 > TAU ms=713
read 11 s=61 N1-V none 0 fid=0.000000 <= TAU ms=653
read 12 s=62 N1-V none 0 fid=0.000000 <= TAU ms=718
read 13 s=65 N1-V none 0 fid=0.000000 <= TAU ms=636
read 14 s=78 N1-V none 0 fid=0.025507 > TAU ms=643
read 15 s=81 N1-V none 0 fid=0.000003 <= TAU ms=649
read 16 s=91 N1-V none 0 fid=0.040885 > TAU ms=659
read 17 s=92 N1-V none 0 fid=0.000001 <= TAU ms=630
read 18 s=130 N1-V none 0 fid=0.000000 <= TAU ms=725
read 19 s=135 N1-V none 0 fid=0.021833 > TAU ms=644
read 20 s=141 N1-V none 0 fid=0.029564 > TAU ms=651
read 21 s=147 N1-V none 0 fid=0.000000 <= TAU ms=643
read 22 s=149 N1-V none 0 fid=0.012675 <= TAU ms=688
read 23 s=152 N1-V none 0 fid=0.044854 > TAU ms=633
```

- **Before the reads.** The copy was the commit, the stage's root and report absent; the manifest 23/23; the self-test
  344/344; the package and closure lines equal to the laptop's before the run started. Then, in the output's order,
  "DRIVER … HEAD's committed bytes", G-VER PASS, R6's bridge, n's identifier `8264f719efd347a9` under the 4,096
  window, and a load of 12,804 ms.
- **The counts, by tool over the 24 lines:**
  - 10 reads are above TAU (launch indices 1, 4, 7, 8, 10, 14, 16, 19, 20 and 23), the largest 0.086070;
  - 15 are above TAU/4;
  - 7 read 0.000000, and two more are below 1e-5 (0.000003 and 0.000001).
- **Reads 0 and 1** repeat the smoke's two values exactly (0.014660 and 0.086070; `0eb7671`).
- **The end.** "PAUSE fidelity-binomial at the run's end"; "end PAUSE: 24/24 reads; report backend-ext.json". The
  report's end_state is PAUSE, and its identity lines equal step 3's.
- **The timing.** Each read's ms, both paths: min 630, median 657.0, max 973.

## 3. The diagnostic

Its lines 37–49, verbatim:

```text
label S, token 0: n 24, |cached - fresh| min 0, median 0, max 0 (nats)
label S, token 1: n 24, |cached - fresh| min 1.38117e-07, median 0.00314801, max 0.0375112 (nats)
label S, token 2: n 24, |cached - fresh| min 3.14713e-09, median 1.73785e-07, max 1.44522e-06 (nats)
label S, the first token alone: n 24, |cached - fresh| min 0, median 0, max 0 (nats)
label S, the rest summed: n 24, |cached - fresh| min 7.28231e-08, median 0.00314837, max 0.0375097 (nats)
label U, token 0: n 24, |cached - fresh| min 0, median 0, max 0 (nats)
label U, token 1: n 24, |cached - fresh| min 1.38117e-07, median 0.00860631, max 0.0492441 (nats)
label U, token 2: n 24, |cached - fresh| min 1.06959e-09, median 1.34173e-07, max 1.81453e-06 (nats)
label U, the first token alone: n 24, |cached - fresh| min 0, median 0, max 0 (nats)
label U, the rest summed: n 24, |cached - fresh| min 6.30844e-09, median 0.00860649, max 0.0492442 (nats)
first token: shared by both labels in 24 of 24 reads; its fresh log-probability identical in the two full forwards in 24 of 24
identity: the rel computed here equals the run of record's fid line, to six decimals, in 24 of 24 reads
timing over the 24 reads (ms): the cached read (one prefill, two continuations) median 309.0, max 601.4; the fresh pair (two full forwards) median 357.1, max 387.2
```

- **Before the reads.** The copy was the commit with exactly the diagnostic untracked; the manifest 22/22; its
  self-test 30/30; the run's `run.txt` by path (`e4e1c810…e378`, equal to the run's output, lines 50–83). Then one
  load (31,053 ms), the bridge held.
- **What the paths are** (`primitive.py`). The cached path is one prefill, whose last-position row predicts label
  token 0. Then, per label, its tokens but the last go through the cache in one forward: two positions here, whose rows
  predict tokens 1 and 2. The fresh path is one full forward per label, whose rows at those positions predict tokens
  0–2.
- **What the lines say,** read as numbers only:
  - Token 0, the prefill's row against the full forward's, is equal in all 24 reads for both labels.
  - Token 1, the continuation's first position, carries the discordance: medians 0.0031 (S) and 0.0086 (U) nats,
    maxima 0.0375 and 0.0492.
  - Token 2, its second position, is below 2e-06 nats in every read.
  - The rest summed is token 1's to within 2e-06 (token 2's size).
- **The first token** is the same id in all 12 "bare" labels: `labels.json` counts 1 distinct id at token 0, 12 at
  token 1 and 10 at token 2. On the cached path it is one prefill row for both labels. Its fresh value is identical in
  the two full forwards in 24 of 24 reads, so it cancels in both margins.
- **Identity.** The diagnostic's rel equals the run's fid to six decimals in 24 of 24 reads. It measured the run's own
  discordance, and the box repeated it.
- **Code's reading of the seven 0.000000 reads.** Token 1's minimum is the same for S and U (1.38117e-07). On each
  path, the row that predicts token 1 takes the same input for both labels, the shared first token. So a difference
  between the paths that moves both labels' token-1 log-probabilities alike cancels in the margin. The per-token
  values are nonzero in every read.

## 4. Items Code declares, without adjudicating

- **The diagnostic's two additions** to §1.3 item 3, the coordinating session's OK given, declared so the seat can
  strike either:
  - the two counts (the first token's fresh value, and the identity);
  - the timing line. It answers §1.4's request for the fresh path's cost without opening `data/n/ckpt`. The records'
    `duration_ms_fresh` stayed closed under item 2.
- **Code's reading of "nothing per session":** a cell of fewer than three reads prints its count only. Every cell here
  has n 24, so no line was cut.
- **The cost of the fresh path, from the diagnostic's timing** (§1.4, for G-TIME-n):
  - the fresh pair's median is 357.1 ms against the cached read's 309.0 ms, so the fresh path costs about 1.16 times
    the cached read at the median;
  - the maxima are 387.2 ms for the fresh pair and 601.4 ms for the cached read;
  - the stage, with both paths at every read, took a median 657.0 ms a read (the run's lines).
- **Departures,** with their class:
  - *Code's, an unpruned `find` over a ckpt and a report copy.* After the copy-back, Code ran a `find -type f` over its
    scratch folder holding the copied report and cell. It printed their two names only, no size or time. Item 2 lists
    any unpruned `find` among the forms barred over those files. Disclosed to the coordinating session.
  - *The pod session's, none.* Its first ship of the diagnostic's files stopped at its own check, with nothing sent,
    because the folder name was in use; it renamed the folder in its scripts first (its record, item 1).

## 5. Q1 — `p01`'s adjudication

The seat's §1.3 item 4: "cleared as the measurement, or a defect named".

*The readings to weigh:*
- **How it fired.** `p01` fired at the end-of-run evaluation, the only one a 24-read stage reaches. p0 = 0 of 2,400 is
  BK's rate on BK's hardware (n §2.1), and here 10 of 24 reads exceed TAU.
- **The box repeats itself.** Reads 0 and 1 repeat the smoke's values exactly, and the diagnostic reproduced all 24
  to six decimals. Code's reading: the discordance is a property of the two paths on this box, not run-to-run noise.
- **Where it sits.** The first label token, the prefill's row against the full forward's, agrees exactly. Token 1, the
  continuation's first position, carries the discordance, and token 2, its second position, nearly none.
- **The seat's own reading** (§1.1) puts the discordance in the continuation tokens. The diagnostic puts it in the
  first of the two continuation positions.
- **The split by session.** Seven reads print fid 0.000000 (rel below 5e-7), and ten exceed TAU. The per-token values
  are nonzero in every read (the minima in §3).
- **What follows the ruling** (§1.3 item 4, which names no difference between the two forms): the ruling file's
  sha256 enters the report, and the resume (`--resume --ruling p01=PATH`) completes skip-only. It prints the
  distribution and ADDENDUM-n1 §2's comparison.

## 6. Q2 — the read of record (§1.4: "the seat decides at the adjudication")

*The readings to weigh:*
- **The condition §1.4 sets.** It says "If the diagnostic puts the discordance in the continuation tokens, the fresh
  path … is the candidate read of record for the campaign". Code's reading: the discordance sits in token 1, a
  continuation token, so the condition reads as met; the decision is the seat's.
- **The quantity is unchanged.** As §1.4 says, it is the margin at the choice position under the steered-span mask; the
  implementation would depart from BK's.
- **The cost** is §4's estimate: the fresh pair at about 1.16 times the cached read at the median, per read, on this
  box. It comes from the diagnostic's own timing. §1.4 named the records' `duration_ms_fresh` as the source; those
  sit in the cell, closed to Code under item 2. The seat, or the analyzer at G-TIME-n, may read them there.

## 7. Not questions

- **The steps before the reads:** the copies, the manifests, the self-tests (344/344 and 30/30), the run's package
  and closure hashes and its G-VER, the diagnostic's hash of the run's stdout, and R6's bridge in both.
- **The report's counters.** The seat reads them in the committed report. Code read only its `cells` record, to check
  that the copied cell is the one the report records: equal `json_sha256` (`80770a19…78ea`), 24 records.
- **The capture arrays** stay on the box's volume, their digests in the committed cell (the coordinating session's
  word, v1's plan).
- **The cell's diffs.** The cell's records carry each read's margin and the restricted read's pick, which n :130 keeps
  from everyone before VERDICTS. This commit adds `/data/n/ckpt/** -diff` to `.gitattributes`, as m, mf3 and p have
  for their ckpt folders (m:318's form), so the cell never renders in a diff or a `log -p`. Whether the cell may be
  pushed before VERDICTS is the seat's and the PI's; the pre-push screen halts on it.
- **The box stays up** through the resume, on the PI's standing word (§5 of the seat's answers). Both copies and their
  work folders are left in place.

## 8. The record

- **This raw:** `results/raw/2026-11-18_n-step4-run-pause_code-to-design_STOP.md`.
- **The run:**
  - `results/raw/2026-11-18_n-step4_bext-run3_out.txt` (`910e20a7…0e48`, 88 lines) and `…_run.txt` (`3a3fef2e…d44c`,
    94 lines);
  - `data/n/reports/backend-ext.json` (`27bc906a…2496`);
  - `data/n/ckpt/backend-ext/N1-V__none__0.json` (`80770a19…78ea`).
  `.gitignore` admits exactly the report and the cell, and `.gitattributes` keeps `data/n/ckpt/**` out of diffs.
- **The diagnostic:**
  - `results/raw/2026-11-18_n-step4_bext-diag_out.txt` (`0d311f01…fc8b`, 51 lines) and `…_run.txt`
    (`61e73ce4…07c5`);
  - the script, `results/raw/2026-11-18_n-step4-diag_n_bext_diag.py.txt` (`c0ac67e4…08d1`);
  - its self-test raw (the laptop's run, the box's lines beside it), `results/raw/2026-11-18_n-step4-diag_selftest.txt`.
- **Nothing is pushed.** The resume waits for the seat's ruling and the PI's word.
