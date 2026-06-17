"""
Build 01_jupyter_morning_session.ipynb using nbformat.

Mixed-skill-level audience, NIEHS, 9:30-12:00.
Focus: mechanics of the notebook tool itself (cells, kernel, execution
order, hidden state, hygiene), using the shared biomarker_data.csv as the
running example. Statistics are intentionally minimal.
"""

import nbformat as nbf

nb = nbf.v4.new_notebook()
cells = []

md = nbf.v4.new_markdown_cell
code = nbf.v4.new_code_cell

# ---------------------------------------------------------------------------
# Title / front matter
# ---------------------------------------------------------------------------
cells.append(md(r"""# Jupyter Notebooks for Scientific Computing
### NIEHS Notebook Training — Morning Session (9:30 - 12:00)

**Today's plan**

| Time | Module |
|---|---|
| 9:30 - 10:00 | Module 1: Tour of the Notebook |
| 10:00 - 10:20 | Module 2: Markdown & Narrative |
| 10:20 - 10:35 | *Break* |
| 10:35 - 11:15 | Module 3: Loading & Exploring Data |
| 11:15 - 11:45 | Module 4: Notebook Hygiene & Reproducibility |
| 11:45 - 12:00 | Module 5: Looking Ahead to marimo |
| 12:00 - 1:00 | *Lunch* |

**Goal of the morning:** get comfortable with *how a Jupyter notebook works* —
cells, the kernel, execution order, and the habits that keep a notebook
reproducible. We'll use a small simulated NIEHS biomarker dataset
(`biomarker_data.csv`) as our running example, but the focus today is the
**tool**, not the statistics.

> **How to use this notebook:** Run cells with `Shift+Enter`. Cells marked
> **Exercise** are for you to try — pause and work through them before
> moving on. There are no wrong answers; the point is to *notice what
> happens*.
"""))

# ---------------------------------------------------------------------------
# Module 1
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## Module 1: Tour of the Notebook (30 min)

A Jupyter notebook is a sequence of **cells**. Each cell is either:

- a **code cell** (runs Python, in this notebook), or
- a **markdown cell** (formatted text, like this one)

Behind every notebook is a **kernel** — a running Python process that holds
all your variables in memory. The notebook file itself is just a record of
cells and their *last* outputs; the kernel is where the *actual* program
state lives.

Let's start the kernel by running the cell below.
"""))

cells.append(code(r"""print("Hello, NIEHS!")"""))

cells.append(md(r"""Notice the `In [1]` / `Out[1]` (or just `[1]`) to the left of the cell.
That number is the **execution count** — it tells you the *order in which
cells were run*, not their position in the notebook.

Two modes you'll move between constantly:

- **Edit mode** (green border, cursor in the cell) — type code/text
- **Command mode** (blue border, click to the left of a cell or press `Esc`) — keyboard shortcuts act on the cell itself

| Shortcut | Action |
|---|---|
| `Shift + Enter` | Run cell, move to next |
| `Ctrl + Enter` | Run cell, stay put |
| `Esc` then `A` | Insert cell **a**bove |
| `Esc` then `B` | Insert cell **b**elow |
| `Esc` then `D D` | **D**elete cell (press D twice) |
| `Esc` then `M` | Convert cell to **m**arkdown |
| `Esc` then `Y` | Convert cell to code |

Try it: click this cell, press `Esc`, then `B`, then `Shift+Enter` on the new
empty cell below to create and run a blank code cell."""))

cells.append(code(r"""# scratch cell - try the shortcuts above on this one
"""))

cells.append(md(r"""### Exercise 1.1 — Execution order vs. cell position

Run the next two cells **in order** (`x = 10`, then the `print` cell)."""))

cells.append(code(r"""x = 10"""))

cells.append(code(r"""y = x * 2
print(f"y = {y}")"""))

cells.append(md(r"""Now: **go back to the `x = 10` cell, change it to `x = 100`, and run *only
that cell*.** Don't touch the `y = x * 2` cell.

- What does `y` equal right now, in the kernel's memory?
- What if you scroll up — does the *displayed output* of the `y` cell change?
- What has to happen for `y` to actually become `200`?

