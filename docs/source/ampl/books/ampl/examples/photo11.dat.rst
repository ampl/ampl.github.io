photo11.dat
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

:download:`photo11.dat <EXAMPLES/LOGIC/EXAMPLES/photo11.dat>`

.. code-block:: ampl

    
    param nPeople := 11;
    
    set PREFS := 
       1 3   1 5   1 8   2 5   2 9   3 4   3 5   4 1   4 5    4 10  
       5 6   5 1   6 1   6 9   7 3   7 8   8 9   8 7   9 10  10 11 ;
