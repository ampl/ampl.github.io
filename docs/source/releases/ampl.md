# AMPL Changelog

## 20231012

* Fix a glitch in reading values in solution (.sol) files for suffixes on logical constraints.

* Fix a bug with a new problem after solving a problem with a "var ... in set_expr" declaration when the new problem does not involve that variable.  Constraints and variables used to implement the "in set_expr" phrase were erroneously included in the new problem.

## 20230918

* Fix a fault with reading suffix values in a data section.  Example:
```
	var x{i in 1 .. 2};
	minimize zot{j in 1 .. 3} : sum{i in 1 .. 2} (x[i] - (i + j))^2;
	data;
	param: x.sstatus_num :=
		1 2;
	var x :=
	 1 2
	 2 3;
```

* Fix a fault simplifying logical expressions involving <==>.  The bug only bit when the <==> had to be retained but its right-hand side could be simplified.

* Make the $AMPLFUNC found at startup the $$AMPLFUNC value, so it survives a "reset option;" command.

* New debugging option -w causes AMPL to give return code 0 when exiting after producing various error messages.

* Fix a glitch (fault) illustrated by
```
	var x{i in 1..2} integer := i;
	c: x[1] < x[2]; # logical constraint
	print c; #faulted
```
Note that if c is a logical constraint, then c.val and c should be treated alike, but changing "print c;" to "print c.val;" in the above example avoided the fault.

* When 'e' appears in ($solver & '_auxfiles'), so that a .env file containing the current environment is written by the solve command, remove the .env file at the end of the solve, like other temporary files, such as the .nl file.  When 'e' appears in $auxfiles, have the write command write a .env file.

## 20230816

* Fix a couple of bugs with debugging options -G and -O.  (If you do not know what they do, you do not need them.)

* Fix a rarely seen memory-overwrite bug with multiple declared problems.

## 20230516

* Fix bugs introduced 20230426 in some "let" statements for an entity declared with a side condition, such as a >= expression.

## 20230430

* Change the error message for
```
    display intersection{i in 1 .. 0} {i};
```
from "empty iterated intersection" to "empty iterator in iterated intersection".

* Make integer[1,10] equivalent to 1..10 instead of (erroneously) giving an error message.

* Fix a possible fault with "display _var;" on some systems. (If it does not fault, then there is not a problem here.)

* Fix a little off-by-one formatting bug in displaying some numeric values, as in
```
        display {a in 0..1, b in 0..1} (a, b, if a and b then 1 else 0);
```
which gave
```
:      a     b   if a && b then 1    :=
0 0   0     0            0
0 1   0     1            0
1 0   1     0            0
1 1   1     1            1
;
```
rather than
```
:     a   b  if a && b then 1    :=
0 0   0   0          0
0 1   0   1          0
1 0   1   0          0
1 1   1   1          1
;
```

* Fix a bug in generated names for piecewise-linear terms and unions
of intervals: when more than one set of constraints was generated,
the same names were used. Now the generation number is appended,
except for the first set. Also, change the character separating
components of generated names from '+' to '@'.  Example:
```
        set S := 1 .. 2; var x{S};
        minimize zot: sum{i in S} <<i;-1,1>> x[i];
        solexpand;
```
produced
```
        minimize zot:
                -(zot+x[1]+s)[0] + (zot+x[1]+s)[1] - (zot+x[2]+s)[0]
                + (zot+x[2]+s)[1];
```

Now it produces
```
        minimize zot:
                -(zot@x[1]@s)[0] + (zot@x[1]@s)[1] - (zot@x[2]@s_2)[0] +
                (zot@x[2]@s_2)[1];
```

* Fix trouble with ord(a), next(a), and prev(a) when a runs over a subscripted set with subscripts involving dummy variables of a "for"
loop. Example:
```
        set A; set B{A} ordered;
        data; set A := a b;
        set B[a] := c d;
        set B[b] := e f;
        for{a in A, b in B[a]} print a, b, ord(b); #faulted
```

* New logical function alldistinct(...), true when ... are all different sets and false otherwise. Order is ignored, so alldistinct({'a','b'}, {'b','a'}) is false.  New logical function alldisjoint(...) is true if ... are all disjoint sets and false otherwise.


* Fix a bug that prevented suffixes on logical constraints from being conveyed to the .nl file (except in the special case of no algebraic constraints, in which case the first suffix on a logical constraint was conveyed).

* Only print one "not within" error message (instead possibly of several).  Example:
```
        set S; set A;
        set B{S} within A;
        data; set S := a b;
        set A := d e f g;
        set B[a] := h i;
        set B[b] := k l;
        display B;
```

## 20230124

  Show error context in blockmode (invocations of "`ampl -b ...`").

## 20221013

  Fix a bug, introduced in version 20220505, in handling data sections.
  Example:
```ampl
set A := 1..2; param p{A}; param q{A};
data;
param: p q :=
[*] 1 2.5 3	# erroneously complained about "."
    2 4 5.6;
display p, q;
```

## 20221008
  Fix a configuration bug in the 64-bit ARM binary that caused a wrong
value for some things, such as `Normal01()`, to be computed.  With
today's 64-bit ARM binary, "`ampl -vvq`" will report version 20221008.


## 20220927
  Fix error a couple of error messages caused by inappropriate uses
of variables.  Previously the (silly) example

```ampl
var x >= 0 integer; var y >= 0 integer;
subj to con: x + y in {0,3,5};
solve;
```

got the surprising error message

```
presolve, constraint con:
    Logical constraint is always false.
Infeasible constraints determined by presolve.
```

Now the second line elicits the error message

```
Cannot test whether a variable expression is in a set expression.
context:  subj to con: x + y in  >>> {0,3,5}; <<< 
```

This example can be restated as

```ampl
var x >= 0 integer; var y >= 0 integer;
var z in {0,3,5};
s.t. con: x + y == z;
```

Previously the second line of the little example

```ampl
var x >= 0;
subj to con: x in {0,3,5};
```

elicited the surprising error message

```text
continuous variable in tuple
context:  subj to con: x in  >>> {0,3,5}; <<< 
```

Not it gets

```text
Cannot test whether a variable is in a set expression.
context:  subj to con: x in  >>> {0,3,5}; <<< 
```

The example can be rewritten (without complaint) as

```ampl
var x in {0,3,5};
```

For a "`var x in set_expr`" declaration, AMPL quietly generates binary
variables related by an SOS1 condition and a constraint defining x.


## 20220812

Fix a bug in the changes of 20220730 that caused a fault with some uses of defined variables -- only when the changes of 20220730 were relevant.

## 20220730

Fix a bug with defined variables: if a defined variable used a problem variable nonlinearly, another defined variable used the first one linearly, no other use was made of the problem variable, and the second defined variable was used nonlinearly, then derivatives with respect to the problem variable were not computed. Example: 
```ampl
set I = 1..3; var x{i in I} := i;  
var v1 = x[1] + x[2]^2;  
var v2 = v1 + x[3]^3;
minimize obj: v2^2;
```
Derivatives with respect to `x[2]` were not computed because of an error in the .nl file.

## 20220703

Fix a glitch introduced in version 20220505: in data sections, an unquoted "-" in the subscript of a subscripted set gave an error message. Example: 
```ampl
set S; set T{S}; data;  
set S := 2022-06-26_03;  
set T[2022-06-26_03] := a b c;  
display T;
```
Changing the third line to  
```ampl
set T['2022-06-26_03'] := a b c;
```
was a work-around.

## 20220621

Fix a glitch with console input: if the cursor is at the start of the current line (perhaps because of pressing the HOME key), the DELETE key did nothing.  
  
Increase the longest line that can be recalled correctly with history and the up and down arrow keys from 1000 to 4000 characters.

## 20220506

In data sections, when x is a variable, treat x.val as x when x does not yet have a current value, and similarly for c and c.dual when c is a constraint.  
  
In the little example 
```ampl 
var x; data; var x.dual := 3;  
```
change the error message from "dual is not a suffix" to "dual is not an assignable suffix." (When x is a defined variable, declared with "`var x = expression;`", x.dual is the value of the dual variable for the implied constraint "x = expression". Defined variables are substituted out of the problem, so the solver does not see them, but sometimes it is desirable to see dual variable values for them.)

## 20220505

Fix a bug in the "`show`" command, which did not print default (dual) values for constraints. Example:
```ampl  
var x; s.t. cx default 1: x <= 4;  
show cx;
```
Allow suffixes (on variables, constraints, objectives, problems) to appear in data sections. As usual for data sections, the name of a constraint, objective, or problem can be introduced with "param" or "var". For example,
```ampl
var x;  
minimize o: (x-3)^2;  
suffix foo;  
data;  
var o.foo 3.2; # or "var o := 3.2"; the ":=" is optional here.  
# or "param o.foo 3.2", etc.  
```
This is meant to make "snapshots" more efficient; there is no checking whether suffix values are replaced.  
  
When `"option show_write_files 2"` is specified and no variables remain used after presolve, print "# No .nl file written: no variables used."  

Quietly reduce absurdly large precisions in printf formats. For example, `"%.410g"` faulted. Now it works and `"%.500g"` is quietly reduced to `"%.415g"`.

## 20220323

Make option `bad_subscripts` apply in more cases. For example,
```ampl
set S; var x{S}; data; set S := a b;  
var x := b 2.1 a 1.1 c 3.1; display x;
```
now gives  
```text
Error executing "display" command:  
error processing var x:  
          invalid subscript x['c'] discarded.  
x [*] :=  
a 1.1  
b 2.1  
;
```
Inserting `"option bad_subscripts 0;"` before the display command suppresses the error message. The default `$bad_subscripts` is still 3.  
  
Fix a bug in displaying several items indexed over a cross-product of sets, some ordered, some not. A fault was sometimes possible. Example:  
```ampl
set A ordered; set B;  
param x{A, B};  
param y{A, A};  
data; set A := 1; set B := 0;  
param x 1 0 1.1; param y 1 1 2.2;  
display x, y; # The 64-bit binaries faulted; 32-bit did not,  
# nor did "display y, x;".
```

## 20220310

Fix more error-message bugs. If foo1 said "`include foo2`" and foo2 said "`model diet.mod data diet.dat`" and the current directory contained diet.mod but not diet.dat, then invoking ampl and typing "`include foo1`" gave a fault. After changing foo2 by moving "`data diet.dat`" to a second line, invoking ampl and typing "`include foo1`" gave
```text
foo2, line 2 (offset 159431244):  
     Can't find file "diet.dat"  
context: data >>> diet.dat <<< ;  
       
include stack...  
     -, line 1 includes  
     foo1, line 1 includes  
     foo2  
```
with an erroneous offset.


## 20220224

Fix an off-by-one error in line numbers on some error messages. For example, if "foo1" said "`include foo2`", foo2 said "`model diet.mod`" and the current directory did not have a file named diet.mod, then invoking ampl and typing "`include foo1`" gave
```text
foo2, line 1 (offset 6):  
     Can't find file "diet.mod"  
context: model >>> diet.mod <<<  

include stack...  
    -, line 0 includes  
      foo1, line 0 includes  
      foo2
```
rather than
```text
foo2, line 1 (offset 6):  
     Can't find file "diet.mod"  
context: model >>> diet.mod <<<  
  
include stack...  
     -, line 1 includes  
     foo1, line 1 includes  
     foo2
```  

## 20220219

Fix a bug with "`data filename;`" in a compound statement. If a second such statement appeared in the compound statement with the same filename after the file was recreated after the first "`data filename;`", wrong data was read unless an explicit "`close filename;`" appeared before the file was recreated. Example (under Linux):
```ampl
set A;  
if (1 < 2) then {  
     shell 'echo "set A := a b c;"' >foo;  
     data foo  
     # close foo; # uncomment to bypass bug  
     display A;  
     shell 'echo "set A := x y z;"' >foo;  
     update data A;  
     data foo  
     display A;  
     }
```
For MS Windows, it is necessary to omit the double quotes in the shell commands and to add "`close foo;`" immediately after them. Then the example runs correctly.  
Fix an obscure fault with an input file without a final newline that is directly accessed by "include" at the command prompt. For example, if file foo contains just "param/" without a newline character, then "ampl foo" correctly said
```text
foo, line 1 (offset 5):  
     unexpected end of file  
context: >>> / <<<
```
but (in an interactive AMPL session)
```ampl
ampl: include foo
```
faulted.  

## 20220119

Restore some error-handling behavior prior to 20220110. The changes of 20220110 sometimes resulted in several error messages per statement.  
Fix a parsing bug in error handling (infinite loop, introduced 20220110) seen with
```ampl
set A dimen 2; data; set A := (1,a) (2,b);  
for{i in 1..2}  
    for{j in {'a','b'}}  
        print {k in U[j]} i,j,k; # U was not declared
```

## 20220110

Fix a rarely seen bug with deducing bounds on variables, illustrated by
```ampl
var x >= 0; display x.ub; # correctly showed x.ub = Infinity  
var y = max{i in {0}} x;# logically the same as "var y = x;"  
display x.ub;# incorrectly showed x.ub = 0
```
Specifying `"option presolve 0;"` bypassed the bug. Fix a bug with handling certain errors. Example:
```ampl
ampl: param p {i in 1..10} := j;  
   
j is not defined  
context: param p {i in 1..10} := >>> j; <<<  
ampl: redeclare param p {i in 1..10} := i;  
Ignoring redeclaration of p:  
    system parameters may not be redeclared.  
context: redeclare param p {i in 1..10} := >>> i; <<<  
ampl: display p;  
Segmentation fault (core dumped)  
```
Fix a bug with redeclare:
```ampl
set X; data; set X := 1;  
redeclare set X ordered;  
update data X; data; set X := 1 2; # faulted
```

## 20211222

After an error message "variable in ...", replace the whole expression in question by a constant (that can be seen with a "show" command). Previously the example  
     var a := 12; set S := 4 .. a;  
     display S;  
(if entered interactively) gave different results on different kinds of machines. Now "display S;" should give "set S := ; # empty" and "show S;" should give "set S = 4 .. 0;".

## 20210906

Fix a bug with suffixes: if the suffixed entity had not yet been instantiated, a fault was possible. Example:  
     var x{i in 1..2} := i;  
     var y{1..2};  
     s.t. c: sum{i in 1..2} x\[i\].val \* y\[i\] >= 3;  
     expand c; # faulted; workaround: "display x;" before "expand c;"  
Change to when an entity is instantiated: if the entity depends on suffix values, changes to those values no longer cause the entity to be instantiated anew. In the above example, adding  
     let x\[1\] := 1.5;  
     expand c;  
will give the same constraint as before -- the change to x\[1\] == x\[1\].val does not cause c to be reinstantiated. This change is partly to facilitate scripts that add cutting planes. It is also necessary for consistency with a forthcoming new implementation of AMPL (that supports functions in AMPL, among other things). AMPL has facilities for causing entities to be reinstantiated when declared prerequisites change. For example, changing the above example to use a named parameter for the coefficients of c will cause c to be reinstantiated when the parameter values change:  
     param p{1..2};  
     redeclare s.t. c: sum{i in 1..2} p\[i\]\*y\[i\] >= 3;  
     let {i in 1..2} p\[i\] := x\[i\];  
     expand c;  
     let p\[1\] := x\[1\] + 2;  
     expand c;

