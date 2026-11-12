# LOCK-m-F3.md — v0.2 (Q-F3's lock after G-ID-F3, PROPOSAL-m v1.11 §3.2 m:296)

*Q-F3's lock at v0.2, above the re-issued v0.1, which follows below verbatim: the re-issue's part, then v0.1's text. m:296: "LOCK-m-F3 v0.2. Cap; path; projections." A stage cites the whole file by its sha256, which v0.2's entry names.*

## v0.2 §0. Status

- **Version:** v0.2, 2026-11-11. LOCK-m-F3 v1.0 follows G-F3 and G-PWR, with D2 (m:298; D2's date, 2026-12-22, m:16).
- **On the PI's word.** The coordinating session relayed the PI's "Route as given" (2026-11-11) on the seat's answers
  on G-ID-F3. The answers were committed at `a6c6297`, with the close line on G-ID-F3's entry. The routing's items 3
  and 5, verbatim:

  > 3. LOCK-m-F3 v0.2 to §5 — cap; path uncached with the artifact; the uncached projections on the four-session basis, the cached table not applicable; the `id` blob and PINs; the counters [go].
  > 5. After v0.2: the `qual` wiring → G-F3, 40 sessions uncached, announced and serialized, ≈ one laptop day → the seat's read [go].

- **The rulings it rests on** (each file's sha256, and the commit that added it):

  | ruling | file | sha256 | committed at |
  |---|---|---|---|
  | the seat's read of G-ID-F3 (§5: v0.2's contents) | `results/raw/2026-11-10_gid-f3_design-to-code_answers.md` | `c51ef5ba77c30f223875de254c9e0fb0cdef44d900f62c30795659a431a4a9d7` | `a6c6297` |
  | the seat's read of G-TIME-F3's re-run (`r2:`) | `results/raw/2026-11-10_gtime-f3-r2_design-to-code_answers.md` | `54679f70c4082255a8df64a010cea8480fd58db93b7c5310ee9e49fd79adf01d` | `54b1e51` |
  | the seat's read of G-TIME-F3's first run (`gt:`; its §5 confirms v0.2's form) | `results/raw/2026-11-08_gtime-f3_design-to-code_answers.md` | `f683f5d234d76de2bec9f3e81508dad122ca315e0356f417a73edec4c664ee19` | `daca8b0` |
  | ADDENDUM-m2 v0.5 | `ADDENDUM-m2-f3-reasoning-block-v0_5.md` | `f27505c556a3304097d2154698bcf4498927e692c7341aec5060803c833b5354` | `7589c1d` |
  | the list of record v2 | `results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md` | `6c1135f5c0113e994399a80a5338bc48e45fbea57d3f0dbe21925e4c323e6cdd` | `fc43249` |

- **The form.** `gt:`§5, verbatim: "Code's form (the v0.1 text kept verbatim; cap, path, projections; the driver's
  blob of record and its history; the nine PIN sites; the snapshot-revision refusal at `time`; the plural at :72) is
  right, with one order: v0.1 is re-issued first (A-m2 §4.3), and v0.2 follows G-ID-F3 on the re-run; the cap it
  records is the re-run's."
  - v0.2 comes first. Then a rule and one sentence: where the re-issue's or v0.1's text below differs from v0.2, v0.2
    is of record.
  - Then the re-issued v0.1, byte for byte as committed at `f674583` (sha256
    `70da4a70aeeff434cae7f6a436d8391556118c26513b2456f3940d3872e81d3f`), which carries v0.1's own text below it.
  - The seat's §5 lists v0.2's contents. Each is in a section below.
- **The list of record:** the list of record v2 (above; its §2) binds every session on this unit.
- **How a stage cites this file from v0.2's commit:**
  - `lock_file` is `"LOCK-m-F3.md"`. `lock_sha256` is this file's sha256 as committed at v0.2, which v0.2's entry
    names (a file cannot hold its own hash).
  - G-F3 (m:297) runs under v0.2, at `reasoning_cap` 120 (v0.2 §2), carrying `locked_path` `"uncached"` (v0.2 §3).
  - G-F3's prior is G-TIME-F3's re-run checkpoint, taken by path, with the first run's refused (A-m2 v0.5 §4.3).
    G-ID-F3's artifact must be on disk at cap 120, any verdict (`stages.PRIOR_STAGE`'s PIN).
  - G-TIME-F3's first run ran under v0.1 (`1e79955`); its re-run and G-ID-F3 ran under the re-issue (`f674583`). Their
    identities carry those `lock_sha256`s. mf3's `prior_gate` compares a prior's proposal, not its lock.
  - The licence by file runs unchanged: lock §1 below, as the re-issue's R1 amends it.
- **Generated, not transcribed.** These were generated with a tool at v0.2's base, HEAD `15d2f70` (`v02_gen.py`,
  Code's scratch):
  - v0.2 §1's two tables, and the driver's history in v0.2 §5;
  - the verbatim PIN texts in v0.2 §5 and §7.

  Every file they hash or quote is committed there with identical working-tree bytes, and the checkpoints are hashed
  only. The prose is Code's, from the sources it cites.
- **Conventions:**
  - "v0.2 §N" is a section of this amendment; "R N" is a section of the re-issue's part; "lock §N" is a section of
    v0.1's text.
  - Code anchors are at HEAD `15d2f70`. The driver's lines are those of its blob of record, `8d878f4a…` (v0.2 §5).
  - The figures marked [E] are estimates: the seat's (its §4), re-computed by Code from the stages' seconds.

## v0.2 §1. The binding identity at v0.2

| what | path or scope | sha256 | since the re-issue |
|---|---|---|---|
| the proposal of record | `PROPOSAL-m-gating-campaign-v1_11.md` | `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b` | unchanged |
| ADDENDUM-m1 v0.1 | `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md` | `ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001` | unchanged |
| ADDENDUM-m2 v0.5 | `ADDENDUM-m2-f3-reasoning-block-v0_5.md` | `f27505c556a3304097d2154698bcf4498927e692c7341aec5060803c833b5354` | unchanged |
| the analyzer (G-ANL-F3) | `scripts/m_analyze.py` | `d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48` | unchanged |
| m's package | `valence_core/m/*.py` (`resume.package_sha256_of`) | `7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb` | unchanged |
| the Q-F3 closure (PIN-V2-12) | the base closure plus `LAZY_F3_MODULES`, 22 modules | `06a36cbfb4ab5dce94bc1f900d43cea93e667a4cbe64b69f24986f5847eb63e8` | unchanged |
| the base closure | 15 modules | `a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b` | unchanged |
| mf3's package | `valence_core/mf3/*.py` | `098455d91d1ae32371c32cfe883a3ce90c51b7607526e38f5460346ce44dda13` | unchanged |
| the driver (the DRIVER line's value) | `scripts/mf3_sessions.py` | `8d878f4a894e05e4edf8a3c829548a9c0c864d5f45118875b7630e55d1d200e7` | new: the `id` wiring (`fb82daa`) |
| G-SHAPE-F3's artifact | `data/mf3/gates/G-SHAPE-F3.json` | `ff3eaae5b1c6f0b660be418e42709132018d904e53657046367517c1243f1bf3` | unchanged |
| G-ANL-F3's artifact | `data/m/gates/G-ANL-F3.json` | `c2b87ab6c00a9b61ff9265d33cf73aa0aeadcbf9470e7aee2435e004689dc08c` | unchanged |
| Q-F3's schedules manifest | `data/mf3/schedules/manifest.json` | `c7b5df4405981cca40d86564828c854f45c65211f2b2e9c138d43fdacd2a3314` | unchanged |
| G-ID-F3's artifact | `data/mf3/gates/Q-F3_G-ID.json` | `ea8f7d3acd20c3c3b00a11d7dad48283ff20a0abe961462270c3930553e39260` | new: G-ID-F3 (`efb7bef`) |

- **Not repeated:** the eleven m files and the weights of record are unchanged. v0.1's §1 rows below remain the lines
  the licence and the driver read, as the re-issue's R1 says.
- **The records v0.2 rests on**, hashed only (the checkpoints never opened; the list of record v2's item 1):

| record | path | sha256 | committed at |
|---|---|---|---|
| G-TIME-F3's re-run: the checkpoint (-diff) | `data/mf3/ckpt/Q-F3_time-r2.json` | `ff644fa17599d2c816a3fda12be1dd1bd4292ecfb1597dbf8ef5faef984751b8` | `93ecaf9` |
| G-TIME-F3's re-run: the report | `data/mf3/reports/Q-F3_time-r2_report.json` | `e9fc51b55d02f8c78daa6cb2c7260ad2f10b6f2059bf65ed1901471db4dce1ba` | `93ecaf9` |
| G-TIME-F3's re-run: the reads | `data/mf3/reports/Q-F3_time-r2_reads.json` | `859031b062b60500aeb75b19e70a9daffb5b00d8c86ebf8dec541aabcb80a066` | `93ecaf9` |
| G-ID-F3: the checkpoint (-diff) | `data/mf3/ckpt/Q-F3_id.json` | `4244c7fc6467c856a9a86cc85897fc64936d254b7ec3cf0711fa47bcb5ace519` | `efb7bef` |
| G-ID-F3: the report | `data/mf3/reports/Q-F3_id_report.json` | `b3b004287955b78d95142df4aa8046019cc21b0c1df9f0746bb9e590d8f2ed48` | `efb7bef` |
| G-ID-F3: the reads | `data/mf3/reports/Q-F3_id_reads.json` | `79da1b71783afbc549ae0cf998c197b24b29d88246c648e3dccb143d857ce44f` | `efb7bef` |
| G-TIME-F3's first run: the checkpoint (-diff; never written again) | `data/mf3/ckpt/Q-F3_time.json` | `b809c0873840ee29878d7e09733a3771e8d13b0456cbe16bac5ca5edb87f8fc7` | `acc3b52` |

## v0.2 §2. The cap (m:294, m:296; A-m2 v0.5 §4.1)

- **`reasoning_cap = 120`.**
  - A-m2 v0.5 §4.1: "The cap is 120 at the re-run of G-TIME-F3 and at every later Q-F3 stage (G-ID-F3, G-F3, the
    campaign)".
  - The seat (`r2:`§1.4): "The cap of record is 120 (v0.5 §4.1; m:294's count 0 of ≤ 36, reported, moving nothing;
    recorded at v0.2 with the count, m:296)."
- **m:294's count, beside.** G-TIME-F3's re-run printed this CAP TRIGGER line (its raw, `93ecaf9`), verbatim:
  `CAP TRIGGER G-TIME-F3: 0 of <= 36 reasoning lines reached the cap of 120 without a newline (threshold 3; m:294's trigger, reported, moving nothing: A-m2 v0.5 §4.1); the cap is 120, recorded at LOCK-m-F3 v0.2 with this count (m:296)`.
- **The history.** G-TIME-F3's first run ran at 60 (`acc3b52`), and its line read `CAP TRIGGER G-TIME-F3: 1 of <= 36 reasoning lines reached the cap (threshold 3); the cap fixed is 60 (m:294), applied from G-ID-F3 on (m:295) and recorded at LOCK-m-F3 v0.2 (m:296)`.
  - The seat stopped that run (`gt:`).
  - A-m2 v0.5 §4.1 set 120 from the re-run on.
  - G-ID-F3 ran at 120 (its identity).
- **How it binds:** as the re-issue's R1 and R3 record it.
  - The cap of record binds every run on a model: `stages._extra`, `resume.Identity`, `stages.prior_gate` with
    `require_real`, and the driver.
  - The stub path alone may run at 60.

## v0.2 §3. The path (m:295–296; the seat's G-ID-F3 answers, §1.3)

