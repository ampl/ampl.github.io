# AMPL Options

The behavior of AMPL commands depends not only on what you type directly, but on a variety of
_options_ that determine the parameters of model and data processing, the choice of a solver, the
appearance of displayed results, and much else.

Each option has a name, and a value that may be a number or a character string. For
example, the option print_separator is a string that specifies a character to be written between
outputs of the print statement. The option display_width has a numeric value, which says
how many characters wide the output produced by the display command may be.

The option command displays and sets option values. If option is followed by a list of option
names, AMPL replies with their current values:

```ampl
ampl: option print_separator, display_width;
option print_separator ' ';
option display_width 79;
ampl:
```
A * in an option name is a “wild card” that matches any sequence of characters:

```ampl
ampl: option print*;
option print_precision 0;
option print_round '';
option print_separator ' ';
ampl:
```
The command option \*, or just option alone, lists all current options and values.

When option is followed by a name and a value, it resets the named option to the specified
value. In the following example we change the display width and the print separator, and then
verify that the latter has been changed:

```ampl
ampl: option display_width 60, print_separator ', ';
ampl: print {i in 1..5} i;
1, 2, 3, 4,  5 
ampl:
```
You can specify any string value by surrounding the string in matching quotes '...' or "..." as
above; the quotes may be omitted if the string looks like a name or number. Two consecutive
quotes alone ('' or "") denote an empty string, which is a meaningful value for some options. At
the other extreme, if you want to spread a long string over several lines, place the backslash
character \ at the end of each intermediate line.

When AMPL starts, it sets many options to initial, or default, values. The print_separator
option is initialized to ' ' (a space), for instance, so that by default the outputs of print are
space-separated. The display_width option has a default value of 79. Other options, especially
ones that pertain to particular solvers, are initially unset:

```ampl
ampl: option knitro_options;
option knitro_options ''; #not defined
```
To return all options to their default values, use the command reset options.

AMPL maintains no master list of valid options, but rather accepts any new option that you define.
Thus if you mis-type an option name, you will most likely define a new option by mistake, as the
following example demonstrates:

```ampl
ampl: option display_wdith 60;
ampl: option display_w*;
option display_wdith 60;
option display_width 79;
```
The option statement also doesn’t check to see if you have assigned a meaningful value to an
option. You will be informed of a value error only when an option is used by some subsequent
command. In these respects, AMPL options are much like the environment variables of your
operating system. In fact when AMPL starts, the current settings of environment variables are
used to define AMPL options with the same names, possibly overriding option defaults.

In the following listing, each option name is followed by a letter that indicates the kind of value
that is expected:

```
b 0 or 1
n integer
r any number
s character string
```

## Display Command Options

These options regulate output from the display command. They affect only the _formatting_ of the
display output; AMPL’s internal record of the displayed values or set members is not changed.

### display_1col n (default 20)

Whether to display params in one or multiple columns. The display is in one column when the
number of param values is less than or equal to _n_ , and is in multiple columns when the number of
param values is greater than _n_. (Specify _n_ as zero to force multiple columns, and as a very large
number to force one column.)

### display_eps r (default 0)

The smallest magnitude that should be displayed as nonzero. For example when _r_ is 0.00001,
both 0.000001 and –0.000001 are displayed as zero.

### display_max_2d_cols n (default 0)

The maximum number of columns in a multiple-column (2-dimensional) param display. If more
than _n_ columns are needed, the display is broken into tables of at most _n_ columns each. When _n_
has its default value of 0, there is no limit on the number of columns.

### display_precision n (default 6)

The maximum number of significant digits shown in displayed numbers. Values are rounded if
necessary, and trailing zeros after the decimal point are dropped; thus for example when _n_ is 6, the
value 12.3456789 is displayed as 12.3457, while 12.30001 is displayed as 12.3. Specify _n_ as 0 to
request full precision — the shortest representation that, when converted to binary and properly
rounded, will give exactly the binary value stored in the computer.

### display_round n (default "")

The number of digits shown relative to the decimal point in displayed numbers, overriding
**display_precision** when not null. For example 1234.5678 displays as 1234.57 when _n_ is 2,
as 1235 when _n_ is 0, and as 1200 when _n_ is –2.

### display_set_1col n (default 0)

Whether to display sets in one or multiple columns. The display is in one column when the
number of set members is less than or equal to _n_ , and is in multiple columns when the number of
set members is greater than _n_. (Specify _n_ as zero to force multiple columns, and as a very large
number to force one column.)

