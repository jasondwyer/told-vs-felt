# n — the corpus's acceptance check: the blind values-check, as returned, with every disposition

PI date 2026-11-17. Code (the n-build session).

**What was checked.** One blind pass by a subagent over two drafts: the entry (sha256 `88e49cf9…40a1`) and the
acceptance raw (`8a9842b2…879a`, its hand-written head `7667f939…59b8`). It covered the raw's hand-written sections
§1–§5 and checked §2's readings against the script.

**The checker's brief:**
- named the sources;
- quoted the PI's block of 2026-11-17 and the coordinating session's item 4, verbatim;
- quoted the list of record v2's items 1–5, verbatim;
- barred any interpreter (the battery window was closed), any guard marker in an argv, anything under `data/mf3`,
  and any write.

**The report.** It is in §3 below, extracted verbatim from the subagent's hand-back by `jq` (149 lines, sha256
`de321a96…5123`). It writes `<scratch>` and `<repo>` for the local roots.

**Totals:** 102 items — 76 CONFIRMED, 7 IMPRECISE, 1 FAIL, 18 NOT CHECKABLE — and 11 observations.

## 1. Dispositions

**The IMPRECISE items and the FAIL, all applied:**
- **27** (entry, the G-VEC mapping). Applied as Code's proposal, per observation 4: "Code proposes that G-VEC's
  wiring, when built, map the one to the other, with no corpus edit".
