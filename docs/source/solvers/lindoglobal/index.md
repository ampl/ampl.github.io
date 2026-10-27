(lindo-global-solver)=

# LINDO Global Solver

LINDO Global is a versatile nonlinear optimizer that supports global optimization in continuous and discrete variables. It accepts a variety of objective and constraint functions, including many that are nonconvex and nonsmooth.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/lindoglobal/)
| [Options](options.md)
| [Changes](changes.md)

[Download LINDO Global](https://ampl.com/download/lindoglobal)
| [Start a LINDO Global Trial Now!](https://ampl.com/trial/lindoglobal)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install lindoglobal # install LINDO Global

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="lindoglobal", lindoglobal_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver lindoglobal; # change the solver
            ampl: option lindoglobal_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Features

### Algorithms

:::{dropdown} Global: branch-and-bound with convexification
Tolerances: `epsr` and `epsa`. Time limit: `maxtime` (CPU seconds).
Threads: `threads`.
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
LINDO Global reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...), nor `complements`. Through MP2NL, MP reformulates them first.

The LINDO Global driver includes the [MP2NL](../mp2nl/index.md) bridge: set `mp2nl=1` in `lindoglobal_options`. MP's own options (`cvt:...`, `sol:chk:...`) then go into the AMPL option `mp_options`.

MP reformulates logic with binary variables, which LINDO Global handles as integer variables.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="lindoglobal", lindoglobal_options="mp2nl=1", mp_options="cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver lindoglobal;
ampl: option lindoglobal_options 'mp2nl=1';
ampl: option mp_options 'cvt:compl=1';
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

LINDO Global solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```
