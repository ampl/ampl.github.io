steelT.sa7c
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`steelT.sa7c <EXAMPLES/LOOP1/steelT.sa7c>`

.. code-block:: ampl

    
    model steelT.mod;
    data steelT.dat;
    
    option solution_precision 10;
    option solver_msg 0;
    
    set AVAIL3 default {};
    param avail3_obj {AVAIL3};
    param avail3_dual {AVAIL3};
    
    let avail[3] := 0;
    param previous_dual default Infinity;
    
    repeat sens_loop {
    
       let avail[3] := avail[3] + 1;
    
       solve;
    
       if time[3].dual = previous_dual then continue;
    
       let AVAIL3 := AVAIL3 union {avail[3]};
       let avail3_obj[avail[3]] := total_profit;
       let avail3_dual[avail[3]] := time[3].dual;
    
       for {t in 1..T}
          if time[t].dual < 2700 then break sens_loop;
    
       let previous_dual := time[3].dual;
       }
    
    display avail3_obj, avail3_dual;
