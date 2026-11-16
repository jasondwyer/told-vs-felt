# n — G-ANL-n: nine questions for the seat before its canonical run (Code → design)

*The n-analyzer session (Code), PI date 2026-11-16. For the PI to route. It asks what PROPOSAL-n v0.2 leaves open for `n_analyze.py` (n §3 "G-ANL-n", §8 step 9), before the analyzer's canonical run binds an answer; the coordinating session asked for it as one early block. What ran: nothing on a model and nothing of record. In this session's scratch, in battery windows the coordinating session granted (nice -n 19, model-free): the draft analyzer's battery (154 checks, all passing at its last run, the reader built from the committed schema included; a draft, not of record) and two short scripts that read BK's `reduced.json`; their figures are marked [C]. Earlier Python processes, and short system-Python runs, are disclosed in the entry. Sources read: PROPOSAL-n v0.2 at root (sha256 `30a3d0f5…04f4`); the seat's answers of 2026-11-15 (`1f3ce1f9…df84b`, committed at `a215c28`), §2.3, §5 and §9; the read runner's record schema, `valence_core/n/schema.py` at `5a97527` (sha256 `77c12d6d…94bc`); BK's `prereg.json` (`c55ab6b9…`), `analysis.json` (`12c35645…`) and `reduced.json` (`ec5fea59…`) under `data/n/bk`, each its `SHA256SUMS` entry; BK's paper (sha256 `e92c69cb…fa49`; the PDF now sits in a reference subfolder of the folder the proposal's header names, its sha256 unchanged). n-build's block of the same date, `results/raw/2026-11-16_n-schema_code-to-design_questions.md`, asks its own questions; this block cites its Q2, Q3 and Q5 where they touch these. Not opened: any checkpoint, report or verdicts file; nothing under `data/mf3` or `data/p`. `n:N` is PROPOSAL-n v0.2's line N at root. Calendar dates only; the commit hash is the record.*

## 0. The short form

- **What this block stops:** G-ANL-n's canonical run, which writes the artifact and fixes the analyzer sha256 that LOCK-n v0.1 binds (n:117), and with it LOCK-n v0.1; and anything else that would bind a pending answer. Both wait for the seat's answers and the PI's routing.
- **What it does not stop:** the build. `n_analyze.py` and its battery are built, reviewed and may be committed carrying the readings below, each registered in the code as OPEN-Q1 to OPEN-Q9 and tagged *pending the seat* in the battery's lines that test it. n-build's steps (the package, G-VEC, G-CAL-n) are not touched.
- **Nine questions,** Q1–Q9 (§1). Each gives the text that leaves it open, the reading Code carries meanwhile, its consequence, and the alternatives, as readings or in its ask. §2 lists facts declared without a question, §3 the readings Code declares as its own, §4 the order. Appendix A gives Code's sentence forms verbatim.
- Code adjudicates nothing.

## 1. The questions

**Q1. The slope fit.** n:126: "per arm, the OLS slope of Δm on d over the arm's own dose points, per session, with its mean and CI; **the floor for an arm** = the largest |mean slope| among the 24 random directions refit on that arm's dose points (C12)". BK's paper: "Slopes are obtained via an ordinary least-squares (OLS) regression of the difference in the choice margin on dose" (Fig. 4's caption; Figs. A7–A12 say the same in other words). BK's `prereg.json` (`rules.primary`): "the OLS slope of the paired difference d(dose) = margin(dose) - margin(0) on signed dose over the five points … d is identically zero at dose 0 by construction". None of the three says whether the fit has an intercept, and the paper's text carries no intercept or origin wording.
- On BK's symmetric grid the two fits coincide: 0.9164 either way, the floor 0.3641 [C]. On N1-V's points they do not. On N1-V's grid restricted to BK's own points {+1, +1/2, 0, −1} (BK read neither d_eq nor d_20), BK's 160 sessions give 0.9114 with an intercept against 0.9329 through the origin, and the 24-direction floor 0.3658 against 0.3641 [C].
- The fit enters N1's conjunct (ii) (n:136: the valenced mean slope against its floor) and every arm's reported slope.
- Readings: (a) OLS with an intercept over the arm's dose points, d = 0 with Δm(0) = 0 included where the arm lists it; (b) a fit through the origin over the nonzero points.
- Carried meanwhile: (a), pending the seat.

