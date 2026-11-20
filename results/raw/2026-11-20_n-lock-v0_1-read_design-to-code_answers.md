# n: the seat's read of LOCK-n v0.1's draft (`LOCK-n.md`, `5acca00f…586a`, 1010 lines) — the lock stands for step 10 after seven text edits and two riders in one battery window (the package's own `hashes`; the realized fidelity sample pinned); the BUILD's remaining open flags ruled; v7's readings R-A–R-E and PIN-n-40–42 accepted; G-ANL-n's PASS accepted (design → Code)

*Design seat, PI date 2026-11-20 (second sitting). On `LOCK-n.md` at the root, read whole (the 1010 lines of Code's draft 9) against `results/raw/2026-11-20_n-gvec-gcal-reads_design-to-code_answers.md` (`d639bdd`), ADDENDUM-n3 v0.1 (`0744136`) and n:117, as the first sitting's §5.2 asked; the read block `results/raw/2026-11-20_n-lock-v0_1_code-to-design_read.md` (`411b15c`) and its entry; the entries of `b6ea27f` (n_analyze.py v7: R-A–R-E, PIN-n-40–42, the parallel start), `1641948` (G-ANL-n's canonical run) and `bc85386` (the PI's routing of the first sitting, `2026-11-20_first-sitting_pi-routing.md`); the riders `…_n-lock-v0_1_plan-sha{,_out}.{md,txt}` and `…_interval{,_out}.{md,txt}`; the records the lock cites, each figure it quotes re-read from its source (`data/n/gvec/gvec.json`, `gvec_cosines.json`, `data/n/gcal/gcal.json`, `dose_map.json`, `data/n/gates/G-ANL-n.json`'s sha256, `data/n/ids/MANIFEST.json`'s, `valence_core/n/schema.py` :262–266); the lock's own two lines at :810–811. Not opened: anything under `data/n/ckpt`, `data/n/reports` or `data/mf3`. HEAD `411b15c`, origin `bc85386`, 3 commits unpushed. Placed untracked over the bridge; Code commits by path on the PI's routing; the n-build, n-analyzer, pod and coordinating sessions add their close lines. Calendar dates only; the commit hash is the record.*

## 0. The short form

- **The lock stands.** Every value I re-read is its source's: the site and the two R's, R_ℓ, the four named rows and the 24 random rows, the six G-VEC files and the three G-CAL-n files by sha256, the dose map (d_eq 0.2869170055735837, d_20 0.5738340111471674, seven points, none merged), the gate line and its figures, TAU, p0 1/26, C 0.25, alpha 0.01, the tile and E = 48 with 0.3827, the read plan (7,680 = 960 + 4,800 + 640 + 3 × 320 + 2 × 160) and its sha256, the analyzer v7 and its schema pin, G-ANL-n's artifact, the package digest and its twelve-file closure, the manifest and session-set hashes, the four documents' sha256s, the interval table (S: 39–554, median 142, eight values; SU: 39 on all 160), the two lines in PIN-n-26's form. n:117's eleven items and the coordinating session's five are each a section.
- **Before step 10's commit: seven text edits (§2) and two riders in one model-free battery window (§3)** — the package's own `hashes` at the lock's HEAD (Q1: measured, not read off a diff), and the realized fidelity sample's count and digest, which closes the BUILD's flag and makes the power sentence's "about 16" exact. Nothing in the design changes.
- **The remaining BUILD flags are ruled** (§4): N4's schedule notation is no discrepancy; G-READ-n's two seeds stand as pinned; a G-VER-STOP of any cause is a STOP for the seat before any read; the addenda are bound through the lock, no schema field; the rest as the lock has them.
- **v7's R-A–R-E and PIN-n-40–42 accepted; the parallel start inert; G-ANL-n's PASS accepted** (§5). The standing lines gain one (§2, edit 7). Step 10's order and what follows (§6); departures inert (§7); routing (§8).

## 1. What was read, and how

Each section against its sources: §1 against MANIFEST.json (`53a8cd74…99d8`; the six files' sha256s and counts); §2 against `schema.SESSION_SET_SHA256` (:262); §3–§4 against `gvec.json`'s `site`, `of_record`, `directions`, `random_sha16`, `files_sha256` and `valence` blocks and `gcal.json`'s `dose_map` and `figures`; §6's plan sha against the rider's output; §7 against `schema.TAU` (:265) and A-n2; §9 against `b6ea27f`'s and `1641948`'s entries; §12 against the first sitting's §2 of 2026-11-19; §13 against `ef105f1`'s entry and ans20 §3; §18 against `ef105f1`'s digest and `idsv`'s closure; §21's interval table against the rider's output (`ad82c1b7…7660`) and schema.py:64–66's 83 sessions; §23 against the four documents' sha256s and my three raws'. Every anchor opened was found at `1641948`. The drafting notes (drafts 3–9) are the lock's own history and stay. The `R:N` anchors hold at `1641948` alone, as the Conventions say; the commit is named, so they resolve.

## 2. Seven text edits before the commit (Code's, on this ruling; no value changes)

1. **The status line** becomes, at the commit: *Status: LOCK-n v0.1 — COMMITTED at PROPOSAL-n v0.2 §8 step 10 (commit named in its entry); of record from that commit until LOCK-n v1.0 supersedes it at step 13.* The first italic paragraph stays as history.
2. **§3's second bullet** — "The capture convention stands as built (ans19:16, Q1/G1): …every token in the passage mean and in R…" — states the superseded convention beside the convention of record. It is reframed: *The capture convention as first ruled (ans19:16, Q1/G1), superseded at the second sitting by the next bullet after G-VEC's first run STOPPED:* and then the quotation. Two bullets, one convention of record.
3. **Sources:** `S/step4b/lock/routing_lock.txt` is Code's scratch; a committed lock cites committed texts. The coordinating session's routing of the draft is committed as a raw in the lock's commit (`results/raw/2026-11-20_n-lock-v0_1_routing.txt`, or the name Code gives it, byte for byte as saved) and the Sources line names that path; the header's parenthetical likewise.
4. **§5, the fidelity sample:** after Code's PIN, the rider's result (§3.2): *the realized sample under `n-fid|{s}`: N of 160 sessions, the sha256 of their ids in the session set's order `…` (`results/raw/2026-11-20_n-lock-v0_1_fidsample_out.txt`)*; Code's flag "no digest of the realized sample is bound" is then closed and the sentence says so. §13's power sentence gains, after "about 16", the bracket *(the realized sample: N sessions, §5)*.
5. **§5, N4's schedule:** after Code's flag, one sentence: *Ruled at the lock's read: no discrepancy — n:50's "(40/39 and 41/40)" and n:92's "40/40 by `present` order as near as 79/81 allows" carry the same counts, told-S 40 in each `present`-order group and told-U 39 and 41; the schedule of record is the realized one, `n4_schedule_sha256` `228ab470…55f3`.*
6. **§18:** the closure's sentence "(Code's reading of the diff; the package's own `hashes` was not re-run)" is replaced by the `hashes` run's result (§3.1), the raw named, the twelve files and the digest as it printed them.
7. **§22, the standing lines,** gain (iv): *Code's declared departures (1)–(10) from G1–G14's and GC1–GC23's words, in `gvec.py`'s and `gcal.py`'s docstrings, stand as declared (ans19 §6; ans19b §3; `bc50244`).* And §23 gains this raw by path and sha256, as the lock's read, beside the three answers it already names.

A re-check by tool of the changed claims after the edits, as draft 9's values-check did; no second full pass.

## 3. Two riders, one battery window, before step 10

**3.1 Q1 — the closure: the package's own `hashes`, run once.** Code's reading of the diff is sound and is not the instrument: n:159 and pre06:14 bind the package "closure-style" by the package's own `package_sha256` and its own listing of each imported module, and ledger (82)'s class holds — a bound is measured, not inferred. One run of the package's `hashes` at the lock's HEAD, model-free, in a battery window the coordinating session grants, its output committed byte for byte as `results/raw/2026-11-20_n-lock-v0_1_hashes_out.txt` with its command and exit line in a rider. If it prints `06b55761…1d39` and the twelve files at §18's sha256s, §18 cites it and nothing else changes; a different digest or a different closure is a STOP for the seat before the commit.

**3.2 The realized fidelity sample.** By the package's own `keys` function over the 160 sessions of record in the set's order, in the same window: the sessions with `stream(f"n-fid|{s}").random() < 0.10`, their count, and the sha256 of their ids joined by newlines in that order; the output committed byte for byte as `results/raw/2026-11-20_n-lock-v0_1_fidsample_out.txt`, the script, command and exit line in a rider, a shell derivation beside it if one is cheap. The lock pins the count and the digest (§2, edit 4). The runner asserts nothing new: the key and the session set already fix the sample; the pin lets the campaign's report be checked against the lock, which is what a pin is for.

## 4. The BUILD's open flags (R:5372–5407 at `1641948`; the lock's §21), ruled

- **SCOPE's specifics:** the runner's PIN as written, with PIN-n-37's conservative form (ans18c) and O4 (ans20 §3) — accepted.
- **N4's schedule notation:** no discrepancy (§2, edit 5).
- **The keyed sample's digest:** pinned (§3.2).
- **Cap and alpha as the runner's inputs from the lock,** a resume refused under another: accepted; the lock is where they live (§11, §13).
- **The label-mass floor:** PIN-n-17's .20 is the analyzer's descriptive floor; the runner's `label_mass_below_floor` null while no floor is declared to it — accepted; nothing binds on it (n §4's counters decide nothing).
- **A G-VER-STOP that is not a token mismatch:** G-VER runs before any read (n:119); a STOP of any of its causes — `seq_len`, `ids_sha`, the spans' tiling, N4's two sequences, a label candidate, the manifest's pin — is a STOP for the seat, never a pause and never an exclusion; no read is launched and the campaign does not start. One sentence in §10's G-VER row.
- **`addendum_sha256` beside `proposal_sha256`:** no schema field. The identity's `lock_sha256` binds the lock; the lock names the three addenda by sha256 (§23); the analyzer of record binds all four. The chain is complete as it stands.
- **The comparator's band medians:** the lock's line stands (§10).
- **The reads' I/O outside the cap:** the cap is model time as the runner computes it (§11); I/O is outside and declared so.
- **`cache.crop(n)` below transformers 5.18:** the box's environment is pinned at 5.15.0 (§17); a move past 5.18 is a backend change, the characterization's concern, not the lock's.
- **G-READ-n's `cv_seed` 20261116 and `shuffle_seed` 20260905, and `fit_lr`'s four values:** accepted as pinned, declared before data.

## 5. v7 (`b6ea27f`), G-ANL-n (`1641948`), and the draft's making

- **R-A–R-E accepted** as Code reads them: N2's [f] filled by §3.4's deciding point and the reason clause alone; every point placed at d_20 or d_eq is its kept point under A-n1 §5.1's merge, "where the norms are equal exactly" holding where d_eq is unmerged (on this map nothing merges); both reasons named when both hold; §7.3's line a clause of Code's form around A-n3's two reasons; VERDICTS reads v1.0's lock, which carries v0.1's gate line verbatim. **PIN-n-40, PIN-n-41, PIN-n-42 accepted;** the gate line's form, once a relay, is now committed text (the lock's §21; A-n3 §3.3; this raw).
- **The parallel start:** v7 drafted in scratch in parallel with the runner delta, one development run of draft 1 before the delta's commit (not of record), nothing committed before it, the review–mutants–values-check–battery order as the coordinating session accepted — inert; the declaration's one failed part is recorded as Code declared it. The lock's draft 5, prepared in parallel with v7 — A-n3 §8.3's item (5) begun before its item (4) had landed, the departure from the listed order Code declared — likewise inert: scratch only, nothing committed, every anchor re-pinned after v7.
- **G-ANL-n's canonical run accepted:** PASS, battery 242/242, every coverage id reached, the pinned map's reach equal to the hand derivation under both gate branches; the artifact `e775cbb4…6088` is hole 13's. Code's binding of a pause's read to PIN-n-37 (the review's F1) accepted.

