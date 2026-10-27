# Code → design seat / PI — the release block: what is verified, and what the runs need decided first (note arc; 2026-10-27)

*Code. This file answers `results/raw/2026-10-27_note-design-to-code_release-block.md`, committed at `2fb0cf0` and cited below as "block :line". The laptop reached `2fb0cf0` by `git fetch origin main` and a fast-forward merge of `origin/main`. After that, seven reader agents mapped every script the block runs, read-only: no audit script was run and no git command changed state. Three refuters then values-checked this file against the repository at `2fb0cf0`, and their findings are applied below. Calendar dates only. Each point says whose call it is and gives Code's recommendation; nothing here is applied. Figures marked "estimate" or "predicted" were not produced by running the script in question.*

## 0. Verified (Code's checks at `2fb0cf0`)

- **Block §1 item 1.** `origin` is `https://github.com/jasondwyer/told-vs-felt.git`.
- **`32aefcc`.** `PREPRINT-v1_0-draft.md` has sha256 `5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467`. Its parent's blob is `45b67246f2b2bcb40774e95462ad4e3c5f559fdd0358387cceec0155bebe7a41`. The diff adds the banner line and one blank line.
- **`0a3f925`.** The three 2026-10-22 SVGs hash to:
  - F1a `f0c1cd73e474eff54f11dd677a9b8e385ebae1e63cd667babc88d83123985bfc`
  - F1b `640c13e87b161dc8c14e2813acba1dc6a09b94d7beb5b9d1784cfe34371633af`
  - F2 `0e0459cf628ee7adef2d8c462a1b6c854d3a87a9743baa4f18b44134fbf969bc`

  These match block :11's prefixes and suffixes. `2026-10-22_figure-checksums.md` is in no local ref and not on disk, so Code checked against block :11 only.
- **`f5a580d`.** It deletes exactly the eight `HANDOFF-2026-08-20 … 09-12.md` files and `DESIGN-to-CODE-PROPOSAL-m-v1.2-decisions.md`, and edits `README.md` (13 lines added, 5 removed).
- **Block §2 item 3, early.** `jlens-qwen36/.venv/bin/python -E -s -m valence_core.regression.analysis` prints `154/154 reproduced through valence_core` at `2fb0cf0`. It is re-run at the release commit.
- **Block §2 item 5's grep, early.** No script in `scripts/` or `valence_core/` opens any of the nine removed paths from the working tree. The hits fall into five groups:
  - pinned reads at `bbc9ffe`: N10's `git show` of `HANDOFF-2026-08-22.md`, and N2vi's `git grep` that reaches `HANDOFF-2026-08-25.md`;
  - the N12 scripts, which read history objects;
  - names only;
  - comments;
  - one working-tree glob, `scripts/audit_note_preflight.py:60` (with :138–158), which hashes the first sorted match of `HANDOFF-*.md`. Today that first match is an untracked design-seat handoff. The preflight is not in this block, so it should not be re-run as written.

  The commands and the hit list go into item 5's raw.
- **Refs on origin.** Besides `HEAD`, `main` and the three tags, origin holds one ref and no `wip/*`, `main-*` or `claude/*` head. Code's untracked STOP raw (`results/raw/2026-10-27_note-code-to-PI_STOP-teleport-ref.md`) describes that ref. Code put the STOP to the PI in chat on 2026-10-27; it is not repeated here.

## 1. Posting day (the PI's)

**N1 round 11 cannot be done at round 10's standard today.** Code estimates at least a full day and likely two to three, plus the time the rulings in §4 take. The reasons:

- **Little of v0.6 carries over.**
  - v0.7 (the PI-redraft merge, made before passes 18–19) keeps only 36 of its 105 digit-bearing lines verbatim from v0.6. Code counted lines matching `[0-9]`, verbatim meaning the identical line appears anywhere in v0.6.
  - Passes 18–19 (block :37) then reformat every statistic in v0.8 on top of that.
  - Round 10's base was 970 note rows and 304 render rows (`results/raw/2026-10-12_note-N1-v0_6-note-rows.json`). Round 11 is close to a full remap of the note rows, an estimate Code cannot firm up until v0.8 lands.
