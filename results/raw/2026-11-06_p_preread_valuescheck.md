# PROPOSAL-p v0.1 pre-read: blind values-check of the STOP block, the entry, the renders raw and the referent check's dispositions (Code's raw, 2026-11-06)

*A blind values-check agent (fresh context, read-only) checked four of Code's drafts against their sources at HEAD `0f35954`: the STOP block (`results/raw/2026-11-06_p_code-to-design_preread.md`, as drafted), the RESULTS.md entry, the renders raw's header, and the referent check's dispositions. Its report follows verbatim, local paths scrubbed (`<tmp>` = Code's session scratch). Code's dispositions follow it, each item re-checked at source.*

## 1. The report (verbatim)

84 items: 58 CONFIRMED, 19 IMPRECISE, 2 FAIL, 5 NOT CHECKABLE

I checked against HEAD `0f35954`, which did not move from start to end. p's sha256 is `1821a235…9953` and p is untracked. My probes are in <tmp>/vc_p/. Re-running renders_p.py at HEAD reproduced renders_p_out.txt byte for byte. I computed the closures with `m_analyze.closure()`. I changed nothing in the repository.

## 1. stop_draft.md (51 items)
1. CONFIRMED. Header anchors: p is untracked at `1821a235…9953`; ans is `4c3f57d4…bf82`, added at `0f35954`; m is `42ab36ec…6c6b`; no *.py file changed between `e0b4f2c` and `0f35954`.
2. CONFIRMED. The PI block's text is identical, with its lines joined, to RESULTS.md@0f35954:31–33.
3. NOT CHECKABLE. "relayed by the coordinating session (in its message, not a file)". The same block is committed at RESULTS.md@0f35954:31–33, and citing it would make the quote checkable.
4. CONFIRMED. §0: G-ANL-F3 BUILD is at `e0b4f2c`, so p:88 (a)'s condition is false. "declared riding item of G-ANL-F3's round" is verbatim at ans:25.
5. CONFIRMED. No LOCK-m-F3-*, LOCK-m-OLMo-*, LOCK-p-* or LOCK-n-* file exists at HEAD or in the tree. Only LOCK-g, LOCK-h and LOCK-m-F0 exist.
6. CONFIRMED. §0 and §3: the three NOT-RUN outputs record analyzer_sha256 `6ec3222b…93d9`, which is e0b4f2c's blob and HEAD's. That is not LOCK-m-F0.md:147's `655e0f7f…c16f`. p:122 and ans:9 name the command, not a blob.
7. CONFIRMED. §1 method:
   - `corrupt_m` looks up `_eligible_m` as a module global (corr.py:221), so the swap takes effect.
   - The per-slot draw is at :233, the formula at :236, and the roster skip at :239–242 over `ROSTERS_OF_RECORD` (:135, both rosters).
   - `_k_m` is called at :223.
8. CONFIRMED. §1 environment: the venv has numpy 2.5.1; the known-answer check is True; the pool pin is at corr.py:80. The seat's 2.2.6 rests only on p:31.
9. CONFIRMED. §1 result:
   - The renders, frame words and n (m→p) match p:35–50 cell for cell.
   - k = 3 on all sixteen items, sum 48. m's sum is 54, the model-free k_sum.
   - Zero skips.
   - The roster check is case-insensitive (corr.py:108 asserts lowercase roster words).
   - k ≤ ⌊n/2⌋ holds, and the renders equal to m's are items [0, 12].
10. CONFIRMED. The json.dumps sha256 is `1551c19997dc4541` (full …5722), equal to p:52.
11. IMPRECISE. §1's "(corr.renders_sha, … the form the G-CAL artifacts record) … as the … artifacts' renders_sha256 has it", and Q3 (c)'s "record renders_sha256 by corr.renders_sha".
   - The prefixes are right.
   - The artifacts' identity.renders_sha256 is the full 64-hex sha256 of the newline-joined renders (gcal.py:796). corr.renders_sha is only its first 16 hex (asserted at gcal.py:390).
   - Fix: "the newline-joined form whose full sha256 the G-CAL artifacts record as renders_sha256 (corr.renders_sha = its first 16 hex): p's 6baf494960da4589, m's a04f67b0e5105a05 (the artifacts' a04f67b0…4372)".
   - p's full digest is 6baf494960da45896206f7eaadbc6b158642a42e09e1d11f70812959e3673c4c.
