# p package — BUILD (p §8 step 4): the design raw (Code's, 2026-11-07)

*Code's raw for the BUILD entry (RESULTS.md, 2026-11-07). PROPOSAL-p v0.2 (`18b0111`, sha256 `42f2977b…3b32`) and the design seat's answers of 2026-11-07 (`ab40f470…b08b`; ans2). HEAD at assembly `9838664`; Code stamp Sat Nov  7 21:37:53 UTC 2026 (date -u). The PINs are Code's readings, each a flag the seat may strike until LOCK-p v0.1; the FLAGs are for the seat and adjudicate nothing.*

## 1. Files (sha256 of the bytes committed with this raw)

| file | sha256 |
|---|---|
| `valence_core/p/__init__.py` | `2e21845c6c7c263d5736caa00e3178be79a8928a063a923a728b734a4d81079d` |
| `valence_core/p/register.py` | `cfaf26969be3001a76f3c89e801573c50ccb7343c5455036a2d2ac3ec9a2503b` |
| `valence_core/p/corrupt.py` | `1ae7d853989b6563949c8652aa1a200e439381a8121dd6aaab5726a9536bb1bc` |
| `valence_core/p/keys.py` | `2b426a5def376972f9e88a3616b025f0ff8cee242eb0f8df8cf9dc0a41d140ce` |
| `valence_core/p/schedule.py` | `5b5a54c3aa0fb9e2d40cb1608ff36ecd5e3d46a4b603192b066338ab3f56ab56` |
| `valence_core/p/proxy.py` | `889458cf851d517a50f9ff9890387dbd9ed1cdd81b2379a616f846ef5ac01878` |
| `valence_core/p/report.py` | `2b20f82c3f999e00ac9729e1eea1016b14fef5ee740d4720fee3479675dbd687` |
| `valence_core/p/testing.py` | `f5637c3b4cfd0d2b7583a361e8a7e4cd33e99cf252758001c0e7c10ac5bf9f31` |
| `valence_core/p/guard.py` | `a4dc2343a1e11d72f7405d6601b9d20effcedf528f2130e17a6921e96521dae0` |
| `valence_core/p/gcal.py` | `e5618be7a6327c5109645e55c643b022a28e0d82bddf3e1701076944b3e694f3` |
| `valence_core/p/gshape.py` | `6c6d386ba49c126b63925274b887d9a49af2a404aa8e71d6d122e494587c772b` |
| `scripts/p_sessions.py` | `4d75cf03c6a3eb1036cf0c0609403b5795a528a54b22c59324041a0389466bde` |
| `.gitignore` | `99bddf893dc35255aec0d6826dae8b9ed4046c8278146c16a532042e540cdb1d` |
| `.gitattributes` | `e298706e789d2552be6722af69fc1102cfa54bc50248507c788863aa572812eb` |

`data/p/schedules/` (19 files; m's schema names and layout, p's own manifest):

