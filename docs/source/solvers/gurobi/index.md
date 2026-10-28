(gurobi)=

# Gurobi

Gurobi is a powerful commercial suite of optimization products, which include simplex, parallel and nonlinear barrier, and primal-dual hybrid gradient (PDHG) solvers to handle linear programming (LP), quadratic programming (QP), and nonlinear programming (NLP);
also quadratically constrained (QCP, SOCP) and the mixed-integer variations thereof (MILP, MIQP, MIQCP, MISOCP, MINLP).
The (MI)NLP capability is provided via nonlinear expressions (formulas).
The [MP Library](https://mp.ampl.com/) used by the AMPL Gurobi driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/gurobi/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features](#features)
| [Options](#gurobi-options)
| [Changes](changes.md)

[Download Gurobi](https://ampl.com/download/gurobi)
| [Start a Gurobi Trial Now!](https://ampl.com/trial/gurobi)

Our enhanced Gurobi driver is now the default. The new driver provides significantly extended modeling support for logical and nonlinear operators natively through Gurobi’s built-in nonlinear and “general constraints” and through linearizations performed by the [MP Library](https://mp.ampl.com/). There are two binaries in this package: `gurobi` [[options](options.md)] is the new version, `gurobiasl` [[options](gurobiasl)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install gurobi # install Gurobi

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="gurobi",
                       gurobi_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis_ampls.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver gurobi;                  # Select solver
            ampl: option gurobi_options 'option1=value1 option2=value2';
            ampl: solve;
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Features](#features)
* [Gurobi options](#gurobi-options)
* [Solve result codes](#retrieve-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/gurobi)
* [Using with callbacks](https://ampls.ampl.com/)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP, QP, QCP, SOCP, NLP
* MILP, MIQP, MIQCP, MISOCP, MINLP

Passed to Gurobi natively: quadratic terms, and as general constraints or
expressions `min`, `max`, `abs`, `and`, `or`, indicator constraints, `exp`,
`log`, logistic, `sin`, `cos`, `tan`, `tanh`, `pow` and `signpow`
(`acc:...` options; see the
[modeling guide](https://mp.ampl.com/model-guide.html) for the others).
:::

:::{dropdown} LP and convex QP: simplex, barrier, PDHG
`alg:method`: `-1` automatic (default), `0` primal simplex, `1` dual simplex,
`2` barrier, `3`/`4` concurrent, `6` PDHG (first-order). PDHG on a GPU:
`alg:pdhggpu=1`. After barrier, `bar:crossover=0` returns the interior
solution without a basis.
:::

:::{dropdown} MIP: branch-and-cut
Relative and absolute gaps: `mip:gap`, `mip:gapabs`. Search focus:
`mip:focus`. Most other controls are `mip:...` and `cut:...` options.
:::

:::{dropdown} Nonconvex and nonlinear models: global
Nonconvex quadratic terms and nonlinear functions are solved to global
optimality by spatial branch-and-bound (`qp:nonconvex`, default `-1`).
Gurobi's piecewise-linear approximation of nonlinear functions remains
available with `pre:funcnonlinear=-1 acc:_expr=0`.
:::

:::::{dropdown} Nonlinear models: local
`alg:optimalitytarget=1` uses Gurobi's nonlinear barrier, which returns a
local optimum without a gap. Only for continuous models: add `alg:relax=1`
to solve the relaxation of a model with integer variables. Its iteration
limit `nlbar:iterlim` (default 1000) can stop large models before a
feasible point; raise it together with `lim:time`.

::::{tab-set}
:::{tab-item} Python
```python
ampl.solve(solver="gurobi", gurobi_options="optimalitytarget=1 nlbar:iterlim=100000")
```
:::
:::{tab-item} AMPL
```ampl
ampl: option solver gurobi;
ampl: option gurobi_options 'optimalitytarget=1 nlbar:iterlim=100000';
ampl: solve;
```
:::
::::
:::::

### Solver features

For the options used most often, such as time limits, gaps and tolerances,
see the [MP options overview](https://mp.ampl.com/features-guide.html#important-features).

```{include} features.inc
```

## Gurobi options

Full list of AMPL/Gurobi options:
```{toctree}
options.md
```
```{toctree}
:hidden:
gurobiasl.md
```

Many solver parameters can be changed directly from AMPL, by specifying them as a space-separated string in the [AMPL option](https://dev.ampl.com/ampl/reference/options.html) `gurobi_options`, or `mp_options`. 
A list of all supported solver options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        .. code-block:: python

            import os
            exit_code = os.system("gurobi -=")

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: shell "gurobi -=";

   .. tab-item:: Shell

        .. code-block:: bash

            $ gurobi -=
```


Solver options can have multiple aliases, to accomodate for different user types. 
The main nomenclature is given first in the `-=` output, then followed by aliases in brackets,
 see for example the listing for `lim:iter`:

```
lim:iter (iterlim, iterlimit)
      Iteration limit (default: no limit).
```

The main nomenclature contains a prefix (`lim:` in this case) to help categorize and find the 
options relevant to a context. To list only the options with a specific prefix (`lim:` for this example), 
run:

```
gurobi -=lim:
```

More details on solver options: [MP solver options](https://mp.ampl.com/features-guide.html#solver-options).

## Specify solver options and solve

After formulating the model in AMPL, execute the following to select `gurobi` as the solver and pass the two options:
`return_mipgap=3` and `outlev=1`.


```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        .. code-block:: python

            ampl.option["show_stats"] = 2
            ampl.solve(solver="gurobi",
                mp_options="return_mipgap=3 outlev=1",     # or: gurobi_options
                verbose=True)

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver gurobi;                    # Select solver
            ampl: option mp_options 'return_mipgap=3 outlev=1';
            ampl: solve [>output.log];                     # Solve [redirect output]
            
   .. tab-item:: Shell

        .. code-block:: bash

            $ [auxfiles=rc] ampl -obmodel snapshot.run     # Produce an NL file
                                                           # [with name files]
            $ mp_options='lim:time=100' gurobi model       # Version 1
            $ gurobi_options='kappa_exact=1' gurobi model  # Version 2
            $ gurobi model lim:time=100 wantsol=7          # Version 3
```

## Retrieve solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the related message in
`solve_result`.

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        .. code-block:: python
        
            print(ampl.solve_result, ampl.solve_result_num)
            ROI_Values = ampl.var['ROI_Level'].to_pandas()
            
            ampl.param["a"] = ampl2.var["x"].get_values()
            ampl.eval(r" x >(“obj” & n & “.out”) ;")       #save solution in a .out file

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: display solve_result_num, solve_result;
            ampl: display _varname, _var, _conname, _con.slack;
            ampl: display _logconname, min {i in 1.._nlogcons} _logcon[i].val;
                                                           # Logical constraints
            ampl: display _cconname, _ccon.slack;          # Complementarities
            

   .. tab-item:: Shell

        .. code-block:: bash

            $ gurobi model lim:time=100 wantsol=6          # Print solution
            $ gurobi model timing=2 wantsol=1              # Save .sol file
                                                           # to be explored in AMPL
```


Gurobi solve result codes can be obtained by running `gurobi -!` or `ampl: shell "gurobi -!";`:
```{literalinclude} solve_results.inc
:language: none
```

:::{dropdown} Solve result codes of the legacy driver gurobiasl
```{literalinclude} solve_results_gurobiasl.inc
:language: none
```
:::

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Handle infeasibility

### Irreducible inconsistent set (IIS)

When a model is infeasible, one useful information kind is the IIS, which are subsets of constraints that are
incompatible. See the details [here](https://mp.ampl.com/features-guide.html#irreducible-inconsistent-subset-iis).


### Feasibility relaxation

Another approach to tackle infeasibilities is the feasibility relaxation to find a solution which only penalizes infeasibilities. 
See the details  [here](https://mp.ampl.com/features-guide.html#feasibility-relaxation).

## Gurobi compute server and Gurobi cloud

Gurobi supports solving your model on other machines in two alternative ways:
* [Compute server](https://www.gurobi.com/products/gurobi-compute-server/) - where a computer (or a cluster) can be configured to the specific task of solving models via Gurobi
* [Gurobi cloud](https://www.gurobi.com/products/gurobi-instant-cloud/) - where the compute server is by Gurobi itself 

To use a compute server, the option `tech:server` must be set, together with appropriate values for the `tech:server_*` options.
For Gurobi instant cloud, the options `tech:cloudid` and `tech:cloudkey` must be set, and optionally the other options `tech:cloud*`, for example:

```ampl

# Solve with compute server
option gurobi_options "tech:server=192.168.1.55";
solve;

# Solve with Gurobi instant cloud
option gurobi_options "tech:cloudid=mygurobiid tech:cloudkey=myprivatekey";
solve;
```

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesasl.md
```
