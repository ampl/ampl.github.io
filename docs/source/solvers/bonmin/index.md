(bonmin)=

# BONMIN

The [COIN Bonmin solver (BONMIN)](https://coin-or.github.io/Bonmin/) is an experimental open-source C++ code for solving general MINLP (*Mixed Integer NonLinear Programming*) problems of the form:

```
   min     f(x)

s.t.       g_L <= g(x) <= g_U
           x_L <=  x   <= x_U
           x_i in Z for all i in I and,
           x_i in R for all i not in I.
```
where `f(x): R^n --> R`, `g(x): R^n --> R^m` are twice continuously differentiable functions and `I` is a subset of `{1,..,n}`.

The algorithms in Bonmin are exact when the functions `f` and `g` are convex; in the case where `f` or `g` or both are non-convex they are heuristics.

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [Features](#features)
| [Options](#solver-options)

[Download BONMIN](https://ampl.com/download/coin)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install coin # install BONMIN

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="bonmin", bonmin_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver bonmin; # change the solver
            ampl: option bonmin_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

- [BONMIN](#bonmin)
  - [How to use it](#how-to-use-it)
  - [Resources](#resources)
  - [Solver options](#solver-options)
  - [Retrieving solutions](#retrieving-solutions)

## Features

### Algorithms

:::{dropdown} Algorithms
`bonmin.algorithm`: `B-BB` (NLP-based branch-and-bound, default), `B-OA`
(outer approximation), `B-QG` (Quesada-Grossmann), `B-Hyb` (hybrid),
`B-Ecp`, `B-iFP`. Exact for convex models, heuristic otherwise. Time
limit: `bonmin.time_limit`. Ipopt options (for the NLP subproblems) are
also accepted.

```ampl
ampl: option bonmin_options 'bonmin.algorithm=B-OA bonmin.time_limit=60';
```
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
Natively, Bonmin solves smooth nonlinear models with continuous and integer variables. MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...) and `complements` are not part of its native model type: through MP2NL, MP reformulates them into it first.

Call [MP2NL](../mp2nl/index.md) as the solver and name Bonmin inside it; MP's options go into `mp2nl_options`, Bonmin's own into `bonmin_options`.

MP reformulates logic with binary variables, which Bonmin handles as integer variables.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="mp2nl", mp2nl_options="solver=bonmin cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=bonmin cvt:compl=1';
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

BONMIN solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

