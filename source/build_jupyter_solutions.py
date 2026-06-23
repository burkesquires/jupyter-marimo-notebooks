"""
Build 01_jupyter_morning_session_SOLUTIONS.ipynb from
01_jupyter_morning_session.ipynb by filling in Exercises 2.1, 3.1, and 3.2.
"""

import nbformat as nbf

nb = nbf.read("01_jupyter_morning_session.ipynb", as_version=4)

md = nbf.v4.new_markdown_cell
code = nbf.v4.new_code_cell

CLIPBOARD = "\U0001F4CB"  # clipboard emoji
CHECK = "\u2705"  # check mark emoji

new_cells = []
for cell in nb.cells:
    src = cell.source

    # --- Title cell: mark as solutions copy ---
    if src.startswith("# Jupyter Notebooks for Scientific Computing"):
        cell.source = src.replace(
            "> **How to use this notebook:**",
            f"> **{CLIPBOARD} INSTRUCTOR SOLUTIONS COPY** \u2014 Exercises 2.1, "
            f"3.1, and 3.2 are filled in below (look for \"{CHECK} Solution\"). "
            "Keep this copy separate from the participant version.\n>\n"
            "> **How to use this notebook:**",
        )
        new_cells.append(cell)
        continue

    # --- Exercise 3.1: filter Durham, mean PFOA (via .query) ---
    if src.strip() == "# Your code here":
        new_cells.append(
            code(
                f"# {CHECK} Solution to Exercise 3.1\n"
                "# Primary approach: .query()\n"
                'durham_mean_pfoa = df.query("site == \'Durham\'")["pfoa_serum"].mean()\n'
                'print(f"Mean serum PFOA in Durham (.query): {durham_mean_pfoa:.2f} ng/mL")\n'
                "\n"
                "# Early-finisher check: boolean indexing should give the same number\n"
                'durham_mean_bool = df[df["site"] == "Durham"]["pfoa_serum"].mean()\n'
                'print(f"Mean serum PFOA in Durham (boolean): {durham_mean_bool:.2f} ng/mL")\n'
                'print(f"Match: {durham_mean_pfoa == durham_mean_bool}")'
            )
        )
        continue

    # --- Exercise 3.2, step 1: define threshold ---
    if src.strip() == "# step 1: define threshold here":
        new_cells.append(
            code(f"# {CHECK} Solution to Exercise 3.2, step 1\nthreshold = 200")
        )
        continue

    # --- Exercise 3.2, step 2: use threshold ---
    if src.strip() == "# step 2: use threshold here":
        new_cells.append(
            code(
                f"# {CHECK} Solution to Exercise 3.2, step 2\n"
                'above_threshold = df[df["cholesterol"] > threshold]\n'
                'print(f"{len(above_threshold)} participants with cholesterol > {threshold}")'
            )
        )
        continue

    new_cells.append(cell)

    # --- Exercise 2.1: add a model-answer markdown cell right after the
    #     participant placeholder cell ---
    if src.strip() == "*(your Exercise 2.1 cell goes here)*":
        new_cells.append(
            md(
                f"{CHECK} **Solution to Exercise 2.1** (one possible answer "
                "\u2014 participants' answers will vary, that's expected):\n"
                "\n"
                "### My goals for today\n"
                "\n"
                "- Get comfortable with the Jupyter execution model (cells, kernel, order)\n"
                "- Understand the \"hidden state\" problem and how to avoid it\n"
                "- See how marimo addresses these issues differently this afternoon\n"
                "\n"
                "A silly equation, just to confirm math rendering works:\n"
                "\n"
                "$$ E = mc^2 $$"
            )
        )

print(f"Original cells: {len(nb.cells)}, new cells: {len(new_cells)}")
nb.cells = new_cells

with open("01_jupyter_morning_session_SOLUTIONS.ipynb", "w") as f:
    nbf.write(nb, f)
