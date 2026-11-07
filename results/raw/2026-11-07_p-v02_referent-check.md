# PROPOSAL-p v0.2: the blind referent check (p §9, the body §0–§8, the "What changed" list, ans2's dispositions) — 2026-11-07

*Blind referent-check agent (fresh context; read-only on the repository). Document: `PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md`, untracked at root, sha256 `42f2977b941bc016d3155ba9e34828f1b050121d9f18a9e3307e3f7023cf3b32` (checked at start and end). Format after `results/raw/2026-11-06_p_preread_referent-check.md`. Verdicts: CONFIRMED; IMPRECISE (true but misleading, overstated, or not exactly as the source has it); FAIL (contradicted by the source); NOT CHECKABLE. Every number below was computed by a tool. Probe scripts are in `<scratch>/podwatch/probe/` (the session scratchpad), not in the repository.*

## The report

**159 items: 143 CONFIRMED, 13 IMPRECISE, 0 FAIL, 3 NOT CHECKABLE.**

**HEAD.** `139635f` at start and at end. No commit landed during the check. The files checked are clean at HEAD: `valence_core/m/`, `scripts/m_analyze.py`, `valence_core/adapters/olmo_hf.py`, `data/m/gates/` and `data/m/verdicts/`. I changed nothing in the repository.

**Method.**
- **The renders.**
  - §1.1's rule is implemented independently: FUNCTION_WORDS, words as maximal runs of ASCII letters matched case-insensitively, and words in single-quoted spans excluded.
  - `corr.corrupt_m` ran once per item, imported from `valence_core.m`. For each call, `corr._eligible_m` was swapped **in memory only** for m's eligible positions restricted to frame words. It was restored in `finally`, and restoration was asserted after the loop.
  - `corr.renders_m`, `corr.renders_sha`, `corr._k_m`, `corr.load_pool`, `corr.ROSTERS_OF_RECORD` and `keys.stream_known_answer` were used by import.
- **Environment.** Laptop venv `jlens-qwen36/.venv` (numpy 2.5.1), run with `PYTHONDONTWRITEBYTECODE=1` and `-B`. No `.pyc` file was written.
- **Sources.** The G-CAL figures come from the three committed artifacts' `records`. Line anchors were checked with `sed -n`. RESULTS entries were checked with `git show <commit>:RESULTS.md`.

### Header (v0.2:1–7)
1. v0.2's sha256 `42f2977b…3b32`. **CONFIRMED** (shasum at start and end; untracked at root).
2. "Supersedes v0.1 (sha256 `1821a235…9953`, STOPPED at §8 step 2 by Code's pre-read, `results/raw/2026-11-06_p_code-to-design_preread.md`, entry RESULTS.md@`fb742e4`); v0.1 is never committed". **CONFIRMED**:
   - the untracked v0.1's sha256 is `1821a23521cf…069953`;
   - `git log --all` shows no commit of v0.1;
   - `fb742e4` adds the raw and the entry "PROPOSAL-p v0.1 — PRE-READ (p §8 step 2): STOP …" at RESULTS.md@fb742e4:24.
