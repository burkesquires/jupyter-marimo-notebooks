import marimo

__generated_with = "0.23.9"
app = marimo.App(app_title="marimo afternoon session")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def _(mo):
    mo.md(
        r"""
        # Reactive Notebooks with marimo
        ### NIEHS Notebook Training — Afternoon Session (1:00 - 4:30)

        | Time | Module |
        |---|---|
        | 1:00 - 1:20 | Module 1: What Is marimo? |
        | 1:20 - 1:50 | Module 2: marimo Basics |
        | 1:50 - 2:20 | Module 3: Rebuilding the Morning Workflow |
        | 2:20 - 2:35 | *Break* |
        | 2:35 - 3:15 | Module 4: Interactive UI |
        | 3:15 - 3:45 | Module 5: SQL Cells |
        | 3:45 - 4:10 | Module 6: Apps, Export & Conversion |
        | 4:10 - 4:30 | Module 7: Recap & Q&A |

        **Goal of the afternoon:** see how a *reactive* notebook changes the
        rules from this morning. Same dataset (`biomarker_data.csv`), same
        kinds of tasks — but a different execution model. As before, the
        focus is the **tool**, not the statistics.

        > **How to use this notebook:** marimo notebooks are plain `.py`
        > files. Cells run automatically when their inputs change — there's
        > no "run order" to manage. Editing UI elements (sliders, dropdowns)
        > re-runs whatever depends on them, instantly.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## Module 1: What Is marimo? (20 min)

        marimo is a notebook that's also a **plain Python file** (`.py`, not
        `.ipynb`/JSON). Three things follow from that:

        - It's **git-friendly** — diffs look like normal Python diffs.
        - It can be run as a **script** (`python notebook.py`), a **notebook**
          (`marimo edit notebook.py`), or an **app** (`marimo run notebook.py`)
          — same file, three modes.
        - marimo can reorder cells in the file to match the order they were
          *written* for readability, but it executes them in **dependency
          order** — the order is determined by which cells' outputs other
          cells use as inputs, not by position on the page.

        That last point is the big one. Let's see it in action.
        """
    )
    return


@app.cell
def _(mo):
    count = mo.ui.slider(1, 20, value=5, step=1, label="Pick a number")
    count
    return (count,)


@app.cell
def _(count, mo):
    doubled = count.value * 2
    mo.md(f"Doubled, automatically, every time you move the slider: **{doubled}**")
    return (doubled,)


@app.cell
def _(mo):
    mo.md(
        r"""
        Drag the slider above. The "doubled" cell — which you didn't touch —
        updated immediately. Nothing was "re-run" in the Jupyter sense; marimo
        saw that `count` changed, knew the `doubled` cell depends on `count`,
        and re-executed exactly that cell (and nothing else).

        ### The other half of the deal: one name, one cell

        In exchange for that automatic re-running, marimo enforces a rule
        that Jupyter doesn't: **a variable can only be assigned in one
        cell.** If you write `df = ...` in two different cells, marimo
        refuses to run, with an error like:

        ```
        MultipleDefinitionError: The variable 'df' was defined by another cell
        ```

        This feels restrictive at first. But think back to this morning's
        Module 3 — `df = df[...]` redefinitions, scattered across cells, were
        *exactly* the source of "which version of `df` am I looking at?"
        confusion. marimo's rule forces you to give meaningfully different
        things different names (`df`, `df_durham`, `df_filtered`, ...) —
        which, not coincidentally, was also Module 4's hygiene tip this
        morning. marimo just makes it mandatory.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Revisiting this morning's hidden-state trap

        Recall Cell A / Cell B from this morning: Cell B's *displayed output*
        could silently go stale relative to Cell A.

        In marimo, that specific failure mode can't happen:

        - If Cell B depends on Cell A's output, **changing Cell A
          automatically re-runs Cell B** — its output is never stale.
        - If you delete the cell that defines a variable, every cell that
          referenced it immediately shows an error (undefined name) — it
          can't silently keep using an old value from kernel memory, because
          there *is no separate kernel memory* to fall out of sync with the
          file. The file (this notebook) and the running program are kept in
          lock-step.

        We'll feel this directly in Module 3.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## Module 2: marimo Basics (30 min)

        A few mechanics before we get back to the data:

        - **Cells can live in any order in the file.** marimo's editor will
          often place cells in the order you create them, but execution
          order is always determined by the dependency graph.
        - **Markdown cells** use `mo.md(...)` — this cell is one.
        - **Run modes:** by default marimo runs in *autorun* mode (what
          you've seen so far). There's also a *manual* mode where changed-but-
          not-yet-run cells are marked **stale** (greyed out) until you
          explicitly run them — useful for expensive computations you don't
          want firing on every keystroke.

        Let's build a small reactive chain, the same shape as `x` / `y` from
        this morning.
        """
    )
    return


