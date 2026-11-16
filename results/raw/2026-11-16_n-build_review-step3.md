# n package — BUILD, step 3: the blind review of the step-3 changes, with mutants, and Code's dispositions

*The n-build session (Code), PI date 2026-11-16. This is the second blind review of the BUILD. The first, of the
drafts at `14e65d8`, is its own raw. This one read the changes the seat's order made at step 3 (the seat's answers
of 2026-11-16, second sitting, §5, committed at `52b2c97`; ADDENDUM-n1 v0.1, `a61f13d`):*

- *`ids.py`: the ids of record's render, load, `ids_of` and `label_ids`;*
- *`verify.py`: G-VER asserting the committed data;*
- *`cells.py`: one capture array per layer, written in place;*
- *`primitive.py` and `hftiny.py`: the band past the site;*
- *`runner.py`: the keepers and `loads_ms`;*
- *`probe.py`: kfold10 and the PASS rule;*
- *`guard.py` and the driver.*

*One blind reviewer, a Code subagent, read the drafts in Code's scratch build folder against those rulings. The
repository was at HEAD `d791bd9`, with schema v5 committed there. Its brief held it to these rules:*

- *run no Python, and nothing else that executes the code;*
- *write nothing, and use no network;*
- *put no guard marker in any command line;*
- *list or read nothing under `data/mf3`: no whole-tree `git status` and no unscoped search;*
- *print no token id, and open neither `data/n/ids/*.jsonl` nor `labels.json`;*
- *the list of record v2's items 1–5, quoted verbatim.*

*It returned 13 findings: 1 BUG, 6 RISK and 6 NIT. It also returned 20 mutants. By its reading, 8 are killed by
existing checks and 12 survive, and it gave each survivor the test that would kill it.*

*A second Code subagent implemented the fixes and tests from Code's brief. Code read `cells.py`'s production code in
full and checked every disposition below at its site in the drafts.*

*The package self-test on the fixed drafts gave 217/217 (it was 187). It ran on the laptop, under the jlens venv at
`nice -n 19`, from a scratch overlay, in a battery window the coordinating session granted. The package sha256 was
`60d892dc…cc66`.*

*The 20 mutants were then run for real against that self-test, in their own window. The results are in the last
section.*

*The report is reproduced as the reviewer returned it. "S" is Code's scratch build folder, and its line numbers are
those of the drafts it read, before the fixes.*

## The review, as returned

Blind reading review of the n package drafts in S (= scratchpad/build). I ran no code. My only commands were name-only listings, `wc -l`, shasum, `git rev-parse`/`hash-object`, a scoped `git diff` of schema.py, and scoped greps (`':!data/**'` on the repo). I opened nothing under data/. Code paths below are S-relative and equal the repo paths at commit; rulings are repo-relative.

