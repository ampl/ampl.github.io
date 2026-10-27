(lindo-global-solver)=

# LINDO Global Solver

LINDO Global is a versatile nonlinear optimizer that supports global optimization in continuous and discrete variables. It accepts a variety of objective and constraint functions, including many that are nonconvex and nonsmooth.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/lindoglobal/)
| [Options](options.md)
| [Changes](changes.md)

[Download LINDO Global](https://ampl.com/download/lindoglobal)
| [Start a LINDO Global Trial Now!](https://ampl.com/trial/lindoglobal)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install lindoglobal # install LINDO Global

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="lindoglobal", lindoglobal_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver lindoglobal; # change the solver
            ampl: option lindoglobal_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
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
