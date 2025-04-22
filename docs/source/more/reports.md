# Reports & Papers

## General principles of modeling languages

Robert Fourer, [Algebraic Modeling Languages for Optimization](../REFS//amlopt.pdf). In S.I. Gass and M.C. Fu, eds., _Encyclopedia of Operations Research and Management Science,_ Springer (2013).

Robert Fourer, [On the Evolution of Optimization Modeling Systems](https://www.zib.de/groetschel/pubnew/paper/groetschelismp2012.pdf). M. Groetschel, _Optimization Stories._ Documenta Mathematica (2012) 377-388.

Robert Fourer, [Modeling Languages versus Matrix Generators for Linear Programming](https://dx.doi.org/10.1145/357456.357457). _ACM Transactions on Mathematical Software_ **9** (1983) 143-183.

Abstract:
> Linear optimization problems (linear programs) are expressed in one kind of form for human modelers, but in a quite different form for computer algorithms. Translation from the modeler’s form to the algorithm’s form is thus an unavoidable task in linear programming. Traditionally, this task of translation has been divided between human and computer, through the writing of computer programs known as matrix generators.

> An alternative approach leaves almost all of the work of translation to the computer. Central to such an approach is a computer-readable _modeling language_ that expresses a linear program in much the same way that a modeler does. It is argued that modeling languages should lead to more reliable application of linear programming at lower overall cost.

## General principles of AMPL

David M. Gay, [The AMPL Modeling Language — an Aid to Formulating and Solving Optimization Problems](../REFS//muscat14.pdf). In _Recent Developments in Numerical Analysis and Optimization_, M. Al-Baali, L. Grandinetti and A. Purnama, eds., _Springer Proceedings in Mathematics and Statistics_ (to appear).

Abstract:
> Optimization problems arise in many contexts. Sometimes finding a good formulation takes considerable effort. A modeling language, such as AMPL, facilitates experimenting with formulations and simplifies using suitable solvers to solve the resulting optimization problems. AMPL lets one use notation close to familiar mathematical notation to state variables, objectives, and constraints and the sets and parameters that may be involved. AMPL does some problem transformations and makes relevant problem information available to solvers. The AMPL command language permits computing and displaying information about problem details and solutions returned by solvers. It also lets one modify problem formulations and solve sequences of problems. AMPL addresses both continuous and discrete optimization problems and offers some constraint programming facilities for the latter. More generally, AMPL permits stating and solving problems with complementarity constraints. For continuous problems, AMPL makes first and second derivatives available via automatic differentiation. The freely available AMPL/solver interface library (ASL) facilitates interfacing with solvers. This paper gives an overview of AMPL and its interaction with solvers and discusses some problem transformations and implementation techniques. It also looks forward to possible enhancements to AMPL.

Robert Fourer, David M. Gay and Brian W. Kernighan, [Design Principles and New Developments in the AMPL Modeling Language](../REFS//design.pdf). In _Modeling Languages in Mathematical Optimization_, J. Kallrath, ed., Kluwer Academic Publishers, Dordrecht, The Netherlands (2003).

Abstract:
> The design of the AMPL modeling language stresses naturalness of expressions, generality of iterating over sets, separation of model and data, ease of data manipulation, and automatic updating of derived values when fundamental values change. We show how such principles have guided the addition of database access, complementarity modeling, and other language features.

Robert Fourer, David M. Gay and Brian W. Kernighan, [A Modeling Language for Mathematical Programming](https://dx.doi.org/10.1287/mnsc.36.5.519). Management Science **36** (1990) 519-554.

Abstract:
> Practical large-scale mathematical programming involves more than just the application of an algorithm to minimize or maximize an objective function. Before any optimizing routine can be invoked, considerable effort must be expended to formulate the underlying model and to generate the requisite computational data structures. AMPL is a new language designed to make these steps easier and less error-prone. AMPL closely resembles the symbolic algebraic notation that many modelers use to describe mathematical programs, yet it is regular and formal enough to be processed by a computer system; it is particularly notable for the generality of its syntax and for the variety of its indexing operations. We have implemented a translator that takes as input a linear AMPL model and associated data, and produces output suitable for standard linear programming optimizers. Both the language and the translator admit straightforward extensions to more general mathematical programs that incorporate nonlinear expressions or discrete variables.

## Hooking solvers to AMPL

David M. Gay, [Hooking Your Solver to AMPL](../REFS//hooking3.pdf). Technical report, Bell Laboratories, Murray Hill, NJ (1993; revised 1994, 1997).

Abstract:
> This report tells how to make solvers work with AMPL’s solve command. It describes an interface library, amplsolver.a, whose source is available from the AMPL web site in https://ampl.com/netlib/ampl (where updates first appear) and from netlib. Examples include programs for listing LPs, automatic conversion to the LP dual (shell-script as solver), solvers for various nonlinear problems (with first and sometimes second derivatives computed by automatic differentiation), and getting C or Fortran 77 for nonlinear constraints, objectives, and their first derivatives. Drivers for various well known linear, mixed-integer, and nonlinear solvers provide more examples.

## Running AMPL remotely on the NEOS Server

Elizabeth D. Dolan, Robert Fourer, Jean-Pierre Goux, Todd S. Munson and Jason Sarich, [Kestrel: An Interface from Optimization Modeling Systems to the NEOS Server](https://dx.doi.org/10.1287/ijoc.1080.0264). _INFORMS Journal on Computing_ **20** (2008) 525-538. 

Abstract:
> The NEOS server provides access to a variety of optimization resources via the Internet. The new Kestrel interface to the server enables local modeling environments to request NEOS optimization services and retrieve the results for local visualization and analysis so that users have the same convenient access to remote NEOS solvers as to those installed locally. Kestrel agents have been implemented for the AMPL and GAMS modeling environments; these agents have been designed so that subproblems can be queued for execution and later retrieval of results, making possible a rudimentary form of parallel processing.

Elizabeth D. Dolan, Robert Fourer, Jorge J. Moré and Todd S. Munson, [Optimization on the NEOS Server](https://www.siam.org/pdf/news/457.pdf). _SIAM News_ **35,** 6 (July/August 2002), 4, 8-9.

## Details of AMPL’s design

David M. Gay, [Revisiting Expression Representations for Nonlinear AMPL Models](../REFS//muscat17.pdf). _4th International Conference on Numerical Analysis and Optimization,_ Muscat, Oman, 2-5 January 2017.

Abstract:
> AMPL facilitates stating and solving nonlinear programming problems involving algebraically defined objectives and constraints. For solving such problems, the AMPL/solver interface library provides routines that compute objective functions, constraint residuals, and associated derivatives. Objectives and constraint bodies hitherto have been represented by ‘‘executable’’ expression graphs, in which each node points to its operands and to a function that computes the node’s result. Nodes also store partial derivatives for use in computing gradients and Hessians by automatic differentiation. Storing these values makes the graphs nonreentrant. To enable several threads to evaluate the same expression at different points without having separate copies of the expression graphs, such details as variable values and partial derivatives must be stored in thread-specific arrays. We describe and compare some expression-graph representations for use in computing function, gradient, and Hessian values, and for extracting some auxiliary problem information. In particular, we describe some details of an updated AMPL/solver interface library that uses operation lists to represent expressions.

David M. Gay, [Using Expression Graphs in Optimization Algorithms](https://dx.doi.org/10.1007/978-1-4614-1927-3_8). _Mixed-Integer Nonlinear Programming: IMA Volumes in Mathematics and its Applications_ **154** (2012) 247-262.

Abstract:
> An expression graph, informally speaking, represents a function in a way that can be manipulated to reveal various kinds of information about the function, such as its value or partial derivatives at specified arguments and bounds thereon in specified regions. (Various representations are possible, and all are equivalent in complexity, in that one can be converted to another in time linear in the expression’s size.) For mathematical programming problems, including the mixed-integer nonlinear programming problems that were the subject of the IMA workshop that led to this paper, there are various advantages to representing problems as collections of expression graphs. “Presolve” deductions can simplify the problem, e.g., by reducing the domains of some variables and proving that some inequality constraints are never or always active. To find global solutions, it is helpful sometimes to solve relaxed problems (e.g., allowing some “integer” variables to vary continuously or introducing convex or concave relaxations of some constraints or objectives), and to introduce “cuts” that exclude some relaxed variable values. There are various ways to compute bounds on an expression within a specified region or to compute relaxed expressions from expression graphs. This paper sketches some of them. As new information becomes available in the course of a branch-and-bound (or -cut) algorithm, some expression-graph manipulations and presolve deductions can be revisited and tightened, so keeping expression graphs around during the solution process can be helpful. Algebraic problem representations are a convenient source of expression graphs. One of my reasons for interest in the AMPL modeling language is that it delivers expression graphs to solvers.

Robert Fourer and David M. Gay, [Numerical Issues and Influences in the Design of Algebraic Modeling Languages for Optimization](../REFS//dundee03.pdf). In _Proceedings of the 20th Biennial Conference on Numerical Analysis,_ Dundee, Scotland, D.F. Griffiths and D.A. Watson, eds. Numerical Analysis Report NA/217 (2003) 39-51.

Robert Fourer and David M. Gay, [Extending an Algebraic Modeling Language to Support Constraint Programming](https://dx.doi.org/10.1287/ijoc.14.4.322.2825). _INFORMS Journal on Computing_ **14**, 4 (2002) 322-344.

Abstract:
> Although algebraic modeling languages are widely used in linear and nonlinear programming applications, their use for combinatorial or discrete optimization has largely been limited to developing integer linear programming models for solution by general-purpose branch-and-bound procedures. Yet much of a modeling language’s underlying structure for expressing integer programs is equally useful for describing more general combinatorial optimization constructs.

> Constraint programming solvers offer an alternative approach to solving combinatorial optimization problems, in which natural combinatorial constructs are addressed directly within the solution procedure. Hence the growing popularity of constraint programming motivates a variety of extensions to algebraic modeling languages for the purpose of describing combinatorial problems and conveying them to solvers.

> We examine some of these language extensions along with the significant changes in solver interface design that they require. In particular, we describe how several useful combinatorial features have been added to the AMPL modeling language and how AMPL’s general-purpose solver interface has been adapted accordingly. As an illustration of a solver connection, we provide examples from an AMPL driver for ILOG Solver.

David M. Gay, [Symbolic-Algebraic Computations in a Modeling Language for Mathematical Programming](../REFS//sacomp.pdf). In _Symbolic Algebraic Methods and Verification Methods,_ G. Alefeld, J. Rohn, and T. Yamamoto, eds, Springer-Verlag (2001) 99-106.

Abstract:
> This paper was written for the proceedings of a seminar on “Symbolic-Algebraic Methods and Verification Methods — Theory and Applications” held 21-26 November 1999 at Schloss Dagstuhl, Germany. It gives an overview of symbolic and algebraic computations within the AMPL processor and its associated solver interface library.

Robert Fourer and David M. Gay, [Conveying Problem Structure from an Algebraic Modeling Language to Optimization Algorithms](../REFS//probstruc.pdf). In _Computing Tools for Modeling, Optimization and Simulation: Interfaces in Computer Science and Operations Research,_ M. Laguna and J.L. González-Velarde, eds., Kluwer Academic Publishers, Dordrecht, The Netherlands (2000). 

Abstract:
> Optimization algorithms can exploit problem structures of various kinds, such as sparsity of derivatives, complementarity conditions, block structure, stochasticity, priorities for discrete variables, and information about piecewise-linear terms. Moreover, some algorithms deduce additional structural information that may help the modeler. We review and discuss some ways of conveying structure, with examples from our designs for the AMPL modeling language. We show in particular how “declared suffixes” provide a new and useful way to express structure and acquire solution information.

Michael C. Ferris, Robert Fourer and David M. Gay, [Expressing Complementarity Problems in an Algebraic Modeling Language and Communicating Them to Solvers](https://dx.doi.org/10.1137/S105262349833338X). _SIAM Journal on Optimization_ **9** (1999) 991-1009.

Abstract:
> Diverse problems in optimization, engineering, and economics have natural formulations in terms of complementarity conditions, which state (in their simplest form) that either a certain nonnegative variable must be zero or a corresponding inequality must hold with equality, or both. A variety of algorithms have been devised for solving problems expressed in terms of complementarity conditions. It is thus attractive to consider extending algebraic modeling languages, which are widely used for sending ordinary equations and inequality constraints to solvers, so that they can express complementarity problems directly. We describe an extension to the AMPL modeling language that can express the most common complementarity conditions in a concise and flexible way, through the introduction of a single new “complements” operator. We present details of an efficient implementation that incorporates an augmented presolve phase to simplify complementarity problems, and that converts complementarity conditions to a canonical form convenient for solvers.

Robert Fourer, [Extending a General-Purpose Algebraic Modeling Language to Combinatorial Optimization: A Logic Programming Approach](../REFS//loglang.pdf). In D.L. Woodruff, ed., _Advances in Computational and Stochastic Optimization, Logic Programming, and Heuristic Search: Interfaces in Computer Science and Operations Research,_ Kluwer Academic Publishers (Dordrecht, The Netherlands, 1998) 31-74.

David M. Gay, [Automatically Finding and Exploiting Partially Separable Structure in Nonlinear Programming Problems](../REFS//psstruc.pdf). Bell Laboratories, Murray Hill, NJ (1996).

Abstract:
> Nonlinear programming problems often involve an objective and constraints that are partially separable — the sum of terms involving only a few variables (perhaps after a linear change of variables). This paper discusses finding and exploiting such structure in nonlinear programming problems expressed symbolically in the AMPL modeling language. For some computations, such as computing Hessians by backwards automatic differentiation, exploiting partial separability can give significant speedups.

David M. Gay, [More AD of Nonlinear AMPL Models: Computing Hessian Information and Exploiting Partial Separability](../REFS//ad96.pdf). In _Computational Differentiation: Techniques, Applications, and Tools,_ M. Berz, C. Bischof, G. Corliss and A. Griewank, eds., SIAM (Philadelphia, 1996) 173-184. 

Abstract:
> We describe computational experience with automatic differentiation of mathematical programming problems expressed in the modeling language AMPL. Nonlinear expressions are translated to loop-free code, which makes it easy to compute gradients and Jacobians by backward automatic differentiation. The nonlinear expressions may be interpreted or, to gain some evaluation speed at the cost of increased preparation time, converted to Fortran or C. We have extended the interpretive scheme to evaluate Hessian (of Lagrangian) times vector. Detecting partially separable structure (sums of terms, each depending, perhaps after a linear transformation, on only a few variables) is of independent interest, as some solvers exploit this structure. It can be detected automatically by suitable “tree walks”. Exploiting this structure permits an AD computation of the entire Hessian matrix by accumulating Hessian times vector computations for each term, and can lead to a much faster computation of the Hessian than by computing the whole Hessian times each unit vector.

Robert Fourer and David M. Gay, [Expressing Special Structures in an Algebraic Modeling Language for Mathematical Programming](../REFS//spestruc.pdf). _ORSA Journal on Computing_ **7** (1995) 166-190. 

Abstract:
> A knowledge of the presence of certain special structures can be advantageous in both the formulation and solution of linear programming problems. Thus it is desirable that linear programming software offer the option of specifying such structures explicitly. As a step in this direction, we describe extensions to an algebraic modeling language that encompass piecewise-linear, network and related structures. Our emphasis is on the modeling considerations that motivate these extensions, and on the design issues that arise in integrating these extensions with the general-purpose features of the language. We observe that our extensions sometimes make models faster to translate as well as to solve, and that they permit a “column-wise” formulation of the constraints as an alternative to the “row-wise” formulation most often associated with algebraic languages.

Robert Fourer and David M. Gay, [Experience with a Primal Presolve Algorithm](../REFS//pripre.pdf). In _Large Scale Optimization: State of the Art,_ W.W. Hager, D.W. Hearn and P.M. Pardalos, eds., Kluwer Academic Publishers (Dordrecht, 1994) 135-154.

Abstract:
> Sometimes an optimization problem can be simplified to a form that is faster to solve. Indeed, sometimes it is convenient to state a problem in a way that admits some obvious simplifications, such as eliminating fixed variables and removing constraints that become redundant after simple bounds on the variables have been updated appropriately. Because of this convenience, the AMPL modeling system includes a “presolver” that attempts to simplify a problem before passing it to a solver. The current AMPL presolver carries out all the primal simplifications described by Brearely _et al._ in 1975. This paper describes AMPL’s presolver, discusses reconstruction of dual values for eliminated constraints, and presents some computational results.

David M. Gay, [Automatic Differentiation of Nonlinear AMPL Models](../REFS//autodiff.pdf). In _Automatic Differentiation of Algorithms: Theory, Implementation, and Application,_ A. Griewank and G. Corliss, eds., SIAM (Philadelphia, 1991) 61-73.

Abstract:
> We describe favorable experience with automatic differentiation of mathematical programming problems expressed in AMPL, a modeling language for mathematical programming. Nonlinear expressions are translated to loop-free code, which makes analytically correct gradients and Jacobians particularly easy to compute — static storage allocation suffices. The nonlinear expressions may either be interpreted or, to gain some execution speed, converted to Fortran or C.

David M. Gay, [Correctly Rounded Binary-Decimal and Decimal-Binary Conversions](../REFS//rounding.pdf). Numerical Analysis Manuscript 90-10, AT&T Bell Laboratories, Murray Hill, NJ (1990).

Abstract:
> This note discusses the main issues in performing correctly rounded decimal-to-binary and binary-to-decimal conversions. It reviews recent work by Clinger and by Steele and White on these conversions and describes some efficiency enhancements. Computational experience with several kinds of arithmetic suggests that the average computational cost for correct rounding can be small for typical conversions. Source for conversion routines that support this claim is available from netlib.
