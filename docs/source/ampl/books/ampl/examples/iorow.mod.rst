iorow.mod
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`iorow.mod <EXAMPLES/EXAMPLES2/iorow.mod>`

.. code-block:: ampl

    set MAT;             # materials
    set ACT;             # activities
    param io {MAT,ACT};  # input-output coefficients
    
    param revenue {ACT};
    param act_min {ACT} >= 0;
    param act_max {j in ACT} >= act_min[j];
    
    var Run {j in ACT} >= act_min[j], <= act_max[j];
    
    maximize Net_Profit:  sum {j in ACT} revenue[j] * Run[j];
    
    subject to Balance {i in MAT}:
       sum {j in ACT} io[i,j] * Run[j] = 0;
