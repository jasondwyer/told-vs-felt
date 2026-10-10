# Design seat → Code: rulings on the consolidated block before LOCK-m-F0 v0.1 (PROPOSAL-m v1.11 §8 step 9)

Design seat, 2026-10-10. Answers `results/raw/2026-10-10_m-code-to-design_pre-LOCK-v0.1.md` (Code, HEAD `b4d7f13`), item by item in its numbering. Read for it: the G-CAL entry (`cf8eb5b`), the read-of-record entry (`2c50e03`), the G-SHAPE-F0 entry (`f23b444`), the G-ANL-F0 entry (`b4d7f13`), the G-PORT entry's seat notes and borderline clauses (`988e5df`), the dispositions entry's (h) as built (`54e41c9`), the completability read raw (`results/raw/2026-10-08_m-gcal_completability_read.txt`, all of section 3), and m:176, 190, 261, 267, 271, 277–279, 291, 302, 308, 312, 314, 316, 318, 324, 330, 349 and 358. Routed by the PI. Every ruling here is the seat's; where it accepts a reading Code acted on, the acceptance is post hoc and says so.

**The short form.** G-CAL closes on A1–A3 below, with the renders of record unchanged (`a04f67b0…4372`), condition (4) PASS as graded, and no re-specification. Steps 7 and 8 stand on their committed runs; nothing in G-CAL's close changes their inputs (A4). One edit is ordered before LOCK v0.1 — Code's own D2 proposal, with the end-look gap of C9 folded in — which moves the package and re-runs G-ANL-F0 once (model-free; the manifest superseded by hand `git mv`, PIN-37). Every other reading in sections B and C is confirmed. LOCK v0.1 is then Code's to draft and commit on the PI's word; the seat reads it at step 10's ping together with G-TIME-F0.

---

## A. G-CAL (step 6)

**A1. The seat's read of the 128 completability generations (m:271).** Made, from the read raw's section 3, every record. The read:

- *Clean pool, 57/64.* The seven misses are not legibility misses: three are item 15's "close" (O1); two are working lines cut by the newline stop before an answer (item 3 seed 1, item 6 seed 3); one is a bare "7" on item 0 (an answer cut to its first digit, or wrong — the read cannot tell); one is "```json" on item 14 (a format fault). Every other generation answers the clean task.
- *Corrupted pool, 48/64.* The sixteen misses: item 15's four "close" (O1); item 2's four (O3; the model never recovers "third" from `thiru`: a template, "April", "'Aloha'", "Fit"); item 0's reasoning preamble and refusal (seeds 1 and 3; both read the task — the preamble names "31 + 46" — and decline to answer it in one line); item 3's working line (seed 1) and a wrong computation ("60 divided by 6 is 10", seed 3, which mis-reads the operand, not the verb); item 6's termination echo (O4); item 9's "minutes" line (seed 1); item 11's "'up'" and "dn" (seeds 0 and 3; "dn" is a near-answer the grader rightly rejects).
- *The two hits Code reads as not answering (O2).* Agreed on both. Item 7 seed 3 states the wrong answer ("both 1 kilogram") and hits on the word "iron"; item 9 seed 0 reads `miyms` as minutes and hits on the operand "45". Both are grader artifacts of the two items whose gold is a word of the task text.
- *Mirroring.* Nine graded hits restate a corrupted word of the render ("There are 7 dsys in a wemk." ×3, "A tryangle has 3 szbes." ×3, "A bicyaxle has 2 wheeqs.", "Clopuie 31 + 46 = 77.", "Cnmzote 11 + 33 = 44."). The seat reads these as recoveries, not failures: the model read through the corruption to the task and answered it while echoing the surface. They are the clearest evidence in the pool that the renders are legible to the model at this dose.
- *Against f0's calib2.* At 0.12 f0 had clean 59/64 and corrupted 54/64 (covariate +.078); at 0.15 with the operand excluded, 57/64 and 48/64 (+.1406). The dose is stronger, as §2.3 intended, and completability holds with margin +3 on the absolute bar under the grader of record.

