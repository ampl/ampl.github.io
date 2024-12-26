steelT.sa1
==========

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