| file | sha256 |
|---|---|
| `data/p/schedules/OLMo-dpo_campaign_A0-OLMo-dpo.json` | `e1b51b382b0e7d20554d7f0d7ccdbc466168f10f74c175c988413b9de2f7cfaf` |
| `data/p/schedules/OLMo-dpo_campaign_A0s-OLMo-dpo.json` | `079ad1eaa0234765c408884d9b77cd1baa67be62830540951426b0213cd10a31` |
| `data/p/schedules/OLMo-dpo_qual_A0-OLMo-dpo.json` | `bf5c76d6f117392cd0c3a5bfdf2241919ab09f735ee343f068703dc0deafb9a9` |
| `data/p/schedules/OLMo-dpo_qual_A0s-OLMo-dpo.json` | `d19515cb17e8c00c66fec4435ced2fb54249e005ad3678f887c200c8b7ca40f7` |
| `data/p/schedules/OLMo-dpo_time_A0-OLMo-dpo.json` | `7127a7e2349d5171a6021e55cdfdcb1bddce1ce2ed2b9e79a073073b6bda1dea` |
| `data/p/schedules/OLMo-dpo_time_A0s-OLMo-dpo.json` | `827aa9ea0c91db9f918b1b8d4cfa25f39d6a34df9efe03eafd067d42808666c5` |
| `data/p/schedules/OLMo-instruct_campaign_A0-OLMo-instruct.json` | `3fd3e58739ac3d1207bf8e5821bc41b43bd23dd4cffc60dac890d154fa93e83c` |
| `data/p/schedules/OLMo-instruct_campaign_A0s-OLMo-instruct.json` | `21c8f4b2edcaff6545d923dc212d8a1dfc1a9dcfaf6c3d260b2f3f103b1bc9b3` |
| `data/p/schedules/OLMo-instruct_qual_A0-OLMo-instruct.json` | `f9ab4ebc9e8b2b6fe3a66f911f72c525535f8595ae6cc9b5e5a213361e56f821` |
| `data/p/schedules/OLMo-instruct_qual_A0s-OLMo-instruct.json` | `77bcc070fa67d151333ea510288954c5f33488d54fac632a79d4020653c73154` |
| `data/p/schedules/OLMo-instruct_time_A0-OLMo-instruct.json` | `c4b06a5124eebffb8cbc974d5d3b2c66e3b6e27864189511ba073450283d7639` |
| `data/p/schedules/OLMo-instruct_time_A0s-OLMo-instruct.json` | `d171b647bb4bd7b3b5c322376cada8a1971ce3eba32e24ac6be3515f4a9f4ab7` |
| `data/p/schedules/OLMo-sft_campaign_A0-OLMo-sft.json` | `56703ec998073cfc3e2371f7d46f759213ed8a7476fe7ac60de2db8ea6136fc3` |
| `data/p/schedules/OLMo-sft_campaign_A0s-OLMo-sft.json` | `8140e3e5201115d1bac3e36013a05c86e016856fddaf40a74751aaaeaecaa209` |
| `data/p/schedules/OLMo-sft_qual_A0-OLMo-sft.json` | `6938e232040a80ebb37fcf50b1e21ee031c55f18be9c4a8acc16d9e5508d83d0` |
| `data/p/schedules/OLMo-sft_qual_A0s-OLMo-sft.json` | `377487dbdc0946c6260b3a1d2cde731962e24266df36065c533443327cb8b120` |
| `data/p/schedules/OLMo-sft_time_A0-OLMo-sft.json` | `1ac7d2920e213148c76977fcbac26273e5725e78aec833fe75a8a4bfe118b537` |
| `data/p/schedules/OLMo-sft_time_A0s-OLMo-sft.json` | `9cd29a32b2a6b13b13651c759eb5b80c0e2c19adf50545a2c6176f5f4d96010e` |
| `data/p/schedules/manifest.json` | `999373656ab0fd76771a254f6d8d7d7da696c1448f8ae49b9e0ababe21eddb34` |

## 2. The licence (p §4.2, C2's form) and the register, as `scripts/p_sessions.py hashes` prints them

