# LOCK-p-OLMo-{sft,dpo,instruct} v0.1 -- the blind values-check of the three locks and their entry

*Code's raw, PI date 2026-11-09. A blind values-check of the three locks as first generated and of the LOCK-p v0.1
entry's draft, against HEAD `f8b16d5` and the working tree. 106 items: 93 PASS, 7 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE
(prospective or session history). No value was wrong. Each of the seven was applied before the commit:*

- *#10: each lock now names its own unit's checkpoint as the one whose `lock_sha256` it is.*
- *#17: the locks say a backend change STOPs the stage, and that a same-class box gives the same identifier (m:267),
  in the checker's wording. The same overstatement in the stage's PIN (`stage.py:36-38`) and in the BUILD entry's
  reading (h) is left as written and carried to the seat.*
- *#41: §5 lists all fifteen keys of each checkpoint (the preferred form); the generator asserts the list equals the
  unit's keys in `keys.all_olmo_keys`.*
- *#42: §6 states that its sha256s are over each constant's JSON form, the form the precheck reads, and adds the raw
  bytes' table, whose nine rows equal LOCK-m-F3 §6's.*
- *#91, #96, #98: the entry's wording, as suggested.*

*The fixes were checked by tool, not by a second blind pass: in a process that imports the driver only,
`lock_required` reports no problem for any unit; each lock names all 56 values and carries one BACKEND line,
`641ee466f4553b6a`; 15 of 15 keys are listed per lock; the nine raw-byte rows equal LOCK-m-F3's. The fixes changed the
three files' sha256s; the committed ones are in the entry. The report is verbatim, its local paths scrubbed (`<repo>`,
`<tmp>`) and its headings set one level down.*

## Blind values-check: LOCK-p-OLMo-{sft,dpo,instruct} v0.1 and the draft LOCK-p v0.1 entry

**Summary.** I checked 106 claims by tool against the repository at HEAD `f8b16d5`. The three locks are untracked in the working tree, and the entry is the scratchpad draft `podwatch/lock_entry.md`. Result: **93 PASS, 7 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE.**

Every hash, count and per-checkpoint value holds:
- In a process that imports only the driver, `stage.lock_required` reports no problem for any unit.
- Each lock names all 56 of its values, and §1 to §3 equal those values line for line.
- The BACKEND line equals the BACKEND raw's printed identifier and G-CAL-p's three identities.
- The weights, schedules, scaffold sets, keys, bars and `identity_extra` match the code and the artifacts for all three checkpoints.
- Code's generator, loaded as a module, reproduces each lock byte for byte.

The seven IMPRECISE items are wording problems; no value is wrong. In the locks there are four:
- The header says "every G-TIME-OLMo (p) checkpoint", but each lock binds only its own unit's checkpoint.
- The box-change clause is too broad: the stage catches a backend change, not a box change (m:267).
- §5 lists only part of the keys: 8 of each unit's 15 keys are missing, against m:302's "keys".
- §6's banner sha256s are taken over the JSON form, not the bytes. LOCK-m-F3 records different sha256s for the same m constants.

In the entry there are three:
- The keys summary repeats the §5 problem.
- The label "step 6's m-3" is ambiguous.
- "More valence_core modules" is too broad: only modules outside `valence_core/p` and `valence_core/m` count.

FLAG (j)'s mechanism is confirmed:
- Importing `m_analyze` adds exactly `valence_core/e2d/habit.py`, and the closure grows to 15 files.
- `lock_required` then reports a drift that is not real, while all 56 values stay identical.
- In the stage's own process state, the closure is the recorded 14 files.

### Method

- **Hashes.** For every hashed file I ran `git show HEAD:<path> | shasum -a 256` and `shasum -a 256 <path>`. Every pair agreed. The files were the two analyzers, both proposals, the three G-CAL-p artifacts, G-SHAPE-p, G-ANL-p, the lexicon, the schedules manifest and 18 schedule files, the three scaffold sets, the driver, all 14 `valence_core/p/*.py`, the 18 `valence_core/m/*.py` and `olmo_hf.py`.
- **Python.** All Python ran as `nice -n 19 jlens-qwen36/.venv/bin/python -B` from the repo root. The scripts and their outputs are in `<tmp>/scratchpad/lockvc_blind/`:
  - `chk_a`: imports `p_sessions` only, then runs `lock_required` ×3, `lock_names`, `lock_backend`, the §1 to §3 equality, `identity_extra` and `import_closure`.
  - `chk_b`: imports `p_sessions` then `m_analyze`, then checks the closure, the drift and m's closure sha256.
  - `chk_c`: constants; renders, banners and both packages recomputed by hand; weights; keys; bars; the register table; the PIN sites.
  - `chk_d`: the closure after the precheck's earlier steps and after `gen_locks.py`'s imports, and the values with `m_analyze` imported.
  - `chk_e`: the generator loaded as a module (never as `__main__`) and compared with the lock bytes.
- **Not run.** No model or tokenizer was loaded. No session, gate stage, self-test or driver command was run.
- **Repository untouched.** `find -newer` shows no file in the repo written during the check. My opening `git status --short` may have refreshed `.git/index`'s stat cache; no tracked or working-tree file changed.
- **Skipped.** The placeholders `@@STAMP@@` and `@@VC@@`.

