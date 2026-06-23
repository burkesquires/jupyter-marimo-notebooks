"""
Build 01_jupyter_morning_session.ipynb using nbformat.

Mixed-skill-level audience, NIEHS, 9:30-12:00.
Focus: mechanics of the notebook tool itself (cells, kernel, execution
model, hygiene), using the shared biomarker_data.csv as the running example.
Statistics are intentionally minimal. Jupyter is taught on its own terms.
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
| 11:45 - 12:00 | Module 5: Wrap-Up & Where Jupyter Shines |
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

It helps to picture these as **two separate things**:

- The **document** — the `.ipynb` file on disk (or what you see in the
  browser): an ordered list of cells, plus a saved copy of each cell's most
  recent output.
- The **kernel** — a live Python process running in the background. It
  remembers every variable you've defined, every library you've imported,
  and every function you've created, regardless of where (or whether) those
  things still appear in the document.

Almost every notebook "gotcha" we'll see today comes from these two drifting
apart. Keep the distinction in your back pocket.

Let's start the kernel by running the cell below.
"""))

cells.append(code(r"""print("Hello, NIEHS!")"""))

cells.append(md(r"""Notice the `In [1]` / `Out[1]` (or just `[1]`) to the left of the cell.
That number is the **execution count** — it tells you the *order in which
cells were run*, not their position in the notebook. A few states worth
recognizing:

- `[ ]` (empty) — the cell hasn't run since the kernel started
- `[*]` — the cell is *running right now* (useful for spotting a long
  computation, or one that's hung)
- `[7]` — the cell finished, and it was the 7th cell executed in this kernel
  session

Two modes you'll move between constantly:

- **Edit mode** (green border, cursor in the cell) — type code/text
- **Command mode** (blue border, click to the left of a cell or press `Esc`) — keyboard shortcuts act on the cell itself

| Shortcut | Action |
|---|---|
| `Shift + Enter` | Run cell, move to next |
| `Ctrl + Enter` | Run cell, stay put |
| `Alt + Enter` | Run cell, insert new one below |
| `Esc` then `A` | Insert cell **a**bove |
| `Esc` then `B` | Insert cell **b**elow |
| `Esc` then `D D` | **D**elete cell (press D twice) |
| `Esc` then `M` | Convert cell to **m**arkdown |
| `Esc` then `Y` | Convert cell to code |
| `Esc` then `Z` | Undo cell delete |

Two kernel controls you'll want to know early, both in the **Kernel** menu
(and on the toolbar):

- **Interrupt** (the ■ stop button) — stops a cell that's running too long or
  stuck in a loop, without wiping your variables.
- **Restart** — kills the Python process and starts fresh: *every* variable,
  import, and function is gone. This is the big reset we'll lean on for
  reproducibility later.

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

A markdown cell has two states: **edit** (you see the raw text, with the
`#`, `*`, and `|` symbols) and **rendered** (you see the formatted result).
`Shift+Enter` renders it; double-click goes back to editing. Everything
below is the raw syntax — double-click this cell anytime to see how it's
written.

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

> a blockquote, good for callouts
```

You can also build **tables**, which are handy for small results summaries
or data dictionaries:

```
| Column | Meaning | Units |
|---|---|---|
| pfoa_serum | Serum PFOA concentration | ng/mL |
| cholesterol | Total cholesterol | mg/dL |
```

renders as:

| Column | Meaning | Units |
|---|---|---|
| pfoa_serum | Serum PFOA concentration | ng/mL |
| cholesterol | Total cholesterol | mg/dL |

Markdown cells also render **LaTeX math**, using `$...$` for inline math and
`$$...$$` for a centered equation on its own line. For example, body mass
index:

$$ BMI = \frac{\text{weight}_{kg}}{\text{height}_m^2} $$

is written as `$$ BMI = \frac{\text{weight}_{kg}}{\text{height}_m^2} $$`.

For scientific work this matters: you can write the actual formula a cell
implements right next to the code, so a reviewer can check that the code
matches the math."""))

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

The columns:

| Column | Meaning |
|---|---|
| `participant_id` | Unique ID, 1–200 |
| `age` | Age in years |
| `sex` | Female / Male |
| `pfoa_serum` | Serum PFOA concentration (ng/mL) |
| `cholesterol` | Total cholesterol (mg/dL) |
| `site` | One of three NC study sites |

A quick orientation to the three workhorse functions you'll use on almost
any new dataset:

- `df.head()` — peek at the first few rows (is the data shaped the way you
  expect?)
- `df.info()` — column names, data types, and non-null counts (did anything
  import as the wrong type, or have missing values?)
- `df.describe()` — summary statistics for numeric columns (do the ranges
  look sane?)

