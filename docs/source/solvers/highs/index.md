(highs)=

# HiGHS

A leading free solver that has evolved from a large-scale optimization project
at the University of Edinburgh. [HiGHS](https://highs.dev/) is open-source software to solve
linear programming, mixed-integer programming, and convex quadratic programming models.
The driver is built on the [MP library](https://mp.ampl.com/), which reformulates
logical and other expressions that the solver does not accept natively.

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

[Download HiGHS](https://ampl.com/download/highs)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install highs # install HiGHS

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="highs", highs_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver highs; # change the solver
            ampl: option highs_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/highsmp)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP, convex QP
* MILP

Received natively: linear constraints and ranges, and a quadratic objective
for models without integer variables (for MIQP, `cvt:quadobj=0` approximates
the quadratic objective). Logical constraints become big-M rows; quadratic
constraints and nonlinear functions are [approximated piecewise-linearly](https://mp.ampl.com/modeling-expressions.html#piecewise-linear-approximation).

All constructs: [native constraints and expressions by driver](https://mp.ampl.com/modeling-tools.html#full-cons-list).
:::

:::{dropdown} LP: simplex, interior point, PDLP
`alg:method`: `choose` (default), `simplex`, `ipm` (interior point,
automatic), `ipx`, `hipo`, `pdlp` (first-order), `pdlp-gpu` (NVIDIA GPU,
not on macOS). Parallel simplex: `alg:parallel=on`.
:::

:::{dropdown} Convex QP: active set
QPs are solved by the active-set method (`alg:method=qpasm`).
:::

:::{dropdown} MIP: branch-and-cut
Relative gap: `mip:gap`.
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

HiGHS solve result codes can be obtained by running `highs -!` or `ampl: shell "highs -!";`:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
