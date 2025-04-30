singleHoist.mod
===============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

:download:`singleHoist.mod <EXAMPLES/LOGIC/EXAMPLES/singleHoist.mod>`

.. code-block:: ampl

    
    # Robert Rodosek and Mark Wallace
    # A Generic Model and Hybrid Algorithm for Hoist Scheduling Problems
    # in Michael J. Maher and Jean-Francois Puget eds.
    # Principles and Practice of Constraint Programming - CP98,
    # Springer, Lecture Notes in Computer Science, volume 1520, 1998.
    
    # Adapted from
    # www.g12.csse.unimelb.edu.au/minizinc/downloads/examples-latest/singHoist2.mzn
    
    param numTanks integer > 0;
    param numJobs integer > 0;
    
    param empty {0..numTanks, 0..numTanks};
    param full {0..numTanks};
    param minTime {1..numTanks};
    param maxTime {1..numTanks};
    
    param perMax = sum {i in 1..numTanks} maxTime[i];
    
    var Entry {0..numTanks} integer >= 0, <= numJobs * perMax;
    var Removal {0..numTanks} integer >= 0, <= numJobs * perMax;
    
    var Period integer >= 0, <= perMax;
    
    minimize Objective: Period;
    
    subj to Balance {t in 0..numTanks}:
       Removal[t] + full[t] = Entry[(t+1) mod (numTanks+1)];
    
    subj to EntRem {t in 1..numTanks}:
       Entry[t] + minTime[t] <= Removal[t] and
       Entry[t] + maxTime[t] >= Removal[t];
    
    subj to Disjoint {t1 in 0..numTanks-1, t2 in t1+1..numTanks, k in 1..numJobs-1}:
    
       Entry[(t1+1) mod (numTanks+1)] + empty[(t1+1) mod (numTanks+1),t2] <= Removal[t2] - k * Period or
       Entry[(t2+1) mod (numTanks+1)] + empty[(t2+1) mod (numTanks+1),t1] <= Removal[t1] + k * Period;
    
    subj to RemovalInit:
       Removal[0] = 0;
    
    subj to RemovalLImit:
       Removal[numTanks] + full[numTanks] <= numJobs * Period;
    
