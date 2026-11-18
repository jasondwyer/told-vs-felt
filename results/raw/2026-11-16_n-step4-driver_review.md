# n — the BACKEND extension's driver: the blind review, and Code's dispositions

*The n-build session (Code), PI date 2026-11-16. This is the blind review of `scripts/n_sessions.py backend-ext`. It
is §5 step 4 of the seat's order: the BACKEND extension on the box, then ADDENDUM-n1 §2's label-convention comparison
in the same session, here in one invocation.*

- *The command is wired in the driver, so the package (`60d892dc…cc66`) is unchanged.*
- *One blind reviewer, a Code subagent, read the first draft (`80d30846…b03d`) against the governing text:*
  - *n v0.2 §2.1 and §3's G-ACQ;*
  - *ADDENDUM-n1 §1.3 and §2;*
  - *the seat's answers of 2026-11-16, §2.4 and §5;*
  - *G-ACQ's dated notes GA-4 and GA-5;*
  - *the box's characterization raw (`7ab4d2f`);*
  - *the code it calls.*
- *Its brief held it to these rules:*
  - *run no Python, and nothing that executes the code;*
  - *write nothing, and use no network;*
  - *no guard marker in any command line;*
  - *nothing under `data/mf3`;*
  - *no token id, no file size or time, and no clock time;*
  - *the list of record v2's items 1–5, quoted verbatim.*
- *Code's readings R1–R6 were given to the reviewer to check, not to adjudicate.*
- *It returned 13 findings (6 RISK, 7 NIT; no BUG) and 15 mutants, of which 12 survived by its reading. Each survivor
  came with the test that would kill it.*

*Code applied every finding and wrote a test for each survivor. The draft as frozen (`64cf6ee1…16cb`) passed the
driver's self-test (every n module's self-test and the driver's own checks) at 267/267 on the laptop, under the jlens
venv at `nice -n 19`, from a scratch overlay, in battery windows the coordinating session granted. The runs are in the
last section.*

*The report is reproduced as the reviewer returned it. Its line numbers are those of the first draft; "P" is Code's
scratch folder.*

## The review, as returned

Blind review of `backend-ext` in P/step4/scripts/n_sessions.py. Below, `:N` means a line of that file. I ran nothing and wrote nothing. I found no hard BUG: the call signatures, the plan, the identity, the records and the report all fit the runner and schema at backend-ext, and the R1–R6 readings are implemented as stated. The findings are risks: late or silent failures and gaps in the self-test.

**(1) Findings**

1. **RISK (high) — the loaded folder is never tied to the weights the identity records.** `:402–404`, `:454`, `:255–260`/`:470`.
   - `--model-dir` only has to be an existing folder. `weights_sha256` is copied from the manifest's `olmo2_instruct` entry, and nothing checks that the folder holds those weights.
   - Scenario: `--model-dir /workspace/models/instruct` (an OLMo-3 folder on the same volume).
     - G-VER only decodes, so it may still pass.
     - The bridge passes: apart from `n_layers` the provenance carries nothing model-specific, and `path` and `seed` are dropped from the hash.
     - The 64 × 5120 shape check passes.
     - 24 reads are then written under `weights_sha256 = 36f05404…0fdb`.
   - m's driver loads only from the manifest entry's `path`, checks the file list and each file's byte count, and prints a WEIGHTS line before the load (`scripts/m_sessions.py:733–761, 792–796`).
   - Fix, before G-VER:
     - require `Path(model_dir).resolve()` to equal the entry's `path`, or drop the flag and use that path;
     - check the file listing, byte counts and the `config.json`/tokenizer sha256s against the entry;
     - print m's WEIGHTS line.