## 20210810

Fix a bug with split defined variables (where the linear part is sometimes handled separately) introduced in version 20190824. An example on which the bug caused a fault:  
     var x := 1;  
     var y = 2\*x + x^2;  
     c: x + y >= 1 complements sin(y) <= .5;  
Fix a bug that, under complicated conditions, affected some problems with complementarity constraints.

## 20210731

Fix an obscure bug: under complicated conditions, variable.val and constraint.val did not reflect recent changes. Example:  
     var x; fix x := 3; display x.astatus;  
     unfix x; let x := 5;  
     display x.val, x; # printed x.val = 3 rather than 5

## 20210714

Fix another performance bug: assignments to suffixes, such as "relax", should not cause presolve to run in preparation for the assignment.  
  
When bailing out due to option eexit, dump presolve messages before stopping.  
  
Under MS Windows, allow blanks in option TMPDIR (a bad idea). Blanks in $TMPDIR were already allowed on other systems.

## 20210625

Fix a performance bug: after a "delete variable" command, some commands, such as "display", could cause presolve to run unnecessarily.

## 20210613

Fix a couple of glitches in the "expand" and "solexpand" commands: incorrect printing (under complicated conditions) of comments "Eliminated by presolve" and "free row".

## 20210531

Fix a bug with complementarity constraints that could incorrectly lead to the message "presolve finds a nonsquare complementarity system", e.g., with econ.mod and econ.dat in the AMPL book.  
  
Change from 200 to 299 the value assigned to solve\_result\_num when presolve eliminates all variables and finds an infeasible constraint. Now whenever presolve finds the problem infeasible, solve\_result\_num should be set to 299. It is set to 99 when presolve solves a feasible problem.

## 20210521

Fix a bug in the MS Windows binaries with "write ...; solve;". Binaries for other platforms (such as Linux and MacOS) are unaffected.

## 20210505

Fix bugs with data sections appearing after something causes an entity's declared default value to be used. Unless a "reset data" or "update data" command has given permission for the data section to provide a new value for the entity, there should be an error message. Example:  
     var v default .1;  
     display v; # cause default to be used  
     data;  
     var v := 0.08; # should (but did not) elicit an error message  
     display v; # showed the old value, .1  
     # For sets, showed the new value.  
     # With today's bug fix and with "reset data;" or "reset data p;"  
     # or "update data;" or "update data p;" before "data;",  
     # "display v;" would show the new value.

## 20210414

New option log\_file\_flush. If option log\_file is given and $log\_file\_flush is 1, $log\_file is flushed after each write to it. By default (option log\_file\_flush 0), $log\_file is only flushed when the input file is stdin.

## 20210330

Fix a bug with deleting constraints and variables that crept into version 20201019. The bug manifested itself at the second delete.

## 20210325

Fix a presolve bug with the default option var\_bounds = 1 setting: if a constraint was dropped because it implied a stronger bound on an integer variable, the stronger bound was not conveyed to the solver. (Specifying "option var\_bounds 2" was a work-around.)  
  
Fix a presolve bug with complementarity constraints. Removing a constraint after fixing all the variables in it should correctly resolve a complementarity condition involving the constraint.  
  
New builtin param \_check\_failures records how many check statements failed in the most recent relevant command ("check" or "solve" or "solution" or "write").

## 20210126

Recant change of 20210220, as it suppressed syntax errors in interactive declarations.  
  
Fix a possible bug (e.g., fault) with recursive parameters.  
  
New command "reset check;" causes all "check" statements to be executed afresh by a "check" or "solve" or "solution" or "write" command. Normally a check statement is only executed at the first "check" or "solve" or "solution" or "write" command after the check statement's declaration or at a later "check" or "solve" or "solution" or "write" command if something the statement is testing has changed.

## 20210123

When too much memory is used, normally an error message such as  
  
Bug: Too much memory used -- 4276003800 bytes; couldn't get 32780 more.  
  
appears, but if a memory block needed to print how much memory was used cannot be allocated, simply print "Too much memory used." rather than silently quitting.

## 20201123

Fix a bug with some subscripted generic synonyms after some of the entities in question have been dropped/fixed. Wrong values were computed. Example:  
     model diet.mod  
     data diet.dat  
     solve;  
     drop diet\['B1'\];  
     display \_conname, \_con, \_con.body, \_con.slack;  
     display {i in 1..\_ncons} (\_conname\[i\], \_con\[i\], \_con\[i\].body, \_con\[i\].slack);  
     # \_con\[i\].body and \_con\[i\].slack were wrong for i > 1.  
Fix a bug with \_ccon\[something\].astatus and \_ccon\[something\].status, which gave "Bug: bad case 6 in f\_OPSYNDOTSYM".

## 20201110

New option let\_domain\_check (default 0). The domain check in let, introduced 20201031, is now only done if $let\_domain\_check is nonzero. Someone provided an example where the test greatly increased run time.

## 20201031

Fix a glitch (possible fault) in interactive mode connected with an error message for a wrong number of subscripts. Example:  
     ampl: set S1 := 1..3;  
     ampl: set S2 := 1..3;  
     ampl: param a {S1,S2};  
     ampl: let a\[1\] := 1;  
     # fault  
For entities with restricted domains (e.g., params with an "in" clause), check the restrictions at the end of "let". Example:  
     set A := {'a', 'aa', 'aaa'};  
     param a symbolic in A;  
     let a := 'bcd';  
     display a; # no longer reached

## 20201019

Fix a bug (fault) with a set of variables indexed over the empty set.  
  
Have the delete command recover more memory from constraints and variables.

## 20200810

Fix bugs in computing the value of a defined variable, which was sometimes wrong if the right-hand side involved a piecewise-linear term or a defined variable with a linear part.

## 20200501

Fix a seemingly invisible bug with "let \_con\[i\] := ...".  
  
Fix a bug with \\ in data sections. Example:  
     param p symbolic;  
     data;  
     param p := "x\\  
\\\\  
y"; # erroneous error message about missing "  
Fix a bug with \_nvars after a "delete variable" command.  
  
Fix an obscure display bug that gave error message "corrupted del\_mblk arg".

## 20200110

Fix a fault with "option;" after adding a new option to another environment that is not in the current one.  
  
Add a Caution about ignoring a duplicate ":=" in a data section. The example that caused this addition led to a fault (now avoided).

## 20191223

Fix a bug with presolve on problems with piecewise-linear terms: an incorrect array reference could have an out-of-bounds subscript on problems of the "right" size.

## 20191116

Fix a bug with "drop" and "restore" that arose under complicated and rarely seen conditions. Memory corruption was possible.

## 20191108

Fix a glitch with blockmode ("ampl -b ...") introduced 20190819. Error messages from presolve had the wrong label.

## 20191031

Fix a bug that appeared under complicated conditions involving the member() function.  
  
Arrange for "option cmdtrace 1;" to print command numbers with full precision, which only matters if many commands are executed.

## 20191015

Fix memory leaks with "print", "printf", and "display".

## 20191001

Fix bugs with "astatus" and "exitcode" suffixes on problems.  
  
Banish one reason for a rarely seen "OPDIV botch in e2v" message.

## 20190927

Fix an obscure fault.

## 20190919

Fix a potential compiler-dependent bug (not yet actually seen) on 64-bit systems with first(Set), last(Set), and card(Set).

## 20190911

Fix a rarely-seen glitch (wrong value computed) with a defined involving a piecewise-linear term applied to another defined variable involving a piecewise-linear term.  
  
Fix a fault that was possible with inappropriate outopt values, such as "write zfoo;". Invoking "ampl -o?" shows the allowed values.

## 20190830

Fix a bug with suffixes: after an indexed constraint goes from having some suffix values to none, due to a decrease in the indexing-set cardinality, a subsequent addition to the indexing set could lead to trouble.

## 20190824

Fix some seldom-seen bugs (faults or possible misbehavior), e.g., with slices in some command sequences or with bad data-section syntax.

## 20190819

Fix a glitch under MS Windows with block mode ("ampl -b ...") and option show\_presolve\_messages (at its default value).

## 20190817

Complain when an input file ends in the middle of a comment.

## 20190814

Fix a bug with suffixes initialized in declarations: when some initial values were 0, it was possible for some subsequent initial values to be lost (converted to 0). Example:  
     set A = 1..5; set C = {2,3,5};  
     var x {a in A} >= 0 integer suffix relax if a in C then 1 else 0;  
     display x.relax; # x\[5\].relax was lost.  
Fix a glitch with Unicode (UTF8) characters affecting "show" commands and the output of "ampl -D" on input without commands. Some text was lost. Examples (requiring a window that understands UTF8): "ampl" on  
     set pá; param cost {pá} > 0; show pá, cost;  
"ampl -D" on  
     set pá; param cost {pá} > 0; data; set pá := dód cär;  
Fix a glitch introduced 20190716 with demo licenses: the error message for oversize problems was lost.

## 20190716

New builtin symbolic parameter \_presolve\_messages is assigned messages produced by presolve. New option show\_presolve\_messages (default 1) determines whether the presolve messages are printed.

## 20190617

Fix a bug (possible fault), introduced in version 20190418, with "option single\_step 1; commands 'somefile';".  
  
Until further unforeseeable changes come along that require solvers to react to the AMPL version, the date that sometimes appears on line 1 of a .nl file is now fixed at 20190616. This should facilitate some kinds of testing, as it removes a gratuitous cause for differences in .nl files generated with different AMPL versions, at least those with versions >= 20190616.  
  
Forbid "load" commands from overriding existing declarations.

## 20190616

Fix a bug with cleaning up after a "not defined" error in a nested-loop context. An infinite loop or surprising error message was possible. Example:  
     set A dimen 2; data; set A := (1,a) (2,b);  
     for{i in 1..2}  
          for{j in {'a','b'}}  
               print {k in U\[j\]} i,j,k; # U was not declared

## 20190612

Fix a bug with variable.val: some expressions were not recomputed when the value of the variable changed. (Workaound: use variable rather than variable.val, which is also easier to read.)  
  
New option load\_funcdcl determines whether imported functions are implicitly declared when their library is loaded or (new possibility) when an imported function makes another imported function available:  
  
0 ==> no (default and the old behavior)  
1 ==> yes, quietly  
2 ==> yes, with a report of the declaration.  
  
Explicit declarations after implicit declarations are allowed.

## 20190529

Fix a bug with "display p;" involving declarations of the form  
     set S; set T{S} ordered; param p{i in S, T\[i\]};  
When the bug bit, it caused a surprising "display bug!" message.  
  
Fix a glitch with prompts. For example, after "include junk" typed at the "AMPL:" prompt, if file "junk" contained another "include", such as "data foo.dat", the "AMPL:" prompt was lost at the end of file "junk".

## 20190505

Redo update of 20190220 (to fix a fault with too few dummy variables in an indexing) so the arity of the indexing set is maintained.  
  
Adjust error processing so in interactive mode (reading from stdin when, e.g., -vi1 was specified on the command line or when stdin is a console window), execution of a command is not skipped during error recovery.

## 20190418

In the contexts  
     _commands filename;  
     data filename  
     include filename  
     model filename_  
if _filename_ starts with "<", the remainder of _filename_ is taken to be a command and operands to be interpreted by the host operating system (e.g., by /bin/sh on Unix systems), and the standard output of the command is processed as the contents of _filename_. For example,  
     _model '< gzip -dc foo.mod.gz foo.dat.gz'_and  
     _model '< unzip -p zap.zip zap.mod zap.dat'_  
would decompress foo.mod.gz and foo.dat.gz or would extract zap.mod and zap.dat from zap.zip and take them as input. (For this to work, foo.dat or zap.dat would need to begin with "data;".) For "model", "data", and "commands" (but not "include")  
     _model < filename  
     data < filename  
     commands < filename;_  
are treated as though filename began with "<", so, .e.g,  
     _model '< gzip -dc foo.mod.gz foo.dat.gz';_and  
     _model < 'gzip -dc foo.mod.gz foo.dat.gz';_  
are treated alike.

## 20190223

Fix a bug (fault) with "reset options;" in a compound command, such as a loop.

## 20190220

Fix a fault with too few dummy variables in an indexing. Example:  
     set S; set T = {t in {S,S}}; # faulted

## 20190207

New command  
     sleep \[expr\];  
causes the AMPL process to be suspended for expr seconds (default 1).  
  
Give a more detailed error message for attempts to use a function with out-args in a declaration.  
  
Fix a bug introduced in 20190130 that affected problems with piecewise-linear terms.  
  
Adjust the logic for "option randseed 0;" to avoid some trouble with repeated uses of this option. On some 64-bit systems, after a while "option randseed 0;" seemed not to affect the sequence of pseudo-random numbers generated.

## 20190130

When presolve complains about an infeasible constraint with no variables, retain the constraint, so a second "write" or "solve" command will emit an infeasible problem when option infeas\_clear has its default value 1, or when a .nl file is written by a command-line invocation of the form "ampl -ogfoo foo.mod".

## 20190122

Fix a bug with data updates that cause some variables to disappear completely after being used in a "solve". A fault (or worse) was possible in a subsequent solve.

## 20181217

Fix a bug with iterated "let" in the following example:  
     set S; var x{S}; let S := {}; /\*empty: card(S) = 0\*/  
     let{i in S} x\[i\] := i^2 + 1;  
     let S := 1..4; /\* now card(S) >= 2 \*/  
     let{i in S} x\[i\] := i^2 + 2; # corrupted memory

## 20181210

Fix a bug (fault or worse) with sequences of solves in which a variable or constraint indexing set starts with positive size, then is updated to have size 0, then is updated to have size larger than 1.

## 20181123

Fix a seldom-seen bug in saving primal and dual variable values after the indexing set of the variable or constraint in question has decreased sufficiently in size. There was a fault in the illustrating example.  
  
Fix a fault with nonlinear use of a defined variable involving a piecewise-linear term. Example:  
     var x in \[-1,10\];  
     var y = <<1,3,6;-1,1,-1,1>> x;  
     minimize zot: exp(2\*y); solve; # faulted  
Ignore HEARTBEAT lines in the ampl.lic file.

## 20181114

Fix bugs (faults) with a "model" or "data" commands of the forms  
     model (if t == 1 then 'a.mod' else 'b.mod')  
and  
     model (if t == 1 then 'a.mod' else if t == 2 then 'b.mod')

## 20181102

Fix a bug introduced 20181022 in the logic that determines which entities need to be updated. Some were not updated when they should have been (in a complicated example).

## 20181026

Convert "param x random" to "var x random". Issue a Caution about this conversion unless "option randparam\_warn 0;" has been specified.

## 20181022

Fix a rarely seen bug (fault) in saving variable values.  
  