12. CONFIRMED. §1 other [S] figures:
   - The k vectors at .15 and .10.
   - n = 19, 10, 14, 14 at items 2, 9, 11, 15, the four items at ≤ 2/4 on every checkpoint.
   - Clean counts 62/61/59 and bars 47/46/45 (⌈44.8⌉ = 45; 46.5, 45.75, 44.25).
13. CONFIRMED. The description of the renders file's contents. The 6baf… prefix is in its header only.
14. IMPRECISE. The Q0 heading quotes p:84 as "Imported unchanged, never by copy". p:84 reads "imported unchanged by import, never by copy". Fix: quote it whole, or "imported unchanged … never by copy".
15. IMPRECISE. Q0's "need m's code to run with one m module attribute changed". The analyzer site needs at least two (Q1: the Clock and the pin; see also item 24). Fix: "with named attributes of an m module changed".
16. CONFIRMED. Q0: `_eligible_m` is module-level, and the replacement expression is inline in `corrupt_m` (corr.py:236). "Only two ways" is Code's argument.
17. IMPRECISE. Q0 and Q4 cite "keys.py:95–154", but :95 is blank. item_key starts at :96, arm_key at :112, sched_key at :142, and gate_sched_key runs :148–154. Fix: ":96–154". The `m-…` literals and Q4's key forms are right and match A-m1:26.
18. CONFIRMED. The pin:
   - `PROPOSAL_SHA256` (:98) is refused at V1 of `run_verdicts` (:2257) and of the Q-F3 reader (:4120).
   - In `run_not_run` it is refused through `analyzer_binding` (:2540, PIN-42). That step is not labelled V1, and both postings use it too.
   - The pin is written into every output.
   - `clock_of_record` returns D_O′ 2026-11-30 (:139, :548).
19. CONFIRMED. corr is among mf3's eleven hashed files (`guard.M_HASHED`). data/m/schedules holds 18 OLMo files plus the manifest.
20. CONFIRMED. The A3 quote is verbatim (G-ANL-F3 answers :16, `54bbfe5`), and so is the p:88 quote. Neither rule bars an in-place round today.
21. CONFIRMED. `UNITS` is at :162. `record_problems` asserts the template against `keys.templates` (:801). D_p is 2026-12-15 (p:98).
22. CONFIRMED. `run_posting_v2` cross-checks Q-F0 and the three OLMo coordinates against one verdicts_dir (:4377–4378, `crosscheck_coordinate(…, v2=True)`). The docstring at :2661 names it PIN-23.
23. IMPRECISE. Q1's "the committed analyzer, as committed, cannot post p's states in the OLMo positions".
   - This holds for the declared roots: in data/m/verdicts, PIN-23 meets m's NOT-RUN outputs and refuses.
   - But `crosscheck_coordinate` (:2660–2691) reads only file presence, state and reason, never provenance or commit state.
   - A --verdicts-dir assembled with Q-F0's outputs beside p's would pass, since the file names are the same under Q4 (ii).
   - Fix: "cannot post p's states from the declared roots (only a directory assembled to hold Q-F0's and p's outputs together would pass PIN-23, and no rule declares one)".
24. IMPRECISE. Q1's "The data roots are not fixed: verdicts and not-run take --campaign, --time, --qual and --out".
   - `not-run` takes `--campaign` only with `--v2-closure`.
   - `--campaign none` checks the fixed path data/m/ckpt/{U}_campaign.json (:2583; ckpt_dir is not a CLI option).
   - With m's unit strings (Q4 (ii)), a p unit's "none" would be checked against m's root, not data/p/ckpt.
   - Fix: add "except the v2 closure's --campaign none check, which reads data/m/ckpt (m_analyze.py:2583)".
