(cplex)=

# IBM CPLEX

IBM ILOG CPLEX has been a well known and widely used large-scale solver for over three decades. Its efficiency and robustness have been demonstrated through varied applications in thousands of commercial installations worldwide.
The driver is built on the [MP library](https://mp.ampl.com/), which reformulates
logical and other expressions that the solver does not accept natively.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/cplex/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

[Download CPLEX](https://ampl.com/download/cplex)
| [Start a CPLEX Trial Now!](https://ampl.com/trial/cplex)

This package contains an all-new CPLEX driver, that provides significantly extended modeling support for logical and nonlinear operators through linearizations performed by the [MP library](https://mp.ampl.com/). For compatibility, there are two binaries in this package: `cplex` [[options](options.md)] is the new version, `cplexasl` [[options](cplexasl.md)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install cplex # install CPLEX

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="cplex", cplex_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis_ampls.rst.inc

   .. tab-item:: AMPL

        CPLEX options consist of a single-word option, or an option followed by an = sign and a value; a space may be used as a separator in place of the =.

        .. code-block:: ampl

            ampl: option solver cplex; # change the solver
            ampl: option cplex_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/cplex)
* [Using with callbacks](https://ampls.ampl.com/)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP, convex QP and QCP, SOCP, nonconvex QP objective
* MILP, MIQP, MIQCP, MISOCP

Received natively: indicator constraints, piecewise-linear functions, SOS,
quadratic constraints. Other logical constraints become indicator
constraints or big-M rows; other nonlinear functions are [approximated piecewise-linearly](https://mp.ampl.com/modeling-expressions.html#piecewise-linear-approximation).

All constructs: [native constraints and expressions by driver](https://mp.ampl.com/modeling-tools.html#full-cons-list).
:::

:::{dropdown} LP and QP: simplex, barrier, sifting, network
`alg:method`: `0` automatic (default), `1` primal simplex, `2` dual simplex,
`3` network simplex, `4` barrier, `5` sifting, `6` concurrent. After
barrier, `bar:crossover` controls the basis computation.
:::

:::{dropdown} MIP: branch-and-cut, Benders
Relative and absolute gaps: `mip:gap`, `mip:gapabs`. Benders decomposition:
`alg:benders=1` (the model needs integer and continuous variables). Most
other controls are `mip:...` and `cut:...` options.
:::

:::{dropdown} Nonconvex quadratic objective
`qp:target=3` solves a (MI)QP with a nonconvex quadratic objective to global
optimality; `2` searches for a first-order (local) point of a continuous QP.
Nonconvex quadratic constraints are not supported.
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
```{toctree}
:hidden:
cplexasl.md
```

More details on solver options: [MP solver options](https://mp.ampl.com/features-guide.html#solver-options).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

CPLEX solve result codes can be obtained by running `cplex -!` or `ampl: shell "cplex -!";`:
```{literalinclude} solve_results.inc
:language: none
```

:::{dropdown} Solve result codes of the legacy driver cplexasl
```{literalinclude} solve_results_cplexasl.inc
:language: none
```
:::

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesasl.md
```
