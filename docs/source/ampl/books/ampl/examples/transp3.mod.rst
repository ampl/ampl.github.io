transp3.mod
===========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

:download:`transp3.mod <EXAMPLES/EXAMPLES2/transp3.mod>`

.. code-block:: ampl

    set ORIG;   # origins
    set DEST;   # destinations
    
    set LINKS within {ORIG,DEST};
    
    param supply {ORIG} >= 0;   # amounts available at origins
    param demand {DEST} >= 0;   # amounts required at destinations
    
       check: sum {i in ORIG} supply[i] = sum {j in DEST} demand[j];
    
    param cost {LINKS} >= 0;   # shipment costs per unit
    var Trans {LINKS} >= 0;    # units to be shipped
    
    minimize Total_Cost:
       sum {(i,j) in LINKS} cost[i,j] * Trans[i,j];
    
    subject to Supply {i in ORIG}:
       sum {(i,j) in LINKS} Trans[i,j] = supply[i];
    
    subject to Demand {j in DEST}:
       sum {(i,j) in LINKS} Trans[i,j] = demand[j];
    
