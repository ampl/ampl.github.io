(modeling-and-data)=
# Modeling and data
In the upcoming sections, we will build upon our previous examples to formulate a generic production problem that encompasses both the lemonade and mulled wine scenarios.
We'll delve deeper into the usage of sets in AMPL, explore the creation and use of data files, and further investigate AMPL's data mode and its interplay with APIs.

:::{admonition} Section summary
In this section we will learn the following:

1. **Declaring sets**:
    ```{literalinclude} ampl_files/production.mod
    :lines: 1-3
    :emphasize-lines: 2-3
    :language: ampl
    ```
    
<br>

2. **Specifying data for sets with filters**:
    ```ampl
    ampl: set ODDS := {i in 1..10: i mod 2};
    ampl: display ODDS;
    set ODDS := 1 3 5 7 9;
    ```

<br>

3. **Writing parametric models:**
    ```{literalinclude} ampl_files/production.mod
    :language: ampl
    :linenos: true
    :caption: production.mod
    ```

<br>

4. **Writing `.dat` files:**
    ```{literalinclude} ampl_files/lemonade.dat
    :language: ampl
    :linenos: true
    :caption: lemonade.dat
    ```

<br>

5.  **Setting data from native objects** such as Pandas DataFrames:
    ::::{tab-set}
    :::{tab-item} Python
    ```{literalinclude} ampl_files/set_data_nc.py
    :language: python
    :linenos: true
    :caption: set_data_nc.py
    ```
    :::
    
    :::{tab-item} R
    ```{literalinclude} ampl_files/set_data_nc.R
    :language: R
    :linenos: true
    :caption: set_data_nc.R
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
    ```{literalinclude} ampl_files/set_data_nc.h
    :language: cpp
    :linenos: true
    :caption: set_data_nc.h
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

As demonstrated by the lemonade and mulled wine example, the current approach of hard-coding problem coefficients in our model files necessitates modifications to the model itself each time our problem coefficients change. 
However, AMPL provides a rich set of features that allow for a convenient separation between our optimization model and its data, such as the problem instance's coefficients. 
In AMPL, all model coefficients, such as resource constraints, recipes or profits can be declared as parameters.
Values to these parameters can be supplied to AMPL in a separate data file, which AMPL can read when in data mode. 
AMPL's data mode is optimized for fast ingestion of large data files.

Moving forward, we will refer to models where all problem coefficients are expressed as parameters as parametric models.
The models we have seen so far were non-parametric because not all coefficients of our optimization model were expressed as parameters.

**Parametric models offer a more streamlined optimization workflow** as they enable us to develop general abstract models applicable to all problems belonging to the same class, independent of the problem instances coefficients.


## Problem formulation
You may have noticed that the two models we discussed for the lemonade and mulled wine stands are quite similar. 
In reality, the core optimization problem we solved in each case is the same, only with different data.

We express our generic production model as the following integer programming problem:

$$
\begin{alignat*}{3}
    & \textrm{Maximize: }   &       & \sum_{j \in P} c_{j} x_{j} - C                    & \\
    & \textrm{Subject To: } & \quad & \sum_{{j \in P}} a_{ij} x_j \leq b_i,             & \forall i \in I \\
    &                       & \quad & \quad \quad \quad  x_{j} \in \mathbb{Z},          &\quad \forall j \in P
\end{alignat*}
$$ (ip:production)

Where $P$ is the set of products, $I$ is the set of ingredients, $c_j$ is the profit per unit of product $j$, $x_j$ is the units of product $j$ made, C is a fixed cost, $a_{ij}$ is the usage of ingredient $i$ by unit of product $j$, and $b_i$ is the limit of ingredient $i$.

**Fortunately, AMPL allows us to express the production problem introduced above with the same level of abstraction**.


## Model formulation in AMPL