Fix a bug with \_ampl\_time, \_ampl\_system\_time, \_ampl\_user\_time, \_ampl\_elapsed\_time, and \_session\_time, which were not updated after their first evaluation.

## 20181018

Fix a bug with limiting the number of file descriptors in use. When a file was closed so its file descriptor could be reused and later was reopened with a different file descriptor, a saved copy of the original descriptor was not updated. This caused a surprising read failure in the example that brought this bug to light.

## 20181005

Fix a bug in combining linear expressions or with defined variables involving piecewise-linear terms. A fault was sometimes possible.

## 20180927

When an error message of the form  
     z must be redeclared without y.val  
appears due to y being a defined variable, add text of the form  
     because y is a defined variable  
     and y.val is not allowed here.  
to the error message.

## 20180822

Fix bugs with simplifying some logical constraints, leading to an error message about an "unexpected nonvariable type".

## 20180820

Fix a bug seen in scripts of the form  
     repeat {  
          solve;  
          break;  
          }  
     print solve\_exitcode;  
in which the "solve" commands gives a nonzero solve\_exitcode.  
  
Modification to changes of 20160325: when a shell or solve command gives shell\_exitcode > $shell\_exitcode\_max > 0 or solve\_exitcode > $solve\_exitcode\_max > 0, respectively, show an option command that would have suppressed a "<BREAK>" message. The shell or solve command behaves as if a BREAK (control-C) had been received if $shell\_exitcode > abs($shell\_exitcode\_max) or $solve\_exitcode > abs($solve\_exitcode\_max), respectively.  
  
Another change: "exit code" is changed to "exit value" in some messages. When a shell or solve process ends, it returns an "exitcode value" that is assigned to option shell\_exitcode or solve\_exitcode, respectively, and on Unix-like systems (such as Linux and MacOSX) is computed as  
  
     256\*(exit\_value) + termination\_code  
  
in which termination\_code is zero if the shell or solve process ended by calling exit(exit\_value) or returning exit\_value and is nonzero if the exit() call could not be reached due to a segmentation fault (i.e., serious bug) or similar error. On MS Windows systems, the "exitcode value" is the exit\_value.

## 20180624

Add variant "write 1;" of "write 0;" that does not emit the message "No files written: option outopt is 0."  
  
Have printf honor field widths given with %c format specifiers. For example,  
     printf "X%4cY%-4cZ\\n", 'a', 'b';  
formerly printed "XaYbZ" and now prints "X   aYb   Z".

## 20180618

Fix a bug with string-valued imported functions that seems to have crept in with version 20070301: calls involving at least one numeric argument faulted. An example using amplfunc.dll compiled from https://ampl.com/netlib/ampl/solvers/funclink/funcadd.c:  
     function kth symbolic; print kth(2,1,3,5); # faulted

## 20180525

Compute tanh(x) and tanh'(x) for large |x| without complaint.

## 20180522

In data sections, accept "param :setname: parname (tr)" followed by a : ... := table (called a value-table on p. 476 of the AMPL book). For example,  
     set S dimen 2; param p{S};  
     data; param :S: p (tr)  
          : X Y Z :=  
          A 1 2 3  
          B 4 . 6;  
     display S, p;  
will now work, with X, Y, and Z as first members of the tuples in S.

## 20180519

Fix a rarely seen bug (e.g., losing some variable or constraint indices) that bit after an update, such as reordering a set, caused some entities to be reinstantiated.  
  
Compute tanh(x) and tanh'(x) for large x without complaint.

## 20180511

Fix a bug (possible fault) in processing utterly pointless input of the form "data; param p := .;".

## 20180503

When single-stepping, try to recover from input errors rather than simply exiting.  
  
Fix a bug, introduced 20171122, with "param :setname: parname" followed by a : ... := table (called a value-table on p. 476 of the AMPL book). For example,  
     set S dimen 2; param p{S};  
     data; param :S: p  
          : X Y Z :=  
          A 1 2 3  
          B 4 . 6;  
     display S, p;  
will now work again.

## 20180423

Fix a bug with a double inequality giving a bound on a defined variable and another constraint giving a stronger bound on the variable. The other bound on the variable was sometimes lost.

## 20180417

"Invisible" tweak to yesterday's changes.

## 20180416

Withdraw option funcwarn and the associated -f command-line option; now the former "option funcwarn 1" is always assumed. Fix a bug with the sequence  
     solve;  
     # error message about an unavailable function  
     load some\_library.dll; # to provide the function  
     solve;  
The constraint or objective in question was not regenerated using the newly available function.  
  
Fix a bug with "load library" providing a decoding function: the "read" command was not properly handled after decoding started. Relevant documentation may only be provided on request.

## 20180316

Fix a bug with a sequence of solves involving fixing some but not all members of a set of variables, then unfixing all of the set of variables, then doing something causing the set of variables in question to be regenerated. The previously fixed variables were erroneously held fixed. The update of 20170706 seems to have revealed, but not caused, this bug.

## 20180308

Under -b (block-mode), suppress some superfluous lines that sometimes (harmlessly) appeared to identify commands.

## 20180125

Adjust history mechanism so it may deal better with unexpected escape sequences, and use a larger stacksize in hopes of avoiding a bug in Red Hat's glibc-2.17-196.el7\_4.2.x86\_64. No update to MS Windows binaries.

## 20180123

Fix a bug that could arise under complicated conditions with problems involving piecewise-linear terms or "var ... in set..." constructions.

## 20180115

Expand and clarify "ampl -v?" output.  
  
On Unix-like systems, extend history mechanism so escape-backspace acts like control-w, omitting the preceding word; control-a acts like the "Home" key, moving the cursor to the start of the line; control-e acts like the "End" key, moving the cursor to the end of the line; escape-b moves the cursor back one word; escape-f, like control-w, moves the cursor ahead one word; and escape-d omits the word ahead.  
  
On Unix-like systems, suppress history if at least one input file is given on the command line and no command-line input files are "-" (a single dash). This can be overridden by invoking "ampl -vi4 ...", which could matter if an "include -" phrase appears.

## 20171212

Fix an obscure fault, hitherto not seen, involving piecewise linear terms.

## 20171209

Fix unlikely trouble with reduced-cost computations when "option allow\_NaN 1" is in effect and with exp(...) expressions that underflow to zero.  
  
Fix a bug with defined variables whose value is a linear expression plus a defined variable involving a nonconvex piecewise-linear term. The linear expression got lost. Example:  
     var y >= -10;  
     var z = 3\*y;  
     s.t. xb: -1 <= z <= 16;  
     var pl = <<2,3,5,9,12;1,-1,1,-1,1,-1>> z;  
     var c = 4\*z + 3\*pl;  
     minimize pd: c; # the 4\*z part got lost  
Fix another bug with nonconvex piecewise-linear terms illustrated by the example  
     var x >= -1 <= 16;  
     minimize pl: <<2,3,5,9,12;1,-1,1,-1,1,-1>> x;  
     s.t. q: (x-6)^2 <= 200;  
which resulted in an invalid .nl file.  
  
Fix an infinite loop involving unusual use of defined variables.

## 20171122

Fix a possible fault with "data foo" when file foo contains an ill-formed header.  
  
Extend option allow\_NaN to apply to more contexts, e.g., computation of reduced costs when some constraints are removed by presolve. Example of using $allow\_NaN in an interactive session:  
     _ampl:_ var x{1..2} >= 0;  
     _ampl:_ minimize zot: sum{i in 1..2} (x\[i\] - i)^2 + sqrt(x\[1\]);  
     _ampl:_ s.t. vex: x\[1\] + x\[2\] <= 1;  
     _ampl:_ s.t. c1: x\[1\] <= 0;  
     _ampl:_ solve;  
     MINOS 5.51: optimal solution found.  
     1 iterations, objective 2  
     Nonlin evals: obj = 4, grad = 3.  
     _ampl:_ display x.rc;  
     Error executing "display" command:  
       
     Error differentiating zot: can't compute sqrt'(0).  
     _ampl:_ option allow\_NaN 1;  
     _ampl:_ display x.rc;  
     x.rc \[\*\] :=  
     1 NaN  
     2 0  
     ;

## 20171111

Circumvent scurrilous behavior by Microsoft's ODBC software -- unexpectedly changing arithmetic details when x8087 instructions are involved. This was seen in a "write table" example. A "read table" likely would also have caused the trouble, which was seen in the round() function, but would also affect other binary <--> decimal conversions.

## 20171107

Fix a glitch with "reset;" under -R: $PATH could have been corrupted.

## 20171103

Fix a bug that, under complicated conditions involving "unfix", gave error message "... presolve finds no feasible solution possible." Example:  
     var x >= 2 := 10;  
     minimize f: x;  
     fix x;  
     s.t. c: x <= 5;  
     display c.slack;  
     unfix x;  
     display c.slack;  
     solve; # ... presolve finds no feasible solution possible.

## 20171028

Fix a bug with "ampl foo" when file foo ends with an incomplete data section (no final semicolon) whose last line is incomplete, i.e., does not end with a newline character. With some versions of MS Windows, the 64-bit ampl.exe faulted on such examples.

## 20171002

Have printf format %q quote ".".  
  
Fix a glitch that sometimes caused "write table" to run presolve unnecessarily, which could cause a spurious "Solution determined by presolve" message to appear.  
  
Fix a bug in the handling of synonym \_con by "write table".

## 20170925

In $table\_debug\_template just require one % and no white space.

## 20170924

Fix a fault that arose under unusual conditions.  
  
New debug options table\_debug (default 0) and table\_debug\_template (default "%.dbtab") can cause tables in the format of .tab files to be read or written rather than or in addition to files specified for "read table" and "write table" commands. For this to work, option table\_debug\_template must contain one % character and otherwise only alphanumeric characters or plus, minus, underscore or period. When $table\_debug and $table\_debug\_template indicate a .tab-format file, the file's name is obtained by substituting the declared table name for the % character in $table\_debug\_template; $table\_debug is the sum of  
  
     1 ==> "read table" should read the .tab-format file  
               and ignore the 2 bit if set in $table\_debug  
     2 ==> "read table" should write the .tab-format file  
     4 ==> "write table" should also write the .tab-format file  
     8 ==> "write table" should not write the declared table  
  
While the builtin .tab file handlers only act on file names that end with ".tab", the .tab-format files controlled by $table\_debug act on the constructed .tab-format file names.

## 20170914

Fix a bug with a subscripted defined variable subject to bound constraints when the indexing set, after being instantiated for one "solve", increased in size beyond the next power of 2 for a subsequent "solve".  
  
Add a Caution for "(numeric expression) & (numeric expression)", which converts both numeric values to strings and concatenates them. Since dummy variables may have string or numeric values, the new Caution is not given for "A & B" when A or B is a dummy variable.

## 20170902

Fix a bug with reading ".tab" tables with rows more than 2000 characters long. An occasional value might have been misread as 0.

## 20170731

Allow "and" as a synonym for "for all" and "or" as a synonym for "there exists". Thus the logical expressions  
     there exists {i in I} b\[i\]  
and  
     or {i in I} b\[i\]  
are treated alike, and the logical expressions  
     for all all {i in I} b\[i\]\]  
and  
     and {i in I} b\[i\]\]  
are treated alike.  
  
In "shell" and "solve" commands, ignore "> filename" and ">> filename" redirections when the file was specified in "option logfile" (which makes no sense). Previously a fault resulted.

## 20170724

Fix bugs with "break commands;" and "break all;" that could bite if the command terminated a loop with dummy variables.

## 20170718

Fix a another possible fault in "display p;" when p has an indexing set involving three or more set expressions and some later set expressions depend on earlier ones. Whether the bug bit depended on the relative sizes of the component sets. Example:  
     set A; set B{A} ordered; set C;  
     param p{i in A, B\[i\], C} := Normal01();  
     data;  
     set A := 1 2 3;  
     set B\[1\] := a b c;  
     set B\[2\] := c a b;  
     set B\[3\] := b c a;  
     set C := W X Y Z;  
     display p; # faulted

## 20170717

Fix a possible fault in "display p;" when p has an indexing set in which later set expressions depend on earlier ones. Example:  
     set A; set B{A} ordered;  
     param p{i in A, B\[i\]}; data;  
     set A := 1 2;  
     set B\[1\] := a b c;  
     set B\[2\] := c a b;  
     param p : a b c :=  
     1 11 12 13  
     2 21 22 23;  
     display p; # faulted

## 20170711

More fixes to "break" commands in nests of "commands" commands.

## 20170706

Extend the change of 20170621 so in the context of  
     for outerloop {...} {  
          for {...} {  
               ...  
               commands foo;  
               ...  
               }  
          }  
a "break outerloop;" in a file in a nest of "commands" commands in file foo will terminate the outer loop.

## 20170630

Fix a botch in the changes of 20170621 that could cause a fault in a "commands" command.

## 20170628

Fix a fault that arose under complicated conditions.  
  
Fix a nasty bug with defined variables that led to wrong objectives and constraints: when a defined variable had both a linear and a nonlinear part, wrong linear parts were sometimes transmitted to the .nl file under the default option linelim 1. Example:  
     var x := 3; var y = 2\*x + (x-1)^2;  
     minimize foo: 3\*x + y; # behaved as 5\*x + y

## 20170621

In commands of the form  
     for outerloop {...} {  
          for {...} {  
               ...  
               commands foo;  
               ...  
               }  
          }  
have a "break outerloop;" in file foo terminate the outer loop.

## 20170616

Honor "ordered" in  
     set S{1..1} ordered; param p{S\[1\]};  
     data; param :S\[1\]: p := b 1 a 2 c 3;  
     display p; # previously ignored the S\[1\]'s ordering  
and in  
     set GEN ordered; param a {GEN};  
     table Gen IN /\*...\*/: \[GEN\] IN, a;  
     read table Generators; display a;

## 20170614

Fix a fault that was possible under complicated conditions.

## 20170613

Fix another bug with defined variables; the bug resulted in an incorrect .nl file. Example:  
     var x{i in 1..2} := i;  
     var y1 = x\[1\] + x\[2\]^2; # nonlinear defined variable  
     var y2 = 2\*y1 + 1; # linear use of y1  
     minimize o: 1/y2; # nonlinear use of y2

## 20170531

Allow an optional comma between phrases in a set declaration (as already allowed in param, variable, objective, and constraint declarations -- none of which is described in the AMPL book).  
  
Allow commas to separate values in "read" commands.  
  
Fix a fault with complicated uses of piecewise-linear terms in iterated constraints.  
  
Fix some bugs (leading to invalid .nl files) with complicated uses of defined variables.

## 20170412

Fix a glitch (surprising error message) in computing reduced costs involving an imported function with a string valued "if ... then ... else" argument.

## 20170207

Fix a bug that could only bite a script running more than 4294967296 (i.e., 2^32) commands.

## 20170126

Fix some bugs with tab completions, and extend ambiguous matches over the unambiguous part.

## 20170111

Fix a bug with handling more than 64 output files from file redirections (">filename" or ">>filename"): a fault was possible in "solve" or "shell" commands on Unix-like systems, such as Linux.  
  
