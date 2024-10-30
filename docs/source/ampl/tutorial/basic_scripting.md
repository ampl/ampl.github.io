# Basic scripting
In this section, we will cover various aspects of working with AMPL, including command line arguments, invoking AMPL with files in command line arguments, indexing sets, and scripting through APIs or using AMPL's built-in features.

We will begin by introducing an integer program closely related to our lemonade stand example. 
Following this, we will discuss AMPL's command line arguments, and then present a few small scripts that can be used to set solvers, assign initial guesses to variables, or print solutions.
 
To help you navigate this section, here is a quick summary of the AMPL concepts that will be covered.

:::{admonition} Section summary
In this section we will learn the following:

1. **Basics of AMPL's command line arguments**, which can be recalled by executing:
	```bash
	ampl -?
	```

<br>

2. **Indexing sets** such as `{1..6}`, which allows us to declare indexed model entities as follows:

    
    ::::{tab-set}
    :::{tab-item} Interactive
    ```ampl
    ampl: param ones{1..6} := 1;  
    ampl: display ones;
    ones [*] :=
    1  1
    2  1
    3  1
    4  1
    5  1
    6  1
    ;
    ```
    or
    ```ampl
    ampl: param one2six{i in 1..6} := i;
    ampl: display one2six[1], one2six[3], one2six[6];
    one2six[1] = 1
    one2six[3] = 3
    one2six[6] = 6
    ```
    :::
    
    :::{tab-item} Python
    
    ```python
    ampl.eval("""
        param ones{1..6} := 1;
        display ones;
        """)
    ```
    or
    ```python
    ampl.eval("""
        param one2six{i in 1..6} := i;
        display one2six[1], one2six[3], one2six[6];
        """)
    ``` 
    :::
    
    :::{tab-item} R
    ```r
    ampl$eval(paste("param ones{1..6} := 1;",
                    "display ones;"))
    ```
    or
    ```r
    ampl$eval(paste("param one2six{i in 1..6} := i;",
                    "display one2six[1], one2six[2], one2six[3];"))
    ```
    :::
    
    :::{tab-item} MATLAB
    ```matlab
    ampl.eval(['param ones{i in 1..6} := 1;' newline ...
               'display ones;'])
    ```
    or
    ```matlab
    ampl.eval(['param one2six{i in 1..6} := i;' newline ...
               'display one2six[1], one2six[2], one2six[3];'])
    ```
    :::
    
    :::{tab-item} C++
    ```cpp
    ampl.eval(R"(param ones{1..6} := 1;
                 display ones;)")
    ```
    or
    ```cpp
    ampl.eval(R"(param one2six{i in 1..6} := i;
                 display one2six[1], one2six[2], one2six[3];)")
    ```
    :::
    
    :::{tab-item} C#
    ```cs
    ampl.Eval(@"param ones{i in 1..6} := 1;
                display ones;")
    ```
    or
    ```cs
    ampl.Eval(@"param one2six{i in 1..6} := i;
                display one2six[1], one2six[2], one2six[3];")
    ```
    :::
     
    :::{tab-item} Java
    ```java
    ampl.eval("param ones{i in 1..6} := 1;" +
              "display ones;")
    ```
    or
    ```java
    ampl.eval("param one2six{i in 1..6} := i;" +
              "display one2six[1], one2six[2], one2six[3];")
    ```
    :::
    ::::

<br>

3. **Generic synonyms** for entities, such as `_varname` for variable names, and `_var` for their values:

    ::::{tab-set}
    :::{tab-item} Interactive
    ```ampl
    ampl: model mulled_wine.mod; 
    ampl: display _varname, _var;
    :    _varname   _var    :=
    1   mulled_wine   0
    2   hot_tea       0
    ;
    ```
    :::
    
    :::{tab-item} Python 
    ```python
    ampl.eval("""
        model mulled_wine.mod;
        display _varname, _var;
        """)
    ```
    :::
    
    :::{tab-item} R
    ```r
    ampl$eval(paste("model mulled_wine.mod;",
                    "display _varname, _var;"))
    ```
    :::

    :::{tab-item} MATLAB
    ```matlab
    ampl.eval(['model mulled_wine.mod;' newline ...
               'display _varname, _var;'])
    ```
    :::
    
    :::{tab-item} C++
    ```cpp
    ampl.eval(R"(model mulled_wine.mod;
                 display _varname, _var;)")
    ```
    :::
    
    :::{tab-item} C#
    ```cs
    ampl.Eval(@"model mulled_wine.mod;
                display _varname, _var;")
    ```
    :::
     
    :::{tab-item} Java
    ```java
    ampl.eval("model mulled_wine.mod;" +
              "display _varname, _var;")
    ```
    :::
    ::::

