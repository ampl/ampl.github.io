econ2min.mod
============

:download:`econ2min.mod <EXAMPLES/EXAMPLES2/econ2min.mod>`

.. code-block:: ampl

    set PROD;   # products
    set ACT;   # activities
    
    param cost {ACT} > 0;     # cost per unit of each activity
    param demand {PROD} >= 0;  # units of demand for each product
    param io {PROD,ACT} >= 0;  # units of each product from 1 unit of each activity
    
    param level_min {ACT} > 0;  # max allowed level for each activity
    param level_max {ACT} > 0;  # max allowed level for each activity
    
    var Level {j in ACT} >= level_min[j], <= level_max[j];
    
    minimize Total_Cost:  sum {j in ACT} cost[j] * Level[j];
    
    subject to Demand {i in PROD}:
       sum {j in ACT} io[i,j] * Level[j] >= demand[i];