Adjust history processing on Unix-like systems so when the current input line is nonempty, control-D behave like "Delete", deleting the character under the cursor. Also arrange for the tab key to do filname-completion (when unambiguous, except on 32-bit Sparc Solaris).

## 20161231

Fix a rarely seen bug with defined variables fixed by presolve that led to the error message "bug: corrupted del\_mblk arg".

## 20161220

Fix a bug with defined variables: nonlinear expressions all of whose variables were fixed by presolve were effectively ignored. Example:  
     var x >= 0; var y = sqrt(x);  
     s.t. c: x == 1; print y; # printed 0 rather than 1

## 20161209

Fix a glitch with NaNs in min() and max() expressions. E.g., min(3,NaN) should be NaN, not 3.  
  
New command-line option -x sss instructs AMPL to run for at most about sss wall-clock seconds. It may run 4 or 5 seconds longer, particularly under MS Windows, to allow solvers to stop and clean up. On Unix-like systems, such as Linux, signals SIGHUP (when not being ignored, e.g., by running under nohup), SIGINT, SIGQUIT and SIGTERM are now passed to solvers, and SIGHUP (when not ignored) and SIGTERM cause the AMPL session to terminate. When the solver is a binary, the solver now sees all of SIGHUP, SIGINT, SIGQUIT and SIGTERM. When the solver is a shell script, results depend on what "trap" settings have been specified.  
  
New system parameters (automatically maintained, and not adjustable, e.g., in "let" commands):  
  
     \_session\_time = wall-clock seconds consumed  
     \_session\_maxtime = wall-clock session specified by "-x sss"  
  
When -x is not given on the AMPL command-line, \_session\_maxtime is reported to be 0.

## 20161110

Fix a parsing glitch (surprising error message) that could arise with a model or data command immediately following a compound command (at the outermost level) of the form  
     for{i in ...} repeat { ... } while ... p\[i\] ... ;  
where the test in the while clause involves an entity subscripted by a dummy variable instantiated in the for{...}.

## 20161107

Fix a glitch (surprising error message) in 64-bit binaries with models having defined variables and at most one constraint or objective, but not one constraint and one objective.

## 20161025

Adjust presolve to eliminate some defined variables that were previously rendered as constant-valued variables. Example:  
     var x{i in 1..2} := i+1;  
     var y = 1 / x\[2\]; # appeared in the .nl file as a  
     s.t. c: x\[2\] = 3; # defined var with constant value 1/3  
     minimize zot: (x\[1\] - y)^2;

## 20161005

Fix a bug that could bite after some error messages, such as (the unlikely) "cannot multiply ... by Infinity". No examples of the bug actually biting are known.

## 20160920

Rather than always terminating execution after an error message of the form "nnn is not defined", when this message appears after a "model", "data", or "commands" command or include phrase issued in interactive mode, return to interactive input (after ignoring the rest of the offending input file).

## 20160907

Fix a glitch in the update of 20160829, which led to an inappropriate "syntax error" under complicated conditions.

## 20160829

Fix a parsing glitch: do a better job of treating comments delimited by /\* and \*/ as white space. Example:  
     print if 1 < 2 then 3/\*comment\*/ else 4;  
     # erroneously complained "3else is not defined"; now prints 3

## 20160803

Change the message "xxx is not defined" from a warning to a fatal error (which terminates execution).

## 20160714

Fix a bug with constraints, objectives, and defined variables involving a nonlinear expression of the form  
     sum{i in S} if ... then i else ...  
or  
     sum{i in S} if ... then ... else i  
in which "if ..." involved variables. An incorrect "if" operator could appear in the .nl file, which on some systems might lead to incorrect nonlinear evaluations in solvers. (On at least one system, a 32-bit Linux system, the bug was invisible.)

## 20160712

Fix a bug with models having both "var in set" declarations and logical constraints. Incorrect .nl files or faults with "solexpand" were sometimes possible. Example:  
     var x{1..2} integer in {11, 22};  
     s.t. c: alldiff{i in 1..2} x\[i\]; solexpand; #fault

## 20160614

## 20160609

Fix a rarely seen bug in which the right-hand side of a "let" command involved a defined variable whose value was miscomputed.

## 20160602

Fix a bug with some suffixes (of length 4-7) on synonyms. When the bug bit, memory corruption was possible.

## 20160530

Fix a bug in reading .sol files involving partially dropped logical constraints: memory corruption was possible.  
  
Extend option infeas\_clear so "option infeas\_clear 3;" allows "write" and "solve" commands to proceed when presolve detects infeasibility. In short, possible values for infeas\_clear are now  
  
     0 ==> always suppress "solve" and "write"  
     1 ==> allow a second "solve" or "write" to proceed when reading stdin in interactive mode (default)  
     2 ==> always allow a second "solve" or "write" to proceed  
     3 ==> always allow "solve" or "write" to proceed.  
  
Suppress some unlikely option commands issued while reading .sol files when they have no effect.

## 20160519

Fix a bug (possible fault) in updating indexed symbolic params via "read table".  
  
Adjust ordering of sections in .nl files so bounds on variables and constraint bodies and primal and dual initial guesses precede constraint bodies. This change should be invisible to solvers that use the AMPL/solver interface library. For other solvers, turning on the "32" bit of $nl\_permute will restore the old ordering. This interpretation of the "32" bit will eventually be removed unless we hear of a good reason to retain it.

## 20160513

Fix a bug introduced in 20150721 that caused some defined variables involving linear uses of other defined variables to be miscomputed in the AMPL session (but not by solvers). Example:  
     var w >=0.5 <=1 :=1;  
     var x = sum{i in 0..4} w^i;  
     var y = x;        # linear use of defined var x  
     var z = exp(y/w); # = exp(x/w) worked correctly  
     maximize o: z;  
     display x, y, z, objective; # z and o were wrong

## 20160510

Fix some trouble in reading very large data sections, requiring memory blocks >= 2^32 bytes long (which requires 64-bit binaries).  
  
Some binary <--> decimal conversions should now be faster. This should not affect anything but timing, but please let us know if you see other effects.

## 20160325

When a shell command gives shell\_exitcode > abs($shell\_exitcode\_max), resulting in "<BREAK>", show an option command that would have suppressed the "<BREAK>". The new printing of an option command is suppressed if $shell\_exitcode\_max < 0. Previously the test for issuing a "<BREAK>" was whether shell\_exitcode > $shell\_exitcode\_max.

## 20160310

Fix glitches with floating-point values in hexadecimal notation (use of which is supported but very unlikely): some values that should overflow to (appropriately signed) Infinity, such as 0x1p1025, were mishandled, and values greater than 0x1p-1075 and less than 0x1.0000000000001p-1075 where treated as zero rather than the smallest denormal number.  
  
Fix a bug with with the current environment: after an environ command changed the environment, a problem command specifying the current problem did not change the environment back to the problem's environment.

## 20160221

Fix a bug (possible fault) with the interaction of blockmode (used with some API variants), option log\_file, and shell or solve commands.  
  
New builtin function date(fmt,t) returns a string representing time t (as returned by the builtin time() function), formatted according to fmt (a character string). Either or both t and fmt may be omitted; time() is assumed if t is omitted and "%Y%m%d %H:%M:%S" is assumed if fmt is omitted; otherwise date(t,fmt) and date(fmt,t) are treated alike. The expected usual usage is simply date(), i.e., omitting both arguments, as in  
     print date();  
The fmt string is similar to that allowed for the "date" command on many Unix-like systems, such as Linux and AIX; fmt is interpretted by the widely available strftime() library function. In short, various letters, when preceded by a % character, are replaced by details derived from the time t. Some, indicated by \* below, may be affected by the current locale. Commonly available are  
  

<table><tbody><tr><td>%a</td><td>&nbsp;&nbsp;abbreviated day of the week*</td></tr><tr><td>%A</td><td>&nbsp;&nbsp;day of the week, fully spelled out*</td></tr><tr><td>%b</td><td>&nbsp;&nbsp;abbreviated month*</td></tr><tr><td>%B</td><td>&nbsp;&nbsp;month, fully spelled out*</td></tr><tr><td>%c</td><td>&nbsp;&nbsp;date and time as preferred in the current locale*</td></tr><tr><td>%d</td><td>&nbsp;&nbsp;two-digit day of the month (1-31)</td></tr><tr><td>%H</td><td>&nbsp;&nbsp;2-digit hour (00-23) based on 24-hour clock</td></tr><tr><td>%I</td><td>&nbsp;&nbsp;2-digit hour (00-11) based on 12-hour clock</td></tr><tr><td>%j</td><td>&nbsp;&nbsp;day of year (001-366)</td></tr><tr><td>%m</td><td>&nbsp;&nbsp;2-digit month (01-12)</td></tr><tr><td>%M</td><td>&nbsp;&nbsp;2-digit minute (00-59)</td></tr><tr><td>%p</td><td>&nbsp;&nbsp;AM or PM</td><td>&nbsp;&nbsp;</td></tr><tr><td>%U</td><td>&nbsp;&nbsp;week number of the current year (00-53), with week 01 starting on the first Sunday of the year</td></tr><tr><td>%w</td><td>&nbsp;&nbsp;day of the week (0-6), with Sunday = 0</td></tr><tr><td>%W</td><td>&nbsp;&nbsp;week number of the current year (00-53), with week 01 starting on the first Monday of the year</td></tr><tr><td>%x</td><td>&nbsp;&nbsp;preferred date representation*</td></tr><tr><td>%X</td><td>&nbsp;&nbsp;preferred time representation (without date)*</td></tr><tr><td>%y</td><td>&nbsp;&nbsp;2-digit year (no century)</td></tr><tr><td>%Y</td><td>&nbsp;&nbsp;4-digit year</td></tr><tr><td>%Z</td><td>&nbsp;&nbsp;time zone</td></tr><tr><td>%%</td><td>&nbsp;&nbsp;% character</td></tr></tbody></table>

  
Also available on some systems are  
  

<table><tbody><tr><td>%C</td><td>&nbsp;&nbsp;similar to %c, but also including the timezone</td></tr><tr><td>%D</td><td>&nbsp;&nbsp;%m/%d/%y</td></tr><tr><td>%e</td><td>&nbsp;&nbsp;like %d, but with a space in place of a leading 0</td></tr><tr><td>%F</td><td>&nbsp;&nbsp;%Y-%m-%d</td></tr><tr><td>%G</td><td>&nbsp;&nbsp;ISO 8601 4-digit year</td></tr><tr><td>%g</td><td>&nbsp;&nbsp;IS0 8601 2-digit year -- no century digits</td></tr><tr><td>%h</td><td>&nbsp;&nbsp;%b</td></tr><tr><td>%k</td><td>&nbsp;&nbsp;like %H, but with leading zero changed to blank</td></tr><tr><td>%l</td><td>&nbsp;&nbsp;like %I, but with leading zero changed to blank</td></tr><tr><td>%n</td><td>&nbsp;&nbsp;newline character</td></tr><tr><td>%P</td><td>&nbsp;&nbsp;lower-case %p: am or pm</td></tr><tr><td>%s</td><td>&nbsp;&nbsp;number of seconds since 19700101 00:00:00 UTC</td></tr><tr><td>%t</td><td>&nbsp;&nbsp;tab character</td></tr><tr><td>%T</td><td>&nbsp;&nbsp;%H:%M:%S</td></tr><tr><td>%u</td><td>&nbsp;&nbsp;decimal day of the week (1-7), with Monday = 1</td></tr><tr><td>%V</td><td>&nbsp;&nbsp;ISO 8601 week number (01-53)</td></tr></tbody></table>

  
On some systems, a #, E, or O may be inserted between % and some of the function letters indicated above to modify the conversion. Please experiment to see what works on your system.  
  
The fmt string may begin with %K or %L, which are removed and affect whether the rest of the fmt string reflects UTC time, formerly known as Greenwich Mean Time (%K), or local time (%L). Local time is the default, which %L simply confirms. If nothing remains after an initial %K or %L is removed, the default fmt is assumed. Thus date("%K") shows the current UTC time.  
  
The builtin ctime() function is extended to behave like date(), but with fmt = "%a %b %d %H:%M:%S %Y" assumed if fmt is omitted or is empty after an initial %K or %L is removed. Thus ctime("%K") shows the current UTC time, but formatted differently than date("%K").

## 20160211

Adjust debugging option nl\_permute so when permutations are suppressed, the .nl file will indicate numbers of nonlinear constraints and variables based on the last nonlinear constraint or variable. Give a Caution message when suppressing permutations affects the .nl file. The "8" and "16" bits of $nl\_permute can suppress these new Cautions. $nl\_permute is now the sum of  
     1 → reorder constraints  
     2 → reorder variables  
     4 → reorder objectives  
     8 → suppress Caution about constraints  
    16 → suppress Caution about variables.  
The default value for $nl\_permute remains 3. Option nl\_permute is not meant for use with solvers; great confusion may arise if binary or integer variables are present. Most users should avoid fiddling with $nl\_permute.

## 20160207

Fix a fault with an invalid subscript message occurring after generation of a newly instantiationed variable declared before previously instantiated variables (an obscure situation).

## 20160201

Fix a fault that arose under complicated conditions.  
  
Fix trouble with "option log\_File" when the solver faults.

## 20160131

Fix a rarely seen bug in changing the size of the indexing set of an indexed variable.  
  
Fix some bugs in the changes of 20160119.  
  
Fix a bug with "reset;" after "option log\_file" specifies an invalid file.

## 20160121

Fix a possible fault with "display foo;" when foo has a named 2-dimensional indexing set that is also the indexing set of an indexed collection of ordered sets.  
  
Fix possible trouble in the update of 20160119 during "reset;" when option log\_file is not "".

## 20160119

Arrange for defined variables that do not affect constraints not to participate in presolve deductions. Under unusual conditions, such defined variables could cause incorrect deductions.  
  
When more that 64 output files would be open, close the least recently used file and reopen it when necessary.

## 20151222

Fix a bug with reading large data sections (more than 16 or 32 kilobytes of values and subscripts for 32- and 64-bit binaries, respectively): data corruption or a fault was sometimes possible.

## 20151216

Fix a bug with using variables when params could be used: an assignment to an otherwise unused variable of a value involving a defined variable used in the problem just solved generally used 0 as the value of the defined variable. Example:  
    var F; # could be param F, as solvers do not see it  
    set I = 1..2; var x{I};  
    var f = sum{i in I} (x\[i\] - i)^2;  
    minimize o: f;  
    s.t. vex: sum{i in I} x\[i\] = 1;  
    solve; display f; # f = 2 (correct value)  
    let F := f; display F; # F was zero

## 20151203

Fix a bug with computing values of defined variables eliminated by presolve: the linear parts were ignored.

## 20151130

Fix a bug with "read table" or "write table" that gave error message "1 contexts remain open after compile!" under complicated conditions.  
  
Disallow defined variables in IN or INOUT table declarations.  
  
Update ODBC table handler so "Strcol:" prefixes in column labels are honored for "read table". Previously they only affected "write table".

