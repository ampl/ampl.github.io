multi.mod
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`multi.mod <EXAMPLES/EXAMPLES2/multi.mod>`

.. code-block:: ampl

    set ORIG;   # origins
    set DEST;   # destinations
    set PROD;   # products
    
    param supply {ORIG,PROD} >= 0;  # amounts available at origins
    param demand {DEST,PROD} >= 0;  # amounts required at destinations
    
       check {p in PROD}:
          sum {i in ORIG} supply[i,p] = sum {j in DEST} demand[j,p];
    
    param limit {ORIG,DEST} >= 0;
    
    param cost {ORIG,DEST,PROD} >= 0;  # shipment costs per unit
    var Trans {ORIG,DEST,PROD} >= 0;   # units to be shipped
    
    minimize Total_Cost:
       sum {i in ORIG, j in DEST, p in PROD}
          cost[i,j,p] * Trans[i,j,p];
    
    subject to Supply {i in ORIG, p in PROD}:
       sum {j in DEST} Trans[i,j,p] = supply[i,p];
    
    subject to Demand {j in DEST, p in PROD}:
       sum {i in ORIG} Trans[i,j,p] = demand[j,p];
    
    subject to Multi {i in ORIG, j in DEST}:
       sum {p in PROD} Trans[i,j,p] <= limit[i,j];
