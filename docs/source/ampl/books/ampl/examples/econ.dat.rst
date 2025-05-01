econ.dat
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`econ.dat <EXAMPLES/EXAMPLES2/econ.dat>`

.. code-block:: ampl

    data;
    
    param: ACT:   cost  :=
            P1    2450      P1a   1290
            P2    1850      P2a   3700      P2b   2150
            P3    2200      P3c   2370
            P4    2170  ;
    
    param: PROD:  demand :=
           AA1     70000
           AC1     80000
           BC1     90000
           BC2     70000 
           NA2    400000
           NA3    800000  ;
    
    param io (tr):
             AA1  AC1  BC1  BC2   NA2   NA3 :=
       P1     60   20   10   15   938   295
       P1a     8    0   20   20  1180   770
       P2      8   10   15   10   945   440
       P2a    40   40   35   10   278   430
       P2b    15   35   15   15  1182   315
       P3     70   30   15   15   896   400
       P3c    25   40   30   30  1029   370
       P4     60   20   15   10  1397   450 ;
