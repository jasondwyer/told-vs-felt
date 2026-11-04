# Design → Code — moving tag `note-2026-10-v2` before the flip (note arc; 2026-11-03, routed by the PI)

*Design seat. Amends one line of `results/raw/2026-10-28_note-design-to-code_release-block-answers.md` §8 ("The tag commit is the last audit commit, which is the second N18.") and the tail of its §10 item 5. Changes no pre-registration, label or figure. Calendar dates only. Committed by path on `main` at the PI's direction. No RESULTS entry.*

## 0. Why

- At `fee3706` (the second N18; the tag commit of `note-2026-10-v2`, pushed), `README.md:3` reads "a LessWrong copy is under that site's review." The PI deletes the original LessWrong post on 2026-11-04 (replaced by a shorter post written entirely by him), so that clause is false in the tagged tree from the flip onward, on the page every reader following the note's link lands on. The 11-03 handoff flagged the line before "tag"; the edit did not route in time. Whether that goes in the ledger is the PI's call; if it does, it is a design-seat routing slip.
- **The PI's decision (2026-11-03, in chat): move the tag forward to a descendant on `main` before the flip.** No commit is rewritten; `fee3706`, `23ec9b1` and `881bd61` stay in history as the record of the first tag; the tag has never been public.

## 1. Order (replaces the sequence in 10-28 §8 and the tail of §10 item 5)

1. **README.md path commit** (the PI's edit, or Code's by path on his word): delete the clause `; a LessWrong copy is under that site's review` from line 3, so the parenthetical reads `(posted at https://jasondwyer.github.io/2026-10-27-told-vs-felt-porting-behavioral-pharmacology/)`. No other line changes; the canonical-copy paragraph at line 5 stays. If `README-NOTE.md` or any other tracked file names the tag *commit* hash (`fee3706`) rather than the tag name, re-point it in the same commit; the tag name does not change.
2. **N18, third run**, the manifest regenerated in place as the last audit commit (N18 hashes README.md, so it follows item 1). Ruling amended: *the tag commit is the last audit commit, which is the third N18.*
3. **Move the tag.** Local: `git tag -d note-2026-10-v2`, then re-tag (annotated, same name, same message convention, plus one line: moved from `fee3706` on 2026-11-04, README.md:3) on the third N18. Remote: delete first, then push — `git push origin :refs/tags/note-2026-10-v2`, then `git push origin note-2026-10-v2`. If Code's session is refused on the delete (as the seat's was on the five branches and the teleport ref), the PI runs the delete from the laptop checkout and tells Code.
4. **The re-runs at the new tag commit, as at `23ec9b1`:** the five N12 re-runs (history, content screen, licenses, gitleaks, password — the PI supplies the word at scan time; it is never written down), N11 at the tag, and the tag record. The tag record carries a dated line: the tag moved from `fee3706` to the third N18 on 2026-11-04, before publication, because of README.md:3; the raws of `23ec9b1` and `881bd61` are the first tag's record and stand. Raws committed after the tag, by path.
5. **The pre-flip read** (`scripts/audit_note_N12_preflip.py`, unchanged) at the new tag, its raw committed after the tag: `ls-remote` = `main` + the four tags, each equal to the local ref; the surfaces at zero as before.
6. **Fresh-clone 154/154 at the new tag** (the count README.md states; run it at the new tag even if it ran at `fee3706`). Then "ready to flip."

## 2. What does not change

v0.8 at the root (sha256 `6fcfbfd6…1198d`); `audit_note_N18.py` on v0.8; Tier 1 on patch v7 at `note-2026-10-v1`; the three earlier tags; the 2026-10-28 (i)-line answer, whose condition (0 true-secret candidates, 0 untriaged on the re-run) holds again at the new tag or is a fresh STOP; `.gitignore`. After the flip, on `main` only: `CITATION.cff` with the Zenodo DOI; optionally a README-NOTE line pointing at the blog's dated correction block.
