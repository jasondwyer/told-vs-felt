# Blind values-check of the G-CAL-OLMo entry (draft) and of the BACKEND (190ba90) and smoke (b9a26ef) entries -- the checker's report verbatim, its scratch-folder names normalised to <scratch>/, then Code's dispositions. PI-local date 2026-11-06.

# Blind values-check: the G-CAL-OLMo entry draft (A), the BACKEND entry at 190ba90 (B), the smoke entry at b9a26ef (C)

Checker: a blind values-check agent, read-only. PI-local date 2026-11-06. Repo HEAD at check time: `54bbfe5`
(RESULTS.md unmodified; the six G-CAL-OLMo artifacts and the two G-CAL raws untracked in the tree). Nothing in the
repository was edited, created, staged, committed or deleted.

Texts: (A) `<scratch>/gcal_entry_draft.md` (placeholders ignored); (B) `git show 190ba90:RESULTS.md | sed -n '24,92p'`;
(C) `git show b9a26ef:RESULTS.md | sed -n '24,93p'`.

## Verdict legend

- **CONFIRMED**: matches a committed source, a tool recomputation, or a live read.
- **CONFIRMED-BY-RAW-HEADER-ONLY**: the only source is a raw's header written by the same author (box-side facts).
- **CONFIRMED-BY-SCRATCH-ONLY**: no committed source. The only support is the author's uncommitted captures of box
  state in the session scratchpad (`<scratch>/`: `box_dirty_hashes.tsv`, `holding_out.txt`, `holding_hashes.tsv`,
  `box_ignored.txt`, `modified_list.txt`, `untracked_list.txt`, `watch.log`, `jspace.bundle`, `gcal_box_sha.txt`).
  These are evidence, but they are not the record.
- **NOT CHECKABLE**: no source at all (chat-only words, write-time stamps, box-side facts with no capture).
- **IMPRECISE**: true, but misleading, overstated, or not exactly as the source has it.
- **FAIL**: contradicted by a source.

## How it was checked (by tool, not mental arithmetic)

- Counts, fractions, bars, covariates, cap hits, cross-checkpoint identity counts and control characters were recomputed
  in Python from `data/m/ckpt/G-CAL_olmo-{ckpt}.json`, whose records equal the gate artifacts' records. Tallies (iii)
  and (iv) were recomputed by re-implementing `gcal.py:1029–1073` against `data/m/gates/G-CAL_model-free.json` and
  `data/configs/f_termination_patterns.json`.
