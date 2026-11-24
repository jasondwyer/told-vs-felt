# n — the N-pod campaign's seat block and BUILD: the focused blind values-check of the later edits, as returned, with every disposition

PI date 2026-11-23. Code (the n-build session). LOCK-n.md is cited as LOCK-n v1.0 cites it (LOCK-n.md:54–57):
`L:N` is line N of v0.1's text, as `deabf3f` numbers it; a line of the file at `098218c` is `LOCK-n.md:N`.

**What was checked.** One blind pass by a subagent, at HEAD `098218c`, over every line that changed in seven texts
after an earlier blind check had read them, and over four new texts:
- P1–P3, the seat block, the spec raw's head and the block's entry, against the drafts the block's first
  values-check read (`ef8b64e7…4e5b`, `cc1b2427…8bfd`, `be927cc3…deae`);
- P4–P6, the BUILD's entry, its review raw's head and its self-test raw, against the drafts the BUILD's values-check
  read (`82de4546…768a`, `05fa5d79…5ddd`, `73536a88…2a10`);
- P7, the driver, draft 2 (`7249b88f…d9b5`) to draft 3 (`fd643681…26d9`);
- N1, Code's addendum to the readings (`e8171ce0…dd75`); N2, the spec raw as assembled in a trial; N3 and N4, the
  heads and dispositions of the two values-checks' raws.

**The checker's brief** was a file the checker read itself, as its prompt directed: Code's scratch file
`S/step4b/camp/build/fc_brief.md` (`06956032…9668`, 157 lines). It:
- named the texts with their earlier drafts, each by name and sha256, to be compared by `git diff --no-index -U0`;
  the sources in the repository, at `098218c`, with the seat's raw untracked; in Code's scratch, the reports, the
  spec raw's five sources and Code's running list of its commands' kinds, each by name and sha256; in the sessions'
  notes folder, two named files; in this session's transcript, the coordinating session's messages;
- gave the citation forms, LOCK-n v1.0's own among them;
- allowed `shasum`; `jq` on committed JSON and on this session's transcript; and `sed -n`, `/usr/bin/grep`, `cut`,
  `diff`, `cmp`, `od`, `wc -l`, `tr`, `sort`, `uniq` and `git diff --no-index` on the named scratch files. It barred
  any other interpreter (`awk` among them), any write, any network, any guard marker in an argv, and globs over the
  root, `results/raw/` or a folder of marker-named files;
- barred anything under `data/m[f]3`, any read, listing, size or time of a ckpt or reports file, anything in Code's
  scratch but the named files, and any look for G-TIME-n's two steered cells;
- asked for a sweep of Code's shell commands from the BUILD values-check's end (2026-11-24T02:38:59.712Z, T's UTC
  stamp) to the command that hashed the running list, classed as the seat block's or the BUILD's;
- quoted the list of record v2's items 1–5 verbatim (equal by `diff` to the survey's brief's), and required item 3's
  pathspec and the campaign folder's exclusion on every git command over the tree.

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (249 lines, sha256
`0da6ac5fb671cd0a5858622d4430f6de59650e5fb37e5e5695e5c4a9874b9a67`), with one change. Its item 95 names the two
strings the first seat check's item 100 counted, two that a commit here may not carry; they are written "the temp
root's user folder" and "the scratch folder's name", as in that check's raw, and nothing else is changed. It names
scratch files as S/..., the sessions' notes folder as N and the transcript as T. Its times are T's UTC stamps.

**Totals:** 118 items: 102 CONFIRMED, 12 IMPRECISE, 2 FAIL, 2 NOT CHECKABLE; and 9 observations.

**The checker's departures,** as its report states them, are in the entry's departures, for the seat to class.

## 1. Dispositions

The seat's texts (P1–P3) and the BUILD's (P4–P6) were edited as their v2 copies, by the file tools only, and their
edits are replayed by tool, the seat's in this commit's first values-check raw and the BUILD's in the BUILD's. The
first check's dispositions (N3) are in this commit's first values-check raw; the BUILD check's (N4) are in the BUILD's
values-check raw. The driver's one item goes to the BUILD's next draft, with its own self-test window.

**The two FAILs, one point:**
- **Items 26 and 100, how R: reads after the rebase.** Applied in the checker's words. The block's short form is now
  "R: is `RESULTS.md` at `098218c`; its line anchors move with every entry (this block's parent is `c26b117`)", and
  the first check's observation-1 disposition says the same: the parent moved to `c26b117`, R: stays `098218c`'s, and
  the spec raw's head keeps every file:line at `098218c`. So the block's R:7842–7847 stands as it was.

**The twelve IMPRECISE items:**
- **Items 20, 25 and 102, m:251's "last clause".** Applied in the checker's words: "m:251's clause on a restart", in
  the block's CP13 texts and its Q7, and in the first check's observation-6 disposition.
- **Item 30, the spec raw's cited lines.** Applied in the checker's words: §3's seat:N is the seat's raw's line N,
  committed unchanged at `c26b117`. The head now names `c26b117` as the raw's parent, which changes `RESULTS.md` alone
  among the cited files, so §1's R: anchors are `098218c`'s.
- **Item 38, step 13's two `jq` commands.** Applied in the checker's words, in the block's entry.
- **Item 50, after13's provenance.** Applied in the checker's words: the output as step 7's tool result holds it, its
  lines before its last, "step 7 exit 0".
- **Item 52, the BUILD entry's Citations bullet.** Applied in the checker's words: LOCK-n v1.0 cites `L:N` and "v1.0
  §N"; "L §N" is this driver's form for v1.0's "v0.1 §N".
- **Item 53, the history list.** Applied: `gtime_lock_inputs`'s docstring (v0.1's §3–§4, which v1.0 carries) is on
  it, which the BUILD's check and Code had both missed.
