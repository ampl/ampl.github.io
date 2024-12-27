steel3.dat
==========

:download:`steel3.dat <EXAMPLES/EXAMPLES2/steel3.dat>`

.. code-block:: ampl

    data;
    
    set PROD := bands coils plate;
    
    param:    rate  profit  commit  market :=
      bands    200    25     1000    6000
      coils    140    30      500    4000
      plate    160    29      750    3500 ;
    
    param avail := 40;
