(cbc)=

# CBC

The [COIN Branch and Cut solver (CBC)](https://github.com/coin-or/Cbc) is an open-source mixed-integer program (MIP) solver written in C++.
The driver is built on the [MP library](https://mp.ampl.com/), which reformulates
logical and other expressions that the solver does not accept natively.

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

[Download CBC](https://ampl.com/download/cbc)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install cbc # install CBC

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="cbc", cbc_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver cbc; # change the solver
            ampl: option cbc_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/cbcmp)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP
* MILP

Received natively: linear constraints and ranges, SOS. Quadratic objectives
are not supported; nonlinear functions are [approximated piecewise-linearly](https://mp.ampl.com/modeling-expressions.html#piecewise-linear-approximation);
logical constraints become big-M rows.

All constructs: [native constraints and expressions by driver](https://mp.ampl.com/modeling-tools.html#full-cons-list).
:::

:::{dropdown} LP: CLP simplex and barrier
CBC solves LPs with CLP. Barrier settings: `bar:...` options.
:::

:::{dropdown} MIP: branch-and-cut
Cut generators: `cut:...` options, e.g., `cut:gomorycuts`.
:::

### Instrumentation

For a generic summary of the options and features used most often, see
[Important features](https://mp.ampl.com/features-guide.html#important-features)
in the MP documentation.

```{include} features.inc
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```

More details on solver options: [MP solver options](https://mp.ampl.com/features-guide.html#solver-options).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

CBC solve result codes can be obtained by running `cbc -!` or `ampl: shell "cbc -!";`:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
