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
    copt/index
    cplex/index
    ilogcp/index
    highs/index
    mosek/index
    xpress/index
    cbc/index
    scip/index
    gcg/index


.. csv-table::
   :file: _tables/slv_lin.csv
   :header-rows: 1

.. rubric:: Footnotes

.. [#] Conic programming: Mosek supports SOCP and exponential cones, other solvers only SOCP
.. [#] MINLP: Gurobi 11 requires the non-default setting `global=1`


Non-linear Solvers
------------------

"Nonlinear" solvers target convex problems;
non-convex problems are accepted, but only locally optimal solutions can be returned.

.. csv-table::
   :file: _tables/slv_nonlin.csv
   :header-rows: 1

.. toctree::
    :hidden:

    conopt/index
    knitro/index
    loqo/index
    minos/index
    snopt/index


Global Solvers
--------------

.. csv-table::
   :file: _tables/slv_glob.csv
   :header-rows: 1

.. toctree::
    :hidden:

    baron/index
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
