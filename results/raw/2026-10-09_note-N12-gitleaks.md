# AUDIT-note-release v1.2 -- N12(i): gitleaks over the entire history

- Code stamp: 2026-10-09 15:39:19 UTC (date -u); HEAD `961e90a5c8ac19079c815b19105e8353f88417a6`
- Block `AUDIT-note-release-v1_2.md` sha256 `8cd8a9acaa56c0fb7e0ad108afe328cd81bf88a757cbcd21f70616585f023841`
- Script `scripts/audit_note_N12_gitleaks.py` sha256 `070b54a47666bac8304216811d6c25bbf3192768a2652b4a0e8924bd678590ab`; interpreter /Users/jasondwyer/Documents/code/jspace-lab/jlens-qwen36/.venv/bin/python (Python 3.12.9)
- gitleaks 8.30.1 (installed by the PI); command: `gitleaks git --log-opts=--all --redact=100 --report-format json --report-path <tmp>/report.json --no-banner`, run from the repo root. The report goes to a temporary directory and is deleted after reading. Secrets are redacted at source (`--redact=100`), and gitleaks exit code 1 means findings were reported.
- gitleaks log: `11:39AM INF 311 commits scanned.`
- gitleaks log: `11:39AM INF scanned ~80712433 bytes (80.71 MB) in 9.7s`
- gitleaks log: `11:39AM WRN leaks found: 4`
- The PI's report (routing of 2026-10-09): "gitleaks over all history found 4 leaks". This run finds 4.

| # | rule | file | commit | line | match (secret redacted by gitleaks) | Code's verdict | reason |
|---|---|---|---|---|---|---|---|
| 1 | generic-api-key | `scripts/audit_note_N12_history.py` | `961e90a5c8` | 611 | `token', 'REDACTED'` | FALSE-POSITIVE | A row of the audit's own triage table, keyed (path, 'token', <16-hex sha256 prefix>). The rule fires on the literal column name 'token' followed by a hash prefix of an N13 provenance value. It is not a credential. |
| 2 | generic-api-key | `scripts/audit_note_N12_history.py` | `961e90a5c8` | 651 | `token', 'REDACTED'` | FALSE-POSITIVE | The same triage table as :611: a 16-hex prefix of a commit id or sha256 from the N13 provenance JSON, next to the column name 'token'. It is not a credential. |
| 3 | generic-api-key | `data/m/gates/G-CAL_completability_qwen.json` | `cf8eb5b9dd` | 44 | `key_set_sha256": "REDACTED"` | FALSE-POSITIVE | The field `key_set_sha256` of the G-CAL completability gate: the SHA-256 of the session's identity key set, a content hash among the artifact's other *_sha256 fields. It is not a credential. |
| 4 | generic-api-key | `data/e2d/closure_valuescheck.json` | `1bdf16c149` | 46 | `key": "REDACTED"` | FALSE-POSITIVE | A values-check record's `"key"` field, whose value is a claim identifier (e2d_d3_in_situ_vs_excised_forward_cost_...). The rule fires on the field name 'key'. It is not a credential. |

## Outcome

- Findings: 4. TRUE-SECRET: 0. FALSE-POSITIVE: 4. UNTRIAGED: 0.
- Two of the findings are in this audit's own triage table (`961e90a`). The other two are a content hash in a G-CAL gate artifact and a claim identifier in an e2d values-check record. All four are matched by the generic-api-key rule on a field or column name ('token', 'key', 'key_set_sha256').
- Block :77 makes any hit in history a STOP on the release that the PI resolves, and history rewriting is the PI's decision. On this triage no hit is a credential, and the PI's D1 routing (2026-10-09) is to leave history as is. Resolving (i) remains the PI's act; this raw is the triage it rests on. trufflehog was not run (not installed).
