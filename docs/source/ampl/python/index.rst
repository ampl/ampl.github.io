
.. _python_integration:

AMPL integration with Python
============================

.. image:: https://portal.ampl.com/dl/ads/python_ecosystem_horizontal.png
  :width: 100 %
  :target: https://ampl.com/python
  :alt: AMPL' All-New Python ecosystem

:ref:`AMPL and all solvers are now available as python packages <amplpy.modules>` for Windows, Linux, and macOS. For instance, to install AMPL with HiGHS, CBC and Gurobi,
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

[`Python API <http://amplpy.readthedocs.io>`_] [`Available on Google Colab <http://colab.ampl.com>`_] [`GitHub <https://github.com/ampl/amplpy>`_] [`AMPL Community Edition <https://ampl.com/ce>`_]

.. toctree::
    :maxdepth: 2

    modules
    colab
    streamlit
