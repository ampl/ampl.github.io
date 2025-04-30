cut.dat
=======


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

:download:`cut.dat <EXAMPLES/EXAMPLES2/cut.dat>`

.. code-block:: ampl

    data;
    
    param roll_width := 110 ;
    
    param: WIDTHS: orders :=
              20     48
              45     35
              50     24
              55     10
              75      8  ;
