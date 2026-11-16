# n_analyze.py, the schema pin move: the blind values-check, two passes (PI date 2026-11-16)

Code's raw for the entry `n package — scripts/n_analyze.py, the schema pin moved from 5a97527 to 14e65d8`. Two blind
values-checkers, each a subagent of this session under a brief quoting the list of record v2's items 1–5 and allowing
no Python, checked the entry and the pin-move raw against their sources, claim by claim. The second checked the
revised texts, and this raw's §1–§2: whether each of the first pass's dispositions was carried. Each report is
reproduced whole (its headings demoted two levels), followed by Code's dispositions. The checkers write SCRATCH for
Code's scratch folder and REPO for the repository.

## 1. The first pass: the checker's report, whole

### Blind values-check: the schema pin move (entry draft and raw draft)

PI date 2026-11-16. SCRATCH is the author's scratch folder (the `n9` folder). REPO is the repository checkout. I edited
nothing in REPO or SCRATCH; this report is the only file written.

Drafts checked:

1. `SCRATCH/pin/pin_entry.md`: the RESULTS.md entry. Its "Values-check: {VC}" line is a placeholder and was skipped.
2. `SCRATCH/pin/2026-11-16_n-analyze_pin-move.md`: the raw.

#### Tools

**Within the brief:** Read, `shasum -a 256`, `/usr/bin/grep`, `awk`, `sed -n`, `diff`, `cmp`, `comm`, `sort`,
`wc -l`, name-only `ls`, and `git log` / `show` / `rev-parse` / `diff`. The awk programs included split.awk's three
rules rewritten to print to stdout, a "complement" program printing the lines split.awk writes nowhere, and a
transitive-closure program over the d14 files.

**Beyond the brief's list.** All were read-only; I report them as asked:

- `cat`, once, to print `SCRATCH/pin/defs.awk`. One `cat -A` was rejected by macOS.
- `head`, once, in that same pipe.
- `tr`, to reflow name lists.
- `tail -1`, on `git diff --stat` of `valence_core/n/schema.py` between the two commits.
- `uniq -d`, to check for duplicate definition names.
- `git hash-object scripts/n_analyze.py`, a digest only.
- `git grep`, twice: at `14e65d8` with `-- . ':!data/**'`, and on two named committed paths.
- `git ls-files results/raw`.
- `git status --porcelain`, scoped to four named paths.
- `git diff --quiet HEAD -- RESULTS.md`.
- `git diff --stat` and `--numstat`, on `valence_core/n/schema.py` and `scripts/n_analyze.py` only.
- One recursive `/usr/bin/grep -l` over SCRATCH, excluding `__pycache__`.
- Shell builtins: echo, printf, for, while read, test, case, cd.

**What I did not do.**

- I ran no Python and no interpreter other than awk.
- Nothing ran in the background.
- I wrote no temporary files: only pipes and process substitution. One diff's stdout was discarded to `/dev/null`.
- Nothing under `data/` was listed, read, stat'ed or searched, and `data/mf3` was not touched.
- I ran no whole-tree status.

#### How the checks were made

- **Hashes.** I hashed `git show <c>:valence_core/n/schema.py | shasum -a 256` at 5a97527, 5c0ae6b and 14e65d8. I
  also hashed the tree's `schema.py` and `scripts/n_analyze.py`, and `SCRATCH/pin/schema_5a97527.py` and
  `schema_14e65d8.py`. `git rev-parse` gave the full commit ids and the analyzer's blob ids.
- **The split.**
  - I ran split.awk's rules as a stdout program on each blob and diffed the result against the d5/d14 files,
    concatenated in the same order. They are identical: all 77 blocks for 5a97527 → d5, and all 109 for 14e65d8 → d14.
  - Each blob has its number of definition starts (77 and 109) with no name twice. So the splitter's
    truncate-on-reopen cannot have overwritten a block.
  - The scratch copies `schema_5a97527.py` and `schema_14e65d8.py` hash as the blobs.
- **The discarded lines.** A complement awk program printed every line split.awk writes nowhere, for each blob. I
  diffed the two outputs. The full `git diff 5a97527 14e65d8 -- valence_core/n/schema.py` was checked against them.
- **What the analyzer reaches.**
  - I collected every `sm.<name>` in the tree's `scripts/n_analyze.py`. I also searched for any other alias, for
    `importlib` and for `getattr` on the module. Only `sm` is bound to `schema_module()`, which uses `importlib` once
    to import the schema.
  - I then computed a conservative closure from those 10 names over the d14 blocks: every identifier token naming a
    split block, iterated. The three docstring blocks were excluded.
- **§2's table.** I rebuilt it from d5/d14 and the analyzer's `sm` set, in C-locale order. A block counts as "comment or
  blank lines only" if every line of its diff is blank or a comment. My table and the raw's 77 rows are identical.
- **§3–§7.** I diffed each code block against its source:
  - §3: the d-file diffs;
  - §4: the 14e65d8 blob, lines 1219–1224;
  - §5: `split.awk`;
  - §6: `git diff -- scripts/n_analyze.py`;
  - §7: `SCRATCH/runs/pin1.out`, with the repository root replaced by `<repo>`.

#### Could the splitter hide a change?

**Yes, by construction.** Its third rule ends the current block at any column-0 line that is not a comment and does not
start with `)`, `]` or `}`. That line, and every line after it up to the next definition start, is written nowhere. So
these are never compared:

- the module docstring's prose, except lines that begin `word:` at column 0, which the splitter takes for definitions;
- imports;
- top-level statements: loops, `del`, calls, and augmented or subscript assignments;
- decorators;
- the `__main__` block;
- tuple assignments: `A, B = …` does not match `NAME *[:=]`.

The splitter discards 139 lines of 5a97527 and 188 of 14e65d8. Between the two blobs they differ only in:

- **The module docstring's prose:**
  - its first line;
  - the second line of the `schema:` sentence;
  - the sentence on the other records (two lines become four);
  - the two-line EXAMPLES paragraph. It is replaced by the stage-report and G-READ-n sections, the PASS-rule paragraph
    and a new EXAMPLES paragraph.
- **`import json`, added.** Only new code uses it (`identity_sha256`, `_selftest`). In 5a97527 "json" occurs only
  inside strings.
- **The NESTED registration loop and `del _t`, added.** This is the raw's §4.

Among the discarded lines, these are unchanged:

- the other imports;
- the `__main__` block;
- `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = "N1-V", "none", "0"`, at line 200 of 5a97527 and line 279 of 14e65d8.
  This is a top-level definition the splitter misses entirely, and the analyzer reaches it: `shadow_read_id` uses it,
  and `check_record` calls `shadow_read_id`.

Neither blob has a decorator.

**Cross-check.** `git diff 5a97527 14e65d8 -- valence_core/n/schema.py` shows 815 insertions and 10 deletions. The 10
removed lines are:

- 7 in the four module-docstring passages above;
- 2 in `SchemaError`'s docstring;
- 1, `check_record`'s message.

These are the six rewritten places that n-build's committed entry lists (RESULTS.md at 14e65d8, "What changed").

**What this means.** The split did hide real changes: the docstring prose and `import json`. None of them touches
anything the analyzer reaches. The one hidden code change that matters is the loop, which the raw examines in §4.
Neither draft says that the discarded lines were compared, and the raw never mentions `import json` (see E30, R4 and
R16).

**The NESTED registration cannot change an old table's dispatch.** None of the 18 new tags occurs as a quoted string
anywhere in 5a97527's blob. The record, cell, identity and nested field tables are identical in both blobs.

#### Draft 1: the entry (`SCRATCH/pin/pin_entry.md`)