Discuss with a neighbor, then re-run the `y` cell to check your answer."""))

cells.append(md(r"""**Key idea:** the notebook *document* (what you see) and the kernel's
*state* (what Python actually has in memory) can get out of sync. The
execution-count numbers are your only clue about what's actually happened,
in what order. This will matter a lot in Module 3."""))

# ---------------------------------------------------------------------------
# Module 2
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## Module 2: Markdown & Narrative (20 min)

Markdown cells are how a notebook becomes a **computational narrative** —
code *and* the reasoning around it, in one document. The cell you're reading
right now is markdown.

Common syntax:

```
# Header 1
## Header 2
**bold**, *italic*, `inline code`

- bullet
- list

1. numbered
2. list

[a link](https://example.com)
```

Markdown cells also render **LaTeX math**, using `$...$` for inline math and
`$$...$$` for a centered equation on its own line. For example, body mass
index:

$$ BMI = \frac{\text{weight}_{kg}}{\text{height}_m^2} $$

is written as `$$ BMI = \frac{\text{weight}_{kg}}{\text{height}_m^2} $$`."""))

cells.append(md(r"""### Exercise 2.1 — Write your own markdown cell

Double-click this cell to edit it, then below it create a **new markdown
cell** (`Esc` then `B`, then `Esc` then `M`) and write a short note that:

1. Has a header
2. Has a bulleted list of 2-3 things you hope to get out of today
3. Includes *one* equation of your choosing (it can be silly — e.g.
   $E = mc^2$, or make one up)

Run the cell (`Shift+Enter`) to render it."""))

cells.append(md(r"""*(your Exercise 2.1 cell goes here)*"""))

cells.append(md(r"""**Why this matters:** a notebook that mixes narrative and code lets you
(and others, including future-you) follow *why* an analysis was done a
certain way — not just *what* the code does. We'll come back to this idea
of "the notebook as a record of reasoning" all day."""))

# ---------------------------------------------------------------------------
# BREAK
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## ☕ Break (10:20 - 10:35)
"""))

# ---------------------------------------------------------------------------
# Module 3
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## Module 3: Loading & Exploring Data (40 min)

We'll use a small simulated dataset, `biomarker_data.csv` — 200 participants
with age, sex, site, serum PFOA, and total cholesterol. (This is the same
dataset used in the afternoon marimo session, and the same one from prior
NIEHS R/Quarto trainings, just regenerated in Python.)

Run the cells below in order."""))

cells.append(code(r"""import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("biomarker_data.csv")
df.head()"""))

cells.append(code(r"""df.info()"""))

cells.append(code(r"""df.describe()"""))

cells.append(md(r"""### Exercise 3.1 — A quick filter

In the empty cell below, write code to:

1. Filter `df` to only rows where `site == "Durham"`
2. Compute the mean `pfoa_serum` for that subset

(Hint: `df[df["site"] == "Durham"]["pfoa_serum"].mean()`)"""))

cells.append(code(r"""# Your code here
"""))

cells.append(code(r"""fig, ax = plt.subplots()
ax.hist(df["pfoa_serum"], bins=20)
ax.set_xlabel("Serum PFOA (ng/mL)")
ax.set_ylabel("Count")
ax.set_title("Distribution of serum PFOA")
plt.show()"""))

cells.append(md(r"""### The "hidden state" trap

This is the most important idea of the morning. Run the next three cells
**in order**."""))

cells.append(code(r"""# Cell A
older = df[df["age"] > 50]
print(f"{len(older)} participants over 50")"""))

cells.append(code(r"""# Cell B
mean_chol_older = older["cholesterol"].mean()
print(f"Mean cholesterol (age > 50): {mean_chol_older:.1f}")"""))

cells.append(md(r"""Now do this, **carefully, one step at a time**:

1. Scroll up to **Cell A** and change `age > 50` to `age > 60`.
2. Run **only Cell A** (`Ctrl+Enter`, so you stay on it). Don't touch Cell B
   yet.
3. Look at Cell B's output. Has it changed?
4. Now run Cell B.
5. Now, **Restart the kernel** (Kernel menu → Restart) but *don't* run any
   cells. Look at Cell B's output again — is it still showing a number?

Talk through with a neighbor: at each step, what does Cell B's *displayed
output* actually represent — the current data, or a snapshot from whenever
it last ran?"""))

