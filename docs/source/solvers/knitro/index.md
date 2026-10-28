(knitro)=

# Knitro

[Artelys Knitro](https://www.artelys.com/solvers/knitro/) is an especially powerful nonlinear solver, offering a range of state-of-the-art algorithms and options for working with both smooth and discrete objective and constraint functions in continuous and integer variables. It is designed for local optimization of large-scale problems with up to hundreds of thousands of variables.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/knitro/)
| [Features](#features)
| [Options](options.md)
| [Changes](changes.md)

[Download Knitro](https://ampl.com/download/knitro)
| [Start a Knitro Trial Now!](https://ampl.com/trial/knitro)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install knitro # install Knitro

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="knitro", knitro_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver knitro; # change the solver
            ampl: option knitro_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Features

### Algorithms

:::{dropdown} Continuous models: interior point, active set, SQP
`nlp_algorithm`: `0` automatic (default), `1` interior point (direct),
`2` interior point (CG), `3` active set (SLQP), `4` SQP, `5` several
algorithms, `6` augmented Lagrangian. Knitro returns local optima.
:::

:::{dropdown} Mixed-integer models
`mip_method`: `0` automatic, `1` branch-and-bound, `3` mixed-integer SQP.
On nonconvex models the result is a local, not a global, optimum.
:::

:::{dropdown} Multistart
`ms_enable=1` solves from several starting points and keeps the best local
optimum; `ms_maxsolves` sets how many. For MIP, `mip_multistart=1`.
:::

:::{dropdown} Threads and time
`numthreads` (parallel features), `maxtime` (seconds).
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic and counting (MP2NL)
Knitro reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...). Through MP2NL, MP reformulates them first. (Knitro accepts `complements` natively.)

The Knitro driver includes the [MP2NL](../mp2nl/index.md) bridge: set `mp2nl=1` in `knitro_options`. MP's own options (`cvt:...`, `sol:chk:...`) then go into the AMPL option `mp_options`.

MP reformulates logic with binary variables, which Knitro handles as integer variables.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="knitro", knitro_options="mp2nl=1", mp_options="cvt:bigM=1e5")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver knitro;
ampl: option knitro_options 'mp2nl=1';
ampl: option mp_options 'cvt:bigM=1e5';
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

Knitro solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```
