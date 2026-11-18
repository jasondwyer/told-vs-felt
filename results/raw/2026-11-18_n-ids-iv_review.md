# n — ids of record, (iv): the blind review of the render's drafts, as returned, with every disposition

PI date 2026-11-18. Code (the n-build session).

**What was reviewed.** One blind pass by a subagent over the drafts of `valence_core/n/ids.py` (sha256
`2bb137ea…f31f`) and `scripts/n_sessions.py` (`0bcc05ea…a4cb`), read against HEAD's two files.

**The reviewer's brief:**
- gave the specification (ADDENDUM-n1 §1; the seat's answers of 2026-11-18, §3 item 3), the A3 recipe
  (`scripts/box_e0_corpus.py`, `valence_core/extract.py`) and the loader's consumers;
- quoted the list of record v2's items 1–5, verbatim;
- barred any interpreter, any guard marker in an argv, anything under `data/mf3`, and any write.

The reviewed drafts are the bytes run 1 tested (236/236).

**The report** is in §2, extracted verbatim from the subagent's hand-back by `jq` (222 lines, sha256 `0d9ec56a…4435`).
It writes `<repo>` and `<scratch>` for the local roots. Its disclosure, that the permission layer refused one plain
recursive `grep` before it ran, stands as written; nothing was read.

**Totals:** 12 findings (0 BUG, 5 RISK, 7 NIT), 25 surviving mutants, 3 equivalent mutants and 10 observations.

## 1. Dispositions

**Findings** — every one applied: F1–F10 and F12 in the drafts the render ran (run 2, 266/266), and F11 at the pin's
move (run 4, 267/267):
- **F1** (RISK, a failure after the first write). `render_iv` builds the folder in a staging folder beside `--out`.
  `--out` must not exist. Each (i)–(iii) file's bytes are re-checked against the base manifest as they are copied.
  The folder is read back, then renamed into place, and on any failure the staging folder is removed. Tests: a
  synthetic write failure leaves neither folder; a leftover staging folder is refused.
- **F2** (RISK, nothing binds A3's texts).
  - `render-ids-iv` refuses outside Python's UTF-8 mode; the render ran with `PYTHONUTF8=1`.
  - Each A3 record carries `prefix_sha256` and `full_sha256`.
  - The iv block's `a3` holds A3's input digests, the sha256s of `scripts/box_e0_corpus.py` and
    `valence_core/extract.py` as loaded (both equal HEAD's), and the contexts' digest (`a3_digest`: the sha256 of
    `_dumps` of the rows in order) with their count. The render prints them.
- **F3** (RISK, an absent listed file). `load` refuses, naming any listed file that is absent; tested. Every later
  box bundle carries all six files of `data/n/ids/`. That is for the step-4 box check's file list.
- **F4** (RISK, the driver's two checks). `refusal` returns the refusal's text and turns any other raise into a failed
  check, not a crash. The checks assert render-ids-iv's own message for `--out` and the date's message, and that
  neither tokenizer library is imported before or after.
- **F5** (RISK, the special-token test). The all-classes test asserts the count, 7. Three single-class variants each
  STOP, with counts 3 (passages), 2 (prefixes) and 2 (fulls).
- **F6** (NIT). A passage line that is not JSON is noted and STOPs; tested.
- **F7** (NIT). The driver computes `extract.span_start` itself for each context, under the adapter's encode, and
  passes the list. `render_iv` STOPs where its own boundary differs, or where the list is the wrong length; both are
  tested. At the render, all 1,344 agreed.
- **F8** (NIT). `enc_special` calls `tok.encode(text, add_special_tokens=True)`. The two encoders are factored into
  `_encoders` and tested with a stub tokenizer that records each call's flag.
- **F9** (NIT). render-ids-iv tests the repository first, with its own message, then `guard.refuse_out`.
  `render_iv`'s messages name folders by their basename.
- **F10** (NIT). `_base_of` re-derives the base manifest's bytes from an (i)–(iv) manifest. `load` refuses when they do
  not hash to the iv block's `base_manifest_sha256`; this is tested. The read-back also asserts they hash to
  `base_pin`, a clause `load`'s own check already implies. A self-test check asserts the re-derived base equals the
  base manifest byte for byte.
- **F11** (NIT). Applied at the pin's move: `ids.py`'s comment on `MANIFEST_OF_RECORD` and `verify.py`'s docstring.
- **F12** (NIT). Applied to render-ids-iv: the form by regular expression, the date by `datetime.date.fromisoformat`.
  Tests: "Nov 18", "2026-13-45" and "20261118". `render-ids` is unchanged; its run is committed.

**Mutants** — each has a test written to kill it, in the drafts that passed runs 2 and 4. The mutants themselves were
not run. Each mutant and its test:
- M1: STOPs on another environment, and on another tokenizer digest.
- M2: a base folder of (i)–(iv), its own manifest given as the pin, STOPs.
- M3–M5: special tokens on one class alone STOP, with counts 2, 2 and 3.
- M6: the all-classes count, 7.
- M7: every (iv) record's `ids_sha` re-derived, in the test and in the read-back.
- M8: the report's six sha256s equal the files on disk, and its counts for MANIFEST.json (5) and `a3_contexts.jsonl`
  (2) are asserted. The pin was taken by `shasum` of the rendered MANIFEST.json, not from the report.
- M9, M10, M11: a full that does not extend its prefix; a span at token 0; a span at the full's end.
- M12: a duplicate id. M13: a non-string value. M14: an extra key. M15: an empty text.
- M16: the count STOP's problem line names the counts.
- M17, M18: four files with no iv block; three files with one.
- M19: the two (iv) file names pinned.
- M20: `seq_len` and `span_len` pinned exactly.
- M21, M22: the refusal texts (F4).
- M23: the stub tokenizer (F8).
- M24, M25: `_a3_inputs` against a stub corpus module: it keeps `e0_contexts`' order and fields, records the frozen
  digests as returned, takes each boundary from `span_start` under the given encode, and records both files'
  sha256s.

**Observations** (for the seat; noted, with these responses):
- **O1.** The pin moves, to `fdf73d85…ef38`, and (v) will move it again. LOCK-n v0.1's "rendering and spans" names
  whichever is committed when the lock is drafted.
- **O2.** The schema id stays "n-ids-v1" for both shapes. (i)–(iii)'s date stays, and (iv)'s is `iv.pi_date`.
- **O3.** The passages are under the same assertion.
- **O4.** The committed A3 ids are G-DATA's rendering of A3's texts (ADDENDUM-n1 §1.1's tokenizer of record), not a
  record of a box run. The report's `span_len` now carries the mean, for comparison with A3's
  `span_len_min_max_mean`.
- **O5.** Rule-18 hygiene for A3 belongs in G-VEC's wiring.
- **O6.** `prefix_differs` is 0 on these texts.
- **O7.** The overlay's two text-building files equal HEAD's (`66c18554…ab57` and `2405b1a6…07fe`; the render raw,
  R-iv6).
- **O8.** A re-render needs a base folder at `d76f34f`; the driver has no `--base-dir`.
- **O9.** The files and the pin move are in one commit.
- **O10.** The three A3 digests are `FROZEN_SHA`'s 16-hex form, as A3 recorded them.

## 2. The report as returned

```text
# Blind review: the ids (iv) drafts, `ids.py` (render_iv, load) and `n_sessions.py` (render-ids-iv)

The drafts are `<scratch>/ids.py` and `<scratch>/n_sessions.py`, read against `<scratch>/ids.base.py` and `<scratch>/n_sessions.base.py`. Line numbers refer to the drafts unless another file is named.

## Conduct
- I ran no Python and no other interpreter, and I wrote or edited nothing.
- What I read: the `diff -u` of each base against its draft, both drafts in full, and the specification and recipe files named in the brief. My searches stayed in `<repo>` and the session's scratch folder. I did not open the HF cache.
- Both bases equal HEAD by git blob id (`ids.base.py` f51d3c84, `n_sessions.base.py` f72e4559). `scripts/box_e0_corpus.py` and `valence_core/extract.py` in the tree also equal HEAD.
- I read the HF adapter with `cd valence_core/adapters` and `sed -n … < *_hf.py`, so no guard marker appeared in any argv.
- I did not read, list or search anything under `data/mf3`, `data/*/ckpt` or `data/*/reports`.
- **Disclosure.** The permission layer refused one of my commands before it ran. It was a plain recursive `grep` for the manifest pin's prefix, and I had written it with git's exclusion pathspec. Plain `grep` does not honour that pathspec, so it would have searched all of `data/`, including `data/mf3` and the ckpt and reports directories. Nothing was read. I redid the search as `git grep -l … -- . ':!data/**'`.

## Facts checked on the inputs (model-free)
- **`data/n/passages.jsonl`:**
  - sha256 ef6b00dc…3cc3, which equals PASSAGES_SHA256.
  - 544 lines. All 544 match `^{"id": "…", "state": "…", "pole": "…", "text": "…"}$`, with no quote or backslash in any value.
  - No byte outside printable ASCII. No duplicate id. No empty or space-padded text.
  - 56 lines for each of 8 states, and 96 neutral.
  - Consequence: `splitlines()` gives 544 records and every one passes line 340. The malformed-line, duplicate-id and empty-text paths cannot be reached on the adopted bytes.
  - The file is untracked today; N.2 commits it before the render.
- **`data/n/ids/MANIFEST.json`:** sha256 7f51bd91…821d, which equals MANIFEST_I_III. It is in `_dumps` form (compact, sorted keys) and was added at d76f34f.
- **A3's inputs:** the sha256[:16] of `data/corpus/e0_tasks.jsonl`, `data/configs/e0_frames.json` and `data/configs/e0_probes.json` equal FROZEN_SHA's three values.
- **The tokenizer folder the (i)–(iii) render used** (`tok_n` in the session's scratch):
  - It holds the three files at the pins: 73fd5254…ecca, fff5b944…3fc7 and 78afb564…e2f2.
  - In `tokenizer.json`, `post_processor` is null (its line 225).
  - `tokenizer_config.json` names GPT2Tokenizer and has no add_bos_token or add_eos_token key.
  - G-DATA's raw records that the template adds no BOS (`results/raw/2026-11-06_n-gdata.md:79`).
  - My reading of these files is that `add_special_tokens=True` adds nothing in G-DATA's environment, so the new assertion should hold. The render is the test of that, not this reading.

## Answers in brief
- **Wrong ids or a wrong span start on the real inputs:** none found.
  - Passages are encoded alone with `add_special_tokens=False`, which is the (i)–(iii) call and directions.py's convention.
  - Contexts are A3's `full`, encoded whole. The span starts at the first id where full's ids leave prefix's ids; this is `extract.span_start`'s loop, at 364–366.
  - The draft applies `capture`'s degenerate-span test (367; extract.py:111–114).
  - Contexts keep `e0_contexts()`'s order and text.
  - What nothing binds is the text itself (F2).
- **Special tokens:** the assertion runs on every text A3's recipe encodes and on every passage. The recipe encodes the prefix and the full (extract.py:77–78, 109). The test cannot show this coverage (F5).
- **Manifest:**
  - (i)–(iii)'s fields and entries are carried as parsed values and re-serialized by the same canonical `_dumps`.
  - The new manifest is well formed for `load` (274–276).
  - It is also well formed for `verify.verify`, which reads only fields the extension keeps (verify.py:78–85).
  - A byte-level check that the fields are unchanged is available but absent (F10).
- **STOP paths:** every STOP returns before `out.mkdir` (387). A failure after that point leaves a populated folder (F1).
- **Refusals, in order:**
  - In the driver: the PI date's shape (204), --out (206–208), the environment (215), the tokenizer folder (216), and A3's frozen inputs (220).
  - In render_iv: the base manifest's pin and file set (315), its environment and tokenizer files (318), the passages' sha256 (321), the counts (326), and a non-empty --out (385).
  - The --out refusal does come before the tokenizer libraries are imported, as the check's name says. Its tests do not show that (F4).
- **Ids in the report:** none on any path I traced. The report holds counts, sha256s, state names, and problem lines built from names and counts. `printable` and the self-test check key names only (see C6 below). Refusal texts print absolute paths (F9), not ids.
- **A malformed passage line** crashes the run rather than STOPping (F6). This cannot happen on the adopted bytes.
- **Five files in the manifest:** no caller breaks in code. G-VER now reads and hashes the two (iv) files on every load (F3).

## Findings

**F1 — RISK — ids.py:384–407. A failure after the first write leaves a populated --out.**
- *What:* every STOP returns before `out.mkdir` (387), but three failures can come after it, and each leaves files behind:
  - the read-back `load(out)`, which raises SystemExit on a sha256 or count mismatch (405);
  - the read-back comparison (406–407);
  - any I/O error in `_atomic_write`, which also leaves `*.tmp` files.
- *Evidence:* the (i)–(iii) files are read twice. `load(base_dir)` verifies them at 313; the copy at 389 reads them again without verification. A change between the two reads is caught only by the read-back. By then all six files, MANIFEST.json included, are already in --out. The folder of a failed run looks complete, and the plan copies from it by hand.
- *Fix:*
  1. Build the folder in a staging folder beside --out.
  2. Before writing each (i)–(iii) file, assert that the sha256 of the bytes being copied equals `bman["files"][f]["sha256"]`.
  3. Read the staging folder back, then `os.replace(staging, out)`.
  4. On any exception, remove the staging folder.
  
  The driver's statement "on a STOP nothing is written" then holds for every failure.

**F2 — RISK — ids.py:372–373 and 397–402; n_sessions.py:219–222; scripts/box_e0_corpus.py:85–92 and 109–114. Nothing binds the A3 texts the ids are rendered from.**
- *What:*
  - `assert_frozen_inputs` hashes file bytes, but the texts are built by code (`task_prefix`, `e0_contexts`) from files opened without an encoding, so they are decoded with the locale's encoding.
  - The A3 records carry no text digest, although the passages carry `text_sha256`.
  - The iv block records only the three 16-hex input digests. It records neither the bytes of `box_e0_corpus.py` and `extract.py`, which build the text, nor a digest of the 1,344 texts in order.
  - If the render runs from a scratch overlay, as (i)–(iii) did, those two code files are the overlay's copies.
- *Evidence:* `e0_tasks.jsonl` has raw UTF-8 multibyte characters (em dashes) on 8 lines, and `e0_frames.json` has them (§, em dashes) on 5. Under a non-UTF-8 LC_CTYPE the texts would change while every check in render_iv still passes.
- *Fix:*
  1. Refuse unless `sys.flags.utf8_mode` is set or `locale.getencoding()` is UTF-8; alternatively, launch with PYTHONUTF8=1 and assert it.
  2. Add `full_sha256` (and `prefix_sha256`) to each A3 record.
  3. Add `contexts_sha256` to the iv block: the sha256 of `_dumps([[prefix, full, condition, item_id, variant], ...])` in A3's order.
  4. Add the sha256s of `scripts/box_e0_corpus.py` and `valence_core/extract.py` as read.
  5. Print all of these in the raw.

**F3 — RISK — ids.py:278–279 (`load`) once the manifest lists five files.**
- *What:* every `ids.load` then reads and hashes both (iv) files: G-VER at the box, gver-trial, and render_iv's read-back. A listed file that is absent raises FileNotFoundError, a traceback rather than a refusal that names the file.
- *Evidence:* the BUILD's second site check verified an explicit list holding "the four files under data/n/ids/" (`results/raw/2026-11-16_n-build_sitecheck2_inputs.txt:9–10, 29–32`). A box whose data/n/ids/ receives the new MANIFEST.json without both (iv) files would crash G-VER's load.
- *Nothing else breaks with five files:*
  - `verify.verify` reads `environment`, `tokenizer_files`, `session_set_sha256` and the pin (verify.py:78–85), plus `by_session`, `by_variant` and `candidates`.
  - The runner receives `ids_of` and `label_ids` (runner.py:242–243).
- *Fix:* every box bundle and its check list carry six files. In `load`, refuse with a SystemExit naming any listed file that is absent.

**F4 — RISK — n_sessions.py:122–127. Both new driver checks can pass for the wrong reason.**
- *What:*
  - At the box (transformers 5.15.0), every call ends in `ids.check_environment`'s SystemExit (215), whether or not the --out and date refusals exist.
  - In G-DATA's environment, where the laptop self-test runs (RESULTS.md:380), a missing refusal reaches `check_tokenizer_dir` on the absent `no-tok` folder. Its `iterdir()` raises FileNotFoundError (ids.py:112). `refused()` (109–114) does not catch that, so the whole self-test aborts with a traceback and no tally.
  - The check's claim "before anything loads" is never observed.
- *Fix:*
  1. Make `refused()` return the SystemExit's text, and have each check assert it ("outside the repository"; "YYYY-MM-DD").
  2. For "before anything loads", snapshot `sys.modules` and assert that `transformers` and `tokenizers` were not newly imported. hftiny runs after these checks, so the snapshot is clean.

**F5 — RISK — ids.py:330–336, 343 and 361. The special-token assertion is complete, but its only test (S3, 694–695) cannot show that.**
- *What the code does:* it asserts on every text that needs it: each passage, and each context's prefix and full. Those are the texts A3's recipe encodes: `span_start` encodes the prefix and the full (extract.py:77–78), and `capture` encodes the full (109).
- *What the test does:* S3 changes every text at once, so it cannot show that any one class is checked. `special_tokens_differ` is never asserted.
- *Note on the counter:* it counts encodes, not texts. A task's prefix is checked once per context, 28 times.
- Mutants M3–M6 survive.
- *Fix:* add three variants of S3, each with an `encode_special` that differs on one class only: passages, the prefix, and the fulls. Each must STOP, with `special_tokens_differ` at 3, 2 and 2 respectively. S3 itself should assert 7.

**F6 — NIT — ids.py:339. A malformed passage line crashes instead of STOPping.**
- *What:* `json.JSONDecodeError` escapes render_iv as a crash with no report. Every other bad input notes a line and STOPs.
- This cannot happen on the adopted bytes.
- *Fix:* catch ValueError, note `passage line {i + 1}: not JSON`, and continue.

**F7 — NIT — ids.py:364–366. The span rule is a copy of `extract.span_start`'s loop, not a call to it.**
- *What:* the driver has already imported `valence_core.extract` (box_e0_corpus.py:51), yet render_iv carries its own copy of the loop. The copy is faithful today, but a later change to the recipe would not reach the render.
- *Fix:* in the driver, compute `extract.span_start(shim, c.prefix, c.full)` for each context, with `shim.encode = enc_special`, and pass the list in. render_iv STOPs wherever its own k differs.

**F8 — NIT — n_sessions.py:229–230. The comment on `enc_special` is not literally true.**
- *What:* the comment says "the adapter's default, which A3's capture used". The adapter calls `self._tok.encode(text, add_special_tokens=…)` (the HF adapter under valence_core/adapters/, 95–98). The draft calls `tok(text, add_special_tokens=True)["input_ids"]`.
- By my reading, the two give the same ids for a fast tokenizer.
- *Fix:* call `tok.encode(text, add_special_tokens=True)`, so the comment is literally true.

**F9 — NIT — n_sessions.py:68–69 (`render_out`, called at 206); ids.py:386 and 407. Two problems with refusal messages.**
- *Wrong command named:* an --out under data/n/bk gets render_out's text, "render-ids writes inside the repository only under data/n/ids/, not {p}". It names the other command, and it implies that data/n/ids/ is admitted, which render-ids-iv refuses.
- *Absolute paths:* that text, and render_iv's `{out}: not empty …` and `{out}: the folder does not read back …`, print absolute paths. A raw that prints the output whole would then carry the scratch path, which embeds the home folder's name.
- *Fix:* in cmd_render_ids_iv, test `_within(REPO)` first, with its own message, then call `guard.refuse_out`. Name folders by their basename in messages.

**F10 — NIT — ids.py:274–276 and 405–407. Nothing checks at the byte level that the base fields are unchanged.**
- *What:* `load` admits any `iv` block; for example, `{"pi_date": "x"}` passes when five files are listed.
- *Why a byte-level check is possible:* `_dumps` is canonical, and `render` wrote the base as `_dumps(manifest) + "\n"`. So the five-file manifest determines the base's bytes.
- *Fix:* drop `iv` and the two (iv) entries, apply `_dumps`, add a newline, and hash the result. The hash must equal `iv.base_manifest_sha256` and MANIFEST_I_III. Assert this in the read-back and in C2, and optionally in `load` whenever `iv` is present.

**F11 — NIT — verify.py:19–21; ids.py:71–72. Two comments go stale when the pin moves.**
- verify's docstring still calls the default pin "the committed render's at d76f34f".
- ids.py's comment keeps the clause "(i)-(iii)'s until (iv)'s render is committed".
- *Fix:* update both in the commit that moves the pin.

**F12 — NIT — n_sessions.py:204. The date check only checks the shape.**
- 2026-13-45 passes, as it does in render-ids (168).
- *Fix:* use `datetime.date.fromisoformat`.

## The self-test, check by check
By my count there are 19 new executed checks: 17 in `ids._selftest` and 2 in the driver.

| Check | Line | Does it test what its name says? |
|---|---|---|
| C1: PASS writes six files | 647 | Yes. |
| C2: manifest kept and extended | 653 | Yes, on parsed values. `iv.conventions` is never read, and there is no byte-level check (F10). |
| C3: copied byte for byte | 659 | Yes. |
| C4: passage record | 662 | Yes, for passage 0 and for s-02's index. Under the character tokenizer, "alone" and "with special tokens" coincide by construction. |
| C5: context record | 667 | Yes, for context 1, except `ids_sha` (M7). |
| C6: report carries counts and sha256s, no id | 671 | Only partly. "No id" is checked by key name only, so ids under another key, or inside a problem line, would pass. The sha256s in the `files` block are never read, though they are the source of the next pin (M8). `seq_len` is never read (M20). |
| C7: writes once | 677 | Yes, for a non-empty folder. |
| S1 | 690 | Yes. |
| S2 | 692 | Yes for the pin; the file-set clause is untested (M2). |
| S3 | 694 | Changes every text at once (F5; M3–M6). |
| S4 | 696 | No. Its case, full == prefix, is also refused at 367, so neither the startswith clause nor the degenerate-span test is tested on its own (M9–M11). |
| S5 | 698 | Yes, but the early clause is masked by the ok gate at 375 (M16). |
| S6 | 700 | Tests one form of "not exactly", a missing key. An extra key and a non-string value are untested (M13, M14). |
| Merge | 705 | Yes. |
| L1 | 715 | Yes. |
| L2 | 723 | Yes, but both load clauses fire on its input (M17). |
| Pins | 726 | Checks 8-hex prefixes and counts only; the (iv) file names are not pinned (M19). |
| Driver checks | 122, 126 | See F4. |

## Surviving mutants
Each is a one-line change that the self-test does not kill, followed by the test that would.

- **M1** — ids.py:318, the environment and tokenizer comparison becomes `if False:`. No test passes an environment or tokenizer sha256s other than the base's, and `stop_iv` cannot override them. *Kill:* STOP with env `{**ENV_OF_RECORD, "transformers": "5.15.0"}`, and again with one tokenizer digest changed; nothing written in either case.
- **M2** — ids.py:315, drop `or sorted(bman["files"]) != sorted(FILES_I_III)`. *Kill:* render_iv with base_dir set to the iv_ok folder and base_pin set to its own manifest's sha256 must STOP.
- **M3** — ids.py:361, `a = [int(x) for x in encode(prefix)]`, so the prefix is unchecked. *Kill:* an `encode_special` that adds a token only to the exact prefix text must STOP, with `special_tokens_differ` 2.
- **M4** — ids.py:361, `b = [int(x) for x in encode(full)]`, so the full is unchecked. *Kill:* an `encode_special` that changes only texts longer than the prefix and starting with it must STOP, with count 2.
- **M5** — ids.py:343, `ids = [int(x) for x in encode(r["text"])]`, so passages are unchecked. *Kill:* an `encode_special` that changes only the passage texts must STOP, with count 3.
- **M6** — ids.py:333, delete `rep["special_tokens_differ"] += 1`. *Kill:* S3 asserts the count is 7.
- **M7** — ids.py:373, `"ids_sha": ids_sha(a)`. Nothing reads an A3 record's ids_sha, and the read-back compares gvec's only. *Kill:* every record of both files satisfies `ids_sha(r["ids"]) == r["ids_sha"]`, checked in the self-test and in the read-back.
- **M8** — ids.py:409, the report gives MANIFEST.json's sha256 as `base["manifest_sha256"]`. `rep_iv["files"]` is never read, yet this is the value the pin step would read. *Kill:* the report's `files` equals the six on-disk sha256s and counts. Separately, the pin should be taken from `shasum` of the copied file, never from the report.
- **M9** — ids.py:358, `if full == prefix:`. *Kill:* a context whose full does not start with its prefix (for example "Task: u\n…") must STOP.
- **M10** — ids.py:367, `if not 0 <= k < len(b):`. *Kill:* an encoder that prepends an id to one full only gives k = 0 and must STOP.
- **M11** — ids.py:367, `if not 0 < k <= len(b):`. *Kill:* an encoder that maps one full to the prefix's ids gives k = len(b) and must STOP.
- **M12** — ids.py:352, the uniqueness check becomes `if False:`. *Kill:* two passages with id "s-00" must STOP.
- **M13** — ids.py:340, drop the `isinstance(r[k], str)` clause. *Kill:* a line with `"pole": 1` must STOP, with nothing written.
- **M14** — ids.py:340, `not set(PASSAGE_KEYS) <= set(r)`. *Kill:* a line with a fifth key must STOP.
- **M15** — ids.py:344, `if ids is None:`. *Kill:* a passage with text "" must STOP with the "no tokens" line.
- **M16** — ids.py:326, drop `or len(contexts) != expect_contexts`. S5 still STOPs, but with no problem line. *Kill:* S5 asserts its problem line names the counts.
- **M17** — ids.py:274, drop the `names not in (...)` clause. *Kill:* a four-file manifest ((i)–(iii) plus gvec) without an iv block must be refused.
- **M18** — ids.py:275, `or (names == sorted(FILES_I_III + FILES_IV) and "iv" not in manifest)`. *Kill:* three files with an iv block must be refused.
- **M19** — ids.py:65, `GVEC_FILE = "gvec_passage.jsonl"`. *Kill:* `FILES_IV == ("gvec_passages.jsonl", "a3_contexts.jsonl")`, the names in ADDENDUM-n1 §1.2 (iv).
- **M20** — ids.py:381, `seq_len = [min(...), min(...)]`. *Kill:* seq_len equals `[len(enc(ctx[1][1])), len(enc(ctx[0][1]))]`.
- **M21** — n_sessions.py:207, `if False and _within(...)`. It survives at the box; in G-DATA's environment it aborts the run (F4). *Kill:* assert the refusal text.
- **M22** — n_sessions.py:204, the date check becomes `if False:`. Same pattern and same kill as M21.
- **M23** — n_sessions.py:230, `add_special_tokens=False` in `enc_special`. The driver's encoders are exercised by no test, so the render would PASS with a vacuous assertion. *Kill:* factor the two encoders into a helper that takes `tok`, and test it with a stub tokenizer that records the flag.
- **M24** — n_sessions.py:222, iterate `sorted(e0.e0_contexts(), key=lambda c: c.condition)`. This is untested, and the render would PASS while committing a non-A3 order. *Kill:* a model-free check that the list passed to render_iv equals `e0_contexts()` in order, or the `contexts_sha256` from F2.
- **M25** — n_sessions.py:232, `a3_input_shas={}`. This is untested, and the manifest would carry an empty provenance block. *Kill:* assert that the iv block's `a3_input_shas` equals `box_e0_corpus.FROZEN_SHA`.

Three equivalent mutants are noted, not counted:
- Deleting 406–407: once `load(out)` has checked every file against sha256s taken from the same bytes, the comparison cannot fail.
- At 370, `!=` → `<`: k ≤ len(a) always.
- At 291, `GVEC_FILE in out` → `A3_FILE in out`: `load` admits both (iv) files or neither.

## Observations for the design seat
- **O1. The manifest is extended in place.** MANIFEST_OF_RECORD moves from 7f51bd91… to the sha256 of the (i)–(iv) manifest, and rendering (v) would move it again. ADDENDUM-n1 §1.5 puts MANIFEST.json's sha256 in LOCK-n v0.1's "rendering and spans", and no LOCK-n file is at the root today. So whether LOCK-n v0.1 is placed before or after (v) decides whether its pin survives (v). A separate (iv) manifest that names (i)–(iii)'s by sha256 would leave G-VER's pin where it is.
- **O2. Schema and dates.** The five-file manifest keeps schema "n-ids-v1", so `load` accepts both shapes under one schema id. It also keeps (i)–(iii)'s top-level pi_date, 2026-11-16; (iv)'s date is `iv.pi_date`. (iv)'s environment and tokenizer files are recorded only as equal to the base's, which ids.py:318 asserts.
- **O3. The special-token assertion also binds the passages.** By definition the passages' convention is no special tokens (directions.py:10–11). A tokenizer that added a token under `add_special_tokens=True` would STOP the passages as well as A3.
- **O4. Where the coincidence of conventions is established.**
  - It is established in G-DATA's environment only.
  - A3's own runs encoded on the box, and ADDENDUM-n1 §0.1 shows a box environment tokenizing the same files differently: under transformers 5.15.0, BK's sessions came to 1,225–1,233 tokens against 1,273.
  - So the committed A3 ids are G-DATA's rendering of A3's texts, not a record of what A3 ran.
  - A descriptive comparison is available. box_a3_extract.py writes `span_len_min_max_mean` into each stage's A3 record (209–210). The render's report gives span_len as [min, max] only; adding the mean would make the comparison like for like.
- **O5. Rule-18 hygiene.** A3's run asserts rule-18 hygiene before it captures (box_a3_extract.py:134). The render does not. It changes no id; G-VEC's wiring is the place for it.
- **O6. Merges across the boundary.**
  - The render follows `extract.span_start`, so a span may start before the prefix's own token count.
  - It records `prefix_tokens` beside `span_start`, and counts `prefix_differs` without stopping.
  - Rule 28(d)'s standing form (a) asserts that the boundary equals the prefix token count. That rule is scoped to positional delivery under a length-limited encode, and A3's capture is neither.
  - `prefix_differs` is the figure the seat would see.
- **O7. Running from a scratch overlay**, as (i)–(iii) did, makes REPO the overlay:
  - the "outside the repository" refusal and `guard.refuse_out` then guard the overlay, not the checkout;
  - A3's text comes from the overlay's `box_e0_corpus.py` and `extract.py` (F2).
- **O8. Re-rendering after the (iv) commit.** render-ids-iv then refuses itself, because data/n/ids/ no longer hashes to MANIFEST_I_III. A re-render or a values-check reproduction would need a base folder at d76f34f, and the driver has no `--base-dir` option.
- **O9. Commit order.** If the files and the pin edit land in separate commits, HEAD between them has G-VER STOP on the pin. The pin edit also changes the n package's sha256.
- **O10. Digest lengths.** The A3 input digests are FROZEN_SHA's 16-hex truncations; every other digest in the manifest is a full sha256.

## Totals
- **Findings: 12.** BUG 0, RISK 5 (F1–F5), NIT 7 (F6–F12).
- **Surviving mutants listed: 25** (M1–M25), each with a test that kills it. Three equivalent mutants are noted separately.

```
