steel.dat
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

:download:`steel.dat <EXAMPLES/EXAMPLES2/steel.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils;
    
    param:    rate  profit  market :=
      bands    200    25     6000
      coils    140    30     4000 ;
    
    param avail := 40;
