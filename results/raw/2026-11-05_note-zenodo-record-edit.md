# AUDIT-note-release v1.2 -- after the flip: the PI's edit of the Zenodo record, `CITATION.cff`'s author entry, and orcid.org as a public host

- Date: 2026-11-05, the PI's calendar date. Zenodo's stamps below are UTC.
- This raw closes the first open item of `results/raw/2026-11-04_note-release-zenodo.md@e0693ea` (section 7, :95-98): the PI's edit of the record's metadata, with the PI's decision on the second creator.
- The PI's words in chat, 2026-11-05, each an answer to Code's question:
  - "Just me", to "Should Claude stay listed as a creator on the Zenodo record?";
  - "Yes, I edited and published it", to "Want me to check the Zenodo record after you save your edit?";
  - "Yes, add them", to "Add your ORCID and affiliation to CITATION.cff?";
  - "Yes, add it", to "Add orcid.org to the history scan's public hosts so the ORCID can go in CITATION.cff?".

## 1. The record after the PI's edit

- Record 23969333, read through Zenodo's records API (`/api/records/23969333`, in its InvenioRDM form and its legacy form) on 2026-11-05:
  - revision 4, updated 2026-11-05T05:56:28Z, published;
  - version DOI `10.5281/zenodo.23969333` and concept DOI `10.5281/zenodo.23969332`, unchanged;
  - the latest version of its concept: the InvenioRDM form gives `versions` index 1, is_latest; the legacy form gives `relations.version` index 0, is_last (it counts from 0).
- Its metadata at revision 4:
  - title "told-vs-felt";
  - publication date 2026-11-04; version `note-2026-10-v2`; resource type software;
  - one creator, a personal name: family name "Dwyer", given name "Jason", ORCID iD 0009-0006-7648-9086, affiliation "Sentieum Lab", role researcher; no contributors;
  - rights, in the InvenioRDM form: Apache License 2.0 (`apache-2.0`) and Creative Commons Attribution 4.0 International (`cc-by-4.0`); the legacy form lists one license, `apache2.0`;
  - related identifiers, both isSupplementTo: https://github.com/jasondwyer/told-vs-felt/tree/note-2026-10-v2 (resource type software) and the post, https://jasondwyer.github.io/2026-10-27-told-vs-felt-porting-behavioral-pharmacology/ (publication-report);
  - description, the PI's text: "Companion code to the Research Note published 2026-10-27. Told-vs-felt: porting behavioral pharmacology frameworks to measure internal state valence in language models.", then the post's URL;
  - no keywords;
  - the code repository, the InvenioRDM form's custom field `code:codeRepository`: https://github.com/jasondwyer/told-vs-felt, the repository root, which shows `main`, not the tag;
  - publisher Zenodo.
- Its file is unchanged: `jasondwyer/told-vs-felt-note-2026-10-v2.zip`, 277,363,394 bytes, `md5:af51e89331bd89af4818c8f0d0ca6a13`.
- What the edit replaced, revision 3's defaults (the earlier raw, section 5):
  - the title "jasondwyer/told-vs-felt: note-2026-10-v2";
  - two creators, "Jason Dwyer" (the whole name as the family name) and "Claude";
  - Apache-2.0 alone;
  - one related identifier, the tag's tree;
  - the tag's message as the description;
  - the publication date 2026-11-05.

## 2. The DOI's registered metadata

- Read through doi.org content negotiation on 2026-11-05, after the edit.
- APA (`Accept: text/x-bibliography; style=apa`), with its italics rendered: "Dwyer, J. (2026). told-vs-felt (Version note-2026-10-v2) [Computer software]. Zenodo. https://doi.org/10.5281/ZENODO.23969333".
- DataCite's JSON (`Accept: application/vnd.datacite.datacite+json`):
  - one creator, "Dwyer, Jason" (Personal; given name Jason, family name Dwyer; ORCID 0009-0006-7648-9086; affiliation Sentieum Lab);
  - title told-vs-felt; publication year 2026, Issued 2026-11-04; version note-2026-10-v2;
  - rights apache-2.0 and cc-by-4.0;
  - related identifiers: IsSupplementTo the tag's tree and the post, and IsVersionOf 10.5281/zenodo.23969332.

