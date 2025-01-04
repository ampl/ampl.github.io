steelT.sa1a
===========

:download:`steelT.sa1a <EXAMPLES/LOOP1/steelT.sa1a>`

.. code-block:: ampl

    
    solve;
    
    display total_profit >steelT.sens;
    
    commands steelT.sa1b;
    
    let avail[3] := avail[3] + 5;
