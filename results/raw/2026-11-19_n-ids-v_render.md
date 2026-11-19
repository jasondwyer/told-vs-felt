# n — ids of record, third commit: the render of ADDENDUM-n1 §1.2 (v) in G-DATA's environment, G-CAL-n's 48 prompts in the rendering of record

*The n-build session (Code), PI date 2026-11-19. Under ADDENDUM-n1 v0.1 §1.2 (v) and §1.5, and the seat's answers of
2026-11-19, first sitting (`results/raw/2026-11-19_n-starred-twelve_design-to-code_answers.md`, committed at
`a33252a`): §1.7 (Q7, "the 48 prompts stand … (v)'s render goes") and §1.8 (Q8: "the generations and (v)'s render use
the rendering of record"), routed by the PI's item 2 of "N. n-build (and the pod session on the box)", on "Route as
given". On the laptop, model-free: tokenizer files only, no weights. The token ids are in the committed files under
`data/n/ids/`; this raw prints none.*

## The runs

All three runs were in battery windows the coordinating session granted on 2026-11-19, each process at `nice -n 19`,
with the Hugging Face libraries offline (`HF_HUB_OFFLINE=1`, `TRANSFORMERS_OFFLINE=1`), `TMPDIR` in Code's scratch,
`PYTHONDONTWRITEBYTECODE=1`, Python's UTF-8 mode (`PYTHONUTF8=1`) on runs 1 and 3, and the jlens venv's interpreter
reached as `cd jl*/.venv/bin && ./python`, so that no guard marker was in an argv. Run 1 ran from Code's scratch
overlay, 161 files of HEAD `035947e` on the paths the runs use, checked equal to HEAD's blobs by tool before it (161
joined, 0 differing, 0 untracked). Runs 2 and 3 ran from the same overlay with `ids.py` replaced by the pin's move and
`data/n/ids/` holding the render's seven files (`MANIFEST.json` replaced, `gcal_prompts.jsonl` added). `<scratch>`
stands for Code's scratch folder.

| run | what | bytes | result |
|---|---|---|---|
| 1 | `render-ids-v`, the render of record | HEAD `035947e`'s code, unchanged | PASS, exit 0 (output whole, below) |
| 2 | `--selftest` | the pin moved, `ids.py` `fd3e9c63…7022`; the render's seven files in place | 545/545, exit 0 |
| 3 | `hashes`, then `gver-trial` | as run 2 | both exit 0: the package digest, and G-VER PASS (outputs whole, below) |

Run 1's command:

```text
HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 PYTHONUTF8=1 TMPDIR=<scratch>/step4b/v/tmp PYTHONDONTWRITEBYTECODE=1 \
    nice -n 19 <python> <scratch>/step4b/gcal/overlay/scripts/n_sessions.py render-ids-v \
    --tokenizer-dir <scratch>/tok_n --out <scratch>/step4b/v/out_render --pi-date 2026-11-19
```

Run 2's is G-CAL-n's self-test command, `<python> <scratch>/step4b/gcal/overlay/scripts/n_sessions.py --selftest`,
with `TMPDIR=<scratch>/step4b/gcal/tmp`. Its output is one line, sha256
`af912421488c638ecd1502e05ad4c7a6c04e5554820d110417e5d158a9a4f158`, verbatim:

```text
  545/545 n selftest checks pass
```

Its line is byte-equal to the count line of G-CAL-n's draft 6 run (`results/raw/2026-11-19_n-gcal-delta_selftest.txt`,
run 6; the same sha256): the pin's move changes the ids check it carries, not the count.

Run 3's two commands, in turn, with `TMPDIR=<scratch>/step4b/gcal/tmp`:

```text
<python> <scratch>/step4b/gcal/overlay/scripts/n_sessions.py hashes
<python> <scratch>/step4b/gcal/overlay/scripts/n_sessions.py gver-trial --model-dir <scratch>/tok_n
```

Their outputs are whole in the package's section and in G-VER's, below.

## What the render asserts, and what it writes

**Before it renders,** `render-ids-v` refuses any arguments but `--tokenizer-dir`, `--out` and `--pi-date`; a PI date
that is not a calendar date written YYYY-MM-DD; an `--out` inside the repository, or under `guard.refuse_out`'s roots;
any environment but G-DATA's (`ids.check_environment`: python 3.12.9, transformers 5.5.0, tokenizers 0.22.2); and a
tokenizer folder that is not exactly the three files at the manifest's `olmo2_instruct` pins
(`ids.check_tokenizer_dir`). In an overlay run, "the repository" is the overlay's root, so an `--out` inside the
working repository would not be refused from an overlay; run 1's `--out` was outside both.

