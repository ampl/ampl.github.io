multi1.run
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`multi1.run <EXAMPLES/LOOP2/multi1.run>`

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
    
    option solver minos;
    option omit_zero_rows 1;
    option display_1col 10;
    option display_eps .000001;
    
    # ----------------------------------------------------------
    
    problem MasterI: Artificial, Weight, Excess, Multi, Convex;
    problem SubI: Artif_Reduced_Cost, Trans, Supply, Demand;
    
    repeat { printf "\nPHASE I -- ITERATION %d\n\n", nPROP+1;
    
       solve SubI;
       printf "\n";
       display Trans;
    
       if Artif_Reduced_Cost >= - 0.00001 then {
          printf "\n*** NO FEASIBLE SOLUTION ***\n";
          break;
          }
       else {
          let nPROP := nPROP + 1;
          let {i in ORIG, j in DEST}
             prop_ship[i,j,nPROP] := sum {p in PROD} Trans[i,j,p];
          let prop_cost[nPROP] := 
             sum {i in ORIG, j in DEST, p in PROD} cost[i,j,p] * Trans[i,j,p];
          };
    
       solve MasterI;
       printf "\n";
       display Weight; display Multi.dual;
       display {i in ORIG, j in DEST} 
          limit[i,j] - sum {k in 1..nPROP} prop_ship[i,j,k] * Weight[k];
    
       if Excess <= 0.00001 then break;
       else {
          let {i in ORIG, j in DEST} price[i,j] := Multi[i,j].dual;
          let price_convex := Convex.dual;
       };
    };
    
    # ----------------------------------------------------------
    
    printf "\nSETTING UP FOR PHASE II\n\n";
    
    problem MasterII: Total_Cost, Weight, Multi, Convex;
    problem SubII: Reduced_Cost, Trans, Supply, Demand;
    
    solve MasterII;
    printf "\n";
    display Weight; display Multi.dual; display Multi.slack;
    
    let {i in ORIG, j in DEST} price[i,j] := Multi[i,j].dual;
    let price_convex := Convex.dual;
    
    repeat { printf "\nPHASE II -- ITERATION %d\n\n", nPROP+1;
    
       solve SubII;
       printf "\n";
       display Trans;
    
       if Reduced_Cost >= - 0.00001 then {
          printf "\n*** OPTIMAL SOLUTION ***\n";
          break;
          }
       else {
          let nPROP := nPROP + 1;
          let {i in ORIG, j in DEST}
             prop_ship[i,j,nPROP] := sum {p in PROD} Trans[i,j,p];
          let prop_cost[nPROP] := 
             sum {i in ORIG, j in DEST, p in PROD} cost[i,j,p] * Trans[i,j,p];
          };
    
       solve MasterII;
    	
       printf "\n";
       display Weight;
    
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
