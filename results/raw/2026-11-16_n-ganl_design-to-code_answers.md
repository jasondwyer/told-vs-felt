# G-ANL-n: the nine questions answered — slopes through the origin, N1-P read at the program's doses, "answered" by §0.6 everywhere, the sentence forms adopted with amendments; Code's readings and PINs accepted (design → Code)

*Design seat, PI date 2026-11-16 (second sitting). On the n-analyzer session's block `results/raw/2026-11-16_n-ganl_code-to-design_prebuild.md` (`8e3bf91`), read in full with its entry; the BUILD entry (`5c0ae6b`), the pin move (`2822721`) and the `verdicts` command's entry (`bedc198`) for the readings they register (PIN-n-20 to PIN-n-26, PIN-n-12 and PIN-n-16 amended); PROPOSAL-n v0.2 at root (§0.4, §0.6, §2.3–§2.4, §3, §4, §5, §7). The [C] figures are taken as the block's values-check left them. n-build's two blocks are answered in `results/raw/2026-11-16_n-build_design-to-code_answers.md`, placed with this raw; its rulings on the merge (Q3 there), the capture band (Q5 there) and the committed ids bear on this block and are cited where they do. The design changes are gathered in **ADDENDUM-n1 v0.1** at root. `n:N` = PROPOSAL-n v0.2's line N, as the block anchors it. **Placed untracked over the bridge; Code commits by path on the PI's routing; the n-analyzer session and the coordinating session add their close lines.** Calendar dates only; the commit hash is the record.*

## 0. The short form

