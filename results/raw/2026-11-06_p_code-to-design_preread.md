# PROPOSAL-p v0.1 (p §8 step 2): Code's pre-read — STOP with every question, the renders reproduced, the referent check (2026-11-06)

*Code to the design seat, through the PI. The routing is the PI's block of 2026-11-06, relayed by the coordinating session (in its message, not a file), verbatim: "1. Date: [2026-11-06]. The three m NOT-RUN records: [go]. 2. PROPOSAL-p v0.1: [route for Code's pre-read]. If routed: letter [p]; §1's frame-word rule [confirmed as written]; D_p [2026-12-15]; pod budget [12 h for G-CAL-p, gate stages and three campaigns]; order on the pod [G-CAL-p first, then whichever lock chain is ready]; §5's v2 posting rule and its two declared sentences [adopted]. 3. The pod: [stays up]." The same block is quoted in `0f35954`'s entry (RESULTS.md@0f35954:31–33). Anchors: `p:N` = line N of `PROPOSAL-p-olmo-told-controls-frame-dose-v0_1.md`, untracked at root, sha256 `1821a235…9953` (p §8 step 3 commits it after this cycle); `ans:N` = line N of the seat's answers on the gate, `results/raw/2026-11-06_gcal-olmo_design-to-code_answers.md`, sha256 `4c3f57d4…bf82`, committed at `0f35954`; `m:N` = PROPOSAL-m v1.11 at root (`42ab36ec…6c6b`); `A-m1` = ADDENDUM-m1 v0.1; `n:N` = PROPOSAL-n v0.2 at root. Code is cited at HEAD `0f35954` (code unchanged since `e0b4f2c`) by function or constant name, with line numbers at that commit.*

## 0. Where it stands

- **G-ANL-F3 — BUILD is committed (`e0b4f2c`), before p commits.** So p §4.4's route (a) (p:88), the seat's "declared riding item of G-ANL-F3's round" (ans:25), is gone (Q1).
- No `LOCK-m-F3-*`, `LOCK-m-OLMo-*`, `LOCK-p-*` or `LOCK-n-*` file exists at HEAD or in the tree.
- m's three OLMo NOT-RUN outputs (p §8 step 1) are committed at `0f35954`, written by `m_analyze.py not-run` at `e0b4f2c`.
- This STOP edits no code, and p's file stays untracked.
- Its companion raws:
  - the renders file (§1);
  - the referent check (§4);
  - the blind values-check of this block.

## 1. The renders, reproduced — identical to p §1.2

