# Code → design seat: step 15's questions, after the analyzer round (PROPOSAL-m v1.11 §8 step 15)

Code, 2026-10-14 (PI-local date). For the PI to route. This block carries no stamp; the entry's stamps are Code's, UTC.

Read for it:
- this block;
- RESULTS.md's entry `2026-10-14 — THE R2 3 ANALYZER ROUND AND THE G-ANL-F0 RE-RUN`, with its "Corrections to
  `b046b16`'s records";
- the G-F0m-Qwen close line ("The preprint");
- the review raw `results/raw/2026-10-14_m-analyzer-round-step15_review.txt` (committed at `b046b16`): the PIN texts
  verbatim in its header, then every round. Read it with the entry's corrections;
- `LOCK-m-F0.md` (v0.2, `db7d970`) and its v0.1 text: §1 (:519–:524, :558–:560), §§9.3–9.6, §10 (:1706), §11 items 5
  and 8;
- the seat's R1 (A2, C4, C6, C7) and R2 (items 2 and 3);
- the step-10 read's Q1 and §2 items 3 and 5;
- the step-14 read's Q2, Q3, Q4, §4 and "What Code does now" item 2;
- `PREPRINT-v1_0-draft.md` :176 and :268–:282;
- `valence_core/m/bars.py:232–236` (P024) and `valence_core/m/stages.py:2306–2310`;
- m:14, m:16, m:58, m:190, m:192, m:210, m:285, m:286, m:316, m:324, m:330, m:338, m:343, m:355, m:356 and m:371.

**The short form.**
- R2 3's three analyzer edits are built, reviewed and committed at `b046b16`. The analyzer moves from `66fb5214…7d5e`
  to `522e80576659aff1818239105c3e9b2b76d4b222e8959ac9fdd8dfb499fefd3c`.
- G-ANL-F0 re-ran on it: PASS, 444/444. The new manifest is `1dae14b9…ff66`, and the old one was moved by `git mv`
  (PIN-37).
- Next in step 15, in the PI's word's order and the read's ("What Code does now" item 2), the table's place in it
  Code's reading (Q6):
  1. the sentence table of record, on the PI's word to Code on PI 1 (on the copy it names, or, if it names none, from
     the root copy on §4 item 3's default); until a word reaches Code, the table waits;
  2. the v1.0 draft naming this analyzer;
  3. G-PWR on the uncached path with r = 18/24;
  4. the PI's cap;
  5. v1.0's commit.
- Seven questions for the seat follow, and four items for the PI. Each question has the reading Code acts on without
  an answer, and what an answer costs (Q6's, an ordered re-run, is one run on unchanged inputs).
- Without an answer, none stops the work before v1.0's commit. An answer adopting Q4's reading (B) could hold v1.0
  under m:355's rule.
- Four can bear on the analyzer's bytes: Q1's terms; Q2, if the seat orders a check or a stated limit; Q3, if it
  orders a PIN-17 change; Q5, if it wants stale texts corrected.
  - An answer that strikes or adds there moves the analyzer once more, re-runs G-ANL-F0 (its manifest superseded
    again) and redraws the v1.0 draft.
  - After G-PWR has run, it would also fall after R2 3's "names the new analyzer sha256 before G-PWR". Whether G-PWR
    then re-runs would be the seat's to say. So such answers are cheapest before G-PWR.
- Q3 and Q4 bear on the sentence table and on v1.0's text. The table is built on the PI's word on PI 1 unless the PI
  holds it for them (PI 4), and an answer that arrives after it rebuilds the table. Q7 bears on G-PWR's figures. Q6 is
  about this round's order.

## For the PI (the PI's items; not the seat's)

**PI 1 — the preprint of record: which copy, and by when.**
- The record:
  - m:58 (v1.11) records the preprint of record as "the PI's redraft from v1.1, placed at root by the PI before
    LOCK-m-F0 v1.0 and hashed there; its §8.1/§8.2 and header note name the cells this campaign gates".
  - The PI's v1.7 routing of 2026-10-04 lists it as to come: "the preprint of record at root (my redraft from
    PREPRINT-v1_1-draft.md), before step 15" (RESULTS.md@6920b4b:4541–4542).
  - The v1.8 routing of the same date lists "the preprint of record at root before step 15", naming no source
    (RESULTS.md@6920b4b:4334).
  - The step-14 read §4 item 3: "the PI's item. The root copy at patch v7 is the tagged one and stands unless the PI
    places another; the sentence table of record is built from whatever is placed, so the Q-F0 sentences (the e2a and
    f1 labels, the title clauses) should be final in that copy".
