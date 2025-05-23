nQueens.mod
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`nQueens.mod <EXAMPLES/LOGIC/EXAMPLES/nQueens.mod>`

.. code-block:: ampl

    
    param n integer > 0;
    var Row {1..n} integer >= 1 <= n;
    
    subj to c1: alldiff ({j in 1..n} Row[j]);
    subj to c2: alldiff ({j in 1..n} Row[j]+j);
    subj to c3: alldiff ({j in 1..n} Row[j]-j);
