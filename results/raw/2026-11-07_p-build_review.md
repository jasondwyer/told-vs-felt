# p package — BUILD: the blind code review, rounds 1–3 (Code's raw, 2026-11-07)

*Three blind review agents, each read-only on the repository, each given the spec, the seat's rulings and the code (rounds 2 and 3 also the previous round's report); their probes ran in the session's scratch directory. Code's dispositions come first; the reports follow verbatim. Local paths scrubbed: the repository's prefix as <repo>, temp and scratch roots as <tmp>.*

## 0. Code's dispositions (each item re-checked at source before it was applied or disclosed)

### Round 1 (1 MAJOR, 11 MINOR, 11 NOTE)

| item | severity | disposition |
|---|---|---|
| M1 | MAJOR | Fixed. The driver's gcal cases run with the pod id removed, the canonical roots patched to a scratch root and the loader trapped; the simulated-box case also replaces G-CAL-p's `run` with a recorder (and, from round 2, its precheck with a stand-in) and puts a stand-in OLMo adapter module in `sys.modules`. gcal's own non-stub case runs with the pod id removed and the roots patched. Round 2 confirmed it by probe in a simulated post-commit box state. |
| m1 | MINOR | Fixed. Canonical paths are not resolved; links on the way, at a temp name or (from round 2) a non-file there are refused before any load; checkpoints are written through `guard.atomic_write_nofollow`, artifacts and schedule files through `guard.write_once_bytes` (O_NOFOLLOW). |
| m2 | MINOR | Fixed. `refuse_out` adds `data/olmo`; `refuse_test_out` refuses everything under `data/` for a test or stub output; case-insensitive from round 2. |
| m3 | MINOR | Fixed in part, disclosed. The AST check covers the round-1 forms and more (sixteen planted forms) and scans the driver; its docstring names the forms it does not follow (round 2's N-g). |
| m4 | MINOR | Fixed. Each built entry's replacement is enforced; from round 2 by object identity (N-h). |
| m5 | MINOR | Fixed. `olmo_hf_sha256` and `driver_sha256` are in G-CAL-p's identity. |
| m6 | MINOR | Fixed. Seams are refused on a canonical run. |
| m7 | MINOR | Fixed. The proxy's pass-through is asserted by object identity, attribute delegation on a double that has them, a multi-character-token double (`ChunkScriptedAdapter`), m's startup pieces through the proxy, and the generate calls checked against m's (AST and dynamic). |
| m8 | MINOR | Fixed. The G-SHAPE-F0 comparison reads HEAD's blob and the enumeration is checked against m's directly; the "p edits no m file" check is removed (a commit-time fact, verified on the commit's file list); the schedules check is unconditional. |
| m9 | MINOR | Fixed. Checkpoint validation and the pod-change check run before the load; the docstrings state the order. |
| m10 | MINOR | Declared, for the seat: PIN P21 and FLAG F-p7. The segment comes from m's `SEGMENT_FORM`; the call is pinned by an AST comparison (also run in the precheck from round 2) and a dynamic check of all 128 calls. |
| m11 | MINOR | Fixed for G-SHAPE-p (m's package hash checked against m's committed blobs); for G-CAL-p in round 2 (N-i). |
| NOTE 1 | NOTE | Flagged, F-p8 (the proposal pin in G-CAL-p's identity). |
| NOTE 2 | NOTE | Fixed: §3.2's conditions (1)–(3) in G-CAL-p's artifact (computed before the load from round 2). |
| NOTE 3 | NOTE | Fixed: every STOP in the loop is recorded in the checkpoint. |
| NOTE 4 | NOTE | Fixed: the driver maps refusals to 2 and other STOPs to 4 (completed in round 2, N-c). |
| NOTE 5 | NOTE | Declared: P4 and F-p2 (the schedules' `key_template` field, outside the register's form). |
| NOTE 6 | NOTE | Fixed: `olmo_hf.py:286`, `schedule.py:512`. |
| NOTE 7 | NOTE | Flagged, F-p9 (ahead of step 6); the podchange admit line added. |
| NOTE 8 | NOTE | Fixed: entry (3)'s kinds are the Clock and the data roots; entry (4)'s reason restated. |
| NOTE 9 | NOTE | Fixed: `cap_hits_returned_in_cuts`; a STOPped generation's text is in the checkpoint's stop field (no artifact is written on a STOP). |
| NOTE 10 | NOTE | Fixed: OSError handling in the weights check; `run_gcal` has no seam. |
| NOTE 11 | NOTE | Fixed: G-SHAPE-p's artifact points at the runners' dynamic evidence. |

### Round 2 (0 MAJOR, 3 MINOR, 11 NOTE)

| item | severity | disposition |
|---|---|---|
| R2-1 | MINOR | Fixed: §3.2's conditions (register entry (1)'s site) computed in G-CAL-p's precheck, before any load (P1). |
| R2-2 | MINOR | Fixed: a STOP before the generation counts nothing as launched; a self-test case checks both kinds. |
| R2-3 | MINOR | Fixed: the simulated-box case replaces G-CAL-p's precheck with a stand-in, so no state of the record matters. |
| N-a | NOTE | Fixed: the root comparison is case-insensitive. |
| N-b | NOTE | Fixed: the schedule writer checks every path and temp name before writing any file. |
| N-c | NOTE | Fixed: schedule refusals exit 2 (`ScheduleRefusal`), other STOPs 4; G-CAL-p's precheck lets a register STOP through as a STOP. |
| N-d | NOTE | Fixed: the ProxyStop excerpt is 200 characters, and the stop field keeps 600 of its message. |
| N-e | NOTE | Flagged, F-p10 (the cut log keeps the returned text for the seat's read). |
| N-f | NOTE | Fixed: the AST pin survives an eval failure as a problem, and runs in G-CAL-p's precheck. |
| N-g | NOTE | Disclosed: the guard's docstring names the forms the static check does not follow. |
| N-h | NOTE | Fixed: the register resolves the declared replacement and compares by identity; a stand-in wearing its name is refused (self-test). |
| N-i | NOTE | Fixed: G-CAL-p's committed check covers every `valence_core/m/*.py`. |
| N-j | NOTE | Fixed: the five docstrings; a non-file at a temp name refused in `gcal.paths`. |
| N-k | NOTE | Fixed: the POD CHANGED message carries m's instruction; `.gitignore` admits the checkpoints' pod-change set-asides. |

### Round 3 (0 MAJOR, 1 MINOR, 7 NOTE)

| item | severity | disposition |
|---|---|---|
| R3-1 | MINOR | Fixed for the driver's half: its simulated-box and weights-files cases use literal weights stand-ins, so no record file is read there. The other half is by design and disclosed (the design raw §7, the entry): gcal's stub runs and gshape's `--out` run read their inputs of record (the OLMo manifest and scaffold files, G-CAL-OLMo's gate artifact, the seat's answers raw, the renders raw, PROPOSAL-m) from their committed blobs, so an uncommitted edit to one fails the self-test (values-check pass 3 measured it). |
| R3-2 | NOTE | Fixed: the call pin catches an unavailable source or an unparsable form and reports it as a problem (G-CAL-p's precheck refuses, exit 2); a self-test case plants an unavailable source. |
| R3-3 | NOTE | Fixed: a ProxyStop carries the returned text whole, and the checkpoint's stop field keeps it. |
| R3-4 | NOTE | Fixed: renders that do not reproduce are a STOP in G-CAL-p as in G-SHAPE-p (exit 4); an OS error on an `--out` path is a refusal (exit 2) in `--build-schedules` and `gshape`. |
| R3-5 | NOTE | Fixed in part, disclosed: the register binds each declared replacement at its first use in the process and keeps it; a rebinding before that first use is outside its reach, and the renders pin catches any change of entry (1)'s rule downstream. |
| R3-6 | NOTE | Fixed: on a `--resume`, every identity field the adapter does not give is compared before the load (a self-test case), the backend identifier and the ban ids after it. |
| R3-7 | NOTE | Fixed: a test or stub output is refused anywhere inside the repository. |
| R3-8 | NOTE | Fixed: the driver's and the guard's docstrings, and the entry's wording on the register. |

## 1. Round 1 (the agent's report, verbatim)

# Blind code review, round 1: `valence_core/p/` and `scripts/p_sessions.py` (the uncommitted p BUILD)

Reviewer: a blind agent, read-only. Tree: HEAD `993eba1`, with the parallel m track mid G-SHAPE-F0 re-run (`data/m/gates/G-SHAPE-F0.json` staged as renamed, a new copy untracked). Spec: PROPOSAL-p v0.2 (`42f2977b…3b32`) §1–§4 and §8, and ans2 (`ab40f470…b08b`) Q0–Q4. No repository file was edited. Every probe ran under `<tmp>/…/scratchpad/podwatch/probes/` with `python -B`. `git status` was identical before and after the self-test run.

**Self-test as run here:** `88/89`. The suite has 89 checks while `data/p/schedules/` exists and 88 when it is absent (see m8). The one FAIL is `gshape-p: each unit's placement keys equal G-SHAPE-F0's committed artifact's`. It reads `data/m/gates/G-SHAPE-F0.json: working-tree bytes are not HEAD's blob` and is caused by the parallel session's supersession, not by p (see m8).

---

## MAJOR

### M1. On the box after the BUILD commit, the self-test launches the canonical G-CAL-p-sft run

- **Where:** `scripts/p_sessions.py:227-233`, with a related case at `valence_core/p/gcal.py:517-528`.
- **Problem:** The driver self-test runs the real `main(["gcal", "--unit", "OLMo-sft"])` path, with the real `_load_olmo`. Its expected refusal depends on two things: `RUNPOD_POD_ID` being absent, and p being uncommitted. On the box after the BUILD commit, neither holds.
- **Failure scenario:** The box is in the state just before G-CAL-p. `RUNPOD_POD_ID` is set (RunPod sets it, and env.sh exports it). The BUILD is committed and pulled. CLAUDE.md is clean. The weights are present. No `data/p/ckpt/G-CAL_olmo-sft.json` exists yet. Someone runs `python scripts/p_sessions.py --selftest` as a pre-flight. Then:
  1. `gcal.precheck` passes, and so does `weights_files_problems`.
  2. The DRIVER and WEIGHTS lines print.
  3. `gcal.run(lambda: _load_olmo(w["path"]), …, stub=False)` loads OLMo-sft and runs all 128 generations.
  4. It writes `data/p/ckpt/G-CAL_olmo-sft.json` and `data/p/gates/G-CAL_completability_olmo-sft.json` of record.

  This is p §3's one-shot gate (§0.5: "condition (4) at the frame-word dose, per checkpoint, once"), run without the PI's go (§8 step 5: "on the PI's go for the box"). The gate line, PROVENANCE, per-generation lines and verdict go into the self-test's `contextlib.redirect_stdout` buffer, so the raw of record (rule 27) is lost. Only `_short(o, 120)` survives, in the FAIL note. Any later attempt is refused: CHECKPOINT EXISTS, or the artifact exists.
- **Verified by probe** (`probes/probe_box_selftest.py`). In this process only, it set `RUNPOD_POD_ID`, stubbed `gcal.committed_problems` and the driver's committed-blob read (the post-commit state), stubbed `weights_files_problems` (weights present), and replaced `_load_olmo` with a sentinel. Result: `DRIVER SELFTEST CASE: MODEL LOAD REACHED for /workspace/models/sft`. Every other precheck item (proposal, renders, reference, weights of record, pod id, gate line) passed for real.
- **Related case:** in the same state, gcal's own self-test case `("OLMo-sft", {"stub": False})` (`gcal.py:518`) gets past precheck and calls the factory. Then `px.provenance()` raises `AttributeError`. Nothing is written, but the check is site-dependent and FAILs on the box.
- **m's form is site-independent.** m's G-CAL self-test removes the pod id (`mock.patch.dict(os.environ, env_no_pod, clear=True)`), and its N12 fix (`993eba1`) points the canonical paths at an empty temporary root.
- **Suggested fix:**
  - Run both cases with `RUNPOD_POD_ID` removed and the canonical paths pointed at a temporary root.
  - Never let a self-test reach the real `_load_olmo`. For example, give `run_gcal` a factory seam and pass one that raises.
  - Better: refuse `--selftest` when a pod id is present and assert the refusal.

---

## MINOR

### m1. The canonical checkpoint path is resolved before the symlink test; temp names are opened through links

- **Where:** `valence_core/p/gcal.py:116`, `:167`, `:250-253`; `valence_core/p/schedule.py:92-97`.
- **Problem:** `paths()` returns `(CKPT_DIR / ckn).resolve()`. So `ck_on_disk = pa["ckpt"].exists() or pa["ckpt"].is_symlink()` tests the link's target, never the link itself.
  - A dangling symlink at `data/p/ckpt/G-CAL_olmo-{ckpt}.json` reads as "no checkpoint on disk".
  - The run then writes its checkpoint through the link, to any location, including `data/m/…`.
  - `guard.refuse_out` is applied only to stub out dirs, never to canonical paths.
  - The artifact has `out_link`. The checkpoint has no equivalent.
- **Verified by probe** (`probes/probe_ckpt_symlink.py`, scratch roots): `precheck's ck_on_disk: False (the link itself is_symlink: True)`, then `written through the link … True`.
- **Same class:** `schedule.write_schedule_files` opens `<name>.tmp` with `open(tmp, "wb")`, which follows links. A planted `.tmp` link sends the schedule bytes through the link, and `os.replace` leaves the final schedule path as a symlink. Verified in scratch: `victim written through the .tmp link: True | final path is a link: True`. m's G-SHAPE writer uses `O_NOFOLLOW` for exactly this case.
- **Context:** m's G-CAL `_paths` has the same resolve pattern (inherited). The schedule writer is p's own.

### m2. Test-directory outputs can land in data/olmo and in p's own directories of record

- **Where:** `valence_core/p/guard.py:37`; `valence_core/p/gshape.py:385-391`; `valence_core/p/gcal.py:120-126`.
- **Problem:** `REFUSED_ROOTS` is (data/m, data/mf3, /workspace/models).
  - It omits `data/olmo`, which both `m_resume.CANONICAL_ROOTS` and mf3's `refuse_canonical_out` refuse.
  - It does not refuse p's own root. mf3 refuses its whole `data/mf3` for synthetic runs. p refuses only "at or around" `data/p/gates` (gshape) or `data/p/{gates,ckpt}` (gcal stubs).
- **Failure scenario:** `p_sessions.py gshape --out data/p/schedules`, `--out data/p/verdicts` or `--out data/olmo` is accepted. It writes a never-of-record `G-SHAPE-p.json` into a git-admitted directory of record: `.gitignore` admits `/data/p/*/*.json` and `/data/olmo/*.json`. In `data/p/schedules` it also makes `verify_schedule_dir` report `unlisted G-SHAPE-p.json`.
- **Verified** (decision logic only, no write): data/p/schedules, ckpt and verdicts, and data/olmo are each `p.refuse_out: allowed; gshape --out: ALLOWED`. `m.refuse_canonical_out` refuses data/olmo.

### m3. Term (e)'s static check is easy to evade and does not scan the drivers

- **Where:** `valence_core/p/guard.py:74-75`, `:101-132`.
- **Problem:** `_m_aliases` collects only `from …m import x` names. Assignments are flagged only when the target is `Name.attr`. `setattr` is flagged only as a bare name.
- **Verified by probe** (`probes/probe_static_guard.py`). Ten of eleven plausible forms EVADE:
  - `import valence_core.m.corr as corr; corr._eligible_m = f`
  - `from .. import m; m.corr._eligible_m = f`
  - a tuple target (`corr._eligible_m, y = f, 1`)
  - `vars(corr)[...] =` and `corr.__dict__[...] =`
  - `mock.patch.object(corr, …)`
  - `builtins.setattr` and `object.__setattr__`
  - a local alias (`c = corr; c._eligible_m = f`)
  - `del corr._eligible_m`
  - a module-level `try: from ..m import testing`
  - `importlib.import_module("valence_core.m.testing")`

  Only the baseline form is caught.
- **Scope gap:** `production_files()` covers `valence_core/p/*.py` only. `scripts/p_sessions.py` is never scanned, and neither will `scripts/p_analyze.py` be. That is where register entry (3)'s sites will live (p §4.2: "in scripts/m_analyze.py, through p_analyze").

### m4. The register checks which entry is used, never what is substituted

- **Where:** `valence_core/p/register.py:83-105`.
- **Problem:** `substituted` checks the entry number, the module `__name__` and the attribute names. Under term (a), every entry names its replacement (entry (1): `valence_core.p.corrupt.eligible_p`; entry (2): p's four key functions), but the value is never compared with it.
- **Failure scenario:** A future edit runs `register.substituted(1, corr, {"_eligible_m": other_rule})`. It passes the register and both static and runtime checks. The register's own self-test does exactly this with `lambda t: [1]`.
- **Suggested fix:** store the replacement object (or its qualified name) in `Entry` and assert `values[a] is` that object.

### m5. The checkpoint identity does not bind olmo_hf.py, a licence file

- **Where:** `valence_core/p/gcal.py:75`, `:193-200`, `:290-292`.
- **Problem:** The identity binds p's package and m's package hashes, but not `olmo_hf.py`'s sha256. Yet p §4.2 makes olmo_hf.py's sha a licence line. The backend identifier is built from `adapter.provenance()`, which carries no code hash. `licence_at_run()` is computed when the artifact is built, not at generation time.
- **Failure scenario:**
  1. G-CAL-p-sft is interrupted at record 70.
  2. `olmo_hf.py` is changed and committed. ans2 Q2 notes n's build runs in parallel.
  3. `--resume` passes `committed_problems()` (committed and unedited) and `load_or_init` (identity unchanged).
  4. Records 70–127 come from a different adapter.
  5. The artifact's `licence_at_run.olmo_hf_sha256` names only the second version.
- **Suggested fix:** add `olmo_hf_sha256` (and the driver's sha256) to `P_IDENTITY`.

### m6. The self-test seams of `run()` are accepted on a canonical run

- **Where:** `valence_core/p/gcal.py:322-336`.
- **Problem:** `startup=` and `wrap=` are accepted with `stub=False`. Nothing refuses a seamed canonical run. Contrast `gshape.write`, which refuses seams on the canonical path, and m's gcal ("production code has no seam").
- **Failure scenario:** Any future caller (a driver or a re-wiring) passes `wrap=lambda a: a` or a `startup` seam on the box.
  - With `wrap`, §2.2's proxy is skipped.
  - With `startup`, m's whole `_startup_olmo` is skipped: insulation, base and cross-checkpoint refusal, the 8192 window, b3's ban list, the weights path, TEMP and cap, and the tokenizer probe.

  Either way the artifact is still written at `data/p/gates/…` as of record.

### m7. Self-tests that cannot fail, or do not test what they name

- **(a) `proxy.py:100-101`:** "a result with no line break is stored exactly as returned (text, ids, stop, cap)" checks only `text == "77"` and `stop_reason == "newline"`.
  - The scripted adapter's defaults are `stop_reason="newline"` and `cap_hit=False`. These are the very values a proxy that always applied `dataclasses.replace(…, stop_reason="newline", cap_hit=False)` would produce.
  - So a pass-through regression passes. Ids, cap and object identity (`out is g`) are not asserted.
  - §2.2's clean-pool identity "by construction" rests on this property. G-CAL-OLMo's clean pools include cap hits.
  - `cut_result` does return the same object today (checked).
- **(b) `proxy.py:113-115`:** the `path` delegation compares `None == None`, because `CharScriptedAdapter` has no `path` attribute (checked). It cannot fail.
- **(c) `gcal.py:425`:** `stub_startup` replaces all of `_startup_olmo`. So m's real startup never runs through the proxy anywhere: `assert_olmo_adapter`'s `path`/`choice_window` reads, `build_ban_list`'s `special_token_strings`/`encode`, and `tokenizer_appends`. m's own self-test replaces only the module-level `olmo_startup`.
- **(d) No check that G-CAL-p's generate calls equal m's `run_completability` calls** (prefix, segment, seed, temp 0.7, max_tokens 60, ban_ids, cached False, injections ()). m's scripted adapter records `calls`, so this is cheap to add (see m10).
- **(e) §2.1's actual case is untested.** In OLMo, `---\n\n` is a single token, carrying content and the break. The char tokenizer of `testing.CharScriptedAdapter` splits it into characters.
  - **My probe on OLMo's real tokenizer shows the cut is right** (`probes/probe_proxy_bpe.py`, the Olmo-3 base tokenizer cached locally, offline). The returned text `"---\n\nTask: Write the opposite of 'enter"` is stored as `'---'`, n_tok 1, stop newline, cap False; the stored ids decode to `'---\n\n'`.
  - `'Cold.\rTask: x'` is stored as `'Cold.'`. `'-\n- item'` is stored as `'-'`.
  - 1,977 OLMo tokens carry content and then a break; none carries content after the break.
  - In every case the text cut and the token-id boundary agree.

  A test double with multi-character tokens would pin this.

### m8. Self-test results depend on the state of the record and of the parallel track (N12's class)

- **(a) `gshape.py:448-450`** FAILs whenever `data/m/gates/G-SHAPE-F0.json` is not HEAD's blob. Observed live during the m track's G-SHAPE-F0 supersession: 88/89.
- **(b) `p_sessions.py:258-262`** ("p edits no m file …") FAILs whenever the m track has any uncommitted edit to an m file, `m_analyze.py` or `m_sessions.py`, whoever made it. It measures the tree, not p.
- **(c) `p_sessions.py:207-210`** is skipped when `data/p/schedules` is absent. That changes the check count (88 vs 89) instead of failing. After the BUILD commits the schedules, their absence should FAIL. m's PIN is that "the check count is the same on every site".

The seat's N12 ruling asks that cases "hold in every state of the record".

### m9. The driver docstring claims every model-free refusal precedes the load; several come after it

- **Where:** `scripts/p_sessions.py:17-21`, `:33`; `valence_core/p/gcal.py:327-353`.
- **The claims:** "Every refusal that needs no model runs before the load" and "it loads after every refusal".
- **What actually happens after the 64 GB load (176–212 s cold):** these refusals in `run()`/`load_or_init` need no adapter, yet run only after the load:
  - a `--resume` of a checkpoint whose `stop` is set (p's new refusal)
  - a malformed checkpoint or record list
  - malformed cuts
  - POD CHANGED (`seen` comes from the checkpoint, `now` from the environment)
- **Context:** m's G-CAL has the same placement. Nothing is written before these refusals, so the cost is a wasted load and a statement that misdescribes the behaviour.

### m10. The G-CAL-p loop restates m's prompt and generation call instead of importing them

- **Where:** `valence_core/p/gcal.py:364-391`.
- **What p §3.1 says:** "The prompt, seeds, grader and generation call are m's `gcal`'s by import or by §4.2's register."
- **What the code does:** `seg = f"Task: {task}\nResponse:"` (`:367`), the `px.generate(…)` call (`:374-375`) and the record literal (`:377-379`) restate m's `run_completability` (`valence_core/m/gcal.py:1155`, `:1164-1165`, `:1168-1170`). Register entry (4) is "declared; not exercised". So the generation call is neither imported nor registered.
- **Today the restated call matches m's** (read line by line: SESSION_BANNER, the segment, `injections=()`, the key's seed, `_ro.OLMO_TEMP`, `_ro.STOP_CAP`, the startup ban ids, `cached=False`). But nothing pins that.
- **Suggested fix:** use `m_gcal.SEGMENT_FORM.format(task=task)` for the segment, and add the call-equality self-test of m7(d). Or have the seat rule that p's own loop with a restated call satisfies §3.1.

### m11. G-SHAPE-p's run of record can record m's package hash from an uncommitted tree

- **Where:** `valence_core/p/gshape.py:275`, `:137-141`.
- **Problem:** The artifact records `m_package_sha256 = m_resume.package_sha256()`, which hashes all 18 `valence_core/m/*.py` files (cached per process). The canonical committed check covers only the sources map's 17 m files: `M_HASHED` excludes `testing.py` (checked: `m/testing.py in p sources map: False`). Nothing asserts that the recorded hash is the hash of m's committed blobs.
- **Failure scenario:** the m track has an uncommitted edit to `valence_core/m/testing.py`. A canonical G-SHAPE-p then passes and records an m package hash that no commit has. G-SHAPE-F0 refuses this exact case ("an uncommitted package is never recorded"; `committed_package` and `provenance_drift`'s fresh re-hash).

---

## NOTE

1. **gcal identity, `proposal_sha256` is p's** (`gcal.py:194`, the PIN at `:26-31`).
   - p §4.2 (3) reads: "the proposal pin kept m's, with `proposal_p_sha256` recorded beside it in every p output".
   - ans2 Q1 (iii) reads: "The proposal pin stays m's; `proposal_p_sha256` is recorded beside it in every p output".
   - p §3.2 lists `proposal_p_sha256` as an *added* reported field.
   - In the G-CAL-p identity both fields hold p's sha. This is defensible, since G-CAL-p's gate line runs under p, but the seat should confirm that the "every p output" reading does not extend to the G-CAL-p identity.
2. **Conditions (1)–(3) of §3.2 appear in no artifact.** §3.2 says "(1)… and (2)… structural, from §1.2, reported; (3) the seat's read of record". No G-CAL-p or G-SHAPE-p artifact records them (per-item n_eligible, k, changed positions, or the seat-read reference). m recorded them in its model-free artifact, which p does not build. The G-CAL-p entry must carry them.
3. **Only the hair trigger is recorded as a STOP in the checkpoint.** The others are not: the rule 28(d)(a) boundary (`gcal.py:369-372`), `ProxyStop`, and `assert_insulated`. So "a stopped checkpoint is never resumed" protects only the trigger, and a `--resume` after an un-adjudicated boundary STOP continues the same checkpoint (as in m).
4. **Some STOPs exit 1, a code the driver does not declare.** `RegisterStop`/`KeysStop` raised inside `gcal.precheck` (renders → `corrupt_p` → `substituted`) are outside every `try` in `run_gcal` (`p_sessions.py:149-153` catches `GcalPRefusal` only). `corrupt.renders_problems` catches `CorrStop`/`ValueError` only. Such a STOP exits with code 1, while the driver declares 0, 2 and 4.
5. **The schedule builder's output is post-processed** (`schedule.py:8-14`, `:53-60`; flagged by its PIN). The six campaign `key_template` fields are overwritten after m's builder runs. This is not a register substitution. If a future p stage ran m's own `verify_schedule_dir` under entry (2), it would mismatch on those six files.
6. **Citations that are off by a line or two.**
   - `proxy.py:12` and `:21` cite "olmo_hf.py:284" for the stripped decode. Line 284 is blank; `text=self.decode(gen).strip()` is at `:286` (the return at `:285`).
   - `schedule.py:9` and `:59` cite "valence_core/m/schedule.py:511" for the literal. The `"key_template": f"m-sched|…"` line is `:512`; the dict opens at `:511`.
7. **Looking ahead to the stage wiring.**
   - `register.py:17-19`'s PIN says "every site runs before any model load". Entry (2)'s stated reason includes "the arm streams and the item streams", which m's scaffold draws per session after the load.
   - `active_count() == 1` may then STOP on any library thread alive after an HF load.
   - The roots m's stages use (data/m/ckpt, reports, schedules) are not among entries (1)–(4); entry (3) covers m_analyze only.
   - p's `.gitignore` admits no `*.json.podchange-*` set-asides (m's does).
8. **Register `kind` labels.** Entry (4)'s kind is "eligibility", for a renders source. Entry (3) has a single kind, "clock", covering the Clock, the roots and the verdicts-dir resolution. These are labels only, harmless while (3) and (4) are unbuilt.
9. **Counters.**
   - `cap_hits` counts the stored `cap_hit`. §2.2 sets it to False on a cut, and the returned value survives only in the cut event (`cap_hit_returned`).
   - A trigger-STOPped generation's text is not tabulated by the counters (rule 23: "over ALL sessions including excluded").
10. **The weights check is a copy of m's** (`p_sessions.py:108-138`). `weights_files_problems` copies `m_sessions.olmo_weights_problems` (declared PIN) and has already drifted:
    - no `OSError` handling on `stat`;
    - the checked root is not returned and used for the load;
    - the `models_root` seam decouples the checked path from the loaded `w["path"]`.
11. **No dynamic-evidence pointer.** p's G-SHAPE artifact omits m's `runner_dynamic_evidence` pointer, the dynamic half of Layer S ("the m self-test at this package_sha256").

---

## Categories with no finding, and checks that came back clean

- **Category 1, G-CAL-p's procedure against m's `run_completability` for OLMo.** These match, read line by line:
  - precheck order (paths, proposal, checkpoint, artifact, renders/reference, weights, pod id, gate line);
  - startup (m's `_startup_olmo`);
  - grader honesty;
  - `key_set` (128 keys, f0's order, `m-cal` seeds);
  - identity (m's `_identity_olmo` plus p's six fields);
  - skip-only resume and the pod-change refusal;
  - `assert_insulated` and the 28(d)(a) boundary before every generation;
  - generation arguments and f0's grade;
  - m's `completability_artifact` and `_write_artifact`.

  The only differences are the declared ones: the proxy, the hair trigger, p's block, no model-free artifact, and no R1 A6 tallies.
- **The proxy's cut is correct on OLMo's real BPE tokenizer** (m7(e)), and the trigger cannot fire behind it.
- **No crc32 seed collision between p's and m's streams.** I checked actual seeds, not key strings, over s 0..2699 and b 0..99, with Q-F0, `corr|i` and `m-cal` included: 25,632 p keys against 34,401 m keys, 0 shared seeds (`probes/probe_seed_collisions.py`).
- **Category 2, the register.** No p production code assigns or setattrs an m attribute outside `register.substituted` (grep). No m module is copied. No bar, DV, verdict or outcome-order function is substituted. Restoration holds in a `finally` and under exceptions. Entries (3) and (4) STOP. Findings: m4, m10, and notes 5 and 8.
- **No file under `valence_core/m`, `valence_core/mf3`, `scripts/m_sessions.py`, `scripts/m_analyze.py`, `scripts/mf3_sessions.py` or `valence_core/adapters/olmo_hf.py` is modified** (`git status` and `git diff` empty).
- **`corrupt_p`** reproduces §1.2's sixteen renders under both sha conventions; equals m's renders on items 0 and 12 only; k = 3 everywhere; no roster skip.
- **The schedules:** with m's keys, p's builder reproduces m's eighteen OLMo files byte for byte, and `data/p/schedules` equals the regeneration.
- **`.gitignore` and `.gitattributes`:** `git check-ignore` confirms that `data/p/{schedules,gates,reports,ckpt,verdicts}/*.json` are admitted, `*.tmp` and `.md` are ignored, and `/data/p/ckpt/** -diff` is present.

## Summary

1 MAJOR, 11 MINOR, 11 NOTE.

- **The MAJOR (M1)** is a write hazard in the self-test. On the box after the BUILD commit (pod id set, code committed, weights present), `p_sessions.py --selftest` reaches the real model load and runs the canonical, one-shot G-CAL-p-sft. It writes its checkpoint and artifact of record with no go from the PI, and its stdout is swallowed. Probe-verified.
- **The MINORs** are:
  - write-path hazards: link following (m1), refused roots narrower than m's and mf3's (m2);
  - guard gaps: the static check (m3), the unchecked replacement value (m4), the checkpoint identity missing olmo_hf.py (m5), the seams accepted on canonical runs (m6), an m package hash that can come from an uncommitted tree (m11);
  - self-test gaps and fragility: m7, m8;
  - refusals after the load that the docstring says come before it (m9);
  - the G-CAL-p generation call restated rather than imported or registered (m10).
- **The core computations are correct.** The renders, keys, schedules, the proxy's cut on OLMo's real tokenizer, and G-CAL-p's generation and grading path all match the spec and m.

## 2. Round 2 (the agent's report, verbatim)

# Blind code review, round 2: `valence_core/p/` and `scripts/p_sessions.py` (the uncommitted p BUILD)

Reviewer: a blind agent, read-only. Tree: HEAD `9838664`, with p uncommitted (`valence_core/p/`, `scripts/p_sessions.py` and `data/p/` untracked; `.gitignore` and `.gitattributes` modified). Spec: PROPOSAL-p v0.2 §1–§4 and §8, and ans2 Q0–Q4. Round 1's report: `p_build_review_r1.md`.

How this review was run:
- No repository file was edited.
- Every probe ran with `python -B` from the repo root. The probes are in `<tmp>/scratchpad/podwatch/probes2/`. They wrote only to scratch temporary directories, and they rebound module attributes only inside their own processes.
- `git status --short` was byte-identical before and after all runs.

**Self-test as run here: 101/101**, in about 8 s. It is also 101/101 in a simulated post-BUILD box state (probe `probe_state_dependence.py box`).

---

## Part 1. Round-1 findings and their round-2 status

| R1 | Round-1 finding (short) | Round-2 status | Verified by |
|---|---|---|---|
| **M1** | The box self-test reaches the real loader and the canonical G-CAL-p-sft run | **FIXED** | Code: `p_sessions.py:245-293`, `gcal.py:714-731`. Probe `probe_m1_box_selftest.py` (below) |
| m1 | Canonical path resolved before the link test; temp names opened through links | **FIXED** | Code: `gcal.py:120-144`, `guard.py:130-198`, `schedule.py:83-104`. Probe `probe_canon_links.py` |
| m2 | Test outputs could land in data/olmo and in p's own directories of record | **FIXED**, with a residual (new NOTE N-a) | Code: `guard.py:52`, `:118-127`. The self-tests assert it |
| m3 | Term (e)'s static check is easy to evade and skips the drivers | **LARGELY FIXED**, with a residual (NOTE N-g) | Code: `guard.py:99-101`, `:249-347`. Probe `probe_static_guard2.py` |
| m4 | The register never checks the substituted value | **FIXED** (by qualified name), with a residual (NOTE N-h) | Code: `register.py:45-47`, `:100-105`. Probe `probe_static_guard2.py` |
| m5 | The checkpoint identity does not bind olmo_hf.py | **FIXED** | Code: `gcal.py:85-86`, `:224-232` |
| m6 | Self-test seams accepted on a canonical run | **FIXED** | Code: `gcal.py:390-391`. The self-test case "seam" |
| m7 | Self-tests that cannot fail | **FIXED** | Code: `proxy.py:96-146`, `gcal.py:600-608`, `:732-742`, `testing.py:33-59` |
| m8 | Self-test results depend on the record and the parallel track | **FIXED** as listed, but the M1 fix adds a new instance (new MINOR R2-3) | Code: `gshape.py:224-228`, `:304-319`, `:483-494`; `p_sessions.py:225-227` |
| m9 | Model-free refusals placed after the load | **FIXED**, with doc residuals (NOTE N-j) | Code: `gcal.py:392-406` |
| m10 | The G-CAL-p call restates m's call instead of importing it | **ADDRESSED AS A DECLARED DEVIATION**: PIN P21 / FLAG F-p7, pending the seat; residuals in NOTE N-f | Code: `gcal.py:441`, `:496-560`, `:600-608`. Probe `probe_ast_pin.py` |
| m11 | G-SHAPE-p can record m's package hash from an uncommitted tree | **FIXED** for G-SHAPE-p; the same class remains in G-CAL-p (NOTE N-i) | Code: `gshape.py:210-221`, `:293-297` |
| N1 | gcal identity: `proposal_sha256` is p's | **UNCHANGED**, now stated in gcal's PIN (`gcal.py:33-39`); still the seat's to confirm | Read |
| N2 | Conditions (1)–(3) are in no artifact | **FIXED** (`gcal.py:335-343`, `:360`), but the fix creates a register site after the load (new MINOR R2-1) | Read; probe `probe_postload_register*.py` |
| N3 | Only the hair trigger is recorded as a STOP | **FIXED**: every loop STOP goes through `_stop` (`gcal.py:443-455`). Caveats: new MINOR R2-2 and NOTE N-d | Self-test; probes `probe_stop_launched.py`, `probe_proxystop_record.py` |
| N4 | Some STOPs exit 1 | **FIXED** on the gcal and gshape paths (SystemExit → 4); residual in NOTE N-c | Read; probe `probe_schedule_partial.py` |
| N5 | The schedule builder's output is post-processed | **UNCHANGED by design**: a PIN, flagged for the seat (`schedule.py:8-16`) | Read |
| N6 | Citations off by a line or two | **FIXED** | Checked at source: `olmo_hf.py:286` is `text=self.decode(gen).strip()`; `m/schedule.py:512` is the `key_template` literal; `corr.py:236` is the replacement expression |
| N7 | Looking ahead to the stage wiring | **PARTLY**: the register PIN is now false for a G-CAL-p site (R2-1); `.podchange-*` set-asides are still not admitted (NOTE N-k); entry (3)'s roots are still unbuilt (carried forward) | Read |
| N8 | Register `kind` labels | **PARTLY**: entry (3) is now `("clock", "roots")`; entry (4) is still `"eligibility"` for a renders source (inert while unexercised) | `register.py:67-76` |
| N9 | Counters | **FIXED**: `cap_hits_returned_in_cuts` (`gcal.py:351`), and the trigger STOP keeps its text in `stop.text`. A STOPped run still builds no artifact, so it tabulates no counters | Read |
| N10 | The weights check is a drifting copy of m's | **FIXED**: per-file `OSError` handling; `run_gcal` checks and loads the same `w["path"]` (`p_sessions.py:118-151`, `:171`, `:181`) | Read; the self-test |
| N11 | No dynamic-evidence pointer | **FIXED** (`gshape.py:379-385`) | Read; the self-test |

### Evidence for the key rows

**M1 (FIXED).**
- Driver case 1 (`p_sessions.py:258-270`) runs `gcal` for OLMo-sft, Q-F0 and OLMo-base. It removes the pod id (`clear=True`), points gcal's `GATES_DIR`/`CKPT_DIR` at a scratch root, and traps `_load_olmo`. POD ID ABSENT is then always among the precheck's problems.
- Driver case 2 (`:271-293`) sets a pod id, mocks `committed_problems` and the weights check, replaces `gcal.run` with a recorder, and puts an `olmo_hf` stand-in that refuses construction into `sys.modules`.
- gcal's own non-stub case (`gcal.py:714-731`) removes the pod id and patches the roots.
- `resume.pod_id()` reads only `RUNPOD_POD_ID` (`m/resume.py:248-259`), so removing the variable is sufficient.
- **Probe `probe_m1_box_selftest.py`.** Setup, in this process only: `RUNPOD_POD_ID` set, `gcal.committed_problems` returning `[]` (the post-BUILD state), and a sentinel `valence_core.adapters.olmo_hf` that records any construction. Result:
  - driver integration checks 12/12;
  - the real `_load_olmo` never called;
  - no adapter constructed;
  - `data/p` byte-identical before and after (19 files).
- The full self-test in the same state is 101/101.
- The `sys.modules` restore drops only the stand-in it added (probe `probe_sysmodules_restore.py`).

**m1 (FIXED).** Probe `probe_canon_links.py` replicated the canonical layout in scratch, with gcal's roots rebound. Each of these is refused by `gcal.paths()` before anything is read or written:
- a symlinked `ckpt` directory;
- a symlinked `gates` directory;
- a link at the checkpoint's `.tmp` name;
- a dangling link at the checkpoint;
- a link at the artifact.

The clean layout is allowed. A directory at a temp name is refused by both `atomic_write_nofollow` and `write_once_bytes`. Both writers open the temp file with `O_NOFOLLOW`. The schedule writer goes through `write_once_bytes` (`schedule.py:100-104`).

**m3 (LARGELY FIXED).** `PLANTED` (`guard.py:361-378`) covers round 1's eleven forms and five more, and the driver is scanned (`scanned_files`, `guard.py:99-101`). The current production code has no false positive (`substitution_problems()` returns `[]`). A residual remains (NOTE N-g).

**m7 (FIXED).** Each round-1 gap now has a test that can fail:
- (a) `Fixed` returns a prepared object with `cap_hit=True, stop_reason="cap"`; the check asserts `is raw` and no cut.
- (b) `Fixed` carries `path`, `choice_window` and `provenance()`.
- (c) `assert_olmo_adapter`, `build_ban_list` and `tokenizer_appends` run through the proxy. The full `_startup_olmo` still runs through it nowhere, because b3's scaffold assertion cannot pass on a stub. That is acceptable.
- (d) All 128 calls are compared with m's procedure.
- (e) `ChunkScriptedAdapter` makes `---\n\n` one token.

**m8 (FIXED as listed).**
- (a) `compare_f0` reads HEAD's blob, beside a direct enumeration check against m's own placements.
- (b) The check was removed.
- (c) The schedules check is unconditional.

**m10 (DECLARED DEVIATION).** The segment now comes from `m_gcal.SEGMENT_FORM`. The AST pin plus the 128-call dynamic check are declared as PIN P21 / FLAG F-p7. Probe `probe_ast_pin.py` checked the pin against edited copies of m's `run_completability`:
- The pin fails for the right reason on six substantive edits: an added `stop_newline=False`, `cap - 1`, `'Answer:'`, a literal OLMo cap, a stripped record text, and `seed + 1`.
- It reports "a generate call is missing" for an aliased call.
- It raises on a benign refactor (NOTE N-f).

**m11 (FIXED for G-SHAPE-p).** On the canonical run, m's package must hash equal over the committed blobs (testing.py included), a fresh re-hash and the cached value, or the run is refused. The recorded hash is therefore a committed tree's.

---

## Part 2. New findings (regressions and defects in the round-2 code)

No MAJOR. Three MINOR, eleven NOTE.

### MINOR

#### R2-1. A register site now runs after the model load, contrary to the register's PIN; a live library thread would STOP G-CAL-p after all 128 generations, unrecorded and unrecoverable by resume

**Where:**
- `valence_core/p/gcal.py:360`: `artifact()` calls `conditions(pool)`.
- `gcal.py:336`: `conditions()` calls `corrupt.conditions_1_2(pool)`.
- `corrupt.py:137`: that calls `corrupt_p` → `register.substituted(1, …)` → `assert_single_threaded` (`register.py:81-85`).
- `artifact()` is called at `gcal.py:464`, after `adapter_factory()` and after the loop.
- `register.py:17-19` declares: "every site runs before any model load, so a library's background thread cannot be present at a site of record."

This is the side effect of the round-1 NOTE 2 fix: conditions (1)–(2) are now recomputed inside the artifact builder.

**Failure scenario, probe-verified** (`probe_postload_register.py`, `probe_postload_register2.py`; a stub run with one Python thread left alive by the "load"):
1. All 128 generations are written: `records 128`, `stop None`, `launched [128]`.
2. `artifact()` raises `RegisterStop: … 2 threads alive`. No artifact is written, and the driver exits 4 ("STOP: REGISTER STOP …").
3. A `--resume` in a fresh process passes precheck (no thread before the load) and makes the adapter again, then STOPs at the same site: `launched [128, 0]`, `adapters made 2`.
4. Recovery needs a code change. That moves `p_package_sha256` in the identity, so the complete checkpoint is refused as CHECKPOINT MISMATCH. The gate's 128 generations would then have to be redone: a second run of a gate p §0.5 runs "once".

**Likelihood.** Not testable here (no torch on this laptop).
- transformers 5.x's loader uses a `ThreadPoolExecutor` shut down with `wait=False` (local 5.5.0 `core_model_loading.py:1125`, `:1270`; the box has 5.15.0). Its workers normally exit long before the artifact is built.
- No other persistent Python thread is known.

The rationale the PIN gives for placing sites before the load no longer holds for this site.

**Fix.** Compute `conditions(pool)` in `precheck`, which is model-free and runs before the load, and pass the block into `artifact()`. The PIN is then true again.

#### R2-2. A STOP raised before any generation is launched is recorded with `launched` already incremented

**Where:** `gcal.py:443-450`. In the `except SystemExit` branch, `entry["launched"] += 1` runs for every loop STOP. That includes `m_guard.assert_insulated()` and `m_sc.assert_boundary(...)`, which raise before `px.generate` is called.

**Failure scenario, probe-verified** (`probe_stop_launched.py`): an adapter whose encode breaks rule 28(d)(a)'s boundary at key 3 gives:
- `generate calls made: 3`
- `records: 3`
- `provenance launched: [4]`
- `stop: {'trigger': 'SystemExit', 'key': 3}`

The stopped checkpoint (the seat's evidence for the STOP) claims one more launched generation than ran.

**Context:**
- For the hair trigger and for a `ProxyStop`, the generation did run, so +1 is right there.
- m's `launched` counts generations recorded: it is incremented right after the record is appended (`m/gcal.py:1171-1172`).

**Fix.** Increment only once `px.generate` has returned or raised. For example, set a `launched_now` flag immediately before the call, or put `assert_insulated`/`assert_boundary` in their own `try` that records the STOP without incrementing.

#### R2-3. The M1 fix's simulated-box case depends on CLAUDE.md being committed and unedited (N12's class, reintroduced)

**Where:** `scripts/p_sessions.py:271-293`.
- Case 2 runs the real `gcal.precheck` with only `committed_problems` and the weights check mocked.
- The precheck's real `m_gcal.gate_line(...)` (`gcal.py:215`) requires CLAUDE.md committed at HEAD with identical working-tree bytes (`m/gcal.py:617`).

**Failure scenario, probe-verified** (`probe_state_dependence.py claude-dirty`). With CLAUDE.md carrying an uncommitted edit (simulated in-process by `stages._committed` reporting it edited), the self-test reads 100/101. The FAIL is "p_sessions: on a simulated clear box …".

This is a working-tree state the memory notes say occurs: the PI's parallel session in the same tree. Nothing is written or loaded; the self-test simply fails for a reason unrelated to p.

**Fix.** In case 2, also stand in for `gate_line` (as `committed_problems` is), or for `_committed` on CLAUDE.md. The case then holds in every state, as N12 asks.

### NOTE

#### N-a. A case-variant spelling of `data/` passes p's test-output guard on the laptop

**Where:** `guard.py:104-127`. `_under` compares resolved `Path` objects case-sensitively, but the laptop's volume is case-insensitive.

**Verified by probe** (`probe_case_paths.py`, decision logic only; nothing written):
- `refuse_test_out(<repo>/Data/p/gates)` is ALLOWED, and so are `Data/m/gates` and `DATA/olmo`.
- `Data/p` is the same directory as `data/p` by inode.
- So `p_sessions.py gshape --out <repo>/Data/m/gates` would write `G-SHAPE-p.json` into m's directory of record. A stub `gcal.run(…, out_dir=<repo>/DATA/p)` would put a stub checkpoint at `data/p/ckpt/G-CAL_olmo-sft.json`.

**Context.** Inherited: m's `resume.refuse_canonical_out` allows the same paths. The box (Linux) is unaffected.

**Fix.** Compare `(st_dev, st_ino)` of the nearest existing ancestor with the refused roots, or `os.path.samefile`. This is likely best done across packages, by the seat's choice.

#### N-b. The schedule writer can refuse after writing

**Where:** `schedule.py:94-104`. The pre-write clash check reads the final names only. A link or non-file at a later file's `.tmp` name is found by `write_once_bytes` mid-loop.

**Verified** (`probe_schedule_partial.py`): a link at the sixth file's temp name gives a `ScheduleStop` after five files are written. Nothing is written through the link.

**Consequence:** small. The files written are byte-identical to a full run, and a re-run completes the set.

**Fix.** Check every `.tmp` name in the clash pass.

#### N-c. Some STOPs exit 2 as "REFUSED", against the driver's PIN

**Where:** the driver's PIN (`p_sessions.py:35-38`) says: "Any other STOP raised on the way (a register or keys STOP among them) exits 4, named." Two paths do otherwise:
- `build_schedules` maps every `SystemExit` to `REFUSED` / exit 2 (`p_sessions.py:83-85`). Probe `probe_schedule_partial.py`: a planted `RegisterStop` gives `exit 2 | REFUSED: REGISTER STOP …`.
- `gcal.precheck` turns any `SystemExit` from `corrupt.renders_problems()`, a `RegisterStop` included, into a refusal problem (`gcal.py:201-204`), so the driver exits 2. Seen in `probe_postload_register.py`'s in-process resume: `GcalPRefusal … ["renders: REGISTER STOP …"]`.

**Consequence:** nothing is loaded in either case. Only the declared exit code and label differ.

#### N-d. A ProxyStop keeps only 40 characters of the generation it stops

**Where:** `gcal.py:448-450` records `text=None` for every non-trigger STOP. The `ProxyStop` message carries `text[:40]` (`proxy.py:57-59`).

**Verified** (`probe_proxystop_record.py`): `{'trigger': 'ProxyStop', 'key': 0, 'text': None}`. The detail ends at `…opposite of 'enter'`, and the returned tail ("and a long tail of more words") is lost.

**Consequence:** rule 25's read of every generation then has a truncated text for exactly the case the seat must adjudicate.

**Fix.** Attach the returned text to `ProxyStop` and store it in `stop.text`, as the trigger does.

#### N-e. (Pre-existing; not raised in round 1) §2.2 says "Nothing after the cut is stored", but the cut log stores the returned text

**Where:** the cut event's `text_returned` (`proxy.py:62`) goes into the checkpoint's `cuts` (`gcal.py:460-461`) and into the artifact of record (`stored_text_invariant.cuts`, `gcal.py:361-362`). It includes everything after the cut, e.g. `"---\n\nTask: Write the opposite of 'enter"`.

**Consequence:** no record text, grade, counter or trigger reads it. The seat should confirm that the audit log is outside §2.2's "stored". Rule 25's read argues for keeping it.

#### N-f. Limits of the AST pin (PIN P21)

- **(i) It runs only in the self-test.** G-CAL-p's precheck does not run `_call_pin_problems()`. G-CAL-p runs before any LOCK-p names m's file shas (p §4.3), so a committed change to m's `gcal.py` between the BUILD and G-CAL-p goes unseen at run time, unless the self-test is re-run. The pin is cheap and model-free; running it in precheck closes this.
- **(ii) It raises rather than reporting on a benign refactor.** It `eval`s m's `seg` expression (`gcal.py:523`). On a benign refactor such as `seg = SEGMENT_FORM.format(task=task)` it raises `NameError` (probe `probe_ast_pin.py`). Because the call sits inside the first `chk(...)` (`gcal.py:585-587`, evaluated twice), the exception aborts gcal's whole self-test: its 21 checks are replaced by one "_selftest raised" FAIL. This fails closed, but the check count changes.

#### N-g. m3 residual: forms outside `PLANTED` still evade term (e)'s static check, and the docstring overclaims

**Where:** `guard.py:249-286`; the docstring at `guard.py:20-28`.

**Verified** (`probe_static_guard2.py`). Eight forms evade:
- a function parameter (`def swap(mod, f): mod._eligible_m = f`);
- a `for` alias;
- a `with … as` alias;
- `mm = sys.modules['valence_core.m.corr']; mm.x = …`;
- `c = importlib.import_module('valence_core.m.corr'); c.x = …`;
- `getattr(corr, '__dict__')[…] = …`;
- a walrus;
- `s = setattr; s(corr, …)`.

**Doc overclaim:** "any import form … a local alias included" claims more than the check does. The first and fifth forms are natural in helper code.

**Fix.** Either track parameters and `import_module` results, or narrow the docstring's claim. The runtime restoration checks stand beside it.

#### N-h. m4 residual: the register's value check is by qualified name

**Where:** `register.py:100-105`.

**Verified** (`probe_static_guard2.py`): `functools.wraps(corrupt.eligible_p)(lambda t: [1])` is ACCEPTED for entry (1), and inside the block the rule returns `[1]`.

**Assessment:** accidental misuse is caught; deliberate re-labelling is not.

**Fix.** An identity check (`is`) against the object found by a lazy import of the declared qualified name would close it.

#### N-i. m11's class remains in G-CAL-p

**Where:**
- The identity's `package_sha256` is m's `resume.package_sha256()` over all 18 `valence_core/m/*.py`, via `_identity_olmo`.
- `committed_problems()` (`gcal.py:147-156`) checks only the 17 `M_HASHED` m files. `m/testing.py` is not among them.

**Failure scenario:** an uncommitted edit to `valence_core/m/testing.py` on the box would be recorded as an m package hash that no commit has. Low likelihood on the box.

**Fix.** Check every m package file in G-CAL-p's committed check, as canonical G-SHAPE-p now does.

#### N-j. Doc and order inaccuracies

- `__init__.py:19-20` still says gcal takes "m's prompt, seeds, grader and generation call by import". `gcal.py:17-21` says the call is restated and pinned.
- `gshape.py:47` says an `--out` run is "refused under data/m, data/mf3 and data/p/gates". It is now refused under all of `data/`, and under `/workspace/models`.
- The driver docstring (`p_sessions.py:24-26`) places "the DRIVER and WEIGHTS lines" after G-CAL-p's run checks (key set, honesty, checkpoint validity, pod change). They are printed at `:175-179`, before `gcal.run` is entered (`:181`). The result: a POD CHANGED refusal appears after both lines, and without the "; nothing loaded" suffix the precheck refusals carry.
- `gcal.py:24` says "Every refusal that needs no adapter runs before the load". `paths()` checks `.tmp` names for symlinks only (`gcal.py:137-140`). So a non-file (e.g. a directory) at the checkpoint's or the artifact's temp name is refused only at the first checkpoint write, after the load, or at the artifact write, after 128 generations.
- `GcalPRefusal`'s docstring, "Nothing generated past it" (`gcal.py:98-99`), is false for the artifact-write refusal at `gcal.py:486-489`. That form is inherited from m.

#### N-k. Carried forward from round-1 NOTE 7

- `.gitignore` admits no `data/p/ckpt/*.json.podchange-*` set-aside (m's does, `.gitignore:242`). A G-CAL-p checkpoint set aside after a pod change would therefore live only on the box (rule 27).
- p's POD CHANGED message (`gcal.py:404-405`) drops m's instruction: "move the checkpoint aside by hand and run again without --resume".

---

## Part 3. Checked and clean (the task's specific questions)

**No self-test or stub run can write a record or load a model.**
- In the box state: probe `probe_m1_box_selftest.py`.
- The schedule, gshape and gcal self-tests write only to temporary directories.
- Every canonical write path is refused with a seam (gshape), with `out_dir` (schedules, `refuse_test_out`), or by the pod-id removal (gcal).
- The one gap needs a case-variant spelling passed by a caller (N-a).

**No new way to write through a symlink.**
- Every p write goes through `write_once_bytes` or `atomic_write_nofollow`: path not a link, temp not a link or non-file, `O_NOFOLLOW`.
- Parent directories up to `data/p` are checked in `paths()`, `gshape.write` and `write_schedule_files`.
- Hard links at a temp name are outside this class, and m's writers share the `O_TRUNC` pattern.

**Refusals after a write:** R2-1 (after 128 generations), N-b (the schedule set), and the inherited artifact-write refusal (N-j).

**The stricter checks give no false positives on today's production paths.**
- `corrupt_p`, `keys.substituted_keys` and `schedule.build_objects` pass both the static check and the register's value check. `build_objects`' `o["key_template"] = …` writes a fresh builder dict, not an m name.
- The alias set is file-wide and flow-insensitive. A future `x = m_mod.ATTR` anywhere in a file makes `x[...] = …` flagged everywhere in that file, which fails closed.
- The register's name check would STOP if p's modules were ever imported under another module name (e.g. run as `__main__`). That also fails closed.

**`read_checkpoint` plus `identity_problems` cover everything m's `_load_ckpt` enforces.** That includes the schema and exact key set, a dict identity compared on the union of keys, the record list as a key-order prefix with each record keyed, typed and re-graded by f0's grader, and provenance as a list. p adds: no STOP recorded, no stored line break, and well-formed cuts. Neither p nor m checks provenance entries' shape (a non-dict entry crashes at the pod-change check, exit 1, before the load) or `n_writes`' type. That is inherited and touches p's own files only.

**`_stop`.** It records the trigger, key, pool, i, seed_index and detail (and the text for the hair trigger), appends no record for the key, writes the checkpoint, and the STOPped checkpoint is refused on resume before any adapter is made. Defects: R2-2 (`launched`) and N-d (the ProxyStop text).

**The AST pin fails for the right reasons** on each substantive change to m's call tried (probe table above). Its limits are in N-f.

**Spot checks.**
- The real adapter's `generate` takes `injections` positionally (`olmo_hf.py:203-205`), as the proxy passes it.
- m's code sets no attribute on an adapter, so the read-only proxy is safe.
- `_is_stub`, `assert_olmo_adapter`, `olmo_ban_list` and `assert_boundary` are all duck-typed and work through the proxy.

---

## Summary

Of round 1's 23 findings:
- **M1 is fixed.** Probe-verified in a simulated post-BUILD box state: no loader reached, no adapter made, data/p unchanged, 101/101.
- **Of the 11 MINORs:**
  - nine are fixed outright: m1, m2, m4, m5, m6, m7, m8, m9 and m11 (for G-SHAPE-p);
  - m3 is largely fixed;
  - m10 is addressed as a declared deviation (PIN P21 / FLAG F-p7) pending the seat.
- **Of the 11 NOTEs:** seven are fixed (2, 3, 4, 6, 9, 10 and 11; 4 with a residual), two are partly addressed (7, 8), and two are unchanged by design for the seat (1, 5).

Round 2 finds **0 MAJOR, 3 MINOR and 11 NOTE**:
- **R2-1:** the NOTE-2 fix put a register site (`corrupt_p` via `conditions`) after the model load. This falsifies the register's PIN, and a live library thread would STOP G-CAL-p after all 128 generations, unrecorded, with a resume that STOPs again.
- **R2-2:** a pre-generation STOP over-counts `launched`.
- **R2-3:** the new simulated-box self-test case fails whenever CLAUDE.md carries an uncommitted edit.

The NOTEs are residuals and documentation (N-a to N-k): a case-insensitive guard gap inherited from m, the schedule writer's partial write, STOP exit codes, the ProxyStop text, the logged `text_returned`, the pin's run-time scope, the static check's remaining evasions, the qualified-name check, the G-CAL-p m-hash scope, doc order, and the `.podchange` admits.

## 3. Round 3 (the agent's report, verbatim)

# Blind code review, round 3: `valence_core/p/` and `scripts/p_sessions.py` (the uncommitted p BUILD)

Reviewer: a blind agent, read-only. Tree: HEAD `9838664` (unchanged since round 2), with p uncommitted
(`valence_core/p/`, `scripts/p_sessions.py` and `data/p/` untracked; `.gitignore` and `.gitattributes` modified).
Spec: PROPOSAL-p v0.2 §1–§4 and §8; the seat's answers of 2026-11-07. Round 2's report: `p_build_review_r2.md`.

How this review was run:
- No repository file was edited.
- Every probe ran with `jlens-qwen36/.venv/bin/python -B` from the repo root. The probes are in
  `<tmp>/scratchpad/podwatch/probes3/`.
  They wrote only to scratch temporary directories (and edited copies of m's function under `probes3/astmods/`), and
  rebound module attributes only inside their own processes.
- `git status --short` was byte-identical before and after all runs. `data/p`'s 19 files hashed identical before and
  after.

**Self-test as run here: 101/101** (about 9.5 s). It is also 101/101 in a simulated post-BUILD box state (pod id set,
gcal's committed check clear) and with CLAUDE.md simulated as carrying an uncommitted edit.

No round-2 snapshot of the code exists in the scratchpad (`site/wt-final1` is the current tree), so each disposition
was verified at source and by probe, and the changed areas were re-read in full.

---

## Part 1. Round-2 items and their round-3 status

| R2 | Round-2 finding (short) | Round-3 status | Verified by |
|---|---|---|---|
| **R2-1** | A register site (`conditions` → `corrupt_p`) ran after the model load | **FIXED** | `gcal.py:223-226` computes `conditions(pool)` in `precheck`, before the factory (`:413`). `artifact()` takes the block as an argument (`:351`, `:365`, `:474`) and reaches no register site. Probe `probe_r21_postload_register.py`: with a library-like thread started by the factory, the run completes (128 records, artifact written, no STOP). Importing the driver loads no torch or transformers and leaves one thread, so precheck's sites are single-threaded on the box too. `register.py:17-19`'s PIN is true again for G-CAL-p. |
| **R2-2** | A STOP before the generation over-counted `launched` | **FIXED** | `gcal.py:450-454` (insulation, boundary: no increment); `:455-460` (a STOP out of `px.generate`: +1); `:462`. Probe `probe_r22_launched.py`: boundary at key 3 → 3 calls, 3 records, launched 3; insulation at key 2 → 2, 2, 2; ProxyStop at key 5 → 6 calls, 5 records, launched 6. The real adapter's `generate` raises no SystemExit (`olmo_hf.py:203-289`), so the +1 applies to the proxy's STOP only, after the generation ran. |
| **R2-3** | The simulated-box case depended on CLAUDE.md being committed | **PARTLY**: fixed for CLAUDE.md; the stand-in's own return value still reads a record file (new MINOR **R3-1**) | `p_sessions.py:284` stands in for `precheck`, but `:279` calls `m_gcal.weights_of_record("sft")` outside the stand-ins. Probe `probe_r23_state.py`: CLAUDE.md dirty 101/101; box 101/101; OLMo manifest dirty 77/79. |
| **N-a** | Case-variant spellings of `data/` passed the test-output guard | **FIXED** | `guard.py:106-111` (casefolded comparison). Probe `probe_na_case.py`: `Data/p/gates`, `DATA/olmo`, `Data/m/gates`, `dAtA`, an upper- or lower-cased repo prefix, `data/../Data/p` and `/WORKSPACE/models/sft` are all refused. `gcal.paths`, `gshape.write` and the schedule writer each refuse `Data/...`. Prefix siblings (`data_scratch`, `Database`, `/workspace/models2`) stay allowed. On the box (Linux) it can only refuse more. |
| **N-b** | The schedule writer could refuse after writing | **FIXED** | `schedule.py:97-103`: one pass over every final and temp name before any write. Probe `probe_nb_nc_schedule.py`: five plants are each refused with 0 files written and the victim untouched: a link at the 6th temp name, a directory at the last temp name, a directory at the 10th final name, a FIFO at the 3rd temp name, and a dangling link at the manifest's name. A mid-loop refusal is now possible only through a race. |
| **N-c** | Some STOPs exited 2 as "REFUSED" | **FIXED** as stated; a residual in NOTE **R3-4** | `p_sessions.py:78-91`; `gcal.py:206` with `corrupt.py:159` (only `CorrStop`/`ValueError` caught). Probes: `--build-schedules` with a register STOP exits 4, a ScheduleStop 4, a mismatch 2; `gcal` with a register STOP in precheck exits 4 ("STOP: REGISTER STOP …; nothing loaded"). |
| **N-d** | A ProxyStop kept 40 characters of its text | **PARTLY**: 200 characters now, which still truncates realistic texts (NOTE **R3-3**) | `proxy.py:59`; `gcal.py:458-460` (`text` still None for a ProxyStop). |
| **N-e** | The cut log stores the text after the cut | **AS STATED**: flagged as F-p10 (BUILD entry draft `build_entry.md:73-74`, design body `:176-177`); code unchanged | Read: `proxy.py:62`, `gcal.py:471`, `:366-367` |
| **N-f** | Limits of the AST pin (PIN P21) | (i) **FIXED**: `precheck` runs it (`gcal.py:207`). (ii) **PARTLY**: an eval failure is now reported (`:533-540`), but other inputs still make it raise (NOTE **R3-2**) | Probes `probe_nf_pin.py`, `probe_nc_nf_gcal.py` |
| **N-g** | Static-check evasions; the docstring overclaimed | **FIXED**: the docstring is narrowed and caveated (`guard.py:20-30`). The eight forms still evade, as it now allows. Small wording residual in NOTE **R3-8** | Probe `probe_ng_nh.py` |
| **N-h** | The register's value check was by qualified name | **FIXED**: by identity with the object the declared name resolves to (`register.py:100-104`, `:119-126`; self-test `:158-168`). Residual in NOTE **R3-5** | Probe `probe_ng_nh.py`: a `functools.wraps` stand-in is refused |
| **N-i** | G-CAL-p's committed check missed `m/testing.py` | **FIXED** | `gcal.py:151-161` globs every `valence_core/m/*.py`. Probe `probe_ni_nj.py`: `testing.py` is named when edited; the 18 files are exactly the package hash's set. |
| **N-j** | Doc and order inaccuracies; non-file temp names | **FIXED**. A residual on the ORDER docstring's first sentence is in NOTE **R3-6** | `__init__.py:19-21`; `gshape.py:47-48`; the driver's order (`p_sessions.py:18-29`) matches `run_gcal` (`:164-182`); `gcal.py:139-144` refuses a non-file at either temp name or path. Probe `probe_ni_nj.py`: a directory or FIFO at a temp name, or a directory at either path, is refused with 0 factory calls. `GcalPRefusal`'s docstring (`:100-101`) is accurate. |
| **N-k** | POD CHANGED text; `.podchange` admit | **FIXED** | `gcal.py:409-412` carries m's "move the checkpoint aside by hand and run again without --resume". `.gitignore` admits `/data/p/ckpt/*.json.podchange-*` (`git check-ignore`: admitted). `.gitattributes`' `/data/p/ckpt/** -diff` covers it (`check-attr`: diff unset), and `*.tmp` stays ignored. |

**Tally of round 2's 14 items:** 10 fixed, 3 partly fixed (R2-3, N-d, N-f), and 1 flagged for the seat as stated
(N-e). None is unaddressed.

---

## Part 2. New findings

**0 MAJOR, 1 MINOR, 7 NOTE.** R3-1 to R3-6 are residuals of round-2 items; R3-7 and R3-8 are new.

### MINOR

#### R3-1. R2-3's stand-in still reads a record file: with `data/olmo/manifest.json` dirty, the driver's integration self-test raises and the check count drops

**Where:**
- `p_sessions.py:279`: `_wp0, w_sft = m_gcal.weights_of_record("sft")` runs outside the `with` of stand-ins, and its value is fed to the precheck stand-in (`:284`).
- `run_gcal`'s WEIGHTS line (`:178`) then subscripts `w`.
- The weights-files case reads the same file's committed blob (`:297`, `:299-300`).
- gcal's own stub runs need it too: `precheck` requires the manifest of record on every run, stub included (`gcal.py:211-212`), as m's precheck does. It also requires G-CAL-OLMo's reference artifact and the seat's answers raw (`:208-210`).

**Failure scenario, probe-verified.** Probe `probe_r23_state.py manifest-dirty` simulates the edit in-process: `m_stages._committed` reports `data/olmo/manifest.json` as edited.
1. `weights_of_record` returns `(problems, None)`, so the stand-in returns `{"weights": None}`.
2. `run_gcal` prints the DRIVER line, and then `w['repo']` raises `TypeError`.
3. The `run()` helper catches only SystemExit, so the driver's `_selftest` aborts: "p_sessions: integration selftest raised TypeError: 'NoneType' object is not subscriptable". Its four remaining checks never run.
4. gcal's `_selftest` also raises at its first stub run (`GcalPRefusal … weights of record`).

The result is **77/79**, not 101/101. The same mechanism gives 80/82 with the reference artifact dirty and 68/71 with
the answers raw dirty (gshape's self-test as well).

**Likelihood.** `data/olmo/manifest.json` is a shared record file that n's acquisition (G-ACQ) edits, and the PI's
parallel session shares the tree. Nothing is written or loaded. The self-test fails for a reason unrelated to p, and
the check count changes, against m's PIN that the count is the same on every site.

**Fix.**
- In case 2 and in the weights-files case, use a literal weights dict and a literal file list. The case's own words, "so no state of the record matters", then hold.
- Whether gcal's stub runs should keep requiring those three committed inputs is the seat's reading of N12. They are inputs the stub's identity and its clean-pool comparison read. The question is "every state of the record" in m's `993eba1` sense (records present or absent) versus edits to committed inputs.

### NOTE

#### R3-2. (Residual of N-f.) The P21 pin, now in precheck, can still raise instead of reporting

**Where:**
- `gcal.py:512-513`: `inspect.getsource` → `ast.parse`, called at `:530`.
- `:566-567` and `:571-572`: `k.value` on the record literal's dict keys.
- All of it reached from `precheck` (`:207`), outside any handler.

**Verified:**
- **Source unavailable** (`probe_nc_nf_gcal.py`). With `inspect.getsource` raising OSError, `p_sessions.py gcal --unit OLMo-sft` raises OSError out of `main`, both on the laptop and on a simulated box. The process would exit 1 with a traceback. Nothing is loaded or written.
- **Benign record-literal refactors** (`probe_nf_pin.py`). Two of them raise AttributeError: a `**` spread (`rec = {**base, …}`, whose key is None) and a key given by a name (`{POOL_KEY: …}`, an `ast.Name`). An eval failure is now reported, as intended: "m's segment expression no longer evaluates alone (NameError)".
- **Source changed on disk after import** (simulated by shifting linecache's lines by 3). The pin reports "a generate call is missing": fail-closed, but the message misleads.

**Likelihood on the box:** low. The box runs a git checkout (`/workspace/repo/jspace-lab`, Python 3.12.3, against
the laptop's 3.12.9, so the AST is the same), so the source is available.

**Consequence:**
- A traceback with exit 1, which the driver's 0/2/4 does not declare, before the load.
- In the self-test, gcal's whole self-test collapses to one "_selftest raised" FAIL.

**Fix.** Catch `(OSError, TypeError, SyntaxError, AttributeError)` inside `_call_pin_problems`, around `fn_tree` and the
key extraction, and return a pin problem. `precheck` then refuses with exit 2, naming the pin.

#### R3-3. (Residual of N-d.) A ProxyStop's text is still cut, now at 200 characters

**Where:**
- `proxy.py:58-59`: the excerpt is `text[:200]!r`.
- `gcal.py:458-460`: a ProxyStop is recorded with `text=None`.
- `_stop` keeps `detail[:600]` (`:384`).

**Verified:**
- Of the 384 committed G-CAL-OLMo record texts, 26 exceed 200 characters (5 sft, 12 dpo, 9 instruct; the longest is 316). Cap-hit texts run 166–316 characters.
- Probe `probe_r22_launched.py`: a 347-character returned text with its break near the end leaves a `stop.detail` that holds neither the whole text nor its tail.

**Context.** A ProxyStop needs a tokenizer whose decode cannot place the break. Round 1's probe of OLMo's tokenizer
found no such token, so this case is near-unreachable.

**Fix (if wanted).** Carry the returned text on the exception and store it in `stop.text`, as the hair trigger does.

#### R3-4. (Residual of N-c.) One STOP class still exits 2 on the gcal path; some errors exit 1

**Where:** `corrupt.py:159` catches `corr.CorrStop` and turns it into a problem. `CorrStop` is a SystemExit raised as "RENDERS STOP", "CORRUPT_M STOP" or "POOL STOP". The two stages then treat that problem differently:
- `gcal.py:206` makes it a refusal.
- `gshape.py:257-259` makes it a STOP.

**Verified** (`probe_nc_corrstop.py`). One planted `CORRUPT_M STOP` gives:
- exit 2 through `gcal`: "REFUSED: … renders: CORRUPT_M STOP …";
- exit 4 through `gshape --out`: "STOP: G-SHAPE-p STOP: the renders of record do not reproduce …".

The driver's PIN (`p_sessions.py:38-39`) says any other STOP raised on the way exits 4.

Separately, a non-SystemExit error on the way exits 1 with a traceback:
- `--build-schedules --out <a regular file>` raises FileExistsError at `schedule.py:108` (probe);
- R3-2's OSError.

Nothing is written in either case.

**Consequence:** the label and the exit code only.

#### R3-5. (Residual of N-h.) The identity check binds the declared name's current object, not the committed one

**Where:** `register.py:101` compares with `_resolve(qualified)`, the name's binding at the time of the call
(`:119-126`).

**Verified** (`probe_ng_nh.py`):
- With `valence_core.p.corrupt.eligible_p` rebound in-process to another rule, `corrupt_p` passes the register: the render is the clean text, with n_eligible 1 and k 0.
- Term (e)'s static check does not flag the rebind (`corrupt.eligible_p = …` evades), because it polices m objects only.

**Downstream.**
- `renders_problems` (the sixteen pinned renders and both shas) would refuse any such change in G-CAL-p and G-SHAPE-p.
- For entry (2), rebinding `keys.item_key` makes the register STOP, because `P_FUNCS` holds the originals (`keys.py:59`).

So this is deliberate-misuse territory only.

**Fix (if wanted).** Capture each built entry's replacement objects once (at p's import or at first use), or extend the
static check to p's own replacement names.

#### R3-6. (Residual of N-j and round-1 m9.) On a resume, a model-free identity mismatch is refused only after the load

**Where:**
- `gcal.py:24` says "Every refusal that needs no adapter runs before the load".
- The identity comparison (`:426-431`) follows the factory (`:413`).
- Most identity fields are model-free: the proposal, renders, package, olmo_hf and driver hashes, the key set, the pool and the weights. Only the backend identifier and the ban ids need the adapter.

**Verified** (`probe_resume_identity_order.py`):
1. A stub run crashed at key 5, a non-SystemExit error, so no stop was recorded.
2. p's package hash was then moved (simulated in-process).
3. The `--resume` was refused as CHECKPOINT MISMATCH only after the factory had been called a second time.

On the box, that second factory call is a 64 GB load (176–212 s cold), spent on a refusal that could be decided before it.

**Context:** `:30-31` declare the identity comparison as after the load, and m places it the same way.

**Fix (optional).** Compare the identity's model-free fields with the checkpoint before the load, or narrow `:24`'s first
sentence.

#### R3-7. The guard's roots claim overstates: a test output can land in a git-admitted directory outside `data/`

**Where:** `guard.py:11-14`: "…so a never-of-record file cannot land in a git-admitted directory." `refuse_test_out`
refuses only `data/` and the refused roots (`:123-132`).

**Verified:**
- `git check-ignore --no-index` admits a `*.json` in `results/raw/`, at the repo root, in `scripts/`, in `results/` and in `valence_core/p/`.
- `refuse_test_out` allows all of these (probe `probe_na_case.py`, decision only; nothing written).
- So `p_sessions.py gshape --out results/raw` would write an admitted `results/raw/G-SHAPE-p.json`, and `--build-schedules --out .` nineteen admitted JSON files at the root.

**Consequence:** small, since commits are made by pathspec.

**Fix.** Narrow the sentence to `data/`, or refuse the whole repository for a test output.

#### R3-8. Wording residuals

- **The driver's docstring.** `p_sessions.py:8-10` says the gcal cases run "with the pod id removed". Case 2 (`:278-287`) runs with a stand-in pod id (`selftest-pod`), with `precheck` and `run` stood in.
- **Term (e)'s docstring.** `guard.py:23-25` makes two positive claims that are wider than the check:
  - "no `vars()` or `__dict__` access on an m object": `getattr(corr, '__dict__')[…] = …` evades;
  - "no `setattr`/`delattr` family call": `s = setattr; s(corr, …)` evades.

  Its "module-level alias assignment" under-claims: an alias in a function body is caught too (probe).
- **The BUILD entry draft.** `build_entry.md:11` (scratchpad) still says each built entry's replacement is "enforced by qualified name". Since N-h it is enforced by identity with the object the name resolves to, as the design body's `:7` says.

---

## Part 3. Checked and clean

**No self-test or stub run can load a model or write a record.**
- Driver case 1 (`p_sessions.py:259-271`): pod id removed, gcal's roots a scratch root, the loader trapped; POD ID ABSENT, exit 2.
- Driver case 2 (`:272-296`): `precheck`, the weights check and `run` are stand-ins; the loader is trapped; the olmo_hf module is a stand-in that refuses construction.
- gcal's canonical-run cases (`gcal.py:754-771`): pod id removed, roots a scratch root, the factory a list append.
- All stub runs go through `refuse_test_out` (case-insensitive now).
- The full self-test is 101/101 in the box state. `data/p` was unchanged (19 files) and git status identical across every probe.

**No refusal after a write, other than the declared ones.**
- R2-1's post-load register site is gone. After the factory, `run` reaches only `identity()`, `artifact()` (`clean_identity`, `strict_grade`, `report.counters`, `licence_at_run`, m's `completability_artifact`) and the writers. None of these calls `corrupt_p`, `renders_p`, `conditions_1_2` or `substituted_keys`.
- What remains:
  - the artifact-write refusal, after the generations, declared in `GcalPRefusal`'s docstring;
  - the STOPs, which are recorded by design;
  - the schedule writer's mid-loop refusal, now possible only through a race.

**No new link-following write.**
- Every production write is `atomic_write_nofollow` or `write_once_bytes` (grep of every write primitive in p). The new checks (`gcal.paths`' non-file temp names, the schedule pre-pass) only add refusals.
- An inherited observation, not new: parent directories are link-checked once, in `precheck`. The checkpoint writes after the load re-check only the final name and its temp name, and `O_NOFOLLOW` guards the last component only. A link planted under `data/p` during the load would therefore be followed.

**No false positive of the register's identity check or the precheck's pin on today's code.**
- Legitimate uses pass:
  - `corrupt_p` (sixteen calls each in `renders_problems` and `conditions`);
  - `keys.substituted_keys` (the schedule builds);
  - `renders_problems() == []`;
  - the self-test, 101/101.
- `_resolve` imports only modules the driver has already loaded, so the runtime import set is unchanged; the guard self-test asserts `M_IMPORTED`.
- The pin returns `[]` on today's m and p. It fails for the right reason on round 2's six substantive edits, re-run here: an added `stop_newline=False`, `cap - 1`, `'Answer:'`, a literal cap, a stripped record text, and `seed + 1`.
- Both m asserts in the pre-generation `try` raise SystemExit (`session.py:55`, `scaffold.py:317`), so R2-2's split catches them.

**How a `_call_pin_problems` failure surfaces on the box** (the task's specific question): see R3-2. It is an uncaught
exception before the load (traceback, exit 1), with nothing loaded or written. It is unlikely there, because the box
runs a git checkout on the same Python minor version.

**Other.**
- The precheck runs twice on the canonical path (`p_sessions.py:164`, `gcal.py:397`). Both runs are before the load and model-free, so this is harmless.
- The real adapter's `generate` takes `injections` positionally, as the proxy passes it (`olmo_hf.py:203-207`).

---

## Summary

All 14 round-2 items were re-checked at source and by probe.
- **Ten are fixed:** R2-1, R2-2, N-a, N-b, N-c, N-g, N-h, N-i, N-j and N-k.
- **Three are partly fixed:**
  - **R2-3** holds for CLAUDE.md, but the stand-in's value still reads `data/olmo/manifest.json`.
  - **N-d** raises the excerpt to 200 characters, while 26 of 384 committed G-CAL-OLMo texts are longer.
  - **N-f** now runs the pin in precheck and reports eval failures, but `getsource` and two record-literal refactors still raise.
- **One is flagged for the seat as stated:** N-e (F-p10).

Round 3 finds **0 MAJOR, 1 MINOR and 7 NOTE.**
- **The MINOR (R3-1):** with the OLMo manifest dirty, the driver's integration self-test raises TypeError and the suite reads 77/79.
- **The NOTEs** are R2-3's and the other items' residuals: the pin's raise path, the ProxyStop excerpt, a CorrStop exiting 2 in gcal and 4 in gshape, the identity check binding the current name, and the post-load identity refusal on resume. Two are new: the guard's "git-admitted directory" overclaim and some wording.

No path was found by which a self-test or stub run loads a model or writes a record. No new refusal-after-write and no new link-following write was found.

