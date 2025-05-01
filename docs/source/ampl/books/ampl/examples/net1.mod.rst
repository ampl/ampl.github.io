net1.mod
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`net1.mod <EXAMPLES/EXAMPLES2/net1.mod>`

.. code-block:: ampl

    set CITIES;
    set LINKS within (CITIES cross CITIES);
    
    param supply {CITIES} >= 0;   # amounts available at cities
    param demand {CITIES} >= 0;   # amounts required at cities
    
    check: sum {i in CITIES} supply[i] = sum {j in CITIES} demand[j];
    
    param cost {LINKS} >= 0;      # shipment costs/1000 packages
    param capacity {LINKS} >= 0;  # max packages that can be shipped
    
    var Ship {(i,j) in LINKS} >= 0, <= capacity[i,j]; 
                                  # packages to be shipped
    
    minimize Total_Cost:
       sum {(i,j) in LINKS} cost[i,j] * Ship[i,j];
    
    subject to Balance {k in CITIES}:
       supply[k] + sum {(i,k) in LINKS} Ship[i,k] 
          = demand[k] + sum {(k,j) in LINKS} Ship[k,j];
    
