steelT.sa1
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`steelT.sa1 <EXAMPLES/EXAMPLES2/steelT.sa1>`

.. code-block:: ampl

    solve;
    
    display Total_Profit >steelT.sens;
    
    option display_1col 0;
    option omit_zero_rows 0;
    display Make >steelT.sens;
    display Sell >steelT.sens;
    
    option display_1col 20;
    option omit_zero_rows 1;
    display Inv >steelT.sens;
    
    let avail[3] := avail[3] + 5;
