"""PROPOSAL-m Q-F3 -- the F3 package (v1.11 §2.2 m:174, §2.6 m:265, §3.2 m:288-298, §8 step 19
m:361; ADDENDUM-m1 v0.1 decision (10') and §4 step 5; the design seat's prebuild answers of
2026-11-06, Q1 (C2)).

A sibling of ``valence_core.m``. It imports that package's shared modules UNCHANGED, by import and
never by copy, and adds what Q-F3 needs and the m package refuses: its own keys, banner bytes for
the six F3 templates and the reasoning block, scaffold (F2 block order; the reasoning-line seed
before each menu order, m:159), runner (the reasoning block and the reasoning-line classes, m:174,
m:265), verifier (G-VER, m:284), read rules (m:263, m:271, m:318), bar table (m:271, m:293, m:297,
m:316, m:330), stage drivers, G-SHAPE-F3 (m:290), resume identity carrying the reasoning-line cap
(m:174, m:267) and the cached-path source guard (m:267), plus Q-F3's schedules under
``data/mf3/schedules/`` with their own manifest.

THE LICENCE (Q1 (C2)). LOCK-m-F3 v0.1 names (a) this package's own ``package_sha256``, computed as
``valence_core.m.resume.package_sha256_of`` computes m's (every ``*.py`` directly in the package),
and (b) the file sha256 of each ``valence_core.m`` module this package imports, listed by name
(``guard.M_MODULES``, with the package's own ``__init__.py``: ``guard.M_HASHED``). Every non-stub
stage checks both at start (``stages.licence_problems``).
The package imports neither ``valence_core.m.stages`` nor ``valence_core.m.gshape`` (nor gcal,
either runner, verify or testing): ``guard.import_problems`` asserts it statically and in a fresh
interpreter.

Nothing here prints except through ``readrule.session_line`` / ``readrule.printed_reason`` and the
stage drivers' declared lines (m:263, m:318).
"""
