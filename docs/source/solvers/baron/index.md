(baron)=

# BARON

BARON is a general nonlinear optimizer capable of solving nonconvex optimization problems to global optimality. Decision variables may be continuous, integer, or a mixture of the two. BARON has been used for applications in the chemical process industries, pharmaceuticals, energy production, engineering design, and asset management.

An experimental version of the driver, BARONMP, supports the extended modeling capabilities of the [MP library](https://mp.ampl.com/).

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/baron/)]
[[Options](options.md)]
[[BARONMP Options](baronmp.md)]
[[Changes](changes.md)]
[[BARONMP Changes](changesmp.md)]
[[Download BARON and BARONMP](https://portal.ampl.com/user/ampl/download/baron)]

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver baron; # change the solver
            ampl: option baron_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install baron # install Baron

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="baron", baron_options="option1=value1 option2=value2")

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

## Resources

* [BARONMP modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](options.md)
* [BARONMP solver options](baronmp.md)
* [BARONMP solve result codes](#retrieving-solutions)
* [BARONMP sources](https://github.com/ampl/mp/tree/develop/solvers/baronmp)

## Solver options

Full list of solver options:
```{toctree}
options.md
baronmp.md
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

BARONMP solve result codes can be obtained by running `baronmp -!` or `ampl: shell "baronmp -!";`:
```
Solve result table for BaronMP 24.10.10
          0- 99 solved: optimal for an optimization problem, feasible for a satisfaction problem
        100-199 solved? solution candidate returned but error likely
            150 solved? MP solution check failed (option sol:chk:fail)
        200-299 infeasible
            201     infeasible, IIS found
            202     infeasible, IS found, possibly not irreducible
            203     infeasible, IIS sought but not found
        300-349 unbounded, feasible solution returned
        350-399 unbounded, no feasible solution returned
        400-449 limit, feasible: stopped, e.g., on iterations or Ctrl-C
            400     node limit reached
            401     iteration limit reached
            402     CPU time limit reached
        450-469 limit, problem is either infeasible or unbounded
		Disable dual reductions or run IIS finder for definitive answer.
        470-499 limit, no solution returned
        500-999 failure, no solution returned
            500     licensing error
            501     numerical difficulties
            502     interrupted (Control-C)
            503     too little memory
            504     terminated by BARON
            505     BARON syntax error (should not happen)
            506     operation not supported by BARON
            507     Interrupted by Control-C
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).


## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesmp.md
```