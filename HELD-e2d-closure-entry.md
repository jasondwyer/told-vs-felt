# HELD — e2d closure entry draft (NOT the entry of record)

**Status (2026-09-06): the design patch of 2026-09-06 §1 (R7–R13, seven
replacements over the eight held passages) is APPLIED to the quoted text
below; the entry is HELD on THREE items — (1) R7 prints the z-form CI lower
bound as −.157, the artifact gives −0.156494, which is −.156 at the printed
precision (scripts/e2d_closure_verify3.py, 29/30; raw
results/raw/2026-09-06_e2d_closure_verify3.txt); (2) R7's "the paired 95% CI"
is unqualified after a sentence naming two pairings — it is the clean-set
CI, and for the all-rounds pairing (n = 24) the CI [−.218, +.247] z /
[−.230, +.260] t(23) contains a bar-sized change in both directions, so the
precision claim holds for one pairing and fails for the other; (3) R12's
"removed first" labels are inverted under the plain reading of "removed"
(removing idx 12 first from the 27 gives 46/54; removing truncation first
gives 62/38) — the pairs match the ADDITION order from the paired base that
the values-check called "idx-12-first". The refuters' fourth pass:
results/raw/2026-09-06_e2d_closure_glosscheck4.txt. Per the patch's own rule
("if a ninth gloss appears, write it to raw and hold — no fourth patch"),
Code did not reword; the design seat strips the sentences or corrects them.
The original 125-check verify still reproduces byte-identical.**
Earlier status: HELD on eight items in the design-authored text of record, reported
to the design seat 2026-09-05 (Code's message after the third values-check)
and again in HANDOFF-2026-09-06.md §2. This file, committed with HANDOFF-2026-09-06.md, persists the draft across
Code threads because the closure text of record exists nowhere else in the
repo: it was delivered in the design disposition headed 2026-09-05 (PI clock
01:53 EDT), recovered verbatim from the prior Code thread's transcript, patched
per the design patch of 2026-09-05 (R1–R6), and re-dispositioned on R6 by the
design block of 2026-09-05 §1 (Fisher exact two-sided .26).

**On Design's word** (the eight items resolved, or the text re-sent): apply
the resolution to the quoted block below, re-run
`PYTHONPATH=. jlens-qwen36/.venv/bin/python scripts/e2d_closure_verify.py`
(125/125 against the current text; update the script if a figure's form
changes), re-verify any reworded clause, then commit the entry newest-first
in RESULTS.md with the anchor exactly `e2d CLOSURE — TEXT OF RECORD
(values-checked)`, stamped from `date -u`, naming `08a6076` (annotations,
script fix), `edf2574` (verification record) and `733503d` (R6 update). Then
delete this file in the same commit.

**The eight items (verified by Code; not reworded):**
1. "the paired CI, ±.15, spans the bar in both directions" — z form ±.144,
   CI [−.156, +.132]; t(19) form ±.154, [−.166, +.142]; bar .158; neither
   form reaches +.158, only t reaches −.158. False as stated.
2. "±.15" — .144 rounds to .14; only the t(19) form gives .15. No form named.
3. "one-sided .011 — the D3-gate entry's figure" — the .011 is in the
   2026-09-04 closure-completion entry, item 4; the D3-gate entry has no
   Fisher figure. The mis-attribution originated in HANDOFF-2026-09-05 §2
   item 4 (Code's) and the patch's R4 inherited it.
4. "carry 58% of the marks" — 40/68 = 58.8%, rounds to 59%.
5. "the 0.10 anchor … carries no marker value" — d1 holds a pooled within-M
   delta of −.239, recorded as not comparable.
6. "~4× below e2a's ~.17" — 3.9× to 5.1× depending on the e2d rate (hedged).
7. "62% / 38%" — reproduces under the idx-12-first sequential
   decomposition; truncation-first gives 54/46; no order named.
8. "(slip 10)" — resolves only to the untracked HANDOFF-2026-09-04-design.md.

Items 1–3 are the ones Code would not commit past; 4–8 are rounding,
provenance or hedged.

---

- 2026-09-05 — **e2d CLOSURE — TEXT OF RECORD (values-checked). Design-seat
  authored, PI-ratified 2026-09-05 (PI clock); the four held figures resolved
  by six clause-level replacements (design patch of the same date, R1–R6)
  and one further disposition on R6 (design block of the same date, §1);
  every figure re-verified from the committed artifacts on the domain and
  under the test the text names — [`scripts/e2d_closure_verify.py`](scripts/e2d_closure_verify.py),
  raw [`_closure_verify`](results/raw/2026-09-05_e2d_closure_verify.txt).
  Names `08a6076` for the PI-approved rule-2 and rule-21 annotations and the
  `excised_source` script fix, and `edf2574` for the verification record; this
  entry's own commit carries the text.**
  (Stamp verified at write time: `date -u` → **Sat Sep  5 16:42:55 UTC 2026**.)

  > e2d closed at its qualification rung by the pre-registered run-dose rule:
  > at f = 0.20, D2 returned STOP, SCOPED on Q2 and Q3, adopted by PI
  > disposition before D3 existed, so the verdict-tier free operant under
  > LOCK-j never ran. The apparatus held — Q1 passed at 3/32, exact binomial
  > p = .878 (forced scope). The record channel failed both conjuncts of the
  > registered readability gate (median ≥ .70 AND 10th percentile ≥ .60):
  > .574 / .524 at 0.20 and .613 / .526 at 0.30 (k = 2, criterion set), with
  > the 0.20 displacement comparator at .534 (none at 0.30 — D3 ran M-only
  > under ADDENDUM-j1). The marker imprint sat below the 0.158 bar in every
  > cell and in both readout contexts (0.20: excised +.103, in situ +.127;
  > 0.30: excised +.141, in situ +.062); the primary within-M paired Δ+ =
  > +.103 (n = 27, sd .40, one-sided sign test p = .061) also failed 2·|Δ_R|
  > = .138, and five pre-declared estimators span −.070 to +.103, all below
  > bar. The two contexts differ in magnitude (2.3× at 0.30) and the gap
  > flips direction across dose, so systematic dilution is neither
  > demonstrated nor excluded; what is context-invariant is the below-bar
  > conclusion. Paired on shared content the marker shows no detectable
  > change from 0.20 to 0.30 (clean −.0121, n = 20, one-sided sign test p =
  > .41; all-rounds +.0149, n = 24, one-sided sign test p = .27 — opposite
  > signs, neither resolved, not averaged; the paired 95% CI is [−.157,
  > +.132] in the z form (half-width .144) and [−.166, +.142] under t(19)
  > (.154): a bar-sized increase, +.158, lies outside it under both forms,
  > and a bar-sized decrease inside it under t only); the apparent unpaired
  > rise (+.038 clean, +.068 all-rounds) is a composition artifact with two
  > sources — one session decidable at 0.20 only (idx 12) and roster
  > truncation (D3 ran 24 M sessions to D2's 32) — that split 62/38 when idx
  > 12 is removed first and 46/54 when truncation is removed first; the split
  > is order-dependent, the artifact is not. Degeneracy is ordered across
  > three doses (audit .000 / .023 / .047; read-marked .000 / .113 / .155; on
  > the 24 shared indices audit .025 → .047, read .133 → .155) with a single
  > resolved step (read .10→.20, Fisher exact two-sided p = .021; one-sided
  > .011), neither .20→.30 step resolved (two-sided: audit p = .15, read p =
  > .20; both ≥ .10 one-sided), the .20→.30 read rise carried by one index
  > (s12: 0/10 → 7/10) while indices 1 and 5 sit at 10/10 at both doses and
  > carry 59% of the marks (40/68 on the 24 shared indices) — and it is not
  > axis-specific: D2's random arm degrades at .045 at 0.20, twice M's .023
  > at the same dose.
  >
  > The free operant itself was administered 537 times across D1–D3 (42 / 357
  > / 138 choices over 96 sessions, every read insulated at KL = 0) and
  > returned habit-locked first-pick shares: Δ_first = +0.017 at 0.20 under
  > the primary rule (15/29, valid sessions; 15/30 = 0.000 over all M
  > sessions with a first pick, the domain that includes excluded idx 30) and
  > +0.109 at 0.30 (14/23, where the two domains coincide; one-sided exact
  > binomial p = .202), against first-pick habit-break rates of 1/30 and 1/23
  > (all sessions including excluded — the rule-23 secondaries domain).
  > Nothing above 0.30 was run; the closure is bounded by the measured range.
  > The D2 failure was legibility with coherence intact — not a coherence
  > limit (design ledger slip 10: the pre-written stop sentence encoded 'with
  > coherence' as the predicted failure mode where the failure was Q2/Q3 with
  > coherence intact — defined in the untracked HANDOFF-2026-09-04-design.md
  > §2, restated here for the committed record).
  >
  > Raising the dose did not open the record channel; what it bought in
  > degradation is ordered across three doses and resolved at one step. The
  > weak-state alternative to the e2a null retires in its dose form. The
  > channel question — whether any route other than the transcript can carry
  > the state to the choice — is banked (ledger 23) as motivation for future
  > pre-registration; no unwritten document inherits it.
  >
  > Caveats. V1's L48/0.20 cell (+.408) is a state-live read at the probe and
  > a B2a dose-finding cell excluded from verdicts by V1's own pre-
  > registration; e2d's marker is a no-injection read of text the state
  > produced — different channels, not a ratio. Instrument transfer is
  > unmeasured (the .958 is a self-score on the fit set, refit false). The
  > 0.10 anchor (n = 4 M sessions, pooled estimator) carries no comparable
  > marker value (its pooled within-M delta, −.239 over 20/20 generations, is
  > a different statistic, recorded as not comparable) and is the left end of
  > the readability and degeneracy series only. D3's readability lacks D2's
  > task-disjointness guarantee.
  >
  > Banked (ledger 23; license pre-registrations, never verdicts): the
  > composition artifact as above; alternation decay e2a .840 (pooled; reward
  > arm .827) → D2 M .690 → D3 M .522, all on habit.secondaries' domain of
  > all sessions including excluded (rule 23; valid-only e2a .837 / .824),
  > with the first-pick break rate flat within e2d (1/30 vs 1/23; Fisher
  > exact two-sided p = 1.00) and four to five times below e2a's .17 (32/188,
  > all sessions: 5.1× D2's 1/30, 3.9× D3's 1/23, 4.5× the pooled 2/53) —
  > only D2→D3 is a clean dose step and it is unresolved (.690 vs .522,
  > Fisher exact two-sided p = .26 — the test of record for count comparisons
  > in this entry); degeneracy tracks displacement, not the reward direction;
  > estimator sign-instability (−.070 to +.103); in-situ scoring at 2.57 vs
  > 0.54 s per forward (4.7×, matching D2's ratio); the clean/all-rounds sign
  > disagreement on the dose change, flagged not averaged.

  - **Provenance of the text.** The held text was never committed; it was
    delivered to the prior Code thread in the design disposition headed
    2026-09-05 (PI clock 01:53 EDT, 05:53 UTC) and recovered verbatim from
    that thread's transcript for this entry. Each of the six clauses the patch
    replaces matched the recovered text exactly once; no other character
    changed. Disposition §1 adopted all seven values-check glosses as
    OVERSTATED and rewrote them into the text above (comparator bound to D2;
    dilution neither demonstrated nor excluded; the V1 ratio moved to caveats
    as a channel distinction; ordered-with-one-resolved-step on the paired
    basis; no-detectable-change with its precision; break rate flat within
    e2d only; the verdict-tier operant never ran, reason of record the
    run-dose rule). Critic items: the conjunctive gate stated with both
    conjuncts; the entry titled as text of record; no disposition assigned to
    an unwritten document; the legibility/degradation sentence recast; the
    transfer caveat as a self-score with refit false.
  - **What changed from the held text (six replacements and the R6
    re-disposition). No figure changed by a change of DATA: R5 moves the
    primary DV to its own domain; R4 adds the one-sided and per-step
    figures beside the ones already printed; R6 replaces two p-values by
    naming a different test (.85 → 1.00 for 1/30 vs 1/23; .21 → .26 for
    the D2→D3 step), the counts underneath unchanged.**

    | | held | of record |
    |---|---|---|
    | R1 | `p = .878` | `exact binomial p = .878` |
    | R2 | `sign p = .061` | `one-sided sign test p = .061` |
    | R3 | `sign p = .41; … p = .27` | `one-sided sign test p = .41; … one-sided sign test p = .27` |
    | R4 | `Fisher p = .021 two-sided … (p ≥ .10)` | `Fisher exact two-sided p = .021; one-sided .011 … (two-sided: audit p = .15, read p = .20; both ≥ .10 one-sided)` |
    | R5 | `Δ_first = 0.000 at 0.20 (15/30)` | `Δ_first = +0.017 at 0.20 under the primary rule (15/29, valid sessions; 15/30 = 0.000 over all M sessions with a first pick …)`, domains named for 14/23 and for the break rates |
    | R6 | `(1/30, 1/23; p = .85) … (p = .21)` | ladder domain named (all sessions incl. excluded; valid-only e2a .837 / .824); `Fisher exact two-sided p = 1.00`; the D2→D3 step re-dispositioned to `(.690 vs .522, Fisher exact two-sided p = .26 — the test of record for count comparisons in this entry)` |

  - **VERIFICATION RECORD — the six clauses, each on its named domain and
    under its named test (script above; every figure recomputed, not read
    back).**

    | clause | figure | domain / test | reproduces |
    |---|---|---|---|
    | R1 | Q1 3/32, p = .878 | exact binomial, one-sided (greater) vs p0 = .15 — the registered form; two-sided would be .467 | .8782 ✓ |
    | R2 | Δ+ +.103, n 27, sd .40, p = .061 | one-sided sign test, 18/27 positive (two-sided .122) | +.1030 / 27 / .399 / .0610 ✓ |
    | R3 | clean −.0121, n 20, p = .41; all-rounds +.0149, n 24, p = .27 | one-sided sign tests, 11/20 and 14/24 (two-sided .824 / .541) | ✓ both, recomputed from per-session diffs |
    | R4 | read .10→.20 .021 (one-sided .011); audit .20→.30 .15; read .20→.30 .20; one-sided both ≥ .10 | Fisher exact, M arm, rounds + choices, all sessions incl. excluded | .0213 / .0112 / .1508 / .1959 / .1021 / .1029 ✓ |
    | R5 | 15/29 = +.017 valid; 15/30 = .000 all-with-a-pick; 14/23 both; p = .202; breaks 1/30, 1/23 | valid = not excluded under the e2a-scope rule recorded in `d2_sessions.json` (`exclusion_scope: "e2a"`, 3 M excluded: idx 24 audit@forced3, idx 30 lexical:plaza@free0, idx 31 lexical:ridge@forced0; only idx 30 has a first pick); one-sided exact binomial; `habit.secondaries` over all sessions | ✓ all; break rates 1/30 and 1/23 reproduce on the all-sessions domain (valid-only would be 1/29, 1/23) |
    | R6 | e2a .840 / .827; valid-only .837 / .824; D2 .690; D3 .522; Fisher 1.00; step Fisher .26 | all sessions incl. excluded: 157/187, 86/104 (valid 154/184, 84/102); D2 20/29, D3 12/23 on both domains; 1/30 vs 1/23 Fisher two-sided 1.0000; 20/29 vs 12/23 Fisher two-sided .2597 | ✓ all — see the second hold below |

    **The Fisher table of record** (test of record for count comparisons in
    this entry: Fisher exact, two-sided; one-sided printed beside; counts are
    M-arm rounds + choices over all sessions including excluded — audit D1
    0/40, D2 7/300, D3 11/233; read-marked D1 0/40, D2 34/300, D3 36/233):

    | step | two-sided | one-sided |
    |---|---|---|
    | audit .10→.20 | 1.0000 | .4129 |
    | audit .20→.30 | .1508 | .1021 |
    | **read .10→.20** | **.0213** | .0112 |
    | read .20→.30 | .1959 | .1029 |

    The `.011` is the one-sided figure. **Attribution corrected here:** it
    was printed in the 2026-09-04 closure-completion entry (item 4, "read
    .10→.20 p = .011"), NOT in the D3-gate entry, whose only .011-family
    figure is the steered-arm binomial .0117; HANDOFF-2026-09-05 §2 item 4
    (Code's) mis-attributed it and the patch's R4 inherited the attribution.
    The disposition's `.021` is two-sided; "p ≥ .10" for the three
    unresolved steps holds under both.

    **The second hold, and its disposition.** The patch's R6 named the D2→D3
    alternation step as "two-proportion z p = .21". That figure reproduces
    under the unpooled-variance form only (z = 1.244, p = .2136); the
    pooled form — the one Code used to pin the neighbouring ".85" — is
    z = 1.236, p = .2164, which prints .22. Reported, not reworded
    (`edf2574`). Design's disposition (block of 2026-09-05, §1): the clause
    of record is **Fisher exact two-sided p = .26** (20/29 vs 12/23:
    .2597), the entry's own declared test for count comparisons; under
    every variant the step is unresolved. Ledger, design seat: folded into
    slip (14)'s class as a fifth unnamed test.

    **The four-figure report that held the entry (from the `08a6076` hold,
    carried as the record):** (1–2) e2a alternation .840 pooled / .827 reward
    are correct on all sessions including excluded (157/187, 86/104; valid-only
    .8370 / .8235), which is also the domain of D2 .690 and D3 .522
    (`habit.secondaries`, rule 23) — resolved by naming the domain (R6).
    (3) "p = .85" for 1/30 vs 1/23 was a two-proportion z (z = .192,
    p = .8477); two-sided Fisher gives 1.0000 — resolved by naming the test
    (R6). (4) Δ_first = 0.000 (15/30) counted the excluded idx 30 under the
    primary DV's name; the primary rule gives 15/29 = +.0172 — resolved by
    moving the primary DV to its own domain and keeping 15/30 beside it, labelled
    (R5). Test of record for Fisher named and printed above (R4).

    **Everything else in the text:** 125 checks in all (the six clauses plus every other figure in the text), 125 pass checks, all pass —
    readability conjuncts, comparator, the four marker cells and the bar,
    2·|Δ_R|, the five estimators, the paired CI (±.144), the composition
    decomposition (62% idx 12 / 38% roster truncation, by the values-check's
    sequential decomposition A → B → C), degeneracy rates on both bases, s12
    and the idx 1/5 saturation (40/68 = 58.8%), axis non-specificity
    (R .045 vs M .023, S 0/151), 537 / 42 / 357 / 138 choices over 96
    sessions every read at KL = 0, the cost ratio 2.57 / 0.54 (4.72×), the
    .958 self-score with refit false, the 0.10 anchor.
  - **Beside-notes carried (disposition §4, never over).** (i) The D3 scoring
    entry's "the marker delta does not move" reads "shows no detectable
    movement, at a precision that cannot exclude a bar-sized change"; its
    mechanism sentence ("survive exclusion and cleaning") is 62% right; its
    degeneracy table is on D2's full 32 where release condition 4 wants the
    paired 24 — the closure carries the paired basis. Annotated here; the
    entry stands as written. (ii) `data/e2d/d3_excision_check.json`'s
    top-level `excised_source` reads "committed D2 scoring (not rescored)"
    for a D3 run — a hardcoded string, fixed in the script at `08a6076`; the
    committed artifact is untouched and its nested `_source` was always
    correct. (iii) `HANDOFF-2026-09-04-design.md` §1 quotes the EARLIER held
    sentence of record (the pre-disposition text the values-check graded, with
    "a quarter of its short-context value" and "(dilution excluded)") and §7
    paraphrases it; both superseded by the text above. Untracked, referenced
    by name: no edit, no rename.
  - **Ledger, design seat (PI-ratified 2026-09-05, PI clock).** Slip (12):
    the closure was written in the verdict register beyond what the tests
    licensed — seven overstated glosses in one text, caught pre-commit by the
    values-check. Slip (13): design block headers carried UTC dates the seat
    could not verify, one day fast from `a9e6a74` on; Code's half stands in
    the record-hygiene entry. Slip (14): in the replacement text the primary
    DV Δ_first was reported on the all-sessions domain under the primary
    rule's name, and three further rates/tests were stated without their
    domain or test named — one item, four instances, caught pre-commit by
    Code's 80-figure re-verification; a fifth instance folded in by the
    same-day block (the alternation step's z-test named without its
    variance form, resolved to the test of record). **Design count: fourteen**
    at the 2026-09-05 patch. *Added by the design patch of 2026-09-06 §1
    (numbering the design seat's):* **Slip (16), design seat:** a claim about
    the paired CI that the figure contradicts ("spans the bar in both
    directions"; would not commit past). **The `.011` attribution, both
    seats:** inherited from HANDOFF-2026-09-05.md §2 item 4 (Code's) and
    propagated unverified into the patch's R4 (design's); corrected beside
    in that handoff 2026-09-06. **R9–R13's class** (rounding, an unnamed
    order, a hedged ratio, an uncommitted reference) **folded into slip
    (14).** Code's four draft fixes stand. Standing
    addition to the design-side standard: in closure prose every rate names
    its domain and every p names its test, no exceptions. Standing fix, design
    side: block headers carry the PI's clock, labelled as such, never a bare
    "(UTC)"; Code stamps from `date -u`.
  - **Rule annotations (disposition §6, PI-approved).** Rule 2 and rule 21
    annotated at `08a6076`, verbatim from the disposition-2 entry item 6, as
    annotations not rewrites.
  - **What this entry does not do.** It reopens nothing: Q2 and Q3 failed,
    the run-dose rule returned STOP, SCOPED, and the verdict tier never ran.
    The judge-port acceptance run (built, never run) and the content-class
    candidate (not adopted) are unaffected and still owed / awaiting
    adjudication.
