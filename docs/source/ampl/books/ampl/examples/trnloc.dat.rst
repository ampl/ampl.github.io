trnloc.dat
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`trnloc.dat <EXAMPLES/LOOP2/trnloc.dat>`

.. code-block:: ampl

    
    param: ORIG: supply := 
       1 23070    6 21090   11 22690   16 17110   21 16720
       2 18290    7 16650   12 19360   17 15380   22 21540
       3 20010    8 18420   13 22330   18 18690   23 16500
       4 15080    9 19160   14 15440   19 20720   24 15310
       5 17540   10 18860   15 19330   20 21220   25 18970 ;
    
    param: DEST: demand :=
            A3    12000
            A6    12000
            A8    14000
            A9    13500
            B2    25000
            B4    29000 ;
    
    param fix_cost  default 500000 ;
    
    param var_cost:
    
              A3      A6      A8       A9      B2      B4  :=
        1   73.78   14.76   86.82    91.19   51.03   76.49
        2   60.28   20.92   76.43    83.99   58.84   68.86
        3   58.18   21.64   69.84    72.39   61.64   58.39
        4   50.37   21.74   61.49    65.72   60.48   56.68
        5   42.73   35.19   44.11    58.08   65.76   55.51
        6   44.62   39.21   44.44    48.32   76.12   51.17
        7   49.31   51.72   36.27    42.96   84.52   49.61
        8   50.79   59.25   22.53    33.22   94.30   49.66
        9   51.93   72.13   21.66    29.39   93.52   49.63
       10   65.90   13.07   79.59    86.07   46.83   69.55
       11   50.79    9.99   67.83    78.81   49.34   60.79
       12   47.51   12.95   59.57    67.71   51.13   54.65
       13   39.36   19.01   56.39    62.37   57.25   47.91
       14   33.55   30.16   40.66    48.50   60.83   42.51
       15   34.17   40.46   40.23    47.10   66.22   38.94
       16   41.68   53.03   22.56    30.89   77.22   35.88
       17   42.75   62.94   18.58    27.02   80.36   40.11
       18   46.46   71.17   17.17    21.16   91.65   41.56
       19   56.83    8.84   83.99    91.88   41.38   67.79
       20   46.21    2.92   68.94    76.86   38.89   60.38
       21   41.67   11.69   61.05    70.06   43.24   48.48
       22   25.57   17.59   54.93    57.07   44.93   43.97
       23   28.16   29.39   38.64    46.48   50.16   34.20
       24   26.97   41.62   29.72    40.61   59.56   31.21
       25   34.24   54.09   22.13    28.43   69.68   24.09 ;
