transp.dat
==========

:download:`transp.dat <EXAMPLES/EXAMPLES2/transp.dat>`

.. code-block:: ampl

    data;
    
    param: ORIG:  supply :=  # defines set "ORIG" and param "supply"
            GARY   1400
            CLEV   2600
            PITT   2900 ;
    
    param: DEST:  demand :=  # defines "DEST" and "demand"
            FRA     900
            DET    1200
            LAN     600
            WIN     400
            STL    1700
            FRE    1100
            LAF    1000 ;
    
    param cost:
             FRA  DET  LAN  WIN  STL  FRE  LAF :=
       GARY   39   14   11   14   16   82    8
       CLEV   27    9   12    9   26   95   17
       PITT   24   14   17   13   28   99   20 ;