@app.cell
def _():
    a = 5
    return (a,)


@app.cell
def _(a):
    b = a * 2
    return (b,)


@app.cell
def _(b):
    c = b + 1
    return (c,)


@app.cell
def _(a, b, c, mo):
    mo.md(f"`a = {a}`, so `b = a * 2 = {b}`, and `c = b + 1 = {c}`")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Exercise 2.1 — Change one thing, watch the chain

        1. Scroll up to the `a = 5` cell and change it to `a = 50`.
        2. Watch `b`, `c`, *and the markdown cell below them* all update —
           you ran one cell; three updated.
        3. Now try the editor's drag handle to physically move the
           `c = b + 1` cell to the very top of the file (above `a = 5`).
           Does the notebook still work the same way? (It should — file
           position is cosmetic.)

        Compare this to this morning's Exercise 1.1, where changing `x` did
        **not** automatically update `y`.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## Module 3: Rebuilding the Morning Workflow (30 min)

        Same dataset as this morning. Let's load it and immediately try to
        recreate the Module 3 "hidden state" setup — and see what marimo does
        differently.
        """
    )
    return


@app.cell
def _(pd):
    df = pd.read_csv("biomarker_data.csv")
    df.head()
    return (df,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Try this morning's trap again

        This morning, after loading `df`, the next cell was something like:

        ```python
        older = df[df["age"] > 50]
        ```

        If you add a *new* cell below and write:

        ```python
        df = df[df["site"] == "Durham"]
        ```

        marimo will immediately flag a `MultipleDefinitionError` — `df` is
        already defined, two cells up. **You're stopped before the confusion
        can even start.**

        The fix is exactly the naming discipline from this morning's Module 4:
        give the filtered version its own name.
        """
    )
    return


@app.cell
def _(df):
    df_durham = df[df["site"] == "Durham"]
    df_durham.head()
    return (df_durham,)


@app.cell
def _():
    n_bins = 20
    return (n_bins,)


