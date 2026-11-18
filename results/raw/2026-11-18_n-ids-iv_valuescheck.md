# n — ids of record, (iv): the blind values-check, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was checked.** One blind pass by a subagent over three drafts:
- the entry, sha256 `e573336d…de63`;
- the render raw, `8407db78…19db`: its hand-written text, with its output blocks checked against their sources;
- the review raw's §1, `a48d9195…c2d8`.

**The checker's brief:**
- named the sources: the drafts as committed and as reviewed, every run's output, the rendered folder, the overlay,
  the specification, the corpus and the repository's files;
- gave the package digest's rule;
- quoted the PI's item 4 and the list of record v2's items 1–5, verbatim;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3`, and any write.

**The report** is in §3, extracted verbatim from the subagent's hand-back by `jq` (230 lines, sha256 `35ee36a6…0551`).
It writes `<repo>` and `<scratch>`.

**The checker's own departure.** Its report discloses it: two hash-comparison loops put marker-carrying relative paths
into the argv of 36 git calls, model-free. It stands as written there. Code relayed it to the coordinating session for
Q-F3's run list.

**Totals:** 138 items — 112 CONFIRMED, 11 IMPRECISE, 1 FAIL, 14 NOT CHECKABLE — and 11 observations.

## 1. Dispositions

**The FAIL and the IMPRECISE items, all applied in the checker's terms:**
- **104, FAIL** (the review raw's findings header). It now says F1–F10 and F12 were in the drafts the render ran, and
  F11 came at the pin's move (run 4). This is the checker's reconstruction of run 2's `ids.py` (its item 56), and Code's
  own record of the edits agrees: the comment fixes were made after run 3.
- **20** (the entry; the render raw's R-iv3). 3,232 is the count of encodes, with each task's prefix counted once per
  context. The raw adds "over 1,936 distinct texts", the checker's figure.
- **26** (the entry). The tail `…bd84c` was mistyped; it is now `…d84c`, cut by tool.
- **29** (the entry). The code is in the same commit as the files, per the review's O9; the seat's §3 item 3 is not
  claimed for it.
- **37** (the entry). 266/266 is "after the review's fixes (F11's two comments excepted)", and 267/267 is "after the
  pin's move and F11".
- **57** (the render raw's table, run 2). "with the review applied but F11".
- **71** (the render raw, R-iv5). Em dashes, in 8 task completions and 4 frames; the frames file's `_doc` holds a §,
  which no context uses.
- **92** (the render raw's review section). F1–F10 and F12 were in the drafts runs 2–4 ran; F11 came at the pin's move.
- **95** (the render raw, the re-render). The render STOPs on its own output as a base, and the driver has no option to
  name another.
- **114** (the review raw, F10). The read-back's base clause is implied by `load`'s own check. The byte-level equality
  is its own test.
- **123** (the review raw, M8). Six sha256s and two counts are asserted.
- **135** (the review raw, O7). The two sha256s are given.

**The observations:**
1. **F11's timing.** Applied through 104, 37, 57 and 92.
2. **G-VER's `manifest_ok` is not the pin.** Applied. The render raw's G-VER section and the entry say that PASS
   requires the pin (`pin_ok`), which is not printed.
3. **The read-back's redundant clause.** Noted; the code is as run, and 114's disposition says so.
4. **What the checker reproduced without Python.** Noted. It stands in the report: the contexts' digest from HEAD's
   inputs by `jq`, the base manifest byte for byte, the per-state figures, and the span starts.
5. **Encodes, not texts.** Applied (20).
6. **The § is in no context.** Applied (71).
7. **F4's import assertion brackets only the two `--out` calls.** Noted. By code order the date refusal also comes
   before any import, but that order is not asserted. The code is as run.
8. **Under M2 the self-test fails by a raise.** Noted; it is still a kill.
9. **The `.gitignore` comment.** Applied. Its comment over `data/n/ids/` now names (iv) and the seat's answers of
   2026-11-18; the change is to comments only, and the file is in this commit.
10. **"STOPs" that are refusals.** Applied. The render raw now says that a base failing `load`, or an `--out` or
    staging folder that already exists, is a refusal, and that nothing is written either way.
11. **The departures' wording.** Applied. The entry now says "while Code built the overlay and read the adapter", as
    the raw does.

**The NOT CHECKABLE items (14)** rest on Code's own runs and the commit to come. No change.

## 2. The edits after the check, checked by tool

Each final text's full `diff` against its checked snapshot holds only the dispositions above, and Code read each diff
in full. The render raw's output blocks are reassembled from the same files and compared with `cmp`.

## 3. The report as returned

```text
# Blind values-check: the (iv) render's entry, render raw and review raw §1

