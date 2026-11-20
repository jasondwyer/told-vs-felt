# n_analyze.py v7, ADDENDUM-n3's gate in VERDICTS and the tile (R12), F5 and R13 on n-build's delta: the blind review, its mutants and the dispositions (PI date 2026-11-20)

Code's raw for the entry `n package — scripts/n_analyze.py v7: the tile (R12), F5 and R13 followed on n-build's delta
(ef105f1), the seat's rulings on v6's readings carried in, and ADDENDUM-n3's gate in VERDICTS`.

- **What changed under review.** The draft is compared against the committed analyzer (`1185e15`, sha256
  `418c2136…072d`). It carries:
  - ADDENDUM-n3 v0.1 (`7f4a7a75…9313`, committed at `0744136`) §3.3–§3.5, with the second sitting's §2.5
    (`results/raw/2026-11-19_n-gvec-stop-lock-opens_design-to-code_answers.md`, sha256 `887b7646…dc87`, committed at
    `f4b3e73`): N2's decision point under the reward axis's 5(d) gate, §7.3's report line, the lock's gate line, and
    the pinned map's reach under both gate branches (PIN-n-40 to PIN-n-42), the addendum bound by sha256;
  - the schema pin moved to n-build's R12, F5 and R13 delta at `ef105f1` (`1cab28df…edff`): a standing pause's batch
    bound to the runner's tile, F5's fixtures, R13's texts;
  - the first sitting's §4 (`results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md`, sha256
    `e6ff066d…6d5a`, committed at `a33252a`): PIN-n-37 (a)–(c), PIN-n-38 and PIN-n-39 as ruled.

  The ADDENDUM-n3 part was drafted in scratch from `db00d6d`, in parallel with n-build's delta, on the coordinating
  session's word of 2026-11-20 (the entry declares it). Its first draft ran once in a battery window (239/241, the
  code forms' digest still v6's, as expected); the delta's parts were written against `ef105f1` as committed, and
  draft 3 ran once: 242/242.
- **The review, blind** (§1). A reviewer read draft 3's run copy, frozen read-only at sha256 `309a1c43…926a`
  (242/242 on those bytes, every one of its 246 coverage ids reached), against the base and the diff.
  - It was a subagent of this session. Its brief (sha256 `97e7cc10…a496`) quoted the list of record v2's items 1–5
    with item 4's two amendments (C.2 of 2026-11-16, and the fourth sitting's §6.2), and the standing lines: item 3's
    pathspec with `':!data/mf3/**'`, even for a named file; no guard marker in any command's arguments; a glob
    expanded and read before it is looped over; no listing of `results/raw`; a tracked-and-clean check by `rev-parse`
    against `hash-object`. It allowed no interpreter but `shasum`.
  - Its specification: ADDENDUM-n3 §3 and §8.3 (4); the second sitting's §2.5 and §8 item 5, and the PI's routings of
    the second and third sittings; the referent check's observations 3 and 4 and their dispositions; the first
    sitting's §3 and §4 and its routing; the entries of `1185e15`, `ef105f1` and `db00d6d`; PROPOSAL-n v0.2 §5 and
    §7.3; ADDENDUM-n1 §5.1, §5.3 and §7.6; `valence_core/n/schema.py` and `valence_core/n/runner.py` at `ef105f1`.
  - It ran no Python and no repository code. Its report lists what it ran beyond reading files (§1, its last part):
    two `awk` line filters, which its brief's "no interpreter" bars, and one `sed -n` print over the frozen copy,
    `/usr/bin/grep` and `wc -l` over named files, a `while read` loop over a patterns file it wrote under its own
    folder, and name-only `ls` of the review folders. It ran no git command and opened nothing under `data/`.
  - It returned:
    - production findings F1–F4: F1 MINOR, F2–F4 NOTEs, no MAJOR;
    - battery findings B1–B8: B1–B4 MINOR, B5–B8 NOTEs;
    - 41 mutants, V01–V41. It predicted that 11 would survive the frozen copy (V07, V08, V14, V15, V28, V33, V34, V36,
      V37, V38 and V39).
- **The dispositions** (§2). Every finding is taken; draft 4 carries them, with one battery case of Code's own (a
  tail of one read), found while Code drafted its mutants, and draft 5 carries SENT-CODE-FORMS' description (F4's
  last point, applied at the values-check).
- **The mutants** (§3). The reviewer's 41, less V33 (moot: F3's disposition removes its line), V37 re-expressed on
  draft 4's scope check, and nine of Code's: 49. They ran once each, on draft 4's run copy (sha256 `9cf85798…3a91`,
  242/242, every one of its 246 coverage ids reached): **47 of 49 killed.** V28 and V38 survived, as the reviewer
  predicted: V28 by design, V38 on a fixture the values-check corrected (§3). The other eight it predicted would survive
  that ran are killed, each by a case the dispositions added.
- **The battery runs** (§4) and **the committed bytes** (§5). The committed file differs from the mutation-tested base
  in the repository line, one fixture's read (the values-check's R41) and seven text regions (§5).
- **The tallies** (§6).

Every Python run here was inside a battery window the coordinating session granted, on bytes named to it first by
sha256. Each ran as one process at a time, at `nice -n 19` with `-I -B`, with its temp folders in Code's scratch, in
the foreground. The interpreter was reached by `cd` into the venv's bin by glob, in a subshell, so no argv named its
path. Nothing ran on a model or on the box.

Each mutant was applied to a copy of its base as an exact text replacement (`.old` → `.new`), asserted to occur once
and to change the file. Before the mutants ran, the base's, the runner's and the manifest's sha256 were named to the
coordinating session, which checked them, read the runner whole and checked each mutant's changed lines. "Killed"
means a non-zero exit.

## 1. The reviewer's report, as saved from its hand-back (unedited)

The report is reproduced whole, as the reviewer's hand-back message gave it, taken from the subagent's transcript by
`jq`, the hand-back's message only (sha256 `d0dad6c2…3b06` as saved). It names Code's scratch folder and the
repository by description, as its brief asked.

## What checks out

