steel.mod
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steel.mod <EXAMPLES/EXAMPLES2/steel.mod>`

.. code-block:: ampl

    set PROD;  # products
    
    param rate {PROD} > 0;     # tons produced per hour
    param avail >= 0;          # hours available in week
    
    param profit {PROD};       # profit per ton
    param market {PROD} >= 0;  # limit on tons sold in week
    
    var Make {p in PROD} >= 0, <= market[p]; # tons produced
    
    maximize Total_Profit: sum {p in PROD} profit[p] * Make[p];
    
                   # Objective: total profits from all products
    
    subject to Time: sum {p in PROD} (1/rate[p]) * Make[p] <= avail;
    
                   # Constraint: total of hours used by all
                   # products may not exceed hours available