25. CONFIRMED. The referents of Q1 (b), (a′) and (c): p:88 (b), the p:96 quote, p:82, and data/p/verdicts (p:84). LOCK-m-F3 v0.1 names the analyzer blob (m:292; A-m1:44).
26. IMPRECISE. Q1 (a′)'s "the analyzer's third blob". m_analyze.py has nine committed blobs. Lock-bound ones already include 66fb5214… (LOCK-m-F0 v0.1, LOCK-m-F0.md:83) and 655e0f7f… (v1.0), and 6ec3222b… is G-ANL-F3's. Fix: "a further analyzer blob (after 655e0f7f… and 6ec3222b…)".
27. FAIL. Q1 (iv)'s "m:349's 519,480-tuple space". m:349 is §7.5's posting rule and gives no count. The 519,480 count is at m:291 (also m:73 and A-m1:60). Fix: "m:291's 519,480-tuple space". The p:96 and p:94 quotes are CONFIRMED.
28. CONFIRMED. Q2: no lock or licence names olmo_hf.py. No LOCK-*.md mentions it, `M_HASHED` does not list it, and neither do gshape's SCORING_STACK_FILES or TOOLING_FILES (PIN-S10's map).
29. CONFIRMED. The closures: base has 15 modules (`a3bc7bb9…`), Q-F3 has 22 (`d19f336d…f039`). Both include adapters/__init__.py and base.py; neither includes olmo_hf.py.
30. CONFIRMED. `backend_identifier` (resume.py:239–245) hashes provenance minus n_encodes_clipped, path and seed. `provenance()` (olmo_hf.py:311–336) holds no source hash. `641ee466f4553b6a` appears in all three G-CAL artifacts.
31. CONFIRMED. n:159 says "unchanged" and puts the 5(f) primitive in n's own package. valence_core/n does not exist.
32. CONFIRMED. Seeding and the runner:
   - `manual_seed` is at olmo_hf.py:220–221, and the runner passes each round's seed at :137 and :164.
   - The `add_round` fields are at scaffold.py:385–392, and g.text goes into the transcript.
   - `assert_olmo_adapter` (:63–78) checks only path and choice_window; no m module type-checks the adapter.
33. IMPRECISE. Q2 quotes "n's build takes the edited file before LOCK-n v0.1". p:64 reads "PROPOSAL-n's build, which imports it unchanged (n:§8 step 6), takes the edited file before LOCK-n v0.1". Fix: "PROPOSAL-n's build … takes the edited file before LOCK-n v0.1".
34. CONFIRMED. `STOP_CAP = 60` is at session_e2a.py:90. 2 of 384 stored texts hold a line break: DPO and instruct, corrupted item 15, seed 0.
35. CONFIRMED. Q2 (a) and (b):
   - The p:64 and p:72 quotes are verbatim.
   - `_is_stop` (:290–294) needs content_seen; `.strip()` is at :286.
   - The loop breaks before appending the stop token at :251–254 and :274–277.
   - No clean text holds a line break, and the records carry no token ids.
36. CONFIRMED. Q3: m's package_sha256 is `60199b36…feec`. PIN-V2-12 (:4131–4134) requires the lock to name m's package_sha256. mf3_sessions.py:177 asserts the hash prefix; it is a self-test check, which also asserts 18 files.
37. CONFIRMED. A module in valence_core/p moves none of m's package, `M_HASHED`, mf3's package (`f30ad505…6310`) or either closure.
38. IMPRECISE. Q3 (b) cites "gcal.py:386" for the quoted message. The check is at :386, but the message is at :387, inside `_renders_of_record`. Fix: "gcal.py:386–387".
39. CONFIRMED. Q4:
   - schedule.py's schema, manifest schema and default root are at :66–69, and it draws through keys at :230, :244 and :504–505.
   - mf3/schedule.py imports balance_report, cells_sha256, dumps_schedule, GATE_TABLE and the schema names.