| Q | ruling | moves the analyzer? |
|---|---|---|
| 1 | **(b)** OLS through the origin over the nonzero points; the with-intercept slope reported beside, descriptive | yes |
| 2 | **(c)** N1-P read at +d_20 and +d_eq as well (+320 reads at most, positive doses only); P(d) then exists at every certified point | the read plan (n-build's schema); the ceiling rule's form unchanged |
| 3 | **(a)** §0.6 governs dose, N1 and N2; Code's A.6 for the (G-READ-n PASS, N4 not PASS) cell | yes |
| 4 | confirmed: inputs, not coordinates; 385 tuples | no |
| 5 | confirmed: total functions; reachability reported per merge shape; no refusal of impossible tuples | no |
| 6 | **(a)**, with N1-P's own points in dose's and N2's causes | yes (small) |
| 7 | when the cap binds, N2 is decided at f = 0.10 against N1-V at d_eq; f = 0.20 beside against d = 1 with the ratio | yes |
| 8 | Appendix A adopted with the amendments of §1.8 (the dose sentences' figures; the sign; the labels) | yes |
| 9 | **(a)**, through the origin | yes (small) |

The block's §3 readings and every PIN are accepted (§2). The changes land before the canonical run, which still waits for G-CAL-n's dose map (§3). The routing block is §4.

## 1. The questions

**1.1 Q1 — (b).** BK's own pre-registration says the paired difference "is identically zero at dose 0 by construction". A line fitted to Δm(d) with a free intercept estimates a parameter the construction fixes at 0 and weighs an exact zero as if it were an observation; a fit through the origin is the model BK's words state. The two coincide on BK's symmetric grid (0.9164 either way [C]) and differ on ours, so the choice has to be made, and it is made by the construction, not by which call BK's unavailable code used. The floor is refit the same way (C12), so conjunct (ii) compares like with like. The with-intercept slope is reported beside, labelled descriptive, for anyone comparing with BK's figure. ADDENDUM-n1 §7.1.

**1.2 Q2 — (c).** Dose's DETECTABLE at d_eq is the sentence "dose alone does not account for the program's null", and it is certified against a leak ceiling that, without N1-P at d_eq, would hold no same-pole term there. (a) certifies against the random directions alone; (b) borrows P(+1), which is a different dose. (c) measures it: N1-P reads +1, +d_20, +d_eq and −1 under the merge, so at most 320 more reads, positive doses only; §0.4's negative counts are unchanged and the forward total becomes about 10,800. P(d) then exists at every point where a certification is made, and n:122's rule needs no "where N1-P is not read" clause. The read plan and the schema's `read_plan` move (n-build's follow-up schema commit). ADDENDUM-n1 §5.2.

**1.3 Q3 — (a).** §0.6 is rule 5(b)'s application and names both conditions; §5's dose clause abbreviated it and dropped (i), the seat's omission. *Answered* means N4 PASS and G-READ-n PASS for the axis and dose: N1 at d = +1, dose at d_eq, N2 for `span_reward` at its decision f (Q7). N1's NOT-REPLICATED and N2's NULL carry the label the same way. The (G-READ-n PASS, N4 not PASS) cell takes Code's A.6; its 256 evaluations [C] are the cell's. ADDENDUM-n1 §7.2.

**1.4 Q4 — confirmed.** G-READ-n at +1, G-READ-n for `span_reward` at the decision f, and N4's no-read INDETERMINATE form are inputs that change a sentence, not coordinates; m:278's precedent holds; the battery evaluates every tuple under every value (1,921 evaluations) and the count stays at 385.

**1.5 Q5 — confirmed.** The sentence functions are total over the 385, as n:115 asks; the battery reports which tuples can occur on each merge shape, and on the pinned map once G-CAL-n pins d_eq; the analyzer refuses no tuple on reachability grounds. A refusal would add a failure mode and remove nothing: an unreachable tuple is never presented.

**1.6 Q6 — (a), amended for N1-P's points.** The causes Code carries are the ones §5's words imply and did not list: N1 is INDETERMINATE when N1-V is incomplete; dose when N1 is, or when N1-V's, N1-R's or N1-P's reads at d_eq are incomplete (the d_20 figure beside is then reported as not computed); N2 when N2-E, N1-V, N1-R or N1-P at the norm-matched point is incomplete; N4 with a pause standing on its reads, as "no read obtained". Under Q2 (c) the clause "N1-P where d_20 sits at +1" becomes "N1-P at the norm-matched point". A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable only in the case the block names, where those arms are nonetheless complete; the incompleteness causes decide it otherwise. (b) would judge arms on partial read sets, which n:134 forbids. ADDENDUM-n1 §7.4.

**1.7 Q7 — decided now, conditionally.** N2's comparison is a norm-matched one. If 2·d_eq > 1, d_20 is 1 by the cap and N2-E at f = 0.20 has no matched N1-V point; the comparison at 0.20 would be between unequal norms, a ratio of 2·d_eq. The ruling: when the cap binds, N2 is decided at f = 0.10 against N1-V at d_eq, where the norms are equal exactly, and f = 0.20 is reported beside against N1-V at d = 1 with the ratio printed; otherwise as written. No read-set change: N1-V and N1-R at 2·d_eq > 1 would be a dose BK never applied. The f slot enters A.7's sentences. ADDENDUM-n1 §5.3.

**1.8 Q8 — Appendix A adopted, with these amendments** (the rest verbatim as Code wrote it, including A.6 and the three forms OPEN-Q8 gained since the block):
- **The dose sentences carry the figures.** In all three NOT-DETECTABLE forms (answered; not answered; A.6), "the margin does not move beyond the leak ceiling" becomes *the margin's movement is not certified (Δm(d_eq) = [x] nats [CI] against a leak ceiling of [c])*, which is true in both sub-cases (a CI including 0; a mean below the ceiling).
- **The sign.** DETECTABLE requires the mean at d_eq > 0; PARTIAL requires the mean at +1 > 0. A certified movement against the conditioned zone is NOT-DETECTABLE, or NOT-REPLICATED, and the sentence's clause reads *the margin moves against the conditioned zone beyond the leak ceiling (Δm = [x] nats [CI], ceiling [c])*. ADDENDUM-n1 §7.3.
- **The labels.** A.2's and A.7's "[label]" is *answered* or *concluded, not answered*, by §0.6 as §1.3 rules.
- **A.7's "at f = 0.20"** becomes *at f = [f]*, filled from Q7.
- A G-READ-n cell not computed takes the not-readable sentence: accepted.

**1.9 Q9 — (a), through the origin.** N2's slope is reported over its two points on BK's scale, d_eq and 2·d_eq, through the origin (Q1), its floor refit on the random reads at d_eq's and d_20's kept points. When the cap binds, the floor's second point is d = 1 against N2-E's 2·d_eq, and the mismatch is printed beside the figure. No outcome reads it. ADDENDUM-n1 §7.5.

## 2. Code's readings and PINs — accepted

- **The block's §3, all nine:** the signed mean slope above the floor for (ii); "excluding 0" as wholly on one side, an endpoint at 0 not excluding; an absent or not-computed G-READ-n cell not PASS; the bootstrap's form (one resample matrix per arm from `n-boot|{arm}` under m:159's function, 4,000 rows in session order; percentile intervals with linear interpolation, 2.5/97.5 and N4's 1/99), to be stated in the lock; the merge rule, as n-build's Q3 is ruled; conjunct (iv) evaluated under A1; the TAU/4 row's handling; the label-mass counter's bar at .20; secondary (d) as Pearson's r.
- **PIN-n-20, -21, -22, and PIN-n-12 amended** (`5c0ae6b`): accepted. The floor of n ≥ 20 for (a), (c) and (d) is rule 28(a)'s.
- **PIN-n-23 to PIN-n-26, and PIN-n-16 amended** (`bedc198`): accepted. PIN-n-26's two lines are the lock's form from v0.1 on. PIN-n-24's F2 reading — complete means every planned read produced, finite or not, so a non-finite read makes its arm INDETERMINATE and never the unit NOT-RUN — is the reading the seat would have given.
- **OPEN-Q8's three added forms** (the route slot's two fills; VALUE_MERGED): adopted with Appendix A.
- The CV form the artifact records becomes `kfold10` with its seed (n-build's raw, §2.5); the analyzer reads the status and the band median as before.

## 3. What moves, and the order

1. `scripts/n_analyze.py`: the slope through the origin with the with-intercept figure beside (Q1, Q9); N1-P's points in the ceiling and in the causes (Q2, Q6); *answered* by §0.6 with A.6 (Q3); the sign rules (Q8); the decision f when the cap binds and the f slot (Q7); the amended sentence forms (Q8). The battery's oracle keeps §5's verbatim cells; the amended forms are pinned by digest as Code's are now, with this raw and ADDENDUM-n1 as their source.
2. The reader follows n-build's follow-up schema commit (the read plan with N1-P's four points; the capture band and `kfold10` in the G-READ-n form); the pin moves as before.
3. One blind review round on the changes and their mutants; the battery; the values-check; the commit, with close lines on `8e3bf91`'s entry citing this raw.
4. G-ANL-n's canonical run, as before, after G-CAL-n pins d_eq; its artifact's sha256 into LOCK-n v0.1, drafted to the seat.

## 4. Routing block for the PI (defaults in brackets; your words are the record)

**File placed untracked on the laptop:** this raw under `results/raw/` — sha256 and bytes in the paste block.

**N. n-analyzer**
1. Q1 (b), Q9 (a) through the origin, the with-intercept slope beside [as ruled].
2. Q2 (c): N1-P at +1, +d_20, +d_eq, −1 under the merge; the plan moves in n-build's schema commit [as ruled].
3. Q3 (a) with A.6; Q4 and Q5 confirmed; Q6 (a) amended for N1-P; Q7 the f = 0.10 decision when the cap binds; Q8 Appendix A with §1.8's amendments [as ruled].
4. The block's §3 readings and PIN-n-20 to -26, -12 and -16 as amended: accepted; PIN-n-26 the lock's form [as ruled].
5. The order of §3; close lines on `8e3bf91`'s entry citing this raw [go].