- `PREPRINT-v1_1-draft.md` is not on disk.
- The root copy, `PREPRINT-v1_0-draft.md` at patch v7 (sha256 `d9635ca2…1fe6`, the blob tagged by
  `note-2026-10-v1`), carries none of the five items m:58 lists for patch v5. The G-F0m-Qwen close line ("The
  preprint") lists them, among them:
  - e2b's label "*Answered.*" at :176, where m:338's e2b label is never *Answered*;
  - the "reasoning block removed" phrase at :278.
  Q3 below gives what follows for §8.
- **The question:** does the root copy stand, with the Q-F0 sentences (the e2a and f1 labels, the title clauses)
  final in it, as §4 item 3 asks ("should be final in that copy")? Or does the PI place another copy?
- **The window:** Code builds the table on the PI's word to Code on this item, which can come with this block's
  routing: on the copy it names, or, if it names none, from the root copy on §4 item 3's default, as the close line
  reads it. Until a word from the PI reaches Code, the table waits.
  - A copy placed before Code builds the table costs no rebuild. One placed after it means the table is rebuilt and
    values-checked again.
  - If the copy's sentences need a `KINDS_VOCAB` or schema change, that is an analyzer edit beyond R2 3: it goes to the
    seat first, moves the analyzer and re-runs G-ANL-F0.
- **The deadline:** m:356 (and m:58 in the same words) says "before step 15 or before any posting, whichever comes
  first", and step 15 began after `5af9e07`. On §4 item 3's default, the root copy has been at root since before step
  15; whether that meets m:356, for a copy m:58 describes as the PI's redraft from v1.1, is the PI's to say. A copy
  placed now meets m:286's "before this lock" but not m:356's. The step-14 read's §4 lists the placement inside
  step 15, under m:286 (item 3). How m:356's deadline and §4's placement read together for a copy still to come is not
  Code's to settle (the close line).
- If the PI places a redraft, a new root file name keeps the tagged note release's file (`PREPRINT-v1_0-draft.md`,
  which the note's audit scripts pin at `d9635ca2…`) from moving. The table records the path it was built from.

**PI 2 — v1.1's text, for the re-anchoring** (Q3, Q4). Placing `PREPRINT-v1_1-draft.md` on disk as a reference, not as
the copy of record, lets Code re-anchor against v1.1's text. Without it, Code re-anchors from the descriptions of v1.1
(Q4), and v1.0 says so.

**PI 3 — the decisions block** (`DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md`, sha256 `fab576d8…34f8`, untracked):
whether to commit it. Code's default: untracked, as at step 3 (the note below). Cost: untracked, the sha256 v1.0 names
binds bytes the repository does not hold (rule 27), as step 3's does now; committed, the file joins the tree at root and
the hashes resolve in the repository.

**PI 4 — what G-PWR and v1.0's commit wait on.**
- The PI's word makes v1.0's commit wait on the cap.
- Code proposes that no answer holds v1.0 except one adopting Q4's reading (B), which would hold it by its own rule.
  Answers to Q3 and Q4 are cheapest before the table is built; answers to Q1, Q2 and Q5 before G-PWR.
- Whether the table, G-PWR or v1.0 waits for the seat's answers is the PI's call. The table is built on the PI's word
  on PI 1, so answers to Q3 and Q4 reach Code before it only if the PI holds the table for them; otherwise an answer
  that changes the §8 mapping or the re-anchoring rebuilds the table and re-values-checks it.
- Without a word on this item, Code builds the table on PI 1's terms and runs G-PWR when the order reaches it.
- If v1.0 is not committed with a committer date in UTC on or before Q-F0's Clock date, 2026-10-30 (m's D1, m:16; lock
  §11 item 5; R1 C7's boundary day), Q-F0 is NOT-RUN (m:324). m:324 also gives the PI that path by declining to
  commit.

## Questions for the seat

**Q1 — the terms of the analyzer's new readings, and of its PIN-index changes.**
- What was built:
  - three register entries, PIN-44 (a), PIN-45 (b) and PIN-46 (c), their sites marked "declared at LOCK v1.0"; each
    new entry's text quotes its ruling and labels every reading beyond it as Code's;
  - PIN-26's text, extended with the posting's exit 5.
- The PIN index (lock §1 :524; lock §10; C6's terms extended to it, the step-10 read §2 item 3). By the index's
  extraction rule, `b046b16`:
  - adds three sites marked "declared at LOCK v1.0" (`m_analyze.py:2024` PIN-46, `:2050` PIN-45, `:2546` PIN-44);
  - extends P313, PIN-26's site comment (now `:7935`), with the posting's exit 5;
  - drops P311, the STR-PIN-COMMENTS label that carried the marker literally (the check is now exact by version; v0.1
    markers 48 → 47).
  The 46 other marker blocks are byte-identical and move line only (Code's mechanical comparison). The step-14 read's
  Q2 gave v1.0's addendum its form for the driver's sites. Code's default for the analyzer is the same form: v1.0's
  addendum lists the three new sites on the terms below, P313's new text, and P311 as no longer a marker block. The
  v0.1 index is not edited.
- The review raw lists every reading, each Code's: the build spec's "Code's readings to build" (round 1); the round-3
  fixer report's §3 (cumulative beyond the spec); round 4's report; and Code's round-4 dispositions (r5: F-1's limit
  sentence). Among them:
  - (a)'s scope: posted-kind runs only; an of-record run records the bar as not applicable;
  - the rewrite list's form and its committed-at-HEAD rule;
  - the comparator: Q-F0's VERDICTS output, else the posting's own of-record output, identity-checked;
  - the comparison is reported and decides nothing; PASS or FAIL is the bar alone;
  - `changed` against `moved`;
  - a FAIL writes nothing and exits 5;
  - (b)'s reading of "fired" through a reused look;
  - an end-raised pause is the last one and unadjudicated, and a reused cadence pause is ruled by a str (`""` accepted
    as a str: round 2's R2BC-4; listed in round 4's report);
  - (b)'s id check on the end's class at a STOP whose end look fired;
  - (c) at every recorded end look, with a reused look's own count.
    - That is wider than Code's own round-2 block, whose item (c) R2 3 ordered built under the block's heading, and
      which described (c) at the STOP ("`end_look.at_launches` equals the launches recorded at the STOP").
    - PIN-46 says so.
    - Code built the widening without asking first, on its reading that it is within R2 3's words: R2 3 orders "(c)
      the end look's launch count", the block's heading, which names no STOP. So, on that reading, the widening is not
      an edit beyond the order (the step-10 read §2 item 5) the way R3M-5's check is (Q2).
    - If the seat reads (c) as the block's STOP-only description, the widening is a departure, and striking it costs
      the short form's.
- The record's terms:
  - The step-14 read's Q2 holds the driver's v1.0-declared sites "strikable from the step-14 commit until LOCK v1.0's
    commit, the same close as the register's".
  - Lock §11 item 5: "C6's strike window closes at v1.0".
  - No ruling yet states the terms of analyzer entries, or analyzer index sites, first declared at v1.0.
- Code's reading: the same terms, strikable from `b046b16` until v1.0's commit. Without a word, that stands.
- Cost: the short form's. After v1.0, such a reading would be corrected "only as a register entry is, by a disclosed
  amendment or at a hash-moving round" (the step-14 read's Q2, its words for a driver reading).

**Q2 — R3M-5: PIN-45's class check, only at a fired end look or at every STOP; and what stays open either way.**
- PIN-45 checks a STOP's recorded class by ids, against the writer's own assertions: a hair-trigger STOP's (template,
  s) is the last session recorded, and a G-VER STOP's is none of them. It runs at a STOP whose end look fired.
- At a silent end look, a one-field hand edit of a hair-trigger STOP (its `stop.bar` set to a G-VER bar) therefore
  passes. VERDICTS then requires no PI-stop record (PIN-8, which lock §9.3's index labels "a hair-trigger STOP needs a
  PI-stop record").
- Running the same ids-only check at every STOP closes that one-field relabel.
  - It refuses no checkpoint the writer writes: `stages._stop_end_look` asserts both id rules at every STOP, before the
    fired/silent split (`stages.py:2306–2310`).
  - Its mutant `n:cls-every-stop` also survives the battery at 444/444, with the end paths P1–P10 among its cases.
- It does not close every route around PIN-8 (R3M-5 and its refuter, the review raw's round 3; PIN-45's limits). With
  or without it, two hand edits of a hair-trigger STOP reach VERDICTS without a PI-stop record:
  - its stop block replaced by a terminal PI-STOP block, at a silent end look and at a fresh fired one given the
    adjudication (PIN-45's text states this only at a reused look);
  - its bar relabelled G-VER with its (template, s) moved off the record, at any end look (PIN-45 states it generally,
    adding that at a reused look the pause is given a ruling).
  Ids cannot tell the first from a legitimate end, nor the second where the id is moved to its arm's next launch;
  elsewhere the second passes only because V2 checks a G-VER STOP's id against the record alone.
- The reviewers left two further candidates, neither built:
  - an ids-only check that a G-VER STOP's s equals the count of its template's recorded sessions (round 4, F-1 and its
    refuter), which narrows the second route to the arm's next-launch id;
  - a stop-block shape check on non-id fields, which would be a new refusal (rounds 2 and 3).
- The R3M-5 extension guards PIN-8's input, not (b). The two candidates guard the end's class, which PIN-8 reads and
  which, at a reused look, chooses (b)'s rule; each would be a new refusal beyond the writer's own assertions. All three
  are beyond R2 3's three edits as built ("put to the seat before Code acts on it", the step-10 read §2 item 5).
- Code's default: none built, and the stop→terminal route's wider scope (at a silent or a fresh fired end look) not
  added to PIN-45's or PIN-8's text. PIN-45 states that route at a reused look only, and the G-VER relabel generally.
- Cost: if the seat orders a check, or orders a limit stated in a text, it lands before v1.0 at the short form's cost.

**Q3 — PIN-17 and Step 7 against the placed preprint (R1 C4: "Re-verified against the placed preprint at LOCK v1.0").**
- PIN-17's text: "Confirmed by the seat (C4, 2026-10-10): §8.1 text = one clause per control with a v1 coordinate (A0,
  A0-OLMo-sft/-dpo/-instruct) with m:343's tokens; A1 belongs to §8.2, 'open' at v1; re-verified against the placed
  preprint at LOCK v1.0."
- m:343 (Step 7): §8.2's sentences "state whether its cells ran; §8.2 is closed into §5.7 iff L1 ∧ A2 = PASS ∧ A3\* =
  NULL, otherwise open with each cell's outcome, f2's included; "open" at v1 by construction".
- In the root copy:
  - §8.1 (:268–:280) holds all seven cells: A0 (:270), A0-OLMo (:272), A1 (:274), A2 (:276) and A3 (:278), and the
    outcome rules (:280).
  - §8.2 (:282) is "The two missing arms" (the Tagliabue arms) and carries none of this campaign's cells.
- So, against the root copy:
  - PIN-17's substance holds: the controls with a v1 coordinate are A0 and A0-OLMo; A1 has none at v1.
  - Its anchor ("A1 belongs to §8.2") and Step 7's §8.2 point at the root copy's §8.2 (:282), which carries none of
    this campaign's cells.
- If the PI places a redraft from v1.1 whose §8.1/§8.2 "name the cells this campaign gates" (m:58), the question is
  moot.
- Code's default, if the root copy stands:
  - PIN-17's text unchanged;
  - v1.0 records the re-verification (substance holds, anchor differs);
  - v1.0 maps v1.1's "§8.2" to the root copy's A1–A3 paragraphs (:274–:278), as m:58's re-anchoring (Q4), resting on
    the descriptions of v1.1 unless the PI places v1.1's text (PI 2);
  - Step 7's §8.2 status then reads those paragraphs.
- Bears on:
  - the sentence table of record. On Code's mapping, `s8.1-status` rows are A0 (:270) and A0-OLMo (:272), not A1–A3
    (:274–:278). An answer that changes the mapping after the table is built rebuilds and re-values-checks it;
  - v1.0's text;
  - the analyzer, only if the seat orders PIN-17 changed.

**Q4 — m:58's re-anchoring, m:371's deferred referents, and whether a referent with no counterpart STOPs v1.0.**
- The governing words:
  - m:58: "Until it is placed, every reference to v1.1 sections resolves against the project copy and is re-anchored
    by Code at LOCK-m-F0 v1.0; §9 scopes those referents there."
  - m:371 (in §9, "Referents Code verifies at commit"): "`PREPRINT-v1_1-draft.md` and the PI's placed redraft —
    scoped to LOCK-m-F0 v1.0 (step 15), not to step 2; at step 2 Code records them as deferred by design".
  - m:355 (step 2): "any unresolved substantive item → STOP".
- The v1.1 project copy is not on disk (m:58: "not on disk at STOP-6"). So these references resolve against no file
  in the repository (STOP-5, the v1.7 referent check, item A8, RESULTS.md@6920b4b:4631–4635):
  - §0.1's §8.2;
  - Step 7's "§8.2 status";
  - Step 4's "§8.2's screen";
  - §7.4's "§8.2 stays open";
  - the v1.1-only items of §7.5's seed list;
  - the §7.6 number of Step 6's rival (m:14 maps the rival to root:248).
- Code knows v1.1's sections only through descriptions of them: PROPOSAL-m's, which are of record, and the untracked
  design handoff's section-level notes (`HANDOFF-2026-10-04-design.md`:26, :29). Neither gives §8's text, and Q3's
  mapping rests on PROPOSAL-m's.
- Reading (A), Code's default: m:58 schedules a re-anchoring, not a second check.
  - Code re-anchors each reference where a counterpart exists, and records "no counterpart" where none does.
  - Each is a dated note in v1.0, saying what it rests on.
  - Cost: none to the schedule.
- Reading (B): m:371 moves step 2's check for these referents to v1.0, with its rule.
  - An unresolved substantive referent STOPs v1.0 for re-specification: a gated §8.2 sentence (m:14 gates "§8.1 and
    §8.2 of the preprint"), or a v1.1-only §7.5 seed item with no counterpart.
  - Minor residues become dated notes if the PI's routing adopts the e9b5022 precedent for v1.0, as m:355 made it the
    PI's routing's to adopt at step 2. That is the PI's to say.
  - Cost: v1.0 waits, and Q-F0 is NOT-RUN if v1.0 is not committed by 2026-10-30 (m:324; R1 C7).
- Under either reading, if the PI places v1.1's text on disk as a reference (PI 2), Code re-anchors against the text
  rather than the descriptions.
- Bears on: the sentence table of record, whose rows for the §7.5 seed list and §8 are built on this re-anchoring (an
  answer after the table is built rebuilds and re-values-checks it); v1.0's text; under (B), possibly v1.0's commit.

**Q5 — stale texts in PIN-7, PIN-9 and PIN-10.**
- PIN-9's text still reads "Code's reading, flagged for the seat", and PIN-10's "Code's reading of C3, flagged for the
  seat", over the pause raised at a STOP and its route. R2 item 2 made those readings the seat's ("Accepted as built,
  post hoc, and made the seat's by this ruling"), and lock v0.1 §§9.3 and 10 already record that.
- PIN-7's list of V2 structural refusals does not name the new PIN-45 and PIN-46 refusals, and neither does PIN-10's
  statement of the end-look refusal (the builder's report, the review raw's round 1, §6 item 5).
- R2 item 2 on texts:
  - "every text that says 'the seat's C9(ii)', 'the seat's C3' or 'the seat's D2' over the pause, the reuse, the
    route, the V2 refusal or the analyzer half of the stage-start check is accurate as of today, so none is amended;
    the entry and this file record that the attribution became true by ruling". PIN-9's and PIN-10's clauses are the
    reverse case: texts that still credit Code and flag for the seat, which the ruling made stale. No ruling speaks to
    them.
  - For the paraphrases of its rulings in the PIN texts it lists (PIN-9 among them, PIN-10 not): "a misparaphrase
    found later is a text correction at the next hash-moving round, not a reason to open one". Code reads this as
    covering misparaphrases of a ruling, which these clauses are not, so it did not apply it at `b046b16` (the entry).
- Lock §1 (:558–:560) left the same reverse case in `stages.py` "unamended, as no hash moves". That ground is Code's,
  and `b046b16` moved the analyzer's hash.
- Code's default: no change. v1.0 notes that R2 2 made the clauses the seat's, and lists the PIN-7 and PIN-10
  omissions.
- Cost: a correction now moves the analyzer again, at the short form's cost, and is cheapest before G-PWR. Without
  one, the clauses stand until a later hash-moving round, or are corrected after v1.0 only by a disclosed amendment.

**Q6 — the sentence table's place in the round.**
- The governing words:
  - The PI's word (2026-10-13): "Then go for step 15 in the read’s §4 order: the analyzer round and G-ANL-F0 re-run
    first, the v1.0 draft, G-PWR on the uncached path with r = 18/24; v1.0’s commit waits on my cap."
  - The read's §4 item 4: "**The three analyzer edits** (R2 3; v0.1 §9.6) built in one round with the sentence table,
    G-ANL-F0 re-run with its battery extended".
  - R2 3: "All three are built in one analyzer round at step 15, with the sentence table of record (m:278: the table
    is built from the placed preprint at LOCK v1.0), and G-ANL-F0 is re-run then".
  - The step-14 read's "What Code does now" item 2: "the analyzer round with the sentence table from the placed
    preprint and the G-ANL-F0 re-run".
- Read as written (R1 A2: "a list inside a §8 step is ordered as written"), the table is part of the analyzer round
  and precedes the re-run. Code's order departs from that letter unless "one analyzer round" is read as Code reads it.
- Code built and committed the analyzer, re-ran G-ANL-F0, and builds the table next, on the PI's word on PI 1, before
  the v1.0 draft. Built after the re-run and on that word, the table takes the PI's answer on the copy without a
  rebuild.
- The order was acted on before the seat was asked, so it is put here (R1 A2: "a reading that departs from a listed
  order is put to the seat before Code acts on it").
- It changes nothing the re-run took: "the placeholder table serves G-ANL-F0 only" (m:286), and the re-run's
  `placeholder` is unchanged.
- The cost of the order: on Code's reading the table needs no `KINDS_VOCAB` or schema change (`table_problems`
  accepts, per row, any kinds drawn from the vocabulary, empty included; the table needs one row of kind
  `f1-corr-line`).
  - If it does need one, that is an analyzer edit beyond R2 3's three: it goes to the seat first, moves the analyzer
    again, re-runs G-ANL-F0 and redraws the v1.0 draft.
  - Building the table before the re-run would have surfaced that need inside one round.
- Code's default: no re-run. If the seat reads the order as written, it is a departure. Code proposes it be accepted
  post hoc as one that changed no input (the placeholder is unchanged), as the step-14 read's Q4 accepted the `qual`
  build. Whether it is accepted, and whether anything re-runs, is the seat's. Cost: none to the inputs; an ordered
  re-run of G-ANL-F0 is one run on unchanged inputs (PIN-37: byte-identical).

**Q7 — G-PWR's methods.**
- The governing words:
  - m:285: "the exact sequential false-pause probabilities of §6 for that look count; the exclusion guard's
    false-pause figure";
  - m:330: "Code's exact sequential computation at p = p0 gives each unit's per-bar false-pause probabilities at that
    unit's G-PWR; the joint figure and the guard's beside";
  - m:316: the guard's "false-pause figure is reported at G-PWR with §6's".
- **The planning row.**
  - At k = 18 of 24 on the uncached path, m:210's row "| 20–17 | 128 | 64 | **192** | 5 |" gives L = 128 and 64,
    total 192, 5 looks.
  - Power at the floors (80, 32) is .878 ≥ .85 (m:190), so no n is raised.
  - Code recomputes both at G-PWR, where PIN-3's base case is re-derived with the planned floors (R1 C6; lock §11
    item 5).
- **(a) The n_j at each look** (PIN P024, `bars.py:232–236`: "G-PWR states its n_j assumption beside the figure").
  - No text gives a model of the realised rounds per look.
  - Code's default: the projection. Each arm launches to its L, interleaved by the campaign rule, and every sham
    session runs its 10 rounds.
  - Beside it:
    - the case where the sham arm leaves the rotation at its floor;
    - the sham arm at G-F0m-Qwen's measured 136 of 160 realised rounds (sham-only, as reported in the G-F0m-Qwen
      entry).
