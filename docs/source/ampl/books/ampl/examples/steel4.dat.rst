steel4.dat
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

:download:`steel4.dat <EXAMPLES/EXAMPLES2/steel4.dat>`

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
    
    param avail :=  reheat 35   roll   40 ;
