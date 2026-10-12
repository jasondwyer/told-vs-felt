# AUDIT-note-release v1.2 -- the release tag note-2026-10-v1: post-tag record

- Code stamp: 2026-10-12 22:28:53 UTC (date -u). Written after the push of the tag; committed after the tag, because the tag commit cannot hold its own hash (results/raw/2026-10-09_note-release-manifest.md, N18's self-reference statement). The note's footer, which block :133 asks to carry the tag commit hash, is the design seat's (AUDIT-note-release-v1_2.md@bbc9ffe:133).
- Tag `note-2026-10-v1`: annotated, tag object `60b7516eaef1e672d2ca88b31562c4eedeee3227`, tagger date 2026-10-12T18:09:34-04:00; message: "note-2026-10-v1: the release of the audit block AUDIT-note-release-v1_2.md, with note v0.6, the preprint at patch v7 and the three 2026-10-10 renders.".
- **The tag commit (R2): `98d07bc3c5735a7ca31d01ee458b400d07ff4b48`**, tree `cd782d6b81b8a9005775add2ef302e50ad8cc0ca`. Its parent, R1 (the N12 scripts for the release run): `e8fb54dc90bd0766f1686c41b7c2497a79fa5391`.
- Server refs after the push (`git ls-remote origin`, read at this run):
  - `refs/heads/main` `98d07bc3c5735a7ca31d01ee458b400d07ff4b48`
  - `refs/tags/note-2026-10-v1` `60b7516eaef1e672d2ca88b31562c4eedeee3227`
  - `refs/tags/note-2026-10-v1^{}` `98d07bc3c5735a7ca31d01ee458b400d07ff4b48`

## Files the tag commit holds, as the PI routed them (sha256 of the blob at the tag)

| path | sha256 at the tag |
|---|---|
| `PREPRINT-v1_0-draft.md` | `d9635ca24d32dcba193cd9aade273de2679c99c5c2218787b410e793a42d1fe6` |
| `RESEARCH-NOTE-v0_6-draft.md` | `2c7e1cf526f6dfe737c6246cf137f1ae9bc18816846e8329de2f9c3c04426fbb` |
| `2026-10-10_F1a_headline-strip.svg` | `6ffad6cd971aabdc70d7b684a6408988c9a05e5445125d3ce61a78557405cee6` |
| `2026-10-10_F1b_five-link-panels.svg` | `6fcb060f6a2cf2c0ce1f5374c3267c5cec67304994a9967e49a2afaffcf6113e` |
| `2026-10-10_F2_macar-lineage-roc_post.svg` | `81b13e805e64e6a9534e65e6dfeb50d6c6a65cf3d8b02b9cb3a1e36852e5ac4e` |
| `README-NOTE.md` | `e03da42ae4813baa7ef911fb3e533b47285bd1e9844d83135b3cd4400d307050` |
| `results/raw/2026-10-09_note-release-manifest.json` | `9a5cc889ac3abbf061a4d9f9a577decf21b9d75f3a0a2dad9a3b47caf99f7d2b` |
| `results/raw/2026-10-08_note-N12-scrub.md` | `10b6dbd64f42c75f63acf62173307bb3d1851a4b9feb0d6ba17cb945b1c0c2a2` |

## The release run at the tag commit, before the push (raws committed in this commit)

- History (`results/raw/2026-10-12_note-N12-history-release.md`, sha256 `05915036bbf71bee775920e113f34e7acdeccebcc681ab6d8495751e3a500872`): the (i) line carries the PI's answer of 2026-10-12 and reads 'This release run: TRUE-SECRET-CANDIDATE 0; UNTRIAGED 0 in every table'; its (v) line reads '(v): PASS'.
- Content screen (`results/raw/2026-10-12_note-N12-content-screen-release.json`, sha256 `5ef8e2830efdd93cc54f3338a4844f557c989c6f862aa13eb7bb5131bc409407`): written (the script writes only when its leak guard is clean).
- Licenses (`results/raw/2026-10-12_note-N12-licenses-release.md`, sha256 `bd471766e7d297b31028080786b6eccb8dedb7f81e9fd60174f58e0399598b80`): (iv) licenses recorded.
- Gitleaks (`results/raw/2026-10-12_note-N12-gitleaks-release.md`, sha256 `a6b30a53186c01c413ec6607ef7242b68be0693ba81907a029267153eddf15ed`): History findings: 6. TRUE-SECRET: 0. FALSE-POSITIVE: 6. UNTRIAGED: 0. TRIAGE entries re-found: 6 of 6. Completeness: gitleaks scanned 336 commits.
- Gitleaks, first run (`results/raw/2026-10-12_note-N12-gitleaks-release-run1.md`, sha256 `18c11e80602572d7903838de4b90fda2a5c664c1ae083681a703a9a348380aec`, kept as written; its Command line names the release path, under which it was first written): STOP on the skip probe, 0 probed paths gave a finding. Code's explanation: the probe's random 32-character value can contain one of the words gitleaks' generic-api-key rule treats as stopwords, and then no probe file gives a finding (reproduced with values containing 'client', 'access', 'token', 'example' and 'sample'; with 'secret' and 'abcdef' the finding stands). The run failed closed: its fallback scanned every historical version of all the paths it took as skipped, as text copies, and found only the known false-positive lines (their 1442 historical versions as copies: 8 findings, each a version of a line triaged FALSE-POSITIVE in history; run 1's history scan itself: History findings: 6. TRUE-SECRET: 0. FALSE-POSITIVE: 6. UNTRIAGED: 0.). The second run, at the release name, found the 4 skipped paths the rehearsal found.
- Password (`results/raw/2026-10-12_note-N12-password-release.md`, sha256 `01d8430996a16394bfdd183f0c9a3ee4c211c90bf2cc2e1c3bbf641a88cc2126`; counts and locators only, the value never written): (1) Tracked files at the ref (`git grep -i -F`): 0 hit line(s). (2) Blobs reachable from any ref, scanned by content: 1430 blobs, 447636541 bytes; 0 blob(s) contain it. (3) Commit messages scanned: 336; with it: 0. Tag annotations with it: 0. (4) Untracked, not-ignored working-tree files and extras scanned: 30; with it: 5. (the D4 handoff files, never committed, as at e0fd85c).
- N11 at the tag (`results/raw/2026-10-12_note-N11-smoke-tag.txt`, sha256 `3e20048d10d8957a4b5330ff33178edf189417102c6a73791a6b9a30ecd54c48`): N11: PASS at the release tag note-2026-10-v1 (98d07bc3c5735a7ca31d01ee458b400d07ff4b48).

## Still to run

- The pre-flip read (scripts/audit_note_N12_preflip.py: `git ls-remote origin` and the GitHub-side surfaces) runs just before the PI's visibility flip, at the PI's word, with that script updated for the release names in its own commit then (README-NOTE §8; the scrub index, section 10).