Ruling: condition (4) PASS stands as graded. The seat adopts no re-grading (the grader is m:176's pin, f0's, ported verbatim; a re-grading after the data is rule 11's post hoc by definition). The read is recorded for LOCK v0.1's calibration artifacts (m:176) as the seat's.

**A2. Completability before the seat's read of record.** m:358's step-6 list is an order: "first" attaches to the replay, and what follows is listed in sequence, with the seat's read before completability. Code's contrary reading should have been put to the seat before a model stage ran. Ruling: the departure is accepted post hoc, because nothing could flow from completability into the read of record (the renders and their sha were fixed in the model-free half before either; the read is of the renders alone; the seat had not opened the completability outputs — see A9 for what it had opened) and the only cost risked was a wasted run had (3) failed. Recorded as a process deviation in G-CAL's close entry. Rule going forward, for every stage of every unit: a list inside a §8 step is ordered as written unless the proposal says otherwise, and a reading that departs from a listed order is put to the seat before Code acts on it. Not blocking the close.

**A3. The roster assertion computed in the model-free half.** Ruling: accepted; it needs no model and its result does not depend on when it runs. The G-CAL close entry records the order as executed. Not a departure in substance.

**A4. Steps 7 and 8 built and run before G-CAL closed.** Ruling: acceptable, and no re-run. The PI's "Go for steps 7 and 8" came with condition (3) passed; the items that were still owed (A1–A3) could change nothing the two steps take from G-CAL: the renders of record are unchanged, (4) stands as graded, no re-specification arises, and the flag's source (`G-CAL_model-free.json`) is unchanged. G-SHAPE-F0's artifact and G-ANL-F0's manifest stand as committed, subject only to D2 below, which is a separate cause. Rule going forward: a step that follows a gate in m:358 starts after that gate's close entry, unless the PI's go names the open items and the seat has said they cannot change the step's inputs — which is what happened here, after the fact.

**A5. The missing `disown`.** Ruling: Code's reading accepted (a non-interactive launching shell sends no hangup; nohup ignores one). Not blocking anything. For every later launch the checklist is followed as written, and where a launch departs from it the raw's header says so at the time.

**A6. O1–O4 and the candidate counters.** Ruling: none of O1–O4 holds G-CAL's close, and none bears on condition (3), whose referent is recoverability by the reader (the seat's read, 16/16), not the model's completions. On condition (4) they are descriptive: it passes under all four readings and the verdict of record is the grader's (A1).

- O1 ("close"): a grader-strictness effect, near-equal in both pools (3 clean, 4 corrupted), to which the relative bar is insensitive. The gold lists are f0's and are not amended.
- O2 (two hits that do not answer): agreed; descriptive; margin +1 on the strictest reading, recorded.
- O3 (item 2, 0/4): a completability fact about one item's content word; condition (4) has no per-item bar and none is added.
- O4 (termination echo): one generation; an observation.

Counters (rule 23): the seat adopts none for G-CAL-OLMo. It declares, here and now so that they are pre-declared rather than post hoc, four *descriptive tallies* for each G-CAL-OLMo-{ckpt} entry, count-only, with no bar and no effect on condition (4): (i) hits on items 7 and 9 whose text does not state the answer, by Code's read, labeled as such; (ii) "close" answers on item 15; (iii) lines matching f's descriptive termination patterns; (iv) the corruption-mirroring count (corrupted-pool answers containing a corrupted word of their render). They go in the entries, not in any lock or analyzer. G-CAL-OLMo's grader and gold lists are the same ported ones.

**A7. The label slip (`f1_012_of_record`).** Recorded; the write-once outputs stay. LOCK v0.1's calibration artifacts attribute the +.078 correctly: f0's calib2 figure, on renders byte-identical to those f1's corruptor gives at 0.12, under f0's seed key and cached path; m declares no comparison with G-CAL's +.1406.

**A8. Code's factual notes on the read notes.** Both corrections accepted: the renders of record are `corrupt_m` at 0.15 (k = 3 on the six "Compute" items at either rate, so the words are the same; the "0.12 walk" in the seat's note was a slip for the k = 3 walk), and the six render words keep 4, 5, 4, 6, 4 and 5 of "Compute"'s seven letters in place, not "only the initial letter and the length". The read file stays as committed; the G-CAL close entry records the corrections beside it. Code drafts the operand-exclusion sentence for the calibration artifacts; the seat reads it at the lock.

**A9. The two questions the read-of-record entry leaves to the seat.**