40. CONFIRMED. Q4 (i) and (ii): the p:82 quote, and p:72's seeds. With only arm_key changed, the cells (sched_key) and item orders (item_key) stay m's.
41. IMPRECISE. §3's "G-ACQ (n) is complete (e7e070f, PASS)".
   - `e7e070f` says "PASS on every part run; the BACKEND extension's 24 fresh-versus-cached reads are not run and wait for the n package (GA-5)".
   - n:109 puts that extension inside G-ACQ.
   - Fix: "G-ACQ (n) is committed (e7e070f), PASS on every part run; its BACKEND extension waits for the n package (GA-5)".
42. CONFIRMED. No G-ANL-F3.json exists at HEAD or in the tree.
43. NOT CHECKABLE. §3 and §5: "waits for the coordinating session's word".
44. CONFIRMED. The tallies 107 = 85/17/3/2 (H1–H9 plus items 1–98, counted).
45. CONFIRMED. FAIL 1, corrupted item 2:
   - DPO and instruct say "The thirteenth month…" at seeds 1–3.
   - Both refuse at seed 0 ("I'm sorry, but I can't assist…").
   - SFT answers 'maanum'…, February, 'Tishri' and 'Narlei'.
46. CONFIRMED. FAIL 2: m:176 says "against v1.7's rule"; v1_7.md:59 (§2.3) has "fixed at rate 0.15."; v1_8.md:137 adds ", operand excluded"; ans:15 has "(v1.7)".
47. CONFIRMED. FAIL 3: n:16 is "0.4 Welfare and exposure", and n quotes no slope. A-m1:32 quotes 0.037 (rounded) and A-m1:67 quotes 0.0366.
48. CONFIRMED. Planning item 1:
   - The m:205 quote is verbatim.
   - m:214's 3.4/3.9/4.5 h already include the 26 gate sessions (recomputed).
   - The smoke raw's three loads are 211.6 + 175.7 + 183.3 s ≈ 9.5 min.
   - Note: m:205 says its amortized basis already carries a load and over-counts it at SFT/DPO, so "about 10 min" is an upper estimate.
49. IMPRECISE. Planning item 2 says "misreads two of §1.2's own renders" but then names three: items 7, 8 and 3. Fix: "three".
50. CONFIRMED. The other IMPRECISE wordings all match their sources: items 8, 10, 11, 15, 18, 20, 40, 43, 46, 58, 71, 73, 78, 89 and 96.
51. IMPRECISE. "Code re-checked … each was confirmed. None changes a question above except item 52."
   - Item 38 cannot be confirmed: the renders reproduce on numpy 2.5.1, but the seat's version is still unknown.
   - Item 40 underlies Q0, and the STOP itself tags it "(Q0)".
   - Fix: "…each finding held (item 38 stays not checkable). None changes a question except item 52 (Q2 (b)); item 40 also underlies Q0."

## 2. entry_preread.md (13 items)
52. CONFIRMED. The title and summary. Note that Q3 is a call made explicit rather than a question.
53. CONFIRMED. The PI block equals RESULTS.md@0f35954:31–33, whitespace aside.
54. NOT CHECKABLE. The relay "(in its message, not a file)".
55. CONFIRMED. The sha256s of p and the seat's answers, and "cited at 0f35954".
56. CONFIRMED. The renders bullets: 1551c19997dc4541; k = 3 with sum 48; zero skips; items 0 and 12; the file per p:54; 6baf494960da4589.
57. IMPRECISE. The entry quotes p:84 as "imported unchanged, never by copy" (same issue as item 14). Fix: "imported unchanged by import, never by copy".
58. CONFIRMED. Route (a) is gone, and posting v2 reads the four v1 coordinates from one --verdicts-dir.
59. IMPRECISE. "so as committed it cannot post p's states" (same issue as item 23). Fix: "so, from the declared roots, it cannot post …".
60. CONFIRMED. No lock, licence or analyzer closure names olmo_hf.py, and the backend identifier hashes no source.
61. IMPRECISE. "decides whether G-CAL-p's clean pool can reproduce G-CAL-OLMo's byte for byte". Under the literal reading it may still reproduce; the STOP's own words are "could fail". Fix: "decides whether the clean-pool identity holds by construction or can fail on a stop token's content alone".
62. CONFIRMED. The Q3 and Q4 summaries (facts as in items 36–40).
63. CONFIRMED. The referent-check tallies, the three FAIL relays, item 52, and §6.1 against m:214.
64. NOT CHECKABLE. "Q-F3's lock chain waits for the coordinating session's word".