<br>

4. **`for` statements** used in conjunction with generic synonyms to develop a general-purpose solution printer:

    ::::{tab-set}
    :::{tab-item} AMPL
    ```{literalinclude} ampl_files/print_solution.run
    :language: ampl
    :linenos: true
    :caption: print_solution.run
    ```
    :::
    :::{tab-item} Python
    ```{literalinclude} ampl_files/print_solution.py
    :language: python
    :linenos: true
    :caption: print_solution.py
    ```
    For more information about these methods checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
    :::
    
    :::{tab-item} R
    ```{literalinclude} ampl_files/print_solution.R
    :language: R
    :linenos: true
    :caption: print_solution.R
    ```
    For more information about these methods checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
    :::
    
    :::{tab-item} MATLAB
    ```matlab
    %%% %%%%%%%%%%% %%%
    %%% COMING SOON %%%
    %%% %%%%%%%%%%% %%%
    ```
    For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
    :::
    
    :::{tab-item} C++
    ```{literalinclude} ampl_files/print_solution.h
    :language: cpp
    :linenos: true
    :caption: print_solution.h
    ```
    
    For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
    :::
    
    :::{tab-item} C#
    ```cs
    /// /////////// ///
    /// COMING SOON ///
    /// /////////// ///
    ```
    
    For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
    :::
    
    :::{tab-item} Java
    ```java
    /// /////////// ///
    /// COMING SOON ///
    /// /////////// ///
    ```
    For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
    :::
    ::::

<br>

5. **`let` and `if-then-else` statements** used to provide warm starts:

    ::::{tab-set}
    :::{tab-item} AMPL
    ```{literalinclude} ampl_files/warm_start.run
    :language: ampl
    :linenos: true
    :caption: warm_start.run
    ```
    :::
    
    :::{tab-item} Python
    ```{literalinclude} ampl_files/warm_start.py
    :language: python
    :linenos: true
    :caption: warm_start.py
    ```
    :::
    
    :::{tab-item} R
    ```{literalinclude} ampl_files/warm_start.R
    :language: r
    :linenos: true
    :caption: warm_start.R
    ```
    :::
    
    :::{tab-item} MATLAB
    ```matlab
    %%% %%%%%%%%%%% %%%
    %%% COMING SOON %%%
    %%% %%%%%%%%%%% %%%
    ```
    :::
    
    :::{tab-item} C++
    ```{literalinclude} ampl_files/warm_start.cc
    :language: cpp
    :linenos: true
    :caption: warm_start.cc
    ```
    :::
    
    :::{tab-item} C#
    ```cs
    /// /////////// ///
    /// COMING SOON ///
    /// /////////// ///
    ```
    :::
    
    :::{tab-item} Java
    ```java
    /// /////////// ///
    /// COMING SOON ///
    /// /////////// ///
    ```
    :::
    ::::

<br>

:::



## Problem formulation
Your lemonade stand works well during the summer months, but as winter approaches, you sense the need to switch your business model. 
Thankfully, your inheritance of ingredients can be adapted from lemons to wine and spices, and you decide to open a mulled wine and hot tea stand. 
As before, your goal is to maximize your daily profit by deciding how many cups of mulled wine and hot tea to sell, subject to the constraint that you have a limited amount of wine, spices, sugar, and tea bags available to you each day.

In this example you will offer two drinks: mulled wine $(x_{\textrm{mulled_wine}})$, which requires two cups of wine, two tablespoons of spice and four tablespoons of sugar per glass, and hot tea $(x_{\textrm{hot_tea}})$, which requires one tea bag, two tablespoons of sugar, and two cups of water per glass.

Thankfully, you still have access to unlimited water, however your daily inheritance of ingredients has changed to: 12 tablespoons of spices, 8 cups of tea, 30 tablespoons of sugar, and 15 cups of wine.

Your goal will again be to maximize profit by determining how many glasses of each drink to make given your limited daily ingredients. You can sell each glass of wine for \$2.00 and each glass of  tea for \$1.50. Since you have cornered the market on drink stands in town, you can expect to sell all the drinks that you make and remember that your ingredient list is limited but costs nothing.

To formulate this as an integer programming problem, we can use the following model:



$$
\begin{equation}
\begin{array}{lcrcrl}
&\textrm{Objective:}  & \max &    2x_{\textrm{mulled_wine}} & + & 1.5x_{\textrm{hot_tea}}   & -    & 2  \\
&\textrm{Subject to:} &      &                              &   &                           &      &    \\
&                     &      &    2x_{\textrm{mulled_wine}} &   &                           & \leq & 12 \\
&                     &      &                              &   & x_{\textrm{hot_tea}}      & \leq & 8  \\
&                     &      &   4x_{\textrm{mulled_wine}}  & + & 2x_{\textrm{hot_tea}}     & \leq & 30 \\
&                     &      &   2x_{\textrm{mulled_wine}}  &   &                           & \leq & 15 \\
&                     &      &                              &   &                           &      &    \\
&                     &      &    x_{\textrm{mulled_wine}}  &   &                           & \geq & 0  \\
&                     &      &                              &   & x_{\textrm{hot_tea}}      & \geq & 0  \\
&                     &      &    x_{\textrm{mulled_wine}}  & , & x_{\textrm{hot_tea}}      & \in  & \mathbb{Z}
\end{array}
\end{equation}
$$ (lp:mulled_wine)



## Model formulation in AMPL

We can build the non-parametric model for a wine and hot tea stand in AMPL with just a few small modifications to the existing lemonade model. 

Before continuing, try to use the lemonade model as a guide to create the mulled wine example.
You will notice the overall problem remains the same; you just need to update the drink names, ingredients, profits, and corresponding recipes and constraints. 

See the full mulled-wine model below:

:::{admonition} Mulled wine model
:class: dropdown
```{literalinclude} ampl_files/mulled_wine.mod
:language: ampl
:linenos: true
:caption: mulled_wine.mod
```
Download link: [mulled_wine.mod](ampl_files/mulled_wine.mod)
:::

The model again looks very similar to the mathematical formulation in {eq}`lp:mulled_wine` and is also similar to the already familiar [lemonade.mod](ampl_files/lemonade.mod) file.
 

## Solving our second model
We will proceed in a similar manner to how we solved the lemonade model.
In other words, we will load our model into AMPL, set a solver, solve, and print the solution.
However, this time we will invoke the AMPL interpreter in scripting mode, as opposed to interactive mode. 

### Invoking the `ampl` interpreter
Instead of just typing `ampl` by itself into the terminal/command prompt, we will also specify one or more file names containing AMPL commands.
When doing so, AMPL will sequentially execute the commands found in those files. 
It will quit once it has reached the end of input, barring early termination due to fatal errors, or if specifically instructed to expect input from the standard input.

#### AMPL's command line arguments
AMPL accepts files as command line arguments along with a variety of options.
The filename -- (a literal minus sign) is interpreted as the standard input of the AMPL process, which is useful for providing input interactively after a file has been specified.

