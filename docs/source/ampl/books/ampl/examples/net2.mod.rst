net2.mod
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`net2.mod <EXAMPLES/EXAMPLES2/net2.mod>`

.. code-block:: ampl

    param p_city symbolic;
    
    set D_CITY;
    set W_CITY;
    set DW_LINKS within (D_CITY cross W_CITY);
    
    param p_supply >= 0;           # amount available at plant
    param w_demand {W_CITY} >= 0;  # amounts required at warehouses
    
       check: p_supply = sum {k in W_CITY} w_demand[k];
    
    set CITIES = {p_city} union D_CITY union W_CITY;
    set LINKS = ({p_city} cross D_CITY) union DW_LINKS;
    
    param supply {k in CITIES} = 
       if k = p_city then p_supply else 0;
    
    param demand {k in CITIES} = 
       if k in W_CITY then w_demand[k] else 0;
    
    ### Remainder same as general transshipment model ###
    
    param cost {LINKS} >= 0;      # shipment costs/1000 packages
    param capacity {LINKS} >= 0;  # max packages that can be shipped
    
    var Ship {(i,j) in LINKS} >= 0, <= capacity[i,j]; 
                                  # packages to be shipped
    
    minimize Total_Cost:
       sum {(i,j) in LINKS} cost[i,j] * Ship[i,j];
    
    subject to Balance {k in CITIES}:
       supply[k] + sum {(i,k) in LINKS} Ship[i,k] 
          = demand[k] + sum {(k,j) in LINKS} Ship[k,j];