Run the cells below in order."""))

cells.append(code(r"""import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("biomarker_data.csv")
df.head()"""))

cells.append(code(r"""df.info()"""))

cells.append(code(r"""df.describe()"""))

cells.append(md(r"""`describe()` only covers numeric columns. For categorical columns like
`site` and `sex`, `value_counts()` is the equivalent — it tells you the
categories and how many rows fall in each:"""))

cells.append(code(r"""df["site"].value_counts()"""))

cells.append(md(r"""And a very common first analysis step: a **grouped summary** — split the
data by a category, then summarize each group. Here, mean PFOA and
cholesterol per site:"""))

cells.append(code(r"""df.groupby("site")[["pfoa_serum", "cholesterol"]].mean()"""))

cells.append(md(r"""### Exercise 3.1 — A quick filter (two ways)

So far we've selected rows with **boolean indexing** — `df[df["site"] ==
"Durham"]`. Read it inside-out: `df["site"] == "Durham"` produces a column
of `True`/`False`, one per row, and `df[...]` keeps only the `True` rows.
It's powerful but the doubled `df[df[...]]` can be hard to read.

pandas offers a second style, **`.query()`**, that takes a condition as a
string and reads much more like plain English (or SQL — which is exactly
what you'll meet in the afternoon marimo session):

```python
df.query("site == 'Durham'")          # same result as df[df["site"] == "Durham"]
df.query("age > 50 and sex == 'Male'")  # conditions chain naturally
```

A few things to notice about `.query()`:

- Column names are written **bare** (`site`, not `df["site"]`).
- String *values* still need quotes — and since the whole condition is
  already in double quotes, use single quotes inside (`'Durham'`).
- Combine conditions with `and` / `or` (not `&` / `|` as in boolean
  indexing).

**Your task** — in the empty cell below, using **`.query()`**:

1. Select only rows where `site == "Durham"`
2. From that result, compute the mean `pfoa_serum`

(Hint: `df.query("site == 'Durham'")["pfoa_serum"].mean()`)

If you finish early: write the *same* filter the boolean-indexing way
(`df[df["site"] == "Durham"]...`) and confirm the two numbers match. They
should — `.query()` is a more readable spelling of the same operation, not a
different result. Two paths to one answer is a good habit for catching
mistakes."""))

cells.append(code(r"""# Your code here
"""))

cells.append(code(r"""fig, ax = plt.subplots()
ax.hist(df["pfoa_serum"], bins=20)
ax.set_xlabel("Serum PFOA (ng/mL)")
ax.set_ylabel("Count")
ax.set_title("Distribution of serum PFOA")
plt.show()"""))

cells.append(md(r"""### Understanding execution order and cell outputs

This is the most important idea of the morning — the heart of how Jupyter's
execution model works. Run the next three cells **in order**."""))

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

cells.append(md(r"""**Here's what this teaches about Jupyter's model:** a cell's output is a
**snapshot from the last time that cell ran**, not a live mirror of the
current state. Jupyter gives you full manual control over execution — *you*
decide which cell runs and when — and that control is exactly what makes
notebooks so good for iterative, exploratory work. The flip side of that
control is that you're the one keeping track of what's run.

To make the answer explicit: after step 2, Cell B's output still showed the
*old* mean — computed from the `age > 50` version of `older`, even though
Cell A now defines `older` as `age > 60`. Cell B simply hadn't been re-run
yet. Re-running Cell B (step 4) brought it up to date. And after a kernel
restart (step 5), the *output text remains visible in the document* even
though the kernel no longer has `older` defined — a nice illustration of the
two-things model from Module 1: the document (what you see) and the kernel
(the live program) are distinct.

This is a direct, logical consequence of cells being independently runnable
in any order — the same property that makes Jupyter flexible. The next module
covers the simple, reliable habit that keeps the document and kernel in
sync: **Restart & Run All**."""))

cells.append(md(r"""### Exercise 3.2 — Explore the document/kernel distinction

This exercise makes the two-things model from Module 1 concrete and
hands-on.

1. In the empty cell below, create a new variable, e.g. `threshold = 200`.
2. In the cell *after that*, use `threshold` in some small calculation
   (e.g. `df[df["cholesterol"] > threshold]`).
3. Now **delete the cell that defines `threshold`** (`Esc`, `D`, `D`).
4. Run the remaining cell. It still works — the kernel still remembers
   `threshold`, even though no cell in the notebook defines it anymore. (The
   kernel holds the live state; the document is a separate thing.)
5. Now: **Restart & Run All** (Kernel menu → Restart Kernel and Run All
   Cells).

What happens on step 5, and why is that result the one you'd actually want
to trust before sharing the notebook?"""))

cells.append(code(r"""# step 1: define threshold here
"""))

cells.append(code(r"""# step 2: use threshold here
"""))

# ---------------------------------------------------------------------------
# Module 4
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## Module 4: Notebook Hygiene & Reproducibility (30 min)

Now that you understand how Jupyter's execution model works, here are the
habits that make the most of it — the same practices experienced scientific
Python users rely on to keep their notebooks reproducible and easy to share:

1. **Restart & Run All before you trust a result, share a notebook, or end
   a session.** This is Jupyter's built-in reproducibility check — it runs
   the whole notebook top-to-bottom in a fresh kernel, exactly as a
   colleague would. If it runs cleanly start to finish, you know the
   document and the results are in sync. (R Markdown users will recognize
   this as the same idea as knitting in a clean session.)
2. **Write cells to run top-to-bottom, in the order they appear.** If a
   later cell depends on an earlier one, that dependency should be visible
   *in the document*, not just in kernel memory.
3. **Avoid silently overwriting the same variable name many times** (e.g.
   `df = df[...]` repeated across many cells). Each reassignment makes
   "which version of `df` am I looking at?" harder to answer. Prefer new
   names for meaningfully different subsets: `df_durham`, `df_older`, etc.
4. **Keep imports and file-loading near the top.** Putting `import pandas`,
   `pd.read_csv(...)`, and other setup in the first few cells means a reader
   (or future-you) can run the notebook top-to-bottom without hunting for a
   stray import buried in the middle.
5. **Use relative paths and check your working directory.** This notebook
   loads `"biomarker_data.csv"` with no folder in front of it, which works
   because the file sits in the same directory. If a load fails with
   `FileNotFoundError`, run `import os; os.getcwd()` to see where the kernel
   actually is — it's a frequent source of "it worked yesterday" confusion.
6. **Clear outputs before committing to version control** (Edit →
   Clear Outputs, or `nbstripout` if you use git). Stale outputs in a shared
   `.ipynb` are a common source of confusion.
7. **Save / export** — `File → Save and Checkpoint`, and `File → Download
   as` (or `jupyter nbconvert`) to get `.py`, `.html`, or `.pdf` versions.

The first three are about *avoiding* trouble; the rest are about making your
notebook legible to the next person who opens it — very often yourself, six
months later."""))

cells.append(md(r"""### Exercise 4.1 — The gold-standard test

1. If Exercise 3.2 left your notebook in a broken state (a `NameError`),
   that's expected — *fix it now* by re-adding a definition for `threshold`
   in a sensible place (before it's used).
2. Once it's fixed, run **Restart Kernel and Run All Cells** one more time.
3. Confirm: does the notebook run from top to bottom with no errors?

This "Restart & Run All, no errors" check is something you should be able to
do with *every* notebook before walking away from it.

If you're curious where the kernel is reading files from (hygiene habit #5),
run the cell below — it prints the kernel's current working directory, which
is the folder `pd.read_csv("biomarker_data.csv")` looked in:"""))

cells.append(code(r"""import os
print("Kernel working directory:", os.getcwd())"""))

# ---------------------------------------------------------------------------
# Module 5
# ---------------------------------------------------------------------------
cells.append(md(r"""---
## Module 5: Wrap-Up & Where Jupyter Shines (15 min)

Let's consolidate what you built this morning. You now understand Jupyter's
**execution model** — the single most important thing to internalize as a
notebook user:

- **You control execution.** Cells run when *you* run them, in whatever order
  you choose. The `In [n]` counter records that order. This manual control is
  what makes notebooks excellent for iterative, exploratory analysis — you can
  poke at data, try things, and re-run just the piece you're working on.
- **The document and the kernel are two separate things.** The kernel holds
  live state; the document holds cells and their last-saved outputs. A cell's
  output is a snapshot from when it last ran.
- **Restart & Run All keeps them in sync.** It's Jupyter's built-in
  reproducibility check, and the one habit that matters most before you trust
  or share a result.

These aren't quirks to memorize — they're a coherent model, and once it
clicks, notebooks become a powerful and predictable tool.

### Where Jupyter is the right choice

Jupyter is the most widely used notebook in scientific computing, and for
good reasons that are worth naming:

- **Ubiquity and ecosystem.** It's the de facto standard — the format your
  collaborators expect, the one Google Colab and most cloud platforms run,
  and the one with the deepest set of extensions, kernels (R, Julia, and
  100+ others), and integrations.
- **Sharing and teaching.** `.ipynb` files render directly on GitHub, in
  nbviewer, and in countless tutorials. If you want someone to *read* your
  analysis without running it, the saved outputs are right there.
- **Exploratory, throwaway work.** When you're rapidly trying ideas, full
  manual control over what runs (and when) is exactly what you want.
- **The broadest toolchain.** JupyterLab, Jupyter Notebook, Colab, VS Code,
  and many other editors all speak `.ipynb` natively.

The skills you built this morning — cells, the kernel, execution order,
markdown narrative, data exploration, and Restart & Run All — transfer to
every one of those environments.

### This afternoon: marimo

After lunch we'll learn **marimo**, a newer Python notebook with a different
execution model: instead of you choosing run order, marimo determines it
automatically from how cells depend on one another. It's a genuinely
different design with its own strengths — not a replacement for what you
learned this morning, but a second tool worth knowing. We'll use the same
`biomarker_data.csv` so you can focus on the tool rather than the data.

Both tools are worth having in your kit; by the end of the day you'll be able
to pick the right one for a given task.

**See you back here at 1:00 — and try leaving this notebook in a working
(Restart & Run All clean!) state, since that's the habit we just covered.**"""))

nb["cells"] = cells

with open("01_jupyter_morning_session.ipynb", "w") as f:
    nbf.write(nb, f)

print(f"Wrote {len(cells)} cells to 01_jupyter_morning_session.ipynb")
