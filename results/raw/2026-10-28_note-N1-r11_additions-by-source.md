# note-N1 round 11 — the two enumerations the seat owed: "every A0 figure" and "the restored figures", located in the posted text with their sources

- Design seat, 2026-10-28. Answers Code's `results/raw/2026-10-27_note-code-to-design_release-block-questions.md` §4e (`268787f`): the 10-23 handoff's list named these two groups as categories; this file enumerates them. Lookup only — no analysis; no note sentence or figure changes; no RESULTS entry.
- The text: `RESEARCH-NOTE-v0_8-draft.md` at the root, commit `0de15a1` (sha256 `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d`, 63,299 bytes, 258 lines) — the text as posted on 2026-10-27, with the fallback paragraph. "Line" below is that file's line; "§" is the note's own section or footnote.
- Method: every unit of the two lists in the 10-23 handoff (the seat's, untracked, D4) was searched in the v0.8 text by pattern (Unicode forms included: `−`, `≈`, `×`, superscripts, italic `*p*`); each hit was read in its sentence. For the restored figures, the same unit was searched in `RESEARCH-NOTE-v0_6-draft.md` at tag `note-2026-10-v1` and in the v0.6 ledger `results/raw/2026-10-12_note-N1-v0_6-claims-ledger.md` (its `quoted` and `computed` columns). Ledger row ids below come from that pattern match; Code re-keys from the row, not from this file. In a ledger citation, the `:NN` after a row id is the ledger's own second column — the line of `AUDIT-note-release-v1_2.md@bbc9ffe` the row answers — not a line of v0.6 or of the ledger file. Where the v0.6 ledger has no row, the item raw or the record line is given.
- Record line numbers for `RESULTS.md` are at `0de15a1`. The Q-F0 VERDICTS entry occupies lines 24–405 there; it was introduced at `0fa8539` and its close line appended at `79d462b`, so the same lines sit a few rows lower at `0fa8539` than at `79d462b`/`0de15a1`. N1 pins by commit (block-questions §4a, route (a)); the pin is Code's.

## 1. Every A0 figure in the posted text

The told positive control (PROPOSAL-m Q-F0, arm A0 with its sham A0s). Every figure below postdates N1's record pin `bbc9ffe`; carriers: `RESULTS.md` (the VERDICTS entry), `results/raw/2026-10-19_m-verdicts-qf0.txt` and `data/m/verdicts/Q-F0_VERDICTS.json` (both at `bfc179c`), `results/raw/2026-10-19_m-verdicts-qf0-entry_extractions.txt` (`0fa8539`), and for the design sentences PROPOSAL-m v1.11 and LOCK-m-F0 v1.0 (`d474406`).

| # | Unit, as it reads in v0.8 | Line · § | Carrier at the record |
|---|---|---|---|
| 1 | "79 of 80 first choices went to the label described as clean" | 17 · TL;DR, the Choice Cells bullet | `RESULTS.md:25` ("P = 79/80"); `:112`; `2026-10-19_m-verdicts-qf0.txt@bfc179c:887` |
| 2 | "Δ = +0.49" (rounded form of +0.4875; pass 14) | 17 · TL;DR | `RESULTS.md:25`, `:112`, `:138` (+0.4875) |
| 3 | "the sham bounds of 0.06" (rounded form of 0.0625; pass 14) | 17 · TL;DR | `RESULTS.md:26`, `:113`, `:148` (E = 0.0625) |
| 4 | "*p* < 10⁻²²" (derived from 81/2⁸⁰ ≈ 6.70 × 10⁻²³) | 17 · TL;DR | `RESULTS.md:122` ("p = 81/2^80 ≈ 6.70 × 10^-23"); `2026-10-19_m-verdicts-qf0-entry_extractions.txt:69` |
| 5 | "a pre-registered α = .01" | 17 · TL;DR; also 161 (§5.2, "the pre-registered α of .01") | `RESULTS.md:115` ("…< .01"); LOCK-m-F0 v1.0 (the A0 criterion) |
| 6 | "six consequential free choices" | 159 · §5.2 | PROPOSAL-m v1.11 §2.5 (`N_FREE = 6`, e2a's templates; file line 172) |
| 7 | "alternating forced-phase" | 159 · §5.2 | PROPOSAL-m v1.11 §2.5 (file line 174: "e2a's alternating forced order (A B A B, start counterbalanced)") |
| 8 | "every corrupted item changes at least three letters" | 159 · §5.2; also 250 (‖(b), "changes at least three letters of every item") | `RESULTS.md:183` (the §7.5 sentence of record, quoting G-CAL, `data/m/gates/G-CAL_model-free.json`) |
| 9 | "two truthful lines in the session banner" | 159 · §5.2; 17 · TL;DR ("two truthful banner lines") | PROPOSAL-m v1.11 §2.5 (the A0 banner lines) and §0.5 (every banner line true under the session's map and arm) |
| 10 | "Of 94 sessions launched in the told arm" | 161 · §5.2 | `RESULTS.md:111–112` ("n = 80 domain sessions of 94 launched"); `:150` ("on 94 and 35 launches") |
| 11 | "80 reached a first choice with no exclusion-bearing event before it" | 161 · §5.2 | `RESULTS.md:112` (80 domain sessions); `:150` (A0 80 at its floor) |
| 12 | "79 of the 80 chose the label described as clean" | 161 · §5.2 | `RESULTS.md:25`, `:112` (P = 79/80 = 0.9875) |
| 13 | "Δ = +0.4875" | 161 · §5.2 | `RESULTS.md:25`, `:112`, `:120` (= 39/80), `:138` |
| 14 | "sham bounds of 0.0625" | 161 · §5.2; 256 (¶¶(c), "the bounds of 0.0625") | `RESULTS.md:26`, `:113`, `:120` (E = 0.0625 = 1/16), `:148` |
| 15 | "two-sided Clopper–Pearson 95% CI on Δ from +0.4323 to +0.4997" | 161 · §5.2 | `RESULTS.md:26`, `:113`, `:138`; `2026-10-19_m-verdicts-qf0.txt@bfc179c:887` |
| 16 | "40 of 41 on one label-to-property map and 39 of 39 on the other" | 161 · §5.2 | `RESULTS.md:112`, `:121` (map 0 40/41 = 0.9756, map 1 39/39 = 1.0000), `:129` |
| 17 | "exact one-sided binomial *p* = 81/2⁸⁰ ≈ 7 × 10⁻²³" | 161 · §5.2 | `RESULTS.md:26`, `:122` (the only carrier of the fraction in prose); `Q-F0_VERDICTS.json@bfc179c:52, :1846` (`"exact": "81/1208925819614629174706176"`; line 1589 is a different p, the absolute exclusion guard's); extractions raw `:69` (= 6.700e-23) |
| 18 | "(0.000, Link 5)" — the clean-versus-corrupted contrast's Δ | 165 · §5.3 | f1 CORR of record (v0.6 ledger, the Link 5 f1 table rows); not an A0 figure, listed because the §5 passage carries it |
| 19 | "Δ = +0.035" (the transcript cell, restated in §5.3) | 165 · §5.3; 125 · Link 5 | e2a correction of record — see §2 row 25 below |
| 20 | "The corruption dose was calibrated by a legibility read and a completability check, both pre-registered" | 256 · ¶¶(a) | LOCK-m-F0 v1.0 §3.7 (condition (4), completability, `data/m/gates/G-CAL_completability_qwen.json`); the G-CAL legibility read (`data/m/gates/G-CAL_model-free.json`; `RESULTS.md` G-CAL entries) |
| 21 | "Fourteen small differences between this harness and the archived cells', none touching the read, are listed in the repository" | 256 · ¶¶(b) | PROPOSAL-m v1.11 §2.7 ("the fourteen-item F0m-vs-f1 list", file lines 86, 136, 267); `RESULTS.md:4905` ("§2.7's fourteen"). **Not** the 14 PIN sites of the campaign wiring (`RESULTS.md:310`) — a different fourteen. |
| 22 | "The sham arm chose its first label in 18 of 32 (0.5625)" | 256 · ¶¶(c) | `RESULTS.md:113`, `:128`, `:147–148` (18/32, P_sham = 0.5625, map 0 8/17, map 1 10/15), `:427` |
| 23 | "Pre-pick exclusions were 14 of 94 in the told arm vs. 3 of 35 in the sham" | 256 · ¶¶(c) | `RESULTS.md:115` (14/94 = 0.1489; 3/35 = 0.0857), `:129`, `:144–145` |
| 24 | "one-sided Fisher *p* = .26" (0.2648 at two decimals) | 256 · ¶¶(c) | `RESULTS.md:116`, `:145` (Fisher one-sided p = 0.2648); `2026-10-19_m-verdicts-qf0.txt@bfc179c:887` |

**Units in the 10-23 handoff's A0 list that are not in the posted text** (N1 need not look for them; they were in the seat's A0 section draft and did not survive the PI's weaving and the breathing pass): "four looks" / the five looks; the floors as "80/32"; 4.6 h of the 40 h cap; power .878 at the floors; 0.9875 as a decimal (the text has 79 of 80); 2026-10-16 (the lock date); "fourteen" as the PIN-site count (see row 21). The launch counts 128/64 are also absent.

## 2. The restored figures

Figures that the PI's redraft of 2026-10-21 (`RESEARCH-NOTE-v0_7-draft vJD.md`) had dropped and the seat put back in pass 1 (2026-10-21, change-log items E08–E27) and pass 2, taken from the audited v0.6/v0.7 text. Every one is in v0.6 at `note-2026-10-v1` except the three scorer-corrected figures of row 11, which came in with passes 3–4 and are already on Code's list by source (block :32, "12/40 vs 7/44 (+0.14, *p* = .10)").

| # | Unit | v0.8 line · § | v0.6 line (at `note-2026-10-v1`) | v0.6 ledger row(s) / other source |
|---|---|---|---|---|
| 1 | π̂ = 0.0172 | 254 · ‡‡ | 58, 170 | L110 (:101, reproduced: 11/640 = 0.0171875) |
| 2 | 11 of 640 paired reads | 254 · ‡‡ | 58 | L110 |
| 3 | the 0.0735 bar | 254 · ‡‡ | 58, 170 | L111 (:101, reproduced) |
| 4 | first-pick habit 83.4% | 49 · §3 | 108, 156 | L079 (:57, reproduced: 156/187 = 0.8342) |
| 5 | 154/154 (the regression suite) | 214 · §9 | 175 | L087, L088 (:68, :70), L127, L128 (:107) — the ledger marks these "discrepant" against the block's stale "103/103" referent; the computed value in every row is 154/154, which is what the note carries (N1 watch-list W6 cleared in the freeze read) |
| 6 | Δ+ = +0.285 | 73 · Link 2 | 74 | L129 (:107, reproduced) |
| 7 | Δ− = −0.395 | 73 · Link 2 | 74 | L130 (:107, reproduced) |
| 8 | the bar 0.158 / −0.158 | 73 · Link 2 | 74 | L131 (:107, reproduced) |
| 9 | random direction at most \|Δ\| = 0.088 | 73 · Link 2 | 74 | L132 (:107) |
| 10 | base 0.431 (25 of 58 decidable) | 93 · Link 4 | 92 (0.431); the 25/58 fraction is new in v0.7 | L004, L015 (:30, :34, reproduced: 0.4310 = 25/58, below the 64/96 floor); L005 is the 58/96 row |
| 11 | 12/40 vs. 9/44, Δ = +0.095, *p* = .22 (SFT injected arm); the scorer-corrected 12/40 vs. 7/44 (+0.14, *p* = .10) | 99 · Link 4 ¶1 (12/40, 9/44, .22); 226 · ‡(a) (9/44 within 17/85); 232 · ‡(d) (12/40 vs. 7/44, +0.14, .10) | 98 (12/40, 9/44, .22) | L019 (12/40), L020 (9/44) (:34, reproduced); L034 (.22, :34, computed-new). The 7/44, +0.14, .10 forms: not in v0.6; passes 3–4 (block :32) |
| 12 | 14/32 (Qwen's own transcripts, the judge at chance) | 114 · Link 4 | 102 | no ledger row matched by this lookup; item raw `results/raw/2026-10-08_note-N4-e2a.md@09c3a8c:305` ("judge 14 of 32 AB trials"); `archive/RESULTS-cycles3-4.md:671` |
| 13 | the largest pseudo-Δ 0.152, a random-direction arm of 23 sessions | 248 · ¶(b) | 108 | L068 (:57, = 0.1522); `archive/RESULTS-cycles3-4.md:653` ("0.152 (random1, n=23; sham +0.014, random2 +0.045)") |
| 14 | the sham arm (37 sessions) Δ = +0.014 | 248 · ¶(b) | 108 | L067/L080/L083 (:57–:58, the arm sizes); +0.014 at `archive/RESULTS-cycles3-4.md:653` |
| 15 | a second random arm, 22 sessions | 248 · ¶(b) | 108 | L069/L080/L083 (:57–:58) |
| 16 | detects a first-choice shift of +0.13 (approach probability .63) with 80% power | 248 · ¶(c) | 108 | `results/raw/2026-10-08_note-N4-e2a.md@09c3a8c:487, :494` (MDE δ* = +0.1294 at 80% power); L078 (:57, the .63 — "discrepant -- cause" in the ledger: read the row) |
| 17 | the full pass rule approximately +0.16 to +0.19 | 248 · ¶(c) | 108 | `results/raw/2026-10-08_note-N4-e2a.md@09c3a8c:487` ("the full pass rule about +0.16 to +0.19") |
| 18 | the Wilson interval on the approach probability .44 to .63 | 248 · ¶(c) | 108, 111 | L077 (:57, quoted "≈ [.44, .64]"; reproduced at 2 dp under Clopper-Pearson or Wald per its note), L078 (:57, "Wilson on 55/102 gives it"; "discrepant -- cause" — read the row: the note now states Wilson and the n = 101 run); N4 raw `:487, :494` ("[.44, .63]" at n = 101) |
| 19 | the valid-*n* floor of 48 | 250 · ‖(a) | 111 | L092 (:98: "valid 47 of 56 declared, floor 48: below by 1 (FDBK 44 of 56, below by 4)") |
| 20 | 44 of 56 valid sessions (the verdict-line contrast) | 250 · ‖(a) | 111 | L092 (:98, reproduced) |
| 21 | corruption rate .12 | 250 · ‖(b) | — (v0.6 has it as "G-CAL 0.12 artifact") | L105 (:98, reproduced); `results/raw/2026-10-12_note-N1-v0_6-note-rows.json` (f1's corruptor at 0.12) |
| 22 | 2 of 16 items rendered unchanged | 250 · ‖(b) | — | L105 (:98: "items [1, 12] unchanged") |
| 23 | 40 of 306 corrupted-label rounds … across all 64 sessions | 250 · ‖(b) | — | L105 (:98: "40/306 Q rounds byte-clean over all 64 CORR sessions (forced 16/124, free 24/182)") |
| 24 | 16 of the 56 valid sessions saw one corrupted task rather than two | 250 · ‖(b) | 111 | L105 (:98) |
| 25 | the e2a figures: Δ = +0.035 (54/101 sessions), *p* = .275; the correction of record from 55 of 102, +0.039, *p* = .244 | 125 · Link 5 (54/101, +0.035, .275); 165 · §5.3 (+0.035); 248 · ¶(a) (55/102, +0.039, .244) | 27, 108 | L071 (:57, quoted "54 of 101 valid sessions"; its related line carries '54 of 101, Δ = +0.035, p = 0.275' — watch-list W7); L065 (:57, "state arm 55 of 102 → +0.0392"), L072 (:57, "+0.039"); the correction entry `RESULTS.md:11415, :11464–11465, :11518` ("55/102 → 54/101, p .244 → .275", FINDINGS-5 §3) |
| 26 | 1 of 24 rounds differed from the uncached path in the T-step check | 252 · †† | 136 | no v0.6 ledger row names the T-step check (the `/24` matches in the ledger, L125 and L158, are OLMo DPO map figures — a false match); record: `RESULTS.md:8884` ("the T-step checks at 0.10 / 0.20 found 23/24 and 22/24 rounds identical"), `:10041` (`data/e2d/tstep_check_f010.json`, 23/24 identical); the artifact `data/e2d/tstep_check_f010.json` |

Also in ‖(c), from v0.6 and in the ledger (not on the 10-23 list, listed so round 11 has the footnote whole): termination attempts ≈ 1% of rounds (0.8–2.0% by arm, the sham highest; post-hoc exact test *p* = .72) — L102 (:98; computed column: SOLV 1.28%, DIFF 0.79%, NOV 1.05%, CORR 1.51%, FDBK 1.19%, sham 1.99% — the note's "0.8–2.0% by arm, the sham arm highest"; the row is "discrepant -- cause" against v0.6's "≈ 1% by arm", which v0.8 no longer says) — and menu share .47–.58 — L103 (:98: SOLV 0.540, DIFF 0.479, NOV 0.525, CORR 0.470, FDBK 0.576, sham 0.505); v0.6 line 111; watch-list W8 ("termination ≈ 1% with the by-arm range in ‖(c)") cleared in the freeze read. The .72 is not in L102's quoted or computed columns as matched here; round 11 reads the N5 raw (`results/raw/2026-10-08_note-N5-f1.md@09c3a8c:216–217`).

## 3. Additions after the block was written (passes 21–23, 2026-10-27)

Code's block (`2fb0cf0`, 15:51) lists additions through pass 19. After it:
- **Pass 21** (Gemini round 6) and **pass 22** (the PI's scrub): no new figure, no changed figure ("For N1: nothing", both entries). Wording changes only, including Link 3's four-sentence "Crucially" passage and the TL;DR item 3 clause ", consistent with a parity of the sign and the menu order".
- **Pass 23** (the fallback paragraph, N = 7): new ledger units — the hashes, the date and "twenty-five" from `results/raw/2026-10-08_note-N13-provenance.md` (the provenance table); "seven days" is the PI's choice of N on 2026-10-27 — the commit hashes `c54c4e0`, `1970b50`, `ea011bd`, `72b09a9`, `e9b5022`; the date 2026-08-20; "twenty-five rows"; "within seven days of this post" (lines 3 Foreword, 23 TL;DR last bullet, 214 §9). No figure changed.
- **The freeze read** (17:46) traced 271 numeral units: 192 shared with v0.6, 79 new since v0.6, three checked against the record directly (94 launches; 18/32 = 0.5625; the .12 corruptor rate) — all three are in the tables above.

## 4. Limits

Pattern matching finds the unit, not the claim: a row above says where a figure sits and where its source line is, not that the sentence around it is right — that is round 11's job. The ledger row ids were matched on the `quoted`/`computed` columns and may miss a row that writes the unit in another form (row 12 is one such miss); the v0.6 line numbers are from `git show note-2026-10-v1:RESEARCH-NOTE-v0_6-draft.md`. Nothing here was run through `scripts/audit_note_N1.py`.
