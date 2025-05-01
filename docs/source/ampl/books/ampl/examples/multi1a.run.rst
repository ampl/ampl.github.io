multi1a.run
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`multi1a.run <EXAMPLES/LOOP2/multi1a.run>`

.. code-block:: ampl

    
    # ----------------------------------------
    # DANTZIG-WOLFE DECOMPOSITION FOR
    # MULTI-COMMODITY TRANSPORTATION
    # ----------------------------------------
    
    model multi1.mod;
    data multi1.dat;
    
    let nPROP := 0;
    let price_convex := 1;
    let {i in ORIG, j in DEST} price[i,j] := 0;
    
    param phase symbolic, default "I";
    
    option solver minos;
    option omit_zero_rows 1;
    option display_1col 10;
    option display_eps .000001;
    
    # ----------------------------------------------------------
    
    problem Master: Artificial, Weight, Excess, Multi, Convex;
    problem Sub: Artif_Reduced_Cost, Trans, Supply, Demand;
    
    repeat { printf "\nPHASE %s -- ITERATION %d\n\n", phase, nPROP+1;
    
       solve Sub;
       printf "\n";
       display Trans;
    
       if phase = "I" then {
          if Artif_Reduced_Cost >= - 0.00001 then {
             printf "\n*** NO FEASIBLE SOLUTION ***\n";
             break;
             }
          }
       else {
          if Reduced_Cost >= - 0.00001 then {
             printf "\n*** OPTIMAL SOLUTION ***\n";
             break;
             }
          };
    
       let nPROP := nPROP + 1;
       let {i in ORIG, j in DEST}
          prop_ship[i,j,nPROP] := sum {p in PROD} Trans[i,j,p];
       let prop_cost[nPROP] := 
          sum {i in ORIG, j in DEST, p in PROD} cost[i,j,p] * Trans[i,j,p];
    
       solve Master;
       printf "\n";
       display Weight; 
    
       if phase = "I" then {
          display Multi.dual;
          display {i in ORIG, j in DEST} 
             limit[i,j] - sum {k in 1..nPROP} prop_ship[i,j,k] * Weight[k];
    
          if Excess <= 0.00001 then {
             printf "\nSETTING UP FOR PHASE II\n\n";
             let phase := "II";
    
             problem Master;
                drop Artificial; restore Total_Cost; fix Excess;
             problem Sub;
                drop Artif_Reduced_Cost; restore Reduced_Cost;
    
          #  problem Master; show obj; solve;
             solve Master;
             printf "\n";
             display Weight; display Multi.dual; display Multi.slack;
             };
          };
    
       let {i in ORIG, j in DEST} price[i,j] := Multi[i,j].dual;
       let price_convex := Convex.dual;
    };
    
    # ----------------------------------------------------------
    
    printf "\nPHASE III\n\n";
    
    problem MasterIII: Opt_Cost, Trans, Supply, Demand, Opt_Multi;
    
    let {i in ORIG, j in DEST}
       opt_ship[i,j] := sum {k in 1..nPROP} prop_ship[i,j,k] * Weight[k];
    
    solve MasterIII;
    printf "\n";
    display Trans;
