(cplex)=

# IBM CPLEX

IBM ILOG CPLEX has been a well known and widely used large-scale solver for over three decades. Its efficiency and robustness have been demonstrated through varied applications in thousands of commercial installations worldwide.
The framework used by the driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/cplex/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Options](#solver-options)
| [Changes](changes.md)

[Download CPLEX](https://ampl.com/download/cplex)
| [Start a CPLEX Trial Now!](https://ampl.com/trial/cplex)

This package contains an all-new CPLEX driver, that provides significantly extended modeling support for logical and nonlinear operators through linearizations performed by the [MP library](https://mp.ampl.com/). For compatibility, there are two binaries in this package: `cplex` [[options](options.md)] is the new version, `cplexasl` [[options](cplexasl.md)] is the legacy version. If you are upgrading an existing installation and encounter any issues with the new version please report them to [support@ampl.com](mailto:support@ampl.com).


## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install cplex # install CPLEX

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="cplex", cplex_options="option1=value1 option2=value2")

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

        CPLEX options consist of a single-word option, or an option followed by an = sign and a value; a space may be used as a separator in place of the =.

        .. code-block:: ampl

            ampl: option solver cplex; # change the solver
            ampl: option cplex_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Important features](https://mp.ampl.com/features-guide.html#important-features)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/cplex)
* [Using with callbacks](https://ampls.ampl.com/)


## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
cplexasl.md
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).


## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

CPLEX solve result codes can be obtained by running `cplex -!` or `ampl: shell "cplex -!";`:
```
Solve result table for CPLEX 22.1.1
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


## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesasl.md
```
