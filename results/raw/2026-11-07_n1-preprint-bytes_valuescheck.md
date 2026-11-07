# N1: blind values-checks of the raw, the entry and the change, with Code's dispositions (2026-11-07)

*Two blind checks ran before the commit, each by a fresh agent with no part in the drafting:*

1. *the first, on the first drafts and the change in the shared tree (38 items), before N1 was held;*
2. *the second, on the revised drafts and the change applied in a scratch worktree at `10a2bbb` (43 items).*

*Both reports follow verbatim, with local paths replaced by `<scratch>`, `<repo>` or `<tmp>`. Code's dispositions follow each report.*

---

## Check 1

# Blind values-check — N1 (preprint bytes restored, banner to sidecar), 2026-11-07

Checked: RAW `results/raw/2026-11-07_n1-preprint-bytes.md` (untracked), ENTRY `scratchpad/n1_test/entry_draft.md`, the working-tree change at HEAD `139635f`. Read-only; the only command run besides git/hash/read was the permitted negative N18 re-run (`--out …/n1_test/neg2/manifest.json`), which wrote nothing (`neg2/` not created; `git status --porcelain` identical before/after).

1. **"the change that G-ANL-F3's N1 FLAG (`e0b4f2c`) called for"** — RAW:3. **IMPRECISE.** The FLAG raised the condition and left the fix open ("No analyzer change is made for it; the fix is the seat's or the PI's call", RESULTS.md@e0b4f2c:62–69). The change is the seat's ruling (answers §7 N1).
2. **Ruling: answers of 2026-11-07, §7, N1, `…answers.md:46`, committed at `139635f`** — RAW:5, ENTRY:1–2. **PASS.** The file was added at 139635f, its sha256 is `ab40f470…b08b` (= RESULTS.md@139635f:77), and N1's paragraph is :46.
3. **PI routing item 2, verbatim** — RAW:6, ENTRY:11–12. **PASS.** Byte-equal to RESULTS.md@139635f:82, curly apostrophes included.
4. **"one commit with four files"** — RAW:7 vs ENTRY:40–42. **IMPRECISE (RAW–ENTRY).** ENTRY's "Committed by path" names 7 paths: the 4 changed files, the raw, the values-check raw and RESULTS.md. "Four" counts only the change's files.
5. **"Nothing in it moves a hash that a lock names"** — RAW:7. **PASS (literal).**
   - LOCK-g, LOCK-h and LOCK-m-F0 name none of these: README-NOTE (`de4fffa2…`), N18 (`561659f4…`), `5d677a72…`, the STATUS file.
   - The preprint moves *to* LOCK-m-F0's `45b67246…`.
   - valence_core/m and the closure inputs are untouched.
   - See item 33 for the downstream analyzer effect.
6. **Tag `note-2026-10-v2` untouched; N18's record there stands** — RAW:7, :81; ENTRY:7, :38. **PASS.**
   - Tag object `e6049b7` points to `6d8c237`, whose preprint blob is `dd4524c` (`5d677a72…`).
   - `results/raw/2026-10-09_note-release-manifest.*` are unmodified.
7. **Before: HEAD = `32aefcc`'s blob, `5d677a72…4467`, 89,267 B, 470 lines** — RAW:11, ENTRY:15. **PASS.** Blob `dd4524c` at both HEAD and 32aefcc; sha256 full match; `wc -c`/`wc -l`.
8. **"`32aefcc` is the only commit that touched the file after `1523cce`"** — RAW:11. **PASS.** `git log --full-history 1523cce..HEAD --` gives 32aefcc only, with no merges in the range. The full history is 98d07bc, 1523cce, 32aefcc.
9. **After: `1523cce`'s blob, `45b67246…7a41`, 88,668 B, 468 lines, byte for byte `32aefcc`'s parent blob** — RAW:12–13, ENTRY:16. **PASS.** 32aefcc^ = f5a580d. Its blob = 1523cce's blob = `e2123f2` = the disk file's hash-object, and `cmp` finds them identical.
10. **Diff removes exactly the banner line + blank line, 599 bytes** — RAW:14, ENTRY:17. **PASS.**
    - numstat 0/2 for the preprint; 89,267 − 88,668 = 599.
    - The 32aefcc blob = a 599-byte prefix (2 lines, ending `\n\n`) + the parent blob.
