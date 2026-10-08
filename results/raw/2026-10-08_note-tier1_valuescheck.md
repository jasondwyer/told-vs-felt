# AUDIT-note-release v1.2: Tier 1 and N12 values-check record (all rounds)

- Code stamp: 2026-10-08 13:16:02 UTC (date -u). Block sha256 8cd8a9ac...3841 (committed at bbc9ffe).
- What this is: a process record. For every Tier-1 item and every N12 part, each adversarial checker pass is listed: claims checked, whether the item's script regenerated its raw identically, the redaction result, each finding (severity, verdict, claim condensed) and the next fixer's disposition.
- Source: the local workflow run journals and results of this session, which are not in the repo. Runs: wf_410a595b-4ef (Tier 1 build/verify/fix/verify2), wf_720539ca-6b7 (N12 scan/review/verify/fix), wf_ea086056-efc (N12 round 2), wf_a9bc1c2d-168 (Tier 1 round 2/3), wf_f1040ac8-1e0 (round 4). The item raws themselves carry the authoritative Values-check sections; this file indexes them across rounds.
- Severity: substantive means the finding would change a number, a status, a STOP/pass outcome or a sentence of the note; minor means wording, locators or precision.

## N2vi

### Pass 1 (verify): 110 claims checked; regenerates identically: True; redaction clean: n/a; findings 14 (3 substantive)
- [substantive] incomplete: Each figure has a status from the vocabulary reproduced | log-only | not found | discrepant | computed-new (task rule 4; N1 ledger input, block :22-23)
- [substantive] wrong: Note 3: the design seat's N2(v) instruct arithmetic (d' ~ +0.15, p ~ .5) 'cannot be checked here'. Builder summary pi_item: the instruct-FPR correction 'changes ... the design seat's N2(v) instruct arithmetic'.
- [substantive] wrong: Source prompt format: 'bare base-model prompt for olmo_base; chat template for the post-trained stages' (section 7 table and JSON decoding.prompt_format); builder summary: 'Prompts are bare for base'
- [minor] imprecise: Paper v1 prompt_format: 'not stated'
- [minor] incomplete: Note 2 lists the pre-data sizing figures that depend on the instruct FPR: the power table RESULTS.md@bbc9ffe:7356-7361 and joint power 0.9642
- [minor] unsupported: Joint power 0.9642 'presumably used the section 0.2 table, i.e. instruct at 0.3%'; not recomputed
- [minor] imprecise: Note 5: 'The record's L_M = 44 rests on the code rule (ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:60-68)'
- [minor] incomplete: Version table v4 row: 'D.1 at L=19/22'; note 1: the cited 'Fig 21' structure exists only in v1
- [minor] imprecise: v2/v4/v5: 'Table 3 (official checkpoints, L=25, alpha=4): TPR-FPR SFT -11.5 +/- 2.4, DPO +9.8 +/- 0.5'; builder summary: 'Their Table 3 gives only official SFT/DPO TPR-FPR'
- [minor] imprecise: Answer 3: 'Neither [table nor figure] ... Nothing was digitized.'
- [minor] imprecise: Note 7: ADDENDUM :274 and RESULTS.md@bbc9ffe:7181 'say the section 0.2 table is "exact against paper"'; '7 of its 8 rate cells are exact'
- [minor] incomplete: The note's sentence (block :35, 'the note now carries 0.001 / 0.149 / 0.029 / 0.009')
- [minor] imprecise: Answer 4 locator: ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:213-214 for 'the aggregate is diluted by past-optimum strengths'
- [minor] incomplete: Block :35 'If the source states per-stage TPR in text, quote it'; the raw quotes only the SFT sentence and paraphrases base, DPO and instruct

### Fix 1: 15 dispositions: fixed 15

### Pass 2 (verify2): 125 claims checked; regenerates identically: True; redaction clean: n/a; findings 10 (2 substantive)
- [substantive] incomplete: Section 0 row 17 and section 12: the [g3-A] joint power 0.9642 is 'discrepant' (residual -0.0003, cause not identified) and 'not a STOP: no analyzer of record computes that figure, and recomputing it needed no code change.'
- [substantive] incomplete: Section 7, row 18 and note 3: the design seat's source-point d'/p are 'confirmed' at 800/80 'per (layer, alpha) configuration, as the block assumes'; 'the correction does not change the seat's instruct arithmetic'; 'N2(v)'s choice of n matters more than ...
- [minor] incomplete: Section 6(a) reports 'single pair base > dpo' 0.98296 against the record's 0.9825, residual -0.0005, and adopts the record's label without testing it.
- [minor] overclaim: Row 8 note: 'the record's 0.003 is the v1 instruct introspection rate; transcription, a referent note, not a STOP' (same unhedged wording in the JSON figures[7].note).
- [minor] overclaim: Section 5: 'The README is therefore not evidence of the producing configuration; the v1 caption is.'
- [minor] imprecise: Section 3 says the three non-SFT stages are 'paraphrased' and the raw 'keeps to one short quotation from the source'.
- [minor] imprecise: Section 2 heading ':7345-7348 -- the source's text, paraphrased in the record'; v1 row: 'Section 3.3 points to Appendix C.'
- [minor] incomplete: Section 0 'record locator(s)' for the source values (rows 1-9).
- [minor] imprecise: Row 12: '~800 injected / ~80 control per (layer, alpha) configuration' is 'not found'.
- [minor] imprecise: Section 2: "'clopper' is its Clopper-Pearson import and the criterion's interval calls on data."

### Fix 2: 11 dispositions: disclosed 1, fixed 10
- disclosed: Cross-item and housekeeping disclosures: (a) The N2vi JSON keeps every key the N2 script reads (stages.*, grid.n_scenarios_computed_new, decoding.*, and the 800/80 source-point rows, unchanged apart from two added keys); a tool check ...

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 6 (2 substantive)
- [substantive] incomplete: a block :23 consequence is missing: Section 0 row 17 and section 12: the retired criterion's Instruct power is 'log-only' 'at the record's rates', and the block :23 conditions cover only the instruct FPR 0.3% and +0.6 pp themselves.
- [substantive] inconsistent with the block's rule 2 and with the raw's ...: Section 0 row 16: 'lineage: four HF repos' has status 'reproduced'.
- [minor] stale on disk, and the cross-reference is circular: Section 7 'Consistency with the N2 raw' records N2's ROC JSON sha256 2b036edd... 'at this run'; JSON source_points_dprime_computed_new.n2_consistency_check.sha256 carries the same value.
- [minor] imprecise referent: Section 5 and note 4: data/configs/b2_concepts.json's provenance.concepts_source 'cites the source's DEFAULT_TEST_CONCEPTS, '50 words from the paper''.
- [minor] incomplete locator list: Note 2, item (2): the joint-power locator list is 'ADDENDUM :147-148; RESULTS :7180, :7189-7194, :7268-7269; ... also :7173, :7251'.
- [minor] incomplete: a derived figure is not covered: Section 12 condition 4 cuts '~800 injected / ~80 control per configuration as the source's n'.

### Fix 3: 6 dispositions: fixed 6

