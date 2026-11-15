# Item 7's line: (a) and (d) together, no BUILD; the locks may be placed (design → Code)

*Design seat, PI date 2026-11-14 (evening). On the pod session's block `results/raw/2026-11-14_p-backend-line_code-to-design.md` and its entry (`bd8808c`), read in full; the entries `cdccc66` (the seat's answers committed; the close on G-F3) and `dd0bb89` (`WORKFLOW.md` v1.0 committed; the PI's "Hold the locks"); the amended drafts' sha256s and diffs as `bd8808c`'s entry prints them (each diff exactly (A1)–(A3); no second read owed, §B.5 of the seat's answers of 2026-11-14, `6b963adf…db3a`, here `gl:`). The code sites are taken as the block cites them (`valence_core/p/stage.py:615`, `:639`, `:1352–1357`, `:1550`; m's `stages.py:1109`, `:1346–1349`, `:2065`, `:2412`; `resume.py:324`); the seat opened no checkpoint, call log or report. **Placed untracked over the bridge; Code commits by path on the PI's routing; the pod session adds its close line.** Calendar dates only; the commit hash is the record.*

## 0. The short form

- **Q1: (a) and (d), carried together. (b) declined. (c) declined now; its substance is a self-test, owed at p's next hash-moving BUILD if there is one, not a BUILD before the locks.** Item 7's sentence in `gl:`§B.4 was wrong about the place: the comparison prints nothing when the identifiers are equal, and the precheck never sees the adapter's identifier, so no raw can carry "the comparison's line" without (c). The sentence is corrected here; the ruling's purpose — that the record show the campaign ran on the backend of record, where the self-test cannot show the comparison ran — is met by (a) and (d).
- **The locks:** nothing in this answer moves p's code or the amended drafts. On the PI's word releasing his hold, each amended draft is placed byte for byte as `LOCK-p-OLMo-{ckpt}.md` and committed by path, its v1.0 entry naming its sha256 (`fafb786d…2bc4`, `25c52f56…3dcf`, `f71c97c1…0e67`), now (§B.5: "now, not at the date"; D_p 2026-12-15 at the latest).
- **Ledger (69), the seat's:** `gl:`'s header gives the dpo draft's sha256 as `f2a6960f…a28d`; the file and `012ffbe`'s block give `…a28b`. The coordinating session caught it before routing; the pod session carries it as an observation. A typed prefix; the fix is that every sha256 prefix in a seat text is pasted from the tool's output, never typed. Nothing else in the raw rests on it.

## 1. The ruling and its ground

**What item 7 guards.** S3 is a test gap, not a code gap: p's live comparison (`stage.py:1352–1357`) runs after the load in every recorded run and STOPs on a differing identifier, but no self-test exercises it on the stub, so a mutant that dropped it would survive. The consequence of a dropped comparison would be a campaign running on a backend other than the lock's without a STOP. That consequence is already guarded twice: **before the campaign**, by the seat's §4.2/§B.3 rule — respawn (ii)'s `BACKEND — characterization` on the replacement box must give `641ee466f4553b6a`, and a differing identifier is a STOP for the seat before any precheck; **on a `--resume`**, by m's identity check, which carries `backend_identifier` (CHECKPOINT MISMATCH). The only case p's comparison alone covers is a fresh start on a box whose characterization matched and whose adapter then differs — a box that changed between its characterization and its first launch.

**Why (a) and (d), and why together.**
- **(a)** puts the first guard in the precheck ×3 raw: beside each unit's `backend of record 641ee466f4553b6a`, respawn (ii)'s identifier for the box, computed by Code's laptop check from the characterization run's provenance block as on 2026-11-06 (`results/raw/2026-11-06_respawn_determinism.txt`, lines 65 and 69), with the `BACKEND — characterization` entry's hash and the respawn raw's path; and the word "equal". It moves one line in the box's precheck wrapper and nothing in p's code or the locks.
- **(d)** puts the second computation in each campaign's raw, once each invocation has ended (the list of record v2, item 5): m's campaign report `identity.backend_identifier`, computed by the same function over the campaign adapter's own provenance, against the lock's line — the identifier only, never the record's stamp — and the entry's form carries it, as the gates' raw did at `qual` (`results/raw/2026-11-11_p-qual.txt`, line 2). It moves nothing in p's code or the locks.
- Together they record the identifier of record by two computations on two provenance blocks (the characterization run's; the campaign adapter's), before the campaign and after each invocation. **And (d) is the detector for the S3 case itself:** if a dropped comparison ever let a run continue on a differing adapter, (d)'s line would read "not equal" after that invocation, which is a STOP for the seat — the report's identity would disagree with the lock while nothing had fired. So the record shows what the self-test cannot: not that a line of code executed, but that the campaign's backend was the lock's, invocation by invocation, and that any S3 failure would have been visible at the first look.
- An invocation that launches no session leaves no provenance entry (`resume.py:324`) and so no (d) line; it generates nothing either, so nothing is at stake in it. The STOP path prints itself.

**Why not (b).** Three model loads on the box to repeat, before the campaign, a comparison the stage makes after its own load; it is a copy of the check, not a record of it, at the cost of three cold loads (130–200 s each, m:205) and a wrapper that loads adapters outside the stage.

**Why not (c), now.** One print line from `_run_recorded` moves p's package hash (`a38d93bb…a2d7`), which each draft names, which the precheck checks, and which G-SHAPE-p's and G-ANL-p's artifacts record: a BUILD with its review and values-check, both re-runs, three new drafts whose diff goes beyond (A1)–(A3), a second read, and a day of calendar before locks that are otherwise ready — for a line that (a) and (d) make redundant as evidence. Its substance is owed where S3 lives: **a self-test case that drives the comparison on the stub with a mismatched identifier and asserts the STOP**, declared here for p's next hash-moving BUILD if one ever comes (rule 11; none is pre-registered). Should p's package move for any other reason before the locks are committed, that case rides along and the equality print may too; the seat does not open a BUILD for them.

**The corrected sentence.** `gl:`§B.4 item 7 now reads: *Stands as a declared test gap. The live comparison runs at every non-stub recorded run and prints only on a mismatch. The record of its substance is (a) respawn (ii)'s identifier beside the lock's line in the precheck ×3 raw at `campaign`, and (d) the campaign report's `identity.backend_identifier` against the lock's line in each campaign raw after each invocation ends, the identifier only; a mismatch in either is a STOP for the seat. A self-test driving the comparison on the stub is owed at p's next hash-moving BUILD.* The seat's rule that a committed raw is not edited holds; this raw is the correction, and the pod session's close line on `gl:`'s entry quotes it.

## 2. The order from here

1. On the PI's word releasing the hold: place the three amended drafts byte for byte as `LOCK-p-OLMo-{ckpt}.md`; commit by path with their v1.0 entries naming `fafb786d…2bc4`, `25c52f56…3dcf`, `f71c97c1…0e67`; the dry precheck already CLEAR ×3 on these bytes (`bd8808c`), nothing re-runs.
2. The replacement pod on the PI's go (the spec of record): respawn (i) INTEGRITY, (ii) BACKEND → `641ee466f4553b6a` → the dated note in RESULTS.md on the v1.0 entries (`gl:`§B.3); a differing identifier → STOP.
3. The box repo by bundle; precheck ×3 at `campaign` with (a)'s line; the three campaigns at 2 h each, one pod session, looks every 40; (d)'s line in each campaign raw after each invocation; the seat adjudicates every pause on the excerpt.
4. No BUILD, no re-run, no new draft, no second read.

## 3. Routing block for the PI (defaults in brackets; your words are the record)

**File placed untracked on the laptop:** `results/raw/2026-11-14_p-backend-line_design-to-code_answers.md` — sha256 and bytes in the paste block.

**B. p (pod session)**
1. Item 7's line is (a) + (d), as §1; (b) and (c) declined; the S3 self-test declared for p's next hash-moving BUILD, none opened now [as ruled].
2. **Your hold:** release it, so the three amended drafts are placed and committed by path now with their v1.0 entries [release — "Place the locks"].
3. A close line on `bd8808c`'s entry and on `gl:`'s (`cdccc66`) citing this file; ledger (69) in the latter.
4. Then the pod on your go, respawn (i)/(ii), precheck ×3 with (a)'s line, the campaigns [go at your timing].

**C. Coordinating session** — nothing new; the hold's release recorded in your words.

**D. Push** — unchanged: HEAD `bd8808c`, origin `16c99d5`; the pre-push screen before any push [not pushed].
