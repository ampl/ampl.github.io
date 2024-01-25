# LINDO Global Solver

LINDO Global is a versatile nonlinear optimizer that supports global optimization in continuous and discrete variables. It accepts a variety of objective and constraint functions, including many that are nonconvex and nonsmooth.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/lindoglobal/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download LINDO Global](https://portal.ampl.com/user/ampl/download/lindoglobal)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver lindoglobal; # change the solver
            ampl: option lindoglobal_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install lindoglobal # install LINDO Global

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="lindoglobal", lindoglobal_options="option1=value1 option2=value2")
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