## Conventions and conduct
- `<repo>` is the repository root. `<scratch>` is the brief's scratch folder, which the render raw writes as `<scratch>/iv`. The tokenizer folder is the render raw's `<scratch>/tok_n`.
- I ran no interpreter and wrote or edited nothing. Tools used: shasum, wc, grep (/usr/bin/grep), sed, cut, diff, cmp, jq, name-only ls, find with the ckpt/reports prune, and git log/show/rev-parse/hash-object/grep. Every `git grep` carried `':!data/**'`.
- I read nothing under `data/mf3`, `data/*/ckpt` or `data/*/reports`.
- I reached marker-named paths by `cd` plus a glob, or by a `<` redirect: the HF adapter, and the model manifest in both the repository and the overlay.
- **Departure (mine), disclosed here.** Two hash-comparison loops passed marker-carrying relative paths as arguments to `git hash-object` and `git -C <repo> rev-parse HEAD:<path>`:
  - the loop over the overlay's `valence_core/` hit 4 files: the two marker-named adapters and `valence_core/m/runner_*` for both models;
  - the loop over the overlay's `data/n`, `data/corpus` and `data/configs` hit 14 BK skeleton files under `data/n/bk/…/<model>_32b/neutral/`.

  That is 36 git invocations of a few milliseconds each. They were model-free: no interpreter, and no `data/mf3`, ckpt or reports path. I noticed this only after they ran.

## Items

### ENTRY (`entry_iv.md`)
1. ENTRY l.1 "ids of record, second commit: ADDENDUM-n1 §1.2 (iv)". **CONFIRMED.** ADDENDUM-n1 l.24 names the two (iv) files. The seat's answers §3 item 3 say "committed by path as `n — ids of record`'s second commit".
2. ENTRY l.1 "rendered once on the laptop in G-DATA's environment". **CONFIRMED.** render_run3.txt l.2 prints python 3.12.9 / transformers 5.5.0 / tokenizers 0.22.2, which is ADDENDUM-n1 §1.1. out/ holds one render output.
3. ENTRY l.2 gvec = "the 544 passages of data/n/passages.jsonl". **CONFIRMED.**
   - 544 lines.
   - The (id, state, pole) sequence equals the corpus's in order: jq digest `eacace6b…` on both files.
   - text_sha256 is equal for passages 0, 1 and 543.
   - The 544 text_sha256 values are distinct.
4. ENTRY l.2–3 a3 = "A3's frozen 1,344 contexts". **CONFIRMED.** 1,344 lines. The (item_id, condition, variant) order equals tasks × CONDITIONS × 4: jq digest `ea8ad85e…` on both sides.
5. ENTRY l.3 "MANIFEST.json extended. G-VER's pin and the n package move with it". **CONFIRMED** (ids.py:74 diff; the package digests in item 34).
6. ENTRY l.4 "seat's answers of 2026-11-18, §3 item 3, and the PI's item 4 of that date". **CONFIRMED.** The answers raw (git log `26cf7d2`) has §3 item 3. RESULTS.md:35 holds item 4, matching the brief's text.
7. ENTRY l.6 "run 3 of four". **CONFIRMED.** out/ holds outputs for runs 1, 2, 3 (render) and 4.
8. ENTRY l.6 "in the coordinating session's battery windows of 2026-11-18". **NOT CHECKABLE.**
9. ENTRY l.7 "scratch overlay of HEAD's files with the drafts in place". **CONFIRMED.**
   - The overlay's `valence_core/`: 103 of 105 files equal HEAD's blobs; the two that differ are `ids.py` and `verify.py`, the drafts.
   - Its data files under n, corpus and configs (ids excluded): 43 of 43 equal HEAD's.
   - `box_e0_corpus.py` and the model manifest equal HEAD's; `n_sessions.py` is the draft.
10. ENTRY l.7–8 "jlens venv (… G-DATA's environment, the only one render-ids-iv accepts)". **CONFIRMED.**
    - The versions are in output l.2.
    - `ids.check_environment` requires `dict(env) == ENV_OF_RECORD` (ids.py:61, 99–102), called at n_sessions.py:314.
    - Which venv was used is NOT CHECKABLE.
11. ENTRY l.8–9 "The Hugging Face libraries were offline". **NOT CHECKABLE.** The code loads with `local_files_only=True` (n_sessions.py:318).
12. ENTRY l.9 "Python was in UTF-8 mode". **CONFIRMED.** n_sessions.py:306–307 refuses otherwise, and the run exited 0 with PASS.
13. ENTRY l.9 "at nice -n 19". **NOT CHECKABLE.**
14. ENTRY l.9 "model-free". **CONFIRMED.** Output l.1 says PyTorch is absent. The driver loads AutoTokenizer only.
15. ENTRY l.9 "Exit 0, PASS". **CONFIRMED** (render_run3.exit = 0; `"status": "PASS"`).
16. ENTRY l.10 "544 of 544 passages, each encoded alone, with no special tokens and no template". **CONFIRMED.** The report shows n 544, ok 544. `enc` is `tok(text, add_special_tokens=False)` (n_sessions.py:263–264), applied per text in ids.py's `ids_both`.
17. ENTRY l.11 "1,344 of 1,344 contexts, in A3's order, each full encoded whole". **CONFIRMED** (report n/ok 1344; the order is as in item 4).
18. ENTRY l.11–12 "span starts at extract.span_start's boundary, which the render computes itself and asserts equal … on all 1,344". **CONFIRMED.**
    - ids.py's render_iv has the k loop and the `span_starts[j] != k` STOP.
    - `_a3_inputs` calls `extract.span_start` under `enc_special` (n_sessions.py:279–280).
    - ok = 1,344, with no problem line.
