sched.mod
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

:download:`sched.mod <EXAMPLES/EXAMPLES2/sched.mod>`

.. code-block:: ampl

    set SHIFTS;               # shifts
    
    param Nsched;             # number of schedules;
    set SCHEDS = 1..Nsched;   # set of schedules
    
    set SHIFT_LIST {SCHEDS} within SHIFTS;
    
    param rate {SCHEDS} >= 0;
    param required {SHIFTS} >= 0;
    
    minimize Total_Cost;
    subject to Shift_Needs {i in SHIFTS}: to_come >= required[i];
    
    var Work {j in SCHEDS} >= 0,
       obj Total_Cost rate[j], 
       coeff {i in SHIFT_LIST[j]} Shift_Needs[i] 1;
    
