# told-vs-felt

**Companion to the Research Note of 2026-10-27** (posted at https://jasondwyer.github.io/2026-10-27-told-vs-felt-porting-behavioral-pharmacology/). Start at [`README-NOTE.md`](./README-NOTE.md): it maps every figure and claim in the note to the committed file that carries it. The note links this repository at the tag `note-2026-10-v2`; `main` keeps moving and nothing points a reader at it.

The canonical copy of the Research Note is posted at https://jasondwyer.github.io/2026-10-27-told-vs-felt-porting-behavioral-pharmacology.

This repository was named `jspace-lab` until the release, after the J-lens (Jacobian-space) replication it began as; the old name appears throughout the log and in paths, and the old URL redirects here.

> **Names you will see.** Three things share the "J" and none of them is a method of this work.
> - **`jspace-lab`** is this repository's former name; it appears in paths and in every log line written before the release. The old URL redirects here.
> - **`jlens-qwen36`** and its package **`jlens_qwen`** are an external dependency, not code of this repository: an MLX port of Anthropic's Jacobian-lens code (github.com/WeZZard/jlens-qwen36, Apache-2.0, pinned at `d788bc3`; a gitignored clone, never committed here) that served as the Qwen inference stack — model loader, kernel patch, Python environment — for every Qwen run from cycle 1 through the PROPOSAL-m told control. The scripts' `jlens-qwen36/.venv/bin/python` lines name that environment.
> - **"J-space"** and **"J-lens"** in the early documents are the terms of Anthropic's global-workspace paper: the small set of internal representations its Jacobian lens reads. The program began (July 2026) by replicating that paper's five functional properties on Qwen ([`FINDINGS.md`](./FINDINGS.md)), and the lab kept the name. The lens then had two roles: cycle 1's state induction used steering directions built from its vocabulary basis — the design the 2026-08-01 pivot retired — and the Qwen cycles ran a lens-based evaluation-awareness monitor on every trial (unsteered arms decision-relevant; [`CLAUDE.md`](./CLAUDE.md) ledger rule 8). From that pivot on, every state the Research Note reports is extracted and read in the raw residual stream (ledger rule 3: "no vocabulary-basis shortcuts"); the note itself does not use the lens, and the OLMo arm uses none (the models run on PyTorch/CUDA; only the laptop-side analysis scripts are invoked from that same Python environment).

Began as a local replication of Anthropic's J-lens / global-workspace
interpretability work (July 2026) against Qwen3.6-27B on Apple Silicon. It
has since become a four-cycle experimental program asking whether a language
model has *valenced* internal states in the behavioural sense — revealed
preference, never testimony — and is now a developmental study of the same
question across a training series.

**Read [`CLAUDE.md`](./CLAUDE.md) first** — it is the operative design law
(v3.1), including the constraints ledger every run answers to.

## Where the program stood at 2026-08-20 (kept as written)

Four cycles on Qwen converged on **reward-marking without reward-seeking**:
the evaluative state exists, is causally potent, is implantable, and couples
to nothing that chooses. See the synthesis chain
[`FINDINGS.md`](./FINDINGS.md) → [`FINDINGS-2.md`](./FINDINGS-2.md) →
[`FINDINGS-3.md`](./FINDINGS-3.md) → [`FINDINGS-4.md`](./FINDINGS-4.md).

**Phase 2** tests that synthesis developmentally on the OLMo-3.1-32B
instruct lineage (Base → SFT → DPO → Instruct), asking when *marking*, when
*reading*, and whether ever *wanting*. The pre-registration of record is
[`PROPOSAL-g-ontogeny-of-evaluation.md`](./PROPOSAL-g-ontogeny-of-evaluation.md)
(committed `72b09a9`; the hash is its timestamp).

Phase 0 is complete: `valence_core/` is built and accepted under the
refactor-regression law, all four checkpoints are acquired and
hash-anchored, and the CUDA backend is characterized. Phase A (calibration)
is under way.

The program's results as of the release are stated in the note, not here. The labels of record are in `data/m/verdicts/Q-F0_VERDICTS.json`; the dated log is [`RESULTS.md`](./RESULTS.md).

## Orientation

| you want | read |
|---|---|
| the note's companion: every figure's provenance, the pre-registration table, the audit | [`README-NOTE.md`](./README-NOTE.md) |
| the operative law | [`CLAUDE.md`](./CLAUDE.md) |
| the pre-registrations of record and the locks | `PROPOSAL-*.md`, `LOCK-*.md` — committed before data; the commit hash is the timestamp (tabulated in README-NOTE §2) |
| the Phase-2 pre-registration and its bars | [`PROPOSAL-g-…`](./PROPOSAL-g-ontogeny-of-evaluation.md) |
| the dated experiment log (newest first) | [`RESULTS.md`](./RESULTS.md) |
| prior-cycle syntheses | `FINDINGS*.md` |
| frozen prior logs | `archive/` (tags `cycle-2-close`, `cycle-4-close`) |
| licenses | [`LICENSING.md`](./LICENSING.md) |

## Code

`valence_core/` is the model-agnostic measurement battery: a thin
`ModelAdapter` boundary with MLX (Qwen oracle) and PyTorch/CUDA (OLMo)
implementations, plus extraction, steering, readouts, gates, monitors, the
session harness, and the detection and tag-balance harnesses.

Its acceptance test is the point rather than a formality — ledger 26 says a
refactor is accepted only by reproducing published numbers through the new
path:

```bash
python -m valence_core.regression.analysis
```

Model-free; must print **154/154**. Runs anywhere, including the box, because
it reads only committed artifacts. The oracle tier
(`valence_core.regression.oracle`) needs the laptop Qwen stack and reproduces
the three criteria that require real inference.

`scripts/` holds the box-side runners (acquisition, surveys, determinism,
respawn gate) and the Qwen-side satellites.

## Sites

- **Laptop (M4 Pro, MLX)** — design/dev, and the Qwen oracle where every
  published cycle-1–4 number lives. `jlens-qwen36/` is a gitignored external
  clone; nothing is ever committed inside it.
- **Cloud box (A100-80GB, PyTorch/CUDA)** — Phase-2 execution, ephemeral by
  assumption. Weights live on a persistent network volume; the repo is the
  record. A run that exists only on a box does not exist.