19. ENTRY l.12–13 "no span starts before the prefix's own token count (prefix_differs 0)". **CONFIRMED.** The report shows 0. In the file, span_start == prefix_tokens in all 1,344 records.
20. ENTRY l.14 "on every text encoded (3,232 in all)". **IMPRECISE.** 3,232 = 544 + 2 × 1,344 is the number of encodes. The distinct texts number 1,936: 544 passages, 48 prefixes (48 distinct prefix_sha256) and 1,344 fulls. Accept: "on every encode (3,232 in all: the 544 passages, and each context's prefix and full, a task's prefix once per context), adding special tokens changes no id".
21. ENTRY l.14–15 "A3's convention (the adapter's default) and n's coincide here". **CONFIRMED.** The HF adapter's `encode(self, text, add_special_tokens: bool = True)` is at its l.95 and calls `self._tok.encode(...)` at l.98. special_tokens_differ is 0.
22. ENTRY l.16 "A3's inputs are frozen". **CONFIRMED.** The output's digests (`3c53e5a54fbaa233`, `9654b9398743116f`, `ec2296182e726969`) equal FROZEN_SHA (box_e0_corpus.py:62–64), which equals sha256[:16] of the three input files as I computed them.
23. ENTRY l.16–17 box_e0_corpus.py `66c18554…ab57`, extract.py `2405b1a6…07fe`, "both HEAD's". **CONFIRMED.** shasum gives the same values for the repository files (blobs `10ae7c9a`/`318830d9` = HEAD's) and for the overlay's copies.
24. ENTRY l.17–18 contexts' digest `9cfd90aa…4802`. **CONFIRMED.** It is in the output and the manifest. I also reproduced it independently: `jq -n -j -c -a` over HEAD's e0_tasks.jsonl and e0_frames.json, building rows [prefix, full, condition, item_id, variant] in tasks × CONDITIONS × 4 order, hashes to `9cfd90aa…4802`.
25. ENTRY l.20 gvec `444352c1…33a5` (544 records). **CONFIRMED** (shasum; wc -l).
26. ENTRY l.21 a3 `757026e8…bd84c` (1,344). **IMPRECISE.** The tail has five hex digits; by the 8…4 convention (cut) it is `d84c`. The count is right. Accept: "`a3_contexts.jsonl` `757026e8…d84c` (1,344);".
27. ENTRY l.22–23 MANIFEST `fdf73d85…ef38`, keeping (i)–(iii)'s fields and entries and adding the two files and an iv block (date, base, corpus, A3's provenance, conventions). **CONFIRMED.**
    - Top-level fields and the three file entries are identical to the committed manifest.
    - The iv keys are a3{code_sha256, contexts, contexts_sha256, input_shas}, base_manifest_sha256, conventions, passages_sha256 and pi_date.
    - The base re-derived with jq (iv and the two (iv) entries dropped, `-cS`) is byte-equal (cmp) to the committed `7f51bd91…821d` file.
