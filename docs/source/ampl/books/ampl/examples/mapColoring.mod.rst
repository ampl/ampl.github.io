mapColoring.mod
===============


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

    
    To explore examples showcasing these recent features, please visit:

    - `AMPL Streamlit Apps <https://ampl.com/streamlit/>`__
    - `AMPL+Python Book <https://ampl.com/mo-book/>`__
    - `AMPL Colab Notebooks <https://ampl.com/colab/>`__

:download:`mapColoring.mod <EXAMPLES/LOGIC/EXAMPLES/mapColoring.mod>`

.. code-block:: ampl

    param NumColors;
    
    set Countries;
    set Neighbors within Countries cross Countries;
    
    var color{Countries} integer >= 1 <= NumColors;
    
    s.t. different_colors{(c1, c2) in Neighbors}:
      color[c1] != color[c2];
    
    data;
    
    param NumColors := 4;
    
    set Countries := Belgium Denmark France Germany Luxembourg Netherlands;
    
    set Neighbors :=
      Belgium France 
      Belgium Germany 
      Belgium Netherlands
      Belgium Luxembourg
      Denmark Germany 
      France  Germany 
      France  Luxembourg
      Germany Luxembourg
      Germany Netherlands;
