# How to install AMPL

After downloading your AMPL & Solvers bundle from the [AMPL Portal](https://portal.ampl.com),
please follow the instructions below that correspond to your operating system:

- [How to install AMPL](#how-to-install-ampl)
  - [Google Colab](#google-colab)
  - [Python](#python)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)

## Google Colab

[AMPL Model Colaboratory](https://ampl.com/colab/) is a collection of AMPL models in Jupyter Notebooks that run on platforms such as **Google Colab**, **Kaggle**, **Gradient**, and **AWS SageMaker**. In order to be use AMPL on these notebook platforms you just need to following two code blocks
at the beginning of your notebook:

```bash
# Install dependencies
%pip install -q amplpy
```

```python
# Google Colab & Kaggle integration
from amplpy import AMPL, ampl_notebook
ampl = ampl_notebook(
    modules=["gurobi", "cbc", "highs"], # modules to install
    license_uuid="default") # license to use
```

## Python

[AMPL and all solvers are now available as python packages](amplpy.modules) for **Windows, Linux (X86_64, aarch64, ppc64le), and macOS**. For instance, to install AMPL with HiGHS, CBC and Gurobi,
you just need the following:

```bash
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
```

## Windows

**For Windows, we have an installer available that asks for your license UUID during the installation process.**

In case you have AMPL already installed, activate your license if you received a license UUID (e.g., [AMPL CE](https://ampl.com/ce) or [AMPL for Courses](https://ampl.com/courses) licenses):

Run this command in AMPL to activate your license:
```
ampl: shell "amplkey activate --uuid <license-uuid>";
      # replace <license-uuid> by the license UUID
```
Note: you need to restart AMPL in order to start using the new license.

```{note}
**It is recommended to install AMPL in your home folder.**
Otherwise, if you use dynamic cloud licenses, make sure the AMPL folder is not read-only (e.g., it will not work if installed at `"C:\Program Files\AMPL"`).
```

## macOS

**For macOS, we have an installer available that asks for the license UUID at the end for the installation process.**

In case you have AMPL already installed, activate your license if you received a license UUID (e.g., [AMPL CE](https://ampl.com/ce) or [AMPL for Courses](https://ampl.com/courses) licenses):

Run this command in AMPL to activate your license:
```
ampl: shell "amplkey activate --uuid <license-uuid>";
      # replace <license-uuid> by the license UUID
```
Note: you need to restart AMPL in order to start using the new license.

## Linux

1. **To install:**
   
    Download and extract your bundle above. This will be your AMPL directory. Rename it if you like, and move it anywhere on your computer that you want.

    ```{warning}
    Please make sure you place AMPL in a **directory where you have write permissions** such as your home directory. Otherwise, please see the note at the end.
    ```

2. **To run via IDE:**
    
    Inside your AMPL folder, enter the directory named `amplide` and run the `amplide` executable.

3. **To run via the command line:**

    In a command window, use cd to go to your AMPL directory, then type `./ampl` at the system prompt. Then you will see an `ampl:` prompt and can proceed to type AMPL commands.

4. **Activate your license if you received a license UUID (e.g., [AMPL CE](https://ampl.com/ce) licenses):**

    Run this command in AMPL to activate your license:
    ```
    ampl: shell "amplkey activate --uuid <license-uuid>";
          # replace <license-uuid> by the license UUID
    ```
    Note: you need to restart AMPL in order to start using the new license.

```{note}
**If you install AMPL somewhere in your home directory, you do not need to worry about the following.**

If you use cloud licenses (e.g., [AMPL Community Edition](https://ampl.com/ce/) licenses), **the AMPL directory cannot be read-only**. If really you want to have AMPL installed on a read-only directory, you need to set the environment
variables `AMPL_LICFILE` to a location where you store `ampl.lic` and where you have permissions to write, and set `AMPLKEY_RUNTIME_DIR` to a temporary directory.

For instance, assuming that you want to install AMPL on a Linux system in the `/opt` directory, which is not writeable by normal users. To install AMPL and dynamic licenses, you need to do the following:

1. Unpack the AMPL tarball into `/opt` as root user. The executables should then be at
`/opt/ampl.linux-intel64/`.
2. For each user that wants to use this AMPL installation with his own license:
    1. Define environment variables to point to a writeable directory in the user home directory:
        ```bash
            export AMPL_LICFILE=$HOME/.ampl/ampl.lic
            export AMPLKEY_RUNTIME_DIR=$HOME/.ampl
            export PATH=/opt/ampl.linux-intel64/:$PATH
        ```
        and add those definitions to the `.bash_profile` or `.bashrc` of each user.
    2. Start a new terminal in order to load the new environment variable definitions.
    3. Run the `amplkey activate --uuid <license-uuid>` command in the terminal.
```
