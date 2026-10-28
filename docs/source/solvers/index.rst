.. _solvers:

Solvers
=======

AMPL connects with most commercial and open-source solvers and provides
an easy way to switch between them.

.. |y| unicode:: U+2705
   :trim:

.. |n| unicode:: U+274C
   :trim:

.. |a| unicode:: U+2248
   :trim:

.. |mp| raw:: html

   <a href="https://mp.ampl.com/model-guide.html" target="_blank">MP</a>

.. |br| raw:: html

   <br />

.. toctree::
   :hidden:
   :caption: Linear and mixed-integer

   gurobi/index
   xpress/index
   cplex/index
   copt/index
   cuopt/index
   mosek/index
   highs/index
   scip/index
   gcg/index
   cbc/index

.. toctree::
   :hidden:
   :caption: Global nonlinear

   baron/index
   lindoglobal/index
   couenne/index
   raposa/index
   lgo/index

.. toctree::
   :hidden:
   :caption: Local nonlinear

   knitro/index
   conopt/index
   ipopt/index
   bonmin/index
   snopt/index
   minos/index
   loqo/index

.. toctree::
   :hidden:
   :caption: Constraint programming

   cpsat/index
   gecode/index
   ilogcp/index

.. toctree::
   :hidden:
   :caption: Complementarity

   path/index

.. toctree::
   :hidden:
   :caption: Meta-driver and NEOS

   mp2nl/index
   kestrel/index

Linear and Mixed-Integer Solvers
--------------------------------

Linear and mixed-integer solvers are advancing into the
nonlinear domain (MINLP,  *Mixed Integer NonLinear Programming*).
Which constraints and expressions each MP-based driver receives natively is
compared in the MP documentation:
`native constraints and expressions by driver <https://mp.ampl.com/modeling-tools.html#full-cons-list>`_.

.. csv-table::
   :file: _tables/slv_lin.csv
   :header-rows: 1

.. rubric:: Footnotes

.. [1] GPU-accelerated algorithms, such as `PDLP <https://ampl.com/cuPDLP>`_, are available.
.. [2] Conic programming: MOSEK and COPT support SOCP and `exponential cones <https://amplopt.streamlit.app/Logistic_Regression>`_, other solvers only SOCP.
.. [3] Approximated: quadratic or nonlinear terms that the solver does not accept natively are approximated by `piecewise-linear functions <https://mp.ampl.com/modeling-expressions.html#piecewise-linear-approximation>`_.
.. [4] COPT solves NLP to local optimality.

.. _nonlinear-solvers:

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
.. [#mp2nl] With the :ref:`MP2NL meta-driver <mp2nl>`, built into the Knitro, CONOPT and
   LINDO Global drivers (option ``mp2nl=1``).

.. _cp-solvers:

Constraint Programming Solvers
------------------------------

Constraint programming solvers search over integer variables by propagation
and branching, and receive logical and counting constraints directly. The
same AMPL constructs are reformulated for MIP solvers by the
`MP library <https://mp.ampl.com/model-guide.html>`_, so a constraint
programming model can also be solved by the solvers above.

.. csv-table::
   :file: _tables/slv_cp.csv
   :header-rows: 1

.. rubric:: Footnotes

.. [#gecode] Gecode: ``*``, ``div``, ``mod``, ``abs``, ``min``, ``max``; no ``^``.
.. [#ilogcp] ILOG CP: a model with continuous variables is passed to CPLEX
   if it is linear and has no logical constraints (option ``optimizer``).

Complementarity Solvers
-----------------------

:ref:`path` solves square complementarity problems (MCP). MP-based solvers
also accept ``complements`` and reformulate it, see
`complementarity <https://mp.ampl.com/modeling-expressions.html#complementarity>`_ in the MP modeling guide.

MP2NL and NEOS
--------------

:ref:`mp2nl` applies MP's reformulations for any solver that reads NL files.
Try NEOS directly from Google Colab here: `Open in Google Colab <https://colab.ampl.com/tags/neos.html>`_,
or with the :ref:`Kestrel client <kestrel>`.
