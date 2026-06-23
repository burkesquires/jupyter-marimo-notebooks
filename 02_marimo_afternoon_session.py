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
    mo.md(r"""
    # Reactive Notebooks with marimo
    ### NIEHS Notebook Training — Afternoon Session (1:00 - 4:30)

    | Time | Module |
    |---|---|
    | 1:00 - 1:20 | Module 1: What Is marimo? |
    | 1:20 - 1:50 | Module 2: marimo Basics |
    | 1:50 - 2:20 | Module 3: A Reactive Data Workflow |
    | 2:20 - 2:35 | *Break* |
    | 2:35 - 3:15 | Module 4: Interactive UI |
    | 3:15 - 3:45 | Module 5: SQL Cells |
    | 3:45 - 4:15 | Module 6: Apps, Export, Sandbox & Testing |
    | 4:15 - 4:30 | Module 7: Recap & Q&A |

    **Goal of the afternoon:** learn marimo, a reactive Python notebook,
    on its own terms. We'll use the same dataset as the morning
    (`biomarker_data.csv`) so you can focus on the tool rather than the
    data. As in the morning, the focus is the **tool**, not the
    statistics.

    > **How to use this notebook:** marimo notebooks are plain `.py`
    > files. Cells run automatically when their inputs change — marimo
    > works out the run order from how cells depend on each other.
    > Editing a value or moving a UI element (sliders, dropdowns) re-runs
    > whatever depends on it.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
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
    """)
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
    return


@app.cell
def _(mo):
    mo.md(r"""
    Drag the slider above. The "doubled" cell — which you didn't touch —
    updated immediately. marimo saw that `count` changed, knew the
    `doubled` cell depends on `count`, and re-executed exactly that cell
    (and nothing else). This is marimo's defining feature: it tracks how
    cells depend on each other and keeps everything consistent
    automatically.

    ### One variable, one cell

    marimo has one rule that follows directly from its reactive design:
    **a variable can only be assigned in one cell.** If you write `df =
    ...` in two different cells, marimo asks you to rename one, with a
    message like:

    ```
    MultipleDefinitionError: The variable 'df' was defined by another cell
    ```

    The reason is mechanical: for marimo to know which cells to re-run
    when `df` changes, each variable needs exactly one definition site.
    In practice this nudges you toward giving distinct things distinct
    names (`df`, `df_durham`, `df_filtered`, ...), which tends to make
    notebooks easier to read. It's a small adjustment if you're used to
    reassigning the same name repeatedly, and most people find the habit
    natural within a few cells.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### What the reactive model guarantees

    Because marimo runs cells based on their dependencies, two things are
    always true while you work:

    - **Outputs stay current.** If cell B uses a value from cell A,
      changing A automatically re-runs B. You never have to remember to
      re-run downstream cells by hand.
    - **The notebook and the running program stay in step.** marimo
      notebooks are `.py` files, and the live state is derived directly
      from running that file's cells in dependency order — so what you
      see reflects the current code.

    This is the flip side of the morning's execution model. In Jupyter,
    *you* choose the run order, which is ideal for free-form exploration.
    In marimo, the *dependency graph* chooses it for you, which is ideal
    when you want the whole notebook to stay internally consistent as you
    edit. Neither is "correct" — they're two designs suited to different
    ways of working. We'll feel marimo's version directly in Module 3.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
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

    Let's build a small reactive chain to see the dependency tracking in
    action.
    """)
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
    mo.md(f"""
    `a = {a}`, so `b = a * 2 = {b}`, and `c = b + 1 = {c}`
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Live narrative: mo.md with computed values

    The `mo.md(f"...")` pattern above isn't just for simple labels — it's
    how marimo enables **living results prose**. Instead of computing a
    result and manually typing the number into a sentence (then forgetting
    to update it when the data changes), you embed the computation
    directly in the narrative. The paragraph below re-writes itself
    whenever `a` changes:
    """)
    return


