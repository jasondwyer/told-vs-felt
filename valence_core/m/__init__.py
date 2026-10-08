"""PROPOSAL-m — the gating campaign's package (v1.11, committed at 05c4636).

Step 4 of §8 builds the Q-F0 subset: the F0m runner (Qwen) and the F0m-OLMo
runner, the CORR delivery module, ``corrupt_m``, the F0m and F0m-OLMo
verifiers, Q-F0's and the OLMo units' schedules and gate files, the audit
wrapper's task-round classes, the source guard, the resume-identity machinery
and the read-rule tooling of §3. Nothing of Q-F3 is built before step 19
except the shared modules (§0.7, m:54).

Modules: ``keys`` (streams, seeds), ``corr`` (CORR delivery, ``corrupt_m``,
f1's corruptor for G-PORT/G-CAL), ``banner`` (§2.5's lines), ``schedule``
(campaign and gate-stage schedules), ``bars`` (exact bars, P <= alpha),
``audit`` (task-round claim classes), ``guard`` (insulation, cached-path
licence, call-site check), ``resume`` (identity, atomic checkpoints),
``readrule`` (§3's stripping, redaction, printing), ``scaffold`` (one session
code path for runner, verifier and G-PORT), ``runner_qwen``, ``runner_olmo``,
``verify``, ``stages``; step 6 adds ``gcal`` (G-CAL: the model-free artifact, the
seat's read request, completability on Qwen). Driver and self-test:
``scripts/m_sessions.py``.

No module here imports steering machinery; ``guard.assert_insulated`` asserts
the quarantined state-present module absent at startup and before every read.
"""
