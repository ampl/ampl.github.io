steelT2.dat
===========

:download:`steelT2.dat <EXAMPLES/EXAMPLES2/steelT2.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils ;
    set WEEKS := 27sep 04oct 11oct 18oct ;
    
    param avail :=  27sep 40  04oct 40  11oct 32  18oct 40 ;
    
    param rate :=  bands 200  coils 140 ;
    param inv0 :=  bands  10  coils   0 ;
    
    param prodcost :=  bands 10    coils 11 ;
    param invcost  :=  bands  2.5  coils  3 ;
    
    param revenue: 27sep   04oct   11oct   18oct :=
          bands       25      26      27      27
          coils       30      35      37      39 ;
    
    param market:  27sep   04oct   11oct   18oct :=
          bands     6000    6000    4000    6500
          coils     4000    2500    3500    4200 ;
