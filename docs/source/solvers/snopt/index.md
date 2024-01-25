# SNOPT

SNOPT is a widely used large-scale optimizer for difficult large-scale nonlinear problems. It incorporates proven methods that have wide applicability and are especially effective for nonlinear problems whose functions and gradients are expensive to evaluate.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/snopt/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download SNOPT](https://portal.ampl.com/user/ampl/download/snopt)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver snopt; # change the solver
            ampl: option snopt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install snopt # install SNOPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="snopt", snopt_options="option1=value1 option2=value2")
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