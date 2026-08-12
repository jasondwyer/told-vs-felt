# RESULTS — Phase 2

Dated experiment log for Phase 2 (the OLMo-3.1-32B developmental study).
Prior logs, frozen and archived: cycles 1–2 at
[`archive/RESULTS-cycle1-2.md`](archive/RESULTS-cycle1-2.md) (tag
`cycle-2-close`); cycles 3–4 at
[`archive/RESULTS-cycles3-4.md`](archive/RESULTS-cycles3-4.md) (tag
`cycle-4-close`). Synthesis chain: [`FINDINGS.md`](FINDINGS.md) →
[`FINDINGS-2.md`](FINDINGS-2.md) → [`FINDINGS-3.md`](FINDINGS-3.md) →
[`FINDINGS-4.md`](FINDINGS-4.md). Operative design:
[`CLAUDE.md`](CLAUDE.md) (v3.1); Phase 1 is **not** licensed and awaits
PROPOSAL-g plus its pre-registrations.

Conventions unchanged: dated entries, dense, newest-first within a
section; raw stdout worth keeping goes to
`results/raw/YYYY-MM-DD_short-name.txt` and is linked; verdict-relevant
analysis artifacts are committed under `data/` (ledger 27);
design-relevant findings are flagged for discussion, never silently
applied to CLAUDE.md.

## Log — Phase 2

- 2026-08-12 — **Phase 0 step 0a: restructure executed. CLAUDE.md v3.1
  is operative; the cycle-3/4 record is archived and frozen at tag
  `cycle-4-close` (commit `50906bf`). Infrastructure only — no
  experiments run, none licensed beyond Phase 0.**

  - **Amendment to step 0 (user, 2026-08-12), logged here as
    instructed.** Step 0 splits. **0a (this entry)** — verify
    FINDINGS-4 present; apply its housekeeping list; tag
    `cycle-4-close`; archive v2 CLAUDE.md and RESULTS.md; place the
    v3.1 draft as CLAUDE.md; open this log; commit, push. **0b
    (deferred, its own future entry)** — the `paper-1` release is cut
    **only when the user declares the preprint final**; it freezes the
    state the published paper cites and is explicitly **NOT a Phase-0
    prerequisite**. Steps 1–5 proceed without it. CLAUDE.md §Phase 0
    step 0 was edited to carry the 0a/0b split; step 1 (core refactor
    + rule-26 regression) remains laptop-side.
  - **Blocked-then-cleared history:** step 0 was first attempted
    2026-08-12 and stopped at its own first instruction —
    `FINDINGS-4.md` did not exist in the working tree, on any branch,
    or on origin, and no preprint existed to define the `paper-1`
    state. Escalated rather than self-adjudicated (two-instance
    protocol). FINDINGS-4 was then placed by the design instance;
    `paper-1` became 0b.
  - **FINDINGS-4 housekeeping list, disposition:** (1) status lines —
    **done**, the archived v2 CLAUDE.md carries a terminal status block
    (cycles 3 and 4 CLOSED, five nulls, no experiments licensed by that
    document, superseded-by pointer); note that FINDINGS-4's "program
    at write-up; pending any fifth-cycle GO" is **superseded** by v3.1,
    which licenses Phase 0 (infrastructure) and gates Phase 1 on
    PROPOSAL-g — no experiment is licensed either way. (2) ledger
    candidates — **signed off** via v3.1 acceptance, mapping below.
    (3) forward pointers — **done** (FINDINGS-3 gains a fourth-cycle
    blockquote; FINDINGS.md gains the fourth chain line). (4) preprint
    v0.3 and (5) blog coda — **deferred to 0b**; neither artifact lives
    in this repo, both are design-instance/user work.
  - **Ledger sign-off mapping (verified, not assumed).** FINDINGS-3's
    four: trace-channel closure of rule 5 → **5(c)**; checkpointed-bars
    principle → **21**; purity≠potency selection law → **22**;
    persistent-KV ban → **5(d)**. FINDINGS-4's four: completed tripwire
    framework → **21**; anecdote-governance counters → **23**;
    below-floor discipline → **24**; apparatus-hazards addendum →
    **partially distributed** across 13 (completion-style, stop
    discipline, scaffold bans, frozen audit patterns), 18 (tag-roster
    lexical assertions against every pool), and 21 (stimulus-provoked
    degeneracy gates on unprovoked domains).
  - **FLAGGED for design-instance adjudication — one candidate not
    fully cashed.** The apparatus-hazards addendum's fourth clause has
    no ledger home: *exclusion rules can render descriptive features
    structurally undefined on the surviving sample (the degen-round
    feature) — define descriptive features against the exclusion rule,
    not alongside it.* This is a live hazard for Phase 1's
    screen-tier operant, where the same exclusion machinery runs per
    checkpoint. Not applied; flagged per protocol.
  - **Ledger 27 applied to the cycle-4 record (user-approved).** The
    cycle-4 analysis artifacts existed **only** inside the gitignored
    `jlens-qwen36/` external clone; RESULTS' `data/f/…` citations
    resolved to an empty directory. Copied out (never committed inside
    that clone) into repo `data/f/`: `sessions.jsonl` (344 lines =
    344/344 declared sessions, a clean check against the N
    declaration), `sessions_smoke.jsonl`, `screen_analysis.json`,
    `postscreen_descriptive.json`, `calib.json`, `pools.json` — 1.6 MB.
    `.gitignore` gains a scoped exception (`data/f/*.json`,
    `data/f/*.jsonl` tracked; `.npz` and everything else still
    ignored; verified with `git check-ignore`). All 33 cycle-4 raw
    stdout files were already committed.
  - **FLAGGED — rule 26's oracle set has the same provenance gap, and
    it blocks nothing yet but will.** Step 1 acceptance requires
    reproducing (i) the g1r kernel-gate KLs, (ii) a 128-context B2b
    subsample, (iii) e2a choice-read construction KL = 0.0 **on
    archived session texts**. Those three inputs —
    `e2a/g1_kernel_gate.json` (7 KB), `e0/e0_b2_b2b.json` (1.7 KB),
    `e2a/sessions.jsonl` (1.0 MB) — currently exist only in the
    gitignored clone, i.e. on one laptop. Recommendation: extend the
    `data/` exception to those three before step 1 begins, so the
    regression law's reference values are in the record rather than on
    a machine. Awaiting user/design-instance go; ~1 MB.
  - **Repo state after 0a:** root carries CLAUDE.md (v3.1),
    FINDINGS-1..4, PROPOSAL-d/e/f, README, this log. `archive/` carries
    CLAUDE-cycle1-2 / RESULTS-cycle1-2 (tag `cycle-2-close`) and
    CLAUDE-v2-cycles3-4 / RESULTS-cycles3-4 (tag `cycle-4-close`).
    Archived docs' relative links are stale by design — records, not
    working docs.
  - **Next:** step 1, `valence_core/` refactor + the rule-26 regression
    suite, laptop-side (the Qwen oracle is here). Steps 2–5 are
    cloud-side and follow. No Phase-1 work on an unverified core.
