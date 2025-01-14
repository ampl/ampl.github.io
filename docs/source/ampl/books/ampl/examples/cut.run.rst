cut.run
=======

:download:`cut.run <EXAMPLES/EXAMPLES2/cut.run>`

.. code-block:: ampl

    model cut.mod;
    data cut.dat;
    option solver cplex, solution_round 6;
    option display_1col 0, display_transpose -10;
    
    problem Cutting_Opt: Cut, Number, Fill;
    option relax_integrality 1;
    
    problem Pattern_Gen: Use, Reduced_Cost, Width_Limit;
    option relax_integrality 0;
    
    let nPAT := 0;
    for {i in WIDTHS} {
       let nPAT := nPAT + 1;
       let nbr[i,nPAT] := floor (roll_width/i);
       let {i2 in WIDTHS: i2 <> i} nbr[i2,nPAT] := 0;
    }
    
    repeat {
       solve Cutting_Opt;
       let {i in WIDTHS} price[i] := Fill[i].dual;
    
       solve Pattern_Gen;
       if Reduced_Cost < -0.00001 then {
          let nPAT := nPAT + 1;
          let {i in WIDTHS} nbr[i,nPAT] := Use[i];
       }
       else break;
    }
    display nbr, Cut;
    
    option Cutting_Opt.relax_integrality 0;
    solve Cutting_Opt;
    display Cut;
