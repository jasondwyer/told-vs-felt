# AUDIT-note-release v1.2 -- after the flip: N11 from the published remote, the GitHub release on `note-2026-10-v2`, its Zenodo record, and `CITATION.cff`

- Date: 2026-11-04, the PI's calendar date. GitHub's and Zenodo's stamps below are UTC, as they record them, and git's carry their offset; the release was published on 2026-11-04 by the PI's calendar and on 2026-11-05 in UTC.
- The routing:
  - the design seat's release-block answers name "the Zenodo DOI on the tag" among the steps "At the flip (the PI, with the seat)" (`results/raw/2026-10-28_note-design-to-code_release-block-answers.md@908a659`:69);
  - the seat's r11 answers give the order at the flip: "the correction block (§2 and §3 item 1), the Zenodo DOI, the T+0 follow-up to the four author groups, then T+3" (`results/raw/2026-11-02_note-design-to-code_N1-r11-answers.md@da50cd1`:61);
  - the tag-move block: "After the flip, on `main` only: `CITATION.cff` with the Zenodo DOI; optionally a README-NOTE line pointing at the blog's dated correction block" (`results/raw/2026-11-03_note-design-to-code_tag-move.md@4358425`:21);
  - README-NOTE: N11 "asks for one more with `--source` set to the published remote once the repository is public" (`README-NOTE.md@8afb14c`:71);
  - the tag record's list of what remained after the flip (`results/raw/2026-11-04_note-release-tag.md@9edbc77`:83) and the PI's licenses ruling there, "Rule it covered" (:68).
