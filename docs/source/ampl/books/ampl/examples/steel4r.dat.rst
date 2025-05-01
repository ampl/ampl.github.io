steel4r.dat
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steel4r.dat <EXAMPLES/EXAMPLES2/steel4r.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils plate;
    set STAGE := reheat roll;
    
    param rate:  reheat  roll :=
      bands        200    200
      coils        200    140
      plate        200    160 ;
    
    param:    profit  commit  market :=
      bands     25     1000    6000
      coils     30      500    4000
      plate     29      750    3500 ;
    
    # param avail :=  reheat 35   roll   40 ;
    param avail_mean := reheat 35  roll  40;
    param avail_variance := reheat 5  roll 2;