- **52** (raw §1, the Python runs). Applied in the checker's words.
- **57** (raw §1, the exploration's fields). Applied in the checker's words.
- **61** (raw §1, the self-test's coverage). Applied in the checker's words.
- **84** (raw §2, CR9). Applied in the checker's words.
- **89, FAIL** (raw §3, the naming). Applied in the checker's words. Code confirmed that the record's §2 (its line 17)
  writes "flow engagement".
- **92** (raw §3, the G-VEC mapping). Applied as Code's proposal, as 27.
- **98** (raw §4, the venv call). Applied in the checker's words. "A guard marker" is now "two guard markers", per its
  item 97.

**The observations:**
1. **Z1.** Applied: raw §3 item 3 and the entry's observations.
2. **gravel.** Applied after Code's own check. `grep -w` over `data/n/passages.jsonl` gives the same six ids, and
   `results/raw/2026-08-09_e2a_g1.txt:3` and `archive/RESULTS-cycles3-4.md:922` read as the checker quotes them. In the
   raw it sits in the RESULT block (for the seat's ruling), in §2 CR6 and in §3 item 2; in the entry, in its first
   bullet.
3. **The validator's exit status.** Applied: raw §1, run 5.
4. **The G-VEC mapping as Code's proposal.** Applied (27, 92).
5. **passage_spans.** Applied with 57.
6. **CR9 and the docstring's G9 line.** Noted. The script stands verbatim as run and is not edited; CR9 now states what
   the code does (84).
7. **The 2026-11-16 routing's item 12.** Applied: the raw's head quotes it; Code read the line.
8. **N.2.** Applied. The raw's §5 quotes "re-hashing each first". Its §3 item 7 adds that the validator reads `ROOT`
   only in its recover mode, and that a push carries the path. The entry's commit bullet says "re-hashing each first".
9. **The unsaved outputs.** Applied. The raw's §1 says the outputs of runs 1–3 were not saved, and that the lines it
   transcribes come from the session's tool output. `explore_bk.py` is verbatim in a new §9.
10. **neutral-71, the only one.** Applied: raw §3 item 6 and the entry.
11. **The run numbering.** Applied: the raw's runs are now 1–5, as the entry's are.

**The NOT CHECKABLE items (18).** They rest on Code's own runs and the coordinating session's window; no change. Item 6,
the raw's link, is checked at the commit, which places the raw under that name.

## 2. The edits after the check, checked by tool

- A full `diff` of the raw's hand-written head and of the entry against the checked drafts holds only the dispositions
  above. It also holds one wording edit of Code's own: §3 item 2's sentence now opens "The token gravel". Code read the
  diff in full.
- The raw's body after its head is unchanged except for the appended §9.
- Each verbatim section, §6–§9, equals its source file (extracted by `awk`, compared by `cmp`).
- The final raw: sha256 `2fac6fd0…3c05`, 1,025 lines. The final entry: sha256 `e1dae65f…7d2c`, 74 lines.

## 3. The report as returned

```text
VALUES-CHECK — n corpus acceptance: ENTRY (<scratch>/corpus/entry.md) and RAW §1–§5 (<scratch>/corpus/raw.md), with RAW §2's CR1–CR10 checked against the §8 script. Blind, read-only. Tools used: shasum, wc, grep, git grep, awk, sed, sort, comm, cmp, diff, a name-only ls, git status on three named paths, a pruned find, and the Read tool. No interpreter was run. No argv carried a guard marker: marker folders were reached by cd plus a glob, and their names were printed only by shell builtins. Nothing under data/mf3 or any ckpt/reports path was touched, and no file was written.

The verbatim sections match their sources. RAW §6 equals <scratch>/corpus/out/check_run.txt (diff empty, 174 lines). RAW §7 equals out/seat_validate_run.txt (diff empty). RAW §8 equals <scratch>/corpus/corpus_check.py (diff empty, 603 lines, sha256 3db93584…36f6, the same as out/check_script.sha256). out/check_run.exit and out/seat_validate_run.exit both read 0.

ENTRY
1. ENTRY header — "PROPOSAL-n v0.2 §0.8 Route B, §3 G-VEC" — CONFIRMED — <repo>/PROPOSAL-n-bk-reconciliation-v0_2.md:2 (v0.2), :36 (**0.8**, "Route B (the default, run regardless)"), :105 (## §3 Gates), :111 (**G-VEC.**).
2. ENTRY header — "the seat's answers of 2026-11-15, §5.3, the PI's item 11" — CONFIRMED — results/raw/2026-11-15_campaign-go-p1-n-spinup_design-to-code_answers.md:64 (**5.3 The corpus**), :96 (## 10. Routing block for the PI), :117 ("11. The corpus's acceptance check and assembly when the parts land (§5.3) [go].").
3. ENTRY header — "the PI's routing of 2026-11-17, N.1 and N.3, "route as given"" — CONFIRMED — the PI's block: header PI date 2026-11-17, items 1 and 3, "route as given".
4. ENTRY header — "every gate PASS, not a STOP" — CONFIRMED — RAW §6: G1–G9 all PASS; out/check_run.exit is 0.
5. ENTRY header — "assembled in the brief's order: 544 lines, 157,520 bytes, sha256 ef6b00dc…3cc3, the block's expected file" — CONFIRMED — shasum, wc -l and wc -c of data/n/passages.jsonl, diffed by tool against the block. A cat of the nine parts in the record's order, piped to cmp against the file: equal (for the order, see 82).
6. ENTRY header — raw link results/raw/2026-11-17_n-corpus_acceptance.md — NOT CHECKABLE — results/raw has no 2026-11-17 file yet. Check the name when the raw is placed.
7. ENTRY inputs — "nine part files under data/n/passages.parts/ and its prompt record … placed untracked" — CONFIRMED — ls -A lists exactly the nine names. git ls-files on the three paths: 0. git status --porcelain --ignored: !! for each.
8. ENTRY inputs — "BK's 160 session records (data/n/bk)" — CONFIRMED — 14 *.sessions.jsonl files in data/n/bk/…/skeletons/<the one folder>/neutral/; wc -l total 160 (8 files × 5 + 6 × 20).
9. ENTRY inputs — "the two rosters of record" — CONFIRMED — valence_core/e2d/config.py:9 ("ROSTER OF RECORD = the h-roster"), :36–37. LOCK-g.md:22 "Roster of record" (quartz/velvet, copper/walnut, maple/saddle, amber/granite) equals data/olmo/a1_repair_roster.json:2304 selected_tags.
10. ENTRY — "Model-free: the standard library only, no model and no tokenizer" — CONFIRMED — imports are standard library only: corpus_check.py:52–62, explore_bk.py:3–6, validate.py (sys, re, json, hashlib, collections, os).
11. ENTRY G1 — "The prompt record (323cf9d8…44b5, 18,167 bytes) equals the PI's block, and so do its §4 table, its stated order and its stated concatenation. Each part's sha256, bytes and lines equal them." — CONFIRMED — shasum and wc -c of the record. Record :35–43 table, sed-extracted and diffed against the block: equal. Record :45 gives the stated order and "**544 lines, 157,520 bytes, sha256 `ef6b00dc…3cc3`**". The nine parts' sha256, bytes and lines, diffed against the block: equal.
12. ENTRY G2/G3 — "544 lines … 544 distinct ids" — CONFIRMED — wc -l gives 544. The id field has 544 unique values and 0 duplicates.
13. ENTRY G4 — "56 for each of the eight states and 96 neutral; every line parses, with its file's state and that state's pole" — CONFIRMED — all 544 lines match ^{"id": …, "state": …, "pole": "[-+0]", "text": "[^"\\]*"}$. Per part, awk finds 0 misses: ids <stem>-NN from 00, state equal to the stem, pole as declared for the state.
14. ENTRY G5 — "every text 2–4 sentences by the declared splitter (whitespace after ".", "!" or "?")" — CONFIRMED — awk counts the whitespace runs after [.!?], plus 1: 3 for all 544.
15. ENTRY G6 — "1,632 sentences, 1,632 distinct after normalization, none shared" — CONFIRMED — awk split plus §8's normalization: 1632 sentences, 1632 after sort -u.
16. ENTRY G7 — "none of BK's twelve zone labels (B8, D7, H0, K7, L4, M2, N1, Q3, R9, T5, V3, W6), by code or by full label" — CONFIRMED — cue_S and cue_U each carry exactly these twelve (320 values = 2 × 160). A case-insensitive grep over the 544 texts, with no letter or digit adjacent: 0.
17. ENTRY G8 — "none of the twelve roster tokens …, plurals included" — CONFIRMED — grep -i -E '(^|[^A-Za-z0-9])(granite|…|amber)(e?s)?([^A-Za-z0-9]|$)' over the texts: 0.
18. ENTRY G9 — "the nine parts concatenated … equal the block's expected file. The file was written once, by exclusive create, then read back equal. A shell cat … same sha256." — CONFIRMED — corpus_check.py:407–420: the write happens only if no gate failed, uses open(OUT, "xb"), then re-reads and compares. §6 prints "written, read back … = the block's expected file". My cat gives ef6b00dc…3cc3. "Once" rests on the author's run; the refusal at :351–352 bars a second write while the file exists.
19. ENTRY per-state — "Every passage has three sentences (two/three/four: 0/544/0)" — CONFIRMED — as 14.
20. ENTRY per-state — "Words: 30–63, mean 44.3. The eight states' means run 41.4–49.4; neutral's is 38.3." — CONFIRMED — an awk recomputation (whitespace split, median by sort) reproduces every word column of §6. Serenity 41.4 is the lowest mean and frustration 49.4 the highest; neutral 38.3; all passages 30/44.0/44.3/63.
21. ENTRY per-state — "Characters: 161–304, mean 220.1" — CONFIRMED — same recomputation; the texts have no escapes, so the JSON length is the character count. All passages 161/221.0/220.1/304, and every row of §6 is reproduced.
22. ENTRY D5 — "eight hits, none a G8 match: "ridge" inside fridge, bridge or cartridge (six), "amber" inside chambers (one), and … cedar (serenity-17)" — CONFIRMED — awk over alphanumeric runs: contentment-05 and -14 fridge; relief-16, serenity-18 and neutral-18 bridge; neutral-53 cartridge; dread-53 chambers. serenity-17 has "the cedar ticks". lattice: 0. G8: 0.
23. ENTRY — "D1–D4 and D6 are 0. D6 is rule 18's check against BK's 1,920 session passages." — CONFIRMED — §6 shows 0 for each, and each is reproduced independently:
    - D1: the shape regex (key order, no quote or backslash), the ids, no CR, ASCII only, a final newline.
    - D2: no [.!?] before a non-space, every text ends in [.!?], every sentence opens on a capital.
    - D3: 1632 unique out of 1632.
    - D4: a grep for "zone" and for letter-digit tokens finds 0.
    - D6: comm -12 of the corpus's and BK's normalized sentences finds 0.
    1,920 = 160 records × 12: n_passages is 12 in all 160, and every record has exactly 14 '["Zone Xn", "' openers (12 history pairs, plus present, plus order).
24. ENTRY — "The seat's validator was extracted from the record (cc1fad61…f269, as stated) and run unedited on the laptop's bytes: PROBLEMS: 0" — CONFIRMED — awk between the record's two ``` fences, piped to shasum: cc1fad61…f269, 8889 bytes, the values stated at record :54. cmp: equal to <scratch>/corpus/seat/validate.py. out/seat_validate_run.txt reads "PROBLEMS: 0".
25. ENTRY obs — "the record's "mostly three", where every passage has three" — CONFIRMED — record :18 and :50 say "mostly three"; the count is 0/544/0.
26. ENTRY obs — "the corpus spells flow_engagement and the package "flow engagement" (directions.py)" — CONFIRMED — the state field reads flow_engagement in all 56 lines of that part; valence_core/n/directions.py:27.
27. ENTRY obs — "G-VEC's wiring maps the one to the other, with no corpus edit" — IMPRECISE — no such mapping exists yet. POSITIVE_STATES has no consumer in the tree, and scripts/n_sessions.py:26 says G-VEC is "wired at [its] own step". Accept: "G-VEC's wiring, when built, is to map the one to the other, with no corpus edit;".
28. ENTRY obs — "neutral-71 has the word "neutral" (a car's gear)" — CONFIRMED — its text says "put the car in neutral", and it is the only one of the 544 with the word.
29. ENTRY obs — "the record's validator sets ROOT to a local root that names the laptop's user" — CONFIRMED — record :72 (validate.py:16); it is the record's only home-directory path.
30. ENTRY — "Every tenth passage (lines 10, 20, …, 540; 54 passages) is printed in the raw's §6" — CONFIRMED — awk 'NR%10==0' over passages.jsonl, printed in §6's form and diffed against §6's sample block: empty. 54 lines.
31. ENTRY run — "One battery window, the coordinating session's of 2026-11-17, now closed" — NOT CHECKABLE — it is consistent with this check's brief, which says the window is closed.
32. ENTRY run — "Each run was nice -n 19 /usr/bin/python3 -I, in this order" — NOT CHECKABLE — Python 3.9.6 is in §6 line 1; the invocation and the order rest on the author's runs.
33. ENTRY run 1 — "an exploration of BK's records (no corpus line)" — CONFIRMED — explore_bk.py reads only the skeleton folder and an os.walk of data/n/bk.
34. ENTRY run 2 — "self-test, 35/35" (the 35) — CONFIRMED — selftest() has 35 chk( calls (grep -c, the def excluded).
35. ENTRY run 2 — that all 35 passed — NOT CHECKABLE — the self-test's output was not saved.
36. ENTRY run 3 — "its preflight, the record against the block (no part file)" — CONFIRMED — preflight() (:425–438) reads the record, BK's records and the rosters, and only tests whether OUT exists.
37. ENTRY run 4 — "the check of record, once, exit 0 (script sha256 3db93584…36f6, verbatim in the raw)" — CONFIRMED — shasum of the disk copy and of the awk-extracted §8 both give 3db93584…36f6; the §8 diff is empty; the exit file reads 0. "Once" rests on the run.
38. ENTRY run 5 — "the seat's validator" — CONFIRMED — out/seat_validate_run.txt (= RAW §7); exit file 0.
39. ENTRY departures — the four commands (ls data/olmo; a stray -c 1 of the venv interpreter; two python3 -c one-liners naming the OLMo roster files) — NOT CHECKABLE — only the folder-name part is checkable from the files (see 97).
40. ENTRY departures — "The last three ran outside nice -n 19." — NOT CHECKABLE.
41. ENTRY departures — "None touched data/mf3, a ckpt or reports path, the corpus or a model. … disclosed … at the time." — NOT CHECKABLE.
42. ENTRY commit — "the raw, the values-check raw and this entry … the nine parts, data/n/passages.jsonl and the prompt record stay untracked until N.2 … .gitignore's admit line as for data/n/ids/ … Not pushed." — CONFIRMED — this matches the relay's item 4 and the block's item 2. .gitignore:271 is "!/data/n/ids/", and the three paths are currently ignored by .gitignore:263 "/data/n/*". "Not pushed" describes the commit still to come.

RAW
43. RAW head — "PI date 2026-11-17 … items N.1 and N.3 … ("route as given")" — CONFIRMED — the block.
44. RAW head — "Code (the n-build session) … relayed by the coordinating session with a battery window" — NOT CHECKABLE.
45. RAW head — block items 1 and 3, "verbatim" — CONFIRMED — grep -x -F of each quoted line in raw.md: one match each.
46. RAW head — "§5.3 of results/raw/2026-11-15_…_answers.md (routed as that raw's item 11)" — CONFIRMED — :64 and :117.
47. RAW head — "The prompt record's §5 notes were read before the check was written." — NOT CHECKABLE.
48. RAW head — "Model-free: no model and no tokenizer loaded, the standard library only." — CONFIRMED — as 10.
49. RAW head — "Nothing under data/mf3, data/*/ckpt or data/*/reports was listed, opened or hashed." — NOT CHECKABLE — the three scripts name no such path, and a pruned find shows data/n/bk has no ckpt or reports directory. The claim, though, covers every command run.
50. RAW head — "No part file was edited." — CONFIRMED — all nine sha256, bytes and lines equal the block's values at placement.
51. RAW head — "RESULT: every gate PASS (G1–G9) … 544 lines, 157,520 bytes, sha256 ef6b00dc…3cc3 (full) … stays untracked (ignored) until N.2", and the pointers (§6, §3 and §6, §2) — CONFIRMED — §6; shasum and wc; git status !!; each pointer resolves.
52. RAW §1 — "One battery window. Every Python run was nice -n 19 /usr/bin/python3 -I (Python 3.9.6) on a script in Code's scratch, with no guard marker in any argv" — IMPRECISE — §4 lists three Python runs that were none of these: a venv interpreter with a guard marker in argv[0], and two -c one-liners naming data/olmo paths, none of them at nice -n 19. §4 itself says "Every later Python run is as §1 states". Python 3.9.6 is confirmed by §6 line 1. Accept: "One battery window. Every Python run listed below was `nice -n 19 /usr/bin/python3 -I` (Python 3.9.6) on a script in Code's scratch, with no guard marker in any argv, one at a time, in this order (the three interpreter calls of §4 were not, and are disclosed there):".
53. RAW §1 item 0 — "explore_bk.py (sha256 f3667fa6…8928)" — CONFIRMED — shasum of <scratch>/corpus/explore_bk.py.
54. RAW §1 item 0 — "before the check was written" — NOT CHECKABLE.
55. RAW §1 item 0 — "It read BK's 14 skeleton files and every text file under data/n/bk, and no corpus line." — CONFIRMED — explore_bk.py:8–16 reads the skeleton folder's *.sessions.jsonl. :43–50 walks data/n/bk, pruning ckpt/reports and skipping non-UTF-8 files. It names no corpus path.
56. RAW §1 item 0 — "It found 160 records" — CONFIRMED — wc -l gives 160.
57. RAW §1 item 0 — "the same twelve labels in each zone-bearing field (cue_S and cue_U, present, order, history, turn_spans)" — IMPRECISE — by grep, each listed field carries exactly the twelve. But the records have a sixth zone-bearing field, passage_spans, which explore_bk.py:23–33 does not tabulate (it also carries the same twelve). Accept: "the same twelve labels in each zone-bearing field it tabulated (cue_S and cue_U, present, order, history, turn_spans; it did not tabulate passage_spans, which also carries the twelve)".
58. RAW §1 item 0 — "no zone-shaped string ("Zone" and a letter-digit code) other than those twelve in any text file under data/n/bk" — CONFIRMED — git grep -I -o -E '[Zz]one[[:space:]]+[A-Za-z]{1,2}-?[0-9]{1,2}' -- data/n/bk ':!data/*/ckpt/**' ':!data/*/reports/**' returns exactly the twelve. data/n/bk holds 28 files, all tracked, and no ckpt/reports directory.
59. RAW §1 item 1 — "selftest: 35/35" (the 35) — CONFIRMED — as 34.
60. RAW §1 item 1 — "pass, exit 0" — NOT CHECKABLE.
61. RAW §1 item 1 — coverage: "the splitter and the matchers; a clean synthetic corpus …; each gate firing on its own planted defect; the descriptive counts firing with no gate; and the record parser on an agreeing record and on three single-defect records" — IMPRECISE — all true except "each gate … on its own planted defect". G2 is tested only together with G4 (:519, one removed neutral line, asserting "G2" in f and "G4" in f). Every other gate has a test where it fires alone; D1–D6 each have a test with f == []; the three single-defect records are the table, the record's own hash and the stated order. Accept: "each gate firing on a planted defect (G2 only together with G4, on one removed neutral line)".
62. RAW §1 item 1 — "It reads no repository file." — CONFIRMED — selftest() (:442–585) builds its parts, labels, BK set and records in memory. Every open, listdir and load_* call sits at :155–438.
63. RAW §1 item 2 — "--preflight: the prompt record against the block, BK's labels and the rosters, with no part file read" — CONFIRMED — as 36.
64. RAW §1 item 2 — the preflight output's values ("agrees"; the twelve labels; "7077 distinct BK passage sentences"; Qwen granite … walnut; OLMo amber … walnut) — CONFIRMED —
    - "agrees": the record equals the block (see 11).
    - The labels: see 16.
    - 7077: reproduced by awk over the 1,920 history passages (\uXXXX escapes mapped to a non-alphanumeric, then §8's splitter and normalization, then sort -u).
    - The two token lists are the sorted token sets of config.py:36–37 and a1_repair_roster.json:2304–2321.
    - Each line's format matches what preflight() prints.
65. RAW §1 item 2 — the capture itself ("output exists: False", exit 0) — NOT CHECKABLE — no output was saved. It is consistent with the run of record's exclusive create having succeeded.
66. RAW §1 item 3 — "the check of record, once: exit 0. Its output (174 lines) is verbatim in §6." — CONFIRMED — out/check_run.txt has 174 lines and its diff against §6 is empty; the exit file reads 0. "Once" rests on the run.
67. RAW §1 item 4 — "extracted from the prompt record's §6 by awk (the lines between its two code fences): cc1fad61…f269, 8,889 bytes, the values the record states" — CONFIRMED — the record has exactly two ``` lines; otherwise as 24.
68. RAW §1 item 4 — "ran unedited in its plain-file mode on the nine parts: exit 0, PROBLEMS: 0. Its output is verbatim in §7." — CONFIRMED — §7 equals out/seat_validate_run.txt. Its FILES rows equal the nine files' names, lines, bytes and sha256 (diff empty). The exit file reads 0; see observation 3.
69. RAW §1 shell — "a cat of the nine parts in the brief's order gives ef6b00dc…3cc3" — CONFIRMED — reproduced.
70. RAW §1 shell — "shasum … ef6b00dc…3cc3, its wc -l 544 and its wc -c 157,520" — CONFIRMED — reproduced.
71. RAW §1 shell — "git status --porcelain --ignored … gives !! for each" — CONFIRMED — reproduced; the parts folder shows as data/n/passages.parts/.
72. RAW §1 — "corpus_check.py, sha256 3db93584…36f6 (603 lines), verbatim in §8" — CONFIRMED — shasum and wc -l of the disk copy. §8 extracted by awk gives the same sha256, and its diff is empty.
73. RAW §1 — "the file has not changed since" — CONFIRMED — out/check_script.sha256, the current sha256 and §8's sha256 are the same.
74. RAW §1 — "Its sha256 was taken after the preflight and before the run of record" — NOT CHECKABLE.
75. RAW §2 CR1 — CONFIRMED —
    - record_checks() (:128–151) compares the record's own sha256 and bytes with BLOCK_PROMPT, its §4 rows (in ORDER, each sha, bytes and lines) with BLOCK, its stated order with ORDER, and its stated concatenation with EXPECT.
    - check() (:191–201) compares each part's digest with BLOCK and fails G1 on any other name in the folder; non-.jsonl names are included via :358–365.
    - ls -A shows nine names only.
76. RAW §2 CR2 — CONFIRMED — check() parses each line with json.loads and requires a dict whose keys are exactly {id, state, pole, text}, all strings, with state equal to the stem and pole equal to POLE[stem]. Any miss fails G4, and so does any per-state count other than COUNT.
77. RAW §2 CR3 — CONFIRMED — SPLIT_RX (:98) and split_sentences (:101–102) equal, character for character, the validator's SENT_SPLIT_RX and its split comprehension. D2's four conditions are in check(); §6 shows D2 0.
78. RAW §2 CR4 — CONFIRMED — norm_sentence (:105–106). Sentences are deduplicated within each passage (dict.fromkeys, :275), and G6 fires when two pids hold the same sentence (:303).
79. RAW §2 CR5 — CONFIRMED — load_bk() takes the labels from cue_S and cue_U and refuses unless there are 14 files, 160 records and 12 labels of the form "Zone [A-Z]\d". zone_rx (:257) matches the code with re.I and no letter or digit adjacent. word_zone and word_code (:259) feed D4; §6 shows D4 0.
80. RAW §2 CR6 — the reading, the two source files, "twelve tokens, read from those files; the record's list of twelve is the same set", the match rule and D5 — CONFIRMED —
    - load_roster() (:173–185) reads both files and refuses unless there are 8 + 8 tokens whose union is ROSTER_12.
    - check() is called with the declared ROSTER_12 (:371), which equals that union because of the refusal.
    - roster_rx (:258) matches the token plus an optional (e)s, case-insensitive, with no letter or digit adjacent.
    - D5 counts tokens inside longer words (:293–299) and the earlier tokens through earlier_rx (:260).
    - Record :20 lists the same twelve.
81. RAW §2 CR6 — "the earlier roster tokens lattice and cedar (e2a's pairs; the superseded OLMo selection, data/olmo/a1_roster.json)" — CONFIRMED — results/raw/2026-08-09_e2a_full.txt:5 gives the v3 roster (slate, prism), (maple, cedar), (granite, lattice), (plaza, saddle). a1_roster.json:173 has selected_tags [[maple, cedar]] and :179 "sufficient": false.
82. RAW §2 CR7 — "The brief sits in the project's docs, with no laptop copy. The order used is the one the prompt record's §4 states and the PI's block lists; the two are the same." — CONFIRMED — record :3 says "no laptop copy exists", and the answers raw :64 says "project docs". A pruned find over <repo> and <scratch> finds no copy of the brief. The script's ORDER (:64), record :45 and the block's listing order are the same.
83. RAW §2 CR8 — CONFIRMED — sample() takes range(10, len+1, 10) over 544 lines: lines 10 to 540, 54 passages.
84. RAW §2 CR9 — "Only when all of G1–G8 hold, by exclusive create; then re-read and compared. A failing gate would have left nothing written." — IMPRECISE — the write also requires G9's own pre-write test: `failed` covers every gate G1–G9 (:407), and G9's concatenation test runs in check() (:305–308). A failed read-back, which the docstring counts as part of G9, would leave the file written (:416–418, "WRITTEN BUT NOT VERIFIED"). Accept: "Only when G1–G8 hold and the nine parts' concatenation equals the block's expected file, by exclusive create; then re-read and compared. A gate failing before the write would have left nothing written; a failed read-back would have left the file in place, with a STOP."
85. RAW §2 CR10 — CONFIRMED — the descriptive counts never enter `failed`, and the validator ran as a separate step.
86. RAW §3 item 1 — the eight D5 hits by id — CONFIRMED — as 22.
87. RAW §3 item 1 — "D1–D4 and D6 are 0: no form defect, no splitter blind spot, no sentence repeated within a passage, neither the word "zone" nor any letter-digit token, and no corpus sentence among BK's 1,920 session passages (rule 18)" — CONFIRMED — as 23.
88. RAW §3 item 2 — "three sentences … 0/544/0. The record's §5 says "mostly three". Its own figure, 1,632 distinct sentences with none shared, is 544 × 3." — CONFIRMED — record :50 (§5) and :29 ("1,632 distinct sentences, none shared"); 544 × 3 = 1,632.
89. RAW §3 item 3 — "The corpus's state field spells flow_engagement, the file stem, as the record's working specification has it." — FAIL — the working specification (record §2, :17–21) writes "flow engagement" with a space (:17: "pole `+` for contentment, flow engagement, relief, serenity") and never spells the state field. The underscore form appears only in the record's §4 table (:36), its stated order (:45) and its validator's STATES (:73). Accept: "The corpus's `state` field spells `flow_engagement`, the file stem, as the record's §4 table, its stated order and its validator's `STATES` do (its §2 working specification writes "flow engagement")."
90. RAW §3 item 3 — "POSITIVE_STATES spells "flow engagement", BK §3.1's words" — CONFIRMED — directions.py:27. Record :9 gives BK §3.1's states as "contentment, flow engagement, relief, serenity", and PROPOSAL-n :36 refers to "the state names of BK §3.1".
91. RAW §3 item 3 — "Nothing consumes that tuple yet." — CONFIRMED — git grep, and grep -rn over valence_core, scripts and tests, find POSITIVE_STATES (and NEGATIVE_STATES) only at their definitions.
92. RAW §3 item 3 — "G-VEC's stage maps the one to the other in the package, with no corpus edit." — IMPRECISE — as 27: scripts/n_sessions.py:26, and no mapping code exists. Accept: "G-VEC's stage, when it is wired, is to map the one to the other in the package, with no corpus edit."
93. RAW §3 item 4 — "neutral-71 has the word "neutral" (a car's gear). The record's word lists bar no such word" — CONFIRMED — the neutral-71 text has it. Neither the record's §2 forbidden list (:18–21) nor the validator's STATE_WORDS or EVAL_WORDS include "neutral".
94. RAW §3 item 5 — "the prompt record's §6 validator sets ROOT to a local root that names the laptop's user (the record's line 72). Committed as placed, that path enters the repository." — CONFIRMED — record :72.
95. RAW §4 — "Before the check was written, four commands carried a guard marker … disclosed … at the time." — NOT CHECKABLE.
96. RAW §4 item 1 — "ls data/olmo: a name-only listing; no Python." — NOT CHECKABLE.
97. RAW §4 item 2 — "./jl*/.venv/bin/python … the expanded folder name (a guard marker) was in argv[0]" — CONFIRMED — at the repository root, jl* expands to one folder whose name carries two guard markers, and jl*/.venv/bin/python exists. Checked with shell builtins only.
98. RAW §4 item 2 — "It ran -c 1 only: no import, no model, stderr discarded. Not at nice -n 19." — IMPRECISE — the run itself cannot be checked, but "no import" cannot hold literally. Without -S, that interpreter's startup processes its site-packages hooks, and the venv holds _virtualenv.pth, whose one line is "import _virtualenv" (plus an editable-install .pth that only adds a path). Accept: "It ran `-c 1` only: no import in its code (interpreter startup ran the venv's site hooks, among them `_virtualenv.pth`'s `import _virtualenv`), no model, stderr discarded. Not at `nice -n 19`."
99. RAW §4 items 3 and 4 — "Two /usr/bin/python3 -I -c one-liners … named data/olmo/a1_repair_roster.json and data/olmo/a1_roster.json … keys and selected tags. Not at nice -n 19." — NOT CHECKABLE.
100. RAW §4 — "None touched data/mf3, a ckpt or reports path, the corpus or a model. Every later Python run is as §1 states." — NOT CHECKABLE.
101. RAW §5 — block item 2, "verbatim" — CONFIRMED — grep -x -F: one match.
102. RAW §5 — "Before G-VEC, ADDENDUM-n1 §1.2 (iv) renders the 544 as ids (gvec_passages.jsonl), and the 1,344 A3 contexts as a3_contexts.jsonl, by the procedure of (i)–(iii): in a battery window, at nice -n 19, one process." — CONFIRMED —
    - ADDENDUM-n1-rendering-of-record-and-gread-band-v0_1.md:22 has "(iv) `gvec_passages.jsonl` (the 544 of `data/n/passages.jsonl`) and `a3_contexts.jsonl` (the 1,344)", "(iv) and (v) when their texts exist, by the same procedure", and "a battery window at `nice -n 19`, one process".
    - :84 (8.3 (5)) has "(iv), (v) rendered before G-VEC and G-CAL-n".
    - PROPOSAL-n :81 takes the A3 axes from "the frozen 1,344-context corpus".

OBSERVATIONS
1. Z1. The record's §1 (:10) and its validator's comment (:80) name "Z1", from BK's paper transcripts, among the zone codes. Z1 is not one of the twelve labels in BK's records, and no "Zone Z1" occurs anywhere in data/n/bk. G7 bars only the twelve; D4 (any letter-digit token) is 0, so Z1 is absent from the corpus too. This is worth a line for the seat, since the record names a code the gate does not test.
2. Another earlier roster token. "gravel" was a tag of e2a's original roster: results/raw/2026-08-09_e2a_g1.txt:3 has the pair (gravel, plaza), and saddle replaced it at e2a's v3 build (archive/RESULTS-cycles3-4.md:922). It occurs as a word in six passages: serenity-15, serenity-51 (one of the 54 printed), weariness-21, weariness-29, dread-48 and neutral-15. D5's earlier-token list is lattice and cedar only, so D5 does not count it. No gate is affected under CR6's reading, but the seat may want it stated beside cedar.
3. The validator's exit status carries no verdict. Its main() returns nothing and the file never calls sys.exit, so it exits 0 whatever PROBLEMS says; only a failed assert (for example a missing final newline) exits non-zero. The result is the "PROBLEMS: 0" line, and "exit 0" adds nothing to it.
4. The G-VEC mapping (27, 92) is a plan written in the present tense. It is how N.3's "no edit to a part file" would be honored, so it could be put to the seat as Code's proposal.
5. passage_spans (57) is the sixth zone-bearing field in BK's records. The exploration skipped it; it carries the same twelve labels.
6. CR9 follows the script docstring's G9 line ("only when G1-G8 hold"). The docstring's head ("only when every gate holds") matches the code.
7. Provenance. The PI's block header also cites "the routing of 2026-11-16, item 12" (results/raw/2026-11-16_second-sitting_pi-routing.md:34: "its acceptance check runs when the parts land, as routed on 2026-11-15 [noted]"). Neither draft cites it.
8. For N.2:
   - The block's header says Code commits by path "re-hashing each first"; neither draft's N.2 line says so.
   - For the ROOT decision: the validator reads ROOT only in recover() (validate.py:55–58), its saved-tool-result mode. Plain-file mode, the mode run here, never reads it, so neutralizing ROOT would not change the plain-file result.
   - A push after N.2 would carry that path to the remote.
9. Some outputs were never saved: the self-test's, the preflight's and the exploration's. The raw gives explore_bk.py's sha256 but not its text, so a reader of the committed raw cannot tie the hash to a file. The exploration's three findings are confirmed independently here (56, 57, 58).
10. neutral-71 is the only passage among all 544 with the word "neutral", not only among the 54 printed. The drafts could say so.
11. Run lists. The ENTRY's "Each run was nice -n 19 …" is scoped by its list and is followed by "The last three ran outside nice -n 19", so it reads consistently; RAW §1's sentence (52) has no such scope. The ENTRY numbers the runs 1–5 and the RAW 0–4, in the same order.

TOTALS: 102 items checked — 76 CONFIRMED, 7 IMPRECISE (27, 52, 57, 61, 84, 92, 98), 1 FAIL (89), 18 NOT CHECKABLE (6, 31, 32, 35, 39, 40, 41, 44, 47, 49, 54, 60, 65, 74, 95, 96, 99, 100).
```
