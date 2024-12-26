steel.dat
=========

:download:`steel.dat <EXAMPLES/EXAMPLES2/steel.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils;
    
    param:    rate  profit  market :=
      bands    200    25     6000
      coils    140    30     4000 ;
    
    param avail := 40;