### display_transpose n (default 0)

Whether to transpose 2-dimensional tables. The displayed table is transposed if the number of
rows minus the number of columns is less than _n,_ and is not transposed if the number of rows
minus the number of columns is greater than or equal to _n._ (Specify _n_ as 0 to display all non-
square tables with more rows than columns. Specify _n_ as a large positive number for force
transposition, and as a large negative number to prevent transposition.)


### display_width n (default 79)

The maximum number of characters in each line of display output.

### gutter_width n (default 3)

The number of spaces between columns in display output.

### omit_zero_cols b (default 0)

Whether to omit columns that are all zeros. When _b_ is set to 1, only columns that have at least one
nonzero value are displayed. Values that are missing or that are less than **display_eps** in
magnitude are considered to be zeros for purposes of this option.

### omit_zero_rows b (default 0)

Whether to omit rows that are all zeros. When _b_ is set to 1, only rows that have at least one
nonzero value are displayed. Values that are missing or that are less than **display_eps** in
magnitude are considered to be zeros for purposes of this option.

## Other Formatting Options

These options regulate how numbers appear in various contexts. They affect only the _formatting_ of
numbers; AMPL’s internal record of the values is not changed. (For related options in the
display command, see **Display Command Options.** )

### csvdisplay_header b (default 1)

When to display a header line at the beginning out output from the csvdisplay command. Set _b_
to 0 to omit the header line.

### csvdisplay_precision n (default 0)

The number of significant digits in numerical values written by the csvdisplay and \_display
commands. Interpretation is the same as for **display_precision.**

### csvdisplay_restrict n (default "")

Whether the csvdisplay command issues an error message when asked to display multiple
tables. By default (or when _n_ is 0) any number of tables may be displayed. Set _n_ to 1 (detailed
error message) or 3 (one-line error message) to restrict the command to displaying one table.

### csvdisplay_round n (default "")

The number of digits shown relative to the decimal point in numerical values written by the
csvdisplay and \_display commands. Interpretation is the same as for display_round.

### expand_precision n (default 0)

The number of significant digits shown in numerical values written by the expand command.
Interpretation is the same as for **display_precision.**


### expand_round n (default "")

The number of digits shown relative to the decimal point in coefficients and constants in the
output of the expand command. Interpretation is the same as for display_round.

### format_range_errmsg s (default " ")

Out-of-range error indicator for formatted printing. If _s_ is a non-empty string, it appears as the
value of any %i, %d, %o, %u, %x, or %X format, in a printf command or sprintf invocation,
whenever the number to be formatted is outside the appropriate range of integers. When _s_ is left at
its default, an empty string, an error message appears and the command or function is aborted.

### MD_precision n (default 0)

The number of significant digits in numerical values written by AMPL’s -M and -D command-line
options. When model and/or data files are specified on the AMPL command line, -M requests a
listing of all model statements read, and -D requests a listing of all data statements read.
Interpretation is the same as for **display_precision.**

### print_precision n (default 0)

The number of significant digits in numerical values written by the print command.
Interpretation is the same as for **display_precision.**

### print_round n (default "")

The number of digits shown relative to the decimal point in numerical values written by the
print command. Interpretation is the same as for display_round.

### print_separator s (default " ")

The character string that separates values written on each line of print command output. The
default is one space character.

## Presolve Options

These options regulate the behavior of AMPL’s presolve phase, which attempts to reduce the size
of a problem instance before sending it to a solver. Presolve reductions include removing one-
variable inequalities that can be merged with variable bounds, and analyzing constraints (together
with variable bounds) to determine bounds that can be tightened, variables that can be fixed, and
constraints that can be dropped.

### constraint_drop_tol r (default 0)

