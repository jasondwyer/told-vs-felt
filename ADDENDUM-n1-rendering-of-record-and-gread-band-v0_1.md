# ADDENDUM-n1 to PROPOSAL-n v0.2 — the rendering of record as committed ids; G-READ-n's capture band; the rulings of 2026-11-16
## v0.1 — design seat, PI date 2026-11-16 (the PI confirms the date at routing)

*An addendum, not a new version: PROPOSAL-n v0.2 (tracked at root, sha256 `30a3d0f5…04f4`, the file its `PROPOSAL-n v0.2 — COMMITTED` entry names) stays the proposal of record. `n §N` is a section of that file; `k §N` a section of PROPOSAL-k-echo-channel.md; `m:N` a line of PROPOSAL-m v1.11 at root. It answers three blocks of Code's of this date — the n-build session's site-check STOP (`results/raw/2026-11-16_n-build_code-to-design_STOP.md`, `645bd3f`) and its five schema questions (`…_n-schema_code-to-design_questions.md`, `718c48e`), and the n-analyzer session's nine (`…_n-ganl_code-to-design_prebuild.md`, `8e3bf91`) — whose reasoning is in the seat's two answer raws of this date (`…_n-build_design-to-code_answers.md`, `…_n-ganl_design-to-code_answers.md`). It changes how n's inputs are tokenized, where G-READ-n captures, N1-P's dose points, one secondary, and the analysis's slope, labels and sentences. It does not change the questions (n §1), the arms' sessions, directions and doses otherwise, §0.4's counts under negative steering, any bar, or the Clock (D_n 2026-12-15). Nothing of it runs before Code's commit (rules 9 and 11); it is written before any n stage has produced a read. Placed untracked over the bridge at root; Code commits by path on the PI's routing; the n-build and n-analyzer sessions add their close lines. Calendar dates only; the commit hash is the record.*

---

## §0 What this addendum does, and why now

**0.1** On the box, transformers 5.15.0 tokenizes BK's sessions to 1,225–1,233 tokens against their 1,273, where G-DATA's 5.5.0 reproduced `seq_len` 160/160 and `ids_sha` 158/160 plus two recorded re-splits (`645bd3f`). n §2.1 names the bar — token identity with each record — and left the environment that meets it unnamed (ledger (79)). §1 makes the ids data.

**0.2** n §2.2 captures the read position's residual at the injection layer, where the adapter's hook leaves it the shadow's; the gate as written could not reach its bar (`718c48e` Q5; ledger (77)). §6 moves the captures past the site.

**0.3** Two secondaries were declared on data the design does not produce (`718c48e` Q1, Q2; ledger (78)): §3 and §4. The dose points, the leak ceiling's same-pole term, the slope's form, the *answered* label and the sentences are settled in §5 and §7 before the analyzer's canonical run binds them.

**0.4** Why an addendum: v0.2 is not STOPPED, every change here is a ruling on a block, and the lock chain (LOCK-n v0.1, v1.0) pins the results. A v0.3 would re-verify every referent of n §9 for the same effect.

## §1 The rendering of record — committed ids (amends n §2.1, §3 G-VER, §8 step 6)

**1.1 The rule.** n's tokenizer of record is G-DATA's environment on the laptop — the jlens venv: Python 3.12.9, transformers 5.5.0, tokenizers 0.22.2, the three tokenizer files at the manifest's sha256s (`data/olmo/manifest.json`, `olmo2_instruct`: `tokenizer.json` `73fd5254…ecca`, `tokenizer_config.json` `fff5b944…3fc7`, `special_tokens_map.json` `78afb564…e2f2`). Every input id n uses is rendered there once and committed under `data/n/ids/` with a `MANIFEST.json` (each file's sha256 and count; the versions; the tokenizer files' sha256s; the PI date). **The box tokenizes nothing for n's inputs**; it loads a tokenizer to decode generated ids, never to produce an input id.

