(mosek)=

# Mosek

Mosek is a versatile linear, quadratic, quadratically constrained and conic optimizer that supports continuous and discrete variables.
The framework used by the driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/mosek/)]
[[Modeling guide](https://mp.ampl.com/model-guide.html)]
[[Options](#solver-options)]
[[Changes](changes.md)]
[[Download MOSEK](https://portal.ampl.com/user/ampl/download/mosek)]

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver mosek; # change the solver
            ampl: option mosek_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install mosek # install MOSEK

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="mosek", mosek_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_
```

## At a glance

### Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/mosek)

### Features

* Problem types: 

  * LP, QP, QCP, conic programs (SOCP, exponential cones)
  * MIP, MIQP, MIQCP, mixed-integer conic programs

* Features for all models:
    * Problem input
        * [Basis IO](https://mp.ampl.com/features-guide.html#input-and-output-basis)
        * [Warm start](https://mp.ampl.com/features-guide.html#warm-start)

    * Model investigation

        * [Sensitivity analysis](https://mp.ampl.com/features-guide.html#sensitivity-analysis)

    * Dealing with infeasibility/unboundedness
    
        * [Unbounded rays](https://mp.ampl.com/features-guide.html#unbounded-rays)



* Features for MIP models:
    * Model investigation
      * [Return MIP gap](https://mp.ampl.com/features-guide.html#return-mip-gap)
      * [Return best dual bound](https://mp.ampl.com/features-guide.html#return-best-dual-bound)
      

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

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).


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
```
Solve result table for MOSEK 10.2.0
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
