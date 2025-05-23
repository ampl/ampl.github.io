steelT3.dat
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelT3.dat <EXAMPLES/EXAMPLES2/steelT3.dat>`

.. code-block:: ampl

    data;
    
    param T := 4;
    
    set PROD := bands coils;
    set AREA[bands] := east north ;
    set AREA[coils] := east west export ;
    
    param avail :=  1 40  2 40  3 32  4 40 ;
    
    param rate :=  bands  200  coils  140 ;
    param inv0 :=  bands   10  coils    0 ;
    
    param prodcost :=  bands 10    coils 11 ;
    param invcost  :=  bands  2.5  coils  3 ;
    
    param revenue :=
    
      [bands,*,*]:   1      2      3      4 :=
          east     25.0   26.0   27.0   27.0
          north    26.5   27.5   28.0   28.5
    
      [coils,*,*]:   1     2     3     4 :=
          east      30    35    37    39
          west      29    32    33    35
          export    25    25    25    28 ;
    
    param market :=
    
      [bands,*,*]:     1     2     3     4 :=
           east     2000  2000  1500  2000
           north    4000  4000  2500  4500
    
      [coils,*,*]:     1     2     3     4 :=
           east     1000   800  1000  1100
           west     2000  1200  2000  2300
           export   1000   500   500   800 ;
    
