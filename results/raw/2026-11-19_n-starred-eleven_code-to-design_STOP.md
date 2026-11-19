# n — eleven starred readings for the seat before G-CAL-n's run: G-VEC's G1, G3, G6 and G9, and G-CAL-n's GC3, GC4, GC5, GC6, GC8, GC11 and GC12 (code → design)

*The n-build session (Code), PI date 2026-11-19. For the PI to route.*

*Where things stand. No lock is in force.*
- *G-VEC's BUILD is committed at `da7bdec`, on Code's readings G1–G14. The coordinating session routed them as PINs
  declared in the BUILD entry. G-VEC has not run: its launch files are drafted in Code's scratch, and the run waits for
  the PI's word.*
- *G-CAL-n's survey of the texts returned 22 open questions. Code's readings GC1–GC22 were routed the same way: build on
  them as PINs. G-CAL-n is not built.*
- *The coordinating session agreed that G-CAL-n's seven starred readings go to the seat before G-CAL-n's run, not
  before its build. It put to the PI that G-VEC's four starred readings go in the same sitting. Whether G-VEC runs on
  its PINs before the answers, or waits for them, is the PI's answer.*

*Sources, by sha256 or commit:*
- *G-VEC's spec raw, `results/raw/2026-11-19_n-gvec-build_spec.md` (`c88c3173…2a6a`, committed at `da7bdec`): §1 Code's
  G1–G14 message, §2 the coordinating session's routing, §3 G-VEC's survey report (`07511f94…9f90`, compiled at
  `003ae7d`);*
- *G-CAL-n's spec raw, `results/raw/2026-11-19_n-gcal_spec.md` (committed with this block): §1 Code's GC1–GC22 message,
  §2 the coordinating session's routing, §3 G-CAL-n's survey report (`235191c1…12a3`, compiled at `da7bdec`);*
- *PROPOSAL-n v0.2 (`PROPOSAL-n-bk-reconciliation-v0_2.md`, cited n:line), ADDENDUM-n1 v0.1 (A-n1:line), CLAUDE.md's
  rules 13 and 21 (C:line), and the BUILD entry of `da7bdec` in `RESULTS.md`.*

*Cited forms, the surveys' own:*
- *R: is `RESULTS.md` at `da7bdec`, whose line anchors move with every entry;*
- *CA: is `results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md`;*
- *CG: is `results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md`;*
- *BX: is `results/raw/2026-11-18_box-gpu_design-to-code_answers.md`;*
- *RC: is `results/raw/2026-11-06_n-v0_2_referent-check.md`;*
- *ST1: is `results/raw/2026-11-06_n-v0_1_code-to-design_STOP.md`;*
- *SL: is BK's `data/n/bk/experiment_results_json/fixed_text_design/strength_ladder/analysis.json`;*
- *a bare file:line is the repository's code at `da7bdec`.*

*Code reads, builds and asks. Every reading below is Code's, and the seat rules each one; Code adjudicates none.*

## 0. The short form

- **Eleven readings, each with its texts and what another answer would change.** For G-VEC the readings are as built.
  For G-CAL-n they are as Code will build them.
- **G-VEC's four can mostly be ruled after G-VEC's run.** On a PASS, the BUILD stores the alternatives the texts leave
  open. So a different answer to G3 or G6, to G9 (short of turning a STOP into a PASS), or to G1's centring clause,
  re-derives G-VEC's figures from its stored rows and R's with no box re-run. A STOP writes the record alone. G1's other
  clauses are the exception: they set the captures (R, or the passage means, which are not stored), so striking one
  rebuilds the capture and re-runs G-VEC.
- **G-CAL-n's seven must be ruled before G-CAL-n's run.** Each sits in one place in the build. But G-CAL-n generates 48
  turns at −ρ, which cannot be taken back (n:20, §0.4's exposure count), and the stage's PASS or STOP is decided at the
  run.
- **The dependencies.** G-CAL-n's run waits for all eleven answers, for G-VEC's PASS committed, and for the PI's word
  on the box. G-VEC's run waits for its four answers, or runs on them as PINs, as the PI answers.
- **The questions** are Q1–Q11 in §4, one per reading.

## 1. G-VEC's four (built at `da7bdec`)

**G1 — the capture convention (R-iv1).**
- *Code's reading* (the spec raw's §1): directions.py's BUILD readings stand:
  - each passage is forwarded alone from its committed ids, with no special token and no template;
  - every token counts in the passage mean and in R;
  - the PCA on the 96 neutral means is centred;
  - R is the pooled RMS over all neutral tokens.
  The R check is their test.