- The PI's words in chat, 2026-11-04: "Repo is public. I authorized zenodo but not too sure what I should do with it"; then, after Code's four steps (Zenodo's switch for the repository, the GitHub release on the tag, the record's metadata, `CITATION.cff` on `main`), "Step 1 is done" and "please proceed with other steps".
- Section 8 lists the commands behind these reads; the documents read (GitHub's REST documentation, the `invenio-github` code, the CFF schema guide and schema) are named where they are used.

## 1. The flip, as read after it

- The repository: `visibility` public, default branch `main`, GitHub's license detection `apache-2.0`, `has_wiki` false.
- `git ls-remote https://github.com/jasondwyer/told-vs-felt.git` with no user or system git config and no credential helper (an anonymous read): nine refs, `HEAD`, `refs/heads/main`, the four tags and the peeled entries of the three annotated ones, each equal to this checkout's. Read five times: after the flip, before N11, before the release, after the refused first `gh` command (section 4) and after the release.

## 2. Zenodo's switch (the PI's)

- Before it (the PI's first message): no webhook and no release on the repository.
- After the PI's "Step 1 is done": one webhook, id 707598337, active, events `release`, content type JSON, posting to Zenodo's GitHub receiver (path `/api/hooks/receivers/github/events/`; the URL's query, which carries a token, was not read out), created 2026-11-05T03:53:24Z. Its ping was delivered with HTTP 202 at 2026-11-05T03:53:25Z.

## 3. N11 from the published remote

- Command (the raw's :12, run from the repository root): `/Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python scripts/audit_note_N11.py --ref note-2026-10-v2 --source https://github.com/jasondwyer/told-vs-felt.git --out results/raw/2026-11-04_note-N11-smoke-published.txt`.
- Raw: `results/raw/2026-11-04_note-N11-smoke-published.txt`, 3,493 lines, sha256 `3a411e78529c9da9ed124b4d2406f9ea7a2d60c6dda337d160ff8057dff67c08`. Its verdict line (:3359): "N11: PASS at the release tag note-2026-10-v2 (6d8c237bfc6d85fc340917aa1a1c2daa136ddce5); cloned from the published remote, https://github.com/jasondwyer/told-vs-felt.git; and resting on the design seat and the PI accepting N/N (here 154/154) in place of the block's 103/103 (note 1), which is Code's reading, not a ruling. The suite prints 154/154 from the fresh clone with no read outside the clone apart from the interpreter's own installation and its own temp files."
- Its section (1): the clone of the published remote checked out `refs/heads/main` at `8afb14c8d9959213291de6565bf300091b3fe1e8` before the detach, then `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5` ("equals --ref"), with an empty `git status --porcelain`. The header's 'HEAD (source repository, at run time)' line reads this checkout's `HEAD`, `8afb14c8d9959213291de6565bf300091b3fe1e8`, which was the published `main` at the run (section 1).
- N11's fix, Code's, made before the run: the verdict line at a tag and referent note 2 (:3310) were written for clones of the local repository, and printed "cloned from %s, not from the published remote (the repository is not public at this run)" and "(this audit makes no network access, so the remote form is not exercised here)" whatever `--source` named. A branch is added for a `--source` that begins `https://`, `http://`, `ssh://`, `git://` or `git@`: at a release tag, such a run names its `--source` as the published remote in note 2 and in the verdict line. The `file://` wording, and a run at a non-tag `--ref`, are unchanged. `scripts/audit_note_N11.py` sha256 before: `189699782f96497151bc5ad9904d12e7f9561cd11e3111ac7b4ad72355c1ab38` (at `8afb14c` and at the tag); as run, and as committed with this raw: `5ea671623e84a5b0d5f0f882b844f1185d446d921234b6f33c3e10555faac5db` (the raw's 'Script' line, :9). The next commit corrects the new code comment, which names referent note 2 '(3) item 2', and the module docstring, which says nothing is downloaded. It changes comments and the docstring only: a run would print the same body, but the script's sha256, which the header's 'Script' line prints, changes with it, and this raw's :9 names the version committed here.
- Text written for earlier passes is printed again, with this run's values and later annotations: the values-check sections (:3361-3448) and the closing section's opening bullets (from :3449). This run contradicts some of that text. Instances:
  - round 1's item 8: its finding (:3377), "no tag exists yet, and the clone source was the local repository", and its disposition (:3378), which ends "it was not exercised against a remote here, because this audit makes no network access";
  - the closing section's Fix bullet (:3451), which ends "Nothing else is computed differently; round 4 and this section are new."
- The closing comparison (from :3449) has no class for a line that differs only because `--source` differs from the compared raw's; it counts such lines under 'content at the new --ref', e.g. the header's 'Clone source' line (:6), the clone command (:33) and the lineage clone (:428).
- Placement: N11 ran before the release, as Code had told the PI it would.

## 4. The GitHub release (Code's, on the PI's "please proceed with other steps")

- First command: `gh release create note-2026-10-v2 --repo jasondwyer/told-vs-felt --verify-tag --notes-from-tag --title note-2026-10-v2`. gh 2.96.0 refused it ("using `--notes-from-tag` with `--repo` is not supported"), exit 1. No release was created (the releases list stayed empty), and the refs were unchanged.
- Second command: the same, with `--notes-file` in place of `--notes-from-tag`, naming a file that holds the tag object's message, the bytes of `git cat-file tag note-2026-10-v2` after its header (230 bytes; `git for-each-ref --format='%(contents)'` gives the same text plus one newline, 231 bytes, and was not used). It printed the release's URL and exited 0. `--verify-tag` refuses a tag that is not already on the remote, so no tag was made; the nine refs read after it are unchanged (section 1).
- The release: id 434768929, https://github.com/jasondwyer/told-vs-felt/releases/tag/note-2026-10-v2.
  - Tag and title `note-2026-10-v2`; at publication the tag is tag object `e6049b7b05f9dda30f0858eb0ca5bc4c567e8f07` on `6d8c237bfc6d85fc340917aa1a1c2daa136ddce5`.
  - Not a draft, not a prerelease, not immutable. GitHub marks it Latest (`releases/latest` returns it).
  - Published 2026-11-05T04:03:14Z by `jasondwyer`. Its `created_at`, 2026-11-05T01:10:15Z, is the same second as 6d8c237's commit date and the tag's tagger date (both 2026-11-04T20:10:15-05:00); GitHub gives a release's `created_at` as the date of its commit.
  - `target_commitish` `main`, the default branch, which a release on an existing tag does not use.
  - Its notes are the tag's message, byte for byte.
- The webhook's deliveries for it:
  - `release`/`released`, HTTP 202, 2026-11-05T04:03:16.047Z;
  - `release`/`published`, HTTP 409, 04:03:16.152Z;
  - `release`/`created`, HTTP 409, 04:03:16.182Z.
- How Zenodo treats those deliveries: the `invenio-github` package's `receivers.py` (master, read 2026-11-04) archives a release on any of the three actions (`published`, `released`, `created`) unless it is a draft. It answers `ReleaseAlreadyReceivedError` and `RepositoryDisabledError` with 409. The 202 shows the repository was enabled, so the two 409s are the same release received again, as the single record below bears out.

## 5. The Zenodo record

- Zenodo's records search for "jasondwyer/told-vs-felt", read 2026-11-04: 1 record. Zenodo's badge endpoint for the repository's GitHub id, 1444998581, redirects to https://doi.org/10.5281/zenodo.23969333. Both DOIs resolve through doi.org (HTTP 302 to the record's pages).
- Record 23969333 (read 2026-11-04):
  - version DOI `10.5281/zenodo.23969333`; concept DOI `10.5281/zenodo.23969332` (concept record 23969332);
  - created 2026-11-05T04:03:34Z; revision 3, updated 2026-11-05T04:03:34.564355Z (this section describes that revision);
  - published (state done, submitted); open access; no Software Heritage identifier at the read (`swh` empty).
- Its metadata, as Zenodo filled it (the tag carries no `CITATION.cff` or `.zenodo.json`):
  - title "jasondwyer/told-vs-felt: note-2026-10-v2";
  - version `note-2026-10-v2`;
  - publication date 2026-11-05, the release's UTC date;
  - resource type software;
  - creators: two personal names, each storing GitHub's display name as the whole family name, with no given name: "Jason Dwyer" (family name "Jason Dwyer"; no affiliation) and "Claude" (family name "Claude"; affiliation "@anthropics"). Zenodo took them from GitHub's contributor list for the repository (`jasondwyer`, 393 commits; `claude`, display name Claude, 18; the API's counts on 2026-11-04). The DOI's APA citation at this revision, with its HTML entity and italics rendered, reads "Jason Dwyer, & Claude. (2026). jasondwyer/told-vs-felt: note-2026-10-v2 (Version note-2026-10-v2) [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.23969333";
  - license Apache License 2.0 (`apache-2.0`; the API's legacy form gives `apache2.0`);
  - related identifier https://github.com/jasondwyer/told-vs-felt/tree/note-2026-10-v2, relation isSupplementTo;
  - description: the release notes (the tag's message) as HTML, two paragraphs;
  - no keywords.
- Its file: `jasondwyer/told-vs-felt-note-2026-10-v2.zip`, 277,363,394 bytes, `md5:af51e89331bd89af4818c8f0d0ca6a13`. This is GitHub's zip of the tag, which Zenodo fetches from the release's `zipball_url` (`invenio-github`'s release code, read 2026-11-04).
  - It was not downloaded here, so it is not compared with the tag.
  - The tag's `.gitattributes` has no export-ignore, export-subst or LFS line, so an archive of the tag carries every file of its tree. `git archive note-2026-10-v2` in this checkout lists 1,002 entries: the tree's 968 files and its 34 directories.
  - That archive's zip is 277,299,108 bytes. GitHub builds its own archive, so the two byte counts are not comparable.

## 6. On `main` (this commit)

- `CITATION.cff` (new; sha256 `426e0cc185903588b39fcd7212437a4b871d393eca7ca4100a503e6c21dbd69b`):
  - `doi` is the version DOI, "the Zenodo DOI on the tag" (908a659:69). `version` is the tag's name. `identifiers` lists both DOIs and the GitHub release's URL.
  - `repository-code` is the tag's tree URL, so that a citation built from the file points at the tag, where README.md:3 points readers ("`main` keeps moving and nothing points a reader at it"). `url` is the post, as README.md:3 gives it.
  - `authors`: Jason Dwyer, the holder LICENSING.md names ("Copyright 2026 Jason Dwyer.", `LICENSING.md@6d8c237`:3). The record's creators are the PI's to set (section 7), and `CITATION.cff` follows if they differ.
  - `date-released` "2026-11-04", the PI's calendar date of the release. The record's publication date is Zenodo's UTC date, 2026-11-05.
  - No `license` key. A CITATION.cff reads a list of licenses as alternatives ("When there are multiple licenses, it is assumed their relationship is OR, not AND", the CFF 1.2.0 schema guide), and LICENSING.md splits them by part (code under Apache-2.0; documents and data under CC BY 4.0). `message` states the split and names LICENSING.md.
  - `abstract`: README.md:3's first two sentences, with the bold, link and code markup dropped.
  - Checked against the CFF project's `schema.json` at its 1.2.0 tag (63,763 bytes, sha256 `0b8d22140da702d766df318dcff3a91af2f39521298dcf36d76315fd99cc169b`) by a scratch check: valid. A copy of this file with an unknown key added and the DOI's `10.` changed to `11.` fails on both.
  - The check implements `$ref`, type, const, properties, required, additionalProperties, enum, pattern (Python's `re`), items, minItems, uniqueItems, minLength, anyOf, oneOf and allOf. It does not check formats; the schema's date, orcid and url definitions, which carry formats, also carry patterns, and those it checks. Nor does it check maxLength, minimum and maximum, which the schema uses only in its `reference` definition; this file has no reference.
  - The licenses script does not read `CITATION.cff`: `.cff` is not among its text extensions (`TEXT_EXT`, which has `.cfg`). By hand, the file's hosts are github.com, in the repository's own URLs (`jasondwyer/told-vs-felt`, an entry of the script's `CLASS`), and jasondwyer.github.io, the PI's own site. The script's entries for jasondwyer.github.io, on the PI's word of 2026-10-29, cover this audit's files and README.md, not this file. Whether the sweep should read `.cff` is the PI's (a rule change, with a host entry for this carrier).
- `scripts/audit_note_N12_licenses.py` (sha256 `5429303b139d3228634a176562e192fc492d3e1a91b1f47cfd455294cdb23cad` before, `d1c9d37c1ea8946e402acf47afa09536ed97210d5edbf7ad2c025f9e89d5f325` after): the entry the PI's ruling of 2026-11-04 adds on `main` after the flip (9edbc77:68).
  - `CLASS_POSTFLIP` holds one id entry, `jasondwyer/told-vs-felt.wiki`, this repository's wiki under its new name: the `git ls-remote https://github.com/jasondwyer/told-vs-felt.wiki.git` probe of the first v2 tag's pre-flip read, exit 128 (`results/raw/2026-11-03_note-N12-preflip.json@881bd61`:220-221).
  - The raw and its JSON (`postflip_entries_applied`) list it apart from round 9's and release v2's entries. Every earlier rule and entry is unchanged.
  - A trial run at `8afb14c` with this script (Code stamp 2026-11-05 04:55:41 UTC; outputs outside the repository) printed "pass: (iv) licenses recorded", with the entry classifying 1 id. Its projection over N11's raw and a draft of this raw, both untracked at that run, left 0 ids and 0 hosts unclassified.
- `scripts/audit_note_N11.py`: the fix in section 3, as run.
- `results/raw/2026-11-04_note-N11-smoke-published.txt` (section 3) and this raw.
- The tag is not touched.

## 7. Open

- The PI's: the record's metadata on Zenodo. An edit there changes neither DOI.
  - Its creators need the PI's name split (family name "Dwyer", given name "Jason", as `CITATION.cff` has it) and the PI's decision on the second creator.
  - Its title, description and license are Zenodo's defaults; LICENSING.md's split needs CC BY 4.0 beside Apache-2.0.
  - Until the edit, the DOI's citation (section 5) and the one GitHub builds from `CITATION.cff` differ in authors and title.
- The order at the flip. The seat's r11 answers put the blog's correction block before the Zenodo DOI (da50cd1:61).
  - The post carries a dated block, headed "Update and correction, 2026-11-04.", and it was live before the webhook was created. The GitHub Pages build now serving the post (the blog repository's commit 840e000) finished at 2026-11-05T03:08:39Z; the webhook was created at 03:53:24Z.
  - Whether it is the block the seat names ("§2 and §3 item 1") is the PI's and the seat's to say. If it is, the order at the flip held.
  - Code's flag to the PI before the release assumed that the site was down and the block not yet posted; by then the post carried the dated block.
- The optional README-NOTE line pointing at the correction block (4358425:21): the block exists; the line is the PI's to ask for.
- N11, from the review of this change, for a later pass:
  - a network `--source` is recognized by its prefix, not by git's own rule for URLs, and the branch names any such source "the published remote";
  - at a non-tag `--ref`, a network run keeps the pre-release wording ("No release tag exists yet", "this audit makes no network access");
  - the `file://` verdict at a tag still says "(the repository is not public at this run)", which is false for any such run after the flip.
- Before any later GitHub release: the webhook stays active and the repository has no `.zenodo.json`, so Zenodo would read `CITATION.cff` at that release's tag for the new version's metadata. The file names this release throughout (`message`, `abstract`, `version`, `doi`, `identifiers`, `repository-code`, `date-released`); it needs updating before such a release, or a `.zenodo.json` added.
- Not done here: a comparison of the record's file with the tag, which needs the 277 MB archive downloaded.
- The PI's, from the release route and the seat's order at the flip: re-adding the repository to the Claude GitHub app; the T+0 follow-up; T+3.
- Before the push, Code's gate: the history scan and the licenses script at the pushed commit, their outputs outside the repository. Their outcomes are not in this commit.

## 8. Reads

- GitHub, through `gh api` (GET):
  - `repos/jasondwyer/told-vs-felt` (visibility, default branch, license, has_wiki);
  - `repos/jasondwyer/told-vs-felt/hooks` (id, active, events, content type, created_at, the URL's host and path);
  - `repos/jasondwyer/told-vs-felt/hooks/707598337/deliveries` (event, action, status code, delivery time);
  - `repos/jasondwyer/told-vs-felt/releases`, `releases/434768929` and `releases/latest`;
  - `repos/jasondwyer/told-vs-felt/contributors?per_page=100`, `users/claude` and `users/jasondwyer` (display names; the repository's id, 1444998581, is in `repos/jasondwyer/told-vs-felt`);
  - for the blog, `repos/jasondwyer/jasondwyer.github.io/pages/builds/latest` and the repository's latest commits (dates only).
- Zenodo's records API, `/api/records/23969333`, in its default form and with `Accept: application/vnd.inveniordm.v1+json`; its records search, `/api/records?q="jasondwyer/told-vs-felt"`; its badge endpoint, `/badge/latestdoi/1444998581`.
- doi.org: `https://doi.org/10.5281/zenodo.23969333` and `https://doi.org/10.5281/zenodo.23969332` (redirects), and the first with `Accept: text/x-bibliography; style=apa`.
- git, in this checkout: `git cat-file tag note-2026-10-v2` and `git for-each-ref --format='%(contents)' refs/tags/note-2026-10-v2`; `git log -1 --format=%cI 6d8c237`; `git ls-tree -r note-2026-10-v2`; `git show note-2026-10-v2:.gitattributes`; `git archive note-2026-10-v2`, as tar (entries) and as zip (bytes); the anonymous `git ls-remote` of section 1.
- The post, as served: https://jasondwyer.github.io/2026-10-27-told-vs-felt-porting-behavioral-pharmacology/ (the dated block's heading).
- Hashes: `shasum -a 256` of each file this raw hashes; for the 'before' values, `git show HEAD:<path> | shasum -a 256` at `8afb14c`.
- The licenses trial: `jlens-qwen36/.venv/bin/python -B scripts/audit_note_N12_licenses.py --out <outside>/lic_trial2.md --json-out <outside>/lic_trial2.json`, at `8afb14c`, with the working-tree script (section 6).