@app.cell
def _(a, b, c, mo):
    mo.md(f"""
    ### Reactive results paragraph

    In this chain, a base value of **{a}** produces a doubled value of
    **{b}** and a final value of **{c}**. The ratio of final to base is
    **{c / a:.2f}x**.

    *Change `a = 5` above to any number and watch this entire paragraph
    rewrite itself — no copy-paste, no stale numbers.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Exercise 2.1 — Change one thing, watch the chain

    1. Scroll up to the `a = 5` cell and change it to `a = 50`.
    2. Watch `b`, `c`, the inline label *and the results paragraph* all
       update — you ran one cell; four cells updated. That's the
       dependency graph at work: marimo re-ran exactly the cells that
       depend on `a`.
    3. Now try the editor's drag handle to physically move the
       `c = b + 1` cell to the very top of the file (above `a = 5`).
       Does the notebook still work the same way? (It should — marimo
       runs cells by dependency, so file position is cosmetic.)

    Notice what the results paragraph demonstrates: when we do this with
    real biomarker data in Module 3, changing a filter will rewrite the
    results narrative automatically — no copying numbers by hand.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Module 3: A Reactive Data Workflow (30 min)

    Let's load the biomarker data and build a small analysis on it,
    seeing how marimo's reactivity behaves with real data.
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv("/Users/burkesquires/Documents/GitHub/jupyter-marimo-notebooks/biomarker_data.csv")
    df.head()
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""
    ### One variable, one cell — in practice

    Say you've loaded `df` and now want a Durham-only subset. It's
    tempting to write:

    ```python
    df = df[df["site"] == "Durham"]   # reassigning df
    ```

    marimo will flag a `MultipleDefinitionError`, because `df` is already
    defined in the cell above. The fix is to give the subset its own
    name:

    ```python
    df_durham = df[df["site"] == "Durham"]
    ```

    This keeps both the full dataset and the subset available, each with
    a clear name — which also means any cell can refer to whichever one
    it needs, and marimo can track those dependencies cleanly.
    """)
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
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Exercise 3.1 — Feel the reactivity

    Scroll up to the `n_bins = 20` cell and change it to `n_bins = 5`,
    then `n_bins = 60`.

    Notice: you edited a cell with **no visible output at all**, and the
    histogram — several cells away — redrew itself each time, with no
    "run" action on your part.

    This is marimo's reactive model on real data: change one input, and
    everything that depends on it updates automatically.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### The full pipeline: filter → compute → narrative

    The real payoff of reactivity isn't just a redrawing histogram. It's
    what happens when your analysis has **multiple downstream steps** —
    filters, summaries, figures, and written results — all depending on
    the same upstream choices.

    The cells below build a simple pipeline on top of `df_durham`:
    a computed-stats cell, and a results narrative that reads like a
    methods section. Change the filter that defines `df_durham` and
    everything — numbers, prose, all of it — updates in one pass.
    """)
    return


@app.cell
def _(df, df_durham):
    n_total = len(df)
    n_durham = len(df_durham)
    mean_pfoa_durham = round(df_durham["pfoa_serum"].mean(), 2)
    mean_pfoa_overall = round(df["pfoa_serum"].mean(), 2)
    pct_durham = round(n_durham / n_total * 100, 1)
    return mean_pfoa_durham, mean_pfoa_overall, n_durham, n_total, pct_durham


@app.cell
def _(mean_pfoa_durham, mean_pfoa_overall, mo, n_durham, n_total, pct_durham):
    mo.md(f"""
    ### Live results summary

    The Durham site contributed **{n_durham} of {n_total} participants**
    ({pct_durham}%). Mean serum PFOA in Durham was
    **{mean_pfoa_durham} ng/mL**, compared to **{mean_pfoa_overall} ng/mL**
    across all three sites.

    *Now go back and change the filter `df[df["site"] == "Durham"]` to
    `df[df["site"] == "Chapel Hill"]` and watch every number in this
    paragraph update automatically — no copy-paste, no stale values.*
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## ☕ Break (2:20 - 2:35)
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Module 4: Interactive UI (40 min)

    `n_bins` was a plain Python variable — *you* edited the code to
    change it. `mo.ui` elements let the people *using* a notebook (not
    editing it) change values too, via widgets. Same reactive graph,
    different kind of input.

    Let's build an interactive view of `biomarker_data`: an age-range
    slider and a site dropdown that drive a filtered table and a plot.
    """)
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
    return


@app.cell
def _(mo):
    mo.md(r"""
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
    """)
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
    mo.md(r"""
    ---
    ## Module 5: SQL Cells (30 min)

    marimo has native SQL cells, backed by DuckDB. A SQL cell can query a
    pandas (or polars) DataFrame **by its Python variable name** — `df`
    in SQL refers to the `df` defined earlier in this notebook. The
    result comes back as a DataFrame and re-enters the reactive graph
    like anything else.

    (In the editor, you create one of these via the cell-type menu —
    "SQL". The underlying code is just a call to `mo.sql(...)`.)

    ### When SQL vs. Python

    Both can filter and aggregate the same data — the question is which
    reads more clearly for the task:

    | Task | Better tool |
    |---|---|
    | Row filtering, grouping, aggregation | SQL — closer to how the question is phrased |
    | Reshaping, merging multiple DataFrames | Either; pandas has strong join/pivot support |
    | Statistical modeling, custom functions | Python — SQL has no `scipy.stats` |
    | Quick ad-hoc check on a known DataFrame | SQL — often fewer keystrokes |

    For researchers already comfortable with SQL (common in database-
    driven labs or with REDCap/clinical data backgrounds), native SQL
    cells mean you don't have to translate the query into pandas idioms —
    write the SQL you'd write anywhere, get a DataFrame back, continue
    in Python.
    """)
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
    mo.md(r"""
    `site_summary` above is a regular DataFrame — it flows into ordinary
    Python cells just like `df_filtered` did.
    """)
    return


@app.cell
def _(plt, site_summary):
    sql_fig, sql_ax = plt.subplots()
    sql_ax.bar(site_summary["site"], site_summary["avg_pfoa"])
    sql_ax.set_ylabel("Mean serum PFOA (ng/mL)")
    sql_ax.set_title("Mean PFOA by site (from SQL cell above)")
    sql_ax.tick_params(axis="x", labelrotation=15)
    sql_fig
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### SQL → Python → narrative: a complete pipeline

    The SQL result (`site_summary`) is just a DataFrame — it flows into
    any Python cell as a normal dependency. This means you can chain SQL
    and Python together: use SQL for the aggregation it's good at, then
    Python for the downstream logic or annotation.

    The cells below take `site_summary`, identify the highest-exposure
    site in Python, and write a reactive results sentence — the same
    live-narrative pattern from Module 2, now driven by a SQL query.
    """)
    return


