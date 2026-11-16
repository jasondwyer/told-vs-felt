# n — ids of record: the blind values-check

*The n-build session (Code), PI date 2026-11-16.*

- **What was checked:**
  - the raw (sha256 `73940f97…9517`);
  - the entry (`4d81e408…a591`), whose values-check line was then a placeholder;
  - the close lines on `645bd3f`'s entry (`044a7cf3…c50c`) and on `a61f13d`'s (`02ddfe5c…724f`);
  - the `.gitignore` block (`980c7d24…585b`).
- **The checker:** one blind pass by a fresh agent. Its brief quoted the list of record v2's items 1–5 verbatim with
  the coordinating session's lines, and added: no Python, no guard marker in any argv, no writes, and never a token id
  printed.
- **Its report** came back as the agent's hand-back message. Code extracted it from the agent's transcript with `jq`
  into this raw, unedited: 119 lines, sha256 `ee665e7c…21fc`. Its paths are the checker's, with S for Code's
  scratch folder.
- **The counts:** 63 items: 50 CONFIRMED, 7 IMPRECISE, 0 FAIL and 6 NOT CHECKABLE.

## The checker's report, as returned

Values-check of R (S/build/ids_raw.md), E (S/build/ids_entry.md), C1 (S/build/ids_close_645bd3f.md), C2 (S/build/ids_close_a61f13d.md) and G (S/build/ids_gitignore_block.txt). There are 63 items: 50 CONFIRMED, 7 IMPRECISE, 0 FAIL and 6 NOT CHECKABLE. I printed no id from the ids files. Observation 1 records one departure of mine from a source file.

