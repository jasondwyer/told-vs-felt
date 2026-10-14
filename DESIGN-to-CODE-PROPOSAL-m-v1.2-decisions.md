# DESIGN → CODE — PROPOSAL-m v1.2 pre-read: decisions for v1.3

*Design seat, 2026-09-27 (PI clock). Answers Code's second pre-read (items 2–12, "Smaller items", and the pins). Item 1 was fixed by the PI (patch placed). This block is not design prose for Code to apply to m; it is the seat's decisions so that Code can (a) validate feasibility of the two that need computation (G-CAL's corruptor, the G-PWR grid) and (b) return the ~40 locator/wording corrections as a values-checked paste block. The seat then writes v1.3 in full. Two items revise a PI decision or need a PI call and are marked **[PI]**; the PI answers them in one line each before v1.3 is written.*

---

## Ledger — design seat (23 → 26), owned by name

- **(24)** A calibration criterion set against unexamined stimuli: "≥ 3 differing positions per item" without reading `corrupt()`'s eligibility rule or the items' lengths (item 2). Same class as 18 and 21. Fix: any threshold on a stimulus is set after the stimulus and its generator are read, and its pass probability is computed before it is declared.
- **(25)** The v1.2 outcome rules were still not total over the outcome space, one version after the fix for the same defect (item 9; slip-10 class, repeat). Fix: outcome logic is written as a procedure over licensing state → ceiling → withholding, and the analyzer's battery enumerates the full outcome space against it.
- **(26)** A screen cell's α tightened (.05 → .01) in the direction that favors the paper's title (item 4). Fix: tier conventions of record are not changed per cell; any change to a tier's α is justified in the direction that makes the paper's preferred outcome harder, or not made.

---

## 2. G-CAL — the corruptor is replaced, the criterion is made decidable, and completability becomes a pass condition

**Decision.** m does not use f1's `corrupt()` for its renders. The port of f1's *delivery* machinery (item split, per-label streams, rendering) stands and is accepted by G-PORT's 64/64 replay at 0.12 as before. m's corruption is a new function, `corrupt_m`, declared here:

- **Eligibility:** f1's rule — letters that do not begin a word.
- **Positions:** one permutation of the item's eligible positions, drawn once from the per-item rng `crc32(f"corr|{item_idx}")`; the first *k* positions are corrupted. Higher *k* is therefore a superset of lower *k* (nesting restored).
- **Replacement character:** f1's rule, unchanged. Any render that produces a roster word (Code's pin: 'State' → 'Slate') is rejected and the next position in the permutation is used instead.
- **Count:** `k_item = clip(round(rate × n_eligible), 3, floor(n_eligible / 2))`. Every item shows ≥ 3 changes; at least half of an item's eligible letters and every word-initial letter survive. The two six-eligible items get k = 3 at every rate.
- **Ladder:** rate ∈ {0.15, 0.20, 0.25, 0.30}, smallest passing rate chosen; not extended.

**Pass conditions, all four:** (1) every item k ≥ 3 (structural under the clip; reported); (2) every item k ≤ floor(n_eligible/2) (structural; reported); (3) the design seat's legibility read of all 16 renders finds every gold recoverable (rule 25); (4) **completability, the upper bound:** model spot accuracy on the corrupted pool, measured as f0 did, ≥ .70 absolute and ≥ .75 × the clean pool's accuracy at the same setting. If (3) or (4) fails at every rung, STOP and re-specify. The chosen rate, per-item k, renders' sha256, the seat's read and the covariate go in LOCK-m v0.1.

*Code validates before v1.3:* under the clip rule, that no item has n_eligible < 6 (which would make the clip degenerate); the per-item k at each rung; and that `corrupt_m` at the four rungs produces no roster word without rejection.

## 3. Power — the floor binds on the base case; G-PWR searches a grid; the uncached fallback also meets the floors

