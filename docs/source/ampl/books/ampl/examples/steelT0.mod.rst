steelT0.mod
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelT0.mod <EXAMPLES/EXAMPLES2/steelT0.mod>`

.. code-block:: ampl

    set PROD;     # products
    param T > 0;  # number of weeks
    
    param rate {PROD} > 0;         # tons per hour produced
    param avail {1..T} >= 0;       # hours available in week
    param profit {PROD,1..T};      # profit per ton
    param market {PROD,1..T} >= 0; # limit on tons sold in week
    
    var Make {p in PROD, t in 1..T} >= 0, <= market[p,t];
    			       # tons produced
    
    maximize Total_Profit:
       sum {p in PROD, t in 1..T} profit[p,t] * Make[p,t];
    
    	# total profits from all products in all weeks
    
    subject to Time {t in 1..T}:
       sum {p in PROD} (1/rate[p]) * Make[p,t] <= avail[t];
    
    	# total of hours used by all products
    	# may not exceed hours available, in each week
