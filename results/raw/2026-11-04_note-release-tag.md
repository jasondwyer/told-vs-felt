# AUDIT-note-release v1.2 -- the release tag note-2026-10-v2, moved: post-tag record

- Code stamp: Thu Nov  5 01:28:30 UTC 2026 (date -u). Written after the push of the moved tag; committed after the tag, because the tag commit cannot hold its own hash (`results/raw/2026-10-09_note-release-manifest.md`, its 'Tag commit' line: "A commit's hash is computed over a tree that contains this file, so the hash cannot be written inside it"). The file names carry the PI-local date of the runs, 2026-11-04.
- **2026-11-04: the tag `note-2026-10-v2` moved from `fee3706` to N18's fourth run, `6d8c237`, before publication, because of README.md:3**, by way of N18's third run, `33c0d53`. README.md:3 said "a LessWrong copy is under that site's review", which is false once the PI deletes the original LessWrong post (2026-11-04). The PI's decision of 2026-11-03, in the design seat's tag-move block (`results/raw/2026-11-03_note-design-to-code_tag-move.md@4358425`:7-8): "move the tag forward to a descendant on `main` before the flip"; "No commit is rewritten". No commit was rewritten: `fee3706`, `23ec9b1` and `881bd61` stay in `main`'s history, and the raws of `23ec9b1` and `881bd61` (`results/raw/2026-11-03_note-release-tag.md`, the first tag's re-run raws and N11, and its pre-flip read `results/raw/2026-11-03_note-N12-preflip.md`) are the first tag's record and stand (:15). The tag was never public at any of its three placements.
- Tag `note-2026-10-v2`: annotated, tag object `e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07`, tagger date 2026-11-04T20:10:15-05:00; message: "note-2026-10-v2: the second release of the audit block AUDIT-note-release-v1_2.md, with note v0.8, the preprint at patch v8 under its status banner and the three 2026-10-22 renders." and one line, as the block's item 3 orders (:14): "Moved from fee3706 on 2026-11-04, README.md:3." The two earlier tag objects, `33040097b13e9d1c9025c5b4039918b1efd44edb` (on `fee3706`, 2026-11-03) and `fa72fe6452295beadfa7def16e8ad5fd85281cb7` (on `33c0d53`, 2026-11-04, the same message as now), are deleted locally and on the server.
- **The tag commit (N18's fourth run): `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5`**, tree `92a16ab5db2e2b205be5de03f7b4e4112a0636e5`. Its parent, the README-NOTE re-point: `dba52b477998b151c1164b16da67d3d5758fda41`.

## The move, in order

After `881bd61` (the first tag's last post-tag commit):

1. `4358425`: the tag-move block, committed by path, as its header says.
2. `b4c9214`: README.md:3 with the clause deleted, no other line changed (the block's item 1). In the same commit, on the PI's answer of 2026-11-04 to Code's question, "Re-point both": README-NOTE.md :242 re-pointed to N18's third run and :4's source list given the block, and `scripts/audit_note_N18.py`'s tag-commit and re-run texts re-pointed to the third run, quoting the amended ruling at `4358425`:13.
3. `33c0d53`: N18's third run, the manifest regenerated in place (the block's item 2); the tag re-made on it (tag object `fa72fe6`). The re-runs at `33c0d53` ran there, before any push (below). `main` and that tag were then pushed from this checkout at 2026-11-04 18:16:02 -05:00, outside Code's session (the remote-tracking ref's reflog: "update by push").
4. Code's read-only review of the move (four checkers and a skeptic per finding) found README-NOTE.md §8 (:251, :252, :254) and :200 still stating the release sequence as it stood before the move, beside :242's new placement. On Code's question the PI first answered "Redo unpushed commits", on Code's statement that `b4c9214` and `33c0d53` had not been pushed; Code reset local `main` to `4358425` and deleted the local tag, then found that the server already held both commits and the tag (the push of 18:16:02), and restored local `main` and the local tag to match the server; nothing on the server was changed. Asked again with the push stated, the PI answered "Fourth N18 on top": nothing rewritten, a README-NOTE re-point on top of `33c0d53`, then N18's fourth run as the tag commit and the tag moved again, server delete first.
5. `dba52b4`: README-NOTE.md §8 (:241, :242, :251, :252, :254), :4 and :200 re-pointed to the moved tag, and N18's texts to the fourth run; a second read-only review of the change before its commit was applied.
6. `6d8c237`: N18's fourth run, the manifest regenerated in place: 148 files, all tracked and equal to HEAD; "Tag state at this run: absent."; the tag re-made on it (tag object `e6049b7`).

Code's orderings inside the block's items 2-4: the local tag was deleted just before each of N18's third and fourth runs rather than after them, so that the manifest records the tag as absent rather than naming the commit it then pointed to (item 1's rule: no tracked file names the tag commit's hash in place of the tag's name); N11 ran with the re-runs, before the push. Two commit messages are inexact and are corrected here, not rewritten: `b4c9214`'s "No tracked file outside the first tag's raws names the tag commit hash" leaves out the tag-move block itself, which names `fee3706`; `4358425`'s names the block's amendment of the 2026-10-28 answers' §8 but not of the tail of their §10 item 5, which the block also amends (:3).

