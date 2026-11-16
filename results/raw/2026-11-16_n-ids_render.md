# n — ids of record: the render of ADDENDUM-n1 §1.2 (i)–(iii) in G-DATA's environment, 160 of 160

*The n-build session (Code), PI date 2026-11-16. Under ADDENDUM-n1 v0.1 §1 (committed at `a61f13d`, sha256
`e979f8f2…5e03`) and the seat's answers of 2026-11-16 (second sitting), §1.2–§1.3 and §5 item 1
(`results/raw/2026-11-16_n-build_design-to-code_answers.md`, committed at `52b2c97`). On the laptop, model-free:
tokenizer files only, no weights. The token ids are in the committed files under `data/n/ids/`; this raw prints none.*

## The run

- **The window.** The coordinating session granted a battery window for this render on 2026-11-16: one process, two
  runs at most. One run was made.
- **The command**, from Code's scratch overlay: the repository's tracked files these steps use plus the n drafts of
  Appendix A, under the jlens venv's interpreter at `nice -n 19`:

  ```text
  HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TMPDIR=<scratch> nice -n 19 <python> scripts/n_sessions.py render-ids \
      --tokenizer-dir <scratch>/tok_n --out <scratch>/ids_out --pi-date 2026-11-16
  ```

  - The two offline variables are the coordinating session's addition, so that the Hugging Face libraries could not
    reach the network.
  - `<scratch>` stands for Code's scratch folder, and `<python>` for the jlens venv's interpreter.
- **The result.** Exit 0, PASS, in 8 seconds. The output follows whole, stdout and stderr.
- **Among what `render-ids` refuses before it renders:**
  - It refuses any environment but G-DATA's (Python 3.12.9, transformers 5.5.0, tokenizers 0.22.2). Output line 2
    prints the environment.
  - It refuses a tokenizer folder that is not exactly the three files at `data/olmo/manifest.json`'s `olmo2_instruct`
    sha256s (lines 251–262). Output lines 3–5 print those checks.
  - It also refuses a `--pi-date` not of the form YYYY-MM-DD, and an `--out` the guard refuses: the box's model
    volume, or anywhere in the repository outside `data/n/`.
- **What it asserts, and what it writes.**
  - (i) Each of the 160 sessions reproduces BK's `seq_len` and `ids_sha`, with G-DATA's two recorded re-splits
    applied.
  - (ii) Each of the 320 N4 sequences keeps BK's tokens before `n_pre`. The told zone is N4's schedule's
    (`keys.n4_schedule`), and the line is placed by the join that ADDENDUM-n1 §1.2 (ii) fixes.
  - (iii) For each label candidate convention, it tests that the prefix holds and the tail is the same in every
    context. A candidate that fails is reported and dropped; no candidate kept is a STOP. The four conventions are
    ADDENDUM-n1 §2's. The contexts are the 160 sessions and the 320 N4 sequences, each with both cues: 960 per
    candidate.
  - Code reads (iii)'s contexts beyond §1.2's words to include N4's sequences, since N4's reads use the same label ids.
  - It writes the four files only when (i) and (ii) hold for every session and at least one candidate is kept.
    Otherwise it STOPs and writes nothing.

## The tokenizer folder

- **`tokenizer.json`** came from the laptop's HF cache, copied by `cd` and a shell redirect: the hub snapshot of
  `allenai/Olmo-3-1125-32B` at `c2b61dae89a1ad10e4ad5653d0e46b590902607b`. Its sha256 is the pin in full,
  `73fd5254…ecca`.
- **`tokenizer_config.json` and `special_tokens_map.json`** came from the box's `/workspace/models/olmo2_instruct/`
  through the pod session. Each was checked against the manifest on the box, in staging and at the destination. The
  pod session's log is Appendix B, verbatim. Nothing was downloaded.
- All three equal the manifest's pins: `tokenizer.json` `73fd5254…ecca`, `tokenizer_config.json` `fff5b944…3fc7` and
  `special_tokens_map.json` `78afb564…e2f2`. The render checked them again.

## The output, whole

