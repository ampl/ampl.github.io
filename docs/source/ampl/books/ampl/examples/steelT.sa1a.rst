steelT.sa1a
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

:download:`steelT.sa1a <EXAMPLES/LOOP1/steelT.sa1a>`

.. code-block:: ampl

    
    solve;
    
    display total_profit >steelT.sens;
    
    commands steelT.sa1b;
    
    let avail[3] := avail[3] + 5;