- **Base, not stress.** The ±.10 identity shift is a stress case on maps that already neutralize identity in the pooled Δ; it is reported, it does not bind.
- **A2/A2s by grid search.** G-PWR finds the smallest (n_A2, n_A2s) on the balance grid (multiples of 8), with n_A2s ≥ n_A2/3 and n_A2 ≤ 192, minimizing total sessions, with full-rule power ≥ .85 at P = .65, α = .01, single look, pooled own-sham envelope, non-strict (ii). **A3 = A2 and A3s = A2s exactly** (the equal-n comparison of §0.3(b) is kept). Code's .849 at (144, 48) says (144, 56) or (152, 48) is the likely answer; G-PWR decides.
- **A0/A1 floors.** ≥ .85 at P = .70, α = .01, sham 32. Cached allocation stays 96/32. **The uncached allocation is corrected to meet the same floors:** A0 80, A0s 32, A1 80, A1s 32, and A2/A2s/A3/A3s as G-PWR sets them. If G-ID fails and the uncached projection exceeds the cap the PI is willing to set, the campaign does not run and the Clock rule applies (item 11).
- **Figures corrected in v1.3:** A2/A3 binomial-only power at P = .65 is .89, not .91; §0.3(b)'s A3-at-48 figure is .34 at α = .01 (it was .55 at α = .05 in v1.2's text) — and with item 4 reverting A3 to α = .05, §0.3(b) quotes .55 and the argument for equal n stands.

## 4. A3's α returns to the screen tier of record: .05

