# AUDIT-note-release v1.2 — pressure-test and release-scrub block for the Research Note

*Design seat, 2026-10-05; v1.1 2026-10-06 after the Digest seat's F1/F2 renders (FIGURE-REVIEW-2026-10-06.md); v1.2 2026-10-07: one change — N12(iii) no longer writes the continuity password, since this document is committed to a repository that is about to be public; the PI supplies it to Code out of band. This document goes to root and is committed with the first raw it produces, so that every `results/raw/<stamp>_note-N*` file cites a document with a sha in the record. Changes from v1.0: N1 now covers every number in F1 and F2; N2(v) computes corrected d′ and a test of hits against false alarms per stage for both arms and both datasets, and the greedy row; N2(vi) must state which configuration the "theirs" per-stage values were recovered from; N3(i) cites the stored shuffled-label null and N3(ii) is reduced to confirming it; N4(i) carries the design seat's arithmetic (55/102, share − ½, p = 0.24422) for Code to confirm against the record's fields, and the preprint's "54 of 101" and "half the difference between break rates" sentences to reconcile. For the PI to route to Code. This is an audit block, not a pre-registration: it reads the record and reproduces figures from committed artifacts; it changes no analyzer, no criterion, no label, and no pre-registration. It does not touch the PROPOSAL-m build or the k arc. Every item names what it defends (the objection in NOTE-HEAT-PLAN §6b), its referents, its procedure, its output, its pass condition, and what happens on failure. Code keeps its own `date -u` stamps; calendar dates in this document are the PI's. Repository facts supersede this document; where a referent below is wrong, Code names the right one in the raw and proceeds — a wrong referent here is a note to fix, not a STOP, because nothing downstream is built from it.*

**Routing suggestion for the PI:** a fresh Code thread, so the STOP-8 thread's state for PROPOSAL-m v1.11 is undisturbed. Tier 1 is blocking for the note; Tier 2 hedges or strengthens sentences; Tier 3 is footnotes. Rough size: Tier 1 is on the order of three to four Code sessions, dominated by N3 and N12.

## 0. Rules for this block

1. **Read-only on the record.** No file under `valence_core/`, `scripts/` (existing), `data/`, or any `PROPOSAL-*`/`LOCK-*`/`FINDINGS-*` is modified. New code goes under `scripts/audit_note_*.py` and writes only to `results/raw/`.
2. **Reproduce from committed artifacts, not from memory or chat.** A figure reproduces if a script reading committed JSON/npz prints it. A figure that exists only in a log entry and cannot be recomputed from committed artifacts is reported as `[log-only]` with the log locator, and the note's sentence that carries it is downgraded (N1 §).
3. **A reproduction that would need a code change is a STOP on that item, not a fix.** Report the discrepancy and the suspected cause; the design seat and PI decide.
4. **Every rate names its domain; every p its test; every AUC its probe, layer, contrast and CV scheme.** Outputs that omit any of these are incomplete.
5. **No model inference in Tier 1** except N11's regression suite (model-free) and N3(ii)–(iv), which re-fit probes on committed residual arrays if those arrays are local (`data/echo/*.npz` stay local by design; if absent on the machine running the audit, N3(ii)–(iv) are reported `[not run: arrays not local]` and the note's §9 "linear probe" objection keeps its queue wording).
6. **One commit at the end** carrying all raws, the provenance table, the README-for-readers, and the tag. The tag name is the PI's; the design seat suggests `note-2026-10-v1`. The tag points at the commit the note's figures come from, which N1 identifies; if that is not HEAD, the README and raws are committed on top and the tag is placed on that commit regardless.

## Tier 1 — blocking for posting

### N1. Claims ledger

