# AUDIT-note-release v1.2 -- the moved tag note-2026-10-v2: a fresh clone of the server's repository, 154/154

- The design seat's tag-move block, item 6 (`results/raw/2026-11-03_note-design-to-code_tag-move.md@4358425`:17): "**Fresh-clone 154/154 at the new tag** (the count README.md states; run it at the new tag even if it ran at `fee3706`). Then "ready to flip.""
- Code's run, after the pre-flip read (`results/raw/2026-11-04_note-N12-preflip.md`): a fresh clone of the server's repository, `https://github.com/jasondwyer/told-vs-felt.git` (private at this run, so cloned with the laptop's own git credentials, which N11's isolated git, with its global and system config nulled, does not use), detached at the tag, then the suite README.md names (`python -m valence_core.regression.analysis`, README.md:70; "Model-free; must print **154/154**", :73). N11 at the tag (`results/raw/2026-11-04_note-N11-smoke-tag.txt`, 154/154) cloned the local repository; this run reads what the server serves.
- Expected: the clone's HEAD and the tag's commit equal `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5` (the tag commit, `results/raw/2026-11-04_note-release-tag.md`), the tag object `e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07`, and the suite's summary line '154/154 reproduced through valence_core'.

## The run

- Code stamp: Thu Nov  5 01:42:39 UTC 2026 (date -u)
- $ git clone https://github.com/jasondwyer/told-vs-felt.git <scratch>/clone
  exit: 0
- $ git -C <scratch>/clone checkout --detach note-2026-10-v2
  exit: 0
- clone HEAD: 6d8c237bfc6d85fc340917aa1a1c2daa136ddce5; the tag in the clone: object e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07, commit 6d8c237bfc6d85fc340917aa1a1c2daa136ddce5
- clone status --porcelain (empty expected): []
- $ cd <scratch>/clone && /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python -B -m valence_core.regression.analysis
  exit: 0
- suite output: 159 lines; its last 6:
      [PASS] e2d (v): balanced form differs at e2a's actual imbalance     expected differs by ~0.0135 got +0.0135 at 53/49   (AMENDMENT 2 (v), exact-balance caveat)
      [PASS] e2d (iii): read-marks refuse an unknown content class        expected 4 classes, refuses a 5th got 4 classes, refused True   (AMENDMENT 2 (iii))
      [PASS] e2d (i): g1 gate reads as first-token-only                   expected not a T-step licence got T-step=False   (AMENDMENT 2 (i) conditional)
      [PASS] e2d: resume reproduces the run and refuses a different one   expected identical transcripts + refusal got identical True, reads True, refused True   (incident 2026-09-02 (D2 died at 9/64 with nothing on disk))
    ------------------------------------------------------------------------------
      154/154 reproduced through valence_core

**Outcome:** PASS -- the server's repository, cloned fresh, holds the tag `note-2026-10-v2` as object `e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07` on `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5`, the tag commit, and the suite prints 154/154 there.

## The pre-flip read's section 2 FLAG, and the PI's ruling

The pre-flip read (`results/raw/2026-11-04_note-N12-preflip.md`, run before this clone) passes its parts 1, 3 and 4 and prints for part 2: "FLAG -- activity record: force push 0, branch deletion 2, records on other refs 0, read exit 0." Its rule takes any branch deletion in the repository's activity record as a flag. The two records (`gh api repos/jasondwyer/told-vs-felt/activity`, read by Code after the pre-flip read; type, ref, time, the object before and after, abbreviated) are both deletions of the tag's ref, the tag move's "delete first" steps (`results/raw/2026-11-03_note-design-to-code_tag-move.md@4358425`:14):

- `branch_deletion` `refs/tags/note-2026-10-v2`, 2026-11-04T23:15:46Z, `3304009` -> `0000000`: the first tag object (on `fee3706`), deleted just before the push of `main` to `33c0d53` (23:16:02Z).
- `branch_deletion` `refs/tags/note-2026-10-v2`, 2026-11-05T01:25:33Z, `fa72fe6` -> `0000000`: the second tag object (on `33c0d53`), deleted by Code just before the push of `main` to `6d8c237` and the new tag (01:25:35Z).

There is no force push; every other surface the read lists is empty. **The PI's ruling of 2026-11-04, on Code's question, "Accept the flag": the two deletions are the move's own, and the flag stands as written.**