- **Item 76, "L §N" in the driver's docstring.** Applied in the BUILD's next draft, in the checker's words: "L §N,
  this driver's form for v1.0's "v0.1 §N", is a section of v0.1's text".
- **Item 92, the spec raw's build script.** No text claims it: the brief alone said that the script differs from its
  predecessor "only by the fifth source, its heading and its checks". The checker's account is the right one, and no
  committed text needs a change.
- **Item 105, `82de4546…c768a`.** Applied: `82de4546…768a`, a five-character tail slip of the same kind as the
  coordinating session found in a window request (observation 9).
- **Item 108, "the three drafts".** Applied in the checker's words: "the two drafts (1 and 2) and HEAD's driver as
  copied".

**The two NOT CHECKABLE items:** item 51 is the commit, Code's plan; item 103 is the commit gate's scan, whose script
is not among the checker's sources.

**The nine observations:**
- **O1, the review raw's §2 and `L:N`.** Applied: the review raw's head now says that its §2, as returned, writes
  `L:N` for the file's line at `098218c`, its brief's form.
- **O2, "four docstrings and comments".** Applied: "four corrections in docstrings and a comment", in the BUILD's
  entry, its review raw, its self-test raw and its values-check raw.
- **O3, the rendering pause "by digest" only.** Applied in the spec raw's head: the renderer's own refusal, in the
  package's masked form, beside the digest.
- **O4, the usage error for `campaign`.** Applied in the BUILD's next draft: the message names G-VER's STOP record
  beside the stage's root and report.
- **O5, the addendum's "(LOCK:361)".** Met in the spec raw's head, whose list of imprecise points as sent now has §3's
  point 1: LOCK:361 is a gate re-run's delta, and the BUILD's move is LOCK:356–358 and :382. The addendum stays
  verbatim, as sent.
- **O6, "the seat's next thread".** Applied: the block and its entry speak of the seat's next sitting (ans23b:68) or
  of the seat, and keep rt23a's quotation as it stands.
