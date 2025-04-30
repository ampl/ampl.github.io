steelT.sa4
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`steelT.sa4 <EXAMPLES/EXAMPLES2/steelT.sa4>`

.. code-block:: ampl

    model steelT.mod;
    data steelT.dat;
    
    option solution_precision 10;
    option solver_msg 0;
    
    set AVAIL3 default {};
    param avail3_obj {AVAIL3};
    param avail3_dual {AVAIL3};
    param avail3_step := 5;
    
    repeat {
       solve;
       let AVAIL3 := AVAIL3 union {avail[3]};
       let avail3_obj[avail[3]] := Total_Profit;
       let avail3_dual[avail[3]] := Time[3].dual;
       let avail[3] := avail[3] + avail3_step;
    } until Time[3].dual = 0;
    
    display avail3_obj, avail3_dual;
