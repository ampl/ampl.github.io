# Commands and data

Finally, we will formulate our production model in AMPL and review some useful AMPL commands that enhance efficiency when working with abstract models and data files.

% MISSING INTRO AND SUMMARY

% WORK THIS IN AS WELL:

## `if` statements in parameter declarations

Below we will introduce two scripts, the first script shows how to create a conditional expression using the `if` statement and demonstrate the use of `let`.
 

that first loads [mulled_wine.mod](ampl_files/mulled_wine.mod).
Next, we create a two-dimensional parameter that will hold our guesses (one for each variable `mulled_wine` and `hot_tea`). 
We can use AMPL's `if` statement to construct a conditional expression and use it during the declaration of `my_guess` to assign 4 to `my_guess[1]` and 8 to `my_guess[2]`. 
The `if` statement checks the value of the dummy variable `i`, which assumes values 1 and 2.
If `i == 1`, then `my_guess[i] := 4`; otherwise `my_guess[i] := 8`.
Then we will use AMPL's `let` command to overwrite the default values of our variables by using AMPL's built-in variable `_var`.
Finally, the display statement is there to validate that we have successfully assigned new values to our variables.

```{literalinclude} ampl_files/mulled_wine_let_param.run
:language: ampl
:linenos: true
:caption: mulled_wine_let_param.run
```


The general form of a conditional expression is:

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">if</span> <i>lexpr</i> <span style="color: darkgreen; font-weight: bold">then</span> <i>expr<sub>true</sub></i> <span style="color: darkgreen; font-weight: bold">else</span> <i>expr<sub>false</sub></i>  ;
</code>
</pre>

where <i>lexpr</i> is a logical expression. 
If <i>lexpr</i> evaluates to true, the conditional expression takes the value of <i>expr<sub>true</sub></i>; if <i>lexpr</i> is false, the expression takes the value of <i>expr<sub>false</sub></i>. 
If <i>expr<sub>false</sub></i> is zero, the `else` <i>expr<sub>false</sub></i> </code> part can be dropped.

Most often, <i>expr<sub>true</sub></i> and <i>expr<sub>false</sub></i> are arithmetic expressions, but they can also be string or set expressions, as long as both are expressions of the same kind. 
Since `then` and `else` have lower precedence than any other operators, a conditional expression must be parenthesized, unless it occurs at the end of a statement.







