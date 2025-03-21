steelT.sa7
==========

:download:`steelT.sa7 <EXAMPLES/EXAMPLES2/steelT.sa7>`

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
    
    repeat {
       let avail[3] := avail[3] + 1;
       solve;
       if Time[3].dual = previous_dual then continue;
    
       let AVAIL3 := AVAIL3 union {avail[3]};
       let avail3_obj[avail[3]] := Total_Profit;
       let avail3_dual[avail[3]] := Time[3].dual;
    
       if Time[3].dual = 0 then break;
    
       let previous_dual := Time[3].dual;
    }
    
    display avail3_obj, avail3_dual;
