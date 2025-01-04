singleHoist4.dat
================

:download:`singleHoist4.dat <EXAMPLES/LOGIC/EXAMPLES/singleHoist4.dat>`

.. code-block:: ampl

    
    param numTanks := 4;
    param numJobs := 4;
    
    param empty:  0  1  2  3  4 :=
               0  0  2  3  3  3
               1  2  0  2  3  2
               2  3  2  0  2  2
               3  3  3  2  0  0
               4  2  3  1  4  2 ;
    
    param full := 0 4  1 4  2 4  3 5  4 2 ;
    
    param minTime := 1 10  2 25  3 10  4 40 ;
    param maxTime := 1 10  2 25  3 10  4 40 ;