- **(b) The guard's figure.**
  - The absolute half has a p0 (.20 on Qwen), so its sequential figure is exact over the contrast arm's launches per
    look.
  - The Fisher half has none: it compares the contrast arm with its matched sham.
  - Code's default: compute the Fisher half under a common null rate equal to the absolute p0 (.20), with a grid of
    rates and the supremum beside.
  - The guard pauses if either half fires (m:316), so "the exclusion guard's false-pause figure" (m:285) is the
    probability that either half fires at some look. Code's default: that union, computed jointly over the contrast
    and sham counts under the common null rate (.20, with the grid and its supremum beside), with each half's own
    figure beside it.
- **(c) "the joint figure".**
  - In Q-F0 the only §6 bar with a p0 and a domain, the exclusion guard aside (its figure is "beside", m:330; (b)
    above), is `round_degeneracy`. The hair triggers carry no p0, and the lexical bar has no domain (m:330: "in Q-F0
    … lexical is reported only").
  - Code's default: the joint figure is that bar's own figure, with the guard's beside.
  - The other reading, a joint over the degeneracy bar and the guard, is not separable: a sham pre-pick exclusion can
    count in both, so it would need a model of their dependence.
- These are Code's readings, declared at G-PWR on the terms Q1 proposes for v1.0-declared readings (strikable until
  v1.0's commit), unless the seat says otherwise. A strike changes only G-PWR's figures, which are recomputed.
- Bears on: G-PWR's figures, not its run.

## Not questions

- **What v1.0 truncates** (the step-10 read's Q1: "Settled now, so it is not put again at step 15").
  - v1.0 truncates the analyzer's sha256 at §1 (:519) and §9.1 (:1554), and its header lists each truncation as the
    step-10 read's Q1 requires.
  - The superseded manifest's sha256 (:522, :1555) stays in full. The step-10 read's Q1 does not name it and no test
    reads it. v1.0's header marks it superseded, with its new path (Code's reading).
  - The closure. The step-10 read's Q1 names the closure among "the superseded full hashes" to truncate, and
    conditions only the package's truncation ("if it ever moves"). The closure did not move (`a3bc7bb9…b22b`; no
    import and no closure file changed). Code reads "superseded" as conditioning the closure too, so there is no
    superseded closure value for PIN-14 (the only lock-text check that reads it) to separate (lock §11 item 8's
    mechanism). Code keeps it in full at §1 (:521) and §10 (:1706); §9.1 (:1558) already truncates it. This is Code's
    reading against the ruling's letter. The seat may say otherwise, at the cost of v1.0's text only (v1.0 names the
    closure in full for PIN-14 either way).
  - Besides check (f) and PIN-14, only the driver self-test's "a lock-named non-proposal" case reads one of these
    hashes, the current analyzer's sha256 (`stage_identity_extra`), which v1.0 names in full; so no truncation breaks
    a test, and none is a new question under the step-10 read's Q1.
