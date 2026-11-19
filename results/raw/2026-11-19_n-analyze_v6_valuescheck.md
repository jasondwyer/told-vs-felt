# n_analyze.py, the seat's ruling of the third sitting and ADDENDUM-n2 carried in: the blind values-check, two passes (PI date 2026-11-19)

Code's raw for the entry `n package — scripts/n_analyze.py, the seat's ruling of the third sitting and ADDENDUM-n2
carried in`.

**Who checked what.** Two blind values-checkers checked six texts against their sources, claim by claim, and the
second also checked this raw's first part (this head and Code's dispositions of the first pass):
- the entry;
- the three close lines, on the entries of `bfc869f`, of `ADDENDUM-n2 v0.1 — COMMITTED` (`7a54eb9`) and of `6e3474d`;
- the review raw;
- the analyzer's new and changed texts: its registers, its constants' comments, and the docstrings, comments and
  check descriptions the change touched.

Each checker was a subagent of this session, and its brief allowed no interpreter. The brief quoted the list of record
v2's items 1–5, with item 4's two amendments (C.2 of 2026-11-16, and the fourth sitting's §6.2). It also carried the
standing lines:
- item 3's pathspec with `':!data/mf3/**'`, even for a named file;
- a glob expanded and read before it is looped over;
- no listing of `results/raw`;
- a tracked-and-clean check by `rev-parse` against `hash-object`.

The two passes:
- The first pass checked the first drafts.
- The second pass checked the drafts as revised after the first, and whether each of the first pass's dispositions
  was carried and is true.
- With no FAIL, the second pass is the last. The edits after it are checked by tool (its dispositions).

**What the passes changed in the analyzer.** The passes changed seven texts in the analyzer, none of them code: five
after the first pass and three after the second, PIN-n-38 after both. All came after its mutation testing (the review
raw's §5). The run of record is on the final bytes.

**Their departures.** Each checker disclosed its own departures, and each report carries them. The entry names them
for the seat to class.

**How the reports appear.** Each report is reproduced whole and followed by Code's dispositions. The reports are the
checkers' hand-back messages, taken from the subagents' transcripts by script. The checkers write their briefs'
labels, SCRATCH for Code's scratch folder and REPO for the repository, and no literal path.

## Pass 1: the report, as saved from its hand-back (unedited)

# Blind values-check: the v6 entry, three close lines, the review raw and n_analyze.py's new texts

There are 217 claims: **187 CONFIRMED, 9 IMPRECISE, 3 FAIL, 18 NOT CHECKABLE.** Claims about the run of record and the commit are graded "pending" as the brief asks.

## The three FAILs

1. **close_bfc869f L14–15** says the entry flags "one reading of §6". The entry flags three readings in PIN-n-37, (a) to (c), each resting on §6. PIN-n-37 itself says "Three readings here are Code's".
2. **entry L21–25** says, under "The file", that both sittings' answers are cited by path. The analyzer cites the third sitting's raw in four places. It has no reference to the fourth sitting at all: 0 matches for its file name or for "fourth sitting". bfc869f's entry uses the same wording for a path the file does cite.
3. **review.md L66** says the reviewer's report "writes SCRATCH … and REPO". The saved report contains neither word (0 and 0 matches); it names the folders by description.

## Inputs

- All six texts match their given prefixes: entry 359ec9b23d59c754, close_bfc869f 08e04f9d43e350dd, close_addendum_n2 3bcd2461b875ce70, close_6e3474d 63ec4b2c097d1c92, review 754d1300310ada6f, final/n_analyze.py 2d75c11e96360933 (full `2d75c11e…c294`).
- The brief matches its full sha256.
- HEAD is `003ae7d`. schema.py, runner.py, ADDENDUM-n2, both answers raws and the PI-routing raw are tracked and clean (rev-parse HEAD:path equals hash-object), and each equals its `003ae7d` blob.
- HEAD's scripts/n_analyze.py is still `bfc869f`'s blob, and SCRATCH/base-bfc869f.py equals it.

Source digests, all as the texts cite them:

| File | sha256 |
|---|---|
| base | `3d22da1d…d048` |
| d1 = review copy | `0e459d7d…cfddc` |
| d2 = mutant base | `b605b91f…4c2c` (full value also matches) |
| manifest | `abc1355e…20a8` |
| reviewer brief | `b0079a19…2323` |
| reviewer report | `acdc099d…55cd` |
| d1.out | `a10d5229…9c6b` |
| d2.out | `795b5f5a…8138` |
| kills.txt | `362a3b60…9f01` |
| ADDENDUM-n2 | `41f76c49…bb3f` |
| schema at 003ae7d | `5cbf60db…574c` |
| schema at d791bd9 | `0ea39600…0db6` |
| third sitting | `d51279ec…0bf4` |
| fourth sitting | `c265797f…61a5` |
| runner | `e8e81ab0…f787` |

## 1. entry.filled.md

- E1 L1: PI date 2026-11-19. CONFIRMED (matches the other texts; HEAD committed 2026-11-19).
- E2 L1–3: what is carried in (PIN-n-37 to the conservative form, the kind, the second row, the pin to `003ae7d`). CONFIRMED (base→final diff).
- E3 L3–4: grounds cited (third §6; routing item 5; A-n2 §2.1, §3, §6.3 (4); fourth §5). CONFIRMED (each section says that).
- E4 L4: battery 230/230. CONFIRMED, pending the run of record. d2.out gives 230/230, and final differs from d2 only at line 62.
- E5 L4–5: 44 of 45 killed. CONFIRMED (kills.txt has 45 lines, V11 "SURVIVED"; V11.out 230/230; the other 44 outputs each show FAILs).
- E6 L5–6: three readings in PIN-n-37, plus PIN-n-38 and -39, are Code's. CONFIRMED (PIN-n-37's text; the PINS comment).
- E7 L6: model-free, nothing on a model or box, no stage ran. NOT CHECKABLE.
- E8 L7–9: file sha; `3d22da1d…d048` at `bfc869f`. CONFIRMED.
- E9 L10–11: pin moved from `0ea39600…0db6` (d791bd9) to `5cbf60db…574c` (003ae7d). CONFIRMED (the base and final constants; git show d791bd9 schema | shasum).
- E10 L11–12: follow-up settled with this session and accepted by the fourth sitting's §5. CONFIRMED (RESULTS.md:52–53 "the form agreed with n-analyzer"; v2f's entry :921–924 "settled with n-analyzer. Names agreed so far"; §5's heading "the schema follow-up: accepted").
- E11 L13: kind directly after `nonfinite`. CONFIRMED (schema.py:1122).
- E12 L14–15: the rule gains ceiling, median_rel and alpha, and the counters gain the ceiling counter. CONFIRMED (schema.py:494–499 and 1205; none at d791bd9).
- E13 L15: the reader reads the first two and the counter. CONFIRMED (ceiling_of, median_of, report_problems).
- E14 L16: it reads neither alpha nor label_convention. CONFIRMED (only two comments mention them, at 2757 and 2848).
- E15 L16–17: batch alpha asserted beside p0. CONFIRMED (schema.py:1458–1460).
- E16 L17: every stage report passes through the schema's check. CONFIRMED (final:6112 `_load_checked(report, sm.check_report…)`; the battery's reports go through check_report in _bt_report_for).
- E17 L18: addendum sha; committed at `7a54eb9`. CONFIRMED.
- E18 L18–19: bound as ADDENDUM-n1 is (VERDICTS, NOT-RUN, artifact, battery). CONFIRMED (base dict, not_run_doc, ganl_artifact, BOUND_RELS, STR-ADDENDUM2-SHA).
- E19 L19–20: commands unchanged. CONFIRMED (main() to the end of the file is identical).
- **E20 L21–25: answers "cited by path" (third and fourth). FAIL**, as above. If the line means the entry's own links, it is true but misplaced under "The file".
- E21 and E22 L22–25: the two answers' shas and commits. CONFIRMED (each file's only commit is 3b2b855 or c7d0009).
- E23 L26–28: run of record 230/230, 233 ids, exit 0. CONFIRMED, pending the run of record. This is predicted by d2.out, with exit 0 by `return 0 if battery()["ok"] else 1`.
- E24 L29–30: routing raw ("Route as given") committed at `7a54eb9`. CONFIRMED.
- E25 L32: item 5 quote. CONFIRMED (byte-identical to the raw's line 23).
- E26 L35–36: a binomial pause stands on every read in its range, re-computed or not. CONFIRMED (§6; paused_points).
- **E27 L37: "every planned read of that session". IMPRECISE.** The code reaches the session's planned steered reads only, not N4's. PIN-n-37's qualifier "each read against it" is dropped here.
- E28 to E30 L38–42: single-read pauses; N1 and N4 per arm; the trials-only form struck; the binding unchanged. CONFIRMED (§6; the binding code is untouched in the diff).
- E31 L43: quote "Nothing changes in any outcome today". CONFIRMED (verbatim).
- **E32 L43–44: "the battery's synthetic campaigns, which carry no keyed-sample re-computation in N2's arms". IMPRECISE.** This holds for A's and C's campaigns (ck, c2). It does not hold for cg, cvc, cs3 and cr, all added in this change, which sample N2-E, N2-S or N2-C reads.
- E33 L44–46: A and C now leave N2 INDETERMINATE (pause:N2-E) on N2's six points, where bfc869f left it decided. CONFIRMED (final A and C expectations; base A and C have SHARED).
- E34 to E37 L48–55: ceiling test (both paths finite, strict); both-ways binding; "pauses at once" quote; F3; the counter and per-arm counters; identity bound = C, asserted by the schema and carried in the records. CONFIRMED (above_ceiling; schema.py:1056–1057, 854–856, 1062, 1692; A-n2 §2.1, §2.2).
- E38 to E41 L57–62: drops and over_half; the second row only where over half; median-emptied; §3's trigger replacing §1.4's quoted "where it empties". CONFIRMED.
- E42 to E48 L63–75: readings (a), (b) and (c), with their quotes and BINOMIAL_FIELDS; F1 reachable; "Before, it read the scope"; causes by arm under PIN-n-36 (accepted); N2-E not in A's scope. CONFIRMED. A's scope is its trial arms, N1-P, N4-T and N4-Ts.
- E49 L76–77: the binding follows R12 and R13. CONFIRMED (runner docstring FIDELITY BINOMIAL; 003ae7d's entry :139–146).
- E50 and E51 L78–82: PIN-n-38 and -39 readings; PIN-n-24 binds one way, as accepted. CONFIRMED.
- E52 L83: 222→230 checks, 225→233 ids. CONFIRMED (bfc869f's entry gives 225; eight new ids).
- E53 L84–87: the eight new checks. CONFIRMED.
- E54 L88–92: the rewritten checks (sixteen cases counted; D is new; VD-REFUSE's three cases; VD-SENSITIVITY; VD-PISTOP-STANDING). CONFIRMED.
- E55 L93: the schema's example defaults (C and the identity bound 0.25, median 0.01). CONFIRMED (schema.py:1595–1616).
- **E56 L93–94: "moved two battery inputs", naming F14 as one. IMPRECISE.** F14's inputs (0.01 and 1e-9) are unchanged. What moved is its expectation, from 2 exceedances to 0 of 480. Only A's hot read is a moved input.
- E57 L95: hot read 0.1, above TAU and below C. CONFIRMED (worked by hand: scale = 1 + |m| = 1.16, so rel = 0.086).
- E58 to E63 L97–107: the review's figures, the dispositions, 44 of 45, V11 equivalent, and the 13 killed by checks the dispositions added or extended. CONFIRMED (report.md; dispositions.md; each killing condition counts 0 in d1).
- E64 L108–109: the committed bytes differ in the repository line only. CONFIRMED as of now (d2→final is one hunk, at line 62). The values-check edits are pending.
- E65 L112: windows and bytes named first. NOT CHECKABLE.
- E66 L113–114: nice, -I, temp folders, foreground, venv by glob. NOT CHECKABLE. The one temp path printed anywhere (C10.out) is under SCRATCH/tmp, which is consistent.
- E67 L115–116: 227/227 and 230/230, one run each. CONFIRMED.
- E68 L116–118: window closed and reopened; three per call; manifest checked first. NOT CHECKABLE (the 45 files and the manifest do match).
- E69 L119: run of record: 1. NOT CHECKABLE, pending.
- E70 L121–122: Q-F3 beside; no other window open. NOT CHECKABLE.
- E71 L123–125: grounds for the three close lines. CONFIRMED (each header names n-analyzer; §8 item 5). The commit is pending.
- E72 L125–126: commit-time count 0 (§5.2). NOT CHECKABLE, pending the commit. The citation is right, and none of the six texts contains the home-folder prefix.
- E73 L126: not pushed. NOT CHECKABLE, pending the commit.
- E74 L126–127: Next. CONFIRMED (the module docstring and bfc869f's entry say the same).

## 2a. close_bfc869f.filled.md

- B1 to B6 (L1–12): PI date and grounds (§6, §8 item 5); path, sha and 3b2b855; this entry's PIN-n-37 (RESULTS.md:1112, 1165); routing item 5 at 7a54eb9; the sha; the rule restated; the narrower form struck; the binding stands. All CONFIRMED.
- **B7 L14–15: "one reading of §6". FAIL**, as above.

## 2b. close_addendum_n2.filled.md

- A1 to A6: grounds (the header names n-analyzer; §6.3 (4)); the binding as ADDENDUM-n1's; §2.1 on schema 003ae7d (PIN-n-39); §3's drops and over-half trigger (PIN-n-38); both readings flagged in the entry. All CONFIRMED.

## 2c. close_6e3474d.filled.md

- C1 L1–2: header plus §10 item 4. CONFIRMED (item 4 sits in n-build's group but asks for "close lines").
- C2 L2–4: path, sha, c7d0009, §5. CONFIRMED.
- **C3 L4–5: the lead-in "accept the names the n-build and n-analyzer sessions settled" covers all three bullets. IMPRECISE.** Only bullet 1's names were settled by the sessions (v2f's entry: "Names agreed so far"). Alpha is the seat's addition ("joins them"), and the convention of record is §5's own ruling.
- C4 and C5: bullets 1 and 2. CONFIRMED (§5).
- **C6 L9: "directly after `non-finite` in `schema.PAUSE_KINDS`". IMPRECISE.** That is the seat's spelling, but the tuple's member is "nonfinite" (schema.py:1122), as the entry writes it.
- C7 to C10: reads the first three at this commit; reads neither alpha nor label_convention; batch alpha asserted beside p0 (003ae7d's note); reports pass through check_report. CONFIRMED.

## 3. review.md

**Head**
- R1 to R6: title; entry title; base `bfc869f` (the review diff's body equals diff base d1); the citations of the third sitting, ADDENDUM-n2 and the pin. CONFIRMED.
- R7 "drafted in one step", R10 "read-only", R11 "a subagent of this session": NOT CHECKABLE.
- R8 and R9: 227/227 (d1); frozen copy sha, 230 ids. CONFIRMED.
- R12 and R13: the brief's sha, its quoted rules and standing lines, no interpreter, its spec list. CONFIRMED (review/BRIEF.md:13–35, 88–123).
- R14: the reviewer's commands; wrote no file; nothing under data/. CONFIRMED (the summary leaves out its `head` pipes and grep loop, which its report lists).
- R15 to R20: findings and severities; the 14 named survivors; the dispositions; the three new checks; the mutant set and result; §5; tallies and the forms' digest. CONFIRMED.
- R21: the Python runs' terms. NOT CHECKABLE.
- R22: each mutant one exact replacement. CONFIRMED in effect: each of the 45 files is one hunk off d2, and every anchor occurs once. The assertion itself is not checkable.
- R23: hashes named, and per-file checks. NOT CHECKABLE (the manifest re-hash diff is empty).
- R24: "Killed" means a non-zero exit. CONFIRMED (the battery returns 1 when not ok).

**§1**
- R25: §1 is reproduced whole and unedited, sha `acdc099d…55cd`. CONFIRMED (lines 68–446 are byte-identical to review/reviewer/report.md).
- R26: "taken from the subagent's transcript by script". NOT CHECKABLE.
- **R27 L66: "It writes SCRATCH … and REPO". FAIL**, as above.
- R28: the report's anchors, spot-checked. CONFIRMED.
  - 30 cited d1 line numbers land as stated.
  - d1's "fifteen cases" holds.
  - The rel table and the counts 81, 160, 82, 25 and 24 hold when worked by hand.
  - 227 = 222 + 5.
  - F14 gives 0 of 480.
  - All 35 old texts occur once in d1.
  - The runner's clear_batch calls are at runner.py:449–451 and 526–530.

**§2** (equals dispositions.md)
- R29 to R43: F1 to F6 and B1 to B9 as applied. CONFIRMED (d1→d2 diff).
- **R44: "D samples N2-S's first read alone". IMPRECISE.** D samples two reads, N2-E's last and N2-S's first. What changed is that N2-C's run-7 sample was removed.
- **R45: "Code's own additions before the review, in the fixed draft too: …". IMPRECISE.**
  - All four checks are absent from d1 (0 matches in d1, 1 in d2).
  - The same four are credited above to B2, B5, B6 and F3, and §3 credits their kills to the dispositions.
  - ceiling-unpaused is F3's own fix: C27 "was written on d2".
  - Code's pre-review spec (mutants_c.spec, C15, C16 and C22) does predict kills by the first three, which supports a pre-review plan for those.
- R46 and R48: V35 re-expressed (its old text is in d1, not d2); the 17 duplicates, the nine others and C27. CONFIRMED.
- R47 "written before the review": NOT CHECKABLE.

**§3**
- R49 and R50: the base; the manifest (45 files). CONFIRMED.
- R51 manifest checked by the coordinating session, and R52 three per call over fifteen calls: NOT CHECKABLE.
- R53 to R62: CONFIRMED.
  - The table equals raw/kill_table.md, and its rows agree with kills.txt and the specs (V30 differs only by the table's escaped pipe).
  - The V11 reasoning holds.
  - V35 fails on ['D'].
  - C10's FileNotFoundError and C24's KeyError 'addendum2_sha256' are in their outputs.
  - The blocks equal mutants_v35r.spec and mutants_c_run.spec.
  - Code's anchors occur once in d2, and C27's is absent from d1.

**§4**
- R63 to R66: the d1, d2 and mutant rows; the run-of-record sha. CONFIRMED. Exits are inferred from the return rule. The result is pending the run of record.
- R67: window and Q-F3 sentences. NOT CHECKABLE.

**§5**
- R68: the REPO line is the only difference; the drafts carried an absolute path. CONFIRMED.
- **R69: "No difference touches code a mutant reads." IMPRECISE.** No mutant alters line 62 (their hunks lie at lines 72–6176), but every run executes that line. What holds is that it computes the same root at the committed path.
- R70: CODE_FORMS_SHA256 is the base's. CONFIRMED.

**§6**
- R71: `41d0d654…b1da` is identical in base, d1, d2 and final; no hunk touches a form; 2,561. CONFIRMED.

## 4. final/n_analyze.py texts (48 CONFIRMED, 1 IMPRECISE)

- CONFIRMED: the module docstring's PINS paragraph and its "PIN-n-7 to PIN-n-37 ruled"; the comment above PINS; the reader header; the ADDENDUM2_REL, ADDENDUM2_SHA256, SCHEMA_SHA256, CEILING_KEY, MEDIAN_KEY and CEILING_COUNTER constants and their comments; ceiling_of, median_of and schema_module; PIN-n-37 (quotes verbatim, PIN-n-24's included); PIN-n-39 (quotes verbatim apart from the addendum's bold).
- **PIN-n-38: IMPRECISE.** It says reads drop "by their own re-computation or their session's shadow's" for every arm, but N4's drop by their own only (row_drops: "for a steered read"). Its three quotes are verbatim.
- CONFIRMED: the docstrings of State (unusable, at), _causes, n2_outcome, build_state (the slope path uses `emptied`), counters, tau4_drop (unchanged), median_drop, row_drops, over_half, above_ceiling (the same test as runner.py:201–202), secondaries, report_counters, report_problems, paused_points, run_verdicts, _bt_files, _bt_report_for, _bt_write_campaign and _bt_sec_shift (its rel values hold when worked by hand).
- CONFIRMED: the descriptions and comments of RD-PAUSE-POINTS (16 cases), RD-CEILING, RD-SECOND-ROW, RD-SENSITIVITY/F14, VD-PAUSE-POINTS A–D, VD-SECOND-ROW, VD-CEILING, VD-SECOND-ROW-TRIGGER, VD-SECOND-ROW-PAUSE, VD-BATCH-CLEARS, VD-REFUSE, VD-SENSITIVITY, VD-PISTOP-STANDING, CMD-NOTRUN, STR-GANL-ARTIFACT, STR-ADDENDUM2-SHA and A's hot-read comment. Each description matches its condition, and d2 passes them all.

## Counts

| Text | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|
| Entry (74) | 62 | 3 | 1 | 8 |
| close_bfc869f | 6 | 0 | 1 | 0 |
| close_addendum_n2 | 6 | 0 | 0 | 0 |
| close_6e3474d | 8 | 2 | 0 | 0 |
| Review raw (71) | 57 | 3 | 1 | 10 |
| Analyzer (49) | 48 | 1 | 0 | 0 |
| **Total (217)** | **187** | **9** | **3** | **18** |

## Observations

1. **The count of Code's readings differs across texts:** three in the entry, one in close_bfc869f, two in the review head. The head means two findings were kept unapplied; F2's fix is itself reading (c).
2. **`nonfinite` (entry, schema) vs `non-finite`** (close_6e3474d, the seat's spelling).
3. **Fixing E20** means either citing the fourth sitting in the analyzer where the schema's names are read, or moving the line out of "The file".
4. **A possible missing disclosure.** The review raw says the reviewer's report was "taken from the subagent's transcript by script". 003ae7d's entry declared transcript greps as a departure (RESULTS.md:175–178), and this entry has no departures line. Code's scratch also holds Perl scripts (review/apply_all.pl, splice.pl, msgs.pl, cmds.pl, fillbrief.pl); the texts state only the Python runs' terms. I did not read or run those scripts.
5. **The entry's list of altered checks omits** VD-COMPLETE, CMD-NOTRUN and STR-GANL-ARTIFACT, all extended for the addendum's binding.
6. **Cosmetic only:** short wrapped lines in the docstring (final:21) and in two description strings.

## Commands beyond reading files and the brief's git forms

- `shasum -a 256` on scratch files and on eight named repository files, none under data/.
- Name-only `ls` of scratch folders only.
- `wc -l`, `diff` / `diff -u` (including over process substitution), `cut`, `tr`, `rev`, `head`, `tail`, `cat -n`, `printf`, `echo`, `[ ]`.
- zsh loops over names I had listed and read first.
- `/usr/bin/grep` inside named single files only, never recursive.
- `sed -n` for line ranges, and `sed -e` only to mask the home path in printed output.
- **A departure:** I ran `awk 'NR>=a && NR<=b'` twice on RESULTS.md as a line filter. awk is an interpreter.
- One `echo ====` triggered a zsh `=` expansion error, with no other effect.
- One loop was refused by the harness's safety check before it ran (on zsh modifier syntax; it contained no removal), and I rewrote it.
- Files written only to SCRATCH/vc/checker/: diffs, two section copies, header and name lists, a re-hash. Two `diff -u` headers there first carried the scratch files' modification times; I rewrote them without those lines.
- Git:
  - `git rev-parse <rev>:<path>`, `git hash-object --` and `git rev-parse HEAD` without item 3's pathspec (the brief's tracked-and-clean form, plus bfc869f: and 003ae7d: variants).
  - `git show <rev>:valence_core/n/schema.py` at d791bd9, bfc869f and 003ae7d without the pathspec.
  - `git log --format` and `git show --name-status` with item 3's pathspec plus `':!data/mf3/**'`.
- Nothing under data/ was touched; no git status; no model process.


## Pass 1: Code's dispositions

Pass 1 checked 217 claims: 187 CONFIRMED, 9 IMPRECISE, 3 FAIL and 18 NOT CHECKABLE, with six observations. Every FAIL
and IMPRECISE item is applied, and so are the observations, as follows.

#### The FAILs

1. **close_bfc869f, "one reading of §6".** Now: the commit's entry flags three readings in PIN-n-37 as Code's, for the
   seat, and names them.
2. **The entry, "cited by path" (the fourth sitting).** The analyzer now cites the fourth sitting's answers by path,
   in the comment above CEILING_KEY, where the names the seat accepted are read (an analyzer text, the review raw's
   §5).
3. **The review raw, "It writes SCRATCH … and REPO".** Now: the report names Code's scratch folder and the repository
   by description, as its brief asked.

#### The IMPRECISE

- **E27, "every planned read of that session".** Now "every planned steered read of that session, each read against
  it".
- **E32, the synthetic campaigns.** Now scoped to the campaigns of scenarios A and C. The sentence also says why no
  outcome of record changes: no campaign has run.
- **E56, "moved two battery inputs".** Now "one battery expectation and one input": F14's inputs are unchanged and
  its expectation moved, and scenario A's hot read is the moved input.
- **C3, the close line on 6e3474d.** Now §5's three parts are told apart: the names the sessions settled, accepted;
  `alpha` and the convention of record, the seat's additions; the kind's place, as the sessions had it.
- **C6, "non-finite".** Now `nonfinite`, the tuple's member.
- **R44, D's sampling.** Now: D no longer samples an N2-C read (it samples N2-E's last read and N2-S's first).
- **R45, "Code's own additions before the review".** Now "made while the review ran, and so absent from the frozen
  copy", with B2, B5 and B6 asking for the same afterwards, and `ceiling-unpaused` F3's.
- **R69, "No difference touches code a mutant reads".** Now: no mutant's change lies in a region that differs; the
  repository line runs in every battery run and computes, at the committed path, the root the drafts' line gave.
- **PIN-n-38, the shadow's drop for every arm.** Now "or, a steered read, its session's shadow's" (an analyzer text).

#### Observations

1. **The count of Code's readings.** The texts now agree:
   - the entry and the close line on bfc869f name PIN-n-37's three readings (a)–(c);
   - the review raw's head says F1 is kept as reading (b) and F3's converse for the other kinds is not applied, each
     put to the seat, and that F2's fix is reading (c).
2. **`nonfinite` against "non-finite".** The code's token is `nonfinite` wherever a text names the tuple's member.
   The prose keeps "non-finite" for the kind's meaning, as PIN-n-37 and the seat's texts do.
3. Applied with FAIL 2.
4. **The missing disclosure.** The entry gains a departures bullet for the seat to class:
   - Code's reads of this session's own transcript, by Perl;
   - its two reads of the n-build session's record through the session tool;
   - the hand-backs taken from the subagents' transcripts;
   - its Perl, shell and `awk` tools over its scratch files and RESULTS.md.
5. **The altered checks.** The entry's list now names VD-COMPLETE, CMD-NOTRUN and STR-GANL-ARTIFACT, for the
   addendum's binding.
6. **The short wrapped lines.** The module docstring's paragraph and the descriptions of VD-CEILING and
   STR-GANL-ARTIFACT are rewrapped (analyzer texts).

#### The checker's departures (for the seat to class)

The checker disclosed them in its report. None read anything under `data/`, and none touched `data/mf3`:
- two `awk` line filters over RESULTS.md (an interpreter);
- git digests and blob shows, in the brief's tracked-and-clean form, without item 3's pathspec;
- `diff -u` headers that carried two scratch files' modification times into its own scratch files, which it rewrote
  without them;
- a zsh `=` expansion error and one loop the harness refused before it ran.

## Pass 2: the report, as saved from its hand-back (unedited)

# Blind values-check, second pass: the v6 entry, three close lines, the review raw, n_analyze.py's new texts and the values-check raw's first part

I checked 256 claims: **224 CONFIRMED, 7 IMPRECISE, 0 FAIL, 25 NOT CHECKABLE.** Claims about the run of record and the commit are marked "pending", as the brief asks. The placeholders @@VC_LINE@@ (entry L115) and @@REC_RESULT@@ (review.md L671) were skipped.

None of the seven IMPRECISE items is in the analyzer. Every edit made after mutation testing checks out (§4). Every disposition of the first pass is carried. All are true, with two nuances: C3's third part (C5/D9 below), and the PIN-n-38 fix, which reached the analyzer but not the entry's summary (E50).

## Inputs

- **The eight texts and the source.** All eight match their given prefixes: entry 11d136f3…, close_bfc869f bf4bff99…, close_addendum_n2 e8cfd8a5…, close_6e3474d 51dde856…, review 14be1a62…, final 5c275c52… (full value `5c275c524674f6579ac845035bbca8a575596df3872d545980412fe77a42294b`), vc_head 2bedf41d…, pass1_dispositions b0a5eaf9…. The source pass1.md (63dad5ab…) matches too. BRIEF2.md matches its full sha256.
- **Source digests.** Each is as the texts cite it:
  - base 3d22da1d…d048. `git hash-object` of SCRATCH/base-bfc869f.py equals bfc869f:scripts/n_analyze.py.
  - d1 = the review copy, 0e459d7d…fddc.
  - d2 = the mutant base = work/n_analyze.py, b605b91f…4c2c (full value matches).
  - manifest abc1355e…20a8.
  - reviewer's brief b0079a19…2323; report acdc099d…55cd.
  - d1.out a10d5229…9c6b; d2.out 795b5f5a…8138; kills.txt 362a3b60…9f01.
- **Repository state.** HEAD is now da7bdec (n-build's G-VEC BUILD), which came after pass 1's 003ae7d.
  - da7bdec touched none of the cited sources. schema.py and runner.py are 003ae7d's blobs, and scripts/n_analyze.py is still bfc869f's blob.
  - Every named source is tracked and clean (rev-parse HEAD:path = hash-object). That covers schema.py, runner.py, ADDENDUM-n2, the second, third and fourth sittings, the PI routing raw, PROPOSAL-n v0.2 and RESULTS.md.
  - RESULTS.md line numbers below are at da7bdec.

## 1. entry.filled.md

- **E1 L1** PI date 2026-11-19 — CONFIRMED (today; HEAD da7bdec is dated 2026-11-19).
- **E2 L1–3** What is carried in: PIN-n-37's conservative form, the kind, the second row, and the pin moved to 003ae7d — CONFIRMED (base→final diff).
- **E3 L3–4** The grounds: third sitting §6; routing item 5; A-n2 §2.1, §3 and §6.3 (4); fourth sitting §5 — CONFIRMED (each section says so).
- **E4 L4** Battery 230/230 — CONFIRMED, pending the run of record. d2.out gives 230/230. Final differs from d2 only in review §5's six regions, and none of them alters a check's logic.
- **E5 L4–5** Reviewed blind; 44 of 45 killed — CONFIRMED. kills.txt has 44 killed rows and "V11 | SURVIVED". V11.out is 230/230; every other output falls short.
- **E6 L5–6** Three readings in PIN-n-37, plus PIN-n-38 and PIN-n-39, are Code's — CONFIRMED (final:2522–2526; PINS comment at final:2397–2399).
- **E7 L6** Model-free; no stage ran — NOT CHECKABLE.
- **E8 L7–9** The file's sha; 3d22da1d…d048 at bfc869f — CONFIRMED.
- **E9 L10–11** Pin moved from d791bd9's 0ea39600…0db6 to 003ae7d's 5cbf60db…574c — CONFIRMED (`git show <rev>:schema.py | shasum`; base:2730 against final:2766).
- **E10 L11–12** Settled with this session and accepted by the fourth sitting's §5 — CONFIRMED. RESULTS.md:199 says "the form agreed with n-analyzer", v2f's entry :1068 says "settled with n-analyzer", and §5 is headed "accepted".
- **E11 L13** The kind sits directly after `nonfinite` — CONFIRMED (schema.py:1122).
- **E12 L14–15** The rule gains ceiling, median_rel and alpha; the counters gain the ceiling counter — CONFIRMED (schema.py:494–499 and :1205).
- **E13 L15** The reader reads the first two and the counter — CONFIRMED (final:2839–2851; report_counters; report_problems :5830).
- **E14 L16** It reads neither alpha nor label_convention — CONFIRMED. "alpha" appears only in one comment (final:2757); label_convention appears nowhere.
- **E15 L16–17** The schema asserts batch alpha beside p0 — CONFIRMED (schema.py:1459–1460 and :180).
- **E16 L17** Every report reaches the reader through check_report — CONFIRMED (final:6111 `_load_checked(report, sm.check_report…)`; `_bt_report_for` calls sm.check_report).
- **E17 L18** The addendum's sha; committed at 7a54eb9 — CONFIRMED (its only commit).
- **E18 L18–20** Bound as ADDENDUM-n1 is — CONFIRMED (VERDICTS :6133, not_run_doc :4350, ganl_artifact :5440, BOUND_RELS :5394, STR-ADDENDUM2-SHA :2696).
- **E19 L19–20** The commands are unchanged — CONFIRMED. main, run_ganl, run_not_run, not_run_precheck, verdicts_precheck and verdicts_line are byte-identical to the base.
- **E20 L21** Both answers cited by path — CONFIRMED.
  - The third sitting is cited at final:19, 2397, 2511 and 5435.
  - The fourth is cited at final:2837, and is absent from the base and from d2.
- **E21 L22–23** d51279ec…0bf4 at 3b2b855 — CONFIRMED.
- **E22 L24–25** c265797f…61a5 at c7d0009 — CONFIRMED.
- **E23 L26–28** Run of record: 230/230, 233 ids, exit 0, and the raw — CONFIRMED as predicted by d2.out ("233 required ids reached"); exit by `return 0 if battery()["ok"] else 1`. Pending the run and the commit.
- **E24 L29–31** "Route as given", committed verbatim at 7a54eb9 — CONFIRMED.
- **E25 L32** The item 5 quote — CONFIRMED. It equals the raw's line 23 whole, apart from its leading space.
- **E26 L35–36** A binomial pause stands on every read in range, re-computed or not — CONFIRMED (§6; final:5970–5972).
- **E27 L37–38** "Every planned steered read of that session, each read against it" — CONFIRMED (final:5975–5979 loops STEERED_ARMS over camp.planned).
- **E28 L39–40** Single-read pauses — CONFIRMED (§6).
- **E29 L41** N1's and N4's pauses per arm — CONFIRMED (§6).
- **E30 L42–43** The trials-only form struck; the binding unchanged — CONFIRMED. The `cleared`, `first_w` and `last_w` lines and the batch message each occur once, identically, in base and final.
- **E31 L44–46** A's and C's campaigns have no keyed sample in N2's arms, so the batch stands on N2's six points — CONFIRMED. ck (:4740) and c2 (:4676) are written without `sampled`; the expectations are at :4784 and :4790.
- **E32 L46** A and C now give N2 INDETERMINATE (pause:N2-E), where bfc869f decided — CONFIRMED (base A and C expectations had SHARED).
- **E33 L46–47** No campaign has run; the §6 quote — CONFIRMED. RESULTS.md:273 says "No campaign report exists"; the quote is verbatim.
- **E34 L49–50** The ceiling test (both paths finite, strict) — CONFIRMED (above_ceiling :3414–3419; absdiff is null where a path is non-finite).
- **E35 L51–52** Bound both ways; "pauses at once"; F3 — CONFIRMED (:5880–5881, :5889–5894; A-n2 §2.1).
- **E36 L53–54** The counter is bound; the record counters — CONFIRMED (:5830, :3365).
- **E37 L55–56** The identity bound is C, asserted by the schema and carried by the records — CONFIRMED (A-n2 §2.2; schema.py:854–856 and :1062).
- **E38–E40 L58–62** drops and over_half; second_row only where a point is over half, strictly; median-emptied — CONFIRMED (:6170–6182, :6201–6202).
- **E41 L63** The trigger replaces §1.4's "where it empties" — CONFIRMED (the second sitting §1.4 verbatim; A-n2 §3).
- **E42 L64** Registered and strikable until LOCK-n v1.0 — CONFIRMED.
- **E43 L66–67** Reading (a) — CONFIRMED (paused_points reads no arms_in_scope).
- **E44 L68–69** Reading (b): BINOMIAL_FIELDS and the §6 quote — CONFIRMED (schema.py:1175 "the first read of the trials counted").
- **E45 L69–72** F1 is reachable under PI-STOP — CONFIRMED (the reviewer's F1 scenario).
- **E46 L72** "If the seat means the runner's batch…" — CONFIRMED (F1's fix).
- **E47 L73–74** Reading (c); "Before, it read the scope" — CONFIRMED. final:581 replaced base:574 `bool(st.paused.get(a))`, and paused_from (:5946–5948) reads arms_in_scope.
- **E48 L75–76** Causes name the arm under PIN-n-36 (accepted); in A, N2-E is outside the scope — CONFIRMED.
  - PIN-n-36 names "a pause by its arm"; the second sitting §3.3 accepted it.
  - A's scope holds only the arms with trials in the batch: N1-P, N4-T and N4-Ts.
- **E49 L77–78** The binding follows R12 and R13 — CONFIRMED (runner docstring FIDELITY BINOMIAL; RESULTS.md:286 and :290).
- **E50 L79–81** PIN-n-38: "drops by a read's own re-computation or its session's shadow's" — **IMPRECISE.**
  - A session's shadow drops only a steered read. N4's reads drop by their own re-computation alone (row_drops :3405; build_state :3187).
  - The analyzer's PIN-n-38 now says so ("or, a steered read, its session's shadow's": pass 1's PIN-n-38 item). The entry's summary does not.
- **E51 L82–83** PIN-n-39 both ways; PIN-n-24 binds one way and was accepted — CONFIRMED (2026-11-16 answers §2, line 50).
- **E52 L84** 222→230 checks; 225→233 ids — CONFIRMED (EXPECTED_CHECKS; d1.out 230 ids, d2.out 233; bfc869f's entry 225).
- **E53 L85–88** Eight new checks — CONFIRMED (_REQ :1159–1170).
- **E54 L89–94** The rewritten checks — CONFIRMED. I counted sixteen cases; scenarios A–D; VD-REFUSE's kind-ceiling, ceiling-count and ceiling-unpaused; VD-SENSITIVITY; VD-PISTOP-STANDING; VD-COMPLETE :4580, CMD-NOTRUN :5625, STR-GANL-ARTIFACT :5694–5696.
- **E55 L95–96** The new defaults (0.25, 0.01) moved one expectation and one input — CONFIRMED. schema.py:1595–1616 sets them; in base→final, F14's expectation and A's hot read are the only changes tied to them.
- **E56 L97–98** F14 — CONFIRMED. The base expected `==2` with bound 0; final expects 0 out of 480 (:4158–4159); F14's shift lines are unchanged.
- **E57 L99** The hot read 0.1 apart is above TAU and below C — CONFIRMED (rel = 0.1/1.16 ≈ 0.086).
- **E58–E63 L101–111** The review: frozen sha and 227/227; severities; 14 predicted survivors; dispositions; 45 run on b605b91f…4c2c; V11; 13 killed by added or extended checks — CONFIRMED (report; dispositions.md; outputs).
- **E64 L112–113** Committed bytes differ in the REPO line plus five texts — CONFIRMED (six hunks d2→final).
- **E65 L116** Windows granted; bytes named first — NOT CHECKABLE.
- **E66 L117–118** nice, -I, temp folders, cd by glob — NOT CHECKABLE. It is consistent: C10.out's only temp path is under SCRATCH/tmp, and commit_steps.sh's record step has the same form.
- **E67 L119–120** One run each: 227/227 and 230/230 — CONFIRMED (one output each).
- **E68 L120–122** Window closed and reopened; three per call; manifest checked — NOT CHECKABLE. The manifest does match the 45 files.
- **E69 L123** The run of record: 1 — NOT CHECKABLE, pending.
- **E70 L125–126** Q-F3 ran beside them; no other window was open — NOT CHECKABLE.
- **E71 L127–128** "None read data/…" — NOT CHECKABLE.
- **E72 L129–133** The Perl transcript reads — NOT CHECKABLE. msgs.pl and cmds.pl do what the line says (see O4a).
- **E73 L134–135** The session-tool listings — NOT CHECKABLE.
- **E74a L137** "As at bfc869f" — CONFIRMED (v5 review raw :60; v5 values-check raw :26).
- **E74b L136–137** The reports taken from transcripts — NOT CHECKABLE; the second report is pending.
- **E75 L138–140** Perl, shell and awk tools — NOT CHECKABLE. apply_all.pl, splice.pl, fillbrief.pl and assemble.sh exist and do these jobs (see O4b and O4c).
- **E76 L141–143** Committed by path; the three grounds — CONFIRMED, pending the commit (see O6).
- **E77 L143–144** Commit-time count 0 (§5.2) — NOT CHECKABLE, pending the commit.
  - The citation is right. None of the nine texts contains the home-folder prefix, the user name or the temp root.
  - commit_steps.sh's record step replaces the repository root with `<repo>` in the self-test raw, as the v5 self-test raw does. d2.out's INVOCATION line carries the absolute interpreter path, so that step is what makes the 0 hold.
- **E78 L144** Not pushed — NOT CHECKABLE, pending.
- **E79 L144–145** "Next" — CONFIRMED (docstring final:25; bfc869f's Next).

## 2a. close_bfc869f.filled.md

- **B1 L1–2** Date; grounds §6 and §8 item 5 — CONFIRMED.
- **B2 L2–4** Path, sha, 3b2b855; §6 amends this entry's PIN-n-37 — CONFIRMED (RESULTS.md:1259 and :1312).
- **B3 L4–5** Routing raw at 7a54eb9, item 5 — CONFIRMED.
- **B4 L7** Carries item 5; the sha — CONFIRMED, pending the commit.
- **B5 L8–11** The rule restated — CONFIRMED. It uses §6's own words, "on every read of that session" (see O2).
- **B6 L12** The narrower form struck; the binding stands — CONFIRMED.
- **B7 L14–15** The three readings, named — CONFIRMED (entry L65–74).

## 2b. close_addendum_n2.filled.md

- **A1–A5** All CONFIRMED: the grounds (the header names the n-analyzer session; §6.3 (4)); bound as ADDENDUM-n1 in the same four places; §2.1 on 003ae7d (PIN-n-39); §3's drops and trigger (PIN-n-38); both readings flagged in the entry (L79–83).

## 2c. close_6e3474d.filled.md

- **C1 L1–2** Header and §10 item 4 — CONFIRMED.
- **C2 L2–4** Path, sha, c7d0009, §5 — CONFIRMED.
- **C3 L5–6** The names the sessions settled; p0 as (k + 1, n + 2) — CONFIRMED (§5; v2f's entry :1068–1070 "Names agreed so far").
- **C4 L7–8** alpha added; the convention of record — CONFIRMED (§5).
- **C5 L9–10** "As the sessions had it" — **IMPRECISE (minor).** The seat's words are "as Code reads it". The files record the place as n-build's "Code's reading, for the seat" (v2f's entry :1070). n-analyzer's agreement on it before the ruling is in messages, not files.
- **C6–C8 L12–16** The first three are read; neither alpha nor label_convention is; batch alpha beside p0 ("that commit's note": RESULTS.md:211; schema.py:1459); reports go through check_report — CONFIRMED.

## 3. review.md

**Head**

- **R1–R6** Title; entry name; base bfc869f/3d22da1d (the review diff's body equals `diff -u` base→d1); the citations of the third sitting, ADDENDUM-n2 and the pin — CONFIRMED.
- **R7a** "Drafted in one step; window" — NOT CHECKABLE. **R7b** 227/227 — CONFIRMED.
- **R8** Frozen sha; 230 ids — CONFIRMED ("read-only" is not checkable).
- **R9** A subagent of this session — NOT CHECKABLE.
- **R10** The brief's sha; items 1–5 (byte-identical to the list of record's lines 18–22); C.2 and §6.2; the standing lines; no interpreter — CONFIRMED (review/BRIEF.md).
- **R11** The specification list — CONFIRMED.
- **R12** The reviewer's commands — CONFIRMED. The summary leaves out its `head` pipes and its 003ae7d: variant, both of which the report lists.
- **R13–R18** Findings and severities; the 14 named survivors; the dispositions; the three new checks; the mutant set and result; §5; the tallies — CONFIRMED.
- **R19** The Python runs' terms — NOT CHECKABLE.
- **R20** Exact replacement, asserted once and changed — CONFIRMED. apply_all.pl dies unless the count is 1 and the file changed. For all 45, the change in `diff d2 mutant` equals `diff <id>.old <id>.new`.
- **R21** Hashes named to the coordinating session — NOT CHECKABLE.
- **R22a** Per-file manifest checks — NOT CHECKABLE (the manifest re-hash matches). **R22b** "Killed" means a non-zero exit — CONFIRMED (a group's exception is a failed check).

**§1**

- **R23** Reproduced whole, sha acdc099d…55cd — CONFIRMED (lines 69–447 are byte-identical to review/reviewer/report.md).
- **R24** "By script from the transcript" — NOT CHECKABLE.
- **R25** "Names … by description, as its brief asked" — CONFIRMED. The report has 0 matches for SCRATCH, REPO or a literal path, and review/BRIEF.md:98–99 asks for description. Pass 1's FAIL 3 is fixed.

**§2** (lines 449–518 are byte-identical to review/dispositions.md)

- **R26–R30** F1–F4 — CONFIRMED (d1→d2 diff; V05 kills A).
- **R31a** F5 (a) and **R31c** F5 (c) — CONFIRMED.
- **R31b** F5 (b): "'on that read alone' is now … 'on that read, not a range' in the docstring" — **IMPRECISE (minor).** The frozen copy's paused_points docstring (d1:5816) read "on that alone", not "on that read alone"; the reviewer's quote was loose (O8).
- **R32** F6 — CONFIRMED (PIN-n-20 and PIN-n-36 unchanged; n2_outcome's docstring updated).
- **R33–R41** B1–B9 — CONFIRMED: ct1/ct2; 2 of 4 and 3 of 4; cs3; cr; the 22 keys and the 159 reads; point_causes; C = 0.30 with 0.27; the rename, D's samples, the sixteenth case.
- **R42** Own additions absent from the frozen copy; `ceiling-unpaused` is F3's — CONFIRMED (0 in d1, present in d2). "While the review ran" is not checkable.
- **R43** The mutant set — CONFIRMED. mutants_c.spec holds C01–C26, 17 are dropped, 9 plus C27 are run, and mutants_v.spec holds 35: 45 in all. "Written before the review" is not checkable.

**§3**

- **R44** The base sha; 230/230; 233 ids — CONFIRMED.
- **R45a** The manifest: 45 files and its sha — CONFIRMED. **R45b** Checked by the coordinating session — NOT CHECKABLE.
- **R46** Three per call, fifteen calls, one window — NOT CHECKABLE.
- **R47** Outputs in scratch; the table built from them — CONFIRMED (45 outputs).
- **R48–R49** The table — CONFIRMED.
  - It equals raw/kill_table.md.
  - Its result column equals kills.txt.
  - Its function, what-breaks and predicted columns equal the specs (V30's pipe is escaped; V35 keeps the reviewer's header).
- **R50** V11's reasoning — CONFIRMED (PAUSE_KINDS' order; a non-finite read has a null absdiff; a rendering read is not launched).
- **R51** The 13 others, each by its check — CONFIRMED by the failing checks in the outputs:
  - V08: the sixteenth case.
  - V13 and V14: VD-BATCH-CLEARS.
  - V19: RD-CEILING.
  - V22: VD-PISTOP-STANDING.
  - V23: 'the points'.
  - V24: both.
  - V25: 'more than half'.
  - V26 and V28: -TRIGGER and -PAUSE.
  - V29: -PAUSE.
  - V32: VD-SECOND-ROW.
  - V35: ['D'].
- **R52** C10's FileNotFoundError and C24's KeyError 'addendum2_sha256' — CONFIRMED.
- **R53–R54** The V35 block equals mutants_v35r.spec, and the block at lines 619–658 equals mutants_c_run.spec — CONFIRMED.

**§4**

- **R55** The rows for d1, d2 and the mutants — CONFIRMED (exits inferred from the return rule).
- **R56** The run-of-record row — CONFIRMED, pending the run.
- **R57** The window sentences — NOT CHECKABLE.

**§5**

- **R58** Six regions, as diff counts them — CONFIRMED.
- **R59** The five items — CONFIRMED.
  - Three of them are rewraps whose words are identical.
  - PIN-n-38 changed in one phrase.
  - The CEILING_KEY comment gained the fourth sitting's path.
- **R60** No mutant's change lies in a differing region — CONFIRMED. The mutant hunks fall between d2:72 and d2:6176, none within 21–23, 62, 2537–2544, 2836–2837, 4879–4882 or 5690–5692.
- **R61** The REPO line computes the drafts' root — CONFIRMED (`pwd -P` of the repository equals the drafts' absolute path; neither scripts/ nor the file is a symlink).
- **R62** CODE_FORMS_SHA256 is the base's — CONFIRMED.

**§6**

- **R63** 41d0d654…b1da in base, d1, d2 and final; 2,561 — CONFIRMED.

## 4. final/n_analyze.py: the texts and the edits after mutation testing

All 52 are CONFIRMED:

- **A1** The module docstring's PINS paragraph (16–25).
- **A2** The comment above PINS (2393–2399).
- **A3** The reader section's header comment (2756–2758).
- **A4–A5** ADDENDUM2_REL and its comment, ADDENDUM2_SHA256 (70–71).
- **A6** SCHEMA_SHA256 "# 003ae7d", and the schema_module docstring.
- **A7–A8** CEILING_KEY and MEDIAN_KEY with their comment, and CEILING_COUNTER (2836–2840).
- **A9** PIN-n-37: quotes verbatim, PIN-n-24's included.
- **A10** PIN-n-38: quotes verbatim; the steered qualifier matches row_drops.
- **A11** PIN-n-39: quotes verbatim apart from the addendum's bold.
- **A12–A33** The docstrings and comments of State.unusable and State.at, `_causes`, `n2_outcome`, `build_state`, `counters`, `tau4_drop` (unchanged), `median_drop`, `row_drops`, `over_half`, `above_ceiling`, `ceiling_of`, `median_of`, `secondaries` (n §4 (f) is the TAU/4 row; A-n2 §3 amends it), `report_counters`, `report_problems`, `paused_points`, `run_verdicts` (with :6173's comment), `_bt_files`, `_bt_report_for`, `_bt_write_campaign`, `_bt_sec_shift` and `_BT_SEC_MEDIAN`. The rel values, worked by hand:
  - N1-V +1: 0.0068–0.0073.
  - N1-P −1: about 0.013.
  - rand_03: about 0.0034.
  - Shadow 2: about 8.9e-6.
- **A34–A50** The check descriptions and comments. Each matches its condition, and d2 passes all of them:
  - RD-PAUSE-POINTS: 16 cases counted.
  - RD-CEILING.
  - RD-SECOND-ROW: 22 points; the counts 81, 160, 82, 25 and 24; 78 sessions.
  - RD-SENSITIVITY/F14.
  - VD-PAUSE-POINTS A–D: A's scope is N1-P, N4-T, N4-Ts; D's is N2-S, N4-T, N4-Ts; B covers 20 points.
  - VD-SECOND-ROW, VD-CEILING, VD-SECOND-ROW-TRIGGER, VD-SECOND-ROW-PAUSE and VD-BATCH-CLEARS.
  - VD-REFUSE and its two ceiling comments.
  - VD-SENSITIVITY: 40 of 160, 20 of 960.
  - VD-PISTOP-STANDING.
  - CMD-NOTRUN, STR-GANL-ARTIFACT and STR-ADDENDUM2-SHA.
  - A's hot-read comment.
- **A51** The edits after mutation testing (d2→final) are exactly the six regions of review §5, each as described.
- **A52** ganl_artifact's "spec" string (not on the list, but changed) — correct.

## 5. vc_head.md and pass1_dispositions.md

**vc_head**

- **V1–V2** The title and the entry's name — CONFIRMED.
- **V3 L6** "Two … checkers checked six texts" — **IMPRECISE.** This pass also checks the values-check raw's first part: this head and Code's pass-1 dispositions (BRIEF2 item 5).
- **V4a** Each checker was a subagent of this session — NOT CHECKABLE. **V4b** Neither brief allowed an interpreter — CONFIRMED.
- **V5** The briefs quoted items 1–5 (byte-identical to the list of record's lines 18–22), C.2 and §6.2, and the standing lines — CONFIRMED (vc/BRIEF.md and BRIEF2.md).
- **V6** The two passes' scopes — CONFIRMED (BRIEF2's "What this pass adds"; pass 1's input hashes differ from today's).
- **V7** "With no FAIL, the second pass is the last" — CONFIRMED (this pass returns 0 FAIL).
- **V8** Five analyzer texts, all after mutation testing — CONFIRMED.
- **V9** The run of record is on the final bytes — pending.
- **V10** Each report carries its departures — CONFIRMED.
- **V11** "The entry names them for the seat to class" — NOT CHECKABLE, pending @@VC_LINE@@ (O5).
- **V12** The reports are taken from transcripts by script — NOT CHECKABLE.
- **V13 L35** "The checkers name Code's scratch folder and the repository by description" — **IMPRECISE.** Pass 1 writes the brief's label "SCRATCH" five times (e.g. "SCRATCH/base-bfc869f.py", "SCRATCH/vc/checker/"). It never writes a literal path, and this report also uses the brief's labels.

**pass1_dispositions**

- **D1** 217 claims = 187/9/3/18, with six observations — CONFIRMED.
- **D2** Everything applied — CONFIRMED (§6 below).
- **D3–D8, D10–D20** Each disposition carried and true — CONFIRMED.
- **D9** C3's third part, "as the sessions had it" — **IMPRECISE.** This is the same point as C5, appearing in two texts.
- **D21a** The checker's departures — CONFIRMED for: two awk filters; diff -u headers; the zsh `=` error and the refused loop; nothing under data/.
- **D21b** "Git digests and blob shows, in the brief's tracked-and-clean form" — **IMPRECISE (minor).** The blob shows (`git show <rev>:schema.py`) were the brief's git-history form, which pass 1 lists separately.

## 6. Pass 1's FAILs, IMPRECISE items and observations

| Pass 1 item | Carried | True |
|---|---|---|
| FAIL 1 | close_bfc869f L14–15 | yes |
| FAIL 2 | final:2836–2838 | yes (absent from d2; listed in review §5) |
| FAIL 3 | review.md L66–67 | yes |
| E27 | entry L37–38 | yes |
| E32 | entry L44–47 | yes |
| E56 | entry L95–99 | yes |
| C3 | close_6e3474d bullets | parts 1–2 yes; part 3 loosely attributed (C5) |
| C6 | close_6e3474d L9 | yes (schema.py:1122) |
| R44 | review.md L506–507 | yes (d1→d2 drops the N2-C sample) |
| R45 | review.md L509–511 | yes |
| R69 | review.md L688–689 | yes |
| PIN-n-38 | final:2536 | yes; not carried into the entry's summary (E50) |
| Obs 1 | — | yes |
| Obs 2 | `nonfinite` in entry L13, close L9, review L584 | yes |
| Obs 3 | with FAIL 2 | yes |
| Obs 4 | entry L127–140 | yes, as far as checkable (O4) |
| Obs 5 | entry L94 | yes |
| Obs 6 | — | yes (rewraps are word-identical) |

## Counts

| Text | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|
| Entry (80) | 66 | 1 | 0 | 13 |
| close_bfc869f (7) | 7 | 0 | 0 | 0 |
| close_addendum_n2 (5) | 5 | 0 | 0 | 0 |
| close_6e3474d (8) | 7 | 1 | 0 | 0 |
| Review raw (68) | 58 | 1 | 0 | 9 |
| Analyzer (52) | 52 | 0 | 0 | 0 |
| vc_head (14) | 9 | 2 | 0 | 3 |
| pass1_dispositions (22) | 20 | 2 | 0 | 0 |
| **Total (256)** | **224** | **7** | **0** | **25** |

## Observations

- **O1. The entry and the analyzer disagree on PIN-n-38.** The entry's PIN-n-38 summary (L80) still has pass 1's PIN-n-38 imprecision, which was fixed only in the analyzer (E50).
- **O2. The shadow extension is worded three ways, all consistent with the code (planned, steered).**
  - close_bfc869f uses §6's "every read of that session".
  - The entry has "every planned steered read…, each read against it".
  - PIN-n-37 and the docstring have "every planned read…, each read against it".
  - A reader comparing them could take the close line to include N4's reads.
- **O3. PIN-n-38's new "and an arm whose slope it leaves with no common session" holds only for N1-V and N1-R.**
  - It carries the accepted PIN-n-36's wording, and build_state's docstring says the same.
  - In the code, which is unchanged from the base, only N1-V's slope and N1-R's direction slopes mark their arm.
  - The N2 arms' slopes are descriptive: they set `fig["slopes_N2"][arm] = None` and mark nothing, in either row.
  - No outcome turns on this.
- **O4. Possible gaps in the departure lines:**
  - (a) msgs.pl prints each message's transcript timestamp beside it. The output went to Code's own session.
  - (b) fillbrief.pl's fixed line indices (18–22, 46, 49) match the committed list-of-record, C.2 and fourth-sitting raws. If it read them in place, "over its scratch files and RESULTS.md" leaves out three raws.
  - (c) At the commit, commit_steps.sh's place step runs commit/place.pl, which is Perl over RESULTS.md, and the bullet does not name it.
  - (d) pass1_dispositions does not name pass 1's read-only tools beyond its brief: cut, tr, rev, sed, head, tail, wc, printf, echo and process substitution. bfc869f's entry named that class.
- **O5. vc_head's "the entry names them" depends on @@VC_LINE@@.** As drafted, the entry's departures bullet is Code's alone; at bfc869f, the values-check bullet carried the checkers' departures.
- **O6. Entry L141–143's parentheticals mix subject and ground.** "(the third sitting's §6)" names what the line carries, while that close line's own header cites §6 and §8 item 5. The other two parentheticals name the ground.
- **O7. In the assembled values-check raw, the heading levels nest Code's dispositions under pass 1's report.** pass1.md's "#" and "##" headings follow "## Pass 1…", so Code's "### Pass 1's dispositions" falls under pass 1's last section. A reader of the outline could take the dispositions for part of the checker's report.
- **O8. The reviewer's F5(b) misquotes the frozen copy.** It quotes d1:5816 as "on that read alone"; the line reads "on that alone". This is in the source (§1 is unedited), and the disposition repeats it (R31b).

## Commands beyond reading files and the brief's git forms

- **Read-only shell tools beyond the brief's list:**
  - `shasum`, a name-only `ls` (scratch folders only), `wc -l`, and `diff` or `diff -u` with process substitution.
  - `sed -n`, and `sed -e` / `sed -n s///p` to mask paths and to normalize table and tally lines; `cut`, `tr`, `sort`, `head`, `tail`, `cat`, `printf`, `echo`, `basename`.
  - `[ ]` and `[ -L ]`, and `pwd -P` inside the repository (compared in the shell; it printed only "equals").
  - zsh loops over literal lists.