28. ENTRY l.25 "(i)–(iii)'s files are unchanged". **CONFIRMED.** git hash-object of the rendered sessions, n4 and labels files equals their blobs at `d76f34f`, which equal HEAD's.
29. ENTRY l.26 "The code, in the same commit, as the seat's §3 item 3 and the review's O9 ask". **IMPRECISE.** §3 item 3 says nothing about code. O9 is an observation (§2 l.311), not an ask. Accept: "**The code,** in the same commit as the files (the review's O9: in separate commits, HEAD between them would have G-VER STOP on the pin):".
30. ENTRY l.27–28 "`load` accepts (i)–(iii), or (i)–(iv) under an `iv` block whose base it re-derives byte for byte". **CONFIRMED.** ids.py's load runs the names/iv clause, then the `_sha256_bytes(_base_of(manifest))` check against `iv.base_manifest_sha256`.
31. ENTRY l.28–29 MANIFEST_OF_RECORD moves to `fdf73d85…ef38` from `7f51bd91…821d`, which is now MANIFEST_I_III. **CONFIRMED** (diff from base to draft at ids.py:65–74).
32. ENTRY l.30 verify.py: "its docstring's sentence on the pin". **CONFIRMED.** The only hunk is verify.py:19–22.
33. ENTRY l.31 n_sessions.py: "the render-ids-iv command". **CONFIRMED.** The draft also adds `_e0_corpus`, `_encoders`, `_a3_inputs` and four self-test checks.
34. ENTRY l.33 package `60d892dc…cc66` (the BUILD's) → `f927608c…3c03`. **CONFIRMED.**
    - The brief's shell rule gives `60d892dc…cc66` on `<repo>` (valence_core/n clean) and `f927608c…3c03` on the overlay.
    - RESULTS.md:390 and :448 give the BUILD's.
35. ENTRY l.33 "the closure is unchanged". **CONFIRMED.** Run 4's 11 imported_sha256 lines equal run 2's and those of the BUILD's site check (`results/raw/2026-11-16_n-build_sitecheck2_out.txt:50–60`), and equal shasum of the repository files.
36. ENTRY l.33–34 "The step-4 driver is rebased onto this commit; the box carries this package". **NOT CHECKABLE.**
37. ENTRY l.36 "236/236 on the reviewed drafts, 266/266 after the review's fixes, 267/267 after the pin's move". **IMPRECISE.** The numbers and exit codes are right (selftest_run1/2/4, exits 0). F11 was not in run 2's drafts (item 99). Accept: "236/236 on the reviewed drafts, 266/266 after the review's fixes (F11's two comments excepted), 267/267 after the pin's move and F11;".
38. ENTRY l.37–38 gver-trial PASS; 160 sessions, ids, N4 pairs, spans; 4 of 4 kept; "the manifest is at the pin". **CONFIRMED.**
    - gver_run4.txt gives sessions/ids_ok/n4_ok/spans_ok 160 and labels_kept/labels_ok 4.
    - labels.json has 4 candidates, all kept.
    - PASS requires `pin_ok` (verify.py:86, 140). The printed `manifest_ok` is a different check (observation 2).
39. ENTRY l.39 "The review was blind". **NOT CHECKABLE.**
40. ENTRY l.39 "12 findings (0 BUG, 5 RISK, 7 NIT) and 25 surviving mutants". **CONFIRMED** (§2 Totals).
41. ENTRY l.39–40 "Every finding is applied, and every mutant has a test written to kill it". **CONFIRMED.** Each of F1–F12 and M1–M25 is checked against the committed drafts (items 100–128).
42. ENTRY l.40 "the mutants themselves were not run". **NOT CHECKABLE.**
43. ENTRY l.42–48 "R-iv1–R-iv6 in the raw", six readings. **CONFIRMED.** The six bullets map one-to-one onto R-iv1–R-iv6.
44. ENTRY l.50 "the pin moves again at (v), and LOCK-n v0.1 names whichever is committed when it is drafted". **CONFIRMED.** ADDENDUM-n1 §1.2 (v) and §1.5 ("MANIFEST.json's sha256"); seat §3 item 4. No LOCK-n file is at the root.
45. ENTRY l.51 "the A3 ids are G-DATA's rendering of A3's texts (ADDENDUM-n1 §1.1), not a record of a box run". **CONFIRMED** (§1.1, the tokenizer of record).
46. ENTRY l.52–57 Departures: three commands; none ran Python or touched a model, mf3, ckpt or reports; disclosed. **NOT CHECKABLE.**
47. ENTRY l.59–64 committed-by-path list, raw names, "Not pushed". **NOT CHECKABLE** (future). It is consistent with the drafts. `.gitignore:271` admits `data/n/ids/` as a folder, so no admit line is needed. Neither raw name exists yet.

### RAW (`render_raw.md`)
48. RAW title "544 passages and 1,344 A3 contexts". **CONFIRMED.**
49. RAW header "Under ADDENDUM-n1 v0.1 §1.2 (iv) and §1.5". **CONFIRMED** (ADDENDUM-n1 l.24, l.30).
50. RAW header: the answers raw path, "committed at `26cf7d2`", §3 item 3. **CONFIRMED** (git log).
51. RAW header PI quote "then the render of ADDENDUM-n1 §1.2 (iv) in a window (no box needed)". **CONFIRMED.** It is a verbatim substring of item 4 (RESULTS.md:35).
52. RAW header "model-free: tokenizer files only, no weights … this raw prints none". **CONFIRMED.** No `"ids": [` occurs in the raw. The report holds no ids (`printable`).
53. RAW §The runs: battery windows, one process, nice, the HF offline variables, TMPDIR, `cd jl*/.venv/bin && ./python`. **NOT CHECKABLE.** The `<scratch>/iv/tmp1–4` folders exist and are empty.
54. RAW §The runs: overlay = HEAD's tracked files (valence_core/, the two scripts, data/n/, the e0 corpus files, the model manifest) plus the drafts. **CONFIRMED** (item 9; the overlay manifest's blob `66174d40` equals the repository's).
55. RAW table run 1: ids.py `2bb137ea…f31f`, n_sessions.py `0bcc05ea…a4cb`, 236/236, exit 0. **CONFIRMED** (the `.reviewed.py` files; selftest_run1).
56. RAW table run 2: ids.py `d52af8c4…76db`, n_sessions.py `a7b79386…7330`, 266/266, exit 0, package `e4da7cf6…7c98`. **CONFIRMED.**
    - The committed ids.py with the reviewed l.71–73 in place of its l.71–74, and without its l.878–888, hashes to `d52af8c4…76db`.
    - The package rule over HEAD's n modules, with that ids.py and HEAD's verify.py, gives `e4da7cf6…7c98`.
57. RAW table run 2 "with the review applied". **IMPRECISE.** By item 56, run 2's drafts carry neither F11 change. Accept: "with the review applied but F11 (its two comments came with the pin's move, run 4): …".
58. RAW table run 3: "the render of record | as run 2 | PASS, exit 0". **CONFIRMED.** Exit 0 and PASS. The report's post-review fields (span_len mean, contexts_sha256, provenance line) fit run 2's drafts.
59. RAW table run 4: ids.py `28157d89…4809`, verify.py `4de26209…d516`, n_sessions.py as run 2; the overlay's data/n/ids/ holds the six files; 267/267, exit 0; `f927608c…3c03`; G-VER PASS. **CONFIRMED.** The overlay's ids/ files equal out_render's by sha256.
60. RAW command block. **NOT CHECKABLE.** It is consistent: the overlay script, tok_n, out_render and tmp3 exist, and iv.pi_date is "2026-11-18".
61. RAW "PYTHONDONTWRITEBYTECODE=1 was also set on every run". **NOT CHECKABLE.** Consistent: there is no `__pycache__` or `.pyc` anywhere in the overlay.
62. RAW §What the render asserts, the six refusals before rendering. **CONFIRMED.** In n_sessions.py they run in this order: date (:295–301, regex plus `fromisoformat`), repository (:302–304), `guard.refuse_out` (:305), UTF-8 (:306), environment (:314), tokenizer folder (:315; `check_tokenizer_dir` requires exactly the three files at the pins), and the frozen inputs (:321 via `_a3_inputs` :277).
63. RAW render_iv STOP conditions: base at MANIFEST_I_III `7f51bd91…821d` with exactly three files, same environment and tokenizer digests; corpus `ef6b00dc…3cc3`; 544/1,344; exact keys, all strings, unique ids, ≥1 token; full extends prefix, 0<k<len, equal to span_start; special tokens. **CONFIRMED.** These are the checks in ids.py's render_iv; data/n/passages.jsonl hashes to `ef6b00dc…3cc3` (committed at b4522ae). Observation 10 notes refusals as against STOPs.
64. RAW "What it writes": staging beside --out, rename after read-back; (i)–(iii) copied and re-checked; gvec fields; a3 fields; manifest and iv block. **CONFIRMED.**
    - Code: `stage = out.with_name(out.name + ".staging")`, the sha check per copied file, `load(stage)`, then `os.replace`.
    - The files' key sets (jq): 8 keys in gvec and 11 keys in a3, exactly as listed.
65. RAW R-iv1: "directions.py's reading, declared at the BUILD"; state field kept (flow_engagement); mapping "as ruled". **CONFIRMED.** directions.py:8–10 is "declared at the BUILD", and the file's only commit is 83a50a0. The state names appear in the output. RESULTS.md:32 item 1 says "[as ruled]".
66. RAW R-iv2: "frozen 1,344 of e0_contexts(), in its order: 48 tasks × 7 conditions × 4 paraphrases"; boundary asserted; prefix count beside it, prefix_differs 0. **CONFIRMED.** box_e0_corpus.py:11 and :132–144; e0_tasks.jsonl has 48 lines; the order is as in item 4.
67. RAW R-iv3: the adapter's default adds special tokens; n's ids add none; the assertion over 3,232 with `tok.encode(text, add_special_tokens=True)` against `tok(text, add_special_tokens=False)`. **CONFIRMED.** The adapter is at l.95/98; extract.py:77–78 and :109 encode through `adapter.encode`; the encoders are n_sessions.py:263–267. Item 20's nuance applies, but this sentence itemises "each of the 1,344 contexts' prefix and full".
68. RAW R-iv3 "post_processor is null, as the review noted". **CONFIRMED.** tok_n/tokenizer.json:225 reads `"post_processor": null`, as §2 l.120 says.
69. RAW R-iv4: extended "as the seat's §3 item 3 asks"; the pin move; both constants named; load re-derives; schema stays "n-ids-v1". **CONFIRMED.** §3 item 3 says "MANIFEST.json extended"; the manifest's schema is n-ids-v1.
70. RAW R-iv5 "requires Python's UTF-8 mode, so A3's files decode as UTF-8 whatever the locale". **CONFIRMED.** n_sessions.py:306; box_e0_corpus.py:110 and :114 open the files without an encoding.
71. RAW R-iv5 "Their texts carry non-ASCII characters (§ and em dashes)". **IMPRECISE.**
    - e0_tasks.jsonl's only non-ASCII characters are em dashes, in 8 completions.
    - e0_frames.json has 4 em dashes, in self_pos[0], self_neg[0], char_pos[0] and char_neg[0].
    - Its single § is in `_doc`, which `e0_contexts` never reads, so no context carries a §.

    Accept: "Their texts carry non-ASCII characters: em dashes, in 8 task completions and 4 frames. (The frames file's `_doc` also holds a §, which no context uses.)"
72. RAW R-iv6: overlay "as the (i)–(iii) render did"; the two sha256s, equal to HEAD's; the other n modules equal HEAD's except ids.py and verify.py. **CONFIRMED.** The (i)–(iii) render raw (`d76f34f`) l.12. Items 9 and 23.
73. RAW §The tokenizer folder: the (i)–(iii) folder, provenance in that raw; exactly three files with the three pins, which are the manifest's olmo2_instruct; output l.3–5; nothing downloaded. **CONFIRMED.**
    - tok_n holds exactly the three files, at `73fd5254…ecca`, `fff5b944…3fc7` and `78afb564…e2f2`.
    - In the model manifest the three digests sit at `["olmo2_instruct","files",<name>,"sha256"]`.
    - The (i)–(iii) raw l.17 and l.41–48 give the provenance.
    - The driver loads with `local_files_only=True`.
74. RAW run 3's output block. **CONFIRMED.** Lines 110–117 equal out/render_run3.txt (diff empty); it contains no local path.
75. RAW "first line is the transformers library's notice … as at the (i)–(iii) render". **CONFIRMED** (that raw's l.58 is identical).
76. RAW report counts: 544/544, 1,344/1,344, special_tokens_differ 0, prefix_differs 0, no problem line. **CONFIRMED.**
77. RAW per-state token counts (9 triples). **CONFIRMED.** All match the report, and jq recomputes them from gvec_passages.jsonl (n_tokens = len(ids) throughout; 56 per state, 96 neutral).
78. RAW A3's contexts: seq_len 32–90; span "(the Reviewer turn)" 10–29, mean 16.82; digest `9cfd90aa…4802`. **CONFIRMED.** jq over the file gives 32/90 and 10/16.82…/29. box_e0_corpus.py:12 and :133 say "Span = the Reviewer turn".
79. RAW files table: six names, records 160/320/4/544/1344/"5 files", six full sha256s. **CONFIRMED** (shasum, wc -l, labels.json candidates = 4, manifest files = 5).
80. RAW "copied from <scratch>/iv/out_render/. The three (i)–(iii) files are byte-equal to those committed at d76f34f". **CONFIRMED** for byte-equality (item 28). The copy itself is future.
81. RAW package "Before the pin's move … e4da7cf6…7c98, with the drafts as rendered". **CONFIRMED** (hashes_run2.txt; item 56).
82. RAW package "As committed … MANIFEST_OF_RECORD at the new manifest and the comment fixes (F11) … f927608c…3c03 … package of record". **CONFIRMED** (hashes_run4.txt). The drafts to be committed equal the overlay's files by sha256.
83. RAW "Its eleven closure lines are run 2's, unchanged". **CONFIRMED** (11 lines; diff empty).
84. RAW "Reproduced in the shell … overlay `f927608c…3c03` … HEAD's tree `60d892dc…cc66`, the BUILD's". **CONFIRMED.** The rule matches `m.resume.package_sha256_of` (resume.py:328–350); RESULTS.md:390 gives the BUILD's value.
85. RAW run 4's hashes block. **CONFIRMED** (it equals out/hashes_run4.txt).
86. RAW G-VER "on the assembled folder: the committed (i)–(iii) plus the render's three new files … tokenizer loaded to decode only, from <scratch>/tok_n". **CONFIRMED.** The overlay's ids/ holds the six files. Decode-only is n_sessions.py:208–211. The `--model-dir` value is NOT CHECKABLE.
87. RAW G-VER block. **CONFIRMED** (it equals out/gver_run4.txt).
88. RAW self-test outputs, "each one line, whole" (236/266/267 with two leading spaces). **CONFIRMED** (wc -l = 1 each; od).
89. RAW "Run 4 adds one check to run 2's 266: the committed data/n/ids/ is (i)–(iv) …". **CONFIRMED.** By item 56, the only added check is ids.py:878–888; verify.py and n_sessions.py add none.
90. RAW "Run 2's 266 are the BUILD's 217, plus 45 for (iv) in ids.py and 4 in the driver". **CONFIRMED.**
    - RESULTS.md:392 and :470 give 217/217 on the laptop.
    - HEAD's n package and driver are the BUILD's (git log 83a50a0).
    - Executed (iv) checks in run 2's ids.py number 45, counting the loops (3 × 2, 3 × 1) and the five `refused_load` calls.
    - The driver's checks are at n_sessions.py:141, 148, 164 and 182.
91. RAW §The review: 12 findings (0/5/7), 25 mutants, the review raw's link. **CONFIRMED.**
92. RAW §The review "Every finding is applied, and every mutant has a test … in the drafts runs 2–4 ran". **IMPRECISE.** F11 is only in run 4's drafts. Accept: "Every finding is applied — F1–F10 and F12 in the drafts runs 2–4 ran, F11 at the pin's move (run 4) — and every mutant has a test written to kill it, in the drafts runs 2–4 ran; the mutants were not run."
93. RAW §Departures, the three commands and their disclosure. **NOT CHECKABLE.** Consistent: the overlay's manifest equals HEAD's.
94. RAW Observations, the pin, whose rendering and rule 18:
    - (v) is G-CAL-n's prompts (ADDENDUM-n1 §1.2 (v)); §1.5; §1.1.
    - A3's `span_len_min_max_mean` is at box_a3_extract.py:209.
    - A3's `hygiene()` runs at :134, before `capture` at :153; the render path calls no hygiene.
    - The O1, O4 and O5 attributions match §2.

    **CONFIRMED.**
95. RAW Observations "A re-render … render-ids-iv refuses its own output as a base". **IMPRECISE.** By the raw's own vocabulary this is a STOP: `load` passes, then the base_pin check makes `render_iv` return status STOP and the driver exits 1. Accept: "from this commit on, `render-ids-iv` STOPs on its own output as a base (its MANIFEST.json is not at `MANIFEST_I_III`), and the driver has no option to name another base. (The review's O8.)"

### REVIEW §1 (`review_raw.md`, header and dispositions)
96. Header "PI date 2026-11-18. Code (the n-build session)". **NOT CHECKABLE.**
97. "drafts of ids.py (`2bb137ea…f31f`) and n_sessions.py (`0bcc05ea…a4cb`), read against HEAD's two files". **CONFIRMED.** The bases' blobs `f51d3c84` and `f72e4559` equal HEAD's.
98. The reviewer's brief: spec, recipe, consumers, list items 1–5, the bars. **NOT CHECKABLE.** Consistent with §2's Conduct.
99. "The reviewed drafts are the bytes run 1 tested (236/236)". **NOT CHECKABLE** as to identity. 236/236 is confirmed.
100. "§2, extracted verbatim … by jq (222 lines, sha256 `0d9ec56a…4435`)". **CONFIRMED.** l.96–317 equal review_returned.md (diff empty), which has 222 lines and that sha256. The jq step is NOT CHECKABLE.
101. "It writes <repo> and <scratch> for the local roots". **CONFIRMED.** No absolute path, user name or session id appears.
102. The disclosure of the refused recursive grep "stands as written". **CONFIRMED** (§2 l.106).
103. Totals: 12 (0/5/7), 25, 3 equivalent, 10 observations. **CONFIRMED.**
104. "Findings — every one applied in the drafts the render ran (run 2, 266/266)". **FAIL.** Run 2's drafts (items 56–57) carry the reviewed ids.py comment "(i)-(iii)'s until (iv)'s render is committed" and HEAD's verify.py docstring. F11's own line says "Applied at the pin's move". Accept: "**Findings** — every one applied: F1–F10 and F12 in the drafts the render ran (run 2, 266/266), F11 at the pin's move (run 4, 267/267):".
105. F1. **CONFIRMED.** Staging, --out must not exist, re-check on copy, read-back, `os.replace`, `rmtree` on BaseException. The tests are `iv_boom` (OSError on MANIFEST.json, neither folder left) and `iv_st` (a leftover staging folder is refused).
106. F2. **CONFIRMED.**
    - The UTF-8 refusal is at :306.
    - `prefix_sha256` and `full_sha256` are in all 1,344 records.
    - `iv.a3` holds `input_shas`, `code_sha256` (as loaded, equal to HEAD's), `contexts_sha256` (`a3_digest`, the `_dumps` of the rows; reproduced in item 24) and `contexts`.
    - All are printed (output l.6 and l.8).
    - "with PYTHONUTF8=1": UTF-8 mode is confirmed; the variable itself is NOT CHECKABLE.
107. F3. **CONFIRMED.** load raises "listed in MANIFEST.json but absent"; the test is `refused_load("absent")`. "Every later box bundle carries all six files" is NOT CHECKABLE.
108. F4. **CONFIRMED.** `refusal` (n_sessions.py:127–134) turns any other raise into a failed check. The --out check asserts its own message and `not loaded_before and not loaded_after`; the date check asserts "YYYY-MM-DD". Observation 7 has a nuance.
109. F5. **CONFIRMED.** The all-classes count is asserted at 7; the per-class variants at 3, 2 and 2.
110. F6. **CONFIRMED** (`except ValueError` → "not JSON"; test `iv_json`).
111. F7. **CONFIRMED.** The driver computes `span_start` under `enc_special`. render_iv STOPs on a different boundary (`iv_starts`) or a list of the wrong length (`iv_nstarts`). At the render, all 1,344 agreed.
112. F8. **CONFIRMED** (`_encoders`, n_sessions.py:260–268; the StubTok check at :151–166).
113. F9. **CONFIRMED.** The repository check with its own message (:303–304) comes before `guard.refuse_out` (:305). render_iv's messages use `out.name` or file names only.
114. F10 "… load refuses …, and the read-back asserts they hash to base_pin; both are tested". **IMPRECISE.** load's refusal is tested (`basebad`). The read-back clause cannot fail once `load(stage)` passes: `iv.base_manifest_sha256` is `base["manifest_sha256"]`, already equal to base_pin. The byte-level equality is tested by its own self-test check. Accept: "`load` refuses when they do not hash to the iv block's `base_manifest_sha256` (tested); the read-back also asserts they hash to `base_pin`, a clause `load`'s own check already implies; and a self-test check asserts the re-derived base equals the base manifest byte for byte."
115. F11. **CONFIRMED.** The reviewed and committed ids.py differ at :71–74; verify.py's docstring changes at :19–22. Both were applied at the pin's move, as stated.
116. F12. **CONFIRMED.** Regex plus `fromisoformat` (:295–301); the tests are "Nov 18", "2026-13-45" and "20261118". `cmd_render_ids` is unchanged, and its run is committed at `d76f34f`.
117. Mutants header: tests in "the drafts that passed runs 2 and 4". **CONFIRMED.** All the (iv) tests are in run 2's ids.py (item 56) and in n_sessions.py `a7b79386`. "not run" is NOT CHECKABLE.
118. M1. **CONFIRMED** (`iv_env`, `iv_tok`).
119. M2. **CONFIRMED** (`iv_five`; see observation 8).
120. M3–M5, counts 2, 2, 3. **CONFIRMED** (the prefixes, fulls and passages variants).
121. M6. **CONFIRMED** (count 7).
122. M7. **CONFIRMED.** The self-test's all-records `ids_sha` check plus the read-back's `bad` count.
123. M8 "the report's six sha256s and counts equal the files on disk". **IMPRECISE.** The test asserts six sha256s but only two counts, MANIFEST.json 5 and a3 2. "Pin taken by shasum" is NOT CHECKABLE (the value matches). Accept: "M8: the report's six sha256s equal the files on disk, and its counts for MANIFEST.json (5) and `a3_contexts.jsonl` (2) are asserted. The pin was taken by `shasum` of the rendered MANIFEST.json, not from the report."
124. M9–M11. **CONFIRMED** (`iv_noext` with "Task: u…", `iv_k0`, `iv_kfull`, each expecting "extend"/"degenerate").
125. M12–M15. **CONFIRMED** (`iv_dup`, `iv_keys_nonstr`, `iv_keys_extra`, `iv_empty`).
126. M16–M20. **CONFIRMED.** `iv_count` expects "2 contexts". `refused_load` "four" and "threeiv". The FILES_IV pin. seq_len and span_len asserted exactly.
127. M21–M23. **CONFIRMED** (the refusal-text asserts; the StubTok flag check).
128. M24, M25. **CONFIRMED.** `_a3_inputs` with stubs: the order is (self_neg, char_pos, self_pos), so sorting would fail; frozen digests and file sha256s are asserted.
129. O1. **CONFIRMED.**
130. O2. **CONFIRMED** (schema n-ids-v1; top-level pi_date 2026-11-16; iv.pi_date 2026-11-18).
131. O3. **CONFIRMED.**
132. O4. **CONFIRMED** (span_len is [10, 16.82, 29]; box_a3_extract.py:209).
133. O5. **CONFIRMED** (a position, consistent with box_a3_extract.py:134).
134. O6. **CONFIRMED.**
135. O7 "(sha256 above)". **IMPRECISE.** No sha256 of the two files appears above in the review raw; they are in the render raw's R-iv6. Accept: "**O7.** The overlay's two text-building files equal HEAD's (`66c18554…ab57` and `2405b1a6…07fe`; the render raw, R-iv6)."
136. O8. **CONFIRMED.** argparse has no `--base-dir`; `base_dir` is fixed to `ids.IDS_DIR` (:325).
137. O9 "The files and the pin move are in one commit". **NOT CHECKABLE** (future).
138. O10. **CONFIRMED.** FROZEN_SHA is in 16-hex form. A3 records `assert_frozen_inputs()`'s values as `input_shas` (box_a3_extract.py:133, 200).

Every abbreviated hash in the three drafts was re-cut by tool (first 8, last 4). All match except item 26.

## Observations
1. **F11's timing is now proven, not asserted.** Run 2's ids.py and run 2's package both reproduce exactly (item 56). So the render ran without either F11 comment. Four sentences say or imply otherwise (items 37, 57, 92, 104). The render's outputs do not depend on comments.
2. **G-VER's printed `manifest_ok` is not the pin.** It covers the environment, the tokenizer files and the session set (verify.py:81–82). `pin_ok` (:86) is never printed and only gates PASS (:140). "The manifest is at the pin" is true because of PASS; the seat may want that said.
3. **One read-back clause is redundant.** render_iv's read-back base clause is equivalent (item 114), like the reviewer's first equivalent mutant in the reviewed draft.
4. **Reproduced without Python** (the seat may want these on record):
   - the contexts' digest, from HEAD's inputs with jq; this binds A3's order, texts and UTF-8 decoding;
   - the base manifest, byte for byte;
   - the per-state statistics and seq_len/span_len;
   - span_start == prefix_tokens on all 1,344;
   - spot checks, all equal: text_sha256 for passages 0, 1 and 543; prefix and full sha256 for contexts 0 and 111 (e04/char_neg/3, whose completion carries an em dash).
5. **3,232 counts encodes, not texts.** The distinct texts number 1,936.
6. **The § is in no context.** It sits only in e0_frames.json's `_doc`. e0_probes.json also has non-ASCII on 3 lines, including a §, but `e0_contexts` does not read it.
7. **F4's import assertion brackets only the two --out calls.** The three date refusals run after `loaded_after` is taken. By code order the date refusal comes before any import, but this is not asserted.
8. **Under M2 the self-test fails by a raise, not a STOP.** The run reaches `load(stage)`, whose base check raises SystemExit. The driver records that as "ids: its self-test ran to its end" FAIL. It is still a kill.
9. **.gitignore needs no change.** l.271 admits `data/n/ids/` as a folder, so the two new files need no line. Its comment (l.266–270) still describes only (i)–(iii)'s contents (optional).
10. **Some "STOPs" are refusals.** In the raw's "STOPs, writing nothing, unless …", a base that fails `load`, or an existing --out or staging folder, raises SystemExit; it does not return a STOP report. Nothing is written either way.
11. **The departure bullets read slightly differently.** The entry says "While Code built the overlay"; the raw adds "and read the adapter", which is where the grep was.

## Totals
138 items: 112 CONFIRMED, 11 IMPRECISE (items 20, 26, 29, 37, 57, 71, 92, 95, 114, 123, 135), 1 FAIL (item 104), 14 NOT CHECKABLE.
```
