(cuopt)=

# NVIDIA cuOpt

NVIDIA [cuOpt](https://www.nvidia.com/en-eu/ai-data-science/products/cuopt/)  is an open-source GPU-accelerated optimization engine delivering near real-time solutions for complex decision-making challenges.
The driver is built on the [MP library](https://mp.ampl.com/), which reformulates
logical and other expressions that the solver does not accept natively.

[Try cuOpt on Google Colab using NVIDIA GPUs for free!](https://ampl.com/cuOpt)

[Learn More](https://ampl.com/products/solvers/open-source-solvers/)
| [Modeling guide](https://mp.ampl.com/model-guide.html)
| [Features](#features)
| [Options](#solver-options)
| [Changes](changes.md)

## System requirements

### CUDA/GPU requirements
* CUDA 12.0+
* NVIDIA driver >= 525.60.13 (Linux) and >= 527.41 (Windows)
* Volta architecture or better (Compute Capability >=7.0)

### OS requirements
* Only Linux is supported and Windows via WSL2
  * x86_64 (64-bit)
  * aarch64 (64-bit)

### Container
Use a container from [here](https://hub.docker.com/r/nvidia/cuda) is reccomended; the *runtime* tag is needed, as it includes needed maths libraries. 
An example of supported container is::

    $ docker run -it --rm --gpus all nvidia/cuda:12.9.0-runtime-ubuntu24.04 /bin/bash

## How to use it

```{eval-rst}

.. tab-set::

   .. tab-item:: Python
   
        How to install:

        .. code-block:: bash

            # Install Python API for AMPL:
            $ python -m pip install amplpy --upgrade

            # Install AMPL & solver modules:
            $ python -m amplpy.modules install cuopt # install cuopt

            # Activate your license (e.g., free ampl.com/ce or ampl.com/academia licenses):
            $ python -m amplpy.modules activate <your-license-uuid>

        How to use:

        .. code-block:: python

            from amplpy import AMPL
            ampl = AMPL()
            ...
            ampl.solve(solver="cuopt", cuopt_options="option1=value1 option2=value2")

        `Try cuOpt on Google Colab using NVIDIA GPUs for free! <https://ampl.com/cuOpt>`_

        Learn more about what we have to offer to implement and deploy `Optimization in Python <https://ampl.com/python/>`_.

   .. include:: /solvers/_include/other_apis.rst.inc

   .. tab-item:: AMPL

        .. code-block:: ampl

            ampl: option solver cuopt; # change the solver
            ampl: option cuopt_options 'option1=value1 option2=value2'; # specify options
            ampl: solve; # solve the problem
```

## Resources

* [Modeling guide](https://mp.ampl.com/model-guide.html)
* [Solver options](#solver-options)
* [Solve result codes](#retrieving-solutions)
* [Driver sources](https://github.com/ampl/mp/tree/develop/solvers/cuoptmp)

## Features

### Problem types and algorithms

:::{dropdown} Problem types
:open:
* LP
* MILP

Logical and nonlinear expressions are reformulated by MP.
:::

:::{dropdown} LP: PDLP on the GPU, dual simplex
`alg:method`: `0` concurrent (default), `1` PDLP, `2` dual simplex. PDLP
settings: `alg:solver_mode` (`1` Stable2, default).
:::

:::{dropdown} MIP
Relative and absolute tolerances: `mip:reltol`, `mip:abstol`.
:::

### Instrumentation

For a generic summary of the options and features used most often, see
[Important features](https://mp.ampl.com/features-guide.html#important-features)
in the MP documentation.

```{include} features.inc
```

## Solver options

Full list of solver options:
```{toctree}
options.md
```

More details on solver options: [MP solver options](https://mp.ampl.com/features-guide.html#solver-options).

## Retrieving solutions

The outcome of the last optimization is stored in the AMPL parameter `solve_result_num` and the relative message in
`solve_result`.

```ampl
display solve_result_num, solve_result;
```

cuOpt solve result codes can be obtained by running `cuopt -!` or `ampl: shell "cuopt -!";`:
```
        0- 99 solved: optimal for an optimization problem,
            feasible for a satisfaction problem
    100-199 solved? solution candidate returned but error likely
        150 solved? MP solution check failed (option sol:chk:fail)
    200-299 infeasible
    300-349 unbounded, feasible solution returned
    350-399 unbounded, no feasible solution returned
    400-449 limit, feasible: stopped, e.g., on iterations or Ctrl-C
    450-469 limit, problem is either infeasible or unbounded.
            Disable dual reductions or run IIS finder for definitive answer.
    470-499 limit, no solution returned
    500-999 failure, no solution returned
        550 failure: numeric issue, no feasible solution
```

For general information, see [MP result codes guide](https://mp.ampl.com/features-guide.html#solve-result-codes).

## Changelog

```{toctree}
changes.md
```
