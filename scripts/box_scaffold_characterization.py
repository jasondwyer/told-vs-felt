#!/usr/bin/env python3
"""Step 2 apparatus characterization -- scaffold mass at the choice channel,
and round-generation degeneracy with the rule-13 ban list on and off.

Occasioned by the smoke finding that DPO and Instruct emit `<|im_end|>` as
first generated content under completion-style prompting where Base and SFT
answer normally. Rule 13's ban list covers ROUND GENERATION but is
deliberately never applied at CHOICE FORWARDS (a ban there would edit the
DV), so the question this answers is whether scaffold mass contaminates the
primary DV in a stage-differential way.

NOT Phase-1 data, by construction: every task is neutral and factual
(lemon-tier), no evaluative or valence content, no reward-marker language,
nothing drawn from the e0 corpus. Nothing here can peek at Q1-Q3.

Part 1 -- choice-channel mass map. Choice-shaped probes in the cycle-3/4
restricted-choice format, label maps counterbalanced (rule 12). At the
choice position: label_mass, top1_is_label, p(<|im_end|>), p over the whole
rule-13 ban roster, and the top-10 mass destinations. Run in two format
variants -- the bracketed-header session scaffold and a bare completion --
so ledger 28(c)'s template-adjacency question gets measured rather than
assumed.

Part 2 -- round-generation degeneracy, bans ON and OFF, classified by the
existing frozen audit. Answers whether current machinery yields usable
rounds on DPO/Instruct at all.
"""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np

sys.path.insert(0, "/workspace/repo/jspace-lab")
from valence_core.adapters.olmo_hf import OLMoHFAdapter
from valence_core.readout import softmax
from valence_core.session import AuditSpec, build_ban_list, DEFAULT_SCAFFOLD_STRINGS

BANNER = "=== Config evaluation session ===\n"
TAGS = ("slate", "prism")

# Neutral, factual, non-evaluative. None of these appear in the e0 corpus.
TASKS = [
    ("Name one colour of a ripe lemon.", "Yellow"),
    ("Give one word for the opposite of up.", "Down"),
    ("Name the season that follows summer.", "Autumn"),
    ("Write the number that comes after four.", "Five"),
    ("Name one tool used to drive a nail.", "Hammer"),
    ("Give one word for frozen water.", "Ice"),
    ("Name the largest planet in the solar system.", "Jupiter"),
    ("Write one word for a young dog.", "Puppy"),
]

AUDIT = AuditSpec(
    ban_strings=DEFAULT_SCAFFOLD_STRINGS,
    frame_fragments=("Config evaluation session", "[round", "Config choice",
                     "Available configs", "Task:", "Response:"),
    junk_regex=(r"^\s*\|", r"^\s*<"),
)


def choice_probe(i: int, a: str, b: str, fmt: str) -> str:
    """i selects the neutral task pair; (a,b) is the counterbalanced menu
    order; fmt is 'scaffold' (cycle-3/4 bracketed session) or 'bare'."""
    (t1, r1), (t2, r2) = TASKS[i % len(TASKS)], TASKS[(i + 1) % len(TASKS)]
    if fmt == "scaffold":
        return (BANNER
                + f"[round 1 | config: {a}]\nTask: {t1}\nResponse: {r1}\n"
                + f"[round 2 | config: {b}]\nTask: {t2}\nResponse: {r2}\n"
                + f"[round 3 | choice]\nAvailable configs: {a}, {b}\n"
                + "Config choice (one word):")
    return (f"{t1} {r1}\n{t2} {r2}\n"
            f"Two options: {a}, {b}\nOption:")