- **v0.8 cites sources N1 has no way to admit yet** (§4).
- **Earlier rounds, for scale.** Elapsed time from the previous ledger commit to each round's ledger commit was about 16 hours for round 8 (`ef5c446`→`fd2b136`), about 20 for round 9 (`fd2b136`→`fa1b41e`) and about 25 for round 10 (`fa1b41e`→`c18854f`). Those windows include overnight gaps and other work; they are elapsed time, not effort.

**Code's recommendation:** use the block's fallback (block :51). Post today with the "will be released within N days" paragraph, and flip when the block completes. The rest of this file assumes the block runs over the next days.

## 2. Ref hygiene before any N12 run (the PI's word: these delete local refs)

- **The prune.** `git fetch --prune origin` drops the laptop's remote-tracking refs for the five branches deleted on origin. Two of them, `origin/wip/cloud-handoff-2026-10-18` and `origin/wip/step16-review-scratch`, share no history with `bbc9ffe`: `git merge-base` returns nothing. On those two the history script stops before it writes ("cannot place …").
- **The local branch.** `wip/cloud-handoff-2026-10-15` (`f885957`) is the last local ref to a deleted branch once the prune has run. While it exists, every `--all` scan reads its 475 added `wip/` paths (455 scratch files, 19 memory files, one README). The content screen would screen them and write masked excerpts of up to 40 characters of any hits into the release JSON, which becomes public.
- **What deleting loses.** After deletion, no ref or reflog holds `f885957`. The object stays until a `git gc` prunes it: the default is two weeks by object age, so from about 2026-10-29.

**Recommendation:** Code runs the prune. On the PI's word, Code first writes a bundle of `f885957` to a path outside the repository, then deletes the local branch.

## 3. N12 re-runs (block §2 item 1): rulings the scripts need

The five scripts v1's `e8fb54d` touched (content, gitleaks, history, licenses, scrub) need dated output names and their release constants re-pinned, in one "N12 scripts for the release run" commit, as at v1. The password script takes `--out` and needs no edit. Those edits are Code's. The points below are not.

**3a. The (i) line.**
- The history script prints the PI's basis for (i) verbatim. In v1 that basis was the answer of 2026-10-12, "Yes to all five; tag it", which carried ruling 4 of 2026-10-09 to the release run. Printing it on a 2026-10-27 run would misattribute it.
- *The PI's words are needed.* Code proposes the question: "Does ruling 4 cover this release run's (i), as it covered v1's?"
- Without an answer, the raw records (i) as a STOP.

**3b. Gitleaks: the paths it must be told about.**
- **Attribute paths.** Four new paths carry `-diff`: `data/m/ckpt/Q-F0_{time,id,qual,campaign}.json` (`git check-attr` reads `unset`). The script's history scan already reads every path as text (`--text`), and it stops on any `-diff` path not on its list; its comment reserves each addition to the PI and the seat. The blinding reason for `-diff` (m:318) was "before VERDICTS", and VERDICTS ran on 2026-10-19. **Recommendation:** list the four. That clears the STOP; it accepts a read that already happens.
- **Skipped paths.** The three 2026-10-22 SVGs fall under gitleaks' default `.svg` skip. The skip list holds only the 2026-10-10 renders and `figures/fig1_inverted_u.png`, on the basis of the PI's answer of 2026-10-12, question 4, and any skipped path not listed is a STOP. **Recommendation:** add the three on that basis.

**3c. C2PA.**
- Each 2026-10-22 render carries one `<c2pa:manifest>` element, 7,684 characters each.
- The history script's declaration (its round 9) covers the 2026-10-10 renders only. N1 rounds 9–10 exclude the element by a separate mechanism.
- Without an extension, the history raw labels the three elements "undeclared". That is not a STOP.
- **Recommendation:** extend the declaration to the three.

