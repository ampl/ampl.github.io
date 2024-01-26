# GCG

[GCG](https://gcg.or.rwth-aachen.de/) is a generic decomposition solver for mixed-integer programs (MIPs).
It automatically performs a Dantzig-Wolfe reformulation and runs a full-fledged
branch-price-and-cut algorithm to solve it to optimality. Alternatively,
GCG is able to automatically apply a Benders decomposition.
No user interaction is necessary, thus GCG provides decomposition-based MIP solving technology to everyone.

[[Read More](https://ampl.com/products/solvers/open-source-solvers/)]
[[GCG modeling guide](#gcg-modeling-guide)]
[[Options](#solver-options)]
[[Changes](changes.md)]
[[Download GCG](https://portal.ampl.com/user/ampl/download/gcg)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver gcg; # change the solver
            ampl: option gcg_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install gcg # install GCG

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="gcg", gcg_options="option1=value1 option2=value2")

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

- [GCG](#gcg)
  - [How to use it](#how-to-use-it)
  - [Resources](#resources)
  - [GCG modeling guide](#gcg-modeling-guide)
  - [Solver options](#solver-options)
  - [Retrieving solutions](#retrieving-solutions)
  - [Changelog](#changelog)

## GCG modeling guide

GCG can apply Dantzig-Wolfe or Benders decomposition,
either automatically or user-controlled,
see
[types of structures GCG can detect](https://gcg.or.rwth-aachen.de/doc/structure-types.html)
and
[AMPL/GCG Colab examples](https://colab.ampl.com/tags/gcg.html#tag-gcg).

Moreover, AMPL logical and some nonlinear expressions can be
automatically linearized by the driver,
see [MP modeling guide](https://mp.ampl.com/model-guide.html).

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

GCG solve result codes can be obtained by running `gcg -!` or `ampl: shell "gcg -!";`:
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