**Line numbers.** "sft:N" is a line of `LOCK-p-OLMo-sft.md`. The DPO and Instruct locks run one line lower from sft:8 on, because they lack the SFT sentence. "E:N" is a line of `lock_entry.md`. "m:N" is a line of `PROPOSAL-m-gating-campaign-v1_11.md`, and "p:N" a line of `PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md`. Pipes inside keys are escaped as `\|` in the table.

### 1. The three locks: shared text and values (each checked in all three locks)

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 1 | sft:1, sft:3: title "LOCK-p-OLMo-{ckpt} v0.1"; "PROPOSAL-p's lock for its unit OLMo-{ckpt}" | PASS | `stage.LOCK_TEMPLATE` = "LOCK-p-OLMo-{ckpt}.md" (stage.py:110); `stage.lock_rel`. A diff of the three locks shows only unit-specific lines differ. |
| 2 | sft:3: "p v0.2 §4.1's chain: G-CAL-p → LOCK-p v0.1 → G-TIME-OLMo (p) → LOCK v0.2 → G-F0m-OLMo (p) → G-PWR → LOCK v1.0 with D_p → the campaign" | PASS | p:84 (§4.1) has the same nodes in the same order. The lock abridges it: p:84 also has "the PI's cap share", "preprint of record pending", the raws and VERDICTS. |
| 3 | sft:3: written on the design seat's answer of 2026-11-08 (`de729c4`, §4) | PASS | `results/raw/2026-11-08_p-step6_design-to-code_answers.md` (sha256 9e178349…9bab, added at de729c4), §4 "Order": … → LOCK-p-OLMo-{ckpt} v0.1 ×3 → G-TIME-OLMo (p) ×3 on the box. |
| 4 | sft:3: the PI's routing of 2026-11-08 quoted in de729c4's close lines, item 2: "build → G-SHAPE-p re-run → G-ANL-p → LOCK-p v0.1 ×3 → G-TIME-OLMo (p) on the box [go]" | PASS | `git show de729c4 -- RESULTS.md`: the p-step6 close quotes item 2. The lock's quote is a byte-exact substring of HEAD:RESULTS.md (checked in Python). |
| 5 | sft:3: entry (9) as the seat's answer to Code's block of 2026-11-08 declares it; the PI's routing of 2026-11-09 quoted at `6b63973`, item 2 ("p: entry (9) on `resume.Identity` [declared]; step 6 continues — …") | PASS | The raw `2026-11-08_open50-entry9_design-to-code_answers.md` (d6296d44…2b97) answers the block at 9624f70 in §2. Its §3 item 2 is byte-exact. The 6b63973 close lines quote it as the routing ("Route as given"). |
| 6 | sft:3: "It licenses G-TIME-OLMo (p) on OLMo-{ckpt}; nothing later" | PASS | `p_sessions.py:96-104`: `qual` and `campaign` are refused until LOCK-p v0.2 and v1.0. |
| 7 | sft:3: "Version v0.1, 2026-11-09, drafted by Code" | PASS | chk_e: the generator `gen_locks.py`, loaded without running main, outputs each lock byte for byte (True ×3). The date is the session date. |
| 8 | sft:3: "committed by path" | NOT CHECKABLE | Prospective. The locks are untracked at f8b16d5 (`git ls-files --error-unmatch` fails). |
| 9 | sft:3: "This file's own sha256 is named in its entry (RESULTS.md, 2026-11-09, LOCK-p v0.1)" | PASS | Checked against the draft: E:7-9 equal `shasum -a 256` of each lock. RESULTS.md does not carry the entry yet. |
| 10 | sft:3: the lock's sha256 "is every G-TIME-OLMo (p) checkpoint's identity_extra lock_sha256" | **IMPRECISE** | `stage.identity_extra(unit, …, lock_bytes)` carries only that unit's lock (stage.py:320-330). The precheck reads `lock_rel(unit)` (:363). All three locks carry the same sentence, so each claims every unit's checkpoint. |
| 11 | sft:6: the disclosure, "p §5.4; F-p3's sentence, verbatim" | PASS | Byte-exact in `results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md` §1. That raw's sha256 e3de1c03…d006 equals `gcal.RULING_SHA256` (added at 38f9974). The text equals `gcal.DISCLOSURE`. p:102 is §5.4; F-p3 corrects its 2026-11-06 date. |
| 12 | sft:7: the SFT sentence "G-CAL-p passed at the bar, 47/64 against 47" (`daca8b0`, §0.1) and its scope; only the SFT lock carries it | PASS | The daca8b0 raw `2026-11-08_p-gcal_design-to-code_answers.md` (4b77e39a…48e1), §0.1, is byte-exact, scope included. The text equals `report.SFT_AT_BAR`. The sft artifact has corrupted 47/64 against a relative bar of 93/128, so the bar is 47. The DPO and Instruct locks lack the line (diff). |
| 13 | sft:8: D_p 2026-12-15 (p §5.3, p:100); each v1.0 is committed by it | PASS | p:100: "D_p: each `LOCK-p-OLMo-{ckpt} v1.0` is committed by 2026-12-15". `analysis.D_P`; `D_P_LINE` = 100. |
| 14 | sft:9, :22-23: the proposal pins (F-p8): `PROPOSAL-m-gating-campaign-v1_11.md` 42ab36ec…6c6b in `proposal_sha256`; `PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md` 42f2977b…3b32 in `proposal_p_sha256` | PASS | Each HEAD blob's sha256 equals the working tree's. F-p8 is ruled at 38f9974 raw §2. Every current `data/p/gates` artifact carries m's pin in `proposal_sha256` and p's in `proposal_p_sha256`. |
| 15 | sft:10: the path is uncached (m:267) | PASS | m:267: "OLMo uncached (Phase B's path)". `identity_extra.locked_path` is "uncached"; `runner_olmo.py:116-117`. |
| 16 | sft:11: the backend identifier of record: m:302; the `BACKEND — characterization` entry of 2026-11-06 (`190ba90`) and its raw; G-CAL-p's three identities | PASS | m:302 lists "the backend identifier" among LOCK v0.1's contents. The entry is at RESULTS.md:2589; `git show 190ba90 --stat` adds it together with `results/raw/2026-11-06_respawn_determinism.txt`. |
| 17 | sft:11: "the stage reads it from this one line, never from code (a box change after this lock STOPs the stage before it generates; …)" | **IMPRECISE** | "Reads … never from code" holds: the precheck runs `lock_backend` on the committed lock (stage.py:372), and the post-load check raises StageStop "nothing generated" (:832-837). The identifier occurs in p code only in the self-test (:1041-1044). But the check compares identifiers built from adapter provenance (versions, GPU name, CUDA, dtype; resume.py:239-245, olmo_hf.py:311-336), which has no host or pod field. m:267 says the identifier "cannot tell two boxes of one class apart". So a same-class new box passes, and only a backend change STOPs the stage. The same wording is in stage.py:36-38. |
| 18 | sft:14: the one line `BACKEND OF RECORD 641ee466f4553b6a` | PASS | HEAD:results/raw/2026-11-06_respawn_determinism.txt:79 reads "backend identifier (printed block): 641ee466f4553b6a". `identity.backend_identifier` is 641ee466f4553b6a in all three G-CAL-p artifacts. `stage.lock_backend` finds exactly one such line in each lock (chk_a). |
| 19 | sft:20, :129: m's analyzer `scripts/m_analyze.py` d347ea0c…5e48 | PASS | The HEAD blob equals the working tree; `G-ANL-p.json` `code.m_analyzer_sha256` matches. |
| 20 | sft:21, :129: p's analyzer `scripts/p_analyze.py` d3758fc4…7008 | PASS | The HEAD blob equals the working tree; `G-ANL-p.json` `code.p_analyzer_sha256` matches. |
| 21 | sft:24, :129: m's package_sha256 7756dcf4…49bb | PASS | Recomputed by hand over `valence_core/m/*.py` (18 files) with `package_sha256_of`'s rule (resume.py:328-350). G-SHAPE-p and G-ANL-p record the same value. |
| 22 | sft:25, :53, :129: p's package_sha256 7a08dbfa…1d24 | PASS | Recomputed by hand over 14 files; `valence_core/p/*.py` in the working tree equals HEAD. |
| 23 | sft:28: G-SHAPE-p's artifact 3c4125a3…1554 | PASS | The HEAD blob equals the working tree. It is the re-run of record at fdd79d8 (F-p12, daca8b0 §2): verdict PASS, recorded packages equal to the current ones. |
| 24 | sft:29: G-ANL-p's artifact 6440468b…b01a | PASS | The HEAD blob equals the working tree (f8b16d5): verdict PASS, recorded analyzers and packages equal to the current ones. |
| 25 | sft:30, :132: p's renders by m's convention (sha16) 6baf494960da4589 | PASS | By hand, `sha256("\n".join(RENDERS_OF_RECORD))[:16]`. p:54; the G-CAL-p artifacts' `renders_sha256` is 6baf4949…3c4c. |
| 26 | sft:31: p's renders by p's convention (sha256) 1551c199…5722 | PASS | By hand, `sha256(json.dumps(renders))`. p:54. |
| 27 | sft:32: the lexicon (F-p11) be41ad97…bab9 | PASS | `data/p/lexicon/web2.txt`'s HEAD blob equals the working tree and `report.LEXICON_SHA256`. "Declared at LOCK-p v0.1": daca8b0 raw §3 and de729c4 raw §3 ("web2 stands"). |
| 28 | sft:33, :89: p's schedules manifest 99937365…db34 | PASS | The HEAD blob equals the working tree. |
| 29 | sft:40-45: the six banner values in §1 | PASS | They equal `stage.banner_shas()`, recomputed by hand as `sha256(json.dumps(v, sort_keys=True, ensure_ascii=False))`. See #42 for the convention. |
| 30 | sft:46, :111: the OLMo ban list sha16 2dd86a453a2275ef (b3's) | PASS | `audit.OLMO_BAN_IDS_SHA16` (audit.py:62). `data/olmo/b3_screen_{sft,dpo,instruct}.json` all have `ban_list.sha16` 2dd86a453a2275ef and n_ids 9. |
| 31 | sft:48: the driver `scripts/p_sessions.py` d91e41e1…a943 | PASS | The HEAD blob equals the working tree. |
| 32 | sft:19-48: §1 holds "the values the stage's precheck requires, verbatim" | PASS | chk_a, driver-only process: `lock_required` problems are [] for each unit. There are 56 values, 29 + 19 licence lines + 8 register lines. §1's 29 lines equal ``- {label}: `{value}` `` in `lock_required`'s order. `stage.lock_names` finds 56 of 56 in each lock. |
| 33 | sft:53: "LICENCE valence_core/p package_sha256 7a08… (14 files, valence_core/p/*.py)" | PASS | HEAD has 14 `*.py` files in `valence_core/p` (`git ls-tree`). The line equals `guard.licence_lines()[0]`. |
| 34 | sft:54-70: the 17 `valence_core/m` licence lines | PASS | Each `git show HEAD:<f> \| shasum -a 256` equals the working tree and the line. The order is `guard.M_HASHED`. A fresh import of every p production module loads exactly `guard.M_IMPORTED` (16 modules) plus `__init__`. |
| 35 | sft:71: `valence_core/adapters/olmo_hf.py` df80b79b…92dc | PASS | The HEAD blob equals the working tree. |
| 36 | sft:50: §2 "(p §4.2; the m shas as they stand), one line each, verbatim" | PASS | p:86, the licence in C2's form; F-p5 (38f9974 raw §6). The §2 block equals the licence values (chk_a). `git diff --stat a665a09 HEAD -- valence_core/m valence_core/adapters/olmo_hf.py` is empty, so no move since the p BUILD needs recording. |
| 37 | sft:74: §3, entries (6)-(9) as declared at de729c4; (9) on `resume.Identity` at 6b63973 §2 | PASS | de729c4 raw §1: Q1 gives (6), Q2 gives (7), Q3 (a) gives (8) and (9), then on `stages._identity`. 6b63973 raw §2 moves (9) to `resume.Identity`. |
| 38 | sft:76: "(6) roots, (7) roots, (8) pins, (9) pins on `resume.Identity`, with Q9 (b)'s roots as parameters (entry (3)'s reason); (8) and (9) are entered and restored together" | PASS | 6b63973 raw §2's last sentence, and "(8) and (9) are entered and restored together". The kinds match `register.table()`. Entry (3)'s reason contains "(b) The roots are parameters wherever m takes them, not a site (the seat's Q9 (b))". |
| 39 | sft:79-86: the 8 REGISTER lines, verbatim | PASS | They equal `"REGISTER " + json.dumps(e, sort_keys=True, ensure_ascii=False)` over `register.table()` (chk_a). The entries are 1, 2, 3, 5, 6, 7, 8, 9: 38f9974 raw §4 struck (4) and entered P21 as (5). |
| 40 | sft:82-86: line references inside the register text | PASS | m gcal.py:1104 is `temp, cap`, :1155 the `seg`, :1164 `adapter.generate`. stages.py:309 reads `DEFAULT_OUT`; stages.py:1106 is `return _resume.Identity(`; resume.py:507 is `Identity(**dict(identity))`. |
| 41 | sft:3, sft:97-99: "It contains m:302's LOCK v0.1 contents for this checkpoint"; §5 "Keys (p §4.1: m's OLMo families under p's prefixes, register entry (2))" | **IMPRECISE** | §5 lists, per template, the G-TIME arm and items, the G-TIME gate schedule and the campaign schedule key. That covers 3 of p §4.1's six families. Missing: the campaign arm `p-olmo\|{ckpt}\|{template}\|{s}`, the G-F0m arm `p-olmo-qual\|…`, `p-olmo-items\|{ckpt}\|{s}`, `p-olmo-items-qual\|{ckpt}\|{s}` and `p-sched\|OLMo-{ckpt}\|qual\|{template}\|0`, which is 8 of each unit's 15 keys (`keys.all_olmo_keys()` has 45 for the three units). m:302 lists "keys" among LOCK v0.1's contents. LOCK-m-F0 v0.1 (LOCK-m-F0.md:1743-1752) lists every stage's keys and defers the OLMo keys to each checkpoint's v0.1 (:1778). The keys that are listed are correct (#58, #67, #76). |
| 42 | sft:101-107: §6 "Banner bytes …", with `` `SESSION_BANNER` sha256 `7f71…` `` and so on | **IMPRECISE** | The values are `stage.banner_shas()`, sha256 over `json.dumps(value, sort_keys=True, ensure_ascii=False)` (stage.py:159-161), not over the bytes. Over the bytes, `SESSION_BANNER` is 6124c724…30ae, `COMMON` 5d915bd8…33b0 and `TOLD_OBJ` a50ca235…56bb. Those are the values LOCK-m-F3.md §6 records for the same m constants (:316-322). Read side by side, the two locks show different sha256s for banners described as "m's, unchanged". |
| 43 | sft:101: "(m's, unchanged; p's records keep m's template strings, p:84)" | PASS | `banner.py`'s licence line equals HEAD. The raw-byte sha256s equal LOCK-m-F3's. p:84: "p's records keep m's unit and template strings". |
| 44 | sft:110: the verifier `valence_core/m/verify.py` (sha256 in §2), run on every record before it is written (G-VER, m:271, m:284) | PASS | verify.py's docstring begins "verifiers: F0m (Qwen) and F0m-OLMo". stages.py:51-53 says `verify.verify_and_mark` "runs on the record BEFORE it is written to the checkpoint" (call at :1177). m:284 defines G-VER; m:271's `template_breakage` is "harness bytes fail G-VER". |
| 45 | sft:111: the scaffold set's ban-id sha16 (b3's), "asserted against `data/olmo/scaffold_{ckpt}.json` … at every stage start (`runner_olmo.olmo_startup`)" | PASS | stages.py:944-951: `_startup` runs once per stage and calls `runner_olmo.olmo_startup` (:98-105), then `olmo_ban_list` (:81-86), then `audit.assert_olmo_scaffold` (audit.py:253-280). It checks the strings against the file's `ban_strings` and the ids' sha16 against 2dd86a45… and b3's record. The file's sha256 itself is bound by the precheck (`lock_required`), not by `olmo_startup`. |
| 46 | sft:114: "Qwen's +9/64 and f1's +.078" | PASS | p:76 (§3.2): "Qwen's (+9/64) and f1's 0.12 figure (+.078)". p:13: Qwen 57/64 against 48/64. The artifacts' `covariate.f1_012_of_record` is "0.078125 (+.078)". |
| 47 | sft:116-125: §9 "Every later bar (m:302, by reference; m's `bars.OLMO_BARS`, each field verbatim)", and the m:N citations in the rows | PASS | m:302 says "every later bar". Each cited line says what the rows attribute to it: m:262 (b3's ban list, the echo class, OLMo session end at the first claim, p0 .02), m:271 (hair triggers, binomial conventions, the G-TIME-OLMo pause), and m:284, m:253, m:308, m:316 and m:330. |
| 48 | sft:126: p's hair trigger `line_break_in_stored_text` (p §2.3), every stored text, enforced in the proxy (the seat's Q5), a STOP, zero base rate by construction | PASS | p:68; de729c4 raw §1 Q5. proxy.py:148-151 raises ProxyStop "HAIR TRIGGER line_break_in_stored_text (p §2.3)"; `has_line_break` covers \n and \r. |
| 49 | sft:129: m's analyzer closure sha256 a3bc7bb9…b22b | PASS | chk_b: `m_analyze.closure_sha256(m_analyze.closure())` gives a3bc7bb9df3d…cb22b, computed in a fresh `-I -B` subprocess (15 modules plus data/olmo/a1_repair_roster.json). `G-ANL-p.json` contains it, and de729c4 raw Q8 names a3bc7bb9…. |
| 50 | sft:132-133: the `identity_extra` field list; p's four fields (`proposal`, `proposal_p_sha256`, `p_package_sha256`, `renders_sha256_p`) through entries (8) and (9) | PASS | `stage.identity_extra` has exactly analyzer_sha256, lock_file, lock_sha256, locked_path, package_sha256, proposal_file, proposal_sha256 and renders_sha16. `identity.IDENTITY_KEYS_OLMO_P` minus m's keys is exactly the four fields. |
| 51 | sft:135-162: the 27 PIN sites by file and line | PASS | grep "PIN (Code" over `valence_core/p/*.py`, `scripts/p_sessions.py` and `scripts/p_analyze.py` (working tree = HEAD) gives the same 27 file:line pairs. §12 is identical in all three locks. |

