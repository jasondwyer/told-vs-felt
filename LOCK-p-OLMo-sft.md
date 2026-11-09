# LOCK-p-OLMo-sft v0.1

*PROPOSAL-p's lock for its unit OLMo-sft (p v0.2 §4.1's chain: G-CAL-p → LOCK-p v0.1 → G-TIME-OLMo (p) → LOCK v0.2 → G-F0m-OLMo (p) → G-PWR → LOCK v1.0 with D_p → the campaign). Written by Code on the design seat's answer of 2026-11-08 (`de729c4`, §4) and the PI's routing of 2026-11-08 quoted in `de729c4`'s close lines, item 2 ("build → G-SHAPE-p re-run → G-ANL-p → LOCK-p v0.1 ×3 → G-TIME-OLMo (p) on the box [go]"), with entry (9) as the seat's answer to Code's block of 2026-11-08 declares it and the PI's routing of 2026-11-09 quoted at `6b63973`, item 2 ("p: entry (9) on `resume.Identity` [declared]; step 6 continues — build → G-SHAPE-p re-run → G-ANL-p → LOCK-p v0.1 ×3 [go]"). It contains m:302's LOCK v0.1 contents for this checkpoint and the seat's additions. It licenses G-TIME-OLMo (p) on OLMo-sft; nothing later. Version v0.1, 2026-11-09, drafted by Code and committed by path. This file's own sha256 is named in its entry (RESULTS.md, 2026-11-09, LOCK-p v0.1) and is the identity_extra lock_sha256 of OLMo-sft's G-TIME-OLMo (p) checkpoint.*

