multi.dat
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`multi.dat <EXAMPLES/EXAMPLES2/multi.dat>`

.. code-block:: ampl

    data;
    
    set ORIG := GARY CLEV PITT ;
    set DEST := FRA DET LAN WIN STL FRE LAF ;
    set PROD := bands coils plate ;
    
    param supply (tr):  GARY   CLEV   PITT :=
                bands    400    700    800
                coils    800   1600   1800
                plate    200    300    300 ;
    
    param demand (tr):
               FRA   DET   LAN   WIN   STL   FRE   LAF :=
       bands   300   300   100    75   650   225   250
       coils   500   750   400   250   950   850   500
       plate   100   100     0    50   200   100   250 ;
    
    param limit default 625 ;
    
    param cost :=
    
     [*,*,bands]:  FRA  DET  LAN  WIN  STL  FRE  LAF :=
            GARY    30   10    8   10   11   71    6
            CLEV    22    7   10    7   21   82   13
            PITT    19   11   12   10   25   83   15
    
     [*,*,coils]:  FRA  DET  LAN  WIN  STL  FRE  LAF :=
            GARY    39   14   11   14   16   82    8
            CLEV    27    9   12    9   26   95   17
            PITT    24   14   17   13   28   99   20
    
     [*,*,plate]:  FRA  DET  LAN  WIN  STL  FRE  LAF :=
            GARY    41   15   12   16   17   86    8
            CLEV    29    9   13    9   28   99   18
            PITT    26   14   17   13   31  104   20 ;
