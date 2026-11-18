# n_analyze.py, the seat's ruling of 2026-11-18 on PIN-n-27 to PIN-n-32 and F11: the blind review, its mutants and the dispositions (PI date 2026-11-18)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's ruling on PIN-n-27 to PIN-n-32 and F11`.

- **What changed under review.** Against the committed analyzer (`977b78b`, sha256 `97097ce0…251e`), the draft carries
  §5 of the seat's answers of 2026-11-18,
  `results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md` (sha256 `5843a9bd…7165`, committed at `26cf7d2`):
  - PIN-n-27, PIN-n-28 and PIN-n-31 accepted (§5.1);
  - N2's causes read point by point (§5.2, PIN-n-29 amended);
  - each N2 figure with its CI and the zone's words (§5.3, PIN-n-30 accepted with its sentences amended);
  - the merge note in the NOT-DETECTABLE forms (§5.4, PIN-n-32 amended);
  - the fourth NOT-DETECTABLE form (§5.6, F11 ruled);
  - the forms' digest moved (§5.1).
  It was drafted in one step and run in a battery window the coordinating session granted: 214/217, then 217/217.
- **The review, blind.** A reviewer read that draft, frozen as a read-only copy at sha256 `51396daf…fc41` (217/217 on
  those bytes, every one of its 220 coverage ids reached).
  - It was a subagent of this session, under a brief that quoted the list of record v2's items 1–5 and allowed no
    Python.
  - Its spec: the answers raw's §5 and §7 item 6; the entry of `977b78b` and its review raw, for what the seat ruled
    on; ADDENDUM-n1 v0.1 §7; PROPOSAL-n v0.2 §0.6, §3 and §5; and `valence_core/n/schema.py`.
  - It executed no code (it read files and computed digests) and opened nothing under `data/`.
  - It returned production findings F1–F8 (F1 MINOR, a question for the seat; F2–F8 NOTEs; no MAJOR) and battery
    findings B1–B7 (B1–B2 MINOR, B3–B7 NOTEs), with 35 mutants, V01–V35. It predicted that 8 of them would survive
    the frozen copy: V08, V12, V14, V15, V16, V17, V18 and V24 (§1).
- **The dispositions** (§2).
  - F1: the draft carries §5.2's pause rule as written. Its two departures from rulings of record go to the seat as a
    question; PIN-n-33 quotes both.
  - Registered: F2, F3 and F7 in PIN-n-36's text; F8 in PIN-n-34's.
  - Fixed: F5, F6 and B1–B7.
  - Kept, for the seat: F4, a question on the seat's own form.
  - Beyond the findings, Code added two cases after the freeze: the dose sentence's own refusal of the new input, and
    a TAU/4 row that empties a point.
- **The mutants** (§3). M01–M35 are V01–V35, verbatim. M36–M54 are 19 of the 39 Code wrote while the review ran; Code
  dropped the other 20 as overlapping the reviewer's (§3 names them). They ran once, on the fixed draft (sha256
  `285c6168…87db`, 217/217): **54 of 54 killed.** The 8 the reviewer predicted would survive are each killed by a check
  the dispositions added or extended.
- **The battery runs** (§4) and **the committed bytes** (§5). The committed file differs from the mutation-tested
  base in the repository line and, from the values-check, in nine texts and one battery comparand (§5).
- **The tallies, by hand** (§6): the derivation that `_bt_expected_tallies` cites.

Every Python run here was inside a battery window the coordinating session granted: one process at a time,
`nice -n 19`, `-I`, temp folders outside the repository, in the foreground. Nothing ran on a model or on the box.
Each mutant was applied to a fresh copy of its base as an exact text replacement (`.old` → `.new`), asserted to occur
once. That copy's battery then ran with `--selftest`; "killed" means a non-zero exit.

## 1. The reviewer's report, as saved from its hand-back (unedited)

The reviewer returned its report as its final message. Code saved it by script from the subagent's transcript (sha256
`2104634c…acb4`); its headings are moved down two levels here, and nothing else is changed. Line numbers in it are the
frozen copy's.

**Blind review of the frozen n_analyze draft against the seat's answers of 2026-11-18, §5 and §7 item 6**

I checked the frozen copy with shasum: 51396dafcfe2e05246bc3acdb8a4c73543d3b6607d54bbc4a8bf5e514123fc41, equal to the stated hash. I ran no Python, edited nothing and wrote no file. Paths below are REPO- or SCRATCH-relative, as the brief defines them.

#### What checks out

- **§5.2.**
  - `n2_reads` (518–522) lists exactly the reads N2's certification uses: N2-E at the decision f, and N1-V, N1-R and N1-P at the norm-matched point. For N1-R, `build_state` groups a point's read ids across all 24 directions.
  - `n2_outcome` (539) is INDETERMINATE iff one of those reads is not usable or a pause stands on its arm.
  - An incompleteness elsewhere leaves N2 decided: N1-P at −1 or +1, N1-R at +1/2, N1-V at −1, or N2-E at the other f.
  - N1 (`_causes`) and dose (`complete`) stay per arm and are unchanged.
  - The other f's E, V, ceiling and both certifications are "not computed" exactly where their own reads are not usable.
  - Per-arm statistics are computed on a complete arm only: N1-V's two slopes, N1-R's floor, N2's floor and the N2 arms' slopes.
- **Point-by-point usability** (`build_state`, 2844–2855 and 2880–2886).
  - The causes are: a read absent ("incomplete"), non-finite ("nonfinite"), a bad shadow of any session the arm reads ("shadow"; N1-R checks its 40 floor sessions), or a point emptied in the TAU/4 row ("tau4-emptied").
  - Statistics are computed only at usable points.
  - On reader input, every lookup in `n2_outcome`, `gleak_table`, `fill` and `secondaries` is gated by the same `st.at` entry that gated the statistic's computation, so none can miss.
- **Complete campaign.** The primary row computes exactly 977b78b's statistics: the same Δm vectors, `boot_index` keys and counts, and insertion order of V, L, P, E, S, C and `fig`; `st.at` is all `[]`.
- **Sentence forms, byte for byte.** I rebuilt FOURTH, `_ORC_FOURTH`, DEQ_FIGURE+MERGE_NOTE, `_ORC_NOTE`, ZONE_WORDS and SPECIFIC's valence clause from the module's literal lines and matched each with `grep -F` against the raw.
  - All are byte-equal; Δ is U+0394 in both files and the apostrophes are straight.
  - C_N2's three forms are 977b78b's A.7 text with only [CIE], [CIV], [zoneE] and [zoneV] added.
  - The battery's own literal strings also equal the raw: the fourth form in SENT-FILLED-DOSE-FOURTH, `spec_v`, and the note in SENT-FILLED-DOSE-ND.
- **The fourth form** is selected exactly when the dose's `against` holds (CI excludes 0, certified, mean below 0).
  - Readability follows G-READ-n at d_eq; the label follows §0.6.
  - It contains no "explanation of record".
  - [merge] follows the figure in all four NOT-DETECTABLE forms, and `merge_text` mirrors `value_text`.
  - `fill` leaves no slot: every new slot is in SLOTS and the STOP on leftovers stands.
- **Counts, re-derived by hand.**
  - 2,561 evaluations: the 128 NOT-DETECTABLE tuples give 640 evaluations, which the fourth input doubles.
  - T10's tallies: 64 answered, then 64/576 in 7.1 and 7.3, and 512 × 5 for N4.
  - 217 checks = 207 + 10, and 220 coverage ids = 210 + 10; both match the diff.
- **Register texts.**
  - PIN-n-29, -30 and -32 say what §5.2–§5.4 rule.
  - PIN-n-34, -35 and -36 are each needed and describe the code.
  - §5.5 is correctly untouched.

#### Findings — production code

**F1 MINOR (seat-level) — `n2_outcome` line 539; PIN-n-33 (2358–2363).**
- **What changed.** The pause rule moved both ways:
  - pauses on N1-V, N1-R or N1-P now make N2 INDETERMINATE;
  - a pause on N2-S or N2-C alone no longer does.