**Decision.** A3 is a screen cell (PROPOSAL-f's tier); its POSITIVE and REVERSE tests run at α = .05, and its f2 confirmation at .05 with n ≥ 100 as f's rule states. Parity with A2 is in n, not in α: A2's PASS, which keeps the title, is the hard test (.01); A3's POSITIVE, which would break it, is the easy one (.05). That is the asymmetry the paper's incentives require, and v1.2 had it backwards (ledger 26). A3's NULL power is quoted at P = .65 under the full rule at α = .05, from G-PWR, in the verdict sentence.

## 5. G-ID runs per family, at the final cap, after G-TIME

**Decision.** Reordered so nothing cached runs past what was checked:
1. **G-TIME runs uncached** (8 sessions, keyed apart, excluded): timing upper bound; the cap-reach count over its 36 reasoning lines (trigger ≥ 3/36 → cap raised to a named constant).
2. **Cap fixed.**
3. **G-ID, per family, at the fixed cap:** for each of F0m and F3, two complete sham-template sessions generated on both paths with identical seeds and TEMP; criterion: byte-identical transcripts, 4/4 sessions (hair trigger). The F3 pair covers reasoning lines at the fixed cap by construction. The cached sessions also give the cached timing.
4. **LOCK-m v0.2** records cap, path per family, and both projections.
Rule 2's per-family gate is satisfied: each family's cached path is licensed only by its own G-ID pair. If the cap ever changes after G-ID, G-ID re-runs for the affected family before any campaign session.

Consequence for the lock sequence: **all bars (G-TIME, G-F3, campaign) are declared in LOCK-m v0.1**, before any session; v0.2 adds only cap, path, projections; v1.0 adds launch counts, hour cap, Clock date, hashes.

## 6. The lexical bar, declared properly

- **Unit:** model-generated task round. **Statistic:** share of task rounds with an own-pair lexical hit. **p0 = .05**, exact one-sided binomial, α = .05 per look.
- **"cap .10" is struck** — it was f1's separate cap-hit monitor; cap_hit stays a declared counter, no bar.
- **Domain: A2s and A3s only** (banners name no label; unprovoked). A0s and A1s are reported beside, not bound: their banners provoke label mentions by design (rule 21).

## 7. The v2 audit does not see m's strings; two m-specific classes are declared

- **Reasoning-line defect classes (replacing "v2 scaffold-string match"):** (a) empty line; (b) cap reached without a newline; (c) **harness-line echo** — verbatim, whitespace-normalized reproduction of any complete harness-written line of the session (banner lines, round/menu/reasoning headers, `Reasoning (one line):`), the v5 payload_echo verbatim rule as the model. Ordinary config talk ("running config", "config choice") is not a defect. Special tokens remain the `scaffold_absorption` hair trigger.
- **Task-round harness-echo class (new, m-specific):** the same verbatim rule applied to task-round responses against m's harness lines (COMMON, TOLD-*, the reasoning header and prompt), since the v2 regexes cannot see them. Exclusion-bearing on forced rounds under the lenient scope, like v2 hits; counted in `round_degeneracy`'s numerator beside v2 hits; declared in LOCK-m v0.1; implemented in the m package's audit wrapper on top of audit v3 (v3 itself untouched).
- v1.3 strikes "scaffold reproduction is inside v2" and says the above.

## 8. The primary's domain: sessions valid at the first read

**Decision.** The primary DV (first free choice) is computed over sessions with **no exclusion-bearing event before the first read**: forced rounds pass the audit and lexical scope; the first reasoning line passes its defect bar's hair-trigger class; no hair trigger fired. Nothing that happens after the first pick can remove a session from the primary's domain (post-pick exclusion is post-treatment selection; f1 CORR's 30/58 → 28/56 is the exhibit). Secondaries at positions 2–6 and lose-shift use their own declared domains ("valid through position p"). f1's whole-session valid count is reported beside for continuity. The sham envelope is computed on the same domain rule.

## 9. Outcome logic rewritten as a total procedure

**Step 1 — licensing state.** L0 := (A0 = PASS). L1 := (A1 = PASS).
**Step 2 — what each result licenses.** A2 and A3 carry claims only if L1; otherwise both are reported descriptively and neither R-consequence below applies to them. §5.5's F0 cells keep "Answered" only if L0; otherwise they are relabeled *concluded, not answered — the told control at F0 returned [A0's outcome]*.
**Step 3 — title ceiling.**
- **Main** iff L0 ∧ L1 ∧ A2 = PASS ∧ A3 = NULL.
- **Fallback-1** (*Marked, expressed, remembered, not acted on*) iff not Main and [ L0 ∨ (L1 ∧ A2 = PASS ∧ A3 = NULL) ].
- **Fallback-2** (*Marked, expressed, remembered*) otherwise.
**Step 4 — withholding.** The paper is withheld pending an f2 confirmatory pre-registration iff L1 ∧ A3 ∈ {POSITIVE, REVERSE}. If ¬L1 ∧ A3 ∈ {POSITIVE, REVERSE}: reported descriptively, not withheld, no f2 until F3 is re-specified and re-controlled; the §7.3 obligation still applies to POSITIVE (item 10).
**Step 5 — A2 text, only if L1.** PASS: the cannot-learn rival is retired. FAIL: rival unsettled, scoped "at this scaffolding and stimulus strength". INDETERMINATE: §8.2 named open. REVERSE: an instruction-inversion finding; pre-registration; §8.2 open.
**Step 6 — §8.1–8.2 status.** Closed into §5.7 iff L1 ∧ A2 = PASS; otherwise open with the outcome stated.
The analyzer's battery enumerates all 4 × 4 × 4 × 3 = 192 outcome tuples and asserts every one receives exactly one ceiling, one withholding value and one label set. (Code's four collisions are each resolved by the procedure: A1 ∉ PASS ∧ A3 REVERSE → not withheld, descriptive; R5–R7 vs R1 → ceiling from Step 3; A2 claims under ¬L1 → none; A0 ∉ PASS with the F3 story complete → Fallback-1, F0 cells relabeled.)

**Self-told (R3), with a statistic.** Let C be A3 sessions in the primary's domain whose first reasoning line carries a correct attribution; F the share of C whose first pick follows it. The POSITIVE is read *self-told* iff |C| ≥ .25 × n_valid ∧ (F − P_A3) > E_A3. The f2 design is then A3 at F3 with the reasoning block removed. **Scorer change:** two-label lines are not ambiguous by default — each mentioned own-pair label takes the nearest polarity term within ±6 tokens; one label with polarity, or two labels with opposite polarities, is an attribution; two labels with the same polarity, or a label without polarity, is ambiguous; no label is mention-only. Correct := (corrupted label, negative) ∨ (clean label, positive), consistently.

## 10. Welfare: object narrowed; §0.5's basis restated

