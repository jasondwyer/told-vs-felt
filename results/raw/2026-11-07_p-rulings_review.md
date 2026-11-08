# PROPOSAL-p -- G-CAL-p's flags applied: the blind code review, rounds 1-2 (Code's raw, 2026-11-07)

*Two blind review agents, read-only on the repository, each given the seat's ruling (`38f9974`) and the working-tree diff (round 2 also round 1's report). Code's dispositions come first; the reports follow verbatim. Local paths scrubbed.*

## 0. Code's dispositions (each item re-checked at source before it was applied or disclosed)

### Round 1 (1 MAJOR, 4 MINOR, 12 NOTE)

| item | severity | disposition |
|---|---|---|
| M1 | MAJOR | Fixed: `gcal.gate_record` stores m's gate-line record with its proposal field under p's name, `proposal_p_sha256` (the sha256 the gate line checks), and `run` stores `gate_record(pre["gate"])`; `proposal_sha256` holds m's alone in every p artifact. A self-test case builds the real gate record and checks the stored form and the call. |
| m1 | MINOR | Fixed: `gcal.disclosure_problems` checks DISCLOSURE against the ruling's §1 sentence, read from its committed bytes at their pinned sha256; G-CAL-p's precheck refuses otherwise; a self-test case. |
| m2 | MINOR | Fixed: a self-test case in gcal and one in gshape plant a wrong PROPOSAL-m sha256 and assert the refusal. |
| m3 | MINOR | Fixed: the trigger path's and a ProxyStop's `returned_text` are asserted whole (the ProxyStop by a double whose token ids cannot place the break). |
| m4 | MINOR | Fixed: the ORDER docstrings of gcal and the driver, and gshape's inputs paragraph, name the PROPOSAL-m and disclosure checks. |
| n1 | NOTE | Fixed: report.py quotes the ruling's definition byte for byte, the path on one line. |
| n2 | NOTE | Fixed: whitespace-split, then each token normalized -- the ruling's own order -- declared as a PIN, with a contraction case (`I don't know` against `down` is not counted). The 384 records still give 0/3/5. |
| n3 | NOTE | Flagged for the seat, F-p11 (the residual common-word class), in the entry and in report.py's docstring. |
| n4 | NOTE | Fixed: cases for the length rule (`a` against gold `ab`) and gold normalization (`twenty-fuor` against `twenty-four`). |
| n5 | NOTE | Fixed: the label names the ruled definition's figures. |
| n6 | NOTE | Disclosed and flagged: the dated note on G-SHAPE-p's entry states what the 5009e77 artifact holds (no `proposal_sha256` field; the pre-ruling disclosure); the canonical re-run before LOCK-p v0.1 needs that artifact superseded, F-p12, the seat's ruling. |
| n7 | NOTE | Fixed: term (e) stated in its amended form in register.py; `__init__.py` too. |
| n8 | NOTE | Fixed: the proxy's docstring rewrapped. |
| n9 | NOTE | Fixed: `clean_task_words` reads `it["task"]` (a pool item without a task is an error); the synthetic test pool carries tasks. |
| n10 | NOTE | Fixed: the refusal names the observed sha256 against v1.11's; no trailing space. |
| n11 | NOTE | No change: the redundant guard is defence in depth. |
| n12 | NOTE | No change: no p checkpoint was ever written (G-CAL-p has not run), so `p-gcal-checkpoint-v1` names the only layout any record will have. |

### Round 2 (0 MAJOR, 1 MINOR, 8 NOTE)

| item | severity | disposition |
|---|---|---|
| r2-m1 | MINOR | Fixed: `gate_record` renames both proposal fields, `proposal_file` → `proposal_p_file` and `proposal_sha256` → `proposal_p_sha256`. A self-test walks an artifact and a checkpoint built with m's real gate record: `proposal_sha256` holds m's v1.11 alone, and `proposal_file` appears nowhere. |
| r2-n1 | NOTE | Flagged: F-p11 now names the inflection false positives too (`January's`, `Iron's`, `Seven's`, `twenty-fourth`, `Close.`, `Colder.`), in report.py's docstring and the entry. |
| r2-n2 | NOTE | Fixed: the walk test above, not only the structural check. |
| r2-n3 | NOTE | Fixed: the length witness is `b` against gold `ab`, not counted, with `bb` counted beside it. |
| r2-n4 | NOTE | Fixed in part: failing cases for a DISCLOSURE off the ruling's sentence, a ruling not at its sha256, and a pool item without a task. The not-committed PROPOSAL-m branch fails closed and the clean-word argument's only effect on the pool is `hot`/`shut`; both are disclosed and left without a case. |
| r2-n5 | NOTE | Fixed: the gate record's form is declared a PIN (`gate_record`'s docstring), and the module docstring names it beside m's schema. |
| r2-n6 | NOTE | Fixed: `__init__.py` says `proposal` names PROPOSAL-p, with p's sha256 in `proposal_p_sha256` and m's in `proposal_sha256`. |
| r2-n7 | NOTE | Fixed: RegisterStop's docstring reads "never an unpinned copy"; gshape's long docstring line is rewrapped. |
| r2-n8 | NOTE | Fixed: G-CAL-p's artifact declares `diagnostic_fields`, and G-SHAPE-p's inputs check the disclosure (`gcal.disclosure_problems`) before writing it. |

## 1. Round 1 (the agent's report, verbatim)

# Blind review: the five G-CAL-p flag rulings as applied in the working tree (uncommitted)

Reviewer: blind, read-only. Scope: `git diff HEAD -- valence_core/p scripts/p_sessions.py` (six files changed:
`__init__.py`, `gcal.py`, `gshape.py`, `proxy.py`, `register.py`, `report.py`; the driver is unchanged), read against
the seat's answer `results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md` (committed at `38f9974`, blob
sha256 `e3de1c0316c95701e627fb89596c50b0cf0596f31c352ed6ee9a8daca5d1e006`, recomputed). HEAD `38f9974`.

Method: every changed line read against the ruling and against every consumer; the m code it binds read at source
(`valence_core/m/gcal.py` `gate_line` :599-627, `_identity_olmo` :837-856, `completability_artifact` :983-1026,
`run_completability` :1088-1210; `valence_core/m/stages.py` `PROPOSAL_REL` :144-145, `_committed` :415). Probes were
model-free and written only under `scratchpad/podwatch/probes4/`. They ran at `nice -n 19` with `-B` and
`PYTHONDONTWRITEBYTECODE=1`.

- `p1_verbatim.py`: byte comparison of the three ruling texts with the code.
- `p2_counter.py`: the counter on G-CAL-OLMo's 384 committed records, under three readings.
- `p3_gate_field.py`: a stub G-CAL-p run with the real gate record injected, walking every `proposal_sha256` field.
- `p4_mutants.py`: in-memory mutants of the working-tree modules, each loaded under its real module name from a
  scratch copy and run against that module's own `_selftest`.
- `p5_residual.py`: the pinned counter on plausible answers.

The self-test was run in the real tree. `git status --porcelain --untracked-files=all` was identical before and after,
and no file under the repository was newer than a marker set before the run.

**Self-test: 104/104, exit 0.** It confirms the author's figure, and the run wrote nothing to the tree.

---

## 0. Verdict at a glance

| Ruling | Applied exactly? | Applied completely? |
|---|---|---|
| F-p3 (§1) disclosure | yes: `gcal.DISCLOSURE` is byte-equal to the ruling's italic span | yes in code (G-CAL-p and G-SHAPE-p); the self-test does not pin it (MINOR m1); the 5009e77 artifact keeps the old sentence (NOTE n6) |
| F-p8 (§2) pins | identity, precheck and G-SHAPE-p: yes | **no**: G-CAL-p's checkpoint and artifact still carry a field named `proposal_sha256` holding p's sha, in `provenance[].gate` (**MAJOR M1**) |
| F-p10 (§3) returned text | yes: `returned_text` (cut log, ProxyStop, STOP record); trigger, grader and records read `text` only | yes, every consumer renamed; the STOP record's field is untested (MINOR m3) |
| P21 (§4) register | yes: term (e)'s amendment byte-equal after unwrapping the docstring; entry (4) struck; entry (5) has kind `"pinned restatement"` and cannot be substituted | yes; `__init__.py:4-5` still says "never by copy" (NOTE n7) |
| F-p1 (§5) counter | yes: the definition is implemented; 0/3/5 on the 384 records reproduced, and the ruling's examples hold | the docstring's "quote" is not verbatim (NOTE n1); the normalize-then-split reading is undeclared (NOTE n2); residual false positives (NOTE n3) |