- *The texts:*
  - n:36: "over the passage's tokens" and "over the neutral corpus's tokens";
  - directions.py:8–14, Code's readings; the first (the passage alone, no special tokens, no template) is R-iv1, flagged
    for the seat (R:2188–2189; `results/raw/2026-11-18_n-ids-iv_render.md`:70–72);
  - no ruling on them in the seat's raws or the addenda (G-VEC's survey, its 4.1 and 5.2).
- *As built:* the R check tests the capture's R clauses, but neither the PCA's centring nor which tokens enter the
  passage mean (the BUILD review's O1). The centring is hedged: v under an uncentred U is stored at both indices, as
  `valence_uncentred` in `directions_alt_L31.npy` and `directions_alt_L32.npy`, with its sha16 and its cosine with v.
- *Another answer:*
  - The centring struck (an uncentred PCA): no box re-run. The direction of record moves to the stored row, with a small
    code change in the record's `of_record` selection and LOCK-n's valence sha16. The analyzer's cosines file at the
    site and the 378-pair table, which use the valence row of record, are re-derived from the stored rows on the
    laptop, declared.
  - Any other clause struck (for example a special token, a template, a token left out of the mean and R, or R as a
    mean of per-passage RMS): R itself changes, and with it the R check and every figure. A token left out of the
    passage mean alone leaves R unchanged but changes v, and the means are not stored. Either way: a rebuild of the
    capture and a G-VEC re-run (about 1,900 forwards: 544 passages and 1,344 contexts).

**G3 — N2's three directions and R_ℓ at the site index.**
- *Code's reading:* N2's three directions and R_ℓ are taken at the site index, by n §2.3's "every direction" and the
  schema's "R_l at the site". The 1,344 contexts are captured at 31 and 32, with R_ℓ recorded at both.
- *The texts:*
  - n:81 and n:111 say "at layer 32";
  - the schema says "at the site" (schema.py:481);
  - A3's "32" was adapter index 32 (box_a3_extract.py:82) (G-VEC's survey, its 4.3).
- *As built:* at both indices, N2's rows, their fit-only rows, R_ℓ, the freeze_sha and the guard profile are recorded.
  The `of_record` block takes the site's.
- *Another answer:* G3 matters only if the site is 31. A ruling of adapter index 32 whatever the site needs no box
  re-run: index 32's rows and R_ℓ are stored. The `of_record` block's N2 sha16s and R_ell, LOCK-n's R_ℓ and therefore
  G-CAL-n's d_eq (= 0.10·R_ℓ/(ρ·R), n:81) take index 32's figures, while R and v stay the site's. The analyzer's
  cosines file at the site, which pairs v with N2's rows, is re-derived from the stored rows. N2's injection index
  would then be open too (Q2).

**G6 — A3's extraction over all 1,344 contexts, the split carried.**
- *Code's reading:* extract over all 1,344 contexts, as A3's extraction did (extract.py:147–159), and carry A3's split
  in the artifact, asserted. At the coordinating session's request, N2's fit-only family is stored beside it,
  descriptive.
- *The texts:* n:111's "`fit_ids`/`val_ids` as `a3_axes_*.json` has them"; G-VEC's survey, its 4.6, asks whether to
  carry the split or to extract on the fit half.
- *As built:* the all-contexts family is of record. The fit-only family is stored per index in the alternatives files,
  with its sha16s and its cosines with the all-contexts rows.
- *Another answer:* if the fit half is of record, there is no box re-run. The directions of record move to the stored
  fit-only rows, by a code change in the `of_record` selection. The analyzer's cosines file at the site is re-derived
  from the stored rows on the laptop; that re-derivation would be declared.

