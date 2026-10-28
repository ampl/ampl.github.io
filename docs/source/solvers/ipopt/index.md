(ipopt)=

# IPOPT

The [COIN Ipopt solver (IPOPT)](https://github.com/coin-or/Ipopt) is an open-source solver
for large-scale nonlinear continuous optimization. Ipopt uses an interior point method,
together with a filter linear search procedure.

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [Features](#features)
| [Options](#solver-options)

[Download IPOPT](https://ampl.com/download/coin)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install coin # install IPOPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="ipopt", ipopt_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver ipopt; # change the solver
            ampl: option ipopt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Ipopt documentation](https://coin-or.github.io/Ipopt/)

## Features

### Algorithms

:::{dropdown} Interior point (local)
Ipopt is a primal-dual interior-point method with a filter line search. It
returns local optima and treats integer variables as continuous.
Barrier update: `mu_strategy` (`monotone` or `adaptive`). Linear solver:
`linear_solver` (e.g., `mumps`; HSL solvers such as `ma27`, `ma57` where
installed). Limits: `max_iter`, `max_cpu_time`.

```ampl
ampl: option ipopt_options 'mu_strategy=adaptive max_iter=3000';
```
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
Ipopt reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...), nor `complements`. Through MP2NL, MP reformulates them first.

Call [MP2NL](../mp2nl/index.md) as the solver and name Ipopt inside it; MP's options go into `mp2nl_options`, Ipopt's own into `ipopt_options`.

Ipopt is a continuous solver: it relaxes the binary variables that MP uses for logical constraints, and the result can violate the logic (MP's solution check then reports it). Use it for constructs that need no binaries, such as complementarity with a smooth reformulation (`cvt:compl=1` or `2`); use an MINLP solver for models with logic.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="mp2nl", mp2nl_options="solver=ipopt cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=ipopt cvt:compl=1';
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

IPOPT solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

