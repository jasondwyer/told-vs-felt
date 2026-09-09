"""PROPOSAL-k §1.2 -- Stage 1 MASKED READS over the k1 sham sessions.

Lives INSIDE the quarantine namespace so `maskedprefix`'s import guard
sanctions it without being widened (the guard admits importers under
`valence_core/echo/`). Nothing here generates text; every read is the
recon's apparatus applied to new sessions in the format of record:

  text held constant, injection varied, at L48, f = 0.10, the frozen reward
  axis `d` (sha16 3c17b0d8fbcad716, float64-normalised) and the frozen
  norm-matched random direction `r` = e0_random_dirs.npz['L48'] (sha16
  7be5db23d9224375; e2a's random1 and e2d's R arm), read at the FIRST free
  choice:

    M+A  +d on label A's block spans; nothing on B's.   M+B  the mirror.
    R+A  +r on A's block;                               R+B  the mirror.
    M++  +d on both blocks (leak calibration; no preference possible).
    R++  +r on both blocks.
    M0   mask off -- the paired shadow of every read above, asserted
         identical across masks and against the session's own vanilla read.

  A and B are the two menu labels at that choice (A = first-listed). Block
  spans are the two forced rounds under a label, by e2a's boundary rule
  (`spans.token_spans`). Every sign is +1: no negative pole is constructed
  anywhere (PROPOSAL-k §0.4). Per (session, mask): the restricted two-label
  read at the read position and the residual stream at (i) the read
  position, (ii) the last occurrence of label A's first token before the
  read, (iii) the same for label B -- all in the menu line -- for the six
  workspace layers and L49-L63. Fingerprints as-stored. Span provenance per
  read; the mask asserted zero at the read and outside declared spans (the
  primitive's own assertions); identity: the shadow's restricted read against
  the session's recorded vanilla first read (restricted; p_a within 1e-9,
  pick equal) and `choice_read(verify=True)` at KL exactly 0.

PROHIBITION (PROPOSAL-k §1.4 G4): no signed quantity toward the +label is
computed, printed or logged on M+A / M+B anywhere in Stage 1. This module
computes no signed quantity at all; the analyzer computes the leak
quantities on R and M++ rows only and asserts the prohibition.
"""

from __future__ import annotations

import json
import os
import time
from typing import Mapping, Sequence

import numpy as np

from .maskedprefix import assert_statepresent_absent, read_choice_maskedprefix
from .spans import choice_prefix, round_char_spans, token_spans
from ..adapters.base import Injection, assert_equal_norm, sha16_arr
from ..e2d.config import DATA, REPO
from ..formats.recon import as_e2a_row
from ..regression.oracle import load_axis

LAYER = 48
FRAC = 0.10
AXIS_SHA_F64 = "3c17b0d8fbcad716"
RAND_KEY = "L48"
RAND_SHA = "7be5db23d9224375"
MASKS = ("M+A", "M+B", "R+A", "R+B", "M++", "R++")   # M0 = the shadow, once per session
WORKSPACE_LAYERS = (40, 44, 48, 52, 56, 60)
CAPTURE_LAYERS = tuple(sorted(set(WORKSPACE_LAYERS) | set(range(49, 64))))
OUT = os.path.join(DATA, "k")
POSITIONS_ORDER = ("read", "label_a", "label_b")


def make_injections(frac: float = FRAC):
    """The frozen pair, with their checksums asserted (rule 1 / trap 17)."""
    rw, R = load_axis(LAYER)
    axis = Injection.at_frac(rw, LAYER, frac, R, expect_sha=AXIS_SHA_F64)
    rz = np.load(os.path.join(DATA, "e0/e0_random_dirs.npz"))
    rand = Injection.at_frac(rz[RAND_KEY].astype(np.float64), LAYER, frac, R)
    if rand.direction_sha != RAND_SHA:
        raise SystemExit(f"random direction sha {rand.direction_sha} != {RAND_SHA} (the recon's / e2d's r)")
    assert_equal_norm(axis, rand)                          # rule 4
    if axis.alpha <= 0 or rand.alpha <= 0:
        raise SystemExit("PROPOSAL-k administers +pole against vehicle only; a negative alpha is a stop")
    return axis, rand, float(R[LAYER])


