# The coordinating session's three close lines on the routing of 2026-11-16 (second sitting): the blind values-check and its dispositions (PI date 2026-11-16)

Code's raw for the three close lines committed with the seat's three answer raws of 2026-11-16 (second sitting): on
`e5aba51`'s entry (the push note; the p-counters raw's section C), on `645bd3f`'s entry (the n-build raw) and on
`8e3bf91`'s entry (the n-ganl raw). One blind checker, a subagent of the coordinating session, under a brief quoting the
list of record v2's items 1–5 (with item 4's amendment by C.2 of this date) and allowing no interpreter, checked the
three drafts against the paste block as the coordinating session saved it, the three raws, ADDENDUM-n1, the two later
pushes' screen outputs and RESULTS.md. Its report is reproduced whole, as its hand-back message gave it, with one scrub:
a program's install path is shown as `<prefix>`. SCRATCH is the coordinating session's scratch folder. Code's
dispositions follow it.

## 1. The checker's report, whole

## Values-check of three draft close lines (routing of 2026-11-16, second sitting)

There are no FAILs. Four claims are IMPRECISE, all cheap to fix. Every hash, byte count, commit count, quotation and screen figure checks out. The one item that could have a real effect is observation O-1, the pod session's "items 1 and 4".

### Header

**What I read**
- **In full:** the three drafts and `paste_block.txt` (SCRATCH = routing-11-16b); the three seat raws; `ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md`; and, in c7-commit, `screen_push2.txt`, `screen_push3.txt`, `gitleaks_push3.out`, `gitleaks_push3.json` and `gitleaks.out` (the earlier push's).
- **RESULTS.md:** lines 185–232 (`645bd3f`), 538–637 (`9464f61`), 725–790 (the close lines on `9189623`'s entry, including `18102d0`'s), 868–924 (`8e3bf91`), 925–978 (`e5aba51`) and 1325–1345 (inside the 2026-11-15 entry at 1255).
- **Counts only, by grep,** over three committed Code blocks: the n-ganl prebuild, the n-build STOP and the n-schema questions.

**Commands**
- `shasum -a 256` and `wc -c` on the four placed files.
- `git rev-list --count` on both ranges.
- `git log` (ids, subjects, commit times), including `-3 origin/main`.
- `git reflog` of `origin/main` (ids and subjects).
- `git show --name-only e5aba51`, and `git show e5aba51 -- RESULTS.md` piped to grep.
- One pickaxe, scoped `-- RESULTS.md`.
- `git status --porcelain` scoped to five named paths.
- `ls data/n` (name only).
- `which -a gitleaks` and `gitleaks version`.

**Tools:** Bash only: cat, sed, awk (as a text utility), tr, cut, head, sort, uniq, `/usr/bin/grep`, shasum, wc, ls, git, which, and gitleaks for its version only.
- I ran no Python, JXA or other interpreter.
- I edited and wrote nothing, in the repository or anywhere else.
- I listed and read nothing under `data/mf3`. I read, listed and sized nothing under any `data/*/ckpt` or `data/*/reports`.
- No whole-tree status, no `--stat`/`--numstat`, no contact with the pod.

**State:** `origin/main` = HEAD = `bedc198`. RESULTS.md is clean. The four placed files are untracked.

**Disclosures** (none touches data/):
- (a) I printed the first 300 characters of `c7-commit/gitleaks.json`, the earlier push's raw gitleaks report, which is not a listed source. That showed one finding's rule, description, line/column numbers and a redacted match context. A grep count shows that finding's file is outside every ckpt and reports directory.
- (b) A grep over `c7-commit/screen3.py` for `sha|64|digest|hex` printed one line of the screen's pattern table that holds pod-value literals (a port and a proxy-user token). I do not repeat them here.
- (c) `ls -l` on six scratch files in c7-commit printed their sizes and times. These are scratch files only.
- (d) The pickaxe `git log -1 -S'<full sha256>' -- RESULTS.md` used a positive pathspec, RESULTS.md only. That is not one of item 3's listed exclusion forms, so I disclose it.

**Hashes, by tool:**
- The draft hashes match my `shasum` output by exact 64-character string match, and they match the paste block:
  - `aea918c5…0395`, 11,583 B
  - `a4980152…151a`, 18,342 B
  - `ff2e5d89…ebec`, 11,146 B
- The sizes match `wc -c`.
- ADDENDUM-n1, which the drafts do not cite, also matches PB:11: `e979f8f2…5e03`, 15,804 B.

**Abbreviations:**
- PB = paste_block.txt
- RC = the p-verdicts-counters raw
- RB = the n-build raw
- RG = the n-ganl raw
- AD = ADDENDUM-n1
- R = RESULTS.md
- S2 / S3 = screen_push2 / screen_push3
- G3 = gitleaks_push3.out

### Draft 1: close_e5aba51.md

1. "PI date 2026-11-16, second sitting": **CONFIRMED.** PB:1; RC:3.
2. "the coordinating session's line, per the p-counters raw's header": **CONFIRMED.** RC:3, "…the dpo VERDICTS session and the coordinating session add their close lines".
3. "its §6, items 5–6": **CONFIRMED.** RC:61–63.
4. "The seat's answers of 2026-11-16 (second sitting)": **CONFIRMED.** RC:3.
5. Link name and path: **CONFIRMED.** The file is present; PB:4.
6. sha256 `aea918c5…0395`: **CONFIRMED.** Exact match; PB:5.
7. 11,583 bytes: **CONFIRMED.** `wc -c` gives 11583; PB:5.
8. "are committed by path here": **NOT CHECKABLE** (this commit).
9. "re-hashed equal to the paste block's figures": **CONFIRMED.** My re-hash.
10. "Their section C rules on this note": **CONFIRMED.** RC:43, RC:10.
11. The PI's word, verbatim "Route as given": **CONFIRMED.** PB:31.
12. "(PI date 2026-11-16, second sitting)" for the paste block: **CONFIRMED.** PB:1.
13. "The block's item 11, verbatim" and the quoted line: **CONFIRMED, character for character.** PB:28, compared as an exact line.
14. C.1: the first pass's halt, cleared by my own re-run, inert, no strike: **CONFIRMED.** RC:45; R:949.
15. C.1: "From here a halt … goes to the seat with the re-run beside it … and the seat clears it": **CONFIRMED** as a paraphrase of RC:45 (see O-5).
16. C.2: the shape class I printed for the three matches inside `data/mf3/reports` is inert: **CONFIRMED.** RC:46; R:951–952.
17. C.2: item 4 amended, with the quoted rule: **CONFIRMED, character for character.** RC:46.
18. C.3: the matches are sha256 digests by the reports' own schema, false positives by class: **CONFIRMED** as a compression of RC:47.
19. C.3: "Push, with a note" stands as the push's word: **CONFIRMED.** RC:47.
20. C.3: "From here the screen classifies … stays a halt.": **CONFIRMED, word for word.** RC:47.
21. C.3: "The screen takes this rule before the next push.": **NOT CHECKABLE.** It is the session's own plan and is not in RC's C.3 (see O-2).
22. C.4: this note's form is the standing rule while Q-F3's campaign runs: **CONFIRMED.** RC:48; R:964–965.
23. C.4: on the box … or after the campaign, never on the laptop meanwhile: **CONFIRMED.** RC:48.
24. C.4: the window rule for a p VERDICTS run stands as written: **CONFIRMED.** RC:48; R:970–972.
25. "C.5, the two later pushes, one line each": **CONFIRMED.** RC:49. The reflog of `origin/main` shows 16c99d5 → fa27c45 → 645bd3f → bedc198, each "update by push".
26. Range `fa27c45..645bd3f`: **CONFIRMED.** S2:1; RC:49; reflog.
27. 13 commits: **CONFIRMED.** `rev-list --count` gives 13; S2:1.
28. "Yes, push first": **NOT CHECKABLE** (said in chat). It fits R:630–631, which holds the runs for the PI's answer on a push first.
29. Every class CLEAR but `port`: **CONFIRMED.** S2:2–8.
30. The one port match outside, `port 22`, in this note's own text: **CONFIRMED.** S2:5–6 ("1 distinct … READ"; "port 22 at RESULTS.md@e5aba51"). `git show e5aba51` puts it in the note's "container port 22/tcp" (R:937).
31. Nothing inside `ckpt` or `reports`: **CONFIRMED.** S2:2–9.
32. "gitleaks 8.30.1": **CONFIRMED indirectly.** S2 prints no version. The only gitleaks on PATH is `<prefix>/bin/gitleaks`, and it reports 8.30.1. R:939 names 8.30.1 for the earlier push (see O-4).
33. "0 findings": **CONFIRMED.** S2:9.
34. "no halt": **CONFIRMED.** S2.
35. Range `645bd3f..bedc198`: **CONFIRMED.** S3:1; reflog.
36. 1 commit: **CONFIRMED.** `rev-list --count` gives 1; S3:1; G3:1.
37. "Push it": **NOT CHECKABLE** (said in chat).
38. Every class CLEAR: **CONFIRMED.** S3:2–7.
39. "gitleaks 8.30.1": **CONFIRMED indirectly**, as in 32.
40. "no leaks": **CONFIRMED.** G3:3 "no leaks found"; the json is `[]`.
41. "no halt": **CONFIRMED.**
42. "The raw's section B" (the label): **IMPRECISE.** See the fixes below.
43. B relayed verbatim to dpo, and in substance to instruct and sft: **NOT CHECKABLE** (relays).
44. The dpo session does the counters for the three units: **CONFIRMED.** RC:55; PB:13; R:541, R:552–553.
45. The briefs amended "as the raw's §2.2 words it", with the quote "each unit's three checkpoints and three call logs": **CONFIRMED verbatim.** RC:26; RC:62; PB:27.
46. "the counters step alone reads …, by exact path, never a listing, for the counts the record names": **CONFIRMED** in substance. It is the briefs' second sentence (R:773–774) as amended by RC:26. "never a listing" comes from RC:28 (§2.3).
47. After the counters raw, each session commits its own unit's outputs, secondary, raws and entries: **CONFIRMED.** RC:35–36; the standing division at R:731–732; R:635 (see O-6).
48. The dpo session adds its close line on `9464f61`'s entry: **CONFIRMED.** RC:3, RC:59; PB:17 (see O-7).
49. "with ledger (76)": **CONFIRMED.** RC:39–41, RC:59.

### Draft 2: close_645bd3f.md

1. The PI date: **CONFIRMED.** PB:1; RB:3.
2. The coordinating session's line per the n-build raw's header: **CONFIRMED.** RB:3.
3. "§6, items 6–7": **CONFIRMED.** RB:77–79.
4. The seat's answers of 2026-11-16 (second sitting): **CONFIRMED.** RB:3.
5. Link and path: **CONFIRMED.** PB:6.
6. sha256 `a4980152…151a`: **CONFIRMED.** Exact match; PB:7.
7. 18,342 bytes: **CONFIRMED.**
8. "committed by path here": **NOT CHECKABLE.**
9. "re-hashed equal": **CONFIRMED.**
10. "They answer this block and `718c48e`'s": **CONFIRMED.** RB:3.
11. STOP Q1 (b): **CONFIRMED.** RB:7, 14.
12. Q2, BK's form: **CONFIRMED.** RB:8, 27.
13. Schema Q1 (a): **CONFIRMED.** RB:9, 31.
14. "Q2 struck": **CONFIRMED.** RB:9, 33; PB:23.
15. Q3 (a): **CONFIRMED.** RB:9, 35.
16. "Q4 the comparison": **CONFIRMED.** RB:9, 37.
17. "Q5 the band": **CONFIRMED.** RB:9, 39–44.
18. "the flagged readings accepted, three amended", listed as answering these two blocks: **IMPRECISE.** See the fixes below.
19. Ledger (77)–(79): **CONFIRMED.** RB:52–56.
20. "Route as given": **CONFIRMED.** PB:31.
21. Decisions (n-1) and (n-2) are the paste block's items 5 and 6, [adopt]: **CONFIRMED.** PB:20–21; AD:82.
22. "recorded in ADDENDUM-n1 v0.1's own commit": **NOT CHECKABLE** (future). It is consistent with AD:84, §8.3 (2), "the PI's routing quoted verbatim".
23. That commit follows the referent check "(its §8.4)": **CONFIRMED.** PB:27; AD:84, 86. RB:78 says "its §8".
24. And it comes before LOCK-n v0.1: **CONFIRMED.** PB:27; RB:64, 78.
25. Items 7 and 8 relayed verbatim to n-build: **NOT CHECKABLE** (relay). They are n-build's items: PB:22–23.
26. "the raw's own items 1 and 4 to the pod session": **CONFIRMED** as the raw's own words, RB:70 "(and the pod session for items 1 and 4)". The relay itself is not checkable (see O-1).
27. The quotation "a download only on a failed check — yours": **CONFIRMED, character for character.** PB:22; RB:71.
28. "is the PI's": **CONFIRMED** in substance. RB:23 "on the PI's word"; AD:28 (see O-9).
29. A download only if a check of the two small files against the manifest fails, then on the PI's word: **CONFIRMED.** RB:23; AD:28; PB:22.
30. "Relayed with them": **NOT CHECKABLE** (relay).
31. The quotation "Nothing of it runs before Code's commit (rules 9 and 11)": **CONFIRMED, character for character.** AD:4.
32. The render, the copy and the comparison wait for ADDENDUM-n1's commit: **CONFIRMED.** AD:4 with AD:84 (§8.3: the commit at (2), before n-build's ids at (3) and §2's check at (5)). The copy is AD:28 (see O-8).
33. "Item 12, noted": **CONFIRMED.** PB:29.
34. `data/n` holds only `bk`: **CONFIRMED.** `ls data/n` gives `bk`; PB:29; RB:79.
35. The acceptance check when the parts land, "as routed on 2026-11-15": **CONFIRMED.** PB:29; R:1339–1340, inside the 2026-11-15 entry at R:1255.
36. n-build adds close lines here and on `718c48e`'s entry: **CONFIRMED.** RB:75; PB:23.
37. "the pod session adds one here": **NOT CHECKABLE** as to which entry. RB:3 names the pod session among those adding close lines, but no entry.

### Draft 3: close_8e3bf91.md

1. The PI date: **CONFIRMED.** PB:1; RG:3.
2. The coordinating session's line per the n-ganl raw's header: **CONFIRMED.** RG:3.
3. The seat's answers of 2026-11-16 (second sitting): **CONFIRMED.** RG:3.
4. Link and path: **CONFIRMED.** PB:8.
5. sha256 `ff2e5d89…ebec`: **CONFIRMED.** Exact match; PB:9.
6. 11,146 bytes: **CONFIRMED.**
7. "committed by path here": **NOT CHECKABLE.**
8. "re-hashed equal": **CONFIRMED.**
9. "They answer this block": **CONFIRMED.** RG:3.
10. Q1 (b), through the origin: **CONFIRMED.** RG:9, 66.
11. Q9 (a), through the origin: **CONFIRMED.** RG:17, 44, 66.
12. Q2 (c): **CONFIRMED.** RG:10, 67.
13. Q3 (a) with A.6: **CONFIRMED.** RG:11, 68.
14. Q4 and Q5 confirmed: **CONFIRMED.** RG:12–13, 68.
15. Q6 (a) amended for N1-P: **CONFIRMED.** RG:14, 33, 68.
16. "Q7 decided for the cap": **IMPRECISE.** See the fixes below.
17. Q8 Appendix A with the amendments: **CONFIRMED.** RG:16, 68; PB:24.
18. The block's §3 readings accepted: **CONFIRMED.** RG:48, 69.
19. PIN-n-20 to -26, with -12 and -16 as amended, accepted, listed under "They answer this block": **IMPRECISE.** See the fixes below.
20. "Route as given": **CONFIRMED.** PB:31.
21. "Its item 9" is n-analyzer's: **CONFIRMED.** PB:24.
22. Relayed verbatim with items 5 and 6: **NOT CHECKABLE** (relay).
23. "nothing it defines runs before its commit": **CONFIRMED** as a paraphrase of AD:4.
24. "so is the addendum's hold" (relayed): **NOT CHECKABLE** (relay).
25. The n-analyzer session adds its close line here: **CONFIRMED.** RG:3, 58, 70; PB:24.

### Totals

| Draft | Claims | CONFIRMED | IMPRECISE | FAIL | NOT CHECKABLE |
|---|---|---|---|---|---|
| close_e5aba51 | 49 | 43 | 1 | 0 | 5 |
| close_645bd3f | 37 | 31 | 1 | 0 | 5 |
| close_8e3bf91 | 25 | 20 | 2 | 0 | 3 |
| **All** | **111** | **94** | **4** | **0** | **13** |

### IMPRECISE items and fixes (no FAIL)

- **Draft 1, claim 42: "The raw's section B".**
  - **Source:** the raw has no section B. Its B is a block inside its §6 routing block (RC:55, "**B. p (the dpo VERDICTS session, for the three units)**"). Its "Section C" (RC:10, 43) is top-level. The B the PI routed is the paste block's section B (PB:13–17), which RESULTS.md has called "The block's section B" (R:545) and "Section B" (R:729).
  - **Fix:** "**The paste block's section B (the raw's §6 block B), and the raw's §6 item 5:** section B is relayed verbatim…". If it was the raw's text that was relayed, say "the raw's §6 block B" instead.
- **Draft 2, claim 18: "They answer this block and `718c48e`'s: …; the flagged readings accepted, three amended".**
  - **Source:** RB:10, "The flagged readings of `5a97527` and `14e65d8` are accepted as §3 lists them, three amended" (RB:48–50). `645bd3f`'s own "Code's readings" are its Q1 and Q2 (R:205–208).
  - **Fix:** "…; the flagged readings of `5a97527` and `14e65d8` accepted, three amended; …".
- **Draft 3, claim 16: "Q7 decided for the cap".**
  - **Source:** RG:68 (= PB:24), "Q7 the f = 0.10 decision when the cap binds"; RG:35, "Q7 — decided now, conditionally".
  - **Fix:** "Q7 the f = 0.10 decision when the cap binds".
- **Draft 3, claim 19: the PINs listed under "They answer this block".**
  - **Source:** the PINs are registered by `5c0ae6b` and `bedc198` (RG:3, 49–50). The `8e3bf91` block names no PIN (grep count 0).
  - **Fix:** "…; the block's §3 readings, and PIN-n-20 to -26 with -12 and -16 as amended (registered at `5c0ae6b` and `bedc198`), accepted."

### Observations (no verdict)

- **O-1 (draft 2, claim 26; the one that matters most).** "the raw's own items 1 and 4" copies RB:70's words, but the numbering is ambiguous.
  - In RB §6, item 4 is the flagged readings (with the pause precedence and the cap clause).
  - In RB §5 ("the pod session where named", RB:58), item 1 is the small files and the render, and item 4 is "The BACKEND extension on the box, then §2.4's comparison" (RB:63). That is the plainest box work in the raw.
  - Name the section in the line. Whichever was meant, check that the pod session's relay covers the §5 item 4 comparison.
- **O-2 (draft 1, claim 21).** "The screen takes this rule before the next push." sits inside a bullet that otherwise restates the seat's C.3, and RC:47 does not say it. Mark it as the session's own plan. `screen3.py` has no 64-hex/sha rule and no gitleaks call, so the rule belongs wherever the gitleaks classification lives. I did not look for that code.
- **O-3 (C.5, first line).** The close line repeats `port 22`, so the next pre-push screen will match it again in RESULTS.md (outside the protected directories, so a READ, not a halt). That is harmless but worth expecting. Alternatively, name the port without the literal. Saying that the range includes `e5aba51` itself would make "this note's own text" clear on its face.
- **O-4 (C.5, both lines).** Neither run's output records gitleaks's version. If the record should carry it from the run itself, the screen could print `gitleaks version` into its output.
- **O-5 (C.1).** The seat's form ends "the seat clears it, in a line" (RC:45). The draft drops "in a line".
- **O-6 (draft 1, last bullet).**
  - (i) RC:55 puts items 1–4 under "(the dpo VERDICTS session, for the three units)", and item 4 includes the outputs and "the three entries". Saying the per-session split follows `18102d0`'s division (R:729–732, R:635) keeps it from reading as a departure from B's heading.
  - (ii) The paste block's B differs from the raw's B in a few words: item 1 reads "task_correct over every stage" against "every stage", and item 4 reads "citing the raw" against "citing this raw", plus spacing and backticks. Name which text was relayed verbatim.
  - (iii) "its own unit's … entries": there is one entry per unit (RC:36, "the three entries").
- **O-7 (drafts 1 and 3).** The raws say "close lines", plural (RC:59; RG:58, 70). The drafts give one line per session. That is consistent with the headers (RC:3, RG:3); I note the plural only.
- **O-8 (draft 2, claim 32).** RB §5 lists the addendum's commit at item 5 ("before LOCK-n v0.1"), after the copy and render at item 1 (RB:60, 64). AD:4 and AD §8.3 (AD:84) put the commit first, and the draft rightly follows the addendum. Citing §8.3 beside the quotation would show a reader of RB why the render waits.
- **O-9 (draft 2, claim 28).** "is the PI's" can read as authorship of the bracket, which is the seat's default, adopted by "Route as given". "leaves the download to the PI" says what is meant.
- **O-10 (drafts 2 and 3).** Draft 2 quotes the hold verbatim and draft 3 paraphrases it; one form in both would be cleaner. The relay to n-analyzer also does not say whether its model-free battery runs on §7's changes count as "runs" under the hold (RG:56–58).
- **O-11 (draft 1).** p's routing (block B and the briefs) is recorded in the close line on the push note's entry. The dpo session's close line on `9464f61`'s entry will cite the raw, so a pointer is optional.
- **O-12.** Full sha256s in this "(sha256 `…`, N bytes)" form were already added within push 2's range: three occurrences of one hash, the latest at `9464f61`. That push's gitleaks reported 0 findings, so no new exposure is expected.

## 2. Code's dispositions

Every IMPRECISE item is applied in the checker's terms, and so are nine of the twelve observations.

- **Draft 1, claim 42:** applied. The bullet now opens "The paste block's section B (the raw's §6 block B), and the raw's §6 item 5:", and it names the paste block's section B as the text relayed verbatim (O-6 (ii)).
- **Draft 2, claim 18:** applied. "the flagged readings of `5a97527` and `14e65d8` accepted, three amended".
- **Draft 3, claim 16:** applied. "Q7 the f = 0.10 decision when the cap binds".
- **Draft 3, claim 19:** applied. The PINs move out of what the raw answers into what it accepts: "They accept the block's §3 readings, and PIN-n-20 to -26 with -12 and -16 as amended (registered at `5c0ae6b` and `bedc198`)."
- **O-1:** applied. The line now names the box work of the raw's §5 items 1 and 4 and records, as an observation for the seat, that the §6 header's "items 1 and 4" fits §5's numbering, §6's own item 4 being the flagged readings. The pod session had raised the same point and reads it the same way. The relay to the pod session already covered §5 item 4 (the BACKEND extension with §2.4's comparison, later).
- **O-2:** applied. The sentence is marked as my plan, and it names the screen's gitleaks classification as what takes the rule.
- **O-3:** applied. The close line names "the container port this note's own text declares, the range holding `e5aba51`", without the literal. This raw quotes the checker's report whole, so the next pre-push screen will read its `port` matches here, outside the protected directories.
- **O-4:** applied in the text: the C.5 bullet says the version is 8.30.1, the one on the laptop's path, and that the runs' outputs do not print it. My plan: the screen prints gitleaks's version from the next push on.
- **O-5:** applied. "and the seat clears it, in a line".
- **O-6 (i):** applied. The line says the per-session split is "the division `18102d0`'s close line records". **(ii):** applied, as for claim 42. **(iii):** kept, with its source: each unit's entries are "`— VERDICTS` and `— secondary DVs`, as routed on 2026-11-15" (that routing's section B item 6, quoted in `9189623`'s entry). The seat's "the three entries" is read as the three VERDICTS entries; the seat may say otherwise.
- **O-7:** noted; one line per session, as the headers have it.
- **O-8:** applied. The hold's quotation is followed by "Its §8.3 puts that commit before n-build's ids."
- **O-9:** applied. "leaves the download to the PI".
- **O-10:** applied. Both lines quote the hold verbatim. My reading of it, as relayed to the n sessions, is stated for the seat in the line on `645bd3f`'s entry: battery runs of drafts on synthetic data, in a window, are development, not the addendum running.
- **O-11:** not acted on; the dpo session's close line on `9464f61`'s entry cites the raw.
- **O-12:** noted.
- **The checker's disclosures (a)–(d)** are recorded here for the seat (list v2 item 8), as the checker gave them. None touched `data/`. For (b), the pod values are not repeated here. For (d), the pickaxe's positive pathspec named RESULTS.md alone, so no checkpoint or report could match.

The edits after the check were checked by tool. A `diff` of each checked draft against its final text shows these changes and nothing else. Seven quotations were counted in their sources with `/usr/bin/grep -c -F`, each found once except the 2026-11-15 routing's words, found twice in RESULTS.md: "(and the pod session for items 1 and 4)" and "a download only on a failed check — yours" in the n-build raw, "Nothing of it runs before Code's commit (rules 9 and 11)" in ADDENDUM-n1, "each unit's three checkpoints and three call logs" and "the seat clears it, in a line" in the p-counters raw, and "VERDICTS and — secondary DVs, fresh sessions" and "commits its own outputs and entries" in RESULTS.md. There was no second blind pass.