**R — the raw**
1. R:1. The render of §1.2 (i)–(iii), 160 of 160. Source: S/render_ids_out.txt:7 ("sessions" n 160 / ok 160, "n4" 320/320, "status": "PASS"). CONFIRMED.
2. R:3–4. ADDENDUM-n1 v0.1 was committed at `a61f13d`, sha256 `e979f8f2…5e03`. Source: `git log` on the file gives a61f13d (parent 52b2c97). shasum gives the full hash, and the abbreviation checked by `cut` is e979f8f2…5e03. CONFIRMED.
3. R:4–5. The seat's answers (second sitting), §1.2–§1.3 and §5 item 1, at the path given, committed at `52b2c97`. Sources: answers raw :3, :16–23, :60; `git log` gives 52b2c97. CONFIRMED.
4. R:5–6. Laptop, model-free, tokenizer files only, and the raw prints no id. Sources: S/tok_n holds exactly the three tokenizer files. n_sessions.py:108–136 loads AutoTokenizer only. ids.py:219–224 asserts that the report holds no "ids" or "labels" key. A scan of every number in R found only counts, lengths, versions, dates, bytes and line references. CONFIRMED.
5. R:10–11. A window was granted for one process and at most two runs, and one run was made. NOT CHECKABLE: the grant is not in the sources. It is consistent with the single output file and with the write-once folder (ids.py:192–193).
6. R:12–13. The overlay holds the tracked files plus the drafts of Appendix A. Check: the overlay has 135 files. 15 are the drafts. The other 120 each equal HEAD's blob (`git hash-object --stdin` against `git rev-parse HEAD:<path>`). CONFIRMED. The venv and `nice -n 19` cannot be checked beyond output line 2.
7. R:16–17. The command. Sources: n_sessions.py:141–152 (render-ids needs `--tokenizer-dir`, `--out` and `--pi-date`). S/tok_n and S/ids_out exist. MANIFEST.json `pi_date` is "2026-11-16". CONFIRMED as consistent; the invocation itself is not recorded.
8. R:20 (and E:9's "ran offline"). "The two offline variables are the coordinating session's addition, so that nothing could reach the network." IMPRECISE. `HF_HUB_OFFLINE` and `TRANSFORMERS_OFFLINE` switch the Hugging Face libraries to offline mode; they do not block other network access. Suggested wording: "so that the Hugging Face libraries could not reach the network". That they were the coordinating session's addition is not checkable.
9. R:22. Exit 0, PASS. Sources: the output's `"status": "PASS"`; n_sessions.py:136 and :166 return 0 only on PASS. CONFIRMED. The output file has no exit line, so exit 0 rests on the code path.
10. R:22. "in 8 seconds". NOT CHECKABLE: no timing is in the sources.
11. R:22 and R:54–60. The output is given whole. `cmp` against S/render_ids_out.txt (7 lines, final newline) finds them byte-identical. CONFIRMED.
12. R:24–25. render-ids refuses any environment but G-DATA's (3.12.9 / 5.5.0 / 0.22.2), and output line 2 prints the environment. Sources: ids.py:48 and :68–71; n_sessions.py:119–122; output :2. CONFIRMED.
13. R:26–27. render-ids refuses a folder that is not exactly the three files at the `olmo2_instruct` sha256s (manifest lines 251–262), and output lines 3–5 print those checks. Sources: ids.py:45–49 and :74–90; data/olmo/manifest.json:170 (the entry starts) and :251–262 (the three files); output :3–5. CONFIRMED.
14. R:23. The section "What render-ids refuses before it renders" lists two refusals. IMPRECISE: the list is not complete. render-ids also refuses:
    - a `--pi-date` that is not YYYY-MM-DD (n_sessions.py:117–118);
    - an `--out` under data/m, data/mf3, data/p, data/olmo or /workspace/models, or inside the repository outside data/n/ (n_sessions.py:126; guard.py:74–81);
    - missing arguments (n_sessions.py:150–151).

    Suggested: open with "Among what it refuses before it renders:", or add the `--pi-date` and `--out` refusals.
15. R:29–30. (i): each of the 160 sessions reproduces BK's `seq_len` and `ids_sha`, with two re-splits applied. Sources: sessions.py:52–53 (exactly two split entries) and :173–190; ids.py:136–145 and :161–162. By jq, `seq_len` and `ids_sha` equal BK's records for all 160. By shasum, `ids_sha` recomputed from the id lists (the first 16 hex characters of the json.dumps form) matches in 160 of 160 sessions and 320 of 320 N4 sequences. CONFIRMED.
16. R:31–32. (ii): each of the 320 N4 sequences keeps BK's tokens before `n_pre`; the zone comes from `keys.n4_schedule`; the join is the one §1.2 (ii) fixes. Sources: sessions.py:149–156 and :193–199; keys.py `def n4_schedule`; n_sessions.py:132; ADDENDUM-n1:22; seat raw :18 ("The join, fixed here"). By jq:
    - the first `n_pre` ids equal the session's ids in 320 of 320;
    - `n_pre` equals BK's;
    - every N4-T line is "Prefer <cue>." naming the scheduled zone's cue;
    - every N4-Ts line is "Either is fine.".

    CONFIRMED.
17. R:33–35. There are four conventions, all §2's. The contexts are 160 sessions plus 320 N4 sequences, each with both cues, 960 per candidate. Sources: ids.py:53–54, :111–119, :171–175; ADDENDUM-n1:32; output (contexts 960 ×4). CONFIRMED.
18. R:28 with R:33. (iii) is listed under "What it asserts". IMPRECISE. (iii) is a test that keeps or drops each candidate: a failing candidate "is reported and dropped", and only "none kept" is a STOP (ids.py:19–21, :182–188; seat raw :19). Suggested: "(iii) For each label candidate convention, it tests that the prefix holds and the tail is the same in every context; a candidate that fails is reported and dropped, and no candidate kept is a STOP."
19. R:36. Counting N4's sequences among the contexts is labeled Code's reading, beyond §1.2's words. Sources: ADDENDUM-n1:22 (iii) and seat raw :19 name only the session's ids; ids.py:19–21. CONFIRMED.
20. R:37–38. render-ids writes only when (i) and (ii) hold and at least one candidate is kept; otherwise it STOPs and writes nothing. Sources: ids.py:127–134, :161–162, :186–188 (the folder is made at :190, after every STOP return). CONFIRMED.
21. R:42–44. tokenizer.json is the HF-cache snapshot of allenai/Olmo-3-1125-32B at c2b61dae…, and its sha256 is the pin in full. The brief's command returns 73fd5254…eaecca, equal in full to manifest:256. S/tok_n/tokenizer.json is identical. The cache folder is models--allenai--Olmo-3-1125-32B, its snapshot and refs/main are c2b61dae…, and manifest:3–4 gives the base entry's revision as c2b61dae89a1. CONFIRMED.
22. R:42. "copied by `cd` and a shell redirect". NOT CHECKABLE.
23. R:45–47. The two small files came from the box's `/workspace/models/olmo2_instruct/` through the pod session, were checked on the box, in staging and at the destination, and nothing was downloaded. Sources: copy log :1–10; the folder is not named in the log but is manifest:176's `path`. S/tok_box equals S/tok_n for both files (`cmp`), and their byte counts 4869 and 581 match manifest:261 and :253. CONFIRMED.
24. R:48–49. All three files equal the pins, with three abbreviations, and the render checked them again. shasum of S/tok_n matches manifest:252/256/260 and output :3–5; the abbreviations check by `cut`. CONFIRMED.
25. R:65–70. The table: 160, "320 (160 told, 160 sham)", "4 candidates, all kept", "3 files", and four full sha256s. shasum of S/ids_out matches the report's "files" map, and jq confirms the counts. CONFIRMED.
26. R:73. Each file's sha256 equals the report's and MANIFEST.json's `files` entries. CONFIRMED.
27. R:74–75. The manifest names the environment, the three pins, the session set `be50011a…ba84`, N4's schedule by sha256, and the PI date. Checks:
    - jq on MANIFEST.json shows the fields (plus `schema` "n-ids-v1").
    - The session set, recomputed as BK's 14 files concatenated in C-locale order, is be50011a…ba84, the same as schema.py:243.
    - `n4_schedule_sha256` recomputed from the records' zones in `bk_run` order matches.

    CONFIRMED.
28. R:76–77. 160 records and 160 distinct sessions; every list's length equals `seq_len`; both assertions are true; 144 sessions are 1,273 tokens and 16 are not, as BK's records have them. jq on S/ids_out/sessions.jsonl and on BK's records: BK has 144 at 1273, and every `seq_len` is equal per session. CONFIRMED.
29. R:78–79. 320 records, 160 N4-T and 160 N4-Ts, the prefix asserted on all, 13 distinct lines (12 told plus the sham). By jq: told 12, sham 1, sham line not among the told lines. CONFIRMED.
30. R:80–81. Each candidate holds 12 labels; tails are 3 tokens for bare and space and 4 with the end-of-turn token. jq on lengths only: 12 ×4; [3], [3], [4], [4]. CONFIRMED.
31. R:72. Code checked the files by shasum and jq and printed no id. NOT CHECKABLE as a process; the checks themselves reproduce (items 25–30).
32. R:83–84. The convention of record is decided on the box by §2's comparison, in the BACKEND extension's session, after G-VER has asserted (i). Sources: ADDENDUM-n1:32; seat raw :37 ("after G-VER has asserted (i)"). CONFIRMED.
33. R:88–89 and Appendix A's hashes. Checks:
    - The overlay's file hashes give an empty diff against R:94–108.
    - The package hash, recomputed in m's form (valence_core/m/resume.py:328–350) by shell over the overlay's 14 files, is 45c70818…6a98.
    - The 11 closure files (from S/pkg_hashes8.txt, the `hashes` output at the same package) each equal HEAD's blob and their listed sha256.

    CONFIRMED.
34. R:92–109. Appendix A is byte-identical to S/render_drafts_manifest.txt (`cmp`). CONFIRMED.
35. R:89–90. "The BUILD commits the drafts, and its entry states any difference." NOT CHECKABLE: it describes a future commit.
36. R:111–125. Appendix B is verbatim, sha256 `eb3bef45…1f92`. `cmp` against S/site/out/copy_tok_out.txt finds it identical; the sha256 is eb3bef45…1f92 by `cut`. CONFIRMED.

**E — the entry**
37. E:1–4. The heading, the seat's §1.2 and §5 item 1, the PI's item 7 "as ruled" (routing raw :27), and the raw's link path. CONFIRMED. data/n/ids/ is not yet in the tree; the commit is pending.
38. E:5–9. One run in a window; package `45c70818…6a98`; Python 3.12.9, transformers 5.5.0, tokenizers 0.22.2 as "the only one render-ids accepts"; offline; exit 0, PASS. These agree with R and with the sources in items 9, 12 and 33. CONFIRMED. The window grant is as in item 5, and "offline" carries item 8's caveat.
39. E:11–16. (i)–(iii), with Code's reading labeled at E:16. CONFIRMED (items 15–19).
40. E:17–18. The MANIFEST.json contents. CONFIRMED (item 27).
41. E:19–21. The tokenizer files and their route. CONFIRMED (items 21, 23 and 24).
42. E:23–26. The four abbreviations, checked by `cut` against the full hashes. CONFIRMED.
43. E:28–29. `.gitignore` admits data/n/ids/ on a line of its own, as the BK comment asks of "any later n artifact". Sources: .gitignore:260–261 ("any later n artifact (captures, checkpoints, reads) needs its own line"); G:7. CONFIRMED.
44. E:31. "G-VER asserts these files on the box against BK's records and the spans (ADDENDUM-n1 §1.3)". IMPRECISE. §1.3 (ADDENDUM-n1:24) says "G-VER (n §3) asserts (i) on the box against BK's `seq_len`, `ids_sha` and spans". Seat raw :25 says the same of sessions.jsonl, and R:84 says "(i)". The draft verify.py:4–18 also checks the other files, but that is Code's draft, not §1.3. Suggested: "G-VER asserts (i) on the box against BK's `seq_len`, `ids_sha` and the spans (ADDENDUM-n1 §1.3); the drafts' G-VER also checks the other files against MANIFEST.json."
45. E:32–33. §2's comparison decides the convention among the four candidates there, in the BACKEND extension's session. Source: ADDENDUM-n1:32. CONFIRMED.
46. E:34. Next in §5 is the follow-up schema commit. Source: seat raw :61. CONFIRMED.
47. E:35–37. The windows behind this commit: the self-test, 179/179, and the render. IMPRECISE (probable; the window grants are not in the sources). Evidence:
    - S/pkg_st7.txt shows 179/179.
    - Later runs follow: S/pkg_st8.txt 183/185, with FAILs in `primitive` and `runner`, then S/pkg_st8b.txt 187/187.
    - S/pkg_hashes7.txt shows package 92dd7f69…f805; S/pkg_hashes8.txt shows 45c70818…6a98, the render's package.
    - Names-only `ls -t` order: pkg_st7 → pkg_hashes7 → pkg_st8 → pkg_st8b → pkg_hashes8 → copy log → render output.

    So 179/179 appears to be the earlier package's count. The drafts the render ran appear to have been self-tested at 183/185 and then 187/187, and those two runs are not listed. If Code's window log confirms this, suggested: list every run with its package, e.g. "179/179 (package 92dd7f69…f805); then 183/185 (two FAILs, fixed) and 187/187 (package 45c70818…6a98, the render's)".
48. E:40. "`.gitignore`'s admit line". IMPRECISE (minor): G adds a blank line, five comment lines and `!/data/n/ids/`. Suggested: "`.gitignore`'s admit block (a comment and the admit line)".
49. E:39–44. The commit's contents and "Not pushed." NOT CHECKABLE: the commit is future.

**C1 — the close line on 645bd3f's entry**
50. C1:1. "The dated note the seat's raw, §5 item 1, asks for." Source: seat raw :60. CONFIRMED.
51. C1:2–5. The ruling raw's link, its full sha256 a4980152…151a, "committed by path at `52b2c97`", ruling on this block. Sources: shasum (full match); `git log`; RESULTS.md:303; seat raw :3. CONFIRMED.
52. C1:6–7. Q1 (b) and Q2 as stated. Source: seat raw :7–8, :14–17, :27, :71–72. CONFIRMED.
53. C1:8–11. The PI's item 7, verbatim, from the routing raw committed at a61f13d. diff against routing raw :27 (leading space stripped) is identical, and `git log` gives a61f13d. CONFIRMED.
54. C1:13–14. Done in this commit; both checks passed; nothing downloaded. Source: copy log :3–10. CONFIRMED (the commit is pending).
55. C1:15–18. Ledger (79), the seat's §4, verbatim. Joined, it is identical to seat raw :56. The only difference is that the source's bold `**(79)**` is plain "(79)". CONFIRMED.

**C2 — the close line on a61f13d's entry**
56. C2:1–3. Rendered and committed in this commit, 160 of 160, the tokenizer files checked, nothing downloaded; this is n-build's close as RESULTS.md:83 asks. CONFIRMED.
57. C2:3–4. "Next of §8.3 (3): the follow-up schema commit, G-VER asserting data, the site check re-run, and the BUILD entry." Sources: ADDENDUM-n1:84 says "G-VER's assertion form"; :80 says "G-VER asserts data"; RESULTS.md:79–80 uses the same paraphrase. It is an unquoted paraphrase. CONFIRMED.

**G — the .gitignore block**
58. G:2–5. Cites ADDENDUM-n1 §1 and the seat's §1.2; lists the 160 sessions' ids, N4's 320 sequences and the label candidates, and MANIFEST.json (each file's sha256 and record count). CONFIRMED.
59. G:5. "Record, not cache: G-VER asserts them on the box (ledger 27)." IMPRECISE (minor, citation placement). The BK block attaches "(ledger 27)" to "record, not cache" (.gitignore:258–259). Rule 27 says the repo is the record and says nothing about G-VER. Suggested: "Record, not cache (ledger 27): G-VER asserts them on the box."
60. G:6. "Admitted as one folder that MANIFEST.json lists." MANIFEST.json lists the other three files. That is the BK block's convention: SHA256SUMS does not list itself (0 matches). CONFIRMED.
61. Placement after `!/data/n/bk/`. Source: .gitignore:264. CONFIRMED.

