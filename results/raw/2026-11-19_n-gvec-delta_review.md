# n — G-VEC's delta (second sitting): the blind review of draft 1, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over draft 1, the delta from HEAD `f4b3e73`'s bytes to the seat's
change (the answers of 2026-11-19, second sitting: §1.2, §1.3, §1.4 (ii)–(iv), §1.5):
- `valence_core/n/gvec.py`, from `a620349f…ec71` to `38743639…8f1d` (878 lines), read in full;
- `valence_core/n/directions.py`, from `f9d0114c…2db4` to `30b516d7…aed2` (162 lines), read in full;
- `scripts/n_sessions.py`, from `655430f3…d027` to `ba47050e…f8b6` (3644 lines): G-VEC's section, its self-test and
  `gcal_gvec_inputs` read in full.
Draft 1's self-test ran 555/555 in a battery window while the review ran.

**The reviewer's brief** (`c0c50e1f…8729`, 92 lines):
- gave the three deltas' FROM and TO files, by sha256, and the `git diff --no-index -U3` form; the seat's answers of
  the second sitting (§1 in full and §3's last paragraph), for what the delta must do; and the first sitting's (§0,
  §1.1–§1.4) and the "Wording owed" bullet of `355e3a2`'s entry, against which every claim of the new wording was to
  be checked;
- asked whether R over every position reproduces the first run's R bit for bit on identical forwards; whether each of
  Code's declared readings is sound, and whether any breaches §1.3's "Nothing else"; whether the consumers
  (`gcal_gvec_inputs`, the analyzer) break, and whether any code reads `data/n/gvec/gvec.json` at the path the commit
  moves it from; and whether the self-test count of 555 holds;
- asked for findings, surviving mutants, box risks and observations, and for any command a rule bars;
- quoted the list of record v2's items 1–5, verbatim, and barred any interpreter but shasum, any write, any network,
  any model or adapter code run, any guard marker in an argv, anything under `data/mf3`, any whole-tree git status,
  any read, listing, size or time of a ckpt or reports file, and, in Code's scratch, anything but the files it named.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (113 lines, sha256
`e5bffcd5…4724`). It names scratch files only by their paths inside the scratch folder. Two of its hash
abbreviations depart from the first-8…last-4 form, against the full sha256s its brief gave and it checked:
"f9d0114c…a2db4" carries a five-character tail (`f9d0114c…2db4`), and "e6ff066d…5d5a" is a slip for `e6ff066d…6d5a`.

**Totals:** 0 BUG; 8 findings (1 RISK, 7 NIT); 6 surviving mutants; 3 box risks; 9 observations.

## 1. Dispositions, applied in draft 2

Draft 2: `valence_core/n/gvec.py` `939c9f9c…5b69` (956 lines), `valence_core/n/directions.py` `c63c8ea8…e527` (163
lines) and `scripts/n_sessions.py` `2728146e…570c` (3662 lines). Draft 3, the bytes committed, changes two clauses of
`gvec.py`'s module docstring on the texts' values-check (its observations 2 and 8), and nothing else (`gvec.py`
`e2f7a49e…be94`, 958 lines, +7 −5 on draft 2); this review's scope stays the draft 1 → 2 delta.

- **F1** (RISK), applied: a non-finite descriptive figure no longer raises. `diagnostic_at` records it as null and
  names its key in the index's `nonfinite` list (sorted), and the diagnostic line ends "; not finite, recorded as
  null: …" when the list is not empty; R itself still raises. `compute` prints the token lines, R's count line and
  the R lines before it checks the figures finite and before it computes the diagnostic block. A position's passages
  are counted by their token counts, not by the absence marker, so a non-finite residual cannot drop a passage from
  a count. A new self-test case gives position 0 an infinite row: R_all, `rms_by_position` "0" and `max_norm` "0" are
  null and listed, every other figure is finite, and R over 1..n equals the clean R.
