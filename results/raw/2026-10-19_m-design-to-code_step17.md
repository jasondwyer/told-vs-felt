# Step 17 — `PROPOSAL-m Q-F0 — VERDICTS`: the PI's word and the seat's block

*Design seat, 2026-10-19, v1.1 — replaces the uncommitted v1.0 of the same name: every path literal now resolves at `de6dfc5`; files Code will create are given by naming rule, not by path; nothing of substance moves. For the PI to route to a fresh Code session. Part 1 is the PI's word (his to edit); Part 2 is the seat's block, routed with it. Calendar dates only; the commit hash is the record. This file (the same name as v1.0) is placed untracked under `results/raw/` as the seat's blocks are, and committed by path by the PI.*

---

## Part 1 — the PI's word (for Code)

> Fresh session, on the laptop. `main` is at `de6dfc5` (the Q-F0 campaign's launch entry: COMPLETE, exit 0). `git status` first; the untracked drafts stay. Step 17 on my word: run the analyzer of record (`655e0f7f…c16f`) over the campaign checkpoint and the table of record, and write `PROPOSAL-m Q-F0 — VERDICTS` and `PROPOSAL-m Q-F0 — secondary DVs` as m:358 and LOCK v1.0 have them. The seat's block below carries its rulings on the launch entry and the content of the two declared inputs. Nothing in the driver, the package or the analyzer moves before VERDICTS. Commit the outputs, the inputs and the raw by path, then the two entries; the VERDICTS entry stays open at "the reads" and closes at the seat's read. On a refusal or a STOP, stop there and report the message; nothing is edited.

*(If the session runs in the cloud instead: Code pre-syncs — `git fetch origin main && git merge --ff-only origin/main` — pushes to `main-882qqu`, and the PI's loop brings it to `main` before any seat file is committed. The analyzer is model-free; either site serves.)*

---

## Part 2 — the seat's block

### 1. Preconditions (reported in the raw; a departure STOPs before the run)

- HEAD `de6dfc5`, `main == origin/main`, no tracked change. Since `a6c81f2` only the campaign's own outputs landed (`de6dfc5`).
- The three hashes PIN-14 reads, at HEAD with identical working-tree bytes, each named in full in LOCK v1.0 §1: the analyzer `scripts/m_analyze.py` `655e0f7f6743d0bf497f5ba97ce37f7febf9fcf6a45e068b5385ee945c5dc16f`; `package_sha256` (the 18 files under `valence_core/m/`) `5f646db6e82c5561ff8a425e91beb5454068a381564894e93d19b9165459d771`; the closure `a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b`.
- The two PIN-40 reads, each named in full in v1.0 §2: the table of record `data/m/gates/m_posting_sentences.json` `af5cb81622f4af74d57c4b708d6ede82d5895cd7dd6a623f6b4bccbaebd1f902` (`kind` `of-record`; `table_problems` `[]`), and its preprint `PREPRINT-v1_0-draft.md` `45b67246f2b2bcb40774e95462ad4e3c5f559fdd0358387cceec0155bebe7a41`.
- PIN-31: the proposal at root is the pinned v1.11, `PROPOSAL-m-gating-campaign-v1_11.md` `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b` (the seat re-hashed it on its clone of `de6dfc5`).
- The lock `LOCK-m-F0.md` `fc7e9db8ecfa28d61b1ce1765d869000fbf827dcb013cd1d65220c9e85e0015c`, which V2 asserts equal to the campaign identity's `lock_sha256`.
- The campaign checkpoint `data/m/ckpt/Q-F0_campaign.json` as committed at `de6dfc5` — hashed there, opened by no one: ended COMPLETE; no end pending; `pauses` `[]`; `stop` null; an end look at 129 = the launches recorded (PIN-46), silent, so PIN-45's pause rule is not engaged; floors 80 and 32 recorded. Its sha256 in the analyzer's `inputs` equals the launch entry's.
- The gate checkpoints `data/m/ckpt/Q-F0_time.json` and `data/m/ckpt/Q-F0_qual.json`: ended `Q-F0/time` and `Q-F0/qual`. (G-ID's `data/m/ckpt/Q-F0_id.json` is not an input: its sham-only sessions were read in full at G-ID and are not re-reported, PIN-32.)
- The flag source `data/m/gates/G-CAL_model-free.json`, committed (PIN-19).
- The analyzer's own battery first: `python scripts/m_analyze.py --selftest`, exit 0, in the jlens venv as the campaign's self-test of record ran; write-free (PIN-29); its tally in the raw.

### 2. The two declared inputs — the seat's content; Code writes the files and commits them by path

**(a) `--olmo-states`**, schema `m-olmo-states-v1`. Every OLMo checkpoint is PENDING: no VERDICTS entry, not NOT-RUN, unlocked, no pod started, D_O = 2026-10-30 not passed (PIN-6: a declared input, recorded as given; the boundary day is C7's — D_O inclusive to 23:59:59 UTC).

```json
{"schema": "m-olmo-states-v1",
 "states": {
  "OLMo-sft":      {"state": "PENDING", "substate": "unlocked-before-D_O", "clock_passed": false, "date": "YYYY-MM-DD"},
  "OLMo-dpo":      {"state": "PENDING", "substate": "unlocked-before-D_O", "clock_passed": false, "date": "YYYY-MM-DD"},
  "OLMo-instruct": {"state": "PENDING", "substate": "unlocked-before-D_O", "clock_passed": false, "date": "YYYY-MM-DD"}}}
```

Before writing, Code replaces each `YYYY-MM-DD` with the UTC calendar date on which it makes the Clock comparison (its `date -u`), the same in all three. Exactly these four keys per state.

**(b) `--decisions`**, schema `m-decisions-v1`. No decision about Q-F0 was taken with another unit's outcome known — no other unit has one (m:318):

```json
{"schema": "m-decisions-v1", "unit": "Q-F0", "decisions_with_other_outcomes_known": []}
```

**Homes and names:** beside the outputs, in the directory PIN-25 names for them (`scripts/m_analyze.py:95`, `VERDICTS_REL`; `scripts/m_analyze.py:1798–1803`). Code names the two files in the record's form — the unit, then what the file is — and the analyzer records each one's path and sha256 in the output, so the names are Code's and need no declaration here.

### 3. The run

One invocation, in the jlens venv, from the repository root; stdout to a raw under `results/raw/`, dated by Code's `date -u` and named as the campaign's raws are (m-verdicts-qf0):

`python scripts/m_analyze.py verdicts --unit Q-F0 --lock LOCK-m-F0.md --sentences data/m/gates/m_posting_sentences.json`, plus `--decisions` and `--olmo-states`, each given the file Code wrote at §2.

The other arguments at their defaults: `--campaign` `data/m/ckpt/Q-F0_campaign.json`, `--time` `data/m/ckpt/Q-F0_time.json`, `--qual` `data/m/ckpt/Q-F0_qual.json`, `--flag-source` `data/m/gates/G-CAL_model-free.json`, `--out` PIN-25's directory. No `--adjudication` (no pause exists; PIN-9 refuses one given) and no `--pi-stop` (the end is COMPLETE; PIN-8 refuses one given). The gate line prints first (V0, m:267). Exit codes (PIN-26, `scripts/m_analyze.py:8165–8177`): 0 — the unit's VERDICTS and secondary outputs, named as PIN-25 names them, written once (PIN-37); 2 — refused before any pick-bearing byte is interpreted, nothing written; 4 — STOP (V4's content assertions, or COMPLETE with an arm below floor), nothing written. A 2 or a 4 comes to the seat with its message and the raw as it stands.

The analyzer's stdout prints the §5 sentence (its `VERDICTS Q-F0:` line); from that line the pre-VERDICTS window is closed (m:271) and the verdict word may appear in the entries and the commit messages.

### 4. What is committed, by path, in this order

1. One commit: the `.gitignore` admit block for the outputs' directory (PIN-25 defers it to the commit that first writes there; the `data/m/gates/` pattern), the two outputs, the two declared inputs, the raw.
2. One commit: the two entries, newest first, with their values-check raw in the campaign entry's form (two passes of three lenses, each with a strict refuter, Code's dispositions): `PROPOSAL-m Q-F0 — VERDICTS` and `PROPOSAL-m Q-F0 — secondary DVs` (issuing no claim; secondaries (a), (b), (d), (e) per PIN-13; (c) and (f) are Q-F3's).

### 5. The VERDICTS entry's contents (m:358 with the lock's additions), written for the seat

- **A0 with its §5 sentence** (PIN-4's clauses in order): the verdict word; (i)–(iii) against E and the bar at α .01 (`rates`, `tests`: every rate with its domain, every p with its test — PIN-2's exact forms); Δ_c with its Clopper–Pearson interval; the attained power of record at the realised n (PIN-3); the arm's pre-pick exclusion rate beside A0s's with the guard's result at the last look (m:316).
- **The unit outcome:** ANALYZED, COMPLETE at floors (80/32 on 94/35 launches), the cap not reached.
- **§7's v1 outputs** from the output's `v1_outputs`, under the tuple (A0's state; PENDING ×3): L0; the labels for e2a and f1 as m:338 words them (Step 2's texts, not v8's :176/:184 wording — a posting-time rewrite by row id, per the step-15b answers' "Two notes for the PI, not the table"); the ceiling (Fallback-1 iff L0, else Fallback-2); the abstract OLMo clause (PIN-27, verbatim; with no OLMo stage passing it is the "concluded, not answered (§5.5)" clause); the §8.1 status text (PIN-17: A0's outcome; the three OLMo controls pending); Step 7 "open"; the dose note under the flag of record; **the §7.5 enumeration of record** over the table of record, values-checked, by row id, with its clause ((a)/(b)/(c)) per row. The all-PASS tuple's 23 items (v1.0 §2) are not this tuple's expectation; the entry states the count obtained.
- **Counters by property** (rule 23; over all sessions, excluded included; the output's `counters` and `counter_rates`) and **the per-property exclusion table** (VERDICTS-only; the pre-pick column is f1's 7-vs-1 column, C7, with `sessions_excluded_any_phase` beside).
- **The release** (m:271; V3, `readrule.release_full`, `valence_core/m/readrule.py:799`): the G-TIME-F0 A0 session's picks and the 8 G-F0m-Qwen A0 sessions' picks, by role, with their released free-round events (PIN-32, `gate_release`), tabulated apart from the counters of record; the campaign's A0 picks are the analysis itself; the sham first-pick share (the campaign reported none, m:318); the contrast sessions' seconds and the stage durations (Code's PIN at `valence_core/m/stages.py:2390`), reportable now; the A0 reads after the first, withheld at the looks (`valence_core/m/stages.py:1936`), now counted.
- **The looks** (`every_look`) and **the guard at the last look**, as the campaign entry printed them, now with the contrast side filled in.
- **Any `CHECKPOINT STATE INCONSISTENT` line:** none printed in the campaign raw (the launch entry); a V2/V4 finding against the checkpoint is a refusal or STOP and comes to the seat sealed (the step-14 read's Q3).
- **The seat's rulings of §7 below,** quoted.
- **"The reads"** (m:318): the seat's — §6. The entry carries the item open and closes at the seat's read, as the G-F0m-Qwen entry closed at `5af9e07`.

### 6. The reads — the seat's VERDICTS read, in this order (the seat's own discipline)

After the analyzer's output exists (m:318), the PI routes the entry. The seat reads: (1) A0's verdict against its bar and the §5 sentence; (2) the A0s sham figures; (3) the §7 v1 outputs — the labels, the ceiling, the abstract clause, §8.1's text, the enumeration; (4) then the contrast side — the per-property table, the counters by property, the gate stages' contrast picks and released events, the seconds; (5) **the full unredacted read of every session of the unit** from the checkpoints as committed: 129 campaign (94 A0, 35 A0s), the 2 G-TIME-F0 and the 24 G-F0m-Qwen — 155 sessions (G-ID's 2 were read in full at G-ID, PIN-32) — the attractor tally on the contrast forced rounds carried forward and the free rounds now counted. The seat records the read as a dated file under `results/raw/`, named as its reads are (m-design-to-code, VERDICTS read); the PI places it untracked and commits it by path; Code adds the entry's close line. That closes the rule-25 window (m:271).

### 7. Rulings on the launch entry (`de6dfc5`) — the seat's, for the VERDICTS entry to quote

- **The two disclosures** — the second `kill -0` on the PID, and the session kept open for the end-wait — **accepted, inert:** neither read a figure or a raw, the open session made no commit, and the end-wait was the README's §2's. No strike.
- **The 14 PIN sites** of the campaign wiring (`scripts/m_sessions.py:529` to `:1286`, as the launch entry lists them), closed at the launch entry with no strike (v1.0 §8): stands.
- **O1-3, RM4-1 and O4-1** (not built; flagged with Q3's package message): the next unit's driver edit, not step 17's. Nothing in the driver, the package or the analyzer moves before VERDICTS — PIN-14 binds the three hashes to the lock's text, and a moved hash is a refusal.
- **The `posting` command** (`posting --posting v1`; PIN-44's bar; the rewrite list by row id; PIN-23's tuple file) is step 18's, run on the posted text at the v1 posting. It is not run now; no dry run is needed — the VERDICTS output already carries the enumeration of record.

### 8. What comes back to the seat, through the PI

The two entries (the VERDICTS entry open at "the reads"), the raw, and the paths and sha256s of the two outputs and the two inputs. On a refusal or a STOP: the message and the raw as it stands, nothing else.
