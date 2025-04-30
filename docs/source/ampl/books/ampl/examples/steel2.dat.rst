steel2.dat
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

:download:`steel2.dat <EXAMPLES/EXAMPLES2/steel2.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils plate;
    
    param:    rate  profit  market :=
      bands    200    25     6000
      coils    140    30     4000
      plate    160    29     3500 ;
    
    param avail := 40;
