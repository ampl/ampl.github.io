net1.dat
========

:download:`net1.dat <EXAMPLES/EXAMPLES2/net1.dat>`

.. code-block:: ampl

    data;
    
    set CITIES := PITT  NE SE  BOS EWR BWI ATL MCO ;
    
    set LINKS := (PITT,NE) (PITT,SE)
                 (NE,BOS) (NE,EWR) (NE,BWI)
                 (SE,EWR) (SE,BWI) (SE,ATL) (SE,MCO);
    
    param supply  default 0 := PITT 450 ;
    
    param demand  default 0 :=
      BOS  90,  EWR 120,  BWI 120,  ATL  70,  MCO  50;
    
    param:      cost  capacity  :=
      PITT NE    2.5    250
      PITT SE    3.5    250
    
      NE BOS     1.7    100
      NE EWR     0.7    100
      NE BWI     1.3    100
    
      SE EWR     1.3    100
      SE BWI     0.8    100
      SE ATL     0.2    100
      SE MCO     2.1    100 ;