Whether to change presolve behavior to avoid a subtle issue apparently caused by roundoff error.
A complete description is given in [https://www.netlib.org/ampl/fixlog](https://www.netlib.org/ampl/fixlog).

### infeas_clear n (default 1)

Whether to allow a solve or write command to proceed with sending a problem to the solver,
after presolve has determined that no feasible solution is possible:
```
0 never allow solve or write to proceed
1 allow a second solve or write to proceed, if typed at the command line
2 allow a second solve or write to proceed, under all circumstances
3 always allow a solve or write to proceed
```
Under the default setting of 1, when presolve determines infeasibility it displays a warning
message and does not send the problem to the solver; typing solve a second time overrides this
behavior and forces the problem to be sent to the solver, which makes its own determination of
infeasibility and may return additional information of interest. Specify 2 to use this feature also in
scripts, or 3 to force the problem to be sent to the solver under all circumstances.

### presolve n (default 10)

Maximum number of passes in AMPL’s presolve phase. A higher value of _n_ may reduce the size
of the problem instance sent to the solver, but may take more time. Set _n_ to 0 to turn off presolve.

### presolve_assoc n (default 7)

Whether to simplify constants in certain nonlinear contexts during presolve. Set to the sum of
```
1 to simplify using associativity of addition and subtraction
2 to simplify using associativity of multiplication and division
4 to simplify using distributivity of multiplication over addition and subtraction
```
By default all simplifications are turned on, and they should only be turned off in rare situations
where simplifying could affect numerical accuracy of the computations.

### presolve_eps r (default 0)

The presolve feasibility tolerance. Presolve reports infeasibility of a variable or constraint only
when its lower bound exceeds its upper bound by more than _r._

### presolve_epsmax r (default 1e-5)

The reporting threshold for **presolve_eps** changes. If setting **presolve_eps** to a higher value, but
not greater than _r,_ might change the results of presolve, then an appropriate warning message is
displayed. Set _r_ to **presolve_eps** to turn off all such messages.

### presolve_fixeps r (default 0)

The presolve fixing tolerance. When the upper and lower bounds of a variable or constraint differ
by less than _r,_ the variable or constraint is fixed at the average of the two bounds.

### presolve_fixepsmax r (default 1e-5)

The reporting threshold for **presolve_fixeps** changes. If setting **presolve_fixeps** to a higher value,
but not greater than _r,_ might change the results of presolve, then an appropriate warning message
is displayed. Set _r_ to **presolve_fixeps** to turn off all such messages.

### presolve_inteps r (default 1e-6)

The presolve integrality tolerance. When inferring bounds on integer variables, presolve subtracts
_r_ from the lower bound before rounding it up to the next higher integer, and adds _r_ to the upper
bound before rounding it down to the next lower integer.


### presolve_intepsmax r (default 1e-5)

The reporting threshold for **presolve_inteps** changes. If setting **presolve_inteps** to a higher value,
but not greater than _r,_ might change the results of presolve, then an appropriate warning message
is displayed. Set _r_ to **presolve_inteps** to turn off all such messages.

### presolve_logfile s (default "")

Destination for presolve log. When not null, _s_ specifies the name of a file to which a list of
presolve actions will be written. Specify >> at the beginning of _s_ to append the log to the named
file; otherwise if the file exists, it will be overwritten. Specify _s_ as the single character – to direct
the log to standard output (usually, the terminal window).

### presolve_warnings n (default 5)

The presolve message limit. Presolve displays at most _n_ separate messages such as infeasibility
warnings, and reports the number of additional messages suppressed.

### project_fixed_vars n (default 1)

How to handle a variable that is fixed to a value outside of its bounds. When _n_ is at its default
value of 1, presolve fixes the variable instead to its nearest bound. (Set _n_ to 2 to display a message
for each fixed variables that is “projected” in this way, until **presolve_warnings** such messages
have appeared.) When _n_ is 0, presolve changes the variable’s bounds to equal the value at which
the variable is fixed.

### show_presolve_messages b (default 1)

Whether to show presolve messages. Set _b_ to 0 to suppress the warning and error messages that
presolve normally displays when it finds a problem to be trivial or infeasible.

### var_bounds n (default 1)

Which presolve bounds on variables to send to the solver. Presolve computes two sets of bounds
on the variables, which may be tighter than the bounds declared in the model. The first set, chosen
when _n_ is 1, reflects bounds deduced from constraints that were eliminated by presolve. The
second set, chosen when _n_ is 2, also incorporates bounds deduced from constraints that presolve
did not eliminate; in general this set is even tighter the first, but may also produce more
degeneracy in the solutions. The optimal value is the same with either set, and solvers often run
faster with the first set (the default), but the second set is available for those who want to
experiment. After the presolve phase has run (usually as part of a solve), suffixes .lb1, .ub1
and .lb2, .ub2 on the variables give the bounds in the first and second sets, respectively,
while .lb, .ub give whichever bounds were sent to the solver.

## Solve Options

These options govern solve and related commands for sending problem instances to solvers.

### auxfiles s, (solver)_auxfiles s (default "")

List of auxiliary (additional) files of variable or constraint names, to be written when a problem
instance is generated. These files have names of the form _stub.ext,_ where _stub_ matches the name of
the problem ( _stub_ .nl) and solution ( _stub_ .sol) files that AMPL uses for communicating with the
solver. Each letter in _s_ specifies a content of the file and choice of _ext,_ as follows:
```
a .adj constant added to objective values
c .col AMPL names of variables the solver sees
e .env environment (written by a solve command)
f .fix variables eliminated from the problem because their values are known
p .spc MINOS ‘‘specs’’ file for output style m
r .row AMPL names of constraints and objectives the solver sees
s .slc constraints eliminated from the problem
u .unv unused variables
```
Option ``auxfiles`` affects the subsequent ``write`` command.
Option ``(solver)_auxfiles`` affects the subsequent ``solve;`` using that ``(solver)``.


### dual_initial_guesses b (default 1)

Whether to send to the solver the current dual values for the constraints. Dual values are sent when
_b_ is at its default value of 1, and are not sent if _b_ is set to 0. Dual values can be useful in
initializing certain algorithms, but each solver makes its own determination as to how and whether
the values are used.

### linelim b (default 1)

How to handle defined variables whose defining expression is a linear function of other variables.
When _b_ is at its default value of 1, such variables are eliminated from the problem by substitution;
this may make the problem denser, but it allows the variables in the defining expression to be seen
by the solver as linear. When _b_ is set to 0, this special handling of linear defined variables is
turned off, and all of the variables in any defining expression are seen by the solver as nonlinear.

### nl_comments b (default 0)

Whether to add comments to the problem files that AMPL writes for solvers. When a command of
the form write g _stub_ ; is executed, when _stub_ is some valid filename, AMPL writes a description
of the currently defined optimization problem to a text file _stub_ .nl. When _b_ is set to 1,
informational comments are included in the file. This feature is mainly useful for writing and
debugging solver interfaces.

### nl_permute n (default 3)

Whether to permute variables and constraints so that solvers see the nonlinear ones first. Some
solvers require this, but with other solvers, occasionally it is useful to suppress these permutations
by setting _n_ to the sum of
```
1 to permute constraints
2 to permute variables
4 to permute objectives
```
By default the constraints and variables are permuted.

### outopt s (default "")

Argument to the write command, which creates an AMPL problem (.nl) file but does not
invoke a solver. When a write command is given, without any argument, it is interpreted as
write _s_. When a write command is given with an argument string, that string is assigned to _s_.


### output_precision n (default 0)

The maximum number of significant digits that AMPL uses to represent numbers in the problem
file that AMPL writes for solvers. The interpretation of _n_ is as for **display_precision**. The default
value requests full precision — the shortest representation that, when converted to binary and
properly rounded, will give exactly the binary value stored in the computer.

### pl_bigM r (default 1e6)

Large constant used in linearizing an AMPL piecewise-linear function of a variable. The
linearization normally assumes that the variable’s value will lie between the smallest breakpoint
minus _r_ , and the largest breakpoint plus _r_. The constant is adjusted to a larger value, however, in
special cases: where a breakpoint has a magnitude > _r_ /2, or the variable has been defined with a
bound that has a magnitude > r.

### pl_linearize b (default 1)

Whether to replace each appearance of the AMPL piecewise-linear operator <<...;...>> by
equivalent linear expressions. When _b_ is at its default value of 1, all piecewise-linear operators are
linearized; variables and constraints must be added for this purpose, and in nonconvex cases some
of the variables must be binary. When _b_ is set to 0, piecewise-linear operators are treated as
nonlinear expressions, which are sent to the interface for the chosen solver, and are handled (or
rejected) according to the features that the solver provides.

### relax_integrality b (default 0)

Whether to relax the integrality of variables in the problem. When _b_ is set to 1, then in the problem
that is sent to the solver, integer variables are converted to continuous variables, and binary
variables are converted to continuous variables with lower bound 0 and upper bound 1. With _b_ at
its default value of 0, all integer and binary variable definitions are honored.

### reset_initial_guesses b (default 0)

Whether to send to the solver the current values of the variables. Values are sent when _b_ is at its
default value of 0, and are reset to the initial values specified in the model if _b_ is set to 1. Current
values can be useful in initializing certain algorithms, but each solver makes its own determination
as to how and whether the values are used.

### send_statuses b (default 1)

Whether to send simplex basis status information to the solver. Values of the .sstatus suffix for
variables and constraints are sent to the solver when _b_ is at its default value of 1, but are not sent
when _b_ is set to 0. When a solver applies the simplex method, it returns statuses as part of the
optimal solution; these can provide a good start for a subsequent solve.

### send_suffixes n (default 3)

Whether to send or receive suffix values when running solvers:
```
0 do not sent or receive suffix values
1 only send suffix values to the solver
2 only receive suffix values from the solver
3 both send and receive suffix values (the default)
```
Suffix values are sent along with the optimization problem when a solve begins, and are returned
along with the solution when a solve is completed.

### solver s

The name of the solver to be invoked. The solve command attempts to start a program named _s,_
normally a “solver” that reads a problem file, computes a solution, and writes a solution file for
AMPL to process. If _s_ is not a fully qualified filename, AMPL attempts to find it using the system
search path.

### substout b (default 0)

Whether to communicate certain constraints as defined variables rather than as explicit constraints.
When _b_ is set to 1, AMPL scans the constraints in the order of their appearance in the model, and
constraints of the form _variable = expression_ are converted to defined variables if the _variable_ ’s
definition imposed no restrictions on it (such as integrality or bounds) and the _variable_ has not
appeared in any previous such constraint. Defined variables are normally communicated to solvers
in the form of nonlinear subexpressions, but **linelim** can be set to eliminate linear defined
variables by direct substitution instead.

## Solve Message Options

These options regulate error, warning, informational, and diagnostic messages associated with
solving optimization problems.

### bad_subscripts n (default 3)

Limit on number of invalid subscript combinations reported. An AMPL data statement may
specify values that correspond to illegal index (subscript) combinations, due to mistakes such as
incorrect index sets in the model, indices in the wrong order, misuse of (tr), and typing errors;
similar errors may be caused by assignment (let) statements that change the membership of index
sets. AMPL catches these when processing a solve or other command that causes a problem
instance to be generated. The number of invalid combinations displayed is limited to _n_.

### compl_warn n (default 1)

Whether to warn of non-square systems of complementarity constraints. When some of a model’s
constraints use the complements operator, they are considered to form a “square”
complementarity system when the number of _inequality_ complements _inequality_ constraints plus
the number of equations equals the number of variables. Some complementarity solvers require
square systems, so by default AMPL warns about nonsquare systems. Set _n_ to 2 to also regard
nonsquare complementarity systems as infeasible. To turn off all complementarity warnings, set _n_
to 0.

### gentimes b (default 0)

Whether to display detailed time and memory statistics for generating individual AMPL model
components. Set _b_ to 1 to see statistics for all sets, parameters, variables, objectives, and
constraints. This option can be useful in locating model components that are taking AMPL large
amounts of time or memory to generate.


### show_stats n (default 0)

Whether to display statistics of the current problem instance. Set _n_ to 1 to display a summary of
presolve activities and counts of variables, constraints, and nonzeros. Set _n_ to 2 to request
additional information about the presolve run.

### show_write_files n (default 0)

Whether the write command reports the name of the file it writes:
```
0 no
1 yes if the file is specified indirectly though the setting of "outopt"
2 yes in all cases
```
### solver_msg b (default 1)

Whether to show the solver’s brief message summarizing its results. Change _b_ to 0 to suppress the
message.

### strict_ineq_warn n (default 1)

How to handle > and < constraints. Algebraic constraints that use > or < as their comparison
operator (rather than ≥ or ≤ or =) cannot be handled by many popular solvers. When _n_ has its
default value of 1, AMPL prints a warning message and represents the constraint in its problem
file as a “logical constraint” that a few solvers can accept. Set _n_ to 0 to suppress the warning
message, and to 2 to print an error message and reject the constraint.

### times b (default 0)

Whether to display detailed time and memory statistics for the major AMPL execution phases. Set
_b_ to 1 to see statistics for all subsequent AMPL commands. This option can be useful in locating
steps where AMPL is taking large amounts of time or memory.

## Result Options

These options relate to optimal solutions and other results received from solvers.

### abs_boundtol r1 (default 0)

### rel_boundtol r1 (default 0)

Tolerances for whether a constraint eliminated by presolve should be considered active (tight) in
an optimal solution, when deducing dual values. Each AMPL constraint is sent to the solver in the
form _lb_ ≤ _body_ ≤ _ub,_ where _lb_ and ub are constants and _body_ contains the variables. The _lb_ ≤ _body_
inequality is considered tight if

_body_ – _lb_ ≤ 0 or

_body_ – _lb_ < _ub_ – _body_ and _body_ – _lb_ ≤ max (r1, abs( _lb_ )*r2)

Similarly the _body <= ub_ inequality is considered tight if

_ub_ – _body_ ≤ 0 or

_ub_ – _body < body_ – _lb_ and _ub_ – _body_ ≤ max (r1, abs( _ub_ )*r2)

These tests only apply to constraints that were eliminated by AMPL’s presolve phase; since
eliminated constraints are not sent to the solver, no dual values are received from the solver for
them, and hence AMPL must deduce dual values through computations that are sensitive to
whether such constraints are considered tight.

### boundtol_max r (default 1e-5)

### show_boundtol b (default 1)

Whether to report changes to **abs_boundtol** or **rel_boundtol** that would affect the deduced dual
values of constraints eliminated by presolve. When _b_ is at its default value of 1, changes are
reported if they involve an **abs_boundtol** or **rel_boundtol** of at most _r._ Set _b_ to 0 to turn off all
reporting of such changes.

### objective_precision n (default 10)

The maximum number of significant digits shown in the objective value reported by the solver’s
result message. The interpretation of n is the same as for display_precision.

### rel_boundtol r (default 0)

Relative tolerance for whether a constraint eliminated by presolve should be considered active
(tight) in an optimal solution, when deducing dual values. Details are given in the entry for
**abs_boundtol.**

### show_boundtol b (default 1)

Whether to report changes to **abs_boundtol** or **rel_boundtol** that would affect the deduced dual
values of constraints eliminated by presolve. Details are given in the entry for **boundtol_max.**

### solution_precision n (default "")

The maximum number of significant digits in solution values returned by solvers. When primal
and dual variable values are returned by the solver, they are rounded to _n_ significant digits before
being recorded in AMPL. When this option is left at its default value (an empty string), values
returned by the solver are recorded unchanged in AMPL. (Unlike other “_precision” options, this
one affects the values that are stored in AMPL and used for all subsequent operations. To change
only the number of significant digits displayed or written, use **display_precision** and similar
options instead.)

### solution_round n (default "")

The number of digits relative to the decimal point in solution values returned by solvers,
overriding **solution_precision** when not null. When primal and dual variable values are returned
by the solver, they are rounded at the _nth_ digit after the decimal place (for _n_ ≥ 0) or the - _nth_ digit
before the decimal place (for _n_ < 0) before being recorded in AMPL. When this option is left at its
default value (an empty string), it has no effect. (Unlike other “_round” options, this one affects
the values that are stored in AMPL and used for all subsequent operations. To change only the
number of digits displayed or written, use display_round and similar options instead.)

## Execution Options

These options relate to AMPL’s execution of scripts, solvers, and external commands.


### allow_NaN b (default 0)

How to handle numerical evaluation errors (such as division by 0 or log of a negative number) that
occur in AMPL. When _b_ is at its default value of 0, an evaluation error results in an error message.
When _b_ is set to 1, an evaluation error causes the return of a special floating-point value that does
not correspond to any valid number; when displayed, this value is represented as NaN (“not a
number”). The setting of this option does not affect how numerical errors are handled in solvers.

### ampl_include s (default ".")

Directory (or folder) where AMPL looks for files referenced in model, data, include, and
commands commands. AMPL interprets _s_ as a fully qualified path or as a path relative to the
current directory, according to the rules of the operating system; the default value. causes files to
be sought in the current directory, which is typically the user’s AMPL directory. (Setting this
option does not change the current directory; AMPL’s cd command can be used instead for that
purpose.)

### Cautions n (default 1)

How to handle caution messages. Leaving _n_ at its default value of 1 displays all caution messages.
Set _n_ to 0 to suppress caution messages; set _n_ to 2 to treat cautions as errors.

### cmdtrace b (default 0)

Whether to display command trace information. When _b_ is set to 1, AMPL displays the name of
each command executed and, when the command comes from a file, the filename and line number
of the command.

### eexit n (default -10)

Number of statement error messages or presolve warnings to show. Set _n_ < 0 to terminate the
current statement after - _n_ messages, or set _n_ > 0 to terminate the AMPL session after _n_ messages.
When _n_ is set to 0, all of a statement’s error messages and all presolve warnings are displayed.

### shell_exitcode_max n (default 65536)

Threshold shell_exitcode value for aborting compound commands. When the AMPL shell
command is invoked to run an operating system command from within AMPL, the exit code of the
operating system command is returned as a nonnegative number in the built-in parameter
shell_exitcode, typically 0 if the command was successful, or some positive value if
unsuccessful. If the returned shell_exitcode value is > _n,_ any currently executing compound
commands (include, commands, repeat, for, if) are aborted. The default value of _n_ (equal
to 216 ) allows currently executing compound commands to continue in most circumstances.

### shell_exitignore n (default 0)

Threshold value for suppressing the “exit code _e_ ” message displayed by the AMPL shell
command. If _e_ < _n_ , the message is suppressed. When _n_ is at its default value of 0, all such
messages are suppressed.

### single_step n (default 0)

Whether to run scripts in single-step mode, which automatically returns control to the command
prompt after execution of specified commands. Single-step mode begins immediately when _n_ is
set to a positive value, and continues until _n_ is set back to 0. Any command may be typed at the
prompt, and execution may be advanced by one or more statements in the script by typing step,
skip, next, cont, and end commands. (In most circumstances, _n_ should be set to 1 to turn on
single-step mode; but where there is nesting of data and commands commands specifying files
and appearing within a compound command, single-step mode applies only to commands at insert
level _n_ or less.)

### single_step_cmdno n (default 0)

Command number at which to turn on single-step mode. AMPL sets **single_step** to 1 after _n_
commands have been executed in the current session.

### solve_exitcode_max n (default 0)

Threshold solve_exitcode value for aborting compound commands. A solver run returns a
nonnegative number in the built-in parameter solve_exitcode, either 0 if the run was
successful, or some positive value if unsuccessful. If the returned solve_exitcode value is > _n,_
any currently executing compound commands (include, commands, repeat, for, if) are
aborted. In particular, when _n_ is at its default value of 0, a failed solver run aborts any currently
executing compound commands.

### stdin_offset b (default 0)

Whether to report input offset and command number in error messages for commands, when
commands are being read from the standard input. To request this information set _b_ to 1.

## File Options

These options identify and regulate various library, log, option, and temporary files that AMPL
reads and writes.

### log_data b (default 0)

Whether statements read in data mode are echoed to the AMPL log file. Most commonly, these are
statements read from AMPL data files by data commands. Set _b_ to 1 to request that these
statements appear in the file specified by the log_file option.

### log_file s (default "")

Name of a log file, to which subsequent AMPL commands and responses to commands are
written. AMPL does not log statements that it reads from included files (by use of model, data,
or include statements), unless the **log_model** and/or **log_data** option is also set accordingly.
When _s_ is left at its default setting, an empty string, no file is written.

### log_model b (default 0)

Whether statements read in model mode are echoed to the AMPL log file. Most commonly, these
are statements read from AMPL model files by model commands, and statements read from
AMPL scripts by include commands. Set _b_ to 1 to request that these statements appear in the file
specified by the log_file option.


### OPTIONS_IN s (default "")

Name of a option setting file that AMPL reads and executes at startup. For this option to have an
effect, a system environment variable named OPTIONS_IN must be defined and set to a non-
empty string _s_ before AMPL is started. (Environment variables are read by AMPL at startup and
assigned to corresponding AMPL options.) The intention is for this file to contain AMPL option
statements, although any AMPL statements in the file will be read and executed.

### OPTIONS_INOUT s (default "")

Name of an option setting file that AMPL reads and executes at startup, and writes at shutdown.
For this option to have an effect on startup, a system environment variable named
OPTIONS_INOUT must be defined and set to a non-empty string _s_ before AMPL is started.
(Environment variables are read by AMPL at startup and assigned to corresponding AMPL
options.) At shutdown, if _s_ is nonempty, a list of option commands specifying the current option
values is written to file _s_. In normal use, the environment variable OPTIONS_INOUT is set once,
and no changes are made to the file or to the value of **OPTIONS_INOUT** during an AMPL
session; consequently, all options are set at the beginning of each AMPL session to the values that
they had at the end of the previous session. The file _s_ is read after any file specified by
**OPTIONS_IN** and before any file specified by **OPTIONS_OUT**.

### OPTIONS_OUT s (default "")

Name of an option setting file that AMPL writes at shutdown. If _s_ is nonempty, a list of option
commands specifying the current option values is written to the specified file.

### shell_env_file s (default "")

Name of a file to which a list of current AMPL options and their values is written before execution
of an AMPL shell command. When _s_ is left at its default setting, an empty string, no file is
written.

### TMPDIR s (default "")

Location to which AMPL’s temporary problem (.nl) and solution (.sol) files are written. String
_s_ must represent a folder or directory name in a format appropriate to the operating system; it may
be fully qualified or relative to the current folder (directory). When _s_ has its default value, an
empty string, the system’s default choice of temporary location is used.

## Library Options

These options relate to external function libraries, and user-defined AMPL functions that are
imported from them.

### AMPLFUNC s (default "")

### ampl_funclibs s (default -)

Names of external AMPL function libraries currently in use. This option is normally set
automatically.


### ampl_libpath s

Directory/folder in which AMPL looks for external function libraries. This option is normally set
automatically.

### libmap_32_64 b (default 1)

How libraries are handled when there are 32-bit and 64-bit variants.

### load_funcdcl n (default 0)

When imported functions are implicitly declared:
```
0 when their library is loaded
1 when an imported function makes another imported function available
2 like 1, with a report of the declaration.
```
## Prompt Options

These options change the prompts that AMPL displays in various contexts, when run in interactive
mode. Normally they are not changed by the user.

### cmdprompt1 s (default "%s ampl: ")

### cmdprompt2 s (default "%s ampl? ")

### dataprompt1 s (default "ampl data: ")

### dataprompt2 s (default "ampl data? ")

### insertprompt s (default "<%d>")

### prompt1 s (default "ampl: ")

### prompt2 s (default "ampl? ")

## Miscellaneous Options

### convert_logical_to_algebraic b (default 1)

Whether constraints that appear to be logical constraints because they are surrounded by
parentheses, but that would be recognized as algebraic constraints without the surrounding
parentheses, should be converted to algebraic constraints during parsing. By default, the
conversion is made; change _b_ to 0 to turn off the conversion.

### integer_markers b (default 1)

Whether to mark integer variables in MPS files created by AMPL’s write command. When _b_ is
left at its default value of 1, 'MARKER' 'INTORG' and 'MARKER' 'INTEND' lines delimit the
variables that are constrained to be integer. Set _b_ to 0 to omit these lines, converting the problem
to its continuous relaxation.


### lazy b (default 0)

Whether to treat = (or :=) in a param statement as equivalent to default, so that values are
computed only as needed. Set _b_ to 1 to turn on this feature.

### mpsfile_numwidth n (default 12)

Width of numeric fields in MPS files created by AMPL’s write command. When an MPS-format
problem file is written with an AMPL command of the form write m _stub_ , numbers in the file are
rounded if necessary to fit into fields of _n_ characters. The default requests 12-character fields as
specified in the original MPS standard.

### outarg_warn b (default 1)

Whether to warn of unexpected behavior of output arguments of imported functions.

### randparam_warn b (default 1)

Whether to display a warning message when a param statement specifies random. Set _b_ to 0 to
suppress this message.

### randseed n (default 1)

Seed value for AMPL’s random number generator. Each value of _n_ ≠ 0 gives a particular sequence
of random values. Set _n_ to 0 to request a random seed based on the system clock and to report the
chosen seed; for all practical purposes, the seed chosen in this way will be different every time.
Using an option command to set _n_ (even to its current value) causes the random number
sequence to be restarted.

### table_debug n (default "")

### table_debug_template s (default "%.dbtab")

Instructions for writing and reading AMPL text-format database tables, for use in debugging
table statements. A complete description is given in [https://www.netlib.org/ampl/fixlog](https://www.netlib.org/ampl/fixlog).

### table_errbreak n (default 0)

How read table and write table commands handle errors. When _n_ has its default value of 0,
on error these commands report the issue and immediately terminate processing. Values 1 ≤ _n_
≤ 3 are interpreted as the sum of the following:
```
1 suppress error reporting for write table
2 suppress error reporting for read table
```
Setting _n_ to 4 works like 0, except that, when read table or write table is iterated over a
set, errors are reported for all iterations before terminating.

### version s

Version description of the AMPL process currently running. At AMPL startup, _s_ is a string
indicating the build date along with platform and license information.
