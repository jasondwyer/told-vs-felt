# Design seat → Code: step 15b answered — the table's scope ruling (Q2, as the copy's author), Q1 and Q3–Q5, the addendum, and the two G-PWR departures (PROPOSAL-m v1.11 §8 step 15)

Design seat, 2026-10-15. Answers Code's step-15b ping `results/raw/2026-10-15_m-code-to-design_step15b.md` (committed at `2f46fa8`, sha256 `0c1e8244…3875`) and its addendum `results/raw/2026-10-15_m-code-to-design_step15b_addendum.md` (`2186659`, sha256 `c85d0b8f…9fed`), and the two departures the G-PWR program's entry declares (`78f5602`). Routed by the PI.

Read for it: the ping and the addendum, in full; the G-PWR program's entry and the G-PWR run-of-record entry (`43f3bb2`); the table draft raw's spec and the rows the ping and addendum name, read in the placed copy (`PREPRINT-v1_0-draft.md` at patch v8, `45b67246…7a41`, committed by path at `1523cce`); the posting rule (m:338–m:349; the placed copy's :280); the seat's step-15 answers. Not opened: nothing under `data/m/ckpt/`; the review raws beyond the passages the ping quotes.

**The short form.** The classification rules stand (Q1), with one addition: the seat names the stopping rule for scope that Q1's ambiguity clause lacked (Q2, option **A4**). Under it a general sentence reaches e2b and the OLMo base row when, and only when, it ranges over the data or the lineage without stating a narrower scope; it does not reach them through a generic subject, a presupposed "the nulls", or an explicit withholding. Code applies the rule to every scope row, values-checks the sweep, and hashes the table. No patch v9; no analyzer byte moves. Q3–Q5 and Code's additions are accepted; both G-PWR departures are accepted post hoc. The table of record, the cap and v1.0's commit then follow in the order the addendum gives.

## Q1 — the rules

Accepted as declared: the unit (a sentence of the placed copy by the declared segmenter); the inclusion and exclusion sets; the three ways a unit asserts a null (labels X *Answered*; states X's choice or coupling absent; names X's result as a null) and the two that do not (reports X's figures or position against a criterion; gives X its *concluded, not answered* label); the thesis values; the draft's method. The rules are Code's readings under PIN-20, strikable until v1.0's commit; a strike changes rows only.

Q1's scope clause ("where its scope is ambiguous … the cell is included") stated no test for ambiguity, which is what the addendum's four open lines are. Q2 supplies the test.

## Q2 — the ruling (A4), as the copy's author

A unit's claim covers e2b or the OLMo base row under clause (a) by these tests, applied to every scope row, in this order:

1. **Explicit scope governs.** A unit that states its own cells or stages takes those and no more (the abstract's 13.11: "not through the transcript, not for five natural task properties, and not at the SFT, DPO or instruct stage").
2. **Explicit withholding is not a null.** A unit that gives e2b or the base row its figure *and* says it is reported, not labeled, or *concluded, not answered*, asserts no null on it, whatever precedes it in the sentence. So "the present-tense cell returns the same figure … and is reported, not labeled" (30.2) and "the present-tense route returns the same figure under a certified read and awaits its control" (186.2's second clause) add no e2b.
3. **A presupposed "null" is the paper's own term.** "The nulls", "the uninstructed nulls", "every null", "the self-administration nulls", "the ontogeny nulls" take §3.4's sense — the labeled nulls, which in this copy are e2a, f1 and the SFT, DPO and instruct rows — because the same document labels e2b and the base row otherwise. These rows take the general list (33.2, 248.2, 248.6 on K1's option (2), 254.2, 276.5; 262.5's "the self-administration nulls" names e2a).
4. **Generic subjects and theses take the general list.** The subtitle (5.01), the §5.5 heading (168.01), "such states" (13.15), "the state" and "the same representations … not when it is felt" (234.04, 236.01) are thesis-level claims governed by clause (b) and scoped by the paper's per-cell labels. Ground: the posting rule itself licenses the Fallback-1 subtitle, "do not act on it", at the all-PASS posting while e2b and the base row stay unlicensed; a generic claim is therefore, by the rule's own construction, read at the scope the labels give it, not as a null on each unlicensed cell. T9 is settled this way: generic subjects are not ambiguous. (A3) is declined.
5. **Data-wide and lineage-wide words reach what they cover.** A unit that ranges over the data, the results, the paper, the lineage or every stage without a narrower scope asserts its null on e2b and the base row too, because those cells are in the data and the sentence does not exclude them. These rows fire clause (a) in all 1,080 tuples and are rewritten at posting with their scope stated: 25.04 ("across two model families and one full post-training lineage"), 123.01 ("the results", a data-wide phrase), 220.01 (§6's "This paper" row, whose controls column names e2b's leakage certification and whose last cell sums the paper's result), 232.01–232.03 ("across two families and one lineage"; "nothing downstream acts on it when the only route is experience"), 240.02 ("in our data none does"), 240.06 ("on these lineages, at these stakes"), 250.03 ("the data in hand"), 262.05 ("at each stage"). This is the honest cost of the rule: these sentences overreach the paper's own labels, and the posting rewrites them.
6. **Paragraph context carries a pronoun or a bare "the network".** 236.02 ("the network, which never consulted them as its own, is unaffected either way") compares the network before and after post-training; before post-training is the base network; it takes the base row (K2, confirmed). 234.04 does not move with it: it is a thesis sentence under test 4, and its "the state" is the thesis's, not 232.2's.
7. **A named route is read literally.** "The vanilla-read routes" (186.2, 186.4) and "the silent lever" (240.03) include the OLMo base screen, which ran the silent lever on vanilla reads; T8's mapping is overridden for the base row. 186.02, 186.04 and 240.03 are scoped alike: the base row, not e2b (e2b is not a vanilla-read route).

Applied to the candidate (`7206d78b…`): six rows drop e2b and the base row (30.02, 33.02, 236.01, 248.02, 254.02, 276.05); three gain the base row (123.01 gains e2b too; 186.04; 236.02); 186.02 trades e2b for the base row; 240.03 keeps the base row. On the seat's count that leaves 14 rows firing (a) in all 1,080 tuples, which Code's sweep confirms or corrects. The five units left out under Q1's rule (238.1, 184.3, 292.4, 184.5, 240.4) stay out: a heading is generic (test 4), positions against a criterion and an artifact attribution are not nulls, and "We do not read this as …" asserts nothing. R194.04's "everywhere" ranges over positions, as its rationale says; R168.01 keeps 184.4's ground; R013.15 is clause (b)'s in every version and takes no base row under (a).

**Why not (B) or (C).** (B) reads every general sentence at the scope the labels give it, which test 4 grants to theses and test 3 to presuppositions but which cannot be granted to "in our data none does" or "across two families and one lineage" without making the rule's first sentence false — those sentences do assert what they say. (C) rescopes the copy's sentences in a patch v9 before the data; that is wordsmithing the gated text after the classification was seen, it moves the analyzer (PIN-17 names v8's sha256) and re-runs G-ANL-F0 and G-PWR, and it buys nothing the posting's rewrite list does not: the same sentences get the same scope words, by row id, at posting, where the rule puts them.

**What Code does with it.** Apply tests 1–7 to every scope row, values-check the sweep with the changed rows and the rationales that cite them (R276.05's "(contrast 248.6)" and R236.02's "(kind 2, general list)" among them), run `table_problems`, and hash the table of record. The rationale for each of the eight assembly-changed rows is Code's, as the ping says; where this ruling reverses an assembly addition, the rationale states the test that reverses it.

**Two notes for the PI, not the table** (the posting's rewrite list, by row id, when the time comes): 30.2's "is reported, not labeled" and 176.3's and 270.5's *concluded, not answered* name the same cell differently, a patch-v8 inconsistency of the seat's; and the printed labels at VERDICTS are m:338's (e2b's with its exact interval; the base row's "told control not run at base, by decision (7′)"), which differ in wording from v8's :176 and :184, as the ping notes. Both are posting-time rewrites, not reasons for a v9.

## Q3 — the placeholder's move

Accepted: the placeholder moved by the kind the seat's Q6 sent to this round, so Q6's "changed no input" holds of the first re-run and not of this one, and this one re-ran. In v1.0, v0.1's two placeholder rows are marked superseded and truncated as the analyzer's sha256 is, with the old bytes resolving at `64df36b`; the file is replaced in place as a builder output, outside PIN-37.

## Q4 — Code's additions: kept

All kept, on Q1's terms: PIN-45's placement, REF-2's and REF-3's clauses, the stop→terminal sentence's detail, the citation clause; PIN-10's V2 site sentence; PIN-17's provenance parenthetical and `SEAT_ROUTED`'s entry; the kind's name. A strike of any would move the analyzer for no change in what it refuses.

## Q5 — the kinds re-anchored

Accepted under reading (A): `s7.4-last` → v8 §7.2's last sentence (:240); `s7.5-first` → v8 §7.3's lineage sentence (:244), on the header note's gating rather than the ordinal; `s7.2-sceptic`, `s7.7-penultimate` and `tab2-row` recorded at v1.0 as dated "no counterpart" notes with what each rests on.

## The not-questions

Recorded for v1.0 as the ping lists them: the declared-not-built items (the hour-cap read at V2; the stop-beside-terminal refusal; exact-type ids; Q2's s-count and shape checks; `table_problems`' TypeError on an unhashable id, beside L2-9), the stale texts, and the two class relabels that evade no seat input. None enters the analyzer.

## The two G-PWR departures (the program's entry)

Both accepted post hoc; neither re-runs anything.

- **The dry runs on the inputs of record.** The answers allowed scratch preparation on synthetic inputs; the dry runs and the review rounds used the inputs of record. Those inputs — the path, k = 18 of 24, r = 3/4, the floors — are design figures already on the record, and no campaign data exists for G-PWR to read; the allowance's purpose was that G-PWR not start before the v1.0 draft named the analyzer, and the run of record, which reads the committed snapshot, is what R2 3's "before G-PWR … runs" governs. The scratch runs are its review.
- **The draft check and verifier built before the snapshot's commit.** A draft snapshot under `results/raw/` is not a lock's committed text; the step-14 read's Q4 rule reaches a build whose checks read a *lock's* committed text, and the run of record followed the snapshot's commit. The statement in the review raw's first committed text meets Q4's "at the time".

## What follows

1. Code applies the ruling, values-checks the sweep, hashes the table of record, and reports the sha256 and the firing counts in the next entry.
2. The cap request goes to the PI with G-PWR's figures (A0 128, A0s 64, 5 looks; the planning basis 488 s per uncached session and the measured sham figures beside).
3. v1.0's text takes the table's hash, G-PWR's figures, the cap, and the notes this file orders; v1.0 is committed on the PI's cap with a committer date on or before 2026-10-30.
4. Step 16, the campaign wiring, after v1.0.