(the-display-command)=
### The `display` command
As mentioned before the AMPL book dedicates an entire chapter ([Ch. 12](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf)) to the `display` command.
It uses the same list and table formats as the data statements described above and more extensively in [Ch. 9](https://ampl.com/wp-content/uploads/Chapter-9-Specifying-Data-AMPL-Book.pdf) of the AMPL book. 
By default `display` automatically formats the values in an intuitive and familiar arrangement; as much as possible.
However, the formatting can also be influenced through the setting of various options discussed in detail in [Ch. 12](https://ampl.com/wp-content/uploads/Chapter-12-Display-Commands-AMPL-Book.pdf) of the AMPL book.

The easiest way to examine data and also result values is to type `display` and a description of what you want to look at.
For example, if we simply want to print the values of the `usage` parameter for the mulled wine example simply type `display usage;`: 

```ampl
ampl: model production.mod
ampl: data mulled_wine.dat
ampl: display usage;
usage :=
spice   hot_tea       0
spice   mulled_wine   2
sugar   hot_tea       2
sugar   mulled_wine   4
tea_bag hot_tea       1
tea_bag mulled_wine   0
wine    hot_tea       0
wine    mulled_wine   2
;

```

`display` can also handle expressions, we could easily display results of computations such as the cross product of the `INGR` and `PROD` sets:

```ampl
ampl: display INGR cross PROD;
set INGR cross PROD :=
(spice,mulled_wine)     (tea_bag,hot_tea)       (wine,mulled_wine)
(spice,hot_tea)         (sugar,mulled_wine)     (wine,hot_tea)
(tea_bag,mulled_wine)   (sugar,hot_tea);
```


:::{admonition} Advanced: `display` command
:class: dropdown

The `display` command formats various entities in tables or lists, as appropriate, it has the following syntax:

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">display</span> <i>[ indexing: ] disparglist redirection<sub>opt</sub> </i>;
</code>
</pre>



The *disparglist* is similar to an *arglist* for `print` or `printf`, except that an item to be displayed can also be a set expression or the unsubscripted name of an indexed parameter, variable, constraint, or set; furthermore iterated *arglists* cannot be nested, i.e., they are restricted to the forms

```
indexing expr
indexing ( exprlist )
```

where *exprlist* is a nonempty, comma-separated list of expressions. 
The `display` command prints scalar expressions and sets individually, and partitions indexed entities into groups having the same number of subscripts, then prints each group in its own table or sequence of tables.

By default, the display command rounds numeric expressions to six significant figures, but this can be changed with the options `display_precision` or `display_round`.

:::



### Solving the lemonade instance
After loading `production.mod`, we load `lemonade.dat`, set a solver, execute the solve command, and display the solution:

```ampl
ampl: model production.mod
ampl: data lemonade.dat 
ampl: include highs_solve.run

HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes

ampl: display _varname, _var;
:        _varname      _var    :=
1   "make['lemonade']"   6
2   "make['iced_tea']"   8
;
```

As you can see, using generic synonyms with the `display` command has become even more straightforward than with `print` commands.

    
### Solving the mulled wine instance
After loading `production.mod`, we load `mulled_wine.dat`, set a solver, execute the solve command, and display the solution:

```ampl
ampl: model production.mod   
ampl: data mulled_wine.dat
ampl: include cbc_solve.run

cbc 2.10.7: optimal solution; objective 16.5
0 simplex iterations

ampl: display _varname, _var;
:         _varname        _var    :=
1   "make['mulled_wine']"   4
2   "make['hot_tea']"       7
;
```

There is an even more efficient way to solve multiple instances of the same abstract problem with the help of the `reset data;` command.
In the next section we will introduce the various `reset;` commands.


#### The `reset` commands
Section A.18 in the [appendix](https://ampl.com/wp-content/uploads/Appendix-A-AMPL-Book.pdf) of the AMPL book provides a concise summary of AMPL's modeling commands, including various versions of the `reset;` command.

The `reset` command has several forms.

`reset;` causes AMPL to forget all model declarations while retaining the current option settings. 

We can also `reset options;` to reset all options.

`reset data;` causes AMPL to forget all assignments read in data mode and allows for reading data for a different problem instance.
We can also reset only specific values of the data using:
<code>
    reset data <i>name-list </i>;
</code>. 
This causes AMPL to forget any data read for the entities within the names listed.

Below, we first solve the lemonade instance, then call `reset data;` and load the mulled wine data. 
Since our `highs_solve.run` script already set the solver option we can simply call `solve;` to obtain the solution for the mulled wine instance.

```ampl
ampl: model production.mod   
ampl: data lemonade.dat      
ampl: include highs_solve.run

HiGHS 1.5.1: optimal solution; objective 15
0 simplex iterations
1 branching nodes

ampl: display _varname, _var;
:        _varname      _var    :=
1   "make['lemonade']"   6
2   "make['iced_tea']"   8
;

ampl: reset data;
ampl: data mulled_wine.dat
ampl: solve;     
HiGHS 1.5.1: optimal solution; objective 16.5
1 simplex iterations
1 branching nodes
ampl: 
ampl: display _varname, _var;
:         _varname        _var    :=
1   "make['mulled_wine']"   4
2   "make['hot_tea']"       7
;
```

Notice that we have found the same optimal solutions as we did using our first and second model for their respective problems.


## Summary 

```{important}
Through the general production model and its data files we have introduced:
1. Sets and indexing in AMPL.
2. General parametric models in AMPL.
3. AMPL data mode and how load data for abstract models.
```


```{todo}
- [x] Introduce comments somewhere on the top.
- [] Built-in functions.
- [x] Brief intro to AMPL syntax etc white space doesn't matter etc.
- [] Say something in the introduction about how the real power of AMPL is in the parameteric formulation.
- [] See if we can fit redeclare somewhere in the beginning.
- [x] Say something about how the first two models we will defer talking about sets, data files etc. so we can focus on more basic things but that the real power of AMPL lies in the advanced topics.
- [] Model analysis, shadow prices etc.
- [] At the end mention things that weren't discussed.
- [x] Add refernce to APIs, data connectors.
- [x] Add something about APIs data connectors in the beginning as well. You can insert data from other places and analyze results in other places.
- [] Add to the beginning something about AMPL being a very powerful language that can tell you a lot about your model, presolve, show_stats, gentimes. etc.
- [] **AMPL doesn't restrict you, you can use other software to feed data or extract data from AMPL**
- [] Cutting stock problem in AMPL knapsack etc.
- [] generate visualizations.


#### `check` and `let`
 A `check` statement has the following syntax where *lexpr* stands for a logical expression:

---
**`check` statement**
 
<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">check</span> <i>[indexing<sub>opt</sub> :] lexpr    </i>;
</code>
</pre>
---


---
**`let` command**
 
<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">let</span> <i>indexing<sub>opt</sub> name :=  expr    </i>;
</code>
</pre>
---

The `let` command is one way to modify the data, it is convenient when only changing one or a couple values in your data. 
The `let` command can update the value of the possibly indexed set, parameter or variable name to the value of the expression given.

To demonstrate these, we can create a new model exactly the same as our production model, but with an additional `check` statement ensuring nonnegativity of the stand fee.

Download link: [production_chk.mod](https://github.com/gomfy/ampl_tutorial/blob/main/src/source/ampl_files/production_chk.mod)

Now running the modified model we load our model, data, but manually set a negative fee with a `let` command, this will then fail our `check` when we attempt to solve the model as we see above. 
```




