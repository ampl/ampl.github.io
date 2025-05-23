multi2.run
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`multi2.run <EXAMPLES/LOOP2/multi2.run>`

.. code-block:: ampl

    
    # ----------------------------------------
    # DANTZIG-WOLFE DECOMPOSITION FOR
    # MULTI-COMMODITY TRANSPORTATION
    # ----------------------------------------
    
    model multi2.mod;
    data multi2.dat;
    
    param nIter default 0;
    
    let {p in PROD} nPROP[p] := 0;
    let {p in PROD} price_convex[p] := 1;
    let {i in ORIG, j in DEST} price[i,j] := 0;
    
    option omit_zero_rows 1;
    option display_1col 0;
    option display_eps .000001;
    
    # ----------------------------------------------------------
    
    problem MasterI: Artificial, Weight, Excess, Multi, Convex;
    
    problem SubI {p in PROD}: Artif_Reduced_Cost[p], 
       {i in ORIG, j in DEST} Trans[i,j,p], 
       {i in ORIG} Supply[i,p], {j in DEST} Demand[j,p];
    
    repeat { 
    
       let nIter := nIter + 1;
       printf "\nPHASE I -- ITERATION %d\n", nIter;
    
       for {p in PROD} { printf "\nPRODUCT %s\n\n", p;
    
          solve SubI[p];
          printf "\n";
          display {i in ORIG, j in DEST} Trans[i,j,p];
    
          if Artif_Reduced_Cost[p] < - 0.00001 then {
             let nPROP[p] := nPROP[p] + 1;
             let {i in ORIG, j in DEST}
                prop_ship[i,j,p,nPROP[p]] := Trans[i,j,p];
             let prop_cost[p,nPROP[p]] := 
                sum {i in ORIG, j in DEST} cost[i,j,p] * Trans[i,j,p];
          };
       };
    
       if min {p in PROD} Artif_Reduced_Cost[p] >= - 0.00001 then {
          printf "\n*** NO FEASIBLE SOLUTION ***\n";
          break;
       };
    
       solve MasterI;
       printf "\n";
       display Weight; display Multi.dual;
       display {i in ORIG, j in DEST} 
          limit[i,j] - sum {p in PROD, k in 1..nPROP[p]} 
             prop_ship[i,j,p,k] * Weight[p,k];
    
       if Excess <= 0.00001 then break;
       else {
          let {i in ORIG, j in DEST} price[i,j] := Multi[i,j].dual;
          let {p in PROD} price_convex[p] := Convex[p].dual;
       };
    };
    
    # ----------------------------------------------------------
    
    printf "\nSETTING UP FOR PHASE II\n";
    
    problem MasterII: Total_Cost, Weight, Multi, Convex;
    
    problem SubII {p in PROD}: Reduced_Cost[p], 
       {i in ORIG, j in DEST} Trans[i,j,p], 
       {i in ORIG} Supply[i,p], {j in DEST} Demand[j,p];
    
    solve MasterII;
    printf "\n";
    display Weight; display Multi.dual; display Multi.slack;
    
    let {i in ORIG, j in DEST} price[i,j] := Multi[i,j].dual;
    let {p in PROD} price_convex[p] := Convex[p].dual;
    
    repeat {
    
       let nIter := nIter + 1;
       printf "\nPHASE II -- ITERATION %d\n\n", nIter;
    
       for {p in PROD} { printf "\nPRODUCT %s\n\n", p;
    
          solve SubII[p];
          printf "\n";
          display {i in ORIG, j in DEST} Trans[i,j,p];
    
          if Reduced_Cost[p] < - 0.00001 then  {
             let nPROP[p] := nPROP[p] + 1;
             let {i in ORIG, j in DEST}
                prop_ship[i,j,p,nPROP[p]] := Trans[i,j,p];
             let prop_cost[p,nPROP[p]] := 
                sum {i in ORIG, j in DEST} cost[i,j,p] * Trans[i,j,p];
          };
       };
    
       if min {p in PROD} Reduced_Cost[p] >= - 0.00001 then break;
    
       solve MasterII;
    	
       printf "\n";
       display Weight;
    
       let {i in ORIG, j in DEST} price[i,j] := Multi[i,j].dual;
       let {p in PROD} price_convex[p] := Convex[p].dual;
    };
    
    # ----------------------------------------------------------
    
    printf "\nPHASE III\n";
    
    let {i in ORIG, j in DEST, p in PROD}
       Trans[i,j,p] := sum {k in 1..nPROP[p]} prop_ship[i,j,p,k] * Weight[p,k];
    
    param true_Total_Cost 
       := sum {i in ORIG, j in DEST, p in PROD} cost[i,j,p] * Trans[i,j,p].val;
    
    printf "\n";
    display true_Total_Cost;
    display Trans;