```text
PyTorch was not found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
environment: python 3.12.9 | transformers 5.5.0 | tokenizers 0.22.2
tokenizer file special_tokens_map.json 78afb564e81264029b25f9caf24bda2521d5bdaeff5cd3fdbc01d3da2e8ce2f2 = the manifest's olmo2_instruct
tokenizer file tokenizer.json 73fd5254624f39a88e3faac6a8e11300fc3c735ed37880d4f4f08db898eaecca = the manifest's olmo2_instruct
tokenizer file tokenizer_config.json fff5b9441e8fe1d696eebed3541e719776e5b096692ef38cea68b891fc4f3fc7 = the manifest's olmo2_instruct
render-ids (ADDENDUM-n1 §1.2 (i)-(iii)):
{"candidates": {"bare": {"contexts": 960, "kept": true, "prefix_kept": 960, "tail_equal": 960}, "bare+eot": {"contexts": 960, "kept": true, "prefix_kept": 960, "tail_equal": 960}, "space": {"contexts": 960, "kept": true, "prefix_kept": 960, "tail_equal": 960}, "space+eot": {"contexts": 960, "kept": true, "prefix_kept": 960, "tail_equal": 960}}, "files": {"MANIFEST.json": {"records": 3, "sha256": "7f51bd914eb03510442f01bfbf7cad7ba74c7e9fb98edb307db350d9772a821d"}, "labels.json": {"records": 4, "sha256": "43a32a1b7dec52f239020fb916e5ae9e2758be10ed232d762edcd5d048a549da"}, "n4_variants.jsonl": {"records": 320, "sha256": "e887f19ede4a1b2ca42cfeffe41f4ee81f67774b5bfcd58e0f3765739834b702"}, "sessions.jsonl": {"records": 160, "sha256": "fd8bb2341aaf7d4b1365873564d1e858a3cace4fb5cc578e4bd827c4ee14a45a"}}, "first_problems": [], "n4": {"n": 320, "ok": 320}, "sessions": {"n": 160, "ok": 160}, "status": "PASS"}
```

## The files, as committed under `data/n/ids/`

| file | records | sha256 |
|---|---|---|
| `sessions.jsonl` | 160 | `fd8bb2341aaf7d4b1365873564d1e858a3cace4fb5cc578e4bd827c4ee14a45a` |
| `n4_variants.jsonl` | 320 (160 told, 160 sham) | `e887f19ede4a1b2ca42cfeffe41f4ee81f67774b5bfcd58e0f3765739834b702` |
| `labels.json` | 4 candidates, all kept | `43a32a1b7dec52f239020fb916e5ae9e2758be10ed232d762edcd5d048a549da` |
| `MANIFEST.json` | 3 files | `7f51bd914eb03510442f01bfbf7cad7ba74c7e9fb98edb307db350d9772a821d` |

Code checked the files after the run, by `shasum` and by `jq`, printing no id:
- **The hashes.** Each file's sha256 equals the report's, and the manifest's own entries.
- **The manifest** names the environment above, the three pins, the session set of record (`be50011a…ba84`), N4's
  schedule by sha256, and the PI date.
- **Sessions:** 160 records, 160 distinct sessions. Every id list's length equals its `seq_len`, and both assertions
  are true. 144 sessions are 1,273 tokens long and the other 16 are 1,266–1,272, as BK's records have them.
- **N4:** 320 records, 160 N4-T and 160 N4-Ts, the prefix asserted on all. They hold 13 distinct lines: twelve told
  lines and the sham's.
- **Labels:** each candidate holds 12 labels. The tails are 3 tokens for the bare and spaced labels, and 4 with the
  end-of-turn token.

The convention of record among the four is decided on the box by ADDENDUM-n1 §2's comparison, in the BACKEND
extension's session, after G-VER has asserted (i).

## Appendix A — the drafts at the render

The n package's sha256, and each draft file's, as `render-ids` ran them. The import closure's 11 files equal `HEAD`'s
committed files, checked by `git hash-object` against `git rev-parse HEAD:<path>`. Of the files listed,
`__init__.py` equals `HEAD`'s; the rest are drafts. The BUILD commits the drafts, and its entry states any difference
from these.