## 20151120

Fix a bug with introduced 20151104 in handling complementarity constraints involving an explicit upper bound of +Infinity. An incorrect error message about the Infinity was given.

## 20151118

Fix a bug with "expand c;" when c is a constraint of the form  
    double-inequality complements expression  
or  
    expression complements double-inequality.  
If the expression involved a constant term, the constant term did not appear in the "expand" output. Example:  
    var x{1..3};  
    s.t. c: 3 <= x\[1\] <= 5 complements 123 + x\[2\] + 2\*x\[3\];  
    expand c; # 123 did not appear; it did appear in "solexpand c;"

## 20151104

Fix bugs with problems involving complementarity constraints and defined variables. Under complicated conditions, incorrect .nl files were written.  
  
Complain in more cases about objectives and constraints involving NaNs or bounds with inappropriately signed Infinity. (There was already a complaint about linear expressions with a Nan or Infinity as a coefficient.)

## 20151029

Fix some trouble updating variables under complicated conditions.  
  
Fix a glitch with "xref": named problems were listed twice.

## 20151026

Fix bugs that caused faults under complicated conditions.

## 20151015

Fix a bug (possible fault) with dropping all constraints and objectives that use a defined variable.  
  
Fix a bug with evaluating piecewise-linear terms in problems involving defined variables fixed by presolve. A wrong value might have been computed, e.g., for use in display.

## 20151010

Fix bugs with some complicated uses of defined variables and piecewise-linear terms. Examples:  
    var x;  
    var y = x + 3;  
    s.t. c: y = 7;  
    minimize o: <<4;-2, 3>> x;  
    write 0;  
    display x, y, o; # printed "y = 3" rather than "y = 7"  
and (illustrating a separate bug)  
    node n{1..3};  
    arc a{i in 0..2} from {if i >= 1} n\[i\] to {if i < 2} n\[i+1\];  
    s.t. c: a\[1\] = 3;  
    var x = a\[2\] + 1;  
    var y;  
    minimize o: x + <<7;-1,1>> y;  
    solve;  
    display o, x, y; # o and y were 11 and -7 rather than -3 and 7

## 20150929

Fix a bug (likely fault) with single-use licenses that only afflicted recent MacOSX and MS Windows binaries.

## 20150928

Fix some trouble (possible fault) with the update of 20150923.

## 20150923

Fix a bug with defined variables in scripts that change the cardinality of indexing sets of variables declared before the defined variables. A fault or other wrong behavior was possible.

## 20150910

Fix a bug with deducing that a defined variable has a fixed value. If the number of variables was sufficiently more than the number of constraints, memory corruption was possible.

## 20150831

Update the tableproxy\*.exe binaries in the ampl.mswin\*.zip bundles. They should have been updated in October 2014.

## 20150827

Under "ampl -b4", have error messages show context. This affects the AMPL IDE.

## 20150815

On some systems, mainly MacOSX and hpux-ia64, catch errors not reported via errno in evaluating some math functions.

## 20150721

Fix bugs with defined variables that are used as the only variable in an equality constraint. Solvers saw correct problems, but commands (such as display and print) that used expressions involving the defined variables saw incorrect values for those variables. Example:  
    var x := 2;  
    var y = (if x >= 1 then (x-1)^2) + 2.5;  
    s.t. c: y = 17.5;  
    display x, y, y.defeqn;  
    # gave y = -16 rather than 3.5  
    # and y.defeqn = 0 rather than 1  
Fix a bug in the indexarity functions: scalar variables gave -1 rather than 0. Example:  
    var x; print indexarity('x'); # printed -1 rather than 0

## 20150630

Fix a glitch with output redirections, which could get lost during computation of duals for eliminated constraints.  
  
Fix some possible trouble with a single-use license.

## 20150516

Fix a glitch with v.lb, v.ub, v.lslack, v.uslack, and v.slack where v is a variable instantiated without need of presolve and after one or more other variables have been instantiated. Example:  
    var x <= 0; var y <= 0; display y.lb; display x.ub;  
    # x.ub was wrong (with separate display commands)  
    # but all went well with "display y.lb, x.ub;"

## 20150505

Fix some glitches with error processing.

## 20150501

Fix a bug with logical constraints that bit under complicated conditions.

## 20150424

Fix a rarely seen licensing glitch.

## 20150422

When history is desired (e.g., stdin is not a file) but cannot be instantiated, allow "solve" and "shell" to work without the need to invoke "ampl -vi2". This is only known to be relevant to 32-bit Alpine systems and has no effect on MS Windows systems.

## 20150415

Fix some bugs that could affect models with logical constraints, defined variables, and piecewise-linear terms, and fix a bug with "option presolve 0" applied to such models.

## 20150327

Fix a bug (possible fault) that could bite during cleanup after an error message arising during instantiation of a defined variable.

## 20150325

Fix a bug (possible infinite loop) with a constraint of the form "1 ==> algebraic\_constraint" when the algebraic\_constraint involved a complicated sum.

## 20150313

Adjust printf format %q to treat non-ASCII Unicode characters as alphabetic characters. This affects the display command. For example,  
    set S; data; set S := π ρ σ τ; display S;  
now gives  
    set S := π ρ σ τ;  
rather than  
    set S := 'π' 'ρ' 'σ' 'τ';

## 20150312

Fix a glitch in processing UTF8-encoded Unicode that caused declared names starting with a non-ASCII character to be mishandled.

## 20150302

Fix a bug in assigning suffixes to subscripted problems by "solve" and "solution" commands. Suffixes were assigned to the problem's first subscript rather than the current one.

## 20150214

Fix a bug that bit under complicated conditions and gave error message "tva top error".

## 20150213

Extend simplification of logical constraints so a constraint of the form  
    logical\_condition ==> linear\_constraint  
in which logical\_condition is found always to be true is reduced in more cases to a linear rather than a nonlinear constraint.  
  
Fix a glitch in the reported number of eliminated algebraic constraints in the output of "option show\_stats 1" when logical constraints are converted to algebraic constraints.

## 20150131

Fix a possible fault with loops involving indexed collections of objectives and increases to the cardinality of the indexing sets of those objectives.

## 20150127

Fix a glitch with format %.0e that caused  
    printf "%.e\\n", 4.7;  
to print "4e+00" rather than "5e+00".  
  
Fix a fault with "show table\_name;" when table table\_name involves nested indexings. Example:  
    set S; set T; param p{S, T};  
    table mytab : \[S\], {j in T}<{i in S} p\[i,j\]~(i&j)>;  
    show table mytab; # faulted

## 20141231

To work around a Microsoft bug, set $ampl\_funclibs to "-" rather than "" when "solve" does not involve imported functions.

## 20141228

Fix a bug introduced in version 20140220 that sometimes bit with defined variables involving piecewise-linear terms, leading to incorrect results.

## 20141216

Fix a bug introduced 20141206 with defined variables not appearing in the current problem (i.e., not in any constraint or objective): such a variable was sometimes miscomputed.

## 20141206

Fix a couple of small memory leaks that accumulate over many commands.  
  
Fix a bug evaluating dropped objectives that depend on defined variables.

## 20141124

Fix a bug with expressions involving values of dropped objectives or of constraint bodies of dropped constraints when the expressions appear in commands, such as printing commands, and previous commands, such as "let" commands, have changed something involving variables involved in the expressions. Under some conditions -- without a "solve", "solution", or "write" command, including "write 0;", being executed after the changes -- the expressions were not computed correctly.  
  
Fix a bug with "solve; display v;" when v is a defined variable. Under some conditions, v was not recomputed to reflect the results of the solve.  
  
Fix two bugs with redirecting a printing command (display, print, or printf) to a file that cannot be created. The next command could elicit a surprising error messages, such as "... contexts remain open".

## 20141117

