singleHoist3.dat
================

:download:`singleHoist3.dat <EXAMPLES/LOGIC/EXAMPLES/singleHoist3.dat>`

.. code-block:: ampl

    
    param numTanks := 3;
    param numJobs := 3;
    
    param empty:  0  1  2  3 :=
               0  0  2  3  3
               1  2  0  2  3
               2  3  2  0  2
               3  3  3  2  0 ;
    
    param full := 0 4  1 4  2 4  3 5 ;
    
    param minTime := 1 10  2 25  3 10 ;
    param maxTime := 1 10  2 25  3 10 ;
