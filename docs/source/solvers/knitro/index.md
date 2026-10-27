(knitro)=

# Knitro

[Artelys Knitro](https://www.artelys.com/solvers/knitro/) is an especially powerful nonlinear solver, offering a range of state-of-the-art algorithms and options for working with both smooth and discrete objective and constraint functions in continuous and integer variables. It is designed for local optimization of large-scale problems with up to hundreds of thousands of variables.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/knitro/)
| [Options](options.md)
| [Changes](changes.md)

[Download Knitro](https://ampl.com/download/knitro)
| [Start a Knitro Trial Now!](https://ampl.com/trial/knitro)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install knitro # install Knitro

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="knitro", knitro_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver knitro; # change the solver
            ampl: option knitro_options 'option1=value1 option2=value2'; # specify options
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