3. "Dating as PROPOSAL-m m:6". **CONFIRMED** (m:6: "the commit hash is the timestamp of record").
4. `m:N` = PROPOSAL-m v1.11 at root, `42ab36ec…6c6b`. **CONFIRMED** (shasum `42ab36ecc814…96c6b`; last commit `05c4636`; clean).
5. `A-m1` = ADDENDUM-m1 v0.1 at root, `f26bc59`. **CONFIRMED** (the only commit touching the file; sha256 `ea08322d…9001`, as f26bc59's message gives it).
6. `n:` = PROPOSAL-n v0.2 at root, `5916097`. **CONFIRMED** (`PROPOSAL-n-bk-reconciliation-v0_2.md`; only commit `5916097`; clean).
7. `gcal`: the entry (`6ce8b9a`), the two raws, the three artifacts, schema `m-gcal-completability-v1`. **CONFIRMED** (`6ce8b9a --stat` adds all six; each artifact's `schema`).
8. `ans:` sha256 `4c3f57d4…bf82`, committed at `0f35954`. **CONFIRMED** (shasum `4c3f57d4ec4c…bf82`; `0f35954 --stat`).
9. `pre:` = the pre-read, with its renders raw and referent check, all at `fb742e4`. **CONFIRMED** (`fb742e4 --stat` adds all three, plus the values-check).
10. `ans2:` = `results/raw/2026-11-07_p-preread_design-to-code_answers.md`. **CONFIRMED** (tracked at `139635f`; sha256 `ab40f470…b08b`, as that entry gives it).
11. CLAUDE.md rules 9, 11, 13, 21, 23, 25, 27, 28(c) and 28(d). **CONFIRMED** (each rule exists and is used per its text; one use of rule 27 is item 92).
12. "o stays reserved for decision (12)'s state-present told control (n's header, the PI's word at the 11-05 routing)". **CONFIRMED** (n:4: "decision (12)'s state-present told control, if written, takes o (the PI confirmed at the 11-05 routing)"; m:16 (12)).

### §0.1
13. G-CAL-OLMo ran on 2026-11-06 on pod `qny1x4v8padeke`, backend identifier `641ee466f4553b6a`, box HEAD `1bf94a6`. **CONFIRMED**:
    - each artifact's `identity.backend_identifier`, `provenance[0].pod_id` and `gate.head` `1bf94a6c…`;
    - runs 2026-11-07T02:20:02Z–02:35:53Z UTC, which is 2026-11-06 PI-local;
    - RESULTS.md@6ce8b9a:54 and :62.
14. "the sixteen renders Qwen's G-CAL had passed". **CONFIRMED** (`identity.renders_sha256` `a04f67b0…4372` in the Qwen artifact and all three OLMo artifacts; Qwen's verdict PASS).
15. The condition-(4) figures. **CONFIRMED** (each artifact's `accuracy`, `condition_4` and `covariate`, recomputed as exact Fractions):
    - corrupted 42/64, 44/64, 42/64 and clean 62, 61, 59;
    - bars 7/10 and 93/128, 183/256, 177/256;
    - covariates +5/16, +17/64, +17/64;
    - Qwen +9/64 (57/64 vs 48/64, PASS).
16. m:324's "a checkpoint does not re-specify the shared dose", and "a Qwen G-CAL failure STOPs for re-specification, an OLMo one does not". **CONFIRMED** (m:324 verbatim, "… a Qwen G-CAL failure STOPs for re-specification and reaches NOT-RUN only through the Clock"; m:176).
17. The three NOT-RUN records were written at `0f35954` through `m_analyze.py not-run` on the analyzer at HEAD (`6ec3222b…93d9`), no OLMo lock binds one, and each carries the full read of its 128 generations. **CONFIRMED**:
    - the three outputs' `analyzer_sha256` is `6ec3222b…93d9`, which is `scripts/m_analyze.py` at HEAD, unchanged since `e0b4f2c`;
    - RESULTS.md@0f35954:57: "at HEAD `e0b4f2c`: G-ANL-F3's extended analyzer";
    - each of the three entries has its "full read of its 128 generations" block;
    - no `LOCK-m-OLMo-*` file exists.

### §0.2
18. m:338 needs the told control before an OLMo Q3 row can be *answered*. **CONFIRMED** (m:338: "*Answered* iff its own L0-OLMo-c").

### §0.3
19. The 16 per-item corrupted renders and their SFT/DPO/instruct hits. **CONFIRMED** (parsed from v0.2:17 by tool and compared with each artifact's `records`: 16/16 strings and 48/48 counts; the served renders are identical across checkpoints).
20. Clean misses are 2, 3 and 5 of 64. **CONFIRMED** — the ten clean misses are exactly these:
    - the wrong answers `September.`, `▁4`, `Four`, `<<April`;
    - the format artifacts `Answer:` and `<answer`;
    - the item-7 refusal at DPO and at instruct.

    By checkpoint: sft 2 s3, 4 s0; dpo 7 s1, 10 s2, 13 s0; instruct 2 s0, 7 s1, 10 s0, 10 s2, 13 s0.
21. "The failing items are the four at ≤ 2 of 4 on every checkpoint — 2, 9, 11, 15 (n_eligible 19, 10, 14, 14) — item 7, at k = 7, being 2 of 4 at instruct only". **CONFIRMED** (records; m:176's n list; `corr._k_m`).
22. `thiru` read as *thirteenth*, 6 of 12 (DPO and instruct, seeds 1–3); SFT's four give `maanum`, February, `Tishri`, `Narlei`; DPO and instruct each refuse once. **CONFIRMED** (records, with the refusals at s0; read raw O1, :53).
23. "`miyms` read as a product or a quotient (`2025` ×8 — 45² — `4050`, `4.5`)". The counts are **CONFIRMED** (`2025` at sft s0, s2, dpo s0–s2, instruct s0–s2; `4050` at instruct s3; `4.5` at sft s3). The wording is **IMPRECISE**:
    - the read raw's O1 (:53) says "every other answer multiplies or squares (2025, 4050, 4.5)";
    - no source calls any of these a quotient, and 90 ÷ 45 = 2 is none of the answers.
    - Fix: "`miyms` read as a multiplication or a square (`2025` ×8 = 45², `4050`, once `4.5`)", or pre-read item 10's own wording.
24. Class (a)'s other words (`timns`; `dsys`/`wemk`; `hourw`), with `ftrst`/`ybaa` no longer listed in (a). **CONFIRMED** (records).
25. Class (b)'s six strings sit on the three `Write the opposite of` items, whose clean renders score 4/4/4. **CONFIRMED** (dpo 5 s3 and dpo 15 s2; 11 s3 on all three; 15 s3 on all three; instruct 15 s2; dpo and instruct 11 s2; instruct 5 s3; clean items 5, 11, 15 at 4/4/4).
26. Class (c). **CONFIRMED** (sft 8 s2; dpo and instruct 8 s2 and s3; dpo and instruct 11 s1; instruct 1 s1):
    - item 8's five misses, all January (`Janbaa`, `Januwy` ×2, `Janyooar`, `Janaury`);
    - `dn`;
    - `Ther qro abov two dsys in a wemk`.
27. The four arithmetic items whose render left the operator legible (0, 3, 6, 12) are 16/16/16. **CONFIRMED** (records).
28. "the two whose operator word was struck (`miyms`, `timns`) are 2/12 and 7/12". The figures are **CONFIRMED** (item 9: 1+1+0; item 14: 3+2+2). The wording is **IMPRECISE**:
    - item 3's operator word was struck too: `divided` → `diyided` in `Coepqte 60 diyided by 5.`;
    - the same sentence lists that render among the legible four;
    - what separates the groups is legibility, not whether the operator word was struck.
    - Fix: "the two whose operator word was garbled past legibility (`miyms`, `timns`)".
29. The k formula sits at its floor of 3 on every failing item, and at rate 0.10 only items 4, 7 and 10 change. **CONFIRMED**:
    - `corr._k_m` on m:176's n list gives [3,3,3,3,4,3,3,7,3,3,4,3,3,3,3,3], sum 54;
    - the 0.10 analogue, (10n+50)//100 clipped, gives [3,3,3,3,3,3,3,5,3,3,3,3,3,3,3,3];
    - the two vectors differ only at items 4, 7 and 10.
30. "(v1.8's re-specification of v1.7's rule, m:176)". **CONFIRMED**:
    - m:176: "items 5, 11 and 15 lose 2, 1 and 3 positions against v1.7's rule";
    - `archive/PROPOSAL-m-gating-campaign-v1_7.md:59`: "fixed at rate 0.15.";
    - `…v1_8.md:137`: "fixed at rate 0.15, operand excluded."
31. "under the same banner bytes and prompt form (`banner_sha256` `6124c724…` in both artifacts; gcal.py:44–46)". **CONFIRMED**:
    - `6124c724758f…` appears in the Qwen artifact and in all three OLMo artifacts;
    - both substrates' `procedure.prompt` is `SESSION_BANNER + 'Task: {task}\nResponse:'`;
    - gcal.py:44–46: "b3's banner is ``SESSION_BANNER`` itself … so the prompt bytes are Qwen's".
32. "the covariate doubles at identical renders"; "identity and provenance clean". **CONFIRMED** (20/64 against 9/64 is ×2.22, and 17/64 is ×1.89; ans:13 and the G-CAL-OLMo entry).

### §0.4
33. Berg & Kaiser's slopes, 0.0366 at base and 0.978 at DPO, anchored to "A-m1 §1.5 and §5; `data/n/bk/experiment_results_csv/figure4.csv`". **CONFIRMED**:
    - figure4.csv is tracked (sha256 `c8f8dbe8…e638`); its hidden_state rows give base 0.036585… and dpo 0.978440…;
    - A-m1:32 (§1.5): "0.037 [0.015, 0.058] against 0.978 at DPO";
    - A-m1:67 (§5): "0.0366 [0.0153, 0.0579] … 0.978 [0.782, 1.173]".
34. "m's OLMo Q3 rows are the program's only pre-registered told controls across post-training stages". **NOT CHECKABLE**: an unanchored, program-wide scope claim. Nothing found against it: n's instructed-preference control (N4, n:72) runs on the one OLMo-2 checkpoint n acquires.
35. "Without p every OLMo row reads *concluded, not answered — the told control at this stage was not run: dose not completable* at v1 and v2 alike". **CONFIRMED** (m:338's template; `NOT_RUN_CAUSES["dose-not-completable"]`'s phrase, m_analyze.py:449–450; the three outputs' `rows`).
36. "a quarter-hour of GPU"; "≈ 3.4–4.5 h for three campaigns, m:214". **CONFIRMED** (02:20:02Z–02:35:53Z is 15 min 51 s; m:214: "Three checkpoints at 160/192/224 ≈ 3.4/3.9/4.5 h of generation").

### §0.5–§0.7
37. The cause `dose-not-completable`. **CONFIRMED** (m_analyze.py:449).
38. Ledger numbers 56–58. **CONFIRMED** (n:14 "(47 → 55)"; (56)–(58) occur only in p v0.1/v0.2, the pre-read raws and ans2).
39. (56): **CONFIRMED** (m:176: "serves all five units", and "14 of 16 golds recoverable, items 5 (…) and 15 (…) not — the operand exclusion above is the re-specification"; m:324). Its claims:
    - one substrate calibrated the shared dose for five units;
    - NOT-RUN is the only per-substrate path;
    - the operand was protected after two golds were read unrecoverable.
40. (57): "(gcal read §4 O5)". **CONFIRMED** (read raw :57).
41. (58): v0.1's "12 of 12", "n:§0.4" and "v1.7" were the referent check's three FAILs (items 9, 21, 17), and "(50)'s class". **CONFIRMED** (v0.1's text; the referent-check raw; n:14's (50) is a figure taken "from prose about a neighbouring figure"). The provenance glosses are the seat's own account of its errors.
42. §0.7: "the routing block of 2026-11-06 is the record of (1)–(8) as v0.1 put them". **CONFIRMED** (RESULTS.md@0f35954:31–33 quotes the block; its items match v0.1's §0.7 (1)–(8)):
    - the date;
    - the route for the pre-read;
    - the letter p;
    - the rule "[confirmed as written]";
    - D_p;
    - 12 h;
    - the pod order;
    - §5's rule and its two sentences.
43. "the routing of this version confirms them on v0.2's text and adds (9)". **NOT CHECKABLE**: it was forward-looking when written.
    - The 2026-11-07 routing at RESULTS.md@139635f:83 reads "3. PROPOSAL-p v0.2: [route to step 3]; route (b) and the register [accepted]". That is (2) and (9).
    - It restates none of (1) or (3)–(8).
    - It has no date item like the 11-06 block's "1. Date: [2026-11-06]". So the header's "the PI confirms the date at routing" (2026-11-07) has no bracketed confirmation in the quoted block. This matters for step 3's record of §0.7.

### §1
44. §1.1: everything is m:176's except the eligible set, restricted to the frame. **CONFIRMED** (m:176; corr.py:224, :225, :233, :236, :240, :209). That is:
    - the key `corr|{i}`;
    - one permutation;
    - one `integers(25)` draw per visited slot;
    - the replacement formula;
    - the roster skip on both rosters;
    - the k formula.
45. n_eligible is 6–12 under the restriction, k = 3 throughout, and m's render is reproduced on items 0 and 12, the only two whose eligible set is unchanged. **CONFIRMED**:
    - n_p = [6,8,8,7,8,7,6,12,8,6,8,7,6,8,6,7];
    - the eligible set equals m's on items 0 and 12 only;
    - the render equals m's on items 0 and 12 only.
46. §1.2's sixteen rows (frame words; n m → p; k; render; the "(= m's)" marks; gold). **CONFIRMED** (every cell compared by tool against the in-memory run: 0 mismatches; golds are `pools.json`'s).
47. "k sums to 48 (m's 54); no roster skip on any item; no roster word occurs in any render as a substring (both rosters, case-insensitive); every n_eligible ≥ 6, so k ≤ ⌊n/2⌋". **CONFIRMED**:
    - Qwen roster 8 words, OLMo roster 8, 12 distinct: 0 substring hits for either roster;
    - every render changes exactly 3 positions.
48. By p's convention, `1551c19997dc4541` (full `1551c19997dc45419c496d7f64a61711735672f9388bab4be2e2c1a450f85722`). **CONFIRMED**.
49. By m's convention, `6baf494960da4589` (full `6baf494960da45896206f7eaadbc6b158642a42e09e1d11f70812959e3673c4c`); m's renders `a04f67b0e5105a05`; the G-CAL artifacts record the newline-joined renders' full sha256 as `renders_sha256`. **CONFIRMED** (`corr.renders_sha`; gcal.py:388–391; `identity.renders_sha256` `a04f67b0…4372` is the sha256 of `"\n".join(corr.renders_m(...))`).
50. The renders equal `results/raw/2026-11-06_p_preread_renders.txt`, on numpy 2.5.1, with `keys.stream_known_answer()` clean. **CONFIRMED** (the raw's `json.dumps(renders)` line equals the recomputed list; the known answer is `[]` on numpy 2.5.1).
51. §1.3: **CONFIRMED** (ans2 §0; keys.py:37–41):
    - the seat's read of record, 2026-11-07, on Code's file: 16 of 16, with the glosses;
    - it is repeated only if the renders change;
    - a known-answer mismatch is a STOP before any session.
52. §1.4: `corrupt_p` is `corr.corrupt_m` with `_eligible_m` swapped for the call; the replacement expression is "inline at `corr.py:236`, not importable"; `_k_m`, `load_pool` and the roster words are imported by name. **CONFIRMED** (corr.py:236; :204, :176, :135/:138/:141; ans2 Q0).
53. "it is one of the eleven m files mf3's licence names by sha (BUILD (F3), `cd9756e`)". **CONFIRMED**:
    - RESULTS.md@cd9756e:24 ff. lists the ten imported modules plus `__init__`;
    - its `corr` hash `74818109…7fce` equals HEAD's corr.py;
    - `valence_core/mf3/guard.py:66–71` (`M_HASHED`).
54. `data/f/pools.json` `8547d9a11ba55b95`. **CONFIRMED** (sha256 `8547d9a11ba55b95dda2…`; corr.py:80).

### §2
55. §2.1: `OLMoHFAdapter.generate` checks `_is_stop` (:290–294) before setting `content_seen` (:251/:256 on the cached path, :274/:279 on the uncached); `_is_stop` needs `content_seen`, so a first token carrying content and a newline is appended. **CONFIRMED**:
    - olmo_hf.py:242–262 is the `if cached:` branch and :263–280 the uncached one;
    - :293 requires `content_seen`;
    - that `---\n\n` was a single token is not stored, but a stored `---\n\nTask: …` can arise only this way.
56. Two stored texts carry a line break (DPO and instruct, corrupted item 15 seed 0, the two quoted texts); no clean generation does ("pre:§4 item 51"). **CONFIRMED** (records: 2 of 384, and 0 of the 192 clean texts; referent-check raw item 51).
57. "A stop-discipline defect (rule 13)". **CONFIRMED** (CLAUDE.md rule 13, "stop discipline"; ans2 §6 on item 46).
58. §2.2: `STOP_CAP` = 60; "(2 of G-CAL-OLMo's 384)"; m's runner stores what is returned (`SessionLog.add_round`); "the stop token dropped whole, as today"; "a newline before any content does not stop generation, as today". **CONFIRMED** (session_e2a.py:90; scaffold.py:385–392; olmo_hf.py:251–254, :274–277, :293).
59. §2.3: m:258's eight declared strings; the DEL of instruct item 7 s1; the added harness-shaped strings occur in the records. **CONFIRMED**:
    - m:258: "with the two reasoning-block lines, eight declared harness strings";
    - instruct corrupted 7 s1 starts with `\x7f`;
    - `Reasoning:` at 7 s3 on all three, `Answer:` at clean 13 s0 ×2, `Input:` on item 5.

### §3
60. §3.1's procedure, "as the G-CAL-OLMo artifacts record them". **CONFIRMED** (`procedure.generation`, `.boundary` and `.seeds`, and the `identity` of all three artifacts; `keys.cal_seed`). It covers:
    - uncached generation, `injections=()` and the newline stop;
    - each checkpoint's ban list, ids sha16 `2dd86a453a2275ef`;
    - `STOP_CAP` 60 and TEMP 0.7;
    - the rule 28(d)(a) boundary before every generation;
    - seeds `crc32('m-cal|{pool}|{i}|{seed}') % 2**31`, seed 0..3.
61. "m's stops on any renders but `corr.renders_m`'s, `gcal.py:386–387`". **CONFIRMED** (in `_renders_of_record`; m's completability path also takes `corr.renders_m` at :795).
62. "Grader f0's `normalize`/`grade`, ported verbatim (m:176)". **CONFIRMED** (m:176; `procedure.grader` reads "f0's normalize / grade, ported verbatim (f0_calibrate.py:56-66)").
63. The clean pool's 64 generations are the same (prompt, seed) pairs as G-CAL-OLMo's. **CONFIRMED**:
    - the clean tasks are unchanged, and m:176's seed key carries no render or checkpoint field;
    - no clean text of record holds a line break, so §2.2's proxy leaves all 192 clean texts as stored.

    Byte-for-byte reproduction is the run's own check.
64. §3.2: conditions (1)–(4) as in m:176, and the bars 47/46/45. **CONFIRMED** (exact Fractions; pre §1):
    - ⌈.70 × 64⌉ = ⌈44.8⌉ = 45;
    - ¾ × 62, 61, 59 = 46.5, 45.75, 44.25, so the bars are 47, 46, 45.
65. The covariates "reported beside", with f1's 0.12 figure (+.078). **CONFIRMED** (`covariate.f1_012_of_record` "0.078125 (+.078)"; m:176).
66. §3.3's tallies. **CONFIRMED** (records):
    - Compute 20/19/18 of 24, the four legible items at 16/16/16;
    - Write 5/5/5 of 12;
    - State/Name 17/20/19 of 28, against clean 26/25/23.
67. §3.3 re-read against §1.2's renders. **CONFIRMED** (changed positions per render: item 3 hits Compute and `by`; item 7 hits `which` and `is`; item 8 hits `the` and `of`):
    - the Compute operators are intact, and item 3's `by` → `bh` is the one function word struck among them;
    - the verb is garbled on items 1, 4, 10, 13, and `Niye` on item 2;
    - items 7 and 8 keep their verb.

    Items 7 and 8 each have two function words struck, as the parenthesis lists.
68. "≈ 53/52/50 of 64"; "the checkpoints land at the bars". **NOT CHECKABLE**: the seat's forecast. It sits under the 55/54/52 ceiling its own components give.

### §4
69. §4.1: the P/Q delivery of m:159, with CORR_clean on the sham arm (m:172). **CONFIRMED** (m:159; m:172: "Sham arms serve `CORR_clean` to both labels").
70. All six OLMo key families go `m` → `p`, and G-CAL-p keeps `m-cal|…`. **CONFIRMED** (keys.py:96–154 and m:159: `m-sched|{unit}|{arm}|{b}`, `m-sched|{unit}|{gate}|{template}|0`, `m-olmo|`, `m-olmo-time|`, `m-olmo-qual|`, `m-olmo-items|`, `m-olmo-items-{gate}|`; `m-cal|` is G-CAL's direct seed).
71. Floors 80/32 (m:205); α .01 and A0's outcome order (m:326); the per-arm computations of m:278. **CONFIRMED**.
72. Bars, cadence, blinding and reads. **CONFIRMED** (m:302: "the seat's read under §3's rule — the sham session redacted, the contrast session's forced rounds only", and picks to the checkpoint file):
    - hair triggers;
    - `round_degeneracy` at p0 .02 on the sham domain;
    - the G-TIME-OLMo bar (m:271, m:302);
    - the cadence (m:330);
    - blinding (m:318);
    - the G-TIME read.
73. The lock chain's "LOCK v1.0 with D_p and 'preprint of record pending'". **IMPRECISE**:
    - m:302's rule is conditional: "the preprint of record's hash if it is placed, else 'preprint of record pending' — an OLMo lock does not wait for the placement";
    - A-m1:59 (§4 step 4, the chain v0.2 adapts) keeps the condition: "'preprint of record pending' where it is (m:302)";
    - v0.2 writes the else-branch unconditionally, unchanged from v0.1.

    The rest of the chain is m:302's, and "— secondary DVs" is A-m1:59's.
    - Fix: "LOCK v1.0 with D_p and the preprint of record's hash, or 'preprint of record pending' where it is (m:302)".
74. The box-change rule (m:302; §2.4, at m:251), the hours and looks (m:205–214, m:330), the base checkpoint not run (decision (7′); m:16 (14)), NOT-RUN and PENDING (m:324), and decisions recorded under m:318. **CONFIRMED**.
75. §4.2: "on BUILD (F3)'s pattern (Q1 (C2), `cd9756e`)", with the licence naming each file "by name on one lock line". **CONFIRMED** (f3-build prebuild answers :9–14; RESULTS.md@cd9756e, finding 8: "each m file by its path and sha256 on one line").
76. "**No file a live lock or licence names is edited:** … `valence_core/adapters/olmo_hf.py` (§2.2)". **IMPRECISE**. No live lock or licence names olmo_hf.py:
    - LOCK-g.md, LOCK-h.md and LOCK-m-F0.md do not mention it;
    - mf3's licence (`guard.M_HASHED`) covers `valence_core/m` files only;
    - G-SHAPE-F0's sources map (gshape.py `SCORING_STACK_FILES`/`TOOLING_FILES`) does not list it;
    - pre:Q2: "Nothing that binds `valence_core/adapters/olmo_hf.py` today".

    It stays unedited by §2.2's choice and is first named by LOCK-p v0.1.
    - Fix: name it apart: "… and `valence_core/adapters/olmo_hf.py`, which no lock names today, unedited by §2.2 (LOCK-p v0.1 names it)".
77. The rest of that list. **CONFIRMED** (gshape.py:105, `TOOLING_FILES`; LOCK-m-F0.md; `guard.M_HASHED`):
    - LOCK-m-F0's record;
    - the eleven m files;
    - PIN-S10's sources map, `scripts/m_sessions.py` included;
    - `scripts/m_analyze.py`.
78. §4.3: **CONFIRMED** (ans2 Q1 (i), Q3 (a)):
    - Q-F3's lock chain does not wait for p;
    - LOCK-p v0.1 is written after LOCK-m-F3 v0.1;
    - the one-round rule extends to p;
    - the seat rules if LOCK-m-F3 v0.1 is not yet written when p is ready to lock.
79. §4.4: `run_posting_v2` (m_analyze.py:4344), "PIN-23's form" (`crosscheck_coordinate`, :2660), "m:291's tuple space" and G-ANL-F3's v2 battery. **CONFIRMED** (519,480 tuples, m:291). A note: `run_posting_v2` already reads Q-F3's coordinate from its own `f3_dir`, while Q-F0's and the OLMo coordinates share one `verdicts_dir`. So the resolution that is new is between Q-F0 and the OLMo units.
80. The regression's anchors: "Q-F0's two, on the G-ANL-F3 battery's identity binding" (A1's case at `e0b4f2c`) and "the three OLMo NOT-RUN outputs at `0f35954`". **CONFIRMED**.

### §5
81. §5.1. **CONFIRMED** (m:338; m:343; A-m1:42):
    - the rows' labels are m:338's (Step 2);
    - in §8.1 (Step 7, m:343) the status sentence is followed by A-m1 §2.4 (b)'s sentence, then by the PI's declared sentence;
    - both are values-checked at POSTING v1;
    - the abstract's clause takes m:338's "none" form.
82. §5.1's state text, "*NOT-RUN at G-CAL-OLMo, 2026-11-06, condition (4): [x]/64 against 7/10 and ¾ × [clean]/64*". **IMPRECISE**:
    - the seat's declared ending (ans:9) is "*… NOT-RUN at G-CAL-OLMo, condition (4): corrupted-pool accuracy [x]/64 against 7/10 and ¾ × [clean]*";
    - v0.2 adds the date, drops "corrupted-pool accuracy" and adds "/64" after [clean];
    - the pre-read recorded this as an uncounted note under its item 78, and ans2 does not dispose it.
    - Fix: give ans:9's form, or mark v0.2's as a paraphrase of the PI's words at the posting.
83. §5.2: p's unit is "the told control at this stage" in m:338's rule, and m's NOT-RUN rows stand beside as text. **CONFIRMED** (m:338; ans2 Q1 (iv)). m:338's third bracket, "is pre-registered and pending at this posting", is rightly absent at v2, where m:324 closes PENDING.
84. §5.3. **CONFIRMED** (RESULTS.md@0f35954:31–33; A-m1:28 and RESULTS.md@18c32df:73; A-m1:24: "applies to exactly three units now"; m:16 (11) and A-m1:40; n:152):
    - D_p 2026-12-15, the PI's word of 2026-11-06;
    - "inclusive to 23:59:59 UTC on the committer date (C7's convention)";
    - "p has no decision (16)";
    - D2 2026-12-22;
    - D_n and D_n-lap untouched.
85. §5.4: "the unit was pre-registered on 2026-11-06". **IMPRECISE**:
    - the sentence is v0.1's, unchanged;
    - v0.2's header gives PI date 2026-11-07, and v0.1 was never committed;
    - m:6 makes the commit hash the timestamp of record, so p's units are pre-registered at v0.2's step-3 commit, not before 2026-11-07;
    - 2026-11-06 is v0.1's date and routing, which confirmed the rule as then written;
    - §8 step 3 writes this disclosure sentence into the COMMITTED entry.
    - Fix: the step-3 commit's date (or the date the PI confirms at routing), e.g. "pre-registered on [step-3 date] (the frame-word rule routed 2026-11-06)".

### §6
86. §6.1: G-CAL-OLMo's three runs took "16 minutes wall-clock with their loads (02:20:02Z–02:35:53Z, gcal)", and G-CAL-p, with the same count of generations, takes "under half an hour". **CONFIRMED** (gcal raw :24–30, one process and one load per checkpoint; 15 min 51 s; 384 generations).
87. "inside m:214's campaign figures already (m:205: 'the unit's total + 26 sessions per checkpoint')". **CONFIRMED** (m:205 verbatim: "applied to the unit's total + 26 sessions per checkpoint (24 qualification + 2 timing)").
88. "one cold load per checkpoint (176–212 s, the smoke raw) ≈ 10 min for the three". **CONFIRMED** (smoke raw :19, :39, :59 give 211.6, 175.7 and 183.3 s; the sum is 570.6 s = 9.5 min).
89. "≈ 3.4/3.9/4.5 h for the three at 160/192/224 sessions". **CONFIRMED** (m:214; recomputed from m:205's bases with the +26: 3.35, 3.93 and 4.51 h).
90. The budget, "12 h (the PI's word of 2026-11-06)", at "$1.79/h". **CONFIRMED** (RESULTS.md@0f35954:31–33; RESULTS.md@6ce8b9a:96, "RUNNING at $1.79/hr").
91. §6.2. **CONFIRMED** (m:251, m:302; the routing block; RESULTS.md@e7e070f:24–32: "PASS on every part run" and "Not run: the BACKEND extension's 24 fresh-versus-cached reads, which wait for the n package (GA-5)"). It covers:
    - the respawn protocol and a BACKEND entry if the box is not `qny1x4v8padeke` at `641ee466f4553b6a`;
    - a box change after a lock restarting that checkpoint under m:302;
    - the pod order (the PI's word of 2026-11-06);
    - "G-ACQ (n) is complete (`e7e070f`); its BACKEND extension waits for the n package".
92. §6.2: "each campaign within one pod session (rule 27)". **IMPRECISE**:
    - rule 27 is the commit-before-stop provenance law;
    - "one campaign per pod session" comes from the respawn protocol's consistency clause ("a verdict campaign completes on ONE characterized backend") and m:251 ("Each OLMo checkpoint's campaign runs within one pod session on one characterized backend (CLAUDE.md:127–130 …)");
    - §4.1 attaches rule 27 correctly ("raws and checkpoints committed before the pod stops (rule 27)");
    - the text is carried from v0.1.
    - Fix: "(m:251; the respawn protocol's consistency clause)".
93. §6.3 = m:330. **CONFIRMED** (m:330: looks every 40 launches and at the end; `round_degeneracy` at OLMo p0 .02 on the sham arms; "Code never self-adjudicates").

### §7–§8
94. §7: "exactly what m:338 and m:343 let an OLMo told control license". **CONFIRMED**.
95. §8: steps 1 and 2 done at `0f35954` and `fb742e4`; step 2's v0.2 check matches ans2 §9 item 2. **CONFIRMED**.

### §9 (v0.2:138)
96. The m anchors m:6, m:16 ((7′), (12)), m:159, m:172, m:176, m:205–214, m:251, m:258, m:271, m:278, m:291, m:302, m:318, m:324, m:326, m:330, m:338, m:343 and m:358. **CONFIRMED** (each opened; m:251 lies inside §2.4, m:178–252; m:358 is step 17, which §8 step 1 paraphrases).
97. The A-m1 anchors §1.5 (:32), §2.4 (b) (:42), §2.5 (:44), §3 (:46–52), §4 step 4 (:59) and §5 (:65–67). **CONFIRMED**: each exists. Item 113 covers §3's use.
98. n's header letter sentence (n:4) and §8 step 6 (n:159: "importing `valence_core.m`'s shared modules and `valence_core.adapters.olmo_hf` unchanged"). **CONFIRMED**.
99. The RESULTS entries at `6ce8b9a`, `0f35954`, `e0b4f2c`, `e7e070f`, `fb742e4` and `cd9756e`. **CONFIRMED**: each commit adds the named entry at RESULTS.md@<commit>:24 (G-CAL-OLMo; the three NOT-RUN entries; G-ANL-F3 BUILD; G-ACQ (n); the p pre-read; BUILD (F3)).
100. The artifacts' fields `procedure`, `condition_4`, `identity.backend_identifier`, `identity.banner_sha256` and `renders_sha256`. **CONFIRMED**. The last sits at `identity.renders_sha256`; there is no top-level `renders_sha256`.
101. `data/m/verdicts/OLMo-{ckpt}_NOT-RUN.json`. **CONFIRMED** (sha256 `72745cb4…`, `94869b83…` and `e2ecef56…`, as the 0f35954 entries give them).
102. The read raw's §4 (O1–O7, :52–59) and §5 (:61–545). **CONFIRMED**.
103. `results/raw/2026-11-06_p_preread_renders.txt`. **CONFIRMED** (item 50).
104. `data/n/bk/experiment_results_csv/figure4.csv`. **CONFIRMED** (item 33).
105. corr.py:187–201 (`_eligible_m`), :204–209 (`_k_m`), :212–252 (`corrupt_m`) and :236. **CONFIRMED**.
106. keys.py:27–29 (`stream`) and :96–154 (`item_key`, `arm_key`, `item_gate`, `sched_key`, `gate_sched_key`). **CONFIRMED**.
107. gcal.py:44–46 and :386–387. **CONFIRMED** (items 31 and 61).
108. olmo_hf.py:237–294 (`store` at :237 through `_is_stop` at :290–294), :251/:256 and :274/:279. **CONFIRMED** (the file is unchanged since `e26e9c9`).
109. The `scripts/m_analyze.py` symbols, at HEAD (`6ec3222b…93d9`). **CONFIRMED**:
     - not-run's usage (:35);
     - `NOT_RUN_CAUSES["dose-not-completable"]` (:449–450);
     - `validate_not_run_record` (:632);
     - `UNITS` (:162);
     - `clock_of_record` (:548);
     - `run_not_run`'s `ckpt_dir` (:2550–2552; the default `REPO / CKPT_REL` = `data/m/ckpt` at :2583, :109);
     - `run_posting_v2` (:4344);
     - `crosscheck_coordinate` (:2660).
110. `scripts/mf3_sessions.py:177`. **CONFIRMED** (the self-test asserts that m's `package_sha256` starts with `60199b36`, with 18 m files).
111. `data/f/pools.json`. **CONFIRMED** (item 54).
112. ans and ans2. **CONFIRMED** (items 8 and 10).
113. §9 as "only what this document quotes". **IMPRECISE**.
     - It lists two referents the body does not quote:
       - A-m1 §3, which v0.2 no longer quotes (v0.1's §6.1 "as A-m1 §3 offered" was cut);
       - `scripts/mf3_sessions.py:177`, which v0.2's body never cites (ans2 Q3 does).
     - It omits referents the body does quote:
       - A-m1 §1.1, decision (16) (§4.1, §5.3);
       - A-m1 §1.3, D_O′ and C7's convention (§5.1, §5.3);
       - m:16 (11), D2 2026-12-22 (§5.3);
       - the smoke raw, `results/raw/2026-11-06_gcal-olmo_smoke.txt` (§6.1's 176–212 s);
       - the gcal run raw (its stamps).
     - Item 100's field path is a further nit.
     - Fix: drop A-m1 §3 (and mf3_sessions.py:177 unless the body cites it); add A-m1 §1.1 and §1.3, m:16 (11) and the smoke raw.
114. The [S] figures §9 asks to reproduce. **CONFIRMED**:
     - §1.2's table and both sha conventions (items 46–50);
     - 47/46/45 (item 64);
     - 6 of 12, item 8's five and `2025` ×8 (items 22, 23, 26);
     - the rate-0.10 vector (item 29);
     - §6.1's hours (items 86–89).

### "What changed from v0.1" (v0.2:7), against ans2 and the pre-read referent check
115. "every item of pre:§4's referent check and pre:§2's five questions is disposed in ans2". **CONFIRMED**:
     - ans2 §1–§5 answer Q0–Q4;
     - ans2 §6 disposes the three FAILs, the seventeen IMPRECISE items, and items 38 and 52;
     - the STATE notes under items 70 and 92 are handled at ans2 §2 and §8.
116. "§0.3's three FAILs corrected (6 of 12, not 12 of 12; v1.8's operand exclusion; the lineage slopes anchored to A-m1 §1.5 and §5) and its fourteen wordings". **IMPRECISE**.
     - All three corrections appear in v0.2: two in §0.3 and one in §0.4.
     - FAIL 21 was §0.4's, not §0.3's: the referent-check raw lists item 21 under "## §0.4".
     - "Fourteen" matches the fourteen IMPRECISE items dispositioned "For v0.2" other than the two planning items 57 and 85: items 8, 10, 11, 15, 18, 20, 43, 46, 58, 71, 73, 78, 89 and 96. Only six of those (8, 10, 11, 15, 18, 20) are §0.3's, and the rest are named again later in the same paragraph.
     - Fix: "the three FAILs corrected (§0.3 ×2, §0.4) and the referent check's fourteen wordings (six in §0.3)".
117. "§1.2 carries m's sha convention beside p's and names the renders of record". **CONFIRMED** (ans2 Q3 (c) and §0; v0.2 §1.2).
118. "§1.4 states the corruptor's form (Q0)". **CONFIRMED** (ans2 Q0; v0.2 §1.4).
119. "§2.1's classification and anchors". **CONFIRMED** (items 43 and 46; v0.2 §2.1).
120. "§2.2 is the reading Code's pre-read calls (b) … through a proxy, `olmo_hf.py` unedited (Q2)". **CONFIRMED** (ans2 Q2; v0.2 §2.2).
121. "§3.3's expectation re-read against §1.2's own renders". **CONFIRMED** (item 57; v0.2 §3.3).
122. "§4.1's key families (Q4) and m's unit and template strings in p's records". **CONFIRMED** (ans2 Q4 (i)–(ii); v0.2 §4.1).
123. "§4.2's substitution register (Q0) and the adapter proxy". **CONFIRMED** (ans2 Q0, Q2; v0.2 §4.2).
124. "§4.3's sequencing against LOCK-m-F3". **CONFIRMED** (ans2 Q1 (i), Q3 (a); v0.2 §4.3).
125. "§4.4's analyzer path fixed at route (b) with the v2 posting through `scripts/p_analyze.py` (Q1)". **CONFIRMED** (ans2 Q1; v0.2 §4.4).
126. "§5.1's placement of the declared sentences". **CONFIRMED** (item 78; v0.2 §5.1).
127. "§6.1's hours and §6.2's G-ACQ state". **CONFIRMED** (items 85 and 89; ans2 §8; v0.2 §6.1–§6.2).
128. "§8 renumbered around the steps already done". **IMPRECISE**: nothing was renumbered.
     - v0.2's §8 keeps v0.1's step numbers 1–7 (v0.1:122–128 and v0.2:124–130 both run "1." to "7."), and `139635f` routes v0.2 to "its s8 step 3".
     - What changed instead: steps 1 and 2 are marked done; step 2 adds v0.2's check; step 6 adds `scripts/p_analyze.py`; the Entries line drops m's NOT-RUN entries.
     - Fix: "§8's steps 1–2 marked done (numbering kept)".
129. "§9's anchors". **CONFIRMED** (item 96's correction applied and new anchors added; completeness at item 113).
130. "ledger (58)". **CONFIRMED** (ans2 §6; v0.2 §0.6).
131. Completeness: an unlisted change to a PI-confirmed rule. **IMPRECISE**.
     - §1.1 now reads "a word being a maximal run of ASCII letters, matched case-insensitively" (v0.1: "… ASCII letters;").
     - The change traces to neither ans2 nor the referent check.
     - The 11-06 routing confirmed "§1's frame-word rule [confirmed as written]" on v0.1's text.
     - It is inert on this pool: no CORR_clean task has a capitalized word after its first, so the frame words and all sixteen renders are identical under either matching (tool).
     - The other unlisted edits all trace to a disposition:
       - §0.1 (ans2 §8);
       - §0.6 (57) (item 46);
       - §0.7 (the routing);
       - §1.3 (ans2 §0);
       - §2.3's reporting tool and "Levenshtein";
       - §3.1 (Q3 (b); item 52);
       - §3.2 (Q3 (c); Q1 (iii));
       - §5.2;
       - §5.3, §6.1 and §6.2's "the PI's word of 2026-11-06".
     - Fix: add "§1.1 states its case-insensitive match (inert on the pool)" to the list.

### ans2 §6: the referent check's items, each against its proposed fix and v0.2's text
132. FAIL 9 (fix: "6 of 12 …"), at v0.2 §0.3: "(6 of 12: DPO and instruct at seeds 1–3; SFT's four give other names …; DPO and instruct refuse once each)". **CONFIRMED** (applied, reworded; true to the records).
133. FAIL 17 (fix: "(v1.8, re-specifying v1.7's rule; m:176)"), at v0.2: "(v1.8's re-specification of v1.7's rule, m:176)". **CONFIRMED**.
134. FAIL 21 (fix: "(A-m1 §1.5, §5; figure4.csv …)"), at v0.2 §0.4. **CONFIRMED**.
135. IMPRECISE 8 (add `▁4`): applied verbatim. **CONFIRMED**.
136. IMPRECISE 10 (fix: "`2025` (45², or a year), `4050` (a product), once `4.5`"): applied in part. **IMPRECISE**; this is the same finding as item 23.
     - The counts and 45² are carried.
     - "or a year" is dropped.
     - The readings are recast as "a product or a quotient", which neither the fix nor the read's "multiplies or squares" says.
137. IMPRECISE 11 (drop `ftrst`/`ybaa` from (a)): dropped, and item 8's five misses now sit in (c). **CONFIRMED**.
138. IMPRECISE 15 (define the failing items): "The failing items are the four at ≤ 2 of 4 …". **CONFIRMED**.
139. IMPRECISE 18 (same banner bytes): "under the same banner bytes and prompt form (`banner_sha256` …; gcal.py:44–46)". **CONFIRMED**.
140. IMPRECISE 20: "The four arithmetic items whose render left the operator legible …". **CONFIRMED**. The clause added after it is item 28.
141. IMPRECISE 40 (disposition "Q0 of the STOP"): §1.4 follows ans2 Q0 (the expression is inline and runs inside `corrupt_m`), not the raw's alternative "restated and asserted equal". **CONFIRMED**: ans2 Q0 supersedes the alternative, and the raw's own table routed item 40 to Q0.
142. IMPRECISE 43 (anchors): "(`:251`/`:256` on the cached path, `:274`/`:279` on the uncached)". **CONFIRMED** (the path labels are right).
143. IMPRECISE 46 (rule class): "A stop-discipline defect (rule 13)", and (57)'s "read against rule 28(d)" became "read against the stored-text boundary". **CONFIRMED** (the seat's own reclassification, ans2 §6).
144. IMPRECISE 57, at §3.3. **CONFIRMED**.
145. IMPRECISE 58: "of m:159 … m:172". **CONFIRMED**.
146. IMPRECISE 71: m:278 for the per-arm computations (§4.1, §4.4) and m:291 for the tuple space. **CONFIRMED**.
147. IMPRECISE 73: v0.1's sentence citing "the prebuild answers' R1" went out with route (a). v0.2's regression cites "the G-ANL-F3 battery's identity binding", which is A1's case at `e0b4f2c`. **CONFIRMED**: disposed by removal, and no wrong anchor remains.
148. IMPRECISE 78, at §5.1. **CONFIRMED**.
149. IMPRECISE 85, at §6.1: the fix text is applied nearly verbatim. **CONFIRMED**.
150. IMPRECISE 89, at §6.2. **CONFIRMED**.
151. IMPRECISE 96, at §9: "corr.py:187–201". **CONFIRMED**.
152. NOT CHECKABLE 38: moot, since §1.2 now cites Code's numpy 2.5.1. **CONFIRMED**.
153. NOT CHECKABLE 52: §2.2's reading (b). **CONFIRMED**.
154. ans2 §6's own list (FAILs 9, 17, 21; IMPRECISE 8, 10, 11, 15, 18, 20, 40, 43, 46, 57, 58, 71, 73, 78, 85, 89, 96) equals the referent-check raw's dispositions table, item for item. **CONFIRMED**.

### ans2's rulings against v0.2 §2.2, §4.1, §4.2, §4.4
155. Q2 → §2.2. **CONFIRMED**; nothing is missing or contradicted:
     - the proxy in `valence_core/p/`, with `olmo_hf.py` unedited;
     - LOCK-p v0.1 names olmo_hf.py's sha256 (§4.2's licence);
     - the cost is accepted;
     - reading (a) is confirmed;
     - reading (b) is adopted, in near-verbatim text;
     - item 52 is disposed.
156. Q4 → §4.1 (+§4.2). Three parts are **CONFIRMED**:
     - (i) the six families, with `m-cal|…` kept;
     - (ii) m's unit and template strings, the `proposal: PROPOSAL-p` field with p's sha256, the source guard refusing m's and mf3's roots, and the entry name;
     - (iii) p's keys and m's builders under register entry (2), `data/p/schedules/` with its own manifest, and the self-test of (c).

     One clause of (iii) is missing: "m's schema names reused as mf3 reuses them", which v0.2 does not state. **IMPRECISE**: an omission, not a contradiction.
     - Fix: add "m's schema names reused, as mf3 reuses them" to §4.1's schedule clause.
157. Q0 → §4.2 (+§1.4). **CONFIRMED**:
     - the one declared form;
     - terms (a)–(d), carried in substance;
     - term (e), carried as "Any site not in the register is a STOP, never a copy";
     - register entries (1)–(4);
     - §1.4's correction.
158. Q1 → §4.4 (+§4.3). **CONFIRMED**:
     - (i)–(iv);
     - G-ANL-p's cases and the regression;
     - LOCK-p v1.0 naming both blobs;
     - G-ANL-p's artifact, named at LOCK-p v0.1, recording them.

     Two notes:
     - (iii)'s "`p_analyze` refuses unless the p file at root matches p's committed sha (p's own V1)" appears only as register entry (3)'s "verified against this document's committed sha at every run". It is tied to the Clock, with no refusal wording.
     - §4.4's last sentence ("if every checkpoint fails G-CAL-p, no p analyzer is built … §5.2 does not arise") is v0.1's. ans2 does not address it, and it does not contradict (ii).
159. Q3 → §4.2 (placement), §4.3 ((a)), §3.1 ((b), gcal.py:386–387) and §1.2/§3.2 ((c)). **CONFIRMED**.

### Observed, not counted
- `valence_core/p/` exists, untracked, in the working tree: `__init__.py`, `corrupt.py`, `gcal.py`, `guard.py`, `keys.py`, `proxy.py`, `register.py`, with mtimes 13:42–13:51 local on 2026-11-07. That is package code ahead of §8 step 3's commit. I did not read or check it.
- No FAIL was found. None of the thirteen IMPRECISE items changes a figure, a bar, a render, a key or a rule. Items 85 (§5.4's date) and 43 (no date item in the 11-07 routing block) bear on what step 3 writes.
