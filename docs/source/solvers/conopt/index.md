(conopt)=

# CONOPT

A proven choice for highly nonlinear problems, CONOPT’s efficient and reliable multi-method architecture handles a broad range of models. Specialized techniques achieve feasibility quickly, while powerful preprocessing tools reduce problem size and suggest formulation improvements.

[Product Page](https://ampl.com/products/solvers/solvers-we-sell/conopt/)
| [Options](options.md)
| [Changes](changes.md)

[Download CONOPT](https://ampl.com/download/conopt)
| [Start a CONOPT Trial Now!](https://ampl.com/trial/conopt)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
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

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver conopt; # change the solver
            ampl: option conopt_options 'option1=value1 option2=value2'; # specify options
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
