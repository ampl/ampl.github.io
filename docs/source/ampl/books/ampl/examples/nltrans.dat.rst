nltrans.dat
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`nltrans.dat <EXAMPLES/EXAMPLES2/nltrans.dat>`

.. code-block:: ampl

    data;
    
    param: ORIG:  supply :=
            GARY   1400    CLEV   2600    PITT   2900 ;
    
    param: DEST:  demand :=
            FRA     900    DET    1200    LAN     600 
            WIN     400    STL    1700    FRE    1100 
            LAF    1000 ;
    
    param rate :  FRA  DET  LAN  WIN  STL  FRE  LAF :=
            GARY   39   14   11   14   16   82    8
            CLEV   27    9   12    9   26   95   17
            PITT   24   14   17   13   28   99   20 ;
    
    param limit :  FRA  DET  LAN  WIN  STL  FRE  LAF :=
            GARY   500 1000 1000 1000  800  500 1000
            CLEV   500  800  800  800  500  500 1000
            PITT   800  600  600  600  500  500  900 ;
