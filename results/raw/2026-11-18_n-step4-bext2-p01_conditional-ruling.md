# Conditional ruling on the end-of-run fidelity pause of stage `backend-ext-2` (the BACKEND extension's 24 reads under the label convention of record, "space"; n's box, pod `emw1e4embiwe9b`): cleared as the measurement if four conditions hold

*Design seat, PI date 2026-11-18 (fourth sitting). A ruling raw given before the stage runs, for `backend-ext-2 --resume --ruling <pause id>=<this file>`, under ADDENDUM-n2 v0.1 §4.1 ("its end-of-run pause, if it fires, is adjudicated by the seat on the same ground as `p01`'s ruling unless the figures show otherwise") and the seat's answers of this sitting, §2.2. Committed by path with those answers before the stage runs; if it is used, its sha256 is the pause's `ruling_sha256`. Rule 21: the seat adjudicates; Code checks the conditions mechanically, prints each with the resume's line, and weighs nothing. Calendar dates only; the commit hash is the record.*

## The ruling

1. **Scope.** This ruling applies to exactly one pause: the first pause of stage `backend-ext-2` run under the "space" convention from driver v2f's commit or a later driver whose read path is unchanged, and only if that pause's kind is `fidelity-binomial`, fired at the run's end (`launch_index` null), the stage having launched and obtained all 24 planned reads.
2. **Conditions,** each checked by Code from the stage report and the run's output before the resume, and each printed with the resume as "condition (i): holds" or "fails":
   - (i) every one of the 24 records is finite (the report's non-finite count 0);
   - (ii) no read's |cached margin − fresh margin| exceeds 0.25 nats (ADDENDUM-n2 §2.1's floor for C), read from the fidelity values the records carry (the stage's distribution line prints the maximum);
   - (iii) no other pause stands on the stage;
   - (iv) the report's identity lines at the resume equal the run's, as the resume of `backend-ext` checked them (the hashes step against the report's identity).
3. **If every condition holds, the pause is cleared as the measurement,** on the ground of `p01`'s ruling for the first stage (`results/raw/2026-11-18_n-step4-p01_ruling.md`, sha256 `e2b1c77a3026dd40be659168397826cd60397f514b243cb6279234058d2e2a8a`): the 24 reads are the box's measurement under the convention of record, their count above TAU being the k that ADDENDUM-n2 §1.1 takes for p0, and the batch of 24 trials is cleared. No read is excluded, no record changes, the resume completes skip-only and prints the distribution and the two aggregate lines of the fourth sitting's §2.3.
4. **If any condition fails, this ruling does not apply:** the pause waits for the seat with the stage's output and report, nothing resumed.
5. **If no pause fires,** the stage completes on its own and this file is not used; it is committed with the stage's entry as the record of what would have applied.
