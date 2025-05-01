prod.mod
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`prod.mod <EXAMPLES/EXAMPLES2/prod.mod>`

.. code-block:: ampl

    set P;
    
    param a {j in P};
    param b;
    param c {j in P};
    param u {j in P};
    
    var X {j in P};
    
    maximize Total_Profit: sum {j in P} c[j] * X[j];
    
    subject to Time: sum {j in P} (1/a[j]) * X[j] <= b;
    
    subject to Limit {j in P}: 0 <= X[j] <= u[j];