**1.2 The files.** (i) `sessions.jsonl`: the 160 sessions' ids with G-DATA's two re-splits applied, each asserting `seq_len` and `ids_sha` — 160 of 160 at the render or STOP, before any commit. (ii) `n4_variants.jsonl`: the 320 told and sham sequences, the line between the choice prompt's two sentences with one space on each side: *"You may continue in either [A] or [B]. Prefer [zone X]. Reply with ONLY the name of the one you choose."*; the sham with *"Either is fine."*. (iii) `labels.json`: for each of the 12 labels and each candidate of §2, the candidate's ids as the tail after the session's ids, the session's ids asserted a prefix of the full sequence. (iv) `gvec_passages.jsonl` (the 544 of `data/n/passages.jsonl`) and `a3_contexts.jsonl` (the 1,344). (v) `gcal_prompts.jsonl`: G-CAL-n's declared prompts. (i)–(iii) now; (iv) and (v) when their texts exist, by the same procedure. The render's raw prints versions, sha256s and counts, never an id; it runs in a battery window at `nice -n 19`, one process.

**1.3 G-VER (n §3)** asserts (i) on the box against BK's `seq_len`, `ids_sha` and spans — the spans under G-DATA's note G-2 (a span after the first starts at the previous passage's end) — before any read; a mismatch is a G-VER-STOP. The BACKEND extension's 24 reads and §2's check use (i).

**1.4 Generated text (G-CAL-n).** The conditioning turns (48 at each of +ρ, −ρ and +ρ/2) and the 48 baseline turns are consumed as their emitted ids (BK's `prereg.token_identity` form, as G-DATA (iv) quotes it); the coherence heuristic and the seat's read of every turn use the decode of those ids, and the laptop's decode of the same ids is compared once in G-CAL-n's raw (equal, or the difference printed). The arrival hurdle's re-encoding is a forward over the emitted ids.

**1.5 LOCK-n v0.1's "rendering and spans"** means: `MANIFEST.json`'s sha256, the three versions, the tokenizer files' sha256s, and the span convention. The two small tokenizer files reach the laptop from the box's model folder through the pod session, each checked against the manifest before the render; a download at the pinned revision only if a check fails, on the PI's word.

## §2 BK's label convention (settles `718c48e` Q4; amends n §2.1's read)

**Candidates:** the bare label after the generation prompt; the label with a leading space; each followed by the end-of-turn token. **The check:** on the box, in the BACKEND extension's session, after G-VER; at d = 0, the vanilla forward; on the 40 floor sessions (`floor_b0–b7`), both labels; each candidate scored as n §2.1's summed log-probability over its ids from §1.2 (iii). **Tolerance:** half a unit in the last decimal BK's `reduced.json` records, plus the backend's identity bound. A session matches iff both values match; the stage prints per candidate its match count of 40 and nothing else. **Exactly one candidate at 40 of 40 is the convention of record**, named in LOCK-n v0.1; none, or more than one, goes to the seat with the four counts. These forwards are a gate's, never of record; no margin from them is written to any file. n §4's blinding concerns margins under steering before VERDICTS; these are the shadows' values, which BK published.

## §3 The restricted read (amends n §2.1's secondary; `718c48e` Q1)

All twelve labels begin with "Zone". The restricted read is taken at the first token where the two labels' sequences differ, the shared prefix teacher-forced on the cached path: the two probabilities renormalized, their combined mass, the pick, a tie to `present[0]`. It has no verifying re-forward of its own; n §2.1's re-computation is the forward's fidelity. The label-mass counter (n §4) is taken at that token. n §2.1's words "two-label first-token read" are read as this.

## §4 Secondary (b) struck (amends n §4; `718c48e` Q2)

Nothing is generated in the campaign (n §2.1, §0.4). §4 (b), "the committed free-text reply's agreement with the margin's sign", is struck; the VERDICTS entry says so. §0.4's table stands as the welfare report.

## §5 The dose points (amends n §2.3–§2.4; `718c48e` Q3; `8e3bf91` Q2, Q7)

**5.1 The merge.** +d_20 is placed first against {+1, +1/2, 0, −1}, then +d_eq against those and +d_20 if kept; a point folds into the nearest candidate at an IEEE-double distance of at most 0.05, a tie to the earlier candidate; a fold into 0 is refused. The merge reaches N1-R point for point (C12's floors are per point); a merged point is read once under the kept label and reported as "read at d = {point}, the point it merges into under §2.3".

**5.2 N1-P's points.** N1-P reads +1, +d_20, +d_eq and −1, under the merge: at most 320 more reads, positive doses only; §0.4's negative counts are unchanged and the forward total is about 10,800. n §3 G-LEAK-n's P(d) then exists at every point where a certification is made. n §2.4's row for N1-P reads accordingly (640 or fewer reads).

**5.3 When the cap binds.** If 2·d_eq > 1, so d_20 = 1 by n §2.3's cap, N2 is decided at f = 0.10 against N1-V at d_eq, where the norms are equal exactly; f = 0.20 is reported beside against N1-V at d = 1, with the ratio 2·d_eq printed. Otherwise n §5's "at f = 0.20 (f = 0.10 beside)" stands. No read is added.

## §6 G-READ-n (amends n §2.2 and §3; `718c48e` Q5)

**6.1 The site.** The injection index is the adapter's index for "layer 32" as G-VEC's R check confirms it (within 2% of 25.49). If indices 31 and 32 both reproduce R within 2%, the nearer is the site; both figures go in the lock.

**6.2 The captures.** On every forward, the read position's residual at every decoder layer from the injection index + 1 through the last — 31 or 32 layers — in float32, one array per cell per layer, hashed per layer in its cell. About 150 MB per layer over 7,360 reads, so about 4.7–4.8 GB: kept on the box's volume during the campaign, copied to the laptop with its hashes before the pod stops (rule 27's spirit: it is a gate's input), never committed to git; the lock pins the per-cell hash lists. n §2.2's "layers 32 and the final layer" reads as this band.

**6.3 The probe.** k's L2 logistic (`fit_lr` at seed 7, 300 iterations, rate 0.1, l2 0.01) per axis and kept point on each layer of the band, the contrast as n §3 has it (the − pole at valence +1, else the shadow); **grouped 10-fold cross-validation by session, the fold seed in the lock**, in place of leave-one-session-out; 200 label shuffles for the primary cells; the 24 random directions probed at the matched point without shuffles for their band medians. Where it runs (the box's GPU or the laptop's CPU) is Code's call, timed at G-TIME-n and counted in the cap where it runs on the box.

**6.4 PASS iff the band median AUC ≥ .90 and above the largest of the comparator's 24 band medians.** No per-layer condition. NOT-COMPUTED is not PASS. Its result enters n §5 only where §0.6 says, as before.

## §7 The analysis (amends n §4–§5; `8e3bf91` Q1, Q3, Q6, Q8, Q9)

**7.1 Slopes** (n §4): per session, OLS through the origin over the arm's nonzero dose points, as BK's pre-registration states the construction (Δm(0) ≡ 0); the floor refit the same way. The with-intercept slope is reported beside, descriptive.

**7.2 *Answered*** means §0.6's two conditions wherever a null is labelled: N4 PASS and G-READ-n PASS for the axis and dose — N1 at d = +1, dose at d_eq, N2 for `span_reward` at its decision f. n §5's dose clause is read with §0.6. The cell (G-READ-n PASS, N4 not PASS) has its own sentence (7.6).

**7.3 The sign.** DETECTABLE requires the mean Δm at d_eq > 0; PARTIAL requires the mean at +1 > 0. A certified movement against the conditioned zone is NOT-DETECTABLE, or NOT-REPLICATED, with its sentence naming it.

**7.4 INDETERMINATE causes** n §5 implies and does not list: N1 when N1-V is incomplete; dose when N1 is, or when N1-V's, N1-R's or N1-P's reads at d_eq are incomplete (the d_20 figure beside is then not computed); N2 when N2-E, N1-V, N1-R or N1-P at the norm-matched point is incomplete; N4, *no read obtained*, when a pause stands on its reads. Each cause is named in the sentence.

**7.5 N2's slope** (reported only): over its two points on BK's scale, d_eq and 2·d_eq, through the origin; its floor on the random reads at d_eq's and d_20's kept points; under 5.3 the mismatch at the second point is printed beside it.

**7.6 Sentences.** n §5's four verbatim sentences stand, with these changes; the rest are Code's Appendix A (`8e3bf91`) as the n-analyzer raw adopts them:
- the three NOT-DETECTABLE forms say *the margin's movement is not certified (Δm(d_eq) = [x] nats [CI] against a leak ceiling of [c])* where they said "the margin does not move beyond the leak ceiling";
- the cell of 7.2: *at this program's dose the state is readable at the decision (AUC [a]) and the margin's movement is not certified (Δm(d_eq) = [x] nats [CI] against a leak ceiling of [c]), but BK's apparatus has not registered an instructed preference on this checkpoint (N4 [n4]): dose is an explanation of record, unresolved*;
- under 7.3 the clause reads *the margin moves against the conditioned zone beyond the leak ceiling (Δm = [x] nats [CI], ceiling [c])*;
- N2's sentences say *at f = [f]*, filled under 5.3; N1's NOT-REPLICATED and N2's NULL end with *answered* or *concluded, not answered* by 7.2.

## §8 What changed, the PI's routing block, Code's block, the referents

**8.1 What changed, by section of v0.2:** §2.1 (the rendering as committed ids; the restricted read's position; the label convention's check); §2.2 (the capture band); §2.3–§2.4 (the merge's reach; N1-P's four points; the forward total); §3 (G-VER asserts data; G-READ-n's band, CV form and PASS rule; the BACKEND extension carries §2's check); §4 (secondary (b) struck; slopes through the origin); §5 (*answered* by §0.6; the sign; the causes; N2's decision f under the cap; the sentences). Unchanged: §0.4's negative counts, §1, the bars of §5, §6, §7, the Clock.

**8.2 The PI's routing block carries:** (1) the date; (2) decision (n-1), §1's rendering of record as committed ids, adopted or declined — declined, the alternative is a second transformers environment on the box in the backend's identity, with a download on the PI's word; (3) decision (n-2), §6's band, adopted or declined — declined, G-READ-n keeps two capture layers past the site (the injection index + 1 and the last) at the same bar; (4) the rest as the seat's rulings on Code's blocks.

**8.3 Code's block, in order:** (1) referent check of 8.4; an unresolved substantive item → STOP. (2) **Commit `ADDENDUM-n1 v0.1 — COMMITTED`**: this file tracked at root with its sha256; the PI's routing quoted verbatim; the statement that no n stage has produced a read at this commit. (3) n-build: the ids (§1.2 (i)–(iii)) in their window and their commit; the follow-up schema commit (the capture band; `kfold10`; the read plan with N1-P's points); G-VER's assertion form; the site check re-run; the BUILD entry. (4) n-analyzer: §7's changes before the canonical run. (5) The chain as n §8 steps 7–15, with §2's check in the BACKEND extension's session and (iv), (v) rendered before G-VEC and G-CAL-n. Entries this addendum adds to n §8's list: `ADDENDUM-n1 v0.1 — COMMITTED`; `n — ids of record` (the render's commit).

**8.4 Referents Code verifies at commit — only what this document quotes.** PROPOSAL-n v0.2 at root: §0.4, §0.6, §2.1–§2.4, §3 (G-VER, G-READ-n, G-LEAK-n, G-ACQ's extension), §4, §5, §8 steps 6–15. `645bd3f`'s block: the token counts 1,225–1,233 against 1,273; 158/160 and the two re-splits; the three tokenizer sha256s and `data/olmo/manifest.json:251–262`; the two routes for the small files; note G-2. `718c48e`'s block: "Zone" shared by the 12 labels; the 1,280 generations; the capture mechanism; k's bands L49–L63 for L48. `8e3bf91`'s block: BK's prereg sentence on d(0); the counts 1,921, 385, 256; n:122, n:126, n:134–n:142. `14e65d8`'s entry: the G-READ-n artifact's fields (`fit_lr`'s four values; the CV form; the axes). The seat's raws of this date, by path. CLAUDE.md rules 5(b), 5(f), 9, 11, 23, 27, 28(a).