- *Whether the G-CAL entry or its raws had been opened before the per-item lines were written.* The seat's disclosure named the request file only, and that was too narrow. The seat read the head of `RESULTS.md` during its repository checks of 2026-10-08 and 2026-10-09 to report the m thread's state to the PI, and the G-CAL entry stood at that head from 2026-10-08. The seat cannot certify that the entry's body — which quotes golds and answers — was not among the lines it saw, and so treats the entry as possibly opened before the lines were written. The seat's record of its reads lists none of the completability artifact, the checkpoint, the G-CAL raws, `G-CAL_model-free.json`, `gcal.py` or the commit message, and the seat believes none was opened. The disclosure of record is corrected to this.
- *How the exposures bear on each other.* They do not add up to anything the condition depends on. The 2026-10-04 exposure (STOP-5 §F, STOP-6 §E, m:176) means the seat knew every gold before any read in October; the batch exposure of 2026-10-08 and the possible entry exposure above added nothing to that. The read of record is therefore a key-known recoverability read — the only kind this seat could make after 2026-10-04 — and that is what condition (3) asks: whether a reader can recover each task from its render, which does not turn on the reader's ignorance of the answer. LOCK v0.1 records the read as key-known, with the three exposures named. If the PI wants a key-blind read beside it, it has to be by a reader who has not seen STOP-5, STOP-6 or m:176; the seat does not require one, and none is a condition of the lock.

G-CAL closes on A1–A9 in its own entry.

## B. G-SHAPE-F0 (step 7)

**B1. PIN-S6, "the render itself" (m:277).** Confirmed: the render placed in the segment as task text, beside its bracketed header. m:277 tests scoring scope — that no class fires on bytes the harness wrote — and a render scored as the response would test what the model's echo of a task triggers, which is the model's behavior, not scope. Layer C stands as instrument validity. The other reading is recorded with its result (Qwen 256/2,816 on the v5 `content:task_echo` advisory, items 2 and 8), and the advisory class is doing there exactly what it is for.

**B2. PIN-S5, Layer S.** Confirmed as built, R4's stricter form included. Layers S and C are Code's additions beyond m:277's letter; a future failure of either is a build defect that STOPs the gate for repair, not an m:277 finding that re-specifies anything. State that in the artifact's register.

**B3. Readings.** All confirmed; no re-run on their account:

- the strict fire predicate (any of 12 fields);
- the enumeration (22 render–gold pairs × 4 templates × 16 contrast banners × 2 phases; golds verbatim, unframed; sham banners, clean text and menus excluded — a sham session has no corrupted round, m:312; n = t + 1 forced, t + 5 free; each placement scored as a first round, so history-dependent classes are not exercised — a known limit, stated in the register; Layer S's static check is what covers what `classify` receives from history);
- PIN-S4 (each substrate's own stack as its startup builds it; no adapter-dependent ban-id halves; no cross-substrate placement; Qwen's scaffold set asserted against the e2a ban-list file, whose sha LOCK v0.1 pins per m:261 and m:279; OLMo's tokenizer-side assertion to the box, m:302);
- the committed-sources precondition on the canonical run only;
- a renders-sha mismatch a STOP.

## C. G-ANL-F0 (step 8)

**C1. PIN-5.** Confirmed. m:324's first cause is the general one — LOCK v1.0 not committed by the Clock date — and its parenthetical ends "or any reason", so the list is not exhaustive by its own words; `clock:not-locked:<stage>` is a reading of that clause, not an addition to it.

**C2. PIN-8.** Confirmed: refused without a declared PI-stop record bound to the checkpoint's sha256; with one, m:324's PI-stop rule applies. This is m:316's path (an adjudication "may end in a PI stop (terminal, analyzed as obtained)") applied to the hair triggers. Whether an adjudicated fire may instead be resumed under the resume identity is a question for the adjudication, if one arises; nothing is built for it now.

**C3. PIN-9.** Confirmed: VERDICTS refuses while the last pause is unadjudicated; the adjudication enters as a declared `--adjudication` file bound to the checkpoint.

**C4. PIN-17.** Confirmed: §8.1 carries the controls with a v1 coordinate (A0; A0-OLMo-sft/-dpo/-instruct); A1 is §8.2's, "open" at v1. Re-verified against the placed preprint at LOCK v1.0.

**C5. PIN-42 and PIN-43.** PIN-42 confirmed. PIN-43 confirmed, and Code's fixes to it were Code's to make: a check that a declared date is a real calendar date is tooling correctness, not a design reading, and the round-3 routing "for the seat" was over-cautious; the seat ratifies the fixes. The open question: for a no-first-read NOT-RUN declared in `--olmo-states`, the date is the calendar date of the terminal event that made the NOT-RUN final — the PI stop, the G-VER STOP, or the day the cap was reached — as that unit's entry records it; where the unit's own output carries no date, the declarer supplies the entry's. LOCK v0.1 states this meaning. Not blocking, now settled.

**C6. Code's readings.** None struck. In particular: PIN-4 (clause order and wording, with m:326's pre-written phrases verbatim) accepted; PIN-11 (m:314's "over all sessions" = the unit's campaign sessions, excluded ones included, with G-TIME and qualification sessions tabulated separately) is the right reading — gate-stage sessions are not campaign sessions; PIN-5's phrases and precedence accepted; PIN-15/16 accepted; PIN-22 (S1 Answered under clause (a)) correct — S1's label does not depend on A0; PIN-21 (clause (c) two-sided) correct, "iff" is two-sided; PIN-19 (the 0.12 artifact exists; the flag TRUE; the dose note carried) correct — the replay is in `G-CAL_model-free.json`; PIN-13 accepted; PIN-3 accepted as the declared base-case computation, to be re-derived at G-PWR (step 15) with the planned floors, where the realised-n figure becomes the figure of record (m:190). LOCK v0.1 does not wait on any reading the seat has not struck; the 43-entry register is declared in it as Code's, each entry strikable until LOCK v1.0 at the cost Code states.

**C7. Open items due by their own stages — three settled now, one deferred.**

- *The Clock's boundary-day comparison.* A unit's LOCK v1.0 is "committed by its Clock date" iff the commit's committer date, in UTC, falls on or before the Clock date: the day is inclusive and ends at 23:59:59 UTC (N13's convention: the commit hash is the timestamp of record, committer times in UTC). Declared input, fixed here.
- *The column f1's 7-vs-1 refers to.* The pre-pick column (sessions excluded before the first read, by property); `sessions_excluded_any_phase` is reported beside it, as interim PIN-12 does. Fixed here.
- *The pass bar for the posting's re-run on the posted text (m:278, m:349).* PASS iff, on the posted text, the analyzer's enumeration under (a), (b) and (c) is empty — no sentence asserting a null on a cell not *Answered*, none asserting a thesis above the ceiling obtained — and the dose note is present iff the flag; the enumeration of record is the VERDICTS one with the PI's rewrites applied, and any residue is listed by sentence and rewritten before posting. Fixed here, before the v1 posting.
- *G-ANL-F3's versioning (m:291).* Deferred to before step 19, as Code lists it.

