
# CBC Options

```
dualB(ound) : Initially algorithm acts as if no gap between bounds exceeds this value
The dual algorithm in Clp is a single phase algorithm as opposed to
a two phase algorithm where you first get feasible then optimal. 
If a problem has both upper and lower bounds then it is trivial to
get dual feasible by setting non basic variables to correct bound.
If the gap between the upper and lower bounds of a variable is more
than the value of dualBound Clp introduces fake bounds so that it
can make the problem dual feasible.  This has the same effect as a
composite objective function in the primal algorithm.  Too high a
value may mean more iterations, while too low a bound means the code
may go all the way and then have to increase the bounds.  OSL had
a heuristic to adjust bounds, maybe we need that here.
<Range of values is 1e-20 to 1e+12;
	current 1e+10>

dualT(olerance) : For an optimal solution no dual infeasibility may exceed this value
Normally the default tolerance is fine, but one may want to increase
it a bit if the dual simplex algorithm seems to be having a hard time.
One method which can be faster is to use a large tolerance e.g. 1.0e-4
and the dual simplex algorithm and then to clean up the problem using
the primal simplex algorithm with the correct tolerance (remembering
to switch off presolve for this final short clean up phase).
<Range of values is 1e-20 to 1.79769e+308;
	current 1e-07>

primalT(olerance) : For a feasible solution no primal infeasibility, i.e., constraint violation, may exceed this value
Normally the default tolerance is fine, but one may want to increase
it a bit if the primal simplex algorithm seems to be having a hard
time.
<Range of values is 1e-20 to 1.79769e+308;
	current 1e-07>

primalW(eight) : Initially algorithm acts as if it costs this much to be infeasible
The primal algorithm in Clp is a single phase algorithm as opposed
to a two phase algorithm where you first get feasible then optimal.
So Clp is minimizing this weight times the sum of primal infeasibilities
plus the true objective function (in minimization sense).  Too high
a value may mean more iterations, while too low a value means the
algorithm may iterate into the wrong directory for long and then has
to increase the weight in order to get feasible.
<Range of values is 1e-20 to 1.79769e+308;
	current 1e+10>

psi : Two-dimension pricing factor for Positive Edge criterion
The Positive Edge criterion has been added to select incoming variables
to try and avoid degenerate moves. Variables not in the promising
set have their infeasibility weight multiplied by psi, so 0.01 would
mean that if there were any promising variables, then they would always
be chosen, while 1.0 effectively switches the algorithm off. There
are two ways of switching this feature on.  One way is to set psi
to a positive value and then the Positive Edge criterion will be used
for both primal and dual simplex.  The other way is to select PEsteepest
in dualpivot choice (for example), then the absolute value of psi
is used. Code donated by Jeremy Omer.  See Towhidi, M., Desrosiers,
J., Soumis, F., The positive edge criterion within COIN-OR's CLP;
Omer, J., Towhidi, M., Soumis, F., The positive edge pricing rule
for the dual simplex.
<Range of values is -1.1 to 1.1;
	current -0.5>

zeroT(olerance) : Kill all coefficients whose absolute value is less than this value
This applies to reading mps files (and also lp files if KILL_ZERO_READLP
defined)
<Range of values is 1e-100 to 1e-05;
	current 1e-20>

allow(ableGap) : Stop when gap between best possible and best less than this
If the gap between best known solution and the best possible solution
is less than this value, then the search will be terminated.  Also
see ratioGap.
<Range of values is 0 to 1.79769e+308;
	current 0>

cuto(ff) : Bound on the objective value for all solutions
All solutions must have a better objective value (in a minimization
sense) than the value of this option.  CBC also updates this value
whenever it obtains a solution to the value of the objective function
of the solution minus the cutoff increment.
<Range of values is -1.79769e+308 to 1.79769e+308;
	current 1e+50>

inc(rement) : A valid solution must be at least this much better than last integer solution
Whenever a solution is found the bound on the objective value for
new solutions is set to the      objective function of the found solution
(in a minimization sense) plus this.  If it is not set then CBC will
try and work one out, e.g. if all objective coefficients are multiples
of 0.01 and only integer variables have entries in the objective function,
then the increment can be set to 0.01.  Be careful if setting this
to a negative value!
<Range of values is -1.79769e+308 to 1.79769e+308;
	current 1e-05>

integerT(olerance) : For a feasible solution no integer variable may be more than this away from an integer value
Beware of setting this smaller than the primal feasibility tolerance.
<Range of values is 1e-20 to 0.5;
	current 1e-07>

preT(olerance) : Tolerance to use in presolve
One may want to increase this tolerance if presolve says the problem
is infeasible and one has awkward numbers and is sure that the problem
is really feasible.
<Range of values is 1e-20 to 1.79769e+308;
	current 1e-08>

pumpC(utoff) : Fake cutoff for use in feasibility pump
A value of 0.0 means off. Otherwise, add a constraint forcing objective
below this value in feasibility pump
<Range of values is -1.79769e+308 to 1.79769e+308;
	current 0>

ratio(Gap) : Stop when gap between best possible and best known is less than this fraction of larger of two
If the gap between the best known solution and the best possible solution
is less than this fraction of the objective value at the root node
then the search will terminate.  See 'allowableGap' for a way of using
absolute value rather than fraction.
<Range of values is 0 to 1.79769e+308;
	current 0>

sec(onds) : maximum seconds
After this many seconds coin solver will act as if maximum nodes had
been reached.
<Range of values is -1 to 1.79769e+308;
	current 1e+08>

force(Solution) : Whether to use given solution as crash for BAB
-1 off.  If 1 then tries to branch to solution given by AMPL or priorities
file. If 0 then just tries to set as best solution If >1 then also
does that many nodes on fixed problem.
<Range of values is -1 to 20000000;
	current -1>

idiot(Crash) : Whether to try idiot crash
This is a type of 'crash' which works well on some homogeneous problems.
It works best on problems with unit elements and rhs but will do something
to any  model.  It should only be used before the primal simplex algorithm.
It can be set to -1 when the code  decides for itself whether to use
it, 0 to switch off, or n > 0 to do n passes.
<Range of values is -1 to 2147483647;
	current -1>

maxF(actor) : Maximum number of iterations between refactorizations
If this is left at its default value of 200 then CLP will guess a
value to use.  CLP may decide to re-factorize earlier for accuracy.
<Range of values is 1 to 2147483647;
	current 200>

maxIt(erations) : Maximum number of iterations before stopping
This can be used for testing purposes.  The corresponding library
call
	setMaximumIterations(value)
can be useful.  If the code stops on seconds or by an interrupt this
will be treated as stopping on maximum iterations.  This is ignored
in branchAndCut - use maxN!odes.
<Range of values is 0 to 2147483647;
	current 2147483647>

output(Format) : Which output format to use
Normally export will be done using normal representation for numbers
and two values per line.  You may want to do just one per line (for
grep or suchlike) and you may wish to save with absolute accuracy
using a coded version of the IEEE value. A value of 2 is normal. otherwise
odd values gives one value per line, even two.  Values 1,2 give normal
format, 3,4 gives greater precision, while 5,6 give IEEE values. 
When used for exporting a basis 1 does not save values, 2 saves values,
3 with greater accuracy and 4 in IEEE.
<Range of values is 1 to 6;
	current 2>

randomS(eed) : Random seed for Clp
Initialization of the random seed for pseudo-random numbers used to
break ties in degenerate problems. This may yield a different continuous
optimum and, in the context of Cbc, different cuts and heuristic solutions.
The special value of 0 lets CLP use the time of the day for the initial
seed.
<Range of values is 0 to 2147483647;
	current 1234567>

slog(Level) : Level of detail in (LP) Solver output
If 0 then there should be no output in normal circumstances.  1 is
probably the best value for most uses, while 2 and 3 give more information.
This parameter is only used inside MIP - for Clp use 'log'
<Range of values is -1 to 63;
	current 1>

sprint(Crash) : Whether to try sprint crash
For long and thin problems this method may solve a series of small
problems created by taking a subset of the columns.  The idea as 'Sprint'
was introduced by J. Forrest after an LP code of that name of the
60's which tried the same tactic (not totally successfully).  CPLEX
calls it 'sifting'.  -1 lets CLP automatically choose the number of
passes, 0 is off, n is number of passes
<Range of values is -1 to 2147483647;
	current -1>

cutD(epth) : Depth in tree at which to do cuts
Cut generators may be off, on, on only at the root node, or on if
they look useful.       Setting this option to a positive value K
let CBC call a cutgenerator on a node whenever the depth in the tree
is a multiple of K.       The default of -1 lets CBC decide.
<Range of values is -1 to 2147483647;
	current -1>

cutL(ength) : Length of a cut
At present this only applies to Gomory cuts. -1 (default) leaves as
is. Any value >0 says that all cuts <= this length can be generated
both at root node and in tree. 0 says to use some dynamic lengths.
If value >=10,000,000 then the length in tree is value%10000000 -
so 10000100 means unlimited length at root and 100 in tree.
<Range of values is -1 to 2147483647;
	current -1>

depth(MiniBab) : Depth at which to try mini branch-and-bound
Rather a complicated parameter but can be useful. -1 means off for
large problems but on as if -12 for problems where rows+columns<500,
-2 means use Cplex if it is linked in.  Otherwise if negative then
go into depth first complete search fast branch and bound when depth>=
-value-2 (so -3 will use this at depth>=1).  This mode is only switched
on after 500 nodes.  If you really want to switch it off for small
problems then set this to -999.  If >=0 the value doesn't matter very
much.  The code will do approximately 100 nodes of fast branch and
bound every now and then at depth>=5.  The actual logic is too twisted
to describe here.
<Range of values is -2147483647 to 2147483647;
	current -1>

hot(StartMaxIts) : Maximum iterations on hot start
<Range of values is 0 to 2147483647;
	current 100>

log(Level) : Level of detail in Coin branch and Cut output
If 0 then there should be no output in normal circumstances.  1 is
probably the best value for most uses, while 2 and 3 give more information.
<Range of values is -63 to 63;
	current 1>

maxN(odes) : Maximum number of nodes to do
This is a repeatable way to limit search.  Normally using time is
easier but then the results may not be repeatable.
<Range of values is -1 to 2147483647;
	current 2147483647>

maxSaved(Solutions) : Maximum number of solutions to save
Number of solutions to save.
<Range of values is 0 to 2147483647;
	current -1>

maxSo(lutions) : Maximum number of feasible solutions to get
You may want to stop after (say) two solutions or an hour.  This is
checked every node in tree, so it is possible to get more solutions
from heuristics.
<Range of values is 1 to 2147483647;
	current -1>

passC(uts) : Number of rounds that cut generators are applied in the root node
The default is to do 100 passes if the problem has less than 500 columns,
100 passes (but stop if the drop in the objective function value is
small) if the problem has less than 5000 columns, and 20 passes otherwise.
A negative value -n means that n passes are also applied if the objective
does not drop.
<Range of values is -2147483647 to 2147483647;
	current 20>

passF(easibilityPump) : How many passes to do in the Feasibility Pump heuristic
<Range of values is 0 to 10000;
	current 30>

passT(reeCuts) : Number of rounds that cut generators are applied in the tree
The default is to do one pass. A negative value -n means that n passes
are also applied if the objective does not drop.
<Range of values is -2147483647 to 2147483647;
	current 1>

pumpT(une) : Dubious ideas for feasibility pump
This fine tunes Feasibility Pump 
	>=10000000 use as objective weight switch
	>=1000000 use as accumulate switch
	>=1000 use index+1 as number of large loops
	==100 use objvalue +0.05*fabs(objvalue) as cutoff OR fakeCutoff if
set
	%100 == 10,20 affects how each solve is done
	1 == fix ints at bounds, 2 fix all integral ints, 3 and continuous
at bounds. If accumulate is on then after a major pass, variables
which have not moved are fixed and a small branch and bound is tried.
<Range of values is 0 to 100000000;
	current 1005043>

randomC(bcSeed) : Random seed for Cbc
Allows initialization of the random seed for pseudo-random numbers
used in heuristics such as the Feasibility Pump to decide whether
to round up or down. The special value of 0 lets Cbc use the time
of the day for the initial seed.
<Range of values is -1 to 2147483647;
	current -1>

slow(cutpasses) : Maximum number of rounds for slower cut generators
Some cut generators are fairly slow - this limits the number of times
they are tried.      The cut generators identified as 'may be slow'
at present are Lift and project cuts and both versions of Reduce and
Split cuts.
<Range of values is -1 to 2147483647;
	current 10>

strat(egy) : Switches on groups of features
This turns on newer features. Use 0 for easy problems, 1 is default,
2 is aggressive. 1 uses Gomory cuts with a tolerance of 0.01 at the
root node, does a possible restart after 100 nodes if many variables
could be fixed, activates a diving and RINS heuristic, and makes the
feasibility pump more aggressive.
<Range of values is 0 to 2;
	current 1>

strong(Branching) : Number of variables to look at in strong branching
In order to decide which variable to branch on, the code will choose
up to this number of unsatisfied variables to try minimal up and down
branches on.  Then the most effective one is chosen. If a variable
is branched on many times then the previous average up and down costs
may be used - see also option trustPseudoCosts.
<Range of values is 0 to 2147483647;
	current 5>

trust(PseudoCosts) : Number of branches before we trust pseudocosts
Using strong branching computes pseudo-costs.  This parameter determines
after how many branches for a variable we just trust the pseudo costs
and do not do any more strong branching.
<Range of values is -3 to 2147483647;
	current 5>

allC(ommands) : Whether to print less used commands
For the sake of your sanity, only the more useful and simple commands
are printed out on ?.
<Possible options for allCommands are: no more all;
	current  no>

chol(esky) : Which cholesky algorithm
For a barrier code to be effective it needs a good Cholesky ordering
and factorization.  The native ordering and factorization is not state
of the art, although acceptable.  You may want to link in one from
another source.  See Makefile.locations for some possibilities.
<Possible options for cholesky are: native dense fudge(Long_dummy) wssmp_dummy Uni(versityOfFlorida_dummy) Taucs_dummy Mumps_dummy Pardiso_dummy;
	current  native>

crash : Whether to create basis for problem
If crash is set to 'on' and there is an all slack basis then Clp will
flip or put structural     variables into the basis with the aim of
getting dual feasible.  On average, dual simplex seems to perform
better without it and there are alternative types of 'crash' for primal
simplex, e.g. 'idiot' or 'sprint'.     A variant due to Solow and
Halim which is as 'on' but just flips is also available.
<Possible options for crash are: off on so(low_halim) lots idiot1 idiot2 idiot3 idiot4 idiot5 idiot6 idiot7;
	current  off>

cross(over) : Whether to get a basic solution with the simplex algorithm after the barrier algorithm finished
Interior point algorithms do not obtain a basic solution. This option
will crossover to a basic solution suitable for ranging or branch
and cut.  With the current state of the solver for quadratic programs
it may be a good idea to switch off crossover for this case (and maybe
presolve as well) - the option 'maybe' does this.
<Possible options for crossover are: on off maybe presolve;
	current  on>

direction : Minimize or Maximize
The default is minimize - use 'direction maximize' for maximization.
You can also use the parameters 'maximize' or 'minimize'.
<Possible options for direction are: min(imize) max(imize) zero;
	current  min(imize)>

error(sAllowed) : Whether to allow import errors
The default is not to use any model which had errors when reading
the mps file.  Setting this to 'on' will allow all errors from which
the code can recover simply by ignoring the error.  There are some
errors from which the code can not recover e.g. no ENDATA.  This has
to be set before import i.e. -errorsAllowed on -import xxxxxx.mps.
director<Possible options for errorsAllowed are: off on;
	current  off>

fact(orization) : Which factorization to use
The default is to use the normal CoinFactorization, but other choices
are a dense one, OSL's, or one designed for small problems.
<Possible options for factorization are: normal dense simple osl;
	current  normal>

keepN(ames) : Whether to keep names from import
It saves space to get rid of names so if you need to you can set this
to off.  This needs to be set before the import of model - so -keepnames
off -import xxxxx.mps.
<Possible options for keepNames are: on off;
	current  on>

mess(ages) : Controls if Clpnnnn is printed
The default behavior is to put out messages such as:
Clp0005 2261  Objective 109.024 Primal infeas 944413 (758)
but this program turns this off to make it look more friendly.  It
can be useful to turn them back on if you want to be able to 'grep'
for particular messages or if you intend to override the behavior
of a particular message.  This only affects Clp not Cbc.
<Possible options for messages are: off on;
	current  off>

perturb(ation) : Whether to perturb the problem
Perturbation helps to stop cycling, but CLP uses other measures for
this.  However, large problems and especially ones with unit elements
and unit right hand sides or costs benefit from perturbation.  Normally
CLP tries to be intelligent, but one can switch this off.
<Possible options for perturbation are: on off;
	current  on>

presolve : Whether to presolve problem
Presolve analyzes the model to find such things as redundant equations,
equations which fix some variables, equations which can be transformed
into bounds, etc.  For the initial solve of any problem this is worth
doing unless one knows that it will have no effect.  Option 'on' will
normally do 5 passes, while using 'more' will do 10.  If the problem
is very large one can let CLP write the original problem to file by
using 'file'.
<Possible options for presolve are: on off more file;
	current  on>

printi(ngOptions) : Print options
This changes the amount and format of printing a solution:
normal - nonzero column variables 
integer - nonzero integer column variables
special - in format suitable for OsiRowCutDebugger
rows - nonzero column variables and row activities
all - all column variables and row activities.

For non-integer problems 'integer' and 'special' act like 'normal'.
Also see printMask for controlling output.
<Possible options for printingOptions are: normal integer special rows all csv bound(ranging) rhs(ranging) objective(ranging) stats boundsint boundsall fixint fixall;
	current  normal>

scal(ing) : Whether to scale problem
Scaling can help in solving problems which might otherwise fail because
of lack of accuracy.  It can also reduce the number of iterations.
It is not applied if the range of elements is small.  When the solution
is evaluated in the unscaled problem, it is possible that small primal
and/or dual infeasibilities occur. Option 'equilibrium' uses the largest
element for scaling. Option 'geometric' uses the squareroot of the
product of largest and smallest element. Option 'auto' let CLP choose
a method that gives the best ratio of the largest element to the smallest
one.
<Possible options for scaling are: off equi(librium) geo(metric) auto(matic) dynamic rows(only);
	current  auto(matic)>

timeM(ode) : Whether to use CPU or elapsed time
cpu uses CPU time for stopping, while elapsed uses elapsed time. (On
Windows, elapsed time is always used).
<Possible options for timeMode are: cpu elapsed;
	current  cpu>

clique(Cuts) : Whether to use Clique cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
Reference: https://github.com/coin-or/Cgl/wiki/CglClique
<Possible options for cliqueCuts are: off on root ifmove forceOn onglobal;
	current  ifmove>

combine(Solutions) : Whether to use combine solution heuristic
This heuristic does branch and cut on given problem by just using
variables which have appeared in one or more solutions. It is obviously
only tried after two or more solutions have been found. Value 'on'
means to use the heuristic in each node of the tree, i.e. after preprocessing.
Value 'before' means use the heuristic only if option doHeuristics
is used. Value 'both' means to use the heuristic if option doHeuristics
is used and during solve.
<Possible options for combineSolutions are: off on both before onquick bothquick beforequick;
	current  off>

combine2(Solutions) : Whether to use crossover solution heuristic
This heuristic does branch and cut on the problem given by fixing
variables which have the same value in two or more solutions. It obviously
only tries after two or more solutions. Value 'on' means to use the
heuristic in each node of the tree, i.e. after preprocessing. Value
'before' means use the heuristic only if option doHeuristics is used.
Value 'both' means to use the heuristic if option doHeuristics is
used and during solve.
<Possible options for combine2Solutions are: off on both before;
	current  off>

constraint(fromCutoff) : Whether to use cutoff as constraint
For some problems, cut generators and general branching work better
if the problem would be infeasible if the cost is too high. If this
option is enabled, the objective function is added as a constraint
which right hand side is set to the current cutoff value (objective
value of best known solution)
<Possible options for constraintfromCutoff are: off on variable forcevariable conflict;
	current  off>

cost(Strategy) : How to use costs for branching priorities
Value 'priorities' assigns highest priority to variables with largest
absolute cost. This primitive strategy can be surprisingly effective.
Value 'columnorder' assigns the priorities 1, 2, 3, ... with respect
to the column ordering. Value '01first' ('01last') assignes two sets
of priorities such that binary variables get high (low) priority.
Value 'length' assigns high priority to variables that occur in many
equations. 
<Possible options for costStrategy are: off pri(orities) column(Order?) 01f(irst?) 01l(ast?) length(?) singletons nonzero general(Force?);
	current  off>

cplex(Use) : Whether to use Cplex!
If the user has Cplex, but wants to use some of Cbc's heuristics then
you can!  If this is on, then Cbc will get to the root node and then
hand over to Cplex.  If heuristics find a solution this can be significantly
quicker.  You will probably want to switch off Cbc's cuts as Cplex
thinks they are genuine constraints.  It is also probable that you
want to switch off preprocessing, although for difficult problems
it is worth trying both.
<Possible options for cplexUse are: off on;
	current  off>

cuts(OnOff) : Switches all cut generators on or off
This can be used to switch on or off all cut generators (apart from
Reduce and Split). Then one can turn individual ones off or on. Value
'on' enables the cut generator and CBC will try it in the branch and
cut tree (see cutDepth on how to fine tune the behavior). Value 'root'
lets CBC run the cut generator generate only at the root node. Value
'ifmove' lets CBC use the cut generator in the tree if it looks as
if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
<Possible options for cutsOnOff are: off on root ifmove forceOn;
	current  on>

Dins : Whether to try Distance Induced Neighborhood Search
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for Dins are: off on both before often;
	current  off>

DivingS(ome) : Whether to try Diving heuristics
This switches on a random diving heuristic at various times. One may
prefer to individually turn diving heuristics on or off. Value 'on'
means to use the heuristic in each node of the tree, i.e. after preprocessing.
Value 'before' means use the heuristic only if option doHeuristics
is used. Value 'both' means to use the heuristic if option doHeuristics
is used and during solve.
<Possible options for DivingSome are: off on both before;
	current  off>

DivingC(oefficient) : Whether to try Coefficient diving heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for DivingCoefficient are: off on both before;
	current  on>

DivingF(ractional) : Whether to try Fractional diving heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for DivingFractional are: off on both before;
	current  off>

DivingG(uided) : Whether to try Guided diving heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for DivingGuided are: off on both before;
	current  off>

DivingL(ineSearch) : Whether to try Linesearch diving heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for DivingLineSearch are: off on both before;
	current  off>

DivingP(seudoCost) : Whether to try Pseudocost diving heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for DivingPseudoCost are: off on both before;
	current  off>

DivingV(ectorLength) : Whether to try Vectorlength diving heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for DivingVectorLength are: off on both before;
	current  off>

dw(Heuristic) : Whether to try Dantzig Wolfe heuristic
This heuristic is very very compute intensive. It tries to find a
Dantzig Wolfe structure and use that.Value 'on' means to use the heuristic
in each node of the tree, i.e. after preprocessing. Value 'before'
means use the heuristic only if option doHeuristics is used. Value
'both' means to use the heuristic if option doHeuristics is used and
during solve.
<Possible options for dwHeuristic are: off on both before;
	current  off>

feas(ibilityPump) : Whether to try the Feasibility Pump heuristic
This heuristic is due to Fischetti, Glover, and Lodi and uses a sequence
of LPs to try and get an integer feasible solution. Some fine tuning
is available by options passFeasibilityPump and pumpTune. Value 'on'
means to use the heuristic in each node of the tree, i.e. after preprocessing.
Value 'before' means use the heuristic only if option doHeuristics
is used. Value 'both' means to use the heuristic if option doHeuristics
is used and during solve.
<Possible options for feasibilityPump are: off on both before;
	current  on>

flow(CoverCuts) : Whether to use Flow Cover cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
Reference: https://github.com/coin-or/Cgl/wiki/CglFlowCover
<Possible options for flowCoverCuts are: off on root ifmove forceOn onglobal;
	current  ifmove>

GMI(Cuts) : Whether to use alternative Gomory cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
This version is by Giacomo Nannicini and may be more robust than gomoryCuts.
<Possible options for GMICuts are: off on root ifmove forceOn endonly long longroot longifmove forceLongOn longendonly;
	current  off>

gomory(Cuts) : Whether to use Gomory cuts
The original cuts - beware of imitations!  Having gone out of favor,
they are now more fashionable as LP solvers are more robust and they
interact well with other cuts.  They will almost always give cuts
(although in this executable they are limited as to number of variables
in cut).  However the cuts may be dense so it is worth experimenting
(Long allows any length). Value 'on' enables the cut generator and
CBC will try it in the branch and cut tree (see cutDepth on how to
fine tune the behavior). Value 'root' lets CBC run the cut generator
generate only at the root node. Value 'ifmove' lets CBC use the cut
generator in the tree if it looks as if it is doing some good and
moves the objective value. Value 'forceon' turns on the cut generator
and forces CBC to use it at every node. Reference: https://github.com/coin-or/Cgl/wiki/CglGomory
<Possible options for gomoryCuts are: off on root ifmove forceOn onglobal forceandglobal forceLongOn long;
	current  ifmove>

greedy(Heuristic) : Whether to use a greedy heuristic
This heuristic tries to obtain a feasible solution by just fixing
a percentage of variables and then try a small branch and cut run.
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for greedyHeuristic are: off on both before;
	current  on>

heur(isticsOnOff) : Switches most primal heuristics on or off
This option can be used to switch on or off all heuristics that search
for feasible solutions,      except for the local tree search, as
it dramatically alters the search.      Then individual heuristics
can be turned off or on.
<Possible options for heuristicsOnOff are: off on;
	current  on>

knapsack(Cuts) : Whether to use Knapsack cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
Reference: https://github.com/coin-or/Cgl/wiki/CglKnapsackCover
<Possible options for knapsackCuts are: off on root ifmove forceOn onglobal forceandglobal;
	current  ifmove>

lagomory(Cuts) : Whether to use Lagrangean Gomory cuts
This is a gross simplification of 'A Relax-and-Cut Framework for Gomory's
Mixed-Integer Cuts' by Matteo Fischetti & Domenico Salvagnin.  This
simplification just uses original constraints while modifying objective
using other cuts. So you don't use messy constraints generated by
Gomory etc. A variant is to allow non messy cuts e.g. clique cuts.
So 'only' does this while 'clean' also allows integral valued cuts.
'End' is recommended and waits until other cuts have finished before
it does a few passes. The length options for gomory cuts are used.
<Possible options for lagomoryCuts are: off endonlyroot endcleanroot root endonly endclean endboth onlyaswell cleanaswell bothaswell onlyinstead cleaninstead bothinstead onlyaswellroot cleanaswellroot bothaswellroot;
	current  off>

latwomir(Cuts) : Whether to use Lagrangean TwoMir cuts
This is a Lagrangean relaxation for TwoMir cuts.  See   lagomoryCuts
for description of options.
<Possible options for latwomirCuts are: off endonlyroot endcleanroot endbothroot endonly endclean endboth onlyaswell cleanaswell bothaswell onlyinstead cleaninstead bothinstead;
	current  off>

lift(AndProjectCuts) : Whether to use Lift and Project cuts
These cuts may be expensive to compute. Value 'on' enables the cut
generator and CBC will try it in the branch and cut tree (see cutDepth
on how to fine tune the behavior). Value 'root' lets CBC run the cut
generator generate only at the root node. Value 'ifmove' lets CBC
use the cut generator in the tree if it looks as if it is doing some
good and moves the objective value. Value 'forceon' turns on the cut
generator and forces CBC to use it at every node. Reference: https://github.com/coin-or/Cgl/wiki/CglLandP
<Possible options for liftAndProjectCuts are: off on root ifmove forceOn;
	current  off>

local(TreeSearch) : Whether to use local tree search when a solution is found
The heuristic is from Fischetti and Lodi and is not really a heuristic
although it can be used as one (with limited functionality).  It is
not switched on when heuristics are switched on.
<Possible options for localTreeSearch are: off on;
	current  off>

mixed(IntegerRoundingCuts) : Whether to use Mixed Integer Rounding cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
Reference: https://github.com/coin-or/Cgl/wiki/CglMixedIntegerRounding2
<Possible options for mixedIntegerRoundingCuts are: off on root ifmove forceOn onglobal;
	current  ifmove>

node(Strategy) : What strategy to use to select the next node from the branch and cut tree
Normally before a feasible solution is found, CBC will choose a node
with fewest infeasibilities.   Alternatively, one may choose tree-depth
as the criterion. This requires the minimal amount of memory, but
may take a long time to find the best solution.  Additionally, one
may specify whether up or down branches must be selected first (the
up-down choice will carry on after a first solution has been bound).
The default choice 'hybrid' does breadth first on small depth nodes
and then switches to 'fewest'.
<Possible options for nodeStrategy are: hybrid fewest depth upfewest downfewest updepth downdepth;
	current  fewest>

PrepN(ames) : If column names will be kept in pre-processed model
Normally the preprocessed model has column names replaced by new names
C0000...Setting this option to on keeps original names in variables
which still exist in the preprocessed problem
<Possible options for PrepNames are: off on;
	current  off>

pivotAndC(omplement) : Whether to try Pivot and Complement heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for pivotAndComplement are: off on both before;
	current  off>

pivotAndF(ix) : Whether to try Pivot and Fix heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for pivotAndFix are: off on both before;
	current  off>

preprocess : Whether to use integer preprocessing
This tries to reduce size of model in a similar way to presolve and
it also tries to strengthen the model - this can be very useful and
is worth trying.  Value 'save' saves the presolved problem to a file
presolved.mps. Value 'equal' will turn inequality-cliques into equalities.
Value 'sos' lets CBC search for rows with upper bound 1 and where
all nonzero coefficients are 1 and creates special ordered sets if
the sets are not overlapping and all integer variables (except for
at most one) are in the sets. Value 'trysos' is same as 'sos', but
allows any number of integer variables outside of sets. Value 'equalall'
lets CBC turn all valid inequalities into equalities by adding integer
slack variables.
<Possible options for preprocess are: off on save equal sos trysos equalall strategy aggregate forcesos stop(aftersaving);
	current  sos>

probing(Cuts) : Whether to use Probing cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
Value 'forceOnBut' turns on probing and forces CBC to do probing at
every node, but does only probing, not strengthening etc.     Value
'strong' forces CBC to strongly do probing at every node, that is,
also when CBC would usually turn it off because it hasn't found something.
Value 'forceonbutstrong' is like 'forceonstrong', but does only probing
(column fixing) and turns off row strengthening, so the matrix will
not change inside the branch and bound.     Reference: https://github.com/coin-or/Cgl/wiki/CglProbing
<Possible options for probingCuts are: off on root ifmove forceOn onglobal forceonglobal forceOnBut forceOnStrong forceOnButStrong strongRoot;
	current  on>

proximity(Search) : Whether to do proximity search heuristic
This heuristic looks for a solution close to the incumbent solution
(Fischetti and Monaci, 2012). The idea is to define a sub-MIP without
additional constraints but with a modified objective function intended
to attract the search in the proximity of the incumbent. The approach
works well for 0-1 MIPs whose solution landscape is not too irregular
(meaning the there is reasonable probability of finding an improved
solution by flipping a small number of binary variables), in particular
when it is applied to the first heuristic solutions found at the root
node. Value 'on' means to use the heuristic in each node of the tree,
i.e. after preprocessing. Value 'before' means use the heuristic only
if option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for proximitySearch are: off on both before 10 100 300;
	current  off>

randomi(zedRounding) : Whether to try randomized rounding heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for randomizedRounding are: off on both before;
	current  off>

reduce(AndSplitCuts) : Whether to use Reduce-and-Split cuts
These cuts may be expensive to generate. Value 'on' enables the cut
generator and CBC will try it in the branch and cut tree (see cutDepth
on how to fine tune the behavior). Value 'root' lets CBC run the cut
generator generate only at the root node. Value 'ifmove' lets CBC
use the cut generator in the tree if it looks as if it is doing some
good and moves the objective value. Value 'forceon' turns on the cut
generator and forces CBC to use it at every node. Reference: https://github.com/coin-or/Cgl/wiki/CglRedSplit
<Possible options for reduceAndSplitCuts are: off on root ifmove forceOn;
	current  off>

reduce2(AndSplitCuts) : Whether to use Reduce-and-Split cuts - style 2
This switches on reduce and split  cuts (either at root or in entire
tree). This version is by Giacomo Nannicini based on Francois Margot's
version. Standard setting only uses rows in tableau <= 256, long uses
all. These cuts may be expensive to generate. See option cuts for
more information on the possible values.
<Possible options for reduce2AndSplitCuts are: off on root longOn longRoot;
	current  off>

residual(CapacityCuts) : Whether to use Residual Capacity cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
Reference: https://github.com/coin-or/Cgl/wiki/CglResidualCapacity
<Possible options for residualCapacityCuts are: off on root ifmove forceOn;
	current  off>

Rens : Whether to try Relaxation Enforced Neighborhood Search
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve. Value 'on' just does
50 nodes. 200, 1000, and 10000 does that many nodes.
<Possible options for Rens are: off on both before 200 1000 10000 dj djbefore usesolution;
	current  off>

Rins : Whether to try Relaxed Induced Neighborhood Search
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for Rins are: off on both before often;
	current  on>

round(ingHeuristic) : Whether to use simple (but effective) Rounding heuristic
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for roundingHeuristic are: off on both before;
	current  on>

sosO(ptions) : Whether to use SOS from AMPL
Normally if AMPL says there are SOS variables they should be used,
but sometime sthey should be turned off - this does so.
<Possible options for sosOptions are: off on;
	current  on>

sosP(rioritize) : How to deal with SOS priorities
This sets priorities for SOS.  Values 'high' and 'low' just set a
priority     relative to the for integer variables.  Value 'orderhigh'
gives first highest priority to the first SOS and integer variables
a low priority.  Value 'orderlow' gives integer variables a high priority
then SOS in order.
<Possible options for sosPrioritize are: off high low orderhigh orderlow;
	current  off>

two(MirCuts) : Whether to use Two phase Mixed Integer Rounding cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
Reference: https://github.com/coin-or/Cgl/wiki/CglTwomir
<Possible options for twoMirCuts are: off on root ifmove forceOn onglobal forceandglobal forceLongOn;
	current  root>

Vnd(VariableNeighborhoodSearch) : Whether to try Variable Neighborhood Search
Value 'on' means to use the heuristic in each node of the tree, i.e.
after preprocessing. Value 'before' means use the heuristic only if
option doHeuristics is used. Value 'both' means to use the heuristic
if option doHeuristics is used and during solve.
<Possible options for VndVariableNeighborhoodSearch are: off on both before intree;
	current  off>

zero(HalfCuts) : Whether to use zero half cuts
Value 'on' enables the cut generator and CBC will try it in the branch
and cut tree (see cutDepth on how to fine tune the behavior). Value
'root' lets CBC run the cut generator generate only at the root node.
Value 'ifmove' lets CBC use the cut generator in the tree if it looks
as if it is doing some good and moves the objective value. Value 'forceon'
turns on the cut generator and forces CBC to use it at every node.
This implementation was written by Alberto Caprara.
<Possible options for zeroHalfCuts are: off on root ifmove forceOn onglobal;
	current  ifmove>

allS(lack) : Set basis back to all slack and reset solution
Mainly useful for tuning purposes.  Normally the first dual or primal
will be using an all slack basis anyway.

barr(ier) : Solve using primal dual predictor corrector algorithm
This command solves the current model using the  primal dual predictor
corrector algorithm.  You may want to link in an alternative ordering
and factorization.  It will also solve models with quadratic objectives.

basisI(n) : Import basis from bas file
This will read an MPS format basis file from the given file name.
It will use the default directory given by 'directory'.  A name of
'$' will use the previous value for the name.  This is initialized
to '', i.e. it must be set.  If you have libz then it can read compressed
files 'xxxxxxxx.gz' or xxxxxxxx.bz2.

basisO(ut) : Export basis as bas file
This will write an MPS format basis file to the given file name. 
It will use the default directory given by 'directory'.  A name of
'$' will use the previous value for the name.  This is initialized
to 'default.bas'.

directory : Set Default directory for import etc.
This sets the directory which import, export, saveModel, restoreModel
etc will use.  It is initialized to './'

dualS(implex) : Do dual simplex algorithm
This command solves the continuous relaxation of the current model
using the dual steepest edge algorithm.The time and iterations may
be affected by settings such as presolve, scaling, crash and also
by dual pivot method, fake bound on variables and dual and primal
tolerances.

either(Simplex) : Do dual or primal simplex algorithm
This command solves the continuous relaxation of the current model
using the dual or primal algorithm, based on a dubious analysis of
model.

end : Stops clp execution
This stops execution ; end, exit, quit and stop are synonyms

exit : Stops clp execution
This stops the execution of Clp, end, exit, quit and stop are synonyms

export : Export model as mps file
This will write an MPS format file to the given file name.  It will
use the default directory given by 'directory'.  A name of '$' will
use the previous value for the name.  This is initialized to 'default.mps'.
It can be useful to get rid of the original names and go over to using
Rnnnnnnn and Cnnnnnnn.  This can be done by setting 'keepnames' off
before importing mps file.

gsolu(tion) : Puts glpk solution to file
Will write a glpk solution file to the given file name.  It will use
the default directory given by 'directory'.  A name of '$' will use
the previous value for the name.  This is initialized to 'stdout'
(this defaults to ordinary solution if stdout). If problem created
from gmpl model - will do any reports.

guess : Guesses at good parameters
This looks at model statistics and does an initial solve setting some
parameters which may help you to think of possibilities.

help : Print out version, non-standard options and some help
This prints out some help to get user started.  If you have printed
this then you should be past that stage:-)

import : Import model from mps file
This will read an MPS format file from the given file name.  It will
use the default directory given by 'directory'.  A name of '$' will
use the previous value for the name.  This is initialized to '', i.e.
it must be set.  If you have libgz then it can read compressed files
'xxxxxxxx.gz' or 'xxxxxxxx.bz2'.  If 'keepnames' is off, then names
are dropped -> Rnnnnnnn and Cnnnnnnn.

initialS(olve) : Solve to continuous
This just solves the problem to continuous - without adding any cuts

max(imize) : Set optimization direction to maximize
The default is minimize - use 'maximize' for maximization.
You can also use the parameters 'direction maximize'.

min(imize) : Set optimization direction to minimize
The default is minimize - use 'maximize' for maximization.
This should only be necessary if you have previously set maximization
You can also use the parameters 'direction minimize'.

para(metrics) : Import data from file and do parametrics
This will read a file with parametric data from the given file name
and then do parametrics.  It will use the default directory given
by 'directory'.  A name of '$' will use the previous value for the
name.  This is initialized to '', i.e. it must be set.  This can not
read from compressed files. File is in modified csv format - a line
ROWS will be followed by rows data while a line COLUMNS will be followed
by column data.  The last line should be ENDATA. The ROWS line must
exist and is in the format ROWS, inital theta, final theta, interval
theta, n where n is 0 to get CLPI0062 message at interval or at each
change of theta and 1 to get CLPI0063 message at each iteration. 
If interval theta is 0.0 or >= final theta then no interval reporting.
n may be missed out when it is taken as 0.  If there is Row data then
there is a headings line with allowed headings - name, number, lower(rhs
change), upper(rhs change), rhs(change).  Either the lower and upper
fields should be given or the rhs field. The optional COLUMNS line
is followed by a headings line with allowed headings - name, number,
objective(change), lower(change), upper(change).  Exactly one of name
and number must be given for either section and missing ones have
value 0.0.

primalS(implex) : Do primal simplex algorithm
This command solves the continuous relaxation of the current model
using the primal algorithm.  The default is to use exact devex. The
time and iterations may be affected by settings such as presolve,
scaling, crash and also by column selection  method, infeasibility
weight and dual and primal tolerances.

printM(ask) : Control printing of solution on a  mask
If set then only those names which match mask are printed in a solution.
'?' matches any character and '*' matches any set of characters. 
The default is '' i.e. unset so all variables are printed. This is
only active if model has names.

quit : Stops clp execution
This stops the execution of Clp, end, exit, quit and stop are synonyms

restoreS(olution) : reads solution from file
This will read a binary solution file from the given file name.  It
will use the default directory given by 'directory'.  A name of '$'
will use the previous value for the name.  This is initialized to
'solution.file'.  This reads in a file from saveSolution

saveS(olution) : saves solution to file
This will write a binary solution file to the given file name.  It
will use the default directory given by 'directory'.  A name of '$'
will use the previous value for the name.  This is initialized to
'solution.file'.  To read the file use fread(int) twice to pick up
number of rows and columns, then fread(double) to pick up objective
value, then pick up row activities, row duals, column activities and
reduced costs - see bottom of CbcOrClpParam.cpp for code that reads
or writes file. If name contains '_fix_read_' then does not write
but reads and will fix all variables

solu(tion) : Prints solution to file
This will write a primitive solution file to the given file name.
It will use the default directory given by 'directory'.  A name of
'$' will use the previous value for the name.  This is initialized
to 'stdout'.  The amount of output can be varied using printi!ngOptions
or printMask.

stat(istics) : Print some statistics
This command prints some statistics for the current model. If log
level >1 then more is printed. These are for presolved model if presolve
on (and unscaled).

stop : Stops clp execution
This stops the execution of Clp, end, exit, quit and stop are synonyms

branch(AndCut) : Do Branch and Cut
This does branch and cut.  There are many parameters which can affect
the performance.  First just try with default settings and look carefully
at the log file.  Did cuts help?  Did they take too long?  Look at
output to see which cuts were effective and then do some tuning. 
You will see that the options for cuts are off, on, root and ifmove,
forceon.  Off is obvious. Value 'on' enables the cut generator and
CBC will try it in the branch and cut tree (see cutDepth on how to
fine tune the behavior). Value 'root' lets CBC run the cut generator
generate only at the root node. Value 'ifmove' lets CBC use the cut
generator in the tree if it looks as if it is doing some good and
moves the objective value. Value 'forceon' turns on the cut generator
and forces CBC to use it at every node. For probing, forceonbut just
does fixing probing in tree - not strengthening etc.  If pre-processing
reduced the size of the problem or strengthened many coefficients
then it is probably wise to leave it on.  Switch off heuristics which
did not provide solutions.  The other major area to look at is the
search.  Hopefully good solutions were obtained fairly early in the
search so the important point is to select the best variable to branch
on.  See whether strong branching did a good job - or did it just
take a lot of iterations.  Adjust the strongBranching and trustPseudoCosts
parameters.  If cuts did a good job, then you may wish to have more
rounds of cuts - see passC!uts and passT!ree.

doH(euristic) : Do heuristics before any preprocessing
Normally heuristics are done in branch and bound.  It may be useful
to do them outside. Only those heuristics with 'both' or 'before'
set will run.  Doing this may also set cutoff, which can help with
preprocessing.

mips(tart) : reads an initial feasible solution from file
The MIPStart allows one to enter an initial integer feasible solution
to CBC. Values of the main decision variables which are active (have
non-zero values) in this solution are specified in a text  file. The
text file format used is the same of the solutions saved by CBC, but
not all fields are required to be filled. First line may contain the
solution status and will be ignored, remaining lines contain column
indexes, names and values as in this example:

Stopped on iterations - objective value 57597.00000000
0  x(1,1,2,2)               1 
1  x(3,1,3,2)               1 
5  v(5,1)                   2 
33 x(8,1,5,2)               1 
...

Column indexes are also ignored since pre-processing can change them.
There is no need to include values for continuous or integer auxiliary
variables, since they can be computed based on main decision variables.
Starting CBC with an integer feasible solution can dramatically improve
its performance: several MIP heuristics (e.g. RINS) rely on having
at least one feasible solution available and can start immediately
if the user provides one. Feasibility Pump (FP) is a heuristic which
tries to overcome the problem of taking too long to find feasible
solution (or not finding at all), but it not always succeeds. If you
provide one starting solution you will probably save some time by
disabling FP. 

Knowledge specific to your problem can be considered to write an external
module to quickly produce an initial feasible solution - some alternatives
are the implementation of simple greedy heuristics or the solution
(by CBC for example) of a simpler model created just to find a feasible
solution. 

Silly options added.  If filename ends .low then integers not mentioned
are set low - also .high, .lowcheap, .highcheap, .lowexpensive, .highexpensive
where .lowexpensive sets costed ones to make expensive others low.
Also if filename starts empty. then no file is read at all - just
actions done. 

Question and suggestions regarding MIPStart can be directed to
haroldo.santos@gmail.com. 

nextB(estSolution) : Prints next best saved solution to file
To write best solution, just use solution.  This prints next best
(if exists)  and then deletes it.  This will write a primitive solution
file to the given file name.  It will use the default directory given
by 'directory'.  A name of '$' will use the previous value for the
name.  This is initialized to 'stdout'.  The amount of output can
be varied using printi!ngOptions or printMask.

prio(rityIn) : Import priorities etc from file
This will read a file with priorities from the given file name.  It
will use the default directory given by 'directory'.  A name of '$'
will use the previous value for the name.  This is initialized to
'', i.e. it must be set.  This can not read from compressed files.
File is in csv format with allowed headings - name, number, priority,
direction, up, down, solution.  Exactly one of name and number must
be given.

solv(e) : Solve problem
If there are no integer variables then this just solves LP.  If there
are integer variables this does branch and cut.
```

