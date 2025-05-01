steelT.sa3
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelT.sa3 <EXAMPLES/EXAMPLES2/steelT.sa3>`

.. code-block:: ampl

    model steelT.mod;
    data steelT.dat;
    option solver_msg 0;
    
    set AVAIL3;
    param avail3_obj {AVAIL3};
    param avail3_dual {AVAIL3};
    let AVAIL3 := avail[3] .. avail[3] + 15 by 5;
    
    for {a in AVAIL3} {
       let avail[3] := a;
       solve;
       let avail3_obj[a] := Total_Profit;
       let avail3_dual[a] := Time[3].dual;
    }
    display avail3_obj, avail3_dual;
