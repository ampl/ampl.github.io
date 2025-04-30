steel3.dat
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

:download:`steel3.dat <EXAMPLES/EXAMPLES2/steel3.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils plate;
    
    param:    rate  profit  commit  market :=
      bands    200    25     1000    6000
      coils    140    30      500    4000
      plate    160    29      750    3500 ;
    
    param avail := 40;
