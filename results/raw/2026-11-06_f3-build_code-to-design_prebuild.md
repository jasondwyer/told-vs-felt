# m package — BUILD (F3), ADDENDUM-m1 §4 step 5: STOP before the first package edit (Code → design seat, through the PI)

*Code's raw. Written 2026-11-06 UTC at HEAD `24ebeae` = origin, and revised after two blind values-checks before its push.*

*The PI's word in this session was "Yes, start here", in answer to Code's question "Begin the Q-F3 build (ADDENDUM-m1 §4
step 5) in this session?". The build has started with its inputs: three read-only maps of the F3 spec, the package and
the record, kept in Code's scratch directory. **No package or driver code is written, and no file that LOCK-m-F0 names
is edited.***

*Code stops here under the seat's standing rules:*
- *Step-10 read §2 item 5: "a post-lock edit to a file the lock names is put to the seat before Code acts on it".*
- *R1 A2: "a reading that departs from a listed order is put to the seat before Code acts on it".*

*`m:N` is PROPOSAL-m v1.11 (sha256 `42ab36ec…6c6b`); `A-m1` is ADDENDUM-m1 v0.1 (`f26bc59`). Two blind values-checks ran
before the push: one of the first draft (128 claims: 2 FAIL, 14 IMPRECISE) and one of the rewrite (154 claims: 0 FAIL,
13 IMPRECISE). Both reports, with Code's dispositions, are in `results/raw/2026-11-06_f3-build_prebuild_valuescheck.md`.
Every item was re-verified by Code and is applied here.*

## 1. What binds, and what is pending on both tracks

**The bindings, checked at source:**
- `package_sha256` hashes every `*.py` directly in `valence_core/m/` (`resume.py:296–328`, non-recursive). Its value is
  `5f646db6…` over 18 files, and LOCK-m-F0 v1.0 names it.
- Every non-stub stage start checks three things (`stages.py:530–608`):
  - (d) it hashes the analyzer's bytes against the identity's `analyzer_sha256` (:586–594);
  - (e) it recomputes `package_sha256` (:595–600);
  - (f) it requires the governing lock's committed text to name both (:601–607).
- The lock's v0.1 text, §1 (LOCK-m-F0.md:1186–1188, from the D2 round entry's "To the seat"), says: "A later edit to the package or
  the analyzer moves a hash this file names. Every non-stub stage then refuses until a lock revision names the new hash."
- Code's statement recorded in the lock (:2396–2400, labelled "(Code's statement, from the record)") adds: "An edit to a
  `SCORING_STACK_FILES` entry (`gshape.py:92–104`) re-runs G-SHAPE-F0 first (R1 D3; PIN-S10)". That list includes
  `keys`, `banner`, `schedule`, `scaffold`, `runner_qwen`, `runner_olmo`, `audit` and `corr`.
- PIN-S10 itself (`gshape.py:233–236`) reaches wider. G-SHAPE-F0's artifact records each scoring-stack and tooling file's
  sha256, where the tooling files are `gshape.py` and `scripts/m_sessions.py` (`:105`), and "any difference re-runs
  G-SHAPE-F0 first". The seat has cleared subcommand-wiring driver edits (the step-10 read's Q2). Which other edits
  re-run it is the seat's to state.
- The analyzer's `verdicts` command asserts the analyzer, package and closure shas against the unit's lock (PIN-14,
  `m_analyze.py:1934–1944`). Its other path, "a worktree of the lock commit", is declared and not implemented.
  `posting` records the three shas and does not refuse on them.
- The analyzer imports `audit`, `bars`, `keys`, `readrule` and `resume` at module level (`:79`), and `stages` lazily. So
  a package edit can change the analyzer's behaviour without moving its own sha; PIN-14 binds it through
  `package_sha256`.
- The schedule directory:
  - `verify_schedule_dir`, run at every stage start, rejects any unlisted `*.json` (`schedule.py:647`);
  - the manifest (`8c89636a…`, which LOCK-m-F0 pins as a record) lists 25 files;
  - two self-tests pin the directory's 26 files, manifest included (`schedule.py:953–954`, `scripts/m_sessions.py:3470`);
  - the writer refuses to overwrite a changed file unless `overwrite=True` (`schedule.py:596–605`).

