singleHoist3.dat
================


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`singleHoist3.dat <EXAMPLES/LOGIC/EXAMPLES/singleHoist3.dat>`

.. code-block:: ampl

    
    param numTanks := 3;
    param numJobs := 3;
    
    param empty:  0  1  2  3 :=
               0  0  2  3  3
               1  2  0  2  3
               2  3  2  0  2
               3  3  3  2  0 ;
    
    param full := 0 4  1 4  2 4  3 5 ;
    
    param minTime := 1 10  2 25  3 10 ;
    param maxTime := 1 10  2 25  3 10 ;
