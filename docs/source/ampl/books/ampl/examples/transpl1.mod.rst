transpl1.mod
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`transpl1.mod <EXAMPLES/EXAMPLES2/transpl1.mod>`

.. code-block:: ampl

    set ORIG;   # origins
    set DEST;   # destinations
    
    param supply {ORIG} >= 0;   # amounts available at origins
    param demand {DEST} >= 0;   # amounts required at destinations
    
       check: sum {i in ORIG} supply[i] = sum {j in DEST} demand[j];
    
    param rate1 {i in ORIG, j in DEST} >= 0;
    param rate2 {i in ORIG, j in DEST} >= rate1[i,j];
    param rate3 {i in ORIG, j in DEST} >= rate2[i,j];
    
    param limit1 {i in ORIG, j in DEST} > 0;
    param limit2 {i in ORIG, j in DEST} > limit1[i,j];
    
    var Trans {ORIG,DEST} >= 0;    # units to be shipped
    
    minimize Total_Cost:
       sum {i in ORIG, j in DEST} 
          <<limit1[i,j], limit2[i,j]; 
            rate1[i,j], rate2[i,j], rate3[i,j]>> Trans[i,j];
    
    subject to Supply {i in ORIG}:  
       sum {j in DEST} Trans[i,j] = supply[i];
    
    subject to Demand {j in DEST}:  
       sum {i in ORIG} Trans[i,j] = demand[j];