- sha256 was recomputed for all six artifacts, the answers file (working tree and 54bbfe5's blob),
  `scripts/m_sessions.py` at 1bf94a6, and `data/olmo/determinism_base.json`.
- Each raw's "verbatim" body was re-hashed against its declared box sha256, and all match: integrity `ab7aae4d…`,
  determinism `6b31aada…`, smoke `f753c659…`, box self-test `2854e383…`, the three G-CAL logs
  `b22fb127…` / `6a571918…` / `c4774357…`, stamps `f6e6f9ca…`, smoke script `179ab066…`, wrapper `525e60d3…`.
- The backend identifier was recomputed from `resume.py`'s definition (`BACKEND_DROP = ("n_encodes_clipped", "path",
  "seed")`, resume.py:147, :239–246) on three inputs: the determinism raw's printed block, the committed 2026-08-19
  block, and each G-CAL provenance record. Every result is `641ee466f4553b6a`.
- The read raw's section 5 was parsed: 384 generation lines, each identical to its checkpoint record in hit, n_tok, stop
  and text (0 mismatches). I made my own read of tallies (i) and (ii) from the texts.
- Live read-only RunPod reads at about 2026-11-07T02:52Z: `get-pod qny1x4v8padeke`, `get-pod uimuzt7d890y5b`,
  `get-network-volume o73qvy742n`. Also `git ls-remote origin` and the local reflog of `refs/remotes/origin/main`.
  No host, IP or port appears in this report.

## Summary

165 items: **122 CONFIRMED, 13 CONFIRMED-BY-RAW-HEADER-ONLY, 12 CONFIRMED-BY-SCRATCH-ONLY, 10 NOT CHECKABLE,
8 IMPRECISE, 0 FAIL.**

| text | items | CONFIRMED | RAW-HEADER-ONLY | SCRATCH-ONLY | NOT CHECKABLE | IMPRECISE | FAIL |
|---|---|---|---|---|---|---|---|
| A (draft) | 1–65 | 54 | 5 | 1 | 2 | 3 | 0 |
| B (190ba90) | 66–123 | 37 | 3 | 11 | 6 | 1 | 0 |
| C (b9a26ef) | 124–165 | 31 | 5 | 0 | 2 | 4 | 0 |

The eight IMPRECISE items:

- **42 (A):** the tallies table's (i) column ("state the answer: 9 of 12 / 8 of 12 / 7 of 9") reports the complement of
  R1 A6's tally (i). R1 A6 defines (i) as hits "whose text does not state the answer" (RESULTS.md@9cbacdb:4108), so
  the declared tally is 3 / 4 / 2.
- **46 (A):** "the feathers called heavier, or "90 * 45 = 4050"" reads as an exhaustive list, but it misses one case.
  sft corrupted 7 s3 gives both weights as 1 kilogram with no comparison. Also, "90 * 45 = 4050" is dpo's text only;
  sft's is "90 miyms 45. = 4050".
- **51 (A):** "(item 2 at 0/12, item 9 at 2/12, both artifacts)": the counts are right, but "both artifacts" reads as
  covering both items. Per O1, only item 9's two hits are artifacts; item 2's 0/12 are plain misses.
- **85 (B):** "re-hashed every file under /workspace/models/": the script checks only the manifest's files in the
  four checkpoint directories, plus unlisted entries there. Files directly under /workspace/models/, such as
  determinism_base.json, are not hashed. The wording comes from CLAUDE.md's protocol and the 2026-08-23 entry.
- **133 (C):** the quotation "the box run writes data/m/gates and data/m/ckpt only" drops the stage label in
  parentheses, "the box run (G-CAL-OLMo-{ckpt}) writes …", without marking the cut (m_sessions.py:484–486).
- **135 (C):** "Per unit: … olmo_weights_problems; driver_problems": driver_problems ran once, before the unit loop,
  not once per unit. The table row "weights and driver checks: clean ×3" repeats that one shared check in each column.
- **139 (C):** "8 generations through G-CAL-OLMo's own loop body (gcal.py:1152–1165)": the smoke script does not
  execute those lines. It re-implements their three calls, with identical arguments, in its own loop. Its own docstring
  says "own call (gcal.py:1155-1165)".
- **155 (C):** the check at "m_sessions.py:6923–6929" holds the expectation, but two things sit just above that range:
  the pod-id forcing and the box-path call (6919–6922). That call runs unit OLMo-instruct, not OLMo-sft. The substance
  is unchanged.

---

## A. The G-CAL-OLMo entry draft

1. **CONFIRMED.** Claim: "PROPOSAL-m v1.11 m:176, m:302, §5". m:176 has "**G-CAL-OLMo:** condition (4) per
   checkpoint (128 generations) … failure → that checkpoint NOT-RUN with reason "dose not completable" (§5)". m:302 is
   the G-CAL-OLMo-{ckpt} node. §5 (m:324) makes an OLMo unit NOT-RUN when "its G-CAL-OLMo failed condition (4)".
2. **CONFIRMED.** Claim: "ADDENDUM-m1 §4 step 4". ADDENDUM-m1:59 is the OLMo track: … → `BACKEND — characterization` →
   G-CAL-OLMo-{ckpt} → ….
3. **CONFIRMED.** Claim: "the PI's routing of 2026-11-06 and the seat's answers C1–C4". The routing is at
   RESULTS.md@54bbfe5:233 ("PI date 2026-11-06"). The answers' §C holds C1–C4 (answers:35–45).
4. **CONFIRMED.** Claim: "CONDITION (4) FAILS ON ALL THREE CHECKPOINTS". Each artifact's `condition_4.verdict` is
   FAIL. Recomputed: corrupted 21/32, 11/16 and 21/32 fall below both bars.
5. **CONFIRMED.** Claim: each is NOT-RUN with reason "dose not completable". Source: the three driver end lines (raw
   `_gcal-olmo` :175, :320, :465) and each artifact's `on_fail`.
6. **CONFIRMED.** Quote: "failure → that checkpoint NOT-RUN with reason 'dose not completable'". It matches m:176 word
   for word; the source's inner double quotes are rendered as single quotes inside the outer quote.
7. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "Escalated to the seat; nothing adjudicated". The only source is raw
   `_gcal-olmo`:10, "Escalated; nothing adjudicated".
8. **CONFIRMED.** Claim: "The verdict of record is the grader's". Sources: the seat's ruling
   (`results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1.md`:19, "condition (4) PASS stands as graded. The seat
   adopts no re-grading") and m:176's grader pin.
9. **CONFIRMED.** Quote: "Go for G-CAL-OLMo on sft, dpo and instruct, smoke first". Exact at RESULTS.md@54bbfe5:237.
10. **CONFIRMED.** Claim: "order (a) with the second-STOP flip as C1, batching as C2, the pod up through the OLMo
    track". Source: RESULTS.md@54bbfe5:238–239. The block spans :233–241, and :237 is its first body line.
11. **CONFIRMED.** Claim: the block is "quoted in the G-ANL-F3 STOP entry's close (RESULTS.md@54bbfe5:237)". The STOP
    entry opens at @54bbfe5:163 and its close at :196. Lines :231–243 (the routing block) sit inside that close.
12. **CONFIRMED.** Claim: the answers file has "sha256 4edfbb8e…ca42e, committed at 54bbfe5". The working-tree file
    and 54bbfe5's blob both hash to `4edfbb8e3d08…2207777ca42e`. `git show --stat 54bbfe5` shows the file added.
13. **CONFIRMED.** Claim: "section C is this run's". Answers §C (answers:33–45) opens with C1: "G-CAL-OLMo-{ckpt}
    runs now …".
14. **CONFIRMED.** Quote: "as the BACKEND entry has it". Exact at answers:36.
15. **CONFIRMED.** Claim: "The apparatus smoke of b9a26ef". b9a26ef is that entry: RESULTS.md plus the two smoke raws.
    The PI's words "Yes, smoke" are chat-only, recorded only in b9a26ef's texts.
16. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: after C4's line, the prechecks were re-run "in a fresh shell with env.sh
    alone: PASS ×3, pod id qny1x4v8padeke". The only source is raw `_gcal-olmo`:3.
17. **NOT CHECKABLE.** Claim: the re-run found "driver and weights clean". The raw header (:3) records only "PASS x3,
    pod id qny1x4v8padeke". Nothing records the re-run's driver and weights results. (The runs of record printed DRIVER
    and WEIGHTS lines and then loaded; the driver allows that only when both checks are clean, m_sessions.py:460–461,
    :497–509.)
18. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: one line was appended to /workspace/env.sh (sha256 a0587921… →
    f5174faa…; old file kept as env.sh.bak-2026-11-06). The only source is raw `_gcal-olmo`:4.
19. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: the quoted C4 line. It is byte-identical to raw `_gcal-olmo`:5 and to
    the author's scratch `c4_line.txt`. Its form meets C4's terms (answers:45: exported from the PID-1 environment via
    /proc/1/environ, never typed). Whether it is in the box's env.sh is a box-side fact.
20. **CONFIRMED.** Claim: the variable is "unset before source and qny1x4v8padeke after; resume.pod_id() returns
    qny1x4v8padeke". The evidence is indirect but comes from box output:
    - stamps.txt (raw :24, :26, :28) prints `RUNPOD_POD_ID=qny1x4v8padeke` right after the wrapper's
      `source /workspace/env.sh`;
    - each checkpoint's provenance `pod_id`, written by `resume.pod_id()` at gcal.py:1142, is qny1x4v8padeke;
    - before C4 the variable was unset: smoke raw:10, "inherited by this process: None".

    The fresh-shell test itself is not in any raw.
21. **CONFIRMED.** Claim: "C4's check: PASS ×3 … provenance block records pod_id qny1x4v8padeke (one entry each, 128
    launched)". Each checkpoint and each artifact has exactly one provenance entry: pod_id qny1x4v8padeke, launched
    128. Note that C4 (answers:45) says the provenance block "must print" the id "or STOP". The PASS rests on reading
    it from the checkpoint's provenance entry, which item 22 discloses.
22. **CONFIRMED.** Claim (residue): stdout's `PROVENANCE:` line "prints the adapter record and the stamp only; the pod
    id is in the checkpoint file's provenance entry (gcal.py:1142)". gcal.py:1142 sets `entry["pod_id"]`, and
    :1144–1145 prints only `{"record","stamp"}`. The PROVENANCE lines at raw :38, :183 and :328 carry no pod_id.
23. **CONFIRMED.** Claim: the command `scripts/m_sessions.py gcal completability --unit OLMo-{ckpt} --proposal-file
    PROPOSAL-m-gating-campaign-v1_11.md`. It matches the INVOCATION lines at raw :33, :178 and :323.
24. **CONFIRMED.** Claim: "back to back through a wrapper". The wrapper (raw :467–490, sha256 `525e60d3…` verified)
    loops over sft, dpo and instruct, and each launch stamp equals the previous end stamp.
25. **CONFIRMED.** Claim: "on box HEAD 1bf94a6". The DRIVER lines say "committed at HEAD 1bf94a6…, working tree
    identical" (raw :34, :179, :324), and each artifact's `gate.head` matches.
26. **CONFIRMED.** Claim: "DRIVER f0e9d5c4…8403". The sha256 of `scripts/m_sessions.py` at 1bf94a6 (and in the tree)
    is `f0e9d5c497a1…5ea218403`.
27. **CONFIRMED.** Claim: "02:20:02Z → 02:35:53Z". The verbatim stamps.txt (raw :24, :30) gives these. They bracket
    the driver's own PROVENANCE stamps: 02:23:37Z, 02:28:38Z, 02:34:11Z.
28. **CONFIRMED.** Clean 62/64, 61/64, 59/64, recomputed.
29. **CONFIRMED.** Corrupted 42/64 = 21/32, 44/64 = 11/16, 42/64 = 21/32, recomputed.
30. **CONFIRMED.** "≥ 7/10: no" ×3 (exact Fractions).
31. **CONFIRMED.** "≥ 3/4 × clean: no (93/128), no (183/256), no (177/256)". The bars are 3/4 × 31/32, 3/4 × 61/64 and
    3/4 × 59/64, and corrupted falls below each.
32. **CONFIRMED.** Covariates +5/16, +17/64, +17/64 (0.3125, 0.265625), recomputed as clean − corrupted.
33. **CONFIRMED.** Claim: "Each identity carries backend identifier 641ee466f4553b6a". All six files carry it, and it
    was recomputed from each provenance record.
34. **CONFIRMED.** Claim: "the WEIGHTS lines are the BACKEND entry's weights of record". The revisions and
    files_aggregate_sha256 values (152782ecc41a / ecce2061…, fc84a4f69991 / c6e5e2ab…, ac0587e4a774 / 0708cef3…) equal
    `data/olmo/manifest.json`'s sft, dpo and instruct entries. That is the manifest whose 29 files BACKEND step (i)
    re-hashed. The identities' `weights_*` fields match too.
35. **CONFIRMED.** Claim: the artifacts' sha256s are "in the raw". Raw :15–20 equal shasum of the six working-tree
    files. Note: "committed here" is prospective; the files are untracked now.
36. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "byte-identical to the box's". The source is raw :14. The author's scratch
    `gcal_box_sha.txt` corroborates it: the box hashes equal the local ones.
37. **CONFIRMED.** Claim: the chain rule is to continue on PASS or a verdict FAIL and halt on a refusal or a STOP.
    The wrapper code (raw :484–488) continues on rc 0, or on rc 4 with the NOT-RUN line and no `^STOP:` line, and halts
    otherwise. "declared before launch" is header-only (raw :9).
38. **CONFIRMED.** Claim: each run ended in a verdict FAIL (exit 4, the NOT-RUN line, no STOP line). The stamps show
    exit=4 three times, each log has its NOT-RUN line, and no raw line starts with "STOP:".
39. **CONFIRMED.** Claim: the tallies are "count-only, no bar, no effect on condition (4); gcal.py:1042–1060".
    Sources: gcal.py:1044–1045, and R1 A6 at RESULTS.md@9cbacdb:4104–4114 ("count-only, with no bar and no effect on
    condition (4)").
40. **CONFIRMED.** Tally (iii): 0 / 0 / 0, recomputed with f's termination patterns.
41. **CONFIRMED.** Tally (iv): 12 (9), 6 (4), 9 (5), recomputed with `corrupted_words` and `mirrors` re-implemented.
42. **IMPRECISE.** Claim: column "(i) hits on items 7, 9: state the answer: 9 of 12 / 8 of 12 / 7 of 9". The counts
    are right; my own read of the 33 texts agrees (9, 8, 7). But R1 A6 defines tally (i) as hits "whose text does not
    state the answer" (RESULTS.md@9cbacdb:4108). A table titled "R1 A6's tallies" therefore shows the complement. The
    declared tally is 3 / 4 / 2.
43. **CONFIRMED.** Tally (ii), "close": 0 of 2 / 0 of 3 / 0 of 3. The candidates were recounted, and none of the 8
    texts is "close".
44. **CONFIRMED.** Claim: "Code read all 384 generations (… every text in its section 5)". Section 5 has 384 generation
    lines in 96 item blocks, and every one matches its record.
45. **CONFIRMED.** Claim: every (i) candidate read as not stating the answer is a corrupted-pool hit on item 7 or 9.
    All 9 of them (3 + 4 + 2) are CORR_corrupted.
46. **IMPRECISE.** Claim: ": the feathers called heavier, or "90 * 45 = 4050"". This reads as exhaustive, but it misses
    sft corrupted 7 s3 ("…a kilogram of iron is 1 kilogram. The weight of a kilogram of feathers is 1 kilogram.": no
    comparison; read raw :15). Also, "90 * 45 = 4050" is the text of dpo corrupted 9 s3 only; sft corrupted 9 s1 reads
    "90 miyms 45. = 4050". The nine break down as 6 feathers-heavier, 2 multiplications and 1 no-comparison.
47. **CONFIRMED.** Claim: none of the eight item-15 misses is "close"; they are banner or scaffold text, or
    "Regenerate.". The eight texts are '=== Actual module name ===', 'Regenerate.' ×3, "---\n\nTask: Write the opposite
    of 'enter" / "…'help", '=== Config evaluation session ===' and '### Response:'.
48. **CONFIRMED.** Claim: "By R1 A6's terms neither read moves condition (4)". R1 A6 says "no effect on condition (4)".
49. **CONFIRMED.** Claim: the seat's ruling of 2026-10-10, "a re-grading after the data is rule 11's post hoc by
    definition". Exact at `results/raw/2026-10-10_m-design-to-code_pre-LOCK-v0.1.md`:19.
50. **CONFIRMED.** Claim: "Seven observations … (the read raw's §4)". O1–O7 are at read raw :53–59.
51. **IMPRECISE.** Claim: "(item 2 at 0/12, item 9 at 2/12, both artifacts)". The counts were recomputed (item 2:
    0 + 0 + 0; item 9: 1 + 1 + 0). But "both artifacts" reads as covering both items. Per O1, the artifacts are item 9's
    two graded hits (the operand "45" restated after a multiplication); item 2's 0/12 are plain misses.
52. **CONFIRMED.** Claim: "clean-pool hits on a "correction"; harness-shaped text; the configuration-topic reading".
    These are O2–O4, spot-checked in the records: dpo clean 2 s3 "September.  (Incorrect; the correct answer is
    March"; '[PROLOGUE' ×3; dpo and instruct corrupted 14 s3 "…configuration…".
53. **CONFIRMED.** Claim: "two embedded double newlines before the stop and one control character". dpo and instruct
    corrupted 15 s0 contain "\n\n" with stop_reason newline. instruct corrupted 7 s1 starts with U+007F (DEL) and ends
    at the cap. No other text of the 384 has a newline or control character.
54. **CONFIRMED.** Claim: identical texts on the same keys, dpo / instruct 95 of 128. Recomputed: 95 (sft/dpo 66,
    sft/instruct 61).
55. **CONFIRMED.** Claim: "cap hits". O7's 2/4, 1/8 and 0/9 were recomputed.
56. **CONFIRMED.** Claim: "m:176 and m:302 make a failing checkpoint NOT-RUN with reason "dose not completable"". See
    item 1.
57. **CONFIRMED.** Claim: the docstring adds "never 'STOP and re-specify'". gcal.py:55–56 reads 'FAIL -> that
    checkpoint NOT-RUN, "dose not completable", never "STOP and re-specify"'; the inner quotes are normalised.
58. **CONFIRMED.** Claim: "The covariates are recorded as the runs printed them". The driver's covariate lines equal
    the artifacts' `covariate` fields.
59. **CONFIRMED.** Claim: "No LOCK-m-OLMo-{ckpt} is written (C1's hold …)". No LOCK-m-OLMo* file exists in the tree or
    the index. C1 (answers:38): "The first LOCK-m-OLMo-{ckpt} v0.1 is written after G-ANL-F3's commit". "No next node"
    is consistent with m:302 and §5.
60. **CONFIRMED.** Claim: "Nothing is pushed". True of this entry's commit. Origin main is 273ca8f (ls-remote), so
    b9a26ef and 54bbfe5 are unpushed too. But 190ba90, 958e762 and 273ca8f are on origin; see observation 1.
61. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "The box repo holds the six files untracked, byte-identical to those
    committed here". The only support is scratch `gcal_box_sha.txt`: box HEAD 1bf94a6, six "??" lines, sha256s equal to
    the local files. There is no committed record.
62. **CONFIRMED.** Claim: "The pod is RUNNING at $1.79/hr, kept up per C3". Live get-pod: status RUNNING, cost 1.79,
    no restart since creation (startedAt = createdAt). C3 is at answers:43.
63. **NOT CHECKABLE.** Claim: "G-ACQ (PROPOSAL-n) runs on the box in parallel … (/workspace/staging-n); its GPU pieces
    were to wait for this stop". This is box- or chat-side. Only the PI's G-ACQ choice "Now, in parallel" is on record
    (RESULTS.md@54bbfe5:243).
64. **CONFIRMED.** Claim: the BACKEND entry (190ba90) and the smoke entry (b9a26ef) were committed without a
    values-check. 190ba90 holds RESULTS.md and the two respawn raws; b9a26ef holds RESULTS.md and the two smoke raws.
    Neither has a values-check raw, while 958e762 and 1bf94a6 each carry one.
65. **CONFIRMED.** Quote: "Values-check pre-commit as the record does". Exact at m:363.

## B. The BACKEND entry (190ba90)

66. **CONFIRMED.** Claim: "(PROPOSAL-m v1.11 m:251, m:302; ADDENDUM-m1 §4 step 4, the OLMo track's first node)". m:251
    says each new box runs the respawn protocol and gets its own BACKEND entry. m:302 and ADDENDUM-m1:59 make it the
    first node.
67. **NOT CHECKABLE.** The PI's go, "Go when in stock", then "Yes, watch": chat-only. It is repeated only in the
    author's scratch `procedure.md`.
68. **CONFIRMED.** Claim: "the respawn protocol on the new box, pod qny1x4v8padeke". Sources: the raws and the live
    get-pod read.
69. **CONFIRMED.** Claim: "(i) INTEGRITY PASS, 29/29 files". Box output: "INTEGRITY PASS — 29 files match the manifest
    across 4 checkpoints". The 29 ok lines (base 7, sft 7, dpo 7, instruct 8) are the manifest's 29 files.
70. **CONFIRMED.** Claim: "(ii) BACKEND PASS: A, B and C are all exact at 0.0". Box output: every probe exact=True with
    max|d| 0 and symKL 0, and the SUMMARY line.
71. **CONFIRMED.** Claim: "the new artifact is byte-identical to the committed one". The laptop-check lines give both
    sha256 as `61f160ea…5434` at 2819 bytes. The author's scratch copy of the box file has the same hash.
72. **CONFIRMED.** Claim: "Backend identifier 641ee466f4553b6a", recomputed.
73. **NOT CHECKABLE.** Stamp "Sat Nov  7 00:36:43 UTC 2026": a write-time stamp. It is consistent with the record: it
    falls after the run's end (00:33:38Z) and before the commit (00:37:39Z).
74. **CONFIRMED.** Claim: "Pod qny1x4v8padeke, named jspace-olmo-m". Live get-pod name.
75. **CONFIRMED.** Claim: "made by the RunPod MCP's create-pod at 2026-11-07T00:17:14Z". Live createdAt is
    2026-11-07T00:17:14.85Z. That the RunPod MCP's create-pod made it is recorded only in scratch `watch.log`.
76. **CONFIRMED.** Claim: "on the spec of record". RESULTS.md:17234–17237 at HEAD: "Pod specs live in HANDOFF §2
    (US-CA-2, A100-SXM4-80GB, volume o73qvy742n at /workspace, image runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404,
    TCP 22)". The live pod matches every field.
77. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: the watch read about every 20 minutes, and its 20th read was the first to
    list US-CA-2, at price.secure $1.79/hr. Scratch `watch.log`: ticks about 21 min apart; ticks 1–19 "US-CA-2 absent";
    tick 20 "US-CA-2 LISTED"; price.secure 1.79. The price matches the live cost of 1.79. C3's "twenty reads"
    (answers:43) derives from this entry, so it is not independent.
78. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "list-pods before the create showed no jspace-olmo-m; the old pod
    uimuzt7d890y5b (EXITED) was not touched". The source is `watch.log` tick 20. It is consistent with the live read:
    uimuzt7d890y5b is EXITED, last started 2026-08-25.
79. **CONFIRMED.** Claim: "Image runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404; 1 × NVIDIA A100-SXM4-80GB; data
    center US-CA-2; network volume o73qvy742n at /workspace". Live get-pod: image, gpu count 1 and id, dataCenterId,
    mounts.network.
80. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "(81,920 MiB, driver 595.91.07, driver CUDA 13.2)". The source is
    determinism raw:2. Driver CUDA 13.2 also matches the live cudaVersion.
81. **CONFIRMED.** Claim: "466 G". Live get-network-volume gives size 500 GB = 465.7 GiB, which is df's "466G".
    CLAUDE.md:98–99 says "Persistent volume 466 GB".
82. **NOT CHECKABLE.** Claim: "242 G used". Box-only; there is no raw or capture.
83. **CONFIRMED.** Claim: "container disk 30 GB; port 22/tcp only". Live get-pod: disk 30, ports ["22/tcp"].
84. **NOT CHECKABLE.** Claim: "The env.sh hook was missing from ~/.bashrc and is restored". Box-only.
85. **IMPRECISE.** Claim: "box_respawn_check.py re-hashed every file under /workspace/models/ against the committed
    manifest". The script hashes each manifest file in the four checkpoint directories and flags unlisted entries in
    those directories. Files directly under /workspace/models/ are outside its scope, for example the
    determinism_base.json that step (ii) rewrites. The wording is that of CLAUDE.md's protocol and the 2026-08-23
    entry.
86. **CONFIRMED.** Claim: "29 files match across base / sft / dpo / instruct, both directions, exit 0". Box output.
    The script runs MISSING and EXTRA checks ("Checks in both directions") and returns 0 only on PASS.
87. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "(00:23:05Z → 00:29:55Z)". The source is integrity raw:6. The author's
    scratch `.launch` and `.exit` copies corroborate it.
88. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "run only after (i) passed (box_determinism.py --stage base --repeats 5,
    env.sh sourced, exit 0, 00:30:14Z → 00:33:38Z)". Sources: determinism raw:1 and :4–7, corroborated by scratch.
    That env.sh was sourced is consistent with the printed `cublas_workspace_config` ":4096:8".
89. **CONFIRMED.** Table row A: "exact, max|d| 0.000e+00, symKL 0".
90. **CONFIRMED.** Table row B: "repeat-exact, and identical to ON (max|d| 0.000e+00, symKL 0)".
91. **CONFIRMED.** Table row C: "exact, worst symKL 0.000e+00 vs the 1e-3 bar".
92. **CONFIRMED.** Claim: "108 leaf fields each, 0 differences, byte-identical (sha256 61f160ea…5434)". The committed
    file was recounted at 108 leaves, its sha256 was recomputed, and the laptop-check lines agree.
93. **CONFIRMED.** Claim: "As on 2026-08-23, the committed artifact is left as it stands". RESULTS.md:14998–14999: "The
    committed artifact is therefore left as it stands". git log shows the file unchanged since 214fd17 (2026-08-19).
94. **CONFIRMED.** Claim: "Backend identifier (m:251)". m:251: "the backend identifier is the adapter's provenance
    record (Code's definition)".
95. **CONFIRMED.** Claim: it is `resume.backend_identifier` on the printed block, and the check is appended to the
    determinism raw. The raw's laptop-check section holds it.
96. **CONFIRMED.** Claim: "The printed block equals the committed 2026-08-19 block". The two compare equal, both give
    641ee466f4553b6a, and the block was committed at 214fd17 on 2026-08-19.
97. **CONFIRMED.** Claim: the provenance list (torch 2.8.0+cu128 … 64 layers). It matches the printed block. "CUDA 12.8
    (torch's build)" is `torch.version.cuda` (olmo_hf.py:326).
98. **CONFIRMED.** Claim: "OLMoHFAdapter(path, choice_window=8192) with the same deterministic and seed defaults
    (scripts/m_sessions.py:809)". Line 809 passes `runner_olmo.CHOICE_WINDOW`, which is 8192 (runner_olmo.py:50). The
    defaults are deterministic=True and seed=20260818 (olmo_hf.py:54–55). box_determinism.py:59 uses
    deterministic=True and the default seed.
99. **CONFIRMED.** Claim: the provenance "differs from this run's only in path, which the identifier drops".
    `BACKEND_DROP` contains path (resume.py:147). The three G-CAL provenance records later differ from the printed
    block in `path` alone.
100. **CONFIRMED.** Claim: "(the 2026-08-23 housekeeping, again)". See RESULTS.md:15006, "Box housekeeping".
101. **NOT CHECKABLE.** Claim: "The box repo was at 6dfc455 (2026-08-24)". The box's earlier HEAD is in no raw and no
     capture. The git side is consistent: 6dfc455 is dated 2026-08-24, is an ancestor of 1bf94a6 (so a fast-forward is
     possible), and tracks the four "modified" paths.
102. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "4 modified tracked files and 66 untracked files … Every one was hashed".
     Scratch `modified_list.txt` has 4, `untracked_list.txt` 66, and `box_dirty_hashes.tsv` 70 hashes.
103. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "60 are byte-identical to the laptop's HEAD 1bf94a6 at the same path".
     Recomputed from `box_dirty_hashes.tsv` against `git ls-tree -r 1bf94a6`: 60.
104. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "4 are byte-identical to that HEAD at another path". Same method: scripts/
     c1r3_gate_repA.json, c1r3_gate_repB.json and e0_frames.json match their data/configs/ copies, and
     scripts/e0_tasks.jsonl matches data/corpus/e0_tasks.jsonl.
105. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: the 4 modified files equal earlier commits of the same path (.gitignore at
     5c1b161, HANDOFF-2026-08-24.md at f4b402a, RESULTS.md at c17337c, paper_analysis.ipynb at 947b9ea). For each,
     `git rev-parse <commit>:<path>` equals the box hash in scratch (eeda99f4…, f53e7f17…, de8d72ce…, 54afce55…).
106. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: the 2 ADDENDUM-g3-b2r files "were never committed and are byte-identical to
     the laptop's own untracked copies". `git log --all` on both paths is empty, and `git hash-object` of the laptop
     copies (880c1e74…, f153d073…) equals the scratch box hashes.
107. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "So nothing box-only existed". 60 + 4 + 4 + 2 = 70, all accounted for.
108. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "The one gitignored file the merge would overwrite,
     data/olmo/b2r_concepts_base.npz". Of the 25 ignored paths in scratch `box_ignored.txt`, only this one is tracked
     at 1bf94a6 (blob b774fe25…). 6dfc455's .gitignore ignores /data/olmo/* except *.json.
109. **NOT CHECKABLE.** Claim: the .npz "is byte-identical to HEAD's". No box hash of it is recorded, in a raw or in
     scratch.
110. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: nothing was deleted; 66 files were moved and 4 copied, all 70 hashes were
     re-checked, and the 4 were restored. Scratch `holding_out.txt` has "copied modified: 4" and "moved untracked: 66",
     with empty porcelain after the restore. The 70 hashes in `holding_hashes.tsv` equal those in
     `box_dirty_hashes.tsv`.
111. **CONFIRMED-BY-SCRATCH-ONLY.** Claim: "a full-history git bundle (279 MB, main at 1bf94a6)". Scratch
     `jspace.bundle` is a v2 bundle with no prerequisites and refs/heads/main at 1bf94a6. Its size is 279,474,757
     bytes (279.5 MB, or 266.5 MiB).
112. **CONFIRMED.** Claim: "box HEAD = laptop HEAD at ship time = 1bf94a6". The box's own output shows HEAD 1bf94a6:
     the smoke's "SMOKE start …; HEAD 1bf94a6…" and the G-CAL DRIVER lines. The laptop's HEAD was 1bf94a6 from
     18:59:07 to 19:35:45 -0500, and the bundle was written at 19:17. "working tree clean" is header-only (integrity
     raw:3).
113. **CONFIRMED.** Claim: the laptop "has since moved to 958e762, which changes only RESULTS.md and two raws".
     `git show --stat 958e762`: RESULTS.md, the code-to-design prebuild raw and the prebuild values-check raw. 958e762
     is 190ba90's parent.
114. **CONFIRMED.** Claim: "RUNPOD_POD_ID is unset in a non-interactive ssh shell". The smoke's box output says
     "inherited by this process: None" (smoke raw:10).
115. **CONFIRMED.** Quote: "verify on the box before the first OLMo stage", at resume.py:256–257. Exact.
116. **CONFIRMED.** Quote: "Every OLMo stage requires the pod id at its start". Exact at resume.py:28–29, the module
     docstring.
117. **CONFIRMED.** Claim: the variable is set in the container's PID-1 environment. The smoke's box output reads "in
     PID 1's environment: 'qny1x4v8padeke'".
118. **CONFIRMED.** Claim: "/workspace/env.sh does not export it". Indirect: the smoke's box output under env.sh shows
     it inherited as None, and C4 later appended the export. The file itself is box-side.
119. **CONFIRMED.** Quote: "Both PASS before anything runs". Exact at CLAUDE.md:127.
120. **CONFIRMED.** Claim: the consistency clause, "a campaign completes on this one backend, and a box change aborts
     and restarts it". See CLAUDE.md:127–130.
121. **CONFIRMED.** Claim: "The next node is G-CAL-OLMo-{ckpt} (m:302); it waits for the PI's word, with a smoke
     first". m:302. Answers:36 and §D item 1 call this "the BACKEND entry's standing line".
122. **CONFIRMED.** Claim: "No lock is written and nothing is pushed". True at write time: no LOCK-m-OLMo* existed, and
     origin/main stayed at 9cbacdb until the push at 2026-11-07T01:31:08Z. 190ba90 itself reached origin later; see
     observation 1.
123. **CONFIRMED.** Claim: "The pod is RUNNING at $1.79/hr and bills while it waits". Live get-pod: RUNNING, cost 1.79,
     no restart since 00:17:14Z.

## C. The smoke entry (b9a26ef)

124. **NOT CHECKABLE.** The PI's word "Yes, smoke": chat-only.
125. **CONFIRMED.** Claim: "no G-CAL item, key, seed or grader ran". The smoke script (its appended source hashes to
     `179ab066…`) uses 4 tasks, none among the 32 tasks G-CAL served. Its seeds are
     `crc32("m-smoke|{ck}|{t}|{s}") % 2**31`, and it never calls a grader.
126. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "nothing was written under data/". The source is smoke raw:2–3 ("working
     tree clean before and after"). By code reading, the script only prints.
127. **CONFIRMED.** Claim: "each loads, passes G-CAL-OLMo's startup, gives backend identifier 641ee466f4553b6a". Box
     output per unit; the identifier was recomputed from the printed provenance.
128. **CONFIRMED.** Claim: it "generates through G-CAL-OLMo's own call". The script calls `adapter.generate(SESSION_BANNER,
     seg, injections=(), seed, temp=OLMO_TEMP, max_tokens=STOP_CAP, ban_ids, cached=False)`. That is gcal.py:1164–1165's
     call with the same arguments. See item 139 on "loop body".
129. **CONFIRMED.** Claim: "launched from ssh, the real precheck refuses "POD ID ABSENT", its only problem, and passes
     with PID 1's RUNPOD_POD_ID". Box output: one-item refusal lists ×3 and PASS ×3.
130. **CONFIRMED.** Claim: "the m self-test on the box is 844/846, both FAILs on laptop-site assumptions". Box output
     reads "844/846 m selftest checks pass", with two [FAIL] lines (selftest raw :779, :836). The attribution to
     laptop-site assumptions is Code's reading.
131. **NOT CHECKABLE.** Stamp "Sat Nov  7 02:10:11 UTC 2026": a write-time stamp. It is consistent: b9a26ef was
     committed at 02:10:57Z.
132. **CONFIRMED.** Claim: "The record defines no G-CAL smoke: the Qwen G-CAL's completability run (2026-10-08) was its
     run of record". PROPOSAL-m defines no G-CAL smoke, and the G-CAL entry is dated 2026-10-08 (RESULTS.md:5500;
     commit cf8eb5b).
133. **IMPRECISE.** Claim: "The driver also refuses a real-model --out ("the box run writes data/m/gates and data/m/ckpt
     only")". The refusal is real (m_sessions.py:483–487). But the message reads "the box run (G-CAL-OLMo-{ckpt}) writes
     data/m/gates and data/m/ckpt only (nothing loaded)". The quote drops the stage label in parentheses without marking
     the cut.
134. **CONFIRMED.** Claim: the smoke runs the committed path's "own pieces, up to and not including its 128 keyed
     generations, from a script outside the repo (its source and sha256 are in the raw)". The script ran from
     /workspace/smoke/, and its appended source hashes to the declared `179ab066…`.
135. **IMPRECISE.** Claim, step 1: "Per unit: … gcal.precheck(…) …, then again with the value from PID 1's environment;
     olmo_weights_problems; driver_problems". The two prechecks and olmo_weights_problems ran per unit, but
     driver_problems ran once, before the unit loop: `main()` prints a single "driver_problems: []" line (smoke raw:11).
     The table row "weights and driver checks: clean | clean | clean" repeats that one shared check in each column.
136. **CONFIRMED.** Step 2, "the load through the driver's _load_olmo": the script calls `ms._load_olmo(ck, w["path"])`.
137. **CONFIRMED.** Step 3, `_startup_olmo`: insulation; olmo_startup's base and cross-checkpoint refusal; the 8192
     window; b3's ban list against the scaffold file; TEMP 0.7 and STOP_CAP 60; the weights path; the tokenizer probe.
     All are at gcal.py:866–890.
138. **CONFIRMED.** Step 4, "adapter.provenance() and resume.backend_identifier on it".
139. **IMPRECISE.** Claim, step 5: "8 generations through G-CAL-OLMo's own loop body (valence_core/m/gcal.py:1152–1165:
     …)". The script does not run gcal.py:1152–1165. It re-implements that body's three calls, with identical
     arguments, in its own loop: `guard.assert_insulated`, `sc.assert_boundary` and `adapter.generate`. Its own docstring
     says "G-CAL-OLMo's own call (gcal.py:1155-1165)". gcal's SystemExit → GcalStop handling, grading and record append
     are not exercised. The call as quoted does match gcal.py:1164–1165.
140. **CONFIRMED.** Claim: "4 neutral tasks (scripts/box_determinism.py's probes, none of them a G-CAL item) × 2 seeds
     keyed m-smoke|{ckpt}|{t}|{s}". These are box_determinism.py's first four PROBES of five; the fifth carries a banner
     and a round header. None is among the 32 G-CAL tasks.
141. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "Then the m self-test, model-free, on the box, in the same background
     job". Sources: smoke raw:5 (COMMAND) and selftest raw:1–3.
142. **CONFIRMED.** Claim: "smoke exit 0, 01:31:47Z → 01:41:53Z". Box output has the SMOKE start and end lines. Exit 0
     follows from "units failed to start or load: 0", since the script returns 0 only then. The exit file itself is
     header-only.
143. **CONFIRMED.** Claim: the box repo is at 1bf94a6, "whose m code is the laptop's: the only code change since is
     scripts/audit_note_N12_history.py". Outside RESULTS.md and results/raw/, `git diff 1bf94a6..273ca8f` touches only
     that file. valence_core/m/ and scripts/m_sessions.py are unchanged through HEAD.
144. **CONFIRMED.** The results table matches what the box printed:
     - prechecks: REFUSED with POD ID ABSENT only, then PASS ×3;
     - load 211.6 / 175.7 / 183.3 s;
     - `_startup_olmo` PASS with 9 ban ids ×3;
     - backend identifier ×3;
     - 8 generations: 9.6 / 1.20 / 5.39, 10.0 / 1.26 / 3.56, 10.3 / 1.29 / 4.41;
     - CUDA peak 60.1 ×3 (sft's post-load line reads 60.0; its end-of-unit peak is 60.1).

     The driver half of the "weights and driver checks" row is item 135.
145. **CONFIRMED.** Claim: the identifier is now measured through m's own loader, and the BACKEND entry gave it by code
     reading. Smoke box output; the BACKEND entry says "By code reading, not measured".
146. **CONFIRMED.** Claim: "Code read all 24 generations … 23 stop at the newline. 1 hits the 60-token cap (sft, task
     0, seed 0 …)". The 23 newline stops and 1 cap stop were recounted. The quote "The user is asking for a color that
     represents the sea" is exact.
147. **CONFIRMED.** Claim: sft once answers `{ "answer": "blue"`. sft t=0 s=1, exact.
148. **CONFIRMED.** Claim: "one load (about 3–3.5 min) plus 128 generations at about 1.2–1.3 s each". Loads took
     2.93–3.53 min and the generation means were 1.20–1.29 s. The entry labels this "not a projection of record"; the
     runs of record later took about 0.76–0.93 s per generation.
149. **CONFIRMED.** Claim, finding 1: "every OLMo unit's precheck refuses with "POD ID ABSENT: … ($RUNPOD_POD_ID)" and
     nothing else; with PID 1's value it passes". Box output; the elided quote matches the precheck message.
150. **CONFIRMED.** Finding 2: "844/846". Box output.
151. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "(exit 1; 01:41:54Z → 02:07:28Z". The source is selftest raw:3,
     corroborated by the author's scratch exit and launch copies.
152. **CONFIRMED.** Claim: "about 25.5 min against the laptop's 5 min 15 s". The box run took 1,534 s = 25 min 34 s
     (25.6 min). The laptop's figure is "5:15.42 total" (`results/raw/2026-11-06_m-olmo-build_selftest.txt`:850).
153. **CONFIRMED.** Claim: "`qwen_snapshot's production defaults …` (scripts/m_sessions.py:4158) compares
     MLX_LM_ALLOW_PATTERNS with the list parsed from mlx_lm's own source". The chk is at 4158, the parse at 4144–4153
     and the comparison at 4166.
154. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "mlx_lm is not installed on the box (find_spec("mlx_lm") returns None), so
     the parsed list is empty". Selftest raw:3 says "mlx_lm's source is absent on the box". The find_spec value is in
     no raw, and the printed detail (selftest raw:779) is cut off before the parsed list. By code reading, no spec gives
     an empty list and the check FAILs.
155. **IMPRECISE.** Claim: "`gcal completability --unit OLMo-sft …` (scripts/m_sessions.py:6923–6929) forces the pod id
     absent and expects … "POD ID ABSENT" and "weights:"". The expectation is in the cited range (at 6928). But the
     forcing (`with env_pod(None)`) and the box-path call are at 6919–6922, and that call runs unit OLMo-instruct, not
     OLMo-sft. Instruct's weights are present too, so the substance holds.
156. **CONFIRMED.** Claim: "On the box the weights are present (olmo_weights_problems: [] above)". The smoke shows
     olmo_weights_problems: [] for all three checkpoints.
157. **CONFIRMED.** Claim: the check's printed detail shows its stub half as expected (exit 4, the NOT-RUN line).
     Selftest raw:836: "(4, '…completability: FAIL -- that checkpoint NOT-RUN…".
158. **CONFIRMED.** Quote: "neither FAIL for the clone's absence nor disappear", gcal.py:108–112. Exact, at :111–112.
159. **CONFIRMED.** Claim: "Neither is G-CAL-OLMo's own path … these two have no such provision". Neither check
     (m_sessions.py:4141–4167, 6919–6929) branches on the site. One is a Qwen-loader check; the other tests the driver's
     refusal.
160. **CONFIRMED.** Claim: "The self-test of record stays the laptop's 846/846". The m-olmo-build selftest raw:1 has
     "Tally: '846/846 m selftest checks pass'".
161. **CONFIRMED.** Claim: "scripts/m_sessions.py, a TOOLING_FILES entry". See valence_core/m/gshape.py:105.
162. **CONFIRMED-BY-RAW-HEADER-ONLY.** Claim: "The box repo is clean at 1bf94a6, with nothing for OLMo under data/m/gates
     or data/m/ckpt". The sources are the smoke raw:3 and selftest raw:1 headers.
163. **CONFIRMED.** Claim: "nothing is loaded on the GPU". The script deletes each adapter and exits, and the self-test
     is model-free.
164. **CONFIRMED.** Claim: "No G-CAL-OLMo run, no lock, nothing pushed". No G-CAL-OLMo output exists before 02:20Z
     (stamps), and there is no LOCK-m-OLMo*. b9a26ef is not on origin (origin main is 273ca8f). Note, though, that
     origin/main moved during the smoke window: 1bf94a6 was pushed at 2026-11-07T01:31:08Z, then 273ca8f, carrying
     958e762 and 190ba90, at 01:39:16Z (local reflog, "update by push").
165. **CONFIRMED.** Claim: "The pod is RUNNING at $1.79/hr and bills while it waits". Live get-pod.

---

## Observations outside the three texts (not graded)

1. **190ba90 is already on the public origin.** `git ls-remote origin refs/heads/main` returns `273ca8f`. The local
   reflog of `refs/remotes/origin/main` shows "update by push" at 2026-11-06 20:31:08 -0500 (1bf94a6) and 20:39:16
   -0500 (273ca8f). So 958e762, 190ba90 (the BACKEND entry checked here) and 273ca8f are on origin. Yet 273ca8f's own
   commit message says: "The approved push covers 9cbacdb..1bf94a6; this commit, 958e762 and 190ba90 are not in it".
   This bears on the draft's "Two gaps disclosed": the BACKEND entry is already public, so any correction to it would
   be a new commit, not an amend.
2. **Twelve claims rest on uncommitted scratch.** Item 61 and items 77–78 and 102–111 rest only on the author's
   uncommitted captures in `<scratch>/`. If the record should carry that evidence, the captures would need to be
   committed: `box_dirty_hashes.tsv`, `holding_out.txt`, `holding_hashes.tsv`, `box_ignored.txt`, `watch.log`,
   `gcal_box_sha.txt`. Scratch files are cleaned after about four days.
3. **The smoke's budget line overstated per-generation time.** Item 148's estimate was 1.2–1.3 s per generation. In the
   runs of record, launch to PROVENANCE stamp took 204–215 s, then 128 generations took 97–119 s (about 0.76–0.93 s
   each); each run lasted 5 min 12 s to 5 min 23 s. This is not a values error, since C labels the line "not a
   projection of record".
4. **Footprint of this check.** No repository file was touched. The RunPod calls were reads only: the runpod-mcp guide,
   get-pod ×2 and get-network-volume. `git ls-remote` is also a read. One temporary listing,
   `<scratch>/vc_tree_1bf94a6.txt`, was created outside the repo for item 103 and then removed.

---

## Code's dispositions (2026-11-06)

- **42 (A), applied.** The tallies table states (i) in R1 A6's own terms (RESULTS.md@9cbacdb:4108: hits on items 7 and 9 "whose text does not state the answer, by Code's read"): 3 / 4 / 2, with the candidate counts beside. (ii) is stated as R1 A6 defines it ("close" answers on item 15): 0 / 0 / 0, checked by tool (read raw §6).
- **46 (A), applied.** The nine (i) hits are listed in full: 6 call the feathers heavier, 1 gives both as 1 kilogram (sft 7 s3), 2 multiply and restate the operand (sft "90 miyms 45. = 4050"; dpo "90 * 45 = 4050").
- **51 (A), applied.** "item 2 at 0/12; item 9 at 2/12, both of its hits artifacts".
- **85 (B), corrected in the G-CAL-OLMo entry** (190ba90 is public and cannot be amended): step (i)'s scope is the manifest's files in the four checkpoint folders plus unlisted entries there; top-level files under /workspace/models/ are not hashed.
- **133, 135, 139, 155 (C), corrected in the G-CAL-OLMo entry** (b9a26ef has another session's commit on top and is not rewritten): the refusal's quote with its label (m_sessions.py:484-486); driver_problems ran once, before the loop; the smoke re-implemented gcal.py:1152-1165's three calls with the same arguments, and gcal.py's lines did not execute; the box-path call is at m_sessions.py:6919-6922 and runs OLMo-instruct.
- **The 12 CONFIRMED-BY-SCRATCH-ONLY items (61, 77-78, 102-108, 110-111): put on the record** in results/raw/2026-11-06_backend_box-captures.txt (the stock-watch log, the 70 box files' hashes and classification, the holding folder's re-check, the bundle's identity, the box's hashes of the six G-CAL files).
- **The 10 NOT CHECKABLE items: acknowledged.** They are chat-only words (the PI's "Go when in stock", "Yes, watch", "Yes, smoke"), write-time stamps, and box facts never captured (242 G used at 00:20Z, the restored ~/.bashrc hook, the box's prior HEAD 6dfc455, the .npz's pre-merge hash). No new capture can reach the past state; they stand as Code's statements.
- **The two findings outside the texts.** (1) 190ba90 is public via the second push (273ca8f, 20:39:16 -0500), beyond the range 273ca8f's own message calls approved: flagged in the G-CAL-OLMo entry and to the routing session, not adjudicated. (2) The scratch-only evidence: as above.
