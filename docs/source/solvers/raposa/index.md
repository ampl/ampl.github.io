(raposa)=

# RAPOSa

RAPOSa is a global optimization solver, specifically designed for mixed-integer polynomial programming problems with box-constrained variables. Written entirely in C++, it is based on the Reformulation-Linearization Technique developed by Hanif D. Sherali and Cihan H. Tuncbilek, and subsequently improved by Hanif D. Sherali, Evrim Dalkiran and collaborators.

[Learn More](https://raposa.usc.es)
| [Options](options.md)
| [Download](https://raposa.usc.es/download/)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="raposa", raposa_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver raposa; # change the solver
            ampl: option raposa_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Features

### Algorithms

:::{dropdown} Global: reformulation-linearization
RAPOSa solves polynomial (mixed-integer) models with bounded variables by
the reformulation-linearization technique. Time limit: `maxtime` (default
300). Subsolvers: `linsolver` (LP) and `intnonlinsolver` (MINLP, for the
upper bounds).
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
RAPOSa reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...), nor `complements`. Through MP2NL, MP reformulates them first.

Call [MP2NL](../mp2nl/index.md) as the solver and name RAPOSa inside it; MP's options go into `mp2nl_options`, RAPOSa's own into `raposa_options`.

MP reformulates logic with binary variables, which RAPOSa handles as integer variables.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="mp2nl", mp2nl_options="solver=raposa cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=raposa cvt:compl=1';
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

RAPOSa solve result codes:
```{literalinclude} solve_results.inc
:language: none
```