- **`path = uncached`.** G-ID-F3 computed FAIL (`efb7bef`), and the seat ruled (§1.3): "G-ID-F3: FAIL stands as
  computed."; "The path of record is uncached".
  - m:295: "a divergence sends Q-F3 uncached". Lock §8, bar 6: "G-ID-F3 FAIL: Q-F3 runs uncached (m:295)".
  - Nothing is re-run or re-specified (the routing's item 1).
- **The artifact**, `data/mf3/gates/Q-F3_G-ID.json` (sha256 in v0.2 §1):
  - verdict `FAIL`, `n_pairs` 1, `pairs_identical` `[false]`, under the seat's F-7 criterion;
  - the bar `gid_divergence@G-ID-F3` fired at k = 1 of n = 1;
  - the stage "stops at the first divergence (m:281, m:295)" (bar 6's row), so A3s did not run.
- **The pair's record**, A2s at index 0:
  - identical through the four forced rounds;
  - the transcripts first differ inside round 5's reasoning line, after 658 shared characters;
  - all six lines differ, and the picks agree through round 9 and differ at round 10.
- **The halves' seconds:** uncached 1,942.675 s, cached 208.347 s. In the seat's words (§1.3), they "are recorded as the
  stage's seconds (m:281's "cached timing recorded"), the uncached one joining the basis (§4)".
- **How it binds** (Code's description):
  - every later Q-F3 stage carries `locked_path` `"uncached"`;
  - `stages._locked` refuses a run whose locked path differs from the one the G-ID licence gives on the backend at the
    cap;
  - `guard._gid_pass` (`valence_core/mf3/guard.py:97–102`) admits the cached path only on a PASS artifact with two
    identical pairs.
- **The campaign's launches** are the uncached table's, m:234–241 (v0.2 §4). Their per-arm counts and the hour cap are
  v1.0's (m:298).

## v0.2 §4. The projections, uncached (m:296; the seat's G-ID-F3 answers, §4 and §5) [E]

- **The basis:** four uncached sham sessions at cap 120 under F-b (the seat's §4):

  | stage | session | seconds | reasoning tokens |
  |---|---|---|---|
  | G-TIME-F3's re-run (`93ecaf9`) | A1s | 1,175.9 | 160 |
  | G-TIME-F3's re-run (`93ecaf9`) | A2s | 1,041.4 | 226 |
  | G-TIME-F3's re-run (`93ecaf9`) | A3s | 1,118.3 | 240 |
  | G-ID-F3 (`efb7bef`) | A2s, the uncached half | 1,942.7 | 375 |

  The four total 5,278.3 s: a mean of 1,319.6 s (22.0 min). The slowest is 1,942.7 s.
- **The campaign** (672–960 uncached launches, m:234–241, k ≥ 24, all arms):
  - at the mean, ≈ 245–350 h (246.3 h; 351.9 h);
  - at the slowest observed, ≈ 360–520 h (362.6 h; 518.0 h).
- **G-F3's 40 sessions:** ≈ 14.7 h at the mean, ≈ 21.6 h at the slowest.
- **Beside, not the basis:**
  - m:234–241's own column, 120–190 h, at m:230's 641.6–713.6 s per session;
  - G-TIME-F3's first run's sham seconds at cap 60: 109.1, 209.4 and 392.5 s (`gt:`§6).
- **The cached table** (m:216, m:220–226) is not applicable under the FAIL (the seat's §1.3). G-ID-F3's cached
  member, 208.3 s, is recorded as a figure of the stage, not a projection.
- **Where the decision sits** (the seat's §4):
  - The PI sets Q-F3's hour cap at v1.0 (m:298).
  - m:243: "the PI may decline to commit LOCK-m-F3 v1.0, which makes Q-F3 NOT-RUN".
  - m:324 lists "the PI declined to commit v1.0, for projected hours or any reason" among NOT-RUN's causes.
  - D2 is 2026-12-22.
  - The seat's default is to run G-F3 first, which brings the basis to 24 sham sessions before the cap is set.

## v0.2 §5. The driver of record, its history and its PINs (the `time` and `id` wirings; the seat's F-1)

- **The DRIVER line's value of record:** `scripts/mf3_sessions.py`, sha256
  `8d878f4a894e05e4edf8a3c829548a9c0c864d5f45118875b7630e55d1d200e7` (the `id` wiring, `fb82daa`), as G-ID-F3's
  DRIVER line printed it before the load.
- **Its history**, every commit that changed it:

| commit | the edit | the blob's sha256 | the model runs its DRIVER line printed it for |
|---|---|---|---|
| `cd9756e` | the F3 BUILD | `48008a53440d201044268bf48f118f79ed7ed82f7c894820e25726a2aba164cf` | — |
| `993eba1` | G-ANL-F3's hygiene commit | `fad31c20e44451db7367391ea14e1b9560527390dc8d249f03689d9950900cbb` | — |
| `acde2d8` | the `time` wiring | `890084e6c626a3ced2007c4285c255fb73978c07aeca15427172fc17028690af` | G-TIME-F3's first run (`acc3b52`) |
| `9c7062e` | the A-m2 smoke's driver (`time --smoke`) | `c9393a482001270e4564b940c17fa982f711aa9cf1a08e72ec239f16a0884d9b` | the A-m2 smoke (`6cfd3db`; never of record) |
| `5d40d59` | the A-m2 v0.5 BUILD (the smoke form retired) | `1b593ba0465c5cf1af4d5b47283456b32359b37e0e3974848aade0f1d31287c6` | G-TIME-F3's re-run (`93ecaf9`) |
| `fb82daa` | the `id` wiring | `8d878f4a894e05e4edf8a3c829548a9c0c864d5f45118875b7630e55d1d200e7` | G-ID-F3 (`efb7bef`) |

- **The `time` wiring's nine PIN sites, declared at v0.2.** They were at :72, :81, :98, :108, :221, :284, :334, :359, :442 in the `time` wiring's own
  blob (`acde2d8`). In the blob of record they are at :92, :102, :150, :160, :278, :386, :462, :487, :577:

| site | where | the text in the blob of record (verbatim) |
|---|---|---|
| `scripts/mf3_sessions.py:92` | comment | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; the seat's F-1, carrying the step-10 read's Q2: "an edit … that wires a subcommand … does not re-run G-SHAPE-F0", here G-SHAPE-F3): ``time`` is wired for Q-F3 under LOCK-m-F3 v0.1 (lock §11 item 1: "the `time` subcommand is wired in `scripts/mf3_sessions.py` at its step"), on the PI's routing of 2026-11-07, item 1 ("… → LOCK-m-F3 v0.1 → G-TIME-F3 [go]"). The edit touches no scoring-stack function. The new blob's sha256 is printed by the DRIVER line and recorded in the G-TIME-F3 entry and in LOCK-m-F3 v0.2 (the step-10 read's Q2 condition, which Code reads F-1's "with the same scope" as carrying; the routing of 2026-11-07). qual and campaign stay refused until their steps; id is wired at its own step (the id wiring's PIN, below). |
| `scripts/mf3_sessions.py:102` | comment | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's TIME_* form carried, scripts/m_sessions.py): G-TIME-F3 cites LOCK-m-F3.md (lock §1); one session per Q-F3 arm (m:293: "One session per Q-F3 arm (6), as G-TIME-F0"), the counts the committed time schedules carry (n 1 each); locked_path "uncached" (m:293, "G-TIME-F3 (Qwen, uncached)"); reasoning cap 60 at the first run (m:174), 120 from the re-run on (A-m2 v0.5 §4.1; the PIN below). The five flags are the lock's values, as LOCK-m-F0 §0's "How a stage cites this file" made them for m's driver. The values are Q-F3's; TIME_REASONING_CAP and TIME_FLAG_HELP have no counterpart in m. |
| `scripts/mf3_sessions.py:150` | comment | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's PIN at LOCK v0.2 carried, scripts/m_sessions.py): the model id the Qwen path loads -- QwenMLXAdapter's default, passed explicitly by _load_qwen; the model of record mf3.resume binds -- and mlx_lm.utils._download's default allow_patterns, with which the snapshot check resolves the snapshot as the load does. The self-test asserts both equal their sources (the adapter's and mlx_lm's source, read, not imported) and m's driver's constants (its source, read, not imported). |
| `scripts/mf3_sessions.py:160` | comment | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's TOTALS_RX / redact_totals / _say carried): every REFUSED and STOP line of the stage path passes through redact_totals (the step-14 read's Q3) and goes to stderr, as m's do. |
| `scripts/mf3_sessions.py:278` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's stage_identity_extra carried, scripts/m_sessions.py): the proposal's and the lock's sha256 are computed here from their COMMITTED blobs (stages.committed: committed at HEAD, working tree identical). The lock is TIME_LOCK_FILE, and its committed text must name the proposal's sha256 in full. The analyzer's and mf3's package sha256 and the renders' sha16 are the values the command line gives -- the lock's -- and are never derived here from the bytes they are checked against: the licence checks the first two at stage start ((d), (e)) and _renders_of_record the third. m_module_sha256 and the weights binding are read from the lock's committed text (the routing of 2026-11-07): each of guard.M_HASHED's eleven files with the one sha256 the lines naming it carry, and the one WEIGHTS line, which must name QWEN_MODEL_ID; the licence then checks them against the files ((e')), the hub cache ((g)) and that same text ((f)). reasoning_cap 120, the cap of record (A-m2 v0.5 §4.1), and locked_path "uncached" (m:293) are this driver's; prior_proposal_sha256s is omitted (none under LOCK-m-F3 v0.1, lock §1). The result is validated by stages._extra as a run on a model (stub=False), which refuses any cap but 120 (A-m2 v0.5 §4.2: "the driver's `time` at any cap but 120 is refused"). |
| `scripts/mf3_sessions.py:386` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's stage_precheck carried for "time", scripts/m_sessions.py): the licence by file ((a)-(g)); the run-time known answers on the proposal the identity names; the renders of record; the committed schedule files; the checkpoint (the path itself; an ENDED one; one on disk without --resume and no end pending); m:267's laptop checklist (power, one model process, disk); the gate line and its files (CLAUDE.md and the analyzer committed, working tree identical; HEAD known). The stage (stages.run_gate_stage) makes each of them again after the load, except the refusal of a looping link at the checkpoint path, which only this precheck makes. NOT made here, so made only by the stage after the load: a resume's comparison of the checkpoint with this run (rs.load_or_init's identity and readability refusals, stages._record_licence), runner.f3_startup's pins, the counts against the committed files' n, the bars' firing-case completeness and the stage's internal assertions. ``run_time`` adds the driver check's and the snapshot check's problems and refuses once. Every problem passes through redact_totals. |
| `scripts/mf3_sessions.py:462` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's driver_problems carried): the step-10 read's Q2 makes the record of the wiring driver's blob a condition of every wiring of its kind ("the new blob's sha256 printed by the DRIVER line and recorded in the entry of the stage it wires and in the next lock revision …"), which Code reads F-1 as carrying to this driver (the routing of 2026-11-07: G-TIME-F3's entry and LOCK-m-F3 v0.2). run_time's Qwen path refuses an uncommitted driver and prints the DRIVER line from this one call before the load, so the value recorded is a value the run logged. A process running any file but the driver of record (REPO/DRIVER_REL) -- a copy, edited or not -- is refused: the DRIVER line names that path's committed blob, which would not be the code running (the review's MINOR-2; m derives DRIVER_REL from __file__). |
| `scripts/mf3_sessions.py:487` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's qwen_snapshot carried verbatim in its checks, the routing of 2026-11-07: "Build at time"): each refusal mirrors how the load resolves the weights (jlens_qwen.model.load -> mlx_lm.load -> mlx_lm.utils._download -> huggingface_hub.snapshot_download): HF_HUB_OFFLINE must be exactly "1"; MLXLM_USE_MODELSCOPE must not be "true" in any case (mlx_lm tests it so, and would take modelscope's downloader); no path or link named like the model id may exist relative to the working directory (mlx_lm loads an existing one before the hub cache; a dangling link is refused conservatively); the hub cache's `refs/main` for QWEN_MODEL_ID must be, as raw file text, a 40-hex revision whose snapshot directory exists and holds config.json, tokenizer.json, model.safetensors.index.json and every weight file the index names (each a plain file name, resolving to a file); and the hub's own offline resolution with mlx_lm's patterns (snapshot_download, local_files_only) must succeed and return that same directory. The cache is huggingface_hub's HF_HUB_CACHE. info: model_id, revision, snapshot_dir, n_snapshots (snapshot directories of the model's cache repo), offline. The licence's (g) checks the bound revision and the binding; this check is the load's own resolution, and its SNAPSHOT line is the raw's record. |
| `scripts/mf3_sessions.py:577` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's _run_stage Qwen path carried, scripts/m_sessions.py): ``adapter_factory`` and ``out_root`` are the self-test's seam (a scripted stub writing a test directory, which stages refuses anywhere under data/mf3); without the factory the adapter is Qwen through qwen_or_explain, the out root is stages.DEFAULT_OUT (read at call time), a given ``out_root`` is refused before any load, and time_precheck, the driver check (one driver_problems call) and the snapshot check (one qwen_snapshot call), their problems refused together, then the DRIVER and SNAPSHOT lines, come before the load; after it, the snapshot is read again and the adapter's model_id compared: a re-read that refuses, a moved refs/main or another model id STOPs before a session (SNAPSHOT RE-READ REFUSED / SNAPSHOT MOVED / MODEL ID). A STOP, and any exit other than 0 or 2, is escalated to the seat; Code never self-adjudicates. |

- **The `id` wiring's four PIN sites, declared at v0.2:**

| site | where | the text in the blob of record (verbatim) |
|---|---|---|
| `scripts/mf3_sessions.py:128` | comment | PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's run_id form carried, scripts/m_sessions.py): ``id`` is wired for Q-F3 under LOCK-m-F3 v0.1 as re-issued, at its step -- the seat's read of G-TIME-F3 r2, §5 item 1, routed by the PI on 2026-11-10 (its §8 item 4: "The `id` wiring (F-1's kind, named in its entry) → G-ID-F3 at 120 on the laptop"). G-ID-F3 (m:295): keys m-id\|F3\|{template}\|{s}, A2s and A3s once each (keys.GID_TEMPLATES), criterion 2/2 (stages.gid_decide; each pair's identity under the seat's F-7, stages._gid_pair), a divergence sending Q-F3 uncached. Its identity carries time's five flags' values (the lock's, ID_LOCK_FILE) and no locked_path (the path is recorded at LOCK-m-F3 v0.2, lock §1); its reasoning cap is the cap of record, ID_REASONING_CAP (A-m2 v0.5 §4.1), the one prior_gate fixes with require_real on. Its prior is G-TIME-F3's re-run checkpoint, ID_PRIOR_CKPT_NAME, taken by path, the first run's name refused (A-m2 v0.5 §4.3: "the `id` and `qual` wirings take the re-run's checkpoint by path and refuse the first"; lock R4 item 2). Its checkpoint, report and reads are m's default stem for "id" (stages.out_paths), its artifact guard.gid_artifact_path(), write-once. The edit is of F-1's kind: the new blob's sha256 is printed by the DRIVER line and recorded in the G-ID-F3 entry and in LOCK-m-F3 v0.2. |
| `scripts/mf3_sessions.py:273` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's stage_identity_extra for "id" carried): G-ID-F3's identity is built as G-TIME-F3's, below, citing the same lock (ID_LOCK_FILE), with reasoning_cap ID_REASONING_CAP and no locked_path (m's "G-ID-F0m carries none"; the path is recorded at LOCK-m-F3 v0.2, lock §1); stages._extra validates it for "id" as a run on a model, which refuses any cap but 120 and a locked_path. |
| `scripts/mf3_sessions.py:375` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's stage_precheck for "id" carried, scripts/m_sessions.py): at G-ID-F3 the checks are G-TIME-F3's, below, on G-ID-F3's committed schedule files (A2s and A3s) and its own checkpoint (stages.out_paths("id"): the path itself, an ENDED one, one on disk without --resume and no end pending), and two more, m's: the prior -- id_prior_checkpoint, then stages.prior_gate with require_real on, as the stage makes it after the load (G-TIME-F3 ended PASS, under this proposal, not written on the stub, at the cap of record, which is this run's) -- and an existing G-ID artifact, a link included, unless G-ID-F3's own checkpoint carries an end pending. Only this precheck refuses a link at the artifact path that does not resolve (the stage tests exists() alone), as in m. Made only by the stage after the load, beside the list below: on a re-finish of G-ID-F3's own pending end, the artifact's byte-identity with the one the finish re-derives (stages._finish_gid's G-ID ARTIFACT DIFFERS). |
| `scripts/mf3_sessions.py:571` | docstring | PIN (Code, declared at LOCK-m-F3 v0.2; the id wiring; m's _run_stage "id" branch carried): G-ID-F3 runs the Qwen path below as G-TIME-F3 does, its stage_identity_extra and stage_precheck for "id", and then stages.run_gid_pair_f3 with the prior id_prior_checkpoint gives at this run's out root -- the path the precheck read; the stage's prior_gate reads it again after the load -- its own checkpoint the stage's default, and the resume flag; the stage itself refuses an existing artifact (B7). |

- **The revised WIRED_CMDS sentence**, in the PIN that opens at `scripts/mf3_sessions.py:92` (its lines `:98–99`), verbatim:
  "qual and campaign stay refused until their steps; id is wired at its own step (the id wiring's PIN, below)."
  At the `id` wiring it replaced "id, qual and campaign stay refused until their steps."
- **The plural** (Code's form, `gt:`§5).
  - The same PIN says "the step-10 read's Q2 condition, which Code reads F-1's "with the same scope" as carrying".
  - The step-10 read's Q2 names four conditions. The `time` wiring's entry calls this "one of the step-10 read's four
    Q2 conditions".
  - v0.2 reads the PIN as the plural, "conditions".
- **The snapshot-revision refusal** (Code's form, `gt:`§5).
  - Before the load, `run_stage` refuses a refs/main other than the lock's weights revision: m's REVISION_STAGES
    refusal, extended to `time` at the `time` wiring and to `id` at the `id` wiring.
  - After the load, the re-read's SNAPSHOT MOVED stands beside it.
- **R3's anchors, re-anchored:** the re-issue's R3 cites `scripts/mf3_sessions.py:88` (the TIME_* PIN) and `:95` (the
  re-issue's PIN) on blob `1b593ba0…`. In the blob of record they are at `:102` and `:109`.
- **F-1:** the `id` wiring touched no scoring-stack function, so G-SHAPE-F3 was not re-run (its entry, `fb82daa`).

## v0.2 §6. The counters and the first-pick shares (A-m2 v0.5 §3.4; m:318 exception (2); rule 23)

- **G-TIME-F3's re-run** (`93ecaf9`; the seat's `r2:`§1–§2):
  - the bars: `round_degeneracy@G-TIME-F3` 0/30 and `reasoning_line_defect@G-TIME-F3` 0/18 (critical 5 each);
  - counter (a): 0 of 18 sham lines;
  - counter (b): 3 of 42 (A1s free rounds 8, 9 and 10), confirmed;
  - the sham first-pick shares: A1s 1/1, A2s 1/1, A3s 0/1.
- **Beside it, the first run** (`acc3b52`):
  - its sham first-pick shares were 1/1, 0/1 and 0/1;
  - its 13 sham lines held 9 banners and 2 frames;
  - the counters are declared from the re-run on (A-m2 v0.5 §3.4).
- **G-ID-F3** (`efb7bef`; the seat's §2):
  - counter (a): 2 of 12, descriptive;
  - counter (b): 0 of 20, confirmed;
  - the first free pick: P on both halves.

## v0.2 §7. Code's two BUILD readings, strikable until v1.0 (`r2:`§5 item 4; the routing's item 6 of 2026-11-10)

| reading | site | the PIN (verbatim) |
|---|---|---|
| `m.audit.qwen_ends` in counter (b)'s G-TIME-F3 contrast branch | `valence_core/mf3/lines.py:202` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; the build review's findings 1 and 2): every task round of a full record carries its audit (scaffold's round record), so a round with no audit mapping is refused -- the domain fails closed -- except in G-TIME-F3's contrast read, whose rounds keep {phase, ri, n, text} only (ruling (h); m.readrule.TIME_ROUND_KEEP). There the claimed round follows from m.audit.qwen_ends, "forced -> any claim" under the lenient scope: a claimed forced round ends the session, so the one claimed round is the last one generated when the read says excluded_at_forced, and no other (Code's reading). Each candidate carries the record's path, which tells a G-ID-F3 pair's two members apart. |
| F6: `prior_gate` refuses a prior at another cap on a run on a model | `valence_core/mf3/stages.py:493` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "prior_gate (F6) reads the fixed cap as 120 unless its require_real is off"; F6 re-read): on a run on a model (require_real) the fixed cap is the cap of record, scaffold.CAP_OF_RECORD, whatever the trigger counts (§4.1: it is reported and moves nothing), and a prior G-TIME-F3 written at another cap -- the first run's form, at 60 -- is refused (Code's reading of F6 under §4.1: the prior's lines and the stage's are both at the cap of record). With require_real off -- the stub path, which alone may run at 60 -- the fixed cap is re-computed from the prior's own checkpoint, as at LOCK-m-F3 v0.1. |

- **The seat's rulings** (`r2:`§5 item 4):
  - `qwen_ends`: "accepted as Code's reading, strikable until v1.0";
  - F6: "accepted, it is v0.5 §4.2's sentence".
- **The routing's item 6** (`r2:`§8): "The BUILD entry's readings (`qwen_ends`; F6) accepted, strikable until v1.0".

## v0.2 §8. The departures ruled, cited by this file

- **`r2:`§4, Q3.** The harness's git-status listing at a compaction or at a session's or subagent's start: "Not a
  departure, mid-stage or after; nothing is needed."
- **`r2:`§4, Q4.** The F3 session's two bounds and the coordinating session's two: "inert; no strike".
  - From there, for every stage with contrast sessions, G-ID-F3 included "by the same form", the end notice carries
    the exit status and the word "ended", with no stamp and no window.
- **The seat's G-ID-F3 answers, §6:**
  - the pod session's note 1: "inert, no strike";
  - its note 2: a departure of the Q4 kind, disclosed, "inert in substance", "No strike";
  - the values-check's interval between two start-side stamps (the G-ID-F3 entry): "start-side stamps place no end;
    inert".

  Ledger (65) and (66) are the seat's.
- **Pending:** the coordinating session's dated note of 2026-11-11 (`15d2f70`) puts an observation on §6's ruling on
  the pod session's note 2 to the seat's next read.

## v0.2 §9. What follows

1. **The `qual` wiring** in `scripts/mf3_sessions.py`. The driver refuses `qual` until its step.
   - It is an edit of F-1's kind, and its entry names the edit and the DRIVER line's new blob.
   - It takes G-TIME-F3's re-run checkpoint by path and refuses the first (A-m2 v0.5 §4.3).
   - Code intends it to require v0.2's cap and path lines (v0.2 §2 and §3) in the lock's committed text, refusing an
     earlier blob, as m's `qual` required its v0.2's path line. The wiring's entry declares it (Code's; the routing
     does not ask it).
2. **G-F3**, m:297 verbatim (its bold dropped): "G-F3. 40 sessions, keys `m-f3|{template}|{s}`, own item keys, excluded: 8 each of the A1s, A2s, A3s templates (24 sham), 8 of the A3 template, 4 of the A1 template and 4 of the A2 template (16 contrast); each template's sessions cover pairs × maps as evenly as the count allows, start and clause order balanced across the template. Bars: hair triggers; `round_degeneracy` on the sham sessions' ≤ 240 rounds, p0 .05 (critical 19); reasoning-line defects on the sham sessions' ≤ 144 lines, p0 .10 (critical 22), numerator the union of the three classes of §2.6; contrast sessions reported beside; the seat's attractor tally on the contrast sessions' forced rounds; first-pick share for sham templates only. r for Q-F3 = pooled over all 40." Its bars agree with lock §8's G-F3 rows.
   - It runs uncached, at cap 120, on the PI's word (the routing's item 5).
   - It is announced to the coordinating session and serialized (≈ 15–22 h [E], v0.2 §4).
   - Its end notice carries "ended" and the exit status, with no stamp and no window.
3. **Then:**
   - the seat's read of G-F3 (m:271's redacted reads, the contrast forced rounds, the attractor tally);
   - G-PWR;
   - the PI's Q-F3 cap and LOCK-m-F3 v1.0, with D2 (m:298; D2 2026-12-22).

---

Where the re-issue's or v0.1's text below differs from v0.2, v0.2 is of record (the form of the re-issue's own rule, and of LOCK-p v0.2's).

# LOCK-m-F3.md — v0.1, re-issued under ADDENDUM-m2 v0.5 (2026-11-10)

*Q-F3's first lock, re-issued above its v0.1 text, which follows below verbatim: ADDENDUM-m2 v0.5 §4.3, "LOCK-m-F3 v0.1 is re-issued above its v0.1 text, which it keeps verbatim". This part records what §4.3 lists; v0.1's text (2026-11-07, committed at `1e79955`) runs from its own heading to the file's end. A stage cites the whole file by its sha256, which the re-issue's entry names.*

## R0. Status

- **Version:** v0.1, re-issued 2026-11-10, before the re-run of G-TIME-F3. LOCK-m-F3 v0.2 follows G-ID-F3 (m:296), as
  before.
- **On the PI's word.** The routing of 2026-11-10, A5, verbatim at RESULTS.md's close line (`0516832`): "… → G-SHAPE-F3
  and G-ANL-F3 re-runs → LOCK-m-F3 v0.1 re-issued (cites the list v2) → G-TIME-F3 re-run into Q-F3_time-r2.json at
  cap 120, announced, ≈ 2.5–3.5 h → STOP for the seat's read [go]". Its C2, verbatim at the close on `750a7dd`'s
  entry (`fc43249`): "LOCK-m-F3's re-issue and LOCK-p v0.2 cite v2."
- **The list of record:** the list of record v2 (`results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md`,
  §2; committed at `fc43249`) binds every session on this unit from 2026-11-10, in place of the sweeps ruling of
  2026-11-09, §2.
- **Generated, not transcribed:** R1's identity table and R3's verbatim blocks (the PIN tables and the register) were
  generated with a tool at the re-issue's HEAD (`reissue_gen.py`, Code's scratch; HEAD `23865fa`). Every file they
  hash or quote is committed there with identical working-tree bytes. R1's rulings table and the driver's flag line
  are Code's, typed and checked against the files. The prose is Code's, from the sources it cites.

## R1. The binding identity at the re-issue

| what | path or scope | sha256 | at v0.1 |
|---|---|---|---|
| the proposal of record | `PROPOSAL-m-gating-campaign-v1_11.md` | `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b` | unchanged |
| ADDENDUM-m1 v0.1 | `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md` | `ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001` | unchanged |
| ADDENDUM-m2 v0.5 | `ADDENDUM-m2-f3-reasoning-block-v0_5.md` | `f27505c556a3304097d2154698bcf4498927e692c7341aec5060803c833b5354` | new |
| the analyzer (G-ANL-F3) | `scripts/m_analyze.py` | `d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48` | unchanged |
| m's package | `valence_core/m/*.py` (`resume.package_sha256_of`) | `7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb` | unchanged |
| the Q-F3 closure (PIN-V2-12) | the base closure plus `LAZY_F3_MODULES`, 22 modules | `06a36cbfb4ab5dce94bc1f900d43cea93e667a4cbe64b69f24986f5847eb63e8` | new |
| the base closure | 15 modules | `a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b` | unchanged |
| mf3's package | `valence_core/mf3/*.py` | `098455d91d1ae32371c32cfe883a3ce90c51b7607526e38f5460346ce44dda13` | new |
| the driver (the DRIVER line's value) | `scripts/mf3_sessions.py` | `1b593ba0465c5cf1af4d5b47283456b32359b37e0e3974848aade0f1d31287c6` | new |
| G-SHAPE-F3's artifact | `data/mf3/gates/G-SHAPE-F3.json` | `ff3eaae5b1c6f0b660be418e42709132018d904e53657046367517c1243f1bf3` | new |
| G-ANL-F3's artifact | `data/m/gates/G-ANL-F3.json` | `c2b87ab6c00a9b61ff9265d33cf73aa0aeadcbf9470e7aee2435e004689dc08c` | new |
| Q-F3's schedules manifest | `data/mf3/schedules/manifest.json` | `c7b5df4405981cca40d86564828c854f45c65211f2b2e9c138d43fdacd2a3314` | unchanged |

- **Unchanged and not repeated:** the eleven m files and the weights of record.
  - `scripts/mf3_sessions.py hashes` at the re-issue's HEAD prints each m file's sha256 and the WEIGHTS line exactly as
    v0.1's §1 lists them below.
  - Those rows remain the lines the licence and the driver read: each m file on one line with its sha256, and one
    WEIGHTS line.
- **The values a non-stub stage's identity_extra carries beside the hashes:**
  - `renders_sha16` `a04f67b0e5105a05`, unchanged;
  - `reasoning_cap` 120, the cap of record, at every Q-F3 stage on a model, G-TIME-F3's re-run included (R2);
  - `locked_path` `"uncached"` at G-TIME-F3, unchanged.
- **How a stage cites this file:** v0.1's §1 item stands, with two changes.
  - **The cap.** `_extra` refuses any cap but 120 on a run on a model at every stage, and admits 60 on the stub path
    only. `prior_gate` reads the fixed cap as 120 on a run on a model. v0.1's 60 at G-TIME-F3 is now admitted on the
    stub path only, beside 120 (m:174's pair at every stage). Its trigger-fixed cap from G-ID-F3 on holds on the stub
    path only (R2; R3, F6, F8 and F19).
  - **The driver's `time`** passes this file's values:

    `--proposal-file PROPOSAL-m-gating-campaign-v1_11.md --lock-file LOCK-m-F3.md --analyzer-sha256 d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48 --package-sha256 098455d91d1ae32371c32cfe883a3ce90c51b7607526e38f5460346ce44dda13 --renders-sha16 a04f67b0e5105a05`

    It writes `data/mf3/ckpt/Q-F3_time-r2.json`, its report and reads named after it. Its precheck refuses an existing
    or ENDED checkpoint there and refuses the first run's checkpoint name, `Q-F3_time.json`, as a target.
  - **The licence's new (h):** in `stages.licence_problems`' words, "(h) the reasoning block's addendum, A-m2 v0.5
    (``banner.ADDENDUM_M2_REL``), committed with the working tree's bytes, its sha256 the pinned one, its F-b literal
    and cap the code's". Its sha256 is in the table above.
  - v0.1's line anchors in `valence_core/mf3/stages.py` refer to that file at `1e79955`.
- **The rulings this re-issue rests on** (each file's sha256 and the commit that added it):

  | ruling | file | sha256 | committed at |
  |---|---|---|---|
  | ADDENDUM-m2 v0.5 | `ADDENDUM-m2-f3-reasoning-block-v0_5.md` | `f27505c556a3304097d2154698bcf4498927e692c7341aec5060803c833b5354` | `7589c1d` |
  | the seat's answers on the v0.4 STOP (ruling (a)) | `results/raw/2026-11-10_a-m2-v04-stop_design-to-code_answers.md` | `a85b924930866191ab22e9ac9874a55fa9a3ff9c0b881f7d4aa34e04e7fb8faf` | `0516832` |
  | the list of record v2 | `results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md` | `6c1135f5c0113e994399a80a5338bc48e45fbea57d3f0dbe21925e4c323e6cdd` | `fc43249` |
  | the seat's read of the smoke | `results/raw/2026-11-09_a-m2-smoke_design-to-code_answers.md` | `f13447d9e9c018a0fc7b3e2651948225ccc4da6078470bfdcb98aa7012b273cd` | `50fea90` |

## R2. What the re-issue records (A-m2 v0.5 §4.3's list, in its order)

- **The fire** (§0).
  - G-TIME-F3 (`acc3b52`) computed PASS on an echo domain that v0.1's F25 and F28 narrowed. Under m:265's domain, "the
    bar reads 9/13 against a critical of 4 at n = 13 and fires" (§0.2).
  - The seat ruled G-TIME-F3 STOPPED before G-ID-F3, and re-specified; the dated correction on its entry is at
    `daca8b0`.
  - The first run's sessions, picks and reads stay where m:271 and m:318 put them. Its checkpoint,
    `data/mf3/ckpt/Q-F3_time.json`, is never written again.
- **The class correction** (§1).
  - The echo class's domain is m:265's: every complete harness-written line of the session, up to the reasoning line
    in question (Code's P1).
  - Its match is equality after whitespace normalization.
  - Q8's containment is withdrawn from the bar and kept as counter (a) (§3.4).
- **The smoke's result and the selected form** (§3.5, §4.1).
  - The smoke (`6cfd3db`) ran four forms on sham sessions. Its rule selected F-b: 3 defect lines of 18, against F-a's 6.
  - Its second stop fired, so nothing was adopted then; the seat's read is at `50fea90`.
  - A-m2 v0.4, then v0.5, re-specified the block as F-b, with its exact bytes as A-m2 §3.1 gives them:
    `[round {n} | reasoning]\nReasoning (one line): So far,` (`valence_core.mf3.banner.REASONING_SEGMENT`).
- **The cap of 120, and m:294's trigger as report-only** (§4.1).
  - The cap is 120 at the re-run of G-TIME-F3 and at every later Q-F3 stage. The PI decided it on 2026-11-09 (the
    routing of 2026-11-09 (evening), A2).
  - m:294's trigger is reported at the re-run, as the count of lines at the cap, of ≤ 36, and moves nothing.
  - The bar is untouched: a line at 120 without a newline is a defect line under m:265 (v0.1's §8, bar 5).
- **The stub path's admission** (§4.2; ruling (a)).
  - In §4.2's words: "The cap of record binds on every run on a model; the stub path alone may run at 60."
  - The analyzer's battery drives mf3's stub chain at 60 (`scripts/m_analyze.py:10713`, `:10722`).
  - `scaffold.f3_config`'s per-stage table, `STAGE_REASONING_CAPS`, keeps m:174's pair (60, 120) at every stage, the
    caller choosing.
- **The new mf3 package hash and the driver's blob; the new Q-F3 closure; G-SHAPE-F3's and G-ANL-F3's new artifacts:**
  R1.
  - The BUILD is `5d40d59`. The re-runs are `0684263` (G-SHAPE-F3) and `23865fa` (G-ANL-F3).
  - Each earlier artifact is kept as `*.superseded-2026-11-10.json` beside its successor.
  - Four modules of the Q-F3 closure moved with the BUILD: mf3's `banner`, `lines`, `readrule` and `scaffold`.
- **The re-declared PINs F25 and F28, F29's correction, and the revised readings of F6, F8, F11 and F19:** R3.
- **The list of record, cited in one line:** R0.
- **The analyzer, unchanged.**
  - `scripts/m_analyze.py` is not touched (sha256 `d347ea0c…`). In §4.3's words, "its lexicons and counter (c) are
    unaffected by the block's form or the cap".
  - v0.1's §3 stands.

## R3. The PINs at the re-issue

- **F25 and F28 re-declared; F6, F8, F11 and F19 re-read; F29's sentence corrected.** Each is quoted verbatim from its
  site at the re-issue's HEAD. They replace v0.1's register rows for the same numbers (§9 below):

| PIN | site | at | the text at the re-issue (verbatim) |
|---|---|---|---|
| F6 | `stages.prior_gate` | `valence_core/mf3/stages.py:493` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "prior_gate (F6) reads the fixed cap as 120 unless its require_real is off"; F6 re-read): on a run on a model (require_real) the fixed cap is the cap of record, scaffold.CAP_OF_RECORD, whatever the trigger counts (§4.1: it is reported and moves nothing), and a prior G-TIME-F3 written at another cap -- the first run's form, at 60 -- is refused (Code's reading of F6 under §4.1: the prior's lines and the stage's are both at the cap of record). With require_real off -- the stub path, which alone may run at 60 -- the fixed cap is re-computed from the prior's own checkpoint, as at LOCK-m-F3 v0.1. |
| F8 | `stages._extra` (the check) | `valence_core/mf3/stages.py:621` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "stages._extra (F8's site) refuses any cap but 120 on a non-stub run and admits 60 on the stub path only"): m:174's pair on the stub, at every stage; the cap of record, scaffold.CAP_OF_RECORD, alone on a run on a model. |
| F8 | `stages._extra` (its docstring PIN, opening at `:598`; the revised sentence) | `valence_core/mf3/stages.py:602` | The reasoning cap (A-m2 v0.5 §4.1-§4.2; F8 re-read): the cap of record, 120, on a run on a model at every stage, G-TIME-F3's re-run included; m:174's pair, 60 or 120, on the stub, which alone may run at 60; from G-ID-F3 on, the cap prior_gate fixes. |
| F11 | `stages.cap_trigger` | `valence_core/mf3/stages.py:1040` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "stages.cap_trigger (F11) keeps its count and reports it"; §4.1: "m:294's trigger is reported at the re-run -- the count of lines at the cap, of <= 36 -- and moves nothing (m:174 names no value beyond 120)"; F11 re-read): ``cap`` is the run's reasoning cap, its checkpoint identity's. The count is as above. A run at 120 fixes 120 whatever the count; a run at 60 -- the stub path's, which alone may run at 60 -- fixes the cap by the count, as at LOCK-m-F3 v0.1. |
| F19 | `scaffold.f3_config` (cap) | `valence_core/mf3/scaffold.py:144` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "scaffold.f3_config's per-stage cap (F19's site; the build makes it a table) keeps m:174's pair, 60 or 120, the caller choosing, since it carries no stub signal"; F19 re-read): every stage admits STAGE_REASONING_CAPS[stage], m:174's pair. The cap of record (120, §4.1) binds every run on a model at stages._extra (F8), resume.Identity, stages.prior_gate (F6) and the driver; the stub path alone may run at 60 (§4.2). |
| F25 | `lines.domain` | `valence_core/mf3/lines.py:52` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1, m:265; Code's P1 of the A-m2 pre-read; F25 re-declared): over the pieces, which tile the transcript, the span before ``upto`` splits into newline-terminated lines; a line is in the domain iff no model-written piece (generation, reasoning_text) touches it: none overlaps any of its characters, its newline included, and no zero-length one sits within it. A model text can hold a newline, so overlap, not a piece's start, decides. Every other piece kind is the harness's. An unterminated final fragment is not a complete line. Each line is kept as rendered (labels included); distinct by its ws_norm form, first occurrence kept; each non-empty after ws_norm (asserted: no harness line of F3 is blank). So the banner, its Note lines, every round header, every Task line, every menu line and the pick line as rendered are in it; a Response line and, under F-b, the reasoning label line are not (the model continues each). |
| F28 | `lines.classify_line` (echo) | `valence_core/mf3/lines.py:155` | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1: "equality after whitespace normalization (runs of whitespace collapsed, ends stripped; case-sensitive)"; F28 re-declared): echo = the first line of the domain (``echo_set``, domain order) whose ws_norm form equals the line's; Q8's containment is withdrawn from the class and is counter (a)'s. |
| F29 | `lines.review_counter` | `valence_core/mf3/lines.py:265` | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q4): the unit is the generation (a task round or a reasoning line), keyed (template, kind, string); a generation containing two of the strings counts once under each. Its home is this module. At VERDICTS the analyzer is untouched: Code tabulates it with this module's functions over the same records in its own step, reported in the VERDICTS entry beside the analyzer's outputs (A-m2 v0.5 §3.4, which corrects F29's "the analyzer tabulates it" at the lock's re-issue). |

- **F29's correction, a dated note (2026-11-10; A-m2 v0.5 §3.4).**
  - v0.1's register gives F29's reading as "the analyzer tabulates it".
  - At VERDICTS the analyzer is untouched. Code tabulates counters (a) and (b) and the Q4 review counter with mf3's
    functions over the same records, in its own step, reported in the VERDICTS entry beside the analyzer's outputs.
- **PIN sites revised in place,** under their earlier "declared at" tags (the BUILD's review, round 2), with their text
  at the re-issue:

| site | at | its text at the re-issue (verbatim) |
|---|---|---|
| F29's site | `valence_core/mf3/lines.py:265` | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q4): the unit is the generation (a task round or a reasoning line), keyed (template, kind, string); a generation containing two of the strings counts once under each. Its home is this module. At VERDICTS the analyzer is untouched: Code tabulates it with this module's functions over the same records in its own step, reported in the VERDICTS entry beside the analyzer's outputs (A-m2 v0.5 §3.4, which corrects F29's "the analyzer tabulates it" at the lock's re-issue). |
| `_extra`'s docstring PIN (opening at `:598`; the revised sentence) | `valence_core/mf3/stages.py:602` | The reasoning cap (A-m2 v0.5 §4.1-§4.2; F8 re-read): the cap of record, 120, on a run on a model at every stage, G-TIME-F3's re-run included; m:174's pair, 60 or 120, on the stub, which alone may run at 60; from G-ID-F3 on, the cap prior_gate fixes. |
| `out_paths`'s docstring PIN | `valence_core/mf3/stages.py:101` | PIN (Code, declared at LOCK-m-F3 v0.1): m's layout under data/mf3 -- schedules/ (read only), ckpt/Q-F3_{stage}.json (pick-bearing; -diff), reports/Q-F3_{stage}_report.json and _reads.json (no contrast pick), G-ID-F3's artifact at guard.gid_artifact_path(). A-m2 v0.5 §4.2 keeps m's default stem here, for the stub; G-TIME-F3's re-run checkpoint and the refusal of the first run's live in the driver's precheck, which names the checkpoint (scripts/mf3_sessions.py), and for_checkpoint names the report and reads after it. |
| `assert_boundary`'s PIN | `valence_core/mf3/scaffold.py:176` | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8 on the "\n\n" after the reasoning segment, N6): the token-comparison form is valence_core.m.scaffold.assert_boundary (the adapters' own comparison; the boundary must be the prefix token count); the character-offset form decodes the first k tokens of the UNTRUNCATED joint encode, k the prefix token count, and requires exactly the prefix's characters (NFC-normalised, the Qwen tokenizer's own normaliser; identity on ASCII and on the stub). Every generation's prefix is the whole transcript so far, so a reasoning line -- an empty one leaving F-b's "So far," then its joiner's "\n" (A-m2 v0.5 §4.1; runner.py's check), or a newline-led one -- lies with its joiner inside a later prefix, and the assertion is exact over them. Either form failing is a BOUNDARY INCIDENT: HALT before the generation, escalate. |
| the driver's wiring PIN | `scripts/mf3_sessions.py:88` | PIN (Code, declared at LOCK-m-F3 v0.2; the time wiring; m's TIME_* form carried, scripts/m_sessions.py): G-TIME-F3 cites LOCK-m-F3.md (lock §1); one session per Q-F3 arm (m:293: "One session per Q-F3 arm (6), as G-TIME-F0"), the counts the committed time schedules carry (n 1 each); locked_path "uncached" (m:293, "G-TIME-F3 (Qwen, uncached)"); reasoning cap 60 at the first run (m:174), 120 from the re-run on (A-m2 v0.5 §4.1; the PIN below). The five flags are the lock's values, as LOCK-m-F0 §0's "How a stage cites this file" made them for m's driver. The values are Q-F3's; TIME_REASONING_CAP and TIME_FLAG_HELP have no counterpart in m. |

- **Code's readings declared at the BUILD.** Each is strikable by the seat until LOCK-m-F3 v1.0, at the cost v0.1's §0
  states:
  - **Counter (b)'s domain on G-TIME-F3's contrast read** (`lines.b_candidates`). It rests on `m.audit.qwen_ends`
    ("forced -> any claim" under the lenient scope): a claimed forced round ends the session, so the one claimed round
    is the last forced round of a session the read marks `excluded_at_forced`.
  - **F6:** on a run on a model, `prior_gate` refuses a prior G-TIME-F3 written at another cap.
- **The PIN sites declared at the re-issue:** every line of `valence_core/mf3/*.py` and `scripts/mf3_sessions.py` that
  opens `PIN (Code, declared at LOCK-m-F3 v0.1's re-issue`.

18 sites.

| site | where | its opening |
|---|---|---|
| `valence_core/mf3/banner.py:55` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; ADDENDUM-m2 v0.5 §4.1-§4.2): the reasoning block is F-b, |
| `valence_core/mf3/gshape.py:275` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: the selected form "verified at every stage s |
| `valence_core/mf3/gshape.py:454` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1; the build review's finding 11 carried): §1's |
| `valence_core/mf3/lines.py:52` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1, m:265; Code's P1 of the A-m2 pre-read; |
| `valence_core/mf3/lines.py:155` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1: "equality after whitespace normalization |
| `valence_core/mf3/lines.py:185` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §3.4, "Q8's containment, as a counter"; Code's |
| `valence_core/mf3/lines.py:202` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; the build review's findings 1 and 2): every task round |
| `valence_core/mf3/readrule.py:376` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §3.4: "a gate stage's entry reports (a) over its |
| `valence_core/mf3/resume.py:192` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "resume.Identity ... admits 60 only for an |
| `valence_core/mf3/runner.py:167` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §1, §4.2: "runner.py (the domain built |
| `valence_core/mf3/scaffold.py:144` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "scaffold.f3_config's per-stage cap (F19's |
| `valence_core/mf3/stages.py:186` | docstring | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: the selected form "verified at every |
| `valence_core/mf3/stages.py:380` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: the selected form is "verified at every stag |
| `valence_core/mf3/stages.py:493` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "prior_gate (F6) reads the fixed cap as 120 |
| `valence_core/mf3/stages.py:621` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "stages._extra (F8's site) refuses any cap b |
| `valence_core/mf3/stages.py:1040` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.2: "stages.cap_trigger (F11) keeps its count an |
| `valence_core/mf3/stages.py:1145` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §3.4: "a gate stage's entry reports (a) over its |
| `scripts/mf3_sessions.py:95` | comment | PIN (Code, declared at LOCK-m-F3 v0.1's re-issue; A-m2 v0.5 §4.1-§4.3): the re-run of G-TIME-F3 runs at the ca |

## R4. What follows

1. **G-TIME-F3's re-run** (A-m2 v0.5 §4.3):
   - six sessions on Qwen, uncached, on the same schedule cells and keys;
   - the bars under §1, the cap 120, and m:294's count reported;
   - written into `data/mf3/ckpt/Q-F3_time-r2.json`, its report and reads named after it;
   - announced to the coordinating session and serialized with any other laptop model run (≈ 2.5–3.5 h, §4.4);
   - then a STOP for the seat's read.
2. **G-ID-F3 at 120.** In §4.3's words, "the `id` and `qual` wirings take the re-run's checkpoint by path and refuse
   the first". Then:
   - LOCK-m-F3 v0.2, recording the cap and the path;
   - G-F3, G-PWR, and LOCK-m-F3 v1.0 with D2 (2026-12-22).
- **The self-test:** the BUILD's two driver checks that read this file's committed text (its review's finding 11) are
  expected to pass once this re-issue is committed. Code re-runs the self-test then.

---

Where v0.1's text below differs from the values and readings this re-issue records (R1–R3), the re-issue's are of record (A-m2 v0.5 §4.1–§4.3).

# LOCK-m-F3.md — v0.1 (Q-F3's first lock, PROPOSAL-m v1.11 §3.2 m:292, §8 step 19 m:361)

## 0. Header and status

- **Version** v0.1, 2026-11-07. This is Q-F3's first lock under `PROPOSAL-m-gating-campaign-v1_11.md` (m:292; entry
  name `LOCK-m-F3 v0.1`). The proposal's sha256 and every hash a stage's licence checks are in §1, except this
  file's own sha256, which its entry names. The lexicons', the schedule files' and the banner bytes' sha256 are in
  §3, §4 and §6.
- **Drafted and committed by Code on the PI's word.** The PI's routing of 2026-11-07, item 1, as the coordinating
  session relayed it and as quoted at RESULTS.md@139635f:79–81: "1. G-ANL-F3: hygiene commit (N9, N12) → G-SHAPE-F0/F3
  re-runs → canonical `ganl` → LOCK-m-F3 v0.1 → G-TIME-F3 [go]; N10 m:312 stands [confirmed]; N13 no change
  [confirmed]." The seat's answers of 2026-11-07, §9 item 1: "LOCK-m-F3 v0.1 (naming the analyzer, the lexicons, the
  re-run G-SHAPE-F3)".
- **m:292's list, and where each item is in this lock:**

  | m:292 | here |
  |---|---|
  | Q-F3's schedules and interleave rule | §4 |
  | keys | §5 |
  | the F3 verifier | §6 |
  | banner and reasoning-block bytes | §6 |
  | module homes | §5 |
  | the reasoning-line classes | §7 |
  | G-SHAPE-F3's result | §2 |
  | G-ANL-F3's analyzer and lexicon hashes | §1, §3 |
  | every bar of its later stages with class, unit, p0, α, domain and cadence | §8 |

- **What it binds:** Q-F3's stages from G-TIME-F3 to LOCK-m-F3 v0.2 (m:293–296). They are G-TIME-F3, the cap fixed
  by its trigger, and G-ID-F3. Each non-stub mf3 stage checks the licence of §1 at its start
  (`valence_core/mf3/stages.py`, `licence_problems`). LOCK-m-F3 v0.2 records the cap, the path and the projections
  (m:296). G-F3, G-VER, G-PWR and LOCK-m-F3 v1.0 with D2 follow (m:297–298).
- **Code's readings declared here** (§9, and N10's condition in §3) are each a flag the seat may strike until
  LOCK-m-F3 v1.0, "at the cost Code states" (the F3 prebuild answers, line 50). Striking one moves the hash of its
  site's file. That is the analyzer's or mf3's package, both named here, or the driver's (F57's site,
  `scripts/mf3_sessions.py`), which this lock does not name. N10's condition has no site: striking it means building
  the count, an analyzer change, which moves the analyzer's hash.

