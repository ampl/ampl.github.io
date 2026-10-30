(gcg)=

# GCG

[GCG](https://gcg.or.rwth-aachen.de/) is a generic decomposition solver for mixed-integer programs (MIPs).
It automatically performs a Dantzig-Wolfe reformulation and runs a full-fledged
branch-price-and-cut algorithm to solve it to optimality. Alternatively,
GCG is able to automatically apply a Benders decomposition.
No user interaction is necessary, thus GCG provides decomposition-based MIP solving technology to everyone.

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [GCG modeling guide](#gcg-modeling-guide)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

[Download GCG](https://ampl.com/download/gcg)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install gcg # install GCG

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="gcg", gcg_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver gcg; # change the solver
            ampl: option gcg_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

- [GCG](#gcg)
  - [How to use it](#how-to-use-it)
  - [Resources](#resources)
  - [GCG modeling guide](#gcg-modeling-guide)
  - [Solver options](#solver-options)
  - [Retrieving solutions](#retrieving-solutions)
  - [Changelog](#changelog)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP
* MILP

Received natively: linear constraints and ranges. GCG does not accept
quadratic objectives: quadratic and nonlinear terms are [approximated piecewise-linearly](https://mp.ampl.com/modeling-expressions.html#piecewise-linear-approximation);
logical constraints become big-M rows. Decomposition applies to MIP models.

All constructs: [native constraints and expressions by driver](https://mp.ampl.com/modeling-tools.html#full-cons-list).
:::

:::{dropdown} Dantzig-Wolfe and Benders decomposition
`gcg:mode`: `0` Dantzig-Wolfe with branch-price-and-cut (default), `1`
Benders, `2` no decomposition. Detection of the structure: `det:...`
options; see the [GCG modeling guide](#gcg-modeling-guide).
:::

### Instrumentation

For a generic summary of the options and features used most often, see
[Important features](https://mp.ampl.com/features-guide.html#important-features)
in the MP documentation.

```{include} features.inc
```

## GCG modeling guide

GCG can apply Dantzig-Wolfe or Benders decomposition,
either automatically or user-controlled,
see
[types of structures GCG can detect](https://gcg.or.rwth-aachen.de/doc/structure-types.html)
and
[AMPL/GCG Colab examples](https://ampl.com/colab/tags/gcg.html#tag-gcg).

Moreover, AMPL logical and some nonlinear expressions can be
automatically linearized by the driver,
see [MP modeling guide](https://mp.ampl.com/model-guide.html).

## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
gcg-cpx.md
```

More details on solver options: [MP solver options](https://mp.ampl.com/features-guide.html#solver-options).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

GCG solve result codes can be obtained by running `gcg -!` or `ampl: shell "gcg -!";`:
```{literalinclude} solve_results.inc
:language: none
```

:::{dropdown} Solve result codes of the gcg-cpx driver
```{literalinclude} solve_results_gcg-cpx.inc
:language: none
```
:::

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
