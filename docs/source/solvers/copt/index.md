(copt)=

# COPT

Cardinal Optimizer (COPT) incorporates a full suite of solvers for
linear, (non-)convex quadratic, second-order and exponential conic mixed-integer programming.
It ranks at the top of benchmark tests on continuous linear programs,
and has been fully extended to handle integer variables.
The driver is built on the [MP library](https://mp.ampl.com/), which reformulates
logical and other expressions that the solver does not accept natively.


[Product Page](https://ampl.com/products/solvers/solvers-we-sell/copt/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features guide](https://mp.ampl.com/features-guide.html)
| [Options](#solver-options)
| [Changes](changes.md)

[Download COPT](https://ampl.com/download/copt)
| [Start a COPT Trial Now!](https://ampl.com/trial/copt)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install copt # install COPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="copt", copt_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis_ampls.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver copt; # change the solver
            ampl: option copt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Important features](https://mp.ampl.com/features-guide.html#important-features)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/copt)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP, (non-)convex QP, (non-)convex QCP, conic programs (SOCP, exponential
  cones)
* MILP, (non-)convex MIQP, (non-)convex MIQCP, mixed-integer conic programs
* NLP (local)
* MINLP (approximated)
:::

:::{dropdown} LP: simplex, barrier, PDLP
`alg:method`: `-1` automatic (default), `1` dual simplex, `2` barrier,
`4` concurrent, `5` simplex or barrier, `6` first-order (PDLP). GPU for
barrier and PDLP: `alg:gpumode` (CUDA, Windows and Linux).
:::

:::{dropdown} MIP and nonconvex quadratic models: branch-and-cut
Relative gap: `mip:gap`. For continuous nonconvex quadratic models,
`alg:nonconvex`: `-1` default (as of COPT 8 a local search), `1` local,
`2` global. Nonlinear functions other than quadratic are
[approximated piecewise-linearly](https://mp.ampl.com/modeling-expressions.html#piecewise-linear-approximation)
by default, which allows approximate solving of MINLP.
:::

:::::{dropdown} Nonlinear models: local
With `acc:_expr=1`, nonlinear functions (`exp`, `log`, trigonometric,
powers, divisions) are passed to COPT natively as expressions, and its
barrier returns a locally optimal solution (`solve_result` `solved?`,
message "locally optimal solution"); on a nonconvex model, different
starting points can give different local optima. For the continuous
relaxation of an MINLP, add `alg:relax=1`. With the default `acc:_expr=0`,
these functions are approximated piecewise-linearly instead.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="copt", copt_options="acc:_expr=1 outlev=1")  # local NLP
print(ampl.solve_result, ampl.get_value("solve_message"))
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver copt;
ampl: option copt_options 'acc:_expr=1 outlev=1';  # local NLP
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

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

COPT solve result codes can be obtained by running `copt -!` or `ampl: shell "copt -!";`:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
