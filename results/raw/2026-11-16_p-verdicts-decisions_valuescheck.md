# Blind values-checks: p's VERDICTS ×3, the joint STOP block and its entry (two passes, with Code's dispositions)

*The instruct VERDICTS session (Code), PI date 2026-11-16. Two blind passes, each by a fresh subagent briefed with the
drafts, the sources, the list of record v2's items 1–5 verbatim and the campaign lines of this session's task verbatim,
and told to run no Python and to write nothing but its raw. Pass 1 checked the two-question draft (block sha256
`e17b78c1326ba13a8fac2b4b98e1b035624d9a8ed92870c5d5496724ccaa2775`, entry
`fbbe20ea3ab6be1348b3bdbf18f8716416964a77e6d49e841ac58e994b03ff67`). Pass 2 checked the four-question draft (block
`d2cdb3036e48d471c5e5b7d39cf30a69b5efa6b1b47fe420588a9cbd49b9bbfc`, entry
`1bd532caaa0e8c8957c227a7eba7906bf5e5d0c178db7c2a1fba6e511691cffb`). The committed block is
`results/raw/2026-11-16_p-verdicts-decisions_code-to-design.md`, sha256
`caf6a8387d5a9c73284dcd2d8515c9d3883cf03d6ef8bbd09068f1703da0d8bc`. Each checker's raw follows verbatim, with only
the local paths in its header replaced: the scratch directory by `<scratch>` and the repository's root by `<repo>`.
Calendar dates only; the commit hash is the record.*

## 0. Code's dispositions

**Pass 1** (109 claims: 97 CONFIRMED, 3 IMPRECISE, 1 FAIL, 8 NOT CHECKABLE):
- FAIL 14, the dpo not-run record's hash tail: corrected to `4ed8576b…fde8`.
- IMPRECISE 33 (`other_state` for Q-F3), 40 (both outputs move aside, the move in an entry) and 74 (m's `run_verdicts`
  reads PROPOSAL-m only; PROPOSAL-p, the code of record and the lock's names are read on p's side): applied.
- O1 (MAJOR): Q2 is now framed on the VERDICTS' existence, marked as Code's reading of m:318. The readings turn on
  whether a run, or its window, is a decision. Two order-free procedures are named: inputs fixed before the first run,
  and no state read or carried in end notices.
- O2 (MAJOR): PIN-35's reading and m's precedent are set beside Q1 (a) as the case against it. The instruct session's
  Q1 reading moved from (a) to (c), and Q1's options became (a)–(d).
- O3–O10 (MINOR): applied. The header lists every source by sha256, the 2026-11-15 answers are named by path, the
  header gives the PI date, "§2's two items" is used throughout, Q6's first member is said to be carried as
  `other_state`, the (p-1) item quotes ADDENDUM-p1 §1, and the end notices are covered by procedure (ii).
- O11 (HEAD moved): noted; the drafts cite RESULTS.md by commit, not by line.

**Pass 2** (141 claims: 123 CONFIRMED, 12 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE):
- IMPRECISE 20, 35, 57, 69, 75, 92, 98, 101, 102, 106, 117 and 135: each applied in the checker's terms (a hash tail;
  PIN-35 at `:657–665`; Q1's frame; two lower-case quotes; (d)'s items not drafted; the report commands "with the same
  part withheld"; the `task_correct` raw's licence string; Q-F0's extractions as Code's precedent; the brief's bold
  markers; the lock sha256 as the precheck's).
- M1 (MAJOR): Q1 is now "the decisions Q6's list does not name". The block states that the G-CAL-p go and m's
  go-carrying records predate Q6, and that Q6 names no go.