11. **Binding: LOCK-m-F0.md:29, :204, :414; m_posting_sentences.json:42** — RAW:15. **PASS.**
    - Each line carries the full `45b67246…7a41`: :29 is in the PI's quoted "Placed" message, :204 is the preprint-of-record line, :414 is the Binds table.
    - json:42 is preprint.sha256, with bytes 88668 at :39 and lines 468 at :40.
    - LOCK-m-F0 has exactly 3 occurrences.
12. **Sidecar: 892 bytes, sha256 `6277f6f4…4626`** — RAW:19, ENTRY:18. **PASS.**
13. **Sidecar's first 599 bytes = `32aefcc`'s added bytes (line + blank line)** — RAW:21, ENTRY:18. **PASS.** `side[:599] == ban[:len(ban)-len(par)]`.
14. **One added sentence, as the ruling asks; quote verbatim** — RAW:22–24, ENTRY:19–20. **PASS.**
    - The quote is byte-equal to sidecar line 3 (292 B + LF = the remaining 293 B).
    - It carries the ruling's content: moved because the table of record and LOCK-m-F0 bind the file's bytes, found by G-ANL-F3's N1.
    - Within the one sentence it adds the date, the sha and a gloss on "this file".
15. **`PREPRINT_ROUTED` (`5d677a72…4467`) and `PREPRINT_BANNER` (`32aefcc`, `45b67246…7a41`) keep their values; both true of the tag** — RAW:28, ENTRY:22. **PASS.** N18:218–219 are unchanged. The tag's blob is `5d677a72…` and 32aefcc^ is `45b67246…`.
16. **Section title "updated to the sidecar form" vs the ruling's words** — RAW §3, ENTRY:21–26. **IMPRECISE.**
    - The ruling (answers:46) says "`PREPRINT_ROUTED`/`PREPRINT_BANNER` … updated in the same commit to the sidecar form"; the routing says "N18's constants … updated".
    - The two named constants are not changed; a new constant and a new case serve the form.
    - The reason given is true (items 17–18), but the raw states it as done rather than marking it as Code's reading of the ruling's words for the seat to confirm.
17. **Release block quotes `PREPRINT_ROUTED` on its :10 and :40; N18's `SOURCES` assert those quotes; changing it would contradict them** — RAW:29, :31; ENTRY:22–23. **PASS.**
    - RB = `…release-block.md@2fb0cf0`. Both :10 and :40 carry the full 64-hex value.
    - SOURCES N18:239–240 ("post-banner `%s`") and :244 ("--preprint-pi-confirmed %s") interpolate PREPRINT_ROUTED. Any other value STOPs with "does not carry".
    - `need(ban_sha == PREPRINT_ROUTED)` at :542 would also STOP.
18. **Banner check reads `32aefcc` and its parent from history** — RAW:30, ENTRY:23. **PASS.** `git show 32aefcc:` and `32aefcc^:` at N18:539–540.
19. **New `PREPRINT_STATUS`; on-disk case accepted only without `--preprint-pi-confirmed` and only if the sidecar begins with the banner's bytes; manifest records path, sha256, bytes** — RAW:33–35, ENTRY:24–26. **PASS.**
    - N18:223 defines the constant.
    - The case at :563–583 is `ps == par_sha`, then `pconf is None`, then the sidecar is on disk, then `side.startswith(banner prefix)`.
    - The JSON gets `status_sidecar` {path, sha256, bytes, begins_with_banner_verbatim}.
    - (The .md render, :859–877, prints none of the sidecar fields.)
