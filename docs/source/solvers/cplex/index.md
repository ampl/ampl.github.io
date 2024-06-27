(cplex)=

# IBM CPLEX

IBM ILOG CPLEX has been a well known and widely used large-scale solver for over three decades. Its efficiency and robustness have been demonstrated through varied applications in thousands of commercial installations worldwide.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/cplex/)]
[[Options](#solver-options)]
[[Changes](changes.md)]
[[Download CPLEX](https://portal.ampl.com/user/ampl/download/cplex)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        CPLEX options consist of a single-word option, or an option followed by an = sign and a value; a space may be used as a separator in place of the =.

        .. code-block:: ampl

            ampl: option solver cplex; # change the solver
            ampl: option cplex_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
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

* [Solver options](#solver-options)
* [Using with callbacks](https://ampls.ampl.com/)

## Solver options

Full list of solver options:
```{toctree}
options.md
```
```{toctree}
:hidden:
cplexmp.md
```

## Changelog

```{toctree}
changes.md
```
```{toctree}
:hidden:
changesmp.md
```
