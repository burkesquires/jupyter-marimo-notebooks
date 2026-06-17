# Facilitator Guide — Jupyter & marimo Notebook Training
**NIEHS — Thursday, June 25, 2026 — 9:30 AM to 4:30 PM**

## Files in this package

| File | Purpose |
|---|---|
| `01_jupyter_morning_session.ipynb` | Morning notebook (Modules 1-5) |
| `02_marimo_afternoon_session.py` | Afternoon notebook, marimo format |
| `biomarker_data.csv` | Shared dataset used by both sessions (N=200) |
| `generate_dataset.py` | Regenerates `biomarker_data.csv` if needed |
| `01_jupyter_morning_session_INSTRUCTOR_executed.ipynb` | Morning notebook, pre-run, for your reference / answer key |
| `01_jupyter_morning_session_SOLUTIONS.ipynb` | Morning notebook with Exercises 2.1/3.1/3.2 filled in |
| `02_marimo_afternoon_session_SOLUTIONS.py` | Afternoon notebook with Exercises 4.1/5.1 filled in |

All four "live" files (`01_...ipynb`, `02_...py`, `biomarker_data.csv`, and
ideally a copy of the instructor `.ipynb`) should sit **in the same folder**
on whatever environment attendees use — both notebooks load the CSV via a
relative path (`"biomarker_data.csv"`).

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
    marimo-jupyter-extension duckdb sqlglot pandas matplotlib
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

- **The morning's "hidden state" demo (Module 3) is the linchpin of the
  whole day.** Everything in the afternoon refers back to it ("recall Cell
  A/B..."). Slow down here — have people actually do the
  change-Cell-A-don't-rerun-Cell-B-look-at-the-output sequence themselves,
  not just watch you do it.
- **Module 1 of the afternoon (the `MultipleDefinitionError` discussion) is
  intentionally *described*, not triggered live** — the notebook is built to
  run clean end-to-end. If you want to *show* the actual error message live,
  you can briefly type a duplicate `df = ...` cell into a scratch copy,
  trigger the error on the projector, then delete it — don't do this in the
  master copy attendees will use.
- **Mixed skill levels:** the Exercise cells (3.1/3.2 in the morning, 2.1/
  4.1/5.1 in the afternoon) are designed so faster participants can extend
  them (e.g., Exercise 4.1's optional cholesterol-threshold + reference-line
  task) while others complete the core step. Consider pairing.
- **Timing buffer:** the module times sum to exactly 6.5 hours of content
  across 7 hours scheduled (incl. lunch and two breaks) — there's effectively
  no slack. If Module 3 (morning) or the SQL module (afternoon) run long,
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
      platform — confirm `mo.ui`, matplotlib figures, and the SQL cells
      (needs `duckdb` + `sqlglot`) all render
- [ ] Spot-check that attendee accounts have write access to the folder
      (Exercises require editing and saving)
