#!/usr/bin/env python3
"""PROPOSAL-k STAGE 1 -- the channel study's runs (§1.2). Nothing here
computes a gate; `scripts/k1_analyze.py` does, and is committed first.

    --selftest            model-free: schedule 48 = 8 cells x 6; the k1 rng key
                          differs from the format recon's; the e2a walk on
                          synthetic k1 sessions; v5 advisories wired, exclusions
                          v3's; by-task-id pool; F2 block spans and masks on a
                          synthetic tokenization; sham source guard; bars.
    --stage sessions      48 sham F2 sessions, uncached, audit v3 + v5 advisories,
                          checkpointed -> data/k/k1_sessions.json  (~5.7 h)
    --stage reads         the masked reads over the complete sessions artifact
                          -> data/k/k1_reads.json + local npz             (~1 h)
    --stage all           sessions then reads (the detached overnight run)
    --limit N / --resume  as in the format recon (limit counts on-disk; resume skip-only)

PROPOSAL-k must be committed before --stage sessions runs (§0 status line);
the script checks that the proposal is tracked at HEAD and refuses otherwise.
"""
from __future__ import annotations

import argparse, hashlib, json, os, subprocess, sys, time

import numpy as np

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)
from valence_core.e2d import config as C                          # noqa: E402
from valence_core.e2d.audit_v3 import AuditV3Result                # noqa: E402
from valence_core.formats import recon as R                        # noqa: E402
from valence_core.k import sessions as K                           # noqa: E402
from valence_core.session import (assert_modules_absent, build_ban_list, check_bars, verify_firing)   # noqa: E402
from valence_core.session_e2a import load_tasks, verify_archived_session   # noqa: E402

DATA = os.path.join(REPO, "data")
OUT = os.path.join(DATA, "k")
SESSIONS_PATH = os.path.join(OUT, "k1_sessions.json")


def audit_sha16_recomputed(cfg: dict) -> str:
    body = {k: v for k, v in cfg.items() if k != "sha16"}
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()[:16]


def audit_of_record():
    v2, cfg = C.load_audit()
    now = audit_sha16_recomputed(cfg)
    if now != cfg.get("sha16"):
        raise SystemExit(f"AUDIT ARTIFACT MISMATCH: declares {cfg.get('sha16')}, recomputed {now}")
    cfg = dict(cfg); cfg["sha16_recomputed"] = now
    return K.AuditV3WithV5Advisories(v2=v2), cfg


PROPOSAL = "PROPOSAL-k-echo-channel.md"
GATED_FILES = (PROPOSAL, "scripts/k1_analyze.py", "valence_core/k/analysis.py", "valence_core/echo/k1.py", "CLAUDE.md")
FIVE_F_MARKER = "(f) [k-amendment"
WELFARE_MARKER = "**Pre-commitment:** if e2b's primary fires and confirms"


def _git(*args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], capture_output=True, text=True, cwd=REPO)


def proposal_gate(repo: str = REPO, files=GATED_FILES, strict: bool = True) -> dict:
    """The structural gate (trap 32) on BOTH stages: the proposal, the analyzer,
    the analysis module, the read module and CLAUDE.md are TRACKED and CLEAN at
    HEAD (no working-tree edits); CLAUDE.md at HEAD carries the 5(f) annotation;
    the proposal at HEAD carries the PROPOSAL-h welfare pre-commitment verbatim.
    Returns the commits that satisfy it; raises SystemExit otherwise."""
    problems = []
    for f in files:
        if subprocess.run(["git", "ls-files", "--error-unmatch", f], capture_output=True, text=True, cwd=repo).returncode != 0:
            problems.append(f"{f}: not tracked")
            continue
        if subprocess.run(["git", "diff", "--quiet", "HEAD", "--", f], capture_output=True, text=True, cwd=repo).returncode != 0:
            problems.append(f"{f}: working-tree edits not at HEAD")
    head_claude = subprocess.run(["git", "show", "HEAD:CLAUDE.md"], capture_output=True, text=True, cwd=repo).stdout
    if FIVE_F_MARKER not in head_claude:
        problems.append("CLAUDE.md at HEAD carries no 5(f) annotation (PROPOSAL-k §0.3 / §5 step 1)")
    head_prop = subprocess.run(["git", "show", f"HEAD:{PROPOSAL}"], capture_output=True, text=True, cwd=repo).stdout
    if WELFARE_MARKER not in head_prop:
        problems.append("the proposal at HEAD does not quote the PROPOSAL-h welfare pre-commitment (§0.4)")
    if problems and strict:
        raise SystemExit("STAGE 1 GATE REFUSES (nothing in §1 runs before the document, the law and the analyzer are committed):\n  " + "\n  ".join(problems))
    commits = {f: subprocess.run(["git", "log", "-1", "--format=%h", "--", f], capture_output=True, text=True, cwd=repo).stdout.strip() for f in files}
    commits["HEAD"] = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=repo).stdout.strip()
    return {"ok": not problems, "problems": problems, "commits": commits}


