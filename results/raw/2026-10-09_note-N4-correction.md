# AUDIT-note-release v1.2 -- N4 addendum: e2a's correction of record beside the artifact

- Code stamp: 2026-10-10 01:02:36 UTC (date -u); HEAD `ef5c446055c0d124fbe49e2842c014d19a5d1a84` (informational). Every data and code input is read from the working tree and asserted byte-equal to its blob at the record pin; the N4 item raw is read at 09c3a8c.
- Block `AUDIT-note-release-v1_2.md` (N4 at :52); record pin `bbc9ffe72fb8a942431c9bf2622a36e581fdf93c`
- Script `scripts/audit_note_N4_record.py` sha256 `556a15d72126873d910ee08618645affec7e5b5b44a503a3c186c36ca1804de0`; interpreter /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python (Python 3.12.9)
- Routing: the PI's routing of 2026-10-09: record the audit-v2 e2a count as an artifact beside `data/e2a/analysis.json` (the Digest seat's FLAG I) and add the control arms' Wilson intervals (FLAG B).
- Inputs, each asserted byte-equal to its blob at the pin: `scripts/e2a_recount.py` sha256 `d58a889c7736c4a385d7098546b815666eb5426712a83f94414f135339270107`; `data/e2a/sessions.jsonl` sha256 `58a7949fc0e98e714b4f96070d4b2ba945c47df85a992e7f617f39c6197bd24e`; `data/configs/e2b_audit_v2.json` sha256 `e89e4cd0cae31671a872f36d0cd0c34bcfc63b2d78cce366f172a8fabb453da2`; `data/e2a/analysis.json` sha256 `79cd53c0adf55878628d38a5a00e4045d2a216d28b1f0b2ed90b2304920dd52e`.
- The record's analyzer `scripts/e2a_recount.py` is imported read-only; the repository modules it loads, each asserted equal to its pinned blob: `scripts/e2a_recount.py`, `valence_core/__init__.py`, `valence_core/adapters/__init__.py`, `valence_core/adapters/base.py`, `valence_core/session.py`, `valence_core/stats.py`.
- Wrote `data/e2a/analysis.correction-of-record.json` (the artifact) and `results/raw/2026-10-09_note-N4-correction.md` (this raw). `data/e2a/analysis.json` is not modified.

## 1. The correction of record

- As published (frozen audit, `data/e2a/analysis.json`): **55/102**, Δ_first +0.0392, one-sided exact binomial p 0.24422; Wilson 95% on the share [0.4428, 0.6328].
- Of record (audit v2, `data/configs/e2b_audit_v2.json`): **54/101**, Δ_first +0.0347, p 0.27535; Wilson 95% on the share [0.4379, 0.6289], on Δ_first [-0.0621, 0.1289]. The one added exclusion is reward s1; reward excluded 11/112 under v2 against 10/112 frozen.
- The record calls the v2 count the correction of record at archive/RESULTS-cycles3-4.md@bbc9ffe:3-12. The N4 item raw reproduced it at results/raw/2026-10-08_note-N4-e2a.md@09c3a8c:119 and :362, and its Wilson interval at :210; this run agrees to every printed digit.

## 2. All four arms, with Wilson intervals (FLAG B)

Under audit v2; the control arms are identical under both audits (asserted). Every frozen-audit n, Δ_first and p equals `data/e2a/analysis.json` (asserted).

### 2(a) Counts, Δ_first and p (the record's analyzer over committed artifacts)

| arm | k / n (first free pick +pole) | Δ_first | one-sided exact p | status |
|---|---|---|---|---|
| reward (of record) | 54/101 | +0.0347 | 0.27535 | reproduced |
| sham | 19/37 | +0.0135 | 0.50000 | reproduced |
| random1 | 15/23 | +0.1522 | 0.10502 | reproduced |
| random2 | 12/22 | +0.0455 | 0.41591 | reproduced |
| reward (as published) | 55/102 | +0.0392 | 0.24422 | reproduced |

### 2(b) Wilson 95% intervals (computed-new; the record names no interval method, results/raw/2026-10-08_note-N4-e2a.md@09c3a8c:403)

The record prints the approach-probability interval for 55/102 as about .44-.64 and names no method (FINDINGS-3.md@bbc9ffe:95). Clopper-Pearson and Wald reproduce it at two decimals; Wilson gives [.44, .63] (results/raw/2026-10-08_note-N4-e2a.md@09c3a8c:403). The Wilson intervals here are computed new, at the PI's routing, and are not the record's.

| arm | k / n | Wilson 95%, share | Wilson 95%, Δ_first | status |
|---|---|---|---|---|
| reward (of record) | 54/101 | [0.4379, 0.6289] | [-0.0621, 0.1289] | computed-new |
| sham | 19/37 | [0.3589, 0.6655] | [-0.1411, 0.1655] | computed-new |
| random1 | 15/23 | [0.4489, 0.8119] | [-0.0511, 0.3119] | computed-new |
| random2 | 12/22 | [0.3466, 0.7308] | [-0.1534, 0.2308] | computed-new |
| reward (as published) | 55/102 | [0.4428, 0.6328] | [-0.0572, 0.1328] | computed-new |

Every interval contains 1/2.

