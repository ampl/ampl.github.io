# AMPL Suffixes

To represent values associated with an entity, AMPL employs various qualifiers or _suffixes_ appended to entity names. A suffix consists of a period or "dot" (.) followed by a (usually short) identifier, so that for example the reduced cost associated with a variable Buy[j] is written Buy[j].rc, and the reduced costs of all such variables can be viewed by giving the command display Buy.rc. There are numerous built-in suffixes of this kind, available for use in any AMPL session; see our tables of _built-in_ suffixes for details below.

AMPL cannot anticipate all of the values that a solver might associate with model components, however. The values recognized (as input) or computed (as output) depend on the design of each solver and its algorithms. To provide for the representation of these values, the concept of a suffix has been extended to permit the definition of new suffixes for the duration of an AMPL session.

The following section shows all built-in suffixes of AMPL.

## Built-in Suffixes

### Variables

| Suffixes | Interpretation |
| --- | --- |
| .astatus | AMPL status (fixed, presolved, or substituted out) |
| .defeqn | Index in \_con of "defining constraint" used to substitute variable out |
| .dual | Dual value on defining constraint of variable substituted out |
| .init | Current initial guess |
| .init0 | Original initial guess (set by := or default or by a data statement) |
| .lb | Current lower bounds |
| .lb0 | Initial lower bounds, from the var declaration |
| .lb1 | Weaker lower bounds from AMPL's presolve phase |
| .lb2 | Stronger lower bounds from AMPL's presolve phase |
| .lrc | Reduced costs at lower bounds |
| .lslack | Slacks at lower bounds (val - lb) |
| .rc | Reduced cost (at the nearer bound) |
| .relax | Ignore integrality restriction if positive |
| .slack | Bound slack (the lesser of lslack and uslack) |
| .sstatus | Solver status (basis status of variable) |
| .status | AMPL status if not "in", otherwise solver status |
| .ub | Current upper bounds |
| .ub0 | Initial upper bounds, from the var declaration |
| .ub1 | Weaker upper bounds from AMPL's presolve phase |
| .ub2 | Stronger upper bounds from AMPL's presolve phase |
| .urc | Reduced costs at upper bounds |
| .uslack | Slacks at upper bounds (ub - val) |
| .val | Current value |

### Constraints

To define these values unambiguously, all constraints are assumed to be put in the form _lower bound_ <= _body_ <= _upper bound_, where the the constraint body contains all terms involving variables, and the bounds are constants.

| Suffixes | Interpretation |
| --- | --- |
| .astatus | AMPL status (dropped, presolved, or substituted out) |
| .body | Current value of constraint body |
| .defvar | Index in \_var of "defined variable" substituted out by the constraint |
| .dinit | Current initial guess for the constraint's dual variable |
| .dinit0 | Original initial guess for the constraint's dual variable |
| .dual | Current value of the constraint's dual variable |
| .lb | Constraint lower bounds |
| .lbs | Constraint lower bounds sent to solver (reflecting adjustments for fixed variables) |
| .ldual | Current dual values associated with lower bounds |
| .lslack | Slacks at lower bounds (body - lb) |
| .slack | Constraint slack (the lesser of lslack and uslack) |
| .sstatus | Solver status (basis status of constraint's slack or artificial variable) |
| .status | AMPL status if not "in", otherwise solver status |
| .ub | Constraint upper bounds |
| .ubs | Constraint upper bounds sent to solver (reflecting adjustments for fixed variables) |
| .udual | Current dual values associated with upper bounds |
| .uslack | Slacks at lower & upper bounds (ub - body) |

### Objectives

| Suffixes | Interpretation |
| --- | --- |
| .astatus | AMPL status |
| .exitcode | Exit code returned by solver after most recent solve with this objective |
| .message | Result message returned by solver after most recent solve with this objective |
| .result | Result string returned by solver after most recent solve with this objective |
| .val | Current value |

### Problems

| Suffixes | Interpretation |
| --- | --- |
| .astatus | AMPL status |
| .exitcode | Exit code returned by solver after most recent solve of this problem |
| .message | Result message returned by solver after most recent solve of this problem |
| .result | Result string returned by solver after most recent solve of this problem |