- **Method.** `corr.corrupt_m` itself ran on each CORR_clean item, with `corr._eligible_m` replaced for the duration of each call by p §1.1's restriction. The restriction is m's eligible positions that lie inside a frame word: the item's first word, or a word of FUNCTION_WORDS, a word being a maximal run of ASCII letters, none inside a single-quoted span. The walk, the per-slot draw, the replacement formula (`corr.py:236`), the roster skip on `corr.ROSTERS_OF_RECORD` and `_k_m` are m's code, byte for byte.
- **Environment.** The laptop venv (numpy 2.5.1; the seat's was 2.2.6). `keys.stream("f|CORR|0").permutation(16)` equals `keys.F_CORR_0_PERMUTATION`, so the stream is the stream of record. The pool is `corr.load_pool()`, sha-pinned `8547d9a11ba55b95`.
- **Result.** All sixteen renders are byte-identical to p §1.2's table, in item order, and so are their frame words and n_eligible (m → p). k = 3 on every item, and k sums to 48 (m's: 54). Zero roster skips. No roster word appears in any render as a case-insensitive substring. k ≤ ⌊n/2⌋ holds everywhere. Items 0 and 12 equal m's renders.
- **The list's sha256**, by p §1.2's definition (`json.dumps(renders)` at its defaults), is `1551c19997dc4541` (full: `1551c19997dc45419c496d7f64a61711735672f9388bab4be2e2c1a450f85722`), p §1.2's [S] figure. m's own convention is the newline-joined renders, whose full sha256 the G-CAL artifacts record as `renders_sha256` (`corr.renders_sha` is its first 16 hex). By it, p's renders give `6baf494960da4589` (full `6baf494960da45896206f7eaadbc6b158642a42e09e1d11f70812959e3673c4c`), and m's give `a04f67b0e5105a05` (the artifacts' `a04f67b0…4372`). See Q3 (c).
- **The other [S] figures reproduced:**
  - m's k vector at rate 0.15: [3,3,3,3,4,3,3,7,3,3,4,3,3,3,3,3] (sum 54). At rate 0.10: [3,3,3,3,3,3,3,5,3,3,3,3,3,3,3,3] (p §0.3).
  - m's n_eligible on the four failing items: 19, 10, 14, 14 (items 2, 9, 11, 15).
  - §3.2's binding bars from the clean figures 62, 61, 59: max(⌈.70 × 64⌉ = 45, ⌈¾ × clean⌉) = 47, 46, 45 (exact arithmetic: 3 × clean / 4 = 46.5, 45.75, 44.25).
- **The file the seat reads** (p §1.3): `results/raw/2026-11-06_p_preread_renders.txt`. It holds the per-item table, the sixteen strings as one `json.dumps` line, both sha prefixes, and the probe script verbatim.

## 2. The questions

### Q0 (cross-cutting). "m's modules imported unchanged by import, never by copy" (p §4.2, p:84), where m's code fixes m's constants. What form may p's reuse take?

**What the record has.** Three of p's reuse sites need m's code to run with named attributes of an m module changed:
- **The corruptor (p §1.4, p:56).** `corrupt_m` reads the module-level `_eligible_m`. The replacement arithmetic that p §1.4 would import is not a function: it is inline in `corrupt_m` (`corr.py:236`). p's corruptor can therefore reuse m's walk in only two ways: run `corrupt_m` with `_eligible_m` replaced for the call (as §1 did), or re-literal the walk and the formula, which is a copy.
- **The schedules (Q4).** `valence_core.m.schedule`'s builders draw their streams through `valence_core.m.keys`. There, every OLMo key family is a literal `m-…` string: `sched_key`, `gate_sched_key`, `arm_key` and `item_key`, at `keys.py:96–154`.
- **The analyzer (Q1).** `scripts/m_analyze.py` checks `PROPOSAL_SHA256` (m's v1.11) at V1 of `run_verdicts`, `run_not_run` and the Q-F3 reader, and writes it into every output. `clock_of_record` gives D_O′ for every OLMo unit. The v2 posting reads all four v1 coordinates from one `--verdicts-dir`.

**Code's proposal.** One declared form. A context manager in p's package replaces named attributes of an m module for the duration of one call and restores them in a `finally`.
- Each replacement is named, with its replacement, in the BUILD entry and in LOCK-p v0.1, beside the imported files' sha256s.
- p's self-test asserts each one where p must equal m:
  - `corrupt_p` reproduces m's renders on items 0 and 12;
  - with m's keys in place, p's schedule builder reproduces the OLMo files of `data/m/schedules/` byte for byte;
  - with m's constants in place, p's analyzer reproduces m's committed outputs.
- The alternatives are a copy, which p §4.2 forbids, or an edit of m's modules. `corr.py` is one of the eleven files mf3's licence names (p:56), and m's package sha256 is bound (Q3).

**The question:** does the seat accept this form as "imported unchanged"? If not, at which sites may p copy?

### Q1. The analyzer path (p §4.4, p:88; with p §5.2, p:96)

**What the record has:**
- **Route (a) is gone.** G-ANL-F3 committed (`e0b4f2c`) before p commits.
- **The one-round rule.** The seat's G-ANL-F3 answers (A3, `54bbfe5`) read: "no in-place analyzer commit while an OLMo unit is open". p §4.4 adds: "in no other round while Q-F3 is open (from LOCK-m-F3 v0.1 to its VERDICTS)". Today neither bars an in-place round: no OLMo unit is open (m's three are NOT-RUN, none was locked), and Q-F3 is not open (LOCK-m-F3 v0.1 does not exist).
- **What `m_analyze.py` fixes to m's units:**
  - the proposal pin (`PROPOSAL_SHA256`, checked at V1 and recorded in every output's `proposal_sha256`);
  - the unit vocabulary (`UNITS`) and, through `keys.templates`, the template names that `record_problems` asserts;
  - the Clock (`clock_of_record`: D_O′ = 2026-11-30 for each OLMo unit; p's is D_p = 2026-12-15);
  - the v2 posting's OLMo coordinates. `run_posting_v2` cross-checks Q-F0 and the three OLMo coordinates against `{U}_VERDICTS.json` / `{U}_NOT-RUN.json` in one `--verdicts-dir` (`crosscheck_coordinate(u, x, …, verdicts_dir, v2=True)` for `u` in `UNITS`). m's three NOT-RUN outputs sit in `data/m/verdicts` (`0f35954`). So the committed analyzer cannot post p's states in the OLMo positions from the declared roots: PIN-23's cross-check meets m's NOT-RUN outputs there and refuses. It reads only each output's presence, state and reason (`crosscheck_coordinate`). So only a directory assembled to hold Q-F0's outputs beside p's would pass, and no rule declares one.
  - The data roots are not fixed, with one exception. `verdicts` takes `--campaign`, `--time`, `--qual` and `--out`; `not-run` takes `--time`, `--qual` and `--out`, and `--campaign` only with `--v2-closure`. The exception is the v2 closure's `--campaign none` check, which reads `data/m/ckpt/{U}_campaign.json`: `run_not_run`'s `ckpt_dir` defaults to it and is not a CLI option.

**What remains:**
- **(b) as p writes it.** `scripts/p_analyze.py` imports `m_analyze` unchanged and binds p's roots and document sha, and LOCK-p v1.0 names both blobs. p's unit outputs (VERDICTS, secondary DVs, NOT-RUN) go through m's functions with p's roots as parameters. Under Q0's form, p_analyze replaces the Clock (D_p) and the proposal pin. For the pin, the alternative is to keep m's proposal as the analyzer's proposal (p's units being m's by reference, p:82) and record p's sha256 beside it in every p output. **The v2 posting:** under (b), "the v2 posting's analyzer path … takes p's states as the OLMo coordinates under 4.4's mechanism" (p:96) means the v2 posting of record runs through `p_analyze.py`. That is m's `run_posting_v2`, with the three OLMo coordinates' cross-check reading p's outputs in `data/p/verdicts` and Q-F0's in `data/m/verdicts`. LOCK-m-F3 names m_analyze's blob; this p_analyze blob is one it does not name.
- **(a′) An in-place round of its own (G-ANL-p) before LOCK-m-F3 v0.1 and before any LOCK-p v0.1.** Both rules permit it today. It would teach m_analyze p's units, roots, D_p, §2.3's counters and the v2 OLMo coordinates' source, so that one analyzer posts everything. Its cost: a further analyzer blob (after `655e0f7f…` and `6ec3222b…`); a full G-ANL round (battery, regression, review); and Q-F3's lock chain waits until it lands, since LOCK-m-F3 v0.1 names the blob. It also cannot be built before p's design settles (Q0, Q2, Q4).
- **(c) (b) for p's unit outputs now, and a v2-posting round of m_analyze after Q-F3's VERDICTS and p's.** This is the window both rules leave open. Its cost: a later hash-moving round, and the v2 posting on a blob that neither LOCK-m-F3 nor LOCK-p names.

**Code recommends (b),** both for p's unit outputs and for the v2 posting through p_analyze (Q0's form), because:
- it is the route p and the seat name;
- it leaves `scripts/m_analyze.py`, and therefore LOCK-m-F3 v0.1, independent of p;
- G-ANL-p's battery can then assert that p_analyze with m's constants reproduces m's committed posting computations.

**The questions:**
- (i) Which route?
- (ii) Under (b), does the v2 posting of record run through p_analyze as described?
- (iii) The proposal pin: replace it, or keep m's and record p's sha256 beside it?
- (iv) §5.2's "m's three NOT-RUN rows beside them in the table of record and in §8.1's status sentence". Code reads it as text beside the v2 enumeration, not inside it. The v2 tuple keeps one coordinate per OLMo position (p's), so m:291's 519,480-tuple space and G-ANL-F3's v2 battery are unchanged, and m's rows and the PI's declared sentence are carried as at v1 (p:94: "neither enters §7.5's enumeration"). Is that right?

### Q2. The stored-text rule's site (p §2.2, p:64)

**What the record has:**
- **Nothing that binds `valence_core/adapters/olmo_hf.py` today:**
  - no lock or licence names it: not LOCK-m-F0, not mf3's licence (`guard.M_HASHED`), not G-SHAPE-F0's sources map (`gshape.py`);
  - it is in neither analyzer closure. The base closure's fifteen modules and the Q-F3 closure's twenty-two include `valence_core/adapters/__init__.py` and `base.py`, not `olmo_hf.py`.
- **The backend identifier.** `resume.backend_identifier` hashes the adapter's `provenance()`, and that record holds library versions, device facts and declared settings, not the source. So an edit would not move `641ee466f4553b6a`.
- **PROPOSAL-n.** n's build imports the adapter "unchanged" (n:159, §8 step 6) and builds its 5(f) primitive in n's own package; n's build has not started.
- **Seeding.** Every generation is seeded on its own (`generate`: `t.manual_seed(seed)` when a seed is given). m's runner passes each round's seed (`runner_olmo.py:137` and `:164`). So the tokens up to the line break are the same tokens whether the adapter stops there or a wrapper truncates afterwards, as p §2.2 says.
- **m's runner.** `run_session_olmo` stores what the adapter returns. `SessionLog.add_round` (`scaffold.py:385–392`) records `text` = `g.text`, `n_tok` = `len(g.token_ids)`, `cap_hit` and `stop_reason`, and `g.text` goes into the transcript the next round sees. The runner checks only the adapter's `path` and `choice_window` (`assert_olmo_adapter`, `runner_olmo.py:63–78`).

**Code recommends p's runner, via an adapter proxy in `valence_core/p/`, with `olmo_hf.py` unedited.** The proxy delegates every attribute to the loaded `OLMoHFAdapter`. Its `generate` applies §2.2 to the result before returning it: text cut at the first line break after non-whitespace; token ids cut at the token that carried it; `stop_reason` `newline`; `cap_hit` false. m's runner, unchanged, then stores only the cut text. Why the proxy:
- No bound file changes, and p's timeline is not coupled to n's build (p's condition, "PROPOSAL-n's build … takes the edited file before LOCK-n v0.1", never arises).
- Every past OLMo result stays reproducible on the adapter of record: the b-series box scripts, G-CAL-OLMo, the BACKEND characterization.
- G-CAL-p's clean-pool identity check (p:72) runs on the very generation path that produced G-CAL-OLMo's 64 clean generations.

Its cost: the tokens generated past the break, at most `STOP_CAP` = 60 (`session_e2a.py:90`) per affected generation (2 of G-CAL-OLMo's 384). LOCK-p v0.1 names `olmo_hf.py`'s sha256 as p §4.2 has it, and p's package (with the proxy).

**The question:** the proxy site, or the adapter?

**Two readings of §2.2's text for the seat to confirm (the proxy implements both):**
- **(a)** "A stop on a bare newline token with no content yet (the existing rule's purpose) is unchanged." The existing `_is_stop` (`olmo_hf.py:290–294`) does not stop on a newline before content: `content_seen` must be true. A leading newline is appended and removed by the result's `.strip()` (`:286`). Code reads the sentence as "a newline before any content does not stop generation (unchanged)".
- **(b) What is stored once content has been seen** (found by the referent check, its item 52). The existing stop drops the stop token whole: once content has been seen, a token that carries content and then a newline (for example `.\n`) is not appended, so its content is not stored (`olmo_hf.py:251–254`, `:274–277`). §2.2's definition would store that content and that token: the text "up to, and not including, the first line break that follows any non-whitespace character", and the ids ending "at the token that carried that line break". Code reads §2.2 as enforced on the adapter's returned result. The text is cut at its first line break, and the ids at the token whose decoded text first holds a line break after content. Nothing else changes: every generation whose text has no line break is stored exactly as the adapter returns it, stop-token handling included. Under this reading p:72's "no clean generation of record carries a line break, so §2.2 changes none of them" holds by construction (the referent check confirms that no clean text of record holds a line break). Under the literal reading it cannot be checked. The G-CAL-OLMo records store no token ids, so no one can tell whether a clean generation's stop token carried content, and G-CAL-p's clean-pool identity check could fail for that reason alone.

### Q3. Placement: the package, and the corruptor (p §4.2, p:84; p §1.4, p:56; ans:25). Code's call, made explicit

- **The call.** The package is `valence_core/p/`, a sibling on BUILD (F3)'s pattern, with drivers `scripts/p_sessions.py` and, under Q1 (b), `scripts/p_analyze.py`. **The corruptor goes in `valence_core/p/`, outside every module mf3 imports, not beside `corr.py`.** So do the adapter proxy (Q2), p's keys and schedule builder (Q4), and G-CAL-p's and G-SHAPE-p's tooling.
- **Why it is outside m's package:**
  - m's `package_sha256` covers every `valence_core/m/*.py` (`resume.package_sha256_of`), so a module beside `corr.py` moves `60199b36…feec`.
  - That hash is bound twice. The G-ANL-F3 analyzer's Q-F3 reader refuses unless LOCK-m-F3 names m's `package_sha256` (PIN-V2-12). And `scripts/mf3_sessions.py:177` asserts that the hash starts `60199b36`.
  - Beside `corr.py`, the corruptor would have to land before LOCK-m-F3 v0.1, with mf3's self-test and G-SHAPE-F3's record re-examined.
  - In `valence_core/p/` it moves none of m's package, mf3's licence, mf3's package or either analyzer closure.
- **(a) For the coordinating session's sequencing:** under this call, Q2's recommendation and Q1 (b), nothing of p touches a file or hash that LOCK-m-F3 v0.1 names. **Q-F3's lock chain need not wait for p.** It would wait only under Q1 (a′).
- **(b) G-CAL-p's tooling is p's own.** m's `gcal` builds its artifact from `corr.renders_m` and stops on any other renders (`gcal.py:386–387`: "the per-item renders are not corr.renders_m's"). G-CAL-p therefore reuses gcal's prompt, seeds, grader and generation call under Q0's form or by import, not its artifact builder. p §4.2 already lists G-CAL-p's tooling as p's.
- **(c) The renders' sha convention (minor).** m's G-CAL artifacts record `renders_sha256` as the full sha256 of the newline-joined renders, `corr.renders_sha` being its first 16 hex (p's renders: `6baf494960da4589`). p §1.2 defines the list's prefix by `json.dumps` (`1551c19997dc4541`). Code proposes that G-CAL-p's artifact records m's field by m's convention, and that p's step-3 entry quotes both.

### Q4. The schedule generation (p §4.1, p:82; p §4.2)

**What the record has:**
- **m's OLMo key families** (`keys.py:96–154`):
  - the schedule permutation `m-sched|{unit}|{arm}|{b}`, and the gate π `m-sched|{unit}|{gate}|{template}|0`;
  - the arm streams `m-olmo|…`, `m-olmo-time|…`, `m-olmo-qual|…`;
  - the item streams `m-olmo-items|{ckpt}|{s}` and `m-olmo-items-{gate}|{ckpt}|{s}`.
- **m's builder.** `valence_core.m.schedule` (schema `m-schedule-v1`, manifest `m-schedules-manifest-v1`, default root `data/m/schedules`) draws all of them through `valence_core.m.keys`.
- **mf3's precedent.** mf3 has its own `keys` and its own `schedule` module, importing `valence_core.m.schedule`'s helpers (`balance_report`, `cells_sha256`, `dumps_schedule`, `GATE_TABLE`, the schema names). It never edits m's.
- **What p names.** p:82 names three families, `p-olmo|…`, `p-olmo-time|…` and `p-olmo-qual|…`, the arm streams. It also says "the item-stream rule (m:159) under p's key prefixes".

**The questions:**
- **(i) The key map.** Do the item streams and the schedule permutation and gate-π keys take p's prefix too? Code proposes all six families, `m` → `p`: `p-sched|…`, `p-olmo|…`, `p-olmo-time|…`, `p-olmo-qual|…`, `p-olmo-items|…` and `p-olmo-items-{gate}|…`, so that no p stream coincides with an m stream. G-CAL-p's seeds stay `m-cal|…`, as p:72 binds them. With the arm keys alone changed, p's cells and item orders would be m's committed ones.
- **(ii) Unit and template strings in p's records.** Code proposes m's: `OLMo-{ckpt}`, `A0-OLMo-{ckpt}`, `A0s-OLMo-{ckpt}`. m's runner, read rule, record checks and analyzer functions then run unchanged. p is identified by its roots (`data/p/…`), its key prefixes, its package hash in every record's identity, and its lock. "PROPOSAL-p OLMo-{ckpt}" stays the name in entries and postings.
- **(iii) The builder.** Code proposes p's own `keys` module (the six p families) and m's builders run under Q0's form, with m's schema names reused as mf3 reuses them. The output root is `data/p/schedules/`, with its own manifest. The self-test check: with m's keys substituted back, the builder reproduces `data/m/schedules/`'s OLMo files byte for byte. If the seat declines Q0's form here, the fallback is mf3's: p's own builder over `m.schedule`'s helpers.

## 3. Observations (no question)

- **m's three OLMo NOT-RUN outputs (`0f35954`) were written by the G-ANL-F3 analyzer.** That is `scripts/m_analyze.py` at `e0b4f2c`, sha256 `6ec3222b…93d9`, not LOCK-m-F0's `655e0f7f…c16f`. p §8 step 1 and the seat's answers (ans:9) name the command, not the blob, and no OLMo lock exists to bind one. The outputs record the analyzer's sha256. This is recorded here because the referent check noted it (its item 92); it is not a question.
- **G-ACQ (n) is committed** (`e7e070f`), PASS on every part run; its BACKEND extension waits for the n package (GA-5). So p §6.2's "G-ACQ (n) continues as routed" is stale (referent item 89).
- **No `G-ANL-F3.json` is committed yet.** The canonical `ganl` run on `e0b4f2c` is G-ANL-F3's next step, and it waits for the coordinating session's word.

## 4. The referent check (p §9)

107 items: 85 CONFIRMED, 17 IMPRECISE, 3 FAIL, 2 NOT CHECKABLE. Code re-checked every item that was not CONFIRMED at source, and each finding held (item 38 stays not checkable). The agent's report and Code's dispositions are in `results/raw/2026-11-06_p_preread_referent-check.md`. None changes a question above except item 52, which is Q2 (b); item 40 also underlies Q0. Every correction is the seat's to make in v0.2; Code edits nothing of p.

- **The three FAILs:**
  - §0.3's "`thiru` → *thirteenth* (12 of 12)" is 6 of 12: DPO and instruct at seeds 1–3. SFT gives four other answers, and DPO and instruct refuse once each.
  - §0.3's "m's operand exclusion (v1.7, m:176)" is v1.8's: m:176 says "against v1.7's rule", and v1.7's §2.3 reads "fixed at rate 0.15." where v1.8's adds ", operand excluded". The seat's answers (ans:15) carry the same slip.
  - §0.4's anchor "n:§0.4" for figure4.csv's slopes: n's §0.4 is "Welfare and exposure", and the slopes are quoted at A-m1 §1.5 and §5.
- **Two IMPRECISE items that bear on planning:**
  - §6.1's gate-stage hours are already inside m:214's campaign figures (m:205: "applied to the unit's total + 26 sessions per checkpoint"), so the ≈ 45 min is counted twice. The loads add at most about 10 min for the three checkpoints, since m:205's basis already carries one.
  - §3.3's expectation misreads three of §1.2's own renders: items 7 and 8 keep their verb, and item 3's operator word "by" is garbled to "bh".
- **The other IMPRECISE items, all wordings** (proposed text in the raw):
  - in §0.3, the clean-miss list omits SFT's `▁4`, item 8's misses are class (c), not (a), `2025` is also 45², the failing items are left undefined, the banners are the same bytes, and "a garbled verb 4/4" fits only the four items whose operator stayed legible;
  - §1.4's "replacement arithmetic" is inline, not importable (Q0);
  - in §2.1, the line anchors, and the rule class: rule 13's stop discipline, not 28(d);
  - "m:155–159" should read m:159 and m:172;
  - "m:291's computations" should read m:278's and m:291's;
  - "the prebuild answers' R1" is the G-ANL-F3 answers' A1;
  - A-m1 §2.4 (b)'s sentence follows §8.1's status sentence (m:343), not m:338's label;
  - G-ACQ (n) is committed;
  - corr.py:187–200 should read :187–201.
- **The two NOT CHECKABLE items:**
  - the seat's numpy version; the renders reproduce on numpy 2.5.1 (§1);
  - item 52 (Q2 (b)).

## 5. What Code does meanwhile

- Nothing is built or locked.
- p's file stays untracked.
- The renders file is committed with this block, for the seat's read (p §1.3).
- Q-F3's lock chain waits for the coordinating session's word as before. Under Q3's call, nothing in this pre-read binds it.
