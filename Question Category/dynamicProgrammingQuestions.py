"""
Dynamic Programming is an algorithmic paradigm that solves a given
complex problem by breaking it into subproblems and stores the results
of subproblems to avoid computing the same results again.
If a problem can be solved using DP, usually has such two main properties:
    1. Overlapping Subproblems (BST is not a DP problem since it don't has common problems)
    2. Optimal Substructure
"""
"""
I. For overlapping problem, we have:
    a. Memoization (Top Down): Initialize a lookup table with nil values, whenevert we need
        solution to a subproblem, we first look into the lookup table before calculate, it
        the value not there, we calculate and put the result into table
    b. Tabulation (Bottom Up): build a table by filling entries one by one
II.For Optimal Substructure: f optimal solution of the given problem can be obtained
   by using optimal solutions of its subproblems.
   A shortest path problem can use this way, but longest path cannot
