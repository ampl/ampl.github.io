
.. _python_integration:

AMPL integration with Python
============================

.. image:: https://portal.ampl.com/dl/ads/python_ecosystem_horizontal.png
  :width: 100 %
  :target: https://amplopt.streamlit.app
  :alt: AMPL' All-New Python ecosystem

[`Model Colaboratory <http://colab.ampl.com>`_] [`AMPL on Streamlit <http://ampl.com/streamlit>`_] [`AMPL Community Edition <https://ampl.com/ce>`_]

:ref:`AMPL and all solvers are now available as python packages <amplpy.modules>` for **Windows, Linux (X86_64, aarch64, ppc64le), and macOS**. For instance, to install AMPL with HiGHS, CBC and Gurobi,
you just need the following:

.. code-block:: bash

    # Install Python API for AMPL
    $ python -m pip install amplpy --upgrade

    # Install solver modules (e.g., HiGHS, CBC, Gurobi)
    $ python -m amplpy.modules install highs cbc gurobi

    # Activate your license (e.g., free https://ampl.com/ce license)
    $ python -m amplpy.modules activate <license-uuid>

    # Import in Python
    $ python
    >>> from amplpy import AMPL
    >>> ampl = AMPL() # instantiate AMPL object

.. note::
  You can use a free `Community Edition license <https://ampl.com/ce>`_, which allows **free
  and perpetual use of AMPL with Open-Source solvers**.

.. code-block:: python

    # Minimal example:
    from amplpy import AMPL
    import pandas as pd
    ampl = AMPL()
    ampl.eval(r"""
        set A ordered;
        param S{A, A};
        param lb default 0;
        param ub default 1;
        var w{A} >= lb <= ub;
        minimize portfolio_variance:
            sum {i in A, j in A} w[i] * S[i, j] * w[j];
        s.t. portfolio_weights:
            sum {i in A} w[i] = 1;
    """)
    tickers, cov_matrix = # ... pre-process data in Python
    ampl.set["A"] = tickers
    ampl.param["S"] = pd.DataFrame(
        cov_matrix, index=tickers, columns=tickers
    ).unstack()
    ampl.option["solver"] = "gurobi"
    ampl.option["gurobi_options"] = "outlev=1"
    ampl.solve()
    assert ampl.get_value("solve_result") == "solved"
    sigma = ampl.get_value("sqrt(sum {i in A, j in A} w[i] * S[i, j] * w[j])")
    print(f"Volatility: {sigma*100:.1f}%")
    # ... post-process solution in Python

[`Python API <http://amplpy.readthedocs.io>`_] [`GitHub <https://github.com/ampl/amplpy>`_]

On Google Colab
~~~~~~~~~~~~~~~

You can also install AMPL on :ref:`Google Colab <colab>` (`where it is free by default <https://colab.ampl.com/getting-started.html#ampl-is-free-on-colab>`_) as follows:

.. code-block:: bash

    # Install dependencies
    !pip install -q amplpy
    # Google Colab & Kaggle integration
    from amplpy import AMPL, tools
    ampl = tools.ampl_notebook(
        modules=["coin", "highs", "gokestrel"], # modules to install
        license_uuid="default", # license to use
        g=globals()) # instantiate AMPL object and register magics


.. note::
    On Google Colab there is a default `AMPL Community
    Edition license <https://ampl.com/ce/>`_ that gives you **unlimited access to AMPL
    with open-source solvers** (e.g., HiGHS, CBC, Couenne, Ipopt, Bonmin)
    or with commercial solvers from the `NEOS Server <http://www.neos-server.org/>`_ as described in `Kestrel documentation <https://dev.ampl.com/solvers/kestrel.html>`_.

    In the list ``modules`` you need to include
    ``"gokestrel"`` to use the `kestrel <https://dev.ampl.com/solvers/kestrel.html>`_ driver;
    ``"highs"`` for the `HiGHS <https://highs.dev/>`_ solver;
    ``"coin"`` for the `COIN-OR <https://www.coin-or.org/>`_ solvers.
    To use other commercial solvers, your license needs to include the commercial solver (e.g., an AMPL CE commercial solver trial).

[`Model Colaboratory <http://colab.ampl.com>`_]

On Streamlit Cloud
~~~~~~~~~~~~~~~~~~

AMPL can be used on `Streamlit <https://streamlit.io/>`_ to produce interactive prescriptive analytics
applications.

Check it out on Streamlit Cloud: |RunOnStreamlit|

.. |RunOnStreamlit| image:: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
   :target: http://ampl.com/streamlit

- `💡 Modeling tips on Streamlit <http://ampl.com/streamlit/Modeling_Tips>`_
- `👑 M-Queens Problem <http://ampl.com/streamlit/N-Queens>`_
- `📈 Risk Return (Prescriptive Analytics example) <http://ampl.com/streamlit/Risk_Return>`_

[`AMPL on Streamlit <http://ampl.com/streamlit>`_]

See more
~~~~~~~~

.. toctree::
    :maxdepth: 2

    colab
    streamlit
    modules

