cut3.run
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`cut3.run <EXAMPLES/LOOP2/cut3.run>`

.. code-block:: ampl

    
    # ----------------------------------------
    # GILMORE-GOMORY METHOD FOR
    # CUTTING STOCK PROBLEM
    # ----------------------------------------
    
    option solver cplex;
    option solution_round 6;
    option solver_msg 0;
    
    model cut1.mod;
    data cut.dat;
    
    problem Cutting_Opt: Cut, Number, Fill;
       option relax_integrality 1;
       option presolve 0;
    
    problem Pattern_Gen: Use, Reduced_Cost, Width_Limit;
       option relax_integrality 0;
       option presolve 1;
    
    let nPAT := 0;
    
    for {i in WIDTHS} {
       let nPAT := nPAT + 1;
       let nbr[i,nPAT] := floor (roll_width/i);
       let {i2 in WIDTHS: i2 <> i} nbr[i2,nPAT] := 0;
       };
    
    repeat {
       solve Cutting_Opt >/dev/null;
    
       let {i in WIDTHS} price[i] := Fill[i].dual;
    
       solve Pattern_Gen >/dev/null;
    
       printf "\n%7.2f%11.2e  ", Number, Reduced_Cost;
    
       if Reduced_Cost < -0.00001 then {
          let nPAT := nPAT + 1;
          let {i in WIDTHS} nbr[i,nPAT] := Use[i];
          }
       else break;
    
       for {i in WIDTHS} printf "%3i", Use[i];
       };
    
    let {j in PATTERNS} Cut[j] := ceil(Cut[j]);
    
    printf "\n\n\nRounded up to integer: %3i rolls", sum {j in PATTERNS} Cut[j];
    printf "\n\nCut  ";
    printf {j in PATTERNS}: "%4i", Cut[j];
    printf "\n\n";
    for {i in WIDTHS} {
       printf "%3i  ", i;
       printf {j in PATTERNS}: "%4i", nbr[i,j];
       printf "\n";
       }
    
    printf "\nWASTE = %5.2f%%\n\n\n", 
       100 * (1 - (sum {i in WIDTHS} i * orders[i])  / (roll_width * Number));
    
    option Cutting_Opt.relax_integrality 0;
    option Cutting_Opt.presolve 10;
    solve Cutting_Opt >/dev/null;
    
    printf "Best integer: %3i rolls", sum {j in PATTERNS} Cut[j];
    printf "\n\nCut  ";
    printf {j in PATTERNS}: "%4i", Cut[j];
    printf "\n\n";
    for {i in WIDTHS} {
       printf "%3i  ", i;
       printf {j in PATTERNS}: "%4i", nbr[i,j];
       printf "\n";
       }
    
    printf "\nWASTE = %5.2f%%\n\n", 
       100 * (1 - (sum {i in WIDTHS} i * orders[i])  / (roll_width * Number));
