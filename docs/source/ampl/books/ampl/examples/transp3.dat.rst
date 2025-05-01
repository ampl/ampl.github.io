transp3.dat
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`transp3.dat <EXAMPLES/EXAMPLES2/transp3.dat>`

.. code-block:: ampl

    data;
    
    param: ORIG:  supply :=
        GARY  1400    CLEV  2600    PITT  2900 ;
    
    param: DEST:  demand :=
        FRA   900   DET  1200   LAN   600    WIN  400 
        STL  1700   FRE  1100   LAF  1000 ;
    
    param: LINKS:  cost :=
        GARY DET 14   GARY LAN 11   GARY STL 16   GARY LAF  8
        CLEV FRA 27   CLEV DET  9   CLEV LAN 12   CLEV WIN  9
        CLEV STL 26   CLEV LAF 17
        PITT FRA 24   PITT WIN 13   PITT STL 28   PITT FRE 99 ;