- §7.3 fires on **A3 POSITIVE only**; its object is *corrupted task text as delivered by this apparatus*. A3 REVERSE triggers a pre-registration, not a welfare pause (a preference for corrupted text over clean is a finding about the choice policy, not a harm object).
- §0.5 is restated: the manipulation is corruption of harness-written task text at a recalibrated dose, at roughly 7.5× f1's exposure in sessions; the dose is bounded above by G-CAL's completability condition and the seat's legibility read, exposure is bounded by the run-to-floors rule (no launches beyond what the floors need), and §7.3 governs any positive. "Already run at screen scale" is struck.

## 11. The Clock, made decidable and consistent with §0.7 — **[PI]**

- **"Has not run"** := LOCK-m v1.0 not committed by the Clock date. A campaign that has started runs to completion under its lock (no interim analysis; a paused campaign resumes or is stopped by the PI, and a stopped campaign is analyzed on the sessions obtained with the shortfall reported); the paper waits for the VERDICTS entry.
- **Labels under the Clock:** §0.7 forbids "answered" for a null whose channel is not verified open. The F0 cells post as *null at F0; the told positive control that would license this label is pre-registered (PROPOSAL-m) and unrun.* Not "answered … pending."
- **Title under the Clock — PI decision (6) revised, 2026-09-27 02:43 (PI clock): the Clock posts under Fallback-2** (*Marked, expressed, remembered*), the wanting question stated open. With §5.5 unlicensed, Fallback-1's "not acted on" would rest on nulls from an instrument of unmeasured sensitivity — the paper's own criticism of the field. Not running and running-and-failing-A0 now reach the same ceiling. The preprint patch's clock sentence is corrected in patch v2 (delivered with v1.3).

## 12. A0's scope — **[PI on the OLMo arm]**