### 2. Per-checkpoint values

#### LOCK-p-OLMo-sft.md

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 52 | :17: weights allenai/Olmo-3.1-32B-Instruct-SFT, revision 152782ecc41a, files_aggregate_sha256 ecce2061…1ab5, 7 files at /workspace/models/sft | PASS | HEAD:data/olmo/manifest.json["sft"]; `weights_of_record('sft')` has no problems. The aggregate, recomputed from the per-file digests with box_hash_checkpoints.py:45-47's rule, equals the recorded value. |
| 53 | :26: G-CAL-p's artifact 78f46f07…5123 | PASS | The HEAD blob of `data/p/gates/G-CAL_completability_olmo-sft.json` equals the working tree: verdict PASS, unit OLMo-sft. |
| 54 | :27, :114: covariate 15/64 | PASS | The artifact's `covariate.fraction` is "15/64": clean 62/64 minus corrupted 47/64. |
| 55 | :114: PROPOSAL-m's covariate at the shared renders, +5/16 | PASS | p:76. p:13 has clean 62 and corrupted 42, so 20/64. `gcal.M_COVARIATES['sft']`. |
| 56 | :34-39, :90-95: the six schedule files' sha256s | PASS | Each HEAD blob equals the working tree and its manifest entry. |
| 57 | :47, :111: scaffold set `data/olmo/scaffold_sft.json` 0c3592ad…a8 | PASS | The HEAD blob equals the working tree. |
| 58 | :98-99: keys `p-olmo-time\|sft\|A0[s]-OLMo-sft\|{s}`, `p-olmo-items-time\|sft\|{s}`, `p-sched\|OLMo-sft\|time\|A0[s]-OLMo-sft\|0`, `p-sched\|OLMo-sft\|A0[s]-OLMo-sft\|{b}` | PASS | They equal p's `arm_key`, `item_key`, `gate_sched_key` and `sched_key`. Each is m's key with "m-" replaced by "p-". |
| 59 | :117-125: nine bar rows | PASS | Each row's JSON equals the dataclass fields of `bars.OLMO_BARS('sft')`, 9 of 9. The field types are str, int, bool and None. |
| 60 | :132: identity_extra `lock_file` `LOCK-p-OLMo-sft.md`, and the lock's sha256 as `lock_sha256` | PASS | `stage.identity_extra('OLMo-sft', stub=False, lock_bytes=…)`: lock_sha256 c786da46…313a; the other fields as stated. |

