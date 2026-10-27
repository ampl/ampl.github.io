(raposa)=

# RAPOSa

RAPOSa is a global optimization solver, specifically designed for mixed-integer polynomial programming problems with box-constrained variables. Written entirely in C++, it is based on the Reformulation-Linearization Technique developed by Hanif D. Sherali and Cihan H. Tuncbilek, and subsequently improved by Hanif D. Sherali, Evrim Dalkiran and collaborators.

[Learn More](https://raposa.usc.es)
| [Options](options.md)
| [Download](https://raposa.usc.es/download/)

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="raposa", raposa_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver raposa; # change the solver
            ampl: option raposa_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Options

Full list of solver options:
```{toctree}
options.md
```