- **F2** (NIT), applied: the STOP's printed lines (`gvec.STOP_LINE`; the driver's `GVEC_STOP_END`) and the docstrings
  now send the STOP to the PI, with the diagnostic block, on the seat's stated default (the second sitting, §1.5).
  The self-test checks each line printed (`STOP_LINE` last of `compute`'s lines on a STOP, `GVEC_STOP_END` last of
  the driver's) and pins "for the PI" and "§1.5" in `STOP_LINE`'s text; `GVEC_STOP_END`'s words are checked only
  against the constant itself.
- **F3** (NIT), applied: the smoke's announce line reads "R over positions 1..n, R_ell and the diagnostic block; never
  of record", pinned by the driver's smoke check.
- **F4**, **F5** (NIT), applied: F4 in the reviewer's words; F5 in its substance, in the docstring's own sentence.
- **F6** (NIT), applied by declaring: `gvec.py`'s readings paragraph names the printed count line, each diagnostic
  line's "; tokens" clause and the order of the prints; the driver's docstring names the smoke record's two token
  counts and the convention as Code's reading.
- **F7** (NIT), applied: the 3-token case is computed only when such a passage exists, and the check fails, rather
  than raising, if none does.
- **F8** (NIT), applied: G1's text keeps the BUILD's and the first run's clause beside the new one, as the convention
  `R_all` keeps.
- **M1–M6**, each killed by a new or extended check: M1 by the R_mean clause in the line check; M2 and M3 by a capture
  whose position 0 is shrunk a hundredfold and whose last row is grown fiftyfold, its `max_norm` checked against a
  computation apart; M4 by the convention's words pinned; M5 by a two-id passage captured (its count entering R 1,
  its mean its row 1); M6 by `passage_mean` on two rows.
- **B1** and **B2** ask for nothing; B2's one way to end with no record is F1, now closed for the descriptive figures;
  R stays a raise, declared. **B3** goes to launch files v2.
- **O1–O6**, **O8** and **O9** ask for nothing in the code. O1 and O6 give the read its checks against the first run.
- **O7**, applied: run_gvec refuses, before the load, a passage with no token at positions 1..n; the driver's
  refusals before the load gain the case.
- **The coordinating session's wording point**, applied with the review: `neutral_tokens_in_R` is the seat's §1.2 item
  ("the count entering R beside"), not a reading of Code's; `n_by_position` is a count beside each `rms_by_position`
  figure, not a figure.
- **The reviewer's departures,** as its report states them, are in the delta's entry, for the seat to class.

## 2. The report as returned

Blind review: G-VEC's second-sitting delta (convention of record + diagnostic block)

I found no BUG. There is one RISK, seven NITs and six surviving mutants. I agree the self-test count is 555, and I expect no check to fail.

I checked every hash before reading. The brief is c0c50e1f…8729. The three FROM files are a620349f…ec71, f9d0114c…a2db4 and 655430f3…d027; each is clean at HEAD f4b3e73 (rev-parse equals hash-object). The three TO files are 38743639…8f1d, 30b516d7…aed2 and ba47050e…f8b6. The two answers raws are 887b7646…dc87 and e6ff066d…5d5a, both clean. data/n/gvec/gvec.json is 3331da71…ee95, clean. Line numbers below are the TO files' (S/step4b/gvec2/draft/gvec.py, directions.py, n_sessions.py) unless a repository path is named.

