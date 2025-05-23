steelP.mod
==========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`steelP.mod <EXAMPLES/EXAMPLES2/steelP.mod>`

.. code-block:: ampl

    set ORIG;   # origins (steel mills)
    set DEST;   # destinations (factories)
    set PROD;   # products
    
    param rate {ORIG,PROD} > 0;     # tons per hour at origins
    param avail {ORIG} >= 0;        # hours available at origins
    param demand {DEST,PROD} >= 0;  # tons required at destinations
    
    param make_cost {ORIG,PROD} >= 0;        # manufacturing cost/ton
    param trans_cost {ORIG,DEST,PROD} >= 0;  # shipping cost/ton
    
    var Make {ORIG,PROD} >= 0;       # tons produced at origins
    var Trans {ORIG,DEST,PROD} >= 0; # tons shipped
    
    minimize Total_Cost:
       sum {i in ORIG, p in PROD} make_cost[i,p] * Make[i,p] +
       sum {i in ORIG, j in DEST, p in PROD}
    			trans_cost[i,j,p] * Trans[i,j,p];
    
    subject to Time {i in ORIG}:
       sum {p in PROD} (1/rate[i,p]) * Make[i,p] <= avail[i];
    
    subject to Supply {i in ORIG, p in PROD}:
       sum {j in DEST} Trans[i,j,p] = Make[i,p];
    
    subject to Demand {j in DEST, p in PROD}:
       sum {i in ORIG} Trans[i,j,p] = demand[j,p];