To formulate our generic production model introduced in {eq}`ip:production` in AMPL, we have to revisit [sets](#sets), a fundamental component of AMPL that we briefly touched upon {ref}`previously <simple-sets-and-indexing>`.

In the next section, we will focus on sets before moving on to formulating the parametric model in AMPL and introducing the associated model file. 
Once we have established the abstract model, we will talk about data files, which enable us to convert the abstract model into a specific problem instance.

### Sets
As mentioned earlier, in a typical AMPL model, almost all of the parameters, variables, and constraints are indexed over sets, and many expressions contain operations (usually summations) over sets.
Sets are fundamental in AMPL, and the language offers a wide variety of set types and operations.
To provide a comprehensive understanding of sets, the AMPL book dedicates two full chapters, [Ch. 5](https://ampl.com/wp-content/uploads/Chapter-5-Simple-Sets-and-Indexing-AMPL-Book.pdf) and [Ch. 6](https://ampl.com/wp-content/uploads/Chapter-6-Compound-Sets-and-Indexing-AMPL-Book.pdf) on this topic, as well as sections A.2, A.3, A.4, and A.6 of the [appendix](https://ampl.com/wp-content/uploads/Appendix-A-AMPL-Book.pdf).
For a detailed discussion of sets, we refer you to the book.

For our production model we will declare two sets: one for our products and one for their ingredients.
Set declarations in AMPL start with the `set` keyword, followed by a set name and a semicolon.

```{literalinclude} ampl_files/production.mod
:lines: 1-3
:emphasize-lines: 2-3
:language: ampl
```

We will use these sets in our model to index our model parameters, variables, and constraints. 
`PROD` will contain product identifiers such as `lemonade` or `ice_tea`, essentially our non-parametric variable names.
`INGR` will contain names of our ingredients such as `sugar`, `tea_bag` etc.

It's important to note that at this point, we have not assigned any set members to the sets introduced above.
Since we want to keep this model completely parametric, we will assign set members in the data file.
However, AMPL does allow for set member assignment in the model file if desired, but doing so would not maintain the model's abstract nature.

:::{admonition} Advanced: General Set Syntax
:class: dropdown

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">set</span> <i>name alias<sub>opt</sub> indexing<sub>opt</sub> attributes<sub>opt</sub> </i>;

    <i>attributes: </i>
        <span style="color: darkgreen; font-weight: bold">dimen</span> <i>n</i> 
        <span style="color: darkgreen; font-weight: bold">within</span> <i>sexpr</i>
        = <i>sexpr</i>
        <span style="color: darkgreen; font-weight: bold">default</span> <i>sexpr</i>
</code>
</pre>

As noted earlier in this tutorial, here *sexpr* stands for set expression:

A set's members may be strings or numbers, ordered or unordered; they may occur singly, or as ordered pairs, triples or longer "tuples". 
Sets may be defined by listing or computing their members explicitly, by applying operations like union and intersection to other sets, or by specifying arbitrary arithmetic or logical conditions for membership.

For example, to generate a set whose members are odd numbers between 1 and 10 we can do the following in AMPL:

```ampl
ampl: set ODDS := {i in 1..10: i mod 2};
ampl: display ODDS;
set ODDS := 1 3 5 7 9;
```

The sequence `1..10` generates a dummy set whose members are: `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}`.
Then, for all elements of the set `{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}` AMPL performs the modulo operation specified after the colon.
Non-zero return values evaluate to true, and hence odd numbers are included in the set, while the rest are discarded.

Returning to our lemonade and mulled wine examples, if we create a set containing all our products: `{'lemonade', 'iced_tea', 'mulled_wine', 'hot_tea'}` and then would like to create another set with all the tea-based products, this can be achieved as follows in AMPL:

```ampl
ampl: set PROD := {'lemonade', 'iced_tea', 'mulled_wine', 'hot_tea'};
ampl: set TEAS := {j in PROD: match(j, '[Tt][Ee][Aa]')}; 
ampl: display TEAS;
set TEAS := iced_tea hot_tea;
```

For every product, we check the string against the regular expression `[Tt][Ee][Aa]`.
If we find a match, then that string will be included in the `TEAS` set.
In the example above, we have used one of AMPL's built-in regular expression function to perform the check.
For more details regarding built-in string and regular expression functions, refer to [Ch. 13](https://ampl.com/wp-content/uploads/Chapter-13-Command-Scripts-AMPL-Book.pdf) and section A.4.2 of the [appendix](https://ampl.com/wp-content/uploads/Appendix-A-AMPL-Book.pdf) of the AMPL book.

:::


In general, any model component such as parameters or variables, as well as iterated operations like `for` or `let` statements, can be indexed over any set using a standard form of indexing expression.
Additionally, sets themselves may be declared in collections indexed over other sets.
The following sections will cover the indexed model entities necessary for our abstract production model.

### Indexed variable declarations
We begin by declaring our $x_j$ variables. 
However, in AMPL we can use a descriptive name for them such as `make`.

To declare `make` in AMPL, we start with the `var` keyword, followed by the variable name, the **indexing set** enclosed in curly braces, integrality and nonnegativity attributes, and a semicolon.
```{literalinclude} ampl_files/production.mod
:lines: 5-6
:emphasize-lines: 2
:language: ampl
```
`make` is indexed over the set `PROD`, which as mentioned earlier will contain all product identifiers for our production model. 

### Indexed parameter declarations
We will declare all of the production model coefficients from {eq}`ip:production` as parameters.

Our fixed cost $C$ will be called `fee` and is not indexed, the only difference here to our earlier model files is that we don't assign any value to fee in the model file.

The objective function coefficients $c_j$ indicating the profits per product will be represented by the parameter `profit_per_product` indexed over all products.

The right hand side of our constraints $b_i$ will be named `limit` and indexed over all ingredients, as these are our resources limits.

Finally, our constraint coefficients $a_{ij}$ are expressed as the `usage` parameter indexed over both the ingredients and the products, this matrix essentially encodes our recipes.

In the case of parameters, just like with the variable declarations, the **indexing set** follows the name surrounded by curly braces ending with a semicolon:

```{literalinclude} ampl_files/production.mod
:lines: 8-12
:emphasize-lines: 2-5
:language: ampl
```
Our parameters are indexed over the sets `PROD` and `INGR` which, as mentioned earlier, will contain all product and ingredient identifiers for our specific problem instance. 

### Objective declaration
While we only have one objective function in {eq}`ip:production`, the function body: $\sum_{j \in P} c_{j} x_{j} - C$ contains an indexed summation.
AMPL generalizes indexed operators, such as $\sum$, by expressions for iterating operations over sets. 

Our objective declaration is similar to what we have seen before, first specifying the direction of optimization, followed by a name, a colon, an expression, and a semicolon:

```{literalinclude} ampl_files/production.mod
:lines: 14-16
:emphasize-lines: 2-3
:language: ampl
```

The keyword `sum` may be followed by any indexing expression. 
The subsequent arithmetic expression is evaluated once for each member of the index set (in our case `PROD`), and all the resulting values are added. 

Thus, the sum above represents the total profit made when selling our products.

Before moving on to constraints, we mention that AMPL allows you to concisely declare multiple objective functions by indexing them.
Since our production model only has one objective function, there is no need for that feature in this model.

### Indexed constraint declarations
In {eq}`ip:production` we have a constraint for each ingredient: $\sum_{j \in P} a_{ij} x_{j} \leq b_i,\; \forall i \in I$.
Instead of listing each of them individually, as we have done in the past, we can concisely express all our constraint in essentially one line, since our `limit` and `usage` parameters are indexed by ingredients. 

To declare ingredient constraints in AMPL, we first use the keywords `subject to`, followed by a name, the **indexing set**, a colon, a constraint expression, and a semicolon:

```{literalinclude} ampl_files/production.mod
:lines: 18-20
:emphasize-lines: 2-3
:language: ampl
```

The constraint expression following the colon is enforced once for each member of the index set (in our case `INGR`). 

### The complete parametric model
Below we introduce the general production model in its parametric form in AMPL in its entirety. 
As you can see it looks very similar to the mathematical formulation in {eq}`ip:production`. 

```{literalinclude} ampl_files/production.mod
:language: ampl
:linenos: true
:caption: production.mod
```

Download link: [production.mod](https://github.com/gomfy/ampl_tutorial/blob/main/src/source/ampl_files/production.mod)


## Solving instances of our production model
If we try to solve `production.mod` by itself, understandably, AMPL will complain that it is missing data for various declared entities such as sets and parameters:

```ampl
ampl: model production.mod
ampl: option solver highs;
ampl: solve;
Error executing "solve" command:
error processing var make[...]:
	no data for set PROD
```

As expected, we can supply AMPL with the necessary data via AMPL data files, the [APIs](https://ampl.com/products/ampl/apis/) or [data connectors](https://ampl.com/products/ampl/data-connectors/).


(specifying-data)=
### Specifying data via `.dat` files
We have mentioned [earlier](#ampl-modes) that AMPL has a **data** mode.
AMPL reads its data statements in data mode that is initiated by the `data` command. 
In its most common use, this command consists of the keyword `data` followed by the name of a file:
<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">data</span> <i>filename </i>
</code>
</pre>

Similarly as with `model`, the above is a shorthand for: 

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">data</span> ; <span style="color: darkgreen; font-weight: bold">include</span> <i>filename </i>
</code>
</pre>

Once in data mode, AMPL interprets input differently then in model mode.
Lexical rules of AMPL in data mode are designed to enable intuitive data entry.
For example, AMPL treats all white space as a single space and ignores commas. 
This helps us to arrange data into easy-to-read lists and tables when applicable. 

In the next sections we will introduce data files (`.dat` files) by writing two of them, one for the lemonade problem and one for the mulled wine problem, in such a way that they will both work with our generic production model.
These data files will suffice to introduce lists of one and two-dimensional sets and parameters.
However, Chapters [9](https://ampl.com/wp-content/uploads/Chapter-9-Specifying-Data-AMPL-Book.pdf) and [10](https://ampl.com/wp-content/uploads/Chapter-10-Database-Access-AMPL-Book.pdf) of the AMPL book provide more information about specifying data in AMPL.

```{note}
AMPL does not care about the file extensions, but it is customary to use `.dat` for files intended to be read in data mode.
```

#### Lists of one dimensional sets and parameters
For a parameter indexed over a one-dimensional set like the parameter `limit`, the specification of the set can be simply a listing of its members:

```{literalinclude} ampl_files/lemonade.dat
:lines: 4-8
:emphasize-lines: 2-5
:language: ampl
```

and the parameter's specification may be virtually the same except for the addition of a value after each set member:
```{literalinclude} ampl_files/lemonade.dat
:lines: 16-20    
:emphasize-lines: 2-5
:language: ampl
```

The parameter specification could equally well be written as
```ampl
param limit := lemon 10 tea_bag 8 sugar 20;
```
since extra spaces and line breaks are ignored.

#### Lists of two-dimensional sets and parameters
The extension of data lists to the two-dimensional case is largely straightforward, we will examine it in case of parameters, where two one dimensional sets are used for indexing. 
As an example, consider the following from our production model:

```{literalinclude} ampl_files/production.mod
:lines: 1-3, 12    
:emphasize-lines: 2-4
:language: ampl
```

The members of `PROD` and `INGR` can be given as for any one-dimensional sets:

```{literalinclude} ampl_files/mulled_wine.dat
:lines: 1-9
:emphasize-lines: 2, 5-9
:language: ampl
```

Data values for a parameter indexed over two sets, such as the parameter `usage` from our production model are naturally specified in a table as follows:

```{literalinclude} ampl_files/mulled_wine.dat
:lines: 24-29 
:emphasize-lines: 2-6
:language: ampl
```

The row labels give the first index and the column labels the second index, so that for example usage["sugar","hot_tea"] is set to 2.0. 
To enable AMPL to recognize this as a table, a colon must follow the parameter name, while the := operator follows the list of column labels.

#### The complete data files
1. **`lemonade.dat`**
```{literalinclude} ampl_files/lemonade.dat
:language: ampl
:linenos: true
:caption: lemonade.dat
```
Download link: [`lemonade.dat`](https://github.com/gomfy/ampl_tutorial/blob/main/src/source/ampl_files/lemonade.dat)

2. **`mulled_wine.dat`**
```{literalinclude} ampl_files/mulled_wine.dat
:language: ampl
:linenos: true
:caption: mulled_wine.dat
```
Download link: [`mulled_wine.dat`](https://github.com/gomfy/ampl_tutorial/blob/main/src/source/ampl_files/mulled_wine.dat)

#### Solving multiple instances
In this section, we will solve multiple instances of the same production problem. 
The `multi_instance_solve.run` script below leverages a common model – `production.mod` – to tackle our two distinct problems: lemonade and mulled wine production.
The process begins with loading `production.mod`. 
Subsequently, we load `lemonade.dat`, and solve with CBC. 
Once this is done, we use the `reset data;` command to clear the current data in preparation for the next problem instance.

Next, we load the `mulled_wine.dat` data file and use HiGHS to solve the second instance. 
During this process we will continue to rely on scripts introduce earlier, namely ([cbc_solve.run](ampl_files/cbc_solve.run) and ([print_solution.run](ampl_files/print_solution.run)).

::::{tab-set}
:::{tab-item} AMPL
```{literalinclude} ampl_files/multi_instance_solve.run
:language: ampl
:linenos: true
:caption: multi_instance_solve.run
```
Running:

```bash
$ ampl multi_instance_solve.run > multi_instance_solve.run.out
```

Gives:

```{literalinclude} ampl_files/multi_instance_solve.run.out
:caption: multi_instance_solve.run.out
```
:::
::::

##### Using APIs
When using high-level interpreted languages like Python or R, which offer mature methods for handling data, we generally recommend using native data structures like Pandas DataFrames to pass data to AMPL. 
We will delve into this topic in the following section.
However, if you already have an AMPL data file at your disposal and prefer to use that, the examples provided below will guide you on how to do so.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/multi_instance_solve.py
:language: python
:linenos: true
:caption: multi_instance_solve.py
```
For more information about `read_data()` and `eval()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ python multi_instance_solve.py > multi_instance_solve.py.out
```

Gives:

```{literalinclude} ampl_files/multi_instance_solve.py.out
:caption: multi_instance_solve.py.out
```
:::

:::{tab-item} R
```{literalinclude} ampl_files/multi_instance_solve.R
:language: r
:linenos: true
:caption: multi_instance_solve.R
```
For more information about `readData()` and `eval()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.

Running:

```bash
$ Rscript multi_instance_solve.R > multi_instance_solve.R.out
```

Gives:

```{literalinclude} ampl_files/multi_instance_solve.R.out
:caption: multi_instance_solve.R.out
```
:::

:::{tab-item} MATLAB
```matlab
%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about `readData()` and `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```{literalinclude} ampl_files/multi_instance_solve.cc
:language: cpp
:linenos: true
:caption: multi_instance_solve.cc
```

For more information about `readData()` and `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ ./multi_instance_solve > multi_instance_solve.cc.out
```

Gives:

```{literalinclude} ampl_files/multi_instance_solve.cc.out
:caption: multi_instance_solve.cc.out
```
:::

:::{tab-item} C#
```cs
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```

For more information about `ReadData()` and `Eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
:::

:::{tab-item} Java
```java
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```
For more information about `readData()` and `reset()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/java/com/ampl/AMPL.html#methods) of the API documentation.
:::
::::

### Specifying data through APIs
In this section, we will delve into how native objects, such as Pandas DataFrames, can be directly passed to AMPL using its APIs.
AMPL's APIs provide a rich assortment of methods for data passing, the selection of which depends on the working environment (e.g., high-level interpreted languages like Python or compiled languages like C++).
Therefore, we will discuss the specifics in the context of the source code, in the form of comments, provided below.

#### Set data method
In this part, we'll introduce a method that serves as an alternative to AMPL's `.dat` files, which we presented earlier. 
This 'set data' method will load either the lemonade or mulled wine data into AMPL, depending on the argument passed to it, eliminating the need to rely on a `.dat` file.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/set_data.py
:language: python
:linenos: true
:caption: set_data.py
```

For more information about these methods checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.
:::

:::{tab-item} R
```{literalinclude} ampl_files/set_data.R
:language: R
:linenos: true
:caption: set_data.R
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
```{literalinclude} ampl_files/set_data.h
:language: cpp
:linenos: true
:caption: set_data.h
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

#### Solving multiple instances with set data method 
Just as in our earlier examples, we will solve multiple instances of the same production problem in this section. 
The difference here is that we'll use the 'set data' method to supply the necessary data, effectively eliminating the need for `.dat` files.
During this process we will continue to rely on functions introduce earlier, namely `set_n_solve()` and `print_solution()`.

::::{tab-set}
:::{tab-item} Python
```{literalinclude} ampl_files/df_multi_instance_solve.py
:language: python
:linenos: true
:caption: df_multi_instance_solve.py
```
For more information about `read()` and `eval()` checkout the [methods section](https://amplpy.readthedocs.io/en/latest/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ python df_multi_instance_solve.py > df_multi_instance_solve.py.out
```

Gives:

```{literalinclude} ampl_files/df_multi_instance_solve.py.out
:caption: df_multi_instance_solve.py.out
```
:::

:::{tab-item} R
```{literalinclude} ampl_files/df_multi_instance_solve.R
:language: r
:linenos: true
:caption: df_multi_instance_solve.R
```
For more information about `read()` and `eval()` checkout the [methods section](https://rampl.readthedocs.io/en/latest/reference/ramplcpp.html#ampl) of the API documentation.

Running:

```bash
$ Rscript df_multi_instance_solve.R > df_multi_instance_solve.R.out
```

Gives:

```{literalinclude} ampl_files/df_multi_instance_solve.R.out
:caption: df_multi_instance_solve.R.out
```
:::

:::{tab-item} MATLAB
```matlab
%%% %%%%%%%%%%% %%%
%%% COMING SOON %%%
%%% %%%%%%%%%%% %%%
```
For more information about `read()` and `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/matlab/classes/matlabAMPL.html) of the API documentation.
:::

:::{tab-item} C++
```{literalinclude} ampl_files/df_multi_instance_solve.cc
:language: cpp
:linenos: true
:caption: df_multi_instance_solve.cc
```

For more information about `read()` and `eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/cpp/classes/ampl.html#ampl) of the API documentation.

Running:

```bash
$ ./df_multi_instance_solve > df_multi_instance_solve.cc.out
```

Gives:

```{literalinclude} ampl_files/df_multi_instance_solve.cc.out
:caption: df_multi_instance_solve.cc.out
```
:::

:::{tab-item} C#
```cs
/// /////////// ///
/// COMING SOON ///
/// /////////// ///
```

For more information about `Read()` and `Eval()` checkout the [methods section](https://portal.ampl.com/docs/api/latest/dotnet/autoapi/ampl/AMPL/index.html#methods) of the API documentation.
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