**`ids.render_v` then STOPs, writing nothing,** unless all of these hold. A base that fails `load`, or an `--out` or
staging folder that already exists, is a refusal instead; nothing is written either way.
- the committed (i)–(iv) folder's manifest is at `MANIFEST_I_IV` (`fdf73d85…ef38`) with exactly its five files, under
  the same environment and tokenizer digests;
- the end-of-turn text, `<|endoftext|>`, encodes to one id;
- `gcal.plan` gives 48 prompts over the 12 labels of record;
- for every prompt, its user turn and its whole text (`gcal.prompt_parts`) encode so that the whole begins with the user
  turn's own ids, the first id where they leave it (`gen_start`) equal to the user turn's count, strictly inside the
  whole.

**What it writes.** A complete ids folder, built in a staging folder beside `--out` and renamed into place only after
it reads back (every record's `ids_sha` re-derived; the (i)–(iv) part of the new manifest re-derived to
`MANIFEST_I_IV`):
- (i)–(iv)'s five files, copied byte for byte and re-checked as copied;
- `gcal_prompts.jsonl`: per prompt, in the plan's order, its index, label, replicate, seed, the user turn's and the
  whole text's sha256s, the user turn's token count, `gen_start`, `seq_len`, `ids_sha` and ids;
- `MANIFEST.json` extended: (i)–(iv)'s fields and entries kept, the file added, and a `v` block with its PI date, the
  base manifest's sha256, the labels, the prompt count, the end-of-turn id and text, the prompt template and the two
  conventions.

## Code's readings, flagged for the seat

- **R-v1, the prompts.** BK's zone prompt over the 12 labels of record × 4, prompt i label i mod 12 and replicate
  i // 12, each a single opening user turn in the rendering of record (`gcal.prompt_parts`: the user turn
  `<|user|>\n` + the prompt + `\n`, the generation prompt `<|assistant|>\n`), encoded whole with no special token added
  (Q7, Q8). Every prompt's user turn is 25 ids, its whole 31, so `gen_start` is 25 on all 48.
- **R-v2, the stop.** `<|endoftext|>` is one id, recorded as the `v` block's `eos_id`: GC7's stop (the end of turn or
  the cap, no newline stop).
- **R-v3, the manifest extended in place**, as (iv)'s was. `MANIFEST_OF_RECORD`, G-VER's pin, moves from
  `fdf73d85…ef38` to `53a8cd74…99d8`; `MANIFEST_I_IV` is `render_v`'s base, kept, and `load` re-derives it from the
  new manifest byte for byte. The schema id stays "n-ids-v1".
- **R-v4, the committed-ids check.** `ids.py`'s self-test check that the committed `data/n/ids/` is the ids of record
  moves from (i)–(iv) to (i)–(v): the six files, iv's base `MANIFEST_I_III` and v's base `MANIFEST_I_IV`, the pin
  neither earlier manifest, and 48 prompts beside the 544 passages and 1,344 contexts. The BUILD review named it
  (`results/raw/2026-11-19_n-gcal-build_review.md`, its O11). It is reworded, not added: the count stays 545.
- **R-v5, the code of record.** The render ran HEAD `035947e`'s own code (`render_v` and `render-ids-v`, built at
  `89a55c3`), not a draft; only the pin's move and the check above change the package, after the render.

## The tokenizer folder

It is the folder the (i)–(iii) and (iv) renders used (`<scratch>/tok_n`; its provenance is in the (i)–(iii) render's
raw): exactly `tokenizer.json` `73fd5254…ecca`, `tokenizer_config.json` `fff5b944…3fc7` and `special_tokens_map.json`
`78afb564…e2f2`, the manifest's `olmo2_instruct` pins. The render checked them again (its output, lines 3–5). Nothing
was downloaded.

## Run 1's output, whole

Seven lines, sha256 `7b88e98663f780624af5d86cec7f0f41d5ce7ce1f697df58aba27a940114564d`; the first is the library's own
notice that the venv holds no PyTorch (tokenizers only are used); the last, the report, is sha256
`0f67b35b37b632d3e5e4854a05b4e35241b705cabf211185e374e07e4f91d82c` with its newline:

