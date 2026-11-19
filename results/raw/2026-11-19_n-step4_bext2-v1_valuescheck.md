# n step 4 — backend-ext-2's entry: the blind values-check, as returned, with every disposition

PI date 2026-11-19. Code (the n-build session).

**What was checked.** One blind pass by a subagent over two drafts:
- T1, the entry (`RESULTS.md`, the Log's head), sha256 `a25b52b0…f2e3`;
- T2, six lines for `.gitignore`, to follow the first stage's report line, `4023bc50…7d5c`.

**The checker's brief** (`4005849a…6db3`, 81 lines):
- named the sources:
  - the seat's answers of the fourth sitting, the conditional ruling raw, ADDENDUM-n2 at root, and v4's committed
    output;
  - `RESULTS.md`'s entries of `6e3474d` and `732a58f`, `.gitignore` and `.gitattributes`, HEAD's driver, and git
    history;
  - in Code's scratch, by name only: the seven copied-back files and the four launch files, read in full, and the
    report and the cell by `shasum` only;
  - the coordinating session's words and the pod session's, which are in no file, quoted verbatim;
- quoted the list of record v2's items 1–5, verbatim; required item 3's pathspec and the `data/mf3` exclusion on every
  git command over the tree, that a glob is expanded and read before it is looped over, and the `rev-parse` form for a
  tracked-and-clean check;
- barred any interpreter, any write, any network and any guard marker in an argv; anything under `data/mf3`; any
  content read of a ckpt or reports file; and, in Code's scratch, anything but the named files.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (150 lines, sha256
`057069f0…9430`). It names no local path.

**Totals:** 84 items — 78 CONFIRMED, 1 IMPRECISE, 0 FAIL, 5 NOT CHECKABLE — and 16 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