## 3. renders_raw.txt header (7 items)
65. CONFIRMED. p is untracked at the full sha256.
66. CONFIRMED. The method paragraph: corr.py:236, the rosters, the pool pin, and the CASE-SENSITIVE flag, which never fires.
67. CONFIRMED. numpy 2.5.1, and the known-answer check is the first output line.
68. CONFIRMED. "HEAD e0b4f2c; valence_core/m unchanged since 71cc23c (60199b36…feec)". The output was written at 23:50, before 0f35954 (00:11:57), and 0f35954 touched no file the probe reads.
69. CONFIRMED. The result line: 1551c19997dc4541, 6baf494960da4589, a04f67b0e5105a05.
70. IMPRECISE. "Command, from the repository root: …/python -B renders_p.py". The script is not in the repository, so that command fails at the root. Fix: "<repo>/jlens-qwen36/.venv/bin/python -B <path>/renders_p.py (the script below), run with the repository root as the working directory".
71. CONFIRMED. The output and script sections are byte-identical to renders_p_out.txt and renders_p.py.

## 4. refcheck_head.md and refcheck_dispositions.md (13 items)
72. CONFIRMED. The head's p sha256 and untracked status.
73. CONFIRMED. HEAD moved from e0b4f2c to 0f35954 during the agent's check (report line 3 and the commit times agree).
74. IMPRECISE. The head says "that commit changed no code, artifact or design document". 0f35954 added m's three NOT-RUN records and outputs, 89 lines of RESULTS.md and two raws, and committed the seat's answers raw as placed. Fix, in the agent's own words: "…added m's three NOT-RUN records and outputs and committed the seat's answers raw with its sha unchanged; it touched no code file, gate artifact, m, A-m1, n or p."
75. FAIL. The head says "local paths scrubbed", but refcheck_report.md line 3 still carries the full scratch path (<tmp>…<tmp>…/scratchpad/p_refcheck/). Fix: replace it with `<tmp>/p_refcheck/`. No other local path appears in the drafts.
76. NOT CHECKABLE. The agent's process ("blind", "verbatim", "did not recompute the renders"). It is consistent with report items 7, 29 and 34.
77. CONFIRMED. Rows 9, 17 and 21, at source.
78. CONFIRMED. Rows 8, 10, 11, 15 and 20, against the artifacts' records.
79. IMPRECISE. Row 18: "Both artifacts' procedure.prompt is `SESSION_BANNER + …`". The OLMo artifacts' prompt reads "SESSION_BANNER (b3's banner) + 'Task: …'". Fix: "both start with SESSION_BANNER and both record banner_sha256 6124c724…".
80. CONFIRMED. Rows 40, 43, 52 and 96: corr.py:236 and :201; olmo_hf.py :251/:256/:274/:279, :290–294, :251–254 and :274–277.
81. CONFIRMED. Row 46: the CLAUDE.md 28(d) quote is right. "Stop-discipline boundary (rule 13)" is a reading; classifying O5 is the seat's call.
82. CONFIRMED. Rows 57, 58, 71, 73, 78, 85 and 89: m:155/159/172, m:278/291, prebuild.md:35 with answers A1, A-m1:42, m:205, and e7e070f.
83. CONFIRMED. Rows 38 and 92.
84. IMPRECISE. The dispositions header says "each was confirmed … The rest are text corrections for v0.2", but row 40's disposition is "Q0 of the STOP" and row 38 is not a correction. Fix as in item 51.

## 2. Code's dispositions

Code re-checked every item marked FAIL, IMPRECISE or NOT CHECKABLE at source before acting; each finding held. All corrections were applied to the drafts before the commit, as below. The 58 CONFIRMED items need no change.

