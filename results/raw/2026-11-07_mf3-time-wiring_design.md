# G-TIME-F3's wiring: `time` in `scripts/mf3_sessions.py` — Code's design, readings and PIN register (2026-11-07)

*Code's raw. The wiring of `time` (G-TIME-F3, PROPOSAL-m v1.11 m:293) in Q-F3's driver, under LOCK-m-F3 v0.1
(`1e79955`, sha256 `377c5d60…6ce7`). The edit is to `scripts/mf3_sessions.py` alone: nothing under `valence_core/`
changes, so mf3's `package_sha256` (`f30ad505…6310`), m's (`7756dcf4…49bb`), the analyzer (`d347ea0c…5e48`) and the
lock stand. The driver's blob moves from `fad31c20…0cbb` (`1e79955`) to `890084e6c626a3ced2007c4285c255fb73978c07aeca15427172fc17028690af`.*

## 1. Authority

- **LOCK-m-F3 v0.1 §11 item 1** (`1e79955`): "the `time` subcommand is wired in `scripts/mf3_sessions.py` at its
  step, after this lock's commit."
- **The PI's routing of 2026-11-07, item 1** (quoted at RESULTS.md@139635f:81): "… canonical `ganl` → LOCK-m-F3 v0.1
  → G-TIME-F3 [go] …".
- **The seat's F-1** (`results/raw/2026-11-06_ganl-f3_design-to-code_answers.md:24`): "Yes: the step-10 read's Q2
  clearance carries to `scripts/mf3_sessions.py` with the same scope — an edit that wires a subcommand at its step,
  touching no scoring-stack function, does not re-run G-SHAPE-F3; any other edit to the driver does."
- **The seat's F-2** (same raw, `:25`), verbatim: "**F-2.** Accepted: the campaign's ruling forms (O4-1, O1-3, RM4-1,
  VC4-1, VC4-2) and the rest of m's pre-load check arrive with the campaign subcommand's wiring, in
  `scripts/m_sessions.py`'s forms, each named in that step's entry; the docstring's declaration stands until then."
