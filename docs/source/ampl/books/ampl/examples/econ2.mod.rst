econ2.mod
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`econ2.mod <EXAMPLES/EXAMPLES2/econ2.mod>`

.. code-block:: ampl

    set PROD;   # products
    set ACT;    # activities
    
    param cost {ACT} > 0;      # cost per unit of each activity
    param demand {PROD} >= 0;  # units of demand for each product
    param io {PROD,ACT} >= 0;  # units of each product from
                               # 1 unit of each activity
    
    param level_min {ACT} > 0; # min allowed level for each activity
    param level_max {ACT} > 0; # max allowed level for each activity
    
    var Price {i in PROD};
    var Level {j in ACT};
    
    subject to Pri_Compl {i in PROD}:
       Price[i] >= 0 complements
          sum {j in ACT} io[i,j] * Level[j] >= demand[i];
    
    subject to Lev_Compl {j in ACT}:
       level_min[j] <= Level[j] <= level_max[j] complements
          cost[j] - sum {i in PROD} Price[i] * io[i,j];