For example, we could load the `mulled_wine.mod` file and then interactively set the solver to [CBC](https://dev.ampl.com/solvers/cbc/index.html) and execute the `solve` command:

::::{tab-set}
:::{tab-item} Interactive
```ampl
$ ampl mulled_wine.mod -
ampl: option solver cbc;
ampl: solve;
cbc 2.10.7: optimal solution; objective 16.5
0 simplex iterations
```
:::
::::

##### Command line arguments
Depending on the operating system on which AMPL is run, the invocation may include one or more command-line arguments to set various properties, options, and specify input files. 
To examine these command-line arguments, type the command `ampl -?`:

```
$ ampl -?
Usage: ampl [options] [file [file...]]
No file arguments means read from standard input, as does - by itself.
Options:
	-Cn {0 = suppress Cautions; 1 = default; 2 = treat as error;}*
	-Ln {0 = treat linear definitional constrs and var = decls as nonlin}*
	-P {skip presolve -- same as "option presolve 0;" }
	-S {substitute out definitional constraints (var = expression)}*
	-T {show genmod times for each item}*
	-enn {exit (if nn > 0) or abort command at |nn|-th error; 0 = no exit}*
	-g {run in a separate process group}
	-ix {import functions from x; specify -i? for details }
	-ooutopt {specify -o? for details}*
	-s[seed] {seed for random numbers; -s means current time}*
	-t {show times}*
	-v {show version and license details; -v? shows other -v options}
	--version {show version and exit, ignoring license files}
	-xnn {allow nn wall-clock seconds of execution time}
	-?? {show debug and obscure options}
* Equivalent option settings:
	-Cn	option Cautions n;		-Ln	option linelim n;
	-P	option presolve 0;		-S	option substout 1;
	-T	option gentimes 1;		-enn	option eexit nn;
	-ofstub	option outopt fstub;		-s	option randseed '';
	-snn	option randseed nn;		-t	option times 1;
```

It is beyond the scope of this material to explain these command line options in detail. 
For now, we will focus on the fact that some command line options can be used to initialize AMPL options, which we will illustrate via an example.

If invoked with the `-T` command line option (which is equivalent to the AMPL option `gentimes`) AMPL prints a detailed summary of the resources that AMPL's genmod phase consumes in generating a model instance. 
After invoking AMPL with `-T mulled_wine.mod -` command line options when the `ampl:` prompt appears we set the solver option to CBC and then execute the `solve` command:

::::{tab-set}
:::{tab-item} Interactive
```ampl
$ ampl -T mulled_wine.mod -
ampl: option solver cbc;
### option ...
ampl: solve;
### solve ...
##genmod times:
##seq      seconds    cum. sec.    mem. inc.  name
## 89        2e-06        2e-06            0  derstage
## 93        5e-06        7e-06            0  sstatus
## 107        5e-06      1.2e-05            0  mulled_wine
## 109        2e-06      1.4e-05            0  hot_tea
## 111        3e-06      1.7e-05            0  fee
## 112      3.6e-05      5.3e-05        38400  profit
## 114        6e-06      5.9e-05            0  spice_constraint
## 116        2e-06      6.1e-05            0  tea_bag_constraint
## 118        5e-06      6.6e-05            0  sugar_constraint
## 120        4e-06        7e-05            0  wine_constraint
cbc 2.10.7: optimal solution; objective 16.5
0 simplex iterations
```
:::
::::

At a minimum the timing will differ depending on the machine/operating system used.
With a tiny model such as our `mulled_wine.mod` these times do not tell us much, but at a later stage we will explore various use cases for this information.
Currently, the primary goal of this example is to demonstrate the application of command-line options when launching AMPL.

#### Setting `gentimes` via APIs
If you're using [AMPL's APIs](https://ampl.com/products/ampl/apis/) and wish to solve the mulled wine problem with option `gentimes` enabled you can do it as follows:

::::{tab-set}
:::{tab-item} Python
```python
ampl.read("mulled_wine.mod")
ampl.set_option("gentimes",  1)
ampl.set_option("solver", "cbc")
ampl.solve()
```
For more information about `read()`, `set_option()`, and `solve()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} R
```r
ampl$read("mulled_wine.mod")
ampl$setOption("gentimes", 1)
ampl$setOption("solver", "cbc")
ampl$solve()
```
For more information about `read()`, `setOption()` and `solve()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
:::

:::{tab-item} MATLAB
```matlab
ampl.read('mulled_wine.mod')
ampl.setIntOption('gentimes', 1)
ampl.setOption('solver', 'cbc');
ampl.solve();
```
For more information about `read()`, `setIntOption()`, `setOption()`, and `solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```cpp
ampl.read("mulled_wine.mod");
ampl.setIntOption("gentimes", 1)
ampl.setOption("solver", "cbc");
ampl.solve();
```
For more information about `read()`, `setIntOption()`, `setOption()`, and `solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} C#
```cs
ampl.Read("mulled_wine.mod");
ampl.SetOption("gentimes", 1)
ampl.SetOption("solver", "cbc");
ampl.Solve();
```
For more information about `Read()`, `SetOption()` and `Solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
ampl.read("mulled_wine.mod");
ampl.setIntOption("gentimes", 1)
ampl.setOption("solver", "cbc");
ampl.solve();
```
For more information about `read()`, `setIntOption()`, `setOption()` and `solve()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::


## Scripting with APIs and AMPL
For scripting, we generally recommend using of one of our many [APIs](https://ampl.com/products/ampl/apis/), which provide the flexibility of a general-purpose programming language, such as our [Python](https://amplpy.readthedocs.io/en/latest/), [C++](https://ampl.com/api/latest/cpp/) or [Java](https://ampl.com/api/latest/java/) API.
However, in some cases, it might be appropriate to write small scripts in AMPL.
AMPL offers looping and `if-then-else` constructs that enable the execution of various commands repeatedly and the manipulation of control flow.
In this tutorial, we will cover the basics, such as `for` loops and `if-then-else` statements.
For a detailed discussion of scripting in AMPL, checkout [Ch. 13](https://ampl.com/wp-content/uploads/Chapter-13-Command-Scripts-AMPL-Book.pdf) of the AMPL book.

% FOUR SCRIPTS
In this section, we will create three scripts for the mulled wine problem. 
The first two will be relatively simple, setting the solver option and then calling the `solve` command, which we have seen before. 
The third script will introduce generic AMPL names and a `for` loop.
Before we can introduce those concepts, however, we will have to begin by briefly touching upon the concept of sets in AMPL. 

(simple-sets-and-indexing)=
### Simple sets and indexing
Sets are fundamental components of AMPL models.
In the small lemonade model from the previous section, we managed without them.
However, in a typical AMPL model, almost all of the parameters, variables, and constraints are indexed over sets, and many expressions contain operations (usually summations) over sets. 
Set indexing is the feature that permits a concise model to describe a large mathematical program.

In the [general production model](#a-general-production-model) section, we will talk about [sets](#sets) and indexing in more detail.
For this section, all we need to understand is how sets are used for indexing purposes. 

Within in model mode, we can define an indexing set (a set used to index over components of an entity) by appending the set declaration after the entity's name.  
For example, we can declare a parameter, which essentially is an array of six ones as follows: 

```ampl
param ones{1..6} := 1;
```

We can think of the indexing set `{1..6}` as the set of integers between 1 and 6 i.e. `{1, 2, 3, 4, 5, 6}`. 
A more general arrangement would be to define parameters for the beginning and the end of our desired indexing interval as follows:

```ampl
param begin = 1;
param end = 6;
param ones{begin..end} := 1;
param twos{begin..end} := 2;
```

Assigning values based on the position of an entity's component can be accomplished as follows:

```ampl
param one2six{i in 1..6} := i;
```

Here the dummy variable `i` will iterate over all the members of the set `{1..6}` and get assigned to the i<sup>th</sup> component of the array. 
Elements of `one2six` can be accessed via brackets. 
In our example, `one2six[1]` would refer to the first, `one2six[2]` to the second element of the array, and so on:

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: param one2six{i in 1..6} := i;
ampl: print one2six[1], one2six[2], one2six[3];
1 2 3
```
:::

