(couenne)=

# COUENNE

The [COIN Couenne solver (COUENNE, Convex Over and Under ENvelopes for Nonlinear Estimation)](https://github.com/coin-or/Couenne) is a spatial branch & bound algorithm that implements linearization, bound reduction, and branching techniques for Mixed-integer, Nonlinear Programming (MINLP) problems. The purpose of Couenne is to find global optima of nonconvex MINLPs.

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [Features](#features)
| [Options](#solver-options)

[Download COUENNE](https://ampl.com/download/coin)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install couenne # install COUENNE

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="couenne", couenne_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver couenne; # change the solver
            ampl: option couenne_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

- [COUENNE](#couenne)
  - [How to use it](#how-to-use-it)
  - [Resources](#resources)
  - [Solver options](#solver-options)
  - [Retrieving solutions](#retrieving-solutions)

## Features

### Algorithms

:::{dropdown} Global: spatial branch-and-bound
Couenne builds convex relaxations of the nonconvex terms and branches on
continuous and integer variables to find a global optimum. Time limit:
`bonmin.time_limit`; Ipopt options apply to its local NLP solves.
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
Natively, Couenne solves nonlinear models with continuous and integer variables. MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...) and `complements` are not part of its native model type: through MP2NL, MP reformulates them into it first.

Call [MP2NL](../mp2nl/index.md) as the solver and name Couenne inside it; MP's options go into `mp2nl_options`, Couenne's own into `couenne_options`.

MP reformulates logic with binary variables, which Couenne handles as integer variables.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="mp2nl", mp2nl_options="solver=couenne cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=couenne cvt:compl=1';
ampl: solve;
```
:::
::::

More: [Meta-driver MP2NL](https://mp.ampl.com/modeling-tools.html#meta-driver-mp2nl).
:::::


## Solver options

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

COUENNE solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```

