# Knitro

Artelys Knitro is an especially powerful nonlinear solver, offering a range of state-of-the-art algorithms and options for working with smooth objective and constraint functions in continuous and integer variables. It is designed for local optimization of large-scale problems with up to hundreds of thousands of variables.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/knitro/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download Knitro](https://portal.ampl.com/user/ampl/download/knitro)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver knitro; # change the solver
            ampl: option knitro_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install knitro # install Knitro

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="knitro", knitro_options="option1=value1 option2=value2")
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