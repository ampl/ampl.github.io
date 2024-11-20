.. _solvers:

Solvers
=======

AMPL connects with most commercial and open-source solvers and provides
an easy way to switch between them.

.. |y| unicode:: U+2705
   :trim:

.. |n| unicode:: U+274C
   :trim:

.. |mp| raw:: html

   <a href="https://mp.ampl.com/model-guide.html" target="_blank">MP</a>

.. |br| raw:: html

   <br />

'Linear-Quadratic' Solvers
-----------------------------------------

Traditional 'linear-quadratic' solvers are advancing into the
nonlinear domain (MINLP,  *Mixed Integer NonLinear Programming*).

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

.. csv-table::
   :file: _tables/slv_lin.csv
   :header-rows: 1

.. rubric:: Footnotes

.. [#] Conic programming: Mosek supports SOCP and exponential cones, other solvers only SOCP.


Nonlinear Solvers
------------------

Nonlinear solvers traditionally target smooth problems with continuous variables.
However, some solvers accept integer variables (MINLP), and some target global optimality
(vs returning only locally optimal solutions for non-convex problems.)

.. csv-table::
   :file: _tables/slv_nonlin.csv
   :header-rows: 1

.. rubric:: Footnotes

.. [#] Global optimality: while Knitro and Bonmin accept integer variables,
   they only guarantee local optimum for non-convex models.


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
    ipopt/index
    bonmin/index
    couenne/index


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

