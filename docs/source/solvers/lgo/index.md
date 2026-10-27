(lgo)=

# LGO

LGO is capable of determining high-quality solutions to global optimization problems with continuous variables that have (possibly many) locally optimal solutions. Because LGO makes only limited assumptions as to problem structure and differentiability, it can be applied in a broad range of design and operational applications.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/lgo/)
| [Options](options.md)

[Download LGO](https://ampl.com/download/lgo)
| [Start a LGO Trial Now!](https://ampl.com/trial/lgo)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install lgo # install LGO

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="lgo", lgo_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver lgo; # change the solver
            ampl: option lgo_options 'option1=value1 option2=value2'; # specify options
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