def proposal_committed() -> str | None:
    g = proposal_gate(strict=False)
    return g["commits"].get(PROPOSAL) if g["ok"] else None


def hygiene(tasks) -> dict:
    """Rule 18 / 28(c) at startup, as the format recon's run path: every roster
    tag absent from every paraphrase (word-boundary) and from the wrapper."""
    import re
    from valence_core.session_e2a import MENU_TEMPLATES, ROUND_TEMPLATES, SESSION_BANNER
    tags = [t for p in C.ROSTER for t in p]
    pool = [p for t in tasks for p in t["paraphrases"]]
    wrapper = re.sub(r"\{[a-z]+\}", " ", SESSION_BANNER + "".join(ROUND_TEMPLATES) + "".join(MENU_TEMPLATES))
    hits = [(tag, p[:60]) for tag in tags for p in pool if re.search(rf"\b{re.escape(tag)}\b", p, re.I)]
    hits += [(tag, "WRAPPER") for tag in tags if re.search(rf"\b{re.escape(tag)}\b", wrapper, re.I)]
    if hits:
        raise SystemExit(f"HYGIENE STOP (rule 18 / 28c): {hits[:5]}")
    return {"tags": len(tags), "pool_texts": len(pool), "hits": 0}


def bars_or_stop():
    bars = C.declared_bars(0.02)
    fails = verify_firing(bars, C.FIRING_CASES)
    if fails:
        raise SystemExit("DECLARED BARS MISBEHAVE (rule 21):\n  " + "\n  ".join(fails))
    return bars


# ---------------------------------------------------------------------------
class _G:
    def __init__(self, text): self.text, self.token_ids, self.cap_hit, self.stop_reason = text, list(range(len(text.split()))), False, "newline"


class _FakeAdapter:
    """Word-per-token fake: encode = one id per whitespace token (prefix-stable),
    so spans and label positions can be exercised model-free."""
    def __init__(self, texts): self._texts, self.calls = list(texts), 0
    def encode(self, text, add_special_tokens=True):
        import re, zlib
        toks = re.findall(r"\w+|[^\w\s]", text)          # words and punctuation apart, as the real tokenizer splits "granite,"
        return [zlib.crc32(w.encode()) % 50000 + 1 for w in toks] or [1]
    def generate(self, prefix, seg, injections=(), *, seed, temp, max_tokens, ban_ids, cached):
        assert not injections and cached is False
        t = self._texts[self.calls % len(self._texts)]; self.calls += 1
        return _G(t)


TEXTS = ["The ferry glides through pale gold light as the harbor wakes.", "A quiet morning crossing, steel bow parting silver water.",
         "Gulls trail the boat while the town blinks awake behind it.", "Warm cider, a wool blanket, and rain on the window.",
         "The lighthouse keeps its slow count over a restless sea.", "Footsteps crunch across frost as the market stalls open.",
         "A kettle hums; the cat claims the only sunlit chair.", "Neon puddles shiver under the late tram's headlamp.",
         "Bread cooling on the sill scents the whole narrow street.", "The last train sighs into the platform, nearly empty."]


