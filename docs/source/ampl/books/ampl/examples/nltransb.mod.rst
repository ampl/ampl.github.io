nltransb.mod
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`nltransb.mod <EXAMPLES/EXAMPLES2/nltransb.mod>`

.. code-block:: ampl

    set ORIG;   # origins
    set DEST;   # destinations
    
    param supply {ORIG} >= 0;   # amounts available at origins
    param demand {DEST} >= 0;   # amounts required at destinations
    
       check: sum {i in ORIG} supply[i] = sum {j in DEST} demand[j];
    
    param rate {ORIG,DEST} >= 0;   # base shipment costs per unit
    param limit {ORIG,DEST} > 0;   # limit on units shipped
    
    var Trans {i in ORIG, j in DEST} >= 0, <= .9999 * limit[i,j]; # units to ship
    
    minimize Total_Cost:
       sum {i in ORIG, j in DEST} 
          rate[i,j] * Trans[i,j] / (1 - Trans[i,j]/limit[i,j]);
    
    subject to Supply {i in ORIG}:  
       sum {j in DEST} Trans[i,j] = supply[i];
    
    subject to Demand {j in DEST}:  
       sum {i in ORIG} Trans[i,j] = demand[j];
