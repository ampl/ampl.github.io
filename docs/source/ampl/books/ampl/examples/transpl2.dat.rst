transpl2.dat
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`transpl2.dat <EXAMPLES/EXAMPLES2/transpl2.dat>`

.. code-block:: ampl

    data;
    
    param: ORIG:  supply :=
            GARY 1400  CLEV 2600  PITT 2900 ;
    
    param: DEST:  demand :=
            FRA  900   DET 1200   LAN  600   WIN  400 
            STL 1700   FRE 1100   LAF 1000 ;
    
    param npiece:  FRA DET LAN WIN STL FRE LAF :=
           GARY     3   3   3   2   3   2   3
           CLEV     3   3   3   3   3   3   3
           PITT     2   2   2   2   1   2   1 ;
    
    param rate :=
      [GARY,FRA,*] 1 39  2 50  3 70   [GARY,DET,*] 1 14  2  17  3  33
      [GARY,LAN,*] 1 11  2 12  3 23   [GARY,WIN,*] 1 14  2  17
      [GARY,STL,*] 1 16  2 23  3 40   [GARY,FRE,*] 1 82  2  98
      [GARY,LAF,*] 1  8  2 16  3 24
    
      [CLEV,FRA,*] 1 27  2 37  3 47   [CLEV,DET,*] 1  9  2  19  3  24
      [CLEV,LAN,*] 1 12  2 32  3 39   [CLEV,WIN,*] 1  9  2  14  3  21
      [CLEV,STL,*] 1 26  2 36  3 47   [CLEV,FRE,*] 1 95  2 105  3 129
      [CLEV,LAF,*] 1  8  2 16  3 24
    
      [PITT,FRA,*] 1 24  2 34         [PITT,DET,*] 1 14  2  24
      [PITT,LAN,*] 1 17  2 27         [PITT,WIN,*] 1 13  2  23
      [PITT,STL,*] 1 28               [PITT,FRE,*] 1 99  2 140
      [PITT,LAF,*] 1 20 ;
    
    param limit :=
      [GARY,*,*] FRA 1  500  FRA 2 1000  DET 1  500  DET 2 1000
                 LAN 1  500  LAN 2 1000  WIN 1 1000
                 STL 1  500  STL 2 1000  FRE 1 1000
                 LAF 1  500  LAF 2 1000
    
      [CLEV,*,*] FRA 1  500  FRA 2 1000  DET 1  500  DET 2 1000
                 LAN 1  500  LAN 2 1000  WIN 1  500  WIN 2 1000
                 STL 1  500  STL 2 1000  FRE 1  500  FRE 2 1000
                 LAF 1  500  LAF 2 1000
    
      [PITT,*,*] FRA 1 1000  DET 1 1000  LAN 1 1000  WIN 1 1000
                 FRE 1 1000 ;
