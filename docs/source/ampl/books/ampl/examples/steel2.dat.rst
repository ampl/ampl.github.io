steel2.dat
==========

:download:`steel2.dat <EXAMPLES/EXAMPLES2/steel2.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils plate;
    
    param:    rate  profit  market :=
      bands    200    25     6000
      coils    140    30     4000
      plate    160    29     3500 ;
    
    param avail := 40;
