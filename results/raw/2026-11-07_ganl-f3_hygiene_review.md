# G-ANL-F3 hygiene commit (N9, N12): blind code review and values-check (Code's raw, 2026-11-07)

*A blind agent (fresh context, read-only) reviewed the hygiene diff in Code's scratch worktree (`139635f` plus `scripts/m_sessions.py`, `scripts/mf3_sessions.py` and `valence_core/m/gcal.py`, at the first scratch commit) and values-checked the RESULTS entry's draft. Its report follows verbatim, local paths scrubbed (`<tmp>` = Code's session scratch). Code's dispositions follow it, each item re-checked at source. Two NOTEs changed code, so m's package hash moved again (`252e2fb2…8049` → `7756dcf4…49bb`; the report names the first). The mf3 literal was updated to match, and the site check and gcal's three-state runs were re-run on the final bytes (the site-check raw).*

## 1. The report (verbatim)

(R) 0 MAJOR, 2 MINOR, 7 NOTE. (V) 37 items: 30 CONFIRMED, 3 IMPRECISE, 1 FAIL, 3 NOT CHECKABLE.

I changed no git state and the worktree is as I found it (only the untracked HANDOFF file that was already there). My probe scripts and their outputs are in <tmp>/hyg_review/ (results in probes_out.txt).

## Review

**Checked, no finding:**
- **Production is unchanged.** I compared the syntax trees of 139635f and 2b96683 for all three files. Every top-level node outside `_selftest` is identical, and the text outside `_selftest` is byte-identical.
- **Both substitutions are scoped and restored.**
  - gcal.py:2406–2410: a `mock.patch` context around the one `precheck` call.
  - m_sessions.py:6930–6933: the `patched` helper (try/finally, :1874–1881) around the one `run_gcal_completability` call.
  - The case passing in the present state proves the patch takes effect, because without it CHECKPOINT EXISTS would fire.
- **State independence (probe).** For sft, dpo and instruct, production `_canonical` gives CHECKPOINT EXISTS. With the stand-in, the only refusal is POD ID ABSENT (no model-free, weights or gate-line problem), and `_canonical` is restored afterwards.
  - Under the stand-in, neither call reads a canonical artifact or checkpoint path, so both cases hold in any repo state.
  - The cases can still fail: losing the pod-id rule drops "POD ID ABSENT"; losing the weights check drops "weights:"; a `_paths` that bypassed `_canonical` would trip CHECKPOINT EXISTS again.
- **N9.** `data/f/pools.json` is committed (blob 8a54d3c7, unchanged since 50906bf). Its sha256 8547d9a1…17a0 is named in full at LOCK-m-F0.md:419 and :1443.
  - Probe: `stage_identity_extra` is clean for it and `startup_problems` returns a banner problem. The analyzer gives "not named in full". The proposal gives no banner problem.
  - The case still tests "a committed file the lock names that is not a proposal (the banner check)", now on a frozen file. The old analyzer premise had broken twice before (the 2026-10-14 step-15 raw :376, and N9).
- **m's package.** 252e2fb2a11771c1…8049 is right: I recomputed it independently over the git blobs of 2b96683 and over the worktree (18 files). It was 60199b36…feec at 71cc23c and at 139635f.
  - The new check at mf3_sessions.py:179 uses m's own formula plus the 18-file count. It is sound as a tripwire, prefix-only like the line it replaces.
- **Live uses of the old hash.** mf3_sessions.py:177 was the only live code naming 60199b36.
  - Posting's cross-check of NOT-RUN outputs reads only reason and cause (m_analyze.py:2675–2681).
  - The ganl manifest check (m_analyze.py:11216) applies to G-ANL-F3.json, which does not exist yet.
  - No lock names 60199b36: LOCK-m-F0 names 5f646db6…, and no LOCK-m-OLMo-* or LOCK-m-F3 exists.
  - gcal.py's own sha256 (d60b78e5…) is bound nowhere live. The untracked valence_core/p computes m's package live (p/gcal.py:22) and pins nothing.

**MINOR**
- **M1. A departure from the seat's order is not flagged.** The entry says the mf3 literal "rides in this commit, as the coordinating session's step 1 lists it". The seat's §7 sequence (answers:50) is: hygiene commit → G-SHAPE-F0 re-run → mf3_sessions.py literal → G-SHAPE-F3 re-run.
  - Failure case: an audit of declared order finds step 3 done inside step 1, with an uncommitted message as the only warrant.
  - The effect is harmless. G-SHAPE-F0's TOOLING_FILES are gshape.py and m_sessions.py (gshape.py:105). Without the literal, mf3_sessions would sit at 135/136 at the hygiene commit.
  - The same paragraph supports it ("with its consequences taken now"). The entry should say all of this.
- **M2. The entry silently contradicts the seat.** The seat's §7 N12 says "(mf3's package moves; G-SHAPE-F3 re-runs…)". The entry's "What does not move: mf3's package f30ad505…6310" is correct: the package is valence_core/mf3/*.py (15 files, unchanged), and mf3_sessions.py lives in scripts/.
  - The entry should flag that the seat's parenthetical does not hold. mf3's package last moved at e0b4f2c (44110d15…→f30ad505…), which is what N3's re-run answers.