- **Its ground** is §5.2's "iff … or a pause stands on one of them", which answered PIN-n-29, an incompleteness question.
- **The N1 half reverses an explicit ruling.**
  - The prebuild block's Q6 said: "A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable, as written".
  - The seat's 2026-11-16 answers §1.6 accepted it: "leaves N2 evaluable only in the case the block names, where those arms are nonetheless complete".
  - 977b78b's removed check N2-NOT-PAUSED-BY-N1 encoded it: "their pauses are not".
- **The guard half departs from n:140**, "an unadjudicated pause stands on N2's reads"; N2-S and N2-C are N2's arms (n §2.4).
- PIN-n-33 cites neither text; it states only what 977b78b did.
- **Scenario.** PI-STOP with an unadjudicated binomial pause scoped to N1-R (PIN-n-24 lets it through), all arms complete.
  - 977b78b and the 2026-11-16 ruling decide N2.
  - The draft gives INDETERMINATE (pause:N1-R).
  - Conversely, a pause scoped to N2-S alone now leaves N2 decided.
- **Fix.** Keep the code if the seat confirms. Amend PIN-n-33 to quote §1.6 and n:140 and to say they are reversed on §5.2's "iff", and put the question to the seat in the entry, not only as a strikable reading.

**F2 NOTE — `build_state` `arm_emptied` (2866–2868; called at 2910 and 2935); PIN-n-36.**
- "tau4-emptied" now names two events:
  - a point left with no session, which is recorded in `st.at`;
  - a slope with no common session, which marks the arm only, so its points stay usable.
- So the TAU/4 sensitivity row now decides N2 where 977b78b had INDETERMINATE.
- On VD-SENSITIVITY's own campaign the sensitivity tuple moves from (INDET, INDET, INDET, PASS, PASS) to (INDET, INDET, SHARED, PASS, PASS).
- This is consistent with §5.2 (N2 reads no slope), but PIN-n-36 does not say so. Fix: add one clause to it.

**F3 NOTE — `build_state` 2928–2946 (`floors_N2`).**
- N2's floor reads N1-R only at d_eq's and d_20's kept points, yet it is computed only on a complete N1-R. An N1-R gap at −1 withholds it while N2 itself is decided.
- §5.2's reason for keeping N1 per arm ("an arm whose slopes read every point") does not cover a two-point slope.
- Fix: compute it when those two points are usable, or name the choice explicitly. PIN-n-36 says only "floors".

**F4 NOTE — `sentence_dose` 760–761; FOURTH.**
- The fourth form's text is identical in the answered cell and in the (G-READ-n PASS, N4 not PASS) cell.
  - The §0.6 label lives only in the record's `label` field.
  - N4's state is not printed; A.6 printed "(N4 [n4])".
- §5.6 says "the *answered* label by §0.6 as the others", and N1's and N2's forms print "— [label]".
- **Scenario.** N4 DEAD, G-READ-n PASS, Δm(d_eq) −0.30 [−0.40, −0.20]: nothing in the text marks the result as concluded, not answered.
- Fix: none in code, since the form is the seat's verbatim. Ask the seat whether the field suffices.

**F5 NOTE — registers.**
- OPEN-Q3 (2389–2391) still gives the (G-READ-n PASS, N4 not PASS) cell "its own sentence (A.6 …)". That holds only when no movement is certified against the zone, and A.6 now carries §5.4's note.
- OPEN-Q6 (2397–2401) omits §5.2's clause on N2's beside, "reported as not computed where its reads are missing"; PIN-n-29 carries it.
- The comment above OPEN (2382–2383) names only the 2026-11-16 answers and ADDENDUM-n1, though Q4, Q6 and Q8 now cite 2026-11-18.
- OPEN-Q4 appends Code's PIN-n-35 to a "confirmed" ruling. It is labelled, so this is acceptable.

**F6 NOTE — docstrings.**
- `delta_m` (2793–2794) says "Called only on a usable arm"; it is now called on usable points of incomplete arms.
- `map_reach` (1935–1936) says its N1-R-at-+1/2 pattern leaves N2 evaluated. That is false where the cap binds and d_eq folds into +1/2 (R_ell 39.78, as in RD-MERGED-DEQ), because +1/2 is then N2's decision point. The effect is harmless: the N1-P −1 pattern still reaches those triples.

**F7 NOTE — `n2_outcome` 540–541.**
- An INDETERMINATE N2 carries no beside at all, as at 977b78b; an INDETERMINATE dose reports `d_20_beside: "not computed"`.
- **Scenario.** N2-E's f = 0.20 cell is missing on shape (a), while f = 0.10's reads are all usable. They are never reported.
- This is the seat's call if §5.2's last sentence is meant to hold whatever N2's state.

**F8 NOTE — PIN-n-34's placement.**
- The zone words go after "against [c]", producing "(Δm = −0.3000 nats […] against 0.0500, against the conditioned zone)".
- The seat's SPECIFIC pattern puts them right after the CI. The reading is registered; raise the double "against" with the seat.

#### Findings — the battery

**B1 MINOR — `n2_outcome`'s beside, read point by point (548).**
- Every check on a decided N2 with an unusable read puts that read at the beside's own point (N2-BESIDE-NOT-COMPUTED, and RD-POINTWISE's pw3). There, per-arm and per-point agree.
- RD-INDET, pw1 and N2-POINT-ELSEWHERE assert states only.
- So V08 survives: the beside judged per arm, as 977b78b did.
- Fix: in pw1 and N2-POINT-ELSEWHERE, assert that beside[F10]'s E, V, ceiling, certified and certified_V are all computed.

**B2 MINOR — `emptied_at`'s true branch is never reached.**
- No check empties a point in the TAU/4 row: RD-SENSITIVITY keeps at least 119 sessions per point, and VD-SENSITIVITY empties N1-R through its slope.
- V15–V17 survive. Each would raise KeyError (or give NaN) in `n2_outcome` or `gleak_table` on a campaign that does empty a point.
- Fix: shift all 40 sessions of one N1-R direction at +d_20 above TAU/4. Assert `st.at[("N1-R", d20)] == ["tau4-emptied"]`, the arm marked, N2 INDETERMINATE with tau4-emptied:N1-R@+d_20, and L at the other points.

**B3 NOTE — VD-SENSITIVITY pins the sensitivity tuple only against `outcomes(st_s)` of the same code.**
- So F2's change is unpinned, and V18 survives.
- Fix: assert the tuple literally as ["INDETERMINATE", "INDETERMINATE", "SHARED", "PASS", "PASS"], and that every N1-R `st_s.at` entry is `[]`.

**B4 NOTE — exactly-0 valence figure.** SENT-FILLED-N2-ZONE's "not at a mean of exactly 0" is tested on span_reward's figure only, so V24 survives. Fix: add a case with V = `_Z` at the norm-matched point.

**B5 NOTE — cause order within one read.**
- The order (incomplete, nonfinite, shadow) is pinned only on literal states; no reader campaign has two causes at one point, so V12 survives.
- Fix: omit N1-P's +d_20 cell and make run 100's shadow non-finite. Assert N2's causes end with "incomplete:N1-P@+d_20", "shadow:N1-P@+d_20".

**B6 NOTE — point_causes keys.** VERDICTS' `point_causes` is asserted at three keys only, so V14 (an "N1-V@0" entry) survives. Fix: assert the full key set.

**B7 NOTE — `_bt_expected_tallies` (1859).** Its docstring cites "the v4 review raw" for the derivation, and that raw does not exist at these bytes. Fix: cite the derivation where it actually stands.

#### Mutants

Of the 35 below, 8 are predicted to survive: V08, V12, V14, V15, V16, V17, V18 and V24.