- **O7, run 3.** Applied: the BUILD's texts give run 3 from the transcript's records (774/774, run 2's bytes).
- **O8, the running list.** Applied: its two slips are corrected, and the memory note's edit is named in it, for the
  BUILD's entry.
- **O9, abbreviations.** Applied: before each commit, a check by tool takes every "first 8 … last 4" abbreviation in
  the commit's texts and finds its full sha256 among the files and records they name.

**The sweep.** Its uncovered kinds, (a) to (j), are in Code's running list now. Its class counts set the split: 18
commands to the block's entry, 22 to the BUILD's. Its count of guard markers and of the campaign folder's plain name
in the span's commands is 0.

## 2. The report as returned

```text
FOCUSED BLIND VALUES-CHECK: the changed lines of P1–P7 and the new texts N1–N4, at HEAD 098218c. Read-only. The only interpreters run were shasum and jq.

Inputs. The brief's sha256 (0695603249d0…9668, 157 lines) matched before I read it. All 33 named scratch files match their sha256s by `shasum -c`, and every line count the brief gives is right. HEAD is 098218c. The untracked seat raw (ans23b) is e07fba2c…eba9, 68 lines. N's addendum copy equals N1 by `cmp`. Every repository file I cite is clean (`git rev-parse HEAD:<path>` = `git hash-object <path>`). The P7 delta file equals the direct `git diff --no-index` of draft 2 against draft 3: four hunks, +6 −3.

ITEMS

P1 (S/step4b/camp/seat/block_v2.md)
1. P1:8. The previous thread read v1.0's draft (ans23a) and handed off (ans22b:31; rt23a:37–38). CONFIRMED. rt23a:3 (the draft's read, the thread's last before its handoff); ans22b:31; rt23a:37–38.
2. P1:9–11. ans23b §1 accepts v1.0 as committed; its §2 is ans23b:24–31; N.2 quote; the PI's "Route as given" (rt23b); the addendum is the spec raw's §3. CONFIRMED. ans23b:1, :13–18, :20–31, :55. T at 2026-11-24T02:50:28Z holds the coordinating session's relay of "Route as given" (14 bytes).
3. P1:13–15. `LOCK_SHA256` is v0.1's (drv:3820); `gtime`/`gver` refuse (LOCK:356–361); the self-test fails on the same checks (drv:4562, :5549). CONFIRMED.
   - drv:3820 is 88d9fe7b…e9d5.
   - drv:4562 calls `gtime_lock_inputs(work)`, which raises at :3913–3914. drv:5549 is GV4's check through `gver_lock_check`, which raises at :5167–5168.
   - drv:457–464 record each section's SystemExit as a failed "ran to its end" check.
4. P1:28–30. §3 e8171ce0…dd75 (39 lines); §4 the brief; §5 7f728f96…43d1 (342 lines), compiled at 098218c. CONFIRMED. Hashes and counts by tool; survey_report_v1.md:1 says "at HEAD 098218c".
5. P1:43–44, :46. ans23b's path, "the seat's second sitting of 2026-11-23" (placeholders skipped). CONFIRMED (ans23b:3).
6. P1:96–97. No `--smoke` and no `--out`; at a start G-VER STOP, G-VER's record is written beside the report. CONFIRMED. draft 3:7700–7727 refuses both options. CAMP_GVER_STOP (draft 3:6160) is data/n/reports/campaign_gver_stop.json, beside data/n/reports/campaign.json.
7. P1:141–145. A rendering pause's read sequence, as runner:470–479 derives it; untold reads against BK's; N4-T/N4-Ts "as found now"; the masked form (ids:148–151); never a token id. CONFIRMED. runner.py:470–479 tests `ids_sha` only when `told` is None. ids.py:148–151 is `_problem`. draft 3:6483–6507.
8. P1:149–151 and :156–158. The ans23b:27 quote and the spec raw's §3 point 4; ans23b:27 added to the texts. CONFIRMED (ans23b:27; N1:20–24).
9. P1:159–164. The driver refuses a ruling that is not at HEAD's committed bytes. When an excerpt cannot be formed, it prints one line and the exit stays 3. CONFIRMED. draft 3:6581–6590; :6769–6782 ("EXCERPT pNN unavailable: <kind>; the pause stands in the report"; PAUSE 3).
10. P1:165–169. m keeps its file beside the checkpoint (stages.py:272–278); the analyzer refuses a file beside the cells (anl:3199–3203). CONFIRMED. valence_core/m/stages.py:271–278 (`adjudication_path`); scripts/n_analyze.py:3199–3203.
11. P1:174–182. CP9 (a) as built, a session whose failed ids count once included. CONFIRMED.
   - Code: draft 3:5369–5400 (`gver_write`: `check_gver` before the write and after the read-back), :6322–6332, :6335–6387 and :6714–6735 (the record is removed if the report fails; exit 1).
   - verify.py:94–105 `continue`s past a session whose ids fail.
   - schema.py:1195–1199 and :1533–1537; anl:6238 and :6710–6719; LOCK:938.
12. P1:184, :186–187. At a resume, G-VER's record is printed whole. A MANIFEST.json off its pin reaches this STOP at a resume, because `rendering_id` is the pin. CONFIRMED. draft 3:6736–6741 and :6642–6644. verify.py:19 and :140 put the pin in the pass rule.
13. P1:188–191. The PI's stop is limited to a standing pause by Code's design; the schema:208–210 quote; schema:213; :1197; n:134's "a PI stop". CONFIRMED. schema.py:1518–1525 sets no pause requirement for PI-STOP; draft 3:6422–6424.
14. P1:199–201 and :210. The build line for (a)/(c), exits 6 and 7, and "G-VER's STOP record if any". CONFIRMED (draft 3:6184 CAMP_EXITS; item 11).
15. P1:225–227. Nothing in the driver; the BUILD adds the `.gitignore` lines. CONFIRMED (P4:79–88, +19 −3). The close's script is plan.
16. P1:233–239. The exits; any SystemExit, with or without a message, exits 1; argparse exits 2; ans22a:25's "the record on disk"; a resume's G-VER STOP; at a PAUSE the exit stays 3. CONFIRMED. draft 3:6671–6675 (`_camp_why`), :6694–6782; ans22a:25.
17. P1:240–244. The ruled classes against Code's additions. CONFIRMED. ans22a:27 (the weights folder's files, one of the eight, an ids file; the "stop, touch nothing, escalate" quote); ans22b:24 (the missing folder is INTEGRITY).
18. P1:247–252. The ans23b:28 quote; G-TIME-n's exits (drv:4384–4385, :4391–4405, :4448). CONFIRMED. The quote is verbatim. drv:4396–4400 give 2, :4405 gives 3 or 1, :4448 gives 0.
19. P1:263–264. Code's reading against the respawn protocol's two steps. CONFIRMED (CLAUDE.md's respawn protocol: "Both PASS before anything runs").
20. P1:269–273. "m:251, whose last clause reads "after a restart … carries the new identifier"". IMPRECISE. The quotation is in m:251, but a clause follows it: "raw outputs and checkpoints are committed before any pod instance stops (rule 27), under §4's blinding rule."
   - Put instead: "m:251, whose clause on a restart reads "after a restart the new `BACKEND` entry's identifier … carries the new identifier"".
21. P1:308–310. The DRIVER line prints the BUILD's driver's sha256; CP4 as sent said STAGE line; mF3ans:43; "the seat's to confirm for n". CONFIRMED (draft 3:6604; cp_readings_v1:64–66; mF3ans:43).
22. P1:313. The survey's departures are in §5. CONFIRMED (N2's §5 heading).
23. P1:323–329. Q3: each excerpt in its own raw (ans23b:27). The excerpt prints `absdiff` at full precision, the per-read line prints `rel`, and their ratio is the cached path's scale. CONFIRMED. draft 3:6458 (`!r`); runner.py:509–511; schema.py:416–418 (scale "max(|logprob_S|, |logprob_U|), cached path"); review O3.
24. P1:330–341. Q4's additions. CONFIRMED. runner.py:330–331 with schema.py:1134 STOP_KINDS; anl:6238, :6710–6719; schema.py:213; n:134; anl:6677–6679; draft 3:6797–6799.
25. P1:347–350. "m:251's last clause carries a restart's new identifier into the resume identity". IMPRECISE, as item 20.
   - Put instead: "m:251's clause on a restart carries a restart's new identifier into the resume identity".
26. P1:49 (unchanged, but the change contradicts it). "R: is `RESULTS.md` at `098218c`, this block's parent". FAIL. P1:43–46 now cite ans23b and rt23b as "committed at `@ITEM5@`", and P3:58 names `@ITEM5@` "this block's parent".
   - Put instead: "R: is `RESULTS.md` at `098218c`; its line anchors move with every entry (this block's parent is `@ITEM5@`);". P1:153's R:7842–7847 then stays right.

P2 (S/step4b/camp/seat/spec_head_v2.md)
27. P2:7–10. The readings went as the note 2026-11-23_n-build_campaign-pins.md, a byte copy checked by `cmp`, named by name, abbreviation and line count. CONFIRMED (departures.md:32; the seat check's item 89).
28. P2:13–18. §3 verbatim (e8171ce0…dd75, 39 lines); N.2's quote; "Route as given"; CP8 and CP12 each gain a sentence; the note 2026-11-23_n-build_campaign-pins-addendum.md, checked by `cmp`; in no other repository file. CONFIRMED.
   - ans23b:55; T 02:50:28Z.
   - Code's `cp`/`cmp` at 02:51:23Z; my `cmp` of N1 with N's copy: equal.
   - `git grep` of two N1 phrases with item 3's pathspec and the m[f]3 exclusion: no match.
29. P2:19, :21, :28, :37–38, :40, :53–54. The move to five sections. CONFIRMED: no stale §3/§4 is left in P2.
30. P2:26. "Every file:line in §1, §3 and §5 is the repository's at `098218c`." IMPRECISE. §3's seat:N cites the seat's raw, which is untracked at 098218c (it is committed at `@ITEM5@`).
   - Put instead: "Every file:line in §1, §3 and §5 is the repository's at `098218c`, but §3's seat:N, the seat's raw's line N, committed unchanged at `@ITEM5@`. @PARENTLINE@".
31. P2:43–47. The untold digest against BK's (runner.py:477–479); N4-T/N4-Ts "as found now". CONFIRMED (draft 3:6505–6507).

P3 (S/step4b/camp/seat/entry_v2.md)
32. P3:13–17. CONFIRMED (ans23b:3, :20–31, :55; T 02:50:28Z).
33. P3:28–30. CP8/CP12 gain a sentence (points 4 and 5); Q3 and Q4 each carry one question from the review. CONFIRMED (P1:149–151, :247–250; review O3 and O5).
34. P3:40–45. The five sections and their hashes; "two in §5". CONFIRMED.
35. P3:48–51. The values-check: items 1–5 quoted; `shasum` and `jq` allowed; 124 items (97/18/4/5); 12 observations. CONFIRMED (vc_report.md:5 and each item's verdict; the seat check's prompt in T holds item 5's line).
36. P3:52–55. The four FAILs as fixed. CONFIRMED (vc_report items 89, 107, 112, 115; P2:7–10; P3:76–77, :115–118, :131–139).
37. P3:56–58. Every disposition applied or met; observation 1 met by the routing, "committed at `@ITEM5@`, this block's parent". CONFIRMED as N3 states it; the commit is plan. See item 26.
38. P3:67–68. "`jq` over the step-13 sweep's record file in scratch and over this session's transcript, the first through a `while read` loop of `jq` calls … (two commands)". IMPRECISE. T 2026-11-23T08:07:52Z ran `jq` over the record file and over T, and the T pass went through a `while read` loop of `jq` calls over T. 08:08:47Z ran `jq` over the record file. "the first" reads as the record file.
   - Put instead: "`jq` over the step-13 sweep's record file in scratch, and in the first of the two commands also over this session's transcript through a `while read` loop of `jq` calls, for the sweep's counts (two commands);".
39. P3:69–75. Span A's `rm`, `mkdir -p`/`mv`/`rm`, `make_raw13.sh`, `bash -n`, `fill_window13.sh` with `grep -c`/`-n`. CONFIRMED (vc_report item 106 and span A).
40. P3:76–85. Span B's additions (two memory notes; `git show HEAD:RESULTS.md` into `sed -n`/`grep -n -E`; `grep -c -F`; the gate script's grep; the scoped status; the values file's `diff`/`tr`/`wc -c`/`shasum`). CONFIRMED (items 107–108, span B).
41. P3:99–101 and :106–108. Two `ls -1` of the root; PROPOSAL-n through `fold`; stages.py added. CONFIRMED (items 110–111).
42. P3:115–118. The `printf >>` to the memory index with `tail` and `wc -l`; the scratch `mkdir -p` and two files made by redirects. CONFIRMED (item 112).
43. P3:122–130. `--name-status` of 2ca24e8 and d92500b, `--name-only` of d92500b; `wc -c` of three notes; `cat` of two scratch files. CONFIRMED. T 2026-11-24T00:38:53Z (2ca24e8 --name-status); 00:38:58Z (d92500b --name-status, and --name-only in its loop); item 114.
44. P3:131–139. Fifteen raws; five commands in results/raw/; two narrow globs; `valence_core/n/*.py` (sixteen names); `wc -c` of a PROPOSAL-m line. CONFIRMED (item 115; `git ls-files` shows 16 *.py there).
45. P3:140–145, :149–150. The quoted-glob `git ls-files` into `wc -l`, the `while read` loop and isMeta; the block draft's checks. CONFIRMED (items 116 and 119).
46. P3:156–157. The file tools in every span. CONFIRMED (vc_report O10 and its sweep).
47. P3:158–163. The outputs that printed Q-F3's short name. CONFIRMED (item 121).
48. P3:164–168. The survey's item 4 additions. CONFIRMED (item 122).
49. P3:169–173. The values-checker's departures. CONFIRMED (vc_report DEPARTURES 1–4).
50. P3:174–180. after13's output, "7 lines, sha256 `ec413c1c…b771`… the tool result of step 7 of `098218c`'s window, verbatim … (two matching records … equal by `cmp`)", with its contents. IMPRECISE.
   - Step 7's tool result (T 2026-11-23T22:48:05Z) has 8 lines, the last "step 7 exit 0". Its first 7 lines hash to ec413c1c…b771 (`jq -r`, then `sed '/^step 7 exit 0$/,$d'`, then `shasum`).
   - Two records hold it: a "user" record (T line 73683) and an "api-request-blob" (73685). The contents are as stated.
   - Put instead: "It is after13's output as the tool result of step 7 of `098218c`'s window holds it, verbatim (the result's lines before its last, "step 7 exit 0"), taken from …".
51. P3:186. Committed by path with after13's output. NOT CHECKABLE (plan).

P4 (S/step4b/camp/build/entry_v2.md)
52. P4:5–7. "LOCK-n.md is cited as LOCK-n v1.0 cites it (LOCK-n.md:54–57): `L:N` …; "L §N" is a section of v0.1's text and "v1.0 §N" …; … `LOCK-n.md:N`." IMPRECISE. LOCK-n.md:54–57 define `L:N` and "v1.0 §N". v1.0 writes v0.1's sections as "v0.1 §N" (22 lines of 1–395). "L §N" occurs 0 times in LOCK-n.md (grep).
   - Put instead: "LOCK-n.md is cited as LOCK-n v1.0 cites it (LOCK-n.md:54–57) for `L:N`, line N of v0.1's text as `deabf3f` numbers it, and "v1.0 §N", a section of v1.0's part; "L §N" (v1.0's "v0.1 §N") is a section of v0.1's text, and `LOCK-n.md:N` a line of the file at `098218c`."
53. P4:12–15. The list of where "LOCK-n v0.1" stays. IMPRECISE. Draft 3 holds the string 9 times (grep -F).
   - Eight are on the list: :182 and :240 (the two heads), :212, :265 and :268 (GT3, GV2, GV4), :1096 (`convention_line`, backend-ext), :3932 (`lock_fidelity_rule`) and :5651 (a `gver` check name).
   - The ninth is :3969, `gtime_lock_inputs`'s docstring, "GT4: the lock's inputs (LOCK-n v0.1's §3-§4, which v1.0 carries unchanged)". HEAD's :3895 read "LOCK-n v0.1's inputs".
   - Put instead: "…the `gtime` and `gver` paragraphs' heads, `lock_fidelity_rule`'s docstring, `gtime_lock_inputs`'s docstring (v0.1's §3–§4, which v1.0 carries), one backend-ext printed line and one `gver` check name."
54. P4:16–18. The cap is held to v1.0 §2's span (LOCK-n.md:106). CONFIRMED (the span is on LOCK-n.md:106; draft 3:6163–6164).
55. P4:42–45. "(L:543, LOCK-n.md:938)"; `rendering_id` is the pin. CONFIRMED. v0.1's text starts at LOCK-n.md:396, so L:543 is :938, G-VER's row. draft 3:6610–6611 and :6643.
56. P4:66–67. Every other option is refused; `--selftest` is taken before any command. CONFIRMED (draft 3:7700–7727).
57. P4:68–71. The docstring has "but CP4's DRIVER line as built (the review's F6) and CP8's excerpt…". CONFIRMED (draft 3:318, :325–326).
58. P4:72–73. Draft 3 is fd643681…26d9, 7,834 lines, +1,643 −33 from 55885e65…385f. CONFIRMED (shasum; wc -l; `git diff --no-index --numstat` gives 1643 33).
59. P4:76–78. Draft 2 is 7249b88f…d9b5 (7,831 lines). Draft 3 is +6 −3, for items 14, 80 and 81 and observations 8 and 9. No check reads them. CONFIRMED. numstat gives 6 3. The four hunks map to those items. The driver's only two `__doc__` uses are `keys.__doc__` (:4683) and the module docstring's first line (:7681), and no `chk` reads a docstring.
60. P4:92–93. Draft 2 ran 774/774. CONFIRMED.
61. P4:101–104. F1 on N4-T's told and N4-Ts's sham reads; F2 counted three times; the counts; "F1–F5". CONFIRMED (review_report.md:9–19, :7–174; F5 "Applied").

P5 (S/step4b/camp/build/review_head_v2.md)
62. P5:3–4. The citation form for `L:N`. CONFIRMED (LOCK-n.md:57). See observation 1.
63. P5:41, :44–46. F1–F5; draft 3's hash, 7,834 lines, +6 −3, the items, no check reads them. CONFIRMED.
64. P5:62–63. F1's check forms. CONFIRMED (draft 3:7051–7069: untold, N4-T, N4-Ts, a missing sequence, read 5, past the plan, another kind → None, no launch index → None).
65. P5:64–65. F2 over-counted three times. CONFIRMED (review_report.md:16).
66. P5:81–82. The PI's stop (new=False) removes nothing. CONFIRMED (draft 3:6358–6361, :6434).
67. P5:95–97. F6: "the BUILD's driver blob"; draft 3's PINs header; the DRIVER line; mF3ans:43; the CP4 line. CONFIRMED (cp_readings_v1:65; draft 3:318, :325–326, :6604; mF3ans:43 "the campaign's DRIVER line prints the new one").
68. P5:102–103. F9 (LOCK-n.md:106; U+00D7, C3 97 by `od`). CONFIRMED (`od` of draft 3:6164 shows c3 97).
69. P5:153–154. O4 "(L:543, LOCK-n.md:938)". CONFIRMED.

P6 (S/step4b/camp/build/selftest_raw_v2.txt)
70. P6:5. 55885e65… (+1643 −33). CONFIRMED.
71. P6:10, :19–22. The package by shell over three overlays; all three built by the script; overlay3 differs from overlay2 in the driver alone. CONFIRMED. T 03:14:49Z printed 175 files, "package by shell 06b55761…1d39", driver fd643681…26d9, and a `diff -rq` of one line, the drivers. Overlays 1–2 are per the BUILD check's items 2 and 70.
72. P6:23–25. No marker in an exec'd process's argv; the glob is in `cd`'s argument. CONFIRMED (the run command cds by `jl*` and runs `./python … --selftest`).
73. P6:28–33. The grants' checks before each run; Code's own checks (TMPDIR before run 1; both before runs 2 and 3); after each run, stderr and TMPDIR empty and no process; the closes. CONFIRMED.
   - Runs 1 and 2: the BUILD check's items 21 and 72 and its O7.
   - Run 3, read in T, partly after this brief's hash: Code's check at 03:14:49Z (0 TMPDIR entries, 0 run-3 files); the grant at 03:24:18Z ("TMPDIR S/camp/tmp empty, and no selftest_run3 file"); the check after the run at 03:24:52Z (exit 0, stderr 0 bytes, TMPDIR 0, no process); the close at 03:25:21Z.
74. P6:47. F1-F5 and F8-F11. CONFIRMED.
75. P6:57–63. Run 3: draft 3's sha, +6 −3, the four corrections; "run 3 has run 2's checks". CONFIRMED (delta3; T 03:24:52Z: run 3's output is run 2's bytes, 5aa33ca8…def0, "774/774").

P7 (draft 2 → draft 3)
76. draft 3:290–291. "LOCK-n.md is cited as LOCK-n v1.0 cites it (LOCK-n.md:54-57): L:N … (L:543, G-VER's row, is LOCK-n.md:938 at 098218c), and L §N is a section of v0.1's text." IMPRECISE. `L:N` and L:543 = :938 are right, but "L §N" is not v1.0's form (item 52).
   - Put instead: "… (L:543, G-VER's row, is LOCK-n.md:938 at 098218c); L §N, this driver's form for v1.0's "v0.1 §N", is a section of v0.1's text."
77. draft 3:318. CONFIRMED (CP4's line at :325–326 says the DRIVER line and the sha256).
78. draft 3:6516. `committed` raises ValueError outside the repository. CONFIRMED (`committed_bytes`, :2832–2837, `relative_to` raises; the callers catch it at :6404–6407 and :6584–6587).
79. draft 3:6788–6789. A failed write leaves the file as the write left it. CONFIRMED (:6335–6362, :6807–6811).

N1 (S/step4b/camp/spec/cp_readings_v1_add1.md)
80. N1:3–9. The raw's path, e07fba2c…eba9, 68 lines, untracked; §2's and N.2's quotes; "Route as given" relayed on 2026-11-23; fd80cf43…23b0; points 4 and 5. CONFIRMED (ans23b:22, :55; T 02:50:28Z).
81. N1:11–13 (point 1). CONFIRMED. ans23b:24; drv:3820; LOCK:361; draft 3:3893 holds 59e0b1bc…00aa. See observation 5.
82. N1:14–16 (point 2). CONFIRMED (LOCK:106, :949, :122–123; ans23b:25; draft 3:6163, :6653–6656: COMPLETE or CAP refused before the load).
83. N1:17–19 (point 3). CONFIRMED (LOCK:1252, :862 7f7d7301…88a6, :1070; draft 3:6300–6307).
84. N1:20–24 (point 4). CONFIRMED (LOCK:931, :936–950, :1041 "§13. Alpha and the tile"; ans23b:27; the EXCERPT lines at draft 3:6448, :6776).
85. N1:25–27 (point 5). CONFIRMED (ans23b:28; P1:247–252).
86. N1:28–31 (point 6). CONFIRMED (ans23b:29; LOCK:382–385).
87. N1:32–34 (point 7), "none is ever committed" included. CONFIRMED (ans23b:30; LOCK:385–389; CP10 "Never the arrays").
88. N1:35–39 (point 8). CONFIRMED (ans23b:31); the one commit is plan.

N2 (S/step4b/camp/seat/trial/spec_trial.md and the scripts)
89. The head is P2's current file with its one placeholder line filled. CONFIRMED: `sed -n 1,54p` diffed against P2 gives one hunk, 26c26, "@PARENTLINE@" → "(the parent line, a trial fill)".
90. The five fenced bodies are byte for byte the five sources. CONFIRMED: `cmp` of lines 59–248, 254–272, 278–316, 322–426 and 432–773 against cp_readings_v1, routing_camp, the addendum, brief_scrubbed and survey_report_v1.
91. The headings and fences are as the script prints them. CONFIRMED: `sed -n l` of the frame lines; 10 fence lines; no local path in the trial (grep count 0).
92. The script differs from build_spec.sh "only by the fifth source, its heading and its checks". IMPRECISE. The diff also adds a refusal of a head that holds a placeholder line (`@[A-Z0-9]+@`; the trial's second build was refused by it), rewrites the header comment, and renumbers the brief's and the report's headings to §4 and §5. The fence count goes 8 → 10.
   - Put instead: "differs from build_spec.sh by the fifth source (its sha256 check, its fence check, its §3 heading and fences), the brief's and the report's headings renumbered §4 and §5, the fence count 10, a new refusal of a head holding a placeholder line, and its header comment."

N3 (S/step4b/camp/seat/vc_head_src.md and vc_disp_src.md)
93. Head:5–10. T1 ef8b64e7…4e5b (305); T2 cc1b2427…8bfd (48) and the raw 233b4173…832e (724); T3 be927cc3…deae (134) with three placeholders. CONFIRMED. The 724-line raw's full sha256 is in T (233b417339fb…e832e). entry_src holds exactly @VC@, @VCDEP@ and @FINAL@.
94. Head:12–25. The brief was given as the prompt: vc_brief.md 8916cd5c…aed3, 116 lines, and its contents. CONFIRMED. T's Agent call at 2026-11-24T00:55:47Z: its prompt, with `jq -r`'s newline, hashes to 8916cd5c…aed3, 116 lines. Phrase counts in it (awk, the spans, jq, item 5, UTC, steered cells) are each ≥ 1. I did not reproduce the contents.
95. Head:27–31. The report: jq, 251 lines, 86bb0ff0…6a02; item 100's two strings. CONFIRMED (vc_report.md:100 lists the temp root's user folder and the scratch folder's name among its strings). The rewording at assembly is plan.
96. Head:33, :35. The totals, and where the departures go. CONFIRMED (vc_report.md:5; per verdict: IMPRECISE 18, FAIL 4, NOT CHECKABLE 5; O1–O12).
97. Disp:7–16, the four FAILs applied. CONFIRMED (items 27, 40, 42, 44).
98. Disp:18–33, items 5, 7, 8, 41, 54, 63, 64, 68 and 71 applied. CONFIRMED (items 1, 3, 7, 13, 16, 17, 18, 19). Draft 3's `camp_excerpt` and `_camp_rendering` docstrings say "never a token id" (:6443–6444, :6488). Draft 1's wording is not among my sources.
99. Disp:34–37, items 106, 108, 110, 111, 114, 116, 119, 121 and 122 applied. CONFIRMED (items 38–48), with item 38's wording.
100. Disp:40–45 (O1). The first parts are CONFIRMED: T 01:28:42Z (Code holds the block's window request); T 02:50:28Z ("Route as given"); the block cites ans23b's items 4 and 5. But "The parent's anchors moved: R: is `RESULTS.md` at `@ITEM5@`, and the spec raw's head says so." FAIL. P1:49 says R: is RESULTS.md at 098218c, and P2:26 keeps every file:line of §1, §3 and §5 at 098218c; §1's R:7842–7847, R:2799 and R:1131–1140 are 098218c's.
   - Put instead: "The parent moved to `@ITEM5@`: R: stays `RESULTS.md` at `098218c`, as the block's short form now says with `@ITEM5@` named as its parent, and the spec raw's head keeps every file:line at `098218c`."
101. Disp:46–60, O2–O5 and O7–O11. CONFIRMED (P3:174–180; P1:96–97, :333–337, :165–169, :225, :20–22, :237–239; P3:156–157).
102. Disp:52 (O6). "CP13's texts quote m:251's last clause". IMPRECISE, as item 20.
   - Put instead: "CP13's texts quote m:251's clause on a restart".
103. Disp:61–63 (O12). The gate's scan. NOT CHECKABLE (the gate script is not among the sources). "verbatim" holds (item 90).

N4 (S/step4b/camp/build/vc_head_src.md and vc_disp_src.md)
104. Head:3–4. The citation form. CONFIRMED.
105. Head:7. "T1 … `82de4546…c768a` (141 lines)". IMPRECISE. By `cut`, the abbreviation is `82de4546…768a`. The count and the three placeholders (@SEATCOMMIT@, @VC@, @DEPARTURES@) are right.
   - Put instead: "`82de4546…768a`".
106. Head:8–13. T2–T5's hashes and counts. CONFIRMED.
107. Head:15–16. The checker read the brief file itself (3a5756b2…be9a, 152 lines). CONFIRMED (T 02:39:13Z's prompt: "Your whole brief is one file").
108. Head:17–22. "In Code's scratch, by name and sha256: the three drafts and HEAD's driver as copied…". IMPRECISE. vc_brief.md:48–73 names two drafts of the driver (draft 1 and draft 2) and HEAD's copy. The rest of the list holds.
   - Put instead: "the two drafts (1 and 2) and HEAD's driver as copied".
109. Head:23–33. The tools, the bars, the span from 00:55:07.441Z, and the list of record "equal by diff". CONFIRMED. vc_brief.md:6–11, :100–111, :124–152. My `diff` shows vc_brief:147–152 equal to survey_brief_v1:100–105. T 03:23:47Z appended the seat brief's lines 111–116 into this brief, and its tail equals the survey brief's.
110. Head:35–39. The report's hash and 280 lines; S/…, N, T; UTC stamps; totals 91 (75/10/0/6); 10 observations. CONFIRMED.
111. Head:41–44, :46. The brief's "L:line, the file's line" (vc_brief:35–36); LOCK-n.md:57; items 8, 64 and 80; "L:106" the slip. CONFIRMED.
112. Disp:3–5. The v2 copies, edited by the file tools only. CONFIRMED. T 03:13:43Z `cp`/`cmp`; 11, 12 and 6 Edits on them in the span; no shell edit. The replay is plan.
113. Disp:8–15, items 8, 64 and 80. CONFIRMED (P4:5–7, :17, :42; P5:3–4, :103, :153; draft 3:290–291; the delta touches docstrings and one comment only).
114. Disp:16–26, items 14, 81, 24, 47, 48, 52 and 54. CONFIRMED.
115. Disp:28–44, O1–O10. CONFIRMED. O2's list is the checker's own, and T 03:13:02Z has the `sed -n` of draft 2's lines 182, 240, 1094, 3930 and 5649. The checker and Code both missed :3969 (item 53).
116. Disp:46–47. The six NOT CHECKABLE items (35, 36, 37, 45, 66, 77). CONFIRMED.
117. Disp:49–53. (a)–(k) and the two slips are in the list; the counts 25 and 138; markers 0. CONFIRMED (departures.md:149–167, :141, :145–146; vc_report:253–257).
118. Disp:55–56. Draft 3 carries items 14, 80 and 81 and O8 and O9. CONFIRMED.

TOTALS
- 118 items: 102 CONFIRMED, 12 IMPRECISE, 2 FAIL, 2 NOT CHECKABLE.
- IMPRECISE: items 20, 25, 30, 38, 50, 52, 53, 76, 92, 102, 105, 108.
- FAIL: items 26 and 100.
- NOT CHECKABLE: items 51 and 103.

OBSERVATIONS
1. P5's raw: its new head sentence makes `L:N` v0.1's line N, but its §2 (the review report, verbatim) writes `L:N` for the file's line: review_report.md:56 "L:106", :58 "L:376", :165 "L:160–162". N4's head explains the same mismatch for its own §3. P5's head could add "§2, as returned, writes L:N for the file's line at 098218c (its brief's form)."
2. "Four docstrings and comments" (P4:77, P5:44, P6:59, N4 disp:55). The four corrections sit in three places: two in the module docstring, `CampEnv.committed`'s comment, and `run_campaign_pi_stop`'s docstring. "four corrections in docstrings and a comment" would be exact.
3. P2:43–47 gives a rendering pause "by digest" only. P1:144–145 and draft 3's `_camp_rendering` also give the renderer's own refusal in the package's masked form.
4. Draft 3's usage error for `campaign` (:7720–7722) says it writes data/n/ckpt/campaign/ and data/n/reports/campaign.json, but not G-VER's STOP record, which CP2 (P1:96–97) now names. It is only a message, outside the delta.
5. N1:12 cites "(LOCK:361)" for the BUILD's declared delta. ans23b:24 cites L:356–358, L:361 and L:382 for the same sentence. LOCK:361's delta is a gate re-run's, while :358 and :382 carry the BUILD's move.
6. P1:3 and :20 still speak of "the seat's next thread". With ans23b, that thread is open, and ans23b:68 sets the starred readings for its next sitting.
7. Run 3 is in T after this brief's hash (2026-11-24T03:24:27Z): exit 0, "774/774", its output run 2's bytes (5aa33ca8…def0), stderr empty, TMPDIR empty, no process; the window closed at 03:25:21Z. @RUN3@ can be filled from these.
8. departures.md, this span:
   - line 173 says "two quoted phrases"; three were counted (02:51:12);
   - line 180 says "five edits" to the seat entry; there were six (03:19:43–03:20:30), and the sixth, the observation-1 line, is counted nowhere;
   - one file-tool Edit of a memory note (the n-step14 BUILD note) is not named. The BUILD entry's @DEPARTURES@ should carry it.
9. `…c768a` is the same five-character tail slip as the `…62ad6` the coordinating session flagged in the draft-3 window note. A `cut` check of every abbreviation in the texts before the commit would catch both.

THE SWEEP (T; the assistant records' Bash tool_use items after 2026-11-24T02:38:59.712Z, through 03:22:33.809Z, the loop that hashed departures.md d6d6e32c…c493): 40 commands.

Commands outside item 1's forms that the list does not cover, by time and kind:
- (a) The list's own upkeep:
  - `printf >>` appends to the pending list (02:51:23, 02:51:51, 02:53:00) and to departures.md (03:13:37, 03:13:43, 03:17:47, 03:19:09, 03:20:05, 03:22:07);
  - the `cat >>` heredoc append of the "found by the sweep" block, with `wc -l` (03:13:37);
  - `/usr/bin/grep -n -E` over departures.md and `cat` of the pending list (03:13:22).
  The list names only the merge (`cat >>`, `: >`) and its two file-tool edits.
- (b) 02:51:07: `git status --porcelain` scoped to the seat's raw.
- (c) 02:52:26: `/usr/bin/grep -n` of the spec head's section references. 02:52:52: `mkdir -p` of the trial folder.
- (d) 03:14:16: `/usr/bin/grep -n -c` of `__doc__` over draft 2.
- (e) 03:14:22: `sed -n` of draft 3's docstring lines.
- (f) 03:14:43: a width count over draft 3 (UTF-8 locale).
- (g) 03:16:47 and 03:17:06: `/usr/bin/grep -n` of two v2 copies for edited citations and phrases (not counts).
- (h) 03:20:34: a placeholder grep over five texts into `sort` and `uniq -c`. 03:20:58: `cat` of the seat check raw's head source into `head`.
- (i) 03:22:24: `jq` over T (tool calls of 02:38–02:40), to fix this check's span start.
- (j) 03:22:33: `wc -l` (with `tr`, `printf`) beside `shasum` in the 32-file loop.

Wording slips in the list: line 173 (two → three phrases) and line 180 (five → six edits).

By class:
- the seat block's: 18 (02:51:07–02:53:00, 8; 03:18:05–03:20:58, 10);
- the BUILD's: 20 (02:39:21; 03:11:43–03:17:47, 18; 03:22:07);
- this check's preparation: 2 (03:22:24, 03:22:33), 22 with the BUILD's as the BUILD check counted its own.

Guard markers in the commands' text: [m]lx 0, [j]lens 0, [q]wen 0, [o]lmo 0, [i]pykernel 0. The campaign folder's plain name ([m]f3, any case): 0. The same holds for the command after the hash.

After the hash, to this brief's own hash: one command, 03:23:47. Its kinds:
- `cat` of the brief's head into the brief (`cat >`);
- `sed -n` of the seat check's brief, appended (`>>`);
- `diff` over process substitutions (`tail -n`, `sed -n` of the survey brief), with `echo`;
- `cmp` of the addendum against N's copy, with `echo`;
- `sed` of the placeholder into `cmp` against `head -n 54` of the trial, with `echo`;
- `wc -l`;
- a bracketed marker count;
- `shasum | cut`.

Beyond it are 16 more, run 3 (03:24:27) among them.

DEPARTURES
1. One `jq` pass over T, selecting tool results that held both "AFTER13 PASS" and "step 7 exit 0", printed several whole tool results beyond the one the finding needed. They included file contents, scratch paths, an agent id and a gate script's id list. I viewed them only and reproduced nothing here.
2. I read T beyond the sweep and beyond the coordinating session's messages, each time with a minimal print:
   - Code's commands and results at 08:07:52 and 00:38:53–58;
   - step 13's window result (22:48:05);
   - overlay3's build (03:14:49);
   - run 3 and its check, after this brief's hash (03:24:27–03:24:52);
   - the two values-checks' Agent prompts (a head; a hash, line count and phrase counts);
   - Code's SendMessage inputs (their heads).
3. `cat -A` was tried as a filter on piped output. BSD cat has no -A, so it printed only its usage error. `cat` is not among the brief's named tools.
4. One redirect to /dev/stdout inside a `jq` pipeline; no file was written.
5. One zsh `=` expansion error (`echo ======`) stopped one command, which I re-ran without it.
6. One unused shell variable named `awk_free`; no awk ran.
7. `sed` (substitution) as a filter to shorten paths and mask ids. I also used `sed -n`, `tr`, `od` and `/usr/bin/grep` over clean repository files, and `git diff --no-index` between HEAD's driver and the scratch drafts.
   No other interpreter, no write and no network. No marker or plain campaign-folder name in any argv; bracketed patterns only. Nothing under data/ read or listed. In S, only the named files, with no listing or glob. In N, only the two named files.
```
