openShop.dat
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`openShop.dat <EXAMPLES/LOGIC/EXAMPLES/openShop.dat>`

.. code-block:: ampl

    
    param endTime := 2809 ;
    param nMach := 4 ;
    param nJobs := 3 ;
    
    param duration:  
            1    2    3 :=
       1  121  661    6
       2  333  168  489
       3  343  621  212
       4  171  505  324 ;
