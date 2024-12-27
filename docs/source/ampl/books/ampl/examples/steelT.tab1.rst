steelT.tab1
===========

:download:`steelT.tab1 <EXAMPLES/EXAMPLES2/steelT.tab1>`

.. code-block:: ampl

    printf "\nSALES";
    printf {p in PROD}: "%14s   ", p;
    printf "\n";
    for {t in 1..T} {
       printf "week %d", t;
       for {p in PROD} {
          printf "%9d", Sell[p,t];
          printf "%7.1f%%", 100 * Sell[p,t]/market[p,t];
       }
       printf "\n";
    }