**Inputs.** The brief, the frozen copy, the base and the diff each hash to the value given. In REPO:
- `ADDENDUM-n3-…-v0_1.md` hashes to `ADDENDUM3_SHA256` (7f4a7a75…9313, the third sitting's routing figure).
- `valence_core/n/schema.py` hashes to `SCHEMA_SHA256` (1cab28df…edff, ef105f1's figure per its entry).
- `runner.py` hashes to 9bf75cbb…d61e.
- `ADDENDUM3_REL` is in `BOUND_RELS`, in VERDICTS and the secondary (through `base`), in `not_run_doc` and in `ganl_artifact`.
- `gcal.json` is read nowhere.

**Item 1 (N2's decision point).** `n2_reasons`/`n2_decision_f` give f = 0.20 iff the gate is PASS and 2·d_eq ≤ 1, else f = 0.10, with the reasons in §3.4's order ('gate', 'cap', or both). Any other gate value is refused.
- No production caller has a default: `map_reach` and `build_state` take the gate keyword-only.
- `n2_outcome`, `outcomes()["gread"]["E"]` and `gread_table` all read `st.gate.result`.
- Points are the kept (resolved) points, with `match_ratio` printed: shape (c) under FAIL gives 0.5/0.98 and 1.0/0.98. The cap with FAIL and the d_eq = 0.5 edge are also right.

**Item 2 (the lock's gate line).** `lock_gate` reads one whole stripped line.
- A line counts as the gate's if it starts with the head without its trailing space, so a line missing the space is counted and then refused.
- The count must be ASCII decimal, with no leading zero, 0–48; PASS iff k ≥ 36.
- The reconstruction test closes the missing-space case. The leakage line is not counted.
- The refusals are those PIN-n-40 lists. On the frozen copy I found no lock text that passes wrongly.

**Item 3 (§7.3's line).**
- `[why]` is Code's clause around §3.4's words. `addendum3_spans` parses correctly (2 italic spans, 2 reasons, the bar).
- INDETERMINATE names f, and `fill` STOPs on an f and reasons that disagree.
- The template sentence sets are unchanged in number (385 tuples, 2,561 evaluations, T1–T10). The gate enters only as a fill, as [f] and the cap already did. That meets §3.5's "one sentence set per tuple" under reading (d), which is declared.

**Item 4 (reach).** `coupling_shape` equals the old classification under PASS; under FAIL it gives (b), or (d) where d_eq's point is +1. The battery and `run_ganl` cover both branches.

**Item 5 (the tile).** `report_problems` binds a standing fire exactly as the runner at ef105f1 writes it (`Monitors.observe`/`evaluate`/`pending`, and `run()`'s refusal of anything but reads 0..M−1):
- at a read L: (L−cad+1, L);
- at the run's end: ((m//cad)·cad, m−1);
- n counts records with a fidelity block, non-finite ones included; k counts `exceeds_tau is True`;
- the scope must hold the tile's trial arms.

No `cleared` remains, so no ruling moves a range. Given check_report's form, the checks that can fire alone are the tail's end, n, k and the scope. These cannot:
- the bounds of a fire at a read;
- the tail's start (it is the only multiple of the cadence in the last cad reads once the end is m−1);
- `lo_w % cad != 0`, which never fires.

**Item 6 (F5).** The fixtures come from `example_identity` (p0 1 of 26), the batches from `example_pause(identity=…)`, and the schema refuses 0 of 2400 with "(F5)".

**Item 7 (registers).**
- PIN-n-37 quotes §4 (a) and (b) verbatim. (c), PIN-n-38 "accepted as read" and PIN-n-39's both-ways / one-way binding match §4 and the first sitting's item 6. The interim is rightly not built, since ef105f1 carries the tile.
- PIN-n-40 to -42 and OPEN-Q7's extension agree with §3.3–§3.5, the second sitting's §2.5 and item 5, and the third sitting's items 1 and 6.
- Readings (a) and (b) answer referent-check observations 3 and 4, as their dispositions asked. (c), (d) and the v0.1/v1.0 reading are consistent; the last is fail-closed.

**Item 8 (the battery).** 242 checks = 230 + 12; 246 coverage ids by my count (233 + 13). The listed checks test what they claim, except as below.

## Findings — production

**F1 — MINOR — `report_problems`, lines 6326–6358 (with `paused_points` 6439 and `paused_from` 6416–6418).** A standing pause's read and scope are bound one way only, and this is pre-existing.
- `q["launch_index"]` is never checked against the record of `q["read_id"]`. Yet the tile is computed from the launch index (6326–6327), while `paused_points` adds the read's own point.
- The scope only has to hold the tile's trial arms; the schema adds the read's arm. A larger scope passes, and `paused_from` makes every arm in it INDETERMINATE.
- Failure scenario: under PI-STOP, a standing fidelity-binomial pause at launch_index m−1 (a valid tile) names `read_id` N1-V|valence|+1|floor_b0/3, which is on disk at another index. Both check_report and report_problems accept it. `paused_points` then marks (N1-V, +1). On shape (c) under PASS, N2 is decided at f = 0.20 against +1, so N2 becomes INDETERMINATE (pause:N1-V) although that read never fired. A scope inflated to N4's arms likewise makes N4 "no read obtained". The runner writes neither.
- Fix:
  - For a pause whose read is on disk, require `camp.records[rid]["launch_index"] == q["launch_index"]`.
  - For a standing pause, require the runner's SCOPE exactly: the read's arm, plus the tile's trial arms, plus, for a shadow read, the session's paired steered arms taken from the plan.
  - That would also refuse fixture B (see B5).

**F2 — NOTE — `lock_gate`, lines 6199–6203.** Every line anywhere in the lock that starts with the head counts as a gate line. A definitional line ("…coherence: k of 48, PASS or FAIL"), or G-CAL-n's printed line quoted in a code block beside the line of record, gives "2 found" and VERDICTS refuses. This is fail-closed, not a wrong pass. The lock's text should be coordinated with n-build, or this stated in PIN-n-40.

**F3 — NOTE — `report_problems` docstring 6274–6280, and line 6329.**
- "Four checks here cannot fire alone" leaves out the disjunct `lo_w % cad != 0`, which can never fire: the tail's lo_w is always a multiple of the cadence, and a fire at a read must equal the report's first, which check_report already holds to one. It also leaves out the tail's start.
- Drop the disjunct or list it.

**F4 — NOTE — texts.**
- PIN-n-40 (2798) cites "§3.4 (i) and §3.5's 'LOCK-n v0.1's gate line'". The phrase is §3.4 (i)'s; §3.5 says "the lock's gate line".
- PIN-n-40 (2802) and the `lock_gate` docstring (6193) quote "from a gcal.json whose status is PASS"; the addendum has backticks around `gcal.json`.
- In the `lock_gate` docstring, "VERDICTS refuses (the default)" is unclear.
- "Agreed through the coordinating session, PI date 2026-11-19" and "n-build: it fills v0.1's hole and carries into v1.0" cannot be checked from the named sources.
- The analyzer cannot detect a v1.0 gate line that differs from v0.1's. That residue belongs to the v0.1/v1.0 reading put to the seat.
- `code_forms()` and SENT-CODE-FORMS call GATE_LINE_HEAD, a parse head, a "sentence form".

## Findings — battery

**B1 — MINOR — LOCK-GATE, 5436–5459.** No case exercises the reconstruction test.
- Every bad case is refused by some other condition, so dropping the test survives (V07). Without it, "…coherence:30 of 48, FAIL" (no space) is read as 0 of 48 FAIL, and "…coherence:136 of 48, PASS" as 36 PASS.
- There is also no two-line case where one line lacks the space, so V08 survives.
- Fix: add bad cases for a missing space, a tab after the colon, and a good line beside a no-space line.

**B2 — MINOR — VD-GATE, 5420–5433.** The gate goes through `run_verdicts` once, under FAIL with the cap binding, and only the primary is checked.
- Neither the TAU/4 row's nor the second row's gate is checked (V14, V15 survive).
- No VERDICTS run has the gate's FAIL alone. On a map without the cap, a row built under PASS would decide its N2 at f = 0.20.
- Fix: run a FAIL lock on the example map (no cap), and assert f = 0.10 with reasons ['gate'] and the gate document in the primary and in the TAU/4 row.

**B3 — MINOR — the standing tiles in VD-PAUSE-POINTS (A–C), VD-BATCH-CLEARS and VD-CEILING's D.** Every read in a standing tile is above both TAU and TAU/4 or above neither (shifts of 0.1, 0.30, or none). So k counted at TAU/4 survives (V34). Fix: put a TAU/4-only read (a 0.015 shift, as in the main campaign) in a standing tile and assert k.

**B4 — MINOR — R13's own case has no fixture.** No adjudicated pause's read lies inside a standing tile: the rulings at 808, 5919, 6399 and 7199 all sit in earlier tiles. A mutant that drops ruled reads from the tile's trials therefore survives (V36). VD-CEILING's D cites R13 (5195–5196), but its read is the standing pause's own. Fix: place an adjudicated ceiling pause, rel above TAU, inside the tile that fires later; assert it counts in n and k, and refuse a report that leaves it out.

**B5 — NOTE — `fired()`, 5045–5058; pb at 5080; pc at 5085–5086.** Two fixtures are not quite the runner's reports. Neither changes what the checks assert, since points come from `paused_points` and N2 reads them point by point.
- Fixture B's pause sits on a shadow read with scope ["N1-V"]. The runner's SCOPE adds the session's paired steered arms (N1-P, N2-E, N2-S, N2-C for neutral session 159), so B is not a report the runner writes.
- In C, the non-finite d = 0 read's identity block is `within: False`, so the runner would also fire identity-bound. The fixture lists only nonfinite and fidelity-binomial (a pre-existing pattern).

**B6 — NOTE — `paused_points` 6442–6443; RD-PAUSE-POINTS 4276–4333.** In every tile, each point has more than one read, so an off-by-one at the range's ends survives (V39). A one- or two-read tail at a cell boundary would separate it.

**B7 — NOTE — launch order (`_bt_write_campaign` 3794; comment 4270–4272).** The battery writes in `plan_cells` order: N1-V's steered cells first, then the shadows at 800–959. The runner's ORDER PIN puts the shadows first, at 0–159, so B's "shadows' tile" is not a tile the runner's order produces. The analyzer is order-agnostic, so nothing it decides changes; the fixtures' "as the runner writes" claim holds for the tiles' form only.

**B8 — NOTE — smaller gaps.**
- N2-GATE-INDET (1632–1639) checks the gate document on `ie` only, not `iv`.
- Every standing tile covers one arm, so the scope test written with `&` instead of `<=` survives (V37). On runner-written reports the tiles are arm-aligned, so this is near-equivalent.
- Adjudicated batches are unchecked by design (V38 survives, and would be stricter).
- `cad` hard-coded to 160 would survive: every fixture uses 160.
- `run_ganl`'s STOP across both branches is never exercised, by design (V28).

## Mutants

```
@@ V01 | DoseMap.n2_reasons | the gate's FAIL never decides (cap alone) | predicted: killed by NUM-GATE-DECISION-F, N2-GATE-F10
        return tuple(r for r, on in (("gate", gate == "FAIL"), ("cap", self.cap_binds())) if on)
~~
        return tuple(r for r, on in (("cap", self.cap_binds()),) if on)
@@ V02 | DoseMap.n2_reasons | both reasons out of §3.4's order | predicted: killed by NUM-GATE-DECISION-F, N2-GATE-F10, VD-GATE
        return tuple(r for r, on in (("gate", gate == "FAIL"), ("cap", self.cap_binds())) if on)
~~
        return tuple(r for r, on in (("cap", self.cap_binds()), ("gate", gate == "FAIL")) if on)
@@ V03 | DoseMap.n2_reasons | a gate result not PASS/FAIL read as PASS | predicted: killed by NUM-GATE-DECISION-F (its refusals)
        if gate not in GATE_STATES:
~~
        if gate is None:
@@ V04 | DoseMap.n2_decision_f | decision by the cap alone | predicted: killed by N2-GATE-F10, N2-GATE-DECIDES
        return F10 if self.n2_reasons(gate) else F20
~~
        return F10 if self.cap_binds() else F20
@@ V05 | Gate.__post_init__ | PASS needs k > 36 | predicted: killed by LOCK-GATE (36 PASS: group raises)
        if self.result not in GATE_STATES or (self.result == "PASS") != (self.k >= GATE_BAR):
~~
        if self.result not in GATE_STATES or (self.result == "PASS") != (self.k > GATE_BAR):
@@ V06 | Gate.__post_init__ | k above 48 accepted | predicted: killed by LOCK-GATE ("49")
        if not (type(self.k) is int and 0 <= self.k <= GATE_N):
~~
        if not (type(self.k) is int and 0 <= self.k):
@@ V07 | lock_gate | no whole-line reconstruction ("coherence:30 of 48, FAIL" read as 0 FAIL) | predicted: survives
    if not (sep and digits and result in GATE_STATES and lines[0] == f"{GATE_LINE_HEAD}{k_s}{sep}{result}"):
~~
    if not (sep and digits and result in GATE_STATES):
@@ V08 | lock_gate | a no-space line beside a good one not counted | predicted: survives
    head = GATE_LINE_HEAD.rstrip()
~~
    head = GATE_LINE_HEAD
@@ V09 | lock_gate | leading zero accepted | predicted: killed by LOCK-GATE ("leading zero")
    digits = bool(k_s) and all(c in "0123456789" for c in k_s) and (k_s == "0" or not k_s.startswith("0"))
~~
    digits = bool(k_s) and all(c in "0123456789" for c in k_s)
@@ V10 | lock_gate | two gate lines accepted | predicted: killed by LOCK-GATE ("twice"), VD-REFUSE (lock-two-gates)
    if len(lines) != 1:
~~
    if not lines:
@@ V11 | lock_gate | lines not stripped | predicted: killed by LOCK-GATE ("padded")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip().startswith(head)]
~~
    lines = [ln for ln in text.splitlines() if ln.startswith(head)]
@@ V12 | lock_gate | result recomputed, not refused, against the bar | predicted: killed by LOCK-GATE, VD-REFUSE (lock-gate-bar)
        return Gate(int(k_s), result)
~~
        return Gate(int(k_s), "PASS" if int(k_s) >= GATE_BAR else "FAIL")
@@ V13 | run_verdicts | the lock's gate never read | predicted: killed by VD-GATE, VD-REFUSE (lock-gate cases)
    gate = lock_gate(ltext)
~~
    gate = GATE_FIXTURE["PASS"]
@@ V14 | run_verdicts | TAU/4 row decided under PASS whatever the lock | predicted: survives
    st_s, fig_s = build_state(camp, paused=paused, gread=g, drop=tau4_drop(camp), paused_at=pat, gate=gate)
~~
    st_s, fig_s = build_state(camp, paused=paused, gread=g, drop=tau4_drop(camp), paused_at=pat, gate=GATE_FIXTURE["PASS"])
@@ V15 | run_verdicts | second row decided under PASS | predicted: survives
                                  emptied="median-emptied", gate=gate)
~~
                                  emptied="median-emptied", gate=GATE_FIXTURE["PASS"])
@@ V16 | outcomes | N2's label input read at f = 0.20's cell | predicted: killed by N2-GATE-GREAD
           "E": st.gr("span_reward", st.dmap.n2_decision_f(st.gate.result))}
~~
           "E": st.gr("span_reward", st.dmap.n2_decision_f("PASS"))}
@@ V17 | n2_outcome | decision f ignores the gate, reasons follow it | predicted: killed by N2-GATE-F10, N2-GATE-DECIDES
    f_dec = st.dmap.n2_decision_f(st.gate.result)
~~
    f_dec = st.dmap.n2_decision_f("PASS")
@@ V18 | n2_outcome | outcome records a PASS gate | predicted: killed by N2-GATE-F10, N2-GATE-INDET, VD-GATE
    why = {"f": f_dec, "reasons": list(st.dmap.n2_reasons(st.gate.result)), "gate": st.gate.doc()}
~~
    why = {"f": f_dec, "reasons": list(st.dmap.n2_reasons(st.gate.result)), "gate": GATE_FIXTURE["PASS"].doc()}
@@ V19 | n2_outcome | INDETERMINATE carries no reasons | predicted: killed by N2-GATE-INDET, SENT-FILLED-N2-GATE
        return {"state": "INDETERMINATE"} | why | {"causes": causes}
~~
        return {"state": "INDETERMINATE", "f": f_dec, "reasons": [], "gate": st.gate.doc(), "causes": causes}
@@ V20 | fill | f and reasons not cross-checked | predicted: killed by SENT-FILLED-N2-GATE (its STOPs)
        if rs not in ([], ["gate"], ["cap"], ["gate", "cap"]) or bool(rs) != (n2["f"] == F10):
~~
        if rs not in ([], ["gate"], ["cap"], ["gate", "cap"]):
@@ V21 | fill | [why] never filled | predicted: killed by SENT-FILLED-N2-GATE, SENT-FILLED-N2-CAP, VD-GATE
        sub.update({"[f]": F_TEXT[n2["f"]], WHY_SLOT: why_text(n2["reasons"])})
~~
        sub.update({"[f]": F_TEXT[n2["f"]], WHY_SLOT: ""})
@@ V22 | why_text | both reasons joined by a comma | predicted: killed by SENT-ADDENDUM3, SENT-FILLED-N2-GATE
    return "" if not rs else N2_WHY.format(reasons=" and ".join(words[r] for r in rs))
~~
    return "" if not rs else N2_WHY.format(reasons=", ".join(words[r] for r in rs))
@@ V23 | why_text | reasons out of order or repeated accepted | predicted: killed by SENT-ADDENDUM3
    if rs not in ([], ["gate"], ["cap"], ["gate", "cap"]):
~~
    if any(r not in ("gate", "cap") for r in rs):
@@ V24 | C_N2 | INDETERMINATE's line loses [why] | predicted: killed by SENT-ADDENDUM3 ('slot'), SENT-CODE-FORMS
        "INDETERMINATE": N2_HEAD + "INDETERMINATE: N2 is not evaluated at f = [f][why] ([causes])"}
~~
        "INDETERMINATE": N2_HEAD + "INDETERMINATE: N2 is not evaluated at f = [f] ([causes])"}
@@ V25 | coupling_shape | shape (b) by the cap alone | predicted: killed by REACH-GATE-FAIL, NUM-REACH-CLASS
    if dmap.n2_decision_f(gate) == F10:
~~
    if dmap.cap_binds():
@@ V26 | map_reach | FAIL branch's states carry a PASS gate | predicted: killed by REACH-GATE-FAIL
    g = GATE_FIXTURE[gate]
~~
    g = GATE_FIXTURE["PASS"]
@@ V27 | pinned_map_reach | FAIL branch not reported | predicted: killed by NUM-REACH-CLASS (group raises), STR-GANL-ARTIFACT
    for gate in GATE_STATES:
~~
    for gate in ("PASS",):
@@ V28 | run_ganl | reach STOP only if both branches fail | predicted: survives
    if dmap is not None and any(x["raised"] or not x["dose_iff_n1"] or not x["agrees_with_hand"]
~~
    if dmap is not None and all(x["raised"] or not x["dose_iff_n1"] or not x["agrees_with_hand"]
@@ V29 | build_state | reader's state ignores the lock's gate | predicted: killed by RD-GATE-FAIL, VD-GATE
    st = State(dmap=dmap, gate=gate, complete={a: camp.usable(a) and a not in unusable for a in ARMS},
~~
    st = State(dmap=dmap, gate=GATE_FIXTURE["PASS"], complete={a: camp.usable(a) and a not in unusable for a in ARMS},
@@ V30 | report_problems | tail ends at the last trial (v6) | predicted: killed by VD-BATCH-CLEARS
            lo_w, hi_w = (((m // cad) * cad, m - 1) if q["read_id"] is None
~~
            lo_w, hi_w = (((m // cad) * cad, max(r["launch_index"] for r in camp.records.values() if r["fidelity"] is not None)) if q["read_id"] is None
@@ V31 | report_problems | tail bounds taken from the report | predicted: killed by VD-BATCH-CLEARS, VD-REFUSE (batch-end)
            lo_w, hi_w = (((m // cad) * cad, m - 1) if q["read_id"] is None
~~
            lo_w, hi_w = ((b["first_launch_index"], b["last_launch_index"]) if q["read_id"] is None
@@ V32 | report_problems | a fire at a read's tile one read too long | predicted: killed by VD-PAUSE-POINTS, VD-CEILING
                          else (q["launch_index"] - cad + 1, q["launch_index"]))
~~
                          else (q["launch_index"] - cad, q["launch_index"]))
@@ V33 | report_problems | multiple-of-cadence disjunct dropped | predicted: survives (equivalent)
            if (b["first_launch_index"], b["last_launch_index"]) != (lo_w, hi_w) or lo_w % cad != 0 \
~~
            if (b["first_launch_index"], b["last_launch_index"]) != (lo_w, hi_w) \
@@ V34 | report_problems | k counted at TAU/4 | predicted: survives
                    or (len(ins), sum(r["fidelity"]["exceeds_tau"] is True for r in ins)) != (b["n"], b["k"]):
~~
                    or (len(ins), sum(r["fidelity"]["exceeds_tau4"] is True for r in ins)) != (b["n"], b["k"]):
@@ V35 | report_problems | non-finite re-computation not a trial | predicted: killed by VD-PAUSE-POINTS (C), VD-REFUSE (batch-read-count)
            ins = [r for r in camp.records.values() if r["fidelity"] is not None and lo_w <= r["launch_index"] <= hi_w]
~~
            ins = [r for r in camp.records.values() if r["fidelity"] is not None and r["fidelity"]["finite"] and lo_w <= r["launch_index"] <= hi_w]
@@ V36 | report_problems | a ruled pause's read leaves its tile (R13) | predicted: survives
            ins = [r for r in camp.records.values() if r["fidelity"] is not None and lo_w <= r["launch_index"] <= hi_w]
~~
            ins = [r for r in camp.records.values() if r["fidelity"] is not None and lo_w <= r["launch_index"] <= hi_w
                   and r["read_id"] not in {p_["read_id"] for p_ in rep["pauses"] if p_["adjudicated"]}]
@@ V37 | report_problems | scope need only meet the tile's arms | predicted: survives
            if not {r["arm"] for r in ins} <= set(q["arms_in_scope"]):
~~
            if not {r["arm"] for r in ins} & set(q["arms_in_scope"]):
@@ V38 | report_problems | adjudicated batches bound too (stricter) | predicted: survives
        if b is not None and not q["adjudicated"]:
~~
        if b is not None:
@@ V39 | paused_points | tile's last read left out of the range | predicted: survives
                           if b["first_launch_index"] <= r["launch_index"] <= b["last_launch_index"])
~~
                           if b["first_launch_index"] <= r["launch_index"] < b["last_launch_index"])
@@ V40 | paused_points | only a read-less fire extends to its tile | predicted: killed by VD-PAUSE-POINTS (B: 15 points, not 20)
        if b is not None:
~~
        if b is not None and q["read_id"] is None:
@@ V41 | paused_points | adjudicated binomial pause still stands | predicted: killed by VD-PAUSE-POINTS (A: N1-P@-1 added)
        if q["adjudicated"]:
~~
        if q["adjudicated"] and q["binomial"] is None:
```

## Commands that a rule in the brief might bar

- Two `awk -F: '$1>N'` line-number filters over `grep -n` output of the frozen copy in SCRATCH. awk is an interpreter, so this breaches "no interpreter at all".
- One `sed -n` line-range print of the frozen copy. Stated in case sed counts as an interpreter.
- `/usr/bin/grep -n` searches over named repository files only: RESULTS.md, `valence_core/n/schema.py`, `valence_core/n/runner.py`, and `results/raw/2026-11-19_addendum-n3_referent-check.md`. None was a tree or git search, and none touched `data/`.
- `wc -l` (line counts) on named repository files and on the three SCRATCH files.
- A `while read` loop of `/usr/bin/grep -c -F [-x] -e <line>` over the frozen copy. Its lines came from the one file I wrote, `SCRATCH/review/reviewer/patterns.txt`; I checked that none holds a marker.
- Name-only `ls` of `SCRATCH/review` and `SCRATCH/review/reviewer`.

`shasum -a 256` was used as allowed. I ran no git command. Nothing under `data/` was listed, read or searched, `results/raw` was not listed (named files were read with the Read tool), no marker was in any argv, and no model process was started.

## 2. Code's dispositions

Every finding is taken. Draft 4 (sha256 `7cc0c78f…10be`) carries them all but F4's last point, SENT-CODE-FORMS'
description, which draft 5 carries (applied at the values-check).

### Production code

- **F1 (MINOR), a standing pause's read and scope bound one way.** Applied, both halves.
  - A pause whose read is on disk must name it at its own launch index: `report_problems` refuses "its read is on
    disk at launch index N, not the pause's". The runner writes a pause at its read's launch index, a resumed
    rendering pause's read being launched at its own place.
  - A standing pause's scope must equal the runner's SCOPE at `ef105f1` (its pin SCOPE; `_scope`): new
    `runner_scope` gives the read's arm, the arms with a trial in its tile where the binomial fired, and, for a
    shadow, every arm with a steered read of that session in the plan; a fire at the run's end, its tile's trials'
    arms alone. `report_problems` refuses "its scope is not the runner's". An adjudicated pause's scope is not
    checked, as its batch is not: no outcome reads them.
  - Two refusal cases join VD-REFUSE (a read on disk at another index; a scope with N4's arms added), and the
    batch-scope case's message is the new one. PIN-n-37's binding text says both, flagged as Code's for the seat.
- **F2 (NOTE), every head line counts.** Stated in PIN-n-40: the lock carries the line once, and a lock with a second
  line of its own beginning with the head, a quotation of the line or its form, is refused, two being found; a
  quotation inside another line, or blockquoted, is not read (draft 5's wording, from the values-check). The
  coordinating session had already checked n-build's lock draft for one such line; nothing else is built.
- **F3 (NOTE), what cannot fire alone.** The `lo_w % cad != 0` disjunct, which never fires, is removed, and the
  docstring now names what cannot fire alone: the two shas, the per-arm counts, and, of a standing tile's bounds, a
  fire at a read's both ends and a tail's start.
- **F4 (NOTE), texts.** PIN-n-40 cites §3.4 (i) for "LOCK-n v0.1's gate line" and §3.5 for "the lock's gate line";
  the quotation of §3.5 keeps the addendum's backticks around `gcal.json`; the agreed form is marked as a relay no
  committed text records; the residue the reviewer named (a v1.0 line that differed from v0.1's would be read as
  given) is stated in PIN-n-40; `lock_gate`'s docstring says VERDICTS refuses a lock with no line, finding none;
  `code_forms`' docstring calls GATE_LINE_HEAD a head the reader parses, pinned beside the forms, not a sentence,
  and SENT-CODE-FORMS' description says the same (applied at the values-check, its pass 1).

### The battery

- **B1 (MINOR), LOCK-GATE.** Three bad lines join it, each refused by the whole line's reconstruction alone or by two
  candidates: no space after the head, a tab after it, and a good line beside one missing the space. Eighteen
  refusals now. V07 and V08 are killed.
- **B2 (MINOR), VD-GATE.** A campaign under a lock recording 35 of 48, FAIL, on the example map (no cap), with
  N1-V's +1 reads of runs 79–159 0.015 apart so that the second row is reported: N2 is decided at f = 0.10 by the
  gate alone, with the gate as the lock records it, in the primary, the TAU/4 row and the second row, and its line
  names the gate. V14 and V15 are killed.
- **B3 (MINOR), a TAU/4-only read in a standing tile.** VD-PAUSE-POINTS A's tile now holds two keyed-sample trials,
  one 0.1 apart (above TAU) and one 0.015 apart (above TAU/4 alone): k = 1. V34 is killed.
- **B4 (MINOR), R13's own case.** VD-BATCH-CLEARS' campaign holds a keyed-sample read 0.30 apart inside its tail, a
  ceiling pause adjudicated there before the fire at the run's end: the tail counts it as a trial and an exceedance
  (2 of 2), and a report whose tail leaves it out (1 of 1) is refused. V36 is killed.
- **B5 (NOTE), the fixtures' scope and kinds.** The fixtures' scopes are the runner's (`runner_scope`), and
  VD-PAUSE-POINTS B asserts its shadow's: N1-P, N1-V, N2-C, N2-E, N2-S, a neutral session's arms. C's non-finite
  read, outside the identity bound, now fires nonfinite, identity-bound and the binomial, as the runner would.
- **B6 (NOTE), the range's ends.** RD-PAUSE-POINTS gains a seventeenth case, a tail of one read at a tile's start,
  its point alone: Code's own, found while it drafted its mutants, before the report came. V39 is killed.
- **B7 (NOTE), the launch order.** The comments and VD-PAUSE-POINTS' text say it: the battery's order is plan_cells',
  not the runner's ORDER, and the analyzer reads no order, so the tiles are the runner's in form over the battery's
  order.
- **B8 (NOTE), the smaller gaps.** N2-GATE-INDET checks the gate on both its outcomes. The others stand by design:
  V37's scope test is re-expressed on the new check (§3); adjudicated batches stay unchecked (V38); every fixture's
  cadence is n §2.1's 160; `run_ganl`'s STOP across both branches is reached by no map the battery derives (V28).

### The mutants

The reviewer's 41 ran less V33, whose line F3's disposition removes; V37 is re-expressed on draft 4's scope check.
Code's own twelve were written before the report came. Five the reviewer's duplicate are dropped (C06 = V39, C08 =
V04, C09 = V02, C11 = V09, C12 = V22), C03 is moot with V33, and C05 is re-expressed on the new scope check; three
more cover the new code (C13, the launch-index check; C14 and C15, `runner_scope`'s shadow pairing and tile arms):
49 in all.

## 3. The mutants and their run

- **The base:** draft 4's run copy, `mut/base.py` in Code's scratch, sha256
  `9cf8579813454bf14142e4b07e606c4c21b24ca3bc00a2c2602ba09e08f13a91`. It differs from draft 4 only in its
  repository line, and is 242/242 on its own run, every one of its 246 coverage ids reached.
- **The manifest:** `mut/manifest.txt`, the base, the runner and the 49 files, 51 lines, sha256 `d6d45817…51b4`. The
  coordinating session checked it, read the runner (`mut/run_mutants.sh`, sha256 `60d029dd…c000`) whole, and checked
  each mutant's changed lines, before the base ran.
- **The runs:** the base first, then the mutants three per foreground call (one call of one, the last), the runner
  running each battery in turn. Each run's output is in Code's scratch; the table is built from them by script
  (the results file, sha256 `ad38a3ab…29ff`; the runner's exit list, `5779a4c1…f8fa`, 49 lines).
- **The survivors.** V28 lets `run_ganl` STOP only when both gate branches fail; no map the battery derives breaks
  either branch, so the STOP is never reached (by design, as the reviewer noted). V38 binds adjudicated batches too,
  stricter than the reader. On draft 4 one adjudicated batch was not a tile of the records: VD-REFUSE's fire at
  read 479 on c4, a tile with no trial (N1-V's +d_20 cell), whose case is refused anyway, its expected message among
  the first three, so V38 changed no outcome. The values-check found it (its R41); the final bytes move that fire to
  read 159, the end of N1-V's +1 cell, each of whose 160 reads carries a trial, so every fixture's adjudicated batch
  is now a tile of the records.

| Mutant | Where | What it breaks | Predicted | Result | First FAIL (its description, cut) |
|---|---|---|---|---|---|
| V01 | DoseMap.n2_reasons | the gate's FAIL never decides (cap alone) | killed by NUM-GATE-DECISION-F, N2-GATE-F10 | killed, 231/242 | N2's decision point under the gate (ADDENDUM-n3 §3.4 |
| V02 | DoseMap.n2_reasons | both reasons out of §3.4's order | killed by NUM-GATE-DECISION-F, N2-GATE-F10, VD-GATE | killed, 228/234 | N2's decision point under the gate (ADDENDUM-n3 §3.4 |
| V03 | DoseMap.n2_reasons | a gate result not PASS/FAIL read as PASS | killed by NUM-GATE-DECISION-F (its refusals) | killed, 240/242 | OPEN-Q7 as ruled and ADDENDUM-n3 §3.4 (PIN-n-41): the cap b |
| V04 | DoseMap.n2_decision_f | decision by the cap alone | killed by N2-GATE-F10, N2-GATE-DECIDES | killed, 231/242 | N2's decision point under the gate (ADDENDUM-n3 §3.4 |
| V05 | Gate.__post_init__ | PASS needs k > 36 | killed by LOCK-GATE (36 PASS: group raises) | killed, 233/236 | verdicts: group raised ValueError: the gate's result 'PASS'  |
| V06 | Gate.__post_init__ | k above 48 accepted | killed by LOCK-GATE ("49") | killed, 240/242 | the lock's gate line (PIN-n-40): read whole and stripped, be |
| V07 | lock_gate | no whole-line reconstruction ("coherence:30 of 48, FAIL" read as 0 FAIL) | survives | killed, 240/242 | the lock's gate line (PIN-n-40): read whole and stripped, be |
| V08 | lock_gate | a no-space line beside a good one not counted | survives | killed, 240/242 | the lock's gate line (PIN-n-40): read whole and stripped, be |
| V09 | lock_gate | leading zero accepted | killed by LOCK-GATE ("leading zero") | killed, 240/242 | the lock's gate line (PIN-n-40): read whole and stripped, be |
| V10 | lock_gate | two gate lines accepted | killed by LOCK-GATE ("twice"), VD-REFUSE (lock-two-gates) | killed, 239/242 | the lock's gate line (PIN-n-40): read whole and stripped, be |
| V11 | lock_gate | lines not stripped | killed by LOCK-GATE ("padded") | killed, 233/236 | verdicts: group raised AnlRefusal: REFUSED: the lock does no |
| V12 | lock_gate | result recomputed, not refused, against the bar | killed by LOCK-GATE, VD-REFUSE (lock-gate-bar) | killed, 239/242 | the lock's gate line (PIN-n-40): read whole and stripped, be |
| V13 | run_verdicts | the lock's gate never read | killed by VD-GATE, VD-REFUSE (lock-gate cases) | killed, 238/242 | verdicts on a merged dose map (R_ell 40.0) under a Route A l |
| V14 | run_verdicts | TAU/4 row decided under PASS whatever the lock | survives | killed, 240/242 | verdicts reads the lock's gate line (PIN-n-40) into N2's dec |
| V15 | run_verdicts | second row decided under PASS | survives | killed, 240/242 | verdicts reads the lock's gate line (PIN-n-40) into N2's dec |
| V16 | outcomes | N2's label input read at f = 0.20's cell | killed by N2-GATE-GREAD | killed, 240/242 | N2's label input follows the gate's branch: span_reward's G- |
| V17 | n2_outcome | decision f ignores the gate, reasons follow it | killed by N2-GATE-F10, N2-GATE-DECIDES | killed, 233/242 | N2's decision point under the gate (ADDENDUM-n3 §3.4 |
| V18 | n2_outcome | outcome records a PASS gate | killed by N2-GATE-F10, N2-GATE-INDET, VD-GATE | killed, 238/242 | N2's decision point under the gate (ADDENDUM-n3 §3.4 |
| V19 | n2_outcome | INDETERMINATE carries no reasons | killed by N2-GATE-INDET, SENT-FILLED-N2-GATE | killed, 239/242 | under the gate's FAIL an INDETERMINATE N2 names the points f |
| V20 | fill | f and reasons not cross-checked | killed by SENT-FILLED-N2-GATE (its STOPs) | killed, 240/242 | N2's report line names its deciding point in each state, IND |
| V21 | fill | [why] never filled | killed by SENT-FILLED-N2-GATE, SENT-FILLED-N2-CAP, VD-GATE | killed, 238/242 | N2's sentence where the cap binds (2·0.72 > 1), filled, equ |
| V22 | why_text | both reasons joined by a comma | killed by SENT-ADDENDUM3, SENT-FILLED-N2-GATE | killed, 238/242 | ADDENDUM-n3's words, from its bytes: §3.3's lock form ('rew |
| V23 | why_text | reasons out of order or repeated accepted | killed by SENT-ADDENDUM3 | killed, 240/242 | ADDENDUM-n3's words, from its bytes: §3.3's lock form ('rew |
| V24 | C_N2 | INDETERMINATE's line loses [why] | killed by SENT-ADDENDUM3 ('slot'), SENT-CODE-FORMS | killed, 238/242 | ADDENDUM-n3's words, from its bytes: §3.3's lock form ('rew |
| V25 | coupling_shape | shape (b) by the cap alone | killed by REACH-GATE-FAIL, NUM-REACH-CLASS | killed, 239/242 | reachability under the gate's FAIL (ADDENDUM-n3 §3.4 |
| V26 | map_reach | FAIL branch's states carry a PASS gate | killed by REACH-GATE-FAIL | killed, 239/242 | reachability under the gate's FAIL (ADDENDUM-n3 §3.4 |
| V27 | pinned_map_reach | FAIL branch not reported | killed by NUM-REACH-CLASS (group raises), STR-GANL-ARTIFACT | killed, 235/238 | commands: group raised KeyError: 'FAIL' |
| V28 | run_ganl | reach STOP only if both branches fail | survives | survived, 242/242 |  |
| V29 | build_state | reader's state ignores the lock's gate | killed by RD-GATE-FAIL, VD-GATE | killed, 239/242 | reader path (shape c) under the gate's FAIL (ADDENDUM-n3 §3 |
| V30 | report_problems | tail ends at the last trial (v6) | killed by VD-BATCH-CLEARS | killed, 240/242 | verdicts binds a fire at the run's end to the stage's tail,  |
| V31 | report_problems | tail bounds taken from the report | killed by VD-BATCH-CLEARS, VD-REFUSE (batch-end) | killed, 239/242 | verdicts binds a fire at the run's end to the stage's tail,  |
| V32 | report_problems | a fire at a read's tile one read too long | killed by VD-PAUSE-POINTS, VD-CEILING | killed, 239/242 | verdicts under PI-STOP with a standing tile, bound in the fo |
| V34 | report_problems | k counted at TAU/4 | survives | killed, 240/242 | verdicts under PI-STOP with a standing tile, bound in the fo |
| V35 | report_problems | non-finite re-computation not a trial | killed by VD-PAUSE-POINTS (C), VD-REFUSE (batch-read-count) | killed, 239/242 | verdicts under PI-STOP with a standing tile, bound in the fo |
| V36 | report_problems | a ruled pause's read leaves its tile (R13) | survives | killed, 240/242 | verdicts binds a fire at the run's end to the stage's tail,  |
| V37 (re-expressed) | report_problems | the scope need only meet the runner's (the review's V37, re-expressed on the exact-scope check) | killed by VD-REFUSE (scope-inflated) | killed, 240/242 | verdicts refuses, each by its message (58 cases): a date |
| V38 | report_problems | adjudicated batches bound too (stricter) | survives | survived, 242/242 |  |
| V39 | paused_points | tile's last read left out of the range | survives | killed, 240/242 | reader path: the points a standing pause stands on (PIN-n-37 |
| V40 | paused_points | only a read-less fire extends to its tile | killed by VD-PAUSE-POINTS (B: 15 points, not 20) | killed, 240/242 | verdicts under PI-STOP with a standing tile, bound in the fo |
| V41 | paused_points | adjudicated binomial pause still stands | killed by VD-PAUSE-POINTS (A: N1-P@-1 added) | killed, 239/242 | verdicts under PI-STOP with a standing tile, bound in the fo |
| C05 | report_problems | the scope check dropped (re-expressed on the exact-scope check) | killed by VD-REFUSE (batch-scope, scope-inflated) | killed, 240/242 | verdicts refuses, each by its message (58 cases): a date |
| C13 | report_problems | a pause's read on disk at another launch index accepted | killed by VD-REFUSE (pause-read-index) | killed, 240/242 | verdicts refuses, each by its message (58 cases): a date |
| C14 | runner_scope | a shadow's session's arms left out of the scope | killed by VD-PAUSE-POINTS (B's scope, the five arms) | killed, 240/242 | verdicts under PI-STOP with a standing tile, bound in the fo |
| C15 | runner_scope | a fire's tile's trial arms left out of the scope | killed by VD-BATCH-CLEARS (the tail's scope N2-C) | killed, 228/231 | verdicts: group raised SchemaError: report.pauses[3].arms_in |
| C01 | report_problems | the tail ends one read before the stage's last | killed by VD-BATCH-CLEARS (the tail accepted) and VD-REFUSE (batch-end) | killed, 239/242 | verdicts binds a fire at the run's end to the stage's tail,  |
| C02 | report_problems | a fire at a read's tile starts one read late | killed by VD-PAUSE-POINTS (A, B, C accepted) and VD-CEILING (D) | killed, 239/242 | verdicts under PI-STOP with a standing tile, bound in the fo |
| C04 | report_problems | the tile's exceedances no longer bound | killed by VD-REFUSE (batch-exceedances) | killed, 240/242 | verdicts refuses, each by its message (58 cases): a date |
| C07 | paused_points | the range leaves out its first read | killed by RD-PAUSE-POINTS (a tail of one read) | killed, 240/242 | reader path: the points a standing pause stands on (PIN-n-37 |
| C10 | Gate | the bar at 35 of 48 | killed by LOCK-GATE (35 FAIL; 36 PASS) and SENT-ADDENDUM3 (the bar phrase) | killed, 229/235 | N2's decision point under the gate (ADDENDUM-n3 §3.4 |

## 4. The battery runs

Every run was in a battery window the coordinating session granted, on bytes named to it first by sha256, with the
terms above.

| Run | Bytes (sha256) | Result | Exit | Output (sha256) |
|---|---|---|---|---|
| r1, draft 1's run copy (the parallel start; development) | `71eb884a…87dd` | 239/241: SENT-CODE-FORMS (the forms' digest moved, as expected; set by tool in draft 2) and the coverage check, its one id unreached | 1 | `4fe3b573…5cde` |
| r2, draft 3's run copy (development; the frozen copy) | `309a1c43…926a` | 242/242, 246 coverage ids reached | 0 | `ad969e87…fe50` |
| r3, draft 4's run copy, the mutant base | `9cf85798…3a91` | 242/242, 246 coverage ids reached | 0 | `9196c33e…8582` |
| the 49 mutants | the manifest, `d6d45817…51b4` | 47 killed, 2 survived (V28, V38), 0 not run | 1 for each killed | the results, `ad38a3ab…29ff` |
| the run of record, `scripts/n_analyze.py` | `735da934…a7a8` | 242/242, 246 coverage ids reached | 0 | the self-test raw |

Q-F3's campaign ran on the laptop beside these runs, as the coordinating session's windows allow; by its grants, no
other battery window was open during any of them.

## 5. The committed bytes against the mutation-tested base

The committed file, `scripts/n_analyze.py` (sha256 `735da934272048a795203e8fdef9bfa5a4bde2ba38cdf9ba79d81f313788a7a8`), differs from the mutant base
(`9cf85798…3a91`) in nine change regions, as `diff` counts them:
- the repository line, `REPO = Path(__file__).resolve().parents[1]`, which the committed file computes, as
  every draft does, and the run copies gave as an absolute path;
- VD-REFUSE's fixture `bz`: its fire's read and resumption, 479 and 480, moved to 159 and 160, and its comment (the
  values-check's R41: at 479 the tile, N1-V's +d_20 cell, held no trial; at 159 it is N1-V's +1 cell, each of its
  160 reads a trial). It is the one code change; its case refuses as before, by its read not on disk;
- seven text regions from the values-check's pass 1: SENT-CODE-FORMS' description (the lock line's head beside the
  sentence forms); PIN-n-40 (a quotation of the line on a line of its own counts; one inside another line, or
  blockquoted, does not); VD-CEILING's comment and description for its case D (R12 alone: its ceiling read is the
  standing pause's own, R13's ruled read being VD-BATCH-CLEARS'), in two regions; `ganl_artifact`'s spec (the
  answers of 2026-11-19 it carries); `lock_gate`'s docstring (as PIN-n-40); and `report_problems`' docstring (a
  tail's start fixed by check_report's form once its end is bound).

No mutant's change lies in a region that differs, but one mutant's outcome rests on the moved fixture: V38, which
survived on the base because `bz`'s batch was refused anyway, would meet, at 159, a tile of the records, and so,
by reading (it is not run again), would survive for the reason §3 gives. The repository line runs in every battery
run; at the committed path it computes the root that the run copies' absolute line gave. The forms' digest,
CODE_FORMS_SHA256, is the base's.

## 6. The tallies

The outcome space is unchanged from `1185e15`'s: 385 tuples and 2,561 evaluations, the tuple pass's hand tallies the
same. The deciding branch enters no sentence set: §7.3's reason clause is a slot filled at VERDICTS, as [f] is. The
code forms' digest moved once, at draft 2, with the new and changed forms (ADDENDUM-n3's two reasons, Code's clause
around them and the lock line's head; C_N2's four forms, each gaining [why], INDETERMINATE's also "at f = [f]"):
from `41d0d654…b1da` to `47883844…be4d`, set by tool from run 1's printed digest.
