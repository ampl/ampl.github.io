import csv
import os
import shutil

# Define the input CSV file and output RST file
csv_file = "examples.csv"
csv_fig_file = "examples_fig.csv"
csv_additional_scripts_1 = "examples-additional-scripts-1.csv"
csv_additional_scripts_2 = "examples-additional-scripts-2.csv"
csv_logic_examples = "examples-logic.csv"
rst_file = "index.rst"


def csv_to_rows(csv_file):
    # Read the CSV file
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter="|")
        rows = list(reader)
    return rows


examples_files = {}


def preprocess_rows(rows):
    def link_examples(value, examples):
        if value in examples:
            return examples[value]
        if " " in value:
            return " ".join(map(lambda v: examples.get(v, v), value.split(" ")))
        return value

    for row in rows:
        for value in row:
            if value.endswith((".mod", ".dat", ".run")) or value.startswith(("steelT")):
                for v in value.split(" "):
                    examples_files[v] = f":doc:`{v} <{v}>`"
    return [[link_examples(value, examples_files) for value in row] for row in rows]


def rows_to_rst_table(rows, file):
    # Determine column widths
    col_widths = [
        max(len(str(row[col])) for row in rows) for col in range(len(rows[0]))
    ]

    # Generate the RST table
    # Write the table header
    header_border = (
        "+" + "+".join("-" * (col_width + 2) for col_width in col_widths) + "+"
    )
    file.write(header_border + "\n")
    header_row = (
        "|"
        + "|".join(
            f" {col:{col_width}} " for col, col_width in zip(rows[0], col_widths)
        )
        + "|"
    )
    file.write(header_row + "\n")
    file.write(header_border.replace("-", "=") + "\n")  # Header underline

    # Write the table rows
    for row in rows[1:]:
        row_line = (
            "|"
            + "|".join(
                f" {cell:{col_width}} " for cell, col_width in zip(row, col_widths)
            )
            + "|"
        )
        file.write(row_line + "\n")
        file.write(header_border + "\n")
    file.write("\n\n")


HEADER = """
AMPL Book Examples
==================

| **AMPL: A Modeling Language for Mathematical Programming**
| by Robert Fourer, David M. Gay, and Brian W. Kernighan
| Second edition
| 517 + xxi pp., ISBN 0-534-38809-4
| :download:`The AMPL Book PDF <../ampl-book.pdf>`

.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL. For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_. Additionally, for modern data transfer and programmatic interaction with your models, we recommend using :ref:`APIs <apis>` such as our widely used :ref:`Python API <python_integration>`.

Use this page to download all the model, data, and script files that appear as examples in the AMPL book (second edition). You can download everything in one file:

- :download:`zipfile <./EXAMPLES/EXAMPLES2/amplbook2.zip>` with line endings characteristic of Windows
- :download:`gzipped tar file <./EXAMPLES/EXAMPLES2/amplbook2.tgz>` with line endings characteristic of Unix

Or download individual files from our listings below, by filename or by figure number.
\n
"""

with open(rst_file, mode="w", encoding="utf-8") as file:
    file.write(HEADER)
    file.write("\n")
    file.write("Book examples by filename\n")
    file.write("-------------------------\n\n")

    rows = csv_to_rows(csv_file)
    rows = preprocess_rows(rows)
    rows_to_rst_table(rows, file)

    file.write("\n")
    file.write("Book examples by figure number\n")
    file.write("------------------------------\n\n")

    rows = csv_to_rows(csv_fig_file)
    rows = preprocess_rows(rows)
    rows_to_rst_table(rows, file)

    file.write("\n")
    file.write("Additional Scripts: Looping and Testing - 1\n")
    file.write("-------------------------------------------\n\n")
    file.write("Writing “scripts” in the AMPL command language\n\n")
    file.write(
        "All examples use :doc:`steelT.mod <steelT.mod>` as the model file and the :doc:`steelT.dat <steelT.dat>` as the data file.\n\n"
    )

    rows = csv_to_rows(csv_additional_scripts_1)
    rows = preprocess_rows(rows)
    rows_to_rst_table(rows, file)

    file.write("\n")
    file.write("Additional Scripts: Looping and Testing - 2\n")
    file.write("-------------------------------------------\n\n")
    file.write("Implementing algorithms through AMPL scripts\n\n")

    rows = csv_to_rows(csv_additional_scripts_2)
    rows = preprocess_rows(rows)
    rows_to_rst_table(rows, file)

    file.write("\n")
    file.write("Logic & Constraint Programming Examples\n")
    file.write("---------------------------------------\n\n")
    file.write(
        "This is a preliminary set of examples to offer some starting points for experimenting with AMPL’s `“logic” and constraint programming interfaces <https://ampl.com/products/ampl/logic-and-constraint-programming-extensions/>`_. We welcome comments for improvements or other examples. \n\n"
    )

    rows = csv_to_rows(csv_logic_examples)
    rows = preprocess_rows(rows)
    rows_to_rst_table(rows, file)

    file.write("List of example files\n")
    file.write("---------------------\n\n")

    file.write("\n.. toctree::\n")
    file.write("    :maxdepth: 2\n\n")
    for ampl_file in sorted(examples_files):
        file.write(f"    {ampl_file}.rst\n")

print(f"RST file '{rst_file}' has been generated.")

paths = [
    "EXAMPLES/EXAMPLES2",
    "EXAMPLES/LOOP1",
    "EXAMPLES/LOOP2",
    "EXAMPLES/LOGIC/EXAMPLES",
]

warning_generic = """
.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL."""
warning_mod = f"""{warning_generic}
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

"""
warning_dat = f"""{warning_generic}
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

"""
warning_run = f"""{warning_generic}
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

"""

for ampl_file in examples_files:
    rst_file = f"{ampl_file}.rst"
    for path in paths:
        fname = f"{path}/{ampl_file}"
        if os.path.isfile(fname):
            break
    assert os.path.isfile(fname), f"{fname} not found"
    content = open(fname, "r").read()
    with open(rst_file, "w") as file:
        file.write(f"{ampl_file}\n{'='*len(ampl_file)}\n\n")
        if fname.endswith(".mod"):
            file.write(warning_mod)
        elif fname.endswith(".dat"):
            file.write(warning_dat)
        else:
            file.write(warning_run)
        file.write(f":download:`{ampl_file} <{fname}>`\n\n")
        file.write(".. code-block:: ampl\n\n")
        for line in content.splitlines():
            file.write(f"    {line}\n")
