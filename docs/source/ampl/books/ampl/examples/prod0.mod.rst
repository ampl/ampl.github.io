prod0.mod
=========


.. warning::
    The original AMPL book does not reflect many of the latest features available in AMPL.
    For example, it doesn't cover our new high-level modeling constructs that are `automatically reformulated <https://mp.ampl.com/model-guide.html>`_.

:download:`prod0.mod <EXAMPLES/EXAMPLES2/prod0.mod>`

.. code-block:: ampl

    var XB;
    var XC;
    maximize Profit: 25 * XB + 30 * XC;
    subject to Time: (1/200) * XB + (1/140) * XC <= 40;
    subject to B_limit: 0 <= XB <= 6000;
    subject to C_limit: 0 <= XC <= 4000;
