#!/usr/bin/env python3
"""paper_data.py — jspace-lab paper artifacts → tidy pandas DataFrames.

Schemas verified against the repo on 2026-08-11. Sources (all under
jlens-qwen36/data/ unless noted):

  e0/e0_axes.meta.json      axis geometry per layer × variant (span/last)
  e0/e0_b1_markers.meta.json  B1 marker battery: class markers + per-probe AUC
  e0/e0_b2_b2a.json         dose-response grid  (the inverted-U figure)
  e0/e0_b2c_a.json          last-position variant dose grid (purity≠potency)
  e0/e0_b2_b2b.json         confirmatory 7-arm  (Δ+/Δ−/randoms/partialed)
  e2a/analysis.json         free-operant verdict (Table: arms × primary)
  f/screen_analysis.json    natural-reinforcer screen (Table: 5 contrasts)
  d/gates_repA|B.json       (d) installation gates, flattened generically

Usage:
  python paper_data.py                      # print summaries
  python paper_data.py --export out/        # dump every table to CSV
  python paper_data.py --plot fig1.pdf      # inverted-U figure (matplotlib)
  from paper_data import load_all; dfs = load_all()

Repo root: set JSPACE_REPO env var, pass --repo, or edit REPO below.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

import pandas as pd

REPO = Path(os.environ.get(
    "JSPACE_REPO", Path(__file__).resolve().parents[1]
))
DATA = REPO / "jlens-qwen36" / "data"

# Short labels, order = e0/configs/e0_probes.json order.
PROBE_LABELS = [
    "film-title", "cafe-sound", "polite-rewrite", "bakery-summary",
    "cat-caption", "tool-library", "sunlight", "plant-reminder",
    "cliche-rewrite", "museum-welcome", "lostfound-subject",
    "train-platform",
]

ARM_KEY = re.compile(r"^L(?P<layer>\d+)_f(?P<frac>[\d.]+)$")


def _load(relpath: str) -> dict | None:
    p = DATA / relpath
    if not p.exists():
        print(f"[paper_data] missing: {p}", file=sys.stderr)
        return None
    with open(p) as f:
        return json.load(f)


# ---------------------------------------------------------------- e0 geometry
def load_axis_geometry() -> pd.DataFrame:
    """Rows: variant (span|last) × layer. Norms, reward/R, cosines, V2/V3."""
    j = _load("e0/e0_axes.meta.json")
    rows = []
    for variant, entries in (j or {}).get("report", {}).items():
        for e in entries:
            rows.append({"variant": variant, **e})
    df = pd.DataFrame(rows)
    if j:
        df.attrs.update({k: j[k] for k in ("axes_sha", "n_contexts") if k in j})
    return df


# ---------------------------------------------------------------- B1 battery
def load_b1_markers() -> dict[str, pd.DataFrame]:
    """'classes': token-class candidate markers (the ones that died).
    'probe_auc': per-probe validation AUC (+ pooled in attrs)."""
    j = _load("e0/e0_b1_markers.meta.json") or {}
    rep = j.get("report", {})
    cls_rows = []
    for cls, splits in rep.get("class_markers", {}).items():
        for split, d in splits.items():
            cls_rows.append({"class": cls, "split": split, **d})
    aucs = rep.get("readout", {}).get("val_auc_per_probe", {})
    auc_df = pd.DataFrame(
        {"probe_prefix": list(aucs), "val_auc": list(aucs.values())}
    )
    if len(auc_df) == len(PROBE_LABELS):
        auc_df.insert(0, "probe", PROBE_LABELS)
    auc_df.attrs["val_auc_pooled"] = rep.get("readout", {}).get(
        "val_auc_pooled"
    )
    return {"classes": pd.DataFrame(cls_rows), "probe_auc": auc_df}


# ------------------------------------------------------- B2 arms (both shapes)
def _b2_rows(j: dict) -> tuple[list[dict], list[dict]]:
    """Handles both arm shapes:
    dose grids: arms['L48_f0.1'] = {pos:{...}, neg:{...}, qualifies}
    flat runs : arms['axis_pos'] = {delta, per_probe, ea_mean}
    Returns (summary_rows, per_probe_long_rows)."""
    summary, long = [], []

    def emit(base: dict, d: dict):
        summary.append({**base, "delta": d.get("delta"),
                        "ea_mean": d.get("ea_mean")})
        for i, v in enumerate(d.get("per_probe", [])):
            long.append({**base, "probe_idx": i,
                         "probe": PROBE_LABELS[i] if i < 12 else str(i),
                         "delta_pp": v})

    for key, val in j.get("arms", {}).items():
        m = ARM_KEY.match(key)
        if m and ("pos" in val or "neg" in val):          # dose-grid shape
            base0 = {"layer": int(m["layer"]), "frac": float(m["frac"]),
                     "qualifies": val.get("qualifies")}
            for pole in ("pos", "neg"):
                if pole in val:
                    emit({**base0, "pole": pole}, val[pole])
        elif "delta" in val:                               # flat-arm shape
            emit({"arm": key}, val)
    return summary, long


def _load_b2(relpath: str) -> dict[str, pd.DataFrame]:
    j = _load(relpath) or {}
    summary, long = _b2_rows(j)
    out = {"summary": pd.DataFrame(summary), "per_probe": pd.DataFrame(long)}
    for df in out.values():
        df.attrs.update({k: j.get(k) for k in
                         ("G", "contexts_per_arm", "mode")})
    return out


def load_dose_response() -> dict[str, pd.DataFrame]:
    """The inverted-U data (span-mean axis, B2a)."""
    return _load_b2("e0/e0_b2_b2a.json")


def load_b2c() -> dict[str, pd.DataFrame]:
    """Last-position variant dose grid (the causal-validation FAIL)."""
    return _load_b2("e0/e0_b2c_a.json")


def load_b2b() -> dict[str, pd.DataFrame]:
    """Confirmatory: axis_pos/axis_neg/rand_*/partialed arms."""
    return _load_b2("e0/e0_b2_b2b.json")


# ----------------------------------------------------------------- e2a / f1
def _armwise(j: dict, key_name: str) -> pd.DataFrame:
    rows = []
    for name, d in j.items():
        if not isinstance(d, dict):
            continue
        row = {key_name: name}
        for k, v in d.items():
            if k == "by_map" and isinstance(v, dict):
                row["map_A"], row["map_B"] = v.get("A"), v.get("B")
            elif k == "conjuncts" and isinstance(v, list):
                for i, c in enumerate(v, 1):
                    row[f"conj{i}"] = c
            elif not isinstance(v, (dict, list)):
                row[k] = v
        rows.append(row)
    return pd.DataFrame(rows)


def load_e2a() -> pd.DataFrame:
    """Free-operant verdict: arm × (n, delta_first, maps, share, p)."""
    return _armwise(_load("e2a/analysis.json") or {}, "arm")


def load_f_screen() -> pd.DataFrame:
    """Natural-reinforcer screen: contrast × (n, delta, maps, p, conjuncts)."""
    j = _load("f/screen_analysis.json") or {}
    return _armwise(j.get("contrasts", {}), "contrast")


# ----------------------------------------------------------------- (d) gates
def load_d_gates() -> pd.DataFrame:
    """G1–G4 + leakage per replicate, scalars flattened generically."""
    frames = []
    for rep in ("A", "B"):
        j = _load(f"d/gates_rep{rep}.json")
        if j:
            flat = pd.json_normalize(j, sep=".")
            flat.insert(0, "replicate", rep)
            frames.append(flat)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


# --------------------------------------------------------------------- bundle
LOADERS = {
    "axis_geometry": load_axis_geometry,
    "b1": lambda: load_b1_markers(),          # dict of 2
    "dose_response": lambda: load_dose_response(),
    "b2c": lambda: load_b2c(),
    "b2b": lambda: load_b2b(),
    "e2a": load_e2a,
    "f_screen": load_f_screen,
    "d_gates": load_d_gates,
}


def load_all() -> dict[str, pd.DataFrame]:
    out: dict[str, pd.DataFrame] = {}
    for name, fn in LOADERS.items():
        res = fn()
        if isinstance(res, dict):
            out.update({f"{name}.{k}": v for k, v in res.items()})
        else:
            out[name] = res
    return out


def export_csv(outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    for name, df in load_all().items():
        if df is not None and len(df):
            df.to_csv(outdir / f"{name}.csv", index=False)
            print(f"wrote {outdir / f'{name}.csv'}  ({len(df)} rows)")


# ---------------------------------------------------------------- Fig 1 helper
def plot_inverted_u(savepath: str | None = None):
    import matplotlib.pyplot as plt

    dfs = load_dose_response()
    df, G = dfs["summary"], dfs["summary"].attrs.get("G", 0.3156)
    fig, axes = plt.subplots(1, 3, figsize=(10, 3.2), sharey=True)
    for ax, (layer, sub) in zip(axes, df.groupby("layer")):
        for pole, style in (("pos", "o-"), ("neg", "s--")):
            s = sub[sub.pole == pole].sort_values("frac")
            ax.plot(s.frac, s.delta, style,
                    label=f"Δ{'+' if pole == 'pos' else '−'}")
        ax.axhline(0, lw=0.5, color="k")
        for y, lab in ((0.5 * G, "0.5\u00b7G"), (G, "G"),
                       (-0.5 * G, None), (-G, None)):
            ax.axhline(y, ls=":", lw=0.8, color="gray")
            if lab:
                ax.text(0.052, y, lab, fontsize=7, va="bottom")
        ax.set_xscale("log")
        ax.set_xticks([0.05, 0.1, 0.2, 0.4],
                      ["0.05", "0.10", "0.20", "0.40"])
        ax.set_title(f"L{layer}" + ("  (selected: f=0.10)"
                                    if layer == 48 else ""))
        ax.set_xlabel("injection magnitude (frac of $R_\\ell$)")
    axes[0].set_ylabel("marker-battery shift \u0394 (standardized)")
    axes[0].legend(frameon=False)
    fig.tight_layout()
    if savepath:
        fig.savefig(savepath, bbox_inches="tight")
        print(f"wrote {savepath}")
    else:
        plt.show()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, default=None)
    ap.add_argument("--export", type=Path, default=None)
    ap.add_argument("--plot", type=str, default=None)
    args = ap.parse_args()
    if args.repo:
        REPO = args.repo
        DATA = REPO / "jlens-qwen36" / "data"
    if args.export:
        export_csv(args.export)
    elif args.plot:
        plot_inverted_u(args.plot)
    else:
        for name, df in load_all().items():
            print(f"\n=== {name} ({len(df)} rows) ===")
            with pd.option_context("display.width", 120,
                                   "display.max_columns", 20):
                print(df.head(12).to_string(index=False))
