steelT.sa1b
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    To programmatically interact with your models you should use :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>`.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelT.sa1b <EXAMPLES/LOOP1/steelT.sa1b>`

.. code-block:: ampl

    
    option display_1col 0;
    option omit_zero_rows 0;
    display Make >steelT.sens;
    display Sell >steelT.sens;
    
    option display_1col 20;
    option omit_zero_rows 1;
    display Inv >steelT.sens;
