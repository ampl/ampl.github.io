(loqo)=

# LOQO

LOQO is a powerful solver for smooth constrained optimization problems, based on interior-point method applied to a sequence of quadratic approximations. Subject to the requirement that the defining functions be smooth (at the points evaluated by the algorithm), LOQO can handle a range of problems: linear or nonlinear, convex or nonconvex, constrained or unconstrained. For convex problems, LOQO finds a globally optimal solution; otherwise, it iterates from the given starting point to find a locally optimal solution.

[Learn More](https://ampl.com/products/solvers/solvers-we-sell/loqo/)
| [Options](options.md)
| [Changes](changes.md)
| [Download LOQO](https://portal.ampl.com/user/ampl/download/loqo)
| [Start a LOQO Trial Now!](https://portal.ampl.com/user/ampl/request/amplce/trial?solver=loqo)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver loqo; # change the solver
            ampl: option loqo_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install loqo # install LOQO

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="loqo", loqo_options="option1=value1 option2=value2")

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

## Options

Full list of solver options:
```{toctree}
options.md
```

## Changelog

```{toctree}
changes.md
```
