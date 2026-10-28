(mosek)=

# MOSEK

Mosek is a versatile linear, convex quadratic, convex quadratically constrained and conic optimizer that supports continuous and discrete variables.
The driver is built on the [MP library](https://mp.ampl.com/), which reformulates
logical and other expressions that the solver does not accept natively.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/mosek/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

[Download MOSEK](https://ampl.com/download/mosek)
| [Start a MOSEK Trial Now!](https://ampl.com/trial/mosek)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install mosek # install MOSEK

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="mosek", mosek_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver mosek; # change the solver
            ampl: option mosek_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/mosek)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP, convex QP, convex QCP, conic programs (SOCP, exponential cones)
* MILP, convex MIQP and MIQCP, mixed-integer conic programs

Second-order and exponential cones are recognized from their algebraic form
([conic modeling](https://mp.ampl.com/modeling-expressions.html#socp)).
:::

:::{dropdown} LP and conic: interior point, simplex
`alg:method`: `2` automatic (default), `4` interior point, `1`/`6` dual
simplex, `8`/`7` primal simplex, `3` free simplex. After the interior-point
method, `bar:basis` controls the basis computation (default: always).
:::

:::{dropdown} MIP: branch-and-cut
Relative gap: `mip:gap`.
:::

### Instrumentation

For a generic summary of the options and features used most often, see
[Important features](https://mp.ampl.com/features-guide.html#important-features)
in the MP documentation.

```{include} features.inc
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```

Many solver parameters can be changed directly from AMPL, by specifying them as a space separated string in the option `mosek_options`. 
A list of all supported options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```
mosek -=
```

or from AMPL:

```ampl
shell "mosek -=";
```

Solver options can have multiple aliases, to accomodate for different user types. 
The main numenclature is given first in the -= output, then followed by aliases in brackets,
 see for example the listing for `lim:iter`:

```
lim:iter (iterlim, iterlimit)
      Iteration limit (default: no limit).
```

The main numenclature contains a prefix (`lim:` in this case) to help categorize and find the 
options relevant to a context. To list only the options with a specific prefix (`lim:` for this example), 
run:

```
mosek -=lim:
```

More details on solver options: [MP solver options](https://mp.ampl.com/features-guide.html#solver-options).

## Specifying solver options and solving a model

After formulating the model in AMPL, execute the following to select Mosek as solver and pass the two options:
`return_mipgap=3` and `outlev=1`.

```ampl
option solver mosek;
option mosek_options "retmipgap=3 outlev=1";
solve;
```

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

Mosek solve result codes can be obtained by running `mosek -!` or `ampl: shell "mosek -!";`:
```{literalinclude} solve_results.inc
:language: none
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
