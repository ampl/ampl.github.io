net2.dat
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`net2.dat <EXAMPLES/EXAMPLES2/net2.dat>`

.. code-block:: ampl

    data;
    
    param p_city := PITT ;
    
    set D_CITY := NE SE ;
    set W_CITY := BOS EWR BWI ATL MCO ;
    
    set DW_LINKS := (NE,BOS) (NE,EWR) (NE,BWI)
                    (SE,EWR) (SE,BWI) (SE,ATL) (SE,MCO);
    
    param p_supply := 450 ;
    
    param w_demand :=
      BOS  90,  EWR 120,  BWI 120,  ATL  70,  MCO  50;
    
    param:      cost  capacity  :=
      PITT NE    2.5    250
      PITT SE    3.5    250
    
      NE BOS     1.7    100
      NE EWR     0.7    100
      NE BWI     1.3    100
    
      SE EWR     1.3    100
      SE BWI     0.8    100
      SE ATL     0.2    100
      SE MCO     2.1    100 ;