**NOTE**
- **N-1.** Both stand-ins re-implement `_canonical` instead of deriving from it (gcal.py:2402–2405, m_sessions.py:6926–6929), and they name the parameter `u` where production uses `unit`.
  - If `_canonical` gains a key or moves the model-free path, the cases diverge silently or raise KeyError.
  - Deriving from the original makes "model-free stays canonical" true by construction: `{**orig(unit), "out": …, "ckpt": …}`.
- **N-2.** The seat said "an empty temporary checkpoint root", but the fix also redirects the artifact path. That is necessary: with only the checkpoint redirected, the probe refuses COMPLETABILITY ARTIFACT EXISTS, because 6ce8b9a also committed the three completability artifacts. Add one clause saying so, as Code's reading of the ruling.
- **N-3.** The evidence is narrower than the claim. State B moved only the three checkpoints and left the three artifacts in place, a state the record never had, and only gcal's own self-test ran there. m_sessions' case ran only in the present state. The claim holds by construction; say that, and say what was run.
- **N-4.** "Every state of the record" does not mean every site. m_sessions-olmo's case still assumes no /workspace/models/instruct, and on the box it fails on "weights:" (results/raw/2026-11-06_gcal-olmo_smoke_box-selftest.txt:836). This is outside N12.
- **N-5. "What moves" leaves out recorded provenance this commit makes stale.**
  - Going stale, both re-run next:
    - data/m/gates/G-SHAPE-F0.json: provenance.package_sha256 60199b36…, and tooling m_sessions.py f0e9d5c4…. So the G-SHAPE-F0 reason can name the package too.
    - data/mf3/gates/G-SHAPE-F3.json: mf3_sessions.py 48008a53…
  - Historical and fine:
    - The G-CAL-OLMo checkpoints and completability artifacts record identity.package_sha256. A `--resume` would now refuse with CHECKPOINT MISMATCH, as the Qwen G-CAL artifact (4b496587…) already would.
    - data/m/verdicts/OLMo-*_NOT-RUN.json. Re-invoking `not-run` would no longer reproduce them; the write-once rule refuses.
- **N-6.** The site-check raw to be committed should:
  - say that the untracked HANDOFF-2026-09-04-design.md was copied into the worktree, because closure_verify3's R13 reads it (e2d_closure_verify3.py:101). The G-ANL-F3 build's site-check raw did this at :6–7.
  - scrub paths: sitecheck_out/m_sessions.txt has 48 lines with <tmp> or <tmp> paths, and mf3_sessions.txt has 3.
- **N-7.** The comment at m_sessions.py:4479, "LOCK-m-F0 names only 655e0f7f...", should read "names in full only". The lock also carries the truncated 66fb521488db41e7… (e.g. LOCK-m-F0.md:83, :1137).

