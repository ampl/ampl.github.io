netasgn.mod
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`netasgn.mod <EXAMPLES/EXAMPLES2/netasgn.mod>`

.. code-block:: ampl

    set PEOPLE;
    set PROJECTS;
    
    set ABILITIES within (PEOPLE cross PROJECTS);
    
    param supply {PEOPLE} >= 0;   # hours each person is available
    param demand {PROJECTS} >= 0; # hours each project requires
    
    check: sum {i in PEOPLE} supply[i] = sum {j in PROJECTS} demand[j];
    
    param cost {ABILITIES} >= 0;   # cost per hour of work
    param limit {ABILITIES} >= 0;  # maximum contributions to projects
    
    var Assign {(i,j) in ABILITIES} >= 0, <= limit[i,j];
    
    minimize Total_Cost:
       sum {(i,j) in ABILITIES} cost[i,j] * Assign[i,j];
    
    subject to Supply {i in PEOPLE}:
       sum {(i,j) in ABILITIES} Assign[i,j] = supply[i];
    
    subject to Demand {j in PROJECTS}:
       sum {(i,j) in ABILITIES} Assign[i,j] = demand[j];