#### LOCK-p-OLMo-dpo.md

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 61 | :16: weights allenai/Olmo-3.1-32B-Instruct-DPO, revision fc84a4f69991, c6e5e2ab…3e60, 7 files at /workspace/models/dpo | PASS | The manifest at HEAD; the aggregate recomputed equals the recorded value. |
| 62 | :25: G-CAL-p's artifact 035a204a…4832 | PASS | The HEAD blob equals the working tree: verdict PASS, unit OLMo-dpo. |
| 63 | :26, :113: covariate 9/64 | PASS | The artifact's fraction is "9/64": 61/64 minus 52/64. |
| 64 | :113: PROPOSAL-m's +17/64 | PASS | p:76. p:13: 61 minus 44. |
| 65 | :33-38, :89-94: the six schedule files | PASS | HEAD blob, working tree and manifest agree. |
| 66 | :46, :110: `scaffold_dpo.json` 0c39ce96…574a | PASS | The HEAD blob equals the working tree. |
| 67 | :97-98: keys (the dpo forms) | PASS | They equal p's key functions. |
| 68 | :116-124: nine bar rows | PASS | They equal `bars.OLMO_BARS('dpo')`, 9 of 9. |
| 69 | :131: identity_extra `lock_file` `LOCK-p-OLMo-dpo.md` | PASS | `stage.identity_extra`; lock_sha256 d3baab42…2880. |

