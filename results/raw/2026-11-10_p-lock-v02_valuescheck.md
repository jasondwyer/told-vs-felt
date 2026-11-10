# PROPOSAL-p -- LOCK-p-OLMo-{sft,dpo,instruct} v0.2: blind values-check

*Code's raw, PI date 2026-11-10. A blind values-check of the three LOCK-p v0.2 files and their entry's draft, against the committed v0.1 texts, the seat's answers of 2026-11-09 and 2026-11-10, the list ruling v2, the PI's routing quoted in RESULTS.md, the G-TIME-OLMo (p) entry, PROPOSAL-m v1.11 and PROPOSAL-p v0.2, and `stage.lock_required` recomputed on the committed code (HEAD `ba89279`). 118 claims: 104 CONFIRMED, 4 IMPRECISE, 0 FAIL, 10 NOT CHECKABLE. The four were applied before the commit:

- Each lock's header now cites m:302 in PROPOSAL-m v1.11's words, "(acceptance; projections)", with the seat's phrase given as the seat's. That moved each file's sha256 from the one checked here. Each committed file differs from the checked file in that one header line alone (by diff). The re-generation re-ran the generator's own checks, and Code re-ran the structural ones, by tool, not by a second blind pass.
- The entry's §A bullet is reworded as the checker suggests.

The checker's observations on the seat's own text go to the seat in the entry, not adjudicated. Its disclosures are in its report below. The report is verbatim, its local paths scrubbed (`<repo>`, `<tmp>`) and its headings set one level down.*

## Blind values-check: LOCK-p-OLMo-{sft,dpo,instruct} v0.2 and their draft entry

**What was checked.** The checkout R is at HEAD `ba89279` (`ba892798e49c…`), with the three lock files modified and uncommitted (`git status --porcelain`: ` M` ×3). The files at check time:

- `LOCK-p-OLMo-sft.md` `4ab66e27…5b3e`
- `LOCK-p-OLMo-dpo.md` `bc049a5a…f9b7`
- `LOCK-p-OLMo-instruct.md` `145f0a6f…b082`
- the draft entry (`qualbuild/entry_lock_filled.md`, scratch) `20e08147…6a65`

I re-hashed all four after the last check, and none had changed.

### Totals

- CONFIRMED: 104
- IMPRECISE: 4
- FAIL: 0
- NOT CHECKABLE: 10

There were 118 claims in all: 28 per lock and 34 in the entry. No value is wrong. Every one of the 56 `lock_required` values matches in all three files, and the structure checks pass.

### Commands (the table's evidence cites them)

- **C1, `lock_required` recomputed.** One fresh interpreter per unit: `cd R && nice -n 19 R/jlens-qwen36/.venv/bin/python -I -B -c '<script>' OLMo-<ckpt>`.
  - The script calls `stage.lock_required(unit)`, then `stage.lock_names(text, v)` for every value, once over the whole file and once over §B alone. It also calls `stage.lock_backend(text)` and `stage.qual_lock_problems(unit, text)`, and parses §B's bullets, `LICENCE` lines and `REGISTER` lines against the dict that `lock_required` returned.
  - It printed the same for each of sft, dpo and instruct: `PROBLEMS 0 []`; `N 56`; `not named in file: []`; `not named in B: []`; `lock_backend: ([], '641ee466f4553b6a')`; `qual_lock_problems: []`; `B bullets 29 req bullets 29 keys equal True values equal True`; `bullet order equal True`; `LICENCE lines in B 19 req 19 equal in order True`; `REGISTER lines in B 8 req 8 equal in order True`.
- **C2, the files' digests.**
  - `shasum -a 256` on the three locks gave `4ab66e275afa27b64849edf7aa99c290ba2572700e7b2a558bc5d10548c05b3e`, `bc049a5a2da2561cf8b3d2b8ce0885bb64c1f8c692d0d71e9444bc72b96ff9b7` and `145f0a6fd91e40485cb2ce69be40eac3acb5ef66efa49f3729cf8da91933b082`. Each equals the value the draft entry gives.
  - `git check-attr -a` on each file printed nothing, so no attribute or filter applies to them.
- **C3, structure.**
  - The superseding line: `grep -c -x '<the superseding line>'` gave 1 in each file, at line 94. Line 92 is `---`; lines 93 and 95 are blank.
  - The v0.1 text: `cmp <(git show HEAD:LOCK-p-OLMo-<ckpt>.md) <(tail -n +96 LOCK-p-OLMo-<ckpt>.md)` found the two identical for all three files.
  - The HEAD blobs' sha256 are `9cc9045a…39ae`, `efcba384…5aba` and `c03a1ef9…5cbd`. These are the v0.1 entry's values (RESULTS.md:904–906).
  - `git log --format='%h %cd %s'` on each lock lists only `0afd842` (v0.1).
  - The backend line: `grep -n 'BACKEND OF RECORD'` found one line per file (sft :109, dpo :108, instruct :108). It reads `BACKEND OF RECORD 641ee466f4553b6a` and sits inside the v0.1 text.
  - The acceptance line: `grep -n -E` for any checkpoint's line found only the file's own, at line 10, indented 3 spaces as a continuation of item 1.
