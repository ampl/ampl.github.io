steelT.sa2
==========

:download:`steelT.sa2 <EXAMPLES/EXAMPLES2/steelT.sa2>`

.. code-block:: ampl

    model steelT.mod;
    data steelT.dat;
    
    for {1..4} {
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
    }
