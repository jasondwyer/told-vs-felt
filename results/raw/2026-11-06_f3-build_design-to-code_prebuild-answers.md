# m package — BUILD (F3): the design seat's answers to Code's prebuild STOP (design seat → Code, through the PI)

*Design seat's raw, PI date 2026-11-06. Answers `results/raw/2026-11-06_f3-build_code-to-design_prebuild.md` (HEAD `24ebeae` at its write; `9cbacdb` at the push) item by item. `m:N` = PROPOSAL-m v1.11 at root; `A-m1` = ADDENDUM-m1 v0.1 (`f26bc59`). Every ruling here is the seat's; the one item that needs the PI's word is Q7, and it is routed beside this file. Nothing here moves a hash a lock names until the sequence of Q2 and Q3 says it may.*

## 0. The correction Code's §1 forces, owned

A-m1 called the OLMo units "build-complete" (§0.1, §0.4 at :16, §3 item 5 at :52). That held of §8 step 4's list and not of readiness: G-CAL-OLMo's tooling is not built (`gcal.py:39–40`) and the OLMo stages are not wired in the driver (`scripts/m_sessions.py:491–492`). Ledger (55), logged in PROPOSAL-n v0.2 §0.3: readiness is read from the driver's wiring and the gate tooling, named per stage, never from a module's presence. **The OLMo track's first node is therefore its own build** — G-CAL-OLMo (b3's banner and generation path) and the OLMo stage wiring — before `BACKEND — characterization`; the campaign hours of record (m:205–214) are unchanged by it; N9's double count of the 26 gate-stage sessions is accepted (the table already includes them).

## 1. Q1 — where Q-F3's code lives: (C2)

Adopted as Code recommends, with these terms fixed now so LOCK-m-F3 v0.1 can name them:
- A sibling package **`valence_core/mf3/`**, importing `valence_core.m`'s shared modules unchanged by import, never by copy: `corr`, `corrupt_m`, the audit's task-round classes, `bars`, the banner constants, `schedule`'s cells, `keys.stream`, `readout`. **It imports neither `stages` nor `gshape`** (both reach `runner_olmo`; `gshape` reaches `gcal`). Its own: scaffold (F2 block order, m:174; the reasoning-line seed before each menu order, m:159), runner with the reasoning block and the line classes (m:174, m:265), verifier, F3 read rules, bar table, stage drivers, G-SHAPE-F3, resume identity carrying the line cap (m:267), keys and source guard (m's `keys.py:66–67` and `guard.py:160–162` refusals stay as they are), and Q-F3's schedules under `data/mf3/schedules/` with their own manifest and self-tests.
- **A new driver, `scripts/mf3_sessions.py`.** `scripts/m_sessions.py` is a tooling file in G-SHAPE-F0's sources map (PIN-S10); the F3 build does not edit it, so G-SHAPE-F0 does not re-run on the F3 build's account.
- **Its licence (C2):** LOCK-m-F3 v0.1 names (a) `mf3`'s own `package_sha256`, computed as `resume.py:296–328` computes m's (every `*.py` directly in the package), and (b) the file sha256 of each `valence_core.m` module `mf3` imports, listed by name, closure-style. Every non-stub `mf3` stage checks both at start, as `stages.py:530–608` checks m's. At VERDICTS the analyzer's PIN-14 binds `valence_core.m`'s whole `package_sha256` as it does today; that is the reason for Q2's order, not a reason to change the licence.
- The analyzer's unit check (`m_analyze.py:1921`, `keys.UNITS_BUILT`) is G-ANL-F3's: the extended analyzer reads Q-F3's keys from `mf3`.

## 2. Q2 — sequencing: builds before locks, on both tracks

