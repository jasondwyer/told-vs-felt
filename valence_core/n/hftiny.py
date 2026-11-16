"""PROPOSAL-n -- the HF backend's self-test on a tiny OLMo-2 built from a config (SELFTEST-ONLY; box site check).

No weights are downloaded or read: ``Olmo2ForCausalLM(Olmo2Config(...))`` with four layers, width 64, seeded random
initialization, float32 on the CPU. The adapter is ``OLMoHFAdapter`` itself, unchanged, constructed without its
``__init__`` (which loads a checkpoint by path) and given the tiny model; ``HFBackend`` then runs through the adapter's
own ``_make_hooks``. Skipped where torch or transformers is absent (the laptop); it runs in the post-build site check
on the box.

What it checks (float32 on the CPU: every comparison within 1e-4, the deviation recorded, since a kept-last-logits
forward and a full one need not agree bit for bit -- but for the site check, two prefills of one kind, exact):
  * the prefill's read-position logits and captures equal the adapter's own ``forward`` (no injection), and with an
    injection on declared spans (both through the adapter's hooks);
  * the cached continuation's rows equal the full forward's rows for the same label, unsteered and under the same
    injection (the fresh path runs under the identical mask);
  * the cache is cropped back to the prefill's length after each label;
  * an injection on earlier spans moves the read position's logits;
  * the band's premise (ADDENDUM-n1 §6.2; ledger (77)) on the HF path: at the site (layer 1) the steered prefill's
    read-position residual is the unsteered one's exactly, and one layer past it (layer 2) it differs (> 1e-3);
  * the primitive's ``read`` gives a shadow and a steered read paired with it, both accepted by
    ``schema.check_record``, the steered read's re-computation below TAU.
"""
from __future__ import annotations

import numpy as np


def available() -> bool:
    try:
        import torch  # noqa: F401
        import transformers  # noqa: F401
    except Exception:                                    # noqa: BLE001
        return False
    return True


def tiny_adapter(n_layers: int = 4, width: int = 64, vocab: int = 128, seed: int = 20261115):
    import torch
    from transformers import Olmo2Config, Olmo2ForCausalLM

    from ..adapters.olmo_hf import OLMoHFAdapter
    torch.manual_seed(seed)
    cfg = Olmo2Config(vocab_size=vocab, hidden_size=width, intermediate_size=2 * width,
                      num_hidden_layers=n_layers, num_attention_heads=4, num_key_value_heads=2,
                      max_position_embeddings=512)
    model = Olmo2ForCausalLM(cfg).eval()
    a = object.__new__(OLMoHFAdapter)
    a._torch, a.path, a.device, a.dtype_name = torch, "tiny-olmo2-config", "cpu", "float32"
    a.seed, a.deterministic, a._tok, a._model = seed, False, None, model
    a.choice_window, a._layers, a._n_layers = 512, model.model.layers, n_layers
    return a