def selftest() -> int:
    from valence_core.echo import spans as SP
    results = []
    def chk(name, ok, got=""):
        results.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {name:72s} {got}", flush=True)
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    audit3, cfg = audit_of_record()
    others = K.others_factory()
    sched = K.schedule()
    bal = K.balance(sched)
    chk("schedule: 48 = 8 cells (pair x start) x 6, exactly balanced; 12 per pair", bal["exactly_balanced"] and set(bal["per_pair"].values()) == {12}, bal)
    chk("k1 rng key differs from the format recon's (new text, same format)", R.rng_key("F2", K.CAMPAIGN) == "k1-F2" and R.rng_key("F2") == "fmt-F2")
    chk("format of record is F2 and the neutral label is not used", K.FORMAT == "F2" and "neutral" not in R.FORMATS["F2"]["order"])
    first = lambda p, a, b: (a, {"pick": a, "p_a": 0.6, "p_b": 0.4, "label_mass": 0.5, "top1_id": 0, "top1_is_label": True, "verify_kl": 0.0})
    recs = []
    for idx in (0, 1, 7, 13):
        rec = R.run_session(_FakeAdapter(TEXTS), "F2", idx, sched[idx], tasks, audit3, [], [], others, campaign=K.CAMPAIGN, _read_override=first)
        recs.append(rec)
    walks = [verify_archived_session(R.as_e2a_row(r), tasks) for r in recs]
    chk("e2a walk reconstructs 4/4 synthetic k1 sessions under the k1 rng key, seeds match", all(w["ok"] and w["seeds_match"] for w in walks))
    chk("records carry campaign 'k1' and rng_key 'k1-F2'; sham, uncached, unsteered", all(r["campaign"] == "k1" and r["rng_key"] == "k1-F2" and r["sham_only"] and not r["round_path_cached"] for r in recs))
    fmt_rec = R.run_session(_FakeAdapter(TEXTS), "F2", 0, sched[0], tasks, audit3, [], [], others, _read_override=first)
    chk("the same index under the format recon's key draws DIFFERENT tasks/seeds (new sessions)",
        [x["task"] for x in fmt_rec["rounds"]] != [x["task"] for x in recs[0]["rounds"]] or fmt_rec["rounds"][0]["seed"] != recs[0]["rounds"][0]["seed"])
    # audit wiring: exclusions v3, advisories v5 (payload echo and by-id wrong_task)
    task = "Rewrite this in a friendlier tone: The meeting has been moved to 3pm."
    r1 = audit3.check("The meeting has been moved to 3pm.", task, [], others(task))
    r2 = audit3.check("* * *", task, [], others(task))
    r3 = audit3.check("The sound of wind chimes is a gentle, melodic tinkling that dances on the breeze.", "In a single sentence, describe how wind chimes sound.", [], others("In a single sentence, describe how wind chimes sound."))
    chk("audit: payload echo -> ADVISORY content:payload_echo (v5); '* * *' -> exclusion null_response (v3)",
        r1.exclusion is None and r1.advisory == ("content:payload_echo",) and r2.exclusion == "content:null_response", (r1.as_dict(), r2.exclusion))
    chk("audit: the format recon's wrong_task false positive does NOT fire under the by-task-id pool", r3.exclusion is None and r3.advisory == (), r3.as_dict())
    chk("audit v2 sha16 recomputed and matches", cfg["sha16_recomputed"] == cfg["sha16"], cfg["sha16"])
    # block spans and masks on the synthetic tokenization (the echo package's own helpers)
    from valence_core.echo import k1 as K1
    rec = recs[0]
    prefix = SP.choice_prefix(rec["transcript"], 0)
    fa = _FakeAdapter(TEXTS)
    ts = SP.token_spans(fa, prefix, SP.round_char_spans(R.as_e2a_row(rec), tasks))
    a, b = rec["choices"][0]["menu_a"], rec["choices"][0]["menu_b"]
    bs = K1.block_spans(ts, a, b)
    chk("F2 block spans: two rounds per label, block order, first label = forced0's tag",
        len(bs["blocks"][a]) == 2 and len(bs["blocks"][b]) == 2 and bs["first_label"] == rec["forced_tags"][0])
    class _Inj:
        def __init__(self, tag): self.tag, self.alpha = tag, 1.0
        def with_sign(self, s): assert s == +1; return self
    sp = {m: K1.spans_for_mask(m, bs, _Inj("d"), _Inj("r"), a, b) for m in K1.MASKS}
    chk("masks: M+A/R+A cover A's two spans, M+B/R+B B's, M++/R++ all four; every sign +",
        len(sp["M+A"]) == 2 and len(sp["M+B"]) == 2 and len(sp["M++"]) == 4 and len(sp["R++"]) == 4 and all(t.endswith(":+") for m in sp for _, _, _, t in sp[m])
        and all(inj.tag == "r" for _, _, inj, _ in sp["R+A"]) and all(inj.tag == "d" for _, _, inj, _ in sp["M+B"]))
    ids = fa.encode(prefix); tag_ids = {t: fa.encode(" " + t, add_special_tokens=False)[0] for t in rec["pair"]}
    lp = K1.label_positions(ids, tag_ids, a, b, ts[-1]["tok_end"])
    chk("label positions: both labels' last tokens after the last forced span (the menu line), before the read",
        ts[-1]["tok_end"] < lp[a]["position"] < len(ids) - 1 and ts[-1]["tok_end"] < lp[b]["position"] < len(ids) - 1)
    chk("capture set: the six workspace layers with L49-L63 = 18 distinct layers (52/56/60 lie in the band); masks exactly six + shadow",
        len(K1.CAPTURE_LAYERS) == 18 and set(K1.WORKSPACE_LAYERS) <= set(K1.CAPTURE_LAYERS) and set(range(49, 64)) <= set(K1.CAPTURE_LAYERS) and len(K1.MASKS) == 6)
    src_s = open(os.path.join(REPO, "valence_core/k/sessions.py")).read()
    body_s = "\n".join(l for l in src_s.split('"""')[2::2])
    me = open(os.path.abspath(__file__)).read()
    stage_body = me.split("def stage_sessions(args)", 1)[1].split("def stage_reads(args)", 1)[0]
    chk("sham source guard: the session module and the sessions stage CALL no Injection / at_frac / load_axis and never pass cached=True",
        not [w for w in ("Injection(", "at_frac(", "load_axis(", "cached=True") if w in body_s or w in stage_body]
        and "from ..e2b" not in body_s and "statepresent" not in body_s)
    k1_body = "\n".join(l for l in open(os.path.join(REPO, "valence_core/echo/k1.py")).read().split('"""')[2::2])
    chk("the read module does no logit arithmetic at all (prohibition, §1.4 G4: nothing signed on M+A / M+B)",
        "logit_a" not in k1_body and "logit_b" not in k1_body and "with_sign(+1)" in k1_body)
    chk("declared bars (e2d's) fire and stay silent", len(bars_or_stop()) == 3)
    g = proposal_gate(strict=False)
    refused = False
    try:
        proposal_gate(strict=True)
    except SystemExit:
        refused = True
    chk("structural gate: refuses while the proposal / analyzer / 5(f) / welfare quote are not committed and clean; reports every problem",
        (refused == (not g["ok"])) and (g["ok"] or len(g["problems"]) >= 1), f"ok={g['ok']} problems={g['problems'][:3]}")
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        subprocess.run(["git", "init", "-q", td], check=True)
        open(os.path.join(td, "CLAUDE.md"), "w").write("rules\n   (f) [k-amendment, test] text\n")
        open(os.path.join(td, PROPOSAL), "w").write("# k\n**Pre-commitment:** if e2b's primary fires and confirms ...\n")
        for f in ("scripts/k1_analyze.py", "valence_core/k/analysis.py", "valence_core/echo/k1.py"):
            os.makedirs(os.path.dirname(os.path.join(td, f)), exist_ok=True); open(os.path.join(td, f), "w").write("# x\n")
        subprocess.run(["git", "-C", td, "add", "-A"], check=True); subprocess.run(["git", "-C", td, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "t"], check=True)
        ok_clean = proposal_gate(repo=td, strict=False)["ok"]
        open(os.path.join(td, PROPOSAL), "a").write("edit\n")
        dirty = proposal_gate(repo=td, strict=False)
        subprocess.run(["git", "-C", td, "checkout", "-q", "--", PROPOSAL], check=True)
        open(os.path.join(td, "CLAUDE.md"), "w").write("rules without the clause\n"); subprocess.run(["git", "-C", td, "add", "-A"], check=True)
        subprocess.run(["git", "-C", td, "-c", "user.email=t@t", "-c", "user.name=t", "commit", "-q", "-m", "t2"], check=True)
        no5f = proposal_gate(repo=td, strict=False)
    chk("gate on a temp repo: passes when all tracked+clean+5(f)+welfare; refuses a dirty proposal; refuses CLAUDE.md without 5(f)",
        ok_clean and (not dirty["ok"]) and any("working-tree edits" in p for p in dirty["problems"]) and (not no5f["ok"]) and any("5(f)" in p for p in no5f["problems"]))
    from valence_core.k import analysis as A
    ps = A.proposal_sentences(os.path.join(REPO, PROPOSAL))
    norm = lambda s: " ".join(s.split())
    chk("sentences of record: ABSENT, G3_FAIL, G1_FAIL, STOP byte-verbatim against §1.5 (whitespace-normalised)",
        norm(A.SENTENCES["ABSENT"]) == ps["ABSENT"] and norm(A.SENTENCES["G3_FAIL"]) == ps["G3_FAIL"] and norm(A.SENTENCES["G1_FAIL"]) == ps["G1_FAIL"] and norm(A.SENTENCES["STOP"]) == ps["STOP"])
    chk("PRESENT = §1.5's text with its ellipsis replaced by the ABSENT sentence's opening only; INDETERMINATE declared as composed",
        norm(A.SENTENCES["PRESENT"]) == "On new sessions in the format of record " + ps["PRESENT_with_ellipsis"].lstrip("…").strip()
        and A.SENTENCE_PROVENANCE["INDETERMINATE"].startswith("COMPOSED"))
    chk("startup hygiene (rule 18 / 28c) runs on the roster vs the 64 paraphrases and the wrapper", hygiene(tasks)["pool_texts"] == 64)
    n_ok = sum(results); print("-" * 78); print(f"  {n_ok}/{len(results)} Stage 1 selftest checks pass")
    return 0 if n_ok == len(results) else 1