20. **Docstring paragraph (round 6) states all of this** — RAW:36. **PASS.** N18:124–131: the binding, the move, the tag, why the two constants stay, both acceptance conditions, the record.
21. **34 lines added, none removed** — RAW:37, ENTRY:21. **PASS.** numstat 34/0 (9 + 4 + 21).
22. **Logic of the new case** (requested check). **PASS.**
    - It is reached only when the on-disk sha256 equals 32aefcc^'s blob, which cannot coincide with PREPRINT_REF `d6431e97…` or `ban_sha`.
    - With `pconf` it STOPs, as the old `elif pconf is not None` branch would have (`pconf == ps` fails); only the message differs. The top-level check guarantees `pconf == PREPRINT_ROUTED`, so "is the tag's routed value" is right.
    - The `else` branch is unchanged and still reached for every other state.
    - `tracked_at_head` and `equal_to_banner_commit_blob` are still set after the chain (false here, correctly).
    - See the observations for wording issues.
23. **Positive test: no confirmation, scratch `--out`, exit 0, sidecar case taken, committed manifest untouched** — RAW:38, ENTRY:27. **PASS.**
    - The manifest's `command` field confirms the flags; `status_sidecar` is present.
    - Exit 0 is inferred: run.txt shows "0 re-hash mismatches", and `main` returns 0 then.
    - script_sha256 `559c4576…` = the working-tree N18.
24. **"The manifest's `preprint` section reads:"** — RAW:38–48. **IMPRECISE.**
    - Every quoted value is exact.
    - The block shows 7 of the section's 12 keys: path, on_disk_matches_block_reference, block_reference, routing and rerun_trigger are omitted.
    - It shows 3 of `banner`'s 8 keys.
    - There is no ellipsis or "in part".
25. **"The run's other sections are as N18 finds the tree today."** — RAW:50. **IMPRECISE.**
    - The run (code_stamp 18:36:20 UTC) came before README-NOTE.md's edit (mtime 18:37:19 UTC).
    - Its files section records README-NOTE.md at HEAD's `de4fffa2…` (208,362 B), not the change's `0414dd9c…` (208,902 B).
    - So the positive test covers 3 of the 4 files in their final state.
26. **"Its wait check records the files modified today and stops on nothing."** — RAW:50. **IMPRECISE.**
    - All four WAIT_FILES recorded `modified_today: false`; README-NOTE.md's mtime was then 2026-11-05T01:08:55Z.
    - The check cannot stop except on a missing file (N18:620–632).
    - A re-run on the final tree would record README-NOTE.md as modified today.
27. **Negative test: tag's value, exit 2, nothing written, STOP line verbatim** — RAW:51–55, ENTRY:27–28. **PASS.** The re-run printed the identical line and exited 2. Nothing was written (`neg2/` absent) and `git status` was unchanged.
28. **README-NOTE.md:78 before/after quotes** — RAW:61–67. **PASS.**
    - Only line 78 differs (255 lines in both).
    - Before is a prefix of HEAD:78; after is a prefix of WT:78; the prose after each is identical.
29. **"The rest of the line describes the tag" / "the tag's account"** — RAW:59, ENTRY:29–30. **IMPRECISE (minor).** The rest describes Tier 1's six scripts:
    - patch v7 at note-2026-10-v1;
    - their refusal of the bannered file at the v2 tag;
    - N8's exits;
    - the clone reads;
    - N2/N9/N10/N14's checked reads.

    It is unchanged and still true at HEAD.
30. **src gains two sources at its head; well formed** — RAW:69–71, ENTRY:29. **PASS.**
    - new src = `<!-- src: ` + the two items + the old src verbatim.
    - `@139635f:46` checks out. STATUS:1 is the banner and :3 the sentence.
    - Note: the STATUS cite is unpinned (the file is added in the same commit). README-NOTE.md:254's `README.md:3` is the one other unpinned file:line cite.
31. **"N18 accepts and records that sidecar form, and README-NOTE.md:78 says so."** — ENTRY:6. **IMPRECISE.** README-NOTE.md:78 describes the restored file and the sidecar; it says nothing of N18's sidecar case.
32. **N1-a anchors: "three message texts that describe the bannered HEAD (`:4480`, `:4676`, `:9984`)"** — RAW:75, ENTRY:32–33. **IMPRECISE.**
    - :4480–4481 (PIN-V2-11) and :9984 do describe the bannered HEAD.
    - :4676 is PIN-17 ("re-verified against the placed preprint … (sha256 45b67246…7a41), before LOCK v1.0"), which does not.
    - The remaining bannered-HEAD text is the comment at :9871–9872.
    - The anchors are the seat's, repeated. m_analyze.py is unchanged (`6ec3222b…93d9`), which holds.