## 0. Standing
- **Disclosure** (p §5.4; F-p3's sentence, verbatim): *pre-registered on 2026-11-07 (PROPOSAL-p v0.2, `18b0111`; v0.1 routed 2026-11-06), after the shared dose of PROPOSAL-m failed completability on this lineage at G-CAL-OLMo on 2026-11-06; the corruption rule changed once, from the gate's read, before any session ran.*
- **The SFT sentence** (the seat's answer of 2026-11-08, `daca8b0`, §0.1, declared for every entry, lock line and posted sentence that reports OLMo-SFT's A0 outcome): *G-CAL-p passed at the bar, 47/64 against 47*.
- **D_p:** 2026-12-15 (p §5.3, p:100); each LOCK-p-OLMo-{ckpt} v1.0 is committed by it.
- **The proposal pin** (F-p8): `PROPOSAL-m-gating-campaign-v1_11.md` sha256 `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b` in every p output's `proposal_sha256`; PROPOSAL-p `PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md` sha256 `42f2977b941bc016d3155ba9e34828f1b050121d9f18a9e3307e3f7023cf3b32` in `proposal_p_sha256`.
- **The path:** uncached (m:267).
- **The backend identifier of record** (m:302; the `BACKEND — characterization` entry of 2026-11-06, `190ba90`, its raw `results/raw/2026-11-06_respawn_determinism.txt`; G-CAL-p's three identities): the stage reads it from this one line, never from code (a backend change after this lock -- an adapter whose backend identifier is not this line's -- STOPs the stage before it generates; a new box of the same class gives the same identifier (m:267), so this line does not detect it; m:302's superseding BACKEND entry is the seat's to route)

```
BACKEND OF RECORD 641ee466f4553b6a
```

- **The weights of record:** allenai/Olmo-3.1-32B-Instruct-SFT revision `152782ecc41a`, files_aggregate_sha256 `ecce20615022c2038199b7959ce1b239d6267270fb6a88e375f9d8da06f01ab5`, 7 files at `/workspace/models/sft`.

## 1. The values the stage's precheck requires, verbatim (`valence_core.p.stage.lock_required`)
- m's analyzer (scripts/m_analyze.py): `d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48`
- p's analyzer (scripts/p_analyze.py): `d3758fc4543b174bd8e923781f094a55c56c19cecee08e091a92c9eadf577008`
- PROPOSAL-m (m's proposal pin, F-p8): `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b`
- PROPOSAL-p (proposal_p_sha256): `42f2977b941bc016d3155ba9e34828f1b050121d9f18a9e3307e3f7023cf3b32`
- m's package_sha256: `7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb`
- p's package_sha256: `7a08dbfad83aab44dbd11d52844c0473a24610790502a949dfbe650cc9661d24`
- G-CAL-p's artifact: `78f46f07acfdc3577b2117a9671f46b77092042981e5bb2aa40afe03156b5123`
- the covariate (p §3.2): `covariate G-CAL-p-sft (clean minus corrupted, f0's sign): 15/64`
- G-SHAPE-p's artifact: `3c4125a353b70ff7a89ce19687041f44556249ebce496fa4b3f6c9288f2d1554`
- G-ANL-p's artifact: `6440468b60a95de0995431385bb899de8210de2a270eb95d266cc56a9f36b01a`
- p's renders, m's convention (sha16): `6baf494960da4589`
- p's renders, p's convention (sha256): `1551c19997dc45419c496d7f64a61711735672f9388bab4be2e2c1a450f85722`
- the lexicon (F-p11): `be41ad97963bf8dabedd5871d5d691596175269d540956b0f9965a885c2bbab9`
- p's schedules manifest: `999373656ab0fd76771a254f6d8d7d7da696c1448f8ae49b9e0ababe21eddb34`
- schedule OLMo-sft_campaign_A0-OLMo-sft.json: `56703ec998073cfc3e2371f7d46f759213ed8a7476fe7ac60de2db8ea6136fc3`
- schedule OLMo-sft_campaign_A0s-OLMo-sft.json: `8140e3e5201115d1bac3e36013a05c86e016856fddaf40a74751aaaeaecaa209`
- schedule OLMo-sft_qual_A0-OLMo-sft.json: `6938e232040a80ebb37fcf50b1e21ee031c55f18be9c4a8acc16d9e5508d83d0`
- schedule OLMo-sft_qual_A0s-OLMo-sft.json: `377487dbdc0946c6260b3a1d2cde731962e24266df36065c533443327cb8b120`
- schedule OLMo-sft_time_A0-OLMo-sft.json: `1ac7d2920e213148c76977fcbac26273e5725e78aec833fe75a8a4bfe118b537`
- schedule OLMo-sft_time_A0s-OLMo-sft.json: `9cd29a32b2a6b13b13651c759eb5b80c0e2c19adf50545a2c6176f5f4d96010e`
- banner SESSION_BANNER: `7f71cccbf74778ff3370c49ec68796bd054612b5f42e37034ef2041054d47e99`
- banner COMMON: `e4ab3c3e68439b0b449d2c7124f4332415e6df302c1ccc7c3bc2d2d83910c923`
- banner TOLD_MAP: `2a85bd6561d96fdb7ed77c4d4b25579d21d33358974fbf59a38fd3a123e8e017`
- banner TOLD_MAP_SHAM: `2e5cc2943d879173e6fe39ce3078d5646e65320b7d6d42cea504c7fd67f84cc9`
- banner TOLD_OBJ: `f59f7044a44bde123d2ba07209cdc5f3921fb9e6eb158a2bcbb44bf53aa973a2`
- banner DECLARED_HARNESS_STRINGS: `e7cb0a23811890edcc2dd90bdf7a8c7afeb7a2d08461b686780a4a3e0142837a`
- the OLMo ban list (sha16): `2dd86a453a2275ef`
- the OLMo scaffold set (data/olmo/scaffold_sft.json): `0c3592ad0bb2cb1d359c14eca1603317ce39e412eab33dc747dd959c5fdcb5a8`
- the driver (scripts/p_sessions.py): `d91e41e1436b56b8f5aada09f1e24ae45c401234b50feeafb53771b32bf9a943`

## 2. The licence (p §4.2; the m shas as they stand) -- one line each, verbatim

```
LICENCE valence_core/p package_sha256 7a08dbfad83aab44dbd11d52844c0473a24610790502a949dfbe650cc9661d24 (14 files, valence_core/p/*.py)
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
```

## 3. The register (p §4.2; entries (6)-(9) as the seat declared them at `de729c4`, entry (9) on `resume.Identity` as its answer to Code's block of 2026-11-08 declares it, `6b63973`, §2) -- one line each, verbatim

- As that answer has this lock record it: (6) roots, (7) roots, (8) pins, (9) pins on `resume.Identity`, with Q9 (b)'s roots as parameters (entry (3)'s reason); (8) and (9) are entered and restored together.

```
REGISTER {"attrs": ["_eligible_m"], "kind": "eligibility", "module": "valence_core.m.corr", "n": 1, "reason": "p §1.4: corrupt_p is corr.corrupt_m with the frame-word eligible set (p §1.1)", "replacement": "valence_core.p.corrupt.eligible_p", "status": "built at the p BUILD (p §8 step 4)"}
REGISTER {"attrs": ["item_key", "arm_key", "sched_key", "gate_sched_key"], "kind": "keys", "module": "valence_core.m.keys", "n": 2, "reason": "p §4.1: the six OLMo key families under p's prefix, for the schedule builder, the arm streams and the item streams, so that no p stream coincides with an m stream", "replacement": "valence_core.p.keys.{item_key, arm_key, sched_key, gate_sched_key}", "status": "built at the p BUILD (p §8 step 4)"}
REGISTER {"attrs": ["clock_of_record", "crosscheck_coordinate"], "kind": "clock; roots", "module": "m_analyze", "n": 3, "reason": "p §4.4: p's outputs through m's analyzer (scripts/m_analyze.py, imported by scripts/p_analyze.py), the proposal pin kept m's (proposal_p_sha256 beside it): (a) the Clock -- D_p for the OLMo units, m's own for Q-F0 and Q-F3; (c) the v2 posting's per-unit verdicts-dir resolution -- data/p/verdicts for the OLMo units, data/m/verdicts for Q-F0. (b) The roots are parameters wherever m takes them, not a site (the seat's Q9 (b))", "replacement": "valence_core.p.analysis.{clock_of_record_p, crosscheck_coordinate_p}", "status": "built at p §8 step 6 (the seat's answer of 2026-11-08, de729c4)"}
REGISTER {"attrs": ["run_completability's segment and generation call (gcal.py:1155, :1164; the OLMo branch's temp, cap at :1104)"], "kind": "pinned restatement", "module": "valence_core.m.gcal", "n": 5, "reason": "p §3.1, P21: m's call is an inline fragment of run_completability, which cannot run for p (its precheck, roots and identity, and no hair trigger)", "replacement": "valence_core.p.gcal.run's restated segment (m's SEGMENT_FORM) and call, pinned by gcal._call_pin_problems (an AST comparison, also run in G-CAL-p's precheck) and the self-test's dynamic check of all 128 calls", "status": "admitted by the seat's ruling of 2026-11-07 (38f9974, §4); a restatement, never substituted"}
REGISTER {"attrs": ["DEFAULT_OUT"], "kind": "roots", "module": "valence_core.m.stages", "n": 6, "reason": "the seat's Q1: p's gate stages and campaign write under data/p; m's out-root guard reads DEFAULT_OUT at call time (stages.py:309) and so admits data/p and refuses data/m for p", "replacement": "valence_core.p.stage.DEFAULT_OUT_P (REPO/data/p)", "status": "built at p §8 step 6 (the seat's answer of 2026-11-08, de729c4)"}
REGISTER {"attrs": ["verify_schedule_dir"], "kind": "roots", "module": "valence_core.m.schedule", "n": 7, "reason": "the seat's Q2: m's load_committed runs m's verifier, which regenerates all four units' files and m's manifest and so refuses data/p/schedules; p's is m's check over p's eighteen files and p's manifest, regenerated by p's builder under entry (2)", "replacement": "valence_core.p.schedule.verify_schedule_dir", "status": "built at p §8 step 6 (the seat's answer of 2026-11-08, de729c4)"}
REGISTER {"attrs": ["IDENTITY_KEYS_OLMO"], "kind": "pins", "module": "valence_core.m.resume", "n": 8, "reason": "the seat's Q3 (a): p's four identity fields in every p gate-stage and campaign checkpoint's identity, as F-p8 ruled for checkpoints and p:84 asks", "replacement": "valence_core.p.identity.IDENTITY_KEYS_OLMO_P (m's key set + proposal, proposal_p_sha256, p_package_sha256, renders_sha256_p)", "status": "built at p §8 step 6 (the seat's answer of 2026-11-08, de729c4)"}
REGISTER {"attrs": ["Identity"], "kind": "pins", "module": "valence_core.m.resume", "n": 9, "reason": "the seat's Q3 (a): p's four fields added to m's identity by m's own builder, wrapped -- the stage's build (stages._identity, stages.py:1106) and m's rebuild in _validated (resume.py:507) both resolve resume.Identity at call time. Declared at de729c4 on stages._identity, which cannot run (Code's block of 2026-11-08, 9624f70); on resume.Identity by the seat's answer to that block (6b63973, §2), entered and restored with entry (8)", "replacement": "valence_core.p.identity.identity_p (m's builder, wrapped)", "status": "built at p §8 step 6 (the seat's answer of 2026-11-08, de729c4)"}
```

## 4. This checkpoint's schedules (`data/p/schedules`; manifest sha256 `999373656ab0fd76771a254f6d8d7d7da696c1448f8ae49b9e0ababe21eddb34`)
- `OLMo-sft_campaign_A0-OLMo-sft.json` sha256 `56703ec998073cfc3e2371f7d46f759213ed8a7476fe7ac60de2db8ea6136fc3`
- `OLMo-sft_campaign_A0s-OLMo-sft.json` sha256 `8140e3e5201115d1bac3e36013a05c86e016856fddaf40a74751aaaeaecaa209`
- `OLMo-sft_qual_A0-OLMo-sft.json` sha256 `6938e232040a80ebb37fcf50b1e21ee031c55f18be9c4a8acc16d9e5508d83d0`
- `OLMo-sft_qual_A0s-OLMo-sft.json` sha256 `377487dbdc0946c6260b3a1d2cde731962e24266df36065c533443327cb8b120`
- `OLMo-sft_time_A0-OLMo-sft.json` sha256 `1ac7d2920e213148c76977fcbac26273e5725e78aec833fe75a8a4bfe118b537`
- `OLMo-sft_time_A0s-OLMo-sft.json` sha256 `9cd29a32b2a6b13b13651c759eb5b80c0e2c19adf50545a2c6176f5f4d96010e`

## 5. Keys (p §4.1: m's six OLMo families under p's prefix, register entry (2); every key of this checkpoint, fifteen, as `keys.all_olmo_keys` builds them)
  - A0-OLMo-sft: arm (campaign) `p-olmo|sft|A0-OLMo-sft|{s}`; arm (G-TIME) `p-olmo-time|sft|A0-OLMo-sft|{s}`; arm (G-F0m-OLMo) `p-olmo-qual|sft|A0-OLMo-sft|{s}`; gate schedule (G-TIME) `p-sched|OLMo-sft|time|A0-OLMo-sft|0`; gate schedule (G-F0m-OLMo) `p-sched|OLMo-sft|qual|A0-OLMo-sft|0`; campaign schedule `p-sched|OLMo-sft|A0-OLMo-sft|{b}`
  - A0s-OLMo-sft: arm (campaign) `p-olmo|sft|A0s-OLMo-sft|{s}`; arm (G-TIME) `p-olmo-time|sft|A0s-OLMo-sft|{s}`; arm (G-F0m-OLMo) `p-olmo-qual|sft|A0s-OLMo-sft|{s}`; gate schedule (G-TIME) `p-sched|OLMo-sft|time|A0s-OLMo-sft|0`; gate schedule (G-F0m-OLMo) `p-sched|OLMo-sft|qual|A0s-OLMo-sft|0`; campaign schedule `p-sched|OLMo-sft|A0s-OLMo-sft|{b}`
  - items: campaign `p-olmo-items|sft|{s}`; G-TIME `p-olmo-items-time|sft|{s}`; G-F0m-OLMo `p-olmo-items-qual|sft|{s}`

## 6. Banner bytes (m's, unchanged; p's records keep m's template strings, p:84)
- Each sha256 in this list is over the constant's JSON form, `json.dumps(value, sort_keys=True, ensure_ascii=False)` in UTF-8 (`stage.banner_shas`, the form the stage's precheck reads), not over its raw bytes:
  - `SESSION_BANNER` sha256 `7f71cccbf74778ff3370c49ec68796bd054612b5f42e37034ef2041054d47e99`
  - `COMMON` sha256 `e4ab3c3e68439b0b449d2c7124f4332415e6df302c1ccc7c3bc2d2d83910c923`
  - `TOLD_MAP` sha256 `2a85bd6561d96fdb7ed77c4d4b25579d21d33358974fbf59a38fd3a123e8e017`
  - `TOLD_MAP_SHAM` sha256 `2e5cc2943d879173e6fe39ce3078d5646e65320b7d6d42cea504c7fd67f84cc9`
  - `TOLD_OBJ` sha256 `f59f7044a44bde123d2ba07209cdc5f3921fb9e6eb158a2bcbb44bf53aa973a2`
  - `DECLARED_HARNESS_STRINGS` sha256 `e7cb0a23811890edcc2dd90bdf7a8c7afeb7a2d08461b686780a4a3e0142837a`
