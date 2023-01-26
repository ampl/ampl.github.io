AMPL on Google Colab 
--------------------

`AMPL Model Colaboratory <https://colab.ampl.com>`_ is a collection of AMPL models in `Jupyter Notebooks <https://jupyter.org/>`_
that run on platforms such as **Google Colab**, **Kaggle**, **Gradient**, and **AWS SageMaker**.

In order to be use AMPL on these notebook platforms you just need to following two code blocks
at the beginning of your notebook:

.. code-block:: bash

   # Install dependencies
   !pip install -q amplpy


.. code-block:: python

   # Google Colab & Kaggle integration
   MODULES, LICENSE_UUID = ["coin", "highs", "gokestrel"], None
   from amplpy import tools
   ampl = tools.ampl_notebook(modules=MODULES, license_uuid=LICENSE_UUID, g=globals()) # instantiate AMPL object and register magics

In the list ``MODULES`` you can specify the AMPL solvers you want to use in your notebook.
Full list of AMPL modules available: ``amplgsl``, ``baron``, ``cbc``, ``coin``, ``conopt``, ``copt``, ``cplex``, ``gokestrel``, ``gurobi``, ``highs``, ``knitro``, ``lgo``, ``lindoglobal``, ``loqo``, ``minos``, ``octeract``, ``open``, ``plugins``, ``snopt``, ``xpress``.

.. raw:: html

    <a href="https://colab.ampl.com" target="_blank">
        <video width="100%" autoplay loop muted poster="https://ampl.com/upload/videos/nqueens_poster.jpg">
            <source src="https://ampl.com/upload/videos/nqueens.mp4" type="video/mp4" />
        </video>
    </a>

[`AMPL Model Colaboratory <https://colab.ampl.com>`_] [`N-Queens notebook <https://colab.research.google.com/github/ampl/amplcolab/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb>`_]