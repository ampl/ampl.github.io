assign.dat
==========

:download:`assign.dat <EXAMPLES/EXAMPLES2/assign.dat>`

.. code-block:: ampl

    data;
    set ORIG := Coullard Daskin Hazen Hopp Iravani Linetsky 
                Mehrotra Nelson Smilowitz Tamhane White ;
    
    set DEST := C118 C138 C140 C246 C250 C251 D237 D239 D241 M233 M239;
    
    param supply default 1 ;
    
    param demand default 1 ;
    
    param cost:
              C118 C138 C140 C246 C250 C251 D237 D239 D241 M233 M239 :=
     Coullard   6    9    8    7   11   10    4    5    3    2    1
     Daskin    11    8    7    6    9   10    1    5    4    2    3
     Hazen      9   10   11    1    5    6    2    7    8    3    4
     Hopp      11    9    8   10    6    5    1    7    4    2    3
     Iravani    3    2    8    9   10   11    1    5    4    6    7
     Linetsky  11    9   10    5    3    4    6    7    8    1    2
     Mehrotra   6   11   10    9    8    7    1    2    5    4    3
     Nelson    11    5    4    6    7    8    1    9   10    2    3
     Smilowitz 11    9   10    8    6    5    7    3    4    1    2
     Tamhane    5    6    9    8    4    3    7   10   11    2    1
     White     11    9    8    4    6    5    3   10    7    2    1 ;
