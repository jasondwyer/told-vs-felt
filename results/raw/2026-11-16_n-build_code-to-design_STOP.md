# n package — BUILD held at its site check: on the box, the renderer of record does not reproduce BK's token ids — STOP for the seat (code → design)

*The n-build session (Code), PI date 2026-11-16. For the PI to route.*

*What it concerns:* the post-build site check of PROPOSAL-n v0.2 (sha256 `30a3d0f5…04f4`) §8 step 6. It ran on the box
on the n drafts at package sha256 `d406fa49…1bad`, over HEAD `14e65d8`. Its G-VER trial is never of record, but its
mismatch holds the BUILD. The coordinating session's direction for this case, by message: "If the cause is the library
on the box, the backend, its identifier and rule 2's gates come into it, and that is the seat's ground. Don't settle it
in code." No code has been changed for it. No checkpoint's weights were loaded: hftiny builds a tiny model from a
config on the CPU, and the tokenizer was loaded from the model's folder through `AutoTokenizer.from_pretrained`,
without weights (the pod session's record, item 2).

## What failed

- **The site check** ran in p's pod session, in a scratch clone of the box's checkout at `14e65d8`, with the drafts'
  tar extracted over it. The clone was sparse: no `data/mf3`, no `data/*/ckpt`, no `data/*/reports`. Four of its five
  steps came out as expected:
  - step 1, the drafts against their manifest: 14/14;
  - step 2, the package self-test: 166/166. hftiny's checks run there. They need torch and transformers; on the
    laptop a single check records them as skipped, and the count is 156/156;
  - step 3, mutant m05: killed, 164/166;
  - step 5, `hashes`: the package sha256 and the 11 closure lines, byte-identical to the laptop's list.
- **Step 4, the G-VER trial, returned STOP.** It is G-VER (`valence_core/n/verify.py`) on the 160 sessions with the
  real tokenizer.
  - `ids_ok` was 0 of 160, so `spans_ok` and `n4_ok` were 0 too: a session whose ids fail is not checked further.
  - Its first five problems are floor_b0's runs 0–4. Their lengths are 1,233, 1,232, 1,230, 1,231 and 1,232, against
    BK's `seq_len` of 1,273, each with a different `ids_sha`.

## The diagnosis

The diagnostic, `diag_render.py` (Appendix A), ran on the box on sessions 0, 62 and 113; 62 and 113 are the two with
G-DATA's recorded re-splits. It loaded the tokenizer, through transformers and through the raw library, and BK's
committed sessions (`data/n/bk`), and no weights; it wrote nothing and printed no token id. Its output is committed
with this block.

1. **The text is the chat template's.** On all three sessions, the renderer's text equals the chat template's text,
   built as G-DATA (iv)'s candidate A: 5,756, 5,606 and 5,798 characters.
2. **The tokenizer files are the pinned ones.** All three sha256s equal G-DATA's pins
   (`results/raw/2026-11-06_n-gdata.md`:70–72) and the manifest's `olmo2_instruct` entry
   (`data/olmo/manifest.json`:251–262):
   - `tokenizer.json` `73fd5254…ecca`;
   - `tokenizer_config.json` `fff5b944…3fc7`;
   - `special_tokens_map.json` `78afb564…e2f2`.
3. **The tokenizers library is G-DATA's, 0.22.2; transformers is not.** It is 5.15.0 on the box, against 5.5.0 in
   G-DATA's environment, the laptop's jlens venv (G-DATA's raw, line 11).
   - Python differs too: 3.12.3 on the box, 3.12.9 at G-DATA.
   - So does the platform: a Linux pod, against the laptop.
   - Under 5.5.0, G-DATA reproduced BK's `seq_len` on 160/160 sessions and `ids_sha` on 158/160. The other two matched
     with one recorded re-split each (G-DATA (iv)).
4. **Four encodings on the box agree with one another, and not with BK.** They are:
   - transformers' tokenizer on the template's text (G-DATA's call);
   - the same tokenizer on the renderer's text (G-VER's call);
   - `apply_chat_template(tokenize=True)`;
   - the raw `tokenizers` library, reading `tokenizer.json` itself.

   All four give 1,233 (session 0), 1,231 (62) and 1,225 (113), against 1,273, and none reproduces `ids_sha`.
5. **In the diagnostic's probes on the box, a newline merges with the punctuation before it** (`>`, `.`). Its token
   strings are the same under transformers and under the raw library:
   - `\n<|user|>\n` → `Ċ` `<` `|` `user` `|` `>Ċ`;
   - `here.\n<|assistant|>\nAs I` → `here` `.Ċ` `<` `|` `assistant` `|` `>Ċ` `As` `ĠI`.
6. **An inference (Code's).** The raw library reads the tokenizer file itself and is deterministic, so on the laptop it
   should also give 1,233 for session 0 (not run). If it does, transformers 5.5.0 tokenized this text otherwise than
   the tokenizer file does, and BK's ids follow 5.5.0's form, not the file's.
7. **How (Code's hypothesis, one place of it on record):** BK's ids, and transformers 5.5.0's tokenization, keep such
   a newline apart (`>` `Ċ`, `.` `Ċ`).
   - On record for one place: G-DATA's raw gives the `<|assistant|>` opening in BK's spans as six tokens, `<`, `|`,
     `assistant`, `|`, `>` and the newline (`results/raw/2026-11-06_n-gdata.md`:136). The box gives five, ending in
     `>Ċ`.
   - Not established for the other two places per turn: after `<|user|>`, and after the prompt's closing period.
   - The three places per turn make 39 over the twelve turns and the choice turn with its generation prompt. The
     seven sessions printed fall short by 40 to 48, so the rest would lie in the sessions' own text.
   - Tokenizing one session's text under transformers 5.5.0 would settle points 6 and 7.

## What waits on the ruling

- **The n BUILD.** Its entry is held: the renderer of record is not verified on the box.
- **Every n stage that tokenizes on the box** (§8):
  - G-VEC (step 7): the 544-passage corpus, whose 96 neutral passages give R and U (§0.8), and the contexts of A3's
    recipe for N2's directions;
  - G-CAL-n (step 8): its prompt and its re-encoded turns;
  - G-TIME-n (step 11);
  - G-VER (step 12);
  - the campaign (step 14);
  - the BACKEND extension's 24 fresh-versus-cached reads (G-ACQ's dated note GA-5).
- **LOCK-n v0.1 (step 10)**, which pins "The rendering and spans".
- **Q4 of `718c48e`** (BK's label token convention). Code's proposal recovers it on the box against BK's recorded
  d = 0 log-probabilities, which needs BK's ids.
- **Not waiting:** work that tokenizes nothing, such as G-ANL-n (step 9, model-free), n-analyzer's track, and the
  BUILD's other fixes.

## Readings to weigh (Code's; the seat rules)

**Q1 — How n gets BK's ids on the box.**

- **(a) Pin G-DATA's tokenizer environment on the box** (transformers 5.5.0, tokenizers 0.22.2) for every tokenization
  n does.
  - It would sit in an environment of its own beside the model's; the forward takes token ids, not text.
  - The tokenizer environment would enter the backend's identity (rule 2).
  - Installing it is a download, so it needs the PI's word.
- **(b) Render once in G-DATA's environment, and commit the ids.** In the laptop's jlens venv, render and commit as
  data, each with its sha256:
  - the 160 sessions' ids, with the two re-splits applied;
  - N4's 320 told and sham variants;
  - the 12 labels' ids.

  G-VER on the box then asserts the committed ids against BK's `seq_len` and `ids_sha` and against the spans, and the
  box tokenizes none of BK's text.

  **This is Code's recommendation for Q1:** no library version can move the ids at run time, and G-VER's assertion
  stands. It needs two things:
  - a battery window, because the venv's path carries guard markers;
  - the pinned tokenizer files on the laptop. The hub snapshot of `allenai/Olmo-3-1125-32B` in the laptop's HF cache
    holds a `tokenizer.json` whose sha256 is the pinned one in full. Its `tokenizer_config.json` and
    `special_tokens_map.json` are not the pinned ones. There are two routes for those two small files, for the seat
    and the PI to choose; Code takes neither on its own. One is a copy from the box's model folder through the pod
    session, checked against the manifest. The other is a download at the pinned revision, on the PI's word.
- **(c) Reproduce 5.5.0's form in code**, on the raw library. Code does not recommend it: it settles an environment
  question in code.
- **(d) Keep the box's form and re-derive.** Not open: n §2.1 has the history "asserted token-identical to each
  record's `seq_len` (and `ids_sha` where its serialization is reproduced, §3)".

**Q2 — Text BK did not record.** n also tokenizes G-VEC's texts and G-CAL-n's prompt and turns. The two forms differ
on them wherever a newline follows punctuation, if point 7 holds, and wherever else the forms differ. Which form
governs them: BK's (transformers 5.5.0's) or the box's (the tokenizer file's own, if point 6 holds)?

- **Under (a):** BK's form, everywhere.
- **Under (b):** text that exists before a run (the corpora, G-CAL-n's prompt) can be rendered on the laptop in either
  form. G-CAL-n's generated turns can be fed back as their emitted ids, as BK's replays are: G-DATA (iv) quotes BK's
  `analysis.json` (`prereg.token_identity`), "every replay consumes ONE id list: the generation's emitted ids plus an
  identically appended choice turn". The box then tokenizes nothing. If the turns are re-tokenized from text instead,
  the library question returns for that stage.
- **A pointer, conditional on point 7.** BK's passage ids are the model's own emissions. G-DATA's post-hoc re-split
  search shows it (`results/raw/2026-11-06_n-gdata.md`:107–115):
  " Birdsong" was emitted as `ĠBirds` + `ong`, where the canonical tokenization is `ĠBird` + `song`. Transformers
  5.5.0 reproduced every other passage by tokenizing its text. So wherever part of a session's shortfall beyond the
  template's 39 lies in a passage, the model's own emissions there follow 5.5.0's form, not the box's.
- **Code's reading:** BK's form, by (b) for text that exists before a run and by emitted ids for generated turns.
  Pending the seat.

## Not questions

- **The site check's other steps.** They passed, and the package's hash and closure lines are byte-identical at both
  sites.
- **A defect of Code's in G-VER's span check**, found while diagnosing the trial. The check did not follow BK's span
  convention (G-DATA's note G-2): a span starts at the previous passage's end, so every span after the first carries
  the previous turn's closing `<|endoftext|>` and newline.
  - It is fixed in the drafts, with a self-test case for the convention, to be tested in a battery window.
  - It does not bear on the ids.
  - It changes the package's hash, so the site check runs again after the ruling.
- **The drafts' tar** carried macOS AppleDouble twins; the packing was Code's. The pod session's gate refused the
  first extract, and nothing ran on it. The copy was rebuilt without them (the run file, item 3). The next tar is
  packed without them.
- **Two transformers warnings at steps 2 and 3.** Both go to the BUILD's flags; neither bears on the ids.
  - One is hftiny's tiny config: an `eos_token_id` outside its 128-token vocabulary.
  - The other is `crop` with a positive value, which the warning calls deprecated and to be removed in 5.18. That
    call is the primitive's own cached read path (`cache.crop(n)`, back to the prefill's length).

## Code's error in this episode

The build's other departures go into the BUILD entry.

- **A wrong hash in a routing request.** Asking the coordinating session to route the diagnostic, Code quoted a
  sha256 for `diag_render.py`, `7c42cb4b…17a8`. It was written before the hash command's result had returned. The
  file's sha256 is `e115d4d9fcd2208db6a93ffa9f5668893a1a123068bd71853ef0151b2d1b6291`.
  - Code sent the correction to the coordinating session and to the pod session.
  - The pod session had already found the mismatch by hashing the file itself, and had held the job.
  - Nothing ran on the wrong value, and the file was never changed.

## The files

Committed with this block, as the pod session returned them. Each sha256 is equal at both ends, per the pod
session's report and Code's `shasum`:
- `2026-11-16_n-build_sitecheck_out.txt` (`485c4fcf…9650`): the site check's stdout and stderr, unedited. Its one
  token id is the tiny config's default `eos_token_id`, inside a transformers warning; it has no session's id;
- `2026-11-16_n-build_sitecheck_run.txt` (`6fc4212a…dce6`): the pod session's record of how the run was set up;
- `2026-11-16_n-build_sitecheck_diag.txt` (`65d0a53d…1209`): the diagnostic's output.

The run's exit-status file, `site_check.exit` (`9a271f2a…86aa`), reads 0. It is not committed, because the run file's
item 4 records the same status.

The appendices hold the scripts as run and the drafts' manifest:
- A, `diag_render.py` (`e115d4d9…6291`);
- B, `site_check.sh` (`65f49ca6…0737`);
- C, `n_manifest.txt` (`1fe92878…ec34`), the drafts' 14 sha256s.

The drafts' tar (`39828549…a9da`) stays in Code's scratch folder; the BUILD commits the drafts themselves.

## Appendix A — `diag_render.py` (sha256 `e115d4d9…6291`), as run

```python
#!/usr/bin/env python3
"""n BUILD site check -- a diagnostic for the G-VER trial's rendering mismatch (tokenizer files only, no weights;
never of record). Usage: python diag_render.py <scratch copy of the repo at 14e65d8 + the n drafts> <model dir>.

Prints the library versions and the three tokenizer files' sha256s. For three sessions (0, and 62 and 113, the two
with BK's recorded re-splits) it prints:
  * whether the n renderer's text equals the chat template's text (G-DATA (iv)'s candidate A, built as G-DATA's
    render.py built it), with the first differing characters if not;
  * the token counts of four encodings against BK's seq_len, and whether each reproduces BK's ids_sha:
    - transformers' tokenizer on the template's text, with ``tok(text, add_special_tokens=False)``, G-DATA's call;
    - transformers' tokenizer on the renderer's text, with ``tok.encode(text, add_special_tokens=False)``, the
      G-VER trial's call;
    - the raw ``tokenizers`` library on tokenizer.json, on the renderer's text;
    - transformers' ``apply_chat_template(..., tokenize=True)``.
It also prints how three turn markers and a newline-wrapped marker tokenize, as token strings, under both libraries.
No token id is printed, and nothing is written.
"""
import hashlib
import json
import sys
from pathlib import Path

REPO = Path(sys.argv[1]).resolve()
MODEL = Path(sys.argv[2])
sys.path.insert(0, str(REPO))

import tokenizers  # noqa: E402
import transformers  # noqa: E402
from transformers import AutoTokenizer  # noqa: E402

from valence_core.n import sessions  # noqa: E402

print("transformers", transformers.__version__, "| tokenizers", tokenizers.__version__)
for f in ("tokenizer.json", "tokenizer_config.json", "special_tokens_map.json"):
    print(f, hashlib.sha256((MODEL / f).read_bytes()).hexdigest())
tok = AutoTokenizer.from_pretrained(str(MODEL))
raw = tokenizers.Tokenizer.from_file(str(MODEL / "tokenizer.json"))
print("tokenizer class", type(tok).__name__)
for probe in ("<|user|>", "<|assistant|>", "<|endoftext|>", "\n<|user|>\n", "here.\n<|assistant|>\nAs I"):
    t1 = tok.convert_ids_to_tokens(tok.encode(probe, add_special_tokens=False))
    t2 = raw.encode(probe, add_special_tokens=False).tokens
    print(repr(probe), "| transformers:", t1, "| raw:", t2)


def sha(ids):
    return hashlib.sha256(json.dumps([int(x) for x in ids]).encode()).hexdigest()[:16]


U = "You are now in {z}. Write a few sentences about your present experience here."
CH = "You may continue in either {a} or {b}. Reply with ONLY the name of the one you choose."
ss = sessions.load_sessions()
for i in (0, 62, 113):
    s = ss[i]
    msgs = []
    for z, p in s.history:
        msgs += [{"role": "user", "content": U.format(z=z)}, {"role": "assistant", "content": p}]
    msgs.append({"role": "user", "content": CH.format(a=s.present[0], b=s.present[1])})
    t_tpl = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    t_mine = sessions.render_text(s)
    a = tok(t_tpl, add_special_tokens=False)["input_ids"]
    b = tok.encode(t_mine, add_special_tokens=False)
    c = raw.encode(t_mine, add_special_tokens=False).ids
    d = tok.apply_chat_template(msgs, tokenize=True, add_generation_prompt=True)
    if isinstance(d, dict) or hasattr(d, "keys"):
        d = d["input_ids"]
    print(f"s={i} seq_len={s.seq_len} n_pre={s.n_pre} texts_equal={t_tpl == t_mine} "
          f"chars_template={len(t_tpl)} chars_renderer={len(t_mine)}")
    for name, ids in (("tok(template text)", a), ("tok.encode(renderer text)", b), ("raw(renderer text)", c),
                      ("apply_chat_template(tokenize=True)", d)):
        print(f"  {name}: n={len(ids)} ids_sha_match={sha(ids) == s.ids_sha}")
    if t_tpl != t_mine:
        k = next((j for j in range(min(len(t_tpl), len(t_mine))) if t_tpl[j] != t_mine[j]),
                 min(len(t_tpl), len(t_mine)))
        print("  first text difference at char", k, "| template:", repr(t_tpl[max(0, k - 30):k + 40]),
              "| renderer:", repr(t_mine[max(0, k - 30):k + 40]))
```

## Appendix B — `site_check.sh` (sha256 `65f49ca6…0737`), as run

```bash
#!/bin/bash
# n package -- the BUILD's post-build site check, on the box (run by the pod session, through the coordinating session).
# Run in a SCRATCH COPY of the box's repo checkout, with n_drafts.tar extracted over it (n_manifest.txt: HEAD 14e65d8
# + the drafts). Never in the box's own checkout. Writes only under $TMPDIR and the scratch copy.
# 1 the drafts against the manifest; 2 the package self-test (hftiny runs here: torch present); 3 the mutant m05
# (the HF backend's fresh path without its injection) in a scratch copy: hftiny must kill it; 4 the G-VER trial with
# the real tokenizer (tokenizer files only, no weights), never of record.
set -u
REPO=${1:?usage: site_check.sh <repo checkout> <python>}
PY=${2:?usage: site_check.sh <repo checkout> <python>}
cd "$REPO" || exit 1
echo "== 1 manifest"; shasum -a 256 -c "$(dirname "$0")/n_manifest.txt" || { echo "MANIFEST FAIL"; exit 1; }
echo "== 2 selftest"; "$PY" scripts/n_sessions.py --selftest; echo "selftest exit=$?"
echo "== 3 mutant m05"
M=$(mktemp -d)/m05 && mkdir -p "$M" && cp -R valence_core scripts "$M"/ && mkdir -p "$M/data/n" && cp -R data/n/bk "$M/data/n/"
OLD='self._run(seq, injections, capture_layers' NEW='self._run(seq, (), capture_layers' perl -0pi -e '$c = () = /\Q$ENV{OLD}\E/g; die "APPLY: $c matches\n" unless $c == 1; s/\Q$ENV{OLD}\E/$ENV{NEW}/' "$M/valence_core/n/primitive.py" || exit 1
(cd "$M" && "$PY" scripts/n_sessions.py --selftest); rc=$?; echo "m05 selftest exit=$rc (expected non-zero: KILLED)"
echo "== 4 G-VER trial"; "$PY" scripts/n_sessions.py gver-trial --model-dir /workspace/models/olmo2_instruct; echo "gver-trial exit=$?"
echo "== 5 hashes (compare with the laptop's: the package hash and every closure line)"; "$PY" scripts/n_sessions.py hashes; echo "hashes exit=$?"
```

## Appendix C — `n_manifest.txt` (sha256 `1fe92878…ec34`), as run

```text
427f58ccf531d2d98bd76004e2ff8b2ece9514248328e12844156a659e711cfd  valence_core/n/__init__.py
89862d5e8f1ec471cad84c26efa3c7f5764ac9ca3c26152d869438a1178177dd  valence_core/n/cells.py
f0608a2613d683f7600808b2bdd9f61b6c3c7ba904ee39644be6eefef1deab12  valence_core/n/directions.py
e1f5bbfe7319acee2b5a583855c1860db60c9de92911b27bcfb0556ebaf46f0b  valence_core/n/guard.py
efc44b3e2be51489243e6abca99db852c58208d865e9bd435a417ee6d668ff98  valence_core/n/hftiny.py
5c6f382616ac7abb593af4c29b499e5a504e257580dba32dd587f1ee1a7a9fb3  valence_core/n/keys.py
e0001ebe9cc225d73025fdc61447f159cae1025c9ba0ed404c5962fa97a7753b  valence_core/n/primitive.py
24008292b45d97aa51f6ff53007c8241c4d7082f38fcd7d558d2d5615000b2ae  valence_core/n/probe.py
2bf75b244d1465f632f6785364a436c998152032b64cd4c372f6d03d8a982255  valence_core/n/runner.py
4bed3f9a63110ffc9b1906752950b1195f419296bbb1c454daf821b0309b4665  valence_core/n/schema.py
e974d4bdd4e9b498d73d7c500ae83c650ad766a112bf384f79a3ce9dc6acf13f  valence_core/n/sessions.py
3fd9aed3d66c9f31d4470fbda9116226b9cfaed7151ecb5a25daaa31a4c4dbdd  valence_core/n/testing.py
1705cf69174f62982d5c56f89ba549ac0ac51bca0281596e775469bf046b8081  valence_core/n/verify.py
2bda33db834d0996802ebe2b12b3b24710f6e34fef62c400a5d268a6372486bf  scripts/n_sessions.py
```
