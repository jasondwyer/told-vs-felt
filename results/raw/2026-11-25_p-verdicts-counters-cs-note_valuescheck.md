# The blind values-check of the dated note on corrupted_spelling's rule, with Code's dispositions (Code, the dpo VERDICTS session; PI date 2026-11-25)

*The coordinating session asked for one blind pass on the note before its commit, the report committed as a raw beside it. The note goes on `9464f61`'s entry. It answers Q1 of the seat's read of the sft VERDICTS (`results/raw/2026-11-25_p-sft-verdicts-read_design-to-code_answers.md`, §4 item 7) under the PI's routing item 3, "[note, no change]".*

*The checker was a fresh subagent with no part in the drafting, and it ran no interpreter. Its brief quoted the list of record v2, items 1–5 (item 4 with C.2's amendment of 2026-11-16, second sitting), and the rules of Q-F3's campaign on this laptop. It opened nothing under `data/p/ckpt`, `data/p/verdicts`, `data/p/reports` or `data/mf3`. It read the seat's sft-read raw at its line 1 and §4 only, and the counters raw at its header and the start of its stdout, the lexicon by `shasum` and whole-line counts only.*

*Its report follows verbatim (sha256 `aed686d76b81a114e2f659295339967d4ec65f647257f9ef495e0c23df90c8c5`), then Code's dispositions. The edits after it were checked by tool, not by a second blind pass. Calendar dates only; the commit hash is the record.*

## The report, verbatim

# Values-check (blind): the dated note on `corrupted_spelling`'s rule as implemented (`note_cs_9464f61.md`), against HEAD `13ca2fe`, 2026-11-25

**Result:** 35 claims: 30 CONFIRMED / 2 IMPRECISE / 0 FAIL / 3 NOT CHECKABLE. Skipped as instructed: `SEAT_READ_COMMIT` (line 4), along with the "committed by the coordinating session at" that goes with it. The raw is untracked now (`??`).

| # | Where (line) | Claim | Verdict | Evidence / fix |
|---|---|---|---|---|
| 1 | 1 | "PI date 2026-11-25" | NC | This is the PI's calendar. It matches the question raw's date (in its name) and this session's date. |
| 2 | 1 | "the corrupted-spelling rule as the counters step implements it" | I | The step implements no rule. `scripts/p_verdicts_counters.py`:38 says "WHAT IT ADDS: no definition. It applies the imported predicates …". The rule is in `valence_core/p/report.py`:203–217, as the note's own line 9 says. **Fix:** "the corrupted-spelling rule as the counters step applies it." |
| 3 | 1–2 | the note's author, "The dpo VERDICTS session" | NC | The author names itself. This matches the counters raw's header (line 1), which names its author "Code, the dpo VERDICTS session". |
| 4 | 2 | "on Q1 of the seat's read of the sft VERDICTS" | C | Raw line 1: "# PROPOSAL-p OLMo-sft — VERDICTS: the seat's read (p §8 step 7; …)". §4 item 7: "**One question, not a ruling — Q1:**". |
| 5 | 3 | the link `results/raw/2026-11-25_p-sft-verdicts-read_design-to-code_answers.md` | C | The file is at that path (untracked, `??`). The link text is its basename. RESULTS.md is at the root, so the relative link resolves. |
| 6 | 4 | sha256 `3f8ccda4…fdad` | C | `shasum -a 256` gives `3f8ccda4889e865d…fdad`. Abbreviated by awk `substr`: `3f8ccda4…fdad`. |
| 7 | 4 | "§4 item 7" | C | Item 7 of "## 4. Dispositions of Code's "for the seat" items …" (lines 65–74) is "**The counters step** (`922d7a3`; …)". It holds Q1. |
| 8 | 5–7 | the PI's routing, item 3, verbatim | NC | It is not in any file (it was relayed to the drafting session). Its substance matches the last sentence of §4 item 7: "Code states the rule as implemented, in a dated note or its next values-check; the counter's form is frozen at its first report (rule 23) and nothing moves". |
| 9 | 8 | "Nothing changes: not the script, not its outputs, not the counts" | C | At HEAD the script's sha256 is `a87749e9…d6f6`, the same as at the run (counters raw line 3; gate 4, line 16). Its blob at `1ceebbf`, at HEAD and in the working tree are the same. Its `run` writes only stdout: every file write comes after its self-test marker (line 674). The counters raw has one commit (`922d7a3`) and is clean. report.py last changed at `d215d5b` (2026-11-09). This matches item 7's "nothing moves". |
| 10 | 9 | "The step defines no counter of its own." | C | Script :38: "WHAT IT ADDS: no definition." Script :7 quotes the seat: "adds no definition of its own". All five predicates in p23_table are p's (see NOTE 5 on `cap_hits`). |
| 11 | 9–10 | "It calls p's `report.corrupted_spelling`, unchanged, in `valence_core/p/report.py`." | C | Script :125 imports `valence_core.p.report` ("… unchanged"). p23_table :298–299 calls `p_report.corrupted_spelling(…)`. report.py's last commit, `d215d5b`, is earlier than the run (`922d7a3`, 2026-11-16). The working tree matches the HEAD blob. |
| 12 | 10–11 | "That file's sha256 is `e807c5ad…5af1`, as the counters raw prints at its imports." | C | `shasum` gives `e807c5adc6d43cd9…5af1` (awk-abbreviated `e807c5ad…5af1`). Counters raw file line 64 reads "imports: valence_core/p/report.py sha256 e807c5ad…5af1; …", and the full value is equal. |
| 13 | 11 | passes "each round's item gold variants (m's CORR_clean)" | C | p23_table :298 passes `pool[_item(r, pool)]["gold"]`. The pool comes from `pool_of_record` (:229–235): `m_corr.load_pool()` (CORR_clean, `data/f/pools.json`), asserted equal to task_correct's. |
| 14 | 11 | "the clean pool's task words" | C | p23_table :293: `clean = p_report.clean_task_words(pool)`. See report.py :155–158. |
| 15 | 12 | "the pinned lexicon: `data/p/lexicon/web2.txt`, sha256 `be41ad97…bab9`" | C | `run` :629 calls `lex = p_report.load_lexicon()`, which loads `REPO / LEXICON_REL` (report.py :103, :174). The load is refused unless the bytes hash to `LEXICON_SHA256` (:104, :182–184). `collect` passes the lexicon to p23_table at :488. The file hashes to `be41ad97963bf8da…bab9`, the pinned constant. Counters raw file line 65 prints the path and the value. |
| 16 | 12–13 | "which each LOCK-p v1.0 names as "the lexicon (F-p11)"" | C | There are three `LOCK-p*` files, `LOCK-p-OLMo-{sft,dpo,instruct}.md`, each "v1.0". In each, §8.1 (lines 86–117) has at line 99: "- the lexicon (F-p11): `be41ad97…bab9`". The LOCKs name the digest, not the path. The phrase is byte-exact. |
| 17 | 13 | "A round counts iff one of its words is a hit" | C | p23_table :313–315 appends the round's key only when the predicate is true. `corrupted_spelling` returns True at the first hit and False otherwise (report.py :215–217). |
| 18 | 14 | "the stored text is split on whitespace, and each token is normalized by f0's `normalize`" | C | report.py :209–210: `for tok in str(text).split(): w = m_gcal.normalize(tok)`. gcal.py:184–185 sits under the comment "f0's grader, ported verbatim (f0_calibrate.py:56-66)". See also the PIN at report.py :64–65. |
| 19 | 14–15 | normalize "lower-cases it, makes every character but a–z, 0–9, `/` and the space a space, and strips the ends" | C | gcal.py:185: `return re.sub(r"[^a-z0-9/ ]", " ", s.lower()).strip()`. |
| 20 | 16–17 | candidates: "length ≥ 2, not in … FUNCTION_WORDS and not a word of the clean pool's tasks" | C | report.py :211: `if not w or len(w) < 2 or w in FUNCTION_WORDS or w in clean_words: continue`. |
| 21 | 16 | "p §1.1's FUNCTION_WORDS" | C | report.py :88 imports the list from `corrupt.py`. corrupt.py :3 reads "THE RULE (p §1.1) … the closed list ``FUNCTION_WORDS``", defined at :27–28. PROPOSAL-p v0.2 line 31 (§1.1) lists the same 21 words in the same order. report.py :66: "FUNCTION_WORDS is p §1.1's list". |
| 22 | 17 | "the seat's pinned definition of 2026-11-07, `38f9974`" | C | `results/raw/2026-11-07_p-gcal-flags_design-to-code_answers.md` §5 (line 23): "**The pinned definition:** candidate words are the stored text's whitespace-split, `normalize`d words of length ≥ 2, excluding FUNCTION_WORDS and every word of the clean pool's tasks; …". The raw was added at `38f9974` (2026-11-07), its only commit, and the working tree matches the HEAD blob. |
| 23 | 18–19 | "F-p11 (the seat's refinement of 2026-11-08, `daca8b0`, §3) excludes a candidate on either ground" | C | `results/raw/2026-11-08_p-gcal_design-to-code_answers.md` §3: heading at line 23 ("F-p11 — the corrupted-spelling counter, refined once more …"), text at line 25 ("Add two exclusions …"). The raw was added at `daca8b0` (2026-11-08), its only commit. report.py :213: `if in_lexicon(w, lex) or gold_up_to_suffix(tok, gs): continue`. |
| 24 | 20 | (i) "in a committed English lexicon" | C | Byte-exact in §3 line 25 (`/usr/bin/grep -c -F` gives 1). |
| 25 | 20 | "web2, with every part of a multi-part candidate listed" | C | report.py :189–192: `parts = word.split(); return bool(parts) and all(x in lexicon for x in parts)`. The lexicon is web2's lines passed through `normalize` (:185). See NOTE 2. |
| 26 | 21 | (ii) "equal to a gold up to trailing punctuation and a possessive or plural suffix" | C | Byte-exact in §3 line 25. It is implemented by `gold_up_to_suffix` (:195–200) on the raw token: trailing non-alphanumerics are dropped, then each of `'s`, `’s`, `s'`, `s’`, `es`, `s` is dropped in turn. |
| 27 | 22–23 | the hit: not a gold, distance to some normalized non-numeric gold ≤ 1 (gold length ≤ 3), ≤ 2 otherwise | C | report.py :208: `gs = spelling_golds(gold)`. Per :161–168, golds are normalized, and a gold whose non-space characters are all digits counts as numeric and is dropped. :215: `any(w not in gs and levenshtein(w, g) <= (1 if len(g) <= 3 else 2) for g in gs)`. This is the wording of 11-07 §5. |
| 28 | 25 | "`don`, `col` and `close` are each a line of web2 (`/usr/bin/grep -x` …)" | C | `/usr/bin/grep -c -x -- WORD data/p/lexicon/web2.txt` gives don 1, col 1, close 1. |
| 29 | 25 | "with the file at its pinned sha256" | C | `shasum -a 256` gives `be41ad97…bab9`, equal to `LEXICON_SHA256` (report.py :104). The working tree matches the HEAD blob. The file has one commit, `d215d5b`. |
| 30 | 26 | "F-p11 (i) therefore excludes each before any distance is taken" | C | In `corrupted_spelling` the order is: :211 (the candidate rule), then :213 ((i) first, and `or` short-circuits), then :215 (the distance). Each word normalizes to itself and is in the normalized lexicon, so :213 skips it before :215. None is removed earlier at :211 (NOTE 1). |
| 31 | 26 | "`Close` normalizes to `close`" | C | `s.lower()` gives `close`. Every character is in `a–z`, so nothing is replaced or stripped. |
| 32 | 27 | "The seat's ruling names the third itself: "so `there`, `could`, `close` do not count" (`daca8b0`, §3)" | C | Byte-exact, backticks included, in §3 line 25. |
| 33 | 28 | "p §2.3's sentence names the class the counter aims at" | C | PROPOSAL-p v0.2 line 68 (§2.3, under "## §2" at line 62): "**answers in corrupted spelling** (a word of the stored text within Levenshtein distance 2 of a gold and not equal to it — class (c) of §0.3, …)". |
| 34 | 28–29 | "The counter is the pinned definition with F-p11's two exclusions, so it counts less than that sentence describes" | C | Every hit is a normalized word within the sentence's distance of a normalized gold and not equal to it. The pinned definition removes short words, function words, task words and numeric golds, and tightens the limit for short golds to 1 (11-07 §5: "As written the counter fires on common words near short golds"). F-p11 also removes lexicon words and forms equal to a gold up to a suffix. See NOTE 4. |
| 35 | 29–30 | "The ruling says as much: "the counter under-counts the class and says so"" | I | The quotation is byte-exact (11-08 §3 line 25; also 11-07 §5 line 23). But in both rulings this clause ends a sentence about "`Janbaa` and `Janyooar`, at distance ≥ 3, (still) do not". Those are forms that the sentence's own distance 2 also leaves out. Neither ruling says that the exclusions make the counter count less than §2.3's wording. Neither says that lexicon exclusions of genuine corruptions (`don` for *down*, `col` for *cold*) fall under the clause. "Says as much" reads the ruling as covering the very point the seat's Q1 puts to Code as a question. **Fix:** replace that sentence with: "The rulings' clause "the counter under-counts the class and says so" (`38f9974`, §5; `daca8b0`, §3) is said there of `Janbaa` and `Janyooar`, at distance ≥ 3, which that sentence's distance 2 leaves out as well; whether `don` and `col`, excluded by (i), fall under it is for the seat." |

## NOTES

1. **Line 26's "therefore" leaves out a step.** Each word has to survive the candidate rule (:211) before it reaches (i) at :213. All three do:
   - each has length ≥ 2;
   - none is in FUNCTION_WORDS (corrupt.py :27–28);
   - none is a clean-pool task word. I checked this with a jq replica of `clean_task_words` (split on whitespace, ASCII lower-case, `[^a-z0-9/ ]` to a space, ends trimmed, empties dropped) over CORR_clean in `data/f/pools.json`. That pool has 16 items, and the file's sha256 is `8547d9a1…17a0`, the value the counters raw prints at file line 65. The replica returns false for all three words; the controls `the` and `is` return true.

   Optional wording for line 26: "None is a function word or a clean-pool task word, so F-p11 (i) excludes each before any distance is taken."
2. **Line 20: how broad the lexicon is.** F-p11 reads "Code picks the source (a frozen common-words list)". report.py's PIN (:38–43, "declared at step 6, LOCK-p v0.1") reads "It is a full dictionary, not a frequency-ranked common-words list: it excludes every English word it lists, common or rare, so it excludes more than such a list would". This breadth is what removes `don` and `col`, and the seat's Q1 ("suggests the implementation excludes dictionary words") turns on it. The bullet is accurate as it stands. Optional clause after "web2": "(Code's pick, declared at LOCK-p v0.1: "a full dictionary, not a frequency-ranked common-words list", where F-p11 named "a frozen common-words list")".
3. **The three cases are the seat's.** I checked them as the seat names them: stored tokens that normalize to exactly `don`, `col` and `close`. No record was opened. Under the PIN (report.py :65–66), a stored `don't` would be the single candidate `don t`, which is a different case. The note does not need it.
4. **Line 29, "counts less".** This holds on the normalized reading, which both the pinned definition and the seat's Q1 use. If the words are read as raw strings, normalization can also let a token in. For example, `Januwy.` is beyond distance 2 of its gold as raw strings, but at distance 2 once both are normalized, and both rulings say it counts. No change needed.
5. **Line 9, `cap_hits`.** p23_table restates this counter inline as `bool(r["cap_hit"])` (script :296), the same expression report.py's `counters` uses (:236). That is p's counter, not a new one, so the claim stands. For corrupted_spelling, p23_table calls p's own function (:298–299), the same call p's `session_counters` makes (report.py :291–292).
6. **Optional citations.** Line 17 could add §5 after `38f9974`, as report.py :57 does. Line 10's "the counters raw" could add `922d7a3`, as item 7 does.
7. **Line 21: the seat's own `Close.` example.** The seat's (ii) uses `Close.` as its example. report.py's PIN (:48–49) says "(ii) alone would not exclude it, ``close`` not being ``closed`` up to a suffix"; (i) is what excludes it. Line 26 agrees with the PIN. The note could optionally say so, since the seat placed its `Close.` example under (ii).
8. **Departures from the brief, for the coordinating session to class.**
   - (a) The counters raw's stdout starts at file line 12: lines 1–10 are the header and line 11 is the fence. Its first 70 stdout lines are therefore file lines 12–81. Stdout lines 61–70 (file lines 72–81) turned out not to be gates, imports or rulings: they are the start of the first stage section ("== OLMo-sft / time"). I read them as part of the 70 lines the brief allowed. Nothing from them is used or reported here.
   - (b) `data/f/pools.json` is not on the brief's source list, but it is outside every forbidden path. I ran one `shasum` on it and the jq replica of `clean_task_words` from NOTE 1. The replica printed only booleans and two counts (16 items, 49 distinct task words).
   - (c) On the lexicon, besides `shasum` and `/usr/bin/grep -c -x`, I ran `git log --format='%h %cs'`, `git rev-parse HEAD:`, `git hash-object` and `git check-attr -a`. These print ids, digests and attributes only, with no byte, size or time.
   - (d) I ran one `head -n 5` on `/usr/bin/grep -n`'s line numbers for `valence_core/p/corrupt.py`. `head` is not on the brief's tool list, though it is not an interpreter. I also used the shell builtins `printf`, `echo` and `for`.
   - (e) RESULTS.md is not on the source list. I used `/usr/bin/grep -c` and `-n` to count the target entry's heading: it is at line 14057 in the working tree, appears once at `9464f61`, and is absent at its parent.
   - (f) I took line counts with `awk 'END{print NR}'` of the seat raw, report.py, the script and the counters raw. I found the bounds of the seat raw's §4 with grep and awk printing line numbers only.

Not opened: anything under `data/p/ckpt`, `data/p/verdicts`, `data/p/reports` or `data/mf3`; the seat raw beyond its line 1 and §4 (lines 65–74); the counters raw beyond its file line 81; the lexicon's content. Not run: any interpreter (no Python, node, perl or ruby), any whole-tree `git status` (every status was scoped to named paths), any tree-wide content search, any pickaxe. Nothing was written except this report.

## Code's dispositions

The two IMPRECISE items are applied in the checker's words; there was no FAIL.

- **#2** (the step applies the rule, it does not implement one): applied. The title now reads "as the counters step applies it". The PI's routing keeps its own words, "as implemented".
- **#35** (the "under-counts" clause): applied in the checker's words, as two sub-bullets.
  - The clause is said in both rulings of `Janbaa` and `Janyooar`, at distance ≥ 3. Code confirmed this by tool in each ruling's text.
  - Whether `don` and `col`, excluded by (i), fall under it is left to the seat.
- **NOT CHECKABLE items (#1, #3, #8): they stand.**
  - #1, the PI's calendar date.
  - #3, the note's author.
  - #8, the routing item, relayed to this session verbatim and not in a file.

**NOTES**
1. **Applied:** "None is a function word or a clean-pool task word, so F-p11 (i) excludes each". Code checked both by tool. `FUNCTION_WORDS` in `valence_core/p/corrupt.py` has none of the three. The 16 CORR_clean tasks in `data/f/pools.json`, lower-cased with every character outside a–z, 0–9, `/` and the space made a space, give 0 matches for the three as whole words.
2. **Applied:** the lexicon's breadth, quoted from report.py's PIN ("a full dictionary, not a frequency-ranked common-words list") beside F-p11's "a frozen common-words list".
3. **No change.**
4. **No change.**
5. **No change.**
6. **Applied:** "§5" after `38f9974`, and `922d7a3` after "the counters raw".
7. **Applied:** F-p11's (ii) example `Close.`, with report.py's PIN quoted: "(ii) alone would not exclude it, ``close`` not being ``closed`` up to a suffix". It was confirmed by tool against the docstring, whose line wraps.
8. **The checker's departures, as it gave them, for the coordinating session to class.**
   - (a) It read the counters raw's stdout lines 61–70, which are the start of its first stage section. Nothing from them is used or reported.
   - (b) It ran `shasum` and a `jq` replica of `clean_task_words` on `data/f/pools.json`, a file outside every bound path. The replica printed booleans and two counts.
   - (c) It ran `git log`, `rev-parse`, `hash-object` and `check-attr` on the lexicon: ids, digests and attributes only.
   - (d) It ran one `head -n 5` on `grep`'s line numbers.
   - (e) It ran `grep -c` and `-n` counts on RESULTS.md.
   - (f) It took line counts with `awk`.

   Code's reading: (b)–(f) read names, ids and digests, or files outside the bound paths. (a)'s lines hold counts from the committed counters raw, not an outcome.

**The edits after the check, checked by tool:** 9 `/usr/bin/grep -F` checks on the note, each fix present and each replaced phrase absent; all PASS. No second blind pass was run.
