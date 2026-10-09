# Licensing

Copyright 2026 Jason Dwyer.

- **Code** is licensed under the Apache License, Version 2.0 ([`LICENSE`](./LICENSE)). Code means the Python packages and modules (`valence_core/`), the scripts (`scripts/`, including the `audit_note_*` audit scripts), shell drivers, and notebooks (`*.ipynb`).
- **Documents and data** are licensed under the Creative Commons Attribution 4.0 International license ([`LICENSE-CC-BY-4.0`](./LICENSE-CC-BY-4.0)). This covers everything else in the repository: the Markdown documents (pre-registrations, logs, findings, handoffs, the audit block, README files), `data/`, `results/` (including `results/raw/`), `figures/`, and `archive/`.

## Third-party material

Some third-party material keeps its own terms, which these licenses do not change:

- **Macar et al. 2026 (arXiv:2603.21396).** The prompt text recovered from this work is in `data/configs/b2_framing.json`, `data/configs/b2_concepts.json` and the `MACAR_FRAMING` / `TRIAL_QUESTION` constants in `valence_core/detection.py`. It covers the framing, the acknowledgement turn, the trial question and the extraction template. The paper, which prints this text, is distributed under CC BY 4.0; attribution is to the paper. The companion code repository (github.com/safety-research/introspection-mechanisms, pinned in the config) carries no license file. Provenance: `results/raw/2026-10-08_note-N12-licenses.md`.
- **Lindsey 2025.** The fifty concepts and one hundred baseline words in `data/configs/b2_concepts.json` originate in Lindsey (2025), *Emergent Introspective Awareness in Large Language Models* (Anthropic; transformer-circuits.pub/2025/introspection). That page states no license. The lists are attributed to Lindsey (2025), and this repository does not relicense them.
- **Models.** No model weights are included. The OLMo checkpoints (allenai) and Qwen3.6-27B (mlx-community conversion) are used under their own licenses, as their model cards state.
- **Jacobian lenses.** The lenses used in cycles 1–4 are not included; see the N12 licenses raw for their sources and licenses.
- **`jlens-qwen36/`** is a gitignored external clone of a third-party repository. Nothing from it is tracked here.

Each license text is reproduced verbatim:

| File | Source | sha256 |
|---|---|---|
| `LICENSE` | Apache License 2.0 | `cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30`, equal to the canonical `LICENSE-2.0.txt` |
| `LICENSE-CC-BY-4.0` | CC BY 4.0 legal code, plain text | `cce5d01fa4a83b794271bd2c28cffdf99afd43c803e6ddefddae39b591ea7448` |