cells.append(md(r"""**This is the core hazard of notebooks:** outputs on screen can be
*stale* — leftover from a previous run, computed against data or code that
no longer exists in that form. A notebook can *look* internally consistent
and be completely wrong, because nothing forces cells to stay in sync with
each other.

This isn't a Jupyter bug — it's a direct consequence of cells being
independently runnable in any order. Keep this example in mind; we'll
revisit it this afternoon."""))

cells.append(md(r"""### Exercise 3.2 — Break it, then find it

1. In the empty cell below, create a new variable, e.g. `threshold = 200`.
2. In the cell *after that*, use `threshold` in some small calculation
   (e.g. `df[df["cholesterol"] > threshold]`).
3. Now **delete the cell that defines `threshold`** (`Esc`, `D`, `D`).
4. Run the remaining cell. It still works — the kernel still remembers
   `threshold`, even though no cell in the notebook defines it anymore!
5. Now: **Restart & Run All** (Kernel menu → Restart Kernel and Run All
   Cells).

What happens on step 5, and why is that actually the *more honest* result?"""))

cells.append(code(r"""# step 1: define threshold here
"""))

cells.append(code(r"""# step 2: use threshold here
"""))

# ---------------------------------------------------------------------------
# Module 4
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## Module 4: Notebook Hygiene & Reproducibility (30 min)

A few habits that prevent the problems from Module 3:

1. **Restart & Run All before you trust a result, share a notebook, or end
   a session.** This is the closest thing notebooks have to "does this
   actually work?" If it doesn't run top-to-bottom cleanly, it's not done.
2. **Write cells to run top-to-bottom, in the order they appear.** If a
   later cell depends on an earlier one, that dependency should be visible
   *in the document*, not just in kernel memory.
3. **Avoid silently overwriting the same variable name many times** (e.g.
   `df = df[...]` repeated across many cells). Each reassignment makes
   "which version of `df` am I looking at?" harder to answer. Prefer new
   names for meaningfully different subsets: `df_durham`, `df_older`, etc.
4. **Clear outputs before committing to version control** (Edit →
   Clear Outputs, or `nbstripout` if you use git). Stale outputs in a shared
   `.ipynb` are a common source of confusion.
5. **Save / export** — `File → Save and Checkpoint`, and `File → Download
   as` (or `jupyter nbconvert`) to get `.py`, `.html`, or `.pdf` versions."""))

cells.append(md(r"""### Exercise 4.1 — The gold-standard test

1. If Exercise 3.2 left your notebook in a broken state (a `NameError`),
   that's expected — *fix it now* by re-adding a definition for `threshold`
   in a sensible place (before it's used).
2. Once it's fixed, run **Restart Kernel and Run All Cells** one more time.
3. Confirm: does the notebook run from top to bottom with no errors?

This "Restart & Run All, no errors" check is something you should be able to
do with *every* notebook before walking away from it."""))

# ---------------------------------------------------------------------------
# Module 5
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## Module 5: Looking Ahead (15 min)

Let's name the pain points from this morning:

- **Execution order is invisible** — the document doesn't show you the
  *order* cells actually ran in, only the *last* order.
- **State can outlive its source** — delete or change the cell that created
  a variable, and the kernel may still remember the old value.
- **Outputs can be stale** — what's on screen may not reflect the current
  code or data at all.
- **Discipline is the only fix** — Restart & Run All works, but it relies on
  *you* remembering to do it.

This afternoon, we'll look at **marimo**, a notebook tool that takes a
different approach: it builds a dependency graph of your cells and
*automatically* re-runs whatever depends on what changed — and it won't even
let you define the same variable in two cells.

We'll revisit `biomarker_data.csv` and rebuild parts of what we did this
morning, so you can feel the difference directly.

**See you back here at 1:00 with this notebook in a working
(Restart & Run All clean!) state.**"""))

nb["cells"] = cells

with open("01_jupyter_morning_session.ipynb", "w") as f:
    nbf.write(nb, f)

print(f"Wrote {len(cells)} cells to 01_jupyter_morning_session.ipynb")