| ID | Claim | Status | How / correction |
|---|---|---|---|
| E1 | Date 2026-11-16 | CONFIRMED | A calendar date only. It matches the raw's PI date and 14e65d8's entry. |
| E2 | The schema pin moved from 5a97527 to 14e65d8 | CONFIRMED | The §6 diff: `SCHEMA_SHA256` goes from 77c12d6d…94bc (`# 5a97527`) to 4bed3f9a…4665 (`# 14e65d8`). |
| E3 | n-build's schema commit changed the file the analyzer pins | CONFIRMED | `git show --name-status 14e65d8` shows M `valence_core/n/schema.py`, which is the analyzer's `SCHEMA_REL`. |
| E4 | The coordinating session's order: BUILD 5c0ae6b, then the schema, then this | CONFIRMED, as recorded | 5c0ae6b's committed entry says: "n-build's schema commit, which the coordinating session orders after this one … The pin then moves in its own entry". SCRATCH/PLAN.md has "Commit order (coordinating session, 2026-11-16)", items 1–3. In git, 14e65d8's parent is 5c0ae6b. No file holds the coordinating session's own words. |
| E5 | "Four lines" (headline) | IMPRECISE | The edit removes four lines and adds six, in four hunks (`--numstat` gives 6 4). Correction: "Four lines rewritten as six" or "four edits; six lines in, four out". |
| E6 | Battery 171/171 | CONFIRMED | pin1.out has 171 `[PASS]` lines, 0 `[FAIL]`, and ends "171/171 n_analyze battery checks pass". `EXPECTED_CHECKS` is 171. |
| E7 | The battery ran "against the new schema" | UNVERIFIABLE | pin1.out records neither the analyzer's bytes nor the schema's. Its 171 check lines and its summary are byte-identical to the BUILD's run of record against 5a97527 (`results/raw/2026-11-16_n-analyze_build_selftest.txt`), so the output cannot show which pair ran. The claim is consistent with the code: the edited analyzer passes its reader-path checks only on a schema that hashes to 4bed3f9a…, the tree's file now. |
| E8 | Model-free: nothing ran on a model or on the box | UNVERIFIABLE | A claim about activity. pin1.out's own checks do pass: "no model library is imported by the battery …" and "module-level imports are numpy and the standard library only". |
| E9 | The analyzer at 5c0ae6b refuses any `schema.py` but 5a97527's bytes (sha256 77c12d6d…94bc) | CONFIRMED | The analyzer's blob at 5c0ae6b and HEAD is d1c35444…, with `SCHEMA_SHA256 = "77c12d6d…94bc"`. `schema_module()` raises `AnlRefusal` when the file's sha256 differs. The blob hashes to 77c12d6d…94bc at both 5a97527 and 5c0ae6b. |
| E10 | 14e65d8 changed that file to sha256 4bed3f9a…4665 | CONFIRMED | Hash of the blob. |
| E11 | So from that commit the analyzer's reader and battery refused | CONFIRMED, by reading the code | `load_campaign` (`sm = sm or schema_module()`), `_bt_reader` and `_bt_commands` all call `schema_module()`. No run of the refusal is recorded, and the drafts claim none. |
| E12 | The raw (link) holds the check in §1–§5 | CONFIRMED | §1–§5 are the check. The link's file name matches the draft. The raw is not yet in REPO, and its name collides with nothing in `results/raw`. |
| E13 | Code verified the commit and the blob (§1) | CONFIRMED | Every §1 value holds: R8–R14. |
| E14 | Split both blobs, from `git show <commit>:…`, at their top-level definitions with a short awk script | CONFIRMED | The scratch copies hash as the blobs. d5 and d14 are exactly split.awk's split of the blobs, reproduced on stdout and diffed. |
| E15 | Each pair present in both was compared with `cmp` | CONFIRMED | My `cmp` of the 77 shared pairs gives the same 70 / 2 / 5. |
| E16 | "Of 5a97527's 77 definitions" (and, later, "the 32 new definitions") | IMPRECISE | These are the splitter's block counts. 5a97527's 77 include two module-docstring lines, `schema:` (line 6) and `own:` (line 95). They omit the three names of the unchanged tuple assignment `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = …`. 14e65d8's 109 include three docstring lines (`schema:`, `own:`, `carries:`), so the 32 new blocks are 31 definitions plus `carries:`. Correction: "Of the 77 blocks the splitter finds in 5a97527 (75 definitions and two docstring lines, `schema:` and `own:`)…" and "Of the 32 new blocks (31 definitions and the docstring line `carries:`)…". |
| E17 | None is gone | CONFIRMED | `comm` finds no name only in d5. The full diff removes no definition line. |
| E18 | 70 are identical | CONFIRMED | `cmp`. |
| E19 | Two differ in comment or blank lines only (`check_cell`, `example_cell`) | CONFIRMED | `check_cell` gains one comment line at its end ("# --- the stage report …"). `example_cell` no longer ends with the "# --- self-test …" comment and a blank line; in 14e65d8 those end `example_gread`. |
| E20 | Five changed | CONFIRMED | `check_record`, `SchemaError`, `__all__`, `_selftest` and `schema`. |
| E21 | `check_record`: one refusal message | CONFIRMED | Its block's diff is one `_fail` message (line 112 becomes lines 112–113). The condition is untouched. |
| E22 | The new message: "is never a record (a pause during a stage; a G-VER-STOP at G-VER)" | CONFIRMED | Verbatim as the runtime string, which is two adjacent literals: `"…(a pause during a "` and `"stage; a G-VER-STOP at G-VER)"`. |
| E23 | The old message: where it "is a STOP" | CONFIRMED | 5a97527 reads "…a rendering mismatch is a STOP, never a record". |
| E24 | `SchemaError`: its docstring | CONFIRMED | Its block's diff is lines 2–3, the docstring. |
| E25 | `__all__`, n-build's `_selftest`, and a line of the module docstring that the splitter takes for a definition | CONFIRMED | `__all__` gains five lines (10a11,15). `_selftest` gains 202 lines (286a287,488) and loses none. The `schema:` line (line 6) changed. |
| E26 | "Everything it calls in the schema (`sm.<name>`), and everything `check_cell` and `check_record` reference by name, is identical apart from `check_record`'s message." | **FAIL** | The analyzer calls `sm.SchemaError`, whose docstring changed: the entry's own "Five changed". It also calls `sm.check_cell`, whose block differs by a comment: the entry's own "Two differ in comment or blank lines only". The raw's §3 lists all three. Correction: "…is identical but for three blocks: `check_record` (its message), `SchemaError` (its docstring) and `check_cell` (the section comment that now follows its unchanged code); the raw's §3." |
| E27 | `NESTED`'s literal is identical | CONFIRMED | `cmp` of the 14-line block: 5a97527 lines 574–587, 14e65d8 lines 653–666. |
| E28 | 14e65d8 registers 18 new keys in it, none of its 9 old ones | CONFIRMED | The loop at 14e65d8 lines 1219–1224 names 18 tags. They are disjoint from the literal's 9 keys. Neither blob assigns into `NESTED` anywhere else. |
| E29 | Of the 32 new definitions, the analyzer calls none | CONFIRMED | None of the 32 names that exist only in d14 is among the 10 `sm` names, and the closure from those 10 reaches none of them. See E16: `carries:` is a docstring line. |
| E30 | "This confirms, for the committed bytes, the list of changes n-build sent before its commit." | IMPRECISE | See the note after this table. |
| E31 | `SCHEMA_SHA256` to 4bed3f9a…4665 | CONFIRMED | §6 equals `git diff`. |
| E32 | "Its section comment and `schema_module`'s docstring to 14e65d8" | IMPRECISE | The docstring is right. The section comment also takes the sha prefix `4bed3f9a...4665` and gains a second line: "its record and cell checks as at 5a97527 but for check_record's rendering-mismatch message". That line is true; see E26's corrected form. Correction: "its section comment to 14e65d8 and 4bed3f9a…4665, with a line saying the record and cell checks are as at 5a97527 but for check_record's message; schema_module's docstring to 14e65d8". |
| E33 | `counters`' docstring now quotes `check_record`'s new wording | CONFIRMED | It quotes "a rendering mismatch is never a record (a pause during a stage; a G-VER-STOP at G-VER)". That is a verbatim substring of the new message; the docstring wraps it after "a". |
| E34 | Six lines in, four out | CONFIRMED | `git diff --numstat` gives 6 4. |
| E35 | `scripts/n_analyze.py` becomes sha256 `4f63903f161885a8bb16ea933157d6e0e609e3cfa91503ac3ef68b1af23c5d73` | CONFIRMED | Hash of the tree's file, whose blob is c5efdf0, the diff's index line. |
| E36 | "The battery against the tree's `schema.py` at 14e65d8" | UNVERIFIABLE | Same reason as E7. |
| E37 | 171/171, every one of the 172 coverage ids reached | CONFIRMED | pin1.out's last lines. |
| E38 | Exit 0 | UNVERIFIABLE | No exit status is recorded. Under `main`'s rule, `return 0 if battery()["ok"] else 1`, where `ok` means every check passes, the count equals 171 and no coverage id is left unreached, the printed lines imply 0. |
| E39 | It ran in a window the coordinating session granted, one process at `nice -n 19`, in the foreground | UNVERIFIABLE | No committed or scratch file records the grant or how the run was invoked. |
| E40 | No other Python ran for this step | UNVERIFIABLE | A negative claim about activity. |
| E41 | Committed by path: `scripts/n_analyze.py`, the raw and this entry. Not pushed. | UNVERIFIABLE | It describes the coming commit. Today `scripts/n_analyze.py` is modified, uncommitted, and the raw is not in REPO. |
| E42 | Next: the `verdicts` command, in a BUILD of its own | CONFIRMED | It matches 5c0ae6b's entry: "It is built after n-build commits its stage-report and G-READ-n forms, in an entry of its own". |
| E43 | The forms are committed (n-report-v1 and n-gread-v1, at 14e65d8) | CONFIRMED | 14e65d8's blob has `REPORT_SCHEMA = "n-report-v1"` and `GREAD_SCHEMA = "n-gread-v1"`; so does its entry. |
| E44 | G-ANL-n's canonical run waits for the seat's answers and G-CAL-n's dose map | CONFIRMED, as recorded | 5c0ae6b's entry says so, and no later RESULTS entry records either. |

**E30 in detail.**

- **What n-build sent.** n-build's list survives only in Code's note in SCRATCH/PLAN.md ("Schema pin move"):
  - the names that are byte-identical, including `read_plan_sha256`, `_check_table` and `_check_type`;
  - `check_record`: one message only;
  - `SchemaError`: docstring only;
  - "module-level additions (json import, report and G-READ constants/checks/builders, __all__, 18 NESTED type names,
    no collision)".
