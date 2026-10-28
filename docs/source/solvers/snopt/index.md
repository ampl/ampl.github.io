(snopt)=

# SNOPT

SNOPT is a widely used large-scale optimizer for difficult large-scale nonlinear problems. It incorporates proven methods that have wide applicability and are especially effective for nonlinear problems whose functions and gradients are expensive to evaluate.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/snopt/)
| [Features](#features)
| [Options](options.md)
| [Changes](changes.md)

[Download SNOPT](https://ampl.com/download/snopt)
| [Start a SNOPT Trial Now!](https://ampl.com/trial/snopt)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install snopt # install SNOPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="snopt", snopt_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver snopt; # change the solver
            ampl: option snopt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Features

### Algorithms

:::{dropdown} Sequential quadratic programming (local)
SNOPT is an SQP method with a quasi-Newton Hessian, suited to models whose
functions and gradients are expensive; it returns local optima and treats
integer variables as continuous. LPs and QPs go to SQOPT (`qpcheck`).
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
SNOPT reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...), nor `complements`. Through MP2NL, MP reformulates them first.

Call [MP2NL](../mp2nl/index.md) as the solver and name SNOPT inside it; MP's options go into `mp2nl_options`, SNOPT's own into `snopt_options`.

SNOPT is a continuous solver: it relaxes the binary variables that MP uses for logical constraints, and the result can violate the logic (MP's solution check then reports it). Use it for constructs that need no binaries, such as complementarity with a smooth reformulation (`cvt:compl=1` or `2`); use an MINLP solver for models with logic.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="mp2nl", mp2nl_options="solver=snopt cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver mp2nl;
ampl: option mp2nl_options 'solver=snopt cvt:compl=1';
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

SNOPT solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```
