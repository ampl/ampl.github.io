transpl2.mod
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`transpl2.mod <EXAMPLES/EXAMPLES2/transpl2.mod>`

.. code-block:: ampl

    set ORIG;   # origins
    set DEST;   # destinations
    
    param supply {ORIG} >= 0;   # amounts available at origins
    param demand {DEST} >= 0;   # amounts required at destinations
    
       check: sum {i in ORIG} supply[i] = sum {j in DEST} demand[j];
    
    param npiece {ORIG,DEST} integer >= 1;
    
    param rate {i in ORIG, j in DEST, p in 1..npiece[i,j]} 
      >= if p = 1 then 0 else rate[i,j,p-1];
    
    param limit {i in ORIG, j in DEST, p in 1..npiece[i,j]-1} 
      > if p = 1 then 0 else limit[i,j,p-1];
    
    var Trans {ORIG,DEST} >= 0;    # units to be shipped
    
    minimize Total_Cost:
       sum {i in ORIG, j in DEST} 
          <<{p in 1..npiece[i,j]-1} limit[i,j,p]; 
            {p in 1..npiece[i,j]} rate[i,j,p]>> Trans[i,j];
    
    subject to Supply {i in ORIG}:  
       sum {j in DEST} Trans[i,j] = supply[i];
    
    subject to Demand {j in DEST}:  
       sum {i in ORIG} Trans[i,j] = demand[j];
    
