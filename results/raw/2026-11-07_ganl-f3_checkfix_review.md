# G-ANL-F3 -- the check fix (order (b)): blind review of the delta (Code's raw, 2026-11-07)

*A blind review agent (fresh context, read-only) reviewed `git diff f105bdd 05062c9 -- scripts/m_analyze.py` in Code's scratch worktree (the first form of the edit, analyzer `ea872bdc…5b4a`) against the seat's answer of 2026-11-07, §1. Its report follows verbatim, local paths scrubbed (`<tmp>` = Code's session scratch). Code's dispositions follow it. Three NOTEs changed code, so the analyzer's final sha256 is `d347ea0c…5e48`, and the site check and the restored-state battery were re-run on the final bytes (the runs raw).*

## 1. The report (verbatim)

**Tallies: 0 MAJOR, 0 MINOR, 6 NOTE. Three texts that now read as stale are listed separately and not counted.**

Line numbers refer to `scripts/m_analyze.py` at 05062c9 (blob ea872bdc…, 11,365 lines).

## Verdict on the review questions

**1. Does the delta do what the ruling says, and nothing else? Yes.**
- One file changes, in four line hunks. At the AST level there are exactly three code changes:
  - `PINS_F3["PIN-V2-11"]`;
  - one inserted assignment in `_bt_qf0_regression` (:9895);
  - the one `B.chk` call in `_bt_riding` (:9983–9988).
- The fourth hunk is the comment at :9867–9875.
- PIN-V2-11's new text equals the old text with the ruled substitution applied, character for character.
- Word diff of the comment:
  - deleted: `PREPRINT-v1_0-draft.md at HEAD carries the note release's status banner since 32aefcc ("not a text of record"), so`
  - inserted before the colon: `, whatever the tree holds; HEAD's sha256 reported`
- The condition is now exactly `blob_sha256 == table_sha256`. The detail prints the head file's sha256 and `head_file_is_table`. The label no longer presupposes the banner. Neither "banner" nor "32aefcc" appears anywhere in the analyzer now.

**2. Is the check state-independent? Yes.** I simulated each state in-process (only reads of that one path were patched) and ran the check's own statement, compiled from its source:

| Preprint state | New check | Detail printed | Old condition |
|---|---|---|---|
| bannered (5d677a72…) | PASS | (…, '5d677a724652c418', False) | True |
| restored (45b67246…7a41) | PASS | (…, '45b67246f2b2bcb4', True) | False |
| absent | PASS | ('45b6…', 'None', False) | False |

- In all three states the regression itself was unaffected: error None, status written, both Q-F0 outputs byte-identical, all seven PIN-29 pins true.
- The real preprint is read nowhere else in the analyzer. `run_verdicts` gets the 1523cce blob through `read_repo_file`, and every other preprint in the battery is a synthetic temp file. So the whole battery verdict no longer depends on the preprint's state.
- Under the old code, a restored or absent preprint also failed the "538 ids reached" coverage check, because coverage is only marked on a pass. That is fixed too.

**3. Can it still fail where it should? Yes.** Three plants all give FAIL:
- the 1523cce blob mutated;
- the 1523cce blob missing;
- the table naming another sha256.

**4. Is `head_file_is_table` safe for every consumer? Yes.**
- `battery()` passes `reg` through. `_g_anl_f3_block` (:11143) and `ganl_artifact` (:11167) embed it.
- `ganl_artifact_problems` (:11202) checks only the top-level keys of `g_anl_f3`, plus equality with a rebuild from the same `res`. Nothing asserts the key set inside the regression or preprint dicts.
- `json_text`/`_assert_native` (resume.py:159) accept `bool`.
- `--selftest` reads only `res["ok"]`.
- The battery's fake manifest result carries no regression.
- `REGRESSION_REPORT` is static and makes no claim about the preprint.
- No consumer outside m_analyze.py (git grep over \*.py, \*.json, \*.sh).
- Probe: `ganl_artifact_problems(art, res) == []` with the real regression dict, and the artifact's preprint keys gain `head_file_is_table`.
- No G-ANL-F3.json exists yet, so no written artifact changes shape.

**5. Do the rewordings say what the ruling says? Yes**, verbatim for PIN-V2-11; NOTE 6 has a small prose point on the comment.

**6. Do check counts or coverage ids change? No.**
- EXPECTED_CHECKS is still 525; `len(REQUIRED_COVERAGE)` is still 538.
- There are 308 static `chk` call sites before and after, with identical cover expressions. `_REQUIRED` is untouched, and the replaced call is an unconditional one-for-one swap.
- The PIN-site regexes match identically on both sources (STR-PIN-COMMENTS: 50 markers; F3R-PIN-REGISTER: 24 sites).
- `_forbidden()` finds nothing in the new source.

## NOTEs

1. **The boolean also enters the artifact.** It is computed in `_bt_qf0_regression` (:9895), so besides the battery line it lands in G-ANL-F3.json at `g_anl_f3.regression.preprint.head_file_is_table`. This matches how `head_file_sha256` is already carried, and the ruling asks for a "reported boolean". It is an artifact-content change beyond the check, though, so disclose it in the entry for "nothing else changes" to read true. Computing it inline in the detail (:9987) would have left the regression dict and the artifact untouched.

2. **"HEAD's" is really the working tree.** `head_pre = REPO / pre["path"]` (:9891, read at :9894) is the working-tree file. The new label (:9984–9985) and PIN-V2-11 (:4480) call it HEAD's, and the two agree only on a clean tree.
   - Concrete case: the scratch worktree right now shows ` M PREPRINT-v1_0-draft.md`, your probe, at HEAD 05062c9, whose blob is 5d677a72…. A battery run there prints the tree's values under "the file at HEAD's".
   - In `ganl`, `ganl_commit_problems` (:11059) does not cover the preprint. An uncommitted edit would be recorded in the write-once artifact as HEAD's.
   - The PIN wording is the seat's verbatim. The label is Code's own and could say "the file in the tree". The field name predates this edit.

3. **The check is state-independent; the artifact's bytes are not.** `head_file_sha256` (already there) and now `head_file_is_table` record the tree. A canonical `ganl` re-run after any later draft edit (the seat's own "a later draft edit moves the file again") is refused by `write_texts_once` as different bytes, even though the battery passes. This is consistent with "G-ANL-F3.json records the restored tree"; worth a line in the entry.

