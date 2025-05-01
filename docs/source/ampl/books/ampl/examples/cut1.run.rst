cut1.run
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`cut1.run <EXAMPLES/LOOP2/cut1.run>`

.. code-block:: ampl

    
    # ----------------------------------------
    # GILMORE-GOMORY METHOD FOR
    # CUTTING STOCK PROBLEM
    # ----------------------------------------
    
    option solver cplex;
    option solution_round 6;
    
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