## The push: delete first, then push

The block's item 3 (:14), after the re-runs below (the PI's answer of 2026-11-04 to Code's question, "Before the push"):

1. `git push origin :refs/tags/note-2026-10-v2`: "- [deleted] note-2026-10-v2" (the server's tag, then `fa72fe6` on `33c0d53`).
2. `git push origin refs/heads/main:refs/heads/main refs/tags/note-2026-10-v2:refs/tags/note-2026-10-v2`: "33c0d53..6d8c237 main -> main" (a fast-forward) and "* [new tag] note-2026-10-v2 -> note-2026-10-v2".

Server refs after the push (`git ls-remote --symref origin`, read at this run):

- `HEAD` -> `refs/heads/main`
- `refs/heads/main` `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5`
- `refs/tags/cycle-2-close` `f597ea7961a6d750600593ed4d770078e926adc8`
- `refs/tags/cycle-4-close` `2390272650dd1270bc4c465e3f521f92d10ed6f1` (`^{}` `50906bfef778dc1e4d8c311b304185db15a745c7`)
- `refs/tags/note-2026-10-v1` `60b7516eaef1e672d2ca88b31562c4eedeee3227` (`^{}` `98d07bc3c5735a7ca31d01ee458b400d07ff4b48`)
- `refs/tags/note-2026-10-v2` `e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07` (`^{}` `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5`)

The commits no local ref reaches (the origin-only ref's commit and the three wip branches' origin commits, read from the release-v2 records by the history script's own reader, in memory, never printed): asked of `jasondwyer/told-vs-felt` with `gh api repos/jasondwyer/told-vs-felt/commits/<commit>` after the push, each returns HTTP 422 (not served). The two deleted tag objects are still served by id (`gh api repos/jasondwyer/told-vs-felt/git/tags/<object>`: HTTP 200 for `33040097` and for `fa72fe6`), as GitHub keeps unreferenced objects; each holds only a tag message (the first tag's, and the one this tag carries) and points at a commit `main` reaches (`fee3706`, `33c0d53`; HTTP 200).

## Files the tag commit holds, as routed (sha256 of the blob at the tag)

| path | sha256 at the tag |
|---|---|
| `PREPRINT-v1_0-draft.md` | `5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467` |
| `RESEARCH-NOTE-v0_8-draft.md` | `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d` |
| `2026-10-22_F1a_headline-strip.svg` | `f0c1cd73e474eff54f11dd677a9b8e385ebae1e63cd667babc88d83123985bfc` |
| `2026-10-22_F1b_five-link-panels.svg` | `640c13e87b161dc8c14e2813acba1dc6a09b94d7beb5b9d1784cfe34371633af` |
| `2026-10-22_F2_macar-lineage-roc_post.svg` | `0e0459cf628ee7adef2d8c462a1b6c854d3a87a9743baa4f18b44134fbf969bc` |
| `README-NOTE.md` | `de4fffa266c78e38eb6862318b594f08f10aab6e0752493586ceaf27bb08d785` |
| `README.md` | `7880548da13d5f23579733ebd6a7ae94b7308a30d4b8099450ef5373fe1e2999` |
| `results/raw/2026-10-09_note-release-manifest.json` | `997f104cacf2636758ce5da3690143bc5ccb117327514f45e000a1666411e831` |
| `results/raw/2026-10-09_note-release-manifest.md` | `ea8417d3f469725171185293c2eba55bc0ab10e47a567e260872f45a2038a762` |
| `results/raw/2026-10-08_note-N12-scrub.md` | `75e684854d25a99cac55df9b180d48bb4f114abba3eabcd0e4a2f7c92435b83f` |
| `results/raw/2026-11-02_note-N1-v0_8-claims-ledger.md` | `3e9a6169d5cf9a1a701aa541a8e485335b188cd8bec0b910b8e0b45dcd326a81` |
| `results/raw/2026-11-02_note-N1-v0_8-claims-ledger.json` | `db54575552aaf2d97d0dab8997d059e6b311aa10d94f5df90f080602b635ef43` |
| `results/raw/2026-11-02_note-N1-v0_8_valuescheck.md` | `2e4c2239326ffd5cd56cfa1ec7c6234a8c9cdb8dec149b429cab1f85ba11c16d` |
| `results/raw/2026-11-03_note-design-to-code_tag-move.md` | `7ec1b53bf93636ce36e40ef703f40b5ec1fc46ad08cd97049dabd0470c6f171e` |
| `scripts/audit_note_N12_preflip.py` | `ac442fa3fcd10a2602aba6c24731d78af371f12f8685b0561a3061f2fe4f8f34` |
| `scripts/audit_note_N18.py` | `561659f411aa950f88afec537825be91b0516b396884c0c97788d2d4c9a35bef` |

Against the first tag commit (Code's check, `git diff --name-status fee3706 6d8c237`: 17 paths): changed, README.md, README-NOTE.md, `scripts/audit_note_N18.py` and N18's manifest (`.md`, `.json`); added, the tag-move block and the eleven post-tag raws of the first tag (`23ec9b1`: nine; `881bd61`: two); every other path, the note, the three renders and the preprint among them, unchanged.

## The re-runs at the tag commit, before the push (raws committed in this commit)

As at `23ec9b1` (the block's item 4, :15), and before the push on the PI's answer of 2026-11-04 ("Before the push"); history first, the password search last, between 01:10 and 01:25 UTC on 2026-11-05 (2026-11-04, PI-local).

- History (`results/raw/2026-11-04_note-N12-history-tag.md`, sha256 `61be121b38231a84ee6c3e3d79db008728c0d497f28d6c1528e0ab230cc7166f`; `.json` `e604c4de99661a088c251a6babde9ea348e705b6a0498b0261f5439b9f5693c5`): its (i) line, 'This tag-commit re-run, this script's part of (i): TRUE-SECRET-CANDIDATE 0; UNTRIAGED 0 in every table'; (v) PASS; controls ALL PASS; its guard: 1,141 candidates, 442 refused, 0 found in its outputs. The 2026-10-28 (i)-line answer's condition holds again at the new tag (the block's §2). Its (i) line names the gitleaks re-run's raw by its form, and as found at its run the first tag's (`results/raw/2026-11-03_note-N12-gitleaks-tag.md`): history runs first, and this tag commit's gitleaks raw, below, did not yet exist.
- Content screen (`results/raw/2026-11-04_note-N12-content-screen-tag.json`, sha256 `6e160128597908687708dbb6269096cc005ae4d769983e6680c76a6d735270b3`): written at `6d8c237` (the script writes only when its leak guard is clean; 35 values checked), with the retained finding recorded as the PI ruled on 2026-11-02 (`retained_in_history`, 1 entry).
- Licenses (`results/raw/2026-11-04_note-N12-licenses-tag.md`, sha256 `bbe5cf06c39f85d2fd91fdaac8dd1f45ac883b7f97358225833c5609122cfc08`; `.json` `d77eaa6576e567661b5dc02e9f3baf0db059e72c543eed5aa1a1d340d91fdd66`): **'(iv) NOT recorded -- failed conjunct(s): external-reference sweep: 0 unclassified ids.'** The id sweep leaves one repository id unclassified, `jasondwyer/told-vs-felt.wiki` (the raw prints it redacted, `jaso...28:b5085882`): this repository's own wiki URL, from the pre-flip read's `git ls-remote https://github.com/jasondwyer/told-vs-felt.wiki.git` probe, which the first tag's pre-flip JSON records (`results/raw/2026-11-03_note-N12-preflip.json@881bd61`:220) and which entered the tag's tree with the move. The script classifies the former name's wiki, `jasondwyer/jspace-lab.wiki`, as this repository's wiki (`scripts/audit_note_N12_licenses.py@6d8c237`:2678) and has no entry for the new name. The URL-host sweep leaves 0 unclassified; every other gate of the pass line holds. **The PI's ruling of 2026-11-04, on Code's question after the same finding at `33c0d53`, "Rule it covered": the id is this repository's own wiki; the raw stands as written, the ruling is recorded here, and the missing entry is added on `main` after the flip.**
- Gitleaks (`results/raw/2026-11-04_note-N12-gitleaks-tag.md`, sha256 `9669e9c995e4df5ea6fd49bd22333c3c1685d3028c1ebff16f277f4057c2550c`): 'History findings: 6. TRUE-SECRET: 0. FALSE-POSITIVE: 6. UNTRIAGED: 0.'; 412 commits scanned, `git rev-list --all --count` 413 less its one deletion-only commit.
- Password (`results/raw/2026-11-04_note-N12-password-tag.md`, sha256 `962b71ecaf8df5b551ea977527ccf0170a73462affa95921eadcbcbb8aff017d`; counts and locators only, the value never written; the PI typed it in chat on 2026-11-04, and it was read from a file outside the repository, deleted after the run): (1) tracked files at the tag: 0 hit lines; (2) 1,653 blobs reachable from any ref: 0 contain it; (3) 413 commit messages: 0, and 0 tag annotations; (4) 33 untracked files scanned: 5 with it, the design handoffs, never committed. It ran last. Code also checked the eight raws and the runs' stdout for it: 0 hits.

## N11 at the tag

- N11 (`results/raw/2026-11-04_note-N11-smoke-tag.txt`, sha256 `ff7b4bb2206480f1af7ce9fcaec35ddd0740ca111c58b5f4c295c7b92db2b14c`): 'N11: PASS at the release tag note-2026-10-v2 (6d8c237bfc6d85fc340917aa1a1c2daa136ddce5)'; the suite prints 154/154 from a fresh clone of the local repository, not of the published remote (the repository is not public at this run). The block's item 6 (:17), a fresh clone at the new tag with the count README.md states, runs after the pre-flip read, from the server; its record is committed with the pre-flip read's raw.

## The re-runs at `33c0d53`, superseded

The same six runs ran at `33c0d53` on 2026-11-04 (13:42-13:57 UTC), before any push of it; their raws, written under the names above, were never committed. Before N18's fourth run Code moved them out of the repository (N18 hashes every `results/raw/*_note-*` file on disk, and the tag commit must hold each file its manifest lists); they are kept outside it, and the re-runs at `6d8c237` supersede them under the same names. Their outcomes: history, TRUE-SECRET-CANDIDATE 0 and UNTRIAGED 0 in every table, (v) PASS, controls ALL PASS; content screen written (35 values checked; 1 retained entry); licenses, '(iv) NOT recorded' on the same one id, the finding the PI's ruling above answers; gitleaks, 6 findings, all false positives, 0 untriaged (410 commits); N11, PASS, 154/154; password, absent from every tracked file, blob (1,649), commit message (411) and tag annotation, 5 untracked design handoffs with it. Their sha256s, as written: history `.md` `121ee26b544f9cff5b04c87cb060f25d78f495983c32fbb26ced6bf53c53b2a9`, `.json` `16be055ad45c571d44b82fdf71961ecbfea431da3d77e4501fd7726ac16e70b0`; content screen `6e724ab99617bc704a4c787f8638b1f2042b2c41ab63ad0268b8636383608239`; licenses `.md` `57bcf9022c341f19cc45099579b75c0c2e4a8a138a084e79ab041351c922e218`, `.json` `9974d44b4ec49a8bb16a4f4ff5a5871eb6216c9d4ca4fb348d4e158e6c8a2105`; gitleaks `10bf38bca6a92356e9bd0561d5853e16712d4021d38e5031d91e6a62b97b6035`; password `93a644aace326c3cb3dfcc343a341e4ca84e82df68264f0f754dbe1cb5a937c8`; N11 `bccc3a8762f4b435eab62abc4ff6529807a468006e93a7f97cd904be084584fc`. Code's read-only read of those six raws against the first tag's (five readers over the raw pairs, a skeptic per finding) explained every changed hunk by run identity, the content of the commits since `fee3706`, the licenses finding, the remote-tracking ref's moves and the run order, and found no value in clear that the first tag's raws redact.

## Still to run, and the PI's

- The pre-flip read (`scripts/audit_note_N12_preflip.py`, unchanged, the block's item 5, :16), after this commit is pushed; its raw, `results/raw/2026-11-04_note-N12-preflip.md` and `.json`, is committed next, with the fresh clone's record (the block's item 6).
- The visibility flip: the PI's. After it, the PI's own steps of the release route: re-adding the repository to the Claude GitHub app and to Zenodo; then N11's run with `--source` set to the published remote (README-NOTE, section 3); on `main` only, `CITATION.cff` with the Zenodo DOI and, optionally, a README-NOTE line pointing at the blog's dated correction block (the block's §2), and the licenses script's entry for `jasondwyer/told-vs-felt.wiki` (the PI's ruling above).