```
LICENCE valence_core/p package_sha256 717958dadfbadf489a07a577f625bb7f77314c4b2405ea399ead96738a43b900 (11 files, valence_core/p/*.py)
LICENCE valence_core/m/audit.py sha256 16d0abb91444af1b86dcdabdca919f8e61ce371055fe9581a96d02eb950e50f6
LICENCE valence_core/m/bars.py sha256 e7f028d8a08c70d29b03296276dc292d8a4042a0e20ac8e6f0c70540b91e1d6c
LICENCE valence_core/m/banner.py sha256 730442ca354d8d92fe52135d42506cd83cef2d10deb7dfc23d0a1c204a6d170c
LICENCE valence_core/m/corr.py sha256 74818109a284d203177bae82170cbfa1f2cec8cbd85dfa2f7db018530eb27fce
LICENCE valence_core/m/gcal.py sha256 fbae9a015330677a67c9d401699dc49848fad4a20ce26bb760eb6723eb53f6ef
LICENCE valence_core/m/gshape.py sha256 257e02f43bfe8bb67156129cfb2c270f594ab48b62bd555c627eb2f0b66ca13c
LICENCE valence_core/m/guard.py sha256 6aa5ac2dc7a7e071ad848053aa1a7e73c9539d1d5cb6fe1152b0f11e7a4d8b87
LICENCE valence_core/m/keys.py sha256 a7d5ee3a9cde0deed785df204ae840cb56ee0e1eeefa9192fe1c1b0abb6b3beb
LICENCE valence_core/m/readrule.py sha256 fca9e7329ec42419ed0eaa658d1a954b68db0e05a93cbb6b3a4502f781737a9e
LICENCE valence_core/m/resume.py sha256 78f2fc8eb8b3b16ffa39c6dac7022b37dc98d8d002f50390d5c4540f22bf8fb7
LICENCE valence_core/m/runner_olmo.py sha256 95ebd48f3aa347bfdc9e125b49f244fb2ea2584322c891100b515794d499f317
LICENCE valence_core/m/runner_qwen.py sha256 68bf4be75a99bce26c36e5dfc2edf7ff21caa5d3cf728bc8b16bcf16386e806c
LICENCE valence_core/m/scaffold.py sha256 39d8b32f193c1b0a64705dbb3e5557759f3f046158af85cde31870a53c0921d5
LICENCE valence_core/m/schedule.py sha256 f262f9e0120bcf6e694c0850b56dc3a19ab3c931b28ba92d47009f9f49a72d0d
LICENCE valence_core/m/stages.py sha256 42cb4002a8a790bd13a6d0b0e729cec2a7e619b5ecbaf3241358a7f6b1aa275f
LICENCE valence_core/m/verify.py sha256 6940c2543827b416863e55087becf6c0d31d54cf980b2e996d3999413f8c9254
LICENCE valence_core/m/__init__.py sha256 b5175bcb6a521ef277de105315dd8d2f637a7b03e5d7baf30406dd83d0db35c4
LICENCE valence_core/adapters/olmo_hf.py sha256 df80b79b205c64121187ab0b307e5f35db5bd6632d45940a980c0175b8a092dc
REGISTER {"attrs": ["_eligible_m"], "kind": "eligibility", "module": "valence_core.m.corr", "n": 1, "reason": "p §1.4: corrupt_p is corr.corrupt_m with the frame-word eligible set (p §1.1)", "replacement": "valence_core.p.corrupt.eligible_p", "status": "built at the p BUILD (p §8 step 4)"}
REGISTER {"attrs": ["item_key", "arm_key", "sched_key", "gate_sched_key"], "kind": "keys", "module": "valence_core.m.keys", "n": 2, "reason": "p §4.1: the six OLMo key families under p's prefix, for the schedule builder, the arm streams and the item streams, so that no p stream coincides with an m stream", "replacement": "valence_core.p.keys.{item_key, arm_key, sched_key, gate_sched_key}", "status": "built at the p BUILD (p §8 step 4)"}
REGISTER {"attrs": ["clock_of_record (OLMo units)", "the data/m/... root defaults (run_not_run's ckpt_dir included)", "the v2 posting's per-unit verdicts-dir resolution"], "kind": "clock; roots", "module": "scripts/m_analyze.py (through scripts/p_analyze.py)", "n": 3, "reason": "p §4.4: p's outputs through m's analyzer, the proposal pin kept m's (proposal_p_sha256 beside it)", "replacement": "D_p; data/p/...; data/p/verdicts for the OLMo coordinates", "status": "declared; built with scripts/p_analyze.py at p §8 step 6"}
REGISTER {"attrs": ["the renders source"], "kind": "eligibility", "module": "valence_core.m.gcal", "n": 4, "reason": "p §3.1: the prompt, seeds, grader and generation call at p's renders", "replacement": "p's renders of record (valence_core.p.corrupt)", "status": "declared; not exercised -- G-CAL-p does not call m's run_completability (p's own loop calls m's pieces, p's renders an argument of gcal._task_of), so no attribute of gcal is replaced"}
SCHEDULES MANIFEST data/p/schedules/manifest.json sha256 999373656ab0fd76771a254f6d8d7d7da696c1448f8ae49b9e0ababe21eddb34
```

## 3. The substitution register (p §4.2; ans2 Q0), as built

The one declared form: an attribute of an m module replaced for the duration of one call and restored in a `finally`
(`valence_core/p/register.py`, `substituted`), under the seat's five terms (a)–(e). `substituted` refuses an entry
that is unknown or not built at this step, a module or attribute set other than the entry's, a kind outside
eligibility / keys / pins / Clock / roots, and any replacement value other than the entry's declared one (the object
its declared name resolves to at its first use in the process, kept and compared by identity, term (a)); it asserts
the single thread at the site. Restoration is in a `finally`, so it holds
after an exception, and it is asserted after a normal exit. The four entries: module, attributes, replacement, kind
and status as `scripts/p_sessions.py hashes` prints them (§2), and term (c)'s self-test, Code's note:

| n | module | attributes | replacement | kind | status | term (c)'s self-test (Code's note) |
|---|---|---|---|---|---|---|
| (1) | `valence_core.m.corr` | `_eligible_m` | `valence_core.p.corrupt.eligible_p` | eligibility | built at the p BUILD (p §8 step 4) | `corrupt_p` reproduces §1.2's sixteen renders and equals m's on items 0 and 12; `corr._eligible_m` is m's after the call, an exception included |
| (2) | `valence_core.m.keys` | `item_key`, `arm_key`, `sched_key`, `gate_sched_key` | `valence_core.p.keys.{item_key, arm_key, sched_key, gate_sched_key}` | keys | built at the p BUILD (p §8 step 4) | with m's own keys (no substitution) p's builder reproduces `data/m/schedules/`' eighteen OLMo files byte for byte; restoration after the block, an exception included |
| (3) | `scripts/m_analyze.py (through scripts/p_analyze.py)` | `clock_of_record (OLMo units)`; `the data/m/... root defaults (run_not_run's ckpt_dir included)`; `the v2 posting's per-unit verdicts-dir resolution` | `D_p; data/p/...; data/p/verdicts for the OLMo coordinates` | clock; roots | declared; built with scripts/p_analyze.py at p §8 step 6 | step 6's |
| (4) | `valence_core.m.gcal` | `the renders source` | `p's renders of record (valence_core.p.corrupt)` | eligibility | declared; not exercised -- G-CAL-p does not call m's run_completability (p's own loop calls m's pieces, p's renders an argument of gcal._task_of), so no attribute of gcal is replaced | none (not exercised) |

No other site exists: `guard.substitution_problems` (term (e)'s static form), run over p's production modules and
`scripts/p_sessions.py`, finds outside the self-test bodies no write into an object imported from `valence_core.m`
(bound by a from-import, an import-as, a dotted import or an alias assignment; through a tuple target, a `vars()` or
a `.__dict__` subscript), no call named `setattr`/`delattr`/`__setattr__`/`__delattr__` with anything but `self` first
outside `register.py`, no assignment into `sys.modules`, no `unittest.mock`, no test-double import and no
`.classify(...)` call; its self-test plants sixteen forms and catches each. It is a static check of those forms;
guard.py's docstring names the ones it does not follow (an m object passed as a function argument, a dynamic import
bound to a name, a write through a `sys.modules` lookup or through a container, an alias by annotation, walrus or
`for` target, `getattr(x, '__dict__')`, a `setattr` bound to another name, a bare-name `classify`). No write through
any of them occurs in p's code or driver except the register's own: `register.substituted` receives m's module as its
argument by design.

## 4. The PIN register (Code's readings, declared at the p BUILD; each a flag the seat may strike until LOCK-p v0.1)

- **P1 (register).** "Single-threaded" (term (d)) is asserted as: the calling thread is the main thread and no other
  Python thread is alive (`threading.active_count() == 1`). Every site built at this step runs before any model
  load: the renders, the schedules, and G-CAL-p's §3.2 conditions (computed in its precheck); see F-p9 for the arm
  and item streams at step 6.