- **What the raw's check covers.** Every item except the `json` import. That import lies outside the split, and the
  raw never mentions it. The module docstring's prose changes are outside the split too; they are named in n-build's
  committed entry, though not in PLAN.md's note.
- **The list is right in substance.** I confirmed the rest from the discarded-lines comparison and the full diff
  described above.
- **Correction:** "This confirms the definition-level items of the list n-build sent before its commit. Its `import
  json` and the module docstring's prose lie outside the split; a comparison of the lines the splitter discards shows
  them, the §4 loop and nothing else." Add that comparison to the raw.

#### Draft 2: the raw (`SCRATCH/pin/2026-11-16_n-analyze_pin-move.md`)

| ID | Claim | Status | How / correction |
|---|---|---|---|
| R1 | Title: the pin moved from 5a97527 to 14e65d8 (PI date 2026-11-16) | CONFIRMED | As E2. A calendar date only. |
| R2 | "Code's raw for the entry `n package — scripts/n_analyze.py, the schema pin moved to 14e65d8`" | IMPRECISE | This is not the entry's title verbatim. The entry reads "n package — `scripts/n_analyze.py`, the schema pin moved from `5a97527` to `14e65d8`". Correction: quote it that way, or present it as a short form without the code quotes. |
| R3 | 14e65d8 changed `schema.py`, which the analyzer committed at 5c0ae6b pins by sha256 and refuses otherwise | CONFIRMED | As E9–E10. |
| R4 | "every top-level definition of the two schema blobs compared (§2)" | IMPRECISE | §2 compares the 77 blocks the splitter finds in both blobs, and two of those are docstring lines. The tuple assignment `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = …` is a top-level definition the splitter never sees; it is unchanged, and the analyzer reaches it through `shadow_read_id`. Correction: "every top-level block the splitter finds; the lines it discards compared separately", and give that result. |
| R5 | The section list, §1–§7 | CONFIRMED | The raw's sections are as listed. |
| R6 | "Nothing ran on a model or on the box." | UNVERIFIABLE | As E8. |
| R7 | "The one Python process was the battery (§7), in a window the coordinating session granted, at `nice -n 19`, in the foreground." | UNVERIFIABLE | As E39–E40. |
| R8 | 14e65d8 is `14e65d812fe5e1a1e311150c7e1bf0d31b745899` | CONFIRMED | `git rev-parse`. |
| R9 | Parent 5c0ae6b | CONFIRMED | `git log --format=%P` gives 5c0ae6b18c48…. |
| R10 | Paths: M `RESULTS.md`; A `results/raw/2026-11-16_n-schema-v2_valuescheck.md`; M `valence_core/n/schema.py` | CONFIRMED | `git show --name-status`. |
| R11 | The blob's sha256 at 5a97527 is `77c12d6d0e7e…94bc` (full) | CONFIRMED | Hash of the blob. It is the same at 5c0ae6b. |
| R12 | The blob's sha256 at 14e65d8 is `4bed3f9a6311…4665` (full) | CONFIRMED | Hash of the blob. |
| R13 | "(n-build's message gave `4bed3f9a…`)" | UNVERIFIABLE | The message is in no file. SCRATCH/PLAN.md records only the step "n-build sends the commit + sha256". The same full value appears twice in n-build's committed raw, `results/raw/2026-11-16_n-schema-v2_valuescheck.md`. |
| R14 | The tree's file is `4bed3f9a…` | CONFIRMED | Hash of the file. A status scoped to the file shows `schema.py` unmodified. |
| R15 | Each blob was split at its top-level lines by split.awk (§5) | CONFIRMED | As E14. |
| R16 | The splitter's rule as described ("…starts a definition, which runs to the next top-level line; a top-level comment joins the definition before it") | IMPRECISE | Right as far as it goes, but three things are missing. A column-0 line starting with `)`, `]` or `}` also joins the definition. A column-0 line that starts no definition ends the current one, and that line and everything up to the next definition start are discarded: docstring prose, imports, the tuple assignment, the §4 loop with `del _t`, and the `__main__` block are never compared. And `NAME:` also catches docstring lines. Correction: say so, and report the separate comparison of the discarded lines. |
| R17 | Each definition present in both blobs was compared with `cmp`; differences in comment or blank lines only are marked | CONFIRMED | Reproduced. |
| R18 | "Two 'definitions' are lines of the module docstring … (`schema:`, and in 14e65d8 `carries:`); they are text." | **FAIL** | There are three. `own:` ("own: ``ids_sha_bk`` is null.") is one too, in both blobs: line 95 of 5a97527 and line 98 of 14e65d8. It sits in §2's table as an unmarked "identical" row. Correction: "Three 'definitions' are lines of the module docstring that begin with a word and a colon at column 0 (`schema:` and `own:` in both blobs, and in 14e65d8 `carries:`); they are text." |
| R19 | §2's table: 77 rows and each one's status | CONFIRMED | Rebuilt independently; the diff is empty. |
| R20 | §2's "The analyzer calls it" column (10 names) | CONFIRMED | The `sm.<name>` set in the tree's analyzer is `CELL_SCHEMA`, `SchemaError`, `TOLD_LINE`, `cell_filename`, `check_cell`, `dose_point_values`, `dose_points`, `example_identity`, `example_record` and `read_plan`. The analyzer has no other way into the module. |
| R21 | `check_cell` references `CELL_FIELDS`, `CELL_SCHEMA`, `_check_table`, `_fail`, `cell_filename`, `check_record`, `check_stage_identity` and `read_id` | CONFIRMED | Its block's identifiers, intersected with the split names, in both blobs. `schema` also matches, but only inside strings. |
| R22 | `check_record` references the 23 names listed | CONFIRMED | Same method, both blobs. It references none of the `SHADOW_*` names. |
| R23 | The words `schema`, `own` and `carries` match only inside their strings | CONFIRMED | `rec["schema"]`, `w("schema")` and an f-string; "…whose sequence is its own"; "…carries a direction…" and similar. |
| R24 | Each is identical across the two blobs, but `check_record` (the message in §3) | CONFIRMED | `cmp` finds all 31 listed names identical except `check_record`. |
| R25 | `_check_table` dispatches through `_check_type` and `NESTED`, both identical; `NESTED`'s new keys are none of its old ones | CONFIRMED | Also, no new tag occurs as a quoted string in 5a97527's blob, so no old table's type tag can select one. |
| R26 | The 32 names new in 14e65d8 | CONFIRMED | Exactly the names that exist only in d14. |
| R27 | None of them is called by the analyzer | CONFIRMED | As E29. |
| R28 | §3: the three blocks the analyzer can reach that differ are `check_record`, `SchemaError` and `check_cell` | CONFIRMED | The closure from the 10 `sm` names over the split, without the docstring lines, has 71 names: 68 identical, these 3 differing, and no new block. `__all__`, `_selftest`, `example_cell` and the docstring lines are not reached. |
| R29 | §3: `check_record`'s diff | CONFIRMED | Verbatim `diff d5/check_record.txt d14/check_record.txt`. |
| R30 | §3: `SchemaError`'s diff | CONFIRMED | Verbatim. |
| R31 | §3: `check_cell`'s diff | CONFIRMED | Verbatim. |
| R32 | `check_cell`'s block differs only by the section comment that now follows it; its code is unchanged | CONFIRMED | 14e65d8, lines 990–993. |
| R33 | The `NESTED = {…}` literal is identical | CONFIRMED | As E27. |
| R34 | Its nine keys | CONFIRMED | 5a97527, lines 575–583. |
| R35 | 14e65d8 registers 18 more at import, in one loop, each to its report checker | CONFIRMED | Each tag gets its own closure over `_check_report_nested`. |
| R36 | The loop's code | CONFIRMED | Verbatim at 14e65d8, lines 1219–1224. |
| R37 | None of the 18 is one of the 9 | CONFIRMED | |
| R38 | §5: split.awk, whole | CONFIRMED | Diffed against `SCRATCH/pin/split.awk` (5 lines): empty. |
| R39 | §6: `git diff -- scripts/n_analyze.py` against 5c0ae6b, whole | CONFIRMED | Identical to the live diff. Its base blob, d1c3544, is 5c0ae6b's and HEAD's. |
| R40 | The committed file becomes sha256 `4f63903f…` | CONFIRMED | As E35. |
| R41 | §7: the battery ran at sha256 `4f63903f…` | UNVERIFIABLE | The output carries no digest; see E7. |
| R42 | §7: with the tree's `schema.py` at 14e65d8 | UNVERIFIABLE | As E7. |
| R43 | Run from the repository root | CONFIRMED | The INVOCATION line names the script by the relative path `scripts/n_analyze.py`. |
| R44 | At `nice -n 19` | UNVERIFIABLE | Not recorded anywhere. |
| R45 | Exit 0 | UNVERIFIABLE | As E38. |
| R46 | The repository root is shown as `<repo>` | CONFIRMED | pin1.out names the root literally, and the raw replaces it. |
| R47 | §7's output block | CONFIRMED | 173 lines, identical to pin1.out with the root replaced by `<repo>`: 171 PASS, 0 FAIL. |

#### Paths, user name and clock times

| ID | Claim | Status | How |
|---|---|---|---|
| X1 | Neither draft has a local path, the user name or a clock time beyond the `<repo>` form | CONFIRMED | I searched both drafts with `/usr/bin/grep` for home and tmp paths, the user name, "Documents", "scratchpad", `hh:mm`, AM/PM and time zones. The only hit is §7's INVOCATION line, `<repo>/jlens-qwen36/.venv/bin/python …`. Only calendar dates appear. |

#### Totals

The 92 claims are 44 in the entry, 47 in the raw and 1 across both drafts.

| Status | Entry | Raw | Both | Total |
|---|---|---|---|---|
| CONFIRMED | 32 | 36 | 1 | 69 |
| IMPRECISE | 4 | 3 | 0 | 7 |
| FAIL | 1 | 1 | 0 | 2 |
| UNVERIFIABLE | 7 | 7 | 0 | 14 |

#### FAILs and IMPRECISE items, most important first

1. **E26, FAIL** (entry, "What the analyzer reaches"). The analyzer's `sm.SchemaError` (docstring changed) and
   `sm.check_cell` (a comment attached after its code) are not identical, by the entry's own terms. Correction: "…is
   identical but for three blocks: `check_record` (its message), `SchemaError` (its docstring) and `check_cell` (the
   section comment that now follows its unchanged code); the raw's §3."
2. **R18, FAIL** (raw §2). The docstring lines the splitter counts as definitions are three, not two: `own:` is the
   one left out, at line 95 of 5a97527 and line 98 of 14e65d8. Correction as given in R18.
3. **E30, IMPRECISE** (entry, "This confirms … the list of changes n-build sent").
   - The split cannot see lines outside definitions.
   - n-build's list, as Code's SCRATCH/PLAN.md records it, includes the `json` import, which the raw never examines.
   - The module docstring's prose changes are also outside the split.
   - The list is right: the discarded lines differ only in docstring prose, `import json`, and the loop with
     `del _t`. Narrow the claim to the definition-level items and add that comparison to the raw.
4. **R16 and R4, IMPRECISE** (the raw's splitter description and its "every top-level definition … compared").
   - State that column-0 lines starting no definition are discarded, together with everything up to the next
     definition start, and are not compared. This covers the docstring prose, the imports, the tuple assignment
     `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = …` (unchanged, and reached through `shadow_read_id`), the loop with
     `del _t`, and the `__main__` block.
   - State that closing-bracket lines join.
   - Report the separate comparison.
5. **E16, IMPRECISE.** "77 definitions" means 75 definitions and two docstring lines. "32 new" means 31 definitions
   and `carries:`. The three-name tuple is outside the count.
6. **E32, IMPRECISE.** The section comment also takes the new sha prefix and gains the line "its record and cell
   checks as at 5a97527 but for check_record's rendering-mismatch message".
7. **E5, IMPRECISE.** "Four lines" should read "four lines rewritten as six" (six in, four out).
8. **R2, IMPRECISE.** The raw's quotation of the entry's title drops "from `5a97527`".

**A recommendation, not a status.** E7, E36, R41 and R42 are UNVERIFIABLE because pin1.out's 171 check lines and its
summary are byte-identical to the BUILD's run of record (`results/raw/2026-11-16_n-analyze_build_selftest.txt`). The
output cannot show which analyzer bytes or which schema ran. §7 could say so plainly, and name the digests Code took of
both files at the run, as Code's statement.

## 2. Code's dispositions of the first pass (every FAIL and IMPRECISE item)

| Item | Status | Disposition |
|---|---|---|
| E26 | FAIL | Accepted. The entry says what the analyzer reaches is identical but for three blocks: `check_record` (its message), `SchemaError` (its docstring) and `check_cell` (the section comment that now follows its unchanged code), as the raw's §3 shows. |
| R18 | FAIL | Accepted. §2 names three docstring lines the splitter takes for blocks (`schema:` and `own:` in both blobs, `carries:` in 14e65d8), and restates the counts: 77 blocks are 75 definitions and two docstring lines; 32 new blocks are 31 definitions and `carries:`. |
| E30 | IMPRECISE | Accepted, with an added comparison. §2b compares what the splitter discards: only docstring prose changes, and `import json` and the NESTED registration loop are added. The entry's confirmation now names the definitions and the `import json` of n-build's list. A whole-file diff, as a check, keeps all but 10 of 5a97527's lines, each accounted for. |
| R16, R4 | IMPRECISE | Accepted. §2 says what the splitter discards, naming the tuple line `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = …`, and that a line starting with `)`, `]` or `}` joins the block before it. §2b compares the discarded parts. |
| E16 | IMPRECISE | Accepted (with R18): 75 definitions and two docstring lines; 31 new definitions and `carries:`. |
| E32 | IMPRECISE | Accepted. The entry says the section comment takes 14e65d8's commit and sha256 and gains a line on the record and cell checks. |
| E5 | IMPRECISE | Accepted: "four lines rewritten as six". |
| R2 | IMPRECISE | Accepted. The raw quotes the entry's title whole: "moved from 5a97527 to 14e65d8". |
| Recommendation (§7) | — | Accepted. §7 says the battery prints no hash and its output is line for line the BUILD's run of record. It passes only if the tree's `schema.py` hashes to the analyzer's pin, and the command that ran it hashed both files first, to the session's output. |
| The checker's departures | — | Noted, all read-only. Beyond the brief's list it used `cat` (once), a rejected `cat -A` with `head`, `tr`, `tail -1`, `uniq -d`, `git hash-object` on the analyzer, and two `git grep`s (one with `':!data/**'`, one on two named paths). It also used `git ls-files results/raw`, a status scoped to four named paths, `git diff --quiet`, `git diff --stat`/`--numstat` on the two code files only, and one recursive grep over SCRATCH. It edited nothing, ran no Python, and touched nothing under `data/`. |

## 3. The second pass: the checker's report, whole

### Blind values-check, second pass: the schema pin move (entry, raw, values-check raw)

PI date 2026-11-16. SCRATCH is the author's scratch folder (the `n9` folder); REPO is the repository checkout
(branch `main`, HEAD `14e65d8`). I edited nothing in REPO or SCRATCH; this report is the only file written.

Drafts checked:

1. `SCRATCH/pin/pin_entry.md`: the RESULTS.md entry (E-rows).
2. `SCRATCH/pin/2026-11-16_n-analyze_pin-move.md`: the raw (R-rows).
3. `SCRATCH/pin/2026-11-16_n-analyze_pin-move_valuescheck.md`: the values-check raw (V-rows, then the dispositions,
   D-rows), checked last.

#### Tools

**Within the brief:** the Read tool; `shasum -a 256`; `/usr/bin/grep`; `awk` (inline programs, and `awk -f
SCRATCH/pin/discarded.awk`, which prints to stdout only); `sed -n` printing; `diff`; `cmp`; `comm`; `sort`; `wc -l`;
name-only `ls`; `git log`, `git show` (incl. `--name-status`), `git rev-parse`, `git diff` (incl. `--numstat` and
`--quiet`, on `valence_core/n/schema.py`, `scripts/n_analyze.py` and `RESULTS.md` only).

**Beyond the brief's list (all read-only, stdout only):**

- `tr -d ' '`, once, in a pipe counting a diff's non-comment lines;
- `uniq -c`, once, tallying the analyzer's `sm.<name>` uses;
- `sed` with substitution expressions (`s/^=== //`, `s/\.txt$//`, `s/^[<>] \{0,1\}//`) as stdout filters in two
  commands, never `-i`;
