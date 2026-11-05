# AUDIT-note-release v1.2 -- N12 pre-flip read (release v2)

- Code stamp: Thu Nov  5 01:35:25 UTC 2026 (date -u); HEAD `9edbc77002aaca5e22f0a13cfce7c44dc1316174`; repository `jasondwyer/told-vs-felt` (origin `https://github.com/jasondwyer/told-vs-felt.git`).
- Script: `scripts/audit_note_N12_preflip.py` sha256 `ac442fa3fcd10a2602aba6c24731d78af371f12f8685b0561a3061f2fe4f8f34`; the history script `scripts/audit_note_N12_history.py` sha256 `918dae5a735240c379e679c61f20816775c10918736715f6e1ec0c6ae3cabaa8` at HEAD, equal to the pinned `918dae5a735240c379e679c61f20816775c10918736715f6e1ec0c6ae3cabaa8` (working tree: equal).
- The read, as the release block names it (`results/raw/2026-10-27_note-design-to-code_release-block.md@2fb0cf0:46`, item 6, asserted verbatim at this run): "`git ls-remote origin` = `main` + tags only (`cycle-2-close`, `cycle-4-close`, `note-2026-10-v1`, `note-2026-10-v2`); the GitHub-side surfaces (PRs, issues, Actions, wiki, Pages, deploy keys, webhooks, force-pushes). Any remaining `wip/*`, `main-*` or `claude/*` head: STOP and report." Under the release route (the PI's word of 2026-10-29, "fresh repository at the tag push, as proposed"), this read is of the new repository, and it checks there that the commits no local ref reaches are not served.
- Read-only: `git ls-remote`, `git rev-parse`, `git cat-file`, `git remote get-url` and `gh api` GET reads; nothing fetched, pushed or written but this file and its JSON (and the history script's outputs, outside the repository). It prints ref names, flags, counts and HTTP statuses: no GitHub-side text, no unexpected ref by name, no commit id of the four in section 3.

## 1. Server refs (`git ls-remote --symref origin`)

| ref | on the server | local | equal | object local | its commit |
|---|---|---|---|---|---|
| `refs/heads/main` | `9edbc77002aaca5e22f0a13cfce7c44dc1316174` | `9edbc77002aaca5e22f0a13cfce7c44dc1316174` | yes | yes | `9edbc77002aaca5e22f0a13cfce7c44dc1316174` |
| `refs/tags/cycle-2-close` | `f597ea7961a6d750600593ed4d770078e926adc8` | `f597ea7961a6d750600593ed4d770078e926adc8` | yes | yes | `f597ea7961a6d750600593ed4d770078e926adc8` |
| `refs/tags/cycle-4-close` | `2390272650dd1270bc4c465e3f521f92d10ed6f1` | `2390272650dd1270bc4c465e3f521f92d10ed6f1` | yes | yes | `50906bfef778dc1e4d8c311b304185db15a745c7` |
| `refs/tags/note-2026-10-v1` | `60b7516eaef1e672d2ca88b31562c4eedeee3227` | `60b7516eaef1e672d2ca88b31562c4eedeee3227` | yes | yes | `98d07bc3c5735a7ca31d01ee458b400d07ff4b48` |
| `refs/tags/note-2026-10-v2` | `e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07` | `e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07` | yes | yes | `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5` |

- HEAD on the server points at `refs/heads/main`.
- Refs on the server beyond these five: 0; `wip/*`, `main-*` or `claude/*` heads: 0.

**Pass/STOP line (1):** PASS -- the server holds `main` and the four tags only, each equal to the local ref, and HEAD points at `main`.

## 2. GitHub-side surfaces (read-only `gh api`)

| surface | count |
|---|---|
| pull requests | 0 |
| issue comments | 0 |
| review comments | 0 |
| commit comments | 0 |
| releases | 0 |
| deploy keys | 0 |
| webhooks | 0 |
| milestones | 0 |
| forks | 0 |
| issues | 0 |
| workflows | 0 |
| actions runs | 0 |
| artifacts | 0 |
| discussions | 0 |
| deployments | 0 |
| environments | 0 |
| wiki refs | 0 |
| Pages (`repos/jasondwyer/told-vs-felt/pages`) | HTTP 404 |
| Projects (v2), not in the block's list | not read (the token lacks the scope) |

- Activity record: 8 record(s), by type branch_creation 1, branch_deletion 2, push 5; by ref `refs/heads/main` 6, `refs/tags/note-2026-10-v2` 2.
- Repository: `jasondwyer/told-vs-felt`, created 2026-11-04T00:50:14Z, private True, visibility private, default branch `main`, fork False, archived False; has_issues True, has_projects True, has_wiki False, has_pages False, has_discussions False, allow_forking True; description 73 characters, homepage 0 characters, topics 0 (texts not printed).

**Pass line (2):** FLAG -- activity record: force push 0, branch deletion 2, records on other refs 0, read exit 0.

## 3. The commits no local ref reaches (the release route's check)

The origin-only ref's commit and the three wip branches' origin commits, read from the release-v2 records by the history script's `read_v2_record`, held in memory and never printed; each asked of this repository with `gh api repos/jasondwyer/told-vs-felt/commits/<commit>`.

- commit 1 of 4: HTTP 422, not served
- commit 2 of 4: HTTP 422, not served
- commit 3 of 4: HTTP 422, not served
- commit 4 of 4: HTTP 422, not served

**Pass line (3):** PASS -- none of the four is served.

## 4. The interim history scan

`jlens-qwen36/.venv/bin/python scripts/audit_note_N12_history.py --out <outside>/history_interim.md --json-out <outside>/history_interim.json` (outputs outside the repository; exit 0; 377.2 s): true-secret candidates 0; untriaged 0 (ids 0, sweep 0, shape rows 0; pending files 0); found verbatim 0; controls ALL PASS.

**Pass line (4):** PASS

## 5. For the PI

- Not all parts pass (above): not ready for the flip.
- After the flip, the PI's own steps from the release route: re-adding the repository to the Claude GitHub app and to Zenodo.
