nQueens0.mod
============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`nQueens0.mod <EXAMPLES/LOGIC/EXAMPLES/nQueens0.mod>`

.. code-block:: ampl

    
    param n;
    
    set ROWS := {1..n};
    set COLUMNS := {1..n};
    
    var X{ROWS, COLUMNS} binary; 
       # X[i,j] is one if there is a queen at (i,j); else zero
    
    #maximize max_queens: sum {i in ROWS, j in COLUMNS} X[i,j];
    
    subject to column_attacks {j in COLUMNS}:
    	sum {i in ROWS} X[i,j] = 1;
    
    subject to row_attacks {i in ROWS}:
    	sum {j in COLUMNS} X[i,j] = 1;
    
    subject to diagonal1_attacks {k in 2..2*n}:
    	sum {i in ROWS, j in COLUMNS: i+j=k} X[i,j] <= 1;
    
    subject to diagonal2_attacks {k in -(n-1)..(n-1)}:
    	sum {i in ROWS, j in COLUMNS: i-j=k} X[i,j] <= 1;
