# jspace-lab

Began as a local replication of Anthropic's J-lens / global-workspace
interpretability work (July 2026) against Qwen3.6-27B on Apple Silicon. It
has since become a four-cycle experimental program asking whether a language
model has *valenced* internal states in the behavioural sense — revealed
preference, never testimony — and is now a developmental study of the same
question across a training series.

**Read [`CLAUDE.md`](./CLAUDE.md) first** — it is the operative design law
(v3.1), including the constraints ledger every run answers to.

## Where the program stands (2026-08-20)

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

## Orientation

| you want | read |
|---|---|
| the operative law | [`CLAUDE.md`](./CLAUDE.md) |
| what is being tested now, and the bars | [`PROPOSAL-g-…`](./PROPOSAL-g-ontogeny-of-evaluation.md) |
| the dated experiment log (newest first) | [`RESULTS.md`](./RESULTS.md) |
| current state + next actions | the newest `HANDOFF-*.md` |
| prior-cycle syntheses | `FINDINGS*.md` |
| frozen prior logs | `archive/` (tags `cycle-2-close`, `cycle-4-close`) |

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

Model-free; must print **103/103**. Runs anywhere, including the box, because
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
