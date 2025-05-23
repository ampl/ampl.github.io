sudokuVeryEasy.dat
==================


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`sudokuVeryEasy.dat <EXAMPLES/LOGIC/EXAMPLES/sudokuVeryEasy.dat>`

.. code-block:: ampl

    
    param given default 0:
    
                   1 2 3 4 5 6 7 8 9 :=
               1   . . 1 . 8 . 3 . .
               2   4 5 . . 6 . . 2 .
               3   . . 9 . . 3 7 6 .
               4   . . . 8 9 . . 3 7
               5   . 1 7 5 . 2 6 9 .
               6   3 9 . . 4 7 . . .
               7   . 4 5 9 . . 8 . .
               8   . 2 . . 5 . . 1 6
               9   . . 6 . 7 . 4 . . ;
