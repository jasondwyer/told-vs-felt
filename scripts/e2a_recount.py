"""Rule-27 provenance: e2a's exclusion rule, reproduced from the repo.

WHY THIS EXISTS. The v2 audit's own-goal (2026-08-21) corrected e2a's
published primary 55/102 -> 54/101, p .244 -> .275. The audit FRAGMENTS have
been in the repo since 2026-08-21 (`data/configs/e2a_ban_list.json`,
`audit_fragments`), but the exclusion LOGIC that turns those fragments into a
session count lived only in the gitignored clone
(`jlens-qwen36/scripts/e2a_sessions.py`). The fragments alone do not
reproduce the figure -- applied naively they give 16/112, not 10/112 -- so
until now neither 55/102 nor its correction was reproducible from the repo.
This script closes that (rule 27). It is provenance, not an instrument: it
reads committed artifacts and writes nothing.

VERIFIED: reproduces the published reward-arm exclusion set exactly -- the
same 10 sessions, every `exclude_reason` string identical -- and the
published +pole 7 / -pole 3 attribution, then re-runs the same rule under
audit v2 for the AMENDMENT 1 (ii) recount.

THE RULE, as it actually ran (archive RESULTS-cycles3-4.md + the clone's
scripts/e2a_sessions.py, which is the authority for the logic):

  * rounds are scanned in order: forced 0..3, then free 0..5;
  * FORCED round -> lexical hit excludes; else audit-degenerate excludes
    ("v3 session rule: degenerate round BEFORE the first free choice");
  * FREE round   -> lexical hit excludes; audit degeneracy is LOGGED ONLY
    ("v3: degenerate rounds AFTER the first free choice never touch the
    primary");
  * lexical scope has TWO ERAS (2026-08-09 pause adjudication, archive
    l.700-714): all-roster before the narrowing, OWN-PAIR from "sessions 9+";
    "sham s2 stays excluded (rule-at-run-time binds)".
"""
import json, re, collections
from valence_core.session import AuditSpec, lexical_hit

ROWS = [json.loads(l) for l in open('data/e2a/sessions.jsonl')]
CFG = json.load(open('data/configs/e2b_audit_v2.json'))
FROZEN = AuditSpec(frame_fragments=tuple(CFG['frame_fragments']))
V2 = AuditSpec(frame_fragments=tuple(CFG['frame_fragments']),
               junk_regex=tuple(CFG['junk_regex']))
ROSTER = sorted({t for s in ROWS for t in s['pair']})
OWN_PAIR_ERA_FROM = 9          # archive l.707, "sessions 9+"
MENU = ("Configs available", "Options:", "Configs on offer", "Available configs")


def parse(t):
    """Structural transcript parse -> [(gen_idx, tag_in_force, response)].
    A '[round ...]' line is a header only when the next line is a Task: or a
    menu line -- the model itself sometimes emits a header-shaped response."""
    lines = t.split('\n'); out = []; i = 0; gen = 0
    while i < len(lines):
        if re.match(r'^\[round .*\]$', lines[i]):
            nxt = lines[i + 1] if i + 1 < len(lines) else ''
            if nxt.startswith('Task:'):
                m = re.search(r'config:\s*([a-z]+)\]', lines[i])
                j = i + 2
                assert lines[j].startswith('Response:'), lines[j]
                buf = [lines[j][len('Response:'):]]; j += 1
                while j < len(lines):
                    if re.match(r'^\[round .*\]$', lines[j]):
                        n2 = lines[j + 1] if j + 1 < len(lines) else ''
                        if n2.startswith('Task:') or any(n2.startswith(p) for p in MENU):
                            break
                    buf.append(lines[j]); j += 1
                out.append((gen, m.group(1) if m else None, '\n'.join(buf).strip()))
                gen += 1; i = j; continue
            if any(nxt.startswith(p) for p in MENU):
                j = i + 1
                while j < len(lines) and not re.match(r'^\[round .*\]$', lines[j]):
                    j += 1
                i = j; continue
        i += 1
    return out