:::{tab-item} Python

```python
ampl.eval("""
    param one2six{i in 1..6} := i;
    print one2six[1], one2six[2], one2six[3];
    """)
```
For more information about `eval()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} R
```r
ampl$eval(paste("param one2six{i in 1..6} := i;",
                "print one2six[1], one2six[2], one2six[3];"))
```
For more information about `eval()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
:::

:::{tab-item} MATLAB
```matlab
ampl.eval(['param one2six{i in 1..6} := i;' newline ...
           'print one2six[1], one2six[2], one2six[3];'])
```
For more information about `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```cpp
ampl.eval(R"(param one2six{i in 1..6} := i;
             print one2six[1], one2six[2], one2six[3];)")
```
For more information about `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} C#
```cs
ampl.Eval(@"param one2six{i in 1..6} := i;
            print one2six[1], one2six[2], one2six[3];")
```
For more information about `Eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
ampl.eval("param one2six{i in 1..6} := i;" +
          "print one2six[1], one2six[2], one2six[3];")
```
For more information about `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::

In the following section, we will review the scripts responsible for setting solver options.
Afterward, we will discuss how to use indexing sets and AMPL's builtin parameters for writing a general-purpose solution printer.

### Setting option solver
The two scripts introduced below are essentially identical, apart from the solver option they set. 
The first one sets CBC, while the second one sets HiGHS.

In the AMPL tab, we will introduce stand alone scripts (`.run` files) for setting CBC and HiGHS. 

```{note}
AMPL does not care about the file extensions, but it is customary to use `.run` for AMPL scripts.
```

::::{tab-set}
:::{tab-item} AMPL
```{literalinclude} ampl_files/cbc_solve.run
:language: ampl
:linenos: true
:caption: cbc_solve.run
```

```{literalinclude} ampl_files/highs_solve.run
:language: ampl
:linenos: true
:caption: highs_solve.run
```
:::
::::

#### Using APIs
In the examples below, we'll utilize the capabilities of the underlying programming language to implement a single, generic function through the API.
This function will achieve the same effect as the AMPL scripts introduced above.
As we'll see, in such situations, it's often more practical to rely on the AMPL APIs as opposed to scripting in AMPL.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/set_n_solve.py
:language: python
:linenos: true
:caption: set_n_solve.py
```

For more information about these methods checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} R
```{literalinclude} ampl_files/set_n_solve.R
:language: R
:linenos: true
:caption: set_n_solve.R
```

For more information about these methods checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
:::

