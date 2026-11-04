# AUDIT-note-release v1.2 -- the release tag note-2026-10-v2: post-tag record

- Code stamp: Wed Nov  4 00:54:21 UTC 2026 (date -u). Written after the push of the tag; committed after the tag, because the tag commit cannot hold its own hash (`results/raw/2026-10-09_note-release-manifest.md`, its 'Tag commit' line: "A commit's hash is computed over a tree that contains this file, so the hash cannot be written inside it"). The file names carry the PI-local date of the runs, 2026-11-03.
- Tag `note-2026-10-v2`: annotated, tag object `33040097b13e9d1c9025c5b4039918b1efd44edb`, tagger date 2026-11-03T13:24:51-05:00; message: "note-2026-10-v2: the second release of the audit block AUDIT-note-release-v1_2.md, with note v0.8, the preprint at patch v8 under its status banner and the three 2026-10-22 renders."
- **The tag commit (N18's second run): `fee3706617c70ba0dfbd8425977309fdeadd6472`**, tree `b2000bdf9d88b482b5a126b569811fc1506b6ee3`. Its parent, the preflip-script commit: `c514caaac2ac2bc5708bc0240a868b687471e6cd`.
- Release v2's commits after the round-11 ledger's first commit, in order: `979700f` (the ledger), `e65e4d4` (N18's first run), `091116f` (README-NOTE re-point), `71bba9a` (README.md: the PI's canonical-copy sentence, the PI's words of 2026-11-03), `87cbd82` (the ledger's W3 and O3 correction, on the PI's word of 2026-11-03, "Yes fix it if it's wrong."), `022a9e8` (README-NOTE re-pointed to it), `c514caa` (the preflip script), `fee3706` (N18's second run, the tag commit).

## The push: the release route

The PI's word of 2026-10-29, "fresh repository at the tag push, as proposed" (the scrub index, `results/raw/2026-10-08_note-N12-scrub.md` section 14), as run on 2026-11-03 after the re-runs below:

1. The existing repository (id 1304587748) renamed `told-vs-felt-old`; it stays private.
2. A new, empty, private repository created as `jasondwyer/jspace-lab` (id 1444998581), with the old repository's settings: wiki off, issues and projects on, its description copied as written.
3. `main` and the four tags pushed to it by URL (`git push https://github.com/jasondwyer/jspace-lab.git` with explicit refspecs for `refs/heads/main` and the four tags; nothing else).
4. The new repository renamed `told-vs-felt`; `jasondwyer/jspace-lab` now redirects to it (id 1444998581), and the local `origin` URL names it.

Server refs after the push (`git ls-remote --symref origin`, read at this run):

- `HEAD` -> `refs/heads/main`
- `refs/heads/main` `fee3706617c70ba0dfbd8425977309fdeadd6472`
- `refs/tags/cycle-2-close` `f597ea7961a6d750600593ed4d770078e926adc8`
- `refs/tags/cycle-4-close` `2390272650dd1270bc4c465e3f521f92d10ed6f1` (`^{}` `50906bfef778dc1e4d8c311b304185db15a745c7`)
- `refs/tags/note-2026-10-v1` `60b7516eaef1e672d2ca88b31562c4eedeee3227` (`^{}` `98d07bc3c5735a7ca31d01ee458b400d07ff4b48`)
- `refs/tags/note-2026-10-v2` `33040097b13e9d1c9025c5b4039918b1efd44edb` (`^{}` `fee3706617c70ba0dfbd8425977309fdeadd6472`)

The commits no local ref reaches (the origin-only ref's commit and the three wip branches' origin commits, read from the release-v2 records by the history script's own reader, in memory, never printed): asked of the new repository with `gh api repos/jasondwyer/told-vs-felt/commits/<commit>`, each returns HTTP 422 (not served); the old repository, `told-vs-felt-old`, returns 200 for each. The pre-flip read checks this again (its section 3).

## Files the tag commit holds, as routed (sha256 of the blob at the tag)

| path | sha256 at the tag |
|---|---|
| `PREPRINT-v1_0-draft.md` | `5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467` |
| `RESEARCH-NOTE-v0_8-draft.md` | `6fcfbfd64784412d616d4de40d4a6a54596202a052cb3dd0d9d78a26cbe1198d` |
| `2026-10-22_F1a_headline-strip.svg` | `f0c1cd73e474eff54f11dd677a9b8e385ebae1e63cd667babc88d83123985bfc` |
| `2026-10-22_F1b_five-link-panels.svg` | `640c13e87b161dc8c14e2813acba1dc6a09b94d7beb5b9d1784cfe34371633af` |
| `2026-10-22_F2_macar-lineage-roc_post.svg` | `0e0459cf628ee7adef2d8c462a1b6c854d3a87a9743baa4f18b44134fbf969bc` |
| `README-NOTE.md` | `178b53b9a5e11fbf02f1110f7821ec8a142e3334df4a9d633cd710ead0a75731` |
| `README.md` | `7967d33aff7795e3132c2f17059290065c69e7b929ba3f49cec34886d82354da` |
| `results/raw/2026-10-09_note-release-manifest.json` | `dc8966a49f7ccab309735eaf3809da439b81d814610eb0543745704c73c707c1` |
| `results/raw/2026-10-09_note-release-manifest.md` | `0ba182d6ba9790ca71f366fd5628740db3980c43a3ed62b31b6d16d5dd3edbfe` |
| `results/raw/2026-10-08_note-N12-scrub.md` | `75e684854d25a99cac55df9b180d48bb4f114abba3eabcd0e4a2f7c92435b83f` |
| `results/raw/2026-11-02_note-N1-v0_8-claims-ledger.md` | `3e9a6169d5cf9a1a701aa541a8e485335b188cd8bec0b910b8e0b45dcd326a81` |
| `results/raw/2026-11-02_note-N1-v0_8-claims-ledger.json` | `db54575552aaf2d97d0dab8997d059e6b311aa10d94f5df90f080602b635ef43` |
| `results/raw/2026-11-02_note-N1-v0_8_valuescheck.md` | `2e4c2239326ffd5cd56cfa1ec7c6234a8c9cdb8dec149b429cab1f85ba11c16d` |
| `scripts/audit_note_N12_preflip.py` | `ac442fa3fcd10a2602aba6c24731d78af371f12f8685b0561a3061f2fe4f8f34` |

## The re-runs at the tag commit, before the push (raws committed in this commit)

The release order as the design seat's answers of 2026-11-02 list it puts the post-tag scans after the push and the pre-flip read (`results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:60). Code ran all five at the tag commit before the push, as v1's were run (`results/raw/2026-10-12_note-release-tag.md@11cc35b`, 'The release run at the tag commit, before the push') and as the committed history and gitleaks scripts state for these re-runs ('this run is this script's re-run, which the release sequence makes at the tag commit, before the push'; 'The re-runs at the tag commit, before the push, their raws committed after the tag'): nothing reached GitHub before every scan had run. That is the one departure from the listed order.

- History (`results/raw/2026-11-03_note-N12-history-tag.md`, sha256 `a6f4515fe43f1809e8fb734bca702d4c47a135e2b61d2edc1a4615612724d79d`; `.json` `b20805d16cc1d1739fe6e836ff09a32c7fc93663be3040565b40d7cda30079e4`): its (i) line, 'This tag-commit re-run, this script's part of (i): TRUE-SECRET-CANDIDATE 0; UNTRIAGED 0 in every table'; (v) PASS; controls ALL PASS; its guard: 1,141 candidates, 442 refused, 0 found in its outputs.
- Content screen (`results/raw/2026-11-03_note-N12-content-screen-tag.json`, sha256 `47b5271a6ea89e3050c928b8200006dfbf99493b353714d262266212d4dbd913`): written (the script writes only when its leak guard is clean; 35 values checked), with the retained finding recorded as the PI ruled on 2026-11-02 (`retained_in_history`, 1 entry).
- Licenses (`results/raw/2026-11-03_note-N12-licenses-tag.md`, sha256 `fa21ba69f12d6cb8a601f7b0597e97607f17f1547badac1c59f95bf87be19559`; `.json` `8afac9b5428e4449eafe739cda82d8f61f2b8f08f10775f64b3ac60fff055a8b`): '(iv) licenses recorded' at `fee3706`; its id and host sweeps leave 0 unclassified.
- Gitleaks (`results/raw/2026-11-03_note-N12-gitleaks-tag.md`, sha256 `3e24dd95fa371797a9e7c14c4d27f171aa850844aa4addc86fad0f767aea979d`): 'History findings: 6. TRUE-SECRET: 0. FALSE-POSITIVE: 6. UNTRIAGED: 0.'; 405 commits scanned, `git rev-list --all --count` 406 less its one deletion-only commit.
- Password (`results/raw/2026-11-03_note-N12-password-tag.md`, sha256 `b916fd48720b738568d2f10970084269112fc362af7b3f0c5938ff6004a97ead`; counts and locators only, the value never written; the PI typed it in chat on 2026-11-03, and it was read from a file outside the repository, deleted after the run): (1) tracked files at the tag: 0 hit lines; (2) 1,632 blobs reachable from any ref: 0 contain it; (3) 406 commit messages: 0, and 0 tag annotations; (4) 32 untracked files scanned: 5 with it, the design handoffs, never committed. It ran last.

Code's read of the four scan raws written first (history, content screen, licenses, gitleaks), each diffed against its v2 release run of 2026-10-30 (`2f2c8b5`) and the history raw also against a rehearsal at `022a9e8`: every changed hunk is explained by run identity, by the content of the commits since `530aca4`, by the history and content scripts' changes (`bec62e3`, `b562977`) or by the tag-run framing (history 72 hunks, content screen 30, licenses 26, gitleaks 8); no value appears in clear. One label in the licenses raw is older than this run and unchanged by it: its '21 data/olmo/ JSON artifacts' counts the other files of that row too (data/olmo/ holds 16), as the 2026-10-30 raw's '20' did.

## N11 at the tag

- N11 (`results/raw/2026-11-03_note-N11-smoke-tag.txt`, sha256 `a989d9fec949616981183c60bb5181ed367431fb39e8ac65a5896498bfebe177`): 'N11: PASS at the release tag note-2026-10-v2 (fee3706617c70ba0dfbd8425977309fdeadd6472)'; the suite prints 154/154 from a fresh clone of the local repository, not of the published remote (the repository is not public at this run). This is the release-commit run the design seat's answers owe (`results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:51) and that the note's :214 states ('154/154 from a fresh clone at the tag').

## Still to run, and the PI's

- The pre-flip read (`scripts/audit_note_N12_preflip.py`, release v2's read since `c514caa`), after this commit is pushed: the server refs (`main` and the four tags only), the GitHub-side surfaces, the four commits again, and the interim history scan, which covers this commit. Its raw, `results/raw/2026-11-03_note-N12-preflip.md` and `.json`, is committed next.
- The visibility flip: the PI's. After it, the PI's own steps of the release route: re-adding the repository to the Claude GitHub app and to Zenodo; then N11's run with `--source` set to the published remote (README-NOTE, section 3); the correction block, the Zenodo DOI, the T+0 follow-up and T+3, in the design seat's order (`results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:61).
- At this writing, `https://jasondwyer.github.io/` and the note's canonical URL that README.md names answer GitHub's "Site not found" page (HTTP 404), though the Pages API reports the site built on 2026-10-29; the PI was told on 2026-11-03.
