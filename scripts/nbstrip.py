#!/usr/bin/env python3
"""Git clean-filter: strip notebook outputs and execution counts.

Deliberately dependency-free (stdlib only, system python3) rather than
nbstripout from a venv: the venvs here live inside gitignored trees, so a
filter pointing into one breaks silently the moment that tree is rebuilt --
and a silently-broken clean filter means fat notebooks land in the record
without anyone noticing. This script is committed, so the filter works on
any checkout, including the box.

Reads a notebook on stdin, writes the stripped notebook on stdout.
"""
import json, sys

nb = json.load(sys.stdin)
for cell in nb.get("cells", []):
    if "outputs" in cell:
        cell["outputs"] = []
    if "execution_count" in cell:
        cell["execution_count"] = None
    md = cell.get("metadata", {})
    for k in ("execution", "collapsed", "scrolled"):
        md.pop(k, None)
nb.get("metadata", {}).pop("widgets", None)
json.dump(nb, sys.stdout, indent=1, ensure_ascii=False, sort_keys=True)
sys.stdout.write("\n")