**The direction of the rule.** An edit made *after* a lock names the old hash, to a `*.py` file directly in
`valence_core/m` or to the analyzer, makes that lock's non-stub stages refuse until a revision names the new hash. A lock
written *after* an edit names the new hash, and nothing refuses.

**Code pending on both tracks.**
- **Q-F3** needs:
  - a different scaffold: F2 block order (m:174), and a reasoning-line seed before each menu order (m:159);
  - a runner with the reasoning block (m:174) and the reasoning-line classes (m:265);
  - a resume identity that carries the line cap (m:174, m:267);
  - F3 read rules, bars and stage drivers, and Q-F3's schedules.
- **The OLMo track** is not build-complete either:
  - G-CAL-OLMo is not built (`gcal.py:39–40`: "G-CAL-OLMo (per checkpoint, b3's banner and generation path) is the
    OLMo track's and is not built here"; `gcal.py:692` writes `"substrate": "qwen"`).
  - The OLMo stages are not wired in the driver; they still carry "the step-9 track's refusal" (`scripts/m_sessions.py:491–492`).
  - A-m1 calls the units "build-complete" (§0.1; also :16 and :52). That holds of step 4's list (m:357): Q-F0 also
    built its G-CAL tooling at its own step (`c75d4d8`, step 6) and wired each subcommand at its own step
    (LOCK-m-F0.md:2488). The readiness reading does not hold, namely §0.4's hours at :16 and §3 item 5's "the units are
    build-complete and short" at :52: G-CAL-OLMo's tooling and the OLMo stage wiring are still to be built before the
    first OLMo stage. Code's referent check at `f26bc59`, scoped to §5's referents, did not test this.
  - The OLMo track therefore has its own build step before its first stage. Code placed for it under `valence_core/m`
    moves `package_sha256` as well.

**What follows.** Both tracks hold code that would land in, or bind to, `valence_core/m`. Whichever track's code moves the
package after the other track has a lock that binds `package_sha256` forces a revision of that lock, and of every earlier
such lock. The analyzer is the same under every placement: G-ANL-F3's in-place edit after an OLMo lock names `655e0f7f…`
makes the OLMo stages refuse at start (check (d)), not only their VERDICTS.

**Other consequences, by placement.**
- **G-SHAPE-F0** re-runs on any difference in its sources map (PIN-S10), subject to the seat's clearance of subcommand-wiring driver edits.
- **A-m1 §2.5 (3)'s byte-for-byte regression** of `Q-F0_VERDICTS.json` meets that file's embedded shas:
  - the analyzer sha under every placement, because G-ANL-F3 extends `m_analyze.py` in place;
  - the package sha only if `valence_core/m` moves;
  - the closure sha under any placement, if the extended analyzer's imports (module-level, and its lazy verdict
    modules) reach new code outside `valence_core/m`, or if a new data file is read at import (`m_analyze.py:1681–1734`;
    `:1714` excludes `valence_core/m`).
  How the regression treats those fields is G-ANL-F3's.
- **A subdirectory** such as `valence_core/m/f3/` lies outside both the package hash and the closure. It would run
  unbound, and Code rules it out.

## 2. The questions

**Q1. Where Q-F3's code lives, and what its licence binds (binds LOCK-m-F3 v0.1's "module homes").** Code recommends
**(C2)**.
- **(A) Extend `valence_core/m` in place.**
  - The least code.
  - It moves `package_sha256`, and it re-runs G-SHAPE-F0 because scoring-stack files are edited.
  - It rewrites the self-tests that assert today's Q-F3 refusals, among them:
    - `keys.py:204–214`;
    - `banner.py:238–254`: "TOLD_OBJ never used", and "refuses clause 2/bool, A1, base, …";
    - `guard.py:1502–1505`, `resume.py:1158`, `schedule.py:812–815` and `stages.py:2683–2695`;
    - the driver's step-19 refusals.
- **(B) New flat modules in `valence_core/m` plus small edits.** This moves `package_sha256` too. G-SHAPE-F0 re-runs
  only if a scoring-stack file is among the edits.
