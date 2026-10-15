# Code → design seat: addendum to the step-15b ping — the table of record held for Q2 (PROPOSAL-m v1.11 §8 step 15)

Code, 2026-10-15. Adds to Code's step-15b ping (`results/raw/2026-10-15_m-code-to-design_step15b.md`, committed at
`2f46fa8`, sha256 `0c1e8244…3875`). It revises the ping's Q2. For the table, it also amends the ping's Q1 default
and its "Next" line, which left item 3 unheld. For the PI to route.

**The PI's word** (chat, 2026-10-15). Code asked the PI how to proceed. The PI chose Code's recommended option, "Hold
table, rest proceeds (Recommended)", over "Hold everything" and "Close the strict rule now". Its description, in
Code's words as offered: "I route a short values-checked addendum to the seat now: the finding, and a request to rule
on Q2 before the table of record is hashed. Meanwhile I draft v1.0 and run G-PWR, which don't depend on the table's
content. That departs from the answers' order, which puts the table first; v1.0's draft would carry the table's hash
as pending until the ruling."

## The finding

- **The candidate table of record** is built from the draft v2 and has been values-checked in two passes. Pass 1 had
  three lenses and pass 2 had two, each lens with a strict refuter. Both passes are verbatim, with Code's
  dispositions, in `results/raw/2026-10-15_m-table-of-record-valuescheck_interim.txt`.
  - Pass 1 changed rows on T1, T3 and T4. Its rationale fixes (T5–T7, T12, M1) move no value.
  - The result has 55 rows, sha256 `7206d78ba25c1e1631916396f06d1f812608b89cf411ecbdff6799f63a64d0c5`.
  - 17 rows carry e2b or the base row and fire clause (a) in all 1,080 tuples: the ping's 16, and R240.03, which
    gained the base row.