:::{tab-item} MATLAB
```matlab
%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```{literalinclude} ampl_files/set_n_solve.h
:language: cpp
:linenos: true
:caption: set_n_solve.h
```

For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} C#
```cs
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```

For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::

### General-purpose solution printer script
In order to build a general-purpose solution printer script we will require two new concepts:
1. AMPL's generic synonyms for variables, constraints and objectives.
2. The `for` looping statement.

#### Generic synonyms for variables, constraints and objectives
AMPL provides automatically updated parameters that hold the numbers of variables, constraints, and objectives in the current problem instance:
```ampl
_nvars     # number of variables in the current problem
_ncons     # number of constraints in the current problem
_nobjs     # number of objectives in the current problem
```
Correspondingly indexed parameters contain the AMPL names of all the components:
```ampl
_varname{1.._nvars}     # names of variables in the current problem
_conname{1.._ncons}     # names of constraints in the current problem
_objname{1.._nobjs}     # names of objectives in the current problem
```
Finally, the following synonyms for the components are made available:
```ampl
_var{1.._nvars}     # synonyms for variables in the current problem
_con{1.._ncons}     # synonyms for constraints in the current problem
_obj{1.._nobjs}     # synonyms for objectives in the current problem
```
These synonyms let you refer to components by number.
Using the variables as an example, `_var[5]` refers to the fifth variable in the problem.

For more information about generic synonyms refer to [Ch. 12](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf) section 12.6 and table A-13 in section A.20 of the [appendix](https://ampl.com/wp-content/uploads/Appendix-A-AMPL-Book.pdf) of the AMPL book.

#### Iterating over a set: the `for` statement
As we mentioned earlier, while complex scripting is best suited for one of the many AMPL [APIs](https://ampl.com/products/ampl/apis/), such as [Python](https://amplpy.readthedocs.io/en/latest/), [C++](https://ampl.com/api/latest/cpp/) or [Java](https://ampl.com/api/latest/java/), there are situations where small scripts can be effectively written using AMPL. 

The `for` statement executes a statement or collection of statements once for each member of a specified set. 
As a simple example to introduce the concept of a for loop, we can use a `for` statement followed by an indexing expression and a `print` command. 

::::{tab-set}
:::{tab-item} Interactive
```ampl
ampl: param begin = 1;
ampl: param end = 6;
ampl: param ones{begin..end} := 1;
ampl: for {i in begin..end} print ones[i];
1
1
1
1
1
1
```
:::
::::

The example above generates a set containing every integer from the interval $[\verb!begin!, \verb!end!]$, which is then used to index the parameter `ones`. 
The `:=` operator assigns 1 to each element of `ones`.
The `for` loop then iterates through every integer in the interval $[\verb!begin!, \verb!end!]$, executing the `print` statement for each value of `ones`.

##### Using APIs
In the API examples below, we present API-language for-loops that achieve the same effect as the AMPL for-loop introduced above.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/for_print.py
:language: python
:linenos: true
:caption: for_print.py
```
For more information about `eval()` and `get_data()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ python for_print.py > for_print.py.out
```

Gives:

```{literalinclude} ampl_files/for_print.py.out
:caption: for_print.py.out
```
:::

:::{tab-item} R
```{literalinclude} ampl_files/for_print.R
:language: r
:linenos: true
:caption: for_print.R
```
For more information about `eval()` and `getData()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.

Running:

```bash
$ Rscript for_print.R > for_print.R.out
```

Gives:

```{literalinclude} ampl_files/for_print.R.out
:caption: for_print.R.out
```
:::

:::{tab-item} MATLAB
```matlab
ampl.eval(['param begin = 1;' newline ...
           'param end = 6;' newline ...
           'param ones{begin..end} := 1;'])

%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about `eval()` and `getData()`checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```{literalinclude} ampl_files/for_print.cc
:language: cpp
:linenos: true
:caption: for_print.cc
```

For more information about `eval()` and `getData()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ ./for_print > for_print.cc.out
```

Gives:

```{literalinclude} ampl_files/for_print.cc.out
:caption: for_print.cc.out
```
:::

:::{tab-item} C#
```cs
ampl.Eval(@"param begin = 1;
            param end = 6;               
            param ones{begin..end} := 1;")

/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```

For more information about `Eval()` and `GetData()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
ampl.eval("param begin = 1;" +
          "param end = 6;" +
          "param ones{begin..end} := 1;")

/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about `eval()` and `getData()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::
  
#### General-purpose solution printer
Combining generic synonyms with the `for` statement allows us to design the general-purpose solution printer script.
First we create a set of numbers ranging from 1 to the total number of variables in the model i.e. `1 .. _nvars`.
Then we will loop through every element of that set and use it to retrieve each value of the indexed parameters `_varname` and `_var` to print out the name and value of each variable.

