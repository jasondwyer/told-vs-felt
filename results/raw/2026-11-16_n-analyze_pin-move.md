# n_analyze.py: the schema pin moved from 5a97527 to 14e65d8 (PI date 2026-11-16)

Code's raw for the entry `n package — scripts/n_analyze.py, the schema pin moved from 5a97527 to 14e65d8`.
n-build's commit `14e65d8` changed `valence_core/n/schema.py`, which the analyzer committed at `5c0ae6b` pins by
sha256 and refuses otherwise. This raw holds:
- the schema commit as verified (§1);
- every block of the two schema blobs compared (§2), and what the splitter discards, compared (§2b);
- the three blocks the analyzer can reach that differ (§3);
- NESTED's keys (§4);
- the splitter (§5);
- the analyzer's diff (§6);
- its battery against the new schema (§7).

Nothing ran on a model or on the box. The one Python process was the battery (§7), in a window the coordinating
session granted, at `nice -n 19`, in the foreground.

## 1. The schema commit, verified

- `14e65d8` (`14e65d812fe5e1a1e311150c7e1bf0d31b745899`), parent `5c0ae6b`, paths (`git show --name-status`): M `RESULTS.md`; A `results/raw/2026-11-16_n-schema-v2_valuescheck.md`; M `valence_core/n/schema.py`.
- `valence_core/n/schema.py`'s blob sha256: at `5a97527` `77c12d6d0e7eee370291e0f5e587204f4ae613c65ce57f95c336f507273494bc`; at `14e65d8` `4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665` (n-build's message gave `4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665`); the tree's file `4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665`.

## 2. Every block of the two schema blobs, compared

