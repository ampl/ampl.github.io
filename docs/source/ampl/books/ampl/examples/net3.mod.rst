net3.mod
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`net3.mod <EXAMPLES/EXAMPLES2/net3.mod>`

.. code-block:: ampl

    set D_CITY;
    set W_CITY;
    set DW_LINKS within (D_CITY cross W_CITY);
    
    param p_supply >= 0;            # amount available at plant
    param w_demand {W_CITY} >= 0;   # amounts required at warehouses
    
       check: p_supply = sum {j in W_CITY} w_demand[j];
    
    param pd_cost {D_CITY} >= 0;    # shipment costs/1000 packages
    param dw_cost {DW_LINKS} >= 0;
    
    param pd_cap {D_CITY} >= 0;     # max packages that can be shipped
    param dw_cap {DW_LINKS} >= 0;
    
    var PD_Ship {i in D_CITY} >= 0, <= pd_cap[i];
    var DW_Ship {(i,j) in DW_LINKS} >= 0, <= dw_cap[i,j];
                                    # packages to be shipped
    
    minimize Total_Cost:
       sum {i in D_CITY} pd_cost[i] * PD_Ship[i] +
       sum {(i,j) in DW_LINKS} dw_cost[i,j] * DW_Ship[i,j];
    
    subject to P_Bal:  sum {i in D_CITY} PD_Ship[i] = p_supply;
    
    subject to D_Bal {i in D_CITY}:  
       PD_Ship[i] = sum {(i,j) in DW_LINKS} DW_Ship[i,j];
    
    subject to W_Bal {j in W_CITY}:
       sum {(i,j) in DW_LINKS} DW_Ship[i,j] = w_demand[j];
    