- M2 (MAJOR): Q3 now quotes the seat's `task_correct` ruling in full ("Tabulated by Code's own step from the records at
  each entry") and A-m2 v0.3 §3.4's form, and says (c) would depart from the ruling for `task_correct`. Readings are
  given on Q3 ((a), Code's own step) and on Q4 ((b), the per-unit rule), which also answers m10.
- M3 (MAJOR): Q-F0's extractions are named Code's precedent, not m's requirement ("an addition to block §4's list that
  carries no figure of record"; m:358 names no extraction).
- m1–m17 (MINOR): applied.
  - m3: the campaigns' earlier goes (2026-11-13 items 5–6; 2026-11-14 (evening) B4) join (iv) and the (c) item.
  - m5: a tool inside p's package would make the remaining runs refuse.
  - m12: the JSON is drafted for OLMo-instruct; ADDENDUM-p1's own `{ckpt}` is marked as its text.
  - m13: (16)'s and the adoption's dates are stated beside p:102 and `ADDENDUM_M1_DATE`.
  - m14: the entry's heading no longer reads "`PROPOSAL-p OLMo-{…} — VERDICTS`".
  - m16: the list's "open today" clause is quoted.
  - m17: p §8's registered steps are set beside Q1's decisions.

**After pass 2:**
- The sft session's Q1 reading, (c), was added with its point that the precedent does not separate (c) from (d).
- The dpo session's Q2 reading is quoted from its message.
- Every quote added after pass 2 was checked by tool against its source, and two bold markers were set right.
- There was no third blind pass.
- Pass 2's disclosure of a whole-index `git ls-files` is carried to the entry, for the seat.
- Pass 1 wrote eleven temporary extracts into the scratch directory, outside the repository, and deleted them before
  writing its raw. That departs from its brief's "write only your raw" and is disclosed in its raw.

---

## 1. Pass 1, verbatim

# Blind values-check: the p VERDICTS decisions block and its entry (drafts), 2026-11-16

*Checked: the block draft `<scratch>/block_draft.md` (sha256 `e17b78c1326ba13a8fac2b4b98e1b035624d9a8ed92870c5d5496724ccaa2775`; to be committed as `results/raw/2026-11-16_p-verdicts-decisions_code-to-design.md`) and the entry draft `<scratch>/entry_draft.md` (sha256 `fbbe20ea3ab6be1348b3bdbf18f8716416964a77e6d49e841ac58e994b03ff67`), both re-hashed at the start and at the end, unchanged; `VALUESCHECK_LINE` skipped. Repository `<repo>`, branch `main`: HEAD `e5aba51bf727686383330233d3b7a8d61bb61afb` at the start. HEAD moved during the check to `8e3bf9126bacda887726e11320247af0e06276f2` (one commit, n's G-ANL-n block: a 57-line insertion at RESULTS.md line 24 with no line removed, and two new raws). No file either draft cites changed, and every verdict below holds at both commits. RESULTS.md line anchors below are at `e5aba51`; add 57 at `8e3bf91`. Every file hashed below is clean against HEAD (`git status --porcelain` with their paths printed nothing). Rules followed: no Python of any kind; nothing in the repository edited; no git write; `git status` only with a pathspec; nothing under `data/*/ckpt` or `data/*/reports` opened, searched, hashed, stat'ed or listed by metadata (only the names of nine checkpoint files were printed, by `git show --name-status`, item 1's form); nothing under `data/mf3` touched; the list of record v2, items 1–5, and the campaign lines of the brief; calendar dates only. The two chat sources were checked against the brief's verbatim text.*

## A. The block: header (lines 3–16)

1. **The writer: the instruct VERDICTS session, for the three units, on the coordinating session's instruction.** NOT CHECKABLE. Session identity is not in the repository. The brief's chat text agrees ("one joint block for all three units, written by you"; "Coordinate with p-verdicts-sft and p-verdicts-dpo directly").
2. **Code date 2026-11-16.** CONFIRMED (the calendar date of this check).
3. **The PI's routing of 2026-11-15 (evening), "Route as given", section B, item 6.** CONFIRMED. `fa27c45`'s entry: RESULTS.md:287 (the paste block's header, "… PI date 2026-11-15 (evening)"), :289 ("Route as given"), :291–294 (section B, item 6).
4. **"Start them", relayed by the coordinating session.** CONFIRMED against the brief's chat text, verbatim.
5. **Nothing ran: no `verdicts` invocation, no Python, nothing on a model or the box.** NOT CHECKABLE (the session's own acts). Its trace in the tree, no p VERDICTS output, is CONFIRMED at 22.
6. **PROPOSAL-m v1.11 at root, `42ab36ec…6c6b`.** CONFIRMED (`shasum -a 256`: `42ab36ecc814…9fc96c6b`).
7. **PROPOSAL-p v0.2, `42f2977b…3b32`; §4.1, §8 step 7.** CONFIRMED (`42f2977b941b…7023cf3b32`; §4.1 is the paragraph p:84; §8 step 7 is p:130).
8. **ADDENDUM-p1 v0.1, `16cdbc11…cb1b`; §2.4, §4 step 3.** CONFIRMED (`16cdbc11ec2a…1faf3cb1b`; §2.4 at ADDENDUM-p1:30, §4 step 3 at :42).
9. **The seat's answers of 2026-11-08: path, `9e178349…9bab`, committed at `de729c4`; Q6.** CONFIRMED (`9e1783496c71…a4571b9bab`; `git show --name-status de729c4` shows `A results/raw/2026-11-08_p-step6_design-to-code_answers.md`, the only commit touching it; Q6 at its line 15).
10. **Code's block they answer: path, `4b053577…dad7`; Q6.** CONFIRMED (`4b0535770002…e614dad7`). The answers' header reads "Answers `results/raw/2026-11-08_p-step6_code-to-design_prebuild.md` (`c9acd66`)", and that block's Q6 is at its line 86.
11. **The dated note on the `PROPOSAL-p v0.2 — COMMITTED` entry, added at `d215d5b`** (stated in the header and again in §2). CONFIRMED. The note "Dated notes (2026-11-09; the design seat's answer of 2026-11-08 at `de729c4`, §2)" is at RESULTS.md:6548, inside the entry headed at :6440, and its bullet "p:84's decisions sentence (Q6)" follows it. `git show d215d5b -- RESULTS.md` adds both lines.
12. **LOCK-p-OLMo-{sft,dpo,instruct} v1.0: `fafb786d…2bc4`, `25c52f56…3dcf`, `f71c97c1…0e67`, committed at `038bf3e`.** CONFIRMED. Each file's line 1 reads "… v1.0" and the hashes match. `git log` on the three files gives `038bf3e` as the last commit, and it modifies all three.
13. **OLMo-sft not-run record, `a30df61c…1be7`.** CONFIRMED.
14. **OLMo-dpo not-run record, `4ed8576b…cde8`.** **FAIL.** `data/m/verdicts/OLMo-dpo_not-run-record.json` hashes to `4ed8576b5687ed338155f2282020218a0e84e87cb5d7ae7bb5b4d9bb088cfde8`, so the short form is `4ed8576b…fde8`, not `…cde8`. The OLMo-dpo NOT-RUN entry (RESULTS.md:6677) gives `4ed8576b…fde8`.
15. **OLMo-instruct not-run record, `e633b2ac…c829`.** CONFIRMED.
16. **The three records committed at `0f35954`.** CONFIRMED (`git show --name-status 0f35954` adds all three; it is the only commit touching them).
17. **`scripts/m_analyze.py`, `d347ea0c…5e48`.** CONFIRMED. It is also p_analyze.py:58's pin.
18. **`scripts/p_analyze.py`, `d3758fc4…7008`.** CONFIRMED.
19. **`valence_core/p/analysis.py`, `6809a7d2…9d63`.** CONFIRMED.
20. **The list of record v2, `6c1135f5…6cdd`.** CONFIRMED (`results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md` hashes to `6c1135f5c011…4c323e6cdd`).
21. **No checkpoint, call log or report opened; nothing under `data/mf3`.** NOT CHECKABLE (the session's own acts).

## B. The block: §0

22. **No p VERDICTS output exists** (also §3 Q2: "At this block's commit no p VERDICTS output exists"). CONFIRMED. `git ls-files data/p/verdicts` prints nothing, `ls data/p/verdicts` reports no such directory, and RESULTS.md has no `PROPOSAL-p OLMo-… — VERDICTS` entry.
23. **"No session runs `p_analyze.py verdicts` until the seat's answer is routed (the coordinating session's instruction to the three sessions)."** CONFIRMED against the brief's chat text: "No session runs `verdicts` until the seat's answer is routed"; "I'm telling them now to hold".
24. **The `--decisions` input is m:318's record (PIN-35). m's analyzer validates it and carries it verbatim into `{U}_VERDICTS.json`, which is written once.** CONFIRMED: m_analyze.py:657–665 (PIN-35: "carried verbatim into {U}_VERDICTS.json / {U}_NOT-RUN.json"), :706 (`copy.deepcopy`), :2385, and :1917–1920 (PIN-37).
25. **m's three NOT-RUNs enter each output's `p` block on their own (`analysis.decisions_beside`).** CONFIRMED: analysis.py:158 (`p_block`'s `"decisions_beside": decisions_beside()`), :169 (`augment` adds `"p"`), p_analyze.py:192 (`block=_block(unit)`).

## C. The block: §1

26. **`p_analyze.py verdicts --decisions D` passes D to m's `run_verdicts` (p_analyze.py:168–192).** CONFIRMED (:179 `decisions=Path(decisions)`; :189 and :191 `m_analyze.run_verdicts(inp, env)`).
27. **m reads it at V1 (m_analyze.py:2280–2283).** CONFIRMED (:2253 "# V1 --"; :2280 `decisions_file(...)`; :2283 `dbytes`).
28. **`decisions_file`, :710–718.** CONFIRMED.
29. **`validate_decisions`, :690–707.** CONFIRMED.
30. **The input is `{schema m-decisions-v1, unit, decisions_with_other_outcomes_known}`, and each item is `{decision, date, other_unit, other_state}`.** CONFIRMED (:157, :711, :716; :695).
31. **`OTHER_UNITS` = Q-F0, OLMo-sft, OLMo-dpo, OLMo-instruct, Q-F3 (:666).** CONFIRMED (:666 is `UNITS + ("Q-F3",)`, and `UNITS` is defined at :162).
32. **`other_unit` must not be the unit itself (:701).** CONFIRMED.
33. **"`other_state` is a known outcome: one of `Q5` (`:163`: PASS, REVERSE, DEAD, INDETERMINATE, NOT-RUN)."** **IMPRECISE.** This holds for Q-F0 and the OLMo units (:685–686). For `other_unit` Q-F3 the accepted forms are "NOT-RUN" or a map {A1, A2, A3[, A3*]} of Q-F3's words (:676–682), and a Q5 word such as PASS is refused there. Accurate form: "for a built unit, one of Q5 (:163, :685–686); for Q-F3, 'NOT-RUN' or {A1, A2, A3[, A3*]} (:676–682)". This does not affect the drafted items, which are all Q-F0 / PASS.
34. **PENDING is refused (:683–684).** CONFIRMED.
35. **The list enters the output as `decisions_with_other_outcomes_known` (:2385).** CONFIRMED. It sits in `common`, which is spread into the VERDICTS document at :2400. The secondary output, `secondaries(records, U)` at :2414, does not carry it.
36. **The file's path and sha256 enter as `inputs.decisions` (:2286).** CONFIRMED (`_file_rec`, :1974–1975, records `{path, sha256}`).
37. **The list enters no computation; A0's state, its tests and the secondaries read the records, the counts and the floors.** CONFIRMED. Within `run_verdicts` (:2236–2420), `decisions` appears only at :2280 and :2385. `unit_state`, `rates_and_tests` and `secondaries` take records, counts, guard and floors.
38. **The output is written once (PIN-37, :1917–1920).** CONFIRMED.
39. **p's staged writer refuses a p command's re-run (analysis.py:202–212).** CONFIRMED.
40. **"A list found wrong after the run means a supersession on the seat's ruling (the output moved aside with `git mv` to a dated name) and a second run."** **IMPRECISE.** One `verdicts` run writes two outputs, `{U}_VERDICTS.json` and `{U}_secondary.json` (:2416). m's write-once check (:1929–1934) runs on the seeded copies, so p refuses the re-run while either p output is in `data/p/verdicts` (analysis.py:202–212), and both have to be moved aside. PIN-37 (:1917–1920) also requires the move to be "recorded in an entry". Accurate form: "both outputs moved aside with `git mv` to dated superseded names on the seat's ruling, recorded in an entry, then a second run".
41. **Every p output carries `p.decisions_beside` (analysis.py:108–121): m's three NOT-RUNs, each named `PROPOSAL-m OLMo-{ckpt}`, with its reason and its output's sha256. It is not an input.** CONFIRMED (:119–120; read from committed blobs through `m_stages._committed`, :115; no command-line flag).
42. **The seat's Q6 put them there because m's validator refuses a unit naming itself, and p keeps m's unit strings.** CONFIRMED (Q6: "since m's validator refuses a unit naming itself and p keeps m's unit strings").

## D. The block: §2

43. **m:318's last sentence, verbatim.** CONFIRMED. The block's quote, with its `  > ` prefix stripped, was compared byte for byte with m:318 from "A decision about one unit" to the end of the line, bold markers included: identical.
44. **p:84 is p §4.1's last sentence, verbatim.** CONFIRMED. §4.1 is the single paragraph p:84 (p:85 is blank and §4.2 starts at p:86). The quote is identical once the block's wrapped line is joined.
45. **The seat's Q6 (`de729c4`, its §2), verbatim.** CONFIRMED. It is the answers' line 15, under "## 2. The analyzer path …" at line 13, and is byte-identical once `  > ` is read as `- `.
46. **ADDENDUM-p1 §2.4, verbatim.** CONFIRMED (ADDENDUM-p1:30 after "**2.4 Order.** ", identical).
47. **m's three OLMo not-run records each carry two items, each with `other_unit` Q-F0 and `other_state` PASS.** CONFIRMED (the three files, read in full).
48. **One is A-m1's decision (16), dated 2026-11-06.** CONFIRMED.
49. **The other is the PI's go for that G-CAL run, 2026-11-06 (the `PROPOSAL-m OLMo-{ckpt} — NOT-RUN` entry).** CONFIRMED. Each record's second item reads "the PI's go for G-CAL-OLMo on sft, dpo and instruct, smoke first (…)", dated 2026-11-06. The OLMo-sft NOT-RUN entry (RESULTS.md:6653–6655) reads "… ADDENDUM-m1's decision (16), dated 2026-11-06 …; and the PI's go for this G-CAL run, 2026-11-06."
50. **The first drafted item's text is byte-identical to the one in each of m's three records.** CONFIRMED. `cmp` of block lines 85–90 against each record's lines 9–14 reports identical, three times.
51. **The second item's date is that of p's disclosure (gcal.py:105, quoted).** CONFIRMED. gcal.py:105 is `DISCLOSURE = ("pre-registered on 2026-11-07 (PROPOSAL-p v0.2, `18b0111`; v0.1 routed 2026-11-06), …`, and the quoted fragment is verbatim.
52. **The second item's own references: PROPOSAL-p v0.2 committed at `18b0111`; v0.1 routed 2026-11-06; "the OLMo told controls at a frame-word corruption dose".** CONFIRMED. `18b0111` adds the file. The routing block of 2026-11-06 is quoted in the OLMo-sft NOT-RUN entry (RESULTS.md:6633–6634; item 2 "PROPOSAL-p v0.1: [route for Code's pre-read]"). The phrase is PROPOSAL-p's title (its line 1).
53. **The drafted file is in m's accepted form.** CONFIRMED by reading; nothing was run. It has three keys (:716). Each item has its four keys (:695), a non-empty decision (:697), an ISO date (:699), `other_unit` Q-F0, which is not the unit (:701), and `other_state` PASS, which is in Q5 (:685). `"unit": "OLMo-{ckpt}"` is a per-unit placeholder.
54. **Q-F3's outcome is known at no run: its campaign is running, and its VERDICTS session runs only after the `POSTING v1` entry exists (ADDENDUM-m1 (10′), as the seat's answers of 2026-11-15, §4.1, quote it).** CONFIRMED. `e5aba51`'s note says "while Q-F3's campaign runs" (RESULTS.md:25–26, :53–54). `results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md`:50 (§4.1) reads: ADDENDUM-m1 (10′): Q-F3's VERDICTS session "runs only after the `POSTING v1` entry exists". ADDENDUM-p1:20 agrees. Two seat raws carry that date (O5).

## E. The block: §3

55. **Q6 dated 2026-11-08.** CONFIRMED (the answers' header: "PI date 2026-11-08").
56. **(i) The PI's cap share, "2 h each" (PI date 2026-11-14; each lock's §2, LOCK-p-OLMo-{ckpt} v1.0 at `038bf3e`).** CONFIRMED. LOCK-p-OLMo-{sft,dpo,instruct}.md:29 reads "## §2. The hour cap (the PI's cap share; …)", and :31 reads "(PI date 2026-11-14, …): **"2 h each"**".
57. **m:318 names "an OLMo cap" among the decisions it records.** CONFIRMED.
58. **(ii) ADDENDUM-p1's decision (p-1) (PI date 2026-11-15; committed at `fa27c45`); its §2.4 has the entry record, "in m:318's form", the computation "after this re-specification".** CONFIRMED (ADDENDUM-p1:2 "PI date 2026-11-15"; `fa27c45` adds the file; :30 for both fragments).
59. **(iii) The PI's go for the replacement pod, "Go for the pod whenever you need it." (PI date 2026-11-15).** CONFIRMED. RESULTS.md:188 (`41bfab4`'s entry) has the quote with its period. RESULTS.md:1027–1028 reads "The replacement box … is pod `m43y3deb1gq3rp`, made on the PI's go …".
60. **Other decisions in the same date range: the locks' placements and the seat's rulings on p's gate stages.** CONFIRMED. `038bf3e`'s subject cites "the PI's "Route as given" + "Place the locks" (PI date 2026-11-14)". `e619d3d` (2026-11-09) is "The seat's answer on G-TIME-OLMo (p) closed". `a2c354e` (2026-11-13) commits `results/raw/2026-11-12_p-qual_design-to-code_answers.md`.
61. **The readings move only the input's bytes (the list and `inputs.decisions`), and no code, lock or hash of record moves.** CONFIRMED. The list enters only at :2286 and :2385. The decisions file is read by `_load_json` / `_read_bytes` (:2280, :2283), not through `env.committed` as the lock is (:2263), and no lock names it.
62. **m:318's words "in that unit's VERDICTS entry".** CONFIRMED (a verbatim fragment; the sentence goes on "or NOT-RUN record"; see O2).
63. **(b)'s two drafted items: their references and dates (`038bf3e`, §2, 2026-11-14; `fa27c45`, 2026-11-15).** CONFIRMED. Both are in m's accepted form, as at 53. The (p-1) text is Code's paraphrase (O9).
64. **Q6's "p's own other units' known outcomes".** CONFIRMED (verbatim).
65. **The three runs are serialized, each in a battery window from the coordinating session, one at a time, while Q-F3's campaign runs on the laptop.** CONFIRMED by the brief's campaign line, RESULTS.md:423–424 ("model-free test batteries at low priority, one at a time. This session gives each battery a window") and :69–71 (`e5aba51`'s note extends the windows "to a p VERDICTS run").
66. **m's validator accepts a sibling as `other_unit`, with its state word as `other_state`; each item still needs a decision.** CONFIRMED (:666, :701, :685; :697–698).
67. **`run_staged` copies `data/p/verdicts`' files into its staging directory before m's function runs (analysis.py:190–195).** CONFIRMED. Regular `*.json` files only; `fn(st)` is called at :197.
68. **m's refusals there test only the run's own unit's file names (`refuse_beside`, m_analyze.py:1953–1964).** CONFIRMED. For an OLMo unit, `run_verdicts` checks its out directory in only two places: `refuse_beside` (:2415, `{U}_NOT-RUN.json`) and `write_texts_once` (:2416, `{U}_VERDICTS.json` and `{U}_secondary.json`, named at :2284–2285). The second is also a refusal on the unit's own names (:1929–1934); the block does not cite it. The only out-directory read of other units' outputs is Q-F0's (:2314).
69. **A p unit's VERDICTS run is the registered step (p §8 step 7).** CONFIRMED (p:130).
70. **The order-free procedure is named, not chosen.** CONFIRMED against the brief's chat text ("computing all three before any session reads a sibling's output. Name it, don't choose it.").

## F. The block: §4

71. **"Code adjudicates nothing (CLAUDE.md; WORKFLOW.md §4)".** CONFIRMED. CLAUDE.md says "Code escalates fired gates, never self-adjudicates", and WORKFLOW.md:36, in §4, says **"Code adjudicates nothing"**.

## G. The block: §5

72. **`p_analyze.py verdicts` never reaches `m_analyze.battery()`. Only `_selftest` calls it (p_analyze.py:344), and only `--selftest` (:722) and `ganl` (:668) reach `_selftest`.** CONFIRMED. p_analyze.py's only `m_analyze.battery()` call is :344, inside `_selftest` (:300). `_selftest` is called only from `run_battery` (:651), which is called only at :668 (`run_ganl`) and :722 (`--selftest`). The `verdicts` branch (:742–745) calls `run_verdicts_p`. m_analyze.py's own `battery()` calls are at :11110 (m's ganl) and :11301 (m's `--selftest`), both outside `run_verdicts`, and nothing calls it at module level (the file ends in a `__main__` guard).
73. **It touches nothing under `data/mf3`.** CONFIRMED by reading; nothing was run. The path reads PROPOSAL-m and PROPOSAL-p, CLAUDE.md, ADDENDUM-m1, both analyzers, p's and m's packages, `olmo_hf.py` and p's driver through git, plus the lock, the decisions file, the three `data/p/ckpt` checkpoints, m's three NOT-RUN outputs and `data/p/verdicts`. Outside `valence_core/mf3`, `git grep -l mf3` over `valence_core` finds only p's `guard.py` (root constants for refusing outputs), `gshape.py` (G-SHAPE-p) and `schedule.py` (a docstring). `e5aba51`'s note agrees (RESULTS.md:63–65: "p's VERDICTS path … calls none of them").
74. **"m's `run_verdicts` reads its named inputs …, committed blobs through git, the two proposals, ADDENDUM-m1, CLAUDE.md and the analyzer. … p's side adds m's three NOT-RUN outputs, read through git, and `data/p/verdicts`."** **IMPRECISE.** m's `run_verdicts` reads one proposal, PROPOSAL-m: through the gate line (stages.py:478) and at V1 (m_analyze.py:2256). PROPOSAL-p is read on p's side, by `analysis.d_p_problems` (analysis.py:81–92, called from p_analyze.py:96 and :126). p's side also checks the code of record at HEAD (`gcal.committed_problems`, p_analyze.py:95; gcal.py:170–180) and reads the lock (p_analyze.py:156–165). Accurate form: "m's `run_verdicts` reads … PROPOSAL-m, ADDENDUM-m1, CLAUDE.md and the analyzer; p's side adds PROPOSAL-p, the code of record and the lock, m's three NOT-RUN outputs through git, and `data/p/verdicts`". None of these is under `data/mf3`, so the conclusion stands.
75. **Q-F3's reader (m_analyze.py:2249–2250) is not reached.** CONFIRMED. The branch is `U == UNIT_F3`, and p_analyze refuses any unit outside its three OLMo units (:729–731).
76. **`production_env()` with no unit adds no mf3 module to the closure (:1904–1911).** CONFIRMED. p_analyze calls it with no argument (:172). `lz` is None unless `unit == UNIT_F3` (:1906). The default lazies are `valence_core.m.stages` alone (:143, :1837). No file in `valence_core/m` mentions mf3, and m_analyze's mf3 imports are function-local in Q-F3 paths (:3532 ff., :4116).
77. **`--lock LOCK-p-OLMo-{ckpt}.md` (v1.0, `038bf3e`): each sha256, re-hashed, is the campaign's `lock_sha256` as `41bfab4`'s entry gives it (`fafb786d…`, `25c52f56…`, `f71c97c1…`).** CONFIRMED. RESULTS.md:201 gives "`lock_sha256` `fafb786d…`, `25c52f56…` and `f71c97c1…`", and :238–239 say "each identity carries its lock's sha256". The precheck raw prints `identity_extra.lock_sha256` (`results/raw/2026-11-15_p-campaign_precheck.txt`:11, :13, :15, :75), and its 16-character prefixes equal the re-hashed locks'. Each lock also names m's analyzer sha256 in full (5 lines each).
78. **`--campaign`, `--time`, `--qual` are `data/p/ckpt/OLMo-{ckpt}_{campaign,time,qual}.json`, as the entries of `41bfab4`, `2258c52` and `a225a89` name them.** CONFIRMED. Each commit adds its three files (`git show --name-status`, names only), and each entry's diff names `data/p/ckpt/OLMo-{ckpt}_campaign.json`, `…_time.json` and `…_qual.json` respectively.
79. **They are also p_analyze's defaults (p_analyze.py:180–181).** CONFIRMED. The defaults are `ck / f"{unit}_campaign.json"`, `_time.json` and `_qual.json`, with `ck` = `data/p/ckpt` by default (:61, :169, :177). `_cli_path(None)` returns None (m_analyze.py:11258–11259).
80. **No `--adjudication`, since no campaign paused (each m report's `pauses` empty, `41bfab4`'s entry), and no `--pi-stop`.** CONFIRMED. RESULTS.md:238 says "Each m report's `pauses` is empty and its `stop` null", and the entry's headline says "no pause, no STOP".
81. **The input's home is `data/p/verdicts/OLMo-{ckpt}_decisions.json`, in Q-F0's input style; the `PROPOSAL-m OLMo-{ckpt} — NOT-RUN` entry gives the reason.** CONFIRMED (RESULTS.md:6656–6657: "The file name is Code's, in Q-F0's input style (`{U}_decisions.json`, …), inside the repo so the output records its path relative to the root.").
82. **`.gitignore`'s `!/data/p/verdicts/*.json` admits it.** CONFIRMED (.gitignore:313; `git check-ignore -v --no-index data/p/verdicts/OLMo-sft_decisions.json` names that negation).
83. **It is committed with the outputs, as Q-F0's was (`bfc179c`).** CONFIRMED. `bfc179c` adds `data/m/verdicts/Q-F0_decisions.json` beside Q-F0's VERDICTS, secondary and olmo-states files.
84. **ADDENDUM-p1 §2.4's sentence goes in each VERDICTS entry under every reading.** CONFIRMED (ADDENDUM-p1:42, §4 step 3: "each entry carrying §2.4's sentence").
85. **The runs: one invocation per unit, at `nice -n 19`, each in a battery window the coordinating session grants.** CONFIRMED as consistent with the record. RESULTS.md:423 reads "model-free test batteries at low priority, one at a time"; `nice -n 19` is the practice for model-free runs (e.g. `5a97527`'s entry, RESULTS.md:158); the windows are as at 65.
86. **"(each session's step 1; the instruct session's read of the code)".** NOT CHECKABLE (the sessions' own steps).

## H. The entry

87. **Dated 2026-11-16.** CONFIRMED.
88. **Headline: VERDICTS held before any run; the `--decisions` input is m:318's list (PIN-35); STOP for the seat's read; Code's block at this commit.** CONFIRMED. It is consistent with the block and with m_analyze.py:657 (PIN-35), and WORKFLOW.md §4 has the "STOP for the seat's read" form.
89. **The instruct VERDICTS session writes it, for the three units, on the coordinating session's instruction.** NOT CHECKABLE (as 1).
90. **Nothing ran: no `verdicts` invocation and no Python.** NOT CHECKABLE (as 5).
91. **No p VERDICTS output exists.** CONFIRMED (as 22).
92. **The routing, verbatim: the PI's paste block of 2026-11-15 (evening), "Route as given", section B, item 6.** CONFIRMED. Entry line 7, with its `    > ` prefix stripped, is byte-identical to RESULTS.md:294 and to the line `fa27c45` adds. The header and the word are as at 3.
93. **"Start them".** CONFIRMED (the brief, verbatim).
94. **The coordinating session's words: "So it's a STOP for the seat: one joint block for all three units, written by you, since you raised it."** CONFIRMED. It is an identical substring of the brief's text; both drafts use straight ASCII quotes throughout.
95. **No session runs `verdicts` until the answer is routed; the sft and dpo sessions hold too.** CONFIRMED (the brief: "No session runs `verdicts` until the seat's answer is routed"; "I'm telling them now to hold").
96. **What the record settles: Q6 (`de729c4`, §2; the note at `d215d5b`); two items with Q-F0 / PASS (A-m1's (16) and the adoption, 2026-11-07); the NOT-RUNs through `analysis.decisions_beside`; Q-F3 known at no run.** CONFIRMED (as 11, 25, 45, 47–52, 54).
97. **Q1's members and fragments: "2 h each" (2026-11-14) and "an OLMo cap"; (p-1) (2026-11-15) and "m:318's form"; the PI's goes, which m's not-run records list.** CONFIRMED (as 49, 56–58).
98. **Q2: the runs are serialized in battery windows, and the order-free procedure is named without being chosen.** CONFIRMED (as 65, 70).
99. **Code's readings: Q1 (a), "the input holds Q6's two items and the later decisions go in each entry's text, in m:318's form"; Q2 (a), no sibling item.** CONFIRMED in substance (block §4). Its wording differs from block §3 (a) (O7).
100. **Not questions: no `m_analyze.battery()`, nothing under `data/mf3`.** CONFIRMED (as 72–73).
101. **Each lock's sha256 is its campaign's `lock_sha256` (sft `fafb786d…`, dpo `25c52f56…`, instruct `f71c97c1…`).** CONFIRMED (as 77).
102. **The checkpoints are `data/p/ckpt/OLMo-{ckpt}_{campaign,time,qual}.json`.** CONFIRMED (as 78).
103. **No adjudication and no PI-stop.** CONFIRMED (as 80).
104. **ADDENDUM-p1 §2.4's sentence goes in every VERDICTS entry.** CONFIRMED (as 84).
105. **The block link `results/raw/2026-11-16_p-verdicts-decisions_code-to-design.md`, with Code's draft input in its §2 and §3.** CONFIRMED. The path follows WORKFLOW.md §4's form, and block §2 and §3 (b) carry the JSON. The link label follows RESULTS.md's `_topic` style.
106. **This session's reads: one `git ls-files` over `data/p`, its `ckpt` and `reports` names filtered from the output; two later name listings under `data/p/ckpt` refused by the permission classifier.** NOT CHECKABLE (the session's own acts). `git ls-files` is item 1's form.
107. **"the paths above come from the entries that committed them".** CONFIRMED (as 78).
108. **Next: the three runs, one invocation per unit in the coordinating session's windows, and the six entries, each VERDICTS entry with §2.4's sentence.** CONFIRMED. p:130 and ADDENDUM-p1:42 give a VERDICTS and a secondary-DVs entry per unit, six in all.
109. **Not pushed; committed by path.** NOT CHECKABLE (acts after this check).

**109 claims: 97 CONFIRMED, 3 IMPRECISE, 1 FAIL, 8 NOT CHECKABLE**

## Observations

- **O1 (MAJOR): Q2's order-free procedure is framed on knowledge; m:318's trigger is existence.** Block §3 says of the procedure: "No session then knows a sibling's outcome at any run, and the three lists have one form." m:318's trigger is a decision "taken after another unit's VERDICTS exist", recorded "as taken with the other unit's outcome known": what counts is that the other unit's VERDICTS exist, not that anyone has read them. Under the procedure, runs 2 and 3 still come after a sibling's VERDICTS exist. Whether their lists then gain an item turns on whether a run, or the window that starts it, is a decision about that unit. That is reading (a)'s premise ("not a decision about another unit"), not a question of who has read an output. "The three lists have one form" holds under (a) with or without the procedure, and under (b) only because (b) is defined by reading ("its session reads the earlier units' state words"). The block says neither this nor whether the three input files are fixed before the first run. The seat is asked to weigh the procedure, so a careful reader would expect it said.
- **O2 (MAJOR): the case for Code's Q1 (a) leaves out PIN-35's own reading and m's precedent.** The case rests on m:318's "in that unit's VERDICTS entry", quoted without the sentence's "or NOT-RUN record". The block does not set beside it:
  - PIN-35, m's declared reading (m_analyze.py:657–658): "m:318's record of decisions taken with another unit's outcome known is a REQUIRED declared input", carried verbatim into `{U}_VERDICTS.json`. It sits in the analyzer of record whose sha256 each LOCK-p v1.0 names, and the block's own §0 adopts it ("the `--decisions` input is m:318's record … (PIN-35)").
  - m's precedent: m put a class-(iii) decision, the PI's go, inside the analyzer's input (the not-run records' lists), not in entry text only.

  Under (a), the input that PIN-35 calls m:318's record would hold less than the entry. Both points bear directly on Q1, and §3 and §4 give reasons for (a) only; (c) cites the precedent without that argument. This is an omission, not a factual error.
- **O3 (MINOR): the FAIL at 14 is a one-character transcription.** The block has `…cde8` where the hash ends `…fde8`. The OLMo-dpo NOT-RUN entry (RESULTS.md:6677) has it right. A committed raw is not edited, so the fix belongs before the commit.
- **O4 (MINOR): the header's list of sources omits sources the body cites.** Omitted: `valence_core/p/gcal.py` (`9aa21354…6af5`, cited as gcal.py:105); the seat's answers of 2026-11-15 (`results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md`, `1f3ce1f9…f84b`, §4.1); `.gitignore`; `WORKFLOW.md` (`e7195706…b061`); `CLAUDE.md` (`955788de…8a62`); and the entries of `41bfab4`, `2258c52`, `a225a89`, `fa27c45` and m's NOT-RUN entry. WORKFLOW.md §4's header form lists "the sources read … by sha256".
- **O5 (MINOR): "the seat's answers of 2026-11-15, §4.1" is ambiguous.** Two seat raws carry that date: `…_campaign-go-p1-n-spinup_…` and `…_lock-m-f3-v1_…`. Only the first has the §4.1 the block quotes. A path or hash would settle it.
- **O6 (MINOR): the header gives "Code date 2026-11-16".** WORKFLOW.md §4's header form names "the PI date". Four of the five Code blocks dated 2026-11-11 to 2026-11-15 carry "PI date …" in their first lines; the fifth carries neither. Noted only; which date applies is not in the repository.
- **O7 (MINOR): the block and the entry name Code's Q1 (a) differently.** The entry has "the input holds Q6's two items"; block §3 (a) has "§2's two items". Q6's form names five members, of which the record settles two today, so "§2's two items" is the exact referent.
- **O8 (MINOR): the block does not say how Q6's first member is met.** Q6's "Q-F0's outcome" (p:84's "Q-F0's PASS") is carried only as the `other_state` of the two drafted items, since m's validator admits no item without a decision (:697–698). A reader of Q6 or p:84 would ask.
- **O9 (MINOR): (b)'s drafted (p-1) text is a paraphrase.** "a p checkpoint's outcome enters the posting its VERDICTS entry reaches, v1 included" drops ADDENDUM-p1 §1's "or its `— NOT-RUN` record". If (b) or (c) is ruled, the seat may want (p-1)'s own words.
- **O10 (MINOR): the procedure does not say what the end notices carry.** Under the order-free procedure the coordinating session still grants each window. For the campaigns, "each end notice to the coordinating session carried the outcome only" (`41bfab4`'s entry, RESULTS.md:217–218). For a VERDICTS run that outcome would be the unit's state, and the procedure as named does not say what the end notices carry until the third run ends.
- **O11 (MINOR): HEAD moved during this check.** It went to `8e3bf91` (n's G-ANL-n block, inserted at RESULTS.md:24). The drafts cite no RESULTS.md line, so nothing in them moves. The entry will sit above `8e3bf91`'s.

## Disclosures

- **Command forms outside item 1's list, none under `data/*/ckpt`, `data/*/reports` or `data/mf3`:**
  - content reads of committed text and code with `sed -n`, `cat`, `head -1`, `tail -4`, `awk` line ranges and the Read tool; item 2 admits them outside those directories;
  - single-file content searches with `/usr/bin/grep`;
  - one tree search, `git grep -l "mf3" -- 'valence_core' ':!data/**' ':!valence_core/mf3/**'`, in item 3's exclusion form;
  - `git show --format= <commit> -- RESULTS.md` (`d215d5b`, `fa27c45`, `2258c52`, `a225a89`, `41bfab4`) and `-- .gitignore` (`bfc179c`), piped to grep;
  - `git diff -U0 e5aba51 HEAD -- RESULTS.md` (hunk headers and a count of removed lines);
  - `git check-ignore -v --no-index` on one not-yet-existing path under `data/p/verdicts`;
  - `git rev-parse HEAD`;
  - `wc -l` on the two drafts and on four code files (scripts/p_analyze.py, scripts/m_analyze.py, valence_core/p/analysis.py, valence_core/p/gcal.py);
  - `cmp` on extracted text;
  - `git status --porcelain` with a pathspec (item 1's bare form, narrowed as the brief requires).
- **Item 1's forms used:**
  - `git show --name-status` on `de729c4`, `d215d5b`, `038bf3e`, `0f35954`, `bfc179c`, `fa27c45` and `18b0111`, and on `41bfab4`, `2258c52` and `a225a89` filtered to the nine checkpoint names (names only);
  - `git log` with ids, subjects and dates (one call formatted a commit time and printed only its date);
  - `git ls-files`, a name-only `ls data/p/verdicts`, and `shasum -a 256`.
- **Read beyond the brief's list of sources:**
  - `valence_core/p/report.py` (:220–250), `valence_core/p/guard.py` (:184–214) and `valence_core/m/stages.py` (:415–466, its import lines);
  - grep counts or import lines of `valence_core/session.py`, `valence_core/e2d/habit.py` and `valence_core/p/{register,stage,identity}.py`;
  - `WORKFLOW.md` (:1–38);
  - `results/raw/2026-11-15_p-campaign_precheck.txt` (grep), `results/raw/2026-11-15_lock-m-f3-v1_design-to-code_answers.md` (grep) and the first five lines of five Code blocks dated 2026-11-11 to 2026-11-15;
  - `CLAUDE.md` and the list-of-record raw, hashed only.
- **Scratch files, a departure from "write only your raw".** For the byte comparisons I wrote eleven temporary text extracts (`vc_*.txt`) into the scratchpad, outside the repository, and deleted them before writing this raw.
- **No departure from the binding rules.** No Python, no edit, no git write, no unscoped `git status`, no metadata of `ckpt` or `reports`, nothing under `data/mf3`. No clock time is written here.

---

## 2. Pass 2, verbatim

# Blind values-check (2nd pass): p's VERDICTS decisions block and its RESULTS.md entry (v4 drafts)

*Checked: the block `<scratch>/block_v4.md` (sha256 `d2cdb3036e48d471c5e5b7d39cf30a69b5efa6b1b47fe420588a9cbd49b9bbfc`, re-hashed at the start and the end: equal) and the entry `<scratch>/entry_v4.md` (sha256 `1bd532caaa0e8c8957c227a7eba7906bf5e5d0c178db7c2a1fba6e511691cffb`, equal at both ends), against `<repo>` on `main`. HEAD at the start: `718c48e1c335016541695446b9c8fcbda063e5d8`; HEAD at the end: `718c48e1c335016541695446b9c8fcbda063e5d8` (unchanged). The cited code and lock files were re-hashed at the end: unchanged. Rules followed: no Python of any kind; no git write; no `git status` without a pathspec; nothing under `data/*/ckpt` or `data/*/reports` opened, listed by name, hashed or stat-ed; nothing under `data/mf3` read; content searches limited to named files or to RESULTS.md; the list of record v2 items 1–5 as quoted in the brief; calendar dates only. `VALUESCHECK_LINE` skipped. Line anchors are to the working-tree files at HEAD unless a commit is named. Dates are PI-local calendar dates as the record gives them.*

## A. The block

### Header (sources)

1. CLAUDE.md `955788de…8a62` — **CONFIRMED**. `shasum -a 256 CLAUDE.md` → `955788dec22e…3de8a62`; `git status --porcelain --` over every cited path printed nothing.
2. WORKFLOW.md `e7195706…b061` — **CONFIRMED** (`e7195706efee…c6b061`).
3. `.gitignore` `2ebda7ff…d0c8` — **CONFIRMED** (`2ebda7ff85a0…bbd0c8`).
4. PROPOSAL-m v1.11 `42ab36ec…6c6b` — **CONFIRMED** (`PROPOSAL-m-gating-campaign-v1_11.md` → `42ab36ecc814…fc96c6b`).
5. PROPOSAL-p v0.2 `42f2977b…3b32` — **CONFIRMED**.
6. ADDENDUM-p1 v0.1 `16cdbc11…cb1b` — **CONFIRMED**.
7. Step-6 answers `9e178349…9bab`, committed at `de729c4` — **CONFIRMED** (`git log --diff-filter=A` → `de729c4 2026-11-08`).
8. Code's step-6 block `4b053577…dad7`, its Q6 — **CONFIRMED** (hash equal; added at `c9acd66`; its Q6 at :86).
9. G-CAL-OLMo answers `4c3f57d4…bf82` at `0f35954` — **CONFIRMED** (added at `0f35954`).
10. G-CAL-p answers `4b77e39a…48e1` at `daca8b0` — **CONFIRMED**.
11. G-TIME-OLMo (p) answers `7b8b1d5f…adc3` at `e619d3d` — **CONFIRMED**.
12. 2026-11-14 answers `6b963adf…db3a` at `cdccc66` — **CONFIRMED**.
13. 2026-11-15 (evening) answers `1f3ce1f9…f84b` at `a215c28` — **CONFIRMED**.
14. The RESULTS.md entries named (`0f35954` NOT-RUN ×3; `d215d5b` the dated note; `2258c52` G-TIME-OLMo (p) ×3; `a225a89` G-F0m-OLMo (p) ×3 and its close at `a2c354e`; `038bf3e` LOCK-p v1.0 ×3 with the close; `fa27c45` ADDENDUM-p1; `41bfab4` the campaigns; `0fa8539` Q-F0's VERDICTS) — **CONFIRMED** (each commit's subject and its RESULTS.md diff).
15. LOCK-p-OLMo-{sft,dpo,instruct} v1.0 `fafb786d…2bc4`, `25c52f56…3dcf`, `f71c97c1…0e67`, committed at `038bf3e` — **CONFIRMED** (hashes equal; `038bf3e` is the last commit touching each).
16. m's not-run records `a30df61c…1be7`, `4ed8576b…fde8`, `e633b2ac…c829`, at `0f35954` — **CONFIRMED** (hashes equal; `git show --name-status 0f35954` lists the three as A).
17. `results/raw/2026-11-11_p-qual_task-correct.txt` `57e9c7dc…56e2`, at `a225a89` — **CONFIRMED**.
18. `scripts/m_analyze.py` `d347ea0c…5e48` — **CONFIRMED**.
19. `scripts/p_analyze.py` `d3758fc4…7008` — **CONFIRMED**.
20. `scripts/p_sessions.py` `9c641e19…6a96d` — **IMPRECISE**. The file hashes to `9c641e19…361a6a96d`; the last four are `a96d`, and the draft carries five characters. Accurate form: `9c641e19…a96d` (as the campaigns' entry, `41bfab4`, writes it).
21. `valence_core/p/analysis.py` `6809a7d2…9d63` — **CONFIRMED**.
22. `valence_core/p/gcal.py` `9aa21354…6af5` — **CONFIRMED**.
23. `valence_core/p/report.py` `e807c5ad…5af1` — **CONFIRMED**.
24. `valence_core/p/stage.py` `3390a448…a406` — **CONFIRMED**.
25. The list of record v2 `6c1135f5…6cdd` — **CONFIRMED** (`results/raw/2026-11-10_list-of-record-v2_design-to-code_answers.md` → `6c1135f5c011…e6cdd`; in `fc43249`'s file list).
26. "Nothing ran in this session … no Python"; "No checkpoint, call log or report was opened" — **NOT CHECKABLE** (the drafting session's own conduct). The absence of any p VERDICTS output is consistent with it (item 27).

### §0

27. "No p VERDICTS output exists" — **CONFIRMED**. `git ls-files data/p/verdicts` prints nothing; `ls data/p/verdicts` → "No such file or directory".
28. "The three sessions agree on these" (the settled items) — **NOT CHECKABLE** for the sft session (no record of its reading is available to me). For the dpo session: agrees (note lines 10–13, 26–33).
29. Q1's four named decisions and dates (cap share 2026-11-14, "Place the locks" 2026-11-14, (p-1) 2026-11-15, the goes) — **CONFIRMED** (items 58, 60, 62–68).

### §1

30. `p_analyze.py verdicts --decisions D` passes D to m's `run_verdicts` (`scripts/p_analyze.py:168–192`) — **CONFIRMED** (`run_verdicts_p` builds `VerdictInputs(decisions=Path(decisions))` at :178–183 and calls `m_analyze.run_verdicts` at :189/:191; the CLI calls it at :742–745).
31. m reads it at V1 (`:2280–2283`), through `decisions_file` (`:710–718`) and `validate_decisions` (`:690–707`); form `{schema m-decisions-v1, unit, decisions_with_other_outcomes_known}`, items `{decision, date, other_unit, other_state}` — **CONFIRMED** (`DECISIONS_SCHEMA = "m-decisions-v1"` at :157; key check :695–696, :716).
32. `OTHER_UNITS` = Q-F0, OLMo-sft, OLMo-dpo, OLMo-instruct, Q-F3 (`:666`); not the unit itself (`:701`) — **CONFIRMED** (:162 `UNITS`, :666 `UNITS + ("Q-F3",)`, :701).
33. `Q5` (`:163`) PASS, REVERSE, DEAD, INDETERMINATE, NOT-RUN; PENDING refused (`:683–686`); Q-F3 "NOT-RUN" or `{A1, A2, A3[, A3*]}` (`:676–682`) — **CONFIRMED**.
34. "a decision names what was decided (non-empty str)" (`:697–698`) — **CONFIRMED** (:698, verbatim).
35. PIN-35 at `:655–663` — **IMPRECISE**. :655–656 are blank; the PIN-35 comment runs :657 ("# PIN (Code, declared at LOCK v0.1): PIN-35 -- m:318's record …") to :665 ("… PENDING is refused: a PENDING unit has no VERDICTS (m:318, m:324)."). Accurate anchor: `:657–665`.
36. The PIN-35 quote with its ellipsis — **CONFIRMED** (both halves verbatim at :657–661 once the comment markers are joined; the ellipsis spans ": the not-run record's key, and verdicts' --decisions file {…}; entries are {decision, date, other_unit, other_state},", so in the source the subject of "carried verbatim" is the entries).
37. The list enters the output as `decisions_with_other_outcomes_known` (`:2385`); path and sha256 as `inputs.decisions` (`:2286`) — **CONFIRMED** (`_file_rec` at :1974–1975 returns `{"path", "sha256"}`).
38. The list enters no computation — **CONFIRMED** (`decisions` is used only in `common`, :2375–2385; the state, rates/tests and secondaries are computed from `records`, `counts` and `floors`, :2362–2414).
39. PIN-37 (`:1917–1920`): write-once; a replaced artifact is moved aside with `git mv` to a dated name on the seat's ruling, recorded in an entry — **CONFIRMED** (verbatim sense at :1917–1920).
40. One run writes `{U}_VERDICTS.json` and `{U}_secondary.json`; p's staged writer refuses a re-run while either exists (`analysis.py:202–212`) — **CONFIRMED** (:2416; analysis.py:202–212 converts m's "exists with different bytes -- write-once" on a seeded p output into a refusal "whether or not its inputs changed").
41. `p.decisions_beside` (`analysis.py:108–121`): m's three NOT-RUNs, each named `PROPOSAL-m OLMo-{ckpt}`, with reason and output sha256; not an input — **CONFIRMED** (it also carries `state`; read through `m_stages._committed`).

### §2

42. m:318's last sentence, verbatim — **CONFIRMED** (`/usr/bin/grep -c -F` of the block's quote against m:318 → 1; it ends the line).
43. m:358, step 17's OLMo clause, verbatim — **CONFIRMED** (fixed-string match on m:358 → 1).
44. p:84 is p §4.1's last sentence, verbatim — **CONFIRMED** (match at :84, the "**4.1 What is inherited unchanged**" paragraph, last sentence).
45. The seat's Q6, verbatim, `de729c4`'s raw §2 — **CONFIRMED** (raw :15 under "## 2. The analyzer path"; sha256 of :15 equals that of the block's :105 with "  > " replaced by "- ": `603317db…dc2d` both).
46. The dated note is on the `PROPOSAL-p v0.2 — COMMITTED` entry, added at `d215d5b` — **CONFIRMED** (`git show d215d5b -- RESULTS.md` adds "**Dated notes (2026-11-09; the design seat's answer of 2026-11-08 at `de729c4`, §2).**" with "p:84's decisions sentence (Q6)"; at HEAD it sits in the entry headed "PROPOSAL-p v0.2 — COMMITTED").
47. ADDENDUM-p1 §2.4, verbatim — **CONFIRMED** (fixed-string match → 1, line 30).
48. A-m1's (16) as its commit entry records it (`f26bc59`), with ellipsis — **CONFIRMED** (RESULTS.md@f26bc59:111–113; both halves match; the ellipsis spans "RESULTS.md@18c32df:382–383 already says so for any OLMo decision taken now, and").
49. m's three records each carry two input items, `other_unit` Q-F0 and `other_state` PASS; (16) dated 2026-11-06; the PI's go for the G-CAL run, 2026-11-06 — **CONFIRMED** (`cat` of the three records).
50. The seat's G-CAL-OLMo answers, line 9, quote — **CONFIRMED** (fixed-string match on :9 → 1).
51. The first draft item is byte-identical to the item in each of m's records — **CONFIRMED** (the four fields, indentation stripped, hash to `cc5f9061…020a` in the block and in all three records).
52. `valence_core/p/gcal.py:105` quote — **CONFIRMED** (the opening of `DISCLOSURE` at :105).
53. p §0.7's (5) D_p 2026-12-15 and (6) the pod budget, 12 h — **CONFIRMED** (p:25).
54. The dpo session's draft has the same two items and words the second differently — **CONFIRMED** (note lines 26 and 32; date 2026-11-07 in both).
55. Q-F3's VERDICTS session runs only after the `POSTING v1` entry exists (A-m1 (10′), as the 2026-11-15 (evening) answers §4.1 quote it) — **CONFIRMED** (that raw :50).
56. Q-F3's campaign is running — **CONFIRMED** by the record (`e5aba51`'s subject: "while Q-F3's campaign runs on the laptop"; the brief's campaign lines). Not checked live (nothing under `data/mf3`).

### §3, Q1

57. "Q6 (2026-11-08) names the decisions that existed then. Since then, more decisions …", with (iv) listing the G-CAL-p go — **IMPRECISE**. (iv)'s first member, the PI's routing of 2026-11-07, item 1 (the G-CAL-p go), predates Q6 (`de729c4`, 2026-11-08), and Q6 does not name it. `git merge-base --is-ancestor daca8b0 de729c4` → true, so the seat's §0.1 declaration at `daca8b0`, given as a decision "of other kinds" in "the same date range", also precedes Q6. Accurate form: Q6 (2026-11-08) names A-m1's (16) and the adoption. It names neither the PI's G-CAL-p go of 2026-11-07, which existed then, nor the decisions taken since.
58. (i) The PI's cap share "2 h each", PI date 2026-11-14, each lock's §2 at `038bf3e` — **CONFIRMED** (LOCK-p-OLMo-{sft,dpo,instruct}.md :29 "## §2. The hour cap …", :31 "**The PI's word, verbatim** (PI date 2026-11-14 …): **"2 h each"**").
59. m:318 names "an OLMo cap" — **CONFIRMED**.
60. (ii) "Place the locks", PI date 2026-11-14, in the close on the entry that held the locks, committed with the locks at `038bf3e` — **CONFIRMED** (`038bf3e`'s RESULTS.md diff: the close on `bd8808c`'s entry, "Route as given" + "Place the locks"; the v1.0 entry dated 2026-11-14).
61. m:318 names "a declined v1.0 after A0 is known" — **CONFIRMED**.
62. (iii) ADDENDUM-p1's (p-1), PI date 2026-11-15, committed at `fa27c45`; §2.4's "in m:318's form" and "after this re-specification" — **CONFIRMED**.
63. (iv) G-CAL-p: the routing of 2026-11-07, item 1, quote, in the `G-CAL-p-{sft,dpo,instruct}` entry — **CONFIRMED** (HEAD RESULTS.md, the entry added at `ec0d9d3`: "The PI's block of 2026-11-07, item 1, relayed verbatim …").
64. (iv) LOCK-p v0.1 and G-TIME-OLMo (p): the routing of 2026-11-08, item 2, quote, in each LOCK-p v0.1 header — **CONFIRMED** (each lock file :256, the v0.1 header kept verbatim).
65. (iv) LOCK-p v0.2 and G-F0m-OLMo (p): the routing of 2026-11-10, B1, quote (leading "..." included), in each v0.2 header — **CONFIRMED** (each lock file :161).
66. (iv) G-PWR (p), the wiring and LOCK-p v1.0: the routing of 2026-11-13, item 4, quote with ellipsis, in the close at `a2c354e` — **CONFIRMED** (the elided span is "the launch counts from k = 23/24/24 and your cap share per checkpoint within the 12 h budget [your call at G-PWR] → the campaign wiring (build now, land after G-PWR)").
67. (iv) The campaigns: "Go for the pod whenever you need it." (PI date 2026-11-15) and section B, item 5, "The campaigns as routed", in `41bfab4`'s entry — **CONFIRMED**.
68. (iv) These sessions: section B, item 6, "[go, after its commit]", and the PI's "Start them" — **CONFIRMED** (`fa27c45`'s entry; chat source 2).
69. The seat's §0.1 declaration at `daca8b0`: "Every entry, lock line and posted sentence that reports OLMo-SFT's A0 outcome carries *G-CAL-p passed at the bar, 47/64 against 47*" — **IMPRECISE** (quote). The source (`results/raw/2026-11-08_p-gcal_design-to-code_answers.md:9`) reads "every entry, lock line and posted sentence …" in lower case, after "**Declared now for p's record:**".
70. The p block carries that sentence already (`declared_sentences`, `report.py:220–222`) — **CONFIRMED** (`SFT_AT_BAR = "G-CAL-p passed at the bar, 47/64 against 47"` at report.py:109; the p block's `declared_sentences`, analysis.py:159).
71. The readings move nothing but the input's bytes: the list and its `inputs.decisions` sha256 — **CONFIRMED** (by item 38; the p block does not depend on the list).
72. (a)'s "For it": m:318's "in that unit's VERDICTS entry or NOT-RUN record" — **CONFIRMED**.
73. (a)'s "Against it": PIN-35's "m:318's record"; m's precedent put the PI's go in the input — **CONFIRMED** (items 36, 49).
74. "The dpo session's note reads (a)" — **CONFIRMED** (note line 14: the later decisions "are recorded in the VERDICTS **entry** …, not added to the file").
75. "Code's drafts of the items (b)–(d) add" — **IMPRECISE**. The four drafted items are (b)'s three and (c)'s campaigns' go. (d)'s further members of (iv) (the G-CAL-p go, the v0.1/G-TIME go, the v0.2/G-F0m go, the G-PWR/wiring/v1.0 go, these sessions' go) have no drafted item. Accurate: "Code's drafts of the items (b) and (c) add".
76. The (p-1) item quotes ADDENDUM-p1 §1's decision — **CONFIRMED** (its first clause verbatim, italics dropped; the clauses after "v1 included" are not carried).
77. The six drafted items are in the validator's shape (four keys; YYYY-MM-DD dates; `other_unit` Q-F0 ≠ an OLMo unit; `other_state` PASS ∈ Q5) — **CONFIRMED** (by reading :690–707; nothing ran).

### §3, Q2

78. Q6's list carries "p's own other units' known outcomes" — **CONFIRMED**.
79. m:318's trigger "taken after another unit's VERDICTS exist" — **CONFIRMED** (quote). The gloss after the colon is Code's reading (observation m6).
80. The three runs are serialized: battery windows one at a time while Q-F3's campaign runs — **CONFIRMED** (the brief's campaign line; `e5aba51`).
81. m's validator accepts a sibling as `other_unit` with its state word, and refuses PENDING — **CONFIRMED** (:701, :683–686). See observation m7 on "so a sibling can enter a list only once its VERDICTS or NOT-RUN record exists".
82. p keeps m's unit strings — **CONFIRMED** (p:84: "**p's records keep m's unit and template strings**").
83. The analyzer copies `data/p/verdicts`' files into staging before m's function runs (`analysis.py:190–195`) — **CONFIRMED** (it copies `*.json` regular files, :192–195).
84. m's refusals there test only the run's own unit's file names (`refuse_beside`, `m_analyze.py:1953–1964`) — **CONFIRMED** (called with the unit's own `outs`, :2390, :2415; `write_texts_once` on the unit's own two outputs, :2416).
85. A unit's VERDICTS run is the registered step (p §8 step 7) — **CONFIRMED** (p:132).
86. Q2 (a): "the dpo session's note reads the same" — **CONFIRMED** (note line 13: "p's own other units: no decision about OLMo-dpo was taken with a sibling's outcome known, so no item"); see observation m8.

### §4, Q3

87. p §2.3, verbatim — **CONFIRMED** (fixed-string match at p:68).
88. The `task_correct` ruling (G-TIME-OLMo (p) answers, line 34), verbatim in part — **CONFIRMED** (the quoted words are at :34). See observation M2 for the clause it leaves out.
89. The 2026-11-14 answers, §B.4 item 3 (line 67): "The VERDICTS entry opens the rest (m:271)." — **CONFIRMED** (:67 under "**B.4 Q3 — …**").
90. `report.session_counters` (`report.py:260–303`), called once per stage report (`stage.py:966`) — **CONFIRMED** (the function is :260–301, then two blank lines; :966 is in `build_report`, def :917; its only other caller is report.py's self-test, :446).
91. What it counts (hair trigger over every round; sham control characters, harness first lines, cap hits, refusals; corrupted spelling over sham forced rounds; contrast forced rounds' control characters) — **CONFIRMED** (:279–300).
92. "Every other count is ``WITHHELD``" (its docstring, `:270`) — **IMPRECISE** (quote). The source at :270 reads "every other count is ``WITHHELD``" in lower case.
93. `WITHHELD` (`:249–252`), verbatim — **CONFIRMED** (the four string pieces joined equal the block's quote byte for byte).
94. "every proxy count over the contrast sessions withheld, as at G-TIME" (`stage.py:35`, of G-F0m-OLMo (p)'s report) — **CONFIRMED** (:35 in the qualification paragraph).
95. The campaigns' entry (`41bfab4`) defers the same counts to each unit's VERDICTS — **CONFIRMED** ("The contrast arms' counts other than the forced rounds' control characters are withheld to each unit's VERDICTS (m:318)"; the sham free rounds' corrupted-spelling count "withheld to VERDICTS").
96. The `p` block's keys (`analysis.py:155–160`); no p counter, no `task_correct` — **CONFIRMED** (proposal, register, roots, analyzers, d_p, disclosure, decisions_beside, declared_sentences, staging; `resolution` only on the posting path).
97. m's own counters in the output are m:314's — **CONFIRMED** (`counters_json`, :2383; PIN-11 at :897: "the counters are m:314's two lists in full").
98. `p_sessions.py`'s report commands (`:715–733`) "re-derive the stage reports, withheld part included" — **IMPRECISE**. The anchors hold (time-report :715–717, qual-report :722–724, campaign-report :731–733). The commands re-derive p's report "from m's checkpoint and the call log … when a stage ended and its tail did not write the report", written once and refused when the report exists (usage :51–57, :74, :91–92). They go through the same builder (`stage.write_report` → `build_report` → `session_counters`), so the re-derived report withholds the same part. As written, "withheld part included" can read as computing it. Accurate: "re-derive the stage reports, the same part withheld". The entry's wording, "re-derive the stage reports", is accurate.
99. `report.counters` (`:225–246`) is G-CAL-p's form, keyed by pool, item and seed, called at `gcal.py:408` — **CONFIRMED** (function :225–245; key at :230; gcal.py:408 `cn = report.counters(recs, pool)`).
100. `task_correct` at G-F0m-OLMo (p) was computed by Code's own script — **CONFIRMED** (the raw's lines 2, 30, 38).
101. The quote "reads the reads files' sham records only, never the checkpoint, the call log or a contrast session" — **IMPRECISE** (quote). The raw's string is "the reads files' sham records only, never the checkpoint, the call log or a contrast session" (:36). That is the read licence the script's docstring quotes from "the seat's answers of 2026-11-10 (p qual wiring), §4, and the PI's routing of 2026-11-10, B4" (:35), and "reads" is not part of it. The script's own sentence is :2, "It reads the reads files' sham records only (a contrast record is skipped by its flag, nothing of it accessed)".

### §4, Q4

102. "m's form for a VERDICTS entry includes Code's own extractions from the released checkpoints (Q-F0's E1–E12)"; (b) "m's form in full" — **IMPRECISE**. Q-F0's VERDICTS entry (RESULTS.md@0fa8539:350–356) calls the extractions raw "an addition to block §4's list that carries no figure of record". It calls E3's split and E12 "Code's additions: post-hoc". m:358 step 17's list for a VERDICTS entry names no Code extraction. Accurate: "Q-F0's VERDICTS entry, m's one precedent, carried Code's extractions E1–E12 as an addition to the seat's block §4 list". See observation M3.
103. Q-F0's VERDICTS entry (2026-10-19, `0fa8539`) carries the analyzer's two outputs and Code's script over the released checkpoint, run after the output existed: E1–E12, "21 of 21 checks equal" — **CONFIRMED** (RESULTS.md@0fa8539:352 "Code's script and its output, E1–E12, 21 of 21 checks equal"; the raw's :2 "Made after the analyzer's output exists (bfc179c …)"; its last line prints 21/21).
104. Among them: E3 seconds and stage durations; E2 the looks' contrast side; E5, E11 the gate stages' later picks and exclusion details; E12 secondary (e) over the domain alone, labeled post-hoc (m:320; rule 11) — **CONFIRMED** (the extractions raw's headings :12, :27, :50, :89, :97; m:320 verbatim "Any analysis not listed is post-hoc, labeled, licensing at most a new pre-registration (rule 11)").
105. The list of record v2 binds "before its VERDICTS or NOT-RUN record" (its §2 heading) — **CONFIRMED** (list raw :16, "… for every unit before its VERDICTS or NOT-RUN record; …").
106. The briefs' text "p's checkpoints and call logs (`data/p/ckpt`) are read only by the analyzer (list v2 item 2). Never open them yourself." — **IMPRECISE** (quote, minor). The instruct session's brief, as given to me, reads "**p's checkpoints and call logs** (`data/p/ckpt`) are read only by …". The bold markers are dropped without the record's usual "(bold markers aside)".
107. The sft and dpo sessions' briefs say the same — **NOT CHECKABLE** (those briefs are not in the repository or the dpo note).
108. `data/p/ckpt` holds all three units' files — **CONFIRMED** by the entries (`41bfab4`, `2258c52` and `a225a89` name `data/p/ckpt/OLMo-{ckpt}_{campaign,time,qual}.json`). Not listed (rule).

### §5

109. Under Q1 (c), each unit's input is §2's two items and four more, identical but for `unit`, at `data/p/verdicts/OLMo-{ckpt}_decisions.json` — **CONFIRMED** (consistent with §3's four drafts; see observation m12).
110. Every VERDICTS entry carries ADDENDUM-p1 §2.4's sentence — **CONFIRMED** (ADDENDUM-p1 §4 step 3: "each entry carrying §2.4's sentence").
111. Code adjudicates nothing (CLAUDE.md; WORKFLOW.md §4) — **CONFIRMED** (CLAUDE.md "Code escalates fired gates, never self-adjudicates"; WORKFLOW.md §4 "**"Code adjudicates nothing"**").

### §6

112. `verdicts` never reaches `m_analyze.battery()`: only `_selftest` calls it (`p_analyze.py:344`), and only `--selftest` (`:722`) and `ganl` (`:668`) reach `_selftest` — **CONFIRMED** (:344 is in `_selftest`, def :300; `_selftest` is called only at :651 in `run_battery`, which is called only at :668 and :722; in m_analyze.py, `battery()` is called only at :11110 (m's `ganl`) and :11301 (m's `--selftest`)).
113. It touches nothing under `data/mf3`; m's `run_verdicts` reads the lock, the decisions file, the three checkpoints, committed blobs through git, PROPOSAL-m, ADDENDUM-m1, CLAUDE.md and the analyzer — **CONFIRMED** by code reading (ADDENDUM-m1 via `_clock_refusal`, :2004–2012; CLAUDE.md via `stages.gate_line`, stages.py:467–488; no module-level mf3 import in m_analyze.py, stages.py or `valence_core/p/*.py`). Not run.
114. Q-F3's reader (`:2249–2250`) is not reached for an OLMo unit — **CONFIRMED**.
115. `production_env()` with no unit adds no mf3 module to the closure (`:1904–1911`) — **CONFIRMED** (:1906 `lz = … if unit == UNIT_F3 else None`; `closure` then imports `LAZY_VERDICT_MODULES = ("valence_core.m.stages",)`, :143, :1837).
116. p's side reads, through git, PROPOSAL-p for D_p, the code of record and m's NOT-RUN outputs; reads the lock's text; copies `data/p/verdicts` — **CONFIRMED** (`d_p_problems`, analysis.py:81–92; `binding_problems`, p_analyze.py:84–97, and `gcal.committed_problems`, gcal.py:170–180; `decisions_beside`; `lock_binding_problems`, p_analyze.py:156–165; `run_staged`).
117. Each lock's sha256 "is its campaign checkpoint's `lock_sha256` as `41bfab4`'s entry gives it" — **IMPRECISE** (anchor). The values agree. `41bfab4`'s entry gives the prefixes in its precheck bullet ("`lock_sha256` `fafb786d…`, `25c52f56…` and `f71c97c1…`"), from the precheck raw's `lock_sha256` (:11, :13, :15, printed from the precheck's `identity_extra`, :75), and says only that each m report's identity "carries its lock's sha256". It states no checkpoint field. Accurate: "the precheck's `lock_sha256` as `41bfab4`'s entry gives it" (the entry draft's "its campaign's `lock_sha256`" is fine).
118. `--campaign`/`--time`/`--qual` are `data/p/ckpt/OLMo-{ckpt}_{campaign,time,qual}.json`, as `41bfab4`, `2258c52` and `a225a89` name them — **CONFIRMED** (one match each in the three RESULTS.md diffs).
119. They are `p_analyze`'s defaults (`p_analyze.py:180–181`) — **CONFIRMED** (with `P_CKPT = REPO / "data" / "p" / "ckpt"`, :61).
120. No `--adjudication` (each m report's `pauses` empty, per `41bfab4`) and no `--pi-stop` — **CONFIRMED** (the entry: "Each m report's `pauses` is empty and its `stop` null").
121. The input's home in Q-F0's input style; the `PROPOSAL-m OLMo-{ckpt} — NOT-RUN` entry gives the reason — **CONFIRMED** (`0f35954`'s entry: "The file name is Code's, in Q-F0's input style (`{U}_decisions.json`, `{U}_olmo-states.json`), inside the repo so the output records its path relative to the root").
122. `.gitignore`'s `!/data/p/verdicts/*.json` admits it — **CONFIRMED** (.gitignore :311–313).
123. Committed with the outputs, as Q-F0's was (`bfc179c`) — **CONFIRMED** (`bfc179c` adds `data/m/verdicts/Q-F0_decisions.json` beside `Q-F0_VERDICTS.json` and `Q-F0_secondary.json`).
124. One invocation per unit at `nice -n 19`, in the coordinating session's battery windows — **CONFIRMED** as the record's practice (laptop runs "at `nice -n 19`" in the G-SHAPE-p, G-ANL-p and n-schema entries; the brief's window line). It is a plan.

## B. The entry

125. Heading: the record does not fully settle the input or two things the entries carry; STOP for the seat's read; "No p VERDICTS output exists" — **CONFIRMED** (items 27, 57–108).
126. The routing, verbatim: the PI's paste block of 2026-11-15 (evening), "Route as given", section B, item 6 — **CONFIRMED** (fixed-string match of the quoted item in RESULTS.md@fa27c45 → 1; that entry gives the header "PI date 2026-11-15 (evening)" and "Route as given").
127. "Start them", relayed by the coordinating session — **CONFIRMED** (chat source 2, verbatim).
128. The coordinating session's words "So it's a STOP for the seat: one joint block for all three units, written by you, since you raised it." — **CONFIRMED** (chat source 1, a verbatim substring).
129. "the sft and dpo sessions hold too"; "The sft and dpo VERDICTS sessions sent their facts and readings, and each item taken from them was re-verified" — **NOT CHECKABLE** (chat and the sessions' conduct).
130. What the record settles: Q6 (`de729c4`, §2; note at `d215d5b`), two items with Q-F0/PASS, the adoption dated 2026-11-07; `analysis.decisions_beside`; Q-F3 known at no run — **CONFIRMED** (items 41, 45, 46, 51–55).
131. "The three sessions agree on these" — **NOT CHECKABLE** for sft (as item 28).
132. Q1's bullets: "2 h each" (2026-11-14) with m:318's "an OLMo cap"; "Place the locks" (2026-11-14) with "a declined v1.0"; (p-1) (2026-11-15) with §2.4's "m:318's form"; the goes as the class m's records put in the input — **CONFIRMED** (each a verbatim substring of its source).
133. Q2's summary (the trigger, the two procedures) — **CONFIRMED** as consistent with the block. The trigger gloss is Code's reading (observation m6).
134. Q3: p §2.3's "reported in the gate and VERDICTS entries"; the ruling's "the contrast sessions' rounds at the unit's VERDICTS"; "to the unit's VERDICTS … recomputable from the checkpoint" (`report.py:249–252`); "No p code computes it … the report commands re-derive the stage reports" — **CONFIRMED** (each a verbatim substring; anchor holds).
135. Q4: "m's form for a VERDICTS entry includes Code's own extractions from the released checkpoints (Q-F0's E1–E12, `0fa8539`)" — **IMPRECISE**, as item 102.
136. Q4: the list v2 quote; the briefs' "Never open them yourself", with no end given — **CONFIRMED** for the instruct brief (sft and dpo briefs as item 107).
137. Code's readings: Q1 (c) for the instruct session; the dpo note's (a) as "§2's two items in the input, the rest in the entry"; Q2 (a); none on Q3 or Q4 — **CONFIRMED** (consistent with the block's §5 and the dpo note's lines 10–14).
138. Not questions: lock sha256 = the campaign's `lock_sha256` (sft `fafb786d…`, dpo `25c52f56…`, instruct `f71c97c1…`); the checkpoint paths; no adjudication, no PI-stop; §2.4's sentence in every VERDICTS entry — **CONFIRMED** (items 15, 110, 117–120).
139. The block's link `results/raw/2026-11-16_p-verdicts-decisions_code-to-design.md`, with Code's draft items in its §2 and §3 — **CONFIRMED** (WORKFLOW.md §4's path form; the drafts are in §2 and §3; the file is not yet in `results/raw`, as expected before the commit).
140. This session's reads (one filtered `git ls-files` over `data/p`; two refused name listings under `data/p/ckpt`) — **NOT CHECKABLE** (the session's own commands).
141. Next: the three runs, then six entries, each VERDICTS entry with §2.4's sentence — **CONFIRMED** (m:358 step 17 and ADDENDUM-p1 §4 step 3: `— VERDICTS` and `— secondary DVs` ×3).

## Totals

141 claims: 123 CONFIRMED, 12 IMPRECISE, 0 FAIL, 6 NOT CHECKABLE

(IMPRECISE: 20, 35, 57, 69, 75, 92, 98, 101, 102, 106, 117, 135. NOT CHECKABLE: 26, 28, 107, 129, 131, 140.)

## Observations

**MAJOR**

- **M1. Q1's frame, "the decisions taken since Q6".** (iv)'s first member, the PI's G-CAL-p go (routing of 2026-11-07, item 1), predates Q6 (`de729c4`, 2026-11-08). Q6 also names no go of any kind. Yet m's two-item precedent (`0f35954`, committed 2026-11-07, carrying the PI's G-CAL go as an input item) was in view when the seat wrote "A-m1's (16) as m's records carry it". Q6's silence on goes is therefore not only a matter of date. That bears on (a)'s "For it" ("Q6's form names no later decision") and on the precedent argument for (c) and (d). The seat's §0.1 declaration (`daca8b0`) also precedes Q6 (`daca8b0` is an ancestor of `de729c4`). The block's "Q6 (2026-11-08) names the decisions that existed then" invites the opposite reading.
- **M2. Q3 leaves out the operative half of the seat's `task_correct` ruling.** The same line 34 that the block quotes "in part" continues: "**Tabulated by Code's own step from the records at each entry** (A-m2 v0.3 §3.4's form), not by p's package or the analyzer: no package moves, no hash moves, no re-run." A-m2 v0.3 §3.4 (`archive/ADDENDUM-m2-f3-reasoning-block-v0_3.md:48`) gives that form at VERDICTS: "At VERDICTS the analyzer is untouched: Code tabulates (a), (b) and the Q4 review counter with mf3's functions over the same records in its own step, reported in the VERDICTS entry beside the analyzer's outputs". The task_correct raw's docstring (:38) cites the same form. For `task_correct` over the contrast sessions, the seat has therefore already ruled who computes it and from what. Option (b), "not computed at VERDICTS", would depart from that ruling, and the ruling presumes a Code read of the records at VERDICTS, which bears on Q4. p §2.3's own words ("computed by p's own reporting tool over the checkpoints") likewise register a reader of the checkpoints for the VERDICTS counters. As drafted, Q3 and Q4 are presented as if no ruling existed.
- **M3. Q4's "m's form".** The Q-F0 VERDICTS entry records the extractions as "an addition to block §4's list that carries no figure of record", and E3's split and E12 as "Code's additions: post-hoc" (RESULTS.md@0fa8539:350–356). m:358's list for a VERDICTS entry names no Code extraction. Calling the extractions "m's form" (and (b) "m's form in full", in the block and the entry) can lead the seat to read (a) as a departure from m, when the record makes the extractions Code's precedent, not m's requirement.

**MINOR**

- m1. `9c641e19…6a96d` (header) has a five-character tail. The campaigns' entry writes the same blob as `9c641e19…a96d`.
- m2. "withheld part included" (block §4) against "re-derive the stage reports" (entry): the wording differs, and the block's can be read as the report commands computing the withheld part (item 98).
- m3. The campaigns have earlier goes than those (iv) and the (c) item name. One is the routing of 2026-11-13, items 5 ("The replacement pod, on your go …") and 6 ("Then the bundle, precheck ×3, the three campaigns within one pod session … [go]"), quoted at `a2c354e`. The other is the 2026-11-14 (evening) section B, item 4 ("… three campaigns at 2 h each, (d)'s line after each invocation [go at the PI's timing]"), quoted at `038bf3e`. The (c) item names only the 2026-11-15 words the campaigns' entry quotes.
- m4. Under (d), the further items are not drafted (item 75), so the seat cannot read their exact text before choosing (d).
- m5. Q3 (a): "If the tool is not in p's package, p's package hash does not move" understates the consequence. LOCK-p v1.0 §4 pins p's package sha256, and `p_analyze`'s `lock_binding_problems` (:156–165, applied at :173–176) refuses a VERDICTS whose lock does not name the current p `package_sha256`. A tool placed inside `valence_core/p/` before the last of the three runs would therefore make the remaining `verdicts` runs refuse. I did not compute the current package hash (no Python).
- m6. The Q2 gloss "what counts is that the VERDICTS exist, not that anyone has read them" (the entry: "m:318's trigger is that VERDICTS exist, not that anyone read them") is stated as fact, not marked as Code's reading. m:318's record form says "as taken with the other unit's outcome known".
- m7. "so a sibling can enter a list only once its VERDICTS or NOT-RUN record exists": the validator checks the state word (Q5, PENDING refused), not that the sibling's output exists. The constraint holds by rule, not by code.
- m8. The dpo note's line 13 was written before any sibling VERDICTS existed. It does not take up whether a later run, or the window that starts it, is a decision, which is what separates Q2 (a) from (b). "Reads the same" is Code's characterization.
- m9. The sft session's readings on Q1 and Q2 are not given, though the header says the sft and dpo sessions sent theirs, and Q1 (c) is labeled "for the instruct session".
- m10. The coordinating session asked, per question, for "your reading marked as a reading". The block gives none on Q3 or Q4 and states why. The seat may want that departure named as such.
- m11. What every VERDICTS entry carries under every reading also includes p §5.4's disclosure (p:102: "Every p entry, lock, artifact and posted sentence that reports a p outcome states …"). For sft, the entry, and not only the output's p block, must carry the §0.1 sentence ("every entry … carries"). The block's §5 names only ADDENDUM-p1 §2.4's sentence.
- m12. The (p-1) item's decision text contains a literal `{ckpt}` (from ADDENDUM-p1 §1), while `"unit": "OLMo-{ckpt}"` in §2 is a placeholder. A substitution over the whole file would alter the decision text and break "identical but for `unit`".
- m13. Dates, for context. Decision (16) was routed on PI date 2026-11-05 (`f26bc59`'s subject; m_analyze.py:141 `ADDENDUM_M1_DATE = "2026-11-05"`, "A-m1's commit day (f26bc59; the PI's routing date)"). m's records and the draft date it 2026-11-06, the entry's date, as the seat's line 9 specifies ("dated as its commit entry is"). For the adoption, p §5.4 (p:102) says "pre-registered on 2026-11-06", and the draft's 2026-11-07 follows the seat's F-p3 ruling as carried in `gcal.DISCLOSURE`.
- m14. The entry's heading opens "PROPOSAL-p OLMo-{sft,dpo,instruct} — VERDICTS: held …", the entry name that ADDENDUM-p1 §1 and §2.4 key on. A later referent check for "no `PROPOSAL-p OLMo-{ckpt} — VERDICTS` entry exists" could match this hold entry.
- m15. The header's source list omits sources the body cites: the G-CAL-p entry (`ec0d9d3`), A-m1's commit entry (`f26bc59`), the Q-F0 extractions raw, `valence_core/m/stages.py` (for the gate line), m:271/m:314/m:320 beyond "m:318, m:358", and the dpo note (outside the repository). WORKFLOW.md §4 asks for "the sources read … by sha256".
- m16. The list v2's §2 heading also says "open today: Q-F3 (`data/mf3`), p (`data/p`), n …". It names p as one open domain, which bears on Q4's per-unit question. The block quotes only the per-unit clause.
- m17. p §8 step 6 registers "the PI's cap share" (and step 5 "the PI's go for the box") as steps, as step 7 registers the VERDICTS run. Q2 (a)'s rationale ("the registered step … is not a decision") sits beside Q1's treatment of the cap share and the goes as decisions. m:318 names "an OLMo cap" explicitly, so the line may hold, but the seat may want it drawn.

## Disclosures

- Content reads of committed files outside `data/` (outside item 1's names-only list; not restricted by items 2–3): `git show <rev>:RESULTS.md` at `f26bc59`, `fa27c45`, `0fa8539` and HEAD; `git show --format= <rev> -- RESULTS.md` (diffs of RESULTS.md only) at `d215d5b`, `038bf3e`, `a2c354e`, `2258c52`, `a225a89`, `41bfab4`, `0f35954`; `awk`/`sed`/`/usr/bin/grep` on single named files; `cat` of the three `data/m/verdicts/OLMo-*_not-run-record.json` (as the brief permits).
- `git show --name-status --format= <rev> -- . ':!data/*/ckpt/**' ':!data/*/reports/**' ':!data/mf3/**'` over 18 commits: item 1's form, with item 3's exclusion added.
- One pickaxe, `git log -S'<the G-CAL-p entry's heading text>' -- RESULTS.md`. It is item 3's content search, with its pathspec limited to RESULTS.md, so no `data/` path was in range.
- One `git ls-files | /usr/bin/grep -i 'ADDENDUM-m2'` over the whole index. Only two names printed (one at the root, one in `archive/`). The enumeration itself passed over index names under `data/*/ckpt`, `data/*/reports` and `data/mf3`, none printed. It is item 1's form, but it may fall under the brief's "never … list anything under `data/*/ckpt`", so I disclose it for the seat. Also `git ls-files data/p/verdicts` and `git ls-files data/m/verdicts` (scoped).
- `git status --porcelain -- <named paths>` (scoped); `git check-attr -a` on two absent `data/p/verdicts` paths; `git log` with `--format` of ids, subjects and dates, and `--diff-filter=A`, over named paths; `git merge-base --is-ancestor daca8b0 de729c4`; `git log --format=%h daca8b0..de729c4 | wc -l`; `shasum -a 256` on named files outside `data/*/ckpt|reports` and on the drafts.
- `wc -l` on committed documents and code (line counts only, none under `data/`): outside item 1's list.
- Name-only `ls`: of `results/raw` (filtered), of `data/p/verdicts` (absent), and of the side-session-notes folder outside the repository.
- Read beyond the brief's listed sources: `archive/ADDENDUM-m2-f3-reasoning-block-v0_3.md` (lines 7, 25, 46, 48); `results/raw/2026-10-19_m-verdicts-qf0-entry_extractions.txt` (headings, :2–3, E3's first lines, E5's lines); `results/raw/2026-11-15_p-campaign_precheck.txt` (a grep for `lock_sha256`: its :11, :13, :15, :75) and a `lock_sha256` count over `results/raw/2026-11-15_p-campaign_OLMo-sft.txt` (0); `valence_core/m/stages.py` (a grep for `gate_line`/`CLAUDE`); PROPOSAL-p §5.4 and §8; the G-CAL-p entry; `p_sessions.py`'s usage text; and the dpo session's note (permitted). For one anchor (item 46), I also read the working-tree RESULTS.md, which carries another session's staged changes. Every other RESULTS.md read was of a commit.
- No Python, no git write, no whole-tree `git status`, and nothing under `data/*/ckpt`, `data/*/reports` or `data/mf3` opened, hashed or stat-ed.
