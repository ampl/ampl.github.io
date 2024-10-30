# Introduction
**Welcome to this AMPL tutorial!**
In this tutorial, we will focus on exploring the AMPL modeling language itself and the AMPL interpreter. 

However, before we begin, we would be remiss not to point out that AMPL is much more than just a modeling language. 
Upon implementing our optimization model in AMPL, we gain access to the comprehensive **AMPL Ecosystem**, significantly enhancing the power and flexibility of our modeling capabilities.
The main pillars of the AMPL Ecosystem are the extensive set of solver libraries and interfaces, our APIs, and data connectors. 
The features of AMPL along with its Ecosystem allows us to: 

<br>

   * **Readily formulate our optimization problems as abstract models that are close to their mathematical formulation and hence easily understandable.**

<br>

   * **Comfortably solve multiple instances of the same problem class because AMPL's features allow us to separate optimization problem coefficients, i.e. "data" from the model.** 

<br>

   * **Effortlessly experiment with different solvers.**

<br>

   * **Smoothly embed our model into production systems via:** 
        * [APIs](apis), such as [Python](https://amplpy.readthedocs.io/en/latest/), [R](https://rampl.readthedocs.io/en/latest/), [C++](https://portal.ampl.com/docs/api/latest/cpp/) or [Java](https://portal.ampl.com/docs/api/latest/java/).
        * [Data connectors](https://amplplugins.readthedocs.io/en/latest/rst/userguides.html) such as [CSV](https://amplplugins.readthedocs.io/en/latest/rst/amplcsv.html) and [Spreadsheet](https://amplplugins.readthedocs.io/en/latest/rst/amplxl.html) interfaces or [Table Handlers](https://amplplugins.readthedocs.io/en/latest/rst/ampltabl.html) for relational databases.

<br>

Through out this tutorial we will concentrate on the first three concepts mentioned above. 


## Prerequisites
In order to follow along with this tutorial, please ensure the following:

<br>

* **Have AMPL and solvers installed.**
   * Check out our {ref}`installation instructions <how-to-install-ampl>` for details.
   * You can check to see if AMPL was installed correctly by typing `ampl` into a command prompt or opening the AMPL IDE.
   * Make sure that the solvers {ref}`HiGHS <highs>` and {ref}`CBC <cbc>` were installed and are discoverable by AMPL. Open source solvers such as HiGHS and CBC are available in AMPL by default. If you have followed the installation instructions correctly, they should be available and there is no need for additional steps.

<br>

* **Have access to a text editor.** AMPL users have a wide variety of options available:
   * [AMPL IDE](https://ampl.com/products/ampl/ide/).
   * [VS Code](https://code.visualstudio.com/) with [AMPL plugin](https://marketplace.visualstudio.com/items?itemName=michael-sundvick.ampl).
   * [Vim](https://www.vim.org/) or [Emacs](https://www.gnu.org/software/emacs/) with [AMPL plugin](https://github.com/dpo/ampl-mode).
   * Any text editor capable of generating plain text files.

<br>

If you experience any difficulties with the above steps, please reach out via our [Discuss](https://discuss.ampl.com/) forum or [support@ampl.com](mailto:support@ampl.com) email.


## Overview
In this tutorial, we will introduce the basic concepts in AMPL through a simple example of a lemonade stand, where our goal is to maximize our daily profit by deciding how many glasses of lemonade and iced tea to sell.

After introducing the mathematical formulation of a problem, we will present a corresponding AMPL model file, followed by a discussion of the file's components and a demonstration of basic AMPL commands and concepts using the model at hand. 
 
By the end of this tutorial, you will know how to declare model entities, such as variables, parameters, objectives and constraints. 
You will also have acquired a sense of how to use AMPL's powerful features to streamline your optimization workflow by creating abstract models that can be applied to many different instances of the same problem class.
As well as using various AMPL commands to investigate your model and its solution.

<br>

```{note}
Please note that this tutorial provides a basic introduction to AMPL concepts and is not intended to cover all the details comprehensively. There is much more to each AMPL concept than what is discussed in this tutorial. For a complete and detailed explanation of these concepts, we recommend referring to the [AMPL book](https://ampl.com/wp-content/uploads/BOOK.pdf). 
```