## 1. Binding identity and the licence by file

- The tables and the verbatim blocks in §1–§9 were generated with a tool at the lock's HEAD (`lockgen.py`, Code's
  scratch), with one exception: the N10 quotation in §3, which Code typed, verbatim from the seat's answer. Nothing
  generated is transcribed by hand. The dated notes, and the counts and abbreviated hashes in the prose of §2, §3
  and §10, are Code's text, taken from the sources they cite. Every file the tables list is committed at HEAD with
  identical working-tree bytes.
- `package_sha256` follows `valence_core.m.resume.package_sha256_of`'s rule, over `valence_core/m/*.py` (m's) and
  `valence_core/mf3/*.py` (mf3's). The closures' sha256 is `scripts/m_analyze.py`'s `closure_sha256` (PIN-1's form).
- **The licence (Q1 (C2)).** Every non-stub mf3 stage checks, at its start:
  - HEAD known;
  - the proposal and this lock committed, with the working tree's bytes;
  - the analyzer's sha256 and mf3's `package_sha256` as computed now;
  - each of the eleven m files below as hashed now;
  - this lock's committed text naming verbatim the analyzer's sha256, mf3's, and the weights' revision and sha256,
    and each m file by path and sha256 on one line;
  - the weights of record, offline (`HF_HUB_OFFLINE` exactly "1", the hub cache's `refs/main` the bound revision, the
    binding recomputed on that snapshot).
