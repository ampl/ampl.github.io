Solve result table for Gurobi 13.0.3
          0- 99 solved: optimal for an optimization problem,
                feasible for a satisfaction problem 
        100-199 solved? solution candidate returned but error likely 
            120 locally optimal solution
            150 solved? MP solution check failed (option sol:chk:fail) 
        200-299 infeasible 
            220 locally infeasible solution
        300-349 unbounded, feasible solution returned 
        350-399 unbounded, no feasible solution returned 
        400-449 limit, feasible: stopped, e.g., on iterations or Ctrl-C 
            401 interrupted, feasible solution
            402 time limit, feasible solution
            403 iteration limit, feasible solution
            404 node limit, feasible solution
            405 bestobjstop or bestbndstop reached, feasible solution
            408 solution limit
            409 work limit, feasible solution
            410 soft memory limit, feasible solution
        450-469 limit, problem is either infeasible or unbounded.
                Disable dual reductions or run IIS finder for definitive answer.
        470-499 limit, no solution returned 
            471 interrupted, without a feasible solution
            472 time limit, without a feasible solution
            473 iteration limit, without a feasible soluton
            474 node limit, without a feasible soluton
            475 objective cutoff
            477 bestbndstop reached, without a feasible solution
            479 work limit, without a feasible solution
            480 soft memory limit, without a feasible solution
        500-999 failure, no solution returned 
            550 failure: numeric issue, no feasible solution
            601 Could not talk to Gurobi Instant Cloud or Gurobi Server.
            602 Job rejected by Gurobi Instant Cloud or Gurobi Server.
            603 No license for specified Gurobi Instant Cloud or Gurobi Server.
            604 Surprise failure while starting the cloud/server environment.
            605 Bad value for cloudid or cloudkey, or Gurobi Cloud out of reach.
