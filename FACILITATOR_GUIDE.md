# Facilitator Guide — Jupyter & marimo Notebook Training
**NIEHS — Thursday, June 25, 2026 — 9:30 AM to 4:30 PM**

## Files in this package

| File | Purpose |
|---|---|
| `01_jupyter_morning_session.ipynb` | Morning notebook (Modules 1-5) — give this to attendees |
| `02_marimo_afternoon_session.py` | Afternoon notebook, marimo format — give this to attendees |
| `biomarker_data.csv` | Shared dataset used by both sessions (N=200) |
| `01_jupyter_morning_session_SOLUTIONS.ipynb` | Morning notebook with all exercises filled in (your answer key) |
| `02_marimo_afternoon_session_SOLUTIONS.py` | Afternoon notebook with Exercises 4.1, 5.1, and 6.1 filled in |

All three "live" files (`01_...ipynb`, `02_...py`, and `biomarker_data.csv`)
should sit **in the same folder** on whatever environment attendees use —
both notebooks load the CSV via a relative path (`"biomarker_data.csv"`).

**Keep the `_SOLUTIONS` and `_INSTRUCTOR_executed` files out of the folder
attendees can browse** — they're for your prep/reference only.

## Dataset

`biomarker_data.csv` is a Python re-implementation (numpy, seed 42, N=200)
of the `biomarker_data` dataset from your R Markdown/Quarto NIEHS workshop —
same columns and "story" (`participant_id`, `age`, `sex`, `pfoa_serum`,
`cholesterol`, `site` ∈ {Research Triangle Park, Durham, Chapel Hill}).
Values will differ from the R version (different RNG), but the dataset
serves the same narrative role and gives the day continuity with prior NIEHS
trainings.

---

## Platform setup — do this *before* Thursday

You mentioned the choice between (a) the marimo-jupyter-extension on your
existing TLJH/AWS hub, or (b) molab. With June 25 as the date, you have time
to test (a) and fall back to (b) if needed.

### Option A (recommended): marimo-jupyter-extension on TLJH

On the TLJH host:

```bash
sudo /opt/tljh/user/bin/pip install 'marimo[sandbox]>=0.23.9' \
    marimo-jupyter-extension duckdb sqlglot pandas matplotlib pytest
```

This installs into TLJH's shared user environment, so it should be available
to all attendees without per-user setup. After installing, restart each
running user server (or have attendees use **File → Hub Control Panel →
Stop My Server**, then start again) so the new packages and the JupyterLab
extension are picked up.

**One config decision worth testing ahead of time:** the extension defaults
to launching marimo via `uvx` "sandbox" mode, which creates an isolated
environment per notebook (and may try to download packages on first launch —
risky on conference wifi). For a workshop where everyone shares one
pre-built environment, it's likely simpler to disable sandboxing in
`jupyterhub_config.py`:

```python
c.MarimoProxyConfig.no_sandbox = True
```

then restart JupyterHub. With this set, marimo runs directly in the same
environment as JupyterLab — the `pandas`/`matplotlib`/`duckdb`/`sqlglot`
packages you installed above will be available to `02_marimo_afternoon_session.py`
with no extra prompts.

**Test it end-to-end** with a throwaway user account: log in, confirm the
marimo icon appears in the JupyterLab launcher, open
`02_marimo_afternoon_session.py` in marimo, and confirm it runs without
errors (it was validated locally with `marimo export html` and runs clean).

### Option B (fallback): molab

If Option A doesn't check out in time, [molab.marimo.io](https://molab.marimo.io)
is free, zero-install, cloud-hosted marimo (browser only). You'd need to:

1. Upload `02_marimo_afternoon_session.py` and `biomarker_data.csv` to a
   notebook on molab (or push them to a small GitHub repo and use
   `molab.marimo.io/github` to open from there — molab can mirror from
   GitHub).
2. Have attendees open the shared/forked notebook link. Note: molab
   notebooks are *public but undiscoverable* — fine for this synthetic
   dataset, just worth knowing.
3. This is a second login/platform for the afternoon (vs. one platform all
   day with Option A) — minor context-switch cost, but zero install risk.

Either way, **do a full dry run of the afternoon notebook** on whichever
platform you choose before Thursday — the exercises (Module 3's reactivity
demo especially) depend on the audience being able to edit and re-save the
file.

---

## Delivery notes

- **The two halves are parallel intro trainings, not a "migrate from Jupyter
  to marimo" arc.** A participant should leave able to use *either* tool well
  and pick the right one for a task. Teach each tool positively, on its own
  terms. The morning is a complete intro to Jupyter; the afternoon a complete
  intro to marimo.
- **The execution-model contrast is the key teaching thread, and it's
  factual, not evaluative.** Jupyter: *you* choose run order (great for
  exploration); marimo: the dependency graph chooses it (great for staying in
  sync). Present both as legitimate designs. Avoid framing Jupyter's model as
  a "trap" or marimo's as "the fix" — that's the tone we deliberately moved
  away from.
- **The morning's execution-order demo (Module 3, Cell A/B) is the most
  important hands-on moment of the morning.** Slow down here — have people
  actually do the change-Cell-A-don't-rerun-Cell-B-look-at-the-output
  sequence themselves. The lesson is "a cell's output is a snapshot from when
  it last ran, and Restart & Run All keeps the document and kernel in sync" —
  a core part of understanding how Jupyter works, taught as a feature of the
  model, not a defect.
- **Module 1 of the afternoon (the `MultipleDefinitionError` discussion) is
  intentionally *described*, not triggered live** — the notebook is built to
  run clean end-to-end. If you want to *show* the actual error message live,
  you can briefly type a duplicate `df = ...` cell into a scratch copy,
  trigger the error on the projector, then delete it — don't do this in the
  master copy attendees will use.
- **`marimo convert` is framed as practical interop** (open one of the
  millions of existing `.ipynb` files from GitHub in marimo), not as a
  migration mandate. Keep that framing if asked about it.
- **Mixed skill levels:** the Exercise cells (3.1/3.2 in the morning, 2.1/
  4.1/5.1/6.1 in the afternoon) are designed so faster participants can extend
  them (e.g., Exercise 4.1's optional cholesterol-threshold + reference-line
  task) while others complete the core step. Consider pairing.
- **Timing buffer:** the module times sum to roughly 6.5 hours of content
  across 7 hours scheduled (incl. lunch and two breaks) — there's little
  slack. If Module 3 (morning) or the SQL module (afternoon) run long,
  Module 7 (afternoon recap) is the easiest to compress to 10 minutes.

---

## Pre-flight checklist (do by ~June 22)

- [ ] Regenerate or confirm `biomarker_data.csv` is present alongside both
      notebooks
- [ ] Decide Option A vs. B for the afternoon platform; install/test
      accordingly
- [ ] Full Restart & Run All on `01_jupyter_morning_session.ipynb` on the
      actual delivery platform (TLJH)
- [ ] Full run of `02_marimo_afternoon_session.py` on the actual delivery
      platform — confirm `mo.ui`, matplotlib figures, the SQL cells
      (needs `duckdb` + `sqlglot`), and the unit test cells (needs `pytest`)
      all render and pass
- [ ] Spot-check that attendee accounts have write access to the folder
      (Exercises require editing and saving)
