# RESULTS — cycle 3

Dated experiment log for the third design cycle. Prior cycles: full log at
[`archive/RESULTS-cycle1-2.md`](archive/RESULTS-cycle1-2.md) (frozen at tag
`cycle-2-close`); syntheses: [`FINDINGS.md`](FINDINGS.md) (cycle 1, semantic
states) and [`FINDINGS-2.md`](FINDINGS-2.md) (cycle 2, strain states).
Operative design: [`CLAUDE.md`](CLAUDE.md) (v2) +
[`PROPOSAL-d-distilled-trace.md`](PROPOSAL-d-distilled-trace.md) +
[`PROPOSAL-e-reward-axis-hijack.md`](PROPOSAL-e-reward-axis-hijack.md).

Conventions unchanged: dated entries, dense, newest-first within a section;
raw stdout worth keeping goes to `results/raw/YYYY-MM-DD_short-name.txt` and
is linked; design-relevant findings are flagged for discussion, never
silently applied to CLAUDE.md.

## Log

- 2026-08-08 — **proposals accepted; rule-2 carve-out resolved; e0
  opened.**
  - (d) and (e) accepted by the user in-session; CLAUDE.md status
    updated. Execution order: **e0 first**; order beyond e0 decided at
    the PROPOSAL-e §7 gate.
  - **Rule 2 amended (user decision, narrow carve-out):**
    temperature-sampled steered generation may use the cached O(T) path
    behind the per-state next-token-KL gate (≤ 1e-3 nats, both
    directions), **re-validated per direction family and dose** (rule-1
    spirit — the gate was validated on strain states; the reward axis is
    a new family). Greedy readouts and any generation feeding a choice
    DV stay on the uncached path.
  - Correction to the earlier 08-08 flag's cost note: strict rule 2 does
    **not** cost ~8× on (d) distillation data-gen — PROPOSAL-d §1 takes
    activation targets from single teacher forwards over fixed text (no
    generation loop; the full-sequence kernel is the validated one either
    way). The carve-out's practical payoff is e2's steered sampled
    session loops.
  - workspace-layer attribution fixed in CLAUDE.md. Precise fact:
    `WORKSPACE_LAYERS` is defined in `workspace_layers.py`;
    `fingerprint.py` does **not** import it (its capture functions take
    layers as parameters); `eval_awareness.py` is the module that imports
    it. The earlier flag's "(fingerprint imports it)" was wrong.

- 2026-08-08 — **cycle-3 doc verification flags (from the restructure's
  full read of CLAUDE.md v2; flagged for discussion, not applied):**
  - **Ledger rule 2 is stricter than the r2/r3 record it cites.** The rule
    says "use the validated O(T²) uncached path whenever high-norm steering
    is active," but r2/r3 sampled data-gen ran the cached-ops path behind a
    per-state next-token-KL gate (≤ 1e-3 nats, both directions) — sound
    because the near-tie argmax flip motivating the rule is greedy-specific
    and irrelevant under temperature sampling. Decide whether rule 2 gets
    that carve-out (sampled generation + KL gate ⇒ cached-ops allowed); the
    strict reading costs ~8× wall-clock on any (d) distillation data-gen.
  - Minor: the Environment note attributes the workspace-layer set to
    `fingerprint.py`; it is defined in `workspace_layers.py` (fingerprint
    imports it).

- 2026-08-07 — **cycle-3 reset:** cycles 1–2 archived at tag
  `cycle-2-close`; operative docs = CLAUDE.md (v2) + PROPOSAL-d +
  PROPOSAL-e; FINDINGS-2.md is the cycle-2 synthesis.
