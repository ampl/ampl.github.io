(ipopt)=

# IPOPT

The [COIN Ipopt solver (IPOPT)](https://github.com/coin-or/Ipopt) is an open-source solver
for large-scale nonlinear continuous optimization. Ipopt uses an interior point method,
together with a filter linear search procedure.

[[Read More](https://ampl.com/products/solvers/open-source-solvers/)]
[[Options](#solver-options)]
[[Download IPOPT](https://portal.ampl.com/user/ampl/download/coin)]

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver ipopt; # change the solver
            ampl: option ipopt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install coin # install IPOPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="ipopt", ipopt_options="option1=value1 option2=value2")

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

* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)

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

IPOPT solve result codes:
```
          0- 99 solved: optimal for an optimization problem, feasible for a satisfaction problem
        100-199 solved? solution candidate returned but error likely
        200-299 infeasible
        300-399 unbounded
        400-499 limit
        500-999 failure, no solution returned
```
