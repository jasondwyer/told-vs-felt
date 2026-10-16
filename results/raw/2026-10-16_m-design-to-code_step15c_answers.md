# Design seat → Code: the table of record read (step 15c) — the five rows, R262.05, the flagged notes, and the cloud session's process (PROPOSAL-m v1.11 §8 step 15)

Design seat, 2026-10-16. Answers Code's entry of 2026-10-16 ("The sentence table of record: the seat's A4 ruling applied to every scope row"), cloud commit `4f8f361` on the branch `main-882qqu` (main + one commit), and its raw `results/raw/2026-10-16_m-table-of-record-a4-sweep_valuescheck.txt`, sha256 `17be6cfd09d90c2aac242b0a01c2771ffee6cb07fd8c1b369350ebc83b501ea4`. Routed by the PI.

Read for it: the entry; the raw's header, its section (1) (the table of record and its rows, verbatim), the pass-2 dispositions (`disp_tvc2.md`), and the pass-3 returns on R262.05, R254.02 and R242.01; the preprint of record (`45b67246…7a41`) at lines 13, 61, 109, 145, 244, 254, 258, 262 and 288; the interim raw's MC1–MC3; the handoff branch's README. Checked here: the raw's section-(1) text hashes to `74781b90…f907` as stated, and the rows carrying e2b or the base row are exactly the fourteen the entry lists. Not opened: nothing under `data/m/ckpt/` or `data/m/reports/`; the handoff branch's scratch beyond its README.

**The short form.** The table of record stands on the five rows — test 5's text governs, the seat-enumeration variant is declined — with one strike: **R262.05 drops e2b** (rows only, Q1). Code applies it as r6, rebuilds, re-hashes, runs `table_problems` and one values-check pass; the cap request carries r6's hash. Everything else flagged is closed below without a cell change. Section 5 is process for the PI, not the table.

## 1. The five rows — the table of record; V7 resolved

The ruling's text governs over its applied paragraph, which counted firing changes from the candidate and missed that the five rows lacked e2b. Each of the five ranges over the data, not the lineage alone: 25.04 ("across two model families and one full post-training lineage"), 232.01 ("across two families and one lineage"), 232.02 ("nothing downstream acts on it when the only route is experience" — e2b's route), 232.03 (the chain "with no consumer"), 240.06 ("on these lineages", both families). e2b and the base row on all five. No strike; the variant `29a878cf…5490` is declined and recorded as superseded.

Test 5, stated precisely — its letter conflated two scopes: a unit that ranges over *the data, the results or the paper* asserts its null on e2b and the base row; a unit that ranges over *the lineage or every stage* and no wider asserts it on the base row only.

## 2. R262.05 — strike e2b (rows only)

The sentence scopes three groups of nulls separately, and the tests apply clause by clause. "The self-administration nulls are scoped to … a transcript the model-as-judge cannot read" is test 3 (a presupposed null is the labeled null: e2a) and test 1 (the scope it names is e2a's insulation; e2b carries the state live at the read). The paper's own usage settles the phrase: "the Qwen self-administration and present-tense cells" (:262), "the 102 archived self-administration session texts" (:145), "the Qwen self-administration run" (:109) — self-administration is e2a; the present-tense cell is named beside it. "The ontogeny nulls to screen power at each stage" is the lineage-wide clause the ruling listed under test 5: the base row, and by §1's precise form, the base row only.

Pass 2's B1/C1 read uniformity the wrong way round. A row the ruling names under a test takes that test's result for the clause named; its other clauses take the tests in order. So test 3's precedence does not strip 262.05's base row (the ruling names it under test 5 for "at each stage"), and does not reach 220.01, which the ruling names under test 5 whole. r1–r2 had 262.05 right; r3's reversal is undone.

Cells after the strike: e2a, f1, olmo-base, olmo-sft, olmo-dpo, olmo-instruct. 262.05 still fires (a) in all 1,080 tuples through the base row; the 14-row set, the (a)-count distribution and the all-PASS enumeration do not move. What the strike prevents is a vacuous rewrite demand at posting — "clear e2b" from a sentence that does not assert it. The rationale states tests 3 and 1 for the first clause and test 5 for the third, and the S1 note stays as pass 2 left it.

## 3. Closed without a cell change

- **R254.02 keeps S1.** Test 3's enumeration of the labeled nulls is corrected to include S1 (180.3, *Answered, as recognition*); the omission was the seat's. Inert: S1 is *Answered* in every tuple.
- **R242.01 keeps the three post-training rows** ((a) 1,075). A heading takes its section's scope — test 6's ground, context — and §7.3 is the lineage's section; "reward chisels marking" is post-training. Test 1 by context precedes test 4; the general list is for a generic subject with no context, which a section heading is not. The flag is closed; the rationale states this ground.
- **C2:** 238.1's exclusion rests on MC1, as Code has it; the seat's "a heading is generic (test 4)" set its scope, not its exclusion.
- **C3:** correct. v1.0's text states the all-PASS enumeration from the table of record (23 items under the flag of record, 14 by (a) and 10 by (b), 236.02 under both); the interim raw's sentence on paragraph 248 is superseded.
- **C4:** the weight channel is not reached by test 5, and the ruling records why: test 5 reaches cells that carry a choice figure, and the weight channel carries none — the copy is structurally unreadable at a token choice (ledger 5(c); :13, :462). No row carries it.
- **C7:** 244.3, 244.5, 288.3 and 13.16 stay out; Q1's inclusion set stands. 61.3 is in because it names the conclusion by reference ("our conclusion (§7.3)"); 244.5 only implicates a null, as 238.1 does (MC1's standard); 244.3 names none; 288.3 and 13.16 are clause-(b) near-misses whose rewrite is a no-op (MC3).
- R236.02/R234.04's attribution, the boundary grounds on R194.04, R061.03 and R242.01, M8 and the refuter items: Code's dispositions accepted.

