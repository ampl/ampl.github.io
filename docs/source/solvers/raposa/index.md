(raposa)=

# RAPOSa

RAPOSa is a global optimization solver, specifically designed for mixed-integer polynomial programming problems with box-constrained variables. Written entirely in C++, it is based on the Reformulation-Linearization Technique developed by Hanif D. Sherali and Cihan H. Tuncbilek, and subsequently improved by Hanif D. Sherali, Evrim Dalkiran and collaborators.

[[Read More](https://raposa.usc.es)]
[[Options](options.md)]
[[Download](https://raposa.usc.es/download/)]

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver raposa; # change the solver
            ampl: option raposa_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem

   .. tab-item:: Python

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="raposa", raposa_options="option1=value1 option2=value2")

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. tab-item:: Other APIs

        `AMPL APIs <https://ampl.com/apis/>`_ are interfaces that allow developers to access the features of the AMPL interpreter from within a programming language. We have APIs available for:

        - `Python <https://ampl.com/api/latest/python>`_
        - `R <https://ampl.com/api/latest/R>`_
        - `C++ <https://ampl.com/api/latest/cpp>`_
        - `C#/.NET <https://ampl.com/api/latest/dotnet>`_
        - `Java <https://ampl.com/api/latest/java>`_
        - `MATLAB <https://ampl.com/api/latest/matlab>`_
```

## Options

Full list of solver options:
```{toctree}
options.md
```

