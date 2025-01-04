steelT.tab2
===========

:download:`steelT.tab2 <EXAMPLES/LOOP1/steelT.tab2>`

.. code-block:: ampl

    
    printf "\nSALES";
    printf {p in PROD}: "%14s   ", p;
    printf "\n";
    
    for {t in 1..T} {
       printf "week %d", t;
    
       for {p in PROD} {
          printf "%9d", Sell[p,t];
          if Sell[p,t] < market[p,t] then
             printf "%7.1f%%", 100 * Sell[p,t]/market[p,t];
          else printf "    --- ";
          }
    
       printf "\n";
       }
    
    printf "\n";