- The Q-F3 VERDICTS reader (`scripts/m_analyze.py`, PIN-V2-12) refuses unless this lock names the analyzer's sha256,
  m's `package_sha256` and the Q-F3 closure's sha256.
- **How a stage cites this file** (`valence_core/mf3/stages.py`, `_extra` at :556, its PIN in the docstring; LOCK-m-F0
  v0.1's item of the same name, for Q-F3's keys).
  - A non-stub Q-F3 stage's `identity_extra` carries `lock_file` = `"LOCK-m-F3.md"` and `lock_sha256` = the sha256
    of this file as committed. The `LOCK-m-F3 v0.1` entry names it (a file cannot contain its own hash).
  - The hashes and the weights it carries beside those are this section's tables. `renders_sha16` and
    `reasoning_cap` are in the generated list below. The keys are:
    - `proposal_file` = `"PROPOSAL-m-gating-campaign-v1_11.md"` and `proposal_sha256`;
    - the analyzer's `analyzer_sha256` and mf3's `package_sha256`;
    - `m_module_sha256`, mapping each of the eleven m files to its sha256;
    - `weights_revision` and `weights_sha256`, the WEIGHTS line's;
    - `renders_sha16` and `reasoning_cap`.
  - G-TIME-F3 also carries `locked_path` `"uncached"` (m:293). `_extra` refuses `"cached"` there and any reasoning cap
    but 60. G-ID-F3 carries no `locked_path`: the path is recorded at LOCK-m-F3 v0.2 (m:295–296).
  - At stage start the licence by file (`licence_problems`, :280) checks every key above except `renders_sha16`,
    `reasoning_cap` and `locked_path`.
    - `renders_sha16` is checked against the renders of record built at stage start (`_renders_of_record`, :619).
    - `reasoning_cap` is checked by `_extra`: 60 at G-TIME-F3, and 60 or 120 from G-ID-F3 on. From G-ID-F3 on it
      is also checked by `prior_gate` against the cap G-TIME-F3's trigger fixes ("NOT THE FIXED CAP", :466–477).
    - `locked_path` is checked by `_extra`, and against the path this backend's G-ID licence gives (`_locked`,
      :642).
    - None of these three is compared with this file's text.
  - `prior_proposal_sha256s` is **none under this file**. No earlier proposal is re-adopted. G-TIME-F3 takes no
    prior stage. G-ID-F3's and G-F3's prior is G-TIME-F3 (`PRIOR_STAGE`, :397), which runs under this proposal. So a
    stage either omits the key or passes `[]`. Either way the checkpoint's licence records `[]` (`_record_licence`,
    :491), and a resume or re-finish licensed by other values is refused.
  - A driver passes this file's values. The `time` subcommand is wired at its step, after this lock's commit (§11).
    How the subcommand takes the values is that wiring's, and its entry declares it.

