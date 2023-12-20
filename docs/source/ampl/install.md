# How to install AMPL

After downloading your AMPL & Solvers bundle from the [AMPL Portal](https://portal.ampl.com),
please follow the instructions below that correspond to your operating system:

- [How to install AMPL](#how-to-install-ampl)
  - [Windows](#windows)
  - [Linux](#linux)
  - [macOS](#macos)

## Windows

**For Windows we have an installer available that we strongly recommend using instead
of following the old manual procedure with zip packages.** In case you want to install
according to the old procedure, the instructions are the following:

1. **To install:**

    Download and extract your bundle. This will be your AMPL folder. Rename it if you like and move it to any convenient location on your computer.

    ```{warning}
    Please make sure you place `ampl.mswin64` in a **folder where you have write permissions** without Administrator access. For read-only locations please see the note at the end.
    ```

2. **To run via the IDE:**

    In your AMPL folder, enter the `amplide` folder and then double-click `amplide.exe` to start the IDE.

3. **To run via the commnad line:**

    Inside your AMPL folder, double-click the `sw.exe` icon and type `ampl` at the prompt in the window that appears. Then you will see an `ampl:` prompt and can proceed to type AMPL commands.

4. **Activate your license if you received a license UUID (e.g., [AMPL CE](https://ampl.com/ce) licenses):**

    Run this command in AMPL to activate your license:
    ```
    ampl: shell "amplkey activate --uuid <license-uuid>";
          # replace <license-uuid> by the license UUID
    ```
    Note: you need to restart AMPL in order to start using the new license.

```{note}
**If you install AMPL somewhere in your home directory, you do not need to worry about the following.**

If you use cloud licenses (e.g., [AMPL Community Edition](https://ampl.com/ce/) licenses), **the AMPL folder cannot be read-only** (e.g., `"C:\Program Files\ampl.mswin64"`). If really you want to have AMPL installed on a read-only folder, you need to set the environment
variables `AMPL_LICFILE` to a location where you store `ampl.lic` and where you have permissions to write, and set `AMPLKEY_RUNTIME_DIR` to a temporary folder.
```

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

## macOS

**For macOS we have an installer available that we strongly recommend using instead
of following the old manual procedure with tgz packages.** In case you want to install
according to the old procedure, the instructions are the following:

1. **To install:**

    1. Download and extract your bundle. This will be your AMPL folder. Rename it if you like and move it to any convenient location on your computer.

    2. Next, **you will need to tell macOS that your AMPL software is safe to run**. Double-click your AMPL folder to open it and then follow these steps:

        - Control-click the `ampl.command` file and select **'Open'** in the context menu.
        - If a warning message (**"macOS cannot verify the developer..."**) pops up, click **'Open'**.
        - A Terminal window will appear. After a few seconds, you will see `ampl:` in the last line in the window. You can now close the window. (If a warning message saying **"Do you want to terminate running processes in this window?"** pops up, click **'Terminate'**.)

        ```{warning}
        If this step is skipped, you will get errors such as: **"Amplide" is damaged and can't be opened.** You need to run ``ampl.command`` to tell macOS that your AMPL software is safe to run.
        ```

2. **To run via IDE:**

    In your AMPL folder, enter the `amplide` folder and then double-click the `Amplide` application (with a black cat’s-head icon) to start the IDE. (The first time you open the AMPL IDE, you might see a few **"Amplide would like to access files"** boxes at startup; click **OK** in each box to dismiss it.)

3. **To run via the command line:**

    In your AMPL folder, double-click `ampl`. You should see an `ampl:` prompt appear and can now proceed to enter AMPL commands.

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
```
