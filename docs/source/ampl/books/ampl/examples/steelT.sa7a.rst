steelT.sa7a
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`steelT.sa7a <EXAMPLES/LOOP1/steelT.sa7a>`

.. code-block:: ampl

    
    model steelT.mod;
    data steelT.dat;
    
    option solution_precision 10;
    option solver_msg 0;
    
    set AVAILt;
    param availt_obj {AVAILt};
    param availt_dual {AVAILt};
    
    param avail_orig;
    param previous_dual;
    
    for {t in 1..T} {
    
       let AVAILt := {};
       reset data availt_obj;
       reset data availt_dual;
    
       let avail_orig := avail[t];
       let avail[t] := 0;
       let previous_dual := Infinity;
    
       repeat {
    
          let avail[t] := avail[t] + 1;
    
          solve;
    
          if time[t].dual = previous_dual then continue;
    
          let AVAILt := AVAILt union {avail[t]};
          let availt_obj[avail[t]] := total_profit;
          let availt_dual[avail[t]] := time[t].dual;
    
          if time[t].dual = 0 then break;
    
          let previous_dual := time[t].dual;
          }
    
       let avail[t] := avail_orig;
    
       display t, availt_obj, availt_dual;
       }
    