**General**
62. No IP address, port, local path, clock time or token id appears in R, E, C1, C2 or G. Pattern scans found none. A number scan found only allow-listed values plus E:36's "179". The one path is R:45's box folder (observation 5). CONFIRMED.
63. E, C1 and C2 agree with R, except E:31's scope against R:84 (item 44). CONFIRMED.

**Observations**
1. A departure of mine: an early `grep -n` over S/overlay/valence_core/n/sessions.py printed its line 52, the first RECORDED_SPLITS entry, which holds four token ids in source code. It went to my tool output only. Nothing was written, I have not repeated it, and every later code read masked the digits.
2. Other method points:
    - names-only `ls -t` and `wc -c` on scratch files only;
    - perl for the number scan;
    - `git status --porcelain` scoped to the cited paths (all clean, data/n/bk included);
    - no Python, no network, nothing written;
    - globs were used for the barred words;
    - nothing was read under data/*/ckpt, data/*/reports or data/mf3.
3. data/n holds only `bk` at HEAD. Every file check ran on S/ids_out; the commit must carry those bytes.
4. The render's drafts go beyond ids and G-VER. The overlay's schema.py differs from HEAD and contains `kfold10` 8 times (HEAD has 0). pkg_st8's FAIL names are primitive and runner, which matches the band work. Appendix A also labels `__init__.py` a draft, though it equals HEAD's blob.
5. R:45's `/workspace/models/olmo2_instruct/` is the box path given in manifest:176, which is already committed text, not a laptop path.
6. The other 16 sessions are 1,266–1,272 tokens long. N4's schedule is 80 S and 80 U. Each end-of-turn tail extends its base tail by one token.
7. E:2 cites seat §1.2 and R:4 cites §1.2–§1.3; the two are consistent.
8. The closure list in item 33 is S/pkg_hashes8.txt, which is outside the brief's source list. Its 11 lines equal pkg_hashes7's.

