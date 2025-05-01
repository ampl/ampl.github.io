steelT.sa6b
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelT.sa6b <EXAMPLES/LOOP1/steelT.sa6b>`

.. code-block:: ampl

    
    model steelT.mod;
    data steelT.dat;
    
    option solution_precision 10;
    option solver_msg 0;
    
    param avail3_lower default  0; param dual_lower;
    param avail3_upper default 70; param dual_upper;
    param other_bkpts default 0;
    
    let avail[3] := avail3_lower;
    solve; let dual_lower := time[3].dual;
    
    let avail[3] := avail3_upper;
    solve; let dual_upper := time[3].dual;
    
    repeat {
    
       let avail[3] := (avail3_lower + avail3_upper) / 2;
    
       solve;
    
       if time[3].dual = dual_lower 
          then let avail3_lower := avail[3];
          else if time[3].dual = dual_upper 
             then let avail3_upper := avail[3];
             else {
                let other_bkpts := other_bkpts + 1;
                let avail3_lower := avail[3];
                let dual_lower := time[3].dual;
                };
    
       } until (avail3_upper - avail3_lower) / avail[3] < 0.0000001;
    
    printf "Dual value %11.6f for avail[3] < %9.6f\n",
       dual_lower, avail3_lower;
    
    printf "Dual value %11.6f for avail[3] > %9.6f\n",
       dual_upper, avail3_upper;
    
    if other_bkpts > 0 then
       printf "Additional breakpoints detected: %2d\n", other_bkpts; ;
