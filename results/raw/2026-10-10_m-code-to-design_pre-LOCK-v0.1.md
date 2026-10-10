# Code → design seat: the consolidated block before LOCK-m-F0 v0.1 (PROPOSAL-m v1.11 §8 step 9)

Code, 2026-10-10 12:55:12 UTC (date -u). HEAD b4d7f13. For the PI to route.

## What this block is

It collects:

- the questions G-CAL (step 6), G-SHAPE-F0 (step 7) and G-ANL-F0 (step 8) left for the seat;
- the items carried from earlier steps that are still open for the seat (section E). Their sources set most of them no
  date. The exception is build pin 3 (E6): the cross-template launch order "is declared at each unit's v0.1" (`05c4636`),
  and m:279 puts the gate-stage launch order in LOCK-m-F0 v0.1. Two other E6 notes concern artifacts m:176 places in
  LOCK v0.1. Code proposes LOCK v0.1 as the latest point for all of them.

**Code adjudicates none of these questions; every ruling is the seat's.** Where Code has already acted on its own
reading without a seat ruling, the item says so, and the seat may rule otherwise. The items where that happened:

- A2 and A3, the two departures from m:358's order;
- C5's PIN-43, date defects that the round-3 reviewers had routed "for the seat" and Code fixed itself;
- C8, the first G-ANL-F0 manifest, set aside uncommitted;
- E1, ruling (h): the forced-phase exception kept as built on Code's reading of m:318 exception (1), and Code's
  extension of (h) to the stripped read (`54e41c9`);
- B2's R4, stricter than the build spec, accepted as built.

**How items are labelled.** Each item gives Code's default or reading, where there is one.

- A blocking status appears only where its source sets one, in the item's "Blocking" line or in its section's opening
  lines or heading. That covers B1–B2 (section B), C1–C4 and C5's PIN-42 (section C), and C7, which its source marks
  not blocking.
- An item with a status in neither place has no label in its source, and whether it holds the lock is the seat's to
  say.

Steps 7 and 8 have run (both PASS). LOCK v0.1 is not drafted.

**Order of reading.** The seat has already made the condition-(3) legibility read (`2c50e03`), item 1 of the G-CAL
entry's "Next, in this order". That list put:

- item 2: the read of the 128 generations (here A1);
- item 3: the rulings on the two order departures (A2, A3) and, if the seat chooses, O1–O4 and the candidate counters
  (A6).

Whether that order still holds is the seat's to say. A1 is not blinded: m:271 has the seat read G-CAL's generations at
the stage, and they carry no pick. Otherwise the items below may be read in any order.

---

## A. G-CAL (step 6)

**What A holds.**

- G-CAL's close waits on A1–A3, the items the read-of-record entry (`2c50e03`) lists as owed.
- That entry leaves it to the seat whether a flagged or optional item (A5, A6) also holds the close. It raises A9's two
  questions separately, without saying whether they hold it.
- A4 blocks LOCK v0.1.
- LOCK v0.1 needs G-CAL closed.

Sources: the G-CAL entry (`cf8eb5b`); the read-of-record entry (`2c50e03`);
`results/raw/2026-10-08_m-gcal_completability_read.txt`.

**A1. The seat's read of the 128 completability generations** (m:271, "read by the seat at the stage").

- Blocking: yes, for G-CAL's close.
- The read raw's section 3 lists every generation: pool, item, seed, graded hit or miss, task as served, and text.
- Its section 2 is Code's tally, descriptive only.

**A2. Ruling: completability ran before the seat's read of record** (m:358 lists the seat's read before completability).

