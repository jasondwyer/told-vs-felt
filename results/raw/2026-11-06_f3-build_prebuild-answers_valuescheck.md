# m package — BUILD (F3): blind values-check of the STOP's close and of Code's referent check of the seat's answers (2026-11-06)

*Code's raw. One blind refuter (a general-purpose agent with no access to Code's reasoning) checked the close sub-bullet appended to the F3 pre-build STOP entry in RESULTS.md and `results/raw/2026-11-06_f3-build_prebuild-answers_referent-check.md`, both as drafted at HEAD `9cbacdb` plus the uncommitted drafts, against their sources, read-only. Result: 97 items, 2 FAIL, 10 IMPRECISE, the rest CONFIRMED. Code re-checked every FAIL and IMPRECISE item at its source before applying it (§2). The report is reproduced verbatim except that local absolute paths are replaced (the repository's absolute prefix dropped, leaving repo-relative paths; the session scratch shown as `<scratch>/`), since the origin is public. Line numbers in the report are working-tree lines of the drafts as checked; the drafts have since been edited by the dispositions.*

## 1. The report (verbatim, paths replaced as stated)

97 items checked (several bundle sub-claims): 2 FAIL, 10 IMPRECISE, the rest CONFIRMED. Line numbers are working-tree lines unless stated; "answers" = `results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md`, "prebuild" = `..._code-to-design_prebuild.md`, "v0_2"/"v0_1" = the PROPOSAL-n files, "valuescheck" = `results/raw/2026-11-06_f3-build_prebuild_valuescheck.md`. Nothing in the repository was edited.

**A. The close (RESULTS.md:55–105)**

A1. Answers committed by path in the commit that adds the close, as their first commit, so `git log --diff-filter=A` names it (:55–57). CONFIRMED as far as it can be checked now: the file is untracked (`??`), and `git log --diff-filter=A -- <path>` prints nothing.
A2. The link target exists (:58). CONFIRMED.
A3. sha256 `aec58440…4df3` "as routed" (:58–59). CONFIRMED by `shasum -a 256`. It equals the routing (:70) and the referent check's header (:3).
A4. "Its PROPOSAL-n lines are the record of PROPOSAL-n v0.2's §0.9 decisions; that document's commit entry quotes them again" (:61–62). IMPRECISE (minor). v0_2:38 says "the routing block is their record", and decision (1), the date, is in the header line (:64), not the PROPOSAL-n lines (:72–73). The commit-entry quote is what v0_2:158 (§8 step 3) requires.
A5. Routing: v0.2's sha256 is `30a3d0f5…04f4` (:68). CONFIRMED by shasum.
A6. Routing: the answers' sha256 (:70). CONFIRMED.
A7. Routing: both files are "untracked" (:66). CONFIRMED (both show `??`).
A8. Routing: "supersedes v0.1; v0.1 to archive/ at step 3" (:68). CONFIRMED (v0_2:2, v0_2:158).
A9. Routing: the A1, A2 and Route A slots (:72–73). CONSISTENT with v0_2:38 §0.9 (2)–(4); §0.7 (v0_2:34) is the rule-13 departure.
A10. Routing: the Q7 line (:74–75). CONSISTENT with answers:46.
A11. Routing: "the e9b5022 precedent" (:78). The commit exists (PROPOSAL-k v1.1 COMMITTED).
A12. Q1: (C2), `valence_core/mf3/`, new driver `scripts/mf3_sessions.py` (:81–82). CONFIRMED (answers:9, :12, :13).
A13. Q1: the licence is mf3's own package hash plus the file sha256 of each imported `valence_core.m` module (:82–83). CONFIRMED (answers:14 (a), (b)).
A14. Q1: it imports neither `stages` nor `gshape` (:83). CONFIRMED (answers:12).
A15. Q1: at VERDICTS, PIN-14 still binds the whole `valence_core.m` hash (:83–84). CONFIRMED (answers:14).
A16. §0/Q2: the OLMo track's first node is its own build (G-CAL-OLMo and the stage wiring) in `valence_core/m` and `m_sessions.py`, before any LOCK-m-OLMo v0.1 (:85–86). CONFIRMED (answers:7, :19).
A17. "On both tracks, builds land before locks" (:86–87). CONFIRMED (answers:17, heading).
A18. Q3: G-ANL-F3 extends the analyzer in place and lands only while no OLMo unit is open, either (a) before any OLMo LOCK v0.1 or (b) after the OLMo VERDICTS (:88–89). CONFIRMED (answers:25–26).
A19. Q3: the BUILD entry records which order obtains (:89). CONFIRMED (answers:26).
A20. Q3: the riding texts are listed by anchor for the seat to confirm before LOCK-m-F3 v0.1 (:89–90). CONFIRMED (answers:27). The close leaves out the seat's recommendation of (b) if the pod comes up first (answers:26); that is an omission, not an error.
A21. Q4: Code's proposal adopted; the three strings become a rule-23 descriptive counter (:91). CONFIRMED (answers:29–31).
A22. Q5: "the cap trigger counts the lines of all six sessions" (:92). IMPRECISE (minor). answers:35 says it "counts cap-reach over all six G-TIME-F3 sessions' reasoning lines (≤ 36)".
A23. Q5: contrast sessions report forced rounds and per-line cap booleans, with no free-round text and no pick (:92–93). CONFIRMED (answers:36). The adoption of #10 (answers:37) is omitted.
A24. Q6: "'the next unit' is the OLMo wiring build" (:94). IMPRECISE.
- answers:42 scopes this "for a driver edit".
- It also says `scripts/mf3_sessions.py` uses the same forms from the start.
- And the weights-snapshot binding goes into each unit's identity at its own build: mf3's at the F3 build, the OLMo identity's at the wiring build.
A25. Q7 is the PI's, confirmed above (:94). CONFIRMED (answers:44–46; routing :74–75).
A26. "Q8 rules seven readings, and the other twenty-four stay Code's PINs" (:95). The count is CONFIRMED (answers:50 "the seven items", :58 "The other twenty-four readings"; prebuild:178 "Thirty-one"). The wording is IMPRECISE (minor):
- The answers count "items", and valuescheck:487–489 (I13) shows the "\n\n" item is the build hazard, not a reading.
- answers:58 also leaves "the declared check for the build hazard" as Code's PIN, which the close omits.
A27. The referent check is linked, finds no unresolved item, and makes five notes (:96–98). CONFIRMED.
A28. N1: `corrupt_m` "is a function of `corr`", and `readout` is outside the package (:99). CONFIRMED (corr.py:212; valence_core/readout.py). Wording nit: "a function in `corr`" is what is meant.
A29. N2 (:100). CONFIRMED (m:281).
A30. N3 and its quote "as Q-F0 ran them" (:101). CONFIRMED (answers:54, verbatim).
A31. N4 (:102). CONFIRMED (m:258).
A32. N5 (:103). CONFIRMED as a summary of referent-check:35.
A33. "What follows": the OLMo build, then the F3 build, then G-SHAPE-F3, then PROPOSAL-n §8 (:104). IMPRECISE (minor).
- It drops G-ANL-F3, which referent-check:42 and answers:63 carry ("G-SHAPE-F3 → G-ANL-F3 under Q3's rule → the lock chain").
- The serial order is Code's choice: answers:20 says the F3 build "runs in parallel", and answers:62 lists it first.
A34. "Nothing in this close moves a hash, edits a package file, or starts a pod" (:105). CONFIRMED. Only RESULTS.md and results/raw files change; none is a package `*.py`, the analyzer, or an entry in the gshape.py:92–105 maps.

**B. The referent check (results/raw/2026-11-06_f3-build_prebuild-answers_referent-check.md)**

B1. Header: the answers' sha256 "as routed", and HEAD `9cbacdb`. CONFIRMED.
B2. m:N is v1.11 with sha256 `42ab36ec…6c6b`. CONFIRMED.
B3. A-m1 is at root at `f26bc59`. CONFIRMED: last commit touching it, file clean, sha256 `ea08322d…9001`.
B4. No unresolved item; five residues as dated notes (the routing's process line and e9b5022). CONFIRMED (routing :77–78).
B5. "Nothing here changes a ruling." CONFIRMED, with a note: N3 picks the ruling's operative words over its gloss, and N4 reads away a double count. Both are declared PINs the seat can strike (answers:50).
B6. "build-complete" at A-m1:10 (§0.1), :16 (§0.4) and :52 (§3 item 5). CONFIRMED.
B7. The gcal.py:39–40 quote. CONFIRMED verbatim.
B8. m_sessions.py:491–492 (the OLMo units keep the step-9 refusal). CONFIRMED.
B9. Ledger (55) is in v0.2 §0.3. CONFIRMED (v0_2:14).
B10. m:174 (F2 block order, reasoning block). CONFIRMED.
B11. The m:159 quote. CONFIRMED verbatim.
B12. m:265 (the line classes). CONFIRMED.
B13. m:267 (the resume identity, which includes "cap"). CONFIRMED.
B14. keys.py:66–67, "Q-F3 keys are built at step 19 (decision (10)); not at step 4". CONFIRMED.
B15. guard.py:160–162: `_substrate` calls `keys.templates`, which goes through `_unit_parts` (keys.py:71–73) and raises for Q-F3. CONFIRMED.
B16. resume.py:296–328: a non-recursive `glob("*.py")`, with `package_sha256` at :321–328. CONFIRMED.
B17. stages.py:530–608 is `licence_problems` (:530 def to :608 `return probs`). CONFIRMED.
B18. m_analyze.py:1921, the `keys.UNITS_BUILT` check. CONFIRMED.
B19. At module load, `keys` and `audit` import no m module (keys imports numpy only; audit.py:52–55 imports e2d.* and session). CONFIRMED.
B20. `schedule`, `bars`, `corr` and `banner` import `keys` (schedule.py:61, bars.py:56, corr.py:73, banner.py:30). CONFIRMED.
B21. stages.py:135–136 imports both runners; gshape.py:51 and :54 import gcal and runner_olmo. CONFIRMED.
B22. "The lazy imports … reach only banner, audit, session_e2a, session and stats" (:9). The eight cited sites are CONFIRMED, but "only" is IMPRECISE. Two lazy imports are missing:
- bars.py:1218, `__import__("valence_core.e2d.config")`, inside `_selftest`;
- audit.py:636–652, `_load_b3`, which executes scripts/box_b3_sessions.py; that file imports adapters.base, readout, session and session_e2a, and `_load_b3` is called from audit's `_selftest` at :719.
Neither reaches a valence_core.m module, so the conclusion stands.
B23. [C] import check (:10). CONFIRMED: I reproduced it (jlens venv, `-I -B`). Loaded from the package: exactly valence_core.m, audit, banner, bars, corr, keys and schedule; none of stages, gshape, gcal or either runner.
B24. The PIN-S10 quote at gshape.py:233–236. CONFIRMED verbatim.
B25. SCORING_STACK_FILES at :92–104 with 26 entries (I counted 26), and TOOLING_FILES at :105. CONFIRMED.
B26. The docstring quote "No model, no tokenizer, no generation" (gshape.py:30). CONFIRMED.
B27. Write-once, and the PIN-S9 quote at :1508–1517. CONFIRMED.
B28. The step-10 read's Q2 quote at :45, with its ellipsis. CONFIRMED.
B29. RESULTS.md@9cbacdb:2604 (the record continues to :2605). CONFIRMED.
B30. The m:291 and m:292 quotes, and the remark on the answers' "(m:292)". CONFIRMED: answers:25 attaches it to "in place", while prebuild:127–128 attached it to the lock naming the blob.
B31. A-m1:44 is §2.5, with its ending sentence. CONFIRMED.
B32. The m:261 scaffold-set quote. CONFIRMED.
B33. The m:174 and m:293 quotes agree. CONFIRMED.
B34. The m:271 quotes. CONFIRMED.
B35. The m:265 quote "The reasoning line is not a round". CONFIRMED.
B36. The inference that a cap boolean is not a free-round event. CONFIRMED as a reading from m:265. The seat's own ground is different ("content, not counts", answers:36).
B37. m:263. CONFIRMED.
B38. Step-3 notes #10, #87, #116 and #130 read as the prebuild block quoted them (step3_notes.md:20, :97, :126, :140 against prebuild:154–157). CONFIRMED.
B39. The prebuild block was values-checked twice (prebuild:14–16). CONFIRMED.
B40. m:73, m:298 and m:302 with their quotes. CONFIRMED.
B41. The m:258 and m:261 echo-class quotes. CONFIRMED.
B42. m:265, m:314, rule 28(d) standing form (a) (CLAUDE.md:402–403), and m:361. CONFIRMED. Note: the answers' "by character offset" (:56) comes from 28(d)'s class sentence (CLAUDE.md:397–399), not from form (a), which says "asserted equal to the prefix token count".
B43. N1: `corrupt_m` is corr.py's corruptor (m:176, corr.py:212), and readout is outside valence_core.m. CONFIRMED.
B44. N1: the licence (b) quote, which does not list readout (answers:14). CONFIRMED.
B45. N1: m's stage licence does not bind readout. CONFIRMED: `licence_problems` checks HEAD, the proposal, the lock, the analyzer and the package only, and stages.py contains no "readout" or "closure".
B46. N1: PIN-14's closure binds readout at VERDICTS. CONFIRMED.
- LAZY_VERDICT_MODULES is `stages` (m_analyze.py:99).
- stages.py:130 imports guard, and guard.py:72 imports readout.
- data/m/gates/G-ANL-F0.json's closure.modules lists valence_core/readout.py.
B47. N2: the m:281, m:294 and m:295 quotes. CONFIRMED.
B48. N3: the answers' parenthetical, quoted (answers:54). CONFIRMED.
B49. N3: the property axis is the CORR property; the m:314 quote; m_analyze.py:797 and :948–950 (PIN-12); corr.py:86. CONFIRMED.
B50. N3: "The content-class counters carry a separate `category` key (`m_analyze.py:806`)" (:27). FAIL.
- :805–806 is the key tuple of `audit_degenerate (v2)`.
- The content-class counters key on `class`: content_exclusion (v3/v4) at :808–809 and content_advisory (v5) at :810–812.
- The point being made (a classification key separate from `property`) still holds.
B51. N3: the operative-words quote, and m:314's "reasoning-line defects by class [Q-F3]" with no property key (m_analyze.py:823–825 declares keys `()`). CONFIRMED.
B52. N4: m:258's eight strings include the two reasoning-block lines; the ruling's quote (answers:51); `[round {n} | reasoning]` (m:174); the m:265 quote. CONFIRMED.
B53. N5: the quoted clearance "with no change under `valence_core/m` (an edit there moves the package and is outside this answer)" (:33). FAIL: the quote is not verbatim. At G-TIME-F0_read.md:45, "with no change under `valence_core/m`," is in the ground sentence, and the parenthetical follows "Conditions, …: no change under `valence_core/m`". The substance is right.
B54. N5: the OLMo build edits valence_core/m (answers:19). CONFIRMED.
B55. N5: "driver edits that wire no subcommand: … and the listing commands" (:34). IMPRECISE (minor).
- The O2-3 listing commands belong to "the next unit's README" and its "checklist" (VERDICTS_read.md:86; prebuild:168), not to driver code. The other items are driver edits (step17.md:86; prebuild:164–166).
- N5 also leaves out the step-14 read (G-F0m-Qwen_read.md:42). That read extended the clearance to print-path edits that wire no subcommand and change nothing under `valence_core/m`, which would cover the CHECKPOINT STATE INCONSISTENT redaction. Its condition fails here too, so the conclusion stands.
B56. N5: Code's reading of Q2 (answers:19), and supersession under PIN-S9 (gshape.py:1515–1517). CONFIRMED.
B57. §3 item 1: the OLMo build goes first, with its scope, Q6's carry-overs and the snapshot binding, and its LOCK v1.0s are due by D_O′ = 2026-11-30 (answers:19, :42; A-m1:28 §1.3 under decision (16); f26bc59). CONFIRMED.
B58. §3 item 2: the F3 build's paths and its build-design raw (answers:12–13, :50). CONFIRMED.
B59. §3 item 2: "Both builds land before any new lock (Q2)" (:41). IMPRECISE (minor).
- answers:19–20 require two things: the OLMo build before LOCK-m-OLMo-{ckpt} v0.1, and any shared-module OLMo edit before LOCK-m-F3 v0.1.
- They say the F3 build "runs in parallel", so putting it before the OLMo locks is Code's order, not Q2's.
B60. §3 item 3: G-SHAPE-F3, then G-ANL-F3 under Q3's rule, with (a) or (b) recorded (answers:26, :63). CONFIRMED.
B61. §3 item 4: "PROPOSAL-n v0.2 §8 from step 1, as the routing orders it". The routing's words are CONFIRMED (RESULTS.md:77). The placement is IMPRECISE (minor): putting it after G-SHAPE-F3, ahead of answers:63's G-ANL-F3 and lock chain and :64's OLMo track, is Code's own reading of "Run the prebuild answers as written" (answers:65 says "after this block"). The text does not declare it as a reading.
B62. §3 item 4: "decision (6), 2026-11-05" (:43). IMPRECISE (minor). This is v0.1's §0.9 (6) (v0_1:26; RESULTS.md:140, :155). In v0.2 the pod order is (7), and v0.2's (6) is the Clock dates and pod budget (v0_2:38).
B63. "No pod starts without the PI's word; runpod re-authorisation first" (answers:64; routing :78). CONFIRMED.

**FAIL and IMPRECISE: suggested corrections**

1. FAIL B50 (referent check:27): "The content-class counters carry a separate `class` key (`m_analyze.py:808–812`; v2's counter carries `category`, :806)."
2. FAIL B53 (:33): quote the clause exactly. Either "…wires a subcommand, under the condition 'no change under `valence_core/m` (an edit there moves the package and is outside this answer)'", or mark the join with an ellipsis.
3. B22 (:9): after the list, add "plus, in self-tests only, `e2d.config` (bars.py:1218, `__import__`) and box_b3_sessions.py's imports via `_load_b3` (audit.py:636–652, :719): adapters.base, readout, session, session_e2a; no `valence_core.m` module".
4. B55 (:34): drop "the listing commands" from the driver edits, or write "(the listing commands are README and checklist text)". Add that the step-14 read's print-path extension (G-F0m-Qwen_read.md:42) also requires no change under `valence_core/m`.
5. B59 (:41): "Both builds land before any new lock (Code's order; Q2 requires the OLMo build before the OLMo locks, and any shared-module edit before LOCK-m-F3 v0.1)."
6. B61 (:43): declare the placement as Code's reading: after the builds and G-SHAPE-F3, while G-ANL-F3 and the lock chain proceed under Q3.
7. B62 (:43): "(PROPOSAL-n v0.1 §0.9 decision (6), routed 2026-11-05; v0.2 §0.9 (7))".
8. A24 (RESULTS.md:94): "'the next unit' for a driver edit is the OLMo wiring build; `scripts/mf3_sessions.py` uses the same forms from the start, and each unit's identity takes the weights-snapshot binding at its own build."
9. A22 (:92): "the cap trigger counts cap-reach over the reasoning lines of all six sessions (≤ 36)".
10. A33 (:104): "…then G-SHAPE-F3 (G-ANL-F3 under Q3's rule), then PROPOSAL-n v0.2's §8 from step 1". Optionally add "(Code's order; the answers run the builds in parallel)".
11. A26 (:95): "Q8 rules the seven items Code named; the other twenty-four readings, and the build hazard's declared check, stay Code's PINs."
12. A4 (:61): "Its header and PROPOSAL-n lines are the record of …".

**Coverage notes (not errors)**
- The referent check's §1 has no line for answers §6. Its items (O1-3, RM4-1, O4-1, VC4-1, VC4-2, O2-3) do exist, at step17.md:86 and VERDICTS_read.md:86.
- §1 also has no line for:
  - §0's m:205–214 and N9 (RESULTS.md:289);
  - §3's N8 (RESULTS.md:287–288);
  - §2's statement about `posting`;
  - §9.
- The answers rule on the "\n\n" item (:56), which valuescheck I13 identifies as the build hazard, and also leave its "declared check" to Code (:58). The two are compatible, but neither text says so.
- The "empty line" reading (prebuild:180; B1 in Code's scratch map at `<scratch>/f3build/maps/spec.md:379–410`) is not among the seven rulings, so it stays among the twenty-four.

Files:
- RESULTS.md
- results/raw/2026-11-06_f3-build_prebuild-answers_referent-check.md
- results/raw/2026-11-06_f3-build_design-to-code_prebuild-answers.md
- scripts/m_analyze.py
- results/raw/2026-10-13_m-design-to-code_G-TIME-F0_read.md
- results/raw/2026-10-13_m-design-to-code_G-F0m-Qwen_read.md
- results/raw/2026-11-06_f3-build_prebuild_valuescheck.md

## 2. Code's dispositions (each re-checked at source first)

| item | re-check at source | disposition |
|---|---|---|
| B50 (FAIL) | `m_analyze.py:805–812`: v2's `audit_degenerate` keys on `category`; content_exclusion and content_advisory key on `class` | N3 corrected: "`class` key (`m_analyze.py:808–812` …); v2's `audit_degenerate` carries `category` (`:805–806`)" |
| B53 (FAIL) | `…G-TIME-F0_read.md:45`: the ground sentence and the conditions are separate clauses | N5 now quotes the ground sentence and the condition separately, verbatim |
| B22 | `bars.py:1218`; `audit.py:636–652`, `:719` | the two self-test-only lazy imports added; the conclusion unchanged |
| B55 | `…VERDICTS_read.md:86`; `…G-F0m-Qwen_read.md:42` | the listing commands moved out of the driver edits (README and checklist text); the step-14 extension and its condition added |
| B59 | answers:19–20 | §3 item 2 says the before-any-lock order is Code's, not Q2's |
| B61 | answers:62–65; the routing | §3 declares the order as Code's reading; the place of PROPOSAL-n's model-free steps against the F3 build goes to the PI at the OLMo build's entry |
| B62 | `PROPOSAL-n…v0_1.md:26` item (6) is the pod order; v0.2's is (7) | corrected |
| A4 | v0.2:38 | "Its header and PROPOSAL-n lines …" |
| A22 | answers:35 | "cap-reach over the reasoning lines of all six sessions (≤ 36)"; A23's #10 added |
| A24 | answers:42 | scoped "for a driver edit", with mf3_sessions.py's forms and the per-unit weights binding |
| A26 | answers:50, :58 | "the seven items Code named … and the build hazard's declared check" |
| A33 | answers:20, :62–63 | G-ANL-F3 and the lock chain added; declared as Code's order |
| B42 note | CLAUDE.md:397–399, :402–403 | new dated note N6 |
| B36 note | answers:36 | §1's line marks the cap-boolean inference as Code's reading and gives the seat's ground |
| coverage | m:205–214; RESULTS.md@9cbacdb:236, :238; `m_analyze.py:2370–2387`; step17.md:86; VERDICTS_read.md:86; review raw :200–207 | §1 gains lines for §0's hours and N9, §2's `posting`, §3's N8 and §6's carry-overs; §9 is the referent check's §3 |