2. **RISK — R6 shows the box is of the characterized class, not that it is the characterized box.** `:456–460`, `:503–512`.
   - m's own disclosure says `backend_identifier` "cannot tell two boxes of one class apart (m:267) -- hence the pod id" (`valence_core/m/resume.py:141–147`).
   - The driver names pod m43y3deb1gq3rp in a comment (`:503`) but never compares `$RUNPOD_POD_ID` with it.
   - Scenario: Runpod replaces the pod with the same image and GPU class. The bridge still gives 641ee466f4553b6a, and the stage runs where respawn step (ii) never ran. That contradicts CLAUDE.md's "Both PASS before anything runs" and the docstring's "the box is the characterized one" (`:34–35`).
   - Fix: bind the identifier to its pod (a `--characterized-pod` argument, or a literal beside `CHARACTERIZED_IDENTIFIER`) and refuse in `bext_refusals` unless the pod matches.

3. **RISK — R3's bound is measured on the margin, but the comparison is per label.** `:490`, `:371`; `schema.py:397, 529–536` (`absdiff = |margin − fresh_margin|`).
   - A cached-vs-fresh shift that is the same for both labels cancels in the margin. The bound can then be about 0 while each per-label fresh value is off.
   - BK's `logprob_S/U` sit beside its cached `margin`; BK records its fresh path only as `fresh_margin`.
   - So the tolerance does not cover the per-label cached-vs-fresh term it exists for. The right convention can miss 40/40 and go to the seat: a spurious escalation, never a wrong lock.
   - The docstring (`:293`) and the print (`:485`) call this quantity "|cached − fresh|".
   - Fix, for the seat since R3 is a reading:
     - also compute the largest per-label gap, |logprob_z − fresh_logprob_z| over reads and labels; the records hold both values;
     - print it beside `absdiff` and declare which bound the tolerance adds;
     - reword the docstring and print to "|margin − fresh_margin|".

4. **RISK — checks that need no model run only after the 64 GB load.** Some run after all 24 reads. `:431` vs `:456–460`, `:478`, `:492–496`; `runner.py:309–312, 360–362, 373–375, 393–401`.
   - (a) Records or a report on disk without `--resume`.
   - (b) A `--ruling` with no standing pause. Example: re-running after a ruled COMPLETE with the same `--ruling p01=…` gives "rulings name no standing pause".
   - (c) A resume on another pod or package. `pod_id` and `package_sha256` are known before the load.
   - (d) `CUBLAS_WORKSPACE_CONFIG` set but not `:4096:8`, or a changed library or Python version. The adapter only checks that the variable is set (`olmo_hf.py:70–74`), so the bridge refuses after the load; every provenance field except `n_layers` comes from the environment.
   - (e) numpy's stream known answer, which R1's draw rests on.
   - (f) Model-free work that runs after the reads: `bk_d0_floor`, the four candidates' `ids.label_ids` (a dropped candidate is a SystemExit), and `label_counts`' window and `ids_sha` checks.
   - Fix: one pre-load block covering (a)–(f):
     - for (c), read any prior report (`cells.read_json` + `check_report`) and compare `pod_id`, `package_sha256` and `rendering_id`;
     - for (d), compare `CUBLAS_WORKSPACE_CONFIG`, Python and `importlib.metadata` versions with `CHARACTERIZED_PROVENANCE`;
     - for (e), call `stream_known_answer()`;
     - for (f), build the floor table and the candidate getters, and run their checks.

5. **RISK — a run of record accepts `--root`/`--report` anywhere under `data/n/` or outside the repository.** `:420–421`; `guard.py:74–81`.
   - (i) `--report data/n/ids/MANIFEST.json` or `--root data/n/bk` pass `refuse_out`, and `atomic_write_json` overwrites them at the run's end.
   - (ii) A smoke's root and report, resumed with `--resume` but without `--smoke`, are adopted into the run of record. `plan[:k]` is a prefix of the plan, and the identity carries no smoke mark.
   - (iii) Forgetting `--smoke` with an outside root writes a full run outside `data/n`.
   - Fix:
     - without `--smoke`, require exactly `BEXT_ROOT`/`BEXT_REPORT`, or paths under `data/n/ckpt/` and `data/n/reports/`, as `render_out` does for render-ids;
     - with `--smoke`, keep the outside-repo rule and leave a marker in the smoke root that a non-smoke run refuses.