FINDINGS
- **F1 — RISK.** gvec.py:404 (with :213, :216, :219, :221–222) and n_sessions.py:2263–2265.
  - Every diagnostic figure passes `_finite`, which raises. `diag` is computed at :404, before the first line prints (:418) and before the STOP/PASS branch (:427).
  - So a non-finite descriptive figure would end the run of record with a ValueError. The most exposed are the sink's: R_all, rms_by_position "0" and max_norm "0".
  - The result would be no R line in the raw, the staging folder removed by run_gvec, no record and no STOP block. That comes from figures §1.3 makes "none a decision". At FROM only R and its rel could end the run this way (:409).
  - This is remote here: float64 squares of bf16 residuals of order 10².
  - Fix: print the R lines from `r` and `site` before computing `diag`. Then either record a non-finite descriptive figure as null with a declared `nonfinite` list (the exit code still R's), or keep the raise and declare it as a reading.
- **F2 — NIT.** The STOP's addressee under §1.5.
  - The printed "…; the seat rules" appears at gvec.py:428 and n_sessions.py:2269. "A STOP for the seat" appears at gvec.py:11–12 and :236, and at n_sessions.py:149 and :2133.
  - §1.5 says a STOP at both indices again is "STOP for the PI, with §1.3's figures; the seat rules no third convention on its own authority".
  - The behaviour already matches (exit 2; the record alone, with the diagnostic block). Only the words are stale, and the box prints them into the raw (results/raw/2026-11-19_n-gvec-v1_out.txt:122, :124).
  - Fix: e.g. "…; to the PI with the diagnostic block, on the seat's stated default (the second sitting, §1.5)". No self-test pins either line's text.
- **F3 — NIT.** n_sessions.py:2174–2175.
  - The smoke's announce line still says "R and R_ell only; never of record" (it printed so at results/raw/2026-11-19_n-gvec-v1_out.txt:87).
  - The smoke now records the diagnostic block and prints its two lines, as the driver's own docstring at :146–148 says. Only `startswith("SMOKE:")` is checked (:2439).
  - Fix: "…; R over positions 1..n, R_ell and the diagnostic block; never of record".
- **F4 — NIT.** gvec.py:393–395, compute's docstring.
  - It says "on a STOP … the figures end at R and nothing else is computed". The STOP's figures now carry the diagnostic block (:404, :414).
  - Fix: "end at R and the diagnostic block".
- **F5 — NIT.** directions.py:67–69, rms_norm's docstring.
  - It says "G-VEC passes the sums and counts over positions 1..n". gvec.diagnostic_at also passes every position's, for R_all (gvec.py:219).
  - Fix: "for R, over positions 1..n (passage_rows); for the diagnostic block's R_all, over every position".
- **F6 — NIT.** gvec.py:74–78, the declared readings. They leave out three additions that §1.2–§1.3 do not ask for:
  - the printed count line "R over positions 1..n: … of the … neutral tokens, …" (gvec.py:420–421; it is also a new head in n_sessions.py:2414);
  - the "; tokens …" clause on each diagnostic line (gvec.py:228, :231);
  - the smoke record's new keys `diagnostic`, `neutral_tokens`, `neutral_tokens_in_R` and `convention` (n_sessions.py:2247–2249).
  - Fix: declare them, the smoke's in the driver's docstring, or drop the count line and the smoke's three extra keys.
- **F7 — NIT.** gvec.py:678–680, self-test.
  - `d3 = diagnostic_at(pc, short3, 4)` runs before the chk's `bool(short3.any())`. If the toy had no 3-token neutral passage, `rms_norm` would raise "no neutral tokens" (directions.py:71–72) and every later gvec check would be lost.
  - With seed 29 the chance is about (3/4)^96, so it will not fire; the guard simply does not guard.
  - Fix: compute d3 only when short3.any().
- **F8 — NIT.** gvec.py:30–38.
  - The heading still says the readings were "declared at G-VEC's BUILD", but G1*'s text is now the second sitting's. The BUILD's clause ("every token in its mean and in R"), which R_all embodies, appears nowhere in the module.
  - Fix: one parenthesis in G1*, e.g. "(at the BUILD and the first run: every token in its mean and in R — R_all's convention)".

SURVIVING MUTANTS
- **M1** — gvec.py:231: `{d['R_mean_of_passage_rms']!r}` → `{d['R_all']!r}`.
  - The line check (:685–689) never tests R_mean's text. Every other line check compares against `diagnostic_line` itself (:823–824; n_sessions.py:2449–2450).
  - Kill: add `f"; R_mean_of_passage_rms {d4['R_mean_of_passage_rms']!r}; tokens " in dl` to :685–689.
- **M2** — gvec.py:181: `float(norms[0])` → `float(np.max(norms))`.
  - In the test double, each position's state comes from a running mean, and at position 0 that mean is the state itself (valence_core/n/testing.py:52–54). So position 0 has the largest norms, and the global maximum sits at a position 0.
  - The direct checks at :672 and :680 therefore agree with the mutant. The sink check (:628–639) scales position 0 up and never checks max_norm.
  - Kill (with M3): a copy of fwd_sink that scales position 0 by ×0.01 and the last row by ×50, with max_norm checked against diag_direct.
- **M3** — gvec.py:182: `norms[directions.CAPTURE_FROM:]` → `norms[directions.CAPTURE_FROM:-1]`.
  - The double's norms fall with position, so the maximum over 1..n sits at position 1, which survives the cut for every 3–6-id toy passage.
  - Kill: as M2.
- **M4** — gvec.py:113–115: change R_CONVENTION's words, e.g. "positions 1..n" → "positions 0..n".
  - Every check compares the field with the constant itself (:820, :860; n_sessions.py:2447).
  - Kill: pin the text, e.g. `"positions 1..n" in R_CONVENTION and "position 0 of every passage left out" in R_CONVENTION`.
- **M5** — gvec.py:162: `<= directions.CAPTURE_FROM` → `<= directions.CAPTURE_FROM + 1`. This refuses a valid two-id passage.
  - Kill: capture a two-id passage and check nr is 1 and its mean is its row 1.
- **M6** — directions.py:57: `a.shape[0] <= CAPTURE_FROM` → `<= CAPTURE_FROM + 1`.
  - Kill: `np.array_equal(passage_mean(sink[:2]), sink[1])`.

BOX RISKS
- **B1 — The box self-test.** No new case can reach a production load or write a canonical folder.
  - The new gvec checks run passage_captures, diagnostic_at, compute and write on the double, write under tmp only, and read back only there.
  - The driver's new check reads env3's tmp smoke record and runs `passage_captures(fwd_of(None), …)` on the double.
  - `production_gvec_env()` (n_sessions.py:2302) is built and compared, never run. `env_for(out=GVEC_OUT)` is refused before a GvecEnv exists (:2387–2388, :2544–2545).
- **B2 — The run of record.**
  - F1 is the one way it can end with no record.
  - Memory: the extra per passage and index is one [T] norm vector and five squared norms, beside the [T, D] float64 cast the stage already made.
  - Warnings: none on finite data. `isnan`/`nansum` run only with k > 0, and every division is by a count of at least 1.
  - JSON: string keys, Python float/int/None values. pos_sq's NaN never leaves passage_captures, so allow_nan=False cannot trip.
- **B3 — Launch files v2, which the self-test cannot see.** These need updating:
  - The box self-test total: 555 plus the 11 HF checks is 566, if that delta still stands.
  - The smoke's line counts. The v1 script asserted "each must be 1" (out raw :99). v2 adds two diagnostic lines, and the SMOKE line's text changes if F3 is taken.
  - The run's line counts (out raw :127). There is a new "R over positions 1..n:" line, so any count by a bare "R " prefix would read 3. There are also two diagnostic lines, and the STOP text changes if F2 is taken.
  - The record's checks: schema "n-gvec-v2", R now over 1..n, and the new `diagnostic`, `site.convention` and `passages.neutral_tokens_in_R`.
  - A new fresh copy at the move's commit. The da7bdec copy holds data/n/gvec/gvec.json, so G7 refuses there.

OBSERVATIONS
- **O1 — Item 3: R_all reproduces the first run's R bit for bit, given bitwise-identical forwards.** No operation differs.
  - `sq_all` (gvec.py:178, :189) is FROM's `sq`, operation for operation: the same float64 cast (:167) and `float(np.sum(h*h))`. passage_rows, the norms, head and tail never modify h. The passages are in the same order.
  - `diagnostic_at` (:206, :219) uses the same boolean mask object and the same `rms_norm` (body unchanged), then `_finite` and the JSON repr, as FROM's `r_at` and `_finite(r[i])` did.
  - So R_all should read 44.04249774012646 at 31 and 45.107750142385356 at 32. The smoke's R_all likewise reproduces 42.62270212364156 and 43.66884683035452.
- **O2 — Items 1–2: the delta does what the seat asked.**
  - §1.2 and §1.3 are implemented as written, on a STOP as on a PASS, and the smoke prints the same lines.
  - §1.4 (ii) and (iii) are done. (iv) holds: CAPTURE_FROM, passage_rows and passage_mean are used only in gvec.py and the driver's G-VEC section, and gcal.py imports neither module.
  - The new wording's claims check out. "G-VEC runs as built" is the first sitting's §0 verbatim, ruled before the run (a33252a before 355e3a2). "One clause of G1" is the second sitting's §0, with the clause at §1.2. "each over the 96 passages" is §1.3 verbatim. "Shortest 35 tokens" matches the first run's token table (neutral minimum 35, every other state 38 or more).
  - The stale sentence named in 355e3a2's "Wording owed" bullet is gone.
- **O3 — Item 4: each of Code's readings is sound.**
  - n-gvec-v2: R changed meaning, and the only schema check (n_sessions.py:2669) tracks the constant.
  - n_by_position: the only addition inside the diagnostic block. It is neither thing §1.3's colon names (a per-position profile beyond 4, or a per-passage figure), so it is no breach by the sentence's own gloss. It is still a fifth entry that "Nothing else" does not list — the seat's call.
  - Null: cannot occur in the run or the smoke (minimum 35 tokens), and is the only form allow_nan=False permits.
  - R_CONVENTION and neutral_tokens_in_R sit outside the block. The latter is what §1.2 asks for as "the count entering R beside".
  - Not asked for and not declared: the three items in F6.
- **O4 — Item 5: nothing breaks.**
  - gcal_gvec_inputs reads schema, stage, status, site.site, of_record and files_sha256, all unchanged in form. Its self-test fakes the record using the constant (:3023).
  - of_record.R becomes R over 1..n, which G-CAL-n's dose map then uses — what the convention implies.
  - The analyzer reads only the cosines file (scripts/n_analyze.py:6045–6060), whose form is unchanged.
  - The git mv: no code path or self-test reads data/n/gvec/gvec.json at its old path. GVEC_OUT is either an out folder that is refused if present, or G-CAL-n's input after a committed v2 PASS. The self-tests only compare or refuse the path, and use tmp folders.
  - gvec.json is the only tracked file in data/n/gvec/, so a fresh copy at the move's commit has no such folder.
  - Committed texts that cite data/n/gvec/gvec.json at 3331da71…ee95 (355e3a2's entry; the second sitting's header) will point at a different file after the re-run; the hash stays the record.
- **O5 — Item 6: I agree with 555.**
  - chk call sites, FROM → TO: gvec.py 32 → 40. Two were replaced in place, and the one-id check has two sites in a try/except of which one executes, so +7 executed. directions.py 9 → 11 (+2). The driver 147 → 148 (+1).
  - I expect none to fail. The double is deterministic, outputs float32, records `calls`, and gives position 0 a distinct norm. The toy passages of 3–6 ids give the counts at positions 3, 4 and 5..n strictly between 0 and 96.
- **O6 — Figures the read can check against §1.1:** neutral_tokens 4,163; neutral_tokens_in_R 4,067; n_by_position 96 at 0–4 and 3,683 at 5..n. rms_by_position "0" is an RMS, the same form as the seat's 240–250 estimate.
- **O7 — The one-id refusal sits where §1.2 places it, but after the load.** It fires after the load and after all earlier passages' forwards. run_gvec's pre-load checks hold the longest input (n_sessions.py:2197–2199) but not the shortest, against its own docstring at :2132. Moot for this corpus (minimum 35).
- **O8 — §1.4 (i) is a later delta's.** Until then the package mixes conventions: v from 1..n, the arrival score over every position. No stage can run in between.
- **O9 — The smoke's R line does not name the convention.** The "SMOKE R" line (n_sessions.py:2253–2254) does not say R is now over 1..n, and the smoke prints no count line. Compare R_all, not R, against 355e3a2's smoke.

DEPARTURES
- **Narrower pathspec.** Two git grep runs used a narrower include than the brief's `.` — `'*.py'`, and `'*.py' '*.sh' '*.json'` — each with all three exclusions. I re-ran both in the brief's form and got the same matches.
- **Harness-saved output.** One git grep in the brief's form printed 51.5 KB, which the harness saved to its own tool-results folder, outside the repository and S. No command of mine wrote it, and I did not open it.
- **Reads beyond the named files** (no rule bars them): valence_core/n/testing.py, scripts/n_analyze.py, RESULTS.md (355e3a2's entry), plus greps of valence_core/extract.py, valence_core/n/gcal.py, valence_core/n/hftiny.py and results/raw/2026-11-19_n-gvec-v1_out.txt.
- **Otherwise none.** No interpreter but shasum. No guard marker in any argv. Nothing under data/mf3, data/*/ckpt or data/*/reports touched. In S, only the brief and the three drafts.
