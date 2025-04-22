(octeract)=

# Octeract

The Octeract Engine supports global optimization of mixed-integer nonlinear optimization problems. It is designed to achieve substantial speedups on very large numbers of parallel processing nodes, while also performing efficiently on multi-core shared memory architectures.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/octeract/)
| [Contact Sales](https://ampl.com/contact/sales/)

[Download Octeract](https://ampl.com/download/octeract)
| [Start a Octeract Trial Now!](https://ampl.com/trial/octeract)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install octeract # install Octeract

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="octeract", octeract_options="option1=value1 option2=value2")

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

            ampl: option solver octeract; # change the solver
            ampl: option octeract_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Solver options

Octeract options differ significantly from those of other solvers and cannot be set using the `octeract -=` command. For a complete list of available options, please refer to the [Octeract Options Reference Manual](https://www.octeract.com/docs/octeract-engine-options/options-reference/).

For example, to set the MIP solver to HiGHS and the time limit to 25 seconds:
```ampl
option octeract_options 'MIP_SOLVER=HIGHS MAX_SOLVER_TIME=25';
```