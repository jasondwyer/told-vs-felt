# G-ANL-F3: Code's referent check of the seat's answers (PI routing, PI date 2026-11-06)

*Code's raw. It checks `results/raw/2026-11-06_ganl-f3_design-to-code_answers.md` (sha256 `4edfbb8e3d08844e47a329a951f9c2dd381115f0fd92c8b2b77f2207777ca42e`, as routed) against its referents at HEAD `273ca8f`, reading only. It covers sections A to D: C's included, as the coordinating session's relay asks ("every anchor at source, C's included"), and D against the routing block as relayed. `m:N` = PROPOSAL-m v1.11 at root (sha256 `42ab36ec…6c6b`); `A-m1:N` = ADDENDUM-m1 v0.1 at root (`f26bc59`); `answers:N` = the F3 prebuild answers (`results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md`); `STOP` = Code's G-ANL-F3 pre-build block (`results/raw/2026-11-06_ganl-f3_code-to-design_prebuild.md`, `958e762`). Result: no unresolved item, and five minor residues, carried as dated notes (§2) under the routing's process line. A blind values-check of this raw and of the close line (81 items) ran before the commit; its raw, with Code's dispositions, is committed beside this one (`results/raw/2026-11-06_ganl-f3_answers_valuescheck.md`).*

## 1. Checked, as cited

- **Header.**
  - The STOP is committed at `958e762`.
  - The F3 build design's flags F-1 to F-7 are at `results/raw/2026-11-06_mf3-build_design.md:155–161`.
  - The build review's finding 3 is in `results/raw/2026-11-06_mf3-build_review.md` §1.
  - The BACKEND entry's flag is in RESULTS.md's BACKEND entry (committed at `190ba90`): "FLAG, not adjudicated: `RUNPOD_POD_ID` is unset in a non-interactive ssh shell on this pod."
- **A1 (Q1, R1).**
  - A-m1:44 has "(rule 26's form)".
  - `git cat-file blob ed8e886:scripts/m_analyze.py` hashes to `655e0f7f6743d0bf…c16f`.
  - LOCK-m-F0.md:147–149 names the analyzer `655e0f7f…`, the package `5f646db6…` and the closure `a3bc7bb9…`.
  - `Q-F0_VERDICTS.json`'s `inputs.lock` is `LOCK-m-F0.md`, sha256 `fc7e9db8…`, equal to the file at HEAD.
  - PIN-14's check is at `scripts/m_analyze.py:1934–1944`.
  - The seven files are those the STOP names: `data/m/ckpt/Q-F0_{campaign,time,qual}.json`, `data/m/verdicts/Q-F0_{decisions,olmo-states}.json` and the two outputs. All seven are committed.
  - m:318 is the blinding paragraph that covers a unit's picks until its VERDICTS.
  - answers:26's "asserts the OLMo v1 outputs unchanged".
  - The 1,080 tuples under both flag values are G-ANL-F0's (m:278; `scripts/m_analyze.py:9–10`).
- **A2 (Q2, P1).**
  - m:324: "A checkpoint still PENDING at the v2 posting is closed there: PI-stopped and analyzed as obtained if it has sessions, else NOT-RUN with the reason recorded".
  - `pending-closed-at-v2` is a v2-only OLMo cause at `scripts/m_analyze.py:413–415`, refused at v1 by PIN-38 (`:2467–2468`, `:2925–2927`).
  - The counts: 481 × 5 × 91 = 218,855 and 481 × 5 × 125 = 300,625, which sum to m:291's 519,480.
- **A3 (Q3).**
  - Q7 is at answers:46. The PI's word confirming it is in the routing of 2026-11-06 (the F3 build's STOP close in RESULTS.md: "v2's sentence table is built at the Q-F3 VERDICTS session against the posted v1: [confirmed]").
  - answers:26's rule.
- **A4 (riding texts).**
  - (i) A-m1:44's items (1)–(3).
  - (ii) `results/raw/2026-10-19_m-design-to-code_VERDICTS_read.md:83`. `_prod_committed` is at `scripts/m_analyze.py:1768–1773`, and its test `rel == str(p)` makes a relative path read "outside the repository". `flag_of_record`'s silent FALSE is at `:1657–1660`.
  - (iii) `results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1_round2.md:19`: "a misparaphrase found later is a text correction at the next hash-moving round".