```text
PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
environment: python 3.12.9 | transformers 5.5.0 | tokenizers 0.22.2
tokenizer file special_tokens_map.json 78afb564e81264029b25f9caf24bda2521d5bdaeff5cd3fdbc01d3da2e8ce2f2 = the manifest's olmo2_instruct
tokenizer file tokenizer.json 73fd5254624f39a88e3faac6a8e11300fc3c735ed37880d4f4f08db898eaecca = the manifest's olmo2_instruct
tokenizer file tokenizer_config.json fff5b9441e8fe1d696eebed3541e719776e5b096692ef38cea68b891fc4f3fc7 = the manifest's olmo2_instruct
render-ids-v (ADDENDUM-n1 §1.2 (v)):
{"files": {"MANIFEST.json": {"records": 6, "sha256": "53a8cd74fd3427acb618ab2a3c9034f0b6ed4a2dd5e197bd5a865aa23ce699d8"}, "a3_contexts.jsonl": {"records": 1344, "sha256": "757026e8260fd2d3080e88a6f6a4ba00c85fef957ee021c66418e2f85a6bd84c"}, "gcal_prompts.jsonl": {"records": 48, "sha256": "a1197eb59a784aabcdbd2cffc21bf6d5708ec608fcf8ae1265c974ec24fae35d"}, "gvec_passages.jsonl": {"records": 544, "sha256": "444352c156aad9aa238fd5377b1192bbcbcaecbf70c9e9ee4603569eafb333a5"}, "labels.json": {"records": 4, "sha256": "43a32a1b7dec52f239020fb916e5ae9e2758be10ed232d762edcd5d048a549da"}, "n4_variants.jsonl": {"records": 320, "sha256": "e887f19ede4a1b2ca42cfeffe41f4ee81f67774b5bfcd58e0f3765739834b702"}, "sessions.jsonl": {"records": 160, "sha256": "fd8bb2341aaf7d4b1365873564d1e858a3cace4fb5cc578e4bd827c4ee14a45a"}}, "first_problems": [], "prompts": {"boundary_merged": 0, "gen_start": [25, 25], "n": 48, "ok": 48, "seq_len": [31, 31]}, "status": "PASS"}
```

## The files, as committed under `data/n/ids/`

The five (i)–(iv) files are byte-equal to HEAD's (`git rev-parse HEAD:<path>` against `git hash-object`); one file is
new and one is extended.

| file | records | sha256 | |
|---|---|---|---|
| `sessions.jsonl` | 160 | `fd8bb2341aaf7d4b1365873564d1e858a3cace4fb5cc578e4bd827c4ee14a45a` | unchanged |
| `n4_variants.jsonl` | 320 | `e887f19ede4a1b2ca42cfeffe41f4ee81f67774b5bfcd58e0f3765739834b702` | unchanged |
| `labels.json` | 4 | `43a32a1b7dec52f239020fb916e5ae9e2758be10ed232d762edcd5d048a549da` | unchanged |
| `gvec_passages.jsonl` | 544 | `444352c156aad9aa238fd5377b1192bbcbcaecbf70c9e9ee4603569eafb333a5` | unchanged |
| `a3_contexts.jsonl` | 1344 | `757026e8260fd2d3080e88a6f6a4ba00c85fef957ee021c66418e2f85a6bd84c` | unchanged |
| `gcal_prompts.jsonl` | 48 | `a1197eb59a784aabcdbd2cffc21bf6d5708ec608fcf8ae1265c974ec24fae35d` | new |
| `MANIFEST.json` | 6 files | `53a8cd74fd3427acb618ab2a3c9034f0b6ed4a2dd5e197bd5a865aa23ce699d8` | extended |

## The cross-check against the sessions of record (the BUILD review's O10)

Code's own check, after run 1 and outside the render's code: model-free and tokenizer-free, by `jq` over the render's
`gcal_prompts.jsonl` and the committed `sessions.jsonl`, comparing ids and printing only counts. Each of the 160
sessions' first 25 ids (a prompt's user turn) and first 31 (its whole, with the generation prompt) is looked up among
the 12 distinct user turns and the 12 distinct wholes of (v):

```text
jq -c -n --slurpfile v <scratch>/step4b/v/out_render/gcal_prompts.jsonl --slurpfile s data/n/ids/sessions.jsonl \
    -f <scratch>/step4b/v/o10_prefix.jq
```

The program, `o10_prefix.jq`, whole (sha256 `3a7f99b1…2a0d`):

```text
($v | map({key: (.ids[0:.user_tokens] | tostring), value: .label}) | unique_by(.key) | from_entries) as $u
| ($v | map({key: (.ids | tostring), value: .label}) | unique_by(.key) | from_entries) as $w
| {v_prompts: ($v | length), distinct_user_turns: ($u | length), distinct_wholes: ($w | length), sessions: ($s | length),
   sessions_by_user_turn_match: ([$s[] | (.ids[0:25] | tostring) as $p | ($u[$p] // "none")]
                                 | group_by(.) | map({(.[0]): length}) | add),
   sessions_whole_prefix_match: ([$s[] | (.ids[0:31] | tostring) as $p | ($w[$p] // "none")]
                                 | group_by(.) | map({(.[0]): length}) | add)}
```

