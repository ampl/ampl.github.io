(lgo)=

# LGO

LGO is capable of determining high-quality solutions to global optimization problems with continuous variables that have (possibly many) locally optimal solutions. Because LGO makes only limited assumptions as to problem structure and differentiability, it can be applied in a broad range of design and operational applications.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/lgo/)
| [Options](options.md)

[Download LGO](https://ampl.com/download/lgo)
| [Start a LGO Trial Now!](https://ampl.com/trial/lgo)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install lgo # install LGO

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="lgo", lgo_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver lgo; # change the solver
            ampl: option lgo_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Features

### Algorithms

:::{dropdown} Global search without derivatives
`search` (synonym `opmode`): `0` local only, `1` global branch-and-bound
plus local search, `2` adaptive random search plus local search, `3`
multistart local search (default). Time limit: `timelim` (default 300).
Continuous variables only.
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
LGO reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...), nor `complements`. Through MP2NL, MP reformulates them first.

Call [MP2NL](../mp2nl/index.md) as the solver and name LGO inside it; MP's options go into `mp2nl_options`, LGO's own into `lgo_options`.

LGO is a continuous solver: it relaxes the binary variables that MP uses for logical constraints, and the result can violate the logic (MP's solution check then reports it). Use it for constructs that need no binaries, such as complementarity with a smooth reformulation (`cvt:compl=1` or `2`); use an MINLP solver for models with logic.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="mp2nl", mp2nl_options="solver=lgo cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=lgo cvt:compl=1';
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

LGO solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```
