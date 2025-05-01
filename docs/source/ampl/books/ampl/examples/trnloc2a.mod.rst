trnloc2a.mod
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`trnloc2a.mod <EXAMPLES/LOOP2/trnloc2a.mod>`

.. code-block:: ampl

    
    # ----------------------------------------
    # LOCATION-TRANSPORTATION PROBLEM 
    # USING LAGRANGIAN RELAXATION
    # ----------------------------------------
    
    set CITY;
    
    param build_limit integer;
    
    param demand {i in CITY} integer > 0;
    param supply {CITY} integer > 0;
    
    param ship_cost {i in CITY, j in CITY} >= 0;
    
    param mult {CITY} >= 0;   # Lagrange multipliers for Demand constr
    
    var Build {CITY} integer >= 0 <= 1;    # = 1 iff warehouse built at i
    var Ship {i in CITY, j in CITY} >= 0;  # amounts shipped
    
    minimize Lagrangian:
       sum {i in CITY, j in CITY} ship_cost[i,j] * Ship[i,j] +
       sum {j in CITY} mult[j] * (demand[j] - sum {i in CITY} Ship[i,j]);
    
    minimize Shipping_Cost:
       sum {i in CITY, j in CITY} ship_cost[i,j] * Ship[i,j];
    
    subj to Supply {i in CITY}:
       sum {j in CITY} Ship[i,j] <= supply[i] * Build[i];
    
    subj to Demand {j in CITY}:
       sum {i in CITY} Ship[i,j] >= demand[j];
    
    subj to Limit:  sum {i in CITY} Build[i] <= build_limit;
