iocol2.mod
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

:download:`iocol2.mod <EXAMPLES/EXAMPLES2/iocol2.mod>`

.. code-block:: ampl

    set MAT;             # materials
    set ACT;             # activities
    
    param io {MAT,ACT};  # input-output coefficients
    
    set MATF within MAT; # finished materials
    
    param revenue {MATF} >= 0;
    
    param sell_min {MATF} >= 0;
    param sell_max {i in MATF} >= sell_min[i];
    
    param cost {ACT} >= 0;
    param act_min {ACT} >= 0;
    param act_max {j in ACT} >= act_min[j];
    
    maximize Net_Profit;
    
    subject to Balance {i in MAT}: to_come = 0;
    
    var Run {j in ACT} >= act_min[j], <= act_max[j],
       obj Net_Profit -cost[j],
       coeff {i in MAT} Balance[i] io[i,j];
    
    var Sell {i in MATF} >= sell_min[i], <= sell_max[i],
       obj Net_Profit revenue[i],
       coeff Balance[i] -1;
    