| Item | Verdict | Re-checked at source | Disposition |
|---|---|---|---|
| 27 | FAIL | `grep -n 519,480` on PROPOSAL-m v1.11 finds lines 16, 62, 73, 94, 141, 291, 361 and 370, not 349. | Applied: "m:291's 519,480-tuple space". |
| 75 | FAIL | The draft `refcheck_report.md` carried the scratch path, because the scrub runs when the raws are assembled. | Applied at assembly: the committed raw reads `<tmp>/p_refcheck/` (checked after assembly). |
| 11 | IMPRECISE | `gcal.py:796` records the full sha256 of the newline-joined renders; `:388–390` asserts its first 16 hex equal `corr.renders_sha`. p's full digest is `6baf4949…3c4c` (recomputed). | Applied in §1 and Q3 (c). |
| 14, 57 | IMPRECISE | p:84: "m's modules imported unchanged by import, never by copy". | Applied: quoted whole in the STOP's Q0 heading and in the entry. |
| 15 | IMPRECISE | The analyzer site replaces the pin and the Clock. | Applied: "named attributes of an m module". |
| 17 | IMPRECISE | `keys.py:95` is blank; `item_key` starts at :96. | Applied: `keys.py:96–154`, both places. |
| 23, 59 | IMPRECISE | `crosscheck_coordinate` (`m_analyze.py:2660–2691`) reads only presence, state and reason. | Applied: "from the declared roots", with the assembled-directory caveat in the STOP; "from the declared roots" in the entry. |
| 24 | IMPRECISE | `not-run` takes `--campaign` only with `--v2-closure`; the `none` check reads `REPO / CKPT_REL` unless `ckpt_dir` is passed in-process (not a CLI option). | Applied in Q1. |
| 26 | IMPRECISE | LOCK-m-F0.md:83 names `66fb5214…` (v0.1); `655e0f7f…` is v1.0's; `6ec3222b…` is G-ANL-F3's. | Applied: "a further analyzer blob (after `655e0f7f…` and `6ec3222b…`)". |
| 33 | IMPRECISE | p:64: "PROPOSAL-n's build, which imports it unchanged (n:§8 step 6), takes the edited file before LOCK-n v0.1". | Applied: quoted with an ellipsis. |
| 38 | IMPRECISE | `gcal.py:386` is the check and `:387` the message. | Applied: `gcal.py:386–387`. |
| 41 | IMPRECISE | `e7e070f`'s message: "PASS on every part run; the BACKEND extension's 24 fresh-versus-cached reads are not run and wait for the n package (GA-5)". | Applied in §3, §4 and the referent dispositions (row 89). |
| 49 | IMPRECISE | The sentence names items 7, 8 and 3. | Applied: "three". |
| 51, 84 | IMPRECISE | Item 38 is not checkable; item 40 underlies Q0. | Applied in the STOP's §4 and the referent dispositions' header. |
| 61 | IMPRECISE | The STOP's Q2 (b) says the identity "could fail". | Applied in the entry. |
| 70 | IMPRECISE | The probe script is not in the repository. | Applied: the command names the script's scratch path (scrubbed), run with the repository root as the working directory. |
| 74 | IMPRECISE | `git show --stat 0f35954`: RESULTS.md, m's three NOT-RUN records and outputs, two raws, and the seat's answers raw. | Applied in the referent check's head. |
| 79 | IMPRECISE | The OLMo artifact's prompt reads "SESSION_BANNER (b3's banner) + …"; both artifacts record `banner_sha256` `6124c724…`. | Applied (row 18). |
| 48 (note) | — | m:205's amortized basis already carries a load. | Applied: "at most about 10 min". |
| 3, 54 | NOT CHECKABLE | RESULTS.md@0f35954:31–33 quotes the same block. | Applied: both drafts now also cite the committed copy. |
| 43, 64 | NOT CHECKABLE | Plan statements. | No change. |
| 76 | NOT CHECKABLE | The agent's process. | No change. |
