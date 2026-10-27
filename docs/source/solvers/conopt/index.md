(conopt)=

# CONOPT

A proven choice for highly nonlinear problems, CONOPT’s efficient and reliable multi-method architecture handles a broad range of models. Specialized techniques achieve feasibility quickly, while powerful preprocessing tools reduce problem size and suggest formulation improvements.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/conopt/)
| [Options](options.md)
| [Changes](changes.md)

[Download CONOPT](https://ampl.com/download/conopt)
| [Start a CONOPT Trial Now!](https://ampl.com/trial/conopt)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install conopt # install CONOPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="conopt", conopt_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver conopt; # change the solver
            ampl: option conopt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Features

### Algorithms

:::{dropdown} Generalized reduced gradient (local)
CONOPT is an active-set method (GRG with SLP and SQP phases, `flg_slpmode`,
`flg_sqpmode`); it returns local optima, and it treats integer variables
as continuous. Limits: `maxftime` (seconds), `iterlim`. `flg_convex=1`
declares the model convex.
:::

### Modeling with MP expressions

:::::{dropdown} MP expressions: logic, counting, complementarity (MP2NL)
CONOPT reads the classic NL format, without MP's expressions (`==>`, `or`, `atmost`, `count`, `alldiff`, piecewise-linear terms, ...), nor `complements`. Through MP2NL, MP reformulates them first.

The CONOPT driver includes the [MP2NL](../mp2nl/index.md) bridge: set `mp2nl=1` in `conopt_options`. MP's own options (`cvt:...`, `sol:chk:...`) then go into the AMPL option `mp_options`.

CONOPT is a continuous solver: it relaxes the binary variables that MP uses for logical constraints, and the result can violate the logic (MP's solution check then reports it). Use it for constructs that need no binaries, such as complementarity with a smooth reformulation (`cvt:compl=1` or `2`); use an MINLP solver for models with logic.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="conopt", conopt_options="mp2nl=1", mp_options="cvt:compl=1")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver conopt;
ampl: option conopt_options 'mp2nl=1';
ampl: option mp_options 'cvt:compl=1';
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

CONOPT solve result codes:
```{literalinclude} solve_results.inc
:language: none
```

## Changelog

```{toctree}
changes.md
```
