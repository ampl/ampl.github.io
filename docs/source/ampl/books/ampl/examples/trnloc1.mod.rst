trnloc1.mod
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`trnloc1.mod <EXAMPLES/LOOP2/trnloc1.mod>`

.. code-block:: ampl

    
    # ----------------------------------------
    # LOCATION-TRANSPORTATION PROBLEM 
    # USING BENDERS DECOMPOSITION
    # (using primal formulation of subproblem)
    # ----------------------------------------
    
    ### SUBPROBLEM ###
    
    set ORIG;   # shipment origins (warehouses)
    set DEST;   # shipment destinations (stores)
    
    param supply {ORIG} > 0;
    param demand {DEST} > 0;
    
    param fix_cost {ORIG} > 0;
    param var_cost {ORIG,DEST} > 0;
    
    param build {ORIG} binary;  # = 1 iff warehouse built at i
    
    var Ship {ORIG,DEST} >= 0;  # amounts shipped
    
    minimize Ship_Cost:
       sum {i in ORIG, j in DEST} var_cost[i,j] * Ship[i,j];
    
    subj to Supply {i in ORIG}:
       sum {j in DEST} Ship[i,j] <= supply[i] * build[i];
    
    subj to Demand {j in DEST}:
       sum {i in ORIG} Ship[i,j] = demand[j];
    
    ### MASTER PROBLEM ###
    
    param nCUT >= 0 integer;
    param cut_type {1..nCUT} symbolic within {"point","ray"};
    param supply_price {ORIG,1..nCUT} <= 0.000001;
    param demand_price {DEST,1..nCUT};
    
    var Build {ORIG} binary;   # = 1 iff warehouse built at i
    var Max_Ship_Cost >= 0;
    
    minimize Total_Cost:
       sum {i in ORIG} fix_cost[i] * Build[i] + Max_Ship_Cost;
    
    subj to Cut_Defn {k in 1..nCUT}:
       if cut_type[k] = "point" then Max_Ship_Cost >= 
          sum {i in ORIG} supply_price[i,k] * supply[i] * Build[i] + 
          sum {j in DEST} demand_price[j,k] * demand[j];
