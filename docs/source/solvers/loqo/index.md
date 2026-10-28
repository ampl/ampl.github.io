(loqo)=

# LOQO

LOQO is a powerful solver for smooth constrained optimization problems, based on interior-point method applied to a sequence of quadratic approximations. Subject to the requirement that the defining functions be smooth (at the points evaluated by the algorithm), LOQO can handle a range of problems: linear or nonlinear, convex or nonconvex, constrained or unconstrained. For convex problems, LOQO finds a globally optimal solution; otherwise, it iterates from the given starting point to find a locally optimal solution.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/loqo/)
| [Features](#features)
| [Options](options.md)
| [Changes](changes.md)

[Download LOQO](https://ampl.com/download/loqo)
| [Start a LOQO Trial Now!](https://ampl.com/trial/loqo)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install loqo # install LOQO

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="loqo", loqo_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver loqo; # change the solver
            ampl: option loqo_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Features

### Algorithms

:::{dropdown} Interior point (local)
LOQO applies an interior-point method to a sequence of quadratic
approximations; it returns local optima. Iteration limit: `maxit`. For a
convex model, `convex` lets LOQO use that.
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
Natively, LOQO solves smooth nonlinear models with continuous variables. MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...) and `complements` are not part of its native model type: through MP2NL, MP reformulates them into it first.

Call [MP2NL](../mp2nl/index.md) as the solver and name LOQO inside it; MP's options go into `mp2nl_options`, LOQO's own into `loqo_options`.

LOQO is a continuous solver: it relaxes the binary variables that MP uses for logical constraints, and the result can violate the logic (MP's solution check then reports it). Use it for constructs that need no binaries, such as complementarity with a smooth reformulation (`cvt:compl=1` or `2`); use an MINLP solver for models with logic.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="mp2nl", mp2nl_options="solver=loqo cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=loqo cvt:compl=1';
ampl: solve;
```
:::
::::

More: [Meta-driver MP2NL](https://mp.ampl.com/modeling-tools.html#meta-driver-mp2nl).
:::::


## Options

Full list of solver options:
```{toctree}
options.md
```

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

LOQO solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```
