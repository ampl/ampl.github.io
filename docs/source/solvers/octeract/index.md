# Octeract

The Octeract Engine supports global optimization of mixed-integer nonlinear optimization problems. It is designed to achieve substantial speedups on very large numbers of parallel processing nodes, while also performing efficiently on multi-core shared memory architectures.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/octeract/)]
[[Download Octeract](https://portal.ampl.com/user/ampl/download/octeract)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver octeract; # change the solver
            ampl: option octeract_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
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
```