- **Item 75** (IMPRECISE; the `.gitignore`'s description in "Committed by path"): applied, in the form the changed text
  (§2) needs: a sentence added to the first stage's comment, and four rules that admit exactly the second stage's report
  and its one cell's JSON, one of them ignoring the rest of that stage's root.
- **The NOT CHECKABLE items** (23, 66, 73, 74, 79) stand: the report's one read, Code's own acts, and commit-time facts.
- **The observations:**
  1. Applied: the pod session proposed the new names, and the coordinating session accepted them.
  2. Applied: "The box at the end", from the pod session's record, with the box and the pod waiting for the PI's word.
  3. Applied: "Code's one read of the report on the laptop, after it came back by hash".
  4. Applied: "the script's step 4 (the hashes)".
  5. Applied: the environment pinned (python, torch, transformers, tokenizers, the cuBLAS setting), and the backend's
     identifier the one v4's resume printed.
  6. Applied: the model's one load.
  7. Applied: the script's non-bare `git status` as Code's departure (the seat's §7 class), and the pod session's
     record stating none of its own.
  8. Applied: the entry before the follow-up is the coordinating session's order.
  9. Applied: the PI's routing in the header.
  10. Applied: **Next** last.
  11. Applied: "ADDENDUM-n2 §4.1 and §4.2".
  12. Applied: why the box runs 11 checks more.
  13. Applied: the run's heading names the script's output beside the pod session's record.
  14. Left: the committed raws carry their own digests.
  15. Applied: BK's 0.031 in nats.
  16. Applied: `.gitattributes` does not change.

## 2. The text changed after the check, and the edits checked by tool

- **T2 changed after the brief went out,** at the coordinating session's request: the comment above the first stage's
  lines is to be extended "by a sentence naming backend-ext-2 and its source". The two-line comment the check read is
  gone; a sentence of three comment lines now follows the first stage's comment (after `.gitignore`'s line 286). The
  four rules are the checked T2's lines 3–6, byte for byte (`cmp`). The commit's gate rebuilds `.gitignore` from HEAD
  plus the two insertions.
- **The entry's edits.** The draft the checker read was not kept, so the edits were checked by fixed-string search over
  the final entry: each disposition's new wording present, and the wording it replaced absent, 21 of 21. The entry's
  quotations are found in their sources, 7 of 7.
- **The finals:** the entry `b7e4aa52…ac25, 116 lines (spliced with the blank line that ends it)`; `.gitignore` `da3d6f39…4b1d`.

## 3. The report as returned

```text
BLIND VALUES-CHECK: T1 (entry.md) and T2 (gitignore_added.txt)

Brief verified: sha256 4005849a14bb4b437c75c66b06944d586877f248af40333c13173884efc66db3. T1 verified: a25b52b07b7d9b5fd8d20389836a2de0a28a94edc8bb386d58c4d4d59755f2e3 (85 lines). T2 verified: 4023bc50be98b667fc454b81468e9a5ca7d0a9e8c7628a188708a8e75c087d5c (6 lines). Repo HEAD is 732a58f98d2f…. Every named repository source is tracked and clean (rev-parse HEAD:<path> against hash-object).

Abbreviations used below:
- OUT = out/bext2_v1_out.txt
- REC = out/bext2_box_run.txt (the pod session's record)
- STAGE = out/run.txt
- SH = frozen/bext2_v1.sh
- RUL = the conditional ruling
- ANS = the fourth-sitting answers raw
- A2 = ADDENDUM-n2 v0.1
- V4 = 2026-11-18_n-step4_bext-resume4_out.txt
- R = RESULTS.md
- POD = the pod session's quoted words; (c1)–(c5) are the coordinating session's words.

Every hash tail below was cut by tool (first 8 … last 4).

ITEMS
1. T1:1, date 2026-11-19. CONFIRMED. REC:4 "PI date 2026-11-19".
2. T1:1, "from driver v2g's commit `732a58f`". CONFIRMED. OUT:4 has fresh copy HEAD 732a58f98d2f…. git show --name-only 732a58f: subject "driver v2g committed…", and it touches scripts/n_sessions.py.
3. T1:1-2, 24 reads under "space", the convention of record. CONFIRMED. OUT:56 and OUT:65-88; ANS §1.2 (line 17).
4. T1:2, COMPLETE with no pause, so the ruling was not used. CONFIRMED. OUT:89, 95, 96.
5. T1:3, cites ANS §2 and A2 §4.1. CONFIRMED. ANS line 23 is §2, Q2 backend-ext-2; A2 line 34 is §4.1, which defines backend-ext-2.
6. T1:4-5, the report and cell enter here, under the package and checker they ran with, before the schema follow-up. CONFIRMED. (c3); ANS §5 (line 43).
7. T1:7, bext2_v1.sh `bf1d6b77…5b83`. CONFIRMED. shasum + cut.
8. T1:7, ended "bext2 v1 COMPLETE (pass; complete)", exit 0. CONFIRMED. OUT:103 (exact substring); exit file reads "0".
9. T1:7-8, pod emw1e4embiwe9b, run by the pod session on the coordinating session's relay. CONFIRMED. OUT:64; REC:1-4.
10. T1:9, 24 read lines, every one at or below TAU. CONFIRMED. OUT:65-88; a token tally of STAGE gives 24 "<=" and 24 "TAU"; exceed_tau 0.
11. T1:9-10, quote "end COMPLETE: 24/24 reads; report backend-ext-2.json". CONFIRMED. OUT:89.
12. T1:10, report COMPLETE under "space", no pause. CONFIRMED. OUT:95.
13. T1:11, cites A2 §4.2 and ANS §2.4. CONFIRMED. ANS line 31 heads §2.4 "(ADDENDUM-n2 §4.2)"; A2 line 36. See Observation 11.
14. T1:11-12, k = 0 of 24 above TAU. CONFIRMED. OUT:90, exceed_tau 0, reads 24.
15. T1:12, largest margin discordance 0.06250051725487715 nats. CONFIRMED. OUT:90, absdiff max, digit for digit. n_sessions.py:615 defines absdiff as "|margin - fresh_margin| in nats"; also SH:35-36 and RUL item 2 (ii).
16. T1:12-13, median rel 0.0013026706058596332. CONFIRMED. OUT:90.
17. T1:13, p0 = (k+1)/(n+2) = 1/26. CONFIRMED. A2 §1.1 (line 18); ANS §4 (line 39).
18. T1:13, C = max(0.25, 2 × 0.0625005…) = 0.25, the floor binding. CONFIRMED. A2 §2.1 (line 24); 2 × 0.0625005… = 0.125001… < 0.25; the truncation is correct; ANS §8 "C's floor binds at 0.25".
19. T1:14, BK's figures: 0 of 2,400; 0.125; 0.031 at a mean scale of 11.15. CONFIRMED. ANS line 31, verbatim.
20. T1:15, report `a1499f77…734c`. CONFIRMED. OUT:99; shasum of rec/data/n/reports/backend-ext-2.json.
21. T1:15, cell `e8c5a0db…f627`. CONFIRMED. shasum of rec/data/n/ckpt/backend-ext-2/N1-V__none__0.json; equals POD.
22. T1:15, copied back by hash only. CONFIRMED. (c4); both files sit under rec/ at their repository paths, at these digests.
23. T1:15-16, the cell's sha256 equals the report's own record of it. NOT CHECKABLE (per the brief).
24. T1:17, the pod session's record, committed as a raw. CONFIRMED. REC; T1:81.
25. T1:18, launch files from n-build's scratch, relayed by the coordinating session at their hashes. CONFIRMED. REC:13, REC:24.
26. T1:19, manifest `df697f62…7c0a`, 24 lines. CONFIRMED. shasum + cut; wc -l gives 24.
27. T1:19-20, "v4's, with the driver line set to v2g's `7aefd06b…5b67`, plus BK's reduced.json, which §2.3's lines read". CONFIRMED.
    - REC:17-19 and SH:26-27 say so.
    - V4:10-32 lists v4's 23 names in the same order as manifest lines 1-23.
    - git log 1272702..732a58f (with the pathspec): of the manifest's files, only scripts/n_sessions.py changed.
    - shasum -c of the manifest at HEAD: 24/24 OK.
    - R:42-45: v2g reads reduced.json.
28. T1:20, hashes file `93783db0…7b36` (v4's bytes). CONFIRMED. The committed v4 raw ..._bext-resume4_hashes.txt has the same sha256; REC:20; R:376.
29. T1:20-21, ruling `ba9f9632…cc32`, committed at c7d0009. CONFIRMED. The frozen and repository copies hash equal; git show --name-only c7d0009 lists the file.
30. T1:21-22, /workspace/nsite/bext2-v1 and /workspace/nsite/out-bext2-v1. CONFIRMED. REC:24, REC:52-53.
31. T1:22-23, the relayed bext2 and out-bext2 already held the step-4 smoke's folders; the coordinating session accepted the new names. CONFIRMED. (c1); REC:27-29. See Observation 1.
32. T1:23, the script finds its files through its own folder. CONFIRMED. SH:64, 92, 138, 156; REC:28-29.
33. T1:24-25, the sync: 1272702..main, main at 732a58f, refs/bundles/n-site9, checkout at ad856f0. CONFIRMED. REC:31-35.
34. T1:26-28, the fresh copy: path, clone flags, origin removed, sparse patterns (exact), detached at 732a58f, clean. CONFIRMED. REC:37-40; OUT:4-5.
35. T1:28, the source copy copy-resume4-1272702 was only read. CONFIRMED. SH:6 "only read here", plus SH:96-103 and 121-131 (rev-parse, digests, cp from it); REC:44, 48-49.
36. T1:30-31, the copies and ruling held, and the "copied and compared: 33 files … (mismatches: 0)" quote. CONFIRMED. OUT:1-8; the quote is an exact substring of OUT:8.
37. T1:32, manifest 24 of 24 OK. CONFIRMED. OUT:10-33.
38. T1:32-33, "408/408 n selftest checks pass", after the two library warnings that v4's output also holds. CONFIRMED. OUT:35-37; selftest.txt:1-3; V4:34-35 has the same two warnings.
39. T1:33, hashes equal to the laptop's. CONFIRMED. OUT:54.
40. T1:34, STAGE line under "space". CONFIRMED. OUT:56.
41. T1:34, DRIVER line `7aefd06b…5b67`, "HEAD's committed bytes". CONFIRMED. OUT:58; shasum of HEAD's scripts/n_sessions.py.
42. T1:34-35, first stage's report line `dd217d78…ce79`, "COMPLETE at 24 of 24 under 'bare'". CONFIRMED. OUT:59 (cut from the printed value; exact quote).
43. T1:35-36, G-VER PASS, labels_ok 4, ids_ok 160. CONFIRMED. OUT:61.
44. T1:36-37, identifier 8264f719efd347a9, characterization 4ed3f2c70fe8afbf, load 11999 ms. CONFIRMED. OUT:64.
45. T1:37, 12 of the 24 reads at fid=0.000000. CONFIRMED. STAGE tally gives 12 (reads 1, 3, 6, 9-13, 17, 20, 22, 23).
46. T1:37-38, the end line, the distribution, the two lines, run exit 0. CONFIRMED. OUT:89-93.
47. T1:39, identity lines equal to step 4's. CONFIRMED. OUT:98; report-identity.txt, hashes.txt and the frozen hashes file all hash 93783db0…7b36.
48. T1:39-40, each print once, no in-band, comparison or convention line. CONFIRMED. OUT:100.
49. T1:40, first-stage files and the source copy's report and cell unchanged. CONFIRMED. OUT:101-102.
50. T1:41, PID 5781, end-wait on the PID alone. CONFIRMED. REC:57-58.
51. T1:42, "(fidelity values, no margin)". CONFIRMED. OUT:90 label.
52. T1:42-44, absdiff min/q1/median/q3/p90/max. CONFIRMED. OUT:90, all six digit for digit.
53. T1:44-45, rel min/q1/median/q3/max. CONFIRMED. OUT:90, all five.
54. T1:45, label median 0.0016011952745769165, max 0.04607116519749255. CONFIRMED. OUT:90.
55. T1:46, exceed_tau 0, exceed_tau4 4, 24 of 24 finite. CONFIRMED. OUT:90.
56. T1:47, "(nats; discordances, no margin)". CONFIRMED. OUT:91-92 labels.
57. T1:48, (a): 24 of 24; median 0.03125010212219692, max 0.0937508301700607. CONFIRMED. OUT:91.
58. T1:49-50, (b) S and U, each count, median and max. CONFIRMED. OUT:92.
59. T1:50-51, pooled (R8): 48 of 48; median 0.032457661606258625, max 0.11527832851047748. CONFIRMED. OUT:92.
60. T1:53, reading them is the seat's. CONFIRMED. ANS §2.3 (line 29) "the seat's".
61. T1:54-55, ruling not used; no pause; step 6 never ran. CONFIRMED. OUT has no "== 6" section; OUT:103 shows scope/conditions/resume at 9 (not run); SH:225-230.
62. T1:55-56, condition (ii) through the package's reader, never ran, read nothing. CONFIRMED. SH:35-36 and 242-258 (cells.load_cell, inside the PAUSE branch only); (c2).
63. T1:56, the raw as the record of what would have applied (its item 5). CONFIRMED. RUL line 15.
64. T1:58-59, out/ files by explicit name, sha256 equal at three points, address/port count 0. CONFIRMED. REC:106-111.
65. T1:60, report and cell later, by hash only, via the coordinating session, paths kept. CONFIRMED. (c4); REC:111-112; the rec/ paths.
66. T1:61-62, Code's read: the report's cells record equals `e8c5a0db…f627`. NOT CHECKABLE (per the brief).
67. T1:62, also the pod session's value. CONFIRMED. POD.
68. T1:63, the 31 arrays stay on the box. CONFIRMED. (c4).
69. T1:64-66, the left-on-box list; cleanup waits for the PI's word, with the earlier leftovers. CONFIRMED. REC:114-120; (c5).
70. T1:67, schema follow-up (A2 §6.3 (3)). CONFIRMED. A2 line 48.
71. T1:67, n-analyzer's pin move. CONFIRMED. A2 line 48 "the pin moving as before"; R:2909 "n-analyzer moves its pin".
72. T1:67-68, LOCK-n v0.1's draft with these figures (§4.2). CONFIRMED. A2 lines 36 and 48 (item 5); ANS line 31.
73. T1:70-72, departure 1 (git show of the committed report piped to shasum). NOT CHECKABLE: Code's own act. The forms it cites match items 1 and 2 of the list of record.
74. T1:73-74, departure 2. NOT CHECKABLE.
75. T1:77, ".gitignore: four admit lines for the second stage's report and cell". IMPRECISE. T2 is six lines: a two-line comment and four rules, and one of the rules (`/data/n/ckpt/backend-ext-2/*`) ignores rather than admits. Instead: "- `.gitignore`: six lines after the first stage's, a two-line comment and four rules that admit exactly the second stage's report and its cell's JSON;"
76. T1:78, the two data paths. CONFIRMED. The rec/ paths per (c4); T2 admits exactly these.
77. T1:79-81, seven raws, their mapping and names. CONFIRMED. The seven out/ files (REC:106-109 plus the record). The names follow 6e3474d's resume4 pattern (git show --name-only 6e3474d: …_out, _exit, _hashes, _resume-identity, _resume, _run). STAGE becomes _stage so that _run stays the pod session's record.
78. T1:84, cites "the third sitting's answers, §5.2". CONFIRMED. 2026-11-18_n-step4-run-pause_design-to-code_answers.md: line 3 "(third sitting)", line 38 "5.2 … a count of the home-folder prefix over the staged diff". Same citation as R:147.
79. T1:84-85, count 0; Not pushed. NOT CHECKABLE (commit-time facts).
80. T2:1, cites A2 v0.1 §4.1 and ANS fourth sitting §2. CONFIRMED.
81. T2:1-2, "the second stage's report and its one cell's JSON, likewise written on the box and copied back by hash; its arrays stay on the box". CONFIRMED. All 24 read lines are "N1-V none 0", so one cell; (c4); "likewise" matches .gitignore:283-286.
82. T2:3-6, the rules admit exactly data/n/reports/backend-ext-2.json and data/n/ckpt/backend-ext-2/N1-V__none__0.json, each re-inclusion after the rule it overrides. CONFIRMED.
    - `!/data/n/ckpt/backend-ext-2/` follows `/data/n/ckpt/*` (:288), under the re-included `!/data/n/ckpt/` (:287) and `!/data/n/` (:262).
    - `/data/n/ckpt/backend-ext-2/*` then ignores the folder's contents, and the next line re-includes only the cell JSON.
    - `!/data/n/reports/backend-ext-2.json` follows `/data/n/reports/*` (:293), under `!/data/n/reports/` (:292).
    - Every rule after :294 is anchored to /data/mf3/ or /data/p/. The only unanchored rules (:170-175) match neither path. No excluded parent blocks a re-inclusion.
83. T2, six lines, to go directly after `!/data/n/reports/backend-ext.json`. CONFIRMED. wc -l gives 6; the anchor occurs exactly once (.gitignore:294).
84. T2, .gitattributes already marks the cell -diff. CONFIRMED. .gitattributes:21 `/data/n/ckpt/** -diff`; git check-attr gives "diff: unset" for the new cell and "unspecified" for the report.

TOTALS: 84 items. 78 CONFIRMED, 1 IMPRECISE (item 75), 0 FAIL, 5 NOT CHECKABLE (items 23, 66, 73, 74, 79).

OBSERVATIONS
1. T1:22-23 omits who proposed the new folder names; (c1) says the pod session proposed them. Suggested: "…already held the step-4 smoke's folders (d5d08fa's box check), so the pod session proposed new names and the coordinating session accepted them."
2. The box's end state is missing. (c5) has the pod itself, not only the cleanup, waiting for the PI's word, which the coordinating session has asked for. REC §6 gives the state: no interpreter job, no GPU compute app, GPU at 0 MiB. 6e3474d's entry had a "The box at the end" bullet (R:300-302).
3. T1:61 "Code's one read of the report" can be read as the report's only read. The script also read it on the box: the state line (OUT:95), the identity check (OUT:98) and report-identity.txt, which is committed. Suggested: "Code's one read of the report on the laptop, after it came back by hash:" (6e3474d's form, R:279).
4. T1:39 "step 4's", in an entry headed "n step 4", is ambiguous. Say "the script's step 4 (the hashes)".
5. Ledger 27: the entry pins no library versions or determinism flag. REC §4 has python 3.12.3, torch 2.8.0+cu128, transformers 5.15.0, tokenizers 0.22.2 and CUBLAS_WORKSPACE_CONFIG=:4096:8. Also, identifier 8264f719efd347a9 equals v4's (V4:60), so both stages ran on one characterized backend; one line would record it.
6. There is no "Model:" bullet, which 6e3474d's entry had (R:277-278): one load on the box, the stage's (707/707), for the 24 reads.
7. Departures completeness:
   - SH:107 runs `git status --porcelain --untracked-files=all`, not item 1's bare form. It prints only on a failure branch, which did not fire. ANS §7 ruled this class inert for the pod session's scripts; the entry could note it for Code's script.
   - REC states no departure of its own; 6e3474d's entry said so in its own line (R:322).
8. n-build's close line on 6e3474d's entry (R:528-530) put the schema follow-up before the entry. (c3) set the entry first. T1:4-5 could name whose order it is.
9. 732a58f's header carries the PI's "route as given" (R:26). T1's header has no PI routing, while REC:3-4 cites routing item 2.
10. 732a58f puts **Next:** last (R:149); T1 puts it before Departures.
11. T1:11 is optional to change: A2 §4.1 names the three figures and §4.2 the lock's declarations. "(ADDENDUM-n2 §4.1 and §4.2; the answers' §2.4)" would be exact.
12. The box self-test was 408, against v2g's laptop 397 (R:31). v4's 389 against v2f's 378 (R:274, R:542) was the same gap of 11. The script required exactly 408, so the entry could say why the box runs 11 more.
13. The heading at T1:17 attributes T1:29-40 to REC, but those lines come from OUT. Suggested: "(the pod session's record and the script's output, both committed as raws)".
14. Optional parity facts: hashes.txt and report-identity.txt are both 93783db0…7b36, and the exit file is 9a271f2a…86aa, equal to v4's committed exit raw. 6e3474d's pod close line gave such hashes.
15. BK's 0.031 is in nats (ANS line 21) and sits beside this box's median rel. Adding "nats" would prevent a units misreading. The seat's own §2.4 form is otherwise reproduced exactly.
16. The Committed list could say .gitattributes needs no change, since its `/data/n/ckpt/** -diff` covers the new cell. 6df2131's entry named its .gitattributes line (R:983-984).

DEPARTURES
Barred by a rule, stated plainly:
1. `git ls-files -- 'results/raw/2026-11-18_*answers*'` with the three exclusions: a narrower positive pathspec glob in place of `.`. It printed nothing (the known ls-files quirk).
2. The same command without the exclusions. It printed five results/raw names only.
Neither pathspec could match anything under data/.

Not barred, stated for the seat to class:
- `git check-attr diff` on three named paths, two under data/n/ckpt and one under data/n/reports (item 1's form; attributes only).
- shasum for every digest (a Perl script on macOS, which item 1 permits), including `shasum -c` of the frozen manifest from the repo root. It read 24 named files, none under ckpt, reports or mf3; the marker word appears only in the manifest's text and its output.
- Reads beyond the named sources:
  - RESULTS.md lines 535-537, 612-625, 770-783, 978-987 and 2905-2912, plus whole-file greps of it;
  - greps of the second- and third-sitting answers raws, and line 38 of the third;
  - shasum of three committed v4 raws (hashes, resume-identity, exit).
- tr, sort, comm, uniq and wc -l on named S files, with zsh process substitution, which writes no file.
- No grep, listing, find or glob in S; rec/ files by shasum only; nothing under data/mf3; no interpreter, write or network; no guard marker in any argv.
```
