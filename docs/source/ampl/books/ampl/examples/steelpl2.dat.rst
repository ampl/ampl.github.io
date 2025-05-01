steelpl2.dat
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelpl2.dat <EXAMPLES/EXAMPLES2/steelpl2.dat>`

.. code-block:: ampl

    data;
    
    param T := 4;
    set PROD := bands coils;
    
    param:    rate  inv0  prodcost  invcost :=
      bands    200   10     10        2.5
      coils    140    0     11        3 ;
    
    param: avail_min  avail_max  time_penalty :=
       1       35         42         3100
       2       35         42         3000
       3       30         40         3700
       4       35         42         3100 ;
    
    param revenue:    1     2     3     4 :=
           bands     25    26    27    27
           coils     30    35    37    39 ;
    
    param commit:     1     2     3     4 :=
           bands   3500  5900  3900  6400
           coils   2500  2400  3400  4100 ;
    
    param market:     1     2     3     4 :=
           bands   6000  6000  4000  6500
           coils   4000  2500  3500  4200 ;
