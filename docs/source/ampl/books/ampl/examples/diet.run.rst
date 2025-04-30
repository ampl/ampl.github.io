diet.run
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`diet.run <EXAMPLES/EXAMPLES2/diet.run>`

.. code-block:: ampl

    model diet.mod;
    data diet2.dat;
    
    param N symbolic in NUTR;
    param nstart > 0;
    param nstep > 0;
    read N, nstart, nstep <- ;   # read data interactively
    
    set N_MAX default {};
    param N_obj {N_MAX};
    param N_dual {N_MAX};
    option solver_msg 0;
    
    for {i in nstart .. 0 by -nstep} {
       let n_max[N] := i;
       solve;
       if solve_result = "infeasible" then {
          printf "--- infeasible at %d ---\n\n", i;
          break;
       }
       let N_MAX := N_MAX union {i};
       let N_obj[i] := Total_Cost;
       let N_dual[i] := Diet[N].dual;
    }
    display N_obj, N_dual;