6. **RISK — the command's own flow is never tested.** `:428–500` vs `:515–683`.
   - The self-test stops at `bext_refusals` and never calls `cmd_backend_ext`. Untested:
     - the order: refusals, G-VER, load, bridge, shape, identity, plan, run, distribution, comparison;
     - a G-VER STOP returning before the load;
     - which identifier the bridge compares;
     - the smoke truncation of plan and floor;
     - which statistic is used as the bound, and how the candidates are wired.
   - Every single-site change there survives (M13 below).
   - Fix: give the command injectable seams (decoder/G-VER, adapter factory, backend). Drive it over `testing.CausalDouble` behind a stub adapter whose provenance is the characterization's with window 4,096, writing only in the temp root. Assert:
     - a G-VER STOP returns 1 and the factory is never called;
     - a wrong identifier refuses before any read;
     - `--smoke 2` gives 2 records and "/2" counts;
     - the bound passed in is `absdiff.max`;
     - the command refuses a missing folder before any tokenizer loads.

7. **NIT** — the comparison line prints the bound (`:497`). The seat's §2.4 says "its match count of 40 and nothing else — no value". The bound is already in the discordance line; point to it there.

8. **NIT** — under `--smoke`, `convention_line` prints "…the convention of record for LOCK-n v0.1" on k-of-k counts (`:392`, `:499`). Prefix SMOKE or skip the line.

9. **NIT** — a G-VER STOP prints and returns 1 but writes no stage report (`:447–449`).
   - The schema defines a G-VER-STOP end state whose "report holds no record and no pause" (`schema.py:171–177, 1457–1461`).
   - The runner refuses to resume after a STOP (`runner.py:311–312`).
   - Either write that report or declare as a reading that at backend-ext the raw is the STOP's record.

10. **NIT** — `half_unit`'s refusals print BK's recorded text (`:319`, `:321`), a log-probability on stdout. Print the session and zone instead.

11. **NIT** — `weights_sha256` reads the working-tree manifest (`:259`). m's PIN requires the committed copy (`valence_core/m/resume.py:97–105`). Compare it with `git rev-parse HEAD:data/olmo/manifest.json` before the load.

12. **NIT** — the self-test restores the environment with `os.environ.clear()` plus `update(env)` (`:681–683`). That touches far more than the two keys it sets, and the restore is never asserted. Restore the two keys and assert the environment afterwards.

13. **NIT** — `--ruling` is silently ignored by the other commands, and a repeated PAUSE_ID silently keeps the last value (`:704–712`). Refuse both.

**(2) Mutants** (each a single-site change; line numbers in the reviewed file)

