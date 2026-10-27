(cpsat)=

# CP-SAT

[CP-SAT](https://developers.google.com/optimization/cp/cp_solver) is the
constraint programming solver of Google OR-Tools. It combines a SAT solver
with lazy clause generation, linear relaxations and large neighborhood
search, and solves models with integer variables: scheduling, assignment,
timetabling and other combinatorial problems. The driver is built on the
[MP library](https://mp.ampl.com/): logical and counting constraints are passed
to CP-SAT natively, and other expressions are reformulated.

[Learn More](https://developers.google.com/optimization/cp)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features guide](https://mp.ampl.com/features-guide.html)
| [Options](#solver-options)
| [Changes](changes.md)

[Download CP-SAT](https://portal.ampl.com)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python

        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install cpsat # install CP-SAT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="cpsat", cpsat_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver cpsat; # change the solver
            ampl: option cpsat_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Important features](https://mp.ampl.com/features-guide.html#important-features)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/cpsat)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
Models with **integer variables only**; continuous variables are rejected
("CP-SAT supports integer variables only"). Fractional coefficients are
accepted. Finite bounds on the variables help the search.

Passed to CP-SAT natively: linear constraints and objectives, `alldiff`,
counting (`count`, `numberof`, `atmost`, `atleast`, `exactly`), `if-then-else`,
implications (`==>`), `and`/`forall`, `or`/`exists`, `min`, `max`, `abs`,
products and integer powers of variables, `div` and `mod`. MP reformulates
other expressions where possible. Real-valued functions (`/`, `exp`, `log`,
...) need continuous variables and are therefore rejected. See the
[modeling guide](https://mp.ampl.com/model-guide.html) and the
[acceptance options](https://mp.ampl.com/modeling-tools.html#acceptance-options)
(`cpsat -=acc:`).
:::

:::{dropdown} Search
CP-SAT runs a portfolio of search workers in parallel (`tech:threads`,
default `0`: automatic). `tech:seed` changes the random seed, which can change
the search noticeably.

```ampl
ampl: option cpsat_options 'threads=8 timelim=60 outlev=1';
```
:::

:::{dropdown} Linear relaxation
`alg:linearization` sets how much of the model CP-SAT also keeps as a linear
relaxation (0 none, 1 some constraints, the default, 2 full), which gives bounds and guides the search. Level 2 can
help models that are mostly linear, at a cost per search node.
:::

:::{dropdown} Search log
`tech:outlev=1` prints the CP-SAT log; `tech:logfile` writes it to a file,
whatever `tech:outlev` is.
:::

### Solver features

```{include} features.inc
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

CP-SAT solve result codes can be obtained by running `cpsat -!` or `ampl: shell "cpsat -!";`:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
