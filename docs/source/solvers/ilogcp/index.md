# ILOG CP

IBM ILOG CP Optimizer is a generic CP-based system to model and solve scheduling problems.

[Learn More](https://ampl.com/products/solvers/solvers-we-sell/cplex/)
| [Options](options.md)
| [Changes](changes.md)
| [Download](https://portal.ampl.com)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install ilogcp # install ILOG CP

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="iglocp", ilogcp_options="option1=value1 option2=value2")

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver ilogcp; # change the solver
            ampl: option ilogcp_options 'option1=value1 option2=value2'; # specify options
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