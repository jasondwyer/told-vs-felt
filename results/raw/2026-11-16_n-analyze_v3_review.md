# n_analyze.py, the seat's answers to G-ANL-n's nine questions and the schema's follow-up commit: the blind review, its mutants and the dispositions (PI date 2026-11-16)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's answers to G-ANL-n's nine questions`.

- **What changed under review.** Against the committed analyzer (`bedc198`, sha256 `34a513f9…98b6`), the draft carries
  the seat's answers to the question block (`8e3bf91`; the answers raw
  `results/raw/2026-11-16_n-ganl_design-to-code_answers.md`, committed at `52b2c97`) and ADDENDUM-n1 v0.1 (`a61f13d`),
  and moves the schema pin from `14e65d8` to n-build's follow-up commit `d791bd9`. It was built in two steps, each run
  in a battery window the coordinating session granted:
  - step 1, against the schema at `14e65d8`: the rulings (slopes through the origin; N1-P's points in the ceiling and
    the causes; the decision f when the cap binds; the sign rule; ADDENDUM-n1 §7.6's forms; secondary (b) struck; the
    registers). Two runs: 192/197, then 197/197;
  - step 2, against the schema at `d791bd9`: N1-P's plan row with the keepers, the capture forms per layer, the cap's
    `loads_ms`, P(d) required where G-LEAK-n certifies, the pin moved. Two runs: 197/198, then 198/198.
- **The review, blind.** A reviewer read the step-2 draft, frozen as a read-only copy at sha256 `1316f93a…dd06`
  (198/198 on those bytes, run from the working copy before it was frozen unchanged).
  - It was a subagent of this session, under a brief quoting the list of record v2's items 1–5, allowing no Python.
  - Its spec: the answers raw and the question block; ADDENDUM-n1 v0.1; PROPOSAL-n v0.2 §0.6, §2.3–§2.4, §3, §4, §5;
    `valence_core/n/schema.py` at `d791bd9`; and the n-build answers raw's §2.3, §2.5 and §3. It executed no code
    (it read files and computed digests) and opened nothing under `data/`.
  - It returned production findings F1–F11 (F5 MINOR, the rest NOTEs; no MAJOR) and battery findings B1–B10 (B1–B3
    MAJOR, B4–B8 MINOR, B9–B10 NOTEs), with 40 mutants V01–V40 and its predictions: 19 surviving the frozen copy
    (V01–V19), 21 killed (§1).
