cut2.mod
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`cut2.mod <EXAMPLES/EXAMPLES2/cut2.mod>`

.. code-block:: ampl

    
      problem Cutting_Opt;
    # ----------------------------------------
    
    param nPAT integer >= 0, default 0;
    param roll_width;
    
    set PATTERNS = 1..nPAT;
    set WIDTHS;
    
    param orders {WIDTHS} > 0;
    param nbr {WIDTHS,PATTERNS} integer >= 0;
    
       check {j in PATTERNS}: sum {i in WIDTHS} i * nbr[i,j] <= roll_width;
    
    var Cut {PATTERNS} integer >= 0;
    
    minimize Number: sum {j in PATTERNS} Cut[j];
    
    subject to Fill {i in WIDTHS}:
       sum {j in PATTERNS} nbr[i,j] * Cut[j] >= orders[i];
    
    
      problem Pattern_Gen;
    # ----------------------------------------
    
    param price {WIDTHS} default 0;
    
    var Use {WIDTHS} integer >= 0;
    
    minimize Reduced_Cost:  
       1 - sum {i in WIDTHS} price[i] * Use[i];
    
    subject to Width_Limit:  
       sum {i in WIDTHS} i * Use[i] <= roll_width;