**3d. Licenses classes.** These are predicted from a re-implementation of the script's matchers; the run will confirm them. The licenses run prints "(iv) NOT recorded" unless it has:
- a class for `jasondwyer/told-vs-felt`: "this repository, renamed from jasondwyer/jspace-lab". The old entry stays.
- classes for two Qwen ids at today's refs, or three after §2's prune:
  - `mlx-community/Qwen3.6-27B-8bit` (`results/raw/2026-10-13_m-gid-driver_review.txt:471`);
  - a digit-masked `mlx-community/Qwen…` (`results/raw/2026-10-18_m-campaign-qf0_launchchecks.txt:2678`);
  - after the prune, a cache path in `results/raw/2026-10-13_m-gid-driver_review.txt:393`.

  Code reads each line before writing a class.
- a rule for `claude.ai/admin-settings/usage`, which is linked eight times in `results/raw/2026-10-18_m-campaign-driver_review.txt` (lines 4582–4585, 4806, 4827, 4846, 4865).

The script's docstring (:81–82) reserves new rules to the PI. The rows themselves are labelled "Code to review", except `told-vs-felt`, which is labelled "for the PI". **Recommendation:** yes to all three.

**3e. The decisions file and the content screen.**
- Block :29 says the file was "excluded by name from the content runs". The content script has no name exclusion; its scope (tracked `results/raw/` and `HANDOFF-*.md`) never held the file.
- The exclusions by name are the history script's, which covers working-tree reads, and the scrub generator's, which covers names only. Neither touches history blobs.
- At v2 the file is a history-only path. The content screen therefore reads its blob at `f5a580d^1` and may write masked excerpts of any hits.
- Options: (a) screen it, and have the scrub index say so, since it is in the public history either way; or (b) add a name filter, which gives the script a new sha.
- **Recommendation:** (a), with the scrub index's D4 census sentence reworded to match.

**3f. The password search, part (4).**
- Part (4) reads every untracked, not-ignored file, the six design-seat handoffs among them, and lists the file names and line numbers of hits, as v1's release raw did. This is how the scan shows where the value sits off the record.
- **Recommendation:** keep it, and say so in the scrub index. v1's housekeeping line ("never opened") reads wider than what v1 actually did.

**3g. Coverage after item 1.**
- The block lists N12 first (block :27–29) and says "at the release commit". In v1 the release commit was the tag commit. The PI's routing of 2026-10-27 in chat lists "N12 re-runs" among the work to start before v0.8 lands.
- Raws committed at item 1 cannot cover v0.8, items 2–6 or the tag.
- **Recommendation:** run item 1 as the block orders. At the tag commit, before the push, re-run the password search and gitleaks outside the repository and record their counts in the post-tag raw. The PI supplies the word twice. The seat confirms or reorders.

**3h. The scrub index.** Recommendations:
- Regenerate `results/raw/2026-10-08_note-N12-scrub.md` in place. v1 created it and regenerated it in place three times (four commits); v1's form stays at `98d07bc` and the tag.
- Put the v2 checklist in a new §14. The generator asserts §10's items 1–7 as v1's record.
- State the D4 census as block :29 asks, computed from history: the decisions file was added at `5dca58b` (2026-10-14), after `11cc35b`, and removed at `f5a580d`.

## 4. N1 round 11 (block §2 item 2): rulings needed before the mapping starts

**4a. The A0 figures** (79/80, +0.4875, 0.0625, 81/2⁸⁰).
- Carriers: `RESULTS.md@0fa8539` carries all four, and is the only carrier of 81/2⁸⁰. `results/raw/2026-10-19_m-verdicts-qf0.txt@bfc179c` and `data/m/verdicts/Q-F0_VERDICTS.json@bfc179c` carry the other three.
- All of them postdate N1's record pin `bbc9ffe`, and none matches a pin class, so N1 cannot admit them.
- Either route below is a script change that must leave v0.3–v0.6 reproducing:
  - (a) a later-record class naming those commits;
  - (b) treat the verdicts raw as an audit-outcome raw: a pin class plus an outcome-raw entry. The fields that cite an outcome raw must then be printable ASCII, a rule that binds the citing fields, not the note text.
- **Recommendation:** (a).