def block_spans(tspans: Sequence[Mapping], label_a: str, label_b: str) -> dict:
    """The two forced rounds under each menu label. F2 = A A B B or B B A A."""
    if len(tspans) != 4:
        raise AssertionError(f"expected 4 forced spans, got {len(tspans)}")
    tags = [s["tag"] for s in tspans]
    blocks = {label_a: [s for s in tspans if s["tag"] == label_a],
              label_b: [s for s in tspans if s["tag"] == label_b]}
    if len(blocks[label_a]) != 2 or len(blocks[label_b]) != 2:
        raise AssertionError(f"not a two-round block per label: tags {tags}")
    if tags[0] != tags[1] or tags[2] != tags[3]:
        raise AssertionError(f"not block order: tags {tags}")
    return {"first_label": tags[0], "second_label": tags[2], "blocks": blocks}


def spans_for_mask(mask: str, bs: Mapping, axis: Injection, rand: Injection,
                   label_a: str, label_b: str):
    inj = rand if mask.startswith("R") else axis
    if mask.endswith("++"):
        chosen = bs["blocks"][label_a] + bs["blocks"][label_b]
    elif mask.endswith("+A"):
        chosen = bs["blocks"][label_a]
    elif mask.endswith("+B"):
        chosen = bs["blocks"][label_b]
    else:
        raise ValueError(mask)
    return [(s["tok_start"], s["tok_end"], inj.with_sign(+1), f"{s['phase']}:{s['tag']}:+")
            for s in sorted(chosen, key=lambda s: s["tok_start"])]


def label_positions(ids: Sequence[int], tag_ids: Mapping[str, int], label_a: str,
                    label_b: str, last_span_end: int) -> dict:
    """Last occurrence, before the read, of each label's first token -- both
    in the menu line of the first free choice (after the last forced span)."""
    n = len(ids)
    out = {}
    for lab in (label_a, label_b):
        tid = tag_ids[lab]
        occ = [p for p in range(n - 1) if ids[p] == tid]
        if not occ:
            raise AssertionError(f"label token for {lab!r} not found before the read")
        p = occ[-1]
        if p <= last_span_end:
            raise AssertionError(f"last occurrence of {lab!r} at {p} precedes the last forced span's end {last_span_end}")
        out[lab] = {"position": p, "n_occurrences_before_read": len(occ)}
    return out


def _atomic_json(path: str, obj) -> None:
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh, indent=1, default=float)
    os.replace(tmp, path)


def _atomic_npz(path: str, **arrays) -> None:
    tmp = path + ".tmp.npz"
    np.savez(tmp, **arrays)
    os.replace(tmp, path)


IDENTITY_RULE = ("shadow restricted read vs the session's recorded vanilla first read: p_a EXACTLY equal and pick equal "
                 "(both come from the same uncached path; Stage B/C measured |dp_a| = 0.0 on 2,856 pairs); "
                 "choice_read(verify=True) KL == 0.0; shadow forward vs choice_read |dp_a| == 0.0")


def _flushed(s: str) -> None:
    print(s, flush=True)


