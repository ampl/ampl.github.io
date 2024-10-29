(baron)=

# BARON

BARON is a general nonlinear optimizer capable of solving nonconvex optimization problems to global optimality. Decision variables may be continuous, integer, or a mixture of the two. BARON has been used for applications in the chemical process industries, pharmaceuticals, energy production, engineering design, and asset management.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/baron/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download BARON](https://portal.ampl.com/user/ampl/download/baron)]

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

## Options

Full list of solver options:
```{toctree}
options.md
```

## Changelog

```{toctree}
changes.md
```