- The raw bytes (UTF-8), each string's sha256 -- the values LOCK-m-F3 §6 records for the same m constants:

  | constant | bytes | sha256 |
  |---|---|---|
  | `SESSION_BANNER` | 34 | `6124c724758f61109af42141cd2dd576e2fb4e4b9c781e5a22af8be16a6a30ae` |
  | `COMMON` | 89 | `5d915bd852b5d5984f6997623a1dd614cdf336e9518bd55e6d9916f7dffe33b0` |
  | `TOLD_MAP`, clause 0 | 134 | `6bfc495be9b72cbfce0d53f952dfdd0969a51c483eefa2dfeeb5abcd54dc89ba` |
  | `TOLD_MAP`, clause 1 | 134 | `a6fe3b799dc62012ec5e934a9d7a154c94d5df8fef9b6c1b307eb2661afffae4` |
  | `TOLD_MAP_SHAM`, clause 0 | 107 | `5bdf99055b93792ffa5b78962f4e2b1b79569ad4fe93a295ce9ae56f0ec7e3d3` |
  | `TOLD_MAP_SHAM`, clause 1 | 107 | `a8b3befdfde53cbc72233564e6d3467abc4806cc092b0073f1fb0e576b198b25` |
  | `TOLD_OBJ` | 137 | `a50ca2358a40ec9ff0360489c81b93c0eebf40943a8922d27fc5c16424ce56bb` |
  | `REASONING_HEADER` | 23 | `58b8d5553639b13c6e294668e56d3437da36d84d892b03181baf15574e6078b0` |
  | `REASONING_LINE` | 21 | `999aca0d3a889c37761366e7a0149b3945566e4004dafd11347c0f651ea39d65` |