#### The binding identity (computed at the lock's HEAD)

| what | path or scope | sha256 |
|---|---|---|
| the proposal of record | `PROPOSAL-m-gating-campaign-v1_11.md` | `42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b` |
| ADDENDUM-m1 v0.1 | `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md` | `ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001` |
| the analyzer (G-ANL-F3) | `scripts/m_analyze.py` | `d347ea0c9b69f73ced13484f3683f0b52f79a826cc9963a81359b2adc2205e48` |
| m's package | `valence_core/m/*.py` (`resume.package_sha256_of`) | `7756dcf42532b222b50e3bd8f41e2dc20053fa0a7a2b60e033dda559666349bb` |
| the Q-F3 closure (PIN-V2-12) | the base closure plus `LAZY_F3_MODULES`, 22 modules | `d19f336dc69e987b7be0b69d84d32f4a55cc47c8f4728c0f13b0378608cbf039` |
| the base closure | 15 modules | `a3bc7bb9df3d8361bfa803238e61a61a7eef76a6d839540413e53cd7919cb22b` |
| mf3's package | `valence_core/mf3/*.py` | `f30ad5053904ac222a81fa220f142b5f11f4da7965fdb8cdb83cd9b19e786310` |
| G-SHAPE-F3's artifact | `data/mf3/gates/G-SHAPE-F3.json` | `0c9de56e17d0872851f941473933c4811a79e754cfd99ebcdf589ca5f4e91461` |
| G-ANL-F3's artifact | `data/m/gates/G-ANL-F3.json` | `b91a8c672e85f1d493444c6b6388588ab0a646a8c36971320421c9f03aef936c` |
| Q-F3's schedules manifest | `data/mf3/schedules/manifest.json` | `c7b5df4405981cca40d86564828c854f45c65211f2b2e9c138d43fdacd2a3314` |


#### The eleven m files mf3's licence hashes (Q1 (C2) part (b); one line each, as `stages.licence_problems` (f) reads them)

| file | sha256 |
|---|---|
| `valence_core/m/__init__.py` | `b5175bcb6a521ef277de105315dd8d2f637a7b03e5d7baf30406dd83d0db35c4` |
| `valence_core/m/audit.py` | `16d0abb91444af1b86dcdabdca919f8e61ce371055fe9581a96d02eb950e50f6` |
| `valence_core/m/banner.py` | `730442ca354d8d92fe52135d42506cd83cef2d10deb7dfc23d0a1c204a6d170c` |
| `valence_core/m/bars.py` | `e7f028d8a08c70d29b03296276dc292d8a4042a0e20ac8e6f0c70540b91e1d6c` |
| `valence_core/m/corr.py` | `74818109a284d203177bae82170cbfa1f2cec8cbd85dfa2f7db018530eb27fce` |
| `valence_core/m/guard.py` | `6aa5ac2dc7a7e071ad848053aa1a7e73c9539d1d5cb6fe1152b0f11e7a4d8b87` |
| `valence_core/m/keys.py` | `a7d5ee3a9cde0deed785df204ae840cb56ee0e1eeefa9192fe1c1b0abb6b3beb` |
| `valence_core/m/readrule.py` | `fca9e7329ec42419ed0eaa658d1a954b68db0e05a93cbb6b3a4502f781737a9e` |
| `valence_core/m/resume.py` | `78f2fc8eb8b3b16ffa39c6dac7022b37dc98d8d002f50390d5c4540f22bf8fb7` |
| `valence_core/m/scaffold.py` | `39d8b32f193c1b0a64705dbb3e5557759f3f046158af85cde31870a53c0921d5` |
| `valence_core/m/schedule.py` | `f262f9e0120bcf6e694c0850b56dc3a19ab3c931b28ba92d47009f9f49a72d0d` |


#### The weights of record (Q6; `stages.licence_problems` (g))

- WEIGHTS mlx-community/Qwen3.6-27B-4bit revision c000ac2c2057d94be3fa931000c31723aac53282 sha256 03922eed43c73bf4af06cf4c51982005d95640dc6f39b57caf604749cf001e26


#### The values a non-stub stage's identity_extra carries beside the hashes above (computed from the code)

- `renders_sha16` `a04f67b0e5105a05`: the renders of record (`scaffold.pool_and_renders`, `m_corr.renders_sha`), as `stages._renders_of_record` builds them at stage start.
- `reasoning_cap` 60 at G-TIME-F3 (`scaffold.REASONING_CAPS` = (60, 120)); from G-ID-F3 on, the cap G-TIME-F3's trigger fixes (3 or more lines at the cap without a newline: 120).
- `locked_path` `"uncached"` at G-TIME-F3. The checkpoint's licence records `analyzer_sha256`, `lock_file`, `m_module_sha256`, `package_sha256`, `prior_proposal_sha256s`, `proposal_file`, `weights_revision`, `weights_sha256` (`stages.LICENCE_KEYS`).


#### The rulings this lock rests on (each file's sha256 and the commit that added it)

| ruling | file | sha256 | committed at |
|---|---|---|---|
| the F3 prebuild answers | `results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md` | `aec58440c8b1774bef1277bd29865b72cd1cc385e6c507e159ab82814fb64df3` | `dc1ffe1` |
| the G-ANL-F3 answers | `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md` | `4edfbb8e3d08844e47a329a951f9c2dd381115f0fd92c8b2b77f2207777ca42e` | `54bbfe5` |
| the G-CAL-OLMo answers | `results/raw/2026-11-06_gcal-olmo_design-to-code_answers.md` | `4c3f57d4ec4c1404026bceb2dc2f07141ef36e3d1af66705a5f383dff148bf82` | `0f35954` |
| the p pre-read answers (the FLAG rulings) | `results/raw/2026-11-07_p-preread_design-to-code_answers.md` | `ab40f470b93a7eae58a9f1552eab17e166d6159c3f0bdac917627fc7385cb08b` | `139635f` |
| the N1 battery answer (order (b)) | `results/raw/2026-11-07_n1-battery_design-to-code_answers.md` | `6b711d946f331201262242dd053d51dbb5447c6403e3d0fc86d853f5d7d5b409` | `f105bdd` |
| ADDENDUM-m1 v0.1 | `ADDENDUM-m1-olmo-reregistration-and-qf3-start-v0_1.md` | `ea08322d601011923524021832d27d0ddf57b3e51ee4d88f265985c6c9bf9001` | `f26bc59` |


## 2. G-SHAPE-F3 (m:290): PASS, re-run on `993eba1` (`f9700ba`)

- **The re-run of record:** `python scripts/mf3_sessions.py gshape` on HEAD `993eba1`, after the hygiene commit and
  after G-SHAPE-F0's re-run, as the seat's answers of 2026-11-07 §7 order it. It writes
  `data/mf3/gates/G-SHAPE-F3.json` (sha256 in §1).
- **The result:**
  - Layer A: A1 2,816, A2 1,408 and A3 1,408 placements, 0 fired, coverage exact, every required control firing on
    every placement.
  - Layer R: 8,448 line placements, 0 fired.
  - Layer S: 0 problems.
  - Layer T: 640 joins, 0 failed.
- The superseded artifact (`0f9b7bb9…6e9c`, the BUILD (F3) commit's run) is at
  `data/mf3/gates/G-SHAPE-F3.superseded-2026-11-07.json`. The two differ only in provenance (mf3's package, its
  sources); every result is identical. The entry is at RESULTS.md (`f9700ba`).

## 3. G-ANL-F3 (m:291): the analyzer and the lexicons

- **The analyzer** is `scripts/m_analyze.py`, extended in place at `e0b4f2c` (G-ANL-F3 — BUILD). Its sha256 is in §1.
  It was edited once more in place at `10a2bbb` (the check fix, order (b): the seat's answer of 2026-11-07 on N1, §1,
  at `f105bdd`). That moved its sha256 from the BUILD's `6ec3222b…93d9` to the value in §1 before any lock or
  G-ANL-F3.json named it. m's three OLMo NOT-RUN outputs (`0f35954`) stay bound to `6ec3222b…`, the blob that wrote
  them (PIN-42).
- **The canonical run** wrote `data/m/gates/G-ANL-F3.json` (sha256 in §1; its entry `02dadb3`): the battery
  passes 525/525 and reaches all 538 coverage ids; v1's 2,160 evaluations are unchanged, and the v2 space's 519,480
  tuples are each asserted. A second run to a test directory wrote the same bytes.
- **The lexicons**, frozen here (m:292: "G-ANL-F3's … lexicon hashes"). They are counter (c)'s stage-1 terms, polarity
  terms and window (m:312 (c)), as the analyzer carries them and as the artifact's `g_anl_f3.counter_c` block records
  them. Their sha256 is declared below.

#### Counter (c)'s lexicons (m:312 (c); frozen here; `scripts/m_analyze.py`)

- stage-1 terms (19): `corrupt`, `corrupted`, `corruption`, `garbled`, `garble`, `typo`, `typos`, `misspelled`, `misspelling`, `scrambled`, `jumbled`, `mangled`, `broken`, `clean`, `correct`, `intact`, `fine`, `readable`, `legible`
- negative polarity (8): `corrupt*`, `garbl*`, `typo*`, `misspell*`, `scrambl*`, `jumbl*`, `mangl*`, `broken`
- positive polarity (6): `clean`, `correct*`, `intact`, `fine`, `readable`, `legible`
- window: ±6 tokens
- the lexicons' sha256 (compact sort-keyed JSON of the G-ANL-F3 artifact's `g_anl_f3.counter_c` block, as built by `_g_anl_f3_block`): `1b7d5a01af967d9f7953168dbce3468c562602b9f754069041f32b740d088028`


