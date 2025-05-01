blend.mod
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`blend.mod <EXAMPLES/EXAMPLES2/blend.mod>`

.. code-block:: ampl

    set INPUT;    # inputs
    set OUTPUT;   # outputs
    
    param cost {INPUT} > 0;
    param in_min {INPUT} >= 0;
    param in_max {j in INPUT} >= in_min[j];
    
    param out_min {OUTPUT} >= 0;
    param out_max {i in OUTPUT} >= out_min[i];
    
    param io {OUTPUT,INPUT} >= 0;
    
    var X {j in INPUT} >= in_min[j], <= in_max[j];
    
    minimize Total_Cost:  sum {j in INPUT} cost[j] * X[j];
    
    subject to Outputs {i in OUTPUT}:
       out_min[i] <= sum {j in INPUT} io[i,j] * X[j] <= out_max[i];
