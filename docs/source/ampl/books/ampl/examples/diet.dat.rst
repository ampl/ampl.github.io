diet.dat
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`diet.dat <EXAMPLES/EXAMPLES2/diet.dat>`

.. code-block:: ampl

    data;
    
    set NUTR := A B1 B2 C ;
    set FOOD := BEEF CHK FISH HAM MCH MTL SPG TUR ;
    
    param:   cost  f_min  f_max :=
      BEEF   3.19    0     100
      CHK    2.59    0     100
      FISH   2.29    0     100
      HAM    2.89    0     100
      MCH    1.89    0     100
      MTL    1.99    0     100
      SPG    1.99    0     100
      TUR    2.49    0     100 ;
    
    param:   n_min  n_max :=
       A      700   10000
       C      700   10000
       B1     700   10000
       B2     700   10000 ;
    
    param amt (tr):
               A    C   B1   B2 :=
       BEEF   60   20   10   15
       CHK     8    0   20   20
       FISH    8   10   15   10
       HAM    40   40   35   10
       MCH    15   35   15   15
       MTL    70   30   15   15
       SPG    25   50   25   15
       TUR    60   20   15   10 ;
