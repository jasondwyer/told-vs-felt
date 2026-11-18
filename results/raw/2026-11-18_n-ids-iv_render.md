# n — ids of record, second commit: the render of ADDENDUM-n1 §1.2 (iv) in G-DATA's environment, 544 passages and 1,344 A3 contexts

*The n-build session (Code), PI date 2026-11-18. Under ADDENDUM-n1 v0.1 §1.2 (iv) and §1.5. The seat's answers of
2026-11-18 (`results/raw/2026-11-18_n-corpus-adoption_design-to-code_answers.md`, committed at `26cf7d2`), §3 item 3,
are routed by the PI's item 4 of that date: "then the render of ADDENDUM-n1 §1.2 (iv) in a window (no box needed)".
On the laptop, model-free: tokenizer files only, no weights. The token ids are in the committed files under
`data/n/ids/`; this raw prints none.*

## The runs

All runs were in battery windows the coordinating session granted on 2026-11-18. Each was one process at
`nice -n 19`, with the Hugging Face libraries offline (`HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`), `TMPDIR` in
Code's scratch, and the jlens venv's interpreter reached as `cd jl*/.venv/bin && ./python`, so no guard marker was in
an argv. Each ran from Code's scratch overlay: HEAD's tracked files on the paths the runs use (`valence_core/`, the
two scripts, `data/n/`, the e0 corpus files, the model manifest), with the drafts in place. `<scratch>` stands for
Code's scratch folder.