@app.cell
def _(df, n_bins, plt):
    hist_fig, hist_ax = plt.subplots()
    hist_ax.hist(df["pfoa_serum"], bins=n_bins)
    hist_ax.set_xlabel("Serum PFOA (ng/mL)")
    hist_ax.set_ylabel("Count")
    hist_ax.set_title(f"Distribution of serum PFOA (bins = {n_bins})")
    hist_fig
    return hist_ax, hist_fig


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Exercise 3.1 — Feel the reactivity

        Scroll up to the `n_bins = 20` cell and change it to `n_bins = 5`,
        then `n_bins = 60`.

        Notice: you edited a cell with **no visible output at all**, and the
        histogram — several cells away — redrew itself each time, with no
        "run" action on your part.

        This is the direct answer to this morning's closing question: *"what
        if a notebook tracked dependencies and only ran what's needed,
        automatically?"* This is what that looks like.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## ☕ Break (2:20 - 2:35)
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## Module 4: Interactive UI (40 min)

        `n_bins` was a plain Python variable — *you* edited the code to
        change it. `mo.ui` elements let the people *using* a notebook (not
        editing it) change values too, via widgets. Same reactive graph,
        different kind of input.

        Let's build an interactive view of `biomarker_data`: an age-range
        slider and a site dropdown that drive a filtered table and a plot.
        """
    )
    return


@app.cell
def _(mo):
    age_range = mo.ui.range_slider(
        start=18, stop=90, value=[18, 90], step=1, label="Age range"
    )
    age_range
    return (age_range,)


@app.cell
def _(mo):
    site_picker = mo.ui.dropdown(
        options=["All", "Research Triangle Park", "Durham", "Chapel Hill"],
        value="All",
        label="Site",
    )
    site_picker
    return (site_picker,)


@app.cell
def _(age_range, df, mo, site_picker):
    if site_picker.value == "All":
        df_filtered = df[
            (df["age"] >= age_range.value[0]) & (df["age"] <= age_range.value[1])
        ]
    else:
        df_filtered = df[
            (df["age"] >= age_range.value[0])
            & (df["age"] <= age_range.value[1])
            & (df["site"] == site_picker.value)
        ]
    mo.ui.table(df_filtered, page_size=10)
    return (df_filtered,)


@app.cell
def _(df_filtered, plt):
    scatter_fig, scatter_ax = plt.subplots()
    colors = {"Female": "tab:purple", "Male": "tab:green"}
    for sex_value, group in df_filtered.groupby("sex"):
        scatter_ax.scatter(
            group["pfoa_serum"],
            group["cholesterol"],
            label=sex_value,
            alpha=0.6,
            color=colors.get(sex_value),
        )
    scatter_ax.set_xlabel("Serum PFOA (ng/mL)")
    scatter_ax.set_ylabel("Total cholesterol")
    scatter_ax.set_title("Filtered participants")
    scatter_ax.legend()
    scatter_fig
    return scatter_ax, scatter_fig


@app.cell
def _(mo):
    mo.md(
        r"""
        ### What just happened

        Moving either control re-ran **two** cells: the table cell and the
        plot cell — both depend on `age_range` and/or `site_picker`, neither
        depends on the other. marimo figured out the minimal set of cells to
        re-run from the dependency graph, the same mechanism as Exercise 3.1,
        just triggered by a widget instead of an edit.

        ### Exercise 4.1 — Add a third control

        In the empty cell below, create a slider for a cholesterol threshold,
        e.g.:

        ```python
        chol_threshold = mo.ui.slider(100, 350, value=240, step=10,
                                       label="Cholesterol threshold (mg/dL)")
        chol_threshold
        ```

        Then think about (and if time allows, try) how you'd use
        `chol_threshold.value` in the scatter-plot cell — e.g., drawing a
        horizontal reference line with `scatter_ax.axhline(...)`. Remember:
        any cell that uses `chol_threshold` needs it in its function
        signature.
        """
    )
    return


@app.cell
def _():
    # Exercise 4.1 starter -- uncomment and complete:
    # chol_threshold = mo.ui.slider(100, 350, value=240, step=10,
    #                                label="Cholesterol threshold (mg/dL)")
    # chol_threshold
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## Module 5: SQL Cells (30 min)

        marimo has native SQL cells, backed by DuckDB. A SQL cell can query a
        pandas (or polars) DataFrame **by its Python variable name** — `df`
        in SQL refers to the `df` defined earlier in this notebook. The
        result comes back as a DataFrame and re-enters the reactive graph
        like anything else.

        (In the editor, you create one of these via the cell-type menu —
        "SQL". The underlying code is just a call to `mo.sql(...)`.)
        """
    )
    return


@app.cell
def _(df, mo):
    site_summary = mo.sql(
        f"""
        SELECT
            site,
            COUNT(*) AS n,
            AVG(pfoa_serum) AS avg_pfoa,
            AVG(cholesterol) AS avg_cholesterol
        FROM df
        GROUP BY site
        ORDER BY site
        """
    )
    return (site_summary,)


@app.cell
def _(mo):
    mo.md(
        r"""
        `site_summary` above is a regular DataFrame — it flows into ordinary
        Python cells just like `df_filtered` did.
        """
    )
    return


@app.cell
def _(plt, site_summary):
    sql_fig, sql_ax = plt.subplots()
    sql_ax.bar(site_summary["site"], site_summary["avg_pfoa"])
    sql_ax.set_ylabel("Mean serum PFOA (ng/mL)")
    sql_ax.set_title("Mean PFOA by site (from SQL cell above)")
    sql_ax.tick_params(axis="x", labelrotation=15)
    sql_fig
    return sql_ax, sql_fig


