(baron)=

# BARON

BARON is a general nonlinear optimizer capable of solving nonconvex optimization problems to global optimality. Decision variables may be continuous, integer, or a mixture of the two. BARON has been used for applications in the chemical process industries, pharmaceuticals, energy production, engineering design, and asset management.

An experimental version of the driver, BARONMP, supports the extended modeling capabilities of the [MP library](https://mp.ampl.com/).

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/baron/)
| [Options](options.md)
| [BARONMP Options](baronmp.md)
| [Changes](changes.md)

[Download BARON](https://ampl.com/download/baron)
| [Start a BARON Trial Now!](https://ampl.com/trial/baron)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install baron # install Baron

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="baron", baron_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver baron; # change the solver
            ampl: option baron_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [BARONMP modeling guide](https://mp.ampl.com/model-guide.html)
* [Important features](https://mp.ampl.com/features-guide.html#important-features)
* [Solver options](options.md)
* [BARONMP solver options](baronmp.md)
* [BARONMP solve result codes](#retrieving-solutions)
* [BARONMP sources](https://github.com/ampl/mp/tree/develop/solvers/baronmp)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* NLP, MINLP, nonconvex, solved to global optimality
* LP, MILP

With BARONMP, logical and other MP expressions are reformulated by MP.
:::

:::{dropdown} Global search: branch-and-reduce
Stopping tolerances: `epsr` (relative) and `epsa` (absolute). Time limit:
`maxtime`, in CPU seconds, **default 1000**. Local searches: `numloc` in
preprocessing, `dolocal` during upper bounding. LP solver: `lpsolver`.

With BARONMP, the same controls are `alg:epsr`, `alg:epsa`, `alg:numloc`,
`alg:dolocal` and `lim:time`; the LP algorithm is `lp:alg`.
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic and counting (MP2NL)
BARON reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...). Through MP2NL, MP reformulates them first. (BARON accepts `complements` natively.)

The BARON driver includes the [MP2NL](../mp2nl/index.md) bridge: set `mp2nl=1` in `baron_options`. MP's own options (`cvt:...`, `sol:chk:...`) then go into the AMPL option `mp_options`.

MP reformulates logic with binary variables, which BARON handles as integer variables. Alternatively, BARONMP (`baronmp`) is built on MP
and accepts these expressions directly.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="baron", baron_options="mp2nl=1", mp_options="cvt:bigM=1e5")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver baron;
ampl: option baron_options 'mp2nl=1';
ampl: option mp_options 'cvt:bigM=1e5';
ampl: solve;
```
:::
::::

More: [Meta-driver MP2NL](https://mp.ampl.com/modeling-tools.html#meta-driver-mp2nl).
:::::



### Solver features (BARONMP)

```{include} features.inc
```

## Solver options

Full list of solver options:
```{toctree}
options.md
baronmp.md
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

BARONMP solve result codes can be obtained by running `baronmp -!` or `ampl: shell "baronmp -!";`:
```{literalinclude} solve_results_baronmp.inc
:language: none
```

The classic BARON driver (`baron`) uses AMPL's default ranges:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesmp.md
```