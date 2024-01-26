# COPT

Cardinal Optimizer (COPT) incorporates a full suite of solvers for
linear, convex quadratic, and second-order conic mixed-integer programming.
It ranks at the top of benchmark tests on continuous linear programs,
and has been fully extended to handle integer variables.
The framework used by the driver supports automatic reformulation for many expression types; the modeling guide can be
found [here](https://mp.ampl.com/model-guide.html).


[[Read More](https://ampl.com/products/solvers/solvers-we-sell/copt/)]
[[Modeling guide](https://mp.ampl.com/model-guide.html)]
[[Options](#solver-options)]
[[Changes](changes.md)]
[[Download COPT](https://portal.ampl.com/user/ampl/download/copt)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver copt; # change the solver
            ampl: option copt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install copt # install COPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="copt", copt_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. tab:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/copt)

## Solver options

Full list of solver options:
```{toctree}
options.md
```

More details on solver options: [Features guide](https://mp.ampl.com/features-guide.html).


## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

COPT solve result codes can be obtained by running `copt -!` or `ampl: shell "copt -!";`:
```
          0- 99 solved: optimal for an optimization problem, feasible for a satisfaction problem
        100-199 solved? solution candidate returned but error likely
            150 solved? MP solution check failed (option sol:chk:fail)
        200-299 infeasible
        300-349 unbounded, feasible solution returned
        350-399 unbounded, no feasible solution returned
        400-449 limit, feasible: stopped, e.g., on iterations or Ctrl-C
        450-469 limit, problem is either infeasible or unbounded
        470-499 limit, no solution returned
        500-999 failure, no solution returned
            550 failure: numeric issue, no feasible solution
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```