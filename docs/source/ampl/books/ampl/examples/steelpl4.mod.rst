steelpl4.mod
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelpl4.mod <EXAMPLES/EXAMPLES2/steelpl4.mod>`

.. code-block:: ampl

    set PROD;      # products
    param T > 0;   # number of weeks
    
    param rate {PROD} > 0;          # tons per hour produced
    param inv0 {PROD} >= 0;         # initial inventory
    param commit {PROD,1..T} >= 0;  # minimum tons sold in week
    param market {PROD,1..T} >= 0;  # limit on tons sold in week
    
    param avail_min {1..T} >= 0;                 # unpenalized hours available
    param avail_max {t in 1..T} >= avail_min[t]; # total hours available
    param time_penalty {1..T} > 0;
    
    param prodcost {PROD} >= 0;     # cost per ton produced
    param invcost {PROD} >= 0;      # carrying cost per ton of inventory
    param revenue {PROD,1..T} >= 0; # revenue per ton sold
    
    var Make {PROD,1..T} >= 0;                  # tons produced
    var Inv {PROD,0..T};                        # tons inventoried
    var Sell {p in PROD, t in 1..T}
       >= commit[p,t], <= market[p,t];          # tons sold
    
    var Use {t in 1..T} >= 0, <= avail_max[t];  # hours used
    
    maximize Total_Profit:
       sum {p in PROD, t in 1..T} (revenue[p,t]*Sell[p,t] -
          prodcost[p]*Make[p,t] - invcost[p]*Inv[p,t]) -
       sum {t in 1..T} <<avail_min[t]; 0,time_penalty[t]>> Use[t];
    
                   # Objective: total revenue less costs in all weeks
    
    subject to Time {t in 1..T}:
       sum {p in PROD} (1/rate[p]) * Make[p,t] = Use[t];
    
                   # Total of hours used by all products
                   # may not exceed hours available, in each week
    
    subject to Init_Inv {p in PROD}:  Inv[p,0] = inv0[p];
    
                   # Initial inventory must equal given value
    
    subject to Balance {p in PROD, t in 1..T}:
       Make[p,t] + Inv[p,t-1] = Sell[p,t] + Inv[p,t];
    
                   # Tons produced and taken from inventory
                   # must equal tons sold and put into inventory