Each blob (`git show <commit>:valence_core/n/schema.py`) was split at its top-level lines by `split.awk` (§5). A line `def NAME` or `class NAME`, or a line `NAME =` or `NAME:` at column 0, starts a block, which runs to the next top-level line. A top-level comment, and a line starting with `)`, `]` or `}`, join the block before them. Any other top-level line (an import, the module docstring's first line, a tuple assignment such as `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = …`, a loop) is discarded with what follows it, up to the next top-level line: §2b compares those parts. Each block present in both blobs was compared with `cmp`; a difference in comment or blank lines only is marked so. Three blocks are module-docstring text, each headed by a line that begins with a word and a colon at column 0: `schema:` and `own:` in both blobs, and `carries:` (a 38-line passage) in 14e65d8. They are text, not definitions, so `5a97527`'s 77 blocks are 75 definitions and two docstring lines, and `14e65d8`'s 32 new blocks are 31 definitions and `carries:`.

| Block | 5a97527 → 14e65d8 | The analyzer calls it |
|---|---|---|
| `ARMS` | identical |  |
| `ARM_CELLS` | identical |  |
| `ARM_SPAN_KIND` | identical |  |
| `BK_CELLS` | identical |  |
| `CAPTURE_FIELDS` | identical |  |
| `CELL_FIELDS` | identical |  |
| `CELL_SCHEMA` | identical | `sm.CELL_SCHEMA` |
| `DIRECTION_IDS` | identical |  |
| `DOSES` | identical |  |
| `DOSE_MAP_FIELDS` | identical |  |
| `DOSE_RULE_LABELS` | identical |  |
| `DOSE_SLUGS` | identical |  |
| `FIDELITY_FIELDS` | identical |  |
| `FIDELITY_REASONS` | identical |  |
| `FIDELITY_RULE_FIELDS` | identical |  |
| `IDENTITY_CHECK_FIELDS` | identical |  |
| `MAX_WINDOW` | identical |  |
| `MERGE_DISTANCE` | identical |  |
| `NESTED` | identical |  |
| `N_FLOOR` | identical |  |
| `N_RANDOM` | identical |  |
| `N_SESSIONS` | identical |  |
| `PROPOSAL_SHA256` | identical |  |
| `RANDOM_IDS` | identical |  |
| `RECORD_FIELDS` | identical |  |
| `RECORD_SCHEMA` | identical |  |
| `RESTRICTED_FIELDS` | identical |  |
| `RHO` | identical |  |
| `SESSION_SET_SHA256` | identical |  |
| `SHAM_LINE` | identical |  |
| `STAGES` | identical |  |
| `STAGE_IDENTITY_FIELDS` | identical |  |
| `SchemaError` | CHANGED | `sm.SchemaError` |
| `TAU` | identical |  |
| `TAU4` | identical |  |
| `TOLD_LINE` | identical | `sm.TOLD_LINE` |
| `TOLD_VARIANT` | identical |  |
| `UNIT` | identical |  |
| `_HEX16` | identical |  |
| `_HEX64` | identical |  |
| `_SESSION` | identical |  |
| `__all__` | CHANGED |  |
| `_check_capture` | identical |  |
| `_check_dose_map` | identical |  |
| `_check_dose_points` | identical |  |
| `_check_fidelity` | identical |  |
| `_check_fidelity_rule` | identical |  |
| `_check_identity_block` | identical |  |
| `_check_records_list` | identical |  |
| `_check_restricted` | identical |  |
| `_check_stage_identity_table` | identical |  |
| `_check_table` | identical |  |
| `_check_type` | identical |  |
| `_fail` | identical |  |
| `_is_float` | identical |  |
| `_is_int` | identical |  |
| `_selftest` | CHANGED |  |
| `bk_cell_of` | identical |  |
| `cell_filename` | identical | `sm.cell_filename` |
| `check_cell` | comment or blank lines only | `sm.check_cell` |
| `check_record` | CHANGED |  |
| `check_stage_identity` | identical |  |
| `dose_point_values` | identical | `sm.dose_point_values` |
| `dose_points` | identical | `sm.dose_points` |
| `example_cell` | comment or blank lines only |  |
| `example_identity` | identical | `sm.example_identity` |
| `example_record` | identical | `sm.example_record` |
| `expected_alpha` | identical |  |
| `fidelity_numbers` | identical |  |
| `own` | identical |  |
| `read_id` | identical |  |
| `read_plan` | identical | `sm.read_plan` |
| `read_plan_sha256` | identical |  |
| `schema` | CHANGED |  |
| `session_id` | identical |  |
| `shadow_read_id` | identical |  |
| `shared_prefix` | identical |  |

**What check_cell and check_record reach.** By name, `check_cell` references `CELL_FIELDS`, `CELL_SCHEMA`, `_check_table`, `_fail`, `cell_filename`, `check_record`, `check_stage_identity` and `read_id`; `check_record` references `ARMS`, `ARM_CELLS`, `ARM_SPAN_KIND`, `BK_CELLS`, `DOSES`, `DOSE_RULE_LABELS`, `FIDELITY_REASONS`, `N_FLOOR`, `RECORD_FIELDS`, `RECORD_SCHEMA`, `SHAM_LINE`, `TOLD_LINE`, `TOLD_VARIANT`, `_SESSION`, `_check_table`, `_fail`, `dose_point_values`, `expected_alpha`, `fidelity_numbers`, `read_id`, `session_id`, `shadow_read_id` and `shared_prefix` (the words `schema`, `own` and `carries` match only inside their strings). Each is identical across the two blobs, but `check_record`, whose one change is the message in §3. `_check_table` dispatches through `_check_type` and `NESTED`, both identical; `NESTED`'s new keys (§4) are none of its old ones.

New in 14e65d8, none called by the analyzer: `BINOMIAL_FIELDS`, `BINOMIAL_STATE_FIELDS`, `CAP_FIELDS`, `COUNTERS_FIELDS`, `CV_FORMS`, `END_STATES`, `GREAD_AXES`, `GREAD_BAR`, `GREAD_CAMPAIGN_FIELDS`, `GREAD_FIELDS`, `GREAD_LR`, `GREAD_MERGEABLE`, `GREAD_PROBE_FIELDS`, `GREAD_RESULT_FIELDS`, `GREAD_SCHEMA`, `GREAD_STATUSES`, `PAUSE_FIELDS`, `PAUSE_KINDS`, `REPORT_FIELDS`, `REPORT_SCHEMA`, `STOP_FIELDS`, `STOP_KINDS`, `VALID_CELL_NAMES`, `_CELL_KEYS`, `_check_report_nested`, `carries`, `check_gread`, `check_report`, `example_gread`, `example_pause`, `example_report`, `identity_sha256`.

## 2b. What the splitter discards, compared

`discarded.awk` (below) prints what `split.awk` discards: each top-level line that starts no block, with what
follows it up to the next top-level line, by the same rules. Its output for the two blobs, without its `@@` header lines (139 and 188 lines;
248 and 314 with them), was compared with `diff`: 6 hunks.
- Removed or changed from `5a97527`: 6 lines, all prose of the module docstring.
- Added in `14e65d8`: prose of the module docstring, namely the rewritten passages' new text (among it a new
  sentence on NOT-RUN), the stage report's end-state rules, G-READ-n's artifact and its PASS rule, and the
  examples' list; then `import json`, and the loop that registers NESTED's 18 new keys, with `del _t` (§4). The
  stage report's `carries:` list is not among these: the splitter takes it for a block (§2).
- Unchanged: the rest, among it the tuple line `SHADOW_ARM, SHADOW_DIRECTION, SHADOW_DOSE = "N1-V", "none", "0"`.

As a check on both comparisons, a whole-file `diff` of the two blobs keeps all but 10 of `5a97527`'s lines: seven
of the module docstring (one of them the `schema:` line), two of `SchemaError`'s docstring, and `check_record`'s
message. Everything else in the diff is added.

```awk
# Print what split.awk discards: each top-level line that starts no definition, with what follows it up to the next
# top-level line (the same rules as split.awk), each block headed by its first line's number.
/^(def|class) [A-Za-z_][A-Za-z_0-9]*/ { keep = 0; next }
/^[A-Za-z_][A-Za-z_0-9]* *[:=]/ { keep = 0; next }
/^[^ \t#)\]}]/ { keep = 1; print "@@ " NR; print; next }
{ if (keep) print }
```

## 3. The three blocks the analyzer can reach that differ

`check_record` (`diff` of its block, 5a97527 then 14e65d8):