```text
package_sha256 valence_core/n 45c70818fc9c63c209d4d42ea8c96a1b520e5c94ec366b68aff44aae9eb76a98
draft_sha256 valence_core/n/__init__.py 427f58ccf531d2d98bd76004e2ff8b2ece9514248328e12844156a659e711cfd
draft_sha256 valence_core/n/cells.py 03c13928ed2210ad216532f78e04e8b9db6d1374db211706bde496d2c9885252
draft_sha256 valence_core/n/directions.py f0608a2613d683f7600808b2bdd9f61b6c3c7ba904ee39644be6eefef1deab12
draft_sha256 valence_core/n/guard.py 014c518f1baecb980b1ba1cd1040771455f94d0c008cf01a5d4495ffc7e4aaa7
draft_sha256 valence_core/n/hftiny.py c61ea7513051584aefdd9bcc9da15f3d07437236d88f6bc29db11c92556e82be
draft_sha256 valence_core/n/ids.py bea4b333de1a6662d7238c27be5848b56867cf9007f99b7c974422751fb507fa
draft_sha256 valence_core/n/keys.py 5c6f382616ac7abb593af4c29b499e5a504e257580dba32dd587f1ee1a7a9fb3
draft_sha256 valence_core/n/primitive.py bae61d60d6c4a84ac9b0ac847f35be9d04a769b996c68e99674ad7212fdc4069
draft_sha256 valence_core/n/probe.py cfd269dd58076a249d9cb30622f28340d13627744391621e5a78d3fbedbf3772
draft_sha256 valence_core/n/runner.py 6e1760d5ec50cbde5a2f5b015df3d7f22ad2b424823220343fa5c3ee8af43457
draft_sha256 valence_core/n/schema.py 33419938a2b8a905588f96e1c53dd771c3f324a13f94d309eb53a906f42d111d
draft_sha256 valence_core/n/sessions.py e974d4bdd4e9b498d73d7c500ae83c650ad766a112bf384f79a3ce9dc6acf13f
draft_sha256 valence_core/n/testing.py 3fd9aed3d66c9f31d4470fbda9116226b9cfaed7151ecb5a25daaa31a4c4dbdd
draft_sha256 valence_core/n/verify.py 627ae4b6ac33d20ce26a8a8466c2b13fead58e262cad6e809ecc66206981c2a3
draft_sha256 scripts/n_sessions.py 5082ac24b6e158d05386f29ea612f17a3e9a031c79589e0906f1ba3599796481
```

## Appendix B — the pod session's copy log (sha256 `eb3bef45…1f92`), verbatim

```text
box:         tokenizer_config.json  sha256 fff5b9441e8fe1d696eebed3541e719776e5b096692ef38cea68b891fc4f3fc7  bytes 4869
box:         special_tokens_map.json  sha256 78afb564e81264029b25f9caf24bda2521d5bdaeff5cd3fdbc01d3da2e8ce2f2  bytes 581
box: both files equal the manifest's olmo2_instruct pins (sha256 and bytes)
staging: both files equal the manifest's pins
destination: tokenizer_config.json  sha256 fff5b9441e8fe1d696eebed3541e719776e5b096692ef38cea68b891fc4f3fc7  bytes 4869
destination: special_tokens_map.json  sha256 78afb564e81264029b25f9caf24bda2521d5bdaeff5cd3fdbc01d3da2e8ce2f2  bytes 581
COPY-TOK OK: 2 files, the box's = the manifest's (data/olmo/manifest.json at HEAD a61f13d, olmo2_instruct) = staged = destination
  tokenizer_config.json  sha256 fff5b9441e8fe1d696eebed3541e719776e5b096692ef38cea68b891fc4f3fc7  bytes 4869
  special_tokens_map.json  sha256 78afb564e81264029b25f9caf24bda2521d5bdaeff5cd3fdbc01d3da2e8ce2f2  bytes 581
Nothing downloaded; nothing written on the box.
exit=0
```
