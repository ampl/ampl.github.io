# Basic commands

Before we delve into the details, we'll provide a brief summary of the AMPL concepts we're going to explore in this section:

:::{admonition} Section summary
In this section we will learn the following:

1. **Loading the model in AMPL interactively or via API calls:**
    
    :::::{tab-set}

    ::::{tab-item} Interactive
    ```ampl
    ampl: model lemonade.mod;
    ```
    ::::
    
    ::::{tab-item} Python
    ```python
    ampl.read("lemonade.mod")
    ```
    ::::
    
    ::::{tab-item} R
    ```r
    ampl$read("lemonade.mod")
    ```
    ::::

    ::::{tab-item} MATLAB
    ```matlab
    ampl.read('lemonade.mod')
    ```
    ::::
    
    ::::{tab-item} C++
    ```cpp
    ampl.read("lemonade.mod");
    ```
    ::::
    
    ::::{tab-item} C#
    ```cs
    ampl.Read("lemonade.mod");
    ```
    ::::
     
    ::::{tab-item} Java
    ```java
    ampl.read("lemonade.mod");
    ```
    ::::
    :::::

<br>

2. **Setting a solver and solving in AMPL interactively or via API calls:**
    :::::{tab-set}

    ::::{tab-item} Interactive
    ```ampl
    ampl: option solver highs; 
    ampl: solve;
    ```
    ::::
    
    ::::{tab-item} Python
    ```python
    ampl.set_option("solver", "highs")
    ampl.solve()
    ```
    ::::
    
    ::::{tab-item} R
    ```r
    ampl$setOption("solver", "highs")
    ampl$solve()
    ```
    ::::

    ::::{tab-item} MATLAB
    ```matlab
    ampl.setOption('solver', 'highs');
    ampl.solve();
    ```
    ::::
    
    ::::{tab-item} C++
    ```cpp
    ampl.setOption("solver", "highs");
    ampl.solve();
    ```
    ::::
    
    ::::{tab-item} C#
    ```cs
    ampl.SetOption("solver", "highs");
    ampl.Solve();
    ```
    ::::
     
    ::::{tab-item} Java
    ```java
    ampl.setOption("solver", "highs");
    ampl.solve();
    ```
    ::::
    :::::

<br>

3. **Displaying a solution in AMPL interactively or in a data-frame native to the API's language:**

    :::::{tab-set}
    
    ::::{tab-item} Interactive
    ```ampl
    $ ampl
    ampl: model lemonade.mod;
    ampl: option solver highs;
    ampl: solve;
    ampl: display lemonade, iced_tea, profit;
    ```
    ::::
    
    ::::{tab-item} Python
    ```{literalinclude} ampl_files/sp_lemonade.py
    :language: python
    :linenos: true
    :caption: sp_lemonade.py
    ```
    ::::
    
    ::::{tab-item} R
    ```{literalinclude} ampl_files/sp_lemonade.R
    :language: r
    :linenos: true
    :caption: sp_lemonade.R
    ```
    ::::

    ::::{tab-item} MATLAB
    ```matlab
    ampl.read('lemonade.mod')
    ampl.setOption('solver', 'highs');
    ampl.solve();
    
    %%% %%%%%%%%%%% %%%
    %%% COMING SOON %%%
    %%% %%%%%%%%%%% %%%
    ```
    ::::
    
    ::::{tab-item} C++
    ```{literalinclude} ampl_files/sp_lemonade.cc
    :language: cpp
    :linenos: true
    :caption: sp_lemonade.cc
    ``` 
    ::::
    
    ::::{tab-item} C#
    ```cs
    ampl.Read("lemonade.mod");
    ampl.SetOption("solver", "highs");
    ampl.Solve();
    
    /// /////////// ///
    /// COMING SOON ///
    /// /////////// ///
    ```
    ::::
      
    ::::{tab-item} Java
    ```java
    ampl.read("lemonade.mod");
    ampl.setOption("solver", "highs");
    ampl.solve();
    
    /// /////////// ///
    /// COMING SOON ///
    /// /////////// ///
    ```
    ::::
    :::::

<br>

:::


## Solving our first model
Now that we have formulated our first model in AMPL - the lemonade stand problem - we're ready to solve it and find the optimal solution.
To do this, we will need to invoke the AMPL interpreter, load our [lemonade.mod](ampl_files/lemonade.mod) file, set a desired solver, and issue a command to solve. 
Once the solution is obtained, we'll learn how to display it. 
In the following sections, we will go over the basics for each of these steps.

