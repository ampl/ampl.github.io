cut.run
=======


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

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
