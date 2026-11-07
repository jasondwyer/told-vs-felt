# N1: the preprint's bytes of record restored, its status banner moved to a sidecar (2026-11-07)

*Code's raw, PI date 2026-11-07. This is the change the seat ruled for G-ANL-F3's N1 FLAG (`e0b4f2c`), which had left the fix open.*

- **The ruling:** the seat's answers of 2026-11-07, §7, N1 (`results/raw/2026-11-07_p-preread_design-to-code_answers.md:46`, committed at `139635f`).
- **Its amendment:** the seat's answer to Code's STOP (`results/raw/2026-11-07_n1-battery_design-to-code_answers.md`, committed at `f105bdd`).
- **The PI's routing:**
  - item 2 of 2026-11-07, verbatim: "N1: restore the preprint’s bytes of record, banner to `PREPRINT-v1_0-draft.STATUS.md`, N18’s constants and README-NOTE:78 updated [go]";
  - after the STOP: "2. N18’s sidecar case [confirmed]; README-NOTE:214 fixed with N1; gitleaks pin left [confirmed]."
- **The scope:** one commit holding four changed files, `PREPRINT-v1_0-draft.md`, `PREPRINT-v1_0-draft.STATUS.md` (new), `scripts/audit_note_N18.py` and `README-NOTE.md`, together with this raw, its values-check raw and the entry. The tag `note-2026-10-v2` is untouched.

## 0. Why N1 was held, and how it was resolved

- **The conflict.** Restoring the bytes of record would have failed G-ANL-F3's battery check `F3R-PREPRINT-OF-RECORD` (`scripts/m_analyze.py:9983–9986` at blob `6ec3222b…`). Its condition asserted that the working-tree file is *not* the bytes of record, which is true only under the banner.
  - After N1 the battery would not pass, `--selftest` would exit 1, and `ganl` would write nothing. These are consequences read from the code (`m_analyze.py@f105bdd:11299`; `:11108–11111`), not logged runs.
  - The seat had read `:9984`, the check's label, as prose.
  - The F3 session found the conflict, and this change's first blind values-check found it again independently.
- **The STOP.** Code held N1 and sent a STOP (`9838664`).
- **The seat's answer, routed by the PI.** Order (b): fix the check in place before LOCK-m-F3 v0.1, so that it asserts only that the regression is served by the blob of record and reports HEAD's sha256. Two prose anchors are reworded in the same edit. N1 follows that fix and precedes the canonical `ganl`, so that `G-ANL-F3.json` records the restored tree.
- **The fix** is the F3 session's commit **`10a2bbb`**, and this commit follows it.

## 1. `PREPRINT-v1_0-draft.md`

- **Before.** The file at HEAD is `32aefcc`'s blob: sha256 `5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467`, 89,267 bytes, 470 lines. `32aefcc` is the only commit that touched the file after `1523cce`.
- **After.** The file is restored from `1523cce`'s blob: sha256 `45b67246f2b2bcb40774e95462ad4e3c5f559fdd0358387cceec0155bebe7a41`, 88,668 bytes, 468 lines.
  - It is byte for byte `32aefcc`'s parent blob.
  - The diff removes exactly the two lines `32aefcc` added, the banner line and a blank line: 599 bytes.
- **What binds these bytes:** `LOCK-m-F0.md:29`, `:204` and `:414`, and the table of record (`data/m/gates/m_posting_sentences.json:42`).

## 2. The sidecar `PREPRINT-v1_0-draft.STATUS.md`

The file is new: 892 bytes, sha256 `6277f6f483dfe8c8a0b9b191b0b69f79bdd8c3b2cf9d278aa60c30224adf4626`.

