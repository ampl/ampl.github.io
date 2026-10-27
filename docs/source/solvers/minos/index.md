(minos)=

# MINOS

MINOS is an established choice for both linear and nonlinear optimization problems. It incorporates proven methods for large-scale sparse nonlinear constraints, and its methods are especially effective for nonlinear objectives subject to linear and near-linear constraints.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/minos/)
| [Options](options.md)
| [Changes](changes.md)

[Download MINOS](https://ampl.com/download/minos)
| [Start a MINOS Trial Now!](https://ampl.com/trial/minos)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install minos # install MINOS

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="minos", minos_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver minos; # change the solver
            ampl: option minos_options 'option1=value1 option2=value2'; # specify options
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