### Pass 4 (verify4): n/a claims checked; regenerates identically: True; redaction clean: True; findings 2 (1 substantive)
- [substantive] incomplete: Section 6(b): 'The record's conclusion (RESULTS.md@bbc9ffe:7363, "Instruct is the binding constraint and it is not close") is unchanged.' The same view runs through note 2(1) and section 12 condition 3, whose list of instruct-FPR-derived figures stops at ...
- [minor] incomplete: Row 19 (retired criterion's Instruct power) gives its locators as ADDENDUM-g3-b2r-v1.2.md@bbc9ffe:52-53 and RESULTS.md@bbc9ffe:7330-7331, :7354-7361. Note 2(1) gives the same list.

### Fix 4: 2 dispositions: fixed 2

### Check 5: applied correctly 2/2; regenerates identically: True; redaction clean: True; new problems 1
- **open (minor, not applied)**: The round-4 script docstring (scripts/audit_note_N2vi.py line 50) and the own_cp_fast docstring (line 678) say the record's binom_pmf 'raises OverflowError from n = 1030'. That is imprecise. binom_pmf raises only at k where comb(n, k) exceeds the float ... Proposed fix: In both docstrings, change "the record's own binom_pmf raises OverflowError from n = 1030" to "the record's clopper_pearson raises OverflowError from n = 1030 (for k >= 1: its binom_sf_inclusive ...

## N2

### Pass 1 (verify): 165 claims checked; regenerates identically: True; redaction clean: n/a; findings 10 (3 substantive)
- [substantive] incomplete: 5(a), 5(d) and the ROC JSON 'theirs' points: the source's rates are labelled 'source aggregate (20 configurations pooled)' and analysed at 'n = ASSUMPTION 800/80 per configuration'; the seat's theirs DPO d' ~ +0.6 (p ~ .11) and instruct d' ~ +0.15 (p ~ .5) ...
- [substantive] overclaim: 2(c) verdict: '12 parameters differ; 6 of them can change what a control trial yields (temperature, max new tokens, per-trial seed, ...)'. 2(d), the STOP's suspected_cause and referent note 10: 'Temperature, the 60/100-token cap and the seeds cannot be ...
- [substantive] wrong: Table 0 rows 11 and 12 (B2 temperature 0.0, B2 max new tokens 60) and row 27 (scorer of record for the greedy row = v1) have status 'not found'; row 10 (top-p/top-k none) has status 'not found'.
- [minor] wrong: Referent note 4 / ROC JSON notes[3]: 'Block :34 g3b: [g3-B] is the dose-qualification ladder ... it contributes no F2 point.' 5(a) bullet presents g3b in the same way.
- [minor] unsupported: 5(c): 'If 'two-sided 97.5%' is read literally (a 97.5% two-sided interval), its upper limit is the one-sided 98.75% bound, 0.0969.'
- [minor] overclaim: Row 43 note, 5(e) and referent note 8: the exploration controls' replay of section 1 'contradicts' the addendum's 'fresh declared seed'; ADDENDUM 'declares section 3's seed fresh; the run reused section 1's'.
- [minor] incomplete: 2(b): 'the record reports this cell as hit 4/4, FA 0/1, +1.000 and as a scorer defect (RESULTS.md@bbc9ffe:7782)'; F2/ROC greedy register SFT point 2/2, 0/1.
- [minor] imprecise: Row 16: 'greedy run: zero detection claims at every stage (register arm)' status 'discrepant'; ROC JSON greedy register notes: 'a defective scorer for it, not a detection point'.
- [minor] imprecise: Section 10: '(i) reproduces: yes for the four FPRs, the 2.5-point distance (our operand; theirs is log-only) and our decoding fields'.
- [minor] incomplete: Table 0 (the per-figure ledger for N1) covers the block's N2 figures.

### Fix 1: 11 dispositions: disclosed 1, fixed 10
- disclosed: Checker note: paper_analysis.ipynb shows as modified.: Not N2's: the script never opens it, and the git status at the start of this session already listed it as modified. Left untouched. The script does not check it, so the raw stays deterministic.

### Pass 2 (verify2): 152 claims checked; regenerates identically: True; redaction clean: n/a; findings 9 (1 substantive)
- [substantive] overclaim: Ledger row 32: '2 of 42 affirm-scored control trials' = '2 of 42', status reproduced. Section 4 adds that 'The relabel is a hand correction of two trials ... it changes no reading', and base FPR 0.431 is carried without qualification.
- [minor] incomplete: 5(e) and section 4: the exploration controls replay section 1, and FLAG-3 is reported for section 1 only (15/85). The exploration SFT point is given only uncorrected (FA 9/44, sens +0.0955, d' +0.292, Fisher p 0.2246).
- [minor] imprecise: Section 11 item 2: 'Round trip decode(encode(text)) == text here: base 96/96 ...; the checker reported 94/96 at base under its method, which this item did not replicate and does not explain.'
- [minor] unsupported: Row 13: 'decoding source: T 1.0, top-p 1.0, top-k 50, max 100, seed 42 global', status log-only, source results/raw/2026-10-08_note-N2vi-source.json:decoding. The 1(c) source column has no record locator. The status legend (raw :18 and :110) defines ...
- [minor] incomplete: Row 10 / section 1(c): our top-p / top-k 'not found: code-fixed, no artifact field, no log line'; the log search found nothing relevant.
- [minor] incomplete: 2(c): '12 parameters differ'; 'the full prompt for trial n is byte-identical for n = 1..96'.
- [minor] imprecise: Row 21: '2 undecidable trial(s) carry an affirm word inside a denial'.
- [minor] imprecise: Section 10: '(i): ... reproduce; the 2.5-point distance is log-only ...; our top-p/top-k ... not found'. '(iv) single scorer of record: yes for the B2-r figures (v2); no for the full N2 figure set'.
- [minor] imprecise: Section 0 ledger column header 'figure (as the block writes it)'.

### Fix 2: 11 dispositions: disclosed 2, fixed 9
- disclosed: Directive: keep the N2(ii) STOP on link 4's ROC paragraph.: Kept, since the block's fail text at :36 licenses it. The protocol now differs on 13 parameters, 6 of which touch the control FPR. Post-hoc emulations (cross-scoring, the trial-number restriction ...
- disclosed: Concurrency: the N2vi JSON, another item's file that this script only reads, was regenerated by a concurrent session during this work.: Its hash went 1eb31bd5 -> c0911e21 -> c98b2859 (the last change at 09:39 UTC). I re-ran after the last change: the ROC JSON equals the previous run apart from the recorded N2vi hash, and the ...

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 6 (0 substantive)
- [minor] incomplete: Section 1(a) disclosure, section 4 ('The record ruled that negation-safety must cover ... belief verbs, conditionals, futures, ability modals (RESULTS.md@bbc9ffe:6923-6931). At base, 8 of the 25 affirm verdicts are that class') and PI item 7 rest the 8 ...
- [minor] imprecise: 5(e) and ledger row 57: 'two are degenerate texts -- trial 14 (Satellites) ... trial 35 (Illusions)'; 'hits 14 and 35 are degenerate texts (read in full)'.
- [minor] incomplete: The base disclosure is carried, per the fixer, into ledger row 4, 1(a), section 4, the ROC base point, the (iv) verdict and PI item 7. Base v2 counts are still quoted without it in the 2(d) cut table, the trial-number restriction, ledger rows 22-23, ...
- [minor] imprecise: Section 0 is headed 'Per-figure status (for N1's ledger)'. Row 33 ('single scorer across the N2 figure set') and row 21 ('greedy run: protocol otherwise identical') carry status 'discrepant' and are not transcription errors.
- [minor] imprecise: 1(c) source column, trials per stage: 'per (layer, alpha, concept) cell: 100 ... injected, 10 ... control (code defaults); n of concepts not stated [log-only: ... RESULTS.md@bbc9ffe:7435-7436]'.
- [minor] imprecise: Section 11, line 482: 'Row numbers inside each pass's findings are that pass's ledger numbering; where pass 2 moved a row, its current number is given beside it.'

### Pass 4 (verify4): not run

### Fix 4: 7 dispositions: disclosed 1, fixed 6
- disclosed: Cross-item: the N2vi JSON was finalized (sha256 c98b2859... changed to 03542a19...): Re-ran against the final N2vi JSON. The header and ROC n2vi_json now record 03542a19dc726fcd...1bd. Compared old and new N2vi JSON: record_commit, block, stages, decoding and all 20 source_points ...

### Check 5: applied correctly 7/7; regenerates identically: True; redaction clean: True; new problems 3
- **open (substantive, not applied)**: Round 4 breaks the script's documented tokenizer-absent path. If the local OLMo tokenizer.json (outside the record) or the tokenizers library is missing, scripts/audit_note_N2.py now crashes and writes nothing. That makes every N2 figure unreproducible on ... Proposed fix: Make the round-4 code conditional on emu['run']. Use len(figures) == (57 if emu['run'] else 56) at :2679. Compute r_cut only when the row exists at :2967. When the emulation did not run, item 3's ...
- **open (minor, not applied)**: The round-4 rewrite of the docstring's working-tree sentence still lists the working-tree inputs incompletely. The header labels the N2vi raw as a round-4 input, but the '97.5' search has read it since pass 2. PREPRINT-v1_0-draft.md is also read from the ... Proposed fix: In the docstring, write 'The working-tree reads are the N2(vi) item's JSON and raw and PREPRINT-v1_0-draft.md (the raw and the preprint also for the pass-2 '97.5' substring search), all untracked ...
- **open (minor, not applied)**: The round-4 notes on ledger rows 22 and 23 give the disclosure for base only. The SFT values in the same rows also contain section 4's FLAG-3/ambiguous trials, and only 2(d) says so. Proposed fix: Append to row 22's note: '; sft: 3 of 17 ([5, 16, 76]) are section 4's FLAG-3/ambiguous trials (without them 14/85, p 0.0237; 2(d))'. Append to row 23's note: '; sft's [12, 16, 42] include ...

## N3

### Pass 1 (verify): 278 claims checked; regenerates identically: True; redaction clean: n/a; findings 10 (0 substantive)
- [minor] imprecise: ib-1 status 'reproduced' for F1's shuffle-95 null 'approx .57-.59 across layers', while 3g's 'median |delta| <= .10' is 'discrepant' for an overrun of the same kind (.1027 vs .10)
- [minor] incomplete: Section 9 'STOPs: None' stands in for the item's pass verdict
- [minor] unsupported: 'Parts (ii)-(iv) ... are in results/raw/2026-10-08_note-N3-echo-compute.md' (header Scope line; section 10 item 4; JSON pi_items[3])
- [minor] rule-violation: Section 6: the Stage A registered target reads 0.415-0.505 at L49-L63, 'the Stage A entry's .42-.51 above 48'
- [minor] incomplete: Section 6: 'post-hoc #2 (label_a pole, n = 24) 0.427-0.540'
- [minor] rule-violation: 3d: b_labelpole_M1M2 rows are 'bit-identical to Stage C's read rows, C entry'
- [minor] imprecise: 3f note: "'sign flips' is the note's word"
- [minor] incomplete: 3j: k1_analyze.py was not run because it imports the valence_core chain
- [minor] incomplete: (v) summary: 'label_a random 1.000 at L51-L52, 0.826-0.897 at L54-L63'
- [minor] imprecise: Masks definition: 'M3 / M4 the random direction with M1's / M2's sign pattern (scripts/recon_echo.py@bbc9ffe:155)'

### Fix 1: 12 dispositions: fixed 12

### Pass 2 (verify2): 1300 claims checked; regenerates identically: True; redaction clean: n/a; findings 8 (2 substantive)
- [substantive] wrong: 3i-a / section 3f-3i: 'COMPUTED-NEW here: the record tables no flip or |delta| figure on its random masks (the k Stage 1 entry says so: RESULTS.md@bbc9ffe:2638)'; row note: 'the record never tabled flips or |delta| on the random masks; only the SIGNED ...
- [substantive] overclaim: ib-1: 'shuffle-95 null ≈ .57–.59 across layers' is 'discrepant (transcription)'; section 4 item 1: 'the band as quoted holds only if F1 omits L48, L49 and L50'; section 10 item 4: ''.57–.59' holds on L51-L63 only; over any domain that includes L48, L49 or ...
- [minor] incomplete: Referent notes 1, 3, 4 and PI items 1-3 present the 3a domain correction (L50-L63; L49 .695), the 3g overrun (median .1027 > .10) and the 3h scoping (mixed B3x/B4x, toward the first ROUND's label; B1x/B2x +.008/-.002) as the audit's own findings
- [minor] incomplete: 3f: '0-3 of 102 pick flips over the 12 axis masks ... these are restricted-argmax PICK flips (state pick != shadow pick) per session, the record's pi_d; 'sign flips' is the block's wording'
- [minor] imprecise: 3j: 'The reason that binds: scripts/k1_analyze.py has no read-only mode ... --run ... refits every probe and writes data/k/<out-name> ... The block's rule 1 forbids that'
- [minor] incomplete: Section 2: stored AUC at L40/L44/L48 is exactly 0.5 in Stage B's 6 paired families and not in its single-round families (0/8)
- [minor] incomplete: v-1: 'no quoted value to check: block line 48 asks for a report; every value printed from the stored fields' (status reproduced)
- [minor] imprecise: JSON pass: {"N3_i_and_i_b": "met", ...}

### Fix 2: 11 dispositions: fixed 11

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 5 (0 substantive)
- [minor] incomplete (provenance): Section 11 says it reads N3c's JSON (provenance line, md:422; Scope line, md:12; run-dependent-lines note, md:11; script docstring). It also quotes N3c's statuses for the F1 band and for '≈ .58' (md:437-438, md:522).
- [minor] incomplete (domain omitted): Section 11's proposed short-form line: '... (MLP AUC .59–.97, RBF kernel .60–.76, L49–L63, ...); post hoc, ... linearly readable within each menu order (.958–.996) but not pooled.' The R1 check on md:475 reads 'within-subgroup linear min 0.9576 -> 0.958, ...
- [minor] imprecise (referent scope): PI item 4 (md:413), the ib-1 correction (md:381) and section 11's F1-band row (md:438) present '.57–.60' as the record's own prose for the band pooled over the three C1 families ('as the record's own prose writes it, RESULTS.md@bbc9ffe:4402').
- [minor] imprecise (record domain); status unaffected: Row 3i-a1 and the random-masks heading (md:176, md:375) cite RESULTS.md@bbc9ffe:2943-2944 for 'the largest per-family max |Δ|, M5x .2012' as a random-mask figure, checked over the 12 random masks.
- [minor] imprecise (draft contradicts the advice printed beside it): Section 11's proposed exact and short lines open with the MLP level range ('.5950–.9707' / '.59–.97') and the RBF range ('.6048–.7575'). The bullets right after them quote N3c's advice to 'quote the exceedance, or the RBF figure with its grid caveat, ...

### Pass 4 (verify4): not run

### Fix 4: 5 dispositions: fixed 5

### Check 5: applied correctly 5/5; regenerates identically: True; redaction clean: True; new problems 5
- **open (minor, not applied)**: The R4-2 fix added a fourth string quoted from N3c's raw .md, "N3c's raw .md, line 152: 'no null (point estimates only)'". It appears in section 11 (a)'s 'in any linear functional' row (md:443) and in R4-2's detail. Every provenance statement R4-1 added ... Proposed fix: Add the line-152 string to md_strings so the JSON search counts it. Say 'four strings' (two status tags, the advice sentence, the subgroup 'no null' clause) in the Scope line, run-dependent note, ...
- **open (minor, not applied)**: own4-1's detail prints a line number from N3c's .md that changes between runs ('Quoted verbatim from N3c's .md (line 207)', computed from link3.n3c_raw_lines). The run-dependent-lines note does not list it: own4-2 lists only round 4's R4-1, R4-2 and R4-5. Proposed fix: Add own4-1 to the run-dependent-lines note's list of section 12 rows.
- **open (minor, not applied)**: Reading A of the record's R / M++ domain says 'M++ = +d on both blocks (PROPOSAL-k-echo-channel.md@bbc9ffe:218) ... i.e. the 12 random masks and the same-pole axis masks M5/M6'. M6 is −d on every round, so the cited line maps to M5 only. Proposed fix: Either cite PROPOSAL-k-echo-channel.md@bbc9ffe:335 ('the same-pole leak arm') as the basis for including M6, or write 'M5 (+d on both blocks; M6, its −d mirror, is included as the recon's other ...
- **open (minor, not applied)**: The new 'record's max clause' paragraph in section 3f-3i cites RESULTS.md@bbc9ffe:2942-2944 for a quote that starts on line 2941. Proposed fix: Cite RESULTS.md@bbc9ffe:2941-2944 for that paragraph's quote, or start the quote at 'not the R / M++ arms'.
- **open (minor, not applied)**: In the fallback runs (N3c's .md absent or empty), section 12's round-4 rows print as if a check had run. Proposed fix: Guard the R4-1 and own4-1 detail strings on the .md having been read; print 'not run: N3c's .md not read' instead of '0 of the 0' and 'line None'.

## N3c

### Pass 1 (verify): 166 claims checked; regenerates identically: False; redaction clean: n/a; findings 11 (0 substantive)
- [minor] rule-violation: Header L10: 'Non-deterministic lines: the stamp, HEAD ... and lines tagged [wall-clock]. Everything else regenerates byte-identically.' Builder summary also lists a 'N3(ii) extended only if cheap (cost)' figure with status computed-new (~11.8 null AUC/s, ...
- [minor] incomplete: The raw reports STEP 0, the (ii) nulls, the (iii) MLP/RBF results, (iv) L45-L47 and the POST-HOC values without the status vocabulary.
- [minor] incomplete: (iii) MLP at the read position: L49-L63 AUC .5950-.9707 (L51-L61 .7808-.9707; peak .9707 at L53).
- [minor] incomplete: (iii) RBF at the read position: L49-L63 AUC .6048-.7575; 'lambda ... chosen per label column by grouped 5-fold inner CV'; observed lambda 1e-4 at every informative layer.
- [minor] overclaim: POST-HOC reading: 'an XOR across the two subgroups that no single linear functional can read pooled'.
- [minor] rule-violation: 'POST-HOC, descriptive (CLAUDE.md ledger 11: labeled post-hoc; licenses pre-registrations, never verdicts ...)'
- [minor] incomplete: (iv) L45-L47 (new layers): AUC .5000; 200-draw null mean .5040/.4956/.5028; 95th .5726/.5681/.5966; p .5572/.4527/.4826.
- [minor] imprecise: Builder summary: F1 / N3(i-b) 'shuffle-95 null at ~.57-.59 across layers': status 'reproduced'.
- [minor] imprecise: Builder summary: binding at the second label '.81-.96' (cross-check): 'reproduced .8208-.9642 at L51-L61 (.8077 at L63)'. Raw L229: 'label_b L51-L61 0.8208-0.9642'.
- [minor] unsupported: (iv) reading: 'it holds at every informative layer of the sweep, adjacent layers agree, and none is distinguishable from its shuffled-label null'.
- [minor] incomplete: Raw scope: N3 (ii)-(iv) written to results/raw/2026-10-08_note-N3-echo-compute.md; '(the sibling item reports these from the JSON)'.

### Fix 1: 12 dispositions: fixed 12

### Pass 2 (verify2): 178 claims checked; regenerates identically: True; redaction clean: n/a; findings 4 (0 substantive)
- [minor] imprecise: 'MLP early stopping (observed fits, L49-L63): median best epoch per layer L49 92, L50 62, L51 582, L52 1000, L53 1000, L54 234, L55 172, L56 71, L57 99, L58 65, L59 202, L60 127, L61 128, L62 64, L63 35'
- [minor] incomplete: Outcome line: 'a nonlinear read exceeds its own shuffled-label 95th percentile at the read position at MLP [49..63], RBF [49..63] ... The block's rule for this case (:50) keeps link 3's sentence and adds one line'
- [minor] incomplete: Outcome line's handoff: link 3's sentence ('in any linear functional', block :50) stays and the design seat writes the nonlinear line
- [minor] imprecise: Script docstring: 'Seeds fixed; deterministic apart from the stamp, HEAD and the lines tagged [wall-clock].'

### Fix 2: 5 dispositions: disclosed 1, fixed 4
- disclosed: Method: how the raw was regenerated without the 75-90 min compute (declared in the raw): I moved the report code into render(o, rt), which reads only the JSON dict. The compute path now writes the JSON, then renders the raw from that same JSON text. --render-only renders the raw from ...

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 2 (0 substantive)
- [minor] imprecise: Raw line 10 (the 'Rendered by --render-only' header) says 'every figure below is read from that JSON by render()'. Its list of inputs 'Evaluated at this render, not read from the JSON' names only the Block line's pin hash, the BLAS name and the ...
- [minor] imprecise (count only): Raw line 336: 'The diff from that pre-edit render to round 2's raw is exactly the round-2 edits: ... the outcome line's two added sentences ...'

### Pass 4 (verify4): not run

### Fix 4: 5 dispositions: disclosed 2, fixed 3
- disclosed: Code's own addition (b), not a checker finding: the (iii) disclosure (line 176) stopped at round 2.: Added one sentence. It records round 3 (pass 3's full re-run of round 2's script plus its own re-implementations of the spec MLP, the MLP and RBF nulls and the POST-HOC fits; the files are in ...
- disclosed: Method check: the raw was regenerated without re-running any fit.: Regenerated with `--render-only` (absolute script path, default args), so the JSON is unchanged (d431a2a5...a6f3) and no computed number changed. A line and word diff against round 2's raw shows ...

### Check 5: applied correctly 5/5; regenerates identically: True; redaction clean: True; new problems 0

## N4

### Pass 1 (verify): 104 claims checked; regenerates identically: True; redaction clean: n/a; findings 14 (5 substantive)
- [substantive] incomplete: (iv) 'Which cells generated on the cached path (Qwen)' lists e2a as the full run plus smoke2/smoke3, and the README paragraph and scope sentence follow that list.
- [substantive] overclaim: Figures row 'cells generated on the cached path' has status 'reproduced'.
- [substantive] overclaim: Figures row 'choice reads unaffected' has status 'reproduced' (source valence_core/readout.py@bbc9ffe:90-120 and data/e2a/g3prime_kl.jsonl).
- [substantive] rule-violation: STOPs: 'None. Every N4(i) figure reproduces from committed artifacts...'. Yet the (i) figures table carries a 'discrepant' row ('every arm integer under share − ½, none under (approach − avoid)/n'), and the raw has no explicit pass line.
- [substantive] incomplete: (ii) MDE at the sham-envelope criterion: E1 δ* = +0.1911 (n = 101) and +0.1909 (n = 102); joint ≈ +0.192; the Reading sentence says '(E1) it needs δ = +0.191'.
- [minor] wrong: e2a full run: every launch prints 'round generation path (g1r, mechanical): cached' at results/raw/2026-08-09_e2a_full.txt@bbc9ffe lines [2, 27, 54, 205].
- [minor] wrong: Rule-26 recheck locator: results/raw/2026-08-18_rule26_recheck_choiceread.txt@bbc9ffe:23-26.
- [minor] imprecise: 'Δ_first is half the difference...' is not in the preprint; the identity is a within-arm mechanism gloss; 'habit.py labels the decomposition post-hoc algebra (rule 11)'.
- [minor] overclaim: '54 of 101 valid sessions' and 'half the difference ...' are 'not in the preprint'; the block's quotation likely comes from RESEARCH-NOTE v0.2.
- [minor] imprecise: README paragraph: 'A later T-step check at the e2a/e2b dose ... found 23 of 24 rounds token-identical'; 'two samplers that agree in distribution'; 'each is a separate, uncached forward pass over the transcript text ... checked by an identical re-forward at ...
- [minor] unsupported: (iv) operational meaning: the g1 gate compared distributions 'at the first response position of 16 session-shaped prefixes per pole ... against 1e-3'; (iii) 'against a declared bar of 1e-6 (KL = max of the two directions; ...
- [minor] incomplete: Note 7 and the (iv) note on the g3′ counterfactual: 'the record's own framing of g3 is a live cached-SESSION read (archive:1189-1190) ... Reported, not adjudicated.'
- [minor] incomplete: Figures table covers every figure the block lists for N4.
- [minor] imprecise: Prose values in the raw are printed by the script from computed variables.

### Fix 1: 14 dispositions: fixed 14

### Pass 2 (verify2): 131 claims checked; regenerates identically: True; redaction clean: n/a; findings 10 (3 substantive)
- [substantive] wrong: Referent note 10 and the (iv)/(iii) framing: 'The block's cards 9 and 10 cannot be checked here; their source (presumably FIGURE-REVIEW-2026-10-06.md) is not on this machine.' Note 9 also calls the 270/1,894 boundary collapse 'Beyond the block's ask', and ...
- [substantive] wrong: (iv): the gate does not license sampled-token identity 'not even at the first token, where temperature sampling ... can resolve a near-tie differently ... (the one divergence at 0.10 below is at position 1)'. README paragraph: 'found 23 of 24 rounds ...
- [substantive] imprecise: Figures row 'approach-probability interval ≈ [.44, .64]' carries status computed-new. The (i) pass tally {'reproduced': 11, 'discrepant': 2, 'computed-new': 2} counts it as computed-new.
- [minor] rule-violation: (iv) and README: 'AUC by k {'1': 0.645, '2': 0.759}', 'AUC by k {'1': 0.633, '2': 0.759}', 'the readability AUC 0.759', 'judge 14/32'.
- [minor] imprecise: 'the e2b H2 smoke produced bit-identical transcripts on both kernel paths over 2 sessions (RESULTS.md@bbc9ffe:10410, '2 sessions, smoke only'; log-only)'
- [minor] imprecise: 'Control-arm sizes 37/23/22 ... Verdict entry: archive/RESULTS-cycles3-4.md@bbc9ffe:666.'
- [minor] imprecise: 'sham rounds carry no state (vanilla cached), reward/random rounds carry ±α at L48 (archive/RESULTS-cycles3-4.md@bbc9ffe:1246)'
- [minor] incomplete: Referent note 2: 'PREPRINT-v1_1-draft.md ... and RESEARCH-NOTE v0.2 are both absent (results/raw/2026-10-08_note-preflight.md@bbc9ffe:20)'. Also: the block's quotations 'must come from a text not on this machine'.
- [minor] imprecise: Figures row "preprint '54 of 101 valid sessions'" carries status reproduced.
- [minor] incomplete: 'Not cached' list: d2, d3, k1, format_recon_F0/F1/F2 (round_path_cached false).

### Fix 2: 11 dispositions: fixed 11

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 5 (0 substantive)
- [minor] wrong (stale numbering): Values-check pass-2 row 1 says: 'Note 10 is rewritten: the block's (card 9) on (iv) names card 8's subject ... Note 9 now calls the boundary collapse the handoffs' card 9'.
- [minor] overstated (an inference stated as fact; one part not ...: README draft: 'the one divergence beginning at the second sampled token (0-based index 1, the first content token after a whitespace token both paths shared)'. Referent note 7: 'the first sampled token (index 0, whitespace) agreed', and the record's 'at ...
- [minor] imprecise: Locators added in round 2: 'RESULTS.md@bbc9ffe:5211: (8) the cached-generation / T-step methods disclosure' (note 11), and 'RESULTS.md@bbc9ffe:3086 reads "card 10" occurs only in the proposal; the cards on record stop at 8' (note 11).
- [minor] mixed-status row (consistency): Figures row 'approach-probability interval ≈ [.44, .64] with its method (block: Wilson on 55/102 gives it)' has the single status 'reproduced'.
- [minor] imprecise (pre-existing; not raised in passes 1-2): (iii): 'The 8 smoke3 sessions are byte-identical to the full-run sessions with the same (arm, session): 8/8'.

### Pass 4 (verify4): not run

### Fix 4: 5 dispositions: fixed 5

### Check 5: applied correctly 5/5; regenerates identically: True; redaction clean: True; new problems 1
- **open (minor, not applied)**: The new section is titled 'Values-check (round 4, adversarial checker; ...)' and its intro says 'The round-4 checker read ...'. The two sections above it are 'pass 1' and 'pass 2', and the raw has no pass 3 or round 3, so the numbering skips. The checker ... Proposed fix: Title the section 'Values-check (pass 3, adversarial checker; round-4 dispositions by the fixer)', or keep the title and add one clause to the intro: 'the third checker pass (the workflow's ...

## N11

### Pass 1 (verify): 62 claims checked; regenerates identically: False; redaction clean: n/a; findings 13 (0 substantive)
- [minor] overclaim: Raw line 11: 'To regenerate this raw byte-for-byte apart from the stamp line, pass --ref bbc9ffe72fb8...'
- [minor] wrong: Raw line 364: README.md:40 'FINDINGS*.md' glob: '...newest tracked by name: FINDINGS.md'
- [minor] wrong: Raw line 342: 'README.md at --ref: 74 line(s)'
- [minor] imprecise: Raw line 13: 'Every git command that touches the clone runs with GIT_CONFIG_GLOBAL=/dev/null, GIT_CONFIG_NOSYSTEM=1, LC_ALL=C, and no other GIT_* variables.'
- [minor] incomplete: Verdict conjunct: 'suite prints N/N with N printed, zero [FAIL], exit 0' (pass condition with N in place of 103)
- [minor] rule-violation: Verdict conjuncts 'no warning/error in clone or checkout output', 'tree clean after checkout' and 'tracked notebooks hash to their committed blobs' are part of the N11 PASS, and failing any of them prints 'STOP on the release'
- [minor] unsupported: Raw referent note 1: 'The pass condition applied here is \'N/N with N printed\'.' Builder summary: 'the routed pass condition is \'N/N with N printed\''
- [minor] overclaim: Raw final line: 'N11: PASS -- the suite prints 154/154 from a fresh clone at bbc9ffe...'
- [minor] unsupported: Raw referent note 5: 'The third-party import list in (2) is what a reader\'s own interpreter needs.'
- [minor] incomplete: Raw sections (2) and (4) describe the suite's temp-file use but end with 'Scratch TMPDIR and hook report deleted: True'
- [minor] imprecise: Raw line 382 and note 3: 'RESEARCH-NOTE-v0_2-draft.md is NOT present on this machine (RESEARCH-NOTE* at root or in archive/: none)'
- [minor] incomplete: Builder summary referent note: os.walk structural scans (analysis.py@bbc9ffe:1192-1201 and :809-821) read untracked .py files in a working tree, so a laptop site check and a clone can differ
- [minor] imprecise: Script default --workroot = SCRATCH (the builder's own scratch, scratchpad/N11); stale clone-<sha12>/tmp-<sha12> directories there are rmtree'd at start

### Fix 1: 14 dispositions: disclosed 1, fixed 13
- disclosed: Code's own corrections in this pass (not checker findings): (i) git's delayed progress meter ('Updating files: NN%') appeared in clone stderr on one run, which broke determinism. Meter lines are now dropped from the display by a fixed regex; the warning ...

### Pass 2 (verify2): 88 claims checked; regenerates identically: True; redaction clean: n/a; findings 9 (0 substantive)
- [minor] overclaim: Note 6: 'An earlier record entry needed more: RESULTS.md@bbc9ffe:11593-11594 records the earlier 103/103 after pip install numpy scipy into a bare container'
- [minor] incomplete: Note 1 treats 154/154 as the right referent for the block's 103/103 and passes on 'N/N with N stated'
- [minor] rule-violation: Statuses of the raw's figures (154/154 reproduced, 103/103 discrepant, the import list etc. computed-new)
- [minor] imprecise: 'The clone's own .git/config (written by git clone; the only config in effect besides the repository's .gitattributes)'
- [minor] incomplete: (b) Plain run is 'the README's command plus -E -s'; the block's command is `python -m valence_core.regression.analysis`
- [minor] imprecise: OUTSIDE = 0, and the class 'interpreter: stdlib read 77 77'
- [minor] imprecise: Heading 'Referent notes (block §0 preamble: a wrong referent is a note to fix, not a STOP)'
- [minor] incomplete: 'N11: PASS at bbc9ffe..., provisional -- pre-tag ... and cloned from file://..., not from the published remote'
- [minor] incomplete: README.md:60 'valence_core.regression.oracle' -> 'module path -> valence_core/regression/oracle.py (tracked)', counted among the 30 resolving references

### Fix 2: 9 dispositions: fixed 9

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 4 (0 substantive)
- [minor] imprecise: the system gitattributes file still applies ...: 'So the git inputs in effect on the clone are its .git/config (above) and the repository's own .gitattributes and .gitignore files; no per-user or system file applies.' (raw :69; the scope line :15 lists the git environment)
- [minor] latent gap: the R2-6 fix covers base site-packages but ...: Conjunct (d): 'no reads outside the clone apart from the interpreter's own installation ... (a read in the base environment's site-packages counts as outside)'
- [minor] defensible deviation from the brief's locator rule; the ...: Note 6 and (2e): 'the only mention: valence_core/stats.py@0dd6f56:3 ...'
- [minor] incomplete, and the timing is slightly imprecise: Note 10 and the README.md:60 row: the oracle tier 'needs material absent from a clone': the jlens-qwen36 clone (qwen_mlx.py:36, :41), jlens_qwen.* (:73-76) and the MLX model id (:68)

### Pass 4 (verify4): not run

### Fix 4: 4 dispositions: fixed 4

### Check 5: applied correctly 4/4; regenerates identically: True; redaction clean: True; new problems 3
- **open (minor, not applied)**: Note 10 and the README.md:60 row (raw :501, :560): after the round-4 edit, the bare line numbers ':71', ':41', ':72', ':73-76' and ':68' follow an oracle.py locator, so read by the nearest named file they point into oracle.py, not qwen_mlx.py. Proposed fix: In runtime_dep()'s return string, name the file again on the first locator after the oracle clause, e.g. '(qwen_mlx.py@bbc9ffe:71, in __init__)'. Or move the oracle-construction clause after the ...
- **open (minor, not applied)**: The Regeneration line (raw :13, item iii) says each line that depends on this machine's state is labelled as such. The new parenthetical on raw :74 depends on this machine's system gitattributes file and is not labelled. Proposed fix: Prefix the parenthetical with '(this machine: ...)'. Or name the ':74' sentence, the 'So the git inputs' line, in Regeneration (iii)'s list of machine-state lines in (1).
- **open (minor, not applied)**: Latent: git_inputs_clean's new condition sar['probe_off'] == 0 cannot tell an attribute from the repository's own .gitattributes apart from one from the system file. If they differ, it misattributes a false alarm to the system attributes file. Proposed fix: Test the system file's effect directly. Require that no (attribute, value) pair a probe gets under the environment is one that the system file's own lines set, i.e. that the attributes present ...

## N13

### Pass 1 (verify): 300 claims checked; regenerates identically: True; redaction clean: n/a; findings 17 (1 substantive)
- [substantive] wrong: Row 22 (A-g3): 'commit hash at b6e8f3f 2026-08-25T05:57:51Z (not before data)'. Sec. 2: 'commit hash f14d249 first recorded in a file at b6e8f3f' and 'Commit-hash record precedes the first data commit: False'. JSON: A-g3 ...
- [minor] imprecise: Sec. 1 table header: 'Gaps are in days from the pre-registration commit'. Row 17 (P-h, Commit 34eb7ee) verdict gap 0.0158; row 19 (LOCK-h, Commit 8a97513) verdict gap 0.1287; row 23 (P-j, Commit f7a4a1e) first/verdict gap 0.0644.
- [minor] imprecise: Row 20 (LOCK-g): First data 720a104 but First verdict data 783fdfb (B1, gap 0.0011). 'commit hash at 783fdfb (before data)'. 'Run stamp in raw: none in artifact/raw'. Sec. 7 item 1: 'No row has a verdict cell whose first data commit precedes, or shares, ...
- [minor] imprecise: Sec. 8 STOP: Q1 bet wording 'timestamped 2026-08-18' / 'pre-survey'. Yet table row 15's status reads 'ORDER HOLDS; NO SHA256 RECORDED', and 'Bet lines at the record commit' include PROPOSAL-g@72b09a9:82.
- [minor] incomplete: Item outcome. Sec. 7 item 2 says block :93's pass condition 'cannot be met as written', but the raw gives no item-level verdict. ORDER HOLDS is defined over verdict cells only.
- [minor] incomplete: Row 13 (L-r26) lists only 9f3148c. Other log rows likewise omit 'Data on the same subject committed before the version of record', a line the raw gives for P-g, LOCK-g, A-g3 and P-k.
- [minor] wrong: The H1-u cell's data commits [b2d051b, 7527270]. The per-version lists for P-h b400083 and LOCK-h v2.0 label 7527270 '(H1 run 1 (redesignated H1-u))'.
- [minor] wrong: End-of-file hunk ranges in the version diffs: P-h b400083 this_lines [197,207]; LOCK-h v1.2 last hunk prev [155,154] this [180,184]; P-j v1.1 [343,342]->[345,378]; v1.2 [379,378]->[381,445]; v1.3 [446,445]->[447,468].
- [minor] imprecise: Sec. 2 cell lines print 'data commits: ...' and 'first paths: ...'. Table cell names and sec. 7 item 12 subjects are shortened.
- [minor] imprecise: Sec. 7 item 9: 'In-raw provenance lines (recorded HEAD, lock or amendment commits): 34 listed across the cells'.
- [minor] incomplete: Sec. 0 cites PROPOSAL-m v1.11:6 only as 'the commit hash is the timestamp of record'. Sec. 5, sec. 7 item 10 and sec. 8 then note that the RECORD HYGIENE entry's '+1 day' fails in UTC for cd86e49.
- [minor] incomplete: P-j v1.3 (520f62c): 'data commits of this row's cells committed before this version (5)'.
- [minor] imprecise: W-g cell label: 'B3 screen (the confirm tier the trigger names)'.
- [minor] imprecise: Row 24's 'Run stamp in raw: 2026-09-09T22:53:57Z (k1_stage1_run.log:102)'.
- [minor] incomplete: The set of rows: '25 rows' for 'one row per pre-registration of record'.
- [minor] imprecise: L-c1 note and sec. 6 claim 2: the c1 criteria are in the record 'only as the log prose' / 'as log prose only (the script was never tracked)'.
- [minor] wrong: Builder summary: 'For the 12 other tracked documents (22 rows), no 8-hex prefix ... appears'. It also labels the hash-record search 'computed-new'.

### Fix 1: 17 dispositions: disclosed 1, fixed 16
- disclosed: Findings after 16: The findings list I received stops partway through finding 16. Any later findings were not received; the raw's section 10 says so.

### Pass 2 (verify2): 690 claims checked; regenerates identically: True; redaction clean: n/a; findings 9 (4 substantive)
- [substantive] rule-violation: Item outcome / §8: 'STOPs: 1 -- Q1 bet: the wording 'timestamped 2026-08-18' and 'pre-survey''; row 15 status '…DATE CLAIM UNSUPPORTED (STOP …)'; STOP text: 'so in the record the bet is not pre-survey'
- [substantive] wrong: §9 out-of-pattern item: cycle-1 pivot 'Pre-registered failure mode for tail-PCA' … 'first commit containing the text: c54c4e0 2026-08-08T06:31:08Z'
- [substantive] incomplete: Cell 'data commits (N)' lists and §7 item 6 / §2 amendment counts, e.g. L-e2a `814a254` '11 earlier data commit(s)' (the same 11 as bc153ed); e2a full run 'data commits (4): 54185db, 51f1e72, d49bb5d, 947b9ea'
- [substantive] imprecise: 'Order conjunct: holds for every verdict cell (30 verdict cells with data, in 23 rows)'; row 23 P-j 'First verdict data db5b09c (e2d D1 harness acceptance sessions)'
- [minor] imprecise: Same-commit non-verdict cells: 'The smoke raw lands in the same commit as the entry that states the gate' (L-c1); '(d)/e1 teacher cache … same commit … Same commit as the pre-registration' (L-dgate)
- [minor] imprecise: 'Hash conjunct: unmet … (absence, not mismatch, so no hash STOP under :93)'; §0 '(not a STOP under block :93, which names wrong order or a mismatch)'
- [minor] overclaim: §4 heading 'Other welfare text in the record (found by search at ref)'
- [minor] imprecise: LOCK-h v2.0 change 'where: status block (previous lines 1-10)'; §7 item 6 'LOCK-h f030cdd: status block (previous lines 1-10)'
- [minor] rule-violation: Document content sha256 labelled 'recomputed from git show <commit>:<path>' (JSON rows[].content_sha256_status); the md tables give these values no status

### Fix 2: 10 dispositions: fixed 10

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 6 (2 substantive)
- [substantive] wrong. The pass-2 modify-only fix introduced a double count.: Row 13 (L-r26) same-subject data: '3 files in `5aa9389`, `db0d177`; of these, 1 file by modification only: `results/raw/2026-08-12_rule26_oracle.txt` at `db0d177`'. The same count appears in section 7 item 6 ('L-r26 (3 files)') and in the regenerated ...
- [substantive] wrong for 12 of the 23 rows with data. The wording ...: Item outcome (md:21) and section 7 item 3 (md:973) say: 'What the record supports for a row is 'committed at <commit> (<UTC>), before the first data commit <commit> (<UTC>)', with the commit hash itself recorded in a later commit'.
- [minor] incomplete rationale, and the call is inconsistent with ...: The L-c1 r1/r2 cells are counted as verdict cells. The tier rationale (md:140, :144) and the judgment-call text (md:972, :1009) say: 'the entry calls the full run the primary experiment; no proposal document tiers the (c) arc, although the r2 entry calls ...
- [minor] incomplete.: Section 0: 'Each cell's tier, and the line it rests on, are given in section 2 and in the JSON'. Fixer: 'Every cell now records its tier and the line it rests on'.
- [minor] imprecise. The sentence is flat where each leg depends ...: Item outcome (md:20): 'STOPs: 0. Block :93 names a STOP only for a row whose order is wrong or whose hash does not match; neither occurs.'
- [minor] imprecise. This was already present in the input to this ...: Rows P-g and Q1: 'Data on the same subject committed before the version of record (not governed by it): 27 files in 75939ed, 85ecb52, 214fd17, 9cd324d, 2b21c72, ef12c58'.

### Fix 3: 7 dispositions: disclosed 1, fixed 6
- disclosed: Bookkeeping: A Pass 3 subsection is appended to section 10 (6 dispositions, generated by the script). The header and docstring now say passes 1, 2 and 3. Pass-1 disposition 5 and the pass-2 disposition 3 and 6 ...

### Pass 4 (verify4): n/a claims checked; regenerates identically: True; redaction clean: True; findings 3 (1 substantive)
- [substantive] incomplete: Item outcome: 'Hash conjunct: unmet for 23/23 rows with data' and 'Under the opposite readings, all 23 rows with data would carry a hash STOP' (also in the hash PI item, the section 8 referent note on :90, and pass-3 disposition 5). Row 16 (A-g1) has the ...
- [minor] imprecise: 'For 11 of the 23 rows with data the version's commit hash is also recorded in a later commit: before the row's first data for 9 (P-g, Q1, P-h, W-h, LOCK-g, W-g, A-g3, P-j, P-k), not before it for 2 (L-e2a-g3p, LOCK-h)'. This wording is offered for the ...
- [minor] imprecise: Section 0 data rule: 'A cell's data are artifacts or run raws produced by forward passes of the subject model' ('arithmetic' is among the listed model-free artifacts). Pass-3 disposition 6: 'Every other same-subject file is a forward-pass output or an ...

### Fix 4: 3 dispositions: fixed 3

### Check 5: applied correctly 3/3; regenerates identically: True; redaction clean: True; new problems 0

## N12-history

### Pass 1 (verify): n/a claims checked; regenerates identically: True; redaction clean: True; findings 9 (2 substantive)
- [substantive] WRONG COUNT. The value is at HEAD and appears 78 times ...: (ii) ssh_port row for #25124cd5: 'occ 1, src 1, HEAD occ 0 (-)', first locator 737820a8 <commit message>:41 (md:348; the JSON identifiers entry has the same counts).
- [substantive] OVERCLAIM. (i-b) does not scan binary blobs, and the ...: md:50: 'Coverage limits of the fallback, both closed by (i-b)'. Builder summary: 'The fallback cannot see binary blobs or data/m/ckpt/** (marked -diff); (i-b) covers both.' md:188: 'incl. `data/m/ckpt/**`'.
- [minor] TRUE FOR CONTENT, NOT FOR HISTORY. Commit headers were ...: (ii) summary line: 'SSH key names / fingerprints / public keys 0 / 0 / 0'; md:384 '... SSH public keys, SSH fingerprints ...: 0'.
- [minor] INCOMPLETE BUT HARMLESS. The tagger of the annotated tag ...: Identities table: 4 author/committer identities over 304 commits.
- [minor] NARROW SCOPE. The pattern misses temp paths without the ...: local_temp_path class (/private/tmp, /private/var/folders): 58 distinct, 83 occurrences.
- [minor] TRUE AS WRITTEN, BUT THE ROW'S OWN REASON TEXT UNDOES ...: md:11: 'No candidate secret, RunPod id, IP address ... appears verbatim in this file or its JSON.' The script marks IPv4 value #f1412386 sensitive=True.
- [minor] VERDICT RIGHT, REASON WRONG FOR 2 OCCURRENCES.: (i-a) bulk rule T1 'LLM-token sense' covers all 8076 'token' occurrences.
- [minor] CORRECT FOR THE 5 LOCAL REFS (ancestry re-verified). ...: md:704 / summary: 'Every scanned ref is an ancestor of origin/main ... every reachable blob is already in history GitHub accepted; none could block a push.'
- [minor] REFERENT NOTE, NOT A DEFECT. The block names the N12 ...: The part's output names: results/raw/2026-10-08_note-N12-history.md and .json.
- [missed] Commit headers: 7 SSH-signed commits (gpgsig) embed one ed25519 public key, fingerprint SHA2...[len 50]#488bbe90 (redacted). The builder never scans headers, only messages. It is a public key, not a secret.
- [missed] Exact recount of SSH ports: #25124cd5 is at HEAD (RESULTS.md:9245) and has 78 occurrences in history. The raw reports 1 and HEAD 0.
- [missed] Binary-blob contents: npz string arrays (11 members of dtype <U3/<U8/<U16) and the PNG text chunks were never regex-scanned by the builder. The verifier scanned them with 26 patterns: 0 hits.
- [missed] Context-free secret scan: the builder's high-entropy check needs an assignment or header context. The verifier's context-free scan (runs of 24+ characters, mixed case plus digits, H > 4.3) found 44 distinct values, all false positives: 8 SSH-signature ...
- [missed] Extended patterns the builder lacks, all with 0 true hits: JWT, Stripe, Slack and Discord webhooks, SendGrid, Telegram, PyPI/npm tokens, Google ya29, the legacy 32-character uppercase RunPod-key shape, PuTTY keys, secret-bearing URL query parameters, and ...
- [missed] Tagger identity of the annotated tag cycle-4-close: the same gmail identity, not enumerated.
- [missed] Temp paths without /private (/var/folders/...: 4 at HEAD; bare /tmp/: about 16 in 13 HEAD files) and ~/.claude/projects/<session-uuid> paths (4 distinct, 7 in history, 5 at HEAD) are outside the local_temp_path class. None is a credential.
- [missed] Content copies of jlens-qwen36 (the path-based check cannot see them): 37 files under jlens-qwen36/data/ are byte-identical to tracked blobs. All are the lab's own run outputs that are also committed under data/ (e.g. data/e2a/*, data/f/*, data/corpus/*). ...
- [missed] Remote-only refs (unfetched branches, refs/pull/*, remote tags) were not addressed. The PI should run `git ls-remote origin` before making the repository public.
- [missed] Local unreachable objects: 16 blobs and 1 commit sit in the object store but are reachable from no ref, so a normal push does not publish them. Informational only; the raw mentions only the 26 tmp_obj garbage files.
- [missed] HF_TOKEN appears twice, in a Hugging Face Hub warning with no value; the raw labels these with the LLM-token-sense rule.
- [missed] 'continuity' over all of history: 948 occurrences in 25 files, nearly all a design word. 'continuity password' occurs only 3 times (the audit block twice, the preflight raw once), and no value follows any of them. The only pass-phrase-shaped value is the ...

### Fix 1: 0 dispositions: 

### Pass 2 (verify2): n/a claims checked; regenerates identically: True; redaction clean: True; findings 7 (1 substantive)
- [substantive] Hard rule 4 is broken in a sibling part's output that ...: Release scrub coverage: the raw lists every IDENTIFIER at HEAD and says no candidate secret or RunPod id appears verbatim in its outputs. It defers commits after bab921ce52, including the audit's own end commit, to an advisory PI pre-flip re-run (md:888).
- [minor] The line count is one too high. The byte count is right.: md:36: '`git log -p --all` output: 69,743,183 bytes, 1,793,055 lines.'
- [minor] Imprecise against the block's condition. Block :77 runs ...: md:34: 'gitleaks and trufflehog are not installed (and were not installed), so the block's fallback applies'.
- [minor] The conclusion holds, but the raw's evidence is narrower ...: (iv), md:895 and values-check item 12: 'no jlens code, LICENSE or README content is tracked'.
- [minor] Accurate as far as it goes, but it misses one data ...: (iv)-mechanical: 'Confirm no model weights or residual arrays beyond the allowlisted .npz files are tracked' is reported as a pass, from the npz allowlist plus weight-shaped extensions (md:898-922).
- [minor] Correct as a scan result, but it shows a sensitivity ...: The context-free high-entropy scan (bar 4.3 bits/char) reports 8 distinct values in the commit headers, all SSH-signature lines.
- [minor] md:883 holds on the local evidence. The pre-flip list ...: The PI pre-flip steps (md:885-888) cover `git ls-remote origin`, refs/pull/* and a re-run at the final HEAD. md:883 says local unreachable objects are not published.
- [missed] Already-pending outputs of the audit are outside the scrub's scope: N13's raw (results/raw/2026-10-08_note-N13-provenance.md:643; .json:8321/8410/8916) carries the full pod id #a39ed293 verbatim (finding 1). Six untracked non-audit files ...
- [missed] The block's primary scanners (gitleaks, trufflehog) are installable here (Homebrew present) but were never run, because of the audit's routing. The raw does not say so (finding 3).
- [missed] Clone-index evidence for (iv): 0 of the 62 blobs in the jlens clone's index are reachable in lab history, and the 39 byte-identical files are untracked in the clone (finding 4).
- [missed] Residual-space vectors in tracked JSON: data/e2d/d2_scores.json and d3_scores.json, stored_classifier w/mu/sd, 3 x 5120 floats each (finding 5).
- [missed] Structured base64 below the 4.3 entropy bar (7 of 15 gpgsig armor lines); no base64 key-material marker patterns (finding 6). No instance in blobs or messages.
- [missed] GitHub-side surfaces published by the flip (PRs, issues, Actions logs, wiki, releases, orphaned force-pushed commits) are not in the pre-flip list (finding 7). On local evidence, no force-push happened and the unreachable commit 2591567 was never pushed.
- [missed] Informational, not a secret: /Users/ paths in 4 HEAD raws and the notebook's kernel display name disclose another local project's conda env name and the Jupyter runtime directory. The files are results/raw/2026-09-09_k_launch_entry_valuescheck.txt, ...
- [missed] Informational: the prescribed redaction form prints the whole value for values of 4 characters or fewer, and 4 of 5 digits for the 5-digit SSH ports. The raw discloses this for ports. The values of 4 characters or fewer that it prints in full (a local ...

### Fix 2: 11 dispositions: deferred-to-other-item 1, fixed 10
- deferred-to-other-item: hist_v2 F1 (substantive): N13's pending raw quotes the full RunPod pod id (#a39ed293); the history scope cannot see it: N13's files are N13's to fix. The finding is kept in this raw as a pre-release check, with the routed sentence 'every audit raw must be re-scanned before the release commit'. A new section scans ...

### Pass 3 (verify3): n/a claims checked; regenerates identically: False; redaction clean: True; findings 6 (1 substantive)
- [substantive] Incomplete. The RunPod network-volume NAME is in the ...: (ii) says 'Every identifier value, individually'. The table 'Identifiers present at HEAD' and the pre-release check (16 sensitive values) are meant to cover every RunPod identifier.
- [minor] True when the script ran, stale now. The concurrent ...: Header line 13 and round-2 item 11: 'this run scans HEAD bab921ce52, which includes the 2 commits made after bbc9ffe72f'. Coverage limit (2) at md:55: 'paths under data/m/ckpt/ ever tracked: 0, so that limit has never applied to any committed file'.
- [minor] The verdict is right; the stated mechanism is wrong. The ...: (i-b) headers, md:367: the 7 ssh_key_material_base64 hits are triaged SSH-SIGNATURE because 'the SSH signature embeds the signer's PUBLIC key blob (its wire-format key-type prefix is the marker)'.
- [minor] Over-broad. The flag puts a real redaction breach (N13's ...: Pre-release line (md:973): 'NOT CLEAN -- 3 audit file(s) ... carry a sensitive or untriaged value', including scripts/audit_note_N12_content.py, 'Each is its owning item's to fix before the end commit'.
- [minor] Not byte-reproducible beyond the stamps. One sentence's ...: The re-run reproduces the outputs apart from stamps (round-2 summary and the second checker).
- [minor] Understated. The redaction form also leaves two longer ...: md:14 caveat: 'an 8-hex hash of a short value can be inverted by enumeration (a 5-digit port has 100,000 candidates), so for such values the form hides them only from a casual reader.'

### Fix 3: 9 dispositions: disclosed 2, fixed 7
- disclosed: Code's own: the new 64-hex value under key_set_sha256 (from cf8eb5b) was cleared with the 'label built of words' reason: Added a hex-digest rule ahead of the label rule. It covers a 40- or 64-hex value under a key naming sha/hash/digest. The verdict stays FALSE-POSITIVE and the reason is now accurate. Recorded in R3-2.
- disclosed: Code's own: the pending N16 raw gained counts on lines whose only port word is 'port of' (a code port), which tripped the leak assertion: Added a code-port rule: a line on which every ssh/port/alias match is 'port' in 'port of' is no longer read as a port line, in both the history and pending scans. History has 24 such lines ...

### Pass 4 (verify after round-2 fix): n/a claims checked; regenerates identically: True; redaction clean: True; findings 4 (0 substantive)
- [minor] The class rows add up the per-value source counts; they ...: md:440 defines the class table's `src` column as 'distinct blobs/messages'. The new runpod_volume_name row (md:447) gives src 147.
- [minor] The verdict is right; the reason misdescribes the prose. ...: md:507 (MANUAL_TRIAGE 84cbedd5): `update-network-volume` is FALSE-POSITIVE, 'the RunPod MCP tool name ... in prose about renaming the volume'.
- [minor] Fixed for that value. The gap behind it remains. The ...: Round-3 item 2 (Code's addition): a hex-digest rule now runs before the label rule, so the 64-hex `key_set_sha256` value no longer gets the reason 'a label built of words'.
- [minor] The pending scan has no class for third-party personal ...: md:983-985 and pre-flip step 1: - the pre-release line for redaction-rule values reads CLEAN; - the identity line says the routing's redaction rule 'covers third-party personal data'.

### Pass 5: not run

### Fix 4: 4 dispositions: fixed 4

### Final check: applied correctly 4/4; regenerates identically: True; redaction clean: True; new problems 2
- **open (minor, not applied)**: The R4-3 guarantee is worded more broadly than the code. md:1057 says 'a hex-only value that the hex-digest rule does not clear is now UNTRIAGED' and 'A pre-flip re-run that meets a hex-only value now stops on it instead of clearing it'. The script header ... Proposed fix: Either narrow the wording at md:1057 (the generator at script:2775-2797) and in the script header to 'a hex-only value holding a letter a-f is never cleared by the label rule', and name the two ...
- **open (minor, not applied)**: Two round-4 conclusions are fixed text, not computed. md:1057 says '... FALSE-POSITIVE 41 (round 3's raw: FALSE-POSITIVE 41), so no verdict changes' (script:2792). md:1060 says '... and no history verdict changes' (script:2830-2831). Both print ... Proposed fix: Make both clauses depend on what this run computes. For example, print 'so no verdict changes' only when qd_ == {'FALSE-POSITIVE': 41} and the replayed round-3 verdicts (r3_verdict over this run's ...

## N12-licenses

### Pass 1 (verify): n/a claims checked; regenerates identically: True; redaction clean: True; findings 9 (1 substantive)
- [substantive] REFUTED as stated. A third-party material the record ...: Pass line and section 6: 'the source, pinned sha and license of every third-party material and model are recorded above.'
- [minor] REFUTED. The record states it.: Section 2b: 'whether `ACK` ("Ok.") is theirs is not stated.'
- [minor] Incomplete. The record itself says the upstream is a ...: Section 2c/6: the jlens-qwen36 row gives WeZZard/jlens-qwen36 (Apache-2.0) as the only source.
- [minor] CONFIRMED in substance, but unquantified, and narrower ...: Section 2c: 'Local copies of upstream files may carry local edits; the comparison below uses the on-disk copies.' Plus the HEAD-only scope of the copy check (byte identity, identical bodies, near-copies).
- [minor] Overclaims. The block, the history scans, the clone and ...: Header line 4: 'every repository read is at this commit'.
- [minor] Its text matches block line 85. It is hard-coded, ...: Pass line '(iv) licenses recorded' (script lines 1395-1403).
- [minor] Imprecise.: Section 5: 'Readers could view the code but would have no grant to reuse it.'
- [minor] CONFIRMED (667 tracked, all mode 100644/100755; no ...: Header line 9: text files scanned 645 of 667.
- [minor] The block (line 84) names one output, ...: Output location.
- [missed] The Jacobian lenses (Neuronpedia n=1000, MIT on HF; jlens-qwen36 release lenses v0.1-demo/v0.2-fulldepth) have no license row. They are the primary lens in cycles 1-4 and are untracked: 0 data/lens paths in any of the 304 commits.
- [missed] Anthropic's jacobian-lens (Apache-2.0, per my GitHub API read) is the upstream of jlens-qwen36 and is not named.
- [missed] The copy check is HEAD-only; the release publishes full history. My history-wide check (304 commits, 1,161 distinct blobs, clone index blobs read as a file) finds 0 non-empty upstream blobs and 0 near-copies (max 0.131), so the conclusion holds, but the ...
- [missed] The 4 upstream files carrying local edits on disk are not listed: interventions.py, pyproject.toml, run_experiments.py, uv.lock.
- [missed] Remote-side refs cannot be seen locally. The fetch refspec is the default and .git/FETCH_HEAD is empty, so GitHub may hold branches or PR refs (refs/pull/*) that are not among the 5 local refs scanned. I did not run `git ls-remote origin` (network plus ...
- [missed] Runtime library dependencies (mlx, mlx-lm, transformers, torch, numpy) are not listed. No dependency manifest is tracked and none of them is vendored, so this is optional README content only.
- [missed] The cycle-1-2 residual corpus fell back to C4 through the upstream loader (archive/RESULTS-cycle1-2.md:985-987). I checked that results/raw/2026-07-19_basis_sensitivity_diagnostic.txt (4,759 bytes) holds only statistics, not C4 text. A row is optional.
- [missed] De minimis, recorded for completeness: archive/CLAUDE-cycle1-2.md:391 says one C one-liner prompt was 'borrowed from the jlens-qwen36 demo' (Apache-2.0).

### Fix 1: 0 dispositions: 

### Pass 2 (verify2): n/a claims checked; regenerates identically: True; redaction clean: True; findings 9 (1 substantive)
- [substantive] Incomplete in a way that changes the PI's decision. The ...: Sections 1, 6 and 7 (md:52, :366-367, :381) say the Macar materials carry no license and that no right to redistribute them is granted. The framing row's 'redistribution OK?' cell reads 'not stated'.
- [minor] The sweep only matches github.com and huggingface.co ...: Section 2f's external-reference sweep (21 distinct ids, 0 unclassified) grounds the set of third-party rows 'by a tool run' (md:280, md:398).
- [minor] 20 is an exact single-line match, so it is a lower ...: The trial question is carried by 20 tracked files at HEAD and 20 paths across history (md:38, :40, :367).
- [minor] The script actually uses \bMacar\b, which drops 27 ...: Section 2a's third-party pattern is printed as 'safety-research|introspection-mechanisms|Macar|WeZZard|github.com|huggingface.co|arxiv', with 26 hits.
- [minor] The arithmetic is correct, but the size cannot tell the ...: In 2d, v0.2-fulldepth's two parts sum to 3,303,030,398 bytes, 'equal to lens.npz: True' (md:268).
- [minor] This contradicts section 2f, which prints one ...: 'Redactions applied by this script: 0' (md:388; JSON redactions []).
- [minor] Read literally, the clause is not answered there. 39 ...: The pass line '(iv) licenses recorded', the section 6 jlens row and section 7 item 3 answer block line 80's 'Confirm nothing from the gitignored jlens-qwen36/ clone is tracked' with 'tracked paths: 0'.
- [minor] That was true when the script ran, but HEAD has since ...: The raw's history scans cover 'every commit reachable from the local refs' at commit bbc9ffe.
- [minor] It is two sentences (two questions).: md:52 calls the trial question 'one-sentence'.
- [missed] arXiv:2603.21396 is CC BY 4.0, and its Appendix A Table 4 prints the framing, 'Ok.' and the trial question. So the framing text has a license through the paper, and the raw does not record this (finding 1).
- [missed] Lindsey (2025, Anthropic, 'Emergent Introspective Awareness in Large Language Models') is the origin of the 50 concepts according to Macar Appendix B.1. The record never cites it, and its license was not established (my partial read found none stated).
- [missed] The Anthropic 'Verbalizable Representations Form a Global Workspace' paper (transformer-circuits.pub/2026/workspace; anthropic.com/research/global-workspace) has no row. The cycle-1 raws replicate its figures through upstream run_experiments.py.
- [missed] No host-agnostic URL sweep was run. Hosts outside github.com and huggingface.co (transformer-circuits.pub, anthropic.com, plus two model-output URLs) were not enumerated.
- [missed] Trial question line-wrapped or escaped in RESULTS.md and scripts/b2r_scorer_selftest.py (2 files beyond the 20).
- [missed] Run-time users of MACAR_FRAMING (scripts/box_a2_baserates.py, scripts/box_cached_gen_smoke.py) are missing from the harness row.
- [missed] Commits c75d4d8 and bab921c, added after the read commit bbc9ffe, are not covered. My marker check of their added lines found no third-party material.
- [missed] Independently re-derived and in agreement with the raw: 5 refs, with no stash, notes or replace refs; 304 commits (rev-list --all and --reflog); 670 paths ever; 1161 distinct blobs and 1143 text blobs (the raw's 1142 excludes the empty data/.gitkeep); 667 ...

### Fix 2: 10 dispositions: fixed 9, rejected-with-reason 1
- rejected-with-reason: checker's missed items (independent re-derivations): Nothing to apply: they agreed with the raw. All counts are recomputed at bab921c.

### Pass 3 (verify3): n/a claims checked; regenerates identically: True; redaction clean: True; findings 5 (0 substantive)
- [minor] Incomplete. The prompt text was first published in ...: md:59 says the Lindsey page prints the trial prompt but 'its framing was not compared with the record' (JSON web_reads_recorded.lindsey_2025_page.result.trial_prompt_framing_compared_with_record: false). Section 6's prompt-text row (md:392), section 1's ...
- [minor] The script hard-codes this attribution for any list of ...: Header line 6 (md:6) attributes every commit after the block commit to 'the concurrent PROPOSAL-m session, not by this audit'. The raw also requires a re-run at the final pre-flip commit (md:6, md:415).
- [minor] Incomplete as a location for subsets. Only ...: The concept-list row (md:393) gives the location as `data/configs/b2_concepts.json` '(and 4 of the concepts in data/configs/b2r_step1.json, section 4)'. Section 7 item 1(b) offers 'replace the file with a pointer'.
- [minor] Slight overclaim. hosts_in() keeps a URL host only if it ...: Section 2f's host-agnostic sweep is described as covering 'any `http(s)://` host' with 0 unclassified (md:316). A pass gate rests on it.
- [minor] Wording nit. README lines 3-4 refer to 'Anthropic's ...: md:283 and the section 6 Global Workspace row (md:396) say the README 'names' the Global Workspace paper (README.md@bab921c:3).

### Fix 3: 7 dispositions: disclosed 1, fixed 6
- disclosed: Checker's note: HEAD had moved to cf8eb5b.: Re-run at the current HEAD, cf8eb5b: 307 commits, 683 tracked files, 1162 historical text blobs. All 7 pass gates are True and the pass line reads '(iv) licenses recorded'. Every count is ...

### Pass 4 (verify after round-2 fix): n/a claims checked; regenerates identically: True; redaction clean: True; findings 4 (0 substantive)
- [minor] This is a partial deviation from routing rule 8 ('Keep ...: Header md:6 says bare `file:line` entries from the scans 'are at the commit read'. The Values-check routing row (md:476) says every record locator is now pinned to bbc9ffe.
- [minor] This is a wording inconsistency. Sections 1, 6 and 7 and ...: Section 2f's class cell for arXiv 2603.21396 (md:297) says the prompt text 'appeared earlier, unlicensed, on the Lindsey (2025) page'.
- [minor] This value is stale. It is true of the round-2 read it ...: JSON web_reads_recorded.lindsey_2025_page.result.trial_prompt_framing_compared_with_record is false.
- [minor] The script deviates: it exposes only `--out-dir`, and ...: Routing hard rule (2) requires that 'Each script keeps --out/--json-out with the results/raw defaults'.

### Pass 5: not run

### Fix 4: 6 dispositions: disclosed 1, fixed 5
- disclosed: Code's own note: at the pre-flip re-run this audit's own raws and scripts become tracked, and the pass line gates on 0 unclassified ids and 0 unclassified hosts: Nothing in the gates or the classification rules was changed. To share the sweeps' rules, the id and host classifications became two functions; the tables are unchanged by that move (diffed ...

### Final check: applied correctly 6/6; regenerates identically: True; redaction clean: True; new problems 3
- **open (minor, not applied)**: The round-4 projection text in section 2f, and section 7 item 8, say the sweep gates will fail no matter what the counts are or whether the files are still untracked. At the pre-flip re-run, the very run they are written for, this text would be false and ... Proposed fix: Make both sentences depend on the counts. If own is empty, say this audit's files are tracked at the commit read and the sweeps above count them directly, and refer to the pass gates. If the ...
- **open (minor, not applied)**: The Round-4 row for finding 3 says 'The script reads that field nowhere, so no md text changes with it', but the same row is built by reading that field. Proposed fix: Reword to 'no text in sections 1-7 or the pass line reads that field (only this row quotes it)'.
- **open (minor, not applied)**: The Round-4 'Code's own' row says 'this run's tables equal the round-3 run's apart from the first-locator column and the 2603.21396 class cell'. That holds only for section 2f's two tables. The section-6 table also changed in round 4. Proposed fix: Narrow it to 'this run's section-2f id and host tables equal the round-3 run's apart from ...', or compute the comparison.

## N12(vi) content review

- 13 reviewers (12 chunks + history); flags 59. Refuter round 1: 39 verdicts, 12 survive. Round 2 (the 20 flags the truncated round-1 input left without a verdict): 20 verdicts, 6 survive. Every verdict is in results/raw/2026-10-08_note-N12-content.md sections 4-6 and 9.
## N2: round 5 (the tokenizer-absent fix; run wf_a1faa308-998)

Round 4's application check found one substantive new problem. Round-4 code made scripts/audit_note_N2.py crash when the local OLMo tokenizer, a file outside the record, or the tokenizers library is absent. The fixer applied it and the two minor findings that came with it. The checker then ran the script three ways with the tokenizer absent: missing file, missing library, and an empty HOME. Each exits 0 with 56 figures; only the emulation row drops, and the other 56 are identical to the canonical run field for field.

- a_canonical_rerun: PASS
- b_tokenizer_absent: PASS
- c_minor_findings_applied: PASS
- d_redaction: PASS

- **open (nit, not applied)**: In a tokenizer-absent run, pass-3 item 4's bold finding sentence is printed in that run's row numbering ('Rows 21 and 32'). Section 11's lead says finding sentences carry their own pass's numbering, and pass 3's was 33. Item 2's finding keeps 'row 57' and item 3's keeps 'rows 22-23'.
- **open (nit, not applied)**: The docstring's absent-path sentence ends 'and nothing else changes'. In that path, 2(d) also gains the restricted-set paragraph and section 11's lead gains a sentence.
- **open (nit, not applied)**: Cosmetic: docstring line 23 is 112 chars (not rewrapped), and :3239 reads 'hdr_end =next('.
- **open (nit, not applied)**: Pre-existing since pass 1, edge case only: if PREPRINT-v1_0-draft.md is absent, the header says 'absent; not read', but pass-1 item 5's detail still says the search ran 'in the working-tree PREPRINT-v1_0-draft.md'.