- **Its first 599 bytes are `32aefcc`'s banner, byte for byte.** That is the line and the blank line after it, taken from the banner commit as the bytes its blob has beyond its parent's.
- **One sentence is added,** as the ruling asks:

  > This text was the banner at the head of `PREPRINT-v1_0-draft.md` (from `32aefcc`) and moved here verbatim on 2026-11-07, because the table of record and `LOCK-m-F0.md` bind that file's bytes (sha256 `45b67246…7a41`), as G-ANL-F3's N1 found; "this file" in it means `PREPRINT-v1_0-draft.md`.

## 3. `scripts/audit_note_N18.py`: the sidecar form, Code's reading, confirmed by the seat

- **The ruling's words.** It said "`PREPRINT_ROUTED`/`PREPRINT_BANNER` … updated in the same commit to the sidecar form".
- **Code's reading, put to the seat at `9838664` and confirmed at `f105bdd`.** Both constants keep the tag's values (`5d677a72…4467`; `32aefcc`, `45b67246…7a41`), because both stay true of the tag.
  - The release block quotes `PREPRINT_ROUTED` on its lines 10 and 40, and N18's `SOURCES` assert those quotes. Giving it the restored value would make N18 contradict its own sources.
  - The banner check reads `32aefcc` and its parent from history, not from the disk.
- **What is added.** The audit's purpose, the file labelled not a text of record, is now served by the sidecar.
  - A constant, `PREPRINT_STATUS = "PREPRINT-v1_0-draft.STATUS.md"`.
  - An on-disk case: a file equal to the banner commit's parent blob is the sidecar form. It is accepted only without `--preprint-pi-confirmed`, and only if `PREPRINT_STATUS` begins with the banner's bytes.
  - The manifest records the sidecar's path, sha256 and bytes.
  - A docstring paragraph (round 6) states all of this.
  - The edit is 34 lines added and none removed.
- **Tests, run on this commit's final bytes in a scratch worktree at `10a2bbb`** (the shared tree and the committed manifest untouched):
  - **Positive.** No `--preprint-pi-confirmed`: exit 0. The run's manifest hashes the final README-NOTE.md (sha256 `3f2f394c…`), so the test covers all four changed files. The manifest's `preprint` section, abridged to its status keys and three of `banner`'s eight:

    ```
    status : "patch v8 at its bytes of record, the banner commit's parent blob, restored after the tag on the design seat's ruling of 2026-11-07 (G-ANL-F3's N1): the table of record and LOCK-m-F0 bind these bytes; the banner's text, verbatim, heads PREPRINT-v1_0-draft.STATUS.md, so the file stays labelled not a text of record; the tag holds the bannered file, sha256 5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467"
    sha256 : "45b67246f2b2bcb40774e95462ad4e3c5f559fdd0358387cceec0155bebe7a41"
    pi_confirmation : null
    status_sidecar : {"path": "PREPRINT-v1_0-draft.STATUS.md", "sha256": "6277f6f483dfe8c8a0b9b191b0b69f79bdd8c3b2cf9d278aa60c30224adf4626", "bytes": 892, "begins_with_banner_verbatim": true}
    tracked_at_head : true
    equal_to_banner_commit_blob : false
    banner (3 of 8 keys) : {"commit": "32aefcc", "parent_sha256": "45b67246f2b2bcb40774e95462ad4e3c5f559fdd0358387cceec0155bebe7a41", "banner_bytes": 599}
    ```

    N18's wait check only records the files' modification dates (it stops on a missing file only).
  - **Negative.** `--preprint-pi-confirmed 5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467`, the tag's routed value: STOP, exit 2, nothing written:

    ```
    STOP: --preprint-pi-confirmed 5d677a724652c418963ae835c27e72fa3d22416dc9f2001f4e414acbd9634467 is the tag's routed value, but PREPRINT-v1_0-draft.md on disk is its bytes of record, the banner commit's parent blob (round 6's sidecar form)
    ```
  - **The analyzer's battery on the same tree.** `scripts/m_analyze.py --selftest`, run with the project's venv and `-B`: **525/525**, and every one of the 538 coverage ids reached. `F3R-PREPRINT-OF-RECORD` passes and reports `('45b67246f2b2bcb4', '45b67246f2b2bcb4', True)`: the blob of record, the tree's file, and the tree's file being the table's.