- **The OLMo build** (§0) lands in `valence_core/m` and `scripts/m_sessions.py`: m's own code at m's own step. It moves m's `package_sha256`; Code states in its BUILD entry which scoring-stack or tooling files it edits, and G-SHAPE-F0 re-runs iff one of them is in PIN-S10's map (the seat's clearance of subcommand-wiring driver edits stands). It lands **before `LOCK-m-OLMo-{ckpt} v0.1`**, so every OLMo lock names the final m hash.
- **The F3 build** (Q1) runs in parallel and touches no file a lock names. If the OLMo build edits a shared m module that `mf3` imports, that edit lands before `LOCK-m-F3 v0.1`; Code orders the two commits accordingly, and says so in the F3 BUILD entry.
- LOCK-m-F0 v1.0's `package_sha256` (`5f646db6…`) is Q-F0's record; Q-F0's VERDICTS ran, and `posting` records the three shas without refusing, so a moved package does not block the v1 posting.

## 3. Q3 — the analyzer: Code's reading confirmed, and the sequencing rule

- Confirmed: G-ANL-F3 extends `scripts/m_analyze.py` in place (m:292); each unit's analyzer of record stays the blob its own LOCK v1.0 hashes (PIN-14); the worktree path is declared and not implemented, and nothing below needs it.
- **The rule:** G-ANL-F3's in-place commit lands only when no OLMo unit is open — "open" from its LOCK v0.1 to its VERDICTS entry. Two orders are licensed, and which obtains is a fact of the calendar that Code records in the BUILD entry: **(a)** G-ANL-F3 before any `LOCK-m-OLMo v0.1` — the OLMo locks name the extended blob, and its battery carries A-m1 §2.5 (3)'s regression (`Q-F0_VERDICTS.json` and `Q-F0_secondary.json` byte for byte from the committed inputs, with N8's reading: the D_O-era declarations and their comparison date are left as they were) and asserts the OLMo v1 outputs unchanged; **(b)** the OLMo track completes through its VERDICTS on `655e0f7f…` first, and G-ANL-F3 lands after. The seat's recommendation if the pod is up before G-ANL-F3 is built: (b) — the pod is not held for the analyzer; the v1 posting's `posting` command, run later on the extended blob, takes the OLMo states as declared inputs either way (A-m1 §2.5 (2)).
- **The texts that ride in the round:** A-m1 §2.5's three items, and the text corrections the record had already assigned to "the next hash-moving round" before A-m1 (round 2's). A-m1's "No other change to the analyzer is licensed by this addendum" means no change not already assigned by the record; it revokes nothing. Code lists each riding text by its record anchor in the BUILD entry, and the seat confirms each by anchor before LOCK-m-F3 v0.1 names the blob.

## 4. Q4 — the scaffold-set review: Code's proposal adopted

Q-F3's scaffold set is e2a's by sha (m:261). The three strings from the VERDICTS read (`You are a helpful assistant.`, `4assistant`, `<|end|>`) each occurred in Q-F0's sessions, so they bind no hair trigger (rule 21); they are declared as one descriptive counter under rule 23 — tabulated over all sessions, excluded included, reported in VERDICTS, deciding nothing.

## 5. Q5 — G-TIME-F3's contrast reporting and the cap trigger

- **The cap trigger counts cap-reach over all six G-TIME-F3 sessions' reasoning lines** (≤ 36): m:174 and m:293's "counted over all six" agree, and #130's exception is not taken.
- **What m:271 withholds is content, not counts.** The contrast sessions' free rounds and their picks are withheld to VERDICTS; a per-line boolean (cap reached / not) carries no pick and is not withheld. So: the trigger's count includes the three contrast sessions' lines; the printed form of m:263 at this stage reports the three sham sessions' rounds and lines in full, and for the contrast sessions the forced rounds beside (#116) with the per-line cap booleans and no free-round text or pick. This fixes #87's missing forced-round scope for m:293 and m:297 by statement.
- #10 adopted: counter (c)'s blind read is performed after the analyzer's output exists and before the seat's full read.
- These four step-3 notes are now dispositioned by number; the rest of the 2026-10-06 notes stay as graded.

## 6. Q6 — the carry-overs addressed to "the next unit"

"The next unit" for a driver edit is **the OLMo wiring build**, the next edit of `scripts/m_sessions.py`: the `CHECKPOINT STATE INCONSISTENT` message and options O1-3, RM4-1 and O4-1; VC4-1 and VC4-2; the O2-3 listing commands for the README and the checklist. `scripts/mf3_sessions.py` is written to the same forms from the start, so Q-F3 carries them too. The weights-snapshot binding in the identity goes into each unit's identity at its own build: `mf3`'s at the F3 build, the OLMo identity at the wiring build. Nothing is deferred past a build that touches the file it belongs to.

## 7. Q7 — LOCK-m-F3 v1.0's preprint of record: for the PI's word (routed beside this file)

The seat proposes: LOCK-m-F3 v1.0 carries **"preprint of record pending"**, the OLMo locks' form (m:302); v2's sentence table (m:73) and the lock's hash of "the preprint of record as edited for v2" (m:298) are made at the Q-F3 VERDICTS session, which under (10′) follows `POSTING v1`, against the posted v1 text — the right referent for v2's rewrites. The PI confirms or replaces this in the next routing block; until then the lock chain runs to v0.2 and stops before v1.0 only if the posting has not occurred and the PI's word has not come.

## 8. Q8 — the PIN register, and the seat's rulings on the named items

The register as at Q-F0: Code's proposed reading for each open place goes into the build-design raw, is declared as Code's PIN at LOCK-m-F3 v0.1, is listed as a flag in the BUILD entry, and is strikable by the seat until LOCK v1.0 at the cost Code states. Rulings now on the seven items the raw names:
- **The reasoning-line echo:** a generated line echoes a harness line iff it contains that harness string as a substring after whitespace normalization — containment, since equality misses prefixed echoes; which harness lines count is the declared set of eight strings (m:258) plus the reasoning-block lines.
- **Cap reached without a newline:** the cap-length prefix is the line as generated, kept; it counts as cap-reach; the session continues under m:174's cap rule.
- **A scaffold fire on a reasoning line:** a reasoning line is round generation, so the scaffold ban applies as to any generation (rule 13); the fire is an exclusion event and ends the session at that point as the runner's first-exclusion rule has it for forced rounds; the guard's pre-pick count includes it.
- **Defects "by property":** the audit's property-keyed counters as Q-F0 ran them (m:314's "by property" = per lexical property of the content-class audit); no new keying.
- **G-ID-F3's index rule and its re-run:** as G-ID-F0m's (m:294); the line cap is an identity input, so a cap change re-runs G-ID-F3.
- **The "\n\n" after the reasoning segment:** the boundary is found on the untruncated encode by character offset (rule 28(d)(a)); the empty line and its double newline are part of the declared reasoning segment and the assertion is exact over it.
- **The build's scope:** m:361 names the first node; LOCK-m-F3 v0.1 needs keys, schedules, gate files and the bar table, and all are the F3 build's (as Q-F0's step 4 built its own); the BUILD entry lists every file.
The other twenty-four readings, and the declared check for the build hazard, are Code's PINs under the register's terms.

## 9. What Code does next

1. The F3 build in `valence_core/mf3/` and `scripts/mf3_sessions.py` under Q1; the OLMo build in `valence_core/m` and `scripts/m_sessions.py` under §0 and Q2; the BUILD entries name every file edited and the commit order; G-SHAPE-F0 re-runs iff Q2's condition holds.
2. G-SHAPE-F3 → G-ANL-F3 under Q3's rule → the lock chain to LOCK-m-F3 v0.2; v1.0 on Q7's word.
3. The OLMo track from its build, then `BACKEND — characterization` on the PI's go (runpod re-authorisation first), per checkpoint as m:302.
4. PROPOSAL-n v0.2's §8 after this block, in the routed order against the OLMo units; its `valence_core/n/` package takes Q1's placement and licence form.