```
@@ V01 | State.causes_at | the point-wise record honoured only on a complete arm, so an incomplete arm is "incomplete" everywhere | predicted: killed by N2-POINT-ELSEWHERE (also RD-INDET, RD-POINTWISE)
        if (arm, key) in self.at:
            return list(self.at[(arm, key)])
~~
        if (arm, key) in self.at and self.complete.get(arm):
            return list(self.at[(arm, key)])
```
```
@@ V02 | State.causes_at | a literal state's incomplete arm usable at every point | predicted: killed by N2-INDET-incomplete:N2-E (and :N1-V, :N1-R, :N1-P)
        return [] if self.complete.get(arm) else ["incomplete"]
~~
        return []
```
```
@@ V03 | State.named_at | a point named by its value, not its record label | predicted: killed by N2-INDET-incomplete:N1-V (also N2-POINT-CAUSES, GLEAK-POINTWISE)
        lab = F_LABEL[key] if key in F_LABEL else self.dmap.label_of(key)
~~
        lab = F_LABEL[key] if key in F_LABEL else f"{key:+.4f}"
```
```
@@ V04 | n2_reads | N1-P read at +1 (the pre-Q2 reading) instead of the norm-matched point | predicted: killed by N2-INDET-incomplete:N1-P (also N2-POINT-ELSEWHERE)
    return [("N2-E", f), ("N1-V", m), ("N1-R", m), ("N1-P", m)]
~~
    return [("N2-E", f), ("N1-V", m), ("N1-R", m), ("N1-P", 1.0)]
```
```
@@ V05 | n2_outcome | INDETERMINATE causes read at the beside f | predicted: killed by N2-INDET-incomplete:N2-E (and the other N2-INDET-incomplete ids)
    reads = n2_reads(st, f_dec)
~~
    reads = n2_reads(st, f_bes)
```
```
@@ V06 | n2_outcome | a guard's pause makes N2 INDETERMINATE again (n:140 as 977b78b read it) | predicted: killed by N2-GUARD-PAUSE
    causes = [f"pause:{a}" for a, _ in reads if st.paused.get(a)] + [c for a, k in reads for c in st.named_at(a, k)]
~~
    causes = [f"pause:{a}" for a in ("N2-E", "N2-S", "N2-C", "N1-V", "N1-R", "N1-P") if st.paused.get(a)] + [c for a, k in reads for c in st.named_at(a, k)]
```
```
@@ V07 | n2_outcome | pauses on N1-V/N1-R/N1-P ignored (the 2026-11-16 §1.6 rule) | predicted: killed by N2-INDET-pause:N1-V, N2-INDET-pause:N1-R, N2-INDET-pause:N1-P (also RD-PAUSE)
    causes = [f"pause:{a}" for a, _ in reads if st.paused.get(a)] + [c for a, k in reads for c in st.named_at(a, k)]
~~
    causes = [f"pause:{a}" for a, _ in reads if st.paused.get(a) and a == "N2-E"] + [c for a, k in reads for c in st.named_at(a, k)]
```
```
@@ V08 | n2_outcome | the beside judged per arm: an incompleteness elsewhere blanks the other f's figures | predicted: survives
    ok = {a: not st.causes_at(a, k) for a, k in n2_reads(st, f_bes)}
~~
    ok = {a: bool(st.complete.get(a)) for a, k in n2_reads(st, f_bes)}
```
```
@@ V09 | n2_outcome | the beside's ceiling computed without N1-P at its point | predicted: killed by N2-BESIDE-NOT-COMPUTED
    c_b = ceiling_cert(st, mb) if (ok["N1-R"] and ok["N1-P"]) else NOT_COMPUTED
~~
    c_b = ceiling_cert(st, mb) if ok["N1-R"] else NOT_COMPUTED
```
```
@@ V10 | n2_outcome | the beside certified against the decision point's ceiling | predicted: killed by RD-CAP-BINDS
        return NOT_COMPUTED if NOT_COMPUTED in (x, c_b) else above(x.mean, c_b)
~~
        return NOT_COMPUTED if NOT_COMPUTED in (x, c_b) else above(x.mean, ceil_m)
```
```
@@ V11 | build_state | a point "incomplete" only when every read there is missing | predicted: killed by RD-INDET (delta_m STOPs on rand_07's missing cell; the reader group fails)
            why = (["incomplete"] if any(r not in camp.present[a] for r in ids) else []) \
~~
            why = (["incomplete"] if all(r not in camp.present[a] for r in ids) else []) \
```
```
@@ V12 | build_state | the shadow cause listed before a point's own causes | predicted: survives
            st.at[(a, fkey.get(lab, lv.get(lab)))] = why + sh
~~
            st.at[(a, fkey.get(lab, lv.get(lab)))] = sh + why
```
```
@@ V13 | build_state | N1-V's own points not shadowed by a bad d = 0 read | predicted: killed by RD-SHADOW (delta_m STOPs; the reader group fails)
        sh = [] if shadows_ok(a) else ["shadow"]
~~
        sh = [] if (a == "N1-V" or shadows_ok(a)) else ["shadow"]
```
```
@@ V14 | build_state | N1-V's d = 0 shadows recorded as a point ("N1-V@0" in point_causes) | predicted: survives
            if a == "N1-V" and lab == "0":
~~
            if a == "N1-V" and lab == "0" and False:
```
```
@@ V15 | build_state (emptied_at) | a point the TAU/4 row empties not recorded: usable, with no statistic | predicted: survives
            st.at[(arm, key)] = ["tau4-emptied"]
~~
            pass
```
```
@@ V16 | build_state (emptied_at) | an emptied point leaves its arm complete (its slope then reads a missing vector) | predicted: survives
            st.at[(arm, key)] = ["tau4-emptied"]
            arm_emptied(arm)
~~
            st.at[(arm, key)] = ["tau4-emptied"]
```
```
@@ V17 | build_state (emptied_at) | an N1-R point emptied only when all 24 directions are (L then NaN) | predicted: survives
        if any(len(v) == 0 for v in vecs):
            st.at[(arm, key)] = ["tau4-emptied"]
~~
        if all(len(v) == 0 for v in vecs):
            st.at[(arm, key)] = ["tau4-emptied"]
```
```
@@ V18 | build_state (arm_emptied) | a slope with no common session marks every point, so the TAU/4 row's N2 is INDETERMINATE again | predicted: survives
    def arm_emptied(arm) -> None:
        st.complete[arm] = False
        st.unusable[arm] = "tau4-emptied"
~~
    def arm_emptied(arm) -> None:
        st.complete[arm] = False
        st.unusable[arm] = "tau4-emptied"
        for k_ in [k_ for k_ in st.at if k_[0] == arm and not st.at[k_]]:
            st.at[k_] = ["tau4-emptied"]
```
```
@@ V19 | build_state | N1-V's per-point estimates only on a complete arm | predicted: killed by RD-NONFINITE (n2_outcome KeyErrors on V at +d_20; the reader group fails)
        if usable_at("N1-V", pt):
~~
        if usable_at("N1-V", pt) and st.complete["N1-V"]:
```
```
@@ V20 | build_state | N1-R's L only on a complete arm | predicted: killed by RD-INDET
        if usable_at("N1-R", pt):
~~
        if usable_at("N1-R", pt) and st.complete["N1-R"]:
```
```
@@ V21 | build_state | N1-P's P only on a complete arm | predicted: killed by RD-POINTWISE (ceiling_cert STOPs on pw1; the reader group fails)
        if usable_at("N1-P", pt):
~~
        if usable_at("N1-P", pt) and st.complete["N1-P"]:
```
```
@@ V22 | gleak_table | N1-P required at every row, +1/2 included | predicted: killed by GLEAK-N1P-INCOMPLETE
        reads = [(arm, key), ("N1-R", pt)] + ([("N1-P", pt)] if pt in st.dmap.n1p_points() else [])
~~
        reads = [(arm, key), ("N1-R", pt), ("N1-P", pt)]
```
```
@@ V23 | gleak_table | N2 rows look their arm up by the point, not the f | predicted: killed by GLEAK-POINTWISE
            miss = needs(arm, f, pt)
~~
            miss = needs(arm, pt, pt)
```
```
@@ V24 | fill (N2) | the valence figure takes the zone's words at a mean of exactly 0 | predicted: survives
                        ZONE_V: ZONE_WORDS if v.mean < 0.0 else ""})
~~
                        ZONE_V: ZONE_WORDS if v.mean <= 0.0 else ""})
```
```
@@ V25 | fill (N2) | span_reward's figure takes the words at exactly 0 | predicted: killed by SENT-FILLED-N2-ZONE
                        "[xV]": _n(v.mean), "[CIV]": _ci(v), ZONE_E: ZONE_WORDS if e.mean < 0.0 else "",
~~
                        "[xV]": _n(v.mean), "[CIV]": _ci(v), ZONE_E: ZONE_WORDS if e.mean <= 0.0 else "",
```
```
@@ V26 | fill (N2) | the words only on a certified span_reward movement | predicted: killed by SENT-FILLED-N2-ZONE
                        "[xV]": _n(v.mean), "[CIV]": _ci(v), ZONE_E: ZONE_WORDS if e.mean < 0.0 else "",
~~
                        "[xV]": _n(v.mean), "[CIV]": _ci(v), ZONE_E: ZONE_WORDS if (e.mean < 0.0 and n2["certified_E"]) else "",
```
```
@@ V27 | fill (N2) | the valence figure and CI read at f = 0.20's point when the cap binds | predicted: killed by SENT-FILLED-N2-CAP
            e, v = st.E[n2["f"]], st.V[n2["point"]]
~~
            e, v = st.E[n2["f"]], st.V[st.dmap.norm_matched(F20)]
```
```
@@ V28 | fill (dose) | the merge note never printed | predicted: killed by SENT-FILLED-DOSE-ND (also SENT-FILLED-DOSE-FOURTH)
            sub.update({"[value]": value_text(st.dmap, d["point"]), MERGE_SLOT: merge_text(st.dmap, d["point"]),
~~
            sub.update({"[value]": value_text(st.dmap, d["point"]), MERGE_SLOT: "",
```
```
@@ V29 | merge_text | compared with the resolved d_eq (always equal), so no note on a merged map | predicted: killed by SENT-FILLED-DOSE-ND (also SENT-FILLED-DOSE-FOURTH)
    if point == dm.d_eq:
        return ""
~~
    if point == dm.resolved()["d_eq"]:
        return ""
```
```
@@ V30 | sentence_dose | the fourth form's readability by the §0.6 label, not G-READ-n | predicted: killed by TUP-T2 (also SENT-FILLED-DOSE-FOURTH)
            t, form = D_FOURTH["readable" if gr == "PASS" else "not readable"], FORM_FOURTH
~~
            t, form = D_FOURTH["readable" if lab == ANSWERED else "not readable"], FORM_FOURTH
```
```
@@ V31 | sentence_dose | the fourth form without its [merge] slot | predicted: killed by TUP-T2 (also SENT-FILLED-DOSE-FOURTH)
            t, form = D_FOURTH["readable" if gr == "PASS" else "not readable"], FORM_FOURTH
~~
            t, form = F4["readable" if gr == "PASS" else "not readable"], FORM_FOURTH
```
```
@@ V32 | sentence_dose | the fourth form only in the answered cell | predicted: killed by TUP-T2 (also SENT-FILLED-DOSE-FOURTH)
        if against:
~~
        if against and lab == ANSWERED:
```
```
@@ V33 | sentence_set_filled | the dose's against not passed: a certified movement against the zone printed "not certified" | predicted: killed by SENT-FILLED-DOSE-FOURTH
                        dose_against=bool(o["dose"].get("against")))
~~
                        dose_against=False)
```
```
@@ V34 | evaluations | the fourth input not enumerated (1,921 evaluations) | predicted: killed by TUP-COUNT (also TUP-T10, STR-GANL-ARTIFACT)
                for ag in ((False, True) if t[1] == "NOT-DETECTABLE" else (False,)):
~~
                for ag in (False,):
```
```
@@ V35 | state_figures | point causes keyed by value ("N1-P@-1.0") | predicted: killed by RD-POINTWISE (KeyError; the reader group fails)
    at = {f"{a}@{F_LABEL[k] if k in F_LABEL else st.dmap.label_of(k)}": v for (a, k), v in sorted(
~~
    at = {f"{a}@{k}": v for (a, k), v in sorted(
```