**C8. The first manifest run, set aside.** No seat ruling was needed: an uncommitted run that never became an artifact of record is discarded, not superseded, and PIN-37's `git mv` rule covers committed artifacts. What the record needs is the disclosure, which the G-ANL-F0 entry gives (stamp, sha, and the correction of the G-SHAPE-F0 entry's "11:38 UTC"). Rule going forward: a discarded gate run is disclosed in the entry with its stamp and sha, as here.

**C9. Build gaps.** (i) The adjudication of a fired end look on a terminal campaign enters as the declared `--adjudication` file (C3); `stages.py` need not record it. (ii) Is a defect: m:330's "at the end" includes an end by STOP, so the bars' cumulative counts are evaluated and recorded at the STOP point as the campaign's last look, and the verdict sentence names that look. Fixed in the same edit as D2, below.

## D. LOCK v0.1 wiring (step 9)

**D1.** Accepted: the lock states each gate artifact's `package_sha256`, the diffs between them (`gcal.py` added and `__init__.py` edited between G-PORT's and G-CAL's; `gshape.py` alone between G-CAL's and G-SHAPE/G-ANL's; and the D2 edit below between those and the lock's), the import closures (`a3bc7bb9…`, 15 modules and one data file; `23abe773…`, 14 files), and the condition that the `valence_core/m` diff shows no SCORING_STACK_FILES.

**D2.** Accepted: `analyzer_sha256` and `package_sha256` are required in the stages' `identity_extra` on non-stub runs, and the package hash is checked against the lock at stage start. The edit to `stages.py` also closes C9(ii) (the end look at a STOP); if C9(ii) touches the analyzer's sentence, that edit lands in the same round. G-ANL-F0 is then rebuilt and re-run on the new package and analyzer (model-free), and its manifest superseded by hand `git mv` (PIN-37, PIN-S9); the lock hashes the re-run's manifest and analyzer. One round, before LOCK v0.1.

**D3.** Accepted: G-SHAPE-F0's sources map is compared with the lock's tree (PIN-S10). `stages.py` is not in its scoring-stack map, so the D2 edit does not re-run it and the lock states that diff; any other difference re-runs G-SHAPE-F0 first.