- **grep.** `/usr/bin/grep` only inside named single files, never recursive. One run failed on an empty alternative and I reran it.
- **Writes.** I wrote files only under SCRATCH/vc/checker/p2/: diffs, normalized lists, extracts and a re-hash.
- **Git.**
  - `git log --format` and `git show --name-status` ran with item 3's pathspec plus `':!data/mf3/**'`.
  - Without the pathspec (the brief's forms, which take none): `git rev-parse <rev>:<path>` against `git hash-object --` at HEAD:, 003ae7d: and bfc869f:, and on the scratch base copy; `git rev-parse HEAD`; and `git show <rev>:valence_core/n/schema.py | shasum` at d791bd9, 003ae7d and bfc869f.
- **Departure: two loops over a glob I had not read first.** The loops over SCRATCH/review/mutants_all/*.py and SCRATCH/review/out/*.out printed their expansions only in the same call. Both were read-only (diff, tail).
- **Committed raws read by path beyond the brief's sources.** Each was first checked tracked and clean, then searched with grep; results/raw was not listed:
  - the 2026-11-16 n-ganl answers;
  - the list of record v2;
  - the 2026-11-16 p-verdicts-counters raw;
  - the v5 review, values-check and self-test raws;
  - the schema follow-up's self-test raw.
- **Printed to my own session only, written nowhere.** Two scratch files' modification times, from the review diff's header. A few grep filename prefixes carrying the scratch folder's full name.
- **Not done.** Nothing under data/ was read, listed, stat'ed or searched. I ran no `git status`, no interpreter (I read the Perl scripts' text only) and no model process.


## Pass 2: Code's dispositions

Pass 2 checked 256 claims: 224 CONFIRMED, 7 IMPRECISE, 0 FAIL and 25 NOT CHECKABLE, with eight observations. It found
every one of pass 1's dispositions carried, each true except where its items and observations say otherwise.

With no FAIL, it is the last pass, as at v3, v4 and v5. Its seven IMPRECISE items and its observations are applied.
Its items D9 and D21b, and observation O4 (d), correct pass 1's dispositions. Those dispositions stand above as
written, and the correction is here. Each edit after this pass is checked by tool, not by a third pass.

#### The IMPRECISE

- **E50 (with O1), the entry's PIN-n-38.** The entry's summary now carries the analyzer's "or, a steered read, its
  session's shadow's".
- **C5 (with D9), "as the sessions had it".** The close line on 6e3474d now quotes §5: "as Code reads it". The files
  record the place as n-build's reading for the seat; this session's agreement with it is in messages, not files.
- **R31b (with O8), F5 (b)'s quote.** The review raw's §2 now quotes both texts as they stood: PIN-n-37's "on that
  read alone" and the docstring's "on that alone", which the reviewer quotes both as the first.
- **V3, the texts checked.** The head now says the second pass also checked this raw's first part.
- **V13, the labels.** The head now says the checkers write their briefs' labels, SCRATCH and REPO, and no literal
  path. (The reviewer's report, in the review raw, names them by description: pass 1's FAIL 3 is right there.)
- **D9.** As C5: pass 1's disposition of C3 ("as the sessions had it") is corrected here, by the close line's quote.
- **D21b.** Pass 1's departures, as its report states them: its git digests in the brief's tracked-and-clean form,
  and its blob shows (`git show <rev>:<path>`) in the brief's git-history form, both without item 3's pathspec.

#### Observations

1. **O1:** applied with E50.
2. **O2, the shadow extension's wording.** The close line on bfc869f, the entry, PIN-n-37 and `paused_points`'
   docstring (the last two analyzer texts) now agree on "every planned steered read of that session".
3. **O3, the arms a slope marks emptied.** PIN-n-38 now names them: N1-V's, or an N1-R direction's; N2's slopes are
   descriptive and mark nothing (an analyzer text). No outcome turns on it.
4. **O4, the departure lines.** The entry's departures bullet now says:
   - (a) that the transcript reads printed the messages' transcript times, to this session alone;
   - (b) that the briefs' fill read three committed raws in place (the list of record's, C.2's and the fourth
     sitting's);
   - (c) that the commit's placement of the entry and the close lines in RESULTS.md runs Perl.

   (d) Pass 1's read-only tools beyond its brief, which pass 1's dispositions did not name, are named here: `cut`, `tr`,
   `rev`, `sed`, `head`, `tail`, `wc`, `printf`, `echo` and process substitution.
5. **O5, "the entry names them".** The entry's values-check line now names both checkers' departures for the seat to
   class.
6. **O6, the close lines' grounds.** The entry's parentheticals now name each close line's grounds: §6 and §8 item 5;
   the addendum's header; the fourth sitting's header and §10 item 4.
7. **O7, the headings.** Code's dispositions now take the reports' level ("## Pass 1: Code's dispositions"), so an
   outline does not file them under a report's last section.
8. **O8:** applied with R31b.

#### Checked by tool after this pass

- **Hashes.** The final file's sha256 is in the entry in full and in the close lines abbreviated (by `cut`), filled by
  script.
- **The regions.** The final file differs from the mutant base in nine change regions (`diff`): the repository line
  and the seven texts, PIN-n-37's in two. Its CODE_FORMS_SHA256 line equals the mutant base's.
- **PIN-n-37's rewrap.** Its joined text equals the edited text, word for word, by `cmp` on the strings' contents.
- **No placeholder** is left in the entry, the close lines or the raws (the assembly script refuses one).
- **Widths.** No new line in the analyzer exceeds 120 characters.

#### The checker's departures (for the seat to class)

The checker disclosed them in its report. None read anything under `data/`, and none touched `data/mf3`:
- two loops over a glob it had not read first, each printing its expansion only in the same call (read-only: `diff`,
  `tail`);
- git digests and blob shows in the brief's forms, without item 3's pathspec;
- committed raws read by path beyond its brief's sources, each checked tracked and clean first;
- two scratch files' modification times, from a diff's header, printed to its own session only, and grep filename
  prefixes carrying the scratch folder's name;
- read-only shell tools beyond the brief's list, among them `pwd -P` inside the repository.