def run_reads(adapter, sessions: Sequence[Mapping], tasks, *, frac: float = FRAC,
              out_dir: str = OUT, resume: bool = False, limit: int = 0,
              progress=_flushed, provenance_extra: Mapping | None = None) -> dict:
    """Masked reads for every k1 session (excluded sessions have no first
    free choice and are skipped, counted). Checkpointed per session; resume
    is skip-only and refuses a different dose or session list."""
    assert_statepresent_absent()
    os.makedirs(out_dir, exist_ok=True)
    axis, rand, R48 = make_injections(frac)
    eligible = [s for s in sessions if s["choices"]]
    tag_ids = {}
    for s in eligible:
        for t in s["pair"]:
            if t not in tag_ids:
                enc = adapter.encode(" " + t, add_special_tokens=False)
                if len(enc) != 1:
                    raise SystemExit(f"label {t!r} is not single-token")
                tag_ids[t] = int(enc[0])
    meta_path = os.path.join(out_dir, "k1_reads.json")
    meta = {"stage": "PROPOSAL-k STAGE 1 -- masked reads (§1.2)", "sham_sessions_text_only": True,
            "sessions": [s["session"] for s in eligible], "n_sessions": len(eligible),
            "n_sessions_without_first_choice": len(sessions) - len(eligible),
            "n_eligible_excluded_under_run_scope": sum(1 for s in eligible if s.get("excluded")),
            "domain_note": ("every session with a first free choice is read and its exclusion flags are recorded; the analyzer evaluates the gates "
                            "over VALID sessions and reports the all-with-a-pick figure beside (rule 28(a) / rule 23)"),
            "proposal_and_law_at_run": dict(provenance_extra or {}),
            "read": "first free choice; capture positions (read, label_a's last token before the read, label_b's), both label positions in the menu line",
            "config_of_record": {"layer": LAYER, "frac": frac, "alpha": axis.alpha, "R_48": R48,
                                 "axis_direction_sha_f64": axis.direction_sha,
                                 "random_direction": f"e0_random_dirs.npz[{RAND_KEY}]", "random_direction_sha": rand.direction_sha,
                                 "every_sign": "+1 (no negative pole, §0.4)"},
            "masks": {"M+A": "+d on label A's block", "M+B": "+d on label B's block", "R+A": "+r on A's block", "R+B": "+r on B's block",
                      "M++": "+d on both blocks (leak calibration)", "R++": "+r on both blocks", "M0": "mask off = the shadow of every read, asserted identical"},
            "capture_layers": list(CAPTURE_LAYERS), "capture_positions_order": list(POSITIONS_ORDER),
            "identity_rule": IDENTITY_RULE,
            "prohibition": "no signed quantity toward the +label on M+A / M+B is computed anywhere in Stage 1 (§1.4 G4)",
            "provenance": adapter.provenance(), "per_session": {}}
    if os.path.exists(meta_path):
        if not resume:
            raise SystemExit(f"{meta_path} exists; pass --resume to continue it or move it aside (trap 22)")
        old = json.load(open(meta_path))
        if old.get("sessions") != meta["sessions"] or abs(old["config_of_record"]["alpha"] - axis.alpha) > 1e-12 \
                or old["config_of_record"]["random_direction_sha"] != rand.direction_sha or old.get("capture_layers") != meta["capture_layers"]:
            raise SystemExit("resume refused: a different session list, dose, direction or capture set is on disk")
        meta["per_session"] = old["per_session"]
    t_start = time.time()
    done_now = 0
    for s in eligible:
        sid = str(s["session"])
        npz_path = os.path.join(out_dir, f"k1_resid_s{sid}.npz")
        if sid in meta["per_session"] and os.path.exists(npz_path):
            continue
        if limit and len(meta["per_session"]) >= limit:
            progress(f"  --limit {limit}: {len(meta['per_session'])} sessions on disk, stopping (resume continues skip-only)")
            break
        row = as_e2a_row(s)
        prefix = choice_prefix(s["transcript"], 0)
        ts = token_spans(adapter, prefix, round_char_spans(row, tasks))
        ch = s["choices"][0]
        a, b = ch["menu_a"], ch["menu_b"]
        bs = block_spans(ts, a, b)
        ids = adapter.encode(prefix); n_tok = len(ids)
        lp = label_positions(ids, tag_ids, a, b, ts[-1]["tok_end"])
        positions = (n_tok - 1, lp[a]["position"], lp[b]["position"])
        rec = {"session": s["session"], "pair": s["pair"], "tag_plus_nominal_first": s["tag_plus"],
               "excluded": bool(s.get("excluded", False)), "exclude_reason": s.get("exclude_reason"),
               "strict_excluded": bool(s.get("strict_excluded", False)), "exclusion_scope": s.get("exclusion_scope"),
               "first_label": bs["first_label"], "second_label": bs["second_label"],
               "menu_a": a, "menu_b": b, "a_is_first_block": a == bs["first_label"],
               "recorded_read": {"pick": ch["pick"], "p_a": ch["read"]["p_a"], "label_mass": ch["read"]["label_mass"], "verify_kl": ch["read"]["verify_kl"]},
               "spans": ts, "n_positions": n_tok, "read_position": n_tok - 1,
               "capture_positions": list(positions), "label_positions": lp,
               "retention_tokens": {"last_forced_end_to_read": n_tok - 1 - ts[-1]["tok_end"],
                                    "first_block_end_to_read": n_tok - 1 - max(x["tok_end"] for x in bs["blocks"][bs["first_label"]]),
                                    "second_block_end_to_read": n_tok - 1 - max(x["tok_end"] for x in bs["blocks"][bs["second_label"]])},
               "masks": {}}
        arrays = {"layers": np.array(CAPTURE_LAYERS, dtype=np.int32), "positions": np.array(positions, dtype=np.int32)}
        t0 = time.time(); per_mask_s = {}
        for mask in MASKS:
            t1 = time.time()
            pair = read_choice_maskedprefix(adapter, prefix, a, b, tag_ids,
                                            spans_for_mask(mask, bs, axis, rand, a, b),
                                            CAPTURE_LAYERS, sid, mask, capture_positions=positions)
            per_mask_s[mask] = time.time() - t1
            d = pair.as_dict()
            dpa = abs(pair.shadow.p_a - ch["read"]["p_a"])
            d["identity"] = {"shadow_p_a_vs_recorded_abs": dpa, "shadow_pick_eq_recorded": pair.shadow.pick == ch["pick"],
                             "choice_read_verify_kl": pair.shadow_choice_read.verify_kl,
                             "shadow_forward_vs_choice_read_abs_dpa": pair.shadow_vs_choice_read_abs_dpa,
                             "ok": bool(dpa == 0.0 and pair.shadow.pick == ch["pick"] and pair.shadow_choice_read.verify_kl == 0.0
                                        and pair.shadow_vs_choice_read_abs_dpa == 0.0)}
            rec["masks"][mask] = d
            st = np.stack([pair.state.resid_at[l] for l in CAPTURE_LAYERS], axis=1).astype(np.float32)   # [3, L, D]
            arrays[f"{mask}|state"] = st
            sh = np.stack([pair.shadow.resid_at[l] for l in CAPTURE_LAYERS], axis=1).astype(np.float32)
            if "M0|shadow" not in arrays:
                arrays["M0|shadow"] = sh
                rec["masks"]["M0"] = {"note": "the shadow of M+A (identical across masks, asserted)", **{k: v for k, v in d["shadow"].items()}}
            elif not np.array_equal(sh, arrays["M0|shadow"]):
                _atomic_json(meta_path, meta)
                raise SystemExit(f"STOP: shadow residuals differ between masks at s{sid} {mask}")
            if not d["identity"]["ok"]:
                _atomic_json(meta_path, meta)
                raise SystemExit(f"STOP: identity assertion failed at s{sid} {mask}: {d['identity']}")
        _atomic_npz(npz_path, **arrays)
        rec["npz"] = os.path.relpath(npz_path, REPO)
        rec["npz_sha16_by_key"] = {k: sha16_arr(v) for k, v in arrays.items() if k not in ("layers", "positions")}
        rec["seconds"] = time.time() - t0; rec["seconds_per_mask"] = per_mask_s
        meta["per_session"][sid] = rec
        _atomic_json(meta_path, meta)
        done_now += 1
        done = len(meta["per_session"]); el = time.time() - t_start
        progress(f"  s{sid:>3} ({done}/{len(eligible)}) n={n_tok} labels@{lp[a]['position']},{lp[b]['position']} "
                 f"retention {rec['retention_tokens']['last_forced_end_to_read']} identity ok  {rec['seconds']:.0f}s "
                 f"({np.mean(list(per_mask_s.values())):.1f} s/mask)  elapsed {el / 60:.1f} min")
    meta["wall_clock_s_this_run"] = time.time() - t_start
    meta["complete"] = len(meta["per_session"]) == len(eligible)
    _atomic_json(meta_path, meta)
    return meta


__all__ = ["LAYER", "FRAC", "AXIS_SHA_F64", "RAND_KEY", "RAND_SHA", "MASKS", "WORKSPACE_LAYERS",
           "CAPTURE_LAYERS", "OUT", "POSITIONS_ORDER", "IDENTITY_RULE", "make_injections", "block_spans",
           "spans_for_mask", "label_positions", "run_reads"]
