# n: LOCK-n v0.1's draft, placed untracked at the root as `LOCK-n.md` for the seat's read (code → design; STOP)

*Code (the n-build session), PI date 2026-11-20. On the PI's routing of the seat's reads of 2026-11-20 (first
sitting), item 3, and the placement's form, agreed with the coordinating session. LOCK-n v0.1's draft is placed
untracked at the root as `LOCK-n.md`, sha256 `5acca00f55d19516198cceb1035216b08f514c60045e4ec306790f3a7611586a`, 1010
lines, for the seat to read whole against its answers of 2026-11-20, ADDENDUM-n3 and n:117 before PROPOSAL-n v0.2 §8
step 10 commits it. Nothing in it has run, and nothing in it is of record until step 10. This is a STOP: the lock
waits for the seat's read. Short forms as the lock's Conventions give them; `rt20:N` is line N of
`results/raw/2026-11-20_first-sitting_pi-routing.md` (`bc85386`).*

## 1. What is placed, and why there

- **The routing**, rt20:15, verbatim:

  > 3. LOCK-n v0.1's draft filled from the two records (§5.1: holes 1–9, 11, 15, 16, the gate line, the interval declaration, E = 48 and 1 − 0.99^48 = 0.3827, the monitor sentence with the power note), placed for the seat's read before step 10 [untracked at root under the lock's name, sha256 and line count in the entry].

- **The seat's form for it**, ans20:56: "Code places the filled draft where the seat can open it — untracked at root
  under the lock's own name, its sha256 and line count in the entry that announces it — and the seat reads it whole
  against this raw, A-n3 and n:117 before the commit; the form of that placement is Code's and the coordinating
  session's call. The seat's read is one sitting."
- **The name**: `LOCK-n.md`, the name the analyzer's battery expects VERDICTS to bind (n_analyze.py:4901,
  n_analyze.py:5534; VERDICTS binds its `--lock` file's name, n_analyze.py:6699), at `1641948`.
- **The file**: byte for byte Code's draft 9, 1010 lines, every anchor at HEAD `1641948`. It is placed in the commit
  window of the commit that carries this raw, and it is not committed: it stays untracked until step 10 commits it.
- **The order**, the coordinating session's of 2026-11-20: v7 landed and verified (`b6ea27f`); G-ANL-n's canonical run
  and its commit (`1641948`); Code's re-pin pass at that HEAD; the checks and one blind values-check; the placement in
  the commit window. The placement waited for G-ANL-n's run because v7's `verdicts_precheck` resolves the lock's path
  (realpath), which stats an untracked `LOCK-n.md`. G-ANL-n's run checked that no `LOCK-n.md` was at the root before
  it ran (R:48–49, at `1641948`); Code has placed none before this window.

## 2. The holes

The 18 holes, numbered as the opens STOP raw names them
(`results/raw/2026-11-19_n-lock-v0_1-opens_code-to-design_STOP.md`:20–37, `d85fc34`):

| hole | what | filled at | from | in the lock |
|---|---|---|---|---|
| 1–7 | G-VEC's: the site and R at both indices, the four named rows' sha16s, the 24 random rows', the six files' sha256s, R and R_ℓ, the capture band | draft 3 | `data/n/gvec/gvec.json` (`e3b48ed`) | §3, §4, §6 |
| 8 | d_eq, d_20 and the points the merge keeps | draft 4 | `data/n/gcal/gcal.json` (`db00d6d`) | §4 |
| 9 | G-CAL-n's three files' sha256s | draft 4 | the same | §4 |
| 10 | the read plan after the merge and its `read_plan_sha256` | draft 4b | the package's own function, in a battery window ([rider](2026-11-20_n-lock-v0_1_plan-sha.md)) | §6 |
| 11 | E and 1 − 0.99^E | draft 4 | §6's plan; bc | §13 |
| 12 | `scripts/n_analyze.py`'s sha256 of record | draft 7 | v7 (`b6ea27f`) | §9 |
| 13 | G-ANL-n's canonical run's artifact sha256 | draft 8 | `data/n/gates/G-ANL-n.json` (`1641948`) | §9 |
| 14 | the n package's sha256 at the lock, with its closure | draft 7 | the package at `ef105f1`, unmoved | §18 |
| 15 | A2's extension to G-CAL-n, confirmed | draft 5 | rt19b:23 | §14 |
| 16 | the seat's read of every G-CAL-n turn | draft 6 | ans20 §2.4 | §22, §15 |
| 17 | the departures' standing lines | draft 5 | A-n3:64, carried as written | §22 |
| 18 | G-TIME-n's figures | — | v1.0's (ans19b:43) | §16 |

ans20:54 lists 10 and 17 among the holes "**Still open**". The drafts had filled both before that raw reached Code:
10 by the package's own function at draft 4b, in a battery window the coordinating session granted, and 17 at draft
5, with A-n3 §6.3's three lines carried as written (ans20:54: "the standing lines — A-n3 §6.3's three, carried as
written"). The seat's read may add a standing line; §22 says it joins them there.

## 3. What the last pass changed besides the holes

Drafts 7 to 9 are the pass after n-analyzer's v7 (A-n3:79, item (5)), prepared in scratch on the coordinating
session's word and finished at `1641948`. Besides holes 12, 13 and 14, each change below is cited in the lock:

- **The anchors**, re-pinned by content in two hops, `516b60f` → `b6ea27f` → `1641948`. Each cited block of lines was
  found once, unchanged, in the file at the new commit, by Code's tool. Nine blocks that the changes since `516b60f`
  rewrote are re-cited by hand to the lines that now carry them: gcal.py's hurdles, status and order; runner.py's
  SCOPE, binomial and alpha; schema.py's p0 fields. One continuation anchor in §1 (":310"), which the tool did not read
  as an anchor, is re-pinned by hand at draft 9: schema.py:315.
- **Draft 9**: one blind values-check of draft 8, this raw and its entry, its findings on the lock applied: the
  anchor above, §1's span sentence in R's words, §3's site quote anchored, §5's seed row with the gate's batch, §13's
  quotation of ans19:51, and `m:N` in the Conventions
  ([`2026-11-20_n-lock-v0_1_valuescheck.md`](2026-11-20_n-lock-v0_1_valuescheck.md); the entry gives each item's
  disposition).
- **G-CAL-n's form of record**, §10 and §15, as the stage ran it (`bc50244`, run at `db00d6d`). ans19b:71 listed
  "the arrival's form (§1.4)" for the draft, and draft 5 had not carried it:
  - the arrival, over positions 1..n, with `arrival_all` beside (A-n3:26, A-n3:28);
  - the early STOP and the early PAUSE, the gate's batch in the order (A-n3:30, A-n3:48);
  - O1, accepted at the second sitting (ans19b:58);
  - O2, as changed there (ans19b:59).
- **§13**: the runner's tile as built (`ef105f1`), in place of "the runner today", cumulative.
- **§15 and §21**: F5 as the schema asserts it since `ef105f1`, with O6 (ans20:45); O4 in the runner's SCOPE
  (ans20:44); "the three addenda" in the BUILD's flags.
- **§23**: ADDENDUM-n3's sha256, with decisions (n-5) adopted and (n-6) confirmed; the seat's answers of the second
  sitting of 2026-11-19 and of 2026-11-20 by sha256.
- **§24**: what is done, with each step's commit.
- **§6 and §21** name the two window riders. **§9** drops v6's line: v7 is of record.

## 4. For the seat

- **Q1 — the closure (hole 14).** The package's digest at the lock, `06b55761…1d39`, is computed by shell in m's
  `package_sha256_of` form. Run over `516b60f`'s blobs, the same shell form gives the figure the package's own `hashes`
  printed there (idsv:195). The closure is Code's reading of the diff:
  - no file under `valence_core/` outside `valence_core/n/` has changed since `516b60f`;
  - the package's imports have changed since only within the package (`directions`) and the standard library
    (`shutil`);
  - so the twelve files of `516b60f`'s closure (idsv:196–207) stand, each re-hashed by shell at `1641948`, 12 of 12
    equal.

  The package's own `hashes` was not re-run; it would need a battery window (model-free). Does that reading stand
  for step 10, or does the seat want the package's own `hashes` before it?

Nothing else is asked. The seat reads `LOCK-n.md` whole against ans20, A-n3 and n:117 (ans20:56); step 10 commits it
after that read.

## 5. The riders and the checks

- [`2026-11-20_n-lock-v0_1_plan-sha.md`](2026-11-20_n-lock-v0_1_plan-sha.md) and
  [`2026-11-20_n-lock-v0_1_plan-sha_out.txt`](2026-11-20_n-lock-v0_1_plan-sha_out.txt) (§6's window);
- [`2026-11-20_n-lock-v0_1_interval.md`](2026-11-20_n-lock-v0_1_interval.md) and
  [`2026-11-20_n-lock-v0_1_interval_out.txt`](2026-11-20_n-lock-v0_1_interval_out.txt) (§21's window);
- [`2026-11-20_n-lock-v0_1_check.txt`](2026-11-20_n-lock-v0_1_check.txt): Code's checks of the placed bytes, shell
  only;
- [`2026-11-20_n-lock-v0_1_valuescheck.md`](2026-11-20_n-lock-v0_1_valuescheck.md): one blind values-check of
  `LOCK-n.md`, this raw and the entry.

Their sha256s, and Code's departures in the drafting, are in the entry that announces this raw.
