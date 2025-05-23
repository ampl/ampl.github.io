stoch.dat
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`stoch.dat <EXAMPLES/LOOP2/stoch.dat>`

.. code-block:: ampl

    
    # ----------------------------------------
    # STOCHASTIC PROGRAMMING DATA 
    # ----------------------------------------
    
    param T := 4;
    set PROD := bands coils;
    set SCEN := BASE LOW HIGH ;
    
    param avail :=  1 40  2 40  3 32  4 40 ;
    
    param rate :=  bands 200   coils 140 ;
    param inv0 :=  bands  10   coils   0 ;
    
    param prodcost :=  bands 10    coils  11 ;
    param invcost  :=  bands  2.5  coils   3 ;
    
    param revenue
       [*,*,BASE]:   1     2     3     4 :=
           bands    25    26    27    27
           coils    30    35    37    39
    
        [*,*,LOW]:   1     2     3     4 :=
           bands    23    24    25    25
           coils    30    33    35    36
    
       [*,*,HIGH]:   1     2     3     4 :=
           bands    21    27    33    35
           coils    30    32    33    33 ;
    
    param market:    1     2     3     4 :=
           bands  2000  8500  6500  6500
           coils  3000  2500  4500  4200 ;
    
    param prob :=  BASE  .45
                   LOW   .35
                   HIGH  .20 ;
