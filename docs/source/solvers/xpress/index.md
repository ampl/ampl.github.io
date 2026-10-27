(xpress)=

# FICO XPRESS

Xpress offers proven optimization technology for large-scale applications, with out-of-the-box
high performance on a wide range of model types.  Its ultra-efficient sparse matrix handling
and on-the-fly data compression address the largest problems, with reliable performance
even on numerically difficult or unstable problems.
The [MP Library](https://mp.ampl.com/) used by the AMPL Xpress driver supports automatic
reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/xpress/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features guide](https://mp.ampl.com/features-guide.html)
| [Options](#solver-options)
| [Changes](changes.md)

[Download XPRESS](https://ampl.com/download/xpress)
| [Start a XPRESS Trial Now!](https://ampl.com/trial/xpress)

This package contains an all-new Xpress driver, that provides significantly extended modeling support for logical and nonlinear operators through linearizations performed by the [MP library](https://mp.ampl.com/). For compatibility, there are two binaries in this package: `xpress` [[options](options.md)] is the new version, `xpressasl` [[options](xpressasl.md)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install xpress # install XPRESS

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="xpress", xpress_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis_ampls.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver xpress; # change the solver
            ampl: option xpress_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Important features](https://mp.ampl.com/features-guide.html#important-features)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/xpress)
* [Using with callbacks](https://ampls.ampl.com/)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP, QP, QCP, SOCP, NLP
* MILP, MIQP, MIQCP, MISOCP, MINLP

Nonlinear functions are passed to Xpress natively as expressions
(`acc:_expr=1`, the default).
:::

:::{dropdown} LP and convex QP: simplex, barrier, hybrid gradient
`alg:method`: `1` automatic (default), `2` dual simplex, `3` primal simplex,
`4` barrier. The primal-dual hybrid gradient method (first-order) is
`alg:method=4 bar:alg=4`, on a GPU with `pdhg:barhggpu=1`.
:::

:::{dropdown} MIP: branch-and-cut
Relative gap: `mip:gap`. Most other controls are `mip:...` and `cut:...`
options.
:::

:::::{dropdown} Nonlinear models: global or local
* **Global** (default, `alg:nlpsolver=-1`): FICO Xpress Global, if the
  license allows and the model has no user functions; otherwise a local
  solver. Force it with `alg:nlpsolver=2`.
* **Local**: `alg:nlpsolver=1` uses the local solver chosen by
  `alg:localsolver`: `0` Xpress-SLP (always available), `1` Knitro (only if
  Knitro is installed for Xpress), `2` the Xpress Optimizer (convex
  quadratic problems only); the default `-1` chooses automatically. The
  result is a locally optimal solution (`solve_result` `solved?`, message
  "locally optimal solution"); different starting points can give different
  local optima.
* `alg:global=0` linearizes the expressions that require Xpress Global.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="xpress", xpress_options="nlpsolver=1 localsolver=0")  # local, SLP
ampl.solve(solver="xpress", xpress_options="nlpsolver=2")                # global
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver xpress;
ampl: option xpress_options 'nlpsolver=1 localsolver=0';  # local, SLP
ampl: solve;
```
:::
::::
:::::

### Solver features

```{include} features.inc
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
xpressasl.md
```

Many solver parameters can be changed directly from AMPL, by specifying them as a space separated string in the option `xpress_options`. 
A list of all supported options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```
xpress -=
```

or from AMPL:

```ampl
shell "xpress -=";
```

Solver options can have multiple aliases, to accomodate for different user types. 
The main numenclature is given first in the -= output, then followed by aliases in brackets,
 see for example the listing for `lim:time`:

```
lim:time (timelim, timelimit)
      Limit on solve time (in seconds; default: no limit).
```

The main numenclature contains a prefix (`lim:` in this case) to help categorize and find the 
options relevant to a context. To list only the options with a specific prefix (`lim:` for this example), 
run:

```
xpress -=lim:
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).

## Specifying solver options and solving a model

After formulating the model in AMPL, execute the following to select xpress as solver and pass the two options:
`return_mipgap=3` and `outlev=1`.

```ampl
option solver xpress;
option xpress_options "retmipgap=3 outlev=1";
solve;
```

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

Xpress solve result codes can be obtained by running `xpress -!` or `ampl: shell "xpress -!";`:
```{literalinclude} solve_results.inc
:language: none
```

:::{dropdown} Solve result codes of the legacy driver xpressasl
```{literalinclude} solve_results_xpressasl.inc
:language: none
```
:::

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Handling infeasibility

### IIS

When a model is unfeasible, one usedful information is finding the irreducible inconsistent sets, which are subsets of constraints that are
incompatible. This is supported by the framework, see the description [here](https://mp.ampl.com/features-guide.html#irreducible-inconsistent-subset-iis).

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesasl.md
```