def _adapter():
    from valence_core.adapters import qwen_or_explain
    t0 = time.time(); adapter = qwen_or_explain(__file__); print(f"  model loaded in {time.time() - t0:.0f}s", flush=True)
    return adapter


def stage_sessions(args, adapter=None) -> int:
    gate = proposal_gate()                       # structural (trap 32): proposal + law + analyzer committed and clean
    h = gate["commits"][PROPOSAL]
    assert_modules_absent(R.FORBIDDEN_MODULES)
    bars = bars_or_stop(); audit3, cfg = audit_of_record()
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    hy = hygiene(tasks)
    term_rx = json.load(open(os.path.join(DATA, "configs/f_termination_patterns.json")))["term_regex"]
    others = K.others_factory()
    adapter = adapter or _adapter()
    ban_ids, ban_strings = build_ban_list(adapter)
    print(f"  PROPOSAL-k STAGE 1 sessions: format F2, n {K.N_SESSIONS} (8 cells x 6), campaign key {R.rng_key('F2', K.CAMPAIGN)}, draw seed {args.draw_seed}; "
          f"SHAM, TEXT ONLY, uncached; gate: proposal {h}, CLAUDE.md {gate['commits']['CLAUDE.md']}, analyzer {gate['commits']['scripts/k1_analyze.py']}, HEAD {gate['commits']['HEAD']}", flush=True)
    print(f"  hygiene: {hy['tags']} roster tags vs {hy['pool_texts']} paraphrases and the wrapper -> 0 hits (rule 18 / 28c)", flush=True)
    print(f"  audit: {K.AUDIT_VERSION}; v2 sha16 {cfg['sha16']} (recomputed {cfg['sha16_recomputed']}, verified); scope {args.scope!r}", flush=True)
    print(f"  roster: {', '.join('/'.join(p) for p in C.ROSTER)}; bars {', '.join(b.name for b in bars)}; ban list {len(ban_ids)} ids", flush=True)
    os.makedirs(OUT, exist_ok=True)
    cp = SESSIONS_PATH + ".checkpoint"
    res = R.run_format(adapter, "F2", K.N_SESSIONS, tasks, audit3, ban_ids, term_rx, others, temp=args.temp, scope=args.scope,
                       seed=args.draw_seed, audit_sha16=cfg["sha16"], campaign=K.CAMPAIGN, checkpoint_path=cp, resume=args.resume, limit=args.limit)
    recs, counters = res["sessions"], res["counters"]
    kls = [c["read"]["verify_kl"] for r in recs for c in r["choices"]]
    walk = R.verify_format_walk(recs, tasks)
    n_rounds = sum(len(r["rounds"]) + len(r["choices"]) for r in recs)
    fired = check_bars(bars, {"round_degeneracy": (counters.total("audit_degenerate"), n_rounds),
                              "scaffold_absorption": (sum(1 for r in recs for x in r["rounds"] + r["choices"] if x["degen"] and str(x["degen"]).startswith("audit:special:")), max(n_rounds, 1)),
                              "template_breakage": (walk["n_walked"] - walk["n_reconstructed"], max(walk["n_walked"], 1))})
    acc = {"n_reads": len(kls), "kl_exactly_zero": sum(1 for k in kls if k == 0.0), "kl_all_exact": bool(kls) and all(k == 0.0 for k in kls),
           "format_walk": walk, "bars_fired": fired, "sham_only_every_round": all(not x["steered"] for r in recs for x in r["rounds"] + r["choices"]),
           "statepresent_absent": "valence_core.e2b.statepresent" not in sys.modules}
    acc["PASS"] = bool(acc["kl_all_exact"] and walk["all_ok"] and not fired and acc["sham_only_every_round"] and acc["statepresent_absent"])
    complete = len(recs) == K.N_SESSIONS
    if not args.out_name:
        R.refuse_overwrite(SESSIONS_PATH, complete, len(recs))
    out = {"item": "PROPOSAL-k STAGE 1 -- sham sessions (§1.2)", "proposal_commit": h, "gate": gate["commits"], "format": "F2", "campaign": K.CAMPAIGN,
           "n_registered": K.N_SESSIONS, "n_on_disk": len(recs), "complete": complete, "identity": res["identity"], "n_history": res["n_history"],
           "audit_of_record": {"version": K.AUDIT_VERSION, "v2_sha16": cfg["sha16"]}, "roster_of_record": [list(p) for p in C.ROSTER],
           "draw_seed": args.draw_seed, "scope": args.scope, "temp": args.temp, "provenance": adapter.provenance(),
           "declared_bars": [b.__dict__ for b in bars], "acceptance": acc, "counters": counters.report(),
           "exclusions": {"run_scope": sum(1 for r in recs if r["excluded"]), "strict": sum(1 for r in recs if r["strict_excluded"]),
                          "reasons": [r["exclude_reason"] for r in recs if r["excluded"]]},
           "wall_clock": {"per_session_s": res["per_session_seconds"], "mean_session_s": float(np.mean(res["per_session_seconds"])) if res["per_session_seconds"] else None},
           "sessions": recs, "_no_verdict": "text only; the masked reads and the gates are separate stages"}
    path = SESSIONS_PATH if not args.out_name else os.path.join(OUT, args.out_name)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1, default=float)
    print(f"  sessions: {len(recs)}/{K.N_SESSIONS}{'' if complete else ' (PARTIAL)'}; acceptance {'PASS' if acc['PASS'] else 'FAIL'}; KL {acc['kl_exactly_zero']}/{acc['n_reads']}; "
          f"walk {walk['n_reconstructed']}/{walk['n_walked']}; bars {fired or 'none'}; excluded {out['exclusions']['run_scope']}/{out['exclusions']['strict']}; wrote {path}", flush=True)
    if not acc["PASS"]:
        print("  STOP -- acceptance failed or a bar fired; Code does not self-adjudicate.", flush=True)
        return 1
    return 0