- **(C) A sibling package, e.g. `valence_core/mf3/`, importing `valence_core.m` unchanged.**
  - It reuses by import: `corr`, `corrupt_m`, the audit's task-round classes, `bars`, the banner constants,
    `schedule`'s cells and `keys.stream`.
  - It adds its own scaffold, runner, verifier, line classes, read rules, resume identity, bar table, stage drivers and
    G-SHAPE-F3, plus a new driver and Q-F3's schedules under their own directory and manifest.
  - Q-F3's build then needs no `valence_core/m` edit. Its own keys and source guard live in the new package; today
    `keys.py:66–67` and `guard.py:160–162` refuse Q-F3. The analyzer's unit check is G-ANL-F3's to settle
    (`m_analyze.py:1921`, `keys.UNITS_BUILT`). The cost is more code to review.
  - Two forms of its licence:
    - **(C1)** It binds the whole of `valence_core/m`'s `package_sha256`. Then an OLMo-side edit there after LOCK-m-F3
      v0.1 forces a Q-F3 lock revision, which is the reverse collision.
    - **(C2)** It binds the file sha256 of each `valence_core.m` module Q-F3's runs import, closure-style. Then OLMo-side
      edits collide with Q-F3's stage licences only if they touch a module Q-F3 imports.
      - `gcal.py`, `runner_olmo.py` and the driver are not among them, provided the F3 package imports neither `stages`
        nor `gshape`: both import `runner_olmo`, and `gshape` also imports `gcal` (`stages.py:135`, `gshape.py:51`, `:54`).
      - This decouples stage-time licences only. At VERDICTS the analyzer's PIN-14 binds the whole `package_sha256`
        (`m_analyze.py:1934–1944`), and its production path imports `stages` (`:1783–1784`).

**Q2. Sequencing and the OLMo track's own build.** A-m1 §4 step 4 runs the OLMo track "in parallel with 5".
- Where do G-CAL-OLMo and the OLMo stage wiring go? In `valence_core/m`, which moves the hash, or beside it.
- Under (A), (B) or (C1), Code proposes "builds before locks": every pending package build of both tracks lands before
  the first new lock, so every LOCK-m-OLMo-{ckpt} v0.1 and LOCK-m-F3 v0.1 names the final hash.
- Under (C2), only a package edit to a shared module Q-F3 imports needs sequencing at stage time. The analyzer's edit at G-ANL-F3 needs sequencing against the OLMo locks under every placement (Q3).

**Q3. The analyzer's versioning.** R1 C7 says: "Deferred to before step 19, as Code lists it"; see also PIN-14.
- Code's reading of A-m1 §2.5: G-ANL-F3 extends `scripts/m_analyze.py` in place, and LOCK-m-F3 v0.1 names the extended
  blob (m:292). Each unit's analyzer of record stays the blob its own LOCK v1.0 hashes (PIN-14).
- So if the OLMo locks name `655e0f7f…` and G-ANL-F3 lands while the OLMo track is still running, two things follow.
  The OLMo stages refuse at start (check (d)) until their locks are revised. The OLMo VERDICTS need PIN-14's worktree
  path, which is not implemented. The alternative is that the OLMo track, its VERDICTS included, finishes before
  G-ANL-F3's commit.
- **Please confirm this reading, or choose a new file for G-ANL-F3.** Please also say which texts ride in that round,
  since round 2's "text correction at the next hash-moving round" meets A-m1 §2.5's "No other change to the analyzer is
  licensed by this addendum".
- This blocks G-ANL-F3, not the build.