- **The coordinating session's routing of 2026-11-07** (chat, in reply to Code's question; quoted verbatim):

  > Build at time.
  >
  > Wire m's remaining pre-load checks at the `time` wiring, in scripts/m_sessions.py's forms:
  > - the MLXLM_USE_MODELSCOPE refusal;
  > - the local-path refusal;
  > - the hub's own offline resolution;
  > - the SNAPSHOT line;
  > - the post-load snapshot re-read with its model-id STOP.
  > Name each one in the G-TIME-F3 wiring entry.
  >
  > Why this follows the texts rather than reinterpreting them:
  > - `time` is the first Q-F3 stage that loads Qwen.
  > - Building the checks there satisfies all three texts. They are present when the campaign is wired, which is what the seat's F-2 ruling ("arrive with the campaign subcommand's wiring") needs, and they come with the stage wiring, as the build design §8 and the PIN say.
  > - They only add refusals before a load, plus a SNAPSHOT line in the raw. No measurement or verdict path changes.
  >
  > Carry it in the entry as a dated note under the e9b5022 precedent. Quote the seat's F-2 sentence and give this reading. If the seat reads F-2 as forbidding the checks before the campaign, that note is where it will see it.
  >
  > - The campaign's ruling forms (O4-1, O1-3, RM4-1, VC4-1, VC4-2) stay with the campaign, as ruled.
  > - The DRIVER line (the committed driver's blob sha256) is fine as you describe. Record it in the G-TIME-F3 entry and in LOCK-m-F3 v0.2, with your F-1 reading stated.
  > - Reading m_module_sha256 and the weights from the lock's committed text, with the analyzer sha, the package sha and renders_sha16 as flags in m's form, is fine too.

## 2. Code's readings

- **F-1, on the edit as made.** The edit wires a subcommand at its step and touches no scoring-stack function: every
  change is in the driver. Its changes beside the wiring itself are incidental to it, and none is a scoring-stack
  function:
  - the refusal text for `id`, `qual` and `campaign` ("is not wired yet") and the "no action" text ("… gshape or
    time");
  - the argparse description and the refused subparsers' help;
  - the module docstring;
  - the `os` and `stages` imports;
  - in the self-test: the runner capturing stderr, the quarantine check moved after the time checks, the rename
    `committed` → `committed_`, and the self-test's own additions.
  So G-SHAPE-F3 is not re-run. Its artifact (`0c9de56e…1461`) records the driver at `fad31c20…0cbb` in its sources
  map; that record stays the build's. LOCK-m-F3 v0.2 records the new blob.
- **The step-10 read's Q2 conditions, which Code reads F-1's "with the same scope" as carrying.** All four hold:
  - no change under `valence_core/m` (none under `valence_core/` at all);
  - the build reviewed as the step-10 edit was, with the self-test extended (three rounds, §6 and the review raw);
  - the new blob's sha256 printed by the DRIVER line and recorded in the G-TIME-F3 entry and in LOCK-m-F3 v0.2 (the
    routing above);
  - the new PIN sites declared on C6's terms as extended: the nine of §5, declared at LOCK-m-F3 v0.2.
- **F-2 (dated note, the e9b5022 precedent).** F-2's words place "the rest of m's pre-load check" with the campaign
  subcommand's wiring. The F3 build design §8 (`2026-11-06_mf3-build_design.md:145`) says it "comes with the driver's
  stage wiring (flag F-2)", and the PIN in `valence_core/mf3/stages.py` (`licence_problems`) says "built with the stage
  wiring (flag F-2)". Code builds it at `time`, as routed:
  - `time` is the first Q-F3 stage that loads Qwen;
  - so the checks are present when the campaign is wired, and they come with the stage wiring;
  - they add refusals before the load and the SNAPSHOT line; with them come the DRIVER line, and after the load the
    re-read line and three STOPs before any session. No measurement or verdict path changes.
  The campaign's ruling forms stay with the campaign. If the seat reads F-2 as forbidding the checks before the
  campaign, this note is where it will see it.
- **The values a run takes.** The analyzer's sha256, mf3's `package_sha256` and the renders' sha16 come as flags, the
  lock's values, in m's form. `m_module_sha256` and the weights binding are read from the lock's committed text, as
  routed: each of the eleven m files' one sha256 and the one WEIGHTS line. The licence's (f) is then satisfied by
  construction for those two; (e') and (g) still bind them to the files and the hub cache (the review's NOTE 1).
- **REVISION_STAGES, extended to `time`.** `run_time` refuses, before the load, a snapshot whose revision is not the
  lock's weights revision. That is m's REVISION_STAGES refusal (qual and campaign in m), carried to G-TIME-F3. The
  licence's (g) reads refs/main at the precheck; this read is the load's own, so a move between the two is refused
  before the load, not only by the re-read after it.

## 3. What the edit does, by function (m's form named for each)

- **The constants** (m's `TIME_*` form, with Q-F3's values): `TIME_LOCK_FILE` `"LOCK-m-F3.md"`; `TIME_COUNTS`, one session per
  template (A1, A1s, A2, A2s, A3, A3s; the committed time schedules' n is 1 each); `TIME_LOCKED_PATH` `"uncached"`;
  `TIME_REASONING_CAP` 60; `TIME_FLAGS`, the five flags, with `TIME_FLAG_HELP` keyed by flag. `TIME_REASONING_CAP`
  and `TIME_FLAG_HELP` have no counterpart in m.
  - `QWEN_MODEL_ID` is mf3.resume's model of record, QwenMLXAdapter's default and m's.
  - `MLX_LM_ALLOW_PATTERNS` is mlx_lm's `_download` default and m's.
  - `HF_OFFLINE_ENV`, `TOTALS_RX` and `TOTALS_REDACTED` are m's.
  - The self-test compares `QWEN_MODEL_ID` with mf3.resume's and gshape's by import, and reads the adapter's,
    mlx_lm's and m's values from their sources, not importing them.
- **`redact_totals`, `_say`** (m's): every REFUSED and STOP line of the stage path is redacted and goes to stderr.
- **`_load_qwen`** (m's): `qwen_or_explain` with the model id passed explicitly.
- **`lock_m_modules`, `lock_weights`** (new, as routed): they read from the lock's committed text the one sha256 the
  lines naming each of the eleven m files carry, and its one WEIGHTS line. A WEIGHTS line is one not glued to a
  letter, digit, underscore or hyphen, and it must name `QWEN_MODEL_ID`. Each refuses a file named with no sha256 or
  two different ones, no WEIGHTS line, two different ones, or another model.
- **`time_identity_extra`** (m's `stage_identity_extra` for "time"):
  - the proposal's and the lock's sha256, from their committed blobs;
  - the lock must be `LOCK-m-F3.md`, and its text must name the proposal's sha256 in full;
  - the analyzer's, mf3's package and the renders' values come as given;
  - `m_module_sha256` and the weights come from the lock's text;
  - `reasoning_cap` is 60 and `locked_path` `"uncached"`;
  - `stages._extra` validates it, non-stub.
- **`time_precheck`** (m's `stage_precheck` for "time"), the refusals that need no model:
  - the licence by file, (a)–(g);
  - the run-time known answers on the proposal named;
  - the renders of record;
  - the committed time schedules;
  - the checkpoint: its path, an ENDED one, and one that exists without --resume unless an end is pending, a looping
    link included;
  - m:267's laptop checklist;
  - the gate line, with CLAUDE.md and the analyzer committed.
  Every problem is redacted.
- **`driver_problems`** (m's): clear, with the committed blob's sha256, only when this process runs the driver of
  record (`REPO/scripts/mf3_sessions.py`), committed at HEAD with the working tree's bytes.
- **`qwen_snapshot`, `snapshot_line`** (m's, the checks verbatim):
  - HF_HUB_OFFLINE must be exactly "1", and MLXLM_USE_MODELSCOPE not "true" in any letter case;
  - no path or link named like the model id may exist in the working directory;
  - refs/main must be, as raw text, a 40-hex revision with a complete snapshot;
  - the hub's own offline resolution, with mlx_lm's patterns, must return that directory.
  The SNAPSHOT line names the model, the revision, the directory, the snapshot count and the offline value.
- **`run_time`** (m's `_run_stage` Qwen path, for "time"):
  - a missing flag is refused, and so is an out root with no stub factory;
  - then the identity, refused on its own;
  - then the precheck, the driver check, the snapshot check and the snapshot's revision against the lock's, refused
    together (exit 2, nothing loaded);
  - then the DRIVER line, the SNAPSHOT line, and the load;
  - then the re-read and the model id, each a STOP (exit 4) before any session (SNAPSHOT RE-READ REFUSED, SNAPSHOT
    MOVED, MODEL ID), and the re-read line;
  - then `stages.run_gate_stage(gate="time", templates_counts=TIME_COUNTS, resume=..., identity_extra=...,
    out_root=stages.DEFAULT_OUT)`.
  The exit code is `stages.EXIT_CODES` of the stage's status. Any SystemExit is a STOP (exit 4).
- **`main`**:
  - the `time` subparser: the five flags and `--resume`;
  - a top-level `--selftest`, `--build-schedules` or `--out` beside `time` refused in m's form;
  - `id`, `qual` and `campaign` still refused (`REFUSED_CMDS`).

## 4. Differences from m's forms

- **The identity's keys are mf3's:** `m_module_sha256`, `weights_revision`, `weights_sha256` and `reasoning_cap`.
  Two of them (the m files and the weights) are read from the lock's text, as routed, where m takes every value but
  the committed blobs' as a flag.
- **The lock** is `LOCK-m-F3.md`. The unit is Q-F3 only, so there is no `--unit` flag, and there are no ruling files
  (the campaign's in m) and no prior adjudication (an OLMo qualification's in m).
- **`DRIVER_REL`** is the driver's pre-existing constant `"scripts/mf3_sessions.py"`. `driver_problems` checks that
  the running file is that one (the round-1 review's MINOR-2). m derives the same value from `__file__`.
- **The snapshot's revision against the lock's** is refused at `time`. In m it is refused at qual and campaign (m's
  REVISION_STAGES).
- **The self-test** ports m's cases for its `time` path under mf3's names (§6). Not ported: m's OLMo branches; its
  stdout scans for menu fragments and pick lines (pre-existing scope); the cases of its other stages.

## 5. The PIN register (Code's; each declared at LOCK-m-F3 v0.2, as m's step-10 PINs were at LOCK v0.2)

The nine sites at the final bytes (`890084e6…90af`), each opening `PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; …)`. LOCK-m-F3 v0.2 declares them with the driver's blob, as the seat's G-TIME-F0 read (Q3) had v0.2 declare m's step-10 sites.

| site | subject |
|---|---|
| `scripts/mf3_sessions.py:72` | WIRED_CMDS / REFUSED_CMDS: `time` wired under F-1's clearance; the DRIVER-line record (step-10 Q2) |
| `scripts/mf3_sessions.py:81` | TIME_LOCK_FILE, TIME_FLAGS, TIME_COUNTS, TIME_LOCKED_PATH, TIME_REASONING_CAP (m's TIME_* form) |
| `scripts/mf3_sessions.py:98` | QWEN_MODEL_ID and MLX_LM_ALLOW_PATTERNS (m's), checked against their sources |
| `scripts/mf3_sessions.py:108` | TOTALS_RX, redact_totals, _say: REFUSED and STOP lines redacted, to stderr (m's) |
| `scripts/mf3_sessions.py:221` | time_identity_extra: committed blobs; the lock names the proposal; m files and weights from the lock's text |
| `scripts/mf3_sessions.py:284` | time_precheck: m's stage_precheck for "time" |
| `scripts/mf3_sessions.py:334` | driver_problems: the running file the driver of record, committed; the DRIVER line's value |
| `scripts/mf3_sessions.py:359` | qwen_snapshot: m's checks, built at `time` (the routing's "Build at time"; F-2's dated note) |
| `scripts/mf3_sessions.py:442` | run_time: m's _run_stage Qwen path; the snapshot revision against the lock's (REVISION_STAGES at time) |

## 6. The self-test

`python scripts/mf3_sessions.py --selftest` on the final bytes, in a worktree at `1e79955`: **160/160** (136 before
the wiring). The module self-tests are unchanged, at 124 checks. The driver's own checks go from 12 to 36: one is
changed (the refused-stages check now covers `id`, `qual` and `campaign`, with `time` wired), and 24 are new.

**The 24 new checks, grouped:**
- **The identity:**
  - the identity from the committed lock;
  - the values read from the lock's text, with a planted lock;
  - the identity licensed now;
  - the lock parsers.
- **The constants and the help:**
  - the constants against their sources;
  - `time --help`.
- **The snapshot check:**
  - 19 fake-cache cases;
  - MLXLM_USE_MODELSCOPE in four letter cases;
  - the hub's own offline resolution;
  - the production defaults;
  - the default working directory and the weight names.
- **The stub path:**
  - six sessions, PASS;
  - an ended checkpoint, refused;
  - `--resume` through the stage;
  - the exit code;
  - an end pending.
- **The Qwen path, under the traps:**
  - 35 refused cases;
  - m's multi case;
  - the out-root seam;
  - the reach-load case;
  - absolute paths, an open checkpoint with `--resume`, and an end pending;
  - the post-load STOPs with their evidence, and the order snapshot, load, re-read;
  - `driver_problems` on this driver;
  - the final trap count: the loader 4 times, the stage once, no escape, `data/mf3` unchanged.

**Safety.** No case can load the model, run a session on it, or write `data/mf3`. Where each trap applies:
- the cases that can reach the Qwen branch (`time_q`):
  - `_load_qwen` a trap, or in the post-load cases a stand-in returning an object with a model_id;
  - `stages.run_gate_stage` a trap;
  - `stages.DEFAULT_OUT` a test root and m:267's checklist stubbed;
  - `build_schedules` and `run_selftest` trapped;
- the out-root seam call: the loader and the stage trapped, and `DEFAULT_OUT` a test root. It refuses before the
  identity;
- the stub-factory runs (`stub_run`): sessions run on the stub through the real stage, with the loader trapped and
  `DEFAULT_OUT` a test root. They cannot reach the Qwen branch or `main`;
- the constants check: it calls the real `_load_qwen` with `qwen_or_explain` answering, `get_adapter` refusing, and
  the imports of mlx, mlx_lm and jlens_qwen failing, which closes every Qwen route;
- the fake-cache section: the hub held offline by its own constant.

## 7. Records left as they are (declared)

- G-SHAPE-F3's artifact records the driver's pre-edit blob `fad31c20…0cbb` in its sources map. F-1 clears the re-run.
- LOCK-m-F3 v0.1 §9's F57 row ("what is wired (selftest, schedules, hashes, gshape) and refused (the four stages)") and
  its line "F57's … site, `scripts/mf3_sessions.py`, carries no PIN line" are true of v0.1's tree. The wiring adds
  nine PIN sites, declared at v0.2, and v0.2 records them with the driver's blob.
- `valence_core/mf3/stages.py`'s module docstring still says that no stage is wired in the driver at the build. It is
  left alone, because editing it would move mf3's package.
- Pre-existing drift from m, outside the wiring:
  - refused `id`, `qual`, `campaign` and "no action" print to stdout;
  - `--selftest id` and `--build-schedules qual` run where m refuses them;
  - m's menu-fragment and pick-line stdout scans are not carried.