*Defends:* everything; O1 and every "your number is wrong" comment.
*Referents:* RESEARCH-NOTE-v0_2-draft.md (every numeral and every quoted figure) and the Digest seat's F1/F2 SVGs of 2026-10-06 (every plotted value and every annotation number — the two were rendered from v0.1 and the record, and where they disagree with the preprint the record wins; v0.2 already applies the four disagreements the design seat found); PREPRINT-v1_1-draft.md (project copy) and `PREPRINT-v1_0-draft.md` at root (post-patch-v4 copy, sha `d6431e97…222b8`); `RESULTS.md`; `archive/RESULTS-cycle1-2.md`, `archive/RESULTS-cycles3-4.md`; `FINDINGS*.md`; `scripts/paper_data.py` (its sourcing pattern, not its code).
*Procedure:* build `results/raw/<stamp>_note-claims-ledger.md` with one row per figure in the note: the figure as written; its source (`RESULTS.md@<commit>:<line>` or `archive/...@<commit>:<line>` or a `data/` artifact path with the field name); the reproducing script and the printed value (from the N2–N10, N14–N16 items below, cross-referenced by item id); status ∈ {reproduced, log-only, not found, discrepant}. Also record the commit at which the last of the note's figures entered the record — that is the tag commit.
*Pass:* every figure is `reproduced` or `log-only` with a locator. *On fail:* a `not found` figure is cut from the note; a `discrepant` figure is corrected in the note to the reproduced value if the discrepancy is transcription, and is a STOP on that item if it is not.

### N2. Introspection replication and the criterion-shift claim

*Defends:* O9; the note's link 4 and §8; the F2 figure.
*Referents:* `scripts/b2_analyze.py`, `scripts/b2r_analyze.py`, `scripts/box_b2_detection.py`, `scripts/box_b2r_campaign.py`; `valence_core/detection.py`, `valence_core/detection_v2.py`; `data/configs/b2_concepts.json`, `data/configs/b2_framing.json`, `data/configs/scorer_v3_spec.json`; `data/olmo/*.json` (per-stage detection outputs); the B2/B2-r VERDICTS entries in `RESULTS.md`.
*Procedure:*
(i) Reproduce from committed outputs: per-stage FPR with numerator/denominator (SFT 0.200; DPO 0.000; instruct 0.000; base 0.431 = 58/96); the fidelity-of-text arm's distance from the template arm (≤ 2.5 points); the decoding parameters used (temperature, top-p, max tokens, seed policy) and Macar's, side by side.
(ii) Reproduce the greedy run: confirm it exists as a committed artifact with its own stamp, that the protocol is otherwise identical, and that it yields zero detection claims at every stage; report n per stage.
(iii) Reproduce "178 decidable trials at DPO and instruct at qualified doses → zero detection claims of any kind" with the decidability rule named, and the SFT discrimination figure (+0.096 with its interval and test).
(iv) Name the scorer of record for each figure (detection.py / detection_v2.py / contentclass v3/v4 / audit_v3) and confirm the note's figures are all from one scorer version; if two scorer versions give different per-stage FPRs, report both.
(v) Produce the F2 data: per-stage (FPR, TPR) for ours — both arms: the criterion arm (`b2r_analysis.json` → g3a; 25/58, 17/85, 0/91, 0/91) and the exploration arm (`b2r_explore_{sft,dpo,instruct}.json`; 12/40 hits / 9/44 FA at SFT, 0/43 / 0/45 at DPO, 0/44 / 0/46 at instruct, as F2 labels them) — and for the source's per-stage values; for every point, the corrected d′ (log-linear: (H + ½)/(N_s + 1), (FA + ½)/(N_n + 1)) and criterion c, and a one-sided Fisher exact test of hits against false alarms with its p; the greedy run as its own row (zero claims at every stage, with its ns). The design seat's arithmetic to be replaced, not trusted: theirs base d′ ≈ −1.9, SFT ≈ −0.3, DPO ≈ +0.6 (p ≈ .11 on 0 of ~80 controls), instruct ≈ +0.15 (p ≈ .5), under an assumed 800/80 per configuration; ours SFT ≈ +0.3 (p ≈ .22), DPO and instruct ≈ 0 by construction; upper 95% bound on a per-stage hit rate given 0/43 ≈ .067. Write `results/raw/<stamp>_note-N2-roc.json` for the Draftsman seat; the post version of F2 annotates every point with these.
(vi) Discharge the **[verify]** on the source's per-stage hit rates: the note now carries 0.001 / 0.149 / 0.029 / 0.009 as the design seat's recovery from arXiv:2603.21396 App. C Fig. 21 via ADDENDUM-g3-b2r-v1.2.md §0.2. State, from that addendum and the source: which (layer, α) configuration each per-stage value comes from, or whether it is an aggregate over the L ∈ {25, 32, 38, 45, 51} × α ∈ {1, 2, 4, 8} grid; the n injected and n control per cell; whether the values were read from a table or digitized from a figure. If a per-stage value is a best-of-grid selection, say so — the note's comparison then names it as such. If the source states per-stage TPR in text, quote it; if it does not, the note's sentence is rewritten to what can be read with the recovery method named.
*Pass:* (i)–(iii) reproduce; (iv) single scorer of record; (vi) resolved either way. *On fail:* (ii) failing is a STOP on link 4's ROC paragraph — the heat plan withholds it; (vi) unresolved → the sentence is cut.