#### LOCK-p-OLMo-instruct.md

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 70 | :16: weights allenai/Olmo-3.1-32B-Instruct, revision ac0587e4a774, 0708cef3…e643, 8 files at /workspace/models/instruct | PASS | The manifest at HEAD (8 files, chat_template.jinja included); the aggregate recomputed equals the recorded value. |
| 71 | :25: G-CAL-p's artifact 5e3ef51a…6661 | PASS | The HEAD blob equals the working tree: verdict PASS, unit OLMo-instruct. |
| 72 | :26, :113: covariate 1/8 | PASS | The artifact's fraction is "1/8": 59/64 minus 51/64 = 8/64. |
| 73 | :113: PROPOSAL-m's +17/64 | PASS | p:76. p:13: 59 minus 42. |
| 74 | :33-38, :89-94: the six schedule files | PASS | HEAD blob, working tree and manifest agree. |
| 75 | :46, :110: `scaffold_instruct.json` 21110cea…d9cf | PASS | The HEAD blob equals the working tree. |
| 76 | :97-98: keys (the instruct forms) | PASS | They equal p's key functions. |
| 77 | :116-124: nine bar rows | PASS | They equal `bars.OLMO_BARS('instruct')`, 9 of 9. |
| 78 | :131: identity_extra `lock_file` `LOCK-p-OLMo-instruct.md` | PASS | `stage.identity_extra`; lock_sha256 dae5bc84…2ee1. |

