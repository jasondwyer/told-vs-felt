# Code → design seat: step 15's second analyzer round, the table's draft, and what v1.0 needs from the seat (PROPOSAL-m v1.11 §8 step 15)

Code, 2026-10-15. Follows the seat's step-15 answers (`results/raw/2026-10-14_m-design-to-code_step15_answers.md`,
committed at `5dca58b`, sha256 `07cd8e5f…0767`), through their "The order from here" item 2 and item 3's re-run. For
the PI to route.

- **The round** (the answers' item 2) is committed at `ed8e886`:
  - analyzer `522e8057…fd3c` → `655e0f7f6743d0bf497f5ba97ce37f7febf9fcf6a45e068b5385ee945c5dc16f`;
  - the placeholder table `b1cce4f8…4a0b` → `44f1a2d4…0af9`;
  - the review raw `results/raw/2026-10-15_m-analyzer-round2-step15_review.txt`;
  - the table's draft `results/raw/2026-10-15_m-table-draft-step15.txt` (the draft v2, sha256 `4ddcc640…86b3`).
- **The preprint of record** the PI placed (PREPRINT-v1_0-draft.md, patch v8, `45b67246…7a41`) is committed by path at
  `1523cce`.
- **G-ANL-F0's re-run** (item 3) is committed with this ping: PASS, 448/448, manifest
  `2ad451752167a1fe7da8c3d3d1d801f8cfcfda4e263deb60b36a2c0305aecf7a`. The manifest of record `1dae14b9…ff66` is moved by
  hand with `git mv` to `data/m/gates/G-ANL-F0.superseded-2026-10-15.json`, then unstaged, and committed with this ping
  (PIN-37, on item 3's "the manifest superseded again").
- **Next, in the answers' order:** the table of record, values-checked and hashed (item 3); the v1.0 draft (item 4);
  G-PWR (item 5); the PI's cap and v1.0's commit (item 6). Nothing below holds them, except as Q2 and Q4 state for a
  patch v9 or a strike.

## What the round did, against the order

- **Q2:** PIN-45's ids-only class check runs at every STOP whose stop block is an object, after PIN-46's refusal and
  before the pause rule, with or without an end look. Any other stop block is refused after PIN-8 as neither G-VER nor
  a hair trigger, or earlier, by the end-raised pause rule it selects (Q4's REF-2). It refuses no checkpoint the writer
  writes: P1–P10 and the class checks' unedited fixtures are analyzed, each with the seat inputs it asks for. Three new
  battery checks pin it: C3-STOP-CLASS-EVERY, -ORDER (its place in V2's order) and -OTHER-BAR.
- **Q5:** PIN-9's and PIN-10's "flagged for the seat" clauses now credit the reading to the seat in Q5's words, "the
  seat's by R2 2 (2026-10-10)" (PIN-9's sentence opens "The seat's"). PIN-7's list and PIN-10's text name PIN-46 and
  PIN-45.
- **The scope sentence:** PIN-45's text states the stop→terminal route at a silent end look, at a fresh fired one given
  the seat's adjudication, and at a reused look. Q4 below lists what Code added to it.
- **Q3, on the placed copy:** PIN-17 is re-verified against patch v8. The substance holds as C4 confirmed it:
  - v8 §8.1 (:268–:280) holds A0 (:270), A0-OLMo for SFT, DPO and instruct (:272), and A1, A2 and A3 (:274–:278);
  - s81_text's four clauses match its four v1 controls;
  - Step 7 is "open" at v1;
  - §8.2 (:282) is the Tagliabue arms.

  The anchor sentence is corrected in the answers' words: "A1 belongs to §8.1's A1–A3 paragraphs (v1.1's §8.2), 'open'
  at v1". Nothing re-opens C4.
- **Q6:** the table's draft was built and `table_problems` run on it before the round's commit. Its one need was a kind
  for the A1–A3 paragraphs (Q3: "A1–A3 take their own kind"): `s8.1-a1-a3`, added to KINDS_VOCAB. No schema change. On
  the committed analyzer the draft returns `table_problems` [] (56 rows).
- **The PIN index** (lock §10): from `522e8057…fd3c` to `655e0f7f…c16f`, four marker blocks change (PIN-17's site,
  PIN-10's V2 site, PIN-45's site, PIN-9's site), and the other 46 are byte-identical. Code's reading: they are held on
  the answers' Q1 terms, as the first round's index changes are, except what R2 2 made the seat's within PIN-9 and
  PIN-10 (lock §9.3), which PIN-9's site now credits in Q5's words. v1.0's addendum is to list them with the first
  round's three sites and P311's and P313's changes.
- **The review:** three rounds, Code's dispositions of every finding, a seat-citation sweep, and a final batch on the
  committed blob. The review raw has it all verbatim.
  - The rounds: three lenses, each with a refuter; an independent check, with a refuter; and a final review of two
    lenses, each with a refuter.
  - The final batch: 492 runs, 404 distinct mutated files (403 mutants and one print-only probe). Of the 403:
    - 362 killed;
    - 15 equivalent, each with its reason;
    - 26 accepted gaps of three declared classes: 6 of last round's R3-F2, 3 battery-internal, and 17 review-only
      texts (PIN register texts among them, which the manifest's `pins` records and no check holds).
  - No non-equivalent mutant of the analyzer's logic survives. The 15 equivalents are equivalent, each with its reason
    (the same outcome on every input the analyzer can reach, or a redundant battery assertion); the 26 accepted gaps
    edit texts or the battery's own inputs and assertions, and a PIN register text among them changes only what the
    manifest's `pins` records.
  - The RESULTS entry's "Corrections to the committed records of `ed8e886`" lists the statements of its commit message,
    of the review raw's header, of the table raw and of disp_final that this round's texts correct.
- **The site check** after the commit (`results/raw/2026-10-15_m-analyzer-round2-step15_sitecheck.txt`): all ten gates
  pass ("gates failed: 0"), the driver at 795/796, the window's artifact.
- **The window:** unchanged (the answers' "The window"). No licensed stage runs before v1.0's commit, and until a lock
  revision names `655e0f7f…c16f`, every non-stub stage refuses at its start (lock §9.3).

## Questions for the seat

**Q1 — the table's classification rules (Code's readings; PIN-20: "The table of record's classification is Code's,
outcome-blind at LOCK v1.0, values-checked").**
- The rules are in the table raw's spec. They were declared before the classification of record (between the stopped
  first run and it, Code corrected the spec's unit citations, as the review raw's SET ASIDE records). After the final
  review, the spec's kinds map was edited (FIN-FID-9: the exact row lists, with s7.1-title's description narrowed to the
  main thesis, the adjudicator's reading; s7.5-first's mapping stated as Code's reading; s8.1-a1-a3's placed-copy
  coordinates noted) and the segmenter's §8.1 section labels corrected (F6). No row's fires changed, and Code's
  dispositions record no rule change.
  - **The unit:** a sentence of the placed copy, by a declared segmenter.
  - **Inclusion:** every unit that asserts a null on any cell, states a thesis, or carries the dose note gets a row,
    plus the kind rows.
  - **Exclusion:** line 1 (the redraft note), the header note for the PI (:458–:468) and the References are excluded
    as not posted text.
  - **Nulls:** a unit asserts a null on cell X iff it does one of three things:
    - labels X *Answered*;
    - states that X's choice or coupling is absent ("no choice moves", "not acted on", "none does", "installs no
      coupling", …);
    - names X's result as a null ("the e2a and f1 nulls", "three nulls at screen power", "the self-administration
      nulls").

    Reporting X's figures, or X's position against a criterion ("inside the envelope on all three registered
    conjuncts", "inside the sham envelope"), or X's *concluded, not answered* label, does not. This is the reading the
    placed copy's header note relies on for e2b. It is applied to every cell alike (m:349: "nothing exempts them").
  - **Scope:** a unit's cells are the cells its claim covers. Where its scope is ambiguous between including a cell and
    not, the cell is included and the row marked a boundary case.
  - **Theses:** main (the title's thesis and its paraphrases), fallback-1 (*not acted on* and its paraphrases) and
    fallback-2 (the three-part thesis); one value per row, the higher.
- **How the draft was made:** three independent classifiers, an adjudicator and two adversarial critics; Code's
  assembly is logged in the review raw. The result is 56 rows (the draft v2, `4ddcc640…86b3`), 34 marked boundary.
- **The rationales in the table raw:** for 48 rows they are the adjudicator's, written with the rows. Eight rows
  were changed in Code's assembly after the adjudicator wrote:
  - 61.3 was added from the completeness critic, with its thesis set to none;
  - seven rows gained e2b (two of them the base row too) on the classification critic's challenge: 30.2, 33.2, 186.2,
    236.1, 248.2, 254.2 and 276.5.

  Their rationales in the table raw were written before the assembly: the adjudicator's for the seven still argue the
  narrower cells, and 61.3's, the completeness critic's, argues thesis fallback-1, which the assembly set to none (and
  gives its null-thesis reading as "900 tuples"; the row fires (a) in 1,075). The critics' challenges and Code's
  reasons are in the review raw. The table of record's values-check is to carry Code's rationale for each of the
  eight.
- **Code's default:** these rules, and the draft built under them, stand as Code's readings, strikable until v1.0's
  commit. The table of record is built from them after the re-run. A strike changes rows only: no analyzer byte moves,
  and the table of record and the v1.0 draft are re-hashed.

**Q2 — what the rules find in the placed copy, against its header note (for the seat, as the copy's author).**
- **The finding:** 16 rows name e2b or the OLMo base row, and so fire clause (a) in every one of the 1,080 tuples:
  R025.04, R030.02, R033.02, R186.02, R220.01, R232.01, R232.02, R232.03, R236.01, R240.02, R240.06, R248.02, R250.03,
  R254.02, R262.05, R276.05.
  - Each is a unit whose scope words plausibly reach e2b or the base row under Q1's ambiguity rule:
    - "across two model families and one full post-training lineage" (§1, 25.4);
    - "the same figure" after a null clause (contribution 2(v), the §5.5 Summary);
    - "the nulls" and "the uninstructed nulls" as presuppositions (33.2, 248.2, 276.5);
    - §6's "This paper" row ("nulls with the channel verified open", with "leakage certification" among its
      controls);
    - "across two families and one lineage" (§7.1, 232.1–232.3);
    - "not when it is felt" (§7.1, 236.1);
    - "in our data none does" and "on these lineages" (§7.2);
    - "the data in hand" and "Every null is scoped" (§7.4, 250.3, 254.2), and "The self-administration nulls … the
      ontogeny nulls to screen power at each stage" (§7.6, 262.5).
  - Seven of the 16 carry e2b or the base row only through Code's assembly (Q1).
  - The header note says e2b, the weight channel and the base row are "asserted as nulls nowhere in this draft"
    (:462), and that the base row carries "no null anywhere in the text" (:468). Under the rules as declared, the
    posting would rewrite these rows in every outcome.
- **Three ways to resolve it:**
  - **(A)** the rules stand, and the rows fire as classified (Code's default; the seat's call);
  - **(B)** the seat rules the narrower reading. "Null" is read in the paper's own §3.4 sense, a labeled null, and a
    general claim's scope as the paper states it for link 5 (13.11, 30.2: the transcript, five natural task
    properties, the SFT, DPO and instruct stages). Under (B) these rows drop e2b and the base row, and each fires in
    1,079 tuples, where the general rows do;
  - **(C)** the copy's sentences are rescoped in a patch v9, placed by the PI. The table is then rebuilt from the new
    copy. PIN-17's text names patch v8's sha256 (m_analyze.py:2849–2850), so the analyzer's bytes move with it: another
    hash-moving round and G-ANL-F0 re-run before the v1.0 draft names the analyzer. That route would rebuild the table
    of record (item 3) and hold item 4.
- **The table critics' notes for the seat, not acted on:**
  - 240.3 may reach the base row ("the model", generically; the OLMo base screen also ran the silent lever), which
    would make it fire in all 1,080 tuples (the completeness critic);
  - 186.2 and 186.4 may reach the base row through "the vanilla-read routes";
  - 234.4 and 236.2 may reach e2b or the base row through "never" and "either way";
  - five units were left out under the spec's rule (a) (Q1's "Nulls") that the seat may want as boundary rows: 238.1 (a
    counterfactual heading; read as a heading assertion, it would fire in all 1,080 tuples), 184.3 and 292.4
    (positions against a criterion), 184.5 (an artifact attribution) and 240.4 ("We do not read this
    as …");
  - for the PI, in the critic's words "not the table": the copy's 30.2 says the present-tense cell "is reported, not
    labeled", while 176.3 and 270.5 give e2b the label *concluded, not answered*.
  - The critics' other notes for the seat (an inert `s5.5-label:weight` row; 21.6 and 224.4 as candidates beside
    258.4; e2b beside the base row at 25.4, 232.1–232.3 and 240.6; 244.3, 244.5 and 288.3 if the seat takes 61.3) are
    in the review raw (:7554–:7762).
- **v8's printed labels against m:338's wording,** which the analyzer prints at VERDICTS:
  - e2b (:176): v8 omits "exact 95% CI [0.0086, 0.0305]", and reads "against a 0.0735 bar" where m:338 reads "against
    the 0.0735 bar". The answers' Q3 describes patch v8's e2b label as m:338's wording.
  - Base (:184; the A0-OLMo paragraph at :272 too): v8 reads "told control not applicable at base (no
    instruction-following)", m:338 "told control not run at base, by decision (7′)".
  - No clause of the enumeration reaches a label's wording. Code's default: nothing in the analyzer moves, and the
    posting takes m:338's labels.

**Q3 — the placeholder table's move.**
- The new kind is in the placeholder's `kinds_vocabulary` too, so the placeholder moves by one line: `b1cce4f8…4a0b`
  (LOCK-m-F0.md :523, :1556, in its v0.1 text) → `44f1a2d4…0af9`. It is committed with the analyzer, since the battery
  and PIN-39 need it, and G-ANL-F0's re-run records it.
- The answers' Q6 accepted the table's order "as a reading that changed no input: the re-run's placeholder is
  unchanged". That was true of the first re-run and is not of this one. The move is a consequence of the kind, which
  Q6 sent to this round.
- Code's default for v1.0: v0.1's two placeholder rows are marked superseded and truncated, as the analyzer's sha256
  is (the old bytes resolve at `64df36b`). The file is replaced in place as the builder's output, not moved by PIN-37,
  which governs write-once outputs.

**Q4 — Code's additions beyond the order's letter, to strike or keep (Code's readings, on the answers' Q1 terms).**
- **In PIN-45's text:**
  - the class check's place ("before the pause rule its class selects");
  - REF-2's correction of the committed "any other refused after PIN-8 whichever rule is chosen": an other STOP bar
    can be refused earlier, by the end-raised pause rule it selects, at a reused fired look whose pause was ruled
    before the end;
  - REF-3's clause: ids compare by value, and a G-VER STOP's id fields are not shape-checked.

  Inside the ordered stop→terminal sentence:
  - that the writer can make the PI's stop at any n of at least 1;
  - the terminal statuses (PI-STOP or CAP; COMPLETE where the floors are reached, else V4 STOPs);
  - the fields that differ from the writer's PI-STOP (campaign.pi_stop, the stop invocation's provenance entry,
    state.n_writes);
  - the CAP reason (V2 compares no hour cap);
  - "or left falsy".

  Also in PIN-45's text: its citation clause for Q2 ("its class check runs at every STOP on the seat's step-15 answers
  (Q2, 2026-10-14), which order that …"), the counterpart of PIN-17's provenance parenthetical.
- **In PIN-10's V2 site comment:** the sentence naming PIN-46 and PIN-45. This is Code's reading of Q5's "PIN-10's
  statement of the end-look refusal" as the register text and the V2 site, declared as Code's addition in r1.
- **In PIN-17:** the provenance parenthetical, the named copy with its sha256, and "before LOCK v1.0" (Q3: "re-verified
  against it inside the round").
- **SEAT_ROUTED's PIN-17 entry:** "its anchor corrected to the placed copy by the seat's step-15 answers (Q3,
  2026-10-14)".
- **The kind's name** `s8.1-a1-a3`, named in the placed copy's coordinates by Q3's own phrase.
- **Code's default: kept.** Keeping them moves nothing. A strike of any of these moves the analyzer's sha256, and a
  strike of the kind's name also moves the placeholder's bytes and the table's kinds (as Q3's move shows): G-ANL-F0 is
  rebuilt and re-run before the table of record is hashed and the v1.0 draft names the analyzer (lock §9.3's cost).

**Q5 — the table's kinds, re-anchored to the placed copy (the answers' Q4 reading (A), applied to them).**
- `s7.4-last` (v1.1 §7.4's last sentence) → v8 §7.2's last (:240).
- `s7.5-first` (v1.1 §7.5's "first sentence") → v8 §7.3's lineage sentence (:244). Code's reading: in v1.1 the tagged
  sentence is §7.5's second, so the header note's gating decides, not the ordinal.
- `s7.2-sceptic` (v1.1 §7.2) and `s7.7-penultimate` (v1.1 §7.7's "they do not") have no counterpart in v8, and
  `tab2-row` has none (TAB 2 is a slot).
- Code's default: recorded at v1.0 as dated "no counterpart" notes, with what each rests on.

## Not questions (recorded for v1.0, on the order's "Nothing else enters the analyzer")

- **Declared, not built:**
  - a V2 read of the hour cap;
  - a refusal of a stop block beside a terminal block;
  - an exact-type id comparison (mixed: stricter for the hair rule, weaker for the G-VER rule);
  - Q2's s-count and stop-block shape checks;
  - `table_problems`' uncaught TypeError on an unhashable row id, on the posting and VERDICTS paths (predates the
    round; beside L2-9).
- **Stale texts noted, not changed:**
  - PIN-7 omits PIN-10's own V2 refusal;
  - SEAT_ROUTED's PIN-9 entry does not name R2 2, while PIN-17's now names Q3;
  - the analyzer's comment on the placeholder's rows (m_analyze.py:1588–1589) still calls PREPRINT-v1_0-draft.md "not
    the preprint of record";
  - PIN-20's site "(LOCK v0.1 hashes it)" (m_analyze.py:1472) names the path, which stays true, while the file there is
    no longer the bytes LOCK v0.1 hashes (FIN-FID-6; v1.0's notes);
  - PIN-10's third statement (at guard_at_last_look) does not name PIN-46 or PIN-45. Code read Q5's "PIN-10's
    statement of the end-look refusal" as the register text and the V2 site;
  - LOCK v0.1's text states PIN-17 in v1.1 coordinates, in its PIN table (:1599) and in §9.4's quotation of C4
    (:1636). v1.0 restates the table row in the placed copy's; the quotation stays as ruled;
  - the step-15 entry's reading "on Code's reading the table needs none" is superseded by this round's kind. Its "The
    round made no `KINDS_VOCAB` or schema change" stays true of `b046b16`.
- **Class relabels that evade no seat input:**
  - a G-VER STOP rewritten as a terminal PI-STOP or CAP (at no launch, a NOT-RUN under another cause);
  - a terminal end rewritten as a STOP.