**Dated note, 2026-11-07 (N10; the seat's ruling: "m:312 stands as pinned; no revision before the lexicons freeze at
LOCK-m-F3 v0.1").** m:312's nearest-term rule, as the scorer applies it (PIN-V2-13), scores a line such as "prism is
clean, slate is corrupted" ambiguous. After punctuation is stripped, slate's nearest polarity term within the window
is "clean", one token back, and "clean" is also prism's nearest term. A shared nearest term makes the line
ambiguous. The battery asserts this case as written (`scripts/m_analyze.py:10513`). It is PIN-V2-13's known
limitation, and the rule stands. The seat's two reporting terms, neither an analyzer change:

- The first term, verbatim (Code's typing; the one verbatim block of §1–§9 not generated):

  > if the scorer's output already records the ambiguity's cause, the "same polarity, shared nearest term"
  > subclass is reported as its own count at Q-F3's VERDICTS

  - The scorer's output (`score_line_c`, `scripts/m_analyze.py:3472`, kept per line in counter (c)'s key items)
    records the line's class and each label's polarity, not which term was nearest.
  - So it records the shared polarity but not the shared term, and no such count is built.
  - This is Code's reading of the condition, and the seat may strike it.
- "the seat's blind read scores such lines by (label, polarity) as m:312 has it."

## 4. Q-F3's schedules and the interleave rule

#### Q-F3's schedule files (`data/mf3/schedules/manifest.json`)

- schema `m-schedules-manifest-v1`; construction: PROPOSAL-m v1.11 m:159-172 (Q-F3); 20 files:

| file | sha256 |
|---|---|
| `Q-F3_campaign_A1.json` | `cfc8df1a11214061206ee4d28a800ef14201c0d7e0aa70b8cb123d75c8846eeb` |
| `Q-F3_campaign_A1s.json` | `f3a0682bf1fead75712f2118f6b21c6ec83d10e2df36222be85528df490caee2` |
| `Q-F3_campaign_A2.json` | `a33df12c2dd1f534a4fff818f329cca5b43304c0fcf6547c7d057c1b31af02cb` |
| `Q-F3_campaign_A2s.json` | `319180e54c7f6e225a88b38186e14b887ed53c92fe5cea8f2baedb91615b4d17` |
| `Q-F3_campaign_A3.json` | `13bd869785f81c7527851bc84fc1226ad3b2fa79e22da54af171cf4e89aee059` |
| `Q-F3_campaign_A3s.json` | `de0826c8b643de64550a57bcaaa0fd1a302f22644ca4b3a6693dcd93035814e2` |
| `Q-F3_id_A2s.json` | `aac9cddf059c8334f9854a41876feda1bf1e860f5d6c7c0be94cda97c0af1740` |
| `Q-F3_id_A3s.json` | `ad5671cb5f1fc685ed992dfd2508afe154a1b48c501836a0a9462879b6fe2fad` |
| `Q-F3_qual_A1.json` | `8e023de668481f1450ea647f62f13c3c3cd08d5e553c410b8ece686c23f9dea0` |
| `Q-F3_qual_A1s.json` | `67acb9581556ba78c28c09e278596807fe89952ad76184aa205e68be0bbdc07b` |
| `Q-F3_qual_A2.json` | `38bcc425d568fcb18f1bc3bb789da35d94163544f81faba58b33d53062555223` |
| `Q-F3_qual_A2s.json` | `a0199a2cac2729b1d36950a303cb39182b64fb1e868d0052aafb88c186560500` |
| `Q-F3_qual_A3.json` | `a07b9a859036d94c956b5a00fca90d473cab5c4a80b9dd1535e80d72170b5eb2` |
| `Q-F3_qual_A3s.json` | `001cef2c96e6924402dd332ae685259e460157dfc7c08579c125655cd69909df` |
| `Q-F3_time_A1.json` | `493e3ae7969f9b9569b59af76976d73593dd3525b75416e1c6b364fb6423c6da` |
| `Q-F3_time_A1s.json` | `0a374318e7083233fa6068b4864de6e3e07f42d151bab2d6d4a3e98d94d7949f` |
| `Q-F3_time_A2.json` | `f857324bbd9d28a15b1364576fde052a2d506a60d7c40a5f0411c7271bad45fe` |
| `Q-F3_time_A2s.json` | `27abc7b2972c265fb79925d086e6573c5521d7b4fbf933124927117c18d50753` |
| `Q-F3_time_A3.json` | `13b1f9d65778cd0ba2626ea5ec50055f607e7d0c41dc826a946888be5979a98d` |
| `Q-F3_time_A3s.json` | `cdd9af288ba07633a2193b49d1e19bc2a7c1dea346e6f5bd64c5b1a5a45fdebe` |


#### The schedules and the interleave rule (`valence_core.mf3.schedule`'s docstring, verbatim)

```text
Q-F3's schedules: campaign balance units, gate-stage schedules, the gate-stage launch order and
the six-arm interleave (PROPOSAL-m v1.11 §2.1 m:159-172; §2.4 m:184-192, m:216-243; §3.2 m:293-297).

The CONSTRUCTION is ``valence_core.m.schedule``'s, imported: ``campaign_cells`` (pair x map x start
x clause, clause only where the TOLD line names labels -- A1/A1s; A2-A3s have no clause factor, so
16 cells), the sixteen-row ``GATE_TABLE`` (m:161-170), ``balance_report``, ``cells_sha256``, the
file layout ``dumps_schedule`` and the launch rule ``_n90_launch``. m's ``campaign_schedule``,
``gate_schedule``, ``interleave`` and file writers refuse Q-F3 (they key on keys.UNITS_BUILT), so
the Q-F3 forms are here, keyed by ``mf3.keys``.

FILES under ``data/mf3/schedules/`` with their own ``manifest.json`` -- ``data/m/schedules/`` and
its manifest are untouched (the seat's Q1). Six campaign files (one per arm), six G-TIME-F3 files
(n 1), two G-ID-F3 files (A2s, A3s; sixteen rows available) and six G-F3 files (A1 4, A1s 8, A2 4,
A2s 8, A3 8, A3s 8; m:297): 20 files plus the manifest.
```


#### The interleave rule and the gate-stage launch order (`valence_core/mf3/schedule.py`: each function's signature, docstring and PIN, verbatim)

`valence_core/mf3/schedule.py:185`:

```python
def gate_launch_order(templates_with_counts: Sequence[tuple[str, int]]) -> list[tuple[str, int]]:
    """(template, j) launch list for a multi-template gate stage: strict rotation in §2.4's table
    order, a template leaving the rotation at its count."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's launch-order PIN carried to six templates --
    # the cross-template order is §2.4's table order (A1, A1s, A2, A2s, A3, A3s; G-ID-F3: A2s, A3s);
    # any other order given is refused, not re-sorted; within a template the table's order (m:159).
```

`valence_core/mf3/schedule.py:205`:

```python
def interleave(arms_in_order: Sequence[str], done: Callable[[str], bool],
               start_counts: Mapping[str, int] | None = None) -> Iterator[str]:
    """The next arm to launch: strict rotation by launch index in §2.4's order (A1, A1s, A2, A2s,
    A3, A3s), an arm at its floor leaving the rotation for good (m:172); ``done`` evaluated lazily
    before each yield."""
    # PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's interleave PIN carried to six arms -- next = the
    # live arm with the fewest launches, ties to table order (m.schedule._rotation, imported); the
    # resume counts are validated pairwise exactly as Q-F0's two-arm rule (a precedes b in table
    # order: both live -> b <= a <= b + 1; only a live -> a >= b; only b live -> b >= a - 1).
```


## 5. Keys and module homes

#### Keys (`valence_core.mf3.keys`; `stream` is m's)

- templates ('A1', 'A1s', 'A2', 'A2s', 'A3', 'A3s'); contrast ('A1', 'A2', 'A3'); sham ('A1s', 'A2s', 'A3s'); G-ID templates ('A2s', 'A3s').
- items: `m-f3-items|{s}`, gate `m-f3-items-time|{s}` (and `id`, `qual`).
- arm, time: `m-time|A1|{s}`
- arm, id: `m-id|F3|A2s|{s}`
- arm, qual: `m-f3|A1|{s}`
- arm, campaign: `m|A1|{s}`
- schedules: `m-sched|Q-F3|A1|{b}`; gate π `m-sched|Q-F3|time|A1|0`.


#### Module homes (`results/raw/2026-11-06_mf3-build_design.md` §3, verbatim)

- `__init__.py` — scope and the licence.
- `keys.py` — Q-F3's keys (m:159): items `m-f3-items|{s}` / `m-f3-items-{gate}|{s}`; arms `m|{arm}|{s}`, `m-time|{arm}|{s}`, `m-id|F3|{template}|{s}` (A2s, A3s), `m-f3|{template}|{s}`; schedules `m-sched|Q-F3|{arm}|{b}`, `m-sched|Q-F3|{gate}|{template}|0`; `stream` is m's. No Q-F3 key equals a Q-F0 or OLMo key (self-test).
- `banner.py` — the six F3 banners (A1 TOLD-MAP, A1s TOLD-MAP-SHAM, A2/A2s TOLD-OBJ, A3/A3s COMMON only) and the reasoning block, from m's constants; `spec_problems` against the proposal file and §2.4's banner column.
- `schedule.py` — campaign cells and balance units, the sixteen-row gate schedules (clause None on A2–A3s), the clause-free balance check, the six-template launch order and six-arm interleave, the files and manifest.
- `lines.py` — the reasoning line's three classes, its echo set, the Q4 review counter.
- `scaffold.py` — `F3Scaffold` (F2 block order; `reasoning(ci)` draws the line's seed before the menu order), `f3_config`, `F3Log` (the F3 record), the two-form boundary assertion, `prepick_excluded`.
- `runner.py` — `f3_startup` and `run_session_f3`.
- `verify.py` — G-VER for F3.
- `readrule.py` — F3's read rules, printed reasons, session lines and stage report.
- `bars.py` — `F3Bar` (m's `Bar` with Q-F3's vocabulary), the bar table, firing cases, the realised-n evaluation.
- `guard.py` — the cached-path licence (G-ID-F3's artifact at its cap), the static call-site guard (`valence_core.m.guard`'s scanner, subclassed with Q-F3's names), the import-set check, the forbidden-literal scan; m's insulation re-exported.
- `resume.py` — Q-F3's identity (Q-F0's keys + `reasoning_cap`, `m_module_sha256`, `weights_revision`, `weights_sha256`), `load_or_init`, the weights binding and the model of record's hub-cache directory; m's checkpoint machinery re-exported.
- `stages.py` — the gate stages, G-ID-F3, the campaign, the licence, the reports.
- `gshape.py` — G-SHAPE-F3.
- `testing.py` — the test double (self-test only).
- `scripts/mf3_sessions.py` — the driver.


## 6. Banner and reasoning-block bytes; the F3 verifier

#### Banner and reasoning-block bytes (`valence_core.mf3.banner`; m's constants by import)

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
| `reasoning_block(5)` | 44 | `f4ea7bcb9d1e1fb715005ab0416fdafe1d2c21644acede391795eed841d9f160` |
| `reasoning_block(6)` | 44 | `5a5d76642c5d98d5d67372bd120876fac2bd35d029d6de9b0c09e31e48e703ef` |
| `reasoning_block(7)` | 44 | `d4ac390283740bb2a3321aa921c07018f4fbfbef2842e26f045128a65d75619f` |
| `reasoning_block(8)` | 44 | `50146ea013f1c48616f5fb487b52c8d95a2d5e474e16e09277a681f5ffc73606` |
| `reasoning_block(9)` | 44 | `2793670756c2335c6393e64bd7b45c2d6af419853494ac02aaaf770646cef94a` |
| `reasoning_block(10)` | 45 | `f024bc11d6c9a4b6adce3138bdc80afab4cd8415c652d976ca5b682015643541` |


#### The F3 verifier (`valence_core.mf3.verify`'s docstring, verbatim)

```text
The F3 verifier -- G-VER for Q-F3 (PROPOSAL-m v1.11 §3.1 m:284, carried by m:298; §3 m:271's
``template_breakage`` and ``schedule_mismatch``; §2.1 m:159; §2.2 m:174; §2.5 m:253).

m:284: "every session's harness bytes reconstructed from its recorded fields, the committed schedule
and the rng streams before any artifact is written". ``verify_session`` rebuilds the session's
scaffold through the SAME code path the runner used (``scaffold.f3_config``) from the record's stage,
template, s, path and reasoning cap and the committed schedule's cell, replays it with the RECORDED
generations, reasoning lines and picks, and compares:

  schedule_mismatch -- the cell, the keys (m:159), the banner bytes and Note lines (§2.5), per round
      the label, role, pole, item, delivered text, property and seed, per reasoning line its seed and
      cap, per choice the menu order -- and the template's role: A2/A2s and A3/A3s carry one banner, so
      a contrast record must have served the corrupted render on its Q role and a sham record clean
      text throughout (Code's PIN, the template name decides, the delivery is asserted);
  template_breakage -- the harness bytes (banner; forced ``seg + text + "\n"``; per free choice the
      reasoning block + line + ``"\n"``, then ``menu + " {pick}\n" + seg + text + "\n"``), the
      pieces, round and menu numbering, each pick against its read (menu_a iff p_a >= p_b, verify KL
      exactly 0.0), each reasoning line's classes and scaffold hits re-derived from its text, and the
      record's own end rules (exclusion, strict scope, hair triggers, domain, first pick, completeness).

It never raises on a malformed record (a failure to report is template_breakage); messages name a
field and a phase, never a label, a pick or a free index.
```


## 7. The reasoning-line classes

#### The reasoning-line classes (`valence_core.mf3.lines`)

- `CLASSES` = ('empty', 'cap_no_newline', 'echo'); the review counter's strings `REVIEW_STRINGS` = ('You are a helpful assistant.', '4assistant', '<|end|>').


#### The reasoning-line classes (`valence_core.mf3.lines`' docstring, verbatim)

```text
The reasoning line's classes (PROPOSAL-m v1.11 §2.6 m:265, §3.2 m:293, §4 m:308, m:312 (f),
m:314; the design seat's prebuild answers of 2026-11-06, Q4 and Q8).

m:265: "The reasoning line is not a round (Q-F3). Scored only by its defect bar, counter (c), and the
`scaffold_absorption` hair trigger (the one hair trigger that reads it and can remove a session from
the primary's domain; the runner ends the session at that fire). Its defect classes: empty line; cap
reached without a newline; reasoning-line echo = a verbatim, whitespace-normalized reproduction of
any complete harness-written line of the session (v1.3's definition). Exempt from v2/v3, the
task-round echo class, lexical, and `earlier`; the frozen ban list applies to its generation."

So nothing here calls the task-round audit: a reasoning line never reaches v2, v3, the task-round
echo class or lexical, and never enters ``earlier`` (the runner's PIN). ``classify_line`` returns its
three defect classes (``reasoning_line_defect``'s numerator is their union, m:293) and its
``scaffold_absorption`` hits, beside the echo's matched line index.

The Q4 counter (the seat's answer: the three strings from Q-F0's VERDICTS read, declared as one
descriptive rule-23 counter, deciding nothing) is ``review_counter``, a pure function of the
records' generated texts, tabulated over all sessions, excluded included.
```


## 8. Bars

Every bar of Q-F3's later stages, generated from `valence_core.mf3.bars.QF3_BARS`. Its arithmetic is
`valence_core.m.bars`', imported unchanged.

#### The bar table (generated from `valence_core.mf3.bars.QF3_BARS`; m:292's class, unit, p0, alpha, domain, cadence)

| # | bar (`name`) | stage | kind | unit | numerator (k) | p0 | α | domain | cadence | planned n / critical | on fire |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `scaffold_absorption` | every | hair_trigger | model generation (a task round or a reasoning line) | generations containing a scaffold-set string | — | — (k ≥ 1) | every | evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271) | — | STOP the stage (m:271) |
| 2 | `template_breakage` | every | hair_trigger | session | sessions failing G-VER | — | — (k ≥ 1) | every | evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271) | — | STOP the stage (m:271) |
| 3 | `schedule_mismatch` | every | hair_trigger | session | sessions differing from the committed schedule | — | — (k ≥ 1) | every | evaluated as each generation / session is recorded; a fire anywhere stops the stage (m:271) | — | STOP the stage (m:271) |
| 4 | `round_degeneracy@G-TIME-F3` | time | binomial_stage_end | task round generated (<= 10 per session: 4 forced + 6 free) | rounds claimed by audit v2 or m's harness-echo class (m:261) | 0.05 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 30 / 5 | STOP before G-ID-F3 (m:293; the bars bind alone, m:271) |
| 5 | `reasoning_line_defect@G-TIME-F3` | time | binomial_stage_end | reasoning line generated (<= 6 per session, one per free choice) | reasoning lines with any of m:265's three classes (empty, cap without newline, reasoning-line echo) | 0.10 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 18 / 5 | STOP before G-ID-F3; the seat re-specifies (m:293) |
| 6 | `gid_divergence@G-ID-F3` | id | hair_trigger | complete cached/uncached pair (4 forced rounds + 6 x (reasoning line, read, chosen round) each) | complete pairs whose transcripts differ in any byte | — | — (k ≥ 1) | pairs | per complete pair, uncached first, A2s then A3s; stops at the first divergence (m:281, m:295) | — | G-ID-F3 FAIL: Q-F3 runs uncached (m:295) |
| 7 | `round_degeneracy@G-F3` | qual | binomial_stage_end | task round generated (<= 10 per session: 4 forced + 6 free) | rounds claimed by audit v2 or m's harness-echo class (m:261) | 0.05 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 240 / 19 | STOP: Q-F3 does not run until the seat re-specifies (m:297, m:271) |
| 8 | `reasoning_line_defect@G-F3` | qual | binomial_stage_end | reasoning line generated (<= 6 per session, one per free choice) | reasoning lines with any of m:265's three classes (empty, cap without newline, reasoning-line echo) | 0.10 | 0.05 | sham | once at stage end on the realised n; no mid-stage evaluation (m:271) | 144 / 22 | STOP: Q-F3 does not run until the seat re-specifies (m:297, m:271) |
| 9 | `round_degeneracy@campaign-Q-F3` | campaign | binomial_look | task round generated (<= 10 per session: 4 forced + 6 free) | rounds claimed by audit v2 or m's harness-echo class (m:261) | 0.05 | 0.05 | sham | every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look index in the resume identity (m:330) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 10 | `reasoning_line_defect@campaign-Q-F3` | campaign | binomial_look | reasoning line generated (<= 6 per session, one per free choice) | reasoning lines with any of m:265's three classes (empty, cap without newline, reasoning-line echo) | 0.10 | 0.05 | sham | every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look index in the resume identity (m:330) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 11 | `own_pair_lexical@campaign-Q-F3` | campaign | binomial_look | task round generated in A2s / A3s | task rounds claimed lexical under m:261's claiming order, forced and free | 0.02 | 0.05 | lexical_sham | every 40 launches and at the end, cumulative count, alpha .05 per look, no alpha spending; look index in the resume identity (m:330) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 12 | `exclusion_guard_fisher@campaign-Q-F3` | campaign | guard_fisher | session launched in the arm through the look (pre-pick exclusion) | pre-pick exclusions (sessions excluded before their first read: at a forced round or at reasoning line 1, m:308; the seat's Q8) | — | 0.05 | contrast_arm | at every look, per contrast arm (m:316) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |
| 13 | `exclusion_guard_abs@campaign-Q-F3` | campaign | guard_abs | session launched in the arm through the look (pre-pick exclusion) | pre-pick exclusions (sessions excluded before their first read: at a forced round or at reasoning line 1, m:308; the seat's Q8) | 0.20 | 0.05 | contrast_arm | at every look, per contrast arm (m:316) | — | PAUSE the unit for the seat's adjudication; never a verdict (m:330, m:316) |


- **Dated note, 2026-11-07: row 6's numerator predates the seat's F-7.**
  - The table generates row 6 from `valence_core/mf3/bars.py:197–202`, last edited at `cd9756e`. Its numerator
    reads "complete pairs whose transcripts differ in any byte".
  - The stage decides G-ID-F3 by the seat's F-7 criterion (`stages._gid_pair`, :1139, the F-7 PIN at :1140;
    `guard.GID_CRITERION`, `guard.py:46–49`). A pair is identical only if its transcripts are byte-identical **and**
    each reasoning line's (n_tok, cap_hit, stop_reason) triple is identical.
  - `gid_decide` (:1106) fails G-ID-F3 on a divergence in any pair, complete or not, and the bar fires on that FAIL.
  - F-7 governs. The row's text is not edited here: an edit to `bars.py` would move mf3's package, which this lock
    names.