- **M1** `:218` `BEXT_KEY` "n-bext" → "n-bext2" — **SURVIVES.** Both R1 checks recompute the draw with `BEXT_KEY` itself (`:539–540`). Test: a pinned known answer, e.g. the sha256 of the 24 `session_id`s joined by "\n".
- **M2** `:245` drop `sorted(...)` — killed by "driver: backend-ext's 24 sessions are distinct, in the set's order, and drawn alike twice (R1)".
- **M3** `:276` `"cadence": 160` → `16` (or `"p0_n": 2400` → `240`) — **SURVIVES**; at 16 the binomial would be evaluated mid-stage. Test: `ident["fidelity_rule"] == {tau: TAU, p0_count: 0, p0_n: 2400, cadence: 160, sample_key: "n-fid|{s}", sample_rule: BEXT_SAMPLE_RULE}`.
- **M4** `:259` `[ids.MANIFEST_ENTRY]` → `["instruct"]` — **SURVIVES**; the check only tests for 64 hex characters. Test: equality with the full G-ACQ aggregate `36f05404…0fdb`.
- **M5** `:289` `choice_window_declared=DEFAULT_CHOICE_WINDOW` → `schema.MAX_WINDOW` — killed by "driver: R6: n's provenance (window 4,096) hashes to another identifier and bridges to the characterization's".
- **M6** `:307` `np.quantile(a, 0.9)` → `0.95` — killed by "driver: the discordance distribution, a known answer (numpy's linear quantile)" (0.0455 ≠ 0.041).
- **M7** `:330` drop `parse_float=str` — **SURVIVES.** `json.dumps` writes the shortest repr, so `str(float)` gives back the same text; harmless on a Python-written file but it breaks "as recorded". Test: hand-written synth text `-1.250` → half unit 0.0005.
- **M8** `:342` drop `or r["direction_kind"] != "none"` — **SURVIVES**: every synth row and every real d = 0 read is "none". Test: synth with `direction_kind="valenced"` → refused. Each cue clause alone also survives, because `swapped` trips both; add a mismatch on one cue only.
- **M9** `:364` loop → `((s.cue_S, "S"),)` — **SURVIVES**: candidate B differs only on S. Test: a candidate equal to A except on `cue_U` → count 0.
- **M10** `:371` `half + bound` → `bound` — **SURVIVES**: every test table uses a half unit of 5e-16. Test: half 0.005, bound 0, offset 0.004 → match; 0.006 → no match.
- **M11** `:361–362` drop the `ids_sha` refusal — **SURVIVES.** Test: an `ids_of` that changes one id → refused.
- **M12** `:385` `rows[i]` → `rows[0]` — **SURVIVES**: `vanilla_score` never runs in the self-test. Test: on `CausalDouble`, `vanilla_score(...)(ids, LS)` equals `primitive.read(...)["fidelity"]["fresh_logprob_S"]` for the same d = 0 read exactly (the pattern is at `runner.py:712–718`).
- **M13** `:458` `bridge != backend_of_record` → `bid != …` — **SURVIVES** (finding 6); it would only fail on the box, after the load.
- **M14** `:415` `root is None or report is None` → `and` — **SURVIVES**: only the both-None case is tested. Test: `--smoke` with an outside `--root` and no `--report` → refused. Likewise `:417` `(root, report)` → `(root,)` survives; test an outside root with `report = BEXT_REPORT`.
- **M15** `:681–683` restore → `pass` — **SURVIVES**: `RUNPOD_POD_ID="pod-selftest"` leaks into hftiny's run. Test: `cmd_selftest` asserts the environment equals its snapshot afterwards.

**(3) Observations**

