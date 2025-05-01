prod.dat
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`prod.dat <EXAMPLES/EXAMPLES2/prod.dat>`

.. code-block:: ampl

    data;
    
    set P := bands coils;
    
    param:     a     c     u  :=
      bands   200   25   6000
      coils   140   30   4000 ;
    
    param b := 40;
