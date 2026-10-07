# G-PORT -- F0m (Q-F0, A0/A0s) against f1 CORR: every difference the port and a five-lens comparison reveal, classified against PROPOSAL-m v1.11 §2.7's fourteen (m:267)

Method. Five read-only lenses (harness bytes; delivery and rng; generation and reads; audit and exclusion; records, verification, printing and statistics) each enumerated F0m-vs-f1 differences against HEAD 5f7b968 and f1's `jlens-qwen36/scripts/f_sessions.py`, classifying each as covered by one of §2.7's fourteen or beyond them; every claimed difference was put to a STRICT refuter (refutes only if factually wrong; separately judges the classification). 90 claimed, 1 refuted, 89 surviving. A synthesizer de-duplicated the survivors (Part 1, verbatim). Part 2 is Code's own tokenizer-only recount that settles the synthesis's open [verify] (F6). Part 3 is every lens claim with its refuter's verdict.

---

## Errata (Code, after the entries' values-check pass 1; the synthesis below is kept verbatim)

- **A20, "no f1 analysis reads `graded`": wrong.** f1's SCREEN VERDICT entry (archive/RESULTS-cycles3-4.md:106–113) used the in-session grades: the CORR accuracy covariate PROPOSAL-f:86 pre-registered, P .838 vs Q .833 (244/291, 255/306), DIFF's in-session gap .883/.592 and FDBK's composition 93.4% correct. A values-check agent reproduced these from `graded`. m computes no in-session covariate (its covariate of record is G-CAL's, m:176).
- **A1's quote of m:261.** m:261 reads "Valid-session rule of record: f1's (… `valid` = not excluded, :439)", not "the valid-session rule of record".
- **F5 / "(12) and (14) … unaffected".** It is true of the realised record (no f1 CORR exclusion came from a clipped generation), but 5 of the 135 clipped generations are CORR, post-pick, in sessions f1 kept valid; whether any would have hit unclipped is not settled.
- **The G-PORT walk and newlines.** The walk bounds every generation by the next harness piece the scaffold built. For a transcript's last generation that piece is the bare final "\n" joiner, anchored by the end-of-transcript and rebuild checks (scaffold.py's PIN reworded accordingly).
- **Scope of the lenses.** All five compared HEAD 5f7b968, before the disposition changes to readrule.py and stages.py (ruling (h)); the 52 "internal, no effect" notes were not refuted.

## Part 1 -- the synthesis (verbatim)

# G-PORT: F0m (Q-F0, A0/A0s) against f1 CORR, de-duplicated differences

**Basis**
- The findings come from five lenses: HB harness-bytes, DR delivery-rng, GR generation-reads, AE audit-exclusion, RS records-stats. Every item below survived a strict refuter.
- Where a refuter's covered_by_verdict differs from the finder's, the refuter's is used, and the item says so.
- F0m anchors are HEAD 5f7b968, read with `git show`. f1 anchors are `jlens-qwen36/scripts/f_sessions.py` unless a file is named.

**What I re-checked myself** (model-free, jlens venv):
- A recount of `data/f/sessions.jsonl`. These figures reproduce exactly: 28/56 valid vs 30/58 reached; maps 18/29 and 10/27 vs 19/30 and 11/28; sham 18/33 vs 19/34; post-pick exclusions s4, s25 and sham s35; exclusions 8/64 and 7/40, of which 6 and 6 pre-pick; pooled lexical 19/344, cap 14/3,074, low mass 165/1,745; 0 `special:` rounds.
- A run of the AE refuter's audit probe against m's `QwenTaskRoundAudit`. `audit.py`, `scaffold.py` and `corr.py` have no working-tree diff against HEAD.
- m:358 step 11 (see A6).

**Totals**
- 25 items beyond §2.7 (section A).
- 2 borderline items, beyond §2.7 in the letter, where the refuters split (section B).
- 9 covered items whose consequence §2.7 leaves unstated (section C). Two of them bear on the primary: C1 under (3) and C2 under (6).
- Bearing on A0's comparison with f1's primary:
  - A1 directly.
  - A2 and A3 on the criterion and the label.
  - A4 on n and power.
  - C1 and C2 under covered items.

---

## A. Beyond §2.7's fourteen, most consequential first

### A1. The primary's domain: f1 used whole-session validity, m uses "reached the first read" (the sham envelope E follows)
**Classification:** beyond. All finders (HB, DR, AE, RS×2) and all refuters agree. It is disclosed only in §4 (m:306–308), and m:261 still calls f1's `valid` the "valid-session rule of record".

**f1:**
- `valid = not excluded` (:439). The primary takes first picks from valid sessions only (:461–462), by map (:467–473).
- The sham pseudo-Δ is also computed on valid sessions (:454–457).
- A free-round lexical hit after the pick still excludes the session (:373–375).
- The floors are valid-n floors (PROPOSAL-f:64, :101–102).

**F0m:**
- `domain` means: all forced rounds unclaimed, no forced hair trigger, no forced exclusion. It is asserted equal to "reached the first read" (scaffold.py:429–432).
- `first_free_pick_P` is set iff `domain` (:445).
- A free lexical exclusion keeps the domain (runner_qwen.py:16–21, :199–205; verify.py:251–256).
- The sham share is taken over `_forced_domain` (readrule.py:605–613).
- The sham envelope uses the same rule (m:308). E is computed over the matched sham's domain (m:310).

**Effect:** bears on A0's comparison with f1's primary.
- f1's figure of record is 28/56: Δ .000, map A 18/29, map B 10/27, p .553.
- Under m's rule the same archive gives 30/58: Δ +.017, map A 19/30, map B 11/28, p .448. The two sessions that differ are s4 (lexical:prism@free4) and s25 (lexical:maple@free4); both picked P first.
- The sham moves from 18/33 (E .0455) to 19/34 (E .0588), because s35 (lexical:saddle@free5, picked P) comes back in.
- CORR's Δ stays below E under either rule.
- With m's audit as well (see C2), the count is again 28/56 (map A 17/28, map B 11/28), but on a different set of sessions: s25 and s48 drop out and s4 comes in.

### A2. Conjunct (iii): A0 is held at α .01 in the direction under test, where f1 used one-sided p < .05 toward P
**Classification:** beyond (RS; refuter agrees). It is declared at m:182, m:310 and m:326, so the port did not newly reveal it.

**f1:** CORR's p is the upper tail, p_hi (:474, :477), and conjunct 3 is `conj3 = p < 0.05` (:482). See also PROPOSAL-f:86 and :106.

**F0m:**
- Control α .01, by an exact one-sided binomial against .5 in the direction under test, with a REVERSE outcome (m:310, m:326).
- The analyzer, `scripts/m_analyze.py`, does not exist at HEAD.

**Effect:** changes the criterion A0 is held to, not the share. The critical counts are 60/96 and 51/80 (m:190); at α .05 they would be 57/96 and 48/80.

**Refuter corrections:**
- The ≤-vs-< half cannot be observed at p0 .5: tails are j/2^n, so none equals α for n ≤ 299. It is listed under E (internal).
- bars.py:158–161 is the bar rule, not conjunct (iii).

### A3. Outcome logic: f1's `screen_hit` boolean against m's ordered outcome set
**Classification:** beyond (RS; refuter agrees).

**f1:**
- `hit = conj1 ∧ conj2 ∧ conj3` (:478–483).
- No interval is computed and there is no reverse branch.
- A contrast with no first picks is skipped (:463–464).
- A reverse result is "reported, never celebrated" (PROPOSAL-f:89–90).

**F0m** (specification only):
- The order is INDETERMINATE (no domain session, or E undefined), then REVERSE, then PASS, then DEAD (two-sided Clopper–Pearson 95% upper bound on Δ_c below +0.15), then INDETERMINATE.
- A map with no domain session fails conjunct (ii).
- The verdict sentence states the arm's pre-pick exclusion rate beside its sham's, and the guard's result (m:310, m:324–326).

**Effect:** descriptive; it changes the label, not the estimate. The map-sign conjunct is equivalent wherever (i) holds: f1's "v ≥ 0 when d ≥ 0" (:479–481) means each map's share is at least .5 in the tested direction.

### A4. Floors: what they count, their sizes, the launch projection and the terminal conditions
**Classification:** beyond. (13) covers only the rotation and the stop at floor; refuter agrees.

**f1:**
- A fixed plan from `--n-arms` (:597–608): CORR 64 and sham 40, all run.
- Valid floors 48/32, counted on whole-session validity. Below floor means discussion with the design instance (archive/RESULTS-cycles3-4.md:139–144; PROPOSAL-f:101).
- No hour cap.

**F0m:**
- Floors are A0 96 cached / 80 uncached and A0s 32 (schedule.py:99; m:182), counted on domain sessions (stages.py:1906, :1909, :1935).
- L is a projection only (m:192).
- A unit ends at the floor, the hour cap (resume.py:986–998; stages.py:1911) or a PI stop.
- Below floor, the arm is analysed as obtained with α unchanged (m:247). G-PWR raises n before the run (m:190).

**Effect:** bears on n and power. Through A1, a session excluded at a free round counts toward m's floor but did not count toward f1's 48. Under m's rule, f1's DIFF (49) and FDBK (48) would have met 48. Schedule exhaustion is A14.

### A5. Per-property exclusion table: the reference value crosses a change of unit
**Classification:** beyond (AE, RS; refuters agree). The audit half of the shift belongs to (6).

**f1:** `Counter[(arm, rounds[-1].cfg)]` over all excluded sessions, any phase (:441–446). CORR gives P 7 vs Q 1 (archive:91–93), including s4 and s25, which are free-round exclusions on P.

**F0m:**
- arm × property: rounds generated, rounds excluded by class, sessions excluded pre-pick (m:314).
- Built from rounds[].property and the exclusion phase (scaffold.py:386–392, :413–415; stages.py:1698–1702).
- Reported in VERDICTS only (m:318). The analyzer is not built.

**Effect:** descriptive.
- On f1's archive, the pre-pick column gives 5 vs 1 under f1's audit (P: s27, s36, s49, s55, s60; Q: s53). Under m's audit it gives 5 vs 3, because s25 (forced0) and s48 (forced1) become corrupted-round content claims.
- Summing "rounds excluded by class" still gives 7 vs 1 (f1's audit) or 6 vs 3 (m's).
- The entry should say which column the 7-vs-1 is the reference for; m:314 does not.

### A6. f1's pooled pause monitors are not carried (lexical, cap-hit, low label mass); a sham-arm `round_degeneracy` look bar is added
**Classification:** beyond (AE×2, GR×2, RS; refuters agree). How far each is disclosed varies:
- Lexical: disclosed at m:330 and bars.py:32–34.
- Low label mass: disclosed at m:283 ("not carried").
- Cap-hit: disclosed nowhere. GR's refuter cited m:358 step 11, but "No cap trigger in Q-F0; `STOP_CAP = 60` stands" refers to Q-F3's reasoning-line cap trigger (m:174), not to f1's cap-hit monitor. I checked this.

**f1:**
- Evaluated when any contrast reaches n = 24 (:90) and at completion.
- Exact binomials pooled over all six arms, sham and excluded sessions included:
  - lexical session exclusions, p0 .05 (:418–421);
  - cap hits per round, p0 .10 (:422–424);
  - label_mass < .2 per read, on the stored 4-dp value (:363, :425–427).
- A pause fires on p < .05 (:431–433). The run returns at :664–670; completion flags at :672–677.

**F0m:**
- Q-F0's campaign bars are `round_degeneracy` (sham arm only; rounds claimed by v2 or echo; p0 .05; every look) and the guard (bars.py:539–565, :568–591).
- Lexical is a counter only (audit.py:579–580). So is cap_hit (audit.py:586–587; readrule.py:537).
- `low_label_mass` is computed on the unrounded value (scaffold.py:408; LOW_LABEL_MASS .20 via runner_qwen.py:55). At looks it is reported over all reads for the sham and first reads of domain sessions for the contrast (stages.py:1705–1721, :1750).
- At G-F0m-Qwen the contrast's first-read flags are reported (stages.py:1360–1369, :1421–1422). This corrects GR's "withheld at gate stages"; they are withheld only at G-TIME.

**Effect:** descriptive; these are pause rules only.
- None of f1's monitors came near firing: lexical 19/344, cap 14/3,074, low mass 165/1,745 (CORR: 42/346 reads, 26/58 first reads).
- No stored label_mass equals exactly .2000, so the rounding never mattered.
- Under m, a priming-driven rise in lexical exclusions (item (1)'s exposure) can pause only through the guard: pre-pick, Fisher against a sham whose banner also names labels, or the absolute .20 bar. A free-round rise pauses nothing.

### A7. Exclusion guard: numerator, comparator, arming, cadence and boundary
**Classification:** beyond (AE, RS; refuters agree). m:316 states the change of unit, but outside §2.7. The comparator's content is (4); a shared vs a matched sham follows from (13).

**f1:**
- Per contrast, at that contrast's n = 24 and at completion (:90, :399).
- Numerator: whole-session `excluded` (:398, :401).
- An absolute binomial against .20, and a one-sided Fisher against the one shared sham, armed only at sham n ≥ 12 (:408).
- Pause on p < .05 (:412–415).

**F0m:**
- Per contrast arm at every look: every 40 launches pooled over A0 and A0s (stages.py:1931–1932), and at the end (:2013).
- Numerator: pre-pick (forced-phase) exclusions (stages.py:1698–1702; bars.py:509–510).
- Fisher against the matched A0s at every look, with no minimum sham n (PIN, bars.py:420–424).
- The absolute .20 bar binds on Qwen (bars.py:587).
- Fires iff the exact P ≤ .05 (bars.py:425–429).
- Resuming needs recorded adjudication text (stages.py:1893–1898).

**Effect:** pause only, never a verdict. On f1's archive the numerators move from 8/64 to 6/64 for CORR (8/64 again under m's audit) and from 7/40 to 6/40 for the sham.

### A8. Pre-campaign stages: f1's smoke against G-TIME-F0, G-ID-F0m and G-F0m-Qwen
**Classification:** beyond (AE, RS; refuters agree). Parts overlap other items: (11) for G-ID's licence, (7) for the gate keys, (9) for the verify cadence.

**f1:**
- A smoke at offset session indices (:591–595), with verify_every = 1.
- `smoke_bar_check` runs after every session (:497–511, :629–662):
  - lexical binomial at p0 .05 over all smoke sessions;
  - audit exclusions above 20% of n_done once n_done ≥ 6, with the numerator taken from the sham arm or sessions excluded in the P config;
  - cap hits above 10% of sham-plus-P rounds once rounds reach 10.
- The record holds two smoke blocks: `data/f/sessions_smoke.jsonl`, 24 rows at s 1000/1004 and 1100/1104.
- f1's screen had no round-degeneracy bar (:391–434).

**F0m:**
- G-TIME-F0 (one A0 and one A0s session, uncached), G-ID-F0m (A0s pairs) and G-F0m-Qwen (16 A0s and 8 A0). All are excluded from the campaign.
- Hair triggers run on every session.
- `round_degeneracy` is evaluated once at stage end, on sham-template sessions only, excluded sessions' rounds included. The critical count is 3 at n 10 and 14 at n 160 (bars.py:530–537, :568–591, :853–903; m:271, m:280–283).
- Contrast sessions are reported beside, not bound. There is no lexical or cap bar.
- The qualification valid rate r feeds the launch rule (m:283).

**Effect:** none on the DVs, since gate sessions are excluded. Descriptive through r, which sets the launch counts.

### A9. Hair triggers stop the stage: `scaffold_absorption` (which also cuts a free-round session), `template_breakage`, `schedule_mismatch`
**Classification:** beyond (HB, DR, GR, AE, RS; refuters agree). Declared in §3 (m:271), not among the fourteen.

**f1:**
- A ban string returns `special:{s}` (:132–134).
- At a forced round that is an audit exclusion and the session ends (:339–345).
- At a free round it becomes post_degen and the session runs on (:368–372).
- No run ever stops on it. The smoke's "hair trigger" (:507) is a rate bar above 20%, not a one-hit stop.
- The ban file is the same on both sides (`e2a_ban_list.json`, sha256 9a2f0744…).

**F0m:**
- Forced round: a v2 exclusion (runner_qwen.py:168–169), then the trigger and a break (:170–173).
- Free round: the trigger and a break, with no exclusion and the domain kept (:199–203; self-test :299–305).
- Recorded at scaffold.py:417–422; `on_fire` is STOP (bars.py:513–528).
- The STOP is enforced at stages.py:1351–1357 (gate stages), :1540–1546 (G-ID) and :1936/:1947–1949 (campaign).
- A contrast session's free-phase fire is announced by phase only (stages.py:1055–1059).

**Effect:** none on the first pick. A forced hit excludes in both apparatuses, and a free hit comes after the pick.
- The later positions are lost; the session stays in the domain but is incomplete.
- The stage or campaign STOPs. After a PI stop it is analysed as obtained; if no session reached a first read it is NOT-RUN (m:284, m:324).
- It never happened in f1: 0 `special:` rounds in 3,074, all arms.
- Shared rather than a difference: f1's halt when the recomputed KL is not 0 (:212–214) is kept in `guard.insulated_read`.

### A10. G-VER: each session is rebuilt before its record is written
**Classification:** beyond (GR, RS; refuters agree). Its KL clause overlaps (9). The schedule compare at stage start belongs with (8).

**f1:** no per-session verifier. The row is appended as generated (:386–387). The only construction check is the KL re-forward on the verify_every cadence (:205–215).

**F0m:**
- `verify_session` and `verify_and_mark` (verify.py:83–267) rebuild the cell, keys, banner, seeds, items, deliveries, menus and every harness byte.
- Each pick is checked against its recorded read, and verify_kl must be exactly 0.0 (:186–201).
- `record_session` refuses an unverified record (resume.py:908, :923–925).
- At each stage start the committed schedules are compared byte for byte with a rebuild (schedule.py:620–649, via stages.py:744–778).

**Effect:** none on the DVs; a mismatch is a hair-trigger STOP. The pick-against-read check cannot fire on a genuine record, because p_a and p_b share one positive divisor.

### A11. A boundary assertion before every generation
**Classification:** beyond (GR; refuter agrees). The chunking itself is (14).

**f1:** one encode of prefix plus segment and one extend; no boundary is computed (:162–168).

**F0m:** `assert_boundary` re-encodes and halts unless the token boundary equals the prefix token count (scaffold.py:308–320; rule 28(d)(a)). It runs before both generate calls (runner_qwen.py:158, :189).

**Effect:** none. It adds encodes only, no forward, and maps/e2a.md F13 shows the boundary equals the prefix length on every join shape. It is a new HALT condition.

### A12. How a bar fires: exact P ≤ α against float p < .05
**Classification:** beyond (AE, RS; refuters agree). Declared at m:271.

**f1:** `< 0.05` at :412–415, :431–433 and :504. Tails are floats via lgamma (:144–151); Fisher is an int/int ratio (:154–159).

**F0m:** exact Fractions, with float p0 or α refused (bars.py:90–104). `fires` and `fisher_fires` use `<=` (:158–161, :210–211); so does `Bar.evaluate` (:425–430).

**Effect:** pauses and stops only.
- On the binomial bars the rules disagree only at n 1, k 1, p0 .05, which is G-TIME-F0's round-1 case: f1's float gives 0.05000000000000001 and stays silent, m's 1/20 fires.
- Fisher ties at exactly 1/20, for example (1,1,0,19), (2,4,0,12) and (2,6,0,19), fire in m and stay silent in f1.
- The absolute guard bar (p0 1/5) can never tie.

### A13. Monitoring cadence and end evaluation
**Classification:** beyond (RS; refuter agrees).

**f1:**
- The guard runs at a contrast's n = 24 and at completion.
- The pooled bars are not deduplicated: they re-run after every session while any contrast sits at 24. A replay of the plan shows 11 pooled evaluations, at sessions 127–131 and 145–150 (:90, :399–417, :661, :672–677).
- The guard is re-run at completion even when that coincides with n = 24.

**F0m:**
- LOOK_EVERY = 40 (resume.py:91), pooled over both arms (stages.py:1931–1932).
- When the end falls on a multiple of 40, the end look is reused and not re-evaluated. A fired end look pauses before analysis (stages.py:2007–2020).
- The look index is checkpoint state (resume.py:14–18, :579–588).

**Effect:** descriptive.

### A14. Running out of schedule pauses for the PI
**Classification:** beyond (DR; refuter agrees).

**f1:** a fixed plan; nothing can run out (:597–607).

**F0m:**
- The committed schedules hold A0 2,624 and A0s 960 cells (schedule.py:102–116; MAX_UNITS 82/30 at :142 and :928).
- An arm still below floor at the end of its file pauses with kind `schedule_exhausted`, and only a PI stop ends it (stages.py:1918–1923, :1885–1892).

**Effect:** none at the planned n, since it is reachable only past the k = 1 launch row; descriptive if reached.

### A15. Insulation assertion: f1 forbids six jlens modules, m one; two of f1's six load in every F0m Qwen process
**Classification:** beyond (GR, RS; refuters agree; also maps/e2a.md F11).

**f1:**
- FORBIDDEN_MODULES is `jlens_qwen.{fingerprint, forced_choice, interventions, conditioning, e2a, eval_awareness}` (:51–53), asserted absent at startup and after load (:527–528, :586–587; PROPOSAL-f:59).
- Generation uses a plain StreamSession with the ops kernel set by hand (:165–166).

**F0m:**
- Only `valence_core.e2b.statepresent` is asserted absent (guard.py:77, :119–121): at startup (runner_qwen.py:114), at session start (:129) and at every read (guard.py:127).
- The adapter imports `jlens_qwen.forced_choice` and `jlens_qwen.conditioning` (qwen_mlx.py:74–75).
- Cached rounds use `SteeredStreamSession(model, {})` (:309–313); uncached rounds use `forward_with_positional_state(…, {})` (:328–329).
- Insulation rests on `injections=()`, the AST call-site guard and the statepresent assertion (m:48).

**Effect:** none on the arithmetic. With empty function sets these paths are f1's line for line (conditioning.py:254–282 against model.py:296–321; forced_choice.py:27–58 against model.py:81–132). It is a disclosure: f1's own assertion would fail on F0m's apparatus.

### A16. Pre-declared secondaries with decidable-n floors
**Classification:** beyond for secondaries (a), (b), (d) and the 20-event floor (RS; refuter agrees with a correction). Item (12) covers only (a)'s window at positions 5–6.

**f1:**
- No secondary choice analysis was pre-registered (PROPOSAL-f §3, :99–119; archive:366–418).
- The post-screen descriptives are labelled post hoc (`f_postscreen_descriptive.py`:1–6) and use whole-session-valid sessions (:63–64).
- Refuter's correction: f1 did pre-register a floorless termination counter by arm × cfg × round position over all sessions (archive:207–239; :319–333, :447–452). It also had the per-property table, the FDBK composition and the CORR covariate.

**F0m:** (a) clean-label share by position 1–6 on "valid through p"; (b) lose-shift, contrast arms only; (d) per-pair first-pick shares plus habit identity; (e) termination per round. The floor is 20 events, count-only below it (m:312, m:308). None of this is built at HEAD.

**Effect:** descriptive. (e) is not new in kind: what remains is a floored "valid through p" form beside f1's all-sessions table.

### A17. A strict exclusion scope recorded and reported beside the lenient one
**Classification:** beyond (AE; refuter agrees).

**f1:** a single scope (:338–343, :366–375). Every free-round degeneracy is still kept (:333, :372), so a strict scope can be rebuilt.

**F0m:** `strict_exclusion` is the first claim in any phase (scaffold.py:394–395, :444; audit.py:353–354, :517–519). Before VERDICTS it is reported for sham templates only (readrule.py:602–604, :634–637; m:261).

**Effect:** descriptive. On f1's archive under m's audit, the first strict events are 8 forced and 7 free. Per the refuter's corrected breakdown, the free ones are 4 audit:frame, 2 stuck_attractor and 1 clean lexical (s4).

### A18. Choice-read and verify-KL numerics: MLX float32 against numpy float64
**Classification:** beyond (GR×2; refuters agree). The KL half could equally be filed under E.

**f1:**
- Softmax in float32 (:197–198). Pick rule pa ≥ pb, p_a = pa/(mass+1e-12), top-1 by `mx.argmax` (:200–204).
- KL in float32, the max of the two directions, halting on kl != 0.0 (:205–215).

**F0m:**
- Float64 softmax after max-subtraction (readout.py:44–48). Same pick and tie rule (:107–116; tie at :114).
- KL in float64 (readout.py:51–61, :117–119). It halts on a value above 0.0 (:123–133) and unless the value is a float exactly equal to 0.0 (guard.py:130–137).
- The logits come from the same forward, unembed and float32 cast (qwen_mlx.py:166, :171–173).

**Effect:** none on picks in practice.
- 33 of 1,745 f1 reads are exact ties: 7 of 346 CORR reads, including 3 of 58 CORR first reads (s4, s35, s50). Both runners give these to the menu-first label.
- Refuter's refinement: a second divergence regime exists besides both label probabilities underflowing. When the label logits are tiny next to the maximum (|l| ≲ |max|·2⁻¹⁶), float32 collapses them: f1 calls a tie and m separates them. This cannot be reached on f1's archive, where label mass is at least .04 on every tie.
- KL: the bar is the same exact zero. F0m could halt on drift that f1 would pass, but only in the far tail. All 88 of f1's verified CORR reads gave 0.0.

### A19. Session-level record schema
**Classification:** beyond (DR, AE, RS; refuters agree). Some field contents re-express (1), (5), (6), (7), (8) and (11).

**f1:**
- 15 keys (:377–385), the same on all 344 rows.
- `exclude_reason` is one string carrying the class, the tag or fragment, and the round index (:340, :342, :374).
- `exclude_cfg` holds P, Q or 'sham' (:344, :375). There are also `n_cap_hits` and `n_rounds`.
- One jsonl for all arms.

**F0m:**
- `m-session-v1` (scaffold.py:424–450; dict at :438–447).
- `cell` = {pair_index, pair, map, start, clause, P, Q}, plus keys, banner, note_lines, path and pieces.
- `exclusion` = {class, phase, detail}, with no round index and no role (:413–415).
- New: `strict_exclusion`, `domain`, `hair_triggers`, `complete`, `seconds` (perf_counter including reads, runner_qwen.py:206–209) and `verified`.
- Absent: `exclude_cfg`, `n_cap_hits`, `n_rounds`, `tag_P`, `swap`, `start_P`.

**Effect:** descriptive.
- A join needs a field map: start_P True is start 0, swap is map, cfg is role.
- `exclude_cfg`, which the 7-vs-1 rests on, must be rebuilt from `rounds[-1]`. Both runners stop at the excluding round, so this is exact.
- The per-record `path` field and path in the resume identity are new. The round path itself is item (11).

### A20. Per-round record, including the absence of in-session grading
**Classification:** beyond (GR, DR, AE, RS; refuters agree).

**f1:**
- Fields: cfg, tag, task = `it['task'][:40]`, seed, n_tok, cap_hit, lex, degen, term, graded, verdict (:331–334).
- `lex` is None whenever `degen` is set (:318). `term` is the first matching regex.
- `graded` = `grade(text, gold)` on every round with a gold (:326).
- `verdict` is a bool on every round, True only on FDBK P rounds.
- The model's text is kept only in the transcript.

**F0m:**
- Fields: phase, ri|ci, n, label, role, pole, property, item, task_text (full), template_index, seed, text, n_tok, cap_hit, stop_reason, audit, termination (scaffold.py:385–396).
- `stop_reason` is cap, eos or newline (qwen_mlx.py:275, :318, :335, :348).
- `audit` = {claim, detail, v3, advisory, echo_line, lexical_raw, scaffold, degeneracy, substrate, phase} (audit.py:363–368). `lexical_raw` is recorded on every round (:442, :457).
- `termination` is a bool.
- valence_core/m has no grader. Golds appear only in corr.py's pool validation and hygiene (:165–172, :433).

**Effect:** descriptive.
- m records no in-session accuracy by property. It can be rebuilt, since item, task_text and text are stored and grading is deterministic.
- f1 graded all 597 CORR rounds (499 True, 98 False), but no f1 analysis reads `graded`.
- `stop_reason` is a function of cap_hit, because `<|im_end|>` and `<|endoftext|>` are banned and an eos stop cannot happen.

### A21. Per-choice (read) record
**Classification:** beyond (GR, RS; refuters agree). verify_kl on every read belongs to (9), the dropped `ea` field to (10)'s disclosure, and the prefix length relates to (12).

**f1:** round, menu_a, pick, picked_cfg, label_mass and p_a rounded to 4 dp, top1_is_label, verify_kl (None unless verified), ea (6 dp), and post_degen when the round was degenerate (:361–372). There is no p_b, top1_id, menu_b, menu text or prefix length.

**F0m:**
- Fields: ci, n, menu_index, menu, menu_a, menu_b, read, pick, picked_role, picked_pole, prefix_tokens_at_read, low_label_mass, top1_not_label (:398–411).
- `read` = {pick, p_a, p_b, label_mass, top1_id, top1_is_label, verify_kl}, unrounded (scaffold.py:356–363).
- `prefix_tokens_at_read` costs an extra encode (runner_qwen.py:183).
- Post-choice degeneracy sits on the free round's audit claim, not on the choice.

**Effect:** descriptive. Read values compare with f1's only to 4 dp. f1's clipped-read count in (12) needed a tokenizer recount because f1 recorded no prefix length.

### A22. Rule-23 counters: definitions and keys (termination, post_choice_degeneracy, audit_degenerate)
**Classification:** split. The keying and schema half is beyond. What counts as post-choice degeneracy is covered by (6), per the AE refuter.

**f1:**
- `term` = the first matching regex (:321–325, :333), tabulated by (arm, cfg, round position) over all sessions (:447–453).
- post_degen per choice = the audit reason string (:368–372).
- No audit counter. The pattern file's sha is printed only (:555–560).

**F0m:**
- `termination` is a bool (scaffold.py:304–305, :392), keyed (template, phase) (audit.py:588–589). The PIN at :551–553 says the keys are never a tag, item, round index or property.
- `post_choice_degeneracy` = a free-round v2, echo or content claim, keyed (template, claim) (:554–555, :584–585).
- `audit_degenerate` is keyed by v2 category (:573–574; readrule.py:509–519).
- The pattern file's sha is asserted (scaffold.py:65–66, :295–301). It is the same file on both sides, sha16 014b3940d62401b0.
- Contrast free rounds are withheld at gate stages (readrule.py:565–585).

**Effect:** descriptive; all of it can be rebuilt from the records.
- f1 CORR has 9 termination rounds (s16, s25, s55, s58, s61), all `===\s*[Ee]nd`. f1 already counted all 9 as frame degeneracy, and m's v2 claims them as frame.
- Corrections to the AE finder:
  - s48's '=== END OF EVALUATION SESSION ===' is not a termination round; both sides' patterns are case-sensitive. It is a v2 `banner_terminator` claim, which is a matter for (6).
  - Termination attempts do not become new exclusions.
- post_degen: f1 has 10 events in 5 sessions. m's definition on the rounds as generated gives 13; under m's own session-end flow it gives 10 (s25's two events drop out; the content claims in s8 and s63 come in).

### A23. Per-session stdout line
**Classification:** beyond the fourteen (AE, RS; refuters agree), but already disclosed at m:318 and m:263.

**f1:**
- `[j/N] {arm} s{s}: first=P|Q|X EXCL {exclude_reason}  {secs}s` (:624–628). This prints the pick (sham sessions too), the tag, the round index, the audit sub-category and the seconds.
- Guard and pooled-bar lines carry 4-dp floats (:406–430).
- The smoke prints "Q-caused exclusions" by arm (:660–662).

**F0m:**
- `{stage} {template} s={s} valid|excluded:{audit|echo|content|lexical}@{forced|free}`. A contrast free-round exclusion prints as `excluded:excluded@free` (readrule.py:443–504; `_LINE_RX` at :98–100). Printed at stages.py:1355, :1544 and :1946.
- `content` is a fourth printed class (seat ruling (q)).
- Bar messages show the exact Fraction rounded half-up to 4 places, with `<=` or `>`. Hair-trigger messages carry no count (bars.py:214–224, :436–462).
- Stage reports go to JSON, not stdout.

**Effect:** none on the DVs; it is blinding.

### A24. Blinding before VERDICTS, and the order of analysis
**Classification:** beyond the fourteen (RS; refuter agrees). Declared at m:271 (a rule-25 departure) and m:318.

**f1:**
- No blinding. The analysis runs inside the runner (`--analyze`, :437–494, :543–545) and writes `data/f/screen_analysis.json`.
- Refuter's note: "every transcript read in full" overstates f1's screen. A full read is recorded only for the smoke (archive:131).

**F0m:**
- No pick-bearing artifact is read before VERDICTS, with four exceptions (m:318).
- Contrast transcripts are read with their free rounds removed; sham transcripts are redacted (readrule.py:325–440).
- Stage reports carry contrast forced-round material only, with free rounds withheld (:565–585), and sham first-pick shares pooled and per pair (:587–646). Qualification also reports contrast first-read flags (stages.py:1360–1369, :1421–1422). Contrast seconds are withheld (stages.py:1156–1162).
- The per-property table is VERDICTS-only.
- A separate pre-committed analyzer runs before the reads (m:278; not built).

**Effect:** none on the DVs; it changes when people see picks.

### A25. Checkpoint storage and resume identity
**Classification:** beyond (RS; refuter agrees). §2.7's resume-identity sentence specifies m's side but is not one of the fourteen.

**f1:**
- One JSON line per session, appended with `open('a')` and no fsync (:386–387).
- `--resume` skips (arm, session) pairs already present, with no identity check (:610–614). Without `--resume`, an existing file is appended to, not refused.
- The guard's `evaluated` set is rebuilt on each invocation (:615).

**F0m:**
- One atomic checkpoint JSON per stage under data/m/ckpt/ (resume.py:179–203), holding verified records only (:908–956).
- IDENTITY_KEYS (:93–96) are compared exactly in both directions (:471–480, :803–862), and resume is skip-only.
- An existing checkpoint without `--resume` is refused, as are ended stages. A pending end can only be re-finished. Provenance is recorded per invocation (:247–264).
- Nuance: on a pod change a gate stage restarts rather than being refused.

**Effect:** none on the DVs.

---

## B. Borderline: beyond §2.7 in the letter, where the refuters split
Both are scope or consequence gaps in a named item. I recommend a clause on that item rather than a fifteenth.

### B1. m's uncached generation path also has no encode limit, but (14) is worded for the cached path
**Classification:**
- The HB refuter calls it beyond, as a gap in (14)'s scope.
- The GR refuter calls it covered by (14) read with (11), a wording gap; the GR finder had already said covered.
- My view: beyond in the letter. Extend (14) to say "m has no encode limit on either path".

**f1:** every generation keeps the 512-token tail (:167; jlens model.py:74–79). f1 never generated uncached.

**F0m:**
- The encode happens before the cached/uncached branch (qwen_mlx.py:258–259). The uncached path re-forwards the whole sequence at every step (:324–340).
- max_length is None (:78–80, :97–110), and startup refuses any encode limit (runner_qwen.py:91–100). No window is asserted inside generate (:242–348).
- G-TIME-F0 is uncached by spec (m:280; scaffold.py:250; guard.py:225–226). If G-ID fails, every Q-F0 round runs uncached (m:267).

**Effect:** none on A0's comparison with f1's primary. Per (14)'s [C] count, which I did not recompute, no f1 generation passed 512 tokens before the first pick. Descriptive at later rounds. The chunking half of (14) does not apply to the uncached path, which is (11)'s.

### B2. Sham session s no longer shares contrast session s's cell
**Classification:**
- Both finders said beyond.
- The HB refuter said beyond, narrowly. The DR refuter said covered by (8) together with (5).
- My view: a consequence of (8) that nothing states. Add a clause to (8).

**f1:**
- The cell arithmetic ignores the arm (:275–278), so sham s carried CORR s's pair, swap, start_P and tag_P (40 of 40).
- Its items came from the SHAM pool (:265–267) and its rng from f|sham|s (:273–274).

**F0m:**
- Items are shared across arms (keys.py:96–109; scaffold.py:253–254; m:159).
- Cells come from per-arm schedule keys `m-sched|Q-F0|{arm}|{b}` (keys.py:142–145; schedule.py:217–232; stages.py:1924–1925).
- At gate stages only π is keyed per template (keys.py:148–154; schedule.py:244, :247–263). Map, start and clause are shared and only the pair differs.

**Effect:** descriptive. E and the guard pool over sessions in both apparatuses, and nothing pairs contrast and sham sessions by index. At the same s:

| Sessions compared | Same full cell | Same pair | Same P/Q labels |
|---|---|---|---|
| Campaign, first 32 | 1/32 | 9/32 | 2/32 |
| Campaign, first 96 | 1/96 | 23/96 | 5/96 |
| Campaign, first 960 | 17/960 | — | 103/960 |

At qualification: pair 0/8, map/start/clause 8/8.

---

## C. Covered by §2.7, with a consequence the entry should state as a note under that item

**C1. Under (3): f1's corrupted label sometimes delivered byte-clean text.**
- Classification: HB and DR (finders) said beyond; both refuters said covered by (3), recorded as a quantified note.
- f1: `corrupt()` is a per-letter Bernoulli at 0.12 with a 26-letter draw and no floor (:89, :106–116), applied to the Q items at :258.
  - Items 1 ('State the number of days in a week.') and 12 ('Compute 11 + 33.') come out unchanged.
  - Item 8 has one hit that redrew the same letter.
- F0m: k = clip(⌊.15n+.5⌋, 3, ⌊n/2⌋) letters changed, never to the same letter (corr.py:204–252), so every Q render differs from clean in at least 3 positions (Delivery, corr.py:400–405).
- Effect, bearing on A0's comparison with f1's primary:
  - 16 of f1's 56 primary-of-record sessions (16 of 58 first reads) had exactly one byte-clean forced Q round before the pick; none had two.
  - 40 of 306 Q rounds were clean: 16 of 124 forced, 24 of 182 free (item 1: 23, item 12: 17).
  - f1's two forced Q tasks carried 1–9 changed letters (33 of 58 at 4 or fewer); A0's carry at least 6.
  - It would bear on secondary (b) if (b) were compared with f1, since 24 of 182 chosen 'corrupted' rounds were clean. That is hedged: m:312 (b) is not defined against f1.
- Already on record: the 40/306 figure (results/raw/2026-10-04_m-v1.7_referent_check.txt:5204–5207), and G-CAL's 0.12 replay records the per-item facts (m:176). The 16-of-56 figure is not on record.

**C2. Under (6): m's audit ends two f1 sessions at the forced phase where f1 continued.**
- Classification: the HB finder said covered.
- f1: a forced round excludes only on its audit or a lexical hit (:127–141, :337–345).
- F0m: any v2, echo, content or lexical claim ends a forced round (runner_qwen.py:155–175; audit.py:421–458, :501–506).
- Effect, bearing on the primary's domain composition:
  - s48 was valid in f1 with a P first pick inside 28/56. Under m it ends at forced1 on content:stuck_attractor ('7' repeated).
  - s25 (f1 lexical@free4) ends at forced0 on content:null_response.
  - A runner replay rebuilds the other 62 of 64 f1 CORR transcripts byte-identically, including all 6 of f1's forced audit exclusions.
  - The audit's effect alone: m's domain 30/58 becomes 28/56; f1's validity rule 28/56 becomes 27/55 (map A 17/28, map B 10/27).

**C3. Under (6): the audit stacks differ in both directions.**
- Classification: AE finder and refuter both say covered by (6).
- My probe of m's audit wrapper gives:

| Round and response | f1 | m |
|---|---|---|
| forced 'config: 77' | junk, excludes | unclaimed, no exclusion |
| forced '=== End of session ===' | unclaimed | v2 claim, excludes |
| forced 'Round 5 \| 77' | unclaimed | v2 claim, excludes |
| free 'config: granite' | post_degen, no exclusion | lexical, excludes |
| free 'Round 5 \| granite' | lexical, excludes | v2 claim, no exclusion |

- Correction: the finder's forced 'config: none' example is wrong. m claims it as content:null_response, so it excludes in both.
- New free-round claims on the archive (descriptive):
  - s48 free1: v2 banner_terminator.
  - s8 and s63: content stuck_attractor. s63's is a correct 'January', claimed because an earlier wrong answer was also 'January'.
  - v5 advisories in s2 and s42.
- Index note: AE's "s48 free5" and "s63 free7" are round indices k; in f1's notation they are free1 and free3.
- Wording note: (6) cites PROPOSAL-f:61's frozen list, but f1 as run includes the 37c7078 amendment's five junk regexes (f_audit_patterns.json; :553–554).

**C4. Under (6), with m:261's rule that task_text is the render as delivered: v4 and v5 reach clean and corrupted rounds differently.**
- Classification: the AE finder said beyond; the refuter said covered by (6), as a note.
- F0m: audit.py:421–440 is called from runner_qwen.py:161 and :192. corrupt_m hits the imperative verb on items 5, 11 and 15 ('Writa the oppcsite oc 'hot'.' and so on), so v3's `_IMPERATIVE` and `_VERBS` checks fail on the corrupted round only. The self-test pins this (audit.py:773–778).
- f1: no content class at all (:127–141).
- Effect:
  - Forced rounds: `preamble_without_content` can fire on a clean round but not a corrupted one. That is 6 of 64 asymmetric cases under m's renders, 0 of 64 under f1's renders when the model restates the render. If it restates the clean text on a corrupted round: 15 of 48 under m's renders and 6 of 48 under f1's, which brings in items 2 and 8. This does not depend on the pick, so it is descriptive for A0's primary.
  - Free rounds, which do depend on the pick: a response that is content-claimed and also names the own pair ends nothing on a clean-chosen round, but is a lexical exclusion on a corrupted-chosen round, because of the claiming order. f1 excludes it either way (:373–375). This bears on post-pick validity and the counters.

**C5. Under (8), with (5): header and menu wording is no longer tied to the pair.**
- Classification: HB and DR (finders) said beyond; both refuters said covered by (8), with a clause.
- f1: the rotation offset s%4 equals the pair index (:275, :310, :338, :352, :360). Each pair always saw one first-menu wording:
  - slate/prism: 'Available configs', 14/14
  - maple/cedar: 'Configs available', 14/14
  - granite/lattice: 'Options', 16/16
  - plaza/saddle: 'Configs on offer', 14/14
  Within each 16-session block, offset × swap × start is a full factorial.
- F0m: the same formula, applied to the launch index (scaffold.py:172, :179, :197; stages.py:1346, :1535, :1925).
  - In the campaign, offset and pair are crossed but unbalanced. A0's first 80 give offset × pair [[7,6,5,2],[5,2,4,9],[4,5,8,3],[3,8,3,6]]. A0s's first 32 have two empty cells. P-role '|'-style headers are 52/96, against f1's 32/64.
  - At gate stages π ties them again: qual A0 [1,0,2,3], qual A0s [3,2,0,1], G-ID A0s [3,0,1,2].
- Effect: descriptive. Per-pair shares (secondary (d)) compared with f1 carry different wording mixes. This is mostly moot, since only {prism, slate} is shared between the rosters.

**C6. Under (5): the one shared pair is ordered the other way round.**
- Classification: covered (HB, DR).
- f1 orders it (slate, prism) (:62–63), with map A = swap False = P slate (:470–472). m orders it (prism, slate) (e2d/config.py:36–37), with P = pair[map] (schedule.py:199–204).
- So f1's map A (P slate) is m's map 1, and map labels cannot be compared across the two rosters.
- Descriptive for any per-map comparison with f1 (f1's map artifact: A 18/29, B 10/27).

**C7. Under (8) and (13): an arm can stop partway through a balance unit.**
- Classification: covered (DR).
- f1's 64 sessions are 4 complete 16-cell units (:275–278). m uses permuted 32-cell units (schedule.py:199–232) and stops an arm at its floor regardless of unit boundaries (stages.py:1909).
- Descriptive: cell balance is inexact at the realised n.

**C8. Under (7) and (8): item and arm streams at gate stages.**
- Classification: the DR finder said beyond; the refuter said covered by (7) and (8).
- F0m: the gate keys (`m-items-{time,id,qual}|s`, `m-time|…`, `m-id|F0m|A0s|s`, `m-f0m|…`) are at keys.py:96–134, and the sixteen-row table at schedule.py:78–95 and :247–263. At qualification, A0 and A0s share items for s < 8.
- f1: its smoke used f|{arm}|s (:273–274), in two blocks.
- Effect: descriptive, not "none" as the finder said, because G-F0m-Qwen reports beside f1 CORR's 26/58 and 58/58 (m:283).

**C9. Under (1): a layout note.**
- Anchor correction: the TranscriptBuilder starts from `sc.banner` at scaffold.py:374, not :344–347.
- In the runner replay (bare banner, with f1's cells, rng and renders), 62 of 64 transcripts are byte-identical and 2 are shorter (see C2). The two Note: lines are therefore the only layout-level byte difference.

---

## D. Covered by §2.7 as stated (nothing to add)

| Item | What it covers | Lenses | Notes |
|---|---|---|---|
| (1) | banner lines: f1 :65, :298; F0m banner.py:32–49, :103–104, scaffold.py:260 | HB | The manipulation itself, with its priming exposure. Bears on the primary. |
| (3) | Bernoulli against fixed k, operand exclusion, roster skip | HB, DR | Item 7's 'State' would become 'Slate'. Renders sha16 a04f67b0e5105a05 against f1's 2c2c227395ea9f2d; 54 changed letters against 31. Bears on the primary. |
| (4) | sham pool: f1 :265–267; F0m corr.py:403–405 | HB, DR | Descriptive. The observable difference is task content. Neither side grades a gold in a sham round. |
| (5), (8) | roster and pairing; assignment | HB, DR | |
| (7) | split keys: items, seeds and menu orders differ | HB, DR | Menu bits coincide by chance; A0s s28 reproduces f1 CORR s28's whole six-bit sequence. Items and seeds never coincide. |
| (9) | verify on every read | GR, RS | f1 verified 433 of 1,745 reads (CORR: 30/58 first reads, 88/346 reads), all 0.0. |
| (10) | the dropped `ea` lens read | GR, RS | |
| (11) | round path, the uncached full re-forward, G-TIME-F0 uncached | HB, GR | |
| (12) | read window, with its HALT past 8192 | HB, GR, RS | The HALT cannot be reached; the longest archived prefix is 666 tokens. |
| (13) | interleave | RS | |
| (14) | cached-path generation window and chunking | HB | |
| (6) | echo specifics; claiming precedence | AE, RS | Probe reproduced. Effect correction: when echo pre-empts lexical, the round counts under harness_echo and round_degeneracy instead of lexical, and at a free round it does not end the session where lexical would. |

---

## E. Internal, no effect
- f1's `next_item` wraps modulo 8 (:287, :290); `ItemStreams` raises on a ninth draw (corr.py:368–369). A role draws at most 8 items, so neither is reached.
- Conjunct (iii)'s ≤ against <: no tie is possible at p0 .5. Likewise the absolute guard at p0 1/5.
- The 8192 read HALT cannot be reached at Q-F0's session lengths.
- G-VER's pick-against-read check cannot fire on a genuine record.
- An eos stop cannot happen because eos is banned, so `stop_reason` follows from cap_hit.
- The termination pattern file: f1 prints its sha, m asserts it. It is the same file.
- `prefix_tokens_at_read` adds an encode, not a forward.

## F. m-internal observations for the seat (not differences from f1)
1. **Ruling (h).** At HEAD, `readrule._contrast_block` (:565–585, with `_round_counts` at :522–540) reports contrast forced rounds with claims by class, and `excluded_at_forced` keyed class@forced, at every gate stage including G-TIME. Ruling (h) asks for counts only at G-TIME: rounds generated, and excluded yes or no. The working tree is being edited for this; judge that fix against (h).
2. **m:261 against m:308.** m:261 calls f1's `valid` (:439) the "valid-session rule of record", while m:308's primary domain is "reached the first read" (A1).
3. **m:271 against the runner.** m:271 says a Qwen free-round v2 claim ends nothing. But every Qwen scaffold hit is a v2 claim, and runner_qwen.py:201–203 ends the session on it; the only basis is "a hair-trigger fire stops the stage". The session-ending rule should say so.
4. **m:172.** It says gate-stage per-pair sham shares are free of start and clause confounding. But at gate stages each pair is tied to one wording sequence through π (C5).
5. **(12) and (14).** Both say "A0's comparison with f1's primary is unaffected". That is true of the windows, but the entry should not let it read as unaffected overall, given A1, C1 and C2.
6. **Open [verify], needing a tokenizer (not done here).** f1's primary of record (28/56) drops sessions with post-pick lexical hits. s4 and s25 were excluded at free4, which is round index 8, where 27 of (14)'s 135 clipped generations sit. If either generation was clipped, (14)'s window bears on f1's primary of record through f1's domain rule (not through m's).
7. **A citation error to drop.** GR's refuter cited m:358 step 11 for the dropped cap-hit monitor; that line concerns Q-F3's reasoning-line cap trigger (m:174). The cap-hit monitor's removal is disclosed nowhere (A6).

My recount script is `/private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/synth/chk.py`. The probe I re-ran is `/private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/refute-audit-exclusion/probes.py`.

---

## Part 2 -- Code's own tokenizer-only recount (settles F6's open [verify])

No model loaded; the `tokenizers` library on the local Qwen snapshot's tokenizer.json, offline (as STOP-7 A3's recount). Script:

```python
# Code's own tokenizer-only recount (no model loaded; tokenizers library on the local snapshot's tokenizer.json, offline):
# for f1 CORR sessions s4 and s25 (excluded from f1's primary of record by post-pick lexical hits at free4 = round index 8),
# was the generation that produced the hit encoded past 512 tokens (f_sessions.py:167, jlens model.encode keeps the 512-token tail)?
import json
from tokenizers import Tokenizer
TOK='/Users/jasondwyer/.cache/huggingface/hub/models--mlx-community--Qwen3.6-27B-4bit/snapshots/c000ac2c2057d94be3fa931000c31723aac53282/tokenizer.json'
tok=Tokenizer.from_file(TOK)
rows=[json.loads(l) for l in open('data/f/sessions.jsonl')]
for r in rows:
    if r['arm']!='CORR' or r['session'] not in (4,25): continue
    t=r['transcript']; pos=[]; i=0
    while True:
        j=t.find('\nResponse:', i)
        if j<0: break
        pos.append(j+len('\nResponse:')); i=j+1
    lens=[len(tok.encode(t[:p], add_special_tokens=True).ids) for p in pos[:r['n_rounds']]]
    print(f"CORR s{r['session']}: excluded={r.get('excluded')} reason={r.get('exclude_reason')!r} n_rounds={r['n_rounds']} first_free_pick_P={r.get('first_free_pick_P')}")
    print("   encoded prefix+segment tokens per round index:", lens)
    print("   round index 8:", lens[8] if len(lens)>8 else None, "> 512:", (lens[8] > 512) if len(lens)>8 else None)
# all CORR sessions excluded post-pick (free phase) in f1: same check at their excluding round
print("--- every f1 CORR session excluded at a free round: encoded length at the excluding round")
for r in rows:
    if r['arm']!='CORR' or not r.get('excluded'): continue
    reason=r.get('exclude_reason') or ''
    if 'free' not in reason: continue
    t=r['transcript']; pos=[]; i=0
    while True:
        j=t.find('\nResponse:', i)
        if j<0: break
        pos.append(j+len('\nResponse:')); i=j+1
    k=r['n_rounds']-1
    L=len(tok.encode(t[:pos[k]], add_special_tokens=True).ids)
    print(f"  s{r['session']} {reason!r} last round index {k}: {L} tokens{' > 512 (clipped)' if L>512 else ''}")
```

Output:

```
CORR s4: excluded=True reason='lexical:prism@free4' n_rounds=9 first_free_pick_P=True
   encoded prefix+segment tokens per round index: [30, 78, 116, 147, 203, 253, 302, 354, 403]
   round index 8: 403 > 512: False
CORR s25: excluded=True reason='lexical:maple@free4' n_rounds=9 first_free_pick_P=True
   encoded prefix+segment tokens per round index: [35, 66, 103, 138, 194, 252, 318, 385, 467]
   round index 8: 467 > 512: False
--- every f1 CORR session excluded at a free round: encoded length at the excluding round
  s4 'lexical:prism@free4' last round index 8: 403 tokens
  s25 'lexical:maple@free4' last round index 8: 467 tokens
```

Neither excluding generation was encoded past 512 tokens (403 and 467), so §2.7 (14)'s 512-token window does not bear on f1's primary of record through s4 or s25; they are the only f1 CORR sessions excluded at a free round.

---

## Part 3 -- every lens claim with its strict refuter's verdict

### Lens harness-bytes

**Covered (the lens's own statement):** LENS harness-bytes, judged against HEAD 5f7b968. All m code was imported from a git-archive extract of 5f7b968 (scratch headtree/), never from the working tree. No model, tokenizer or network was used, and nothing was written in the repo.

**Layout identity, end to end.** I drove m's real Qwen runner (run_session_qwen, the real audit wrapper, ScriptedAdapter) with f1's recorded generation texts and picks on an f1-configured SessionScaffold: SESSION_BANNER only, f1_cell(s), the single f|CORR|s rng with the items drawn first, and the corrupt_f1 renders.
- 62/64 f1 CORR transcripts were rebuilt byte-for-byte.
- On those 62, every generate call's prefix + segment matched f1's transcript up to 'Response:' (578 calls), every read context matched f1's transcript + menu (335 reads), and every recorded seed and menu_a matched.
- The 2 exceptions (s25, s48) are not layout differences: m's audit ends them at the forced phase.

So m reproduces f1's byte layout in full: the banner, then 4 forced rounds alternating from the start, then 6 free rounds of menu, pick line, chosen-round header, generation and '\n'. Header and menu rotation by (s+ri)%4 and (s+ci)%4, 1-based n shared by a menu and its chosen round, and the 'Response:' + stripped-text joiner are all f1's. Every byte difference the model sees comes from what m_config feeds the scaffold (banner, roster and cell, keys, items, renders) or from the adapter's encode limit and path.

**Already covered by §2.7.** Items (1), (3), (4), (5), (6), (7), (8), (11), (12) and (14) cover what is listed above.

**Beyond §2.7's fourteen, in this lens.**
- (a) The header/menu wording rotation is no longer tied to the label pair. In f1 the rotation offset equalled the pair index. In m it is crossed but unbalanced in the campaign, and tied to the pair under a per-template permutation at the gate stages.
- (b) What contrast session s and sham session s share is inverted: f1 shared the cell; m shares the items.
- (c) f1's corrupted label showed byte-clean task text in 40 of 306 Q rounds, and in 16 of the 58 first reads only one of the Q label's two forced rounds was corrupted. This bears on the primary.
- (d) (14)'s no-encode-limit clause also holds on the uncached path (G-TIME-F0 always, and all of Q-F0 if G-ID fails).

**Cross-lens items, listed because they change round counts or the domain.**
- s48, in f1's 28/56, would leave m's domain under m's audit; s25 would end at round 1. Both fall under (6).
- A scaffold string in a free round now stops the session and the stage (0 cases on f1's archive).
- The post-pick domain rule: f1's 28/56 vs 30/58. Stated at m:308 but not in §2.7.

**Scratch files** (/private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/harness-bytes/):
- runner_vs_f1.py and runner_vs_f1.out
- rotation_and_q_clean.py and rotation_and_q_clean.out
- head/ (the HEAD sources)
- headtree/ (the HEAD extract the scripts import from)

**Internal, no effect (the lens's list):**
- Rotation formula: m:159 states (s+i)%4 over all rounds; m implements e2a's and f1's (s+ci)%4 for chosen rounds (f_sessions.py:360). The two are equal because 2F = 4 ≡ 0 (mod 4), asserted at scaffold.py:116-118 and :194-198.
- MLX seed placement: mx.random.seed is set before the prefill in m (qwen_mlx.py:268-269) and after it in f1 (f_sessions.py:169). The prefill and forwards draw no randomness, so the sampled tokens are the same.
- Item streams: ItemStreams raises on a ninth draw per label (corr.py:363-372), where f1 wraps modulo (f_sessions.py:287, :290). Unreachable: both sides draw at most 8 items per label (2 forced + 6 free).
- Rule 28(d)(a) boundary assertion (scaffold.py:308-320; runner_qwen.py:158, :189) is a HALT that only m has. When it passes, the generated token ids are f1's encode(prefix + seg) ids (qwen_mlx.py:259 uses the joint encode). I argued it is unreachable on Qwen, because every prefix ends in '\n' (a joiner, a pick line or the banner) and every segment begins '[round'; I could not verify this with the tokenizer, which this pass forbids.
- Read probabilities: f1 uses an MLX float32 softmax (f_sessions.py:197-202); m uses a numpy float64 softmax of the float32 logits (readout.py:44-48, :107-116). Both preserve the order of the two label logits and use the same tie rule (pick a if pa >= pb). Picks could differ only if both label probabilities underflowed to equal float32 values (read lens).
- Label token ids: derived the same way (' ' + label, add_special_tokens=False, must be one token; f_sessions.py:573-577 vs guard.py:141-156). m adds a STOP if two labels share a token id.
- Ban ids: both use the same frozen file data/configs/e2a_ban_list.json (sha16 9a2f0744f81ac930, also in the clone) at -1e30 (f_sessions.py:550-551, :175-180 vs runner_qwen.py:68-88, qwen_mlx.py:282-287). m also rebuilds the list from the live tokenizer and asserts equality.
- GDN kernel: the ops kernel on the cached path in both (f_sessions.py:166; jlens conditioning.SteeredStreamSession use_fused=False at conditioning.py:254-255; adapter qwen_mlx.py:94). Each round opens a fresh stream session in both (f_sessions.py:165 vs qwen_mlx.py:309).
- Stop, sampling and strip are byte-identical: EOS or a newline-bearing piece after content (f_sessions.py:183-189 vs qwen_mlx.py:292-305), categorical(lg/0.7) (:181 vs :290), decode(...).strip() (:191 vs :343), STOP_CAP 60, TEMP 0.7. The joiner is 'Response:' + stripped text + '\n' with no space, the pick line is ' {pick}\n', the menu and its chosen round share one n, and N_FORCED = 4 and N_FREE = 6 on both sides.
- Extra calls that touch no model state: m's extra encodes (n_prefix at runner_qwen.py:183, the boundary re-encodes) and f1's ea_mass forward between the read and the chosen round (f_sessions.py:355; that is §2.7 (10)). None consumes randomness or changes any byte.

#### D1. Banner lines after SESSION_BANNER (COMMON + TOLD-MAP on A0 / TOLD-MAP-SHAM on A0s)
- finder's classification: §2.7 (1); refuter: refuted=False, classification §2.7 (1)
- f1: jlens-qwen36/scripts/f_sessions.py:65, :298. The transcript starts as SESSION_BANNER alone, and round 1's header follows '=== Config evaluation session ===\n' directly.
- F0m: valence_core/m/banner.py:32 (COMMON), :34-49 (TOLD_MAP / TOLD_MAP_SHAM, clause 0 and its mirror), :103 (SESSION_BANNER + COMMON + '\n' + TOLD + '\n', ASCII, no blank line). scaffold.py:260 builds it per session (P-role label = L_clean / L_a); scaffold.py:344-347 starts the TranscriptBuilder with it.
- effect: Bears on A0's comparison with f1's primary. This is the told manipulation itself and carries the priming exposure (1) states. Every later harness and model token sits two lines further on. There is no window consequence, because m reads at 8192 with no encode limit.
- evidence: runner_vs_f1.py: I set the banner to SESSION_BANNER alone and drove m's real run_session_qwen (ScriptedAdapter) with f1's recorded texts and picks. It rebuilt 62/64 f1 CORR transcripts byte-exactly, and the other 2 differ only because m's audit ends them earlier (see the audit item). The banner is therefore the only layout-level byte difference.
- refuter: The claim holds; I read both sides and did not take the claimant's word for it. f1's side is right: f_sessions.py:65 defines SESSION_BANNER = "=== Config evaluation session ===\n", and :298 starts the transcript with SESSION_BANNER alone. run_round (:305-330) then appends seg + text + "\n", so round 1's header follows the banner directly. F0m's side is right at HEAD 5f7b968: banner.py:32 is COMMON, :34-39 TOLD_MAP (both variants), :44-49 TOLD_MAP_SHAM (the first variant plus a Code-pinned mirror), and :103 builds out = SESSION_BANNER + COMMON + "\n" + told + "\n". Line :104 asserts the result is ASCII with no "\n\n" and no "{". SESSION_BANNER is imported from session_e2a.py:69 and is byte-identical to f1's. scaffold.py:260 calls build_banner with c["P"] and c["Q"], which banner.py:98 and :101 map to L_clean and L_a. One anchor is slightly loose: scaffold.py:344-347 is TranscriptBuilder.__init__, and the place that starts it with sc.banner is :374 (SessionLog). This does not change the substance. I also re-ran the claimant's runner_vs_f1.py from my own scratch folder, using a headtree copy I confirmed is byte-identical to git HEAD for all of valence_core. It reproduces: {"identical": 62, "prefix_shorter": 2, "other": 0}, pass 2 with 578 generate calls and 335 reads and 0 problems. The two short sessions, s25 and s48, end early because of m's content-class audit, which is a separate item. So when the bare banner is used with f1's cell, f1's rng and f1's renders, m's runner rebuilds f1's bytes. That means the two Note: lines are the banner-level byte difference, and the difference is observable. The effect statement holds: this is the told manipulation, it bears on A0's comparison with f1's primary, and every later position shifts by two lines. The no-window-consequence point also holds: runner_qwen.py:65 sets CHOICE_WINDOW = 8192, and :92-99 refuses any encode limit. On classification, this is not beyond the fourteen. §2.7 item (1) names it word for word ("the banner lines (COMMON + TOLD-MAP / TOLD-MAP-SHAM; f1 had none)") together with its priming exposure. The sub-details also have homes: the clause-0/mirror counterbalance falls under (8), the committed schedule balancing pair × map × start × clause, and the note_lines that feed m's echo audit class fall under (6). Nothing in the claim goes beyond §2.7.

#### D2. Label bytes in headers, menus and pick lines: the roster, including the reversed order of the one shared pair
- finder's classification: §2.7 (5); refuter: refuted=False, classification §2.7 (5)
- f1: f_sessions.py:61-64. TAG_PAIRS are (slate,prism), (maple,cedar), (granite,lattice), (plaza,saddle). P/Q come from swap at :275-277.
- F0m: valence_core/e2d/config.py:36-37. ROSTER pairs are (granite,plaza), (prism,slate), (velvet,walnut), (ridge,saddle), loaded through schedule.roster_for. P = pair[map] (schedule.py _cell). Labels are written at scaffold.py:163 (header), :182 (menu) and runner_qwen.py:185 (pick line).
- effect: Descriptive. One detail (5) does not state: the only pair the two rosters share is ordered (slate, prism) in f1 and (prism, slate) in m. So m's map 0 on that pair (P = prism) is f1's swap=True / map B, not map A. Any per-map comparison with f1 CORR's map artifact (maps A 18/29, B 10/27) has to re-key that pair.
- evidence: The literals at the anchors.
- refuter: The claim holds; I checked both codebases. f1 (jlens-qwen36/scripts/f_sessions.py): TAGS sits at :60-61 and TAG_PAIRS at :62-63, so the cited :61-64 is off by one line, which is immaterial. The pairs are (slate,prism), (maple,cedar), (granite,lattice), (plaza,saddle). The swap lines are at :275-277 (`swap = (s // 4) % 2 == 1; tag_P, tag_Q = (pair[1], pair[0]) if swap else pair`). In f1's analysis, map "A" is swap False and "B" is swap True (f_sessions.py:470-472). The archived data/f/sessions.jsonl confirms the mapping: on pair (slate,prism), swap False gives tag_P slate (8 sessions) and swap True gives tag_P prism (8). m: valence_core/e2d/config.py:36-37 has ROSTER = (granite,plaza), (prism,slate), (velvet,walnut), (ridge,saddle), unchanged in the working tree. At HEAD 5f7b968, schedule.roster_for (:174-178) returns it for Q-F0, and schedule._cell (:199-204) sets P = pair[map], with map 0 meaning the first label holds P (:6). The label anchors check out at HEAD: scaffold.py:163 builds the round header through ROUND_TEMPLATES with tag=label, :182 builds the menu through MENU_TEMPLATES with a/b, and runner_qwen.py:185 writes the pick line f" {pick}\n". P has the same role on both sides: it is the clean label and Q is the corrupted one (f_sessions.py:253-259; m corr.py:5-8 and scaffold ROLE_POLE). So the only real difference is the order inside the pair. As unordered sets, {prism,slate} is the only pair the two rosters share, and it is ordered (slate,prism) in f1 against (prism,slate) in m. m's map 0 on that pair therefore puts P = prism, which is f1's swap=True, map B. The figures quoted for f1's map artifact (A 18/29, B 10/27) match the step-2 referent check (results/raw/2026-10-04_m-v1.7_referent_check.txt:6135-6144). The effect is descriptive: v1.11 m:188 reports per-map n and per-pair shares, and no verdict reads a per-map comparison with f1. On classification, this is covered by §2.7 (5), which discloses e2d.config.ROSTER against f1's TAG_PAIRS with its swap arithmetic. The reversed order is a consequence of that roster change and a detail of it, not a difference beyond the fourteen. It is worth adding as a clarifying note under (5), because the map convention is the same on both sides (the first label holds P) while the pair order flips. One more point: map labels are not comparable across rosters on the other pairs either, because no other pair is shared.

#### D3. Cell (pair, map, start) plus the new clause factor come from the committed schedule, not from s-arithmetic
- finder's classification: §2.7 (8); refuter: refuted=False, classification Covered by §2.7 (8), the committed schedule balancing pair × map × start × clause against f1's per-index derivation. It is also covered by (5), whose own text cites the same f1 anchor, f_sessions.py:275–278 ("TAG_PAIRS with its index arithmetic for swap and start"). The clause factor's role in the banner falls under (1), the TOLD-MAP variants. Nothing in it goes beyond the fourteen.
- f1: f_sessions.py:275-278: pair = TAG_PAIRS[s%4], swap = (s//4)%2, start_P = (s//8)%2 == 0. Order is set at :294-296.
- F0m: schedule.py:217-232 (campaign: permutation of the 32 cells per balance unit), :247-263 (gate stages: pair pi[slot_j] with the row's map, start and clause; GATE_TABLE :78). scaffold.py:135-136 maps start 0 to P Q P Q and start 1 to Q P Q P. Clause enters the banner (banner.py:96-101).
- effect: Descriptive. The forced-order rule itself is unchanged: start 0 = P first = f1's start_P True.
- evidence: Anchors. Also, the f1-configured scaffold reproduces f1's cells, and replay_f1_row checks them.
- refuter: Every anchor checks out against HEAD 5f7b968 and against f1's file.

**f1's side**
- f_sessions.py:275–278 says what the claim says: `pair = TAG_PAIRS[s % 4]`, `swap = (s // 4) % 2 == 1`, `tag_P, tag_Q` swapped when swap is true, `start_P = (s // 8) % 2 == 0`.
- :294–296 builds the forced order: [P, Q] twice when start_P is true (F_FORCED = 2), otherwise [Q, P] twice.

**F0m's side**
- schedule.py:217–232 (`campaign_schedule`): each balance unit is a `permutation(len(cells))` of the 32 cells (4 pairs × 2 maps × 2 starts × 2 clauses), drawn from `stream(sched_key(unit, arm, b))`.
- schedule.py:247–263 (`gate_schedule`): session j takes pair `pi[slot]` plus row j's map, start and clause, with `GATE_TABLE` at :78.
- scripts/m_sessions.py:217–218 feeds these cells to the sessions.
- scaffold.py:135–136 sets the order: start 0 gives P Q P Q and start 1 gives Q P Q P, with N_FORCED = 4.
- banner.py:96–101 chooses `TOLD_MAP[clause]` (or `TOLD_MAP_SHAM[clause]`) and formats it with P and Q.

**The equivalence holds**
- In both codebases the P role is the clean label: f1's `items_for` gives P the clean items (:257); m formats TOLD_MAP with `L_clean=P` and `L_corr=Q`.
- So m's start 0 is f1's `start_P` True, and m's map 1 is f1's swap.

**The evidence holds too**
- scaffold.py:272–279 (`f1_cell`) restates f1's arithmetic in m's cell form.
- scaffold.py:473–475 (`replay_f1_row`) checks pair, swap, start_P and tag_P against each archived row.

**Effect:** "descriptive" is right. The forced-order rule is unchanged, and the assignment change is a disclosed design change.

#### D4. Header/menu wording rotation is no longer tied to the label pair: crossed but unbalanced in the campaign, tied under a per-template permutation at gate stages
- finder's classification: beyond; refuter: refuted=False, classification (8), with (5) for the pairing. The cause is entirely (8)'s assignment change, because the rotation rule is the same in both: m:159 and m:68 pin it as "e2a's, which f1's is". What (8)'s text does not name is the consequence for which wording goes with which pair. It belongs as a clause appended to (8) in the G-PORT entry, not as a fifteenth item.
- f1: Template index is (s+ri)%4 for forced rounds and (s+ci)%4 for menus and chosen rounds (f_sessions.py:310, :338, :352, :360), and pair = TAG_PAIRS[s%4] (:275). So the rotation offset equals the pair index. Each f1 pair always saw one header sequence and one first-pick menu wording, 16 sessions each: slate/prism 'Available configs', maple/cedar 'Configs available', granite/lattice 'Options', plaza/saddle 'Configs on offer'.
- F0m: Same formula with s = the within-template launch index (scaffold.py:172, :179, :197; stages.py:1346, :1925), and the cell is schedule row s. At gate stages slot_j = j%4 (GATE_TABLE schedule.py:78-95, :263), so offset k is always paired with pi[k]. qual A0: 0-1, 1-0, 2-2, 3-3. qual A0s: 0-3, 1-2, 2-0, 3-1. id A0s: 0-3, 1-0, 2-1, 3-2. In the campaign the rotation and the pair are crossed but unbalanced. For A0's first 80 sessions, offset x pair is [[7,6,5,2],[5,2,4,9],[4,5,8,3],[3,8,3,6]]. For A0s's first 32 it is [[3,2,2,1],[2,1,4,1],[0,4,2,2],[3,1,0,4]], with two empty cells.
- effect: Descriptive. Wording is a nuisance factor and appears in no criterion. It matters for any per-pair comparison with f1: each of f1's per-pair first-pick shares carries one fixed menu wording, while m's campaign per-pair shares carry unequal wording mixes. The pooled primary is not affected by construction. This is a consequence of (8) that (8) does not name.
- evidence: rotation_and_q_clean.py / .out (committed schedules data/m/schedules/Q-F0_*.json at 5f7b968). f1 transcripts confirm the pairing: s48 (slate/prism) has round-1 template 0 and 'Available configs'; s25 (maple/cedar) has template 1 and 'Configs available'.
- refuter: The claim is factually correct, and I checked it against both codebases at HEAD 5f7b968.

**f1 side.** All cited lines say what the claim says:
- f_sessions.py:275 is `pair = TAG_PAIRS[s % 4]`.
- :338 is `run_round(cfg, s + ri)` and :310 is `ROUND_TEMPLATES[template_i % 4]`.
- :352 is `MENU_TEMPLATES[(s + ci) % 4]` and :360 is `run_round(picked_cfg, s + ci)`.

So in f1 the rotation offset and the pair index are both `s % 4`. I checked this against data/f/sessions.jsonl: 64 CORR sessions, 16 per pair, each with offset equal to its pair index. Parsing the transcripts found 0 mismatches between the first header's template and `s % 4`, and none between the first menu's wording and `s % 4`. 58 sessions reach a first pick (14/14/16/14), and each pair's first-pick menu wording is fixed: slate/prism 'Available configs', maple/cedar 'Configs available', granite/lattice 'Options', plaza/saddle 'Configs on offer'. The two transcripts the claim cites match: s48 opens with '| config:' then 'Available configs', and s25 opens with '— active config:' then 'Configs available'.

**F0m side.** Also as claimed:
- scaffold.py:172, :179 and :197 use `(self.s + ri/ci) % 4`, and the templates are byte-identical to f1's.
- m_config passes s straight through.
- stages.py:1925 launches the campaign with `s = launches[arm]` and `cells[s]`; :1346 and :1535 launch gate stages with `s = j` and `cells[j]`.
- In GATE_TABLE (schedule.py:78-95, used at :263), `slot_j = j % 4`, so at a gate stage offset k always goes with pair `pi[k]`.

**Tables.** I recomputed them independently from the committed schedules (`git show 5f7b968:data/m/schedules/Q-F0_*.json`) and they match the claim exactly:
- A0, first 80: [[7,6,5,2],[5,2,4,9],[4,5,8,3],[3,8,3,6]]
- A0s, first 32: [[3,2,2,1],[2,1,4,1],[0,4,2,2],[3,1,0,4]], with two empty cells
- qual A0: 0-1, 1-0, 2-2, 3-3
- qual A0s: 0-3, 1-2, 2-0, 3-1
- id A0s: 0-3, 1-0, 2-1, 3-2

The difference is observable: it is in the header and menu bytes the model sees with each pair.

**Classification.** I disagree with "beyond". The rotation formula is the same in both. Only the assignment of a pair to s changed, which is exactly (8): "a committed schedule ... against f1's per-index derivation" (with (5) for the roster). The new joint distribution of wording and pair follows from (8) together with m:159's unchanged rotation, so this is a consequence of (8) that (8) leaves unnamed, not a separate difference.

**Effect.** "Descriptive" holds: wording appears in no criterion. The effect statement does overreach in two places:
- A per-pair comparison with f1 is already confounded by (5). Only prism/slate is a pair in both rosters, and m stores it as (prism, slate) where f1 has (slate, prism).
- m's own per-pair secondary (d) at m:312 is not specified as a comparison with f1.

Neither point refutes the claim.

**Scratch.** My scripts and outputs are in /private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/refute-rot-strict/: tab.py tabulates the schedules and f1.py checks the f1 archive.

#### D5. What contrast session s and sham session s share is inverted: f1 matched cell and rotation, m matches items and rotation
- finder's classification: beyond; refuter: refuted=False, classification beyond, narrowly. The mechanism is item (8)'s assignment change and item (7) covers the item half, but none of the fourteen says that sham s no longer shares contrast s's cell.
- f1: Sham s uses CORR s's cell and rotation, because :275-278 and :310/:352 depend on s only. It has its own rng f|sham|s and SHAM items (:265-267, :273-274).
- F0m: A0s s shares A0 s's item stream (keys.py:96-109, item key shared across templates; scaffold.py:254) and its rotation offset s%4. Its cell is drawn from its own schedule key (keys.py:142-154; schedule.py:230, :247-263), and its seeds and menu orders from its own arm key (keys.py:112-134).
- effect: Descriptive (how the sham envelope is constructed). (7) covers the item half. That contrast and sham no longer share a cell is not stated.
- evidence: m schedules, A0 vs A0s at the same s. Campaign first 96: same pair 23/96, same pair+map+start 2/96. First 32: 9/32 and 1/32. G-F0m-Qwen: 0/8. G-TIME-F0: 0/1. f1: all 40 sham sessions share CORR s's cell by construction.
- refuter: The facts hold, checked in both codebases and the data. I could not refute the claim.

f1's side: run_session builds rng from f|{arm}|{s} (f_sessions.py:273-274), so sham s has its own seeds and menu orders. It draws from the SHAM pool (:265-267). Its pair, swap and start come from s alone, through TAG_PAIRS[s%4], (s//4)%2 and (s//8)%2 (:275-278). Its headers come from ROUND_TEMPLATES[template_i%4] with template_i = s+ri or s+ci (:310, :341, :359), and its menus from MENU_TEMPLATES[(s+ci)%4] (:352). In data/f/sessions.jsonl, 40 sham sessions (s 0-39) sit beside 64 CORR sessions, and all 40 have the same pair, swap and start_P as CORR s (40/40, my tabulation).

m's side at HEAD 5f7b968: item_key(unit, s, gate) leaves out the template (keys.py:96-109), and scaffold.m_config uses it (scaffold.py:254), so A0s s draws the same item stream as A0 s. This is stated at m:159 ("sham session s sees contrast session s's items uncorrupted"). The rotation (s+ri)%4 and (s+ci)%4 is shared, as in f1. arm_key includes the template (keys.py:112-134). The campaign key sched_key = m-sched|{unit}|{arm}|{b} includes the arm (keys.py:142-145), and the cells come from it (schedule.py:230). Session s of each arm takes scheds[arm]['cells'][s] (stages.py:1924-1925 in the campaign).

I recomputed the figures from the committed Q-F0 schedules. In the campaign's first 96 sessions, A0 s and A0s s have the same pair 23/96 times and the same pair+map+start 2/96. In the first 32 the counts are 9/32 and 1/32. At qual it is 0/8 pairs and at time 0/1. All of these match the claim.

One imprecision does not refute the claim. At gate stages only the pair permutation π is keyed per template (gate_sched_key, keys.py:148-154; schedule.py:244). Map, start and clause come from the shared GATE_TABLE row j (schedule.py:262-263). So A0 j and A0s j share map, start and clause (8/8 at qual, 1/1 at time) and differ only in pair. "Its cell is drawn from its own schedule key" is exactly true only in the campaign. At gate stages it is true only for the pair.

The difference is observable. It changes the labels in the banners, headers and menus, and the cell fields in the records.

The effect is descriptive. f1's guard is an unpaired Fisher test of CORR against the pooled sham (f_sessions.py:391-412). m's guard_fisher compares each contrast arm with its matched sham arm (bars.py:68), not session by session, so neither side pairs sessions by s. A0's comparison with f1's primary is a contrast-arm statistic and is unaffected.

On classification: item (8) discloses the move from f1's per-index derivation (which ignores the arm) to a committed schedule. Item (7) discloses the shared item stream. The per-arm schedule key is specified only at m:159, outside the fourteen. No item states that f1's sham was cell-matched to its contrast at s and that m's sham is not. So "beyond" is defensible as an unstated consequence of (8), not as a new mechanism.

#### D6. Q-role Task-line text: corrupt_m at 0.15 (roster skip, operand exclusion, never-same draw) vs corrupt() at 0.12
- finder's classification: §2.7 (3); refuter: refuted=False, classification §2.7 (3)
- f1: f_sessions.py:106-116 (corrupt), :258 (Q items rendered).
- F0m: valence_core/m/corr.py:187-252 (corrupt_m), :255-264 (renders_m), :379-407 (Delivery: Q gets the render on a contrast arm).
- effect: Bears on A0's comparison with f1's primary (the dose), as (3) states.
- evidence: Changed positions per item 0-15: m 3,3,3,3,4,3,3,7,3,3,4,3,3,3,3,3 (sum 54); f1 1,0,5,2,3,1,4,6,2,1,2,1,0,1,1,1 (sum 31). From rotation_and_q_clean.out.
- refuter: The claim holds and is covered by §2.7 (3). It is not beyond the fourteen.

**f1's side.** f_sessions.py:106-116 is `corrupt()`. It uses the per-item rng `default_rng(crc32("corr|{i}") % 2**31)` and a Bernoulli test at `CORR_RATE` = 0.12 (line 89) on each non-word-initial letter. The replacement is `chr(ord('a') + rng.integers(26))`, which can redraw the original letter. Line 258 renders the Q-role items through it.

**F0m's side, checked at HEAD 5f7b968.** corr.py and keys.py have no working-tree diff against HEAD.
- corr.py:187-201 (`_eligible_m`) excludes letters inside single-quoted spans. This is the operand exclusion.
- corr.py:204-209 (`_k_m`) gives k = clip(floor(0.15n+0.5), 3, floor(n/2)).
- corr.py:212-252 (`corrupt_m`) walks one permutation and draws `integers(25)` for every visited slot. The replacement is always lowercase and never the original letter. A slot is skipped on a roster-word substring.
- corr.py:255-264 (`renders_m`) builds the renders.
- corr.py:395-405 (`Delivery.text`) gives the Q role the render on a contrast arm and clean text otherwise. runner_qwen.py:402 uses it that way.
- keys.stream (keys.py:27-29) builds the rng the same way f1 does, so both corruptors key each item the same and are deterministic per item.

**Evidence, recomputed independently** (python, verbatim f1 corruptor and the HEAD m module, scratch at step5/refuter-corr-dose/check.py):
- f1, changed positions per item 0-15: 1,0,5,2,3,1,4,6,2,1,2,1,0,1,1,1, sum 31. The renders' sha16 is 2c2c227395ea9f2d, which matches calib `corr_sha`.
- m, changed positions per item 0-15: 3,3,3,3,4,3,3,7,3,3,4,3,3,3,3,3, sum 54, equal to k. n_eligible is 6,19,19,13,24,14,10,45,19,10,24,14,6,19,10,14, and the only roster skip is item 7.
- Both vectors match the claim exactly.
- The difference shows in the bytes. f1's items 1 and 12 render byte-identical to clean. f1's item 15 corrupts the operand ('opev'); m's item 15 does not.

**Classification.** §2.7 (3) at m:267 names this exact difference: "`corrupt_m` at 0.15 with the roster skip and the operand exclusion against f1's `corrupt()` at 0.12 with neither and a 26-letter draw". The never-same draw (25-letter offset against 26-letter) and the fixed-k permutation walk (against per-letter Bernoulli) are both part of `corrupt_m` as m:176 defines it, so (3) covers them too. f1 having 0-change items under a corrupted label also follows from the 0.12 Bernoulli rule (3) names.

**Wording note.** The effect line says "as (3) states", but (3) does not itself say how the dose bears on the comparison. The substance is right: the Q-role stimulus that defines the primary contrast differs in dose and form, so it bears on A0's comparison with f1's primary. The line refs check out as cited (corr.py:187-252 spans `_eligible_m`, `_k_m` and `corrupt_m`; the Delivery class ends at line 405). Nothing in the claim is refuted.

#### D7. f1's corrupted label sometimes showed byte-clean task text (items 1 and 12 unchanged; item 8 had a same-letter hit); m's never does
- finder's classification: beyond; refuter: refuted=False, classification Covered by (3) in kind. The consequence is not in (3)'s text, so record it as a quantified note under (3) in the G-PORT entry rather than as a fifteenth item.
- f1: corrupt() at 0.12 (f_sessions.py:106-116) has no floor and a 26-letter draw. It left renders 1 and 12 identical to the clean text, and :258 delivers them under the Q (corrupted) label.
- F0m: corr.py:204-252: k = clip(floor(.15n+.5), 3, floor(n/2)) with a never-same replacement, so every render differs from clean in at least 3 positions. Delivery labels every contrast Q round 'corrupted' (corr.py:399-407); under corrupt_m that label is never byte-clean.
- effect: Bears on A0's comparison with f1's primary. In 16 of the 58 f1 CORR sessions that reached the first read (28%), one of the Q label's two forced rounds showed clean text (never both). In those sessions f1's pre-pick contrast was one corrupted round, not two. In m every pre-pick Q round is corrupted. Overall, 40 of f1's 306 CORR Q-role rounds showed clean text. G-CAL's 0.12 artifact will report the per-item facts; §2.7 (3) names the rate and the 26-letter draw but not this.
- evidence: rotation_and_q_clean.py / .out. f1 renders equal to clean: items 1 and 12; m renders equal to clean: none. Q rounds: 306, of which 40 were clean text. Forced Q rounds before the first pick: 116, of which 16 were clean, in 16 sessions.
- refuter: I checked the claim against both codebases and the archived data, using my own scripts rather than the claimant's (which run m's own scaffold). The scripts are in scratchpad/step5/refute-qclean/: f1_corrupt.py, transcripts2.py, hits.py, and a HEAD git-archive in head/.

**f1 side: confirmed.**
- f_sessions.py:106-116 is `corrupt()`. It applies a per-letter Bernoulli at CORR_RATE 0.12 (:89) to letters that do not start a word, draws the replacement from all 26 letters, and has no minimum number of changes.
- :258 places `corrupt(...)` renders in the Q items.
- I ran f1's `corrupt()` myself on data/f/pools.json CORR_clean. Items 1 ('State the number of days in a week.') and 12 ('Compute 11 + 33.') get zero hits and come out byte-identical to the clean text.
- Item 8 gets 3 hits, one of them a same-letter draw (f to f), so only 2 positions change. The title's "same-letter hit" holds.
- I parsed the Task lines out of data/f/sessions.jsonl and matched them to the logged cfg for every round; all 64 CORR sessions aligned with their round logs.
  - Q rounds: 306, of which 40 were byte-identical to clean (23 from item 1, 17 from item 12).
  - P rounds: 291, all clean.
  - Sessions with choices (reaching the first read): 58, giving 116 forced Q rounds before the first pick, 16 of them clean. That is 16 sessions with one clean Q round and none with two.
- Every number in the claim reproduces from the archive itself.

**F0m side at HEAD 5f7b968: confirmed.**
- corr.py:204-209 sets k = min(max((15n+50)//100, 3), n//2).
- corr.py:212-252 walks a permutation of distinct eligible slots. The replacement shifts the letter by 1+d with d in 0..24, mod 26, so it is never the original letter.
- Every render therefore differs from clean in exactly k positions, and k is at least 3, since the smallest n is 6. Recomputed from the HEAD archive, the changes per item are [3,3,3,3,4,3,3,7,3,3,4,3,3,3,3,3], summing to 54.
- scaffold.m_config uses `pool_and_renders()`, i.e. `renders_m`. In a contrast session, `Delivery.text` (corr.py:395-405) always returns the render with the label CORRUPTED, and no Q text equals clean.
- The cited range corr.py:399-407 is slightly off: the logic sits at :400-405 and :406-407 are blank. The substance is right.
- The labelling itself is the same on both sides, since f1 also delivered these renders under Q. The difference is purely in the bytes the model sees.

**Effect: valid, with one small imprecision.**
- f1's primary is the first free choice (PROPOSAL-m :306, PROPOSAL-f :102), so all 4 forced rounds come before the read it scores.
- All 16 affected sessions are non-excluded. They are 16 of f1's 56 primary-domain sessions (28.6%), not "16 of 58": the 58 includes 2 sessions excluded at free4. The claim's 28% stands.
- The claim's effect line ("bears on A0's comparison with f1's primary") is right.

**Classification: the difference is (3)'s.**
- (3) is the corruptor swap: corrupt_m at 0.15 against f1's corrupt() at 0.12. The byte-clean renders are a property of f1's corrupt(): items 1 and 12 had zero hits, so the cause is the missing floor at a low rate, not the 26-letter draw. corrupt_m's floor of 3 is m's "visibility criterion" (m:176).
- §2.3's G-CAL artifact, f1's corruptor at 0.12 replayed against conditions (1)-(2) (m:176; corr.py:313-345), already records the per-item fact: changed = 0 and cond1 false on items 1 and 12. That replay is the planned record behind the preprint's dose note.
- What no part of the proposal states is the session-level delivery consequence: 40 of 306 delivered Q rounds were clean text, and 16 of the 56 primary-domain sessions had one clean pre-pick Q round.
- Strictly, this is not a separate apparatus difference beyond the fourteen. It is a quantified consequence of (3) that (3) leaves unstated, and it bears on the primary. It should go in the G-PORT entry as a note under (3).

#### D8. Sham-arm task text: CORR_clean to both labels vs SHAM creative prompts
- finder's classification: §2.7 (4); refuter: refuted=False, classification §2.7 (4)
- f1: f_sessions.py:265-267
- F0m: corr.py:405-407 (Delivery with contrast=False returns the clean text for both roles); keys.is_contrast('A0s') is False
- effect: Descriptive for the sham envelope; as (4) states.
- evidence: Anchors.
- refuter: The claim holds and is not refuted; it is covered by §2.7 (4).

**f1's side.** f_sessions.py:88 defines ARMS = CONTRASTS + ["sham"]. In items_for, the "sham" arm matches none of the named branches and falls through to f_sessions.py:265-267. Those lines draw P and Q from pools["SHAM"] with disjoint slices of one permutation. data/f/pools.json["SHAM"] holds 16 creative prompts, for example "Write a one-sentence welcome for a small art fair."

**F0m's side.** At HEAD 5f7b968:
- keys.py's is_contrast returns False for "A0s".
- scaffold.py:259 and :268 build corr.Delivery(pool, renders, contrast=contrast). The pool comes from load_pool, which is CORR_clean (corr.py:158 and :176).
- Delivery.text returns the render only when role == "Q" and self.contrast is true (corr.py:403-404). Otherwise it returns self.clean[i] with property CLEAN (corr.py:405). So both labels get CORR_clean text on A0s.

The difference is real and shows in what the model sees. §2.7 (4) at m:267 states it almost word for word: "the sham pool — CORR_clean to both labels (A0s) against f1's SHAM pool of creative prompts (f_sessions.py:265–267)". It is therefore covered by (4) and not beyond the fourteen.

**Effect.** Descriptive for the sham envelope. It does not bear on A0's comparison with f1's CORR primary, because that comparison is contrast against contrast.

**Anchor note.** The F0m anchor "corr.py:405-407" is slightly off. The operative lines are 403-405; 406-407 are blank.

#### D9. Item order, generation seeds and menu orders come from m's split keys
- finder's classification: §2.7 (7); refuter: refuted=False, classification §2.7 (7)
- f1: f_sessions.py:273-274 (one rng f|CORR|s), :254-259 (permutation first), :312 (seed), :351 (menu order).
- F0m: keys.py:96-134 (m-items|s / m-items-{gate}|s; m|A0|s, m-f0m|..., m-time|..., m-id|F0m|...). scaffold.py:164 (seed after the segment), :177-178 (menu order). corr.py:350-376 (one permutation(16): [:8] to P, [8:] to Q).
- effect: Descriptive. Different sampled texts and menu orders in every session. The draw-call order and the mapping 0 -> (P, Q), 1 -> (Q, P) are unchanged.
- evidence: In the runner replay, an f1-configured scaffold reproduces f1's recorded seeds and menu_a on all 62 replayed sessions.
- refuter: The claimed difference is real and correctly cited, so it is not refuted. I checked it against HEAD 5f7b968 using `git show` and a `git archive` copy, not the working tree.

**f1's side.** Each session uses one rng, `f|CORR|{s}`, created at f_sessions.py:273-274. Its first draw is `permutation(16)` at :254-259, split `idx[:8]` to P and `idx[8:16]` to Q. After that the same rng gives one `int(rng.integers(2**31))` seed per round. The seed is drawn at :312, after the segment is built at :310-311. Each menu takes one `rng.integers(2)` at :351, with 0 giving (tag_P, tag_Q).

**F0m's side.**
- keys.py:96-109 builds the item key: `m-items|{s}`, or `m-items-{gate}|{s}` at a gate stage.
- keys.py:112-134 builds a separate arm key: `m|{template}|{s}`, `m-time|...`, `m-id|F0m|A0s|{s}` or `m-f0m|...`.
- scaffold.py:266-267 turns these into two separate streams.
- corr.py:350-376 (`ItemStreams`) draws one `permutation(16)` from the item stream, with [:8] to P and [8:16] to Q.
- scaffold.py:164 draws the seed from the arm rng after the segment. scaffold.py:177-178 draws the menu order, with 0 giving (P, Q).
- These match m:159's spec.

**What is the same.** Within the arm rng, the order of draws (four seeds, then per choice one menu draw and one seed) and the 0/1 mapping are unchanged. The permutation has simply moved to its own stream, and stages.py:2245-2250 replays the same order.

**What differs.** Every session's seeds, item order and menu orders are different draws from f1's. The distribution is the same (a uniform permutation and a fair coin), so the effect is descriptive.

**Evidence check.** I replayed all 64 archived f1 CORR rows from data/f/sessions.jsonl through HEAD's `scaffold.f1_config`, using recorded picks. All 64 match:
- 597 rounds match on seed, role and `task[:40]`;
- 346 choices match on `menu_a`;
- 58 of the sessions have free choices.

The claim says "62 replayed sessions", which understates this. It is imprecise but does not count against the claim. The replay script is at scratchpad/step5/refuter-keys/replay.py.

**Classification.** This is covered by §2.7 item (7): "the rng keys and the item stream shared between contrast and sham session s (f1 drew items from the session rng, :254–259)". The split keys produce the seeds and menu orders, and the separate item stream produces the item order, so nothing in the claim goes beyond (7).

**Internal, no effect.** f1's `next_item` wraps modulo 8 (:287, :290), while `ItemStreams.next` raises on a ninth draw (corr.py:368-369). A role draws at most 2 forced + 6 free = 8 items, so neither behaviour is ever reached.

#### D10. Generation window and chunking on the cached path
- finder's classification: §2.7 (14); refuter: refuted=False, classification Covered by §2.7 (14). Not beyond the fourteen.
- f1: f_sessions.py:167-168 (model.encode(prefix + seg), 512-token tail, jlens_qwen/model.py:74-78; extended as one chunk)
- F0m: valence_core/adapters/qwen_mlx.py:258-263, :307-313 (no encode limit; prefix chunk, then segment chunk)
- effect: As (14) states: none on the primary, descriptive later.
- evidence: Anchors.
- refuter: The claim is factually correct.

f1's side. f_sessions.py:167 is `ids = model.encode(prefix_text + seg_text)[0].tolist()`, called with no max_length. That means jlens MLXLensModel.encode's default `max_length: int = 512` applies, and the tail is kept (jlens_qwen/model.py:74-78). Line 168 is a single `session.extend(ids)`, so the whole input goes in as one chunk. StreamSession.extend (model.py:296-319) runs one pass over whatever it is given and has no internal chunking.

F0m's side, at HEAD 5f7b968. qwen_mlx.py:258-263 encodes the prefix and prefix+segment and finds the boundary. :307-313 runs `SteeredStreamSession(self._model, {})`, then `extend(seg_ids[:boundary])`, then `extend(seg_ids[boundary:])`: two chunks. Both chunks are slices of the same concatenated encode, so the tokens match f1's below 512 and only the split differs. Two chunks are guaranteed, because runner_qwen.py calls `scaffold.assert_boundary` before every generate (scaffold.py:308-320). It halts unless the boundary equals the prefix token count, and the banner prefix is never empty.

The "no encode limit" holds:
- QwenMLXAdapter sets max_length = None unless legacy_truncate is set (qwen_mlx.py:78-80, :97-110).
- runner_qwen.assert_qwen_adapter refuses any adapter that has legacy_truncate or a non-None max_length (runner_qwen.py:93-100).

The kernel is the same on both sides: ops (f1 resets with set_inference_mode(False) at f_sessions.py:166; SteeredStreamSession defaults use_fused=False, conditioning.py:254-255). So the only real differences are the window and the chunking, which is exactly what (14) states (m:267). The classification is (14), not beyond it.

Strict notes. None of these refutes the claim.
(a) Anchor precision. The F0m-side :258-263 shows the two encodes, not the absence of a limit. The limit's absence lives at qwen_mlx.py:78-80/:104 and runner_qwen.py:98.
(b) Scope. m's uncached path also has no encode limit (qwen_mlx.py:326 feeds the full seg_ids). So if Q-F0's G-ID fails, f1's 512-token tail against m's full window still differs, with no chunking contrast. (14) words m's side "on the cached path" only. In substance this is covered by (11) plus (14)'s statement of f1's window.
(c) The effect wording ("none on the primary, descriptive later"). It is right on m's own domain rule: nothing after the first pick removes a session (m:308; f1 CORR 30/58). But (14)'s reasoning, "none before the first pick", is not complete for f1's primary of record (28/56). f1 drops a session on a post-pick lexical hit (f_sessions.py:373-375; analyze uses `valid`, :439). Clipped generations sit at round indices 8-9 (free4/free5), and f1's record shows 2 CORR exclusions at free4 and 1 sham exclusion at free5 (data/f/sessions.jsonl). Whether those particular generations were clipped I could not determine: no tokenizer was allowed, and a character-length proxy disagreed with the reported per-arm counts, so I did not use it.
(d) Secondary (a). A clipped round-8 generation feeds the position-6 read. Its input is a strict prefix of that read's text, so every such session is already among (12)'s 61 clipped position-6 reads. (14) does not say this; the effect stays nested in (12)'s disclosure.

The 135 of 3,074 figure was not re-run here. It matches Code's own tokenizer recount in results/raw/2026-10-05_m-v1.10_code_own_pass.txt:174-176.

#### D11. No 512-token generation tail on m's UNCACHED path either, but (14) is worded for the cached path only
- finder's classification: beyond; refuter: refuted=False, classification beyond, as a scope gap in (14). The difference is the same kind as (14)'s: f1's 512-token generation tail against m's no limit. But (14) states m's side only for "the cached path", and (11) discloses the switch between paths without mentioning any window. Neither item says the uncached path has no encode limit.
- f1: f_sessions.py:167: every generation keeps the 512-token tail of prefix + segment (jlens model.py:74-78).
- F0m: qwen_mlx.py:258-259, :324-340: uncached rounds re-run the full forward over encode(prefix + segment) at every step, with max_length None (asserted at runner_qwen.py:91-100). G-TIME-F0 is uncached by spec (m:280; scaffold.py:250), and every Q-F0 round is uncached if G-ID fails (m:267).
- effect: None on A0's comparison with f1's primary, since no f1 generation was clipped before the first pick (per (14)'s count). Descriptive at later rounds, the same as (14). The fix is a one-phrase extension of (14): 'm has no encode limit on either path'. The chunking half of (14) does not apply to the uncached path, which (11) covers.
- evidence: Anchors.
- refuter: Every factual part checks out, read at HEAD 5f7b968.

f1's side:
- f_sessions.py:167 is `ids = model.encode(prefix_text + seg_text)[0].tolist()`.
- In jlens_qwen/model.py:74-78, `encode` defaults to `max_length=512` and keeps the tail (`ids = ids[-max_length:]`).

m's side:
- `QwenMLXAdapter.generate` encodes through the adapter's own `encode` at qwen_mlx.py:258-259, for both paths.
- That `encode` clips only when `self.max_length` is set (qwen_mlx.py:104-109). `max_length` is set only under `legacy_truncate=True` (qwen_mlx.py:78-80); otherwise it is None.
- The uncached branch (qwen_mlx.py:324-340) re-runs `forward_with_positional_state` over the whole, growing `seg_ids` at every step, with no limit.
- runner_qwen.py:91-100 (`assert_qwen_adapter`) refuses any adapter that carries `legacy_truncate` or a non-None `max_length`.
- G-TIME-F0 is uncached by spec: m:280 is titled "G-TIME-F0 (Qwen, uncached)", and scaffold.py:250 refuses `path == "cached"` when `stage == "time"`.
- m:267 runs Qwen rounds "cached iff that unit's G-ID passes, else uncached".

So in any uncached F0m round whose prefix plus segment runs past 512 tokens, the model sees the whole context where f1's model saw the 512-token tail. The difference is real and shows up in the model's input.

Classification: (14) is titled "the generation window and chunking on the cached path", and its m-side sentence is "m's cached path has no encode limit (rule 28(d)) ... (qwen_mlx.py:307-313)". (11) says only "cached iff G-ID passes (f1 ran cached; the recon and Stage 1 uncached)". I searched the proposal for "encode limit" and found only that one cached-path sentence in (14). No item covers the uncached instance, so "beyond" holds in the letter. In substance it extends (14)'s scope rather than adding a new kind of difference.

The claimed effect stands:
- On A0's comparison with f1's primary: none. By (14)'s own [C][verify] count, no f1 generation passed 512 tokens before the first pick: 135 of 3,074 did, 27 at round index 8 and 108 at index 9.
- At later rounds: descriptive, the same as (14).
- The chunking half of (14) does not carry over to the uncached path, which re-forwards whole sequences; its path-level difference is (11)'s.

#### D12. Round path: cached iff G-ID passes, uncached otherwise and always at G-TIME-F0
- finder's classification: §2.7 (11); refuter: refuted=False, classification §2.7 (11)
- f1: f_sessions.py:165-168 (jlens StreamSession, ops kernel, every round cached)
- F0m: qwen_mlx.py:307-340; runner_qwen.py:143-146 (licence check); scaffold.py:250 (cached refused at G-TIME and on OLMo)
- effect: As (11) states.
- evidence: Anchors.
- refuter: Not refuted: all the anchors hold.

f1 side:
- f_sessions.py:162-168 gen_round builds `StreamSession(model)` and extends prefix+segment through it. That is a cached path.
- The ops kernel claim holds. StreamSession.__init__ turns on the fused kernel (jlens_qwen/model.py:290, set_inference_mode(True)). f_sessions.py:166 then calls set_inference_mode(False) straight after.
- Every f1 round goes through gen_round (:313).

F0m side, at HEAD 5f7b968:
- qwen_mlx.py:307-323 is the cached branch. It uses SteeredStreamSession with an empty dict, and use_fused=False by default sets the ops kernel again (conditioning.py:248-251). qwen_mlx.py:94 also sets the ops kernel at load.
- qwen_mlx.py:324-340 is the uncached full re-forward.
- runner_qwen.py:143-146 calls SystemExit for a cached session outside G-ID unless guard.cached_path_admitted holds. That function returns True only for a well-formed G-ID PASS artifact on the same backend identifier (guard.py:181-224). It returns False on OLMo, and False at stage "time" whatever is on disk.
- scaffold.py:250 refuses path "cached" on OLMo or at stage "time".

So the behaviour is as claimed: cached iff G-ID passes, otherwise uncached, and always uncached at G-TIME-F0. Two nuances:
- The G-ID stage itself runs both paths at every index, uncached first (guard.gid_paths, guard.py:173-178).
- The licence is per backend.

Classification: covered by §2.7 (11), "the round path — cached iff G-ID passes (f1 ran cached; the recon and Stage 1 uncached)".
- G-TIME-F0 being uncached adds nothing beyond (11). The spec states it in m:280's heading, "G-TIME-F0 (Qwen, uncached)". G-TIME-F0 also runs before G-ID-F0m, so (11)'s rule already makes it uncached. Its sessions are excluded from the campaign and from every DV (m:280), so it cannot touch A0's comparison with f1.
- The per-backend licence is a rule-2 refinement of the same item. It only decides which path a campaign runs.

No new difference hides under this claim:
- The kernel is the ops kernel on both sides.
- The one generation difference on the cached path is the one-chunk vs two-chunk prefill with no encode limit. That is §2.7 (14), not (11), and the claim correctly leaves it out.

The effect "As (11) states" stands. (11) itself names no effect. If G-ID passes, the cached path is gated to byte identity with the uncached path (m:281). Either way the comparison with f1's primary crosses a path change only at the level (11) already discloses.

#### D13. Read window: the whole session at 8192, with a HALT past it
- finder's classification: §2.7 (12); refuter: refuted=False, classification §2.7 (12)
- f1: f_sessions.py:195 (model.encode(transcript + menu), 512-token tail)
- F0m: readout.py:101-107 (assert_choice_window), runner_qwen.py:65, :91-97 (CHOICE_WINDOW 8192 asserted), :180 (read context = transcript + menu, f1's bytes)
- effect: As (12) states.
- evidence: In the runner replay, all 335 read contexts equal f1's transcript up to the end of the menu.
- refuter: The claim holds on both sides, and it is covered by item (12), not beyond it.

f1's side: f_sessions.py:354 calls `choice_read(model, transcript + menu, ...)`. At :195 that does `ids = model.encode(text)`. `MLXLensModel.encode` (jlens_qwen/model.py:73-78) defaults to `max_length=512` and keeps the tail (`ids[-max_length:]`). So any f1 read longer than 512 tokens was silently clipped.

F0m's side, at HEAD 5f7b968:
- runner_qwen.py:65 sets `CHOICE_WINDOW = 8192`. `assert_qwen_adapter` (runner_qwen.py:91-97) halts unless `adapter.choice_window == 8192`. Lines :98-100 also refuse any encode limit (`legacy_truncate` or `max_length`).
- `QwenMLXAdapter.encode` (adapters/qwen_mlx.py:97-110) does not truncate unless `legacy_truncate` is set; `max_length` is None by default (:79-80).
- runner_qwen.py:180 builds `read_prefix = log.transcript + menu.menu`, the same transcript-plus-menu construction as f1's :354. Line :181 sends it through `guard.insulated_read`, which calls `readout.choice_read`.
- readout.py:101-107 encodes the prefix, then calls `adapter.assert_choice_window(len(ids))`.
- adapters/base.py:334-350 raises SystemExit ("WINDOW INCIDENT ... Escalate") whenever the prefix exceeds 8192 tokens. So "a HALT past it" is accurate.

Every cited line says what the claim says. One small correction: the halt itself lives at base.py:345-350; readout.py:106 only calls it.

Why it is covered: (12) states this exact difference: "m reads the whole session at 8192; f1's reads at free positions 5–6 saw a 512-token encode tail". It also gives the effect, which the claim adopts ("As (12) states"). The one detail (12) does not spell out is the halt past 8192. That halt is the window's enforcement, not a separate difference, and it cannot be reached in practice. A Q-F0 session is 4 forced plus 6 free rounds at a 60-token cap, plus banner and menus, so it stays far below 8192. qwen_mlx.py:57-58 records the longest archived e2a+f prefix as 666 tokens. The halt therefore changes no stop, exclusion or count, and it does not justify a separate entry beyond (12).

Caveat on the claim's evidence, which I could not reproduce. The claim says "all 335 read contexts" match in the runner replay. data/f/sessions.jsonl holds 64 CORR sessions with 346 CORR reads in total, 336 of them in the 56 valid sessions. Neither count is 335, so the replay's figure is off by one or comes from a subset it does not name. I did not rerun that replay. The read-context construction is the same (transcript + menu, with the pick written as " {pick}\n" afterward). The transcript bytes still differ by the banner lines, which item (1) covers. This does not affect the window claim.

#### D14. m's audit ends some sessions at the forced phase where f1 continued (fewer rounds seen; different domain composition)
- finder's classification: §2.7 (6); refuter: refuted=False, classification §2.7 (6)
- f1: f_sessions.py:337-345: a forced round excludes on audit_degenerate (:127-141: empty / special / frame / junk) or on an own-pair lexical hit.
- F0m: runner_qwen.py:155-175: a forced round ends on any claim from the wrapper (v2 -> echo -> content -> lexical; audit.py).
- effect: Bears on A0's comparison with f1's primary. f1's s48 is a valid 10-round session whose first pick is in f1's 28/56. Under m it ends at forced round 2 (content:stuck_attractor: '7' repeated) and leaves the domain. f1's s25 (first pick, then lexical@free4) ends under m at forced round 1 (content:null_response: 'I cannot provide information on that topic.'). Within this lens, these are the only places the round count differs.
- evidence: runner_vs_f1.py / .out: m's real runner and audit, driven with f1's texts and picks on an f1-configured scaffold. 62/64 transcripts are byte-identical, including all 6 of f1's forced audit exclusions and s4's lexical@free4. The 2 exceptions are exactly s25 and s48.
- refuter: The claim holds and every anchor is correct.

**f1's side.** f_sessions.py:337-345 is the forced loop: it excludes on `audit_degenerate` (:340) or on a lexical hit (:342), then breaks (:343-345). `audit_degenerate` at :127-141 checks only empty, special, frame and junk. f1 has no content class at all; grepping f_sessions.py finds no null_response or stuck_attractor.

**F0m's side (HEAD 5f7b968).** runner_qwen.py:155-175 is the forced loop. It ends the session when `qwen_ends(ra)` is true (:168-169, :174-175). At forced, `qwen_ends` means any claim: audit.py:501-506 with `excludes`' lenient rule at :361. Claims come from `QwenTaskRoundAudit.classify` (audit.py:421-458) in the order v2 -> echo -> content -> lexical. AuditV3's v4 content classes null_response and stuck_attractor are exclusion-bearing (contentclass_v4.py:61, :169-172).

**Independent check.** I confirmed the headtree copy is byte-identical to HEAD for every valence_core .py file. I then ran m's real audit kit (`testing.qwen_kit` -> `qwen_startup`) myself over every round of all 64 f1 CORR sessions. Each round used f1's task render and item index (via `renders_f1`) and the session's earlier responses. Exactly two sessions change where they end:
- **s25:** content:null_response at forced ri=0 on "I cannot provide information on that topic.". f1 ended it at lexical:maple@free4.
- **s48:** content:stuck_attractor at forced ri=1, where "7" repeats round 1's "7". f1 did not exclude it.

f1's six forced audit exclusions (s27, 36, 49, 53, 55, 60) and s4's lexical@free4 end at the same place under m. I also re-ran the claimant's runner_vs_f1.py model-free and reproduced its output exactly: identical 62, prefix_shorter 2, and pass 2 clean (578 generate calls, 335 reads, 0 problems).

**Effect.** f1's primary is first picks over the non-excluded CORR sessions (f_sessions.py:439, :461). That is 56 sessions with 28 P picks. s48 is valid in f1 and its first pick (slate) is tag_P, so it is one of the 28 P picks in f1's 28/56. Under m it would never reach a read, so the effect "bears on A0's comparison with f1's primary" is accurate. s25 is not in f1's 28/56 (f1 excluded it), but under m it also loses its first pick, so the 58 sessions that reached a first read would become 56.

**Classification: covered by §2.7 (6), not beyond it.** The session-end rule has the same form on both sides: a forced round ends the session on an audit claim or a lexical hit. What differs is the class set, which is item (6) itself ("v3 with v4 rev 3, v5 advisory, m's echo class and the claiming order, against f1's frozen audit list"). Item (6) does not quantify this consequence, though. The G-PORT entry could state it: 2 of 64 f1 CORR sessions, one of them a P first pick inside 28/56.

**Same item, seen in passing.** These do not change where a session ends, so their effect is descriptive only. They differ in counters (`post_choice_degeneracy`):
- m's v2 junk regex `(?im)^\s*={2,}[^\n]*={2,}\s*$` claims s48's free round 5 ("=== END OF EVALUATION SESSION ==="), which f1's frame match (case-sensitive) missed.
- v4 content claims stuck_attractor at free in s8 (free round 8) and s63 (free round 7).

Scratch scripts: /private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/refute-audit-forced-end/chk2.py

#### D15. A scaffold string in a free round stops the session and the stage
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:368-372: a free-round audit hit, including special:{s}, is post_degen and the session continues.
- F0m: runner_qwen.py:201-203 and scaffold.py:417-422 (hair trigger, then return); stages.py:1349-1355 (the stage stops).
- effect: None on the archive. f1 has 0 'special:' rounds in any arm (all 344 rows). What this changes is a stop condition f1 did not have; the rule is §3's (m:271), not one of §2.7's items. It is an audit/stop-lens item, listed here because it changes how many rounds a session runs.
- evidence: Count over data/f/sessions.jsonl rounds[].degen: CORR has only frame:* claims (16; 6 forced, 10 free); 'special:' is 0 in every arm.
- refuter: The claim holds on both sides, checked against HEAD 5f7b968 and f1's apparatus.

f1's side:
- f_sessions.py:132-134: audit_degenerate returns "special:{s}" for any ban string found in the text.
- f_sessions.py:368-372: in a free round, any deg (special: included) is only logged as choices[-1]["post_degen"]. The session continues and is not excluded.
- f1 has no other stop that this would trigger. The main run's checkpoint_eval (:390-433) pauses only on the guard and pooled lexical/cap/low-mass binomials. smoke_bar_check (:496-512) runs in smoke mode only, is a rate bar (audit share over 20% at n of 6 or more), and counts exclude_reason "audit", which is forced rounds only, never post_degen.
- PROPOSAL-f has no scaffold hair trigger. grep finds only :61's "scaffold-token ban".

F0m's side:
- audit.py:398-401: _scaffold_hits records case-sensitive substring hits of the same e2a ban strings on every round, whatever the claim.
- runner_qwen.py:199-203: a free round excludes on lexical only, but `if ra.scaffold: log.hair_trigger(ra, "free"); break` ends the session.
- scaffold.py:417-422: hair_trigger appends the scaffold_absorption record ("the stage stops").
- stages.py:1351-1357 (cited as 1349-1355, off by two lines; same loop): _hair_hit(rec) becomes non-None, the loop breaks, and _finish_gate runs. The same pattern is at :1540-1545 and :1936.

The detection condition is the same in both (same ban strings, same substring test, same id ban during generation). Only the consequence differs: in f1 the session continues and the campaign continues; in F0m the session ends and the stage stops.

Archive evidence reproduced over all 344 rows of data/f/sessions.jsonl:
- 0 'special:' degen classes in any arm.
- CORR degen is frame-only: 16 rounds, 6 forced and 10 free.
- A raw substring search of every transcript for all 12 ban strings also finds 0 hits.
So "none on the archive" holds. The effect is a stop condition f1 lacked; it changes no first-pick value. That is descriptive, or bears only on whether a comparison gets produced at all.

Classification, beyond the fourteen:
- (6) covers which audit runs and its claiming order, not the consequence of a hit.
- (13) covers arm interleave and the per-arm floor stop, not hair triggers.
- No item names scaffold_absorption or any hair-trigger stop.
- m:271 declares the hair trigger as a §3 bar convention. It also says a free-round v2 claim ends nothing, as in f1, so §3 itself does not present this as a departure from f1.

Sibling difference outside this claim: a forced-round scaffold hit is an exclusion in both, but in F0m it also stops the stage (runner_qwen.py:170-173).

#### D16. Analysis domain: an exclusion after the first pick keeps the session (m) but removed it from f1's primary
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:439 (valid = not excluded), :461-462 (first picks over valid sessions only). s4 and s25 (lexical@free4 after a first pick) left f1's primary of 28/56.
- F0m: scaffold.py:429-430, :445: domain = reached the first read, and first_free_pick_P is kept whatever follows (m:308).
- effect: Bears on A0's comparison with f1's primary. f1's 28/56 is computed on a domain that drops post-pick exclusions; m's rule applied to f1's archive gives 30/58, which m:308 itself states. This is an analysis-lens item: it is disclosed at m:308 but absent from §2.7's fourteen, so it is listed for Appendix D.
- evidence: m:308's figures. The f1 code at the anchors.
- refuter: The claim holds on both sides. I checked it against HEAD 5f7b968 and the archive.

f1's side: f_sessions.py:439 sets `valid = [r for r in rows if not r.get("excluded")]`. Lines :461-462 take the arm's `first_free_pick_P` from `valid` only, so an exclusion after the pick takes the session out of the primary. Line :374 sets excluded=True on a free-round lexical hit, even though :382-383 have already recorded the first pick. The sham pseudo-delta at :454-455 also uses `valid`, so f1's sham envelope is narrowed the same way.

The archive, recounted with the .venv python from data/f/sessions.jsonl:
- 64 CORR rows.
- 58 reached a first read, and 30 of those picked P.
- Two were excluded after the pick: s4 (`lexical:prism@free4`) and s25 (`lexical:maple@free4`), both with first_free_pick_P True.
- Valid sessions with a pick: 56, of which 28 picked P.
So 28/56 is f1's figure of record and 30/58 is what m's rule gives, exactly as claimed.

F0m's side, from `git show 5f7b968`:
- scaffold.py:429-430 sets `domain` from the forced rounds only: all forced rounds generated and unclaimed, no forced-phase hair trigger, no forced-phase exclusion.
- :431-432 asserts that domain means exactly "reached the first read".
- :445 keeps `first_free_pick_P` whenever `domain` is true, whatever free-round exclusion follows. :443 records `excluded` separately.
- runner_qwen.py's docstring (lines 16-21) and its free loop (lines 199-205) confirm that a free lexical claim ends the session after the round is recorded, with the domain kept.
- verify.py:251-256 enforces the same rule.
- m:306-308 locks the primary on this domain, says the sham envelope uses the same rule, and states the f1 figures (58 / 30 / two post-pick exclusions; 28/56 of record).

So the difference is real and observable: on the same data, m's primary domain keeps sessions that f1's analyze() drops, and the f1 numerator and denominator shift from 28/56 to 30/58.

Classification: none of §2.7's fourteen (m:267) covers the analysis domain or validity rule. Items (6) audit, (12) read window and (13) interleave and stop at floor are the closest. Item (13)'s floor counts domain sessions, but it is about stopping, not the primary's domain. Item (12)'s remark that "A0's comparison with f1's primary is unaffected" concerns the read window only. So the difference is beyond the fourteen. It is disclosed at m:308 (§4), not in the Appendix D list.

On the effect: "bears on A0's comparison with f1's primary" is defensible, since the primary's domain rule itself differs. It is mitigated by m:308 giving f1's value under m's rule (30/58), which makes a like-for-like comparison possible. One facet is not stated in the claim but strengthens it: f1's sham pseudo-delta (:454-455) is also limited to valid sessions, while m's envelope uses the domain.

### Lens delivery-rng

**Covered (the lens's own statement):** Lens: delivery and randomness. 14 differences found. Covered by §2.7: (3) the corruptor structure, (4) the sham pool, (5) roster and pairing, including the map-polarity detail on slate/prism, (7) split streams, (8) the 32-cell permuted assignment. Beyond the fourteen: 9 items, two of them outside this lens and labelled so. They are: the byte-clean Q renders, which bear on A0's comparison with f1's primary; the cross-arm match that went from cell to items; the rotation-to-pair coupling (f1 coupled, m campaign independent, m gate stages coupled via pi); the record-schema renames, with start polarity inverted; the missing graded counter; the gate-stage streams; schedule exhaustion; and, outside the lens, the primary domain (28/56 vs 30/58, disclosed at m:308 but not in §2.7) and the free-round ban-string hair trigger. Checked and found the same in both: P-role texts byte-identical (same pool, sha 8547d9a1); the [:8]/[8:16] role split; per-label in-order consumption across forced and free rounds, the chosen round taking the picked role's next item; forced order by start; the menu-order mapping; seed form int(rng.integers(2**31)); the per-item corr|{i} key form; the joiners and the pick line. Judged against HEAD 5f7b968 via git show. Scratch scripts are in step5/delivery-rng/ (rot.py, f1items.py).

**Internal, no effect (the lens's list):**
- Item exhaustion: f1 wraps (P_items[iP % len], f_sessions.py:287, :290); m raises ItemStreamExhausted on a ninth draw (corr.py:363-371). Neither can happen: at most 2 forced + 6 free = 8 per role.
- Character class: f1 uses Unicode isalpha (f_sessions.py:111); m uses ASCII [A-Za-z] and asserts the pool is ASCII (corr.py:168, :198, :218). Identical on the pinned pool.
- Pool pin: f1 printed the pools sha but loaded the file unpinned (f_sessions.py:549, :562-564); m refuses any pool whose sha256 does not start 8547d9a11ba55b95 (corr.py:176-182). Same bytes.
- numpy stream known answer: m checks the f|CORR|0 permutation(16) at every stage startup (keys.py:37-49; stages.py:350); f1 had no such check. Same numpy on the laptop.
- Generation seed timing: f1 calls mx.random.seed after the prefill extend (f_sessions.py:168-169); the m adapter seeds before it (qwen_mlx.py:268-269). The prefill draws nothing, and the sampler is the same (-1e30 ban vector, then categorical(lg/0.7) per step: f_sessions.py:174-181 vs qwen_mlx.py:279-290).
- Rotation arithmetic: f1 passes s+ri or s+ci and applies %4 at format time (f_sessions.py:310, :338, :360); m precomputes (s+ri)%4 and (s+ci)%4 and asserts 2F % 4 == 0 (scaffold.py:116-118, :172, :197-198). Same indices.
- Shared n for a menu and its chosen round: f1 uses n_round -= 1 (f_sessions.py:359); m sets n = 2F+1+ci explicitly (scaffold.py:180, :197). Same 5..10.
- Within-round draw order: both take the item, build the segment, then draw the seed (f_sessions.py:308-312; scaffold.py:160-164). Same consumption.
- P/Q split: f1 slices idx[:need] and idx[need:2*need] with need = 8; m slices perm[:8] and perm[8:16] with N_ITEMS = 16 constant (f_sessions.py:254-255; corr.py:358-360). Same.
- f1's oop list (f_sessions.py:280) is computed and never used.

#### D17. f1's corruptor delivered byte-clean text under the corrupted role: items 1 and 12 unchanged, item 8 hit with the same letter
- finder's classification: beyond; refuter: refuted=False, classification covered by (3)
- f1: jlens-qwen36/scripts/f_sessions.py:106-116 (per-letter Bernoulli at 0.12, 26-letter draw) applied at :258 to every Q-role item. The renders of items 1 ('State the number of days in a week.') and 12 ('Compute 11 + 33.') equal the clean text byte for byte. Item 8 has 3 hits but only 2 changed letters (one draw returned the same letter).
- F0m: valence_core/m/corr.py:204-252 (corrupt_m changes exactly k >= 3 letters per item, 54 in total, never the original letter) and corr.py:255-264 (renders_m). Every Q-role render differs from clean; item 1 renders 'State the number oq dsys in a wemk.', item 12 'Cnmzote 11 + 33.'. corr.py:400-405 labels the property by role, which is moot in m because no render equals its clean text.
- effect: Bears on A0's comparison with f1's primary. In 16 of f1's 58 first reads (16 of 56 valid sessions), one of the two forced Q tasks before the pick was byte-clean, so the model saw only one corrupted task before choosing; this never happens in A0. It also bears on secondary (b) lose-shift if compared with f1: 24 of f1's 182 chosen 'corrupted' rounds were clean text. Descriptive for the per-property table: f1 s1's one Q-role post_degen (free ci1) fell on item 12, which is byte-clean. This follows from (3)'s change of corruptor, but (3) names only the rate and the draw, not this consequence.
- evidence: A replay of f1's item streams (f|CORR|{s} permutation(16), Q = [8:16]) against the 64 CORR rows matches every recorded task[:40]. Byte-clean Q rounds: 40 of 306 (16 of 124 forced, 24 of 182 free). First reads after exactly one byte-clean forced Q round: 16 of 58; after two: 0. Letters changed per item under f1: [1,0,5,2,3,1,4,6,2,1,2,1,0,1,1,1], total 31. Scratch: step5/delivery-rng/f1items.py.
- refuter: The facts hold, so I am not refuting the claim. But it is a consequence of item (3), not a difference beyond the fourteen.

How I checked: I wrote my own replay, scratchpad/step5/refuter-delivery-rng/replay.py, and ran it against jlens-qwen36/data/f/pools.json and sessions.jsonl. These are byte-identical to the root copies (sha256 8547d9a1... and d49913e5...). I checked every Q-role round's full "Task: ...\nResponse:" line in all 64 CORR transcripts, not just the 40-character log field.

What I confirmed on f1's side:
- f_sessions.py:106-116 is the per-letter Bernoulli at CORR_RATE 0.12 (:89). It applies only to letters that do not start a word, draws from 26 letters, and is applied at :258 to every CORR Q-role item.
- Items 1 and 12 get 0 hits, so their renders equal the clean text byte for byte.
- Item 8 has 3 hits, one of which drew the original letter, so 2 letters change.
- Letters changed per item are [1,0,5,2,3,1,4,6,2,1,2,1,0,1,1,1], total 31.
- 40 of 306 Q rounds were byte-clean: 16 of 124 forced and 24 of 182 free.
- Of the 58 first reads (56 in sessions that were not excluded), 16 came after exactly one byte-clean forced Q round and none after two.
- s1's only post_degen (ci1) fell on Q item 12.

What I confirmed on F0m's side:
- At HEAD 5f7b968, I called corr.renders_m on the rosters of record. Every one of the 16 renders differs from its clean text, with 54 letters changed in total.
- Item 1 renders 'State the number oq dsys in a wemk.' and item 12 renders 'Cnmzote 11 + 33.', as the claim says.
- `_k_m` (corr.py:204-209) clips k to at least 3. The replacement formula at corr.py:236 never returns the original letter.
- scaffold.N_FORCED is 4 (two forced rounds per role), and A0's Q role always delivers the render (Delivery at corr.py:403-404). So in A0 a first pick is never preceded by a clean forced Q task.
- The PIN comment at corr.py:400-402 itself cites f1's items 1 and 12.

Why I classify it under (3):
- (3) discloses exactly this corruptor difference: corrupt_m at 0.15 against f1's corrupt() at 0.12 and its 26-letter draw. Its two named features, the 0.12 per-letter rate and the 26-letter draw, are the two mechanisms that produce the zero-hit items and the same-letter no-op.
- The proposal already treats the consequence as part of the dose disclosure:
  - §0.4 (m:48) gives 31 changed letters against m's 54.
  - Ledger (27) (m:27) names the 26-letter draw's 1/26 non-change.
  - §2.3 (m:176) schedules a model-free replay of f1's 0.12 corruptor against condition (1), every item ≥ 3 changed. That replay is what records items 1 and 12 at zero.
  - §7.5(c) (m:349) carries the result as the preprint's f1 CORR dose note.
- The 40/306 count was already on record before v1.11: results/raw/2026-10-04_m-v1.7_referent_check.txt:5204-5207 gives 40 of 306 (item 1: 23, item 12: 17) and says the dose note rests on it.

The only figure I did not find on record is 16 of 58 first reads, which is the effect on A0's comparison with f1's primary. Unlike items (12) and (14), (3) says nothing about the primary. The G-PORT entry can state that figure beside (3) as a quantified consequence, not list it as a new difference. The lose-shift point is hedged, since m:312 secondary (b) is not defined as a comparison with f1. The per-property point is descriptive and correct.

#### D18. One session rng in f1, split streams in m: items, seeds and menu orders all differ at every s
- finder's classification: §2.7 (7); refuter: refuted=False, classification §2.7 (7)
- f1: f_sessions.py:273-274 sets rng = f|CORR|{s}. permutation(16) is drawn first (:254), then per round one seed int(rng.integers(2**31)) (:312) and per choice one menu order rng.integers(2) (:351), all from that one stream.
- F0m: keys.py:96-134 gives the item stream m-items|{s} (shared by A0 and A0s) and the arm rng m|A0|{s} or m|A0s|{s}. scaffold.py:253-269 builds ItemStreams(stream(item_key)) and arm_rng = stream(arm_key). The arm rng's first draw is the first forced seed (scaffold.py:580-589 self-test).
- effect: None beyond the disclosure. No m session reproduces any f1 session's items, seeds or menu orders. Within each stream the relative order is the same: in a round the segment is built, then the seed is drawn; per choice the menu order is drawn, then the seed.
- evidence: scaffold.py:159-166 and :174-199 against f_sessions.py:305-312 and :347-360. The mapping 0 -> (P-role label, Q-role label) is the same in both (f_sessions.py:351; scaffold.py:177-178).
- refuter: The difference holds as claimed, and every cited line says what the claim says it does.

f1 side. f_sessions.py:273-274 seeds one rng with default_rng(crc32("f|{arm}|{s}") % 2**31). items_for is called at :281, and for CORR it draws permutation(len(CORR_clean)) at :254, so this comes first: P = idx[:8], Q = idx[8:16], with need = F_FORCED 2 + N_FREE 6. Each round then draws its seed at :312, after next_item and the segment (:308-311). Each choice draws its menu order rng.integers(2) at :351, then the chosen round's seed comes through run_round at :360. corrupt() (:106-112) uses its own corr|{i} stream, not the session rng. I re-derived this order from the archive: all 64 of 64 CORR sessions in data/f/sessions.jsonl match it exactly. The check was permutation(16), then 4 forced seeds, then per choice the menu bit and the free seed, against the logged seeds and menu_a values.

m side, at HEAD 5f7b968.
- keys.py:96-109 gives item_key m-items|{s}, and :112-134 gives arm_key m|A0|{s} or m|A0s|{s} for the campaign. keys.stream (:27-29) uses f1's crc32 form.
- scaffold.py:253-254 and :266-267 build arm_rng = stream(arm_key) and ItemStreams(stream(item_key)).
- ItemStreams (corr.py:350-371) draws one permutation(16) from the item stream and nothing else.
- So the arm rng's first draw is the first forced seed. scaffold.py:164 draws it after the segment is built, and :177 draws the menu bit with 0 -> (P, Q), the same mapping as f1's :351.
- The self-test at scaffold.py:580-589 asserts this order: 4 seeds, then (menu, seed) per choice. The runner draws only through forced/menu/chosen (runner_qwen.py:156, :179, :186); its other rng use (:392-398) is inside the self-test.

Classification. The claim is covered by §2.7 (7), not beyond it. (7) names "the rng keys and the item stream shared between contrast and sham session s (f1 drew items from the session rng, :254–259)". Everything the claim adds follows from that split: different keys, and seeds that no longer come after a permutation. Its effect on the comparison with f1 is none beyond the disclosure.

Minor wording problems (not grounds to refute):
(1) "Menu orders all differ at every s" and "no m session reproduces any f1 session's ... menu orders" are overstated. The menu orders are single bits from an independent stream, so they coincide by chance.
- At the same s (0-63), the first menu bit matches 27 of 64 times for A0 and 33 of 64 for A0s.
- A0s at s=28 reproduces f1 CORR s=28's whole six-bit menu sequence.
- 1,611 of 2,624 A0 campaign sessions (1,631 for A0s) have a six-bit menu sequence equal to some f1 CORR session's.
- Items and seeds never coincide: no same-s permutation, P8 or seed match for s 0-63, and no m campaign permutation equals any f1 permutation.
(2) f1 CORR has s = 0..63 only. For m campaign s ≥ 64 there is no f1 session at the same s to compare against.
(3) The claim names only the campaign keys. At gate stages the arm keys are m-time|, m-id|F0m| and m-f0m|, and the item keys are m-items-{gate}|{s}. The same keys.py:96-134 span covers them, and they are equally covered by (7).

#### D19. Sham items: f1's SHAM pool on its own key, m's CORR_clean on the contrast's item stream
- finder's classification: §2.7 (4); refuter: refuted=False, classification ALREADY COVERED: §2.7 (4), for the sham pool (CORR_clean to both labels against f1's SHAM creative pool, f_sessions.py:265–267), and §2.7 (7), for the item stream that contrast and sham session s share. It is not beyond the fourteen.
- f1: f_sessions.py:265-267: SHAM creative prompts (no gold) split [:8]/[8:16] from the f|sham|{s} rng (:273). The sham shares no items with CORR session s.
- F0m: corr.py:403-405: A0s serves CORR_clean to both roles. keys.py:100-101: m-items|{s} is shared, so A0s session s gets exactly A0 session s's P-role and Q-role pool indices, uncorrupted.
- effect: Already disclosed under (4) and (7). Descriptive: A0s rounds carry golds, which f1's sham rounds did not.
- evidence: scaffold.py:605-609 self-test: sham items equal contrast items at the same s.
- refuter: Both sides check out against f1's code, its pool file and the m package at HEAD 5f7b968.

f1's side:
- f_sessions.py:265–267 sends the SHAM arm to pools["SHAM"] through one permutation. need = F_FORCED + N_FREE = 2 + 6 = 8 (:85–86, :237), so P gets idx[:8] and Q gets idx[8:16].
- The rng at :273 is crc32(f"f|{arm}|{s}"), and the arm string is "sham" (:88), so the key is f|sham|{s}.
- data/f/pools.json SHAM holds 16 {task}-only items (creative prompts such as "Write a one-sentence welcome for a small art fair.") with no gold. Its task set does not intersect CORR_clean's (checked: an empty set), so f1's sham s shares no items with CORR s.
- Archived f1 sham rounds record graded=None (data/f/sessions.jsonl, 40 sham rows; checked the first round of the first row). Grading is the call at :326.

F0m's side:
- corr.py:403–405 corrupts only when role=="Q" and contrast is true; every other case returns clean[i] with property CLEAN, so A0s serves CORR_clean to both roles.
- keys.py:100–101 builds item_key for Q-F0 as m-items|{s} with no template term. It is therefore shared across A0 and A0s at the same s.
- ItemStreams (corr.py:350–360) takes one permutation(16): P=perm[:8], Q=perm[8:16]. So A0s s gets the same per-role index tuples as A0 s, uncorrupted.
- scaffold.py:605–609 asserts this. Two limits: it checks only the forced rounds (sspecs against specs[:4]), and the free-round items depend on picks; the per-role tuples are equal by construction.

Classification: §2.7 (4) names exactly this pool swap and cites f_sessions.py:265–267. §2.7 (7) names the rng keys and the item stream shared between contrast and sham session s. Nothing here goes beyond the fourteen.

One imprecision, which does not refute the claim: the effect line says "A0s rounds carry golds, which f1's sham rounds did not". In the m package at HEAD, 'gold' appears only in corr.py (pool validation and the hygiene roster check), stages.py:20 and :348 (hygiene docstrings) and pool docstrings. Nothing in scaffold, runner_qwen, verify, audit or m_sessions grades or records a gold. So the gold is visible neither to the model nor in the record, and no round in either template is graded, whereas f1 graded CORR rounds at :326. The observable difference is the task content: arithmetic CORR_clean items, identical to A0 s's, against f1's disjoint creative prompts.

'Descriptive' is the right grade for the primary: m:306 locks Δ_c = P − 0.5, with P_arm − P_sham only reported beside it. The swap does bear on any sham-relative comparison with f1, such as P_arm − P_sham and f1's Fisher-vs-sham guard (:393–415). That is still descriptive, but the effect line should say so.

#### D20. The cross-arm match flipped: f1's sham s shared CORR s's cell, not its items; m's A0s s shares A0 s's items, not its cell
- finder's classification: beyond; refuter: refuted=False, classification (8), with (5)'s index arithmetic; not beyond. At most a clarifying clause for (8): "f1's per-index derivation was arm-free, so its sham s carried CORR s's cell; m's schedules are drawn per arm".
- f1: f_sessions.py:275-278: the cell arithmetic (pair = TAG_PAIRS[s%4], swap, start_P, tag_P) does not depend on the arm, so sham session s carried CORR session s's cell. The items came from a different pool (:265-267).
- F0m: keys.py:142-145 and schedule.py:217-232: separate schedule keys m-sched|Q-F0|A0|b and m-sched|Q-F0|A0s|b, so A0s cell s is unrelated to A0 cell s, while items are shared (keys.py:100-101).
- effect: Descriptive. E is pooled in both (f_sessions.py:456; m:310), so index matching does not enter conjunct (i). Any analysis that pairs contrast and sham by index matches different things in the two apparatuses: f1 matched assignment, m matches items. The item half is (7); the loss of cell matching is stated nowhere.
- evidence: In f1's archive all 40 of 40 sham rows (s 0-39) carry their CORR row's pair, swap, start_P and tag_P. In m's committed schedules, A0 and A0s have identical (pair, map, start, clause) at the same s in 1 of the first 32 launch indices, 1 of the first 96 and 17 of 960; identical P/Q labels in 2/32, 5/96 and 103/960.
- refuter: FACTS: the claim holds, with one imprecision. f1 side, checked: f_sessions.py:275-278 builds pair = TAG_PAIRS[s%4], swap = (s//4)%2, tag_P/tag_Q and start_P = (s//8)%2 from s alone. The arm is not used. The rng key f|{arm}|{s} (:273-274) feeds only items and seeds. The sham's items come from pools["SHAM"] (:265-267). CORR's come from CORR_clean (:253-259). In data/f/sessions.jsonl (CORR 64 rows, sham 40), all 40 sham rows (s 0-39) carry their CORR row's pair, swap, start_P and tag_P. Session 0's tasks differ between the two (a creative prompt against a CORR item).

m side, checked at 5f7b968: keys.py:142-145 builds sched_key m-sched|{unit}|{arm}|{b}. schedule.py:217-232 draws each arm's balance units from its own key. stages.py:1919-1925 launches scheds[arm]["cells"][s]. Items come from keys.item_key (keys.py:100-101, m-items|{s}), and scaffold.py:253-254 calls it with no template, so A0 and A0s share items at s.

Recomputed from the committed Q-F0_campaign_A0.json (2,624 cells) and Q-F0_campaign_A0s.json (960 cells): full (pair, map, start, clause) identity at the same s is 1/32, 1/96 and 17/960. Identical P/Q labels are 2/32, 5/96 and 103/960. Both match the claim.

Effect, confirmed descriptive. f1's E is the pooled |mean - .5| over sham (f_sessions.py:454-456). m's E is pooled over the matched sham arm's domain (m:309). P_arm - P_sham is pooled. No primary, secondary or bar pairs contrast and sham sessions by index in either apparatus.

IMPRECISION, not a refutation: "A0s cell s is unrelated to A0 cell s" holds for the campaign only. At the gate stages the key is m-sched|{unit}|{gate}|{template}|0 (keys.py:148-154). Only the pair permutation pi differs by template; map, start and clause come from the fixed sixteen-row table (schedule.py:247-263). In the committed Q-F0_qual files, A0 and A0s share map, start and clause at 8 of 8 indices and the pair at 0 of 8 (pi [1,0,2,3] vs [3,2,0,1]). So at qualification, m keeps three of the four cell factors matched across arms. G-ID runs A0s only.

CLASSIFICATION: covered, not beyond. (8) names this exact change: "a committed schedule balancing pair x map x start x clause against f1's per-index derivation". (5) cites the same index arithmetic, f_sessions.py:275-278. A per-index derivation is arm-free by construction, which is why every f1 arm at s shared a cell. m:159 states that m's schedules are keyed per arm (m-sched|{unit}|{arm}|{b}). So losing the cross-arm cell match is a direct consequence of (8)'s assignment change, not a separate way the sessions differ. What is new is only an unstated implication. The asymmetry is fair to note: (7) announces the item sharing, while nothing spells out the cell un-sharing. That argues for one clarifying clause in (8), not a fifteenth item.

#### D21. Paraphrase rotation tied to the roster pair in f1, independent of the cell in m's campaign, tied again (via pi) at m's gate stages
- finder's classification: beyond; refuter: refuted=False, classification Covered by (8) as to mechanism, with (5)'s "index arithmetic" (f_sessions.py:275–278) as f1's half. The consequence it points to is not stated in (8) or anywhere in §2.7: f1's paraphrase wording was collinear with the pair, m's campaign breaks that link, and m's gate stages restore it under π. That makes this an effect note to attach to (8). It is not a fifteenth item.
- f1: f_sessions.py:275 sets pair = TAG_PAIRS[s%4], and the rotation offset is also s%4: ROUND_TEMPLATES[(s+ri)%4] (:310, :338, :360) and MENU_TEMPLATES[(s+ci)%4] (:352). So the whole template sequence is fixed by the pair: the first-read menu is MENU_TEMPLATES[pair index] in every session, and the forced header style per role (templates 0/2 use '|', 1/3 use '—') is fixed by pair and start. Within each 16-session block, wording × map × start is a full factorial.
- F0m: scaffold.py:172, :179, :197 use the same formula with s = the arm's launch index. stages.py:1918-1925 passes cell = schedule[s], drawn independently, so the wording is not tied to the pair and not balanced against map or start. At gate stages, schedule.py:78-95 (slot = j%4) and :262-263 give pair = pi[j%4] at offset j%4 (stages.py:1346 passes s = j), so pair and wording are coupled again, under a different pair-to-wording mapping.
- effect: Descriptive. It bears on secondary (d) if per-pair first-pick shares are compared with f1, because f1's per-pair shares are fully confounded with the first menu's wording and m's campaign shares are not. The primary is unaffected in expectation: the marginal wording is balanced in both (f1 by design; m by launch index). m's gate-stage per-pair sham shares carry the same kind of confound as f1's.
- evidence: From f1's transcripts, the first-read menu wording per pair: slate/prism 'Available configs' 14/14, maple/cedar 'Configs available' 14/14, granite/lattice 'Options' 16/16, plaza/saddle 'Configs on offer' 14/14. In m's A0 campaign over the first 96 launches: pair 0 meets offsets {0:7, 1:8, 2:6, 3:3}, pair 3 {0:2, 1:9, 2:4, 3:9}; wording × map cells hold 10-14; P-role '|'-style forced headers 52/96 (f1 32/64). Gate-stage pi: qual A0 [1,0,2,3], qual A0s [3,2,0,1], id A0s [3,0,1,2]. Scratch: step5/delivery-rng/rot.py.
- refuter: Every factual part of the claim checks out against HEAD 5f7b968 and the archives, so it is not refuted.

f1 side:
- :275 pair = TAG_PAIRS[s%4]; :310 ROUND_TEMPLATES[template_i%4]; :338 run_round(cfg, s+ri); :352 MENU_TEMPLATES[(s+ci)%4]; :360 run_round(picked_cfg, s+ci). So the first menu's wording index equals the pair index.
- The P role's forced header style ('|' in templates 0/2, '—' in 1/3) is set by pair parity and start_P.
- In each 16-session block, offset × swap × start is the full 4×2×2 factorial.
- The archive (data/f/sessions.jsonl, 64 CORR rows, 58 of which reach a menu) shows the first menu exactly as claimed: slate/prism 'Available configs' 14/14, maple/cedar 'Configs available' 14/14, granite/lattice 'Options' 16/16, plaza/saddle 'Configs on offer' 14/14. P-role '|' headers: 32/64.

m side:
- scaffold.py:172, :179 and :197 use the same (s+i)%4 formula.
- In the campaign, stages.py:1918 sets s = launches[arm] and :1925 passes scheds[arm]["cells"][s], a cell drawn independently of s.
- I recomputed from the committed Q-F0_campaign_A0.json (first 96 launches): pair 0 meets offsets {0:7, 1:8, 2:6, 3:3} and pair 3 meets {0:2, 1:9, 2:4, 3:9}. Wording × map cells hold 10–14, and P-role '|' headers are 52/96.
- At gate stages, GATE_TABLE's slot column is j%4 (schedule.py:78), and :262–263 assign pi[slot]. stages.py:1346 (and :1535 for G-ID) passes j as s, and m_config records j = s. So pair = π[j%4] at offset j%4. The committed π values are as claimed: qual A0 [1,0,2,3], qual A0s [3,2,0,1], id A0s [3,0,1,2].
- The difference is observable: it changes which label pair the model sees with which paraphrase.

On the effect:
- "Descriptive" holds. The marginal wording is balanced in both setups, so A0's comparison with f1's primary is unaffected in expectation.
- Secondary (d) at m:312 pools per-pair first picks and names no f1 comparison. A per-pair comparison with f1 is mostly moot anyway, because the rosters share only slate/prism (item 5).
- m:172 claims the gate-stage per-pair sham shares are free of start/clause confounding. That is true, but it says nothing about wording, and those shares are fully confounded with the first menu's wording. That is m-internal, not a difference from f1, and is worth noting alongside.

On classification:
- The wording rotation is identical in both setups; m:159 cites it as f1's rule. What changed is only that the cell is no longer derived from s, which is exactly what (8) discloses ("committed schedule … against f1's per-index derivation"), with (5) naming f1's index arithmetic.
- The changed joint distribution of pair and wording follows from (8). By the same logic the item streams are also decoupled from the pair; those are further consequences of (8), not separate differences.
- So "beyond" overstates it. The genuinely undisclosed content is the effect note: f1's per-pair shares are confounded with wording, m's campaign shares are not, and m's gate-stage shares are confounded again under π.

Scratch: step5/refute-rot/{check.py, f1check.py}.

#### D22. Assignment: f1's fixed-order 16-cell arithmetic against m's permuted 32-cell committed units
- finder's classification: §2.7 (8); refuter: refuted=False, classification §2.7 (8). (5) cites the same f1 index arithmetic at f_sessions.py:275–278, and the arm ending mid-unit is a consequence of (13)'s per-arm stop at floor.
- f1: f_sessions.py:275-278: pair cycles fastest, then swap, then start. The unit is 16 cells in a fixed order; 64 sessions are 4 complete units. There is no clause factor.
- F0m: schedule.py:199-232: pair × map × start × clause = 32 cells, each balance unit a permutation drawn from m-sched|Q-F0|{arm}|{b}, committed in data/m/schedules/Q-F0_campaign_A0.json (2624 cells) and Q-F0_campaign_A0s.json (960). Stopping at the floor (stages.py:1909) can end an arm mid-unit.
- effect: Already disclosed. Map coding is the same (0 or swap False: the pair's first label holds P), and start is the same (P's round first ⇔ f1 start_P True ⇔ m start 0).
- evidence: scaffold.py:272-279 (f1_cell) maps f1's arithmetic onto m's cell form; schedule.py:13-14 states P = pair[map].
- refuter: Every factual part of the claim checks out against both codebases (HEAD 5f7b968 on the m side).

**f1 side.** f_sessions.py:275–278 is exactly the arithmetic described:
- pair = TAG_PAIRS[s % 4]
- swap = (s // 4) % 2 == 1
- tag_P = pair[1] if swap else pair[0]
- start_P = (s // 8) % 2 == 0

So pair cycles fastest, then swap, then start, giving a fixed 16-cell period. There is no clause factor: f1 had no TOLD line, and its banner is only SESSION_BANNER (f_sessions.py:65). The archive data/f/sessions.jsonl has 64 CORR rows, sessions 0–63, which is 4 complete units. I recomputed pair, swap and start_P from s for all 64 rows and found 0 mismatches.

**m side.**
- schedule.py:199–232 at HEAD builds _cell (P = pair[map], Q = pair[1 − map]). campaign_cells forms pair × map × start × clause (clause in (0, 1), so 32 cells). campaign_schedule permutes each unit with keys.stream(sched_key(unit, arm, b)).
- keys.py:142–145 gives the key as "m-sched|{unit}|{arm}|{b}".
- The committed data/m/schedules/Q-F0_campaign_A0.json has n 2624, n_units 82, balance_unit 32 and key_template "m-sched|Q-F0|A0|{b}". Q-F0_campaign_A0s.json has 960 cells (30 units).
- stages.py:1909 builds the rotation as interleave(arms, lambda a: domain[a] >= fl[a], ...). An arm therefore leaves when its domain count reaches its floor, with no unit-boundary condition, so it can end mid-unit.

**Coding equivalence.**
- scaffold.py:272–279 (f1_cell) maps swap to map 1 and start_P to start 0, with P = pair[map].
- scaffold.py:135 gives start 0 as P Q P Q, matching f1's order of ["P","Q"] when start_P (f_sessions.py:296).
- So map 0 / swap False means the pair's first label holds P, and start 0 means start_P True, both as claimed.

**Classification.** §2.7 (8) discloses this difference verbatim: "a committed schedule balancing pair × map × start × clause against f1's per-index derivation". (5) also names f1's index arithmetic for swap and start at the same lines. The one element the claim adds beyond (8)'s wording is that an arm can end mid-unit. That follows from (13)'s "per-arm stop at floor" combined with (8), so it is not a new difference. Its effect is descriptive only: cell balance at the realised n can be inexact, while f1's 64 were exact.

The claim is correct and correctly placed as covered; it is not beyond the fourteen.

#### D23. Roster and pairing, with a map-polarity detail on the one shared pair
- finder's classification: §2.7 (5); refuter: refuted=False, classification §2.7 (5)
- f1: f_sessions.py:61-64: TAG_PAIRS (slate,prism), (maple,cedar), (granite,lattice), (plaza,saddle).
- F0m: valence_core/e2d/config.py:36-37 (imported at schedule.py:174-178): (granite,plaza), (prism,slate), (velvet,walnut), (ridge,saddle).
- effect: Already disclosed. Detail (5) does not name: map is defined against pair order, and the only common pair is ordered (slate, prism) in f1 but (prism, slate) in m, so f1 map A (P = slate) is m map 1. Five of the eight labels are shared but paired differently. Descriptive for any by-map or by-pair comparison with f1.
- evidence: Compare the two literals; schedule.py:199-204 (_cell, P = pair[map]).
- refuter: The claim holds as stated, and I classify it the same way: covered by (5).

What I checked:
- **f1's roster.** f_sessions.py:61-64 has TAGS = slate, prism, maple, cedar, granite, lattice, plaza, saddle. TAG_PAIRS = (slate,prism), (maple,cedar), (granite,lattice), (plaza,saddle).
- **f1's map.** f_sessions.py:275-277 has pair = TAG_PAIRS[s%4] and swap = (s//4)%2==1. When swap is False, tag_P = pair[0]. At :472 f1 labels swap False as by_map "A". So for the shared pair, f1's map A has P = slate. items_for CORR (:253-259) gives P the clean items and Q the corrupted ones.
- **m's roster.** valence_core/e2d/config.py:36-37 has ROSTER = (granite,plaza), (prism,slate), (velvet,walnut), (ridge,saddle). At HEAD 5f7b968, schedule.py:174-177 (roster_for for Q-F0) returns it through _norm_roster, which keeps both the pair order and the order within each pair (:149-156).
- **m's map.** _cell at schedule.py:199-204 sets P = pair[mp] and Q = pair[1-mp]. m:159 defines map 0 as "the pair's first label holds the P role". In scaffold.py:64 and banner.py:6-7, P is the clean label.

So m's map 1 for (prism, slate) has P = slate, the clean label. That is the same assignment as f1's map A (slate clean). The polarity detail is right.

The label counts are also right. Five labels are shared: slate, prism, granite, plaza, saddle. The only pair the two rosters share, ignoring order, is {slate, prism}. One wording point: "five of the eight labels are … paired differently" is loose. Slate and prism are paired with each other in both rosters. Only granite, plaza and saddle have different partners. That is a minor wording point and does not refute the claim.

The difference is observable: f1 records "swap" in each session row (:377) and computes a by_map split (:467-484), and m records cell.map.

On classification, §2.7 (5) already discloses "the roster and pairing — e2d.config.ROSTER under the committed schedule against f1's TAG_PAIRS with its index arithmetic for swap and start". The polarity flip on the shared pair follows directly from the two literals and the two map definitions. It is a detail (5) does not spell out, not a difference beyond the fourteen. The effect is descriptive: it matters only for a by-map or by-pair comparison with f1. A0's pooled comparison with f1's primary is unaffected.

#### D24. Corruptor structure (Bernoulli versus fixed k)
- finder's classification: §2.7 (3); refuter: refuted=False, classification §2.7 (3)
- f1: f_sessions.py:106-116: each non-word-initial letter is hit with p = 0.12 by a 26-letter draw. Per item 0-6 letters change, 31 in total, operands included (item 15 'opev'); no roster skip.
- F0m: corr.py:204-252: k = clip(floor(0.15n+0.5), 3, n//2) via a permutation walk; one integers(25) draw per visited slot; never the original letter; the roster skip fires once (item 7, where 'State' would become 'Slate'; the Qwen roster word decides, and the renders under the Qwen roster alone equal those under both rosters); the operand is excluded. Renders sha16 a04f67b0e5105a05.
- effect: Already disclosed (the byte-clean consequence is listed separately above). For scale before the first pick: f1's two forced Q tasks carried 1-9 changed letters (33 of 58 first reads at 4 or fewer); m's carry at least 6.
- evidence: corr.py self-test :536-560 and :600-629; f1 replay of 58 first reads, distribution {1:9, 2:12, 3:6, 4:6, 5:7, 6:9, 7:7, 8:1, 9:1}.
- refuter: I checked every factual claim against both codebases and replayed the corruptors myself, without a model or tokenizer. The script is at /private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/refute-corruptor/check.py. It runs f1's own `corrupt()`, taken verbatim from the f_sessions.py source, and HEAD's corr.py, which is identical to the working tree.

f1's side holds.
- `corrupt` is at f_sessions.py:106-116 and `CORR_RATE = 0.12` is at :89. Each non-word-initial letter gets a Bernoulli hit at 0.12 and a 26-letter draw, so a hit can repeat the original letter.
- On CORR_clean, the changed letters per item are [1,0,5,2,3,1,4,6,2,1,2,1,0,1,1,1]: 0 to 6 per item, 31 in total. The renders' sha16 is 2c2c227395ea9f2d, which equals calib corr_sha.
- Item 15 renders "...of 'opev'.", so the operand is hit.
- There is no roster logic, and no render contains a roster word.

F0m's side holds.
- At HEAD, corr.py `_k_m` (:204) is min(max((15n+50)//100, 3), n//2), and `corrupt_m` (:212-252) does one `permutation(n)` (:225) and one `integers(25)` draw per visited slot (:233). The replacement offset is 1 to 25 mod 26, so the original letter never comes back.
- k sums to 54 with a minimum of 3.
- The only skip is item 7, at position 1, where "State" would become "Slate" and 'slate' is a Qwen-roster word. The Qwen-only renders equal the renders under both rosters. The OLMo-only roster gives no skip and a different sha (2879f5f4b40b8c9c).
- The renders under both rosters have sha16 a04f67b0e5105a05. scaffold.py:213 builds the renders of record with ROSTERS_OF_RECORD, so these are the renders the runner uses.
- Items 5, 11 and 15 keep their operands.
- The self-test anchors :536-560 and :600-629 say what the claim says they say.
- Minor anchor imprecision: the operand exclusion itself is in `_eligible_m` at corr.py:187-202, just outside the cited 204-252, which only calls it.

The scale evidence holds.
- I re-derived each f1 CORR session's Q list from rng `f|CORR|s`: `permutation(16)[8:16]`. It matches the logged Q tasks in all 64 sessions.
- 58 sessions reached a first read. The changed letters across their two forced Q rounds are distributed {1:9, 2:12, 3:6, 4:6, 5:7, 6:9, 7:7, 8:1, 9:1}, with 33 at 4 or fewer, exactly as claimed.
- F0m has N_FORCED = 4 rounds alternating P and Q (scaffold.py:63, :136), so there are two forced Q rounds with k ≥ 3 each, giving at least 6 changed letters. Putting m's renders on f1's own draws gives a minimum of 6.

Classification: the difference is covered, not beyond the fourteen. §2.7 (3) discloses "the dose and corruptor": `corrupt_m` at 0.15 with the roster skip and the operand exclusion, against f1's `corrupt()` at 0.12 with neither and a 26-letter draw. `corrupt_m` is defined at m:176 with fixed k, the floor of 3 and the permutation walk. The Bernoulli-versus-fixed-k structure is therefore part of the corruptor that (3) names, and the claimed difference's own covered_by of §2.7 (3) is correct. The effect statement (already disclosed; the before-first-pick figures are descriptive scale) is accurate.

#### D25. Record schema for cell, assignment and delivery: renamed fields, inverted start polarity, item identity recorded only in m
- finder's classification: beyond; refuter: refuted=False, classification beyond (it touches items 5, 7, 8 and 10 but none of them covers it)
- f1: f_sessions.py:377-385, row fields: pair, swap, start_P, tag_P, exclude_cfg ('sham' on the sham arm, :344, :375). Per round (:331-334): cfg, tag, task = render[:40], truncated, with no pool index. Per choice (:361-367): round, menu_a, pick, picked_cfg, with label_mass and p_a rounded to 4 dp. menu_b and the menu text are not recorded.
- F0m: scaffold.py:438-447: cell{pair_index, pair, map, start, clause, P, Q}, keys{arm, items}, s, j, template, contrast. Per round (:386-392): role, pole, label, property, item, task_text (full), template_index, n. Per choice (:404-409): ci, n, menu_index, menu, menu_a, menu_b, picked_role, picked_pole, read{} unrounded.
- effect: None on the data. Any analysis joining f1 rows to m records must map the fields: f1 start_P True = m start 0 (inverted truth value), swap = map, cfg = role. f1's delivered pool indices can be recovered only by replaying f|CORR|{s}, since f1 recorded none.
- evidence: Field lists as cited; f1's task[:40] is checked only by prefix in replay_f1_row (scaffold.py:485-498).
- refuter: I checked both codebases and the archive. The claimed difference holds on every point.

f1's side: the row dict is at f_sessions.py:377-385 and holds pair, swap, start_P, tag_P, exclude_cfg and the rest. exclude_cfg is set to 'sham' on the sham arm at :344 and :375. The per-round log at :331-334 holds cfg, tag, task=it['task'][:40], seed, n_tok, cap_hit, lex, degen, term, graded and verdict, with no pool index. The per-choice log at :361-367 holds round, menu_a, pick, picked_cfg, label_mass and p_a (both rounded to 4 dp), top1_is_label, verify_kl and ea; there is no menu_b and no menu text. All 64 archived CORR rows in data/f/sessions.jsonl have exactly these key sets. Session 0 shows task='State which is heavier: a kilogram of ir' (40 chars) and label_mass 0.3518.

F0m's side at HEAD 5f7b968: SessionLog.record is at scaffold.py:438-447. It records cell (_CELL_KEYS pair_index, pair, map, start, clause, P, Q, :72), keys{arm, items}, s, j, template and contrast. add_round (:386-392) records role, pole, label, property, item (the CORR pool index, :86), the full delivered task_text, template_index and n. add_choice (:404-409) records ci, n, menu_index, menu, menu_a, menu_b, picked_role, picked_pole and read{}. _read_dict (:356-363) keeps those values unrounded as float and adds p_b and top1_id. runner_qwen.py:150-209 builds the record that is written through this SessionLog.

The mapping is right. Scaffold :135 runs P first when start == 0, and f1_cell (:278) maps start_P True to start 0. swap True maps to map 1 (:277), and cfg maps to role (both are 'P'/'Q'). replay_f1_row checks the task only by its 40-character prefix (:485-487, :496-497).

Two small overstatements, neither of which refutes the claim:
- The title's "inverted start polarity" is loose. Both encodings mean the same thing: m's start is an index whose 0 means P first, so only the encoding differs (the body's "inverted truth value" says this correctly).
- "Recoverable only by replaying f|CORR|{s}" is too strong. f1's transcript carries each round's full Task line, so the pool indices can also be recovered by matching that text against CORR_clean and the 16 deterministic corrupt(task, i) renders.

The claim's mapping also leaves out exclude_cfg/exclude_reason against m's exclusion{class, phase, detail}. That is an incompleteness, not an error.

Classification: beyond. No item of §2.7 (m:267) discloses the record schema, meaning field names, rounding, the 40-character task truncation, the pool index, or menu_b and the menu text. Items 5 and 8 disclose how pair/swap(map)/start are derived and assigned, not how they are recorded. Item 7 covers how items are drawn, not how they are recorded. Item 10 covers only the absent ea field. Effect: none on the data, and none on A0's comparison with f1's primary (first_free_pick_P is recorded in both). The only consequence is that any join across the two records needs a field mapping, so it is descriptive at most.

#### D26. No per-round gold grading in m
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:326 and :333: graded = grade(text, gold), recorded on every gold-bearing round.
- F0m: No grade or gold use in valence_core/m or scripts/m_sessions.py at 5f7b968 (golds appear only in pool validation and hygiene, corr.py:165-171, :433). scaffold.py:386-392 has no graded field. m records item and full text, so grades can be recomputed afterwards.
- effect: Descriptive. The in-session completability of delivered CORR rounds (f1's per-round accuracy on P versus Q tasks) is not recorded by m.
- evidence: git grep of grade and gold over valence_core/m and scripts/m_sessions.py at 5f7b968: hits only in corr.py.
- refuter: The claim holds on both sides. f1 (jlens-qwen36/scripts/f_sessions.py:97-103 `grade`, :326 `graded = grade(text, it["gold"]) if "gold" in it else None`, :334 the `"graded"` field in each rounds_log entry) records a per-round grade on every round that carries a gold. That includes CORR P rounds and Q rounds, since Q items keep the clean gold (:258-259). The archived data/f/sessions.jsonl confirms it: CORR session 0 has `"graded": true` on every round. In f1 the grade only drives behaviour for FDBK P rounds (:328-329, the verdict line). For CORR it is recorded and nothing more, and f_postscreen_descriptive.py never reads `graded`. m at 5f7b968 has no grader at all. A `git grep` for grade/gold/accura/correct/normalize( over valence_core/m and scripts/m_sessions.py finds golds only in the corr.py pool validation (:165-172) and hygiene (:433), plus two hygiene docstrings in stages.py (:20, :348). That last point makes the evidence's "hits only in corr.py" slightly imprecise, but the substance is unaffected. The G-CAL grader is not built yet, and the session path has none. SessionLog.add_round (scaffold.py:385-392 at HEAD) records phase, idx, n, label, role, pole, property, item, task_text, template_index, seed, text, n_tok, cap_hit, stop_reason, audit and termination, with no graded field. The difference is observable in what each session records, though it changes nothing the model sees and nothing about how picks are made. Grades can be recomputed afterwards, because m keeps `item`, the full `task_text` and the full `text`, and f1's grade is deterministic. The effect is therefore descriptive only. Neither A0's comparison with f1's primary nor any declared secondary (m:312 (a)-(f)) uses per-round accuracy. The §2.3 covariate is measured separately at G-CAL, not from session rounds. On classification: none of §2.7's fourteen (m:267) covers it. Item (2) is about the CORR delivery renderer, (6) the audit, and (10) the per-choice lens read (ea_mass), not round grading. So "beyond" is correct.

#### D27. Gate-stage item and arm streams within the Q-F0 unit
- finder's classification: beyond; refuter: refuted=False, classification covered by (7) and (8), not beyond
- f1: f1's only sessions outside the campaign were the smoke at s = 1100 and 1104 on the same key family f|{arm}|{s} (f_sessions.py:592-595), with no separate item stream.
- F0m: keys.py:96-134: m-items-time|, m-items-id| and m-items-qual|{s}, with arm rngs m-time|{t}|{s}, m-id|F0m|A0s|{s} and m-f0m|{t}|{s}. Cells come from the sixteen-row table (schedule.py:78-95, :247-263). At qualification, A0 and A0s share items for s < 8.
- effect: None. Gate stages are not compared with f1.
- evidence: data/m/schedules/Q-F0_{time,id,qual}_*.json session_keys.
- refuter: The F0m side holds as written at 5f7b968. keys.py:96-109 gives the gate item keys m-items-{time,id,qual}|{s}. keys.py:112-134 gives the arm keys m-time|{t}|{s}, m-id|F0m|A0s|{s} and m-f0m|{t}|{s}. scaffold.py:253-254 builds every session from these, with j = s at gate stages. schedule.py:78-95 is m:161-170's sixteen-row table and :247-263 is gate_schedule. The committed Q-F0_{time,id,qual}_*.json files carry exactly these session_keys. The qualification split is real: 8 A0 cells and 16 A0s cells, both keyed m-items-qual|{s}, so A0 and A0s share items at s < 8 (their pi differ, because gate_sched_key includes the template). The f1 side also holds in substance: f1 has one key per session, f|{arm}|{s} (f_sessions.py:273-274), and items come from that rng (items_for, :281 / :253-259), so there is no separate item stream. The two sides differ as claimed, so I do not refute the difference.

Two corrections:
(1) The f1 side's "only ... the smoke at s = 1100 and 1104" is incomplete. data/f/sessions_smoke.jsonl holds 24 rows at s = 1000, 1004, 1100 and 1104, with CORR at all four (the "smoke file's 4" that m:275 sets outside the replay). archive/RESULTS-cycles3-4.md:408 says "Smoke indices ≥ 1000". f_sessions.py:592-595 shows only the re-smoke's plan, so the cited lines record 1100/1104 and not the earlier smoke. I could not check the 1000/1004 rows' key family from the current code without git in jlens-qwen36.
(2) The effect "Gate stages are not compared with f1" is too strong. m:283 has G-F0m-Qwen report its low-label-mass and top-1-not-a-label flags beside "f1 CORR first reads 26/58 and 58/58". The effect is therefore at most descriptive, and it bears on neither A0's primary comparison nor a secondary.

Classification: this is not beyond the fourteen. §2.7 item (7) is "the rng keys and the item stream shared between contrast and sham session s (f1 drew items from the session rng, :254–259)". §2.1 (m:159) defines the gate item streams and gate arm rngs in the same key list as the campaign keys. The qualification's shared items at s < 8 are exactly (7)'s contrast/sham item sharing. Item (8), "a committed schedule balancing pair × map × start × clause against f1's per-index derivation", covers the sixteen-row gate table: m:159 defines it as the gate-stage schedule, and m:279 locks "Q-F0's schedules (campaign and gate stages)". What remains is that f1 ran its smoke at offset indices on its own key family while m uses separate gate prefixes. That is a detail of (7), not a new item.

#### D28. Cells can run out: the committed schedule bounds launches and exhaustion pauses
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:597-607: a fixed plan of n per arm; nothing can run out.
- F0m: schedule.py:102-116 materializes A0 2624 and A0s 960 cells; stages.py:1918-1923 pauses with kind 'schedule_exhausted' for the PI if an arm is below its floor.
- effect: None. Reachable only past the k = 1 launch row.
- evidence: Cited lines.
- refuter: I checked both sides and they hold.

f1's side (jlens-qwen36/scripts/f_sessions.py:597-607): the runner builds a fixed plan of n_of[c] sessions per contrast arm (from --n-arms or --n-contrast) plus --n-sham shams, sorted by fractional progress. The loop at :617 runs that list to its end. Nothing stops an arm at a floor, and no finite cell file exists that could run out. Session index s is unbounded and keys everything. PROPOSAL-f:64 mentions floors only as declarations; the runner has no floor-driven stop.

F0m's side, read at HEAD 5f7b968:
- schedule.py:102-116 is a Code PIN that materialises the campaign schedule to the k = 1 launch row: Q-F0 A0 2624 cells (82 units, used on both paths) and A0s 960.
- The committed data/m/schedules/Q-F0_campaign_A0.json and Q-F0_campaign_A0s.json hold n = 2624 and 960, matching their cell counts.
- stages.py:1812 sets n_sched from the committed files.
- At stages.py:1918-1923, an arm still in the rotation reaches the end of its file. Arms at their floor have already left the rotation (schedule.interleave, :418ff). It then records a pause of kind 'schedule_exhausted' and stops with status PAUSE.
- stages.py:1885-1892: after that pause, a resume carrying only an adjudication is refused. Only the PI's stop ends the campaign. So "for the PI" is correct.

The difference is observable: it changes how a session run is stopped once it is reached.

Classification: beyond the fourteen. Item (8) covers the committed balancing schedule against f1's per-index derivation, which is about how cells are assigned. It says nothing about the schedule being finite or bounding launches. Item (13) covers the strict two-arm rotation and the per-arm stop at floor, against f1's six-arm fractional interleave. It does not name exhaustion as a further stop or pause condition. The proposal's own terminal list (m:192 "floor, the unit's cap, or a PI stop"; m:247) does not name it either; it is a Code PIN at LOCK v0.1. It sits next to (8) and (13), but neither covers it.

On the effect, "None" is fair. The pause can only fire once an arm has used every cell in its file while still below floor: 2624 for A0 on either path (beyond the uncached k = 1 row of 2208), 960 for A0s. The only consequence is an arm left below floor and analysed as obtained, a terminal state m:247 already has. "Descriptive at most, if reached" would put it more exactly, but that is no reason to refute.

#### D29. (outside the delivery-rng lens) Primary domain: f1 analysed whole-session-valid sessions; m analyses sessions that reached the first read
- finder's classification: beyond; refuter: refuted=False, classification beyond (none of §2.7's fourteen covers it; it is disclosed only in §4, at m:308)
- f1: f_sessions.py:439 sets valid = not excluded; the primary at :461-462 and the sham pseudo-Δ at :454-456 use valid: 56 sessions, 28 P.
- F0m: scaffold.py:429-432 and :445: domain = reached the first read; first_free_pick_P is kept after a post-pick exclusion. m:308 states this: 58 sessions, 30 P.
- effect: Bears on A0's comparison with f1's primary: f1's figure of record is 28/56, while f1 under m's domain rule gives 30/58 (s4 and s25, excluded lexically at free4, both picked P first). It is disclosed at m:308 but is not among §2.7's fourteen.
- evidence: maps/f1.md section 3: 58 first reads, 30 P; 28/56 valid.
- refuter: I checked the claim against both codebases and the archive, and it holds.

f1's side: f_sessions.py:439 is `valid = [r for r in rows if not r.get("excluded")]`. The sham pseudo-Δ at :454-456 and the per-contrast primary at :461-462 both filter `valid`. PROPOSAL-f:101-102 frames the screen in valid sessions the same way.

F0m's side, at HEAD 5f7b968:
- scaffold.py:429-432 computes `domain` from the forced phase only. All 2F forced rounds must be present and unclaimed, there must be no forced hair trigger and no forced-phase exclusion. It asserts `domain == bool(self.choices)`, which is "reached the first read" (m:308).
- scaffold.py:445 sets `first_free_pick_P` whenever `domain` is true. So a session excluded at free (lexical@free, phase "free") keeps its pick, while `excluded` is True at :443.
- The built code already uses this rule. readrule.py `_sham_block` (:605-613, :643) counts the sham first-pick share over `_forced_domain` sessions, not over valid ones.
- m:308 declares the rule ("Nothing after the first pick removes a session from the domain"), quotes f1's 58 / 30 / two free4 post-pick exclusions, and gives "28/56 of record".

The archive confirms the numbers (my own count of data/f/sessions.jsonl):
- CORR has 64 rows. 56 are valid, with 28 P; 58 reached a first read, with 30 P.
- The two post-pick exclusions are s4 (`lexical:prism@free4`, swap True) and s25 (`lexical:maple@free4`, swap False). Both have first_free_pick_P True.
- So f1 under m's rule moves from Δ = 0 (28/56) to +.017 (30/58).
- The sham side moves too, from 18/33 valid to 19/34 reached (s35, `lexical:saddle@free5`, P first). That takes f1's pooled pseudo-Δ E from .045 to .059. This strengthens the effect claim; it is not in the claim's text.

Classification: none of the fourteen at m:267 covers it.
- (12) concerns the read window. It says only that the first-pick read was never clipped.
- (13) concerns the arm interleave and stop rule, not the analysis domain.
- The other twelve cover delivery, pools, audit, keys, assignment, verify cadence, lens, round path and generation window.

The difference is disclosed, but at m:308 in §4, outside the fourteen. So "beyond the fourteen" is correct as stated.

Effect: "bears on A0's comparison with f1's primary" is right. The domain rule changes f1's own primary figure (28/56 vs 30/58), and through the sham, E. This is the same kind of comparison §2.7 (12) and (14) say they leave unaffected.

Minor caveat: m's primary analyzer is not built at HEAD. The F0m domain side rests on m:308 plus the record fields and stage_report, which already implement the rule. That does not change the verdict.

#### D30. (outside the delivery-rng lens) A ban-list string in a free round stops m's session and stage; f1 logged it and continued
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:368-372: any free-round audit hit, special:{ban string} included, is post_degen and the session continues.
- F0m: runner_qwen.py:201-203: ra.scaffold (the v2 ban strings) fires the scaffold_absorption hair trigger and breaks; the stage stops (runner_qwen.py:24-27, m:271).
- effect: None at f1's observed rates: f1 CORR had 0 special: events (all 10 post_degen events and all 6 audit exclusions were frame:). It changes what continues if one occurs.
- evidence: The f1 CORR post_degen list recomputed from sessions.jsonl is all frame: classes.
- refuter: The claim holds. f1 side: in jlens-qwen36/scripts/f_sessions.py, audit_degenerate (:131-134) returns "special:{s}" for any string from the e2a ban list found in the text. In a free round, any deg value is only logged as choices_log[-1]["post_degen"] and the loop goes on (:368-372). f1's main run has no hair trigger on special: hits. checkpoint_eval (:389-433) has only the guard, lexical, cap and low-mass bars, and the audit "hair-trigger" in smoke_bar_check (:497-511) is a >20%-at-n>=6 smoke bar, not a one-hit stop.

m side at HEAD 5f7b968: valence_core/m/runner_qwen.py:201-203 calls log.hair_trigger(ra, "free") and breaks when ra.scaffold is set. The docstring at :24-27 says this stops the stage (m:271). audit.py:398-400 and :415-419 make ra.scaffold case-sensitive substring hits on v2's ban strings. Those strings come from data/configs/e2a_ban_list.json, which is byte-identical to f1's jlens-qwen36/data/configs/e2a_ban_list.json (sha256 9a2f0744...31c4), so f1 and m test the same strings with the same substring rule. The stop actually happens in the driver: stages.py _hair_hit (:1024) plus the break at :1352-1356 for gate stages, and :1936 for the campaign loop. m:271 says "a hair-trigger fire anywhere stops the stage".

The evidence also holds. I recomputed from data/f/sessions.jsonl: f1 CORR has 10 post_degen events, all frame:. Its exclusions are 6 audit:frame plus 2 lexical, so 0 special:. In fact there are 0 special: events in any of the 344 f1 sessions.

Classification: beyond. None of §2.7's fourteen covers it. Item (6) covers audit classes and claiming order, not a stage-stopping trigger. Item (13) covers arm interleave and per-arm stop at floor. The trigger is declared only in m:271's common bar conventions, outside the fourteen.

Effect is as stated: none at f1's observed rate (0 events). It is a stop-rule difference only. m keeps the session in the domain with no exclusion (see the runner self-test's hair_f case), so if one fires, A0's first pick is unaffected and only continuation changes.

One small extra the claim leaves out: in a forced round, f1 excludes on special: and moves to the next session, while m excludes (v2) and also stops the stage. The free-round claim stands as stated.

### Lens generation-reads

**Covered (the lens's own statement):** Lens: generation and reads. 17 differences: 12 beyond §2.7's fourteen and 5 covered (9, 10, 11, 12, 14).

Covered:
- (9): two forwards on every m read, against one forward on three-quarters of f1's reads.
- (10): f1's ea_mass forward.
- (11): cached iff G-ID passes, with m's uncached path being a full re-forward per step.
- (12): the 512-token read tail. m's new halt past 8192 tokens cannot be reached at F0m's lengths.
- (14): the 512-token generation tail and the two-chunk prefill, with a wording gap. (14) names only the cached path, but G-TIME-F0 (uncached by spec) and any G-ID FAIL also generate with no encode limit, and m asserts no generation window at all.

Beyond the fourteen, none bears on A0's comparison with f1's primary or any secondary:
- **Disclosure-grade:** jlens conditioning and forced_choice are loaded and run with empty fns, so f1's insulation-by-module-absence (PROPOSAL-f:58-59) does not hold for F0m.
- **No effect:**
  - Read softmax precision: f1 MLX float32, m numpy float64. Synthetic check: 0 pick differences in 400 trials. f1's 33 of 1,745 reads at p_a = 0.5000 are exact ties, decided in both by the shared menu-first tie rule.
  - Verify-KL precision.
  - The per-round boundary assertion.
  - The ban list's rebuild and asserts (bytes identical).
  - G-VER's check of each pick against its read.
- **Descriptive or stop-rule only:**
  - scaffold_absorption stops the session and the stage (f1 recorded post_degen and continued; 0 such events in f1).
  - stop_reason is recorded.
  - termination is recorded as a boolean rather than the matching pattern.
  - f1's pooled cap-hit monitor (p0 .10) and low-mass monitor (p0 .20) are not carried. The low-mass one is stated at m:283 but not in §2.7; neither bound in f1.
  - The read record is full precision with new fields, where f1 rounded to 4 dp.

Verified identical, no difference: sampling, TEMP 0.7, STOP_CAP 60, the newline/EOS stop (EOS banned in both), the read forward, the read position and labels, and the top-1 argmax.

**Internal, no effect (the lens's list):**
- MLX seed timing: f1 calls mx.random.seed after the prefill (f_sessions.py:168-169); m calls it before (qwen_mlx.py:268-269). The prefill draws no random numbers, so sampling is identical.
- Sampling is identical: float32 logits plus a -1e30 ban vector, then mx.random.categorical(lg/0.7) (f_sessions.py:174-181; qwen_mlx.py:279-290). TEMP is 0.7 in both (f_sessions.py:83; e2d/config.py:41 via runner_qwen.py:64).
- The stop rule is identical: stop on EOS or on a piece containing a newline after content_seen; the stop token is discarded; output is decode().strip() (f_sessions.py:182-191; qwen_mlx.py:292-305, :315-323, :343). The cap is 60 in both (f_sessions.py:82; session_e2a.STOP_CAP via runner_qwen.py:57, :160). cap_hit and n_tok are defined identically, and both make one wasted extend after the 60th token.
- The read forward is identical: MLXLensModel.forward(ids, capture_layers=[]) then unembed(final[:, -1, :])[0].astype(float32) (f_sessions.py:196-197; qwen_mlx.py:166, :171). m converts the logits to numpy via tolist, which is exact for float32.
- The read position and label-token convention are identical: the last position of transcript + menu, which ends 'Config choice (one word):', with label ids from encode(' '+t, add_special_tokens=False), single-token. f1 asserts single-token labels for its 8 tags at startup with a bare assert (f_sessions.py:573-577). m checks the session's own pair each session with SystemExit and also checks the ids are distinct (guard.py:141-157). The rosters differ, which is (5).
- The ban list and termination patterns are read from the clone in f1 and from the repo in m. The files are byte-identical [run].
- The top-1 flag is identical: MLX argmax and numpy argmax agree, ties included [run, argmax_tie.py].
- m's generate converts first_logits to numpy after generation (qwen_mlx.py:345-346). This does not affect the text.
- m's extra encodes (assert_boundary, prefix_tokens_at_read) are tokenization only, with no forward.
- On a construction incident, both runners raise SystemExit before the session is written, and the process stops.
- Library versions: in the jlens venv, the mlx 0.31.2, mlx-lm 0.31.3 and numpy 2.5.1 dist-info directories are dated Jul 16 2026. That is before f1's run (f_sessions.py mtime Aug 9; sessions.jsonl Aug 10), and they are unchanged since. f1 recorded no provenance, so its OS build cannot be recovered; m records adapter.provenance() (qwen_mlx.py:400-427).

#### D31. Intervention modules loaded in an F0m session; the insulation rests on a different basis
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:5-10 (docstring: the runner imports no intervention module, asserted at startup); :51-53 FORBIDDEN_MODULES = jlens_qwen.{fingerprint, forced_choice, interventions, conditioning, e2a, eval_awareness}; asserted absent at :527-528 and again after load at :586-587; PROPOSAL-f:58-59 ('startup assertion: no intervention/adapter modules active'). Cached rounds run in plain jlens_qwen.model.StreamSession (f_sessions.py:165), set to the ops kernel by hand (:166).
- F0m: valence_core/adapters/qwen_mlx.py:74-75 imports jlens_qwen.forced_choice and jlens_qwen.conditioning when the adapter is built. Cached rounds run in conditioning.SteeredStreamSession(model, {}) (qwen_mlx.py:309-313); uncached rounds run in forced_choice.forward_with_positional_state(..., {}) (:328-329). m asserts only valence_core.e2b.statepresent absent (guard.py:77, :119-121), at startup (runner_qwen.py:114), at each session start (:129) and before every read (guard.py:126). It adds the static AST call-site guard on injections=() and cached (guard.py check_call_sites).
- effect: None on the arithmetic. With empty fns, SteeredStreamSession.extend is StreamSession.extend line for line (conditioning.py:258-282 vs jlens model.py:296-321), and its __init__ switches back to the ops kernel (conditioning.py:254-255), as f1 did by hand. forward_with_positional_state with {} is MLXLensModel.forward (forced_choice.py:27-58 vs model.py:81-132). This is a disclosure: f1's property of being horn-free because the modules are absent (PROPOSAL-f:58-59) does not hold for F0m, whose insulation rests on injections=() plus the statepresent assertion.
- evidence: [read] code at HEAD 5f7b968 and in the jlens clone (read only). The same issue was flagged in maps/e2a.md F11.
- refuter: The claim holds on every substantive point. I read f_sessions.py in the jlens clone (read only), the jlens_qwen modules, and the m package at 5f7b968 using git show.

f1's side, all confirmed:
- f_sessions.py:5-10 is the docstring saying the runner is "HORN-FREE BY CONSTRUCTION" and imports no intervention module.
- :51-53 sets FORBIDDEN_MODULES to fingerprint, forced_choice, interventions, conditioning, e2a and eval_awareness.
- The absence is asserted at :527-528 (start of main) and again at :586-587 (after load).
- PROPOSAL-f-natural-reinforcer-screen.md:59 reads "startup assertion: no intervention/adapter modules active".
- gen_round runs a plain StreamSession (:165) and switches to the ops kernel by hand (:166).

F0m's side, all confirmed:
- qwen_mlx.py:74-75 imports jlens_qwen.forced_choice and jlens_qwen.conditioning in QwenMLXAdapter.__init__.
- Cached rounds build conditioning.SteeredStreamSession(model, {}) (:309-313). The induce_fns come from _induce_fns_flat over an empty placement, so they are {}.
- Uncached rounds call forced_choice.forward_with_positional_state with _positional_fns(()) = {} (:328-329).
- m's FORBIDDEN_MODULES is only valence_core.e2b.statepresent (guard.py:77, asserted at :119-121). It is checked at startup (runner_qwen.py:114), at session start (:129) and inside insulated_read.
- No file in valence_core/m or scripts/m_sessions.py asserts any jlens intervention module absent (git grep).

The effect claim also holds:
- With empty fns, SteeredStreamSession.extend (conditioning.py:258-282) matches StreamSession.extend (model.py:296-321) except for the `if i in self.induce_fns` branch, which is never taken.
- SteeredStreamSession.__init__ calls StreamSession.__init__, which enables the fused kernel, then switches back with set_inference_mode(False) (:254-255). That is what f1 did by hand.
- forward_with_positional_state with {} (forced_choice.py:27-58) matches MLXLensModel.forward (model.py:81-132) step for step.
- conditioning imports fingerprint only lazily inside functions, so loading the adapter brings in exactly two of f1's six forbidden modules: forced_choice and conditioning.

The difference is observable in the sense the task's definition covers ("verified"). f1's own insulation check, its forbidden-module assertion, would fail in an F0m Qwen process. f1's declared horn-free-by-absence property (PROPOSAL-f:59) does not carry over to F0m.

Three small points that do not refute the claim:
- guard.py:126 is the docstring of insulated_read; the assert_insulated() call is at :127.
- At HEAD the m package never builds the adapter itself, because the wiring is outstanding. The modules are loaded in an F0m session only once a QwenMLXAdapter is passed in. m:267 (naming qwen_mlx.py:307-313) and runner_qwen.py:94 both presuppose that adapter, and valence_core/adapters holds no other Qwen adapter.
- The uncached half (the forward_with_positional_state path) mostly belongs to item (11)'s round-path disclosure, since f1 ran only cached rounds.

Classification: beyond. None of §2.7's fourteen items names the dropped module-absence assertion or the loading of conditioning and forced_choice:
- (10) covers the lens read only.
- (11) covers the choice of path (cached iff G-ID passes).
- (14) covers the encode window and chunking.
F0m's side is stated elsewhere but never set against f1: §2.7's preamble names SteeredStreamSession with injections=(), and m:48 (§0.4) states the statepresent-only assertion. maps/e2a.md F11 independently reached the same conclusion. Effect: none on the arithmetic or on A0's comparison with f1's primary or any secondary. It is a disclosure item only.

#### D32. Choice-read softmax precision: MLX float32 in f1, numpy float64 in m
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:197-204: logits .astype(mx.float32); p = mx.softmax(logits) in float32; pick = a if pa >= pb; p_a = pa/(mass+1e-12); top-1 by mx.argmax.
- F0m: readout.py:44-48: float64 softmax after max-subtraction. readout.py:107-116: the same pick rule (ties to the menu-first label, :114), p_a and p_b = p/(mass+1e-12), np.argmax on the float32 logits. The logits come from the same MLXLensModel.forward + unembed + float32 cast (qwen_mlx.py:166, :171-173).
- effect: None on picks, so A0's comparison with f1's primary is unaffected. The model's dtype is bfloat16 (snapshot config.json), so two label logits are either exactly equal (a tie, which goes to the menu-first label in both) or at least one bf16 ulp apart, far above float32 resolution. Recorded p_a and label_mass differ only in low-order bits. The only theoretical divergence is both label probabilities underflowing to 0 in float32 (label logits about 88+ nats below the top-1). f1 would tie that to menu_a while float64 resolves it; f1's masses never come near it.
- evidence: [run] model-free synthetic checks. step5/genreads/softmax_pick.py: 400 trials on bf16-valued 248,320-logit vectors, 131 exact ties, 0 pick differences between f1's MLX-float32 form and m's float64 form. argmax_tie.py: MLX and numpy argmax agree on 300 of 300 tied maxima, both returning the first index. [run] archive: 33 of f1's 1,745 reads (7 of 346 CORR reads; 3 of the 58 CORR first reads, s4, s35 and s50) have p_a = 0.5000 at 4 dp, and all 33 picked the menu-first label. These are exact ties, decided by the tie rule both runners share (f_sessions.py:202; readout.py:114), that is, by the arm rng's menu-order draw.
- refuter: NOT REFUTED. The difference is real and every citation holds at HEAD 5f7b968.

f1's side: f_sessions.py:197-198 takes the logits, casts them to float32 and runs mx.softmax in float32. :200-204 then computes pick = tag_a if pa >= pb, p_a = pa/(mass+1e-12), and top-1 by mx.argmax. The CORR free reads go through this function at :354.

F0m's side: runner_qwen.py:181 calls guard.insulated_read, which calls readout.choice_read(verify=True). readout.py:44-48 is a float64 softmax after subtracting the max. :107-116 applies the same rule: ties go to label_a at :114, p_a and p_b = p/(mass+EPS), and top-1 is np.argmax over the float32 logits at :112. The logits come from qwen_mlx.py:166, then :171-173: the same model.forward, then unembed, then a float32 cast.

Reproduced checks:
- The claimant's softmax_pick.py gives 400 trials, 131 exact ties and 0 pick differences.
- The archive figures hold: 33 of 1,745 reads (7 of 346 CORR reads; 3 of 58 CORR first reads, s4, s35 and s50) have p_a = 0.5, and all 33 picked menu_a. No other p_a falls within 0.01 of 0.5, which fits bf16 granularity, so these are exact ties.

Classification: beyond the fourteen. No §2.7 item (m:267) covers the numerics of the choice read. Item (9) covers verify cadence, (10) the lens read, (12) the read window and (14) the generation window.

Two corrections to the effect text (minor; neither refutes the claim):

(1) "The only theoretical divergence is both label probabilities underflowing" is incomplete. There is a second regime with no underflow. When both label logits are near zero in absolute value, two neighbouring bf16 values sit closer together than float32 can resolve after the max is subtracted (|l| below roughly |max|*2^-16), so they collapse to the same float32 z. f1 then calls a tie and picks menu_a, while float64 separates them. Run in refute-softmax-prec/nearzero.py with max 30: label logits of 1e-5 and 3e-5 that are one bf16 ulp apart give f1 'a' and m 'b'. At 1e-4 the two runners agree. The phrase "at least one bf16 ulp apart, far above float32 resolution" therefore holds only when the label logits are not tiny compared with the max. This regime is practically unreachable on f1's archive: label_mass is at least 0.04 on every tie, and no p_a falls near 0.5 without being a tie. So "none on picks" for A0 vs f1's primary still stands.

(2) "Recorded p_a and label_mass differ only in low-order bits" ignores that f1 rounds both to 4 dp when it records them (f_sessions.py:363-364). m stores them at full precision (scaffold.py _read_dict, about :356-363). At record level the softmax-precision gap is masked on f1's side, except where a value sits on a 4-dp rounding boundary. The rounding itself is a separate difference, not this one.

Effect: none on A0's comparison with f1's primary. Descriptive only, at low-order bits.

#### D33. Verify-KL computation precision and bar form
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:205-215: second forward; KL in MLX float32 with eps 1e-12, max of the two directions; HALT (SystemExit) on kl != 0.0, which also halts on NaN or a negative value.
- F0m: readout.py:51-61, :117-119: KL in numpy float64, eps 1e-12, max of the two directions. readout.py:123-133: assert_construction_stable halts on > 0.0. guard.py:131-138 adds a halt unless the KL is a float exactly equal to 0.0 (NaN and negatives halt).
- effect: None. The bar is the same, exact zero. On bit-identical forwards both give exactly 0.0. m's float64 KL is more sensitive to drift below float32 resolution between the two forwards. Cadence is §2.7 (9); precision is not.
- evidence: [run] all 88 of f1's verified CORR reads have verify_kl 0.0. [read] code.
- refuter: The claim holds and every citation checks out. f1 side, jlens-qwen36/scripts/f_sessions.py:205-215: a second forward, then mx.softmax over logits cast to float32 (:207), eps 1e-12 (:208), the max of the two KL directions summed in MLX float32 (:209-211), and SystemExit when kl != 0.0 (:213-215). Because the test is !=, NaN and negative values also halt. F0m side at HEAD 5f7b968: valence_core/readout.py:44-48 casts to float64 before the softmax, and :51-61 computes the KL in numpy float64 with EPS 1e-12 and takes the max of the two directions. :117-119 re-forwards the same ids and stores symmetric_kl. :123-133 (assert_construction_stable, :130) halts only when the value is > 0.0, so NaN and negatives would pass there. valence_core/m/guard.py:72 imports these functions. :130-131 calls choice_read(verify=True) and then assert_construction_stable. :135-137 adds a halt unless type(kl) is float and kl == 0.0. The bar is therefore exact zero on both sides, and both halt on NaN and negatives. The evidence reproduces: data/f/sessions.jsonl has 88 CORR reads with a verify_kl (85 in non-excluded sessions, 3 in excluded ones), all exactly 0.0; every other CORR read has verify_kl None. Classification: none of §2.7's fourteen covers this. Item (9) covers only cadence (verify on every read against f1's verify_every), and no item mentions the precision of the verify computation. "Beyond" is correct. Effect "none" is right, but one phrase should be corrected. "Drift below float32 resolution between the two forwards" is imprecise. On both sides the logits are bf16 (the mlx-community Qwen3.6-27B-4bit config declares dtype bfloat16), cast to float32 the same way (f_sessions.py:197/207; qwen_mlx.py:171-173). Any drift from one forward to the next is therefore at least one bf16 step, and both sides see the same inputs. F0m's extra sensitivity lies only in the arithmetic after the cast: float64 against float32 softmax and summation, and where eps absorbs a value (about p < 6e-20 in float32 against about p < 1e-28 in float64). So F0m could halt on a drift that f1 would pass, but only in the far tail of the distribution. With bit-identical forwards both give exactly 0.0. A reasonable alternative is to list this as "internal, no effect". It is observable only as a counterfactual difference in when a halt fires, and the 88 f1 reads show none. A side note, not part of this claim: the same float64 shift also touches F0m's recorded p_a, p_b and label_mass and the pa >= pb tie test (readout.py:108-116, against f1's float32 values at f_sessions.py:197-203). That belongs with a read-precision item if no other lens reports it.

#### D34. Boundary assertion (re-encode and halt) before every generation
- finder's classification: beyond; refuter: refuted=False, classification beyond (it sits next to item (14), but item (14) does not cover it)
- f1: f_sessions.py:167-168 encodes prefix+segment as one string and prefills it as one chunk. No boundary is computed or asserted.
- F0m: scaffold.py:308-320: assert_boundary re-encodes the prefix and prefix+segment and raises SystemExit unless the token boundary equals the prefix token count. It runs before every forced round (runner_qwen.py:158) and every chosen round (:189). The adapter then recomputes the boundary for its two-chunk split (qwen_mlx.py:258-263).
- effect: None on bytes or tokens: it adds encodes only, no forward. It is a new halt condition f1 lacked (rule 28(d)(a)). The chunking itself is §2.7 (14).
- evidence: [read] code. [tok, from the build map] maps/e2a.md §2 item 1: on every m join shape the boundary equals the prefix length.
- refuter: The claim holds; I checked both codebases.

f1's side: jlens-qwen36/scripts/f_sessions.py:162-191 (gen_round) builds a fresh StreamSession and encodes prefix+segment as one string (:167). It prefills that in one extend (:168). No boundary is computed or asserted anywhere in the function.

F0m's side at HEAD 5f7b968:
- valence_core/m/scaffold.py:308-320 (assert_boundary) calls adapter.encode on the prefix and on prefix+segment, counts the common token prefix k, and raises SystemExit ("BOUNDARY INCIDENT (rule 28(d)(a)) ... HALT, escalate") unless k equals the prefix token count.
- runner_qwen.py calls it before both generate calls in the session loop: line 158, before the forced-round generate at :159, and line 189, before the chosen-round generate at :190. Those are the only two generate calls in the runner, so "every generation" is accurate.
- qwen_mlx.py:258-263 recomputes the boundary inside generate by the same token comparison. adapter.encode has no limit unless legacy_truncate is set (qwen_mlx.py:97-110), so the assertion compares untruncated encodes, as rule 28(d)(a) requires.

Effect:
- The assertion only encodes. It runs no forward and touches no RNG (mx.random.seed is set later, inside generate), so the bytes and tokens the model sees and produces are unchanged.
- It adds a halt condition f1 never had. That falls under "how sessions are stopped", so it is observable in principle.
- The build map (maps/e2a.md:69-70, :265, F13 at :288) records that every m join shape tokenizes with boundary equal to the prefix length. The halt is therefore not expected to fire, and the effect on the comparison with f1 is none.
- Negligible side effect: the extra encodes fall inside the perf_counter session seconds that feed the hour cap. That value is never printed.

One small imprecision, not enough to refute: the adapter's recomputed boundary drives a two-chunk prefill only on the cached path (qwen_mlx.py:310-313). On the uncached path it only places injections, and with injections=() there are none.

Classification: no item of §2.7's fourteen (m:267) mentions this assertion or halt. Item (14) discloses the generation window and chunking: f1's 512-token encode tail and one-chunk extend, against m's unlimited encode and two-chunk extend (qwen_mlx.py:307-313). It cites rule 28(d) only for the absent encode limit. The halt-on-mismatch is a separate stopping condition, so "beyond" is right. The chunking difference the claim mentions alongside it is item (14), as the claim itself says.

#### D35. Generation ban list: source, live rebuild and assertions
- finder's classification: beyond; refuter: refuted=True, classification beyond: none of the fourteen covers it ((6) is the audit's use of the ban strings, (14) is the generation window and chunking). But it is not a reportable difference. It belongs under "internal, no effect".
- f1: f_sessions.py:55-57, :550-551: ids and strings taken straight from the clone's data/configs/e2a_ban_list.json. They are applied to round sampling only (:175-180) and never in choice_read (:194-216).
- F0m: runner_qwen.py:68-88: the repo copy is loaded via build_ban_list(path=) and rebuilt from the live tokenizer; the two are asserted equal, and a missing file or a mismatch is a STOP. audit.py:59 and :67 pin the file's sha256; audit.py:223 assert_qwen_scaffold. Sampling only (qwen_mlx.py:282-287); readout.choice_read takes no ban.
- effect: None. The same 12 ids are banned and only at generation. Every special token, including the EOS <|im_end|>, is banned in both runners, so the EOS stop is unreachable in both.
- evidence: [run] sha256 of the repo copy and the clone copy are identical, 9a2f0744f81ac930...31c4. The 12 strings and ids were read from the file; the tokenizer config gives eos_token <|im_end|>.
- refuter: I refute this as a difference because nothing in a session can show it. The code-level facts mostly check out, but by the claim's own "Effect: None" the two runners ban the same ids in the same way. The task's own definition puts a change like this under "internal, no effect".

What I checked:
(1) Same bytes. sha256 is 9a2f0744...31c4 for the repo copy, the clone copy and `git show 5f7b968:data/configs/e2a_ban_list.json`. All three hold the same 12 strings and the same 12 ids (248044...248076).
(2) Same application. f1 is f_sessions.py:175-180. F0m is qwen_mlx.py:282-287, called with ban_ids at runner_qwen.py:160 and :191. Both add a -1e30 vector at sampling, temperature 0.7, only when ban_ids is non-empty.
(3) The ban never reaches a read on either side. f1's choice_read (:194-216) has no ban parameter. F0m's guard.insulated_read (guard.py:130) calls readout.choice_read(..., verify=True), whose signature has no ban.
(4) The new assertions only add refusal paths, and no real run takes them. The build's offline tokenizer check (maps/e2a.md:126, :276 F6) found the live rebuild equal to the file. The "missing file is a STOP" part is not new either: f1 also halts at :550, since json.load(open(BAN_PATH)) raises FileNotFoundError.

Factual errors in the claim:
(a) The effect line says "Every special token ... is banned in both runners". That is false. The local Qwen tokenizer.json flags 21 added tokens special=True, and the list bans only 10 of them, plus <think> and </think>, which are special=False. Eleven special-flagged tokens are not banned in either runner: <|object_ref_start|>, <|object_ref_end|>, <|box_start|>, <|box_end|>, <|quad_start|>, <|quad_end|>, <|vision_pad|> and four <tts_*>. The list is DEFAULT_SCAFFOLD_STRINGS plus the tokenizer's named special tokens (session.py:115-116). The narrower conclusion still holds: EOS <|im_end|> 248046 (tokenizer_config eos_token) is banned in both, so the EOS stop is unreachable in both.
(b) Citation slip: audit.py:67 is the path, E2A_BAN_LIST_PATH, not a sha pin. The pin is :59, and it is checked at :235-236 and :195-197. All other cited lines say what is claimed.

One observable piece the claim does not name: F0m records the ban ids' sha16 in the stage resume identity (stages.py:802-806, resume.py:94 and :453), and f1 records no ban hash. If this is listed at all, it is a recording item under resume identity, not this claim.

#### D36. A scaffold string in a generation now stops the session and the stage (scaffold_absorption hair trigger)
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:132-134: special:{s} comes first in the audit's precedence. A forced round's hit is an audit exclusion and ends the session (:339-345). A free round's hit is recorded as post_degen; the session continues and further reads are made (:368-372). The run never stops on it.
- F0m: runner_qwen.py:169-172: at forced, a v2 exclusion plus scaffold_absorption, then break. runner_qwen.py:201-203: at free, the hair trigger fires and the loop breaks, so no further reads or rounds. The stage then STOPs (bars.py:515-518; m:271).
- effect: Descriptive (a stop rule). No effect on the first pick: forced hits exclude in both, and free hits follow the first pick. In m, the positions after a free-round hit are lost and the stage halts. This was never realised in f1.
- evidence: [run] there is no special: claim and no special: post_degen in any of f1's 3,074 rounds (all arms). Banned ids are set to -1e30 at sampling, so only multi-token spellings could produce one.
- refuter: I checked both codebases and the claim holds. F0m code was read at HEAD 5f7b968.

f1's side. f_sessions.py:127-141 checks in this order: empty, then special:{s}, then frame, then junk. So "special comes first" is slightly loose, since "empty" is checked before it at :130-131. That makes no difference here, because a text containing a ban string is never empty. A forced-round hit sets excluded and reason audit:special@forced, then breaks (:339-345). A free-round hit is only written to choices_log as post_degen; the loop goes on with further reads and rounds (:368-372). Neither checkpoint_eval (:391-434) nor main (:617-683) stops on a single special hit. The only audit bar is the smoke-only rule that fires when more than 20% of at least 6 sham+P sessions are audit exclusions (:507). It is not a one-claim trigger, and it is not part of the run of record.

F0m's side, verified at HEAD.
- runner_qwen.py:168-173: at a forced round, qwen_ends leads to log.exclude. If ra.scaffold is set, the hair trigger is logged, stopped is set True, and the loop breaks.
- runner_qwen.py:199-203: at a free round, a scaffold hit logs the hair trigger and breaks, so no further reads or rounds run.
- audit.py:398-401, :458: scaffold hits are recorded as case-sensitive substrings of the e2a ban strings.
- Claims match f1's at both phases. AuditV3.check runs v2's AuditSpec.check first (audit_v3.py:50-53), with the same order as f1 (session.py:140-154). So the hit is a v2 claim of special:{s} in both: an exclusion at forced, and post-choice degeneracy (f1's post_degen) at free.
- bars.py:513-519 declares scaffold_absorption as a hair trigger with on_fire=_STOP. The stop itself is carried out in stages.py: the gate stage at :1352-1357, G-ID at :1541-1546 and the campaign at :1936. m:271 says "a hair-trigger fire anywhere stops the stage".
- The ban list is the same file in both: data/configs/e2a_ban_list.json, sha256 9a2f0744..., byte-identical to jlens-qwen36's copy.

The two real differences:
1. A free-round scaffold hit ends the session in m. In f1 it was logged as post_degen and the session ran on.
2. Any scaffold hit stops the stage or campaign in m. f1 never stopped on one.

Evidence (I ran it). data/f/sessions.jsonl has 344 sessions and 3,074 rounds across all arms. Its degen classes are frame 86 and junk 7. Its post_degen classes are frame 47 and junk 4. There are 0 special claims, 0 special post_degen entries, and 0 transcripts containing any ban string. The smoke file is the same: 205 rounds, 0 special. So the event never happened in f1.

Effect. The claim's effect is right: descriptive, and the first pick is unaffected. A forced hit excludes the session in both. A free hit comes after the read at ci=0. The cost in m is the lost later positions and a stopped stage, which then goes to the seat to adjudicate.

Classification: beyond. Item (6) covers how the audit classifies rounds (v3/v4/v5, echo, claiming order), not stop rules. Item (13) covers the interleave and the per-arm stop at floor, not hair triggers. No other item mentions scaffold_absorption or a stage or session stop on it. The proposal does declare it in §3 (m:271), just not among §2.7's fourteen.

Two citation nits, neither a refutation:
- The forced-round lines are 168-173, not 169-172.
- bars.py:515-518 is where the bar is declared; the stop is enforced in stages.py.

#### D37. Stop reason recorded per round
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:331-334: each round record holds cap_hit and n_tok. Why a round stopped (EOS or newline) is not recorded.
- F0m: qwen_mlx.py:318-319, :335-336, :347-348: stop_reason is one of cap, eos or newline. It is recorded per round (scaffold.py:391) and kept in stripped records (readrule.py:120-121).
- effect: Descriptive. The sampling and stop rule are otherwise identical, and 'eos' is unreachable in both (see the ban-list item).
- evidence: [read] code.
- refuter: The claim holds; I read both sides.

**f1's side.** In f_sessions.py, gen_round (:162-191) returns (text, n_tokens, cap_hit). It stops on eos, or on a newline once content has been seen (:183-186), and keeps no stop reason. The round record at :331-334 holds n_tok and cap_hit and no stop field. The archived data agrees. Across all 344 sessions in data/f/sessions.jsonl, the 3,074 round records carry exactly these keys: cfg, tag, task, seed, n_tok, cap_hit, lex, degen, term, graded and verdict. None has stop_reason.

**F0m's side, at HEAD 5f7b968.**
- qwen_mlx.py sets stop_reason="cap" by default (:275). The cached path (:318) and the uncached path (:335) both set it to "eos" or "newline", and it is returned at :348.
- The stop rule matches f1: eos, or a newline after content; runner_qwen.py calls generate with max_tokens=STOP_CAP 60 (:159, :190).
- scaffold.py:391 writes stop_reason into every round record.

**One citation nit.** readrule.py:120-121 is _FREE_ROUND_KEEP, the field whitelist for free rounds in redact_sham, the redacted sham form. The contrast form, strip_contrast, copies forced rounds whole (readrule.py:335), so stop_reason also survives there. It is kept in both blinded forms, so the substance is right; only the line is narrower than "stripped records".

**The effect is weaker than "descriptive".** In both apparatuses the generation ban list is the same e2a file (data/configs/e2a_ban_list.json, 12 ids). It includes `<|im_end|>`, which the tokenizer_config.json on disk names as the eos token, and `<|endoftext|>`. A ban adds -1e30 to the logit, so an "eos" stop cannot happen. That makes stop_reason a fixed function of cap_hit: "cap" when cap_hit is true, "newline" otherwise. f1's records hold the same information. The difference is a schema-level recording difference: observable as an added field, but with no effect on any comparison with f1.

**Classification.** None of §2.7's fourteen items (m:267) covers round-record fields. Items (11) and (14) are about the cached path, the encode window and chunking, not what a round record holds. "Beyond" is correct.

#### D38. Termination counter: which pattern matched is no longer recorded; tabulation keys changed
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:321-325, :333: the round record stores the first matching regex string (term). analyze tabulates (arm, cfg, round position) over all sessions (:447-453).
- F0m: scaffold.py:304-305, :392: a boolean termination flag. It is a declared counter keyed by (template, phase) (audit.py:91-93, :588-589) and is counted per phase in the stage report (readrule.py:522-540). Contrast free rounds are withheld at gate stages (readrule.py:565-585). The patterns file is sha-pinned (scaffold.py:65-66, :295-301).
- effect: Descriptive.
- evidence: [run] the repo and clone copies of f_termination_patterns.json are byte-identical (sha256 014b3940...2f46). f1's CORR archive has 9 termination rounds, all also frame-claimed by f1's audit.
- refuter: The claim holds. I checked every cited line against HEAD 5f7b968 using git show, and the f1 side in jlens-qwen36/scripts/f_sessions.py.

f1's side:
- At :321-325 the loop sets `term` to the first regex in TERM_REGEX that matches. At :333 that string goes into the round record as field "term", or None if nothing matched.
- analyze() at :447-453 counts term[(arm, cfg, pos)] over every row, excluded rows included, where pos is the index in rounds_log, which runs through forced and free rounds.

F0m's side:
- scaffold.py:304-305 defines `termination()` as `any(re.search(...))` and returns a bool. scaffold.py:392 stores it as "termination". So the field is renamed from "term" to "termination", and its type changes from str/None to bool. The counts come out the same, because "fires" means exactly what f1's "term is not None" meant.
- The declared counter key is (template, phase). See audit.py:91-93 and :588-589, and the PIN at audit.py:551-553: "never a tag, item, round index or property". Round position is gone, and so is cfg/property.
- In the stage report, readrule.py:522-540 (_round_counts) gives one count per rounds list. Its callers pass forced, free and all for the sham (:639-641) but only forced for the contrast (:580), and the contrast's free rounds come out as WITHHELD (:565-585).
- The patterns file is checked by sha16 and stops the run on a mismatch (scaffold.py:65-66, :295-301). f1 only printed the hash (:555-560).

What I ran:
- The repo copy and the clone copy of f_termination_patterns.json have the same sha256, 014b3940...2f46.
- The f1 archive (344 rows) has 9 termination rounds in CORR. All 9 have degen = frame:*. They sit in sessions 16, 25, 55, 58 and 61, at positions 2, 6, 7, 8 and 9.
- Across all arms there are 39 termination rounds, and every stored pattern is the first regex, '===\s*[Ee]nd'.

Small notes; none refutes the claim:
(a) The pattern-identity field is gone, but nothing is lost. F0m stores the full round text (scaffold.py:389) and pins the pattern file, so which pattern matched can be worked out after the fact. On f1's archive the field never varied anyway.
(b) The patterns file's own _doc says to tabulate "per arm x config x round-position". F0m's (template, phase) key departs from that. m:314 restores "by arm; by property in VERDICTS", but round position is not restored at any stage that is built.

Classification: beyond the fourteen.
- None of §2.7's items (m:267) is about the termination counter, its record field or its tabulation keys.
- The nearest is (6), the audit, which covers the audit version, the echo class and the claiming order. Termination is a separate descriptive counter that claims nothing.
- m:314 declares F0m's counter set but is not one of the fourteen disclosures.

Effect: descriptive. Termination is non-gating on both sides and does not affect exclusion, the primary or any secondary.

#### D39. f1's pooled cap-hit monitor is not carried
- finder's classification: beyond; refuter: refuted=False, classification beyond (none of §2.7's fourteen at m:267 is about monitoring or pause bars; the proposal does state the absence elsewhere, at m:358 step 11, "No cap trigger in Q-F0", so this is beyond the fourteen but already acknowledged in the proposal, not something new the port revealed)
- f1: f_sessions.py:416-433 (GUARD_CHECKPOINTS :90): a pooled exact-binomial monitor of cap hits over all rounds of all six arms against p0 .10, PAUSE at p < .05. It is evaluated when any arm reaches n = 24 and at completion. A smoke cap bar exists at :509-510.
- F0m: cap_hit is recorded per round (scaffold.py:390), counted (audit.py:586-587) and reported in the stage report (readrule.py:537). QF0_BARS has no cap bar (bars.py:513-582); m:358 step 11 says there is no cap trigger in Q-F0.
- effect: Descriptive (monitoring and stop rule only; no verdict effect). It never bound in f1.
- evidence: [run] 14 cap hits in 3,074 rounds pooled (p near 1 against .10). CORR: 2 of 597 rounds, both Q-role (s46 round 0, s58 round 2, 60 tokens each).
- refuter: The claim is factually correct. On f1's side, f_sessions.py:416-433 computes cap_x = sum(n_cap_hits) over cap_n = sum(n_rounds) for every row in sessions.jsonl. That covers all six arms, the sham included, and excluded sessions too. It runs binom_p_ge(cap_x, cap_n, 0.10) and adds the pause "pooled CAP" when p < .05. The caller treats any pause as a stop: CHECKPOINT PAUSE then return at :664-670, COMPLETION FLAGS at :672-677. GUARD_CHECKPOINTS = (24,) is at :90. The smoke cap bar at :509-510 is a ratio bar: caps/rounds > .10 once rounds >= 10, on the sham+P domain.

On F0m's side at HEAD 5f7b968, cap_hit is recorded per round (scaffold.py:390), counted as a declared counter (audit.py:91 and :586-587) and reported in the stage report's _round_counts (readrule.py:537 and :540). A git grep of the whole m package for cap_hit, cap-hit and cap hit finds no bar. QF0_BARS (bars.py:568-591, built from the helpers at :513-565) holds only the hair triggers, round_degeneracy at G-TIME-F0 and at G-F0m-Qwen, gid_divergence, and the campaign degeneracy and Fisher/absolute guard bars. The proposal agrees: §6 (m:330) lists no cap bar, the only cap trigger is Q-F3's reasoning-line one (m:174), and m:358 step 11 says "No cap trigger in Q-F0". So the difference is real and observable: f1 could pause on cap hits, and F0m can only count them.

I reproduced the evidence from data/f/sessions.jsonl (344 rows). Pooled cap hits are 14 of 3,074 rounds, a rate of about .0046 against p0 .10, so p is essentially 1. CORR has 2 cap hits in 597 rounds: session 46 at round index 0 and session 58 at round index 2. Both have cfg "Q" and n_tok 60. The rounds carry a field named cfg, not role, so "Q-role" is a loose name for the same thing.

The effect is descriptive only, as claimed: it touches monitoring and the stop rule, not any verdict, and at these rates the bar could never have fired in f1.

Three small imprecisions, none a refutation:
1. The pooled check runs when any of the five CONTRAST arms (not the sham, so not "any arm") has exactly 24 rows, or at completion. The pooled block is not de-duplicated, so it can re-run while an arm stays at 24.
2. The cited range bars.py:513-582 covers the helper functions and part of _qf0_bars; QF0_BARS itself spans :568-591.
3. Classification: "beyond" is correct, since nothing in (1)-(14) mentions monitors, bars or pauses. The G-PORT entry should still cite m:358 step 11 (and m:174 for the Q-F3-only cap trigger) as the place where the proposal already states this.

#### D40. f1's pooled low-label-mass monitor is not carried; m's flag uses the unrounded mass and a different report scope
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f_sessions.py:425-433: a MASS monitor of label_mass < 0.2 against p0 .20 over all reads of all arms, PAUSE at p < .05. It is evaluated on the stored label_mass, which is rounded to 4 dp (:363), at the n = 24 and completion checkpoints.
- F0m: scaffold.py:408 flags low_label_mass = label_mass < 0.20 on the unrounded value (LOW_LABEL_MASS imported at runner_qwen.py:55). It is a declared counter (audit.py:591-592) with no bar (bars.py:513-582). Reported scope: all sham reads; first reads of domain sessions for a contrast arm at campaign looks (stages.py:1705-1721); withheld for contrast sessions at gate stages (readrule.py:565-585). m:283 states that f1's p0 .20 monitor is not carried; §2.7 does not list this.
- effect: Descriptive. f1's monitor never bound, and the 4-dp rounding edge never occurred.
- evidence: [run] 165 of 1,745 reads pooled (p near 1 against .20); CORR 42 of 346 reads. No read anywhere in f1 has label_mass exactly 0.2000 at 4 dp.
- refuter: Not refuted. One sub-clause about m's report scope needs a correction.

f1 side, confirmed in /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/scripts/f_sessions.py:
- :363 stores `round(ch["label_mass"], 4)`.
- checkpoint_eval (:391-434) re-reads the jsonl. At :426 it counts `c["label_mass"] < 0.2` on those stored, rounded values, over every choice of every row (all arms, sham and excluded sessions included).
- :427 tests the count with binom_p_ge(..., 0.20). :431-433 appends "pooled MASS" to the pauses when p < .05.
- The pooled block runs at completion, or whenever any contrast arm's n is in GUARD_CHECKPOINTS = (24,) (:90, :416-417). It runs only outside smoke mode, from :664 and :672.

F0m side, confirmed at 5f7b968:
- scaffold.py:408 sets `low_label_mass = bool(read["label_mass"] < low_mass)`. The value comes from _read_dict (:356-363) as float(ChoiceRead.label_mass). Neither _read_dict nor readout.py:81 ChoiceRead.as_dict rounds it, so the flag uses the unrounded value.
- runner_qwen.py:55 imports LOW_LABEL_MASS from e2d/runner.py (0.20), and :187 passes it in.
- audit.py:591-592 is a counter only.
- bars.py has no mass bar anywhere. Its only "mass" is the binomial tail-mass docstring at :231. The :513-582 range holds only hair triggers, the degeneracy bars and the guards.
- Campaign looks (stages.py:1705-1721, :1750) report the sham arm over all reads and the contrast arm over the first read of each domain session.

Correction: "withheld for contrast sessions at gate stages" is wrong for the qual gate, which is the stage m:283 governs.
- stage_report's contrast block (readrule.py:565-585) does carry no read flags; it marks free_rounds as WITHHELD.
- But _finish_gate adds `contrast_first_read_flags` when gate == "qual" (stages.py:1421-1422, built at :1360-1369 via _read_flags with first_only=True). So at G-F0m-Qwen the contrast arm's first-read low-mass and top-1 flags are reported.
- They are withheld only at the other gate stages (G-TIME).
- The difference from f1 still holds: f1 pooled all reads of all arms against a bar, while m reports per arm and per template, contrast arm on first reads only, with no bar.

Evidence, recomputed from data/f/sessions.jsonl: 344 rows; 165 of 1,745 reads pooled below .2; CORR 42 of 346. No stored label_mass equals 0.2 exactly, so no unrounded value in [0.19995, 0.2) was rounded across the threshold, and the 4-dp edge never occurred. CORR first reads are 26/58 low-mass and 58/58 top-1-not-a-label, which matches m:283's [C]. 165/1,745 ≈ .095 against p0 .20, so the monitor could not have fired. The effect is descriptive.

Classification: beyond §2.7's fourteen. No item (1)-(14) at m:267 mentions the pooled label-mass monitor; item (10) concerns ea_mass, the lens read. It is disclosed elsewhere, at m:283 ("f1's binomial monitor at p0 .20, archive:404, is not carried"), which the claim itself notes. The rounding and scope details are disclosed nowhere.

#### D41. Read record: fields and precision
- finder's classification: beyond; refuter: refuted=False, classification beyond. Two parts of it follow from listed items: verify_kl appearing on every read is a consequence of (9), and f1's `ea` field having no counterpart in m is (10). The core of the claim is in none of the fourteen: the 4-dp rounding, the added fields (p_b, top1_id, menu_b, menu bytes, menu_index, prefix_tokens_at_read, low_label_mass, top1_not_label), and m nesting the read under "read". Item (12) covers the read window, not whether a prefix length is recorded.
- f1: f_sessions.py:361-367: choices[] holds round, menu_a, pick, picked_cfg, label_mass and p_a rounded to 4 dp, top1_is_label, verify_kl (None when not verified) and ea. There is no p_b, top1_id, menu_b or prefix length.
- F0m: scaffold.py:356-363: the read dict at full precision (pick, p_a, p_b, label_mass, top1_id, top1_is_label, verify_kl on every read). scaffold.py:398-411 and runner_qwen.py:183 add menu_a, menu_b, the menu bytes, menu_index, prefix_tokens_at_read (an extra encode of transcript + menu), low_label_mass and top1_not_label.
- effect: Descriptive. Any comparison of read values with f1 holds only at 4 dp. f1's clipped-read count in §2.7 (12) had to come from a tokenizer recount, because f1 recorded no prefix length.
- evidence: [read] code. [run] the f1 choice key set has 9 keys plus an optional post_degen (maps/f1.md §3).
- refuter: I checked this against HEAD 5f7b968 and the f1 archive, and every factual part of the claim holds.

f1's side:
- f_sessions.py:361-367 appends round, menu_a, pick, picked_cfg, label_mass, p_a, top1_is_label, verify_kl and ea. label_mass and p_a are rounded to 4 dp, ea to 6 dp.
- verify_kl comes from ch.get(), which gives None unless the read was verified (:211-212).
- post_degen is added only on a degenerate round (:372).
- My own pass over data/f/sessions.jsonl agrees: 1,694 choices carry exactly those 9 keys and 51 carry post_degen as well. verify_kl is None on 1,312 choices and a float on 433. p_a shows at most 4 decimals.
- None of p_b, top1_id, menu_b or a prefix length is recorded.

F0m's side:
- scaffold.py:356-363 (_read_dict) records pick, p_a, p_b, label_mass, top1_id and top1_is_label as unrounded floats, plus verify_kl.
- verify_kl is always present, because guard.insulated_read calls choice_read with verify=True (guard.py:130) and ChoiceRead.as_dict includes the field whenever it is not None.
- scaffold.py:398-410 (add_choice) adds ci, n, menu_index, menu (the menu bytes), menu_a, menu_b, picked_role, picked_pole, prefix_tokens_at_read, low_label_mass and top1_not_label.
- runner_qwen.py:183 does the extra encode of transcript + menu that supplies the prefix length.
- I searched scaffold, runner_qwen, resume, stages and verify for rounding of read values and found none; the record is passed through json.dumps (scaffold.py:448) with nothing rounded.

The effect claim also holds:
- f1's clip count of 75 reads cited in (12) comes from RESULTS.md@e186162:10006-10010, the window-coverage audit. That audit re-tokenised every archived choice-read prefix, which fits f1 never having recorded a prefix length.
- A0's primary depends only on the pick, so the difference is descriptive.

One addition the claim leaves out: m's readout.py:113 and :118 also nest the read and compute softmax in float64 numpy. f1 (:197-199) computes softmax in float32 MLX. So read values agree only to f1's 4 dp and float32 precision, and a near-tie pick could in principle differ. That is a separate computation difference; it does not refute this claim.

I would not count the classification as wrong because of the (9) and (10) overlaps. Those cover the verify cadence and the lens read, not the record's fields or precision.

#### D42. G-VER checks each recorded pick against its recorded read (new stop condition)
- finder's classification: beyond; refuter: refuted=False, classification Beyond the fourteen for the pick-against-read check. The verify-KL clause inside it is not new in kind and partly overlaps item (9), the verify cadence.
- f1: f_sessions.py:356-358: the pick line is written straight from the read. There is no post-session check of picks against reads.
- F0m: verify.py:184-200: after the session, each recorded pick must be menu_a iff p_a >= p_b (either label is accepted on exact equality), and verify KL must be exactly 0.0. Otherwise it is template_breakage, a hair trigger that STOPs the stage (bars.py:520-522).
- effect: None on picks. It is a consistency check on the record that adds a stop condition.
- evidence: [read] code.
- refuter: The claim holds up against both codebases at HEAD 5f7b968.

f1's side: f_sessions.py:356-358 sets picked = ch["pick"] and writes the line menu + f" {picked}\n" straight from choice_read, where the pick is tag_a if pa >= pb (:202). Neither f_sessions.py nor f_postscreen_descriptive.py rechecks picks against reads after a session; the post-screen script only reads first_free_pick_P.

F0m's side, in git show 5f7b968:valence_core/m/verify.py:
- :186-187: the pick must be a menu label and must equal read.pick, otherwise BREAK.
- :195-199: p_a and p_b must be floats; p_a > p_b requires menu_a and p_a < p_b requires menu_b. On exact equality either label passes, as the claim says.
- :200-201: verify_kl must be a float exactly equal to 0.0, otherwise BREAK.
- stages.py:1006 runs this through verify_and_mark after run_session_qwen; :1016 maps the failure to template_breakage or schedule_mismatch.
- bars.py:520-522 declares template_breakage as a hair trigger ("sessions failing G-VER", on_fire=_STOP).

So the cited lines say what the claim says, and the difference is observable: there is a new verification step and a new stop condition.

Two qualifications, neither enough to refute:

(1) The KL clause is not new in kind. f1 already halted inline on a nonzero KL (f_sessions.py:213-215, SystemExit when kl != 0.0), but only on reads chosen by verify_every: 4 in production (:608), 1 in smoke (:595). F0m also halts inline on every read (guard.py:130-136, insulated_read). What is new is reading every verify_kl, which is item (9)'s cadence. G-VER's KL clause just re-checks that on the record.

(2) On a genuine record the pick-against-read check cannot fire. readout.py:114-115 takes the pick from the raw pa >= pb and records p_a = pa/(mass+EPS) and p_b = pb/(mass+EPS). Dividing both by the same positive number cannot reverse their order, so the check fires only on a corrupted or edited record or a code bug. That matches the claim's stated effect: none on picks, a consistency check that adds a stop condition.

Classification: none of §2.7's fourteen (m:267) mentions G-VER or a check of picks against reads. Item (9) covers only choice_read(verify=True) on every read versus f1's verify_every. The check is therefore beyond the fourteen, with its KL clause overlapping (9).

#### D43. Read window: no encode limit, and a halt past 8192 tokens
- finder's classification: §2.7 (12); refuter: refuted=False, classification §2.7 (12)
- f1: f_sessions.py:195: jlens model.encode(text) with default max_length=512, keeping the tail (jlens model.py:74-79); clipping was silent.
- F0m: No encode limit (qwen_mlx.py:97-110 with legacy_truncate False). readout.py:101-106 and base.py:334-350 raise SystemExit past 8192 tokens at every read. runner_qwen.py:91-100: startup refuses any other window or any encode limit.
- effect: Covered by (12). The halting assertion is new but cannot be reached at F0m's lengths.
- evidence: [read] code. qwen_mlx.py:57-58 records that the longest archived e2a+f read prefix was 666 tokens.
- refuter: I checked every cited line and both sides hold. f1 side: jlens-qwen36/scripts/f_sessions.py:194-195 defines choice_read and calls model.encode(text) with no max_length. f1 imports load from jlens_qwen.model (:45, :569), so this is MLXLensModel.encode. In jlens-qwen36/jlens_qwen/model.py:74-79, encode defaults max_length to 512 and keeps the tail (ids[-max_length:]). f1 counts and records no clipping anywhere (no clip or prefix-length field in f_sessions.py), so the clipping was silent. The read is called at :354 on transcript + menu. F0m side, judged at HEAD 5f7b968: the only read m makes is guard.insulated_read (guard.py:124-138), which calls valence_core.readout.choice_read (imported at guard.py:72). That function encodes at readout.py:101 and asserts the window at :106. Its check, base.py:334-350, raises SystemExit("WINDOW INCIDENT") when n_tokens > choice_window. QwenMLXAdapter.encode (qwen_mlx.py:97-110) truncates only when max_length is set, and max_length is None unless legacy_truncate=True (:79-80). Its CHOICE_WINDOW is 8192 (:60), and it does not override assert_choice_window. runner_qwen.py:91-100 (assert_qwen_adapter, called from qwen_startup at :115) refuses a choice_window other than 8192 and refuses legacy_truncate or max_length. qwen_mlx.py:57-58 records the 666-token maximum archived prefix across e2a+f. On classification, §2.7 (12) (m:267) already says "m reads the whole session at 8192" against f1's 512-token encode tail at free positions 5-6. A declared 8192 window with no encode limit and no silent clip is exactly what that says. The halt past 8192 is how a declared window behaves on overflow, not a separate difference. It also cannot be reached in practice: an F0m session is the banner, 4 forced and 6 free rounds of at most 60 generated tokens each (STOP_CAP), plus menus, far below 8192. So the effect is the one (12) already discloses: A0 against f1's primary is unaffected, and only secondary (a)'s position 5-6 reads cross the window change. The claim is correct and correctly classified as covered by (12).

#### D44. Generation window on m's uncached path (and no generation-window ceiling at all)
- finder's classification: §2.7 (14); refuter: refuted=False, classification §2.7 (14), read with (11). Not beyond the fourteen. The only gap is wording: (14) is scoped to "on the cached path".
- f1: f_sessions.py:167: a 512-token tail on the one-string encode (jlens model.py:74-79). f1 never generated uncached.
- F0m: qwen_mlx.py:258-259, :324-340: the uncached path also encodes with no limit and re-forwards the whole sequence each step. No window is asserted anywhere in generate (qwen_mlx.py:242-348), unlike reads. G-TIME-F0 is uncached whatever is on disk (guard.py:225-226; m:280), and a G-ID FAIL sends Q-F0 uncached.
- effect: As in (14): none before the first pick, because f1's clipped generations were at round indices 8-9. Wording gap: (14) names only the cached path, while G-TIME-F0 and any G-ID-FAIL run generate uncached with the same unlimited window. The path switch itself is (11).
- evidence: [read] code. (14)'s 135 of 3,074 figure was not recomputed here.
- refuter: The claimed difference is factually correct on both sides. f1 side: f_sessions.py:162-168 gen_round always generates cached (StreamSession, one extend of the whole encode). It encodes prefix+seg through model.encode, and jlens_qwen/model.py:74-79 defaults max_length=512 and keeps the tail. Nothing in f_sessions.py generates uncached. F0m side, at HEAD 5f7b968: qwen_mlx.py:258-259 encodes prefix and prefix+segment once, before the cached/uncached branch (:307 and :324). So both paths use the same adapter.encode (:97-110), which clips only under legacy_truncate (max_length is None otherwise). runner_qwen.py:91-100 refuses at startup any adapter that carries legacy_truncate or max_length ("m generates with none"). The uncached branch (:324-340) re-forwards the whole growing sequence through forward_with_positional_state at every step, with no encode in between. Nothing in generate (:242-348) asserts a window. Reads do assert one: guard.insulated_read calls readout.choice_read, which runs adapter.assert_choice_window at readout.py:106; guard.py:1432-1433 is the overflow self-test. guard.py:225-226 returns False for stage "time" whatever is on disk, matching m:280 "G-TIME-F0 (Qwen, uncached)". m:267 makes a G-ID FAIL send the unit uncached. So the uncached path, like the cached one, has no generation-encode limit, where f1 had a 512-token tail. The effect stated ("none before the first pick") is consistent with (14)'s own figures, which I did not recompute. Classification: this is not a new difference. The 512-tail-versus-no-limit contrast is a property of the shared encode, and (14) discloses it. (11) discloses the cached/uncached switch, and with it the absence of chunking on the uncached path, which is whole-sequence re-forwarding. The claim's own label, "covered by (14), wording gap", is right. Strictly, (14)'s title and its m-side clause ("m's cached path has no encode limit") name only the cached path. That leaves G-TIME-F0 and any run after a G-ID FAIL outside the letter of (14), though not outside its substance. A minor caveat on the "no generation-window ceiling at all" sub-claim: it is literally true but practically unobservable. Every forced-round prefix is shorter than the first read prefix. Every free-round prefix plus segment is the read prefix just checked against 8192, plus the pick (" {pick}\n") and the segment, with at most 60 generated tokens after it (STOP_CAP). So no realistic F0m generation can exceed the window the reads enforce.

#### D45. Two forwards on every read
- finder's classification: §2.7 (9); refuter: refuted=False, classification §2.7 (9)
- f1: f_sessions.py:353: verify only when (s*6+ci) % verify_every == 0, with verify_every 4 (:608). Unverified reads make one forward.
- F0m: guard.py:124-138: choice_read(verify=True) on every read, so two forwards every time.
- effect: Covered by (9). Reads are deterministic, so the extra forward changes nothing.
- evidence: [read] code.
- refuter: The claim is correct, and its classification is right. On f1's side, f_sessions.py:353 sets verify = ((s * N_FREE + ci) % verify_every == 0), and N_FREE = 6 (:86). verify_every is 4 on the non-smoke path (:608); the smoke path uses 1 (:595), which the claim leaves out, but the archived run is non-smoke. f1's choice_read (:194-216) makes one forward, plus a second only under verify (:205-206), and halts if kl != 0.0. A recount of data/f/sessions.jsonl matches this: 1,745 reads, 433 carry verify_kl, and 0 depart from the (s*6+ci)%4 cadence. One small point: every f1 read also ran a separate ea_mass forward (:355). That is item (10), not this one, so "unverified reads make one forward" holds for the choice read itself. On F0m's side, at HEAD 5f7b968, guard.py:124-138 is insulated_read, which calls choice_read(..., verify=True) at :130. readout.choice_read:117-119 runs a second adapter.forward on the same ids when verify is set. runner_qwen.py:181 (and runner_olmo.py:157) send every read through guard.insulated_read, so every read takes two forwards and must give KL exactly 0.0. scaffold.py:71 and :499 encode f1's cadence (F1_VERIFY_EVERY = 4, (s*6+ci)%4) only to rebuild f1's records for comparison. §2.7 item (9) names this exact difference ("choice_read(verify=True) on every read against f1's verify_every"), so it is COVERED by (9), not beyond it. The effect is "none": the second forward re-reads identical ids, so the pick, p_a and label_mass are unchanged. The only observable change is that verify_kl is recorded, and checked for a halt, on every F0m read instead of on 433 of f1's 1,745.

#### D46. Extra per-choice lens forward (ea_mass)
- finder's classification: §2.7 (10); refuter: refuted=False, classification §2.7 (10)
- f1: f_sessions.py:219-231, :355: a further forward over transcript + menu with workspace-layer capture after each read. It consumes no rng.
- F0m: runner_qwen.py:180-183: no other forward; the only additions are encodes.
- effect: Covered by (10). It changes no pick or seed in either runner.
- evidence: [read] code.
- refuter: The claim holds and is not refuted; it is covered by §2.7 (10), as the claim says.

f1's side: `ea_mass` is defined at f_sessions.py:219-231. It encodes `transcript + menu` and runs `model.forward` with `capture_layers=list(WORKSPACE_LAYERS)`. It applies `lens.transport` where a Jacobian exists, then unembeds and averages the marker-token mass across the layers. It is called at :355, right after `choice_read` at :354, on the same `transcript + menu`. Its value is logged as `ea` in choices_log. All 1,745 archived f1 reads in data/f/sessions.jsonl carry the `ea` field, so the difference shows in the record. The function touches no rng. It runs after the pick is computed (:354, :356), so it changes no pick, no menu order and no seed.

F0m's side, at HEAD 5f7b968: runner_qwen.py:180-183 builds `read_prefix`, calls `guard.insulated_read` (guard.py:124-138), and then only calls `adapter.encode` for `n_prefix`. `insulated_read` calls `readout.choice_read(verify=True)` (readout.py:90-120): two forwards over the same ids, both with `capture_layers=()`, with no lens and no capture. A search of every m module and scripts/m_sessions.py at HEAD finds no lens, `ea_mass`, `WORKSPACE_LAYERS` or `capture_layers` use. The only `capture_layers` hit is a self-test stub in guard.py:1357.

Two wording points, neither of which makes the claim wrong. "No other forward" holds only in the sense of no forward besides the read: the read itself makes two forwards because of verify. The verify cadence difference is §2.7 (9), not this item.

Classification: §2.7 (10) at m:267 reads "no per-choice lens read (f1's `ea_mass`, :219, :355; m reads nothing but the vanilla choice read)". That matches this difference exactly, so it is not beyond the fourteen. Effect on the comparison with f1: none on picks, seeds or the primary or secondaries. The only effect is descriptive: m's choice records have no `ea` field.

#### D47. Uncached generation is a full re-forward per step
- finder's classification: §2.7 (11); refuter: refuted=False, classification §2.7 (11)
- f1: f_sessions.py:162-191: always cached on the ops kernel.
- F0m: qwen_mlx.py:324-340: with cached=False, forward_with_positional_state over the whole sequence for each sampled token. cached is chosen only by guard.cached_path_admitted (guard.py:208-228), which requires a G-ID PASS on this backend.
- effect: Covered by (11).
- evidence: [read] code.
- refuter: I checked both sides against HEAD 5f7b968 and neither is wrong.

f1's side holds. gen_round (f_sessions.py:162-191) is f1's only generation path; its one call site is :313. It always generates cached: a StreamSession that extends prefix+segment once (:165, :168), then one token per step (:190). It runs on the ops kernel because set_inference_mode(False) is called at :166 and again at :570.

F0m's side holds. In qwen_mlx.py (unmodified in the working tree) the `else:` branch at :324-340 calls forward_with_positional_state on the whole growing sequence at every step, with `ids` concatenated at :340. That is a full re-forward per token. The cached branch is :307-323. The adapter sets the same ops kernel at :94, so the kernel matches f1's and only the path differs. The difference can be seen in the outputs: cached and uncached numerics can give different samples (which is what G-ID tests), and the path is recorded on each session.

The licensing claim is accurate for A0/A0s sessions but slightly overstated as written. It is true that runner_qwen takes path_cached from the stage driver (stages.py:1316, :1818 via guard.cached_path_admitted) and checks the licence again at runner_qwen.py:143. It is also true that cached_path_admitted (guard.py:208-228) needs a well-formed G-ID PASS whose backend_identifier matches this backend (_gid_pass :181-205). But it is not the only source of the path. At the G-TIME stage it returns False whatever is on disk (:225-226). At G-ID the path comes from gid_paths()/run_gid_pair (guard.py:173, stages.py:1530), not from this function. This does not change the claim.

Classification: §2.7 (11) reads "the round path — cached iff G-ID passes (f1 ran cached; the recon and Stage 1 uncached)". The uncached path is that same re-forward path, so the claim is covered by (11) and is not a new difference beyond the fourteen. The backend-match condition is an F0m-internal build PIN on (11)'s licence, not a separate difference from f1. The cached path's two-chunk extension and its lack of an encode limit belong to (14), not to this claim.

One more note: the effect field only repeats the classification. The actual effect is a numerics/path change that G-ID exists to certify.

### Lens audit-exclusion

**Covered (the lens's own statement):** I compared f1 and m (HEAD 5f7b968) across audit and validity. I read f1's audit and validity apparatus: f_sessions.py:93-494 and :497-683, PROPOSAL-f:53-115, and archive/RESULTS-cycles3-4.md:78-95 and :398-404. On the m side I read audit.py, runner_qwen.py, scaffold.py (SessionLog and the termination helpers), readrule.py (printing and stage reports), bars.py (hair triggers, degeneracy, the guard, the boundary), stages.py (_hair_hit, _prepick, campaign_look, the campaign loop) and verify.py's end-rule checks. I also read the spec at m:261-271, m:306-318 and m:330. I checked that the working tree matched HEAD for those modules before importing audit.py and scaffold.py, with PYTHONDONTWRITEBYTECODE=1. No model or tokenizer was loaded.

Scope: every audit class and its precedence, session ends at forced and free rounds, the hair trigger, the lenient and strict scopes, the content classes and advisories, the lexical scope, the echo class, the valid-session and domain rule, the per-property table, the counters, and the exclusion-based monitors. OLMo is out of scope.

Every number is a post-hoc, descriptive, model-free recount of f1's archive. Scratch scripts are in /private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/audit-exclusion/: f1_domain.py, m_on_f1.py, find_content.py, s48.py, asym.py and junk.py. These replay f1's 64 CORR rows through scaffold.f1_config and classify each archived round with m's QwenTaskRoundAudit, which needs the clone-only f_audit_patterns.json only for the junk.py probe.

Main finding beyond the fourteen: f1's primary, sham envelope and by-map conjunct all run on whole-session validity, while m's run on the pre-read domain. On f1's own archive that is 28/56 against 30/58 (sham 18/33 against 19/34). m:308 states it, but §2.7 does not list it. Under m's audit stack the archive's domain becomes 28/56 again, but over a different set of sessions: s25 and s48 drop out on forced-round v4 content claims. corrupt_m's verb hits on items 5, 11 and 15 give v4/v5 a clean-only exclusion path; this does not occur with f1's renders. Minor corrections to maps/f1.md and maps/audit.md: post_degen is 10 events in 5 sessions, not 6; the forced-round property split is clean 127 rounds and corrupted 124, not 110 and 141.

**Internal, no effect (the lens's list):**
- lexical_hit tag order: f1 checks [tag_P, tag_Q] (f_sessions.py:279) and m checks (sc.P, sc.Q) (runner_qwen.py:147). The function body is identical (session.lexical_hit), and the reported tag is never printed.
- f1 computes `oop` (f_sessions.py:280) and never uses it; m computes no out-of-pair set. Lexical scope is the own pair in both, so out-of-pair mentions are unscored in both.
- A free-round lexical exclusion ends the session after that round is recorded in both: f1 at the next iteration's check (f_sessions.py:348-349), m by break (runner_qwen.py:199-205). Neither makes an extra read.
- The choice entry is appended after the chosen round in f1 (f_sessions.py:361) and before its generation in m (runner_qwen.py:187); the content is the same.
- Text stripping and the 'empty' class are identical: decode(...).strip() at f_sessions.py:191 and qwen_mlx.py:343; AuditSpec 'empty' = not text.strip().
- AuditV3 does not run v5 when v2 hits, so v2-claimed rounds carry no advisory (internal to (6)).
- m refuses an item/render mismatch and a malformed echo set (audit.py:428-439, :171-181). These are assertions with no observable effect on valid input.
- G-VER re-derives the exclusion, strict, hair-trigger, domain and first-pick fields from the recorded claims; it does not re-run the audit on the text (verify.py:225-254). The audit's correctness rests on the runner (verify lens).
- Counter keys never carry a tag, item, round index or property (audit.py:551-553), and an unparsed v2 reason is counted as 'unparsed' (readrule.py:104-107). These are blinding mechanics.
- domain == bool(choices) is asserted (scaffold.py:431-432; verify.py:251-253). This equals f1's 'first_free_pick_P not None' for sessions that reached a read.
- The v5 'others' pool is the clean text of the other 15 items (audit.py:291-305, PIN D4). It feeds only the advisory wrong_task, so nothing excludes on it (§2.6 m:261, covered by (6)).

#### D48. Primary-domain rule: f1's whole-session validity vs m's 'reached the first read' domain
- finder's classification: beyond; refuter: refuted=False, classification beyond (not among §2.7's fourteen, m:267). The design states it in §4 at m:308, with the 58/30 vs 28/56 figures, so it is a declared design difference that §2.7's list leaves out, not a defect the port uncovered.
- f1: f1's primary, the sham envelope and the by-map conjunct are all computed on `valid` = never excluded over the whole session. Sources: jlens-qwen36/scripts/f_sessions.py:439 (valid), :454-457 (sham pseudo-delta), :461-462 (firsts), :467-473 (by_map). A free-round lexical exclusion removes the session even though its first pick came earlier (:373-375). Floors are 'valid-n floors' (PROPOSAL-f:64, :101-106). Record of the result: archive/RESULTS-cycles3-4.md:82 (CORR n=56, delta = 0.000).
- F0m: The primary is computed on `domain` = no exclusion-bearing event before the first read: valence_core/m/scaffold.py:429-432 and :445 (first_free_pick_P only if domain), with verify.py:251-254 asserting domain == 'reached the first read'. Spec: m:308 ('Nothing after the first pick removes a session'). The sham envelope uses the same rule (m:308). Whole-session validity is only reported beside it, although m:261 calls f1's rule 'of record'. Floors count domain sessions (stages.py:1906, :1935 in run_campaign).
- effect: Bears on A0's comparison with f1's primary. f1's own CORR archive gives different results under each rule. Under f1's rule (of record): 28/56, delta .000, map A 18/29, map B 10/27, sham 18/33, E = .045. Under m's domain rule with f1's audit: 30/58, delta +.017, map A 19/30, map B 11/28, sham 19/34, E = .059. Sessions s4 and s25 (lexical@free4, both clean first picks) and sham s35 (lexical@free5) come back in. m:308 quotes the 58/30 figure, but none of §2.7's fourteen items lists the domain change.
- evidence: Model-free recount of data/f/sessions.jsonl (scratch f1_domain.py): CORR valid 56, of which 28 picked P; 58 reached a read, of which 30 picked P. The by-map and sham figures are as stated. The free exclusions are [(4, lexical:prism@free4, P), (25, lexical:maple@free4, P)] and sham [(35, lexical:saddle@free5, P)].
- refuter: Every factual part of the claim checks out against both codebases (F0m judged at HEAD 5f7b968).

f1 side:
- f_sessions.py:439 sets `valid = [r for r in rows if not r.get("excluded")]`.
- The sham pseudo-delta (:454-457), the contrast firsts (:461-462) and by_map (:467-473) are all computed on `valid`.
- A free-round lexical hit sets excluded=True (:373-375) after the first pick has been recorded (:382-383 records first_free_pick_P whenever choices exist).
- PROPOSAL-f:64 says "valid-n floors", and :101-102 says "n = 48 valid sessions".
- archive/RESULTS-cycles3-4.md:82-85 gives CORR n=56, delta = 0.000, maps +.121/-.130, sham pseudo-delta .045.

F0m side:
- scaffold.py:429-432 defines `domain` as all forced rounds unclaimed, no forced hair trigger and no forced exclusion, and asserts that domain is the same as having reached a read.
- scaffold.py:445 gates first_free_pick_P on `domain`. verify.py:251-256 re-asserts both.
- runner_qwen.py:17-20 and :199-203: a free lexical claim ends the session as excluded@free but keeps it in the domain.
- The campaign floors in run_campaign count domain sessions (stages.py:1906, :1909, :1935), as does _campaign_report (:2068).
- m:308 states the rule ("Nothing after the first pick removes a session from the domain"; the sham envelope uses the same rule). m:261 names f1's rule as "Valid-session rule of record".

Model-free recount of data/f/sessions.jsonl (rerun independently, same counts):
- CORR, f1's rule: 28/56; map A 18/29, map B 10/27.
- CORR, m's rule: 30/58, delta +.0172; map A 19/30, map B 11/28.
- Sham: 18/33 (E = .0455) under f1's rule, 19/34 (E = .0588) under m's.
- The sessions that come back in are CORR s4 (lexical:prism@free4, P), CORR s25 (lexical:maple@free4, P) and sham s35 (lexical:saddle@free5, P).

Classification. None of §2.7's fourteen covers this:
- (6) covers which audit classes and the claiming order, not the analysis domain.
- (13) covers the arm interleave and live per-arm stop at floor, not which sessions count toward the floor or the primary.
- (12) and (14) both say "A0's comparison with f1's primary is unaffected" and do not mention the domain change.

So "beyond" is correct with respect to the fourteen. The effect, "bears on A0's comparison with f1's primary" (and on E and the by-map conjunct), is also correct.

Two refinements, neither of which refutes the claim:
1. It is already declared in §4 (m:308 quotes 58/30/28/56), so the G-PORT entry should list it as a declared difference missing from the Appendix-D list.
2. f1 had no live stop at a floor. Its plan launched fixed per-arm counts ordered by fractional progress (f_sessions.py:597-607), and the valid-n floors were declared thresholds applied in analysis. Only the counting unit (valid vs domain) belongs to this item; the move to a live stop at floor is item (13).

#### D49. Audit stack (v2 + v4 content exclusion-bearing + v5 advisory + echo + claiming order) applied at forced and free rounds
- finder's classification: §2.7 (6); refuter: refuted=False, classification Covered by §2.7 (6). That item already names the whole stack against f1's frozen audit list: audit v3 (v2 plus the exclusion-bearing v4 rev 3 classes), the v5 advisories, m's echo class and the claiming order. The `earlier` list feeding v4's stuck_attractor belongs to v4 rev 3. The session-end rule (a forced round ends on any claim, a free round only on lexical) has the same structure as f1's (audit at forced excludes, a free-round audit hit becomes post_degen, lexical excludes anywhere); m only has more classes. So the apparatus difference is not beyond the fourteen. The new part is the archive-effect quantification, which (6) does not give and which the G-PORT entry can add. One citation nuance: (6) cites PROPOSAL-f:61 ("frozen audit list"), which predates f1's 37c7078 amendment. That amendment added f1's 5 junk regexes and audit precedence (jlens-qwen36/data/configs/f_audit_patterns.json, loaded at f_sessions.py:553-554). f1's audit as it actually ran is the list plus the amendment.
- f1: f1 checks `audit_degenerate` with the e2a ban strings, the 9 fragments and f1's 5 junk regexes, and runs lexical only if that audit is silent (f_sessions.py:127-141, :317-318). f1 has no content class and no echo class. At a free round a degenerate response becomes post_degen and does not exclude, and lexical is never checked on it (:368-372).
- F0m: valence_core/m/audit.py:421-458 claims each round in the order v2 -> echo -> v4 content -> lexical. A forced round ends the session on any claim; a free round ends it only on lexical (audit.py:348-361, :501-506; runner_qwen.py:168-169, :199-200). `earlier` holds every prior task-round response (runner_qwen.py:167, :198).
- effect: This is covered as an apparatus difference, but (6) does not state its effect on the archive. It bears on A0's comparison through the domain's composition. The junk lists differ in both directions: f1's `config\s*[:=]` and `[a-zA-Z_]+="..."` are not in v2. So 'config: <own tag>' is an audit claim in f1 (at a free round: post_degen, no exclusion) but a lexical claim in m (at a free round: the session is excluded). A forced 'config: none' excludes in f1 and is unclaimed in m. v2's banner_terminator and bracketless_round_header claim lines that f1 leaves to lexical or to nothing. At free rounds, content and echo claims pre-empt lexical, so an own-pair mention inside such a response does not exclude in m.
- evidence: Scratch m_on_f1.py runs m's QwenTaskRoundAudit (HEAD, no banner, so echo is vacuous) over f1's 64 archived CORR rows. All 16 rounds f1 marked degenerate are v2 claims under m, plus one new v2 claim: s48 free5 '=== END OF EVALUATION SESSION ==='. v4 claims 3 forced rounds that f1 left unclaimed: s25 forced0 corrupted null_response, s25 forced3 clean stuck_attractor, and s48 forced1 corrupted stuck_attractor ('7' repeated). This makes s25 (f1: lexical@free4) and s48 (f1: valid, first pick P) pre-pick exclusions. m's audit plus m's domain then gives 28/56 (map A 17/28, map B 11/28), the same count as f1's 28/56 but a different set of sessions. stuck_attractor also crosses properties: s63 free7 is a correct clean 'January', claimed because the model earlier gave 'January' as a wrong answer to corrupted item 2. Probe junk.py gives 'config: granite': f1 junk, m lexical (free: excludes). It gives '=== End of session ===' and 'Round 5 | granite': f1 none, m v2.
- refuter: I verified both sides by reading both codebases (m judged at HEAD 5f7b968; audit.py, runner_qwen.py, scaffold.py and corr.py are unmodified in the working tree). I also re-ran the archive comparison with my own replay: it parses f1's transcripts directly and uses f1's own corrupt() at 0.12, without m's f1_config. Scratch files: .../scratchpad/step5/refute-audit-exclusion/{probes,replay,detail,iso}.py.

CONFIRMED:
- f1's side: f_sessions.py:127-141 (audit order: empty, ban strings, 9 fragments, 5 junk regexes; loaded at :551-554); :317-318 (lexical is checked only when the audit is silent); :339-345 (a forced audit or lexical hit excludes); :368-375 (a free audit hit becomes post_degen and does not exclude; a free lexical hit excludes). f1 has no content class and no echo class.
- m's side: audit.py:421-458 (order v2, echo, content, lexical); :348-361 and :501-506 (lenient rule); runner_qwen.py:167-169 and :198-200 (`earlier` appended and the session ended at both phases). session.lexical_hit is byte-identical to f1's lexical_hit.
- Probes: 'config: granite' is f1 junk but an m lexical claim (excludes at a free round). '=== End of session ===' is nothing in f1 and banner_terminator in m's v2. 'Round 5 | granite' is f1 lexical and bracketless_round_header in m's v2 (at a free round it excludes in f1 but not in m). At a free round, a stuck_attractor or null_response response that contains an own tag is content-claimed in m and does not exclude.
- Archive: all 16 rounds f1 marked degenerate (6 forced, 10 free) are v2 claims under m. s48's '=== END OF EVALUATION SESSION ===' is a new v2 claim. v4 claims s25 k0 (corrupted, null_response), s25 k3 (clean, stuck_attractor) and s48 k1 (corrupted, '7' repeating the clean k0 '7'). s25 and s48 become pre-pick exclusions. m's audit plus m's domain gives 28/56 (map A 17/28, map B 11/28) against f1's 28/56 of record (A 18/29, B 10/27). The sessions differ: m drops s48 and adds s4. s63 k7 is a correct clean 'January' claimed as stuck because k4 answered 'January' to corrupted item 2 (third month, graded False).

ERRORS AND CORRECTIONS (none overturns the difference):
(1) Factually wrong example: "A forced 'config: none' excludes in f1 and is unclaimed in m." v4 strips the leading "config:" label (contentclass_v4.py:71, :139-140), leaving 'none', a null word (contentclass.py:84). So m claims content:null_response, and a forced round excludes in both. The asymmetry is real, but needs an example like forced 'config: 77': f1 junk, excluded; m unclaimed, not excluded.
(2) Index convention: "s48 free5" and "s63 free7" use the 0-based round index k. In f1's own @free notation, used in the same sentence for s25 "lexical@free4", they are free1 and free3.
(3) Attribution: only part of the set change comes from the audit. s48 dropping out is the audit's doing (v4 at forced1, map A). s4 entering (f1 lexical@free4, picked P, map B) comes from m's domain rule (m:308, "Nothing after the first pick removes a session"), not the audit. The audit's isolated effect: under m's domain, 30/58 becomes 28/56 (s25 and s48 removed, both picked P); under f1's whole-session validity rule, 28/56 becomes 27/55 (A 17/28, B 10/27).
(4) Not mentioned in the claim but present: two free-round v4 content claims (s8 k8, s63 k7) and v5 advisories (s2 k8 wrong_task; s42 k3 and k4 task_echo). None of them exclude.

Effect classification: the claim's "bears on A0's comparison through the domain's composition" holds on the archive. It is small: the count is unchanged, and the by-map split moves by one session in each map, one move from the audit and one from the domain rule.

#### D50. Property-asymmetric reach of v4/v5 under task_text = the corrupt_m render as delivered
- finder's classification: beyond; refuter: refuted=False, classification Covered by (6), not beyond. It is a property of item (6)'s audit, v3 with v4 rev 3 content and the claiming order, run with m:261's task_text = the render as delivered. Item (3) only sets which items it reaches. Item (6) does not state the property-dependent reach, so the right fix is a note on (6), not a fifteenth item.
- f1: f1 has no content class. Its 0.12 renders also keep the imperative 'Write' intact on items 5, 11 and 15 ('Write the opposite oy 'hot'.' and so on). jlens-qwen36/scripts/f_sessions.py:106-116, :127-141.
- F0m: The render is passed as v3's task_text: valence_core/m/audit.py:421-440, called from runner_qwen.py:161 and :192, as m:261 directs. The corrupt_m 0.15 renders hit the verb: 'Writa the oppcsite oc 'hot'.', 'Writo the oppssitu of 'up'.', 'Wtite thn opposite on 'open'.'. contentclass.py's `_IMPERATIVE` and `_VERBS` then fail on the corrupted round only.
- effect: Bears on A0's comparison, weakly. A pre-pick exclusion path (preamble_without_content on a forced round) is open on clean rounds and closed on corrupted rounds for these three items. The task_echo advisory likewise fires only on clean rounds. This comes from combining (3) and (6) with §2.6's task_text choice, and neither item names it. It is also descriptive for the per-property exclusion table.
- evidence: Scratch asym.py, 16 items x 4 response forms ('Sure: {t}', '{t}', a generic preamble, 'I will answer: {t}'). Under m's renders, 6 of 64 cases are asymmetric, all on items 5, 11 and 15. 'Sure: <task>' gives content:preamble_without_content on the clean round and no claim on the corrupted round. A verbatim restatement gives a task_echo advisory on clean only. Under f1's renders (F1R=1), 0 of 64 are asymmetric.
- refuter: The claimed difference is real.

**Facts checked against HEAD 5f7b968.**
- f1 has no content class. Its audit, audit_degenerate at f_sessions.py:127-141, never takes the task text, so f1's exclusions cannot depend on the delivered property.
- f1's corrupt() at :106-116 is fixed per item. I recomputed its 0.12 renders with corr.renders_f1: items 5, 11 and 15 all keep "Write" intact.
- F0m passes spec.task_text into audit3.check: audit.py:421-440, called from runner_qwen.py:161 and :192.
- On a contrast Q round, spec.task_text is the corrupt_m render: corr.Delivery.text at :403-404 and scaffold.py:161.
- The renders are exactly as quoted ("Writa the oppcsite oc 'hot'." and so on).
- On those renders, v3's _IMPERATIVE and the _VERBS check in the run test fail (contentclass.py:58-62, :149, :172-188).
- I re-ran the claimant's asym.py: 6 of 64 cases are asymmetric, all on items 5, 11 and 15, and 0 of 64 with F1R=1.
- The build already pins this behaviour: audit.py:773-778, the self-test line "v3's task_text is the render as delivered (preamble on clean, not on the render)", which passes at results/raw/2026-10-06_m-build_selftest.txt:237.

**Classification.** This is not a separate F0m-vs-f1 apparatus difference. f1 runs no task-text-dependent detector, and item (6) is the disclosure that F0m does. The asymmetry is an internal property of that disclosed audit, configured by m:261's declared directive. The claimant's own account (it comes from combining (3) and (6) with §2.6's task_text choice) puts it inside covered items.

**Scope corrections (both checked in scratch step5/refute-asym/).**
1. It is not specific to items 5, 11 and 15, or to m's verb-hitting dose. If the model restates the CLEAN text on a corrupted round ("Sure: {clean}", "{clean}", "Here is the answer: {clean}"):
   - under m's renders, items 2 and 8 are asymmetric too: 15 of 48 cases, over 5 items;
   - under f1's own 0.12 renders, items 2 and 8 are asymmetric: 6 of 48.
   So "0 under f1's renders" holds only when the model restates the render as delivered. The asymmetry comes from task_text = render whenever the corruption falls inside the restated instruction span. Dose (3) only moves which items it reaches.
2. The effect grading. The forced-round path the claim names is pick-independent, because every contrast session's forced rounds carry both properties. Its bearing on A0's primary is therefore descriptive. The pick-dependent path, which the claim does not name, is on free rounds. There the claiming order (v2, then echo, then content, then lexical) lets a content claim take a round that also carries an own-pair lexical hit, and the lenient free rule excludes only on a lexical claim (audit.py:361).
   - Test response: "Sure: Write the opposite of 'hot'. (granite)." on item 5.
   - On a clean-chosen free round it is claimed as content and does not end the session.
   - On a corrupted-chosen free round it is a lexical claim and excludes the session.
   - In f1, the same round would be a lexical exclusion either way (:373-375).
   That path is also inside (6) (the claiming order) and is worth naming in the note.

#### D51. scaffold_absorption hair trigger: session cut and stage/campaign STOP, where f1 logged an audit claim and continued
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: A ban string in a response is `special:` in audit_degenerate (f_sessions.py:132-134). At a forced round it excludes and ends the session (:339-345). At a free round it is post_degen: no exclusion, the session continues to all 6 free rounds (:368-372). There is no run stop.
- F0m: valence_core/m/runner_qwen.py:170-173 (forced: v2 exclusion plus trigger, break) and :201-203 (free: trigger, break, no exclusion). The trigger is recorded at scaffold.py:417-422. bars.py:513-529 sets on_fire to STOP. In the campaign, stages.py:1936 and :1947-1949 set status STOP. A free-phase contrast trigger is announced by phase alone (stages.py:1040-1067).
- effect: No effect on a session's first pick: a forced hit excludes in both, and a free hit comes after the pick. A free-round fire leaves an incomplete session that is still in the domain and still whole-session 'valid', where f1 ran it to completion. A single fire STOPs the stage or the unit's campaign, which f1 never did. This is a stop-rule and record difference.
- evidence: From code: runner_qwen.py:201-203 returns at once on ra.scaffold. The Qwen scaffold set equals v2's ban strings (audit.py:415-419), so a forced hit is also a v2 exclusion. f1's archive has 0 `special:` claims.
- refuter: I checked this claim against f1's code and the m package at 5f7b968. It holds, and none of §2.7's fourteen items covers it.

**f1's side is as stated.**
- In `audit_degenerate` (f_sessions.py:132-134), a ban string in the text returns `special:{s}`. The ban strings come from `data/configs/e2a_ban_list.json` (:57, :551).
- In a forced round, that claim sets `audit:{deg}@forced{ri}`, excludes the session and breaks (:339-345).
- In a free round, it only sets `choices_log[-1]["post_degen"]` (:368-372). There is no exclusion, and the loop goes on with the next free round. Only a later lexical hit can still exclude the session (:373-375).
- No single claim stops the run. The only pauses in the main run are `checkpoint_eval`'s guard-rate binomial and Fisher tests (:391-434). The smoke run's audit bar needs more than 20% of sessions at n of 6 or more (:507).
- f1's archive has 344 rows, 0 rounds with a `special:` degen and 51 `post_degen` choices (my count).

**F0m's side is as stated.**
- Forced round (runner_qwen.py:168-173): `qwen_ends` excludes at forced on any claim (:168-169), then `ra.scaffold` records the trigger, sets `stopped` and breaks (:170-173). The claim cites :170-173 for the exclusion too; the exclusion itself is at :168-169, a trivial cite drift.
- Free round (:199-203): `qwen_ends` is lexical-only at free (audit.py:361). A scaffold hit is claimed by v2 first, so lexical never claims it and the session is not excluded. The runner records the trigger and breaks.
- The two string sets match by construction: audit.py:415-419 asserts the scaffold strings equal v2's ban strings, and runner_qwen.py:76-77 loads them from the e2a ban-list file. The self-test at audit.py:901 confirms a ban string yields both a v2 `special:` claim and a scaffold hit.
- scaffold.py:417-422 records the trigger. In `record()` (scaffold.py:428-447), a free-phase fire leaves `domain` True, `excluded` False and `complete` False.
- bars.py:513-519 sets `on_fire=_STOP` for `scaffold_absorption`, with `_STOP` = "STOP the stage" at :471.
- In the campaign, stages.py:1936 calls `_hair_hit`, and :1947-1949 sets status STOP and breaks. Line 1935 counts the session toward `domain` first. Gate stages also call `_hair_hit` at :1352 and :1541.
- For a contrast session's free-phase fire, `announce_stop` names the phase only and withholds the class (stages.py:1055-1059).

**The effect statement is right.** A forced hit excludes before any read in both apparatuses. A free hit comes after the first pick, so A0's comparison with f1's primary is unaffected. What differs is the stop rule and the record: the session is cut and incomplete, and the stage or campaign STOPs, where f1 logged `post_degen` and finished the session.

**Classification: beyond.**
- Item (6) lists v3, v4 rev 3, v5 advisory, the echo class and the claiming order. It does not name `scaffold_absorption` or any session cut or stop.
- Item (13) covers per-arm stop at floor and the interleave, not hair triggers.
- No other item touches it. The hair trigger is declared in §3's common bar conventions ("a hair-trigger fire anywhere stops the stage") and in §2.6's string-set clause, but neither is one of the fourteen disclosures.

**One further point for the entry.** §3 says a Qwen runner's "free-round v2 claim ending nothing (f1's post_degen, f_sessions.py:368–372)". Every Qwen scaffold hit is a v2 claim, yet the runner ends the session at a free-round fire. For task rounds the proposal states an explicit session end at the fire only for Q-F3 reasoning lines (§2.6). For Q-F0 task rounds, the cut rests only on m:271's "stops the stage". That tension inside m is worth stating next to this difference.

#### D52. Strict scope recorded and reported beside the lenient scope of record
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: One scope only. Forced deg or lexical excludes; free lexical excludes; free deg does not (jlens-qwen36/scripts/f_sessions.py:337-375). The first free degeneracy survives only as post_degen.
- F0m: `strict_exclusion` = the first claim in any phase (valence_core/m/scaffold.py:394-395; audit.py:517-519). It is reported for sham templates only before VERDICTS (readrule.py:602-604, :637). The spec is §2.6 m:261 ('lenient scope with strict beside').
- effect: Descriptive. On f1's archive under m's audit, the first strict events are 8 forced and 7 free, so whole-session validity under strict would differ further.
- evidence: Scratch m_on_f1.py 'strict-first events' Counter: forced 5 clean audit:frame, 1 corrupted audit:frame and 2 corrupted content; free 5 audit:frame, 2 content stuck and 1 clean lexical.
- refuter: The claim holds; I am not refuting it. I checked both codebases, with m judged at HEAD 5f7b968.

**f1's side.** f1 has a single exclusion scope:
- A forced degeneracy or lexical hit excludes the session and ends it (f_sessions.py:338-343).
- A free lexical hit excludes it (:373-375).
- A free degeneracy does not exclude; it is only logged (:366-372).
- f1's record has no session-level strict field. PROPOSAL-f never defines a strict or lenient scope; its only "strict" is the "strict pooled lexical bar", a different sense.
- The f1 SCREEN VERDICT and post-screen entries (archive/RESULTS-cycles3-4.md:32-124) report one valid-n per contrast and no strict figure.

**F0m's side.**
- `SessionLog.add_round` sets `self.strict` to the first claim in any phase (scaffold.py:394-395), and the record carries it as `strict_exclusion` (scaffold.py:444).
- `strict_excludes` and `RoundAudit.excludes('strict')` both mean "any claim" (audit.py:517-519, :353-354).
- `_sham_block` tallies `strict_excluded_sessions` (readrule.py:602-604, :637). The block at :580-584, the one carrying `contrast: True`, has no such tally, and the PIN at :634-636 confirms strict is reported for sham templates only before VERDICTS.
- The spec is m:261: "lenient scope with strict beside".

**Classification: beyond.** §2.7's fourteen do not name the strict scope or its recording. The nearest is item (6), but it covers only the audit's classes and claiming order (v3, v4 rev 3, v5 advisory, the echo class), not the scope beside or the new recorded and reported field. The scope of record is unchanged, so the effect is descriptive, as the claim says.

**Two minor inaccuracies, neither refuting:**
1. The f1 side says "the first free degeneracy survives only as post_degen". In fact every free degeneracy is kept, both as `rounds_log[...]['degen']` (f_sessions.py:333) and as `post_degen` (:372), so the strict scope can be rebuilt from f1's archive after the fact.
2. The evidence breakdown is off. I re-ran the scratch m_on_f1.py with no model or tokenizer, writing output only to step5/refute-strict-beside/out.txt.
   - Forced is right at 8: 5 clean audit:frame, 1 corrupted audit:frame, 1 corrupted null_response, 1 corrupted stuck_attractor.
   - Free is 4 audit:frame (3 corrupted, 1 clean), not 5. With 2 stuck_attractor (one clean, one corrupted) and 1 clean lexical:prism, the free total is 7, matching the effect line's "8 forced and 7 free". The evidence line's own items add up to 8.

Only 6 of the 7 free first events would differ from the lenient scope. The 7th, the clean lexical hit at s4, excludes under lenient too.

#### D53. post_degen vs post_choice_degeneracy (definition and keys); audit_degenerate keyed by category
- finder's classification: beyond; refuter: refuted=False, classification Split. The definition half and the whole 13-vs-10 count gap are covered by §2.7 item (6). The keying and record-schema half is beyond the fourteen and descriptive.
- f1: `choices[-1].post_degen` = the free-round audit-degenerate reason string (v2-type classes only), stored on the choice entry (jlens-qwen36/scripts/f_sessions.py:368-372).
- F0m: post_choice_degeneracy = a free-round v2, echo or content claim, keyed (template, claim) (valence_core/m/audit.py:554-555, :584-585; DECLARED_COUNTERS_QWEN :91-93). audit_degenerate is keyed by the v2 category (empty/special/frame/junk), not by the reason (audit.py:573-574; readrule.py _audit_category). This is Code's PIN (D8); §2.7 says nothing about counters.
- effect: Descriptive. On the same archived rounds the counts are not comparable one for one.
- evidence: f1 CORR archive: 10 post_degen events in 5 sessions (1, 16, 25, 58, 61), all frame:. m's definition on the same rounds as generated gives 13: 11 v2 (one is new, s48 free5) and 2 content stuck_attractor (s8 free8, s63 free7). Source: scratch m_on_f1.py and find_content.py.
- refuter: The facts hold.

f1 side: f_sessions.py:368-372 sets `choices_log[-1]["post_degen"] = deg`. Here `deg` is the reason string returned by the frozen `audit_degenerate` (:127-141), which returns empty, special, frame or junk. It is non-excluding, and lexical is suppressed when `deg` is set (:318). f1's analyze (:437-500) has no post_degen counter and no audit counter. The reason strings live only in rounds[].degen, exclude_reason and choices[].post_degen.

m side at HEAD 5f7b968:
- audit.py:91-93 declares DECLARED_COUNTERS_QWEN with post_choice_degeneracy.
- :554-555 is the PIN: post_choice_degeneracy is "a free-round v2, echo or content claim ... keyed (template, claim)".
- :584-585 does the counting.
- :573-574 keys audit_degenerate by `_category(ra.detail)`.
- readrule.py:509-519 has `_audit_category`, which is also category-keyed in the stage report.
- m's choice record (scaffold.py:398-411) has no post_degen field. The free round's claim and full detail sit on rounds[].audit (:391).

So the record keeps reason-level detail, and only the counters aggregate it. At the record level the field has moved, not been coarsened.

Evidence, reproduced on data/f/sessions.jsonl:
- f1 CORR has 10 post_degen events in sessions 1, 16, 25, 58 and 61, all `frame:`.
- Under m's wrapper on the as-generated rounds there are 13: 11 v2 and 2 `content:stuck_attractor`. In the claim's labels these are s8 "free8" and s63 "free7". Those labels are round indices k; in f1's free{ci} notation they are free4 and free3, and s48 "free5" is free1.

Caveat the claim omits: "as generated" includes rounds m would never produce. m ends s25 at forced 0 (content null_response) and s48 at forced 1 (content stuck_attractor). Applying m's session-end flow to the archive gives 10, not 13. That is 8 frame events shared with f1 plus the 2 content claims; f1's two s25 events drop out.

Classification:
- The membership rule is f1's rule of record (m:261): a free round excludes only on a lexical hit, and other audit hits end nothing. m applies it to §2.7 item (6)'s audit: v3 over v2, v4 rev 3 content, m's echo class and the claiming order v2 → echo → content → lexical.
- Every extra count traces to item (6). The s48 hit is v2's `(?im)^\s*={2,}[^\n]*={2,}\s*$` junk regex, which f1's frozen list did not fire on. The two content claims are v4 rev 3.
- So "definition differs" is covered by (6), not beyond.
- What is beyond the fourteen: no per-choice post_degen field; rule-23 counters (m:314) that f1 lacked; post_choice_degeneracy keyed (template, claim) with no round index or reason; audit_degenerate keyed by category.
- No f1 side is cited for the audit_degenerate sub-claim, because f1 had no such counter. It is only a difference in the sense that m adds a counter.

Effect: descriptive, as claimed. It touches neither the primary's domain (m:308) nor any secondary built at step 4.

#### D54. Exclusion and round record fields renamed, dropped or added
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: Session-level fields: `exclude_reason` is a string carrying class, tag or fragment, and round index (e.g. 'lexical:prism@free4', 'audit:frame:[round@forced1'). Other session fields: `exclude_cfg` (P/Q of the excluding round, 'sham' on the sham arm), `n_rounds`, `n_cap_hits`. Per round: `degen`, `lex` (None whenever degen), `term` (the regex string), `graded`. Per choice: `top1_is_label`. Sources: jlens-qwen36/scripts/f_sessions.py:331-334, :340-344, :374-375, :377-385.
- F0m: `exclusion` = {class, phase, detail}, with no round index and no role (valence_core/m/scaffold.py:413-415). There is no exclude_cfg; role and property sit on each round (:386-392). Per round there is an `audit` dict (claim, detail, v3, advisory, echo_line, lexical_raw, scaffold; audit.py:363-368), `termination` as a bool, `stop_reason`, and no `graded`. Per choice: `top1_not_label` (:409). New session fields: `domain`, `strict_exclusion`, `hair_triggers`, `complete` (:438-447).
- effect: Descriptive. An own-pair mention inside a degenerate round is unrecorded in f1 and recorded in m (lexical_raw). Which termination pattern matched and per-round correctness are lost in m. The excluding round's index and property must be derived from rounds[-1].
- evidence: From code: f1 `hit = None if deg else lexical_hit(...)` (f_sessions.py:318) vs m `lex = lexical_hit(text, op)` on every round (audit.py:442, :456-458). m's add_round dict (scaffold.py:386-392) has no graded key; a grep of valence_core/m finds 'grade' nowhere in the runner path.
- refuter: I checked both codebases, with the m package at HEAD 5f7b968. scaffold.py and audit.py have no working-tree edits, so the line numbers hold. The claim is correct in substance.

f1 side, every cited line checked:
- exclude_reason is built as f"audit:{deg}@forced{ri}" or f"lexical:{hit}@forced{ri}" at f_sessions.py:340/342, and f"lexical:{hit}@free{ci}" at :374.
- The archive in data/f/sessions.jsonl has both quoted examples: CORR s4 'lexical:prism@free4' and CORR s53 'audit:frame:[round@forced1'.
- exclude_cfg is set to "sham" on the sham arm (:344, :375). It is in the archive as sham, P or Q.
- n_cap_hits and n_rounds are at :380-381.
- The per-round fields are at :331-334. lex is None whenever degen (:318); the archive has 93 degenerate rounds and none with lex set. term stores the matching regex string (:321-325); in the archive it is '===\s*[Ee]nd' on 39 rounds. graded is a bool on every f1 CORR round (597 rounds, 98 False).
- top1_is_label is at :365.

F0m side:
- exclusion = {class, phase, detail}, with no round index and no role or property (scaffold.py:413-415).
- Role, pole and property sit on each round (:386-392).
- The audit dict is at audit.py:363-368. lexical_hit runs on every round (:442), and lexical_raw is stored whatever the claim (:457).
- termination is a bool, any() over the patterns (scaffold.py:304-305, :392). stop_reason is at :391.
- There is no graded key anywhere in valence_core/m.
- top1_not_label is at :409.
- domain, strict_exclusion, hair_triggers and complete are new (:438-447). n_rounds and n_cap_hits are absent.
- The excluding round is always rounds[-1], because the runner breaks at the first exclusion (runner_qwen.py:168-175, :199-205).

Imprecisions, none of which refutes the claim:
1. top1 was not renamed. m keeps top1_is_label inside choice.read (scaffold.py:360) and adds top1_not_label beside it.
2. "Lost" overstates two points. The matched pattern and per-round correctness are not recorded, but m stores each round's text and item index, so both can be recomputed after the fact. Likewise, f1's lexical mention inside a degenerate round can be recovered from its stored transcript.
3. The audit dict also carries substrate, phase and degeneracy.
4. The claim leaves out related schema changes: f1's per-choice post_degen flag has no m counterpart, and the arm/session/pair/swap/start_P/tag_P fields are recast as unit/contrast/s/j/cell/keys.

Effect: I agree it is descriptive. The primary key first_free_pick_P is kept. m's declared secondaries and counters (termination per round, the per-property exclusion table) can all be derived from the m record, and f1's analysis uses term only as a truthy value (f_sessions.py:451). Nothing changes A0's comparison with f1's primary or secondaries.

Classification: beyond §2.7's fourteen. No item covers the record schema. Item (10) covers only the dropped per-choice ea, which this claim does not cite. Item (6) covers the audit classes and their claiming order, which keeps f1's audit-before-lexical precedence, but not the recording of lexical_raw on every round or any of the field changes.

#### D55. Per-property exclusion table: f1's whole-session 7-vs-1 reference vs m's pre-pick-session and round-by-class unit
- finder's classification: beyond; refuter: refuted=False, classification beyond (the audit half of the shift, 5v1 to 5v3, comes from item (6); the change of unit is in none of the fourteen)
- f1: analyze() counts excluded sessions (any phase) by (arm, rounds[-1].cfg) (jlens-qwen36/scripts/f_sessions.py:441-446). The reference is 'CORR-P 7 vs CORR-Q 1' (archive/RESULTS-cycles3-4.md:91-93), which includes the two free-round lexical exclusions (s4, s25, both P). PROPOSAL-f:93-97 requires the table.
- F0m: m:314 specifies, per arm x property: rounds generated, rounds excluded by class, and sessions excluded pre-pick. It names f1's 7-vs-1 as the reference. The record supplies this through rounds[].property and the exclusion phase (valence_core/m/scaffold.py:386-392, :413-415; stages.py:1698-1702). m_analyze is not built yet.
- effect: Descriptive. The table's reference value crosses a change of unit and of audit.
- evidence: f1 CORR exclusions (P/Q of the excluding round): s4 P free, s25 P free, s27/s36/s49/s55/s60 P forced, s53 Q forced. In m's pre-pick unit this is 5 vs 1 under f1's audit, and 5 vs 3 under m's audit (s25 forced0 and s48 forced1 are corrupted-round content claims; scratch m_on_f1.py).
- refuter: The claim is not refuted. I checked every anchor against both codebases (m code at HEAD 5f7b968).

f1's side holds. In f_sessions.py, analyze() starts at :437, and :441-446 count excluded sessions of any phase by (arm, rounds[-1].cfg). f1 ends a session at the round that excludes it (forced: break at once; free: the `if excluded: break` at the top of the next free iteration), so rounds[-1] is always the excluding round. In CORR, P is clean and Q is corrupted (:252-258, corrupt() applied to the Q items). I recounted data/f/sessions.jsonl and got ('CORR','P') 7 and ('CORR','Q') 1. The P seven are s4 (lexical:prism@free4) and s25 (lexical:maple@free4), both free-round, plus s27, s36, s49, s55 and s60 (audit frame, forced). The Q one is s53 (audit frame '[round', forced1). Archive RESULTS-cycles3-4.md:91-93 reports "CORR-P 7 vs CORR-Q 1", and PROPOSAL-f:93-97 makes the table a required report. Every anchor is exact.

F0m's side holds. m:314 specifies, per arm and property (clean, corrupted): rounds generated, rounds excluded by class, and sessions excluded pre-pick. It names the 7-vs-1 at archive:91-93 as "the reference" without saying the unit has changed. The record supports the table through three anchors, all exact:
- scaffold.py:386-392 (add_round's dict, which includes "property")
- scaffold.py:413-415 (exclude() records the phase)
- stages.py:1698-1702 (_prepick = exclusion phase "forced")

scripts/m_analyze.py does not exist at HEAD; stages.py:134-135 only names its path.

The numbers hold. Under f1's own audit, the pre-pick unit gives 5 clean vs 1 corrupted, the forced exclusions only. I re-ran a copy of the audit-exclusion scratch replay (step5/refute-perprop-table/m_on_f1.py). It finds m's audit claims s25 at forced0, a corrupted round with a refusal response (content:null_response), and s48 at forced1, a corrupted round that repeats "7" (content:stuck_attractor). Reading the archived transcripts directly agrees. So the pre-pick count under m's audit is 5 vs 3, as claimed.

It is a real difference in how sessions are excluded and analysed, not an internal refactor. f1's per-property figure counts whole sessions excluded in any phase, so it includes the two free-round lexical exclusions, which f1 also drops from its primary. m's domain rule (m:308) is that nothing after the first pick removes a session. m:314's pre-pick column therefore cannot hold s4 or s25, and no m column counts excluded sessions by property across phases.

Classification: none of §2.7's fourteen addresses the exclusion table's unit or the scope of exclusion. Item (6), the audit, accounts only for 5v1 becoming 5v3. Item (13) is interleave and stop-at-floor, not exclusion scope. The proposal states the unit change elsewhere: m:308 for the domain (f1's 58 first reads and two post-pick exclusions) and m:316 for the guard's p0 ("f1's whole-session reference ... carried to m's pre-pick unit"). Neither is in §2.7, and m:314 says nothing about it for the table. So the claim is beyond the fourteen.

Effect is descriptive, as claimed. The table is reported in VERDICTS only (m:318), and the guard reads pooled pre-pick rates per arm, not rates per property.

One nuance, which does not refute the claim: if m:314's "rounds excluded by class" counts only session-ending rounds (post_choice_degeneracy is listed as its own counter in m:314), then summing that column over classes recovers f1's whole-session unit by another name. On the archive that gives 7 vs 1 under f1's audit and 6 vs 3 under m's (clean: s4, s27, s36, s49, s55, s60; corrupted: s25, s48, s53). The G-PORT entry should say which of m:314's columns the 7-vs-1 is the reference for.

#### D56. Printed per-session line: f1 printed the pick and the full exclusion reason; m prints class@phase only
- finder's classification: beyond; refuter: refuted=False, classification beyond (not among §2.7's fourteen at m:267; but the proposal itself already states it at §4 m:318, "f1 printed picks, f_sessions.py:624–627", and at §2.6 m:263, so it is a departure the proposal already discloses, not one the port newly reveals)
- f1: `[j/N] CORR s{s}: first=P|Q|X EXCL {exclude_reason}  {secs}s`. This prints the pick, the tag, the round index and the timing (jlens-qwen36/scripts/f_sessions.py:624-628).
- F0m: Implemented in valence_core/m/readrule.py:443-484 (printed_reason) and :486-504 (session_line), giving `{stage} {template} s={s} valid|excluded:{audit|echo|content|lexical}@{forced|free}`. A contrast free exclusion prints as `excluded@free`, and content is a fourth printed class (seat ruling (q)). No pick, tag, index or seconds is printed. The spec is §2.6 m:263 and §4 m:318.
- effect: None on any DV; this is blinding only.
- evidence: From code (HEAD 5f7b968). The runner_qwen self-test asserts the line form `qual A0s? s=\d+ (valid|excluded:[a-z]+@(forced|free))` (runner_qwen.py:537-545).
- refuter: I checked this against HEAD 5f7b968 using git show, not the working tree. The claim holds. There are only small imprecisions in the details.

f1 side. f_sessions.py:624 sets `first = row["first_free_pick_P"]`, and lines 625-628 print `  [{j+1}/{len(plan)}] {arm} s{s}: first=P|Q|X{ EXCL <exclude_reason>}  {secs}s`. The exclude_reason strings are built at :340, :342 and :374: `audit:{deg}@forced{ri}`, `lexical:{hit}@forced{ri}` and `lexical:{hit}@free{ci}`. `hit` comes from lexical_hit (:119-124), which returns the matched own-pair tag. So f1 printed:
- the pick, as config P/Q/X;
- the tag;
- the forced-round or free-round index;
- the seconds;
- also the audit sub-category (deg), the arm name and a [j/N] progress counter, which the claim does not mention.

The archived stdout confirms this form: results/raw/2026-08-10_f_smoke.txt has `[9/12] CORR s1004: first=Q EXCL lexical:prism@free3  59s`.

F0m side.
- readrule.py:443-483 printed_reason: returns `{PRINT_CLASS[cls]}@{phase}`, or CONTRAST_FREE = "excluded@free" when phase is free and the session is a contrast session (:480).
- PRINT_CLASS (:87-88) holds audit/echo/content/lexical, with v2 mapped to audit. Content is the fourth class, which the PIN at :82-86 mentions; seat ruling (q) keeps it.
- readrule.py:486-504 session_line: builds `{stage} {template} s={s} valid|excluded:<printed_reason>`. It is checked against _LINE_RX at :98-100.
- The runner prints nothing; its self-test asserts this at runner_qwen.py:531-545, and the regex at :539 matches the claim.
- The only per-session stdout is `print(readrule.session_line(rec))` in stages.py at :1355, :1544 and :1946. The bars' blinded look messages are printed separately at :1960.
- So no pick, tag, round index, seconds, progress counter or audit sub-category is printed.

Minor imprecisions, none of which refutes the claim:
- A contrast free-round exclusion prints in the full line as `excluded:excluded@free`. `excluded@free` is the printed_reason value only (see runner_qwen.py:544 and runner_olmo.py:426).
- printed_reason ends at :483, not :484.
- f1's print is :625-628; :624 is the `first` assignment. m:318 cites 624-627.

Effect. Stdout feeds no DV or analysis: f1's analysis reads sessions.jsonl, and m's reads its checkpoints. The difference is blinding and display only, so its effect on the comparison with f1 is "none". The claim is correct there.

Classification. None of §2.7's fourteen items covers stdout printing. They cover the banner, CORR module, dose, sham pool, roster, audit, rng keys, assignment, verify cadence, ea_mass, round path, read window, interleave and generation window. So "beyond" is correct with respect to the fourteen. However, the proposal already names this departure in §4 m:318 and §2.6 m:263. The G-PORT entry should list it as beyond the fourteen with a pointer to m:318 / m:263, not as something the port newly revealed. The entry could also note the extra items f1 printed that m drops: the arm name, [j/N], and the audit sub-category.

#### D57. Exclusion guard: f1's whole-session guard vs m's pre-pick guard (unit, comparator, arming, cadence, boundary)
- finder's classification: beyond; refuter: refuted=False, classification beyond. Nothing in §2.7 (m:267) names the exclusion guard. Two parts of this bundle do touch §2.7 items. What the Fisher comparator contains (the CORR_clean A0s against f1's SHAM pool of creative prompts) is item (4). The comparator being shared across five contrasts in f1 but matched to one contrast in m follows from item (13), the six-arm interleave against two arms. The unit change, the arming change, the cadence change and the boundary change are in none of the fourteen. m:316 states the unit change, but in its own section, not in §2.7's list.
- f1: Per contrast, the guard counts excluded sessions in any phase. It tests them against p0 .20 by binomial at arm n = 24 and at completion (GUARD_CHECKPOINTS :90). It also runs a one-sided Fisher against the shared SHAM-pool arm, armed only at sham n >= 12 (:408). Either pauses on p < .05 (jlens-qwen36/scripts/f_sessions.py:391-415).
- F0m: Per contrast arm the guard counts pre-pick exclusions (stages.py:1698-1702) at every look, i.e. every 40 launches and at the end (stages.py:1724-1754). Fisher runs against the matched A0s, armed at every look with no minimum sham n (bars.py:416-426), and is binding. The absolute .20 bar is binding on Qwen (bars.py:539-566). Fires on P <= alpha. The spec is m:316.
- effect: Pause only, never a verdict. The threshold .20 is carried over to a different unit. m:316 states the adaptation, but §2.7 does not list it.
- evidence: f1 archive: CORR has 8/64 whole-session exclusions vs 6/64 pre-pick under f1's audit (8/64 under m's audit). The sham has 7/40 whole-session vs 6/40 pre-pick (s35 is a free exclusion).
- refuter: The claim holds; I checked both sides.

**f1's side** (jlens-qwen36/scripts/f_sessions.py):
- `GUARD_CHECKPOINTS = (24,)` is at :90.
- `checkpoint_eval` (:391-415) counts `r["excluded"]`, which is whole-session exclusion in any phase, for each contrast in CONTRASTS.
- It evaluates only when the arm's n equals 24, or at completion (:399).
- The absolute test is `binom_p_ge(x, n, 0.20)`.
- The Fisher test runs only `if sh_n >= 12` (:408), against the single sham arm that all five contrasts share.
- A fire on either test pauses at `p < 0.05` (:412-415). The run checks after every session (:664) and at completion (:672).

**m's side, at HEAD 5f7b968:**
- `_prepick` (stages.py:1698-1702) counts only exclusions with `phase == "forced"`.
- `campaign_look` (stages.py:1724-1754) runs the Fisher and absolute bars against the matched sham arm, A0s.
- It is called when total launches are a multiple of 40 (stages.py:1932, `LOOK_EVERY = 40`) and at the end (stages.py:2013).
- The Fisher test has no minimum sham n. The PIN at bars.py:420-424 says f1's `sh_n >= 12` is not carried.
- Both tests fire at `p <= self.alphaq` (bars.py:426, :429).
- Q-F0 is built with `_campaign(..., abs_binding=True)` (bars.py:587), so the absolute .20 bar binds on Qwen. On OLMo it is `False` (bars.py:620).
- `fisher_sf` is the same formula as f1's `fisher_one_sided`, so the test itself is unchanged; only what it is applied to changes.
- m:316 says .20 is "carried to m's pre-pick unit".

**Evidence, recomputed from data/f/sessions.jsonl:**
- CORR has 8/64 exclusions. Two are free-phase lexical (s4 and s25, both at free4), so 6/64 are pre-pick.
- The sham has 7/40 exclusions; only s35 (lexical:saddle@free5) is free-phase, so 6/40 are pre-pick.
- I re-ran the audit-exclusion lens's own script, which applies m's audit to f1's CORR rounds. It gives 8/64 pre-pick: s48 becomes forced-1 content:stuck_attractor, and s25 becomes forced-0 content:null_response. This matches the claim's "8/64 under m's audit".

**Nuances that do not refute the claim:**
- f1's completion check prints "COMPLETION FLAGS" rather than a mid-run pause, but it is still a design-instance hold before any claim.
- m's "every 40 launches" counts both arms together, so a look comes about every 20 sessions per arm.
- The change from `<` to `<=` cannot be observed on the absolute bar: the binomial P at p0 = 1/5 has denominator 5^n and can never equal exactly 1/20.
- For Fisher with matched arms of 1 to 120, P equals exactly .05 only at 3/3 vs 0/3. No campaign look can reach that, so the boundary difference is negligible in practice.

**Effect:** as the claim says, it is a pause only and never a verdict, so the comparison with f1 is descriptive. The one way it could change a sample is if an adjudication ends in a PI stop, which is analysed as obtained.

#### D58. Pooled own-pair lexical monitor: f1's binding session-unit bar has no Q-F0 counterpart
- finder's classification: beyond; refuter: refuted=False, classification beyond (none of §2.7's fourteen names it; it sits next to item (1)'s priming exposure, and the proposal declares it outside §2.7, in §6 at m:330)
- f1: Sessions excluded by lexical, over all arms' sessions, tested by binomial against p0 .05 at checkpoints and completion; a pause on p < .05 (jlens-qwen36/scripts/f_sessions.py:419-421, :431-433; archive/RESULTS-cycles3-4.md:403). f_audit_patterns.json's _doc says junk precedence keeps it to 'coherent own-pair emissions'.
- F0m: There is no lexical bar in Q-F0, because every banner names labels (valence_core/m/bars.py:32-34; m:330). Lexical is only a counter (audit.py:579-580).
- effect: Descriptive and stop-rule only. Under m, a raised rate of lexical exclusions, the priming exposure that (1) discloses, is reported but pauses nothing, whereas f1's monitor would have paused.
- evidence: From code and spec. f1's archive has 2 CORR lexical exclusions in 64 sessions.
- refuter: The claim holds on both sides. Two parts of its wording need tightening.

f1's side, checked:
- In jlens-qwen36/scripts/f_sessions.py, lines 416-421 count sessions whose exclude_reason starts with "lexical". The count runs over every row of the run file: all six arms, the sham included, forced and free-round lexical exclusions together. Each count is tested by binom_p_ge at p0 .05.
- The test runs when a contrast arm reaches n = 24 (GUARD_CHECKPOINTS = (24,), :90) and again at completion.
- Lines 431-433 add a "pooled LEXICAL" pause when p < .05. At a checkpoint that pause stops the run (:664-670, "CHECKPOINT PAUSE").
- archive/RESULTS-cycles3-4.md:403 declares "pooled own-pair lexical p0 = .05".
- The evidence figure reproduces. data/f/sessions.jsonl has 2 lexical-excluded CORR sessions out of 64: s4 "lexical:prism@free4" and s25 "lexical:maple@free4". Across all arms the pooled count is 19/344, P about .36.

F0m's side, checked at 5f7b968:
- bars.py:32-34 reads "no lexical bar in Q-F0 or on OLMo (every banner names labels)".
- m:330 says the same: "in Q-F0 and on OLMo every banner names labels, so the lexical bar has no domain there and lexical is reported only".
- bars.py:863 keeps lexical claims out of the round_degeneracy numerator.
- stages.campaign_look (:1724-1728) holds round_degeneracy, the guard and the read flags, and has no lexical bar.
- audit.py:579-580 is the lexical counter only.
- The difference is observable: it changes when a campaign pauses.

Classification: none of §2.7's fourteen (m:267) names f1's pooled monitors.
- Item (1) discloses the priming exposure that could raise lexical exclusions. It does not mention that the bar which would have caught a rise is gone.
- Items (6) and (13) cover the audit and the arm interleave and stop, not the monitors.
- So "beyond" is correct. The difference is declared elsewhere in the proposal (§6, m:330, "adapted from f1's session-unit monitor (archive:403)" and given a domain only in Q-F3), so it is a declared design change rather than a surprise the port found. It still belongs on G-PORT's beyond-the-fourteen list.

Imprecisions, not grounds to refute:
1. "Pauses nothing" overstates it. Under m, a forced-round (pre-pick) lexical exclusion still counts toward the exclusion guard at every look (m:316; stages.py:1700-1702 counts forced-phase exclusions). That guard binds two ways on Qwen: one-sided Fisher against the matched sham, and exact binomial against an absolute .20. So a large or one-sided rise in pre-pick lexical exclusions can still pause Q-F0. What m lacks is a bar on the lexical class itself at p0 .05, and any bar on free-round lexical exclusions. Because A0's and A0s's banners both name labels, a priming rise shared by both arms would slip past Fisher. It would also slip past the absolute .20 bar unless it is large.
2. At completion, f1 does not pause; it prints "COMPLETION FLAGS ... discussion before any claim" (:672-677).

Effect: the effect line's grading as descriptive and stop-rule only is right. Pauses never change a verdict, so this does not bear on A0's comparison with f1's primary or any secondary.

A related gap outside this claim: f1's other two pooled pauses also have no Q-F0 bar.
- CAP: cap hits over rounds, p0 .10, :422-424.
- MASS: low label mass over choices, p0 .20, :425-427.
Under m, label mass is only reported and cap_hit is only a counter. These two belong in their own entries.

#### D59. Cap-hit and low-label-mass bars dropped to reported counters; low mass judged on the unrounded value
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: Cap hits: p0 .10 over all rounds. Low mass: label_mass < .2 over all reads, p0 .20. Both bars pause on p < .05 (jlens-qwen36/scripts/f_sessions.py:422-433). Low mass is judged on label_mass rounded to 4 dp (:363).
- F0m: low_label_mass = the unrounded label_mass < LOW_LABEL_MASS 0.20 (valence_core/m/scaffold.py:398-409; e2d/runner.py:58). It is reported only: at looks the sham arm reports all reads, the contrast arm first reads of domain sessions only (stages.py:1705-1721). cap_hit is a counter with no bar (audit.py:586-587; m:330).
- effect: Descriptive. The rounding difference never occurs in f1's archive.
- evidence: 0 of 1,745 f1 reads have a rounded label_mass of exactly 0.2 (scratch f1_domain.py). f1 CORR cap hits: 2 of 597 rounds.
- refuter: I checked both sides and the claim holds. The F0m side was read at HEAD 5f7b968 with git show.

f1's side:
- jlens-qwen36/scripts/f_sessions.py:422-424 is a cap bar: binom_p_ge(cap_x, cap_n, 0.10), pooled over every row's n_rounds across all six arms.
- :425-427 is the low-mass bar: label_mass < 0.2 over every read of every arm, p0 .20.
- :431-433 adds a pause when p < 0.05.
- :363 stores label_mass as round(ch["label_mass"], 4), and :426 tests that stored, rounded value.
- The docstring (:21-22) declares both bars ("cap-hits p0=.10; low-mass p0=.20").

F0m's side:
- scaffold.py:398-409 sets low_label_mass = read["label_mass"] < low_mass. _read_dict (:356-363) takes float(d["label_mass"]) without rounding, and readout.py's as_dict (:81-83) does not round either.
- runner_qwen.py:55 and :187 pass e2d/runner.py:58's LOW_LABEL_MASS = 0.20.
- stages.py:1705-1721 and :1750 report the flags at looks: all reads on the sham arm, first reads of domain sessions on the contrast arm. The gate report does the same through _contrast_first_reads (:1361-1369, :1422).
- audit.py:586-587 notes cap_hit as a counter only.
- bars.py declares no cap or label-mass bar. Its only binomial bars are round_degeneracy, the reasoning-line bar, lexical and the guards.

Archive check, re-run against data/f/sessions.jsonl:
- 1,745 reads; 0 have a stored label_mass of exactly 0.2. The nearest is 0.1997, which counts as low under both rules.
- Rounding to 4 dp can only change the verdict when the rounded value is exactly 0.2. So the rounding difference never occurs in the archive, as the claim says.
- CORR: 64 sessions, 597 rounds, 2 cap hits.
- Neither f1 pooled bar was near firing: cap 14/3,074 against p0 .10, low mass 165/1,745 against p0 .20. "Descriptive, no effect on A0 vs f1's primary" is right.

One small citation point: m:330 supports "no cap bar" only by leaving it out of its bar list. The positive statement that cap_hit is a declared counter is at m:314. This does not refute the claim.

Classification is "beyond". None of §2.7's fourteen (m:267) mentions these monitors:
- (6) is the audit class list, not the pooled monitors.
- (13) is the interleave and per-arm stop, not pause bars.
- (9) and (12) concern the reads' verify cadence and window, not low-mass monitoring.

Outside the fourteen, m:283 discloses that the low-mass half is not carried ("f1's binomial monitor at p0 .20 ... is not carried"). I found nothing in the proposal that discloses dropping the cap-hit monitor (p0 .10). Neither half, nor the rounding change, appears in the fourteen, so the G-PORT entry should list both halves, citing m:283 beside the low-mass half.

#### D60. Pre-campaign degeneracy gates and campaign degeneracy looks (rule-21 domains), against f1's smoke bars
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: f1's smoke bars (jlens-qwen36/scripts/f_sessions.py:497-511, :629-662) are: lexical by session binomial p0 .05; audit exclusions as a hair trigger at > 20% of sessions on the 'unprovoked' domain (sham arm plus sessions whose exclusion was in the P config); cap hits > 10% on sham plus P rounds. f1's screen had no round-degeneracy bar (checkpoint_eval :391-434).
- F0m: round_degeneracy counts rounds claimed by v2 or echo, on sham-template sessions only, excluded sessions' rounds included. It is evaluated by exact binomial with p0 .05 and P <= alpha at G-TIME-F0 and G-F0m-Qwen (bars.py:530-537, :568-591, :853-903) and at every campaign look (bars.py:126-129). Contrast sessions are reported beside, with forced rounds as counts only per ruling (h).
- effect: None on the comparison. These are gates and pauses: the domain moves from 'sham + P' to 'sham template only', and the unit from sessions to rounds.
- evidence: From code and spec (m:271, m:330).
- refuter: The core difference holds. f1 had no round-unit degeneracy bar. Its smoke bars (smoke_bar_check, f_sessions.py:497-511, wired at :629-662) were: lexical exclusions over all smoke sessions by exact binomial at p0 .05, firing on p < .05; audit exclusions as a rate threshold; and cap hits above 10% of sham+P rounds once there were at least 10 rounds. The screen's checkpoint_eval (:391-434, GUARD_CHECKPOINTS=(24,) at :90) carries the exclusion guard plus pooled lexical, cap and low-mass bars, and no degeneracy bar. f1 logged per-round `degen` and `post_degen` (:317, :333, :368-372) but nothing gated on them. At HEAD, F0m declares round_degeneracy as an exact binomial with p0 .05 and P <= alpha, on sham-template sessions only. The bar factory is bars.py:530-537 and Q-F0's set is :568-591. stage_end_eval (:853-903) counts v2/echo-claimed rounds, keeps excluded sessions' rounds (PIN :859-865) and refuses contrast sessions (:874-876). The same bar runs at every campaign look: bars.py:539-545, cadence :468-469, evaluated in stages.py:1724-1752 at HEAD.

Classification: beyond the fourteen is correct. Item (6) covers the audit classes and claiming order, which make up the numerator. Item (13) covers the interleave and per-arm stop at floor. None of the fourteen covers the gate stages, the bar domain (sham+P to sham template), the unit (sessions to rounds), the p0, the cadence or the P <= alpha rule. The effect is none on A0's comparison with f1's primary or secondaries: these are stops and pauses, and resume only skips sessions already on disk.

Imprecisions to fix, none of them refuting:
(1) The anchor "bars.py:126-129" for the campaign looks is wrong. Those lines are the body of _count. Use bars.py:539-545 / :468-469 and stages.py:1724-1752.
(2) f1's audit smoke bar takes only its numerator from the unprovoked domain (sham arm or exclude_cfg P, :114-117). The denominator is n_done, which is all smoke sessions. The bar is armed only at n_done >= 6 (:506). Calling it a "hair trigger" repeats the docstring, but it is really a >20% rate threshold.
(3) "Forced rounds as counts only per ruling (h)" describes the post-ruling spec and the uncommitted working tree, not HEAD. At HEAD, readrule._contrast_block (:565-585, with _round_counts :522-536) reports contrast forced rounds with claims by class and excluded_at_forced by class.
(4) The F0m side does not say that f1's smoke lexical and cap bars have no Q-F0 counterpart (m:330: lexical is reported only in Q-F0; no cap bar is declared in bars.py). That is probably a separate difference, not an error in this one.

#### D61. Bar boundary: f1 fires on p < .05; m fires on P <= alpha
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: jlens-qwen36/scripts/f_sessions.py:412-415, :431-433, :503-504 (all `p < 0.05`).
- F0m: valence_core/m/bars.py:1-15, :158-162, and the Fisher branch in Bar.evaluate (:416-426), all exact rationals with `<=`. The spec is m:271 ('a bar fires iff its exact one-sided P <= alpha').
- effect: Pause or stop only. A tie fires in m and not in f1, e.g. a Fisher P of exactly 1/20 (the bars.py self-test, :1043-1045), or G-TIME-F0's n = 1 claim.
- evidence: bars.py self-test 'Fisher ties at exactly 1/20 fire under <=, not under f1's <'.
- refuter: The claim holds; every anchor checks out against f_sessions.py and HEAD 5f7b968.

f1's side: lines :412 and :414 (guard, absolute and sham-relative), :432 (the pooled LEXICAL/CAP/MASS bars) and :504 (smoke lexical) all test `p < 0.05`. f1 computes its binomial in floats with lgamma/exp (:144-151) and its Fisher as an int/int float (:154-159).

m's side, at HEAD: `fires` (bars.py:158-161) and `fisher_fires` (:210-211) test `<=` over exact Fractions. So does `Bar.evaluate`: the Fisher branch at :416-426 sets `exceeds = p <= self.alphaq`. The binomial branch is really :427-430, which matters more than :158-162 because it is the evaluate path the stages call. The docstring at :1-15 and m:271 ("A bar fires iff its exact one-sided P <= alpha", STOP-8 §C item 123) state the rule.

I checked the tie independently with f1's own functions, in scratch under step5/refute-barboundary:
- At n=1, x=1, p0 .05, f1's `binom_p_ge` returns 0.05000000000000001. `< 0.05` is False, so f1 does not fire. m gets exactly 1/20, and 1/20 <= 1/20 fires. This is the G-TIME-F0 round-1 case, which m:271 declares.
- For all six Fisher ties in the bars.py self-test (:1042-1045), f1's `fisher_one_sided` returns exactly 0.05, which is not < 0.05. m fires on all six.
- One nit on the evidence: the self-test's "not under f1's <" check actually calls `session.fisher_two_groups`, not f1's function. Running f1's formula directly gives the same answer, so the point stands.
- I searched n <= 160 and k <= 40 at p0 .05, .02, .10 and .20. The binomial tie P = 1/20 exists only at (k=1, n=1, p0 .05), and that is the only place f1's float rule and m's exact rule disagree. The binding binomial ties are that single case. Fisher ties are the other source.
- On the effect: f1's screen verdict (:482, `conj3 = p < 0.05`) also uses `<`, against m's `<=` at p0 .5. I checked n <= 200 at alpha .05 and .01 and found no disagreement. Tail probabilities are k/2^n, which can never equal 1/20 or 1/100. So the stated effect, "pause or stop only", is right: the difference never reaches A0's comparison with f1's primary or its secondaries.

Classification: none of §2.7's fourteen (m:267) covers it. Item (13) is about the interleave and per-arm stop at floor, (6) is the audit, and (9) is verify cadence. None of them concerns where a bar's firing boundary sits. m:271 declares the convention, but it is not on the §2.7 disclosure list, so it is a difference beyond the fourteen. Its effect is limited to stage pauses and stops. A related point belongs to a separate claim: m's Fisher guard drops f1's `sh_n >= 12` arming minimum (f_sessions.py:408, against the PIN note at bars.py:420-424).

#### D62. Termination counter: pattern string per round, tabulated by (arm, cfg, round position), becomes a bool keyed (template, phase)
- finder's classification: beyond; refuter: refuted=False, classification beyond (the counter's record and tabulation). The v2-claim sub-assertion belongs to §2.7 item (6), the audit, and is wrong on f1 CORR's data anyway.
- f1: `term` = the first matching termination regex (jlens-qwen36/scripts/f_sessions.py:321-325), tabulated as (arm, cfg, round-pos) over ALL sessions (:447-453).
- F0m: `termination` = whether any pattern matches (valence_core/m/scaffold.py:304-305, :392), counted as (template, phase) (audit.py:588-589). It uses the same pattern file, sha16 014b3940d62401b0 (scaffold.py:66). In m, a `===\s*[Ee]nd` attempt on a line of its own is also a v2 banner_terminator claim, which f1's junk `===\s*Config` misses.
- effect: Descriptive. Which pattern matched is not recorded. The position and property tabulation can be rebuilt from the rounds. Termination attempts now also count as degeneracy and exclusion events.
- evidence: f1 CORR: 9 termination rounds, all `===\s*[Ee]nd`. One of them, s48 free5, is unclaimed in f1 and a v2 claim under m (scratch find_content.py).
- refuter: The headline holds, and I checked it against both codebases. f1 stores `term`, the first matching regex string or None (jlens-qwen36/scripts/f_sessions.py:319-325, saved in rounds_log at :333). It tabulates that as (arm, cfg, pos) over all rows, excluded ones included (:447-453). m stores `termination` as a bool from any() (scaffold.py@5f7b968:304-305, :392). It notes it under (template, phase) only (audit.py:588-589). The PIN at audit.py:551-553 says the keys are "never a tag, item, round index or property (D13)", and m:314 defers the property breakdown to VERDICTS. Both sides load the same file: 014b3940d62401b0 for jlens-qwen36/data/configs/f_termination_patterns.json and for the repo copy. One small extra difference: f1 only prints the sha (:559-560), while m asserts it (scaffold.py:299-300). None of §2.7's fourteen items (m:267) mentions this counter, its field or its keys, so "beyond" is right. The effect is descriptive. m stores each round's text, ri/ci and property, so the matched pattern, the round position and the cfg/property split can all be rebuilt. Dropping the cfg and position keys is deliberate blinding (m:271), so that rebuild belongs at VERDICTS.

Three supporting statements are wrong:
(1) The evidence is wrong. f1 CORR does have 9 termination rounds, all `===\s*[Ee]nd`, in sessions s16 (positions 6 and 8), s25 (6), s55 (2), s58 (6) and s61 (6-9). But s48 is not among them: every s48 round has term=None, and no pattern matches anywhere in its transcript. Its free5 text is '=== END OF EVALUATION SESSION ==='. f1's patterns and m's identical patterns are case-sensitive, so neither side counts it as termination. m's v2 banner_terminator does claim that round while f1's case-sensitive fragments miss it, but that is an audit difference under item (6), not a counter difference.
(2) All 9 f1 CORR termination rounds were already audit-degenerate in f1, claimed by `frame:evaluation session` or `frame:Config evaluation session`. My rerun of m's QwenTaskRoundAudit on those texts claims all 9 as v2 through the same frame fragment, not banner_terminator. So f1's junk pattern `===\s*Config` missing them changes nothing. Also, banner_terminator only matches a whole line that starts and ends with two or more '=' (`(?im)^\s*={2,}[^\n]*={2,}\s*$`), not any `=== End` line.
(3) "Now also count as … exclusion events" is wrong. m's run scope for Qwen, `qwen_ends`, follows f1's rule (audit.py:501-506): any claim excludes in a forced round, only a lexical hit excludes in a free round (f1 :338-341 and :366-373). For CORR, m's run scope adds no new degeneracy or exclusion events; free-round claims show up only in the strict scope reported beside it, which is a separate difference.

Scratch check: /private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/refute-term-counter/chk.py

#### D63. Echo class specifics on F0m: complete-line rule, 'Reasoning (one line):' in the echo set, echo pre-empting lexical
- finder's classification: §2.7 (6); refuter: refuted=False, classification §2.7 (6). It names "m's echo class and the claiming order", and m:261 defines both: a verbatim, whitespace-normalised complete "Note:" line or `Reasoning (one line):`, claimed in the order v2 → echo → v4 → lexical. (1) supplies the Note lines that can be echoed. Nothing here goes beyond the fourteen.
- f1: f1 has no banner Note lines and no echo class (f_sessions.py:65, :298). A label copied into a response is a lexical claim (:318).
- F0m: Echo = containment of the whitespace-normalised complete line, final period included, case-sensitive (valence_core/m/audit.py:114-147). The Qwen echo set on F0m = the banner Note lines plus 'Reasoning (one line):' (audit.py:158-163). Echo is claimed before lexical (audit.py:443-453).
- effect: Whole-session validity only; domain composition is barely affected. At a forced round, a verbatim TOLD copy excludes either way (echo vs lexical in f1-like terms). A verbatim COMMON copy excludes only because echo exists, and a COMMON copy without its period gets no class and the session runs on. At a free round, a verbatim TOLD copy is post-choice degeneracy and does not exclude, where lexical would have excluded it. This is covered by (1) and (6).
- evidence: runner_qwen.py self-test cases at :309-335 (finding N6) and :293-298.
- refuter: The claim holds; I checked both codebases at HEAD 5f7b968 (audit.py, runner_qwen.py and banner.py are unchanged from HEAD in the working tree).

f1's side is correct. f_sessions.py:65 sets SESSION_BANNER to just "=== Config evaluation session ===\n" and :298 starts the transcript with it, so f1 has no Note lines. f1's audit_degenerate (:127-141) has only empty/special/frame/junk classes, so no echo class. At :318 an own-pair label in a non-degenerate response is a lexical hit. The "no echo class" point would be better cited to :127-141 than to :65/:298, but the claim is not wrong.

F0m's side is correct. audit.py:114-147 (harness_echo) normalises whitespace in both strings, checks case-sensitive containment of the complete line, and gives Qwen no form without the period (that form is OLMo-only). audit.py:158-163 builds the echo set as the Note lines plus "Reasoning (one line):". audit.py:443-455 claims in the order v2 → echo → content → lexical. The cited self-tests are at runner_qwen.py:293-298 and :307-335.

I also ran the m audit wrapper (no model) over A0/A0s × clause 0/1 × forced/free; script at scratchpad/step5/refute-echo/probe.py:
- Verbatim TOLD at forced: echo, excludes, with a lexical hit underneath, so it would exclude either way.
- Verbatim COMMON at forced: echo, excludes. v3 returns no exclusion, so it excludes only because echo exists.
- COMMON without its period: no claim at either phase; the session runs on.
- TOLD without its period: lexical, which excludes at both phases.
- Verbatim TOLD at free: echo, which does not exclude (run scope), although a lexical hit is present.
- "Reasoning (one line):": echo; the lowercase form gets no claim.

Every stated effect reproduces.

Two minor understatements; neither is a refutation:
1. The effect is not "whole-session validity only". When echo pre-empts lexical, the round's class changes: it counts in harness_echo and in round_degeneracy's numerator instead of the lexical counter. At a free round, an echo claim does not end the session where lexical would, so later picks are still read. That bears on secondaries that use picks 2-6, not on the first pick, which is read before any free round.
2. "Domain composition is barely affected" is a guess about rates. A forced-round COMMON or Reasoning echo does remove a session from the domain.

The covered_by field says (6), while the effect text says "(1) and (6)". The classification is right either way: these are the m:261 specifics of the echo class and claiming order that (6) discloses.

### Lens records-stats

**Covered (the lens's own statement):** LENS records-stats: what each round, choice and session records, verification (G-VER, the read-verify cadence, insulation), stdout, checkpoints and resume, every monitor and bar (p0, α, operator, cadence, domain), floors, the launch rule and terminal conditions beyond (13), the primary, E, conjuncts, outcome logic, secondaries and counters, and blinding. Judged against HEAD 5f7b968 via git show copies in scratchpad/step5/records-stats/head/, never the working tree (readrule.py, stages.py and m_sessions.py may be in edit). The analyzer (scripts/m_analyze.py) is not built at HEAD, so m's DV and analysis side is cited from the spec (m:306-330). Archive figures computed model-free from data/f/sessions.jsonl (sha16 d49913e5ffdfb935) with the jlens venv python: primary under m's domain 30/58 vs 28/56 of record; E .0588 vs .0455; guard numerators 8 to 6 (CORR, of 64) and 7 to 6 (sham, of 40); pre-pick per-property P 5 vs Q 1 vs the 7-vs-1 of record; reads 42/346 below .20 with none within .00005 of .20; first reads verified 30 of 58. Beyond-fourteen items that bear on A0's comparison with f1's primary: the domain rule, and E's domain plus matching. The rest are descriptive, verdict-criterion or monitor-only. Read-only on the repo; no model, tokenizer or network; nothing written outside the scratch directory.

**Internal, no effect (the lens's list):**
- first_free_pick_P: f1 = choices[0].picked_cfg == 'P' if choices else None (f_sessions.py:382-383); m = choices[0].pick == P if domain else None, with domain asserted == bool(choices) (scaffold.py:431-432, :445). Equal on every session.
- lexical_hit: the same regex (\b{tag}\b on text.lower()) and the same own-pair order [P, Q] (f_sessions.py:119-124; valence_core/session.py:76-85; runner_qwen.py:147).
- Verify-KL halt: f1 halts if kl != 0.0 (f_sessions.py:213); m halts unless type(kl) is float and kl == 0.0 (guard.py:131-137). Both halt on NaN and on any nonzero value.
- p_a = pa/(mass + 1e-12), and ties go to the menu-first label, in both (f_sessions.py:202-203; readout.py:113-116).
- n_tok excludes the stop token, and content_seen gates the newline stop, in both (f_sessions.py:183-189; qwen_mlx.py:292-323).
- The Fisher tail is the same quantity, P(X >= a) under the hypergeometric (f_sessions.py:154-159; bars.py:198-208). Only the float vs exact arithmetic differs (see the operator item).
- STOP_CAP 60, TEMP 0.7, the termination-pattern file (sha16 014b3940d62401b0) and the single-token label check are the same. m adds a distinct-id check and pins the term file's sha at load (scaffold.py:295-301; guard.py:141-156).
- f1's FDBK-only `verdict` field (always False on CORR) and its unused `oop` (f_sessions.py:280) have no m counterpart.
- f1 rounds by_map to 4 dp before the map-sign test (f_sessions.py:472-473). No effect at these n.
- UNSURE: f1 computes the choice softmax in MLX float32 (f_sessions.py:197-200); m uses a float64 numpy softmax of the same float32 logits (readout.py:44-48, :107-110; qwen_mlx.py:171-176). Pick, label_mass and top-1 agree except possibly at sub-ulp near-ties of the two label logits, where float32 rounding could turn a strict preference into a tie (which goes to menu_a).

#### D64. Primary's domain: whole-session validity (f1) vs reached-the-first-read (F0m)
- finder's classification: beyond; refuter: refuted=False, classification beyond (none of §2.7's fourteen at m:267 covers it; the rule and f1's figures appear only in §4, m:306-308)
- f1: analyze() builds `valid = [r for r in rows if not r.get("excluded")]` (jlens-qwen36/scripts/f_sessions.py:439) and reads first_free_pick_P only from those rows (:461-462; per map :468-471). `excluded` includes a free-round lexical exclusion after the pick (:373-375), so such a session leaves f1's primary.
- F0m: The record's `domain` = 4 forced rounds, none claimed, no forced hair trigger and no forced exclusion. It is asserted equal to 'reached the first read' (valence_core/m/scaffold.py:428-432), and first_free_pick_P is set iff domain (:445). A free lexical exclusion keeps the domain (runner_qwen.py:16-20, :199-205). Spec: m:306-308.
- effect: Bears on A0's comparison with f1's primary. On f1's own archive m's rule gives CORR 30/58 (Δ_c = +.017; map A 19/30, map B 11/28; one-sided p = .448). f1's primary of record is 28/56 (Δ_c = .000; 18/29 and 10/27; p = .553). The two sessions that differ (s4 and s25, both lexical@free4) both picked P first.
- evidence: Computed with the jlens venv python from data/f/sessions.jsonl (sha16 d49913e5ffdfb935): 58 CORR sessions reached a first read (30 P); 56 are whole-session valid (28 P). data/f/screen_analysis.json gives CORR n 56, delta 0.0. §4 (m:308) states the rule and quotes 28/56 of record, but none of §2.7's fourteen lists it.
- refuter: The claim holds; I checked both codebases and found nothing to refute.

f1's side. `analyze()` sets `valid = [r for r in rows if not r.get("excluded")]` at jlens-qwen36/scripts/f_sessions.py:439. It reads `first_free_pick_P` for the arm from `valid` only (:461-462) and builds the per-map split from `valid` (:468-471). A free-round lexical hit after the pick sets `excluded=True` with reason `lexical:{hit}@free{ci}` (:373-375), so that session drops out of f1's primary. This matches PROPOSAL-f:101-102: "n = 48 valid sessions ... Primary = first free choice".

F0m's side, at HEAD 5f7b968.
- `domain` is defined as 4 forced rounds, none claimed, no hair trigger at forced, no exclusion at forced. It is asserted equal to "reached the first read" (valence_core/m/scaffold.py:428-432).
- `first_free_pick_P` is set iff `domain` (:445).
- A free-round lexical hit excludes the session but keeps the domain (runner_qwen.py:16-20, :199-205).
- readrule.py:543-557 and :605-613 count domain sessions and first picks the same way.
- The spec, m:306-308, says "Nothing after the first pick removes a session from the domain".

Numbers. I recomputed with the jlens venv from data/f/sessions.jsonl (sha16 d49913e5ffdfb935).
- m's rule: CORR 30/58, Δ = +.0172, map A 19/30, map B 11/28, one-sided p = .4478.
- f1's rule: 28/56, Δ = 0, 18/29 and 10/27, p = .5531. This matches data/f/screen_analysis.json (n 56, delta 0.0, p 0.55307).
- The two sessions that differ are s4 (`lexical:prism@free4`, swap=True) and s25 (`lexical:maple@free4`, swap=False). Both picked P first.

Every cited line says what the claim says.

Classification. It is beyond the fourteen. Items (1)-(14) cover the banner, the delivery module, the dose and corruptor, the sham pool, the roster, the audit, the rng keys, the assignment, the verify cadence, the lens read, the round path, the read window, the interleave and stop, and the generation window. None covers the primary's domain. The rule and the 58/30 vs 28/56 figures are stated only in §4 (m:308). m:306 even labels the primary "f1's definition", although f1's domain was whole-session validity. So the difference is worth listing in G-PORT's entry.

Effect: it bears on A0's comparison with f1's primary, as the claim says. One more consequence the claim leaves out: m:308 gives the sham envelope the same domain rule. On f1's archive that makes the sham domain 34 sessions with E = .0588, against f1's 33 whole-session-valid shams with E = .0455 (f_sessions.py:454-456; s35, `lexical:saddle@free5`, P-first, is the difference). So conjunct (i)'s E also changes against f1's figure of record. Under either rule, CORR's Δ stays below E.

#### D65. Sham envelope E: one shared sham arm on whole-session validity vs the matched A0s arm on the domain
- finder's classification: beyond; refuter: refuted=False, classification Partly beyond, partly covered. The domain change is BEYOND the fourteen: §2.7 items (1)-(14) never mention it. The proposal does disclose it, but only in §3 at m:308 ("The sham envelope uses the same domain rule"). The "one shared sham for five contrasts vs a matched A0s" half is effectively COVERED by (13) (f1's six-arm interleave "the sham among them" vs two arms), together with (4) (the sham pool) and (7) (the item stream shared between contrast and sham session s). On its own that half does not change the E value applied to CORR. The finding should therefore be filed as beyond §2.7 for the domain half only.
- f1: pseudo = |mean(first_free_pick_P) - .5| over the valid rows of the single sham arm that serves all five contrasts (f_sessions.py:454-456). It is used as conjunct (1)'s threshold for every contrast (:478).
- F0m: E = |Δ_c(S)| pooled over the matched sham arm's domain (m:310). A0s is matched to A0 alone (m:180-182). The domain rule of m:308 applies to the sham.
- effect: Bears on the comparability of conjunct (i) with f1's. On f1's archive, f1's E = .0455 (18/33 valid shams). The same sham sessions under m's domain rule give 19/34, E = .0588.
- evidence: Computed from data/f/sessions.jsonl: sham whole-session excluded 7/40, pre-pick 6/40. §2.7 (4) covers only the pool's content (CORR_clean vs SHAM prompts), and (13) only the interleave. Neither covers E's domain or the one-sham-per-contrast matching.
- refuter: The claim holds; nothing in it is factually wrong.

f1's side: analyze() sets valid = not excluded (f_sessions.py:439). It computes pseudo = |mean(sham first_free_pick_P) - .5| over those valid sham rows only (:454-456), and uses that one number as conj1's threshold for every contrast in CONTRASTS (:478; CONTRASTS has five arms, ARMS adds the sham, :87-88). Under f1's rule a post-pick free-round lexical hit excludes the whole session (:373-375), so whole-session validity drops sessions that did reach a pick.

F0m's side: m:308 sets the domain to sessions with no exclusion-bearing event before the first read, says that nothing after the first pick removes a session, and says the sham envelope uses the same rule. m:310 defines E = |Δ_c(S)| pooled over the matched sham's domain. In the code at HEAD, scaffold.py:429-432 and :444-445 record domain as exactly "reached the first read", with first_free_pick_P set only on the domain. The runner_qwen.py docstring (:15-21) says the domain is kept after a free exclusion. No code at HEAD 5f7b968 computes E: VERDICTS analysis is not built. So F0m's E exists only as the proposal text, and the claim cites it correctly. The cite "m:180-182" is a table header plus row; only m:182 is the A0/A0s row.

Numbers recomputed from data/f/sessions.jsonl:
- 40 sham sessions, 7 excluded. 6 of those are pre-pick (5 at forced lexical or audit: granite x2, slate, prism, two frame audits).
- One is post-pick: session 35, lexical:saddle@free5, first pick P.
- f1's E = |18/33 - .5| = .04545, which matches screen_analysis.json sham_pseudo.
- Under m's domain rule the same shams give 19/34, E = .05882.
- CORR under the same rules: 28/56 of record vs 30/58 on the domain (consistent with m:308).

The effect stated (it bears on conjunct (i)'s comparability with f1) is correct. E rises from .0455 to .0588 on f1's own archive.

#### D66. Conjunct (iii): A0's α .01 and P <= α vs f1's p < .05
- finder's classification: beyond; refuter: refuted=False, classification beyond (none of §2.7's fourteen covers the test or its α). But it is not something the port reveals: the proposal declares it elsewhere, in m:182's tier column ("control α .01") and m:326. m:186 keeps A3 at f1's screen α .05 and cites PROPOSAL-f:101–106. The entry should list it as "declared in §2.4/§5, not in §2.7". The "P ≤ α vs p < .05" half belongs under "internal, no effect".
- f1: CORR is one-sided; screen conjunct 3 is `p < 0.05` on an exact tail computed as comb/2**n (f_sessions.py:474, :477, :482).
- F0m: A0 is a positive control at α .01 (m:180-182, m:326), tested by exact one-sided binomial vs .5 (m:310). Every criterion and bar fires iff P <= α (m:271), implemented in exact rationals (valence_core/m/bars.py:158-161).
- effect: Changes the criterion A0 is held to, not the first-pick share. Critical counts are 60/96 (cached floor) or 51/80 at α .01 (m:190), against f1's p < .05.
- evidence: m:190 lists the critical counts. f1's rule is the screen tier of PROPOSAL-f:101-106.
- refuter: The α half of the claim holds; the "P ≤ α" half has no observable effect and is partly mis-cited.

f1's side checks out. CONTRASTS includes CORR (f_sessions.py:87), and only DIFF is two-sided (:476). So for CORR, p = p_hi = sum(comb)/2**n (:474, :477), and conjunct 3 is `p < 0.05` (:482). PROPOSAL-f:106 says the screen test is "exact binomial p < .05 (one- or two-sided per the table)", and the table at :86 marks CORR one-sided.

F0m's side checks out. A0 is a "control α .01" arm (m:182), and positive controls are evaluated at α .01 (m:326). Conjunct (iii) is an "exact one-sided binomial vs 0.5 at the arm's α" (m:310). The critical counts at m:190, 60/96 and 51/80, reproduce exactly in my own run. Under f1's α .05 the same floors would need 57/96 and 48/80. So the change is real and observable: it moves the bar A0 must clear. It does not change the first-pick share or the 28/56 reference. Its effect on the comparison with f1's primary is on the verdict criterion only.

Three corrections:

(1) The ≤ vs < half is not observable for conjunct (iii). At p0 = .5 every exact tail is j/2^n, and α = 1/100 or 1/20 has a factor of 5 in its denominator, so P can never equal α. I checked exhaustively for n ≤ 299: none. "P ≤ α" and f1's "p < .05" give identical decisions at every n. This half is "internal, no effect".

(2) m:271 says "A bar fires iff its exact one-sided P ≤ α (the convention at every boundary, STOP-8 §C item 123)". Item 123 is about the G-TIME bars' lower boundary. m:271 says nothing about verdict criteria, and m:310's conjunct (iii) does not say ≤ or <. So "every criterion and bar fires iff P ≤ α (m:271)" overreaches.

(3) bars.py:158–161 is `fires()`, the bar rule. HEAD has no implementation of conjunct (iii); m_analyze.py belongs to G-ANL-F0 and is not built. The only link is the self-test: SPEC_COUNT_CASES at bars.py:736–739 checks the p0 .5 counts at α .01 through `fires()`.

A related point outside this claim: f1 tested CORR only toward P (p_hi). m's conjunct (iii) is tested "in the direction under test", which includes a REVERSE test toward corrupted (m:310, m:326). That belongs with the outcome-space difference, not with this one.

#### D67. Outcome logic: f1's screen_hit boolean vs m's ordered outcome set (CI, DEAD, INDETERMINATE, REVERSE)
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: screen_hit = conj1 ∧ conj2 ∧ conj3, with conj1 False when pseudo is None (f_sessions.py:478-483). No interval is computed. A reverse result is reported, never celebrated (PROPOSAL-f:89-91).
- F0m: Order: INDETERMINATE if no domain session or E undefined; then REVERSE; then PASS; then DEAD if the Clopper-Pearson 95% upper bound on Δ_c < +0.15; then INDETERMINATE. A map with no domain session fails (ii). The verdict sentence states the pre-pick exclusion rate beside its sham's and the guard's result (m:310, m:324-326).
- effect: Descriptive for the comparison (A0's label is a control verdict, not a screen hit). The map-sign conjunct is equivalent: f1 requires each map v >= 0 when d >= 0 (:479-481); m requires each map >= .5 toward the direction tested.
- evidence: f_sessions.py:467-483; m:310, m:326. The analyzer (scripts/m_analyze.py) is not built at HEAD 5f7b968, so m's side is the spec.
- refuter: The claim holds; I checked both sides against the sources.

**f1's side.** jlens-qwen36/scripts/f_sessions.py:478-483 computes `conj1 = pseudo is not None and (abs(d) if two_sided else d) > pseudo`, `conj2 = all(v is not None and ((v >= 0) if (d >= 0) else (v <= 0)) ...)` and `conj3 = p < 0.05`, then `hit = conj1 and conj2 and conj3`. analyze() computes no interval anywhere (grep finds no CI, Clopper-Pearson or Wilson). It also has no reverse branch: for one-sided CORR, `p = p_hi` and conj1 needs d > pseudo. A contrast with no first picks is skipped (`continue`, :463-464) rather than labelled. The archived data/f/screen_analysis.json has exactly this boolean form (CORR: delta 0.0, conjuncts [false, false, false], screen_hit false, hits []). The "reported, never celebrated" convention is at PROPOSAL-f:89-90; the claim cites 89-91, a trivial overrun.

**F0m's side.** m:326 gives A0's order verbatim: INDETERMINATE ("no read obtained") if there is no domain session or E is undefined, then REVERSE, then PASS, then DEAD if the CI upper bound on Δ_c < +0.15, then INDETERMINATE (terminal). m:310 defines that CI as two-sided Clopper-Pearson 95% on P, expressed on Δ_c, and says a map with no domain session fails (ii). m:326 adds that every contrast arm's verdict sentence states the arm's pre-pick exclusion rate beside its sham's, with the guard's result. At HEAD 5f7b968 there is no scripts/m_analyze.py, and nothing in valence_core/m implements DEAD, INDETERMINATE or Clopper-Pearson, so the claim is right that m's side is the spec. This is still a difference: outcome labels are observable outputs of "how sessions are analysed", not an internal refactor.

**The equivalence remark holds.** f1's v is a per-map mean minus .5, so v >= 0 is the same as share >= .5, and `v is not None` matches "a map with no domain session fails (ii)". f1 keys the sign to d's sign and m to the direction under test, but these agree wherever (i) holds, because (i) forces d > E >= 0 for PASS and d < -E <= 0 for REVERSE.

**Classification: beyond.** None of §2.7's fourteen (m:267) touches outcome or verdict logic. They cover the banner, CORR module, dose and corruptor, sham pool, roster and pairing, audit, rng keys, assignment, verify cadence, lens read, round path, read window, interleave and stop, and the generation window.

**Effect.** "Descriptive" is defensible: the rule changes the label, not the primary estimate Δ_c.

**One omission (not a refutation).** The outcome logic also changes the significance bar: A0's α = .01 (m:326) against f1's p < 0.05 (:482). The claim does not mention this, and it should be listed, under this item or its own, if no other lens covers it.

#### D68. Floors: what they count, the launch projection and the terminal conditions
- finder's classification: beyond; refuter: refuted=False, classification beyond (§2.7 (13) covers only the strict rotation and the per-arm stop at floor; the floor's counting rule, its sizes, the L projection, the hour cap, schedule exhaustion and below-floor handling appear in none of the fourteen)
- f1: N declaration: CORR 64 and sham 40 launched, 'all declared sessions run'. Valid floors are 48 per contrast and 32 for the sham, counted on whole-session validity. Below floor at completion means design-instance discussion (archive/RESULTS-cycles3-4.md:139-144; PROPOSAL-f:101). The plan is fixed via --n-arms (f_sessions.py:597-608). There is no hour cap.
- F0m: Floors: A0 96 cached / 80 uncached, A0s 32, counted on primary-domain sessions (m:180-182, m:247). L = ceil_unit(max(⌈1.15·floor⌉, N90(r))), with r the qualification valid rate, is a projection only (m:192). An arm launches until its domain floor, the unit's hour cap (terminal; session seconds accumulated, resume.py:986-998; stages.py:1911), a PI stop, or exhaustion of its committed schedule (PAUSE for the PI, stages.py:1919-1923; capacity MAX_UNITS A0 82 / A0s 30 balance units, schedule.py:142, :928). Below floor, the arm is analyzed as obtained, with shortfall and attained power stated and α unchanged (m:247). G-PWR raises n before the run (m:190).
- effect: Bears on n and power, not on the share. A session excluded at a free round counts toward m's floor; it did not count toward f1's 48.
- evidence: §2.7 (13) covers the rotation and the per-arm stop at floor only. The floor's counting rule, its sizes, the L projection, the hour cap, schedule exhaustion and below-floor handling are not among the fourteen.
- refuter: I checked both sides and the claim holds.

f1 side, every citation verified:
- archive/RESULTS-cycles3-4.md:139-144 gives the N declaration: SOLV/CORR/NOV 64, DIFF/FDBK 56, sham 40; "valid floors 48/32 protected"; "All declared sessions run"; below floor at completion goes to design-instance discussion.
- PROPOSAL-f-natural-reinforcer-screen.md:101 gives "n = 48 valid sessions ... + shared sham n = 32".
- f_sessions.py:597-608 builds the plan from --n-arms/--n-contrast/--n-sham, sorted by fractional progress, and runs all of it. The only stops are checkpoint pauses. There is no hour cap anywhere in the file.
- f1's floor counts whole-session validity. analyze() sets valid = not excluded (:439), and a free-round lexical hit sets excluded (:373-375).
- My recount of data/f/sessions.jsonl matches the record. Valid against reached-first-read: CORR 56 vs 58, DIFF 47 vs 49, FDBK 44 vs 48, SOLV 50 vs 52, NOV 53 vs 54, sham 33 vs 34. The below-floor clause fired on the valid counts (archive:86-87, DIFF 47, FDBK 44).

F0m side, checked at HEAD 5f7b968:
- Floors are FLOORS = A0 96 cached / 80 uncached, A0s 32 (schedule.py:99; m:182).
- Floors count domain sessions (stages.py:1906, :1909, :1935). The domain means the session reached the first read (scaffold.py:429-432). A free-round lexical exclusion keeps the session in the domain (runner_qwen.py:18-20; m:308).
- The hour cap is terminal: hour_cap_exceeded is at resume.py:986-998, the accumulation at :950, and the check at stages.py:1911.
- Schedule exhaustion pauses for the PI (stages.py:1919-1923). After that pause, only a PI stop ends the campaign (:1885-1892).
- Capacity is MAX_UNITS, 82 balance units for A0 and 30 for A0s (schedule.py:142, :928).
- L is a projection only (m:192). Below floor, the arm is analyzed as obtained with α unchanged (m:247). G-PWR raises n before the unit runs (m:190).

Classification: (13) names only the strict rotation and the per-arm stop at floor, against f1's fractional-progress interleave. None of the fourteen mention any of the following: the domain-versus-whole-session counting rule, the floor sizes, the L projection, the hour cap, the schedule-exhaustion pause, or the below-floor rule. So the claim is beyond the fourteen, with (13) covering only the stop half.

One refinement, which does not refute the claim: "not on the share" is too strong for the counting rule's source. The floor counts the same domain that the primary is computed on. f1's primary of record used whole-session validity: CORR 28/56. On f1's own data, m's domain gives 30/58, because of two post-pick lexical exclusions at free4, both on clean first picks (m:308). So the domain change also bears on A0's comparison with f1's primary. m discloses this only in §5 (m:308), not among the fourteen. Under m's rule, f1's DIFF (49) and FDBK (48) would have met the 48 floor.

#### D69. Exclusion guard: numerator, sham comparator, arming and cadence
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: Per contrast arm at arm n = 24 and at completion (GUARD_CHECKPOINTS (24,), f_sessions.py:90, :399-404). Numerator: whole-session `excluded` (post-pick free lexical included). Absolute binomial vs .20. Fisher vs the shared sham arm, armed only at sham n >= 12 (:408). Pause iff p < .05 (:412-415); the runner returns (:667-670).
- F0m: Per contrast arm at every look: every 40 launches pooled over both arms, and at the end (stages.py:1932, :2013; m:316, m:330). Numerator: pre-pick (forced-phase) exclusions (stages.py:1698-1702; bars.py:509-510). Fisher vs the matched A0s, armed at every look with no minimum sham n (PIN at bars.py:420-424). The absolute .20 bar is binding on Qwen. Both fire on exact P <= .05 (bars.py:198-212, :425-427). A fire pauses the unit; resuming requires recorded adjudication text (stages.py:1898).
- effect: Monitor only; it never changes a verdict. On f1's archive the numerator moves from 8/64 to 6/64 (CORR) and from 7/40 to 6/40 (sham).
- evidence: Computed from data/f/sessions.jsonl. §4 (m:316) states the pre-pick carry-over. It is not among §2.7's fourteen.
- refuter: Every part of the claim checks out against both codebases, read at HEAD 5f7b968 through git show, and against the archive.

f1's side (jlens-qwen36/scripts/f_sessions.py):
- :90 is GUARD_CHECKPOINTS = (24,).
- :399 skips an arm unless its n is 24 or the run is at completion.
- :398 and :401 count the numerator as sum(r["excluded"]) over all of the arm's sessions. That includes the free-round lexical exclusion set at :373-375.
- The absolute test is binom_p_ge(x, n, 0.20) (float).
- :408 runs Fisher against the one shared sham arm only when sh_n >= 12.
- :412-415 pause on a strict p < 0.05.
- :667-670 print CHECKPOINT PAUSE and return. At completion f1 only prints COMPLETION FLAGS (:675-677).

F0m's side (HEAD):
- stages.py:1931-1932 compute a look whenever (len(records)+1) % 40 == 0, counted over both arms together. LOOK_EVERY = 40 is set at resume.py:91. :2013 evaluates the end look.
- stages.py:1698-1702: _prepick counts a session only if its exclusion phase is "forced". :1734-1739 apply this to both A0 and A0s.
- bars.py:509-510: the guard's unit and numerator are pre-pick exclusions.
- bars.py:420-424: the PIN says the Fisher test runs at every look with no minimum sham n, and that f1's sh_n >= 12 is not carried.
- bars.py:587: _campaign(..., abs_binding=True), so the .20 absolute bar binds on Qwen.
- bars.py:425-426 (Fisher) and :428-429 (absolute) both fire on exact Fraction P <= alpha.
- stages.py:1893-1898: a paused campaign resumes only once adjudication text (or the PI's stop) is recorded.

Archive recount (data/f/sessions.jsonl, 344 rows, no smoke sessions):
- CORR: 8/64 excluded in total, 6/64 at forced rounds. The 2 post-pick exclusions are lexical:prism@free4 and lexical:maple@free4.
- sham: 7/40 in total, 6/40 at forced rounds. The 1 post-pick exclusion is lexical:saddle@free5.
These match the stated 8/64 to 6/64 and 7/40 to 6/40 exactly.

One locator is imprecise, which does not refute the claim: the cited bars.py:425-427 covers only the Fisher branch. The absolute bar's <= is at :428-429, and fisher_fires is at :210-211.

Classification: this is beyond §2.7's fourteen. None of items (1)-(14) is about the exclusion guard. Item (13) covers the arm interleave and the per-arm stop at floor, not the guard's cadence, numerator or arming. The adaptation is disclosed in §4 (m:316), which states the pre-pick carry-over and calls .20 a declared tolerance. It is not in the Appendix-D list at m:267.

Effect: the guard is a monitor only and changes no verdict (m:316). It does not bear on A0's comparison with f1's primary or secondaries; a pause can only stop or delay the run, or bring a PI stop, which is analyzed as obtained.

#### D70. Campaign bars: f1's pooled lexical, cap-hit and low-label-mass bars dropped; a round_degeneracy bar added
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: At checkpoints and at completion, binding exact binomials pooled over all arms: lexical session exclusions at p0 .05, cap hits per round at p0 .10, low label mass per choice at p0 .20. Pause on p < .05 (f_sessions.py:416-433).
- F0m: Q-F0's campaign bars are round_degeneracy (sham arm only; rounds claimed by v2 or echo; p0 .05; every look) and the guard (bars.py:539-565, :568-591). Lexical has no domain (every banner names labels) and is reported only (m:330). Low label mass and top-1-not-a-label are reported at looks: the sham arm over all reads, the contrast arm over first reads of domain sessions only (stages.py:1705-1721). cap_hit is a rule-23 counter only (audit.py:91-95, :596-597).
- effect: Descriptive. A run whose low-mass rate would have paused f1 (f1 CORR: 42/346 reads and 26/58 first reads below .20) cannot pause m. A sham-arm degeneracy rate f1 never monitored can.
- evidence: m:283 says f1's p0 .20 low-mass monitor is not carried; m:330 says Q-F0 has no lexical bar. The cap-hit bar's removal is stated nowhere in the spec. None of these is among the fourteen.
- refuter: The claim holds on both sides. One citation is wrong and one phrase overstates.

f1's side, checked in jlens-qwen36/scripts/f_sessions.py:
- checkpoint_eval at :416-433 runs whenever any contrast arm sits at GUARD_CHECKPOINTS = (24,) (:90) and again at completion. It pools all rows of all six arms, sham included, into three exact binomials:
  - lexical session exclusions at p0 .05 (:418-421);
  - cap hits per round at p0 .10 (:422-424);
  - choices with label_mass < 0.2 at p0 .20 (:425-427).
- Any p < .05 adds a pause (:431-433). The main loop stops on a checkpoint pause (:664-670) and prints COMPLETION FLAGS at the end (:672-677).
- The header at :21-22 declares the same set.

F0m's side, checked at HEAD 5f7b968:
- bars.py _campaign (:539-565), used for Q-F0 at :568-591, declares exactly three bars:
  - round_degeneracy@campaign: binomial_look, p0 .05, domain sham, numerator DEGEN_CLAIMS qwen = {v2, echo} (:85), on_fire pause;
  - the Fisher guard;
  - the absolute .20 guard.
- No lexical, cap-hit or low-label-mass bar exists anywhere in the package.
- campaign_look (stages.py:1724-1754) reports low label mass and top-1-not-a-label through _read_flags (:1705-1721). The sham arm counts all its reads; the contrast arm counts first reads of domain sessions only (first_only = (a == c_arm), :1750). These flags are reported, never barred.
- The spec says the same. m:330 gives Q-F0's lexical class no domain ("reported only"), and m:283 says f1's p0 .20 low-mass monitor "is not carried".
- cap_hit is only a rule-23 counter: it is declared at audit.py:91-95, tallied at :586-587, and summed in readrule's report at :537. No spec line says that f1's cap-hit bar was dropped. m:314 lists cap_hit only as a counter.

The archive figures reproduce from data/f/sessions.jsonl. In CORR, 42 of 346 reads and 26 of 58 first reads fall below 0.20. f1's pooled totals (165/1745 low mass, 14/3074 cap hits, 19/344 lexical) fire none of its bars, so the effect is descriptive, as claimed. These are pause bars, and pauses never change a verdict.

Two small corrections:
1. The cited audit.py:596-597 is the pre_pick_exclusion counter. The cap_hit tally is at audit.py:586-587.
2. "A sham-arm degeneracy rate f1 never monitored" is true of f1's campaign bars, but too broad as worded. f1 logged degeneracy for every round (the 'degen' field and post_degen), and its smoke stage had a trigger on audit exclusions in unprovoked sessions (smoke_bar_check, :497-510, :630-659). Neither was a campaign-level bar on the sham arm.

Classification: the claim is beyond the fourteen, as stated. None of §2.7's items covers campaign monitor bars:
- (6) concerns the audit's classes and claiming order, not bars over them.
- (13) concerns arm interleave and the per-arm stop at floor.
- (9) and (12) concern reads.

m:283 and m:330 disclose parts of this difference elsewhere in the spec, but not among the fourteen, and the dropped cap-hit bar is disclosed nowhere.

#### D71. Monitoring cadence and end evaluation
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: The guard runs at per-contrast n == 24 and at completion. The pooled bars run when any contrast reaches 24 and at completion (f_sessions.py:90, :399-417, :671-677). Completion flags mean 'design-instance discussion before any claim'.
- F0m: Looks every 40 launches pooled over A0 and A0s, and at the end (stages.py:1932, :1995-2020; LOOK_EVERY = 40, resume.py:91). The end look is not re-evaluated when the end falls on a 40-multiple. A fired end look pauses before analysis. The look index is checkpoint state, asserted equal to completed launches // 40 (resume.py:15-18, :579-588).
- effect: Descriptive.
- evidence: m:330. The 24-session checkpoint is f1's only interim look.
- refuter: Not refuted. Both sides check out against the code at HEAD 5f7b968.

**f1's side (jlens-qwen36/scripts/f_sessions.py):**
- :90 sets `GUARD_CHECKPOINTS = (24,)`.
- In a non-smoke run, `checkpoint_eval` is called after every session (:661) and once at completion (:672).
- The per-contrast guard runs only when that contrast's own n is 24, or at completion (:399). It is deduplicated by the `evaluated` set, and that set resets on each invocation (:615).
- The quoted completion line is at :676-677.

**One correction to f1's side.** The pooled bars (lexical, cap, low mass, over all six arms) are not deduplicated. They are re-evaluated after every session while any contrast's count stands at exactly 24 (:416-417), not once "when any contrast reaches 24". I replayed f1's plan ordering with the archived run's sizes (data/f/sessions.jsonl: 344 rows, CORR, NOV and SOLV 64 each, DIFF and FDBK 56 each, sham 40). The file order equals the replayed plan order exactly. The guard ran at sessions 127 (CORR), 128 (NOV), 129 (SOLV), 145 (DIFF) and 146 (FDBK). The pooled bars ran 11 times: sessions 127-131 and 145-150. So "the 24-session checkpoint is f1's only interim look" holds, but that checkpoint is a window of pooled evaluations, not a single look.

Two smaller points on f1's side:
- f1 re-evaluates the guard at completion even if the end coincides with n = 24, because the dedup key "end" differs from 24. That is a further contrast with m's no-re-evaluation rule.
- f1's completion flags only print. Analysis is a separate --analyze invocation.

**F0m's side (5f7b968):**
- `LOOK_EVERY = 40` is at resume.py:91.
- At stages.py:1931-1932, `at = len(records) + 1` counts launches pooled over both of `keys.templates(unit)`'s arms (A0 and A0s), and `campaign_look` runs only when `at % 40 == 0`.
- At the end (stages.py:2007-2020), when n is a multiple of 40 and the last look is at n, the recorded look is reused with no new evaluation. Otherwise the end look is evaluated once, and if it fires the status becomes PAUSE "before its analysis".
- The look index as state, verified as `completed_launches // 40`, is in the docstring at resume.py:14-18 and asserted at resume.py:579-588. A gate stage records no looks.
- Line citations are accurate to within one line.

**Classification.** It is beyond §2.7's fourteen. Item (13) covers arm interleave and per-arm stop, and item (9) covers the choice-read verify cadence. Neither covers the monitoring look cadence, and m:330 states m's cadence without contrasting it with f1's.

**Effect.** Descriptive is right: pauses are not verdicts and the verdict criteria are untouchable (m:330). The one link to reporting is that A0's verdict sentence quotes the guard at the unit's last look (m:325). That is reporting only.

#### D72. Hair triggers that stop the stage (none in f1's screen)
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: A ban string in a response is only `audit:special:{s}`. At a forced round it excludes and ends the session; at a free round it is `post_degen` and the session continues. The run continues either way (f_sessions.py:132-134, :339-345, :368-372).
- F0m: scaffold_absorption (any e2a ban string in any generation) records the trigger and returns at once, and the stage stops (runner_qwen.py:170-173, :201-203; stages.py:1936). A free-round hit keeps the session's domain. template_breakage (G-VER failure) and schedule_mismatch also STOP (bars.py:513-527).
- effect: None on the DV unless one fires. A fire ends the stage or campaign: analyzed as obtained after a PI stop, or NOT-RUN if no session reached a first read (m:284, m:324).
- evidence: m:271 (hair triggers, domain every session). f1 declared hair-trigger bars only in its smoke (:507-510).
- refuter: The claim holds on both sides. I read f1 directly and m at HEAD 5f7b968 via git show.

f1's side checks out. In jlens-qwen36/scripts/f_sessions.py, audit_degenerate returns `special:{s}` for a ban string (:132-134). At a forced round that becomes an exclusion and the session breaks (:339-345). At a free round it is only logged as `post_degen` and the session continues (:368-372). There is no run-level stop on a ban string. The screen's checkpoint_eval (:398-450) pauses only on binomial or Fisher bars (guard, pooled lexical, cap, low-mass). The smoke bars at :507-510 are rate thresholds, not one-hit triggers, although f1's docstring calls them "hair-trigger". The ban strings are the same e2a file in both: BAN_PATH is data/configs/e2a_ban_list.json (f_sessions.py:57), and audit.py:416-418 asserts the Qwen scaffold set equals v2's ban strings.

F0m's side checks out. In runner_qwen.py@HEAD, a scaffold hit records the hair trigger and breaks at forced (:170-173), where qwen_ends has also excluded it as v2. At free it breaks too (:201-203), which ends the session even though f1 would have continued. The self-test (:299-305) confirms that a free-round hit keeps the session's domain with no exclusion. The stage drivers turn the hit into a STOP: _hair_hit at stages.py:1024 is called at :1352 (gate stages), :1541 (G-ID) and :1936 (campaign), each followed by status STOP or a break. bars.py:513-527 declares scaffold_absorption, template_breakage and schedule_mismatch as hair triggers with domain "every" and on_fire STOP. G-VER failures stop via _verify_hit (stages.py:1011).

Effect: m:284 and m:324 match as cited (a PI stop analyzed as obtained, or NOT-RUN if no session reached a first read). The archive bears out "none on the DV unless one fires": f1's data/f/sessions.jsonl has 0 `special:` audit hits across all 344 sessions, the 64 CORR sessions among them.

Classification: beyond. None of §2.7's fourteen (m:267) covers stage-stopping hair triggers. Item (6) covers the audit's classes and claiming order, (8) the committed schedule itself, (9) the KL-verify cadence, and (13) the arm interleave and per-arm stop at floor. Item (8) entails that a schedule_mismatch check can exist, but it does not disclose the STOP. The hair triggers are declared in §3 (m:271), not among §2.7's fourteen.

Two small precision notes, neither of which refutes the claim:
1. The title's "none in f1's screen" overstates slightly. f1 did have one one-event run halt: the choice-read CONSTRUCTION INCIDENT, `raise SystemExit` on recompute KL != 0 (f_sessions.py:212-214). F0m keeps the same check in guard.insulated_read, so it is shared, not a difference. f1 had no ban-string, harness-verifier or schedule hair trigger.
2. The f0m_side should say outright that a free-round scaffold hit also ends the session, against f1's continue. That is implied by "returns at once" but not stated.

#### D73. G-VER: a per-session reconstruction before any record is written
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: There is no per-session verifier. The only construction check is the choice-forward re-forward KL on the verify_every cadence (f_sessions.py:205-215). The row is appended as generated (:386-387). Its harness bytes were first rebuilt after the fact, by G-PORT.
- F0m: verify.verify_and_mark rebuilds cell, keys, banner, seeds, items, deliveries, menu orders, each pick from its recorded read, and every harness byte from the record plus the committed schedule (verify.py:1-30, :83-262). resume.record_session refuses an unverified record (resume.py:908). The schedule directory is regenerated and sha-checked at every stage start (stages.py:342-355, :744-780).
- effect: None on the DVs. A mismatch is a hair-trigger STOP.
- evidence: m:284. §2.7 (9) concerns the choice-read verify cadence, a different check.
- refuter: The claim holds on substance. On the f1 side, jlens-qwen36/scripts/f_sessions.py has no verifier that checks each session. Its only construction check during a run is the re-forward inside choice_read (:205-215: KL must be exactly 0, otherwise SystemExit HALT). That check is gated by verify_every, which is 1 in smoke runs and 4 in real runs (:595, :608, :353). The row is appended as soon as it is generated (:386-387). The archived rows in data/f/sessions.jsonl (344 rows, 64 of them CORR) carry no verified field, and verify_kl is present on only 433 of 1,745 reads. The other checks in f1 run once at startup (forbidden modules, single-token tags, pattern shas) and are not per-session reconstruction.

On the F0m side, at HEAD 5f7b968, verify.verify_session (verify.py:83-260) and verify_and_mark (:263-267) rebuild each session through scaffold.m_config. They compare the cell, keys, banner and Note lines, and the label, role, pole, item, task_text, property and seed of every round. They check menu order, menu bytes and numbering, and that each pick agrees with its recorded p_a/p_b, with verify_kl exactly 0.0. They rebuild the transcript and pieces byte for byte and check the end rule, exclusion and strict_exclusion, hair triggers, domain, first pick and completeness. stages._launch runs it on every record (:1006). A failure becomes a STOP (:1348-1350, :1927-1930) and the record goes to the stop block. resume.record_session (:908) refuses any record whose verified field is not exactly True (:923-925). So the difference is observable: the record gains a verified field, and there is a new stop path that f1 did not have. "None on the DVs" is correct while the build works correctly.

Classification: beyond the fourteen. Item (9) covers only the cadence of the choice-read verify KL. G-VER is a separate per-session reconstruction, required by m:284 and not listed in §2.7. Two partial overlaps:
- G-VER's KL-exactly-0 check repeats what (9) already covers.
- The check of the schedule directory at stage start is part of the committed-schedule apparatus in (8), so it should be filed under (8), not as part of this difference.

Minor inaccuracies to fix before the entry uses this claim:
1. The citation stages.py:342-355 points at startup_problems, which runs the keys stream, banner-spec and corr-hygiene known answers, not the schedule check. The schedule regeneration is schedule.verify_schedule_dir (schedule.py:620-649). It rebuilds the schedule in memory, compares it byte for byte with the committed files and checks the manifest shas. load_committed (stages.py:744-778, call at :754) runs it at each stage start (:1304, :1507, :1811). "The directory is regenerated" overstates this: it is a regeneration compared against the files, never a rewrite. load_committed itself says it "never regenerates them".
2. The f1-side phrase "first rebuilt after the fact, by G-PORT" is imprecise. The step-4 build's self-test already replayed 10 archived f1 CORR rows through the same scaffold, and one review lens walked all 64 (RESULTS.md:58-60). G-PORT will be the first full replay that is formally claimed.
3. The refusal sits at resume.py:923-925, inside record_session, which starts at :908.

#### D74. Session-level record schema
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: 15 keys (f_sessions.py:377-385): arm, session, pair, swap, start_P, tag_P, excluded, exclude_reason (one string carrying the copied tag and the round index, e.g. `lexical:prism@free4`, `audit:frame:Config evaluation session@forced3`), exclude_cfg (P / Q / 'sham'), n_cap_hits, n_rounds, first_free_pick_P, rounds, choices, transcript. Rows are appended to one jsonl for all six arms.
- F0m: m-session-v1 (scaffold.py:424-450): schema, substrate, unit, stage, template, contrast, s, j, keys, cell {pair_index, pair, map, start, clause, P, Q}, banner, note_lines, path, rounds, choices, pieces (char offsets), transcript, excluded, exclusion {class, phase, detail} (no round index), strict_exclusion, domain, first_free_pick_P, hair_triggers, complete, seconds (perf_counter including reads, runner_qwen.py:206-209), verified. There is no exclude_cfg, n_cap_hits or n_rounds.
- effect: Descriptive. f1's exclude_cfg, which carries the 7-vs-1 reference, has no field in m; it must be rebuilt from the excluding round's role or property. The strict scope is recorded beside the lenient one.
- evidence: Key lists checked against archived rows: every f1 row has the same 15 keys. The swap→map and start_P→start re-expression follows §2.7 (8)'s schedule, but the field set is not among the fourteen.
- refuter: The claim holds, and the classification "beyond" is right. Effect: descriptive.

**f1 side checked.** jlens-qwen36/scripts/f_sessions.py:377-385 builds a row with exactly 15 keys: arm, session, pair, swap, start_P, tag_P, excluded, exclude_reason, exclude_cfg, n_cap_hits, n_rounds, first_free_pick_P, rounds, choices, transcript. All 344 archived rows in data/f/sessions.jsonl have that same key set. They cover six arms: CORR 64, NOV 64, SOLV 64, DIFF 56, FDBK 56, sham 40.
- exclude_reason is set at :340, :342 and :374. Its forms are `audit:{deg}@forced{ri}`, `lexical:{hit}@forced{ri}` and `lexical:{hit}@free{ci}`.
- exclude_cfg is set at :344 and :375 to 'sham' or the round's or pick's config. Archived values: Q 31, P 23, sham 7.
- n_cap_hits and n_rounds feed the pooled CAP binomial (:422-424). The smoke bars use exclude_cfg through `_ecfg` (:638-646).

**m side checked at HEAD 5f7b968.** In valence_core/m/scaffold.py, record() starts at :424 and the dict sits at :438-447. It has exactly the 26 keys the claim lists. cell is {pair_index, pair, map, start, clause, P, Q} (check_cell; schedule.py:202-203). exclusion is {class, phase, detail} (scaffold.py exclude()). detail is "lexical:<tag>" or "audit:<reason>", with no round index (audit.py:315-317). strict_exclusion is the first claim of any class (add_round). verified starts False and is set by verify_and_mark (verify.py:264-266). seconds is perf_counter over the whole session, reads included (runner_qwen.py:152, :206-209). There is no exclude_cfg, n_cap_hits, n_rounds, tag_P, swap or start_P. f1 recorded no seconds field; it only printed time.time() to stdout (:627).

**"7-vs-1 reference" is real.** The archived per-property exclusion table reads "CORR-P 7 vs CORR-Q 1" (archive/RESULTS-cycles3-4.md around :91-93). The m arc cites it as "the 7-vs-1 anomaly" (archive/PROPOSAL-m v1.3:175). The archived CORR rows give exactly 7 P and 1 Q in exclude_cfg.

**Two small precision notes; neither refutes.**
1. Only the lexical form of exclude_reason carries a copied tag. The audit form carries the audit reason, e.g. `frame:Config evaluation session`. The claim's own examples show this.
2. Every dropped field can be rebuilt from per-round data. Both runners end the session at the excluding round (f1 :343-346 and :348-349; m runner_qwen.py forced and free loops), so it is always rounds[-1], which has role, pole and property in m. f1's own analyze() does the same thing (:441-444). n_cap_hits equals the sum of per-round cap_hit, and n_rounds equals len(rounds). This supports "descriptive"; nothing bears on A0's comparison with f1's primary.

**Classification.** None of §2.7's fourteen (m:267) covers the record schema itself. Some field contents follow from covered items:
- cell, map and start re-express (5)/(8)
- keys come from (7)
- banner and note_lines from (1)
- path from (11)
- exclusion classes and strict scope from (6)

But dropping exclude_cfg, n_cap_hits and n_rounds, removing the round index from the exclusion record, and adding domain, complete, hair_triggers, pieces, seconds and verified are not disclosed anywhere in the fourteen. §2.6's printed-reason rule covers stdout and reports only, not the record, and it is not one of the fourteen either. A small storage difference also exists: f1 appends to one jsonl for all arms, while m keeps records in an atomic checkpoint JSON (resume.atomic_write_json). It is also beyond the fourteen, also descriptive.

#### D75. Per-round record: no grading, full render, raw hits, termination as a bool
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: cfg, tag, task (render[:40], truncated), seed, n_tok, cap_hit, lex (None whenever degen is set), degen (reason string), term (the first matching regex), graded (gold match via grade()), verdict (FDBK only) (f_sessions.py:326, :331-334). The model text lives only in the transcript.
- F0m: phase, ri|ci, n, label, role, pole, property, item (pool index), task_text (the full delivered render), template_index, seed, text, n_tok, cap_hit, stop_reason, audit {claim, detail, v3, advisory, echo_line, lexical_raw (the raw own-pair hit even under an earlier claim), scaffold, degeneracy}, termination (bool) (scaffold.py:385-396; audit.py:363-369).
- effect: Descriptive. m grades no task-round response (valence_core/m at HEAD contains no grader), so m's archive has no in-session accuracy by property; f1's has `graded` on all 597 CORR rounds. `term` no longer records which pattern matched.
- evidence: A grep of the HEAD m package finds no grade/gold use outside pool loading and hygiene. f1 archive rounds carry graded ∈ {True, False} and term ∈ {None, '===\s*[Ee]nd'}.
- refuter: I checked this against both codebases (m at HEAD 5f7b968 via git show) and the f1 archive. The claim holds and is correctly classed as beyond §2.7's fourteen items.

f1's side checks out. At f_sessions.py:326 `graded = grade(text, it["gold"])`. At :331-334 the round record is {cfg, tag, task: it["task"][:40], seed, n_tok, cap_hit, lex, degen, term, graded, verdict}. At :318 `hit = None if deg else lexical_hit(...)`, so lex is None whenever degen is set. At :321-325 term is the first matching regex out of the four in data/configs/f_termination_patterns.json. Rounds have no text field; the text is only in the session-level `transcript`.

The archive confirms it. All 3,074 rounds have exactly those 11 keys. There are 597 CORR rounds: graded is True 499 / False 98, term is None 588 / '===\s*[Ee]nd' 9, there are 0 rounds with both lex and degen set, and every task field is ≤40 chars.

F0m's side checks out. At scaffold.py:385-392 add_round records phase, ri|ci, n, label, role, pole, property, item, task_text, template_index, seed, text, n_tok, cap_hit, stop_reason, audit and termination. task_text is the delivered text, untruncated (RoundSpec :87). termination() at :304-305 returns `any(re.search(...))`, which is a bool. At audit.py:363-368 as_dict holds claim, detail, v3, advisory, echo_line, lexical_raw, scaffold and degeneracy. classify (:445-458) sets `lexical_raw = lexical_hit(text, op)` whatever the claim is, so it is the raw hit.

Grepping every file of valence_core/m plus scripts/m_sessions.py at HEAD finds `gold` only in corr.py's pool loading and hygiene checks, and no grade or normalize function. So m grades no task round. G-CAL's grader is not built yet.

Effect: descriptive. Termination counts are unchanged because "any match" and "first match is not None" pick out the same rounds; only which pattern matched is lost. No f1 analyzer reads `graded` (it appears only where f_sessions.py writes it), so A0's comparison with f1's primary is unaffected.

Classification: none of §2.7's items (1)-(14) mentions per-round record fields, in-session grading, task truncation or how termination is recorded. Item (6) covers the audit itself (v3/v4/v5, echo, claiming order), so the precedence rule behind f1's lex=None is (6). Recording a raw hit next to the claim, and the rest of this claim, are beyond.

Minor imprecisions, none of which refute the claim:
- f1's `verdict` is a bool on every round, True only on FDBK P rounds (False on all 597 CORR rounds), not an FDBK-only field.
- "render[:40]" is it["task"][:40]: the item text as delivered (the corrupted render on Q rounds), not the template-wrapped segment. m's task_text is the same kind of text, untruncated.
- m's audit dict also carries substrate and phase.

#### D76. Per-choice record
- finder's classification: beyond; refuter: refuted=False, classification beyond. The residue is not named by any of §2.7's fourteen: the field set and names (round vs ci/n, picked_cfg vs picked_role/picked_pole, the nested read dict, p_b, top1_id, menu_b, menu text, menu_index, prefix_tokens_at_read), 4-dp rounding vs full precision, the low_label_mass and top1_not_label flags, and post_degen moving off the choice. Parts are covered elsewhere, as the claim says: verify_kl on every read is (9), ea's removal is (10), and prefix_tokens_at_read is (12)'s window. The post-degeneracy class set (v2/echo/content against f1's frozen-audit deg) falls under (6).
- f1: round, menu_a, pick, picked_cfg, label_mass and p_a rounded to 4 dp, top1_is_label, verify_kl (None unless verified), ea (6 dp), and post_degen when the chosen round was audit-degenerate (f_sessions.py:361-372). menu_b, the menu text and top-1 id are not recorded.
- F0m: ci, n, menu_index, menu (text), menu_a, menu_b, read {pick, p_a, p_b, label_mass, top1_id, top1_is_label, verify_kl} at full float precision, pick, picked_role, picked_pole, prefix_tokens_at_read, low_label_mass (label_mass < .20 on the unrounded value), top1_not_label (scaffold.py:356-363, :398-411). Post-choice degeneracy sits on the free round's audit claim (v2 / echo / content) and in its counter (audit.py:590-592), not on the choice.
- effect: Descriptive. On f1's archive the 4-dp rounding never crosses the .20 threshold (0 of 346 reads within .00005 of .20).
- evidence: Computed from data/f/sessions.jsonl. verify_kl on every read is §2.7 (9); ea's removal is (10); prefix_tokens_at_read reflects (12)'s window. The rest of the field set is beyond.
- refuter: Checked against both codebases; the claim holds.

f1's side is correct. jlens-qwen36/scripts/f_sessions.py:361-367 appends {round, menu_a, pick, picked_cfg, label_mass and p_a rounded to 4 dp, top1_is_label, verify_kl via ch.get (None unless verified), ea rounded to 6 dp}. Lines :368-372 add post_degen only when the chosen round's deg is set. The archive matches: 1,694 reads have exactly those 9 keys and 51 also carry post_degen. menu_b and top-1 id are not stored anywhere. The menu text is not in the per-choice record, though it can be recovered from the recorded transcript.

F0m's side is correct at HEAD (git show 5f7b968). valence_core/m/scaffold.py:356-363 (_read_dict) keeps pick, p_a, p_b, label_mass, top1_id, top1_is_label and verify_kl as plain floats. Lines :398-411 (add_choice) add ci, n, menu_index, menu, menu_a, menu_b, read, pick, picked_role, picked_pole, prefix_tokens_at_read, low_label_mass and top1_not_label. low_label_mass is read["label_mass"] < LOW_LABEL_MASS, which is 0.20 per e2d/runner.py:58, so it is computed on the unrounded value. runner_qwen.py:187 passes LOW_LABEL_MASS. guard.insulated_read (:130) always reads with verify=True, so verify_kl is present on every read. record() (:438-448) round-trips through json, which keeps full float precision.

One anchor is wrong. audit.py:590-592 is the low_label_mass/top1_not_label counter loop. The post_choice_degeneracy counter is at audit.py:584-585. The round's audit claim itself is stored by add_round (scaffold.py, the ra.as_dict() field). The substance is right; only the line numbers are off.

The effect claim reproduces from data/f/sessions.jsonl. There are 346 CORR reads and none has a recorded label_mass within .00005 of .20. The same holds over all 1,745 f reads.

Omission, not a refutation. f1 used the rounded label_mass in a binding monitor. checkpoint_eval at f_sessions.py:426-433 counts c["label_mass"] < 0.2 from the 4-dp record, pooled over all arms, and pauses when an exact binomial against p0 .20 gives p < .05 ("pooled MASS"). In F0m, low_label_mass is only a descriptive counter (audit.py:590-592; stages.py:1720; readrule.py:622, :642); no bar reads it. The rounding never matters, because 0 of 1,745 reads sit near the threshold. The demotion from a pause monitor to a descriptive counter is itself an F0m-vs-f1 monitor difference beyond the fourteen, and it belongs in its own item. The 'Descriptive' effect is correct for the record-field difference this claim describes.

#### D77. Storage, checkpoint and resume identity
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: One JSON line per session appended with open('a'), no fsync (f_sessions.py:386-387). --resume skips (arm, session) pairs already in the file, with no identity check (:610-614). The guard's `evaluated` set is rebuilt per invocation (:615).
- F0m: One checkpoint JSON per stage under data/m/ckpt/, written atomically (temp file, fsync of file and directory, rename; resume.py:179-205), holding only G-VER-verified records (:908-956). The identity is compared exactly in both directions and any change is refused; resume is skip-only (IDENTITY_KEYS at :93-96: lock, schedule, proposal, package, pool and renders hashes; path; stop_cap; hour_cap; n; key templates; audit and ban shas; backend id; pod id; :803-862). Also: end_pending / re-finish-only, ended stages refused, adapter provenance recorded per invocation.
- effect: None on the DVs.
- evidence: §2.7's resume-identity sentence specifies m's side, but it is not one of the fourteen disclosure items.
- refuter: I read both sides at HEAD 5f7b968 and the claim holds.

f1's side:
- f_sessions.py:386-387 has `with open(out_path, "a") as f: f.write(json.dumps(row) + "\n")`, called inside run_session, with no flush and no fsync.
- Resume is at :611-614: `done = {(arm, session) ...}` is read from the file, and nothing compares n, arms, pools or seeds against what was recorded.
- `evaluated = set()` is at :615, so the guard keys checked by checkpoint_eval (:401-403) are rebuilt on every invocation.
- data/f/sessions.jsonl has 344 rows, one line per session and no duplicate (arm, session) pairs, which matches this format.
- f1 also does not refuse an existing file when --resume is absent. It simply appends. This adds to the difference and contradicts nothing.

F0m's side (resume.py at HEAD):
- IDENTITY_KEYS is at :93-96. It also holds unit, stage and template_set.
- atomic_write_json is at :179-203: write a .tmp file, fsync it, os.replace, then fsync the directory via _fsync_dir.
- record_session (:908-956) refuses any record whose `verified` is not exactly True. It also refuses ended stages, a pending end and duplicates (skip-only).
- load_or_init (:803-862) refuses an ended checkpoint, refuses an existing one without --resume ("CHECKPOINT EXISTS"), and refuses any difference found by _identity_diff (:471-480), which compares every key of both sides as canonical JSON.
- append_provenance (:247-264) adds one entry per invocation.
- The default checkpoint is <out_root>/ckpt/{unit}_{stage}.json with out_root defaulting to REPO/data/m (stages.py out_paths). checkpoint_path forces every checkpoint under ckpt/.

Two small imprecisions, neither a refutation:
- "Any change is refused" is slightly too strong. On a gate stage where only the pod changed, a different backend_identifier is tolerated: the old checkpoint is set aside and the stage restarts, rather than being refused. A pending-end re-finish also tolerates a different backend_identifier and pod_id (:821-829).
- "One checkpoint per stage" is the default. An operator may name a restart path under ckpt/ (for example Q-F0_campaign.podB.json).

Classification: beyond. None of §2.7's fourteen items (m:267) covers storage, atomic writes, the G-VER write gate or resume identity. Item (9) is about verifying the choice read, (13) is about interleaving and the per-arm stop, and (11)/(14) are about the round path and the generation window. §2.7's own resume-identity sentence specifies m's design but is not a disclosure item against f1.

Effect: the claimed "none on the DVs" is right. These are differences in how sessions are recorded and resumed, and they leave the generated sessions unchanged.

#### D78. Stdout: picks, tags and indices printed (f1) vs blinded session lines (F0m)
- finder's classification: beyond; refuter: refuted=False, classification beyond (not among §2.7's fourteen; already stated by the proposal outside that list at §4 Blinding, m:318, under §2.6's printed form, m:263)
- f1: Per session: `[j/N] CORR s{s}: first=P|Q|X EXCL {exclude_reason}  {secs}s`, i.e. the first pick, the full reason with the copied tag and the free-round index, and seconds (f_sessions.py:624-628). Guard and pooled-bar lines with 4-dp floats (:406-430, :665-666). The smoke prints 'Q-caused exclusions' by arm (:660-662).
- F0m: One line per session: `{stage} {template} s={s} valid|excluded:{class}@{phase}`. A contrast free-round exclusion prints as `excluded@free`. No pick, tag, index or seconds (readrule.py:443-506; stages.py:1355, :1946). Bar messages show the exact Fraction rounded half-up to 4 places with `<=` / `>`; hair-trigger messages carry no count (bars.py:214-224, :436-462). Also PROVENANCE, gate and STOP/PAUSE/PASS lines.
- effect: None on the DVs; blinding only.
- evidence: §4 Blinding (m:318) notes that f1 printed picks. Not among §2.7's fourteen.
- refuter: I checked both sides; the difference is real and can be seen on stdout.

**f1 side** (jlens-qwen36/scripts/f_sessions.py)
- :624-628 prints one line per session: `  [{j+1}/{len(plan)}] {arm} s{s}: first=P|Q|X{ EXCL reason}  {secs}s`. That gives the first pick, for sham sessions as well as contrast ones.
- The reason is built at :334/:336/:368 as `audit:{deg}@forced{ri}`, `lexical:{hit}@forced{ri}` or `lexical:{hit}@free{ci}`. `lexical_hit` (:119-124) returns the matched tag, so a lexical reason carries the copied tag and the round index.
- Guard lines at :406/:410 and the pooled line at :427-429 use `:.4f` floats. They are printed at :665-666 and :673-674 (not in smoke mode).
- The smoke prints `Q-caused exclusions` by arm at :660-662.

**F0m side** (at HEAD 5f7b968)
- `readrule.session_line` (:486-504) prints `{stage} {template} s={s} valid|excluded:{printed_reason}`, enforced by the regex `_LINE_RX` (:98-100).
- `printed_reason` (:445-483) returns `{class}@{phase}`. For a contrast free-round exclusion it returns `CONTRAST_FREE = "excluded@free"` (:89, :480), with no tag, index or seconds.
- The line is printed at stages.py:1355, :1544 and :1946.
- `bars._dec` (:214-222) rounds the exact Fraction half-up to 4 places. `_message` (:436-462) prints `<=` or `>` and omits the count for `_ONE_CLAIM` kinds.
- The stage report, which holds the sham first-pick shares, goes to a JSON file, not stdout (stages.py:1410-1445). Stdout gets only the end lines, the stage line and the file paths.

**Small imprecisions (none changes the conclusion)**
- In F0m the whole status token is `excluded:excluded@free`, not `excluded@free`.
- F0m's line names the stage and the template (A0/A0s) where f1 names the arm. F0m also drops f1's `[j/N]` counter.
- f1 printed picks for sham sessions too.

**Classification:** none of §2.7's fourteen items (m:267) covers stdout or printed form, so "beyond" is correct. The G-PORT entry should still say that the proposal already discloses this at §4 m:318 ("never a pick (f1 printed picks, f_sessions.py:624–627; b3 did not)"), so the port did not newly find it.

**Effect:** none on A0's comparison with f1's primary or any secondary. The change concerns blinding and reporting only.

#### D79. Pre-VERDICTS blinding of reads and reports, and the analysis order
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: No blinding. Picks are printed, every transcript is read in full (rule 25), and the per-property exclusion table is reported. The analysis runs inside the runner (--analyze) and writes data/f/screen_analysis.json (f_sessions.py:437-494).
- F0m: No pick-bearing artifact is read before VERDICTS, with four exceptions (m:318). Contrast transcripts are read with their free rounds removed; sham transcripts are redacted (readrule.py:325-440; m:271). Stage reports give contrast forced-round counts only and withhold free-round events; sham first-pick shares are reported, also per pair (readrule.py:565-646). Contrast seconds are withheld (stages.py:1156-1162). The per-property exclusion table is VERDICTS-only; looks report pooled pre-pick counts. VERDICTS come from a separate pre-committed analyzer (m:278; not built at HEAD), before the seat's full read.
- effect: None on the DVs; changes when humans see picks. (m-internal note, not an f1 difference: at HEAD _contrast_block reports contrast forced rounds by claim class at every gate stage, G-TIME included; ruling (h) asks for counts only at G-TIME.)
- evidence: m:271, m:318. This is a declared rule-25 departure for the pre-VERDICTS window.
- refuter: Not refuted. I checked both sides at HEAD 5f7b968 (from git show) and in f1's code and record.

f1 side holds. f1 has no blinding. f_sessions.py:624-627 prints each session's first pick and its full exclude_reason, tag and free-round position included; the committed results/raw/2026-08-10_f_run.txt shows 344 lines such as "first=P EXCL lexical:prism@free4". analyze() sits inside the runner (f_sessions.py:437-494, dispatched at :543-545) and writes screen_analysis.json at :492.

F0m side holds. m:318 gives the four exceptions and the analyzer-before-the-reads order. m:271 gives the read rule and the declared rule-25 departure. In readrule.py, strip_contrast (:325-356) and redact_sham (:368-440) build the stripped and redacted reads. _contrast_block (:565-584) reports forced-round material only, with free_rounds withheld. _sham_block (:587-646) reports first-pick shares, pooled and per pair. stages.py:1156-1162 withholds contrast seconds. m_analyze.py is not in the HEAD tree.

The m-internal note is also correct. At HEAD, _contrast_block reports forced-round claims by class (_round_counts :522-540) and excluded_at_forced keyed class@forced, at every gate stage, G-TIME included. Ruling (h) asks for counts only at G-TIME.

Imprecisions (none overturns the claim):
(a) "Every transcript is read in full (rule 25)" overstates f1's screen. Rule 25 covers smokes and pilots. PROPOSAL-f:64 mandates full-transcript reads. The record shows "All 12 transcripts read" for f1's smoke (archive/RESULTS-cycles3-4.md:131), but the screen verdict entry (:65-94) records no full read of all 344 sessions.
(b) The per-property exclusion table was also a verdict-time output in f1: analyze :446, and the verdict entry's "Per-property exclusion table (required)". So that sub-point is not a timing difference. The real look-time differences are two. First, f1's per-session stdout names the tag and free position, where F0m prints class@phase, or excluded@free for a contrast session (readrule.py:486-505). Second, f1's looks print per-arm guard counts over all exclusions (f_sessions.py:391-410), where F0m reports pooled pre-pick counts.
(c) "Contrast forced-round counts only" leaves out one item at the qualification stage. That report also carries contrast first-read flags (low label mass, top-1-not-a-label; stages.py:1361-1369, :1421-1422). They are pick-free.

Classification: beyond. None of §2.7's fourteen (m:267) concerns blinding, pick printing, redacted reads or analysis order. Item (13) is the interleave and per-arm stop, and item (10) is the lens read. The difference is disclosed elsewhere in the proposal: m:318 names "f1 printed picks, f_sessions.py:624–627", and m:271 declares the rule-25 departure. It is not one of the fourteen.

Effect: none on the DVs or on A0's comparison with f1's primary. It is descriptive, a matter of when humans see picks.

#### D80. Counters and the per-property exclusion table
- finder's classification: beyond; refuter: refuted=False, classification beyond (none of §2.7's fourteen covers counter keys or the exclusion tabulation; item (6) covers the audit patterns and claiming order, not how claims are tabulated). It is not a surprise the port turned up, though: the table's form and the 7-vs-1 reference are declared at m:314, and the change from whole-session to pre-pick unit is declared for the guard at m:316. What m:314 does not state anywhere is that the 7-vs-1 reference is a whole-session count keyed by the last round's cfg.
- f1: Exclusions are tabulated by (arm, cfg of the last round) over whole-session exclusions (f_sessions.py:441-446): CORR P 7 vs Q 1. Termination attempts are tabulated by (arm, cfg, round position) over all sessions (:448-453). post_degen is recorded per choice.
- F0m: Declared Qwen counters: cap_hit, audit_degenerate (v2, keyed by category), harness_echo, content_exclusion, content_advisory, lexical, post_choice_degeneracy (free v2 / echo / content claims), low_label_mass, top1_not_label, termination, pre_pick_exclusion. They are keyed (template, phase[, category]), never by round index, item or property (audit.py:91-95, :547-603). The VERDICTS per-property table is arm × property: rounds generated, rounds excluded by class, sessions excluded pre-pick (m:314).
- effect: Descriptive. f1's 7-vs-1 reference counts whole-session exclusions, including the two post-pick free4 exclusions on P. Counted as m's pre-pick sessions on f1's archive it becomes P 5 (s27, s36, s49, s55, s60) vs Q 1 (s53). Termination by round position becomes derivable from records only.
- evidence: Computed from data/f/sessions.jsonl exclusion reasons. m:314 cites archive:91-93 as the reference.
- refuter: The facts check out on both sides.

f1's side:
- f_sessions.py:441-446 builds Counter[(arm, rounds[-1].cfg)] over every excluded session.
- :448-453 builds Counter[(arm, cfg, pos)] for termination over all rows, excluded ones included.
- post_degen is set on choices_log[-1] at :372, and the archive has it on 51 of 1,745 choices.
- Rerunning that tabulation on data/f/sessions.jsonl gives ('CORR','P') 7 and ('CORR','Q') 1, which matches archive/RESULTS-cycles3-4.md:91-93.

The pre-pick recount holds:
- The CORR P exclusions are s4 and s25 (lexical@free4, post-pick) plus s27, s36, s49, s55 and s60 (audit:frame@forced2/3).
- The one Q exclusion is s53 (audit:frame:[round@forced1).
- So pre-pick sessions come to P 5 vs Q 1, as claimed.

F0m's side at HEAD 5f7b968:
- audit.py:91-93 declares the eleven Qwen counters exactly as listed.
- tally() at :547-597 keys them by template (A0/A0s) and phase, never by tag, item, round index or property; the PIN at :551-553 says so.
- termination is noted as (tpl, ph) with no position.
- pre_pick_exclusion is counted only when the exclusion's phase is "forced".
- m:314 declares the per-property table as arm x property, with three columns: rounds generated, rounds excluded by class, and sessions excluded pre-pick.
- No per-property analyzer exists in the package at HEAD.

Precision notes (none is a refutation):
(1) The key description is loose. post_choice_degeneracy is keyed (template, claim). low_label_mass, top1_not_label and pre_pick_exclusion are keyed by template alone. Content counters carry the content class, not a v2 category.
(2) The effect is incomplete. m's "rounds excluded by class" column, applied to f1's archive, would still give P 7 vs Q 1:
   - P: 5 forced audit-frame rounds plus 2 free lexical rounds. In m a free-round lexical claim still excludes at run scope (audit.py RoundAudit.excludes).
   - Q: 1 forced audit-frame round.
   So the reference can still be recovered from that column, and only the pre-pick column moves to 5 vs 1. The class split also crosses §2.7 (6)'s audit change.
(3) "Termination by round position only from records" ignores m:312 secondary (e), "termination attempts per round", which the VERDICTS analyzer, not yet built, may report by round.

The effect is correctly graded as descriptive: rule-23 counters and the per-property table decide nothing.

#### D81. Firing operator for every bar: P <= α exact vs p < .05 in floats
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: The guard and pooled bars pause on p < .05 (f_sessions.py:412-415, :431-433). Smoke: lexical p < .05 (:504); audit and cap as ratios > .20 and > .10 (:507-510). Tails are computed in lgamma floats (:144-151).
- F0m: Every binomial and Fisher bar fires iff its exact one-sided P <= α, in rationals; float p0 and α are refused (bars.py:90-161, :198-212).
- effect: Descriptive. The two rules differ only at exact ties: n = 1, k = 1, p0 .05 gives P = .05, which fires in m and is silent under f1's <.
- evidence: m:271 ('A bar fires iff its exact one-sided P <= α'); maps/stats.md §4.
- refuter: I checked the claim against both codebases and it holds. The cited lines are right, and the one effect sentence is too narrow but not wrong.

f1's side (jlens-qwen36/scripts/f_sessions.py):
- `binom_p_ge` at :144-151 sums exp(lgamma ...) terms in floats.
- The guard pauses on `p_abs < 0.05` (:412-413) and `p_rel < 0.05` (:414-415).
- The pooled LEXICAL/CAP/MASS bars pause on `p < 0.05` (:431-433).
- The smoke lexical bar uses `p < 0.05` (:504). The smoke audit and cap bars are ratio tests, `> 0.20` and `> 0.10` (:507, :509).

F0m's side (git show 5f7b968:valence_core/m/bars.py):
- `q()` at :90-104 refuses float p0/alpha, and `_prob` enforces it.
- `binom_sf` (:135-148) and `fires` (:158-161) are exact over Fractions and fire on `<=`. So do `fisher_sf` and `fisher_fires` (:198-211).
- `Bar.evaluate` uses `p <= self.alphaq` for both the binomial (:428-429) and the Fisher (:425-426) kinds. stages.py routes every bar through `Bar.evaluate`.
- m:271 says it verbatim: "A bar fires iff its exact one-sided P ≤ α".

I ran the tie case. f1's `binom_p_ge(1,1,0.05)` returns 0.05000000000000001, so f1 is silent there, under `<` or even `<=`. m's exact P = 1/20 <= 1/20 fires, so the stated tie behaves as claimed.

I also scanned n < 200 at p0 ∈ {.05, .02, .10, .20}. Float `<` and exact `<=` disagree on a binomial at exactly one cell: (n 1, k 1, p0 .05).

The narrowness: "the two rules differ only at exact ties: n = 1, k = 1, p0 .05" names only the binomial tie. Exact Fisher ties at P = 1/20 also occur and are realistic: (a, n1, c, n2) = (1,1,0,19), (2,4,0,12), (2,6,0,19) and others (maps/stats.md §5). f1's guard computes them as an integer ratio, gets exactly 0.05 and is silent under `<`. m's guard fires on them. The entry should say ties under the binomial and Fisher bars, not the binomial example alone.

The "Descriptive" effect is right. These bars only pause or stop stages and enter no DV, so A0's comparison with f1's primary or a secondary is untouched.

Classification: beyond. None of §2.7's fourteen (m:267) covers a bar-firing operator or the arithmetic behind it. Item (6) is the audit classes. Item (13) is the interleave and per-arm stop at floor, not a pause bar's comparison rule. The convention is stated in the proposal, but only in §3 (m:271), outside §2.7's list.

#### D82. Pre-campaign stages: f1's smoke vs m's G-TIME / G-ID / G-F0m-Qwen
- finder's classification: beyond; refuter: refuted=False, classification beyond (partial overlaps only: §2.7 (11) for G-ID's cached-path licence, (7) for the gate keys, (9) for the smoke's verify_every = 1 against m's verify on every read; (13) covers the campaign's interleave and per-arm stop, not anything before the campaign)
- f1: One smoke block at offset indices s 1100/1104 per arm (12 sessions), verify_every = 1. Smoke bars on unprovoked sham + P-config domains: lexical binomial at p0 .05 per session; audit > 20% from 6 sessions; cap > 10% from 10 rounds. Pause on fire (f_sessions.py:497-511, :591-595, :629-662). Then the N declaration.
- F0m: G-TIME-F0 (one A0 and one A0s, uncached), G-ID-F0m (A0s pairs), G-F0m-Qwen (16 A0s + 8 A0), all excluded from the campaign. Hair triggers run on every session. round_degeneracy (v2 / echo rounds) is evaluated once at stage end on sham-template sessions only (critical 3 at n 10, 14 at n 160), with contrast sessions reported beside (bars.py:568-591, :853-904; m:271, m:280-283). The qualification valid rate r feeds the launch rule; sham first-pick shares per pair are reported.
- effect: None on the DVs, since gate sessions are excluded. The stop rules before the campaign differ.
- evidence: G-ID's round-path licence is §2.7 (11) and the gate keys are (7). The stage set, its bars and their domains are beyond.
- refuter: The difference is real. I checked both sides.

f1's side:
- f_sessions.py:591-595 builds the smoke plan as the five CONTRASTS (:87) plus sham at s = 1100 and 1104, which is 12 sessions, with verify_every = 1.
- smoke_bar_check (:497-511) runs after every smoke session (:629-662). It has three bars: a lexical exact binomial at p0 .05 with strict p < .05; audit above 20% once n is at least 6; cap-hits above 10% once rounds reach 10. A fire prints PAUSE and returns.
- PROPOSAL-f:177 gives the order: smoke, then the N declaration, then the screen.

F0m's side, at HEAD 5f7b968:
- Hair triggers run on every session (bars.py:513-528).
- round_degeneracy is a stage-end binomial on sham-template sessions only. Its numerator is v2 or echo rounds. Critical 3 at G-TIME-F0 and 14 at G-F0m-Qwen (bars.py:568-591; stage_end_eval at :853-904).
- Contrast sessions are reported beside, not bound (m:271, m:280-283).
- G-ID's divergence is a hair-trigger-style FAIL that sends Q-F0 uncached.
- There is no lexical bar and no cap bar (bars.py:33-34).
- r feeds the launch rule (m:283).

None of §2.7's fourteen lists the pre-campaign stage set, its bars or their domains, so "beyond" stands. The claim itself correctly names (11) and (7) as covering parts. "None on the DVs" is right, since both sides' gate or smoke sessions are kept out of the analysed data. A small qualification: r sets the launch counts, so the stage bears on sizing, but only descriptively.

The claim has three imprecisions on f1's side. None of them refutes it:
1. f1 actually ran two smoke blocks, not one. data/f/sessions_smoke.jsonl has 24 rows: s1000/1004 under pools v1, then a re-smoke at s1100/1104 under the re-scoped bars of adjudications eb0f33b and 27446d3. "One smoke block at 1100/1104" describes the code, not the record.
2. The lexical bar is not on the unprovoked sham + P domain. It counts every smoke session from s1100 on, all arms, as the comment says: "lexical stays blind" (:630-638). The audit bar's numerator is unprovoked-only, but its denominator n_done counts all sessions.
3. f1's bars are checked after every session with strict p < .05. m's are evaluated once at stage end on the realised n, firing at P ≤ α.

#### D83. Insulation assertion: forbidden-module set
- finder's classification: beyond; refuter: refuted=False, classification beyond
- f1: Asserts jlens_qwen.fingerprint, forced_choice, interventions, conditioning, e2a and eval_awareness absent, at startup and after model load (f_sessions.py:51-53, :527-528, :586-587).
- F0m: Asserts only valence_core.e2b.statepresent absent, at startup and before every session and read (guard.py:77, :119-138). The QwenMLXAdapter imports jlens_qwen.forced_choice and jlens_qwen.conditioning at construction (valence_core/adapters/qwen_mlx.py:74-75). Insulation rests on injections=() plus the statepresent assertion.
- effect: None on the DVs. A verification difference to disclose.
- evidence: maps/e2a.md F11 flagged it as not among §2.7's fourteen. Re-checked at HEAD.
- refuter: I checked this against both codebases and the claim holds.

f1's side: f_sessions.py:51-53 defines FORBIDDEN_MODULES as six modules: jlens_qwen.fingerprint, forced_choice, interventions, conditioning, e2a and eval_awareness. It asserts each one absent from sys.modules at the start of main() (:527-528) and again after the model loads (:586-587), then prints "no intervention modules loaded". f1 gets its stream session from jlens_qwen.model (:46).

F0m's side, at HEAD 5f7b968: guard.py:77 sets FORBIDDEN_MODULES = ("valence_core.e2b.statepresent",) and nothing else. assert_insulated (:119-121) is called at startup (runner_qwen.py:114, qwen_startup), at the start of every session (runner_qwen.py:129) and before every read (insulated_read, guard.py:127). The QwenMLXAdapter loads jlens_qwen.forced_choice and jlens_qwen.conditioning when it is constructed (qwen_mlx.py:74-75). The cached path F0m uses is conditioning.SteeredStreamSession, and conditioning imports jlens_qwen.model (conditioning.py:45). So two of f1's six forbidden modules are loaded in every F0m Qwen process, and f1's own check would halt it. Insulation in F0m rests on injections=() (runner_qwen.py:159, :190), the AST call-site guard, and the single statepresent check. That is what m:48 specifies, so F0m follows the proposal, but it still differs from f1.

It can be observed: f1 asserts something F0m does not, and that assertion would fail on F0m's apparatus.

Small citation fix: the per-session assertion is at runner_qwen.py:129 and the startup one at :114, not inside the guard.py:119-138 range. guard.py covers only the definition and the per-read call. This does not change the claim.

Classification: beyond the fourteen. None of §2.7's fourteen items is about the insulation or forbidden-module assertion:
- (10) covers dropping the per-choice lens read.
- (11) covers the round path, cached iff G-ID passes.
- (14) covers the generation window and chunking.

§2.7's preamble says Qwen rounds run cached through SteeredStreamSession with injections=() (qwen_mlx.py:307-313). That quietly discloses that conditioning's class is used. It does not disclose that this module, or forced_choice, is on f1's forbidden list, or that the assertion set was narrowed from six jlens modules to one valence_core module. The preamble and (11) are related context, not cover.

Effect: none on the dependent variables or on A0's comparison with f1's primary or secondaries. It is a verification difference to disclose.

#### D84. Pre-declared secondaries with decidable-n floors (f1 had none)
- finder's classification: beyond; refuter: refuted=False, classification beyond (for (a), (b), (d) and the 20-event floor rule). Item (12) covers only the window crossing in (a) at positions 5-6, and (13) covers only the stop rule. Neither covers the secondaries existing at all. One component is wrong, though: (e) is not new as a pre-registered analysis, because f1 pre-registered a termination counter by round position.
- f1: No secondary was pre-registered (PROPOSAL-f §3). Descriptives were produced after the screen (jlens-qwen36/scripts/f_postscreen_descriptive.py → data/f/postscreen_descriptive.json, marked post_hoc).
- F0m: Pre-declared: (a) clean-label share by position 1-6 on 'valid through position p'; (b) lose-shift, contrast arms only; (d) per-pair first-pick shares and habit identity; (e) termination per round. Floor 20 events, count-only below it (m:312).
- effect: Descriptive. Secondary (a) has no pre-registered f1 counterpart on a position-p domain, and 'valid through p' differs from f1's whole-session validity before a free exclusion. The window change at positions 5-6 is (12).
- evidence: m:312; postscreen JSON keys: post_hoc, features, preamble_markers, fdbk_line, corr_anomaly.
- refuter: The core of the claim holds, but it has one factual error that must be fixed before it goes into the G-PORT entry.

What I checked and found correct:
- f1 pre-registered no secondaries. PROPOSAL-f section 3 (PROPOSAL-f-natural-reinforcer-screen.md:99-119) and the f1 PRE-REGISTRATION entry (archive/RESULTS-cycles3-4.md:366-418) lock only the primary (the first free choice), the three conjuncts, N and floors, and the monitors.
- f1's feature analysis is post-hoc. jlens-qwen36/scripts/f_postscreen_descriptive.py:1-6 says "POST-HOC, LABELED AS SUCH". Its JSON's top-level keys are exactly post_hoc, features, preamble_markers, fdbk_line and corr_anomaly (:90-91, :138, :155). Its domain is whole-session-valid sessions only (:63-64), and f_sessions.py analyze() (:437-485) reads only first_free_pick_P.
- m:312 declares (a) clean-label share by position 1-6, (b) lose-shift on contrast arms only, (d) per-pair first-pick shares plus habit.py's identity, and (e) termination per round. It sets a 20-event floor, with count-only below it. m:308 sets the domain as "valid through position p", with whole-session validity reported beside.
- The m package at HEAD 5f7b968 has no code for the secondaries yet (no grep hits for secondar, lose-shift or habit analysis). The difference therefore lives at the level of the pre-registration and analysis plan. That still counts under "how sessions are analysed".
- Effect: descriptive, as the claim says.

The error: "f1 had none" is false for (e), and the f1 side overstates "descriptives were produced after the screen".
- On f1's own record, the f1 smoke2 adjudication added a termination-attempt counter: "DECLARED BEFORE RUN DATA", tabulated "per arm x config x round-position over ALL sessions INCLUDING audit-excluded ones", and "REQUIRED in the verdict entry" (archive/RESULTS-cycles3-4.md:207-239, titled "pre-registered termination-attempt counter").
- f1 computes it in f_sessions.py:319-333 and :447-452, and reports it in the verdict as a "pre-declared counter" (:97-104).
- F0m ports the same counter: the same sha-pinned data/configs/f_termination_patterns.json (m/scaffold.py:65, :295-305) and the same count (m/audit.py:588-589), and m:314 lists termination among the rule-23 counters.
- f1 also had other required pre-declared descriptive reports: the per-property exclusion table (archive :393-394; f_sessions.py:441-446), the FDBK composition, and the CORR accuracy covariate.

So the residual difference for (e) is narrower than claimed. m adds a post-exclusion "valid through" version with a 20-round floor beside the all-sessions counter, against f1's floorless all-sessions table broken down by round position.

Corrected statement: f1 pre-registered no secondary choice analyses (no positional shares, lose-shift or per-pair shares) and no decidable-n floors. Its only pre-declared descriptives were the termination table, the per-property exclusion table, the FDBK composition and the CORR covariate, all floorless. F0m pre-declares (a), (b) and (d) with a 20-event floor on post-exclusion "valid through p" domains, and adds a floored post-exclusion form of f1's termination counter as (e).

#### D85. Verify cadence of the choice read (recorded verify_kl on every read)
- finder's classification: §2.7 (9); refuter: refuted=False, classification §2.7 (9). It is covered, not beyond the fourteen: m:267 item (9) reads "the verify cadence — `choice_read(verify=True)` on every read against f1's `verify_every`".
- f1: verify at (s*6 + ci) % 4 == 0 (f_sessions.py:353, :608). First picks verified 30 of 58; 88 of 346 reads verified.
- F0m: insulated_read always runs choice_read(verify=True) and requires KL exactly 0.0 (guard.py:124-138). verify_kl is in every recorded read (scaffold.py:361-362).
- effect: None on the DV (all f1 verifies returned 0.0).
- evidence: Computed: 30 first reads verified.
- refuter: The claim is factually correct, so it is not refuted. f1 side: f_sessions.py:353 is `verify = ((s * N_FREE + ci) % verify_every == 0)` (N_FREE = 6). In the campaign branch :608 sets verify_every = 4; :595 sets 1, but only for the smoke plan. f1's choice_read (:205-214) also halts when KL != 0.0. F0m side, at HEAD 5f7b968: guard.py:124-138 insulated_read always calls choice_read(..., verify=True) (:130) and halts unless KL is a float exactly equal to 0.0 (:133-137). runner_qwen.py:181 makes every free read through insulated_read. scaffold.py:356-362 _read_dict copies verify_kl, and add_choice (:403) records it, so every F0m read carries a verify_kl. The counts reproduce in a recount of data/f/sessions.jsonl: f1 CORR has 64 sessions, 58 with choices, 30 of those 58 first picks verified, 88 of 346 reads verified, and the only KL value is 0.0. Effect: none on the DV. Both apparatuses halt on any nonzero KL, so a verified read changes no pick; the only difference is how often the check runs and is recorded. One small point the claim leaves out: f1 also halted on a nonzero KL, so this is a difference in cadence only, not in strictness. The extra float/NaN check in F0m catches NaN, which f1's `kl != 0.0` also catches, so it adds no observable difference. scaffold.py:71/:499 (F1_VERIFY_EVERY) reproduces f1's cadence only in the f1 replay check and does not touch F0m sessions.

#### D86. Per-choice lens read (ea) recorded by f1 only
- finder's classification: §2.7 (10); refuter: refuted=False, classification §2.7 (10)
- f1: ea_mass after every choice_read, recorded as `ea` to 6 dp (f_sessions.py:219-231, :355, :367).
- F0m: No lens read; nothing in the choice record (scaffold.py:398-411).
- effect: None.
- evidence: —
- refuter: The claim holds and every cited line checks out. On f1's side, `ea_mass` is defined at f_sessions.py:219-231. It runs one uncached forward over the workspace layers, transports each layer's state through the Jacobian lens, and averages the softmax mass on the eval-awareness marker tokens. It is called at :355 straight after `choice_read` on the same `transcript + menu`. The result is stored as `"ea": round(eam, 6)` at :367. The lens and marker indices are loaded at :571-585 and passed into `run_session`. In the archived data/f/sessions.jsonl, all 1,745 choice records across 344 sessions carry the `ea` key.

On F0m's side, nothing at HEAD 5f7b968 reads a lens. A grep for lens, ea_mass, marker and workspace in the m modules (scaffold, corr, banner, keys, runner_qwen, audit, verify, readrule, stages, bars, schedule, resume, guard) and in scripts/m_sessions.py finds only unrelated hits: '/workspace' paths and the guard's process-name markers. `add_choice` at scaffold.py:398-411 records ci, n, menu_index, menu, menu_a/b, the read (from `_read_dict` at :356-363: pick, p_a, p_b, label_mass, top1_id, top1_is_label, verify_kl), pick, picked_role/pole, prefix_tokens_at_read, low_label_mass and top1_not_label. None of these is a lens field.

On classification, the difference is covered and is not beyond the fourteen. §2.7 item (10) at m:267 reads "no per-choice lens read (f1's `ea_mass`, :219, :355; m reads nothing but the vanilla choice read)". The claim adds only the :367 record field and the 6-dp rounding, which are details of the same item.

On effect, "None" is right for the picks. The f1 lens forward draws no rng, does not touch the transcript, and comes after the pick is already decided. So what the model sees and how it chooses are the same. The only loss is a descriptive monitor field. I found no use of `ea` in f1's verdict path: no hit in f_postscreen_descriptive.py, and nothing in RESULTS.md or the archive ties it to f1's criteria.

#### D87. Read context window (prefix_tokens_at_read recorded)
- finder's classification: §2.7 (12); refuter: refuted=False, classification Mostly covered by §2.7 (12): the difference between the 512-token tail and the 8192 window is exactly what (12) discloses. One sub-part goes beyond the fourteen, though: recording `prefix_tokens_at_read` is a new per-choice field that f1 never had. (12) and the other thirteen items do not name it. Its effect is descriptive only.
- f1: choice_read encodes through jlens model.encode with a 512-token tail (f_sessions.py:195).
- F0m: 8192 window asserted at every read (readout.py:101-106; runner_qwen.py:91-100). prefix_tokens_at_read is recorded per choice (scaffold.py:400-407).
- effect: As (12) states: secondary (a) at positions 5-6.
- evidence: —
- refuter: Both sides of the claim check out, and every cited line says what the claim says it does.

**f1's side:** `jlens-qwen36/scripts/f_sessions.py:195` reads `ids = model.encode(text)` and passes no `max_length`. `model` comes from `jlens_qwen.model.load` (`f_sessions.py:45`, `:569`). In `jlens_qwen/model.py:74-78`, `MLXLensModel.encode` defaults `max_length=512` and keeps the tail (`ids[-max_length:]`). The read text is `transcript + menu` (`f_sessions.py:354`), so f1's reads were silently tail-clipped at 512 tokens.

**F0m's side at HEAD 5f7b968:**
- `valence_core/readout.py:101-106` encodes and then calls `adapter.assert_choice_window(len(ids))` on every read.
- `adapters/base.py:334-348` raises `SystemExit` ("WINDOW INCIDENT") when a read is longer than the window, so an over-length read halts instead of clipping.
- `m/guard.py:72` and `:124-131` route m's only read, `insulated_read`, through that `choice_read`.
- `m/runner_qwen.py:65` (`CHOICE_WINDOW = 8192`) and `:91-100` (`assert_qwen_adapter`, run at startup via `:115`) require the adapter's `choice_window` to equal 8192 and forbid any `legacy_truncate` or `max_length`.
- `m/scaffold.py:398-407` records `prefix_tokens_at_read` per choice. Its value is `len(adapter.encode(read_prefix))` from the full, untruncated encode (`runner_qwen.py:183`, `:187`). G-VER re-derives it (`runner_qwen.py:364-379`), and the blinded forms strip it as free-only (`readrule.py:106`).

**Classification:**
- **The window itself:** (12) covers it word for word ("m reads the whole session at 8192; f1's reads at free positions 5-6 saw a 512-token encode tail"). The claim's effect ("secondary (a) at positions 5-6; A0 vs primary unaffected") matches what (12) says.
- **The recorded field:** f1's choice record (`f_sessions.py:361-367`: round, menu_a, pick, picked_cfg, label_mass, p_a, top1_is_label, verify_kl, ea) has no prefix-length field. So `prefix_tokens_at_read` is a records difference that none of the fourteen items names. It is descriptive only: f1's prefix lengths can be rebuilt from the archived transcripts by tokenizing them, which is how (12)'s count of 75 of 1,745 was obtained. Nothing in A0's comparisons reads the field.
- **Halt instead of clip on an over-window read:** this is implied by (12) and cannot be reached at Q-F0's session lengths, which are far below 8192, so it has no effect.

**Nit:** the claim cites "readout.py" bare. The file is `valence_core/readout.py`, a core module outside `valence_core/m/`.

#### D88. Interleave and arm stopping
- finder's classification: §2.7 (13); refuter: refuted=False, classification §2.7 (13)
- f1: Six arms sorted by ((i + .5)/n_arm, arm) (f_sessions.py:602-607).
- F0m: Strict rotation, fewest launches first with ties in table order, and an arm leaving at its floor (schedule.py:418-460; stages.py:1909).
- effect: None on the DVs.
- evidence: What the floor counts is the 'Floors' item above (beyond).
- refuter: The claim holds on both sides, and it is covered by item (13), not beyond it.

f1 side, checked: f_sessions.py:87-88 gives five CONTRASTS plus "sham", so six arms. :602-607 builds the entries (arm, i, n) and orders the plan with `sorted(..., key=lambda t: ((t[1] + 0.5) / t[2], t[0]))`, which is fractional progress (i + .5)/n with ties broken by arm name. Each arm runs a fixed n (args.n_contrast / n_arms / n_sham). There is no per-arm floor stop.

F0m side, checked at HEAD 5f7b968: schedule.py:418-464 is `interleave` (its docstring, the PIN at :429-433 stating "the live arm with the fewest launches, ties to table order", and the resume-consistency validation). The rule itself is applied at :476 in `_rotation` (:467-478): `min(live, key=lambda a: (counts[a], arms.index(a)))`, with an arm removed for good once `done(a)` holds. stages.py:1909 passes `done = lambda a: domain[a] >= fl[a]`, so an arm leaves when its domain count reaches its floor. keys.py:22 makes Q-F0 two arms (A0, A0s) in table order.

One citation note, which does not refute the claim: the cited range :418-460 holds the validation and the PIN text, while the selection is implemented at :476, just outside it.

Classification: §2.7 (13) says almost exactly this: "two arms interleaved in strict rotation with per-arm stop at floor, against f1's six-arm interleave (the sham among them) ordered by fractional progress". So COVERED by (13), as the claim says.

Effect "none on the DVs": plausible. Sessions in both apparatuses are keyed per session, not per launch order, so order alone changes no session's output. The per-arm floor stop changes realised n, but the claim rightly defers what the floor counts to its separate "Floors" item.

#### D89. Claim precedence behind exclusions and post-choice degeneracy
- finder's classification: §2.7 (6); refuter: refuted=False, classification §2.7 (6)
- f1: audit (empty → special → frame → junk) then lexical; deg at free → post_degen (f_sessions.py:127-141, :317-318, :368-375).
- F0m: v2 → echo → v4 content → lexical; forced ends on any claim; free ends on lexical only; free v2 / echo / content claims → post_choice_degeneracy (audit.py:421-458, :501-506).
- effect: As (6).
- evidence: —
- refuter: Not refuted. The difference is real, and it is covered by (6), which names "m's echo class and the claiming order" against f1's frozen audit list.

f1's side checks out:
- The audit runs in the order empty, special, frame, junk (f_sessions.py:127-141).
- Lexical is evaluated only on rounds that are not degenerate (:317-318).
- A forced round is excluded on an audit or lexical hit, which breaks the loop (:339-345).
- A degenerate free round is logged as post_degen and does not end the session; a free lexical hit excludes it (:368-375).

F0m's side checks out (HEAD 5f7b968; audit.py and runner_qwen.py are unchanged in the working tree):
- The claim order is v2, then echo, then v4 content, then lexical (audit.py:444-455).
- v2 is session.AuditSpec.check, whose internal order (empty, special, frame, junk; session.py:140-154) matches f1's. AuditV3 runs v2 before content (audit_v3.py:52-57).
- qwen_ends (audit.py:501-506) calls excludes("lenient") (:361): a forced round ends on any claim, a free round only on a lexical claim. The runner applies this at runner_qwen.py:168-175 and :199-205.

The session-end rule itself is f1's, replicated as m:261 declares. What differs is that the new classes (echo, content) and their place in the order are inserted ahead of lexical. So a free round that is content- or echo-claimed but also mentions the own pair counts as post_choice_degeneracy in F0m, where f1 would have excluded it as lexical. That is a consequence of (6)'s claiming order, not something beyond the fourteen.

Precision notes (none of them refutes the claim):
(a) The post_choice_degeneracy mapping is not in the cited ranges 421-458 or 501-506. It sits at audit.py:29-33 (docstring), :554-555 and :584-585 (tally), and runner_qwen.py:199-205.
(b) "Free ends on lexical only" is true for exclusion, but it leaves out the hair trigger. At runner_qwen.py:201-203, a scaffold-string hit in a free round (also a v2 special: claim) stops the session and the stage without excluding it. In f1 the same text would be post_degen and the session would continue. This is a stop-rule difference that none of the fourteen names, and it belongs in its own item.
(c) "Effect: As (6)" is empty, because (6) states no effect. The real effect is as follows. At forced rounds the new classes add pre-pick exclusions, so they change domain composition through (6). At free rounds F0m keeps the session in the domain (m:308), so the order matters only for counters, whole-session validity and secondaries' "valid through position p".
(d) Next to this claim but outside it is a domain difference that §2.7's list does not cover: f1's analyze drops free-excluded sessions (`valid`, f_sessions.py:439; 2 CORR lexical@free in data/f/sessions.jsonl). m keeps them, and the proposal discloses this at m:308 (28/56 of record), not in §2.7.

#### D90. Round path recorded per session
- finder's classification: §2.7 (11); refuter: refuted=False, classification Partly covered, partly beyond. Item (11) covers the round path itself. Recording the path in the session record and in the resume identity is not one of the fourteen. The resume-identity sentence of §2.7 (m:267) declares it, but outside the numbered disclosure list. Effect on the comparison with f1: none, since this is only a record field.
- f1: Always cached (jlens StreamSession); not recorded (f_sessions.py:162-168).
- F0m: `path` field ('cached' / 'uncached') in the record and the identity (scaffold.py:441; resume.py:93-96).
- effect: As (11).
- evidence: —
- refuter: Both sides check out.

**f1's side.** In f_sessions.py, gen_round (lines 162-168) always builds jlens `StreamSession(model)`, so it always runs the cached path. Nothing records which path ran:
- The session-row dict at :377-385 has no path field.
- The 15 top-level keys in the archived data/f/sessions.jsonl contain no 'path'. Those keys are: arm, choices, exclude_cfg, exclude_reason, excluded, first_free_pick_P, n_cap_hits, n_rounds, pair, rounds, session, start_P, swap, tag_P, transcript.
- The per-round keys contain no 'path' either.
- f1's resume identity is only the pair (arm, session), at :610-613.

**F0m's side, at HEAD 5f7b968.**
- valence_core/m/scaffold.py:441 writes `"path": sc.path` into every session record, and scaffold.py:264 sets it in meta.
- resume.py:93-96 lists "path" in IDENTITY_KEYS, and resume.py:451 builds the identity with path.
- resume.py:506-508 also makes path part of a G-ID session's record id, where it must be 'cached' or 'uncached'.

So the difference is real and shows up in the record.

**Classification.** The tag "covered by (11)" is only half right. Item (11) discloses the round path itself: cached iff G-ID passes, where f1 always ran cached. It does not mention recording the path. Two further things are new against f1:
- the per-record `path` field;
- path as part of the resume identity, which also stands against f1's (arm, session)-only resume key.

§2.7's own resume-identity sentence (m:267, "path (cached/uncached)") declares the identity part, but that sentence sits outside the fourteen numbered disclosures. Strictly, then, the recording and identity part goes beyond the fourteen.

**Effect.** "As (11)" overstates it. A record or identity field changes nothing the model sees and no DV. Its effect on A0's comparison with f1 is none, or descriptive at most, because it only documents which path ran. The path effect itself stays under (11).

---

## Part 4 -- Code's own re-run of the model-free scripts behind C1-C3, A1 and the figures above (after the entries' values-check pass 2)

Run by Code from each script's own folder with the jlens venv (`PYTHONDONTWRITEBYTECODE=1`), no model or tokenizer. `runner_vs_f1.py` and `rotation_and_q_clean.py` import the m package from `headtree/`, a `git archive` extract of HEAD 5f7b968 the harness-bytes lens made; the scripts are reproduced verbatim below and their outputs follow.

### `harness-bytes/runner_vs_f1.py`

```python
"""Drive m's real Qwen runner (run_session_qwen) with f1's recorded texts and picks on an
f1-configured scaffold; compare the runner-built transcript with f1's archived one.
Model-free (ScriptedAdapter). Read-only on the repo."""
import json, sys, copy
sys.path.insert(0, "/private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/harness-bytes/headtree")
from valence_core.m import scaffold as S, testing, runner_qwen, corr
from valence_core.m.scaffold import SessionScaffold, f1_cell, SESSION_BANNER
from valence_core.m import keys

pool, _ = S.pool_and_renders()
rows = [r for r in S.load_f1_rows() if r["arm"] == "CORR"]
kit = testing.qwen_kit()

def f1_gens(row):
    # walk the f1 transcript via the f1_config scaffold, return generation texts in order
    sc = S.f1_config(row["session"], pool)
    t = row["transcript"]; pos = len(sc.banner); gens = []
    assert t.startswith(sc.banner)
    nf = min(4, len(row["rounds"]))
    segs = []
    for ri in range(nf):
        segs.append(("seg", sc.forced(ri).seg))
    out = []
    for ri in range(nf):
        seg = segs[ri][1]
        assert t.startswith(seg, pos); pos += len(seg)
        e = t.index("\n", pos); out.append(t[pos:e]); pos = e + 1
    for ci, ch in enumerate(row["choices"]):
        m = sc.menu(ci); assert t.startswith(m.menu, pos); pos += len(m.menu)
        pl = f" {ch['pick']}\n"; assert t.startswith(pl, pos); pos += len(pl)
        spec = sc.chosen(ci, ch["pick"]); assert t.startswith(spec.seg, pos); pos += len(spec.seg)
        e = t.index("\n", pos); out.append(t[pos:e]); pos = e + 1
    assert pos == len(t)
    return out

res = {"identical": 0, "prefix_shorter": 0, "other": 0, "details": []}
for row in rows:
    s = row["session"]
    gens = f1_gens(row)
    rng = keys.stream(f"f|CORR|{s}")
    items = corr.ItemStreams(rng)
    meta = {"substrate": "qwen", "unit": "Q-F0", "stage": "qual", "template": "A0",
            "contrast": True, "path": "uncached", "j": s, "keys": {"arm": f"f|CORR|{s}", "items": f"f|CORR|{s}"}}
    sc = SessionScaffold(banner=SESSION_BANNER, cell=f1_cell(s), s=s, arm_rng=rng, items=items,
                         delivery=corr.Delivery(pool, corr.renders_f1(pool), contrast=True), meta=meta, note_lines=("Note: zq1 xv.", "Note: zq2 xv."))
    a = testing.ScriptedAdapter()
    picks = [c["pick"] for c in row["choices"]]
    # pad picks/texts if m's runner runs longer than f1 (it cannot generate beyond f1's record)
    a.load(gens + ["Seven."] * 10, picks + [sc.P] * 6)
    try:
        rec = runner_qwen.run_session_qwen(a, sc, kit.audit, kit.ban_ids, path_cached=False, term_rx=kit.term_rx)
    except Exception as e:
        res["other"] += 1; res["details"].append((s, "raised", repr(e)[:200])); continue
    t_m, t_f = rec["transcript"], row["transcript"]
    if t_m == t_f:
        res["identical"] += 1
    elif t_f.startswith(t_m):
        res["prefix_shorter"] += 1
        res["details"].append((s, "m ends earlier", len(rec["rounds"]), len(row["rounds"]),
                               rec["exclusion"], row["exclude_reason"], [x["audit"]["claim"] for x in rec["rounds"]]))
    else:
        # first differing offset
        k = next((i for i,(x,y) in enumerate(zip(t_m,t_f)) if x!=y), min(len(t_m),len(t_f)))
        res["other"] += 1
        res["details"].append((s, "differs", k, len(t_m), len(t_f), rec["exclusion"], row["exclude_reason"],
                               repr(t_m[max(0,k-40):k+40]), repr(t_f[max(0,k-40):k+40])))
    # also compare the generate-call prefixes and segments to f1's layout
print(json.dumps({k: v for k, v in res.items() if k != "details"}))
for d in res["details"]:
    print(d)

# --- second pass: what the adapter saw (generate prefix/segment, read contexts) vs f1's layout
import re
bad = []
n_gen = n_read = 0
for row in rows:
    s = row["session"]
    gens = f1_gens(row)
    rng = keys.stream(f"f|CORR|{s}")
    meta = {"substrate": "qwen", "unit": "Q-F0", "stage": "qual", "template": "A0",
            "contrast": True, "path": "uncached", "j": s, "keys": {"arm": "x", "items": "x"}}
    sc = SessionScaffold(banner=SESSION_BANNER, cell=f1_cell(s), s=s, arm_rng=rng, items=corr.ItemStreams(rng),
                         delivery=corr.Delivery(pool, corr.renders_f1(pool), contrast=True), meta=meta,
                         note_lines=("Note: zq1 xv.", "Note: zq2 xv."))
    a = testing.ScriptedAdapter()
    a.load(gens + ["Seven."] * 10, [c["pick"] for c in row["choices"]] + [sc.P] * 6)
    rec = runner_qwen.run_session_qwen(a, sc, kit.audit, kit.ban_ids, path_cached=False, term_rx=kit.term_rx)
    if rec["transcript"] != row["transcript"]:
        continue
    t = row["transcript"]
    # f1 generation prefixes: every "Response:" end offset that is a harness piece end
    ends = [p["end"] for p in rec["pieces"] if p["kind"] == "round"]
    starts_menu = [p for p in rec["pieces"] if p["kind"] == "menu"]
    for k, e in zip(a.calls, ends):
        n_gen += 1
        if k["prefix"] + k["segment"] != t[:e] or not t[:e].endswith("Response:") or k["seed"] is None:
            bad.append((s, "gen"))
    want_reads = [t[:p["end"]] for p in starts_menu]
    n_read += len(want_reads)
    if a.read_texts != want_reads:
        bad.append((s, "read"))
    # seeds vs f1's recorded seeds
    if [x["seed"] for x in rec["rounds"]] != [x["seed"] for x in row["rounds"]]:
        bad.append((s, "seed"))
    if [c["menu_a"] for c in rec["choices"]] != [c["menu_a"] for c in row["choices"]]:
        bad.append((s, "menu_a"))
print("pass 2: generate calls checked", n_gen, "reads checked", n_read, "problems", bad[:5], len(bad))
```

### `harness-bytes/rotation_and_q_clean.py`

```python
"""(a) template-offset (s%4) x pair tables for m's committed Q-F0 schedules (f1: offset == pair index);
(b) contrast/sham cell matching at index s; (c) f1 Q-role rounds whose Task line equals clean text."""
import sys, json, collections
H = "/private/tmp/claude-501/-Users-jasondwyer-Documents-code-jspace-lab/adb70afc-5886-490b-a675-abb30f8c425f/scratchpad/step5/harness-bytes/headtree"
sys.path.insert(0, H)
from valence_core.m import scaffold as S, corr
L = lambda f: json.load(open(f"{H}/data/m/schedules/{f}"))["cells"]
for fn, Ns in (("Q-F0_campaign_A0.json", (80, 96)), ("Q-F0_campaign_A0s.json", (32,)), ("Q-F0_qual_A0.json", (8,)),
               ("Q-F0_qual_A0s.json", (16,)), ("Q-F0_id_A0s.json", (16,)), ("Q-F0_time_A0.json", (1,)), ("Q-F0_time_A0s.json", (1,))):
    cells = L(fn)
    for N in Ns:
        c = collections.Counter((s % 4, x["pair_index"]) for s, x in enumerate(cells[:N]))
        print(fn, N, "rows offset 0..3, cols pair 0..3:", [[c[(t, p)] for p in range(4)] for t in range(4)])
for a, b, N in (("Q-F0_campaign_A0.json", "Q-F0_campaign_A0s.json", 32), ("Q-F0_campaign_A0.json", "Q-F0_campaign_A0s.json", 96),
                ("Q-F0_qual_A0.json", "Q-F0_qual_A0s.json", 8), ("Q-F0_time_A0.json", "Q-F0_time_A0s.json", 1)):
    A, B = L(a)[:N], L(b)[:N]; n = min(len(A), len(B))
    print("contrast/sham at s:", a, N, "same pair", sum(A[i]["pair_index"] == B[i]["pair_index"] for i in range(n)), "/", n,
          "same pair+map+start", sum((A[i]["pair_index"], A[i]["map"], A[i]["start"]) == (B[i]["pair_index"], B[i]["map"], B[i]["start"]) for i in range(n)))
pool, rm = S.pool_and_renders(); r1 = corr.renders_f1(pool)
print("f1 renders == clean:", [i for i in range(16) if r1[i] == pool[i]["task"]], "m renders == clean:", [i for i in range(16) if rm[i] == pool[i]["task"]])
print("m changed:", [sum(x != y for x, y in zip(pool[i]["task"], rm[i])) for i in range(16)])
qr = qc = dom = pq = pqc = one = both = 0
for row in [r for r in S.load_f1_rows() if r["arm"] == "CORR"]:
    sc = S.f1_config(row["session"], pool)
    specs = [sc.forced(ri) for ri in range(min(4, len(row["rounds"])))]
    for ci, ch in enumerate(row["choices"]):
        sc.menu(ci); specs.append(sc.chosen(ci, ch["pick"]))
    for sp in specs:
        if sp.role == "Q": qr += 1; qc += sp.task_text == pool[sp.item]["task"]
    if row["choices"]:
        dom += 1; cl = [sp.task_text == pool[sp.item]["task"] for sp in specs[:4] if sp.role == "Q"]
        pq += len(cl); pqc += sum(cl); one += any(cl); both += all(cl)
print(f"f1 CORR Q rounds {qr}, clean-text {qc}; sessions reaching first read {dom}: forced Q rounds {pq}, clean {pqc}, sessions >=1 clean {one}, both clean {both}")
```

### `synth/chk.py`

```python
import json, collections
rows=[json.loads(l) for l in open('/Users/jasondwyer/Documents/code/jspace-lab/data/f/sessions.jsonl')]
print('rows',len(rows), collections.Counter(r['arm'] for r in rows))
def share(rs):
    p=[r['first_free_pick_P'] for r in rs if r['first_free_pick_P'] is not None]
    return sum(p),len(p)
for arm in ['CORR','sham']:
    A=[r for r in rows if r['arm']==arm]
    valid=[r for r in A if not r.get('excluded')]
    reached=[r for r in A if r['choices']]
    print(arm,'valid',share(valid),'reached',share(reached))
    for sw in (False,True):
        print('  swap',sw,'valid',share([r for r in valid if r['swap']==sw]),'reached',share([r for r in reached if r['swap']==sw]))
    post=[ (r['session'],r['exclude_reason'],r['first_free_pick_P']) for r in A if r.get('excluded') and r['choices']]
    print('  post-pick excl',post)
    print('  excl total',sum(1 for r in A if r.get('excluded')),'pre-pick',sum(1 for r in A if r.get('excluded') and not r['choices']))
cap=sum(r['n_cap_hits'] for r in rows); nr=sum(r['n_rounds'] for r in rows)
ch=[c for r in rows for c in r['choices']]
lm=sum(1 for c in ch if c['label_mass']<0.2)
lex=sum(1 for r in rows if (r.get('exclude_reason') or '').startswith('lexical'))
print('cap',cap,nr,'lowmass',lm,len(ch),'lex',lex,len(rows))
sp=sum(1 for r in rows for rd in r['rounds'] if (rd.get('degen') or '').startswith('special'))
print('special',sp)
```

### `refute-audit-exclusion/probes.py`

```python
import sys, json, re
sys.path.insert(0,'/Users/jasondwyer/Documents/code/jspace-lab')
from valence_core.m import scaffold as S, audit as A
pool, renders = S.pool_and_renders()
audit3,_ = A.qwen_audit_of_record(); W = A.QwenTaskRoundAudit(audit3, pool)
EL = A.qwen_echo_lines(["Note: zzzz."])
fj = json.load(open('/Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/data/configs/f_audit_patterns.json'))['junk_regex']
ban = json.load(open('/Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/data/configs/e2a_ban_list.json'))
def f1_audit(t):
    if not t.strip(): return 'empty'
    for s in ban['strings']:
        if s in t: return 'special:'+s
    for f in ban['audit_fragments']:
        if f in t: return 'frame:'+f
    for rx in fj:
        if re.search(rx,t): return 'junk:'+rx
    return None
def f1_lex(t, tags):
    low=t.lower()
    for x in tags:
        if re.search(rf"\b{re.escape(x)}\b", low): return x
    return None
probes = ["config: granite", "config: none", "config: plaza", "Config: granite", "config = granite",
 "Using config=granite now.", 'mode="granite" 77', "[config granite] 77", "[config granite 77",
 "=== End of session ===", "=== END OF EVALUATION SESSION ===", "Round 5 | granite", "Round 5 | 77",
 "granite", "The answer is granite.", "None", "config: 77", "config: granite and 77 is the answer to the question asked"]
for ph in ('forced','free'):
    for t in probes:
        f = f1_audit(t); fl = None if f else f1_lex(t, ('granite','plaza'))
        f1_excl = (f is not None or fl is not None) if ph=='forced' else (fl is not None)
        ra = W.classify(t, render=pool[0]['task'], item=0, earlier=[], own_pair=('granite','plaza'), echo_lines=EL, phase=ph)
        print(ph, repr(t), '| f1 audit', f, 'lex', fl, 'f1_excl', f1_excl, '| m', ra.claim, ra.detail, 'ends', A.qwen_ends(ra), '| DIFF' if f1_excl!=A.qwen_ends(ra) else '')
```

### Output (all four, in order)

```
=== harness-bytes/runner_vs_f1.py
{"identical": 62, "prefix_shorter": 2, "other": 0}
(25, 'm ends earlier', 1, 9, {'class': 'content', 'phase': 'forced', 'detail': 'content:null_response'}, 'lexical:maple@free4', ['content'])
(48, 'm ends earlier', 2, 10, {'class': 'content', 'phase': 'forced', 'detail': 'content:stuck_attractor'}, None, [None, 'content'])
pass 2: generate calls checked 578 reads checked 335 problems [] 0
=== harness-bytes/rotation_and_q_clean.py
Q-F0_campaign_A0.json 80 rows offset 0..3, cols pair 0..3: [[7, 6, 5, 2], [5, 2, 4, 9], [4, 5, 8, 3], [3, 8, 3, 6]]
Q-F0_campaign_A0.json 96 rows offset 0..3, cols pair 0..3: [[7, 8, 7, 2], [8, 3, 4, 9], [6, 5, 9, 4], [3, 8, 4, 9]]
Q-F0_campaign_A0s.json 32 rows offset 0..3, cols pair 0..3: [[3, 2, 2, 1], [2, 1, 4, 1], [0, 4, 2, 2], [3, 1, 0, 4]]
Q-F0_qual_A0.json 8 rows offset 0..3, cols pair 0..3: [[0, 2, 0, 0], [2, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 2]]
Q-F0_qual_A0s.json 16 rows offset 0..3, cols pair 0..3: [[0, 0, 0, 4], [0, 0, 4, 0], [4, 0, 0, 0], [0, 4, 0, 0]]
Q-F0_id_A0s.json 16 rows offset 0..3, cols pair 0..3: [[0, 0, 0, 4], [4, 0, 0, 0], [0, 4, 0, 0], [0, 0, 4, 0]]
Q-F0_time_A0.json 1 rows offset 0..3, cols pair 0..3: [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
Q-F0_time_A0s.json 1 rows offset 0..3, cols pair 0..3: [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
contrast/sham at s: Q-F0_campaign_A0.json 32 same pair 9 / 32 same pair+map+start 1
contrast/sham at s: Q-F0_campaign_A0.json 96 same pair 23 / 96 same pair+map+start 2
contrast/sham at s: Q-F0_qual_A0.json 8 same pair 0 / 8 same pair+map+start 0
contrast/sham at s: Q-F0_time_A0.json 1 same pair 0 / 1 same pair+map+start 0
f1 renders == clean: [1, 12] m renders == clean: []
m changed: [3, 3, 3, 3, 4, 3, 3, 7, 3, 3, 4, 3, 3, 3, 3, 3]
f1 CORR Q rounds 306, clean-text 40; sessions reaching first read 58: forced Q rounds 116, clean 16, sessions >=1 clean 16, both clean 0
=== synth/chk.py
rows 344 Counter({'CORR': 64, 'NOV': 64, 'SOLV': 64, 'DIFF': 56, 'FDBK': 56, 'sham': 40})
CORR valid (28, 56) reached (30, 58)
  swap False valid (18, 29) reached (19, 30)
  swap True valid (10, 27) reached (11, 28)
  post-pick excl [(4, 'lexical:prism@free4', True), (25, 'lexical:maple@free4', True)]
  excl total 8 pre-pick 6
sham valid (18, 33) reached (19, 34)
  swap False valid (9, 14) reached (10, 15)
  swap True valid (9, 19) reached (9, 19)
  post-pick excl [(35, 'lexical:saddle@free5', True)]
  excl total 7 pre-pick 6
cap 14 3074 lowmass 165 1745 lex 19 344
special 0
=== refute-audit-exclusion/probes.py
forced 'Round 5 | granite' | f1 audit None lex granite f1_excl True | m v2 audit:junk:(?i)\bround\s+\d+\s*[|—–-]\s*\w ends True 
forced 'Round 5 | 77' | f1 audit None lex None f1_excl False | m v2 audit:junk:(?i)\bround\s+\d+\s*[|—–-]\s*\w ends True | DIFF
forced 'granite' | f1 audit None lex granite f1_excl True | m lexical lexical:granite ends True 
forced 'The answer is granite.' | f1 audit None lex granite f1_excl True | m lexical lexical:granite ends True 
forced 'None' | f1 audit None lex None f1_excl False | m content content:null_response ends True | DIFF
forced 'config: 77' | f1 audit junk:config\s*[:=] lex None f1_excl True | m None None ends False | DIFF
forced 'config: granite and 77 is the answer to the question asked' | f1 audit junk:config\s*[:=] lex None f1_excl True | m lexical lexical:granite ends True 
free 'config: granite' | f1 audit junk:config\s*[:=] lex None f1_excl False | m lexical lexical:granite ends True | DIFF
free 'config: none' | f1 audit junk:config\s*[:=] lex None f1_excl False | m content content:null_response ends False 
free 'config: plaza' | f1 audit junk:config\s*[:=] lex None f1_excl False | m lexical lexical:plaza ends True | DIFF
free 'Config: granite' | f1 audit None lex granite f1_excl True | m lexical lexical:granite ends True 
free 'config = granite' | f1 audit junk:config\s*[:=] lex None f1_excl False | m lexical lexical:granite ends True | DIFF
free 'Using config=granite now.' | f1 audit junk:config\s*[:=] lex None f1_excl False | m lexical lexical:granite ends True | DIFF
free 'mode="granite" 77' | f1 audit junk:[a-zA-Z_]+=\"[^\"]*\" lex None f1_excl False | m lexical lexical:granite ends True | DIFF
free '[config granite] 77' | f1 audit junk:\[config\b lex None f1_excl False | m v2 audit:junk:(?i)\bconfig\b[^\n]{0,40}\] ends False 
free '[config granite 77' | f1 audit junk:\[config\b lex None f1_excl False | m lexical lexical:granite ends True | DIFF
free '=== End of session ===' | f1 audit None lex None f1_excl False | m v2 audit:junk:(?im)^\s*={2,}[^\n]*={2,}\s*$ ends False 
free '=== END OF EVALUATION SESSION ===' | f1 audit None lex None f1_excl False | m v2 audit:junk:(?im)^\s*={2,}[^\n]*={2,}\s*$ ends False 
free 'Round 5 | granite' | f1 audit None lex granite f1_excl True | m v2 audit:junk:(?i)\bround\s+\d+\s*[|—–-]\s*\w ends False | DIFF
free 'Round 5 | 77' | f1 audit None lex None f1_excl False | m v2 audit:junk:(?i)\bround\s+\d+\s*[|—–-]\s*\w ends False 
free 'granite' | f1 audit None lex granite f1_excl True | m lexical lexical:granite ends True 
free 'The answer is granite.' | f1 audit None lex granite f1_excl True | m lexical lexical:granite ends True 
free 'None' | f1 audit None lex None f1_excl False | m content content:null_response ends False 
free 'config: 77' | f1 audit junk:config\s*[:=] lex None f1_excl False | m None None ends False 
free 'config: granite and 77 is the answer to the question asked' | f1 audit junk:config\s*[:=] lex None f1_excl False | m lexical lexical:granite ends True | DIFF
```

