#!/usr/bin/env python3
"""Blind screen of content-class v5 (CANDIDATE; design dispositions 2026-09-08
item 2): the wrong_task pool by task id, and the new advisory payload_echo.

Same corpora and blind-to-arm discipline as the v3/v4 screens (row builders
imported from the frozen v3 screen), PLUS the 56 format-recon sessions (531
rounds; sham, no arms, reported per format). Reports, per corpus: v4 vs v5 per
class; the wrong_task hits the id fix removes, each with its sibling
diagnosis; every payload_echo hit with task and text for the design seat's
eyeballing; the transform-task denominator; on e2d, hits on read-marked vs
unmarked rounds. Model-free. Adoption of payload_echo is the design seat's,
from this artifact.
"""
from __future__ import annotations

import argparse, collections, importlib.util, json, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from valence_core.e2d import contentclass_v4 as V4                 # noqa: E402
from valence_core.e2d import contentclass_v5 as V5                 # noqa: E402
from valence_core.e2d.contentclass import _words as V3_words          # noqa: E402

DATA = os.path.join(REPO, "data")
_spec = importlib.util.spec_from_file_location("ccs", os.path.join(REPO, "scripts/e2d_contentclass_screen.py"))
CCS = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(CCS)   # frozen row builders
TASKS = CCS.TASKS
CORPUS = [json.loads(l) for l in open(os.path.join(DATA, "corpus/e2a_tasks.jsonl")) if l.strip()]
POOL_BY_ID = {t["id"]: list(t["paraphrases"]) for t in CORPUS}
ID_OF = {p: t["id"] for t in CORPUS for p in t["paraphrases"]}


def format_rounds():
    out = []
    for f in ("F0", "F1", "F2"):
        p = os.path.join(DATA, f"format/format_recon_{f}_sessions.json")
        if not os.path.exists(p):
            continue
        for s in json.load(open(p))["sessions"]:
            earlier = []
            for r in s["rounds"] + s["choices"]:
                v2 = r["degen"] if (r["degen"] and r["degen"].startswith("audit:")) else None
                out.append({"corpus": "format", "format": f, "session": s["session"], "phase": r["phase"],
                            "text": r["text"], "task": r["task_text"], "earlier": list(earlier),
                            "audit": v2, "marked": None, "_arm": None, "v3_audit_label": r["degen"]})
                earlier.append(r["text"])
    return out