- **A5.**
  - m:64 (§0.10): "Power figure of record (§2.4, §5): the NULL sentence quotes attained power at the realised n, f2's where f2 ran".
  - m:190: ".927 at P = .65" at the planned floors; "Attained power at the realised n is reported in VERDICTS, descriptively, and is the power figure of record for the verdict sentences".
  - N8 is at `results/raw/2026-11-06_m1-v0_1_referent-check.md:213–217`.
- **B.**
  - **F-1.** The step-10 read's Q2 is `results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md:45`: "an edit to `scripts/m_sessions.py` that wires a subcommand, with no change under `valence_core/m`, moves neither `package_sha256` nor the analyzer and does not re-run G-SHAPE-F0, because the gate tests the scoring stack's scope".
  - **F-3.** m:277 does not name a tokenizer. m's gshape module docstring has "No model, no tokenizer, no generation". G-SHAPE-F3's Layer R `scope` text is in its artifact (`1bf94a6`).
  - **F-4.** Q1 (C2) is at answers:14.
  - **F-5.**
    - `scripts/m_gpwr.py` exists.
    - m:184–186 give the arms (A1 / A1s "96 cached, 80 uncached / 32"; A2 / A2s 144 / 56; A3 / A3s 144 / 56).
    - m:190 gives "Power floors: A2 ≥ .85 at P = .65; every control ≥ .85 at P = .70", the grid rule, and attained power at the realised n reported in VERDICTS.
  - **F-6.**
    - Q5 begins at answers:33.
    - m:174 has "(≤ 36)".
    - m:271 withholds a contrast session's free-round events.
  - **F-7.** m:281's criterion: "2/2 byte-identical cached/uncached transcript pairs"; "a divergence sends Q-F0 uncached (and its floors to the uncached column)". m:295 carries it to G-ID-F3 ("criterion 2/2 as above").
  - **Finding 3.** Ruling (h), `excluded@free` for every G-TIME-F3 contrast line, and `excluded@reasoning` gone from `_PRINTED_RX` / `_LINE_RX` are as the build's values-check recorded them (C9 #3, `results/raw/2026-11-06_mf3-build_valuescheck.md:228`; A27, :87). "Every contrast line after the first pick printing `excluded@free`" is F35's register row (`results/raw/2026-11-06_mf3-build_design.md:92`) and the code's PIN (`valence_core/mf3/readrule.py:323–329`); the values-check names neither (N5). m's `announce_stop` names a non-free-phase trigger's bar (`valence_core/m/stages.py:1218–1238`).
- **C.**
  - **C1.**
    - The pod `qny1x4v8padeke` and BACKEND PASS are in the BACKEND entry (`190ba90`).
    - No `LOCK-m-OLMo-*.md` exists at HEAD `273ca8f` or in the tree.
    - A-m1 §3 item 4's fallback is at A-m1:51 ("or deferred to v2, in which case the v1 posting runs the analyzer of record and item (2)'s reading is stated by hand in the `POSTING v1` entry").
  - **C2.**
    - m:302 has the OLMo units per checkpoint.
    - G-TIME-OLMo is "two sessions, one per arm", so ×3 = 6. G-F0m-OLMo is "24 sessions", so ×3 = 72.
    - m:251 runs each checkpoint's campaign "within one pod session on one characterized backend".
  - **C3.**
    - $1.79/hr is in the BACKEND entry ("price.secure **$1.79/hr**").
    - 224 G free is the BACKEND entry's "466 G, 242 G used".
    - ≈ 64 G bf16 and "volume headroom checked against `data/olmo/manifest.json`'s sizes before the pull [C]" are PROPOSAL-n v0.2 §2.7 (`PROPOSAL-n-bk-reconciliation-v0_2.md:101`). The answers' ≈ 128 G fp32 is twice the bf16 figure.
  - **C4.**
    - `valence_core/m/resume.py:253–259`: `pod_id()` reads `RUNPOD_POD_ID` ("empty or whitespace = absent").
    - m:267's resume identity carries "for an OLMo campaign, the pod instance id".
    - The BACKEND entry records that the backend identifier drops `path`.
- **D.** The routing block, as relayed, takes D's five items in order (the go for G-CAL-OLMo, the order, the batching, G-ACQ, the PIN-29 acknowledgement), with a Pod line between the batching and G-ACQ. Its G-ACQ line keeps both options ("[now, in parallel / after the campaigns]"); the PI chose "Now, in parallel" in chat.