33. **N1-a: they "stay as they are … editing them would move the analyzer for prose"** — RAW:75, ENTRY:32–33. **FAIL.**
    - :9984 is the label of battery check F3R-PREPRINT-OF-RECORD (m_analyze.py:9983–9986), not prose only.
    - Its condition requires `head_file_sha256 not in (None, table_sha256)`, where head_file is the working-tree preprint (:9892–9895).
    - With the analyzer's own inputs (the table, 1523cce's blob, the disk file), the condition is True with HEAD's bannered file and **False with N1's tree**.
    - After N1 the check fails and its coverage id goes unreached, so the battery reads 523/525 (it was 525/525 at e0b4f2c; the check PASSed at selftest raw :463).
    - `--selftest` then exits 1, and the canonical `ganl` (routing item 1) prints "STOP: the battery did not pass; nothing written" and exits 4 (:11108–11111).
    - Avoiding this needs either an analyzer edit, which moves `6ec3222b…93d9`, or `ganl` landing before N1. Neither the RAW nor the ENTRY says so.
34. **N1-b: N12_gitleaks:146 `RELEASE` gives `5d677a72…4467` as "the sha256 each must have"; a HEAD run would find a different sha256** — RAW:76–77, ENTRY:34–36. **PASS.**
    - :146 is that entry, and the quoted phrase is the list's header comment at :142.
    - :589–595 compares both `HEAD:` blob and the working tree to `want`; after N1 both are `45b67246…`, so the row fails.
35. **N1-b: "the ruling names N18 and README-NOTE.md:78 only"** — RAW:78. **PASS.** answers:46.
36. **N1-c: README-NOTE.md:242–243 and :254 describe the tag's N18 run and the v2 release with `5d677a72…4467`; stay true** — RAW:80, ENTRY:37. **PASS.**
    - All three carry 5d677a72: :242 is the files at the tag, :243 N18's manifest, :254 the release sequence.
    - The only lines in the file carrying it are 78, 242, 243 and 254.
37. **ENTRY's link to the raw path** — ENTRY:13. **PASS.** The file exists at `results/raw/2026-11-07_n1-preprint-bytes.md`.
38. **"Not pushed … a push waits for the PI's word"** — ENTRY:41–42. **PASS.** Consistent with the ruling, which calls this "a release-surface change (README-NOTE and a public file)".

**Summary: 38 items — PASS 28, IMPRECISE 9, FAIL 1, UNVERIFIABLE 0.**

Observations (no claim; not counted):
- O1. N18's manifest `round` is hard-coded "5 (2026-11-03, N1 round 11; release v2)" (N18:692), so a manifest written by round 6's case is labelled round 5.
- O2. In the sidecar case the manifest keeps the pre-tag wording:
  - `rerun_trigger` (N18:615–618) and the `routing` text still say "If the file changes after this run and before the tag commit … the tag commit is to hold patch v8 under its status banner".
  - The .md prints "The file on disk equals that blob: NO."
  - The .md shows no sidecar sha256 or bytes.
- O3. README-NOTE.md:214's prose "patch v8's :264 does beneath its banner" uses the bannered numbering. Its src pins `PREPRINT-v1_0-draft.md@32aefcc:1,264`, but in the restored tree that line is :262. It is true of the tag, and N1-c does not list it.

### Code's dispositions, check 1