### Invoking the `ampl` interpreter
```{book-appendix} 
A.23 
```

Essentially, there are three ways to invoke the AMPL interpreter to solve our model.
One option is to start an interactive AMPL session by typing `ampl` into the terminal/command prompt.
Another option, which we will discuss in the next example, is to use AMPL non-interactively by writing a script containing AMPL commands.
As a third option, AMPL can be invoked from your favorite programming language (Python, R, C++, MATLAB and more!) through the [APIs](https://ampl.com/products/ampl/apis/).

:::{note}
In order to be able to use AMPL through the APIs, we first have to perform the **Initial Setup** steps for the programming language of our choosing.
These can be found on the language specific API pages, which are all accessible from our [APIs page](https://ampl.com/products/ampl/apis/).
:::

:::::{tab-set}

::::{tab-item} Interactive
```bash
$ ampl
ampl: 
```

::::

::::{tab-item} Python
```python
from amplpy import AMPL
# Create an AMPL instance
ampl = AMPL()
```
::::

::::{tab-item} R
```r
library(rAMPL)
# Create an AMPL instance
ampl <- new(AMPL)
```
::::

::::{tab-item} MATLAB
```matlab
% Create an AMPL instance
ampl = AMPL;
```
::::

::::{tab-item} C++
```cpp
#include "ampl/ampl.h"

int main(int argc, char **argv)
{
    // Create an AMPL instance
    ampl::AMPL ampl;
    return 0;
}
```
::::

::::{tab-item} C#
```cs
using ampl;
using ampl.Entities;

public static int Main(string[] args)
{
    AMPL ampl = new AMPL();
}
```
::::

::::{tab-item} Java
```java
import com.ampl.AMPL;

public class AMPLProgram {

    public static void main(String []args) {
    // Create an AMPL instance
    AMPL ampl = new AMPL();
   }
}
```
::::

:::::

:::::{tip}
When in interactive mode, if the closing semicolon from your statement is missing, the AMPL interpreter will wait for further input, which is indicated by the `ampl?` prompt. 
In order to return to the default state, simply type `;` and hit enter. For example,
::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: var lemonade
ampl? ;
ampl:
```
:::
::::
:::::

Regardless of the method chosen to invoke AMPL, we interact with it through commands.
In the following section, we will go over the commands necessary to solve our lemonade stand problem.


### AMPL commands
Commands are not part of an optimization model, but they prompt AMPL to perform certain actions.
For example, you can issue a command to load an AMPL model file, such as the [lemonade.mod](ampl_files/lemonade.mod)  we created earlier.
AMPL commands can be issued to AMPL as separate commands or via a file (a file containing AMPL commands is called an AMPL script). 
It is best practice to separate model files and commands. 
However, commands have the same effect regardless of whether they are issued separately or are embedded in a file. 

In terms of AMPL's APIs, once an AMPL object is successfully instantiated, we have the option to communicate commands to it via a file, a string, or by invoking methods of the AMPL object that correspond to AMPL commands.
To bring more emphasis to the commands being discussed, whenever possible, we will issue AMPL commands via APIs by invoking the corresponding methods on the AMPL object. 
However, in some cases, it could be more practical to embed AMPL commands into files or strings, which can then be passed to AMPL using a read-file or evaluate-string API call. 
In general, if there is a choice of which method to use, the decision will depend on the use case and extends beyond the scope of this tutorial.

After invoking/instantiating AMPL, the next step needed to solve a problem is to load a model file.
This requires AMPL to be in model mode. 
Our upcoming discussion will cover the different modes in AMPL, the commands for switching between them, and the command to terminate an AMPL session.

#### AMPL modes
AMPL recognizes two modes: **model** and **data**. 
We can switch between them by typing: 

:::::{tab-set}

::::{tab-item} Interactive

```ampl
ampl: model;
```
or
```ampl
ampl: data;
```
::::

::::{tab-item} Python

```python
ampl.eval("model;")
```
or
```python
ampl.eval("data;")
```
For more information about `eval()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
::::

::::{tab-item} R
```r
ampl$eval("model;")
```
or
```r
ampl$eval("data;")
```
For more information about `eval()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
::::

::::{tab-item} MATLAB
```matlab
ampl.eval('model;')
```
or
```matlab
ampl.eval('data;')
```
For more information about `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
::::

::::{tab-item} C++
```cpp
ampl.eval("model;")
```
or
```cpp
ampl.eval("data;")
```
For more information about `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
::::

::::{tab-item} C#
```cs
ampl.Eval("model;")
```
or
```cs
ampl.Eval("data;")
```
For more information about `Eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
::::

::::{tab-item} Java
```java
ampl.eval("model;")
```
or
```java
ampl.eval("data;")
```
For more information about `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
::::
:::::

For now, we will focus on the model mode, which is the default mode when starting ampl and is sufficient to solve our lemonade stand problem. 
In this mode, AMPL recognizes model declarations such as entities and expressions, as well as a set of commands.

#### Terminating/resetting an AMPL session
:::{important}
When using AMPL via the APIs the `quit;` or any terminating command will invalidate the instantiated AMPL object, which means it won't be able to receive further input. 
Therefore, it is best to avoid directly sending terminating commands to AMPL via API calls, as the API will automatically perform clean up operations and take care of closing the active AMPL sessions.
:::

To terminate an AMPL session in interactive mode, type the `quit` or `q` commands.
:::::{tab-set}

::::{tab-item} Interactive
```ampl
ampl: quit;
```
or
```ampl
ampl: q;
```
::::
:::::

:::::{admonition} Advanced: `exit` command
:class: dropdown

AMPL also offers the `exit` command, which is a synonym for `quit`, but it can return a status to the surrounding environment:
 
<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
   <span style="color: darkgreen; font-weight: bold">exit</span> <i>expression<sub>opt</sub></i> ;
</code>
</pre>

For example, in interactive mode, if our surrounding environment is [Bash](https://www.gnu.org/software/bash/) we could do the following:

::::{tab-set}
:::{tab-item} Interactive
```bash
$ ampl
ampl: exit 134;
$ echo $?
134
```
:::
::::
:::::

:::{important}
In AMPL, when utilizing APIs to replace or reload previously loaded model or data files, it's always necessary to execute one of AMPL's reset commands.
:::

The reset command has several forms:

1. `reset;` causes AMPL to forget all model declarations and data and to close all files opened by redirection, while retaining the current option settings.

2. `reset options;` causes AMPL to restore all options to their initial state. 

3. `reset data;` causes AMPL to forget all assignments read in data mode and allows reading data for a different problem instance.

:::::{tab-set}

::::{tab-item} Interactive
```ampl
ampl: reset;
```
::::

::::{tab-item} Python

```python
ampl.reset()
```
or
```python
ampl.eval("reset;")
```
For more information about `reset()` and `eval()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
::::

::::{tab-item} R
```r
ampl$reset()
```
or
```r
ampl$eval("reset;")
```
For more information about `reset()` and `eval()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
::::

::::{tab-item} MATLAB
```matlab
ampl.reset()
```
or
```matlab
ampl.eval('reset;')
```
For more information about `reset()` and `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
::::

::::{tab-item} C++
```cpp
ampl.reset()
```
or
```cpp
ampl.eval("reset;")
```
For more information about `reset()` and `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
::::

::::{tab-item} C#
```cs
ampl.Reset()
```
or
```cs
ampl.Eval("reset;")
```
For more information about `Reset()` and `Eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
::::

::::{tab-item} Java
```java
ampl.reset()
```
or
```java
ampl.eval("reset;")
```
For more information about `reset()` and `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
::::
:::::


Now that we have gained some understanding of how to invoke/terminate and reset AMPL, as well as the initial state AMPL defaults to after invocation, we are ready to complete the set of commands necessary to solve our lemonade stand problem. 
We will continue with the `include`, `solve`, and `option` commands.

```{note}
If you'd like to follow along and try out the commands on your computer, make sure you have either created or downloaded the [lemonade.mod](ampl_files/lemonade.mod) file beforehand.
```

#### `include`, `solve` and `option` commands
Below we will solve our lemonade model interactively.
To begin, we type `ampl` into our terminal/command prompt window, which should then display the `ampl:` prompt.
Then, we load our model using the `include` command (remembering that AMPL is already in model mode by default).
AMPL provides several commands that cause input to be taken from a file. 
For now, we will focus on using the `include` command.
Finally, we execute the `solve;` command to attempt to obtain the solution. 

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: include lemonade.mod
ampl: solve;
Error executing "solve" command:
No solver specified:  option solver is ''.
```
:::
::::

As we have not set a solver, AMPL returns an error.
AMPL requires that you first specify which solver you want it to use to solve your problem.
To that end AMPL maintains an option called `solver`.
For this example, we will set AMPL's `solver` option to use the solver `highs`. 
We achieve this by adding `option solver highs;` before our `solve;` command. 
Note that you could choose to use any other solver capable of solving integer programming problems.

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: include lemonade.mod
ampl: option solver highs;
ampl: solve;
HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes
```
:::
::::

The line beginning with `HIGHS 1.5.1` is returned by the solver, or to be more specific by AMPL's solver driver.
The distinction between the two will be explained in a later section.
It informs us that we have found an optimal solution and that the objective function value is 15.

Before we move on to displaying the solution, let's review how to perform the same tasks that we covered above using AMPL's APIs:

:::::{tab-set}

::::{tab-item} Python
```python
ampl.read("lemonade.mod")
ampl.set_option("solver", "highs")
ampl.solve()
```
For more information about `read()`, `setOption()` and `solve()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
::::

::::{tab-item} R
```r
ampl$read("lemonade.mod")
ampl$setOption("solver", "highs")
ampl$solve()
```
For more information about `read()`, `setOption()` and `solve()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
::::

::::{tab-item} MATLAB
```matlab
ampl.read('lemonade.mod')
ampl.setOption('solver', 'highs');
ampl.solve();
```
For more information about `read()`, `setOption()` and `solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
::::

::::{tab-item} C++
```cpp
ampl.read("lemonade.mod");
ampl.setOption("solver", "highs");
ampl.solve();
```
For more information about `read()`, `setOption()` and `solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
::::

::::{tab-item} C#
```cs
ampl.Read("lemonade.mod");
ampl.SetOption("solver", "highs");
ampl.Solve();
```
For more information about `Read()`, `SetOption()` and `Solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
::::

::::{tab-item} Java
```java
ampl.read("lemonade.mod");
ampl.setOption("solver", "highs");
ampl.solve();
```
For more information about `read()`, `setOption()` and `solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
::::
:::::


:::::{admonition} Advanced: `include`/`model` commands
:class: dropdown

The `include` command causes AMPL to replace the command with the contents of the named file. 
An include can even appear in the middle of another statement, and as mentioned earlier, does not require a terminating semicolon.

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">include</span> <i>filename </i>
</code>
</pre>

When AMPL is in model mode, we can always use the `include` command to load model files.
However, the most reliable way to load a model file would is to use the following sequence:
<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">model</span> ; <span style="color: darkgreen; font-weight: bold">include</span> <i>filename </i>
</code>
</pre>

This approach ensures that AMPL is in model mode before we attempt to load a model file. 
However, AMPL provides a shorthand for the above sequence of commands, which may be abbreviated as:

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">model</span> <i>filename </i>
</code>
</pre>

This command is more commonly used for loading model files because it guarantees that AMPL is in model mode before loading. 
**Going forward, we will use the `model` command to load all model files.**
Below, we illustrate how the example from above looks when `include` is replaced by `model`:

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod
ampl: option solver highs;
ampl: solve;
HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes
```
:::
::::
:::::

:::::{admonition} Advanced: `option` command
:class: dropdown

The behavior of AMPL commands and solvers is influenced by a variety of options.
For instance, the behavior of the `solve;` command depends on the value of the `solver` option.

Options in AMPL are similar to "environment variables" in Windows, MacOS, and Linux operating systems; in fact, AMPL inherits its initial options from these system environments. 
However, AMPL also provides its own default values for many options if they are not inherited. 

Each option has a name and a value that can be either a number or a character string. 
The option command allows you to examine and modify options, taking one of the following forms:


<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">option</span> <i>redirection<sub>opt</sub>  </i>;
    <span style="color: darkgreen; font-weight: bold">option</span> <i>name [ evalue ] [ , name [ evalue ] ... ] redirection<sub>opt</sub>  </i>;
</code>
</pre>


The first form displays all options that have been changed or for which AMPL may provide a default value.

The second form, when used without an *evalue*, prints the current value of option *name* (e.g. `option solver;` will print the value of `solver`). 
If an *evalue* is provided, it assigns that value to *name* (e.g. `option solver highs;` will assign the value `highs` to `solver`).

Options pertaining to a specific solver are set by providing values for the option <code> <i>solvername</i>_options </code>.
For example, to receive more output from HiGHS, we can set `outlev` to 1 by adding `highs_options "outlev=1"`.
Our updated example looks as follows: 

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod;                           
ampl: option solver highs, highs_options "outlev=1";
ampl: solve; 
HiGHS 1.5.1: tech:outlev=1
Running HiGHS 1.5.1 [date: 2023-02-27, git hash: 93f1876]
Copyright (c) 2023 HiGHS under MIT licence terms
Presolving model
1 rows, 2 cols, 2 nonzeros
1 rows, 2 cols, 2 nonzeros
Objective function is integral with scale 2

Solving MIP model with:
   1 rows
   2 cols (0 binary, 2 integer, 0 implied int., 0 continuous)
   2 nonzeros

        Nodes      |    B&B Tree     |            Objective Bounds              |  Dynamic Constraints |       Work      
     Proc. InQueue |  Leaves   Expl. | BestBound       BestSol              Gap |   Cuts   InLp Confl. | LpIters     Time

         0       0         0   0.00%   21              -inf                 inf        0      0      0         0     0.0s

Solving report
  Status            Optimal
  Primal bound      15
  Dual bound        15
  Gap               0% (tolerance: 0.01%)
  Solution status   feasible
                    15 (objective)
                    0 (bound viol.)
                    0 (int. viol.)
                    0 (row viol.)
  Timing            0.00 (total)
                    0.00 (presolve)
                    0.00 (postsolve)
  Nodes             1
  LP iterations     0 (total)
                    0 (strong br.)
                    0 (separation)
                    0 (heuristics)
HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes
``` 
:::
::::

For a [full list of HiGHS options](https://dev.ampl.com/solvers/highs/options.html) or options for other solvers, visit [dev.ampl.com/solvers](https://dev.ampl.com/solvers/).
:::::

:::::{admonition} Advanced: `solve` command
:class: dropdown

The `solve;` command initiates a series of activities, which are discussed in more detail in [Ch. 11](https://ampl.com/wp-content/uploads/Chapter-11-Modeling-Commands-AMPL-Book.pdf) of the AMPL book. 
In a nutshell, `solve;` causes AMPL to send the problem to a solver and to retrieve the solution from the solver.
Upon successful completion optimal variable values become available in AMPL for printing and other uses.

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">solve</span> <i>obj<sub>opt</sub> redirection<sub>opt</sub> </i>;
</code>
</pre>

The optional *obj* is the name of the objective to optimize.
It is useful when multiple objectives are declared in the model, to indicate which one is sent to the solver.
The optional *redirection* is for the solver's standard output.
By default, solvers work in the background silently. 
In some cases, it might be useful to know what the solver is doing.
As seen in the options section, we can set AMPL to display the solver's output on standard output. 
Yet, this could be too verbose in some cases, and we might want to save it in a file.
Below, we demonstrate how to redirect HiGHS' output to a file:

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod;
ampl: option solver highs, highs_options "outlev=1";
ampl: solve > highs.out;
HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
0 barrier iterations
``` 
:::
::::

The output seen in the options section is now saved in the file `highs.out`.
:::::


```{note}
As mentioned earlier, `include` commands in AMPL do not require a semicolon at the end. 
Similarly, `model filename` commands do not need a semicolon either.
However, adding a semicolon to these commands does not change AMPL's behavior, which is why you will often see modelers add a semicolon to end of these statements.
```

#### The `show` and `print` commands
AMPL provides a rich set of tools to examine model components and their values.
One of the most powerful tools is the `display` command, which has its own chapter ([Ch. 12](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf)) in the AMPL book. 
For now, it is enough to know that `display` performs automatic formatting. 
In general, any plain `print` command can be replaced with a `display` command, and it is best to use `display` for displaying indexed entities and sets.
We will formally introduce the `display` command in a {ref}`later section <the-display-command>`.

The `show` command is used to recall model components.
By itself, it lists the names of all components of the current model:

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod;
ampl: show;
parameter:   fee

variables:   iced_tea   lemonade

constraints:   lemon_constraint   sugar_constraint   tea_bag_constraint

objective:   profit
```
:::
::::

Additionally, we can display the declarations of individual components, which saves us the trouble of having to look them up in the model file. 
This can be achieved by simply listing the items we wish to examine after the `show` command, followed by the semicolon.

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod;
ampl: show profit;
maximize profit: 1.5*lemonade + iced_tea - fee;
```
:::
::::

The `print` and `printf` commands are used for displaying the values of model entities, such as optimal solution or objective function values.
The difference between them is that the `print` command does not perform any formatting, while the `printf` command requires an explicit description of the desired formatting.
Both `print` and `printf` commands take a list of arguments to be displayed, followed by the semicolon.

In the example below, after loading the model, we use `print` to obtain the value of our variables (`lemonade` and `iced_tea`) and our objective (`profit`).
Since AMPL initializes variables to zero by default, we get `0 0 -2`, which means that if we don't sell any iced tea or lemonade we incur a loss of $2. 
Next, we solve our problem and use `print` and `printf` commands to add spacing before and after the solver output.
Finally, using `printf`'s formatting features, we can display a brief business plan for the day, detailing how many drinks to make and what profits to expect. 
::::{tab-set}
:::{tab-item} Interactive
```bash
ampl: model lemonade.mod                              
ampl: print lemonade, iced_tea, profit;
0 0 -2
ampl: option solver highs;                            
ampl: print; solve; printf "\n";                      

HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes

ampl: printf "\nIf we make %d lemonade(s) and %d iced tea(s) then\
ampl? our maximum profit will be: $%.2f.\n", lemonade, iced_tea, profit;

If we make 6 lemonade(s) and 8 iced tea(s) then
our maximum profit will be: $15.00.
```
:::
::::

:::::{admonition} Advanced: `show` command
:class: dropdown

The command:

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">show</span> <i>namelist<sub>opt</sub> redirection<sub>opt</sub> </i>;
</code>
</pre>

can be used in 3 different ways:
1. List all model entities, which occurs when *namelist* is empty.
2. Recall an entity's declaration, such as that of `profit` shown above.
3. List all entities belonging to a certain category, such as variables, constraints, and objectives.

An example for the third use case would be to display the name of all constraints:

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod
ampl: show constraints;

constraints:   lemon_constraint   sugar_constraint   tea_bag_constraint
```
:::
::::

The table below, provides a list of entities that `show` accepts:

    | Entity type            | Accepted argument <br> (expressed as a regular expression) |
    | :--------------------- | :--------------------------------------------------------- |
    | checks                 | `ch.*`                                                     |
    | constraints            | `c[^h].*`                                                  |
    | environments           | `e.*`                                                      |
    | functions              | `f.*`                                                      |
    | objectives             | `o.*`                                                      |
    | parameters             | `p[^r].*`                                                  |
    | problems               | `pr.*`                                                     |
    | sets                   | `s[^u].*`                                                  |
    | suffixes               | `su.*`                                                     |
    | tables                 | `t.*`                                                      |
    | variables              | `v.*`                                                      |

The example below will help make sense of the above table:

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod
ampl: show p, pmt, pr, prblm, prof, profit;

parameter:   fee

parameter:   fee

problems: none

problems: none

problems: none
maximize profit: 1.5*lemonade + iced_tea - fee;
```
:::
::::

Both `p` and `pmt` match the regular expression `p[^r].*` but do not match names of declared entities, so `show` will display the names of all declared **parameters**.
For our example, we get `fee`.

`pr`, `prblm`, and `prof` match the regular expression `pr.*` and do not conflict with names of declared entities, so `show` command displays the names of all declared **problems**.
Since none were declared, we get `none`.

While `profit` matches the regex `pr.*` it is also a declared entity, so `show` displays its declaration. 
:::::


:::::{admonition} Advanced: `print` command
:class: dropdown


The `print` and `printf` commands print arbitrary expressions and have the following syntax:

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">print</span> <i>[ indexing: ] arglist redirection<sub>opt</sub> </i>;
    <span style="color: darkgreen; font-weight: bold">printf</span> <i>[ indexing: ] fmt , arglist redirection<sub>opt</sub> </i>;
</code>
</pre>

Optional clauses, such as *indexing* (marked with [ ]), are discussed in detail in the [AMPL book](https://ampl.com/learn/ampl-book/).

An *arglist* is a (possibly empty, comma-separated) list of expressions, such as `0.0725*profit`, which would give you the amount of sales tax you would have to pay in the state of California.

The `print` command prints the items in its *arglist* on one line, separated by spaces and terminated by a newline; the separator may be changed with option `print_separator`. 
By default, numeric expressions are printed to full precision, but this can be changed by a variety of options of which we will illustrate option `print_round`, as shown below. 

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod                           
ampl: option solver highs;                         
ampl: solve;
HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes
ampl: option print_separator ":  ", print_round 2;
ampl: print "Sales tax", 0.0725*profit;           
Sales tax:  1.09
```
:::
::::

The `printf` command allows us to control formatting.
It prints the items in its *arglist* as dictated by its format string `fmt`, which behaves like a `printf` format string in the C programming language.
Below, we will illustrate how to use `printf` to create a mini business plan and use redirect option to save the output to a text file:

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: model lemonade.mod                           
ampl: option solver highs;                         
ampl: solve;
HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes
ampl: printf "Things to make:\  
ampl? \t\tlemonade:\t%d\        
ampl? \t\ticed tea:\t%d\n\      
ampl? profit:\t\t$%.2f\         
ampl? tax:\t\t$%.2f\n",         
ampl? lemonade, iced_tea,       
ampl? profit,                   
ampl? 0.0725*profit > bplan.txt;
```
:::
::::

The `bplan.txt` (business plan) text file has the following content:

```
Things to make:
		lemonade:	6
		iced tea:	8

profit:		$15.00
tax:		$1.09
``` 

For more details about print precision and the `fmt` format string refer to **A.16** of the  [appendix](https://ampl.com/wp-content/uploads/Appendix-A-AMPL-Book.pdf).
:::::

### Complete program listing for APIs

When using AMPL programmatically through its APIs, it's important to consider how to best utilize them.
For optimal performance, we recommend using the APIs primarily to get and set data, and then perform any necessary data manipulation using language-native objects.
For instance, in Python, it would be beneficial to convert the data received from AMPL to a Pandas DataFrame for any data manipulation tasks.

To illustrate this, we will emulate in the API language the AMPL commands introduced earlier, which utilize `show` and `print`.
We would first retrieve the necessary data from AMPL using the API's get-data method.
This method returns the data in a data-frame that's optimized for communication between AMPL and the respective API interface.
However, this interface-specific data-frame may not be the most efficient for data manipulation.
Therefore, the next step is to transfer the data to a more suitable data-frame native to the language we are working with.

Below, we present complete program listings for each API that incorporate these concepts.

:::::{tab-set}

::::{tab-item} Python
```{literalinclude} ampl_files/sp_lemonade.py
:language: python
:linenos: true
:caption: sp_lemonade.py
```
For more information about `get_data()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
python sp_lemonade.py > sp_lemonade.py.out
```

Gives:

```{literalinclude} ampl_files/sp_lemonade.py.out
:caption: sp_lemonade.py.out
```
::::

::::{tab-item} R

:::{note}
Since the R API is built with [Rcpp](https://cran.r-project.org/web/packages/Rcpp/index.html) the `getData()` function directly returns an R `data.frame` object, eliminating the need for any conversion to a native object. 
:::

```{literalinclude} ampl_files/sp_lemonade.R
:language: r
:linenos: true
:caption: sp_lemonade.R
```

For more information about `getData()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.

Running:

```bash
Rscript sp_lemonade.R > sp_lemonade.R.out
```

Gives:

```{literalinclude} ampl_files/sp_lemonade.R.out
:caption: sp_lemonade.R.out
```

::::

::::{tab-item} MATLAB
```matlab
ampl.read('lemonade.mod')
ampl.setOption('solver', 'highs');
ampl.solve();

%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about `getData()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
::::

::::{tab-item} C++
```{literalinclude} ampl_files/sp_lemonade.cc
:language: cpp
:linenos: true
:caption: sp_lemonade.cc
```

:::{admonition} Custom header files
:class: dropdown
```{literalinclude} ampl_files/transpose.h
:language: cpp
:linenos: true
:caption: transpose.h
```

```{literalinclude} ampl_files/MyDataFrame.h
:language: cpp
:linenos: true
:caption: MyDataFrame.h
```
:::

For more information about `getData()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
./sp_lemonade > sp_lemonade.cc.out
```

Gives:

```{literalinclude} ampl_files/sp_lemonade.cc.out
:caption: sp_lemonade.cc.out
```
::::

::::{tab-item} C#
```cs
ampl.Read("lemonade.mod");
ampl.SetOption("solver", "highs");
ampl.Solve();

/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about `GetData()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
::::

::::{tab-item} Java
```java
ampl.read("lemonade.mod");
ampl.setOption("solver", "highs");
ampl.solve();

/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about `getData()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
::::
:::::