## 2. The dispositions (every finding)

### Production code

- **F1 MINOR (seat-level), the pause rule.** Kept as §5.2 writes it: N2 is "INDETERMINATE iff one of those reads is
  missing or non-finite, or a pause stands on one of them". A pause on N1-V, N1-R or N1-P therefore makes N2
  INDETERMINATE, and a pause on a guard alone leaves N2 evaluated. The reviewer is right that both halves depart from
  rulings of record:
  - the answers of 2026-11-16 §1.6: "A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable only in
    the case the block names, where those arms are nonetheless complete";
  - n:140: "INDETERMINATE iff an unadjudicated pause stands on N2's reads", whose "N2's reads" `977b78b` read as
    N2-E's, N2-S's and N2-C's.

  Code does not choose between rulings. PIN-n-33's text now quotes both and says the seat is asked which stands; the
  entry puts the question to the seat directly.
- **F2 NOTE, two "tau4-emptied" events.** PIN-n-36 now says that a slope with no common session in the TAU/4 row marks
  its arm and not its points, so that row decides N2 where `977b78b` had it INDETERMINATE. B3 pins the row's tuple.
- **F3 NOTE, N2's floor per arm.** Kept. N2's floor (N1-R at d_eq's and d_20's points) and the N2 arms' slopes, both
  reported only (ADDENDUM-n1 §7.5), stay on a complete arm; PIN-n-36 now names them among the per-arm statistics.
- **F4 NOTE, the fourth form's label.** No change. The form is the seat's, verbatim (§5.6), and its label is the
  record's field, set by §0.6 "as the others". Its text is the same in the answered cell and in the (G-READ-n PASS, N4
  not PASS) cell. For the seat, as a question on its own form, in the entry.
- **F5 NOTE, registers.**
  - OPEN-Q3 now says that §5.4 amends A.6 and that the A.6 cell takes the fourth form when the movement is certified
    against the zone.
  - OPEN-Q6 now carries §5.2's clause on the beside.
  - The comment above OPEN now names the answers of 2026-11-18.
  - OPEN-Q4 is kept: Code's PIN-n-35 is labelled as such in it.
- **F6 NOTE, docstrings.** `delta_m` now says "a usable point". `map_reach` now says the N1-R pattern leaves N2 evaluated
  wherever N2's point is not +1/2.
- **F7 NOTE, no beside on an INDETERMINATE N2.** Kept, as at `977b78b`. PIN-n-36 now registers the reading, strikable:
  §5.2's "not computed where its reads are missing" is read as applying to a decided N2's beside.
- **F8 NOTE, the double "against".** Kept. PIN-n-34 now quotes the resulting "… against [c], against the conditioned
  zone", so the seat sees it.

### The battery

- **B1 MINOR.** N2-POINT-ELSEWHERE now asserts, per case and shape, exactly which of the beside's figures are not
  computed. There are none, unless a read at the beside's own point is the one not usable: N2-E at the other f, or
  N1-P at +1 when the cap binds. RD-POINTWISE's first campaign asserts the beside fully computed.
- **B2 MINOR.** RD-POINTWISE gains two TAU/4 campaigns, each of which empties a point.
  - Every N1-P read at −1 (added before the review returned).
  - One random direction's 40 reads at +1. This marks N1-R's +1 and the arm, leaves N2 decided and L computed at
    the other points, and leaves G-LEAK-n's +1 row not computed (naming tau4-emptied:N1-R@+1).

  The reviewer's +d_20 cannot be emptied alone: the dose rule re-computes reads at 0 and ±1 only (the schema's
  `DOSE_RULE_LABELS`), so only shadows above TAU/4, at d = 0, could empty it, and every other point of the arm with it
  (PIN-n-16). A first form at +d_20 failed the fixed draft's first run, 215/217 (§4). N2 INDETERMINATE by a point
  emptied at its own reads stays the literal case of N2-POINT-CAUSES.
- **B3 NOTE.** VD-SENSITIVITY now asserts the sensitivity tuple literally, (INDETERMINATE, INDETERMINATE, SHARED, PASS,
  PASS), and that every N1-R point is usable in that row.
- **B4 NOTE.** SENT-FILLED-N2-ZONE gains the valence figure at exactly 0 (seven sentences).
- **B5 NOTE.** RD-POINTWISE gains a campaign with two causes at one point: N1-P's +d_20 cell missing and run 100's
  shadow non-finite. N2's causes are asserted in the reader's order.
- **B6 NOTE.** RD-POINTWISE asserts VERDICTS' point causes over every key (twenty), each [] but N1-P@-1.
- **B7 NOTE.** `_bt_expected_tallies` now cites this raw by its path; the derivation is §6.

### Added by Code after the freeze, before the review returned

