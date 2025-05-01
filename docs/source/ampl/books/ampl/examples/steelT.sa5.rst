steelT.sa5
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelT.sa5 <EXAMPLES/EXAMPLES2/steelT.sa5>`

.. code-block:: ampl

    model steelT.mod; data steelT.dat;
    option solution_precision 10; option solver_msg 0;
    
    set AVAIL3 default {};
    param avail3_obj {AVAIL3};
    param avail3_dual {AVAIL3};
    
    let avail[3] := 1;
    param avail3_step := 1;
    param previous_dual default Infinity;
    
    repeat while previous_dual > 0 {
       solve;
       if Time[3].dual < previous_dual then {
          let AVAIL3 := AVAIL3 union {avail[3]};
          let avail3_obj[avail[3]] := Total_Profit;
          let avail3_dual[avail[3]] := Time[3].dual;
          let previous_dual := Time[3].dual;
       }
       let avail[3] := avail[3] + avail3_step;
    }
    
    display avail3_obj, avail3_dual;