In the AMPL tab, we will introduce a stand alone script (`.run` file) that can print solutions independent of the underlying model, thanks to the use of generic synonyms. 

::::{tab-set}
:::{tab-item} AMPL
```{literalinclude} ampl_files/print_solution.run
:language: ampl
:linenos: true
:caption: print_solution.run
```
:::
::::

`$solver` gives us the value of the option solver, so we can use it to recall, which solver was used to obtain the solution. 
For purposes of clarity we use braces for the body of the `for` statement.
Braces can also be used to execute a collection of commands per iteration. 
Finally, since we only have one objective we don't require a loop and can simply retrieve the objective by printing the first elements of `_objname` and `_obj`.
For more information about scripts and control flow in AMPL refer to [Ch. 13](https://ampl.com/wp-content/uploads/Chapter-13-Command-Scripts-AMPL-Book.pdf) and section A.20 of the [appendix](https://ampl.com/wp-content/uploads/Appendix-A-AMPL-Book.pdf) of the AMPL book.

##### Using APIs
Similarly, in the API examples, we will present functions that, when given an AMPL object, can print the solution regardless of the underlying model.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/print_solution.py
:language: python
:linenos: true
:caption: print_solution.py
```
For more information about these methods checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} R
```{literalinclude} ampl_files/print_solution.R
:language: R
:linenos: true
:caption: print_solution.R
```
For more information about these methods checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.
:::

:::{tab-item} MATLAB
```matlab
%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```{literalinclude} ampl_files/print_solution.h
:language: cpp
:linenos: true
:caption: print_solution.h
```

For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} C#
```cs
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```

For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::

### Combining scripts to obtain solutions
By utilizing our previously introduced solve scripts ([cbc_solve.run](ampl_files/cbc_solve.run) and [highes_solve.run](ampl_files/highs_solve.run)) and the generic solution printer script ([print_solution.run](ampl_files/print_solution.run)) we can construct a comprehensive AMPL script.
This script will allow us to generate solutions for both the mulled wine and the lemonade model using CBC and HiGHS:

::::{tab-set}
:::{tab-item} AMPL
```{literalinclude} ampl_files/multi_solve.run
:language: ampl
:linenos: true
:caption: multi_solve.run
```
Running:

```bash
$ ampl multi_solve.run > multi_solve.run.out
```

Gives:

```{literalinclude} ampl_files/multi_solve.run.out
:caption: multi_solve.run.out
```
:::
::::

#### Using APIs
Our APIs provide a more practical way of reproducing [multi_solve.run](ampl_files/multi_solve.run).
We will demonstrate how to combine our functions from earlier to achieve the same result as above.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/multi_solve.py
:language: python
:linenos: true
:caption: multi_solve.py
```
For more information about `read()` and `reset()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ python multi_solve.py > multi_solve.py.out
```

Gives:

```{literalinclude} ampl_files/multi_solve.py.out
:caption: multi_solve.py.out
```
:::

:::{tab-item} R
```{literalinclude} ampl_files/multi_solve.R
:language: r
:linenos: true
:caption: multi_solve.R
```
For more information about `read()` and `reset()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.

Running:

```bash
$ Rscript multi_solve.R > multi_solve.R.out
```

Gives:

```{literalinclude} ampl_files/multi_solve.R.out
:caption: multi_solve.R.out
```
:::

:::{tab-item} MATLAB
```matlab
%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about `read()` and `reset()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```{literalinclude} ampl_files/multi_solve.cc
:language: cpp
:linenos: true
:caption: multi_solve.cc
```

For more information about `read()` and `reset()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ ./multi_solve > multi_solve.cc.out
```

Gives:

```{literalinclude} ampl_files/multi_solve.cc.out
:caption: multi_solve.cc.out
```
:::

:::{tab-item} C#
```cs
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```

For more information about `Read()` and `Reset()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about `read()` and `reset()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::

### Exploring `let` and `if-then-else` statements through warm starts
We will conduct a simple experiment to demonstrate the use of AMPL's `option relax_integrality`, as well as the `let` and `if` statements.

Our experiment comprises two steps.
First, we will solve our integer programming problem as a linear program by enabling the `relax_integrality` option. 
Second, we aim to enhance the solver's speed (iteration count) by assigning the rounded values of the LP solution to our variables.

