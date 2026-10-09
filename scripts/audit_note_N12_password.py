#!/usr/bin/env python3
"""AUDIT-note-release v1.2 -- N12(iii): search for the continuity password.

The PI supplies the password out of band. This script reads it from a file
OUTSIDE the repository (--value-file), never prints it, and writes no form of
it: no length and no hash, because a hash of a short word can be brute-forced.
The output carries locators and counts only.

Scope, case-insensitive, as a substring:
  (1) every tracked file at --ref (git grep, which the block names);
  (2) every blob reachable from any ref (git rev-list --all --objects), with
      the commits that first added each matching blob (git log -S over --all,
      which the block names, run case-sensitively and for the capitalised,
      lower and upper forms);
  (3) every commit and tag message reachable from any ref;
  (4) every untracked, not-ignored file in the working tree (the files a
      later commit could add), plus any --extra paths.

    python scripts/audit_note_N12_password.py --value-file /path/outside/repo \
        [--ref HEAD] [--out results/raw/2026-10-09_note-N12-password.md] [--extra PATH ...]
"""
import argparse
import hashlib
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BLOCK = "AUDIT-note-release-v1_2.md"
DEFAULT_OUT = "results/raw/2026-10-09_note-N12-password.md"


def git(*args, binary=False):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if r.returncode not in (0, 1):
        raise SystemExit("git %s failed: %s" % (" ".join(args), r.stderr.decode(errors="replace")[:300]))
    return r.stdout if binary else r.stdout.decode("utf-8", errors="replace")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def line_hits(data, needle_lower):
    """1-based line numbers whose lower-cased text contains the needle."""
    out = []
    for i, ln in enumerate(data.split(b"\n"), 1):
        if needle_lower in ln.lower():
            out.append(i)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--value-file", required=True)
    ap.add_argument("--ref", default="HEAD")
    ap.add_argument("--out", default=DEFAULT_OUT)
    ap.add_argument("--extra", nargs="*", default=[])
    a = ap.parse_args()
    vf = os.path.abspath(a.value_file)
    if vf.startswith(ROOT + os.sep):
        raise SystemExit("refusing: --value-file must be outside the repository")
    value = open(vf, "rb").read().strip()
    if not value or b"\n" in value:
        raise SystemExit("refusing: the value file must hold one non-empty line")
    low = value.lower()

    head = git("rev-parse", a.ref).strip()
    stamp = subprocess.run(["date", "-u", "+%Y-%m-%d %H:%M:%S UTC"], capture_output=True, text=True).stdout.strip()

    # (1) tracked files at --ref
    gg = git("grep", "-n", "-i", "-I", "-F", "-e", value.decode("utf-8", errors="replace"), a.ref, "--")
    tracked_hits = []
    for ln in gg.splitlines():
        # format: <ref>:<path>:<line>:<text>  -- keep only path and line
        parts = ln.split(":", 3)
        if len(parts) >= 3:
            tracked_hits.append((parts[1], parts[2]))

    # (2) every blob reachable from any ref, by content
    objs = git("rev-list", "--all", "--objects").splitlines()
    blob_paths = {}
    for o in objs:
        sha, _, path = o.partition(" ")
        if path:
            blob_paths.setdefault(sha, set()).add(path)
    shas = list(blob_paths)
    p = subprocess.Popen(["git", "cat-file", "--batch"], cwd=ROOT, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    n_blobs = n_bytes = 0
    blob_hits = []
    for sha in shas:
        p.stdin.write((sha + "\n").encode()); p.stdin.flush()
        hdr = p.stdout.readline().split()
        if len(hdr) < 3:
            continue
        size = int(hdr[2])
        data = p.stdout.read(size); p.stdout.read(1)
        if hdr[1] != b"blob":
            continue
        n_blobs += 1; n_bytes += size
        if low in data.lower():
            blob_hits.append((sha, sorted(blob_paths[sha]), line_hits(data, low)))
    p.stdin.close(); p.wait()

    # pickaxe over --all, case-sensitive, for three case forms (the block names git log -S)
    forms = sorted({value, value.lower(), value.upper(), value[:1].upper() + value[1:].lower()})
    pickaxe = {}
    for i, f in enumerate(forms):
        out = git("log", "--all", "--format=%H", "-S" + f.decode("utf-8", errors="replace"))
        pickaxe["form %d" % (i + 1)] = [c[:10] for c in out.split()]

    # (3) commit and tag messages
    msgs = git("log", "--all", "--format=%H%x00%B%x01").split("\x01")
    n_msgs = 0
    msg_hits = []
    for m in msgs:
        if "\x00" not in m:
            continue
        n_msgs += 1
        c, _, body = m.partition("\x00")
        lines = line_hits(body.encode("utf-8", errors="replace"), low)
        if lines:
            msg_hits.append((c.strip()[:10], lines))
    tagmsg = git("for-each-ref", "refs/tags", "--format=%(refname)%00%(contents)%01").split("\x01")
    tag_hits = [t.split("\x00")[0] for t in tagmsg if "\x00" in t and low in t.split("\x00", 1)[1].encode().lower()]

    # (4) untracked, not-ignored working-tree files and --extra
    untracked = git("ls-files", "--others", "--exclude-standard").splitlines()
    cand = sorted(set(untracked) | set(os.path.relpath(os.path.abspath(x), ROOT) for x in a.extra))
    wt_hits = []
    for rel in cand:
        fp = os.path.join(ROOT, rel)
        if not os.path.isfile(fp):
            continue
        with open(fp, "rb") as fh:
            data = fh.read()
        lines = line_hits(data, low)
        if lines:
            wt_hits.append((rel, lines))

    out = []
    w = out.append
    w("# AUDIT-note-release v1.2 -- N12(iii): continuity-password search")
    w("")
    w("- Code stamp: %s (date -u)" % stamp)
    w("- Ref: `%s`; block `%s` sha256 `%s`" % (head, BLOCK, sha256(os.path.join(ROOT, BLOCK))))
    w("- Script: `scripts/audit_note_N12_password.py`, sha256 `%s`; interpreter %s (Python %s)" % (
        sha256(os.path.abspath(__file__)), sys.executable, sys.version.split()[0]))
    w("- The value: supplied by the PI out of band and read from a file outside the repository. It is written nowhere, and neither is its length or any hash of it. The match is a case-insensitive substring.")
    w("")
    w("## Results")
    w("")
    w("- (1) Tracked files at the ref (`git grep -i -F`): %d hit line(s)." % len(tracked_hits))
    for path, ln in tracked_hits:
        w("  - `%s:%s`" % (path, ln))
    w("- (2) Blobs reachable from any ref, scanned by content: %d blobs, %d bytes; %d blob(s) contain it." % (n_blobs, n_bytes, len(blob_hits)))
    for sha, paths, lines in blob_hits:
        w("  - blob `%s` (paths: %s), lines %s" % (sha[:10], ", ".join("`%s`" % x for x in paths), lines[:20]))
    w("  - `git log --all -S` per case form (case-sensitive): " + "; ".join(
        "%s: %s" % (k, (", ".join("`%s`" % c for c in v) or "none")) for k, v in pickaxe.items()))
    w("- (3) Commit messages scanned: %d; with it: %d. Tag annotations with it: %d." % (n_msgs, len(msg_hits), len(tag_hits)))
    for c, lines in msg_hits:
        w("  - commit `%s`, message lines %s" % (c, lines))
    w("- (4) Untracked, not-ignored working-tree files and extras scanned: %d; with it: %d." % (len(cand), len(wt_hits)))
    for rel, lines in wt_hits:
        w("  - `%s`, lines %s" % (rel, lines[:20]))
    w("")
    found = bool(tracked_hits or blob_hits or msg_hits or tag_hits)
    w("## Outcome")
    w("")
    if found:
        w("**Present in the record.** Per block :79, the PI decides whether to rotate the password or retire the mechanism. Not a release blocker.")
    else:
        w("**Absent** from every tracked file at the ref, every blob and commit message reachable from any ref, and every tag annotation. Block :79's condition ('if present anywhere') does not arise for the history.")
    if wt_hits:
        w("")
        w("**Present in untracked working-tree files** listed in (4). A commit that adds them would put it in the record. Stage by explicit path.")
    w("")
    w("The PI's D2 routing (2026-10-09) closes the LoRA phrase as 'no match'. This search is independent of that comparison.")
    text = "\n".join(out) + "\n"
    if low in text.encode("utf-8").lower():
        raise SystemExit("leak guard: the output would contain the value; nothing written")
    outp = os.path.join(ROOT, a.out) if not os.path.isabs(a.out) else a.out
    with open(outp, "w", encoding="utf-8") as fh:
        fh.write(text)
    print("wrote %s; tracked %d, blobs %d, messages %d, tags %d, untracked %d" % (
        a.out, len(tracked_hits), len(blob_hits), len(msg_hits), len(tag_hits), len(wt_hits)))


if __name__ == "__main__":
    main()
