(scip)=

# SCIP

[SCIP](https://scipopt.org/) is currently one of the fastest non-commercial solvers for mixed integer programming (MIP)
and mixed integer nonlinear programming (MINLP). It is also a framework for constraint integer
programming and branch-cut-and-price. It allows for total control of the solution process and
the access of detailed information down to the guts of the solver.
The driver is built on the [MP library](https://mp.ampl.com/), which reformulates
logical and other expressions that the solver does not accept natively.

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features guide](https://mp.ampl.com/features-guide.html)
| [Options](#solver-options)
| [Changes](changes.md)

[Download SCIP](https://ampl.com/download/scip)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install scip # install SCIP

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="scip", scip_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver scip; # change the solver
            ampl: option scip_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Important features](https://mp.ampl.com/features-guide.html#important-features)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/scipmp)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP, QP, QCP, SOCP, NLP
* MILP, MIQP, MIQCP, MINLP

Nonlinear functions are passed to SCIP natively as expressions and solved
to global optimality.
:::

:::{dropdown} MIP and MINLP: branch-and-cut, spatial branch-and-bound
Relative gap: `mip:gap`. Predefined settings: `alg:emphasis` (for example
`3` feasibility, `5` optimality). Several SCIP instances in parallel (`alg:concurrent`): by default when
`tech:threads` is above 1.
:::

:::{dropdown} LP relaxations
Solved by SoPlex: `alg:method` (`s` automatic simplex, `p` primal, `d` dual).
:::

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
scip-cpx.md
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

SCIP solve result codes can be obtained by running `scip -!` or `ampl: shell "scip -!";`:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