| # | verdict | disposition |
|---|---|---|
| 33 | FAIL | The battery conflict. N1 was held; Code sent the STOP (`9838664`); the seat ruled order (b) (`f105bdd`); the check was fixed in `10a2bbb`. On N1's final bytes the battery passes 525/525 (raw §3). |
| 1 | IMPRECISE | Applied: the raw's opening line names the change as the seat's ruling, the FLAG having left the fix open. |
| 4 | IMPRECISE | Applied: "one commit holding four changed files … together with this raw, its values-check raw and the entry". |
| 16 | IMPRECISE | Applied: §3 gives the constants' treatment as Code's reading, put to the seat and confirmed at `f105bdd`. |
| 24 | IMPRECISE | Applied: the manifest quote is labelled as abridged. |
| 25 | IMPRECISE | Applied: N18's positive test was re-run on the final bytes, and its manifest hashes the final README-NOTE (`3f2f394c…`). |
| 26 | IMPRECISE | Applied: the wait check "only records the files' modification dates (it stops on a missing file only)". |
| 29 | IMPRECISE | Applied: the rest of `:78` "describes Tier 1's scripts and the tag, unchanged and still true". |
| 31 | IMPRECISE | Applied: the entry says README-NOTE.md's lines 78 and 214 are updated. |
| 32 | IMPRECISE | Applied: N1-a gives the anchors by construct, with `:4676` as PIN-17's (see check 2, item 26). |
| O1–O2 | — | Carried as dated note N1-e; the seat confirmed N18's case as built. |
| O3 | — | `README-NOTE.md:214`, fixed in this commit on the seat's ruling (`f105bdd` §3). |


---

## Check 2

# N1: second values-check (the delta)

*Blind values-checker, 2026-11-07. Repository HEAD is 10a2bbb (checked at the start). The scratch worktree `wt_n1` is at 10a2bbb with the four changed files. Sources: git objects, RESULTS.md at 10a2bbb, and the run files in `n1_final/`. Read-only.*

## Items

1. **Amendment: the seat's answer to the STOP, at f105bdd.** RAW:6. **PASS.** f105bdd adds `results/raw/2026-11-07_n1-battery_design-to-code_answers.md`, which answers `9838664`.
2. **PI routing, item 2, verbatim.** RAW:8, ENTRY:14–15. **PASS.** Byte-identical, curly ’ included, to RESULTS.md:528 (the close added at 139635f). Only the "2. " prefix and the final "." are dropped.
3. **"After the STOP" routing, verbatim.** RAW:9, ENTRY:16–17. **PASS.** Byte-identical to RESULTS.md:245 (the close added at f105bdd).
4. **The check is `m_analyze.py:9983–9986` at blob 6ec3222b…, and its condition asserts that the tree's file is not the bytes of record.** RAW:14. **PASS.**
   - The blob at 10a2bbb^ (= f105bdd) has sha256 6ec3222b…93d9.
   - :9983–9984 is the label. :9985 has `head_file_sha256 not in (None, table_sha256)`, and head_file is read from the tree (:9892–9895).
   - "True only under the banner" is the seat's own wording (f105bdd §0).
5. **"After N1 the battery did not pass, `--selftest` exited 1, and `ganl` wrote nothing"** (and "failed" at RAW:14). RAW:15. **IMPRECISE.**
   - No run of either on N1's tree with 6ec3222b is logged.
   - The STOP (9838664 §1) states these as consequences, in the present tense. The first values-check derived them from the code: at f105bdd, :11299 returns 1 on a failing battery, and :11108–11111 print "STOP: the battery did not pass; nothing written" and exit 4.
   - ENTRY:19–20's conditional is the accurate form. Suggest "would not pass … would exit 1 … would write nothing".
6. **The seat read `:9984`, the check's label, as prose.** RAW:16. **PASS.** 139635f:46 has "three message texts … (`:4480`, `:4676`, `:9984`) … for prose". f105bdd §0: "called `m_analyze.py:9984` a message text. It is the label…".
7. **Found by the F3 session, and again independently by the first blind values-check.** RAW:17. **PASS.** 9838664's raw, §1 "Who found it"; the first report's item 33 (FAIL).
8. **The STOP is 9838664.** RAW:18, ENTRY:21. **PASS.**
9. **The seat's answer.** RAW:19. **PASS.**
   - The claims: order (b); the check asserts only the blob of record and reports HEAD's sha256; the two prose anchors are reworded in the same edit; N1 comes after the fix and before the canonical `ganl`, so that G-ANL-F3.json records the restored tree.
   - Each matches f105bdd §1. The seat's reported boolean is left out but not misstated. PI item 1 is at RESULTS.md:244.