Its output, one line, whole (sha256 `f59603e3…3595`):

```text
{"v_prompts":48,"distinct_user_turns":12,"distinct_wholes":12,"sessions":160,"sessions_by_user_turn_match":{"Zone B8":16,"Zone D7":11,"Zone H0":10,"Zone K7":17,"Zone L4":18,"Zone M2":16,"Zone N1":13,"Zone Q3":11,"Zone R9":10,"Zone T5":14,"Zone V3":11,"Zone W6":13},"sessions_whole_prefix_match":{"Zone B8":16,"Zone D7":11,"Zone H0":10,"Zone K7":17,"Zone L4":18,"Zone M2":16,"Zone N1":13,"Zone Q3":11,"Zone R9":10,"Zone T5":14,"Zone V3":11,"Zone W6":13}}
```

Every session of record opens with exactly one of (v)'s 12 prompts, by its user turn and by its whole: no session
is unmatched, and the per-label counts sum to 160. So (v)'s render and the sessions' render agree, id for id, on
the text the two share. The check is Code's, not the render's: `render_v` does not make it.

## G-VER on the (i)–(v) folder (the BUILD review's O11)

Run 3's second command ran G-VER's site check on the assembled folder, the render's seven files in the overlay's
`data/n/ids/`, the tokenizer loaded to decode only from `<scratch>/tok_n`. Its printed `manifest_ok` covers the
environment, the tokenizer files and the session set; the pin is not printed, and PASS requires the manifest at it
(`verify.py`'s `pin_ok`). Its output, whole:

```text
PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
G-VER trial (the BUILD's site check; never of record):
{"first_problems": [], "ids_ok": 160, "labels_kept": 4, "labels_ok": 4, "manifest_ok": true, "n4_ok": 160, "sessions": 160, "spans_ok": 160, "status": "PASS"}
```

## The package

`valence_core/n/ids.py` moves from HEAD's `cc614c75…8e76` to `fd3e9c63…7022` (+12 −9): the pin, its comment, and the
committed-ids check (R-v3, R-v4). The n package's digest moves from `e5606ddf…b36c` (`035947e`'s) to
`1bb0daea…af51`: by shell in `package_sha256_of`'s form, and as the package's own `hashes` printed it in run 3. Run 3's
`hashes`, whole:

```text
package_sha256 valence_core/n 1bb0daeab853b4a848ed0afb8feac1010013048c2dc712d29a0723210bccaf51
imported_sha256 valence_core/__init__.py 620ad380f023dc8c173ee4e164a160c0b1da2a0c0b99fb6c9717be0b8c78b604
imported_sha256 valence_core/adapters/__init__.py 96d6b48dd41710de8c70ce7d5b28854db4810af6693ff8a96f320f773cafed6a
imported_sha256 valence_core/adapters/base.py 626fbddd8dd970717e929b5bcd87be4e0c83ca8cb889b8451fcb49e2cb091cbf
imported_sha256 valence_core/adapters/olmo_hf.py df80b79b205c64121187ab0b307e5f35db5bd6632d45940a980c0175b8a092dc
imported_sha256 valence_core/discrim.py 7d171ae7b416b33a9f881a277606ace4a6891ce30c96943c3b0a41bd75d2de89
imported_sha256 valence_core/echo/__init__.py 71a6ec160a1d7beefc7f8c37c106f2fca742adc862fd9b737b7750218bf00e43
imported_sha256 valence_core/echo/probe.py d90f9281dff612977da5a3c3ce1a07155159a48103b35dfe521e0fac30152b81
imported_sha256 valence_core/extract.py 2405b1a687f9f882472b06fa3f9b8d47b20206414ada1b854b3c93a02d7a07fe
imported_sha256 valence_core/m/__init__.py b5175bcb6a521ef277de105315dd8d2f637a7b03e5d7baf30406dd83d0db35c4
imported_sha256 valence_core/m/keys.py a7d5ee3a9cde0deed785df204ae840cb56ee0e1eeefa9192fe1c1b0abb6b3beb
imported_sha256 valence_core/m/resume.py 78f2fc8eb8b3b16ffa39c6dac7022b37dc98d8d002f50390d5c4540f22bf8fb7
imported_sha256 valence_core/session_e2a.py f1e53db2e9089ed3869e75693474fa6f36eccf667d1f2a4fbe52b4ba1fe73c71
```

## Departures

- Code: none. The cross-check's `jq` reads committed ids and the render's file, and prints counts only.
- The values-checker's, as its report states them, are in the entry, for the seat to class.
