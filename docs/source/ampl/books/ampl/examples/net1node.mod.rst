net1node.mod
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`net1node.mod <EXAMPLES/EXAMPLES2/net1node.mod>`

.. code-block:: ampl

    set CITIES;
    set LINKS within (CITIES cross CITIES);
    
    param supply {CITIES} >= 0;   # amounts available at cities
    param demand {CITIES} >= 0;   # amounts required at cities
    
       check: sum {i in CITIES} supply[i] = sum {j in CITIES} demand[j];
    
    param cost {LINKS} >= 0;      # shipment costs/1000 packages
    param capacity {LINKS} >= 0;  # max packages that can be shipped
    
    minimize Total_Cost;
    
    node Balance {k in CITIES}: net_in = demand[k] - supply[k];
    
    arc Ship {(i,j) in LINKS} >= 0, <= capacity[i,j],
       from Balance[i], to Balance[j], obj Total_Cost cost[i,j]; 
    
