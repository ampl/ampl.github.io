steelT.dat
==========

:download:`steelT.dat <EXAMPLES/EXAMPLES2/steelT.dat>`

.. code-block:: ampl

    data;
    
    param T := 4;
    set PROD := bands coils;
    
    param avail :=  1 40  2 40  3 32  4 40 ;
    
    param rate :=  bands 200   coils 140 ;
    param inv0 :=  bands  10   coils   0 ;
    
    param prodcost :=  bands 10    coils  11 ;
    param invcost  :=  bands  2.5  coils   3 ;
    
    param revenue:   1     2     3     4 :=
           bands    25    26    27    27
           coils    30    35    37    39 ;
    
    param market:    1     2     3     4 :=
           bands  6000  6000  4000  6500
           coils  4000  2500  3500  4200 ;