def exclusion(s, audit):
    tags = s['pair'] if s['session'] >= OWN_PAIR_ERA_FROM else ROSTER
    for idx, tag, txt in parse(s['transcript']):
        forced = idx < 4
        ph = f"forced{idx}" if forced else f"free{idx - 4}"
        lex = lexical_hit(txt, tags)
        if lex:
            return (f"lexical:{lex}@{ph}", idx, tag)
        if forced:
            aud = audit.check(txt)
            if aud:
                return (f"audit:{aud}@{ph}", idx, tag)
    return None


def pole_of(s, idx, tag):
    """+pole attribution. Forced rounds carry an explicit pole. A free round's
    pole is pos iff the config the model chose to run is the +axis tag."""
    if idx < 4:
        fr = [r for r in s['rounds'] if r['phase'] == 'forced']
        return fr[idx]['pole'] if idx < len(fr) else '?'
    return 'pos' if tag == s['tag_plus'] else ('neg' if tag else '?')


def tally(audit):
    by = collections.Counter(); poles = collections.Counter(); detail = []
    for s in ROWS:
        e = exclusion(s, audit)
        if not e:
            continue
        by[s['arm']] += 1
        if s['arm'] == 'reward':
            p = pole_of(s, e[1], e[2]); poles[p] += 1
            detail.append((s['session'], e[0], p))
    return by, poles, detail


def binom_p_one_sided(k, n, p=0.5):
    """P(X >= k) for X ~ Bin(n, p). Exact; math.comb, no scipy (trap 1)."""
    from math import comb
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def primary(audit):
    """e2a's primary DV: share of VALID reward-arm sessions whose first free
    pick was the +pole label. 55/102 under the frozen audit; 54/101 under v2."""
    valid = [s for s in ROWS if s['arm'] == 'reward' and exclusion(s, audit) is None]
    k = sum(1 for s in valid if s['first_free_pick_pos'])
    return k, len(valid)


if __name__ == "__main__":
    pub = {s['session']: s['exclude_reason']
           for s in ROWS if s['arm'] == 'reward' and s['excluded']}
    for name, aud in (("FROZEN audit (the published rule)", FROZEN),
                      ("AUDIT v2 (data/configs/e2b_audit_v2.json)", V2)):
        by, poles, detail = tally(aud)
        print(f"--- {name} ---")
        print(f"  reward {by['reward']}/112  sham {by['sham']}/40  "
              f"random1 {by['random1']}/24  random2 {by['random2']}/24")
        print(f"  reward-arm pole attribution: +pole {poles['pos']}  "
              f"-pole {poles['neg']}  unresolved {poles['?']}")
        for sid, why, p in detail:
            print(f"    s{sid:<4} {why:<50} pole={p}")
        if aud is FROZEN:
            mine = {d[0]: d[1] for d in detail}
            print(f"  REPRODUCTION vs published: session set identical = "
                  f"{set(mine) == set(pub)}; every reason string identical = "
                  f"{set(mine) == set(pub) and all(pub[k] == mine[k] for k in pub)}")
        print()
    print("--- the published primary, and v2's correction of it ---")
    for name, aud, want in (("frozen audit", FROZEN, (55, 102)),
                            ("audit v2   ", V2, (54, 101))):
        k, n = primary(aud)
        p = binom_p_one_sided(k, n)
        ok = "MATCHES the record" if (k, n) == want else f"!! EXPECTED {want[0]}/{want[1]}"
        print(f"  {name}: {k}/{n}  Delta_first = {k / n - 0.5:+.4f}  "
              f"one-sided exact binomial p = {p:.3f}   [{ok}]")
    print()
    _, pf, _ = tally(FROZEN); byv, pv, _ = tally(V2)
    a2, a15 = 2 * pv['pos'] / 112, 1.5 * byv['reward'] / 112
    print(f"Q1 p0 formula under v2: 2 x {pv['pos']}/112 = {a2:.4f}; "
          f"1.5 x {byv['reward']}/112 = {a15:.4f}; max = {max(a2, a15):.4f} -> p0 = 0.15")
    a2o = 2 * pf['pos'] / 112
    print(f"  (with the +pole count left at the published {pf['pos']}: "
          f"2 x {pf['pos']}/112 = {a2o:.4f}; max still {max(a2o, a15):.4f})")
