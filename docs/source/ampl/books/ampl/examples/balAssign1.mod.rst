balAssign1.mod
==============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`balAssign1.mod <EXAMPLES/LOGIC/EXAMPLES/balAssign1.mod>`

.. code-block:: ampl

    
    # ------------------------------------------------
    # ANTI-ASSIGNMENT PROBLEM:
    # Assign people to groups
    # so that groups are as heterogeneous as possible
    # ------------------------------------------------
    # Version 2: Minimize "sum of deviations"
    # ------------------------------------------------
    
    # To make this problem harder,
    # decrease sample and/or increase numberGrps.
    
    set ALL_PEOPLE ordered;
    
    param sample integer > 0;
    param selection integer >= 0, < sample;
    set PEOPLE := {i in ALL_PEOPLE: ord(i) mod sample = selection};
    
    set CATEG;
    param type {ALL_PEOPLE,CATEG} symbolic;
    param typeWt {CATEG} >= 0;
    
    param numberGrps integer > 0;
    
    set TYPES {k in CATEG} := setof {i in PEOPLE} type[i,k];
    
    var Assign {i in PEOPLE} integer >= 1, <= numberGrps;
    
    var MinInGrp integer <= floor (card(PEOPLE)/numberGrps);
    var MaxInGrp integer >= ceil (card(PEOPLE)/numberGrps);
    
    var MinType {k in CATEG, t in TYPES[k]} integer
       <= floor (card {i in PEOPLE: type[i,k] = t} / numberGrps);
    
    var MaxType {k in CATEG, t in TYPES[k]} integer
       >= ceil (card {i in PEOPLE: type[i,k] = t} / numberGrps);
    
    minimize Variation:  (MaxInGrp - MinInGrp) +
       sum {k in CATEG, t in TYPES[k]} 
          typeWt[k] * (MaxType[k,t] - MinType[k,t]);
    
    subj to MinInGrpDefn {j in 1..numberGrps}:  
       MinInGrp <= numberof j in ({i in PEOPLE} Assign[i]);
    
    subj to MaxInGrpDefn {j in 1..numberGrps}:  
       MaxInGrp >= numberof j in ({i in PEOPLE} Assign[i]);
    
    subj to MinTypeDefn {j in 1..numberGrps, k in CATEG, t in TYPES[k]}:
       MinType[k,t] <= numberof j in ({i in PEOPLE: type[i,k] = t} Assign[i]);
    
    subj to MaxTypeDefn {j in 1..numberGrps, k in CATEG, t in TYPES[k]}:
       MaxType[k,t] >= numberof j in ({i in PEOPLE: type[i,k] = t} Assign[i]);