**4b. N2(vii)** (`results/raw/2026-10-22_note-N2vii-macar-v5.md@8d68b0b`).
- Its date falls outside N1's item-raw pattern (which admits 2026-10-08/09 only), so N1 never reads a status from it.
- Its rows can be computed-new by mapping and pass under ruling 5, but only after a pin class for `8d68b0b` is added. That is the same kind of script change as 4a(a).
- Its figures are present in it: +9.8 ± 0.5, *L* = 25, α = 4, 500 concepts.
- Confirm.

**4c. Pass 12, author correspondence of 2026-10-26.**
- No committed source carries these figures except the block itself (block :33). 1,684 is also in the v0.3 final ledger.
- Options:
  - (i) admit the block as the carrier;
  - (ii) commit a transcription of the figures;
  - (iii) a new ruling admitting the correspondence as a cited source. Ruling 8's machinery caps at nine units, in note spans only, so this needs its own table.
  - (iv) leave them "not found" until T+3 re-sources them to the v2 tables (block :52).
- Code's reading is that the correspondence may be private. The PI's call.

**4d. Pass 13b, the v2 PDF "in the project".**
- It is not in the repository.
- **Recommendation:** before the mapping, commit a transcription raw of the lines the note cites, modelled on N2(vii)'s raw. Otherwise a ruling.

**4e. The 10-23 handoff's list.**
- The handoff is absent from this laptop and from every local ref. Block :31 names its list as categories: every A0 figure; the restored figures; N2(vii)'s; Rodd-Henricks 2002 and Nosek 2018; F2's caption clause.
- "The restored figures" is enumerated in no committed file.
- N1 takes the additions by source from block :31–:38. **The seat enumerates "the restored figures" and "every A0 figure."**

**4f. Rulings 7, 8, 11, 12 and R1** are declared differently, so each re-keys differently:
- rulings 7, 8 and 11 carry verbatim quotes of v0.6;
- ruling 12 is keyed by line or SVG node and the unit "fifty";
- R1 is keyed by row.

Passes 18–19 may have changed the quoted text. Code re-keys a ruling where it still applies verbatim in v0.8, and brings each changed one to the PI. One is already flagged: ruling 12's F2 "fifty" sits in the replaced caption block, beside "v5 gives 50 concepts".

**4g. The former ‖‖(c) (the struck what-if).** Its rows retire, and v0.6 and its ledger at `note-2026-10-v1` stay their record (block :38). v0.8's ‖‖(c) is the former (d), whose rows carry over.

## 5. The preprint and Tier 1 (the PI's)

Six Tier-1 scripts assert patch v7's sha256 `d9635ca2…1fe6` and refuse any other text: N4 :87, N5 :162, N6 :103, N7 :107, N8 :139, N17 :88. At the v2 tag they refuse the bannered preprint, and README-NOTE §3 tells a reader they read patch v7. The options:
- (a) re-point the six scripts to `5d677a72…4467`, re-anchor their line needles to the v8 text, and re-run them, as round 10 did for v7 at `d6bb790`;
- (b) state at the tag that Tier 1 reads patch v7, which `note-2026-10-v1` holds.

**Recommendation:** (b). The banner says the file "is not a text of record".

## 6. Order inside §2 (Code's reading, for the seat)

- **N18.** N18 (item 4) hashes `README-NOTE.md`, every `results/raw/*_note-*` and every `scripts/audit_note_*.py`, and its own re-run rule puts it last. Items 5 and 6 change those files. **Proposed:** run N18 at item 4 as the block orders, and re-run it as the last commit before the tag.
- **The pre-flip read.** Item 6 expects `note-2026-10-v2` on origin, but item 7 places the tag after item 6. **Proposed**, following v1's planned order (README-NOTE §8: the pre-flip read comes just before the flip):
  1. the preflip-script commit;
  2. tag `note-2026-10-v2` on the final audit commit;
  3. push;
  4. the pre-flip read, with its raw committed after the tag;
  5. the PI flips.
- **Untracked raws.** Two untracked files sit under `results/raw/`: the 2026-10-26 design block and Code's STOP raw. N18 lists them and the licenses run reads them. The PI commits or moves each one before N18 runs.

## 7. POST-note

No file of that name is in the repository or its history. Where does it live, and is its refresh (block :47) Code's to make?