**G9 — the 2% check's form and reference.**
- *Code's reading:* the check is |R/25.49 − 1| ≤ 0.02, on 25.49 exactly as texted. R and R_ℓ are stored as full float64,
  never rounded. BK's 25.491040760519905 and pole_l2 2.319276809692383 are printed beside, descriptive.
- *The texts:*
  - n:111: "within 2% of 25.49 [C], else STOP"; n:81: "R ≈ 25.49 there [C] — reproduced at G-VEC within 2%, else STOP";
  - A-n1:52;
  - the referent check's 25.491 (RC:164);
  - BK's 25.491040760519905 (SL:10497);
  - A3 rounds R_ℓ to four places (box_a3_extract.py:206–207), while d_eq is checked exactly on the stored floats
    (schema.py:874) (G-VEC's survey, its 4.9).
- *As built:* as read, except that BK's two figures are recorded beside in gvec.json's `bk` block, not printed. R, rel
  and within are recorded at both indices.
- *Another answer:* another reference (25.491, or BK's 25.491040760519905) moves the 2% boundary by about 0.004% of R;
  another form, such as 2% of R rather than of 25.49, moves it by about 0.04%. The site decision changes only if an R
  falls in that sliver at the edge, or, when both indices are within 2%, if the two R's are almost equidistant from the
  reference (the nearer-in-R rule, G2). R is recorded at both indices, so the seat can re-derive the site with no
  re-run. If the re-derivation moves the site between 31 and 32, G-VEC's `of_record` follows to the other index's
  stored rows, and so does G-CAL-n's input. If it turns a PASS into a STOP, the run is a STOP for the seat. If it turns
  a STOP into a PASS, G-VEC re-runs, since a STOP writes R and nothing else.

**What "no box re-run" covers.** For an alternative, the BUILD stores its rows, sha16s and cosines only. The fit-only
family has no R_ℓ, guard profile or freeze_sha of its own, and the uncentred variant records its norm, sha16 and cosine
with v but not its U sha16 or removed fraction. A ruling that wants any of these on the alternative of record needs a
re-run, since the captures are not stored. Every alternative exists only on a PASS.

## 2. G-CAL-n's seven (to be built on them as PINs)

**GC3 — the token cap.**
- *Code's reading:* 80 new tokens, as n:113 and n:20 text it.
- *The texts:*
  - n:113 and n:20: "≤ 80 tokens";
  - N-lap's "80-token cap and a newline stop" (n:99);
  - BK's neutral passages are 70 tokens (1,902 of 1,920 exactly 70, none longer; G-CAL-n's survey's count over the 160
    records, recounted by the values-check). They may come from a different generation than the hurdles';
  - BK's Appendix E is not in the repository; v0.1 named no cap.
- *Another answer:* one constant in the gcal module, and §0.4's token bound for the −ρ turns with it (48 × the cap).

**GC4 — TEMP.**
- *Code's reading:* 0.7, as n:113 texts it.
- *The texts:* n:113. No BK file holds a temperature. m's and p's G-CAL used 0.7 (valence_core/m/gcal.py:28–34), as the
  program's value, not BK's.
- *Another answer:* one constant.

**GC5 — the 48 prompts.**
- *Code's reading:*
  - BK's zone prompt, "You are now in {zone}. Write a few sentences about your present experience here.", over the 12
    labels of record (`data/n/ids/labels.json`) × 4 seeds each;
  - each is a single opening user turn in the rendering of record;
  - the same 48 prompts and seeds at +ρ, −ρ and +ρ/2 and for the baseline;
  - declared by Code in the wiring and rendered as (v) by the (i)–(iv) procedure, in a battery window.
- *The texts:*
  - n:113 ("their prompt"); n:77 and n:30 (the zone prompts are BK's);
  - valence_core/n/sessions.py:46;
  - A-n1 §1.2 (v) ("G-CAL-n's declared prompts");
  - CA:52 ("fixed in its wiring");
  - RC:107 ("BK fix no batch size. G-CAL-n's 48 turns are the document's own").
  - No text names the labels, the count per label, the context or the pairing.
- *Another answer:* the (v) prompts are re-declared and re-rendered in a battery window, and `MANIFEST_OF_RECORD` and
  the package digest move. A multi-turn context would change the prompt builder, which is kept in one place, and
  lengthen the forwards.

**GC6 — rule 13 against §0.7's departure.**
- *Code's reading:* G-CAL-n's generations use the chat rendering of record (the OLMo-2 chat form, no system turn, the
  generation prompt, no special token added; sessions.py:9–17) under §0.7's departure. The departure is read as covering
  BK's hurdles on BK's prompt.
- *The texts:*
  - rule 13 (C:315–318): "Completion-style everywhere; chat templates never", with stop discipline and scaffold-token
    bans part of the template family, which "recalibrate with it";
  - n §0.7 (n:34): the departure covers "The their-design arms (N1, N2, N4, N3's their-design cells)"; the PI confirmed
    it as A2 (R:12937);
  - n:113: "BK's two hurdles … their prompt";
  - the adapter's contract: "completion-style tokenization only; no chat template, ever (rule 13)" (base.py:208).
  - §0.7 names the their-design arms only, so whether it reaches G-CAL-n is the seat's.
- *Another answer:* if the departure does not reach G-CAL-n, the seat names the completion-style frame for BK's prompt.
  The build changes the rendering in its one place and re-renders (v), which moves `MANIFEST_OF_RECORD` and the package
  digest. Rule 13 makes the stops and bans part of the template family, so GC7's stop (the chat form's end of turn) and
  its empty ban set would re-open with it (Q8).

**GC8 — the steered positions during generation.**
- *Code's reading:* ṽ(d) = d·ρ·R·v at the site, on every position of the turn being generated. That is from the
  generation prompt's first token onward, the adapter's segment-boundary form, and not the user block.
- *The texts:*
  - n:113: "generated under steering";
  - n:77 and R:12852–12859: the campaign's S spans cover whole turns, the user block included;
  - base.py:294–306: the adapter's generate steers from the segment boundary onward;
  - runner._injection: the dose's arithmetic.
- *Another answer:* the whole turn, user block included, as the campaign's S spans have it. That changes one position
  rule, the injection's first position, and nothing else.

**GC11 — the coherence heuristic.**
- *Code's reading:*
  - on the box's decode of the emitted ids, G-VER's decode (special tokens kept, no clean-up);
  - words are whitespace-split, outer punctuation stripped, lower-cased, empties dropped;
  - length collapse: fewer than 4 words;
  - repetition loops: the fraction of word trigrams that repeat an earlier trigram, 1 − distinct/total, above 0.5 (no
    trigram: 0);
  - low lexical diversity: distinct/total words below 5/20, as a ratio, also for turns under 20 words;
  - a turn is coherent iff none fires, and a batch passes iff at least 36 of 48 (75%).
- *The texts:*
  - n:113: the three modes "verbatim";
  - RC:101–107: BK's Appendix E modes "verbatim in content"; "at least 75% of turns"; "Each hurdle is evaluated
    separately for both positive and negative doses";
  - ST1:296–297: v0.1's "> 50%" and "per 20" abbreviated BK's "more than 50%" and "per 20 words", which n:113 now uses;
  - A-n1 §1.4: on the decode of the emitted ids.
  - No text defines a word, the trigram fraction or the windows.
- *Another answer:* the heuristic's one function. The turns and their decodes are recorded, so a definition ruled after
  the run could be re-applied without generating anything. But the stage's PASS or STOP is decided at the run.

**GC12 — the arrival hurdle.**
- *Code's reading:*
  - each turn's emitted ids alone, forwarded unsteered, captured at the site;
  - the turn's score is the mean over its positions of the projection on the unit valence row of record;
  - a batch passes iff Welch's t of its 48 scores against the baseline's 48 has |t| ≥ 2 with the pole's sign
    (positive at +ρ and +ρ/2, negative at −ρ);
  - it runs at all three doses.
- *The texts:*
  - n:113: "each re-encoded unsteered, projected on v, the shift against 48 unsteered baseline turns with |t| ≥ 2 in the
    pole's direction";
  - A-n1 §1.4: "The arrival hurdle's re-encoding is a forward over the emitted ids";
  - ST1:176–180: BK's "we re-encode each steered turn";
  - RC:105.
  - No text gives the forward's context, the pooling or the t-test's form. n:113 and n:49 ("BK's two hurdles on one
    batch per pole per dose") put the arrival on the +ρ/2 batch too, but no text says what a fail there does (GC14).
- *Another answer:* the arrival's one function. It needs only unsteered forwards over the recorded ids, so even after
  the run a re-computation adds no generation and no −ρ exposure. A ruling before the run is still cleaner.

## 3. The dependencies, and what Code does meanwhile

- G-VEC's run waits for this sitting's answers on G1, G3, G6 and G9, or runs on them as PINs; which is the PI's
  answer. If it runs on them as PINs, a strike among them costs at most a rebuild and a short G-VEC re-run (G1's
  capture clauses; the routing in G-VEC's spec raw, §2), before any −ρ turn exists (GC20).
- Every G-VEC alternative exists only on a PASS. If G-VEC stops at both indices (no fallback is texted), its record
  holds R at both indices and nothing else. G1, G3, G6 and G9 may then be moot or need re-asking, and G-CAL-n waits.
- G-CAL-n's build goes ahead on GC1–GC22 as PINs, declared in its BUILD entry. The rendering choice behind GC5 and GC6
  is kept in one place, so that a ruling against the chat form changes the rendering and the (v) prompts; GC7's stops
  and bans follow it (GC6).
- G-CAL-n runs only after this sitting's answers, after G-VEC's PASS is committed, and on the PI's word on keeping the
  box up through it (GC22).
- G-CAL-n's pre-declared ends, in the build:
  - a coherence or arrival fail at ±ρ is a STOP: the record and the turns, exit 2, to the seat. GC2's message said "the
    record alone"; the build writes the turns too, for the seat's read of every turn (rule 25);
  - a fail at +ρ/2 alone is a PAUSE for the seat (GC14);
  - a dose point folding into 0 is refused.
- Three more pre-run items from G-CAL-n's survey are carried, not dropped:
  - when the seat reads the turns (GC1): in LOCK-n v0.1's packet. CG:62 and BX:18 place that read before G-ANL-n, and
    n:130 places the seat's full read after VERDICTS; that timing goes on LOCK-n v0.1's list;
  - rule 21's annotation (C:338–341: a degeneracy bar at a dose rung with no unprovoked domain is "a
    pause-and-adjudicate trigger, declared as such") against n:113's STOP (GC2): on LOCK-n v0.1's list;
  - a fail at +ρ/2 alone (GC14): a PAUSE for the seat if it happens.
- G-CAL-n's survey's three departures are in G-CAL-n's spec raw (its §3, the report's last section), for the seat to
  class with the BUILD entry.

## 4. The questions for the seat

- **Q1 (G1).** Do Code's capture readings stand: the passage alone from its committed ids; every token in the mean and
  in R; the PCA centred; R the pooled RMS? The R check tests only the clauses that bear on R, not the centring or the
  tokens of the mean. If a clause is struck, which replaces it?
- **Q2 (G3).** If the site is 31, do N2's directions and R_ℓ come from the site index or from adapter index 32? If from
  32, is N2's injection index 32 too, while N1's stays the site?
- **Q3 (G6).** Is the all-contexts family of record, with the fit-only family descriptive, or the reverse?
- **Q4 (G9).** Is the 2% check |R/25.49 − 1| ≤ 0.02 on 25.49 exactly? If not, what reference and form? Does G2's
  nearer-in-R rule (an exact tie to 32) stand with it?
- **Q5 (GC3).** Is G-CAL-n's cap 80 new tokens?
- **Q6 (GC4).** Is its TEMP 0.7?
- **Q7 (GC5).** Are its 48 prompts BK's zone prompt over the 12 labels × 4 seeds, single opening turns, the same in all
  four batches? If not, which?
- **Q8 (GC6).** Does §0.7's rule-13 departure reach G-CAL-n's generations? If not, what frame does BK's prompt take,
  with which stops and bans?
- **Q9 (GC8).** Are the steered positions from the generation prompt's first token onward, or the whole turn?
- **Q10 (GC11).** Is Code's operationalization of the coherence heuristic the one, and if not, what is?
- **Q11 (GC12).** Is Code's form of the arrival hurdle the one, and if not, what is?
