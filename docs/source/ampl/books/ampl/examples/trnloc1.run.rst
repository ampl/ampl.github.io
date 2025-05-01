trnloc1.run
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`trnloc1.run <EXAMPLES/LOOP2/trnloc1.run>`

.. code-block:: ampl

    
    # ----------------------------------------
    # BENDERS DECOMPOSITION FOR
    # THE LOCATION-TRANSPORTATION PROBLEM
    # ----------------------------------------
    
    model trnloc1.mod;
    data trnloc.dat;
    
    option omit_zero_rows 1;
    option display_eps .000001;
    
    problem Master: Build, Max_Ship_Cost, Total_Cost, Cut_Defn;
       option display_1col 20;
       option solver cplex, cplex_options '';
    
    problem Sub: Ship, Ship_Cost, Supply, Demand;
       option presolve 0;
       option display_1col 0;
       option solver cplex, cplex_options 'netopt 2 netfind 2';
    
    let nCUT := 0;
    let Max_Ship_Cost := 0;
    let {i in ORIG} build[i] := 1;
    
    param GAP default Infinity;
    
    suffix dunbdd;
    
    repeat { printf "\nITERATION %d\n\n", nCUT+1;
    
       solve Sub;
       printf "\n";
    
       if Sub.result = "infeasible" then {
          let nCUT := nCUT + 1;
          let cut_type[nCUT] := "ray";
          let {i in ORIG} supply_price[i,nCUT] := Supply[i].dunbdd;
          let {j in DEST} demand_price[j,nCUT] := Demand[j].dunbdd;
          expand Cut_Defn[nCUT];
          }
       else if Ship_Cost > Max_Ship_Cost + 0.00001 then {
          let GAP := min (GAP, Ship_Cost - Max_Ship_Cost);
          display GAP, Ship;
          let nCUT := nCUT + 1;
          let cut_type[nCUT] := "point";
          let {i in ORIG} supply_price[i,nCUT] := Supply[i].dual;
          let {j in DEST} demand_price[j,nCUT] := Demand[j].dual;
          }
       else break;
    
       printf "\nRE-SOLVING MASTER PROBLEM\n\n";
    
       solve Master;
       printf "\n";
       display Build;
    
       let {i in ORIG} build[i] := Build[i];
    };
    
    option display_1col 0;
    display Ship;