- `git hash-object scripts/n_analyze.py`, once (a digest; I printed its first 7 characters);
- `git status --porcelain`, once, scoped to five named paths (`valence_core/n/schema.py`, `scripts/n_analyze.py`,
  `RESULTS.md` and the two raws' future `results/raw/` paths);
- shell builtins and syntax: `cd`, `echo`, `for`, `while read`, `if` / `[ ]`, process substitution, `2>/dev/null`, and
  awk's print to `/dev/stderr`.

**What I did not do.** No Python of any kind and no interpreter but awk; nothing in the background; no temporary
file (pipes and process substitution only); `split.awk` was never run (I rewrote its rules to print to stdout); nothing
under `data/` was listed, read, stat'ed or searched, and `data/mf3` was not touched; no whole-tree status.

#### How the checks were made

- **Hashes and ids.** `git rev-parse` of the three commits; `git show <c>:valence_core/n/schema.py | shasum -a 256`
  at 5a97527, 5c0ae6b, 14e65d8; `shasum` of the tree's `schema.py` and `scripts/n_analyze.py`, of
  `git show HEAD:` / `5c0ae6b:scripts/n_analyze.py`, and of `SCRATCH/pin/schema_5a97527.py` and
  `schema_14e65d8.py` (also `cmp` against the blobs).
- **The split.** split.awk's four rules as a stdout program on each blob, against the d5/d14 files concatenated in the
  same order: identical, 77 and 109 blocks, 77 and 109 files, no name twice, no stray file. Block lines plus discarded
  lines equal the blob: 1201 + 139 = 1340 and 1957 + 188 = 2145.
- **The comparisons.** `cmp` of every shared pair; a block whose diff lines are all blank or comments counts as
  "comment or blank lines only"; §2's 77 table rows rebuilt from that and the analyzer's `sm` set, then `diff`ed against
  the raw's rows.
- **What the analyzer reaches.** Every `sm.<name>` in the tree's analyzer; every bare use of `sm` (it is bound only to
  `schema_module()`'s return, at lines 1943, 2525 and 3110, and passed on as `sm`); identifier tokens of `check_cell`
  and `check_record` intersected with the block names in both blobs; a conservative transitive closure from the 10
  `sm` names over d14 (every identifier token naming a block, iterated; the three docstring blocks excluded).
- **The discarded parts.** `awk -f discarded.awk` on each blob, with and without its `@@` lines, against `disc5.txt`,
  `disc14.txt` and `disc_diff.txt`; the whole-file `diff` and `git diff --numstat` of the two blobs.
- **§3–§7.** Each code block `diff`ed against its source (block diffs; the 14e65d8 blob; `split.awk`;
  `discarded.awk`; the live `git diff -- scripts/n_analyze.py`; `SCRATCH/runs/pin1.out` with the repository root
  replaced by `<repo>`); `pin1.out` against `SCRATCH/runs/record3.out` and the committed
  `results/raw/2026-11-16_n-analyze_build_selftest.txt`.
- **Records.** RESULTS.md at HEAD (unmodified: `git diff --quiet HEAD`), the 14e65d8 and 5c0ae6b entries;
  `SCRATCH/PLAN.md` ("Schema pin move", "Commit order"); `SCRATCH/pin/assemble.sh` and `commit_steps.sh`.

#### Draft 1: the entry (`SCRATCH/pin/pin_entry.md`)

| ID | Claim (entry line) | Status | How / correction |
|---|---|---|---|
| E1 | Date 2026-11-16 (l.1) | CONFIRMED | A calendar date only; the raws carry the same PI date. |
| E2 | The pin moved from 5a97527 to 14e65d8 (l.1) | CONFIRMED | Live `git diff`: `SCHEMA_SHA256` 77c12d6d…94bc `# 5a97527` → 4bed3f9a…4665 `# 14e65d8`. |
| E3 | n-build's schema commit changed the file the analyzer pins (l.1–2) | CONFIRMED | `git show --name-status 14e65d8`: M `valence_core/n/schema.py`, the analyzer's `SCHEMA_REL`. |
| E4 | The coordinating session's order: BUILD 5c0ae6b, then the schema, then this (l.2–3) | CONFIRMED, as recorded | 5c0ae6b's committed entry: "n-build's schema commit, which the coordinating session orders after this one … The pin then moves in its own entry". SCRATCH/PLAN.md, "Commit order (coordinating session, 2026-11-16)", items 1–3. 14e65d8's parent is 5c0ae6b. The coordinating session's own words are in no file. |
| E5 | "Four lines rewritten as six" (l.3) | CONFIRMED | Four hunks: −1 +2, −1 +1, −1 +1, −1 +2; `--numstat` 6 4. |
| E6 | Battery 171/171 (l.3) | CONFIRMED | pin1.out: 171 `[PASS]` lines, no `FAIL]`, last line "171/171 n_analyze battery checks pass". |
| E7 | "against the new schema" (l.3) | UNVERIFIABLE | pin1.out is byte-identical to record3.out (the BUILD's run against 5a97527) and prints no digest of the analyzer or schema, so it cannot show which pair ran. Consistent with the code (R57). |
| E8 | Model-free: nothing ran on a model or on the box (l.3–4) | UNVERIFIABLE | An activity claim. pin1.out's checks "no model library is imported by the battery …" and "module-level imports are numpy and the standard library only" pass. |
| E9 | The analyzer at 5c0ae6b refuses any `schema.py` but 5a97527's bytes, sha256 77c12d6d…94bc (l.5–6) | CONFIRMED | `git show 5c0ae6b:scripts/n_analyze.py`: `SCHEMA_SHA256 = "77c12d6d…94bc"` (l.1852); `schema_module` raises `AnlRefusal` when the file's sha256 differs (l.1874–1876). The blob hashes to 77c12d6d…94bc at 5a97527 and 5c0ae6b. |
| E10 | n-build's 14e65d8 changed it to sha256 4bed3f9a…4665 (l.6) | CONFIRMED | Hash of the 14e65d8 blob. "n-build's" as 5c0ae6b's entry names the commit. |
| E11 | So from that commit the reader and battery refused (l.6–7) | CONFIRMED, by the code | `load_campaign` (`sm = sm or schema_module()`), `_bt_reader` and `_bt_commands` call `schema_module()`; 5c0ae6b's entry says `--selftest` fails and `ganl` stops. No refusing run is recorded, and none is claimed. |
| E12 | The raw (link) holds the check, §1–§5 (l.8–9) | CONFIRMED | The link's file name is the scratch draft's; its §1–§5 (with §2b) are the check. Not yet in REPO's `results/raw` (no name there contains `n-analyze_pin-move`). |
| E13 | Code verified the commit and the blob (§1) (l.10) | CONFIRMED | Every §1 value holds (R8–R12, R14). |
| E14 | Both blobs split, from `git show`, into top-level blocks by a short awk script (l.10–11) | CONFIRMED | The scratch copies are byte-identical to the blobs; d5/d14 are exactly split.awk's split (see "How"). |
| E15 | Each pair present in both compared with `cmp` (§2) (l.11–12) | CONFIRMED | My `cmp` of the 77 shared pairs: 70 identical, 2 comment/blank only, 5 changed. |
| E16 | "What the splitter discards (imports, the module docstring's prose, a tuple line, a loop) it compared separately (§2b)" (l.12–13) | IMPRECISE | The comparison covers all of it, but the list omits `del _t` (14e65d8 l.1224) and the `if __name__ == "__main__":` block (5a97527 l.1335, 14e65d8 l.2140; identical), both discarded. Correction: "(the module docstring's prose, the imports, a tuple line, the NESTED loop with `del _t`, and the `__main__` block)". |
| E17 | 5a97527's 77 blocks = 75 definitions and two docstring lines (l.14) | CONFIRMED | The only block starts that are not `def`/`class`/assignments: `schema:` (l.6) and `own:` (l.95). |
| E18 | None is gone (l.14) | CONFIRMED | `comm`: no name only in d5. |
| E19 | 70 are identical (l.14) | CONFIRMED | `cmp`. |
| E20 | Two differ in comment or blank lines only (`check_cell`, `example_cell`) (l.14–15) | CONFIRMED | `check_cell`: `30a31` adds "# --- the stage report …"; `example_cell`: `12,13d11` drops "# --- self-test …" and a blank line. |
| E21 | Five changed (l.15) | CONFIRMED | `check_record`, `SchemaError`, `__all__`, `_selftest`, `schema`. |
| E22 | `check_record`: one refusal message (l.16) | CONFIRMED | Block diff `112c112,113`: one `_fail` message; the condition is untouched. |
| E23 | Quote: "is never a record (a pause during a stage; a G-VER-STOP at G-VER)" (l.16–17) | CONFIRMED | 14e65d8's two adjacent literals concatenate to exactly this after "a rendering mismatch ". |
| E24 | Quote: where it "is a STOP" (l.17) | CONFIRMED | 5a97527: "…a rendering mismatch is a STOP, never a record". |
| E25 | `SchemaError`: its docstring (l.18) | CONFIRMED | Block diff `2,3c2,3`, the docstring's two lines. |
| E26 | `__all__`, n-build's `_selftest`, and a docstring line the splitter takes for a block (l.19) | CONFIRMED | `__all__` `10a11,15` (+5); `_selftest` `286a287,488` (+202, −0); `schema:` `1c1`. |
| E27 | Everything it calls (`sm.<name>`) and everything `check_cell` and `check_record` reference by name is identical but for three blocks (l.20–21) | CONFIRMED | `sm` set: CELL_SCHEMA, SchemaError, TOLD_LINE, cell_filename, check_cell, dose_point_values, dose_points, example_identity, example_record, read_plan. With check_cell's 8 and check_record's 23 names, all identical but SchemaError, check_cell, check_record. The transitive closure from the 10 names reaches 71 blocks: 68 identical, these 3, no new block. |
| E28 | The three: `check_record` its message; `SchemaError` its docstring; `check_cell` the section comment after its unchanged code (l.22–24) | CONFIRMED | Block diffs; at 14e65d8 check_cell's code is l.963–990, the comment l.993. |
| E29 | "These are the raw's §3." (l.26) | CONFIRMED | §3 shows exactly these three. |
| E30 | `NESTED`'s literal is identical (l.26) | CONFIRMED | `cmp` of the NESTED blocks (5a97527 l.574, 14e65d8 l.653). |
| E31 | 14e65d8 registers 18 new keys in it, none of its 9 old ones (l.26–27) | CONFIRMED | The loop at 14e65d8 l.1219–1224 names 18 tags; 0 in common with the literal's 9 keys; no other assignment into NESTED in either blob; none of the 18 occurs as a quoted string in 5a97527. |
| E32 | "Of the 32 new blocks (31 definitions and a docstring line)" (l.27) | IMPRECISE | The counts hold, but the `carries` block is not a line: it is 38 lines of the module docstring (14e65d8 l.133–170, the stage report's list of what it carries). Correction: "(31 definitions and `carries:`, a 38-line docstring passage, the stage report's list)". |
| E33 | …the analyzer calls none (l.27) | CONFIRMED | None of the 32 is an `sm` name, and the closure reaches none. |
| E34 | What the splitter discards changes only in docstring prose (l.28) | CONFIRMED | `disc_diff.txt`: the 6 removed lines and every rewritten or added line but `import json`, the loop, `del _t` and two blank lines are module-docstring prose. |
| E35 | It gains `import json`, which only new code uses (l.28–29) | CONFIRMED | `json.` occurs in d14 only in `identity_sha256` (new), `_selftest` (only in its added lines: d5's `_selftest` has none) and a string of RECORD_FIELDS (also in 5a97527). |
| E36 | …and the loop that registers NESTED's new keys (l.29) | CONFIRMED | Hunk `133a175,182`. |
| E37 | "This confirms, for the committed bytes, the list of changes n-build sent before its commit: the definitions, and its `import json`." (l.30–31) | UNVERIFIABLE | n-build's message is in no file. Against Code's note of it (SCRATCH/PLAN.md, "Schema pin move") and n-build's committed entry (14e65d8, "What changed"), every definition-level item and `import json` hold at the committed bytes; `check_cell`, called byte-identical there, is so as a definition (its block gains only the following comment). The PLAN.md note does not name `_selftest`'s 202 added lines or the docstring prose; the committed entry does. |
| E38 | `SCHEMA_SHA256` to 4bed3f9a…4665 (l.33) | CONFIRMED | Live diff, hunk 2. |
| E39 | Its section comment to 14e65d8's commit and sha256, with a new line noting the record and cell checks are as at 5a97527 but for check_record's message (l.34–35) | CONFIRMED | Hunk 1. The note begins on the rewritten line ("its record and") and ends on the new one; it is true (E28). |
| E40 | `schema_module`'s docstring to 14e65d8 (l.36) | CONFIRMED | Hunk 3. |
| E41 | `counters`' docstring now quotes check_record's new wording (l.37) | CONFIRMED | Hunk 4 quotes "a rendering mismatch is never a record (a pause during a stage; a G-VER-STOP at G-VER)", a verbatim substring of the message, wrapped after "a". No stale wording remains in the analyzer. |
| E42 | Six lines in, four out (l.39) | CONFIRMED | `--numstat` 6 4. |
| E43 | `scripts/n_analyze.py` becomes sha256 4f63903f161885a8bb16ea933157d6e0e609e3cfa91503ac3ef68b1af23c5d73 (l.39) | CONFIRMED | Hash of the tree's file (blob c5efdf0, the diff's index line). |
| E44 | The battery against the tree's `schema.py` at 14e65d8 (l.40) | UNVERIFIABLE | As E7. |
| E45 | 171/171, every one of the 172 coverage ids reached (l.40) | CONFIRMED | pin1.out: "coverage: every one of the 172 required ids reached", "check count 171 == EXPECTED_CHECKS 171", "171/171 …". |
| E46 | Exit 0 (l.41) | UNVERIFIABLE | No file records it. Implied by `main`'s `return 0 if battery()["ok"] else 1` given the printed lines (ok = all pass, count 171, nothing unreached). |
| E47 | It ran in a window the coordinating session granted, one process at `nice -n 19`, in the foreground (l.41–42) | UNVERIFIABLE | No file records the grant or the invocation's niceness. PLAN.md states the rule only ("Every Python run needs a window …; nice -n 19"). |
| E48 | No other Python ran for this step (l.42) | UNVERIFIABLE | A negative activity claim. |
| E49 | Values-check: one blind pass over this entry and the raw (l.43) | CONFIRMED | `SCRATCH/vc/pin_report.md`, "Drafts checked": the entry and the raw. |
| E50 | (a subagent, under a brief quoting the list of record v2's items 1–5, no Python) (l.43) | UNVERIFIABLE | The brief is in no file; the report says it ran no Python. |
| E51 | 92 claims, 69 CONFIRMED, 7 IMPRECISE, 2 FAIL, 14 UNVERIFIABLE (l.43) | CONFIRMED | The report's totals; my tally of its 92 table rows agrees (entry 32/4/1/7, raw 36/3/1/7, X1). |
| E52 | Every item accepted, as text, with one comparison added to the raw (§2b) (l.43) | CONFIRMED | Draft 3 §2: every FAIL and IMPRECISE item and the recommendation "Accepted"; no code change (the analyzer's diff is the one the first pass checked, E35 there). §2b also holds the whole-file diff, framed as a check. |
| E53 | The values-check raw holds the report whole and every disposition (l.43) | CONFIRMED | V5, V7. |
| E54 | Committed by path: the analyzer, the raw, the values-check raw, this entry. Not pushed (l.44) | UNVERIFIABLE | The coming commit. Consistent with `SCRATCH/pin/commit_steps.sh`'s gate (the four paths' status). |
| E55 | Next: the `verdicts` command, in a BUILD of its own (l.45) | CONFIRMED, as planned | 5c0ae6b's entry: "It is built after n-build commits its stage-report and G-READ-n forms, in an entry of its own". |
| E56 | The forms are committed (n-report-v1 and n-gread-v1, at 14e65d8) (l.45–46) | CONFIRMED | 14e65d8 blob l.994–995: `REPORT_SCHEMA = "n-report-v1"`, `GREAD_SCHEMA = "n-gread-v1"`. |
| E57 | G-ANL-n's canonical run waits for the seat's answers and G-CAL-n's dose map (l.46–47) | CONFIRMED, as recorded | 5c0ae6b's entry; no later entry records either. |

#### Draft 2: the raw (`SCRATCH/pin/2026-11-16_n-analyze_pin-move.md`)

The raw is exactly what `assemble.sh` builds: lines 1–21 its header and §1, then `check_part.md` (l.22–108),
`check_part2b.md` (l.110–131) and `check_part2.md` (l.133–188), each `diff`-identical, then §6 and §7.

| ID | Claim | Status | How / correction |
|---|---|---|---|
| R1 | Title: the pin moved from 5a97527 to 14e65d8 (PI date 2026-11-16) | CONFIRMED | As E2; a calendar date. |
| R2 | Quotes the entry `n package — scripts/n_analyze.py, the schema pin moved from 5a97527 to 14e65d8` | CONFIRMED | Identical, em dash included, to the entry's headline words with its code backticks removed. |
| R3 | 14e65d8 changed `schema.py`, which the analyzer committed at 5c0ae6b pins by sha256 and refuses otherwise | CONFIRMED | As E9–E10. |
| R4 | The section list (§1, §2, §2b, §3–§7) | CONFIRMED | Headings at l.17, 22, 110, 133, 165, 180, 190, 239. |
| R5 | Every block of the two blobs compared (§2), and what the splitter discards compared (§2b) | CONFIRMED | 77 shared blocks compared, the 32 new listed; §2b compares every discarded line. |
| R6 | "Nothing ran on a model or on the box." | UNVERIFIABLE | As E8. |
| R7 | The one Python process was the battery, in a granted window, at `nice -n 19`, in the foreground | UNVERIFIABLE | As E47–E48. |
| R8 | 14e65d8 = `14e65d812fe5e1a1e311150c7e1bf0d31b745899` | CONFIRMED | `git rev-parse`. |
| R9 | Parent `5c0ae6b` | CONFIRMED | `git log --format=%P`: 5c0ae6b18c48…. |
| R10 | Paths: M `RESULTS.md`; A `results/raw/2026-11-16_n-schema-v2_valuescheck.md`; M `valence_core/n/schema.py` | CONFIRMED | `git show --name-status 14e65d8`. |
| R11 | Blob sha256 at 5a97527 `77c12d6d0e7eee370291e0f5e587204f4ae613c65ce57f95c336f507273494bc` | CONFIRMED | Hash of the blob (same at 5c0ae6b). |
| R12 | At 14e65d8 `4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665` | CONFIRMED | Hash of the blob. |
| R13 | "(n-build's message gave `4bed3f9a…4665`, full)" | UNVERIFIABLE | The message is in no file; the value is a literal typed into `assemble.sh`, not derived. The same full value appears twice in n-build's committed `results/raw/2026-11-16_n-schema-v2_valuescheck.md`; 14e65d8's commit message gives `4bed3f9a...4665`. |
| R14 | The tree's file `4bed3f9a…4665` | CONFIRMED | Hash of the file; the scoped status lists `schema.py` unmodified. |
| R15 | Each blob split at its top-level lines by `split.awk` (§5) | CONFIRMED | As E14. |
| R16 | The splitter's rules: `def`/`class NAME`, `NAME =`, `NAME:` at column 0 start a block that runs to the next top-level line; a top-level comment and `)`, `]`, `}` lines join the block before them; any other top-level line is discarded with what follows it | CONFIRMED | Matches split.awk's four rules. A column-0 comment or bracket after a discarded line is discarded with it; no such line occurs in either blob's discarded parts. |
| R17 | "Three blocks are lines of the module docstring that begin with a word and a colon at column 0: `schema:` and `own:` in both blobs, and `carries:` in 14e65d8." | IMPRECISE | Names and places hold (l.6 and l.95 in 5a97527; l.6, l.98, l.133 in 14e65d8), but the blocks run past those lines: `own:` is 2 lines (with a blank), and `carries:` is 38 lines, the stage report's list of what it carries, so that part of the new docstring sits in §2's new blocks, not in §2b. Correction: "Three blocks are module-docstring text, each headed by a line that begins with a word and a colon at column 0: `schema:` (1 line) and `own:` (2) in both blobs, and `carries:` in 14e65d8 (38 lines, the stage report's list of what it carries)." |
| R18 | 77 blocks = 75 definitions + two docstring lines; 32 new = 31 definitions + `carries:` | CONFIRMED | As E17 and E32 (counts). |
| R19 | §2's table: 77 rows, each status | CONFIRMED | Rebuilt independently (C-locale order); `diff` with l.28–104 is empty. |
| R20 | The "analyzer calls it" column (10 names) | CONFIRMED | Equals the `sm` set (E27). |
| R21 | `check_cell` references CELL_FIELDS, CELL_SCHEMA, _check_table, _fail, cell_filename, check_record, check_stage_identity, read_id | CONFIRMED | Its identifiers ∩ block names, in both blobs (plus `schema`, in strings). |
| R22 | `check_record` references the 23 names listed | CONFIRMED | Same method, both blobs (plus `own`, `schema`, and in 14e65d8 `carries`, in strings). |
| R23 | `schema`, `own` and `carries` match only inside their strings | CONFIRMED | `rec["schema"]`, `w("schema")`, `f"{where}.schema"`; "…whose sequence is its own"; "…carries a direction…" and two more messages. |
| R24 | Each is identical, but `check_record` (the message in §3) | CONFIRMED | `cmp` of all 28 distinct names: only `check_record` differs. |
| R25 | `_check_table` dispatches through `_check_type` and `NESTED`, both identical; NESTED's new keys none of its old | CONFIRMED | `_check_table`'s `if t in NESTED … else _check_type(…)`; both blocks identical; E31. |
| R26 | The 32 names new in 14e65d8 | CONFIRMED | Equal, as a set, to `comm -13` of d5 and d14 (32). |
| R27 | None called by the analyzer | CONFIRMED | As E33. |
| R28 | `discarded.awk` prints what `split.awk` discards, by the same rules | CONFIRMED | Exact complement on both blobs (line sums above); it also prints an `@@ NR` header per discarded run, as its comment says. |
| R29 | "Its output for the two blobs (139 and 188 lines) was compared with `diff`: 6 hunks." | IMPRECISE | Run as shown, `discarded.awk` prints 248 and 314 lines (109 and 126 `@@` headers), and `diff` of those outputs has 104 hunks (109 lines removed, 175 added), because the headers' line numbers shift. The 139 / 188 lines and the 6 hunks are of the output without its `@@` lines (`disc5.txt`, `disc14.txt`, `disc_diff.txt`), a step the raw does not show. Correction: "Its output for the two blobs, without its `@@` header lines (139 and 188 lines; 248 and 314 with them), was compared with `diff`: 6 hunks." |
| R30 | Removed or changed from 5a97527: 6 lines, all module-docstring prose | CONFIRMED | `disc_diff.txt`: 6 `<` lines (blob l.1, 7, 16, 17, 126, 127), all inside the docstring (it ends at l.128). |
| R31 | "Added in 14e65d8: prose of the module docstring (the stage report's and G-READ-n's specifications, and the examples' list), `import json`, and the loop that registers NESTED's 18 new keys, with `del _t` (§4)." | IMPRECISE | The 55 added lines are: three rewritten passages (7 lines: the first line, now "first committed at `5a97527`"; the end of the `schema:` sentence, now two lines; the sentence on the other records, now four lines, naming the report and G-READ-n's artifact and adding where a NOT-RUN is recorded); 39 lines in place of the old 2-line EXAMPLES paragraph (the stage report's opening and its end-state rules, G-READ-n's artifact, the PASS-rule paragraph, a new 3-line EXAMPLES paragraph, and 3 blank lines); `import json`; the loop (5 lines), `del _t` and 2 blank lines. The parenthetical omits the NOT-RUN sentence and the PASS rule, and "the stage report's specification" is only partly here: its `carries:` list is §2's new block. Correction: "Added in 14e65d8: the rewritten passages' new text (the first line; the `schema:` sentence's end; the sentence on the other records, now naming the report and G-READ-n's artifact and where a NOT-RUN is recorded; the EXAMPLES paragraph), new docstring prose (the stage report's specification but its `carries:` list, which §2 counts as a block, and G-READ-n's, with its PASS rule), `import json`, and the loop … with `del _t` (§4)." |
| R32 | Unchanged: the rest, among it `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = "N1-V", "none", "0"` | CONFIRMED | Verbatim at 5a97527 l.200 and 14e65d8 l.279; no hunk touches the rest; the `__main__` blocks are identical. |
| R33 | A whole-file `diff` keeps all but 10 of 5a97527's lines: seven of the docstring (one the `schema:` line), two of SchemaError's docstring, check_record's message | CONFIRMED | `diff` and `git diff`: 10 removed, at l.1, 6, 7, 16, 17, 126, 127 (docstring; l.6 is `schema:`), 209–210 (SchemaError), 796 (check_record); 1330 of 1340 kept. |
| R34 | Everything else in the diff is added | CONFIRMED | 815 added (`--numstat` 815 10). |
| R35 | The `discarded.awk` listing | CONFIRMED | `diff` with `SCRATCH/pin/discarded.awk` (6 lines): empty. |
| R36 | §3: the three blocks the analyzer can reach that differ | CONFIRMED | The closure (E27): exactly these three. |
| R37 | §3 `check_record` diff | CONFIRMED | Verbatim `diff d5/check_record.txt d14/check_record.txt`. |
| R38 | §3 `SchemaError` diff | CONFIRMED | Verbatim. |
| R39 | §3 `check_cell` diff | CONFIRMED | Verbatim. |
| R40 | check_cell's block differs only by the top-level section comment that now follows it; its code is unchanged | CONFIRMED | 14e65d8 l.963–993; the comment at l.993 is followed by `REPORT_SCHEMA = …`. |
| R41 | §4: the `NESTED = {…}` literal is identical | CONFIRMED | As E30. |
| R42 | §4: its nine keys | CONFIRMED | The literal holds exactly these 9 (listed sorted; the literal's own order differs, and no order is claimed). |
| R43 | §4: 14e65d8 registers 18 more at import, in one loop, each to its report checker | CONFIRMED | Each tag gets its own closure over `_check_report_nested`. |
| R44 | §4: the loop's code | CONFIRMED | Verbatim at 14e65d8 l.1219–1224. |
| R45 | §4: none of the 18 is one of the 9 | CONFIRMED | `comm`: 0 in common. |
| R46 | §5: `split.awk`, whole | CONFIRMED | `diff` with `SCRATCH/pin/split.awk` (5 lines): empty. |
| R47 | §6: `git diff -- scripts/n_analyze.py` against 5c0ae6b, whole | CONFIRMED | Identical to the live diff; its base blob d1c3544 is the analyzer at 5c0ae6b and at HEAD. |
| R48 | §6: the committed file becomes sha256 4f63903f…5d73 | CONFIRMED | As E43. |
| R49 | §7: the battery ran at sha256 4f63903f… | UNVERIFIABLE | The output carries no analyzer digest (E7); `assemble.sh` fills the value from the tree's file at assembly. |
| R50 | §7: with the tree's `schema.py` at 14e65d8 | UNVERIFIABLE | As E7. |
| R51 | §7: run from the repository root | UNVERIFIABLE | Consistent: the INVOCATION line runs `scripts/n_analyze.py` by a relative path with the interpreter under `<repo>`; the working directory is not printed (REPO is derived from `__file__`). |
| R52 | §7: at `nice -n 19` | UNVERIFIABLE | Not recorded. |
| R53 | §7: exit 0 (the runner printed it to the session) | UNVERIFIABLE | As E46. |
| R54 | §7: the repository root is shown as `<repo>` | CONFIRMED | pin1.out names the root literally; the block replaces it. |
| R55 | §7: "The battery prints no hash" | IMPRECISE | It prints one: "[PASS] proposal: PROPOSAL-n v0.2's sha256 is the pinned 30a3d0f5...04f4" (pin1.out l.163). It prints no digest of the analyzer or the schema, which is the point. Correction: "The battery prints no hash of the analyzer or the schema (its one digest is the proposal's pinned `30a3d0f5...04f4`)". |
| R56 | §7: its output is line for line that of the BUILD's run of record against 5a97527 | CONFIRMED | pin1.out is byte-identical to record3.out (173 lines) and, with the root as `<repo>`, to l.2–174 of the committed `results/raw/2026-11-16_n-analyze_build_selftest.txt`; that run's analyzer (2598908d…) pins 77c12d6d…, 5a97527's schema. |
| R57 | §7: it passes only if the tree's `schema.py` hashes to the analyzer's pin, since `schema_module` refuses otherwise | CONFIRMED, by the code | A refusal in `_bt_reader` or `_bt_commands` is caught by `_Battery.group`, which prints a "group raised" FAIL line, so 171/171 with every coverage id cannot follow a refusal. |
| R58 | §7: the command hashed both files first, to the §1 and §6 values, to the session's output | UNVERIFIABLE | In no file. |
| R59 | §7's output block | CONFIRMED | `diff` of l.249–421 with pin1.out (root as `<repo>`): empty; 173 lines, 171 PASS, 0 FAIL. |

#### Draft 3: the values-check raw (`SCRATCH/pin/2026-11-16_n-analyze_pin-move_valuescheck.md`)

| ID | Claim | Status | How |
|---|---|---|---|
| V1 | Title, PI date 2026-11-16 | CONFIRMED | A calendar date. |
| V2 | "Code's raw for the entry `n package — …`" | CONFIRMED | The same string as R2. |
| V3 | The checker was a subagent of this session, under a brief quoting the list of record v2's items 1–5, allowing no Python | UNVERIFIABLE | The brief is in no file; the report's Tools section has a "Within the brief" list and "I ran no Python". |
| V4 | It checked the entry and the pin-move raw, claim by claim | CONFIRMED | The report's "Drafts checked" and its 92 rows. |
| V5 | §1 is the report, whole, its headings demoted two levels | CONFIRMED | l.11–298 equal `SCRATCH/vc/pin_report.md` (288 lines) with `##` prefixed to each of its 9 heading lines (`diff` empty; the report has no code fences). |
| V6 | The checker writes SCRATCH and REPO for the two roots | CONFIRMED | The report's second paragraph. |
| V7 | §2 disposes of every FAIL and IMPRECISE item | CONFIRMED | E26 and R18 (FAIL); E5, E16, E30, E32, R2, R4, R16 (IMPRECISE): all nine are disposed of, R16 and R4 in one row. |

**The dispositions, carried into drafts 1 and 2?**

| ID | Item | Carried | Evidence |
|---|---|---|---|
| D1 | E26 (FAIL): "identical but for three blocks" | APPLIED | Entry l.20–24, in the checker's terms. |
| D2 | R18 (FAIL): three docstring lines; 75 + 2 and 31 + `carries:` | APPLIED | Raw §2 (l.24). See R17 for the word "lines". |
| D3 | E30: §2b comparison, the entry names the definitions and `import json`, the whole-file diff as a check | APPLIED | Raw §2b (l.110–131); entry l.28–31. Not in the checker's wording ("the definition-level items of the list…"), but the narrowing is made. |
| D4 | R16, R4: what the splitter discards, the tuple line, closing brackets join; §2b | APPLIED | Raw l.7 ("every block … and what the splitter discards, compared") and l.24. The `__main__` block, named in the checker's R16, is covered only by "Any other top-level line" (the entry's own list, E16, omits it). |
| D5 | E16: 75 + 2 and 31 + `carries:` | APPLIED | Entry l.14 and l.27 (see E32 for "a docstring line"). |
| D6 | E32: the section comment's commit, sha256 and new line | APPLIED | Entry l.34–35. |
| D7 | E5: "four lines rewritten as six" | APPLIED | Entry l.3. |
| D8 | R2: the title quoted whole, "moved from 5a97527 to 14e65d8" | APPLIED | Raw l.3 (also draft 3 l.3); the quote drops the entry's code backticks, the short form the checker allowed. |
| D9 | The recommendation (§7) | APPLIED | Raw l.243–246. Its "prints no hash" needs R55's correction. |
| D10 | The checker's departures, noted | N/A (a note) | Its account matches the report's Tools section item by item; "a rejected `cat -A` with `head`" is one reading of the report's "`head`, once, in that same pipe". Nothing was due in drafts 1–2. |

#### Paths, user name, clock times

| ID | Claim | Status | How |
|---|---|---|---|
| X1 | No draft has a local path, the user name, a pod address or port, or a clock time beyond the `<repo>` form | CONFIRMED | `/usr/bin/grep` of the three drafts for home and tmp roots, the user name, "Documents", "scratchpad", `~/`, IP-like strings, `hh:mm`, AM/PM, time zones and time-of-day words. The only hits are draft 3's X1 row naming those search terms. The dates are 2026-11-16 throughout and 2026-12-15 inside §7's battery lines. |

#### Observations (no status)

- The entry's values-check line reports one pass. If this pass is cited, the line needs a second pass, and the
  values-check raw a second report and its dispositions.
- The full digest that R13 says "n-build's message gave" is a literal typed into `assemble.sh`. The committed record
  that carries it is n-build's values-check raw; the commit message has the short form. Citing those instead would make
  it checkable.
- The exit status of §7's run is in no file (E46, R53). A one-line exit record beside `SCRATCH/runs/pin1.out` would
  make it checkable next time.
- `SCRATCH/pin/commit_steps.sh`'s header comment still says "The n_analyze.py BUILD commit". It is a scratch script,
  not a draft.

#### Totals

124 claims: 57 in the entry, 59 in the raw, 7 in the values-check raw and 1 across the drafts.

| Status | Entry | Raw | VC raw | Across | Total |
|---|---|---|---|---|---|
| CONFIRMED | 46 | 46 | 6 | 1 | 99 |
| IMPRECISE | 2 | 4 | 0 | 0 | 6 |
| FAIL | 0 | 0 | 0 | 0 | 0 |
| UNVERIFIABLE | 9 | 9 | 1 | 0 | 19 |

Dispositions (draft 3 §2): 9 APPLIED, 0 PARTLY, 0 NOT APPLIED, 1 N/A (the note on the checker's departures).

#### IMPRECISE items, most important first (no FAIL)

1. **R29** (raw §2b). The counts and hunks are of `discarded.awk`'s output without its `@@` lines: run as shown, it
   prints 248 and 314 lines and their `diff` has 104 hunks. Correction: "Its output for the two blobs, without its
   `@@` header lines (139 and 188 lines; 248 and 314 with them), was compared with `diff`: 6 hunks."
2. **R55** (raw §7). "The battery prints no hash" is literally untrue: it prints the proposal's pinned
   `30a3d0f5...04f4`. Correction: "The battery prints no hash of the analyzer or the schema (its one digest is the
   proposal's pinned `30a3d0f5...04f4`)".
3. **R31** (raw §2b, "Added in 14e65d8"). The list omits the rewritten passages' new text, including the new NOT-RUN
   sentence, and the PASS-rule paragraph. Also, the stage report's `carries:` list is §2's new block, not a discarded
   part. Correction as in R31's row.
4. **R17 and E32** (raw §2, entry l.27). The `carries` block is a 38-line docstring passage (the stage report's list),
   not "a line". Corrections:
   - R17: "Three blocks are module-docstring text, each headed by a line that begins with a word and a colon at
     column 0…".
   - E32: "(31 definitions and `carries:`, a 38-line docstring passage)".
5. **E16** (entry l.12–13). The list of what the splitter discards omits `del _t` and the `__main__` block, both
   compared in §2b. Correction: "(the module docstring's prose, the imports, a tuple line, the NESTED loop with
   `del _t`, and the `__main__` block)".

## 4. Code's dispositions of the second pass (every IMPRECISE item; there was no FAIL)

| Item | Disposition |
|---|---|
| R29 (§2b's counts) | Accepted: "without its `@@` header lines (139 and 188 lines; 248 and 314 with them)". |
| R55 (§7, "prints no hash") | Accepted: "no hash of the analyzer or the schema (its one digest is the proposal's pinned `30a3d0f5...04f4`)". |
| R31 (§2b's "Added" list) | Accepted. The list names the rewritten passages' new text (with the new NOT-RUN sentence), the end-state rules, G-READ-n's artifact and its PASS rule, and the examples' list, then `import json` and the NESTED loop. It says the stage report's `carries:` list is §2's new block, not a discarded part. |
| R17, E32 (`carries:`) | Accepted. §2 says the three docstring blocks are each headed by a word and a colon at column 0, and that `carries:` is a 38-line passage; the entry says the same. |
| E16 (the entry's list of what the splitter discards) | Accepted: "the module docstring's prose, the imports, a tuple line, the NESTED loop with `del _t`, and the `__main__` block". |
| The observation (the entry's values-check line) | Accepted. The line now reports both passes. |
| UNVERIFIABLE items | Noted. They are the run's conditions and which bytes ran (the output cannot show them), messages, and the coming commit. |
| The checker's departures | Noted, all read-only. Beyond the brief's list it used `tr -d ' '` and `uniq -c` (once each), `sed` substitutions as stdout filters, `git hash-object` on the analyzer, and one status scoped to five named paths. It wrote no temporary file, never ran `split.awk`, ran no Python, and touched nothing under `data/`. |
