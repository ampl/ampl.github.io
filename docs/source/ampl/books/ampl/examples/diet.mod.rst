diet.mod
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`diet.mod <EXAMPLES/EXAMPLES2/diet.mod>`

.. code-block:: ampl

    set NUTR;
    set FOOD;
    
    param cost {FOOD} > 0;
    param f_min {FOOD} >= 0;
    param f_max {j in FOOD} >= f_min[j];
    
    param n_min {NUTR} >= 0;
    param n_max {i in NUTR} >= n_min[i];
    
    param amt {NUTR,FOOD} >= 0;
    
    var Buy {j in FOOD} >= f_min[j], <= f_max[j];
    
    minimize Total_Cost:  sum {j in FOOD} cost[j] * Buy[j];
    
    subject to Diet {i in NUTR}:
       n_min[i] <= sum {j in FOOD} amt[i,j] * Buy[j] <= n_max[i];