**Bottom line:** one real bug (cells cannot resume after a crash during a cell's first read), six risks to settle before the campaign, and six nits. ids.render, G-VER, the probe's kfold10 and PASS rule, and the cells hashing all match the rulings.

## (1) Findings

**1. BUG — valence_core/n/cells.py:192–196 (with :113–116; the docstring's claim at :10–12)**
- **What happens:** at a cell's first append (n = 0), every layer's array is created with `open_memmap(p, "w+")` and row 0 is written before the JSON exists.
- **Failure:** the process is killed or hits an I/O error between the first `open_memmap` and the rename in `atomic_write_json` (e.g. a pod preemption during one of ~138 cells' first appends, each about 31 creates plus fsyncs). This leaves `<stem>.L*.npy` files with no `<stem>.json`.
- **On resume:**
  - `load_cell` returns `new_cell` with an empty `Captures`.
  - The read is re-launched, spending a forward.
  - `append_record` then hits `if n != 0 or p.exists()` and raises SystemExit ("a capture array the cell does not hold open"), with no report.
  - This repeats on every resume. Recovering needs files deleted under the stage's checkpoint root, which needs a ruling.
- **Why it's new:** the docstring's "the next append writes that row again" holds only for n ≥ 1. The old atomic whole-array rewrite did not have this hole.
- **Fix:**
  - At n == 0, assert the JSON is absent, then create every layer's array with "w+" whether or not a file exists (no JSON names its rows).
  - Alternatively, create the arrays under `.tmp` names and `os.replace` them before the JSON.
- **Test:** put an orphan `.L2.npy` (and a wrong-shaped one) beside a new cell, append, reload; rows and hashes must verify. Today it refuses.

**2. RISK — runner.py:368 and :470–471; cells.py:100, :195**
- **What happens:** `open_cells` loads every cell (mode r+) at the start and keeps each `append_record`'s Captures, so all memmaps stay open for the whole invocation.
- **Why it matters:** CPython's mmap keeps a duplicated fd per mapping (before 3.13's `trackfd`). With about 138 cells × 31–32 layers, that is about 4,300–4,400 open fds — at the end of a fresh campaign, or immediately at load on a resume.
- **Failure:** under a 1,024 soft nofile limit (a common container default), `open_memmap` fails with EMFILE around the 33rd cell, early in N1-R, and every resume then fails inside `load_cell`. Self-tests and G-TIME-n open only a few cells, so nothing before the campaign exercises this.
- **Fix:**
  - Verify cells at load in mode "r", then close them.
  - Hold r+ arrays only for the cell being appended (launch order is cell-major) and close them when the launch moves on.
  - Check or raise RLIMIT_NOFILE at start and log it in the stage entry.

**3. RISK — cells.py:195–199 (scripts/n_sessions.py:67)**
- **What happens:** the in-place writer relies on shared writable mmap, msync and fsync on the box's /workspace network volume, but the self-test's temp directory is the system temp dir, not the volume.
- **Why it matters:** m's `_fsync_dir` already tolerates EINVAL/ENOTSUP "seen on some network volumes"; `cells._fsync_file` has no such tolerance. A FUSE or network mount may refuse writable shared mmap (ENODEV) or not persist it.
- **Fix:**
  - In the post-build site check, run cells' self-test with its temp directory on the stage root's filesystem.
  - Add a write → close → reopen → `rows_sha256` round trip there.

**4. RISK — probe.py:98–109, with :58–66; self-test :121 and :149–152**
- **What happens:** `artifact()` records `shuffles=N_SHUFFLES` and `shuffle_seed=SHUFFLE_SEED` as constants, plus whatever `layers` and `cv_seed` the caller passes. None of these is tied to what `layer_auc` actually ran, and `layers` is never compared with the campaign identity's `capture_layers` (check_gread has no identity to compare with).
- **The self-test shows it:**
  - The nulls come from 20 shuffles at seed 5 over layers [32, 63], while the example identity's band is 32–63.
  - The artifact nevertheless states 200 shuffles at 20260905 over [32, 63], and it passes check_gread.
- **Failure:** a G-READ-n driver probing part of the band (or the old two layers), or using a cv_seed other than the one it records, gets a PASS on a median that ADDENDUM-n1 §6.2/§6.4 does not define.
- **Fix:**
  - `artifact` asserts `list(layers) == campaign_report["stage_identity"]["capture_layers"]`.
  - `layer_auc` returns the shuffles, perm_seed and cv_seed it used, and `result`/`artifact` assert them equal to the declared values.
  - The analyzer re-checks `probe.layers` against the identity named by its sha256.

**5. RISK — runner.py:516 (and :246)**
- **What happens:** `loads_ms` is the prior report's list plus this invocation's load.
- **Failure:**
  - Any invocation that ends without a report (crash, kill, a SystemExit inside `run`, finding 1) loses its load entry.
  - A resume with no prior report starts the list fresh, so the report states fewer invocations than ran.
  - `load_ms: int = 0` makes an unset measurement look like a real 0 ms load.
- **Fix:** persist each load when it happens (an atomic sidecar under the stage root, or an invocation-start report), and make `load_ms` required.

**6. RISK — verify.py:64–69; ids.py:227–248 (`manifest_sha256` is never used); runner.py:444–455**
- **What happens:** nothing compares the loaded MANIFEST.json's sha256 with a pin — LOCK-n's "rendering and spans" (ADDENDUM-n1 §1.5) or the identity's `rendering_id`.
- **Why it matters:**
  - Session ids are bound to BK by `ids_sha`.
  - N4 suffixes and label tails are checked only by decode equality, which is many-to-one under BPE (" Birds"+"ong" decodes the same as " Bird"+"song").
- **Failure:** a re-rendered, internally consistent ids folder with differently segmented N4 or label ids would PASS G-VER and feed the runner without any warning.
- **Fix:**
  - `verify(..., manifest_sha256_pin)` STOPs on a mismatch.
  - The stage driver asserts `loaded["manifest_sha256"]` equals `rendering_id` before building StageInputs.
  - For the BUILD trial, the pin is the render's MANIFEST (7f51bd91…821d).

**7. RISK — hftiny.py:63–93; primitive.py:419–425**
- **What happens:** with captures moved to [2, 3], no HF-path check remains that the read position's residual at the site equals the shadow's and that site + 1 differs.
- **Why it matters:** the premise is tested only on `testing.CausalDouble`, which was written to the same convention. A hook-site or transformers change would leave the band's first layer structurally null in every median, undetected until G-READ-n.
- **Side note:** primitive's site check rebuilds the PositionSpec itself instead of calling `_placed`. It matches `read()` today but would not follow a change.
- **Fix:**
  - In hftiny, prefill with and without `inj` at layers [1, 2]; assert exact equality at layer 1 and a difference > 1e-3 at layer 2.
  - In primitive's self-test, use `_placed(spec, s, len(ids))[2]`.

**8. NIT — verify.py:116–121; self-test :155–157**
- A session-count mismatch STOPs with an empty `first_problems`, and the self-test asserts it is empty.
- A G-VER STOP can also come from the manifest, a missing decoder or a label check with zero id mismatches, while check_report requires `rendering_mismatches ≥ 1` at a G-VER-STOP (schema.py:1457–1461).
- **Fix:** add "N sessions, not 160"; ask the seat how a non-mismatch G-VER-STOP is counted.

**9. NIT — verify.py:9, :43–52, :106–115; ids.py:269–270**
- The docstring says G-VER asserts that the spans tile [0, n_pre); `span_problem` does not check this (it relies on `load_sessions`).
- G-VER checks only the labels a candidate holds. A labels.json missing a cue passes G-VER, then `label_ids` raises SystemExit mid-campaign — not a pause, and no report.
- **Fix:** assert tiling, and assert each kept candidate holds exactly the 12 cues.

**10. NIT — ids.py:175 (:97–101)**
- `_with_splits` raises RenderingMismatch inside the candidate loop and nothing catches it, so such a candidate crashes the render instead of being "reported and dropped".
- **Fix:** catch it and count it as a prefix failure.

**11. NIT — scripts/n_sessions.py:96; :126 with guard.py:74–81; :149–154**
- gver-trial calls `from_pretrained(model_dir)` with no `local_files_only=True` and no is-dir check, so a mistyped path that parses as a hub id is downloaded on the box.
- render-ids' `--out` is admitted anywhere under data/n/ (data/n/bk included), while the docstring says data/n/ids/.
- render-ids is dispatched before `--selftest`.

**12. NIT — ids.py:127–128, :203, :213–216**
- `first_problems` is unbounded (about 480 printed lines on a full STOP).
- `session_set_sha256` is written from the constant, not measured.
- `_atomic_write` has no fsync.
- The manifest does not carry the render code's sha256 (the raw's Appendix A does).

**13. NIT — runner.py:18–19, :321–322; primitive.py:203; cells.py:100**
- The ORDER PIN still says "schema.ARM_CELLS order".
- `_report` hashes one read of each cell file and parses a second read.
- `read()`'s docstring still says "the cell's capture array".
- A missing array raises a bare FileNotFoundError instead of the module's SystemExit.

## (2) Mutants

Eight are killed by existing checks and twelve survive; each surviving one comes with the test that would kill it. A self-test that raises is reported by the driver as "<module>: its self-test ran to its end".

**Killed by existing checks**

| ID | Site | Change | Killed by |
|---|---|---|---|
| M4 | ids.py:237 | drop the sha256 check in `load` | "ids: a file whose sha256 is not the manifest's is refused" |
| M8 | verify.py:39 | `i > 0` → `i >= 0` | "verify: the spans' texts are the rendering up to the twelfth passage's end (G-2's convention)" |
| M9 | verify.py:111 | count every label candidate as ok | "verify: a label candidate whose ids do not decode to its texts is a problem" |
| M10 | verify.py:117 | drop `== expect_n` | "verify: three sessions where 160 are due do not PASS" |
| M12 | cells.py:197 | `arrays[l][n]` → `arrays[l][0]` | "cells: its self-test ran to its end" (`load_cell` refuses row 0) |
| M17 | probe.py:63 | `fold_seed=cv_seed` → `fold_seed=seed` | "probe: the null is the shuffles' 95th percentile on the statistic's own folds (k's kfold form)" |
| M18 | probe.py:60 | `cv_seed` → `seed` in `kfold_auc` | "probe: the AUC is k's grouped 10-fold, at the folds' seed" |
| M20 | primitive.py:363 | `range(layer + 1, …)` → `range(layer, …)` | "primitive: the captures are the band past the site (ADDENDUM-n1 §6.2)" |

**Survive (each needs a test)**

| ID | Site | Change | Test that would kill it |
|---|---|---|---|
| M1 | ids.py:175 | use the raw encode, without `_with_splits` (self-test sessions are runs 0–2, so no split applies) | Patch `sessions.RECORDED_SPLITS` and `ids.RECORDED_SPLITS` to a split on synthetic run 2 at a known character pair; re-synth that session; the render must PASS with every candidate kept. |
| M2 | ids.py:182 | drop `n_equal == n_ctx` | An encoder that shifts only the ids after the last generation prompt when the text contains "Either" (prefix holds, tails differ); the candidate must be dropped with tail_equal < contexts. |
| M3 | ids.py:161 | drop the N4 clause | Use the old `enc_n4` (moves token 0 when a told or sham line is present); the render must STOP with n4.ok == 0 and write nothing. |
| M5 | ids.py:242 | drop the record-count check | Rewrite MANIFEST's sessions `records` to 4 with the sha unchanged; `load` must refuse. |
| M6 | verify.py:78 | drop `ids_sha(ids) != s.ids_sha` (the decode check catches the existing case) | An alias decoder `chr(i % 1_000_000)` and one committed id +1_000_000; ids_ok must be 2. |
| M7 | verify.py:98 | drop the n_pre prefix comparison | Alias the N4 variant's first id and recompute its record's ids_sha; n4_ok must be 2. |
| M11 | cells.py:180 | drop `.copy()` on the hasher | After the "launch index not after" refusal, append a valid read with the same (cell, caps); the reload must verify. |
| M13 | cells.py:139 | drop the per-layer hash check | Tamper a row and rewrite that record's sha16 in the JSON; `load_cell` must refuse. |
| M14 | runner.py:516 | `loads_ms = [load]` only | Run with load_ms=111, resume with 222; the report must hold [111, 222]. |
| M15 | runner.py:132 | `arm_cells` → `ARM_CELLS[arm]` | `campaign_order` under `example_identity(R_ell=50.0)` and `40.0` must equal `read_plan` (6,400 reads at 50.0). |
| M16 | runner.py:445 | drop the ids_sha rendering check | An `ids_of` returning session 4's ids with one token changed must produce a rendering pause, read not launched. |
| M19 | probe.py:77 | `bm >= AUC_BAR` → `>` | `verdict` with band median exactly 0.90 and comparator max 0.85 must PASS. |

## (3) Observations

- **What checks out:**
  - ids.render produces §1.2 (i)–(iii) as ruled: 160 sessions with both assertions; 320 N4 sequences with the fixed join and `n4_schedule`'s zone, prefix to n_pre asserted; four candidates over 960 contexts with the splits applied to the full sequence; dropped candidates reported.
  - The manifest holds everything §1.1/§1.2 list, plus session-set and schedule digests.
  - `load` verifies what it claims.
  - G-VER asserts seq_len, ids_sha and the G-2 spans, and its report is pick-free.
  - kfold10 and its null share folds (`fold_seed = cv_seed`; perm_seed separate), as in k.
  - The PASS rule is §6.4's, with no per-layer condition; check_gread's median matches np.median for an even band.
  - Cells hash rows [0, capture_rows) as little-endian float32 in row order, and capacity 40/160 fits the plan.
  - There is no leftover single-array use inside n; gver-trial is decode-only; PRODUCTION includes ids.
- **Plan check is circular:** `campaign_order`'s plan assertion and `read_plan` both derive from `arm_cells`, so the assertion does not test the keeper mapping on its own (hence M15).
- **Drafts vs the render:** every draft's sha256 equals the render raw's Appendix A except schema.py. The render ran on draft 33419938…111d; S and HEAD hold 0ea39600…0db6. TOLD_LINE, SHAM_LINE, N_SESSIONS, N_FLOOR, BK_CELLS and SESSION_SET_SHA256 are unchanged between 14e65d8 and d791bd9, so the committed ids are unaffected. The BUILD entry should state the difference.
- **n_analyze.py at HEAD still reads the single-array form** (`capture_file` and a whole-file sha256 at scripts/n_analyze.py:1988–1992 and :3034). Its pin move, and the G-READ-n driver, must read and hash rows [0, capture_rows) per layer, not file bytes: the .npy files carry headers, zero rows and possibly a leftover row from a crash.
- **I/O cost:** each read costs 31–32 msync+fsync pairs, and the whole cell JSON is rewritten per append (about 1 GB over the campaign). This is outside the cap but inside pod hours; G-TIME-n should time it on the volume.
- **Comparator size:** the comparator medians use 40 sessions against the axis's 160. That biases the comparator's max upward, which makes PASS harder, so it is conservative, not a false-PASS route. It is worth a line in the lock.
- **Overlay guard:** under the scratch overlay, guard's REPO resolves to the overlay root, so at the render `refuse_out` guarded the overlay, not the repository. Once committed it guards the repository.

## Code's dispositions

By the review's numbers. Every change is in the n drafts or the driver; the committed `schema.py` (v5, `d791bd9`) is
unchanged. A reading left open is flagged in the BUILD entry, pending the seat.

- **1, BUG (a crash before a cell's first JSON leaves arrays that block every resume).** Applied.
  - At a cell's first read, `_write_row` creates each layer's array afresh ("w+"), whatever file of that name is
    there.
  - `append_record` refuses a first append while the cell's JSON is on disk, so "w+" never truncates rows a JSON
    names.
  - The module's docstring now states the crash case at n = 0.
  - Test: two orphan arrays beside a new cell, one float64 of another shape and one of garbage bytes. The append,
    the reload and every row hash verify. The test fails on the code the review read.
- **2, RISK (every cell's maps held open: file descriptors).** Applied: no map outlives its use.
  - `append_record` maps each layer's file for its one row, then writes, flushes, drops the map and fsyncs.
  - `load_cell` checks every layer through a read-only map and drops it. It keeps the arrays, read-only, only for a
    reader that asks (`keep_arrays`; G-READ-n's driver).
  - Between reads a cell is its JSON and its layers' running hashers. At most one map is open at a time, so the
    descriptor limit is neither raised nor logged.
  - Test: an append's and a load's `Captures` carry hashers only.
- **3, RISK (in-place writes on the box's network volume, untested there).** Applied in the box site check.
  - The package self-test runs there with its temporary directory on `/workspace`, where the stage root lies.
  - Its cells cases write rows in place, reload them through fresh maps and check every row hash: the round trip
    the finding asks for. The site-check raw holds the result.
  - `cells._fsync_file` keeps no tolerance for EINVAL or ENOTSUP. Code's reading: a refused file fsync stops the
    stage rather than passing silently. m's `_fsync_dir`, which tolerates both for directories, is imported
    unchanged.
- **4, RISK (the probe's artifact not tied to its run).** Applied.
  - `result` computes every layer through `layer_auc` at the module's `N_SHUFFLES` and `SHUFFLE_SEED`, on the
    caller's `cv_seed`. The shuffles and shuffle seed the artifact records are therefore the ones that ran.
  - `artifact` refuses layers other than the identity's `capture_layers` with a ValueError, and takes `cv_seed` with
    no default.
  - Left to the caller: one `cv_seed` passed to both `result` and `artifact`, since the schema's result has no
    `cv_seed` field. G-READ-n's driver passes the lock's value to both, a PIN for step 15.
  - The finding's third part, the analyzer re-checking `probe.layers` against the identity, is n-analyzer's code.
    Code passes it on with this raw.
  - Tests:
    - a spy on `layer_auc` sees the module's shuffles and seed and the default `cv_seed`;
    - the artifact over band 32..63 at 200 shuffles holds PASS, FAIL and NOT-COMPUTED results;
    - layers [32, 63] are refused;
    - layer data shorter than the layers is refused.
- **5, RISK (`loads_ms` loses an invocation that ends without a report).** Applied in part.
  - `load_ms` is now required, with no default.
  - The CAP pin and the field's comment say that `loads_ms` holds the invocations that wrote a report. An invocation
    that ends without one is absent from it, while its records still count in `used_ms`.
  - Not applied: persisting each load when it happens. That needs a file the schema does not define, so it is
    flagged for the lock.
  - Tests:
    - `loads_ms` is [111], then [111, 222];
    - on a root with a crashed invocation it is [31, 33, 36], and `used_ms` sums all 5 records on disk.
- **6, RISK (nothing pins MANIFEST.json).** Applied.
  - `verify(..., manifest_pin=ids.MANIFEST_OF_RECORD)` STOPs when MANIFEST.json's sha256 is not the pin. By default
    the pin is the committed render's, `7f51bd91…821d` (`d76f34f`). gver-trial uses the default.
  - The stage drivers' assertion that `manifest_sha256` equals the identity's `rendering_id` is wired with the stage
    commands, at their own steps: a PIN.
  - Tests:
    - a pin of 64 zeros STOPs;
    - the default pin is `MANIFEST_OF_RECORD`, and a synthetic folder STOPs on it.
- **7, RISK (no HF-path check of the band's premise).** Applied.
  - hftiny prefills with and without the injection at layers [1, 2]. It asserts exact equality at the site,
    layer 1, and a difference above 1e-3 at layer 2. This runs on the box only.
  - The box site check also runs a mutant that hooks the injection one layer early (b02). This check must kill it.
  - The primitive's own site check now places the injection through `_placed(...)[2]`, `read()`'s helper.
- **8, NIT (G-VER's count STOP).** Applied: "N sessions, not 160" is now the first problem line. Flagged for the
  seat: how a G-VER-STOP that is not a token mismatch counts in `rendering_mismatches`, which `check_report` requires
  to be ≥ 1 at a G-VER-STOP. Such a STOP comes from the session count, the manifest, the pin, the decoder or a label
  check.
- **9, NIT (tiling; the cue set).** Applied.
  - `span_problem` requires one span per turn: the first at 0, each from where the last ended, the last at `n_pre`.
  - Each kept label candidate must hold exactly the sessions' cues.
  - Tests: three untiled cases; a candidate missing one cue.
- **10, NIT (`_with_splits`' mismatch crashes the render).** Applied: it counts as the candidate's prefix failure,
  and the candidate is reported and dropped. Test: four candidates reported, the render STOPs, no exception, nothing
  written.
- **11, NIT (the driver).** Applied.
  - gver-trial refuses a `--model-dir` that is not an existing folder, before transformers is imported. It loads
    with `local_files_only=True`.
  - render-ids refuses an `--out` inside the repository unless it is `data/n/ids/` or under it.
  - `--selftest` is dispatched first.
  - Tests: three driver checks.
- **12, NIT (ids).** Applied in part.
  - Applied: `FIRST_PROBLEMS = 20`; `session_set_sha256` measured; `_atomic_write` fsyncs before its rename.
  - Not applied: the render code's sha256 in the manifest. MANIFEST.json is committed (`d76f34f`) and pinned. The
    render raw's Appendix A records the drafts' sha256s at the render.
- **13, NIT.** Applied.
  - The ORDER pin names `schema.arm_cells`.
  - `_report` parses the bytes it hashed.
  - `read()`'s docstring says "capture arrays".
  - A missing array stops with the module's SystemExit.

**The observations.**

- "Plan check is circular": answered by mutant M15's test. `campaign_order` under the example identity at
  `R_ell` 50.0 and 40.0 gives 6,400 and 5,280 reads, with 160 N1-P +1/2 reads at 40.0.
- "Drafts vs the render": the BUILD entry states every difference from the drafts the render ran (the render raw's
  Appendix A, `d76f34f`), among them schema draft `33419938…111d` against `d791bd9`'s `0ea39600…0db6`. The
  constants the ids depend on are unchanged between the two.
- "n_analyze.py at HEAD still reads the single-array form": passed to n-analyzer. Its step-2 draft reads no capture
  file (its PIN-n-31). G-READ-n's driver reads captures only through `cells.load_cell(..., keep_arrays=True)`, which
  hashes rows [0, capture_rows) per layer, never file bytes. That is Code's PIN to n-analyzer.
- "I/O cost": flagged for G-TIME-n, which times the reads with their writes on the volume.
- "Comparator size": flagged for the lock.
- "Overlay guard": true of the render run, whose `--out` lay in Code's scratch folder, outside both the overlay and
  the repository. Its files were placed under `data/n/ids/` in the commit window. Committed, the guard's root is the
  repository's.

## The mutant runs

**The harness.** A Code subagent wrote `run_mutants.sh` from Code's brief. It reads the 20 mutants from
`mutants.tsv` (`ed881b58…a4d4`): the review's M1–M20, each fitted to the fixed code.

Code read the harness in full and, before the run, made two changes (`5db8cc90…c9c4` → `3615cdbe…12bb`):
- **A baseline first.** One unmutated copy runs the self-test as every mutant does. If it does not exit 0, no mutant
  runs. The coordinating session suggested this: a copy missing a file the self-test needs would make every mutant
  read as KILLED.
- **`data/` copied whole.** The copy takes the overlay's `data/` in one piece, so that no command line spells the
  manifest folder's name. The overlay is Code's scratch copy, which the harness asserts lies outside the repository.
  The harness first asserts that the overlay's `data/` holds only `n/bk` and the manifest's folder, and that the
  folder holds only `manifest.json`. No path under the repository's `data/` was copied.

**How each run went.**
1. A fresh copy of the scratch overlay is made: HEAD's `valence_core`, with the drafts on top, plus `scripts/` and
   `data/` (BK's files and the model manifest).
2. One perl substitution is applied in the copy, asserted to match exactly once.
3. The package self-test (`scripts/n_sessions.py --selftest`) runs from the copy, under the jlens venv at
   `nice -n 19`, with `TMPDIR` in scratch and `PYTHONDONTWRITEBYTECODE=1`.
4. The copy is deleted.

The runs used one window the coordinating session granted for them, and nothing in the tree. The invocation, from
Code's scratch folder, was `PYTHONDONTWRITEBYTECODE=1 bash build/mut3/run_mutants.sh <the jlens venv's python>
overlay mut3_out`. Each self-test inherits that environment variable.

KILLED means a non-zero exit with a FAIL line or a raised self-test. Code read every output in full. 18 mutants were
killed by the check that names the invariant they break. M4 and M12 were killed by their module's self-test raising:
M12 as the review predicted. For M4 the review had predicted the sha256 check's own line; the tampered file was
parsed instead, and `ids`' self-test raised (JSONDecodeError).

**Result: baseline 217/217, exit 0; 20 of 20 KILLED.** No mutant survived, failed to apply, or errored, and the
harness exited 0.

**The 20 mutants** (the edit; what it breaks; the result, with the first check that failed):

- **M1** (`ids.py`): `full = _with_splits(s, [int(i) for i in encode(…)])` → `full = [int(i) for i in encode(…)]`.
  - Breaks: in `ids.render`'s label loop, the raw encode is used, and the recorded re-splits are not applied.
  - **KILLED**, 216/217, by "ids: a recorded split applies to the label loop's full sequences as to the session's
    (patched in for run 2)…".
- **M2** (`ids.py`): `kept = n_prefix == n_ctx and n_equal == n_ctx and sorted(tails) == labels` → the same without
  `n_equal == n_ctx`.
  - Breaks: a candidate is kept without the same tail in every context.
  - **KILLED**, 216/217, by "ids: a candidate whose tail differs between contexts, its prefix kept in all, is
    reported and dropped (tail_equal < contexts); the others are kept".
- **M3** (`ids.py`): `if rep["sessions"]["ok"] != len(sessions) or rep["n4"]["ok"] != 2 * len(sessions):` → the
  same without the N4 clause.
  - Breaks: failed N4 sequences no longer STOP the render.
  - **KILLED**, 216/217, by "ids: N4 sequences that move a token before n_pre STOP the render (n4 ok 0), and nothing
    is written". Under the mutant, `ids.render` went on past the failed N4 sequences and raised a KeyError in its
    label loop, which had no N4 base ids. The check caught the exception, and no report was returned.
- **M4** (`ids.py`): `if _sha256_bytes(data) != meta["sha256"]:` → `if False:`.
  - Breaks: `ids.load` no longer checks a file's sha256 against MANIFEST.json.
  - **KILLED**, 212/213, by "ids: its self-test ran to its end". The tampered file was parsed (JSONDecodeError).
- **M5** (`ids.py`): `if n != meta["records"]:` → `if False:`.
  - Breaks: `ids.load` no longer checks a file's record count.
  - **KILLED**, 216/217, by "ids: a manifest whose record count is not its file's is refused, every sha256
    unchanged".
- **M6** (`verify.py`): `if len(ids) != s.seq_len or ids_sha(ids) != s.ids_sha:` → `if len(ids) != s.seq_len:`.
  - Breaks: G-VER no longer checks committed ids against BK's `ids_sha`; the length check stays.
  - **KILLED**, 216/217, by "verify: committed ids whose ids_sha is not BK's are an ids problem even where they
    decode to the text".
- **M7** (`verify.py`): `if v[:s.n_pre] != ids[:s.n_pre] or ids_sha(v)` → `if ids_sha(v)`.
  - Breaks: an N4 sequence's tokens before `n_pre` are no longer compared with the session's ids.
  - **KILLED**, 216/217, by "verify: an N4 sequence whose tokens before n_pre are not BK's is an N4 problem, though
    its record's ids_sha and its decode agree with it".
- **M8** (`verify.py`): `if i > 0 else ""` → `if i >= 0 else ""`.
  - Breaks: `span_text` puts the closing end-of-turn and newline before the first span too.
  - **KILLED**, 211/217, by six checks. Among them is "verify: the spans' texts are the rendering up to the twelfth
    passage's end (G-2's convention)".
- **M9** (`verify.py`): `elif decode is not None and all(` → `elif True or all(`.
  - Breaks: every kept label candidate counts as ok, bypassing the decoder and the decode check. The cue-set check
    stays.
  - **KILLED**, 215/217, by "verify: without a decoder nothing textual is checked and G-VER does not PASS" and
    "verify: a label candidate whose ids do not decode to its texts is a problem".
- **M10** (`verify.py`): `problems: list[str] = []` → `problems: list[str] = []; expect_n = len(sessions)`.
  - Breaks: a session count other than `expect_n` can PASS. This is the adapted form: dropping `== expect_n` alone is
    now an equivalent mutant.
  - **KILLED**, 216/217, by "verify: three sessions where 160 are due do not PASS, and its line says so".
- **M11** (`cells.py`): `caps.hashers[l].copy() if n > 0` → `caps.hashers[l] if n > 0`.
  - Breaks: `append_record` advances the running hashers in place instead of copying them.
  - **KILLED**, 215/217, by "cells: after refused appends, a valid one on the same (cell, captures) reloads
    verified…".
- **M12** (`cells.py`): `arr[row_index] = row` → `arr[0] = row`.
  - Breaks: `_write_row` writes every row into row 0.
  - **KILLED**, 167/169, by "cells: its self-test ran to its end" ("record 0's layer 2 capture does not match its
    row"). The runner's self-test raised too.
- **M13** (`cells.py`): `if h.hexdigest() != cell["capture_sha256"][str(l)]:` → `if False:`.
  - Breaks: `load_cell` no longer checks a layer's written rows against `capture_sha256`.
  - **KILLED**, 216/217, by "cells: a tampered row whose record's sha16 is rewritten to match is refused by the
    layer's hash".
- **M14** (`runner.py`): `loads_ms = (list(prior["cap"]["loads_ms"]) if prior is not None else []) +
  [int(inputs.load_ms)]` → `loads_ms = [int(inputs.load_ms)]`.
  - Breaks: `loads_ms` holds only this invocation's load.
  - **KILLED**, 215/217, by "runner: loads_ms lists each reporting invocation's load in order, beside the cap and
    outside used_ms" and by the crashed-invocation case.
- **M15** (`runner.py`): `for did, labels in schema.arm_cells(arm, identity):` → `for did, labels in
  schema.ARM_CELLS[arm]:`.
  - Breaks: `campaign_order` reads the labels `ARM_CELLS` lists, with the keepers not applied.
  - **KILLED**, 216/217, by "runner: under merged dose maps each merged point is read once under its keeper…"
    (KeyError '+d_20').
- **M16** (`runner.py`): `if told is None and ids_sha(ids) != s.ids_sha:` → `if False:`.
  - Breaks: a session's ids are no longer checked against BK's `ids_sha` before a read, so there is no rendering
    pause.
  - **KILLED**, 216/217, by "runner: ids whose ids_sha is not BK's are a rendering pause before the read, which is
    not launched". The schema then refused the record at `ids_sha_bk`.
- **M17** (`probe.py`): `fold_seed=cv_seed` → `fold_seed=seed`.
  - Breaks: `layer_auc` computes the shuffle null on the permutation seed's folds, not `cv_seed`'s.
  - **KILLED**, 216/217, by "probe: the null is the shuffles' 95th percentile on the statistic's own folds (k's
    kfold form)".
- **M18** (`probe.py`): `kfold_auc(X, y, groups, K_FOLDS, cv_seed)` → `kfold_auc(X, y, groups, K_FOLDS, seed)`.
  - Breaks: the AUC is computed on the permutation seed's folds.
  - **KILLED**, 216/217, by "probe: the AUC is k's grouped 10-fold, at the folds' seed".
- **M19** (`probe.py`): `bm >= AUC_BAR` → `bm > AUC_BAR`.
  - Breaks: PASS needs a band median above .90, not at least .90.
  - **KILLED**, 216/217, by "probe: a band median exactly at .90, above the comparator's largest, PASSes (at least
    the bar: §6.4)".
- **M20** (`primitive.py`): `capture_layers=list(range(layer + 1, n_layers))` → `capture_layers=list(range(layer,
  n_layers))`.
  - Breaks: `test_identity`'s capture band starts at the site, not past it.
  - **KILLED**, 182/185, by "primitive: the captures are the band past the site (ADDENDUM-n1 §6.2)", by the band's
    first-layer check, and by the runner's self-test raising the schema's band refusal.

**At the box.** The second site check runs two more mutants that only the HF path can kill:
- **m05**, the HF backend's fresh path without its injection;
- **b02**, the adapter's injection hook one layer early (`int(inj.layer) - 1`), which hftiny's new AT-THE-SITE
  check must catch.

The site-check raw holds their results.