10. **The fix is "the F3 session's commit" 10a2bbb, and N1 follows it.** RAW:20, ENTRY:8. **PASS (inferred).**
    - 10a2bbb's message calls N1 "the coordinating session's commit", and its own next steps are the F3 chain (`ganl`, LOCK-m-F3).
    - No commit or raw names 10a2bbb's session.
    - The worktree's HEAD is 10a2bbb.
11. **What 10a2bbb changed.** RAW:19–20, ENTRY:22. **PASS.** Its diff of `scripts/m_analyze.py`:
    - the condition becomes `blob_sha256 is not None and blob_sha256 == table_sha256`;
    - the printed tuple adds `head_file_sha256[:16]` and `head_file_is_table`;
    - PIN-V2-11 (:4480–4481) and the comment (:9871–9872) are reworded;
    - the blob moves from 6ec3222b…93d9 to d347ea0c…5e48.
12. **The seven quoted manifest lines.** RAW:54–62. **PASS.** Each is byte-identical to `key : json.dumps(value)` taken from the `preprint` section of `pos/manifest.json`. `banner` has 8 keys.
13. **Positive run, exit 0, sidecar case taken.** RAW:52, ENTRY:36. **PASS.**
    - `pos_run.txt` does not record the exit code. It prints the "wrote" line with "0 re-hash mismatches" and no MISMATCH line, and `main` returns 1 only on mismatches (N18:959–961).
    - The status text and `status_sidecar` are present.
14. **The manifest hashes the final README-NOTE.md (3f2f394c…), so the test covers all four files.** RAW:52, ENTRY:36–37. **PASS.**
    - The worktree's README-NOTE.md has sha256 3f2f394c5bc4…f9f8, which is `files.list[3]` in `pos/manifest.json`.
    - The other three: `script_sha256` 559c4576… is the worktree's N18; the preprint is 45b67246…; the sidecar is 6277f6f4….
15. **Run on the final bytes, in a worktree at 10a2bbb, with the shared tree and the committed manifest untouched.** RAW:51. **PASS.**
    - `head_at_run` is 10a2bbb, and the `n1_pending` copies equal the worktree's files (all four sha256s).
    - The main tree's status is clean for the four paths and for `results/raw/2026-10-09_note-release-manifest.*`. The worktree's status lists only the four files.
16. **The wait check only records modification times, and stops only on a missing file.** RAW:64. **PASS.** N18:620–632.
17. **Negative run: the STOP line, exit 2, nothing written.** RAW:65–69, ENTRY:37–38. **PASS.**
    - `neg_run.txt` is byte-identical to RAW:68.
    - The exit code is not recorded. The line is printed only by `main`'s `except Stop`, which then returns 2 (N18:944–946), before either output is opened (:950, :952).
18. **Battery: 525/525, 538 ids, the reported tuple.** RAW:70, ENTRY:38–39. **PASS.** `battery.txt` has:
    - 525 [PASS] and 0 [FAIL];
    - "coverage: every one of the 538 required ids reached";
    - at :449, the new label with `('45b67246f2b2bcb4', '45b67246f2b2bcb4', True)`.
19. **The battery ran with the project's venv and `-B`.** RAW:70. **PASS.**
    - The INVOCATION line shows `<repo>/jlens-qwen36/.venv/bin/python`, the venv that 10a2bbb's runs raw uses.
    - `-B` is not shown, since INVOCATION prints sys.argv only. The worktree has no `__pycache__`, which fits it.