- SENT-REFUSES: a fifth case, the dose sentence's own refusal of a movement against the zone on a dose that is not
  NOT-DETECTABLE (the frozen copy refused it in both places, but checked only the set's refusal).
- RD-POINTWISE: the TAU/4 row emptying N1-P at −1 (B2's gap, found while writing Code's mutants).

## 3. The mutants and their run

**The set.** M01–M35 are the reviewer's V01–V35, applied as written. M36–M54 are 19 of the 39 Code wrote while the
review ran, reproduced whole below the table. Code dropped the other 20, to keep the window near 90 minutes, as
overlapping the reviewer's:
- ten make one of the reviewer's own changes, as V02, V09, V16, V19, V20, V21, V25, V33, V34 and V35 do;
- eight mutate a line one of the reviewer's mutates, another way: the lines of V01, V06 and V07 (two), V11, V13, V29,
  V30 and V32. The one on V29's lines breaks the opposite way: a note at d_eq's own point, where V29 drops it from a
  merged map;
- two break, on another line, the same thing as V03 (the point a cause names: dropped, where V03 names it by value)
  and as V28 (the note: never printed).

All 39 as written are in Code's scratch. Each old text was checked to occur exactly once in the base before the run.

**The run.** The base was the fixed draft, frozen as a read-only copy at sha256
`285c61687c95417608e86432530fcab585b8dc5d062f7fe518d3c54c11f987db`.
Its battery passed 217/217, with every one of its 220 coverage ids reached. Each mutant ran once, one battery process at a time,
in batches of five. All 54 were killed.

In the table, "killed" lists the coverage ids the mutant's run left unreached (the battery prints the first six,
sorted), then each group that raised and its exception. A group that raises stops its later checks, so their ids
appear unreached too.

