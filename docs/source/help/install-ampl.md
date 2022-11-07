# AMPL installation instructions

After downloading your AMPL & Solvers bundle from the [AMPL Portal](https://portal.ampl.com),
please follow the instructions below that correspond to your operating system:

- [Windows](install-ampl.md#windows)
- [Linux](install-ampl.md#linux)
- [macOS](install-ampl.md#macos)

## Windows

1. **To install:**

    Download and extract your bundle. This will be your AMPL folder. Rename it if you like and move it to any convenient location on your computer.

2. **To run via the IDE:**

    In your AMPL folder, enter the `amplide` folder and then double-click `amplide.exe` to start the IDE.

3. **To run via the commnad line:**

    Inside your AMPL folder, double-click the `sw.exe` icon and type `ampl` at the prompt in the window that appears. Then you will see an `ampl:` prompt and can proceed to type AMPL commands.

```{note}
If you use cloud licenses (e.g., [AMPL Community Edition](https://ampl.com/ce/) licenses), **the AMPL folder cannot be read-only** (e.g., `"C:\Program Files\ampl.mswin64"`). If really you want to have AMPL installed on a read-only folder, you need to set the environment
variables `AMPL_LICFILE` to a location where you store `ampl.lic` and where you have permissions to write, and `AMPLKEY_RUNTIME_DIR` to a temporary folder.

**If you install AMPL somewhere in your home folder you should not need
to worry about this.**
```

## Linux

1. **To install:**
   
    Download and extract your bundle above. This will be your AMPL folder. Rename it if you like, and move it anywhere on your computer that you want.

2. **To run via IDE:**
    
    Inside your AMPL folder, enter the directory named `amplide` and run the `amplide` executable.

3. **To run via the command line:**

    In a command window, use cd to go to your AMPL directory, then type `./ampl` at the system prompt. Then you will see an `ampl:` prompt and can proceed to type AMPL commands.

```{note}
If you use cloud licenses (e.g., [AMPL Community Edition](https://ampl.com/ce/) licenses), **the AMPL directory cannot be read-only**. If really you want to have AMPL installed on a read-only directory, you need to set the environment
variables `AMPL_LICFILE` to a location where you store `ampl.lic` and where you have permissions to write, and `AMPLKEY_RUNTIME_DIR` to a temporary directory.

**If you install AMPL somewhere in your home directory you should not need to worry about this.**
```

## macOS

1. **To install:**

    1. Download and extract your bundle. This will be your AMPL folder. Rename it if you like and move it to any convenient location on your computer.

    1. Next, you will need to tell macOS that your AMPL software is safe to run. Double-click your AMPL folder to open it and then follow these steps:

        - Control-click the `ampl.command` file and select **'Open'** in the context menu.
        - If a warning message (**"macOS cannot verify the developer..."**) pops up, click **'Open'**.
        - A Terminal window will appear. After a few seconds, you will see `ampl:` in the last line in the window. You can now close the window. (If a warning message saying **"Do you want to terminate running processes in this window?"** pops up, click **'Terminate'**.)

2. **To run via IDE:**

    In your AMPL folder, enter the `amplide` folder and then double-click the `Amplide` application (with a black cat’s-head icon) to start the IDE. (The first time you open the AMPL IDE, you might see a few **"Amplide would like to access files"** boxes at startup; click **OK** in each box to dismiss it.)

3. **To run via the command line:**

    In your AMPL folder, double-click `ampl`. You should see an `ampl:` prompt appear and can now proceed to enter AMPL commands.

```{note}
If you use cloud licenses (e.g., [AMPL Community Edition](https://ampl.com/ce/) licenses), **the AMPL directory cannot be read-only**. If really you want to have AMPL installed on a read-only directory, you need to set the environment
variables `AMPL_LICFILE` to a location where you store `ampl.lic` and where you have permissions to write, and `AMPLKEY_RUNTIME_DIR` to a temporary directory.

**If you install AMPL somewhere in your home directory you should not need to worry about this.**
```