## 4. `README-NOTE.md`, lines 78 and 214

- **`:78`.** The line's first sentence describes the file in the tree, and it changes to the sidecar form. The rest of the line, which describes Tier 1's scripts and the tag, is unchanged and still true.
  - Before:

    > - `PREPRINT-v1_0-draft.md`, tracked since v1's tag commit (`98d07bc`, patch v7), at patch v8 since `1523cce`, and under a status banner since `32aefcc` (sha256 `5d677a72…4467`, as N18 records it, the file at the v2 tag), which is not a text of record, as its banner says (§8).

  - After:

    > - `PREPRINT-v1_0-draft.md`, tracked since v1's tag commit (`98d07bc`, patch v7) and at patch v8 since `1523cce`. From `32aefcc` it carried a status banner (sha256 `5d677a72…4467`, as N18 records it, the file at the v2 tag). Since 2026-11-07 it is back at patch v8's bytes of record (`45b67246…7a41`), which the table of record and `LOCK-m-F0.md` bind, and the banner's text, verbatim, is in `PREPRINT-v1_0-draft.STATUS.md` beside it. It is not a text of record, as the banner says (§8).

  - Its `src` comment gains two sources at its head: `results/raw/2026-11-07_p-preread_design-to-code_answers.md@139635f:46` and `PREPRINT-v1_0-draft.STATUS.md:1,3`.
- **`:214`, as the seat's answer §3 rules: fixed in this commit, with the tag-time reference kept in a parenthesis.**
  - "as patch v8's :264 does beneath its banner, which is not a text of record (§3)." becomes "as patch v8's :262 does (:264 under the banner at the tag), which is not a text of record (§3)."
  - Its `src` comment gains `PREPRINT-v1_0-draft.md@1523cce:262`, beside the kept `@32aefcc:1,264`.
  - Line 262 of `1523cce`'s blob carries both quoted phrases.

## 5. Dated notes (2026-11-07)

- **N1-a.** The ruling's three anchors in `scripts/m_analyze.py` (`:4480`, `:4676`, `:9984`, at `139635f:46`), and the comment Code added at the STOP (`:9871–9872`, `9838664` §1), were, by construct:
  - `:4480–4481`, PIN-V2-11's register text;
  - `:4676`, PIN-17's text about the preprint of record, not about the bannered HEAD;
  - `:9871–9872`, a comment;
  - `:9983–9986`, the battery check `F3R-PREPRINT-OF-RECORD`, the ruling's ":9984".

  The seat's answer adopted the comment as the second prose anchor (`f105bdd` §0–§1). `10a2bbb` rewords the two prose anchors and fixes the check (§0). This commit does not touch the analyzer.
- **N1-b.** `scripts/audit_note_N12_gitleaks.py:146`'s `RELEASE` list keeps the v2 tag's preprint, `5d677a72…4467`, as "the sha256 each must have". This is the v2 release's record at the tag, which still holds those files, and it is left as the seat confirmed. A run of that script at HEAD would find the restored file.
- **N1-c.** `README-NOTE.md`'s lines 242–243 and 254 describe the tag's N18 run and the v2 release with `5d677a72…4467`. They stay true of the tag and are not changed.
- **N1-d.** The tag `note-2026-10-v2` is untouched, and N18's record at the tag stands.
- **N1-e.** Two points noted against N18's output and left, since the seat confirmed the case as built:
  - N18's manifest field `round` still reads 5 (`scripts/audit_note_N18.py:692`).
  - In the sidecar case, the `rerun_trigger` and `routing` texts keep their pre-tag wording.
  - N18's .md rendering ends its banner sentence "The file on disk equals that blob: NO." right after naming the parent's blob (`45b67246…`). The file does equal that blob; the flag compares the file against the banner commit's blob, so in the sidecar case the line reads as false. The rendering also omits the sidecar.