20. **`:214`, before and after.** RAW:85. **PASS.** In the worktree's `git diff` at README-NOTE.md:214, both quotes are exact substrings of the old and new line.
21. **`:214`'s src gains `@1523cce:262` beside the kept `@32aefcc:1,264`.** RAW:86, ENTRY:44. **PASS.** The only src change inserts "PREPRINT-v1_0-draft.md@1523cce:262;" between `@98d07bc:262` and `@32aefcc:1,264`.
22. **Line 262 of 1523cce's blob carries both quoted phrases.** RAW:87. **PASS.** 1523cce:262 has "licensed for first-token identity only" and "the choice reads are unaffected". It is identical to 32aefcc:264 and to the worktree's :262.
23. **The after-text follows the seat's wording.** RAW:84–85. **PASS.** f105bdd §3 gives ":262 in the restored file", and the parenthesis "(:264 under the banner at the tag)" is verbatim.
24. **Only lines 78 and 214 of README-NOTE.md change.** RAW:72, ENTRY:7. **PASS.** Compared line by line; both versions have 255 lines.
25. **N1-a: the constructs at 6ec3222b.** RAW:91–96. **PASS.**
    - :4478–4482 is PIN-V2-11, with the banner clause at :4480–4481.
    - :9871–9872 is a comment.
    - :9983–9986 is the `B.chk` with cover `F3R-PREPRINT-OF-RECORD` (label :9983–9984).
    - :4676 is PIN-17 ("re-verified against the placed preprint … 45b67246…7a41").
26. **N1-a: "The seat's three anchors" are `:4480–4481`, `:9871–9872` and `:9983–9986`.** RAW:91. **IMPRECISE.**
    - The ruling's three (139635f:46, quoted in the STOP) are :4480, :4676 and :9984.
    - :9871–9872 is Code's anchor (9838664 §1, "The other anchors"). The seat adopted it as the second prose anchor (f105bdd §0–§1).
    - 10a2bbb's entry counts :4676 among "the texts the seat named".
    - Suggest: "The ruling's three anchors (`:4480`, `:4676`, `:9984`) and the comment Code added (`:9871–9872`) were, by construct: …".
27. **N1-a: the first two are reworded and the check is fixed in 10a2bbb, and this commit leaves the analyzer alone.** RAW:96, ENTRY:46–47. **PASS.** The 10a2bbb diff; the worktree's diff has no `m_analyze.py`.
28. **N1-b: the gitleaks RELEASE pin.** RAW:97, ENTRY:48. **PASS.**
    - The claims: `:146` keeps 5d677a72…4467 as "the sha256 each must have", it is left as confirmed, and a run at HEAD would find the restored file.
    - :145 opens `RELEASE`, :146 is the preprint row and the phrase is at :142. :589–595 compares HEAD's blob and the tree's file with that value.
    - The tag holds all five rows at their values. f105bdd §3: "leave it". PI: "[confirmed]".
29. **N1-c: README-NOTE.md 242–243 and 254 describe the tag with 5d677a72…4467 and are unchanged.** RAW:98, ENTRY:49. **PASS.**
    - Each line carries the value: 242, the file at the tag; 243, N18's manifest; 254, the release sequence.
    - The only other line with it is :78.
30. **N1-d: the tag is untouched.** RAW:99, ENTRY:50. **PASS.** `note-2026-10-v2` points to 6d8c237, whose preprint is 5d677a72…. The change touches no ref.
31. **N1-e: `round` still reads 5, at N18:692.** RAW:101, ENTRY:51. **PASS.** The worktree's :692 reads `"round": "5 (2026-11-03, N1 round 11; release v2)"`, and `pos/manifest.json` has the same. The edit's docstring and comments call this round 6.
32. **N1-e: `rerun_trigger` and `routing` keep their pre-tag wording, and the .md prints "equals that blob: NO" without the sidecar.** RAW:102, ENTRY:51. **PASS.**
    - `routing` says "the file the tag is to hold", and `rerun_trigger` says "before the tag commit".
    - `manifest.md:35` ends "The file on disk equals that blob: NO.", and `status_sidecar` is not rendered.
    - Note: in that sentence "that blob" comes right after "its parent's blob … 45b67246…", which the file does equal. The flag actually compares with the banner commit's blob (N18:607, :875). So in the sidecar case the line reads as false. The note discloses the line but not this reading.