## 2. Dated notes (minor residues), 2026-11-06

- **N1. F-5's A1 sizes.** F-5 writes "A1 96/32", but m:184 has A1 / A1s at "96 cached, 80 uncached / 32" (m:190: "(96, 32): .916 at P = .70; (80, 32): .878"). Code reads F-5 as m:184's two columns. `scripts/mf3_gpwr.py`, built at F-5's step (after G-F3), will re-derive the column of the path LOCK-m-F3 v0.2 fixes (m:296), as `scripts/m_gpwr.py` did for Q-F0 on its uncached path (A0 80, A0s 32; `scripts/m_gpwr.py:16`; LOCK-m-F0.md:431). The ruling is otherwise unaffected.
- **N2. A1's "PIN-14's posting path".** The binding of the v1 `posting` command is PIN-42's (`analyzer_binding`, `scripts/m_analyze.py:2370–2387`). It records the analyzer, package and closure shas, and refuses only on the proposal pin and an uncommitted analyzer, never on the three shas. PIN-14 is `verdicts`' lock binding. The ruling's content holds: the v1 `posting` command records the three shas and does not refuse on them. G-ANL-F3's report cites PIN-42.
- **N3. B's mf3 edits and G-SHAPE-F3.**
  - F-6 (G-TIME-F3's contrast reporting and its CAP TRIGGER line) and F-7 (G-ID-F3's criterion) are edits to `valence_core/mf3`. They touch `readrule.py`, `stages.py` and `guard.py`, files G-SHAPE-F3's sources map records, and they move mf3's `package_sha256`. The answers give no timing for them; Code applies them in the G-ANL-F3 build, on the coordinating session's relay of 2026-11-06 ("Apply B as written"), as Code's plan.
  - On the step-10 read's own terms (`G-TIME-F0_read.md:45`: its clearance covers a subcommand-wiring driver edit "with no change under `valence_core/m`", and "an edit there moves the package and is outside this answer") and G-SHAPE-F0's PIN-S10 ("any difference re-runs G-SHAPE-F0 first", `valence_core/m/gshape.py:233–236`, not restated in mf3's `gshape.py`), G-SHAPE-F3 re-runs on the new package before LOCK-m-F3 v0.1 names its result (m:292).
  - Its committed artifact (`1bf94a6`) is then superseded by hand, as G-SHAPE-F0's PIN-S9 has it (mf3's `gshape.py:654–655`: "never overwritten"; "supersession is a hand git mv on the seat's ruling"), on the seat's ruling, which the routing of LOCK-m-F3 v0.1 can carry.
  - The re-run and the supersession are not G-ANL-F3's, and they block nothing in G-ANL-F3. LOCK-m-F3 v0.1 names G-ANL-F3's analyzer and lexicon hashes (m:292), so it follows G-ANL-F3's commit in any case, and it waits for the coordinating session's word (its relay of 2026-11-06: "LOCK-m-F3 v0.1, and anything that runs Qwen on the laptop, wait for my word").
- **N4. C2's count.** m:271 (and m:72) also has the seat read each G-CAL-OLMo's generations "at the stage (they carry no pick)". C2's chain names two reads, after G-TIME-OLMo ×3 and after G-F0m-OLMo ×3; batched, the G-CAL-OLMo read is a third (nine unbatched, not six), and a G-TIME-OLMo pause adds the seat's adjudication (m:302: "a pause → the seat's adjudication, before that checkpoint's qualification"). The batching ruling is otherwise unaffected. (Found by the blind values-check, item 69.)
- **N5. Finding 3's sources.** The answers' finding-3 line (answers file :31) credits to the build's values-check both `excluded@reasoning`'s removal and "every contrast line after the first pick printing `excluded@free`", citing "(F35; ruling (h))". The values-check records ruling (h), `excluded@free` at G-TIME-F3 and `excluded@reasoning`'s removal (C9 #3 at `results/raw/2026-11-06_mf3-build_valuescheck.md:228`; A27 at :87); it names neither F35 nor "after the first pick", which are F35's register row (`results/raw/2026-11-06_mf3-build_design.md:92`) and the code's PIN (`valence_core/mf3/readrule.py:323–329`). The rule confirmed is unaffected. (Found by the blind values-check, item 46.)