Realistically, however, this will not improve the solver's performance due to a couple of factors. 
First, the rounding maybe performed in such a way that it results in a bad initial guess.
Second, given the simplicity of the problem, solvers may find the solution during the presolve phase itself. 
Third, solvers might choose to disregard the initial values.
In light of these factors, it is always good practice to familiarize ourselves with the documentation of the solver we decide to use, as the settings can influence the solver's performance. 
Solver-related documentation can be found on our [solvers page](https://dev.ampl.com/solvers/).

Despite these limitations, the experiment serves as a valuable opportunity to explore the use of `let` and `if` statements and expand our understanding of scripting with AMPL and the APIs.

#### `let` and `if-then-else` statements
First, we will solve our [mulled_wine.mod](ampl_files/mulled_wine.mod) as a linear program by relaxing integrality before executing the `solve` command.
We will then use the `if` statement within a `for` loop to filter out variables that do not have integer values, utilizing AMPL's built-in `round(x)` function, which rounds `x` to the nearest integer.  
Next, we'll employ AMPL's `let` command to update variables with non-integer values to their rounded equivalents.
Finally, after disabling the `relax_integrality` option, we'll solve our problem once again.
AMPL will take care of passing the updated values to the solver.

::::{tab-set}
:::{tab-item} AMPL
```{literalinclude} ampl_files/warm_start.run
:language: ampl
:linenos: true
:caption: warm_start.run
```
Running:

```bash
$ ampl warm_start.run > warm_start.run.out
```

Gives:

```{literalinclude} ampl_files/warm_start.run.out
:caption: warm_start.run.out
```
:::
::::


:::::{admonition} Advanced: `let` command
:class: dropdown

The command:

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">let</span> <i>indexing<sub>opt</sub> name := expr </i>;
</code>
</pre>

changes the value of the possibly indexed set, parameter or variable <code><i>name</i></code> to the value of the
expression. 
If <code><i>name</i></code> is a set or parameter, its declaration must not specify a `=` phrase.

Technically, we could have condensed the `for` loop with a single line as demonstrated below: 
```{literalinclude} ampl_files/warm_start_advanced.run
:language: ampl
:lines: 14-15
:emphasize-lines: 2-3
:caption: warm_start_advanced.run
```
In this case, we define an indexing set for the `let` command with a special filter.
We will explore conditional filters in more detail [later](modeling_and_data.md).

For more information about the `let` command visit [Ch. 11](https://ampl.com/wp-content/uploads/Chapter-11-Modeling-Commands-AMPL-Book.pdf) section 11.3 of the AMPL book.
:::::

:::::{admonition} Advanced: `if-then-else` statement
:class: dropdown

Statements such as:

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">if</span> <i>lexpr</i> <span style="color: darkgreen; font-weight: bold">then</span> <i>cmd<sub>true</sub> </i>
    <span style="color: darkgreen; font-weight: bold">if</span> <i>lexpr</i> <span style="color: darkgreen; font-weight: bold">then</span> <i>cmd<sub>true</sub></i> <span style="color: darkgreen; font-weight: bold">else</span> <i>cmd<sub>false</sub> </i>
</code>
</pre>

permit conditional execution of AMPL commands.
In these statements, <i>cmd</i> is either a single, possibly empty, command that ends with a semicolon or a sequence of zero or more commands enclosed in braces. 
<i>lexpr</i> is a logical expression.

For more information about `if-then-else` statements in AMPL refer to [Ch. 13](https://ampl.com/wp-content/uploads/Chapter-13-Command-Scripts-AMPL-Book.pdf) section 13.4 of the AMPL book.
:::::

#### Using APIs
In the API examples below, we present API-language for-loops that achieve the same effect as the AMPL for-loop introduced above.
We will also rely on functions such as `set_n_solve()` or `print_solution()` introduced earlier.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/warm_start.py
:language: python
:linenos: true
:caption: warm_start.py
```
For more information about these methods checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ python warm_start.py > warm_start.py.out
```

Gives:

```{literalinclude} ampl_files/warm_start.py.out
:caption: warm_start.py.out
```
:::

:::{tab-item} R
```{literalinclude} ampl_files/warm_start.R
:language: r
:linenos: true
:caption: warm_start.R
```
For more information about these methods checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.

Running:

```bash
$ Rscript warm_start.R > warm_start.R.out
```

Gives:

```{literalinclude} ampl_files/warm_start.R.out
:caption: warm_start.R.out
```
:::

:::{tab-item} MATLAB
```matlab
%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```{literalinclude} ampl_files/warm_start.cc
:language: cpp
:linenos: true
:caption: warm_start.cc
```

For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ ./warm_start > warm_start.cc.out
```

Gives:

```{literalinclude} ampl_files/warm_start.cc.out
:caption: warm_start.cc.out
```
:::

:::{tab-item} C#
```cs
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```

For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about these methods checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::