33. **ENTRY header facts.** ENTRY:1–9. **PASS.** 139635f §7 N1; the amendment at f105bdd; the commit follows 10a2bbb, the seat's order step 1; the tag is untouched.
34. **ENTRY: why it was held.** ENTRY:19–22. **PASS.** Matches 9838664 §1 and 10a2bbb. "The file at HEAD" is the check's head_file, read from the tree.
35. **ENTRY: the `:214` after-quote, "patch v8's :262 (:264 under the banner at the tag)".** ENTRY:43. **IMPRECISE.**
    - It is not verbatim. The line reads "patch v8's :262 does (:264 under the banner at the tag)", and "does" is dropped without the "…" the before-quote uses.
    - RAW:85 quotes it correctly.
36. **ENTRY N1-a.** ENTRY:46–47. **PASS.**
    - It names the same anchors as RAW N1-a but drops "three". If item 26 is fixed, this line should follow.
    - The anchors are 6ec3222b's. At 10a2bbb the check spans :9983–9988.
37. **RAW–ENTRY consistency, the rest.** **PASS.** The file, the sidecar, N18, the tests, :78, N1-b to N1-e, the raw link and the committed paths agree. The divergences are items 5, 26 and 35.
38. **Spot-check: the restored file's sha256.** RAW:25, ENTRY:25. **PASS.**
    - The worktree's file is 45b67246…7a41, which is the blob at 1523cce and at 32aefcc^: 88,668 bytes, 468 lines. HEAD's is 5d677a72…, 89,267 bytes, 470 lines.
    - It is bound at `LOCK-m-F0.md:29`, `:204` and `:414` and at `m_posting_sentences.json:42`.
    - 32aefcc is the only commit to the file since 1523cce.
39. **Spot-check: the sidecar, 6277f6f4…4626, 892 bytes.** RAW:32, ENTRY:27. **PASS.** Its first 599 bytes are the bytes the banner commit added. Line 3 is the added sentence, equal to RAW:37.
40. **Spot-check: 34 lines added.** RAW:50, ENTRY:30. **PASS.** The hunks add 9, 4 and 21 lines and remove none.
41. **Spot-check: 599 bytes.** RAW:27, ENTRY:26. **PASS.** 32aefcc's blob is a 599-byte, two-line prefix followed by its parent's blob. The worktree's diff removes those two lines.
42. **Spot-check: README-NOTE.md:78's after-text.** RAW:81. **PASS.** It is an exact prefix of the worktree's :78, and the rest of the line, up to the src comment, is unchanged.
43. **Local paths, IP addresses and ports.** Both drafts. **PASS.**
    - None in either draft. The only ":NNNN" hits are line anchors.
    - Aside: `battery.txt` (INVOCATION), `pos_run.txt` and the manifest's `command` field carry local paths. Scrub them if any of these is committed.

**Summary: 43 items. PASS 40, IMPRECISE 3 (items 5, 26, 35), FAIL 0, UNVERIFIABLE 0.**

*Process note: I wrote two temporary copies of the analyzer's blobs to the scratchpad root (`vc2_ma_parent.py`, `vc2_ma_head.py`), which breaks the "write only to the report path" rule, and deleted them a few minutes later. Nothing in the repository or the worktree was written.*

### Code's dispositions, check 2

| # | verdict | disposition |
|---|---|---|
| 5 | IMPRECISE | Applied: "would have failed … would not pass … would exit 1 … would write nothing", given as consequences read from the code, not logged runs. |
| 26 | IMPRECISE | Applied: N1-a names the ruling's three anchors (`:4480`, `:4676`, `:9984`) and the comment Code added (`:9871–9872`), each by construct. The entry follows. |
| 35 | IMPRECISE | Applied: the entry's `:214` quote reads "patch v8's :262 does (:264 under the banner at the tag)". |
| notes | — | N1-e now states the .md line's false reading in the sidecar case. Exit codes and `-B` follow from the code and the run, as the check found. The test outputs are not committed: they are quoted in the raw, scrubbed. |
