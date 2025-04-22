(xpress)=

# FICO XPRESS

Xpress offers proven optimization technology for large-scale applications, with out-of-the-box
high performance on a wide range of model types.  Its ultra-efficient sparse matrix handling
and on-the-fly data compression address the largest problems, with reliable performance
even on numerically difficult or unstable problems.
The framework used by the drivers supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/xpress/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Options](#solver-options)
| [Changes](changes.md)
| [Contact Sales](https://ampl.com/contact/sales/)

[Download XPRESS](https://ampl.com/download/xpress)
| [Start a XPRESS Trial Now!](https://ampl.com/trial/xpress)

This package contains an all-new Xpress driver, that provides significantly extended modeling support for logical and nonlinear operators through linearizations performed by the [MP library](https://mp.ampl.com/). For compatibility, there are two binaries in this package: `xpress` [[options](options.md)] is the new version, `xpressasl` [[options](xpressasl.md)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install xpress # install XPRESS

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="xpress", xpress_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver xpress; # change the solver
            ampl: option xpress_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## At a glance

### Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Important features](https://mp.ampl.com/features-guide.html#important-features)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/xpress)
* [Using with callbacks](https://ampls.ampl.com/)

### Features

* Problem types: 

  * LP, QP, QCP, SOCP
  * MIP, MIQP, MIQCP, MISOCP
  * MINLP

* Features for all models:
    * Problem input
        * [Basis IO](https://mp.ampl.com/features-guide.html#input-and-output-basis)
        * [Warm start](https://mp.ampl.com/features-guide.html#warm-start)
        * [Multiple objectives](https://mp.ampl.com/features-guide.html#multiple-objectives)

    * Model investigation

        * [Multiple solutions](https://mp.ampl.com/features-guide.html#multiple-solutions)

    * Dealing with infeasibility/unboundedness
    
        * [IIS](https://mp.ampl.com/features-guide.html#irreducible-inconsistent-subset-iis)



* Features for MIP models:
    * Model investigation
      * [Return MIP gap](https://mp.ampl.com/features-guide.html#return-mip-gap)
      * [Return best dual bound](https://mp.ampl.com/features-guide.html#return-best-dual-bound)
      * [Fixed model](https://mp.ampl.com/features-guide.html#fixed-model-return-basis-for-mip)


## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
xpressasl.md
```

Many solver parameters can be changed directly from AMPL, by specifying them as a space separated string in the option `xpress_options`. 
A list of all supported options is available [here](options.md) or can be obtained by executing the solver driver with the `-=` command line parameter:

```
xpress -=
```

or from AMPL:

```ampl
shell "xpress -=";
```

Solver options can have multiple aliases, to accomodate for different user types. 
The main numenclature is given first in the -= output, then followed by aliases in brackets,
 see for example the listing for `lim:time`:

```
lim:time (timelim, timelimit)
      Limit on solve time (in seconds; default: no limit).
```

The main numenclature contains a prefix (`lim:` in this case) to help categorize and find the 
options relevant to a context. To list only the options with a specific prefix (`lim:` for this example), 
run:

```
xpress -=lim:
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).


## Specifying solver options and solving a model

After formulating the model in AMPL, execute the following to select xpress as solver and pass the two options:
`return_mipgap=3` and `outlev=1`.

```ampl
option solver xpress;
option xpress_options "retmipgap=3 outlev=1";
solve;
```

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

Xpress solve result codes can be obtained by running `xpress -!` or `ampl: shell "xpress -!";`:
```
Solve result table for XPRESS 9.4.2 (43.01.03)
	  0- 99	solved: optimal for an optimization problem,
		feasible for a satisfaction problem 
	100-199	solved? solution candidate returned but error likely 
	    150	solved? MP solution check failed (option sol:chk:fail) 
	200-299	infeasible 
	300-349	unbounded, feasible solution returned 
	350-399	unbounded, no feasible solution returned 
	400-449	limit, feasible: stopped, e.g., on iterations or Ctrl-C 
	450-469	limit, problem is either infeasible or unbounded.
		Disable dual reductions or run IIS finder for definitive answer.
	470-499	limit, no solution returned 
	500-999	failure, no solution returned 
	    550	failure: numeric issue, no feasible solution
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Handling infeasibility

### IIS

When a model is unfeasible, one usedful information is finding the irreducible inconsistent sets, which are subsets of constraints that are
incompatible. This is supported by the framework, see the description [here](https://mp.ampl.com/features-guide.html#irreducible-inconsistent-set-iis).

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesasl.md
```