- **The decisions block.** v1.0 names its sha256 in full (`fab576d8…34f8`; m:286; the step-14 read §4 item 5) and
  quotes its :91 and :96 with §0.2's marks, as step 3 did (m:356). The file stays untracked unless the PI says
  otherwise (PI 3).
- **PIN-45's stated limits** (its text is verbatim in the review raw's header; carried here as that raw's "FOR THE
  SEAT, NOT BUILT" list says). PIN-45: "No V2 refusal catches any of the three":
  - every fired flag cleared, on a fresh end look or on a reused one together with the look it reuses. This cannot be
    told from a silent look without recomputing `campaign_look` from the session records, which are pick-bearing until
    V3;
  - a hair-trigger STOP at a reused look whose stop block is replaced by a terminal PI-STOP, its end pause given a
    ruling: it has the shape of the PI's stop of a paused look, which ids cannot tell apart;
  - a hair-trigger STOP relabelled G-VER with its (template, s) moved to an id not recorded (at a reused look, its pause
    given a ruling): it passes, since V2 checks a G-VER STOP's id only against the record; moved to its arm's next
    launch, it has the shape of a G-VER STOP there, which ids cannot tell apart. Q2's s-count candidate would narrow it
    to that id.
  They are declared in PIN-45, not built against. Without an answer, none is guarded, and v1.0 declares them as PIN-45
  states them. Q2 is the related question.