Counts: **1 MAJOR, 4 MINOR, 12 NOTE.**

---

## 1. Per-ruling verification

### F-p3: §5.4's date and the disclosure sentence

Ruling, §1 (line 7), the italic span after "The artifacts' disclosure sentence reads:":

> pre-registered on 2026-11-07 (PROPOSAL-p v0.2, \`18b0111\`; v0.1 routed 2026-11-06), after the shared dose of PROPOSAL-m failed completability on this lineage at G-CAL-OLMo on 2026-11-06; the corruption rule changed once, from the gate's read, before any session ran.

Code, `gcal.py:103-105`. The three literals concatenate to:

> pre-registered on 2026-11-07 (PROPOSAL-p v0.2, \`18b0111\`; v0.1 routed 2026-11-06), after the shared dose of PROPOSAL-m failed completability on this lineage at G-CAL-OLMo on 2026-11-06; the corruption rule changed once, from the gate's read, before any session ran.

Probe `p1_verbatim.py` extracted the span from the committed blob with the regex
`disclosure sentence reads: \*(.+?)\* p §5\.4`. Results:

- `gcal.DISCLOSURE == span` is **True**. The string is 265 characters, ASCII-only, sha16 `29a30cd00fb0633d`.
- The two backticks around `18b0111` are kept. With them stripped the equality is False.
- Reading: the markdown italic delimiters are dropped as the quote's frame, and the backticks are kept as bytes of the
  span. Either reading of the backticks is defensible. Keeping them is the byte-literal one, and the BUILD entry should
  say which was taken.

Where it reaches:

- G-CAL-p artifact: `art["p"]["disclosure"]` (`gcal.py:398`).
- G-SHAPE-p artifact: `art["disclosure"] = gcal.DISCLOSURE` (`gshape.py:399`).

No other p module or the driver carries a date or the old sentence; a grep for `2026-11-06`, `pre-registered` and
`§5.4` found only `corrupt.RENDERS_RAW_REL`'s file name and the gshape docstring's "(p §5.4)". §5.2's sentence has no
code counterpart.

Self-test: both checks compare the artifact to the constant itself (`gcal.py:677`, `gshape.py:484`). That is a
tautology, so the constant's text is not pinned to the ruling (MINOR m1; mutant E survives).

### F-p8: m's pin in `proposal_sha256`, p's in `proposal_p_sha256`, in every p artifact

Ruling, §2 (line 11): "**In every p artifact — gates, checkpoints, locks' identity blocks, the analyzer's outputs —
`proposal_sha256` is PROPOSAL-m v1.11's (`42ab36ec…6c6b`) … and `proposal_p_sha256` is PROPOSAL-p's committed
sha256** … The gate line's startup check stays on p's sha". The reason given: "a reader of any file under `data/p/`
must find one meaning per field".

Code:

- `gcal.py:107-108`: `M_PROPOSAL_REL = m_stages.PROPOSAL_REL` (`PROPOSAL-m-gating-campaign-v1_11.md`) and
  `M_PROPOSAL_SHA256 = "42ab36ecc814c9c43d4e7a6e12a4b1c0c006c3881f88ae1458524b9d9fc96c6b"`.
  - It equals `git show HEAD:PROPOSAL-m-gating-campaign-v1_11.md | shasum -a 256`.
  - It matches the ruling's `42ab36ec…6c6b`.
  - It is the sha that LOCK-m-F0.md and LOCK-m-F3.md name.
- `gcal.py:251`: `_identity_olmo(..., proposal_sha256=M_PROPOSAL_SHA256, ...)`, with `proposal_p_sha256` set to p's
  at `:254`. The artifact keeps `proposal_p_sha256` at the top level (`:378`).
- `gcal.py:228-231`: precheck refuses unless PROPOSAL-m is committed at HEAD, unedited, at `M_PROPOSAL_SHA256`.
  - It runs on stub and canonical runs alike and accumulates into the single refusal before any adapter is made.
  - Probe: with the constant patched in memory to zeros, a stub `precheck` is REFUSED with
    `PROPOSAL-m-gating-campaign-v1_11.md: not committed at HEAD with sha256 0000000000000000 (the identity's
    proposal_sha256, F-p8)`, and the scratch out-directory stays empty.
- `gcal.py:239`: the gate line stays `gate_line(PROPOSAL_P_REL, PROPOSAL_P_SHA256, ...)`, as ruled.
- `gshape.py:243-246`: refuses unless the committed PROPOSAL-m hashes to `M_PROPOSAL_SHA256`. `gshape.py:356-357`
  writes `"proposal_sha256": ins["proposal_m_sha256"]` beside `"proposal_p_sha256"`.
- The 5009e77 artifact: `data/p/gates/G-SHAPE-p.json` is unmodified in the working tree.
- Schedules: neither `data/p/schedules/*.json` nor `manifest.json` carries a `proposal*` field, so they need nothing.

Gap (MAJOR M1, §2 below). In a canonical G-CAL-p run, `pre["gate"]` is m's `gate_line` record:
`{"line", "proposal_file", "proposal_sha256": psha, ...}` (m `gcal.py:624`), with `psha` the sha of `proposal_file`,
which is p's. It is stored in the checkpoint's provenance entry (`gcal.py:465-467`). m's `completability_artifact`
then copies that entry into the artifact (m `gcal.py:994`, `:1013`).

Probe `p3_gate_field.py` ran a stub run with the real gate record injected, and walked every field named
`proposal_sha256` or `proposal_p_sha256`:

```
ARTIFACT:   /identity/proposal_sha256 = 42ab36ecc814c9c4 (m's)
            /identity/proposal_p_sha256 = 42f2977b941bc016 (p's)
            /provenance[0]/gate/proposal_sha256 = 42f2977b941bc016 (p's)   <-- second meaning
            /proposal_p_sha256 = 42f2977b941bc016 (p's)
CHECKPOINT: /identity/proposal_sha256 = 42ab36ecc814c9c4 (m's)
            /provenance[0]/gate/proposal_sha256 = 42f2977b941bc016 (p's)   <-- second meaning
```

In m's own G-CAL-OLMo artifacts both fields are m's (`/identity/proposal_sha256` and
`/provenance[0]/gate/proposal_sha256` are both `42ab36ec…`), so the conflict is p's alone. A stub run has
`gate = None`, which is why the self-test cannot see it.

### F-p10: the returned text as a diagnostic field outside the stored text

Ruling, §3 (line 15) sets four terms:

1. The returned text lives in its own named field (`returned_text`, or Code's name), declared diagnostic.
2. It is excluded by name from the hair trigger ("`line_break_in_stored_text` reads the round's text field only"),
   from the grader, from every later round's prompt, and from the read rule's "stored text".
3. "the stop's `stop` field keeps the returned text whole the same way".
4. §2.2's sentence is corrected (in the docs, by a dated note).

Code:

- `proxy.py:73` logs the cut event as `{"returned_text": text, "stored_text": cut, ...}`.
- `proxy.py:33-34` declares `DIAGNOSTIC_FIELDS = ("returned_text",)`, re-exported at `gcal.py:110`.
- `proxy.py:43-45` gives `ProxyStop` a `returned_text` attribute, set whole at `:70`.
- `gcal.py:402-405`: `_stop(..., returned_text=...)` writes `ck["stop"]["returned_text"]` whole. Only `detail` is
  truncated, to 600 characters.
- The ProxyStop path passes `getattr(e, "returned_text", None)` (`:488-489`). The trigger path passes `text` (`:492-494`).

Domain checks, each verified by reading:

- The hair trigger reads `r["text"]` or the stored result's text only (`gcal.py:299`, `:389`, `:492`;
  `report.py:116`).
- The grader reads `text = str(g.text)`, the stored result (`gcal.py:490`, `:497`). `strict_grade` and `counters`
  read records' `text`.
- The cut entries' `returned_text` is read by nothing but the artifact copy (`gcal.py:388`).
- G-CAL-p has no later rounds and no read rule, so those two exclusions hold by construction.

Consumers of the renamed keys (`text_returned`→`returned_text`, `text_stored`→`stored_text`, stop `text`→`returned_text`):

- `read_checkpoint` validates `c.get("stored_text")` (`:304`).
- The two self-tests (`gcal.py:670`, `proxy.py:148-149`).
- No `text=` keyword, `.text` of a ProxyStop, or old key remains in `valence_core/p` or the driver.
- Mutant F2, `read_checkpoint` reading the old key `text_stored`, is KILLED by the resume case, so a missed rename at
  that consumer would be caught.
- The committed BUILD raws (`2026-11-07_p-build_design.md:270`, `_review.md`, `_valuescheck.md`) name `text_returned`.
  They are records, not to be edited. The BUILD entry's dated note and LOCK-p v0.1 must declare `returned_text` (and
  `stored_text`, and the STOP record's `returned_text`) as the ruling's term 1 requires.

Gaps: the STOP record's `returned_text` is never asserted (MINOR m3; mutants B and C survive).

### P21 / F-p7: the pinned restatement, the register's one exception

Ruling, §4 (line 19): "The register's rule "never a copy" (ans2 §1 (e)) is amended, and the amendment is the register's
text at LOCK-p v0.1:

> never an unpinned copy; a restated fragment is admitted only where m's code is an inline fragment of a function that cannot run for p, and only with an AST-level equality assertion to m's fragment in p's self-test and a dynamic check that every call carries m's procedure, so that a later m edit breaks p's self-test before it changes p's behaviour.

… Entry (4), not exercised, is struck from the register; P21 enters it as entry (5), kind "pinned restatement"."

Code:

- `register.py:14-19`, term (e). Probe `p1_verbatim.py` took the quoted text between `LOCK-p v0.1: "` and
  `" ``substituted``` and collapsed whitespace runs (the docstring's wrap). The result is byte-equal to the ruling's
  span: **True**.
- `ENTRIES` (`register.py:65-88`) is numbered 1, 2, 3, 5. Entry (4) is gone, and `BY_N.get(4)` is None, so
  `substituted(4, …)` is a `RegisterStop`.
- Entry (5) (`:80-87`):
  - `kinds=(RESTATEMENT,)` with `RESTATEMENT = "pinned restatement"` (`:35`), the ruling's kind, exact.
  - Status `ADMITTED` (`:36`).
  - The m citations `gcal.py:1104` (`temp, cap = _ro.OLMO_TEMP, _ro.STOP_CAP`), `:1155` (`seg = …`) and `:1164`
    (`g = adapter.generate(…)`) are verified at HEAD; `valence_core/m/` is unchanged.
- `substituted` refuses (5) in two ways: its status is not `BUILT`, and `RESTATEMENT in e.kinds` (`:104`). The
  self-test case `(5, mod, {"x": None})` gives `stop`.
- The pin itself (`_call_pin_problems`) is unchanged. It runs in the self-test (`gcal.py:637-639`) and in precheck
  (`:224`). The dynamic check over all 128 calls is `gcal.py:653-660`.
- Mutant L (the `RESTATEMENT` clause removed) survives only because the status check already refuses. That is
  defence in depth, not a gap (n11).

### F-p1: §2.3's corrupted-spelling counter, pinned

Ruling, §5 (line 23): "candidate words are the stored text's whitespace-split, `normalize`d words of length ≥ 2,
excluding FUNCTION_WORDS and every word of the clean pool's tasks; numeric golds are excluded; a hit iff the word is
not a gold and its Levenshtein distance to some gold is ≤ 1 for a gold of length ≤ 3, ≤ 2 otherwise."

Code (`report.py:80-100`), clause by clause:

| Clause of the ruling | Code |
|---|---|
| whitespace-split, `normalize`d words | `m_gcal.normalize(text).split()`: f0's grader normalize, applied to the whole text, then split (reading: n2) |
| length ≥ 2 | `len(w) >= 2` |
| excluding FUNCTION_WORDS | `w not in FUNCTION_WORDS` (p §1.1's list, all lower-case, imported from `corrupt`) |
| excluding every word of the clean pool's tasks | `clean_task_words(pool)`: the normalized words of every pool item's `task`; `counters` passes the served pool (`report.py:108`, `:113`) |
| numeric golds excluded | `spelling_golds`: a normalized gold is dropped when its non-space characters are digits |
| not a gold | `w not in gs`, against the normalized, non-numeric golds |
| ≤ 1 for a gold of length ≤ 3, ≤ 2 otherwise | `levenshtein(w, g) <= (1 if len(g) <= 3 else 2)` |

Probe `p2_counter.py` ran over G-CAL-OLMo's three committed artifacts (384 records) with the served pool:

- **0 / 3 / 5** records (sft / dpo / instruct), as `report.py:26-28` and the self-test's `want` (`:169-174`) say.
  - dpo: `CORR_clean i=4 s=1` (`true`~`three`, d=2), `CORR_corrupted i=8 s=2` (`januwy`, d=2),
    `CORR_corrupted i=11 s=1` (`dn`~`down`, d=2).
  - instruct: `CORR_corrupted i=4 s=1` (`true`~`three`), `i=7 s=1` (`irom`~`iron`, d=1), `i=8 s=2` (`januwy`),
    `i=8 s=3` (`janaury`), `i=11 s=1` (`dn`).
- The ruling's examples hold in the self-test (`report.py:142-148`): `dn`, `Januwy` and `Janaury` count; `the`, `two`
  and `do` do not; `Janbaa` and `Janyooar` do not.
- All three readings of "whitespace-split, normalized" give the same 0/3/5 on these records: normalize-then-split
  (the code), per-token normalize, and per-token normalize with a re-split.

---

## 2. Findings

### MAJOR

**M1 — F-p8 is incomplete. G-CAL-p's write-once artifact and its checkpoint carry a second `proposal_sha256` that holds p's sha.**

- Where: `valence_core/p/gcal.py:465` (`entry = {..., "gate": pre["gate"], ...}`) with `:239` (`gate_line(PROPOSAL_P_REL,
  PROPOSAL_P_SHA256, ...)`). Through m `gcal.py:624` (`rec = {"line": …, "proposal_file": proposal_file,
  "proposal_sha256": psha, …}`) and m `gcal.py:994`/`:1013` (provenance copied into the artifact).
- Statement: the ruling makes `proposal_sha256` mean m's pin in every p artifact, for the stated reason "a reader of
  any file under `data/p/` must find one meaning per field". The change moves `identity.proposal_sha256` to m's. But
  the gate record m's `gate_line` returns, keyed `proposal_sha256`, is still stored with p's sha in
  `checkpoint.provenance[i].gate` and copied into `artifact.provenance[i].gate`.
- Scenario: on the box, `scripts/p_sessions.py gcal --unit OLMo-sft` writes `data/p/gates/G-CAL_completability_olmo-sft.json`
  once. In it, `/identity/proposal_sha256 = 42ab36ec…` (m's) and `/provenance[0]/gate/proposal_sha256 = 42f2977b…`
  (p's). That is two meanings for one field name in one write-once file under `data/p/`. Probe `p3_gate_field.py`
  shows exactly this; m's own G-CAL-OLMo artifacts have m's in both places.
- Why the self-test misses it: stubs have `gate = None` (`gcal.py:234-240`), so no self-test path stores a gate record.
- Fix, one of:
  - (a) Store p's gate record under p's naming before appending the provenance entry, for example
    `proposal_p_file` / `proposal_p_sha256` in place of `proposal_file` / `proposal_sha256`. Keep `line` (the printed
    gate line, which stays on p's sha as ruled) unchanged. Add a self-test case that injects a stand-in gate record,
    as the probe does, and walks the artifact and checkpoint asserting that every `proposal_sha256` equals m's. That
    also guards any future field.
  - (b) If Code reads "the gate line's startup check stays on p's sha" as covering the stored gate record, take that
    to the seat as a FLAG before G-CAL-p runs. It contradicts the ruling's uniformity sentence, and the artifact is
    write-once.

### MINOR

**m1 — F-p3's verbatim sentence is not pinned to the ruling by any test (mutant E survives).**

- Where: `gcal.py:677` (`art["p"]["disclosure"] == DISCLOSURE`) and `gshape.py:484` (`a0["disclosure"] == gcal.DISCLOSURE`).
- Statement: both checks compare the artifact to the constant itself. Mutant E reverts the date in `DISCLOSURE` to
  2026-11-06, and the gcal self-test still passes 23/23.
- Scenario: a later edit to the constant (a typo fix, a re-wrap that drops a space) changes the write-once artifacts'
  sentence away from the seat's words with every self-test green.
- Fix: assert that `DISCLOSURE` occurs once, byte for byte, in the committed answers raw at its pinned sha256
  (`e3de1c03…d006`). This is the form `corrupt.ANSWERS_SHA256` / `SEAT_READ_LINE` already uses for the seat's read.
  Record the backtick reading.

**m2 — The new m-pin refusal has no negative self-test (mutant A survives).**

- Where: `gcal.py:228-231`, and `gshape.py:243-246` (confirmed by reading: no gshape case plants a wrong PROPOSAL-m).
- Statement: with the whole gcal check replaced by `if False:`, gcal's self-test passes 23/23. The refusal that
  guards the identity's `proposal_sha256` on the box is untested in both modules.
- Scenario: a refactor that drops or inverts the condition lets G-CAL-p write an identity naming m's sha without m's
  file being committed at that sha, with nothing failing.
- Fix: a case per module with `M_PROPOSAL_SHA256` patched, or with `_committed` returning other bytes for
  `M_PROPOSAL_REL`. Expect REFUSED before any adapter is made (gcal) and `GshapePRefusal` before scoring (gshape). The
  probe's in-memory patch shows the gcal form works.

**m3 — The STOP record's `returned_text` (F-p10 term 3) is never asserted (mutants B and C survive).**

- Where: `gcal.py:738-742`. The check is named "... the stop recorded with its text, ..." but asserts only `trigger`,
  `key`, `records == []` and the refused resume. The boundary/generation case at `:775-781` checks `detail` only.
  No case raises a `ProxyStop` through `run`.
- Statement:
  - Mutant B (`returned_text=None` on the hair-trigger STOP) passes 23/23.
  - Mutant C (`returned_text=None` on the ProxyStop path, which also covers a mis-spelled `getattr` name) passes 23/23.
- Scenario: the diagnostic the seat asked to keep "whole" silently stops being recorded on exactly the two STOP paths
  where it matters.
- Fix:
  - Assert `stopped["stop"]["returned_text"] == "a\nb"` in the trigger case.
  - Add a case whose adapter makes the proxy raise `ProxyStop` (`m_testing.OLMoScriptedAdapter`, as in
    `proxy.py:166-172`), and assert the stop record's `returned_text` equals the returned text whole.

**m4 — The declared refusal orders omit the new PROPOSAL-m pin.**

- Where: `gcal.py:25-34` ("ORDER. Every refusal of p's own that needs no adapter runs before the load: the unit, …,
  the proposal, …, the seat's read of record, the generation call's pin (P21), §3.2's conditions (1)-(3) …, the weights
  of record and, on the box, …"). Also `scripts/p_sessions.py:21-25` (gcal's precheck list) and `gshape.py:27-34`
  (INPUTS OF RECORD: "PROPOSAL-m (committed) carrying m:277's criterion", with no sha pin).
- Statement: these enumerated declarations, which the BUILD entry and LOCK may quote, describe the pre-ruling
  precheck. The new refusal sits between the seat's read and the weights (`gcal.py:228`) and before the criterion
  (`gshape.py:244`).
- Scenario: a reader of LOCK-p v0.1's quoted order cannot learn that G-CAL-p refuses on PROPOSAL-m's sha.
- Fix: add "PROPOSAL-m v1.11 committed at its sha256 (F-p8)" to all three lists. The driver edit moves
  `driver_sha256`, which is harmless before the first run.

### NOTE

**n1 — The F-p1 docstring "quote" is not verbatim.** `report.py:21-24` puts the definition in quotation marks with
`>=`/`<=` for the ruling's `≥`/`≤` and ` ``normalize``d ` for `` `normalize`d ``. Probe: no match exact, and no match
after mapping ≥/≤ to ASCII; the first difference is the backticks, at character 57. The file is not ASCII-only (`§`,
`’` occur). Quote the ruling byte for byte, or drop the quotation marks and say "restated". Also, the raw's path is
split across a line inside a literal (`report.py:20-21`), so a grep for the path misses it.

**n2 — The order "normalize the text, then split" is Code's reading and is not declared.**

- Where: `report.py:98`. "whitespace-split, `normalize`d words" can also read as split first, then normalize each
  token.
- On the 384 records the readings agree (0/3/5). They diverge on contractions and hyphenations. Under the code,
  `corrupted_spelling("I don't know", ["down"])` is True (`don`~`down`, d=1). Under per-token normalization it is
  False (`don t`, d=3).
- Item 11's corrupted render ("Writk thn opposite ob 'up'.") makes such an answer plausible at G-CAL-p.
- Mutant K (per-token) survives. Declare the reading as a PIN, and add a contraction case.

**n3 — The pinned definition still counts common words near 4-6-letter golds; FLAG for the seat.** The code is
faithful: `true`~`three` already fires twice on the records of record. Probe `p5_residual.py` shows plausible correct
answers counted as corrupted spelling under the definition as written:

| Item (gold) | Answers that count |
|---|---|
| 4 (three) | "There are three sides" (`there`, d=2); "These have 3 sides" |
| 15 (closed/shut) | "That is closed" (`that`~`shut`, d=2); "out" |
| 5 (cold) | "It could be cold" (d=1); "Cold, as I told you" |
| 1 (seven) | "…seven days…, even…" (d=1); "the seventh day"; "Never mind: 7" |
| 2 (march) | "much" (d=2) |
| 7 (iron) | "from" (d=2); "upon" |
| 10 (two) | "too" (d=1) |
| 11 (down) | "Now, down"; "known: down"; "won't say" |

Descriptive, deciding nothing, and recomputable (the ruling's own terms). The BUILD entry and LOCK-p v0.1 should say
the residual class is wider than `true`/`three` before G-CAL-p's counters are reported.

**n4 — Two clauses of the counter are untested.**

- Mutant G (no `len(w) >= 2`) and mutant H (golds not normalized) survive.
- The length filter is vacuous on the pool of record. The shortest spelling gold is `two`, with threshold 1, so no
  single letter can reach any gold, and only a synthetic gold would exercise the clause.
- Normalization of golds matters only for `twenty-four`.

**n5 — A self-test label is stale.** `report.py:175`: "the counters give the BUILD entry's figures". The BUILD's
figures were 4/10/9 (`2026-11-07_p-build_design.md:232`); `want` is now 0/3/5, the ruled definition's.

**n6 — G-SHAPE-p (process; for the dated note and LOCK-p v0.1).**

- (a) The 5009e77 artifact has no `proposal_sha256` field. It carries `proposal: "PROPOSAL-p"`, `proposal_p_sha256`
  (p's), and m's sha under `inputs.proposal_m.sha256`. The seat's "already written with p's in both fields" does not
  describe its bytes. It also carries the superseded disclosure ("…pre-registered on 2026-11-06…"). The dated note
  should state both.
- (b) The gshape change cannot reach the canonical path while that artifact stands. `guard.write_once_bytes` refuses
  differing bytes ("EXISTS … with different bytes; it is never overwritten"), so "future artifacts carry m's pin" holds
  only for `--out` runs.
- (c) Committing these changes makes 6 of the 48 source sha256s G-SHAPE-p recorded (`__init__`, `gcal`, `gshape`,
  `proxy`, `register`, `report`) differ from HEAD's blobs. p's package hash moves from `717958da…` to `e3831f47…`
  (working tree). Under m's map-check precedent that calls for a G-SHAPE-p re-run, which (b) refuses. LOCK-p v0.1
  needs the seat's word: an F-1-style exemption, or the artifact moved, which would contradict "stands as it is".

**n7 — The register's text still shows the old rule.**

- `register.py:14` keeps "a site not in the register is a STOP, never a copy" and appends the amendment.
- `__init__.py:4-5` still says m's modules are "imported UNCHANGED, by import and never by copy". `:19-22` of the same
  docstring describes the restated call.
- For the register's text at LOCK-p v0.1, state term (e) in its amended form: "… a STOP, never an unpinned copy; a
  restated fragment is admitted only where …".

**n8 — One overlong line.** `proxy.py:19` is 202 characters; the re-wrap was missed. The file's other lines are 127 or
fewer.

**n9 — `clean_task_words` fails open.** `report.py:82` uses `it.get("task", "")`, so a pool without tasks silently
empties the exclusion. The served pool always has `task`; the default exists for the self-test's synthetic pool. An
explicit `it["task"]`, with the synthetic pool given tasks, would fail closed.

**n10 — The m-pin refusal's message is imprecise.** `gcal.py:230-231` says "not committed at HEAD with sha256 X" for a
file that is committed at another sha, and does not print the observed sha. `gshape.py:245`'s form ("hashes to …,
not …") is clearer. There is also a trailing space when `mcp` is empty.

**n11 — The `RESTATEMENT in e.kinds` guard is redundant** (`register.py:104`; mutant L survives) because entry (5)'s
status is not `BUILT`. It is fine as defence in depth; no test isolates it.

**n12 — The schema id is unchanged while field names changed.** `CKPT_SCHEMA` stays `p-gcal-checkpoint-v1` while the
cut and stop field names change. This is harmless before the first G-CAL-p run, since no p checkpoint exists locally
(`data/p` holds only `gates/G-SHAPE-p.json` and the schedules). A BUILD-era checkpoint, were one on the box, would
fail closed: `read_checkpoint` refuses its cuts, and the identity's `proposal_sha256` and package hash differ.

---

## 3. Regression checks (beyond the rulings)

**Model load or record write from a self-test or stub.** None introduced.

- The changed code adds no loader call and no write path.
- gshape's new `a0` evaluate is in memory.
- The m-pin check reads git blobs only.
- The driver's trapped-loader cases pass. In the 104/104 run, `p_sessions: gcal is refused before any load …` and
  `… on a simulated clear box …` both pass, and the tree was unchanged after the run.

**Refusal order.**

- gcal: the new check accumulates into the one pre-load `GcalPRefusal`, after the renders STOP (still raised first)
  and before the weights, pod id, gate line and committed-code checks.
- gshape: it raises `GshapePRefusal` (exit 2) before m's criterion check, consistent with the proposal checks around it.
- The driver's refusal case (pod id removed) still reports POD ID ABSENT.

**Counter edge cases.** Detail is in §1 F-p1 and n2-n4, and the probe table above.

- `normalize` is m's pinned grader function.
- The length filter is applied after normalization.
- FUNCTION_WORDS are lower-case, matching normalized words.
- The clean words come from the served pool's tasks; they include the gold `iron`, harmlessly.
- Numeric golds: the pool's 10 digit-string golds are excluded and `twenty-four` becomes the spelling gold
  `twenty four`.
- Thresholds are keyed on the normalized gold's length. Mutant J (`< 3`) is killed.

**Register refusals.** `substituted(4, …)` (struck), `substituted(5, …)` (a restatement), an unbuilt (3), a wrong
module, an undeclared attribute, a wrong replacement and a qualified-name stand-in are each a `RegisterStop`. All seven
pass in the self-test.

**The m-pin precheck on the box.** It is fail-closed and needs nothing beyond what the box already uses:

- It uses `m_stages._committed` with m's `REPO` (the clone), as `gate_line` and `committed_problems` already do there.
- `PROPOSAL-m-gating-campaign-v1_11.md` is tracked at root and unmodified.
- A missing, edited or differently-hashed file refuses before the load.
- `M_PROPOSAL_REL` binds m's `PROPOSAL_REL`, which m's own PIN calls a stub-only default (`stages.py:140-143`). Since p
  pins the sha, a change of that default fails closed rather than silently.

**Mutants** (in-memory, against each module's own `_selftest`):

| Mutant | Result | Means |
|---|---|---|
| A: gcal m-pin check removed | SURVIVED | m2 |
| B: trigger STOP's `returned_text` dropped | SURVIVED | m3 |
| C: ProxyStop STOP's `returned_text` dropped | SURVIVED | m3 |
| D: identity back to p's sha | KILLED | F-p8 identity is covered |
| E: disclosure date back to 2026-11-06 | SURVIVED | m1 |
| F: `read_checkpoint`'s cut stored-text check removed | SURVIVED | pre-existing gap: no case plants a mismatched cut |
| F2: `read_checkpoint` reads the old key `text_stored` | KILLED | the rename at that consumer is covered |
| G: no length-2 filter | SURVIVED | n4 |
| H: golds not normalized | SURVIVED | n4 |
| I: numeric test without removing spaces | SURVIVED | equivalent on the pool |
| J: threshold `< 3` | KILLED | |
| K: per-token normalize | SURVIVED | n2 |
| L: register's `RESTATEMENT` clause removed | SURVIVED | redundant guard, n11 |

---

## Summary

The five rulings are applied at the points the author intended, and the verbatim texts match the seat's bytes:

- F-p3's sentence is byte-equal, with the backticks kept.
- P21's term (e) is byte-equal after unwrapping the docstring.
- F-p1's definition is faithfully implemented, and 0/3/5 on the 384 records of record is reproduced.
- The self-test is 104/104 and writes nothing to the tree.

One ruling is incomplete, and it lands in a write-once artifact on the next run. That is **MAJOR M1**: G-CAL-p's
checkpoint and artifact will hold `provenance[].gate.proposal_sha256` with p's sha beside `identity.proposal_sha256`
with m's. This is the two-meanings-per-field state F-p8 forbids, and stubs cannot see it.

The **4 MINOR** are test and documentation gaps on the new behaviour:

- m1: the disclosure is unpinned to the ruling.
- m2: the m-pin refusal is untested.
- m3: the STOP record's `returned_text` is unasserted.
- m4: the declared refusal orders omit the m pin.

The **12 NOTE** cover:

- The F-p1 docstring quote is not verbatim, and the normalize-then-split reading is undeclared (`don't` counts against
  `down`).
- The pinned definition's residual false positives (`there`/`three`, `that`/`shut`, `could`/`cold`, …), a FLAG for
  the seat.
- The 5009e77 G-SHAPE-p artifact (field layout and old disclosure for the dated note; a canonical re-run is refused by
  write-once while its recorded sources move).
- Wording, line-length and robustness residuals.

## 2. Round 2 (the agent's report, verbatim)

# Blind review, round 2: the five G-CAL-p flag rulings as applied (uncommitted), after round 1's dispositions

Reviewer: blind, read-only. This round reviews `git diff HEAD -- valence_core/p scripts/p_sessions.py`, seven files:
`__init__.py`, `gcal.py`, `gshape.py`, `proxy.py`, `register.py`, `report.py`, and the driver, where only the docstring
changed.

It reads them against two sources:

- the seat's answer `results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md`, sha256 `e3de1c03…d006`,
  recomputed;
- round 1's report, `podwatch/p_rulings_review.md`, with 1 MAJOR, 4 MINOR and 12 NOTE.

**HEAD.** HEAD was `38f9974` at the start of the review and `acc3b52` by the end. `acc3b52` is a parallel session's
G-TIME-F3 commit. It touches `RESULTS.md`, `data/mf3/` and `results/raw/` only, and none of p's inputs.

**Working tree.** The p working tree was byte-identical throughout. The sha256 of all twelve p files and the driver
were recorded before and after (`probes5/wt_shas_before.txt`). In the working tree:

- p's package sha256 is `1d764a3e5cfe975b…e145`.
- The driver's sha256 is `1140b57e…0690`. HEAD's is `4d75cf03…6bde`. The m4 docstring edit moved it, which is harmless
  before the first run.

**Method.** Each disposition was read at source and exercised by a probe. All probes were model-free and lived under
`scratchpad/podwatch/probes5/`. They ran at `nice -n 19` with `-B` and `PYTHONDONTWRITEBYTECODE=1`. The only writes
were the probes' own, under `probes5/`: stub-run checkpoints in `td/`, which was emptied by `TemporaryDirectory`, and
mutant sources in `mut/`.

| Probe | What it does |
|---|---|
| `q1_gate_walk.py` | M1. A stub G-CAL-p run with **m's real gate-line record** (`m_gcal.gate_line(PROPOSAL_P_REL, PROPOSAL_P_SHA256, stage="G-CAL-p-sft")`, the call a non-stub precheck makes) injected into precheck's result, then a `--resume`. It walks every field named `proposal*`, and every value carrying either sha, in the artifact on disk, the checkpoint, and the checkpoint after the resume. |
| `q2_counter.py` | The counter on G-CAL-OLMo's 384 committed records (HEAD's blobs) with the served pool, under both tokenizations, listing every disagreement. |
| `q3_verbatim.py` | Byte comparison of the three ruling texts with the code and docstrings. |
| `q4_mutants.py` | 29 in-memory mutants. Each is loaded under its real module name before its dependents import it, then run against the listed modules' own `_selftest`. |
| `q5`, `q6`, `q7` | The PIN reading's residuals; G-SHAPE-p's artifact built in memory and walked; the domain of the clean-task exclusion. |

**Self-test: 109/109, exit 0.** It ran at `38f9974` and again at `acc3b52` (11 s).

- `git status --porcelain --untracked-files=all` was identical before and after each run.
- No file under the repository was newer than a marker set before the run.
- The count reconciles with round 1's 104: gcal went from 23 to 27 checks (the ProxyStop, gate-record, DISCLOSURE and
  m-pin cases), gshape-p from 13 to 14 (the m-pin case), and one report label changed.

---

## 0. Verdict at a glance

| Item | Author's disposition | At source |
|---|---|---|
| **M1** | `gate_record` renames the proposal field; `run` stores `gate_record(pre["gate"])` | **FIXED.** With a real gate record, `proposal_sha256` occurs once in the artifact, the checkpoint and the resumed checkpoint, holding m's sha each time (q1). Two residuals: the sibling field `proposal_file` (**r2-m1**), and the guard is structural, not a walk (r2-n2). |
| m1 | `disclosure_problems` pins DISCLOSURE to the ruling's committed bytes (precheck + self-test) | **FIXED.** Mutant E is killed. The precheck wiring and the ruling-sha branch are untested (r2-n4). |
| m2 | failing-case tests for the PROPOSAL-m sha refusal (gcal, gshape) | **FIXED** for the hash branch in both modules. The not-committed branch is untested; it fails closed (r2-n4). |
| m3 | the STOP record's `returned_text` asserted on the trigger and ProxyStop paths | **FIXED.** Mutants B, C, C2, P1 and P3 are killed. |
| m4 | the order docstrings name the PROPOSAL-m and disclosure checks | **FIXED** (gcal ORDER, driver, gshape INPUTS). gshape.py:29 is now 177 characters (r2-n7). |
| n1 | the definition quoted verbatim | **FIXED**: byte-equal after unwrapping. |
| n2 | split, then normalize; a PIN; a contraction case | **FIXED**: mutant K is killed. The reading's own cost is undisclosed (r2-n1). |
| n3 | FLAG F-p11 | Raised: drafted in Code's entry text (scratch). `report.py:33-37` carries the class. |
| n4 | length and gold-normalization cases | **PARTLY.** Gold normalization is pinned (H killed). The length witness is vacuous (G survives; r2-n3). |
| n5 | label | **FIXED.** |
| n6 | FLAG F-p12 | Raised: drafted in Code's entry text (scratch). |
| n7 | term (e) in its amended form; `__init__.py` | **FIXED**: byte-equal. One leftover at register.py:40 (r2-n7). |
| n8 | rewrap | **FIXED**: proxy.py's longest line is now 127 characters, at :127 (HEAD's :120). |
| n9 | `clean_task_words` fails closed | **FIXED** (`it["task"]`, report.py:96). Untested; unreachable with the served pool (r2-n4). |
| n10 | the m-pin refusal's message | **FIXED**: it prints the observed sha16 and has no trailing space. |
| n11, n12 | no change | Accepted. No p checkpoint exists locally (`data/p` holds `gates/G-SHAPE-p.json` and `schedules/`). |

**New findings: 0 MAJOR, 1 MINOR, 8 NOTE.**

---

## 1. Disposition verification

### M1: m's gate-line record stored under p's name

Code:

- `gcal.py:269-276`: `gate_record` drops `proposal_sha256` and adds `proposal_p_sha256` with the gate's value.
- `gcal.py:494`: the provenance entry stores `gate_record(pre["gate"])`.
- `gcal.py:247`: precheck's `gate_line(PROPOSAL_P_REL, PROPOSAL_P_SHA256, ...)` is unchanged. The gate line stays on
  p's sha, as ruled.
- The printed GATE line (`:492-493`) still uses the raw record's `line`.

Probe `q1_gate_walk.py`, output abridged (`probes5/q1_out.txt`):

```
ARTIFACT (on disk)
   /identity/proposal              = 'PROPOSAL-p'
   /identity/proposal_p_sha256     = p's
   /identity/proposal_sha256       = m's
   /p/proposal                     = 'PROPOSAL-p'
   /proposal_p_sha256              = p's
   /provenance[0]/gate/line        carries p's sha16 in text   (the gate line, as ruled)
   /provenance[0]/gate/proposal_file      = 'PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md'
   /provenance[0]/gate/proposal_p_sha256  = p's
   => fields named proposal_sha256: 1; holding other than m's: []
CHECKPOINT                 => fields named proposal_sha256: 1; holding other than m's: []
CHECKPOINT after resume    => 1; [] (two provenance entries, both renamed)
gate keys: analyzer, claude_md_sha256, head, line, proposal_file, proposal_p_sha256
```

Round 1's two-meanings state is gone from the artifact, the checkpoint and the resumed checkpoint.

No reader breaks:

- m's production code only writes `entry["gate"]` (m `gcal.py:1137`). The one read, m `gcal.py:2142`, is in m's
  self-test.
- `scripts/m_analyze.py` reads G-CAL's model-free artifact only (`:104`), never a completability artifact's gate.

So the rename breaks no consumer.

Test: `gcal.py:796-803` unit-tests `gate_record` on m's real record and source-matches the store in `run`. Mutants:

- M1a, the raw record stored: KILLED.
- M1b, the field kept: KILLED.
- M1c, a second copy of the raw record added to the entry: SURVIVED (r2-n2).

The `proposal_file` beside it is r2-m1.

### m1: the disclosure pinned to the ruling's bytes

Code:

- `gcal.py:109-110`: `RULING_REL` and `RULING_SHA256`.
- `:258-266`: `disclosure_problems`.
- `:239`: called in precheck.
- `:804-805`: the self-test case.

Probe q3:

- `DISCLOSURE` equals the ruling's §1 italic span, with the backticks kept.
- The span occurs exactly once in the ruling.
- `disclosure_problems() == []`.
- The whitespace collapse at `:266` is a no-op on the pinned bytes, since the span has no whitespace runs. The check is
  therefore byte equality.

Mutants:

- E, the date reverted: KILLED. The direct check fails, and the stub runs now refuse in precheck.
- E2, precheck's call removed: SURVIVED (r2-n4).
- E3, the ruling's sha comparison removed: SURVIVED (r2-n4).

### m2: failing-case tests for the PROPOSAL-m pin

gcal:

- Code: `gcal.py:233-238`, two branches.
- Test: `:806-814`. M_PROPOSAL_SHA256 is patched to zeros, the run is REFUSED with "PROPOSAL-m v1.11's", and the
  factory is never called (asserted).

gshape:

- Code: `gshape.py:243-246`.
- Test: `:481-489`.

Mutants:

- A_hash_branch, A_both and S_A_no_mpin: KILLED.
- A_commit_branch (`if mcp or mdata is None:` → `if False:`): SURVIVED.
  - `_committed` returns `(problems, None)` on every failure (`stages.py:433-464`).
  - So the mutant raises `TypeError` in `hashlib.sha256(None)`: it fails closed before any write, with exit 1 instead
    of a refusal (r2-n4).

### m3: the STOP record's returned text

Two cases:

- `gcal.py:770-773`: the hair-trigger case now asserts `stop.returned_text == "a\nb"`.
- `:776-795`: the new `NoBreakIds` case. The decoded ids never hold the break, so the proxy raises ProxyStop through
  `run`. It asserts trigger `ProxyStop`, `returned_text == "x\ny tail"` whole, `launched == 1` and no record.

Mutants:

- B (trigger, `None`), C (ProxyStop, `None`), C2 (the old `getattr(e, "text")` name), P1 (the ProxyStop attribute
  `None`) and P3 (raised without the text): KILLED.
- P2 (the cut log's old key): KILLED by proxy's own test.

### m4: the declared orders

- `gcal.py:25-35` (ORDER), `scripts/p_sessions.py:20-33` and `gshape.py:27-29` each name the PROPOSAL-m pin.
- gcal's ORDER and the driver's list also name the disclosure check.
- As a set they are accurate.
- Pre-existing and harmless: the code accumulates P21's problems first (`:229`), while the docstring lists P21 after
  the disclosure. One refusal carries all of them.

### Short items

**n1.** q3: the docstring block at `report.py:23-25`, unwrapped, is byte-equal to the ruling's definition, with
backticks, `≥` and `≤` kept. The raw's path is on one line (`:21`).

**n2.** The PIN is at `report.py:27-30` and `spelling_words` at `:88-90`. The contraction case is `"I don't know"` against
`down` (`:164`). Mutant K (normalize, then split) is KILLED.

**n4.** Mutant H is KILLED. Mutant G SURVIVES (r2-n3).

**n5.** `report.py:192-193`: "the ruled definition's figures (corrupted spelling 0/3/5)".

**n7.**

- q3: term (e) at `register.py:14-19`, unwrapped, is byte-equal to the ruling's amendment.
- `__init__.py:4-6` reads "never by an unpinned copy (the register's one pinned restatement, entry (5), …)".
- Leftover: r2-n7.

**n9.** `report.py:96` reads `it["task"]`, so a task-less pool item raises `KeyError`.

- The served pool's 16 items all carry `task` (q5 prints them).
- Mutant N9 survives (r2-n4).

**n10.** `gcal.py:234-238`:

- "… hashes to `<observed sha16>`, not PROPOSAL-m v1.11's `<pinned sha16>` (the identity's proposal_sha256, F-p8)".
- When the file is not committed: "`<rel>` (the identity's proposal_sha256, F-p8): `<problems>`".

**n3 and n6.** F-p11 and F-p12 are in Code's drafted entry text (scratch). They are not in the repository, which is
expected while the entry is uncommitted. n3's class is also in code, at `report.py:33-37`.

---

## 2. Regression checks

### The counter on the 384 records: 0/3/5, unchanged (q2)

`counters()`, a direct `corrupted_spelling()` and the probe's re-implementation all give **sft 0, dpo 3, instruct 5**.
Split-then-normalize and normalize-then-split agree on every one of the 384 records.

| Unit | Record | Word | Gold | Distance |
|---|---|---|---|---|
| dpo | CORR_clean i=4 s=1 | `true` | `three` | 2 |
| dpo | CORR_corrupted i=8 s=2 | `januwy` | `january` | 2 |
| dpo | CORR_corrupted i=11 s=1 | `dn` | `down` | 2 |
| instruct | CORR_corrupted i=4 s=1 | `true` | `three` | 2 |
| instruct | CORR_corrupted i=7 s=1 | `irom` | `iron` | 1 |
| instruct | CORR_corrupted i=8 s=2 | `januwy` | `january` | 2 |
| instruct | CORR_corrupted i=8 s=3 | `janaury` | `january` | 2 |
| instruct | CORR_corrupted i=11 s=1 | `dn` | `down` | 2 |

This matches `report.py:30-33` item for item.

Each checkpoint's texts hold 8 multi-word normalized tokens, none near a gold. Examples: `don t`, `can t`, `i m`, and
`functions  /functions`. f0's `normalize` keeps `/` and does not collapse inner spaces.

### No refusal after a write

- gcal's two new refusals, the m pin and the disclosure, are in `precheck` (`gcal.py:233-239`).
  - The driver calls it first (`p_sessions.py:171`), before any write, load or print.
  - `run` calls it at `:447`, before the first checkpoint write at `:499`.
- `gate_record` runs while the entry is built, before `:499`.
- gshape's m pin (`gshape.py:244`) is in `inputs_of_record`. That is reached from `evaluate` (`:436`), before
  `write_once_bytes` (`:443`).
- The counter's new code runs in `artifact()` after the generations, as the old counter did.
  - Its only new exception path is n9's `KeyError`, which cannot occur with the served pool.
  - It would fire before the artifact's write, never after it.

### No model load or record write from a self-test

- The new gcal cases use `CharScriptedAdapter` stubs (`NoBreakIds`) in a `TemporaryDirectory`.
  `guard.refuse_test_out` refuses the repository as a test directory.
- The m-pin case's factory is never called (asserted `mp_calls == []`). Had it been called, it returns `None`, not an
  adapter.
- `gate_line`, `disclosure_problems` and `inspect.getsource` only read.
- gshape's new `a0` is `evaluate` in memory. The module's only write is `:443`.
- Both self-test runs left the tree identical, with nothing newer than the marker.

### Mutants (q4; `probes5/q4_out_a.txt`, `q4_out_b.txt`)

29 mutants: 20 KILLED, 9 SURVIVED.

| Mutant | Module (tests run) | Result | Bearing |
|---|---|---|---|
| A_hash_branch | gcal | KILLED | m2 |
| A_commit_branch | gcal | SURVIVED | r2-n4 (fails closed by TypeError) |
| A_both | gcal | KILLED | m2 |
| B_trigger_none | gcal | KILLED | m3 |
| C_proxystop_none | gcal | KILLED | m3 |
| C2_proxystop_oldname | gcal | KILLED | m3 |
| D_identity_p | gcal | KILLED | F-p8 identity |
| E_disclosure_date | gcal (gcal, gshape) | KILLED | m1 |
| E2_precheck_unwired | gcal | SURVIVED | r2-n4 |
| E3_no_ruling_sha | gcal | SURVIVED | r2-n4 |
| M1a_raw_gate | gcal | KILLED | M1 |
| M1b_keep_field | gcal | KILLED | M1 |
| M1c_second_copy | gcal | SURVIVED | r2-n2 |
| F_cut_unchecked | gcal | SURVIVED | pre-existing (round 1) |
| G_no_len2 | report | SURVIVED | r2-n3 |
| H_golds_lower | report | KILLED | n4 |
| K_normalize_then_split | report | KILLED | n2 |
| N9_task_get | report | SURVIVED | r2-n4 |
| J_threshold_lt3 | report | KILLED | |
| X_no_clean_words (in `corrupted_spelling`) | report | KILLED | |
| Y_no_function_words | report | KILLED | |
| Z_gold_itself_counts | report | KILLED | |
| W_counters_no_clean (in `counters`) | report | SURVIVED | r2-n4 (inert on the pool) |
| P1_stop_attr_none | proxy (proxy, gcal) | KILLED | m3 |
| P2_cut_old_key | proxy (proxy, gcal) | KILLED | F-p10 rename |
| P3_raise_no_text | proxy (proxy, gcal) | KILLED | m3 |
| S_A_no_mpin | gshape | KILLED | m2 |
| S_B_art_p_sha | gshape | KILLED | F-p8 |
| L_restatement_clause | register | SURVIVED | n11 (redundant guard; accepted) |

G-SHAPE-p's artifact, built in memory (q5), has verdict PASS. Its fields named `proposal*`:

- `proposal = "PROPOSAL-p"`
- `proposal_sha256 =` m's
- `proposal_p_sha256 =` p's
- `inputs.proposal_m = {path: PROPOSAL-m-gating-campaign-v1_11.md, sha256: m's}`

Its `disclosure` equals `gcal.DISCLOSURE`.

---

## 3. Findings

### MAJOR

None.

### MINOR

**r2-m1: The stored gate record keeps `proposal_file`, holding p's file. Under F-p8, that same field name will carry m's
file in p's later checkpoints.**

**Where.**

- `gcal.py:274-275` renames only `proposal_sha256`. The record keeps `proposal_file: PROPOSAL-p-olmo-told-controls-frame-dose-v0_2.md`
  (q1).
- m's stage machinery pairs the two fields:
  - `licence_problems` (`stages.py:529-563`): "(b) identity_extra's `proposal_file` … its sha256 is `proposal_sha256`
    (finding N2: the document read is the document the identity names)".
  - `_record_licence` (`stages.py:861-874`; `LICENCE_KEYS` includes `proposal_file`) records it in every stage
    checkpoint's `licence` block (`:1501`, `:1747`, `:2075`).

**Scenario.**

1. G-CAL-p writes `data/p/gates/G-CAL_completability_olmo-sft.json` once, with
   `/provenance[0]/gate/proposal_file = "PROPOSAL-p-…v0_2.md"`.
2. Later, at p §8 step 6, a p stage runs on m's stage machinery, as register entries (1)-(3) presuppose. F-p8 names
   "checkpoints" and "locks' identity blocks", so it runs with `proposal_sha256` = m's.
3. Its `proposal_file` must therefore be `PROPOSAL-m-gating-campaign-v1_11.md`, or m's licence refuses.
4. `data/p` then holds `proposal_file` meaning p's proposal in G-CAL-p's files and m's proposal in every later
   checkpoint's `licence`.

That is the state F-p8's stated reason forbids ("a reader of any file under `data/p/` must find one meaning per
field"), now for the sibling field. Round 1's M1 was the same class, in the same nested record.

Today no `data/p` file has a `proposal_file`: the committed G-SHAPE-p.json at `5009e77` has none. The G-CAL-p artifact
would be the first, and it is write-once.

**Fix.**

- In `gate_record`, also move `proposal_file` to `proposal_p_file`. The pair becomes `proposal_p_file` /
  `proposal_p_sha256`, as round 1's fix (a) proposed.
- Add `"proposal_file" not in stored` to the assertion at `:800-803`.
- Declare the record's form as a PIN (r2-n5).
- Alternatively, FLAG it to the seat before G-CAL-p runs. Either way the decision falls before the write-once artifact.

### NOTE

**r2-n1: The PIN's reading has its own false-positive class, which the docstring does not disclose.**

Split-then-normalize makes a gold's possessive, contracted or suffixed form one "word" within 2 of the gold. Probes q5
and q7; each of these is counted under the PIN and **not** under normalize-then-split:

| Answer | Word | Gold | Distance |
|---|---|---|---|
| "January's the first month." (straight or curly apostrophe) | `january s` | `january` | 2 |
| "Iron's heavier? No, the same." | `iron s` | `iron` | 2 |
| "Seven's", "Cold's", "Down's", "Shut's", "March's", "Three's" | `<gold> s` | `<gold>` | 2 |
| "Twenty-four's the answer" | `twenty four s` | `twenty four` | 2 |
| "the twenty-fourth" | `twenty fourth` | `twenty four` | 2 |

The other reading's cost is the one the PIN cites: "Don't know" (`don`~`down`, distance 1) and "I won't say: down"
(`won`~`down`, distance 2). On the 384 records the two readings agree.

Two members of n3's class are the most answer-like:

- "Close." for item 15 (`close`~`closed`, distance 1). It is a valid antonym of "open", and it is graded a miss.
- "Colder." for item 5 (`colder`~`cold`, distance 2).

Suggestion: add both classes to F-p11 and to the PIN's text, so the seat sees each reading's cost before G-CAL-p records
its counters. The counter is descriptive (rule 23) and recomputable.

**r2-n2: M1's guard is structural, not a walk.**

- `gcal.py:796-803` tests `gate_record` and source-matches `'"gate": gate_record(pre["gate"])'` in `run`.
- Mutant M1c adds `"gate_m": pre["gate"]` to the entry. It passes 27/27, yet on the box it would put p's sha back
  under a `proposal_sha256` in both files.
- Round 1's walk test guards any future field: inject the real record into a stub run's precheck, walk the artifact and
  the checkpoint, and assert every `proposal_sha256` is m's (and, with r2-m1, no `proposal_file`).
  `probes5/q1_gate_walk.py` is a working template.
- The source match also fails on a mere reformat. That fails closed.

**r2-n3: n4 is only partly fixed; the length clause's witness is vacuous.**

- `report.py:155` and `:164` claim "a one-letter word is no candidate ('a' against gold 'ab')".
- But `a` is in FUNCTION_WORDS, p §1.1's list. So the case passes with `len(w) >= 2` removed: mutant G survives 7/7.
- `not corrupted_spelling("b", ["ab"])` is a real witness. `b` is no function word and its distance to `ab` is 1, so
  it counts without the clause and does not with it (q7).
- On the pool the clause is inert. The only spelling gold of three letters or fewer is `two`, and no one-letter word is
  within 1 of it.
- So the gap is the label's claim, not a live risk.

**r2-n4: Five new behaviours have no failing case. Each fails closed or is inert on the pool of record.**

| Mutant | Where | What happens if it is broken |
|---|---|---|
| A_commit_branch | `gcal.py:234` | `TypeError` before any write |
| E2 | precheck's disclosure call, `:239` | drift is still caught by the direct check at `:804` |
| E3 | the ruling-sha branch, `:261` | no failing case |
| N9 | `it["task"]`, `report.py:96` | no failing case |
| W | `counters` passing `clean`, `report.py:126` | inert on the pool (below) |

W is inert because the exclusion's whole domain on the pool is one pair: `hot` (item 5's task) within 2 of `shut`
(item 15's gold) (q6). Optional cases:

- `_committed` patched to fail for `M_PROPOSAL_REL`;
- `DISCLOSURE` patched, expecting a run REFUSED;
- `RULING_SHA256` patched;
- a task-less pool, expecting `KeyError`;
- a counters record for item 15 answering "hot".

**r2-n5: The stored gate record's form is not in gcal's PIN register.**

- The module's PINs (`gcal.py:37-46`) state F-p8 for the identity only.
- `:16-17` still describes the artifact as "m's schema with `proposal_p_sha256` and the `p` block".
- But `provenance[].gate` is no longer m's form. m's artifacts have `proposal_file` + `proposal_sha256`; p's have
  `proposal_file` + `proposal_p_sha256`.
- Declare the form, with r2-m1's choice, where LOCK-p v0.1 will quote it.

**r2-n6: `proposal` sits beside `proposal_sha256` with a different referent.**

- The identity (`gcal.py:283`) and G-SHAPE-p's top level (`gshape.py:356`) carry `proposal: "PROPOSAL-p"` next to
  `proposal_sha256` (m's).
- One meaning per field still holds: `proposal` is always p's name. But the natural reading pairs the two fields.
- `__init__.py:31-32` still says p's records carry "a ``proposal`` field carrying p's sha256 (ans2 Q4 (ii))". That
  paraphrases ans2, but after F-p8 p's sha is in `proposal_p_sha256` and `proposal_sha256` is m's.
- The dated note and LOCK-p v0.1 should state all three fields and their referents.

**r2-n7: Two leftovers.**

- `register.py:40`: RegisterStop's docstring still says "a STOP, never a copy". Term (e) now reads "never an unpinned
  copy".
- `gshape.py:29` is 177 characters, from m4's insertion. The file's other lines are at most 126.

**r2-n8 (optional): Two things the artifacts do not say about themselves.**

- `DIAGNOSTIC_FIELDS` (`proxy.py:34`, `gcal.py:115`) is declared but recorded nowhere in the artifact.
  `p.stored_text_invariant.cuts[]` carries `returned_text`, line break included, without marking it diagnostic. The
  ruling requires the declaration only in the BUILD entry and LOCK-p v0.1. A key such as
  `"diagnostic_fields": ["returned_text"]` in that block would make the write-once artifact self-describing.
- gshape writes `gcal.DISCLOSURE` (`gshape.py:399`) without its own `disclosure_problems()` call. The pin binds through
  gcal's self-test and G-CAL-p's precheck.

---

## Summary

Round 1's dispositions are applied at source and hold under probe.

- **M1 is fixed.** With m's real gate-line record injected, G-CAL-p's artifact, checkpoint and resumed checkpoint each
  carry exactly one `proposal_sha256`, holding m's sha. p's sha now sits in `provenance[].gate.proposal_p_sha256`, and
  no m or analyzer code reads the renamed field.
- The four MINORs are fixed: the disclosure is pinned to the ruling's committed bytes; the m-pin refusal has failing
  cases in gcal and gshape; the STOP record's `returned_text` is asserted on both paths; the order docstrings name the
  new checks.
- The NOTEs are fixed, accepted or flagged, except n4, which is partly fixed.
- The self-test is 109/109 at both HEADs and writes nothing to the tree.
- The counter gives 0/3/5 on the 384 records, with no record differing between the two tokenizations.
- No new refusal comes after a write. No self-test path can load a model or write under the repository.
- Of 29 mutants, 20 are killed.

New findings: **0 MAJOR, 1 MINOR, 8 NOTE.**

- **r2-m1:** the gate record's `proposal_file` still names p's file. m's licence pairs `proposal_file` with
  `proposal_sha256`, so p's later stage checkpoints will carry m's file under that name. That is F-p8's two-meanings
  state for the sibling field, in a write-once artifact. Rename it to `proposal_p_file`, or FLAG it, before G-CAL-p
  runs.
- **NOTEs:**
  - the PIN's undisclosed `<gold>'s` / `twenty-fourth` false positives, and `close`/`closed`, for F-p11;
  - the structural M1 guard;
  - the vacuous length witness;
  - five untested fail-closed branches;
  - the undeclared gate-record PIN;
  - the `proposal`/`proposal_sha256` pairing and `__init__`'s wording;
  - two wording/format leftovers;
  - an optional self-describing diagnostic declaration.