### 3. The draft entry (`podwatch/lock_entry.md`)

| # | claim (condensed, file:line) | grade | evidence |
|---|---|---|---|
| 79 | E:1-3: the heading's citations (p v0.2 §4.1's chain; de729c4 §4's order; the routings quoted in de729c4's close lines, item 2, and at 6b63973, item 2) | PASS | As #2 to #5. |
| 80 | E:3: "three locks at the repository root, written by Code's generator" | PASS | The files are at the root. chk_e: the generator's output equals each file's bytes. |
| 81 | E:3, E:45: "committed by path"; "Not pushed. Committed by path." | NOT CHECKABLE | Prospective. |
| 82 | E:3-4: "Each licenses G-TIME-OLMo (p) on its checkpoint and nothing later" | PASS | As #6. |
| 83 | E:4: "Model-free; nothing ran on a model or the box" | NOT CHECKABLE | Session activity is not in the repo. `gen_locks.py` imports no adapter or model library (inspection); `m_analyze` is model-free by design. |
| 84 | E:6: each lock's sha256 "becomes its G-TIME checkpoint's `lock_sha256`" | PASS | `identity_extra` takes `_sha(committed lock bytes)` for that unit (stage.py:320-330, :363-368, :393). |
| 85 | E:7: `LOCK-p-OLMo-sft.md` c786da46…313a, 24,296 bytes | PASS | `shasum -a 256`; `wc -c` gives 24296. |
| 86 | E:8: `LOCK-p-OLMo-dpo.md` d3baab42…2880, 24,080 bytes | PASS | `shasum -a 256`; `wc -c` gives 24080. |
| 87 | E:9: `LOCK-p-OLMo-instruct.md` dae5bc84…2ee1, 24,404 bytes | PASS | `shasum -a 256`; `wc -c` gives 24404. |
| 88 | E:11-14: §0's contents: the disclosure; "on sft alone, the SFT sentence"; D_p 2026-12-15; the pins; uncached (m:267); one code-block line `BACKEND OF RECORD 641ee466f4553b6a` (190ba90, G-CAL-p's three identities); the weights of record | PASS | As #11 to #18 and #52, #61, #70. The diff shows the SFT sentence only in the sft lock. |
| 89 | E:15-18: "56 per lock: 29 in §1 (…), 19 licence lines in §2 and the register's 8 lines in §3" | PASS | chk_a. The listed §1 items add up: 2 + 2 + 2 + 3 + 1 + 2 + 1 + 1 + 6 + 6 + 1 + 1 + 1 = 29. |
| 90 | E:19-20: §3 records the register as the seat's answer on entry (9) asks | PASS | As #38. |
| 91 | E:21-23: "§4–§9: m:302's LOCK v0.1 contents for the checkpoint: … the keys under p's prefixes …" | **IMPRECISE** | As #41: §5 lists the G-TIME keys and the campaign schedule key only. The rest of the list holds: six schedule files and the manifest, banners, verifier, scaffold assertion, covariate (p §3.2), the nine `OLMO_BARS` rows verbatim, and p's hair trigger. |
| 92 | E:24-25: §10 (analyzer blobs, packages, m's closure `a3bc7bb9…b22b`); §11; §12 | PASS | As #19 to #22, #49, #50 and #51. |
| 93 | E:26-29: checked before the commit in a process that imports the driver: `lock_required` reports no problem for each unit; each lock names all 56 values (as a whole line or in backticks), none missing; each lock's one BACKEND line equals the raw and G-CAL-p's identities | PASS | Reproduced in chk_a (driver-only process): problems are [] ×3, 56 of 56 values are named ×3, and the single BACKEND line equals raw line 79 and the three G-CAL-p identities. |
| 94 | E:30-31: "The stage's full precheck (the lock committed at HEAD, the pod id, the weights of record) runs on the box, for all three units, before the launch" | NOT CHECKABLE | Prospective. The precheck does contain those checks: the committed lock at stage.py:363, the pod id at :374, the weights of record at :357. The driver then checks the weights files (p_sessions.py:224-238). |
| 95 | E:33-34: `stage.gshape_drift_problems` compares G-SHAPE-p's recorded import closure with `gshape.import_closure`, which reads the modules loaded in the calling process | PASS | stage.py:220-233 compares the sources map and the closure. gshape.py:168-197 iterates `sys.modules`. |
| 96 | E:33: "(step 6's m-3 fix)" | **IMPRECISE** | The function landed at d215d5b, the step 6 BUILD. Its review raw has two items called m-3. This check is round 2's MINOR m-3 (`results/raw/2026-11-09_p-step6_build_review.md`:263, recorded fixed at :347). Round 3's m-3 (:419) is a different fix, and stage.py calls it "round 3's m-3" (:355, :819). |
| 97 | E:35-36: "In the stage's own process the closure is the recorded 14 files: the driver's `time` runs the precheck first, with the same module-level imports as G-SHAPE-p's run. So the check is exact where it binds." | PASS | chk_a and chk_d (1): after the driver's imports and the precheck's earlier steps (renders, lexicon, weights), the closure has 14 files and equals `G-SHAPE-p.json` `provenance.import_closure`. `p_sessions.py:224-227` runs `stage.precheck` first. `run_time` reuses the driver's precheck (stage.py:748), so the drift check runs once, before the load. |
| 98 | E:37: "A process that has loaded more `valence_core` modules sees drift that is not there." | **IMPRECISE** | Only modules outside `valence_core/p` and `valence_core/m` count, because gshape.py:169-183 skips both packages. chk_d (2): after `gen_locks.py`'s own module-level imports (extra p and m modules) the closure is still the recorded 14 files. |
| 99 | E:37-38: "Code's lock generator imported `m_analyze`, which loads `valence_core/e2d/habit.py`" | PASS | m_analyze.py:90-91 (`valence_core.session` is already in the closure). chk_b: importing `m_analyze` adds exactly `valence_core.e2d.habit`. The closure grows to 15 files, and `gshape_drift_problems` and `lock_required` then report "its recorded import closure differs … ['valence_core/e2d/habit.py']". |
| 100 | E:38: "and its first try was refused" | NOT CHECKABLE | A past run, not in the repo. |
| 101 | E:38-39: the generator computes every `lock_required` before importing `m_analyze`; "no value depends on that order" | PASS | gen_locks.py:27-33. chk_d (3): with `m_analyze` imported, `lock_required` returns one problem (the drift), but all 56 values equal the driver-only process's, for all three units. |
| 102 | E:40: m's analyzer closure is computed in a fresh interpreter (PIN-1) | PASS | m_analyze.py:1828-1841: PIN-1 runs a `python -I -B` subprocess. |
| 103 | E:40-41: Code reads this as a robustness gap in a check Code built, not a defect in the locks | PASS | A judgment, consistent with #97 and #101: no lock value depends on process state, and the check is exact in the stage's process. |
| 104 | E:41-42: a fresh-interpreter closure for p's check "would move p's package" | PASS | The check lives in `valence_core/p` (stage.py, gshape.py), and `package_sha256` covers every `valence_core/p/*.py` (resume.py:328-350). |
| 105 | E:42: "Nothing is changed before the seat's word." | NOT CHECKABLE | Prospective. Nothing is changed at HEAD: p's package is 7a08dbfa…1d24. |
| 106 | E:44-45: "Next: G-TIME-OLMo (p) ×3 on the box, batched, under the routing … item 2; then the seat's read." | PASS | de729c4 raw §4: "G-TIME-OLMo (p) ×3 on the box, batched, then the seat's read". Routing item 2 has "[go]". |

### Corrections suggested (every IMPRECISE item; there is no FAIL)

**#10 (all three locks, line 3).**
- Now: "This file's own sha256 is named in its entry (RESULTS.md, 2026-11-09, LOCK-p v0.1) and is every G-TIME-OLMo (p) checkpoint's identity_extra lock_sha256."
- Suggested: "This file's own sha256 is named in its entry (RESULTS.md, 2026-11-09, LOCK-p v0.1) and is the identity_extra lock_sha256 of OLMo-sft's G-TIME-OLMo (p) checkpoint." In the other two locks, use OLMo-dpo's and OLMo-instruct's.

**#17 (sft:11; dpo:10, instruct:10).**
- Now: "(a box change after this lock STOPs the stage before it generates; m:302's superseding BACKEND entry is the seat's to route)"
- Suggested: "(a backend change after this lock -- an adapter whose backend identifier is not this line's -- STOPs the stage before it generates; a new box of the same class gives the same identifier (m:267), so this line does not detect it; m:302's superseding BACKEND entry is the seat's to route)"
- The same overstatement is in stage.py:36-38's PIN. Correcting the lock text needs no code change.

**#41 (sft:97-99, with the header's "It contains m:302's LOCK v0.1 contents"; dpo and instruct the same).**

Preferred: complete §5. After the two template lines, add (dpo and instruct take the same lines with their own checkpoint name):

```
  - A0-OLMo-sft: arm (campaign) `p-olmo|sft|A0-OLMo-sft|{s}`; arm (G-F0m-OLMo) `p-olmo-qual|sft|A0-OLMo-sft|{s}`; gate schedule (G-F0m-OLMo) `p-sched|OLMo-sft|qual|A0-OLMo-sft|0`
  - A0s-OLMo-sft: arm (campaign) `p-olmo|sft|A0s-OLMo-sft|{s}`; arm (G-F0m-OLMo) `p-olmo-qual|sft|A0s-OLMo-sft|{s}`; gate schedule (G-F0m-OLMo) `p-sched|OLMo-sft|qual|A0s-OLMo-sft|0`
  - items (campaign) `p-olmo-items|sft|{s}`; items (G-F0m-OLMo) `p-olmo-items-qual|sft|{s}`
```

These values come from p's key functions, as checked in this run.

Alternative: narrow the claim instead.
- §5's heading becomes "## 5. Keys of G-TIME-OLMo (p) and the campaign schedule key (p §4.1: three of m's six OLMo families under p's prefix, register entry (2); the G-F0m-OLMo and campaign arm and item keys are not listed here)".
- The header becomes "It contains m:302's LOCK v0.1 contents for this checkpoint, the keys as §5 limits them, and the seat's additions."

**#42 (sft:101; dpo:100, instruct:100).**
- Now: "## 6. Banner bytes (m's, unchanged; p's records keep m's template strings, p:84)"
- Suggested: "## 6. Banner bytes (m's, unchanged; p's records keep m's template strings, p:84) -- each sha256 is over the value's `json.dumps(value, sort_keys=True, ensure_ascii=False)` in UTF-8 (`stage.banner_shas`, the form the precheck reads), not over the bytes; over the bytes, as LOCK-m-F3 §6 records them, `SESSION_BANNER` is `6124c724758f61109af42141cd2dd576e2fb4e4b9c781e5a22af8be16a6a30ae`, `COMMON` `5d915bd852b5d5984f6997623a1dd614cdf336e9518bd55e6d9916f7dffe33b0` and `TOLD_OBJ` `a50ca2358a40ec9ff0360489c81b93c0eebf40943a8922d27fc5c16424ce56bb`"
- I recomputed all three raw-byte values in this run, and they equal LOCK-m-F3.md:316, :317 and :322.

**#91 (E:21-22).**
- If §5 is completed as #41 prefers, no change is needed.
- Otherwise, now: "§4–§9: m:302's LOCK v0.1 contents for the checkpoint: its six schedule files and the manifest, the keys under p's prefixes, the banner bytes, …"
- Suggested: "§4–§9: m:302's LOCK v0.1 contents for the checkpoint: its six schedule files and the manifest, the G-TIME keys and the campaign schedule key under p's prefixes (the G-F0m-OLMo and campaign arm and item keys are not listed), the banner bytes (each sha256 over the component's JSON form), …"

**#96 (E:33).**
- Now: "(step 6's m-3 fix)"
- Suggested: "(the fix of MINOR m-3 in round 2 of step 6's BUILD review, `results/raw/2026-11-09_p-step6_build_review.md`)"

**#98 (E:37).**
- Now: "A process that has loaded more `valence_core` modules sees drift that is not there."
- Suggested: "A process that has loaded a `valence_core` module outside `valence_core/p` and `valence_core/m` that the driver does not load sees drift that is not there; extra p or m modules, such as the generator's own imports, do not count (`gshape.import_closure` skips both packages)."