- `DECLARED_HARNESS_STRINGS` is eight of these strings, in order: `COMMON`, `TOLD_MAP`'s two clauses, `TOLD_MAP_SHAM`'s two clauses, `TOLD_OBJ`, `REASONING_HEADER` and `REASONING_LINE`.

## 7. The F0m-OLMo verifier and the OLMo scaffold set's assertion
- the verifier: `valence_core/m/verify.py` (its sha256 in §2's licence line), run on every record before it is written (G-VER, m:271, m:284).
- the scaffold set: ban ids sha16 `2dd86a453a2275ef` (b3's), asserted against `data/olmo/scaffold_sft.json` sha256 `0c3592ad0bb2cb1d359c14eca1603317ce39e412eab33dc747dd959c5fdcb5a8` at every stage start (`runner_olmo.olmo_startup`).

## 8. The covariate (p §3.2, carried here)
- `covariate G-CAL-p-sft (clean minus corrupted, f0's sign): 15/64` -- beside PROPOSAL-m's at the shared renders (+5/16), Qwen's +9/64 and f1's +.078.

## 9. Every later bar (m:302, by reference; m's `bars.OLMO_BARS`, each field verbatim) and p's hair trigger
  - {"alpha": "0.05", "binding": true, "cadence": "evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271)", "domain": "every", "justification": "A case-sensitive match of one of the six strings of b3's ban list (m:262), asserted equal to the ban-list strings and to b3's id sha16 at startup, in model-generated text; the sampler's ban suppresses them, so the base rate is ~zero.", "kind": "hair_trigger", "name": "scaffold_absorption", "numerator": "generations containing a scaffold-set string", "on_fire": "STOP the stage (m:271)", "p0": null, "planned_crit": null, "planned_n": null, "scope": "OLMo-sft", "stage": "every", "substrate": "olmo", "unit": "model generation (round)"}
  - {"alpha": "0.05", "binding": true, "cadence": "evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271)", "domain": "every", "justification": "Harness bytes that fail G-VER (m:284): the harness writes every scaffold byte itself, so a session whose bytes do not reconstruct from its recorded fields, the committed schedule and the rng streams is a build defect; base rate zero by construction.", "kind": "hair_trigger", "name": "template_breakage", "numerator": "sessions failing G-VER", "on_fire": "STOP the stage (m:271)", "p0": null, "planned_crit": null, "planned_n": null, "scope": "OLMo-sft", "stage": "every", "substrate": "olmo", "unit": "session"}
  - {"alpha": "0.05", "binding": true, "cadence": "evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271)", "domain": "every", "justification": "Pair, map, start order, clause order, banner bytes or item stream differing from the committed schedule (m:271, m:253): the schedule is a committed file and every stream a deterministic key, so the base rate is zero by construction.", "kind": "hair_trigger", "name": "schedule_mismatch", "numerator": "sessions differing from the committed schedule", "on_fire": "STOP the stage (m:271)", "p0": null, "planned_crit": null, "planned_n": null, "scope": "OLMo-sft", "stage": "every", "substrate": "olmo", "unit": "session"}
  - {"alpha": "0.05", "binding": true, "cadence": "once at stage end on the realised n; no mid-stage evaluation (m:271)", "domain": "sham", "justification": "b3's declared p0 .02 on its AuditSpec-only numerator (0/756 on b3's shams [C]); m adds the echo class, so p0 is a declared tolerance at a named, changed contrast (m:271, m:262).", "kind": "binomial_stage_end", "name": "round_degeneracy@G-TIME-OLMo-sft", "numerator": "rounds claimed by b3's AuditSpec or m's harness-echo class (m:262)", "on_fire": "STOP before G-F0m-OLMo-sft (m:302). Fires only on a claim in round 1 or 2 (critical 1 at n <= 2)", "p0": "0.02", "planned_crit": 2, "planned_n": 10, "scope": "OLMo-sft", "stage": "time", "substrate": "olmo", "unit": "task round generated (<= 10 per session: 4 forced + 6 free)"}
  - {"alpha": "0.05", "binding": true, "cadence": "at stage end, before that checkpoint's qualification (m:302)", "domain": "sham", "justification": "On OLMo a session ends at its first claim (m:262), so the one-session G-TIME bar's critical 2 is unreachable past round 2 (STOP-7 A'3); both numerator classes are ~zero-base-rate there (AuditSpec 0/756 on b3's shams; echo a verbatim reproduction of a harness line, its final period aside where OLMo's newline stop drops it -- audit.harness_echo's PIN), which licenses a one-claim pause (m:271, m:302).", "kind": "pause", "name": "gtime_pause@G-TIME-OLMo-sft", "numerator": "rounds claimed by b3's AuditSpec or m's harness-echo class (m:262)", "on_fire": "PAUSE for the seat's adjudication before G-F0m-OLMo; recorded, not a verdict (m:271)", "p0": null, "planned_crit": null, "planned_n": null, "scope": "OLMo-sft", "stage": "time", "substrate": "olmo", "unit": "task round of the G-TIME-OLMo sham session"}
  - {"alpha": "0.05", "binding": true, "cadence": "once at stage end on the realised n; no mid-stage evaluation (m:271)", "domain": "sham", "justification": "b3's declared p0 .02 on its AuditSpec-only numerator (0/756 on b3's shams [C]); m adds the echo class, so p0 is a declared tolerance at a named, changed contrast (m:271, m:262).", "kind": "binomial_stage_end", "name": "round_degeneracy@G-F0m-OLMo-sft", "numerator": "rounds claimed by b3's AuditSpec or m's harness-echo class (m:262)", "on_fire": "STOP: OLMo-sft does not run until the seat re-specifies (m:302)", "p0": "0.02", "planned_crit": 7, "planned_n": 160, "scope": "OLMo-sft", "stage": "qual", "substrate": "olmo", "unit": "task round generated (<= 10 per session: 4 forced + 6 free)"}
  - {"alpha": "0.05", "binding": true, "cadence": "every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look index in the resume identity (m:330)", "domain": "sham", "justification": "b3's declared p0 .02 on its AuditSpec-only numerator (0/756 on b3's shams [C]); m adds the echo class, so p0 is a declared tolerance at a named, changed contrast (m:271, m:262).", "kind": "binomial_look", "name": "round_degeneracy@campaign-OLMo-sft", "numerator": "rounds claimed by b3's AuditSpec or m's harness-echo class (m:262)", "on_fire": "PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316)", "p0": "0.02", "planned_crit": null, "planned_n": null, "scope": "OLMo-sft", "stage": "campaign", "substrate": "olmo", "unit": "task round generated (<= 10 per session: 4 forced + 6 free)"}
  - {"alpha": "0.05", "binding": true, "cadence": "at every look, per contrast arm (m:316)", "domain": "contrast_arm", "justification": "Adapted from f1's guard (archive:400-402): pre-pick exclusion rate vs the matched sham by one-sided Fisher exact, binding on both substrates (m:316).", "kind": "guard_fisher", "name": "exclusion_guard_fisher@campaign-OLMo-sft", "numerator": "pre-pick exclusions (sessions excluded before their first read, m:308)", "on_fire": "PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316)", "p0": null, "planned_crit": null, "planned_n": null, "scope": "OLMo-sft", "stage": "campaign", "substrate": "olmo", "unit": "session launched in the arm through the look (pre-pick exclusion)"}
  - {"alpha": "0.05", "binding": false, "cadence": "at every look, per contrast arm (m:316)", "domain": "contrast_arm", "justification": "f1's whole-session reference .20 at F0 (archive:400-402) carried to m's pre-pick unit: a declared tolerance at a named, changed contrast (m:316). Reported only on OLMo: b3's exclusions are dominated by the lexical class m declines to bar.", "kind": "guard_abs", "name": "exclusion_guard_abs@campaign-OLMo-sft", "numerator": "pre-pick exclusions (sessions excluded before their first read, m:308)", "on_fire": "none (reported only, m:316)", "p0": "0.20", "planned_crit": null, "planned_n": null, "scope": "OLMo-sft", "stage": "campaign", "substrate": "olmo", "unit": "session launched in the arm through the look (pre-pick exclusion)"}
  - p's hair trigger: `line_break_in_stored_text` (p §2.3), every stored text of every session; enforced in the proxy (the seat's Q5), a STOP; zero base rate by construction.

## 10. The analyzer blobs
- m's analyzer `scripts/m_analyze.py` sha256 `d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48`; p's `scripts/p_analyze.py` sha256 `d3758fc4543b174bd8e923781f094a55c56c19cecee08e091a92c9eadf577008`; m's package_sha256 `7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb`; p's package_sha256 `7a08dbfad83aab44dbd11d52844c0473a24610790502a949dfbe650cc9661d24`; m's analyzer closure sha256 `a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b`.

## 11. How G-TIME-OLMo (p) cites this lock
- identity_extra: `lock_file` `LOCK-p-OLMo-sft.md`, `lock_sha256` this file's sha256, `proposal_file` `PROPOSAL-m-gating-campaign-v1_11.md`, `proposal_sha256` m's (F-p8), `renders_sha16` `6baf494960da4589`, `locked_path` uncached, `analyzer_sha256` and `package_sha256` m's (§10).
- the checkpoint identity also carries p's four fields (entries (8), (9)): `proposal`, `proposal_p_sha256`, `p_package_sha256`, `renders_sha256_p`.

## 12. PIN sites in p's package and drivers (`PIN (Code` lines), by file and line at this lock
- `valence_core/p/analysis.py:16`
- `valence_core/p/analysis.py:20`
- `valence_core/p/corrupt.py:76`
- `valence_core/p/identity.py:21`
- `valence_core/p/keys.py:8`
- `valence_core/p/keys.py:84`
- `valence_core/p/proxy.py:23`
- `valence_core/p/proxy.py:27`
- `valence_core/p/register.py:21`
- `valence_core/p/register.py:77`
- `valence_core/p/register.py:133`
- `valence_core/p/report.py:19`
- `valence_core/p/report.py:38`
- `valence_core/p/report.py:64`
- `valence_core/p/report.py:264`
- `valence_core/p/report.py:272`
- `valence_core/p/schedule.py:8`
- `valence_core/p/schedule.py:18`
- `valence_core/p/schedule.py:24`
- `valence_core/p/stage.py:21`
- `valence_core/p/stage.py:35`
- `valence_core/p/stage.py:40`
- `valence_core/p/stage.py:52`
- `valence_core/p/stage.py:69`
- `valence_core/p/stage.py:575`
- `scripts/p_sessions.py:62`
- `scripts/p_analyze.py:28`
