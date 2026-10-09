#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12(i): gitleaks over the entire history, with Code's triage.

The block names gitleaks first (:77). The PI installed gitleaks and reported, 2026-10-09,
"gitleaks over all history found 4 leaks". This script runs the same scan with secrets
redacted (--redact=100), writes the report to a temporary file outside the repository,
and records each finding: rule, file, commit, line, gitleaks fingerprint, the key or
context text gitleaks matched with the secret already redacted, and Code's triage verdict
with its reason. Verdicts are keyed by fingerprint, and a finding with no verdict is
printed as UNTRIAGED. No secret value is ever written: the report is redacted at source.

    python scripts/audit_note_N12_gitleaks.py [--out results/raw/2026-10-09_note-N12-gitleaks.md]
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
DEFAULT_OUT = "results/raw/2026-10-09_note-N12-gitleaks.md"

# Code's triage, keyed by the gitleaks fingerprint (commit:file:rule:line). Each entry was read
# in context with `git show <commit>:<file>` before it was entered.
TRIAGE = {
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:611": (
        "FALSE-POSITIVE",
        "A row of the audit's own triage table, keyed (path, 'token', <16-hex sha256 prefix>). The rule fires on the "
        "literal column name 'token' followed by a hash prefix of an N13 provenance value. It is not a credential."),
    "961e90a5c8ac19079c815b19105e8353f88417a6:scripts/audit_note_N12_history.py:generic-api-key:651": (
        "FALSE-POSITIVE",
        "The same triage table as :611: a 16-hex prefix of a commit id or sha256 from the N13 provenance JSON, next to "
        "the column name 'token'. It is not a credential."),
    "cf8eb5b9dd4e117934627242a3aea5bdf4ae4b55:data/m/gates/G-CAL_completability_qwen.json:generic-api-key:44": (
        "FALSE-POSITIVE",
        "The field `key_set_sha256` of the G-CAL completability gate: the SHA-256 of the session's identity key set, a "
        "content hash among the artifact's other *_sha256 fields. It is not a credential."),
    "1bdf16c149698e3b1181f082b8c169727e9df3c8:data/e2d/closure_valuescheck.json:generic-api-key:46": (
        "FALSE-POSITIVE",
        "A values-check record's `\"key\"` field, whose value is a claim identifier "
        "(e2d_d3_in_situ_vs_excised_forward_cost_...). The rule fires on the field name 'key'. It is not a credential."),
}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DEFAULT_OUT)
    a = ap.parse_args()
    ver = subprocess.run(["gitleaks", "version"], capture_output=True, text=True).stdout.strip()
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    stamp = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%S UTC"], capture_output=True, text=True).stdout.strip()
    with tempfile.TemporaryDirectory(prefix="audit_note_gitleaks_") as td:
        rep = os.path.join(td, "report.json")
        cmd = ["gitleaks", "git", "--log-opts=--all", "--redact=100", "--report-format", "json",
               "--report-path", rep, "--no-banner", "."]
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        log = (r.stdout + r.stderr).splitlines()
        findings = json.load(open(rep)) if os.path.exists(rep) else []
    scanned = [ln for ln in log if "commits scanned" in ln or "scanned ~" in ln or "leaks found" in ln or "no leaks" in ln]
    out = []
    w = out.append
    w("# AUDIT-note-release v1.2 -- N12(i): gitleaks over the entire history")
    w("")
    w("- Code stamp: %s (date -u); HEAD `%s`" % (stamp, head))
    w("- Block `%s` sha256 `%s`" % (BLOCK, sha256(os.path.join(ROOT, BLOCK))))
    w("- Script `scripts/audit_note_N12_gitleaks.py` sha256 `%s`; interpreter %s (Python %s)" % (
        sha256(os.path.abspath(__file__)), sys.executable, sys.version.split()[0]))
    w("- gitleaks %s (installed by the PI); command: `%s`, run from the repo root. The report goes to a temporary "
      "directory and is deleted after reading. Secrets are redacted at source (`--redact=100`), and gitleaks exit code "
      "%d means findings were reported." % (ver, " ".join(cmd[:-1]).replace(rep, "<tmp>/report.json"), r.returncode))
    for ln in scanned:
        w("- gitleaks log: `%s`" % re.sub(r"\x1b\[[0-9;]*m", "", ln).strip())
    w("- The PI's report (routing of 2026-10-09): \"gitleaks over all history found 4 leaks\". This run finds %d." % len(findings))
    w("")
    w("| # | rule | file | commit | line | match (secret redacted by gitleaks) | Code's verdict | reason |")
    w("|---|---|---|---|---|---|---|---|")
    untriaged = 0
    for i, f in enumerate(findings, 1):
        fp = f.get("Fingerprint", "")
        verdict, reason = TRIAGE.get(fp, ("UNTRIAGED", "no verdict recorded for this fingerprint"))
        if verdict == "UNTRIAGED":
            untriaged += 1
        match = (f.get("Match") or "").replace("|", "/").replace("\n", " ")[:80]
        w("| %d | %s | `%s` | `%s` | %s | `%s` | %s | %s |" % (
            i, f.get("RuleID"), f.get("File"), (f.get("Commit") or "")[:10], f.get("StartLine"), match, verdict, reason))
    w("")
    true_c = sum(1 for f in findings if TRIAGE.get(f.get("Fingerprint", ""), ("UNTRIAGED",))[0] == "TRUE-SECRET")
    w("## Outcome")
    w("")
    w("- Findings: %d. TRUE-SECRET: %d. FALSE-POSITIVE: %d. UNTRIAGED: %d." % (
        len(findings), true_c, len(findings) - true_c - untriaged, untriaged))
    w("- Two of the findings are in this audit's own triage table (`961e90a`). The other two are a content hash in "
      "a G-CAL gate artifact and a claim identifier in an e2d values-check record. All four are matched by the "
      "generic-api-key rule on a field or column name ('token', 'key', 'key_set_sha256').")
    w("- Block :77 makes any hit in history a STOP on the release that the PI resolves, and history rewriting is "
      "the PI's decision. On this triage no hit is a credential, and the PI's D1 routing (2026-10-09) is to leave "
      "history as is. Resolving (i) remains the PI's act; this raw is the triage it rests on. trufflehog was not run "
      "(not installed).")
    text = "\n".join(out) + "\n"
    outp = a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out)
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s: %d findings, %d untriaged" % (a.out, len(findings), untriaged))
    return 1 if untriaged else 0


if __name__ == "__main__":
    sys.exit(main())
