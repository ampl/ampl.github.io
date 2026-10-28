(gecode)=

# Gecode

[Gecode](https://www.gecode.org/) (Generic Constraint Development Environment)
is an open-source constraint programming solver. It searches by constraint
propagation and branching, and solves models with integer variables:
puzzles, assignment, sequencing and other combinatorial problems. The driver
reads AMPL's logical and constraint programming expressions directly.

[Learn More](https://www.gecode.org/)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

[Download Gecode](https://ampl.com/download/gecode)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python

        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install gecode # install Gecode

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="gecode", gecode_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver gecode; # change the solver
            ampl: option gecode_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/gecode)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
Models with **integer variables only** and integer coefficients; continuous
variables and fractional objective coefficients are rejected. The objective
must be linear.

Supported in constraints: integer arithmetic (`+`, `-`, `*`, `div`, `mod`,
`abs`, `min`, `max`), comparisons including `!=`, logical operators (`and`,
`or`, `not`, `==>`, `<==>`, `exists`, `forall`), `if-then-else`, `alldiff`,
`count` and `numberof`. Not supported: `^`, `/` and other real-valued
functions; write `x*x` for a square and `div` for integer division.
:::

:::{dropdown} Propagation and branching
Constraint propagation strength: `cp:ipl` (`val`, `bnd`, `dom` or `def`,
the default for each constraint). Domain propagation (`dom`) is often worth
it for `alldiff`.

Branching: `cp:var_branching` (which variable, default `size_min`, the
smallest domain) and `cp:val_branching` (which value, default `min`).

Restarts: `cp:restart` (`none`, `constant`, `linear`, `luby`,
`geometric`), with `cp:restart_base` and `cp:restart_scale`.

```ampl
ampl: option gecode_options 'ipl=dom var_branching=afc_size_max restart=luby';
```
:::

:::{dropdown} Limits and multiple solutions
Limits: `lim:time`, `lim:nodes`, `lim:fail`, and `lim:sol` (stop after this
many solutions). `sol:count=1` returns the number of solutions found in
the `.nsol` problem suffix, and `sol:stub` writes each one to a file.
:::

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

Gecode solve result codes can be obtained by running `gecode -!` or `ampl: shell "gecode -!";`:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```