| Mutant | From | Function | What breaks | Predicted (by its author) | Result: the coverage ids the run left unreached (the battery prints the first six, sorted), and any group exception |
|---|---|---|---|---|---|
| M01 | V01 | `State.causes_at` | the point-wise record honoured only on a complete arm, so an incomplete arm is "incomplete" everywhere | killed by N2-POINT-ELSEWHERE (also RD-INDET, RD-POINTWISE) | killed: GLEAK-POINTWISE, N2-BESIDE-NOT-COMPUTED, N2-POINT-CAUSES, N2-POINT-ELSEWHERE, NUM-REACH-CLASS, RD-INDET |
| M02 | V02 | `State.causes_at` | a literal state's incomplete arm usable at every point | killed by N2-INDET-incomplete:N2-E (and :N1-V, :N1-R, :N1-P) | killed: GLEAK-N1-V-INCOMPLETE, GLEAK-N1P-INCOMPLETE, GLEAK-N2-C-INCOMPLETE, GLEAK-N2-E-INCOMPLETE, GLEAK-N2-S-INCOMPLETE, N2-BESIDE-FIELDS |
| M03 | V03 | `State.named_at` | a point named by its value, not its record label | killed by N2-INDET-incomplete:N1-V (also N2-POINT-CAUSES, GLEAK-POINTWISE) | killed: GLEAK-POINTWISE, N2-INDET-incomplete:N1-P, N2-INDET-incomplete:N1-R, N2-INDET-incomplete:N1-V, N2-POINT-CAUSES, RD-POINTWISE |
| M04 | V04 | `n2_reads` | N1-P read at +1 (the pre-Q2 reading) instead of the norm-matched point | killed by N2-INDET-incomplete:N1-P (also N2-POINT-ELSEWHERE) | killed: N2-BESIDE-NOT-COMPUTED, N2-INDET-incomplete:N1-P, N2-POINT-CAUSES, N2-POINT-ELSEWHERE, RD-POINTWISE, RD-SHADOW |
| M05 | V05 | `n2_outcome` | INDETERMINATE causes read at the beside f | killed by N2-INDET-incomplete:N2-E (and the other N2-INDET-incomplete ids) | killed: CNT-COUNTERS, N2-BESIDE-FIELDS, N2-BESIDE-NOT-COMPUTED, N2-CAP-F10, N2-F10-BESIDE, N2-GUARDS-DECIDE-NOTHING; KeyError raised in the outcomes group; KeyError raised in the reader path group |
| M06 | V06 | `n2_outcome` | a guard's pause makes N2 INDETERMINATE again (n:140 as 977b78b read it) | killed by N2-GUARD-PAUSE | killed: N2-GUARD-PAUSE |
| M07 | V07 | `n2_outcome` | pauses on N1-V/N1-R/N1-P ignored (the 2026-11-16 §1.6 rule) | killed by N2-INDET-pause:N1-V, N2-INDET-pause:N1-R, N2-INDET-pause:N1-P (also RD-PAUSE) | killed: N2-INDET-pause:N1-P, N2-INDET-pause:N1-R, N2-INDET-pause:N1-V, N2-POINT-CAUSES, RD-PAUSE |
| M08 | V08 | `n2_outcome` | the beside judged per arm: an incompleteness elsewhere blanks the other f's figures | survives | killed: N2-POINT-ELSEWHERE, RD-POINTWISE |
| M09 | V09 | `n2_outcome` | the beside's ceiling computed without N1-P at its point | killed by N2-BESIDE-NOT-COMPUTED | killed: N2-BESIDE-NOT-COMPUTED, N2-POINT-ELSEWHERE |
| M10 | V10 | `n2_outcome` | the beside certified against the decision point's ceiling | killed by RD-CAP-BINDS | killed: RD-CAP-BINDS |
| M11 | V11 | `build_state` | a point "incomplete" only when every read there is missing | killed by RD-INDET (delta_m STOPs on rand_07's missing cell; the reader group fails) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; AnlStop raised in the reader path group |
| M12 | V12 | `build_state` | the shadow cause listed before a point's own causes | survives | killed: RD-POINTWISE |
| M13 | V13 | `build_state` | N1-V's own points not shadowed by a bad d = 0 read | killed by RD-SHADOW (delta_m STOPs; the reader group fails) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; AnlStop raised in the reader path group |
| M14 | V14 | `build_state` | N1-V's d = 0 shadows recorded as a point ("N1-V@0" in point_causes) | survives | killed: RD-POINTWISE |
| M15 | V15 | `build_state (emptied_at)` | a point the TAU/4 row empties not recorded: usable, with no statistic | survives | killed: RD-POINTWISE |
| M16 | V16 | `build_state (emptied_at)` | an emptied point leaves its arm complete (its slope then reads a missing vector) | survives | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; KeyError raised in the reader path group |
| M17 | V17 | `build_state (emptied_at)` | an N1-R point emptied only when all 24 directions are (L then NaN) | survives | killed: RD-POINTWISE |
| M18 | V18 | `build_state (arm_emptied)` | a slope with no common session marks every point, so the TAU/4 row's N2 is INDETERMINATE again | survives | killed: RD-POINTWISE, VD-SENSITIVITY |
| M19 | V19 | `build_state` | N1-V's per-point estimates only on a complete arm | killed by RD-NONFINITE (n2_outcome KeyErrors on V at +d_20; the reader group fails) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; KeyError raised in the reader path group |
| M20 | V20 | `build_state` | N1-R's L only on a complete arm | killed by RD-INDET | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; KeyError raised in the reader path group |
| M21 | V21 | `build_state` | N1-P's P only on a complete arm | killed by RD-POINTWISE (ceiling_cert STOPs on pw1; the reader group fails) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; AnlStop raised in the reader path group; AnlStop raised in the verdicts group |
| M22 | V22 | `gleak_table` | N1-P required at every row, +1/2 included | killed by GLEAK-N1P-INCOMPLETE | killed: GLEAK-N1P-INCOMPLETE, GLEAK-POINTWISE |
| M23 | V23 | `gleak_table` | N2 rows look their arm up by the point, not the f | killed by GLEAK-POINTWISE | killed: GLEAK-POINTWISE |
| M24 | V24 | `fill (N2)` | the valence figure takes the zone's words at a mean of exactly 0 | survives | killed: SENT-FILLED-N2-ZONE |
| M25 | V25 | `fill (N2)` | span_reward's figure takes the words at exactly 0 | killed by SENT-FILLED-N2-ZONE | killed: RD-FILLED-FORMS, SENT-FILLED-N2-ZONE |
| M26 | V26 | `fill (N2)` | the words only on a certified span_reward movement | killed by SENT-FILLED-N2-ZONE | killed: SENT-FILLED-N2-ZONE |
| M27 | V27 | `fill (N2)` | the valence figure and CI read at f = 0.20's point when the cap binds | killed by SENT-FILLED-N2-CAP | killed: SENT-FILLED-N2-CAP |
| M28 | V28 | `fill (dose)` | the merge note never printed | killed by SENT-FILLED-DOSE-ND (also SENT-FILLED-DOSE-FOURTH) | killed: SENT-FILLED-DOSE-FOURTH, SENT-FILLED-DOSE-ND |
| M29 | V29 | `merge_text` | compared with the resolved d_eq (always equal), so no note on a merged map | killed by SENT-FILLED-DOSE-ND (also SENT-FILLED-DOSE-FOURTH) | killed: SENT-FILLED-DOSE-FOURTH, SENT-FILLED-DOSE-ND |
| M30 | V30 | `sentence_dose` | the fourth form's readability by the §0.6 label, not G-READ-n | killed by TUP-T2 (also SENT-FILLED-DOSE-FOURTH) | killed: SENT-FILLED-DOSE-FOURTH, TUP-T2 |
| M31 | V31 | `sentence_dose` | the fourth form without its [merge] slot | killed by TUP-T2 (also SENT-FILLED-DOSE-FOURTH) | killed: SENT-FILLED-DOSE-FOURTH, TUP-T2 |
| M32 | V32 | `sentence_dose` | the fourth form only in the answered cell | killed by TUP-T2 (also SENT-FILLED-DOSE-FOURTH) | killed: SENT-FILLED-DOSE-FOURTH, TUP-T10, TUP-T2 |
| M33 | V33 | `sentence_set_filled` | the dose's against not passed: a certified movement against the zone printed "not certified" | killed by SENT-FILLED-DOSE-FOURTH | killed: SENT-FILLED-DOSE-FOURTH |
| M34 | V34 | `evaluations` | the fourth input not enumerated (1,921 evaluations) | killed by TUP-COUNT (also TUP-T10, STR-GANL-ARTIFACT) | killed: STR-GANL-ARTIFACT, TUP-COUNT, TUP-T10 |
| M35 | V35 | `state_figures` | point causes keyed by value ("N1-P@-1.0") | killed by RD-POINTWISE (KeyError; the reader group fails) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; KeyError raised in the reader path group |
| M36 | Code | `n2_reads` | N1-P dropped from N2's reads | killed by N2-INDET-incomplete:N1-P, N2-INDET-pause:N1-P, N2-POINT-CAUSES | killed: BND-CERT-EQUAL, BND-CI-HI-ZERO, BND-CI-LO-ZERO, BND-I-BELOW, BND-I-EXACT, BND-IV-ZERO; KeyError raised in the outcomes group; KeyError raised in the sentences group; KeyError raised in the reachability group; KeyError raised in the reader path group; KeyError raised in the verdicts group |
| M37 | Code | `State.named_at` | N2's f named by its [f] text, not its record label | killed by N2-INDET-incomplete:N2-E, N2-POINT-CAUSES | killed: GLEAK-POINTWISE, N2-INDET-incomplete:N2-E, N2-POINT-CAUSES, RD-POINTWISE, RD-SHADOW |
| M38 | Code | `n2_outcome` | the beside's span_reward figure computed wherever an estimate exists | killed by N2-BESIDE-NOT-COMPUTED | killed: N2-BESIDE-NOT-COMPUTED, N2-POINT-ELSEWHERE |
| M39 | Code | `n2_outcome` | the beside's N1-V figure always computed | killed by N2-BESIDE-NOT-COMPUTED | killed: N2-BESIDE-NOT-COMPUTED |
| M40 | Code | `n2_outcome` | a certification beside read against a ceiling not computed | killed by N2-BESIDE-NOT-COMPUTED (a group raise) | killed: N2-BESIDE-FIELDS, N2-BESIDE-NOT-COMPUTED, N2-CAP-F10, N2-F10-BESIDE, N2-GUARDS-DECIDE-NOTHING, N2-MATCH-RATIO; ValueError raised in the outcomes group |
| M41 | Code | `n2_outcome` | each guard reported with N2-S's pause | killed by N2-GUARD-PAUSE | killed: N2-GUARD-PAUSE |
| M42 | Code | `build_state` | a non-finite read no cause of its point | killed by RD-NONFINITE, RD-POINTWISE (a group raise) | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; AnlStop raised in the reader path group |
| M43 | Code | `build_state` | N2's E, S, C computed on a complete arm only | killed by RD-POINTWISE | killed: CNT-COUNTERS, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES, RD-GREAD, RD-GREAD-MIXED; KeyError raised in the reader path group |
| M44 | Code | `fill` | the valence figure's words follow span_reward's sign | killed by SENT-FILLED-N2-ZONE | killed: SENT-FILLED-N2-ZONE |
| M45 | Code | `fill` | the valence figure printed with span_reward's CI | killed by SENT-FILLED-N2-CAP, SENT-FILLED-N2-ZONE | killed: RD-FILLED-FIGURES, RD-FILLED-FORMS, SENT-FILLED-N2-CAP, SENT-FILLED-N2-ZONE |
| M46 | Code | `sentence_dose` | the dose sentence's own refusal removed | killed by SENT-REFUSES | killed: SENT-REFUSES |
| M47 | Code | `map_reach` | the point-by-point patterns dropped | killed by REACH-SHAPE-a | killed: NUM-REACH-CLASS, REACH-SHAPE-a, REACH-SHAPE-b, REACH-SHAPE-c, REACH-SHAPE-d |
| M48 | Code | `gleak_table` | N1-P not read for a row's certification | killed by GLEAK-POINTWISE, GLEAK-N1P-INCOMPLETE | killed: CNT-COUNTERS, GLEAK-N1P-INCOMPLETE, GLEAK-POINTWISE, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES; KeyError raised in the reader path group |
| M49 | Code | `gleak_table` | rows read per arm (977b78b's) | killed by GLEAK-POINTWISE | killed: GLEAK-POINTWISE, RD-POINTWISE |
| M50 | Code | `n2_outcome` | incompleteness read per arm again | killed by N2-POINT-ELSEWHERE | killed: N2-BESIDE-NOT-COMPUTED, N2-INDET-incomplete:N1-P, N2-INDET-incomplete:N1-R, N2-INDET-incomplete:N1-V, N2-INDET-incomplete:N2-E, N2-POINT-CAUSES |
| M51 | Code | `n2_outcome` | the beside judged by the decision f's reads | killed by N2-BESIDE-NOT-COMPUTED | killed: CNT-COUNTERS, N2-BESIDE-NOT-COMPUTED, N2-POINT-ELSEWHERE, RD-ASYM, RD-CAP-BINDS, RD-CAP-SLOPES; KeyError raised in the reader path group |
| M52 | Code | `MOVE_NC` | the merge slot before the CI | killed by SENT-ADDENDUM, SENT-FILLED-DOSE-ND | killed: SENT-ADDENDUM, SENT-FILLED-DOSE-ND, TUP-T2, TUP-T8 |
| M53 | Code | `C_N2` | SPECIFIC's span_reward words before 'against [c]' | killed by SENT-CODE-FORMS, SENT-RULING, SENT-FILLED-N2-ZONE | killed: SENT-CODE-FORMS, SENT-FILLED-N2-ZONE, SENT-RULING |
| M54 | Code | `DoseMap.label_of` | a kept +d_20 or +d_eq point not found | killed by N2-INDET-incomplete:N1-V (a group raise) | killed: BND-CERT-EQUAL, BND-CI-HI-ZERO, BND-CI-LO-ZERO, BND-I-BELOW, BND-I-EXACT, BND-IV-ZERO; ValueError raised in the outcomes group; ValueError raised in the tables group; ValueError raised in the sentences group; ValueError raised in the reachability group; ValueError raised in the reader path group; ValueError raised in the verdicts group |

**The fifteen runs with a group exception.** Each raise stopped its group. Checks that failed besides the raise, the
coverage check and the count check are named where there were any.
- **M05:** with N2's causes read at the other f, the outcomes group raised a KeyError ('causes': an N2 decided where
  a check expected an INDETERMINATE one). The reader path group raised a KeyError (0.625: a figure at N2's own point,
  which the reader had not computed). Five checks had failed before the first raise, and RD-SHADOW before the second.
- **M11, M13 and M42:** the reader path group raised the AnlStop of `delta_m`, whose guard a mutant had moved:
  - M11: a point counted incomplete only when every read there is missing, met at N1-R's rand_07 cell at +1/2;
  - M13: N1-V's points not shadowed, met at run 100's non-finite shadow;
  - M42: a non-finite read no cause of its point, met at N1-V's +1 read of run 17.
- **M16, M19, M20 and M43:** the reader path group raised a KeyError:
  - M16: ('rand_00', '+1'), N1-R left complete with a point emptied, so its floor read a missing vector;
  - M19 and M20: 0.625, N1-V's V and N1-R's L computed on a complete arm only, so N2 read a point never computed;
  - M43: 'f=0.20', N2-E's E likewise.
- **M21:** the reader path and verdicts groups raised the AnlStop of a missing P(d) at 0.625, N2's point, with N1-P's
  P computed on a complete arm only.
- **M35:** the reader path group raised a KeyError ('N1-P@-1'), the point causes keyed by value.
- **M36:** with N1-P dropped from N2's reads, the outcomes, sentences, reachability, reader path and verdicts groups
  raised a KeyError ('N1-P') at the beside's lookup. Reachability's no-raise check and its four shapes failed before
  that group's raise, and the pinned-map check failed.
- **M40:** the outcomes group raised a ValueError, a certification read against a ceiling "not computed".
  Reachability's no-raise check failed as well.
- **M48:** the reader path group raised a KeyError ('why'): with N1-P not read for a row, a row that should not have
  been computed was. GLEAK-N1P-INCOMPLETE and GLEAK-POINTWISE had failed before.
- **M51:** the reader path group raised a KeyError ('f=0.10'), the beside judged by the decision f's reads.
  N2-POINT-ELSEWHERE and N2-BESIDE-NOT-COMPUTED had failed before.
- **M54:** with a kept +d_20 or +d_eq point not found by `label_of`, six groups raised its ValueError: outcomes,
  tables, sentences, reachability, reader path and verdicts. Before reachability's raise, its no-raise check, shapes
  (a) and (b) and REACH-FOURTH had failed: where N2's point is merged into +1, as on shapes (c) and (d), its label
  is found.

**The eight the reviewer predicted would survive the frozen copy,** each killed by a check the dispositions added or
extended:
- M08 by N2-POINT-ELSEWHERE and RD-POINTWISE (B1);
- M12 by RD-POINTWISE, the two causes at one point (B5);
- M14 by RD-POINTWISE, every key of the point causes (B6);
- M15 and M17 by RD-POINTWISE, the TAU/4 campaigns (B2);
- M16 through the reader path's KeyError on the second of them (B2);
- M18 by RD-POINTWISE and VD-SENSITIVITY (B2, B3);
- M24 by SENT-FILLED-N2-ZONE (B4).

**Code's mutants, whole** (M36–M54; the old text, then the new, each applied to the base exactly once):

```
@@ M36 | n2_reads | N1-P dropped from N2's reads | predicted: killed by N2-INDET-incomplete:N1-P, N2-INDET-pause:N1-P, N2-POINT-CAUSES
    return [("N2-E", f), ("N1-V", m), ("N1-R", m), ("N1-P", m)]
~~
    return [("N2-E", f), ("N1-V", m), ("N1-R", m)]
```
```
@@ M37 | State.named_at | N2's f named by its [f] text, not its record label | predicted: killed by N2-INDET-incomplete:N2-E, N2-POINT-CAUSES
        lab = F_LABEL[key] if key in F_LABEL else self.dmap.label_of(key)
~~
        lab = F_TEXT[key] if key in F_TEXT else self.dmap.label_of(key)
```
```
@@ M38 | n2_outcome | the beside's span_reward figure computed wherever an estimate exists | predicted: killed by N2-BESIDE-NOT-COMPUTED
    e_b = st.E[f_bes] if ok["N2-E"] else NOT_COMPUTED
~~
    e_b = st.E[f_bes] if f_bes in st.E else NOT_COMPUTED
```
```
@@ M39 | n2_outcome | the beside's N1-V figure always computed | predicted: killed by N2-BESIDE-NOT-COMPUTED
    v_b = st.V[mb] if ok["N1-V"] else NOT_COMPUTED
~~
    v_b = st.V[mb]
```
```
@@ M40 | n2_outcome | a certification beside read against a ceiling not computed | predicted: killed by N2-BESIDE-NOT-COMPUTED (a group raise)
        return NOT_COMPUTED if NOT_COMPUTED in (x, c_b) else above(x.mean, c_b)
~~
        return NOT_COMPUTED if x == NOT_COMPUTED else above(x.mean, c_b)
```
```
@@ M41 | n2_outcome | each guard reported with N2-S's pause | predicted: killed by N2-GUARD-PAUSE
                         | {"paused": bool(st.paused.get(a))}
~~
                         | {"paused": bool(st.paused.get("N2-S"))}
```
```
@@ M42 | build_state | a non-finite read no cause of its point | predicted: killed by RD-NONFINITE, RD-POINTWISE (a group raise)
                + (["nonfinite"] if any(r in camp.present[a] and not camp.records[r]["finite"] for r in ids) else [])
~~
                + []
```
```
@@ M43 | build_state | N2's E, S, C computed on a complete arm only | predicted: killed by RD-POINTWISE
            if usable_at(arm, f):
~~
            if usable_at(arm, f) and st.complete[arm]:
```
```
@@ M44 | fill | the valence figure's words follow span_reward's sign | predicted: killed by SENT-FILLED-N2-ZONE
                        ZONE_V: ZONE_WORDS if v.mean < 0.0 else ""})
~~
                        ZONE_V: ZONE_WORDS if e.mean < 0.0 else ""})
```
```
@@ M45 | fill | the valence figure printed with span_reward's CI | predicted: killed by SENT-FILLED-N2-CAP, SENT-FILLED-N2-ZONE
                        "[xV]": _n(v.mean), "[CIV]": _ci(v), ZONE_E: ZONE_WORDS if e.mean < 0.0 else "",
~~
                        "[xV]": _n(v.mean), "[CIV]": _ci(e), ZONE_E: ZONE_WORDS if e.mean < 0.0 else "",
```
```
@@ M46 | sentence_dose | the dose sentence's own refusal removed | predicted: killed by SENT-REFUSES
    if against and state != "NOT-DETECTABLE":
        raise ValueError(f"a movement against the conditioned zone at d_eq is NOT-DETECTABLE, not {state!r}")
~~
    pass
```
```
@@ M47 | map_reach | the point-by-point patterns dropped | predicted: killed by REACH-SHAPE-a
    pats = list(_PATTERNS) + [pointwise(dmap, {("N1-P", -1.0): ["incomplete"]}),
                              pointwise(dmap, {("N1-R", 0.5): ["incomplete"]})]
~~
    pats = list(_PATTERNS)
```
```
@@ M48 | gleak_table | N1-P not read for a row's certification | predicted: killed by GLEAK-POINTWISE, GLEAK-N1P-INCOMPLETE
        reads = [(arm, key), ("N1-R", pt)] + ([("N1-P", pt)] if pt in st.dmap.n1p_points() else [])
~~
        reads = [(arm, key), ("N1-R", pt)]
```
```
@@ M49 | gleak_table | rows read per arm (977b78b's) | predicted: killed by GLEAK-POINTWISE
        return [c for a, k in reads for c in st.named_at(a, k)]
~~
        return [f"incomplete:{a}" for a, k in reads if not st.complete.get(a)]
```
```
@@ M50 | n2_outcome | incompleteness read per arm again | predicted: killed by N2-POINT-ELSEWHERE
    causes = [f"pause:{a}" for a, _ in reads if st.paused.get(a)] + [c for a, k in reads for c in st.named_at(a, k)]
~~
    causes = [f"pause:{a}" for a, _ in reads if st.paused.get(a)] + [c for c in _causes(st, [a for a, _ in reads]) if not c.startswith("pause:")]
```
```
@@ M51 | n2_outcome | the beside judged by the decision f's reads | predicted: killed by N2-BESIDE-NOT-COMPUTED
    ok = {a: not st.causes_at(a, k) for a, k in n2_reads(st, f_bes)}
~~
    ok = {a: not st.causes_at(a, k) for a, k in n2_reads(st, f_dec)}
```
```
@@ M52 | MOVE_NC | the merge slot before the CI | predicted: killed by SENT-ADDENDUM, SENT-FILLED-DOSE-ND
MOVE_NC = MOVE_NOT_CERTIFIED.replace(DEQ_FIGURE, DEQ_FIGURE + MERGE_SLOT)
~~
MOVE_NC = MOVE_NOT_CERTIFIED.replace("[CI]", MERGE_SLOT + "[CI]")
```
```
@@ M53 | C_N2 | SPECIFIC's span_reward words before 'against [c]' | predicted: killed by SENT-CODE-FORMS, SENT-RULING, SENT-FILLED-N2-ZONE
                               "apparatus beyond the leak ceiling (Δm = [xE] nats [CIE] against [c][zoneE]) while the "
~~
                               "apparatus beyond the leak ceiling (Δm = [xE] nats [CIE][zoneE] against [c]) while the "
```
```
@@ M54 | DoseMap.label_of | a kept +d_20 or +d_eq point not found | predicted: killed by N2-INDET-incomplete:N1-V (a group raise)
            if not p["label"].startswith("f") and p["value"] == value:
~~
            if not p["label"].startswith("f") and p["value"] == value and not p["label"].startswith("+d"):
```

## 4. The battery runs

All ran in battery windows the coordinating session granted: one process at a time, `nice -n 19`, `-I`, temp folders
outside the repository, in the foreground. Nothing ran on a model or on the box. The runs named here ran on the
working copy of the draft; each frozen copy was made from it, unchanged, after its run.

- **The draft's window, two runs.**
  - The first: 214/217. The forms' digest had moved, as §5.1 says it does with §5.3, §5.4 and §5.6, and one reader
    expectation (RD-GREAD-MIXED) still named the dose sentence's old form string. The coverage check failed on those
    two.
  - Between the runs, the digest pin was set from that run's printed value and the expectation was updated.
  - The second: 217/217. Those bytes were frozen for the review.
- **The mutant window.**
  - Two runs of the fixed draft. The first: 215/217. B2's first form had tried to empty N1-R's +d_20 point alone in
    the TAU/4 row, which the dose rule makes impossible (§2), so RD-POINTWISE failed, and the coverage check with it.
    The test moved to +1; the second run: 217/217. Those bytes were frozen as the mutant base.
  - Then the 54 mutants, in batches of five (M51–M54 the last four), each batch a tool call that ran its mutants one
    after another.
- **The run of record** is the entry's, from `scripts/n_analyze.py` on the committed bytes.

Q-F3's campaign ran on the laptop beside these windows, as the coordinating session's windows allow; by its grants, no
other battery window was open during any of them.

## 5. The committed bytes against the mutation-tested base

The committed `scripts/n_analyze.py` differs from the mutant base (`285c6168…87db`) in twelve hunks.

- **The repository line.** The base, a scratch file, read the repository at its absolute path; the committed file
  reads it from its own location, as the committed analyzer always has:

  ```
  REPO = Path(__file__).resolve().parents[1]                     # scripts/n_analyze.py -> the repository
  ```
- **Nine texts, from the values-check's two passes:**
  - the comment above the seat's forms: the NOT-DETECTABLE forms print the note, and DETECTABLE keeps VALUE_MERGED;
  - the comment above `C_N2`: the words close the figure's parenthetical, or the sentence where the figure has none;
  - the comment above the oracle's copies: a slip fails T2, for the fourth form and the figure, or SENT-RULING, for
    the note's words;
  - SENT-CODE-FORMS's description, which now names the seat's forms of 2026-11-18;
  - PIN-n-29, which marks N1-P at −1 and N1-R at +1/2 as the seat's examples, with Code's note that +1/2 is N2's own
    point where d_20 folds into it, or d_eq does when the cap binds (pass 2 completed the note);
  - PIN-n-34, which says SHARED's span_reward figure had its CI already, and that the doubled "against" is
    SPECIFIC's and SHARED's;
  - `build_state`'s docstring (two hunks): an arm is complete only if every point is, and a slope with no common
    session in the TAU/4 row marks its arm alone;
  - `_bt_expected_tallies`'s docstring, re-wrapped to the file's width (pass 2);
  - the comment above RD-POINTWISE's +1 campaign, which now says no other point can be emptied alone (pass 2).
- **One battery comparand.** SENT-RULING's note check compares the module's note with the oracle's copy (`_ORC_NOTE`)
  instead of a third literal, so that copy is read by a check. The values-check had found it read for its figure
  alone.

No outcome, sentence or form changes. The forms' digest is the same, since none of the nine texts is a form. The run
of record covers the committed bytes, the changed comparand included.

## 6. The tallies, by hand (TUP-T10; `_bt_expected_tallies`)

The tuple pass evaluates every (tuple, gr1, gre, n4_no_read, dose_against). Its parts:
- the 384 tuples: N1 (4) × dose (3) × N2 (4) × N4 (4) × G-READ-n at d_eq (2);
- each tuple under 4 G-READ inputs: gr1 and gre, each PASS or FAIL;
- doubled where N4 is INDETERMINATE (96 tuples: no read obtained or terminal);
- doubled where dose is NOT-DETECTABLE (128 tuples: the movement at d_eq certified against the conditioned zone or
  not, PIN-n-35).

Counting the 384 tuples in four groups:

| N4 INDETERMINATE | dose NOT-DETECTABLE | Tuples | Evaluations each | Evaluations |
|---|---|---|---|---|
| yes | yes | 32 | 4 × 2 × 2 = 16 | 512 |
| yes | no | 64 | 4 × 2 = 8 | 512 |
| no | yes | 96 | 4 × 2 = 8 | 768 |
| no | no | 192 | 4 | 768 |

That is 2,560 in all, and 2,561 with NOT-RUN. At `977b78b` there were 1,921: the 640 added repeat the 640
NOT-DETECTABLE evaluations (128 × 4 + 32 × 4) with the fourth input set.

- **7.1, N1's sentence,** reads no dose input, and each N1 state takes a quarter of the 2,560: 640 each.
  - NOT-REPLICATED is answered iff N4 PASS and gr1 PASS. N1 NOT-REPLICATED with N4 PASS is 24 tuples (dose 3 × N2 4 ×
    G-READ-n 2), 8 of them with dose NOT-DETECTABLE: 16 × 4 + 8 × 4 × 2 = 128 evaluations.
  - gr1 is PASS in half of them: 64 answered, 576 concluded, not answered.
- **7.2, the dose sentence.**
  - DETECTABLE and INDETERMINATE are never doubled by the fourth input: 128 × 4 + 32 × 4 = 640 each.
  - NOT-DETECTABLE takes 1,280: 640 with no movement against the zone and 640 in the fourth form.
  - The three forms, among the 640:
    - answered (N4 PASS, G-READ-n PASS): N1 4 × N2 4 = 16 tuples × 4 = 64;
    - not readable (G-READ-n FAIL): 64 tuples × 4, + the 16 with N4 INDETERMINATE × 4 = 320;
    - the cell of A.6 (G-READ-n PASS, N4 not PASS): 48 × 4 + 16 × 4 = 256.
  - The fourth form, among the other 640: 64 answered (N4 PASS, G-READ-n PASS, as above) and 576 concluded, not
    answered.
- **7.3, N2's line,** reads no dose input, and each N2 state takes 640.
  - SPECIFIC and NULL are answered iff N4 PASS and gre PASS: 24 tuples each with N4 PASS, 8 of them doubled, giving 128
    evaluations, half with gre PASS.
  - So 64 answered and 576 concluded, not answered, for each.
- **N4's line:** 512 for each of PASS, REVERSE, DEAD, the terminal INDETERMINATE and no read obtained. For example,
  PASS: 64 tuples without a NOT-DETECTABLE dose × 4, + 32 with one × 4 × 2 = 512.
- **NOT-RUN:** 1 in each slot.

Every count is a third more than at `977b78b`, except NOT-RUN's and those of 7.2's DETECTABLE, INDETERMINATE and three
NOT-DETECTABLE forms, which are unchanged, and the fourth form's, which are new.