```
112c112,113
<             _fail(w("ids_sha_bk"), "differs from ids_sha: a rendering mismatch is a STOP, never a record")
---
>             _fail(w("ids_sha_bk"), "differs from ids_sha: a rendering mismatch is never a record (a pause during a "
>                                    "stage; a G-VER-STOP at G-VER)")
```

`SchemaError` (`diff` of its block, 5a97527 then 14e65d8):

```
2,3c2,3
<     """A record, cell or identity that does not match this schema. The runner refuses to write it; the analyzer
<     refuses to load it."""
---
>     """A record, cell, identity, report or G-READ-n artifact that does not match this schema. Its writer refuses to
>     write it; the analyzer refuses to load it."""
```

`check_cell` (`diff` of its block, 5a97527 then 14e65d8):

```
30a31
> # --- the stage report (n-report-v1) and G-READ-n's artifact (n-gread-v1), settled with n-analyzer ----------------
```

`check_cell`'s block differs only by the top-level section comment that now follows it in 14e65d8; its code is unchanged.

## 4. NESTED's keys

The dict literal `NESTED = {…}` is identical in the two blobs. Its keys: `capture`, `dose_map`, `dose_points`, `fidelity`, `fidelity_rule`, `identity`, `records`, `restricted`, `stage_identity`. 14e65d8 registers 18 more at import, in one loop, each to its report checker:

```
for _t in ("per_arm", "cell_shas", "cell_shas2", "pauses", "binomial", "binomial_state", "stop", "cap", "counters",
           "fid_counts",
           "int_by_key", "strs", "gread_campaign", "gread_probe", "lr", "gread_results", "layer_results",
           "comparator"):
    NESTED[_t] = (lambda t: (lambda v, w: _check_report_nested(t, v, w)))(_t)
del _t
```

None of the 18 is one of the 9.

## 5. The splitter (`split.awk`, Code's scratch), whole

```awk
# Write each top-level definition (def/class NAME, or NAME = / NAME:) to DIR/NAME.txt, through to the next top-level line.
/^(def|class) [A-Za-z_][A-Za-z_0-9]*/ { if (out) close(out); n = $0; sub(/^(def|class) /, "", n); sub(/[^A-Za-z_0-9].*$/, "", n); out = DIR "/" n ".txt"; print > out; next }
/^[A-Za-z_][A-Za-z_0-9]* *[:=]/ { if (out) close(out); n = $0; sub(/[^A-Za-z_0-9].*$/, "", n); out = DIR "/" n ".txt"; print > out; next }
/^[^ \t#)\]}]/ { if (out) close(out); out = ""; next }
{ if (out) print >> out }
```

## 6. The analyzer's diff (`git diff -- scripts/n_analyze.py` against `5c0ae6b`), whole

The committed file becomes sha256 `4f63903f161885a8bb16ea933157d6e0e609e3cfa91503ac3ef68b1af23c5d73`.

```diff
diff --git a/scripts/n_analyze.py b/scripts/n_analyze.py
index d1c3544..c5efdf0 100644
--- a/scripts/n_analyze.py
+++ b/scripts/n_analyze.py
@@ -1841,7 +1841,8 @@ def _bt_structure(B: _Battery, ptext: bytes, hook: _Hook) -> None:
 
 
 # =====================================================================================================================
-# 10. The reader (n-read-v1 / n-cell-v1, valence_core/n/schema.py at 5a97527, sha256 77c12d6d...94bc)
+# 10. The reader (n-read-v1 / n-cell-v1, valence_core/n/schema.py at 14e65d8, sha256 4bed3f9a...4665; its record and
+#     cell checks as at 5a97527 but for check_record's rendering-mismatch message)
 # =====================================================================================================================
 # The schema module is imported lazily, on the verdicts path and in the battery only (LAZY_SCHEMA), and bound by its
 # sha256 in every output; its checks run on every cell the analyzer loads ("the checks both sides run"). What the
@@ -1849,7 +1850,7 @@ def _bt_structure(B: _Battery, ptext: bytes, hook: _Hook) -> None:
 # each steered read's shadow exists with its ids_sha; a session's cues and present order agree across its reads; N4-T
 # and N4-Ts carry the same schedule_zone per session, 80 S and 80 U (n §2.4).
 SCHEMA_REL = "valence_core/n/schema.py"
-SCHEMA_SHA256 = "77c12d6d0e7eee370291e0f5e587204f4ae613c65ce57f95c336f507273494bc"     # 5a97527
+SCHEMA_SHA256 = "4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665"     # 14e65d8
 LAZY_SCHEMA = "valence_core.n.schema"
 N_SESSIONS, N_FLOOR = 160, 40
 #: n §2.4's table, independently of the schema's ARM_CELLS (the reader cross-checks the two): arm -> (directions,
@@ -1868,7 +1869,7 @@ GUARD_DIRS = {"N2-E": "span_reward", "N2-S": "span_sentiment", "N2-C": "span_cha
 
 
 def schema_module():
-    """The record schema, imported lazily; refused unless its bytes are the pinned ones (5a97527)."""
+    """The record schema, imported lazily; refused unless its bytes are the pinned ones (14e65d8)."""
     if str(REPO) not in sys.path:
         sys.path.insert(0, str(REPO))
     got = hashlib.sha256((REPO / SCHEMA_REL).read_bytes()).hexdigest()
@@ -2324,7 +2325,8 @@ COUNTER_NAMES = ("fidelity re-computations", "fidelity exceedances at TAU", "fid
 
 def counters(camp: Campaign) -> dict:
     """n §4's counters by arm and dose label, over every read in the campaign (rule 23); the rendering-mismatch
-    counter is the stage report's (a mismatch is a STOP, never a record; schema docstring)."""
+    counter is the stage report's (check_record: "a rendering mismatch is never a record (a pause during a stage; a
+    G-VER-STOP at G-VER)")."""
     out: dict = {}
     for r in camp.records.values():
         key = f"{r['arm']}|{r['dose_label']}"
```