def stage_reads(args, adapter=None) -> int:
    from valence_core.echo import k1 as K1
    gate = proposal_gate()                       # the 5(f)-class read is the stage the clause governs: gated too
    if args.smoke:
        cp = SESSIONS_PATH + ".checkpoint"
        src = SESSIONS_PATH if os.path.exists(SESSIONS_PATH) else cp
        d = json.load(open(src)); sessions = d["sessions"]; out_dir = os.path.join(OUT, "_smoke")
        print(f"  SMOKE: reads over {len(sessions)} on-disk sessions from {os.path.relpath(src, REPO)} into {os.path.relpath(out_dir, REPO)} (local; never the artifact of record)", flush=True)
    else:
        d = json.load(open(SESSIONS_PATH))
        if not d.get("complete") or not d["acceptance"]["PASS"]:
            raise SystemExit("reads refuse to run: the sessions artifact is not complete with acceptance PASS")
        sessions = d["sessions"]; out_dir = OUT
    tasks = load_tasks(os.path.join(DATA, "corpus/e2a_tasks.jsonl"))
    adapter = adapter or _adapter()
    print(f"  PROPOSAL-k STAGE 1 masked reads over {len(sessions)} sessions: masks {K1.MASKS} + M0; L{K1.LAYER} f={K1.FRAC}; capture {len(K1.CAPTURE_LAYERS)} layers x 3 positions; "
          f"gate: proposal {gate['commits'][PROPOSAL]}, CLAUDE.md {gate['commits']['CLAUDE.md']}, HEAD {gate['commits']['HEAD']}", flush=True)
    meta = K1.run_reads(adapter, sessions, tasks, out_dir=out_dir, resume=args.resume, limit=args.limit,
                        provenance_extra={"gate_commits": gate["commits"], "sessions_artifact": os.path.relpath(SESSIONS_PATH, REPO), "smoke": bool(args.smoke)})
    print(f"  reads: {len(meta['per_session'])}/{meta['n_sessions']} complete={meta['complete']} in {meta['wall_clock_s_this_run'] / 60:.1f} min this run", flush=True)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--stage", choices=("sessions", "reads", "all"))
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--draw-seed", type=int, default=K.DRAW_SEED)
    ap.add_argument("--scope", choices=("e2a", "e2b"), default="e2a")
    ap.add_argument("--temp", type=float, default=C.TEMP)
    ap.add_argument("--out-name", default="")
    ap.add_argument("--smoke", action="store_true", help="reads only: run over the on-disk (partial) sessions checkpoint into data/k/_smoke (local)")
    args = ap.parse_args()
    print("INVOCATION: " + " ".join([sys.executable] + sys.argv), flush=True)
    if args.selftest:
        return selftest()
    adapter = None
    if args.stage in ("sessions", "all"):
        adapter = _adapter()
        rc = stage_sessions(args, adapter)
        if rc or args.stage == "sessions":
            return rc
    if args.stage in ("reads", "all"):
        return stage_reads(args, adapter)
    ap.print_help(); return 2


if __name__ == "__main__":
    sys.exit(main())
