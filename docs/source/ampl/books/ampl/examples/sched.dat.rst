sched.dat
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For modern data transfer, we recommend using :ref:`APIs <apis>` such as our popular :ref:`Python API <python_integration>` or table handlers such as `amplxl <https://plugins.ampl.com/amplxl.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`sched.dat <EXAMPLES/EXAMPLES2/sched.dat>`

.. code-block:: ampl

    data;
    
    set SHIFTS := Mon1 Tue1 Wed1 Thu1 Fri1 Sat1
                  Mon2 Tue2 Wed2 Thu2 Fri2 Sat2
                  Mon3 Tue3 Wed3 Thu3 Fri3 ;
    
    param Nsched := 126 ;
    
    set SHIFT_LIST[  1] := Mon1 Tue1 Wed1 Thu1 Fri1 ;
    set SHIFT_LIST[  2] := Mon1 Tue1 Wed1 Thu1 Fri2 ;
    set SHIFT_LIST[  3] := Mon1 Tue1 Wed1 Thu1 Fri3 ;
    set SHIFT_LIST[  4] := Mon1 Tue1 Wed1 Thu1 Sat1 ;
    set SHIFT_LIST[  5] := Mon1 Tue1 Wed1 Thu1 Sat2 ;
    set SHIFT_LIST[  6] := Mon1 Tue1 Wed1 Thu2 Fri2 ;
    set SHIFT_LIST[  7] := Mon1 Tue1 Wed1 Thu2 Fri3 ;
    set SHIFT_LIST[  8] := Mon1 Tue1 Wed1 Thu2 Sat1 ;
    set SHIFT_LIST[  9] := Mon1 Tue1 Wed1 Thu2 Sat2 ;
    set SHIFT_LIST[ 10] := Mon1 Tue1 Wed1 Thu3 Fri3 ;
    set SHIFT_LIST[ 11] := Mon1 Tue1 Wed1 Thu3 Sat1 ;
    set SHIFT_LIST[ 12] := Mon1 Tue1 Wed1 Thu3 Sat2 ;
    set SHIFT_LIST[ 13] := Mon1 Tue1 Wed1 Fri1 Sat1 ;
    set SHIFT_LIST[ 14] := Mon1 Tue1 Wed1 Fri1 Sat2 ;
    set SHIFT_LIST[ 15] := Mon1 Tue1 Wed1 Fri2 Sat2 ;
    set SHIFT_LIST[ 16] := Mon1 Tue1 Wed2 Thu2 Fri2 ;
    set SHIFT_LIST[ 17] := Mon1 Tue1 Wed2 Thu2 Fri3 ;
    set SHIFT_LIST[ 18] := Mon1 Tue1 Wed2 Thu2 Sat1 ;
    set SHIFT_LIST[ 19] := Mon1 Tue1 Wed2 Thu2 Sat2 ;
    set SHIFT_LIST[ 20] := Mon1 Tue1 Wed2 Thu3 Fri3 ;
    set SHIFT_LIST[ 21] := Mon1 Tue1 Wed2 Thu3 Sat1 ;
    set SHIFT_LIST[ 22] := Mon1 Tue1 Wed2 Thu3 Sat2 ;
    set SHIFT_LIST[ 23] := Mon1 Tue1 Wed2 Fri1 Sat1 ;
    set SHIFT_LIST[ 24] := Mon1 Tue1 Wed2 Fri1 Sat2 ;
    set SHIFT_LIST[ 25] := Mon1 Tue1 Wed2 Fri2 Sat2 ;
    set SHIFT_LIST[ 26] := Mon1 Tue1 Wed3 Thu3 Fri3 ;
    set SHIFT_LIST[ 27] := Mon1 Tue1 Wed3 Thu3 Sat1 ;
    set SHIFT_LIST[ 28] := Mon1 Tue1 Wed3 Thu3 Sat2 ;
    set SHIFT_LIST[ 29] := Mon1 Tue1 Wed3 Fri1 Sat1 ;
    set SHIFT_LIST[ 30] := Mon1 Tue1 Wed3 Fri1 Sat2 ;
    set SHIFT_LIST[ 31] := Mon1 Tue1 Wed3 Fri2 Sat2 ;
    set SHIFT_LIST[ 32] := Mon1 Tue1 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[ 33] := Mon1 Tue1 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[ 34] := Mon1 Tue1 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[ 35] := Mon1 Tue1 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[ 36] := Mon1 Tue2 Wed2 Thu2 Fri2 ;
    set SHIFT_LIST[ 37] := Mon1 Tue2 Wed2 Thu2 Fri3 ;
    set SHIFT_LIST[ 38] := Mon1 Tue2 Wed2 Thu2 Sat1 ;
    set SHIFT_LIST[ 39] := Mon1 Tue2 Wed2 Thu2 Sat2 ;
    set SHIFT_LIST[ 40] := Mon1 Tue2 Wed2 Thu3 Fri3 ;
    set SHIFT_LIST[ 41] := Mon1 Tue2 Wed2 Thu3 Sat1 ;
    set SHIFT_LIST[ 42] := Mon1 Tue2 Wed2 Thu3 Sat2 ;
    set SHIFT_LIST[ 43] := Mon1 Tue2 Wed2 Fri1 Sat1 ;
    set SHIFT_LIST[ 44] := Mon1 Tue2 Wed2 Fri1 Sat2 ;
    set SHIFT_LIST[ 45] := Mon1 Tue2 Wed2 Fri2 Sat2 ;
    set SHIFT_LIST[ 46] := Mon1 Tue2 Wed3 Thu3 Fri3 ;
    set SHIFT_LIST[ 47] := Mon1 Tue2 Wed3 Thu3 Sat1 ;
    set SHIFT_LIST[ 48] := Mon1 Tue2 Wed3 Thu3 Sat2 ;
    set SHIFT_LIST[ 49] := Mon1 Tue2 Wed3 Fri1 Sat1 ;
    set SHIFT_LIST[ 50] := Mon1 Tue2 Wed3 Fri1 Sat2 ;
    set SHIFT_LIST[ 51] := Mon1 Tue2 Wed3 Fri2 Sat2 ;
    set SHIFT_LIST[ 52] := Mon1 Tue2 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[ 53] := Mon1 Tue2 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[ 54] := Mon1 Tue2 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[ 55] := Mon1 Tue2 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[ 56] := Mon1 Tue3 Wed3 Thu3 Fri3 ;
    set SHIFT_LIST[ 57] := Mon1 Tue3 Wed3 Thu3 Sat1 ;
    set SHIFT_LIST[ 58] := Mon1 Tue3 Wed3 Thu3 Sat2 ;
    set SHIFT_LIST[ 59] := Mon1 Tue3 Wed3 Fri1 Sat1 ;
    set SHIFT_LIST[ 60] := Mon1 Tue3 Wed3 Fri1 Sat2 ;
    set SHIFT_LIST[ 61] := Mon1 Tue3 Wed3 Fri2 Sat2 ;
    set SHIFT_LIST[ 62] := Mon1 Tue3 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[ 63] := Mon1 Tue3 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[ 64] := Mon1 Tue3 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[ 65] := Mon1 Tue3 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[ 66] := Mon1 Wed1 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[ 67] := Mon1 Wed1 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[ 68] := Mon1 Wed1 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[ 69] := Mon1 Wed1 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[ 70] := Mon1 Wed2 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[ 71] := Mon2 Tue2 Wed2 Thu2 Fri2 ;
    set SHIFT_LIST[ 72] := Mon2 Tue2 Wed2 Thu2 Fri3 ;
    set SHIFT_LIST[ 73] := Mon2 Tue2 Wed2 Thu2 Sat1 ;
    set SHIFT_LIST[ 74] := Mon2 Tue2 Wed2 Thu2 Sat2 ;
    set SHIFT_LIST[ 75] := Mon2 Tue2 Wed2 Thu3 Fri3 ;
    set SHIFT_LIST[ 76] := Mon2 Tue2 Wed2 Thu3 Sat1 ;
    set SHIFT_LIST[ 77] := Mon2 Tue2 Wed2 Thu3 Sat2 ;
    set SHIFT_LIST[ 78] := Mon2 Tue2 Wed2 Fri1 Sat1 ;
    set SHIFT_LIST[ 79] := Mon2 Tue2 Wed2 Fri1 Sat2 ;
    set SHIFT_LIST[ 80] := Mon2 Tue2 Wed2 Fri2 Sat2 ;
    set SHIFT_LIST[ 81] := Mon2 Tue2 Wed3 Thu3 Fri3 ;
    set SHIFT_LIST[ 82] := Mon2 Tue2 Wed3 Thu3 Sat1 ;
    set SHIFT_LIST[ 83] := Mon2 Tue2 Wed3 Thu3 Sat2 ;
    set SHIFT_LIST[ 84] := Mon2 Tue2 Wed3 Fri1 Sat1 ;
    set SHIFT_LIST[ 85] := Mon2 Tue2 Wed3 Fri1 Sat2 ;
    set SHIFT_LIST[ 86] := Mon2 Tue2 Wed3 Fri2 Sat2 ;
    set SHIFT_LIST[ 87] := Mon2 Tue2 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[ 88] := Mon2 Tue2 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[ 89] := Mon2 Tue2 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[ 90] := Mon2 Tue2 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[ 91] := Mon2 Tue3 Wed3 Thu3 Fri3 ;
    set SHIFT_LIST[ 92] := Mon2 Tue3 Wed3 Thu3 Sat1 ;
    set SHIFT_LIST[ 93] := Mon2 Tue3 Wed3 Thu3 Sat2 ;
    set SHIFT_LIST[ 94] := Mon2 Tue3 Wed3 Fri1 Sat1 ;
    set SHIFT_LIST[ 95] := Mon2 Tue3 Wed3 Fri1 Sat2 ;
    set SHIFT_LIST[ 96] := Mon2 Tue3 Wed3 Fri2 Sat2 ;
    set SHIFT_LIST[ 97] := Mon2 Tue3 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[ 98] := Mon2 Tue3 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[ 99] := Mon2 Tue3 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[100] := Mon2 Tue3 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[101] := Mon2 Wed1 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[102] := Mon2 Wed1 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[103] := Mon2 Wed1 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[104] := Mon2 Wed1 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[105] := Mon2 Wed2 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[106] := Mon3 Tue3 Wed3 Thu3 Fri3 ;
    set SHIFT_LIST[107] := Mon3 Tue3 Wed3 Thu3 Sat1 ;
    set SHIFT_LIST[108] := Mon3 Tue3 Wed3 Thu3 Sat2 ;
    set SHIFT_LIST[109] := Mon3 Tue3 Wed3 Fri1 Sat1 ;
    set SHIFT_LIST[110] := Mon3 Tue3 Wed3 Fri1 Sat2 ;
    set SHIFT_LIST[111] := Mon3 Tue3 Wed3 Fri2 Sat2 ;
    set SHIFT_LIST[112] := Mon3 Tue3 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[113] := Mon3 Tue3 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[114] := Mon3 Tue3 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[115] := Mon3 Tue3 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[116] := Mon3 Wed1 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[117] := Mon3 Wed1 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[118] := Mon3 Wed1 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[119] := Mon3 Wed1 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[120] := Mon3 Wed2 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[121] := Tue1 Wed1 Thu1 Fri1 Sat1 ;
    set SHIFT_LIST[122] := Tue1 Wed1 Thu1 Fri1 Sat2 ;
    set SHIFT_LIST[123] := Tue1 Wed1 Thu1 Fri2 Sat2 ;
    set SHIFT_LIST[124] := Tue1 Wed1 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[125] := Tue1 Wed2 Thu2 Fri2 Sat2 ;
    set SHIFT_LIST[126] := Tue2 Wed2 Thu2 Fri2 Sat2 ;
    
    param rate  default 1 ;
    
    param required :=  Mon1 100  Mon2 78  Mon3 52 
                       Tue1 100  Tue2 78  Tue3 52
                       Wed1 100  Wed2 78  Wed3 52
                       Thu1 100  Thu2 78  Thu3 52
                       Fri1 100  Fri2 78  Fri3 52
                       Sat1 100  Sat2 78 ;