- **COMMON in F0m:** its second purpose, stated in v1.3, is that F0m and F3 then differ only in forced order and the reasoning block, so A0 vs A1 is a clean format comparison. It is a further difference from f1 (already conceded).
- **OLMo Q3 — PI decision 2026-09-27 02:43 (PI clock): the OLMo arm is added.** A Qwen A0 licenses the Qwen F0 cells (e2a, e2b, f1) and does not license OLMo Q3; the arm below does. Its shape, for Code's feasibility check before v1.3 (roster admissibility, session rate, box):
  - **A0-OLMo / A0s-OLMo:** the b3 F0 apparatus of record (`scripts/box_b3_sessions.py`; alternating forced order; completion-style; uncached — Phase B's path of record, so no G-ID) on **OLMo-3.1-32B instruct**, delivering the CORR pool at m's G-CAL dose (the same renders, same sha), with the COMMON and TOLD-MAP banner lines of §2.5 (A0s-OLMo carries TOLD-MAP-SHAM). Roster: OLMo's of record (quartz/velvet, copper/walnut, maple/saddle, amber/granite); **Code checks roster-word admissibility of the clean text, the renders and the golds against this roster** (the Qwen check does not transfer). Decoding: b3's TEMP of record; Code names it. n = 48 valid (6 per pair×map cell), sham 32 (4); maps balanced within pair as §2.4. Same primary, conjuncts, per-arm outcomes (PASS / DEAD / REVERSE / INDETERMINATE), α = .01, floor ≥ .85 at P = .70 (G-PWR; if 48 does not clear it at sham 32, the grid rule of item 3 applies).
  - **Why instruct only:** a told line presupposes instruction-following; a DEAD at Base would be uninformative about the lever. The ontogeny claim is scoped accordingly (below).
  - **Gates:** G-PORT-OLMo (CORR delivery inside the b3 apparatus; acceptance by the F0m-OLMo verifier walking every session's harness bytes from its recorded fields and rng stream — G-VER's principle; b3 has no archived CORR transcripts to replay against, so acceptance is by construction plus a full rule-25 read of the qualification sessions); G-F0m-OLMo qualification: 8 A0s-OLMo-template sessions (one balanced block), the same bars as G-F3 minus the reasoning-line bar; G-TIME-OLMo: one session per arm; keys `m-olmo|{arm}|{s}`, `m-olmo-items|{s}`. Constants in the same locks (v0.1 bars and schedule; v0.2 projection; v1.0 launch counts), OLMo columns beside Qwen's.
  - **Hardware:** one pod session on the standing specs (US-CA-2 A100-SXM4-80GB, volume `o73qvy742n`; console-create if the parked pod's host is full; the respawn protocol — manifest re-hash and determinism re-characterization — runs first, as the 08-22 handoff requires). The PI accepts the cost. The OLMo arm may run in parallel with the Qwen campaign (independent hardware) but its lock entries precede its data like everything else.
  - **Outcome integration (extends item 9):** L0-OLMo := (A0-OLMo = PASS). OLMo Q3's four stage labels keep "Answered" iff L0-OLMo; otherwise *concluded, not answered — the told control on this lineage (instruct) returned [X]*. L0-OLMo governs the OLMo labels and the abstract's "at any of the four training stages" sentence (which becomes "on the Qwen substrate; on OLMo, see §5.5" if ¬L0-OLMo); it does **not** enter the title ceiling, which is decided by the Qwen cells. The abstract sentence is pre-written both ways in patch v2.
  - **Welfare:** §7.3 (item 10) covers OLMo exposure to the corrupted pool identically; nothing is administered.
- **f1's CORR null at 0.12:** A0 licenses the F0 lever, not the 0.12 dose. f1's CORR line in §5.5 gets a scope note: *at a dose PROPOSAL-m's calibration later found below its visibility criterion*; the other four f1 contrasts are unaffected.

## Smaller items

- **Below-floor arms.** Rule adopted: **run to floors, blind.** Launch counts are sized so each arm reaches its valid floor with probability ≥ .90 at G-F3's valid rate; the campaign keeps launching (interleaved, outcome-blind) until every arm's valid count ≥ floor or the hour cap is reached; the analyzer refuses to run before that. This is a stopping rule on n, not on outcomes (not a rule-24 top-up). If the cap stops an arm below floor, the arm is analyzed as obtained, the shortfall and attained power are reported in its verdict sentence, α unchanged.
- **Item pairing across arms.** The item permutation is drawn from a per-index key `m-items|{s}` shared by every arm; the arm key `m|{arm}|{s}` governs generation seeds and menu order. "Sham session s sees the items contrast session s sees" then holds; v1.3 states the two keys.
- **Rule 28(a) floors for secondaries.** A secondary cell is reported with an interval only at ≥ 20 events, otherwise as a count; lose-shift is defined on contrast arms only (shams have no corrupted rounds) and v1.3 says so.
- **G-TIME acceptance.** Hair triggers evaluated on G-TIME's 8 sessions; a fire → STOP and re-specify before G-ID. Binomial bars are reported at n = 8, not evaluated.
- **A2s "can differ".** Ratified: the line is true in A2s under rule 19 (configs can differ in this design; in this arm they do not); recorded in v1.3 §2.5.

## Pins — accepted without objection

Ban list on reasoning-line generation; reasoning lines never enter `earlier`. Monitoring denominators = units generated; look index in the resume identity; cadence every 40 launches; the ≈ 18% false-pause rate over ≈ 19 looks is accepted as the cost of pauses that are not verdicts. Shams coded on the nominal clean label. Launch counts rounded up to the balance unit. Counter-(c) scorer fixed in the analyzer (with item 9's two-label change). Roster-word check on G-CAL renders with rejection-and-redraw (item 2). The m package's own cached-path source guard. The ~40 locator and wording corrections: **yes — send them as a values-checked paste block; the seat folds them into v1.3 with everything above.**

---

*What the seat needs back before writing v1.3: the corrections block; Code's validation of item 2 (n_eligible per item; k per rung; roster-word rejections against BOTH rosters) and of item 3's grid (the (A2, A2s) that clears .85; whether A0-OLMo at 48/32 clears .85 at P = .70); the b3 session rate and TEMP of record for the OLMo projection; and whether the parked pod's host has stock. Items 11 and 12 are decided above (Fallback-2 under the Clock; the OLMo arm is added).*

*Header correction: the first paragraph's "Two items … need a PI call" is superseded — both are decided; nothing in this block awaits the PI.*