- **The dispositions** (§2). Fixed: F4–F6, F8–F10 and B1–B10. Registered as Code's readings, their texts amended: F1
  (PIN-n-29), F2 (PIN-n-30), F7 (PIN-n-28), and F3 as a new reading, PIN-n-32. Kept, for the seat: F11. Beyond the
  findings, Code added a refusal case that no case reached (a schema whose read plan differs from the analyzer's).
- **The mutants** (§3). M01–M40 re-express V01–V40: 39 verbatim, and M17 re-expressed on the fixed draft, whose line
  F6 changed. M41–M62 are Code's: on the fixes, and on changed code, mostly lines the reviewer's mutants did not
  touch (M54 and M62 mutate V38's and V27's lines another way). They ran once, on the fixed draft (sha256
  `9e7faea1…e4ce`, 207/207): **62 of 62 killed.** M20–M62 each by its predicted check, directly or through the
  exception its group raised. M01–M19, which the reviewer predicted would survive the frozen copy, each by a check
  the dispositions added or extended (M11 by DOSE-BESIDE-D20 and M18 by STR-GANL-ARTIFACT, the two extended).
- **The battery runs** (§4) and **the committed bytes** (§5): the committed file differs from the mutation-tested base
  in the repository line and in text only: the register texts of PIN-n-30, PIN-n-31 and PIN-n-32 and `plan_cells`'s
  docstring.

Every Python run here was inside a battery window the coordinating session granted: one process at a time,
`nice -n 19`, `-I`, with temp folders outside the repository, and in the foreground but for one batch of mutants,
which the harness moved to the background (§4). Nothing ran on a model or on the box.
Each mutant was applied as an exact, unique text replacement (`.old` → `.new`, asserted to occur once) to a fresh copy
of its base. That copy's battery ran with `--selftest`, and "killed" means a non-zero exit.

## 1. The reviewer's report, as saved from its hand-back (unedited)

The reviewer returned its report as its final message. Code saved it by script from the subagent's transcript; its
headings are moved down two levels here, and nothing else is changed. Line numbers in it are the frozen copy's. Its
bottom line says it found "no MAJOR or MINOR defect in the production code", but its findings list F5 as MINOR;
the entry and §2 follow the findings.

### Blind review: the `scripts/n_analyze.py` draft (frozen copy sha256 1316f93a…dd06), checked against the seat's rulings of 2026-11-16, ADDENDUM-n1 v0.1 and schema d791bd9

**Bottom line:** I found no MAJOR or MINOR defect in the production code. Every ruling Q1–Q9 is implemented as ruled, wherever it applies. The real weakness is in the battery. No check compares the filled text of these sentences to independent literal text:
- a dose NOT-DETECTABLE sentence;
- an N1 NOT-REPLICATED sentence with a certified movement against the conditioned zone;
- an N2 sentence on a map where the cap binds.

So bugs that would print wrong sentences pass all 198 checks (B1–B3; mutants V01–V07). Of the 40 mutants, 19 are predicted to survive.

Method: I only read files. Nothing was run, nothing was written in the repository or the scratch folder, and I opened nothing under `data/`. I confirmed by digest that:
- the frozen copy hashes to 1316f93a…dd06;
- `ADDENDUM_SHA256` (e979f8f2…5e03) matches the committed addendum;
- `SCHEMA_SHA256` (0ea39600…0db6) matches the schema at d791bd9, and the working-tree schema is identical to it.

#### What checks out

- **Q1 and Q9 (slopes):**
  - The N1-V slope, the N1-R floor, N2's slope and N2's floor are all fitted through the origin over the nonzero points. A zero point is refused.
  - The with-intercept N1-V slope is reported beside.
  - On BK's symmetric grid the two fits agree (0.9164). On an asymmetric grid they differ (by hand, 1.9 / 2.25).
  - N2's floor uses the random reads at the points d_eq and d_20 are kept at.
- **Q2 (N1-P's points):**
  - N1-P now reads +1, +d_20, +d_eq and −1. `plan_cells` and `own_plan` derive the same keepers as the schema's `keeper` and `arm_cells` on every merge shape; I checked this case by case.
  - P(d) is computed at each planned label.
  - `ceiling_cert` is used at every certification point: N1 at +1, dose at d_eq and its d_20 beside, N2 at its decision point and its beside point. Its STOP cannot fire on a plan the reader accepted, including the TAU/4 row.
  - +1/2 takes L alone, in the G-LEAK-n table only.
- **Q3, Q4, Q5 (labels and tuples):**
  - The §0.6 label is applied everywhere, with N2 reading span_reward's G-READ-n result at its decision f.
  - 385 tuples, 1,921 evaluations; the sentence functions are total.
  - I re-derived the reachability counts by hand: (a) 28, (b) 25, (c) 24, (d) 17. The shape classifier in `pinned_map_reach` covers every case: d_eq never folds into d_20, and in shape (c) d_eq always folds into +1/2.
- **Q6 (INDETERMINATE causes):** the causes for N1, dose, N2 (now including N1-P) and N4 match the ruling. Pauses on N1 arms still leave N2 evaluated.
- **Q7 (cap binds):** the cap binds iff 2·d_eq > 1, with the d_eq = 0.5 edge handled. The decision f, the decision point, the beside point with 2·d_eq printed, G-READ-n's "E" input and the table's `enters` column all follow from it.
- **Q8 (sentence forms):**
  - §7.6's forms equal the addendum's italic spans (checked against the file's bytes) and are pinned by digest.
  - The `[movement]` slot replaces the quoted clause exactly once in each of the three NOT-DETECTABLE forms.
  - The sign rule: DETECTABLE and PARTIAL require a positive mean; a certified negative movement becomes NOT-DETECTABLE or NOT-REPLICATED and its clause names the movement.
  - The labels and `[f]` are carried.
  - `fill` replaces the longest slot names first, so slots nested inside `[movement]` and `[failing]` get filled. No path I traced leaves a slot.
- **Schema d791bd9:**
  - 7,680 reads in 138 cells.
  - The per-layer capture hash maps are bound to both the stage report and the G-READ-n artifact.
  - `loads_ms` is carried through.
  - `kfold10` and `cv_seed` are enforced by `check_gread`.
- **Struck secondary:** secondary (b) now prints the addendum §4 text.
- **Registers:** each OPEN entry states what the seat ruled. PIN-n-27 to PIN-n-31 are each needed and each describes what the code does.

#### Findings — production code

- **F1 NOTE — `n2_outcome` (line 498) and PIN-n-29 (lines 1925–1928).**
  - Problem: the code applies the incompleteness causes per arm. The ruling reads "N2 when … N1-P at the norm-matched point is incomplete".
  - Scenario: one N1-P read at −1 is non-finite, or rand_07's +1/2 cell is missing (the battery's RD-INDET case). The draft makes N2 INDETERMINATE even though every read its certification uses is present. On the literal reading, N2 is evaluated.
  - Fix: keep the PIN, but put this exact scenario to the seat.
- **F2 NOTE — PIN-n-30, `n2_outcome` (lines 505–507).**
  - Problem: certifications are unsigned in N2, so N1-V moving against the conditioned zone at the norm-matched point gives SPECIFIC.
  - Scenario: the sentence then says the valence direction "does" move BK's apparatus. On shape (b) this SPECIFIC can sit beside a dose NOT-DETECTABLE that names the movement as against the zone.
  - Fix: seat confirmation.
- **F3 NOTE — `fill` (lines 2589–2591) and §7.6's forms.**
  - Problem: when d_eq folds into +1/2, the NOT-DETECTABLE forms print "Δm(d_eq) = …" using the +1/2 figure. They carry no "read at d = +1/2" note, which ADDENDUM-n1 §5.1 asks for and DETECTABLE already carries through `VALUE_MERGED`.
  - Fix: the wording is verbatim, so the seat should decide whether to add the note.
- **F4 NOTE — `build_state` (lines 2432–2435).** The with-intercept slope is written as `figures.per_arm.slope_V_with_intercept` without the "descriptive" label the ruling asks for. Fix: add a label such as `descriptive: true`, or rename the key.
- **F5 MINOR — `dose_outcome` (lines 473–474).**
  - Problem: an INDETERMINATE dose returns no d_20 beside entry at all. The seat's raw §1.6 says the d_20 figure is then "reported as not computed", and OPEN-Q6 omits that clause.
  - Fix: return `"d_20_beside": None` (marked not computed) and add the clause to OPEN-Q6.
- **F6 NOTE — `n2_outcome` beside (lines 508–514).** Under the cap, the f = 0.20 beside reports span_reward's certification but not N1-V's mean or certification at d = 1. ADDENDUM §5.3 says the beside is reported "against N1-V at d = 1". Fix: add V and its certification at the beside point.
- **F7 NOTE — `CONJUNCT_TEXT` (lines 636–637) and PIN-n-28.**
  - The sign condition's name, "the mean Δm at d = +1 above 0", is a new Code form that is not in Appendix A and is not registered on its own.
  - The against form repeats Δm(+1) and its CI (they appear again right after "fails:") inside nested parentheses.
  - Fix: name the form in PIN-n-28 and let the seat choose the wording.
- **F8 NOTE — PIN-n-31 and `load_campaign` (lines 2255–2269).**
  - The reader no longer checks any capture bytes; bedc198 hashed the array file.
  - The PIN relies on "n-build's reading, declared at its BUILD", and that declaration is not yet on record.
  - Fix: mark the dependency as pending in the PIN.
- **F9 NOTE — line 403.** The `State.P` comment still says "at +1, −1".
- **F10 NOTE — `ganl_artifact` spec string (lines 4033–4034).** It omits ADDENDUM-n1 §4 (secondary (b) struck) and §6 (the band forms the reader binds).
- **F11 NOTE — seat-level, no code change.** Under §7.6, an answered NOT-DETECTABLE whose movement is against the zone still ends "dose is an explanation of record for the program's null". A certified movement at d_eq arguably shows the state does reach the decision at that dose.

#### Findings — the battery

- **B1 MAJOR — the `[movement]` fill is untested.**
  - No test fills a dose NOT-DETECTABLE sentence and compares it to literal text. RD-GREAD and RD-GREAD-MIXED (lines 3075–3108) check only the label, the form and that "AUC 0.810" appears. VD-COMPLETE compares against `expect()` (lines 3489–3493), which calls the same `fill`. No campaign produces a dose movement against the zone.
  - Consequence: V02, which writes "moves against the conditioned zone" into every NOT-DETECTABLE sentence, passes.
  - Fix: add reader-path campaigns producing dose NOT-DETECTABLE in each of the three forms, both against and not, and check the full text against literal text.
- **B2 MAJOR — the N1 against fill is untested.** No filled N1 NOT-REPLICATED-against sentence is checked; SENT-FAILING-NOTREP tests only the template.
  - Consequence: V03 (dropping `[c]`) would STOP the analyzer on such a campaign, and V04 drops the seat's clause. Both pass.
  - Fix: add a campaign with N1-V at +1 at about −0.6 (CI excluding 0, above the ceiling) and check the filled sentence against literal text.
- **B3 MAJOR — the N2 sentence where the cap binds is never checked against literal text.** RD-CAP-BINDS fills nothing. RD-MERGED-DEQ compares only the dose sentence. VD-MERGED-ROUTE-A compares against `expect()`. So V05, V06 and V07 survive. Fix: in RD-CAP-BINDS, fill the sentences and compare the N2 sentence to literal text at "f = 0.10".
- **B4 MINOR — the "against" conditions are tested on one side only.** None of these is tested:
  - N1 with a negative mean, CI excluding 0 and within the ceiling (V08 survives);
  - dose with a negative mean above the ceiling and a CI including 0 (V09 survives);
  - dose with a negative mean, CI excluding 0, not certified (V10 survives).
- **B5 MINOR — N2's slope and floor are checked only on shape (a), where N2's points equal the kept points.** V13–V16 survive. Fix: check `slopes_N2` and `floors_N2` in the cap-binding campaign, expecting the mismatch flag true.
- **B6 MINOR — the dose's d_20 beside.** DOSE-BESIDE-D20 asserts only "certified" with V far above the ceiling, so V11 survives.
- **B7 MINOR — `gleak_table`'s `needs()`.** Nothing tests the table with N1-P incomplete, so V12 survives.
- **B8 MINOR — N2 beside fields.** The beside's "E" and the INDETERMINATE "f" are never checked; V17 and V19 survive.
- **B9 NOTE — `BOUND_RELS`.** Nothing asserts that the addendum is in `BOUND_RELS`: CMD-GANL-REFUSE always passes `bound=`. V18 survives.
- **B10 NOTE — four checks claim more than they test:**
  - RD-CAP-BINDS says "N2's label reads … f = 0.10" but checks only the input (lines 2986–2987).
  - SENT-FAILING-NOTREP says "exactly its own" but checks only that each name is included.
  - NUM-BK-REPRO still says "BK's five points"; the fit now uses the four nonzero points.
  - RD-ASYM's "dose ceiling max(L, P)" item is met by L alone, because P(d_eq) ≈ 0.19994 < L(d_eq) = 0.2. The `_bt_asym` docstring also omits N1-P's +0.2 at +d_20 and +d_eq.

#### Mutants

Every old text below is a whole line (or whole lines) that occurs exactly once in the frozen copy; I checked each with a whole-line match. V19–V40 cover the rulings' main branches and are predicted killed, to show what the battery does catch.

```
@@ V01 | fill | the against clause is never printed in a dose sentence | predicted: survives
                        MOVE_SLOT: MOVE_AGAINST if d["against"] else MOVE_NOT_CERTIFIED})
~~
                        MOVE_SLOT: MOVE_NOT_CERTIFIED})
```
```
@@ V02 | fill | every NOT-DETECTABLE sentence says "moves against the conditioned zone" | predicted: survives
                        MOVE_SLOT: MOVE_AGAINST if d["against"] else MOVE_NOT_CERTIFIED})
~~
                        MOVE_SLOT: MOVE_NOT_CERTIFIED if d["against"] else MOVE_AGAINST})
```
```
@@ V03 | fill | [c] is left in a NOT-REPLICATED-against sentence, so the analyzer STOPs | predicted: survives
                        "[c]": _u(n1["ceiling"]), "[x−]": _n(vm1.mean), "[CI−]": _ci(vm1),
~~
                        "[x−]": _n(vm1.mean), "[CI−]": _ci(vm1),
```
```
@@ V04 | fill | N1's sentence drops the seat's against clause | predicted: survives
                        "[failing]": failing_text(n1["failing"], against=n1["against"])})
~~
                        "[failing]": failing_text(n1["failing"])})
```
```
@@ V05 | fill | when the cap binds, N2's Δm and CI come from f = 0.20 | predicted: survives
            e = st.E[n2["f"]]
~~
            e = st.E[F20]
```
```
@@ V06 | fill | N2's sentence says "at f = 0.20" when decided at 0.10 | predicted: survives
            sub.update({"[xE]": _n(e.mean), "[CIE]": _ci(e), "[c]": _u(n2["ceiling"]), "[f]": F_TEXT[n2["f"]],
~~
            sub.update({"[xE]": _n(e.mean), "[CIE]": _ci(e), "[c]": _u(n2["ceiling"]), "[f]": F_TEXT[F20],
```
```
@@ V07 | F_TEXT | the f = 0.10 fill reads "0.20" | predicted: survives
F_TEXT = {F10: "0.10", F20: "0.20"}       # N2's [f] slot (ADDENDUM-n1 §7.6: "at f = [f]")
~~
F_TEXT = {F10: "0.20", F20: "0.20"}       # N2's [f] slot (ADDENDUM-n1 §7.6: "at f = [f]")
```
```
@@ V08 | n1_outcome | "against" without (iii): claims "beyond the leak ceiling" when it is not | predicted: survives
    against = c["ci+1"] and c["iii"] and v1.mean < 0.0
~~
    against = c["ci+1"] and v1.mean < 0.0
```
```
@@ V09 | dose_outcome | "against" with a CI that includes 0 | predicted: survives
    against = v.excludes0() and cert and v.mean < 0.0
~~
    against = cert and v.mean < 0.0
```
```
@@ V10 | dose_outcome | "against" without G-LEAK-n certification | predicted: survives
    against = v.excludes0() and cert and v.mean < 0.0
~~
    against = v.excludes0() and v.mean < 0.0
```
```
@@ V11 | dose_outcome | the d_20 beside ignores P(d_20) | predicted: survives
    c20 = ceiling_cert(st, d20)
~~
    c20 = ceiling(st.L[d20], None)
```
```
@@ V12 | gleak_table.needs | a G-LEAK-n row at d_eq or d_20 certified against L alone when N1-P is incomplete | predicted: survives
        return [arm, "N1-R"] + (["N1-P"] if pt in st.dmap.n1p_points() else [])
~~
        return [arm, "N1-R"] + (["N1-P"] if pt in (1.0, -1.0) else [])
```
```
@@ V13 | build_state | the mismatch on N2's floor points under the cap or a merge is never printed | predicted: survives
                                    "n2_points": list(n2_pts), "mismatch": [p10, p20] != list(n2_pts)}
~~
                                    "n2_points": list(n2_pts), "mismatch": False}
```
```
@@ V14 | build_state | the mismatch on N2's slope points is never printed | predicted: survives
                                                               mismatch=list(pts) != list(fl_pts))
~~
                                                               mismatch=False)
```
```
@@ V15 | build_state | N2's floor fitted at 2·d_eq for reads taken at +1 | predicted: survives
                    _, _, sl = slope_est("N1-R", (p10, p20), [dv[(d_, lab_of[p10])], dv[(d_, lab_of[p20])]])
~~
                    _, _, sl = slope_est("N1-R", n2_pts, [dv[(d_, lab_of[p10])], dv[(d_, lab_of[p20])]])
```
```
@@ V16 | build_state | N2's slope fitted on the kept points, not (d_eq, 2·d_eq) | predicted: survives
        est, n_c, _ = slope_est(arm, pts, [fv[F10], fv[F20]])
~~
        est, n_c, _ = slope_est(arm, fl_pts, [fv[F10], fv[F20]])
```
```
@@ V17 | n2_outcome | the beside reports the decision f's estimate | predicted: survives
    beside = {f_bes: {"point": mb, "E": st.E.get(f_bes), "ceiling": cb,
~~
    beside = {f_bes: {"point": mb, "E": st.E.get(f_dec), "ceiling": cb,
```
```
@@ V18 | BOUND_RELS | a canonical ganl run no longer requires the addendum committed | predicted: survives
BOUND_RELS = (PROPOSAL_REL, ADDENDUM_REL, SCHEMA_REL, f"{BK_NP_REL}/prereg.json", f"{BK_NP_REL}/reduced.json")
~~
BOUND_RELS = (PROPOSAL_REL, SCHEMA_REL, f"{BK_NP_REL}/prereg.json", f"{BK_NP_REL}/reduced.json")
```
```
@@ V19 | n2_outcome | an INDETERMINATE N2 under the cap reports f = 0.20 | predicted: survives
        return {"state": "INDETERMINATE", "f": f_dec, "causes": causes}
~~
        return {"state": "INDETERMINATE", "f": F20, "causes": causes}
```
```
@@ V20 | dose_outcome | a negative certified movement becomes DETECTABLE | predicted: killed by DOSE-ND-AGAINST
    state = "DETECTABLE" if (v.excludes0() and cert and v.mean > 0.0) else "NOT-DETECTABLE"
~~
    state = "DETECTABLE" if (v.excludes0() and cert) else "NOT-DETECTABLE"
```
```
@@ V21 | n1_outcome | a negative certified movement becomes PARTIAL | predicted: killed by N1-NOTREP-sign (and BND-NEG-CERT)
    elif c["ii"] and c["iii"] and c["ci+1"] and c["sign"]:
~~
    elif c["ii"] and c["iii"] and c["ci+1"]:
```
```
@@ V22 | n1_outcome | "against" with a CI that includes 0 | predicted: killed by N1-NOTREP-ci+1-sign
    against = c["ci+1"] and c["iii"] and v1.mean < 0.0
~~
    against = c["iii"] and v1.mean < 0.0
```
```
@@ V23 | build_state.slope_est | slopes of record fitted with an intercept | predicted: killed by RD-ASYM
    def slope_est(arm, pts, vecs, fit=session_slopes_origin):
~~
    def slope_est(arm, pts, vecs, fit=session_slopes):
```
```
@@ V24 | build_state | the with-intercept beside fitted without the d = 0 point | predicted: killed by RD-ASYM
                est_i, _, _ = slope_est("N1-V", v_pts, [zero if pt == 0.0 else vecs[pt] for pt in v_pts],
~~
                est_i, _, _ = slope_est("N1-V", nz_pts, [vecs[pt] for pt in nz_pts],
```
```
@@ V25 | outcomes | N2's label reads span_reward at f = 0.20 under the cap | predicted: killed by RD-CAP-BINDS
           "E": st.gr("span_reward", st.dmap.n2_decision_f())}
~~
           "E": st.gr("span_reward", F20)}
```
```
@@ V26 | DoseMap.cap_binds | the cap binds at 2·d_eq = 1 | predicted: killed by NUM-CAP-DECISION-F
        return 2.0 * self.d_eq > 1.0
~~
        return 2.0 * self.d_eq >= 1.0
```
```
@@ V27 | DoseMap.n1p_points | P(d_eq) never required | predicted: killed by NUM-N1P-POINTS
        return tuple(sorted({1.0, -1.0, r["d_20"], r["d_eq"]}, reverse=True))
~~
        return tuple(sorted({1.0, -1.0, r["d_20"]}, reverse=True))
```
```
@@ V28 | ceiling_cert | a missing P(d) silently falls back to L | predicted: killed by BND-P-REQUIRED
    if pt not in st.P:
        raise AnlStop(f"STOP: no P(d) at d = {pt!r}, a point where G-LEAK-n certifies (ADDENDUM-n1 §5.2)")
    return ceiling(st.L[pt], st.P[pt])
~~
    return ceiling(st.L[pt], st.P.get(pt))
```
```
@@ V29 | n2_outcome | an incomplete N1-P no longer makes N2 INDETERMINATE | predicted: killed by N2-INDET-incomplete:N1-P
    reads = ("N2-E", "N1-V", "N1-R", "N1-P")
~~
    reads = ("N2-E", "N1-V", "N1-R")
```
```
@@ V30 | n2_outcome | the beside's ceiling is L alone | predicted: killed by RD-CAP-BINDS
    cb = ceiling_cert(st, mb)
~~
    cb = ceiling(st.L[mb], None)
```
```
@@ V31 | n2_outcome | decided at d_20's point under the cap | predicted: killed by N2-MATCH-RATIO
    m = st.dmap.norm_matched(f_dec)
~~
    m = st.dmap.norm_matched(F20)
```
```
@@ V32 | n2_outcome | span_reward certified at f = 0.20 under the cap | predicted: killed by N2-CAP-F10
    cert_e = above(st.E[f_dec].mean, ceil_m)
~~
    cert_e = above(st.E[F20].mean, ceil_m)
```
```
@@ V33 | gread_table | the f = 0.20 cell marked as entering §5 under the cap | predicted: killed by GREAD-ENTERS-N2
                     "enters": GREAD_N2_LABEL if f == st.dmap.n2_decision_f() else None})
~~
                     "enters": GREAD_N2_LABEL if f == F20 else None})
```
```
@@ V34 | plan_cells | merged labels read under their own names | predicted: killed by RD-MERGED (reader group raises: schema refuses the cells)
              "+d_20": dmap.kept_label("d_20"), "+d_eq": dmap.kept_label("d_eq")}
~~
              "+d_20": "+d_20", "+d_eq": "+d_eq"}
```
```
@@ V35 | build_state | P computed only at ±1 | predicted: killed by RD-POSITIVE (dose STOPs at d_eq; reader group raises)
        p_labels = sorted({rid.split("|")[2] for rid in camp.planned["N1-P"]}, key=lambda lab: -lv[lab])
~~
        p_labels = ["+1", "-1"]
```
```
@@ V36 | load_campaign | any .npy beside the cells is accepted | predicted: killed by RD-REFUSE
    extra = sorted(set(names) - set(jsons) - captures)
~~
    extra = sorted(n for n in set(names) - set(jsons) - captures if not n.endswith(".npy"))
```
```
@@ V37 | failing_text | every failing condition rendered as the against form | predicted: killed by SENT-FAILING-NOTREP
    return "; ".join(CONJUNCT_TEXT["sign-against" if (k == "sign" and against) else k] for k in keys)
~~
    return "; ".join(CONJUNCT_TEXT["sign-against" if against else k] for k in keys)
```
```
@@ V38 | pinned_map_reach | shape (c) classified as (b) | predicted: killed by NUM-REACH-CLASS
    shape = "d" if r["d_eq"] == 1.0 else "b" if dmap.cap_binds() else "c" if m == 1.0 else "a"
~~
    shape = "d" if r["d_eq"] == 1.0 else "b" if r["d_20"] == 1.0 else "a"
```
```
@@ V39 | dose_outcome | the d_eq ceiling ignores P(d_eq) | predicted: killed by BND-P-DEQ
    ceq = ceiling_cert(st, deq)
~~
    ceq = ceiling(st.L[deq], None)
```
```
@@ V40 | D_ND_ANSWERED | the answered template loses its [movement] slot | predicted: killed by SENT-ADDENDUM and TUP-T2
D_ND_ANSWERED = T_DOSE_ND_ANSWERED.replace(OLD_MOVE, MOVE_SLOT)          # §5's answered form, amended
~~
D_ND_ANSWERED = T_DOSE_ND_ANSWERED.replace(OLD_MOVE, MOVE_NOT_CERTIFIED)          # §5's answered form, amended
```

## 2. The dispositions (every finding)

### Production code

- **F1 NOTE (PIN-n-29, per arm): registered, the scenario stated.** PIN-n-29 now names the consequence the reviewer
  describes: a read missing or non-finite elsewhere in N2's arms (an N1-P read at −1; an N1-R cell at +1/2) makes N2
  INDETERMINATE though its certification reads none of it; read point by point, N2 would be evaluated. The seat
  rules.
- **F2 NOTE (PIN-n-30, unsigned N2): registered, the scenario stated.** PIN-n-30 now names the SPECIFIC case (N1-V
  moving against the zone at the norm-matched point, the sentence saying it "does" move BK's apparatus) and its
  co-occurrence, when the cap binds, with a dose sentence naming the same movement as against the zone. The seat rules.
  (The values-check amended this text twice since; the register's text as committed is in §5.)
- **F3 NOTE (merged d_eq in the NOT-DETECTABLE forms): registered as PIN-n-32.** The three forms are verbatim (§7.6)
  and have no [value] slot; Code adds no words to them. PIN-n-32 says where the merge is reported instead (the dose
  outcome's point, G-LEAK-n's table, DETECTABLE's VALUE_MERGED) and leaves the note to the seat.
- **F4 NOTE (the with-intercept slope's label): fixed.** The figure carries `descriptive: true`; RD-ASYM asserts it.
- **F5 MINOR (INDETERMINATE dose, its d_20 beside): fixed.** The INDETERMINATE dose outcome carries
  `"d_20_beside": "not computed"`; OPEN-Q6's entry has the clause; DOSE-INDET-POINTS asserts it.
- **F6 NOTE (N2's beside lacks N1-V): fixed.** The beside carries N1-V's estimate at its point and its own
  certification (`V`, `certified_V`); N2-BESIDE-FIELDS asserts both shapes and a case where they differ from
  span_reward's.
- **F7 NOTE (the sign's name; the repeated figures): registered.** PIN-n-28 now names the sign's form as Code's and the
  repetition of Δm(+1) and its CI; the wording is the seat's to choose.
- **F8 NOTE (PIN-n-31's dependency): fixed in the text.** The PIN marks n-build's loader declaration as pending until
  its BUILD. (Since that BUILD, `83a50a0`, the PIN cites it: §5.)
- **F9 NOTE (State.P's comment): fixed.**
- **F10 NOTE (the artifact's spec string): fixed** ("ADDENDUM-n1 v0.1 §4-§7").
- **F11 NOTE (an answered NOT-DETECTABLE against the zone ends "an explanation of record for the program's null"):
  kept, for the seat.** The sentence is the seat's form; Code does not change it. It goes to the seat in the entry.

### The battery

- **B1 MAJOR: fixed.** SENT-FILLED-DOSE-ND fills the dose NOT-DETECTABLE sentence in its three forms, with the
  movement not certified and against the zone (six sentences), and compares each with literal text written in the
  battery.
- **B2 MAJOR: fixed.** SENT-FILLED-N1-AGAINST compares N1's filled NOT-REPLICATED sentence with literal text, for a
  certified movement against the zone and for a negative mean within the ceiling.
- **B3 MAJOR: fixed.** SENT-FILLED-N2-CAP compares N2's filled sentence where the cap binds with literal text (SHARED;
  SPECIFIC answered; its label under span_reward's G-READ-n FAIL at f = 0.10 and at f = 0.20).
- **B4 MINOR: fixed.** N1-NOTREP-iii-sign (a negative mean within the ceiling: not against); DOSE-ND-NEG-CI and
  DOSE-ND-NEG-UNCERT (a negative mean with a CI including 0, and one not certified: not against).
- **B5 MINOR: fixed.** RD-CAP-SLOPES checks N2's slope and floor in the cap-binding campaign against hand computations,
  the mismatch printed.
- **B6 MINOR: fixed.** DOSE-BESIDE-D20 adds a beside whose ceiling is P(d_20) and whose estimate lies between L and P.
- **B7 MINOR: fixed.** GLEAK-N1P-INCOMPLETE: with N1-P incomplete, the rows at its points are not computed and +1/2's
  is.
- **B8 MINOR: fixed.** N2-BESIDE-FIELDS: the beside's E is the other f's; an INDETERMINATE N2 names its decision f.
- **B9 NOTE: fixed.** STR-GANL-ARTIFACT asserts BOUND_RELS whole, the addendum in it.
- **B10 NOTE: fixed.** RD-CAP-BINDS' description now says it checks the label's input (the label itself is
  SENT-FILLED-N2-CAP's); SENT-FAILING-NOTREP asserts each form names no condition it does not fail; NUM-BK-REPRO's
  description says the floor is through the origin on the four nonzero points; RD-ASYM's N1-P reads +0.3 at +d_eq,
  so P(d_eq) is above L(d_eq) and the check asserts the dose ceiling is P's.
- **Beyond the findings (Code's):** RD-REFUSE adds a schema whose read plan is one read short of the analyzer's
  (refused), which no case reached before (M51).

## 3. The mutants and their run

**The set.** M01–M40 are the reviewer's V01–V40, applied as written (each old text checked to occur exactly once in
the fixed draft), except M17: its line in `n2_outcome` changed with F6's fix (the beside gained `V`), so M17 makes the
same change on the fixed line, the beside's `"E": st.E.get(f_bes)` becoming `st.E.get(f_dec)`. M41–M62 are Code's,
written against the fixed draft; they are reproduced whole below the table.

**The run.** The base was the fixed draft, frozen as a read-only copy at sha256
`9e7faea157aef3df0618b981173a7f79ae5e8c4a710094519bc68d956d34e4ce`, whose battery passed 207/207 with every one of
its 210 coverage ids reached. Each mutant ran once, one battery process at a time. All 62 were killed. In the table,
"killed" lists the coverage ids the mutant's run left unreached (the battery prints the first six, sorted), then each
group that raised and its exception. A group that raises stops its later checks, so their ids appear unreached too.
The thirteen runs with a group exception:
- **M03:** an AnlStop (a slot left) in the sentences group, inside SENT-FILLED-N1-AGAINST's fill, so
  SENT-FILLED-N2-CAP after it was not reached.
- **M27:** the AnlStop of the missing P(d_eq) in the outcomes, sentences and reachability groups. Four of the six
  reachability checks before the raise had failed, the outcome layer raising on the enumerated states (the
  dose-iff-N1 check and shape (d)'s, where d_eq sits at +1 and P exists, passed). NUM-N1P-POINTS also failed (its
  line; it is not among the first six ids).
- **M29:** an AnlStop in the verdicts group (no P(d) at d = 0.625, d_20's point): with N1-P no longer among N2's
  reads, N2 was evaluated where N1-P was incomplete. N2-INDET-incomplete:N1-P and RD-SHADOW had failed before.
- **M34, M44 and M52:** a KeyError in the reader path and verdicts groups: '+d_20' (M34), d_eq's own value where it
  merged into +1/2 (M44), 0.0 (M52). For M34 and M52 the KeyError came before the refusal and the STOP their
  predictions named; the predicted checks were left unreached all the same. M44's NUM-N2-POINTS had failed before.
- **M35:** an AnlStop in the reader path and verdicts groups (no P(d) at d = 0.3125, d_eq's point).
- **M43:** a KeyError ('f=0.10') in the outcomes group; NUM-CAP-DECISION-F failed (its line).
- **M47:** an AnlRefusal in the reader path and verdicts groups: the reader refused a plan its own derivation does
  not give.
- **M48:** an AnlRefusal in the reader path group: RD-REFUSE's accepted case raised, the files beside the cells
  refused.
- **M50:** a SchemaError in the verdicts group: the schema's `check_gread` refused the artifact's empty capture map.
  RD-REFUSE had failed before.
- **M55:** a KeyError in the reader path group: RD-ASYM's lookup of `descriptive` raised instead of failing the
  check alone.
- **M57:** a KeyError in the commands group: CMD-NOTRUN's lookup of `addendum_sha256`.

| Mutant | From | Function | What breaks | Predicted (by its author) | Result: the coverage ids the run left unreached (the battery prints the first six, sorted), and any group exception |
|---|---|---|---|---|---|
| M01 | V01 | `fill` | the against clause is never printed in a dose sentence | survives | killed: SENT-FILLED-DOSE-ND |
| M02 | V02 | `fill` | every NOT-DETECTABLE sentence says "moves against the conditioned zone" | survives | killed: SENT-FILLED-DOSE-ND |
| M03 | V03 | `fill` | [c] is left in a NOT-REPLICATED-against sentence, so the analyzer STOPs | survives | killed: SENT-FILLED-N1-AGAINST, SENT-FILLED-N2-CAP; AnlStop raised in the sentences group |
| M04 | V04 | `fill` | N1's sentence drops the seat's against clause | survives | killed: SENT-FILLED-N1-AGAINST |
| M05 | V05 | `fill` | when the cap binds, N2's Δm and CI come from f = 0.20 | survives | killed: SENT-FILLED-N2-CAP |
| M06 | V06 | `fill` | N2's sentence says "at f = 0.20" when decided at 0.10 | survives | killed: SENT-FILLED-N2-CAP |
| M07 | V07 | `F_TEXT` | the f = 0.10 fill reads "0.20" | survives | killed: SENT-FILLED-N2-CAP |
| M08 | V08 | `n1_outcome` | "against" without (iii): claims "beyond the leak ceiling" when it is not | survives | killed: N1-NOTREP-iii-sign, SENT-FILLED-N1-AGAINST |
| M09 | V09 | `dose_outcome` | "against" with a CI that includes 0 | survives | killed: DOSE-ND-NEG-CI |
| M10 | V10 | `dose_outcome` | "against" without G-LEAK-n certification | survives | killed: DOSE-ND-NEG-UNCERT |
| M11 | V11 | `dose_outcome` | the d_20 beside ignores P(d_20) | survives | killed: DOSE-BESIDE-D20 |
| M12 | V12 | `gleak_table.needs` | a G-LEAK-n row at d_eq or d_20 certified against L alone when N1-P is incomplete | survives | killed: GLEAK-N1P-INCOMPLETE |
| M13 | V13 | `build_state` | the mismatch on N2's floor points under the cap or a merge is never printed | survives | killed: RD-CAP-SLOPES |
| M14 | V14 | `build_state` | the mismatch on N2's slope points is never printed | survives | killed: RD-CAP-SLOPES |
| M15 | V15 | `build_state` | N2's floor fitted at 2·d_eq for reads taken at +1 | survives | killed: RD-CAP-SLOPES |
| M16 | V16 | `build_state` | N2's slope fitted on the kept points, not (d_eq, 2·d_eq) | survives | killed: RD-CAP-SLOPES |
| M17 | V17 | `n2_outcome` | the beside reports the decision f's estimate | survives | killed: N2-BESIDE-FIELDS |
| M18 | V18 | `BOUND_RELS` | a canonical ganl run no longer requires the addendum committed | survives | killed: STR-GANL-ARTIFACT |
| M19 | V19 | `n2_outcome` | an INDETERMINATE N2 under the cap reports f = 0.20 | survives | killed: N2-BESIDE-FIELDS |
| M20 | V20 | `dose_outcome` | a negative certified movement becomes DETECTABLE | killed by DOSE-ND-AGAINST | killed: DOSE-ND-AGAINST, SENT-FILLED-DOSE-ND |
| M21 | V21 | `n1_outcome` | a negative certified movement becomes PARTIAL | killed by N1-NOTREP-sign (and BND-NEG-CERT) | killed: BND-NEG-CERT, N1-NOTREP-sign, NUM-REACH-CLASS, REACH-SHAPE-d, SENT-FILLED-N1-AGAINST |
| M22 | V22 | `n1_outcome` | "against" with a CI that includes 0 | killed by N1-NOTREP-ci+1-sign | killed: N1-NOTREP-ci+1-sign |
| M23 | V23 | `build_state.slope_est` | slopes of record fitted with an intercept | killed by RD-ASYM | killed: RD-ASYM, RD-CAP-SLOPES |
| M24 | V24 | `build_state` | the with-intercept beside fitted without the d = 0 point | killed by RD-ASYM | killed: RD-ASYM |
| M25 | V25 | `outcomes` | N2's label reads span_reward at f = 0.20 under the cap | killed by RD-CAP-BINDS | killed: RD-CAP-BINDS, SENT-FILLED-N2-CAP |
| M26 | V26 | `DoseMap.cap_binds` | the cap binds at 2·d_eq = 1 | killed by NUM-CAP-DECISION-F | killed: NUM-CAP-DECISION-F |
| M27 | V27 | `DoseMap.n1p_points` | P(d_eq) never required | killed by NUM-N1P-POINTS | killed: BND-CERT-EQUAL, BND-CI-HI-ZERO, BND-CI-LO-ZERO, BND-I-BELOW, BND-I-EXACT, BND-IV-ZERO; AnlStop raised in the outcomes group; AnlStop raised in the sentences group; AnlStop raised in the reachability group |
| M28 | V28 | `ceiling_cert` | a missing P(d) silently falls back to L | killed by BND-P-REQUIRED | killed: BND-P-REQUIRED |
| M29 | V29 | `n2_outcome` | an incomplete N1-P no longer makes N2 INDETERMINATE | killed by N2-INDET-incomplete:N1-P | killed: N2-INDET-incomplete:N1-P, RD-SHADOW, VD-GREAD-MIXED, VD-MERGED-ROUTE-A, VD-NOTRUN-CAP, VD-NOTRUN-GVER; AnlStop raised in the verdicts group |
| M30 | V30 | `n2_outcome` | the beside's ceiling is L alone | killed by RD-CAP-BINDS | killed: RD-CAP-BINDS |
| M31 | V31 | `n2_outcome` | decided at d_20's point under the cap | killed by N2-MATCH-RATIO | killed: N2-MATCH-RATIO, NUM-REACH-CLASS, RD-CAP-BINDS, REACH-SHAPE-b, SENT-FILLED-N2-CAP |
| M32 | V32 | `n2_outcome` | span_reward certified at f = 0.20 under the cap | killed by N2-CAP-F10 | killed: N2-CAP-F10, NUM-REACH-CLASS, REACH-SHAPE-b, REACH-SHAPE-d, SENT-FILLED-N2-CAP |
| M33 | V33 | `gread_table` | the f = 0.20 cell marked as entering §5 under the cap | killed by GREAD-ENTERS-N2 | killed: GREAD-ENTERS-DOSE, GREAD-ENTERS-N1, GREAD-ENTERS-N2 |
| M34 | V34 | `plan_cells` | merged labels read under their own names | killed by RD-MERGED (reader group raises: schema refuses the cells) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; KeyError raised in the reader path group; KeyError raised in the verdicts group |
| M35 | V35 | `build_state` | P computed only at ±1 | killed by RD-POSITIVE (dose STOPs at d_eq; reader group raises) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-FILLED, RD-FILLED-FIGURES; AnlStop raised in the reader path group; AnlStop raised in the verdicts group |
| M36 | V36 | `load_campaign` | any .npy beside the cells is accepted | killed by RD-REFUSE | killed: RD-REFUSE |
| M37 | V37 | `failing_text` | every failing condition rendered as the against form | killed by SENT-FAILING-NOTREP | killed: SENT-FAILING-NOTREP |
| M38 | V38 | `pinned_map_reach` | shape (c) classified as (b) | killed by NUM-REACH-CLASS | killed: NUM-REACH-CLASS |
| M39 | V39 | `dose_outcome` | the d_eq ceiling ignores P(d_eq) | killed by BND-P-DEQ | killed: BND-P-DEQ, BND-P-REQUIRED, RD-ASYM |
| M40 | V40 | `D_ND_ANSWERED` | the answered template loses its [movement] slot | killed by SENT-ADDENDUM and TUP-T2 | killed: SENT-ADDENDUM, SENT-FILLED-DOSE-ND, TUP-T2, TUP-T8 |
| M41 | Code | `session_slopes_origin` | the zero point accepted | killed by NUM-SLOPE-CLOSED-FORM | killed: NUM-SLOPE-CLOSED-FORM |
| M42 | Code | `session_slopes_origin` | divided by the point count, not by Σd² | killed by NUM-SLOPE-CLOSED-FORM | killed: NUM-BK-FITS-COINCIDE, NUM-BK-REPRO, NUM-SLOPE-CLOSED-FORM, NUM-SLOPE-INTERCEPT, RD-ASYM, RD-CAP-SLOPES |
| M43 | Code | `DoseMap.n2_decision_f` | the decision f inverted | killed by NUM-CAP-DECISION-F | killed: GREAD-ENTERS-DOSE, GREAD-ENTERS-N1, GREAD-ENTERS-N2, N2-BESIDE-FIELDS, N2-CAP-F10, N2-F10-BESIDE; KeyError raised in the outcomes group |
| M44 | Code | `DoseMap.n2_slope_points` | N2's floor taken at the program-scale points | killed by NUM-N2-POINTS | killed: CNT-COUNTERS, NUM-N2-POINTS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD; KeyError raised in the reader path group; KeyError raised in the verdicts group |
| M45 | Code | `dose_outcome` | an INDETERMINATE dose drops its not-computed beside | killed by DOSE-INDET-POINTS | killed: DOSE-INDET-POINTS |
| M46 | Code | `n2_outcome` | the beside's valence certified with span_reward's estimate | killed by N2-BESIDE-FIELDS | killed: N2-BESIDE-FIELDS |
| M47 | Code | `plan_cells` | a keeper read twice under a merge | killed by RD-MERGED and RD-CAP-BINDS (the reader refuses the plan) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; AnlRefusal raised in the reader path group; AnlRefusal raised in the verdicts group |
| M48 | Code | `load_campaign` | no capture file accepted by name | killed by RD-REFUSE (the accepted case raises) | killed: RD-REFUSE; AnlRefusal raised in the reader path group |
| M49 | Code | `load_campaign` | a capture file at any layer accepted | killed by RD-REFUSE (capture-layer) | killed: RD-REFUSE |
| M50 | Code | `load_campaign` | the cell's capture map not carried | killed by RD-REFUSE (accepted case) and VD-COMPLETE | killed: RD-REFUSE, VD-COMPLETE, VD-EXPOSURE, VD-GREAD-MIXED, VD-MERGED-ROUTE-A, VD-NOTRUN-CAP; SchemaError raised in the verdicts group |
| M51 | Code | `load_campaign` | the schema's plan never compared with the analyzer's | killed by RD-REFUSE (plan) | killed: RD-REFUSE |
| M52 | Code | `build_state` | d = 0 among the slopes' points | killed by RD-POSITIVE (a STOP in the reader group) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-FILLED, RD-FILLED-FIGURES; KeyError raised in the reader path group; KeyError raised in the verdicts group |
| M53 | Code | `map_reach` | span_reward varied at f = 0.20 on every map | killed by REACH-SHAPE-b | killed: NUM-REACH-CLASS, REACH-SHAPE-b, REACH-SHAPE-d |
| M54 | Code | `pinned_map_reach` | shape (c) classified as (a) | killed by NUM-REACH-CLASS | killed: NUM-REACH-CLASS |
| M55 | Code | `build_state` | the with-intercept figure not marked descriptive | killed by RD-ASYM | killed: CNT-COUNTERS, RD-ASYM, RD-GREAD, RD-GREAD-MIXED, RD-MERGED-DEQ, RD-PAUSE; KeyError raised in the reader path group |
| M56 | Code | `secondaries` | secondary (b) reported as not recorded, not struck | killed by RD-SECONDARY | killed: RD-SECONDARY |
| M57 | Code | `not_run_doc` | the NOT-RUN output does not bind ADDENDUM-n1 | killed by CMD-NOTRUN | killed: CMD-GANL-REFUSE, CMD-NOTRUN, CMD-NOTRUN-REFUSE, STR-GANL-ARTIFACT; KeyError raised in the commands group |
| M58 | Code | `run_verdicts` | VERDICTS does not bind ADDENDUM-n1 | killed by VD-COMPLETE | killed: VD-COMPLETE |
| M59 | Code | `D_ND_NOT_READABLE` | the not-readable form keeps §5's clause | killed by SENT-ADDENDUM and SENT-FILLED-DOSE-ND | killed: SENT-ADDENDUM, SENT-FILLED-DOSE-ND, TUP-T2 |
| M60 | Code | `D_ND_READABLE_N4` | the A.6 form keeps its fixed clause, so a movement against is never named there | killed by SENT-FILLED-DOSE-ND and SENT-ADDENDUM | killed: SENT-ADDENDUM, SENT-FILLED-DOSE-ND, TUP-T2 |
| M61 | Code | `sentence_dose` | the answered form labelled §5's, unamended | killed by TUP-T10 and RD-GREAD-MIXED | killed: RD-GREAD-MIXED, TUP-T10, TUP-T2 |
| M62 | Code | `DoseMap.n1p_points` | +1/2 always among N1-P's points | killed by NUM-N1P-POINTS and BND-P-REQUIRED | killed: BND-P-REQUIRED, GLEAK-N1P-INCOMPLETE, NUM-N1P-POINTS |

**Code's mutants M41–M62**, as run (each old text occurs exactly once in the base; an empty new text deletes it):

```
@@ M41 | session_slopes_origin | the zero point accepted | predicted: killed by NUM-SLOPE-CLOSED-FORM
    if np.any(x == 0.0):
        raise AnlStop("STOP: a slope through the origin given the point d = 0")
~~
```
```
@@ M42 | session_slopes_origin | divided by the point count, not by Σd² | predicted: killed by NUM-SLOPE-CLOSED-FORM
    return y @ x / float(x @ x)
~~
    return y @ x / float(len(x))
```
```
@@ M43 | DoseMap.n2_decision_f | the decision f inverted | predicted: killed by NUM-CAP-DECISION-F
        return F10 if self.cap_binds() else F20
~~
        return F20 if self.cap_binds() else F10
```
```
@@ M44 | DoseMap.n2_slope_points | N2's floor taken at the program-scale points | predicted: killed by NUM-N2-POINTS
        return ((self.d_eq, 2.0 * self.d_eq), (self.norm_matched(F10), self.norm_matched(F20)))
~~
        return ((self.d_eq, 2.0 * self.d_eq), (self.d_eq, 2.0 * self.d_eq))
```
```
@@ M45 | dose_outcome | an INDETERMINATE dose drops its not-computed beside | predicted: killed by DOSE-INDET-POINTS
        return {"state": "INDETERMINATE", "causes": causes, "d_20_beside": "not computed"}   # OPEN-Q6 as ruled
~~
        return {"state": "INDETERMINATE", "causes": causes}
```
```
@@ M46 | n2_outcome | the beside's valence certified with span_reward's estimate | predicted: killed by N2-BESIDE-FIELDS
                      "certified_V": above(st.V[mb].mean, cb) if mb in st.V else None,
~~
                      "certified_V": above(st.E[f_bes].mean, cb) if mb in st.V else None,
```
```
@@ M47 | plan_cells | a keeper read twice under a merge | predicted: killed by RD-MERGED and RD-CAP-BINDS (the reader refuses the plan)
                    if keeper[lab] not in labs:
                        labs.append(keeper[lab])
~~
                    labs.append(keeper[lab])
```
```
@@ M48 | load_campaign | no capture file accepted by name | predicted: killed by RD-REFUSE (the accepted case raises)
        captures |= set(cell["capture_files"].values())
~~
        captures |= set()
```
```
@@ M49 | load_campaign | a capture file at any layer accepted | predicted: killed by RD-REFUSE (capture-layer)
        captures |= set(cell["capture_files"].values())
~~
        captures |= {sm.capture_filename(n, x) for x in range(64)}
```
```
@@ M50 | load_campaign | the cell's capture map not carried | predicted: killed by RD-REFUSE (accepted case) and VD-COMPLETE
        cap = dict(cell["capture_sha256"])
~~
        cap = {}
```
```
@@ M51 | load_campaign | the schema's plan never compared with the analyzer's | predicted: killed by RD-REFUSE (plan)
    if plan != own_plan(dmap):
~~
    if False and plan != own_plan(dmap):
```
```
@@ M52 | build_state | d = 0 among the slopes' points | predicted: killed by RD-POSITIVE (a STOP in the reader group)
    nz_pts = [pt for pt in v_pts if pt != 0.0]                            # the nonzero points, the fits' (OPEN-Q1)
~~
    nz_pts = list(v_pts)
```
```
@@ M53 | map_reach | span_reward varied at f = 0.20 on every map | predicted: killed by REACH-SHAPE-b
    fd = dmap.n2_decision_f()
~~
    fd = F20
```
```
@@ M54 | pinned_map_reach | shape (c) classified as (a) | predicted: killed by NUM-REACH-CLASS
    shape = "d" if r["d_eq"] == 1.0 else "b" if dmap.cap_binds() else "c" if m == 1.0 else "a"
~~
    shape = "d" if r["d_eq"] == 1.0 else "b" if dmap.cap_binds() else "a"
```
```
@@ M55 | build_state | the with-intercept figure not marked descriptive | predicted: killed by RD-ASYM
                fig["slope_V_with_intercept"] = dict(est_i.as_json(), descriptive=True)   # OPEN-Q1 as ruled
~~
                fig["slope_V_with_intercept"] = est_i.as_json()
```
```
@@ M56 | secondaries | secondary (b) reported as not recorded, not struck | predicted: killed by RD-SECONDARY
    out["b_free_text"] = B_STRUCK
~~
    out["b_free_text"] = "not recorded: n §2.1 'No new text is generated for N1, N2 or N4' (the schema's reading 7)"
```
```
@@ M57 | not_run_doc | the NOT-RUN output does not bind ADDENDUM-n1 | predicted: killed by CMD-NOTRUN
            "proposal_sha256": PROPOSAL_SHA256, "addendum_sha256": ADDENDUM_SHA256,
~~
            "proposal_sha256": PROPOSAL_SHA256,
```
```
@@ M58 | run_verdicts | VERDICTS does not bind ADDENDUM-n1 | predicted: killed by VD-COMPLETE
    base = {"unit": UNIT, "date": date, "proposal_sha256": PROPOSAL_SHA256, "addendum_sha256": ADDENDUM_SHA256,
~~
    base = {"unit": UNIT, "date": date, "proposal_sha256": PROPOSAL_SHA256,
```
```
@@ M59 | D_ND_NOT_READABLE | the not-readable form keeps §5's clause | predicted: killed by SENT-ADDENDUM and SENT-FILLED-DOSE-ND
D_ND_NOT_READABLE = C_DOSE_ND_NOT_READABLE.replace(OLD_MOVE, MOVE_SLOT)  # A.5, amended
~~
D_ND_NOT_READABLE = C_DOSE_ND_NOT_READABLE  # A.5, amended
```
```
@@ M60 | D_ND_READABLE_N4 | the A.6 form keeps its fixed clause, so a movement against is never named there | predicted: killed by SENT-FILLED-DOSE-ND and SENT-ADDENDUM
D_ND_READABLE_N4 = A6_DOSE_ND_READABLE_N4.replace(MOVE_NOT_CERTIFIED, MOVE_SLOT)
~~
D_ND_READABLE_N4 = A6_DOSE_ND_READABLE_N4
```
```
@@ M61 | sentence_dose | the answered form labelled §5's, unamended | predicted: killed by TUP-T10 and RD-GREAD-MIXED
            t, form = D_ND_ANSWERED, "§5, amended by ADDENDUM-n1 §7.6"
~~
            t, form = D_ND_ANSWERED, "§5"
```
```
@@ M62 | DoseMap.n1p_points | +1/2 always among N1-P's points | predicted: killed by NUM-N1P-POINTS and BND-P-REQUIRED
        return tuple(sorted({1.0, -1.0, r["d_20"], r["d_eq"]}, reverse=True))
~~
        return tuple(sorted({1.0, -1.0, 0.5, r["d_20"], r["d_eq"]}, reverse=True))
```

**M17 as re-expressed** (old, then new):

```
    beside = {f_bes: {"point": mb, "E": st.E.get(f_bes), "V": st.V.get(mb), "ceiling": cb,       # ADDENDUM-n1 §5.3
~~
    beside = {f_bes: {"point": mb, "E": st.E.get(f_dec), "V": st.V.get(mb), "ceiling": cb,       # ADDENDUM-n1 §5.3
```

## 4. The battery runs

All in battery windows the coordinating session granted; one process at a time, `nice -n 19`, `-I`, with temp folders
outside the repository, in the foreground but for one batch of mutants (below); nothing ran on a model or on the box.
The runs named here ran on the working copy of the draft; each frozen copy was made from it, unchanged, after its run.

- **Step 1** (against the schema at `14e65d8`), two runs. The first: 192/197. The form digest had moved, as the forms
  had; two reader expectations followed the rulings (N2's causes now include N1-P's; the dose forms are labelled
  "amended by ADDENDUM-n1 §7.6"); the coverage check followed from those; and the count check failed on its own,
  EXPECTED_CHECKS still reading `bedc198`'s 185 against 197 checks. Before the second run, the digest was set from
  that run's printed value, EXPECTED_CHECKS to 197, and the two reader expectations to the rulings; the second run:
  197/197.
- **Step 2** (against the schema at `d791bd9`), two runs. The first: 197/198, the expected count alone (it still read
  197 for the one new check); the second: 198/198. That draft was frozen for the review.
- **The mutant window.** One run of the fixed draft (207/207), then the 62 mutants (§3), in batches, each a tool call
  that ran its mutants one after another. A first attempt at the first batch ran no Python: the base had been frozen
  read-only, the runner's copies inherited the mode, and its patch step refused to write them (each reported as an
  apply failure). The runner was changed to make its copies writable, and the batch ran again from M01. That batch
  (M01–M09) reached the tool's 10-minute limit during M08: the harness moved the call to the background, where M08
  and M09 finished, one process at a time as before. The later batches, M10–M15 to M58–M62, six mutants each (the
  last five), ran in the foreground.
- **The run of record** is the entry's, from `scripts/n_analyze.py` on the committed bytes.

## 5. The committed bytes against the mutation-tested base

The committed `scripts/n_analyze.py` differs from the mutant base (`9e7faea1…e4ce`) in the repository line and in
four texts.
- **The repository line.** The base, a scratch file, read the repository at its absolute path; the committed file
  reads it from its own location, as the committed analyzer always has:

  ```
  REPO = Path(__file__).resolve().parents[1]                     # scripts/n_analyze.py -> the repository
  ```
- **PIN-n-30's text.** The values-check's first pass found that its "gives SPECIFIC" holds only while span_reward is
  not certified (SHARED otherwise); its second pass, that G-LEAK-n's certification has no CI condition, so SPECIFIC
  also follows a valence movement beyond the ceiling whose CI includes 0, which the dose sentence at the same point
  (where the cap binds) calls not certified; its third, that the dose sentence says either only if the dose question
  is evaluated. The register's text now states all three.
- **PIN-n-31's text.** It said n-build's loader declaration was pending until n-build's BUILD; it now cites that
  BUILD, `83a50a0`, whose entry declares the PIN.
- **PIN-n-32's text.** The third pass found that under the sign rule the clause prints "Δm = [x]", not "Δm(d_eq)";
  the text now says both.
- **`plan_cells`'s docstring.** The second pass found that "+1/2 where d_eq folds there" missed +1/2 where d_20 folds
  there; it now says "+1/2 where d_20 or d_eq folds there".

The four texts change no logic. No check depends on their words: STR-PINS scans the source only for PIN and OPEN
names, compares the registered names with those cited, and the edits add or remove none. No outcome, sentence or
form changes; the register is carried into the outputs as text.