- **C4, §A against the seat's §2, line by line (python).**
  - Items 1–6 and 8 are byte-equal in all three files.
  - Item 7 differs. Split into head, pointer, rule and tail, the head and the rule are equal (True ×3).
  - Pointer. The seat has "closing the gap the O2-3 sweep found, the seat's sweep ruling of 2026-11-09 §2". The lock has "the p answers' §2 item 7, now pointing at the list of record v2, `results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md`, sha256 `6c1135f5…`, which supersedes the sweeps ruling's §2".
  - Tail. The seat has "sweep ruling's list."; the lock has "list of record's (v2, §2)."
- **C5, quotes (python substring tests on the committed sources).**
  - The header's `m:302's "LOCK-m-OLMo v0.2: projections; OLMo port acceptance", written for p` is in the seat's 2026-11-09 §2 lead-in.
  - The header's "... → LOCK-p v0.2 ×3 → G-F0m-OLMo (p) ×3 on the box, batched → STOP for the seat's read [go]" is in B1 (RESULTS.md:482) after the ellipsis.
  - B3 (RESULTS.md:484) ends "[adopted].".
  - Item 5's "(j)'s fix — a fresh-interpreter closure for p's drift check — lands with this move" is in the 2026-11-10 answers' §1.
  - The entry's B3 quote equals RESULTS.md:484 without its `- B3. ` list prefix (True).
  - The entry's superseding-line quote, with its line wrap removed, equals line 94 of each lock (True ×3).
  - B1 contains "LOCK-p v0.2 ×3" (True).
- **C6, the cited raws.** I hashed each working file and `git show HEAD:<raw>`, and ran `git log --format='%h %cd %s' -- <raw>`. In all three cases the working file equals the HEAD blob.

  | raw | sha256 | committed at |
  |---|---|---|
  | `2026-11-09_p-gtime_design-to-code_answers.md` | `7b8b1d5f…adc3` | `e619d3d` |
  | `2026-11-10_p-qual-wiring_design-to-code_answers.md` | `e20bca13…23a9` | `42c5a92` |
  | `2026-11-10_list-of-record-v2_design-to-code_answers.md` | `6c1135f5…6cdd` | `fc43249` |

  - The seat's §1.4 says "PASS ×3 stand".
  - The list ruling's §2 heading says "supersedes the sweeps ruling of 2026-11-09 §2 in full". Its line 28 says "LOCK-m-F3 v0.1's re-issue and LOCK-p v0.2 cite it in one line each, in place of the sweeps ruling's §2".
  - The 2026-11-10 §3 says "The list of record is cited in one line (the p answers' §2 item 7, now pointing at the list's v2)".
- **C7, the G-TIME entry as committed** (`git show 2258c52:RESULTS.md`, the entry's table):

  | ckpt | sham bar | pause | contrast forced rounds | sham proxy | sham seconds |
  |---|---|---|---|---|---|
  | sft | 0/10 | silent | 4, not excluded; control chars 0 | 10/10 attributed, 0 cuts | 3.528 |
  | dpo | 0/10 | silent | 4, not excluded; control chars 0 | 10/10, 0 cuts | 3.972 |
  | instruct | 0/10 | silent | 4, not excluded; control chars 0 | 10/10, 0 cuts | 5.289 |

  The seat's §1.3 has "control characters 0 of 4 each".
- **C8, the projections (python).**
  - (n + 26) × basis / 3600 gives:

    | basis | n = 160 | n = 192 | n = 224 |
    |---|---|---|---|
    | 22.7 s | 1.17283 h | 1.37461 h | 1.57639 h |
    | 19.5 s | 1.00750 h | 1.18083 h | 1.35417 h |

  - The three campaigns together (one checkpoint at 19.5 s, two at 22.7 s) come to 3.3532, 3.9301 and 4.5069 h.
  - Sources:
    - PROPOSAL-m v1.11 (sha256 `42ab36ec…`, the F-p8 pin). Line 205: "OLMo basis 19.5 s per session at instruct and 22.7 s at SFT/DPO … applied to the unit's total + 26 sessions per checkpoint (24 qualification + 2 timing)". Lines 209–211: OLMo hours 1.0/1.2, 1.2/1.4 and 1.4/1.6 at 160/192/224. Line 214: "≈ 3.4/3.9/4.5 h".
    - PROPOSAL-p v0.2 §6.1: "≈ 3.4/3.9/4.5 h for the three at 160/192/224 sessions … The budget is 12 h".
    - Wall clocks, from the stamps in `results/raw/2026-11-09_p-gtime.txt` (lines 26–31: 18:10:46 → 18:14:31 → 18:18:16 → 18:22:04): 225, 225 and 228 s.
    - `stage.COUNTS["time"] = (1, 1)`: one sham session per checkpoint.
- **C9, the commits.**
  - `git log --format='%h %p %s'`:
    - `ba89279` (parent `f5e695c`) is G-ANL-p's re-run;
    - `f5e695c` (parent `40086e8`) is G-SHAPE-p's re-run;
    - `40086e8` (parent `7589c1d`) is the qual wiring's BUILD.
  - `git show --name-status`:
    - `40086e8` changes `scripts/p_sessions.py` and `valence_core/p/stage.py`;
    - `f5e695c` changes `data/p/gates/G-SHAPE-p.json`;
    - `ba89279` changes `data/p/gates/G-ANL-p.json`.
  - `git diff --name-status 40086e8 HEAD -- valence_core scripts` is empty: no code has changed since the BUILD.
  - Digests at each commit (`git show <rev>:<path> | shasum`; the HEAD blobs compared with `git rev-parse` and found equal):
    - G-SHAPE-p is `f8d22109…631f` at `f5e695c`; before it, at `40086e8`, it was `3c4125a3…`, v0.1's value.
    - G-ANL-p is `90d0d5d6…8f2e` at `ba89279`; before it, at `f5e695c`, it was `6440468b…`, v0.1's value.
    - The driver is `89551017…af44` at `40086e8`; at its parent it was `d91e41e1…`, v0.1's value.
- **C10, FLAG (j)'s fix.**
  - At `40086e8`, `git grep -n … 40086e8 -- valence_core/p/stage.py` finds `:300 def fresh_import_closure` and `:361 _drift(rel, "import closure", fresh_import_closure(), …)`.
  - At `7589c1d`, `fresh_import_closure` is absent (`git grep -c` exits 1), and line 226 used `gshape.import_closure(committed=True)`.
  - stage.py:282–336: the child process is `sys.executable -I -B -c _CLOSURE_CODE`. It imports `scripts/p_sessions.py` by path and reports the `valence_core` modules it loaded.
- **C11, code read** (stage.py at HEAD, which is the same as at `40086e8`).
  - `precheck` (:511–583):
    - reads the lock through `m_stages._committed(lock_rel(unit))`: the HEAD blob, with the working tree identical to it;
    - checks `lock_names` for every `lock_required` value, and `lock_backend`;
    - at `qual`, also runs `qual_lock_problems`;
    - refuses to run without the pod id ("POD ID ABSENT").
  - `GATES = ("time", "qual")`. Any other gate is refused; the campaign is "its own move before LOCK-p v1.0".
  - `identity_extra` (:481–490) sets `lock_sha256` to the sha256 of those committed bytes.
  - `qual_lock_problems` (:472–479) compares `ln.strip()` with `QUAL_LOCK_LINE`, which is m's `OLMO_QUAL_LOCK_LINE` (scripts/m_sessions.py:680).
- **C12, the m:302 phrases.**
  - `git grep -n -F 'projections; OLMo port acceptance' HEAD -- . ':!data/**'` finds the phrase only in:
    - archive PROPOSAL-m v1.6:102 and v1.7:109;
    - a 2026-10-04 raw;
    - the seat's answers, line 21.
  - `grep -c -F "verifier's acceptance of the runner"` gives 0 in PROPOSAL-m v1.8, v1.9, v1.10 and v1.11. The phrase appears at v1.6:99 and v1.7:107.
  - v1.11:302 reads "→ **LOCK-m-OLMo-{ckpt} v0.2** (acceptance; projections)" and "port acceptance recorded at v0.2".
  - v1.11:54 reads "**OLMo port acceptance** = the F0m-OLMo verifier plus the seat's read …".
- **C13, item 8's carry-overs.** `grep -c -F` per file (sft/dpo/instruct):
  - `- **D_p:** 2026-12-15`: 1/1/1;
  - `- **Disclosure** (p §5.4; F-p3`: 1/1/1;
  - "G-CAL-p passed at the bar, 47/64 against 47": 1/0/0.
- **C14, v0.1's forms (python, against `git show HEAD:`).** For each of the three files:
  - B.1's keys equal v0.1 §1's: 29 keys, in the same order.
  - `LICENCE` lines: 19 in each, differing only on `valence_core/p`.
  - `REGISTER` lines: 8 in each, identical.
  - The B.1 values that moved from v0.1 are exactly p's package_sha256, G-SHAPE-p's artifact, G-ANL-p's artifact and the driver.
- **C15, G-TIME's outputs.** `git show --name-status --format= 2258c52 | grep -c '<TAB>data/p/(ckpt|reports)/'` gives 15 (names only). RESULTS.md:588 says "all fifteen G-TIME outputs".
- **C16, the routing.**
  - B6 (RESULTS.md:487): "The pod: keep up until the wiring's commit lands, then re-decide with the time to G-F0m-OLMo (p) in view [the PI's call]."
  - B1 (RESULTS.md:482): "… → LOCK-p v0.2 ×3 → G-F0m-OLMo (p) ×3 on the box, batched → STOP for the seat's read [go]".
- **C17, independent digests.** I ran `shasum -a 256` on:
  - `scripts/m_analyze.py`, `scripts/p_analyze.py` and `scripts/p_sessions.py`;
  - `data/p/lexicon/web2.txt`, `data/p/schedules/manifest.json` and the 18 schedules;
  - `data/p/gates/G-SHAPE-p.json`, `G-ANL-p.json` and the three G-CAL artifacts;
  - `data/olmo/scaffold_{sft,dpo,instruct}.json`;
  - `valence_core/m/*.py` and `valence_core/adapters/olmo_hf.py`.

  In every case the first 16 hex digits equal §B's value. `ls valence_core/p | grep -c '\.py$'` gives 14, matching the licence's "14 files". The full sha256s of PROPOSAL-m v1.11 and PROPOSAL-p v0.2 equal §B's `42ab36ec…6c6b` and `42f2977b…3b32`.

### The table

| # | file | claim (short) | mark | evidence |
|---|---|---|---|---|
| 1 | sft | Header: re-issued above its v0.1 text, kept verbatim | CONFIRMED | C3: one superseding line (l.94); lines 96–end are byte-identical to HEAD's v0.1 blob (cmp) |
| 2 | sft | Header: m:302's "LOCK-m-OLMo v0.2: projections; OLMo port acceptance", written for p | IMPRECISE | C5: byte-equal to the seat's §2 lead-in. C12: the quoted words are not at PROPOSAL-m v1.11:302, which reads "LOCK-m-OLMo-{ckpt} v0.2 (acceptance; projections)"; they are v1.6/v1.7 wording |
| 3 | sft | Header: the seat's answer on G-TIME-OLMo (p), path, sha256 `7b8b1d5f…adc3`, §2 | CONFIRMED | C6; §2 is "Q2 — LOCK-p v0.2 ×3, in p's terms" |
| 4 | sft | Header: the seat's answers on the wiring, path, sha256 `e20bca13…23a9`, §3 | CONFIRMED | C6; §3 is "Q3 — the lock's form after a move" |
| 5 | sft | Header: B1's quoted order; B3's form "[adopted]" | CONFIRMED | C5: substring of RESULTS.md:482 after "... "; B3 ends "[adopted]." |
| 6 | sft | Header: on the code of `40086e8` (BUILD), with `f5e695c` (G-SHAPE-p) and `ba89279` (G-ANL-p) re-runs | CONFIRMED | C9: subjects and parents; no code change 40086e8..HEAD; artifacts at those commits = HEAD blobs |
| 7 | sft | Header: licenses G-F0m-OLMo (p) on OLMo-sft; nothing later | CONFIRMED | C11: `qual` requires v0.2's line; any gate outside ("time","qual") is refused |
| 8 | sft | Header: own sha256 named in its entry; it is the identity_extra lock_sha256 | CONFIRMED | C2: `4ab66e27…5b3e` = the draft entry's; C11: lock_sha256 = sha256(committed bytes); no git filter. The RESULTS.md entry is not yet written |
| 9 | sft | Header: "Version v0.2, 2026-11-10, committed by path" | NOT CHECKABLE | Not yet committed (` M`); the commit is in the future. The date matches the routing's PI date |
| 10 | sft | §A items 1–6 and 8 are the seat's §2 items verbatim | CONFIRMED | C4: byte-equal |
| 11 | sft | §A item 7 keeps the rule; only the pointer changes | CONFIRMED | C4: head and rule equal; the pointer parenthetical and the final noun ("sweep ruling's list" → "list of record's (v2, §2)") changed |
| 12 | sft | §A item 7: list of record v2 path, sha256 `6c1135f5…6cdd`, "supersedes the sweeps ruling's §2" | CONFIRMED | C6 |
| 13 | sft | §A item 1, this checkpoint: 0/10 silent; pause silent; control chars 0 of 4; proxy 10 of 10, 0 cuts; sham 3.528 s; entry 2026-11-09 at `2258c52` | CONFIRMED | C7 sft row; seat §1.3 |
| 14 | sft | §A item 1: the seat's read by path and sha256, "§1: PASS ×3 stand" | CONFIRMED | C6; seat :17 |
| 15 | sft | Acceptance line `G-TIME-OLMo-sft port acceptance recorded`, a whole line in item 1, own checkpoint only | CONFIRMED | C1: `qual_lock_problems` returns []; C3: line 10 only |
| 16 | sft | §A item 3, this checkpoint: 22.7 s; 1.17 / 1.37 / 1.58 h at 160 / 192 / 224 (+26) | CONFIRMED | C8 |
| 17 | sft | §A item 3: sham 3.528 s beside, the load excluded, not a basis | CONFIRMED | C7; seat item 3 |
| 18 | sft | §A item 3 (seat's text) figures: 19.5/22.7 s; 3.4/3.9/4.5 h at 160/192/224; 12 h; 3.528/3.972/5.289 s; 225–228 s; n = 1 | CONFIRMED | C8, C7 |
| 19 | sft | §A item 5 note: the 2026-11-10 §1 quote; fix at `40086e8`; fresh interpreter importing p's driver | CONFIRMED | C5, C10 |
| 20 | sft | §A item 8: D_p 2026-12-15, the disclosure and the SFT sentence carried in v0.1's text | CONFIRMED | C13: 1 / 1 / 1 |
| 21 | sft | §B.1: 29 values = `lock_required`'s (incl. G-CAL `78f46f07…`, covariate 15/64, six schedules, scaffold_sft `0c3592ad…`) | CONFIRMED | C1: keys, values and order equal; 0 problems; C17 |
| 22 | sft | §B.2: 19 LICENCE lines = `lock_required`'s, in order | CONFIRMED | C1, C17 |
| 23 | sft | §B.3: 8 REGISTER lines = `lock_required`'s, in order | CONFIRMED | C1 |
| 24 | sft | Every recomputed value (56) is named in the file and in §B | CONFIRMED | C1: `lock_names` returns no misses over the file and over §B |
| 25 | sft | §B is in v0.1's §1–§3 forms; the values that moved are the package, G-SHAPE-p, G-ANL-p and the driver | CONFIRMED | C14 |
| 26 | sft | Exactly one superseding line, worded as quoted | CONFIRMED | C3: `grep -c -x` returns 1 (l.94) |
| 27 | sft | The committed v0.1 text, verbatim, after it | CONFIRMED | C3: cmp identical; HEAD blob `9cc9045a…` = v0.1 entry's; only commit `0afd842` |
| 28 | sft | Exactly one BACKEND OF RECORD line, v0.1's, `641ee466f4553b6a` | CONFIRMED | C1 `lock_backend`; C3 (l.109) |
| 29 | dpo | Header: re-issued above its v0.1 text, kept verbatim | CONFIRMED | C3 |
| 30 | dpo | Header: m:302's "LOCK-m-OLMo v0.2: projections; OLMo port acceptance", written for p | IMPRECISE | as row 2 (C5, C12) |
| 31 | dpo | Header: the seat's answer on G-TIME-OLMo (p), path, sha256, §2 | CONFIRMED | C6 |
| 32 | dpo | Header: the seat's answers on the wiring, path, sha256, §3 | CONFIRMED | C6 |
| 33 | dpo | Header: B1's quoted order; B3 "[adopted]" | CONFIRMED | C5 |
| 34 | dpo | Header: on `40086e8`, `f5e695c`, `ba89279` | CONFIRMED | C9 |
| 35 | dpo | Header: licenses G-F0m-OLMo (p) on OLMo-dpo; nothing later | CONFIRMED | C11 |
| 36 | dpo | Header: own sha256 named in its entry; identity_extra lock_sha256 | CONFIRMED | C2: `bc049a5a…f9b7` = the draft entry's; C11 |
| 37 | dpo | Header: "Version v0.2, 2026-11-10, committed by path" | NOT CHECKABLE | not yet committed; future |
| 38 | dpo | §A items 1–6 and 8 verbatim | CONFIRMED | C4 |
| 39 | dpo | §A item 7 keeps the rule; only the pointer changes | CONFIRMED | C4 |
| 40 | dpo | §A item 7: list v2 path, sha256, supersedes the sweeps ruling's §2 | CONFIRMED | C6 |
| 41 | dpo | §A item 1, this checkpoint: 0/10 silent; pause silent; 0 of 4; 10 of 10, 0 cuts; sham 3.972 s | CONFIRMED | C7 dpo row |
| 42 | dpo | §A item 1: the seat's read, path/sha256, PASS ×3 stand | CONFIRMED | C6 |
| 43 | dpo | Acceptance line `G-TIME-OLMo-dpo port acceptance recorded`, whole line, own only | CONFIRMED | C1: []; C3: line 10 only |
| 44 | dpo | §A item 3, this checkpoint: 22.7 s; 1.17 / 1.37 / 1.58 h | CONFIRMED | C8 |
| 45 | dpo | §A item 3: sham 3.972 s beside, not a basis | CONFIRMED | C7 |
| 46 | dpo | §A item 3 (seat's text) figures | CONFIRMED | C8, C7 |
| 47 | dpo | §A item 5 note: quote, `40086e8`, mechanism | CONFIRMED | C5, C10 |
| 48 | dpo | §A item 8: D_p and the disclosure carried; the SFT sentence on sft only | CONFIRMED | C13: 1 / 1 / 0 |
| 49 | dpo | §B.1: 29 values = `lock_required`'s (G-CAL `035a204a…`, covariate 9/64, six schedules, scaffold_dpo `0c39ce96…`) | CONFIRMED | C1, C17 |
| 50 | dpo | §B.2: 19 LICENCE lines, in order | CONFIRMED | C1 |
| 51 | dpo | §B.3: 8 REGISTER lines, in order | CONFIRMED | C1 |
| 52 | dpo | Every recomputed value (56) named in the file and in §B | CONFIRMED | C1 |
| 53 | dpo | §B in v0.1's §1–§3 forms; the four moved values | CONFIRMED | C14 |
| 54 | dpo | Exactly one superseding line | CONFIRMED | C3 (l.94) |
| 55 | dpo | The committed v0.1 text, verbatim, after it | CONFIRMED | C3: identical; HEAD blob `efcba384…` = v0.1 entry's |
| 56 | dpo | Exactly one BACKEND OF RECORD line, v0.1's | CONFIRMED | C1; C3 (l.108) |
| 57 | instruct | Header: re-issued above its v0.1 text, kept verbatim | CONFIRMED | C3 |
| 58 | instruct | Header: m:302's "LOCK-m-OLMo v0.2: projections; OLMo port acceptance", written for p | IMPRECISE | as row 2 (C5, C12) |
| 59 | instruct | Header: the seat's answer on G-TIME-OLMo (p), path, sha256, §2 | CONFIRMED | C6 |
| 60 | instruct | Header: the seat's answers on the wiring, path, sha256, §3 | CONFIRMED | C6 |
| 61 | instruct | Header: B1's quoted order; B3 "[adopted]" | CONFIRMED | C5 |
| 62 | instruct | Header: on `40086e8`, `f5e695c`, `ba89279` | CONFIRMED | C9 |
| 63 | instruct | Header: licenses G-F0m-OLMo (p) on OLMo-instruct; nothing later | CONFIRMED | C11 |
| 64 | instruct | Header: own sha256 named in its entry; identity_extra lock_sha256 | CONFIRMED | C2: `145f0a6f…b082` = the draft entry's; C11 |
| 65 | instruct | Header: "Version v0.2, 2026-11-10, committed by path" | NOT CHECKABLE | not yet committed; future |
| 66 | instruct | §A items 1–6 and 8 verbatim | CONFIRMED | C4 |
| 67 | instruct | §A item 7 keeps the rule; only the pointer changes | CONFIRMED | C4 |
| 68 | instruct | §A item 7: list v2 path, sha256, supersedes the sweeps ruling's §2 | CONFIRMED | C6 |
| 69 | instruct | §A item 1, this checkpoint: 0/10 silent; pause silent; 0 of 4; 10 of 10, 0 cuts; sham 5.289 s | CONFIRMED | C7 instruct row |
| 70 | instruct | §A item 1: the seat's read, path/sha256, PASS ×3 stand | CONFIRMED | C6 |
| 71 | instruct | Acceptance line `G-TIME-OLMo-instruct port acceptance recorded`, whole line, own only | CONFIRMED | C1: []; C3: line 10 only |
| 72 | instruct | §A item 3, this checkpoint: 19.5 s; 1.01 / 1.18 / 1.35 h | CONFIRMED | C8 |
| 73 | instruct | §A item 3: sham 5.289 s beside, not a basis | CONFIRMED | C7 |
| 74 | instruct | §A item 3 (seat's text) figures | CONFIRMED | C8, C7 |
| 75 | instruct | §A item 5 note: quote, `40086e8`, mechanism | CONFIRMED | C5, C10 |
| 76 | instruct | §A item 8: D_p and the disclosure carried; the SFT sentence on sft only | CONFIRMED | C13: 1 / 1 / 0 |
| 77 | instruct | §B.1: 29 values = `lock_required`'s (G-CAL `5e3ef51a…`, covariate 1/8, six schedules, scaffold_instruct `21110cea…`) | CONFIRMED | C1, C17 |
| 78 | instruct | §B.2: 19 LICENCE lines, in order | CONFIRMED | C1 |
| 79 | instruct | §B.3: 8 REGISTER lines, in order | CONFIRMED | C1 |
| 80 | instruct | Every recomputed value (56) named in the file and in §B | CONFIRMED | C1 |
| 81 | instruct | §B in v0.1's §1–§3 forms; the four moved values | CONFIRMED | C14 |
| 82 | instruct | Exactly one superseding line | CONFIRMED | C3 (l.94) |
| 83 | instruct | The committed v0.1 text, verbatim, after it | CONFIRMED | C3: identical; HEAD blob `c03a1ef9…` = v0.1 entry's |
| 84 | instruct | Exactly one BACKEND OF RECORD line, v0.1's | CONFIRMED | C1; C3 (l.108) |
| 85 | entry | Title: 2026-11-10; p v0.2 §4.1's chain; B1's "LOCK-p v0.2 ×3", B3's form; the seat's answers at `42c5a92` §3 and `e619d3d` §2 | CONFIRMED | C5, C6; p §4.1's chain includes "LOCK v0.2" (PROPOSAL-p :84) |
| 86 | entry | Each lock re-issued above its v0.1 text, kept verbatim | CONFIRMED | C3 |
| 87 | entry | Each stands on `40086e8`, `f5e695c`, `ba89279` | CONFIRMED | C9 |
| 88 | entry | Each licenses G-F0m-OLMo (p) on its checkpoint, nothing later | CONFIRMED | C11; each header |
| 89 | entry | "Model-free; nothing ran on a model or the box." | NOT CHECKABLE | Code's own conduct; `lock_required` itself is model-free (C1 ran it on the laptop) |
| 90 | entry | Stamp line | NOT CHECKABLE | left open on purpose |
| 91 | entry | `LOCK-p-OLMo-sft.md` `4ab66e27…5b3e` | CONFIRMED | C2 |
| 92 | entry | `LOCK-p-OLMo-dpo.md` `bc049a5a…f9b7` | CONFIRMED | C2 |
| 93 | entry | `LOCK-p-OLMo-instruct.md` `145f0a6f…b082` | CONFIRMED | C2 |
| 94 | entry | Each sha256 is the lock_sha256 its G-F0m-OLMo (p) checkpoint will carry | CONFIRMED | C11: sha256 of the committed bytes; C2: no filter. Holds if each file is committed byte-unchanged |
| 95 | entry | The form, B3 verbatim | CONFIRMED | C5: equals RESULTS.md:484 without "- B3. " |
| 96 | entry | "§A: the seat's eight items …, quoted from its committed bytes. Where an item asks for this checkpoint's values, they sit beside it", then items 1, 3, 5, 7 | IMPRECISE | C4: item 7 is not quoted from the committed bytes but reworded in place (as the seat asks). The notes under items 5 and 7 are not checkpoint values |
| 97 | entry | Item 1: the G-TIME entry's figures (`2258c52`) and the whole acceptance line | CONFIRMED | C7, C1, C3 |
| 98 | entry | Item 3: sft/dpo 22.7 s → 1.17, 1.37, 1.58 h; instruct 19.5 s → 1.01, 1.18, 1.35 h; m's rule total + 26 | CONFIRMED | C8 |
| 99 | entry | Sham seconds 3.528, 3.972, 5.289 s beside, not a basis | CONFIRMED | C7; seat item 3 "no basis" |
| 100 | entry | Item 5: FLAG (j), its fix landing at `40086e8` | CONFIRMED | C10 |
| 101 | entry | Item 7: list v2 path, sha256 `6c1135f5…6cdd`, committed at `fc43249`, "as the seat's §3 and the list ruling's §2 have it" | CONFIRMED | C6 |
| 102 | entry | §B: the 56 values `lock_required` lists on the moved code, in v0.1's §1–§3 forms | CONFIRMED | C1 (N 56 ×3), C14, C9 |
| 103 | entry | "generated with nothing typed" | NOT CHECKABLE | a process claim; the outcome is consistent (C1: all 56 equal) |
| 104 | entry | Among them `08bfa693…fa26`, `89551017…af44`, `f8d22109…631f`, `90d0d5d6…8f2e`; the licence and register lines | CONFIRMED | C1, C9, C17 |
| 105 | entry | v0.1's text verbatim under the quoted superseding line | CONFIRMED | C3, C5 |
| 106 | entry | Its one `BACKEND OF RECORD 641ee466f4553b6a` line is the lock's one, as the precheck requires | CONFIRMED | C1, C3, C11 |
| 107 | entry | Check: names every `lock_required` value in `lock_names`' form | CONFIRMED | C1, re-run; that Code ran it is not checkable |
| 108 | entry | Check: exactly one backend line, v0.1's | CONFIRMED | C1, C3 |
| 109 | entry | Check: the acceptance line as a whole line (`qual_lock_problems`) | CONFIRMED | C1 |
| 110 | entry | Check: the committed v0.1 text verbatim after the superseding line | CONFIRMED | C3 |
| 111 | entry | The stage's precheck at `qual` reads the committed lock | CONFIRMED | C11 |
| 112 | entry | It runs on the box before the launch | NOT CHECKABLE | in the future; C11 shows that without the pod id it is refused, so it can only clear on the box |
| 113 | entry | Values-check line | NOT CHECKABLE | left open on purpose |
| 114 | entry | Next: on the PI's re-decision on the pod (B6) | CONFIRMED | C16 |
| 115 | entry | G-TIME's 15 outputs | CONFIRMED | C15 |
| 116 | entry | Those 15 untracked on the box, set aside by digest at the sync | NOT CHECKABLE | box state; no pod access |
| 117 | entry | Precheck CLEAR ×3 → G-F0m-OLMo (p) ×3, batched → the seat's read | CONFIRMED | C16: B1's order (the events are still to come) |
| 118 | entry | "Not pushed. Committed by path." | NOT CHECKABLE | the commit is in the future |

### Accurate wording, for the IMPRECISE marks

- **Rows 2, 30 and 58: the header of each lock, which is Code's voice.** The quoted words are the seat's (its §2 lead-in), not m:302's: PROPOSAL-m v1.11:302 reads "LOCK-m-OLMo-{ckpt} v0.2 (acceptance; projections)". A wording that keeps the seat's phrase but attributes it correctly: "… re-issued above its v0.1 text kept verbatim: m:302's LOCK-m-OLMo-{ckpt} v0.2 (acceptance; projections), written for p as the seat's "LOCK-m-OLMo v0.2: projections; OLMo port acceptance" (the seat's answer on G-TIME-OLMo (p), `results/raw/2026-11-09_p-gtime_design-to-code_answers.md`, sha256 `7b8b1d5f…adc3`, §2), in the form of …".
  - Any such edit changes the three file sha256s that the entry names (rows 91–93) and that rows 8, 36 and 64 depend on. If an edit lands, re-hash the files and re-run C1 and C3.
- **Row 96: the entry's §A bullet.** "**§A: the seat's eight items** (its answer of 2026-11-09, §2): items 1–6 and 8 are quoted from its committed bytes. Item 7 is quoted with its pointer replaced, as the seat's §3 of 2026-11-10 asks: it now points at the list of record v2 (…), and its rule is unchanged. Beside items 1 and 3 sit this checkpoint's values; under item 5, its fix's landing at `40086e8`: …". The item 7 sub-line would then move out of the "values beside" list.

### Observations for the seat (not marks against these files)

- **The two m:302 quotes in the seat's §2 are not in PROPOSAL-m v1.11.** The seat's §2 lead-in and its item 1 put two phrases in quotation marks as m:302's. Neither is in PROPOSAL-m v1.11, the F-p8 pin `42ab36ec…` (C12):
  - "LOCK-m-OLMo v0.2: projections; OLMo port acceptance" is the wording of the v1.6:102 and v1.7:109 headings.
  - "the F0m-OLMo verifier's acceptance of the runner" is at v1.6:99 and v1.7:107, and in no version from v1.8 on.

  In substance both stand: v1.11:302 has "(acceptance; projections)" and "port acceptance recorded at v0.2", and v1.11:54 defines "OLMo port acceptance" as "the F0m-OLMo verifier plus the seat's read …". The locks carry item 1 verbatim, as they must, so only the header is marked.
- **Item 3's "verify re-forward" is not named at m:205.** Item 3 (the seat's text) says the m:205 figures "carry the load and the verify re-forward amortized". m:205 names only the load's amortization ("which amortize one model load over a whole b3 run"). This is not a figure, and I did not check it further.

### Disclosures under the list of record v2

- **Author dates in one early call.** One early `git log --format='%h %ad %s' --date=iso -n 1` on `e619d3d`, `42c5a92`, `fc43249` and `2258c52` printed author dates (`%ad`), not committer dates. These are commit-object times and show no file's size or time. Every later call used `%cd`. I disclose it in case item 1's "commit times" is read as committer time only.
- **An over-broad grep of RESULTS.md.** A broad pattern over `git show 2258c52:RESULTS.md` (committed text, no `data/` path) printed table rows from unrelated older entries. Among them was a 2026-08-23 table of marker-store sizes in MB, which belongs to no open unit's `ckpt` or `reports`. This is not an item-2 form, and nothing from it is reproduced here.
- **What I touched under `data/`.**
  - I hashed files under `data/p/gates`, `data/p/schedules`, `data/p/lexicon` and `data/olmo` (C17; prefixes printed). Gate artifacts at commits were read only as digests (`git show … | shasum`).
  - I counted names under `data/p/ckpt` and `data/p/reports` at `2258c52` with `git show --name-status … | grep -c`, which printed 15.
  - No file under any `data/*/ckpt` or `data/*/reports` was read, hashed, or listed with a size or time. The stage's own code (`lock_required`, `fresh_import_closure`) read committed blobs through git plumbing, without `-l`.
- **Content searches.** I used `git grep` with `':!data/**'` (C12) or single named files (stage.py at commits, RESULTS.md, the raws, the proposals). I ran no recursive grep, `rg`, `find` or pickaxe.
- **Everything else.**
  - I wrote no file but this report; `cmp` and `diff` used process substitution (pipes).
  - A stray `echo =====` was taken by zsh as an `=` expansion and errored, harmlessly.
  - I ran no git command that changes anything, nothing that loads a model, and nothing on the box.