## 6. Step 10, and what follows

1. The window of §3 (two riders), then the edits of §2, then the re-check by tool.
2. **Commit `LOCK-n v0.1 — COMMITTED` by path** (n §8 step 10): `LOCK-n.md`, this raw, the two riders and their outputs, the routing raw, the entry; the lock's sha256 in the entry — the figure every stage identity from here carries as `lock_sha256` (schema.py:453). The n package does not move for it (no code changes).
3. **G-TIME-n** (step 11) on the box, under v0.1: six reads of each kind timed, projections for the PI's cap; its identity carries v0.1's sha256 and C. **G-VER** (step 12). **LOCK-n v1.0** (step 13) with the projections, the cap in hours (the PI's), D_n, the hashes of this document, the lock chain, the analyzer, BK's input files (n:120), and `lock: LOCK-n v1.0` with the route line — **by D_n 2026-12-15**, the day inclusive. Then the campaign in one pod session (step 14), G-READ-n, VERDICTS on the PI's word.
4. The box stays up through G-TIME-n and the campaign on the PI's word of this morning (rt20 item 4); the backend-ext leftovers cleaned now.

## 7. Departures: inert, no strike

`bc85386`: the coordinating session's forms as stated. `b6ea27f`: Code's parallel start (§5) and its `jq` reads; the reviewer's and the values-checker's forms as its entry states them. `1641948`: the run's `cd` through a glob into the venv's bin so that no marker reached an argument; the `pgrep` lines; the checker's forms. `411b15c`: Code's sweeps and their `jq`; the two window scripts in scratch; the forms its entry states. `d639bdd`'s and the riders' windows ran model-free under `nice -n 19`, Q-F3's campaign (PID 8051) running throughout, untouched. Nothing under `data/mf3`, a ckpt or a reports file was opened, listed or hashed by any of them. Inert, every one; the standing lines stand.

## 8. Routing block for the PI (defaults in brackets; your words are the record)

**File placed untracked on the laptop:** this raw under `results/raw/` — sha256 and bytes in the paste block.

**N. n-build (and the pod session on the box)**
1. LOCK-n v0.1: the two riders in one battery window (§3: the package's own `hashes`; the realized fidelity sample's count and digest); the seven edits (§2); the re-check by tool; then the commit by path at step 10 with this raw, the riders, the routing raw and the entry, the lock's sha256 in the entry [go].
2. G-TIME-n's launch files under v0.1 after the commit; the box's run; the projections to you for the cap at v1.0; then G-VER [go, after step 10].
3. The box: up through G-TIME-n and the campaign; the backend-ext leftovers cleaned now [as you ruled this morning].

**A. n-analyzer**
4. R-A–R-E, PIN-n-40–42 accepted; nothing changes in v7; v1.0's `lock:` line and the gate line verbatim at step 13 [as ruled].

**C. Coordinating session**
5. This raw committed by path in the lock's commit; close lines on `411b15c`, `1641948`, `b6ea27f` and `bc85386` citing it; the departures of §7 and the two parallel starts inert; the BUILD's flags as §4 rules them, the G-VER sentence into §10 [as ruled].

**D. Push**
6. The push of `bc85386..HEAD` behind the amended screen, after step 10's commit [yours].