**Q4. The scaffold-set review the VERDICTS read placed here.** The seat's read §5 item 2 says: "`You are a helpful
assistant.` … `4assistant` … and `<|end|>` … the three strings are candidates for the scaffold-set review at Q-F3's step
4 (m:267's set is e2a's by sha), decided there". The set is defined at m:261; the seat's anchor reads m:267.
- Code's observation: each string occurred in Q-F0's sessions, so as hair triggers they would bind a class with a
  measured base rate (rule 21).
- Code's proposal: keep Q-F3's scaffold set as e2a's by sha, and declare the three strings as a descriptive counter
  under rule 23.
- The decision is the seat's.

**Q5. G-TIME-F3's contrast reporting and the cap trigger, before the stage driver is written.**
- The clauses in conflict:
  - m:174's trigger counts cap-reach over "the reasoning lines G-TIME-F3 generates (≤ 36)".
  - m:293 reports "the A1, A2 and A3 sessions' rounds and lines … beside" and has "cap-reach counted over all six".
  - m:271 withholds contrast sessions' free-round events to VERDICTS. Lines 2–6 of a contrast session follow its picks.
- Code's step-3 notes of 2026-10-06 (`results/raw/2026-10-06_m-v1.11_step3_notes.md`) were graded minor and never
  dispositioned by number:
  - #87 records that m:293 and m:297 lack the forced-round scope.
  - #116 offers "the A1, A2 and A3 sessions' forced rounds reported beside".
  - #130 offers "count the trigger on the three sham sessions' ≤ 18 lines, or declare it an exception in §3 and §4".
  - #10 (counter (c)'s blind read) offers "performed after the analyzer's output exists and before the seat's full read".
- Part of their substance is ruled elsewhere. Ruling (h) covers the G-TIME contrast reporting (LOCK:2411), and the
  step-14 read's Q5 keeps m:263's printed form at every Qwen stage. Neither reaches #130's cap trigger or the contrast
  sessions' reasoning lines.
- Code builds whichever the seat rules.

**Q6. Carry-overs the Q-F0 record addressed to "the next unit".**
- The `CHECKPOINT STATE INCONSISTENT` message and options O1-3, RM4-1 and O4-1 are addressed to "the next unit's step 4"
  or its "driver edit".
- Code's declared limits VC4-1 and VC4-2 wait for "the driver's next edit".
- Binding the weights snapshot in the identity: "a later unit may add it at its step 4".
- The listing commands under O2-3 are addressed to "the next unit's README" and "the next unit's checklist".
- The step-14 read framed the driver-edit items for a build "where the package moves anyway" (`2026-10-13_m-design-to-code_G-F0m-Qwen_read.md:42`). Under (C) that premise does not hold.
- Code's reading is that they are owed at Q-F3's build, unless the seat names the OLMo wiring as "the next unit".
- Please confirm.

**Q7, for LOCK-m-F3 v1.0 and not the build.** m:298 has that lock hash "the preprint of record as edited for v2", and
m:73 builds and hashes v2's sentence table there. Under (10′) (A-m1 §2.3) the lock can come before the v1 posting of a
preprint the PI is now writing from scratch. The OLMo locks have "preprint of record pending" (m:302); this lock has no
such fallback. It needs a word before LOCK-m-F3 v1.0.

**Q8. Code's readings of the spec's open items.** Thirty-one places where the spec leaves a reading open need a PIN, and one build hazard needs a declared check.
Among them:
- the "empty line" and the reasoning-line echo (which harness lines count, containment or equality);
- "cap reached without a newline";
- a scaffold fire on a reasoning line (the session's validity, and the guard's pre-pick count);
- defects "by property";
- G-ID-F3's index rule and its re-run after a cap change;
- the "\n\n" an empty line makes after the reasoning segment, against rule 28(d)'s boundary assertion;
- the build's scope (m:361 names the runner, the verifier and the line classes, while LOCK-m-F3 v0.1 also needs keys,
  schedules, gate files and the bar table).

Code's proposed reading for each goes into the build design raw. They are declared as Code's PINs at LOCK-m-F3 v0.1
and listed as flags in the BUILD entry, as at Q-F0's build, unless the seat rules on any of them first.

## 3. What Code does meanwhile

- Code writes the parts of the build design that do not depend on Q1. Nothing is written into `valence_core/m/`,
  `scripts/m_sessions.py`, `data/m/` or any file a lock names.
- The build starts on the seat's answers to Q1 and Q2, and on Q5 for the stage drivers. Q3, Q6 and Q7 gate later steps.
- The OLMo track (A-m1 §4 step 4) is not run by this STOP. Before its first stage it needs:
  - its own build of G-CAL-OLMo and its stage wiring, whose placement is Q2's;
  - the runpod re-authorisation;
  - the PI's go, which the routing gives after the re-authorisation.
