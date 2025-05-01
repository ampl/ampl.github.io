multic.mod
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`multic.mod <EXAMPLES/EXAMPLES2/multic.mod>`

.. code-block:: ampl

    set ORIG;   # origins
    set DEST;   # destinations
    set PROD;   # products
    
    set orig {PROD} within ORIG;
    set dest {PROD} within DEST;
    set links {p in PROD} = orig[p] cross dest[p];
    
    param supply {p in PROD, orig[p]} >= 0; # available at origins
    param demand {p in PROD, dest[p]} >= 0; # required at destinations
       check {p in PROD}: sum {i in orig[p]} supply[p,i]
                             = sum {j in dest[p]} demand[p,j];
    
    param limit {ORIG,DEST} >= 0;
    
    param cost {p in PROD, links[p]} >= 0;  # shipment costs per unit
    var Trans {p in PROD, links[p]} >= 0;   # units to be shipped
    
    minimize Total_Cost:
       sum {p in PROD, (i,j) in links[p]} cost[p,i,j] * Trans[p,i,j];
    
    subject to Supply {p in PROD, i in orig[p]}:
       sum {j in dest[p]} Trans[p,i,j] = supply[p,i];
    
    subject to Demand {p in PROD, j in dest[p]}:
       sum {i in orig[p]} Trans[p,i,j] = demand[p,j];
    
    subject to Multi {i in ORIG, j in DEST}:
       sum {p in PROD: (i,j) in links[p]} Trans[p,i,j] <= limit[i,j];