- **The window.** Lock §9.3: "every non-stub stage refuses at its start until a lock revision names the new one" (§9.6
  restates it with "then").
  - From `b046b16` until v1.0's commit, a non-stub stage refuses at the licence: at check (d) if the command line gives
    the lock's analyzer sha256, at check (f) if it gives the new one.
  - The driver self-test gives 795/796. Its `time` refusal check fails on one case, "a lock-named non-proposal":
    - with the licence stubbed there, the driver's own proposal-in-lock check (`stage_identity_extra`,
      `m_sessions.py:542–545`) now refuses before the banner check the case expects;
    - it gives 796/796 once a lock line names the new analyzer (the entry; the review raw's controls).
  - No licensed stage runs in the window. G-PWR is not a stages.py stage (Code's reading); R2 3 orders the v1.0 draft
    to name the new analyzer before it runs.
- **L2-9, an observation.** The `verdicts` branch reads `--adjudication`, `--pi-stop`, `--olmo-states`,
  `--sentences` and `--flag-source` by truthiness (and `--campaign`, `--time`, `--qual` and `--out` fall back to their
  defaults), so an empty string reads as absent.
  - Where a surplus file would be refused (an `--adjudication` beside an adjudicated last pause), an empty path is
    dropped silently instead.
  - A needed input that is empty is still refused (PIN-9, or the STOP branch). No verdict or written record changes
    (the round-2 refuter).
  - It predates this round, and Code did not change it: it is not one of the three edits.
- **The sentence table's classification** is Code's (PIN-20: "The table of record's classification is Code's,
  outcome-blind at LOCK v1.0, values-checked"). Its rules go in its build raw. If the table should need a
  `KINDS_VOCAB` or schema change, Q6's cost applies.
- **While the table waits** for the PI's word on PI 1, Code does not run G-PWR and computes none of its figures for
  Q-F0. G-PWR runs in the listed order only: after the table of record is built, after the v1.0 draft names this
  analyzer (R2 3) and the table, and, if the PI so holds it under PI 4, after the seat's answers. G-PWR's raw will
  record the v1.0 draft's sha256 at its start and quote the draft's line naming `522e8057…`.
  - Code's reading, put to the seat with Q6 (R1 A2): Code may prepare in scratch, uncommitted, G-PWR's computation,
    tested on synthetic inputs only. That is not a start of items 2 and 3, as the entry reads the read-only planning
    map under R1 A4. If the seat reads it otherwise, it is recorded as a departure.
  - That preparation reads no lock text, so the step-14 read's Q4 rule ("a build whose checks read a lock's committed
    text starts after that lock's commit") does not reach it; its review raw will say when it began.
- **The campaign wiring** (step 16) waits for v1.0, with the step-14 read's Q3 redaction and the campaign's
  `REVISION_STAGES` entry (the step-14 read §§3, 5 and "What Code does now" item 3).
