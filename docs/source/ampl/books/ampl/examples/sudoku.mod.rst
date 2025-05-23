sudoku.mod
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`sudoku.mod <EXAMPLES/LOGIC/EXAMPLES/sudoku.mod>`

.. code-block:: ampl

    
    param given {1..9, 1..9} integer, in 0..9;
            # given[i,j] > 0 is the value given for row i, col j
            # given[i,j] = 0 means no value given
    
    var X {1..9, 1..9} integer, in 1..9;
            # x[i,j] = the number assigned to the cell in row i, col j
    
    subj to AssignGiven {i in 1..9, j in 1..9: given[i,j] > 0}:
       X[i,j] = given[i,j];
            # assign given values
    
    subj to Rows {i in 1..9}:
       alldiff {j in 1..9} X[i,j];
            # cells in the same row must be assigned distinct numbers
    
    subj to Cols {j in 1..9}:
       alldiff {i in 1..9} X[i,j];
            # cells in the same column must be assigned distinct numbers
    
    subj to Regions {I in 1..9 by 3, J in 1..9 by 3}:
       alldiff {i in I..I+2, j in J..J+2} X[i,j];
            # cells in the same region must be assigned distinct numbers