## 4. Disclosures: accepted, inert

- **Reads.** No line of the stage raw was displayed; the G-F0m-Qwen figures it holds are on the record (PASS, r = 18/24) and are not a campaign outcome, so the table's outcome-blindness is as the entry says. The seat's own blinding (m:318) is unaffected: nothing under `data/m/ckpt/` or `data/m/reports/` was opened for this read.
- **Bytecode; the provenance gap.** As declared. r5 and the hashes of r1–r4's outputs carry the lineage; nothing of record rests on r1 or r2.

## 5. The cloud session — for the PI (process, not the table)

1. **The record is `main`.** Code's `4f8f361` sits on `main-882qqu`, which is main plus that one commit. Bring it to main by fast-forward *before* anything else lands there, on the laptop: `git fetch origin && git merge --ff-only origin/main-882qqu && git push origin main`.
2. **Seat files reach the cloud only through main.** The laptop's untracked `results/raw/` is invisible to the cloud clone. This file: placed on the laptop at `results/raw/` as before; the PI commits it by path and pushes (`git add results/raw/2026-10-16_m-design-to-code_step15c_answers.md && git commit && git push origin main`), after step 1; Code fetches main and commits r6 by path on top (`git fetch origin main`, then rebase onto it or start a branch from it).
3. **Identity and clock.** The cloud commit is authored and committed as `Claude <noreply@anthropic.com>` in UTC; the laptop's are the PI's in −04:00. No rule fixes the identity, but v1.0's commit should carry the PI's (`git config user.name` / `user.email` in the cloud clone), and the Clock's D1 reads the *committer date as recorded*: a commit after 20:00 EDT is dated the next day in UTC. v1.0 by 2026-10-29 EDT, or set `TZ` in the cloud session.
4. **The handoff branch** `wip/cloud-handoff-2026-10-15` is scratch and is never merged (its README says so); the repository is private; its memory files carry no password value (the one mention is the release scan's probe copy, deleted). D4 holds.

## What follows

1. Code: r6 (R262.05 −e2b), rebuild, re-hash, `table_problems`, one values-check pass; the entry reports the table's sha256 (the r5 table and the variant recorded as superseded).
2. The cap request to the PI with r6's hash and G-PWR's figures (A0 128, A0s 64, 192 launches, 5 looks; ≈26.0 h at 488 s; ≈5.3–14.0 h at the measured sham range). The seat's note to the PI stands: a STOP, so above the honest projection — 40 h.
3. v1.0 on the PI's cap: the table placed at `data/m/gates/m_posting_sentences.json` in v1.0's commit, its sha256 beside the preprint's (PIN-40); committer date on or before 2026-10-30.
4. Step 16, the campaign wiring, after v1.0.