@app.cell
def _(mo):
    mo.md(
        r"""
        ### Exercise 5.1 — Your own query

        In the SQL cell below (currently a placeholder `SELECT * FROM df
        LIMIT 5`), write a query that groups by `sex` instead of `site` and
        computes the average `cholesterol` for each group.

        Note: because the query is just a Python f-string under the hood,
        `df` must be a parameter of this cell (it already is) — same rule as
        every other dependency in marimo.
        """
    )
    return


@app.cell
def _(df, mo):
    exercise_query = mo.sql(
        f"""
        SELECT * FROM df LIMIT 5
        """
    )
    return (exercise_query,)


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## Module 6: Apps, Export & Conversion (25 min)

        ### From notebook to app

        `marimo run notebook.py` serves this **same file** as a read-only
        web app: code cells are hidden, and only markdown, UI elements, and
        outputs (tables, plots) are shown. Individual cells can also be
        marked `@app.cell(hide_code=True)` to hide their source even in edit
        mode. No separate "app" codebase — the notebook *is* the app.

        ### Exporting

        `marimo export` can produce several formats from this file:

        - `marimo export html notebook.py -o out.html` — static HTML snapshot
        - `marimo export ipynb notebook.py -o out.ipynb` — a **Jupyter
          notebook**, cells in dependency (topological) order
        - `marimo export script notebook.py` — flatten to a plain `.py`
          script (what you'd run outside marimo entirely)
        - `marimo export pdf` / `marimo export md` — for sharing or docs

        ### Converting *from* Jupyter

        `marimo convert notebook.ipynb -o notebook.py` does a best-effort
        conversion of a `.ipynb` into marimo format. The most common manual
        fix-up afterward is exactly today's theme: Jupyter notebooks often
        reassign the same variable name (`df = df[...]`) across cells, which
        marimo's one-name-one-cell rule won't allow — you'll need to rename
        those, the same way we renamed `df` to `df_durham` in Module 3.

        ### molab — marimo in the cloud

        For trying marimo with zero install, [molab](https://molab.marimo.io)
        is a free, cloud-hosted marimo notebook environment (similar to
        Google Colab, but for marimo) — useful if you want to keep
        experimenting after today without setting anything up locally.
        """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
        ---
        ## Module 7: Recap & Q&A (20 min)

        | | Jupyter | marimo |
        |---|---|---|
        | File format | `.ipynb` (JSON) | `.py` (plain Python) |
        | Execution order | Whatever order you ran cells, tracked by `In [n]` | Dependency graph, independent of file position |
        | Re-running on change | Manual ("Restart & Run All" is the gold standard) | Automatic — affected cells re-run |
        | Reassigning a variable in another cell | Allowed (and a common source of bugs) | Disallowed (`MultipleDefinitionError`) |
        | Interactivity | Widgets (`ipywidgets`), need callbacks | `mo.ui` elements, reactive by default |
        | SQL on DataFrames | Via libraries (e.g. `duckdb` manually) | Native `mo.sql` cells |
        | Running as an app | Needs a separate framework (Voila, Streamlit, ...) | `marimo run` on the same file |
        | Version control diffs | Noisy (JSON, embedded outputs) | Clean (plain Python) |

        ### When to use which

        Neither tool is strictly "better" — they suit different moments:

        - **Jupyter** remains excellent for fast, throwaway exploration; it's
          the dominant teaching/sharing format, has the largest ecosystem,
          and `.ipynb` is what most collaborators expect to receive.
        - **marimo** earns its keep when a notebook will be **revisited,
          shared, parameterized, or turned into a small app/dashboard** —
          anywhere the "is this actually still correct?" question from this
          morning matters most.

        Many people use both: explore in Jupyter, then `marimo convert` an
        analysis that's "graduating" into something others will rely on.

        ### Resources

        - `marimo tutorial intro` — run this in a terminal for an interactive
          tour
        - [docs.marimo.io](https://docs.marimo.io) — guides and API reference
        - [molab.marimo.io](https://molab.marimo.io) — cloud notebooks, no
          install
        - marimo Discord — community help

        **Thanks for a great day — questions welcome!**
        """
    )
    return


if __name__ == "__main__":
    app.run()
