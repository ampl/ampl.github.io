sudokuHard.dat
==============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

:download:`sudokuHard.dat <EXAMPLES/LOGIC/EXAMPLES/sudokuHard.dat>`

.. code-block:: ampl

    
    param given default 0:
    
                   1 2 3 4 5 6 7 8 9 :=
               1   2 . 4 . . . . 5 .
               2   . 9 . . . 8 . . .
               3   8 . . 1 . . . 2 .
               4   . . 7 3 6 . . 8 .
               5   . . 8 . . . 2 . .
               6   . 3 . . 2 1 7 . .
               7   . 8 . . . 3 . . 4
               8   . . . 5 . . . 6 .
               9   . 4 . . . . 8 . 5 ;
