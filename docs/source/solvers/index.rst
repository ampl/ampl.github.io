.. _solvers:

Solvers
=======

AMPL connects with most commercial and open-source solvers and provides
an easy way to switch between them.

.. |y| unicode:: U+2705
   :trim:

.. |n| unicode:: U+274C
   :trim:


Linear Solvers
--------------

.. toctree::
    :hidden:

    gurobi/index
    xpress/index
    cplex/index
    copt/index
    mosek/index
    highs/index
    scip/index
    gcg/index
    cbc/index
    ilogcp/index

.. csv-table::
   :file: _tables/slv_lin.csv
   :header-rows: 1

.. rubric:: Footnotes

.. [#] Conic programming: Mosek supports SOCP and exponential cones, other solvers only SOCP
.. [#] MINLP: Gurobi 11 requires the non-default setting `global=1`
.. [3] Capability added by automatic reformulations in the `MP Library <https://mp.ampl.com>`_.


Nonlinear Solvers
------------------

Nonlinear solvers traditionally target smooth problems with continuous variables.
However, some solvers accept integer variables, and some target global optimality
(vs returning only locally optimal solutions for non-convex problems.)

.. csv-table::
   :file: _tables/slv_nonlin.csv
   :header-rows: 1

.. toctree::
    :hidden:

    
    knitro/index
    baron/index
    snopt/index
    loqo/index
    minos/index
    conopt/index
    lgo/index
    lindoglobal/index
    octeract/index
    raposa/index


Constraint Programming solvers
------------------------------

.. toctree::
    :maxdepth: 1

    ilogcp/index

NEOS Server
-----------

.. toctree::
    :maxdepth: 2

    kestrel/index
