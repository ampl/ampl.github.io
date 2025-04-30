steelT.tab1
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

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