- **Order.** Every refusal in `bext_refusals` comes before transformers is imported. G-VER (ids pinned to `MANIFEST_OF_RECORD`, tokenizer loaded with `local_files_only`, gver-trial's decoder) comes before the adapter, and a STOP returns before any weights load.
- **Plan against runner and schema.** The identity's 23 keys equal `STAGE_IDENTITY_FIELDS`; lock, dose map and identity bound are null exactly at backend-ext; the "dose-rule" reason is what `check_record` requires; the identity-check block is null; the cell name is valid; a resume keeps cap and alpha.
- **Blinding.** No margin or log-probability reaches stdout or the report. Only the cell records hold them, as designed.
- **R6 literal.** `CHARACTERIZED_PROVENANCE` matches the raw's printed block field for field (all 15 keys, the library versions included). `path` and `seed` are dropped from the hash, so the bridge varies only the window.
- **`bk_d0_floor` against reduced.json.** I checked structure only (key and category counts, no values): every d = 0 read is a "none" read, one per session; floor cells occur only in the neutral arm; runs are numbered globally. So (cell, run) is a unique key and gives 40 for `olmo_32b`.
- **Expected outcome, for the seat.** If the cached and fresh paths agree bitwise at d = 0, R3 gives a bound of 0.0. The tolerance then shrinks to BK's half unit, about 5e-16 for 16-significant-digit values, which is below one ulp near 10. That requires this box's uncached forward to reproduce BK's cached-path doubles from other hardware exactly. Given BK's own cached-vs-fresh spread (n §2.1 [C]), "to the seat with four low counts" is the likely result. This is the ruling's effect, not a driver defect.
- **R2.** The bound is measured under bare labels. If another candidate wins (the +eot ones are a token longer), LOCK-n's identity bound comes from reads under a convention the campaign won't use.
- **Ruled non-finite read.** If one is ruled, the comparison is refused on every later invocation (`:487–489`); only a code change can run §2.4's check then.
- **Two identifiers.** n's own (window 4,096) and 641ee466f4553b6a will both stand in the record, and later n stages will need the same bridge.
- **Committing the outputs.** `.gitignore:255–271` admits only `data/n/bk` and `data/n/ids`. The stage's report and cell JSONs need an admit block before the pod stops (rule 27); the `.npy` arrays stay out.
- **Free in-band check.** For the floor sessions among the 24, `vanilla_score` under "bare" should equal the records' fresh values bitwise. Printing "k of k agree" would verify the claim at `:379–380` on the box without printing a value.

## Code's dispositions

By the review's numbers. All changes are in `scripts/n_sessions.py`; `valence_core/n/` is untouched.

- **1, RISK (the loaded folder not tied to the weights the identity records).** Applied.
  - The stage loads only from the committed model manifest's instruct path. `--model-dir` is gone.
  - `weights_of_record` requires the working copy of the manifest to be HEAD's committed bytes (`git show HEAD:`).
  - It reads the instruct entry (`manifest_entry`) and checks the folder (`check_weights_folder`): exactly the entry's
    files, each at its byte count. That is m's form; the full re-hash is respawn step (i).
  - A WEIGHTS line is printed before anything loads.
  - Tests:
    - the entry gives G-ACQ's aggregate (`36f05404…0fdb`), 22 files, its revision and its path;
    - malformed entries are refused;
    - the folder check refuses a missing file, an extra file, another byte count, and a path that is not a folder.
- **2, RISK (the bridge shows the class of box, not the box).** Applied.
  - `CHARACTERIZED_POD` (m43y3deb1gq3rp) sits beside the characterized provenance and identifier, all literals from
    the BACKEND entry `7ab4d2f`.
  - The stage refuses any other pod, or none. A new box is a new characterization and a change to these literals.
  - Tests: another pod; no pod.
- **3, RISK (R3's bound measured on the margin; the comparison is per label).** Applied as a revised reading, R3,
  flagged in the entry.
  - The comparison's bound is each label's largest |logprob − fresh_logprob| over the 24 reads.
  - The margin's distribution (|margin − fresh_margin|) is printed beside it, for the lock.
  - The docstring and the print use those words.
  - Test: the flow test's double shifts both labels' fresh values alike, about 0.29 nats per label and about 1e-4 on
    the margin. The cached-path table then matches under the per-label bound, and a margin bound would not.
- **4, RISK (model-free checks after the 64 GB load).** Applied: every check that needs no model now precedes the
  load.
  - (a)–(c): `prior_state` refuses three cases:
    - records or a report without `--resume`;
    - a report under another stage identity, or one that ended in a STOP;
    - a ruling that names no standing pause, or a standing pause without one.

    The identity, its backend identifier included, is built before the load from the environment's provenance.
  - (d): the cuBLAS setting must equal the characterized one.
    - `environment_provenance` builds, before the load, the provenance the adapter will report: GPU, CUDA,
      capability, libraries and Python. It must bridge to the characterization's identifier.
    - After the load, the adapter's own provenance must hash to the same identifier.
  - (e): numpy's stream known answer.
  - (f): before the load:
    - BK's d = 0 table;
    - every candidate's label getter;
    - every floor session's ids, against BK's ids_sha, and each forward's window.
  - Tests: the flow test's pre-load refusals; in each, the adapter is never made.
- **5, RISK (a run of record accepting any root and report).** Applied.
  - A run of record writes only to `data/n/ckpt/backend-ext` and `data/n/reports/backend-ext.json`. `--root` and
    `--report` are refused without `--smoke`.
  - A smoke must name both, outside the repository.
  - Tests: `--root` without `--smoke`; a smoke with no report; a smoke whose report lies in the repository; smokes of
    0 and 25 reads.
- **6, RISK (the command's own flow untested).** Applied.
  - The command is now `run_backend_ext(env, …)`, over `BextEnv`'s seams. `production_env` wires the box.
  - The flow test runs it over `testing.CausalDouble` behind a stub adapter whose provenance is the
    characterization's at window 4,096. It writes only in the self-test's temporary folder. It checks:
    - COMPLETE, with 24 records and one load;
    - the comparison's and the convention's lines;
    - R3's bound, and the in-band count;
    - the order: WEIGHTS, then G-VER, then the load;
    - a second run without `--resume` is refused before the load;
    - a ruling that names no pause is refused before the load;
    - a resume after COMPLETE launches nothing;
    - another pod is refused;
    - a smoke of 2 writes 2 records and its counts are out of 2;
    - a G-VER STOP returns 1, with no load and nothing on disk;
    - an environment that does not bridge is refused before the load;
    - a loaded provenance that differs from the checked one is refused, with nothing read;
    - eight more refusals, and the cuBLAS setting.
- **7, NIT (the bound on the comparison's line).** Applied: that line prints the four counts only. The bound appears
  in the distribution's line, as fidelity values.
- **8, NIT (a smoke's convention line).** Applied: it opens "SMOKE, never of record: ".
- **9, NIT (no report at a G-VER STOP).** Declared as Code's reading in the docstring: at backend-ext the raw is the
  STOP's record. Flagged in the entry.
- **10, NIT (a refusal quoting BK's text).** Applied. `half_unit` raises a ValueError that quotes nothing, and
  `bk_d0_floor` names the session and zone only.
- **11, NIT (the working-tree manifest).** Applied in `weights_of_record`: the working copy must equal
  `git show HEAD:`'s bytes.
- **12, NIT (the environment's restore).** Applied. The two keys are restored one by one, and the driver's self-test
  asserts the environment unchanged after backend-ext's checks.
- **13, NIT (`--ruling` elsewhere, a repeated pause id).** Applied.
  - The stage's options are refused for every other command.
  - A pause id given twice is refused.
  - backend-ext refuses the folder options.

**The mutants** (the review's list, by its numbers):
- **Killed by existing checks:** M2, M5 and M6, as the review read.
- **New tests for the survivors:**
  - M1: R1's draw pinned, `BEXT_SESSIONS_SHA256` `10f3a127…6b64` (the sha256 of the 24 sessions' ids, computed in a
    battery window);
  - M3: the fidelity rule asserted whole;
  - M4: the instruct entry's aggregate asserted;
  - M7: a hand-written "-1.250" gives a half unit of 0.0005;
  - M8: a d = 0 read that is not a "none" read, and one cue not the session's, are each refused;
  - M9: a candidate whose U label alone differs counts 0;
  - M10: the half unit counts with no bound (0.004 inside 0.005, 0.006 outside);
  - M11: ids that are not BK's are refused;
  - M12: the vanilla score equals `primitive.read`'s fresh log-probability exactly on the double, and within 1e-6 on
    the HF path of a tiny OLMo-2 config (at the box);
  - M13: the flow test's bridge refusals, before and after the load;
  - M14: a smoke with no report, and a smoke whose report lies in the repository;
  - M15: the environment asserted unchanged.

**The observations.**
- **The expected outcome.** If cached and fresh agree bitwise at d = 0, the per-label bound is 0.0 too. The tolerance
  is then BK's half unit alone, and "to the seat with the four counts" is the likely result. The entry states this
  beside R3. It is the ruling's effect (the coordinating session's observation 6 at ADDENDUM-n1's referent check),
  not the driver's.
- **R2** (the bound measured under "bare" labels) is flagged in the entry.
- **A ruled non-finite read** would leave the comparison refused on every later invocation. Flagged: running §2.4's
  check then would need a change.
- **The two identifiers** (n's own, and the characterization's under the default window) both stand in the record.
  Later n stages need the same bridge.
- **Committing the outputs.** The admit block for `data/n/reports/` and the stage's cell JSONs comes with the outputs'
  commit, in its own window. The `.npy` arrays stay out.
- **The in-band check.** Applied (`in_band`): for the floor reads among the 24, the count whose fresh values equal
  the comparison's vanilla score exactly, counts only.

## The self-test runs

All runs were from Code's scratch overlay (HEAD's `valence_core` with the draft driver on top), in battery windows
the coordinating session granted. Each used the jlens venv's interpreter at `nice -n 19`, with
`PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` in scratch. The interpreter was reached by `cd` into its folder and run as
`./python`, so no guard marker appeared in any argv.
1. **The first draft** (`80d30846…b03d`): 249/249. `hashes` gave package `60d892dc…cc66`, with the same 11 closure
   lines as the BUILD.
2. **After the dispositions:**
   - `pin_r1.py` printed `BEXT_SESSIONS_SHA256` `10f3a127…6b64`, which Code pinned.
   - The self-test on the pinned draft (`eac646b7…6a7a`) gave 266/267, exit 1. The one FAIL was "driver: the
     command's flow over the double: COMPLETE, 24 records, one load, the comparison's line". Its detail showed:
     - the comparison's line, "bare 24/24; space 3/24; bare+eot 0/24; space+eot 0/24";
     - the convention line, "exactly one candidate at 24 of 24: bare".
   - **The expectation, before.** The check required the exact line "label convention (ADDENDUM-n1 §2): bare 24/24;
     space 0/24; bare+eot 0/24; space+eot 0/24". The smoke check required "… bare 2/2; space 0/2; bare+eot 0/2;
     space+eot 0/2".
   - **The expectation, now.** It requires a line beginning "label convention (ADDENDUM-n1 §2): bare 24/24; space ",
     and in the smoke check one beginning "… bare 2/2; space ". The convention line's check is unchanged:
     - the last line begins "exactly one candidate at 24 of 24: bare";
     - in the smoke, "SMOKE, never of record: exactly one candidate at 2 of 2: bare".
   - **Why a test fix, not a code fix.**
     - The code computed what ADDENDUM-n1 §2 specifies.
     - The old expectation assumed that no other candidate could fall within the tolerance.
     - In the toy, the tolerance is the per-label bound from a double whose fresh path carries a deliberately large
       bias: about 0.29 nats per label, so that R3's margin-versus-label distinction can be tested.
     - With a tolerance that wide, the "space" labels' values lay within it of the bare cached values for 3 of the
       24 toy sessions. That is the comparison working as written on a toy with a wide bound.
     - What the check exists to show is still asserted: the right candidate at n of n, and exactly one candidate
       there. Only the other candidates' exact counts are no longer pinned.
     - On the box, the bound is the measured per-label discordance.
   - **The change, exactly:** the two hunks below, and nothing else. Code confirmed this by tool: reversing them on
     the final bytes reproduces the run-2 bytes, sha256 `eac646b7…6a7a`.

     ```diff
     @@ -984,3 +984,3 @@ def _bext_selftest(chk, tmp: Path) -> None:
                  rc1 == 0 and len(recs1) == BEXT_N and made.count("run") == 1
     -            and "label convention (ADDENDUM-n1 §2): bare 24/24; space 0/24; bare+eot 0/24; space+eot 0/24" in lines1
     +            and any(x.startswith("label convention (ADDENDUM-n1 §2): bare 24/24; space ") for x in lines1)
                  and lines1[-1].startswith("exactly one candidate at 24 of 24: bare"), lines1[-3:])
     @@ -1020,4 +1020,4 @@ def _bext_selftest(chk, tmp: Path) -> None:
              chk("driver: a smoke of 2: 2 records in its own root, the comparison over 2 floor sessions, marked SMOKE",
     -            rc2 == 0 and n2 == 2 and "label convention (ADDENDUM-n1 §2): bare 2/2; space 0/2; bare+eot 0/2; "
     -                                     "space+eot 0/2" in lines2
     +            rc2 == 0 and n2 == 2 and any(x.startswith("label convention (ADDENDUM-n1 §2): bare 2/2; space ")
     +                                         for x in lines2)
                  and lines2[-1].startswith("SMOKE, never of record: exactly one candidate at 2 of 2: bare"), lines2[-2:])
     ```
   - The self-test on the final draft (`64cf6ee1…16cb`) gave **267/267**. `hashes` gave package `60d892dc…cc66`, with
     the same 11 closure lines.
3. **At the box,** the self-test adds hftiny's 12 checks in place of its one skip line, and the HF-path vanilla
   score in place of its skip line. 278 are expected. The box's runs are their own raws.
