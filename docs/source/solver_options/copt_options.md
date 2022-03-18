
# COPT Options

Obtained with `$ copt -=`.

```
barhomogeneous    whether to use homogeneous self-dual form in barrier
bariterlimit      iteration limit of the barrier solver
barthreads        number of threads used by barrier
basis             whether to use or return a basis
bestbound         whether to return bestbound suffix
conflictanalysis  whether to perform conflict analysis
crossoverthreads  number of threads used by crossover
cutlevel          the cutting planes generation level
divingheurlevel   level of diving heuristics
dualize           whether to dualize a problem before solving it
dualperturb       whether to allow the objective function perturbation
dualprice         specifies the dual simplex pricing algorithm
dualtol           the tolerance for dual solutions and reduced cost
feastol           the feasibility tolerance
heurlevel         the heuristics level
inttol            the integrality tolerance
logging           whether to print solving logs
lpmethod          method to solve the LP problem
matrixtol         input matrix coefficient tolerance
mipstart          whether to use initial guesses in MIP problem
miptasks          number of MIP tasks in parallel
nodecutrounds     rounds of cutting-planes generation of tree node
nodelimit         node limit of the optimization
objno             objective number to solve
poolsolutions     number of alternative MIP solutions written
poolstub          name prefix for alternative MIP solutions written
presolve          whether to perform persolving before solving a problem
relgap            the relative MIP gap
retmipgap         whether to return relmipgap and absmipgap suffix
rootcutlevel      level of cutting-planes generation of root node
rootcutrounds     rounds of cutting-planes generation of root node
scaling           whether to perform scaling before solving a problem
simplexthreads    number of threads used by dual simplex
sos               whether to recognize suffixes '.sosno' and '.ref'
sos2              whether to use SOS2 sets from nonconvex PWL terms
strongbranching   level of strong branching
submipheurlevel   level of Sub-MIP heuristics
threads           number of threads to use
timelimit         time limit of the optimization
treecutlevel      level of cutting-planes generation of search tree
wantsol           whether to write .sol file

```