## 7. The battery against the new schema

`scripts/n_analyze.py --selftest` at sha256 `4f63903f161885a8bb16ea933157d6e0e609e3cfa91503ac3ef68b1af23c5d73`, with the tree's `schema.py` at `14e65d8`, run from the
repository root at `nice -n 19`; exit 0 (the runner printed it to the session). The repository root is shown as
`<repo>`. The battery prints no hash of the analyzer or the schema (its one digest is the proposal's pinned
`30a3d0f5...04f4`), and its output is line for line that of the BUILD's run of record against `5a97527`. It
passes only if the tree's `schema.py` hashes to the analyzer's pin, since `schema_module` refuses
otherwise. The command that ran it hashed both files first, to the values in §1 and §6; that hashing went to the
session's output, not a file.

```
INVOCATION: <repo>/jlens-qwen36/.venv/bin/python scripts/n_analyze.py --selftest
  [PASS] N1 REPLICATED: (i) Δm(+1) 1.0 ≥ 0.545, CI [0.9, 1.1]; (ii) slope 0.9 > floor 0.3; (iii) 1.0 > max(L 0.05, P 0.04); (iv) Δm(−1) −0.7, CI [−0.8, −0.6]
  [PASS] N1 PARTIAL failing ['i']
  [PASS] N1 PARTIAL failing ['iv']
  [PASS] N1 PARTIAL failing ['i', 'iv']
  [PASS] N1 NOT-REPLICATED failing ['ci+1']
  [PASS] N1 NOT-REPLICATED failing ['ii']
  [PASS] N1 NOT-REPLICATED failing ['iii']
  [PASS] N1 NOT-REPLICATED failing ['ci+1', 'ii']
  [PASS] N1 NOT-REPLICATED failing ['ci+1', 'iii']
  [PASS] N1 NOT-REPLICATED failing ['ii', 'iii']
  [PASS] N1 NOT-REPLICATED failing ['ci+1', 'ii', 'iii']
  [PASS] N1 INDETERMINATE by pause:N1-V
  [PASS] N1 INDETERMINATE by pause:N1-R
  [PASS] N1 INDETERMINATE by pause:N1-P
  [PASS] N1 INDETERMINATE by incomplete:N1-V (OPEN-Q6, pending the seat)
  [PASS] N1 INDETERMINATE by incomplete:N1-R
  [PASS] N1 INDETERMINATE by incomplete:N1-P
  [PASS] boundary: Δm(+1) exactly 0.545 meets (i) (≥)
  [PASS] boundary: Δm(+1) one ulp below 0.545 fails (i)
  [PASS] boundary: a CI with lower bound exactly 0 does not exclude 0
  [PASS] boundary: a CI with upper bound exactly 0 does not exclude 0 ((iv) fails)
  [PASS] boundary: |Δm(+1)| equal to the ceiling is not certified (strict >)
  [PASS] boundary: a slope equal to its floor does not exceed it ((ii) fails)
  [PASS] boundary: Δm(−1) exactly 0 fails (iv) (< 0)
  [PASS] ceiling: P(+1) 0.95 above L(+1) 0.5 governs (0.9 uncertified)
  [PASS] ceiling (OPEN-Q2, pending the seat): at d_eq, where N1-P is not read, the ceiling is L(d_eq) alone (0.08 > 0.06 certified)
  [PASS] a negative Δm(+1) beyond the ceiling is certified (|mean|); (i) fails, (ii)-(iii) hold, CI excludes 0 -> PARTIAL (PIN-n-8, as §5 is written)
  [PASS] dose DETECTABLE: Δm(d_eq) 0.3 [0.2, 0.4] against L 0.05
  [PASS] dose DETECTABLE: Δm(d_eq) -0.3 [-0.4, -0.2] against L 0.05
  [PASS] dose NOT-DETECTABLE: Δm(d_eq) 0.3 [-0.01, 0.6] against L 0.05
  [PASS] dose NOT-DETECTABLE: Δm(d_eq) 0.04 [0.02, 0.06] against L 0.05
  [PASS] dose INDETERMINATE whenever N1 is, under each of N1's six causes
  [PASS] dose INDETERMINATE names 'incomplete:points' beside N1's (subsumed; OPEN-Q6, pending the seat)
  [PASS] dose reports d_20 beside (point, estimate, ceiling, certification)
  [PASS] N2 SPECIFIC (N2-SPECIFIC)
  [PASS] N2 SHARED (N2-SHARED-V-CERT)
  [PASS] N2 SHARED (N2-SHARED-V-UNCERT)
  [PASS] N2 NULL (N2-NULL)
  [PASS] N2 INDETERMINATE by pause:N2-E (§5, n:140: 'an unadjudicated pause stands on N2's reads'; the guards' reads are N2's reads)
  [PASS] N2 INDETERMINATE by pause:N2-S (§5, n:140: 'an unadjudicated pause stands on N2's reads'; the guards' reads are N2's reads)
  [PASS] N2 INDETERMINATE by pause:N2-C (§5, n:140: 'an unadjudicated pause stands on N2's reads'; the guards' reads are N2's reads)
  [PASS] N2 INDETERMINATE by incomplete:N2-E (OPEN-Q6, pending the seat)
  [PASS] N2 INDETERMINATE by incomplete:N1-V (OPEN-Q6, pending the seat)
  [PASS] N2 INDETERMINATE by incomplete:N1-R (OPEN-Q6, pending the seat)
  [PASS] a pause on N1-V's or N1-R's reads, or on N1-P's where d_20 sits at +1 (shape b), alone leaves N2 evaluated (§5's N2 reads are N2-E's, N2-S's and N2-C's; OPEN-Q6, pending the seat: those N1 arms' incompleteness is a cause, their pauses are not)
  [PASS] N2 INDETERMINATE by incomplete:N1-P where d_20 sits at +1 (shape b: the ceiling takes P(+1)); with every point distinct (shape a) N1-P enters no N2 certification and N2 is evaluated (OPEN-Q6, pending the seat)
  [PASS] N2's guards decide nothing (span_sentiment, span_character varied over nine pairs, the outcome fixed)
  [PASS] N2 reports f = 0.10 beside (its own certification at d_eq's point), deciding nothing
  [PASS] N2 reports the norm match: ratio 1 on shape (a); 2·0.72/1 = 1.44 when the cap binds (shape b; OPEN-Q7, pending the seat)
  [PASS] N4 PASS
  [PASS] N4 REVERSE
  [PASS] N4 DEAD
  [PASS] N4 INDETERMINATE
  [PASS] N4 INDETERMINATE, no read obtained, by incomplete:N4-T
  [PASS] N4 INDETERMINATE, no read obtained, by incomplete:N4-Ts
  [PASS] N4 INDETERMINATE, no read obtained, by pause:N4-T (OPEN-Q6, pending the seat)
  [PASS] N4 INDETERMINATE, no read obtained, by pause:N4-Ts (OPEN-Q6, pending the seat)
  [PASS] N4 INDETERMINATE, no read obtained, by E-undefined
  [PASS] N4 order: REVERSE before DEAD (mean −0.3 < −E, CI excludes 0, upper −0.2 < 0.5)
  [PASS] N4 order: PASS before DEAD (mean 0.3 > E, CI excludes 0, upper 0.4 < 0.5)
  [PASS] N4 boundary: mean equal to E is not PASS (strict >)
  [PASS] N4 boundary: mean equal to −E is not REVERSE (strict <); upper −0.05 < 0.5 -> DEAD
  [PASS] N4 boundary: an upper bound equal to 0.5 is not DEAD (strict <)
  [PASS] N4 boundary: a 98% CI with lower bound exactly 0 does not exclude 0 (not PASS)
  [PASS] NOT-RUN by clock:no-box: 'LOCK-n v1.0 was not committed by its Clock date (2026-12-15): no box'
  [PASS] NOT-RUN by clock:gate-stopped: 'LOCK-n v1.0 was not committed by its Clock date (2026-12-15): G-CAL-n STOPPED and no re-specification was locked'
  [PASS] NOT-RUN by clock:pi-declined: 'LOCK-n v1.0 was not committed by its Clock date (2026-12-15): the PI declined v1.0'
  [PASS] NOT-RUN by clock:not-locked: 'LOCK-n v1.0 was not committed by its Clock date (2026-12-15)'
  [PASS] NOT-RUN by no-arm:pi-stop: 'locked, and no arm's full read set was produced before a PI stop'
  [PASS] NOT-RUN by no-arm:gver-stop: 'locked, and no arm's full read set was produced before a G-VER STOP'
  [PASS] NOT-RUN by no-arm:cap: 'locked, and no arm's full read set was produced before its cap'
  [PASS] NOT-RUN record refused (PREMATURE)
  [PASS] NOT-RUN record refused (STAGE)
  [PASS] NOT-RUN record refused (UNIT)
  [PASS] NOT-RUN record refused (CAUSE)
  [PASS] NOT-RUN record refused (KEYS)
  [PASS] G-LEAK-n table: N1-V cert reached
  [PASS] G-LEAK-n table: N1-V uncert reached
  [PASS] G-LEAK-n table: N1-V incomplete reached
  [PASS] G-LEAK-n table: N2-E cert reached
  [PASS] G-LEAK-n table: N2-E uncert reached
  [PASS] G-LEAK-n table: N2-E incomplete reached
  [PASS] G-LEAK-n table: N2-S cert reached
  [PASS] G-LEAK-n table: N2-S uncert reached
  [PASS] G-LEAK-n table: N2-S incomplete reached
  [PASS] G-LEAK-n table: N2-C cert reached
  [PASS] G-LEAK-n table: N2-C uncert reached
  [PASS] G-LEAK-n table: N2-C incomplete reached
  [PASS] G-READ-n table: a PASS cell is reported as such
  [PASS] G-READ-n table: a FAIL cell is reported as such
  [PASS] G-READ-n table: a NOT-COMPUTED cell is reported as such
  [PASS] G-READ-n table: exactly three cells enter §5 -- valence +1 (N1), valence d_eq (dose), span_reward f = 0.20 (N2)
  [PASS] §5's four sentences and two labels are the proposal's italic spans at n:136 and n:138, character for character; Code's expansion of the ellipsis ends in the span's own words
  [PASS] N1 PARTIAL names its failing conjuncts (OPEN-Q8, pending the seat): three forms, each naming exactly its conjuncts, no slot left
  [PASS] N1 NOT-REPLICATED names its failing conjuncts (OPEN-Q8, pending the seat): seven forms, each naming exactly its own
  [PASS] INDETERMINATE sentences carry their causes (OPEN-Q8, pending the seat)
  [PASS] the sentence layer refuses a value outside the outcome space (three cases)
  [PASS] Code's 31 sentence forms (OPEN-Q8) are pinned by digest (CODE_FORMS_SHA256), pairwise distinct, and use declared slots only
  [PASS] tuples T1: 1921/1921 evaluations: one sentence set: the four slots 7.1, 7.2, 7.3, N4, each a non-empty text, each state the tuple's coordinate (NOT-RUN: all four)
  [PASS] tuples T2: 1921/1921 evaluations: the set equals the oracle's (§5's verbatim cells read from the proposal file)
  [PASS] tuples T3: 1921/1921 evaluations: 7.1 depends on (N1, G-READ-n valence +1, N4) only
  [PASS] tuples T4: 1921/1921 evaluations: 7.2 depends on (dose, G-READ-n valence d_eq, N4) only
  [PASS] tuples T5: 1921/1921 evaluations: 7.3 depends on (N2, G-READ-n span_reward f = 0.20, N4) only
  [PASS] tuples T6: 1921/1921 evaluations: N4's line depends on (N4, no read obtained) only
  [PASS] tuples T7: 1921/1921 evaluations: (OPEN-Q3, pending the seat) a §0.6 label exactly on the null outcomes (NOT-REPLICATED, NOT-DETECTABLE, SPECIFIC, NULL); answered iff N4 PASS and the slot's G-READ-n cell PASS
  [PASS] tuples T8: 1921/1921 evaluations: §5's verbatim sentences exactly in their cells (REPLICATED; DETECTABLE; NOT-DETECTABLE answered) and nowhere else
  [PASS] tuples T9: 1921/1921 evaluations: no bracketed token outside the declared slots (BK's '[1.00, 1.19]' is text)
  [PASS] tuples T10: the forms tally as derived by hand -- 7.1 480 each (NOT-REPLICATED 48 answered / 432 CNA); 7.2 640 each (NOT-DETECTABLE 64 / 320 / 256); 7.3 480 each (SPECIFIC and NULL 48 / 432); N4 384 x 5; NOT-RUN 1
  [PASS] the outcome space (OPEN-Q4, pending the seat): 385 tuples (4 x 3 x 4 x 4 x 2 = 384, + NOT-RUN), 1921 evaluations (384 x 4 G-READ inputs + 96 x 4 for N4's second INDETERMINATE form + NOT-RUN)
  [PASS] two passes over the 1,921 evaluations give byte-identical canonical JSON
  [PASS] reachability: on every enumerated state of the three shapes, dose is INDETERMINATE iff N1 is (so 160 of the 384 product tuples are unreachable on any map: 64 with N1 INDETERMINATE and dose decided, 96 the reverse)
  [PASS] reachability: the outcome layer raised on no enumerated state
  [PASS] reachability, shape (a) all points distinct: 28 (N1, dose, N2) triples, the hand-derived 28; x N4 (4) x G-READ-n at d_eq (2) = 224 reachable tuples + NOT-RUN
  [PASS] reachability, shape (b) d_20 merged into +1 (the cap binds): 24 (N1, dose, N2) triples, the hand-derived 24; x N4 (4) x G-READ-n at d_eq (2) = 192 reachable tuples + NOT-RUN
  [PASS] reachability, shape (d) d_20 and d_eq merged into +1: 17 (N1, dose, N2) triples, the hand-derived 17; x N4 (4) x G-READ-n at d_eq (2) = 136 reachable tuples + NOT-RUN
  [PASS] reachability: N4 reads its own arms only -- each of its five forms beside N1 REPLICATED and N1 INDETERMINATE
  [PASS] key_stream is m:159's key-to-generator function (equal to valence_core.m.keys.stream on four keys)
  [PASS] numpy's stream known answer: f|CORR|0's permutation(16) is m's pinned value
  [PASS] the resample matrix is PIN-n-12's stream, re-derived literally from its words for N1-V, N1-R (40) and N4-T: equal on a repeat, different across arms, 4,000 x n indices in [0, n)
  [PASS] a constant vector's estimate is (c, c, c)
  [PASS] mean_est equals a loop over the resamples with a hand percentile (linear interpolation), to 1e-12
  [PASS] percentile intervals use linear interpolation (numpy's 'linear' equals the hand rule at 1, 2.5, 97.5, 99)
  [PASS] the per-session slope is OLS with an intercept (equal to polyfit and to the closed form; an exact line of slope 2 gives 2; a flat session 0)
  [PASS] on an asymmetric grid OLS with an intercept and a fit through the origin differ, so OPEN-Q1 (pending the seat) decides a figure (here 0.8114 vs 0.8444)
  [PASS] sd0 is the population SD (ddof 0), C6
  [PASS] a nonfinite value in a statistic's input STOPs (never a silent drop)
  [PASS] §4's statistics on BK's 160 neutral sessions reproduce G-DATA (iii): Panel D means 1.0900 / 0.5072 / −0.3841 / −0.7554; SDs (ddof 0) 0.6233 / 0.3703 / 0.4546; slope 0.9164, SD 0.4466; the 24 random slopes −0.2880 to +0.3641, so the floor on BK's five points is 0.3641
  [PASS] fidelity_ratio on BK's 2,400 neutral re-computed reads reproduces G-DATA (vi): 0 above TAU (p0 = 0/2,400), 570 above TAU/4, largest ratio 0.012143
  [PASS] the dose map: shapes (a), (b), (d) and the merge rule at clear distances (0.03125 merges, 0.0625 does not; d_20 = 2·0.25 = 0.5 is BK's +1/2)
  [PASS] the dose map refuses d_20 above or below min(1.0, 2.0 * d_eq), a non-positive or nonfinite d_eq, a fold into 0, rho above or below 0.3 (each with d_eq computed from it where that matters), R or R_ell not a positive float, and d_eq ≠ (0.10 * R_ell) / (rho * R) (PIN-n-14); it passes shapes (a), (b), (d) and an exact identity (R_ell 23.90625, R 25.5: d_eq 0.3125)
  [PASS] the dose map lists its points as n-build's schema does (order, values, merged lists in fold order) for shapes (a), (b), (d); d_20 and d_eq are read under their keepers' labels
  [PASS] secondary (d)'s Pearson r (PIN-n-18): equal to the hand formula and to numpy's corrcoef; None when one side has no spread
  [PASS] the label-mass counter (PIN-n-17) counts reads strictly below .20 (0.19 counts; 0.20 and 0.9 do not)
  [PASS] N2's slope points (OPEN-Q9, pending the seat): (0, d_eq, 2·d_eq) on BK's scale, its floor at (0, d_eq's point, d_20's point) -- equal on shape (a); 2·0.72 against +1 when the cap binds (shape b)
  [PASS] reader path: a campaign written with the schema's builders (7,360 reads, 136 cells, nothing merged) reads back through check_cell to (REPLICATED, DETECTABLE, SHARED, PASS, PASS)
  [PASS] reader path: the filled sentence set keeps no slot; N1's sentence is §5's with the figures and 'on a reconstructed direction'
  [PASS] reader path: the filled set (REPLICATED, DETECTABLE, SHARED, PASS) equals the battery's literal text, figure for figure: Δm, CIs, slope, floor, the ceilings max(L, P) at +1, d_eq and the norm-matched point, m_told's 98% CI and E
  [PASS] reader path: nothing moves -> (NOT-REPLICATED, NOT-DETECTABLE, NULL, DEAD)
  [PASS] reader path: span_reward still, the valence direction moving -> N2 SPECIFIC; the told line pulling the other way -> N4 REVERSE
  [PASS] reader path: Δm(+1) near 0.3 -> N1 PARTIAL failing (i); a told margin split +2 / -1.5 -> N4 INDETERMINATE (terminal)
  [PASS] reader path: Code's forms filled, against the battery's literal text: N2 SPECIFIC with its label, N4 REVERSE with −E printed negative (E = 0.1), N1 PARTIAL with its failing conjunct and Δm(−1), N4's terminal INDETERMINATE
  [PASS] reader path: a missing N1-R cell -> N1, dose and N2 INDETERMINATE (incomplete:N1-R); a missing N4-Ts cell -> N4 INDETERMINATE, no read obtained
  [PASS] reader path: one non-finite read in N1-V at +1 -> N1-V not usable (PIN-n-20) -> N1 INDETERMINATE (nonfinite:N1-V), every planned read counted present; the counter tabulates it
  [PASS] reader path: a non-finite shadow at run 100 -> N1, dose and N2 INDETERMINATE, N1's causes (nonfinite:N1-V, shadow:N1-P), N2's (shadow:N2-E, nonfinite:N1-V); N1-R (40 floor sessions) keeps its floor and L; N4 PASS
  [PASS] reader path: R_ell 50 merges +d_20 into +1 -> 6,240 reads; N2's norm-matched point is +1, the ratio 2·d_eq reported; N1-P at −0.9 there puts P(+1) above L(+1), and N2's reported ceiling is max(L, P) = P(+1), the one its certification used (E 0.625 below it: SPECIFIC)
  [PASS] reader path (F11): an asymmetric campaign -- a random direction with a negative slope and offset, N1-P at −0.9 / +0.2, N2-E at 1.0 / 0.1 by f with spreads in the ratio 1:2, a negative sham mean, a session offset of mean +0.045 -- reads to the hand computation: the slope with its d = 0 point, the floor as max |mean slope|, L and P as |mean| at their own points, the ceilings, E by f, N2's per-f n and SD, N2's slope, E, and m_told's 98% CI (whose 95% would have excluded 0)
  [PASS] reader path: d_eq ≈ 0.52 merged into +1/2 -> the dose question reads +1/2, and its sentence prints d_eq's value with the point read beside it
  [PASS] reader path: unadjudicated pauses on N1-R and N2-E -> N1 and dose INDETERMINATE (pause:N1-R), N2 INDETERMINATE (pause:N2-E), N4 PASS
  [PASS] reader path: G-READ-n FAIL everywhere -> the tuple's coordinate FAIL; the NOT-REPLICATED and NULL labels concluded, not answered
  [PASS] reader path (F12): G-READ-n FAIL at d_eq only -> the coordinate FAIL, N1's label answered, the dose sentence not readable; FAIL at +1 only -> the coordinate PASS, N1's label concluded, the dose sentence answered with its AUC; N2's label follows span_reward at f = 0.20; a readable dose sentence without an AUC, and a route other than A or B, STOP
  [PASS] reader path (F14): the TAU/4 row (PIN-n-16) drops the 40 reads above TAU/4 at +1 (none above TAU), the 40 above both at −1, and run 2 everywhere (its shadow above TAU/4), from those points and the slopes (79 sessions left), the primary keeping all 160; the counters, through `counters`, tell TAU/4 from TAU, count two identity-bound exceedances and the three label masses strictly below .20
  [PASS] reader path: the secondaries compute -- (a) first-pick shares per arm and dose, (c) groups count-only below 20, (d) r over 160 sessions, (e) six cosines and the matched means -- and (b) reads 'not recorded'
  [PASS] reader path: secondary (c) reports a group's mean at exactly 20 events (the decidable-n floor, rule 28(a)) and withholds it at 19
  [PASS] reader path refuses: a file no cell names; a stage identity that differs between cells; a read whose ids_sha differs from its shadow's; N4-T and N4-Ts zones that differ; a record the schema's check_cell refuses; a session whose cues differ between reads; a schedule of 81 S and 79 U on both N4 arms; a capture array whose bytes are not its recorded sha256, or absent; steered reads whose shadows are not on disk
  [PASS] the merge rule (PIN-n-14) agrees with the schema's dose_points on 400 maps (d_eq 0.003 to 1.2): 384 derived alike, 16 refused alike (a fold into 0)
  [PASS] the merge rule at a decimal distance of exactly 0.05 (IEEE decides): 0.45 folds into +1/2 (as d_eq and as d_20), 0.55 is kept (as d_eq and as d_20), and d_eq = 0.05 beside a kept d_20 = 0.1 ties between 0 and 0.1, goes to 0 and is refused; the schema's dose_points agrees on all five
  [PASS] the pinned map's coupling class: d_20 at +1/2 is (a) (28 triples), d_eq at +1/2 with d_20 at +1 is (b) (24), both at +1 is (d) (17), each agreeing with the hand derivation
  [PASS] not-run writes N-pod_NOT-RUN.json once (written, then identical), refuses other bytes (write-once), and carries the reason in all four sentence slots
  [PASS] not-run's refusals before any write: the output of record only from the committed analyzer; a --out at the repository root or inside it; with nothing left to check it names data/n/verdicts, and a --out outside the repository proceeds
  [PASS] ganl's 18 refusals before any battery run, each by name (a canonical run whose bound files are not committed, or with no pinned map; --out at the repository root or inside it; a map unreadable, not exactly five finite floats, or off §2.3's formulas, a fold into 0 included), and a consistent map outside the repository proceeds
  [PASS] G-ANL-n's artifact names the analyzer, proposal and schema by sha256, the tuple space (385; 1,921 evaluations), the pinned map's points and reach, the PIN and OPEN registers, and no time
  [PASS] proposal: PROPOSAL-n v0.2's sha256 is the pinned 30a3d0f5...04f4
  [PASS] every verbatim constant is on its declared proposal line (n:136, n:138, n:142)
  [PASS] TAU is BK's prereg.json 'tau', and prereg.json is the SHA256SUMS copy
  [PASS] module-level imports are numpy and the standard library only (no repository module, no model library)
  [PASS] no model library is imported by the battery (torch, transformers, mlx, mlx_lm, accelerate, safetensors)
  [PASS] the battery's hook refuses, before any filesystem call or process start, 9 probes: opens (positional, file=, os.open) under data/n/ckpt, data/n/reports and results/raw, a stat, a listing and a scan under data/n's ckpt, reports and verdicts, a process naming data/mf3 by a repository-relative path, and data/mf3 by string; nothing else was refused during the battery
  [PASS] every PIN-n and OPEN-Q cited outside the registers is registered, and every registered one is cited
  [PASS] the battery wrote nothing under data/n (sha256 of every file outside ckpt / reports / verdicts, before = after)
  [PASS] coverage: every one of the 172 required ids reached
  [PASS] check count 171 == EXPECTED_CHECKS 171 (a skipped assertion is a failure)
  171/171 n_analyze battery checks pass
```