## Values-check
1. Seat's rulings dated 2026-11-07 — CONFIRMED.
2. PI's routing of 2026-11-07, item 1 — CONFIRMED (RESULTS.md@139635f:75–81).
3. "the premises of two self-test cases" — FAIL. There are three cases: N9's one and N12's two (843→846; the G-ANL-F3 build site-check raw :8 says "three cases"). Suggested: "the premises of three self-test cases (N9's one, N12's two)".
4. No production behaviour changes — CONFIRMED (syntax-tree comparison).
5. 846/846 "again" — CONFIRMED; the self-test of record is 846/846 at results/raw/2026-11-06_m-olmo-build_selftest.txt:849.
6. Routing quote — CONFIRMED, verbatim, against RESULTS.md@139635f:81.
7. "(in its message, not a file)" — IMPRECISE: the same quote is committed at RESULTS.md@139635f:79–81. Cite that.
8. Answers path, 139635f, sha256 ab40f470…b08b, §7 — CONFIRMED (recomputed).
9. The case names data/f/pools.json — CONFIRMED (m_sessions.py:4480).
10. pools.json is committed — CONFIRMED.
11. LOCK-m-F0 names 8547d9a1… in full — CONFIRMED (:419, :1443).
12. pools.json is neither the proposal nor the analyzer — CONFIRMED.
13. "startup: banner" again, and it holds — CONFIRMED (sitecheck m_sessions.txt:780; probe).
14. The N12 case names — CONFIRMED (gcal.py:2422; m_sessions.py:6935–6937).
15. `_canonical` stand-in, for that one call — CONFIRMED.
16. Artifact and checkpoint resolve under the empty root; model-free stays canonical — CONFIRMED.
17. "every state of the record, with or without the checkpoints 6ce8b9a committed" — IMPRECISE. It holds by construction, but 6ce8b9a committed checkpoints and artifacts, and the evidence is as in N-3.
18. Only self-test code changes — CONFIRMED.
19. 60199b36…feec → 252e2fb2…8049 — CONFIRMED.
20. "because gcal.py is in valence_core/m" — CONFIRMED (the diff's only valence_core/m file).
21. The mf3 check is updated and names the move — CONFIRMED (mf3_sessions.py:176–179).
22. "as the coordinating session's step 1 lists it" — NOT CHECKABLE (see M1).
23. mf3_sessions.py is a G-SHAPE-F3 tooling file — CONFIRMED (mf3/gshape.py:91; G-SHAPE-F3.json:280).
24. Analyzer 6ec3222b…93d9 — CONFIRMED.
25. Base closure a3bc7bb9…b22b — CONFIRMED, recomputed with `closure()`; equals RECORD_CLOSURE_SHA256.
26. Q-F3 closure d19f336d…f039 — CONFIRMED, recomputed with `lazies=LAZY_VERDICT_MODULES + LAZY_F3_MODULES`.
27. "Both cover modules outside valence_core/m" — IMPRECISE. Each closure also hashes the non-.py repo files opened during the imports (PIN-1, m_analyze.py:1833–1836; here data/olmo/a1_repair_roster.json). Suggested: "both hash the loaded valence_core modules outside valence_core/m and the non-.py files opened at import; no valence_core/m file enters either".
28. mf3's package f30ad505…6310 unchanged — CONFIRMED, recomputed (but see M2).
29. The licence's eleven hashed m files, and gcal in ABSENT_MODULES — CONFIRMED (mf3/guard.py:66–71).
30. Site check on 139635f plus the three files — CONFIRMED: the worktree is at 2b96683 and its diff is byte-identical to hygiene.diff (plus the HANDOFF copy, N-6).
31. All ten suites pass; m_sessions 846/846, m_analyze 525/525, mf3_sessions 136/136 — CONFIRMED.
32. gcal 63/63 in both states — CONFIRMED. 63 is also the count of gcal checks in the m_sessions run. "Absent" means the checkpoints only.
33. G-SHAPE-F0 re-run, because m_sessions.py is in PIN-S10's map — CONFIRMED (gshape.py:105, :233–236), though incomplete (N-5).
34. G-SHAPE-F3 re-run under N3 — CONFIRMED (results/raw/2026-11-06_ganl-f3_build_design.md:109).
35. F3R-PREPRINT-OF-RECORD at m_analyze.py:9983–9986 — CONFIRMED. Line :9985 asserts head_file_sha256 is neither None nor the table's sha256. The file is read from the working tree (:9895), so a restored working-tree file fails the check whether or not it is committed.
36. "relayed to the coordinating session" — NOT CHECKABLE.
37. "Not pushed" — NOT CHECKABLE (a future state).

## 2. Code's dispositions

| Item | Re-checked at source | Disposition |
|---|---|---|
| M1 | answers:50 orders the literal after G-SHAPE-F0's re-run; `gshape.py:105` TOOLING_FILES = gshape.py, m_sessions.py. | Applied: the entry states the departure, its warrant (the coordinating session's step 1) and its effect (none on G-SHAPE-F0; mf3_sessions 135/136 without it). |
| M2 | `valence_core/mf3/*.py` unchanged; mf3's package `f30ad505…` before and after. | Applied: a FLAG in the entry, not adjudicated. |
| N-1 | Both stand-ins re-implemented `_canonical`. | Applied: each binds the original before the patch and returns `{**original(unit), "out": …, "ckpt": …}`; the parameter is named `unit`. m's package hash moved again (`7756dcf4…49bb`); the mf3 literal follows. Re-tested: the site check, and gcal's self-test in three states. |
| N-2 | Without the artifact redirect the precheck refuses COMPLETABILITY ARTIFACT EXISTS (the agent's probe; `gcal.precheck`'s order). | Applied: the entry states Code's reading. |
| N-3 | State B left the artifacts in place. | Applied: a state C (checkpoints and artifacts out, the state before `6ce8b9a`) was added for gcal's self-test, and m_sessions' self-test ran in state C too. The entry says what was run, and that the claim holds by construction. |
| N-4 | `results/raw/2026-11-06_gcal-olmo_smoke_box-selftest.txt:836`. | Disclosed, no change. It is a box-site assumption outside N12; the self-test of record is the laptop's. |
| N-5 | G-SHAPE-F0.json's provenance (package, m_sessions.py); G-SHAPE-F3.json's tooling (mf3_sessions.py). | Applied: the entry lists them, both re-run next, and names the historical records that stand. |
| N-6 | The site-check raw's header names the HANDOFF copy; the raw is built from the suites' summary lines and scrubbed. | Already so. |
| N-7 | LOCK-m-F0.md:83 carries `66fb521488db41e7…` truncated. | Applied: "names in full only". |
| V3 (FAIL) | Three cases (843 → 846). | Applied. |
| V7 | RESULTS.md@139635f:79–81 quotes the block. | Applied: cited. |
| V17 | As N-3. | Applied. |
| V27 | PIN-1 (`m_analyze.py:1833–1836`): the closure also hashes the non-.py files opened at import. | Applied. |
| V22, V36, V37 | — | Not checkable; no change. |