## 3. `CITATION.cff` (this commit)

- Compared with revision 4, these fields match: title, the author's family and given names, the number of authors (1), version, date (2026-11-04) and DOI. The author's ORCID iD and affiliation were missing.
- `CITATION.cff` and the DOI's registration (section 2) now name the same single author and the same title, so the difference in authors and title that the earlier raw's :98 recorded is gone.
- Added to the author entry, on the PI's "Yes, add them":
  - `orcid`: the iD 0009-0006-7648-9086, in the URL form the CFF schema's orcid definition requires;
  - `affiliation`: Sentieum Lab.
- Nothing else changes. sha256 before: `426e0cc185903588b39fcd7212437a4b871d393eca7ca4100a503e6c21dbd69b` (as committed at `e0693ea`); after: `bcb7c63964d5d9f0ae67dea44b05fbceebcf2e451bd3e00d3694c7598f357f7e`.
- Checked with the earlier raw's scratch check against the CFF 1.2.0 schema (section 6 there), which applies the orcid definition's pattern: valid. A copy with the iD one digit short fails on that pattern.
- The ORCID URL brings its host, orcid.org, into the repository's history with this commit. The history scan reads every committed text file, `CITATION.cff` included, and classes a URL host that has no entry as UNTRIAGED, which the PI's STOP set for the v2 history run makes a STOP (`scripts/audit_note_N12_history.py`, `I_STOP_SET_V2_WORDS`). On the PI's "Yes, add it":
  - `scripts/audit_note_N12_history.py`'s `PUBLIC_HOSTS` gains orcid.org (sha256 `918dae5a735240c379e679c61f20816775c10918736715f6e1ec0c6ae3cabaa8` before, `00e5b0d107dcae71cc01321bb05e37cab730bd935eee7dae6b3464a3373689ac` after);
  - `scripts/audit_note_N12_licenses.py`'s list of that allowlist's entries gains it too, as a member of the same class with no new rule, as the round-9 hosts were (the list's comment citing the PI's answer of 2026-10-12). The licenses script checks that list against the history script's `PUBLIC_HOSTS` by AST. Its sha256: `d1c9d37c1ea8946e402acf47afa09536ed97210d5edbf7ad2c025f9e89d5f325` before, `dfc75af676658e80c538cf2ddaf14a3154f7b5cac580760daf499c1dbeb45fc6` after.
- The licenses script does not read `.cff` itself (the earlier raw, section 6).
- `scripts/audit_note_N12_preflip.py` pins the history script's sha256 (`HIST_SCRIPT_SHA`, :82, the value before). This commit moves it, so a later pre-flip read will report the history script as not equal to its pin until the pin is re-derived.

## 4. Open

- Still open from the earlier raw's section 7:
  - whether the post's dated block is the one the seat's order names;
  - the optional README-NOTE line pointing at it;
  - N11's later-pass items;
  - before any later GitHub release, `CITATION.cff` or a `.zenodo.json` (:108). Zenodo starts a version that a GitHub release makes from its defaults and what the release's tag carries, so such a version's metadata may need an edit like revision 4's;
  - the archive comparison;
  - the PI's own steps: the Claude GitHub app, the T+0 follow-up, T+3.
- Still open from the earlier raw's section 6 (:84): whether the licenses sweep should read `.cff` (the PI's; a rule change, with a host entry for that carrier).
- New, the PI's: the record's code repository field points at the repository root, which shows `main`, where README.md:3 points readers at the tag. A further edit can set it to the tag's tree, https://github.com/jasondwyer/told-vs-felt/tree/note-2026-10-v2, the URL `CITATION.cff`'s `repository-code` gives.
- Before the push, Code's gate: the history scan and the licenses script at the pushed commit, their outputs outside the repository. Their outcomes are not in this commit.
