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
    from amplpy import AMPL, tools
    ampl = tools.ampl_notebook(
        modules=["coin", "highs", "gokestrel"], # modules to install
        license_uuid="default", # license to use
        g=globals()) # instantiate AMPL object and register magics

In the list ``MODULES`` you can specify the AMPL solvers you want to use in your notebook.
Full list of AMPL modules available: ``amplgsl``, ``baron``, ``cbc``, ``coin``, ``conopt``, ``copt``, ``cplex``, ``gokestrel``, ``gurobi``, ``highs``, ``knitro``, ``lgo``, ``lindoglobal``, ``loqo``, ``minos``, ``octeract``, ``open``, ``plugins``, ``snopt``, ``xpress``.

.. raw:: html

    <a href="https://colab.ampl.com" target="_blank">
        <video width="100%" autoplay loop muted poster="https://ampl.com/upload/videos/nqueens_poster.jpg">
            <source src="https://ampl.com/upload/videos/nqueens.mp4" type="video/mp4" />
        </video>
    </a>

[`AMPL Model Colaboratory <https://colab.ampl.com>`_] [`N-Queens notebook <https://colab.research.google.com/github/ampl/amplcolab/blob/master/authors/glebbelov/miscellaneous/nqueens.ipynb>`_] [`https://try.ampl.com <https://try.ampl.com>`_]

.. grid:: 1 1 2 2
    :gutter: 0
    :margin: 0
    :padding: 0

    .. grid-item-card::
        :margin: 0
        :padding: 0

        You can use the **Christmas notebook** written by `ChatGPT <https://chat.openai.com/>`_ to get started:

        .. image:: https://colab.research.google.com/assets/colab-badge.svg
            :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open In Colab

        .. image:: https://kaggle.com/static/images/open-in-kaggle.svg
            :target: https://kaggle.com/kernels/welcome?src=https://github.com/ampl/amplcolab/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Kaggle

        .. image:: https://assets.paperspace.io/img/gradient-badge.svg
            :target: https://console.paperspace.com/github/ampl/amplcolab/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Gradient

        .. image:: https://studiolab.sagemaker.aws/studiolab.svg
            :target: https://studiolab.sagemaker.aws/import/github/ampl/amplcolab/blob/master/authors/fdabrandao/chatgpt/christmas.ipynb
            :alt: Open In SageMaker Studio Lab

        | BTW: you can even ask `ChatGPT <https://chat.openai.com/>`_ to write models for you! If it makes mistakes you can ask for help in our new `Discourse Forum <https://discuss.ampl.com>`_!

    .. grid-item-card::
        :margin: 0
        :padding: 0

        .. figure:: https://colab.ampl.com/_images/3lines.png
            :alt: the only 3 lines you need to use AMPL on Colab
            :align: center
            :width: 100%
            :target: https://colab.research.google.com/github/ampl/amplcolab/blob/master/template/minimal.ipynb

