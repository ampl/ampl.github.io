steel4r.mod
===========

:download:`steel4r.mod <EXAMPLES/EXAMPLES2/steel4r.mod>`

.. code-block:: ampl

    set PROD;   # products
    set STAGE;  # stages
    
    param rate {PROD,STAGE} > 0; # tons per hour in each stage
    param avail_mean {STAGE} > 0;
    param avail_variance {s in STAGE} > 0, < avail_mean[s] / 2;
    param avail {s in STAGE} =
       max(Normal(avail_mean[s], avail_variance[s]), 0);
                                 # hours available/week in each stage
    param profit {PROD};         # profit per ton
    
    param commit {PROD} >= 0;    # lower limit on tons sold in week
    param market {PROD} >= 0;    # upper limit on tons sold in week
    
    var Make {p in PROD} >= commit[p], <= market[p]; # tons produced
    
    maximize Total_Profit: sum {p in PROD} profit[p] * Make[p];
    
                   # Objective: total profits from all products
    
    subject to Time {s in STAGE}:
       sum {p in PROD} (1/rate[p,s]) * Make[p] <= avail[s];
    
                   # In each stage: total of hours used by all
                   # products may not exceed hours available
