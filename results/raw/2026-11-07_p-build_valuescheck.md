# p package — BUILD: the blind values-check, passes 1–3 (Code's raw, 2026-11-07)

*Three blind values-check agents, read-only on the repository: passes 1 and 2 checked every factual claim of the BUILD entry's draft and the design raw's §3–§6 against its source by tool; pass 3 checked the complete texts (the design raw's §1–§2 and §7 included) and the sentences changed after pass 2. Code's dispositions come first; the reports follow verbatim. Local paths scrubbed: the repository's prefix as <repo>, temp and scratch roots as <tmp>.*

## 0. Code's dispositions (each item re-checked at source before it was applied or disclosed)

### Pass 1 (118 items: 98 CONFIRMED, 15 IMPRECISE, 3 FAIL, 2 NOT CHECKABLE), on the first drafts

| item | verdict | disposition |
|---|---|---|
| A20 | IMPRECISE | Applied: the entry's gcal bullet separates m's pieces by import from p's own precheck and loop, and says m's `run_completability` is not called (PIN P21, FLAG F-p7, both new). |
| A26 | IMPRECISE | Applied: the refusal order stated as it is (and corrected again at pass 2, A28). |
| A34 | IMPRECISE | Applied: entry (4)'s reason is that `run_completability` is not called. |
| A42 | IMPRECISE | Applied: F-p1's borderline `do` record (the entry's summary completed at pass 2, A45). |
| A46 | FAIL | Applied: F-p5 rewritten -- the hygiene commit (`993eba1`) has landed; `gcal.py`'s sha256 and m's package hash given before and after. |
| A50 | IMPRECISE | Applied: the drivers' placement is §8's list; §6.2 gives the reason. |
| B3 | IMPRECISE | Applied: restoration is in a `finally` (an exception included) and asserted after a normal exit. |
| B4 | IMPRECISE | Applied: the table's columns now separate what `hashes` prints from Code's self-test note (completed at pass 2). |
| B8 | IMPRECISE | Applied, as A34. |
| B15 | IMPRECISE | Applied: `schedule.py:512` (the docstring and the error message in the code too). |
| B18 | FAIL | Applied: `olmo_hf.py:286` (the proxy's docstring too). |
| B25 | IMPRECISE | Applied: P7 says the stage, procedure and on_fail strings are Code's extension of ans2 Q4 (ii). |
| B33 | IMPRECISE | Applied: P12's analyzer field holds `scripts/m_analyze.py`'s sha16. |
| B35 | IMPRECISE | Applied: m's model-free builder is `model_free_artifact`, `_renders_of_record` its renders step. |
| B49 | IMPRECISE | Applied: F-p1's borderline record. |
| B50 | IMPRECISE | Applied: `Ther qro abov two dsys in a wemk` named beside `Janbaa` and `Janyooar`. |
| B57 | IMPRECISE | Applied: the six modules beyond mf3's ten, `runner_olmo.py` included. |
| B59 | FAIL | Applied, as A46. |
| (2) | NOT CHECKABLE | The design raw's §1–§2 (generated at the commit from the committed bytes) and the coordinating session's scope message (chat; quoted in both texts). |

### Pass 2 (136 items: 117 CONFIRMED, 14 IMPRECISE, 0 FAIL, 5 NOT CHECKABLE), after review round 2

| item | verdict | disposition |
|---|---|---|
| A12 | IMPRECISE | Applied: the replacement is declared by qualified name and enforced by identity; a stand-in carrying the name is refused. |
| A22 | IMPRECISE | Applied: every STOP of the generation loop is recorded, bar a failure of the checkpoint's own write. |
| A28 | IMPRECISE | Applied: p's refusals that need no adapter precede the load; m's startup, with two model-free asserts of m's own, follows it. The same in gcal.py's ORDER docstring. |
| A45 | IMPRECISE | Applied: the entry's F-p1 names the borderline `do`. |
| A52 | IMPRECISE | Applied: F-p8 quotes ans2 Q1 (iii) and states the analyzer scope as Code's reading, the seat's question. |
| A59 | IMPRECISE | Applied: the PI's item 3 accepts route (b); its build sequence names no analyzer. |
| B4 | IMPRECISE | Applied: a separate column for Code's self-test note. |
| B10 | IMPRECISE | Applied: §3 names the import forms the static check follows and those it does not (guard.py's docstring lists them); none occurs in p's code. |
| B18 | IMPRECISE | Applied: P4 -- the six key templates are the only differing bytes among the eighteen files; m's `verify_schedule_dir` over p's directory would also report the manifest and m's Q-F0 files. The schedule docstring too. |
| B30 | IMPRECISE | Applied: P10 names the checkpoint write's own failure, the STOP that cannot be recorded. |
| B35 | IMPRECISE | Applied: P13 -- the number of changed positions per item. |
| B46 | IMPRECISE | Applied: P21 -- the call sits in the loop both substrates share (`gcal.py:1155`, `:1164`); the OLMo branch binds `temp, cap` (`:1104`). |
| B48 | IMPRECISE | Applied: P21 -- the record's keys in full and six of its ten values. |
| B68 | IMPRECISE | Applied, as A52. |
| (5) | NOT CHECKABLE | As pass 1's two (the design raw's §1–§2 and the scope message, each counted in both texts). |
| C (code notes) | -- | Applied: report.py's F-p1 text, gcal.py's committed-check PIN and ORDER sentence, schedule.py's docstring and its self-test label. |

### Pass 3 (57 items: 52 CONFIRMED, 5 IMPRECISE, 0 FAIL, 0 NOT CHECKABLE), on the complete texts

| item | verdict | disposition |
|---|---|---|
| §7 count claim | IMPRECISE | Applied: §7 states what the self-test's count does not depend on (the pod id, the canonical roots, CLAUDE.md, `data/p/schedules`) and discloses what it does depend on by design (its inputs of record, read from their committed blobs). |
| §7 MAJOR/MINOR claim | IMPRECISE | Applied: fixed, declared (m10) or disclosed (m3; R3-1's second half). |
| the entry's checks bullet | IMPRECISE | Applied, as above. |
| T12 (§3) | IMPRECISE | Applied: §3 names every form guard.py's docstring says it does not follow, and says no write through any of them occurs except the register's own (`register.substituted` receives m's module as its argument by design). |
| F-p10 | IMPRECISE | Applied: a ProxyStop's stop field keeps the returned text whole too, and the alternative covers both. |
| notes | -- | Applied: "three passes" in §7, the entry and this raw's title; the review raw's R3-1 row; the code docstrings that said "under data/" (gcal.py, gshape.py, schedule.py, p_sessions.py) now say "inside the repository"; p_sessions.py's order adds the pre-load identity comparison; gcal.py's `committed_problems` docstring names m's whole package. These docstring edits came after pass 3 and before the site check of record, which ran on the final bytes. |

## 1. Pass 1 (the agent's report, verbatim)

# p package — BUILD: blind values-check, round 1 (2026-11-07)

Texts checked (read-only):
- **A** = `podwatch/build_entry.md` (the RESULTS.md entry draft; 66 lines, sha256 `d6e719c7…2588`, the 14:22 version with the "Scope, by §8's step numbers" bullet).
- **B** = `podwatch/p_build_design_body.md` (design raw §3–§6; 136 lines, sha256 `143d2ce5…2a57`).

Placeholders (`@@PKG@@`, `@@MANIFEST@@`, `@@SELFTEST@@`, `@@CHECKS@@`, `@@STAMP@@`, `@@OLMOHF@@`) are not checked.

Method: every number, file name, file:line anchor, quote, attribution and inclusive claim was checked against its source with a tool. The commands were:
- `jlens-qwen36/.venv/bin/python -B scripts/p_sessions.py --selftest`, `… hashes`, and `… gshape --out <scratch>/vc_r1/gshape_out`;
- `-B` / `-I -B` Python snippets: the fresh-interpreter import set; the 18 schedule files compared with m's; the counters recomputed on the three G-CAL-OLMo artifacts read from `git show HEAD:`; G-SHAPE-F0's placement keys read from `git show <rev>:`;
- `git show`, `git diff`, `git check-ignore`, `/usr/bin/grep -n`, `sed -n`/`awk` line prints.

No repository file was written. Outputs: `<scratch>/vc_r1/{selftest.txt,hashes.txt,gshape.txt,gshape_out/}`.

## 0. State of the tree during the check (read this first)

- **HEAD moved during the check.** It is now `993eba1` (2026-11-07 14:23:57 −0500), the coordinating session's G-ANL-F3 hygiene commit, one commit above `18b0111`. That commit edits `valence_core/m/gcal.py` (sha256 `d60b78e5…02fe` → `fbae9a01…f6ef`; the edit sits in `_selftest`, near :2393), `scripts/m_sessions.py` and `scripts/mf3_sessions.py`. m's `package_sha256` moves `60199b36…` → `7756dcf4…`. Both drafts predate it (14:19 and 14:22). This is behind A46/B59's FAIL.
- **A parallel session is re-running G-SHAPE-F0 and G-SHAPE-F3.**
  - The index holds staged renames: `data/m/gates/G-SHAPE-F0.json → …superseded-2026-11-07.json` and `data/mf3/gates/G-SHAPE-F3.json → …superseded-2026-11-07.json`.
  - A new untracked `data/m/gates/G-SHAPE-F0.json` is present.
  - So `m_stages._committed("data/m/gates/G-SHAPE-F0.json")` refuses: "working-tree bytes are not HEAD's blob".
  - Consequences: (i) p's self-test ran **88/89**, one FAIL: "gshape-p: each unit's placement keys equal G-SHAPE-F0's committed artifact's". (ii) My G-SHAPE-p trial printed no placement-key line.
  - Both are transient. A39 checks the claim directly against the blobs.
  - The BUILD must be committed by path, so that the staged renames do not go into it.
- The self-test has **89 checks**: register 6, corrupt 12, keys 7, schedule 8, proxy 7, report 7, guard 5, gcal 15, gshape-p 10, p_sessions 12. Any "88/88" figure would be out of date.
- **Update at the end of the check.** HEAD moved again, to `f9700ba` (G-SHAPE-F3's re-run) on `0786c11` (G-SHAPE-F0's re-run), and the index holds no staged renames any more. Re-run there:
  - the p self-test is **89/89**, exit 0 (`<scratch>/vc_r1/selftest2.txt`);
  - the `gshape --out` trial PASSes and prints "placement keys vs G-SHAPE-F0's committed artifact: OLMo-sft equal; OLMo-dpo equal; OLMo-instruct equal";
  - m's package is still `7756dcf4…`.

  The transient FAIL is gone. Both drafts were unchanged from start to end (sha256 prefixes `d6e719c7cb553281` and `143d2ce5122e4889`).

## A. The BUILD entry (build_entry.md; l. = draft line)

A1 (l.1) Entry name "p package — BUILD", "p §8 step 4". **CONFIRMED.** p v0.2:127 (step 4 "`p package — BUILD`"); :132 (the entries list).

A2 (l.1–2) `valence_core/p/` has 11 files; driver `scripts/p_sessions.py`. **CONFIRMED.**
- `ls`: `__init__`, corrupt, gcal, gshape, guard, keys, proxy, register, report, schedule, testing.
- `hashes` prints "(11 files, valence_core/p/*.py)".

A3 (l.2) "on PROPOSAL-p v0.2 (`18b0111`)". **CONFIRMED.**
- `git log`: 18b0111 commits v0.2.
- The file's sha256 is `42f2977b…3b32`, which equals `gcal.PROPOSAL_P_SHA256` (gcal.py:71).

A4 (l.2–3) "the design seat's answers of 2026-11-07 (Q0–Q4)". **CONFIRMED.** ans2:1–3, §1–§5.

A5 (l.3) The PI's quote "Then build → G-SHAPE-p → G-CAL-p on your go for the box". **CONFIRMED** byte for byte.
- `grep -F` finds it in RESULTS.md@18b0111 (×2) and @139635f.
- The draft omits only the source's final period.

A6 (l.3–4) "m's modules are imported unchanged". **CONFIRMED.**
- p's diff touches no m file.
- The self-test case "p edits no m file, olmo_hf.py, m_analyze.py or m_sessions.py — each committed at HEAD and unedited" PASSes.
- The term-(e) static check is clean.
- The m edit at 993eba1 is the coordinating session's, not p's.

A7 (l.4) "the one declared substitution form carries register entries (1) and (2)". **CONFIRMED.**
- register.py:51–71: (1) and (2) have status `BUILT`.
- `substituted` refuses (3) and (4) (:86–88; self-test).

A8 (l.5) "a G-SHAPE-p trial PASSes". **CONFIRMED.** My `gshape --out` run: exit 0, "G-SHAPE-p: PASS".

A9 (l.5–6) "Nothing is locked, nothing runs on a model or the box". **CONFIRMED.**
- No `LOCK-p*` file exists; `data/p/` holds only `schedules/`.
- Only `gcal` can load a model, and it refuses off the box: self-test "POD ID ABSENT"; p_sessions.py:149–153.

A10 (l.8–9, l.37) "the design raw … §1 lists every file with its sha256"; "verbatim in the design raw §2". **NOT CHECKABLE.** `results/raw/2026-11-07_p-build_design.md` does not exist yet, and §1–§2 are not in B.

A11 (l.10) `register`: "ans2 Q0's five terms; p §4.2's entries (1)–(4)". **CONFIRMED.**
- ans2:11 gives terms (a)–(e).
- p:86 gives entries (1)–(4).
- register.py:3–15, :55–71.

A12 (l.11–12) `corrupt`: `corr.corrupt_m` under entry (1) with `eligible_p` (p §1.1, §1.4); the renders of record; both sha conventions. **CONFIRMED.**
- corrupt.py:97–106, :32–51.
- p:31, :58.
- Self-test: "corrupt_p reproduces p §1.2's sixteen renders"; both identifications.

A13 (l.13–14) The six key families `p-sched|`, `p-olmo|`, `p-olmo-time|`, `p-olmo-qual|`, `p-olmo-items|`, `p-olmo-items-{gate}|`. **CONFIRMED.**
- keys.py:24.
- m keys.py:105–154 (the same six with `m-`).
- Self-test "the six families are p §4.1's".

A14 (l.14–15) m's builder under entry (2); `data/p/schedules/` holds eighteen files and their own manifest. **CONFIRMED.**
- 18 `*.json` plus `manifest.json`; the manifest lists 18 files.
- schedule.py:46–63 runs `build_schedule_objects` inside `keys.substituted_keys()`.
- Self-test "data/p/schedules equals a fresh regeneration byte for byte, manifest included (18 + 1)" PASSes.

A15 (l.15) "in m's schema names and layout (ans2 Q4 (iii))". **CONFIRMED.**
- Files are schema `m-schedule-v1`, with the same key set as m's files; the manifest is schema `m-schedules-manifest-v1`.
- `m_schedule.dumps_schedule` writes them.
- ans2:38.

A16 (l.15–16) "G-CAL-p's seeds stay `m-cal|…`". **CONFIRMED.**
- m gcal.py:556–569: `key_set` → `keys.cal_seed`, which is never substituted.
- keys self-test "G-CAL-p's seeds stay m-cal".

A17 (l.17–18) `proxy`: §2.2 reading (b), `StoredTextProxy` over the returned result, `olmo_hf.py` unedited. **CONFIRMED.**
- proxy.py:50–88.
- `git diff HEAD -- valence_core/adapters/olmo_hf.py` is empty; the last commit touching it is e26e9c9.

A18 (l.19) `report`: §2.3's five counters and the trigger's predicate. **CONFIRMED.**
- report.py:45 (`COUNTERS`, 5) and :48–50.
- p:68 lists the same five.

A19 (l.20–21) `guard`: package hash, licence sha256s, measured import set, term (e)'s static check, refused roots `data/m`, `data/mf3`, `/workspace/models`. **CONFIRMED.** guard.py:37, :50–71, :90–142, :78–87.

A20 (l.22–23) `gcal`: "m:176's procedure through m's `gcal` by import (key set, task, startup, grader and its honesty asserts, identity, gate line, condition (4), weights of record, write-once writer, the artifact's m fields)". **IMPRECISE.**
- Every listed piece is m's by import:
  - `key_set` :340, `_task_of` :366, `_startup_olmo` :334, `grade`/`normalize` :379/:257, `_grader_honesty` :337;
  - `_identity_olmo` :194, `gate_line` :184, `weights_of_record` :177, `_write_artifact` :413;
  - `completability_artifact` :296, which calls `condition_4`.
- But the procedure's precheck and its generation loop are p's own (p gcal.py:156–190, :322–391). They re-implement m's `run_completability` (m gcal.py:1088–1172) step for step:
  - `assert_insulated`; `assert_boundary`; `seg = f"Task: {task}\nResponse:"`;
  - `generate(SESSION_BANNER, seg, injections=(), seed=…, temp=m_ro.OLMO_TEMP, max_tokens=m_ro.STOP_CAP, ban_ids=…, cached=False)`;
  - the same record dict.
- m's `run_completability` is never called.
- p §3.1 (p:74) and ans2 Q3 (b) (ans2:31) say "the prompt, seeds, grader and generation call are m's `gcal`'s by import or by §4.2's register". The segment form and the generation call are instead written in p with m's constants. No PIN in B declares this (see B8).
- Proposed: "m:176's procedure in p's own precheck and loop, which mirror m's `run_completability` with m's generation arguments (`OLMO_TEMP`, `STOP_CAP`, `cached=False`, `injections=()`), m's `gcal` by import for the key set, task, startup, …". Consider a PIN or FLAG for the departure from p §3.1's "by import or by §4.2's register".

A21 (l.24) "p's own checkpoint (`p-gcal-checkpoint-v1`)". **CONFIRMED.** gcal.py:72.

A22 (l.24–26) The hair trigger and the artifact's `p` block: both renders conventions, the proxy's cuts, the clean-pool identity with G-CAL-OLMo's committed artifacts, the strict grade, the counters, the covariates beside, the licence values at the run, the disclosure. **CONFIRMED.** gcal.py:381–386 (trigger), :300–318 (block).

A23 (l.27–29) `gshape`: G-SHAPE-F0's layers by import (`grid`, `template_shape_problems`, `runner_scope_problems`, `_stop_reasons` minus `coverage:Q-F0`); p's renders read from the committed renders raw; three OLMo units; Layer P. **CONFIRMED.**
- gshape.py:311–318, :297, :228–234, :78.
- The renders raw's sha256 `25bd3d01…b895` equals `RENDERS_RAW_SHA256` (:80).

A24 (l.30–31) `testing`: `CharScriptedAdapter`, a character tokenizer whose decode inverts on every prefix; imported by self-tests only. **CONFIRMED.**
- testing.py:17–29: ids are code point + 1.
- Imported only inside `_selftest` (proxy.py:92, gcal.py:423).
- The static check finds no module-level test-double import.

A25 (l.32–34) Driver subcommands `--selftest`, `--build-schedules`, `hashes`, `gshape`, `gcal --unit OLMo-{ckpt} [--resume]`; `time`, `qual`, `campaign` refused (p §8 step 6). **CONFIRMED.**
- p_sessions.py:288–323, :65–67.
- Self-test: exit 2 for each, named.

A26 (l.33–34) gcal "(the box only: every refusal before the load, the DRIVER and WEIGHTS lines, the OLMo adapter through the proxy)". **IMPRECISE** on "every refusal before the load".
- Before the load (p_sessions.py:149–158): the precheck and the weights-files check.
- After `adapter_factory()` (gcal.py:329–353), before any generation:
  - the stub-mismatch refusal;
  - m's `_startup_olmo` refusals: insulation, base/cross-checkpoint, ban list, weights path, tokenizer probe;
  - the grader-honesty assert;
  - the provenance refusal;
  - the checkpoint/identity refusals (`load_or_init`);
  - POD CHANGED.
- The DRIVER and WEIGHTS lines (:159–164) and the proxy (gcal.py:329) are as stated.
- Proposed: "every refusal that can run without the model before the load (the precheck, the weights files), the startup and checkpoint refusals before the first generation".

A27 (l.35–36) `.gitignore` admits `data/p/{schedules,gates,reports,ckpt,verdicts}/*.json`; `.gitattributes` marks `data/p/ckpt/**` `-diff` (m:318 by reference). **CONFIRMED.**
- `git diff` of both files.
- `git check-ignore -v` admits a `*.json` under each of the five roots and keeps `*.tmp` and other files out.
- m:318 is "**Blinding.**"

A28 (l.37) "The licence (p §4.2, C2's form; `scripts/p_sessions.py hashes`…)". **CONFIRMED.**
- p:86: "Licence (C2's form): LOCK-p v0.1 names p's `package_sha256`, the file sha256 of each imported `valence_core.m` module and of `valence_core/adapters/olmo_hf.py`, each by name on one lock line, and the register".
- `hashes` prints exactly these.

A29 (l.38) `package_sha256` over 11 files. **CONFIRMED.** `hashes`: "(11 files, valence_core/p/*.py)", computed by m's `resume.package_sha256_of` (guard.py:50–51).

A30 (l.38–39) "the seventeen m files p imports (sixteen modules, measured in a fresh interpreter, and `__init__.py`) and … `olmo_hf.py`, each by name on one line". **CONFIRMED.**
- My `-I -B` import of the nine production modules loads exactly sixteen m modules: audit, banner, bars, corr, gcal, gshape, guard, keys, readrule, resume, runner_olmo, runner_qwen, scaffold, schedule, stages, verify.
- Importing the driver gives the same sixteen.
- `hashes` prints 17 `LICENCE valence_core/m/…` lines and one `olmo_hf.py` line.

A31 (l.40–41) "Nothing in `valence_core/m/`, `scripts/m_sessions.py`, `scripts/m_analyze.py`, `olmo_hf.py`, `data/m/` or `data/mf3/` changes." **CONFIRMED** for the BUILD's own files (`valence_core/p/*`, `scripts/p_sessions.py`, `data/p/schedules/*`, `.gitignore`, `.gitattributes`). NOTE: see §0; commit by path.

A32 (l.42–43) "(1) `corr._eligible_m` → `eligible_p`, built; (2) `valence_core.m.keys`' four key functions → p's, built". **CONFIRMED.**
- register.py:56–61.
- p:86 and ans2:11 phrase (2) as "six OLMo key families"; the build realizes them through the four functions.

A33 (l.43–45) "(3) `scripts/m_analyze.py` through `scripts/p_analyze.py` (the OLMo Clock → D_p, the `data/m/…` roots → `data/p/…`, the v2 verdicts-dir resolution), declared, built at step 6". **CONFIRMED.** register.py:62–67; ans2:11; p:86.

A34 (l.45–46) "(4) `gcal`'s renders source, declared and not exercised (G-CAL-p passes p's renders as `_task_of`'s argument)". **IMPRECISE.**
- The parenthesis is true (p gcal.py:366; m gcal.py:893 `_task_of(key, pool, renders)`), but it is not the reason (4) goes unexercised.
- m's own loop also passes renders to `_task_of` as an argument (m gcal.py:1154, from m's precheck).
- Entry (4) is unexercised because p never calls m's `run_completability`/`precheck` (A20).
- Proposed: "(4) … declared and not exercised: G-CAL-p does not call m's `run_completability`; p's own loop passes p's renders to m's `_task_of(key, pool, renders)` as an argument, so no `gcal` attribute changes".

A35 (l.46–48) Term (c)'s equality cases and restoration. **CONFIRMED.**
- `corrupt_p` equals m's renders on items 0 and 12, exactly those (corrupt.py:173–174).
- With m's keys substituted back, p's builder reproduces `data/m/schedules/`' eighteen OLMo files byte for byte (schedule.py:118–123; `data/m/schedules` holds 18 `OLMo-*` files).
- Restoration after each call, an exception included: self-test cases in register, corrupt and keys. All PASS.

A36 (l.48) "No other site exists (term (e)'s static check is clean)." **CONFIRMED** (with a note).
- `guard.substitution_problems()` returns `[]` over the ten production files (`testing.py` excluded).
- The check does not scan `scripts/p_sessions.py`; run on the driver explicitly, it also returns `[]`.
- The driver has no `setattr`, no m-attribute assignment and no `classify`.

A37 (l.49) The trial: "PASS — 2,816 placements per OLMo unit, 8,448 in all, none fired or misplaced". **CONFIRMED.** My trial: 2816/0/0 for each unit; total 8448.

A38 (l.50) "`seg+gold` fires on every placement; the three grids identical; no shape, Layer S or Layer P problem". **CONFIRMED.**
- seg+gold 2816/2816 per unit.
- "OLMo grids identical: True".
- Shape 0, Layer S 0, Layer P 0.

A39 (l.50–51) "each unit's placement keys equal G-SHAPE-F0's committed artifact's". **CONFIRMED** against the blobs.
- `placements_sha256` equal for all three units against `git show HEAD:` (= 18b0111 = 139635f): sft `be6ddba6…`, dpo `2fec663f…`, instruct `f7f90e86…`.
- Also equal against the parallel session's new, untracked G-SHAPE-F0.json.
- At first the trial could not read the committed artifact (`readable: False`) and the self-test's case FAILed (§0). After the parallel session committed its re-run (`0786c11`), the trial prints "equal" for all three units and the self-test is 89/89.

A40 (l.52) "twenty PINs (P1–P20)". **CONFIRMED.** B §4 has P1–P20, contiguous.

A41 (l.53) "Six FLAGs, none blocking". **CONFIRMED.** B §5 has F-p1–F-p6; its heading reads "none blocks G-SHAPE-p, and none decides G-CAL-p".

A42 (l.53–54) F-p1: "counts 23 of G-CAL-OLMo's 384 records, 17 of them only for a common word within distance 2 of a short gold (`the`/`two`)". **IMPRECISE** (borderline; the figures are exact). It carries B49's point: one of the 17 counts the model's own answer `'do'`.

A43 (l.54–55) F-p2: "one gate schedule draws m's π by coincidence". **CONFIRMED.** See B52–B54.

A44 (l.55) F-p3: "§5.4's date (referent item 85) in the artifacts' disclosure". **CONFIRMED.** See B55.

A45 (l.55–56) F-p4: "register entries (3) and (4)". **CONFIRMED.**

A46 (l.56) F-p5: "the licence moves with m's `gcal.py` when the hygiene commit lands". **FAIL (stale).**
- The hygiene commit has landed: 993eba1, HEAD at this check.
- It moved `valence_core/m/gcal.py` from `d60b78e5…` to `fbae9a01…`; `hashes` already prints `fbae9a01…`.
- Proposed: "F-p5, the licence carries m's `gcal.py` as the hygiene commit `993eba1` left it (`fbae9a01…`); LOCK-p v0.1 names the values current at its writing".

A47 (l.56–57) F-p6: "the departure disclosed at `18b0111`". **CONFIRMED.** RESULTS.md@18b0111:105–107 ("A departure, disclosed (Code's)").

A48 (l.58) "This BUILD is step 4's list." **CONFIRMED.**
- p:127 lists `valence_core/p/`, `scripts/p_sessions.py`, the corruptor, the adapter proxy, p's keys and schedules, the G-CAL-p and G-SHAPE-p tooling and the reporting tool.
- All are built and nothing else is.

A49 (l.58–60) `scripts/p_analyze.py`, G-ANL-p and entry (3)'s self-test are step 6's, "before any LOCK-p v0.1 and after LOCK-m-F3 v0.1 (p §4.3)", and "no p analyzer is built if every checkpoint fails G-CAL-p (p §4.4)". **CONFIRMED.**
- p:129 (step 6 "before any LOCK-p v0.1; after LOCK-m-F3 v0.1, §4.3"); p:88; p:90.
- Entry (3)'s self-test as step 6's is a fair reading of p:86 (c) with p:90 (G-ANL-p's "register's equality and restoration cases").

A50 (l.60–61) "The gate-stage and campaign drivers are step 6's too (p §6.2)." **IMPRECISE** (attribution).
- p §6.2 (p:110) gives the pod order and the reason (G-CAL-p "decides whether anything else of p is built"), but no step.
- The placement comes from §8 and §4.2:
  - step 4's list (p:127) names no stage driver;
  - p §4.2 (p:86) lists "the stage drivers" among p's code;
  - step 6 (p:129) runs G-TIME, G-F0m and the campaign.
- Proposed: "(p §8: step 4's list names no stage driver; p §6.2: G-CAL-p 'decides whether anything else of p is built')".

A51 (l.61–62) "The coordinating session confirmed this scope on 2026-11-07: its brief had listed `scripts/p_analyze.py` in the BUILD". **NOT CHECKABLE.** Chat only, not in the repository.

A52 (l.62–63) "the PI's item 3 (…) names no analyzer". **CONFIRMED.** The quoted item 3 (RESULTS.md@18b0111) names no analyzer.

A53 (l.65–66) "G-SHAPE-p's run of record … in its own commit. G-CAL-p waits for the coordinating session's go for the box." **CONFIRMED.**
- p:132 lists `G-SHAPE-p` as its own entry.
- RESULTS.md@139635f's close line: "on the coordinating session's go for the box".

## B. The design raw §3–§6 (p_build_design_body.md; l. = draft line)

### §3 The substitution register

B1 (l.3–4) The form: "an attribute of an m module replaced for the duration of one call and restored in a `finally`" (`register.py`, `substituted`), under the seat's five terms (a)–(e). **CONFIRMED.** Verbatim p:86; register.py:82–105; ans2:11.

B2 (l.4–6) `substituted` refuses an unknown or not-built entry, a module or attribute set other than the entry's, and a kind outside eligibility / keys / pins / Clock / roots. **CONFIRMED.**
- register.py:86–93; `KINDS` is :29.
- Self-test: "entries (3) and (4), an unknown entry, an undeclared attribute and a wrong module are each a STOP".

B3 (l.6–7) "it asserts the single thread at the site, and restoration after the call, an exception included". **IMPRECISE (minor).**
- The single-thread assert is :94.
- Restoration happens in the `finally` on both paths (:100–102).
- But `substituted`'s own check of it (:103–105) runs only on a normal exit. When the block raises, the exception propagates out of the `finally` and :103 is not reached.
- Restoration after an exception is asserted by the self-tests (register, corrupt, keys), not inside `substituted`.
- Proposed: "…asserts the single thread at the site, restores in a `finally` (an exception included) and checks the restoration on a normal exit; the self-tests assert it after an exception".

B4 (l.7) "The four entries, as `scripts/p_sessions.py hashes` prints them (§2)". **IMPRECISE (minor).**
- The table paraphrases the four printed `REGISTER` lines.
- (3)'s kind prints `clock`; the table says "Clock (and roots)".
- The printed status of (1) and (2) is "built at the p BUILD (p §8 step 4)", without the self-test descriptions the table adds.
- "(§2)" points into the unwritten design raw (NOT CHECKABLE).
- Proposed: "The four entries (`hashes` prints them verbatim, §2), with each built entry's self-test:".

B5 (row 1) `valence_core.m.corr` | `_eligible_m` | `valence_core.p.corrupt.eligible_p` | eligibility | built, with its self-test. **CONFIRMED.** `REGISTER` n=1; self-test lines "corrupt_p reproduces…", "items 0 and 12…", "restoration…", "after an exception…".

B6 (row 2) `valence_core.m.keys` | `item_key`, `arm_key`, `sched_key`, `gate_sched_key` | "`valence_core.p.keys`' four" | keys | built; the "eighteen OLMo files byte for byte" self-test; restoration with an exception. **CONFIRMED.**
- `REGISTER` n=2.
- schedule.py:120–123.
- keys.py:107–113 (the exception case).

B7 (row 3) The three attributes, the replacement "D_p; `data/p/…`; `data/p/verdicts` for the OLMo coordinates", and the status "declared; built with `scripts/p_analyze.py` at p §8 step 6". **CONFIRMED.** register.py:62–67. The kind cell is covered in B4.

B8 (row 4) "declared; not exercised: G-CAL-p passes p's renders as the argument of m's `_task_of(key, pool, renders)`, so no m attribute changes". **IMPRECISE.**
- The signature matches m gcal.py:893, and the gcal self-test asserts `vars(m_gcal)` unchanged (p gcal.py:533–534).
- The reason given is incomplete, as in A34: (4) is unexercised because p does not call m's `run_completability`; it runs its own loop (A20).
- No PIN in §4 declares the own loop or the generation call it writes with m's constants.

B9 (l.16–18) "No other site exists: `guard.substitution_problems` … finds no assignment to an attribute of an imported m module, no `setattr` outside `register.py`, no test double imported at module level and no `classify` call in any p production module." **CONFIRMED.**
- The function returns `[]`; it scans 10 production files (guard.py:74–75, :110–132).
- Its `classify` probe catches attribute calls only (:130), but `grep` finds no `classify` call at all.
- `proxy.py`'s `object.__setattr__` sets the proxy's own attributes, not an m module's.

### §4 PINs

B10 P1: "the calling thread is the main thread and no other Python thread is alive (`threading.active_count() == 1`). Every site of record runs before any model load." **CONFIRMED.**
- register.py:75–79.
- The sites are `corrupt_p` (renders_problems ← gcal precheck at gcal.py:174, before `adapter_factory()` at :329; gshape.py:235) and `substituted_keys` (schedule builder; no model).

B11 P2: the quote rule is m's; each `'` toggles; an odd count is refused "as `_eligible_m` refuses it". **CONFIRMED.** corrupt.py:72–79; m corr.py:192–197.

B12 P2: "its first word" is the first maximal ASCII-letter run, a frame word unless quoted ("no CORR item's does"). **CONFIRMED.**
- corrupt.py:75–87.
- The self-test's `SPEC_FRAME` equality holds; every item begins with an unquoted verb.

B13 P2: case-insensitive (v0.2 §1.1's words), inert on the pool of record, referent item 131. **CONFIRMED.** corrupt.py:85; p:31; referent-check.md:364–368.

B14 P3: each p key is m's key with the leading `m-` replaced by `p-`; units outside the three OLMo units pass through; m's builder iterates every built unit. **CONFIRMED.**
- keys.py:33–56.
- m keys.py:19 (`UNITS_BUILT`).
- Self-test: 45 keys, Q-F0 passes through.

B15 P4: the literal `m-sched|{unit}|{arm}|{b}` "(`valence_core/m/schedule.py:511`)". **IMPRECISE** (anchor off by one).
- The literal is on **:512**: `"key_template": f"m-sched|{unit}|{arm}|{{b}}", …`.
- :511 is the `return {"schema": SCHEMA, …` line that opens the dict.
- The file is unchanged since 5f7b968, so this holds at 18b0111 and at HEAD.
- Proposed: "schedule.py:512".
- The same anchor is in `valence_core/p/schedule.py:9` and in the `ScheduleStop` message at :59.

B16 P4 (rest): "Under entry (2) the cells are drawn from `p-sched|…`; p sets that one field after m's call, inside the substitution, to the active `sched_key`'s template form (asserted to be m's literal before the change)… no cell, π or key is touched." **CONFIRMED.**
- m schedule.py:230: the campaign permutation comes from `keys.sched_key`.
- p schedule.py:50–60.
- Self-tests: the term (c) byte equality; "every key template … is p's".

B17 P5: "line break" means `\n` or `\r`, and §2.3's trigger reads both. **CONFIRMED.** proxy.py:28; p:68 ("containing `\n` or `\r`").

B18 P5: "as the adapter strips its decoded text (`olmo_hf.py:284`)". **FAIL** (anchor).
- olmo_hf.py:284 is a blank line.
- The strip is `text=self.decode(gen).strip(), token_ids=gen,` at **:286**, inside `return GenerateResult(` at :285–288. The file is unchanged since e26e9c9.
- m's testing.py:15 and the pre-read (`results/raw/2026-11-06_p_code-to-design_preread.md`:96, "`.strip()` (`:286`)") both cite :286.
- Proposed: "olmo_hf.py:286".
- The same wrong anchor is twice in `valence_core/p/proxy.py` (:12, :21).

B19 P5: the cut text is the text before the first break with trailing whitespace removed; the ids run through the first prefix whose decode holds a break after content; a no-break result is the adapter's own object; an unplaceable break is a STOP. **CONFIRMED.**
- proxy.py:52–63: `return g, None` (:53–54); `.rstrip()` (:60); `ProxyStop` (:57–59).
- Proxy self-test, including the word-hash STOP case.

B20 P6: control characters are Unicode Cc minus `\n` and `\r`, tab included. **CONFIRMED.** report.py:53–54.

B21 P6: "m:258's eight declared strings (placeholders as wildcards) match at the start of the first line, case as written; `=== … ===` is a whole first line". **CONFIRMED.**
- `banner.DECLARED_HARNESS_STRINGS` has 8 entries; m:258 says "with the two reasoning-block lines, eight declared harness strings".
- report.py:38–42 and :57–60 use `startswith` / `re.match` with no IGNORECASE, and `fullmatch` on the stripped first line.
- The placeholders `{L_clean}`, `{L_corr}`, `{L_a}`, `{L_b}`, `{n}` become `.+?`.

B22 P6: refusals match case-insensitively, straight or curly apostrophe. **CONFIRMED.** report.py:43.

B23 P6: `corrupted_spelling` as written, with one reading (a word is §1.1's; a gold variant is compared only when it is itself one such word). **CONFIRMED.**
- report.py:77–80.
- NOTE: the reading is material. With digit golds compared too, the same 384 records count 23/25/26 = 74, not 23.

B24 P7: `proposal_sha256` is p's; `renders_sha256` is p's renders by m's convention (ans2 Q3 (c)); `package_sha256` is m's package. p adds `proposal`, `proposal_p_sha256`, `p_stage`, `p_package_sha256`, `renders_sha256_p`, `proxy`. **CONFIRMED.** gcal.py:193–200; m gcal.py:849–856 (`_resume.package_sha256()`); ans2:32.

B25 P7: "m's strings stay as m writes them (`stage` "G-CAL-OLMo", the artifact's `procedure` and `on_fail`; ans2 Q4 (ii))". **IMPRECISE** (citation).
- The strings themselves are as stated (m gcal.py:849, :999–1014).
- But ans2 Q4 (ii) (ans2:37) rules on m's *unit and template* strings (`OLMo-{ckpt}`, `A0-OLMo-{ckpt}`, `A0s-OLMo-{ckpt}`) and the `proposal` field. It says nothing on the stage string, `procedure` or `on_fail`.
- Proposed: "(Code's reading, by analogy with ans2 Q4 (ii)'s unit and template strings)".

B26 P7: p's stage name, procedure difference and failure consequence are in the `p` block, with `proposal_p_sha256` at the top level. **CONFIRMED.** gcal.py:299–316.

B27 P8: the quote "a hit iff the first word of the normalized text is a gold variant"; `twenty-four` → `twenty four`; leading words for a multi-word variant. **CONFIRMED.**
- The quote is verbatim at p:74.
- `normalize('twenty-four')` returns `'twenty four'` (m gcal.py:184–185).
- `strict_hit` is gcal.py:256–258; its self-test passes.

B28 P9: the fields seed, task, text, n_tok, cap_hit, stop_reason, hit; G-CAL-OLMo's artifact from its blob at HEAD; a refusal before any load; the path fields side by side; "the seat's flag (p §3.1), never a bar". **CONFIRMED.**
- gcal.py:76–79, :142–153, :174–176, :275–287.
- p:74: "a flag to the seat (adjudication), not a bar".

B29 P10: the trigger fires before the record is stored; the text goes to `stop` with its key; nothing is appended; the stage STOPs (exit 4); a stopped checkpoint is never resumed. **CONFIRMED.** gcal.py:381–386, :217–218; p_sessions.py:170–172; self-test.

B30 P11: the committed-at-HEAD requirement, refused before any load; `licence_at_run`; "G-CAL-p needs no lock (p §4.3)". **CONFIRMED.**
- gcal.py:130–139, :180–188, :290–292, :317.
- p:88: "G-CAL-p needs no lock".

B31 P12: the PROVENANCE line prints m's fields plus the pod id; the provenance entry carries the pod id "as m's does". **CONFIRMED.** gcal.py:356–360; m gcal.py:1137–1145 (m prints `{record, stamp}`; its OLMo entry carries `pod_id`).

B32 P12: the gate line is m's `gate_line` for stage `G-CAL-p-{ckpt}` on p's proposal. **CONFIRMED.** gcal.py:184, :105–106.

B33 P12: "its analyzer field names `scripts/m_analyze.py` ("present … not read by G-CAL")". **IMPRECISE (minor).**
- The field is `present <sha16> -- not read by G-CAL`. The sha16 is of m's `_stages.ANALYZER_PATH` = `scripts/m_analyze.py` (m stages.py:149; m gcal.py:620–621).
- It carries no path or name.
- Proposed: "its analyzer field is `scripts/m_analyze.py`'s sha16 ("present <sha16> -- not read by G-CAL")".
- "p's analyzer not existing before step 6" holds.

B34 P13: m's `completability_artifact` is a pure function of the checkpoint that reads no renders; p adds `proposal_p_sha256` and the `p` block; the write is m's write-once `_write_artifact`. **CONFIRMED.** m gcal.py:983–1014, :294–305, :252–283; p gcal.py:295–319, :413.

B35 P13: "m's model-free builder (`_renders_of_record`, `gcal.py:386–387`) is not called". **IMPRECISE (minor naming).**
- :386–387 is the stop on renders other than `corr.renders_m`'s. It is inside `_renders_of_record` (def at :364), the renders step of m's model-free builder `model_free_artifact` (:434, which calls it at :457).
- p calls neither (grep).
- The anchor holds at 18b0111 and at 993eba1; the hygiene edit is below :2390.
- Proposed: "m's model-free path (`model_free_artifact` → `_renders_of_record`, which stops on any renders but m's, gcal.py:386–387) is not called".

B36 P14: m's `_stop_reasons` by import with exactly `coverage:Q-F0` removed ("m's function adds it for every built unit absent from the grid"), plus `p-guard`. **CONFIRMED.**
- gshape.py:293–300.
- m gshape.py `_stop_reasons` adds `coverage:{unit}` for each unit of `UNITS_BUILT` absent from `g`.
- Self-test "exactly 'coverage:Q-F0' removed".

B37 P15: Layer S is m's `runner_scope_problems` as written, its Qwen half included. **CONFIRMED.** gshape.py:316; m gshape.py:1336ff (`RUNNER_FILES`, both runners).

B38 P16: the renders are read from the committed renders raw's `json.dumps(renders)` line, sha256-pinned, asserted equal to `RENDERS_OF_RECORD` and to `corrupt_p`'s recomputation under both conventions; "condition (3) is the seat's read". **CONFIRMED.** gshape.py:79–81, :122–134, :228–237; the raw hashes to `25bd3d01…`; ans2:7.

B39 P17: the canonical run's committed-and-unedited rule (sources map, closure, package hash = blobs' hash) "as G-SHAPE-F0's does"; drift is a refusal; an `--out` run is refused under `data/m`, `data/mf3` and at or around `data/p/gates`; seams never write the canonical path; the placement-key comparison is descriptive. **CONFIRMED.**
- gshape.py:137–141, :259–271, :380–392, :397–401, :278–290.
- m gshape.py:287, :541–548, :1589–1592.
- Minor: `--out` is also refused under `/workspace/models` (guard.py:37), which the parenthesis omits.

B40 P18: the weights-files check is p's own, to `olmo_weights_problems`' semantics; a size check, never a re-hash; "p's licence therefore binds no m script". **CONFIRMED.**
- p_sessions.py:108–138 against m_sessions.py:707–761 (same checks).
- `M_HASHED` names m modules only.

B41 P19: `M_IMPORTED` is measured as sixteen m modules in a fresh `-I -B` interpreter; the list given; seventeen with `__init__.py`. **CONFIRMED.**
- My measurement matches the list exactly.
- guard.py:41–43, :90–98.
- NOTE: the parenthesis follows "every p production module" but lists m modules; consider moving it after "modules".

B42 P19: "m's `testing.py` is imported by p's self-tests only". **CONFIRMED.**
- p/testing.py:14 imports it at module level, and p/testing is imported only inside `_selftest` (proxy.py:92, gcal.py:423).
- gcal.py:422 and proxy.py:122 also import it inside `_selftest`.
- It is not in the fresh-interpreter set.

B43 P19: `refuse_out` refuses `data/m`, `data/mf3` and `/workspace/models` "for any p output". **CONFIRMED.**
- guard.py:37, :78–87.
- Every p write is either canonical under `data/p` or passes through `refuse_out`: schedule.py:78–81, gshape.py:385–388, gcal.py:120–123.

B44 P20: all five `data/p` roots are admitted, in mf3's form; `data/p/ckpt/**` is `-diff`. **CONFIRMED.**
- `.gitignore`: the p block sits at the end of the file and uses the same `!dir/`, `dir/*`, `!dir/*.json` pattern as mf3's block just above it (mf3 has four roots; p adds `verdicts`).
- `.gitattributes`: `/data/p/ckpt/** -diff`.

### §5 FLAGs

Recomputed from `git show HEAD:data/m/gates/G-CAL_completability_olmo-{ckpt}.json` with `report.corrupted_spelling`:

| ckpt | records | counted |
|---|---|---|
| sft | 128 | 4 |
| dpo | 128 | 10 |
| instruct | 128 | 9 |

B45 F-p1: "4/10/9 records (sft/dpo/instruct), 23 in all" of 384. **CONFIRMED.**

B46 F-p1: "Five are §0.3's class (c) (`Januwy` ×2, `Janaury`, `dn` ×2)". **CONFIRMED.** dpo and instruct corrupted 8 s2 `Januwy`; instruct 8 s3 `Janaury`; dpo and instruct 11 s1 `dn`.

B47 F-p1: "one is a misspelling of the model's own (`irom`, instruct item 7 s1)". **CONFIRMED.** `irom`/`iron` is distance 1; the record (the DEL record) also holds `on`/`iron`.

B48 F-p1: "the other 17, four of them clean-pool records", with the pairs listed. **CONFIRMED.**
- sft 4, dpo 8, instruct 5.
- The clean-pool ones are sft 10 s0, sft 10 s1, dpo 4 s1 and dpo 10 s0.
- The pairs are exactly the/two, the/three, true/three, on/iron, in/iron, do/down; all six occur and no other.

B49 F-p1: these 17 "count only a common word within distance 2 of a short gold". **IMPRECISE** (borderline).
- One of the 17, sft CORR_corrupted 11 s2, reads "Correct: 'do' -- 'do' is the oppossitu of 'up' …".
- It counts `'do'` given as the model's *answer* to the opposite of 'up' (do/down): the `dn` kind rather than an incidental common word.
- Proposed: "…16 count only an incidental common word…; one (SFT corrupted 11 s2) counts `'do'`, given as the answer to the opposite of 'up'". Or keep the wording and accept the reading.

B50 F-p1: "`Janbaa` and `Janyooar` (class (c) by §0.3) lie at distance 3 or more." **IMPRECISE** (true but incomplete).
- The distances are 3 and 4; neither is counted.
- But §0.3 (p:17) also lists `Ther qro abov two dsys in a wemk` (instruct corrupted 1 s1) in class (c), and the rule does not count it either: its nearest word is at distance 4 from `seven`.
- dpo 1 s1, `Ther qro abov two.`, is of the same kind, is not listed in §0.3 and is not counted.
- Proposed: add "…and `Ther qro abov two dsys in a wemk` (no word within distance 2 of `seven`)".

B51 F-p1: "The counter decides nothing (rule 23)". **CONFIRMED.** p:68; CLAUDE.md rule 23.

B52 F-p2: `OLMo-sft_qual_A0s-OLMo-sft.json` draws m's π `[3, 1, 0, 2]`, and so m's cells. **CONFIRMED.**
- In that file p and m differ only in `key_template` and `session_keys`.
- m gate_schedule: the cells are a function of π and the fixed `GATE_TABLE`.

B53 F-p2: "a coincidence of two different streams (`permutation(4)` takes 24 values)". **CONFIRMED.** crc32 seeds 1807384619 (`p-sched|…`) and 1467735899 (`m-sched|…`); 4! = 24.

B54 F-p2: "Every other file's cells differ from m's, and so does every other gate file's π (the six campaign files carry none). Each file's key template names `p-sched|…`." **CONFIRMED.** All 18 files were compared:
- 17 have different cells;
- 11 of the other 11 gate files have a different π;
- no campaign file has a `pi`;
- all 18 `key_template`s begin with `p-sched|`.

B55 F-p3: both artifacts carry §5.4's disclosure with 2026-11-06; referent item 85; `18b0111`. **CONFIRMED.**
- gcal.py:82–84 and :318; gshape.py:358.
- p:102; referent-check.md:261–267.
- NOTE: editing the constant edits gcal.py, which moves p's `package_sha256` and G-SHAPE-p's sources map. If G-SHAPE-p's run of record lands first, it re-runs.

B56 F-p4: (3) is built at step 6; its kind field names the Clock; its other two parts are data roots; (4) is declared and not exercised. **CONFIRMED.** register.py:62–70.

B57 F-p5: "The licence names m's `gcal.py`, `gshape.py`, `stages.py`, `runner_qwen.py` and `verify.py` among the sixteen, because p imports them." **IMPRECISE (minor).**
- True: all five are in `M_IMPORTED`.
- But beyond mf3's ten (valence_core/mf3/guard.py:66), p's licence adds *six* m modules: these five and `runner_olmo.py`.
- If the five are meant as that set, `runner_olmo.py` is missing; if they are examples, say so.
- Proposed: "…names m's `gcal.py`, `gshape.py`, `runner_olmo.py`, `runner_qwen.py`, `stages.py` and `verify.py` (beyond mf3's ten)…" or "…among them `gcal.py`…".

B58 F-p5: "The coordinating session's hygiene commit (the 11-07 routing's item 1) edits `valence_core/m/gcal.py`". **CONFIRMED.** `git show --stat 993eba1` lists `valence_core/m/gcal.py`; the routing's item 1 is quoted in its message and in ans2:70.

B59 F-p5: "so p's licence line for it moves when that commit lands". **FAIL (stale).**
- It has landed (993eba1, HEAD at this check): gcal.py moved from `d60b78e5…02fe` to `fbae9a01…f6ef`.
- `hashes` already prints the new value, so this BUILD's licence lines carry it.
- Proposed: "The hygiene commit `993eba1` (the 11-07 routing's item 1) edited `valence_core/m/gcal.py` (`d60b78e5…` → `fbae9a01…`) before this BUILD, so the licence lines here carry the post-hygiene value; LOCK-p v0.1 names the values current at its writing…".

B60 F-p5: "LOCK-p v0.1 names the values current at its writing, and G-SHAPE-p re-runs first if its sources map differs then, as G-SHAPE-F0's and G-SHAPE-F3's rule has it." **CONFIRMED** (as a paraphrase).
- ans2:50: "G-SHAPE-F0 re-runs iff a PIN-S10 file changed"; G-SHAPE-F3 re-runs when mf3's sources move.
- Both re-runs are in progress now (§0).

B61 F-p6: "Disclosed at `18b0111`: the package was written in the working tree while v0.2's referent check ran, before step 3's commit." **CONFIRMED.** RESULTS.md@18b0111:105–107.

### §6 Not built

B62 `scripts/p_analyze.py` and G-ANL-p are p §8 step 6's "(after LOCK-m-F3 v0.1, p §4.3; p §4.4: "if every checkpoint fails G-CAL-p, no p analyzer is built")". **CONFIRMED.** p:129, :88; the quote is verbatim at p:90 (without its bold and trailing comma).

B63 The OLMo gate-stage and campaign drivers are step 6's too: "p §6.2 has G-CAL-p first, as it "decides whether anything else of p is built"". **CONFIRMED.**
- The quote is verbatim at p:110.
- The step-6 placement is presented as Code's inference, and is consistent with p:127 and p:129. A50 asks for A's citation to match this.

B64 "The driver refuses `time`, `qual` and `campaign` (exit 2), each named." **CONFIRMED.** p_sessions.py:319–321, :65–67; self-test.

B65 "No LOCK-p file is written; nothing runs on a model or the box." **CONFIRMED.** No `LOCK-p*` file; no model path runs off the box (A9).

## C. Incidental: the same issues in the code to be committed (not A/B claims)

- C1. `valence_core/p/schedule.py:9` and :59 cite `valence_core/m/schedule.py:511`. The literal is at :512 (B15).
- C2. `valence_core/p/proxy.py:12` and :21 cite `olmo_hf.py:284`. The strip is at :286 (B18).
- C3. `valence_core/p/report.py`'s docstring (:22–27) repeats F-p1's text: B49 and B50 apply there too.
- C4. `valence_core/p/gcal.py`'s docstring (:14) says "The generation call's arguments are m's", which is accurate. p §3.1 and ans2 Q3 (b) say the prompt and the generation call are m's "by import or by §4.2's register". p writes both itself, in its own loop, with m's constants. Neither A nor B declares this as a PIN or FLAG (A20, B8).

## D. Corrections in one place

| item | verdict | correction |
|---|---|---|
| A46, B59 | FAIL | F-p5 is stale: the hygiene commit has landed (`993eba1`); gcal.py is now `fbae9a01…` |
| B18 | FAIL | `olmo_hf.py:284` → `olmo_hf.py:286` (also proxy.py:12, :21) |
| B15 | IMPRECISE | `schedule.py:511` → `schedule.py:512` (also p/schedule.py:9, :59) |
| A20 | IMPRECISE | gcal runs p's own precheck and loop (mirroring m's `run_completability`, m's constants), not "m:176's procedure through m's gcal by import"; consider a PIN or FLAG |
| A34, B8 | IMPRECISE | entry (4) is unexercised because m's `run_completability` is not called, not because of `_task_of`'s argument |
| A26 | IMPRECISE | not every refusal precedes the load: startup, checkpoint and grader-honesty refusals follow it, before any generation |
| A50 | IMPRECISE | the step-6 placement of the drivers rests on §8 (step 4's list), with §6.2 giving the reason |
| A42, B49 | IMPRECISE (borderline) | one of the 17 counts `'do'`, the model's answer |
| B50 | IMPRECISE | §0.3's `Ther qro abov two dsys in a wemk` is also class (c) and also not counted |
| B3 | IMPRECISE | the restoration check inside `substituted` runs on a normal exit only |
| B4 | IMPRECISE | the table paraphrases the printed register (kind `clock`; statuses) |
| B25 | IMPRECISE | ans2 Q4 (ii) covers unit and template strings, not stage, procedure or on_fail |
| B33 | IMPRECISE | the analyzer field holds m_analyze.py's sha16, not its name |
| B35 | IMPRECISE | the model-free builder is `model_free_artifact`; `_renders_of_record` is its renders step |
| B57 | IMPRECISE (minor) | the five listed omit `runner_olmo.py` if meant as "beyond mf3's ten" |

## Summary

118 items: 98 CONFIRMED, 15 IMPRECISE, 3 FAIL, 2 NOT CHECKABLE.
- A, the entry: 53 items — 45 CONFIRMED, 5 IMPRECISE, 1 FAIL, 2 NOT CHECKABLE.
- B, the design raw §3–§6: 65 items — 53 CONFIRMED, 10 IMPRECISE, 2 FAIL.

The three FAILs:
- F-p5 is stale twice (A46, B59): the hygiene commit `993eba1` landed during the check and moved `valence_core/m/gcal.py`.
- P5's `olmo_hf.py:284` (B18) is a blank line; the strip is at :286.

Every count holds when recomputed:
- 11 package files; 18 schedule files plus the manifest;
- 16 measured m modules, 17 licence files;
- 2,816 per unit and 8,448 in all;
- 23 of 384 records (4/10/9), 5 class (c), 1 `irom`, 17 others of which 4 clean-pool;
- π `[3, 1, 0, 2]` in exactly one gate file.

Every quote of the spec and of the PI matches byte for byte.

The self-test has 89 checks. It ran 88/89 while a parallel session's G-SHAPE-F0 re-run was uncommitted, and 89/89 at the final HEAD `f9700ba`. Commit the BUILD by path.

## 2. Pass 2 (the agent's report, verbatim)

# p package — BUILD: blind values-check, round 2 (2026-11-07)

Texts checked (read-only):
- **A** = `podwatch/build_entry.md` (the RESULTS.md entry draft; 83 lines, sha256 `8e073f1b…93bf`).
- **B** = `podwatch/p_build_design_body.md` (design raw §3–§6; 190 lines, sha256 `3331d8a3…423f`).

Placeholders (`@@SELFTEST@@`, `@@STAMP@@`, `@@MANIFEST@@`, `@@PKG@@`, `@@OLMOHF@@`, `@@CHECKS@@`) are not checked.

Method. Every number, file name, file:line anchor, quote, attribution, code description and inclusive claim was checked with a tool:
- `jlens-qwen36/.venv/bin/python -B scripts/p_sessions.py --selftest` (twice), `hashes`, and `gshape --out vc2/gshape_out`;
- `-B` / `-I -B` snippets: the fresh-interpreter import set (production modules, and the driver); `guard.substitution_problems` on the tree and on 11 extra probe files; p's schedules against `data/m/schedules` (bytes, cells, π, key templates); m's `verify_schedule_dir` run on `data/p/schedules` under entry (2); the counters recomputed on the three G-CAL-OLMo artifacts read with `git show HEAD:`; placement keys against m's own enumeration and HEAD's G-SHAPE-F0 blob; m's `gate_line` for `G-CAL-p-sft`; `corrupt.conditions_1_2`; m's package hash over the blobs at `18b0111`, `993eba1` and HEAD; the cached OLMo-3 tokenizer (`~/.cache/huggingface/.../Olmo-3-1125-32B/.../tokenizer.json`, read only);
- `git show`, `git diff`, `git status`, `git check-ignore -v --no-index`, `git check-attr`, `/usr/bin/grep -n`, `sed -n`.

No repository file was written. Outputs: `vc2/{selftest.txt,hashes.txt,gshape.txt,gshape_out/,forms/,start_shas.txt,end_shas.txt}`.

## 0. State during the check

- HEAD was `9838664` (N1 — HELD) at start and end. It is three commits above pass 1's start (`993eba1` hygiene → `0786c11` G-SHAPE-F0 re-run → `f9700ba` G-SHAPE-F3 re-run → `9838664`). None of them touches `valence_core/m/`, `olmo_hf.py` or p's files after `993eba1`.
- A, B, the eleven `valence_core/p/*.py` and `scripts/p_sessions.py` hashed identically at start and end (`vc2/start_shas.txt` = `vc2/end_shas.txt`).
- The self-test is now **101/101** (register 6, corrupt 12, keys 7, schedule 9, proxy 9, report 7, guard 6, gcal 21, gshape-p 12, p_sessions 12), exit 0, both runs.
- `git status` on the BUILD's paths: 31 untracked files (11 package files, the driver, 19 schedule files) and the two modified dotfiles. Nothing under `valence_core/m`, `valence_core/adapters`, `scripts/m_sessions.py`, `scripts/m_analyze.py`, `data/m`, `data/mf3` differs or is untracked.
- One untracked raw appeared during the session's day, `results/raw/2026-11-07_n1-battery_design-to-code_answers.md` (the seat's N1 answer); it names nothing of p.

## A. The BUILD entry (build_entry.md; l. = draft line)

A1 (l.1) "p package — BUILD (p §8 step 4)". **CONFIRMED.** p:127 (step 4 "`p package — BUILD`"); p:132.

A2 (l.1–2) `valence_core/p/` (11 files); driver `scripts/p_sessions.py`. **CONFIRMED.** `ls` (11 `.py`); `hashes`: "(11 files, valence_core/p/*.py)".

A3 (l.2) "on PROPOSAL-p v0.2 (`18b0111`)". **CONFIRMED.** `git log` on the file: `18b0111`; sha256 `42f2977b…3b32` = `gcal.PROPOSAL_P_SHA256` (gcal.py:82).

A4 (l.2–3) "the design seat's answers of 2026-11-07 (Q0–Q4)". **CONFIRMED.** ans2:1–3, §1–§5.

A5 (l.3) The PI's "Then build → G-SHAPE-p → G-CAL-p on your go for the box". **CONFIRMED** byte for byte (U+2192 arrows): RESULTS.md:188 and :319, item 3 (the source ends with a period).

A6 (l.3–4) "m's modules are imported unchanged". **CONFIRMED.** `git diff HEAD` / `git status` on `valence_core/m` empty; `guard.substitution_problems()` = `[]`; the self-test's m-untouched cases pass.

A7 (l.4) "the one declared substitution form carries register entries (1) and (2)". **CONFIRMED.** register.py:58–66 (status `BUILT`); `substituted` refuses (3), (4) (:92–94; self-test "entries (3) and (4) … are each a STOP").

A8 (l.5) "a G-SHAPE-p trial PASSes". **CONFIRMED.** My `gshape --out`: exit 0, "G-SHAPE-p: PASS".

A9 (l.5–6) "Nothing is locked, and nothing runs on a model or the box". **CONFIRMED.** No `LOCK-p*` file; `data/p/` holds `schedules/` only; `gcal` refuses without a pod id (gcal.py:214–217; self-test, exit 2).

A10 (l.8–9) "the design raw … §1 lists every file with its sha256". **NOT CHECKABLE.** `results/raw/2026-11-07_p-build_design.md` does not exist; §1 is not in B.

A11 (l.10) `register`: "ans2 Q0's five terms, p §4.2's entries (1)–(4)". **CONFIRMED.** ans2:11 terms (a)–(e); p:86 entries (1)–(4); register.py:3–15, :58–77.

A12 (l.10–11) "each built entry's replacement enforced by qualified name". **IMPRECISE (minor).**
- The replacement is *declared* by qualified name (`Entry.allowed`, register.py:45–47) but *enforced by identity*: `v is not _resolve(allowed[a])` (:101), the object the name resolves to.
- A name match is exactly what the code refuses: the self-test's "a stand-in carrying its qualified name" is a STOP (register.py:160, :176–181). B §3 says it correctly.
- Proposed: "each built entry's replacement declared by qualified name and enforced by identity with the object that name resolves to".

A13 (l.12–13) `corrupt`: `corr.corrupt_m` under entry (1) with `eligible_p` (p §1.1, §1.4); renders of record; both sha conventions; §3.2's conditions (1)–(2) per item. **CONFIRMED.** corrupt.py:110–113, :32–51, :130–141; p:31, :58.

A14 (l.14–15) The six key families. **CONFIRMED.** keys.py:24; self-test "the six families are p §4.1's"; p:84; ans2:36.

A15 (l.15–17) m's builder under entry (2); `data/p/schedules/`, eighteen files and their own manifest, in m's schema names and layout (ans2 Q4 (iii)). **CONFIRMED.**
- 18 files + `manifest.json`; file names identical to m's 18 `OLMo-*` files; schema `m-schedule-v1` / `m-schedules-manifest-v1`; same key sets as m's files; written by `m_schedule.dumps_schedule` (schedule.py:77).
- The manifest's 18 sha256s match the files; `verify_schedule_dir()` = `[]`.
- ans2:38.

A16 (l.17) "G-CAL-p's seeds stay `m-cal|…`". **CONFIRMED.** m gcal.py:556–569 (`keys.cal_seed`, never substituted); keys self-test.

A17 (l.18–19) `proxy`: §2.2, reading (b), `StoredTextProxy` over the returned result, `olmo_hf.py` unedited. **CONFIRMED.** proxy.py:50–88; `olmo_hf.py` last touched `e26e9c9`, no diff.

A18 (l.20) `report`: five counters and the trigger's predicate. **CONFIRMED.** report.py:45, :48–50; p:68 lists the same five.

A19 (l.21–23) `guard`: package hash, licence sha256s, measured import set, term (e)'s check over p's modules and driver, refused roots `data/m`, `data/mf3`, `data/olmo`, `/workspace/models` (all of `data/` for a test output), the link-safe writers. **CONFIRMED.** guard.py:68–69, :76–94, :59–61 with :206–214, :101–103 with :299–352, :54 with :114–132, :148–203.

A20 (l.24–26) `gcal`'s pieces by import (key set and seeds, task of a key, segment form, startup, f0's grader and honesty asserts, identity, gate line, condition (4), weights of record, boundary assertion, artifact schema fields). **CONFIRMED.** p gcal.py:400, :447, :448 (`m_gcal.SEGMENT_FORM`, m gcal.py:133), :418, :468, :401, :230, :218, :352 (→ `condition_4`, m gcal.py:989), :211, :452 (`m_sc.assert_boundary`), :352.

A21 (l.26–27) p's own: the precheck, the loop, the checkpoint `p-gcal-checkpoint-v1`. **CONFIRMED.** gcal.py:188–226, :445–473, :83.

A22 (l.27) "(… every STOP recorded in it)". **IMPRECISE (minor)** — an inclusive claim wider than P10's.
- Recorded: the loop's four kinds (trigger, boundary, proxy's, insulation guard's), via `_stop` (gcal.py:381–387).
- Not recorded: a register/keys STOP in the precheck, before any checkpoint exists (gcal.py:206, exit 4); and the checkpoint write's own link STOP (`_write`, :293–298, called at :442 and :472), which cannot write the file it refuses.
- Proposed: "the checkpoint (`p-gcal-checkpoint-v1`; every STOP of the loop recorded in it)".

A23 (l.27–30) The hair trigger and the artifact's `p` block (both conventions, conditions (1)–(3), the proxy's cuts, the clean-pool identity, the strict grade, the counters, the covariates beside, the licence values at the run, the disclosure). **CONFIRMED.** gcal.py:463–465; :358–377 (each field present).

A24 (l.30–31) "m's `run_completability` is not called; the generation call, inline there, is restated and pinned to m's by an AST comparison and a check of all 128 calls (P21, F-p7)". **CONFIRMED.**
- `grep`: `run_completability` appears only as `inspect.getsource`'s argument (gcal.py:530).
- `_call_pin_problems()` = `[]`; self-test "every generate call p makes is m's procedure -- 128 calls …" PASS.

A25 (l.32–34) `gshape`: G-SHAPE-F0's layers by import with `coverage:Q-F0` removed, p's renders from the committed raw, three OLMo units, Layer P. **CONFIRMED.** gshape.py:341–348, :323–330, :250–259, :80.

A26 (l.35–36) `testing`: two doubles; `ChunkScriptedAdapter` with `---\n\n` as one token, "as on OLMo's tokenizer"; imported by self-tests only. **CONFIRMED.**
- testing.py:18–59.
- The cached OLMo-3 tokenizer (`Olmo-3-1125-32B`, tokenizer.json, read only) encodes `---\n\n` as one id, and the record text as `['---\n\n', 'Task', ':', …]`. That file is a different revision from the manifest's (sft/dpo/instruct share `75f0d78a…`). Independently, p §2.1's mechanism, under which the gcal records' generation ran past `---\n\n`, needs the first token to carry `---` and the newlines together.
- Only `proxy._selftest` and `gcal._selftest` import it (proxy.py:94, gcal.py:584).

A27 (l.37–38, l.40) The subcommands `--selftest`, `--build-schedules`, `hashes`, `gshape`, `gcal --unit OLMo-{ckpt} [--resume]`; `time`, `qual`, `campaign` refused. **CONFIRMED.** p_sessions.py:347–382, :68–75; self-test (exit 2, each named).

A28 (l.38–40) gcal "(the box only; every refusal that needs no model before the load, m's startup and the checkpoint identity's comparison after it and before any generation; the DRIVER and WEIGHTS lines; the OLMo adapter through the proxy)". **IMPRECISE (minor)** (pass 1's A26, mostly applied).
- Correct:
  - p's own model-free refusals precede the load: the precheck, the weights files, the key set, the honesty asserts, the checkpoint validity and the pod change (p_sessions.py:164–175; gcal.py:397–412).
  - The startup and the identity comparison come after the load (:413–431).
  - The DRIVER and WEIGHTS lines: p_sessions.py:176–180.
  - The proxy: gcal.py:413.
- Not every model-free refusal precedes the load. m's `_startup_olmo`, run on the loaded adapter, holds two model-free asserts: `guard.assert_insulated()` (m gcal.py:872) and the TEMP/cap check (:878).
- Proposed: "every refusal of p's own that needs no model before the load; m's startup (its insulation and TEMP/cap asserts included) and the checkpoint identity's comparison after it and before any generation".

A29 (l.41–42) `.gitignore` admits `data/p/{schedules,gates,reports,ckpt,verdicts}/*.json` and the pod-change set-asides; `.gitattributes` marks `data/p/ckpt/**` `-diff` (m:318 by reference). **CONFIRMED.**
- `git check-ignore -v --no-index`: a `*.json` under each root and `ckpt/*.json.podchange-*` are admitted; `*.tmp`, other files and other directories are ignored.
- `git check-attr diff`: `unset` under `data/p/ckpt/` (nested included).
- m:318 is "**Blinding.**"

A30 (l.43) The licence "(p §4.2, C2's form; `scripts/p_sessions.py hashes`…)". **CONFIRMED.** p:86 "Licence (C2's form): LOCK-p v0.1 names p's `package_sha256`, the file sha256 of each imported `valence_core.m` module and of `valence_core/adapters/olmo_hf.py`, each by name on one lock line, and the register"; `hashes` prints these.

A31 (l.43–44) "verbatim in the design raw §2". **NOT CHECKABLE.** The design raw does not exist.

A32 (l.44–46) p's `package_sha256` (11 files); the seventeen m files (sixteen modules measured in a fresh interpreter, and `__init__.py`); `olmo_hf.py`; each by name on one line. **CONFIRMED.**
- My `-I -B` import of the nine production modules, and separately of the driver, loads exactly sixteen m modules, M_IMPORTED.
- `hashes` prints 1 + 17 + 1 `LICENCE` lines.

A33 (l.46) "m's `gcal.py` is the hygiene commit's (`993eba1`, `fbae9a01…`)". **CONFIRMED.**
- `git show 993eba1:…gcal.py` = working tree = `fbae9a01…f6ef`.
- `18b0111`'s blob is `d60b78e5…02fe`.
- No commit after `993eba1` touches the file.

A34 (l.46–48) "Nothing in `valence_core/m/`, `scripts/m_sessions.py`, `scripts/m_analyze.py`, `olmo_hf.py`, `data/m/` or `data/mf3/` changes." **CONFIRMED.** `git diff HEAD --stat` and `git status --untracked-files=all` on those paths are empty.

A35 (l.49–50) "(1) `corr._eligible_m` → `eligible_p`, built; (2) `valence_core.m.keys`' four key functions → p's, built". **CONFIRMED.** register.py:59–66.

A36 (l.50–52) "(3) `scripts/m_analyze.py` through `scripts/p_analyze.py` (the OLMo Clock → D_p, the `data/m/…` roots → `data/p/…`, the v2 verdicts-dir resolution), declared, built at step 6". **CONFIRMED.** register.py:67–72; p:86 (3); ans2:11.

A37 (l.52–53) "(4) `gcal`'s renders source, declared and not exercised, as G-CAL-p does not call m's `run_completability`". **CONFIRMED.** register.py:73–76; A24. Pass 1's A34 is applied.

A38 (l.53–55) Term (c)'s equality cases pass, and restoration holds after each call, an exception included. **CONFIRMED.**
- `corrupt_p` equals m's renders exactly on items [0, 12] (recomputed).
- `schedule.file_blobs(p_keys=False)` reproduces the 18 `data/m/schedules/OLMo-*` files byte for byte (recomputed).
- Restoration after an exception: the register, corrupt and keys self-tests pass.

A39 (l.55–56) "No other site exists (term (e)'s static check is clean, and it catches the sixteen planted forms of its self-test)". **CONFIRMED.**
- `substitution_problems()` = `[]` over the 10 production files and the driver.
- `PLANTED` has 16 entries, all caught (guard self-test).
- `grep` finds no `importlib`/`__import__`/`sys.modules` write, no `setattr` outside register.py and self, and no `classify` call in production code. See B10 for the check's own reach.

A40 (l.57–58) Trial: "PASS — 2,816 placements per OLMo unit, 8,448 in all, none fired or misplaced". **CONFIRMED.** `gshape.txt`: 2816/0/0 ×3; total 8448.

A41 (l.58–59) "`seg+gold` fires on every placement; the three grids identical; no shape, Layer S or Layer P problem". **CONFIRMED.** seg+gold 2816/2816 ×3; "grids identical: True"; shape 0, S 0, P 0.

A42 (l.59) "each unit's placement keys equal m's own enumeration and G-SHAPE-F0's artifact at HEAD". **CONFIRMED.**
- `placements_sha256` from my trial artifact = m's own enumeration (`m_gshape.placements` with m's renders, recomputed) = HEAD's G-SHAPE-F0 blob (`38ba8e28…`, the `0786c11` re-run), for every unit: sft `be6ddba6…`, dpo `2fec663f…`, instruct `f7f90e86…`.
- Note: the trial prints only the G-SHAPE-F0 comparison. The m-enumeration equality is the self-test's check (gshape.py:484–489), as P17 says.

A43 (l.60) "twenty-one PINs (P1–P21), each the seat's to strike until LOCK-p v0.1". **CONFIRMED.** B §4 holds P1–P21, contiguous; its heading says so.

A44 (l.60–61) "Ten FLAGs, none blocking G-SHAPE-p". **CONFIRMED.** B §5 holds F-p1–F-p10; its heading reads "none blocks G-SHAPE-p".

A45 (l.62–63) F-p1: "counts 23 of G-CAL-OLMo's 384 records, 17 of them only for a common word within distance 2 of a short gold". **IMPRECISE (minor, borderline;** pass 1's A42, not applied in A).
- The figures are exact (B50–B53).
- B now says one of the 17 is borderline: SFT corrupted 11 s2 gives `'do'` as its answer for the opposite of 'up'. A's "only for a common word" still asserts all 17 are incidental.
- Proposed: "…17 of them for a common word within distance 2 of a short gold (`the`/`two`; one borderline, SFT's `do` for the opposite of 'up')".

A46 (l.64) F-p2. **CONFIRMED** (B57–B59).

A47 (l.65) F-p3. **CONFIRMED** (B60).

A48 (l.66) F-p4. **CONFIRMED** (B61).

A49 (l.67) F-p5: "the licence moves with m (the hygiene commit moved `gcal.py`'s sha256)". **CONFIRMED** (A33). Pass 1's FAIL is applied.

A50 (l.68) F-p6. **CONFIRMED.** `18b0111`'s entry and commit message: "Code began writing valence_core/p/ in the working tree while the referent check ran".

A51 (l.69) F-p7: §3.1's "by import or by §4.2's register". **CONFIRMED.** Verbatim at p:74.

A52 (l.70–71) F-p8: "ans2 Q1 (iii) keeps m's pin for the analyzer's outputs". **IMPRECISE (minor)** — see B68.
- ans2:17 reads: "The proposal pin stays m's; `proposal_p_sha256` is recorded beside it in every p output".
- "for the analyzer's outputs" is Code's reading of Q1's scope (Q1 is the analyzer path; p:86 places the same words in entry (3)). The FLAG asks the seat to confirm that reading, so A should not state it as ans2's.
- Proposed: "ans2 Q1 (iii), on the analyzer path, keeps m's pin, with `proposal_p_sha256` beside it 'in every p output'".

A53 (l.72) F-p9. **CONFIRMED** (B69).

A54 (l.73–74) F-p10; quote "Nothing after the cut is stored". **CONFIRMED.** p:66, a verbatim prefix of "Nothing after the cut is stored, graded, or seen by any later round".

A55 (l.75) "This BUILD is step 4's list." **CONFIRMED.**
- p:127 lists the package, the driver, the corruptor, the proxy, the keys and schedules, the G-CAL-p and G-SHAPE-p tooling and the reporting tool.
- All are built; nothing else is.

A56 (l.75–77) `scripts/p_analyze.py`, G-ANL-p and entry (3)'s self-test are step 6's: "before any LOCK-p v0.1 and after LOCK-m-F3 v0.1 (p §4.3)", and "no p analyzer is built if every checkpoint fails G-CAL-p (p §4.4)". **CONFIRMED.**
- p:129 "(before any LOCK-p v0.1; after LOCK-m-F3 v0.1, §4.3)"; p:88; p:90.
- G-ANL-p carries "the register's equality and restoration cases" (p:90), and term (c)'s third case (p:86).

A57 (l.77–78) "The gate-stage and campaign drivers are step 6's too, by §8's list (p §6.2 gives the reason)." **CONFIRMED.**
- Step 4's list names only the G-CAL-p and G-SHAPE-p tooling (p:127); step 6 runs G-TIME, G-F0m and the campaign (p:129).
- §6.2 gives the reason (p:110).
- Pass 1's A50 is applied.

A58 (l.78–80) The coordinating session's confirmation on 2026-11-07 and its quote. **NOT CHECKABLE.** It is chat only: `grep` over the repo finds it nowhere. A and B quote it identically (whitespace-normalized match).

A59 (l.80) "the PI's item 3 names no analyzer". **IMPRECISE (minor).**
- Item 3 (RESULTS.md:188) reads "route (b) and the register [accepted]". Route (b) is p §4.4's analyzer path, `scripts/p_analyze.py` (p:7, :25 decision (9), :90).
- What names no analyzer is its build sequence, "Then build → G-SHAPE-p → G-CAL-p".
- Proposed: "the PI's item 3 accepts route (b) (the analyzer path) but puts no analyzer in its build sequence".

A60 (l.82–83) Next: G-SHAPE-p's run of record in its own commit; "G-CAL-p waits for the coordinating session's go for the box". **CONFIRMED.** p:132 lists `G-SHAPE-p` as its own entry; RESULTS.md (`139635f`'s close): "G-CAL-p waits for the coordinating session's go for the box, as item 3 has it".

## B. The design raw §3–§6 (p_build_design_body.md; l. = draft line)

### §3 The substitution register

B1 (l.3–4) The form, in `register.py`'s `substituted`, under the seat's five terms (a)–(e). **CONFIRMED.** Verbatim p:86 ("an attribute of an m module replaced for the duration of one call and restored in a `finally`"); register.py:88–116; ans2:11.

B2 (l.4–7) `substituted` refuses:
- an unknown or unbuilt entry;
- a module or attribute set other than the entry's;
- a kind outside the five;
- any replacement value other than the declared one (identity, term (a)).

It also asserts the single thread. **CONFIRMED.** register.py:92–94, :95–97, :98–99 (`KINDS` :29), :100–104 with `_resolve` :119–126, :105; self-test.

B3 (l.7–8) "Restoration is in a `finally`, so it holds after an exception, and it is asserted after a normal exit." **CONFIRMED.** register.py:107–116. Pass 1's B3 is applied.

B4 (l.8–9) "The four entries, as `scripts/p_sessions.py hashes` prints them (§2)". **IMPRECISE (minor)** (pass 1's B4, partly applied).
- Module, attributes, replacement and kind match the printed `REGISTER` lines verbatim in all four rows. (3)'s kind now prints `clock; roots`.
- The status cells of rows (1) and (2) are not the printed status ("built at the p BUILD (p §8 step 4)"). They add self-test descriptions that `hashes` does not print, and the table omits the printed `reason` field.
- "(§2)" points into the unwritten design raw (not checkable).
- Proposed: "The four entries (module, attributes, replacement and kind as `scripts/p_sessions.py hashes` prints them, §2; the status column adds each built entry's self-test):".

B5 Row (1): `valence_core.m.corr` | `_eligible_m` | `valence_core.p.corrupt.eligible_p` | eligibility | built, with its self-test. **CONFIRMED.** `REGISTER` n=1. The self-test lines "corrupt_p reproduces p §1.2's sixteen renders of record", "items 0 and 12 are m's renders", "corr._eligible_m is m's own after every call" and "restoration holds after an exception" all pass.

B6 Row (2): the four functions, `valence_core.p.keys.{…}`, keys; self-test "with m's keys (no substitution) … eighteen OLMo files byte for byte; restoration after the block, an exception included". **CONFIRMED.**
- `REGISTER` n=2.
- `build_objects(p_keys=False)` uses `contextlib.nullcontext()` (schedule.py:59), so "(no substitution)" matches the code. The self-test's label says "substituted back" (C5).
- keys.py:107–113.

B7 Row (3): module, attributes, replacement, kind `clock; roots`, status. **CONFIRMED.** Verbatim `REGISTER` n=3.

B8 Row (4): status "declared; not exercised -- G-CAL-p does not call m's `run_completability` (p's own loop calls m's pieces, p's renders an argument of `gcal._task_of`), so no attribute of `gcal` is replaced". **CONFIRMED.** Verbatim `REGISTER` n=4; m gcal.py:893; p gcal.py:447; self-test `vars(m_gcal)` unchanged. Pass 1's B8 is applied.

B9 (l.18–22) "No other site exists": `guard.substitution_problems`, run over p's production modules and `scripts/p_sessions.py`, finds nothing; "its self-test plants sixteen forms and catches each". **CONFIRMED.**
- `scanned_files()` = the 10 production files plus the driver (guard.py:97–103).
- The result is `[]`.
- `PLANTED` has 16 entries (guard.py:366–383), all caught.

B10 (l.19–22) The check's reach: "no write into an object imported from `valence_core.m` (any import form, a local alias, a tuple target, `vars()` or `__dict__` included)… no `classify` call". **IMPRECISE.**
- "any import form" overstates. Probe files run through `substitution_problems`:
  - not caught: a name bound by `importlib.import_module("valence_core.m.corr")`; `__import__(…)`; `import valence_core` followed by `valence_core.m.corr._eligible_m = …`; a write through `sys.modules["valence_core.m.corr"]`;
  - not caught: an alias bound by an annotated assignment, a walrus or a `for` target;
  - not caught: a bare-name `classify(…)` call, since only attribute calls are matched (guard.py:340);
  - caught: `from valence_core import m`, `from valence_core.m import corr as c`, a nested-function import.
- guard.py's own docstring (:28–30) says dynamic imports bound to a name are outside its reach.
- None of the missed forms occurs in p's production code or driver (`grep`), so "No other site exists" stands.
- Proposed: "(the static import forms -- `from … import`, relative or absolute, `import … as`, a dotted `import valence_core.m…` -- a plain-assignment alias, a tuple target, `vars()` or `__dict__` included; dynamic imports are outside its reach, as guard.py says) … no attribute-form `classify` call".

### §4 PINs

B11 P1: the single-thread assertion (`threading.active_count() == 1`, main thread); every site built at this step runs before any model load (the renders, the schedules, §3.2's conditions in the precheck). **CONFIRMED.**
- register.py:81–85.
- Entry (1)'s callers: `renders_problems` and `conditions` in the precheck (gcal.py:206, :226), before `adapter_factory()` (:413); and gshape's inputs (gshape.py:257). After the load `run` uses the constant `RENDERS_OF_RECORD` and `pre["conditions"]`, never `corrupt_p`.
- Entry (2): the schedule builder only.

B12 P2: the quote rule is m's (each `'` toggles; an odd count is refused, as `_eligible_m` refuses it). **CONFIRMED.** corrupt.py:79–87; m corr.py:192–199.

B13 P2: "its first word" is the first maximal ASCII-letter run, a frame word unless quoted; no CORR item's is quoted. **CONFIRMED.** corrupt.py:82–94; `SPEC_FRAME` equality passes; every item starts with an unquoted Compute/State/Name/Write.

B14 P2: FUNCTION_WORDS matched case-insensitively (v0.2 §1.1; inert; referent item 131). **CONFIRMED.**
- corrupt.py:92.
- The 21 words equal p:31's set (parsed).
- referent-check.md:364–372: item 131, "inert on this pool".

B15 P3: m's key with `m-` → `p-`; a non-OLMo unit passes through; m's builder iterates every built unit; p writes the OLMo files only. **CONFIRMED.** keys.py:33–56; m keys.py:19 (`UNITS_BUILT` includes Q-F0); m schedule.py:542; p schedule.py:62.

B16 P4: m's `_campaign_obj` writes the literal `m-sched|{unit}|{arm}|{b}` at `valence_core/m/schedule.py:512`, not through `keys.sched_key`. **CONFIRMED.** :512 is the `"key_template": f"m-sched|…` line. Gate objects use `keys.gate_sched_key` (:521). Pass 1's B15 anchor fix is applied, also in p/schedule.py:9 and :69.

B17 P4: the cells come from `p-sched|…`; p sets the one field after m's call, inside the substitution, asserted to be m's literal first; m's literal under m's keys; no cell, π or key touched; the field is set outside the register's form. **CONFIRMED.** m schedule.py:230; p schedule.py:59–70; recomputed byte equality.

B18 P4: "m's own `verify_schedule_dir` run under entry (2) would differ from p's files on the six campaign files' key templates alone". **IMPRECISE (minor).**
- Run on `data/p/schedules` under `keys.substituted_keys()`, it reports 14 problems:
  - the six campaign files, each differing only in `key_template` (the field compare confirms it);
  - `manifest.json differs from the regeneration` (p's own construction string and file set);
  - 7 Q-F0 files missing.
- So among p's eighteen schedule files the claim holds; among p's files it does not (the manifest).
- Proposed: "…would flag, of p's eighteen schedule files, the six campaign files alone, each in its key template only (beside p's own manifest and m's Q-F0 files, which p does not write)". p/schedule.py:14–15 carries the same sentence.

B19 P4: canonical write `data/p/schedules`; a test write through `guard.refuse_test_out`; every file once through `guard.write_once_bytes`. **CONFIRMED.** schedule.py:84–114.

B20 P5: "line break" is `\n` or `\r` (§2.3's trigger reads both); the cut text is rstripped, "as the adapter strips its decoded text (`olmo_hf.py:286`)". **CONFIRMED.**
- proxy.py:28, :60; p:68.
- olmo_hf.py:286 is `text=self.decode(gen).strip(), token_ids=gen,`.
- Pass 1's B18 FAIL is applied, also in proxy.py:12 and :21.

B21 P5: the ids run through the first prefix whose decode holds a break after content; a no-break result is the adapter's own object; an unplaceable break is a STOP. **CONFIRMED.** proxy.py:52–59; proxy self-test, the word-hash case included.

B22 P6: control characters are Cc minus `\n`, `\r` (tab included). **CONFIRMED.** report.py:53–54.

B23 P6: the seven listed forms and m:258's eight declared strings (placeholders as wildcards) match at the start of the first line, case as written; `=== … ===` is a whole first line; refusals match case-insensitively, either apostrophe. **CONFIRMED.**
- `banner.DECLARED_HARNESS_STRINGS` has 8 entries; m:258 says "with the two reasoning-block lines, eight declared harness strings".
- report.py:38–43, :57–60: `startswith` / `re.match`, no IGNORECASE; `{L_clean}`, `{L_corr}`, `{L_a}`, `{L_b}` and `{n}` become `.+?`; `fullmatch` on the stripped first line; `_REFUSAL` uses IGNORECASE and `['’]`.

B24 P6: `corrupted_spelling` as written, with the one reading (a §1.1 word; a gold compared only when itself one such word). **CONFIRMED.** report.py:77–80.

B25 P6: the counters tabulate the stored records; the artifact adds `cap_hits_returned_in_cuts` (a cut sets `cap_hit` false, §2.2). **CONFIRMED.** gcal.py:355–356; proxy.py:61; p:66.

B26 P7: the identity's keys. `proposal_sha256` is p's (the gate line checks it committed), `renders_sha256` is p's by m's convention (ans2 Q3 (c)), and `package_sha256` is m's. p adds eight fields; "so a resume never splices two adapters or drivers". **CONFIRMED.**
- gcal.py:229–237, :86–87.
- m gcal.py:837–857 (`_resume.package_sha256()`); m `gate_line` checks the proposal at HEAD (m gcal.py:611–616).
- ans2:32.
- Identity comparison on resume: gcal.py:427–431.

B27 P7: m's stage, procedure and on_fail strings stay m's, "Code's extension of ans2 Q4 (ii), which keeps m's unit and template strings in p's records"; the `p` block carries p's stage name, its procedure difference and its failure consequence; `proposal_p_sha256` sits at the top level. **CONFIRMED.**
- m gcal.py:849, :999–1014 (stage "G-CAL-OLMo", procedure, `ON_FAIL['olmo']`).
- ans2:37 covers unit and template strings.
- p gcal.py:357–375.
- Pass 1's B25 is applied.

B28 P8: the quote "a hit iff the first word of the normalized text is a gold variant"; `twenty-four` → `twenty four`; leading words. **CONFIRMED.** Verbatim p:74; `normalize('twenty-four')` = `'twenty four'`; gcal.py:301–303; self-test.

B29 P9: the seven clean fields against G-CAL-OLMo's committed artifact (blob at HEAD), refused before any load if not committed and unedited; the generation-path fields side by side; "the seat's flag (p §3.1), never a bar". **CONFIRMED.**
- gcal.py:88, :164–175 (`m_stages._committed`, which returns HEAD's blob only when the working tree matches), :208–209 with :221–222, :320–332.
- p:74: "a flag to the seat (adjudication), not a bar".

B30 P10: "Every STOP inside the loop -- the hair trigger, rule 28(d)(a)'s boundary, the proxy's, the insulation guard's -- is recorded in the checkpoint's `stop` field with its key (and the offending text, for the trigger) before the stage exits 4; no record is appended for that key, and a stopped checkpoint is never resumed." **IMPRECISE (minor)** — an inclusive claim.
- The four kinds behave exactly as stated: gcal.py:450–465, `_stop` :381–387; GcalPStop → exit 4 (p_sessions.py:186–188); `read_checkpoint` refuses a recorded STOP (:258–259); self-tests.
- But the loop holds a fifth STOP. The checkpoint write's link refusal (`_write`, gcal.py:293–298, called at :472) is a `GcalPStop` that cannot be recorded in the file it refuses.
- Proposed: "Every STOP of these four kinds inside the loop … (the checkpoint write's own link STOP cannot be recorded)".

B31 P10: a STOP before the generation (boundary, insulation) counts nothing launched; one after it (proxy's, trigger) counts the generation. **CONFIRMED.** gcal.py:450–462; self-test (key 0: launched 1; key 4: launched 4).

B32 P11: a non-stub run requires the following, refused before any load:
- p's package files, m's whole package (every `valence_core/m/*.py`), `olmo_hf.py` and the driver, committed and unedited;
- P21's pin, checked in the precheck too;
- `licence_at_run` in the artifact.

"G-CAL-p needs no lock (p §4.3), so no lock line is checked"; seams are refused on a canonical run. **CONFIRMED.**
- gcal.py:151–161, :220, :207, :335–337 with :376, :395–396.
- p:88.
- m `gate_line` checks the proposal, CLAUDE.md, HEAD and the analyzer, with no lock (m gcal.py:599–626).

B33 P12: the PROVENANCE line prints m's fields and the pod id; the entry carries the pod id as m's does; the gate line is m's for `G-CAL-p-{ckpt}`; the analyzer field reads `present <sha16> -- not read by G-CAL`, `scripts/m_analyze.py`'s sha16. **CONFIRMED.**
- gcal.py:437–441; m gcal.py:1137–1145 (m prints `{record, stamp}`; its OLMo entry carries `pod_id`).
- My call printed "GATE G-CAL-p-sft: … analyzer present 6ec3222b54c78ea5 -- not read by G-CAL", which is m_analyze.py's sha16.
- Pass 1's B33 is applied.

B34 P13: p's builder calls m's `completability_artifact`, a pure function of the checkpoint that reads no renders, and adds `proposal_p_sha256` and the `p` block with §3.2's conditions computed in the precheck. **CONFIRMED.** gcal.py:351–378, :226; m gcal.py:983–1027.

B35 P13: "per item n_eligible, k and the changed positions". **IMPRECISE (minor).**
- Each item records `{"i", "n_eligible", "k", "changed", "skips", "c1_…", "c2_…"}`, where `changed` is the *count* `len(meta["changed_positions"])` (corrupt.py:138–140). The positions are not recorded (printed: item 0 `'changed': 3`).
- Proposed: "per item n_eligible, k and the number of changed positions".

B36 P13: m's `model_free_artifact`, whose renders step `_renders_of_record` stops on any renders but m's (`gcal.py:386–387`), is not called; the write is `guard.write_once_bytes`, the bytes m's `write_json_once` would write. **CONFIRMED.**
- m gcal.py:386–387 is `if renders != corr.renders_m(…)` / `raise GcalStop(…)`, inside `_renders_of_record` (:364). `model_free_artifact` is at :434.
- Neither is called by p (grep).
- p writes `json_text(art, indent=1).encode("utf-8")` (gcal.py:496); m writes `json_text(obj, indent=1)` in utf-8 text mode (m gcal.py:286–287, :271), the same bytes on POSIX.
- Pass 1's B35 is applied.

B37 P14: m's `_stop_reasons` by import with exactly `coverage:Q-F0` removed ("m's function adds it for every built unit absent from the grid"), plus `p-guard`. **CONFIRMED.** gshape.py:323–330; m gshape.py:1395–1403 (`for unit in UNITS` = `keys.UNITS_BUILT`, m gshape.py:78); self-test.

B38 P15: m's `runner_scope_problems` as written, Qwen half included; the artifact points at the runners' dynamic evidence. **CONFIRMED.** gshape.py:346, :380–386; m gshape.py:114–115 (both runners).

B39 P16: renders read from the committed raw's `json.dumps(renders)` line (the seat's read's file, ans2 §0; sha256 pinned), asserted equal to `RENDERS_OF_RECORD` and to `corrupt_p`'s recomputation under both conventions; no model-free G-CAL artifact for p. **CONFIRMED.**
- gshape.py:250–259.
- The raw hashes to `25bd3d01…b895` = `RENDERS_RAW_SHA256`.
- One `json.dumps(renders): ` line.
- ans2:7.

B40 P17: the canonical run's committed rule:
- every file of the sources map and closure committed;
- both package hashes equal their committed blobs' hash, as G-SHAPE-F0's does;
- drift re-read before the write;
- `--out` refused under `data/`, never of record;
- seams never canonical;
- the G-SHAPE-F0 comparison read from HEAD's blob, and the self-test checks against m's enumeration.

**CONFIRMED.**
- gshape.py:139–143, :167–196, :199–222, :284–298, :433–437, :417–426, :225–228, :305–320, :484–489.
- m gshape.py:280–297, :534–553, :1588–1591.
- Note: `refuse_test_out` also refuses `/workspace/models` and an empty path. The parenthesis is not exhaustive and does not claim to be.

B41 P18: p's own weights-files check, to `olmo_weights_problems`' semantics; a size check, never a re-hash; "p's licence therefore binds no m script". **CONFIRMED.** p_sessions.py:119–152 against m_sessions.py `olmo_weights_problems`: the same checks (listed files regular at their byte counts, no unlisted file, path a non-link directory, malformed blocks). `M_HASHED` names m modules only.

B42 P19: `M_IMPORTED` measured, sixteen modules (the list given) in a fresh `-I -B` interpreter after importing every production module; seventeen files with `__init__.py`. **CONFIRMED.**
- My measurement equals the list exactly. guard.py:59–61, :206–214.
- Note, carried from pass 1's B41: the parenthesis follows "every p production module" but lists m modules. Five of the names (gcal, gshape, guard, keys, schedule) are also p module names, so a reader can take the list for p's. Consider moving it after "modules".

B43 P19: "m's `testing.py` is imported by p's self-tests only". **CONFIRMED.** gcal.py:582, proxy.py:153, and p/testing.py:15, which is itself imported only at gcal.py:584 and proxy.py:94, all inside `_selftest`. Not in the fresh-interpreter set.

B44 P19: `refuse_out` refuses `data/m`, `data/mf3`, `data/olmo`, `/workspace/models` for any p output; `refuse_test_out` refuses all of `data/` for a test or stub output; the comparison is case-insensitive. **CONFIRMED.**
- guard.py:54, :106–132.
- Every canonical p write is under `data/p` with a link check up to `data/p` (schedule.py:90, gshape.py:428, gcal.py:138); every other write passes `refuse_test_out`.

B45 P20: all five roots admitted at the BUILD, in mf3's form; `data/p/ckpt/**` `-diff`. **CONFIRMED** (A29). mf3's block (`cd9756e`) admitted all its roots at its BUILD; p's pod-change line follows m's block (.gitignore:242), as F-p9 says.

B46 P21: "m's prompt and generation call live inline in `run_completability` (`gcal.py`, the OLMo branch)". **IMPRECISE.**
- `seg = f"Task: …"` (m gcal.py:1155) and `adapter.generate(…)` (:1164) sit in the loop that Qwen and OLMo share (:1152–1172).
- Only `temp, cap = _ro.OLMO_TEMP, _ro.STOP_CAP` and `_startup_olmo` sit in the OLMo branch (:1102–1104); Qwen's branch binds `_rq.TEMP` at :1101.
- Proposed: "…live inline in `run_completability`'s loop (`gcal.py`), shared by both substrates, with `temp, cap` bound in its OLMo branch".

B47 P21: `run_completability` cannot run for p: its precheck reads a model-free artifact on m's renders, it writes m's roots, its identity has no p field, and it has no hair trigger. **CONFIRMED.** m gcal.py:795–797 (`renders_m` → `_model_free_check`); :653–693 (data/m/gates and data/m/ckpt); :837–857; :1152–1175 (no line-break check).

B48 P21: the AST comparison covers "the segment form; the positional arguments; the six keywords, m's `temp, cap` bound to `OLMO_TEMP, STOP_CAP` in its OLMo branch; the record literal's keys and values". **IMPRECISE (minor)** on "values".
- The segment, the positionals, the six keywords and the one `temp, cap` tuple are checked as stated (gcal.py:531–562).
- The record's keys are compared in full, but its values only for six of the ten keys: `shared = ("seed", "task", "text", "n_tok", "cap_hit", "stop_reason")` (:570).
- `pool`, `i` and `seed_index` are identical in source but uncompared; `hit` differs in form (m: a variable; p: an inline `m_gcal.grade` call).
- Proposed: "…the record literal's keys, and the values of its six generation fields".

B49 P21: a dynamic check that all 128 calls carry m's procedure; entry (4) not exercised. **CONFIRMED.** gcal.py:617–623 (self-test PASS); `vars(m_gcal)` unchanged.

### §5 FLAGs

Recomputed from `git show HEAD:data/m/gates/G-CAL_completability_olmo-{ckpt}.json` with `report.corrupted_spelling`:

| ckpt | records | counted |
|---|---|---|
| sft | 128 | 4 |
| dpo | 128 | 10 |
| instruct | 128 | 9 |

B50 F-p1: "4/10/9 records (sft/dpo/instruct), 23 in all" of 384. **CONFIRMED.**

B51 F-p1: five of §0.3's class (c), `Januwy` ×2, `Janaury`, `dn` ×2. **CONFIRMED.** dpo and instruct corrupted 8 s2 `Januwy`; instruct 8 s3 `Janaury`; dpo and instruct 11 s1 `dn`. These are p:17's class (c).

B52 F-p1: one misspelling of the model's own, `irom`, instruct item 7 s1. **CONFIRMED.** `irom`/`iron` is at distance 1. The render left `iron` intact. That record also counts `on`/`iron`.

B53 F-p1: "the other 17, four of them clean-pool records", with the six pairs. **CONFIRMED.**
- sft 4, dpo 8, instruct 5.
- The clean-pool records are sft 10 s0 and s1, dpo 4 s1 and dpo 10 s0.
- The pairs are exactly `the`/`two`, `the`/`three`, `true`/`three`, `on`/`iron`, `in`/`iron` and `do`/`down`: each occurs, and no other.

B54 F-p1: "one of them borderline (sft item 11 s2 gives `do` as its answer for the opposite of 'up')". **CONFIRMED.** SFT CORR_corrupted 11 s2 reads "Correct: 'do' -- 'do' is the oppossitu of 'up' …". Pass 1's B49 is applied.

B55 F-p1: `Janbaa`, `Janyooar` and `Ther qro abov two dsys in a wemk`, class (c) by §0.3, are not counted, having no word within distance 2 of a gold. **CONFIRMED.**
- Their nearest distances are 3 (`janbaa`), 4 (`janyooar`) and 3 (`have`/`seven`, instruct corrupted 1 s1).
- All three are in p:17's class (c).
- Pass 1's B50 is applied.

B56 F-p1: "The counter decides nothing (rule 23)". **CONFIRMED.** p:68; CLAUDE.md rule 23.

B57 F-p2: `OLMo-sft_qual_A0s-OLMo-sft.json` draws m's π `[3, 1, 0, 2]`, and so m's cells. **CONFIRMED.** That file and m's differ only in `key_template` and `session_keys`, and its cells are equal.

B58 F-p2: "a coincidence of two different streams (`permutation(4)` takes 24 values)". **CONFIRMED.** The keys `p-sched|OLMo-sft|qual|A0s-OLMo-sft` and `m-sched|…` differ (m schedule.py:244: `stream(gate_sched_key(…)).permutation(N_PAIRS)`); 4! = 24.

B59 F-p2: "Every other file's cells differ from m's, and so does every other gate file's π (the six campaign files carry none). Each file's key template names `p-sched|…`." **CONFIRMED.**
- 17 of 18 files have different cells.
- 11 of the other 11 gate files have a different π.
- No campaign file, p's or m's, has `pi`.
- All 18 `key_template`s start with `p-sched|`.

B60 F-p3: G-CAL-p's and G-SHAPE-p's artifacts carry §5.4's disclosure with 2026-11-06 (referent item 85, `18b0111`); "the constant changes before G-CAL-p runs". **CONFIRMED.**
- gcal.py:94–96, :377; gshape.py:395. My trial artifact carries the sentence with 2026-11-06.
- p:102; referent-check.md:261–267; `18b0111`'s message (item 85).
- One constant (gshape imports `gcal.DISCLOSURE`).
- Note, from pass 1: an edit moves p's package hash and G-SHAPE-p's sources map. F-p5's re-run rule covers it.

B61 F-p4: (3) is built with `p_analyze` at step 6, its kinds the Clock and the data roots; (4) is declared and not exercised. **CONFIRMED.** register.py:67–76.

B62 F-p5: the sixteen are mf3's ten and six beyond them (`gcal.py`, `gshape.py`, `runner_olmo.py`, `runner_qwen.py`, `stages.py`, `verify.py`). **CONFIRMED.** valence_core/mf3/guard.py:66 (`M_MODULES`, ten); `M_IMPORTED` minus those ten is exactly these six. Pass 1's B57 is applied.

B63 F-p5: "The coordinating session's hygiene commit (`993eba1`) moved `valence_core/m/gcal.py`'s sha256 `d60b78e5…` → `fbae9a01…` and m's package hash `60199b36…` → `7756dcf4…` (self-test code only)." **CONFIRMED.**
- The blob hashes, recomputed: `18b0111` `d60b78e5…02fe`; `993eba1` `fbae9a01…f6ef`.
- `package_sha256_of_blobs` over m's committed `*.py`: `18b0111` `60199b36…feec`; `993eba1` and HEAD `7756dcf4…49bb`. The working tree's matches.
- `git show 993eba1 -- valence_core/m/gcal.py` is one hunk inside `_selftest` (@@ -2393).
- 993eba1's message names it "the coordinating session's step 1".
- Pass 1's B59 FAIL is applied.

B64 F-p5: "LOCK-p v0.1 names the values current at its writing, and G-SHAPE-p re-runs first if its sources map differs then, as G-SHAPE-F0's and G-SHAPE-F3's rule has it." **CONFIRMED** (as a paraphrase). ans2:50 ("G-SHAPE-F0 re-runs iff a PIN-S10 file changed"; G-SHAPE-F3 re-runs under N3); both re-ran at `0786c11` and `f9700ba`.

B65 F-p5: "The licence lines in §2 are this BUILD's, taken at its commit". **NOT CHECKABLE.** The design raw §2 is unwritten. Today's `hashes` output is in `vc2/hashes.txt`.

B66 F-p6. **CONFIRMED** (A50).

B67 F-p7: P21 restated and pinned; the alternative "would need register entries the seat has not declared (m's gcal roots, its identity, its model-free check) and would lose p's hair trigger". **CONFIRMED.** Entry (4) is the only gcal entry (register.py:73–76; p:86); B47.

B68 F-p8: "ans2 Q1 (iii) keeps m's proposal pin "in every p output" of the analyzer, with `proposal_p_sha256` beside it". **IMPRECISE (minor).**
- The quoted words are verbatim, but in ans2:17 they say where `proposal_p_sha256` is recorded: "`proposal_p_sha256` is recorded beside it in every p output".
- "of the analyzer", set right after the quote, is Code's reading of Q1's scope. That reading is defensible: Q1 is the analyzer path, and p:86 puts the same words inside entry (3). But F-p8 asks the seat to confirm it, so the citation should not carry it.
- G-CAL-p's identity does carry p's sha256 in both fields (gcal.py:230–233).
- Proposed: "ans2 Q1 (iii), on the analyzer path, keeps m's proposal pin, `proposal_p_sha256` 'recorded beside it in every p output'".

B69 F-p9:
- the single-thread assertion is met at every site built here;
- entry (2) names the arm and item streams, which m's scaffold draws per session after the load;
- m's stage roots are in no entry;
- p admits the pod-change set-asides as m does.

**CONFIRMED.**
- B11; p:86 entry (2); m scaffold.py:253–254, :266–267.
- Entries (1)–(4) name corr, keys, m_analyze's defaults and gcal's renders, not the stage code's `data/m/{ckpt,reports,schedules}` (m stages.py:139).
- .gitignore:242 and :307.

B70 F-p10: each cut logged in the checkpoint and the artifact with `text_returned`; nothing of it stored as the record's text, graded or shown; the §2.2 quote; "a one-line change". **CONFIRMED.**
- proxy.py:62–63; gcal.py:470–471, :366–367; record text = the stored cut (:461, :466); p:66.
- Note: the production change is one line (proxy.py:62). The proxy self-test asserts on `text_returned` (proxy.py:137), so it moves with it.
- Likewise F-p8's "one argument" (gcal.py:230) moves the gcal self-test's assertion at gcal.py:637.

### §6 Scope

B71 "This BUILD is p §8 step 4's list." **CONFIRMED** (A55).

B72 `p_analyze`, G-ANL-p and entry (3)'s self-test are step 6's, before any LOCK-p v0.1 and after LOCK-m-F3 v0.1 (p §4.3); the §4.4 quote. **CONFIRMED.** p:129, :88; the quote is verbatim at p:90, without its bold and trailing comma.

B73 The OLMo gate-stage and campaign drivers (G-TIME-OLMo (p), G-F0m-OLMo (p), the campaign) are step 6's by §8's list; §6.2's quote. **CONFIRMED.** p:127, :129; "decides whether anything else of p is built" is verbatim at p:110; driver names at p_sessions.py:69.

B74 "The driver refuses `time`, `qual` and `campaign` (exit 2), each named." **CONFIRMED.** p_sessions.py:378–380, :73–75; self-test.

B75 The coordinating session's confirmation and quote. **NOT CHECKABLE** (A58).

B76 "No LOCK-p file is written; nothing runs on a model or the box." **CONFIRMED** (A9).

## Pass 1's IMPRECISE and FAIL items, re-checked against the new texts

| pass 1 | then | now |
|---|---|---|
| A46, B59 (F-p5 stale) | FAIL | applied: A49, B63 CONFIRMED |
| B18 (`olmo_hf.py:284`) | FAIL | applied (`:286`, also proxy.py:12, :21): B20 CONFIRMED |
| B15 (`schedule.py:511`) | IMPRECISE | applied (`:512`, also p/schedule.py:9, :69): B16 CONFIRMED |
| A20 (gcal "by import") | IMPRECISE | applied (pieces by import vs p's own; P21, F-p7): A20, A21, A24 CONFIRMED |
| A34, B8 (entry (4)'s reason) | IMPRECISE | applied: A37, B8 CONFIRMED |
| A26 (refusals before the load) | IMPRECISE | mostly applied; residue at A28 (m's startup's model-free asserts) |
| A50 (§6.2 attribution) | IMPRECISE | applied ("by §8's list"): A57, B73 CONFIRMED |
| A42, B49 (borderline `do`) | IMPRECISE | B applied (B54 CONFIRMED); A not applied (A45) |
| B50 (`Ther qro …`) | IMPRECISE | applied: B55 CONFIRMED |
| B3 (restoration check) | IMPRECISE | applied: B3 CONFIRMED |
| B4 (table paraphrase) | IMPRECISE | partly applied ((3)'s kind now prints `clock; roots`); status column remains (B4) |
| B25 (ans2 Q4 (ii)) | IMPRECISE | applied ("Code's extension"): B27 CONFIRMED |
| B33 (analyzer field) | IMPRECISE | applied: B33 CONFIRMED |
| B35 (model-free builder) | IMPRECISE | applied: B36 CONFIRMED |
| B57 (six beyond mf3's ten) | IMPRECISE | applied: B62 CONFIRMED |
| A10, A51 | NOT CHECKABLE | still (A10, A31, A58) |

Pass 1's notes:
- B36: the driver was not scanned. Now `scanned_files()` includes it, and the text says so.
- B39: `/workspace/models` is still omitted from P17's `--out` parenthesis (B40 note).
- B41: the parenthesis placement is not applied (B42 note).
- B55: the constant edit moves the hashes; F-p5's rule covers it (B60 note).

## C. Incidental: the code to be committed (not A/B claims)

- C1. `valence_core/p/report.py`'s docstring (:22–27) still has F-p1's earlier text:
  - "`Janbaa` and `Janyooar` … lie at distance 3 or more and are not counted", with no `Ther qro abov two dsys in a wemk` (§0.3 class (c), also not counted);
  - no borderline `do` (B54, B55). This is pass 1's C3, not applied.
- C2. `valence_core/p/gcal.py`'s docstring disagrees with itself and with the code:
  - its PIN list (:51–52) says a non-stub run requires "the m modules of the licence … committed";
  - its ORDER (:27–28) and `committed_problems` (:151–161) check m's whole package, as B P11 says.
- C3. The same docstring's ORDER (:24) says "Every refusal that needs no adapter runs before the load". m's `_startup_olmo` holds model-free asserts and runs after it (A28).
- C4. `valence_core/p/schedule.py`'s docstring (:14–15) carries B18's `verify_schedule_dir` sentence.
- C5. The schedule self-test's label (:136) says "with m's keys substituted back", but the code runs m's builder with no substitution (`contextlib.nullcontext()`, :59). B's row (2) wording ("no substitution") matches the code.
- C6. `guard.py`'s docstring states the static check's reach honestly (:28–30); B §3's parenthetical should match it (B10).

## D. Corrections in one place

| item | verdict | correction |
|---|---|---|
| B10 | IMPRECISE | the static check covers static import forms and plain-assignment aliases, not "any import form": dynamic imports, `import valence_core` + attribute path, annotated/walrus/`for` aliases and bare-name `classify` escape it (none occurs in p) |
| B46 | IMPRECISE | m's prompt and generation call are in `run_completability`'s shared loop (gcal.py:1155, :1164), not its OLMo branch; only `temp, cap` are bound there (:1104) |
| A12 | IMPRECISE (minor) | replacement declared by qualified name, enforced by identity (a stand-in wearing the name is refused) |
| A22 | IMPRECISE (minor) | "every STOP of the loop recorded in it" (precheck and checkpoint-write STOPs are not) |
| A28 | IMPRECISE (minor) | "every refusal of p's own that needs no model before the load; m's startup (its insulation and TEMP/cap asserts included) …" |
| A45 | IMPRECISE (minor) | mirror B: one of the 17 is borderline (SFT's `do`) |
| A52, B68 | IMPRECISE (minor) | ans2 Q1 (iii)'s "in every p output" is said of `proposal_p_sha256`; "of the analyzer" is Code's reading, the FLAG's question |
| A59 | IMPRECISE (minor) | item 3 accepts route (b), the analyzer path; its build sequence names no analyzer |
| B4 | IMPRECISE (minor) | the status cells of (1) and (2) add self-test text that `hashes` does not print; the table omits `reason` |
| B18 | IMPRECISE (minor) | m's `verify_schedule_dir` under entry (2) also flags p's manifest (and m's Q-F0 files as missing); the six campaign key templates are the only schedule-file differences |
| B30 | IMPRECISE (minor) | the checkpoint write's own link STOP inside the loop cannot be recorded |
| B35 | IMPRECISE (minor) | the item records the number of changed positions, not the positions |
| B48 | IMPRECISE (minor) | the AST pins the record's keys and six of its ten values |

## Summary

136 items: 117 CONFIRMED, 14 IMPRECISE, 0 FAIL, 5 NOT CHECKABLE.
- A, the entry: 60 items — 51 CONFIRMED, 6 IMPRECISE, 3 NOT CHECKABLE.
- B, the design raw §3–§6: 76 items — 66 CONFIRMED, 8 IMPRECISE, 2 NOT CHECKABLE.

Pass 1's three FAILs are applied: F-p5 now carries the hygiene commit's values (A49, B63), and P5 cites `olmo_hf.py:286` (B20). So are eleven of its fifteen IMPRECISE items. A45 (A's F-p1 summary) is not applied; A28 and B4 are partly applied, with a residue each.

The two substantive IMPRECISE items are both in B:
- B10 overstates the term-(e) static check's reach ("any import form"), against guard.py's own docstring. The probes show what escapes; none of it occurs in p.
- B46 places m's generation call in `run_completability`'s OLMo branch; it is in the shared loop.

The rest are minor wording items. No figure is wrong. Every count recomputes:
- 11 package files; 18 schedule files plus the manifest;
- 16 measured m modules, 17 licence files;
- 2,816 per unit and 8,448 in all;
- 23 of 384 records (4/10/9): 5 class (c), 1 `irom`, 17 others, of which 4 clean-pool and 1 borderline;
- π `[3, 1, 0, 2]` in exactly one gate file;
- m's package `60199b36…` → `7756dcf4…`.

Every quote of the spec, ans2 and the PI matches byte for byte. The self-test is 101/101 at HEAD `9838664`, and the texts and code were unchanged from start to end.

## 3. Pass 3 (the agent's report, verbatim)

# p package — BUILD: blind values-check, pass 3 (final, focused; 2026-11-07)

Texts checked (read-only):
- **A** = `podwatch/build_entry.md` (the RESULTS.md entry; 89 lines, sha256 `f94a4a5b…d9a2`, the same at start and end).
- **B** = `results/raw/2026-11-07_p-build_design.md` (untracked; 302 lines, sha256 `3da75966…568d`), §1–§7.
- **C** = the headers and §0 of `results/raw/2026-11-07_p-build_{selftest.txt,sitecheck.txt,review.md,valuescheck.md}` (untracked).

Placeholders (`@@STAMP@@`, `@@NPASS@@`, `@@PASS3@@`) are not checked. Pass 2's full sweep is not repeated. Only the five
focus areas are checked, plus whatever the code changed after pass 2 touches.

Method. Every claim below was checked with a tool:
- `shasum -a 256` on the working tree, and a Python comparison of B's two tables (33 rows) and of the site-check header (15 rows) with it;
- `jlens-qwen36/.venv/bin/python -B scripts/p_sessions.py --selftest`, `hashes` and `gshape --out vc3/gshape_out`;
- `git -C <the site check's worktree> diff --name-status 9838664 HEAD`, with each blob of the scratch commit hashed against the working tree;
- independent recomputations:
  - p's and m's `package_sha256`, by the PIN's rule, `resume.py:328–335`;
  - the fresh-interpreter (`-I -B`) import set, for the production modules and for the driver;
  - m's builder under register entry (2) against `data/p/schedules`, and m's `verify_schedule_dir` over it;
  - F-p1's counter on the three G-CAL-OLMo artifacts read by `git show HEAD:`;
- in-process state probes, `vc3/probes/probe_state.py` (round 3's `probe_r23_state.py`, copied) and `vc3/probes/probe_state2.py`. They run the full self-test with one committed file reported as edited by `m_stages._committed`. Nothing is edited on disk;
- verbatim checks of C's report sections against the scratch reports (`vc3/verbatim.py`), and of the self-test and site-check raws against their unscrubbed scratch originals;
- `/usr/bin/grep -n`, `sed -n`, `awk`, `git show`, `git log`, `git check-ignore -v --no-index`, `git check-attr`.

No repository file was written. Outputs are in `vc3/`.

## 0. State during the check

- HEAD was `9838664` at start and end.
- The 33 build files (11 package files, the driver, `.gitignore`, `.gitattributes` and the 19 schedule files) hashed identically at start and end (`vc3/start_shas.txt` = `vc3/end_shas.txt`).
- `git status --porcelain --untracked-files=all` (67 lines) was identical before and after every run and probe.
- The five raws' mtimes (15:53 and 16:02 local) predate the check.
- **Self-test: 103/103, exit 0.** By module: register 6, corrupt 12, keys 7, schedule 9, proxy 9, report 7, guard 6, gcal 23, gshape-p 12, p_sessions 12. My output is byte-identical to `_p-build_selftest.txt`'s body once the repository prefix is shown as `<repo>`.
- The code changed after pass 2: proxy, register, driver, report, gcal, schedule and guard, 15:47–15:52 local. Pass 2 ran its self-test at 15:27 (101/101), so every item below is checked against the current bytes.

## 1. B §1–§2 (the files and the licence)

S1 (B l.7–22) The 14 rows for the 11 package files, `scripts/p_sessions.py`, `.gitignore` and `.gitattributes`. **CONFIRMED.**
All 14 sha256s equal `shasum -a 256` of the working tree (`vc3/cmp_tables.py`, 0 mismatches).

S2 (B l.24–46) "`data/p/schedules/` (19 files; m's schema names and layout, p's own manifest)" and its 19 rows. **CONFIRMED.**
- All 19 sha256s equal the working tree's.
- `ls` gives 19 files. The 18 `OLMo-*` names are exactly m's 18 (`diff` empty). The schemas are `m-schedule-v1` and `m-schedules-manifest-v1`.
- The manifest lists 18 sha256s, all equal to the files'.
- Every file in `valence_core/p/` and `data/p/schedules/` is in the table.

S3 (B l.5) "sha256 of the bytes committed with this raw". **CONFIRMED** (as far as it can be before the commit exists).
- The site check's scratch commit `b1c3f6b` (parent `9838664`, "scratch: p BUILD bytes over 9838664") changes exactly 33 files (A/M).
- Those 33 are B §1's 33 rows, and each blob is byte-identical to the working tree.

S4 (B l.48–75) The §2 block "as `scripts/p_sessions.py hashes` prints them". **CONFIRMED.**
- My `hashes` run (rc 0) prints 25 lines. The block's 24 lines equal them minus the first, the INVOCATION line, which carries a local path.
- The block also equals the site-check raw's "Hashes (stdout)" section minus its INVOCATION line.

S5 (B l.3) The header's figures. **CONFIRMED.**
- PROPOSAL-p v0.2 is last committed at `18b0111` and hashes to `42f2977b…3b32`.
- The seat's answers raw hashes to `ab40f470…b08b`.
- HEAD is `9838664`.

## 2. B §7 and A's "Checks before the commit"

K1 (B l.287–288) "The self-test of record: … 103/103, on the final bytes". **CONFIRMED.**
- My run: 103/103, rc 0, the same output.
- The last build-file edit was `guard.py` at 15:52:30 local (20:52:30 UTC). That precedes the site check's start (20:52:46 UTC) and the stamp of record (21:01:51 UTC).

K2 (B l.288–290) "Its check count is the same in every state of the record: the schedules check is unconditional, and the gcal cases run with the pod id removed (or a stand-in), the canonical roots at a scratch root and the loader trapped." **IMPRECISE (substantive).**

What holds:
- The named mechanisms are in the code: `p_sessions.py:231–233` (unconditional); `:264–270` and `:283–292` (pod id removed, or `selftest-pod`; `GATES_DIR`/`CKPT_DIR` patched to a scratch directory; `_load_olmo` trapped); `gcal.py:777–790`.
- Probes: the box state (pod id set, committed check cleared), CLAUDE.md edited and `valence_core/m/testing.py` edited each give **103/103**.

What does not hold: gcal's stub runs and gshape's `--out` run still read committed inputs through `m_stages._committed`, even off-record. With one input reported edited, the count drops:

| input reported edited | result |
|---|---|
| `data/olmo/manifest.json` | **81/82** |
| `data/olmo/scaffold_sft.json` | **81/82** |
| `data/m/gates/G-CAL_completability_olmo-sft.json` | **80/82** |
| `results/raw/2026-11-07_p-preread_design-to-code_answers.md` | **68/71** |
| `results/raw/2026-11-06_p_preread_renders.txt` | **90/92** |
| `PROPOSAL-m-gating-campaign-v1_11.md` | **90/92** |

The cause is a "_selftest raised" collapse: gcal's at `precheck` (`gcal.py:216–220`) or at `_identity_olmo` (m `gcal.py:845–848`); gshape's at `inputs_of_record` (`gshape.py:243`, `:250`, `:260`).

This is review round 3's R3-1, second half. R3-1's report leaves "whether gcal's stub runs should keep requiring those three committed inputs" to the seat's reading of N12. The BUILD itself counts an uncommitted edit as a "state of the record": R2-3's fix says "so no state of the record matters" of CLAUDE.md's edit. So the sentence states as settled what R3-1 left open, and the design raw declares it nowhere (`grep`).

K3 (B l.291–292) The site check. **CONFIRMED.**
- It ran on a scratch commit of the final bytes over `9838664`, and the log's end line reads "# end Sat Nov  7 21:01:35 UTC 2026; main HEAD now 98386640d2cb…".
- The eleven tallies (154/154, 67/67, 21/21, 20/20, 46/46, 18/18, 24/24, 846/846, 525/525, 136/136 and p's 103/103) and "every exit 0" equal `site-final2.log` and the eleven `final2-*.out` summary lines.
- The trial PASS and the hashes are there, both rc 0.

K4 (B l.292) "the ten suites of the G-ANL-F3 build's site check". **CONFIRMED.** These are the same ten `run` lines as `results/raw/2026-11-06_ganl-f3_build_sitecheck.txt` (and as the hygiene commit's `2026-11-07_ganl-f3_hygiene_sitecheck.txt`).

K5 (B l.293–296) The rounds' counts: 1/11/11, 0/3/11 and 0/1/7. **CONFIRMED.**
- The three reports' summaries: `p_build_review_r1.md` "1 MAJOR, 11 MINOR, 11 NOTE."; `_r2.md` "0 MAJOR, 3 MINOR and 11 NOTE"; `_r3.md` "0 MAJOR, 1 MINOR and 7 NOTE".
- The review raw's §0 tables hold 23, 14 and 8 rows with those severities (parsed).

K6 (B l.294–296) The MAJOR's description. **CONFIRMED.** It matches r1's M1: on the box after the BUILD commit, the self-test reaches the real load and runs the canonical one-shot G-CAL-p-sft with no go.

K7 (B l.297–298) "Every MAJOR and MINOR is fixed or, where it is the seat's call, declared (P21 / F-p7); each NOTE is applied or disclosed." **IMPRECISE.**
- The review raw's own §0 gives round 1's **m3** as "Fixed in part, disclosed", which is neither fixed nor declared as P21/F-p7. Its residue, the static check's reach, is disclosed in guard.py's docstring and in B §3.
- R3-1's row says "Fixed", which covers the driver's cases. R3-1's second half, the seat's reading of N12 (see K2), is neither fixed nor declared.
- The NOTE half holds: each NOTE row is fixed, flagged (F-p8, F-p9, F-p10), declared (P4/F-p2) or disclosed (N-g, R3-5).

K8 (B l.299–301) Pass 1 is 118 items (98/15/3/2) and pass 2 is 136 (117/14/0/5). **CONFIRMED.**
- Recounted from the two scratch reports, one verdict per item: pass 1 has IMPRECISE A20, A26, A34, A42, A50, B3, B4, B8, B15, B25, B33, B35, B49, B50, B57; FAIL A46, B18, B59; NOT CHECKABLE A10, A51. Pass 2 has 14 IMPRECISE and 5 NOT CHECKABLE (A10, A31, A58, B65, B75).
- The raw's §0 headers and table rows agree.
- NOTE: "in two passes" is true as written. It and the values-check raw's title ("passes 1–2") and header ("Two blind values-check agents") go stale when A's `@@NPASS@@` becomes three; update them together.

K9 (B l.301–302) "Every item re-checked at source and applied; the NOT CHECKABLE items are this raw's §1–§2 (…) and the coordinating session's message (quoted)." **CONFIRMED.**
- Pass 2's 14 IMPRECISE items are each applied in the current texts (§3 below; T12's residue is new, from round 3's later docstring change, not a non-application).
- The NOT CHECKABLE items are exactly those: A10, A31 and B65 are §1–§2, and A58 and B75 are the message.
- §1–§2 are now checked and CONFIRMED (S1–S4). "Written at the commit" means assembled at `9838664` from the bytes to be committed.

K10 (A l.87) The self-test of record is 103/103. The site check ran on a scratch commit of the final bytes over `9838664`, with the ten tallies, p's 103/103, the trial PASS, the hashes and every exit 0. **CONFIRMED** (K1, K3).

K11 (A l.87) The three rounds' counts, and the MAJOR as a write hazard. **CONFIRMED** (K5, K6).

K12 (A l.87) "every MAJOR and MINOR fixed or, where it is the seat's call, declared (P21, F-p7), each NOTE applied or disclosed". **IMPRECISE**, as K7.

K13 (A l.87) Pass 1 is 118 items (3 FAIL, 15 IMPRECISE) and pass 2 is 136 (0 FAIL, 14 IMPRECISE); "every item re-checked at source and applied". **CONFIRMED** (K8, K9).

K14 (A l.87) "The design raw … carries the files, the licence, the register, the PIN register and the FLAGs." **CONFIRMED.** These are B §1, §2, §3, §4 and §5.

## 3. The sentences changed after pass 2

T1 (A l.10–12; pass 2 A12) "each built entry's replacement is declared by qualified name and enforced by identity with the object that name resolves to (a stand-in carrying the name is refused)". **CONFIRMED.**
- `register.py:45–47` (`allowed`, by name); `:100–104` (`v is not _resolve(...)`); the self-test's `_named_like_eligible_p` case is a STOP (`:166`, `:182–187`).
- Note: since R3-5, `_resolve` binds the object at the name's first use in the process and keeps it (`:119–132`); B §3 says so. A's present tense is fine as a summary.

T2 (A l.27–29; A22) "every STOP of the generation loop recorded in it, bar a failure of the checkpoint's own write". **CONFIRMED.**
- The loop's four STOPs go through `_stop`, which writes `stop` (`gcal.py:389–395`): the insulation guard and the boundary (`:465–469`), the proxy's (`:470–475`) and the trigger (`:478–480`).
- `_write`'s GuardStop becomes an unrecordable GcalPStop (`:301–306`).
- The renders STOP is in the precheck, outside the loop (`:211–214`).

T3 (A l.39–43; A28) gcal's order: p's refusals that need no adapter before the load, and on a `--resume` every identity field the adapter does not give; after the load, m's startup (its adapter checks, with two model-free asserts of m's own) and the two adapter-given identity fields, before any generation; the DRIVER and WEIGHTS lines; the adapter through the proxy. **CONFIRMED.**
- Before the load: `p_sessions.py:168–180` (precheck, weights files, then DRIVER and WEIGHTS) and `gcal.py:403–427` (seams, precheck, key set, honesty, checkpoint validity, the pre-load identity diff minus `ADAPTER_FIELDS`, pod change).
- The load is at `:428`.
- After it: `_startup_olmo` with m's `assert_insulated` and its TEMP/cap assert (m `gcal.py:872`, `:878`), then the full identity diff (`:441–446`).
- `_identity_olmo`'s other fields do not depend on the adapter: `ban_sha256` hashes the committed scaffold file (m `gcal.py:845–856`).
- Note: the artifact's write-once refusal comes after the generations. GcalPRefusal's docstring declares it (`gcal.py:104–106`).

T4 (A l.65–67; A45) F-p1: 23 of 384, 17 of them only for a common word near a short gold, one borderline (SFT's `do` for the opposite of 'up'). **CONFIRMED** (recomputed).
- Counts are 4/10/9.
- Class (c): `Januwy` at dpo 8 s2 and instruct 8 s2, `Janaury` at instruct 8 s3, `dn` at dpo 11 s1 and instruct 11 s1.
- `irom` is at instruct 7 s1.
- The other 17 include four clean-pool records: sft 10 s0, sft 10 s1, dpo 4 s1 and dpo 10 s0.
- The borderline record is sft corrupted 11 s2: "Correct: 'do' -- 'do' is the oppossitu of 'up' …".

T5 (A l.74–76; A52) F-p8. **CONFIRMED.**
- ans2:17 reads "**(iii) The proposal pin stays m's;** `proposal_p_sha256` is recorded beside it in every p output". The quoted words are verbatim.
- ans2 §2 is headed "Q1 — the analyzer path".
- `gcal.py:238` passes p's sha as `proposal_sha256`; `:241` sets `proposal_p_sha256`.

T6 (A l.84–86; A59) "the PI's item 3 accepts route (b), the analyzer path, and its build sequence (…) names no analyzer". **CONFIRMED.**
- RESULTS.md:188 and :319 read "route (b) and the register [accepted]. Then build → G-SHAPE-p → G-CAL-p on your go for the box."
- The quote is verbatim, without the final period.

T7 (A l.22–24) `guard`: the roots p refuses ("`data/m`, `data/mf3`, `data/olmo`, `/workspace/models`; the whole repository for a test output") and the link-safe writers. **CONFIRMED.**
- `guard.py:57`, `:117–135` (`_under(p, REPO)`), `:151–206`.
- The self-test refuses `data/`, p's roots, `results/raw`, the root itself, `Data/m` and an empty path.

T8 (A l.78–79) F-p10's summary. **CONFIRMED.**
- `proxy.py:66`.
- `gcal.py:485–486` (the checkpoint) and `:374–375` (the artifact).

T9 (B l.79–86) §3's form paragraph. **CONFIRMED.**
- `substituted` refuses an unknown or unbuilt entry (`register.py:92–94`), a module or attribute set other than the entry's (`:95–97`) and kinds outside `KINDS` (`:98–99`, `:29`).
- It refuses a replacement that is not identical to the declared name's object, bound at first use and kept (`:100–104`, `:119–132`).
- It asserts the single thread (`:105`).
- Restoration is in a `finally` (`:107–113`) and asserted after a normal exit (`:114–116`).

T10 (B l.86–93; B4) The table's module, attributes, replacement, kind and status columns "as `scripts/p_sessions.py hashes` prints them". **CONFIRMED.**
- Parsed, all five columns equal the four `REGISTER` lines in every row. The table omits `reason`, and its lead-in no longer claims it.
- The self-test-note column matches the register, corrupt, keys and schedule self-test lines.

T11 (B l.95–100) What `substitution_problems` finds, over p's production modules and the driver, outside the self-test bodies:
- no write into an m object, bound by a from-import, an import-as, a dotted import or an alias, through a tuple target, a `vars()` subscript or a `.__dict__` subscript;
- no setattr-family call except on `self`, outside `register.py`;
- no `sys.modules` assignment, no `unittest.mock`, no test-double import and no `.classify(...)`;
- "its self-test plants sixteen forms and catches each".

**CONFIRMED.**
- `guard.py:257–355` (`_m_names` adds the dotted root for `import valence_core.m…`); `EXEMPT_FUNCS` is at `:59`; `scanned_files` at `:104–106`.
- `PLANTED` has 16 entries (`:369–386`), all caught (guard self-test PASS), and `import_problems()` returns `[]`.

T12 (B l.100–103; B10, and review round 3's R3-8) "It is a static check of those forms (guard.py names the ones it does not follow: a dynamic import bound to a name, a write through a `sys.modules` lookup, an alias by annotation, walrus or `for` target, a bare-name `classify`); none of those occurs in p's code or driver." **IMPRECISE (minor).**
- After R3-8, guard.py's docstring (`:30–33`) names four more forms, which B omits:
  - "an m object passed as a function argument";
  - a write "through a container";
  - "`getattr(x, '__dict__')`";
  - "a `setattr` bound to another name".
- The first of those occurs in p by design. `register.substituted` receives `corr` (`corrupt.py:112`) and `m_keys` (`keys.py:65`) and writes through `setattr`.
- A `for`-target alias of m modules also occurs, read only: `gshape.import_closure`, `for name, mod in sorted(list(sys.modules.items()))` (`gshape.py:174`).
- `grep` finds no walrus, no `getattr(…, '__dict__')`, no setattr alias, no bare `classify(`, and no dynamic import or `sys.modules` write on m in production code.
- So "none occurs" holds only as "no write through any of them, outside the register's own form".

T13 (B l.107–110) P1. **CONFIRMED.**
- `register.py:81–85`.
- Entry (1)'s sites are `renders_problems` (`gcal.py:211`) and `conditions` (`:234`), both in `precheck`, before `adapter_factory()` (`:428`), and gshape's inputs (`gshape.py:257`), which load no model.
- Entry (2) is the schedule builder only.
- After the load, `run` reaches no register site: `identity` uses constants, and `artifact` takes `pre["conditions"]`.

T14 (B l.119–129; B18) P4. **CONFIRMED** (recomputed).
- m's `_campaign_obj` holds the literal at m `schedule.py:512`.
- p sets the field inside `substituted_keys()` after asserting the literal (p `schedule.py:59–70`).
- m's builder under entry (2), dumped by `dumps_schedule`, differs from p's 18 files in the six campaign files only. Each differs only in `key_template`; with the field restored, the bytes are identical.
- m's `verify_schedule_dir` over `data/p/schedules` under entry (2) reports 14 problems: the six campaign files, `manifest.json differs` and 7 Q-F0 files missing.
- The pre-pass over every path and temp name is at `:97–103`; `write_once_bytes` is at `:110–111`; `refuse_test_out` is at `:94`.

T15 (B l.158–165; B30) P10. **CONFIRMED.**
- The four kinds, recorded with their key, before exit 4: `_stop` (`gcal.py:389–395`); GcalPStop maps to the driver's `except SystemExit` → 4 (`p_sessions.py:191–193`).
- The offending text is recorded for the trigger (`:479–480`). The proxy's STOP keeps the returned text whole: `ProxyStop(..., text=text)` (`proxy.py:61–63`) and `text=getattr(e, "text", None)` (`gcal.py:475`).
- No record is appended for the stopped key, and a stopped checkpoint is never resumed (`:266–267`).
- `launched` stays unchanged before the generation (`:465–469`) and counts the generation after it (`:474`, `:477`).
- The renders STOP comes before any load (`:211–214`).
- A failure of the checkpoint's own write is GuardStop → GcalPStop → 4. Nothing is written through the link (`guard.py:184–206`).

T16 (B l.166–174) P11. **CONFIRMED.**
- `committed_problems` globs every `valence_core/m/*.py` plus p's files, `olmo_hf.py` and the driver (`gcal.py:156–166`). It runs in the non-stub precheck (`:228`).
- The pin's problems become a refusal (`:215`, `:229–230`). It fails closed on OSError, TypeError, SyntaxError, AttributeError, ValueError and IndexError (`:544–547`), and the self-test plants an unavailable source (`:849–853`).
- On a resume, the pre-load diff covers every field but `ADAPTER_FIELDS = ("backend_identifier", "ban_ids_sha16")` (`:92–93`, `:413–419`); the full diff follows the load (`:442–446`).
- `licence_at_run` is in the artifact (`:384`).
- p §4.3 reads "G-CAL-p needs no lock and runs as soon as p is committed and built".
- Seams are refused (`:403–404`).

T17 (B l.179–185; B35) P13. **CONFIRMED.**
- `artifact` calls m's `completability_artifact(ck)` (`gcal.py:360`) and adds `proposal_p_sha256` and `p` (`:365–385`).
- `conditions_1_3` comes from the precheck: per item `n_eligible`, `k` and `changed`, where `changed` is a count (`corrupt.py:138–140`). `c3` names the read of record (`gcal.py:354–356`).
- m `gcal.py:386–387` is `_renders_of_record`'s STOP, and neither it nor `model_free_artifact` is called.
- The write goes through `write_once_bytes` (`:511–512`).

T18 (B l.197–204) P17. **CONFIRMED.**
- The sources map: `gshape.py:139–143`.
- Committed, unedited and package-hash checks: `:281–298`, with m's blobs globbing every `valence_core/m/*.py` (`:211–222`).
- Drift re-read: `:433–437`.
- "An `--out` run (refused anywhere inside the repository)": `refuse_test_out` (`:423`, `guard.py:132`).
- Seams: `:417–419`.
- HEAD's blob: `:225–228`, `:305–320`.
- The trial prints all three units equal.

T19 (B l.209–214) P19. **CONFIRMED.**
- Measured with `-I -B`, the nine production modules leave exactly the 16 listed m modules, and so does the driver. They equal `M_IMPORTED` (`guard.py:62–63`); with `__init__` that is 17 (`M_HASHED`).
- m's `testing.py` is imported only inside `gcal._selftest` (`gcal.py:605`).
- `refuse_out` and `refuse_test_out`: `guard.py:117–135`; the comparison is casefolded (`:109–114`).
- Pass 2's B42 note (the parenthesis follows "every p production module" but lists m modules) still stands.

T20 (B l.217–225; B46, B48) P21. **CONFIRMED.**
- The loop's anchors: `seg` at m `gcal.py:1155` and `adapter.generate` at `:1164`, both in the loop the two substrates share (`:1152–1176`). `temp, cap = _ro.OLMO_TEMP, _ro.STOP_CAP` is at `:1104`, in the OLMo branch.
- The pin: the segment eval (`gcal.py:556–563`), the tuple binding (`:564–569`), the positionals (`:573–575`) and the six keywords (`:576–585`).
- Record keys in full: `mkeys`/`pkeys == RECORD_KEYS`, ten keys (`:589–592`). Values for six only: `shared` (`:593–597`).
- The dynamic 128-call check passes.

T21 (B l.257–261; B68) F-p8. **CONFIRMED.**
- The quote is verbatim, except for ans2:17's bold markers.
- Code's reading is stated as Code's and left to the seat.
- "One argument": `gcal.py:238`. The self-test's assertion at `:660` moves with it, as pass 2 noted.

T22 (B l.267–271) F-p10: "…if the seat reads the log as storage, the log keeps the returned text's sha256 and length instead -- a one-line change before G-CAL-p runs." **IMPRECISE (minor).**
- For the cut log, the production change is one line (`proxy.py:66`; the self-test assertion `proxy.py:141` moves with it).
- Since R3-3, a ProxyStop also stores the returned text whole, post-break part included. It is in the checkpoint's `stop.text` (`proxy.py:63`, `gcal.py:475`, `:391–392`), and `stop.detail` quotes its first 200 characters (`proxy.py:62–63`).
- P10 says so. F-p10 does not, so the scope of the change F-p10 offers is narrower than what the same reading would reach.

## 4. A's figures

F1 (A l.47) p's `package_sha256` `a197d608…31c8` (11 files). **CONFIRMED.**
- An independent recomputation by the PIN's rule (sorted `rel\nlen\n` + bytes over `valence_core/p/*.py`) gives `a197d608cb5e85aadfbbf677f4493286083b112acfb61a032f1f776959b631c8` over 11 files.
- It equals `hashes`, the trial's provenance and the self-test raw's header.

F2 (A l.48) `olmo_hf.py` `df80b79b…92dc`. **CONFIRMED.** `shasum` equals it, and `olmo_hf.py` is not modified (`git status`).

F3 (A l.17) The schedules manifest `999373656ab0…db34`. **CONFIRMED.** `shasum` equals it, as do `hashes` and the site check.

F4 (A l.1, l.16–17) "`valence_core/p/` (11 files)" and "eighteen files and their own manifest". **CONFIRMED** (S2).

F5 (A l.47–48) "the seventeen m files p imports (sixteen modules, measured in a fresh interpreter, and `__init__.py`)". **CONFIRMED.**
- The fresh `-I -B` import set is 16 modules (T19).
- `hashes` prints 17 `LICENCE valence_core/m/` lines.
- These are mf3's ten plus `gcal`, `gshape`, `runner_olmo`, `runner_qwen`, `stages` and `verify` (`valence_core/mf3/guard.py`'s `M_MODULES`).

F6 (A l.46–48) "each by name on one line", "verbatim in the design raw §2". **CONFIRMED** (S4; the INVOCATION line excepted).

F7 (A l.49) "m's `gcal.py` is the hygiene commit's (`993eba1`, `fbae9a01…`)". **CONFIRMED.**
- `git show 993eba1:` and the working tree both hash to `fbae9a01…f6ef`; `18b0111`'s blob is `d60b78e5…02fe`.
- No later commit touches the file.
- m's package hash recomputes to `7756dcf4…49bb` (18 files).

F8 (A l.49–51) "Nothing in `valence_core/m/`, `scripts/m_sessions.py`, `scripts/m_analyze.py`, `olmo_hf.py`, `data/m/` or `data/mf3/` changes." **CONFIRMED.** `git status --porcelain` on those paths is empty.

F9 (A l.52–56) Register statuses: (1) and (2) built; (3) declared, built at step 6; (4) declared, not exercised. **CONFIRMED.** These match the four `REGISTER` lines' `status` fields and `register.py:54–77`.

F10 (A l.60–62) The trial: 2,816 placements per unit and 8,448 in all; none fired or misplaced; `seg+gold` on every placement; the three grids identical; no shape, Layer S or Layer P problem; the placement keys equal G-SHAPE-F0's at HEAD. **CONFIRMED.**
- My `gshape --out` run gives rc 0 and the same lines as the site check's trial: sources `2db8e1adc016cd9b`, closure `23abe773f751bb19`.
- The m-enumeration equality is the self-test's check, as P17 says.

F11 (A l.63–64) "twenty-one PINs (P1–P21)", "Ten FLAGs". **CONFIRMED.** B §4 has P1–P21 contiguous and B §5 has F-p1–F-p10. A lists ten.

## 5. C's headers

H1 `_p-build_selftest.txt` l.1. **CONFIRMED.**
- The package `a197d608…31c8` and the driver `4785e530…0e6c` match the working tree.
- The tally "103/103 p selftest checks pass" is the raw's last line. Exit 0 is my run's rc.
- HEAD is `9838664`.
- "nothing else changed": the raw equals the unscrubbed scratch original (`podwatch/selftest_raw.txt`) with only the repository prefix replaced. No `<home>` or `<tmp>` occurs, so those clauses are vacuous here.

H2 `_p-build_sitecheck.txt` l.1–25 and its sections. **CONFIRMED.**
- The 15 header sha256s equal the working tree.
- "each file byte-identical to the BUILD commit's": the scratch commit `b1c3f6b` holds the 33 files, each identical to the working tree (S3). The 18 schedule files are covered through the manifest.
- The stamps 20:52:46 and 21:01:35 UTC equal `site-final2.log`. "main's HEAD at the run, unchanged at its end" matches that log too.
- The commands equal `run_site.sh`.
- The HANDOFF copy in the worktree is byte-identical to the root's.
- The raw equals `site/sitecheck-final2.txt` with only path scrubs.
- The trial, hashes and self-test sections equal `final2-*.out`, scrubbed.

H3 `_p-build_review.md` l.1–65. **CONFIRMED.**
- "Three blind review agents", rounds 2 and 3 each given the previous report: r2's and r3's headers say so.
- The §0 tallies are K5's.
- §1–§3 equal `p_build_review_r1.md`, `_r2.md` and `_r3.md` after the path scrub. The only differing line, r1:3, differs by the scrub alone: the original's truncated temp root became `<tmp>/…/scratchpad`.

H4 `_p-build_valuescheck.md` l.1–51. **CONFIRMED.**
- "Two blind values-check agents".
- §0's tallies: pass 1 is 118 items (98/15/3/2) and pass 2 is 136 (117/14/0/5). The table rows list exactly the IMPRECISE and FAIL items of each pass, with NOT CHECKABLE grouped.
- §1–§2 equal `p_build_valuescheck_r1.md` and `_r2.md` after the scrub.

H5 No local absolute path in the four raws. **CONFIRMED.**
- `grep` for the home and temp roots (`/Users/`, `/private/`, `/var/folders`, `/tmp/`, `/home/`), the local user name, the session's scratch-root fragments, `Documents/` and `Library/` finds nothing, in B either.
- Paths appear as `<repo>/…` and `<tmp>/scratchpad/podwatch/…`.
- Note: the values-check raw l.621 (pass 2's report, verbatim) keeps `~/.cache/huggingface/.../Olmo-3-1125-32B/.../tokenizer.json`. It is home-relative and carries no username. It falls outside that raw's stated scrub rule (`<repo>`, `<tmp>`) and is harmless; `<home>/…` would match the self-test raw's rule.

## 6. Notes (no verdict)

- **The review raw §0, R3-1's row.** "Fixed: the driver's simulated-box and weights-files cases use literal weights stand-ins" covers R3-1's first fix bullet. Its second bullet, the gcal and gshape self-tests' reads of committed inputs, is the seat's reading of N12 and is not dispositioned there (K2, K7).
- **Code docstrings, not A/B claims.** None changes behaviour:
  - Test outputs are still bounded at `data/` in `gcal.py:129`, `gshape.py:48`, `schedule.py:19` ("nothing under (the repository's) data/", "refused anywhere under the repository's data/") and `p_sessions.py:13`, `:19`, `:361`, `:364` ("never under data/"). Since R3-7, `refuse_test_out` refuses the whole repository: true, but narrower than the code.
  - `p_sessions.py:27–31` (gcal's order) omits R3-6's pre-load comparison of the model-free identity fields on a `--resume`.
  - `gcal.py:157` (`committed_problems`' docstring) still says "the m modules of the licence". The function globs every `valence_core/m/*.py`, as the module PIN at `:53` says.
- **B layout.** Three blank lines before §7 (l.282–284), and §7's second bullet is one unwrapped line. Cosmetic.
- **Pass count.** B §7, the values-check raw's title and its header sentence follow `@@NPASS@@` (K8).

## 7. Corrections in one place

| item | verdict | correction |
|---|---|---|
| K2 (B §7 l.288–290) | IMPRECISE | "Its check count is the same whether p's records are present or absent and whether a pod id is set: [the four mechanisms as written]. It reads six committed inputs as committed: gcal's stub runs read `data/olmo/manifest.json`, `data/olmo/scaffold_sft.json`, G-CAL-OLMo-sft's gate artifact and the seat's answers raw, and gshape's `--out` run reads the answers raw, the renders raw and PROPOSAL-m. With one of them carrying an uncommitted edit, the count drops (68/71 to 90/92, simulated in-process). This is review round 3's R3-1, second half, the seat's reading of N12." |
| K7 (B §7 l.297–298) | IMPRECISE | "Every MAJOR and MINOR is fixed or, where it is the seat's call, declared (P21 / F-p7), with two exceptions. m3 is fixed in part, its residue disclosed (the static check's reach, §3). R3-1 is fixed for the driver's cases, and its second half is the seat's reading of N12, [disclosed above / declared as a FLAG]. Each NOTE is applied or disclosed." |
| K12 (A l.87) | IMPRECISE | "every MAJOR and MINOR fixed (m3 in part, its residue disclosed; R3-1's second half the seat's reading of N12, disclosed) or, where it is the seat's call, declared (P21, F-p7), each NOTE applied or disclosed" |
| T12 (B §3 l.100–103) | IMPRECISE (minor) | "(guard.py names the forms it does not follow: an m object passed as a function argument, a dynamic import bound to a name, a write through a `sys.modules[...]` lookup or a container, an alias by annotation, walrus or `for` target, `getattr(x, '__dict__')`, a `setattr` bound to another name, a bare-name `classify`); outside the self-tests, no write through any of those occurs in p's code or driver, except the register's own (`register.substituted` receives `corr` and `m_keys` and writes through `setattr`)" |
| T22 (B F-p10 l.269–271) | IMPRECISE (minor) | "…the log keeps the returned text's sha256 and length instead -- a one-line change (`proxy.py:66`, its self-test assertion with it) before G-CAL-p runs. The same reading would reach a ProxyStop's `stop` field, which keeps the returned text whole (P10; R3-3), and its `detail`, which quotes the first 200 characters." |

## Summary

57 items: 52 CONFIRMED, 5 IMPRECISE, 0 FAIL, 0 NOT CHECKABLE.
- §1, B §1–§2: 5 items, all CONFIRMED.
- §2, the checks: 14 items, 11 CONFIRMED and 3 IMPRECISE (K2, K7, K12).
- §3, the changed sentences: 22 items, 20 CONFIRMED and 2 IMPRECISE (T12, T22).
- §4, A's figures: 11 items, all CONFIRMED.
- §5, C's headers: 5 items, all CONFIRMED.

Every hash and count recomputes:
- the 33 files of B §1, which are also the scratch commit's 33;
- B §2, which is `hashes` now, its INVOCATION line excepted;
- the 15 site-check header sha256s;
- p's package `a197d608…`, independently;
- `olmo_hf.py` `df80b79b…` and the manifest `99937365…`;
- 16 measured m modules and 17 licence files;
- 103/103 and the eleven site tallies;
- the review counts 1/11/11, 0/3/11 and 0/1/7;
- the values-check counts 118 (98/15/3/2) and 136 (117/14/0/5);
- F-p1's 23 (4/10/9).

Each of pass 2's 14 IMPRECISE items is applied. The four raws are verbatim apart from the path scrubs, and none keeps a local absolute path.

The one substantive finding is K2. B §7 says the self-test's count is the same in every state of the record. gcal's stub runs and gshape's `--out` run still read six committed inputs, and with one of them edited the count drops to 68/71–90/92. This is review round 3's R3-1, second half, which the texts neither declare nor disclose. The same gap makes "every MAJOR and MINOR fixed or declared" imprecise in both texts (K7, K12), along with m3's own "fixed in part, disclosed". The other two are minor:
- B §3's list of the forms the static check does not follow lags guard.py's post-R3-8 docstring by four forms (T12);
- F-p10's "one-line change" does not reach the ProxyStop's whole stored text that R3-3 added (T22).

