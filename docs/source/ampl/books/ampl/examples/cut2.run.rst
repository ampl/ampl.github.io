cut2.run
========

:download:`cut2.run <EXAMPLES/EXAMPLES2/cut2.run>`

.. code-block:: ampl

    
    # ----------------------------------------
    # GILMORE-GOMORY METHOD FOR
    # CUTTING STOCK PROBLEM
    # ----------------------------------------
    
    option solver cplex;
    option solution_round 6;
    
    model cut2.mod;
    data cut.dat;
    
    problem Cutting_Opt;
       option relax_integrality 1;
       option presolve 0;
    
    problem Pattern_Gen;
       option relax_integrality 0;
       option presolve 1;
    
    let nPAT := 0;
    
    for {i in WIDTHS} {
       let nPAT := nPAT + 1;
       let nbr[i,nPAT] := floor (roll_width/i);
       let {i2 in WIDTHS: i2 <> i} nbr[i2,nPAT] := 0;
       };
    
    repeat {
       solve Cutting_Opt;
    
       let {i in WIDTHS} price[i] := Fill[i].dual;
    
       solve Pattern_Gen;
    
       if Reduced_Cost < -0.00001 then {
          let nPAT := nPAT + 1;
          let {i in WIDTHS} nbr[i,nPAT] := Use[i];
          }
       else break;
       };
    
    display nbr; 
    display Cut;
    
    option Cutting_Opt.relax_integrality 0;
    option Cutting_Opt.presolve 10;
    solve Cutting_Opt;
    
    display Cut;