## Code's dispositions

Each IMPRECISE item is applied in the checker's terms unless the disposition says otherwise. Line numbers are the
checked texts'.

- **Item 8, R:20 and E:9.** Applied: the raw says "so that the Hugging Face libraries could not reach the network",
  and the entry says the run had "the Hugging Face libraries offline".
- **Item 14, R:23.** Applied. The heading now reads "Among what `render-ids` refuses before it renders", and a bullet
  adds the `--pi-date` and `--out` refusals.
- **Item 18, R:28 and R:33.** Applied in the checker's words: (iii) is a test, a failing candidate is reported and
  dropped, and no candidate kept is a STOP.
- **Item 44, E:31.** Applied in the checker's words: G-VER asserts (i) under ADDENDUM-n1 §1.3, and the drafts' G-VER
  also checks the other files against MANIFEST.json.
- **Item 47, E:35–37.** Applied. The checker is right:
  - 179/179 was package `92dd7f69…f805`;
  - the render's drafts (`45c70818…6a98`) were tested in the later window, at 183/185 and then, after two tests were
    fixed, at 187/187.

  The entry's windows list now names every run with its package. It also names the schema self-test's invocation
  departure, which the coordinating session asked to be declared there.
- **Item 48, E:40.** Applied: "admit block (a comment and the admit line)".
- **Item 59, G:5.** Applied: "Record, not cache (ledger 27): G-VER asserts them on the box."
- **Items 5, 10, 22, 31, 35 and 49 (NOT CHECKABLE).** No change. They concern the window's grant, the run's time, the
  copy's method, Code's own checks and the commit to come, which the checker could not see.
