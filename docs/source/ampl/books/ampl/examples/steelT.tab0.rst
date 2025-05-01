steelT.tab0
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelT.tab0 <EXAMPLES/LOOP1/steelT.tab0>`

.. code-block:: ampl

    
    printf "\n%s%14s%17s\n", "SALES", "bands", "coils";
    
    printf {t in 1..T}: "week %d%9d%7.1f%%%9d%7.1f%%\n", 
       t,
       Sell["bands",t], 100*Sell["bands",t]/market["bands",t],
       Sell["coils",t], 100*Sell["coils",t]/market["coils",t];