def run(chk) -> None:
    """``chk(name, ok, detail)`` per check."""
    if not available():
        chk("hftiny: skipped (no torch/transformers here; runs on the box)", True, "")
        return
    from ..adapters.base import Injection, PositionSpec
    from . import primitive, schema
    from .testing import toy_session
    a = tiny_adapter()
    be = primitive.HFBackend(a)
    s, ids = toy_session(3, turn_len=9, tail=5, vocab=128)
    n = len(ids)
    layers = [2, 3]                                   # the band past the site (injection at 1 of 4; ADDENDUM-n1 §6.2)
    def dev(x, y) -> float:
        return float(np.max(np.abs(np.asarray(x, np.float64) - np.asarray(y, np.float64))))
    pre = be.prefill(ids, (), layers)
    ref = a.forward(ids, capture_layers=layers)
    d0 = dev(pre.logits_last, ref.logits)
    chk("hftiny: prefill logits == adapter.forward logits (no injection; tol 1e-4)", d0 <= 1e-4, d0)
    dc = max(dev(pre.captures[l], ref.acts[l][n - 1]) for l in layers)
    chk("hftiny: prefill captures == adapter.forward captures at the read position (tol 1e-4)", dc <= 1e-4, dc)
    label = [5, 9, 17]
    cont = be.continue_label(pre, label)
    rows_f, _ = be.full(ids, label, (), layers)
    d1 = dev(np.vstack([pre.logits_last[None], cont]), rows_f)
    chk("hftiny: cached continuation rows == full forward rows (tol 1e-4)", d1 <= 1e-4, d1)
    cache, n0 = pre.handle
    chk("hftiny: the cache is cropped back to the prefill's length", cache.get_seq_length() == n0 == n,
        cache.get_seq_length())
    u = np.random.default_rng(1).standard_normal(64)
    spans = [(a0, b0) for a0, b0, z in s.turn_spans if z == s.cue_S]
    inj = Injection(u=u, layer=1, alpha=4.0, positions=PositionSpec.spans(*spans))
    pre_i = be.prefill(ids, [inj], layers)
    ref_i = a.forward(ids, capture_layers=layers, injections=[inj])
    d2 = dev(pre_i.logits_last, ref_i.logits)
    chk("hftiny: steered prefill == adapter.forward with the same injection (tol 1e-4)", d2 <= 1e-4, d2)
    d3 = dev(pre_i.logits_last, pre.logits_last)
    chk("hftiny: the injection on earlier spans moves the read position's logits", d3 > 1e-3, d3)
    cont_i = be.continue_label(pre_i, label)
    rows_fi, _ = be.full(ids, label, [inj], layers)
    d4 = dev(np.vstack([pre_i.logits_last[None], cont_i]), rows_fi)
    chk("hftiny: steered: cached continuation rows == the full forward's under the same injection (tol 1e-4)",
        d4 <= 1e-4, d4)
    site_st, site_sh = be.prefill(ids, [inj], [1, 2]), be.prefill(ids, (), [1, 2])     # the site is 1
    at_site = bool(np.array_equal(site_st.captures[1], site_sh.captures[1]))
    past_site = dev(site_st.captures[2], site_sh.captures[2])
    chk("hftiny: AT THE SITE (layer 1) the steered prefill's read-position residual is the unsteered one's exactly, "
        "and past it (layer 2) it differs (> 1e-3): the band's premise on the HF path (ADDENDUM-n1 §6.2)",
        at_site and past_site > 1e-3, (at_site, past_site))
    ident, dirs = primitive.test_identity(u, layer=1, n_layers=4, d_model=64)
    ident = dict(ident, identity_bound=1e-3)
    LS, LU = [5, 9, 17], [5, 11, 2]
    sh_spec = primitive.ReadSpec("N1-V", "none", "0", 0.0, None)
    shadow, _caps = primitive.read(be, s, ids, s.ids_sha, sh_spec, LS, LU, layers, fidelity_reason="dose-rule",
                                   shadow=None, identity_bound=1e-3, launch_index=0, capture_row=0)
    value = schema.dose_point_values(ident)["+1"]
    st_spec = primitive.ReadSpec("N1-V", "valence", "+1", value,
                                 Injection(u=dirs["valence"], layer=1,
                                           alpha=schema.expected_alpha("+1", value, ident["dose_map"])))
    steered, _caps2 = primitive.read(be, s, ids, s.ids_sha, st_spec, LS, LU, layers, fidelity_reason="dose-rule",
                                     shadow=shadow, identity_bound=1e-3, launch_index=1, capture_row=0)
    for name, rec in (("the shadow", shadow), ("a steered read", steered)):
        try:
            schema.check_record(rec, ident)
            ok, detail = True, ""
        except schema.SchemaError as e:
            ok, detail = False, str(e)
        chk(f"hftiny: {name}'s record passes check_record", ok, detail)
    chk("hftiny: the steered read's re-computation agrees with its cached read (below TAU)",
        steered["fidelity"] is not None and steered["fidelity"]["exceeds_tau"] is False,
        None if steered["fidelity"] is None else steered["fidelity"]["rel"])
    chk("hftiny: the steered read moves the margin from its shadow's", steered["margin"] != shadow["margin"], "")
