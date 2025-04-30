econmin.mod
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

:download:`econmin.mod <EXAMPLES/EXAMPLES2/econmin.mod>`

.. code-block:: ampl

    set PROD;  # products
    set ACT;   # activities
    
    param cost {ACT} > 0;     # cost per unit of each activity
    param demand {PROD} >= 0; # units of demand for each product
    param io {PROD,ACT} >= 0; # units of each product from
                              # 1 unit of each activity
    
    var Level {j in ACT} >= 0;
    
    minimize Total_Cost:  sum {j in ACT} cost[j] * Level[j];
    
    subject to Demand {i in PROD}:
       sum {j in ACT} io[i,j] * Level[j] >= demand[i];