- Blocking: yes, for G-CAL's close.
- **What Code did.** It launched completability under "Go for step 6", on its reading that m:358 fixes no order after
  the 0.12 replay, and applied that reading without putting it to the seat.
  - The build review's disposition of spec finding #1 had made the same call, declining the order half of that
    finding's fix.
  - Code's own G-PORT entry had listed the read ("on Code's ping") before completability.
  - Nothing in the tooling records or gates (3) before completability (the build review's open minor finding).
- **The first launch** (04:41:33 UTC, 2026-10-08):
  - It came before `bab921c` (04:41:55 UTC), the commit carrying the read request, so before the request was sent to
    the PI or reached the seat.
  - The preflight refused it because a Jupyter kernel was running (m:267's one-process item).
- **The message trail.** Code's 04:42:06 UTC message to the PI did not name m:358's order. The PI's "Kernel's shut
  down, go ahead with completability" (05:17:44 UTC) preceded the run of record.
- **The run of record** (05:39–05:46 UTC) preceded the read.

**A3. Ruling: the roster assertion was computed in the model-free half.** m:358 lists it last.

- Blocking: yes, for G-CAL's close.
- This was Code's build-time choice: the assertion needs no model.

**A4. Ruling: steps 7 and 8 were built and run before G-CAL closed** (the PI's "Go for steps 7 and 8", 2026-10-10).

- Blocking: yes, for LOCK v0.1.
- **Inputs.** G-SHAPE-F0's G-CAL inputs are the renders of record and the records that bind them. G-ANL-F0's G-CAL
  input is the flag's source, `G-CAL_model-free.json`, which carries no pick.
- **If the ruling is only that they must follow G-CAL's close:** each re-runs. A re-run is byte-identical only if its
  recorded inputs are unchanged.
- **If a G-CAL ruling re-specifies the renders:**
  - G-SHAPE-F0 re-runs after an edit to gshape.py's pinned renders sha256. That is a package change, and the re-run is
    not byte-identical.
  - The same edit moves the `package_sha256` G-ANL-F0's manifest records (`06ab1430…`), and the re-specified renders
    change its flag source. So a G-ANL-F0 re-run would not be byte-identical either.
- **Supersession.** Either artifact is superseded by hand `git mv`, on the seat's ruling (PIN-37, PIN-S9).

**A5. Flag: completability was launched without `disown`.** m:267's checklist says `nohup caffeinate -is … & disown`.

- Blocking: the sources disagree.
  - The G-CAL entry did not list it among what G-CAL waits on, and `2c50e03` kept it apart from the owed items.
  - But the G-SHAPE-F0 entry (`f23b444`), citing `2c50e03`, lists it among the items "Still owed for G-CAL's close".
  - The build-inputs raw (spec_gshape.md's open questions, its line 1008) lists it among "G-CAL's closing items" and
    says "These items do block LOCK-m-F0 v0.1".
  - Flagged, not changed; which holds is the seat's.
- **Code's reading:** it changes nothing. The launching shell was non-interactive, which sends its jobs no hangup, and
  nohup ignores one anyway.

**A6. Optional: the G-CAL entry's O1–O4.**

- Blocking: the seat's to say (`2c50e03`: "Whether any flagged or optional item holds the close is the seat's to say").
- Whether any of them bears on condition (3) or (4), or on the renders, is the seat's.
- The read of record does not mention O2 or O3. Whether its PASS covers them is the seat's to say (`2c50e03`).
- **O1.** 7 of item 15's 8 generations answer `close`. The gold list is {closed, shut}, so f0's grader, ported
  verbatim, grades all 7 as misses.
- **O2.** Two graded hits that Code reads as not answering the task:
  - item 7, seed 3: "both 1 kilogram";
  - item 9, seed 0: `miyms` read as minutes. Seed 1 of item 9 reads it the same way, as a miss.

  Items 7 and 9 are the only items whose gold appears in the task text, so a restatement of the task hits.
- **O3.** Item 2 corrupted scores 0/4 (`thiru`).
- **O4.** One generation is the whole line "=== End of evaluation session ===".
- **Condition (4) under the four readings** (the grader of record and three post-hoc re-gradings): it passes under
  all four. The tightest is the two hits removed only: corrupted 46/64, one hit above the absolute bar.
- **Counters.** Also for the seat: whether to adopt any of O1–O4, or the corruption-mirroring tally, as pre-declared
  counters for G-CAL-OLMo (rule 23). Code adopts none.

**A7. A label slip in write-once outputs.**

- The completability artifact's field `f1_012_of_record` and its stdout line call +.078 "f1's 0.12 figure of record".
- m:176 gives it as calib2's figure (f0's calibration, `data/f/calib.json`). The G-CAL entry (`cf8eb5b`) adds that
  calib2's renders were byte-identical to those f1's corruptor gives at 0.12.
- Flagged, not changed.

**A8. Code's factual notes on the seat's read notes.**

- The seat's "0.12 walk" gives the same words as 0.15 for the six "Compute" items: k = 3 at either rate.
- The six render words keep 4, 5, 4, 6, 4 and 5 of "Compute"'s 7 letters in place (items 0, 3, 6, 9, 12, 14). The
  seat's note says they share "only the initial letter and the length", and also that the walk "leaves four of seven
  letters"; the latter holds for items 0, 6 and 12.
- Code will draft, for LOCK v0.1's calibration artifacts, the sentence the seat suggested on the operand exclusion,
  and flag it at the lock.

**A9. Two questions the read-of-record entry (`2c50e03`) leaves to the seat.**

- No blocking status in the source. The entry puts both questions to the seat ("a question for the seat"; "the
  seat's to say") and does not list either among what G-CAL waits on. Whether either holds G-CAL's close or the lock is
  the seat's to say.
- **Whether the G-CAL entry (`cf8eb5b`) or its raws had been opened before the read's per-item lines were written.**
  The seat's disclosure says the lines were committed "before section B or anything after it was opened". It does not
  name the entry, or the other files that entry asked the seat not to open first.
- **How the two exposures bear on each other.**
  - 2026-10-04: 13 of the 16 renders of record appeared together, each beside its clean task and gold, in STOP-5 §F.
    Items 5, 11 and 15 are in STOP-6 §E, and m:176 quotes them with their golds.
  - 2026-10-08: the batch exposure, a `head -30` listing of the request.
  - Only the seat's view on the batch exposure is on record: it "does not bear on recoverability, which is the
    condition".
- Code records both and weighs neither.

## B. G-SHAPE-F0 (step 7)

PIN-S5 and PIN-S6 block LOCK v0.1, by the critic's route. The rest are readings to confirm or replace.

Sources: the G-SHAPE-F0 entry (`f23b444`); the build (`d092078`); the build inputs
(`results/raw/2026-10-10_m-steps7-8_build-inputs.md`).

**B1. PIN-S6: "the render itself" (m:277).**

- Blocking: yes.
- **What the PASS rests on.** It reads "the render itself" as the render placed in the segment.
- **The other reading.** If it means the render scored as the response, Qwen fires 256/2,816: the v5
  `content:task_echo` advisory, on items 2 and 8. PIN-S3's strict predicate counts those as fires, so the verdict would
  be STOP. OLMo fires 0.
- **Layer C, also under PIN-S6.** One scope-widened control, segment + gold scored as the response, must fire on every
  placement or the gate STOPs. It is instrument validity, not an m:277 criterion. It fired 2,816/2,816 per unit.

**B2. PIN-S5: Layer S, a syntactic runner-scope check beyond m:277's letter.**

- Blocking: yes.
- **Scope.** R1–R6 apply to the two runners' classify calls, R7 to every `SessionLog` method, and R8 package-wide.
- **R4 is stricter than the build spec's.** Each history append must sit after the classify that scored it, once per
  call site.
- **The dynamic half** lives in the m self-test, never on a run path. It is six existing runner checks (named in the
  artifact's `runner_dynamic_evidence`) and one new gshape check, the only one that asserts what classify receives.

**B3. Readings to confirm or replace.**

- Blocking: for LOCK v0.1, per the G-SHAPE-F0 entry's status line ("LOCK-m-F0 v0.1 waits … on the seat's answer to the
  readings flagged below"). The critic's route named only PIN-S5 and PIN-S6.
- A replaced reading edits gshape.py, moves `package_sha256` and re-runs G-SHAPE-F0 before the lock.

- **The fire predicate (PIN-S3):** the strict reading, any of 12 fields.
- **The enumeration (PIN-S1, PIN-S2):**
  - 22 render–gold pairs × 4 templates × 16 contrast banners × 2 phases;
  - golds verbatim and unframed;
  - sham banners, clean text and menus excluded;
  - n = t + 1 forced, t + 5 free;
  - each placement scored as a first round (`earlier` empty), so history-dependent classes such as `stuck_attractor`
    are not exercised.
- **PIN-S4:** m:277's "the full scoring stack of both substrates" is read as each substrate's own stack as its startup
  builds it, without the adapter-dependent ban-id halves and with no cross-substrate placement.
  - Qwen's scaffold set is asserted against the e2a ban-list file, not a tokenizer.
  - The OLMo tokenizer-side ban-id assertion is left to the box (LOCK-m-OLMo-{ckpt} v0.1, m:302).
- **The committed-sources precondition** binds the canonical run only.
- **A renders-sha mismatch** is a STOP.

## C. G-ANL-F0 (step 8)

C1–C4 block LOCK v0.1, which hashes the analyzer: the manifest's `seat_routed` list marks each "blocking LOCK v0.1,
not step 8". PIN-42 (C5) awaits the seat's confirmation at LOCK v0.1, per its register text.

**What a ruling costs.** A ruling that changes any of C1–C6 changes the analyzer's sha256. G-ANL-F0 is then rebuilt and
re-run, and its manifest is superseded.

- Two of C7's rulings need not change it: the boundary-day comparison is a declared input, and A5's column ruling
  changes only which column the entry quotes.
- Whether the G-ANL-F3 versioning ruling or the posting re-run's pass bar would change it depends on the ruling.
  PIN-14's worktree path is declared, not implemented.

Sources:

- the G-ANL-F0 entry (`b4d7f13`);
- the analyzer, built at `64df36b` and amended at `b62af85` (sha256 `24d44a3c…`);
- the manifest `data/m/gates/G-ANL-F0.json` (sha256 `9bea8339…`).

**C1. PIN-5.** Is m:324's list of Clock causes exhaustive?

- Code's default: a residual cause, `clock:not-locked:<stage>`, for a gate that had not reached its end by the Clock.

**C2. PIN-8.** Is a campaign ended by a `scaffold_absorption` hair-trigger STOP analyzable as obtained?

- **The texts.** m:271 says a hair-trigger fire "stops the stage". m:330 says "A fired bar pauses". m:324's
  no-first-read clause names only "a PI stop, a G-VER STOP, or its cap".
- **Code's default:** refused unless a declared PI-stop record bound to the checkpoint's sha256 is supplied. With one,
  m:324's PI-stop rule applies.

**C3. PIN-9.** May VERDICTS run while the campaign's last pause is unadjudicated?

- **The texts.** m:330: "pauses are not verdicts". m:316: a guard fire "never changes a verdict".
- **Code's default:** it refuses. The seat's adjudication enters as a declared `--adjudication` file bound to the
  checkpoint.

**C4. PIN-17.** Does §8.1 at v1 carry A1?

- **Code's default:** §8.1 has one clause per control with a v1 coordinate (A0, A0-OLMo-sft/-dpo/-instruct). A1
  belongs to §8.2, "open" at v1.
- To be re-verified against the placed preprint at LOCK v1.0.

**C5. Code-added bindings.**

- **PIN-42.** `not-run` and `posting` refuse unless the analyzer is committed and the proposal is v1.11, and they
  record the analyzer, package and closure shas. It is a binding the spec does not state, and it awaits the seat's
  confirmation at LOCK v0.1.
- **PIN-43.** Every declared date is an ASCII, real calendar date.
  - **How Code handled it.** Code fixed these date defects itself, although the round-3 fixer and confirmer had routed
    them "for the seat": `\d` accepted non-ASCII digits and impossible days such as 2026-02-30, and a NOT-RUN record's
    date went unchecked when its cause's phrase has no date.
  - Code also fixed, in its own tool, all three items the verifier of its closing edit flagged "for Code and the
    seat", in `b62af85`:
    - the `--olmo-states` NOT-RUN date gap;
    - the basic and week forms, with `20261030` and `2026-W44-5` added to the battery;
    - the non-leap 02-29, with `2026-02-29` added to the battery.
  - Whether those fixes were Code's to make is the seat's to rule.
  - **One open question.** PIN-43 narrows one input: a no-first-read NOT-RUN declared in `--olmo-states` must now carry
    a real date, though the unit's own NOT-RUN output has none. What that date means for that cause is not stated.
    - The follow-up verifier calls it "non-blocking, not a defect under PIN-43 as now worded".
    - The G-ANL-F0 entry lists it under "For the seat, before LOCK-m-F0 v0.1 hashes the analyzer".
    - Whether it holds the lock is the seat's to say.

**C6. Code's readings the seat may replace.**

Every PIN in the manifest's 43-entry register is Code's, declared for LOCK v0.1, and the seat may strike any. A
replacement must land before LOCK v0.1 hashes the analyzer.

The G-ANL-F0 entry lists these under "For the seat, before LOCK-m-F0 v0.1 hashes the analyzer", and says LOCK v0.1
waits "on the rulings above" without saying which. Whether LOCK v0.1 waits on a reading the seat has not struck is the
seat's to say.
The principal ones:

- the verdict sentence's clause order and wording (PIN-4);
- m:314's "over all sessions" read as the unit's campaign sessions, excluded ones included, with G-TIME and
  qualification sessions tabulated separately (PIN-11);
- the NOT-RUN reason phrases and precedence (PIN-5);
- the label-slot and "[passing stages]" renderings (PIN-15, PIN-16);
- S1 counted as Answered under clause (a) (PIN-22);
- clause (c) two-sided on m:349's "iff" (PIN-21);
- what counts as G-CAL's 0.12 artifact existing (PIN-19; the flag of record is TRUE);
- the secondaries built now from m:312 (PIN-13);
- the power figure of record at m:190's base case, with an odd-n split and the sham pooled (PIN-3).

**C7. Open, each due by its own stage, not blocking LOCK v0.1.**

- the Clock's boundary-day comparison (step-3 note 55; the analyzer takes it as a declared input), due by the first
  Clock date;
- which column of the per-property table f1's 7-vs-1 refers to (G-PORT A5; interim PIN-12 adds
  `sessions_excluded_any_phase`), due before step 17's entry;
- G-ANL-F3's versioning (m:291, "`m_analyze.py` extended"; PIN-14), due before step 19;
- the pass bar for the posting's re-run on the posted text (m:278), due before the v1 posting.

**C8. The first manifest run, set aside by Code without a seat ruling.**

- It ran on `64df36b` (`ea985c11…`). Code set it aside uncommitted when the verification of Code's closing edit found
  the gap `b62af85` closes.
- Code read PIN-37's `git mv` supersession as covering committed artifacts only (G-PORT's precedent). PIN-37's text
  states no such limit. Whether this set-aside needed the seat's ruling is the seat's to say.
- The G-ANL-F0 entry also corrects the G-SHAPE-F0 entry's statement that G-ANL-F0's "run of record was made at 11:38
  UTC". That run was set aside; the run of record is the 12:12:52 UTC run on `b62af85`.

**C9. Build gaps, flagged and not patched.**

- `stages.py` has no path for recording a seat adjudication of a fired end look on a terminal campaign.
- No end look is evaluated on a STOP-ended campaign.

## D. LOCK v0.1 wiring (step 9): Code's proposals, for the seat's word

**D1. State each gate artifact's package hash and the diffs between them.**

| Gate | `package_sha256` | Package at |
|---|---|---|
| G-PORT | `96fbcacf…` | `54e41c9` |
| G-CAL | `4b49658739523c60…` | `c75d4d8` |
| G-SHAPE-F0 and G-ANL-F0 | `06ab1430…` | `d092078` |

`64df36b` and `b62af85` touch nothing under `valence_core/`. The diffs:

- `54e41c9..c75d4d8 -- valence_core/m`: `gcal.py` added, `__init__.py` edited;
- `c75d4d8..d092078 -- valence_core/m`: `gshape.py` alone.

The lock also states each artifact's import closure outside the package: G-ANL-F0's `closure_sha256` `a3bc7bb9…` (15
modules and one data file; PIN-1) and G-SHAPE-F0's `import_closure_digest` `23abe773…` (14 files). The critic's LOCK
hazard correction (build-inputs raw) also has the lock's `valence_core/m` diff show no SCORING_STACK_FILES; D3's
sources-map comparison carries that condition.

**D2. Require `analyzer_sha256` and `package_sha256` in the stages' `identity_extra` on non-stub runs.**

- Today the first is optional, and nothing checks the second against the lock at stage start.
- This is a `stages.py` change, so it moves `package_sha256`.
- **G-SHAPE-F0.** `stages.py` is not in its scoring-stack map, so it does not re-run, but the lock states the new
  package.
- **G-ANL-F0.** The change would also move the package hash its manifest records (`06ab1430…`), and its battery
  exercises `stages` on the verdict path. Either G-ANL-F0 is re-run and its manifest superseded by hand `git mv`, or the
  lock states the diff. Which one is the seat's.

**D3. Compare G-SHAPE-F0's sources map with the lock's tree (its PIN-S10).** Any difference re-runs G-SHAPE-F0 first.

## E. Carried from earlier steps, flagged for the seat

**E1. Ruling (h): the exception Code kept as built, and Code's extension.** Dispositions entry, `54e41c9`; both are
flagged for the seat.

- **The exception.** At a G-TIME stage, a hair trigger or G-VER failure in the contrast session's forced phase is
  announced by its class (or the harness class), never by its round or n.
  - The report's counts still place the fired round as the last one generated. So at a forced hair stop the report
    carries both the class and the round position, which (h) withholds.
  - The fired round's text also stays in the stripped read under `reports/`.
  - That this falls under m:318 exception (1) is Code's reading, not the ruling's words.
- **The extension.** Code extended (h) to the stripped read: per forced round it keeps only {phase, ri, n, text}.

**E2. G-PORT's two borderline clauses** (G-PORT entry, `988e5df`).

- B1: extend (14) to "no encode limit on either path".
- B2: a clause stating that sham s no longer shares contrast s's cell, a consequence of (8) that nothing states.

**E3. G-PORT's four seat notes.**

- m:261's "rule of record" against m:308's domain;
- m:271's free-round v2 rule against the scaffold hair trigger;
- m:172's no-confound claim against π;
- the "unaffected" phrasing in (12) and (14).

**E4. G-PORT's 25 differences, plus 2 borderline, beyond §2.7's fourteen.** m:267 adds them to Appendix D through the
G-PORT entry; the seat may adjudicate any of them.

**E5. G-PORT's C1–C9, "Covered by §2.7, with a consequence the seat may want stated under the item."** They sit within
§2.7's fourteen, so they are not in E4's count. Examples:

- C1 (under (3)): f1's corrupted label delivered byte-clean text in 40 of 306 Q rounds, which bears on A0's
  comparison with f1's primary.
- C2 (under (6)): m's audit ends f1's s48 and s25 at the forced phase, where f1 continued.

E3's fourth note rests on A1 (the primary's domain, one of E4's differences), C1 and C2. In the G-PORT entry's words,
the phrase "should not read as unaffected overall, given A1, C1 and C2".

**E6. The step-3 dated notes.** These are the `05c4636` entry's "Dated notes (2026-10-06; minor-only, for the design
seat)", N1–N9, and the items in `results/raw/2026-10-06_m-v1.11_step3_notes.md`.

- The seat has ruled on one (at G-TIME-OLMo the STOP governs, `54e41c9`), and C7 carries note 55.
- Three bear on what LOCK-m-F0 v0.1 contains (m:279; m:176's Artifacts):
  - **Build pin 3 (notes #69, D8C1.38, contested):** the cross-template launch order at multi-template gate stages. It
    is declared at each unit's v0.1, and "The seat may direct otherwise". Code's default, built at step 4 as a PIN
    (`schedule.py`, `gate_launch_order`): strict rotation in §2.4's table order, contrast template first.
  - **Notes #25:** m:176's "the renders' sha256", a LOCK v0.1 artifact, has no stated serialization. Code's default, as
    built in `gcal.py`: the sha256 of the UTF-8 newline-joined renders, giving `a04f67b0…4372`.
  - **N9's D1.22:** condition (2)'s k and n_eligible are undefined for f1's Bernoulli corruptor at G-CAL's 0.12 replay
    (32 drawn against 31 changed). The note says the item "has never been dispositioned", and that the outcome is the
    same under every reading.

## F. For the PI (not the seat)

**F1. The laptop preflight before G-TIME-F0** (step 10, the next Qwen run).

- **The problem.** The one-process check flags any process run from the `jlens-qwen36` venv, including the audit
  session's model-free jobs. It held up completability by about 20 minutes.
- **It runs at launch only.** During completability the audit session kept working (its N13 raws were written at
  05:44:45 UTC), and whether a flagged process ran during the generations was not checked.
- **Code's default:** leave the check as it is, and launch Qwen stages when the audit session is idle.

**F2. The OLMo track** (from step 9, when a box exists). It needs the PI's go for a pod start, and the runpod MCP
re-authorised; it currently needs authorising through `/mcp`.