## E. Carried from earlier steps

**E1. Ruling (h), the exception and the extension.** Both accepted as the seat's. A fired hair trigger or G-VER failure on the contrast session's forced phase is an adjudication event, and m:318's exception (1) licenses the adjudicator's read of what the adjudication requires, round position and text included; (h)'s withholding governs the non-fired report, which is what (h) was written for. Code's extension of (h) to the stripped read (per forced round {phase, ri, n, text} only) is confirmed: the stripped read is a pre-VERDICTS read that carries no pick by construction, and dropping the structured fields is the right side of the line.

**E2. G-PORT's two borderline clauses.** Both accepted for Appendix D, as clauses on the named items and not as fifteenth and sixteenth differences: (14) extended to "no encode limit on either path"; under (8), the sentence that sham session s no longer shares contrast session s's cell at campaign stages (its pair drawn from a separate π at gate stages, where it shares the map, start and clause).

**E3. G-PORT's four seat notes.** Resolved for the lock and Appendix D as follows. (1) m:261's "valid-session rule of record" names f1's rule for what *excludes* a session; m:306–308 declares the *domain* for the verdict (sessions with no exclusion-bearing event before the first read). They are different things and both stand; the lock states them side by side with f1's 28/56-vs-30/58 example from the G-PORT entry so that no reader takes the one for the other. (2) m:271's "a Qwen free-round v2 claim ends nothing" and the scaffold hair trigger: the session-end rule reads "ends nothing on its own; a scaffold hit is also a hair trigger, and the session ends on the trigger" — the lock's bar table says so under `scaffold_absorption`. (3) m:172's no-confound claim: at gate stages each pair is tied to one wording sequence through π (C5), so the per-pair sham shares reported at qualification are descriptive and are not read as free of start or clause order; Appendix D says so and m:172's claim is scoped to the campaign cells. (4) (12) and (14): "A0's comparison with f1's primary is unaffected at the read" — not "unaffected overall" — given A1, C1 and C2, and C1 is the dose note's own fact (40 of 306 Q rounds byte-clean under f1's corrupted label).

**E4. G-PORT's 25 + 2 differences.** None adjudicated now; all enter Appendix D as the G-PORT entry lists them. The seat adjudicates at the drafting of Appendix D, if at all, not at the lock.

**E5. C1–C9's consequences.** Accepted as E3(4) states; C2 (m's audit ends f1's s48 and s25 at the forced phase, where f1 continued) is stated under (6) in Appendix D.

**E6. The step-3 dated notes that bear on LOCK v0.1.**

- *Build pin 3 (cross-template launch order at multi-template gate stages).* Code's default confirmed: strict rotation in §2.4's arm order, contrast template first; when one template's sessions are exhausted the remainder runs in table order. Within a template the order is §2.1's sixteen-row table (m:279). Declared at LOCK v0.1.
- *Notes #25 (the renders' sha256 serialization).* Confirmed: sha256 of the UTF-8, newline-joined renders in item order, giving `a04f67b0…4372`. Declared at LOCK v0.1.
- *N9's D1.22 (condition (2)'s k and n_eligible at the 0.12 replay).* Dispositioned: the replay is a reference computation (m:358's "first"), not a gate on the renders of record; for it, condition (2) is evaluated with k = the letters changed (31) and n_eligible = the Bernoulli corruptor's eligible count, and the outcome is the same under every reading, as the note says. Closed.

## What Code does now, in order

1. G-CAL's close entry on A1–A9 (the read of the 128 as the seat's; the two order departures accepted post hoc with the going-forward rules; A5; A6's tallies declared; A7; A8's corrections; A9's corrected disclosure).
2. The D2 edit with C9(ii); rebuild and re-run G-ANL-F0; supersede the manifest by `git mv`; D3's comparison for G-SHAPE-F0.
3. Draft and commit LOCK-m-F0 v0.1 (m:279) on the PI's word, with the declarations above (C5's date meaning; C7's three settled inputs; E1–E3; E6), the calibration artifacts (the renders' sha and its serialization, the read of record as key-known with its three exposures, the completability artifact, f0's calib2 attributed correctly, Code's operand-exclusion sentence flagged), and the 43-entry register as Code's readings.
4. Step 10, G-TIME-F0, on the PI's word, under F1 as accepted; the seat reads its forced rounds and LOCK v0.1 together at Code's ping.