- **P2 (corrupt).** The quote rule is m's (each `'` toggles the span; an odd count is refused, as `_eligible_m`
  refuses it). "Its first word" is the text's first maximal run of ASCII letters, a frame word unless it lies in a
  quoted span (no CORR item's does). Words match FUNCTION_WORDS case-insensitively (v0.2 §1.1's words; inert on the
  pool of record, referent item 131).
- **P3 (keys).** Each p key is m's own key function's result with its leading `m-` replaced by `p-`: m's
  validation and construction run unchanged, only the prefix differs. A unit outside the three OLMo units passes
  through to m's function unchanged (m's builder iterates every built unit under the substitution; p writes the
  OLMo files only).
- **P4 (schedule).** m's `_campaign_obj` writes its `key_template` field as the literal `m-sched|{unit}|{arm}|{b}`
  (`valence_core/m/schedule.py:512`), not through `keys.sched_key`. Under entry (2) the cells are drawn from
  `p-sched|…`, so p sets that one field, after m's call and inside the substitution, to the active `sched_key`'s
  template form (asserted to be m's literal before the change). Under m's keys the field is m's literal byte for
  byte, so term (c)'s equality holds; no cell, π or key is touched. The field is p's own output, set outside the
  register's form (it substitutes no m attribute): among the eighteen files, the six campaign files' key templates
  are the only bytes that differ from what m's builder writes under entry (2) (m's own `verify_schedule_dir`, run
  over p's directory, would also report p's manifest and m's Q-F0 files, which p does not write). The canonical write is `data/p/schedules`; a test
  write (`--out`) goes through `guard.refuse_test_out` (never inside the repository); every path and temp name is
  checked for a link or non-file before the first file is written, and every file is written once through
  `guard.write_once_bytes`.
- **P5 (proxy).** "Line break" is `\n` or `\r` (§2.3's trigger reads both). The cut text is the text before the
  first line break with trailing whitespace removed, as the adapter strips its decoded text (`olmo_hf.py:286`); the
  token ids run through the first id prefix whose decoded text holds a line break after content. A result with no
  line break is the adapter's own object, unchanged. A tokenizer whose decode cannot place the break is a STOP, never
  a guessed cut.
- **P6 (report, §2.3's counters).** Control characters are Unicode category Cc minus `\n` and `\r` (tab included).
  The listed forms and m:258's eight declared strings (placeholders as wildcards) match at the start of the first
  line, case as written; `=== … ===` is a whole first line. Refusals match case-insensitively, straight or curly
  apostrophe. `corrupted_spelling` is §2.3's rule as written, with one reading: a word is §1.1's, and a gold variant
  is compared only when it is itself one such word (a digit string has no spelling; `twenty-four` is two words). The
  counters tabulate the stored records; G-CAL-p's artifact adds `cap_hits_returned_in_cuts` (a cut sets the stored
  `cap_hit` false, §2.2).
- **P7 (G-CAL-p, identity).** m's `_identity_olmo` keys as m writes them: `proposal_sha256` p's (the document the gate
  runs under; the gate line checks it committed; F-p8), `renders_sha256` p's renders by m's convention (ans2 Q3 (c)),
  `package_sha256` m's package (the code that runs). p adds `proposal` ("PROPOSAL-p"), `proposal_p_sha256`,
  `p_stage`, `p_package_sha256`, `renders_sha256_p`, `proxy`, `olmo_hf_sha256` and `driver_sha256`, so a resume never
  splices two adapters or drivers. m's stage, procedure and on_fail strings stay as m writes them -- Code's extension
  of ans2 Q4 (ii), which keeps m's unit and template strings in p's records -- and p's stage name, its procedure
  difference (the proxy) and its failure consequence are in the artifact's `p` block, with `proposal_p_sha256` at
  the top level.
- **P8 (G-CAL-p, strict grade).** p §3.1's "a hit iff the first word of the normalized text is a gold variant",
  read for a variant that f0's `normalize` turns into several words (`twenty-four` → `twenty four`) as the text's
  leading words being that variant's words; for a one-word variant it is the first word, as written.
- **P9 (G-CAL-p, clean-pool identity).** Per clean key, the fields seed, task, text, n_tok, cap_hit, stop_reason and
  hit are compared with G-CAL-OLMo's committed gate artifact (`data/m/gates/G-CAL_completability_olmo-{ckpt}.json`,
  read from its blob at HEAD; a refusal before any load if it is not committed and unedited), and the two
  identities' generation-path fields are recorded side by side. A non-identity is the seat's flag (p §3.1), never
  a bar.
- **P10 (G-CAL-p, STOPs).** Every STOP of the generation loop -- the hair trigger, rule 28(d)(a)'s boundary, the
  proxy's, the insulation guard's -- is recorded in the checkpoint's `stop` field with its key (and the offending text, for
  the trigger) before the stage exits 4; no record is appended for that key, and a stopped checkpoint is never
  resumed. A STOP before the generation (the boundary, the insulation guard) counts nothing as launched for its key; a
  STOP after it (the proxy's, the trigger) counts the generation, and the proxy's keeps the returned text whole. Renders
  of record that do not reproduce are a STOP too (a pinned figure, m's taxonomy), before any load. A failure of the
  checkpoint's own write (a link planted at its path or temp name during the run) is a STOP that cannot be recorded
  there; the stage exits 4 and the checkpoint on disk is the last good write.
- **P11 (G-CAL-p, the code of record).** A non-stub run requires p's package files, m's whole package (every
  `valence_core/m/*.py`, as the identity records m's package hash), `olmo_hf.py` and the driver committed at HEAD
  with identical working-tree bytes (rule 27), refused before any load; the generation call's pin (P21) is checked in
  the precheck too, failing closed (a refusal) if it cannot be computed; on a `--resume`, every identity field the
  adapter does not give is compared with the checkpoint before the load, the two it gives (the backend identifier,
  the ban ids) after it;
  the licence's values at the run are recorded in the artifact (`licence_at_run`), for LOCK-p v0.1 to be read
  against. G-CAL-p needs no lock (p §4.3), so no lock line is checked. Seams (`startup`, `wrap`) are refused on a
  canonical run.
- **P12 (G-CAL-p, printing).** The PROVENANCE line prints m's fields and the pod id (the checkpoint's provenance
  entry carries it, as m's does). The gate line is m's `gate_line` for stage `G-CAL-p-{ckpt}` on p's proposal; its
  analyzer field reads `present <sha16> -- not read by G-CAL`, the sha16 being `scripts/m_analyze.py`'s, p's
  analyzer not existing before step 6.
- **P13 (G-CAL-p, artifact).** p's builder (p §3.1) calls m's `completability_artifact`, a pure function of the
  checkpoint that reads no renders, for the fields of m's schema, and adds `proposal_p_sha256` and the `p` block
  (with §3.2's conditions (1)–(3), computed in the precheck before any load: per item n_eligible, k and the number
  of changed positions, and the seat's read of record).
  m's model-free builder (`model_free_artifact`, whose renders step `_renders_of_record` stops on any renders but m's,
  `gcal.py:386–387`) is not called. The write is p's link-safe write-once writer (`guard.write_once_bytes`), the
  bytes m's `write_json_once` would write.
- **P14 (G-SHAPE-p, verdict).** m's `gshape._stop_reasons` by import over the OLMo units' grid, the shape problems,
  Layer S and the OLMo identity, with exactly `coverage:Q-F0` removed (m's function adds it for every built unit
  absent from the grid; p places no Q-F0 render), plus `p-guard` on a Layer P problem. Never a copy of m's
  function.
- **P15 (G-SHAPE-p, Layer S).** m's `runner_scope_problems` as written, its Qwen half included (p runs no Qwen
  session; the check is m's, unchanged); the artifact points at the runners' dynamic evidence (m's self-test, p's
  proxy self-test).
- **P16 (G-SHAPE-p, renders source).** The renders placed are read from the committed renders raw's
  `json.dumps(renders)` line (the file of the seat's read of record, ans2 §0; sha256 pinned), asserted equal to
  `corrupt.RENDERS_OF_RECORD` and to `corrupt_p`'s recomputation under both sha conventions. p has no model-free
  G-CAL artifact: condition (3) is the seat's read.
- **P17 (G-SHAPE-p, the run of record).** The canonical run requires every file of the sources map (p's package,
  the licence's m modules, G-SHAPE-F0's scoring stack, `olmo_hf.py`, p's tooling) and of the import closure outside
  both packages committed at HEAD and unedited, p's package hash equal to the hash of its committed blobs, and m's
  package hash equal to the hash of m's committed blobs (every `valence_core/m/*.py`, `testing.py` included), as
  G-SHAPE-F0's does; sources and closure are re-read before the write (drift is a refusal). An `--out` run (refused
  anywhere inside the repository) skips that check and is never of record; a run with any seam set never
  writes the canonical path. Each unit's placement keys are compared with G-SHAPE-F0's artifact as HEAD's blob holds
  it, descriptively (a key carries no render), and the self-test checks them against m's own enumeration directly.
- **P18 (driver, weights files).** The pre-load weights-files check is p's own, to `scripts/m_sessions.py`'s
  `olmo_weights_problems` semantics: every file the committed manifest lists for the checkpoint a regular file at its
  byte count, nothing unlisted, the entry's path a directory; a size check, never a re-hash (the respawn protocol's
  step (i) re-hashes the volume once per box). p's licence therefore binds no m script.
- **P19 (guard).** `M_IMPORTED` is measured: the sixteen `valence_core.m` modules a fresh interpreter (`-I -B`)
  holds after importing every p production module (audit, banner, bars, corr, gcal, gshape, guard, keys, readrule,
  resume, runner_olmo, runner_qwen, scaffold, schedule, stages, verify); with `__init__.py`, the licence's seventeen m
  files. m's `testing.py` is imported by p's self-tests only. `refuse_out` refuses `data/m`, `data/mf3`, `data/olmo`
  and `/workspace/models` for any p output; `refuse_test_out` also refuses the whole repository for a test or stub
  output. The root comparison is case-insensitive (the laptop's volume is), so it only ever refuses more.
- **P20 (roots).** All five `data/p` roots are admitted at the BUILD (schedules, gates, reports, ckpt, verdicts), in
  mf3's form; `data/p/ckpt/**` is `-diff` (m:318 by reference).
- **P21 (G-CAL-p, the generation call).** m's prompt and generation call live inline in `run_completability`'s
  loop, which both substrates share (`gcal.py:1155`, `:1164`; its OLMo branch binds `temp, cap` at `:1104`), not
  importable alone, and `run_completability` cannot run for p (its precheck reads a
  model-free artifact on m's renders, it writes m's roots, its identity has no p field, and it has no hair trigger).
  So p's loop restates the call, with the segment from m's `SEGMENT_FORM`, and the self-test pins it to m's two ways:
  an AST comparison with `run_completability` (the segment form; the positional arguments; the six keywords, m's
  `temp, cap` bound to `OLMO_TEMP, STOP_CAP` in its OLMo branch; the record literal's keys in full and six of its ten
  values -- seed, task, text, n_tok, cap_hit, stop_reason) and a dynamic
  check that all 128 calls p makes carry m's procedure. Register entry (4) is not exercised. FLAG F-p7.

## 5. FLAGs for the seat (descriptive; none blocks G-SHAPE-p)

- **F-p1 (§2.3's corrupted-spelling counter).** On G-CAL-OLMo's 384 committed records the rule as written counts
  4/10/9 records (sft/dpo/instruct), 23 in all. Five are §0.3's class (c) (`Januwy` ×2, `Janaury`, `dn` ×2) and one
  is a misspelling of the model's own (`irom`, instruct item 7 s1); the other 17, four of them clean-pool records,
  count only a common word within distance 2 of a short gold (`the`/`two`, `the`/`three`, `true`/`three`,
  `on`/`iron`, `in`/`iron`, `do`/`down`), one of them borderline (sft item 11 s2 gives `do` as its answer for the
  opposite of 'up'). `Janbaa` and `Janyooar`, and `Ther qro abov two dsys in a wemk`, class (c) by §0.3, are not
  counted (no word within distance 2 of a gold). The counter decides nothing (rule 23); a narrower definition is the
  seat's to give before G-CAL-p's counters are reported, or the counts stand as defined.
- **F-p2 (schedules).** P4's one field. With p's keys, one gate schedule (`OLMo-sft_qual_A0s-OLMo-sft.json`) draws
  m's π, `[3, 1, 0, 2]`, and so m's cells: a coincidence of two different streams (`permutation(4)` takes 24
  values), recorded, not a shared stream. Every other file's cells differ from m's, and so does every other gate
  file's π (the six campaign files carry none). Each file's key template names `p-sched|…`.
- **F-p3 (§5.4's date; referent item 85, `18b0111`).** G-CAL-p's and G-SHAPE-p's artifacts carry §5.4's disclosure
  with the date §5.4 gives (2026-11-06). If the seat rules the date, the constant changes before G-CAL-p runs.
- **F-p4 (register entries (3) and (4)).** (3) is built with `scripts/p_analyze.py` at step 6; its kinds are the
  Clock and the data roots. (4) is declared and not exercised (§3; P21).
- **F-p5 (the licence moves with m).** The licence names the sixteen m modules p imports: mf3's ten and six beyond
  them (`gcal.py`, `gshape.py`, `runner_olmo.py`, `runner_qwen.py`, `stages.py`, `verify.py`). The coordinating
  session's hygiene commit (`993eba1`) moved `valence_core/m/gcal.py`'s sha256 `d60b78e5…` → `fbae9a01…` and m's
  package hash `60199b36…` → `7756dcf4…` (self-test code only). The licence lines in §2 are this BUILD's, taken at
  its commit; LOCK-p v0.1 names the values current at its writing, and G-SHAPE-p re-runs first if its sources map
  differs then, as G-SHAPE-F0's and G-SHAPE-F3's rule has it.
- **F-p6 (the departure).** Disclosed at `18b0111`: the package was written in the working tree while v0.2's
  referent check ran, before step 3's commit.
- **F-p7 (§3.1's "by import or by §4.2's register").** P21: the generation call is restated, pinned to m's by the
  AST comparison and the dynamic check, and register entry (4) is not exercised. The alternative -- running m's
  `run_completability` itself -- would need register entries the seat has not declared (m's gcal roots, its
  identity, its model-free check) and would lose p's hair trigger; the seat's to rule.
- **F-p8 (the proposal pin in G-CAL-p's identity).** ans2 Q1 (iii): "The proposal pin stays m's; `proposal_p_sha256`
  is recorded beside it in every p output". Code reads the rule's scope as the analyzer's (Q1 is the analyzer path).
  G-CAL-p's identity carries p's sha256 in `proposal_sha256` (the document the gate runs under, as its gate line
  checks) and in `proposal_p_sha256`. The scope is the seat's to rule; the change, if ruled, is one argument before
  G-CAL-p runs.
- **F-p9 (ahead of step 6).** The single-thread assertion (P1) is met at every site built here, before any model
  load. Entry (2) names the arm and item streams too, which m's scaffold draws per session after the load, where a
  library's background thread may be alive; m's stage roots (`data/m/ckpt`, reports, schedules) are not in entries
  (1)–(4). Each is for step 6's design. (p's `.gitignore` admits the checkpoints' pod-change set-asides, as m's
  does.)
- **F-p10 (the cut log).** Each proxy cut is logged in the checkpoint and the artifact with the returned text
  (`text_returned`), the part after the break included, and a ProxyStop keeps the returned text whole in the
  checkpoint's `stop` field, so the seat's read of every generation (rule 25) can see what was cut; nothing of it is
  stored as the record's text, graded or shown to a later round. §2.2 says "Nothing after the cut is stored"; if the
  seat reads the log or the stop field as storage, both keep the returned text's sha256 and length instead -- a small
  change before G-CAL-p runs.

## 6. Scope, by §8's step numbers

This BUILD is p §8 step 4's list. `scripts/p_analyze.py`, G-ANL-p and register entry (3)'s self-test are step 6's:
before any LOCK-p v0.1 and after LOCK-m-F3 v0.1 (p §4.3); p §4.4: "if every checkpoint fails G-CAL-p, no p analyzer
is built". The OLMo gate-stage and campaign drivers (G-TIME-OLMo (p), G-F0m-OLMo (p), the campaign) are step 6's too,
by §8's list; p §6.2 gives the reason, G-CAL-p first as it "decides whether anything else of p is built". The driver
refuses `time`, `qual` and `campaign` (exit 2), each named. The coordinating session confirmed this scope on
2026-11-07, by message: "Confirmed: follow p v0.2's §8 as written. My brief was wrong to put scripts/p_analyze.py in
the BUILD." No LOCK-p file is written; nothing runs on a model or the box.



## 7. Checks before the commit

- **The self-test of record:** `scripts/p_sessions.py --selftest`, 103/103, on the final bytes
  ([`_p-build_selftest`](2026-11-07_p-build_selftest.txt)). Its count does not depend on the pod id, the canonical
  roots, CLAUDE.md or the presence of `data/p/schedules` (the schedules check is unconditional; the gcal cases run with
  the pod id removed or a stand-in, the canonical roots at a scratch root and the loader trapped). It does depend, by
  design, on its inputs of record, read from their committed blobs: an uncommitted edit to the OLMo manifest or a
  scaffold file, G-CAL-OLMo's gate artifact, the seat's answers raw, the renders raw or PROPOSAL-m fails it (pass 3
  measured counts of 68/71 to 90/92), as those inputs must be the committed ones.
- **The site check** ([`_p-build_sitecheck`](2026-11-07_p-build_sitecheck.txt)), on a scratch commit of the final
  bytes over main's HEAD `9838664` (unchanged during the run): the ten suites of the G-ANL-F3 build's site check
  pass (154/154, 67/67, 21/21, 20/20, 46/46, 18/18, 24/24, m_sessions 846/846, m_analyze 525/525, mf3_sessions
  136/136), p's self-test 103/103, a G-SHAPE-p trial PASS and the hashes, every exit 0.
- **A blind code review in three rounds** ([`_p-build_review`](2026-11-07_p-build_review.md), with Code's
  disposition of every item): round 1, 1 MAJOR, 11 MINOR, 11 NOTE -- the MAJOR a write hazard in the self-test (on
  the box after the commit, the driver's self-test would have reached the real model load and run G-CAL-p's
  one-shot gate canonically, with no go); round 2, 0 MAJOR, 3 MINOR, 11 NOTE; round 3, 0 MAJOR, 1 MINOR, 7 NOTE.
  Every MAJOR and MINOR is fixed, declared where it is the seat's call (m10: P21, F-p7) or disclosed (m3: the static
  check's reach, named in guard.py; R3-1's second half: the self-test's inputs of record, above); each NOTE is applied
  or disclosed.
- **A blind values-check in three passes** ([`_p-build_valuescheck`](2026-11-07_p-build_valuescheck.md)): pass 1,
  118 items (98 CONFIRMED, 15 IMPRECISE, 3 FAIL, 2 NOT CHECKABLE); pass 2, 136 items (117 CONFIRMED, 14 IMPRECISE, 0
  FAIL, 5 NOT CHECKABLE); pass 3, on the complete texts, 57 items (52 CONFIRMED, 5 IMPRECISE, 0 FAIL). Every item
  re-checked at source and applied; the earlier passes' NOT CHECKABLE items were this raw's §1–§2 (checked at pass 3)
  and the coordinating session's message (quoted).