Tweak error message for failed evaluations an imported functions to mention "gradient" or "Hessian" if appropriate (i.e., if Errmsg starts with ' or ", in which case the initial ' or " is not printed).  
  
Fix a memory leak with for{...}{...} loops.  
  
Fix a bug with new suffixes returned by solvers: if subsequent commands increased the number of components of the suffixed variable, constraint, or objective beyond the next power of 2, memory corruption could result. In the example behind this bug fix, memory corruption caused the error message "bug: corrupted del mblk arg".

## 20141104

Fix a bug that gave a surprising "presolve has k = ..., P.nfv = ..." message instead of "Solution determined by presolve; ...".

## 20141030

Fix a "yacc stack overflow" that was possible with unusual models.

## 20141024

Fix a glitch with "solexpand": when some but not all members of an array of constraints were dropped, "solexpand" sometimes incorrectly commented that constraints were eliminated by presolve.  
  
Do not regard "q" as "quit" if followed on the same line by other text, other than ";".  
  
Fix a glitch with "not alldiff{...}...".

## 20141020

Redo bug fix with updating dependencies for commands when "solve" or "solution" command within a loop causes a new suffix to be introduced to make the fix work in more cases.

## 20141016

Fix a bug with updating dependencies for commands when "solve" or "solution" command within a loop causes a new suffix to be introduced. In the example that revealed the bug, a command of the form "reset data foo;" appeared to be ignored after the new suffix appeared.  
  
On Unix-like systems, arrange to catch and report surprise SIGPIPE signals.

## 20141013

Relink macosx binaries so licenses can consider both hostname and local hostname.

## 201409256

Fix a possible fault with "let" commands assigning to synonyms, e.g.,  
    let{i in 1 .. \_nvars: \_var\[i\] <= 0} \_var\[i\] := .1;

## 20140925

Fix an fault that arose under unusual and complicated conditions.

## 20140923

Fix a possible fault with  
    # various declarations  
    minimize f: /\* nonlinear expression \*/  
    # more declarations and data  
    display f;  
    solve;

## 20140908

Fix a rarely seen fault (or unpredictable behavior) and a bug that gave rise to the error message "named\_genall called".  
  
ampl.mswin64.\*.zip: update ampltabl\_64.dll so by default it starts tableproxy32.exe rather than tablepxory64.exe (a glitch introduced 20140524 by miscompilation).

## 20140904

Fix a bug with "option substout 1;", which did not detect and cope with circular dependencies. Example:  
    option substout 1;  
    var x; var y = x^2 + 1;  
    s.t. zap: x = y;  
    display y; # printed 0 rather than 1

## 20140828

Fix a glitch seen only on a bizarre MS Windows system that got error message "Bad LOCAL\_MGR = 0.0.0.0" with a floating license. Only the MS Windows bundles are updated. If you have not seen the "Bad LOCAL\_MGR" message, you do not need this update.

## 20140827

Fix a bug revealed by the following example:  
    var x := 3; var y;  
    s.t. ydef: y = x^2 + 1;  
    minimize zot: (y-4)^2;  
    print zot;   # faulted

## 20140711

Fix a glitch in the 64-bit MS Windows binary whereby  
    printf "%x\\n", 0xabcd1234;  
printed "ffffffffabcd1234" rather than "abcd1234".

## 20140704

Fix a fault after the error message "nonconstant left-most expression in double inequality constraint".

## 20140630

Adjust computation of \_ampl\_elapsed\_time, \_shell\_elapsed\_time, \_solve\_elapsed time to reduce roundoff error and, for MS Windows, to report elapsed time rather than CPU time.  
  
Fix glitches with adjustments for some complementarity constraints that could lead to incorrect .nl files with some uses of nonlinear defined variables or to incorrectly reading dual variables from a .sol file.  
  
Fix a bug with \_con\[i\].status that could give "log" instead of "sub".  
  
New option display\_set\_1col is analogous to $display\_1col, but applies to sets: if S is a set with $display\_set\_1col >= card(S), the "display S;" lists each element of S on a separate line. The default value 0 for $display\_set\_1col causes no changes to the hitherto seen behavior of "display S;".

## 20140524

Extend test for "no variables, but lower bound = ..." to fix a glitch with "option presolve 0" (which is often a bad idea) whereby infeasible constraints with no variables were eliminated when defined variables were present. When no defined variables are present, such infeasible constraints are passed to the solver.  
  
ampltabl\*.dll: when tableproxy is used, pass along error messages rather than allowing "table read" to appear to work correctly.

## 20140513

Fix a bug that could corrupt memory after a "solve" when "let" assigns to a variable that is not in the current problem but was declared before a variable that is in the current problem.  
  
Fix a bug with sequences of commands in which the first of two sets that previously had the same value is assigned another value. In some cases a computed value changed when it should not have been affected. Example:  
    set A; set B; set C;  
    set D = A union C;  
    set E = B union C;  
    data; set A := a b c; set B := a b c; set C := x y;  
    display D, E;  
    update data A; data; set A := p q r;  
    display D, E; # E was wrong

## 20140508

Fix a glitch in the hpux-ia64 binaries of 20140407, 20140409, and 20140505.

## 20140505

Fix a bug ("corrupted del\_mblk arg") with some sequences of solves of subscripted problems.

## 20140409

Fix a glitch whereby some commands, such as "fix", that should not require the current problem to be fully instantiated, nonetheless did so, possibly leading to an error message about "no value" for sets or parameters involved with variables, constraints, or objectives not involved with the current command.

## 20140407

Linux binaries relinked to facilitate licensing on some virtual machines. "ampl -v" still shows version 20140331.

## 20140331

Fix a bug (causing an error message "Can't evaluate \_con\[...\]") with "expand \_con;" when logical constraints are present. Use "expand \_logcon" to see the logical constraints before presolve.

## 20140330

Work around Microsoft bugs that caused Infinity^2 to give 0.

## 20140328

Fix a bug with sets that appear in loops and involve defined variables, illustrated by the following example.  
    set K; var x {K}; var y {k in K} = x\[k\];  
    data; set K := 1 2; var x := 1 1 2 0;  
    for{i in 1..2}{  
        display x, y;  
        display {k in K : x\[k\] == 1};  
        display {k in K : y\[k\] == 1};    #was wrong in 2nd iter  
        let x\[2\] := i;  
        }  
Fix a bug with problem declarations involving iterated entities. Changes to things that indirectly affected the sets over which the entities were iterated did not cause the drop/restore state to be updated.  
  
Fix a fault that was possible in interactive sessions with "show x;" after an error message about the wrong number of indices in the declaration of x.

## 20140320

Fix a bug with problems with general complementarity conditions (expr1 >= 0 complements expr2 >= 0 where neither expression is linear in just one variable) and some partially linear nonlinear defined variables. The example that revealed the bug resulted in an invalid .nl file.

## 20140312

Fix a bug (fault) that crept into version 20140220.  
  
Fix a bug with "read" commands in compound statements (e.g., loops) that are executed after a "solve" or "solution" command that introduces new suffixes.  
  
New option cmdtrace: "option cmdtrace 1;" turns on printing of the name of each command executed and, when the command comes from a file other than stdin, the filename and line number of the command.

## 20140226

Update the 32-bit Intel Linux binary after recompiling one source file with -O1 rather than -O2 to bypass a compiler bug.

## 20140224

Fix a bug with defined variables in tables: wrong values may have been transmitted by "write table". Explicitly subscripted defined variables and those with a ".val" suffix were not affected by the bug.  
  
Fix a bug (fault) with "solexpand \_con;".

## 20140220

Fix a bug (error or fault) with "s.t. e: 0; display e.val;". (This was reported as corrected on 20140124, but the fix did not make it into the distributed binaries.)  
  
Improve simplification of piecewise-linear terms: after summing terms applied to the same variable, combine adjacent pieces with the same slope and turn the term into a linear term if only one slope remains. Example:  
    var x;  
    minimize zot: <<1,2;-1,2,-3>>x + sin(x) + <<1,2;1,-2,3>>x;  
    solexpand; # now gives sin(x) rather than something messier  
Add new processing for defined variables whose value is a piecewise-linear expression on a single variable. Now the example  
    var x;  
    var y = 0.5\*x + <<1,2,4;-3,1,-1,2>> x + .7;  
    var z = <<-2.3, -1.55, -.8, 1.7, 3.7; -5, 4, -3, 2, -1, 6>> y;  
    minimize zot: 2\*y;  
    minimize zot2: 3\*z;  
gives the same .nl file (but for roundoff) as  
    var x;  
    minimize zot: 2\*(0.5\*x + <<1,2,4;-3,1,-1,2>> x + .7);  
    minimize zot2: 3\*<<-1.2,-.4,0.6,0.9,1,7/6,5/3,2,3,4,4.2,5.2,6;  
                -15, 2.5, -5, 7.5, -10, 6, -4.5, 3,  
                -1, 1.5, -7.5, 5, -2.5, 15>> x + 4.2;  
For now, at least, the "16" bit of $pl\_linearize suppresses the new processing, i.e., "option pl\_linearize 17" gives the former default behavior, and the "32" bit of $pl\_linearize causes explicit definitions of variables involved in nonconvex (or nonconcave, as appropriate) piecewise-linear terms when this gives a sparser representation. Thus "option pl\_linearize 33" may sometimes result in the output of "solexpand;" being slightly easier to read. Today's changes include recording more pl\_linearize bits, including 4 and 8, which may cause changes to .sol files when nondefault $presolve\_fixeps values matter.

## 20140205

Fix bugs in simplifying logical constraints. The bugs could give an error message about "unexpected nonvariable type" or could result in a .nl file that could cause some solvers to complain about an invalid indicator constraint.

## 20140130

Fix a bug in the processing of a scalar string-valued expression by the \_display and csvdisplay commands: the value should have been quoted when the data-section quoting rules require quoting (e.g., the value looks like a number or contains white space).  
  
Though not previously documented, $csvdisplay\_header = 2 has long caused the csvdisplay command to give headers of the form Expr\_1, Expr\_2, ..., whereas the default ($$csvdisplay\_header = 1) used the declared name when appropriate in the header and used Expr\_n when the n-th item was an expression other than a declared name.

## 20131213

Allow execution to continue after "write 0;" gives an error message about infeasibility.

## 20131212

Fix an infinite loop that was possible in interactive AMPL sessions after an error.  
  
Fix a bug (e.g., fault) that was possible with some instances after "option presolve 0;" following a "solve;" of a larger problem.

## 20131203

Fix a fault that was sometimes possible with named problems.

## 20131122

Fix a bug with "redeclare" that with some commands caused a delay in computing the redeclared value. Example:  
    var x := 1; var y := 2; var z = y^2 + 1;  
    display x, y, z;  
    redeclare var z = 3\*x + 4\*y^2;  
    display x, y, z; # z was wrong  
    display z;       # z was now right

## 20131108

Fix a fault with redeclaring recursive declarations.  
  
Allow "display X;" when X is a param or set indexed over an infinite set and X has a recursive default value. The display just shows the values that so far had to be computed. Example:  
  param f{i in Integers} default if i <= 1 then 1 else i\*f\[i-1\];  
  set S{i in Integers} ordered default  
       if i <= 1 then {1} else S\[i-1\] union {i\*last(S\[i-1\])};  
  display f\[6\], S\[6\], f, S;  

## 20131023

Ignore case in MAC addresses during license checks (an issue rarely seen). When ending execution under a floating license, try to read a reply from the license manager to circumvent bug sometimes seen in MS Windows.

## 20131018

Fix a bug with inserting "\_32" or "\_64" (as appropriate) before the final "." in filenames seen by load commands when the portion of the name before the "." was only one or two characters long (such as "cp.dll"). Alternatively, if a given library name has "\_32" or "\_64" before the final "." and fails to load (perhaps after changing "32" to "64" or vice versa, as appropriate), try omitting the "\_32" or "\_64".  
  
When a solution is read by "solve" or "solution" and no dual variables are present but could have been, and when presolve has removed some constraints, delay the computation of dual variables for the removed constraints until something, such as a request to print dual values, requires them to be computed from the then current primal and dual variable values (possibly left over from a previous "solve" or still at their initial values).

## 20131012

Fix a bug that might have bitten after a "problem" command and before the next "solve" or "solution" command. If the "problem" command changed the constraints to be enforced or variables allowed to vary, if previous commands had caused presolve to run, and if nothing else had caused the need to run presolve again, commands such as printing and "let" commands that involved entities that depend on presolve might have used wrong values of some of those quantities.

## 20131010

Fix a bug with two or more entities indexed over a subscripted set with constant subscripts in the entity declarations. The first-used subscript might have been used instead of the correct subscript in subsequent instantiations of the affected entities.  
  
Have "write ...", including "write 0;", set solve\_result\_num = 299 if presolve finds the problem infeasible.  
  
Fix a rarely seen bug introduced with the changes of 20130408 for option linelim 0. A faulty .nl file was sometimes produced, with defined variables incorrectly ordered. Defined variables may sometimes now appear in a different sequence in the .nl file.

## 20131002

Fix a glitch with "ampl -b4 ..." in the error message for an unavailable solver: part of the error message did not appear. Binaries for MS Windows were not affected.

## 20130926

Fix a bug (eventual fault or worse) with an increase (above the next higher power of 2) in cardinality of the indexing set of a defined variable, some of whose values had been used in printing or other commands.

## 20130921

Fix a possible fault (or worse) with instances having piecewise-linear terms whose linearization caused the number of variables to grow beyond the next power of 2.  
  
Fix a bug unlikely to bother many people: a fault with duplicate false constraints:  
    c: 0; d: 0; display c; # faulted

## 20130906

Fix a bug that kept suffixes on logical constraints from being transmitted to the .nl file.

## 20130903

Fix a fault that was possible with some problem instances involving piecewise-linear terms.

## 20130816

Fix a bug (fault) with several entities (e.g., constraints) using, using iterated quantities, such as sums, over the same subscripted set with a constant subscript.

## 20130815

Adjust 64-bit MS Windows binary to avoid trouble (not yet seen) with "sw" if ever a thread handle cannot be represented in 32 bits.  
  
ampltabl.dll: fix faults with "write table" of a table that in AMPL's view is empty but whose existing file-based version contains at least one row.

## 20130809

Fix a parsing glitch with entities named "end". In some contexts, such as "redeclare", "read table", "reset", "show", "suffix", "update", and "write table", "end" was treated as an "end" command.  
  
Fix a bug (fault) that was possible under some conditions with a set of variables indexed over the empty set.  
  
Fix a bug (wrong values; possible fault) in writing suffix values to .nl files for complementarity constraints involving expressions of more than one variable on both sides of "complements". The .nl file has two constraints for each such complementarity constraint, and both get the same suffix value.

## 20130731

Update the MS Windows binaries to fix a bug with inserting "\_64" or substituting "\_64" for "\_32" in file names given to "load" commands. The bug did not afflict other platforms.

## 20130704

Adjustments for handling problems with >= 2^31 Jacobian nonzeros. New .nl file format codes z, h, and (temporarily, for debugging) B, G, H, and Z. The z format has a "K" section instead of a "k" section; the K section has Jacobian column lengths rather than the the k section's sums of such lengths, permitting entries in the K section to be encoded with 32-bit integers as long as the problem has less than 2^31 variables. (Like the b format, the z format is a binary format that only uses 32-bit integers. The z format uses 2 bytes per operation code rather than 4, so it is somewhat more compact than the b format.) When the b format is requested and the problem has at least 2^31 Jacobian nonzeros, AMPL now uses the z format instead.  
  
The h format is another binary format, one using 64-bit integers, permitting encoding of problems with more than 2^31 variables or constraints. The current AMPL cannot process such large problems, but a later version should be able to do so, at least when appropriately compiled. The h format is available now to permit preparing solvers that can handle it.  
  
Debugging format G is like g, except that it has a K section. Debugging formats B, H, and Z are like b, h, and z, but with reversed byte encoding of binary numbers. (The solver interface library adjusts for byte ordering if necessary, allowing one to generate a binary .nl file on a big-endian machine and solve it on a little-endian machine or vice versa.)  
  
Reading the new formats requires use of versions >= 20130703 of ASL, the AMPL/solver interface library.

## 20130625

Fix trouble introduced 20130624 with the incoming $AMPLFUNC.

## 20130624

Fix more trouble with "load" that may only matter for MS Windows.

## 20130621

Adjust "load", "unload", and "reload" commands to canonicalize library names by simplifying paths and, for MS Windows, changing / to \\. For example, "a/b/../c/foo.dll" becomes "a/c/foo.dll" and "./foo.dll" becomes "foo.dll" in \_LIBS and the associated test for whether the library is already loaded. Nonetheless, "./foo.dll" is sought only in the current directory, whereas "foo.dll" is sought in the directories listed in $ampl\_libpath. It is still possible to load the same library more than once by using a different name for it, either via a hard or symbolic link, by using such variations as "foo.dll", "foo\_32.dll", "foo\_64.dll", or using a name that starts with "../" or otherwise involves enough instances of "/../" to take the apparent name above the current directory. Now \_LIBS reflects the canonicalized names, and possibly simplified full pathnames appear in $AMPLFUNC.  
  
Fix some glitches under MS Windows that, depending on the compiler used, could lead to a "Cannot find" rather than a "Cannot load" error message.

## 20130609

Fix a glitch (fault after two "reset;" invocations after the relevant "load" command) with imported libraries that make no addfunc(...) calls.

## 20130530

Add an error message that symbolic variables are not yet available.  
  
Fix a fault with deleting check commands. Example:  
    param p; check p > 3; delete check 1; # faulted

## 20130510

Fix a glitch with \_ncons, which incorrectly gave the number of algebraic constraints plus the number of logical constraints rather than just the number of algebraic constraints, i.e., \_ncons was high by \_nlogcons.  
  
Not previously noted in the change log are generic synonyms for logical constraints:  
  

<table><tbody><tr><td>Name</td><td>Meaning</td></tr><tr><td>_nlogcons</td><td>number of logical constraints before presolve in the current problem</td></tr><tr><td>_snlogcons</td><td>number of logical constraints after presolve, i.e., as seen by the solver</td></tr><tr><td>_logcon</td><td>indexed by {1 .. _nlogcons}: true (1) or false (0) values of logical constraints before presolve</td></tr><tr><td>_slogcon</td><td>indexed by {1 .. _snlogcons}: true or false values (1 or 0) of logical constraints seen by the solver</td></tr><tr><td>_logconname</td><td>indexed by {1 .. _nlogcons}: names of logical constraints in the current problem</td></tr><tr><td>_slogconname</td><td>indexed by {1 .. _snlogcons}: names of logical constraints seen by the solver</td></tr></tbody></table>

## 20130509

Bundles for MS Windows only: ampltabl.dll updated to avoid a fault when a table specifies an unknown extension and no "User DSN" or "System DSN" entries appear in the MS Windows ODBC Administrator.

## 20130506

Fix a glitch with error recovery: after an error message about "no value for ...", supplying the data and then trying to solve sometimes led to an invalid .nl file. Example (typed on stdin):  
    set I = 1..2; var x{I} >= 0; param p{I};  
    s.t. c: sum{i in I} x\[i\] + sum{i in I} 2\*x\[i\] <= 3;  
    minimize zot: sum{i in I} p\[i\];  
    solve; # error processing objective zot: no value for p\[1\]  
    data; param p := 1 -1 2 -2; solve; # bad line 22 of ....nl  
Fix a glitch giving an "unexpected nonvariable type..." error message when option presolve 0 is unwisely used with certain logical constraints involving "exists" or "forall".

## 20130502

Fix a bug with loop invariants having internal dummy variables. In the following example, the inner sum was moved to the wrong place, giving a fault:  
    set I; set J; set S within {I,J} default {};;  
    param p{i in I} = sum{z in {0}: sum{j in J: (i,j) in S} 1 > 0} 1;  
    let I := 1..10; let J := I;  
    display p;  
In this example, "sum{j in J: (i,j) in S} 1" is a bizarre way of writing what more clearly and efficiently would be written "card{(i,j) in S}"; making this change bypassed the bug, as did changing the inner sum to the clumsier "sum{(i,j) in S} 1".

## 20130501

Fix some bugs (infinite loop, fault, or surprising error message "nonvariable type ... in eput") in simplifying some complicated logical expressions.

## 20130427

Fix a bug with logical constraints: on problems having both logical and algebraic constraints, when presolve eliminated all logical constraints but not all algebraic constraints, a fault was possible. Now, on other problems, "Solution determined by presolve" is more often possible.  
  
Fix a bug with "display \_logcon;" on problems having both logical and arithmetic constraints: wrong values were displayed. The bug did not affect, e.g., "display {i in 1 .. \_nlogcons} \_logcon\[i\];".

## 20130422

Fix a bug (possible fault) with logical constraints when presolve eliminates all of them.

## 20130417

Fix a bug "solve" involving complementarity constraints, followed by "fix" command(s) that remove all complementarity constraints, followed by a "solve": an incorrect .nl file was written for the second "solve".  
  
Fix an optimization bug with tests of the forms  
  
    _expr_ != _numeric\_expression_  
    _expr_ == _numeric\_expression_  
    _numeric\_expression_ != _expr_  
    _numeric\_expression_ == _expr_  
  
If _expr_ was not numeric, the _numeric\_expression_ was not evaluated, so an error in it was not detected. Example:  
    set S = {'abc'}; print{i in S, j in S: i != j+1}: i,j;  
printed "abc abc" rather than complaining that j+1 cannot be evaluated.  
  
Fix an obscure bug with complementarity constraints that led to an error message of the form "presolve has k = _nnn_, P.nfc = _mmm_".

## 20130409

Fix a bug giving "unexpected type 0x960c in augment\_incidence()" with nonlinear defined variables involving an if-then-else expression whose "if" test is constant.

## 20130408

Fix a bug with "option linelim 0;" that affected some complicated examples involving linear and nonlinear defined variables. The linear variables were sometimes evaluated after nonlinear variables that used them, leading to wrong values for the nonlinear defined variables. Note that "option linelim 0" can lead to substantially faster processing of some problems, but makes linear defined variables appears as nonlinear. For some nonlinear solvers, this makes no difference, but it cannot be used with purely linear solvers.  
  
Somewhat improve performance in handling many linear defined variables with the default "option linelim 1". In one example, time to invoke the solver was reduced by 16%.  
  
The "temporary" debugging interpretation of the "4" bit of $linelim, describe in the change-log entry of 20011206 (see, e.g., [https://www.ampl.com/netlib/ampl/changes](https://www.ampl.com/netlib/ampl/changes)), is rescinded. (Version 20130407 had a glitch in this change.)

## 20130327

Fix a bug involving imported functions and defined variables, illustrated by the example:  
    load amplgsl.dll;  
    function gsl\_cdf\_ugaussian\_P;  
    param y default 0;  
    var theta;  
    var z = gsl\_cdf\_ugaussian\_P(theta\*y);  
    display z;  
which said "z = 0" rather than "z = 0.5". The bug was that after 0 was substituted for theta\*y (since y has its default value 0), gsl\_cdf\_ugaussian\_P(0) was ignored.

## 20130326

Update ampltabl.dll in MS Windows bundles to ignore trailing slashes when checking the validity of a DBQ=... string.

## 20130320

Update ampltabl\*.dll in MS Windows bundles to remove a complaint when the DBQ=... in a connection string of the form  
  
'Driver={Microsoft Text Driver (\*.txt; \*.csv)};DBQ=.'  
  
specifies a directory.  
  
Relink MS Windows versions to fix trouble with automatic starting of ampl\_lic on some versions of MS Windows (not XP). It is still recommended not to rely on automatically starting ampl\_lic.

## 20130306

Update the tableproxy\*.exe files in ampl.mswin\*.zip. We missed updating them in April 2012.

## 20130226

Fix a bug with fixing variables that appear in complementarity constraints when the fixing should cause the constraints to be removed by presolve. Example:  
    data;var x{1..7};  
    data;s.t. c{i in 1..6}: x\[i\] >= 0 complements x\[i+1\] >= 0;  
    data;fix{i in 1..3} x\[i\];  
    data;solve; # gave error message "presolve has k = 6, P.nfc = 7"

## 20130222

Fix a bug with multiple t-headers in data sections, leading to error message "irregular : ... : header". Here is an example, previously rejected, of multiple t-headers for set and param data:  
    set ORIG; set DEST; set PROD;  
    set ROUTES within {ORIG,DEST,PROD};  
    param cost{ROUTES};  
  
    data;  
    set ROUTES  
        :  FRA   FRA   DET   DET   LAN   LAN   WIN  
        : bands coils bands coils bands coils bands :=  
    GARY    -     -     -     -     -     +     -  
    CLEV    +     +     +     +     +     +     -  
    PITT    +     -     -     -     -     -     +  
  
        :  WIN   STL   STL   FRE   FRE   LAF   LAF  
        : coils bands coils bands coils bands coils :=  
    GARY    -     -     +     -     -     -     +  
    CLEV    +     +     +     -     -     +     -  
    PITT    -     +     -     +     +     -     - ;  
  
    param cost  
          :  FRA   DET   LAN   WIN   STL   FRE   LAF  
          : bands bands bands bands bands bands bands :=  
    CLEV      27     9    12     .    26     .    17  
    PITT      24     .       .  13    28    99     .  
  
          :  FRA   DET   LAN   WIN   STL   FRE   LAF  
          : coils coils coils coils coils coils coils :=  
    GARY       .     .    11     .    16     .     8  
    CLEV      23     8    10     9    21     .     .  
    PITT       .     .     .     .     .    81     . ;  
  
    set ORIG := GARY CLEV PITT ;  
    set DEST := FRA DET LAN WIN STL FRE LAF ;  
    set PROD := bands coils ;  
  
    display cost;  
Note that there is a mistake on line 4 of p. 476 of the AMPL book: the colon before the first "t-header" should be omitted.

## 20130221

Fix a bug, leading to "unexpected type ... in lsimplify()", with <==> in logical constraints. Example:  
    var x{1..2};  
    s.t. c: x\[1\] == 1 <==> x\[2\] == 2;  
Fix bugs with logical expressions involving "not" (i.e., "!") and inequalities involving NaNs. For example,  
    param p; data; param p := NaN;  
    print if !(p > 3) then "yes" else "no";  
    # incorrectly printed "no"  
Similarly, in the (silly) model  
    var x; s.t. c: 1 < 2 ==> !(x > 4);  
render c as the logical constraint !(x > 4) rather than the arithmetic constraint x <= 4.

## 20130218

Fix a bug in deducing reduced costs involving nonlinear if-then-else expressions whose "if" test has a "count" expression. Such expressions are unlikely in practice, but here is an example:  
    var x := 3;  
    minimize f: if count(sin(x) > .1, cos(x)>.1, tan(x) < -.1) >= 2  
                then x^2 else x^3;  
    display x, f, x.rc;    # x.rc was wrong  
    let x := 3.1;  
    display x, f, x.rc;    # x.rc was accidentally right  
Fix a bug with default expressions for scalar params: if evaluation of the default expression failed, e.g., due to a missing value, the param subsequently appeared to have an unpredictable value. This was only an issue in an interactive session, such as  
    ampl: param a;  
    ampl: param b default a + 1;  
    ampl: print b;  
    Error executing "print" command:  
    errror during evaluation of b:  
        no value for a  
    ampl: print b;  
    0    # a potentially random value  
Add a complaint about integer variables declared with bounds that when rounded (up for the lower bound, down for the upper bound) to integer values are inconsistent. Example:  
    var x integer >= 0.1, <= 0.9;  
    maximize obj: x;  
    solve; display x;  
    # Previously said "Solution determined by presolve;"  
    # now says "Infeasible constraints determined by presolve."

## 20130215

Update ampltabl.dll in bundles for MS Windows to bypass an Excel bug with long names.

## 20130207

Fix a bug with $ampl\_libpath after a command sequence of the form  
    # nontrivial declarations and/or commands  
    reset;  
    reset options;  
    # option ampl\_libpath might now have been bogus

## 20130201

Fix a bug (e.g., fault) with read commands having nested indexings in which an inner indexing involves an outer dummy variable.

## 20130117

Diagnose attempts to add "delete" or "purge" commands to a compound command (e.g., a for or repeat loop) via a "commands" command. Such attempts previously could lead to a fault.

## 20130109

Add an error message about a constraint, objective, or defined variable declaration that has a piecewise-linear expression with a variable in the slope or breakpoint list. In printing commands (display, print, printf), variables can appear in slope and breakpoint lists, but not in declarations.

## 20121224

Fix a possible minor glitch (irrelevant "\_32" or "\_64") in an error message about the failure of a "load" command.

## 20121210

Fix potential trouble (not yet actually seen) with generic synonyms in 64-bit binaries.

## 20121120

Fix bugs (faults) with min() and max(), which now return Infinity and -Infinity, respectively.

## 20121116

When a defined variable involves piecewise-linear terms but is otherwise linear and when convexity (or concavity) permits all appearances of the defined variable in constraints and objectives to be linearized, do so.

## 20121024

Fix a bug with "var ... in ... union integer \[...,...\];", as in  
    var x in {2.5} union integer \[3,5\];  
    minimize zot: (x - 4.3)^2;  
The integer interval was treated as a continuous interval. Now, when appropriate, "var ... in integer \[...,...\] ..." will treat the variable as an integer variable.

## 20121021

Fix a bug (sometimes leading to a surprising "solve\_out:..." error message and/or an invalid .nl file) with problems containing both logical constraints and "var ... in ..." declarations, such as  
    var x{S} in {0, 4, 6};

## 20121017

Fix a bug with a "solve" involving no logical constraints after a solve with one or more logical constraints. The bug could cause a fault or other surprising behavior.

## 20121012

Fix a fault in simplifying logical expressions under complicated conditions.

## 20121005

On Unix-like systems (i.e., not MS Windows), when the initial attempt by the "shell" command to invoke a program using execve() fails and execution via /bin/sh is attempted, also use execve() rather than execv(), to ensure passing the same environment. This change should mostly be invisible.

## 20120911

Fix a bug in simplifying "and", "or", and comparison expressions when the result is constant (true or false). The example revealing the bug was of the form  
    s.t. foo: x == 1 ==> 0 == 0;  
(with one of the zeros being an empty sum).

## 20120831

Fix a glitch that gave rise to error message "sysset\_en\_IN called" in the following command:  
    print if 'foo' in \_AVAILFUNCS then 'yes' else 'no';  
Add Addrandinit to struct AmplExports, which is available to imported functions in al->AE. An imported function or, more likely the funcadd\_ASL function that makes known the imported functions in an imported-function library, can invoke addrandinit(rsi,v) (i.e., ae->Addrandinit(ae,rsi,v)) with apparent signature  
    typedef void (\*RandSeedSetter)(void\*, unsigned long);  
    void addrandinit(RandSeedSetter rsi, void\*);  
to have rsi(v,$randseed) called initially with the current value of $randseed (as an unsigned long) and again whenever option randseed is assigned a value. This is meant to supply a new seed for random functions provided by the containing imported-function library. Like calls on at\_reset() and unlike calls on at\_exit, calls on addrandinit() are forgotten after a "reset;". Note that a "reset;" causes the funcadd\_ASL() routines in all currently loaded imported function libraries to be called again.

## 20120804

Fix a glitch that gave error message "opnumber 243 in opgen" under complicated conditions.

## 20120629

Fix another bug that could only bite after a very large number of commands. Note that using iterated commands, such as iterated "let", "printf", "drop", etc. commands, rather than "for" loops, where appropriate can greatly reduce the number of commands executed and give much faster executions. Using slices suitably sometimes also greatly speeds up execution.

## 20120619

Fix a glitch that gave rise to "bug: corrupted del\_mblk arg" after a very large number of commands.

## 20120614

Fix a bug with piecewise-linear terms. When constraints added to linearize such terms increased the total number of constraints beyond the next power of two, a fault was sometimes possible. _For some platforms, updated AMPL binaries will not be available until about 20120620._

## 20120604

Fix two bugs in handling a problem with logical constraints that get converted to algebraic constraints: an incorrect .nl file was produced, and \_logconname was miscomputed.

## 20120601

Extend warning that variables in subscripts are not yet allowed to most subscripts (not just subscripts on variables).

## 20120530

Fix a bug with option debug\_stub on MS Windows systems.  
  
Fix a bug with error messages in the ODBC table handler that prevented some possibly helpful details from being reported.  
  
Under MS Windows, if $Path does not appear in the incoming environment but $PATH does, use $PATH rather than $Path as the list of directories in which "solve" and "shell" commands should look for programs. Usually $Path is set, but at least some versions of the MinGW shell supply $PATH rather than $Path.

## 20120522

Fix a bug (giving "corrupted del\_mblk arg") in "reset data p;" when p is a scalar param whose current value was computed from a default expression. The bug was exposed (previously harmless) was exposed by the changes of 20120214. Example:  
    param p default 3;  
    reset data p; # OK  
    print p; # value computed from default expression  
    reset data p; # "bug: corrupted del\_mblk arg"  
On MS Windows systems, when process creation fails, report the path to the program that would not start, rather than just the program's name.

## 20120517

Fix a bug (fault) with some logical "atmost" expressions.

## 20120516

Fix a bug with "redeclare" that gave error message "xrenumber bug" when the redeclared entity depended on something declared after something that depended on the entity. Example:  
  
    param p default 6; param q = p + 1;  
    param r = 2\*q; display p, q, r;  
    param s default 3;  
    redeclare param q = p + s + 1; # "xrenumber bug"  
    display q;

## 20120515

On MS Windows systems, if $TMPDIR has a nonblank value, use that value as the temporary directory name (as documented in the AMPL book). Otherwise use the value of $TEMP. Hitherto only $TEMP was considered on MS Windows systems. (On most MS Windows systems, $TMPDIR is not set, but $TEMP is set to a non-blank value by default; on such systems, this change should be invisible.)  
  
On MS Windows systems, fix a glitch with embedded blanks in the value of $TMPDIR or $TEMP (as appropriate). Blanks have long been tolerated in $TMPDIR on other systems.

## 20120507

Add a test to explicitly enforce an implicit limit of 199 on the lengths of names.

## 20120505

Fix a presolve bug with logical constraints (e.g., indicator constraints) that bit under complicated conditions.  
  
Fix a bug in the expand command's processing of a logical constraint that could cause it incorrectly to indicate whether presolve had removed the constraint.

## 20120406

Remove ampl\_libpath from the default \_LOCAL\_OPTIONS (thus making $ampl\_libpath available for possible use by the proxy table handle).  
  
Fix a glitch introduced 20120214 (on Unix-like systems) with a "shell;" command: the AMPL process could die from a SIGTTIN signal.

## 20120328

Fix a bug (possible fault) with variables and constraints indexed over a subscripted set. The fault was only possible if such a variable or constraint had to be regenerated.

## 20120319

Fix a bug (possible fault) in handling very long error messages.  
  
Fix a similar bug with long error messages in the ODBC table handler.  
  
Map NaNs in sets to a specific quiet NaN and fix a bug in testing whether NaN is a set member. Here is an example that now works and previously misbehaved:  
    set S; param p{S}; data; param :S: p := NaN 37; print p\[NaN\];  
Adjust license-check in Linux versions for use with FreeBSD.

## 20120306

Add command-line option --version: when given as the sole command-line argument, --version causes AMPL to print its version and exit, regardless of any needed license file or manager.  
  
Adjust default computation of $ampl\_libdirs to work correctly with non-ASCII directory names (where "ASCII" means "7-bit ASCII"). Note that AMPL has long handled UTF-8 encoding of Unicode, which can involve non-ASCII characters. On MS Windows systems, use of non-ASCII names can cause confusion when different code pages are involved. This is an issue outside the scope of AMPL.  
  
A new "tableproxy" table handler is now available. It permits a 32-bit AMPL to access a 64-bit database and vice versa. It also allows AMPL to access databases on other machines where a tableproxy server is running. For more details, [click here.](https://www.ampl.com/NEW/TABLEPROXY/index.html)

## 20120217

Fix the bug that after, e.g., "display \_VARS;", \_VARS was not updated after subsequent variable declarations or deletions.

## 20120214

Correct the change of 20120208 to handle another case.  
  
On Unix-like systems, add command history processing similar to that of the "sw" program under MS Windows. The up- and down-arrow keys move among the history lines, and the left- and right-arrow keys move left or right one character in the current line. Where available, the "home" key moves to the start of the current line, the "end" key moves to the end of the current line, page-up moves up 10 lines and page-down moves down 10 lines. The control-right-arrow key moves forward one alphanumeric "word", and the control-left-arrow key moves left one "word". Control-W deletes the preceding "word". Control-D sends the current text without ending the line and signals end-of-file when there is no current text. Command history can be turned off by invoking "ampl -vi2 ..."; the -vi2 must come first; invoke  
    ampl "-v?"  
for more on -v options.

## 20120208

Fix an obscure and rarely seen bug that arose under complicated conditions with repeated solves involving several entities having the same indexing when the size of the common index set changed. The example that revealed the bug faulted.

## 20120131

Fix a possible fault during startup that could happen with version 20120126 on Unix-like systems.  
  
Fix a bug in simplifying a piecewise-linear term applied to a variable with a negative upper bound greater than the first negative breakpoint when the term has only two negative breakpoints and at least one positive one (after simplification for common slopes). Wrong information was transmitted to the solver.

## 20120126

Fix glitches with \_obj.sense.  
  
Adjust "load" command to facilitate using a 32-bit AMPL binary with a 64-bit solver binary or vice versa: for a 64-bit AMPL, if the library name involves '.' and the final '.' is preceded by "\_32", change the "32" to "64". Otherwise, if the library fails to load and there is a '.' in the name, insert "\_64" before the final '.' unless it is already preceded by "\_64". (For a 32-bit AMPL, the rules are similar, with the roles of "32" and "64" reversed.) The builtin set \_LIBS still shows the names by which libraries were loaded, whereas option AMPLFUNC reflects the adjusted names. The unload command operates on names in \_LIBS. Temporarily, at least, you can suppress the new behavior by specifying "option map\_32\_64 0;".  
  
Under MS Windows, add a test to the "load" command to ignore shared libraries (DLLs) compiled for the wrong number of address bits. (With more sensible operating systems, such libraries simply fail to load.)  
  
Fix a bug with option AMPLFUNC: after a sequence of the form  
    load 'something';  
    load 'more';  
    unload 'something'; # or 'more'  
    load 'another';  
option AMPLFUNC did not show the new library.  
  
Change the default value for $ampl\_libpath from "" to the directory containing the AMPL binary and (if different) the current directory. Absent command-line option -i (invoke ampl "-i?" for details), or an incoming $AMPLFUNC value, look for both amplfunc.dll and ampltabl.dll at startup by the AMPL search rules (rather, for ampltabl.dll, than by system-dependent rules).

## 20120117

Fix a glitch that caused the unload command not to fully unload the specified library. It's not clear whether this ever caused any visible symptoms other perhaps than some memory not being reclaimed.  
  
New builtin suffix ".sense\_num" on objectives is -1 for minimization and 1 for maximization. New builtin suffix ".sense" is a symbolic version of ".sense\_num" with default values "minimize" and "maximize" given by option sense\_table.

## 20120104

Fix a bug that could lead to an error message of the form "presolve has k = 11, P.nfc = 17".

## 20111229

Relink for use with single-user licenses.

## 20111216

For the -ix command-line option, in addition to allowing multiple files on separate lines of a suitably quoted x, allow multiple files on the same line if each file name is enclosed in single or double quotes. Add a brief explanation of multiple files to the "-i?" output.  
  
Fix a bug (introduced 20110531) with "option substout 1": an incorrect .nl file was sometimes generated when several constraints could be chosen to define a particular variable. Here is an example in which the bug bit, giving a .nl file incorrectly containing "nonlinear" constraints:  
    option substout 1;  
    var x >= 3;  
    var y{i in 1..2} >= i;  
    var z;  
    var v = z + 3;  
    var w = v + x;  
    s.t. c{i in 1..2}: z = x + i\*y\[i\];  
    minimize foo: x + z;  

## 20111121

Fix a bug with testing membership in "system sets", i.e., any of \_CONS, \_ENVS, \_FUNCS, \_LOGCONS, \_OBJS, \_PARS, \_PROBS, \_RANDVARS, \_SETS, \_SUFFIXES, \_SYMVARS, \_SYSTEM\_SUFFIXES, \_TABLES, \_VARS or \_VARSETS. The test sometimes came out wrong. Example:  
    reset; print if 'XX' in \_SETS then 'yes' else 'no';  
    # printed yes rather than no  
Add a warning about "data;" not being allowed in a compound command. Other error messages are likely to appear after the new warning. Note that "data filename;" and "data (filename\_expr);" may appear in a compound statement.

## 20111110

Fix bugs (giving a surprising error message or fault) with updating sets over which subscripted objectives and problems are indexed.

## 20111107

Supply missing initialization of SnprintF and VsnprintF in the AmplExports structure passed to imported functions and table handlers. (They have long been provided to imported functions used by solvers.)  
  
When imported functions or table handlers see ae->ASLdate >= 20111028 and ae->asl == 0, ae->Getenv(0) returns a char\*\* value for the complete current environment.  
  
On Unix-like systems, set FD\_CLOEXEC when opening files, to prevent child processes (e.g., from "solve" or "shell" commands) from seeing irrelevant open file descriptors, a bit of tidiness seldom relevant in practice.  
  
Fix the obscure glitch that prompts were preceded by # after reading a file that ended in an incomplete #comment line (one without a terminating newline character). The # persisted until the next complete comment had been read. Now the # should only appear if you manually enter an incomplete comment (e.g., under Unix or Linux, by typing control-D at the end of a # comment line).  
  
Fix a bug (e.g., fault) that bit under complicated conditions, e.g., with solving sequences of named problems.  
  
Permit use of single-user licenses.

## 20111016

Fix more variable-reordering trouble with redeclare (not caught by yesterday's example). Example:  
    var w; var x; var y; var z;  
    minimize foo: w + 2\*x + 3\*y + 4\*z;  
    s.t. c1: x + 5\*y <= 37;  
    s.t. c2: y + 6\*z >= 43;  
    s.t. c3: 4 <= z + 7\*x <= 19;  
    expand;  
    redeclare var y = x^2 + z; # "xrenumber bug" with version 20111015  
    expand; # wrong constraint c3 prior to 20111015  

## 20111015

Fix a bug sometimes seen with "show" after a redeclaration: wrong variable names were sometimes reported (depending on details of the redeclaration). Example:  
    var x; var y;  
    minimize zap: x + y;  
    s.t. C: 2\*y <= 5;  
    expand C; # OK  
    param p default 2;  
    redeclare s.t. C: p\*y <= 5;  
    expand C; # mentioned x rather than y  

## 20111011

Fix a glitch with the values of \_solve\_elapsed\_time and \_shell\_elapsed\_time under Linux.

## 20111005

Allow "ampl -R" (server mode) to use imported functions provided by "load" commands (but not pipe functions).

## 20111003

When processing ampl.lic, ignore new keywords for ampl.netlic.

## 20110913

Fix a rarely seen bug that caused a fault in recent 32-bit Windows binaries.

## 20110909

Fix a memory leak seen in a script involving a number of solves of large problems.  
  
Arrange for printing variables not to require instantiating constraints. With some command sequences, "ampl -t ..." or "ampl -T ..." or the equivalent "option times 1;" or "option gentimes 1;" will produce less output than before.

## 20110908

Fix a bug with complementarity constraints. With certain (somewhat rare) problem dimensions, an incorrect .nl file was generated. An example where this bug bit:  
    var x {1..2} >= 0; minimize obj: x\[1\] + x\[2\];  
    subj to con: x\[1\] <= 3 complements x\[2\] <= 5;

## 20110906

Extend "option show\_stats 1" output to list the numbers (if nonzero) of equality, inequality, and range (i.e., double inequality) constraints.  
  
On Unix-like systems, add command-line option -g to start in a new process group. For a summary of command-line options, invoke "ampl -?" or "ampl --help".  
  
Extend option relax\_integrality to apply to binary variables introduced to handle "in union\_of\_intervals" phrases in variable declarations.

## 20110901

Fix a parsing bug ("syntax error") seen in the following example:  
    param p; var x{1..2};  
    minimize zot: sum{i in 1..2} (1-x\[i\])^2;  
    data goo.dat;  
    if p > 3 then commands goo1.mod;  
    expand;  
  
Changing "expand;" to "expand ;" or ";expand;" worked around the bug.

## 20110825

Fix a parsing bug: an include phrase following an "if" command that could be followed by an "else" command (which might be in the included file), but is followed by something else was mishandled.

## 20110813

Fix glitches in "show f;" when f is a pipe function.  
  
Fix a fault with empty slices that arose under rare conditions.  
  
In equality constraints in which one side involves numeric variables, assume the other side must also be numeric. This matters when the other side involves an if-then-else expressions whose "then" or "else" expression consists only of a dummy variable, such as  
    set I := 1..2; var x{I}; var y{I};  
    subject to c{i in I}: x\[i\] = if i == 1 then y\[i\]  
                else if i == 2 then i;  
which previously was treated as a logical constraint. (Changing "then i" to "then i + 0" was necessary to make constraint c into an algebraic constraint.)

## 20110725

Fix a bug with redeclarations involving variables. Input of the form  
    # ...  
    write bfoo1;  
    var newvar;  
    redeclare minimize o: ... /\* involving newvar \*/;  
    write bfoo2;  
could have resulted in an incorrect foo2.nl.

## 20110722

Fix some bugs with logical constraints. Problem commands did not cause logical constraints to be dropped or restored when they should have been. The "delete suffix ..." command ignored logical constraints. The "drop;" command did not show dropped logical constraints. The "delete lcon;" command, for lcon a logical constraint, misbehaved. For a logical constraint lcon, "expand lcon;" and "solexpand lcon;" sometimes printed an extraneous Infinity.

## 20110713

Change the default computation of c.slack for a complementary constraint of the form  
    c: L <= expr1 <= U complements expr2  
with L and U finite to  
    min(expr1 - L, U - expr1,  
        if expr1 <= 0.5\*(L+U) then expr2 else -expr2)  
Setting new option $old\_complementarity\_slack to 1 restores the old computation:  
    min(expr1 - L, U - expr1,  
        if expr1 <= L then expr2  
        else if expr1 >= U then -expr2  
        else -abs(expr2))  
The new default computation is more useful than the old when an interior-point algorithm is used. With it, a slack value of zero means the constraint is satisfied exactly, a small positive value is a complementarity violation, and a negative value is a constraint violation. Unless we hear feedback that having option old\_complementarity\_slack is useful, this new option may eventually be withdrawn.  
  
When writing a .nl file after a solve or solution command, i.e., when primal or dual values for implicit variables or constraints are available, include their values, if nonzero, with the primal or dual initial guess.  
  
Fix glitches in "expand cc;" and "solexpand cc;", where cc is a complementarity constraint: bounds were sometimes not shown.  
  
Add two numbers to line 3 of the .nl header when complementarities are present: nd = number of "double" complementarities, i.e., those involving a double inequality, such as  
    L <= expr <= U complements expr1  
  
and nzlb = number of complemented variables with a nonzero lower bound. The new numbers are used in a new facility soon to be added to the AMPL/ solver interrface library for optionally modifying complementarity conditions to v1 >= 0 complements v2 >= 0. (With older versions of AMPL, the facility uses upper bounds on nd and nzlb.)

## 20110630

Omit "Highest address used = ..." from "Too much memory" message; the "highest address" seems pointless when virtual memory is used.  
  
Fix two bugs in handling complementarity constraints. In a command-line invocation of the form  
    ampl -obfoo foo.mod foo.dat  
complementarities might sometimes have been misidentified, and "complementarities" of the form v complements expr1 == expr2 (which should just be simplified to expr1 == expr2) may have been conveyed as complementarities (which seemed not to bother the "path" solver).

## 20110614

Fix a glitch in computing Jacobian sparsity in some problems in which a nonlinear defined variable appears linearly in a nonlinear constraint and "option substout 1" is specified. Example:  
    set I = 1..2; var x{I}; var y{I};  
    s.t. c1: y\[1\] = x\[1\] + 1;  
    s.t. ydef: y\[2\] = y\[1\] + x\[2\] - x\[1\];  
    minimize zot: y\[2\]^2;  
    s.t. bletch{i in I}: x\[i\]\*y\[i\] >= 3;  
With $substout = 1, bletch\[2\] was incorrectly indicated to depend on x\[1\]. Aside from sparsity issues, this was harmless.

## 20110531

Adjust processing for $substout=1 to allow mutually recursive variable definitions from several indexed defining constraints.

## 20110527

Relink to permit a quoted "hostname" for MGR\_IP in the ampl.lic file for a floating license.

## 20110524

Fix a bug (fault or worse) with some models having both defined variables and logical constraints.  
  
Fix a bug in simplifying logical constraints with constant logical expressions; the wrong truth value sometimes appeared in a platform- dependent way.

## 20110426

Tweak license checker to correct a rare problem on MS Windows systems.

## 20110419

Fix a fault in the "objective" command that was possible with some forms of iterated objectives. Example:    
    set A dimen 2; var x;  
    minimize Obj{(i,'N') in A}: x^i;  
    data; set A := 1 x 2 N;  
    objective; # faulted

## 20110413

Fix a fault that could arise in a complicated example with fixing and unfixing a defined variable within a bigger loop. Such fixing and unfixing is not allowed, but in the example, the bug bit before an error message about the inappropriate operation was issued.

## 20110321

Fix "sd botch in ordered\_genall" in the following example:  
   
    set S ordered by 1..10 default 1..10; display S;

## 20110306

Fix glitches with iterated columns in table declarations, i.e., with  
   
    indexing < colg\_1 \[, colg\_2, ...\] >   
The indexing set was treated as the empty set in some situations, which might have caused "read table" not to read the columns in question or have caused "write table" to fault.  
  
Fix a glitch in the processing of "include filename" where filename is not quoted. If a nonblank character immediately followed filename, as in "include foo;" (in which semicolon is the nonblank character), that character was sometimes seen at the wrong time. For example, "if 1 < 0 then include f;" was treated as "if 1 < 0 then; include f". (Recall that an include phrase, such here as "include f", is processed before parsing; that is, "include" is unaware of the context in which it appears.)

## 20110222

Fix a bug with solexpand applied to a defining constraint: a spurious "complements" sometimes appeared and a constant term was possibly lost.

## 20110219

Fix a rarely seen bug that caused a fault in a complicated example.  
  
Fix a bug in "table write": symbolic params with numeric values were sometimes treated as having the corresponding string value.  
  
Add an error message for table declarations that involve row-index dummy variables in OUT or INOUT columns and do not specify "set -->" or "set <-->", as in the following example.  
   
    set S; set T = 1..4; param p{S,T};  
    table goo:  
     S <-- \[r ~ R\], {t in T} < p\[r,t\] ~ ("col" & t) >;   
Previously "write table goo" faulted (but worked fine with "S <--" changed to "S <-->" or "S -->").

## 20110121

Fix a rarely seen parse error on a command after an in-line data section.  
  
Add warning that variables in subscripts are not yet allowed.

## 20110112

Fix a rarely seen bug (fault) that bit under the "right" conditions when making adjustments for new suffixes.

# Older changes

Two logs of changes and fixes are available from the [AMPL netlib directory](https://www.ampl.com/netlib/ampl/index.html):

-   **[Changes and recent bug fixes](https://www.ampl.com/netlib/ampl/changes):** A summary of all changes and extensions to AMPL since publication of the AMPL book, plus the last several months’ bug fixes.
-   **[Complete changes and bug fixes](https://www.ampl.com/netlib/ampl/fixlog):** A listing of all changes and bug fixes since 30 November 1992.
