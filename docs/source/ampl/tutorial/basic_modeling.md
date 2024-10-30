# Basic modeling
We'll start this section by presenting an example and formulating an integer program from it.
We'll walk through the essential AMPL syntax required to construct a model based on this example. 

Before we delve into the details, we'll provide a brief summary of the AMPL concepts we're going to explore in this section:

:::{admonition} Section summary
In this section we will learn the following:

1. **AMPL's syntax and lexical rules:**
    * AMPL is declarative.
    * AMPL is case sensitive. 
    * AMPL ignores white space.
    * AMPL comments start with `#`.
    
<br>

2. **Declaring model entities such as variables, parameters, objectives, and constraints** via a simple model that maximizes the profit of a lemonade stand:
    ```{literalinclude} ampl_files/lemonade.mod
    :language: ampl
    :linenos: true
    :caption: lemonade.mod
    ```

<br>

:::

## Problem formulation
Imagine you own a small lemonade stand and want to make the most profit possible. 
You offer two drinks: lemonade $(x_{\textrm{lemonade}})$, which requires two cups of water, one lemon and two cups of sugar per glass, and iced tea $(x_{\textrm{iced_tea}})$, which requires one tea bag, one cup of sugar, and two cups of water per glass. 
Thankfully, you have unlimited access to water for free.

However, you have limited "dry" ingredients to work with each day, including 10 lemons, 8 tea bags, and 20 cups of sugar.
Fortunately, you receive a daily inheritance of ingredients from a relative, so you don't have to worry about purchasing them.

Your goal is to decide how many glasses of each drink to make while staying within your daily ingredient limits to maximize your profit. 
You can sell each glass of lemonade for \$1.50 and each glass of iced tea for \$1.00. 
You also pay the city a daily permit fee of $2 to keep your stand open. 
Since you're the only lemonade stand in town, you won't be spending any money on iced tea or lemonade anywhere else, and will sell all that you make.

To formulate this as an integer programming problem, we can use the following model:

$$
\begin{equation}
\begin{array}{lcrcrl}
&\textrm{Objective:}  & \max & 1.5x_{\textrm{lemonade}} & + & x_{\textrm{iced_tea}} &   -  & 2  \\
&\textrm{Subject to:} &      &                          &   &                       &      &    \\
&                     &      &    x_{\textrm{lemonade}} &   &                       & \leq & 10 \\
&                     &      &                          &   & x_{\textrm{iced_tea}} & \leq &  8 \\
&                     &      &   2x_{\textrm{lemonade}} & + & x_{\textrm{iced_tea}} & \leq & 20 \\
&                     &      &                          &   &                       &      &    \\
&                     &      &    x_{\textrm{lemonade}} &   &                       & \geq & 0  \\
&                     &      &                          &   & x_{\textrm{iced_tea}} & \geq & 0  \\
&                     &      &    x_{\textrm{lemonade}} & , & x_{\textrm{iced_tea}} & \in  & \mathbb{Z}
\end{array}
\end{equation}
$$ (ip:lemonade)

An equivalent formulation of the above problem in AMPL, where our two decision variables are named `lemonade` and `iced_tea`, looks as follows (we will discuss each line in detail throughout the tutorial):

```{literalinclude} ampl_files/lemonade.mod
:language: ampl
:linenos: true
:caption: lemonade.mod
```

On closer look, we can observe that the above model fits into a general production model framework. 
Essentially, we would like to decide how many glasses of lemonade and iced tea to produce to maximize our profits while staying within our resource constraints. 
In other words, the above model can be expressed generally as follows:

$$
\begin{alignat*}{3}
    & \textrm{Maximize: }   &       & \sum_{j \in P} c_{j} x_{j} - C                    & \\
    & \textrm{Subject To: } & \quad & \sum_{{j \in P}} a_{ij} x_j \leq b_i,             & \forall i \in I \\
    &                       & \quad & \quad \quad \quad  x_{j} \in \mathbb{Z},          &\quad \forall j \in P
\end{alignat*}
$$ (ip:production)

Where $P$ is the set of products, $I$ is the set of ingredients, $c_j$ is the profit per unit of product $j$, $x_j$ is the units of product $j$ made, C is a fixed cost, $a_{ij}$ is the usage of ingredient $i$ by unit of product $j$, and $b_i$ is the limit of ingredient $i$.

