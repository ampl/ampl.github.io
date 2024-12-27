import csv
import shutil

# Define the input CSV file and output RST file
csv_file = "examples.csv"
csv_fig_file = "examples_fig.csv"
rst_file = "index.rst"


def csv_to_rows(csv_file):
    # Read the CSV file
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        rows = list(reader)
    return rows


examples_files = {}


def preprocess_rows(rows):
    for row in rows:
        for value in row:
            if "." not in value:
                continue
            examples_files[value] = f":doc:`{value} <{value}>`"
    return [[examples_files.get(value, value) for value in row] for row in rows]


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

    file.write("List of example files\n")
    file.write("---------------------\n\n")

    file.write("\n.. toctree::\n")
    file.write("    :maxdepth: 2\n\n")
    for ampl_file in sorted(examples_files):
        file.write(f"    {ampl_file}.rst\n")

print(f"RST file '{rst_file}' has been generated.")

for ampl_file in examples_files:
    rst_file = f"{ampl_file}.rst"
    fname = f"EXAMPLES/EXAMPLES2/{ampl_file}"
    content = open(fname, "r").read()
    with open(rst_file, "w") as file:
        file.write(f"{ampl_file}\n{'='*len(ampl_file)}\n\n")
        file.write(f":download:`{ampl_file} <{fname}>`\n\n")
        file.write(".. code-block:: ampl\n\n")
        for line in content.splitlines():
            file.write(f"    {line}\n")