### N3. Echo-probe robustness

*Defends:* O3, O4; link 3 and §6.
*Referents:* `scripts/recon_echo.py`; `valence_core/echo/probe.py`, `spans.py`, `maskedprefix.py`, `k1.py`; `data/echo/*.json` (probe tables, span provenance, fingerprints); `data/echo/*.npz` (local only); the RECON BLOCK 2026-09-05 entries in `RESULTS.md`; `PROPOSAL-k-echo-channel.md` for the bars' provenance.
*Procedure:*
(i) From committed JSON: reproduce the sign-at-first-free-choice AUC range (.94–.995) with layer and CV scheme; the primacy profile (.89 first round, .68 fourth); the binding AUC at the label token (≥ .998, L51–61) and at the decision token (.50–.55), with the exact positions ("nine positions before") and the CV scheme; the leakage figures (0–3 of 102 sign flips; median |Δ| ≤ .10 logit; pseudo-shift ±.02–.03 toward the first block's label; the random-direction comparison). Also the PROPOSAL-k Stage 1 figures the note carries (sign median .861 against the .90 bar; binding .88 → .64) from `data/k/*.json` via `scripts/k1_analyze.py`, read-only — the k arc's three open questions are not touched.
(i-b) The stored shuffled-label null: F1's link-3 panel reads `results/raw/2026-09-06_recon_echo_stageC_analysis.txt` (102 sessions, grouped 10-fold, 200 shuffles) and plots a "shuffle-95 null" at ≈ .57–.59 across layers, binding at the first label ≈ 1.0 from L51 on, at the second label .81–.96, and at the choice read .50–.55. Confirm those four series from the committed JSON under `data/echo/` (not from the raw text), and state the CV scheme and shuffle count as stored. The note's link-3 sentence now says "≈ 1.0 at the first label … .81–.96 at the second … below the shuffled-label 95th percentile of ≈ .58"; if the JSON disagrees with the raw text, the JSON wins and the sentence follows it.
(ii) Permutation null, extended only if cheap: 1,000 shuffles at the label tokens and the decision token with the same grouped CV, reporting mean and 95th percentile; otherwise the stored 200-shuffle null stands and is cited as such. Requires the local arrays.
(iii) Nonlinear read at the decision token: a small MLP (one hidden layer, width ≤ 64, early stopping) and an RBF kernel classifier, same CV as (i), same layers; report AUC with its permutation 95th percentile. Either outcome is reported; neither changes a label.
(iv) Layer sweep at the decision token, linear, L44–L61, to show the .50–.55 is not a one-layer accident.
(v) Random-direction control for the binding read: the same probe on the random-direction sessions, if those exist in the recon set; otherwise state that they don't.
*Output:* `results/raw/<stamp>_note-N3-echo-robustness.md` + JSON.
*Pass:* (i) reproduces. (ii)–(v) are reported, not passed; if (iii) finds the binding at the decision token above its permutation ceiling, link 3's sentence stays ("in any linear functional") and a one-line addition states the nonlinear result. *On fail:* (i) not reproducing is a STOP on link 3.

### N4. e2a figures, MDE, and the disclosures

*Defends:* O1, O5; link 5 e2a; the 311/360 and cached-generation disclosures (review cards 9 and 10).
*Referents:* `scripts/e2a_recount.py`; `valence_core/session_e2a.py`; `data/e2a/*.json`, `*.jsonl`; `data/configs/e2a_ban_list.json`; the e2a VERDICTS entry (design seat's belief: `archive/RESULTS-cycles3-4.md`; Code locates); `scripts/box_cached_gen_smoke.py` for the cached-path identity check.
*Procedure:*
(i) Reproduce from `data/e2a/analysis.json`: the definition of Δ as the record's field defines it, and the counts. The design seat's arithmetic, to confirm or refute: Δ = share of first free choices toward the state label minus ½; state arm 55 of 102 → +0.0392, one-sided exact-binomial P(X ≥ 55 | 102, ½) = 0.24422, which is the stored p to five decimals; sham 19/37 → +0.0135; random-1 15/23 → +0.1522 (the "largest pseudo-Δ"); random-2 12/22 → +0.0455 — every arm integer under this definition and none under "(approach − avoid)/n". Two sentences to reconcile against the field: the preprint's "54 of 101 valid sessions" (which reproduces neither +0.039 nor p = 0.244 under any definition — a transcription error, or a different n the record explains) and the preprint's "Δ_first is half the difference between the state and sham arms' break rates" (a different quantity; state whether it is a definition, a mechanism gloss, or an error). Also: map-level +0.104 / −0.031; sham-arm map-level +0.111 / −0.079; the approach-probability interval ≈ [.44, .64] with its method (Wilson on 55/102 gives it); first-pick habit 83.4%; and the control-arm sizes 37/23/22, which the note now states. F1's link-5 y-axis label reads "(approach − avoid)"; the post version is relabeled to the record's definition.
(ii) MDE: at n = 101, α as pre-registered, power .80, the minimum detectable first-choice effect under the registered test; and the same at the sham-envelope criterion.
(iii) 311 vs 360: reproduce "311 distinct verified forward passes at KL = 0" and state in one sentence why 360 was the earlier count (card 10), so the note can carry the right number with its gloss.
(iv) Cached-generation disclosure (card 9): state exactly which cells generated on the cached path, what "licensed for first-token identity only" means operationally, and confirm the choice reads are unaffected; one paragraph for the README and the note's scope sentence.
*Output:* `results/raw/<stamp>_note-N4-e2a.md`.
*Pass:* (i) reproduces; (ii)–(iv) delivered. *On fail:* any (i) discrepancy is a STOP on the e2a bullet.

### N11. Fresh-clone smoke test

*Defends:* O10; the repository link itself.
*Referents:* `README.md`; `valence_core/regression/analysis.py`; `.gitattributes`; `.gitignore`.
*Procedure:* clone the tag into an empty directory on a machine (or a clean directory) without the laptop's git filter config; `python -m valence_core.regression.analysis` must print **103/103** reading only committed artifacts; record Python version and the import list that was needed; confirm no path in the note or README points outside the clone; confirm `.gitattributes`'s filter reference does not break checkout on a machine without the filter configured (if it emits warnings, the README says so and gives the one-line fix).
*Output:* `results/raw/<stamp>_note-N11-smoke.txt`.
*Pass:* 103/103 from a fresh clone. *On fail:* STOP on the release; the note posts with the fallback paragraph.

### N12. Release scrub (full history)

*Defends:* the PI; O12 incidentally.
*Referents:* the whole repository including history; `CLAUDE.md`; `.git/config` (local, not released); `scripts/box_*.py`, `scripts/run_*.sh`; `results/raw/*`; `HANDOFF-*.md`; `.gitignore`.
*Procedure:*
(i) Secrets over the *entire history*, not the working tree: run `gitleaks detect --source . --log-opts="--all"` or `trufflehog git file://.` if installable; otherwise `git log -p --all | grep -nEi '(api[_-]?key|secret|token|password|sk-[A-Za-z0-9]|rp_[A-Za-z0-9]|BEGIN (RSA|OPENSSH)|AKIA[0-9A-Z]{16})'`. Any hit in history is a STOP on the release: history rewriting is a PI decision.
(ii) Identifiers: RunPod volume/pod/endpoint ids, SSH key names, hostnames, absolute paths with the username. Absolute paths with `jasondwyer` are not secrets (the author is named) but the README should not depend on them; list every tracked file containing `/Users/` and recommend which to parameterize (none need fixing before release; this is a list).
(iii) The continuity password. The PI supplies it to Code out of band; it is not written in this document, because this document is committed and the repository is about to be public. `git grep -n -i '<password>'` across tracked files and `git log -S'<password>' --all --oneline` across history. If present anywhere, report the file and commit; once the repository is public the password cannot serve its purpose, and the PI decides whether to rotate it or retire the mechanism. Not a release blocker.
(iv) Third-party materials and licenses: `data/configs/b2_concepts.json` and `b2_framing.json` (Macar et al. materials "recovered verbatim at a pinned commit sha") — record the source repository, its license, and the pinned sha; if the license is absent or restrictive, the README attributes and the PI decides. Confirm nothing from the gitignored `jlens-qwen36/` clone is tracked. Confirm no model weights or residual arrays beyond the allowlisted `.npz` files are tracked (`git ls-files | grep npz` against the `.gitignore` allowlist).
(v) Size: `git count-objects -vH`; list tracked files over 50 MB (GitHub warns) and over 100 MB (GitHub refuses) — the design seat expects `data/olmo/a4_instrument_*.npz` (~50 MB each) and `data/e0/e0_b1_markers.npz` (47.5 MB) to be near the warning line; recommend LFS or a release asset for anything over 100 MB.
(vi) Content review of `results/raw/` and `HANDOFF-*.md` for anything that should not be public: third-party personal data, pasted private correspondence, anything the PI marked confidential. Expected: nothing; report the file count reviewed.
(vii) Produce the README-for-readers (§6 of this block).
*Output:* `results/raw/<stamp>_note-N12-scrub.md`.
*Pass:* (i) no hits, or hits resolved by the PI; (iv) licenses recorded; (v) nothing over 100 MB untreated. *On fail:* STOP on the release; fallback paragraph.

### N13. Pre-registration provenance table

*Defends:* O1 (forking paths), O12; it is the single most valuable artifact for this audience.
*Referents:* `PROPOSAL-d`, `-e`, `-f`, `-g`, `-h`, `-j`, `-k` at root; `LOCK-g.md`, `LOCK-h.md`; `ADDENDUM-*.md`; `RESULTS.md` and the archive logs (where the content hashes were recorded before data); git history.
*Procedure:* one row per pre-registration of record and per LOCK: document; version of record; commit hash; commit date (UTC, from git, with the reflog Unix timestamp where the lab's date rule says it governs); content sha256 at that commit; the log line that recorded the hash before data (`RESULTS.md@<commit>:<line>` or archive); the first data-generating commit for the cell it governs; the gap in days. Include the Q1 bet (timestamped 2026-08-18) and both welfare pre-commitments. Verify by recomputing each sha256 from `git show <commit>:<path>`. Known anchors from the design seat's record, to be confirmed not assumed: PROPOSAL-g `72b09a9`; PROPOSAL-k v1.1 `e9b5022`; e2d closure `cef728f`.
*Output:* `results/raw/<stamp>_note-N13-provenance.md` (markdown table for the README and the note's fallback paragraph) and `.json`.
*Pass:* every row's recomputed sha matches the recorded one and the pre-registration commit precedes the first data commit. *On fail:* a row whose order is wrong or whose hash does not match is a STOP on that cell's "pre-registered" wording in the note — the note then says what the record supports.

## Tier 2 — strengthens or hedges a sentence

### N5. f1 natural-reinforcer figures
*Defends:* link 5 f1. *Referents:* `data/f/*.json(l)`; `PROPOSAL-f-natural-reinforcer-screen.md`; `data/configs/f_termination_patterns.json`; the f1 VERDICTS entry. *Procedure:* reproduce the five contrasts (SOLV +.020 p = .44; DIFF −.096 p = .24 with the valid-n floor and the length-preference deflation test; NOV −.066 and its map-inconsistency; CORR 0.000 with maps +.121/−.130; FDBK +.023 with the 93% positive delivery rate); 344/344 sessions and zero pauses; termination attempts ≈ 1% of rounds by arm; exploration share ≈ .50 by arm; the calibrated accuracies .98/.50 for DIFF. State whether the CORR contrast's dose carries any caveat the note should disclose (the PROPOSAL-m "G-CAL 0.12 artifact" question: is there a known artifact at that dose in the f1 record, yes or no). *Output:* `…_note-N5-f1.md`.

### N6. e2b state-present figures
*Defends:* link 5 e2b; O-leakage (§10 item 1 of the note). *Referents:* `data/e2b/*.json`; `scripts/e2b_verdict_analyze.py`, `e2b_h1_gate.py`, `h1_power.py`; `valence_core/e2b/statepresent.py`, `records.py`; `PROPOSAL-h-state-present-choice.md`; `LOCK-h.md`. *Procedure:* reproduce Δ_first = −0.0104 (47/96), shadow 48/96, the three conjuncts and their sham envelope; π̂_d = 0.0172 against 0.0735 with the certification's definition in one sentence (what is displaced, over what set, bounded how); the quarantined primitive's name and what "quarantined" enforces. *Output:* `…_note-N6-e2b.md`.

### N7. OLMo Q1/Q3 and dose ladder
*Defends:* link 1, link 2 (OLMo), link 5 Q3. *Referents:* `scripts/b1_verdict.py`, `b3_analyze.py`, `box_a4_hijack.py`, `box_b3_sessions.py`; `data/olmo/*.json`; `PROPOSAL-g-ontogeny-of-evaluation.md`; `LOCK-g.md`; the Q1 and Q3 VERDICTS entries. *Procedure:* reproduce G_c per stage (+0.78/+1.03/+1.53/+1.56) and sham 0.0; the base pass at L60; per-stage MEDs (0.05 L60; 0.40 L44; 0.05 L44; 0.05 L44) and the Fisher p = .0047 allocation note; Q3: zero confirmatory triggers, the falsifier, the DPO single-map +0.1667; and produce the per-stage Q3 Δs with n and map split (the preprint's data placeholder) so the note can carry a four-number line if the PI wants it. *Output:* `…_note-N7-olmo.md`.

### N8. Link 2 (Qwen hijack) via the regression suite
*Defends:* link 2. *Referents:* `valence_core/regression/analysis.py`, `oracle.py`; `data/configs/c1r3_gate_repA.json`, `c1r3_gate_repB.json`; `data/e0/*`. *Procedure:* run the suite (103/103) and list which of the note's link-2 figures are among the 103 (Δ+ = +0.285, Δ− = −0.395, bars ±0.158, random ≤ 0.088, LOO Δ+ = 0.085, 9/12 and 10/12, G = 0.316, the purity–potency figures, ‖d‖/R ≈ 0.16, sentiment cosine 0.52, fictional-character cosine ≈ 0.85, self-indexed residual ≈ 0.51) and which are log-only. Also e2d: readability .574/.613 vs .70, comparator .534, audit-flagged .000/.023/.047 from `data/e2d/*.json` via `scripts/e2d_closure_verify3.py` or equivalent. *Output:* `…_note-N8-link2.md`.

### N9. Weight channel
*Defends:* link 5 weight channel. *Referents:* `data/d/*.json`; `PROPOSAL-d-distilled-trace.md`. *Procedure:* reproduce oriented cosines 0.476/0.435, control ceilings ≈ 0.05, the leakage gate's bound and the 17×/10× exceedances. *Output:* `…_note-N9-weight.md`.

### N10. Horn-1 calibration R² = 0.53
*Defends:* P3 in §2; O4. *Referents:* Code locates (design seat's belief: the PROPOSAL-h arc or ADDENDUM-g1). *Procedure:* reproduce or mark `[log-only]` with locator; state the regression (what on what, over which tokens and sessions). *Output:* in N1's ledger.

### N14. Sham-arm pseudo-statistics (the artifact captures)
*Defends:* "what the shields caught." *Referents:* `data/e2a`, `data/f`, `data/olmo` as above. *Procedure:* the three captures with their arm, map, n and statistic in one table: e2a sham +0.111/−0.079 beside state +0.104/−0.031; f1 CORR +.121/−.130; OLMo DPO +0.1667 single map with the other map's figure beside it. *Output:* `…_note-N14-artifacts.md`.

### N15. Echo leakage figures
Folded into N3(i).

### N16. Decoding-parameters table
*Defends:* "decoding is a measurement parameter" against "what were yours." *Procedure:* for every generated-text DV in the note (e2a/e2b/f1 rounds, e2d, B2/B2-r detection, S1 judge, Q3 rounds): temperature, top-p/top-k, max tokens, seed policy, stop tokens, and the commit that fixed them. One table. *Output:* `…_note-N16-decoding.md`.

### N19. Companion-code sensitivity re-run
*Defends:* §8's numbers. *Referents:* `github.com/arvomm/cacophony-public-code`, `notebooks/scoring.ipynb` (external; pin the commit). *Procedure:* re-run at released defaults; reproduce 0.394 (equal credences, optimist vector); strike the metacognition indicator → report computational-level posterior and aggregate under equal credences and under the Level 1–2-heavy weighting; strike the Level 1 coupling indicator → report; record the indicator names as the notebook calls them and the coupling indicator's stated false-positive rate (0.70). *Output:* `…_note-N19-cacophony.md`. *On fail or not run by T:* the note's numbers are cut and the qualitative sentence stays.

## Tier 3 — footnotes

### N17. Qwen numerics and the patch
State in one paragraph for the README: the quantization, what the custom kernel patch changes and where it lives, the two numerics floors (near-tie argmax flips under high displacement; sub-0.05-cosine label geometry), and what "verified against an untouched model" means (same weights and quantization, no patch? or patch with no vector?). *Output:* README paragraph.

### N18. Hashes for the note
sha256 of the final note markdown and the tag commit hash, both to be printed in the note's footer; a `results/raw/<stamp>_note-release-manifest.json` with the tag, the note sha, and the N13 table's shas.

## 6. README-for-readers (deliverable of N12(vii))

A short file at the tag, `README-NOTE.md`, linked from the note, with: (1) one paragraph on what the repository is; (2) the N13 provenance table; (3) how to run the regression suite and what 103/103 covers; (4) the map from each note figure to its artifact (N1's ledger, abbreviated); (5) where the pre-registrations, the ledger, the log and the monitoring records are; (6) the cached-generation and numerics disclosures (N4(iv), N17); (7) licenses and third-party materials (N12(iv)); (8) a sentence that `main` moves and the tag doesn't. It does not describe the multi-seat workflow beyond one sentence pointing at the handoffs for anyone who wants it.

## 7. What this block does not do

It does not build, lock or run anything of PROPOSAL-m; it does not re-run any session; it does not touch ADDENDUM-k1 or the k arc's three open questions; it does not change CLAUDE.md; it does not decide the tag name, the release date or history rewriting — those are the PI's.
