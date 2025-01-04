steelT.tab0
===========

:download:`steelT.tab0 <EXAMPLES/LOOP1/steelT.tab0>`

.. code-block:: ampl

    
    printf "\n%s%14s%17s\n", "SALES", "bands", "coils";
    
    printf {t in 1..T}: "week %d%9d%7.1f%%%9d%7.1f%%\n", 
       t,
       Sell["bands",t], 100*Sell["bands",t]/market["bands",t],
       Sell["coils",t], 100*Sell["coils",t]/market["coils",t];