## 9. PINs

- **Code's readings, declared at this lock.**
  - Two registers, each verbatim below: the F3 build's (F1 onward, the F3 build design §4) and G-ANL-F3's
    (PIN-V2-1 to PIN-V2-24, its build design §2).
  - N10's condition (§3).
  - The registers' sites are listed after them. F57's is the exception: its site, `scripts/mf3_sessions.py`,
    carries no PIN line.
  - Each reading is strikable by the seat until LOCK-m-F3 v1.0, at the cost stated in §0.
- **The seat's rulings set here** (not Code's readings):
  - F-6 (G-TIME-F3's contrast sessions report no per-line list before VERDICTS; "k of ≤ 36");
  - F-7 (G-ID-F3's identity criterion: m:281's byte-identical transcript pair **and**, per reasoning line, an
    identical (n_tok, cap_hit, stop_reason) triple; "A seat PIN at LOCK-m-F3 v0.1; set before G-ID-F3 has run.");
  - PIN-29's exception by blob (A1);
  - N10's (§3) and N13's (§10) terms.

#### The F3 build's PIN register, verbatim (`results/raw/2026-11-06_mf3-build_design.md` §4)

| # | site | reading |
|---|---|---|
| F1 | `guard.M_MODULES`, `guard.M_HASHED` | L1: the ten modules, the transitive production closure; `ABSENT_MODULES` asserted absent (N1); the licence hashes `M_HASHED`, the ten and m's `__init__.py` (finding 7) |
| F2 | `guard._gid_pass` | the licence is m's form plus `identity.reasoning_cap` equal to the asking cap |
| F3 | `stages.licence_problems` | L2's (a)–(g); (f) names each m file by path and sha256 on one line (finding 8); (g) `HF_HUB_OFFLINE` = "1" and `refs/main` = the bound revision (finding 5) |
| F4 | `stages.ANALYZER_PATH` | the analyzer is `scripts/m_analyze.py`, extended in place by G-ANL-F3 (Q3) |
| F5 | `stages.out_paths` | m's layout under `data/mf3` |
| F6 | `stages.PRIOR_STAGE`, `prior_gate` | G-ID-F3 needs G-TIME-F3 PASS; G-F3 needs G-TIME-F3 PASS and the G-ID-F3 artifact at the run's cap; the campaign needs G-F3 PASS. G-ID-F3 and G-F3 refuse any cap but the one G-TIME-F3's trigger fixes, re-computed from its checkpoint; the campaign refuses any but G-F3's (finding 4) |
| F7 | `stages.gid_artifact_problems` | an artifact at another cap is refused (B7) |
| F8 | `stages._extra` | identity_extra's keys; `reasoning_cap` 60 at G-TIME-F3; the stub's weights binding refused on a non-stub run |
| F9 | `stages._hair_hit` | the fired generation may be a reasoning line (phase "reasoning", its ci) |
| F10 | `stages._line_excerpt` | a line after the first pick lists the previous choice's pick as revealed |
| F11 | `stages.cap_trigger` | m:174's count over all six G-TIME-F3 sessions' lines (Q5); ≥ 3 → 120; applied from G-ID-F3 on (m:294–295), recorded at LOCK v0.2 (m:296) |
| F12 | `stages.gid_decide` | one complete identical pair per template, indices advancing per template (m:281's rule, Q8; N2); a divergence anywhere FAILs |
| F13 | `stages.run_gid_pair_f3` | a G-ID-F3 artifact is never overwritten (B7) |
| F14 | `stages._finish_gid` | G-ID-F3's reads are the full sham-only records (§4 exception (4)) |
| F15 | `stages.campaign_look` | the lexical bar's numerator and the beside counts (B23) |
| F16 | `stages.run_campaign` | an artifact at another cap refuses the campaign (B7) |
| F17 | `stages._campaign_report` | m's pick-free campaign report |
| F18 | `scaffold.f3_config` (path) | G-TIME-F3 uncached; G-ID-F3 both paths |
| F19 | `scaffold.f3_config` (cap) | G-TIME-F3 generates lines at 60; G-ID-F3 on, at the cap G-TIME-F3's trigger fixes (m:294–295; F6) |
| F20 | `scaffold.f3_config` (j) | j = s at gate stages, None in the campaign |
| F21 | `scaffold.assert_boundary` | rule 28(d)(a) in both forms at every generation (Q8; N6) |
| F22 | `F3Log.reasoning_hair` | a line's scaffold fire: hair {phase "reasoning", ci} and exclusion {class "scaffold", phase "reasoning", ci}; strict scope unchanged (Q8) |
| F23 | `F3Log.record` | complete = 4 forced + 6 × (line, read, round) |
| F24 | `scaffold.prepick_excluded` | pre-pick = forced, or reasoning with ci 0 (Q8's pre-pick count; m:308's domain: "up to and including the first reasoning line") |
| F25 | `lines.echo_lines` | the eight strings as rendered for the session + the headers written so far (Q8; N4) |
| F26 | `lines.classify_line` (empty) | ws_norm(text) == ""; with both EOS strings banned a whitespace-only line runs to its cap |
| F27 | `lines.classify_line` (cap) | stop_reason "cap" (Q8: the cap-length prefix kept, cap-reach); a newline as the cap-th token is not cap-reach |
| F28 | `lines.classify_line` (echo) | containment, case-sensitive, ws_norm, first match (Q8) |
| F29 | `lines.review_counter` | the Q4 counter: per (template, kind, string), all sessions; the analyzer tabulates it |
| F30 | `readrule._LINE_RX` | the declared session-line forms |
| F31 | `readrule._check_pieces` | only the last free group may be the reasoning block alone, where the line ended the session |
| F32 | `readrule.strip_contrast` (time) | ruling (h)'s form plus the per-line cap booleans (Q5); the list's length locates a free-phase end (flag F-6) |
| F33 | `readrule.strip_contrast` | a contrast session's free and reasoning hair triggers withheld from the read |
| F34 | `readrule.redact_sham` | both labels redacted in free responses and every reasoning line |
| F35 | `readrule.printed_reason` | a contrast line after the first pick prints `excluded@free`; line 1 `scaffold@reasoning`; at G-TIME-F3 every contrast line `excluded@free` (ruling (h): no class; a reasoning line is excluded only for the scaffold class, so its phase would name it; finding 3) |
| F36 | `readrule._contrast_block_time` | G-TIME-F3's contrast block: s, forced rounds generated, excluded at forced, the per-line cap booleans |
| F37 | `resume.weights_binding` | Q6's binding: the snapshot's revision and the sha256 of its load files' content addresses |
| F38 | `resume.Identity` (paths) | G-ID-F3 "cached+uncached"; G-TIME-F3 "uncached" |
| F39 | `resume.load_or_init` | m's order with Q-F3's identity; no pod id on the laptop |
| F40 | `runner.qwen_ban_list` | runner_qwen's procedure (not importable, N1) |
| F41 | `runner.run_session_f3` (licence) | a cached session outside G-ID-F3 re-reads the licence on this backend at this cap |
| F42 | `runner.run_session_f3` (seconds) | the whole session's wall-clock, to the ms |
| F43 | `schedule.L_MAX_K1` | the k = 1 materialization: A1 4352, A1s 1600, A2 = A3 6384, A2s = A3s 2640 (B21) |
| F44 | `schedule.GATE_PLAN` | G-TIME-F3 1 per arm; G-ID-F3 A2s and A3s, 16 rows each; G-F3 4/8/4/8/8/8 |
| F45 | `schedule.roster` | Q-F3's roster is Qwen's of record via `m.schedule.roster_for("Q-F0")` |
| F46 | `schedule.gate_launch_order` | strict rotation in §2.4's order, a template leaving at its count (B5) |
| F47 | `schedule.interleave` | m's rotation over six arms, the counts validated pairwise |
| F48 | `schedule._file_blobs` | m's manifest form, construction "PROPOSAL-m v1.11 m:159-172 (Q-F3)" |
| F49 | `bars._qf3_bars` | scaffold_absorption's unit is the generation (a round or a line) (B26); G-ID-F3's criterion declared `gid_divergence` |
| F50 | `bars` (G-TIME-F3 line bar) | a fire STOPs; the cap-trigger count is reported, applied by nobody until the seat re-specifies (B17) |
| F51 | `bars.counts` | m's stage_end_eval PIN carried; lines by the union of classes |
| F52 | `bars.no_test` | a gate-stage bar at realised n = 0 is reported as no test and not fired, and the stage ends on its other bars: Code's reading by analogy with m:271's Qwen rule, which says "reported, not fired" of G-TIME-F0's realised n of 2–4 and "on Qwen no such pause exists" of OLMo's G-TIME pause (m:271 says nothing of n = 0); revised on finding 6 from a PAUSE that nothing could lift; silent at a campaign look (B30) |
| F53 | `banner._label` | m's label rule |
| F54 | `verify` (read) | m's read check: menu_a iff p_a >= p_b, KL exactly 0.0 |
| F55 | `verify` (role) | A2/A2s and A3/A3s share a banner: the template name decides the role and the delivery is asserted (B22) |
| F56 | `gshape` (Layers R, T) | additions to "as G-SHAPE-F0": the reasoning line's own placements (Layer R) and the build hazard's declared check on the tokenizer of record (Layer T); §7 (Layer R's scope, finding 11) |
| F57 | `scripts/mf3_sessions.py` | what is wired (selftest, schedules, hashes, gshape) and refused (the four stages); Q6's forms (§8) |
| F58 | `guard._F3CallSiteScan`, `guard.check_call_sites` | `valence_core.m.guard`'s hardened scanner, imported and subclassed: the scanner is inherited, and six methods are overridden, each restating m's with Q-F3's names — the four that bind m's guard module or file (`__init__`, `_flag_licensed_bindings`, `_is_guard_alias`, `_licensed`: mf3's guard the one licensed binding, so Q-F0's licence is unlicensed here, m:267), `in_gid` (`run_gid_pair_f3`'s module-level body the one exemption) and `flag` (m's names in every inherited message); `run_session_f3` guarded; m's whole battery reproduces under `_battery_map` (finding 1) |
| F59 | `stages._gid_pair` (`meta_identical`) | beside m:281's criterion, descriptive only: whether a pair's generations agree in token count, cap flag and stop reason (finding 9; flag F-7) |
| F60 | `readrule._contrast_block` | a contrast template reports its sessions' first reasoning lines (pre-pick) beside its forced rounds, by class, with line-1 exclusions and hair triggers; later lines withheld with the free rounds (m:297, m:271; finding 12) |


- **Dated note, 2026-11-07: three of this register's readings are superseded by the seat's rulings, applied at
  `e0b4f2c`.**
  - The three were Code's readings at the F3 build, put to the seat as flags F-6 and F-7:
    - F32's and F36's per-line cap booleans in G-TIME-F3's contrast reports, built as the seat's Q5 ruled;
    - F59's `meta_identical`, kept as descriptive only.
  - The seat ruled both flags (the G-ANL-F3 answers, F-6 and F-7):
    - a contrast session at G-TIME-F3 reports no per-line list before VERDICTS, and its booleans go to the
      checkpoint. F-6 supersedes the per-line-list part of Q5;
    - G-ID-F3's identity criterion binds the per-line triple.
  - `e0b4f2c` applied them:
    - neither the stripped read (`strip_contrast`, `readrule.py:194`, the seat's F-6 PIN) nor the contrast block
      (`_contrast_block_time`, `readrule.py:471`; Code's PIN at :472, citing F-6) carries a per-line list;
    - `meta_identical` is gone, and the triple binds in `_gid_pair` (`stages.py:1140`, the seat's F-7 PIN).
  - The register is reproduced as written. F32's "plus the per-line cap booleans (Q5); the list's length locates a
    free-phase end (flag F-6)", F36's "the per-line cap booleans" and F59 are not Code's readings at this lock. The
    rest of the register stands.

#### G-ANL-F3's PIN register, verbatim (`results/raw/2026-11-06_ganl-f3_build_design.md` §2)

PIN-V2-1 to PIN-V2-24. Each is Code's reading, declared at LOCK-m-F3 v0.1, listed as a flag in the BUILD entry and strikable by the seat until LOCK-m-F3 v1.0 (answers:50). The cost of striking one: the analyzer's sha256 moves, G-ANL-F3 is rebuilt and re-run and its artifact superseded, and after LOCK-m-F3 v0.1 a hash that lock names moves too. Each entry's text is in `PINS_F3`, and each has at least one site, a `# PIN (Code, declared at LOCK-m-F3 v0.1 …): PIN-V2-n --` comment (PIN-V2-9 two):

| PIN | Subject |
|---|---|
| V2-1 | A3's NO-READ sub-reason; arm grain vs unit grain |
| V2-2 | the power figure of record per Q-F3 arm |
| V2-3 | the labels of cells A2 and A3 (Step 3) |
| V2-4 | the v2 sentence table |
| V2-5 | A3*, the withholding value, the v1-note; Q-F3 NOT-RUN's outputs |
| V2-6 | Step 6 rendered from m:342's own texts; "[stages]" and the power slot |
| V2-7 | §8.1 and §8.2 at v2; Step 7 |
| V2-8 | A-m1 §2.5 (1), the CLI paths |
| V2-9 | A-m1 §2.5 (2), the Clock dates |
| V2-10 | N8's era rule for PENDING |
| V2-11 | the regression's identity and the preprint of record |
| V2-12 | the Q-F3 reader's V1 (the Q-F3 closure; the posted v1 precondition; Q-F0's inputs refused) |
| V2-13 | counter (c)'s scorer (punctuation replaced by a space) |
| V2-14 | the blind-read draw (seed 20261106; staged adjudication reads) |
| V2-15 | the shared V2 helper; Q-F3's V4 |
| V2-16 | the Q-F3 arm sentence |
| V2-17 | valid-through at F3; Q-F3's secondaries |
| V2-18 | Q-F3's counters |
| V2-19 | Q-F3's NOT-RUN causes |
| V2-20 | `not-run` for Q-F3 and `--v2-closure` (`--campaign` required: the committed checkpoint, or `none` only while none exists; no campaign session) |
| V2-21 | `posting --posting v2` |
| V2-22 | the v2 enumeration's (b) treatment by A3* |
| V2-23 | the G-ANL-F3 artifact and PIN-39's widened commit check |
| V2-24 | the v2 table of record bound at Q-F3's VERDICTS (PIN-40 carried) |

The seat's rulings are recorded beside, as `SEAT_RULED_F3` (A1–A5). The two PIN-29 sites carry the seat's marker ("the seat's A1, 2026-11-06; acknowledged by the PI").


#### The PIN sites declared at LOCK-m-F3 v0.1 (90 sites: every line of `valence_core/mf3/*.py`, `scripts/mf3_sessions.py` and `scripts/m_analyze.py` that opens `PIN (Code, declared at LOCK-m-F3 v0.1` or `PIN (the seat's`, in a comment or a docstring)

| site | where | its opening |
|---|---|---|
| `scripts/m_analyze.py:112` | comment | PIN (the seat's A1, 2026-11-06; acknowledged by the PI): PIN-29's exception, by blob -- the battery's open hook |
| `scripts/m_analyze.py:131` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (2); the seat's A5 item 9 (2)): PIN-V2-9 -- three declared dates, |
| `scripts/m_analyze.py:529` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:324, m:347): PIN-V2-19 -- Q-F3 takes the causes both substrates |
| `scripts/m_analyze.py:562` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (2); the seat's A5 item 9 (2)): PIN-V2-9 -- the |
| `scripts/m_analyze.py:613` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (2); the seat's A5 item 9 (2); N8): PIN-V2-10 -- the |
| `scripts/m_analyze.py:1878` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; A-m1 §2.5 (1); the VERDICTS read §4 item 2): PIN-V2-8 -- |
| `scripts/m_analyze.py:2048` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:271, m:308; PIN-7, PIN-34 carried): PIN-V2-15 -- the V2 block is |
| `scripts/m_analyze.py:2559` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A2 and A3; m:324): PIN-V2-20 -- `not-run` also takes |
| `scripts/m_analyze.py:2955` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; Step 3, m:339): PIN-V2-3 -- Q-F3's cells A2 and A3 are labelled Answered |
| `scripts/m_analyze.py:2971` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A3): PIN-V2-4 -- the v2 table is schema |
| `scripts/m_analyze.py:3072` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:340, m:291; the STOP's §3 items 3-5, not struck): PIN-V2-5 -- A3* is a |
| `scripts/m_analyze.py:3171` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): PIN-V2-6 -- Step 6 renders m:342's own texts (S6_*) by filling their |
| `scripts/m_analyze.py:3252` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:343; PIN-17 carried): PIN-V2-7 -- at v2 §8.1's text is v1's four |
| `scripts/m_analyze.py:3284` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:349): PIN-V2-22 -- the v2 enumeration is PIN-21's over the v2 table |
| `scripts/m_analyze.py:3368` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): PIN-V2-1 -- A3's NO-READ carries PIN-4's sub-reason |
| `scripts/m_analyze.py:3405` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): PIN-V2-2 -- A1 at α .01, P = .70 (a control, as A0); A2 at α .01, |
| `scripts/m_analyze.py:3431` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:312 (c); the STOP's §3 item 7, not struck by the seat): PIN-V2-13 -- |
| `scripts/m_analyze.py:3447` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:312 (c), "seed pinned"; the STOP's §3 item 7): PIN-V2-14 -- the |
| `scripts/m_analyze.py:3671` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:326; the seat's A5 note on item 1): PIN-V2-16 -- PIN-4's clauses |
| `scripts/m_analyze.py:3744` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:308, m:312; PIN-13 carried): PIN-V2-17 -- "valid through position p" at |
| `scripts/m_analyze.py:3802` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:314): PIN-V2-18 -- Q-F3 tabulates the Qwen counters as Q-F0 does, |
| `scripts/m_analyze.py:4106` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A3; m:271, m:318, m:324, m:326, m:358): PIN-V2-12 -- Q-F3's |
| `scripts/m_analyze.py:4148` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; Q7, the PI's word of 2026-11-06; PIN-40 carried): PIN-V2-24 -- the |
| `scripts/m_analyze.py:4348` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A2 and A3; m:336-343, m:349): PIN-V2-21 -- the v2 |
| `scripts/m_analyze.py:5076` | comment | PIN (the seat's A1, 2026-11-06; acknowledged by the PI): PIN-29's exception is by blob, not by |
| `scripts/m_analyze.py:9867` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's A1; a dated note in the G-ANL-F3 entry): PIN-V2-11 -- |
| `scripts/m_analyze.py:11082` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the STOP's §3 item 11): PIN-V2-23 -- `ganl` writes |
| `valence_core/mf3/banner.py:46` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m.banner's label rule, applied here: a non-empty |
| `valence_core/mf3/bars.py:178` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:271 "unit session/round"): scaffold_absorption's unit is |
| `valence_core/mf3/bars.py:192` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B17): if G-TIME-F3's line bar fires the |
| `valence_core/mf3/bars.py:294` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's stage_end_eval PIN carried -- the domain is every |
| `valence_core/mf3/bars.py:324` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B30, revised on the build review's finding 6): |
| `valence_core/mf3/gshape.py:457` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 11): each gold is placed as a line |
| `valence_core/mf3/guard.py:46` | comment | PIN (the seat's F-7, 2026-11-06): m:281's 2/2 criterion, which m:295 carries ("as above"), and per reasoning line |
| `valence_core/mf3/guard.py:57` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q1 (C2) part (b); N1): the valence_core.m modules |
| `valence_core/mf3/guard.py:68` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 7): the licence's part (b) hashes the |
| `valence_core/mf3/guard.py:93` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174 "the cap enters the resume identity", m:295 "G-ID-F3, |
| `valence_core/mf3/guard.py:241` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build review's finding 1): the check IS |
| `valence_core/mf3/lines.py:37` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "which harness lines count is the declared |
| `valence_core/mf3/lines.py:88` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): "empty line" = the text is empty after whitespace |
| `valence_core/mf3/lines.py:93` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "the cap-length prefix is the line as |
| `valence_core/mf3/lines.py:98` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: containment, "since equality misses prefixed |
| `valence_core/mf3/lines.py:131` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q4): the unit is the generation (a task round |
| `valence_core/mf3/readrule.py:52` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's _LINE_RX PIN carried to F3): the declared session-line |
| `valence_core/mf3/readrule.py:125` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): a free group is FREE_GROUP; only the last may be the |
| `valence_core/mf3/readrule.py:194` | comment | PIN (the seat's F-6, 2026-11-06; superseding the per-line-list part of Q5): a contrast session's |
| `valence_core/mf3/readrule.py:210` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's PIN carried -- a free-phase hair trigger is withheld here |
| `valence_core/mf3/readrule.py:243` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's PIN for free responses carried to the |
| `valence_core/mf3/readrule.py:319` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:263, m:271, ruling (h); the build review's finding 3): a |
| `valence_core/mf3/readrule.py:437` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:297 "contrast sessions reported beside", m:271; the build review's |
| `valence_core/mf3/readrule.py:472` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's ruling (h) carried, and its F-6 of 2026-11-06): at |
| `valence_core/mf3/resume.py:106` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q6, "The weights-snapshot binding in the identity |
| `valence_core/mf3/resume.py:180` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's path rules for Q-F3 -- G-ID-F3 "cached+uncached"; |
| `valence_core/mf3/resume.py:224` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's load_or_init, step for step, its identity validation |
| `valence_core/mf3/runner.py:59` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the procedure of valence_core.m.runner_qwen.qwen_ban_list |
| `valence_core/mf3/runner.py:121` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's defence in depth, carried -- a cached session outside |
| `valence_core/mf3/runner.py:203` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): seconds = perf_counter wall-clock of the whole session |
| `valence_core/mf3/scaffold.py:122` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the path is "cached" or "uncached" per session; |
| `valence_core/mf3/scaffold.py:127` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174): G-TIME-F3 generates its reasoning lines at |
| `valence_core/mf3/scaffold.py:144` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): j = s at gate stages (session j of the sixteen-row |
| `valence_core/mf3/scaffold.py:157` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8 on the "\n\n" after the reasoning segment, |
| `valence_core/mf3/scaffold.py:192` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8: "the fire is an exclusion event and ends |
| `valence_core/mf3/scaffold.py:216` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): complete = 2F forced rounds and N_FREE x (reasoning |
| `valence_core/mf3/scaffold.py:239` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q8): the guard's and the counters' pre-pick |
| `valence_core/mf3/schedule.py:47` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's materialization PIN carried to Q-F3 -- each campaign |
| `valence_core/mf3/schedule.py:91` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the gate-stage plan -- G-TIME-F3 one session per arm |
| `valence_core/mf3/schedule.py:105` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F3 is a Qwen unit, so its roster is Q-F0's -- read |
| `valence_core/mf3/schedule.py:188` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's launch-order PIN carried to six templates -- |
| `valence_core/mf3/schedule.py:210` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): Q-F0's interleave PIN carried to six arms -- next = the |
| `valence_core/mf3/schedule.py:295` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's manifest form, its construction line naming Q-F3; |
| `valence_core/mf3/stages.py:59` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): the analyzer the gate line logs and the licence hashes is |
| `valence_core/mf3/stages.py:99` | docstring | PIN (Code, declared at LOCK-m-F3 v0.1): m's layout under data/mf3 -- schedules/ (read only), |
| `valence_core/mf3/stages.py:291` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the seat's Q1 (C2): "Every non-stub mf3 stage checks both at |
| `valence_core/mf3/stages.py:394` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PRIOR_STAGE carried, m:293-298): G-ID-F3 needs G-TIME-F3 |
| `valence_core/mf3/stages.py:428` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:295; the build design's B7): the artifact's cap must |
| `valence_core/mf3/stages.py:466` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:294-296; the build review's finding 4): the cap is fixed by |
| `valence_core/mf3/stages.py:559` | docstring | PIN (Code, declared at LOCK-m-F3 v0.1; m's _extra carried): identity_extra carries {lock_sha256, |
| `valence_core/mf3/stages.py:715` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's _hair_hit carried): the fired generation is the session's |
| `valence_core/mf3/stages.py:857` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): a reasoning line's excerpt is its block, its text and its |
| `valence_core/mf3/stages.py:986` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:174, m:293, the seat's Q5): the count is the lines whose |
| `valence_core/mf3/stages.py:991` | comment | PIN (the seat's F-6, 2026-11-06): what is reported is the count k against the declared maximum ("k of |
| `valence_core/mf3/stages.py:1110` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m:295 "A2s and A3s once each; criterion 2/2 as above"; the seat's |
| `valence_core/mf3/stages.py:1140` | comment | PIN (the seat's F-7, 2026-11-06; a seat PIN at LOCK-m-F3 v0.1, set before G-ID-F3 has run): a pair is |
| `valence_core/mf3/stages.py:1184` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried; B7): a G-ID-F3 artifact is never overwritten |
| `valence_core/mf3/stages.py:1280` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried): G-ID-F3's sessions are sham-only and read in full |
| `valence_core/mf3/stages.py:1348` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B23): the lexical bar's numerator is the |
| `valence_core/mf3/stages.py:1412` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried, and B7): the G-ID-F3 artifact on disk is |
| `valence_core/mf3/stages.py:1627` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; m's PIN carried): the campaign report is pick-free -- looks with |
| `valence_core/mf3/verify.py:148` | comment | PIN (Code, declared at LOCK-m-F3 v0.1): m's read check, carried: the pick follows choice_read's |
| `valence_core/mf3/verify.py:173` | comment | PIN (Code, declared at LOCK-m-F3 v0.1; the build design's B22): the contrast/sham role is the |


## 10. Dated notes, 2026-11-07

- **N13's entry term (the seat's ruling).** Any v2-closure entry declaring `--campaign none` names every set-aside
  that exists for the unit and its session count, so the declaration is auditable.
