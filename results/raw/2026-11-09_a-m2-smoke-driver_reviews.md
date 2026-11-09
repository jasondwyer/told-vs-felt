# The A-m2 smoke's driver — six rounds of blind code review (`time --smoke --smoke-out DIR` in `scripts/mf3_sessions.py`)

*Code's raw, PI date 2026-11-09.*
- *What was reviewed:* the smoke's driver (A-m2 v0.3 §3.2, §4.2; Code's P4, accepted at ans2 §3), built model-free in a scratch worktree at `daca8b0`.
- *How:* six rounds of blind code review. Each reviewer ran the driver's self-test and its own model-free probes and committed nothing. Every round's report says the self-test's own hash reads the bytes under `data/mf3/ckpt`, outside the traps (round 1 in its NOTE 7). Round 6 also discloses three `find` traversals into that directory (see Round 6).
- *This raw:* each round's report verbatim (local paths scrubbed to `<scratch>/` and `<home>/`), then Code's disposition. Each later round reports on the earlier round's items, and that report is the record of what was applied. Round 2 records two of round 1's NOTEs as not applied.
- *Nothing ran on a model.*

**The bytes each round reviewed** (sha256 prefixes):

| Round | Driver reviewed | Its tallies (MAJOR / MINOR / NOTE) |
|---|---|---|
| 1 | `cc55377c…` (Code's scratch copy; the report names no sha) | 0 / 7 / 8 |
| 2 | `b05c07cc…` (Code's scratch copy; the report names no sha) | 0 / 2 / 10 |
| 3 | `9591a418…` | 0 / 1 / 12 |
| 4 | `b55c4b36…` | 0 / 1 / 6 |
| 5 | `0b508640…` | 0 / 0 / 5 |
| 6 | `4a98f74e…` | 0 / 0 / 5 |
| committed | `c9393a48…`: round 6's bytes plus Code's dispositions of round 6 (§ Round 6) | not reviewed again (the coordinating session's instruction) |

**The stopping rule.** Round 5 came back with no MAJOR and no MINOR. The coordinating session then made round 6 the last ("Round 5 came back with 0 MAJOR and 0 MINOR on a driver that is never of record, so make round 6 the last … If round 6 finds no MAJOR or MINOR, stop adding review rounds. Apply its NOTEs or disclose them, and hold the driver ready to commit.", 2026-11-09). Round 6 found no MAJOR and no MINOR.

**What covers the dispositions of round 6:**
- the self-test on the committed bytes (202/202 on the commit's base);
- the mutation lane: 99 mutants of the smoke code, each applied over the driver with the smoke checks run in a fresh interpreter; all 99 are killed by a failing check, none by a crash.


## Round 1

### The report (verbatim)

**Blind review: the `time --smoke --smoke-out DIR` edit to `scripts/mf3_sessions.py`**

I found nothing MAJOR, 7 MINOR and 8 NOTE. The selection logic matches the spec. The most important item is MINOR-1: a mis-cased `--smoke-out` path gets past the "inside the repository" refusal on this Mac, so the smoke could write under `data/`.

File reviewed: `<scratch>/smoke-wt/scripts/mf3_sessions.py`. Line numbers are in that edited file.

**Self-test run.** In the worktree, `--selftest` gave 187/188 in 64 s, exit 1.
- The one FAIL is "A-m2 is committed at HEAD". A-m2 v0.2 is untracked there, so this is expected.
- The driver must therefore commit after A-m2 v0.2, as A-m2 §6 item 2 orders. If that commit changes the file's bytes, `ADDENDUM_M2_SHA256` has to change with it.
- `git status --porcelain --ignored` in the worktree was identical before and after the run.
- Output: `<scratch>/selftest_out.txt`.
- My edge-case probe of the domain builder (P1): `<scratch>/review_probe/p1_edges.py`.

**Checked and correct (1: spec):**
- **Forms:** the four forms are byte-equal to A-m2 §3.1. The pinned sha256 is 69e23212…cb47, which is the file's.
- **Text check:** the bullet parse reads the committed blob at HEAD, turns the escaped `\n` into a newline, and catches a wrong, missing, duplicate or extra form.
- **Cells and keys:** the cells are G-TIME-F3's committed schedule cells at s = 0. The item key is `m-f3-items-time|0`; the arm key is `m-smoke-f3|{form}|{template}|0`.
- **Draw order:** `SmokeScaffold.reasoning` calls the parent first, so the seed draw order and the order checks are m:159's.
- **P1 (the domain):** overlap is computed over the line including its newline, and a zero-length piece counts at either end of the line. The final unterminated fragment and `Response:` lines are out of the domain. The pick line is in as rendered. The label line is in under F-0 and F-c and out under F-a and F-b; F-b's opener is never in.
- **Match and counter (a):** the match is equality after `ws_norm`, case-sensitive, first index. Counter (a) (P2) is containment of a domain line, or `=== .+? ===`, tested on the `ws_norm` text.
- **Tally:** (i) is the union of the three classes, once per line, over all sessions including excluded ones.
- **Selection:** the key is (union, (a), F-a before F-b) over F-a and F-b only.
- **Stops:** F-0's union below 3, and the selected form's union at 3 or more.

**Checked and correct (2: P4's refusals):**
- The precheck is `time_precheck` minus the checkpoint checks, plus A-m2 and the forms' roster hygiene.
- The licence, startup checks and gate line run, and are printed after the load.
- The backend STOP fires on anything but a734dadec8f8ce9b.
- The `f3_config` substitution is restored in a `finally`.
- Task-round hair triggers stop the smoke; reasoning-line ones end only their session.
- Nothing ever constructs a path to the checkpoint, except one dict entry (NOTE 2).

**3: `time` without `--smoke`.** No behaviour change.
- `run_time` is untouched.
- The only new branch before it refuses `--smoke-out` without `--smoke` with exit 2. Before, argparse refused it, also with exit 2.
- The added imports load no new modules (I checked `sys.modules`).
- No new ambiguity in argparse's abbreviated options.

**4: self-test safety.** No case can load the model or run a session on it, and no case writes in the repository; all writes go to temp directories under `/var/folders`. The traps are not complete; see MINOR-7.

## MAJOR
None.

## MINOR

**MINOR-1 — `smoke_out_problems`, lines 704–710: a mis-cased path passes the inside-repo refusal.**
- **Problem:** "inside the repository" is decided by comparing resolved paths, which is case-sensitive. This volume is case-insensitive and `resolve()` keeps the case as typed.
  - I verified it: `<home>/Documents/code/JSPACE-LAB/data/mf3/smoke-x` is judged outside the repo.
  - Yet `os.path.samefile` says that spelling and the repo are the same directory.
  - The smoke would then write 13 files under the real `data/mf3/`, against A-m2 §3.2 and §4.2.
- **Fix:** decide by file identity. Take the deepest existing ancestor of the resolved path and refuse if it, or any of its parents, is `os.path.samefile(…, REPO)`. Add a self-test case that uses a case-swapped spelling of `REPO/data/...`.

**MINOR-2 — `run_smoke_sessions`, lines 837–848: an exception after a session can lose it.**
- **Problem:** the session's JSON and its raw block are written only after both `smoke_verify` and `smoke_line_reads`.
  - `smoke_line_reads` and `smoke_harness_lines` can raise `ValueError` (unknown piece kind, empty harness line), `IndexError` or `KeyError`. A malformed record is most likely right after G-VER has failed.
  - `run_smoke` catches only `SystemExit`. So the run would end in a traceback with exit 1, which the docstrings at 26–32 and 878–881 do not mention.
  - The session just generated (about 5 minutes of Qwen) would then be in neither the JSON nor the raw.
  - The empty-line `ValueError` cannot fire today, because Qwen's texts are stripped and the pool holds no newlines. My probe shows it does fire on a model text ending in `\n`.
- **Fix:**
  - Write `{form, form_bytes, g_ver, record}` and print the transcript and rounds right after `smoke_verify`.
  - Compute the reads inside `try/except Exception`, rewrite the JSON with what exists, then raise `SystemExit("READS (A-m2 smoke): … -- the smoke stops")`.
  - Document exit 1 and 130 for other exceptions, as `run_time` does.

**MINOR-3 — line 761: the transcript block prints model text raw.**
- **Problem:** control characters — carriage return, ANSI/ESC sequences, DEL; F-p13's class — land unescaped in the raw. Viewed in a terminal, a carriage return overwrites the line and ANSI codes can hide text. Also, a model-written newline looks like a harness line break. Rounds and reasoning lines are already printed with `repr`; the transcript is not.
- **Fix:** escape non-printable characters line by line (a translate table for C0, C1 and DEL, or `repr` per line). The JSON keeps the exact bytes.

**MINOR-4 — self-test, lines 2172–2179: the G-VER tamper check does not test what it claims.**
- **Problem:**
  - It verifies an F-a record as F-0. That changes the arm key, so the refusal is "keys differ" / "seed differ" (the self-test output shows exactly these), not "its blocks differ". The block-bytes comparison is never isolated.
  - `piece` is used only in a tautology (`piece["kind"] == "reasoning"`).
  - `real_cfg` is captured after the twelve stub-run `smoke_verify` calls. So `sc_mod.f3_config is real_cfg` cannot catch an earlier failure to restore.
- **Fix:**
  - Change one byte of the reasoning piece in an F-a record's transcript, keeping the keys, and verify it as F-a. Expect `template_breakage` on the transcript bytes.
  - Capture `f3_config` at the top of `_selftest_smoke`. Check identity there, and again after a `smoke_verify` call whose `verify.verify_session` is patched to raise `SystemExit`.

**MINOR-5 — self-test, lines 1900–1907 and 2192–2195: the defect classes and their union are never exercised.**
- **Problem:** the stub never scripts an empty or cap-reach line. So none of these ever runs:
  - the union over overlapping classes;
  - the pass-through of `empty` and `cap_no_newline` from the package audit;
  - P1's branch for a zero-length piece at the start of a line (an empty F-0 or F-c line).
- The check asserts `union == echo + empty + cap - 0`. That holds only because empty and cap are 0, and it would fail on a correct tally once a whitespace-only line at the cap appears (empty and cap_no_newline both set).
- **Fix:**
  - Script `{"text": "", "n_tok": 60, "cap_hit": True, "stop_reason": "cap"}` lines in an F-0 and an F-a session, plus a run-on cap line.
  - Assert union = the number of lines with at least one class, with empty and cap counted per form.
  - Assert P1's domain on that record (the empty line is out, and no `ValueError`).

**MINOR-6 — `run_smoke` lines 898–923 have no test coverage.**
- **Problem:** this Qwen-branch sequence is copied from `run_time` but never exercised:
  - prechecks refused together in one REFUSED line;
  - the lock-revision refusal;
  - the DRIVER line, then the SNAPSHOT line;
  - the load;
  - the re-read refusal, the moved-revision STOP and the model-id STOP.

  Every smoke CLI case stops at the output directory or the flags, so the loader trap is never reached.
- **Fix:** add `run_time`-style cases for `run_smoke`, patching `smoke_precheck`, `driver_problems` and `qwen_snapshot`, using a loader trap or a stand-in, and trapping `run_smoke_sessions`. Assert exit codes, line order, and that no session runs.

**MINOR-7 — self-test CLI cases, lines 2117–2128: only the loader is trapped.**
- **Problem:** there are no checkpoint or `run_gate_stage` traps here. If the `--smoke-out`-needs-`--smoke` refusal at 2280–2282 ever regressed, a self-test case would fall into `run_time`'s precheck. That precheck `json.loads` the real `data/mf3/ckpt/Q-F3_time.json` (`rs.refuse_ended`, `rs.pending_at`), which m:318 forbids. `_selftest_time` guards its own time cases this way.
- **Fix:** run the CLI block under `stub_run`'s three checkpoint traps, plus a `stages.run_gate_stage` trap.

## NOTE

1. **Order after the load (811–829) differs from P4's bullet order.** The licence runs after the startup checks and the laptop checklist, and the backend STOP comes before `f3_startup` and the renders. This is the stage's own `_begin` → `_licensed` order, and it STOPs earlier. Say so in the entry, or reorder.
2. **`stages.out_paths(SMOKE_STAGE)` (731, 828; self-test 1850–1851) builds a dict holding the checkpoint's path.** The entry is unused, but the path is constructed. `schedule.DEFAULT_OUT` gives the schedules directory without ever forming it.
3. **Exit is 0 even when a §3.3 stop fires** ("adopted: none"). This matches the docstring, but anything reading only the exit code sees success. Consider a distinct exit code, or a `STOP:` line on stderr.
4. **`out_dir.mkdir` (829) runs after the load.** If the parent vanished in the meantime (the scratchpad's midnight cleanup) or is not writable, an uncaught `OSError` follows. Check writability in `smoke_out_problems` and turn an `OSError` at mkdir into a STOP. Also, the JSONs are the only copy of the read probabilities (`p_a`/`p_b`), so they should not sit in the scratchpad, which is cleaned after about 4 days.
5. **The raw could also carry:**
   - an A-m2 line (its sha256, committed, the four forms parsed equal) beside LICENCE;
   - the provenance record;
   - each read's `p_a`, `p_b` and label-mass flags ("every read" currently prints the menu and the pick only);
   - scaffold hits on the round and line entries.
6. **Self-test nits:**
   - `dom_c` (2035) is unused.
   - The stub run's "the loader never reached" (1955) is true by construction under the seam, so it tests nothing.
   - The F-0 domain check (1977–1986) claims round headers but counts only Task lines.
   - The dedup check (around 1987–2016) says "headers repeat", but only the pick line can repeat.
   - "package classes beside" (2032) checks only that the key exists. It could assert `[]` on the F-0 banner echoes.
   - The stdout check (2071) verifies one transcript (`docs[4]`) by line presence. Check all twelve within their own blocks, and count the round, line and read lines.
   - "names no checkpoint" (2205–2207) is a string check. An `open()` trap on `data/mf3/ckpt/` during the stub runs would actually test "never opens".
   - Nothing checks F-0 against `banner.reasoning_block(n)` for n = 5–10.
   - The backend-of-record success path is never shown to proceed.
7. **Scope of the self-test's integrity check:** it hashes every byte under `data/` (including `data/mf3/ckpt/`, as `_selftest_time` already does for `data/mf3`), and only `data/`. Comparing `git status --porcelain --ignored` before and after would cover "nothing written in the repository".
8. **Smaller items:**
   - The `adapter_factory` seam lets a non-stub adapter skip the precheck, driver and snapshot checks; refusing non-stubs there would close it.
   - The `smoke_tally` docstring's "(i) under each scope" is stale.
   - P2's per-template tally of counter (a) is not computed; it can be derived from the raw.

### Code's disposition

**Code's disposition of round 1.** 13 of the 15 items were applied in round 2's bytes. Round 2's "Round-1 items closed" reports on each.
- **NOTE 1 was not applied** (round 2: "not applied, and harmless"). The order after the load is not P4's bullet order. The startup checks, the laptop checklist and the licence come in the stage's own order (`_begin`, then `_licensed`), and the smoke's own checks follow. NOTE 1 asked that this be said in the entry, and the driver's entry says it.
- **NOTE 7 was not applied** (round 2: "rightly not applied"). It proposed a `git status` comparison before and after, and `stages._git` bars status. The `data/` hash stood in. The write traps, from round 4's bytes, now cover the guarded writes NOTE 7 was after; rmdir, shutil, links, truncation and io.FileIO stay outside them.


## Round 2

### The report (verbatim)

**Round-2 blind review of `scripts/mf3_sessions.py` (smoke-wt, base `daca8b0`)**

No MAJOR, 2 MINOR, 10 NOTE. The production changes are correct; both MINORs are gaps in the self-test.

**What I ran** (nothing edited, staged or committed in either tree)
- `--selftest` in the worktree: 191/192 pass. The one FAIL is the by-design "A-m2 v0.2 is committed at HEAD". Output: `<scratch>/am2/r2rev_selftest.txt`
- `git status --porcelain --ignored` in the worktree was identical before and after the self-test and my probes. The main tree is untouched.
- Four model-free probes in `<scratch>/am2/r2rev/` (`probe1.py` to `probe4.py`). They import the driver from the worktree and write only to the scratchpad.
- I opened nothing under `data/mf3/ckpt`. The self-test's own `tree_state` hash does read it, as `_selftest_time` already does.

**Round-1 items closed**
- **MINOR-1 closed.** `_within_repo` refuses every alternate spelling I tried:
  - case-swapped spellings, including deep non-existent tails and the repo itself;
  - the firmlink spelling `/System/Volumes/Data/...`;
  - the `/tmp` symlink spelling;
  - paths with `..` and `.` segments.
  - It admits a fresh scratch path. I found no wrong refusal: the walk compares only existing, symlink-free ancestors by (st_dev, st_ino). The self-test's case-swapped case would fail under the old check. One leftover: NOTE 1.
- **MINOR-2 closed.** The record is written and printed before the line reads. A read that raises gives `lines: None` plus `lines_error`, a rewrite, then a READS STOP (exit 4). The self-test case can tell the old order from the new. Leftover: NOTE 2.
- **MINOR-3 fixed in code.** probe3 confirmed it end to end: the raw shows the escapes and the JSON keeps the bytes. Its regression test is incomplete: new MINOR-1.
- **MINOR-4 closed.** The tamper now changes only the reasoning block's bytes of an F-a record, verified as F-a with its keys kept, and gets "transcript bytes differ". `real_cfg0` is captured at entry, and `f3_config` is checked to be restored after a G-VER that raises.
- **MINOR-5 closed.** The stub now has an empty line at the cap (the realistic shape: `lines.py` says a whitespace-only line runs to its cap) and a run-on cap line. The union counts the empty+cap line once (F-0 is 10, not 11). The rule now selects by the union: F-b (0) over F-a (1), although (a) is 3 against 0.
- **MINOR-6 closed.** Six stand-in cases: precheck refusal, revision refusal, clean order, SNAPSHOT MOVED, MODEL ID, RE-READ REFUSED. Leftover: NOTE 5.
- **MINOR-7 closed.** The CLI cases run with the checkpoint functions, `run_gate_stage`, `run_smoke_sessions` and `open()` trapped.
- **Round-1 NOTEs:**
  - NOTE 2, 4, 5 and 8: closed.
  - NOTE 3: closed by documentation (exit 0 whatever the §3.3 stops say; the SMOKE STOPS line reports them).
  - NOTE 1: not applied, and harmless. The post-load order follows the stage's `_begin` then `_licensed`, and BACKEND stops the run before `f3_startup`.
  - NOTE 7: rightly not applied. `stages._git` forbids diff and status (m's finding R4); the `data/` hash stands in.
  - NOTE 6: addressed as far as the delta shows.

**The new mechanisms are sound**
- **Stub-only seam:** it refuses a non-stub before any session, and the output directory is never made.
- **`open()` traps:** every use enters them through an ExitStack, which restores them in reverse order even on SystemExit. probe4 ran `_selftest_smoke` in-process: afterwards `builtins.open`, `io.open`, `scaffold.f3_config` and the patched module globals were all the originals.
- **Nothing breaks under the traps:** imports go through `_io.open_code`, and subprocess pipes and tempfile fds are integers, so they pass through. The remaining gaps are in NOTE 7.

**MINOR-1 — `mf3_sessions.py:2192-2195` (also `:2180-2191`, `:1997-2008`)**
- Problem: the check is named "the raw escapes non-printable characters" but only unit-tests `_printable`. `blocks_ok` applies `_printable` to both sides, and no stub transcript holds a control character. If `_printable` were removed from `:788`, every check would still pass, so round-1 MINOR-3's wiring has no regression test.
- Fix:
  - Script one control-character response in `rule_default`, e.g. F-c A2s forced round 0 → `"fine\x1b[0m\x7f here"`. In probe3 such a text (on F-0 A1s) stayed unclaimed, G-VER clean and line-readable; check the chosen slot's claim.
  - Assert that `out` holds `Response:fine\x1b[0m\x7f here` in escaped form.
  - Assert that no raw `\x1b` or `\x7f` byte occurs in `out`.
  - Assert that the session JSON's transcript keeps both bytes.

**MINOR-2 — `:2429-2440` (also `:2303`)**
- Problem: the real `smoke_precheck` never runs under `traps()`. It is the "time_precheck less the checkpoint's" that P4 promises, yet:
  - `pre_m` and `pre_f` call it with no traps;
  - `qwen_case` replaces it with a stand-in;
  - the stub runs skip it.
- Its "names no checkpoint" check reads only problem strings. A precheck that silently called `checkpoint_path`, `refuse_ended` or `pending_at` would pass. This is the same class as round-1 MINOR-7.
- Fix: run both calls inside an ExitStack with `*traps()`, and add `len(ckpt_calls) == n0 and not opened_ckpt` to the precheck check.

**NOTEs**
1. **`:706` (also `:729`, `:731`).** On Python 3.12.9, `Path.exists()` and `is_dir()` re-raise EACCES. A `--smoke-out` under an unsearchable directory escapes as a PermissionError traceback before the load, with nothing written (probe1). This was already possible at `:729` in round 1. Fix: catch OSError around the walk and the later checks, and return a REFUSED problem.
2. **`:889-904`.**
   - The second `write_text` truncates the file before rewriting it, so ENOSPC, EIO or a signal during that write destroys the record the first write saved.
   - The first write also comes before the raw print, so a failed write loses the session from both copies, as a traceback.
   - Fix: print the block first (stdout is the committed raw), write via a temp file and `os.replace` (`rs.atomic_write_json` fits), and turn an OSError on either write into a STOP. Optionally keep `traceback.format_exc()` in `lines_error`.
3. **`:771-774`.** `_printable` cannot be reversed unambiguously: a literal backslash sequence in model text prints the same as an escaped control character. probe2: `_printable("a\x1bb") == _printable("a\\x1bb")`. The `!r` views of rounds and lines stay unambiguous. Fix: escape the backslash too (`c.isprintable() and c != "\\"`), or state the ambiguity in the docstring.
4. **`:2254`, `:2234-2249`.** The conjunct `(not case_insensitive or "case-swapped spelling" in outs)` is always true. The refusal cases also assert only that problems are non-empty, not which refusal fired. Fix: assert each message ("inside the repository" for repo, data, link and case-swapped; "not writable" for `ro`; and so on) and drop the vacuous conjunct.
5. **`:2311`, `:2318`.** "Precheck problems are refused together" is tested with a single planted problem. Fix: plant a driver problem and a snapshot problem alongside it, and assert all three appear in the one REFUSED line with nothing loaded.
6. **Wording.**
   - `:1860-1863`: the docstring says `run_smoke_sessions` is a trap in every case that could reach the Qwen branch; in `qwen_case` (`:2303`) it is a stand-in.
   - `:2441-2443`: "no open() under data/mf3/ckpt was made" is not true of the self-test itself, whose `tree_state` reads every file there (hash only, outside the traps). Limit the claim to the trapped smoke paths.
   - `:2187`: the check says "then twelve SMOKE SESSION blocks", but the order is not checked.
7. **`:2441-2443`, `:1888-1898`.**
   - The final check could assert `not loads`, `not ckpt_calls`, and `builtins.open is real_open and io.open is real_io_open`. Today the stub runs after the CLI check rely on their message checks to notice a trap firing.
   - The guard ignores bytes paths, and it compares spellings — the class of bug MINOR-1 fixed — so a case-variant ckpt path would slip through. No smoke code builds one; `os.fsdecode` plus a samefile walk would close it.
8. **`:700`, `:773`, `:887`, `:1901`, `:2278`.** These cite "the review's MINOR-1/2/3/6/7, NOTE 6". The file already cites the time wiring's review the same way: "MINOR-2" at `:353`, "NOTE 3" at `:487`, "MINOR-1" at `:1083`, "NOTE 12" at `:1119`. Once committed, "the review's MINOR-1" and "MINOR-2" each name two different findings. Fix: qualify them, e.g. "the smoke review's round-1 MINOR-2".
9. **`:858-863`.** `rs.backend_identifier(adapter.provenance())` sits outside the PROVENANCE try. A provenance that `provenance_record` accepts but `_assert_native` refuses (a numpy scalar) would raise TypeError, giving a traceback after the load. This is theoretical for Qwen: the stage has the same pattern and ran. Fix: compute `bid` from the recorded `prov`, or move the call inside the try.
10. **`:1920-1921`, `:2443`.** `tree_state` hashes all of `data/`, every checkpoint included. It will FAIL spuriously if a parallel session in the shared tree writes under `data/` during the minute-long self-test. `_selftest_time` scopes its hash to `data/mf3`. Consider the same scope, or say so in the check's name.

### Code's disposition

**Code's disposition of round 2.** All 12 items were applied in round 3's bytes, NOTE 6's three wording items included.
- Round 3's "Round-2 items" reports on each, except NOTE 6, which it "can't map … to a specific hunk without its text". Round 3's delta applies it.
- The residuals became round 3's own items.


## Round 3

### The report (verbatim)

**Round-3 review of `scripts/mf3_sessions.py`: 0 MAJOR, 1 MINOR, 12 NOTE**

The reviewed file is in the worktree at daca8b0, sha256 `9591a418…ac62`. Running `diff` from `driver_pre_r3.py` to this file gives exactly `r3_delta.diff`.

**What I ran**
- `--selftest` in the worktree: 191/192 in 64 s. The one FAIL is the expected "A-m2 v0.2 is committed at HEAD".
- My own model-free probes, in `<scratch>/r3review/exp/`. They loaded the driver under an audit hook that stops on any open under `data/mf3/ckpt` and on any write-mode open inside the worktree. The hook never fired.
- Afterwards the worktree was unchanged: same git status, same sha256, no new `__pycache__`.

**Disclosure:** the allowed `--selftest` reads the bytes of `data/mf3/ckpt/Q-F3_time.json` (tracked in the worktree) to hash them. Both `tree_state` closures do this: the smoke's (1946) and the time test's (1171). I saw only the hash comparison, never the contents.

## MAJOR
None.

## MINOR-1 — the round-3 write path has no regression check (860-866, 910-928, 957)
- **Problem:** no self-test case makes `_smoke_write`, or the mkdir at 895, fail. So all three of these mutants would pass the suite: `_smoke_write` reverted to a plain `write_text`; its `except OSError` removed; the round-2 order (write, then print) restored. When every write succeeds, no check can tell them from the current code.
- **The code is correct today.** I ran a stub through the seam with `rs.m_resume.atomic_write_json` wrapped to raise:
  - ENOSPC at call 1: exit 4, `STOP: OUT DIR (A-m2 smoke): OSError writing 01_F-0_A1s.json -- the smoke stops`. One SMOKE SESSION block with its transcript on stdout; the output directory empty; no `.tmp`.
  - At call 2: exit 4; the first JSON intact, with `lines` None.
  - At call 25 (summary.json): exit 4; all twelve session JSONs intact.
- **Fix:** add those cases to `_selftest_smoke` with `mock.patch.object(rs.m_resume, "atomic_write_json", ...)`, failing at call 1 and at call 2. Assert:
  - rc 4 and "OUT DIR" in stderr;
  - `out.count("SMOKE SESSION ") == 1`, with that session's transcript lines present;
  - the files are `[]`, then `[01_F-0_A1s.json]` with `lines is None`;
  - no file name ends in `.tmp`.

## NOTEs

**1. `_smoke_write` catches only OSError (865).**
- **Problem:** other write failures escape `run_smoke` as a traceback (exit 1, no STOP line):
  - m's `json_text` raises TypeError for non-native values and ValueError for NaN/Inf;
  - the UTF-8 write raises UnicodeEncodeError for a lone surrogate.

  This contradicts the comment at 910-912 ("a write that fails ... is a STOP, not a traceback").
- **Evidence:** in the probe, numpy.float64, a tuple key, a set, an OrderedDict, NaN and a lone surrogate all escaped. Serialization runs before the disk is touched, so nothing on disk changes.
- **Likelihood is low:** the stage's `record_session` applies the same `_assert_native` to the same runner record, `write_checkpoint` uses the same `allow_nan=False`, and G-TIME-F3's Qwen records passed both.
- **Fix:** catch `(OSError, TypeError, ValueError)`, or narrow the comment to OSError.
- **Also:**
  - the message reduces ENOSPC, EIO and EACCES to the bare class name; add `errno.errorcode.get(e.errno)`;
  - a directory-fsync error after `os.replace` (an errno other than EINVAL/ENOTSUP) stops the smoke even though the file is already written.

**2. The comment "loses nothing the run produced" (911-912) overclaims when the first write (919) fails.**
- **Problem 1:** the line reads are computed only after that write, and `smoke_session_lines` prints nothing per reasoning line (n_tok, cap_hit and stop_reason appear for task rounds only). The cap-reach part of (i)'s union is then in neither stdout nor the output directory.
- **Problem 2:** the session block is now built before any write, so an exception inside `smoke_session_lines` (913) loses the JSON too. Round 2 wrote first.
- **Fix:** compute `reads` (inside its existing try) and print both blocks before a single atomic write. Alternatively, add one line per `rec["reasoning"]` entry to the session block (n, n_tok, cap_hit, stop_reason, classes).

**3. The open() guard has no positive control (1913-1923).**
- **Problem:** nothing in the suite opens a path under `data/mf3/ckpt`, so every check passes whether the guard fires or not. A regression in the guard alone would survive, for example the bytes handling reverted or the `_within` test replaced by `False`. Three checks rely on the guard: 2080, 2503-2505, 2507-2512.
- **Fix:** build `g = guarded(lambda *a, **k: "opened")` and call it directly:
  - the str, bytes and Path forms of `ckpt_dir/"probe.json"`, and its swapcase spelling, must each raise SystemExit;
  - a temp path must return "opened";
  - then clear `opened_ckpt`.

  Because the opener is fake, nothing is opened even if the guard fails.

**4. Refusal cases (2266-2303): round-2 NOTE 4 is only partly closed.**
- **Problem 1:** the "exists" test directory is literally named `exists`. Every message for that path contains the expected substring, so the message check there is vacuous.
  - Fix: rename the directory to `present`, or expect `": exists; the smoke writes a new directory only"`.
- **Problem 2:** `case_insensitive == ("case-swapped spelling" in outs)` (2303) is true by construction, the same vacuity as round 2's form. `_short` also cuts the diagnostic at 160 characters, so a skipped case-swap is invisible in the PASS line.
  - Fix: put `case_insensitive` first in the diagnostic, or require it on darwin.

**5. The EACCES handling depends on the Python version (739-747).**
- **Evidence:** on 3.14.6, `Path.exists`, `is_symlink` and `is_dir` return False on EACCES; on 3.12.9 and 3.13.3 they raise PermissionError. I tested all three. A verbatim copy of the round-3 code run under 3.14 reports the unsearchable case as "its parent is not a directory", so the self-test's "cannot be examined" check would fail.
- **Not live:** the venv is 3.12.9.
- **Fix:** classify with `os.lstat(r)` (FileNotFoundError or NotADirectoryError means absent; any other OSError means "cannot be examined") and `os.stat(r.parent)` with `S_ISDIR`.

**6. The chmod-based cases cannot fire when run as root (2286-2287).**
- **Problem:** "parent not writable" (from round 2) and the new "parent unsearchable" both depend on permission bits that root ignores.
- **Not live:** this driver runs on the laptop only.
- **Fix:** skip both under root and say so in the diagnostic.

**7. Totality claim in the `_selftest_smoke` docstring (1885-1888).**
- **Problem:** it says "every smoke path runs with ... trapped", but these run outside `traps()`:
  - the refusal cases (`smoke_out_problems`);
  - the keys/config checks (`smoke_config`, `sc_mod.f3_config`);
  - the P1 and line-read checks on records;
  - `smoke_verify` on the tampered record;
  - `time_identity_extra`;
  - `addendum_m2_problems`.

  None of them can plausibly reach the checkpoint, so this is a wording problem.
- **Fix:** narrow the sentence, or enter `traps()` once after `data_before` and leave it before the final `tree_state`.

**8. Narrowing the hash to `data/mf3` (1946, round-2 NOTE 10) loses coverage.**
- **Problem:** it removes the only check that the smoke writes nothing elsewhere in the repository (data/m, data/olmo, results/raw, the root).
- **Fix (flake-free and wider):** in `guarded`, also raise on any `w`/`a`/`x`/`+` mode open where `_within(pth, REPO)`.

**9. "Refused together in one REFUSED line" is not quite what is asserted (2367-2374).**
- **Problem:** the check asserts that "REFUSED" appears once and that each planted string appears somewhere on stderr, not that one line carries all three.
- **Fix:** `sum(ln.startswith("REFUSED") and all(x in ln for x in planted) for ln in q_pre[2].splitlines()) == 1`.

**10. `r.is_symlink()` at 740 is dead code.**
- **Problem:** `r` is already resolved, so the check never sees a link. In the probe, a dangling `--smoke-out` link pointing outside the repository was accepted, and the smoke would create the link's target. That is harmless (new, outside the repository), but the check reads like a guard.
- **Fix:** test `os.path.lexists(Path(smoke_out).expanduser())` before resolving, or drop the check.

**11. `rs.m_resume.atomic_write_json` (864) reaches through mf3.resume's import of m's module.**
- **Fix:** use mf3's own declared alias `rs.atomic_write_json` (resume.py:52), as stages.py:814 does.

**12. Out of scope, but it affects the evidence: the author's mutation lane over-counts.**
- **Problem:** `am2/mut/lane.py` excludes failures matching `"A-m2 is committed at HEAD"`, which never matches the real check name ("A-m2 v0.2 is committed at HEAD ..."). So every mutant counts the expected failure, and every "first:" column shows that check instead of the one that actually killed the mutant.
- **Impact:** in `lane_r3b` all 44 mutants have at least 2 fails or crashed, so no mutant was falsely reported killed, but every count is one too high.
- **Fix:** correct the substring before citing the lane.

## Check 1, item by item
- **`_within`:** it terminates (q shortens until it reaches `/`). It steps over EACCES: a case-swapped spelling under an unsearchable directory still returned True. It compares by `Path.parents`, so a sibling prefix (Root2 vs Root) returned False. With an absent root it falls back to comparing spellings. No wrong path was admitted.
- **Atomic writes:** see MINOR-1 and NOTEs 1-2. No `.tmp` file was left on any failure, because atomic_write_json deletes it. A SIGKILL mid-write could leave one, but only inside the smoke's own output directory.
- **`_printable`:** I decoded its output back over 20,000 random strings (backslash, x/u/U, digits, C0/C1, DEL, U+2028, a lone surrogate, NBSP, a tag character). There were 0 round-trip failures, and the output was always printable. The escaping is unambiguous.
- **`_within` inside the open hook:** no recursion, since it uses only stat and realpath and never opens. Cost is about 110 µs per call at depth 23. There are about 155 path opens per stub run, so roughly 20 ms per run. The self-test still passes 191/192. The remaining gap is NOTE 3.
- **Print-then-write:** correct for OSError (shown by the probe). Its trade-offs are NOTE 2.

## Round-2 items
- **Closed:** MINOR-1; MINOR-2; NOTE 1 (on 3.12/3.13; 3.14 is NOTE 5 above); NOTE 3; NOTE 5 (small leftover: NOTE 9 above); NOTE 8; NOTE 9; NOTE 10 (coverage leftover: NOTE 8 above).
- **NOTE 2:** closed for OSError. What remains is MINOR-1 and NOTEs 1-2 above.
- **NOTE 7:** closed in code. What remains is NOTE 3 above.
- **NOTE 4:** partly closed; see NOTE 4 above.
- **NOTE 6:** I found nothing in the delta beyond NOTE 7 above. I can't map NOTE 6 to a specific hunk without its text.

### Code's disposition

**Code's disposition of round 3.** 12 of the 13 items were applied in round 4's bytes, and NOTE 12 to the mutation lane.
- NOTEs 5 and 6 were "not live" and were applied anyway: an `os.lstat`/`os.stat` classifier for the out directory, and the permission cases skipped under root.
- NOTE 12 was applied to Code's mutation lane, outside the driver. The lane excluded the dev-only check by its name, "A-m2 is committed at HEAD". Round 1's fixes renamed that check "A-m2 v0.2 is committed at HEAD", so the exclusion stopped matching.
  - The lanes of rounds 2 and 3 counted the dev-only failure, so each mutant's fail count there was one too high.
  - No mutant was falsely reported killed: every mutant in those runs failed two or more checks, or crashed.
  - The exclusion now matches the name by pattern.
- Round 4's "Round-3 items" reports each one.


## Round 4

### The report (verbatim)

**Round-4 review of `scripts/mf3_sessions.py`: 0 MAJOR / 1 MINOR / 6 NOTE**

The file reviewed is the worktree's driver, sha256 `b55c4b36…`. `r4_delta.diff` is exactly `diff -u driver_pre_r4.py driver_r4b.py`, and `driver_r4b.py` is byte-identical to the worktree's driver. All three of the author's claims hold: the re-pin, the §3.3 clause and the round-3 fixes. The residuals are below. Line numbers refer to the round-4 bytes.

## MINOR-1 — `--smoke-out` with an unknown `~user` crashes instead of being refused (mf3_sessions.py:753)
- **Problem:** round 4 moved `given = Path(smoke_out).expanduser()` outside the `try` at 754-757. `expanduser()` raises RuntimeError for an unknown user on 3.12, 3.13 and 3.14.
- **Scenario:** `time --smoke --smoke-out '~scratch/am2' …` (a missing slash). Through `main()` the RuntimeError escapes, giving a traceback, exit 1 and no REFUSED line. The round-3 bytes refuse the same input with `does not resolve (RuntimeError)`, exit 2.
- **Impact:** nothing is loaded or written. I still rate it MINOR because it is a regression in the function this delta rewrote, it breaks run_smoke's "2 refused before the load", and no case tests the "does not resolve" branch.
- **Fix:** put the `expanduser()` back inside the try and also catch ValueError (an embedded NUL through the API; argv cannot carry one). Add refusal cases `~selftest-no-such-user/x` and a symlink loop, both expecting "does not resolve".

## NOTEs

**1. The new positive controls test the guard factories, not what `traps()` installs (2024-2035, 2054-2089).**
- **Scenario:** remove any one guard from `traps()`: the os.mkdir, os.open or os.replace patch, or the builtins/io.open pair. Each of those four mutants passes all 34 non-dev smoke checks.
- **Consequence:** nothing shows that the checkpoint-open trap or any write trap is actually live during the stub runs. Several claims rest on that: the "never reached" and "wrote inside the repository" checks (2225-2230, 2482-2483, 2724, 2732-2739) and "the guards have their own positive controls" (1952).
- **Fix:** inside one `traps()` stack, fire each installed guard on a path whose parent does not exist (assert that first):
  - `open(ckpt_dir/"selftest-absent.json")`;
  - `open(REPO/"selftest-absent"/"x", "w")`, the matching `os.open` with `O_WRONLY|O_CREAT`, `os.mkdir`, and `os.replace(outside, …)`.

  If a trap is missing, the call raises FileNotFoundError and nothing is created; count that as "not fired".

**2. Spellings the write guards don't read (1989, 2008-2022).** So "any write inside the repository" (1950, 2225, 2733) claims more than is checked.
- **Keyword arguments:** `guarded_paths` reads positional arguments only, so `os.mkdir(path=…)` and `os.replace(src=…, dst=…)` pass unchecked (probe).
- **`dir_fd`:** any dir_fd turns the check off, even for an absolute path, which ignores dir_fd (probe). The comment at 2010 only claims the relative case.
- **Final component:** `_path` resolves os.replace's last component, but replace acts on the link itself. Probe, with REPO swapped for a stand-in: replacing onto, or moving out, a symlink inside the stand-in that points outside both pass.
- **Not trapped at all:** os.rename, os.link, os.symlink, os.truncate, io.FileIO.
- **Not live:** the smoke reaches none of these. My audit hook watches all of these operations and never fired.
- **Fix:** any of:
  - bind arguments with `inspect.signature`, check absolute paths whatever dir_fd is, and resolve only the parent for replace and mkdir;
  - one audit hook, gated by a flag that `traps()` sets;
  - narrow the wording to "no guarded write".

**3. A stopped smoke can leave a selection on disk (909-923, 1006).**
- **Scenario:** the directory fsync raises EIO after summary.json is replaced. Probe: exit 4, `STOP: OUT DIR (A-m2 smoke): OSError EIO writing summary.json -- the smoke stops`, and no tally or rule printed. But summary.json is on disk with `selection.selected = F-a`.
- **Conflict:** v0.3 §3.3 says such a smoke "selects nothing". The STOP line doesn't say the file exists. For session files this is documented (913-914), but the STOP line still doesn't say so.
- **Fix:** in the OSError handler, say whether `path` exists. For summary.json, unlink it (or rename it `.stopped`) before raising.

**4. STOP lines (951-954, 983-992).**
- **Co-occurring errors:** when G-VER or READS coincides with a block part that raised, stderr names only the first. Probe: `STOP: G-VER … ['BREAK: planted']`; the block error is only in the raw.
- **mkdir STOP (954):** still prints only the class name (ENOSPC, EROFS and EIO all print "OSError"). No case makes the mkdir fail: a mutant without its try/except passes. That is the half of round-3 MINOR-1 that stays open.
- **Fix:**
  - append `block_errors` to the G-VER and READS lines, as `lines_error` is at 985;
  - name the errno at 954;
  - add a stub_run case with the out directory's mkdir raising (exit 4, OUT DIR, no session).

**5. `not made_dangling` can never fail (2455, 2463).**
- **Problem:** `smoke_out_problems` creates nothing, so the check holds whatever the code does. Round-3 NOTE 10's hazard was the smoke's own mkdir creating the link's target, and no case runs a dangling link through run_smoke. The `exists_msg` assertion is the real check.
- **Fix:** drop it, or add `--smoke-out <dangling>` to the CLI block and assert exit 2, the exists message, and `nowhere` still absent.

**6. Gap between the out-dir check and the mkdir (1038, then 952; pre-existing).**
- **Problem:** the out directory is checked before the load and created after `_load_qwen` (1061), minutes later, with no re-check.
- **Probe:** I swapped the parent for a symlink inside the adapter factory, which sits where the load sits. Exit 0, and all 13 files landed under the swapped-in target. Pointed into the repository, the smoke would write there. This needs someone to replace the directory during the load.
- **Fix:** re-run `smoke_out_problems(str(out_dir))` just before the mkdir, then refuse unless `out_dir.resolve() == out_dir`.

## Checks 2-4: what holds
- **No STOP prints a tally:** every SystemExit site comes before the prints at 1007-1018. So no STOP path prints SMOKE TALLY, SMOKE RULE or SMOKE STOPS; the self-test's no_rule cases and my dir-fsync probe confirm it.
- **Serialization failures:** NaN and a lone surrogate both give SERIALIZE, with no file and no `.tmp` left.
- **Classifier:** `_lstat_state` and the classification order give identical answers on 3.12.9, 3.13.3 and 3.14.6. On 3.14 the round-3 copy accepted a dangling link and a 300-character name. In a 20-input fuzz, only `~nosuchuser` raised; apart from NOTE 6's window, no input slips through.
- **Guards:** no recursion (they call only stat, lstat and realpath). Relative and bytes paths resolve as the kernel does. No false fire outside the repository. The `lines` guard at 2244 is sound.
- **Spec:**
  - the pin at 541-543 is v0.3's (`83093812…fa67`, identical to the main repository's copy);
  - §3.1's four bullets each match once and parse equal to SMOKE_FORMS, with no extra form;
  - v0.2→v0.3 changes only §3.3's last sentence, §3.4's scope and §4.2's pin sentence;
  - the rule and stops (895-906), counter (a), the printing for counter (b) and the full-read licence all match;
  - no A-m2 v0.2 reference remains; the "v0.2" strings left are LOCK-m-F3 PIN tags.

## Round-3 items
- **MINOR-1:** closed for `_smoke_write` (2669-2705). The three named mutants and "summary.json after the prints" each fail that check. The mkdir half is still open (NOTE 4).
- **NOTE 1:** closed (909-923): TypeError/ValueError caught, errno named, the post-replace case documented. Residuals are NOTEs 3 and 4.
- **NOTE 2:** closed (967-982, 853-870): reads first, both block parts printed, one write with the reads inside, RAW BLOCK STOP after the write.
- **NOTE 3:** closed for the factories (2054-2089; dropping the write check is killed). Not closed for installation (NOTE 1).
- **NOTE 4:** closed (2427-2433, 2464): the directory is now `present`, the expected message is the full ": exists; …", the vacuous equality is gone, and the diagnostic leads with "case_insensitive True, root False".
- **NOTE 5:** closed (733-743, 767-774); verified on three Python versions. It was "not live" because the venv is 3.12.9; there is now no version dependence left to go live.
- **NOTE 6:** closed (2413, 2437-2439): the chmod cases skip under root, and the check name says so. Still not live; "name too long" (2436) keeps a root-independent case for "cannot be examined".
- **NOTE 7:** closed (1946-1956): all eight entry-point call sites run under `traps()`. The leftover wording issues are NOTEs 1 and 2.
- **NOTE 8:** closed as proposed and wider (1981-2035). Gaps are NOTE 2.
- **NOTE 9:** closed (2533-2535).
- **NOTE 10:** closed (753, 761-766). The `made_dangling` check is NOTE 5.
- **NOTE 11:** closed (916); this is what lets the write-path cases patch the write at 2685.
- **NOTE 12:** closed outside the driver: `am2/mut/lane.py:4` now matches `A-m2 v0\.\d+ is committed at HEAD`.

## What I ran
- **Self-test:** `--selftest` in review-wt with `-B`: 194/195 in 71 s. The one FAIL is the expected "A-m2 v0.3 is committed at HEAD".
- **Disclosure:** its two `tree_state` hashes (1218, 2040) read the bytes of everything under data/mf3, including `data/mf3/ckpt/Q-F3_time.json`. I saw only the PASS/FAIL lines.
- **My probes**, all in `<scratch>/r4review/`:
  - `probe.py` loads the worktree's driver bytes, optionally mutated, with `__file__` set to the worktree path. It runs under an audit hook that aborts any open or listing under data/mf3/ckpt, and any write-open, mkdir, rename/replace, remove, rmdir, link, symlink, truncate, chmod or utime inside the worktree or the main repository. The smoke self-test's data/mf3 hash is narrowed there to `data/mf3/schedules`, so nothing under ckpt is read.
  - Baseline: 34/35 in 7 s. I ran 15 mutants: 10 killed, 5 survived (the four trap removals and the mkdir catch).
  - `exps.py` holds the experiments: expanduser (round-3 vs round-4 bytes), dir fsync after summary.json, G-VER plus a block error, a lone surrogate, the check-to-mkdir swap, the guard spellings, the final-component case, the spec parse, and the fuzz.
  - `classify_versions.py` runs an ast copy of the classifier on 3.12.9, 3.13.3 and 3.14.6.
  - The hook never fired.
- **Afterwards:** review-wt has the same git status (the driver modified, the three A-m2 copies untracked) and the same sha256s (driver `b55c4b36…`, v0.1 `cdcc8e86…`, v0.2 `69e23212…`, v0.3 `83093812…`). There is no `__pycache__` there or in r4review.
- No git writes, no model loads, no network. In the main repository I only read and hashed A-m2 v0.3 and ans3.

### Code's disposition

**Code's disposition of round 4.** All 7 items were applied in round 5's bytes. Round 5's "Round-4 items" reports each one.
- MINOR-1 was a regression from round 4's own rewrite: `expanduser` had moved outside the `try`. It is back inside it, with an unknown-`~user` case and a symlink-loop case.


## Round 5

### The report (verbatim)

**Round-5 review of `scripts/mf3_sessions.py`: 0 MAJOR / 0 MINOR / 5 NOTE**

The file reviewed is review-wt's driver, sha256 `0b508640…`, byte-identical to `driver_r5.py`. `r5_delta.diff` is exactly `diff -u driver_r4b.py driver_r5.py`. The author's claim holds: the delta acts on MINOR-1 and on NOTEs 1–6, and every mutant those items named is now killed. What remains are residuals of the same kinds, plus some test gaps. Line numbers refer to the round-5 bytes.

## NOTE 1 — The summary's STOP handling has three edge paths left (mf3_sessions.py:1022-1036, 1058)
- **The rename fails** (probe exp_A): the directory fsync fails with EIO, then the rename fails with EIO. Result: exit 4, and summary.json stays on disk with `selection.selected = F-b`.
  - The STOP line does say so: "summary.json is on disk and its rename failed (OSError EIO): it is not a selection".
  - But run_smoke's docstring (1058) says a STOP "leaves no summary.json", and the comment at 1027 says the summary is "never left as a selection".
- **`exists()` raises** (exp_B): the STOP line then says something false: "whether summary.json is on disk is unknown -- the smoke stops; summary.json is on disk and its rename failed (OSError EIO)". No rename was attempted. `exists()` and the rename share one `try`.
- **The cleanup fails too** (exp_I): os.replace fails with ENOSPC and atomic_write_json's own unlink fails with EIO (`valence_core/m/resume.py:229-234`). `summary.json.tmp` is left holding the full selection (`adopted: F-b`). The STOP line says only "summary.json is not on disk".
- **One branch is untested:** the mutant `if spath.exists():` → `if True:` survives. Under it, the w13 case prints a false "summary.json is on disk and its rename failed (FileNotFoundError ENOENT)", and no check notices.
- **Fix:**
  - give `exists()` its own try;
  - if the rename fails, fall back to unlink;
  - name a `summary.json.tmp` when one is present;
  - assert that the w13 case's STOP line has no rename tail;
  - reword 1058 to "no summary.json unless its rename fails, which the STOP line says".

## NOTE 2 — The out directory is not pinned after its mkdir (959-969, 997, 1024; module docstring 30-31)
- **What is left open:** the re-check closes round 4's gap between the check and the mkdir. The ~50 min of writes after the mkdir still go through the path, and nothing re-checks it.
- **Probe (exp_C):** at the first session write I swapped the parent for a link to another temp directory. Exit 0, the tally printed, all 13 files landed in the swapped-in directory and none in the directory the smoke made. Pointed into the repository, the smoke would write there. As in round 4, this needs someone to replace a path component during the run.
- **Fix:**
  - record `os.stat(out_dir)` after the mkdir;
  - before each `_smoke_write`, refuse unless `out_dir.resolve() == out_dir` and `os.path.samestat` still matches;
  - add a stub case shaped like exp_C, expecting exit 4.
- **Related:** run_smoke_sessions now needs out_dir to be the resolved path. The call at 2718 had to add `.resolve()`. The call at 2706 still passes an unresolved `/var/folders/...` path, and is harmless only because the BACKEND STOP fires first. Say so in the docstring at 935.

## NOTE 3 — The trap controls stop short (2077-2089, 2156-2198, 2300-2343)
- **The four checkpoint-function traps have no control.** Removing `checkpoint_path`, `refuse_ended`, `pending_at` or `run_gate_stage` from traps() survives; each mutant still passes 38/39.
- **Nothing shows that a call site enters traps().** Removing `*traps()` from stub_run (2315) survives. The main stub check's "never reached" (2335-2343) then holds vacuously.
- **Fix:**
  - In the live-control stack, call each of the four with no arguments. A trap raises SystemExit. A real function raises TypeError before its body runs, because each takes a required first parameter (`ckpt_path`, `path`, `path`, `adapter`), so this is safe.
  - In stub_factory's `make()` (2301), which runs inside the stub run's stack, record that builtins.open, os.open, os.mkdir, os.replace, os.rename and stages.checkpoint_path are not the originals. Assert that in the main stub check.

## NOTE 4 — Co-occurring stops: two gaps remain (998-1012)
- **READS plus a block error is untested.** The code names both (exp_D: "READS …: the line reads raised ValueError: planted-reads; the block raised [...]"). But no case covers it: dropping `{also}` from the READS line survives.
- **A task-round hair trigger goes unnamed when an earlier stop fires on the same session.**
  - In exp_E, session 5 (F-a A2s) carries `scaffold_absorption`/free in its record.
  - stderr is only "G-VER … ['BREAK: planted5'] -- the smoke stops". Neither "HAIR" nor "scaffold_absorption" appears on stderr or in the raw.
  - §3.3 names that fire as one of the driver's stops.
- **Fix:** add a READS-plus-block case. Compute `hair` before the first raise and append it to the G-VER, READS and RAW BLOCK lines.

## NOTE 5 — Claims broader than the checks
- **Deletions (1984):** the docstring says "Deletions … (the smoke reaches none of them)". The smoke does reach one: on every failed write, atomic_write_json unlinks `<name>.tmp`.
  - exp_F saw `os.remove` on `…/expF/01_F-0_A1s.json.tmp`, and the w1/w2/w13 cases exercise this path.
  - It is harmless, since the file is inside DIR, but the claim is false.
  - Fix: "only atomic_write_json's unlink of its own temp file in DIR, on a failed write".
- **"An absolute path whatever its dir_fd" (1982, 2149-2151):** only os.replace's dst_dir_fd is checked.
  - Reverting guarded_os_open (2063) to round 4's rule survives.
  - exp_H shows the round-5 code is right: an absolute os.open with dir_fd=3 fires, and so does mkdir with dir_fd=3.
  - Fix: add `fires(fake_os, REPO/…, os.O_WRONLY|os.O_CREAT, dir_fd=3)`, a relative path that passes, and `fake_mk(REPO/…, dir_fd=3)`.
- **The symlink loop (2577):** the check name says the loop is "refused as not resolving". That is true only on 3.12. On 3.13.3 and 3.14.6 it is refused as "cannot be examined (OSError)", which the assertion also accepts.

## What holds (checks 2-5)
- **`_oserr`:** gives "OSError ENOSPC" and "FileExistsError EEXIST", and the class alone when errno is missing or unknown.
- **`_smoke_write`'s on-disk statement:** right both after the replace (the fsync case) and before it (the ENOSPC case).
- **The re-check:**
  - At run_smoke, out_dir is smoke_out_problems' resolved path, and re-resolving it is idempotent. I tested that through a link on 3.12, 3.13 and 3.14. So `again != out_dir` fires only on a real change.
  - A directory that appears is refused as "exists"; a parent swapped for a link, as "now resolves to"; a link into the repository, as inside it.
  - The mutant `if again != out_dir:` alone is equivalent, because `again` is None whenever there are problems.
- **No tally or rule on any STOP:** every SystemExit comes before the prints at 1037-1048. All exit-4 runs, including the experiments, printed no SMOKE TALLY, RULE or STOPS. summary.json is left only in NOTE 1's cases.
- **smoke_out_problems' try:** an unknown ~user gives "does not resolve (RuntimeError)"; a NUL and `~` plus NUL give "(ValueError)", on 3.12.9, 3.13.3 and 3.14.6.
- **Live controls:** safe.
  - Each target's parent is checked absent first, and the check FAILs, without trying anything, if it exists.
  - So a missing trap gets ENOENT: nothing under ckpt is read, and nothing is created or moved. `src_kept` covers the two moves.
  - Every trap-removal mutant except NOTE 3's is killed.
- **Regressions:** none. stub_run's new `p/` parent and the `.json` filter change nothing else. The `.resolve()` at 2718 is required by the re-check.

## Round-4 items
- **MINOR-1:** closed (753-757; cases 2552-2553). Moving expanduser back outside the try, or dropping RuntimeError from the except, each fails a check. Verified on three Python versions.
- **NOTE 1:** closed as specified (2156-2198). All seven guard-removal mutants are killed: builtins+io, builtins, io.open, os.open, os.mkdir, os.replace, os.rename. The residual is NOTE 3.
- **NOTE 2:** closed (2019-2089, wording at 1979-1986). Keywords, an absolute path with a dir_fd, the unfollowed final component and os.rename are all checked; round 4's link-inside-pointing-out cases now fire (exp_H). The residuals are NOTE 5.
- **NOTE 3:** closed for the reported case (915-931, 1022-1036; case 2827-2842). The residuals are NOTE 1.
- **NOTE 4:** closed (969, 998-1005; cases 2843-2844 and 2863-2880). The residuals are NOTE 4.
- **NOTE 5:** closed (2572-2581, 2596-2606). The vacuous check is gone, and the CLI dangling-link case kills the lstat-given mutant. `nowhere` being absent is not asserted, but it cannot be reached: the refusal comes before any mkdir.
- **NOTE 6:** closed as specified (959-965; cases 2845-2862). The window after the mkdir is NOTE 2.

## What I ran
- **Self-test:** `--selftest` in review-wt, with `-B` and `PYTHONDONTWRITEBYTECODE=1`: 198/199 in 67 s. The one FAIL is the expected "A-m2 v0.3 is committed at HEAD". Raw output: `<scratch>/r5review/selftest_r5_review.txt`.
- **Disclosure:** its `tree_state` hashes read the bytes of everything under data/mf3, including `data/mf3/ckpt`. Its live controls stat the absent `data/mf3/ckpt/selftest-absent-dir`. I saw only the PASS/FAIL lines.
- **Probes**, all in `<scratch>/r5review/`:
  - `probe.py` loads the worktree's driver bytes, optionally mutated, with `__file__` set to the worktree path. It runs under an audit hook that blocks any open or listing under data/mf3/ckpt, and any write-open, mkdir, remove, rename, link, symlink, truncate, chmod or utime inside review-wt or the main repository. The smoke's data/mf3 hash is narrowed to data/mf3/schedules.
  - Baseline: 38/39.
  - 33 mutants (`mutants_a.txt`, `mutants_b.txt`): 23 killed, 10 survived. Two survivors are equivalent: `if again != out_dir:` alone, and dropping ValueError from the except, since argv cannot carry a NUL. The other eight are the gaps in NOTEs 1, 3, 4 and 5.
  - `exp_A.txt` to `exp_I.txt` are experiments injected into `_selftest_smoke`, all inside temp directories. `classify_r5.py` runs the refusals on three Python versions.
  - The hook fired only on trap-removal mutants: their live-control calls on `data/mf3/ckpt/selftest-absent-dir/x.json` and `review-wt/selftest-absent-dir/x` were blocked before any syscall. Neither parent exists.
- **Afterwards:** review-wt has the same git status, the same HEAD (`daca8b0`) and the same sha256s: driver `0b508640…`, v0.1 `cdcc8e86…`, v0.2 `69e23212…`, v0.3 `83093812…`. There is no `__pycache__` in review-wt or r5review. smoke-wt was not touched.
- No git writes, no model loads, no network. In the main repository I only hashed A-m2 v0.3; it matches. I ran `git status --ignored` twice in review-wt; it listed no ignored path.

### Code's disposition

**Code's disposition of round 5.** All 5 NOTEs were applied in round 6's bytes. Round 6's "Round 5's items" reports each one.


## Round 6

### The report (verbatim)

**0 MAJOR / 0 MINOR / 5 NOTE**

The delta acts on all five of round 5's NOTEs, and every mutant round 5 named is now killed. The new findings are residuals and test gaps: none affects a normal run, and none is reachable without an adversary or several faults at once. Line numbers refer to the round-6 bytes (review-wt's driver, `4a98f74e…`, byte-identical to `driver_r6.py`). `r6_delta.diff` is exactly `diff -u driver_r5.py driver_r6.py`; only the two header path labels differ.

## NOTE 1 — `_summary_stopped` is not pinned, so after a pin STOP it renames or deletes in the swapped-in directory (mf3_sessions.py:1083-1085, 958-985)
- **What happens:** the pin STOP for summary.json is raised inside `_smoke_write`. The handler at 1084 then calls `_summary_stopped(spath)` on the unpinned path, so its lstat, rename and unlink go through `out_dir`, which by then resolves elsewhere.
- **exp_P:** after session 12's write, I swapped the parent for a link to `p1`, which held `<tag>/summary.json` (a decoy). Exit 4.
  - STOP line: "before writing summary.json: ['it now resolves to …/p1/decoy, not …/p/decoy'] -- the smoke stops; nothing written; summary.json renamed summary.json.stopped; …"
  - The decoy in `p1` was renamed. The smoke's own directory holds its 12 files.
- **exp_Q:** the same, with `summary.json.stopped` in `p1` as a non-empty directory. The rename failed and the decoy was deleted: "could not be renamed (IsADirectoryError EISDIR) and was removed".
- **Why it matters:** this needs a swap plus a summary.json at the target, hence NOTE. But it is the one write the pin does not cover, and it runs exactly when the pin fires. Pointed into the repository, it would rename or delete a file there. The self-test's os.rename trap would catch the rename; nothing catches the unlink, because os.unlink and os.remove are untrapped.
- **Fix:**
  - Call `_summary_stopped` only while `_out_dir_moved(*pin) == []`; otherwise say the directory moved and nothing under it was touched.
  - Sturdier: after the mkdir, open DIR once with `O_DIRECTORY`, pin it by `os.fstat`, and give the lstat, rename and unlink `dir_fd=`.
  - Trap os.unlink and os.remove inside the repository, and add an exp_P-shaped case.

## NOTE 2 — Hair naming: two of the three lines are untested, and a failed session write names nothing (1054-1068; case 2959-2988)
- **Surviving mutants (41/42 each):**
  - dropping `{hair_also}` from the RAW BLOCK line (1067);
  - moving `hair_also` out of `also` onto the G-VER line only, so READS loses it.
- **exp_T:** the code is right today. Both "READS … planted-reads5; a task-round scaffold_absorption fired too (phase free)" and "RAW BLOCK … planted-block5 …; a task-round scaffold_absorption fired too (phase free)" name the fire.
- **The claim is broader than the code.** The comment at 1056 and the check headline at 2982 say "every stop a session carries is named on the first stop's line". That fails when the session's own write is the first stop.
  - exp_X: session 5 carries a G-VER problem and a task-round fire, and its write fails with ENOSPC.
  - The STOP line is only "OUT DIR (A-m2 smoke): OSError ENOSPC writing 05_F-a_A2s.json; 05_F-a_A2s.json is not on disk -- the smoke stops".
  - The raw printed before the write does carry both.
- **Fix:**
  - Add exp_T's two runs to the case.
  - Compute `hair`/`also` (with the G-VER problems) before `_smoke_write`, and append them to any SystemExit it raises. Alternatively, narrow the comment and headline to the G-VER, READS and RAW BLOCK lines.

## NOTE 3 — `_out_dir_moved`'s except branch is untested (921-928, 1022-1026)
- **Surviving mutants:** catching only `RuntimeError` (dropping OSError), and `return []` in the except. Under the first, a DIR removed or made unexaminable mid-run gives a traceback (exit 1) instead of exit 4.
- **exp_R:** today's code is right. DIR removed during session 1 gives "before writing 01_F-0_A1s.json: ['it cannot be examined (FileNotFoundError)']", exit 4.
- **Also:** moving `pin = (out_dir, os.stat(out_dir))` out of the try survives.
- **exp_S:** if that stat fails (EIO), the STOP says "OSError EIO making the output directory -- no session runs", but the directory was made and is left behind, empty.
- **Fix:** add an exp_R-shaped case expecting exit 4 and "cannot be examined". Split the try so a failed stat says the directory was made and then could not be examined.

## NOTE 4 — The traps-in-place record covers only the 21 stub runs (2365-2374, 2418, 3122; docstring 2028-2029)
- **Five trap sites lose `*traps()` silently:** the CLI refusals (2662), qwen_case (2713), the backend pair (2780) and both precheck blocks (3092, 3100). Removing it at any of them survives.
  - Those checks' "no checkpoint function … reached" and "opens nothing under data/mf3/ckpt" would then pass vacuously.
  - All five do install the traps today.
- **A loose bound:** the check is `len(trapped_at_load) >= 20`; exp_U shows 21 records.
- **An unasserted safety assumption:** the empty-call live controls are safe only while the four functions keep a required first parameter (stages.py:115 and :921, m/resume.py:713 and :819). Today all four raise TypeError, but nothing asserts it.
- **Fix:**
  - Have `traps()` end with a context manager that records the identity test on entry, and assert the count equals the number of sites.
  - Assert `== 21`.
  - Assert that `inspect.signature(real).bind()` raises TypeError for each of `real_ckpt_fns` before calling them.

## NOTE 5 — Docstrings and wording
- **2033-2035:** "the smoke's one deletion is m's unlink of its own temp file in DIR" is false again. `_summary_stopped:980` unlinks summary.json or summary.json.tmp when its rename fails.
- **33:** "no summary.json" disagrees with run_smoke's docstring at 1107-1108 ("unless both its rename and its removal fail"). exp_W(b) leaves summary.json with `adopted: F-b`, and its STOP line says it is not a selection. Neither docstring names the case where the lstat fails.
- **31:** "checked … before every write" does not cover `_summary_stopped`'s rename and unlink (NOTE 1).
- **1103-1108:** the STOP list omits the new pin STOP. Line 1108 was not re-wrapped (153 columns, now the file's longest).
- **943-944:** "nothing written" also appears after the twelve session files were written. "{path.name} not written" would be exact.

## Regressions
None found.
- The pin returns [] on every write of a normal run: all 21 stub runs and the backend COMPLETE run pass.
- `_smoke_write` has only these two callers.
- `live()`'s new TypeError catch can only turn a crash into a FAIL.
- `post` runs before the temporary directory's cleanup.
- The new helpers behave the same on 3.12.9, 3.13.3 and 3.14.6. Only the symlink-loop exception class differs (RuntimeError, then OSError), and both are caught.
- None of the new cases can leave anything outside a temporary directory: the dir_fd controls use fake openers, and the four functions refuse the empty call.

## Round 5's items
- **NOTE 1:** closed (958-985, 1085; cases 2899 and 3050-3087). Every mutant of `_summary_stopped` I ran is killed except NotADirectoryError, which is near-equivalent; the w13 check now asserts no tail. Residual: wording, my NOTE 5.
- **NOTE 2:** closed (916-944, 1024, 1054, 1083; cases 2990-3048). The pin-off, pin-ignored, no-resolve and no-samestat mutants are killed, and the docstring is at 990. Residuals: my NOTEs 1 and 3.
- **NOTE 3:** closed as specified (2223-2263, 2365-2374). Removing any of the four checkpoint traps, or stub_run's `*traps()`, is killed. Residual: the other five sites, my NOTE 4.
- **NOTE 4:** closed in code (1055-1068) and for the two named cases. Residual: my NOTE 2.
- **NOTE 5:** the dir_fd controls are closed (2189-2190, 2196-2197, 2211; three mutants killed), and the symlink-loop wording is closed (2653-2654). The deletion sentence was reworded but is false again (my NOTE 5).

## What I ran
- **Self-test:** `--selftest` in review-wt, with `-B` and `PYTHONDONTWRITEBYTECODE=1`: 201/202 in 71 s. The only FAIL is the expected "A-m2 v0.3 is committed at HEAD".
  - Disclosure: it hashes the bytes under data/mf3, ckpt included, and stats the absent `data/mf3/ckpt/selftest-absent-dir`. I saw only the PASS/FAIL lines.
- **Probe harness:** round 5's, adapted. It loads the review-wt driver bytes, optionally mutated, under an audit hook that blocks any open or listing under data/mf3/ckpt and any write, mkdir, remove, rename, link or rmtree inside review-wt or the main repository. The data/mf3 hash is narrowed to `schedules`. Baseline: 41/42.
- **Mutants:** 53 in all; 41 killed and 12 survived. The 12 are the six code mutants above (counting the near-equivalent one), the five trap-site removals, and loosening the `>= 20` bound.
  - All 26 of round 5's mutants that still apply are killed, including the seven that survived round 5.
- **Experiments:** P, Q, R, S, T, U, W and X, each injected into the smoke self-test and run inside temporary directories.
- **Hook hits:** only in trap-removal mutants. Their live-control calls on the two absent-parent targets were blocked before any syscall. The baseline and every experiment had none.
- **Disclosure, my own commands:** early on, three `find` traversals of review-wt (a file count, a newer-than filter and a `__pycache__` search) descended into data/mf3/ckpt unpruned. None printed a name from there. Every later traversal pruned ckpt.
- **Afterwards:**
  - review-wt has the same git status (also with `--ignored`) and the same HEAD, `daca8b0`.
  - The sha256s match: driver `4a98f74e…`, v0.1 `cdcc8e86…`, v0.2 `69e23212…`, v0.3 `83093812…`. So do the full file manifest and directory list, with ckpt pruned.
  - There is no `__pycache__` anywhere, and no leftover temporary directory.
  - smoke-wt was not touched. In the main repository I only hashed A-m2 v0.3; it matches.
  - No git writes, no model loads, no network.

All files are in <scratch>/r6review/:
- probe6.py
- probe6b.py
- mutants_all.txt
- mutants_extra.txt
- exp_P.txt to exp_X.txt
- exps.txt
- classify_r6.py
- selftest_r6_review.txt
- baseline_tree.sha
- after_tree.sha

### Code's disposition

**Code's disposition of round 6.** This was the last round. Each NOTE is applied where the change is small, and otherwise disclosed here. There is one behaviour change in production code, NOTE 1's guard. Beside it are a STOP message's wording (NOTE 5), docstrings and a comment; everything else is the self-test.
- **NOTE 1, applied.**
  - After a failed summary write, `_summary_stopped` runs only while the output directory is still the one the smoke made. Otherwise the STOP line says the directory moved and that nothing under it was renamed or removed.
  - `os.unlink` and `os.remove` are now trapped inside the repository, with live controls.
  - The late-swap case puts a decoy `summary.json` in the swapped-in directory and asserts it is left untouched.
  - **Disclosed:** a swap inside the instant between that check and the rename or removal stays possible. It needs a hand on the path at that moment, and the sturdier `O_DIRECTORY`/`dir_fd` form is not built.
- **NOTE 2, applied.**
  - The two untested lines now have cases: a line read that raises, and a block part that raises, each in the session whose task round fired.
  - The comment and the check's headline are narrowed to the G-VER, READS and RAW BLOCK lines.
  - **Disclosed:** a failed write of the session names only itself on its STOP line. The raw printed before the write carries the rest, with two gaps that need a second fault: a line-read error is kept in the session's JSON only, and a block part that raises drops its own lines. If the write then fails, those are lost.
- **NOTE 3, applied.** There is a case for the output directory removed during the first session: exit 4, "cannot be examined (FileNotFoundError)".
  - **Disclosed, not changed:** if the `os.stat` right after the mkdir fails, the STOP line says "making the output directory", though the directory was made and is left empty. Round 6's reviewer reached this with one injected EIO.
- **NOTE 4, applied.**
  - Every `traps()` call site records its entry, asserted exactly: 35 entries.
  - The stub runs' record is asserted exactly: 24.
  - Before their empty calls, `inspect.signature(...).bind()` is asserted to refuse each of the four checkpoint functions.
- **NOTE 5, applied.**
  - The module docstring's STOP clause.
  - The self-test docstring's deletion sentence. The smoke's deletions are m's unlink of its temp file in DIR on a failed write, and `_summary_stopped`'s removal of a summary file in DIR when its rename fails.
  - run_smoke's STOP list now includes the pin, and its overlong line is re-wrapped.
  - "nothing written" becomes "`<file> not written`".
- **The reviewer's disclosure: a departure from O2-3, for the seat.** Three `find` traversals of the review worktree descended into `data/mf3/ckpt` unpruned.
  - One was a newer-than filter, a `find -newer` form by Code's reading of the report. O2-3 names that form among the barred ones ("no size or time metadata of this raw, data/m/ckpt or data/m/reports (ls -l/-t/-s, stat, du, wc -c, find -newer, …)"). Q-F3's carried form allows no size or time metadata of `data/mf3/ckpt` before VERDICTS.
  - None printed a name from there or read a file's contents. The same round's self-test hashed those bytes, as every round's does.
  - The worktree was a fresh checkout at `daca8b0`, so its files carry the checkout's times, not the run's.
  - The precedent: the 2026-10-19 VERDICTS read, item 5, ruled the same kind of departure "accepted, inert". That ruling also noted that the metadata window had closed at the VERDICTS line; Q-F3's is still open. The seat rules.