@app.cell
def _(site_summary):
    highest_site_row = site_summary.loc[site_summary["avg_pfoa"].idxmax()]
    highest_site = highest_site_row["site"]
    highest_pfoa = round(highest_site_row["avg_pfoa"], 2)
    return highest_pfoa, highest_site


@app.cell
def _(highest_pfoa, highest_site, mo):
    mo.md(f"""
    **Highest mean PFOA by site (SQL → Python):**
    The {highest_site} site had the highest mean serum PFOA at
    **{highest_pfoa} ng/mL**. This value is drawn live from the SQL
    aggregation above — edit the query (e.g. add a `WHERE age > 50`
    clause) and this sentence updates automatically.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Exercise 5.1 — Your own query

    In the SQL cell below (currently a placeholder `SELECT * FROM df
    LIMIT 5`), write a query that groups by `sex` instead of `site` and
    computes the average `cholesterol` for each group.

    Note: because the query is just a Python f-string under the hood,
    `df` must be a parameter of this cell (it already is) — same rule as
    every other dependency in marimo.
    """)
    return


@app.cell
def _(df, mo):
    exercise_query = mo.sql(
        f"""
        SELECT * FROM df LIMIT 5
        """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Module 6: Apps, Export, Sandbox & Testing (30 min)

    ### From notebook to app — the research lifecycle

    The three modes (`edit` / `run` / `export`) map naturally onto stages
    a research analysis goes through:

    **Stage 1 — Explore** (`marimo edit notebook.py`)
    You're in the editor, cells visible, building the analysis
    interactively. This is where you spend most of your time during
    active development. The reactive graph means you can tune parameters
    and immediately see downstream effects without managing "run this, then
    that."

    **Stage 2 — Share with collaborators** (`marimo run notebook.py`)
    Once the analysis is stable, `marimo run` serves it as a clean web
    app — code hidden, only outputs and controls visible. A colleague
    with no Python background can adjust a dropdown or slider and explore
    the results themselves, without touching the code. Same file, zero
    extra work.

    **Stage 3 — Archive / publish** (`marimo export`)
    `marimo export html` creates a static snapshot for a report or
    supplementary material. `marimo export html-wasm` creates an
    interactive version that runs in any browser with no server — useful
    for journal supplementaries or institutional repositories that can't
    host a Python process. `marimo export ipynb` hands the work back to
    a Jupyter user if needed.

    `marimo run notebook.py` serves this file as a read-only web app:
    code cells are hidden, and only markdown, UI elements, and outputs
    (tables, plots) are shown. Individual cells can also be marked
    `@app.cell(hide_code=True)` to hide their source even in edit mode.
    No separate "app" codebase — the notebook *is* the app.

    ### Exporting

    `marimo export` can produce several formats from this file:

    - `marimo export html notebook.py -o out.html` — static HTML snapshot
    - `marimo export html-wasm notebook.py -o build/` — **interactive**
      notebook that runs entirely in the browser (no server required);
      suitable for GitHub Pages or sharing with non-technical collaborators
      via a URL (this is how [molab](https://molab.marimo.io) itself works)
    - `marimo export ipynb notebook.py -o out.ipynb` — a **Jupyter
      notebook**, cells in dependency (topological) order
    - `marimo export script notebook.py` — flatten to a plain `.py`
      script (what you'd run outside marimo entirely)
    - `marimo export pdf` / `marimo export md` — for sharing or docs

    ### Opening an existing Jupyter notebook in marimo

    There are millions of Jupyter notebooks out in the world — on GitHub,
    in papers' supplementary materials, in shared analyses. If you find
    one you'd like to work with in marimo, `marimo convert` opens it:

    ```
    marimo convert notebook.ipynb -o notebook.py
    ```

    This does a best-effort conversion of a `.ipynb` into marimo's `.py`
    format. Because marimo uses the one-variable-one-cell model, the most
    common manual fix-up afterward is renaming any variables that the
    original notebook reassigned across cells (a Jupyter notebook might
    use `df = df[...]` several times; in marimo you'd give each step its
    own name, as in Module 3). It's usually a quick cleanup, and it lets
    you bring existing work into marimo when that's the tool you want.

    ### Sandbox mode & reproducible environments

    When you run `marimo edit notebook.py --sandbox`, marimo launches the
    notebook in a fully isolated environment (powered by `uv` under the
    hood). If any imported package is not yet declared, marimo prompts you
    to install it, then automatically adds a **dependency block** at the
    very top of the `.py` file:

    ```python
    # /// script
    # requires-python = ">=3.11"
    # dependencies = [
    #     "marimo",
    #     "numpy==2.2.5",
    #     "pandas==2.2.3",
    # ]
    # ///
    ```

    This is a [PEP 723](https://peps.python.org/pep-0723/) inline script
    metadata block. Anyone who receives the `.py` file can run
    `marimo edit notebook.py --sandbox` and the right package versions
    will be installed automatically — no `requirements.txt` to keep in
    sync, no conda environment to document separately. The notebook
    *carries its own environment*.

    **Why it was disabled on this JupyterHub:** sandbox mode downloads
    packages on first open, which is fragile on conference wifi and
    redundant when everyone shares a pre-built server environment. For
    post-workshop local use (your own laptop, molab, or a personal
    server), `--sandbox` is the right default for any analysis you'll
    share or come back to later.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Unit testing in marimo

    Because a marimo notebook is a plain `.py` file, it integrates with
    `pytest` in two ways that Jupyter can't match without add-on packages:

    1. **In-notebook test cells:** any cell whose *entire content* is
       `def test_...` functions is automatically detected and run by
       marimo when `pytest` is installed. Pass/fail results appear
       inline in the notebook, live as you edit.
    2. **Terminal:** `pytest notebook.py` works directly — marimo's
       pytest plugin collects and runs all test cells, making CI
       integration (GitHub Actions, etc.) straightforward with no extra
       setup.

    For scientific analysis this is genuinely useful: you can write
    data-validity checks right alongside the analysis code, and they
    re-run automatically whenever `df` changes.

    Below are two example tests on our biomarker data, followed by an
    exercise to write two more.
    """)
    return


@app.cell
def _(df):
    # Example test cell — marimo runs these automatically with pytest.
    # Note: df arrives as a dependency (it's in this cell's signature),
    # and the test functions close over it. No import needed.

    def test_pfoa_nonnegative():
        """PFOA is a concentration — all values should be >= 0."""
        assert (df["pfoa_serum"] >= 0).all(), \
            f"Found {(df['pfoa_serum'] < 0).sum()} negative PFOA values"

    def test_participant_count():
        """Dataset should have exactly 200 participants."""
        assert len(df) == 200, f"Expected 200 rows, got {len(df)}"

    return


@app.cell
def _(mo):
    mo.md(r"""
    ### Exercise 6.1 — Write your own data validation test

    The starter cell below has `test_sex_values` already completed as a
    model to follow. Your task: **uncomment and complete
    `test_cholesterol_range`** — confirm all cholesterol values fall
    between 50 and 400 mg/dL (a biologically plausible range for this
    dataset).

    Watch marimo run both tests inline as soon as you save the cell. Then
    try deliberately breaking your assertion (e.g. change `400` to `100`)
    and observe the failure output — that's what a collaborator would see
    if the data ever violated the assumption.

    Bonus: if you have a terminal available, try running pytest directly
    on this file:
    ```
    pytest 02_marimo_afternoon_session.py -v
    ```
    """)
    return


@app.cell
def _(df):
    # Exercise 6.1 starter — complete the assertions

    def test_sex_values():
        expected_sex = {"Female", "Male"}
        actual_sex = set(df["sex"].unique())
        assert actual_sex == expected_sex, f"Unexpected sex values: {actual_sex}"
    # def test_cholesterol_range():
    #     assert ___  # your assertion here
    return


@app.cell
def _(mo):
    mo.md(r"""
    ### molab — marimo in the cloud

    For trying marimo with zero install after today,
    [molab](https://molab.marimo.io) is a free, cloud-hosted marimo
    environment — useful if you want to keep experimenting without a
    local setup. Notebooks can also be mirrored from GitHub, so a
    `--sandbox`-enabled `.py` file pushed to a repo opens and runs
    cleanly on molab with its declared dependencies.
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    ## Module 7: Recap & Q&A (15 min)

    A factual side-by-side of the two tools you've learned today. Neither
    column is "better" — they're different designs, and the right choice
    depends on the task.

    | | Jupyter | marimo |
    |---|---|---|
    | File format | `.ipynb` (JSON) | `.py` (plain Python) |
    | Execution model | You choose run order; tracked by `In [n]` | Dependency graph determines run order |
    | Re-running on change | Manual (Restart & Run All to resync) | Automatic — dependent cells re-run |
    | Variable assignment | A name can be reassigned across cells | One definition per variable (enables reactivity) |
    | Interactivity | Widgets (`ipywidgets`) with callbacks | `mo.ui` elements, reactive by default |
    | SQL on DataFrames | Via libraries (e.g. `duckdb` directly) | Native `mo.sql` cells |
    | Running as an app | Add-on frameworks (Voila, Streamlit, ...) | `marimo run` on the same file |
    | Version control diffs | JSON with embedded outputs | Plain Python |
    | Ecosystem & reach | Largest; renders on GitHub, Colab, many editors; R/Julia/100+ kernels | Newer, Python-focused, growing |
    | Reproducible environments | Managed separately (conda, venv, requirements) | Optional `--sandbox` mode pins deps in the file |

    ### When each is a great fit

    Both are excellent tools; many researchers use both depending on the
    job.

    - **Reach for Jupyter when** you want the broadest ecosystem and
      compatibility, you're doing fast exploratory work, you're sharing
      with collaborators who expect `.ipynb`, you're teaching or
      publishing where rendered outputs on GitHub/Colab matter, or you
      need a non-Python kernel (R, Julia, etc.).
    - **Reach for marimo when** you want cells to stay automatically in
      sync as you edit, you're building an interactive view or small app
      for collaborators, you value clean `.py` files for version control,
      or you want the notebook to carry its own reproducible environment.

    And the two interoperate: `marimo convert` opens an existing `.ipynb`
    in marimo, and `marimo export ipynb` goes the other way — so choosing
    one today doesn't lock you out of the other.

    ### Resources

    - `marimo tutorial intro` — run this in a terminal for an interactive
      tour
    - [docs.marimo.io](https://docs.marimo.io) — guides and API reference
    - [molab.marimo.io](https://molab.marimo.io) — cloud notebooks, no
      install
    - marimo Discord — community help

    **Thanks for a great day — questions welcome!**
    """)
    return


if __name__ == "__main__":
    app.run()