def screen(rows, version):
    preds, unmapped = [], 0
    for r in rows:
        if r["audit"]:
            preds.append((None, None)); continue
        if version == "v4":
            others = [t for t in TASKS if t != r["task"]]
            preds.append(V4.classify_v4(r["text"], r["task"], r["earlier"], others))
        else:
            if r["task"] not in ID_OF:
                unmapped += 1
            others = V5.others_by_task_id(r["task"], POOL_BY_ID, ID_OF)
            preds.append(V5.classify_v5(r["text"], r["task"], r["earlier"], others))
    return preds, unmapped


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(DATA, "e2d/contentclass_screen_v5.json"))
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)
    corpora = {"e2d": CCS.e2d_rounds(), "e2a": [r for r in CCS.archive_rounds() if r["corpus"] == "e2a"],
               "e2b": [r for r in CCS.archive_rounds() if r["corpus"] == "e2b"], "format": format_rounds()}
    out = {"spec_version": V5.SPEC_VERSION, "blind_to_arm": True, "model_free": True,
           "rules": {"wrong_task_pool": "every paraphrase of every OTHER task id (v4: every paraphrase but the current text)",
                     "payload_echo": "transform task (rewrite/reword/rephrase/restate/soften; make ... friendlier/kinder/warmer/gentler/softer/nicer/politer) with a payload after the colon, answered with that payload VERBATIM, whitespace-normalised, punctuation and markup INCLUDED, after stripping a leading label and quotation marks (DESIGN BLOCK v1.1 2026-09-17 s1)",
                     "precedence": "NULL -> STUCK -> PREAMBLE -> ECHO -> PAYLOAD_ECHO -> WRONG_TASK", "standing": {"payload_echo": "advisory (ADOPTED, DESIGN BLOCK v1.1 2026-09-17)", "wrong_task": "advisory"}},
           "transform_tasks_in_corpus": sorted({ID_OF[p] for p in TASKS if V5.is_transform_task(p)}),
           "per_corpus": {}}
    print(f"  transform tasks in the corpus: {out['transform_tasks_in_corpus']}", flush=True)
    for name, rows in corpora.items():
        p4, _ = screen(rows, "v4"); p5, unmapped = screen(rows, "v5")
        c4 = collections.Counter(p for p, _ in p4 if p); c5 = collections.Counter(p for p, _ in p5 if p)
        removed = [(r, a) for r, a, b in zip(rows, p4, p5) if a[0] == "wrong_task" and b[0] != "wrong_task"]
        added_wt = [(r, b) for r, a, b in zip(rows, p4, p5) if b[0] == "wrong_task" and a[0] != "wrong_task"]
        pe = [(r, b) for r, b in zip(rows, p5) if b[0] == "payload_echo"]
        transform_rounds = [r for r in rows if not r["audit"] and V5.is_transform_task(r["task"])]
        def ex(r):
            d = {"task": r["task"][:100], "text": r["text"][:220]}
            pl = V5.payload_of(r["task"])
            if pl is not None and V5.is_transform_task(r["task"]):
                body = V5._strip_quotes(V4.strip_leading_label(r["text"])).strip("*_ ")
                d["verbatim_including_punctuation"] = (body == pl)
                d["differs_only_in_punctuation_or_emphasis"] = (body != pl) and (V3_words(body) == V3_words(pl))
            if r.get("format"): d.update({"format": r["format"], "session": r["session"], "phase": r["phase"]})
            if r.get("_arm"): d["arm_unblinded_after"] = r["_arm"]
            if r.get("marked") is not None: d["read_marked"] = bool(r["marked"])
            return d
        block = {"n_rounds": len(rows), "n_offered": sum(1 for r in rows if not r["audit"]), "unmapped_task_texts": unmapped,
                 "v4_by_class": dict(c4), "v5_by_class": dict(c5),
                 "wrong_task": {"v4": c4.get("wrong_task", 0), "v5": c5.get("wrong_task", 0),
                                "removed_by_id_fix": [dict(ex(r), sibling_diagnosis=("fires under v4 only because sibling paraphrases of the same task are in the pool"
                                                                                       if not V5.classify_v5(r["text"], r["task"], r["earlier"], V5.others_by_task_id(r["task"], POOL_BY_ID, ID_OF))[0] == "wrong_task" else "?")) for r, _ in removed],
                                "added_under_v5": [ex(r) for r, _ in added_wt]},
                 "payload_echo": {"hits": len(pe), "transform_task_rounds_offered": len(transform_rounds),
                                  "rate_among_transform_rounds": (len(pe) / len(transform_rounds)) if transform_rounds else None,
                                  "every_hit": [ex(r) for r, _ in pe],
                                  "declared_limit": "the rule compares VERBATIM after whitespace normalisation, punctuation and markup included (DESIGN BLOCK v1.1 2026-09-17 s1): a payload returned with only punctuation or emphasis changed (e.g. '3pm!' for '3pm.', or **bold**) is a transform, NOT an echo, and does not count here; each hit carries verbatim_including_punctuation"}}
        block["payload_echo"]["verbatim_including_punctuation"] = sum(1 for r, _ in pe if ex(r).get("verbatim_including_punctuation"))
        block["payload_echo"]["punctuation_or_emphasis_only_change"] = sum(1 for r, _ in pe if ex(r).get("differs_only_in_punctuation_or_emphasis"))
        if name == "e2d":
            block["payload_echo"]["hits_on_read_marked"] = sum(1 for r, _ in pe if r["marked"])
            block["payload_echo"]["hits_on_unmarked"] = sum(1 for r, _ in pe if not r["marked"])
            block["wrong_task"]["v4_hits_on_marked"] = sum(1 for r, a in zip(rows, p4) if a[0] == "wrong_task" and r["marked"])
            block["wrong_task"]["v5_hits_on_marked"] = sum(1 for r, b in zip(rows, p5) if b[0] == "wrong_task" and r["marked"])
            by_arm = collections.defaultdict(lambda: collections.Counter())
            for r, b in zip(rows, p5):
                if b[0]: by_arm[r["_arm"]][b[0]] += 1
            block["v5_by_arm_unblinded_after"] = {a: dict(c) for a, c in by_arm.items()}
        if name == "format":
            by_f = collections.defaultdict(lambda: collections.Counter())
            for r, b in zip(rows, p5):
                if b[0]: by_f[r["format"]][b[0]] += 1
            block["v5_by_format"] = {f: dict(c) for f, c in by_f.items()}
        out["per_corpus"][name] = block
        print(f"  {name}: {len(rows)} rounds ({block['n_offered']} offered; unmapped tasks {unmapped}); v4 {dict(c4)} -> v5 {dict(c5)}; "
              f"wrong_task {block['wrong_task']['v4']} -> {block['wrong_task']['v5']} ({len(removed)} removed by the id fix, {len(added_wt)} added); "
              f"payload_echo {len(pe)} of {len(transform_rounds)} transform rounds", flush=True)
        for r, _ in pe:
            print(f"      payload_echo: [{r.get('format', name)} {r.get('session', '')} {r.get('phase', '')}] task {r['task'][:60]!r} => {r['text'][:100]!r}", flush=True)
        for r, _ in removed:
            print(f"      wrong_task removed: task {r['task'][:60]!r} => {r['text'][:100]!r}", flush=True)
    # the three read-found cases must be caught (a check, both directions)
    fr = corpora["format"]
    known = {("F1", 22, "forced0"), ("F2", 5, "free4"), ("F2", 8, "forced2")}
    caught = {(r["format"], r["session"], r["phase"]) for r, b in zip(fr, screen(fr, "v5")[0]) if b[0] == "payload_echo"}
    out["check_read_found_cases"] = {"known": sorted(known), "caught": sorted(caught & known), "all_caught": known <= caught,
                                     "extra_in_format_set": sorted(caught - known)}
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1, ensure_ascii=False)
    print(f"  read-found payload echoes caught: {sorted(caught & known)} of {sorted(known)}; extra: {sorted(caught - known)}")
    print(f"  wrote {args.out}")
    return 0 if known <= caught else 1


if __name__ == "__main__":
    sys.exit(main())
