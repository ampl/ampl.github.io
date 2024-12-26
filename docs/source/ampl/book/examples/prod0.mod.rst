prod0.mod
=========

:download:`prod0.mod <EXAMPLES/EXAMPLES2/prod0.mod>`

.. code-block:: ampl

    var XB;
    var XC;
    maximize Profit: 25 * XB + 30 * XC;
    subject to Time: (1/200) * XB + (1/140) * XC <= 40;
    subject to B_limit: 0 <= XB <= 6000;
    subject to C_limit: 0 <= XC <= 4000;
