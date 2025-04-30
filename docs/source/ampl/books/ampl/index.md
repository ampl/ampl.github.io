(book)=
# The AMPL Book

![](./ampl_s.jpg)

**AMPL: A Modeling Language for Mathematical Programming**  
by Robert Fourer, David M. Gay, and Brian W. Kernighan
Second edition  
517 + xxi pp., ISBN 0-534-38809-4  
[The AMPL Book PDF](./ampl-book.pdf)

```{eval-rst}
.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL. For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_. Additionally, for modern data transfer and programmatic interaction with your models, we recommend using :ref:`APIs <apis>` such as our widely used :ref:`Python API <python_integration>`.
```

A comprehensive guide to building optimization models, for beginning or experienced users.

- Written by the creators of AMPL, this book is a complete guide for modelers at all levels of experience.
- Much more than a user’s manual, it begins with a tutorial on widely used linear programming models and proceeds through a more detailed tutorial exposition of all of AMPL’s features. Extensive examples show how each feature is used in meaningful contexts.
- Advanced chapters cover network, nonlinear, piecewise-linear, and integer programming; database and spreadsheet interactions; and command scripts.
- Most chapters include exercises for study or classroom use.

```{toctree}
:glob:
:maxdepth: 1
chapters/index.md
examples/index.rst
```

## Authors

-   [Robert Fourer](https://www.linkedin.com/in/4er/), AMPL Optimization, Inc.
-   David M. Gay, AMPL Optimization, Inc.
-   Brian W. Kernighan, AMPL Optimization, Inc.

## Citation

If you wish to cite this work, please use

```bibtex
@book{fourer2003ampl,
  title     = {AMPL: A Modeling Language for Mathematical Programming},
  author    = {Fourer, Robert and Gay, David M. and Kernighan, Brian W.},
  year      = {2003},
  edition   = {2nd},
  publisher = {Thomson Brooks/Cole},
  address   = {Pacific Grove, CA},
  isbn      = {0-534-38809-4},
  note      = {517 + xxi pages}
}
```