4. **Latent vacuous pass.** :9986 is True when both sides are None, for example if `reg["preprint"] == {}`. The old second conjunct made that case False.
   - It cannot happen today: nothing returns before :9895 (failures there raise, and `B.group` fails the group). A null table sha256 with a missing blob also sets `error`, which fails F3R-REGRESSION.
   - Hardening that stays inside the ruled form: `pp.get("blob_sha256") is not None and …`.

5. **The check is now implied by F3R-REGRESSION.** It fails exactly when the blob sha differs from the table sha, and that case also sets `reg["error"]` (:9896–9898), so F3R-REGRESSION fails alongside it. It still pinpoints the cause. Informational only.

6. **Comment prose (:9872).** The inserted clause sits before the colon, so "no blob but that one can satisfy the table's binding" now reads as explaining "HEAD's sha256 reported". PIN-V2-11's insertion is inside the parenthesis and reads correctly. The ruling said "the same", so any change here is optional.

## Texts that now read as stale (not defects)

- **:1693–1694.** "Synthetic; not derived from PREPRINT-v1_0-draft.md (not the preprint of record, m:58)". This dates from G-ANL-F0 (64df36b). After N1 the parenthesis is false at HEAD, as it also was between 1523cce and 32aefcc. It is not about the banner.
- **:9867.** The PIN-V2-11 marker cites "a dated note in the G-ANL-F3 entry". That note (RESULTS.md:620–626 at f105bdd) gives the banner as the reason and says "No analyzer change is made for it"; this edit supersedes both. The marker line was outside the ruling's scope, so the forward pointer belongs in the commit entry.
- **:4676 and its site comment :1485 (PIN-17).** Seat-ruled to stay. True again at HEAD after N1.

## Checked in passing (no finding)

- No G-SHAPE artifact (F0, F3, p, or the superseded ones) contains "m_analyze". In the drivers and the p/mf3 packages, the only references are `ANALYZER_PATH` in mf3/stages.py and p's register entry (3); neither is a G-SHAPE map.
- The seat's A3 condition ("no in-place analyzer commit while an OLMo unit is open") is met: all three OLMo units are on record as NOT-RUN (dose-not-completable).

## What I ran

- Read the ruling and `git diff f105bdd 05062c9`, and extracted both blobs to chk_review.
- `probe_static.py`: AST diff, the PIN-V2-11 substitution check, and a census of `chk` sites.
- `probe_dyn.py`: imported the worktree analyzer read-only (python -B, TMPDIR under chk_review), patched in-process reads of the one preprint path for the three states, ran `_bt_qf0_regression()` and the check's statement in a fresh `_Battery`, then the plants on `_bt_git_blob` and the table read.
- `probe_art.py`: `ganl_artifact`, `ganl_artifact_problems` and `json_text` on a result carrying the real regression dict. It builds dicts only; `closure()` ran through its own `-I -B` subprocess.
- Repo-wide greps for consumers.

I did not run `--selftest` or any suite, and wrote nothing to the worktree (`find -newer` found nothing). The worktree's ` M PREPRINT-v1_0-draft.md` appeared during the review and is your probe, not mine.

Outputs are in <tmp>/chk_review/:
- static_out.txt
- dyn_out.txt
- art_out.txt

## 2. Code's dispositions

| NOTE | Disposition |
|---|---|
| 1 (the boolean enters the artifact) | Disclosed in the entry: the artifact will record `head_file_is_table` beside `head_file_sha256`. Reporting it there is the ruling's "reported boolean". |
| 2 ("HEAD's" is the working tree) | Applied to Code's own label: "the file in the tree's sha256". PIN-V2-11's wording is the seat's verbatim and stays. The field name predates this edit. |
| 3 (the artifact's bytes follow the tree) | Disclosed in the entry. |
| 4 (latent vacuous pass) | Applied: `pp.get("blob_sha256") is not None and …`, inside the ruled form. |
| 5 (implied by F3R-REGRESSION) | No change (informational). |
| 6 (the comment's clause order) | Applied: "and, whatever the tree holds (HEAD's sha256 reported), the preprint of record is served by its committed blob (…): no blob but that one can …". |
| Stale :1693–1694 | No change: not about the banner, and outside the ruling. |
| Stale :9867 (the marker's pointer) | The entry names the superseded dated note. |
| Stale :4676 / :1485 (PIN-17) | Seat-ruled to stay. |
