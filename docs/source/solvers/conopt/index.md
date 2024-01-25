# CONOPT

A proven choice for highly nonlinear problems, CONOPT’s efficient and reliable multi-method architecture handles a broad range of models. Specialized techniques achieve feasibility quickly, while powerful preprocessing tools reduce problem size and suggest formulation improvements.

[[Read More](https://ampl.com/products/solvers/solvers-we-sell/conopt/)]
[[Options](options.md)]
[[Changes](changes.md)]
[[Download CONOPT](https://portal.ampl.com/user/ampl/download/conopt)]

## How to use it

```{eval-rst}

.. tabs::

   .. tab:: AMPL

        .. code-block:: ampl

            ampl: option solver conopt; # change the solver
            ampl: option conopt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab:: Python
   
        How to install using `amplpy <https://amplpy.ampl.com>`_:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install conopt # install CONOPT

            # Activate your license (e.g., free ampl.com/ce or ampl.com/courses licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="conopt", conopt_options="option1=value1 option2=value2")
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