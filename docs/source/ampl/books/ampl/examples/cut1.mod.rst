cut1.mod
========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`cut1.mod <EXAMPLES/LOOP2/cut1.mod>`

.. code-block:: ampl

    
    # ----------------------------------------
    # CUTTING STOCK USING PATTERNS
    # ----------------------------------------
    
    param roll_width > 0;         # width of raw rolls
     
    set WIDTHS;                   # set of widths to be cut
    param orders {WIDTHS} > 0;    # number of each width to be cut
    
    param nPAT integer >= 0;      # number of patterns
    set PATTERNS := 1..nPAT;      # set of patterns
    
    param nbr {WIDTHS,PATTERNS} integer >= 0;
    
       check {j in PATTERNS}: 
          sum {i in WIDTHS} i * nbr[i,j] <= roll_width;
    
                                # defn of patterns: nbr[i,j] = number
                                # of rolls of width i in pattern j
    
    var Cut {PATTERNS} integer >= 0;   # rolls cut using each pattern
    
    minimize Number:                   # minimize total raw rolls cut
       sum {j in PATTERNS} Cut[j];   
    
    subj to Fill {i in WIDTHS}:
       sum {j in PATTERNS} nbr[i,j] * Cut[j] >= orders[i];
    
                                       # for each width, total
                                       # rolls cut meets total orders
    
    # ----------------------------------------
    # KNAPSACK SUBPROBLEM FOR CUTTING STOCK
    # ----------------------------------------
    
    param price {WIDTHS} default 0.0;
    
    var Use {WIDTHS} integer >= 0;
    
    minimize Reduced_Cost:  
       1 - sum {i in WIDTHS} price[i] * Use[i];
    
    subj to Width_Limit:  
       sum {i in WIDTHS} i * Use[i] <= roll_width;