- **N1 at this lock:** N1 is committed at `9480f9b` (the coordinating session's commit). `PREPRINT-v1_0-draft.md`
  holds its bytes of record (`45b67246…7a41`), and its status banner is in the sidecar
  `PREPRINT-v1_0-draft.STATUS.md`. G-ANL-F3.json was written on that HEAD, so its `g_anl_f3.regression.preprint`
  records the restored tree, with `head_file_is_table` true. The battery check `F3R-PREPRINT-OF-RECORD` asserts only
  that the committed blob of record serves the regression, whatever the tree holds (`10a2bbb`; the seat's answer §1).
- **m's package moved before this lock.** The hygiene commit (`993eba1`; the seat's N12) moved m's `package_sha256`
  from `60199b36…feec` to the value in §1. This lock names the moved value. mf3's licence's eleven files are
  unchanged by it (gcal is in mf3's `ABSENT_MODULES`).

## 11. What follows

1. **G-TIME-F3's wiring:** the `time` subcommand is wired in `scripts/mf3_sessions.py` at its step, after this
   lock's commit.
   - Code intends it as an edit under F-1's clearance: a subcommand wiring that touches no scoring-stack function, so
     no G-SHAPE-F3 re-run. The wiring's entry states that reading on the edit as made.
   - The coordinating session's routing of 2026-11-07, relayed in chat and recorded in the wiring's entry, has the
     wiring also carry:
     - the rest of m's pre-load check, in `scripts/m_sessions.py`'s forms: the MLXLM_USE_MODELSCOPE and local-path
       refusals, the hub's own offline resolution, the SNAPSHOT line, and the post-load re-read with its model-id
       STOP;
     - a DRIVER line (the committed driver's blob sha256), which LOCK-m-F3 v0.2 records.
   - The seat's F-2 places the pre-load check with the campaign subcommand's wiring. The wiring's entry quotes F-2
     and gives Code's reading in a dated note.
2. **G-TIME-F3** (m:293): its six sessions on the laptop, under m:267's checklist and the Qwen launch checklist; the
   seat's read under m:263's printed form and m's §3 rule.
3. **The cap**, fixed by G-TIME-F3's trigger (m:294).
4. **G-ID-F3** under F-7 (m:295).
5. **LOCK-m-F3 v0.2**: the cap, the path and the projections (m:296).
6. **G-F3** (m:297); **G-VER**, **G-PWR** and **LOCK-m-F3 v1.0** with D2 (m:298; ADDENDUM-m1 §2.3).