| run | what | drafts | result |
|---|---|---|---|
| 1 | `--selftest` | as reviewed: `ids.py` `2bb137ea…f31f`, `n_sessions.py` `0bcc05ea…a4cb` | 236/236, exit 0 |
| 2 | `--selftest`, then `hashes` | with the review applied but F11 (its two comments came with the pin's move, run 4): `ids.py` `d52af8c4…76db`, `n_sessions.py` `a7b79386…7330` | 266/266, exit 0; package `e4da7cf6…7c98` |
| 3 | `render-ids-iv`, the render of record | as run 2 | PASS, exit 0 (output whole, below) |
| 4 | `--selftest`, `hashes`, `gver-trial` | the pin moved: `ids.py` `28157d89…4809`, `verify.py` `4de26209…d516`, `n_sessions.py` as run 2; the overlay's `data/n/ids/` holding the render's six files | 267/267, exit 0; package `f927608c…3c03`; G-VER trial PASS |

The render's command, run 3:

```text
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUTF8=1 TMPDIR=<scratch>/iv/tmp3 nice -n 19 <python> \
    <scratch>/iv/overlay/scripts/n_sessions.py render-ids-iv \
    --tokenizer-dir <scratch>/tok_n --out <scratch>/iv/out_render --pi-date 2026-11-18
```

`<python>` is the jlens venv's interpreter. `PYTHONDONTWRITEBYTECODE=1` was also set on every run.

## What the render asserts, and what it writes

**Before it renders,** `render-ids-iv` refuses:
- a PI date that is not a calendar date written YYYY-MM-DD;
- an `--out` inside the repository, with its own message, or under `guard.refuse_out`'s roots;
- any run outside Python's UTF-8 mode;
- any environment but G-DATA's;
- a tokenizer folder that is not exactly the three files at the manifest's pins;
- A3's inputs if they are not frozen (`box_e0_corpus.assert_frozen_inputs`).

**`ids.render_iv` then STOPs, writing nothing,** unless all of these hold. A base that fails `load`, or an `--out` or
staging folder that already exists, is a refusal instead; nothing is written either way.
- the committed (i)–(iii) folder loads, its manifest at `MANIFEST_I_III` (`7f51bd91…821d`) with exactly its three
  files, under the same environment and tokenizer digests;
- the corpus is the one adopted (`ef6b00dc…3cc3`);
- 544 passages and 1,344 contexts;
- every passage is a record of exactly `id`, `state`, `pole` and `text`, all strings, with unique ids and at least one
  token each;
- every context's full extends its prefix, with a span start strictly inside it, equal to `extract.span_start`'s own
  boundary;
- on every passage, prefix and full, adding special tokens changes no id.

**What it writes.** It builds a complete ids folder in a staging folder beside `--out` and renames it into place only
after reading it back:
- (i)–(iii)'s three files, copied byte for byte and re-checked as copied;
- `gvec_passages.jsonl`: per passage, in the corpus's order, its index, id, state, pole, the text's sha256, its token
  count, `ids_sha` and ids;
- `a3_contexts.jsonl`: per context, in A3's order, its index, item id, condition, variant, the prefix's and the full's
  sha256s, `seq_len`, `span_start`, the prefix's own token count, `ids_sha` and ids;
- `MANIFEST.json` extended. (i)–(iii)'s fields and entries are kept; the two files are added; and an `iv` block holds
  its PI date, the base manifest's sha256, the corpus's sha256, A3's provenance (the three frozen input digests, the
  sha256s of the two files that build its texts, and the contexts' digest and count) and the conventions.

## Code's readings, flagged for the seat

- **R-iv1, the passages.** Each passage is encoded alone, with no special tokens and no template: `directions.py`'s
  reading, declared at the BUILD. The records keep the corpus's `state` field (`flow_engagement`); its mapping to BK's
  words is G-VEC's wiring, as ruled.
- **R-iv2, A3's contexts.**
  - The contexts are the frozen 1,344 of `e0_contexts()`, in its order: 48 tasks × 7 conditions × 4 paraphrases.
  - Each full is encoded whole, and its span starts at `extract.span_start`'s boundary. The render computes the
    boundary itself and asserts it equal to `extract.span_start`'s own.
  - The prefix's own token count is recorded beside the span start. On these texts the two never differ
    (`prefix_differs` 0).
- **R-iv3, special tokens.** A3's capture encoded through the adapter's `encode`, whose default adds special tokens;
  n's ids add none.
  - The render asserted, on every encode (the 544 passages, and each of the 1,344 contexts' prefix and full, a
    task's prefix once per context: 3,232 in all, over 1,936 distinct texts), that `tok.encode(text,
    add_special_tokens=True)` gives the ids that `tok(text, add_special_tokens=False)` gives.
  - So under G-DATA's tokenizer files the two conventions coincide here; any difference would have STOPped the
    render.
  - The tokenizer's `post_processor` is null, as the review noted.
- **R-iv4, the manifest extended in place**, as the seat's §3 item 3 asks.
  - `MANIFEST_OF_RECORD`, G-VER's pin, moves from `7f51bd91…821d` to `fdf73d85…ef38`.
  - Both are named in the code: `MANIFEST_I_III` is the base, and `load` re-derives the base from the new manifest
    byte for byte.
  - The schema id stays "n-ids-v1".
- **R-iv5, UTF-8.** The render requires Python's UTF-8 mode, so A3's files decode as UTF-8 whatever the locale. Their
  texts carry non-ASCII characters: em dashes, in 8 task completions and 4 frames. (The frames file's `_doc` also holds
  a §, which no context uses.)
- **R-iv6, the overlay.** The render ran from a scratch overlay of HEAD's files plus the drafts, as the (i)–(iii)
  render did.
  - The two files that build A3's texts are recorded in the manifest by sha256: `scripts/box_e0_corpus.py`
    `66c18554…ab57` and `valence_core/extract.py` `2405b1a6…07fe`. Both equal HEAD's.
  - The overlay's other n modules equal HEAD's, `ids.py` and `verify.py` excepted.

## The tokenizer folder

It is the folder the (i)–(iii) render used (`<scratch>/tok_n`; its provenance is in that render's raw): exactly
`tokenizer.json` `73fd5254…ecca`, `tokenizer_config.json` `fff5b944…3fc7` and `special_tokens_map.json` `78afb564…e2f2`,
the manifest's `olmo2_instruct` pins. The render checked them again (its output, lines 3–5). Nothing was downloaded.

## Run 3's output, whole

Local paths are written as `<scratch>`.

```text
PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
environment: python 3.12.9 | transformers 5.5.0 | tokenizers 0.22.2
tokenizer file special_tokens_map.json 78afb564e81264029b25f9caf24bda2521d5bdaeff5cd3fdbc01d3da2e8ce2f2 = the manifest's olmo2_instruct
tokenizer file tokenizer.json 73fd5254624f39a88e3faac6a8e11300fc3c735ed37880d4f4f08db898eaecca = the manifest's olmo2_instruct
tokenizer file tokenizer_config.json fff5b9441e8fe1d696eebed3541e719776e5b096692ef38cea68b891fc4f3fc7 = the manifest's olmo2_instruct
A3's inputs frozen: {"corpus_sha": "3c53e5a54fbaa233", "frames_sha": "9654b9398743116f", "probes_sha": "ec2296182e726969"}; the files that build its texts: {"scripts/box_e0_corpus.py": "66c185542db97350e2417aa8122eeccc3d348a7ca7c6d06b902951ae8c11ab57", "valence_core/extract.py": "2405b1a687f9f882472b06fa3f9b8d47b20206414ada1b854b3c93a02d7a07fe"}; 1344 contexts
render-ids-iv (ADDENDUM-n1 §1.2 (iv)):
{"a3_contexts": {"contexts_sha256": "9cfd90aa7fad2f52b85c3e38b994f9df2012a931cb61b03747db94a24a5c4802", "n": 1344, "ok": 1344, "prefix_differs": 0, "seq_len": [32, 90], "span_len": [10, 16.82, 29]}, "files": {"MANIFEST.json": {"records": 5, "sha256": "fdf73d854ebd6fbe02ced28a0c49af1c9658763627aaaa55afd781084f80ef38"}, "a3_contexts.jsonl": {"records": 1344, "sha256": "757026e8260fd2d3080e88a6f6a4ba00c85fef957ee021c66418e2f85a6bd84c"}, "gvec_passages.jsonl": {"records": 544, "sha256": "444352c156aad9aa238fd5377b1192bbcbcaecbf70c9e9ee4603569eafb333a5"}, "labels.json": {"records": 4, "sha256": "43a32a1b7dec52f239020fb916e5ae9e2758be10ed232d762edcd5d048a549da"}, "n4_variants.jsonl": {"records": 320, "sha256": "e887f19ede4a1b2ca42cfeffe41f4ee81f67774b5bfcd58e0f3765739834b702"}, "sessions.jsonl": {"records": 160, "sha256": "fd8bb2341aaf7d4b1365873564d1e858a3cace4fb5cc578e4bd827c4ee14a45a"}}, "first_problems": [], "passages": {"n": 544, "n_tokens": {"contentment": [38, 46.8, 59], "distress": [41, 52.6, 63], "dread": [41, 51.6, 62], "flow_engagement": [41, 51.2, 61], "frustration": [47, 54.7, 68], "neutral": [35, 43.4, 57], "relief": [41, 49.7, 61], "serenity": [39, 45.8, 57], "weariness": [38, 51.5, 66]}, "ok": 544}, "special_tokens_differ": 0, "status": "PASS"}
```

The first line is the transformers library's notice that PyTorch is absent from the venv, as at the (i)–(iii) render.
The report:
- **Counts.** 544 of 544 passages and 1,344 of 1,344 contexts rendered; `special_tokens_differ` 0; `prefix_differs`
  0; no problem line.
- **Token counts per state** (min, mean, max): contentment 38/46.8/59, flow_engagement 41/51.2/61, relief
  41/49.7/61, serenity 39/45.8/57, distress 41/52.6/63, frustration 47/54.7/68, weariness 38/51.5/66, dread
  41/51.6/62, neutral 35/43.4/57.
- **A3's contexts.** `seq_len` 32–90; the span (the Reviewer turn) 10–29 tokens, mean 16.82; the contexts' digest
  `9cfd90aa…4802`.

## The files, as committed under `data/n/ids/`

Each file is the render's output, copied from `<scratch>/iv/out_render/`. The three (i)–(iii) files are byte-equal to
those committed at `d76f34f`.

| file | records | sha256 |
|---|---|---|
| `sessions.jsonl` | 160 | `fd8bb2341aaf7d4b1365873564d1e858a3cace4fb5cc578e4bd827c4ee14a45a` |
| `n4_variants.jsonl` | 320 | `e887f19ede4a1b2ca42cfeffe41f4ee81f67774b5bfcd58e0f3765739834b702` |
| `labels.json` | 4 | `43a32a1b7dec52f239020fb916e5ae9e2758be10ed232d762edcd5d048a549da` |
| `gvec_passages.jsonl` | 544 | `444352c156aad9aa238fd5377b1192bbcbcaecbf70c9e9ee4603569eafb333a5` |
| `a3_contexts.jsonl` | 1344 | `757026e8260fd2d3080e88a6f6a4ba00c85fef957ee021c66418e2f85a6bd84c` |
| `MANIFEST.json` | 5 files | `fdf73d854ebd6fbe02ced28a0c49af1c9658763627aaaa55afd781084f80ef38` |

## The package

- **Before the pin's move.** Run 2's `hashes` gave `package_sha256 valence_core/n e4da7cf6…7c98`, with the drafts as
  rendered.
- **As committed.** With `MANIFEST_OF_RECORD` at the new manifest and the comment fixes (F11), run 4's `hashes` gave
  `package_sha256 valence_core/n f927608c33d12b34c2bef728966038dac1ecfbb041cbd992b7ffd4cf01a73c03`. This is the
  package of record from this commit.
- **The closure.** Its eleven closure lines are run 2's, unchanged.
- **Reproduced in the shell.** Code recomputed the package digest without Python, by `m.resume.package_sha256_of`'s
  rule (each `valence_core/n/*.py` in C-locale order, as its path, its byte count and its bytes). The overlay gives
  `f927608c…3c03`. HEAD's tree before this commit gives `60d892dc…cc66`, the BUILD's.

Run 4's `hashes`, whole:

```text
package_sha256 valence_core/n f927608c33d12b34c2bef728966038dac1ecfbb041cbd992b7ffd4cf01a73c03
imported_sha256 valence_core/__init__.py 620ad380f023dc8c173ee4e164a160c0b1da2a0c0b99fb6c9717be0b8c78b604
imported_sha256 valence_core/adapters/__init__.py 96d6b48dd41710de8c70ce7d5b28854db4810af6693ff8a96f320f773cafed6a
imported_sha256 valence_core/adapters/base.py 626fbddd8dd970717e929b5bcd87be4e0c83ca8cb889b8451fcb49e2cb091cbf
imported_sha256 valence_core/adapters/olmo_hf.py df80b79b205c64121187ab0b307e5f35db5bd6632d45940a980c0175b8a092dc
imported_sha256 valence_core/discrim.py 7d171ae7b416b33a9f881a277606ace4a6891ce30c96943c3b0a41bd75d2de89
imported_sha256 valence_core/echo/__init__.py 71a6ec160a1d7beefc7f8c37c106f2fca742adc862fd9b737b7750218bf00e43
imported_sha256 valence_core/echo/probe.py d90f9281dff612977da5a3c3ce1a07155159a48103b35dfe521e0fac30152b81
imported_sha256 valence_core/m/__init__.py b5175bcb6a521ef277de105315dd8d2f637a7b03e5d7baf30406dd83d0db35c4
imported_sha256 valence_core/m/keys.py a7d5ee3a9cde0deed785df204ae840cb56ee0e1eeefa9192fe1c1b0abb6b3beb
imported_sha256 valence_core/m/resume.py 78f2fc8eb8b3b16ffa39c6dac7022b37dc98d8d002f50390d5c4540f22bf8fb7
imported_sha256 valence_core/session_e2a.py f1e53db2e9089ed3869e75693474fa6f36eccf667d1f2a4fbe52b4ba1fe73c71
```

## Run 4's G-VER trial, whole

It ran on the assembled folder: the committed (i)–(iii) plus the render's three new files, in the overlay's
`data/n/ids/`. The tokenizer was loaded to decode only, from `<scratch>/tok_n`. Its printed `manifest_ok` covers the
environment, the tokenizer files and the session set; the pin is not printed, and PASS requires the manifest at it
(`verify.py`'s `pin_ok`):

```text
PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
G-VER trial (the BUILD's site check; never of record):
{"first_problems": [], "ids_ok": 160, "labels_kept": 4, "labels_ok": 4, "manifest_ok": true, "n4_ok": 160, "sessions": 160, "spans_ok": 160, "status": "PASS"}
```

The self-tests' outputs, each one line, whole:
- run 1: `  236/236 n selftest checks pass`;
- run 2: `  266/266 n selftest checks pass`;
- run 4: `  267/267 n selftest checks pass`.

Run 4 adds one check to run 2's 266: the committed `data/n/ids/` is (i)–(iv), its MANIFEST.json at `MANIFEST_OF_RECORD`,
extending (i)–(iii)'s. Run 2's 266 are the BUILD's 217, plus 45 for (iv) in `ids.py` and 4 in the driver.

## The review

A blind review of the drafts reported 12 findings (0 BUG, 5 RISK, 7 NIT) and 25 surviving mutants. Every finding is
applied: F1–F10 and F12 in the drafts runs 2–4 ran, and F11 at the pin's move (run 4). Every mutant has a test
written to kill it, in the drafts runs 2–4 ran; the mutants were not run. The report as returned and each disposition
are in
[`2026-11-18_n-ids-iv_review.md`](2026-11-18_n-ids-iv_review.md).

## Departures

Before the render, while Code built the scratch overlay and read the adapter on 2026-11-18, three shell commands
carried a guard marker in their argv:
- a `grep` over the HF adapter file;
- a name-only `ls -d ol*` in `data/`;
- `git archive HEAD -- … data/<the model folder>/manifest.json`, piped to `tar` into the overlay.

None ran Python, loaded a model, or touched `data/mf3`, a `ckpt` or a `reports` path. The archive read the
repository's objects and wrote only into scratch. They were disclosed to the coordinating session at the time, for
Q-F3's run list.

## Observations for the seat

- **The pin.** G-VER's pin moves to `fdf73d85…ef38`. Rendering (v), G-CAL-n's prompts, will move it again. LOCK-n
  v0.1's "rendering and spans" (ADDENDUM-n1 §1.5) names whichever is committed when the lock is drafted. (The review's
  O1.)
- **Whose rendering the A3 ids are.** They are G-DATA's rendering of A3's texts, as ADDENDUM-n1 §1.1 makes G-DATA's
  environment n's tokenizer of record. They are not a record of what A3 ran on any box. The span's mean (16.82) is
  printed for comparison with A3's own `span_len_min_max_mean`. (The review's O4.)
- **Rule 18 for A3.** A3's own run asserted rule-18 hygiene before it captured. The render does not, since it changes
  no id; G-VEC's wiring is the place for it. (The review's O5.)
- **A re-render.** A re-render of (iv), or a reproduction by a values-check, needs a base folder at `d76f34f`. From
  this commit on, `render-ids-iv` STOPs on its own output as a base (its MANIFEST.json is not at `MANIFEST_I_III`), and
  the driver has no option to name another base. (The review's O8.)