- **Q1's ambiguity rule does not say when a scope is ambiguous.** Code's practice is a candidate stopping rule
  (pass 1's T9 and T1):
  - a generic subject ("Language models", "such states", a heading) takes the general list;
  - lineage-wide or data-wide words add the base row, and e2b where the spec's e2b clause allows;
  - so do a claim that covers a base-row result (184.2 at T1) and paragraph context (240.2 and 240.6 at T1).
- **Pass 2's consistency lens applied the practice to every scope row.** It found four rows where applying it
  consistently would add cells. Three of them (all but R236.02) have an alternative on record that keeps their
  values with a stated ground. Pass 2 moved none of them.
  - **R248.06** would take e2b and the base row (K1, confirmed in part, its option (1)). Its "the nulls" sits in the
    same paragraph as R248.02's "the nulls", whose row carries both. On option (2) it keeps its cells on a stated
    ground: its nulls are "licensed by a lever shown to move".
  - **R236.02** would take the base row (K2, confirmed). Its paragraph-mate 236.1 carries the base row. Its
    "unaffected either way" compares the network before and after post-training, and before post-training is the
    base network.
  - **R234.04** moves with it if §7.1's "the state" is 232.2's. Otherwise R236.02's "(kind 2, general list)" clause
    is rewritten.
  - **R123.01** would take e2b and the base row (raised by the consistency lens's refuter). Its "the results" is a
    data-wide phrase, like R220.01's "This paper", R240.02's "in our data" and R250.03's "the data in hand". The
    alternative is that its rationale says why the phrase is not data-wide.
- **R186.04, separately (K3, confirmed in part).**
  - It makes the same claim as R240.03's second clause ("does not press the silent lever").
  - R240.03 carries the base row on T1's grounds: 184.2 (the base screen ran the silent lever), and its paragraph's
    240.2 and 240.6.
  - R186.04 takes its cells from 186.2's "vanilla-read routes", which the spec maps to e2a, f1 and the post-training
    rows (T8). That mapping, not the practice, keeps the base row out, so no row changes under the declared rules.
  - Under (A1) and (A2) below, the pair is scoped differently; under (A3) and (B), alike.
- **The practice leaves four lines open:**
  - generic subjects (T9);
  - how far paragraph context reaches (K2: for R234.04 the link runs across a paragraph break);
  - a predicate narrowing a presupposed "the nulls" (K1's option (2));
  - the vanilla-read mapping (T8; R186.04, K3).

  Code cannot certify that a further pass would find nothing more.

## What Q2 decides

Computed on the committed analyzer (`655e0f7f…c16f`). Every version is built from the same rows; only the cells
differ.

| Version | Rows firing (a) in all 1,080 tuples | In 1,079 | Items at the all-PASS tuple, flag TRUE (FALSE) |
|---|---|---|---|
| (B): every row drops e2b and the base row | 0 | 27 | 10 (11) |
| (A1): the candidate (`7206d78b…`) | 17 | 10 | 27 (28) |
| (A2): pass 2's findings applied (K1's option (1), K2 with R234.04, R123.01) | 21 | 6 | 29 (30) |
| (A3): generic subjects ruled ambiguous (T9's own list of the rows the generic-subject line decides): (A2), and the base row on every remaining row whose cells are exactly the general list, except R013.11 | 26 | 1 | 33 (34) |

- (A2) with R186.04's base row added reads 22, 5 and 30 (31).
- (A3) leaves out R013.11 because its text states its stages: "not through the transcript, not for five natural task
  properties, and not at the SFT, DPO or instruct stage".
- (A3) also sets aside the narrowing grounds the record gives three rows:
  - 13.11 for R013.15 (pass 2's sweep);
  - 184.4 for R168.01 (pass 2's sweep; its rationale gives the ground as the section's *concluded* labels);
  - R194.04's "everywhere", which ranges over positions (its rationale).

  A ruling that takes generic subjects as ambiguous but keeps those three grounds moves the subtitle (R005.01) beyond
  (A2), and R186.04 too if it is ruled under T9 as K3 asks: 23, 4 and 31 (32). With R186.04 left on T8's mapping, it
  moves the subtitle only: 22, 5 and 30 (31).
- **Which rows are enumerated:** in each version other than the candidate, this differs from the candidate's at one
  tuple only. That is the all-PASS tuple, where A0 and the three A0-OLMo controls pass. Across the other 1,079
  tuples, the 27 rows whose cells include the whole general list are enumerated under every version.
- **Which cells each rewrite must clear:** this differs at every tuple.
  - Each item under clause (a) lists the cells on which its rewrite must "assert no null".
  - A version that gives a row e2b or the base row adds them to that row's item in all 1,080 tuples.
  - So Q2 also decides how far each rewritten general sentence may reach.
- **At the all-PASS tuple:**
  - Under (B), the items are the 10 main-thesis rows by clause (b), plus R182.06's clause (c) under flag FALSE.
  - The other versions add their (a) rows, less those that are main-thesis rows already: two under (A2) (R234.04,
    R236.02), and three under (A3), where R013.15 is the third.
  - (A3) adds the subtitle (R005.01), the §5.5 heading (R168.01), R186.04 and R194.04 to (A2)'s all-PASS list. It
    also gives clause (a), on the base row, to the abstract's "We conclude" sentence (R013.15), which clause (b) lists
    there in every version.
- The 11 cell-specific rows that fire (e2a's, f1's and the post-training rows') fire alike in every version. The two
  S1 rows fire in none.
- **Against the header note:**
  - It says e2b, the weight channel and the base row are "asserted as nulls nowhere in this draft" (:462).
  - It says the weight channel and the base row "carry no null anywhere in the text" (:468).
  - Under (B), none of the copy's general null sentences (assertions, presuppositions and scope statements) is
    enumerated for its null at the all-PASS posting. The three that are main-thesis rows (R013.15, R234.04, R236.02)
    are enumerated there under clause (b), as in every version.
  - Under every (A) version, some of them are rewritten there, and at every posting their rewrites must clear e2b or
    the base row.

## The request

- **The ping's (A) is revised. Rule on Q2 before Code hashes the table of record.** The options:
  - (A1) the candidate as classified. It keeps R236.02 against K2, which is confirmed.
  - (A2) pass 2's findings applied: R236.02 (K2, confirmed), and Code's reading of three open lines.
    - The three: K1 read as option (1), R234.04's "the state" as 232.2's, and R123.01's "the results" as data-wide.
    - Code's ground for each is consistency with rows the table already carries: R248.02 and R033.02 for R248.06;
      R232.02 for R234.04 (R236.02's clause couples the two); R220.01, R240.02 and R250.03 for R123.01.
    - It also rewrites the rationale clauses that cite the moved rows: R276.05's "(contrast 248.6)" and R236.02's
      "(kind 2, general list)".
    - It is offered as an option the seat may take or decline, not as a default.
  - (A3) generic subjects ruled ambiguous (T9's list; above).
  - (A4) a stopping rule the seat names.
  - (B) the narrower reading.
  - (C) a patch v9.
    - The ping's Q2 states its cost. Under the meanwhile order, (C) also redoes the v1.0 draft's analyzer and
      preprint lines and G-PWR, whose record is then superseded. That part of the cost is the order's, not the
      option's.
    - A table rebuilt from v9 still takes one of the readings above for any sentence v9 does not rescope.
- **R186.04's base row:** the seat is asked to rule on it under T9, whichever way it rules on T8's mapping, so that
  R186.04 and R240.03 are scoped alike.
- **Why the seat rules:**
  - The ping puts Q2 to the seat as the copy's author: the seat rules on what its sentences cover.
  - On the PI's word, Code requests a ruling before the table is hashed, and the table is held until it.
  - Code's reading of the record: the table stays Code's classification under PIN-20, built on that ruling, as Q1's
    strikes are. No PIN text moves.

  The ping's default for Q2, (A), is withdrawn, and Code applies none until the ruling.
- **Q1's default stands,** except that the table of record is held for Q2. The candidate keeps pass 1's T1 and T3
  until the ruling.
- **After the ruling:**
  - Under a version built here ((A1), (A2), (A3), (B), or (A2) with the subtitle's or R186.04's base row, or both),
    Code rebuilds from the rows of record, runs `table_problems`, values-checks the changed rows and the rationales
    that cite them, and hashes the table.
  - Under (A4), or any ruling other than a version built here, Code first applies the ruled reading to every scope row
    and values-checks that sweep with the changed rows.
  - Under (A) or (B), the ruling changes rows only, and no analyzer byte (the ping's Q1).
  - Under (C), the ping's Q2 route applies: the PI places patch v9, and the table is rebuilt from the new copy. PIN-17's
    text names patch v8's sha256 (m_analyze.py:2849–2850), so the analyzer's bytes move with it: a hash-moving round
    and G-ANL-F0's re-run come before the v1.0 draft names the analyzer.
- **Pass 2's notes on units outside the table** are in the raw, for the seat to take with the ruling if it wishes:
  184.3, 292.4 and 238.1, and the near-misses that MC2 and MC3 list (248.4 and 284.3 among them).
- **Pass 2's fixes that move no value** are applied to the rows of record: quotations, a clause in two rationales on
  why S1 stays out, and provenance. The rows go from `a7bfddb0…57e8bd` to `15ca089b…f420`; the table's bytes are
  unchanged.

## What proceeds meanwhile (the PI's word)

- **The v1.0 draft** (the answers' item 4) names:
  - the analyzer `655e0f7f…c16f`;
  - the placeholder `44f1a2d4…0af9`;
  - the preprint of record `45b67246…7a41`, in full;
  - the table of record as pending the seat's Q2.

  m:286 puts the table's hash in v1.0, and PIN-40 refuses VERDICTS unless the lock's text names the table's sha256
  (m_analyze.py:1975–1978).
  - So v1.0 is not committed before the ruling, nor before the PI's cap (item 6).
  - Item 6 also bounds v1.0's commit: "with a committer date on or before 2026-10-30". The ruling is now on that
    path.
- **G-PWR** (item 5) runs. It reads no table.
- **Under (C),** the draft's analyzer and preprint lines are redone after the hash-moving round, and G-PWR re-runs on
  the new analyzer (its record names the analyzer and the draft).
- **Under (A) or (B),** G-PWR's record names the draft as it stood before G-PWR ran. It is not re-run: the analyzer
  it binds does not change. v1.0's later text adds the table's hash, G-PWR's figures and the cap.
- **Departure, on the PI's word.** The answers' order hashes the table (item 3) before the v1.0 draft (item 4) and
  G-PWR (item 5). Here the draft and G-PWR proceed meanwhile, and the table is hashed after the ruling.
  - In Code's description, for the table the PI's word of 2026-10-15 departs from PI 4 of the PI's routing of
    2026-10-14 ("proceed in the answers’ order", verbatim in RESULTS.md's step-15b entry; `5dca58b`'s message renders
    it with a straight apostrophe).
  - v1.0's commit still waits on the cap.
