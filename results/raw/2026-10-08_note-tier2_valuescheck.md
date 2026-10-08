# AUDIT-note-release v1.2: Tier 2/3 values-check record (N5, N6, N7, N8, N9, N10, N14, N16, N17)

- Code stamp: 2026-10-08 12:47:47 UTC (date -u). Block sha256 8cd8a9ac...3841 (committed at bbc9ffe).
- Process record. For each item it lists every adversarial checker pass, the findings by severity, the fixer's dispositions, and the final application check. Source: the local workflow results of runs wf_2d597612-243 (build/verify/fix/verify2) and wf_c1733493-500 (round 2), which are not in the repo. The item raws carry the authoritative Values-check sections.
- Residual minor findings that the final check raised and that were NOT applied are listed under each item as **open (minor, not applied)**. None is substantive.

## N5

### Pass 1: 74 claims checked; regenerates identically: True; redaction clean: True; findings 10 (1 substantive)
- [substantive] Every share reproduces. The 'consistent with ≈ .50' ...: Raw §5 and the Figures row 'exploration share ≈ .50 by arm' (computed-new): the shares are 'consistent with ≈ .50 in every arm' (SOLV .540, DIFF .479, NOV .525, CORR .470, FDBK .576, sham .505).
- [minor] Too generous, and the raw leaves out the record's own ...: Raw §7d: the preprint's clause 'at a dose a later calibration (§8.1) found below its visibility criterion' is 'accurate as far as it goes'.
- [minor] The numbers reproduce, but the wording mixes domains. ...: Suggested note wording (§7d): '40 of 306 corrupted-label rounds delivered clean text, and 16 of 58 sessions saw one corrupted task rather than two before the first choice'.
- [minor] Locators are off. :97 is the 'Termination table' header ...: §4: 'NOV-Q 3 vs NOV-P 3; sham 7 -- as the verdict entry states (archive/RESULTS-cycles3-4.md@bbc9ffe:97)'; and the '33 attempts ≈ 1.0%' row cites :98.
- [minor] The locators are imprecise and one source is missing. P ...: §6 'Record: archive/RESULTS-cycles3-4.md@bbc9ffe:108' for the in-session accuracies; the FDBK 93% row's sources.
- [minor] Confirmed. The f1-era record itself already carries ...: The CORR covariate row: the '+.094' in the verdict entry is a transcription of the superseded f0 v1 value; the figure of record is +.078.
- [minor] The script prints this sha from a constant (script lines ...: The Figures row for the preprint clause prints 'PREPRINT-v1_0-draft.md (working tree, untracked, sha256 d6431e97...222b8)'.
- [minor] Reproduced overall (39/3074 = 1.27%). By arm the range ...: Figures row 'termination attempts ≈ 1% of rounds by arm': reproduced.
- [minor] An omission, not an error. Q accuracy on rounds that ...: §7c/§7d: the byte-clean delivery is reported, but its effect on the record's 'visible but performatively costless' / 'delta VANISHED' reading is not drawn.
- [minor] Off by one: the entry ends at :420 ('pre-registration.').: §1: 'f1 PRE-REGISTRATION ...: archive/RESULTS-cycles3-4.md@bbc9ffe:366-419'.

### Pass 2: 109 claims checked; regenerates identically: True; redaction clean: True; findings 6 (0 substantive)
- [minor] Wrong sign given the raw's own direction check. Hard ...: §3a: 'A generic brevity preference would mimic a toward-hard lean if it were general; the test asks whether it is.'
- [minor] Overbroad. At the pin the substance was already on ...: §7d(i): 'It stated found before any record supported it ... At the pin that was still so'
- [minor] The status is generous. The overall rate reproduces as ...: Figures row 'termination attempts ≈ 1% of rounds by arm': status reproduced
- [minor] Stronger than the raw's own test supports. The post-hoc ...: §5: 'FDBK is the exception to ≈ .50'
- [minor] Not scoped. That smoke ran on the superseded v1 pools ...: §7a: the smoke read 'corrupted tasks render correctly' (archive:357) is cited as part of what the f1 record says about the dose
- [minor] Four locators anchor to the start of an entry rather ...: Locator precision for several cited spans

### Fix 1: 13 dispositions: fixed 13

### Fix 2: 6 dispositions: fixed 6

### Final check: applied correctly 6/6; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: The R2-5 check says the first smoke's CORR rows have '12 in the QA form the recast removed'. That number undercounts the QA form: it counts only Task lines that begin with the literal 'What is'. Proposed fix: Relabel it as '12 beginning with the literal "What is" (18 of 18 in the question form the recast removed; 0 of 20 in the later smokes)', or count lines ending in '?' and keep the JSON key name honest.
- **open (minor, not applied)**: The new by-arm termination row says 'per arm the figure holds for the five contrast arms (0.79%-1.51%) but not for sham'. That draws a cut between CORR's 1.51% and sham's 1.99% without stating a tolerance. Proposed fix: Drop 'holds for the five contrast arms'. Write instead: 'by arm 0.79%-1.99%; sham highest at 1.99% (≈ 2%, twice the stated ≈ 1%), CORR next at 1.51%'. Alternatively, state the tolerance under ...
- **open (minor, not applied)**: Round-1 Values-check row 5 now prints the round-2 locator (:106-107) in its evidence cell. It therefore misreports what round 1 cited, which was :106, and unlike rows 2 and 8 it carries no pointer to its round-2 successor. Proposed fix: Append '[span refined in round 2, row R2-6]' to row 5's evidence cell, or freeze the round-1 row's locator text to what v2 printed.

## N6

### Pass 1: 130 claims checked; regenerates identically: True; redaction clean: True; findings 6 (0 substantive)
- [minor] Imprecise labeling. These rows are definitions and code ...: Figures-table statuses 'reproduced' for 'certification definition', 'quarantined primitive's name' and 'what quarantined enforces'
- [minor] Correct at N6 under the harness rule for Tier-2 items, ...: Two rows marked 'discrepant' (preprint :111 gloss; the directional-leak family '≤ 3% of bar') alongside 'STOPs: None'
- [minor] Partly unsupported. LOCK-h:83 declares the ...: 'Verdict tier, in-campaign monitor (marker + random pooled, as declared at LOCK-h.md@bbc9ffe:83)'
- [minor] Understated. The explicit check is also logged in the ...: §5: the sanctioned import direction 'is logged once, in results/raw/2026-08-22_consolidation.txt@bbc9ffe:30 (log-only)... the only logged exercise found is the consolidation raw'
- [minor] Correct but uncited, and very long. The identity clause ...: §3b one-sentence certification definition: '...sessions identical to the verdict tier's except that no pick selects a state...'
- [minor] Incomplete but harmless. The pinned PROPOSAL-h includes ...: §0 commit-order table: '34eb7ee PROPOSAL-h committed (pre-registration of record)'

### Pass 2: 140 claims checked; regenerates identically: True; redaction clean: True; findings 5 (0 substantive)
- [minor] Every number is right, but the citation hides a wording ...: §2a: 'Registered text: PROPOSAL-h §3 PROPOSAL-h-state-present-choice.md@bbc9ffe:136; LOCK-h v2.0 §2 LOCK-h.md@bbc9ffe:60' is followed by the envelope as max(|pseudo-Δ_sham|, |pseudo-Δ_random|), and conjunct (i) is reported as failing.
- [minor] The logic is correct, but provenance is incomplete. ...: §3b: the certification code is quoted as the 'code of record, pinned' at scripts/e2b_h1_sessions.py@bbc9ffe:171-174,213-225. §4 cites valence_core/session_e2a.py@bbc9ffe:78 for the menu templates.
- [minor] Locator slightly off. :6795 carries only '0.0735 = ...: §3a: '23.4%/41.5% RESULTS.md@bbc9ffe:6795'
- [minor] The exact command cannot be re-run from a clone, because ...: Header: 'Command: ... scripts/audit_note_N6.py --compare-json <session-scratch>/N6/builder_N6.json'
- [minor] The summary is stale against the files. The script on ...: The builder/fixer summary handed to this verifier: script sha256 cb87babd..., and status 'reproduced' for 'certification definition', 'quarantined primitive's name' and 'what quarantined enforces'; '14 insulated harnesses assert the module's absence'.

### Fix 1: 7 dispositions: disclosed 1, fixed 6
- disclosed: Fixer's own additions (not checker findings): These add no new statistic. Two computed-new rows from §2c and §2d's existing prose are now in the Figures table: the 47 vs 48 first-read flips, and the realised envelope at the null median. §0 ...

### Fix 2: 6 dispositions: disclosed 1, fixed 4, rejected-with-reason 1
- disclosed: R2-F5 (minor), staleness: the routing summary was stale (script sha cb87babd..., and 'reproduced' for three rows); N1 should ingest the raw's JSON.: The Round-2 table records this run's script sha256 (it does not begin cb87babd) and the three rows' computed statuses (computed-new). Code's note 5 tells N1 and the README to ingest ...
- rejected-with-reason: R2-F5 (minor), split: reuse the raw's '14 files' phrasing, or split it into 9 harness/runtime assertions and 5 m-package self-test checks.: I kept the raw's phrasing, labelled it a string-marker heuristic, and added a split computed from the AST at bbc9ffe. The result is 10 runtime and 4 self-test only, not 9/5. ...

### Final check: applied correctly 6/6; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: The new signed-reading counterfactual is not labelled post-hoc or computed-new anywhere. It evaluates conjunct (i) under a non-operative reading of the criterion after the data, and appears in §2a (md:148), §6 (md:469), the Figures note of the conjunct (i) ... Proposed fix: Append '(post-hoc, computed-new: a reading of PROPOSAL-h's registered words, not a criterion; the operative lock governs)' to the §2a sentence, and carry 'post-hoc' into the conjunct (i) Figures ...
- **open (minor, not applied)**: The Round-2 intro (md:536) says 'one Figures note gains a pointer', and the fixer summary says the same. The conjunct (i) note actually gained a substantive clause: the |·| provenance (f030cdd) and the counterfactual 'under PROPOSAL-h's literal signed ... Proposed fix: Reword to 'one Figures note (conjunct (i)) gains a sentence on the envelope's provenance and the signed reading, with a pointer to §2a'.
- **open (minor, not applied)**: With --compare-json, the R2-F4 evidence row prints a contradiction: 'this raw was written without the flag (flag given to this run: True)' and 'The command in the header needs no session-scratch input', even though that run's header names the flag. This ... Proposed fix: Make the clause conditional on args.compare_json. When the flag is given, print e.g. 'this run took --compare-json and is not the canonical raw; the canonical raw is written without it'.

## N7

### Pass 1: 75 claims checked; regenerates identically: True; redaction clean: True; findings 10 (1 substantive)
- [substantive] Status overstated: the record does not state the domain, ...: Record-prose row 'V1-lineage bar 0.39-0.78 vs displacements 0.02-0.28' (RESULTS.md@bbc9ffe:8781), status discrepant ('D+ over 16 cells 0.0136-0.2772')
- [minor] Omission. The B3 headline says 'no stage's sign locks ...: Section 5 checks the record prose of the cited Q3 entries (B3 SCREEN COMPLETE, RESULTS.md@bbc9ffe:7655)
- [minor] Not checked by the raw. It is an overstatement for instruct.: Record prose at RESULTS.md@bbc9ffe:7690-7693: round-degeneracy is 'every stage an order of magnitude under the declared p0 of 0.02'
- [minor] Values are correct, but the sensitivity is not surfaced ...: Figure 'ratio of steering displacement to natural contrast about five times larger at base' (PREPRINT-v1_0-draft.md:129) reproduced as 4.28-5.00x, 'at matched dose 0.10, D+ only'
- [minor] Partial gaps.: Rule 6 completeness of the raw's tables
- [minor] The rendered line omits the unit that the raw's own note ...: Code's four-number line in section 4d
- [minor] The value is correct, but the script only echoes the ...: SFT/DPO/instruct qualify at doses of 1.0 or below: MED_c 1.0/1.0/1.0, status reproduced
- [minor] Robustness defect; no wrong output in this run. Many ...: Statuses and the STOP count in scripts/audit_note_N7.py
- [minor] Imprecise. The MED rows cite only the base row for all ...: Locators for the MED figures and PI note 7
- [minor] The command echo omits the working directory, and the ...: Header 'Command:' line

### Pass 2: 92 claims checked; regenerates identically: True; redaction clean: True; findings 4 (2 substantive)
- [substantive] Imprecise in substance. The numbers are right, but the ...: Raw section 1 (and PI note 7's suggested note wording) defines the instrument behind G_c this way: 'the 256 token ids with the largest |mean log-prob difference post-praise - post-criticism| are selected and the difference vector, normalised, is the weight ...
- [substantive] The reproduction is correct as the record's statistic. ...: The 'ratio of steering displacement to natural contrast ~5x larger at base' (preprint :129) is marked reproduced as D+/G_c at frac 0.10. PI note 10 suggests the wording 'positive-pole displacement per unit G_c at matched dose ... 4.3-5.0 times larger at ...
- [minor] Status open to dispute. The record's own sentences set ...: Record-prose row 'V1-lineage bar 0.39-0.78 vs displacements 0.02-0.28 (RESULTS.md@bbc9ffe:8781, :8442)' is marked reproduced 'once the domain is named' (D+ at the MEDs, or over the 6 passing cells).
- [minor] One column has no stated domain.: Section 4e table states each column's domain (rule 6).

### Fix 1: 11 dispositions: fixed 11

### Fix 2: 4 dispositions: fixed 4

### Final check: applied correctly 4/4; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: Section 1b Reading says '(pole mean floors -19.8 to -15.7 here)' with no domain. Those are the stage means (over 12 probes) of the per-probe fit-half pole mean floors. The per-probe pole mean floors, which are what the selection actually imputes, span a ... Proposed fix: Name the domain ('stage means over probes of the fit-half pole mean floors, -19.8 to -15.7; per probe -23.2 to -14.2'), or print the per-probe range instead. No status changes.
- **open (minor, not applied)**: Section 1b Reading says 'On OLMo the pole with the lower mean floor fills all 256 slots'. That reads as if the selected ids belong to that pole, but they are ids absent from it. Proposed fix: Reword to 'ids absent from the pole with the lower mean floor fill all 256 slots'.
- **open (minor, not applied)**: The new lexical-counter domain clause in 4e (and pass-2 #4) has two slips. It cites the stored field as `counters.lexical.total`. It also says the counter fires when 'the session's own roster tag' appears, singular. Proposed fix: Cite `b3_screen_<s>.json:counters.counters.lexical.total`, and say 'either of the session's own two roster tags (tag_plus, tag_minus)'. No value changes.

## N8

### Pass 1: 150 claims checked; regenerates identically: True; redaction clean: True; findings 9 (1 substantive)
- [substantive] Partly reproduced. The lower bound holds. The upper ...: Purity–potency 'last-position self-indexed 0.83–0.88' is 'reproduced' (value printed 0.8294–0.8747, L40–L60)
- [minor] Wrong as stated; the figure is unaffected. ...: §2e: 'D1 has no marks file and its 40 M rounds are taken as unmarked, as the closure does'. The script hard-codes rm['d1'] = (0, n) and marked_keys('d1') = set().
- [minor] Understated status: these p values are already record ...: §2e's dose-step Fisher tests are labeled 'computed-new beside the closure'
- [minor] Incomplete against the record. The closure text of ...: e2d readability '.574/.613 vs .70' row: 'CV: task-disjoint halves, B = 20', given identically for both doses
- [minor] Correct, but the prose figure has no pinned locator, ...: Self-indexed residual row: 'the extraction entry says ≈ .51–.55'
- [minor] Incomplete. It omits two subjects that do name counts: ...: §1: list of 'count changes named in the subjects of commits touching valence_core/regression/analysis.py'
- [minor] Each is Code's paraphrase, not the record's wording. (a) ...: Unlabeled interpretive glosses: (a) S2 'This is the causal counterpart of the 0.85 character cosine'; (b) D1 readability 'n = 4, noise'; (c) random-arm note 'one-sided asymmetry noted in S2's adjudication (ratio 5.05)'
- [minor] The values reproduce. The raw does not flag the carrier ...: ‖d‖/R ≈ 0.16 row (reproduced 0.1568–0.1700)
- [minor] The domain is not stated. The counts are over all M-arm ...: Rule 6 domain for read-marked rates ('Read-marked rounds, M arm … d2 34/300 …')

### Pass 2: 78 claims checked; regenerates identically: True; redaction clean: True; findings 10 (1 substantive)
- [substantive] WRONG STATUS. The record carries this value. The ...: §2e dose-step line, the Figures context row 'dose-step p values', Notes item 10 and values-check row 3 all say: audit .10->.20 two-sided Fisher p = 1.0000 is 'not in the record: computed-new'.
- [minor] WRONG WORDING. At one significant figure every layer ...: Figures row ‖d‖/R and Note 8: 'the preprint's "≈ 0.16 at every layer" holds to one significant figure'.
- [minor] INCONSISTENT AS WRITTEN. 2 × 0.0884 = 0.1768. The 0.1767 ...: §2c V1 line: 'min(Δ+, |Δ−|) 0.2848 > 2·max|Δ_rand| = 2·0.0884 = 0.1767'. Figures row 'random ≤ 0.088': '2x = 0.1767'.
- [minor] MISLEADING WORDING. S2 ran the same 4-bit MLX model ...: Δ+ row and §2c: 'S2's separate full-precision re-run ... gives +0.284778'; 'carried the reward and random arms again at full precision'.
- [minor] STATUS LABEL MISSING. None of these sub-figures is in ...: Figures rows '9/12 and 10/12' and 'LOO Δ+' and 'G = 0.316' carry 8/11 and 9/11, LOO Δ− = -0.1898, 2.14x and 7.9x as plain values.
- [minor] INCOMPLETE. The block also has '103/103' at :137 (§6, ...: Note 1: "Every '103' (block :68/:70/:107, README.md) is the post-S2 count".
- [minor] CORRECT BUT INCOMPLETE. FINDINGS-3.md@bbc9ffe:50 makes ...: Note 5 flags the preprint's 'clean overdose regime at f = .40, where both poles read as post-criticism' as true at L44 only. Note 4 calls FINDINGS-3's 'elsewhere' ambiguous without a locator.
- [minor] RULE-6 GAP (row level). The row names neither its ...: Figures row 'comparator .534': 'arm R (norm-matched random direction, same dose), k = 2, clean domain 74/74'.
- [minor] IMPRECISE. 1,344 = 48 tasks × 7 frames × 4 paraphrases ...: §2a: 'Directions are mean differences of raw-residual activations over the 1,344 extraction contexts'.
- [minor] The JSON output has no 'stops' key (d.get('stops') is ...: Builder summary: 'stops: []'.

### Fix 1: 10 dispositions: fixed 10

### Fix 2: 10 dispositions: fixed 10

### Final check: applied correctly 10/10; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: In the comparator row, '74/74 recomputed (= stored 74/74)' prints '=' as a literal. Nothing compares the recount with the stored n_pos/n_neg: no assert and no conditional. The finding-8 edit made the stored side come from the artifact, but the equality is ... Proposed fix: Assert dom['d2|R|v2+read'] == (rR['n_pos'], rR['n_neg']), or print '=' only when they are equal and 'NO, differs from' otherwise. The other readability sets could get the same check (§2e prints ...
- **open (minor, not applied)**: Round 2's relabelling (finding 5) left two figures of the same class unlabelled. Both are computed here and absent from the record. §2c's 'G over the other 11 probes = 0.2390, half 0.1195' is marked only 'post-hoc beside'. Note 6's 'the R arm degrades at ... Proposed fix: Append 'computed-new (post-hoc, descriptive)' to the G-over-11 figures in §2c and to 1.92x in note 6 (the record has 'twice', RESULTS.md@bbc9ffe:3343), and add both to note 10's list of ...

## N9

### Pass 1: 110 claims checked; regenerates identically: True; redaction clean: True; findings 10 (0 substantive)
- [minor] Partly false. The script accepts the flags, but line 129 ...: Scripts take --out/--json-out with results/raw defaults (harness rule 2), so the item can be re-run into scratch.
- [minor] Rounded upward. The conservative bounds the script ...: Post-hoc control-pair-text lower bounds: figure table 'A >= 0.703; B >= 0.349'; section 2a 'the control-pair texts carry >= 54.7% (A)'; builder summary/pi_items '>= 0.70 (A) and >= 0.35 (B)'.
- [minor] Supported in substance but under-quoted. The ...: 'The pre-registration words G1 as the r3 matched-pair swing criterion; the code that ran tests each replicate's oriented cosine ... (the c1 P2 form), not swings' (section 1; summary item (ii) 'rather than the pre-registered swing form').
- [minor] Over-broad status. Only the bar (0.1) and n (32) are in ...: Figures row 'leakage gate's bound' is status reproduced, with value 'max over n=32 texts of |Δ(logit a − logit b)|, adapter ON − OFF, final position <= 0.10 logit'.
- [minor] True about the archive, but it answers a referent that ...: Referent note 2: "The '(d) VERDICTS entry'. The archive has no (d) entry titled VERDICT."
- [minor] The values are correct, but the comparison is not ...: 'Across the three adapters the maxima rank with the G1 cosine (smoke A: cos 0.1509 -> max 0.5000; B: cos 0.4354 -> 1.0625; A: cos 0.4756 -> 1.7500)'.
- [minor] Correct but only partly located. The 12-example smoke ...: 'one epoch over 12 examples ... against three epochs over 172 for the trained ones' (section 2).
- [minor] Mostly. Three exceptions: 'FINDINGS-3:117' in the ...: Figure-table sources and locators are pinned and name their artifact.
- [minor] Fragment. The menu line in d_gates.py (local, lines ...: Leak-text description: '... then the menu `f"{a} / {b}\nConfig choice (one word):"`' (and the 'verbatim' constants list).
- [minor] Supported, and more strongly than the raw says. No ...: Post-hoc text composition: 8 of 32 leak texts on slate/prism, 24 on control pairs (maple/cedar, granite/lattice, plaza/saddle), 'conditional on the local script'; 'raw cosine flips sign' status reproduced.

### Pass 2: 96 claims checked; regenerates identically: True; redaction clean: True; findings 8 (1 substantive)
- [substantive] false arithmetic. The midpoint of 1.06 and 1.07 is ...: Figures row 'max 1.06 (B)' note, and Values-check row F2: '1.0625 is the exact midpoint of 1.06 and 1.07: '1.06' matches round-half-even or truncation; half-up would give 1.07'
- [minor] the source is correct, but the row omits where the ...: Figures row 'scaling with installation strength (smoke 0.5 → trained 1.75)', marked log-only, gives only the smoke raw stdout as its source
- [minor] both cited phrases span two lines, so each locator gives ...: Locators: 'G2 B 1.02/1.03' at archive@bbc9ffe:479; 'untriggered tags carry no leak' at FINDINGS-3.md@bbc9ffe:143
- [minor] overstated interpretation. 'per replicate' can equally ...: Section 1 / Summary (ii): "'Per replicate' points the other way", i.e. the pre-registered G1 text is ambiguous between the swing form and the per-replicate form
- [minor] coverage gap relative to the sentence N9 defends. The ...: No Figures row for 'rank-8 adapter'
- [minor] incomplete per rule 6. The comparator is the maximum, ...: Companion G3: 'G3 12 vs floor 103', status reproduced; section 3 calls 103.150 the 'max control-pair displacement'
- [minor] borderline status. The raw values come from the JSON's ...: Figures row 'raw cosine flips sign with the assignment', status reproduced
- [minor] slightly overstated. A 1/16 grid follows from bf16 only ...: Section 2a(1): 'This is what label logits held at bfloat16 precision would produce'

### Fix 1: 13 dispositions: fixed 13

### Fix 2: 8 dispositions: fixed 8

### Final check: applied correctly 8/8; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: The R2-1 Figures-row cell contradicts itself. It says '1.0625 rounds to 1.06 at 2 dp under any standard rule' and then '...only directed rounding up gives 1.07'. Directed rounding up (ceiling / round-up) is a standard IEEE/Decimal rule, so the ... Proposed fix: Change 'under any standard rule' to 'under any round-to-nearest rule (half-up, half-even, half-down) and under truncation' in the Figures row and in its echoes in F2 and R2-1, or drop the word ...
- **open (minor, not applied)**: The softened Values-check intros still claim slightly more than is true. Pass 1 says the right-hand numbers are computed by this run 'except the pass-1 values that rows 2 and 8 quote', but row 4's 'bar 0.10 and n = 32' is a string literal. Round 2 says ... Proposed fix: Interpolate row 4's bar and n from leakage.bar and leakage.n, and R2-6's 28 from G1.n_ctrl_pairs (or assert they equal it). Alternatively, list them among the intro's exceptions.
- **open (minor, not applied)**: The new rank-8 row's source cites archive:613 for 'rank 8 / last 8 layers', but in the record the word 'layers' is on :614. This is the same pattern R2-3 fixed, and the fixer said the sweep was complete. Proposed fix: Cite archive/RESULTS-cycles3-4.md@bbc9ffe:613-614 in the row, in VC R2-5 and in JSON locators.prereg_rank, or leave it as is with a note that the numerals are on :613.

## N10

### Pass 1: 58 claims checked; regenerates identically: True; redaction clean: True; findings 8 (2 substantive)
- [substantive] Partly wrong. In the record, 'calibration' next to horn ...: Raw §7 point 5: "'calibration' -- the record calls it the '(b) DV diagnostic' ... The term is a gloss, consistent with use." Also the raw's §2 and the summary: 'The design seat's belief was wrong.'
- [substantive] Incomplete. The preprint has a third carrier at :222, ...: Raw §7 says the preprint has two carriers of the figure, :31 and :192. The PI items cover only those two.
- [minor] The value is right but the label overclaims. 0.511 is r² ...: Figures row 'R² on the log-odds scale of y (what 'label logits' would carry)' = 0.511. The PI item offers 'or quote ≈ 0.51 on the log-odds scale' as an alternative wording for 'label logits'.
- [minor] The raw's table and the builder summary differ. The ...: The Figures table is what N1's ledger reads, and the builder summary lists figure rows.
- [minor] The reading is reasonable, but the locator for the ...: §2: 'C2' is read as cycle 2 because FINDINGS-2 'is the second design cycle, FINDINGS-2.md@bbc9ffe:1; its window 2026-08-01 to 2026-08-06 contains the diagnostic'.
- [minor] The attribution is confirmed, but 'right' is slightly ...: Figures row for the archive parenthetical: its Spearman +0.68 and log-odds +0.72 'round the Δlogit row's (+0.675 / +0.715) ... read as the decisive arm's values they are right; looks like transcription'.
- [minor] The conclusion holds, but the stated scope is narrower ...: §1d: the JSON search for an R² field covers only data/e2b and data/e2d (39 files), and concludes that no JSON carries the R².
- [minor] The arithmetic is correct. The sampling model is ...: Post-hoc Fisher-z CI R² ∈ [0.263, 0.735] and t = 5.916, p = 1.6e-06, labeled 'post-hoc; normal theory'.

### Pass 2: 74 claims checked; regenerates identically: True; redaction clean: True; findings 5 (0 substantive)
- [minor] Wrong line numbers. With `git show bbc9ffe:<path> | cat ...: §1a's 'other R²' locators for results/raw/2026-08-04_slice2_gating_checks.txt@bbc9ffe:28, :29 and :34, and §4's cross-check locator results/raw/2026-08-05_slice3_dv_powered.txt@bbc9ffe:10-42.
- [minor] Incomplete. FINDINGS-2.md@bbc9ffe:51 carries the same ...: §1a/§1b/§2 list every carrier of the figure: 'Summary carriers' are archive :1981, FINDINGS-2 :129, :175, :244 and PROPOSAL-h :65.
- [minor] The raw misses a closer homonym. The two-horns leakage ...: §1c: PROPOSAL-e:221-224/247-248 make '(b)'s post-mortem' 'the calibration source' for the two-horns standing leakage gate. The homonym rows list only cycles3-4:483 ('mean 0.53') and the H-calibration π̂_d.
- [minor] Not reproducible from the repository. The command passes ...: Header 'Command' and the raw's closing paragraph (the number-by-number comparison with the builder's raw).
- [minor] Not pinned. The locator comes from a working-tree `git ...: §3: '.gitignore:113:/data/configs/*' shows the diagnostic JSON is gitignored.

### Fix 1: 8 dispositions: fixed 8

### Fix 2: 5 dispositions: fixed 5

### Final check: applied correctly 5/5; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: §1c's second bullet and the g3 Figures row (the R2-3 edit) say a reader reaches g3 through 'calibration' only by following PROPOSAL-e's indirect 'calibration source'. §1c also says the record attaches 'calibration' to two different things. In fact the ... Proposed fix: In §1c's g3 bullet and the g3 Figures row note, cite archive/RESULTS-cycles3-4.md@bbc9ffe:1242 (g1–g3 named 'calibration gates' in the e2a pre-registration) and :1176. Say that the paragraph-level ...
- **open (minor, not applied)**: R2-1's evidence says the raw 'cites 18 distinct paths with an @bbc9ffe locator, and only 2 of them are among the 101'. The count leaves out .gitignore@bbc9ffe, which the R2-5 edit itself added. Proposed fix: Widen the regex to admit dotfiles (or any extension) and print 19. Alternatively, word it as '18 distinct *.md|*.txt|*.json paths, plus .gitignore, which numbers identically under both splits ...
- **open (minor, not applied)**: The fixer's summary has two inaccuracies that are not in the committed-path files: 'results/raw/...horn1.md, 329 lines', and the Figures table 'gains two rows'. Proposed fix: Correct the summary: 328 lines, and one new Figures row plus the extended FINDINGS-2 row. Optionally have the script's stdout count lines the way wc -l does (len(O) - (O[-1] == '')).

## N14

### Pass 1: 165 claims checked; regenerates identically: True; redaction clean: True; findings 8 (0 substantive)
- [minor] Correct claim, imprecise locator. Line :17 is the ...: Section 2 and note 3: 'f1 has no injected state in any arm (PROPOSAL-f-natural-reinforcer-screen.md@bbc9ffe:17; FINDINGS-4.md@bbc9ffe:15)'
- [minor] Mislabeled for N1. N14's block text (AUDIT@bbc9ffe:116) ...: Figures table, column 'figure as the block writes it': rows 'e2a reward pooled', 'e2a sham pooled', 'f1 CORR pooled 0.000 (maps mirror-cancel)' and 'f1 sham pseudo-Δ .045'
- [minor] Literally true but overstated as a criticism. ...: Note 3: PROPOSAL-h §1's f1 'receipt' 'shows the counterbalance absorbing a state-free label/order artifact; it is not by itself evidence about a vector leak'
- [minor] Attributes a premise the record does not state. ...: Section 6: opposite-signed and ≥0.10 map excursions are common, 'which is the premise of PROPOSAL-j's "A fourth capture is expected and is not a finding"'
- [minor] Arithmetic correct, but one of the 17 is a boundary case ...: Section 6 and the Figures table: '17/22 with a map abs(Δ) ≥ 0.10'
- [minor] Both correct, but each lacks a pinned locator (rule 4).: Section 2: 'target direction: avoid corrupted, one-sided; PROPOSAL-f table row' and section 2 (B3): 'Registered valid targets 48:18:18'
- [minor] Correct, but for e2a the valid set is the frozen ...: Section 1 domain statement: 'n = the arm's VALID sessions ... as each campaign's analyzer removes them'
- [minor] The JSON has interpreter, script sha, stamp and HEAD but ...: JSON header fields

### Pass 2: 165 claims checked; regenerates identically: True; redaction clean: True; findings 5 (1 substantive)
- [substantive] Misleading or contradicted for the two Qwen captures ...: Section 5 reading: 'habit breaks in the Qwen arms lean toward each pair's first-listed tag (pair[0])'. 'No single lean count is significant'. 'In the state arm alone, breaks toward + and breaks toward pair[0] cannot be separated at these counts'. 'Taken ...
- [minor] The numbers are right and the main conclusion stands: ...: B3 DPO reading: 'its breaks do not lean toward pair[0] (4 vs 5 pooled)', and the excursion is 'mostly a forced-order (start-label) imbalance ... rather than a label-identity preference'.
- [minor] Locator is imprecise: the quoted phrase spans two lines.: Section 6: the record read random1's pooled +0.152 as 'noise doing its criterion job' (archive/RESULTS-cycles3-4.md@bbc9ffe:684).
- [minor] Status is mixed. The ≈0.10 scale is a record prose ...: Figures row 'Δ ≈ 0.10 scale (rule 12; preprint §5.6)' has status computed-new.
- [minor] Cross-reference omission. N5 reports a delivery artifact ...: f1 CORR is presented as a label-artifact capture on a 'clean vs corrupted' contrast whose property is fixed across maps (section 4 basis; note 6 cross-references N5 only for the pooled figure).

### Fix 1: 8 dispositions: fixed 8

### Fix 2: 5 dispositions: fixed 5

### Final check: applied correctly 5/5; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: Section 5's reading bullet (raw md line 387) now says 'So on Qwen 'label artifact' names a demonstrated within-campaign effect' and calls the within-pair effect 'distinguishable'. The same bullet then says those p values are post-hoc and descriptive (rule 11). Proposed fix: Replace 'names a demonstrated within-campaign effect, a tag-identity prior' with 'names a tag-identity prior that the record measured independently (H3 C2) and that is visible post-hoc in each ...
- **open (minor, not applied)**: The new bullet 'The state arm, separated by pair' (raw md line 385) says that outside maple/cedar the state arm's breaks go 'toward + in both maps, the direction a state effect would take' and that 'both state-arm maps are ≥ 0 (+0.0122, +0.0750)'. It gives ... Proposed fix: Add one clause after '(+0.0122, +0.0750)': 'the same both-maps-≥0 shape appears without maple/cedar in f1's sham (+0.0556 / +0.1429, no breaks) and f1 CORR (+0.0652 / +0.0000), neither of which ...

## N16

### Pass 1: 194 claims checked; regenerates identically: True; redaction clean: True; findings 13 (4 substantive)
- [substantive] incomplete or misattributed. 6e49242 (2026-08-21) only ...: e2a row, 'commit(s) that fixed them': 'pre-reg 1970b50; template amendment 3637c06; data d49bb5d; ban file admitted 6e49242'. Section 2 says the record fixes e2a/g2/f1 parameters 'through the pre-registration (1970b50), the template amendment (3637c06), ...
- [substantive] omission. The B2-r decoding of record was pre-registered ...: B2-r row, 'commit(s) that fixed them': 'runner scripts/box_b2r_campaign.py@b6e8f3f; stamped head 745c196'. No pre-registration locator is given for B2-r's decoding.
- [substantive] wrong run commit. The record says D1 ran the code at ...: e2d D1 row: max tokens is code-fixed at 'valence_core/e2d/runner.py@db5b09c:192, valence_core/session_e2a.py@db5b09c:90'; the ban at scripts/e2d_sessions.py@db5b09c:133; the commit column reads 'runner valence_core/e2d/runner.py + scripts/e2d_sessions.py ...
- [substantive] status mislabelled, and inconsistent within the raw. The ...: Main table, g2r2 corpus row: temperature '0.7 [log-only: clone docstring jlens-qwen36/scripts/e2a_g2_discriminability.py:11; no artifact field]', source tier 'T L'.
- [minor] Four rows have unescaped '|' inside cells ...: Section 6 Figures table (feeds N1): rows 'e2a: seed policy', 'g2r2 corpus: seed policy', 'f1: seed policy' and 'Qwen: EOS id in the ban list'.
- [minor] The source column names no artifact, so N1 cannot use ...: Section 6 rows for k1 and format F0/F1/F2 (15 rows) give sources such as 'temp / identity.temp', 'sessions[].rounds[].seed', 'sessions[].rounds[].stop_reason'.
- [minor] Some (DV, parameter) cells in the main table have no ...: Section 6 Figures table as the feed for N1 'covers every figure'.
- [minor] Correct, but the domain is unstated (rule 6). The 267 ...: B3 seed policy: 'the same (arm, idx) draws the same seeds ... (267/267 cross-stage pairs equal)'.
- [minor] Wrong line. :293 is the stop condition. The default is ...: B3 stop cell: 'code-fixed, adapter default stop_newline=True, valence_core/adapters/olmo_hf.py@bbc9ffe:293'.
- [minor] Two omissions. (a) 6 strings giving 9 distinct ids means ...: OLMo ban list: '9 ids from 6 strings at every stage' (A2); B3 'n_ids 9, sha16 2dd86a453a2275ef'; A2 sha16 c0297fa8ee89d29d, listed side by side in the appendix.
- [minor] Off-target locator for e2a. :1671 is about f1's and m's ...: e2a and f1 'EOS banned' cite results/raw/2026-10-07_m-gport_differences.md@bbc9ffe:1671.
- [minor] Slight overclaim. The tally reproduces 'newline' only, ...: e2d D1/D2/D3 stop cells: 'newline or cap; EOS banned [reproduced: stop_reason tally ...]'. Ban cells: 'rebuilt from the live tokenizer [reproduced: 12 ids / 12 strings]'.
- [minor] Correct only with rename-following. At bfa87a5 the file ...: Section 2: 'session_e2a STOP_CAP = 60 | bfa87a5', under the header 'git log -S over bbc9ffe's history; oldest hit'.

### Pass 2: 225 claims checked; regenerates identically: True; redaction clean: True; findings 8 (0 substantive)
- [minor] wrong locators (off by two lines); values and statuses ...: Log locators results/raw/2026-08-09_e2a_full.txt@bbc9ffe:7 (e2a ban list printed, 'ban list 12 ids sha 9a2f0744f81ac930'), results/raw/2026-08-09_e2a_g2r2.txt@bbc9ffe:5 (g2r2 'config v3: ban 12 ids sha ...') and ...
- [minor] selective citation; the underlying claim (every B2/B2-r ...: Section 5(c): 'N2's own cap-emulation diagnostics are consistent with this (its 2(d) base row, N2 raw line 220 at read: B2-r controls re-encoded to at most 100 tokens and B2 texts to at most 60: True)'
- [minor] incomplete: e2d's governing pre-registration is not cited: e2d rows, 'commit(s) that fixed them' (code 4e41288 / a274ecd / e58dfca), and the section-2 and PI-item paragraph on what decoding was pre-registered
- [minor] value confirmed (1110); cause mislabelled: N4 cross-check: N4's 1111 generated rounds for data/e2b/h1_sessions.json 'Looks like transcription of the n_rounds field'
- [minor] defensible but weak; already disclosed: e2a: temperature 0.7, status log-only, source valence_core/e2d/config.py@bbc9ffe:41
- [minor] locator covers only part of the printed rule: e2a stop cell: 'newline-after-content or cap 60 [log-only: archive/RESULTS-cycles3-4.md@bbc9ffe:1049]'
- [minor] compound figure: only half is reproduced: B2: seed policy, status reproduced ('args.seed 20260823 (allocation permutation; generation 20260823 + n)')
- [minor] wording ambiguous; the replay is correct: e2a seed cell: 'draws permutation(16), integers(4) per round, then per forced round a seed ...'

### Fix 1: 17 dispositions: disclosed 1, fixed 15, rejected-with-reason 1
- rejected-with-reason: 10b the checker's claim that the sub-word question is 'a decoding fact the record cannot resolve': The record resolves it. The m-v1.10 referent-check raw at bbc9ffe lists the nine ids and says five are sub-word tokens. This script recomputes both stored sha16s from those ids, and both match at ...
- disclosed: self-found: B2 decoding was not pre-registered; e2a_full.txt's stale 'uncached path (g1)' banner: LOCK-g contains no temperature, max-token or top-p/top-k string (computed); its only 'greedy' is the roster search at :40,42. This is stated in the B2 commit cell and a PI item. The e2a path cell ...

### Fix 2: 8 dispositions: disclosed 1, fixed 7
- disclosed: R2-5 (minor): e2a's temperature is 'log-only' on the strength of a later code comment.: No status change, as the fix says. Confirmed: the only committed statement is valence_core/e2d/config.py@bbc9ffe:41, introduced at 4e41288 (2026-09-01). The e2a data commit is d49bb5d ...

### Final check: applied correctly 8/8; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: The round-2 text pins 'newline stop, cap 60' to archive/RESULTS-cycles3-4.md@bbc9ffe:1049. In the section-1 e2a stop cell it reads ':1049 (newline stop, cap 60)'. The R2-6 detail reads ':1049 (the amendment: newline stop, cap 60)'. The section-6 'e2a: stop ... Proposed fix: Make LOG['e2a_amend_stop'] a range, from the '(a) Stop discipline:' line to the 'backstop cap 60 tokens' line (giving :1049-1050), and rerun. Every cell that uses it updates, with no other change.
- **open (minor, not applied)**: The R2-1 detail prints '(each a bare '\r': True)'. Proposed fix: Compute bareness per file (t.count('\r') > t.count('\r\n')) and print that, or relabel the printed boolean as 'the only such separator is \r'.
- **open (minor, not applied)**: The R2-1 detail says 'Of the 146 record files this script reads, 12 contain a splitlines-only separator'. The fixer's summary repeats '146 record files'. Proposed fix: Reword as '146 (path, commit) reads of 115 record files', or count distinct paths.
- **open (minor, not applied)**: The R2-1 detail's 'cited text' excerpt for results/raw/2026-08-09_e2a_full.txt@bbc9ffe:5 shows 'v3 roster [('slate', 'prism'), ('maple', 'cedar'), ('granite...'. That is not the text the locator is cited for. Proposed fix: Print the regex match, or the line's tail around it (e.g. re.search(pattern, line).group(0)), instead of the first 60 characters.

## N17

### Pass 1: 127 claims checked; regenerates identically: True; redaction clean: True; findings 14 (3 substantive)
- [substantive] Wrong on the raw's own static reading. patch_gdn() ...: README paragraph (raw §6) and §2e summary: the port's patch makes 'the layer gradient-checkpointed', and the forward is wrapped in a custom function with a Metal backward.
- [substantive] Contradicted by committed OLMo artifacts. The 4-bit and ...: README last sentence: 'The OLMo results are bf16 throughout and carry none of these caveats.'
- [substantive] This states the superseded v2 rule 2 ...: README: 'The lab's rules therefore require the uncached path for greedy readouts under high-norm steering and allow sampled steered generation on the cached path only behind a next-token KL gate re-run for each direction family and dose.'
- [minor] Wrong line numbers. Under 'git show bbc9ffe:<path> | sed ...: Locators results/raw/2026-08-09_e2a_g1.txt@bbc9ffe:6-7 and results/raw/2026-08-09_e2a_g1r.txt@bbc9ffe:6-7 (§5 and the Figures row for g1). These feed N1's ledger.
- [minor] Misattributed. AUDIT-note-release-v1_2.md contains no ...: Figures row note: 'the block's 'g1/g1r ... 7.11e-4 / 7.39e-4' are g1r's values'.
- [minor] Imprecise. No g1 (v1) artifact was ever committed. The ...: §5: 'g1 (v1 templates) ... [log-only: the committed artifact was overwritten by g1r]'.
- [minor] Broader than the cited support. That provenance is from ...: README: 'Every Qwen result here comes from ... run with MLX 0.31.2 and mlx-lm 0.31.3'. The clause map sources this to data/regression/oracle_rule26.json:provenance (reproduced).
- [minor] Line 83 does not state that purpose. It does describe ...: §2a / clause map: archive/CLAUDE-cycle1-2.md@bbc9ffe:83 is cited for 'purpose: differentiability for Jacobian-lens fitting', and the raw says 'The record never describes the patch's mechanics'.
- [minor] I agree with the static reading, having traced ...: F1's scope: on the static reading, every uncached forward ('choice reads, uncached positional generation, extraction and probe readouts') runs the fused kernel inside the custom function.
- [minor] The count is right, but the table does not name its ...: §2f / Figures row 'lab edits to the clone: ... added 57 files; kernel-defining lines 0'.
- [minor] Loose wording. g1r passed. Its KLs bound distributional ...: §3: the g1r first-token KLs (7.1064e-4 / 7.3906e-4) are listed as 'Later instances of the same floor at the e2a dose'.
- [minor] Partly true. Exactly 0.0 is the refactored core's bar ...: README: 'The choice-read check re-runs the identical unsteered forward on identical token ids and requires a KL of exactly 0.0'.
- [minor] The values reproduce. Rule 6 is incomplete in the table: ...: Floor-2 Figures rows (D_cond, control swings, label-pair cosines).
- [minor] The script refuses any --out or --json-out outside ...: Reproducibility of the run: scripts take --out with results/raw defaults; header 'Command' is the exact command.

### Pass 2: 235 claims checked; regenerates identically: True; redaction clean: True; findings 10 (2 substantive)
- [substantive] discrepant. The artifact exists, and the gate ran on ...: Raw section 3 (line 202) says the OLMo first-token gate is '[log-only; no artifact of the OLMo first-token gate under data/olmo at the pin]'. F1 and the section-3 Reading say the OLMo multi-token divergences came 'after the OLMo first-token gate had found ...
- [substantive] Referent incomplete; it can now be named. The phrase is ...: Section 5 says the phrase 'verified against an untouched model' 'is the note's phrase ... not the record's'. F6 says it 'does not occur in the record'. The figure row reads '1 hit(s), the block only', status not found.
- [minor] Contradicted by the README and by the raw's own clause map.: Raw header: 'a README sentence never depends on the clone'. The 'where the patch lives' row note says 'the README must not depend on it'.
- [minor] Broader than the record. For the cycle 1-4 results it ...: README: 'Every Qwen result here comes from ... (Hugging Face revision c000ac2c), run with MLX 0.31.2 and mlx-lm 0.31.3 (the versions the artifacts record, installed when the project was set up)'.
- [minor] Present-tense restatement of v2 rule 2, which v3.1 ...: README: 'The lab's rules therefore require the uncached path for greedy readouts under high-norm steering.'
- [minor] Overstated. The floor is near-tie argmax flips under ...: Section 3 labels the e2d T-step non-identities '(the floor's instances)'.
- [minor] The record's interpretation is stated as a measured fact.: README: 'the high-strain state leaves the next token near an argmax tie, where small floating-point differences between the two computation paths flip it'.
- [minor] Two README figures have no row, and one row mixes statuses.: The Figures table covers every figure the README paragraph carries.
- [minor] Unpinned referent: the routing prompt is not in the ...: F4 and the g1 figure note cite 'The task text's "g1/g1r kernel gate KL 7.11e-4 / 7.39e-4"'.
- [minor] The summary is stale. The raw on disk (sha256 ...: Builder summary: '28 figure rows: 14 reproduced, 5 log-only, 7 computed-new, 2 not found'.

### Fix 1: 14 dispositions: fixed 14

### Fix 2: 10 dispositions: disclosed 1, fixed 9
- disclosed: 10 (minor) The builder summary ('28 figure rows ...') is stale: That summary is not in this item's files. The raw computes its counts from its own table on every run (this run: 40 rows; 21 reproduced, 8 log-only, 9 computed-new, 2 not found). The disposition ...

### Final check: applied correctly 10/10; regenerates identically: True; redaction clean: True
- **open (minor, not applied)**: Section 5, F6 and the figure note say the source of 'verified against an untouched model' is the preprint's earlier wording. The search behind that claim covered only the preprint drafts (script:1432-1433 globs archive/PREPRINT-v1_0-draft.pre-patch-v*.md ... Proposed fix: Widen the on-disk search to the whole working tree outside the clone and list both occurrences (pre-patch-v2:109 and PROPOSAL-m v1.2:53, both untracked, both for choice_read(verify=True)). Then ...
- **open (minor, not applied)**: README: 'the versions recorded by every Qwen artifact that names its model, the first committed on 15 August 2026'. Proposed fix: Reword to 'the versions every Qwen artifact that names its model records, first recorded on 15 August 2026' (or 'recorded from 15 August 2026 on'). Optionally note that the 12 August oracle ...
- **open (minor, not applied)**: The new clause row ('the near-tie account is the record's reading') and 11b row 7 locate the record's 'Read:' at archive/RESULTS-cycle1-2.md@bbc9ffe:1682-1683. Proposed fix: Use a_read+6..a_read+7, so the locator reads archive/RESULTS-cycle1-2.md@bbc9ffe:1683-1684, in the clause row and in 11b row 7. Also consider extending the section-3 quote (1677-1683) to 1684 so ...
- **open (minor, not applied)**: README: 'The record reads this as the high-strain state leaving the next token near an argmax tie, where small floating-point differences between the two computation paths flip it.' Proposed fix: End the attribution at the argmax tie, e.g. 'The record reads this as the high-strain state leaving the next token near an argmax tie, which numeric noise then flips.' Keep 'between the two ...
- **open (minor, not applied)**: 11b row 4's detail quotes the new README wording with a literal placeholder: '... the first committed on <date>; ...'. Proposed fix: Interpolate the same date string the paragraph uses (time.strftime of first_lv), or quote the final README wording after applying new problem 2's rewording.
- **open (minor, not applied)**: After its attribution was dropped, F4 says 'A text that labels the pair g1 or g1/g1r should say g1r' with no referent, while the raw's own section-3 quote shows the record doing exactly that. Proposed fix: Pin F4 to these record lines. Say the record names the gate by its artifact path (g1_kernel_gate.json), so 'g1' in those lines means the g1r (v2) gate, and that public text should say g1r or 'the ...

