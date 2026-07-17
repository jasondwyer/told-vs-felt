# Sanity check: currency/boot prompt (2026-07-16)

Lens: `jlens-qwen36/data/lens/lens.npz` (v0.2-fulldepth release, 20 prompts, 63 layers)
Interface: jlens-qwen36 web UI (http://127.0.0.1:8765), manual single-turn chat.

## Prompt

```
Fact: The currency used in the country shaped like a boot is the
```

## Model response (full)

```
The country shaped like a boot is **Italy**.

The currency currently used in Italy is the **Euro** (€).

*(Note: Before adopting the Euro in 2002, Italy used the Italian Lira.)*
```

## J-lens grid, qualitative read (position x layer, top-1 token per cell)

- At the position predicting the boot-shaped country: **"Italy"** is the top J-lens
  token across a wide band of middle-to-late layers (~L32 onward), well before the
  model's own text reaches that word.
- At the position predicting the currency: **"Euro" / "euro" / "€"** dominate
  middle-late layers at the same position.
- Notably, **"Lira"** also appears in the readout at this position (deep layers,
  ~L60-63) — foreshadowing the model's own later parenthetical about the historical
  Italian Lira, which was not prompted for.

Full grid text was captured via browser `get_page_text` during the session; not
saved verbatim to disk (UI-rendered, not a script log). Reproducible by re-running
the same prompt against the same lens through the web UI.