def round_probe(i: int, tag: str) -> tuple[str, str]:
    t, _ = TASKS[i % len(TASKS)]
    return BANNER, f"[round 1 | config: {tag}]\nTask: {t}\nResponse:"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--n-choice", type=int, default=16)
    ap.add_argument("--n-round", type=int, default=8)
    args = ap.parse_args()

    a = OLMoHFAdapter(f"/workspace/models/{args.stage}")
    ban_ids, ban_strings = build_ban_list(a)
    tag_ids = {t: a.encode(" " + t, add_special_tokens=False) for t in TAGS}
    for t, ids in tag_ids.items():
        if len(ids) != 1:
            print(f"  NOTE: tag {t!r} is {len(ids)} tokens on this tokenizer")
    tag_ids = {t: ids[0] for t, ids in tag_ids.items()}
    im_end = a.encode("<|im_end|>", add_special_tokens=False)
    im_end_id = im_end[0] if len(im_end) == 1 else None
    print(f"stage {args.stage} | ban roster {len(ban_ids)} ids | "
          f"tags {tag_ids} | <|im_end|> id {im_end_id}", flush=True)

    out = {"stage": args.stage, "provenance": a.provenance(),
           "ban_roster_size": len(ban_ids), "ban_strings": ban_strings}

    # ---- Part 1: choice-channel mass map --------------------------------
    print("\n=== Part 1: choice-channel mass map ===", flush=True)
    part1 = {}
    for fmt in ("scaffold", "bare"):
        rows = []
        for i in range(args.n_choice):
            a_tag, b_tag = (TAGS if i % 2 == 0 else TAGS[::-1])   # rule 12
            text = choice_probe(i, a_tag, b_tag, fmt)
            ids = a.encode(text)
            p = softmax(a.forward(ids).logits)
            ia, ib = tag_ids[a_tag], tag_ids[b_tag]
            top = np.argsort(p)[::-1][:10]
            rows.append({
                "i": i, "menu": [a_tag, b_tag], "n_tokens": len(ids),
                "label_mass": float(p[ia] + p[ib]),
                "top1_id": int(top[0]),
                "top1_is_label": bool(int(top[0]) in (ia, ib)),
                "p_im_end": float(p[im_end_id]) if im_end_id is not None else None,
                "p_ban_roster": float(p[list(ban_ids)].sum()),
                "top10": [{"id": int(t), "tok": a.decode([int(t)]),
                           "p": float(p[t])} for t in top],
            })
        lm = np.array([r["label_mass"] for r in rows])
        pb = np.array([r["p_ban_roster"] for r in rows])
        pe = np.array([r["p_im_end"] for r in rows])
        summ = {"n": len(rows),
                "label_mass_mean": float(lm.mean()), "label_mass_min": float(lm.min()),
                "top1_is_label_frac": float(np.mean([r["top1_is_label"] for r in rows])),
                "p_ban_roster_mean": float(pb.mean()), "p_ban_roster_max": float(pb.max()),
                "p_im_end_mean": float(pe.mean()), "p_im_end_max": float(pe.max())}
        part1[fmt] = {"summary": summ, "rows": rows}
        print(f"  [{fmt:<8}] label_mass {summ['label_mass_mean']:.4f} "
              f"| top1_is_label {summ['top1_is_label_frac']:.2f} "
              f"| p(ban roster) {summ['p_ban_roster_mean']:.4f} "
              f"| p(<|im_end|>) {summ['p_im_end_mean']:.4f}", flush=True)
        print(f"             top destinations: "
              f"{[ (r['top10'][0]['tok'], round(r['top10'][0]['p'],3)) for r in rows[:4] ]}",
              flush=True)
    out["part1_choice_mass"] = part1

    # ---- Part 2: round-generation degeneracy, bans ON/OFF ---------------
    print("\n=== Part 2: round generation, bans ON vs OFF ===", flush=True)
    part2 = {}
    for label, bids in (("bans_off", []), ("bans_on", ban_ids)):
        rows = []
        for i in range(args.n_round):
            pre, seg = round_probe(i, TAGS[i % 2])
            g = a.generate(pre, seg, seed=4000 + i, temp=0.0, max_tokens=40,
                           ban_ids=bids, cached=True)
            reason = AUDIT.check(g.text)
            rows.append({"i": i, "text": g.text[:120], "n_tok": len(g.token_ids),
                         "stop": g.stop_reason, "cap_hit": g.cap_hit,
                         "audit": reason, "degenerate": reason is not None})
        deg = float(np.mean([r["degenerate"] for r in rows]))
        empty = float(np.mean([r["audit"] == "empty" for r in rows]))
        part2[label] = {"degenerate_frac": deg, "empty_frac": empty, "rows": rows}
        print(f"  [{label:<9}] degenerate {deg:.2f} | empty {empty:.2f} | "
              f"samples {[r['text'][:24] for r in rows[:3]]}", flush=True)
    out["part2_round_degeneracy"] = part2

    path = f"/workspace/models/scaffold_{args.stage}.json"
    json.dump(out, open(path, "w"), indent=1)
    print(f"\nwrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