AMPL allows you to express generalized models such as the one above succinctly in a manner very close to their mathematical formulations.
In the AMPL representation of the above model, we replace our decision variable $x$ with a more descriptive variable called `make`, which is indexed over our set of products. 
Additionally, we introduce parameters for our problem coefficients. 
We will discuss each line of the AMPL model, which is displayed below, in detail in the [general production model section](modeling_and_data.md) of the tutorial.

```{literalinclude} ampl_files/production.mod
:language: ampl
:linenos: true
:caption: production.mod
```

With this generalized AMPL model, you can solve a wide range of production problems by providing different input data for the sets and parameters.
This flexibility allows you to apply the model to various scenarios with different products, ingredients, and cost structures.
As you can see, we have only declared sets and parameters but have not specified their members or values. 
Hence, this model is incomplete and will not produce any results if given to AMPL.
The members and values will have to be provided as input data, which we will discuss [later](#specifying-data).

With the general production model we wanted to demonstrate a more practical way of using AMPL at the beginning of the tutorial, as this formulation allows us to solve different instances of the same class of problems, and is the recommended way of using AMPL.
However, in order to make this section more palatable, we will introduce the basics of AMPL using the specific lemonade model.

Before we jump into modeling with AMPL, let's discuss the basic lexical rules of the AMPL modeling language.


## The AMPL language
Section A.1 of the [appendix](https://ampl.com/wp-content/uploads/Appendix-A-AMPL-Book.pdf) of the AMPL book provides a detailed discussion of AMPL's lexical rules.
We will mention the most important below:

:::{important}
* AMPL models involve variables, constraints, and objectives, expressed with the help of sets and parameters. These are called model entities, each of which has an alphanumeric name such as `lemonade`. Upper-case letters are distinct from lower-case so `lemonade` and `Lemonade` would correspond to two separate entities. 

<br>

* The most basic format for declaring any entity in AMPL consists of the entity type (variable, constraint, etc.), the name you give it, and a semicolon at the end of the statement. For example,
    ```ampl
    var lemonade;
    ```

<br>

* AMPL is a "declarative" language, meaning that entities used in expressions must be declared before they can be used.

<br>

* An expression is similar to a mathematical equation or formula and typically involves variables, constants, and mathematical operators such as addition, subtraction, multiplication, and division. Expressions can also include inequalities, logical operators, and other constructs that allow for complex modeling. In AMPL, expressions are used extensively in the definition of the objective function and constraints of a mathematical program. For example:
    ```{literalinclude} ampl_files/lemonade.mod
    :lines: 9
    :language: ampl
    ```

<br>

* Comments in AMPL files begin with: `#`. For example,
    ```{literalinclude} ampl_files/lemonade.mod
    :lines: 8-9
    :emphasize-lines: 1
    :language: ampl
    ```

<br>

* AMPL ignores white space. For example,
    ```{literalinclude} ampl_files/lemonade.mod
    :lines: 2-3
    :language: ampl
    ```
    is equivalent to
    ```ampl
    var lemonade >= 0; var iced_tea >= 0;
    ```

<br>

:::

```{note}

**Each AMPL statement should end with a semicolon, with the exception of include commands, which we will discuss in more detail later**.
```


## Model formulation in AMPL
To formulate the model introduced in {eq}`ip:lemonade` in AMPL, we need to declare the following key entities: 
1. [variables](#variable-declarations), 
2. [parameters](#parameter-declarations),
3. [objective function](#objective-declarations), and
4. [constraints](#constraint-declarations).

The following sections will cover the basic syntax in AMPL for declaring these entities. 
We will begin with an overview of how to declare variables, then move on to defining the objective function and constraints.
Finally, we will introduce the [complete model](#the-complete-model) in AMPL.


### Variable declarations
We begin by declaring our variables $x_{\textrm{lemonade}}$ and $x_{\textrm{iced_tea}}$. 
However, in AMPL we can use descriptive names for them such as `lemonade` and `iced_tea`.

To declare our variables in AMPL, we first use the `var` keyword followed by the variable name, optional attributes, and a semicolon. 
```{literalinclude} ampl_files/lemonade.mod
:lines: 1-3
:emphasize-lines: 2-3
:language: ampl
```
Here our first variable's name is `lemonade` and we are enforcing the optional attribute of integrality and nonnegativity.

:::{admonition} Advanced: General Variable Syntax
:class: dropdown

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">var</span> <i>name alias<sub>opt</sub> indexing<sub>opt</sub> attributes<sub>opt</sub> </i>;

    <i>attributes: </i>
        <span style="color: darkgreen; font-weight: bold">binary</span>
        <span style="color: darkgreen; font-weight: bold">integer</span>
        <span style="color: darkgreen; font-weight: bold">symbolic</span>
        >= <i>expr</i>
        <= <i>expr</i>
        := <i>expr</i>
        <span style="color: darkgreen; font-weight: bold">default</span> <i>expr</i>
        = <i>expr</i>
        <span style="color: darkgreen; font-weight: bold">coeff</span> <i>indexing<sub>opt</sub> constraint expr</i>
        <span style="color: darkgreen; font-weight: bold">cover</span> <i>indexing<sub>opt</sub> constraint</i>
        <span style="color: darkgreen; font-weight: bold">obj</span> <i>indexing<sub>opt</sub> objective expr</i>
        <span style="color: darkgreen; font-weight: bold">in</span> <i>sexpr</i>
        <span style="color: darkgreen; font-weight: bold">suffix</span> <i>sufname expr</i>
</code>
</pre>

Optional clauses marked with *opt* subscript such as *alias* or *indexing* are discussed in detail in the [AMPL book](https://ampl.com/learn/ampl-book/).

As a brief note, *expr* is shorthand for expression, and *sexpr* stands for set expression.

Regarding *attributes*, nonnegativity of `lemonade` and `iced_tea` is an attribute, which is expressed as `>= 0`, where 0 constitutes the expression.
It is also worth mentioning that by default, AMPL initializes all variables to zero unless an initial value is provided via an attribute (e.g. `var x := 1;` in which case the initial value of `x` becomes 1).
This will be important to keep in mind later on when we discuss computing the value of expressions that involve variables. 
:::

**Reminder:** Each AMPL statement ends with a semicolon.

### Parameter declarations
We will declare the permit fee as a parameter. 
The astute reader might observe that we could also declare other constants specified in the problem as parameters, which we will address in a later section. 

To declare the permit fee as a parameter in AMPL, we use the keyword `param`, followed by the parameter name, an optional initial value assignment, and a semi-colon.

```{literalinclude} ampl_files/lemonade.mod
:lines: 5-6
:emphasize-lines: 2
:language: ampl
```
In this example, we declare a parameter named `fee` for the daily permit fee and set it to 2.

:::{admonition} Advanced: General Parameter Syntax
:class: dropdown

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
   <span style="color: darkgreen; font-weight: bold">param</span> <i>name alias<sub>opt</sub> indexing<sub>opt</sub> attributes<sub>opt</sub> </i>;

    <i>attributes: </i>
        <span style="color: darkgreen; font-weight: bold">binary</span>
        <span style="color: darkgreen; font-weight: bold">integer</span>
        <span style="color: darkgreen; font-weight: bold">symbolic</span>
        <i>relop expr</i>
        <span style="color: darkgreen; font-weight: bold">default</span> <i>expr</i>
        = <i>expr</i>
        <span style="color: darkgreen; font-weight: bold">in</span> <i>sexpr</i>

    <i>relop: </i>
        <  <=  =  ==  !=  <>  >  >=
</code>
</pre>

Optional clauses marked with *opt* subscript such as *alias* or *indexing* are discussed in detail in the [AMPL book](https://ampl.com/learn/ampl-book/).

As a brief note, *expr* is shorthand for expression, *sexpr* stands for set expression, and *relop* is short for relational operator. Parameters can take string values if they are declared as *symbolic*, `param time symbolic := "10:30 AM"`.

Regarding *attributes*, assigning the value 2 to the parameter `fee` during declaration is considered an attribute, which is expressed as `= 2`, where 2 constitutes the expression.
:::

### Objective declarations
The next step is to declare the objective function that will maximize our profits.

To specify an objective function in AMPL, we first have to specify the direction of optimization via the keywords `maximize` or `minimize`, which is followed by a name, a colon, an expression involving our variables, and a semicolon.


```{literalinclude} ampl_files/lemonade.mod
:lines: 8-9
:emphasize-lines: 2
:language: ampl
```

Our goal here is to `maximize` the total `profit` and the expression is the sum of the quantities of each beverage produced times their profit per unit.

:::{admonition} Advanced: General Objective Function Syntax
:class: dropdown

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">maximize</span> <i>name alias<sub>opt</sub> indexing<sub>opt</sub> </i> 
        : <i>expression</i> [ <i>suffix-initialization</i> ] ; 
</code>
</pre>

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    <span style="color: darkgreen; font-weight: bold">minimize</span> <i>name alias<sub>opt</sub> indexing<sub>opt</sub> </i> 
        : <i>expression</i> [ <i>suffix-initialization</i> ] ; 
</code>
</pre>


Optional clauses, such as *suffix-initialization* (marked with [ ]) and *alias* or *indexing* (marked with *opt* subscript), are discussed in detail in the [AMPL book](https://ampl.com/learn/ampl-book/).

In the example above, `profit` is the *name* of the objective and the *expression* is: `1.5*lemonade + iced_tea - fee`.

:::

**Reminder:** Variables must be declared before they can be used in an expression.

```{note}
It's good practice to use a descriptive name for the objective function, such as `profit`, which reflects what we're trying to maximize in our lemonade stand example. 

The expression should be a mathematical formula involving our variables that reflect the goal of the optimization problem.
```

### Constraint declarations
Last, we declare the constraints to appropriately restrict our model. 
We need to have a constraint for each dry ingredient, ensuring that we are limited to using no more than 10 lemons, 8 tea bags, and 20 cups of sugar per day.

To declare our lemonade stand constraints in AMPL, we first use the keywords `subject to`, which is followed by a name, a colon, an expression involving our variables, and a semicolon.

```{literalinclude} ampl_files/lemonade.mod
:lines: 10-14
:emphasize-lines: 2-4
:language: ampl
```

Just like the objective function, we can give constraints an informative name and then provide the appropriate expression to describe the constraint. 
For example, the 20 cup limit on sugar and quantities needed for each lemonade and iced tea is captured in the `sugar_constraint` expression.

:::{admonition} Advanced: General Constraint Syntax
:class: dropdown

<pre style="background-color:LavenderBlush">
<code style="background-color:LavenderBlush">
    [ <span style="color: darkgreen; font-weight: bold">subject to</span> ] <i>name alias<sub>opt</sub> indexing<sub>opt</sub> </i>
        [:= <i> initial_dual </i>] [ <span style="color: darkgreen; font-weight: bold">default</span> <i>initial_dual</i> ] 
        : <i>constraint expression</i> [ <i>suffix-initialization</i> ] ;  
</code>
</pre>

**Constraint expressions** can take two forms one-sided and two-sided.

**One-sided** constraint expressions must be specified in one of the following forms:

$$
\begin{equation}
\begin{array}{lcl}
\textrm{expression} & <=  & \textrm{expression} \\
\textrm{expression} & =  & \textrm{expression}  \\
\textrm{expression} & >=  & \textrm{expression}
\end{array}
\end{equation}
$$

Whereas **two-sided** constraint expressions must be declared in one of the following forms:

$$
\begin{equation}
\begin{array}{lcccr}
\textrm{constant expression} & <= & \textrm{expression} & <=  & \textrm{constant expression} \\
\textrm{constant expression} & >= & \textrm{expression} & >=  & \textrm{constant expression} \\
\end{array}
\end{equation}
$$

A **constant expression** is an expression that does not contain any variables.

Optional clauses, such as *initial_dual* or *suffix-initialization*  (marked with [ ]) and *alias* or *indexing* (marked with *opt* subscript), are discussed in detail in the [AMPL book](https://ampl.com/learn/ampl-book/).

In the example above, `lemon_constraint` is the *name* of the constraint and the one-sided *expression* is: `lemonade <= 10`.
:::

````{note}
The `subject to` keyword used to declare constraints can be shortened to `s.t.` or even omitted entirely. In the former case our sugar constraint could be declared as follows: 

```ampl
s.t. sugar_constraint: 2*lemonade + iced_tea <= 20;
```
 
In the latter case, while **not recommended** in order to retain model clarity, the constraint declaration for our sugar constraint would simply start with the name of the constraint i.e. 

```ampl
sugar_constraint: 2*lemonade + iced_tea <= 20;
``` 
````

(the-complete-model)=
### The complete model 
Below we introduce the above lemonade integer program in AMPL in its entirety. 
As you can see it looks very similar to the mathematical formulation in {eq}`ip:lemonade`. 

```{literalinclude} ampl_files/lemonade.mod
:language: ampl
:linenos: true
:caption: lemonade.mod
```

Download link: [lemonade.mod](ampl_files/lemonade.mod)