- **Observation 1, the checker's own departure.** A `grep` over a draft printed `sessions.py`'s line 52, the first
  recorded split, which holds four token ids written in the code. They reached the checker's tool output only, and
  nothing was written. The same four ids are in G-DATA's committed raw (`results/raw/2026-11-06_n-gdata.md`:109–110).
  Recorded here; no further action.
- **Observation 4.** Applied: Appendix A's note says `__init__.py` equals `HEAD`'s.
- **Observation 6.** Applied: the raw gives the other 16 sessions' lengths, 1,266–1,272.
- **Observations 2, 3, 5, 7 and 8.** No change.

## The edits after the check, checked by tool

- **The diff.** From the checked texts to the final ones it holds exactly the dispositions above: 6 hunks in the
  raw, 4 in the entry and 1 in the `.gitignore` block, besides the entry's values-check line. The two close
  lines are unchanged.
- **The verbatim parts.** After the re-splice, the raw's three verbatim parts are byte-identical to their files.
- **Each changed claim,** asserted against its source, one assertion each; all 12 hold:
  1. 179/179 is in the earlier self-test's output;
  2. package `92dd7f69…f805` is in that window's `hashes` output;
  3. the schema's self-test printed 213/213;
  4. the package self-test printed 183/185, then 187/187;
  5. package `45c70818…6a98` is in the later `hashes` output;
  6. the 16 sessions not of 1,273 tokens are 1,266–1,272 (`jq`, lengths only);
  7. the guard refuses the box's model volume and the repository outside `data/n/`;
  8. `render-ids` refuses a `--pi-date` not of the form YYYY-MM-DD;
  9. `__init__.py` equals `HEAD`'s blob;
  10. `ids.py` STOPs when no candidate is kept;
  11. the drafts' G-VER checks the manifest;
  12. ADDENDUM-n1 §1.3 names (i), `seq_len`, `ids_sha` and the spans.
- **The final raw:** sha256 `1388dc2a…4ec2`.
