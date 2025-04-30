stoch2.run
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`stoch2.run <EXAMPLES/LOOP2/stoch2.run>`

.. code-block:: ampl

    
    # ----------------------------------------
    # STOCHASTIC PROGRAMMING PROBLEM 
    # USING BENDERS DECOMPOSITION
    # ----------------------------------------
    
    model stoch2.mod;
    data stoch.dat;
    
    option solver cplex;
    
    option omit_zero_rows 1;
    option display_eps .000001;
    
    problem Master: Make1, Inv1, Sell1, Min_Stage2_Profit,
       Expected_Profit, Cut_Defn, Time1, Balance1;
    
    problem Sub {s in SCEN}: 
       {p in PROD, t in 2..T} Make[p,t,s], 
       {p in PROD, t in 2..T} Inv[p,t,s], 
       {p in PROD, t in 2..T} Sell[p,t,s], 
       Exp_Stage2_Profit[s], 
       {t in 2..T} Time[t,s], 
       {p in PROD} Balance2[p,s], 
       {p in PROD, t in 3..T} Balance[p,t,s];
    
    let nCUT := 0;
    let Min_Stage2_Profit := Infinity;
    let {p in PROD} inv1[p] := 0;
    
    param GAP default Infinity;
    param newGAP;
    
    for {1..50} { printf "\nITERATION %d\n\n", nCUT+1;
    
       let nCUT := nCUT + 1;
    
       for {s in SCEN} { 
          solve Sub[s];
          let {t in 2..T} time_price[t,s,nCUT] := Time[t,s].dual;
          let {p in PROD} bal2_price[p,s,nCUT] := Balance2[p,s].dual;
          let {p in PROD, t in 2..T} 
             sell_lim_price[p,t,s,nCUT] := Sell[p,t,s].urc;
          }
    
       let newGAP := Min_Stage2_Profit - sum {s in SCEN} Exp_Stage2_Profit[s];
       printf "\n";
    
       if newGAP > 0.00001 then {
          let GAP := min (GAP, newGAP);
          option display_1col 0;
          display GAP, Make, Sell, Inv;
          }
       else break;
    
       printf "\nRE-SOLVING MASTER PROBLEM\n\n";
    
       solve Master;
       printf "\n";
       option display_1col 20;
       display Make1, Inv1, Sell1;
    
       let {p in PROD} inv1[p] := Inv1[p];
    };
    
    printf "\nOPTIMAL SOLUTION FOUND\nExpected Profit = %f\n\n", Expected_Profit;
    option display_1col 0;
    
    param MAKE {p in PROD, t in 1..T, s in SCEN}
       := if t = 1 then Make1[p].val else Make[p,t,s].val;
    param SELL {p in PROD, t in 1..T, s in SCEN}
       := if t = 1 then Sell1[p].val else Sell[p,t,s].val;
    param INV {p in PROD, t in 1..T, s in SCEN}
       := if t = 1 then Inv1[p].val else Inv[p,t,s].val;
    
    for {s in SCEN} {
       printf "SCENARIO %s\n", s;
       display {p in PROD, t in 1..T} 
          (MAKE[p,t,s], SELL[p,t,s], INV[p,t,s]);
       }
