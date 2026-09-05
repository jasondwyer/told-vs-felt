"""Round-task spans of an archived e2a session, in the tokenization of the
text the echo read is taken over. Model-free (tokenizer only).

WHAT E2A STEERED. `jlens_qwen.e2a.generate_round_positional` (the runner of
record, gitignored clone) computes, per round,

    prefix_ids = encode(prefix_text); seg_ids = encode(prefix_text + segment)
    boundary   = length of the common prefix of the two id lists
    round_ids  = seg_ids[boundary:]

and the state is live from `boundary` onward through every generated token
of that round; the harness-written newline that closes the round is never
forwarded under the state. So the steered span of round r is
[boundary_r, end of round r's generated text) -- the segment (header + task
line + "Response:") and the response.

THIS MODULE DOES NOT RE-DERIVE THAT RULE. It applies it: `boundary_r` is
computed with the same two encodes over the same two texts, and the span's
end is the token count of the text up to the response's last character.
Both are asserted PREFIX-STABLE against the tokenization of the full read
text (the ids of the shorter text are a prefix of the ids of the longer),
which is what makes per-round token indices valid indices into the full
text's tokens. A session that fails either assertion is reported, not
repaired. (Survey 2026-09-05, 102 valid reward sessions, 408 forced rounds:
0 failures, 0 straddling tokens at either edge.)

Character offsets come from `session_e2a.scaffold_pieces` -- the same walk
`verify_archived_session` uses to reconstruct every archived transcript
byte for byte.
"""

from __future__ import annotations

from typing import Mapping, Sequence

from ..adapters.base import ModelAdapter
from ..session_e2a import scaffold_pieces

#: `regression.oracle.CHOICE_MARKER` -- the text e2a's choice read ended at.
CHOICE_MARKER = "Config choice (one word):"


def choice_prefix(transcript: str, k: int = 0) -> str:
    """The transcript prefix ending at the (k+1)-th choice marker: the exact
    text e2a's k-th free-choice read was taken over."""
    start, idx = 0, []
    while (j := transcript.find(CHOICE_MARKER, start)) != -1:
        idx.append(j + len(CHOICE_MARKER))
        start = j + 1
    if k >= len(idx):
        raise IndexError(f"transcript has {len(idx)} choice markers, "
                         f"asked for index {k}")
    return transcript[:idx[k]]


def round_char_spans(row: Mapping, tasks: Sequence[Mapping]) -> list[dict]:
    """Every round's (segment_start, generation_end) in transcript
    characters, with phase, pole and tag, by walking the archive's own
    scaffolding pieces."""
    sc = scaffold_pieces(row, tasks)
    t = row["transcript"]
    pos = 0
    out: list[dict] = []
    fi = ci = 0
    pending = None
    for kind, text in sc["pieces"]:
        if kind == "generation":
            nl = t.find("\n", pos)
            if nl < 0:
                raise AssertionError("generation never terminates")
            pending["gen_end"] = nl          # newline excluded: harness-written
            pending["segment_text"] = t[pending["seg_start"]:pos]
            out.append(pending)
            pending = None
            pos = nl + 1
            continue
        if t[pos:pos + len(text)] != text:
            raise AssertionError(
                f"{kind} mismatch at offset {pos}: expected {text[:60]!r}, "
                f"found {t[pos:pos + 60]!r}")
        if kind == "round":
            if fi < len(row["rounds"]):
                r = row["rounds"][fi]
                pending = {"phase": f"forced{fi}", "round": fi,
                           "pole": r["pole"], "tag": r["tag"],
                           "seg_start": pos}
                fi += 1
            else:
                c = row["choices"][ci]
                pending = {"phase": f"free{ci}", "round": len(row["rounds"]) + ci,
                           "pole": c["picked_pole"], "tag": c["pick"],
                           "seg_start": pos}
                ci += 1
        pos += len(text)
    if pos != len(t):
        raise AssertionError(f"walk consumed {pos} of {len(t)} bytes")
    return out


def token_spans(adapter: ModelAdapter, read_text: str,
                char_spans: Sequence[Mapping]) -> list[dict]:
    """Map the rounds that lie entirely inside `read_text` to half-open token
    spans in ITS tokenization, by e2a's own boundary rule, asserting
    prefix-stability at both edges."""
    ids_full = adapter.encode(read_text)
    n = len(ids_full)
    out = []
    for cs in char_spans:
        if cs["gen_end"] > len(read_text):
            continue                      # round lies after the read
        pre = read_text[:cs["seg_start"]]
        seg = cs["segment_text"]
        a = adapter.encode(pre)
        b = adapter.encode(pre + seg)
        boundary = 0
        while (boundary < len(a) and boundary < len(b)
               and a[boundary] == b[boundary]):
            boundary += 1
        if ids_full[:len(a)] != a:
            raise AssertionError(
                f"{cs['phase']}: prefix tokens are not a prefix of the full "
                f"text's tokens at the segment start (char {cs['seg_start']})")
        if boundary != len(a):
            raise AssertionError(
                f"{cs['phase']}: e2a boundary {boundary} != prefix length "
                f"{len(a)} -- a token straddles the segment start")
        e = adapter.encode(read_text[:cs["gen_end"]])
        if ids_full[:len(e)] != e:
            raise AssertionError(
                f"{cs['phase']}: tokens are not prefix-stable at the "
                f"generation end (char {cs['gen_end']})")
        end = len(e)
        if not (boundary < end <= n - 1):
            raise AssertionError(
                f"{cs['phase']}: token span [{boundary}, {end}) invalid for "
                f"n = {n}")
        out.append({**{k: v for k, v in cs.items() if k != "segment_text"},
                    "tok_start": boundary, "tok_end": end,
                    "n_tokens": end - boundary})
    return out


__all__ = ["CHOICE_MARKER", "choice_prefix", "round_char_spans", "token_spans"]