**Q2. The leak ceiling where N1-P is not read.** n:122: "Per dose point: L(d) = max over the 24 random directions of |mean Δm| (N1-R), and P(d) = |mean Δm| of the same-pole arm N1-P at that dose … certified at d iff |mean Δm_V(d)| > max(L(d), P(d))" (the second fragment's bold dropped). §2.4's N1-P row reads +1 and −1 only. Dose certifies at d_eq (n:138); N2 at the norm-matched point (n:140), d_20's. Neither has a P(d) unless the point merges into +1.
- Readings: (a) where N1-P is not read, the ceiling is L(d) alone; (b) P(+1) carried to every positive point as an upper bound; (c) N1-P read at d_eq and d_20 as well (+320 reads, positive doses only; a read-set change, the lock's).
- Consequence: under (a), DETECTABLE at d_eq is judged against the random directions alone; (b) is stricter wherever P(+1) > L(d).
- Carried meanwhile: (a), pending the seat.

**Q3. "Answered", and a dose sentence §5 lacks.** n:32 (§0.6): a null read is *concluded, not answered* "unless (i) that design's told positive control … PASSED and (ii) G-READ-n (§3) PASSED for that axis and dose". n:142: "PASS licenses the *answered* reading of nulls in this format on this checkpoint (§0.6, with G-READ-n); nothing else". n:138: "**NOT-DETECTABLE** otherwise — *answered* under G-READ-n PASS at d_eq, else *concluded, not answered*".
- Readings: (a) §0.6 governs: answered iff N4 PASS and G-READ-n PASS; (b) the dose clause governs the dose sentence: G-READ-n PASS alone.
- Under (a), a NOT-DETECTABLE with G-READ-n PASS and N4 not PASS is concluded, not answered, but §5's one not-answered sentence ("…and not readable at the decision: dose is an explanation of record, unresolved", italics dropped) would be false there: the state is readable. Of the tuple pass's 1,920 evaluations of the 384 tuples, 256 fall in that cell [C]. Code's interim text for it is A.6.
- The same question for N1's NOT-REPLICATED (n:136 names "G-READ-n FAIL at d = +1" only) and for N2's null (n:140 gives no label; §0.6 covers any null read).
- Carried meanwhile: (a) for dose, N1 and N2, with A.6's text, pending the seat. Ask: (a) or (b) for each, and the sentence for the (G-READ-n PASS, N4 not PASS) cell.

**Q4. Inputs that change a sentence but are not coordinates.** n:115's tuple carries "G-READ-n for N1-V at d_eq {PASS, FAIL}". Three more inputs change a sentence:
- G-READ-n at d = +1, for N1's NOT-REPLICATED label (n:136);
- G-READ-n for `span_reward` at f = 0.20, for N2's null label, under Q3 (a);
- N4's INDETERMINATE "with *no read obtained*" against its terminal INDETERMINATE (n:142).
- Carried meanwhile: inputs, not coordinates. This follows m:278's precedent ("the f1 dose-note text conditioned on the 0.12-artifact-existence input flag", bold dropped). The battery evaluates every tuple under every value of these inputs: 384 × 4, plus 96 × 4 for N4's second INDETERMINATE form, plus NOT-RUN, for 1,921 evaluations. The tuple count stays at 385. Ask: confirm, or make any of them a coordinate (the count then changes).

**Q5. Tuples that cannot occur.** Dose is INDETERMINATE exactly when N1 is (n:138; its "or the points are incomplete" is N1-V's or N1-R's reads, whose incompleteness already makes N1 INDETERMINATE, Q6). So 160 of n:115's 384 product tuples cannot occur on any dose map: 64 with N1 INDETERMINATE and dose decided, 96 with N1 decided and dose INDETERMINATE. With every point distinct, 28 (N1, dose, N2) triples occur, so 224 tuples (the 384 less the 160). §2.3's merges remove more [C, the draft battery's enumeration against Code's hand derivation]:
- d_20 at +1 (the cap binds, or 2·d_eq within 0.05 of 1): 24 triples, 192 tuples. N1 REPLICATED or PARTIAL needs conjunct (iii) at +1, which is then N1-V's certification at d_20, so N2 cannot be NULL;
- d_eq at +1 as well: 17 triples, 136 tuples.
- These counts assume n-build's form of the merge (a merged point read once under the label kept, N1-R included), which n-build's block asks as its Q3.
- Carried meanwhile: the sentence functions are total — one sentence set for each of the 385, as n:115 asks — and the battery reports separately which tuples can occur on each merge shape, and so on the pinned map once G-CAL-n pins d_eq. Ask: confirm; or have the analyzer refuse the impossible tuples, the form m's v2 battery gives PENDING tuples (m:291; the seat's A2 of 2026-11-06).

**Q6. INDETERMINATE causes §5 does not name.**
- N1: N1-V incomplete. n:136 names N1-R and N1-P; n:134: "An arm with a partial read set is INDETERMINATE". Carried: N1 INDETERMINATE.
- Dose: "the points are incomplete" (n:138). Carried: N1-V's or N1-R's reads incomplete, reported beside N1's cause.
- N2: n:140 names "an unadjudicated pause … on N2's reads" only. Carried: N2 is also INDETERMINATE when N2-E, N1-V or N1-R is incomplete, and N1-P where d_20 sits at +1 (the cap binds, or 2·d_eq within 0.05 of 1), whose P(+1) the ceiling then takes: the arms its certification reads. A pause standing on N1-V's, N1-R's or N1-P's reads leaves N2 evaluable, as written.
- N4: n:142 names "the arm is incomplete or E undefined". Carried: a pause standing on N4's reads makes it INDETERMINATE with no read obtained.
- Readings: (a) the causes carried above; (b) the named causes only. Consequence of (b): N1 would be judged on a partial N1-V; N2 would be certified on figures from incomplete arms (in the shapes where d_20 sits at +1, on a partial N1-P's P(+1)); N4 would be judged with a pause standing on its reads.
- Carried meanwhile: (a). Ask: confirm or rule each, pending the seat.

**Q7. The norm-matched point when the cap binds.** n:81: "d_eq = (0.10 · R_ℓ)/(ρ · R) and d_20 = min(1, 2·d_eq)"; N2's directions are "scaled to f · R_ℓ at f ∈ {0.10, 0.20}". N1-V's and N1-R's largest norm is ρ·R, at d = ±1. If 2·d_eq > 1:
- N2-E at f = 0.20 (norm 0.20·R_ℓ) exceeds every N1-V point;
- d_20 is 1;
- n:140's "N1-V's at the norm-matched point", and the leak ceiling there, are taken at the smaller norm ρ·R, a ratio of 2·d_eq.
n:81's own illustration (55.45 against R ≈ 25.49) would give d_eq ≈ 0.725 and a ratio ≈ 1.45 [C].
- Carried meanwhile: the norm-matched point is d_20's, as pinned, with the ratio reported beside N2's outcome. It assumes n-build's form of the merge, which n-build's block asks as its Q3. Ask: confirm, or rule another form for that case (for example N2 decided at f = 0.10, or N1-V and N1-R read at 2·d_eq, a read-set change). The seat may prefer to rule once G-CAL-n pins d_eq.

**Q8. The sentence forms Code wrote.** §5 words four cells: N1 REPLICATED (n:136) and the three dose sentences (n:138). Code wrote the rest, verbatim in Appendix A:
- N1's PARTIAL and NOT-REPLICATED (n:136: they "name the failing conjunct and the figures");
- every INDETERMINATE and NOT-RUN;
- N2's four descriptive lines (§7.3);
- N4's five lines;
- the expansion of the "…" in the not-answered dose sentence (Code adds "the state is");
- Q3's interim cell.
Three points of wording:
- NOT-DETECTABLE also arises with |mean| above the ceiling but a CI including 0, where "the margin does not move beyond the leak ceiling" is imprecise.
- DETECTABLE and PARTIAL can carry a negative effect: the CI may exclude 0 on either side, and certification is on |mean|. The sentences then give the sign only through the figures.
- A G-READ-n cell not computed takes the not-readable sentence (§3, Code reads "not computed" as not PASS).
- Carried meanwhile: Appendix A, pending the seat. Ask: adopt, amend or replace each form.

**Q9. N2's slope (reported only).** N1-V lists d = 0 among its points (n:81); N2's row lists f = 0.10 and f = 0.20 only (§2.4).
- Readings: (a) N2's slope over its points on BK's scale, {0, d_eq, 2·d_eq} with Δm(0) = 0, its floor refit on the random reads at d_eq's and d_20's points; (b) over its two points alone; (c) on the program's scale f.
- No §5 outcome reads it.
- Carried meanwhile: (a), pending the seat.

## 2. Facts declared (no question)

- **BK's figures reproduce through the draft's own functions [C]:** §4's statistics on BK's 160 neutral sessions give G-DATA (iii)'s figures (Panel D 1.0900 / 0.5072 / −0.3841 / −0.7554; SDs 0.6233 / 0.3703 / 0.4546; slope 0.9164, SD 0.4466; random slopes −0.2880 to +0.3641). The fidelity ratio gives G-DATA (vi)'s: 0 of 2,400 above TAU, 570 above TAU/4, the largest 0.012143.
- **Secondary (b) has no free text to read:** the runner generates no reply (n:77: "No new text is generated for N1, N2 or N4"). n-build's block asks it (its Q2), so it is not asked here.
- **G-READ-n's capture layer** is n-build's Q5. The analyzer reads G-READ-n's status and band median AUC per axis and dose as given, so an answer there changes what G-READ-n computes, not the analyzer's inputs.
- **Reachability** is Q5's fact; the merges' further reductions depend on the d_eq G-CAL-n pins.

## 3. Not questions: Code's readings, declared (each strikable until LOCK-n v1.0)

- n:136's "exceeds its floor" (conjunct (ii)) is the signed mean slope above the floor.
- n:136's "its CI excluding 0" means the interval lies wholly on one side of 0; an endpoint at 0 does not exclude it.
- A G-READ-n cell that is absent or not computed is not PASS for §0.6.
- The bootstrap (n:126 "4,000 resamples, seed in the lock"): one resample matrix per arm, from the stream `n-boot|{arm}` under m:159's key-to-generator function, 4,000 rows over the arm's sessions in session order. Each arm's statistics use its matrix. The intervals are percentile intervals with linear interpolation: 2.5 / 97.5, and N4's 98% at 1 / 99. The lock states it.
- §2.3's merge rule: d_20, then d_eq, each folded into the nearest existing point (+1, +1/2, 0, −1, then d_20 if it was kept) at a distance ≤ 0.05 (in double precision), else added; a tie goes to the earlier candidate; a value equal to an existing point (d_20 = 1 under the cap) is that point; a fold into 0 is refused. The analyzer re-derives the merges from d_eq and d_20, and its reader, built from the committed schema, refuses a dose map whose recorded merges differ. n-build's schema checks the same rule on its side (agreed 2026-11-15; committed at `5a97527`). That the merge reaches N1-R and that a merged point is read once under the label kept is n-build's block's Q3.
- Conjunct (iv) is evaluated: the −1 pole is read under A1, "struck beyond d = −1" (the routing of 2026-11-06).
- The TAU/4 sensitivity row (n:77, n:128 (f)): a read whose re-computation exceeds TAU/4 is dropped. A shadow that exceeds drops its session's Δm at every dose, and a session missing a point drops out of the slopes. Reads with no re-computation are kept.
- The label-mass counter (n:128) counts restricted reads with two-label mass below .20, the reference N-lap's gate cites (n:99; m:283).
- Secondary (d) is Pearson's r between the retention interval and Δm at +1, over N1-V's sessions.

## 4. The order

The build goes on, under the coordinating session's windows. G-ANL-n's canonical run and LOCK-n v0.1 follow the seat's answers. If an answer changes the analyzer, the change lands before that run. The schema's commit (`5a97527`) is the reader's reference.

## Appendix A. Code's sentence forms, verbatim (pending the seat; Q8)

The bracketed slots are filled at VERDICTS. "theirs 1.09 [1.00, 1.19]" is text, not a slot.

- A.1 N1 PARTIAL: *PARTIAL: BK's fixed-text effect on OLMo-2-32B Instruct, in this program's implementation [on their / on a reconstructed direction], meets (ii) and (iii) and its CI at d = +1 excludes 0, but [failing] fails: Δm(+1) = [x] nats [CI], theirs 1.09 [1.00, 1.19]; Δm(−1) = [x−] nats [CI−]; slope [y] against a floor of [z]; leak ceiling [max(L, P)]*
- A.2 N1 NOT-REPLICATED: *NOT-REPLICATED: BK's fixed-text effect does not replicate on OLMo-2-32B Instruct in this program's implementation [on their / on a reconstructed direction]; [failing] fails: Δm(+1) = [x] nats [CI], theirs 1.09 [1.00, 1.19]; slope [y] against a floor of [z]; leak ceiling [max(L, P)] — [label]*
- A.3 INDETERMINATE: N1: *INDETERMINATE: N1 is not evaluated ([causes])*; dose: *INDETERMINATE: the dose question is not evaluated ([causes])*; N2: *N2, descriptive (§7.3; it licenses no thesis sentence): INDETERMINATE: N2 is not evaluated ([causes])*; N4: *INDETERMINATE, no read obtained ([causes])*
- A.4 NOT-RUN (all four slots): *NOT-RUN: [reason]; no question of PROPOSAL-n v0.2 §1 is answered on N-pod*. The [reason] by cause ({date} is D_n, 2026-12-15; {stage} the STOPPED gate): clock:no-box *LOCK-n v1.0 was not committed by its Clock date ({date}): no box*; clock:gate-stopped *LOCK-n v1.0 was not committed by its Clock date ({date}): {stage} STOPPED and no re-specification was locked*; clock:pi-declined *LOCK-n v1.0 was not committed by its Clock date ({date}): the PI declined v1.0*; clock:not-locked *LOCK-n v1.0 was not committed by its Clock date ({date})*; no-arm:pi-stop *locked, and no arm's full read set was produced before a PI stop*; no-arm:gver-stop *locked, and no arm's full read set was produced before a G-VER STOP*; no-arm:cap *locked, and no arm's full read set was produced before its cap*
- A.5 the not-answered dose sentence, expanded: *at this program's dose the margin does not move beyond the leak ceiling and the state is not readable at the decision: dose is an explanation of record, unresolved*
- A.6 dose NOT-DETECTABLE with G-READ-n PASS and N4 not PASS: *at this program's dose the state is readable at the decision (AUC [a]) and the margin does not move beyond the leak ceiling, but BK's apparatus has not registered an instructed preference on this checkpoint (N4 [n4]): dose is an explanation of record, unresolved*
- A.7 N2: SPECIFIC *N2, descriptive (§7.3; it licenses no thesis sentence): SPECIFIC: at f = 0.20 this program's evaluative axis (span_reward) does not move BK's apparatus beyond the leak ceiling (Δm = [xE] nats against [c]) while the valence direction of record at the norm-matched point does (Δm = [xV] nats) — [label]*; SHARED *N2, descriptive (§7.3; it licenses no thesis sentence): SHARED: at f = 0.20 this program's evaluative axis (span_reward) moves BK's apparatus beyond the leak ceiling (Δm = [xE] nats [CIE] against [c]); the valence direction of record at the norm-matched point: Δm = [xV] nats*; NULL *N2, descriptive (§7.3; it licenses no thesis sentence): NULL: at f = 0.20 neither this program's evaluative axis (span_reward, Δm = [xE] nats) nor the valence direction of record at the norm-matched point (Δm = [xV] nats) moves BK's apparatus beyond the leak ceiling ([c]) — [label]*
- A.8 N4: PASS *PASS: BK's apparatus registers an instructed preference on this checkpoint: m_told = [x] nats [CI98] against E = [e]; it licenses the answered reading of nulls in this format on this checkpoint (§0.6, with G-READ-n), nothing else*; REVERSE *REVERSE: m_told = [x] nats [CI98] below −E = [-e]*; DEAD *DEAD: the 98% CI's upper bound is below 0.5 nats: m_told = [x] nats [CI98]*; INDETERMINATE (terminal) *INDETERMINATE: m_told = [x] nats [CI98] against E = [e]*
- A.9 the failing conjuncts' names: i: *conjunct (i) (Δm(+1) ≥ 0.545 nats with its 95% CI excluding 0)*; iv: *conjunct (iv) (Δm(−1) < 0 with its 95% CI excluding 0)*; ci+1: *the 95% CI at d = +1 excluding 0*; ii: *conjunct (ii) (the valenced mean slope above its floor)*; iii: *conjunct (iii) (G-LEAK-n certification at d = +1)*
